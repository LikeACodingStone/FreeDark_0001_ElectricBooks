# Podcast vocabulary notes
Source file: Lex Fridman - Vladimir Vapnik： Predicates, Invariants, and the Essence of Intelligence ｜ Lex Fridman Podcast #71.opus
Improved subtitle: punctuation and vocabulary regenerated from current config.

**[0.00s] English:** The following is a conversation with Vladimir Vapnik, part two—the second time we spoke on the podcast.  
**Translation:** 

**[7.08s] English:** He is the co-inventor of Support Vector Machines, Support Vector Clustering, VC Theory, and many foundational ideas in statistical learning.  
**Translation:** Vocabulary: clustering: 聚类; foundational: 基础的

**[14.82s] English:** He was born in the Soviet Union, worked at the Institute of Controlled Sciences in Moscow, then in the U.S., at AT&T, NEC Labs, Facebook AI Research, and now is a professor at Columbia University.  
**Translation:** 

**[28.52s] English:** His work has been cited over 200,000 times. The first time we spoke on the podcast was just over a year ago—on one of the early episodes.  
**Translation:** Vocabulary: cited: 被引用; columbia: 哥伦比亚大学; moscow: 莫斯科

**[38.76s] English:** This time, we spoke after a lecture he gave titled "Complete Statistical Theory of Learning" as part of the MIT series of lectures on deep learning and AI that I organized.  
**Translation:** 

**[49.82s] English:** I'll release the video of the lecture in the next few days.  
**Translation:** 

**[53.74s] English:** This podcast and lecture are independent of each other, so you don't need one to understand the other.  
**Translation:** 

**[58.94s] English:** The lecture is quite technical and math-heavy, so if you do watch both, I recommend listening to this podcast first, since it is probably a bit more accessible.  
**Translation:** 

**[70.88s] English:** This is the Artificial Intelligence Podcast.  
**Translation:** 

**[73.94s] English:** If you enjoy it, subscribe on YouTube, give it five stars on Apple Podcasts, support it on Patreon, or simply connect with me on Twitter at @LexFriedman (spelled F-R-I-D-M-A-N).  
**Translation:** Vocabulary: patreon: Patreon 赞助; subscribe: 订阅

**[84.44s] English:** As usual, I'll do one or two minutes of ads now, and never any later.  
**Translation:** 

**[88.52s] English:** If there are any ads in the middle that can break the flow of the conversation, I hope that works for you and doesn't hurt the listening experience.  
**Translation:** 

**[95.94s] English:** This show is presented by Cash App, the number-one finance app in the App Store.  
**Translation:** 

**[100.46s] English:** When you get it, use code LEXPODCAST.  
**Translation:** 

**[103.80s] English:** Cash App lets you send money to friends, buy Bitcoin, and invest in the stock market with as little as $1.  
**Translation:** 

**[109.80s] English:** Brokerage services are provided by Cash App Investing, a subsidiary of Square, and member SIPC.  
**Translation:** Vocabulary: brokerage: 证券经纪; subsidiary: 子公司

**[116.24s] English:** Since Cash App allows you to send and receive money to friends, you can send money to friends, and invest in the stock market with as little as $1.  
**Translation:** 

**[118.52s] English:** You can send money digitally, peer-to-peer.  
**Translation:** Vocabulary: digitally: 以数字方式

**[120.00s] English:** And security in all digital transactions is very important. Let me mention the PCI.  
**Translation:** 

**[125.28s] English:** Data security standard, PCI DSS Level 1, that Cash App is compliant with. I'm a big fan of.  
**Translation:** Vocabulary: compliant: 符合要求

**[133.00s] English:** Standards for safety and security, and PCI DSS is a good example of that, where a bunch of  
**Translation:** 

**[139.48s] English:** Competitors got together and agreed that there needs to be a global standard around security.  
**Translation:** 

**[144.22s] English:** Of transactions. Now, we just need to do the same for autonomous vehicles and AI systems in general.  
**Translation:** 

**[151.34s] English:** So, again, if you get Cash App from the App Store or Google Play and use the code LEXPODCAST,  
**Translation:** Vocabulary: autonomous: 自主的

**[156.86s] English:** You get $10, and Cash App will also donate $10 to FIRST, one of my favorite organizations.  
**Translation:** 

**[162.64s] English:** That is helping to advance robotics and STEM education for young people around the world.  
**Translation:** Vocabulary: donate: 捐赠; robotics: 机器人技术

**[169.22s] English:** And now, here's my conversation with Vladimir Vapnik.  
**Translation:** 

**[174.22s] English:** You and I talked about Alan Turing yesterday a little bit, and that he, as the father of  
**Translation:** Vocabulary: turing: 图灵; vladimir: 弗拉基米尔

**[181.34s] English:** Artificial intelligence may have instilled in our field an ethic of engineering and not science.  
**Translation:** 

**[187.04s] English:** Seeking more to build intelligence rather than to understand it. What do you think?  
**Translation:** Vocabulary: instilled: 灌输

**[192.70s] English:** The difference between these two paths of engineering and intelligence, and the science.  
**Translation:** 

**[199.38s] English:** Of intelligence? It's a completely different story. Engineering,  
**Translation:** 

**[204.22s] English:** Vapnik is an imitation of human activity. You have to make a device that behaves as humans do.  
**Translation:** 

**[214.54s] English:** Has all the functions of humans. It doesn't matter how you do it. But to understand what  
**Translation:** Vocabulary: behaves: 模仿; imitation: 模拟

**[223.62s] English:** Is intelligence about a quite different problem. So, I think and believe that it's somehow related to.  
**Translation:** 

**[234.22s] English:** We talked yesterday about because  
**Translation:** 

**[240.00s] English:** Look at the Vladimir Probst idea.  
**Translation:** 

**[245.64s] English:** He just found 31 predicates.  
**Translation:** Vocabulary: predicates: 断言

**[252.88s] English:** He called it "units," which can explain humor behavior.  
**Translation:** 

**[259.10s] English:** At least, in Russian tales.  
**Translation:** 

**[260.90s] English:** He looked at Russian tales and derived from that.  
**Translation:** 

**[264.96s] English:** And then people realized that it's much wider than in Russian tales.  
**Translation:** 

**[269.02s] English:** It is in TV, in movies, and so on and so on.  
**Translation:** 

**[273.90s] English:** So, you're talking about Vladimir Probst.  
**Translation:** 

**[277.72s] English:** Who in 1928 published a book titled "Morphology of the Folktale,"?  
**Translation:** 

**[282.10s] English:** Describing 31 predicates that have this kind of sequential structure.  
**Translation:** Vocabulary: folktale: 民间故事; morphology: 结构; sequential: 顺序的

**[289.28s] English:** That a lot of the stories and narratives follow in Russian folklore and other contexts.  
**Translation:** 

**[294.68s] English:** We'll talk about it.  
**Translation:** Vocabulary: folklore: 民间传说; narratives: 叙述

**[296.04s] English:** I'd like to talk about predicates in a focused way.  
**Translation:** 

**[299.22s] English:** But let me, if you'll allow me, to stay zoomed out on our friend Alan Turing.  
**Translation:** Vocabulary: turing: 图灵; zoomed: 放大

**[304.68s] English:** And, you know, he inspired a generation with the Imitation Game.  
**Translation:** 

**[310.36s] English:** Yes.  
**Translation:** Vocabulary: imitation: 模仿

**[311.56s] English:** Do you think if we could linger on that a little bit longer?  
**Translation:** 

**[315.16s] English:** Do you think we can learn,  
**Translation:** Vocabulary: linger: 停留

**[318.44s] English:** Do you think learning to imitate intelligence can get us closer to understanding intelligence?  
**Translation:** 

**[324.68s] English:** So, why do you think imitation is so...?  
**Translation:** Vocabulary: imitate: 模仿

**[329.02s] English:** So, far from understanding?  
**Translation:** 

**[332.60s] English:** I think that it is different.  
**Translation:** 

**[334.54s] English:** Between you, you have different goals.  
**Translation:** 

**[337.54s] English:** So, your goal is to create something useful.  
**Translation:** 

**[343.60s] English:** Yeah.  
**Translation:** 

**[344.00s] English:** And that is great.  
**Translation:** 

**[345.66s] English:** And you can see how much has been done.  
**Translation:** 

**[349.76s] English:** And I believe that it will be done even more.  
**Translation:** 

**[353.14s] English:** It's self-driving cars, and also this business.  
**Translation:** 

**[356.50s] English:** It is great.  
**Translation:** 

**[358.34s] English:** And it was....  
**Translation:** 

**[359.02s] English:** Spark Bay.  
**Translation:** 

**[359.70s] English:** Spark Bay.  
**Translation:** 

**[360.00s] English:** Curing vision, but understanding is very difficult. It is, more or less, a philosophical category.  
**Translation:** Vocabulary: curing: 治疗; philosophical: 哲学的

**[368.52s] English:** What does it mean to understand the world? I believe in the scheme which starts from Plato, that  
**Translation:** 

**[375.98s] English:** There exists a world of ideas. I believe that intelligence is a world of ideas, but it is  
**Translation:** 

**[383.50s] English:** A world of pure ideas. When you combine them with reality, it creates something, as in my  
**Translation:** 

**[394.72s] English:** Case invariance, which is very specific, I believe, is the result of combining these ideas in a unique way.  
**Translation:** Vocabulary: invariance: 不变性

**[406.52s] English:** To construct an invariant, you need intelligence. But first of all, the predicate. If you want to  
**Translation:** 

**[413.48s] English:** Know the predicate, and hopefully there won't be too much predicate. For example, 31 predicates.  
**Translation:** Vocabulary: invariant: 不变量; predicate: 谓词; predicates: 谓词

**[423.12s] English:** For human behavior, it isn't a lot.  
**Translation:** 

**[425.88s] English:** Vladimir Propp used 31, you can even call them predicates, to describe.  
**Translation:** 

**[434.88s] English:** Stories, narratives. So, you think human behavior is influenced by them to what extent? How much of our behavior can be attributed to stories and narratives?  
**Translation:** 

**[442.54s] English:** World, our universe,...  
**Translation:** Vocabulary: attributed: 归因; narratives: 叙述

**[443.48s] English:** All the things that matter in our existence can be summarized in predicates of the kind:  
**Translation:** 

**[450.76s] English:** That Propp was working with.  
**Translation:** Vocabulary: summarized: 概括

**[452.16s] English:** I think that we have a lot of formal behavior. But I think that's much.  
**Translation:** 

**[459.76s] English:** Less, because even in this example, which I gave you yesterday, you saw that predicate.  
**Translation:** 

**[469.50s] English:** Can be...  
**Translation:** 

**[470.50s] English:** One predicate can be a predicate.  
**Translation:** 

**[472.00s] English:** Okay.  
**Translation:** 

**[473.00s] English:** One predicate can construct many different invariants, depending on your data. They're  
**Translation:** Vocabulary: invariants: 不变量

**[480.00s] English:** To different data, and they give different invariants. But pure ideas, maybe not so much.  
**Translation:** 

**[488.56s] English:** Not so many.  
**Translation:** 

**[489.20s] English:** I don't know about that. But, my guess—hopeful as it is—that's why the challenge is about.  
**Translation:** 

**[495.92s] English:** Digital recognition: How much do you need?  
**Translation:** 

**[498.48s] English:** I think we'll talk about computer vision and 2D images a little bit in your challenge.  
**Translation:** 

**[504.32s] English:** That's exactly what intelligence is about.  
**Translation:** 

**[506.48s] English:** That's exactly about, no, that hopes to be exactly about the spirit of intelligence.  
**Translation:** 

**[515.28s] English:** In the simplest possible way.  
**Translation:** 

**[517.04s] English:** Yeah, absolutely. You should start the simplest way. Otherwise,  
**Translation:** 

**[520.80s] English:** You will not be able to do it.  
**Translation:** 

**[522.24s] English:** Well, there's an open question as to whether starting at the MNIST digit recognition  
**Translation:** 

**[528.40s] English:** Is a step towards intelligence, or is it an entirely different thing?  
**Translation:** Vocabulary: digit: 阿拉伯数字

**[531.68s] English:** I think that to beat records, using  
**Translation:** 

**[536.48s] English:** 300, 200 times fewer examples, you need intelligence.  
**Translation:** 

**[540.56s] English:** You need intelligence. Because you use this term, and it will be nice.  
**Translation:** 

**[545.28s] English:** I'd like to ask some simple — maybe even dumb — questions. Let's start with a predicate.  
**Translation:** Vocabulary: predicate: 谓词

**[552.72s] English:** In terms of how you think about it, what is a predicate?  
**Translation:** 

**[557.36s] English:** I don't know. I have a feeling, formally, they exist. But I believe that predicate.  
**Translation:** 

**[566.48s] English:** For 2D images, one of them is symmetry.  
**Translation:** 

**[571.52s] English:** Hold on a second. Sorry. Sorry to interrupt and pull you back.  
**Translation:** Vocabulary: interrupt: 打断; symmetry: 对称

**[576.32s] English:** At the simplest level, we're not being profound currently.  
**Translation:** 

**[580.56s] English:** A predicate is a statement of something that is true.  
**Translation:** Vocabulary: profound: 深奥的

**[583.68s] English:** Yes.  
**Translation:** 

**[585.04s] English:** Do you think of predicates as somehow probabilistic in nature, or is this binary?  
**Translation:** Vocabulary: binary: 二元的; predicates: 谓词; probabilistic: 概率性的

**[594.56s] English:** This is truly a constraint?  
**Translation:** 

**[596.00s] English:** Yes.  
**Translation:** Vocabulary: constraint: 限制

**[596.40s] English:** Of logical statements about the world.  
**Translation:** 

**[600.00s] English:** In my definition, the simplest predicate is a function.  
**Translation:** 

**[603.92s] English:** Function, and you can use this function to make an inner product.  
**Translation:** 

**[609.38s] English:** That is a predicate.  
**Translation:** 

**[610.56s] English:** What's the input, and what's the output of the function?  
**Translation:** 

**[613.96s] English:** Input is X, something which is input in reality.  
**Translation:** 

**[618.66s] English:** Say, if you consider digit recognition, it's in pixel space.  
**Translation:** 

**[623.74s] English:** Yes.  
**Translation:** Vocabulary: digit: 数字; pixel: 像素

**[624.12s] English:** Input:  
**Translation:** 

**[624.90s] English:** But it is the function, which is defined in pixel space.  
**Translation:** 

**[629.14s] English:** But it can be any function from pixel space.  
**Translation:** 

**[635.62s] English:** And you choose, and I believe that there are several functions.  
**Translation:** 

**[640.54s] English:** Which is important for understanding images.  
**Translation:** 

**[646.34s] English:** One of them is symmetry.  
**Translation:** 

**[648.28s] English:** It's not so simple a construction as I described with the derivative.  
**Translation:** 

**[653.26s] English:** With all this stuff.  
**Translation:** Vocabulary: derivative: 导数

**[655.52s] English:** But another one, I believe; I don't know how many.  
**Translation:** 

**[658.40s] English:** Is how well-structured is the picture.  
**Translation:** 

**[663.42s] English:** Structured?  
**Translation:** 

**[664.26s] English:** Yeah.  
**Translation:** 

**[664.70s] English:** What do you mean by structured?  
**Translation:** 

**[666.86s] English:** It is a formal definition.  
**Translation:** 

**[669.10s] English:** Say: Something heavy in the left corner.  
**Translation:** 

**[673.46s] English:** Not so heavy in the middle, and so on.  
**Translation:** 

**[676.98s] English:** You describe the general concept of what you assume.  
**Translation:** 

**[681.82s] English:** Concepts.  
**Translation:** 

**[682.50s] English:** Some kind of universal concepts.  
**Translation:** 

**[685.18s] English:** Yeah.  
**Translation:** 

**[685.46s] English:** But I don't know how to formulate it.  
**Translation:** 

**[688.40s] English:** I don't know how to summarize this.  
**Translation:** Vocabulary: summarize: 概括

**[690.18s] English:** Do you?  
**Translation:** 

**[690.54s] English:** So, this is the thing.  
**Translation:** 

**[691.56s] English:** There are a million ways we can talk about this.  
**Translation:** 

**[693.56s] English:** I'll keep bringing it up.  
**Translation:** 

**[694.60s] English:** But we humans have such concepts when we look at digits.  
**Translation:** 

**[701.50s] English:** But it's hard to put them, just like you're saying now.  
**Translation:** Vocabulary: digits: 阿拉伯数字

**[703.84s] English:** It's hard to put them into words.  
**Translation:** 

**[705.92s] English:** You know, that is an example.  
**Translation:** 

**[708.58s] English:** When critics in music try to describe music, they use predicates.  
**Translation:** 

**[716.86s] English:** And, not just.  
**Translation:** Vocabulary: predicates: 断定词

**[717.36s] English:** I don't know.  
**Translation:** 

**[717.58s] English:** I don't know.  
**Translation:** 

**[717.60s] English:** I don't know.  
**Translation:** 

**[717.68s] English:** I don't know.  
**Translation:** 

**[717.76s] English:** I don't know.  
**Translation:** 

**[717.82s] English:** I don't know.  
**Translation:** 

**[718.02s] English:** I don't know.  
**Translation:** 

**[718.04s] English:** I don't know.  
**Translation:** 

**[718.10s] English:** I don't know.  
**Translation:** 

**[718.20s] English:** I don't know.  
**Translation:** 

**[718.26s] English:** I don't know.  
**Translation:** 

**[718.32s] English:** I don't know.  
**Translation:** 

**[718.40s] English:** I don't know.  
**Translation:** 

**[718.60s] English:** Too many predicates.  
**Translation:** 

**[720.00s] English:** But in different combinations.  
**Translation:** 

**[722.82s] English:** But they have some special words for describing music.  
**Translation:** 

**[728.42s] English:** And the same should be for images.  
**Translation:** 

**[732.50s] English:** But maybe there are critics who understand.  
**Translation:** 

**[735.50s] English:** Essence of what this image is about.  
**Translation:** 

**[740.60s] English:** Do you think there exist critics?  
**Translation:** 

**[743.00s] English:** Who can summarize the essence of images, human beings?  
**Translation:** 

**[748.28s] English:** I hope so, yes.  
**Translation:** 

**[752.62s] English:** Explicitly state them on paper.  
**Translation:** 

**[756.64s] English:** The fundamental question I'm asking is:  
**Translation:** Vocabulary: explicitly: 明确地

**[760.86s] English:** Do you think there exists a small set of predicates?  
**Translation:** 

**[766.16s] English:** That will summarize images?  
**Translation:** 

**[767.98s] English:** It feels to our mind like it does.  
**Translation:** 

**[771.10s] English:** That the concept of what makes a two, a three, and a four,...  
**Translation:** 

**[775.48s] English:** No, no, no.  
**Translation:** 

**[776.54s] English:** It's not on this.  
**Translation:** 

**[778.28s] English:** It's not on this level.  
**Translation:** 

**[780.86s] English:** It should not describe two, three, or four.  
**Translation:** 

**[784.92s] English:** It describes some construction.  
**Translation:** 

**[786.88s] English:** Which allows you to create invariance.  
**Translation:** Vocabulary: invariance: 不变性

**[792.04s] English:** And invariance—sorry to stick on this, but let's clarify the terminology.  
**Translation:** 

**[796.18s] English:** Invariance is a property of your image.  
**Translation:** Vocabulary: clarify: 澄清; terminology: 术语

**[804.42s] English:** Say, I can say,  
**Translation:** 

**[807.24s] English:** Looking at my image,  
**Translation:** 

**[809.10s] English:** It is more or less symmetric.  
**Translation:** 

**[812.00s] English:** And I can give you a value of symmetry.  
**Translation:** Vocabulary: symmetric: 对称的; symmetry: 对称

