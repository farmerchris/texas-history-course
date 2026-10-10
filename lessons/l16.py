L = dict(
  slug="lesson16", key="tx-lesson16-v1", n=16, label="Lesson 16", short="Texas Government",
  title="Texas Government & Citizenship",
  question="How does the 1876 Constitution shape the government Texans live under today?",
  teks=["1B", "13A", "13B", "14A", "14B", "15A", "15B", "16B", "17A", "23A"],
  quiz_label="Quiz + Checkpoint 3",
  quiz_note="Questions 11–15 review Lessons 11–15 for Checkpoint 3.",
  read='''  <h2>A constitution written in 1876</h2>
  <div class="prose">
    <p>In Lesson 10, Reconstruction ended and Texans reacted against Governor E. J. Davis's powerful state government. In 1876 they wrote a new constitution designed to keep government small and weak. Texas still lives under that constitution today, though voters have amended it more than 500 times.</p>
  </div>

  <div class="dates">
    <div class="date"><span class="yr">1876</span><b>Texas adopts its current constitution</b><p>This is the last of your eight required dates. Your timeline is complete.</p></div>
  </div>

  <h3>Seven constitutions</h3>
  <div class="ruler">
    <div class="era"><span class="yr">1827</span><div><b>Coahuila y Tejas</b><span>Texas as a Mexican state (Lesson 5).</span></div></div>
    <div class="era"><span class="yr">1836</span><div><b>Republic of Texas</b><span>An independent nation (Lesson 8).</span></div></div>
    <div class="era"><span class="yr">1845</span><div><b>Statehood</b><span>Joining the United States.</span></div></div>
    <div class="era"><span class="yr">1861</span><div><b>Confederacy</b><span>Joining the Confederate States (Lesson 10).</span></div></div>
    <div class="era"><span class="yr">1866 · 1869</span><div><b>Reconstruction</b><span>Two constitutions written to rejoin the Union.</span></div></div>
    <div class="era"><span class="yr">1876</span><div><b>Today's constitution</b><span>Limited government after Reconstruction.</span></div></div>
  </div>

  <h3>Read the source: the Texas Bill of Rights</h3>
  <div class="excerpt">
    <span class="who">Texas Constitution, Article 1 · excerpts</span>
    <p class="line">Sec. 1: “Texas is a free and independent State, subject only to the Constitution of the United States…”</p>
    <p class="line">Sec. 2: “All political power is inherent in the people, and all free governments are founded on their authority, and instituted for their benefit.”</p>
    <p>Article 1 lists rights such as freedom of worship, freedom of speech and the press, trial by jury, the right to bear arms, and equality under the law. Like the U.S. Bill of Rights, it protects people from their government. Unlike the U.S. version, it comes <i>first</i> in the constitution.</p>
  </div>

  <h3>Principles you can find in it</h3>
  <div class="regions">
    <div class="card"><div class="ctop"><b>Popular sovereignty</b><span class="tag">Art. 1, Sec. 2</span></div><p>Power comes from the people. Texans vote for many officials and must approve every constitutional amendment.</p></div>
    <div class="card"><div class="ctop"><b>Limited government</b><span class="tag">reaction to 1870s</span></div><p>The governor shares power with other separately elected officials (the lieutenant governor, attorney general, comptroller, and more). The Legislature meets only every other year, for 140 days.</p></div>
    <div class="card"><div class="ctop"><b>Separation of powers</b><span class="tag">three branches</span></div><p>Legislative (150 House members, 31 senators), executive (governor and other officials), and judicial (elected judges, with two top courts).</p></div>
    <div class="card"><div class="ctop"><b>Checks and balances</b><span class="tag">veto · override</span></div><p>The governor can veto bills; the Legislature can override with a two-thirds vote; courts can strike down laws.</p></div>
  </div>

  <h3>Three levels of government close to home</h3>
  <div class="cmpbox"><table class="cmp">
    <thead><tr><th></th><th>City</th><th>County</th><th>State</th></tr></thead>
    <tbody>
      <tr><th>Leaders</th><td>Mayor and city council</td><td>Commissioners court: a county judge and four commissioners</td><td>Governor and Legislature</td></tr>
      <tr><th>Does</th><td>Police, parks, water, trash, local streets</td><td>County roads, jails, courts, elections, records</td><td>State laws, highways, prisons, schools funding</td></tr>
      <tr><th>Pays with</th><td>Property tax, local sales tax, fees, bonds</td><td>Property tax, fees, bonds</td><td>Sales tax (6.25%), oil and gas taxes, fees, federal funds. No state income tax.</td></tr>
    </tbody>
  </table></div>
  <div class="prose"><p>Texas has 254 counties, more than any other state. A <b>bond</b> is borrowed money paid back with interest over many years, and voters usually must approve it. School districts are also local governments with elected boards; property taxes pay for much of your school.</p></div>

  <div class="callout"><b>Citizenship.</b> Rights come with responsibilities: obeying laws, paying taxes, serving on a jury, and voting once you turn 18. Good citizens also stay informed, speak up at public meetings, and volunteer. You can attend a city council or commissioners court meeting right now; they are open to the public.</div>''',
  practice=[
    {"type": "sort", "title": "Texas, U.S., or both?", "intro": "Is this true of the <b>Texas</b> Bill of Rights, the <b>U.S.</b> Bill of Rights, or <b>both</b>?", "button": "Check my sorting", "word": "sorted correctly",
     "choices": [["T", "Texas"], ["U", "U.S."], ["B", "Both"]],
     "items": [["Protects freedom of speech and religion", "B", "Both protect these rights."], ["Comes first, before the rest of the constitution", "T", "The U.S. Bill of Rights was added later as amendments."], ["Protects the right to a trial by jury", "B", "Both guarantee jury trials."], ["Says the state is subject only to the U.S. Constitution", "T", "That's Article 1, Section 1."], ["Is made of the first ten amendments", "U", "Added in 1791."], ["Says political power comes from the people", "T", "Article 1, Section 2. The U.S. version doesn't say it this way, though the Constitution's preamble begins “We the People.”"]]},
    {"type": "match", "title": "Who does it?", "intro": "Which level of government is mainly responsible?", "placeholder": "Choose a level…", "button": "Check my matches", "word": "correct",
     "options": ["City", "County", "State"],
     "items": [["Runs the county jail and courthouse", 1], ["Picks up trash and runs city parks", 0], ["Passes laws for all of Texas", 2], ["Holds elections and keeps land records", 1], ["Builds and maintains interstate highways in Texas", 2], ["Hires the local police department", 0]]},
    {"type": "mc", "title": "Commissioners court simulation", "intro": "Your county wants a new library. It can raise property taxes, ask voters to approve a bond, or charge fees. Pick the best answer.", "button": "Check my answers", "word": "correct",
     "items": [
       {"q": "Who votes on the plan at the county level?", "o": ["The commissioners court: a county judge and four commissioners", "The governor alone", "The U.S. Congress"], "a": 0, "e": "Five members, one vote each."},
       {"q": "If the county uses a bond, what usually has to happen first?", "o": ["Voters must approve it in an election", "The President must sign it", "Nothing; bonds are automatic"], "a": 0, "e": "A bond is borrowed money, so voters weigh in."},
       {"q": "What is one responsibility of a citizen during this decision?", "o": ["Stay informed and speak at the public meeting or vote", "Ignore it", "Refuse to pay all taxes"], "a": 0, "e": "Meetings are open, and citizens can comment."},
       {"q": "Which principle explains why voters get a say?", "o": ["Popular sovereignty", "Monarchy", "Secession"], "a": 0, "e": "Power comes from the people."}]},
    {"type": "order", "title": "Texas constitutions in order", "intro": "Use the arrows to put these constitutions in order, earliest at the top.", "button": "Check my order", "word": "in the right spot", "seed": 14,
     "items": [["Coahuila y Tejas (Mexican state)", "1827"], ["Republic of Texas", "1836"], ["Statehood", "1845"], ["Confederate Texas", "1861"], ["First Reconstruction constitution", "1866"], ["Today's constitution", "1876"]]}
  ],
  quiz=[
    {"q": "What happened in 1876?", "o": ["Texas adopted the constitution it still uses", "Texas joined the U.S.", "Oil was found", "Texas seceded"], "a": 0, "e": "1876 is a required date."},
    {"q": "Why did the 1876 constitution limit government power?", "o": ["Texans reacted against the strong Reconstruction government of E. J. Davis", "Mexico required it", "The U.S. President wrote it", "To give the governor more power"], "a": 0, "e": "Limited government was the goal."},
    {"q": "“All political power is inherent in the people” is an example of…", "o": ["Popular sovereignty", "Checks and balances", "Federalism", "Monarchy"], "a": 0, "e": "Article 1, Section 2."},
    {"q": "How often does the Texas Legislature meet in regular session?", "o": ["Every other year, for 140 days", "Every day", "Once every 10 years", "Only in wartime"], "a": 0, "e": "Part of limited government."},
    {"q": "Who runs a Texas county?", "o": ["A commissioners court", "A mayor", "A president", "A school board"], "a": 0, "e": "A county judge plus four commissioners."},
    {"q": "Which tax does Texas NOT have?", "o": ["A state income tax", "A sales tax", "Property taxes", "Fuel taxes"], "a": 0, "e": "Texas relies on sales and property taxes instead."},
    {"q": "The governor vetoes a bill. What can the Legislature do?", "o": ["Override the veto with a two-thirds vote", "Nothing at all", "Fire the governor", "Ask Mexico"], "a": 0, "e": "That's a check and balance."},
    {"q": "Which is a responsibility of citizenship?", "o": ["Serving on a jury", "Skipping elections", "Ignoring laws", "Refusing to pay taxes"], "a": 0, "e": "Voting begins at 18."},
    {"q": "How many constitutions has Texas had, counting Coahuila y Tejas?", "o": ["Seven", "One", "Three", "Twenty"], "a": 0, "e": "1827, 1836, 1845, 1861, 1866, 1869, 1876."},
    {"q": "Which sentence best answers the big question?", "o": ["The 1876 Constitution created a limited government with power spread among many elected officials, a part-time Legislature, and a Bill of Rights listed first", "The 1876 Constitution gave the governor total power", "Texas has no constitution", "The 1876 Constitution has never changed"], "a": 0, "e": "Use a section or feature as evidence."},
    {"q": "Checkpoint review (Lesson 11): What ended the long cattle drives?", "o": ["Railroads, barbed wire, and windmills", "The Civil War", "Oil", "Hurricanes"], "a": 0, "e": "Cattle could be shipped from Texas."},
    {"q": "Checkpoint review (Lesson 12): What happened in 1901?", "o": ["The Spindletop gusher", "The Galveston hurricane", "Annexation", "The Constitution of 1876"], "a": 0, "e": "It launched the Texas oil boom."},
    {"q": "Checkpoint review (Lesson 13): What caused the Dust Bowl?", "o": ["Drought plus plowing that removed grass holding the soil", "Floods", "Railroads", "Oil wells"], "a": 0, "e": "It hit the Panhandle in the 1930s."},
    {"q": "Checkpoint review (Lesson 14): Barbara Jordan was…", "o": ["The first Black woman from the South elected to the U.S. House", "Founder of LULAC", "A Spindletop driller", "Governor in 1876"], "a": 0, "e": "She was elected in 1972."},
    {"q": "Checkpoint review (Lesson 15): What did the 2022 State Water Plan warn?", "o": ["Population is growing while existing water supplies shrink", "There is too much water", "Texas is shrinking", "Water is free forever"], "a": 0, "e": "Supplies were projected to fall about 18 percent by 2070."}
  ],
  prompt="In 3 to 5 sentences, answer: <b>How does the 1876 Constitution shape the government Texans live under today?</b> Make a claim, give one piece of evidence (a section of Article 1, a principle, or a feature like the plural executive), and explain how it affects Texans now.",
  placeholder="The 1876 Constitution shapes Texas government today by...",
  review="Review the principles cards and the city, county, and state chart",
  sources='<a href="https://statutes.capitol.texas.gov/" target="_blank" rel="noopener">Texas Constitution and Statutes</a> (Article 1) · <a href="https://www.tshaonline.org/handbook" target="_blank" rel="noopener">Handbook of Texas Online</a>: “Constitution of 1876,” “County Government,” “Plural Executive”',
)
