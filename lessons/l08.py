L = dict(
  slug="lesson08", key="tx-lesson8-v1", n=8, label="Lesson 8", short="Republic of Texas",
  title="The Republic of Texas",
  question="Why did the Republic of Texas last only nine years?",
  teks=["1B", "4A", "4B", "17A"],
  read='''  <h2>A new country with big problems</h2>
  <div class="prose">
    <p>Lesson 7 ended with victory at San Jacinto. Texas was now an independent nation, the <b>Republic of Texas</b>. It had a constitution, a president, an army, and even a navy. It also had almost no money, a long border with a Mexico that refused to accept the loss, and strong American Indian nations whose lands settlers kept moving onto.</p>
    <p>Most Texans voted in 1836 to join the United States. The U.S. said no, at least for now. So Texas tried to make it on its own.</p>
  </div>

  <h3>Three presidents, three approaches</h3>
  <div class="cmpbox"><table class="cmp">
    <thead><tr><th></th><th>Sam Houston</th><th>Mirabeau B. Lamar</th><th>Anson Jones</th></tr></thead>
    <tbody>
      <tr><th>Years</th><td>1836–38 and 1841–44</td><td>1838–41</td><td>1844–46</td></tr>
      <tr><th>Money</th><td>Cut spending hard</td><td>Spent heavily and printed paper money that lost its value; debt soared</td><td>Kept costs low</td></tr>
      <tr><th>American Indians</th><td>Sought peace treaties and trade</td><td>Waged war: drove the Cherokee out in 1839 and fought the Comanche in 1840</td><td>Continued Houston's peace policy</td></tr>
      <tr><th>Big goal</th><td>Join the United States</td><td>Build a large, independent Texas; sent the failed Santa Fe Expedition</td><td>Finished annexation</td></tr>
    </tbody>
  </table></div>

  <div class="callout"><b>Lamar's lasting gift.</b> Lamar's spending hurt the Republic, but he also set aside public land to pay for schools and a future university. That is why he is called the Father of Texas Education. He also moved the capital to a new town on the Colorado River named Austin.</div>

  <h3>Problems the Republic could not solve</h3>
  <div class="regions">
    <div class="card"><div class="ctop"><b>Debt</b><span class="tag">money</span></div><p>The government owed millions of dollars. Its paper money, called "redbacks," became nearly worthless.</p></div>
    <div class="card"><div class="ctop"><b>Defense</b><span class="tag">Mexico</span></div><p>Mexico never recognized Texas. In 1842 Mexican armies captured San Antonio twice. A Texian raid into Mexico ended at Mier, where captured men had to draw beans to see who would be shot.</p></div>
    <div class="card"><div class="ctop"><b>Conflict</b><span class="tag">frontier</span></div><p>War with the Cherokee and Comanche cost lives and money. Peace was cheaper, but settlers kept pushing onto Native lands.</p></div>
    <div class="card"><div class="ctop"><b>The Santa Fe Expedition</b><span class="tag">1841</span></div><p>Lamar sent traders and soldiers to claim Santa Fe. They got lost, ran short of food, and were captured by Mexican troops. <b>José Antonio Navarro</b> was among them and spent years in a Mexican prison.</p></div>
  </div>

  <h3>The road to annexation</h3>
  <div class="ruler">
    <div class="era"><span class="yr">1837</span><div><b>U.S. recognizes Texas</b><span>But it refused annexation. Northern leaders opposed adding another slave state, and many feared war with Mexico.</span></div></div>
    <div class="era"><span class="yr">1839–40</span><div><b>Europe takes notice</b><span>France and Britain recognized Texas. Britain hoped Texas would stay independent, and maybe end slavery. Americans worried about Britain gaining influence next door.</span></div></div>
    <div class="era"><span class="yr">1844</span><div><b>Annexation becomes a campaign issue</b><span>A treaty failed in the U.S. Senate. Then James K. Polk won the presidency promising to add Texas.</span></div></div>
    <div class="era"><span class="yr">1845</span><div><b>Texas votes to join</b><span>Congress passed a joint resolution offering annexation. A Texas convention accepted it, and Texas became the 28th state on December 29, 1845. Navarro, home from prison, was the only Tejano delegate, and he fought to keep voting rights from being limited to white men only.</span></div></div>
  </div>

  <div class="dates">
    <div class="date"><span class="yr">1845</span><b>Annexation: Texas joins the United States</b><p>This is one of your eight required dates. Add it to your timeline.</p></div>
  </div>''',
  practice=[
    {"type": "sort", "title": "Houston or Lamar?", "intro": "Which president's policy was this?", "button": "Check my sorting", "word": "sorted correctly",
     "choices": [["H", "Houston"], ["L", "Lamar"]],
     "items": [["Made peace treaties with American Indian nations", "H", "Houston had lived among the Cherokee and preferred peace."], ["Drove the Cherokee out of East Texas", "L", "Lamar's Cherokee War was in 1839."], ["Sent the Santa Fe Expedition", "L", "It was meant to expand Texas trade and territory."], ["Cut government spending to reduce debt", "H", "Houston slashed costs in his second term."], ["Set aside land to pay for public schools", "L", "This is why Lamar is the Father of Texas Education."], ["Wanted Texas to join the United States", "H", "Lamar wanted an independent Texas."]]},
    {"type": "match", "title": "Problems and effects", "intro": "Match each problem to what it led to.", "placeholder": "Choose an effect…", "button": "Check my matches", "word": "correct",
     "options": ["Texans wanted the U.S. to take over the debt and protect them", "Northern leaders blocked annexation for years", "Americans feared Britain gaining a foothold", "Texas saw it needed a stronger protector"],
     "items": [["Paper money became worthless and debt grew", 0], ["Texas allowed slavery", 1], ["Britain showed interest in an independent Texas", 2], ["Mexican armies captured San Antonio in 1842", 3]]},
    {"type": "order", "title": "Republic timeline", "intro": "Use the arrows to put these in order, earliest at the top.", "button": "Check my order", "word": "in the right spot", "seed": 6,
     "items": [["Victory at San Jacinto", "1836"], ["The U.S. recognizes Texas but refuses annexation", "1837"], ["Lamar drives out the Cherokee", "1839"], ["The Santa Fe Expedition is captured", "1841"], ["Mexican armies capture San Antonio twice", "1842"], ["Texas becomes the 28th state", "1845"]]},
    {"type": "mc", "title": "Think it through", "intro": "Pick the best answer.", "button": "Check my answers", "word": "correct",
     "items": [
       {"q": "Why did many Texans want annexation?", "o": ["To escape debt and get U.S. protection from Mexico", "To become part of Britain", "To give up slavery"], "a": 0, "e": "Joining the U.S. solved the Republic's two biggest problems."},
       {"q": "Which is evidence that Lamar's policies made things worse?", "o": ["Debt soared and the Santa Fe Expedition failed", "He moved the capital to Austin", "He supported schools"], "a": 0, "e": "Expensive wars and failed plans deepened the money crisis."},
       {"q": "What did Navarro fight for at the Convention of 1845?", "o": ["Ending annexation", "Keeping voting from being limited to white men only, protecting Tejano rights", "Moving the capital"], "a": 1, "e": "He was the only Tejano delegate."}]}
  ],
  quiz=[
    {"q": "How long did the Republic of Texas last?", "o": ["Two years", "About nine years (1836–1845)", "Fifty years", "One year"], "a": 1, "e": "It became a state at the end of 1845."},
    {"q": "Who was the first elected president of the Republic of Texas?", "o": ["Stephen F. Austin", "Sam Houston", "Anson Jones", "Lorenzo de Zavala"], "a": 1, "e": "Houston served twice."},
    {"q": "Mirabeau B. Lamar is called the Father of Texas Education because he…", "o": ["Built the first college himself", "Set aside public land to pay for schools and a university", "Taught school", "Wrote the first textbook"], "a": 1, "e": "Land grants funded schools for generations."},
    {"q": "How did Lamar's policy toward American Indians differ from Houston's?", "o": ["Lamar sought peace; Houston waged war", "Lamar waged war; Houston sought peace", "They were the same", "Neither had a policy"], "a": 1, "e": "Lamar's wars were costly in lives and money."},
    {"q": "What happened to the Santa Fe Expedition?", "o": ["It captured Santa Fe", "Its members were captured by Mexican troops", "It found gold", "It founded Austin"], "a": 1, "e": "The failure embarrassed Texas and added to debt."},
    {"q": "Why did the U.S. refuse annexation at first?", "o": ["Texas was too small", "Northern opposition to adding a slave state and fear of war with Mexico", "Texas did not want to join", "Britain owned Texas"], "a": 1, "e": "Slavery made annexation a national fight."},
    {"q": "Which was NOT a major problem of the Republic?", "o": ["Debt", "Defense against Mexico", "Too much money in the treasury", "Conflict on the frontier"], "a": 2, "e": "The Republic was always short of money."},
    {"q": "What happened in 1845?", "o": ["Texas declared independence", "Texas joined the United States", "The Civil War began", "Mexico won independence"], "a": 1, "e": "1845 is a required date."},
    {"q": "Who was José Antonio Navarro?", "o": ["A Tejano patriot who signed the Declaration, was imprisoned after Santa Fe, and served at the 1845 convention", "A Mexican general", "The last president of the Republic", "A British diplomat"], "a": 0, "e": "He defended Tejano rights at every step."},
    {"q": "Which sentence best answers the big question?", "o": ["The Republic ended because Mexico conquered it", "Debt, weak defense, and costly frontier wars pushed Texans to join the U.S., which agreed in 1845 once Polk was elected", "Britain bought Texas", "The Republic lasted 100 years"], "a": 1, "e": "Texas could not solve its problems alone."}
  ],
  prompt="In 3 to 5 sentences, complete this claim and defend it: <b>Annexation was mostly about ___.</b> Give one piece of evidence from today's lesson and explain how it supports your claim.",
  placeholder="Annexation was mostly about...",
  reflect_h="Finish the claim",
  review="Review the presidents chart and the Republic's problems",
  sources='<a href="https://www.tshaonline.org/handbook" target="_blank" rel="noopener">Handbook of Texas Online</a>: “Republic of Texas,” “Lamar, Mirabeau Buonaparte,” “Navarro, José Antonio,” “Annexation,” “Texan Santa Fe Expedition”',
)
