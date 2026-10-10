L = dict(
  slug="lesson13", key="tx-lesson13-v1", n=13, label="Lesson 13", short="Reform, Depression & War",
  title="Reform, Depression & the World Wars",
  question="How did national crises reshape Texas from 1900 to 1945?",
  teks=["7C", "7E", "9B", "17B", "18D"],
  read='''  <h2>Four big shocks in 45 years</h2>
  <div class="prose">
    <p>Between 1900 and 1945, the whole nation faced reform movements, a world war, a deep depression, and a second world war. Each one reached into Texas and changed its politics, its economy, and daily life. As you read, tag each change as <b>political</b> (government and voting), <b>economic</b> (jobs and money), or <b>social</b> (how people live together).</p>
  </div>

  <h3>Reform</h3>
  <div class="regions">
    <div class="card"><div class="ctop"><b>Populists</b><span class="tag">1890s</span></div><p>Farmers angry at railroads and banks formed the People's Party. They lost most elections, but many of their ideas, like regulating big business, were later adopted.</p></div>
    <div class="card"><div class="ctop"><b>Progressives</b><span class="tag">1900s–1910s</span></div><p>Reformers wanted cleaner, more efficient government. After the 1900 storm (Lesson 12), Galveston invented the city commission form of government, which spread nationwide.</p></div>
    <div class="card"><div class="ctop"><b>Woman suffrage</b><span class="tag">1918–19</span></div><p>Leaders like Minnie Fisher Cunningham and Jane Y. McCallum won Texas women the right to vote in primaries in 1918. In 1919, Texas became the first Southern state to approve the 19th Amendment.</p></div>
  </div>

  <h3>The wars and the Depression</h3>
  <div class="ruler">
    <div class="era"><span class="yr">1917–18</span><div><b>World War I</b><span>Nearly 200,000 Texans served. Army camps and airfields opened across Texas, including Kelly Field in San Antonio, because of the mild weather and open land.</span></div></div>
    <div class="era"><span class="yr">1929</span><div><b>The Great Depression begins</b><span>Prices for cotton and oil collapsed. Farmers lost their land and workers lost jobs.</span></div></div>
    <div class="era"><span class="yr">1930s</span><div><b>The Dust Bowl</b><span>Years of drought and over-plowing on the southern plains let wind strip away topsoil. Huge dust storms rolled over the Panhandle, burying fences and ruining crops.</span></div></div>
    <div class="era"><span class="yr">1933–39</span><div><b>The New Deal</b><span>Federal programs put people to work. The Civilian Conservation Corps built Texas state parks, such as Palo Duro Canyon and Bastrop. Texans in Washington helped lead it: Vice President <b>John Nance Garner</b> of Uvalde and Congressman <b>Sam Rayburn</b>, who later became the longest-serving Speaker of the House and pushed to bring electricity to rural Texas.</span></div></div>
    <div class="era"><span class="yr">1941–45</span><div><b>World War II</b><span>About 750,000 Texans served, including about 12,000 women. Admiral Chester Nimitz of Fredericksburg commanded the Pacific Fleet. Doris Miller of Waco was honored for heroism at Pearl Harbor. Oveta Culp Hobby led the Women's Army Corps. Bases, shipyards, and factories boomed, pulling Texans from farms into cities.</span></div></div>
  </div>

  <div class="callout"><b>Why do these crises matter for Texas?</b> They pushed Texas from a farm state toward a city and factory state. By 1950, most Texans lived in cities for the first time. They also tied Texas more closely to the national government, which now built parks, paid farmers, and set up military bases across the state.</div>

  <h3>Texas voices of the era</h3>
  <div class="regions">
    <div class="card"><div class="ctop"><b>J. Frank Dobie</b><span class="tag">writer</span></div><p>Collected and retold Texas folk tales about longhorns, mustangs, and vaqueros.</p></div>
    <div class="card"><div class="ctop"><b>Walter Prescott Webb</b><span class="tag">historian</span></div><p>Wrote <i>The Great Plains</i>, showing how the dry land shaped the people who lived on it.</p></div>
    <div class="card"><div class="ctop"><b>Elisabet Ney</b><span class="tag">sculptor</span></div><p>Carved statues of Sam Houston and Stephen F. Austin that stand in the Texas and U.S. Capitols.</p></div>
    <div class="card"><div class="ctop"><b>Scott Joplin</b><span class="tag">composer</span></div><p>Grew up in Texarkana and became the "King of Ragtime."</p></div>
  </div>''',
  practice=[
    {"type": "sort", "title": "Gallery walk: tag the impact", "intro": "Picture each photo in a gallery. Tag its main impact as <b>political</b>, <b>economic</b>, or <b>social</b>.", "button": "Check my tags", "word": "tagged like a historian would",
     "choices": [["P", "Political"], ["E", "Economic"], ["S", "Social"]],
     "items": [["Women lined up to vote in a 1918 primary", "P", "Voting is political."], ["A Panhandle farm buried by a dust storm", "E", "Ruined crops meant lost income."], ["CCC workers building a stone cabin at a state park", "E", "The New Deal created jobs."], ["A family leaving the farm to work at a wartime shipyard in Houston", "S", "The move to cities changed daily life."], ["Galveston's city commissioners at work after 1900", "P", "A new form of government."], ["Women in uniform at a Texas Army base during WWII", "S", "Women's roles changed during the war."]]},
    {"type": "match", "title": "Who's who", "intro": "Match each person to the right description.", "placeholder": "Choose a person…", "button": "Check my matches", "word": "correct",
     "options": ["John Nance Garner", "Sam Rayburn", "Minnie Fisher Cunningham", "Chester Nimitz", "J. Frank Dobie", "Doris Miller"],
     "items": [["Texas vice president under Franklin Roosevelt", 0], ["Longest-serving Speaker of the House; pushed rural electrification", 1], ["Led the fight for Texas women's right to vote", 2], ["Commanded the U.S. Pacific Fleet in WWII", 3], ["Writer who retold Texas folk tales", 4], ["Waco sailor honored for heroism at Pearl Harbor", 5]]},
    {"type": "order", "title": "Put it in order", "intro": "Use the arrows to put these in order, earliest at the top.", "button": "Check my order", "word": "in the right spot", "seed": 11,
     "items": [["Galveston creates commission government", "1901"], ["U.S. enters World War I", "1917"], ["Texas approves the 19th Amendment", "1919"], ["The Great Depression begins", "1929"], ["CCC begins building state parks", "1933"], ["U.S. enters World War II", "1941"]]},
    {"type": "mc", "title": "Cause and effect", "intro": "Pick the best answer.", "button": "Check my answers", "word": "correct",
     "items": [
       {"q": "What caused the Dust Bowl?", "o": ["Drought plus plowing that removed the grass holding the soil", "Too much rain", "Oil wells"], "a": 0, "e": "Human actions and geography together caused it (SE 9B)."},
       {"q": "What was one effect of World War II on Texas?", "o": ["Many Texans moved from farms to cities for war jobs", "Texas lost all its bases", "Cotton became the only industry"], "a": 0, "e": "Urbanization sped up."},
       {"q": "Why did the military build so many bases in Texas?", "o": ["Mild weather and lots of open land", "Texas asked to be left alone", "It had no other land"], "a": 0, "e": "Good flying weather made Texas ideal for training."}]}
  ],
  quiz=[
    {"q": "Which group of the 1890s was made up mostly of angry farmers?", "o": ["The Populists (People's Party)", "The Republicans", "The Whigs", "The Federalists"], "a": 0, "e": "They fought railroads and banks."},
    {"q": "What did Galveston invent after the 1900 storm?", "o": ["The commission form of city government", "The airplane", "The cattle drive", "The oil well"], "a": 0, "e": "Many cities copied it."},
    {"q": "In 1919, Texas became the first Southern state to…", "o": ["Approve the 19th Amendment for woman suffrage", "Leave the Union", "Build an airport", "End the Depression"], "a": 0, "e": "Texas women had voted in primaries since 1918."},
    {"q": "What was the Dust Bowl?", "o": ["Drought and dust storms on the southern plains in the 1930s", "A football game", "A flood in Houston", "An oil boom"], "a": 0, "e": "It hit the Panhandle hard."},
    {"q": "What did the Civilian Conservation Corps do in Texas?", "o": ["Built state parks and gave young men jobs", "Drilled oil wells", "Fought in WWI", "Wrote the Constitution"], "a": 0, "e": "Palo Duro Canyon and Bastrop are examples."},
    {"q": "John Nance Garner was…", "o": ["Vice president of the United States", "A Comanche leader", "A ragtime composer", "Governor during the Civil War"], "a": 0, "e": "He was from Uvalde."},
    {"q": "Sam Rayburn helped bring what to rural Texas?", "o": ["Electricity", "Railroads", "Oil", "Cattle"], "a": 0, "e": "Rural electrification changed farm life."},
    {"q": "About how many Texans served in World War II?", "o": ["About 750,000", "About 7,500", "About 75", "About 7.5 million"], "a": 0, "e": "Including about 12,000 women."},
    {"q": "Elisabet Ney is known for…", "o": ["Sculptures of Sam Houston and Stephen F. Austin", "Founding LULAC", "Drilling Spindletop", "Leading the Dust Bowl relief"], "a": 0, "e": "Her statues stand in two Capitols."},
    {"q": "Which sentence best answers the big question?", "o": ["Reform, war, and depression gave women the vote, brought federal programs and bases, and moved Texans from farms to cities", "Texas was untouched by national events", "Texas got poorer every year until 1945", "Only farmers were affected"], "a": 0, "e": "Name a crisis, an effect, and evidence."}
  ],
  prompt="Cause-and-effect claim. Pick <b>one</b> crisis (reform, World War I, the Depression and Dust Bowl, or World War II). In 3 to 5 sentences, explain <b>how it reshaped Texas</b>. Make a claim, give one piece of evidence, and say whether the effect was political, economic, or social.",
  placeholder="The crisis that reshaped Texas the most was...",
  reflect_h="Explain one cause and effect",
  ck3="I explained the <b>effect</b> and said whether it was political, economic, or social.",
  review="Review the timeline and the gallery tags",
  sources='<a href="https://www.tshaonline.org/handbook" target="_blank" rel="noopener">Handbook of Texas Online</a>: “Populism,” “Woman Suffrage,” “Dust Bowl,” “Civilian Conservation Corps,” “Garner, John Nance,” “Rayburn, Samuel Taliaferro,” “World War II,” “Dobie, James Frank,” “Ney, Elisabet,” “Joplin, Scott”',
)
