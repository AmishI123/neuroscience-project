# Final drafts (story: a brain's state shapes what it takes in)

Written from her own submitted answers plus the choices made with her family: Pragnya opening, anesthesia from curiosity, mouse study credited as 'most of the work, with advice and guidance from my father', EEG study left out, one sentence on the Next Step app. Each story appears in only one essay. Plain text, ready to paste. She should read each one and change anything that doesn't sound like her.

## 1 Why ASDRP (limit 375), 372 words

At Pragnya, where I volunteer with neurodivergent children, I once watched one child dance while another covered their ears because the room was too loud. It was the same room and the same noise, but the two kids reacted in completely opposite ways. I still think about that day. So the difference had to be inside each child, in how their brain was taking it all in.

That idea, that a brain's state changes what it takes in, is what got me into neuroscience. So far I have explored it through code, because I like working things out from real data. In my main project, I used public recordings of thousands of neurons in mouse visual cortex to see whether a mouse's pupil size and running could help predict what its neurons were doing, beyond the image it was looking at. They did, in all three mice I analyzed. Then I shuffled the behavior data to see if the result would fall apart, and the improvement went away. Honestly, that check convinced me more than the result did.

Still, predicting activity only tells me so much. I want to understand what is actually changing inside the neurons, and that is part of why I plan to become a Certified Registered Nurse Anesthetist. Anesthesia turns consciousness off and back on on purpose, and I am curious what happens to neurons and the signals between them when it does, and how drugs and diseases change those signals.

I am applying to ASDRP because I have taken my independent work about as far as I can on my own. I want a mentor who can teach me to analyze data more carefully, push back on my own results, and explain what I find. I also want real lab experience, since a lot of what I am curious about cannot be figured out from a laptop. I also want to work with students who get me into things I would never find by myself.

In the long run, I want to keep combining neuroscience and healthcare through college and beyond, so that understanding the brain at the cellular level helps me make better decisions for patients one day. ASDRP feels like the right place to start.

## 2 Coursework and grades (limit 400), 300 words

In ninth grade I took Biology and Precalculus, which were the hardest science and math classes I could take.

Biology is where my interest in neuroscience and medicine started. Learning about genetics, cells, and how the body regulates itself made me want to know what happens at that same level in the brain. I got an A, and that class is a big part of why I got into research.

Precalculus was harder for me. I finished with a high B, and it was the grade I worked hardest for. The class moved fast, there was no extra credit or test corrections, and I realized pretty early that just showing up to lectures was not going to be enough. I did extra problems, went back through my notes, and kept working on the topics that gave me trouble until I could actually use them. By the end, I understood the material better than I would have if it had come easily.

This year I am taking Honors Chemistry and AP Calculus AB. Chemistry is behind a lot of what I care about, from how neurons send signals to how medications act on the body. Calculus builds right on Precalculus, and it is the math I will need for research.

Outside of school, I taught myself Python and libraries like numpy and scikit-learn so I could work with real datasets for my research projects. I learned it the same way I got through Precalculus, by working problems until they made sense.

My classes gave me a foundation in math and biology, but the more useful thing they taught me is what to do when I get stuck and how to figure something out without waiting for someone to explain it again. Those are the habits I want to bring to ASDRP.

## 3 Other STEM experience (limit 375), 366 words

The two things that have shaped me most outside of school both involve helping someone learn in their own way.

I volunteer with Pragnya, which supports neurodivergent children. I run games and activities and change how I work with each child depending on what they need. One girl I was paired with still remembers my name on days I am not working with her. She comes up to say hi and starts talking about things we both like. Seeing how differently each kid reacts to the same activity was my first real look at how the brain shapes behavior, and it is a big reason I want to study neuroscience.