**[814.98s] English:** Say, level of symmetry.  
**Translation:** 

**[817.18s] English:** Using this function, which I gave you yesterday.  
**Translation:** 

**[823.40s] English:** And you can describe  
**Translation:** 

**[825.06s] English:** That your image has these characteristics.  
**Translation:** Vocabulary: characteristics: 特征

**[831.26s] English:** Exactly, in the way that musical critics describe music.  
**Translation:** 

**[837.24s] English:** So, but this is...  
**Translation:** 

**[840.00s] English:** Invariance applied to specific data, to specific music, to something.  
**Translation:** 

**[847.68s] English:** I strongly believe in these Plato ideas: that there exists a world of predicates and a world  
**Translation:** Vocabulary: predicates: 谓词

**[855.52s] English:** Of reality, and predicate and reality are somehow connected, and you have to know that.  
**Translation:** 

**[862.12s] English:** Let's talk about Plato a little bit.  
**Translation:** Vocabulary: predicate: 谓语

**[864.12s] English:** So, you draw a line from Plato to Hegel to Wigner to today.  
**Translation:** 

**[869.12s] English:** Yes.  
**Translation:** Vocabulary: hegel: 黑格尔; wigner: 魏格纳

**[870.12s] English:** So, Plato has Forms, the Theory of Forms.  
**Translation:** 

**[875.74s] English:** There's a world of ideas and a world of things, as you're talking about, and there's a connection.  
**Translation:** 

**[880.54s] English:** And presumably, the world of ideas is very small, and the world of things is arbitrarily.  
**Translation:** 

**[887.44s] English:** Big.  
**Translation:** Vocabulary: arbitrarily: 随意; presumably: 推测

**[888.44s] English:** But they're all, what Plato calls them, is just a shadow.  
**Translation:** 

**[892.74s] English:** The real world is a shadow from the world of Forms.  
**Translation:** 

**[894.96s] English:** Yeah.  
**Translation:** 

**[895.96s] English:** Do you have a projection?  
**Translation:** Vocabulary: projection: 预测

**[896.96s] English:** Projection:  
**Translation:** 

**[897.96s] English:** Of a world of ideas?  
**Translation:** 

**[898.96s] English:** Yeah.  
**Translation:** 

**[899.12s] English:** Very poetic.  
**Translation:** Vocabulary: poetic: 富有诗意的

**[900.12s] English:** In reality, you can realize this projection using these invariants, because it is a projection.  
**Translation:** 

**[909.88s] English:** On specific examples, which create specific features of specific objects.  
**Translation:** Vocabulary: invariants: 不变量

**[918.36s] English:** So, the essence of intelligence is, while only being able to observe the world of things,  
**Translation:** 

**[924.84s] English:** Try to come up with a world of ideas.  
**Translation:** 

**[927.12s] English:** Exactly.  
**Translation:** 

**[928.12s] English:** Like in this music story.  
**Translation:** 

**[929.12s] English:** Intelligent musical critics know all this, and have a feeling for what it is.  
**Translation:** 

**[934.76s] English:** I feel like that's a contradiction, intelligent music critics.  
**Translation:** Vocabulary: contradiction: 矛盾

**[939.12s] English:** But I think music is to be enjoyed in all its forms.  
**Translation:** 

**[947.80s] English:** The notion of a critic, like a food critic.  
**Translation:** 

**[949.88s] English:** No, I don't want to touch emotion.  
**Translation:** 

**[952.12s] English:** That's an interesting question.  
**Translation:** 

**[953.88s] English:** Does emotion ...  
**Translation:** 

**[954.88s] English:** Yeah.  
**Translation:** 

**[955.88s] English:** Yeah.  
**Translation:** 

**[956.88s] English:** The notion of Chris has always been the source of human psychology and human experience.  
**Translation:** 

**[960.00s] English:** Which seems to almost contradict intelligence and reason,  
**Translation:** 

**[965.40s] English:** Like emotions, like fear, like love, all of those things,  
**Translation:** Vocabulary: contradict: 违背

**[971.16s] English:** Are those not connected in any way to the space of ideas?  
**Translation:** 

**[977.56s] English:** That, I don't know.  
**Translation:** 

**[979.54s] English:** I just want to be focused on a very simple story.  
**Translation:** 

**[986.18s] English:** On digit recognition.  
**Translation:** Vocabulary: digit: 位数

**[987.56s] English:** So, you don't think you have to love and fear death?  
**Translation:** 

**[990.38s] English:** In order to recognize digits?  
**Translation:** Vocabulary: digits: 阿拉伯数字

**[992.82s] English:** I don't know, because it's so complicated.  
**Translation:** 

**[997.04s] English:** It involves a lot of stuff which I never considered.  
**Translation:** 

**[1001.44s] English:** But I know about digit recognition.  
**Translation:** 

**[1005.08s] English:** And I know that for digit recognition,  
**Translation:** 

**[1010.70s] English:** To get records from a small number of observations,  
**Translation:** 

**[1016.44s] English:** You need...  
**Translation:** 

**[1017.56s] English:** You need a predicate.  
**Translation:** 

**[1019.42s] English:** But there isn't a special predicate for this problem.  
**Translation:** Vocabulary: predicate: 谓词

**[1023.62s] English:** But, "universal predicate" that understands the world of images.  
**Translation:** 

**[1028.62s] English:** Of visual information.  
**Translation:** 

**[1029.68s] English:** Visual, yeah.  
**Translation:** 

**[1031.42s] English:** But on the first step, they understand, say,  
**Translation:** 

**[1035.80s] English:** World of handwritten digits, or characters,  
**Translation:** 

**[1039.80s] English:** Or something simple.  
**Translation:** 

**[1041.66s] English:** So, like you said, symmetry is an interesting point.  
**Translation:** 

**[1043.68s] English:** No, that's what I think one of the predicates.  
**Translation:** Vocabulary: predicates: 谓词; symmetry: 对称

**[1046.94s] English:** It's related to symmetry, to the level of symmetry.  
**Translation:** 

**[1050.94s] English:** Okay, degree of symmetry.  
**Translation:** 

**[1052.12s] English:** So, you think symmetry at the bottom is a universal notion?  
**Translation:** 

**[1057.20s] English:** And there are degrees of a single kind of symmetry.  
**Translation:** 

**[1061.50s] English:** Or is there are many kinds of symmetries?  
**Translation:** 

**[1064.14s] English:** Many kinds of symmetries.  
**Translation:** Vocabulary: symmetries: 对称性

**[1066.00s] English:** There is a symmetry, antisymmetry, like the letter S.  
**Translation:** 

**[1072.34s] English:** So, it has vertical anti-symmetry.  
**Translation:** Vocabulary: antisymmetry: 反对称; vertical: 垂直

**[1076.94s] English:** And it goes on and on and on and on and on and on and on.  
**Translation:** 

**[1080.00s] English:** Be diagonal symmetry, vertical symmetry. So, when you cut it vertically, the letter "S" has no symmetry, yeah.  
**Translation:** Vocabulary: diagonal: 对角线; vertically: 垂直地

**[1088.56s] English:** Then, the upper part and lower part are inverted along the y-axis, yeah.  
**Translation:** 

**[1098.72s] English:** But that's just like one example of symmetry, right? Isn't there a degree of  
**Translation:** Vocabulary: inverted: 倒置

**[1104.80s] English:** Symmetry, if you play all this linearity of stuff to do tangent distance, but whatever I.  
**Translation:** 

**[1115.68s] English:** Described, you can do; you can have a degree of symmetry, and that is what describing reasons.  
**Translation:** Vocabulary: tangent: 切线

**[1124.80s] English:** Image: It is the same as you would describe this image saying,  
**Translation:** 

**[1134.80s] English:** Digits it has anti-symmetry; digit three is symmetric, more or less. Look for symmetry.  
**Translation:** Vocabulary: digit: 手指; digits: 数字; symmetric: 对称的; symmetry: 对称性

**[1144.32s] English:** Do you think that concepts like symmetry, as predicates, are hierarchical?  
**Translation:** 

**[1152.48s] English:** A set of concepts, or are these independent, distinct predicates that we want to discover some set of?  
**Translation:** Vocabulary: hierarchical: 层次分明的; predicates: 谓词

**[1164.80s] English:** The degree of symmetry: Is it, or is it not? You see, this is a very interesting example.  
**Translation:** 

**[1172.08s] English:** Of the category of symmetry, you can explore this idea of symmetry further.  
**Translation:** 

**[1181.84s] English:** Very generally, like the degree of symmetry, a degree of symmetry can be zero, meaning no symmetry at all.  
**Translation:** 

**[1188.88s] English:** Or, in terms of the degree of symmetry, it is more or less symmetrical.  
**Translation:** Vocabulary: symmetrical: 对称的

**[1194.80s] English:** Diagonal and anti-symmetry is also considered.  
**Translation:** 

**[1200.00s] English:** Of symmetry, what about shape in general? I mean, symmetry is a fascinating notion, but...  
**Translation:** Vocabulary: diagonal: 对角线的

**[1205.56s] English:** No, I'm talking about digit. I would like to concentrate on that. All I would like to know is the predicate.  
**Translation:** 

**[1213.00s] English:** For digital recognition, yes, but symmetry is not enough for digit recognition, right? It isn't.  
**Translation:** Vocabulary: predicate: 主谓词

**[1219.94s] English:** Necessarily, for digital recognition, it helps to create invariants which you can use.  
**Translation:** 

**[1230.00s] English:** When you will have examples for digital recognition, you have a regular problem of  
**Translation:** Vocabulary: invariants: 不变量

**[1237.26s] English:** Digital recognition: You have examples of first-class or second-class, plus you know that.  
**Translation:** 

**[1242.58s] English:** There is this concept of symmetry, and you apply it when you're looking for a decision rule.  
**Translation:** Vocabulary: symmetry: 对称性

**[1249.58s] English:** You.  
**Translation:** 

**[1249.92s] English:** Will apply the concept of symmetry for this level of symmetry, which you estimate from:  
**Translation:** 

**[1259.12s] English:** So, let's talk. Everything comes from weak convergence. What is convergence? What is it?  
**Translation:** 

**[1268.14s] English:** Weak convergence, what is strong convergence? I'm sorry, I'm going to do this to you, what are  
**Translation:** Vocabulary: convergence: 趋近

**[1273.60s] English:** We are converging from and to you. You're converging; you would like to have a function.  
**Translation:** 

**[1279.56s] English:** The function, which is called an indicator function, which indicates your digit five, for example, a  
**Translation:** Vocabulary: converging: 汇聚; digit: 位数; indicator: 指示器

**[1290.04s] English:** Classification Task: Let's talk only about classification. So, classification means you  
**Translation:** 

**[1295.90s] English:** Will say whether this is a five or not, or say which of the ten digits it is—right, right. I would.  
**Translation:** Vocabulary: classification: 类别划分; digits: 阿拉伯数字

**[1302.44s] English:** Like to have these functions, then.  
**Translation:** 

**[1309.56s] English:** I have some examples I can consider, which are properties of these examples.  
**Translation:** 

**[1320.00s] English:** Say, "symmetry," and I can measure the level of symmetry for every digit.  
**Translation:** 

**[1320.04s] English:** I have some examples I can consider, which are properties of these examples.  
**Translation:** 

**[1328.16s] English:** And then I can take an average from my training data, and I will consider only functions of...  
**Translation:** 

**[1342.64s] English:** Conditional probability, which I'm looking for in my decision rule, which applying to  
**Translation:** Vocabulary: conditional: 条件概率

**[1351.88s] English:** Digits will give me the same average as I observed on training data.  
**Translation:** 

**[1362.08s] English:** So, actually, this is a different level of description of what you want.  
**Translation:** 

**[1368.64s] English:** You want not just your show.  
**Translation:** 

**[1372.54s] English:** Not.  
**Translation:** 

**[1372.64s] English:** Not one digit.  
**Translation:** 

**[1374.04s] English:** You show this predicate, showing a general property of all the digits which you have in mind.  
**Translation:** Vocabulary: digit: 位数; predicate: 断言

**[1383.68s] English:** If you have in mind digit three, it gives you the property of digit three, and you select:  
**Translation:** 

**[1391.88s] English:** As an admissible set of functions, only those functions keep this property.  
**Translation:** Vocabulary: admissible: 可接受的

**[1396.92s] English:** You will not consider other functions.  
**Translation:** 

**[1400.72s] English:** So, you immediately.  
**Translation:** 

**[1402.54s] English:** Looking for a smaller subset of functions.  
**Translation:** 

**[1404.88s] English:** That's what you mean by admissible functions.  
**Translation:** 

**[1406.98s] English:** Admissible function, exactly.  
**Translation:** 

**[1408.38s] English:** Which is still a pretty large.  
**Translation:** 

**[1410.90s] English:** For the number three, it's a large one.  
**Translation:** 

**[1412.94s] English:** It is pretty large, but if you have one predicate,  
**Translation:** 

**[1416.34s] English:** Right.  
**Translation:** 

**[1416.54s] English:** But according to Weak, there is a strong and weak convergence.  
**Translation:** Vocabulary: convergence: 趋同

**[1422.72s] English:** Strong convergence is convergence in function.  
**Translation:** 

**[1426.34s] English:** You're looking for the function, on one function, and you're looking for another function.  
**Translation:** 

**[1431.86s] English:** Okay.  
**Translation:** 

**[1431.94s] English:** I got it.  
**Translation:** 

**[1433.22s] English:** That something isn't right.  
**Translation:** 

**[1435.36s] English:** No one knows.  
**Translation:** 

**[1436.22s] English:** Yes.  
**Translation:** 

**[1436.48s] English:** This is not the case.  
**Translation:** 

**[1438.22s] English:** Yes, two perceive, also no.  
**Translation:** 

**[1440.00s] English:** In any point, make a square, make an integral, and it should be small. That is convergence.  
**Translation:** Vocabulary: integral: 积分; perceive: 感知

**[1446.66s] English:** In a function, suppose you have some function—any function. So, I would say: "I say that some.  
**Translation:** 

**[1454.94s] English:** A function converges to this function if the integral of the square difference between them is small.  
**Translation:** Vocabulary: converges: 趋近

**[1462.96s] English:** That's the definition of strong convergence.  
**Translation:** 

**[1464.74s] English:** That definition of strong convergence.  
**Translation:** 

**[1465.74s] English:** Two functions: the integral of their difference is small.  
**Translation:** 

**[1468.80s] English:** It is convergence in functions. But you have a different convergence in functionals.  
**Translation:** Vocabulary: functionals: 函数泛函

**[1476.64s] English:** You take any function, you take some function φ, and take its inner product. This function is  
**Translation:** 

**[1483.58s] English:** For the function \( f \) and the function \( f_0 \), which you want to find, and that gives you some value.  
**Translation:** 

**[1492.44s] English:** So, you say that set of functions converges.  
**Translation:** 

**[1498.80s] English:** In an inner product with this function, if this value of the inner product converges to the value f0,  
**Translation:** 

**[1509.94s] English:** That is for one φ. But weak convergence requires that it converge for any function.  
**Translation:** 

**[1516.88s] English:** Of Hilbert space. If it converges for any function in Hilbert space, then you will say that this is  
**Translation:** Vocabulary: converge: 趋近; convergence: 收敛; hilbert: 希尔伯特空间

**[1526.50s] English:** Weak convergence.  
**Translation:** 

**[1528.80s] English:** And you think that when you take an integral, that is its integral property of a function.  
**Translation:** Vocabulary: integral: 整体的

**[1536.12s] English:** For example, if you take the sine or cosine, it is the coefficient in a Fourier expansion.  
**Translation:** 

**[1545.74s] English:** So, if it converges for all coefficients of the Fourier expansion, then under some conditions, it converges.  
**Translation:** Vocabulary: coefficient: 系数; coefficients: 系数; converges: 收敛; cosine: 余弦; fourier: 傅里叶

**[1555.18s] English:** To a function, you're looking for.  
**Translation:** 

**[1558.80s] English:** Audience means.  
**Translation:** 

**[1560.00s] English:** Any property. Convergence is not pointwise, but has an integral property of the function. So, weak convergence.  
**Translation:** 

**[1570.88s] English:** Means an integral property of functions. When I talk about predicate, I would like to formulate.  
**Translation:** Vocabulary: predicate: 谓词

**[1580.82s] English:** Which integral properties I would like to have for convergence. If I were to take one predicate,  
**Translation:** 

**[1592.74s] English:** Function which I measure property: if I will use one predicate and say I will consider,...  
**Translation:** 

**[1602.00s] English:** Only function which gives me the same value as with this predicate, I am selecting a set of  
**Translation:** 

**[1609.96s] English:** Functions:  
**Translation:** Vocabulary: selecting: 选择

**[1610.80s] English:** From functions which are admissible in the sense that the function I am looking for in this set.  
**Translation:** 

**[1619.58s] English:** Of functions. Because by checking in the training data, it gives the same.  
**Translation:** Vocabulary: admissible: 可接受的

**[1628.74s] English:** Yes, it always has to be connected to the training data, in terms of...  
**Translation:** 

**[1632.60s] English:** Yeah, but property—you can know independent of training data. And this guy, prop,...  
**Translation:** 

**[1640.80s] English:** Prop, prop, prop.  
**Translation:** 

**[1641.80s] English:** Prop, prop, prop, prop, prop, prop, prop, prop, prop, prop, prop, prop, prop, prop, prop, prop, prop.  
**Translation:** 

**[1642.80s] English:** Yeah.  
**Translation:** 

**[1643.80s] English:** So that there is a formal property: 31 property, and you give...  
**Translation:** 

**[1644.80s] English:** A fairy tale, Russian fairy tale.  
**Translation:** 

**[1645.80s] English:** Right, but a Russian fairy tale is not so interesting. More interesting are people.  
**Translation:** 

**[1652.36s] English:** Applied this to movies, to theater, to different things, and the same works—they're universal.  
**Translation:** 

**[1662.10s] English:** Well, so I would argue that there's a little bit of a difference between the kinds of things.  
**Translation:** 

**[1668.10s] English:** That were applied to, which are essentially stories and kinds of things that were applied.  
**Translation:** 

**[1669.10s] English:** To be more specific, these are essentially stories.  
**Translation:** 

**[1670.10s] English:** Yeah, yeah.  
**Translation:** 

**[1670.16s] English:** Yeah.  
**Translation:** 

**[1670.20s] English:** Yeah.  
**Translation:** 

**[1670.24s] English:** Yeah.  
**Translation:** 

**[1670.34s] English:** Yeah, yeah.  
**Translation:** 

**[1670.46s] English:** Yeah.  
**Translation:** 

**[1670.52s] English:** Yeah.  
**Translation:** 

**[1670.60s] English:** Yeah.  
**Translation:** 

**[1670.80s] English:** And digit recognition: it is the same story. You're saying digits, there's a story within the...  
**Translation:** 

**[1678.88s] English:** Digit, yeah.  
**Translation:** Vocabulary: digit: 位数; digits: 多位数

**[1680.00s] English:** But my point is: why I hope that it's possible to beat a record using not 60,000, but say 100 times less.  
**Translation:** 

**[1693.60s] English:** Because instead, you will give predicates.  
**Translation:** Vocabulary: predicates: 谓词

**[1697.82s] English:** And you will select your decision not from a wide set of functions, but from a set of functions which keep these predicates.  
**Translation:** 

**[1707.12s] English:** But "predicate" is not related just to digit recognition, like in Plato's case.  
**Translation:** Vocabulary: predicate: 谓词

**[1716.88s] English:** Do you think it's possible to automatically discover the predicates?  
**Translation:** 

**[1722.06s] English:** So, you basically said that the essence of intelligence is the discovery of good predicates.  
**Translation:** 

**[1729.56s] English:** Yeah.  
**Translation:** 

