L = dict(
  slug="lesson06", key="tx-lesson6-v1", n=6, label="Lesson 6", short="Road to Revolution",
  title="Road to Revolution",
  question="Was the Texas Revolution inevitable after 1830?",
  teks=["3A", "16A", "20D"],
  read='''  <h2>Trust breaks down, one step at a time</h2>
  <div class="prose">
    <p>Lesson 5 ended with a problem. Mexico invited settlers to hold Texas, and now settlers from the United States far outnumbered Tejanos. Between 1826 and 1835, a chain of events turned that worry into open conflict.</p>
    <p>As you read, ask the historian's question: <b>inevitable</b> means it was bound to happen no matter what. Could anyone have stopped this chain? Look at each step from two sides: the Mexican government's and the Texians' (Anglo settlers in Texas).</p>
  </div>

  <h3>Five steps toward revolution</h3>
  <div class="ruler">
    <div class="era"><span class="yr">1826</span><div><b>Fredonian Rebellion</b><span>Empresario Haden Edwards fought with Mexican officials over land titles in Nacogdoches. His brother declared an independent "Republic of Fredonia." Mexican troops, joined by Stephen F. Austin's militia, ended it quickly in early 1827. Even so, Mexico now suspected Anglo settlers.</span><em>Mexican view: proof settlers might rebel. Texian view: a few hotheads, not the colonies.</em></div></div>
    <div class="era"><span class="yr">1828</span><div><b>The Terán Report</b><span>General Manuel de Mier y Terán toured Texas. He reported that Anglos far outnumbered Mexicans in East Texas, kept their own schools and customs, and traded mostly with the U.S. He warned that Mexico could lose Texas.</span><em>Mexican view: a warning to act now. Texian view: they hardly knew it existed.</em></div></div>
    <div class="era"><span class="yr">1830</span><div><b>Law of April 6, 1830</b><span>Mexico banned further immigration from the United States, sent more soldiers, collected taxes on imports, and banned bringing in more enslaved people.</span><em>Mexican view: protecting its border. Texian view: an attack on their families still trying to come, and on their trade.</em></div></div>
    <div class="era"><span class="yr">1832</span><div><b>Turtle Bayou Resolutions</b><span>After clashes with a Mexican commander at Anahuac, Texians wrote these resolutions. They said they were loyal Mexicans who supported General Santa Anna and the federal Constitution of 1824, and only opposed officials who broke it.</span><em>Mexican view: an armed uprising. Texian view: defending Mexico's own constitution.</em></div></div>
    <div class="era"><span class="yr">1834</span><div><b>Austin's arrest</b><span>Austin traveled to Mexico City to ask for separate statehood for Texas and repeal of the immigration ban. On his way home he was arrested and held for about a year and a half without a trial.</span><em>Mexican view: punishing a letter that sounded like a threat. Texian view: if even Austin was jailed, peaceful requests had failed.</em></div></div>
  </div>

  <div class="callout"><b>The final push.</b> In 1834 and 1835, Santa Anna switched sides. He threw out the federal Constitution of 1824 and took power for the central government. When the state of Zacatecas resisted, his army crushed it. Federalists across Mexico, including many Tejanos, were alarmed. Austin came home in 1835 and said war was the only remedy. In October, fighting began at Gonzales.</div>

  <h3>Reading a document: the Turtle Bayou Resolutions</h3>
  <div class="excerpt">
    <span class="who">Summary of the main points, June 1832</span>
    <p class="line">The writers said they were loyal citizens of Mexico.</p>
    <p class="line">They supported General Santa Anna, who was then fighting for the Constitution of 1824.</p>
    <p class="line">They said they took up arms only against officials who ignored that constitution.</p>
    <p><b>Think:</b> Why would Texians stress their loyalty to Mexico in 1832? Who was the audience?</p>
  </div>''',
  practice=[
    {"type": "order", "title": "Sequence the event cards", "intro": "Drag the cards, or use the arrows, to put the events in order, earliest at the top.", "button": "Check my order", "word": "in the right spot", "seed": 5,
     "items": [["Fredonian Rebellion in Nacogdoches", "1826"], ["Terán tours Texas and warns Mexico", "1828"], ["Law of April 6 bans U.S. immigration", "1830"], ["Turtle Bayou Resolutions", "1832"], ["Austin is arrested on his way home", "1834"], ["Fighting begins at Gonzales", "1835"]]},
    {"type": "sort", "title": "Two points of view", "intro": "Who would most likely say this: a <b>Mexican official</b> or a <b>Texian settler</b>?", "button": "Check my sorting", "word": "sorted correctly",
     "choices": [["M", "Mexican official"], ["T", "Texian settler"]],
     "items": [["“These settlers keep their own language and trade with the United States. We could lose Texas.”", "M", "That is the warning in the Terán Report."], ["“Our relatives back in Tennessee can't join us now. That's unfair.”", "T", "The Law of April 6, 1830 stopped new U.S. immigration."], ["“We need more soldiers and customs houses in Texas.”", "M", "Mexico sent troops and collected taxes to control the border."], ["“We are loyal to the Constitution of 1824, not to officials who break it.”", "T", "That is the message of the Turtle Bayou Resolutions."], ["“Austin's letter suggested Texas might act on its own. He must be held.”", "M", "Officials saw a letter Austin wrote as a threat."], ["“If Austin can be jailed for asking politely, asking doesn't work.”", "T", "Austin's arrest convinced many that peaceful petitions had failed."]]},
    {"type": "match", "title": "Rate the tension", "intro": "For each event, how much did it raise tension between Mexico and the Texians? Historians disagree, but each choice below matches the most common view.", "placeholder": "Choose a level…", "button": "Check my ratings", "word": "matching the common view",
     "options": ["Small: a local fight", "Medium: built distrust", "Large: hit many people at once"],
     "items": [["Fredonian Rebellion (quickly put down, Austin helped Mexico)", 0], ["Terán Report (a warning most settlers never saw)", 1], ["Law of April 6, 1830 (stopped immigration and added taxes)", 2], ["Austin's arrest (the most trusted settler leader jailed)", 2], ["Santa Anna ends the Constitution of 1824", 2]]},
    {"type": "mc", "title": "Inevitable or not?", "intro": "Pick the best answer.", "button": "Check my answers", "word": "correct",
     "items": [
       {"q": "Which fact is the best evidence that war was <i>not</i> inevitable in 1832?", "o": ["Texians said they were loyal Mexicans who supported Santa Anna", "Fighting began at Gonzales", "Austin was arrested"], "a": 0, "e": "In 1832, Texians still wanted to stay in Mexico."},
       {"q": "Which change hurt Tejanos as well as Anglo settlers?", "o": ["The Fredonian Rebellion", "Santa Anna ending the federal Constitution of 1824", "The Terán Report"], "a": 1, "e": "Many Tejano federalists opposed Santa Anna's central rule."},
       {"q": "Why do historians look at both Mexican and Texian viewpoints?", "o": ["To decide which side was evil", "Because each side saw the same events very differently, and both views explain what happened", "Because only one side wrote anything down"], "a": 1, "e": "Point of view shapes how people understand the same event (SE 20D)."}]}
  ],
  quiz=[
    {"q": "What was the Fredonian Rebellion?", "o": ["A Comanche raid on San Antonio", "An empresario's failed attempt to create an independent republic around Nacogdoches", "The first battle of the Texas Revolution", "A Mexican army mutiny"], "a": 1, "e": "Haden Edwards's revolt failed, but it made Mexico suspicious."},
    {"q": "What did General Mier y Terán report in 1828?", "o": ["That Texas had gold", "That Anglos outnumbered Mexicans in East Texas and Mexico could lose Texas", "That Texas should join the U.S.", "That settlers were very loyal"], "a": 1, "e": "His report led to the Law of April 6, 1830."},
    {"q": "Which was part of the Law of April 6, 1830?", "o": ["Free land for all U.S. citizens", "A ban on immigration from the United States", "Texas becoming its own state", "An end to all taxes"], "a": 1, "e": "Mexico also sent troops and taxed imports."},
    {"q": "The Turtle Bayou Resolutions said Texians…", "o": ["Wanted independence right away", "Were loyal to Mexico and the Constitution of 1824", "Wanted to join France", "Supported the Law of April 6"], "a": 1, "e": "In 1832, they still hoped to work within Mexico."},
    {"q": "Why did Stephen F. Austin go to Mexico City in 1833?", "o": ["To ask for separate statehood and an end to the immigration ban", "To sell land", "To join the army", "To surrender Texas"], "a": 0, "e": "He was arrested on the way home."},
    {"q": "How did Santa Anna's actions in 1834–1835 push Texas toward war?", "o": ["He gave Texas independence", "He threw out the federal Constitution of 1824 and centralized power", "He moved to Texas", "He banned the Catholic Church"], "a": 1, "e": "Federalists, Anglo and Tejano, saw their rights taken away."},
    {"q": "Where did fighting begin in October 1835?", "o": ["Gonzales", "San Jacinto", "El Paso", "Galveston"], "a": 0, "e": "Lesson 7 starts there."},
    {"q": "From the Mexican government's point of view, the Law of April 6, 1830 was…", "o": ["A way to protect its border and keep Texas", "A gift to settlers", "A trade deal with the U.S.", "Meaningless"], "a": 0, "e": "Mexico feared losing Texas to the United States."},
    {"q": "Which event shows tension involving slavery?", "o": ["The Law of April 6, 1830 banned bringing in more enslaved people", "The Turtle Bayou Resolutions", "The Terán Report praised slavery", "None; slavery was not an issue"], "a": 0, "e": "Many settlers depended on enslaved labor to grow cotton."},
    {"q": "Which claim is best supported by the events in this lesson?", "o": ["War was certain from the day the first settlers arrived", "Each step made compromise harder, and Santa Anna's end of the 1824 Constitution made war very likely by 1835", "Mexico wanted war in 1826", "Texians never tried peaceful petitions"], "a": 1, "e": "A strong claim uses the evidence, including the attempts at peace."}
  ],
  prompt="In 3 to 5 sentences, answer: <b>What was the single most important cause of the Texas Revolution?</b> Make a claim, give one piece of evidence from today's lesson (an event, a date, a law, or a person), and explain why it mattered more than the others.",
  placeholder="The most important cause of the Texas Revolution was...",
  ck2="I gave specific <b>evidence</b> (an event, a date, a law, or a person).",
  ck3="I explained <b>why</b> my cause mattered more than the others.",
  review="Review the five steps and both points of view",
  sources='<a href="https://www.tshaonline.org/handbook" target="_blank" rel="noopener">Handbook of Texas Online</a>: “Fredonian Rebellion,” “Mier y Terán, Manuel de,” “Law of April 6, 1830,” “Turtle Bayou Resolutions,” “Austin, Stephen Fuller”',
)
