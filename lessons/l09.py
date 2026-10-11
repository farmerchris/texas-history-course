L = dict(
  slug="lesson09", key="tx-lesson9-v1", n=9, label="Lesson 9", short="Early Statehood",
  title="Early Statehood & the U.S.–Mexican War",
  question="How did statehood change Texas's borders and population?",
  teks=["4C", "10A", "10B"],
  read='''  <h2>A new state, a war, and a new shape</h2>
  <div class="prose">
    <p>In Lesson 8, Texas joined the United States in 1845. Mexico had never accepted Texas independence, and the two countries disagreed about where Texas even ended. Within months, that argument became a war.</p>
  </div>

  <h3>The border dispute</h3>
  <div class="regions">
    <div class="card"><div class="ctop"><b>Mexico's claim</b><span class="tag">Nueces River</span></div><p>Texas had always ended at the Nueces River, which reaches the coast at Corpus Christi.</p></div>
    <div class="card"><div class="ctop"><b>Texas and U.S. claim</b><span class="tag">Rio Grande</span></div><p>The border was the Rio Grande, all the way to its source in the Rocky Mountains. That claim even took in Santa Fe.</p></div>
  </div>

  <h3>From war to today's border</h3>
  <div class="ruler">
    <div class="era"><span class="yr">1846</span><div><b>War begins</b><span>President Polk sent General Zachary Taylor's army to the Rio Grande. After a clash between U.S. and Mexican soldiers in the disputed land, Congress declared war. Early battles at Palo Alto and Resaca de la Palma were fought near today's Brownsville.</span></div></div>
    <div class="era"><span class="yr">1847</span><div><b>U.S. captures Mexico City</b><span>Texas Rangers served as scouts. U.S. armies marched into central Mexico and took the capital.</span></div></div>
    <div class="era"><span class="yr">1848</span><div><b>Treaty of Guadalupe Hidalgo</b><span>Mexico accepted the Rio Grande as the Texas border and gave up a huge area, the Mexican Cession, which later became California, Nevada, Utah, and parts of four more states.</span></div></div>
    <div class="era"><span class="yr">1850</span><div><b>Compromise of 1850</b><span>Texas still claimed land as far as Santa Fe. In the Compromise of 1850, Texas gave up that claim in exchange for $10 million from the U.S., which it used to pay the old Republic's debts. This set the shape of Texas you know today.</span></div></div>
  </div>

  <div class="callout"><b>Map task.</b> Compare an 1845 map of Texas (a long strip reaching up into today's Colorado and Wyoming) with an 1850 map (today's shape, with the Panhandle). What land did Texas give up? Find period maps at the <a href="https://texashistory.unt.edu/" target="_blank" rel="noopener">Portal to Texas History</a>.</div>

  <h3>Who came, and where they settled</h3>
  <div class="prose"><p>Statehood brought safety and cheap land, and people poured in. Texas grew from about 212,000 people in 1850 to about 604,000 in 1860. Where each group settled depended on why they came and on the land itself.</p></div>
  <div class="regions">
    <div class="card"><div class="ctop"><b>Germans</b><span class="tag">Hill Country</span></div><p>Fled hard times and political turmoil in Germany. A society of nobles organized settlement at <b>New Braunfels</b> (1845) and <b>Fredericksburg</b> (1846). In 1847 John O. Meusebach made a peace treaty with the Comanche that was kept.</p></div>
    <div class="card"><div class="ctop"><b>Czechs</b><span class="tag">Central Texas</span></div><p>Came for farmland starting in the 1850s and settled the rolling prairies of Fayette, Austin, and Lavaca counties. Many farmed cotton and corn.</p></div>
    <div class="card"><div class="ctop"><b>Mexican Texans</b><span class="tag">South Texas</span></div><p>Already lived there. Tejano families ranched the brush country between the Nueces and the Rio Grande and in San Antonio. Many lost land to newcomers through lawsuits and pressure after the war.</p></div>
    <div class="card"><div class="ctop"><b>Enslaved African Americans</b><span class="tag">East Texas</span></div><p>Did not choose to come. Enslavers forced them to Texas to grow cotton on the rich soils and river bottoms of East Texas and the Brazos and Colorado valleys. By 1860, about 182,000 people, nearly a third of all Texans, were enslaved.</p></div>
  </div>

  <div class="callout"><b>Geography decides.</b> Cotton needs rain, warm weather, and rich soil, so plantations clustered in the wetter east. Ranching works on dry grassland and brush, so it spread south and west. Rivers carried crops to the coast. When you explain where a group lived, look for both the <b>push</b> that made them leave home and the <b>pull</b> of the land in Texas.</div>''',
  practice=[
    {"type": "order", "title": "From dispute to border", "intro": "Drag the cards, or use the arrows, to put these events in order, earliest at the top.", "button": "Check my order", "word": "in the right spot", "seed": 7,
     "items": [["Texas becomes a state", "1845"], ["Taylor's army moves to the Rio Grande; war begins", "1846"], ["The U.S. captures Mexico City", "1847"], ["Treaty of Guadalupe Hidalgo sets the Rio Grande border", "1848"], ["Compromise of 1850 trades land claims for $10 million", "1850"]]},
    {"type": "match", "title": "Why here?", "intro": "Match each group to where most of its members lived in the 1850s.", "placeholder": "Choose a region…", "button": "Check my map", "word": "correct",
     "options": ["Hill Country (New Braunfels, Fredericksburg)", "Central Texas prairies (Fayette County)", "South Texas brush country and San Antonio", "East Texas and river bottoms"],
     "items": [["German immigrants", 0], ["Czech immigrants", 1], ["Tejano ranching families", 2], ["Enslaved African Americans on cotton plantations", 3]]},
    {"type": "sort", "title": "Push or pull?", "intro": "Is this a <b>push</b> (a reason to leave home) or a <b>pull</b> (a reason to come to Texas)?", "button": "Check my sorting", "word": "sorted correctly",
     "choices": [["P", "Push"], ["L", "Pull"]],
     "items": [["Crop failures and hard times in Germany", "P", "Problems at home pushed people to leave."], ["Cheap, fertile land in Texas", "L", "Land drew people to Texas."], ["Political turmoil in Europe after 1848", "P", "Some fled after failed revolutions."], ["Statehood brought U.S. protection", "L", "A safer Texas attracted settlers."], ["Rich soil for growing cotton", "L", "This drew enslavers, who forced enslaved people to come."], ["Crowded farmland back East with little left to buy", "P", "Many U.S. families moved west for land."]]},
    {"type": "mc", "title": "Read the map", "intro": "Pick the best answer.", "button": "Check my answers", "word": "correct",
     "items": [
       {"q": "Compared with 1845, the 1850 map of Texas shows…", "o": ["Texas got bigger", "Texas gave up land to the north and west, near Santa Fe", "Texas lost the coast"], "a": 1, "e": "The Compromise of 1850 traded those claims for $10 million."},
       {"q": "Why did plantations cluster in East Texas?", "o": ["More rain and rich soil for cotton", "It was closest to Mexico", "It was the driest region"], "a": 0, "e": "Geography shaped where cotton could grow."},
       {"q": "How did the U.S.–Mexican War change Texas's border?", "o": ["It made the Nueces the border", "Mexico accepted the Rio Grande as the border", "Texas lost San Antonio"], "a": 1, "e": "The Treaty of Guadalupe Hidalgo settled the Rio Grande line."}]}
  ],
  quiz=[
    {"q": "What started the U.S.–Mexican War?", "o": ["A dispute over the Texas border after annexation", "A fight over oil", "The Civil War", "Spain's return"], "a": 0, "e": "Mexico said the Nueces; the U.S. said the Rio Grande."},
    {"q": "Which river did Mexico say was the Texas border?", "o": ["Rio Grande", "Nueces", "Red", "Sabine"], "a": 1, "e": "The Nueces reaches the coast at Corpus Christi."},
    {"q": "What did the Treaty of Guadalupe Hidalgo (1848) do?", "o": ["Gave Texas back to Mexico", "Set the Rio Grande as the border and gave the U.S. the Mexican Cession", "Ended the Civil War", "Created the Republic of Texas"], "a": 1, "e": "It ended the war."},
    {"q": "In the Compromise of 1850, Texas…", "o": ["Gained New Mexico", "Gave up its claim to land near Santa Fe for $10 million", "Left the Union", "Abolished slavery"], "a": 1, "e": "The money paid the old Republic's debts."},
    {"q": "Where did many German immigrants settle?", "o": ["The Panhandle", "The Hill Country, in towns like New Braunfels and Fredericksburg", "Galveston Island only", "El Paso"], "a": 1, "e": "Their towns still show German influence."},
    {"q": "John O. Meusebach is known for…", "o": ["A peace treaty with the Comanche in 1847", "Starting the Mexican War", "Founding Victoria", "Writing the Compromise of 1850"], "a": 0, "e": "It was one of the few treaties both sides kept."},
    {"q": "About what share of Texans were enslaved in 1860?", "o": ["Almost none", "Nearly one-third", "Half", "Three-quarters"], "a": 1, "e": "About 182,000 of 604,000 people."},
    {"q": "Why did Czech immigrants settle in Central Texas?", "o": ["For gold", "For good farmland on the prairies", "To fight in the war", "To work in factories"], "a": 1, "e": "Fayette County became a Czech center."},
    {"q": "Which physical feature most shaped where cotton plantations were?", "o": ["Mountains", "Rich soil, rainfall, and rivers in East Texas", "Deserts", "Canyons"], "a": 1, "e": "Cotton needs rain and good soil."},
    {"q": "Which sentence best answers the big question?", "o": ["Statehood changed nothing", "The war and the Compromise of 1850 set Texas's border, and safety and cheap land brought Germans, Czechs, and others, while enslaved people were forced in", "Texas lost most of its people", "Only Mexicans moved to Texas"], "a": 1, "e": "Borders were fixed, and the population nearly tripled from 1850 to 1860."}
  ],
  prompt="In 3 to 5 sentences, answer: <b>How did statehood change Texas's borders and population?</b> Make a claim, give one piece of evidence (a treaty, a date, a group, or a number), and explain a <b>“why here?”</b> reason using geography.",
  placeholder="Statehood changed Texas by...",
  ck3="I explained <b>why</b> a group settled where it did, using geography.",
  review="Review the border timeline and the settlement cards",
  sources='<a href="https://www.tshaonline.org/handbook" target="_blank" rel="noopener">Handbook of Texas Online</a>: “Mexican War,” “Treaty of Guadalupe Hidalgo,” “Compromise of 1850,” “German Immigration,” “Czechs,” “Slavery” · <a href="https://texashistory.unt.edu/" target="_blank" rel="noopener">The Portal to Texas History</a> (period maps)',
)
