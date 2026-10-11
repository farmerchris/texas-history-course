L = dict(
  slug='lesson01', key='tx-lesson1-v1', n=1, label='Lesson 1',
  title="Eras, Dates & the Historian's Toolkit",
  title_tag='Texas Eras Lesson 1',
  eyebrow='Lesson 1 of 17',
  question='Why do historians divide Texas history into eras?',
  minutes=90,
  teks=['1A', '1B', '20A', '20B', '21A'],
  teks_text='TEKS 7.1A, 7.1B, 7.20A, 7.20B, 7.21A',
  read='''<h2>Cutting a long story into chapters</h2>
  <div class="prose">
    <p>People have lived in the land we call Texas for more than 13,000 years. That is far too much to study all at once. So historians do what authors do with a long book: they split it into chapters. In history, those chapters are called <b>eras</b>.</p>
    <p>An era is a stretch of time with <b>defining characteristics</b>, things that were true for most of that period. During the Spanish Colonial era, for example, Spain ruled Texas and built missions, forts called presidios, and ranches. When Mexico won its independence in 1821, the rules changed, so a new era began.</p>
    <p>Eras help us see <b>change over time</b>. When you can name the era, you can ask good questions: Who was in charge? How did people make a living? What changed from the era before?</p>
    <div class="callout"><b>Historians disagree about edges.</b> Did the Civil Rights era start in 1945 or 1954? Different books draw the lines differently. The dates below are approximate. What matters most is the big change that separates one era from the next.</div>
  </div>

  <h3>The 12 eras of Texas history</h3>
  <div class="ruler" id="ruler"><div class="era"><div class="yr">Before 1519</div><div><b>Natural Texas and Its People</b><span>American Indian groups such as the Caddo, Jumano, and Karankawa adapt to Texas's very different regions.</span></div></div><div class="era"><div class="yr">1519–1689</div><div><b>Age of Contact</b><span>European explorers like Álvarez de Pineda, Cabeza de Vaca, and La Salle reach Texas.</span></div></div><div class="era"><div class="yr">1690–1821</div><div><b>Spanish Colonial</b><span>Spain builds missions, presidios, towns, and ranches to hold Texas.</span></div></div><div class="era"><div class="yr">1821–1835</div><div><b>Mexican National</b><span>Mexico rules Texas and invites settlers, including Stephen F. Austin's colonists.</span></div></div><div class="era"><div class="yr">1835–1845</div><div><b>Revolution and Republic</b><span>Texans fight for independence and run their own country, the Republic of Texas.</span></div></div><div class="era"><div class="yr">1845–1861</div><div><b>Early Statehood</b><span>Texas joins the United States and grows quickly.</span></div></div><div class="era"><div class="yr">1861–1874</div><div><b>Civil War and Reconstruction</b><span>Texas secedes, fights for the Confederacy, and is rebuilt after the war.</span></div></div><div class="era"><div class="yr">1874–1900</div><div><b>Cotton, Cattle, and Railroads</b><span>Cattle drives, cotton farming, and new railroads spread across the state.</span></div></div><div class="era"><div class="yr">1901–1929</div><div><b>Age of Oil</b><span>The Spindletop gusher starts an oil boom that changes the economy.</span></div></div><div class="era"><div class="yr">1929–1945</div><div><b>Great Depression and World War II</b><span>Hard times, the Dust Bowl, and a world war reshape Texas.</span></div></div><div class="era"><div class="yr">1945–1980</div><div><b>Civil Rights and Conservatism</b><span>Texans fight for equal rights, and political loyalties begin to shift.</span></div></div><div class="era"><div class="yr">1980–today</div><div><b>Contemporary Texas</b><span>Big cities, new technology, and fast population growth.</span></div></div></div>

  <h3>Eight dates every Texan should know</h3>
  <div class="dates" id="dateCards"><div class="date"><span class="yr">1519</span><p>Álvarez de Pineda maps the Texas coast; Spain founds its first settlement on the North American mainland.</p></div><div class="date"><span class="yr">1718</span><p>San Antonio is founded.</p></div><div class="date"><span class="yr">1821</span><p>Mexico, including Texas, wins independence from Spain.</p></div><div class="date"><span class="yr">1836</span><p>Texas declares independence from Mexico.</p></div><div class="date"><span class="yr">1845</span><p>Texas is annexed and becomes a U.S. state.</p></div><div class="date"><span class="yr">1861</span><p>The Civil War begins; Texas has seceded.</p></div><div class="date"><span class="yr">1876</span><p>Texans adopt the state constitution still used today.</p></div><div class="date"><span class="yr">1901</span><p>Oil gushes at Spindletop near Beaumont.</p></div></div>

  <h3>The historian's toolkit: two kinds of sources</h3>
  <div class="ps">
    <div><b>Primary source</b><p>Made by someone who was there, at the time. Letters, diaries, photographs, laws, maps, and interviews with eyewitnesses are primary sources.</p><p class="small">Example: William B. Travis's letter written inside the Alamo in 1836.</p></div>
    <div><b>Secondary source</b><p>Made later by someone who studied the event but did not see it. Textbooks, encyclopedia articles, and most documentaries are secondary sources.</p><p class="small">Example: an encyclopedia article about the Alamo written in 1990.</p></div>
  </div>
  <div class="prose"><p>A quick test: <b>Was the creator there when it happened?</b> If yes, it is primary. If they learned about it afterward, it is secondary. Both are useful. Primary sources give you evidence; secondary sources help explain it.</p></div>''',
  practice=[{'type': 'order',
  'title': 'Put the eras in order',
  'intro': 'Drag the cards, or use the arrows, to move each era. Earliest goes at the top.',
  'button': 'Check my order',
  'word': 'in the right spot',
  'items': [['Natural Texas and Its People', 'Before 1519'],
            ['Age of Contact', '1519–1689'],
            ['Spanish Colonial', '1690–1821'],
            ['Mexican National', '1821–1835'],
            ['Revolution and Republic', '1835–1845'],
            ['Early Statehood', '1845–1861'],
            ['Civil War and Reconstruction', '1861–1874'],
            ['Cotton, Cattle, and Railroads', '1874–1900'],
            ['Age of Oil', '1901–1929'],
            ['Great Depression and World War II', '1929–1945'],
            ['Civil Rights and Conservatism', '1945–1980'],
            ['Contemporary Texas', '1980–today']]},
 {'type': 'match',
  'title': 'Match each date to what happened',
  'intro': 'Pick the event for each year.',
  'placeholder': 'Choose an event…',
  'button': 'Check my matches',
  'word': 'correct',
  'options': ['Texas independence',
              'Annexation to the U.S.',
              'Pineda maps the coast',
              'Spindletop oil discovery',
              'Current constitution adopted',
              'Civil War begins',
              'San Antonio is founded',
              'Independence from Spain'],
  'items': [['<span class="yr">1519</span>', 2],
            ['<span class="yr">1718</span>', 6],
            ['<span class="yr">1821</span>', 7],
            ['<span class="yr">1836</span>', 0],
            ['<span class="yr">1845</span>', 1],
            ['<span class="yr">1861</span>', 5],
            ['<span class="yr">1876</span>', 4],
            ['<span class="yr">1901</span>', 3]]},
 {'type': 'sort',
  'title': 'Primary or secondary?',
  'intro': 'Sort each source. Ask: was the creator there at the time?',
  'button': 'Check my sorting',
  'word': 'sorted correctly',
  'choices': [['P', 'Primary'], ['S', 'Secondary']],
  'items': [["William B. Travis's letter asking for help, written at the Alamo in 1836",
             'P',
             'Travis wrote it during the siege.'],
            ['A 2020 textbook chapter about the Texas Revolution', 'S', 'Written about 185 years later.'],
            ['A photograph of the Spindletop gusher taken in January 1901',
             'P',
             'The photographer was standing there.'],
            ['An encyclopedia article about Spindletop in the Handbook of Texas',
             'S',
             'Written by historians who studied it later.'],
            ["Cabeza de Vaca's own account of his journey across Texas, published in 1542",
             'P',
             'He describes what he lived through.'],
            ['A 2015 documentary film about Comanche history', 'S', 'Made long after the events it describes.'],
            ['A diary kept by a German settler in Fredericksburg in 1847',
             'P',
             'Written by someone living there at the time.'],
            ['The Texas Constitution of 1876', 'P', 'It is the actual document from that time.'],
            ['A biography of Sam Houston written in 1993', 'S', 'The author studied Houston but never met him.'],
            ['An interview with a World War II veteran, recorded in 1999, about his own service',
             'P',
             'Tricky! It was recorded later, but he is an eyewitness telling his own story.']]},
 {'type': 'mc',
  'title': 'Read a graph',
  'intro': 'This graph shows how many people lived in Texas in five census years.',
  'button': 'Check my answers',
  'word': 'correct',
  'before': '<div class="chartbox"><svg viewBox="0 0 640 300" role="img" aria-label="Bar chart of Texas population: '
            '1850, 0.21 million; 1900, 3.0 million; 1950, 7.7 million; 2000, 20.9 million; 2020, 29.1 million."><text '
            'x="60" y="12" font-size="12" fill="var(--muted)">People living in Texas (millions)</text><line x1="60" '
            'x2="624" y1="260" y2="260" stroke="var(--rule)" stroke-width="1"></line><text x="52" y="264" '
            'text-anchor="end" font-size="12" fill="var(--muted)" font-family="IBM Plex Mono, '
            'monospace">0M</text><line x1="60" x2="624" y1="180" y2="180" stroke="var(--rule)" '
            'stroke-width="1"></line><text x="52" y="184" text-anchor="end" font-size="12" fill="var(--muted)" '
            'font-family="IBM Plex Mono, monospace">10M</text><line x1="60" x2="624" y1="100" y2="100" '
            'stroke="var(--rule)" stroke-width="1"></line><text x="52" y="104" text-anchor="end" font-size="12" '
            'fill="var(--muted)" font-family="IBM Plex Mono, monospace">20M</text><line x1="60" x2="624" y1="20" '
            'y2="20" stroke="var(--rule)" stroke-width="1"></line><text x="52" y="24" text-anchor="end" font-size="12" '
            'fill="var(--muted)" font-family="IBM Plex Mono, monospace">30M</text><rect x="84.816" y="258.299264" '
            'width="63.168000000000006" height="1.700736" rx="3" fill="var(--blue)"></rect><text x="116.4" '
            'y="252.299264" text-anchor="middle" font-size="12" font-weight="600" fill="var(--ink)" font-family="IBM '
            'Plex Mono, monospace">0.21M</text><text x="116.4" y="280" text-anchor="middle" font-size="13" '
            'fill="var(--ink)" font-family="IBM Plex Mono, monospace">1850</text><rect x="197.61599999999999" '
            'y="235.61032" width="63.168000000000006" height="24.38968" rx="3" fill="var(--blue)"></rect><text '
            'x="229.2" y="229.61032" text-anchor="middle" font-size="12" font-weight="600" fill="var(--ink)" '
            'font-family="IBM Plex Mono, monospace">3.0M</text><text x="229.2" y="280" text-anchor="middle" '
            'font-size="13" fill="var(--ink)" font-family="IBM Plex Mono, monospace">1900</text><rect x="310.416" '
            'y="198.310448" width="63.168000000000006" height="61.689552" rx="3" fill="var(--blue)"></rect><text '
            'x="342" y="192.310448" text-anchor="middle" font-size="12" font-weight="600" fill="var(--ink)" '
            'font-family="IBM Plex Mono, monospace">7.7M</text><text x="342" y="280" text-anchor="middle" '
            'font-size="13" fill="var(--ink)" font-family="IBM Plex Mono, monospace">1950</text><rect x="423.216" '
            'y="93.18544" width="63.168000000000006" height="166.81456" rx="3" fill="var(--blue)"></rect><text '
            'x="454.8" y="87.18544" text-anchor="middle" font-size="12" font-weight="600" fill="var(--ink)" '
            'font-family="IBM Plex Mono, monospace">20.9M</text><text x="454.8" y="280" text-anchor="middle" '
            'font-size="13" fill="var(--ink)" font-family="IBM Plex Mono, monospace">2000</text><rect '
            'x="536.0159999999998" y="26.83596" width="63.168000000000006" height="233.16404" rx="3" '
            'fill="var(--blue)"></rect><text x="567.5999999999999" y="20.83596" text-anchor="middle" font-size="12" '
            'font-weight="600" fill="var(--ink)" font-family="IBM Plex Mono, monospace">29.1M</text><text '
            'x="567.5999999999999" y="280" text-anchor="middle" font-size="13" fill="var(--ink)" font-family="IBM Plex '
            'Mono, monospace">2020</text></svg><p class="cap">Source: U.S. Census Bureau decennial census. M = '
            'million.</p></div>',
  'items': [{'q': 'About how many people lived in Texas in 1900?',
             'o': ['About 300,000', 'About 3 million', 'About 30 million'],
             'a': 1,
             'e': 'The 1900 bar reaches just past 3 million (3,048,710).',
             'fixed': True},
            {'q': 'Texas passed 20 million people by 2000. Which era was that?',
             'o': ['Age of Oil', 'Civil Rights and Conservatism', 'Contemporary Texas'],
             'a': 2,
             'e': 'The Contemporary Texas era runs from about 1980 to today.',
             'fixed': True},
            {'q': 'Between which two years on the graph did Texas gain the most people?',
             'o': ['1850 to 1900', '1950 to 2000', '2000 to 2020'],
             'a': 1,
             'e': 'About 13 million people were added from 1950 to 2000. (That gap is 50 years, longer than 2000 to '
                  '2020.)',
             'fixed': True}]}],
  quiz=[{'q': 'In what year was San Antonio founded?',
  'o': ['1690', '1718', '1821', '1836'],
  'a': 1,
  'e': 'San Antonio was founded in 1718, during the Spanish Colonial era.',
  'fixed': True},
 {'q': 'Which era comes right after the Mexican National era?',
  'o': ['Spanish Colonial', 'Early Statehood', 'Revolution and Republic', 'Age of Contact'],
  'a': 2,
  'e': 'Mexican rule ended with the Texas Revolution, which began the Revolution and Republic era.',
  'fixed': True},
 {'q': 'What happened in 1901?',
  'o': ['Texas joined the United States', 'Oil gushed at Spindletop', 'The Civil War began', 'San Antonio was founded'],
  'a': 1,
  'e': 'The Spindletop gusher in 1901 began the Age of Oil.',
  'fixed': True},
 {'q': 'What is the main reason historians divide the past into eras?',
  'o': ['To make history shorter',
        'To group times that share defining characteristics so change is easier to study',
        'Because every era lasts exactly 50 years',
        'Because each era had a different capital city'],
  'a': 1,
  'e': 'Eras group years that share defining characteristics, which makes change over time easier to see.',
  'fixed': True},
 {'q': 'Which of these is a primary source about the Texas Revolution?',
  'o': ['A 2020 textbook chapter',
        'A letter written by a soldier in 1836',
        'A museum website about the Alamo',
        'A 1990 encyclopedia article'],
  'a': 1,
  'e': 'The 1836 letter was written by someone who was there at the time.',
  'fixed': True},
 {'q': 'What happened in 1845?',
  'o': ['Texas declared independence',
        'Texas was annexed to the United States',
        'Mexico won independence from Spain',
        'Texas adopted its current constitution'],
  'a': 1,
  'e': 'Texas became a U.S. state through annexation in 1845.',
  'fixed': True},
 {'q': 'In which era did cattle drives and new railroads spread across Texas?',
  'o': ['Cotton, Cattle, and Railroads', 'Age of Contact', 'Age of Oil', 'Early Statehood'],
  'a': 0,
  'e': 'That era (about 1874–1900) is named for those three changes.',
  'fixed': True},
 {'q': 'In what year did Mexico, including Texas, win independence from Spain?',
  'o': ['1519', '1718', '1821', '1861'],
  'a': 2,
  'e': 'Mexico won independence in 1821, starting the Mexican National era.',
  'fixed': True},
 {'q': 'The constitution Texas uses today was adopted in which year?',
  'o': ['1836', '1845', '1876', '1901'],
  'a': 2,
  'e': 'The current Texas Constitution was adopted in 1876.',
  'fixed': True},
 {'q': 'An interview recorded in 1999 with a veteran describing his own World War II service is a…',
  'o': ['Primary source, because he was an eyewitness',
        'Secondary source, because it was recorded later',
        'Neither one',
        'Secondary source, because it is an interview'],
  'a': 0,
  'e': 'What matters is whether the person was there. He was, so it is a primary source.',
  'fixed': True}],
  quiz_label='Quiz',
  reflect_h='Answer the big question',
  prompt="In 3 to 5 sentences, answer: <b>Why do historians divide Texas history into eras?</b> Make a claim, give one piece of evidence from today's lesson (an era, a date, or a change), and explain how your evidence supports your claim.",
  placeholder='Historians divide Texas history into eras because...',
  ck1='I made a clear <b>claim</b> that answers the question.',
  ck2='I gave specific <b>evidence</b> (an era, a date, or an event).',
  ck3='I explained <b>how</b> my evidence supports my claim.',
  review='Review the eras and dates',
  sources='<a href="https://www.thestoryoftexas.com/learn/texas-history-timeline/" target="_blank" rel="noopener">Bullock Museum Texas History Timeline</a> · <a href="https://www.tshaonline.org/handbook" target="_blank" rel="noopener">Handbook of Texas Online</a> · Population: U.S. Census Bureau decennial census counts.',
)
