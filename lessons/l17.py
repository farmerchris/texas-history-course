L = dict(
  slug="lesson17", key="tx-lesson17-v1", n=17, label="Lesson 17", short="My Texas Story",
  title="Capstone: My Texas Story Project",
  question="How did one person, place, or event change Texas?",
  teks=["18D", "20A", "20E", "22B", "22C"],
  read='''  <h2>Your turn to be the historian</h2>
  <div class="prose">
    <p>All year you have read sources, made claims, and backed them with evidence. Now you will choose your own topic from any era of Texas history, research it, and show what you found as a <b>poster</b>, a <b>short video</b>, or a <b>2-page paper</b>. This page gets you started: you'll practice the research skills, then write a project proposal for a parent to approve.</p>
  </div>

  <h3>The project steps</h3>
  <div class="ruler">
    <div class="era"><span class="yr">Step 1</span><div><b>Choose a topic</b><span>Pick one person, place, or event. Make it narrow enough to explain well. "The Texas Revolution" is too big; "Juan Seguín's role in the Revolution" is just right.</span></div></div>
    <div class="era"><span class="yr">Step 2</span><div><b>Find sources</b><span>You need at least <b>one primary source</b> and <b>two secondary sources</b>. Start with the Handbook of Texas Online and the Portal to Texas History.</span></div></div>
    <div class="era"><span class="yr">Step 3</span><div><b>Take notes and cite</b><span>Write down where every fact came from as you go. It is much harder to find later.</span></div></div>
    <div class="era"><span class="yr">Step 4</span><div><b>Make a claim</b><span>Answer the big question for your topic: how did it change Texas? Your claim is the center of the project.</span></div></div>
    <div class="era"><span class="yr">Step 5</span><div><b>Build and present</b><span>Make the poster, video, or paper. Organize it around your claim and evidence, and include a source list.</span></div></div>
  </div>

  <h3>Topic ideas from this year</h3>
  <div class="regions">
    <div class="card"><div class="ctop"><b>People</b><span class="tag">who</span></div><ul><li>Cabeza de Vaca</li><li>José Antonio Navarro</li><li>Quanah Parker</li><li>Minnie Fisher Cunningham</li><li>Hector P. García</li><li>Barbara Jordan</li></ul></div>
    <div class="card"><div class="ctop"><b>Places</b><span class="tag">where</span></div><ul><li>The San Antonio missions</li><li>Galveston</li><li>Spindletop</li><li>Palo Duro Canyon</li><li>Johnson Space Center</li></ul></div>
    <div class="card"><div class="ctop"><b>Events</b><span class="tag">what</span></div><ul><li>The Battle of Medina</li><li>Annexation</li><li>Juneteenth</li><li>The 1900 Galveston hurricane</li><li>The Dust Bowl</li><li><i>Hernandez v. Texas</i></li></ul></div>
  </div>

  <h3>Where to look</h3>
  <div class="ps">
    <div><b>Secondary sources</b><p>Written later by people who studied the past: <a href="https://www.tshaonline.org/handbook" target="_blank" rel="noopener">Handbook of Texas Online</a>, <a href="https://www.thestoryoftexas.com/" target="_blank" rel="noopener">Bullock Texas State History Museum</a>, library books.</p></div>
    <div><b>Primary sources</b><p>Made at the time by people who were there: letters, photos, maps, and newspapers on the <a href="https://texashistory.unt.edu/" target="_blank" rel="noopener">Portal to Texas History</a>, documents at the <a href="https://www.tsl.texas.gov/" target="_blank" rel="noopener">Texas State Library and Archives</a>.</p></div>
  </div>

  <h3>How to cite a source</h3>
  <div class="excerpt">
    <span class="who">A simple citation format</span>
    <p class="line">Author (if known). “Title of the page or article.” <i>Name of the website or book</i>, date published. Web address.</p>
    <p><b>Example:</b> Wooster, Robert, and Christine Moor Sanders. “Spindletop Oilfield.” <i>Handbook of Texas Online</i>, Texas State Historical Association. https://www.tshaonline.org/handbook/entries/spindletop-oilfield</p>
  </div>

  <h3>How your project will be graded</h3>
  <div class="cmpbox"><table class="cmp">
    <thead><tr><th>Category</th><th>4 points means…</th></tr></thead>
    <tbody>
      <tr><th>Accurate history</th><td>Facts, names, and dates are correct and explained in your own words.</td></tr>
      <tr><th>Sources</th><td>At least one primary and two secondary sources, each cited correctly.</td></tr>
      <tr><th>Claim</th><td>A clear claim about how your topic changed Texas, backed by evidence.</td></tr>
      <tr><th>Presentation</th><td>Clear, organized, and easy to follow, with your claim up front.</td></tr>
    </tbody>
  </table></div>
  <div class="callout"><b>Texas History Day.</b> If you enter the Texas History Day contest run by the Texas State Historical Association, your entry can count as this project.</div>''',
  practice=[
    {"type": "sort", "title": "Primary or secondary?", "intro": "Is each source <b>primary</b> or <b>secondary</b>?", "button": "Check my sorting", "word": "sorted correctly",
     "choices": [["P", "Primary"], ["S", "Secondary"]],
     "items": [["A photograph of Beaumont taken in 1901", "P", "Made at the time of the event."], ["A Handbook of Texas article written in 2010", "S", "Written later by a historian."], ["Travis's letter from the Alamo", "P", "Written during the siege by a participant."], ["A documentary film about the Dust Bowl", "S", "Made later, though it may include primary footage."], ["A 1919 newspaper report on woman suffrage", "P", "Written at the time."], ["Your own project about Barbara Jordan", "S", "You are studying the past, so your work is secondary."]]},
    {"type": "mc", "title": "Choose a good topic", "intro": "Pick the topic that is the right size for this project.", "button": "Check my answers", "word": "correct",
     "items": [
       {"q": "Which topic is narrow enough?", "o": ["All of Texas history", "How the Houston Ship Channel helped Houston grow", "Everything about oil"], "a": 1, "e": "One place, one change: just right."},
       {"q": "Which topic is narrow enough?", "o": ["Wars", "Lulu B. White and the fight against the white primary", "The 1900s"], "a": 1, "e": "A person plus a specific effort."},
       {"q": "Which is the strongest claim?", "o": ["Spindletop was a place in Texas.", "Spindletop changed Texas by starting an oil boom that turned the state toward industry.", "I like oil."], "a": 1, "e": "A claim answers how the topic changed Texas, and can be supported with evidence."}]},
    {"type": "match", "title": "Fix the citation", "intro": "Match each part of a citation to an example.", "placeholder": "Choose a part…", "button": "Check my matches", "word": "correct",
     "options": ["Author", "Title", "Website or book", "Web address"],
     "items": [["Wooster, Robert", 0], ["“Spindletop Oilfield”", 1], ["Handbook of Texas Online", 2], ["https://www.tshaonline.org/handbook/entries/spindletop-oilfield", 3]]},
    {"type": "order", "title": "Project steps", "intro": "Use the arrows to put the project steps in order, first at the top.", "button": "Check my order", "word": "in the right spot", "seed": 16,
     "items": [["Choose a narrow topic", "1"], ["Find one primary and two secondary sources", "2"], ["Take notes and record citations", "3"], ["Write a claim about how it changed Texas", "4"], ["Build and present the project", "5"]]}
  ],
  quiz=[
    {"q": "How many sources does the project require at minimum?", "o": ["One primary and two secondary", "None", "One secondary only", "Ten primary"], "a": 0, "e": "Three sources total, at least."},
    {"q": "Which is a primary source?", "o": ["A letter written in 1836", "A 2020 textbook", "An encyclopedia article", "A museum website summary"], "a": 0, "e": "It was made at the time."},
    {"q": "Why should you record citations while you take notes?", "o": ["So you can show where each fact came from without searching again later", "Citations are optional", "To make the project longer", "Teachers don't read them"], "a": 0, "e": "It saves time and keeps your work honest."},
    {"q": "What is a claim?", "o": ["An answer to the question that you can support with evidence", "A list of facts", "A picture", "A citation"], "a": 0, "e": "Your project is built around it."},
    {"q": "Which project formats are allowed?", "o": ["A poster, a short video, or a 2-page paper", "Only a test", "Only a speech", "A text message"], "a": 0, "e": "Pick the one that fits your topic."},
    {"q": "What makes a topic too big?", "o": ["It covers so much you can't explain it well, like “all of Texas history”", "It has a person in it", "It is about a place", "It has a date"], "a": 0, "e": "Narrow it to one person, place, or event."},
    {"q": "Which website is a good secondary source for Texas history?", "o": ["Handbook of Texas Online", "A random social media post", "An ad", "A video game wiki"], "a": 0, "e": "It is written by historians and cites its sources."},
    {"q": "Where can you find primary sources like old photos and newspapers?", "o": ["The Portal to Texas History", "A dictionary", "A math textbook", "A weather app"], "a": 0, "e": "It is run by UNT Libraries."},
    {"q": "Which rubric category checks your sources?", "o": ["Sources: one primary and two secondary, cited correctly", "Presentation only", "Accurate history only", "There is no source category"], "a": 0, "e": "Each category is worth 4 points."},
    {"q": "Your project will be strongest if…", "o": ["Your claim is clear and every main point has evidence from a source", "It is as long as possible", "It has no claim", "It uses only one source"], "a": 0, "e": "Claim plus evidence: the skill you practiced all year."}
  ],
  prompt="Project proposal. In 3 to 5 sentences, tell a parent: <b>your topic</b>, <b>your format</b> (poster, video, or paper), <b>a first-draft claim</b> about how your topic changed Texas, and <b>the sources you plan to use</b> (name at least one primary and one secondary).",
  placeholder="My topic is... I will make a... My claim is... My sources will be...",
  reflect_h="Write your project proposal",
  ck1="I named a <b>narrow topic</b> and a <b>format</b>.",
  ck2="I wrote a first-draft <b>claim</b> about how my topic changed Texas.",
  ck3="I named at least one <b>primary</b> and one <b>secondary</b> source.",
  review="Review the source types and the rubric",
  sources='<a href="https://www.tshaonline.org/handbook" target="_blank" rel="noopener">Handbook of Texas Online</a> · <a href="https://texashistory.unt.edu/" target="_blank" rel="noopener">The Portal to Texas History</a> · <a href="https://www.thestoryoftexas.com/" target="_blank" rel="noopener">Bullock Texas State History Museum</a>',
)
