"""Check that the reordering activity can be solved by dragging, with a mouse and
with touch, and that the arrow buttons still work.

  python3 tools/drag_test.py out/lesson04.html ...
"""
import asyncio, os, sys
from playwright.async_api import async_playwright


async def order_task(pg):
    """Index of the first `order` activity, or None."""
    return await pg.evaluate("""() => {
      const C = window.LESSON; if (!C) return null;
      const i = C.practice.findIndex(t => t.type === 'order');
      return i < 0 ? null : i;
    }""")


async def rows(pg, ti):
    return await pg.evaluate("""(ti) => [...document.querySelectorAll(`#ol${ti} li`)]
        .map(li => li.querySelector('.t').textContent.replace(/\\s*·\\s*\\S+$/, '').trim())""", ti)


async def want(pg, ti):
    return await pg.evaluate(
        "(ti) => window.LESSON.practice[ti].items.map(i => i[0].replace(/<[^>]+>/g, '').trim())", ti)


async def box(pg, ti, idx, sel, edge=None):
    """Center of a row (or its grip). `edge` aims just inside the top/bottom instead:
    dropping exactly on a row's midpoint is ambiguous and lands one slot off."""
    return await pg.evaluate("""([ti, idx, sel, edge]) => {
      const li = document.querySelectorAll(`#ol${ti} li`)[idx];
      const r = (sel ? li.querySelector(sel) : li).getBoundingClientRect();
      const y = edge === 'top' ? r.top + 3 : edge === 'bottom' ? r.bottom - 3 : r.y + r.height / 2;
      return {x: r.x + r.width / 2, y};
    }""", [ti, idx, sel, edge])


async def settle(pg, ti):
    """Bring the list into view and wait out the page's smooth scrolling."""
    await pg.evaluate("(ti) => document.getElementById('ol' + ti).scrollIntoView({block: 'center'})", ti)
    await pg.evaluate("""async () => {
      let last = -1, same = 0;
      for (let i = 0; i < 80 && same < 3; i++) {
        await new Promise(r => requestAnimationFrame(() => setTimeout(r, 16)));
        same = window.scrollY === last ? same + 1 : 0; last = window.scrollY;
      }
    }""")


async def drag(pg, ti, frm, to, touch):
    """Drag row `frm` onto row `to`, grabbing the card itself (not a handle)."""
    await settle(pg, ti)
    a = await box(pg, ti, frm, ".t")
    b = await box(pg, ti, to, None, "top" if frm > to else "bottom")
    if touch:
        # press and hold past the 180ms threshold, then move
        await pg.evaluate("""async ([ti, frm, ax, ay, bx, by]) => {
          const li = document.querySelectorAll(`#ol${ti} li`)[frm];
          const ev = (type, x, y) => li.dispatchEvent(new PointerEvent(type, {
            pointerId: 7, pointerType: 'touch', isPrimary: true, bubbles: true,
            cancelable: true, clientX: x, clientY: y}));
          ev('pointerdown', ax, ay);
          await new Promise(r => setTimeout(r, 260));   // let the hold timer fire
          const steps = 10;
          for (let s = 1; s <= steps; s++) {
            ev('pointermove', ax + (bx - ax) * s / steps, ay + (by - ay) * s / steps);
            await new Promise(r => requestAnimationFrame(r));
          }
          ev('pointerup', bx, by);
        }""", [ti, frm, a["x"], a["y"], b["x"], b["y"]])
    else:
        await pg.mouse.move(a["x"], a["y"])
        await pg.mouse.down()
        await pg.mouse.move(a["x"], a["y"] + 6)        # exceed the 3px start threshold
        for s in range(1, 11):
            await pg.mouse.move(a["x"] + (b["x"] - a["x"]) * s / 10,
                                a["y"] + (b["y"] - a["y"]) * s / 10)
        await pg.mouse.up()
    await pg.wait_for_timeout(260)                      # the 170ms drop animation, then commit