**[1730.88s] English:** Now, the natural question is: "You know, that's what Einstein was good at doing.  
**Translation:** Vocabulary: einstein: 爱因斯坦

**[1737.12s] English:** He was good at doing physics.  
**Translation:** 

**[1738.96s] English:** Can we make machines do these kinds of discoveries of good predicates?  
**Translation:** 

**[1744.26s] English:** Or is this ultimately a human endeavor?  
**Translation:** 

**[1747.78s] English:** That, I don't know.  
**Translation:** Vocabulary: endeavor: 努力

**[1748.94s] English:** I don't think that machine can do it.  
**Translation:** 

**[1751.36s] English:** Because, according to the theory of weak convergence, any function from a Hilbert space can be represented.  
**Translation:** Vocabulary: convergence: 收敛; hilbert: 希尔伯特

**[1762.98s] English:** So, you have an infinite number of predicates.  
**Translation:** 

**[1766.68s] English:** And apparently,...  
**Translation:** Vocabulary: infinite: 无穷的

**[1767.12s] English:** And before, you didn't know which predicate was good and which.  
**Translation:** 

**[1772.80s] English:** But whatever prop show, and why people call it a breakthrough,  
**Translation:** 

**[1779.96s] English:** That there are not too many predicates that cover most situations that happen in the world.  
**Translation:** 

**[1790.88s] English:** So, there's a sea of predicates.  
**Translation:** Vocabulary: predicates: 谓词

**[1793.92s] English:** And most of the...  
**Translation:** 

**[1795.62s] English:** Only a small amount.  
**Translation:** 

**[1797.12s] English:** Are useful for the kinds of things that happen in the world.  
**Translation:** 

**[1800.00s] English:** I think that I would say only a small part of the predicate is very useful; all of it isn't.  
**Translation:** Vocabulary: predicate: 谓语部分

**[1809.60s] English:** All of them, only very few are what we should call them "good predicates.  
**Translation:** 

**[1815.24s] English:** Very good, predicate. Very good predicates, so can we linger on it? What's your  
**Translation:** Vocabulary: linger: 逗留

**[1821.24s] English:** Intuition: Why is it hard for a machine to discover good predicates? I even  
**Translation:** 

**[1828.00s] English:** My talk described how to define predicates and how to find new ones. I'm not sure.  
**Translation:** Vocabulary: intuition: 直觉

**[1833.28s] English:** That's very good. What did you propose in your talk? No, in my talk, I gave  
**Translation:** 

**[1839.44s] English:** Example for diabetes, when we achieve a certain percentage, then we're looking  
**Translation:** Vocabulary: diabetes: 糖尿病

**[1847.26s] English:** From the area where some sort of predicate, which I formulate, does not  
**Translation:** 

**[1858.00s] English:** Keeps invariant, so if it doesn't keep that invariant, I retrain my data and select only relevant functions.  
**Translation:** Vocabulary: invariant: 不变量

**[1869.38s] English:** Which keeps it invariant in the way I did it; I improve my performance.  
**Translation:** 

**[1874.80s] English:** Looking for this predicate, I know technically I have to do that, and you can.  
**Translation:** Vocabulary: technically: 从技术上说

**[1880.12s] English:** Of course, do it using a machine, but I'm not sure that we will.  
**Translation:** 

**[1888.00s] English:** Construct the smartest predicate, but this is the point where I should linger on it.  
**Translation:** Vocabulary: predicate: 谓词

**[1893.70s] English:** Because that's the essence—that's the challenge—that is artificial, that's  
**Translation:** 

**[1897.84s] English:** That's the human-level intelligence we seek: the discovery of these good  
**Translation:** 

**[1902.82s] English:** Predicates: You've talked about deep learning as a way to the predicates they  
**Translation:** 

**[1908.46s] English:** Use, and the functions are mediocre; we can find better ones. Let's talk about it.  
**Translation:** Vocabulary: mediocre: 平庸; predicates: 谓词

**[1915.76s] English:** Deep learning, sure, let's do it!  
**Translation:** 

**[1918.00s] English:** I know only  
**Translation:** 

**[1920.00s] English:** Young slickoon convolutional network, and what else I don't know, and it's a very simple convolution.  
**Translation:** 

**[1927.84s] English:** There's not much else left, and right; yes, I can do it like that one, this one: predicate, it is.  
**Translation:** Vocabulary: convolution: 卷积; convolutional: 卷积的

**[1934.56s] English:** Convolution is a single predicate; it's single, it's a single predicate, yes, it is. You know, exactly.  
**Translation:** 

**[1943.52s] English:** You take the derivative for translation, and this should be kept.  
**Translation:** Vocabulary: derivative: 导数

**[1950.96s] English:** So, that's a single predicate, but humans discovered that one—or at least,  
**Translation:** 

**[1955.60s] English:** Not that is a realistic story; not too many predators do, and that is a big story because Jan did it.  
**Translation:** Vocabulary: predators: 捕食者

**[1962.24s] English:** 25 years ago, and nothing so clear was added to the deep network, and then I don't understand.  
**Translation:** 

**[1973.68s] English:** Uh, why should we talk about deep networks instead of talking about piecewise linear functions?  
**Translation:** Vocabulary: linear: 线性的; piecewise: 分段的

**[1981.12s] English:** Which keeps this predicate well, the you know, a counter-argument is.  
**Translation:** 

**[1987.20s] English:** That might be the amount of predicates necessary to solve general intelligence.  
**Translation:** Vocabulary: predicate: 谓词

**[1994.32s] English:** Say, in the space of images, doing efficient recognition of handwritten digits is very small.  
**Translation:** 

**[2002.24s] English:** And  
**Translation:** Vocabulary: digits: 阿拉伯数字; handwritten: 手写

**[2003.52s] English:** So, we shouldn't be so obsessed with finding; we'll find other good predicates like convolution.  
**Translation:** 

**[2009.60s] English:** For example, you know, there have been other advancements, like, if you look at the work,...  
**Translation:** Vocabulary: advancements: 进步; convolution: 卷积; obsessed: 痴迷; predicates: 谓词

**[2016.16s] English:** With attention, there are attentional mechanisms, especially used in natural language processing.  
**Translation:** 

**[2022.24s] English:** Focusing the network's ability to learn at which part of the input to look at.  
**Translation:** Vocabulary: attentional: 注意力的

**[2027.52s] English:** The thing is, there are other things besides predicates that are important for the actual.  
**Translation:** 

**[2033.28s] English:** Engineering mechanism of showing how much you can really do given such predicates.  
**Translation:** 

**[2040.00s] English:** I mean, that's essentially the work of deep learning: constructing architectures that are able to be given training data to converge towards a function that can approximate and generalize well.  
**Translation:** 

**[2062.44s] English:** It's an engineering problem.  
**Translation:** Vocabulary: approximate: 近似; constructing: 构建; converge: 收敛; generalize: 泛化

**[2063.90s] English:** Yeah, I understand.  
**Translation:** 

**[2065.94s] English:** But let's talk not on an emotional level, but on a mathematical level.  
**Translation:** Vocabulary: mathematical: 数学的

**[2071.78s] English:** You have a set of piecewise linear functions.  
**Translation:** 

**[2076.02s] English:** It is all possible with neural networks.  
**Translation:** Vocabulary: linear: 线性的; neural: 神经网络的; piecewise: 分段线性的

**[2081.50s] English:** It's just piecewise linear functions.  
**Translation:** 

**[2084.00s] English:** There are many, many pieces.  
**Translation:** 

**[2085.28s] English:** A large, large number of piecewise linear functions.  
**Translation:** 

**[2087.10s] English:** Okay, exactly.  
**Translation:** 

**[2088.44s] English:** Very large.  
**Translation:** 

**[2089.38s] English:** Very large.  
**Translation:** 

**[2090.14s] English:** Almost feels like it's too large.  
**Translation:** 

**[2091.64s] English:** It's still simpler than....  
**Translation:** 

**[2094.78s] English:** Say, "convolutional.  
**Translation:** 

**[2095.98s] English:** Then, reproducing kernel Hilbert spaces, which have a Hilbert space of functions.  
**Translation:** Vocabulary: convolutional: 卷积的

**[2100.80s] English:** What is Hilbert space?  
**Translation:** 

**[2102.90s] English:** It's space with an infinite number of coordinates, or a function for expansion, something like that.  
**Translation:** Vocabulary: coordinates: 坐标; hilbert: 希尔伯特; infinite: 无限的

**[2111.72s] English:** So, it's much richer.  
**Translation:** 

**[2114.44s] English:** So, and when I'm talking about a closed-form solution, I'm talking about this set of functions.  
**Translation:** 

**[2121.18s] English:** Not a piecewise linear set, which is...  
**Translation:** 

**[2123.90s] English:** Particular case of:  
**Translation:** 

**[2128.90s] English:** It's a small part.  
**Translation:** 

**[2130.88s] English:** So, neural networks is just a small part of the space of functions you're talking about.  
**Translation:** 

**[2135.90s] English:** Say, small set of functions.  
**Translation:** 

**[2139.02s] English:** Let me take that.  
**Translation:** 

**[2140.46s] English:** But it is fine.  
**Translation:** 

**[2142.00s] English:** It is fine.  
**Translation:** 

**[2142.74s] English:** I don't want to discuss the small or the big.  
**Translation:** 

**[2146.58s] English:** You take advantage.  
**Translation:** 

**[2147.90s] English:** So, you have a set of functions.  
**Translation:** 

**[2150.64s] English:** So, now, when you're trying to create architecture,...  
**Translation:** 

**[2153.90s] English:** You would like to create an admissible set of functions.  
**Translation:** 

**[2158.90s] English:** All your tricks.  
**Translation:** Vocabulary: admissible: 可接受的

**[2160.00s] English:** To use not all functions,  
**Translation:** 

**[2163.06s] English:** But some subset of this set of functions.  
**Translation:** 

**[2167.24s] English:** Say, when you're introducing a convolutional network,  
**Translation:** 

**[2170.04s] English:** It is a way to make this subset useful for you.  
**Translation:** 

**[2176.06s] English:** But, from my point of view,  
**Translation:** 

**[2178.94s] English:** Convolutional, it is something.  
**Translation:** Vocabulary: convolutional: 卷积的

**[2181.94s] English:** You want to keep some invariance.  
**Translation:** 

**[2184.84s] English:** Say, translation invariance.  
**Translation:** Vocabulary: invariance: 不变性

**[2186.30s] English:** But now, if you understand this,  
**Translation:** 

**[2191.74s] English:** And you cannot explain.  
**Translation:** 

**[2194.62s] English:** On the level of ideas,  
**Translation:** 

**[2197.46s] English:** What neural network does is,  
**Translation:** 

**[2201.18s] English:** You should agree that it is much better.  
**Translation:** 

**[2204.20s] English:** To have a set of functions.  
**Translation:** 

**[2206.62s] English:** And they say, "This set of functions,  
**Translation:** 

**[2208.68s] English:** Should be admissible.  
**Translation:** 

**[2210.92s] English:** It must keep this invariant.  
**Translation:** 

**[2212.82s] English:** This invariant, and that invariant.  
**Translation:** Vocabulary: invariant: 不变量

**[2214.54s] English:** You know that.  
**Translation:** 

**[2215.98s] English:** As soon as you incorporate new invariants,  
**Translation:** Vocabulary: incorporate: 吸收; invariants: 不变量

**[2219.14s] English:** Set of functions,  
**Translation:** 

**[2219.92s] English:** Because it keeps getting smaller and smaller and smaller.  
**Translation:** 

**[2222.24s] English:** But all the invariants are specified.  
**Translation:** 

**[2223.90s] English:** By you, the human.  
**Translation:** Vocabulary: specified: 指定的

**[2226.68s] English:** Yeah.  
**Translation:** 

**[2227.38s] English:** But what I hope,  
**Translation:** 

**[2229.66s] English:** That there is a standard predicate,  
**Translation:** 

**[2232.50s] English:** Like a property show.  
**Translation:** Vocabulary: predicate: 谓词

**[2235.88s] English:** That's what I want to find.  
**Translation:** 

**[2237.96s] English:** For digit recognition.  
**Translation:** Vocabulary: digit: 位数

**[2239.66s] English:** If we start, it is a completely new area.  
**Translation:** 

**[2242.80s] English:** Of what is intelligence about?  
**Translation:** 

**[2244.42s] English:** On the level.  
**Translation:** 

**[2245.14s] English:** So, starting from plot as an idea.  
**Translation:** 

**[2248.24s] English:** What is the Vault of Ideas?  
**Translation:** 

**[2250.64s] English:** So, and I believe that it's not too many.  
**Translation:** Vocabulary: vault: 金库

**[2254.64s] English:** Yeah.  
**Translation:** 

**[2256.14s] English:** But, you know, it is amusing.  
**Translation:** 

**[2258.74s] English:** That mathematician is doing something.  
**Translation:** 

**[2260.64s] English:** In a neural network, in general, function,  
**Translation:** Vocabulary: neural: 神经网络的

**[2263.64s] English:** But people from literature, from art,  
**Translation:** 

**[2266.64s] English:** They use this all the time.  
**Translation:** 

**[2269.14s] English:** That's right.  
**Translation:** 

**[2270.14s] English:** Invariance: Saying it is great.  
**Translation:** Vocabulary: invariance: 不变性

**[2274.70s] English:** How people describe music,  
**Translation:** 

**[2277.00s] English:** We should learn from that.  
**Translation:** 

**[2278.80s] English:** And something,...  
**Translation:** 

**[2280.00s] English:** This level, but so why? Vladimir, probe—who was just theoretical and who studied—  
**Translation:** 

**[2289.78s] English:** Theoretical literature: He found that, you know; let me throw that right back at you.  
**Translation:** 

**[2295.12s] English:** Because there's a little bit that's less mathematical and more emotional.  
**Translation:** 

**[2299.82s] English:** Philosophical, Vladimir. Prop: I mean, he wasn't doing math, no, and you just said.  
**Translation:** 

**[2307.76s] English:** Another emotional statement: "which is, you believe that this Platonic world of  
**Translation:** Vocabulary: philosophical: 哲学的; platonic: 理念的

**[2313.44s] English:** Ideas are small. I hope. I hope, dude. No, do you have any intuition, though?  
**Translation:** 

**[2322.26s] English:** We can linger on it, yeah. You know, about this—not just small or big—I know.  
**Translation:** Vocabulary: intuition: 直觉; linger: 停留

**[2328.76s] English:** Exactly, then, when I was introducing the predicate,  
**Translation:** 

**[2335.88s] English:** I decrease.  
**Translation:** Vocabulary: predicate: 主谓词

**[2337.52s] English:** Something.  
**Translation:** 

**[2337.74s] English:** Of functions, but my goal is to decrease the set of functions as much as possible.  
**Translation:** 

**[2345.42s] English:** Much as possible, a good predicate which does this, then I should choose the next predicate which.  
**Translation:** 

**[2353.50s] English:** Does which decrease set as much as possible? So, it is a good predicate such that they decrease.  
**Translation:** 

**[2362.62s] English:** This amount of admissible functions; so, if each good predicate significantly reduces the set of.  
**Translation:** 

**[2371.34s] English:** Admissible functions: that there naturally shouldn't be that many, yeah. Predicates: no, but but  
**Translation:** Vocabulary: admissible: 允许的; predicates: 谓词

**[2378.46s] English:** If you reduce the VC dimension of the function very well, the set of admissible functions is small.  
**Translation:** 

**[2386.70s] English:** And you don't need too much training data to do well.  
**Translation:** Vocabulary: dimension: 维数

**[2392.94s] English:** And VC dimension, by the way, is a measure of the capacity of this set of functions, right?  
**Translation:** 

**[2399.26s] English:** Roughly speaking,  
**Translation:** 

**[2400.00s] English:** Have many functions in this set. You're decreasing, decreasing, and it makes it easy for you to find.  
**Translation:** 

**[2407.60s] English:** Functions you're looking for. The most important part is to create a good, admissible set of.  
**Translation:** Vocabulary: decreasing: 减少的

**[2414.48s] English:** Functions. There are many ways, but a good predicate should be such that it can do that. For this,  
**Translation:** 

**[2427.36s] English:** Duck, you should know a little bit about ducks. What are the three fundamental laws of ducks?  
**Translation:** Vocabulary: predicate: 谓词

**[2435.28s] English:** It looks like a duck, swims like a duck, and quacks like a duck.  
**Translation:** 

**[2438.24s] English:** You should know something about ducks to be able to—  
**Translation:** Vocabulary: quacks: 叫

**[2441.04s] English:** Not necessarily. It looks like a horse, but it's also good.  
**Translation:** 

**[2447.76s] English:** It generalizes from ducks.  
**Translation:** Vocabulary: generalizes: 泛化

**[2449.68s] English:** Yes, and talk like a horse, and make sounds like a horse, and run like a horse, and move like a horse.  
**Translation:** 

**[2457.36s] English:** It is general. It is a general predicate that this applies to ducks. But for ducks, you can say,  
**Translation:** 

**[2467.12s] English:** Play chess like a duck.  
**Translation:** 

**[2469.84s] English:** You cannot say "play chess like duck.  
**Translation:** 

**[2471.52s] English:** Why not?  
**Translation:** 

**[2472.88s] English:** You're saying you can, but that wouldn't be a good—  
**Translation:** 

**[2475.68s] English:** No, you will not reduce a lot of functions.  
**Translation:** 

**[2478.16s] English:** You will not do that, yeah; you would not reduce the set of functions.  
**Translation:** 

**[2481.60s] English:** So, the story is: formal story, mathematical story,...  
**Translation:** 

**[2487.36s] English:** You can use any function you want as a predicate. But some of them are good, and some of them are not.  
**Translation:** Vocabulary: mathematical: 数学的

**[2493.12s] English:** Because some of them reduce many functions to an admissible set, some of them -  
**Translation:** 

**[2499.68s] English:** But the question is, and I'll probably keep asking this question: how do we find such,  
**Translation:** Vocabulary: admissible: 可接受的

**[2505.60s] English:** What's your intuition? Handwritten recognition. How do we find the answer to your challenge?  
**Translation:** 

**[2512.48s] English:** Yeah, yeah. I understand it that way. I understand volts.  
**Translation:** Vocabulary: handwritten: 手写; intuition: 直觉; volts: 伏特

**[2518.08s] English:** What defines?  
**Translation:** 

**[2519.04s] English:** What it means.  
**Translation:** 

**[2520.00s] English:** A new predicate, yeah, like a guy who understands music can say this word which he described him.  
**Translation:** 

**[2527.36s] English:** When he listened to music, he understood it better. He didn't use too many different words, and oh, you could do something like that too.  
**Translation:** Vocabulary: predicate: 谓词

**[2535.44s] English:** You can make a collection of what he's talking about, music, about this, and that; it's not too many.  
**Translation:** 

**[2542.00s] English:** Different situations he described, because we mentioned Vladimir; proper bunch. Let me just.  
**Translation:** 

**[2547.28s] English:** Mention there's a sequence of 31 structural notions that are common in stories.  
**Translation:** 

**[2556.80s] English:** And I think you call them "units," and I think they resonate. I mean, it starts just to give an...  
**Translation:** Vocabulary: notions: 概念

**[2562.96s] English:** Example: An absentee member of the hero's community, a family leaves the security of the home environment.  
**Translation:** 

**[2568.72s] English:** Then it goes to the interdiction, where an forbidding edict or command is passed upon the hero.  
**Translation:** Vocabulary: absentee: 缺席者; edict: 诏令; interdiction: 禁令

**[2574.40s] English:** Don't go there; don't do this, the heroes.  
**Translation:** 

**[2577.28s] English:** Against any action, then step three: violation of interdiction; brace yourself, you know, break.  
**Translation:** Vocabulary: brace: 支撑

**[2585.36s] English:** The rules break out on their own, then reconnaissance: the villain makes an effort to attain.  
**Translation:** 

