L = dict(
  slug="lesson11", key="tx-lesson11-v1", n=11, label="Lesson 11", short="Cotton, Cattle & Railroads",
  title="Cotton, Cattle & Railroads",
  question="How did railroads and the closing frontier remake Texas?",
  teks=["6A", "6B", "6C", "6D", "21B"],
  read='''  <h2>Texas after the war</h2>
  <div class="prose">
    <p>When Reconstruction ended (Lesson 10), Texas was poor but full of two things: land and cattle. Over the next 30 years, cattle drives, railroads, and the end of the open frontier changed where Texans lived and how they made a living. That change came at a terrible cost for American Indians.</p>
  </div>

  <h3>The cattle drives</h3>
  <div class="prose"><p>During the war, millions of longhorns ran wild in South Texas. A steer worth a few dollars in Texas could sell for many times more in the North, where cities wanted beef. So from 1866 to the 1880s, cowboys drove herds north to railroad towns in Kansas, where cattle were loaded onto trains.</p></div>
  <div class="regions">
    <div class="card"><div class="ctop"><b>Chisholm Trail</b><span class="tag">to Abilene, KS</span></div><p>The most famous route, running north from South Texas through Fort Worth.</p></div>
    <div class="card"><div class="ctop"><b>Western Trail</b><span class="tag">to Dodge City, KS</span></div><p>Ran farther west as farms and fences filled in the land along the Chisholm.</p></div>
    <div class="card"><div class="ctop"><b>Goodnight-Loving Trail</b><span class="tag">to New Mexico</span></div><p>Charles Goodnight and Oliver Loving drove herds west and north to forts and mining towns.</p></div>
  </div>
  <div class="callout"><b>Who were the cowboys?</b> Many were young men back from the war. Many were African American or Mexican American, and Mexican vaqueros (Lesson 4) had taught the skills they all used. By the late 1880s, barbed wire fences, windmills, and railroads reaching into Texas itself ended the long drives.</div>

  <h3>Railroads remake the map</h3>
  <div class="prose"><p>In 1870, Texas had only a few hundred miles of railroad track. By 1900 it had nearly 10,000 miles. Railroads let farmers ship cotton and ranchers ship cattle from anywhere along the line, so new towns grew up beside the tracks. Towns the railroad skipped often withered. Railroads also brought settlers to West Texas and the Panhandle.</p></div>
  <div class="ruler">
    <div class="era"><span class="yr">1870</span><div><b>A few short lines</b><span>Mostly around Houston and Galveston, carrying cotton to the coast.</span></div></div>
    <div class="era"><span class="yr">1873</span><div><b>Dallas connects</b><span>Two railroads met in Dallas, which grew into a trading hub.</span></div></div>
    <div class="era"><span class="yr">1881–83</span><div><b>East meets west</b><span>Lines built across West Texas reached El Paso, linking it to the rest of the country.</span></div></div>
    <div class="era"><span class="yr">1900</span><div><b>Nearly 10,000 miles</b><span>Tracks crossed most of the state. Abilene, Midland, Amarillo, and many other towns grew up along them.</span></div></div>
  </div>

  <h3>The end of the open frontier</h3>
  <div class="regions">
    <div class="card"><div class="ctop"><b>The bison</b><span class="tag">1870s</span></div><p>Hide hunters killed millions of bison on the Southern Plains in just a few years. The Comanche, Kiowa, and other Plains nations depended on the bison for food, shelter, and tools (Lesson 2).</p></div>
    <div class="card"><div class="ctop"><b>Buffalo soldiers</b><span class="tag">U.S. Army</span></div><p>African American regiments served at frontier forts such as Fort Concho and Fort Davis. They guarded roads, mapped West Texas, and fought in campaigns against American Indians.</p></div>
    <div class="card"><div class="ctop"><b>Red River War</b><span class="tag">1874–75</span></div><p>The U.S. Army attacked Comanche, Kiowa, and Cheyenne camps. At Palo Duro Canyon, soldiers destroyed their winter food and killed more than 1,000 horses.</p></div>
    <div class="card"><div class="ctop"><b>Quanah Parker</b><span class="tag">Comanche leader</span></div><p>The son of a Comanche chief and Cynthia Ann Parker, a captured settler. He led his band onto a reservation in Oklahoma in 1875, then became a respected leader and rancher who worked to protect his people's land and rights.</p></div>
  </div>

  <h3>Farmers fight back</h3>
  <div class="prose"><p>Cotton was still king, but many farmers, white and Black, worked land they did not own as tenant farmers or sharecroppers. They complained that railroads charged unfair rates to ship their crops. Farmers organized groups like the Grange and the Farmers' Alliance. In 1890, <b>James Stephen Hogg</b> was elected governor, the first born in Texas. He created the <b>Texas Railroad Commission</b> in 1891 to regulate railroad rates.</p></div>

  <div class="callout"><b>Reading a map pattern (SE 21B).</b> When you compare an 1870 railroad map with a 1900 map, ask: Where are the new lines? Which towns appear along them? What does that tell you about where Texans lived and worked? A pattern is something that repeats across the map, like "new towns appear along the tracks."</div>''',
  practice=[
    {"type": "mc", "title": "Read the railroad map", "intro": "Imagine two maps of Texas railroads, one from 1870 and one from 1900. Pick the best answer.", "button": "Check my answers", "word": "correct",
     "before": '''<div class="chartbox"><svg viewBox="0 0 360 170" role="img" aria-label="Bar chart of Texas railroad miles: a few hundred in 1870, about 2,400 at the end of 1879, about 8,500 in 1890, just under 10,000 in 1900">
      <g font-family="IBM Plex Mono, monospace" font-size="11" fill="var(--muted)">
        <line x1="40" y1="140" x2="350" y2="140" stroke="var(--rule)"/>
        <text x="34" y="144" text-anchor="end">0</text><text x="34" y="84" text-anchor="end">5k</text><text x="34" y="24" text-anchor="end">10k</text>
        <line x1="40" y1="80" x2="350" y2="80" stroke="var(--rule)" stroke-dasharray="3 3"/><line x1="40" y1="20" x2="350" y2="20" stroke="var(--rule)" stroke-dasharray="3 3"/>
      </g>
      <g fill="var(--blue)">
        <rect x="60" y="133" width="50" height="7"/><rect x="135" y="111" width="50" height="29"/><rect x="210" y="38" width="50" height="102"/><rect x="285" y="21" width="50" height="119"/>
      </g>
      <g font-family="IBM Plex Mono, monospace" font-size="11" fill="var(--ink)" text-anchor="middle">
        <text x="85" y="158">1870</text><text x="160" y="158">1879</text><text x="235" y="158">1890</text><text x="310" y="158">1900</text>
      </g></svg><p class="cap">Approximate miles of railroad track in Texas. Rounded estimates based on the Handbook of Texas, “Railroads,” which says more than 6,000 miles were built in the 1880s alone.</p></div>''',
     "items": [
       {"q": "In which decade did the most new track get built?", "o": ["1870s", "1880s", "1890s"], "a": 1, "e": "More than 6,000 miles were built in the 1880s."},
       {"q": "Which pattern would you expect on the 1900 map?", "o": ["New towns appear along the tracks", "Towns move away from the tracks", "No new towns appear"], "a": 0, "e": "Railroads created towns like Abilene, Midland, and Amarillo."},
       {"q": "What did the railroads mean for the long cattle drives?", "o": ["They made drives longer", "They ended them, because cattle could be shipped from Texas", "Nothing changed"], "a": 1, "e": "Once tracks reached Texas, there was no need to walk herds to Kansas."}]},
    {"type": "match", "title": "People and groups", "intro": "Match each clue to the right person or group.", "placeholder": "Choose one…", "button": "Check my matches", "word": "correct",
     "options": ["Quanah Parker", "Buffalo soldiers", "James Stephen Hogg", "Charles Goodnight", "Farmers' Alliance"],
     "items": [["Comanche leader who later became a rancher and spokesman for his people", 0], ["African American soldiers at forts like Fort Concho and Fort Davis", 1], ["First Texas-born governor; created the Railroad Commission", 2], ["Rancher who blazed a trail west toward New Mexico", 3], ["Farmers' group that fought high railroad rates", 4]]},
    {"type": "sort", "title": "Cause of change", "intro": "Did this help <b>end the cattle drives</b> or <b>end the open frontier</b> for Plains nations?", "button": "Check my sorting", "word": "sorted correctly",
     "choices": [["C", "End the cattle drives"], ["F", "End the open frontier"]],
     "items": [["Barbed wire fences crossed the open range", "C", "Fences blocked the trails."], ["Hide hunters killed millions of bison", "F", "Plains nations lost their main food source."], ["Railroads reached Texas towns", "C", "Ranchers could ship cattle from home."], ["The Army destroyed winter camps at Palo Duro Canyon", "F", "Without food and horses, bands had to surrender."], ["Quanah Parker's band moved to a reservation in 1875", "F", "The last free Comanche band left the Texas plains."], ["Windmills let ranchers fence and water their own pastures", "C", "Ranching moved onto fenced land."]]},
    {"type": "order", "title": "Put it in order", "intro": "Use the arrows to put these in order, earliest at the top.", "button": "Check my order", "word": "in the right spot", "seed": 9,
     "items": [["Long cattle drives to Kansas begin", "1866"], ["Railroads meet in Dallas", "1873"], ["Red River War and Palo Duro Canyon", "1874"], ["Railroad reaches El Paso", "1881"], ["Hogg creates the Railroad Commission", "1891"], ["Texas has nearly 10,000 miles of track", "1900"]]}
  ],
  quiz=[
    {"q": "Why did Texans drive cattle north after the Civil War?", "o": ["Cattle sold for much more in the North", "Texas banned cattle", "Cattle needed snow", "The Army ordered it"], "a": 0, "e": "Northern cities wanted beef."},
    {"q": "The Chisholm Trail led to…", "o": ["Abilene, Kansas", "El Paso", "Santa Fe", "New Orleans"], "a": 0, "e": "There, cattle were loaded onto trains."},
    {"q": "Which ended the long cattle drives?", "o": ["Barbed wire, windmills, and railroads in Texas", "The Civil War", "Oil wells", "Hurricanes"], "a": 0, "e": "Fenced ranches and nearby railroads made drives unnecessary."},
    {"q": "Who were the buffalo soldiers?", "o": ["Bison hunters", "African American U.S. Army regiments on the frontier", "Comanche warriors", "Cattle buyers"], "a": 1, "e": "They served at forts across West Texas."},
    {"q": "Why was the killing of the bison so harmful to Plains nations?", "o": ["They depended on bison for food, shelter, and tools", "Bison were used to pull wagons", "Bison were sacred to settlers", "It was not harmful"], "a": 0, "e": "Losing the bison forced bands onto reservations."},
    {"q": "Quanah Parker is known for…", "o": ["Leading a Comanche band, then becoming a leader and rancher on the reservation", "Building railroads", "Founding Dallas", "Being governor"], "a": 0, "e": "He worked to protect his people's interests after 1875."},
    {"q": "How did railroads change where Texans lived?", "o": ["New towns grew up along the tracks", "People moved to the coast only", "Everyone left Texas", "Nothing changed"], "a": 0, "e": "Towns without a railroad often faded."},
    {"q": "Why did farmers want the Railroad Commission?", "o": ["Railroad shipping rates were too high", "They wanted free trains", "They wanted to ban trains", "To build canals"], "a": 0, "e": "Governor Hogg created it in 1891."},
    {"q": "Many Texas farmers who did not own land worked as…", "o": ["Sharecroppers or tenant farmers", "Empresarios", "Buffalo soldiers", "Oil workers"], "a": 0, "e": "They paid with part of their crop or rent."},
    {"q": "Which sentence best answers the big question?", "o": ["Railroads and the end of the frontier spread towns and farms across Texas, ended the cattle drives, and forced Plains nations onto reservations", "Texas stayed exactly the same", "Railroads only helped Mexico", "The frontier grew larger"], "a": 0, "e": "Growth for some came at a great cost for others."}
  ],
  prompt="Pattern paragraph. In 3 to 5 sentences, answer: <b>What does the railroad map show about where Texans lived by 1900?</b> State the pattern as a claim, give one piece of evidence (a number, a town, or a date), and explain what caused the pattern.",
  placeholder="By 1900, the railroad map shows that Texans...",
  reflect_h="Explain the pattern",
  ck1="I stated the <b>pattern</b> as a clear claim.",
  ck3="I explained what <b>caused</b> the pattern.",
  review="Review the railroad chart and the frontier cards",
  sources='<a href="https://www.tshaonline.org/handbook" target="_blank" rel="noopener">Handbook of Texas Online</a>: “Cattle Trailing,” “Railroads,” “Buffalo Soldiers,” “Parker, Quanah,” “Red River War,” “Hogg, James Stephen,” “Railroad Commission”',
)
