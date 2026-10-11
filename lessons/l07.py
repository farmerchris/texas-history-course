L = dict(
  slug="lesson07", key="tx-lesson7-v1", n=7, label="Lesson 7", short="Texas Revolution",
  title="The Texas Revolution",
  question="How did a small army win independence in seven weeks?",
  teks=["1B", "3B", "3C"],
  read='''  <h2>From Gonzales to San Jacinto</h2>
  <div class="prose">
    <p>In Lesson 6, Santa Anna threw out the Constitution of 1824 and peaceful requests failed. In the fall of 1835, the fighting began. At first, many Texians and Tejanos fought to restore the 1824 Constitution. By March 1836, they were fighting for independence.</p>
  </div>

  <h3>The road to independence</h3>
  <div class="ruler">
    <div class="era"><span class="yr">Oct 2, 1835</span><div><b>Gonzales</b><span>Mexican soldiers came to take back a small cannon. Settlers flew a flag that said "Come and Take It" and drove them off. This was the first battle.</span></div></div>
    <div class="era"><span class="yr">Dec 1835</span><div><b>Siege of Béxar</b><span>Texian and Tejano volunteers, including <b>Juan Seguín</b>'s company, captured San Antonio from Mexican troops.</span></div></div>
    <div class="era"><span class="yr">Feb 23 – Mar 6, 1836</span><div><b>The Alamo</b><span>Santa Anna's army surrounded about 180 to 250 defenders in the old mission. On March 6 the Mexican army stormed the walls. Nearly all the defenders died, including William B. Travis, James Bowie, and David Crockett.</span></div></div>
    <div class="era"><span class="yr">Mar 2, 1836</span><div><b>Convention of 1836</b><span>Delegates at Washington-on-the-Brazos signed the <b>Texas Declaration of Independence</b>. <b>George Childress</b> was its main author. <b>Lorenzo de Zavala</b>, a Mexican federalist leader, signed it and became interim vice president. Sam Houston was named commander of the army.</span></div></div>
    <div class="era"><span class="yr">Mar 27, 1836</span><div><b>Goliad</b><span>Colonel <b>James Fannin</b> surrendered his men after a battle near Goliad. On Santa Anna's orders, about 340 prisoners were executed. "Remember Goliad!" became a battle cry.</span></div></div>
    <div class="era"><span class="yr">Apr 21, 1836</span><div><b>San Jacinto</b><span>Houston's army of about 900 attacked Santa Anna's camp in the afternoon while many soldiers rested. The battle lasted about 18 minutes. Santa Anna was captured the next day and agreed to order his army out of Texas.</span></div></div>
  </div>

  <div class="dates">
    <div class="date"><span class="yr">1836</span><b>Texas declares independence</b><p>This is one of your eight required dates. Add it to your timeline.</p></div>
  </div>

  <h3>Read the source: Travis writes from the Alamo</h3>
  <div class="excerpt">
    <span class="who">William B. Travis, February 24, 1836 · excerpt</span>
    <p>“To the People of Texas &amp; All Americans in the World—</p>
    <p class="line">Fellow Citizens &amp; compatriots—I am besieged, by a thousand or more of the Mexicans under Santa Anna. … The enemy has demanded a surrender at discretion, otherwise, the garrison are to be put to the sword, if the fort is taken—I have answered the demand with a cannon shot, &amp; our flag still waves proudly from the walls—I shall never surrender or retreat.</p>
    <p class="line">Then, I call on you in the name of Liberty, of patriotism &amp; everything dear to the American character, to come to our aid, with all dispatch. … Victory or Death.”</p>
    <p><b>Annotate as you read:</b> Who is his <b>audience</b>? What is his <b>purpose</b>? What words does he choose to <b>persuade</b> them?</p>
  </div>

  <h3>The defenders were a mix of people</h3>
  <div class="prose"><p>The Alamo defenders came from many places. Most were recent arrivals from the United States, but some were born in England, Ireland, Scotland, Germany, and Denmark. Tejanos fought inside the walls too, such as Gregorio Esparza and José Toribio Losoya. Some survivors were women and children, like Susanna Dickinson and Esparza's family, and Joe, a man Travis held in slavery. Juan Seguín survived because Travis sent him out as a messenger to find help.</p></div>

  <h3>Key people</h3>
  <div class="regions">
    <div class="card"><div class="ctop"><b>Sam Houston</b><span class="tag">commander</span></div><p>Retreated east for weeks while his army trained and grew, then struck at San Jacinto.</p></div>
    <div class="card"><div class="ctop"><b>Santa Anna</b><span class="tag">Mexico's president</span></div><p>Led the Mexican army. His orders of no mercy at the Alamo and Goliad angered Texians and brought in volunteers.</p></div>
    <div class="card"><div class="ctop"><b>Juan Seguín</b><span class="tag">Tejano captain</span></div><p>Messenger from the Alamo. His company of Tejanos fought at San Jacinto.</p></div>
    <div class="card"><div class="ctop"><b>Lorenzo de Zavala</b><span class="tag">signer</span></div><p>Helped write Mexico's 1824 constitution, then signed Texas's Declaration of Independence.</p></div>
  </div>

  <div class="callout"><b>How did a small army win?</b> The Alamo and Goliad cost lives but bought time and turned anger into recruits. Houston's long retreat, called the Runaway Scrape for the families who fled with it, kept his army alive. Santa Anna split his forces and let his guard down. When Houston finally attacked, surprise did the rest. Independence was declared on March 2 and won on April 21: seven weeks.</div>''',
  practice=[
    {"type": "order", "title": "Put the map in order", "intro": "Drag the cards, or use the arrows, to put these places in the order the events happened, earliest at the top.", "button": "Check my order", "word": "in the right spot", "seed": 4,
     "items": [["Gonzales: “Come and Take It”", "Oct 1835"], ["Siege of Béxar: San Antonio captured", "Dec 1835"], ["The Alamo is surrounded", "Feb 23, 1836"], ["Convention of 1836 declares independence", "Mar 2, 1836"], ["The Alamo falls", "Mar 6, 1836"], ["Fannin's men are executed at Goliad", "Mar 27, 1836"], ["Victory at San Jacinto", "Apr 21, 1836"]]},
    {"type": "match", "title": "People cards", "intro": "Match each person to their role.", "placeholder": "Choose a person…", "button": "Check my people", "word": "correct",
     "options": ["George Childress", "Lorenzo de Zavala", "James Fannin", "Sam Houston", "Santa Anna", "Juan Seguín", "William B. Travis"],
     "items": [["Main author of the Texas Declaration of Independence", 0], ["Mexican federalist who signed the Declaration and became interim vice president", 1], ["Surrendered near Goliad; he and his men were executed", 2], ["Commanded the army that won at San Jacinto", 3], ["Mexico's president and general, captured after San Jacinto", 4], ["Tejano captain sent out from the Alamo as a messenger", 5], ["Wrote “Victory or Death” from inside the Alamo", 6]]},
    {"type": "mc", "title": "Annotate the Travis letter", "intro": "Use the excerpt above. Pick the best answer.", "button": "Check my answers", "word": "correct",
     "items": [
       {"q": "Who was Travis's audience?", "o": ["Santa Anna", "“The People of Texas & All Americans in the World”", "His family only"], "a": 1, "e": "He addressed anyone who might send help."},
       {"q": "What was his purpose?", "o": ["To surrender", "To get reinforcements to come quickly", "To describe the weather"], "a": 1, "e": "“Come to our aid, with all dispatch.”"},
       {"q": "Which phrase is a persuasive appeal to the reader's values?", "o": ["“in the name of Liberty, of patriotism”", "“a thousand or more”", "“February 24”"], "a": 0, "e": "He appeals to ideals his readers cared about."},
       {"q": "Why is this letter a primary source?", "o": ["It was written by a historian later", "Travis wrote it during the siege", "It is in a textbook"], "a": 1, "e": "Primary sources come from the time and from people involved."}]},
    {"type": "sort", "title": "Turning point or not?", "intro": "Did this help the Texian side win? Pick <b>Helped Texas win</b> or <b>Hurt Texas</b>.", "button": "Check my sorting", "word": "sorted correctly",
     "choices": [["H", "Helped Texas win"], ["X", "Hurt Texas"]],
     "items": [["Houston's retreat kept his army together while it trained", "H", "A beaten army in March would have ended the war."], ["Fannin's men were captured and executed at Goliad", "X", "Texas lost about 340 soldiers, though it fueled anger."], ["Santa Anna split his army into several parts", "H", "That left him with fewer troops at San Jacinto."], ["The Alamo defenders were all killed", "X", "It was a military loss, even though it bought time and became a rallying cry."], ["Houston attacked in the afternoon when Santa Anna's camp was resting", "H", "Surprise made the 18-minute victory possible."], ["Santa Anna was captured alive", "H", "He ordered his army out of Texas to save himself."]]}
  ],
  quiz=[
    {"q": "Where was the first battle of the Texas Revolution?", "o": ["San Jacinto", "Gonzales", "Goliad", "The Alamo"], "a": 1, "e": "“Come and Take It,” October 2, 1835."},
    {"q": "What happened on March 2, 1836?", "o": ["The Alamo fell", "Texas declared independence at Washington-on-the-Brazos", "Santa Anna was captured", "Goliad prisoners were executed"], "a": 1, "e": "1836 is a required date."},
    {"q": "Who was the main author of the Texas Declaration of Independence?", "o": ["George Childress", "Sam Houston", "Stephen F. Austin", "David Crockett"], "a": 0, "e": "Childress drafted it in about a day."},
    {"q": "Why is Lorenzo de Zavala important?", "o": ["He led the Mexican army", "He was a Mexican federalist who signed the Declaration and became interim vice president", "He wrote the Travis letter", "He died at Goliad"], "a": 1, "e": "He shows the Revolution was not only Anglo Texans."},
    {"q": "What did Travis say he would never do?", "o": ["Write again", "Surrender or retreat", "Leave Texas", "Fight"], "a": 1, "e": "“I shall never surrender or retreat.”"},
    {"q": "Which statement about the Alamo defenders is true?", "o": ["They were all born in Texas", "They included Tejanos and people from the U.S. and Europe", "They all survived", "There were 5,000 of them"], "a": 1, "e": "Gregorio Esparza and José Toribio Losoya were among the Tejano defenders."},
    {"q": "What happened at Goliad?", "o": ["Texas won a big victory", "About 340 Texian prisoners were executed on Santa Anna's orders", "Independence was declared", "The Runaway Scrape ended"], "a": 1, "e": "“Remember Goliad!” became a battle cry."},
    {"q": "Why was Sam Houston's retreat important?", "o": ["It kept his army alive to fight on better terms", "It gave Texas to Mexico", "It ended the war", "It started the Alamo siege"], "a": 0, "e": "He struck only when the odds were in his favor."},
    {"q": "How long did the Battle of San Jacinto last?", "o": ["Three days", "About 18 minutes", "Two weeks", "Seven weeks"], "a": 1, "e": "The surprise attack broke Santa Anna's army quickly."},
    {"q": "Which sentence best answers the big question?", "o": ["Texas had a bigger army", "Houston kept his army alive, Santa Anna split his forces, and a surprise attack at San Jacinto won independence seven weeks after it was declared", "Mexico gave up without fighting", "France sent help"], "a": 1, "e": "Strategy and surprise beat numbers."}
  ],
  prompt="In 3 to 5 sentences, explain <b>one turning point</b> of the Texas Revolution and <b>one person's role</b> in it. Make a claim about why it mattered, give evidence from today's lesson, and explain how that evidence supports your claim.",
  placeholder="One turning point of the Texas Revolution was...",
  reflect_h="Explain a turning point",
  ck1="I named a <b>turning point</b> and made a claim about why it mattered.",
  ck2="I described <b>one person's role</b> with specific evidence.",
  review="Review the timeline and the people cards",
  sources='<a href="https://www.battlefields.org/learn/primary-sources/travis-letter-victory-or-death" target="_blank" rel="noopener">Travis letter, Feb. 24, 1836</a> (American Battlefield Trust; original at the Texas State Library and Archives) · <a href="https://www.tshaonline.org/handbook" target="_blank" rel="noopener">Handbook of Texas Online</a>: “Battle of San Jacinto,” “Alamo, Battle of the,” “Goliad Massacre,” “Seguín, Juan Nepomuceno,” “Zavala, Lorenzo de”',
)