I also tutored math with Learn To Be, a free online tutoring nonprofit. One student could do the arithmetic on IXL but froze on any problem longer than a sentence. We spent our sessions breaking problems into pieces and underlining what each part was asking before touching the numbers. Once she realized it was mostly about translating the words, her scores went up. Tutoring taught me to slow down, figure out where someone is actually confused, and keep trying different explanations until one works. I also understand math differently now that I have taught it.

I am especially interested in Alzheimer's, because of stories I have read and a film about families living with it. What stuck with me was not just what the disease does to the person, but how much their family goes through too.

For a month I volunteered at a hospice, doing administrative work. Working in the office, I saw how many different terminal illnesses brought people there, and how much of their care was about keeping them comfortable and out of pain. That experience is part of why I am drawn to anesthesia and to how drugs affect the nervous system.

I also built a small app called Next Step, using AI coding tools, with advice and guidance from my father. It asks students how much energy they have, and on a low day it only shows them the next step. Working on it reminded me of Pragnya, where the kids usually know better than I do what will help them.

## 4 Diversity (limit 200), 171 words

Volunteering at Pragnya, a program that supports neurodivergent children, has shown me how differently each kid moves through the same room. Some of the kids I work with speak in single words. Others are non-verbal and communicate in other ways. Each of them has their own ideas about what to play and how to play it, and most of those ideas are more creative than mine.

That is what diversity means to me. It is something I see in person, in how people take in the world around them. Being around it has made me a better listener. The game I plan is often not the game we end up playing, and the child usually knows better than I do what will work.

I want to be part of a research group that works the same way, where people bring their own way of thinking and are not expected to change it to fit in. The person who does something differently is often the one who notices what everyone else missed.

## 5 Hands-on research (limit 375), 374 words

I have not been part of a formal lab program yet, but I have done computational research using public biological datasets. Each project taught me something different about when to trust a result.

My main project used public recordings from thousands of neurons in mouse visual cortex. I did most of the work myself, with advice and guidance from my father, who has a software background. I wanted to know whether a mouse's behavior, meaning its pupil size and running, could help predict its brain activity better than the image it was looking at. Adding behavior raised my model's accuracy on held-out data from 0.126 to 0.158 in the first mouse, and the result held up in two more mice (0.154 to 0.203, and 0.143 to 0.191). Pupil size helped in all three. Running barely helped in the mouse that hardly ran, but it did help in the two that ran more. After that, I tried to break the result. When I shuffled the behavior data, the improvement disappeared, and it stayed positive when I left out any one mouse. This project taught me to test my own results before believing them. It also showed me its limits, since it shows prediction and not cause, and three mice are not enough to generalize.

Another project used a brain imaging dataset. I built logistic regression and random forest models to tell healthy scans apart from Alzheimer's scans. The random forest did much better, which told me the patterns were more complicated than a simple straight-line boundary could capture.

I also looked at a sleep health dataset to see whether common claims about stress and steps held up. I trained a linear regression and a decision tree to predict sleep duration. Stress and age both related to sleep, but age was also related to stress, so I read about confounding variables before trusting either one.

These projects pulled me toward molecular neuroscience, because what I want to understand, like how memory breaks down in Alzheimer's or what changes in neurons when a brain's state shifts, takes experimental biology at the cellular level. At ASDRP I want lab experience and mentorship to build on the computational skills I have. My code, results and apps are at amishi123.github.io/neuroscience-project.

## Advisor / field preference (limit 150), 121 words

I'm interested in molecular neuroscience because I want to work in healthcare, helping understand and treat the brain and nervous system. I plan to become a Certified Registered Nurse Anesthetist, and that takes a strong understanding of neuroscience, pharmacology, and how the body works.

I'm especially curious about how neurons communicate, how a brain's state changes what neurons do, and how medications affect the nervous system. Anesthesia interests me because it changes brain activity on purpose so that pain and consciousness can be managed safely.

Building a small app for students also got me interested in human-centered design. I would love to work on a project with Mrs. Sahar Jahanikia and see how lab research shapes the way patients are treated.