**[2590.80s] English:** Knowledge needs to fulfill its plot, so on it goes like this, ending in a wedding.  
**Translation:** Vocabulary: attain: 达到; fulfill: 实现; reconnaissance: 侦察; villain: 反派

**[2597.92s] English:** Number 31, yeah, "happily ever after." No, he just gave a description of all the situations he understands.  
**Translation:** 

**[2606.64s] English:** This vault  
**Translation:** Vocabulary: vault: 金库

**[2608.00s] English:** Of folktales, yeah. Not for stories, and this story is not just in folktales; the stories are in...  
**Translation:** 

**[2618.08s] English:** Detective serials, as well. And probably in our lives, we probably live through things that we read about at the end. They  
**Translation:** Vocabulary: folktales: 民间故事; serials: 连续剧

**[2625.76s] English:** They wrote that this predicate is good for different situations, not for movies.  
**Translation:** 

**[2637.28s] English:** By the way, there's also criticism.  
**Translation:** Vocabulary: predicate: 谓语

**[2640.00s] English:** Right, there's another way to interpret narratives from Claude Lévi-Strauss.  
**Translation:** 

**[2649.72s] English:** Don't know—I am NOT in this business, and I know it's theoretical literature, but  
**Translation:** Vocabulary: interpret: 解释; narratives: 叙述

**[2654.50s] English:** It's looking at Paradise. It's always, yeah, yeah, but at least there are units.  
**Translation:** 

**[2662.88s] English:** It's not too many units that can describe, but this guy probably gives.  
**Translation:** 

**[2668.80s] English:** Another unit, or another way, exactly—another, another, another set of units.  
**Translation:** 

**[2673.96s] English:** Another set of predicates; it doesn't matter who, but they exist. Probably, mine.  
**Translation:** Vocabulary: predicates: 断言

**[2682.54s] English:** The question is whether, given those units, we would need our human brains to  
**Translation:** 

**[2687.82s] English:** Interpret these units, and they would still hold as much power as they have meaning.  
**Translation:** 

**[2693.82s] English:** Are those units enough when we give them to an alien species?  
**Translation:** 

**[2698.38s] English:** Let  
**Translation:** Vocabulary: alien: 外星的

**[2698.64s] English:** Let  
**Translation:** 

**[2698.74s] English:** Let  
**Translation:** 

**[2698.78s] English:** Let me ask you: Do you understand digital images? No, I don't know when you  
**Translation:** 

**[2708.92s] English:** Can recognize these digit images; it means that you understand.  
**Translation:** Vocabulary: digit: 位数

**[2715.06s] English:** Characters, you understand? No, no, no, no. It's the imitation versus...  
**Translation:** 

**[2724.46s] English:** Understanding the question, because I don't understand the mechanism by which you  
**Translation:** Vocabulary: imitation: 模仿

**[2728.72s] English:** Can we find proof? Let's see what details are wrong, like this is the  
**Translation:** 

**[2731.88s] English:** Vertical, and that's the artwork; some of the markings are  
**Translation:** Vocabulary: artwork: 艺术品; vertical: 垂直的

**[2739.90s] English:** There, can we actually make an image? Yes, I just didn't know how you do that.  
**Translation:** 

**[2745.56s] English:** But I came up with a nice idea how you can do that, which I know I'm not talking about yet.  
**Translation:** 

**[2747.62s] English:** About predicates, I'm talking about something you understand involves symmetry.  
**Translation:** 

**[2752.80s] English:** Maybe, structuring it might be something that I cannot formulate; I just was able to find it.  
**Translation:** Vocabulary: cannot: 不能; symmetry: 对称

**[2756.86s] English:** That's a very powerful predicate. My question is,  
**Translation:** 

**[2760.00s] English:** Is there a lot more going on that we're not able to introspect? Maybe I need to be able to.  
**Translation:** Vocabulary: introspect: 自我反省; predicate: 谓词

**[2767.74s] English:** Understand a huge amount in the world of ideas—thousands, millions of predicates.  
**Translation:** 

**[2778.30s] English:** In order to do hand recognition, I don't think so; so you're not hoping for that, are you?  
**Translation:** Vocabulary: predicates: 谓词

**[2785.92s] English:** Intuition lets me explain: enough, you're using digits, you're using examples as well; theory says.  
**Translation:** 

**[2795.16s] English:** That, if you will use all possible functions from Hilda Space and all possible predicates, you don't need  
**Translation:** Vocabulary: digits: 阿拉伯数字; intuition: 直觉

**[2806.94s] English:** Training data you just will have an admissible set of functions which contains one function.  
**Translation:** 

**[2815.92s] English:** Yes, so the trade-off is when you're not using all predicates, you're only using a few good.  
**Translation:** Vocabulary: admissible: 可接受的

**[2822.46s] English:** Predicates: You need to have some training data, yes. Exactly; the more, the better.  
**Translation:** 

**[2827.44s] English:** Predicates: You have the less training data, exactly. That is intelligent, still. Okay, I'm.  
**Translation:** 

**[2835.00s] English:** Going to keep asking the same dumb question: handwritten recognition to solve the challenge.  
**Translation:** 

**[2840.16s] English:** You kind of propose a challenge that says we should be able to get state-of-the-art MNIST.  
**Translation:** 

**[2845.32s] English:** Arrow  
**Translation:** 

**[2845.92s] English:** Rates by using very few, maybe fewer than 60, examples per digit: what kind of predicates do you think?  
**Translation:** Vocabulary: digit: 位数

**[2855.34s] English:** It was that challenge. So, people who will solve this problem will answer and they will.  
**Translation:** 

**[2861.04s] English:** Do you think they'll be able to answer it in a human-explainable way?  
**Translation:** 

**[2867.64s] English:** They just need to write a function, that's it. But can that function be written, I guess?  
**Translation:** 

**[2873.82s] English:** By an  
**Translation:** 

**[2875.92s] English:** Automated reasoning system; whether we're talking about  
**Translation:** 

**[2880.00s] English:** Neural network learning a particular function, or another mechanism?  
**Translation:** Vocabulary: automated: 自动化; neural: 神经网络

**[2884.96s] English:** No. I'm not against neural networks. I'm against the admissible set of functions which create.  
**Translation:** 

**[2892.40s] English:** Neural network. You did it by hand. You don't do it by invariance, by predicate, by reason.  
**Translation:** Vocabulary: invariance: 不变性; predicate: 谓词

**[2904.40s] English:** But neural networks can then do the reverse step of helping you.  
**Translation:** 

**[2908.24s] English:** Find a function. The task of a neural network is to find a disentangled representation.  
**Translation:** Vocabulary: disentangled: 分离的

**[2917.20s] English:** For example, is to find that one predicate function that really captures some kind of  
**Translation:** 

**[2924.40s] English:** Essence: One, not the entire essence, but one very useful essence of this particular  
**Translation:** 

**[2930.56s] English:** Visual space. Do you think that's possible? Listen, I'm grasping, hoping there's an  
**Translation:** 

**[2937.68s] English:** Automated  
**Translation:** Vocabulary: grasping: 勉强理解

**[2938.24s] English:** A way to find good predicates, right? So the question is: what are the mechanisms?  
**Translation:** 

**[2942.88s] English:** Of finding good predicates—ideas that you think we should pursue? A young grad student.  
**Translation:** Vocabulary: predicates: 谓词

**[2948.88s] English:** Listening right now, I gave an example. So, find the situation.  
**Translation:** 

**[2956.48s] English:** Where predicates, which you're suggesting, don't create invariants. It's like in physics.  
**Translation:** Vocabulary: invariants: 不变量

**[2968.80s] English:** Find a situation where existing theory cannot explain it.  
**Translation:** 

**[2977.12s] English:** Find a situation where the existing theory can't explain it.  
**Translation:** Vocabulary: cannot: 不能

**[2979.28s] English:** Theory cannot explain this.  
**Translation:** 

**[2980.88s] English:** So, you're finding contradictions.  
**Translation:** Vocabulary: contradictions: 矛盾

**[2982.64s] English:** Find a contradiction, and then remove it. But in my case,  
**Translation:** 

**[2987.52s] English:** What does "contradiction" mean? You find a function such that, if you use this function, you're not keeping...  
**Translation:** Vocabulary: contradiction: 矛盾

**[2994.00s] English:** Invariants. This is:  
**Translation:** 

**[2997.04s] English:** So, really, the process of -  
**Translation:** 

**[2998.22s] English:** The process of discovering contradictions.  
**Translation:** 

**[3000.00s] English:** Yeah, it's like in physics, find a situation where you have a contradiction for one of the properties.  
**Translation:** 

**[3011.70s] English:** For one of the predicates, include this predicate making invariance and solve against.  
**Translation:** 

**[3019.80s] English:** This problem, now you don't have a contradiction, but it's not the best way, probably. I don't know.  
**Translation:** Vocabulary: invariance: 不变性

**[3029.40s] English:** To look for a predicate that's just one-way, okay—that is, there is no known efficient way to reverse it. The brute force method is not ideal.  
**Translation:** 

**[3036.24s] English:** What about the idea of a big, umbrella term like "symbolic AI" in the 80s?  
**Translation:** Vocabulary: brute: 粗暴; predicate: 谓词; symbolic: 符号化的

**[3047.52s] English:** Expert systems, sort of logic-reasoning-based systems, is there any hope to find some through?  
**Translation:** 

**[3057.12s] English:** Sort of deductive reasons.  
**Translation:** Vocabulary: deductive: 演绎的

**[3059.40s] English:** Reasoning to find good predicates, I don't think so. I think that just logic is not enough; it's kind  
**Translation:** 

**[3072.48s] English:** Of a compelling notion, though, you know that when smart people sit in a room and reason through  
**Translation:** Vocabulary: compelling: 有说服力的; predicates: 谓词

**[3078.48s] English:** Things, it seems, are compelling, and making our machines do the same is also compelling, so everything is.  
**Translation:** 

**[3087.00s] English:** Very simple.  
**Translation:** 

**[3089.40s] English:** When you have an infinite number of predicates, you can choose.  
**Translation:** 

**[3096.66s] English:** The function you want has invariants, and you can kill the function you want.  
**Translation:** Vocabulary: infinite: 无穷的

**[3104.70s] English:** You have to have not too many invariants to solve the problem.  
**Translation:** 

**[3116.10s] English:** So, and there is an infinite number of functions.  
**Translation:** Vocabulary: invariants: 不变量

**[3119.64s] English:** Before and after, for instance, you know, in some certain vibe, do you have a mean and you have a  
**Translation:** 

**[3120.00s] English:** Select a finite and hopefully small number of functions, which is good enough to extract.  
**Translation:** Vocabulary: extract: 提取; finite: 有限的

**[3126.16s] English:** Body, and then you have to recognize this as the predicate for the society, and imagine something.  
**Translation:** 

**[3130.68s] English:** Else, set that, and you can do trivial things, for example, you can do.  
**Translation:** Vocabulary: predicate: 主谓; trivial: 琐碎

**[3133.60s] English:** Something else, set something like you will give an integer instead of using a string.  
**Translation:** 

**[3134.10s] English:** A small set of admissible functions.  
**Translation:** Vocabulary: admissible: 允许的; integer: 整数

**[3138.00s] English:** So they will be admissible; it's for sure, because every function just decreases the set of.  
**Translation:** 

**[3139.22s] English:** And then, you know, are you going to decide when we are going to put everything in perfect order?  
**Translation:** Vocabulary: decreases: 减少

**[3143.32s] English:** Function and leaving it admissible, but it will be small.  
**Translation:** 

**[3143.40s] English:** Position, in a colloquial sense, because people often say that you can "Java" and I am going to return.  
**Translation:** Vocabulary: colloquial: 口语的

**[3146.92s] English:** To you, and I also had trouble understanding most of the part-time jobs. At large, I was sort of just  
**Translation:** 

**[3146.92s] English:** But why do you think logic-based systems can't help? Intuition, not...  
**Translation:** Vocabulary: intuition: 直觉

**[3155.10s] English:** Because you should know the reality.  
**Translation:** 

**[3157.86s] English:** You should know about life.  
**Translation:** 

**[3159.68s] English:** This guy, like Prob, he knows something, and he tried to put his understanding in invariant.  
**Translation:** 

**[3168.60s] English:** But that's the human, yeah, see, you're putting too much value into Vladimir Prob's.  
**Translation:** Vocabulary: invariant: 不变量

**[3176.62s] English:** Knowing something.  
**Translation:** 

**[3177.62s] English:** No, it is--;  
**Translation:** 

**[3178.62s] English:** Am I being misunderstood?  
**Translation:** 

**[3179.62s] English:** The story is: what does "life" mean, you know?  
**Translation:** Vocabulary: misunderstood: 被误解

**[3184.56s] English:** What it means:  
**Translation:** 

**[3185.56s] English:** You know common sense.  
**Translation:** 

**[3186.86s] English:** No, no.  
**Translation:** 

**[3188.46s] English:** You know something?  
**Translation:** 

**[3190.62s] English:** Common sense is some rules.  
**Translation:** 

**[3193.48s] English:** You think so?  
**Translation:** 

**[3195.08s] English:** Common sense is simply a set of rules.  
**Translation:** 

**[3197.44s] English:** Common sense is: it's mortality, it's fear of death, it's love, it's spirituality.  
**Translation:** 

**[3204.80s] English:** Yeah.  
**Translation:** 

**[3205.80s] English:** Yeah.  
**Translation:** 

**[3206.62s] English:** It's spirituality, it's happiness and sadness.  
**Translation:** 

**[3210.94s] English:** All of it is tied up into understanding gravity, which is what we think of as common sense.  
**Translation:** Vocabulary: gravity: 引力; spirituality: 精神境界

**[3216.62s] English:** I don't want to discuss such a wide topic.  
**Translation:** 

**[3219.64s] English:** I want to discuss and understand digit recognition.  
**Translation:** Vocabulary: digit: 位数

**[3222.86s] English:** Any time I bring up love and death, you bring it back to digit recognition.  
**Translation:** 

**[3230.06s] English:** I like it.  
**Translation:** 

**[3231.06s] English:** Yeah.  
**Translation:** 

**[3232.06s] English:** No, you know, it is durable because there is a challenge.  
**Translation:** Vocabulary: durable: 耐用

**[3234.56s] English:** Yeah.  
**Translation:** 

**[3235.56s] English:** I mean, you can have a bunch of love and death and all that.  
**Translation:** 

**[3238.96s] English:** And if any of you want to, like me—like, for I'm just saying that this is just my family.  
**Translation:** 

**[3239.88s] English:** Yeah.  
**Translation:** 

**[3240.00s] English:** Student, concentrate on this work. I will suggest something to solve your mean: handwritten recognition.  
**Translation:** 

**[3240.88s] English:** Yeah.  
**Translation:** 

**[3241.88s] English:** Yeah.  
**Translation:** 

**[3242.88s] English:** Yeah.  
**Translation:** 

**[3243.88s] English:** Yeah.  
**Translation:** 

**[3244.88s] English:** Yeah.  
**Translation:** 

**[3245.88s] English:** Yeah.  
**Translation:** 

**[3246.72s] English:** Yeah, it's beautifully simple, elegant, and I think that "invariance" will solve this.  
**Translation:** Vocabulary: elegant: 优雅; invariance: 不变性

**[3246.88s] English:** Yeah.  
**Translation:** 

**[3247.88s] English:** Yeah.  
**Translation:** 

**[3248.88s] English:** Yeah.  
**Translation:** 

**[3249.88s] English:** Yeah.  
**Translation:** 

**[3250.88s] English:** Yeah.  
**Translation:** 

**[3251.88s] English:** It's going to happen.  
**Translation:** 

**[3252.88s] English:** Right.  
**Translation:** 

**[3253.28s] English:** You do, I think so, yes, but it is not universal. It is maybe what I want some universal invariance which  
**Translation:** 

**[3253.88s] English:** Yeah.  
**Translation:** 

**[3254.88s] English:** Yeah.  
**Translation:** 

**[3255.88s] English:** Yeah.  
**Translation:** 

**[3256.88s] English:** Yeah.  
**Translation:** 

**[3257.88s] English:** Yeah.  
**Translation:** 

**[3258.88s] English:** Yeah.  
**Translation:** 

**[3259.88s] English:** Yeah.  
**Translation:** 

**[3260.88s] English:** Yeah.  
**Translation:** 

**[3261.88s] English:** Yeah.  
**Translation:** 

**[3262.88s] English:** Yeah.  
**Translation:** 

**[3263.88s] English:** Yeah.  
**Translation:** 

**[3264.48s] English:** Are good not only for digit recognition, but also for image understanding.  
**Translation:** 

**[3270.56s] English:** So, let me ask: How hard do you think 2D image understanding is?  
**Translation:** 

**[3278.24s] English:** So, if we can kind of intuit handwritten recognition,  
**Translation:** Vocabulary: handwritten: 手写; intuit: 直觉

**[3283.68s] English:** How big of a step, leap, or journey is it from that? If I gave you good solutions or solved your challenges, how significant would that be?  
**Translation:** 

**[3291.76s] English:** For handwriting recognition, how long would my  
**Translation:** Vocabulary: handwriting: 书写

**[3294.48s] English:** Journey then be from that to understanding more general natural images; immediately, you will.  
**Translation:** 

**[3300.56s] English:** Understand this as soon as you will make a record, because it is not for free. As soon as you will  
**Translation:** 

**[3309.52s] English:** Create several invariants, which will help you to get the same performance as the best neural net.  
**Translation:** 

**[3321.60s] English:** Did using it a hundred times maybe?  
**Translation:** Vocabulary: invariants: 不变量; neural: 神经的

**[3324.48s] English:** More than 100 times fewer examples, you have to have something smart to do that, and you're saying...  
**Translation:** 

**[3332.08s] English:** That is invariant, it is predicated because you should have some idea of how to do that.  
**Translation:** Vocabulary: invariant: 不变的; predicated: 基于

**[3339.28s] English:** But okay, let me just pause. Maybe it's a trivial point, maybe not, but handwritten recognition.  
**Translation:** 

**[3347.12s] English:** It feels like a 2D, two-dimensional problem, and it seems like how complicated it is.  
**Translation:** Vocabulary: trivial: 琐碎的

**[3354.48s] English:** It is the fact that most images are a projection of a three-dimensional world.  
**Translation:** 

**[3360.00s] English:** On a 2D plane, it feels like we are in a three-dimensional world,  
**Translation:** 

**[3365.48s] English:** We need to start understanding common sense in order to understand an image.  
**Translation:** 

**[3371.54s] English:** It's no longer a visual shape and symmetry.  
**Translation:** Vocabulary: symmetry: 对称

**[3377.40s] English:** It's having to start to understand concepts and life.  
**Translation:** 

**[3382.16s] English:** Yeah.  
**Translation:** 

**[3384.36s] English:** You're talking about different environments and predicates.  
**Translation:** 

**[3388.30s] English:** Yeah.  
**Translation:** Vocabulary: environments: 环境; predicates: 谓词

**[3388.54s] English:** And potentially a much larger number.  
**Translation:** 

**[3392.54s] English:** You know, maybe, but let's start with something simple.  
**Translation:** 

**[3396.34s] English:** Yeah, but you said it would be immediate.  
**Translation:** 

**[3398.16s] English:** No, you know, I cannot think about things which I don't understand.  
**Translation:** Vocabulary: cannot: 不能

**[3402.88s] English:** This I understand, but I'm sure that I don't understand everything there.  
**Translation:** 

**[3408.40s] English:** Yeah, that's the difference.  
**Translation:** 

**[3409.14s] English:** It's like Einstein said: "Do as simple as possible, but not simpler.  
**Translation:** 

**[3414.18s] English:** And that is exactly the case.  
**Translation:** Vocabulary: einstein: 爱因斯坦

