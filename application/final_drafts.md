# Final drafts (story: a brain's state shapes what it takes in)

Written from her own submitted answers plus the choices made in this session: Pragnya opening A, anesthesia from curiosity, mouse study credited as 'most of the work, with advice and guidance from my father', EEG study left out; one sentence on the Next Step app (built with AI tools and her father's advice and guidance) added to Essay 3 and the advisor essay as a hint of HCI. Nothing new is claimed beyond her essays, the repo results and those choices. She should read each one and change anything that doesn't sound like her.

Essay 4 is unchanged from the tightened version. Plain text is ready to paste; the bold markers in Essay 5 can be removed.

## 1 Why ASDRP (limit 375), 363 words

At Pragnya, where I volunteer with neurodivergent children, I watched one child dancing while another covered their ears because the room was too loud. Same room, same noise, opposite reactions. I keep coming back to that moment. The input was identical, so the difference had to be in the child's state.

How a brain's state changes what it takes in is the center of my interest in neuroscience, and I explore it through code. Combining computer science with biology lets me work on problems too complicated to solve by hand, and I would rather ask my own questions of data than memorize what someone else has already found. For one project I used public recordings from mouse visual cortex to test whether a mouse's pupil size and running help predict what its neurons do, beyond the image it sees. They did, in all three mice. I also shuffled the behavior data to check the result was not an accident, and the gain disappeared. That check convinced me more than the result did.

Prediction only describes the brain from a distance. What I want to understand is what is actually changing. That is why I plan to become a Certified Registered Nurse Anesthetist. Anesthesia is the one situation where we switch consciousness off and on again on purpose, and I am curious what is changing in neurons and the signals between them, and how drugs and diseases change the way those signals travel.

I am applying to ASDRP because I have taken my independent work about as far as I can alone. I want mentors who can show me how to analyze data more carefully, question my own results, and explain what I find. I want wet-lab experience, because these questions cannot be answered from a laptop. I also want to be around students who push me into topics I would not have looked at on my own.

Longer term, I want to pair neuroscience with healthcare through college and beyond. Understanding anesthesia at the cellular level should help me make better decisions for patients. ASDRP is where I want to start building those habits, in the lab now and in the hospital someday.

## 2 Coursework and grades (limit 400), 258 words

In ninth grade I took Biology and Precalculus, the hardest science and math courses available to me.

Biology is where my interest in neuroscience and medicine began. Learning how genetics, cells, and the body's regulation work made me want to know what happens at that same level in the brain. I earned an A, and the class is a large part of why I am drawn to research.

Precalculus was harder, and I ended the year with a high B, the toughest grade I have worked for. The course moved fast, with no extra credit or test corrections, and I realized early that keeping up took more than attending lectures. I did extra problems, went back through my notes, and stayed with the topics that gave me trouble until I could use them. By the end I understood the material in a way I would not have if it had come easily.

This year I am taking Honors Chemistry and AP Calculus AB. Chemistry sits behind most of what I care about, from how neurons signal and how a brain's state shifts to how medications act on the body. Calculus builds directly on Precalculus and is the math I need for the quantitative questions I want to take on in research.

My classes have given me a foundation in math and biology. The more useful lesson has been what to do when I get stuck and how to learn something without waiting for someone to explain it again. Those are the habits I want to bring to ASDRP.

## 3 Other STEM experience (limit 375), 366 words

Outside the classroom, I look for activities that build both my scientific curiosity and my ability to help others.

I volunteer with Pragnya, which supports neurodivergent children. In one session a child was dancing while another covered their ears because the noise was too much. One girl I was paired with remembers my name on days I am not with her, comes over to say hi, and starts conversations about shared interests. Watching how differently each child engages with the same activity was my first close look at how the brain shapes behavior, and a big part of why I want to study neuroscience.

I also tutor math with Learn To Be. One student on IXL could handle the arithmetic but froze at any problem longer than a sentence. We spent sessions breaking problems into pieces and underlining what each part was asking before touching any numbers. Once she saw it was mostly translation, her scores climbed. Tutoring has taught me to slow down, listen for where someone is actually confused, and try explanations until one lands.

That interest carries into projects I do on my own. Using Python and public datasets, I explore sleep, neuronal activity, and Alzheimer's. For one project I built a classifier on a brain imaging dataset to tell healthy scans from scans at different stages of Alzheimer's. Getting the preprocessing right was harder than the modeling, and it showed me how much of research happens in the careful steps before any result. Alzheimer's interests me because of stories I have read and a film about families living with it. I noticed not only what the disease does to a person, but how much the people around them carry.

I have also built a small app, Next Step, with AI tools and advice and guidance from my father. It asks students how much energy they have and, on a low day, shows only the next step. Designing it taught me that a tool should ask instead of guess, which is what the children at Pragnya keep teaching me.

I want to bring these habits to ASDRP and do research seriously, alongside mentors who can push my thinking further than I can alone.

## 4 Diversity (limit 200), 168 words

Volunteering at Pragnya has shown me how differently each child engages with the same room. In one session, one child was dancing while another covered their ears because the noise was too much. Some of the kids I work with speak in single words. Others are non-verbal and communicate in other ways. Each has their own ideas about what to play and how, and most are more creative than mine.

That is what diversity looks like to me: real, in front of me, in how people move through a room. It has made me a better listener. The game I planned is often not the game we end up playing, and the child usually knows better than I do what will work.

I want to be part of a research group that works the same way, where people arrive with their own approach and are not asked to smooth it out. The person doing something differently is often the one seeing what the rest of us are missing.

## 5 Hands-on research (limit 375), 346 words

I have not been part of a formal lab program yet, but I have done computational research on public biological datasets. Each project taught me something different about how to trust a result.

**1. Mouse visual cortex.** I did most of this project myself, with advice and guidance from my father, who has a software background. Using public recordings from thousands of neurons in mouse visual cortex, I asked whether a mouse's behavior, meaning pupil size and running, improves predictions of its neural activity beyond the image it saw. Adding behavior raised held-out prediction accuracy from 0.126 to 0.158 in the first mouse, and the result held in two more mice (0.154 to 0.203, and 0.143 to 0.191). Pupil-linked arousal helped all three, while running helped by very different amounts. I then tried to break the result. Shuffling behavior across trials erased the gain, and dropping any one mouse left it positive. That taught me a convincing result needs tests built to make it fail. It shows prediction, not cause, and three mice are not a population.

**2. Alzheimer's brain imaging.** Using a public imaging dataset, I built logistic regression and random forest classifiers to separate healthy scans from Alzheimer's scans. The random forest did much better, which told me a simple linear boundary was missing real structure. Preprocessing took more effort than the modeling.

**3. Sleep health data.** I wanted to know whether common claims about stress or steps held up in real data, starting from my own sleep habits. I ran correlations and trained a linear regression and a decision tree to predict sleep duration. Stress and age both correlated with sleep, but age also correlated with stress, so I read about confounding variables before trusting either.

These projects drew me toward molecular neuroscience, because the questions I care about, like how memory breaks down in Alzheimer's or what changes in neurons when a brain's state shifts, need experimental biology at the cellular level. Through ASDRP I want lab experience and mentorship, and to pair wet-lab work with the computational skills I have built.

## Advisor / field preference (limit 150), 123 words

I'm interested in molecular neuroscience because I want to work in healthcare, understanding and treating the brain and nervous system. I'm considering becoming a Certified Registered Nurse Anesthetist or a psychiatrist, and both require a solid grounding in neuroscience, pharmacology, and how the body works.

I'm especially curious about how neurons communicate, how brain state changes what neurons do, and how medications interact with the nervous system. Anesthesia fascinates me because it changes neural activity on purpose, so that pain and consciousness can be managed safely.

I'm also drawn to human-centered design, from a small app I built for students. I would love to work on a project with Mrs. Sahar Jahanikia, to see how lab research shapes the way patients are treated.