async def midair(pg, ti, touch):
    """Hold a card mid-drag and confirm it is lifted and the neighbour has moved aside."""
    await settle(pg, ti)
    a = await box(pg, ti, 0, ".t")
    step = await pg.evaluate("""(ti) => {
      const l = document.querySelectorAll(`#ol${ti} li`);
      const r0 = l[0].getBoundingClientRect(), r1 = l[1].getBoundingClientRect();
      return r1.top - r0.top;
    }""", ti)
    dist = step * 1.3
    probe = """(ti) => {
      const lis = [...document.querySelectorAll(`#ol${ti} li`)];
      const ty = el => { const m = /translateY\\(([-\\d.]+)px\\)/.exec(el.style.transform || ''); return m ? +m[1] : 0; };
      return {dragged: lis.filter(l => l.classList.contains('drag')).length,
              sorting: document.getElementById('ol' + ti).classList.contains('sorting'),
              liftedBy: ty(lis[0]), neighbourMoved: ty(lis[1])};
    }"""
    if touch:
        await pg.evaluate("""async ([ti, ax, ay, dist]) => {
          const li = document.querySelectorAll(`#ol${ti} li`)[0];
          const ev = (t, y) => li.dispatchEvent(new PointerEvent(t, {pointerId: 9, pointerType: 'touch',
            isPrimary: true, bubbles: true, cancelable: true, clientX: ax, clientY: y}));
          ev('pointerdown', ay);
          await new Promise(r => setTimeout(r, 260));
          for (let s = 1; s <= 8; s++) { ev('pointermove', ay + dist * s / 8); await new Promise(r => requestAnimationFrame(r)); }
        }""", [ti, a["x"], a["y"], dist])
        state = await pg.evaluate(probe, ti)
        await pg.evaluate("""([ti, ax, ay, dist]) => {
          const li = document.querySelectorAll(`#ol${ti} li`)[0];
          li.dispatchEvent(new PointerEvent('pointerup', {pointerId: 9, pointerType: 'touch',
            isPrimary: true, bubbles: true, cancelable: true, clientX: ax, clientY: ay + dist}));
        }""", [ti, a["x"], a["y"], dist])
    else:
        await pg.mouse.move(a["x"], a["y"])
        await pg.mouse.down()
        for s in range(1, 9):
            await pg.mouse.move(a["x"], a["y"] + dist * s / 8)
        state = await pg.evaluate(probe, ti)
        await pg.mouse.up()
    await pg.wait_for_timeout(260)
    return state


async def solve_by_drag(pg, ti, touch):
    target = await want(pg, ti)
    for pos in range(len(target)):
        for _ in range(len(target) + 1):
            cur = await rows(pg, ti)
            if cur[pos] == target[pos]:
                break
            at = cur.index(target[pos], pos)
            await drag(pg, ti, at, pos, touch)
    return await rows(pg, ti)


async def run(path, touch):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 390, "height": 1600},
                              has_touch=touch, is_mobile=touch)
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto("file://" + os.path.abspath(path))
        await pg.wait_for_timeout(350)
        await pg.evaluate("localStorage.clear()")
        await pg.reload()
        await pg.wait_for_timeout(350)
        ti = await order_task(pg)
        if ti is None:
            print(f"  {os.path.basename(path)}: no order activity, skipped")
            await b.close()
            return 0
        start = await rows(pg, ti)

        # the arrow buttons must keep working alongside dragging
        await settle(pg, ti)
        await pg.evaluate("""(ti) => document.querySelectorAll(`#ol${ti} li`)[1]
            .querySelector('button[data-d="-1"]').click()""", ti)
        await pg.wait_for_timeout(100)
        swapped = await rows(pg, ti)
        arrows_ok = swapped[0] == start[1] and swapped[1] == start[0]
        await pg.evaluate("""(ti) => document.querySelectorAll(`#ol${ti} li`)[0]
            .querySelector('button[data-d="1"]').click()""", ti)
        await pg.wait_for_timeout(100)

        mid = await midair(pg, ti, touch)
        live_ok = (mid["dragged"] == 1 and mid["sorting"] and mid["liftedBy"] > 20
                   and mid["neighbourMoved"] != 0)
        print(f"        mid-drag: card lifted {mid['liftedBy']:.0f}px, "
              f"neighbour shifted {mid['neighbourMoved']:.0f}px, sorting={mid['sorting']}")

        final = await solve_by_drag(pg, ti, touch)
        target = await want(pg, ti)
        await pg.evaluate("(ti) => document.getElementById('chk' + ti).click()", ti)
        await pg.wait_for_timeout(150)
        fb = await pg.evaluate("(ti) => document.getElementById('fb' + ti).textContent", ti)
        ok = final == target and fb.startswith("All ") and arrows_ok and live_ok and not errs
        print(f"  {'PASS' if ok else 'FAIL'} {os.path.basename(path)} "
              f"({'touch' if touch else 'mouse'}): scrambled->solved by drag, {fb!r}")
        if not ok:
            print(f"        arrows_ok={arrows_ok} live_ok={live_ok}\n        start={start}\n        final={final}\n        want ={target}\n        errors={errs}")
        await pg.evaluate("localStorage.clear()")
        await b.close()
        return 0 if ok else 1


async def main(paths):
    bad = 0
    for f in paths:
        for touch in (False, True):
            bad += await run(f, touch)
    print("drag_test:", "OK" if not bad else f"{bad} failure(s)")
    return bad


sys.exit(1 if asyncio.run(main(sys.argv[1:])) else 0)