**[3416.48s] English:** With handwriting.  
**Translation:** 

**[3417.18s] English:** With handwriting.  
**Translation:** Vocabulary: handwriting: 书写

**[3418.54s] English:** Yeah, but that's the difference between you and me.  
**Translation:** 

**[3421.78s] English:** I welcome and enjoy thinking about things I completely don't understand.  
**Translation:** 

**[3429.66s] English:** Because, to me, it's a natural extension without having solved handwritten recognition.  
**Translation:** 

**[3434.68s] English:** To wonder how difficult the next step of understanding 2D and 3D images is.  
**Translation:** 

**[3445.34s] English:** Because ultimately, while the science...  
**Translation:** 

**[3448.54s] English:** The science of intelligence is fascinating; it's also fascinating to see how that maps.  
**Translation:** 

**[3452.62s] English:** To the Engineering of Intelligence.  
**Translation:** 

**[3454.84s] English:** And recognizing handwritten digits is not necessarily helpful; it might be useful, but it may not be.  
**Translation:** Vocabulary: digits: 阿拉伯数字; handwritten: 手写

**[3462.80s] English:** You, with the problem of general intelligence.  
**Translation:** 

**[3466.60s] English:** We don't know.  
**Translation:** 

**[3467.60s] English:** It'll help you a little bit.  
**Translation:** 

**[3468.60s] English:** We don't know how much.  
**Translation:** 

**[3469.60s] English:** It's unclear.  
**Translation:** 

**[3470.60s] English:** It's unclear.  
**Translation:** 

**[3471.60s] English:** Yeah.  
**Translation:** 

**[3472.60s] English:** It might be very much.  
**Translation:** 

**[3473.60s] English:** But I would like to make a remark.  
**Translation:** 

**[3474.60s] English:** Yes.  
**Translation:** Vocabulary: remark: 评论

**[3475.60s] English:** I do not start with a very primitive problem.  
**Translation:** 

**[3476.60s] English:** Yeah.  
**Translation:** 

**[3477.60s] English:** Yeah.  
**Translation:** 

**[3478.54s] English:** That's what I think.  
**Translation:** 

**[3479.54s] English:** Yeah.  
**Translation:** 

**[3480.00s] English:** Challenge problem: I start with a very general problem with Plato, so you understand, and it  
**Translation:** 

**[3480.54s] English:** And the scale that helps one stand in it.  
**Translation:** 

**[3481.54s] English:** Yeah.  
**Translation:** 

**[3482.54s] English:** Yeah.  
**Translation:** 

**[3483.54s] English:** Although, you might notice, you know, like, when you go through the lab, don't recognize  
**Translation:** 

**[3484.54s] English:** That tells you that you go in and take a 麵, and you don't have to.  
**Translation:** 

**[3485.54s] English:** Do anything else?  
**Translation:** 

**[3486.54s] English:** Yeah.  
**Translation:** 

**[3487.54s] English:** You can't just be one step away from doing it; you have to actually do it, or you just become like this, you know.  
**Translation:** 

**[3488.54s] English:** Really, reptile.  
**Translation:** 

**[3489.54s] English:** That's right.  
**Translation:** Vocabulary: reptile: 爬行动物

**[3489.62s] English:** Comes from Plato to digit recognition, so you basically took Plato and the world.  
**Translation:** 

**[3490.54s] English:** Cause you could mean other parts of it, and give a.  
**Translation:** Vocabulary: digit: 位数

**[3491.54s] English:** Yeah.  
**Translation:** 

**[3492.54s] English:** Yeah.  
**Translation:** 

**[3493.54s] English:** It's entirely up to the person on this term of politics, and yeah, that makes sense.  
**Translation:** 

**[3494.54s] English:** Yeah.  
**Translation:** 

**[3495.54s] English:** Praise, thank you very much.  
**Translation:** 

**[3496.54s] English:** So, today, you've done a fine job.  
**Translation:** 

**[3497.54s] English:** Thank you.  
**Translation:** 

**[3498.00s] English:** Of forms and ideas, and mapped and projected into the clearest, simplest formulation of that big world.  
**Translation:** Vocabulary: projected: 投射

**[3498.54s] English:** Not a problem.  
**Translation:** 

**[3499.54s] English:** Thank you.  
**Translation:** 

**[3500.56s] English:** Thanks.  
**Translation:** 

**[3500.66s] English:** You're welcome.  
**Translation:** 

**[3501.54s] English:** Cheers.  
**Translation:** 

**[3506.22s] English:** You know, I would say that I did not understand Plato until quite recently and until I reconsidered.  
**Translation:** 

**[3517.10s] English:** Weak convergence, and then predicates—and then, oh, this is what Plato told us.  
**Translation:** 

**[3525.20s] English:** So, you linger on that, like why? How do you think about this world of ideas and the world of things?  
**Translation:** Vocabulary: convergence: 趋近; linger: 逗留; predicates: 谓词

**[3531.12s] English:** Plato, no, it is a metaphor. It is, for sure, a metaphor, yeah.  
**Translation:** 

**[3536.10s] English:** Completely  
**Translation:** Vocabulary: metaphor: 比喻

**[3536.22s] English:** Compelling, it's a poetic and beautiful yeah, but what can you do? It is a way.  
**Translation:** 

**[3541.46s] English:** Half of you should try to understand how attacks work in the world.  
**Translation:** Vocabulary: compelling: 有说服力的; poetic: 诗意的

**[3547.04s] English:** So, from my point of view, it is very clear, but it is lying all the time.  
**Translation:** 

**[3555.46s] English:** People looking for that say, "Plato's and Hegel; whatever is reasonable exists.  
**Translation:** Vocabulary: hegel: 黑格尔

**[3564.22s] English:** Whatever existed was reasonable, I don't know what he had in mind.  
**Translation:** 

**[3569.34s] English:** Right, this isn't about the philosophers again. No, no, no, no, no; it is the next stop for Wigner.  
**Translation:** 

**[3576.30s] English:** That mathematics helps us understand something of reality, it is the same as plotting and aligning data.  
**Translation:** 

**[3582.72s] English:** Then it comes suddenly to Vladimir, probing "Look, 31 Ideas, 31 Units," and describes.  
**Translation:** Vocabulary: aligning: 对齐; plotting: 绘图; probing: 探究

**[3592.12s] English:** Everything.  
**Translation:** 

**[3594.22s] English:** There are abstractions and ideas that represent our world.  
**Translation:** Vocabulary: abstractions: 抽象概念

**[3600.00s] English:** And we should always try to reach for that.  
**Translation:** 

**[3603.44s] English:** Yeah, but you should make a projection of reality.  
**Translation:** Vocabulary: projection: 预测

**[3607.56s] English:** But understanding involves abstract ideas.  
**Translation:** 

**[3611.72s] English:** You have, in your mind, several abstract ideas which you can apply to reality.  
**Translation:** 

**[3617.76s] English:** And reality in this case, so if we look at machine learning, is data.  
**Translation:** 

**[3621.30s] English:** This example is data.  
**Translation:** 

**[3622.64s] English:** Data.  
**Translation:** 

**[3623.74s] English:** Okay, let me put this on you, because I'm an emotional creature.  
**Translation:** 

**[3628.14s] English:** I'm not a mathematical creature.  
**Translation:** 

**[3629.78s] English:** You're just like you.  
**Translation:** 

**[3630.66s] English:** I find the idea compelling, forget the space; the sea of functions.  
**Translation:** 

**[3636.36s] English:** There's also a sea of data in the world.  
**Translation:** Vocabulary: compelling: 有吸引力的

**[3639.42s] English:** And I find it compelling that there might be, as you said, teacher,  
**Translation:** 

**[3644.58s] English:** Small examples of data that are most useful for discovering good,  
**Translation:** 

**[3652.76s] English:** Whether it's predicates or good functions,  
**Translation:** 

**[3655.06s] English:** That the selection of data may be a powerful journey.  
**Translation:** Vocabulary: predicates: 谓词

**[3659.78s] English:** A useful mechanism, you know, coming up with a mechanism,...  
**Translation:** 

**[3663.72s] English:** For selecting good data might be useful, too.  
**Translation:** Vocabulary: selecting: 挑选

**[3667.46s] English:** Do you find this idea of finding the right data set interesting at all?  
**Translation:** 

**[3673.96s] English:** Do you kind of take the data set as a given?  
**Translation:** 

**[3677.70s] English:** I think that it is, you know, my scheme is very simple.  
**Translation:** 

**[3682.64s] English:** You have a huge set of functions.  
**Translation:** 

**[3686.26s] English:** If you will apply, and you have not,  
**Translation:** 

**[3689.78s] English:** Too many data.  
**Translation:** 

**[3690.78s] English:** Right.  
**Translation:** 

**[3691.78s] English:** If you will pick up the function, which describes this data,  
**Translation:** 

**[3697.48s] English:** You will not do very well.  
**Translation:** 

**[3701.14s] English:** Like, randomly pick it up.  
**Translation:** 

**[3702.14s] English:** Yeah, you'll overfit here.  
**Translation:** 

**[3704.14s] English:** It will be overfitting.  
**Translation:** Vocabulary: overfit: 模型过拟合; overfitting: 过拟合现象

**[3706.34s] English:** So, you should decrease the set of functions from which you're picking one.  
**Translation:** 

**[3713.60s] English:** So, you should go somehow to the admissible set of functions.  
**Translation:** Vocabulary: admissible: 允许的

**[3717.88s] English:** And this.  
**Translation:** 

**[3720.00s] English:** What about weak convergence?  
**Translation:** Vocabulary: convergence: 趋近

**[3721.98s] English:** So, but  
**Translation:** 

**[3724.24s] English:** From another point of view,  
**Translation:** 

**[3726.94s] English:** To  
**Translation:** 

**[3728.22s] English:** To make  
**Translation:** 

**[3729.42s] English:** Admissible Set of Functions  
**Translation:** 

**[3732.50s] English:** You need just a D.  
**Translation:** 

**[3734.16s] English:** Just function, which you will,  
**Translation:** 

**[3735.94s] English:** Take the inner product.  
**Translation:** 

**[3738.66s] English:** Which you will  
**Translation:** 

**[3740.56s] English:** Measure.  
**Translation:** 

**[3741.06s] English:** Property of your function.  
**Translation:** 

**[3744.28s] English:** And  
**Translation:** 

**[3747.76s] English:** That is how it works.  
**Translation:** 

**[3750.80s] English:** No, I get it. I understand it.  
**Translation:** 

**[3752.66s] English:** But, do you?  
**Translation:** 

**[3753.36s] English:** The reality is  
**Translation:** 

**[3754.90s] English:** Let's think about  
**Translation:** 

**[3757.24s] English:** Examples:  
**Translation:** 

**[3758.56s] English:** You have a huge set of functions.  
**Translation:** 

**[3761.46s] English:** And you have several examples.  
**Translation:** 

**[3763.70s] English:** If you  
**Translation:** 

**[3765.10s] English:** Just trying to  
**Translation:** 

**[3767.46s] English:** Take a function.  
**Translation:** 

**[3769.70s] English:** Which satisfies these examples?  
**Translation:** 

**[3772.00s] English:** You still  
**Translation:** 

**[3774.20s] English:** Will overfeed.  
**Translation:** 

**[3775.34s] English:** You need to decrease.  
**Translation:** 

**[3777.34s] English:** You need  
**Translation:** 

**[3777.74s] English:** You need to decrease.  
**Translation:** 

**[3777.76s] English:** Admissible Set of Functions  
**Translation:** 

**[3779.20s] English:** Absolutely.  
**Translation:** 

**[3780.16s] English:** But what?  
**Translation:** 

**[3781.52s] English:** Say, you have  
**Translation:** 

**[3783.26s] English:** More data than functions.  
**Translation:** 

**[3786.14s] English:** So,  
**Translation:** 

**[3787.02s] English:** Sort of consider the.  
**Translation:** 

**[3787.90s] English:** I mean, maybe not more data than functions.  
**Translation:** 

**[3789.80s] English:** Because that's  
**Translation:** 

**[3790.64s] English:** Impossible.  
**Translation:** 

**[3791.48s] English:** Impossible.  
**Translation:** 

**[3792.06s] English:** But what?  
**Translation:** 

**[3793.26s] English:** I was trying to be poetic for a second.  
**Translation:** Vocabulary: poetic: 诗意的

**[3795.16s] English:** I mean, you have a huge amount of data.  
**Translation:** 

**[3797.22s] English:** A huge amount of examples.  
**Translation:** 

**[3799.88s] English:** But amount of function.  
**Translation:** 

**[3801.72s] English:** Can be even  
**Translation:** 

**[3802.56s] English:** Bigger, I understand.  
**Translation:** 

**[3804.36s] English:** Everything is  
**Translation:** 

**[3805.56s] English:** There's always  
**Translation:** 

**[3806.44s] English:** There's always a bigger boat.  
**Translation:** 

**[3807.74s] English:** In the entire Hilbert space  
**Translation:** 

**[3808.74s] English:** I got you.  
**Translation:** 

**[3809.74s] English:** But, okay.  
**Translation:** 

**[3810.74s] English:** But you don't.  
**Translation:** 

**[3813.74s] English:** You don't find  
**Translation:** 

**[3814.74s] English:** The world of data.  
**Translation:** 

**[3815.74s] English:** To be an interesting person,  
**Translation:** 

**[3817.74s] English:** Optimization Space  
**Translation:** 

**[3818.74s] English:** Like the  
**Translation:** 

**[3819.74s] English:** The optimization  
**Translation:** Vocabulary: optimization: 优化

**[3820.74s] English:** Should be in the space of functions.  
**Translation:** 

**[3821.74s] English:** Creating an admissible set of functions.  
**Translation:** Vocabulary: admissible: 可接受的函数集

**[3826.74s] English:** Admissible Set of Functions  
**Translation:** 

**[3827.74s] English:** No.  
**Translation:** 

**[3828.74s] English:** You know,  
**Translation:** 

**[3829.74s] English:** Even from the  
**Translation:** 

**[3830.74s] English:** Classical Basis Theory  
**Translation:** 

**[3831.74s] English:** From structure risk minimization.  
**Translation:** Vocabulary: minimization: 最小化

**[3835.74s] English:** You should  
**Translation:** 

**[3836.74s] English:** You should  
**Translation:** 

**[3837.72s] English:** Organize  
**Translation:** 

**[3839.72s] English:** Functionality  
**Translation:** Vocabulary: functionality: 功能

**[3840.00s] English:** In the way that they will be useful for you.  
**Translation:** 

**[3840.72s] English:** Is  
**Translation:** 

**[3842.68s] English:** It  
**Translation:** 

**[3843.72s] English:** Transforming  
**Translation:** 

**[3844.72s] English:** Each  
**Translation:** 

**[3845.72s] English:** Every  
**Translation:** 

**[3846.42s] English:** Right.  
**Translation:** 

**[3846.72s] English:** Every  
**Translation:** 

**[3847.46s] English:** And that is admissible.  
**Translation:** 

**[3847.72s] English:** Each  
**Translation:** 

**[3848.72s] English:** Every  
**Translation:** 

**[3849.72s] English:** Million  
**Translation:** 

**[3849.74s] English:** The way you're thinking about usefulness is that you're given a small set of examples.  
**Translation:** 

**[3850.72s] English:** Million  
**Translation:** 

**[3851.72s] English:** Block.  
**Translation:** 

**[3852.72s] English:** Approaches:  
**Translation:** Vocabulary: approaches: 方法

**[3853.72s] English:** Among  
**Translation:** 

**[3854.72s] English:** All  
**Translation:** 

**[3856.72s] English:** That  
**Translation:** 

**[3857.00s] English:** Useful is small.  
**Translation:** 

**[3857.62s] English:** A small set of functions which contains the ones I'm looking for.  
**Translation:** 

**[3857.72s] English:** And  
**Translation:** 

**[3858.72s] English:** Awesome!  
**Translation:** 

**[3859.72s] English:** Biri.  
**Translation:** 

**[3860.72s] English:** A  
**Translation:** 

**[3861.72s] English:** C:  
**Translation:** 

**[3861.76s] English:** Yeah, but looking for something based on an empirical set of small examples.  
**Translation:** 

**[3863.72s] English:** In  
**Translation:** Vocabulary: empirical: 基于事实的

**[3864.72s] English:** Everything.  
**Translation:** 

**[3865.72s] English:** Beautiful.  
**Translation:** 

**[3867.60s] English:** Yeah.  
**Translation:** 

**[3868.08s] English:** But that is another story.  
**Translation:** 

**[3869.50s] English:** I don't touch it because I believe that these small examples are not too small.  
**Translation:** 

**[3877.36s] English:** Say 60 per class, the law of large numbers works.  
**Translation:** 

**[3881.24s] English:** I don't need uniform law.  
**Translation:** 

**[3883.42s] English:** The story is that in statistics, there are two laws: the Law of Large Numbers and the Uniform Law of Large Numbers.  
**Translation:** 

**[3890.76s] English:** So, I want to be in a situation where I use the law of large numbers, but not the uniform law of large numbers.  
**Translation:** 

**[3898.08s] English:** Right.  
**Translation:** 

**[3898.64s] English:** So, 60 is...  
**Translation:** 

**[3899.50s] English:** It's large enough.  
**Translation:** 

**[3901.34s] English:** I hope; no.  
**Translation:** 

**[3902.36s] English:** It still needs some evaluation, some balance.  
**Translation:** Vocabulary: evaluation: 评估

**[3906.50s] English:** But the idea is as follows: that if you trust that, say, this average gives you something close to the expectation,  
**Translation:** 

**[3921.08s] English:** So, you can talk about that, about this predicate.  
**Translation:** Vocabulary: expectation: 预期; predicate: 谓词

**[3926.22s] English:** And that is the basis of human intelligence.  
**Translation:** 

**[3929.50s] English:** Good predicates are the...  
**Translation:** Vocabulary: predicates: 谓词

**[3932.10s] English:** The discovery of good predicates is the basis of human intelligence.  
**Translation:** 

**[3934.50s] English:** No, no.  
**Translation:** 

**[3934.82s] English:** It is the discovery of your understanding of the world, of your methodology of understanding it.  
**Translation:** 

**[3944.88s] English:** Because you have several functions that you will apply to reality.  
**Translation:** Vocabulary: methodology: 研究方法

**[3950.96s] English:** Can you say that again?  
**Translation:** 

**[3952.60s] English:** So, you're...  
**Translation:** 

**[3954.30s] English:** You have several functions.  
**Translation:** 

**[3956.16s] English:** Yeah.  
**Translation:** 

**[3956.78s] English:** Predicate.  
**Translation:** 

**[3958.30s] English:** But they abstract.  
**Translation:** 

**[3959.50s] English:** They abstract.  
**Translation:** 

**[3960.00s] English:** Yes.  
**Translation:** 

**[3961.00s] English:** Then you will apply them to reality, to your data, and you will create predicates in this way.  
**Translation:** 

**[3967.46s] English:** Which is useful for your task.  
**Translation:** 

**[3971.64s] English:** But predicates are not specifically related to your task for this task.  
**Translation:** 

**[3977.90s] English:** It is abstract functions which are being applied to-  
**Translation:** 

**[3983.18s] English:** Many tasks that you might be interested in.  
**Translation:** 

**[3985.18s] English:** It might be many tasks, I don't know.  
**Translation:** 

**[3989.00s] English:** Different tasks.  
**Translation:** 

**[3990.00s] English:** So there should be many tasks, right?  
**Translation:** 

**[3991.56s] English:** Yeah.  
**Translation:** 

**[3992.56s] English:** I believe, like in a property case, it was for fairy tales, but it's happened everywhere.  
**Translation:** 

**[3999.24s] English:** Okay.  
**Translation:** 

**[4000.52s] English:** So, we talked about images a little bit, but can we talk about Noam Chomsky for a second?  
**Translation:** Vocabulary: chomsky: 乔姆斯基

