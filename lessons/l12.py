L = dict(
  slug="lesson12", key="tx-lesson12-v1", n=12, label="Lesson 12", short="Age of Oil",
  title="The Age of Oil",
  question="How did one well in 1901 change Texas's economy?",
  teks=["1B", "7A", "7B", "9B", "11A", "11B", "12A"],
  read='''  <h2>A storm, a gusher, and a new economy</h2>
  <div class="prose">
    <p>In 1900, Texas made its living from farms and ranches: cotton, cattle, and lumber (Lesson 11). Within a few years, two events on the Gulf Coast began to change that. One was a disaster. The other was a fountain of oil.</p>
  </div>

  <h3>The Galveston hurricane, 1900</h3>
  <div class="prose"><p>Galveston was the richest city in Texas and its busiest port. On September 8, 1900, a hurricane pushed a wall of seawater over the low island. At least 6,000 people died, and some estimates are much higher. It is still the deadliest natural disaster in U.S. history.</p>
  <p>Galveston rebuilt. It raised the level of the whole city and built a giant seawall. But shipping companies began to look inland for a safer port. Houston, about 50 miles from the Gulf, dug the <b>Houston Ship Channel</b>, which opened in 1914. Houston soon passed Galveston as the region's big city. Geography, and a storm, shifted where growth happened.</p></div>

  <h3>Spindletop, 1901</h3>
  <div class="prose"><p>Near Beaumont, a hill called Spindletop rose above a salt dome. A local businessman, <b>Pattillo Higgins</b>, was sure oil lay underneath, but most geologists disagreed. An engineer named <b>Anthony F. Lucas</b>, an expert on salt domes, kept drilling. On <b>January 10, 1901</b>, mud and then oil shot more than 100 feet into the air. The Lucas gusher flowed an estimated 100,000 barrels a day, more than any well in the world at the time. It took nine days to cap it.</p></div>

  <div class="dates">
    <div class="date"><span class="yr">1901</span><b>Spindletop gusher</b><p>This is one of your eight required dates. Add it to your timeline.</p></div>
  </div>

  <h3>The boom</h3>
  <div class="regions">
    <div class="card"><div class="ctop"><b>People</b><span class="tag">boomtown</span></div><p>Beaumont grew from about 10,000 people to about 50,000 within months. Workers, investors, and con artists poured in.</p></div>
    <div class="card"><div class="ctop"><b>Companies</b><span class="tag">big oil</span></div><p>Companies that started or grew at Spindletop include the Texas Company (later Texaco), Gulf Oil, and Humble (later part of Exxon).</p></div>
    <div class="card"><div class="ctop"><b>Industry</b><span class="tag">refining</span></div><p>Refineries, pipelines, and the Houston Ship Channel turned the Gulf Coast into a center for oil and chemicals.</p></div>
    <div class="card"><div class="ctop"><b>Energy</b><span class="tag">fuel</span></div><p>Cheap oil fueled ships, trains, factories, and soon automobiles. Texas went from a farm state toward an industrial one.</p></div>
  </div>

  <h3>The bust</h3>
  <div class="prose"><p>Within two years, hundreds of wells crowded onto Spindletop. Each one drained the same field, so the pressure dropped. By 1904, the field produced only a tiny share of what it had. Many people who rushed in lost everything.</p></div>

  <div class="chartbox"><svg viewBox="0 0 360 180" role="img" aria-label="Boom and bust cycle: a line rises sharply as a discovery brings a rush of drilling, peaks, then falls as too many wells and low prices cause a bust">
    <g font-family="IBM Plex Mono, monospace" font-size="11" fill="var(--muted)">
      <line x1="30" y1="150" x2="350" y2="150" stroke="var(--rule)"/><line x1="30" y1="20" x2="30" y2="150" stroke="var(--rule)"/>
      <text x="34" y="170">time →</text><text x="22" y="90" text-anchor="middle" transform="rotate(-90 22 90)">jobs, people, money</text>
    </g>
    <path d="M30 140 C 80 138, 100 40, 140 30 S 200 60, 240 120 S 320 140, 350 135" fill="none" stroke="var(--gold)" stroke-width="3"/>
    <g font-family="Atkinson Hyperlegible, sans-serif" font-size="12" fill="var(--ink)">
      <text x="60" y="110">1 Discovery</text><text x="128" y="20">2 Boom</text><text x="200" y="70">3 Too many wells,</text><text x="200" y="84">prices fall</text><text x="255" y="130">4 Bust</text>
    </g></svg><p class="cap">The boom-and-bust cycle. It happened at Spindletop, and again many times after.</p></div>

  <div class="callout"><b>It kept happening.</b> New fields brought new booms: the huge East Texas field in 1930 and the Permian Basin in West Texas. Busts came too. In the early 1930s, so much oil flooded the market that prices fell to pennies a barrel, and the Texas Railroad Commission (Lesson 11) began limiting how much each well could pump. In the 1980s, a crash in oil prices cost Texas many thousands of jobs. Today, Texas spreads its risk across more industries, but oil and gas still matter.</div>

  <h3>People change the land</h3>
  <div class="prose"><p>Geographers ask how people adapt to and change their environment. Galveston's seawall, the Ship Channel, and oil derricks covering Spindletop are all examples of people modifying the land to make a living. Some changes helped people, and some, like oil spills and drained fields, caused damage.</p></div>''',
  practice=[
    {"type": "order", "title": "Boom-and-bust cycle", "intro": "Use the arrows to put the stages of a boom and bust in order, first at the top.", "button": "Check my order", "word": "in the right spot", "seed": 10,
     "items": [["Oil is discovered", "1"], ["People and companies rush in; towns grow fast", "2"], ["Too many wells drain the field and flood the market", "3"], ["Prices and production fall", "4"], ["Jobs disappear and people leave", "5"]]},
    {"type": "match", "title": "Spindletop facts", "intro": "Match each clue to the right answer.", "placeholder": "Choose one…", "button": "Check my matches", "word": "correct",
     "options": ["January 10, 1901", "Anthony F. Lucas", "Pattillo Higgins", "About 50,000", "100,000 barrels a day", "Houston Ship Channel"],
     "items": [["Date of the Lucas gusher", 0], ["Salt-dome expert who drilled the gusher", 1], ["Local businessman who believed oil was under Spindletop", 2], ["Beaumont's population soon after the boom", 3], ["How much the gusher flowed", 4], ["Opened in 1914 and helped Houston pass Galveston", 5]]},
    {"type": "sort", "title": "Boom or bust?", "intro": "Is this a cause of a <b>boom</b> or a cause of a <b>bust</b>?", "button": "Check my sorting", "word": "sorted correctly",
     "choices": [["B", "Boom"], ["X", "Bust"]],
     "items": [["A gusher is discovered", "B", "Discovery starts the rush."], ["Hundreds of wells drain the same field", "X", "Pressure drops and production falls."], ["Automobiles create huge demand for gasoline", "B", "More demand raises prices and jobs."], ["Too much oil floods the market", "X", "Prices drop, as in the early 1930s."], ["A new pipeline and port make shipping cheap", "B", "Lower costs mean more profit and growth."], ["World oil prices crash, as in the 1980s", "X", "Companies cut jobs when prices fall."]]},
    {"type": "mc", "title": "Geography and growth", "intro": "Pick the best answer.", "button": "Check my answers", "word": "correct",
     "items": [
       {"q": "Why did Houston grow faster than Galveston after 1900?", "o": ["Houston was safer from storms, and the Ship Channel gave it a port", "Galveston had no ships", "Houston had gold"], "a": 0, "e": "Geography and the 1900 storm shifted growth inland."},
       {"q": "Which is an example of people modifying their environment?", "o": ["Building the Galveston seawall", "A hurricane", "A salt dome forming"], "a": 0, "e": "People built the seawall to protect the city."},
       {"q": "How did Spindletop change the Texas economy?", "o": ["It began a shift from farming toward industry", "It ended oil production in Texas", "It made cotton more important than ever"], "a": 0, "e": "Oil, refining, and chemicals became major industries."}]}
  ],
  quiz=[
    {"q": "What happened in 1901?", "o": ["The Spindletop gusher near Beaumont", "Texas joined the U.S.", "The Galveston hurricane", "The Civil War began"], "a": 0, "e": "1901 is a required date."},
    {"q": "Who drilled the Spindletop gusher?", "o": ["Anthony F. Lucas", "Stephen F. Austin", "James Hogg", "Sam Houston"], "a": 0, "e": "Pattillo Higgins had believed in Spindletop first."},
    {"q": "About how much did the gusher flow at first?", "o": ["100 barrels a day", "100,000 barrels a day", "10 barrels a year", "1 million barrels a day"], "a": 1, "e": "More than any well in the world at the time."},
    {"q": "What happened to Beaumont's population?", "o": ["It fell by half", "It grew from about 10,000 to about 50,000", "It stayed the same", "Everyone moved to Galveston"], "a": 1, "e": "A classic boomtown."},
    {"q": "Why did Spindletop's production fall by 1904?", "o": ["Too many wells drained the same field", "A hurricane hit", "Oil was banned", "Lucas left"], "a": 0, "e": "That is a bust."},
    {"q": "What was the Galveston hurricane of 1900?", "o": ["The deadliest natural disaster in U.S. history", "A small storm", "A flood in Dallas", "An oil fire"], "a": 0, "e": "At least 6,000 people died."},
    {"q": "Which company grew out of Spindletop?", "o": ["The Texas Company (Texaco)", "Dell", "NASA", "The Railroad Commission"], "a": 0, "e": "Gulf Oil and Humble also grew there."},
    {"q": "How did the Houston Ship Channel change Texas?", "o": ["It helped Houston become a major port and city", "It flooded Houston", "It moved the capital", "It ended oil shipping"], "a": 0, "e": "It opened in 1914."},
    {"q": "In the early 1930s, why did the Railroad Commission limit oil production?", "o": ["Too much oil had crashed prices", "There was no oil left", "Trains needed the oil", "To start a war"], "a": 0, "e": "Limiting production helped steady prices."},
    {"q": "Which sentence best answers the big question?", "o": ["Spindletop started an oil boom that grew cities, created big companies, and moved Texas from farming toward industry, though booms were followed by busts", "Spindletop ended the oil industry", "Oil made no difference to Texas", "Spindletop happened in Dallas"], "a": 0, "e": "Use a number or a company as evidence."}
  ],
  prompt="In 3 to 5 sentences, answer: <b>How did one well in 1901 change Texas's economy?</b> Make a claim, give one piece of evidence (a number, a company, a city, or a date), and explain how your evidence supports your claim. Bonus: mention one bust.",
  placeholder="The Spindletop well changed Texas's economy by...",
  review="Review the boom-and-bust chart and the Spindletop facts",
  sources='<a href="https://www.tshaonline.org/handbook/entries/spindletop-oilfield" target="_blank" rel="noopener">Handbook of Texas Online: “Spindletop Oilfield”</a> · <a href="https://www.tshaonline.org/handbook" target="_blank" rel="noopener">Handbook of Texas Online</a>: “Galveston Hurricane of 1900,” “Houston Ship Channel,” “East Texas Oilfield,” “Oil and Gas Industry”',
)
