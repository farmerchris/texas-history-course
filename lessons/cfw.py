L = dict(
  slug="cfw", key="tx-cfw-v1", n=None, label="Celebrate Freedom Week", title_tag="Celebrate Freedom Week",
  eyebrow="Celebrate Freedom Week (required)",
  title="Celebrate Freedom Week",
  question="How have the ideas in the Declaration of Independence shaped freedom in Texas and the nation?",
  teks=[], teks_text="Required by 19 TAC §113.19(b)(7)", minutes=60,
  read='''  <h2>Ideas that started a nation</h2>
  <div class="prose">
    <p>Every year, Texas schools set aside a week, usually around Constitution Day on September 17, to study the nation's founding documents. This lesson can be done any time, but it is required. You will read the most famous words of the <b>Declaration of Independence</b>, learn what the <b>U.S. Constitution</b> and <b>Bill of Rights</b> do, trace the Declaration's ideas through Texas history, and recite the required passage.</p>
  </div>

  <h3>Three founding documents</h3>
  <div class="regions">
    <div class="card"><div class="ctop"><b>Declaration of Independence</b><span class="tag">1776</span></div><p>Written mainly by Thomas Jefferson. It explained why the thirteen colonies were breaking from Great Britain and stated the ideas of natural rights and government by consent.</p></div>
    <div class="card"><div class="ctop"><b>U.S. Constitution</b><span class="tag">1787</span></div><p>Signed on September 17, 1787. It set up the federal government with three branches, separation of powers, and checks and balances. It begins, “We the People.”</p></div>
    <div class="card"><div class="ctop"><b>Bill of Rights</b><span class="tag">1791</span></div><p>The first ten amendments to the Constitution. They protect freedoms of religion, speech, press, and assembly, the right to bear arms, and the rights of people accused of crimes, among others.</p></div>
  </div>

  <h3>The required passage</h3>
  <div class="excerpt">
    <span class="who">Declaration of Independence, July 4, 1776</span>
    <p class="line">“We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.—That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed.”</p>
  </div>

  <h3>What the words mean</h3>
  <div class="regions">
    <div class="card"><div class="ctop"><b>Self-evident</b><span class="tag">phrase</span></div><p>So clearly true that it needs no proof.</p></div>
    <div class="card"><div class="ctop"><b>Unalienable rights</b><span class="tag">phrase</span></div><p>Rights that cannot be taken away or given up, because people are born with them.</p></div>
    <div class="card"><div class="ctop"><b>Instituted</b><span class="tag">word</span></div><p>Set up or created. Governments exist to protect rights.</p></div>
    <div class="card"><div class="ctop"><b>Consent of the governed</b><span class="tag">phrase</span></div><p>A government gets its power from the agreement of the people it governs.</p></div>
  </div>

  <h3>Tracing the ideas forward</h3>
  <div class="ruler">
    <div class="era"><span class="yr">1836</span><div><b>Texas Declaration of Independence</b><span>Texans borrowed Jefferson's model (Lesson 7). It said a government that stops protecting “the lives, liberty and property of the people” loses its right to rule, then listed complaints, such as Mexico's failure to set up public schools or guarantee trial by jury.</span></div></div>
    <div class="era"><span class="yr">1830s–1865</span><div><b>Abolition</b><span>Abolitionists such as Frederick Douglass pointed out that a nation that declared “all men are created equal” still held millions of people in slavery. The Declaration's words became an argument against slavery, which ended with the 13th Amendment in 1865. In Texas, freedom was announced on June 19, 1865 (Lesson 10).</span></div></div>
    <div class="era"><span class="yr">1848–1920</span><div><b>Women's suffrage</b><span>At Seneca Falls in 1848, reformers rewrote the line as “all men and women are created equal.” Women won the vote with the 19th Amendment in 1920; Texas approved it in 1919 (Lesson 13).</span></div></div>
    <div class="era"><span class="yr">1900s</span><div><b>Civil rights</b><span>Leaders such as Barbara Jordan appealed to the founding documents to demand equal treatment (Lesson 14).</span></div></div>
  </div>

  <div class="callout"><b>A promise that grew.</b> In 1776, “all men are created equal” did not include enslaved people, women, or American Indians in practice. The ideas were bigger than the society that wrote them. Over 250 years, Americans used those same words to widen who counted as equal.</div>''',
  practice=[
    {"type": "order", "title": "Rebuild the passage", "intro": "Drag the cards, or use the arrows, to put the phrases of the required passage in order. Then practice saying it aloud until you can recite it from memory.", "button": "Check my order", "word": "in the right spot", "seed": 15,
     "items": [["We hold these truths to be self-evident,", "1"], ["that all men are created equal,", "2"], ["that they are endowed by their Creator with certain unalienable Rights,", "3"], ["that among these are Life, Liberty and the pursuit of Happiness.", "4"], ["That to secure these rights, Governments are instituted among Men,", "5"], ["deriving their just powers from the consent of the governed.", "6"]]},
    {"type": "match", "title": "Which document?", "intro": "Match each description to the right document.", "placeholder": "Choose a document…", "button": "Check my matches", "word": "correct",
     "options": ["Declaration of Independence (1776)", "U.S. Constitution (1787)", "Bill of Rights (1791)", "Texas Declaration of Independence (1836)"],
     "items": [["Explained why the colonies broke from Britain", 0], ["Created three branches of the federal government", 1], ["The first ten amendments, protecting freedoms like speech and religion", 2], ["Complained that Mexico failed to set up public schools", 3], ["Begins with “We the People”", 1], ["Says rights come from the Creator and cannot be taken away", 0]]},
    {"type": "mc", "title": "Close reading", "intro": "Pick the best answer.", "button": "Check my answers", "word": "correct",
     "items": [
       {"q": "According to the passage, why are governments created?", "o": ["To secure people's rights", "To collect taxes", "To build armies"], "a": 0, "e": "“To secure these rights, Governments are instituted.”"},
       {"q": "Where does a government get its “just powers”?", "o": ["From the consent of the governed", "From the king", "From the army"], "a": 0, "e": "That's popular sovereignty, also in Texas's Article 1 (Lesson 16)."},
       {"q": "How did women's rights reformers use the Declaration at Seneca Falls?", "o": ["They rewrote it to say “all men and women are created equal”", "They ignored it", "They burned it"], "a": 0, "e": "They held the nation to its own words."}]}
  ],
  quiz=[
    {"q": "Who wrote most of the Declaration of Independence?", "o": ["Thomas Jefferson", "George Washington", "Sam Houston", "Abraham Lincoln"], "a": 0, "e": "It was adopted July 4, 1776."},
    {"q": "What does “unalienable” mean?", "o": ["Cannot be taken away", "From another country", "Optional", "Temporary"], "a": 0, "e": "People are born with these rights."},
    {"q": "Which three rights does the passage name?", "o": ["Life, Liberty, and the pursuit of Happiness", "Speech, press, and religion", "Food, water, and shelter", "Land, money, and votes"], "a": 0, "e": "“Among these are” means the list isn't complete."},
    {"q": "When was the U.S. Constitution signed?", "o": ["September 17, 1787", "July 4, 1776", "March 2, 1836", "June 19, 1865"], "a": 0, "e": "That's why Constitution Day is September 17."},
    {"q": "What is the Bill of Rights?", "o": ["The first ten amendments to the Constitution", "A list of taxes", "The Texas Declaration", "A law from 1876"], "a": 0, "e": "Ratified in 1791."},
    {"q": "“Consent of the governed” means…", "o": ["Government's power comes from the people", "The king decides", "Only soldiers vote", "Laws need no approval"], "a": 0, "e": "This idea is in the Texas Constitution too."},
    {"q": "How did the 1836 Texas Declaration of Independence connect to the 1776 Declaration?", "o": ["It used the same idea that a government that fails to protect rights loses its right to rule", "It copied the Constitution", "It rejected all of Jefferson's ideas", "It had no connection"], "a": 0, "e": "Then it listed complaints against Mexico."},
    {"q": "How did abolitionists use the Declaration?", "o": ["They argued slavery violated “all men are created equal”", "They used it to defend slavery", "They never mentioned it", "They wanted to repeal it"], "a": 0, "e": "Frederick Douglass made this argument powerfully."},
    {"q": "Which amendment gave women the right to vote?", "o": ["The 19th", "The 1st", "The 13th", "The 10th"], "a": 0, "e": "Texas approved it in 1919."},
    {"q": "Which sentence best answers the big question?", "o": ["The Declaration's ideas of equality and consent inspired Texas independence and were later used to end slavery and win rights for women and others", "The Declaration only mattered in 1776", "The Declaration created the Texas Legislature", "The Declaration said nothing about rights"], "a": 0, "e": "The promise widened over time."}
  ],
  prompt="In 3 to 5 sentences, answer: <b>How have the ideas in the Declaration of Independence shaped freedom in Texas or the nation?</b> Quote or explain one phrase from the required passage, and connect it to one later event (1836, abolition, women's suffrage, or civil rights).",
  placeholder="The phrase “...” shaped freedom because...",
  ck1="I made a clear <b>claim</b> and used a phrase from the passage.",
  ck2="I connected it to a <b>later event</b> with specific evidence.",
  ck3="I can <b>recite the required passage</b> from memory to a parent.",
  review="Practice the passage aloud and review the timeline",
  sources='<a href="https://www.archives.gov/founding-docs/declaration-transcript" target="_blank" rel="noopener">Declaration of Independence transcript</a> (National Archives) · <a href="https://www.archives.gov/founding-docs/bill-of-rights-transcript" target="_blank" rel="noopener">Bill of Rights transcript</a> (National Archives) · <a href="https://www.tshaonline.org/handbook" target="_blank" rel="noopener">Handbook of Texas Online</a>: “Texas Declaration of Independence”',
)