**[4007.88s] English:** I believe I don't know him very well.  
**Translation:** 

**[4014.24s] English:** Personally, well,  
**Translation:** 

**[4015.24s] English:** Not personally, I don't know.  
**Translation:** 

**[4017.00s] English:** His ideas.  
**Translation:** 

**[4018.00s] English:** His ideas.  
**Translation:** 

**[4019.00s] English:** Well, let me just say.  
**Translation:** 

**[4020.00s] English:** Do you think language, human language, is essential to expressing ideas, as Noam Chomsky?  
**Translation:** 

**[4026.72s] English:** Believes?  
**Translation:** 

**[4027.72s] English:** So, like, language is at the core of how we form predicates in human language.  
**Translation:** 

**[4034.96s] English:** For me, language and all the story of language is very complicated.  
**Translation:** Vocabulary: predicates: 谓词

**[4040.70s] English:** I don't understand this, and I'm not sure why. I thought about it for a while...  
**Translation:** 

**[4044.80s] English:** Nobody does.  
**Translation:** 

**[4045.80s] English:** I'm not ready to work on that because it's so huge.  
**Translation:** 

**[4046.52s] English:** Yeah.  
**Translation:** 

**[4047.52s] English:** Yeah.  
**Translation:** 

**[4048.52s] English:** Yeah.  
**Translation:** 

**[4049.52s] English:** It's so huge.  
**Translation:** 

**[4050.84s] English:** It is not for me, and I believe not for our century.  
**Translation:** 

**[4054.76s] English:** The 21st century.  
**Translation:** 

**[4057.46s] English:** Not for the 21st century.  
**Translation:** 

**[4059.46s] English:** You should learn something—lots of stuff—from a simple task like digital recognition.  
**Translation:** 

**[4065.24s] English:** So, you think digital recognition is just about 2D images? How would you more abstractly define it?  
**Translation:** Vocabulary: abstractly: 抽象地

**[4074.24s] English:** Digital recognition?  
**Translation:** 

**[4077.24s] English:** It's a 2D image.  
**Translation:** 

**[4079.24s] English:** It's a 2D image.  
**Translation:** 

**[4080.00s] English:** Recognition, essentially, I mean—I'm trying to get a sense of it and thinking about it now.  
**Translation:** 

**[4089.24s] English:** Having worked with MNIST for forever, how small of a subset is this in general?  
**Translation:** 

**[4096.64s] English:** Vision recognition problem and the general intelligence problem: is it  
**Translation:** 

**[4101.98s] English:** Because, yeah, is it a giant subset? Is it not? And how far away is language, you know? Let me refer to...  
**Translation:** 

**[4112.60s] English:** Einstein took the simplest problem as simple as possible, but not simpler, and this is a challenge.  
**Translation:** Vocabulary: einstein: 爱因斯坦

**[4121.14s] English:** It is a simple problem, but it's simple in idea, but not simple to get right when you will.  
**Translation:** 

**[4130.86s] English:** When will you get it?  
**Translation:** 

**[4131.96s] English:** Do this, and you will find some predicate which helps you to do well. Yeah, I mean, with that.  
**Translation:** 

**[4138.14s] English:** With Einstein, you can look at general relativity, but that doesn't help you with  
**Translation:** Vocabulary: predicate: 谓词; relativity: 相对论

**[4145.08s] English:** Quantum mechanics—that's another story. You don't have any universal instrument, yes? So, I'm trying.  
**Translation:** 

**[4152.84s] English:** To wonder if, uh, which space we're in—whether the handwritten recognition is like  
**Translation:** Vocabulary: handwritten: 手写; quantum: 量子

**[4159.46s] English:** General Relativity, and then language.  
**Translation:** 

**[4161.94s] English:** Is like quantum mechanics, so you're still going to have to do a lot of messy work to universalize it, but...  
**Translation:** Vocabulary: universalize: 使普遍适用

**[4168.74s] English:** Uh, I'm trying to see one. So, what's your intuition why handwritten recognition is easier than language?  
**Translation:** 

**[4181.86s] English:** Just, I think a lot of people would agree with that, but if you could elucidate the intuition a bit more, that would be great.  
**Translation:** Vocabulary: elucidate: 阐述; intuition: 直觉

**[4188.66s] English:** Of why  
**Translation:** 

**[4191.94s] English:** You don't know, you know? I don't think in this direction; I'm just thinking in different directions that this.  
**Translation:** 

**[4198.66s] English:** Is the problem?  
**Translation:** 

**[4200.00s] English:** Which, if we solve it well, we will create some abstract understanding of images.  
**Translation:** 

**[4217.38s] English:** Maybe, not all images.  
**Translation:** 

**[4219.58s] English:** I would like to talk to guys who are doing Unreal Images at Columbia University.  
**Translation:** Vocabulary: columbia: 哥伦比亚大学

**[4225.78s] English:** What kind of images? Unreal?  
**Translation:** 

**[4227.58s] English:** Real images. What they already predict, what can be predicted.  
**Translation:** 

**[4234.70s] English:** Symmetry will play a role in real-life images, in any real-life images, 2D images, let's talk about 2D images.  
**Translation:** 

**[4245.58s] English:** Because that's what we know.  
**Translation:** Vocabulary: symmetry: 对称

**[4251.58s] English:** The neural network was created for 2D images.  
**Translation:** 

**[4255.58s] English:** So, the people I know in the  
**Translation:** Vocabulary: neural: 神经网络

**[4257.56s] English:** Vision science, for example, is the field where people study human vision; they usually go  
**Translation:** 

**[4262.44s] English:** To the world of symbols, and something like handwritten recognition, but not really.  
**Translation:** Vocabulary: handwritten: 手写

**[4266.90s] English:** It's other kinds of symbols to study our visual perception system. As far as I know,  
**Translation:** 

**[4272.02s] English:** Know, not much predicate-type thinking is understood about our vision system.  
**Translation:** 

**[4276.94s] English:** They did not think in this direction.  
**Translation:** 

**[4279.36s] English:** They don't, yeah. But how do you even begin to think in that direction?  
**Translation:** 

**[4282.94s] English:** That's what I would like to discuss with them.  
**Translation:** 

**[4286.78s] English:** Yeah.  
**Translation:** 

**[4287.56s] English:** Because if we can show that it is what's working and the theoretical scheme,  
**Translation:** 

**[4298.62s] English:** It's not so bad.  
**Translation:** 

**[4300.40s] English:** So, the unfortunate thing is, if we compare it to language, language has a finite set of letters.  
**Translation:** 

**[4306.48s] English:** And there are a finite set of ways you can put together those letters. So it feels more amenable to  
**Translation:** Vocabulary: amenable: 易于处理的; finite: 有限的

**[4311.94s] English:** Kind of analysis. With natural images, there are so many pixels.  
**Translation:** 

**[4317.40s] English:** No, no, no. Letter.  
**Translation:** Vocabulary: pixels: 像素

**[4320.00s] English:** Language is much, much more complicated.  
**Translation:** 

**[4323.66s] English:** It involves a lot of different stuff.  
**Translation:** 

**[4327.98s] English:** It's not just an understanding of very simple classes of tasks.  
**Translation:** 

**[4334.94s] English:** I would like to see a list of tasks where language is involved.  
**Translation:** 

**[4339.68s] English:** Yes, so there are lots of nice benchmarks now in natural language processing.  
**Translation:** 

**[4344.32s] English:** From the very trivial, like understanding the elements of a sentence,  
**Translation:** Vocabulary: benchmarks: 参考标准; trivial: 琐碎的

**[4350.16s] English:** To question-answering, to much more complicated,  
**Translation:** 

**[4353.02s] English:** Where you talk about open-domain dialogue.  
**Translation:** 

**[4356.00s] English:** The natural question is: with handwritten recognition,  
**Translation:** 

**[4359.14s] English:** It's really the first step in understanding visual information.  
**Translation:** 

**[4364.52s] English:** Right.  
**Translation:** 

**[4367.66s] English:** But, even according to our records, we're going in the wrong direction.  
**Translation:** 

**[4373.38s] English:** Because we need 60,000 digits.  
**Translation:** 

**[4376.66s] English:** So, even this first step.  
**Translation:** Vocabulary: digits: 位数

**[4378.50s] English:** So, forget about talking about the first.  
**Translation:** 

**[4380.00s] English:** This first step should be taken in the right direction.  
**Translation:** 

**[4383.16s] English:** No, no, it's in the wrong direction because 60,000 is unacceptable.  
**Translation:** 

**[4387.14s] English:** No, I'm saying it should be taken in the right direction.  
**Translation:** Vocabulary: unacceptable: 不能接受

**[4390.76s] English:** Because $60,000 is not acceptable.  
**Translation:** 

**[4393.60s] English:** You can talk; it's great. We have a half percent of error.  
**Translation:** 

**[4398.38s] English:** And hopefully, the step from doing hand recognition using very few examples,  
**Translation:** 

**[4404.58s] English:** The step toward what babies do when they crawl.  
**Translation:** 

**[4407.46s] English:** And understand their physical environment.  
**Translation:** 

**[4409.12s] English:** I don't know what babies do.  
**Translation:** 

**[4410.00s] English:** I know you don't know about babies.  
**Translation:** 

**[4411.44s] English:** If you start with very small examples,  
**Translation:** 

**[4415.24s] English:** You will find principles that are different from what we're using now.  
**Translation:** 

**[4424.78s] English:** And theoretically, it's more or less clear.  
**Translation:** Vocabulary: theoretically: 理论上

**[4428.26s] English:** That means that you will use weak convergence.  
**Translation:** 

**[4432.26s] English:** Not just strong convergence.  
**Translation:** Vocabulary: convergence: 收敛

**[4434.14s] English:** Do you think these principles will naturally be human?  
**Translation:** 

**[4439.78s] English:** In terms of the way they're used?  
**Translation:** 

**[4440.00s] English:** Interpretable.  
**Translation:** 

**[4441.58s] English:** Oh, yeah.  
**Translation:** Vocabulary: interpretable: 可解释的

**[4442.48s] English:** So, like, we'll be able to explain them and have a nice presentation to show what those principles are?  
**Translation:** 

**[4447.48s] English:** Or are they going to be very kind of abstract kinds of functions?  
**Translation:** 

**[4454.14s] English:** For example, I talked yesterday about symmetry.  
**Translation:** 

**[4457.54s] English:** Yes.  
**Translation:** Vocabulary: symmetry: 对称

**[4458.56s] English:** And I gave very simple examples.  
**Translation:** 

**[4460.42s] English:** The same will be.  
**Translation:** 

**[4461.50s] English:** You gave, like, a predicate of a basic definition for...  
**Translation:** 

**[4464.62s] English:** For symmetries.  
**Translation:** Vocabulary: predicate: 主谓; symmetries: 对称性

**[4465.72s] English:** Yes, for different symmetries, and you have....  
**Translation:** 

**[4468.20s] English:** For...  
**Translation:** 

**[4469.40s] English:** For degrees of symmetry.  
**Translation:** 

**[4470.54s] English:** That is important.  
**Translation:** 

**[4471.92s] English:** Not just symmetry.  
**Translation:** 

**[4473.62s] English:** Exist and doesn't exist.  
**Translation:** 

**[4475.16s] English:** Degree of Symmetry.  
**Translation:** 

**[4478.00s] English:** Yeah, for handwritten recognition.  
**Translation:** 

**[4480.94s] English:** No, it's not for handwritten.  
**Translation:** 

**[4482.92s] English:** It's for any images.  
**Translation:** 

**[4485.06s] English:** But I would like to apply for handwriting.  
**Translation:** 

**[4487.36s] English:** Right.  
**Translation:** Vocabulary: handwriting: 书写样本

**[4488.14s] English:** In theory, it's more general.  
**Translation:** 

**[4489.64s] English:** Okay.  
**Translation:** 

**[4490.36s] English:** Okay.  
**Translation:** 

**[4494.82s] English:** So, a lot of things we've been talking about fall...  
**Translation:** 

**[4499.40s] English:** We've been talking about philosophy a little bit, but also about mathematics and statistics.  
**Translation:** 

**[4505.10s] English:** A lot of it falls into this idea—a universal idea in statistical theory of learning.  
**Translation:** 

**[4511.38s] English:** What is the most beautiful and sort-of powerful or essential idea you've come across, even just for yourself personally, in the world of statistics or statistical learning theory?  
**Translation:** 

**[4525.18s] English:** Probably on uniform convergence, which we did.  
**Translation:** Vocabulary: convergence: 趋近

**[4529.40s] English:** Yes, Alexey Chervenenko.  
**Translation:** 

**[4532.46s] English:** Can you describe universal convergence?  
**Translation:** 

**[4535.70s] English:** You have the Law of Large Numbers.  
**Translation:** 

**[4540.00s] English:** So, for any function, the expectation of the function, the average of the function, converges to the expectation.  
**Translation:** Vocabulary: converges: 趋近; expectation: 期望值

**[4547.50s] English:** But if you have a set of functions, for any function in the set, it is true.  
**Translation:** 

**[4552.86s] English:** But it should converge simultaneously for all sets of functions.  
**Translation:** Vocabulary: converge: 趋于一致

**[4558.60s] English:** And,...  
**Translation:** 

**[4559.40s] English:** I don't know.  
**Translation:** 

**[4560.00s] English:** For learning, you need uniform convergence.  
**Translation:** 

**[4560.34s] English:** Yeah.  
**Translation:** 

**[4560.66s] English:** I just think it's a very good idea.  
**Translation:** 

**[4562.14s] English:** I think it's a great idea.  
**Translation:** 

**[4563.12s] English:** So, this is a very important topic.  
**Translation:** 

**[4564.22s] English:** I'm sure that the study can give us examples of the evolution of statistics and statistics—things that are more surprising to some of us.  
**Translation:** 

**[4566.74s] English:** Just convergence is not enough.  
**Translation:** 

**[4569.38s] English:** So, I'd like to express that I'm very proud of this project.  
**Translation:** 

**[4570.58s] English:** Because, when you pick up the one that gives the minimum,  
**Translation:** 

**[4572.48s] English:** It's been a great pleasure.  
**Translation:** 

**[4574.20s] English:** I appreciate it.  
**Translation:** 

**[4575.56s] English:** I think it's a very important topic.  
**Translation:** 

**[4576.58s] English:** You can pick up one function that does not converge.  
**Translation:** 

**[4576.90s] English:** And it's very useful.  
**Translation:** 

**[4579.02s] English:** So, have a great day!  
**Translation:** 

**[4579.44s] English:** Thank you.  
**Translation:** 

**[4579.56s] English:** Thank you.  
**Translation:** 

**[4580.24s] English:** Thank you.  
**Translation:** 

**[4580.70s] English:** Thank you.  
**Translation:** 

**[4580.88s] English:** Thank you.  
**Translation:** 

**[4581.00s] English:** Thank you.  
**Translation:** 

**[4581.54s] English:** Thank you.  
**Translation:** 

**[4581.68s] English:** Thank you.  
**Translation:** 

**[4582.12s] English:** And it will give you the best answer for this function.  
**Translation:** 

**[4582.46s] English:** Thank you.  
**Translation:** 

**[4582.60s] English:** Thank you.  
**Translation:** 

**[4582.76s] English:** Thank you, Alexey Chervenko.  
**Translation:** 

**[4583.82s] English:** Thank you.  
**Translation:** 

**[4584.42s] English:** Thank you.  
**Translation:** 

**[4584.92s] English:** Thank you.  
**Translation:** 

**[4586.74s] English:** Thank you.  
**Translation:** 

**[4587.38s] English:** Thank you.  
**Translation:** 

**[4590.00s] English:** So, you need uniform convergence to guarantee learning.  
**Translation:** 

**[4594.94s] English:** So, learning does not rely on trivially large numbers.  
**Translation:** Vocabulary: trivially: 琐碎地

**[4600.48s] English:** It relies on the universal.  
**Translation:** 

**[4602.86s] English:** But the idea of convergence exists in statistics for a long time.  
**Translation:** 

**[4613.50s] English:** But it is interesting that,  
**Translation:** 

**[4618.88s] English:** As I...  
**Translation:** 

**[4620.00s] English:** I think about myself.  
**Translation:** 

**[4622.12s] English:** How stupid I was in my fifties.  
**Translation:** 

**[4625.22s] English:** I did not see weak convergence.  
**Translation:** 

**[4628.02s] English:** I work only on strong convergence.  
**Translation:** Vocabulary: convergence: 收敛

**[4630.84s] English:** But now I think that most powerful is weak convergence.  
**Translation:** 

**[4634.96s] English:** Because it makes an admissible set of functions.  
**Translation:** Vocabulary: admissible: 可接受的

**[4638.44s] English:** And even in all products,  
**Translation:** 

**[4642.62s] English:** When people try to understand recognition of dog laws,  
**Translation:** 

**[4648.08s] English:** It looks like a dog, and so on.  
**Translation:** 

**[4650.00s] English:** They use weak convergence.  
**Translation:** 

**[4652.30s] English:** People in the language, they understand this.  
**Translation:** 

**[4655.66s] English:** But when we're trying to create artificial intelligence,  
**Translation:** 

**[4662.02s] English:** We won't be inventing a different way.  
**Translation:** 

**[4666.06s] English:** We just consider strong convergence.  
**Translation:** 

**[4670.16s] English:** So, reducing the set of admissible functions,  
**Translation:** 

**[4673.02s] English:** You think there should be an effort put into understanding?  
**Translation:** 

**[4679.04s] English:** Properties of  
**Translation:** 

**[4680.00s] English:** Weak convergence, you know, in classical mathematics in a finite-dimensional space, there are only two ways to form.  
**Translation:** 

**[4689.84s] English:** Of convergence, strong and weak: now, we can use both. That means that we did everything, and  
**Translation:** 

**[4701.36s] English:** It so happened that when we used Hilbert space, which is a very rich space of continuous functions,  
**Translation:** Vocabulary: hilbert: 希尔伯特空间

**[4711.06s] English:** Functions, which have an integral and square, so we can apply weak and strong convergence for.  
**Translation:** 

**[4721.06s] English:** Learning has a closed-form solution, so it is computationally simple for me; it is signed.  
**Translation:** Vocabulary: computationally: 计算上; convergence: 收敛; integral: 积分

**[4728.90s] English:** That is the right way.  
**Translation:** 

**[4731.36s] English:** Because you don't need anything realistic; you just know whatever you want.  
**Translation:** 

**[4737.50s] English:** But now, the only thing left is the concept of what is a predicate of a predicate, but it is not.  
**Translation:** 

**[4746.64s] English:** Statistics, by the way, I like the fact that you think the heuristics are a mess that should be  
**Translation:** Vocabulary: heuristics: 启发式; predicate: 谓词

**[4752.70s] English:** Removed from the system, so a closed-form solution is ultimately the way to go. It so happened, then, when you're  
**Translation:** 

**[4760.32s] English:** Using  
**Translation:** 

**[4760.70s] English:** You know,  
**Translation:** 

**[4761.34s] English:** You know, you're using.  
**Translation:** 

**[4761.36s] English:** Right; instrument, you have a closed-form solution.  
**Translation:** 

**[4766.84s] English:** Do you think human-level intelligence, when we create it, will have  
**Translation:** 

**[4779.00s] English:** Something like a closed-form solution?  
**Translation:** 

**[4781.52s] English:** You know, now I'm looking at the bounds, which I gave for convergence, and when I'm  
**Translation:** Vocabulary: bounds: 范围

**[4791.84s] English:** Looking for bounds, I'm thinking: What is the most appropriate kernel for this bound?  
**Translation:** 

**[4800.00s] English:** Bound would be. So, we know that in all our businesses, we use a radial basis function.  
**Translation:** Vocabulary: kernel: 核函数; radial: 径向的

