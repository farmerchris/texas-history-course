L = dict(
  slug='lesson03', key='tx-lesson3-v1', n=3, label='Lesson 3',
  title='Age of Contact',
  title_tag='Age of Contact Lesson 3',
  eyebrow='Lesson 3 of 17',
  question='What did Europeans want from Texas, and what did they find?',
  minutes=90,
  teks=['1B', '2B', '20D'],
  teks_text='TEKS 7.1B, 7.2B, 7.20D',
  read='''<h2>Strangers on the shore</h2>
  <div class="prose">
    <p>In Lesson 2 you met the peoples who had lived in Texas for thousands of years. In <span class="yr">1519</span>, something new appeared off the coast: European ships. Historians call the next period the <b>Age of Contact</b>, the time when American Indians and Europeans first met.</p>
    <p>Why did Europeans come at all? Teachers often sum it up as <b>gold, God, and glory</b>.</p>
  </div>
  <div class="regions">
    <div class="card"><div class="ctop"><b>Gold</b><span class="tag">Wealth</span></div><p>Spain had found silver and gold in Mexico. Explorers hoped Texas held more. They also hunted for a water route to Asia and its spices.</p></div>
    <div class="card"><div class="ctop"><b>God</b><span class="tag">Religion</span></div><p>Spain and France were Catholic countries. Priests traveled with explorers to spread their faith to the people they met.</p></div>
    <div class="card"><div class="ctop"><b>Glory</b><span class="tag">Power and fame</span></div><p>Kings wanted land before rival countries grabbed it. Explorers wanted fame, titles, and rewards for their service.</p></div>
  </div>

  <h3>Who came, and what they found</h3>
  <div class="ruler">
    <div class="era"><span class="yr">1519</span><div><b>Alonso Álvarez de Pineda</b><span>A Spanish captain who sailed the whole Gulf coast looking for a water route to Asia. He found no route, but he drew the first map of the Texas coast.</span></div></div>
    <div class="era"><span class="yr">1528</span><div><b>Cabeza de Vaca and Estevanico</b><span>Part of a Spanish expedition that fell apart. Their rafts washed ashore near Galveston Island. Only a few men survived. They lived among the Karankawa and other peoples for years as captives, traders, and healers.</span></div></div>
    <div class="era"><span class="yr">1536</span><div><b>Four survivors reach Mexico</b><span>Cabeza de Vaca, Estevanico, and two other Spaniards walked across Texas and northern Mexico until they found Spanish soldiers. They told stories of rich cities farther north.</span></div></div>
    <div class="era"><span class="yr">1541</span><div><b>Francisco Vázquez de Coronado</b><span>Led a large army searching for the Seven Cities of Gold. He crossed the Texas Panhandle and found grasslands, huge bison herds, and villages of farmers. He found no gold.</span></div></div>
    <div class="era"><span class="yr">1685</span><div><b>René-Robert Cavelier, Sieur de La Salle</b><span>A French explorer who planned a colony at the mouth of the Mississippi River. He missed it and landed at Matagorda Bay, where he built Fort Saint Louis. Hunger, disease, and conflict ruined the colony. His own men killed him in 1687.</span></div></div>
    <div class="era"><span class="yr">1689</span><div><b>Alonso de León</b><span>A Spanish governor sent to find the French. He found the fort in ruins. Spain now feared France would take Texas, which set up Lesson 4.</span></div></div>
  </div>

  <div class="callout"><b>What did they find?</b> No gold and no shortcut to Asia. They found nations of people with their own leaders and trade, open grasslands full of bison, and a coast that wrecked ships. After Coronado, Spain mostly ignored Texas for about 140 years. It took a French colony to bring Spain back.</div>

  <div class="ps">
    <div><b>Estevanico</b><p>He was an enslaved man from Azemmour, Morocco. He is the first African known to have crossed Texas. He was skilled at learning languages and became the group's go-between. He left no writing of his own, so we only know him through what others wrote.</p></div>
    <div><b>La Belle</b><p>La Salle's ship <i>La Belle</i> sank in Matagorda Bay in 1686. In 1995 Texas Historical Commission archaeologists found it, pumped the water out from around it, and dug it up. Its hull is now on display at the Bullock Museum in Austin.</p></div>
  </div>

  <div class="callout"><b>Contact had a cost.</b> Europeans carried diseases such as smallpox and measles that American Indians had never faced. Their bodies had no defense against them. Over the next two centuries, these diseases killed a huge share of the Native people of Texas, often before many of them had ever met a European.</div>

  <h3>Reading a primary source: whose eyes?</h3>
  <div class="prose">
    <p>Cabeza de Vaca wrote about his journey in a report published in <span class="yr">1542</span>. It is one of the oldest written descriptions of Texas and its people. It is also a source with a strong <b>point of view</b>.</p>
    <p>Ask three questions about any source: <b>Who wrote it? Who was it for? Why?</b> Cabeza de Vaca wrote for the king of Spain. He had lost the expedition and wanted to prove he had still served God and the king well. He hoped for a reward, and he got one: a job as a governor in South America.</p>
    <p>That does not make him a liar. It means some of what he wrote is something he <b>saw</b>, and some is how he <b>interpreted</b> what he saw. Your job in Practice B is to tell the difference.</p>
  </div>''',
  practice=[{'type': 'match',
  'title': "Who's who?",
  'intro': 'Read each clue and pick the person it describes.',
  'placeholder': 'Choose a person…',
  'button': 'Check my matches',
  'word': 'correct',
  'options': ['Álvarez de Pineda', 'Cabeza de Vaca', 'Estevanico', 'Coronado', 'La Salle', 'Alonso de León'],
  'items': [['Sailed the Gulf coast in 1519 and drew the first map of the Texas coast', 0],
            ['Spanish officer who survived a shipwreck, lived among Native peoples for years, and wrote a report about '
             'it',
             1],
            ["Enslaved man from Morocco who survived the same shipwreck and became the group's go-between", 2],
            ['Led a large army across the Panhandle searching for cities of gold', 3],
            ['French explorer who meant to settle near the Mississippi River but landed at Matagorda Bay', 4],
            ['Spanish governor sent to find the French fort, who found it in ruins', 5]]},
 {'type': 'sort',
  'title': 'Saw it, or how he saw it?',
  'intro': 'Read the excerpt. For each line, decide: is it something he could <b>observe</b> with his own eyes, or is '
           'it shaped by his <b>point of view</b>?',
  'before': '<div class="excerpt">\n'
            '      <p class="who">Adapted from Cabeza de Vaca\'s account (1542), retold in modern English</p>\n'
            '      <p class="line">The people of this island hunt with bows and arrows. For part of the year they live '
            'on fish and on roots they pull from under the water.</p>\n'
            '      <p class="line">Of all the people in the world, they love their children the most and treat them '
            'the best.</p>\n'
            '      <p class="line">During the winter there was little food. Many of our men died of cold and '
            'hunger.</p>\n'
            '      <p class="line">The islanders told us to heal their sick. We prayed and made the sign of the cross '
            'over them, and the sick said they were well. We gave thanks to God.</p>\n'
            '      <p class="line">For years I traveled as a trader. I carried shells and sea beads inland and brought '
            'back animal skins and red ochre.</p>\n'
            '      <p class="line">They believed we had come from heaven.</p>\n'
            '    </div>',
  'button': 'Check my sorting',
  'word': 'sorted correctly',
  'choices': [['O', 'Observed'], ['P', 'Point of view']],
  'items': [['They hunt with bows and arrows and eat fish and roots.',
             'O',
             'He could watch them hunt and gather food.'],
            ['Of all the people in the world, they love their children the most.',
             'P',
             'He had not met all the people in the world. This is his opinion, stated as a big claim.'],
            ['During the winter many of our men died of cold and hunger.',
             'O',
             'He lived through it and saw it happen.'],
            ['We prayed over the sick, and they said they were well. We gave thanks to God.',
             'P',
             'He credits his faith for the healing. His readers back in Spain would want to hear that God was on his '
             'side.'],
            ['I carried shells and sea beads inland and brought back skins and red ochre.',
             'O',
             'These are things he did and carried himself.'],
            ['They believed we had come from heaven.',
             'P',
             'He could not see inside their minds. He is guessing what they believed, in a way that makes him look '
             'important.']]},
 {'type': 'order',
  'title': 'Put it in order',
  'intro': 'Use the arrows to put these events in order, earliest at the top. Years appear once an event is in the '
           'right spot.',
  'button': 'Check my order',
  'word': 'in the right spot',
  'seed': 11,
  'items': [['Álvarez de Pineda maps the Texas coast', '1519'],
            ["Cabeza de Vaca's raft washes ashore near Galveston Island", '1528'],
            ['Four survivors reach Spanish soldiers in Mexico', '1536'],
            ["Coronado's army crosses the Panhandle", '1541'],
            ['La Salle builds Fort Saint Louis on Matagorda Bay', '1685'],
            ['<i>La Belle</i> sinks in a storm', '1686'],
            ['Alonso de León finds the French fort in ruins', '1689']]},
 {'type': 'mc',
  'title': 'Cause and effect',
  'intro': 'Every event causes something else. Pick the best answer.',
  'button': 'Check my answers',
  'word': 'correct',
  'items': [{'q': 'Coronado found no gold in 1541. What was one effect?',
             'o': ['Spain sent more armies right away',
                   'Spain mostly ignored Texas for about 140 years',
                   'Spain sold Texas to France'],
             'a': 1,
             'e': 'With no gold to find, Spain had little reason to spend money on Texas.',
             'fixed': True},
            {'q': 'Why did Spain send Alonso de León into Texas in 1689?',
             'o': ['To find and stop the French colony',
                   'To trade bison hides',
                   'To map the Gulf coast for the first time'],
             'a': 0,
             'e': "La Salle's colony made Spain fear France would claim Texas, close to Spain's silver mines in "
                  'Mexico.',
             'fixed': True},
            {'q': 'Why did so many American Indians die after Europeans arrived?',
             'o': ['They had never seen horses',
                   'Europeans brought diseases their bodies could not fight',
                   'Europeans took all the bison'],
             'a': 1,
             'e': 'Smallpox, measles, and other diseases were new in the Americas, so people had no protection against '
                  'them.',
             'fixed': True}]}],
  quiz=[{'q': 'In 1519, who drew the first map of the Texas coast?',
  'o': ['La Salle', 'Coronado', 'Álvarez de Pineda', 'Cabeza de Vaca'],
  'a': 2,
  'e': 'Pineda sailed the Gulf coast looking for a route to Asia and mapped it instead.',
  'fixed': True},
 {'q': 'In “gold, God, and glory,” what does <b>God</b> stand for?',
  'o': ['Finding silver mines', 'Spreading the Catholic faith', 'Winning fame for the king', 'Mapping new rivers'],
  'a': 1,
  'e': 'Priests traveled with explorers to convert the people they met.',
  'fixed': True},
 {'q': 'How did Cabeza de Vaca end up living in Texas?',
  'o': ['The king sent him to build a mission',
        'His expedition fell apart and his raft washed ashore',
        'He was a French prisoner',
        'He was looking for bison'],
  'a': 1,
  'e': "His group's rafts washed ashore near Galveston Island in 1528.",
  'fixed': True},
 {'q': 'Who was Estevanico?',
  'o': ['A French ship captain',
        'A Caddo leader',
        'An enslaved man from Morocco who survived the shipwreck and served as a go-between',
        "Coronado's priest"],
  'a': 2,
  'e': 'He is the first African known to have crossed Texas.',
  'fixed': True},
 {'q': 'What was Coronado searching for?',
  'o': ['The Seven Cities of Gold', 'The mouth of the Mississippi', 'A French fort', 'Cabeza de Vaca'],
  'a': 0,
  'e': "Stories from Cabeza de Vaca's group helped start rumors of rich cities in the north.",
  'fixed': True},
 {'q': 'What did Coronado actually find on the plains?',
  'o': ['Gold and silver', 'Grasslands, bison herds, and farming villages', 'A water route to Asia', 'A French colony'],
  'a': 1,
  'e': 'He found a rich land, just not the kind of riches he wanted.',
  'fixed': True},
 {'q': 'La Salle came to Texas for which country?',
  'o': ['Spain', 'England', 'France', 'Mexico'],
  'a': 2,
  'e': 'He meant to plant a French colony near the Mississippi River.',
  'fixed': True},
 {'q': "Why did La Salle's colony alarm Spain?",
  'o': ['Spain feared France would claim Texas, close to its silver mines in Mexico',
        'La Salle found gold',
        'La Salle attacked Mexico City',
        'Spain wanted La Belle for its navy'],
  'a': 0,
  'e': "A French Texas would put a rival right next to Spain's richest land.",
  'fixed': True},
 {'q': 'Cabeza de Vaca wrote his report for the king of Spain. Why does that matter?',
  'o': ["It doesn't matter at all",
        'It means every word is false',
        'He wanted the king to see him as loyal and faithful, which shaped what he wrote',
        'Kings could not read'],
  'a': 2,
  'e': "A source's audience and purpose shape what the author includes and how he tells it.",
  'fixed': True},
 {'q': 'Which sentence best answers the big question?',
  'o': ['Europeans wanted farmland and found it right away',
        'Europeans wanted gold, faith, and power; they found no gold, but they met many peoples and later competed for '
        'the land',
        'Europeans wanted bison and found them',
        'Europeans came to trade with the Caddo only'],
  'a': 1,
  'e': 'The hopes for gold failed, but contact changed Texas forever and set Spain and France against each other.',
  'fixed': True}],
  quiz_label='Quiz',
  reflect_h='Weigh the source',
  prompt='In 3 to 5 sentences, pick <b>one thing Cabeza de Vaca might have exaggerated or left out</b>, and explain why. Make a claim, give one piece of evidence (a line from the excerpt, or a fact about his audience or purpose), and explain how your evidence supports your claim.',
  placeholder='Cabeza de Vaca might have exaggerated... because...',
  ck1='I named <b>one thing</b> he might have exaggerated or left out.',
  ck2='I gave specific <b>evidence</b> (a line from the excerpt, or his audience or purpose).',
  ck3='I explained <b>why</b> my evidence supports my claim.',
  review='Review the explorer timeline and the point-of-view questions',
  sources='<a href="https://www.tshaonline.org/handbook" target="_blank" rel="noopener">Handbook of Texas Online</a>: “Álvarez de Pineda, Alonso,” “Cabeza de Vaca, Álvar Núñez,” “Estevanico,” “Coronado Expedition,” “La Salle Expedition” · <a href="https://www.thestoryoftexas.com/learn/la-belle-resources/" target="_blank" rel="noopener">Bullock Museum La Belle resources</a>. The excerpt is a plain-language retelling, not a word-for-word translation.',
)
