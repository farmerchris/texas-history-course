L = dict(
  slug="lesson05", key="tx-lesson5-v1", n=5, label="Lesson 5", short="Mexican Texas",
  title="Mexican National Texas",
  question="Why did Mexico invite settlers, and why did that plan backfire?",
  teks=["1B", "2D", "2E", "2F", "10A"],
  quiz_label="Quiz + Checkpoint 1",
  quiz_note="Questions 11–15 review Lessons 1–4 for Checkpoint 1.",
  read='''  <h2>From Spanish Texas to Mexican Texas</h2>
  <div class="prose">
    <p>At the end of Lesson 4, Spain still held San Antonio, Goliad, and Nacogdoches, but it never had enough settlers. Then a war in Mexico changed everything.</p>
    <p>In 1810, a priest named <b>Miguel Hidalgo</b> rang the church bell in the town of Dolores and called on the people of Mexico to rise up against Spain. That fight for independence lasted eleven years, and some of it spilled into Texas.</p>
  </div>

  <h3>How Texas became part of Mexico</h3>
  <div class="ruler">
    <div class="era"><span class="yr">1810</span><div><b>Hidalgo's revolt</b><span>Father Hidalgo's call to rebel starts Mexico's war for independence from Spain.</span></div></div>
    <div class="era"><span class="yr">1813</span><div><b>Battle of Medina</b><span>Spanish royal troops crushed a rebel army south of San Antonio. It was the deadliest battle ever fought in Texas. Spain then punished Tejanos who had backed the rebels, and many fled. Texas lost people it badly needed.</span></div></div>
    <div class="era"><span class="yr">1821</span><div><b>Mexico wins independence</b><span>Spain gave up. Texas was now part of the new nation of Mexico. Moses Austin had just won permission to bring American families to Texas, but he died, and his son <b>Stephen F. Austin</b> took over the plan.</span></div></div>
    <div class="era"><span class="yr">1824</span><div><b>A constitution and a new state</b><span>The <b>Constitution of 1824</b> made Mexico a federal republic, with power shared between the nation and its states. Texas was joined to Coahuila to make one state, <b>Coahuila y Tejas</b>, with its capital far away in Saltillo.</span></div></div>
    <div class="era"><span class="yr">1825</span><div><b>Colonization laws</b><span>New laws offered cheap land to families who would become Mexican citizens, follow the Catholic faith, and obey Mexican law. Contractors called <b>empresarios</b> recruited the families.</span></div></div>
  </div>

  <div class="dates">
    <div class="date"><span class="yr">1821</span><b>Mexico wins independence from Spain</b><p>This is one of your eight required dates. Add it to your timeline from Lesson 1.</p></div>
  </div>

  <h3>Why invite settlers?</h3>
  <div class="prose">
    <p>Mexico had the same problem Spain had: a huge land with few people. Comanche and Apache raids made the frontier dangerous, and Mexico worried the United States wanted Texas. Mexican leaders hoped loyal, hardworking settlers would farm the land, pay taxes, and act as a buffer against raids and against the United States.</p>
  </div>

  <h3>The empresarios</h3>
  <div class="regions">
    <div class="card"><div class="ctop"><b>Stephen F. Austin</b><span class="tag">empresario</span></div><p>Brought the first 300 families, called the <b>Old Three Hundred</b>, to the Brazos and Colorado river valleys. He learned Spanish, worked closely with Mexican officials, and is called the Father of Texas.</p></div>
    <div class="card"><div class="ctop"><b>Martín De León</b><span class="tag">empresario</span></div><p>Founded the town of Victoria in 1824. His was the only colony settled mostly by Mexican families.</p></div>
    <div class="card"><div class="ctop"><b>Erasmo Seguín</b><span class="tag">Tejano leader</span></div><p>A San Antonio leader who welcomed the Austins, represented Texas at the meeting that wrote the Constitution of 1824, and pushed for laws that opened Texas to settlers.</p></div>
  </div>

  <h3>Three plans for settling Texas</h3>
  <div class="cmpbox"><table class="cmp">
    <thead><tr><th></th><th>Spain</th><th>Mexico</th><th>Anglo settlers</th></tr></thead>
    <tbody>
      <tr><th>Goal</th><td>Hold the land and convert American Indians</td><td>Fill the land with loyal citizens and block the U.S.</td><td>Get cheap, rich farmland</td></tr>
      <tr><th>Method</th><td>Missions, presidios, towns, ranches</td><td>Empresarios and land grants</td><td>Move in as families, many from the southern U.S.</td></tr>
      <tr><th>Result</th><td>Too few settlers</td><td>Settlers came, but many did not become loyal Mexicans</td><td>Grew fast and soon outnumbered Tejanos</td></tr>
    </tbody>
  </table></div>

  <div class="callout"><b>Slavery and the plan.</b> Many Anglo settlers came from the southern United States to grow cotton, and some brought enslaved African Americans to do the work. Mexico was moving to end slavery, and in 1829 its president abolished it. Texas settlers won an exemption, and some got around the rules by calling enslaved people "indentured servants." This argument over slavery became one more source of conflict between settlers and the government.</div>

  <div class="callout"><b>Why the plan backfired.</b> The plan worked too well. By 1830, settlers from the United States far outnumbered Tejanos. Most lived apart from Mexican towns, spoke English, traded with the U.S., and did not follow Mexican customs or laws closely. Mexico had invited people to protect Texas, and now it worried it might lose Texas to them. That worry is where Lesson 6 begins.</div>''',
  practice=[
    {"type": "order", "title": "Cause chain", "intro": "Drag the cards, or use the arrows, to put these events in order, earliest at the top. Each one led to the next.", "button": "Check my order", "word": "in the right spot", "seed": 3,
     "items": [["Father Hidalgo calls for revolt against Spain", "1810"], ["Royal troops crush rebels at the Battle of Medina", "1813"], ["Mexico wins independence; Stephen F. Austin takes over his father's grant", "1821"], ["The Constitution of 1824 creates the state of Coahuila y Tejas", "1824"], ["A colonization law opens Texas to empresarios", "1825"], ["Mexico's president abolishes slavery; Texas wins an exemption", "1829"]]},
    {"type": "match", "title": "Who or what?", "intro": "Match each clue to the right name.", "placeholder": "Choose one…", "button": "Check my matches", "word": "correct",
     "options": ["Stephen F. Austin", "Martín De León", "Erasmo Seguín", "Constitution of 1824", "Empresario", "Battle of Medina"],
     "items": [["Brought the Old Three Hundred families to Texas", 0], ["Founded Victoria with mostly Mexican families", 1], ["Tejano leader who helped write Mexico's 1824 constitution and welcomed the Austins", 2], ["Made Mexico a federal republic and joined Texas with Coahuila", 3], ["A contractor who recruited settler families in return for land", 4], ["The deadliest battle ever fought in Texas, in 1813", 5]]},
    {"type": "sort", "title": "Whose purpose?", "intro": "Who had this goal or used this method: <b>Spain</b>, <b>Mexico</b>, or <b>Anglo settlers</b>?", "button": "Check my sorting", "word": "sorted correctly",
     "choices": [["S", "Spain"], ["M", "Mexico"], ["A", "Anglo settlers"]],
     "items": [["Build missions to convert American Indians", "S", "That was Spain's main method (Lesson 4)."], ["Offer land through empresario contracts", "M", "Mexico's colonization laws created the empresario system."], ["Find cheap, fertile land to grow cotton", "A", "Rich land was the main draw for families from the U.S."], ["Use loyal settlers as a buffer against the United States", "M", "Mexico hoped new citizens would help keep Texas Mexican."], ["Guard the frontier with presidios", "S", "Spain built forts to protect its missions."], ["Bring enslaved workers to farm cotton", "A", "Many settlers from the southern U.S. brought enslaved people, against Mexico's wishes."]]},
    {"type": "mc", "title": "Why did it backfire?", "intro": "Pick the best answer.", "button": "Check my answers", "word": "correct",
     "items": [
       {"q": "Which fact best shows Mexico's plan worked <i>too</i> well?", "o": ["Few people came", "By 1830, Anglo settlers far outnumbered Tejanos", "Spain took Texas back"], "a": 1, "e": "Mexico got settlers, but so many that Tejanos became a small minority."},
       {"q": "Why did slavery cause conflict?", "o": ["Mexico was moving to end slavery, while many settlers wanted to keep it", "Mexico required every settler to own slaves", "Slavery was never discussed"], "a": 0, "e": "Settlers pushed for exemptions and found ways around Mexico's rules."},
       {"q": "Settlers had to become Mexican citizens and follow the Catholic faith. Why might many settlers not take those rules seriously?", "o": ["They lived far from Mexican officials and kept their own language and customs", "The rules were written in English", "Mexico paid them to ignore the rules"], "a": 0, "e": "Distance and separate communities made the rules hard to enforce."}]}
  ],
  quiz=[
    {"q": "What happened in 1821?", "o": ["Texas won independence", "Mexico won independence from Spain", "San Antonio was founded", "The Alamo fell"], "a": 1, "e": "1821 is one of the eight required dates."},
    {"q": "Who started Mexico's war for independence in 1810?", "o": ["Stephen F. Austin", "Santa Anna", "Father Miguel Hidalgo", "Martín De León"], "a": 2, "e": "Hidalgo's call to revolt began an eleven-year war."},
    {"q": "Why was the Battle of Medina (1813) so harmful to Texas?", "o": ["It destroyed the missions", "Many Tejanos were killed or fled, leaving Texas with even fewer people", "It gave Texas to France", "It started the Civil War"], "a": 1, "e": "Spain's punishment after the battle emptied much of Texas."},
    {"q": "An empresario was…", "o": ["A Spanish priest", "A Mexican soldier", "A contractor who brought settler families in return for land", "A Comanche leader"], "a": 2, "e": "Austin and De León were empresarios."},
    {"q": "What did the Constitution of 1824 do?", "o": ["Made Mexico a federal republic and created the state of Coahuila y Tejas", "Made Texas independent", "Ended Spanish rule in Florida", "Banned all settlers"], "a": 0, "e": "Power was shared between Mexico's national government and its states."},
    {"q": "Why did Mexico invite settlers from the United States?", "o": ["To start a war with Spain", "To fill the land, grow the economy, and buffer against raids and the U.S.", "To spread English", "To build oil wells"], "a": 1, "e": "Like Spain, Mexico had too few people in Texas."},
    {"q": "Which empresario's colony was settled mostly by Mexican families?", "o": ["Stephen F. Austin's", "Martín De León's", "Haden Edwards's", "Moses Austin's"], "a": 1, "e": "De León founded Victoria in 1824."},
    {"q": "Settlers who received land were expected to…", "o": ["Become Mexican citizens and follow the Catholic faith", "Pay taxes to Spain", "Join the U.S. Army", "Move back after five years"], "a": 0, "e": "Many did not follow these rules closely."},
    {"q": "How did many settlers get around Mexico's limits on slavery?", "o": ["They moved to Louisiana", "They called enslaved people indentured servants", "They asked Spain for help", "They didn't; no settlers held slaves"], "a": 1, "e": "Labels changed, but people were still held in bondage."},
    {"q": "Which sentence best answers the big question?", "o": ["Mexico invited settlers to hold Texas, but so many came, with their own language, customs, and slavery, that Mexico feared losing Texas to them", "Mexico never wanted settlers", "Settlers came only from Spain", "The plan worked perfectly and Texas stayed Mexican"], "a": 0, "e": "That fear sets up the Road to Revolution in Lesson 6."},
    {"q": "Checkpoint review (Lesson 1): Which is a primary source?", "o": ["A textbook chapter written in 2020", "A letter written by a settler in 1825", "A museum website summary", "An encyclopedia entry"], "a": 1, "e": "A primary source was made by someone who was there at the time."},
    {"q": "Checkpoint review (Lesson 1): What happened in 1519?", "o": ["Alonso Álvarez de Pineda mapped the Texas coast", "San Antonio was founded", "Mexico won independence", "Texas joined the U.S."], "a": 0, "e": "Pineda's map is the first known map of the Texas coast."},
    {"q": "Checkpoint review (Lesson 2): Which region of Texas is driest, with mountains and basins in the far west?", "o": ["Coastal Plains", "North Central Plains", "Mountains and Basins", "Great Plains"], "a": 2, "e": "El Paso and the Big Bend sit in this region."},
    {"q": "Checkpoint review (Lesson 3): Cabeza de Vaca is important because he…", "o": ["Founded San Antonio", "Wrote the first account of Texas lands and peoples after being shipwrecked", "Built the first mission", "Discovered oil"], "a": 1, "e": "His account is a primary source, with his own point of view."},
    {"q": "Checkpoint review (Lesson 4): What happened in 1718?", "o": ["Mexico won independence", "San Antonio was founded", "La Salle landed", "The Alamo fell"], "a": 1, "e": "A mission and presidio were built on the San Antonio River."}
  ],
  prompt="In 3 to 5 sentences, answer: <b>Why did Mexico invite settlers, and why did that plan backfire?</b> Make a claim, give one piece of evidence from today's lesson (a person, a date, a law, or a number), and explain how your evidence supports your claim.",
  placeholder="Mexico invited settlers because...",
  review="Review the timeline and the three-plan chart",
  sources='<a href="https://www.tshaonline.org/handbook" target="_blank" rel="noopener">Handbook of Texas Online</a>: “Austin, Stephen Fuller,” “Seguín, Erasmo,” “De León, Martín,” “Constitution of 1824,” “Battle of Medina,” “Slavery”',
)