**[4811.68s] English:** But looking onward, I think that I begin to understand that maybe we need to make corrections.  
**Translation:** 

**[4818.76s] English:** To use a radial basis function to be closer and work better for these bounds, so I'm again  
**Translation:** Vocabulary: corrections: 修正; onward: 向前

**[4829.54s] English:** Trying to understand what type of kernel has the best approximation, non-approximation properties.  
**Translation:** 

**[4839.92s] English:** Fit to this bond.  
**Translation:** Vocabulary: approximation: 近似

**[4842.78s] English:** Sure. So, there's a lot of interesting work that could be done in discovering better  
**Translation:** 

**[4847.20s] English:** Functions and radial basis functions for the kinds of bounds you find.  
**Translation:** 

**[4852.30s] English:** Yeah, but it still comes from... You're looking to mass-produce and trying to understand.  
**Translation:** 

**[4859.30s] English:** What...?  
**Translation:** 

**[4859.54s] English:** From your own mind, looking at the ... I don't know.  
**Translation:** 

**[4862.30s] English:** Yeah, but then I'm trying to understand what will be good for that.  
**Translation:** 

**[4870.78s] English:** Yeah, but to me, there's still a beauty. Again, maybe I'm a descendant of Alan Turing.  
**Translation:** 

**[4876.30s] English:** To heuristics. To me, ultimately, intelligence will be a mess of heuristics. And that's the way it should be.  
**Translation:** Vocabulary: descendant: 后裔; heuristics: 启发式; turing: 图灵

**[4885.04s] English:** Engineering answer, I guess.  
**Translation:** 

**[4887.30s] English:** No, absolutely.  
**Translation:** 

**[4889.30s] English:** Self-driving cars—there's a great guy who will do that. It doesn't matter what theory.  
**Translation:** 

**[4897.70s] English:** Behind that, who has a better feeling has to apply it. But by the way, it is the same.  
**Translation:** 

**[4908.16s] English:** A story about predicates, because you cannot create a rule for... Citation is much more than you.  
**Translation:** 

**[4915.58s] English:** We have a rule for that.  
**Translation:** Vocabulary: cannot: 不能; citation: 引用; predicates: 谓词

**[4917.06s] English:** Yeah.  
**Translation:** 

**[4918.06s] English:** Yeah.  
**Translation:** 

**[4919.06s] English:** Yeah.  
**Translation:** 

**[4920.00s] English:** Maybe you can have a more abstract rule, then it will be less literal.  
**Translation:** Vocabulary: literal: 字面的

**[4920.06s] English:** Yeah.  
**Translation:** 

**[4921.06s] English:** Yeah.  
**Translation:** 

**[4922.06s] English:** Yeah.  
**Translation:** 

**[4923.06s] English:** Yeah.  
**Translation:** 

**[4924.06s] English:** Yeah.  
**Translation:** 

**[4925.06s] English:** Yeah.  
**Translation:** 

**[4926.06s] English:** Yeah.  
**Translation:** 

**[4927.06s] English:** Yeah.  
**Translation:** 

**[4928.06s] English:** Yeah.  
**Translation:** 

**[4928.82s] English:** It is the same story about ideas, and ideas applied to specific cases.  
**Translation:** 

**[4929.06s] English:** Yeah.  
**Translation:** 

**[4930.06s] English:** Yeah.  
**Translation:** 

**[4931.06s] English:** Yeah.  
**Translation:** 

**[4932.06s] English:** Yeah.  
**Translation:** 

**[4933.06s] English:** Yeah.  
**Translation:** 

**[4934.06s] English:** Yeah.  
**Translation:** 

**[4934.80s] English:** But still, you should reach out.  
**Translation:** 

**[4935.06s] English:** Yeah.  
**Translation:** 

**[4936.06s] English:** Yeah.  
**Translation:** 

**[4937.06s] English:** Yeah.  
**Translation:** 

**[4937.30s] English:** You cannot avoid this.  
**Translation:** 

**[4938.06s] English:** Yeah.  
**Translation:** 

**[4938.62s] English:** Yes, of course, but you should still reach for the ideas to understand the science.  
**Translation:** 

**[4939.06s] English:** Yeah.  
**Translation:** 

**[4940.06s] English:** Yeah.  
**Translation:** 

**[4941.06s] English:** Yeah.  
**Translation:** 

**[4942.06s] English:** Yeah.  
**Translation:** 

**[4942.76s] English:** Yeah.  
**Translation:** 

**[4943.06s] English:** Yeah.  
**Translation:** 

**[4943.76s] English:** Let me ask: Do you think neural networks or functions can be made to reason?  
**Translation:** Vocabulary: neural: 神经的

**[4944.06s] English:** Yeah.  
**Translation:** 

**[4945.06s] English:** Yeah.  
**Translation:** 

**[4946.06s] English:** Yeah.  
**Translation:** 

**[4947.06s] English:** Yeah.  
**Translation:** 

**[4948.06s] English:** Yeah.  
**Translation:** 

**[4954.62s] English:** What do you think?  
**Translation:** 

**[4955.62s] English:** We've been talking about intelligence, but this idea of reasoning has an element  
**Translation:** 

**[4961.26s] English:** Of sequentially disassembling and interpreting the images.  
**Translation:** Vocabulary: disassembling: 拆解; interpreting: 解释; sequentially: 依次

**[4969.22s] English:** When you think of handwritten recognition,  
**Translation:** 

**[4973.52s] English:** We kind of think that there will be a single system with an input and an output.  
**Translation:** Vocabulary: handwritten: 手写

**[4977.06s] English:** There's no recurrence.  
**Translation:** 

**[4978.76s] English:** Yeah.  
**Translation:** Vocabulary: recurrence: 重复

**[4979.76s] English:** What do you think about the idea of recurrence — of going back to memory and thinking?  
**Translation:** 

**[4986.40s] English:** Through this sort of sequential mashing up of the different representations over and over.  
**Translation:** Vocabulary: mashing: 混合; representations: 表现形式; sequential: 顺序的

**[4994.02s] English:** Until you arrive at a conclusion?  
**Translation:** 

**[5000.18s] English:** Or is ultimately all that can be wrapped up into a function?  
**Translation:** 

**[5003.02s] English:** No.  
**Translation:** 

**[5003.52s] English:** You're suggesting that we use this type of algorithm.  
**Translation:** Vocabulary: algorithm: 算法

**[5009.76s] English:** When I start thinking, I first of all begin to understand what I want.  
**Translation:** 

**[5016.48s] English:** Can I write down what I want?  
**Translation:** 

**[5020.52s] English:** And then I try to formalize.  
**Translation:** 

**[5024.92s] English:** And when I do that, I think I have to solve this problem.  
**Translation:** 

**[5032.02s] English:** And,  
**Translation:** 

**[5033.52s] English:** You know, I didn't see it.  
**Translation:** 

**[5040.00s] English:** You need recurrence.  
**Translation:** 

**[5043.52s] English:** But  
**Translation:** 

**[5044.36s] English:** Do you observe human beings?  
**Translation:** 

**[5047.20s] English:** Do you try to?  
**Translation:** 

**[5049.38s] English:** It's the imitation question, right?  
**Translation:** 

**[5051.80s] English:** It seems that human beings reason.  
**Translation:** Vocabulary: imitation: 模仿

**[5054.02s] English:** This kind of sequential  
**Translation:** 

**[5056.24s] English:** Sort of.  
**Translation:** 

**[5059.40s] English:** Does that inspire you?  
**Translation:** 

**[5062.22s] English:** A thought that we need to add is that.  
**Translation:** 

**[5064.04s] English:** Into our  
**Translation:** 

**[5065.32s] English:** Intelligent  
**Translation:** 

**[5068.10s] English:** Systems.  
**Translation:** 

**[5068.70s] English:** You're saying,  
**Translation:** 

**[5071.44s] English:** You've kind of answered.  
**Translation:** 

**[5074.02s] English:** Saying, "Until now, I haven't seen a need for it.  
**Translation:** 

**[5076.44s] English:** And so, because of that.  
**Translation:** 

**[5078.38s] English:** You don't see a reason to think  
**Translation:** 

**[5080.34s] English:** About it.  
**Translation:** 

**[5080.80s] English:** You know, most of the things I don't understand.  
**Translation:** 

**[5084.68s] English:** In reasoning.  
**Translation:** 

**[5086.40s] English:** In human  
**Translation:** 

**[5087.22s] English:** It is too complicated for me.  
**Translation:** 

**[5090.42s] English:** For me,  
**Translation:** 

**[5093.14s] English:** The most difficult part  
**Translation:** 

**[5095.50s] English:** Is  
**Translation:** 

**[5097.14s] English:** To ask questions.  
**Translation:** 

**[5099.82s] English:** Good questions!  
**Translation:** 

**[5102.04s] English:** How it works.  
**Translation:** 

**[5103.80s] English:** How people  
**Translation:** 

**[5104.90s] English:** Asking questions.  
**Translation:** 

**[5106.48s] English:** I don't know.  
**Translation:** 

**[5109.40s] English:** This  
**Translation:** 

**[5109.78s] English:** You said that machine learning is not only  
**Translation:** 

**[5113.54s] English:** About technical things.  
**Translation:** 

**[5114.80s] English:** Speaking of questions, but it's also about  
**Translation:** 

**[5117.28s] English:** Philosophy  
**Translation:** 

**[5119.66s] English:** So,  
**Translation:** 

**[5120.46s] English:** What role does philosophy play?  
**Translation:** 

**[5122.12s] English:** Play in Machine Learning.  
**Translation:** 

**[5123.24s] English:** We talked about Plato.  
**Translation:** 

**[5124.44s] English:** But, generally speaking,  
**Translation:** 

**[5126.52s] English:** Over.  
**Translation:** 

**[5128.10s] English:** In this philosophical way? How do philosophy and math fit together in your mind?  
**Translation:** Vocabulary: philosophical: 哲学的

**[5136.42s] English:** First, ideas and then their implementation. It's like that, like  
**Translation:** 

**[5143.94s] English:** Say "admissible set of functions." It all comes together, everything. Because  
**Translation:** Vocabulary: admissible: 可接受的; implementation: 实施

**[5151.78s] English:** The first iteration of the theory was done 50 years ago; I told you that. This is the theory.  
**Translation:** 

**[5160.00s] English:** So, everything is there.  
**Translation:** Vocabulary: iteration: 循环

**[5162.14s] English:** If you have data, you can; and your set of functions is not large in capacity.  
**Translation:** 

**[5173.26s] English:** So, low VC dimension, you can do that.  
**Translation:** Vocabulary: dimension: 维度

**[5175.64s] English:** You can make structural risk minimization by controlling capacity.  
**Translation:** 

**[5181.04s] English:** But you were not able to make an admissible set of functions good.  
**Translation:** Vocabulary: minimization: 最小化

**[5187.84s] English:** But now, when we suddenly realize that we did not use another idea of convergence, which we can, everything comes together.  
**Translation:** 

**[5201.38s] English:** But those are mathematical notions.  
**Translation:** 

**[5203.10s] English:** Philosophy plays a role in simply saying that we should be swimming in the space of ideas.  
**Translation:** 

**[5211.74s] English:** Let's talk about what philosophy is.  
**Translation:** 

**[5214.24s] English:** Philosophy means an understanding of life.  
**Translation:** 

**[5217.84s] English:** So, understanding of life, as people like Plato, they understand it on a very high, abstract level.  
**Translation:** 

**[5226.96s] English:** So, and whatever I'm doing, it's just an implementation of my understanding of life.  
**Translation:** 

**[5236.34s] English:** But every new step is very difficult.  
**Translation:** Vocabulary: implementation: 实施

**[5241.84s] English:** For example, to find this idea,  
**Translation:** 

**[5247.84s] English:** That we needed big convergence was not simple for me.  
**Translation:** Vocabulary: convergence: 汇聚

**[5260.46s] English:** So, that required thinking about life a little bit.  
**Translation:** 

**[5264.16s] English:** Hard to trace, but there was some thought process.  
**Translation:** 

**[5269.76s] English:** You know, I've been working on the same problem for 50 years now.  
**Translation:** 

**[5276.72s] English:** And again, and again.  
**Translation:** 

**[5278.18s] English:** And again, and again.  
**Translation:** 

**[5278.46s] English:** And again.  
**Translation:** 

**[5280.00s] English:** I'm trying to be honest, and that is very important.  
**Translation:** 

**[5282.66s] English:** Not to be very enthusiastic,  
**Translation:** 

**[5284.82s] English:** But concentrate on whatever we were not able to achieve.  
**Translation:** 

**[5289.40s] English:** For example, and understand why.  
**Translation:** 

**[5294.16s] English:** And now I understand that, because I believe in math,  
**Translation:** 

**[5298.78s] English:** I believe in Wigner's idea.  
**Translation:** 

**[5303.62s] English:** But now, when I see that there are only two ways of convergence,  
**Translation:** 

**[5310.48s] English:** And we're using both.  
**Translation:** 

**[5312.86s] English:** That means that we must do as well as people doing.  
**Translation:** 

**[5319.76s] English:** But now, exactly in philosophy and what we know about predicates,  
**Translation:** Vocabulary: predicates: 谓词

**[5325.10s] English:** How do we understand life? Can we describe it as a predicate?  
**Translation:** 

**[5331.08s] English:** I thought about that.  
**Translation:** Vocabulary: predicate: 谓语

**[5334.36s] English:** And that is, more or less, an obvious level of symmetry.  
**Translation:** 

**[5340.80s] English:** But next, I have a feeling it's something about structures.  
**Translation:** Vocabulary: symmetry: 对称

**[5348.98s] English:** But I don't know how to formulate it.  
**Translation:** 

**[5351.84s] English:** How to measure a measure of structure, and all that stuff.  
**Translation:** 

**[5355.56s] English:** And the guy who will solve this challenge problem,  
**Translation:** 

**[5362.14s] English:** Then, when we will look at how he did it,  
**Translation:** 

**[5366.10s] English:** Probably, just symmetry is not enough.  
**Translation:** 

**[5370.00s] English:** But something like symmetry will be there.  
**Translation:** 

**[5373.72s] English:** Oh, yes, absolutely.  
**Translation:** 

**[5375.18s] English:** Symmetry will be there.  
**Translation:** 

**[5377.24s] English:** The level of symmetry will be there.  
**Translation:** 

**[5380.66s] English:** And the levels of symmetry, antisymmetry, diagonal, and vertical.  
**Translation:** Vocabulary: antisymmetry: 反对称; diagonal: 对角线; vertical: 垂直

**[5385.18s] English:** I don't even know how you can use the idea of symmetry in a different direction.  
**Translation:** 

**[5390.60s] English:** It's very general.  
**Translation:** 

**[5392.06s] English:** But it will be there.  
**Translation:** 

**[5394.42s] English:** I think that people are very sensitive to the idea of symmetry.  
**Translation:** 

**[5398.14s] English:** But there are several.  
**Translation:** 

**[5400.00s] English:** Ideas like symmetry.  
**Translation:** 

**[5400.62s] English:** I don't know.  
**Translation:** 

**[5401.22s] English:** I don't know where.  
**Translation:** 

**[5402.46s] English:** But I'm looking at the  
**Translation:** 

**[5402.62s] English:** As I would like to learn,  
**Translation:** 

**[5406.18s] English:** But  
**Translation:** 

**[5407.20s] English:** You cannot learn just by thinking.  
**Translation:** Vocabulary: cannot: 不能

**[5410.38s] English:** About that.  
**Translation:** 

**[5411.10s] English:** You should do challenging problems.  
**Translation:** 

**[5413.86s] English:** And then analyze them.  
**Translation:** 

**[5415.50s] English:** Why it was  
**Translation:** 

**[5417.44s] English:** Able to solve them.  
**Translation:** 

**[5419.32s] English:** And then you will see.  
**Translation:** 

**[5421.12s] English:** Very simple things.  
**Translation:** 

**[5423.68s] English:** It's not easy to find.  
**Translation:** 

**[5425.20s] English:** Even with talking about this,  
**Translation:** 

**[5427.60s] English:** One thing.  
**Translation:** 

**[5428.48s] English:** If you're going to ask me,  
**Translation:** 

**[5429.38s] English:** There's only one thing I can do.  
**Translation:** 

**[5429.50s] English:** Every time  
**Translation:** 

**[5429.78s] English:** There's only one way to solve this problem.  
**Translation:** 

**[5429.82s] English:** There is.  
**Translation:** 

**[5430.24s] English:** I was surprised.  
**Translation:** 

**[5433.94s] English:** I tried to understand.  
**Translation:** 

**[5435.70s] English:** These people describe  
**Translation:** 

**[5437.46s] English:** In language,  
**Translation:** 

**[5438.78s] English:** Strong Convergence  
**Translation:** 

**[5441.26s] English:** Mechanism for Learning  
**Translation:** 

**[5443.00s] English:** I did not see.  
**Translation:** 

**[5445.10s] English:** I don't know.  
**Translation:** 

**[5445.96s] English:** But weak convergence,  
**Translation:** Vocabulary: convergence: 收敛

**[5447.88s] English:** This dark story.  
**Translation:** 

**[5449.82s] English:** And, story like that?  
**Translation:** 

**[5451.60s] English:** When you will explain?  
**Translation:** 

**[5452.74s] English:** To kid, you will use weak convergence.  
**Translation:** 

**[5456.00s] English:** Argument.  
**Translation:** 

**[5456.50s] English:** It looks like it does, like  
**Translation:** 

**[5459.06s] English:** This  
**Translation:** 

**[5459.40s] English:** This  
**Translation:** 

**[5459.48s] English:** This  
**Translation:** 

**[5459.50s] English:** And that  
**Translation:** 

**[5459.66s] English:** But when you try to  
**Translation:** 

**[5462.38s] English:** Formalize  
**Translation:** 

**[5463.32s] English:** You're just ignoring this.  
**Translation:** 

**[5465.50s] English:** Why 50 years?  
**Translation:** 

**[5467.36s] English:** From the start of machine learning  
**Translation:** 

**[5470.04s] English:** And that's the role of philosophy.  
**Translation:** 

**[5471.24s] English:** I think that maybe,  
**Translation:** 

**[5473.46s] English:** I don't know.  
**Translation:** 

**[5475.78s] English:** Maybe this is just a theory, too.  
**Translation:** 

**[5479.90s] English:** We should not blame for that.  
**Translation:** 

**[5482.68s] English:** Because empirical risk  
**Translation:** 

**[5484.40s] English:** Minimization  
**Translation:** Vocabulary: empirical: 经验的; minimization: 最小化

**[5485.22s] English:** And all this stuff.  
**Translation:** 

**[5487.00s] English:** If you read,  
**Translation:** 

**[5488.70s] English:** Now.  
**Translation:** 

**[5489.48s] English:** Textbooks.  
**Translation:** 

**[5490.48s] English:** They just about bounded.  
**Translation:** 

**[5492.38s] English:** About empirical risk minimization.  
**Translation:** Vocabulary: bounded: 有界的

**[5494.20s] English:** They aren't looking.  
**Translation:** 

**[5495.04s] English:** For another problem.  
**Translation:** 

**[5498.10s] English:** Like "admissible set.  
**Translation:** 

**[5499.48s] English:** But, on the topic of life,...  
**Translation:** Vocabulary: admissible: 可接受的

**[5503.48s] English:** Perhaps.  
**Translation:** 

**[5505.44s] English:** We can talk in Russian.  
**Translation:** 

**[5508.48s] English:** For a little bit.  
**Translation:** 

**[5509.18s] English:** What's your favorite memory?  
**Translation:** 

**[5511.76s] English:** From childhood  
**Translation:** 

**[5512.58s] English:** What's your favorite memory?  
**Translation:** 

**[5514.52s] English:** From childhood  
**Translation:** 

**[5515.06s] English:** Music.  
**Translation:** 

**[5518.10s] English:** Music.  
**Translation:** 

**[5518.16s] English:** Music.  
**Translation:** 

**[5518.26s] English:** Music.  
**Translation:** 

**[5519.46s] English:** How about?  
**Translation:** 

**[5520.00s] English:** Can you try to answer in Russian?  
**Translation:** 

**[5520.46s] English:** Music.  
**Translation:** 

**[5521.46s] English:** Music.  
**Translation:** 

**[5522.46s] English:** Music.  
**Translation:** 

**[5522.56s] English:** Music.  
**Translation:** 

**[5523.46s] English:** Music.  
**Translation:** 

**[5524.46s] English:** Music.  
**Translation:** 

**[5524.80s] English:** It was very great when...  
**Translation:** 

**[5525.46s] English:** Music.  
**Translation:** 

**[5526.46s] English:** Music.  
**Translation:** 

**[5527.46s] English:** Music.  
**Translation:** 

**[5527.78s] English:** What kind of music?  
**Translation:** 

**[5528.46s] English:** Music.  
**Translation:** 

**[5529.46s] English:** Music.  
**Translation:** 

**[5529.88s] English:** Classical music.  
**Translation:** 

**[5530.46s] English:** Music.  
**Translation:** 

**[5531.46s] English:** Music.  
**Translation:** 

**[5531.76s] English:** What is your favorite?  
**Translation:** 

**[5532.46s] English:** Music.  
**Translation:** 

**[5532.50s] English:** Nu, different composers.  
**Translation:** 

**[5533.46s] English:** Music.  
**Translation:** 

**[5534.46s] English:** Music.  
**Translation:** 

**[5535.46s] English:** Music.  
**Translation:** 

**[5535.78s] English:** First, it was Vivaldi, I, in general, was surprised that it could be done like that.  
**Translation:** Vocabulary: vivaldi: 维瓦尔第

**[5536.46s] English:** Music.  
**Translation:** 

**[5537.46s] English:** Music.  
**Translation:** 

**[5538.46s] English:** Music.  
**Translation:** 

**[5539.46s] English:** Music.  
**Translation:** 

**[5540.46s] English:** Music.  
**Translation:** 

**[5541.46s] English:** Music.  
**Translation:** 

**[5542.46s] English:** Music.  
**Translation:** 

**[5543.36s] English:** Then, when I understood Bach, I was completely stunned.  
**Translation:** Vocabulary: stunned: 震惊

**[5543.46s] English:** Music.  
**Translation:** 

**[5544.46s] English:** Music.  
**Translation:** 

**[5545.46s] English:** Music.  
**Translation:** 

**[5546.46s] English:** Music.  
**Translation:** 

**[5547.14s] English:** By the way, from it I think that there exist predicates, like structures.  
**Translation:** 

**[5547.46s] English:** Music.  
**Translation:** Vocabulary: predicates: 谓词

**[5548.46s] English:** Music.  
**Translation:** 

**[5556.60s] English:** In Bakh, of course.  
**Translation:** 

**[5557.76s] English:** Because there just seems to be structure everywhere.  
**Translation:** 

**[5562.66s] English:** I don't think that different aspects of life are strongly separated in terms of predicates.  
**Translation:** 

**[5573.04s] English:** Structure in painting, structure in humanity, everywhere.  
**Translation:** 

**[5577.14s] English:** In human relationships, there is a structure.  
**Translation:** 

**[5579.62s] English:** Here's how to find these high-level predicates.  
**Translation:** 

**[5585.08s] English:** In Bakh and in life.  
**Translation:** 

**[5587.36s] English:** All is connected.  
**Translation:** 

**[5590.52s] English:** Now, when we talk about Bach,  
**Translation:** 

**[5594.00s] English:** Let's switch to English because I love Beethoven and Chopin.  
**Translation:** 

**[5598.22s] English:** Chopin is another interesting story.  
**Translation:** Vocabulary: beethoven: 贝多芬; chopin: 肖邦

**[5601.26s] English:** But Bach, if we are talking about predicates,  
**Translation:** 

**[5603.76s] English:** Bach, probably.  
**Translation:** 

**[5606.66s] English:** Has:  
**Translation:** 

**[5607.14s] English:** Probably,  
**Translation:** 

**[5608.14s] English:** The transcript appears to be incomplete or in a non-English script. Could you please provide more context or clarify the intended content? Without additional information, I cannot accurately punctuate and capitalize the given text.  
**Translation:** 

**[5609.14s] English:** Certain  
**Translation:** Vocabulary: cannot: 不能; capitalize: 首字母大写; clarify: 澄清; incomplete: 不完整; punctuate: 标点; transcript: 录音稿

**[5610.14s] English:** Predicates.  
**Translation:** 

**[5611.14s] English:** Knows,  
**Translation:** 

**[5612.14s] English:** Very interesting.  
**Translation:** 

**[5613.14s] English:** Read,  
**Translation:** 

**[5614.14s] English:** What?  
**Translation:** 

**[5615.14s] English:** Critics  
**Translation:** 

**[5616.14s] English:** Write:  
**Translation:** 

**[5617.14s] English:** About Bakh.  
**Translation:** 

**[5618.14s] English:** What?  
**Translation:** 

**[5619.14s] English:** They use words.  
**Translation:** 

**[5620.14s] English:** They are trying.  
**Translation:** 

**[5621.14s] English:** Describe.  
**Translation:** 

**[5622.14s] English:** Predicates.  
**Translation:** 

**[5623.14s] English:** Yes.  
**Translation:** 

**[5624.14s] English:** I  
**Translation:** 

**[5625.14s] English:** And  
**Translation:** 

**[5626.14s] English:** And  
**Translation:** 

**[5627.14s] English:** And  
**Translation:** 

**[5628.14s] English:** And  
**Translation:** 

**[5629.14s] English:** And  
**Translation:** 

**[5630.14s] English:** And  
**Translation:** 

**[5631.14s] English:** And  
**Translation:** 

**[5632.14s] English:** And  
**Translation:** 

**[5633.14s] English:** And  
**Translation:** 

**[5634.14s] English:** And  
**Translation:** 

**[5635.14s] English:** And  
**Translation:** 

**[5636.14s] English:** Chopin.  
**Translation:** 

**[5636.66s] English:** I  
**Translation:** 

**[5637.66s] English:** And  
**Translation:** 

**[5638.66s] English:** And and  
**Translation:** 

**[5639.66s] English:** Continues...  
**Translation:** 

**[5640.00s] English:** On that, so maybe from this you can describe a predicate for digit recognition. I'll from.  
**Translation:** Vocabulary: digit: 阿拉伯数字; predicate: 谓词

**[5648.90s] English:** Bach and Chopin? No, no, no. Not from Bach and Chopin. From the critic's interpretation of the music, yeah.  
**Translation:** 

**[5655.14s] English:** When they're trying to explain your music, what they use is this: they describe it as high.  
**Translation:** Vocabulary: interpretation: 解释

**[5663.84s] English:** Levels of Plato's ideas: what lies behind this music that's so brilliant, so art is not just about self.  
**Translation:** 

**[5672.84s] English:** Explanatory, in some sense, so you have to try to convert it into ideas. It is problems when...  
**Translation:** Vocabulary: convert: 转换; explanatory: 解释性的

**[5681.50s] English:** You go from ideas to the representation, it's an easy way, but when you're trying to go back,...  
**Translation:** 

**[5689.32s] English:** It is, you'll post problems, but nevertheless, I believe that.  
**Translation:** 

**[5693.84s] English:** When you're looking from that, even from art, you will be able to find predicates for digit recognition.  
**Translation:** 

**[5703.60s] English:** That's such a fascinating and powerful notion. Do you ponder your own mortality?  
**Translation:** Vocabulary: predicates: 谓词

**[5711.44s] English:** Do you think about it? Do you fear it? Do you draw insight from it?  
**Translation:** 

**[5716.72s] English:** About mortality, no, yeah. Are you afraid of death?  
**Translation:** 

**[5724.74s] English:** Not too much, not too much.  
**Translation:** 

**[5729.52s] English:** It is a pity that I will not be able to do something which I think I have a feeling to do.  
**Translation:** 

**[5739.28s] English:** For example, I will be very happy to work with theoretical musicians to write this collection.  
**Translation:** 

**[5751.84s] English:** Of course, but what/how they describe music, how they use what predicates, and from art as well.  
**Translation:** 

**[5760.00s] English:** Then, take what is in common and try to understand the predicate which is absolute for everything.  
**Translation:** 

**[5768.48s] English:** And then use that for visual recognition and see if there is a connection, yeah, exactly.  
**Translation:** Vocabulary: predicate: 谓语

**[5773.68s] English:** There's still time; we've got time.  
**Translation:** 

**[5779.04s] English:** We've got time; it's going to take years and years, and maybe even decades. Yeah, it's a long way.  
**Translation:** 

**[5786.32s] English:** Well, see, you've got the patient, mathematical mind, I think it could be.  
**Translation:** 

**[5791.44s] English:** Done very quickly and very beautifully, I think it's a really elegant idea. Yeah, but also some...  
**Translation:** Vocabulary: elegant: 优雅; mathematical: 数学的

**[5797.04s] English:** Of course, yeah. You know, the most of the time, it's not to make this collection to understand.  
**Translation:** 

**[5805.20s] English:** What is the common thing to think about that once again, and again, and again, and again? But I...  
**Translation:** 

**[5811.52s] English:** Think sometimes, especially just when you say this idea now.  
**Translation:** 

**[5815.60s] English:** Even just  
**Translation:** 

**[5817.12s] English:** Putting together the collection and looking at the different items,  
**Translation:** 

**[5822.16s] English:** Sets of data, language trying to interpret music, criticize music, and images: I think there will be.  
**Translation:** Vocabulary: interpret: 解释

**[5829.36s] English:** Sparks of ideas that will come, of course, again and again. You'll come up with better ideas, but...  
**Translation:** 

**[5833.52s] English:** Even just that notion is a beautiful notion. I even have some examples; so, I have a friend.  
**Translation:** Vocabulary: sparks: 火花

**[5845.12s] English:** Who was?  
**Translation:** 

**[5847.28s] English:** Specialist in Russian poetry, she is; professor of Russian poetry, he did not write.  
**Translation:** 

**[5857.92s] English:** Poems, but she knows a lot of stuff. She made a book, several books, and one of them is a collection of  
**Translation:** 

**[5871.92s] English:** Russian poetry: she has images of Russian poetry.  
**Translation:** 

**[5877.12s] English:** She collects all images of Russian poetry.  
**Translation:** 

**[5879.36s] English:** She collects all images of Russian poetry.  
**Translation:** 

**[5880.00s] English:** And I ask you to do the following: You have NIPS, digit recognition, and you get 100 digits, or maybe less than 100—I don't remember, maybe 50 digits—and try from a poetical point of view to describe every image which you see, using only words of images from Russian poets.  
**Translation:** 

**[5910.00s] English:** And she did it.  
**Translation:** Vocabulary: digit: 位数; digits: 数字; poetical: 诗意的

**[5940.00s] English:** And there is an algorithm: when you're working with privileged information, you're doing much better.  
**Translation:** 

**[5949.46s] English:** So, there's something there.  
**Translation:** Vocabulary: algorithm: 算法; privileged: 特权信息

**[5951.24s] English:** And there is, and you see, she unfortunately did it—the collection of digits in poetic descriptions of these digits.  
**Translation:** 

**[5969.26s] English:** Yeah.  
**Translation:** Vocabulary: poetic: 诗意的

**[5969.30s] English:** So, there's some.  
**Translation:** 

**[5970.00s] English:** Something there in that poetic description.  
**Translation:** 

**[5972.84s] English:** But I think that there are abstract ideas on the Platonic level of ideas.  
**Translation:** 

**[5980.44s] English:** Yeah, that they're there, that could be discovered.  
**Translation:** Vocabulary: platonic: 理念的

**[5983.16s] English:** And music seems to be a good entry point.  
**Translation:** 

**[5984.94s] English:** But as soon as we start with this challenge problem.  
**Translation:** 

**[5990.24s] English:** The challenge problem.  
**Translation:** 

**[5991.22s] English:** It immediately connected to all this stuff.  
**Translation:** 

**[5995.32s] English:** Especially with your talk and this podcast, and I'll do whatever I can to advertise.  
**Translation:** 

**[6000.00s] English:** It's such a clean, beautiful, Einstein-like formulation of the challenge before us.  
**Translation:** Vocabulary: advertise: 做宣传

**[6005.14s] English:** Right.  
**Translation:** 

**[6005.84s] English:** Let me ask another absurd question.  
**Translation:** Vocabulary: absurd: 荒谬的

**[6010.02s] English:** We talked about mortality.  
**Translation:** 

**[6012.64s] English:** We talked about the philosophy of life.  
**Translation:** 

**[6014.44s] English:** What do you think is the meaning of life?  
**Translation:** 

**[6017.44s] English:** What's the predicate for mysterious existence here on Earth?  
**Translation:** Vocabulary: predicate: 谓语

**[6023.60s] English:** I don't know.  
**Translation:** 

**[6032.96s] English:** It's very interesting.  
**Translation:** 

**[6035.70s] English:** We have in Russia, I don't know, the guy Strugatsky.  
**Translation:** 

**[6043.00s] English:** They're writing pictures.  
**Translation:** Vocabulary: strugatsky: 斯特鲁加茨基兄弟

**[6046.36s] English:** They're thinking about what's going on.  
**Translation:** 

**[6051.54s] English:** And they have an idea.  
**Translation:** 

**[6053.60s] English:** And they're developing two types of people.  
**Translation:** 

**[6062.70s] English:** Common people and very smart people.  
**Translation:** 

**[6065.08s] English:** They just started.  
**Translation:** 

**[6066.68s] English:** And these two branches of people will go in different directions very soon.  
**Translation:** 

**[6073.20s] English:** So, that's what they're thinking about.  
**Translation:** 

**[6078.00s] English:** So, the purpose of life is to create two paths.  
**Translation:** 

**[6083.60s] English:** Two paths.  
**Translation:** 

**[6084.12s] English:** As human societies,  
**Translation:** 

**[6085.98s] English:** Yes.  
**Translation:** 

**[6086.96s] English:** Simple people, and more complicated people.  
**Translation:** 

**[6089.88s] English:** Which do you like best?  
**Translation:** 

**[6091.42s] English:** The simple people, or the complicated ones?  
**Translation:** 

**[6093.78s] English:** I don't know.  
**Translation:** 

**[6095.62s] English:** It's just his fantasy.  
**Translation:** 

**[6098.44s] English:** But, you know, every week we have a guy who is just a writer and a theoretician of literature.  
**Translation:** 

**[6111.72s] English:** And he explains.  
**Translation:** Vocabulary: theoretician: 理论家

**[6113.60s] English:** How is he going to write?  
**Translation:** 

**[6118.32s] English:** And how is he going to write?  
**Translation:** 

**[6120.00s] English:** And I understood that I'm just a small kid compared to him; he is a very smart guy.  
**Translation:** 

**[6120.78s] English:** Are you going to write an entire story?  
**Translation:** 

**[6121.02s] English:** Do you go to a library and write what's going on on a paper?  
**Translation:** 

**[6121.14s] English:** How is he going to work on a notebook?  
**Translation:** 

**[6121.54s] English:** And how do you warm up on a desk?  
**Translation:** 

**[6122.08s] English:** How does he become a good reader?  
**Translation:** 

**[6122.64s] English:** Do you have a job?  
**Translation:** 

**[6123.22s] English:** How is he going to the Mundial?  
**Translation:** Vocabulary: mundial: 世界杯

**[6123.24s] English:** Because the human difference between this and life has two parts.  
**Translation:** 

**[6123.56s] English:** And when he was about five years old, he showed up on the internet and was doing such a great job.  
**Translation:** 

**[6123.60s] English:** He begins to take notes and he tells.  
**Translation:** 

**[6124.14s] English:** If, for instance, he does the training, he just tells them to bring their assistant.  
**Translation:** 

**[6125.28s] English:** And we'll give you a little secret.  
**Translation:** 

**[6125.60s] English:** He gives a note to that.  
**Translation:** 

**[6125.70s] English:** Because, year after year, watching this, you may hear in the chat.  
**Translation:** 

**[6126.06s] English:** It'll come on something, and who knows? You might see it here.  
**Translation:** 

**[6131.36s] English:** Understanding life, he knows this. Predicate, he knows big blocks of—like, I'm used every time.  
**Translation:** 

**[6141.86s] English:** When I listen to him, and he just talks about literature, I think that I was  
**Translation:** Vocabulary: predicate: 主谓词

**[6148.94s] English:** Surprised, uh, so the managers in big companies, most of them are guys who study.  
**Translation:** 

**[6165.80s] English:** English language and English literature, so why because they understand life.  
**Translation:** 

**[6174.02s] English:** They understand models, and among them,  
**Translation:** 

**[6177.78s] English:** My  
**Translation:** 

**[6178.92s] English:** My  
**Translation:** 

**[6178.94s] English:** There may be many talented critics.  
**Translation:** 

**[6183.82s] English:** Which just analyzing this, and this is big science, like  
**Translation:** 

**[6189.02s] English:** Prop: This is blocks.  
**Translation:** 

**[6193.18s] English:** That's very small.  
**Translation:** 

**[6197.34s] English:** It amazes me that you are and continue to be humbled by the brilliance of others.  
**Translation:** Vocabulary: amazes: 使惊讶; brilliance: 卓越; humbled: 谦卑

**[6202.86s] English:** I'm very modest about myself, seeing so many smart guys around.  
**Translation:** 

**[6208.92s] English:** Well, let me be immodest for you.  
**Translation:** Vocabulary: immodest: 不谦虚; modest: 谦虚

**[6211.72s] English:** You're one of the greatest mathematical statisticians of our time.  
**Translation:** 

**[6216.04s] English:** It's truly an honor; thank you for talking again.  
**Translation:** Vocabulary: mathematical: 数学的

**[6218.06s] English:** And let's talk.  
**Translation:** 

**[6219.78s] English:** It's not.  
**Translation:** 

**[6222.18s] English:** Yeah.  
**Translation:** 

**[6224.74s] English:** Let's talk again when your challenges have been taken on and solved by a grad student.  
**Translation:** 

**[6231.84s] English:** Especially,  
**Translation:** 

**[6234.84s] English:** I hope this will happen.  
**Translation:** 

**[6236.74s] English:** Maybe music will be involved.  
**Translation:** 

**[6238.60s] English:** Vladimir, thank you so much.  
**Translation:** 

**[6240.00s] English:** Been; thank you very much. Thanks for listening to this conversation with Vladimir Vapnik, and thank.  
**Translation:** 

**[6245.90s] English:** You to our presenting sponsor, Cash App. Download it, use code LexPodcast, and you'll get $10.  
**Translation:** Vocabulary: sponsor: 赞助商

**[6252.40s] English:** And $10 will go to an organization that inspires and educates young minds to become  
**Translation:** 

**[6257.40s] English:** Science and technology innovators of tomorrow: If you enjoy this podcast, subscribe on YouTube!  
**Translation:** Vocabulary: educates: 教育; innovators: 创新者; inspires: 启发; subscribe: 订阅

**[6263.10s] English:** Give us five stars on Apple Podcast, support it on Patreon, or simply connect with me on Twitter.  
**Translation:** 

**[6268.42s] English:** At Lex Friedman, and now let me leave you with some words from Vladimir Vapnik.  
**Translation:** Vocabulary: friedman: 莱克斯·弗里德曼; patreon: Patreon; vladimir: 弗拉基米尔

**[6274.58s] English:** When solving a problem of interest, do not solve a more general problem as an intermediate step.  
**Translation:** 

**[6281.44s] English:** Thank you for listening. I hope to see you next time.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
