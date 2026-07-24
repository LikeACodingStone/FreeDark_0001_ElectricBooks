# Podcast vocabulary notes
Source file: Lex Fridman - Vladimir Vapnik： Predicates, Invariants, and the Essence of Intelligence ｜ Lex Fridman Podcast #71.opus

**[0.00s] English:** The following is a conversation with Vladimir Vapnik, part two, the second time we spoke on the podcast.  
**Translation:** 

**[7.08s] English:** He's the co-inventor of Support Vector Machines, Support Vector Clustering, VC Theory, and many foundational ideas in statistical learning.  
**Translation:** Vocabulary: clustering: 聚类; foundational: 基础的

**[14.82s] English:** He was born in the Soviet Union, worked at the Institute of Controlled Sciences in Moscow, then in the U.S., worked at AT&T, NEC Labs, Facebook AI Research, and now is a professor at Columbia University.  
**Translation:** 

**[28.52s] English:** His work has been cited over 200,000 times. The first time we spoke on the podcast was just over a year ago, one of the early episodes.  
**Translation:** Vocabulary: cited: 被引用; columbia: 哥伦比亚大学; moscow: 莫斯科

**[38.76s] English:** This time, we spoke after a lecture he gave titled Complete Statistical Theory of Learning as part of the MIT series of lectures on deep learning and AI that I organized.  
**Translation:** 

**[49.82s] English:** I'll release the video of the lecture in the next few days.  
**Translation:** 

**[53.74s] English:** This podcast and lecture are independent from each other, so you don't need one to understand the other.  
**Translation:** 

**[58.94s] English:** The lecture is quite technical and math-heavy, so if you do watch both, I recommend listening to this podcast first, since the podcast is probably a bit more accessible.  
**Translation:** 

**[70.88s] English:** This is the Artificial Intelligence Podcast.  
**Translation:** 

**[73.94s] English:** If you enjoy it, subscribe on YouTube, give it five stars on Apple Podcasts, support it on Patreon, or simply connect with me on Twitter at Lex Friedman, spelled F-R-I-D-M-A-N.  
**Translation:** Vocabulary: subscribe: 订阅

**[84.44s] English:** As usual, I'll do one or two minutes of ads now and never any later.  
**Translation:** 

**[88.52s] English:** If there are any ads in the middle that can break the flow of the conversation, I hope that works for you and doesn't hurt the listening experience.  
**Translation:** 

**[95.94s] English:** This show is presented by Cash App, the number one finance app in the App Store.  
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

**[120.00s] English:** and security in all digital transactions is very important, let me mention the PCI  
**Translation:** 

**[125.28s] English:** data security standard, PCI DSS level 1, that Cash App is compliant with. I'm a big fan of  
**Translation:** Vocabulary: compliant: 符合标准

**[133.00s] English:** standards for safety and security, and PCI DSS is a good example of that, where a bunch of  
**Translation:** 

**[139.48s] English:** competitors got together and agreed that there needs to be a global standard around the security  
**Translation:** 

**[144.22s] English:** of transactions. Now, we just need to do the same for autonomous vehicles and AI systems in general.  
**Translation:** 

**[151.34s] English:** So again, if you get Cash App from the App Store or Google Play and use the code LEXPODCAST,  
**Translation:** Vocabulary: autonomous: 自主

**[156.86s] English:** you get $10, and Cash App will also donate $10 to FIRST, one of my favorite organizations  
**Translation:** 

**[162.64s] English:** that is helping to advance robotics and STEM education for young people around the world.  
**Translation:** 

**[169.22s] English:** And now, here's my conversation with Vladimir Vapnik.  
**Translation:** 

**[174.22s] English:** You and I talked about Alan Turing yesterday a little bit, and that he, as the father of  
**Translation:** Vocabulary: turing: 图灵; vladimir: 弗拉基米尔

**[181.34s] English:** artificial intelligence, may have instilled in our field an ethic of engineering and not science,  
**Translation:** 

**[187.04s] English:** seeking more to build intelligence rather than to understand it. What do you think is  
**Translation:** Vocabulary: instilled: 灌输

**[192.70s] English:** the difference between these two paths of engineering intelligence and the science  
**Translation:** 

**[199.38s] English:** of intelligence? It's a completely different story. Engineering,  
**Translation:** 

**[204.22s] English:** Vapnik is imitation of human activity. You have to make a device which behaves as human behave,  
**Translation:** 

**[214.54s] English:** have all the functions of humans. It doesn't matter how you do it. But to understand what  
**Translation:** Vocabulary: imitation: 模仿

**[223.62s] English:** is intelligence about is quite a different problem. So I think, I believe, that it's somehow related to  
**Translation:** 

**[234.22s] English:** we talked yesterday about, because  
**Translation:** 

**[240.00s] English:** Look at the Vladimir Probst idea.  
**Translation:** 

**[245.64s] English:** He just found 31 predicates.  
**Translation:** Vocabulary: predicates: 断言

**[252.88s] English:** He called it units, which can explain humor behavior,  
**Translation:** 

**[259.10s] English:** at least in Russian tales.  
**Translation:** 

**[260.90s] English:** He looked at Russian tales and derived from that.  
**Translation:** 

**[264.96s] English:** And then people realized that it's more wide than in Russian tales.  
**Translation:** 

**[269.02s] English:** It is in TV, in movie serials, and so on and so on.  
**Translation:** 

**[273.90s] English:** So you're talking about Vladimir Probst,  
**Translation:** 

**[277.72s] English:** who in 1928 published a book, Morphology of the Folktale,  
**Translation:** 

**[282.10s] English:** describing 31 predicates that have this kind of sequential structure  
**Translation:** Vocabulary: folktale: 民间故事; morphology: 结构分析; sequential: 顺序的

**[289.28s] English:** that a lot of the stories, narratives follow in Russian folklore and other contexts.  
**Translation:** 

**[294.68s] English:** We'll talk about it.  
**Translation:** Vocabulary: folklore: 民间传说

**[296.04s] English:** I'd like to talk about predicates in a focused way.  
**Translation:** 

**[299.22s] English:** But let me, if you allow me to stay zoomed out on our friend Alan Turing.  
**Translation:** Vocabulary: turing: 图灵

**[304.68s] English:** And, you know, he inspired a generation with the imitation game.  
**Translation:** 

**[310.36s] English:** Yes.  
**Translation:** 

**[311.56s] English:** Do you think, if we can linger on that a little bit longer,  
**Translation:** 

**[315.16s] English:** do you think we can learn,  
**Translation:** 

**[318.44s] English:** do you think learning to imitate intelligence can get us closer to understanding intelligence?  
**Translation:** 

**[324.68s] English:** So why do you think imitation is so...  
**Translation:** 

**[329.02s] English:** So far from understanding?  
**Translation:** 

**[332.60s] English:** I think that it is different.  
**Translation:** 

**[334.54s] English:** Between you have different goals.  
**Translation:** 

**[337.54s] English:** So your goal is to create something, something useful.  
**Translation:** 

**[343.60s] English:** Yeah.  
**Translation:** 

**[344.00s] English:** And that is great.  
**Translation:** 

**[345.66s] English:** And you can see how much things was done,  
**Translation:** 

**[349.76s] English:** and I believe that it will be done even more.  
**Translation:** 

**[353.14s] English:** It's self-driving cars and also this business.  
**Translation:** 

**[356.50s] English:** It is great.  
**Translation:** 

**[358.34s] English:** And it was...  
**Translation:** 

**[359.02s] English:** Spark Bay.  
**Translation:** 

**[359.70s] English:** Spark Bay.  
**Translation:** 

**[360.00s] English:** curing vision. But understanding is very difficult. It is more or less a philosophical category.  
**Translation:** Vocabulary: philosophical: 哲学的

**[368.52s] English:** What means to understand the world? I believe in the scheme which starts from Plato that  
**Translation:** 

**[375.98s] English:** there exists a world of ideas. I believe that intelligence is a world of ideas, but it is  
**Translation:** 

**[383.50s] English:** a world of pure ideas. When you combine them with reality things, it creates, as in my  
**Translation:** 

**[394.72s] English:** case, invariance, which is very specific. I believe the combination of ideas in a way  
**Translation:** Vocabulary: invariance: 不变性

**[406.52s] English:** to constructing invariant is intelligence. But first of all, predicate. If you want to  
**Translation:** 

**[413.48s] English:** know predicate, and hopefully then not too much predicate exists. For example, 31 predicate  
**Translation:** Vocabulary: invariant: 不变量; predicate: 谓词

**[423.12s] English:** for human behavior, it is not a lot.  
**Translation:** 

**[425.88s] English:** Vladimir Propp used 31, you can even call them predicates, 31 predicates to describe  
**Translation:** Vocabulary: predicates: 谓词

**[434.88s] English:** stories, narratives. So you think human behavior, how much of human behavior, how much of our  
**Translation:** 

**[442.54s] English:** world, our universe...  
**Translation:** 

**[443.48s] English:** All the things that matter in our existence can be summarized in predicates of the kind  
**Translation:** 

**[450.76s] English:** that Propp was working with.  
**Translation:** Vocabulary: summarized: 概括

**[452.16s] English:** I think that we have a lot of formal behavior. But I think that predicate is much  
**Translation:** 

**[459.76s] English:** less. Because even in this example, which I gave you yesterday, you saw that predicate  
**Translation:** 

**[469.50s] English:** can be...  
**Translation:** 

**[470.50s] English:** One predicate can be a predicate.  
**Translation:** 

**[472.00s] English:** Okay.  
**Translation:** 

**[473.00s] English:** One predicate can construct many different invariants depending on your data. They're  
**Translation:** Vocabulary: invariants: 不变量

**[480.00s] English:** to different data and they give different invariants. But pure ideas, maybe not so much.  
**Translation:** 

**[488.56s] English:** Not so many.  
**Translation:** 

**[489.20s] English:** I don't know about that. But my guess, I hope, that's why challenge about  
**Translation:** 

**[495.92s] English:** digital recognition, how much you need.  
**Translation:** 

**[498.48s] English:** I think we'll talk about computer vision and 2D images a little bit in your challenge.  
**Translation:** 

**[504.32s] English:** That's exactly about intelligence.  
**Translation:** 

**[506.48s] English:** That's exactly about, no, that hopes to be exactly about the spirit of intelligence  
**Translation:** 

**[515.28s] English:** in the simplest possible way.  
**Translation:** 

**[517.04s] English:** Yeah, absolutely. You should start the simplest way. Otherwise,  
**Translation:** 

**[520.80s] English:** you will not be able to do it.  
**Translation:** 

**[522.24s] English:** Well, there's an open question whether starting at the MNIST digit recognition  
**Translation:** 

**[528.40s] English:** is a step towards intelligence or it's an entirely different thing.  
**Translation:** Vocabulary: digit: 阿拉伯数字

**[531.68s] English:** I think that to beat records using  
**Translation:** 

**[536.48s] English:** 300, 200 times less examples, you need intelligence.  
**Translation:** 

**[540.56s] English:** You need intelligence. Because you use this term, and it'll be nice,  
**Translation:** 

**[545.28s] English:** I'd like to ask simple, maybe even dumb questions. Let's start with a predicate.  
**Translation:** Vocabulary: predicate: 谓词

**[552.72s] English:** In terms of terms and how you think about it, what is a predicate?  
**Translation:** 

**[557.36s] English:** I don't know. I have a feeling formally they exist. But I believe that predicate  
**Translation:** 

**[566.48s] English:** for 2D images, one of them is symmetry.  
**Translation:** 

**[571.52s] English:** Hold on a second. Sorry. Sorry to interrupt and pull you back.  
**Translation:** Vocabulary: symmetry: 对称

**[576.32s] English:** At the simplest level, we're not being profound currently,  
**Translation:** 

**[580.56s] English:** a predicate is a statement of something that is true.  
**Translation:** Vocabulary: profound: 深奥

**[583.68s] English:** Yes.  
**Translation:** 

**[585.04s] English:** Do you think of predicates as somehow probabilistic in nature, or is this binary,  
**Translation:** Vocabulary: binary: 非此即彼; predicates: 谓词; probabilistic: 概率的

**[594.56s] English:** this is truly constraints?  
**Translation:** 

**[596.00s] English:** Yes.  
**Translation:** Vocabulary: constraints: 限制条件

**[596.40s] English:** Of logical statements about the world.  
**Translation:** 

**[600.00s] English:** In my definition, the simplest predicate is function.  
**Translation:** 

**[603.92s] English:** Function, and you can use this function to make inner product.  
**Translation:** 

**[609.38s] English:** That is predicate.  
**Translation:** 

**[610.56s] English:** What's the input and what's the output of the function?  
**Translation:** 

**[613.96s] English:** Input is X, something which is input in reality.  
**Translation:** 

**[618.66s] English:** Say, if you consider digit recognition, it's pixel space.  
**Translation:** 

**[623.74s] English:** Yes.  
**Translation:** Vocabulary: pixel: 像素

**[624.12s] English:** Input.  
**Translation:** 

**[624.90s] English:** But it is function which in pixel space.  
**Translation:** 

**[629.14s] English:** But it can be any function from pixel space.  
**Translation:** 

**[635.62s] English:** And you choose, and I believe that there are several functions  
**Translation:** 

**[640.54s] English:** which is important for understanding of images.  
**Translation:** 

**[646.34s] English:** One of them is symmetry.  
**Translation:** 

**[648.28s] English:** It's not so simple construction as I described with the derivative,  
**Translation:** 

**[653.26s] English:** with all this stuff.  
**Translation:** Vocabulary: derivative: 导数

**[655.52s] English:** But another, I believe, I don't know how many,  
**Translation:** 

**[658.40s] English:** is how well-structurized is picture.  
**Translation:** 

**[663.42s] English:** Structurized?  
**Translation:** 

**[664.26s] English:** Yeah.  
**Translation:** Vocabulary: structurized: 结构化

**[664.70s] English:** What do you mean by structurized?  
**Translation:** 

**[666.86s] English:** It is formal definition.  
**Translation:** 

**[669.10s] English:** Say, something heavy on the left corner,  
**Translation:** 

**[673.46s] English:** not so heavy in the middle, and so on.  
**Translation:** 

**[676.98s] English:** You describe in general concept of what you assume.  
**Translation:** 

**[681.82s] English:** Concepts.  
**Translation:** 

**[682.50s] English:** Some kind of universal concepts.  
**Translation:** 

**[685.18s] English:** Yeah.  
**Translation:** 

**[685.46s] English:** But I don't know how to formulate.  
**Translation:** 

**[688.40s] English:** I don't know how to summarize this.  
**Translation:** Vocabulary: summarize: 概括

**[690.18s] English:** Do you?  
**Translation:** 

**[690.54s] English:** So this is the thing.  
**Translation:** 

**[691.56s] English:** There's a million ways we can talk about this.  
**Translation:** 

**[693.56s] English:** I'll keep bringing it up.  
**Translation:** 

**[694.60s] English:** But we humans have such concepts when we look at digits.  
**Translation:** 

**[701.50s] English:** But it's hard to put them, just like you're saying now,  
**Translation:** Vocabulary: digits: 阿拉伯数字

**[703.84s] English:** it's hard to put them into words.  
**Translation:** 

**[705.92s] English:** You know, that is example.  
**Translation:** 

**[708.58s] English:** When critics in music trying to describe music, they use predicate.  
**Translation:** 

**[716.86s] English:** And not just.  
**Translation:** Vocabulary: predicate: 谓词

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

**[718.60s] English:** Too many predicate.  
**Translation:** 

**[720.00s] English:** but in different combination.  
**Translation:** 

**[722.82s] English:** But they have some special words for describing music.  
**Translation:** 

**[728.42s] English:** And the same should be for images.  
**Translation:** 

**[732.50s] English:** But maybe there are critics who understand  
**Translation:** 

**[735.50s] English:** essence of what this image is about.  
**Translation:** 

**[740.60s] English:** Do you think there exists critics  
**Translation:** 

**[743.00s] English:** who can summarize the essence of images, human beings?  
**Translation:** 

**[748.28s] English:** I hope so, yes.  
**Translation:** 

**[752.62s] English:** Explicitly state them on paper.  
**Translation:** 

**[756.64s] English:** The fundamental question I'm asking is  
**Translation:** Vocabulary: explicitly: 明确地

**[760.86s] English:** do you think there exists a small set of predicates  
**Translation:** 

**[766.16s] English:** that will summarize images?  
**Translation:** Vocabulary: predicates: 谓词

**[767.98s] English:** It feels to our mind like it does  
**Translation:** 

**[771.10s] English:** that the concept of what makes a two and a three and a four...  
**Translation:** 

**[775.48s] English:** No, no, no.  
**Translation:** 

**[776.54s] English:** It's not on this.  
**Translation:** 

**[778.28s] English:** It's not on this level.  
**Translation:** 

**[780.86s] English:** It should not describe two, three, four.  
**Translation:** 

**[784.92s] English:** It describes some construction  
**Translation:** 

**[786.88s] English:** which allow you to create invariance.  
**Translation:** Vocabulary: invariance: 不变性

**[792.04s] English:** And invariance, sorry to stick on this, but terminology.  
**Translation:** 

**[796.18s] English:** Invariance, it is property of your image.  
**Translation:** Vocabulary: terminology: 术语

**[804.42s] English:** Say, I can say,  
**Translation:** 

**[807.24s] English:** looking on my image,  
**Translation:** 

**[809.10s] English:** it is more or less symmetric.  
**Translation:** 

**[812.00s] English:** And I can give you a value of symmetry.  
**Translation:** Vocabulary: symmetric: 对称; symmetry: 对称性

**[814.98s] English:** Say, level of symmetry  
**Translation:** 

**[817.18s] English:** using this function which I gave yesterday.  
**Translation:** 

**[823.40s] English:** And you can describe  
**Translation:** 

**[825.06s] English:** that your image has these characteristics  
**Translation:** 

**[831.26s] English:** exactly in the way how musical critics describe music.  
**Translation:** 

**[837.24s] English:** So, but this is...  
**Translation:** 

**[840.00s] English:** invariant applied to specific data, to specific music, to something.  
**Translation:** 

**[847.68s] English:** I strongly believe in these Plato ideas, that there exists world of predicate and world  
**Translation:** Vocabulary: invariant: 不变量; predicate: 谓词

**[855.52s] English:** of reality, and predicate and reality is somehow connected, and you have to know that.  
**Translation:** 

**[862.12s] English:** Let's talk about Plato a little bit.  
**Translation:** 

**[864.12s] English:** So you draw a line from Plato to Hegel to Wigner to today.  
**Translation:** 

**[869.12s] English:** Yes.  
**Translation:** Vocabulary: hegel: 黑格尔; wigner: 魏格纳

**[870.12s] English:** So Plato has forms, the theory of forms.  
**Translation:** 

**[875.74s] English:** There's a world of ideas and a world of things, as you talk about, and there's a connection.  
**Translation:** 

**[880.54s] English:** And presumably the world of ideas is very small, and the world of things is arbitrarily  
**Translation:** 

**[887.44s] English:** big.  
**Translation:** Vocabulary: arbitrarily: 任意; presumably: 推测

**[888.44s] English:** But they're all, what Plato calls them, it's a shadow.  
**Translation:** 

**[892.74s] English:** The real world is a shadow from the world of forms.  
**Translation:** 

**[894.96s] English:** Yeah.  
**Translation:** 

**[895.96s] English:** Do you have projection?  
**Translation:** Vocabulary: projection: 投影片

**[896.96s] English:** Projection.  
**Translation:** 

**[897.96s] English:** Of world of idea?  
**Translation:** 

**[898.96s] English:** Yeah.  
**Translation:** 

**[899.12s] English:** Very poetic.  
**Translation:** 

**[900.12s] English:** In reality, you can realize this projection using these invariants, because it is projection  
**Translation:** 

**[909.88s] English:** on specific examples, which create specific features of specific objects.  
**Translation:** Vocabulary: invariants: 不变量

**[918.36s] English:** So the essence of intelligence is, while only being able to observe the world of things,  
**Translation:** 

**[924.84s] English:** try to come up with a world of ideas.  
**Translation:** 

**[927.12s] English:** Exactly.  
**Translation:** 

**[928.12s] English:** Like in this music story.  
**Translation:** 

**[929.12s] English:** Intelligent musical critics knows all this world and have a feeling about what it is.  
**Translation:** 

**[934.76s] English:** I feel like that's a contradiction, intelligent music critics.  
**Translation:** Vocabulary: contradiction: 矛盾

**[939.12s] English:** But I think music is to be enjoyed in all its forms.  
**Translation:** 

**[947.80s] English:** The notion of critic, like a food critic.  
**Translation:** 

**[949.88s] English:** No, I don't want touch emotion.  
**Translation:** 

**[952.12s] English:** That's an interesting question.  
**Translation:** 

**[953.88s] English:** Does emotion...  
**Translation:** 

**[954.88s] English:** Yeah.  
**Translation:** 

**[955.88s] English:** Yeah.  
**Translation:** 

**[956.88s] English:** The notion of Chris has always been the source of the human psychology, of the human experience.  
**Translation:** 

**[960.00s] English:** which seem to almost contradict intelligence and reason,  
**Translation:** 

**[965.40s] English:** like emotion, like fear, like love, all of those things,  
**Translation:** Vocabulary: contradict: 违背

**[971.16s] English:** are those not connected in any way to the space of ideas?  
**Translation:** 

**[977.56s] English:** That I don't know.  
**Translation:** 

**[979.54s] English:** I just want to be concentrated on a very simple story,  
**Translation:** 

**[986.18s] English:** on digit recognition.  
**Translation:** Vocabulary: digit: 数字

**[987.56s] English:** So you don't think you have to love and fear death  
**Translation:** 

**[990.38s] English:** in order to recognize digits?  
**Translation:** Vocabulary: digits: 阿拉伯数字

**[992.82s] English:** I don't know, because it's so complicated.  
**Translation:** 

**[997.04s] English:** It involves a lot of stuff which I never consider.  
**Translation:** 

**[1001.44s] English:** But I know about digit recognition,  
**Translation:** 

**[1005.08s] English:** and I know that for digit recognition,  
**Translation:** 

**[1010.70s] English:** to get records from small number of observations,  
**Translation:** 

**[1016.44s] English:** you need...  
**Translation:** 

**[1017.56s] English:** You need predicate.  
**Translation:** 

**[1019.42s] English:** But not special predicate for this problem,  
**Translation:** Vocabulary: predicate: 谓词

**[1023.62s] English:** but universal predicate which understand world of images.  
**Translation:** 

**[1028.62s] English:** Of visual information.  
**Translation:** 

**[1029.68s] English:** Visual, yeah.  
**Translation:** 

**[1031.42s] English:** But on the first step, they understand, say,  
**Translation:** 

**[1035.80s] English:** world of handwritten digits, or characters,  
**Translation:** 

**[1039.80s] English:** or something simple.  
**Translation:** 

**[1041.66s] English:** So like you said, symmetry is an interesting point.  
**Translation:** 

**[1043.68s] English:** No, that's what I think one of the predicate,  
**Translation:** Vocabulary: symmetry: 对称

**[1046.94s] English:** it's related to symmetry, to level of symmetry.  
**Translation:** 

**[1050.94s] English:** Okay, degree of symmetry.  
**Translation:** 

**[1052.12s] English:** So you think symmetry at the bottom is a universal notion,  
**Translation:** 

**[1057.20s] English:** and there's degrees of a single kind of symmetry,  
**Translation:** 

**[1061.50s] English:** or is there many kinds of symmetries?  
**Translation:** 

**[1064.14s] English:** Many kinds of symmetries.  
**Translation:** Vocabulary: symmetries: 对称性

**[1066.00s] English:** There is a symmetry, anti-symmetry, say, letter S.  
**Translation:** 

**[1072.34s] English:** So it has vertical anti-symmetry.  
**Translation:** 

**[1076.94s] English:** And it goes on and on, and on, and on, and on, and on, and on.  
**Translation:** 

**[1080.00s] English:** be diagonal symmetry vertical symmetry so when you when you cut vertically the letter s yeah  
**Translation:** Vocabulary: diagonal: 对角线的; vertical: 垂直的; vertically: 垂直地

**[1088.56s] English:** then the upper part and lower part in different directions yeah inverted along the y-axis yeah  
**Translation:** 

**[1098.72s] English:** but that's just like one example of symmetry right isn't there like right but there is a degree of  
**Translation:** 

**[1104.80s] English:** symmetry if you play all this linearity of stuff to to to do tangent distance but whatever i  
**Translation:** 

**[1115.68s] English:** described you can do you can have a degree of symmetry and that is what describing reason of  
**Translation:** 

**[1124.80s] English:** image it is the same as you will describe this image saying about  
**Translation:** 

**[1134.80s] English:** digits it has anti-symmetry digit three symmetric more or less look for symmetry  
**Translation:** Vocabulary: digit: 手指; digits: 数位; symmetric: 对称

**[1144.32s] English:** do you think such concepts like symmetry predicates like symmetry is it a hierarchical  
**Translation:** 

**[1152.48s] English:** set of concepts or are these independent distinct predicates that we want to discover a some set of  
**Translation:** Vocabulary: hierarchical: 层次结构; predicates: 谓词

**[1164.80s] English:** degree of symmetry is it it's not or is it not you see this is a very interesting example  
**Translation:** 

**[1172.08s] English:** of the category of symmetry of symmetry and you can this idea of symmetry make  
**Translation:** Vocabulary: symmetry: 对称性

**[1181.84s] English:** very general like degree of symmetry a degree of symmetry can be zero no symmetry at all  
**Translation:** 

**[1188.88s] English:** or degree of symmetry say more or less symmetrical  
**Translation:** Vocabulary: symmetrical: 对称的

**[1194.80s] English:** Diagonal and anti-symmetry is also considered.  
**Translation:** 

**[1200.00s] English:** of symmetry what about shape in general i mean symmetry is a fascinating notion but  
**Translation:** 

**[1205.56s] English:** no i'm talking about digit i would like to concentrate on all i would like to know predicate  
**Translation:** 

**[1213.00s] English:** for digital recognition yes but symmetry is not enough for digit recognition right it is not  
**Translation:** Vocabulary: predicate: 前提

**[1219.94s] English:** necessarily for digital recognition it helps to create invariant which will which you can use  
**Translation:** 

**[1230.00s] English:** when you will have examples for digital recognition you have regular problem of  
**Translation:** Vocabulary: invariant: 不变量

**[1237.26s] English:** digital recognition you have examples of the first class or second class plus you know that  
**Translation:** 

**[1242.58s] English:** there is this there exists concept of symmetry and you apply when you're looking for decision rule  
**Translation:** 

**[1249.58s] English:** you  
**Translation:** 

**[1249.92s] English:** will apply concept of symmetry of this level of symmetry which you estimate from  
**Translation:** 

**[1259.12s] English:** so let's let's talk everything is comes from weak convergence what is convergence what is  
**Translation:** 

**[1268.14s] English:** weak convergence what is strong convergence i'm sorry i'm going to do this to you what are  
**Translation:** Vocabulary: convergence: 收敛

**[1273.60s] English:** we converging from and to you're converging you would like to have a function  
**Translation:** 

**[1279.56s] English:** the function which uh say indicator function which indicate your digit five for example a  
**Translation:** Vocabulary: converging: 汇聚; digit: 数字; indicator: 指示器

**[1290.04s] English:** classification task let's talk only about classification so classification means you  
**Translation:** 

**[1295.90s] English:** will say whether this is a five or not or say which of the ten digits it is right right i would  
**Translation:** Vocabulary: digits: 十个数

**[1302.44s] English:** like to to to have these functions then  
**Translation:** 

**[1309.56s] English:** i have some examples i can consider property of these examples  
**Translation:** 

**[1320.04s] English:** i have some examples i can consider property of these examples  
**Translation:** 

**[1320.00s] English:** say, symmetry, and I can measure the level of symmetry for every digit.  
**Translation:** Vocabulary: symmetry: 对称性

**[1328.16s] English:** And then I can take an average from my training data, and I will consider only functions of  
**Translation:** 

**[1342.64s] English:** conditional probability, which I'm looking for in my decision rule, which, applying to  
**Translation:** Vocabulary: conditional: 条件概率

**[1351.88s] English:** digits, will give me the same average as I observed on training data.  
**Translation:** 

**[1362.08s] English:** So actually, this is a different level of description of what you want.  
**Translation:** 

**[1368.64s] English:** You want not just your show.  
**Translation:** 

**[1372.54s] English:** Not.  
**Translation:** 

**[1372.64s] English:** Not one digit.  
**Translation:** 

**[1374.04s] English:** You show this predicate, show general property of all digits which you have in mind.  
**Translation:** Vocabulary: predicate: 谓词

**[1383.68s] English:** If you have in mind digit three, it gives you property of digit three, and you select  
**Translation:** 

**[1391.88s] English:** as admissible set of function, only function, which keeps this property.  
**Translation:** Vocabulary: admissible: 可接受的

**[1396.92s] English:** You will not consider other functions.  
**Translation:** 

**[1400.72s] English:** So you immediately.  
**Translation:** 

**[1402.54s] English:** Looking for smaller subset of function.  
**Translation:** 

**[1404.88s] English:** That's what you mean by admissible functions.  
**Translation:** 

**[1406.98s] English:** Admissible function, exactly.  
**Translation:** 

**[1408.38s] English:** Which is still a pretty large.  
**Translation:** 

**[1410.90s] English:** For the number three, it's a large.  
**Translation:** 

**[1412.94s] English:** It is pretty large, but if you have one predicate.  
**Translation:** 

**[1416.34s] English:** Right.  
**Translation:** 

**[1416.54s] English:** But according to weak, there is a strong and weak convergence.  
**Translation:** Vocabulary: convergence: 趋同

**[1422.72s] English:** Strong convergence is convergence in function.  
**Translation:** 

**[1426.34s] English:** You're looking for the function, on one function, and you're looking for the another function.  
**Translation:** 

**[1431.86s] English:** Okay.  
**Translation:** 

**[1431.94s] English:** I got it.  
**Translation:** 

**[1433.22s] English:** That something is not right.  
**Translation:** 

**[1435.36s] English:** No one knows.  
**Translation:** 

**[1436.22s] English:** Yes.  
**Translation:** 

**[1436.48s] English:** This is not the case.  
**Translation:** 

**[1438.22s] English:** Yes, two perceive also no.  
**Translation:** 

**[1440.00s] English:** in any points, make a square, make an integral, and it should be small. That is convergence  
**Translation:** Vocabulary: integral: 积分; perceive: 感知

**[1446.66s] English:** in function. Suppose you have some function, any function. So I would say, I say that some  
**Translation:** 

**[1454.94s] English:** function converge to this function. If integral from square difference between them is small.  
**Translation:** Vocabulary: converge: 趋近

**[1462.96s] English:** That's the definition of strong convergence.  
**Translation:** 

**[1464.74s] English:** That definition of strong convergence.  
**Translation:** 

**[1465.74s] English:** Two functions, the integral of the difference is small.  
**Translation:** 

**[1468.80s] English:** It is convergence in functions. But you have different convergence in functionals.  
**Translation:** Vocabulary: functionals: 函数泛函

**[1476.64s] English:** You take any function, you take some function phi, and take inner product, this function is  
**Translation:** 

**[1483.58s] English:** f function, f0 function, which you want to find. And that gives you some value.  
**Translation:** 

**[1492.44s] English:** So you say that set of functions converge.  
**Translation:** 

**[1498.80s] English:** In inner product to this function, if this value of inner product converge to value f0,  
**Translation:** 

**[1509.94s] English:** that is for one phi. But weak convergence requires that it converge for any function  
**Translation:** 

**[1516.88s] English:** of Hilbert space. If it converge for any function of Hilbert space, then you will say that this is  
**Translation:** Vocabulary: hilbert: 希尔伯特空间

**[1526.50s] English:** weak convergence.  
**Translation:** 

**[1528.80s] English:** And you think that when you take integral, that is integral property of function.  
**Translation:** 

**[1536.12s] English:** For example, if you will take sine or cosine, it is coefficient of say Fourier expansion.  
**Translation:** 

**[1545.74s] English:** So if it converge for all coefficients of Fourier expansion, so under some condition, it converge  
**Translation:** Vocabulary: coefficient: 系数; coefficients: 系数; cosine: 余弦; fourier: 傅里叶

**[1555.18s] English:** to a function you're looking for.  
**Translation:** 

**[1558.80s] English:** audience means.  
**Translation:** 

**[1560.00s] English:** any property. Convergence not pointwise, but integral property of function. So weak convergence  
**Translation:** 

**[1570.88s] English:** means integral property of functions. When I talk about predicate, I would like to formulate  
**Translation:** Vocabulary: convergence: 收敛; integral: 积分; pointwise: 逐点; predicate: 谓词

**[1580.82s] English:** which integral properties I would like to have for convergence. If I will take one predicate  
**Translation:** 

**[1592.74s] English:** function which I measure property, if I will use one predicate and say I will consider  
**Translation:** 

**[1602.00s] English:** only function which give me the same value as with this predicate, I selecting set of  
**Translation:** 

**[1609.96s] English:** functions  
**Translation:** Vocabulary: selecting: 选择

**[1610.80s] English:** from functions which is admissible in the sense that function which I looking for in this set  
**Translation:** 

**[1619.58s] English:** of functions. Because by checking in training data, it gives the same.  
**Translation:** Vocabulary: admissible: 可接受的

**[1628.74s] English:** Yes, it always has to be connected to the training data in terms of...  
**Translation:** 

**[1632.60s] English:** Yeah, but property, you can know independent of training data. And this guy, prop,  
**Translation:** 

**[1640.80s] English:** prop, prop, prop.  
**Translation:** 

**[1641.80s] English:** Prop, prop, prop, prop, prop, prop, prop, prop, prop, prop, prop, prop, prop, prop, prop, prop, prop.  
**Translation:** 

**[1642.80s] English:** Yeah.  
**Translation:** 

**[1643.80s] English:** So that there is formal property, 31 property and you give...  
**Translation:** 

**[1644.80s] English:** A fairy tale, Russian fairy tale.  
**Translation:** 

**[1645.80s] English:** Right, but Russian fairy tale is not so interesting. More interesting that people  
**Translation:** 

**[1652.36s] English:** applied this to movies, to theatre, to different things and the same works, they're universal.  
**Translation:** 

**[1662.10s] English:** Well, so I would argue that there's a little bit of a difference between the kinds of things  
**Translation:** 

**[1668.10s] English:** that were applied to, which are essentially stories and kind of things that were applied  
**Translation:** 

**[1669.10s] English:** to, which are essentially stories.  
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

**[1670.80s] English:** and digit recognition it is the same story you you're saying digits there's a story within the  
**Translation:** 

**[1678.88s] English:** digit yeah  
**Translation:** Vocabulary: digit: 位数; digits: 多位数

**[1680.00s] English:** But my point is why I hope that it's possible to beat a record using not 60,000, but say 100 times less.  
**Translation:** 

**[1693.60s] English:** Because instead you will give predicates.  
**Translation:** Vocabulary: predicates: 谓词

**[1697.82s] English:** And you will select your decision not from a wide set of functions, but from a set of functions which keeps these predicates.  
**Translation:** 

**[1707.12s] English:** But predicate is not related just to digit recognition, like in Plato's case.  
**Translation:** Vocabulary: predicate: 谓词

**[1716.88s] English:** Do you think it's possible to automatically discover the predicates?  
**Translation:** 

**[1722.06s] English:** So you basically said that the essence of intelligence is the discovery of good predicates.  
**Translation:** 

**[1729.56s] English:** Yeah.  
**Translation:** 

**[1730.88s] English:** Now the natural question is, you know, that's what Einstein was good at doing.  
**Translation:** Vocabulary: einstein: 爱因斯坦

**[1737.12s] English:** He was good at doing in physics.  
**Translation:** 

**[1738.96s] English:** Can we make machines do these kinds of discovery of good predicates?  
**Translation:** 

**[1744.26s] English:** Or is this ultimately a human endeavor?  
**Translation:** 

**[1747.78s] English:** That I don't know.  
**Translation:** Vocabulary: endeavor: 努力

**[1748.94s] English:** I don't think that machine can do.  
**Translation:** 

**[1751.36s] English:** Because according to theory about weak convergence, any function from Hilbert space can be predicate.  
**Translation:** Vocabulary: convergence: 收敛; hilbert: 希尔伯特

**[1762.98s] English:** So you have infinite number of predicate.  
**Translation:** 

**[1766.68s] English:** And apparently...  
**Translation:** 

**[1767.12s] English:** And before, you don't know which predicate is good and which.  
**Translation:** 

**[1772.80s] English:** But whatever prop show and why people call it breakthrough,  
**Translation:** 

**[1779.96s] English:** that there is not too many predicate which cover most of situation happened in the world.  
**Translation:** 

**[1790.88s] English:** So there's a sea of predicates.  
**Translation:** 

**[1793.92s] English:** And most of the...  
**Translation:** 

**[1795.62s] English:** Only a small amount.  
**Translation:** 

**[1797.12s] English:** Are useful for the kinds of things that happen in the world.  
**Translation:** 

**[1800.00s] English:** I think that I would say only small part of predicate very useful useful all of  
**Translation:** 

**[1809.60s] English:** all of them only very few are what we should let's call them good predicates  
**Translation:** 

**[1815.24s] English:** very good predicate very good predicates so can we linger on it what's your  
**Translation:** Vocabulary: predicates: 谓词

**[1821.24s] English:** intuition why is it hard for a machine to discover good predicates I even in  
**Translation:** 

**[1828.00s] English:** my talk described how to do predicate how to find new predicate I'm not sure  
**Translation:** Vocabulary: intuition: 直觉; predicate: 谓词

**[1833.28s] English:** that it is very good what did you propose in your talk no in my talk I gave  
**Translation:** 

**[1839.44s] English:** example for diabetes when we achieve some percent so then we're looking  
**Translation:** Vocabulary: diabetes: 糖尿病

**[1847.26s] English:** from area where some sort of predicate which I formulate does not  
**Translation:** 

**[1858.00s] English:** keeps invariant so if it doesn't keep I retrain my data I select only function  
**Translation:** Vocabulary: invariant: 不变的

**[1869.38s] English:** which keeps is invariant in the way I did it I improve my performance I can  
**Translation:** 

**[1874.80s] English:** looking for this predicate I know technically have to do that and you can  
**Translation:** 

**[1880.12s] English:** of course do it using machine but I'm not sure that we will  
**Translation:** 

**[1888.00s] English:** construct the smartest predicate but this is the allow me to linger on it  
**Translation:** 

**[1893.70s] English:** because that's the essence that's the challenge that is artificial that's  
**Translation:** 

**[1897.84s] English:** that's the human level intelligence that we seek is the discovery of these good  
**Translation:** 

**[1902.82s] English:** predicates you've talked about deep learning as a way to the predicates they  
**Translation:** 

**[1908.46s] English:** use and the functions are mediocre we can find better ones let's talk about  
**Translation:** Vocabulary: mediocre: 平庸

**[1915.76s] English:** deep learning sure let's do it  
**Translation:** 

**[1918.00s] English:** I know only  
**Translation:** 

**[1920.00s] English:** young slickoon convolutional network and what else i don't know and it's a very simple convolution  
**Translation:** 

**[1927.84s] English:** there's not much else left and right yes i can do it like that one this one predicate it is  
**Translation:** Vocabulary: convolution: 卷积; convolutional: 卷积的

**[1934.56s] English:** convolution is a single predicate it's single it's it's single predicate yes it is you know exactly  
**Translation:** 

**[1943.52s] English:** you take the derivative for translation and predicate this should should be kept  
**Translation:** Vocabulary: derivative: 导数

**[1950.96s] English:** so that's a single predicate but humans discovered that one or at least  
**Translation:** 

**[1955.60s] English:** not that is a realistic not too many predicators and that is big story because jan did it  
**Translation:** Vocabulary: predicate: 主谓词; predicators: 主谓项

**[1962.24s] English:** 25 years ago and nothing so clear was added to to deep network and then i don't understand  
**Translation:** 

**[1973.68s] English:** uh why we should talk about deep network instead of talking about piecewise linear functions  
**Translation:** Vocabulary: piecewise: 分段线性

**[1981.12s] English:** which keeps this predicate well the you know a counter argument is  
**Translation:** 

**[1987.20s] English:** that maybe the amount of predicates necessary to solve general intelligence  
**Translation:** Vocabulary: predicates: 前提

**[1994.32s] English:** say in space of images doing efficient recognition of uh handwritten digits is very small  
**Translation:** 

**[2002.24s] English:** and  
**Translation:** Vocabulary: digits: 手写字符; handwritten: 手写

**[2003.52s] English:** so we shouldn't be so obsessed about finding we'll find other good predicates like convolution  
**Translation:** 

**[2009.60s] English:** for example you know there has been other advancements like um if you look at the work  
**Translation:** Vocabulary: advancements: 进步

**[2016.16s] English:** with attention there's attentional mechanisms in especially used in natural language  
**Translation:** 

**[2022.24s] English:** focusing the the network's ability to uh to learn at which part of the input to look at  
**Translation:** Vocabulary: attentional: 注意力的

**[2027.52s] English:** the thing is there's other things besides predicates that are important for the actual  
**Translation:** 

**[2033.28s] English:** engineering mechanism of showing how much you can really do given such these predicates  
**Translation:** 

**[2040.00s] English:** I mean, that's essentially the work of deep learning is constructing architectures that are able to be given the training data to be able to converge towards a function that can approximate, can generalize well.  
**Translation:** 

**[2062.44s] English:** It's an engineering problem.  
**Translation:** Vocabulary: approximate: 近似; converge: 收敛; generalize: 泛化

**[2063.90s] English:** Yeah, I understand.  
**Translation:** 

**[2065.94s] English:** But let's talk not on emotional level, but on a mathematical level.  
**Translation:** Vocabulary: mathematical: 数学的

**[2071.78s] English:** You have set of piecewise linear functions.  
**Translation:** 

**[2076.02s] English:** It is all possible neural networks.  
**Translation:** 

**[2081.50s] English:** It's just piecewise linear functions.  
**Translation:** 

**[2084.00s] English:** There's many, many pieces.  
**Translation:** 

**[2085.28s] English:** Large, large number of piecewise linear functions.  
**Translation:** 

**[2087.10s] English:** Okay, exactly.  
**Translation:** 

**[2088.44s] English:** Very large.  
**Translation:** 

**[2089.38s] English:** Very large.  
**Translation:** 

**[2090.14s] English:** Almost feels like too large.  
**Translation:** 

**[2091.64s] English:** It's still simpler than...  
**Translation:** 

**[2094.78s] English:** Say, convolutional.  
**Translation:** 

**[2095.98s] English:** Then, reproducing kernel Hilbert space, which have a Hilbert set of functions.  
**Translation:** Vocabulary: convolutional: 卷积的; hilbert: 希尔伯特; kernel: 核函数; reproducing: 再生的

**[2100.80s] English:** What's Hilbert space?  
**Translation:** 

**[2102.90s] English:** It's space with infinite number of coordinates, say, or function for expansion, something like that.  
**Translation:** 

**[2111.72s] English:** So, it's much richer.  
**Translation:** 

**[2114.44s] English:** So, and when I'm talking about closed-form solution, I'm talking about this set of functions.  
**Translation:** 

**[2121.18s] English:** Not piecewise linear set, which is...  
**Translation:** 

**[2123.90s] English:** Particular case of...  
**Translation:** Vocabulary: piecewise: 分段的

**[2128.90s] English:** It's a small part.  
**Translation:** 

**[2130.88s] English:** So, neural networks is a small part of the space of functions you're talking about.  
**Translation:** Vocabulary: neural: 神经的

**[2135.90s] English:** Say, small set of functions.  
**Translation:** 

**[2139.02s] English:** Let me take that.  
**Translation:** 

**[2140.46s] English:** But it is fine.  
**Translation:** 

**[2142.00s] English:** It is fine.  
**Translation:** 

**[2142.74s] English:** I don't want to discuss the small or big.  
**Translation:** 

**[2146.58s] English:** You take advantage.  
**Translation:** 

**[2147.90s] English:** So, you have some set of functions.  
**Translation:** 

**[2150.64s] English:** So, now, when you're trying to create architecture...  
**Translation:** 

**[2153.90s] English:** You would like to create admissible set of functions.  
**Translation:** 

**[2158.90s] English:** All your tricks.  
**Translation:** Vocabulary: admissible: 可接受的

**[2160.00s] English:** to use not all functions,  
**Translation:** 

**[2163.06s] English:** but some subset of this set of functions.  
**Translation:** 

**[2167.24s] English:** Say, when you're introducing convolutional net,  
**Translation:** 

**[2170.04s] English:** it is a way to make this subset useful for you.  
**Translation:** 

**[2176.06s] English:** But from my point of view,  
**Translation:** 

**[2178.94s] English:** convolutional, it is something  
**Translation:** 

**[2181.94s] English:** you want to keep some invariance,  
**Translation:** 

**[2184.84s] English:** say, translation invariance.  
**Translation:** Vocabulary: invariance: 不变性

**[2186.30s] English:** But now, if you understand this,  
**Translation:** 

**[2191.74s] English:** and you cannot explain  
**Translation:** Vocabulary: cannot: 不能

**[2194.62s] English:** on the level of ideas  
**Translation:** 

**[2197.46s] English:** what neural network does,  
**Translation:** 

**[2201.18s] English:** you should agree that it is much better  
**Translation:** 

**[2204.20s] English:** to have a set of functions.  
**Translation:** 

**[2206.62s] English:** And they say, this set of functions  
**Translation:** 

**[2208.68s] English:** should be admissible.  
**Translation:** 

**[2210.92s] English:** It must keep this invariant,  
**Translation:** 

**[2212.82s] English:** this invariant, and that invariant.  
**Translation:** Vocabulary: invariant: 不变量

**[2214.54s] English:** You know that,  
**Translation:** 

**[2215.98s] English:** as soon as you incorporate new invariants,  
**Translation:** Vocabulary: incorporate: 吸收; invariants: 不变量

**[2219.14s] English:** set of functions,  
**Translation:** 

**[2219.92s] English:** because smaller and smaller and smaller.  
**Translation:** 

**[2222.24s] English:** But all the invariants are specified  
**Translation:** 

**[2223.90s] English:** by you, the human.  
**Translation:** Vocabulary: specified: 指定

**[2226.68s] English:** Yeah.  
**Translation:** 

**[2227.38s] English:** But what I hope,  
**Translation:** 

**[2229.66s] English:** that there is a standard predicate,  
**Translation:** 

**[2232.50s] English:** like prop show.  
**Translation:** Vocabulary: predicate: 谓词

**[2235.88s] English:** That's what I want to find  
**Translation:** 

**[2237.96s] English:** for digit recognition.  
**Translation:** Vocabulary: digit: 数字

**[2239.66s] English:** If we start, it is completely new area  
**Translation:** 

**[2242.80s] English:** of what is intelligence about  
**Translation:** 

**[2244.42s] English:** on the level.  
**Translation:** 

**[2245.14s] English:** So, starting from plot as idea.  
**Translation:** 

**[2248.24s] English:** What is vault of ideas?  
**Translation:** 

**[2250.64s] English:** So, and I believe that it's not too many.  
**Translation:** Vocabulary: vault: 拱顶

**[2254.64s] English:** Yeah.  
**Translation:** 

**[2256.14s] English:** But, you know, it is amusing  
**Translation:** 

**[2258.74s] English:** that mathematician doing something  
**Translation:** 

**[2260.64s] English:** in neural network, in general function,  
**Translation:** Vocabulary: mathematician: 数学家; neural: 神经的

**[2263.64s] English:** but people from literature, from art,  
**Translation:** 

**[2266.64s] English:** they use this all the time.  
**Translation:** 

**[2269.14s] English:** That's right.  
**Translation:** 

**[2270.14s] English:** Invariance saying, say, it is great,  
**Translation:** 

**[2274.70s] English:** how people describe music,  
**Translation:** 

**[2277.00s] English:** we should learn from that.  
**Translation:** 

**[2278.80s] English:** And something,  
**Translation:** 

**[2280.00s] English:** this level but so why Vladimir probe who was just theoretical who studied  
**Translation:** 

**[2289.78s] English:** theoretical literature he found that you know let me throw that right back at you  
**Translation:** 

**[2295.12s] English:** because there's a little bit of a that's less mathematical and more emotional  
**Translation:** 

**[2299.82s] English:** philosophical Vladimir prop I mean he wasn't doing math no and you just said  
**Translation:** 

**[2307.76s] English:** another emotional statement which is you believe that this Plato world of  
**Translation:** 

**[2313.44s] English:** ideas is small I hope I hope dude no do you do what's your intuition though if  
**Translation:** 

**[2322.26s] English:** we can linger on it yeah you know about this not just small or big I know  
**Translation:** Vocabulary: intuition: 直觉

**[2328.76s] English:** exactly then when I introducing some predicate  
**Translation:** 

**[2335.88s] English:** I decrease  
**Translation:** 

**[2337.52s] English:** something  
**Translation:** 

**[2337.74s] English:** of functions but my goal to decrease set of function much by as much as possible by as  
**Translation:** 

**[2345.42s] English:** much as possible good predicate which which does this then i should choose next predicate which  
**Translation:** 

**[2353.50s] English:** does which decrease set as much as possible so set of good predicate it is such that they decrease  
**Translation:** Vocabulary: predicate: 谓词

**[2362.62s] English:** this amount of admissible functions so if each good predicate significantly reduces the set of  
**Translation:** 

**[2371.34s] English:** admissible functions that there naturally should not be that many yeah predicates no but but  
**Translation:** Vocabulary: admissible: 允许的; predicates: 谓词

**[2378.46s] English:** if you reduce very well the vc dimension of the function of admissible set of function is small  
**Translation:** 

**[2386.70s] English:** and you need not too much training data to to do well  
**Translation:** Vocabulary: dimension: 维度

**[2392.94s] English:** and vc dimension by the way is some measure of capacity of this set of functions right  
**Translation:** 

**[2399.26s] English:** roughly speaking  
**Translation:** 

**[2400.00s] English:** have many functions in this set. You're decreasing, decreasing, and it makes it easy for you to find  
**Translation:** 

**[2407.60s] English:** functions you're looking for. The most important part is to create a good admissible set of  
**Translation:** 

**[2414.48s] English:** functions. There are many ways, but the good predicate is such that it can do that. For this  
**Translation:** 

**[2427.36s] English:** duck, you should know a little bit about duck. What are the three fundamental laws of ducks?  
**Translation:** 

**[2435.28s] English:** Looks like a duck, swims like a duck, and quacks like a duck.  
**Translation:** 

**[2438.24s] English:** You should know something about ducks to be able to-  
**Translation:** Vocabulary: quacks: 叫

**[2441.04s] English:** Not necessarily. Looks like, say, horse. It's also good.  
**Translation:** 

**[2447.76s] English:** It generalizes from ducks.  
**Translation:** Vocabulary: generalizes: 概括外推

**[2449.68s] English:** Yes, and talk like, and make sound like horse or something, and run like horse, and move like horse.  
**Translation:** 

**[2457.36s] English:** It is general. It is general predicate that this applied to duck. But for duck, you can say,  
**Translation:** 

**[2467.12s] English:** play chess like duck.  
**Translation:** 

**[2469.84s] English:** You cannot say play chess like duck.  
**Translation:** 

**[2471.52s] English:** Why not?  
**Translation:** 

**[2472.88s] English:** You're saying you can, but that would not be a good-  
**Translation:** 

**[2475.68s] English:** No, you will not reduce a lot of functions.  
**Translation:** 

**[2478.16s] English:** You will not do, yeah, you would not reduce the set of functions.  
**Translation:** 

**[2481.60s] English:** So, the story is, formal story, mathematical story,  
**Translation:** 

**[2487.36s] English:** you can use any function you want as a predicate. But some of them are good, some of them are not,  
**Translation:** Vocabulary: mathematical: 数学的; predicate: 谓词

**[2493.12s] English:** because some of them reduce a lot of functions to admissible set. Some of them-  
**Translation:** 

**[2499.68s] English:** But the question is, and I'll probably keep asking this question, but how do we find such,  
**Translation:** Vocabulary: admissible: 可接受的

**[2505.60s] English:** what's your intuition? Handwritten recognition. How do we find the answer to your challenge?  
**Translation:** 

**[2512.48s] English:** Yeah, yeah. I understand it like that. I understand volt.  
**Translation:** Vocabulary: handwritten: 手写; intuition: 直觉

**[2518.08s] English:** What defined?  
**Translation:** 

**[2519.04s] English:** What it means.  
**Translation:** 

**[2520.00s] English:** a new predicate yeah like guy who understand music can say this word which he described him  
**Translation:** 

**[2527.36s] English:** when he listened to music he understand music he use not too many different oh you can do like prop  
**Translation:** 

**[2535.44s] English:** you can make collection what he talking about music about this about that it's not too many  
**Translation:** 

**[2542.00s] English:** different situations he described because we mentioned vladimir proper bunch let me just  
**Translation:** 

**[2547.28s] English:** mention there's a so there's a sequence of of uh 31 structural notions that are common in stories  
**Translation:** 

**[2556.80s] English:** and i think you call it units units and i think they resonate i mean it starts just to give an  
**Translation:** 

**[2562.96s] English:** example absentian a member of the hero's community a family leaves the security of the home environment  
**Translation:** 

**[2568.72s] English:** then it goes to the interdiction a forbidding edict or command is passed upon the hero  
**Translation:** 

**[2574.40s] English:** don't go there don't do this the heroes  
**Translation:** 

**[2577.28s] English:** against some action then step three violate violation of interdiction brace you know break  
**Translation:** Vocabulary: brace: 支撑; interdiction: 禁令

**[2585.36s] English:** the rules break out on your own then reconnaissance the villain makes an effort to attain  
**Translation:** 

**[2590.80s] English:** knowledge needing to fulfill their plot so on it goes on like this ends uh ends in a wedding  
**Translation:** Vocabulary: reconnaissance: 侦察; villain: 恶棍

**[2597.92s] English:** number 31 yeah happily ever after no he he just gave description of all situations he understands  
**Translation:** 

**[2606.64s] English:** this vault  
**Translation:** Vocabulary: vault: 金库

**[2608.00s] English:** of folktales yeah not for not for stories and this story is not in just folktales the stories in in  
**Translation:** 

**[2618.08s] English:** detective serials as well and probably in our lives we probably live read this at the end they  
**Translation:** Vocabulary: folktales: 民间故事

**[2625.76s] English:** they they they wrote that this predicate is good for different situation from movie from for movie  
**Translation:** 

**[2637.28s] English:** by the way there's also criticism  
**Translation:** Vocabulary: predicate: 谓语

**[2640.00s] English:** right there's an other way to interpret narratives from Claude Levi Strauss I  
**Translation:** 

**[2649.72s] English:** don't know I am NOT in this business and I know it's theoretical literature but  
**Translation:** Vocabulary: interpret: 解释

**[2654.50s] English:** it's looking at paradise it's always yeah yeah but at least there is a units  
**Translation:** 

**[2662.88s] English:** it's not too many units that can describe but this guy probably gives  
**Translation:** 

**[2668.80s] English:** another units or another way exactly another another another set of units  
**Translation:** 

**[2673.96s] English:** another set of predicates it doesn't matter who but they exist probably my my  
**Translation:** Vocabulary: predicates: 谓词

**[2682.54s] English:** question is whether given those units whether without our human brains to  
**Translation:** 

**[2687.82s] English:** interpret these units they would still hold as much power as they have meaning  
**Translation:** 

**[2693.82s] English:** are those units enough when we give them to the an alien species  
**Translation:** 

**[2698.38s] English:** let  
**Translation:** Vocabulary: alien: 外星的

**[2698.64s] English:** let  
**Translation:** 

**[2698.74s] English:** let  
**Translation:** 

**[2698.78s] English:** , let me ask you do you understand digit images no I don't know when you  
**Translation:** 

**[2708.92s] English:** can recognize these digit images it means that you understand you understand  
**Translation:** Vocabulary: digit: 数字

**[2715.06s] English:** characters you understand no no no no I I it's the it's the imitation versus  
**Translation:** 

**[2724.46s] English:** understanding question because I don't understand the mechanism by which you  
**Translation:** Vocabulary: imitation: 模仿

**[2728.72s] English:** can find proof let's see what details is something is wrong like this is the  
**Translation:** 

**[2731.88s] English:** vertical and that's the artwork some of the markings are  
**Translation:** Vocabulary: artwork: 艺术品; vertical: 垂直的

**[2739.90s] English:** there can we actually make an image yes I just didn't know how you do that  
**Translation:** 

**[2745.56s] English:** but I came up with a nice idea how you can do that which I know I'm not talking  
**Translation:** 

**[2747.62s] English:** about I'm talking about predicates you understand that it involves symmetry  
**Translation:** 

**[2752.80s] English:** maybe structure maybe something that I cannot formulate i just was able to find  
**Translation:** Vocabulary: cannot: 不能; symmetry: 对称

**[2756.86s] English:** that's a very powerful predicate. My question is,  
**Translation:** 

**[2760.00s] English:** is is there a lot more going on that we're not able to introspect maybe I need to be able to  
**Translation:** Vocabulary: introspect: 自我反省; predicate: 谓词

**[2767.74s] English:** understand a huge amount in the world of ideas thousands of predicates millions of predicates  
**Translation:** 

**[2778.30s] English:** in order to do hand recognition I don't think so so you're you're not both your hope and your  
**Translation:** 

**[2785.92s] English:** intuition let me explain enough you're using digits you're using examples as well theory says  
**Translation:** 

**[2795.16s] English:** that if you will use all possible functions from Hilda space all possible predicate you don't need  
**Translation:** Vocabulary: digits: 数字; intuition: 直觉

**[2806.94s] English:** training data you just will have admissible set of function which contain one function  
**Translation:** 

**[2815.92s] English:** yes so the trade-off is when you're not using all predicates you're only using a few good  
**Translation:** Vocabulary: admissible: 可接受的; predicates: 谓词

**[2822.46s] English:** predicates you need to have some training data yes exactly the more the more good  
**Translation:** 

**[2827.44s] English:** predicates you have the less training data exactly that is intelligent still okay I'm  
**Translation:** 

**[2835.00s] English:** going to keep asking the same dumb question handwritten recognition to solve the challenge  
**Translation:** 

**[2840.16s] English:** you kind of propose a challenge that says we should be able to get state-of-the-art MNIST  
**Translation:** 

**[2845.32s] English:** arrow  
**Translation:** 

**[2845.92s] English:** rates by using very few 60 maybe fewer examples per digit what kind of predicates do you think  
**Translation:** Vocabulary: digit: 位数

**[2855.34s] English:** it was that is the challenge so people who will solve this problem they will answer they will  
**Translation:** 

**[2861.04s] English:** answer do you think they'll be able to answer it in a human explainable way  
**Translation:** 

**[2867.64s] English:** they just need to write function that's it but so can that function be written I guess  
**Translation:** 

**[2873.82s] English:** by an  
**Translation:** 

**[2875.92s] English:** automated reasoning system whether we're talking about  
**Translation:** 

**[2880.00s] English:** neural network learning a particular function or another mechanism?  
**Translation:** Vocabulary: automated: 自动化; neural: 神经

**[2884.96s] English:** No. I'm not against neural network. I'm against admissible set of function which create  
**Translation:** 

**[2892.40s] English:** neural network. You did it by hand. You don't do it by invariance, by predicate, by reason.  
**Translation:** Vocabulary: invariance: 不变性; predicate: 谓词

**[2904.40s] English:** But neural networks can then do the reverse step of helping you  
**Translation:** 

**[2908.24s] English:** find a function. The task of a neural network is to find a disentangled representation,  
**Translation:** Vocabulary: disentangled: 分离的

**[2917.20s] English:** for example, is to find that one predicate function that really captures some kind of  
**Translation:** 

**[2924.40s] English:** essence. One, not the entire essence, but one very useful essence of this particular  
**Translation:** 

**[2930.56s] English:** visual space. Do you think that's possible? Listen, I'm grasping, hoping there's an  
**Translation:** 

**[2937.68s] English:** automated  
**Translation:** Vocabulary: grasping: 勉强理解

**[2938.24s] English:** way to find good predicates, right? So the question is, what are the mechanisms  
**Translation:** 

**[2942.88s] English:** of finding good predicates, ideas that you think we should pursue? A young grad student  
**Translation:** Vocabulary: predicates: 谓词

**[2948.88s] English:** listening right now. I gave example. So find situation  
**Translation:** 

**[2956.48s] English:** where predicate, which you're suggesting, don't create invariant. It's like in physics.  
**Translation:** Vocabulary: invariant: 不变量

**[2968.80s] English:** Find situation where existing theory cannot explain it.  
**Translation:** 

**[2977.12s] English:** Find situation where the existing theory can't explain it.  
**Translation:** Vocabulary: cannot: 无法解释的情况

**[2979.28s] English:** Theory cannot explain this.  
**Translation:** 

**[2980.88s] English:** So you're finding contradictions.  
**Translation:** Vocabulary: contradictions: 矛盾

**[2982.64s] English:** Find contradiction, and then remove this contradiction. But in my case,  
**Translation:** 

**[2987.52s] English:** what means contradiction, you find function which, if you will use this function, you're not keeping  
**Translation:** Vocabulary: contradiction: 矛盾

**[2994.00s] English:** invariants. This is-  
**Translation:** 

**[2997.04s] English:** So really, the process of-  
**Translation:** Vocabulary: invariants: 不变量

**[2998.22s] English:** The process of discovering contradictions.  
**Translation:** 

**[3000.00s] English:** yeah it is like in physics find situation where you have contradiction for one of the property  
**Translation:** 

**[3011.70s] English:** for one of the predicate then include this predicate making invariance and solve against  
**Translation:** 

**[3019.80s] English:** this problem now you don't have contradiction but it is not the best way probably I don't know  
**Translation:** Vocabulary: invariance: 不变性; predicate: 谓词

**[3029.40s] English:** to looking for predicate that's just one way okay that no no it is brute force way the brute force  
**Translation:** 

**[3036.24s] English:** way what about the ideas of some what big umbrella term of symbolic AI these what in the 80s with  
**Translation:** Vocabulary: brute: 笨拙; symbolic: 符号

**[3047.52s] English:** expert systems sort of logic reasoning based systems is there hope there to find some through  
**Translation:** 

**[3057.12s] English:** sort of deductive reasons  
**Translation:** Vocabulary: deductive: 演绎推理

**[3059.40s] English:** reasoning to find good predicates I don't think so I think that just logic is not enough it's kind  
**Translation:** 

**[3072.48s] English:** of a compelling notion though you know that when smart people sit in a room and reason through  
**Translation:** Vocabulary: compelling: 有说服力; predicates: 谓词

**[3078.48s] English:** things it seems compelling and making our machines do the same is also compelling so everything is  
**Translation:** 

**[3087.00s] English:** very simple  
**Translation:** 

**[3089.40s] English:** when you have infinite number of predicate you can choose  
**Translation:** 

**[3096.66s] English:** the the function you want you have invariants and you can kill the function you want but  
**Translation:** 

**[3104.70s] English:** you have to have a not too many invariants to solve the problem  
**Translation:** 

**[3116.10s] English:** so and have from infinite number of function  
**Translation:** 

**[3119.64s] English:** before and after for instance you know in some certain виbe do you have a mean and you have a  
**Translation:** 

**[3126.16s] English:** body and then you have to recognize this as the predicate for the society and imagine something  
**Translation:** 

**[3130.68s] English:** else set that and you can do trivial things for example you can do  
**Translation:** 

**[3133.60s] English:** something else set something like you will give только an integer punya instead of using integer  
**Translation:** Vocabulary: integer: 整数

**[3139.22s] English:** and then you can are you going to day when you are we are going to put everything in perfect  
**Translation:** 

**[3143.40s] English:** position in a colloquial sense because people inflict the fact that you can Java and I am going to return  
**Translation:** Vocabulary: colloquial: 口语; inflict: 强加

**[3146.92s] English:** to you and I also had trouble understanding most of the part-time jobs at large I was sort of I just  
**Translation:** 

**[3120.00s] English:** select finite number and hopefully small number of functions, which is good enough to extract  
**Translation:** Vocabulary: finite: 有限的

**[3134.10s] English:** small set of admissible functions.  
**Translation:** 

**[3138.00s] English:** So they will be admissible, it's for sure, because every function just decrease set of  
**Translation:** Vocabulary: admissible: 可接受的

**[3143.32s] English:** function and leaving it admissible, but it will be small.  
**Translation:** 

**[3146.92s] English:** But why do you think logic-based systems can't help, intuition, not-  
**Translation:** Vocabulary: intuition: 直觉

**[3155.10s] English:** Because you should know reality.  
**Translation:** 

**[3157.86s] English:** You should know life.  
**Translation:** 

**[3159.68s] English:** This guy like Prob, he knows something and he tried to put in invariant his understanding.  
**Translation:** 

**[3168.60s] English:** But that's the human, yeah, see, you're putting too much value into Vladimir Prob's  
**Translation:** Vocabulary: invariant: 不变量

**[3176.62s] English:** knowing something.  
**Translation:** 

**[3177.62s] English:** No, it is-  
**Translation:** 

**[3178.62s] English:** Am I being misunderstood?  
**Translation:** 

**[3179.62s] English:** The story is that what means you know life?  
**Translation:** Vocabulary: misunderstood: 被误解

**[3184.56s] English:** What it means-  
**Translation:** 

**[3185.56s] English:** You know common sense.  
**Translation:** 

**[3186.86s] English:** No, no.  
**Translation:** 

**[3188.46s] English:** You know something.  
**Translation:** 

**[3190.62s] English:** Common sense, it is some rules.  
**Translation:** 

**[3193.48s] English:** You think so?  
**Translation:** 

**[3195.08s] English:** Common sense is simply rules?  
**Translation:** 

**[3197.44s] English:** Common sense is, it's mortality, it's fear of death, it's love, it's spirituality.  
**Translation:** 

**[3204.80s] English:** Yeah.  
**Translation:** 

**[3205.80s] English:** Yeah.  
**Translation:** 

**[3206.62s] English:** It's spirituality, it's happiness and sadness.  
**Translation:** 

**[3210.94s] English:** All of it is tied up into understanding gravity, which is what we think of as common sense.  
**Translation:** Vocabulary: gravity: 引力

**[3216.62s] English:** I don't ready to discuss so wide.  
**Translation:** 

**[3219.64s] English:** I want to discuss, understand digit recognition.  
**Translation:** Vocabulary: digit: 数字

**[3222.86s] English:** Any time I bring up love and death, you bring it back to digit recognition.  
**Translation:** 

**[3230.06s] English:** I like it.  
**Translation:** 

**[3231.06s] English:** Yeah.  
**Translation:** 

**[3232.06s] English:** No, you know, it is durable because there is a challenge-  
**Translation:** Vocabulary: durable: 耐用

**[3234.56s] English:** Yeah.  
**Translation:** 

**[3235.56s] English:** I mean, you can have a bunch of love and death and all that.  
**Translation:** 

**[3238.96s] English:** And if any of you want to, like me, like for I'm just saying that this is just my family.  
**Translation:** 

**[3239.88s] English:** Yeah.  
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

**[3240.00s] English:** student concentrate on this work i will suggest something to solve you mean handwritten recognition  
**Translation:** 

**[3246.72s] English:** yeah it's a beautifully simple elegant and yet i think that i know invariance which will solve this  
**Translation:** Vocabulary: handwritten: 手写; invariance: 不变性

**[3253.28s] English:** you do i think so yes but it is not universal it is maybe i want some universal invariance which  
**Translation:** 

**[3264.48s] English:** are good not only for digit recognition for image understanding  
**Translation:** 

**[3270.56s] English:** so let me ask how hard do you think is 2d image understanding  
**Translation:** 

**[3278.24s] English:** so if we we can kind of intuit handwritten recognition  
**Translation:** Vocabulary: intuit: 直观理解

**[3283.68s] English:** how big of a step leap journey is it from that if i gave you good if i solved your challenge  
**Translation:** 

**[3291.76s] English:** for handwriting recognition how long would my  
**Translation:** 

**[3294.48s] English:** journey then be from that to understanding more general natural images immediately you will  
**Translation:** 

**[3300.56s] English:** understand this as soon as you will make a record because it is not for free as soon as you will  
**Translation:** 

**[3309.52s] English:** create several invariants which will help you to get the same performance that the best neural net  
**Translation:** 

**[3321.60s] English:** did using hundred time maybe  
**Translation:** Vocabulary: invariants: 不变量; neural: 神经

**[3324.48s] English:** more than 100 times less examples you have to have something smart to do that and you're saying  
**Translation:** 

**[3332.08s] English:** that that is invariant it is predicated because you should put some idea how to do that  
**Translation:** Vocabulary: invariant: 不变的; predicated: 基于

**[3339.28s] English:** but okay let me just pause maybe it's a trivial point maybe not but handwritten recognition  
**Translation:** 

**[3347.12s] English:** feels like a 2d two-dimensional problem and it seems like how much complicated it is  
**Translation:** 

**[3354.48s] English:** is the fact that most images are a projection of a three-dimensional world.  
**Translation:** 

**[3360.00s] English:** onto a 2D plane, it feels like for a three-dimensional world,  
**Translation:** 

**[3365.48s] English:** we need to start understanding common sense in order to understand an image.  
**Translation:** 

**[3371.54s] English:** It's no longer visual shape and symmetry.  
**Translation:** Vocabulary: symmetry: 对称

**[3377.40s] English:** It's having to start to understand concepts, understand life.  
**Translation:** 

**[3382.16s] English:** Yeah.  
**Translation:** 

**[3384.36s] English:** You're talking that there are different environments, different predicates.  
**Translation:** 

**[3388.30s] English:** Yeah.  
**Translation:** Vocabulary: environments: 环境; predicates: 前提

**[3388.54s] English:** And potentially a much larger number.  
**Translation:** 

**[3392.54s] English:** You know, maybe, but let's start from simple.  
**Translation:** 

**[3396.34s] English:** Yeah, but you said that it would be immediate.  
**Translation:** 

**[3398.16s] English:** No, you know, I cannot think about things which I don't understand.  
**Translation:** Vocabulary: cannot: 不能

**[3402.88s] English:** This I understand, but I'm sure that I don't understand everything there.  
**Translation:** 

**[3408.40s] English:** Yeah, that's the difference.  
**Translation:** 

**[3409.14s] English:** It's like Einstein said, do as simple as possible, but not simpler.  
**Translation:** 

**[3414.18s] English:** And that is exact case.  
**Translation:** Vocabulary: einstein: 爱因斯坦

**[3416.48s] English:** With handwritten.  
**Translation:** 

**[3417.18s] English:** With handwritten.  
**Translation:** Vocabulary: handwritten: 亲笔书写

**[3418.54s] English:** Yeah, but that's the difference between you and I.  
**Translation:** 

**[3421.78s] English:** I welcome and enjoy thinking about things I completely don't understand.  
**Translation:** 

**[3429.66s] English:** Because to me, it's a natural extension without having solved handwritten recognition  
**Translation:** 

**[3434.68s] English:** to wonder how difficult is the next step of understanding 2D, 3D images.  
**Translation:** 

**[3445.34s] English:** Because ultimately, while the science...  
**Translation:** 

**[3448.54s] English:** The science of intelligence is fascinating, it's also fascinating to see how that maps  
**Translation:** 

**[3452.62s] English:** to the engineering of intelligence.  
**Translation:** 

**[3454.84s] English:** And recognizing handwritten digits is not, doesn't help you, it might, it may not help  
**Translation:** Vocabulary: digits: 手写数

**[3462.80s] English:** you with the problem of general intelligence.  
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

**[3472.60s] English:** It might very much.  
**Translation:** 

**[3473.60s] English:** But I would like to make a remark.  
**Translation:** 

**[3474.60s] English:** Yes.  
**Translation:** 

**[3475.60s] English:** I start not from very primitive problem.  
**Translation:** 

**[3476.60s] English:** Yeah.  
**Translation:** 

**[3477.60s] English:** Yeah.  
**Translation:** 

**[3478.54s] English:** That's what I think.  
**Translation:** 

**[3479.54s] English:** Yeah.  
**Translation:** 

**[3480.54s] English:** And the scale that helps make one stand in it.  
**Translation:** 

**[3481.54s] English:** Yeah.  
**Translation:** 

**[3482.54s] English:** Yeah.  
**Translation:** 

**[3483.54s] English:** Although, you might notice, you know, like, when you go through lab don't recognize  
**Translation:** 

**[3484.54s] English:** that by tells you that it's that you go in and take a麵 and you don't have to  
**Translation:** 

**[3485.54s] English:** do anything else.  
**Translation:** 

**[3486.54s] English:** Yeah.  
**Translation:** 

**[3487.54s] English:** You can isn't one step you have to do or you just become like this, you know,  
**Translation:** 

**[3488.54s] English:** really reptile.  
**Translation:** Vocabulary: reptile: 冷血动物

**[3489.54s] English:** That's right.  
**Translation:** 

**[3490.54s] English:** Cause you could mean other parts of it and give a.  
**Translation:** 

**[3491.54s] English:** Yeah.  
**Translation:** 

**[3492.54s] English:** Yeah.  
**Translation:** 

**[3493.54s] English:** It's entirely up toanged person on this term politics, and yeah, that makes sense.  
**Translation:** 

**[3494.54s] English:** Yeah.  
**Translation:** 

**[3495.54s] English:** Praise, thank you very much.  
**Translation:** 

**[3496.54s] English:** So today you've done a fine job.  
**Translation:** 

**[3497.54s] English:** Thank you.  
**Translation:** 

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

**[3480.00s] English:** challenge problem i start with very general problem with plato so you understand and it  
**Translation:** 

**[3489.62s] English:** comes from plato to to to digit recognition so so you basically took plato and the uh the world  
**Translation:** Vocabulary: digit: 数字

**[3498.00s] English:** of forms and ideas and mapped and projected into the clearest simplest formulation of that big world  
**Translation:** 

**[3506.22s] English:** you know i i would say that i did not understand plato until uh recently and until i uh consider  
**Translation:** Vocabulary: projected: 投射

**[3517.10s] English:** weak convergence and then predicate and then oh this is what plato told  
**Translation:** 

**[3525.20s] English:** so you linger on that like why how do you think about this world of ideas and world of things in  
**Translation:** Vocabulary: convergence: 趋近; predicate: 谓语

**[3531.12s] English:** plato no it is metaphor it is it's a metaphor for sure yeah  
**Translation:** 

**[3536.10s] English:** completely  
**Translation:** Vocabulary: metaphor: 比喻

**[3536.22s] English:** compelling it's a poetic and a beautiful yeah but what can you but it is a way  
**Translation:** 

**[3541.46s] English:** half you you you should try to understand how attack ideas in the world  
**Translation:** Vocabulary: compelling: 极具说服力的

**[3547.04s] English:** so from my point of view it is very clear but it is lying all the time  
**Translation:** 

**[3555.46s] English:** people looking for that say Plato's and Hegel whatever reasonable it exists  
**Translation:** Vocabulary: hegel: 黑格尔

**[3564.22s] English:** whatever existed as reasonable I don't know what he have in mind reasonable  
**Translation:** 

**[3569.34s] English:** right this philosophers again no no no no no it is it is next stop of Wigner  
**Translation:** 

**[3576.30s] English:** that mathematics understand something of reality it is the same plot align and  
**Translation:** 

**[3582.72s] English:** then it comes suddenly to Vladimir probe look 31 ideas 31 units and describes  
**Translation:** Vocabulary: align: 对齐

**[3592.12s] English:** everything  
**Translation:** 

**[3594.22s] English:** there's abstractions ideas that represent our world  
**Translation:** Vocabulary: abstractions: 抽象概念

**[3600.00s] English:** And we should always try to reach into that.  
**Translation:** 

**[3603.44s] English:** Yeah, but you should make a projection on reality.  
**Translation:** Vocabulary: projection: 预测

**[3607.56s] English:** But understanding is, it is abstract ideas.  
**Translation:** 

**[3611.72s] English:** You have in your mind several abstract ideas which you can apply to reality.  
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

**[3629.78s] English:** You're like you.  
**Translation:** 

**[3630.66s] English:** I find compelling the idea, forget the space, the sea of functions.  
**Translation:** 

**[3636.36s] English:** There's also a sea of data in the world.  
**Translation:** 

**[3639.42s] English:** And I find compelling that there might be, like you said, teacher,  
**Translation:** 

**[3644.58s] English:** small examples of data that are most useful for discovering good,  
**Translation:** 

**[3652.76s] English:** whether it's predicates or good functions,  
**Translation:** 

**[3655.06s] English:** that the selection of data may be a powerful journey  
**Translation:** Vocabulary: predicates: 谓词

**[3659.78s] English:** a useful mechanism, you know, coming up with a mechanism  
**Translation:** 

**[3663.72s] English:** for selecting good data might be useful, too.  
**Translation:** 

**[3667.46s] English:** Do you find this idea of finding the right data set interesting at all?  
**Translation:** 

**[3673.96s] English:** Or do you kind of take the data set as a given?  
**Translation:** 

**[3677.70s] English:** I think that it is, you know, my scheme is very simple.  
**Translation:** 

**[3682.64s] English:** You have a huge set of functions.  
**Translation:** 

**[3686.26s] English:** If you will apply, and you have not,  
**Translation:** 

**[3689.78s] English:** too many data.  
**Translation:** 

**[3690.78s] English:** Right.  
**Translation:** 

**[3691.78s] English:** If you will pick up function, which describes this data,  
**Translation:** 

**[3697.48s] English:** you will do not very well.  
**Translation:** 

**[3701.14s] English:** Like randomly pick up.  
**Translation:** 

**[3702.14s] English:** Yeah, you will overfit here.  
**Translation:** 

**[3704.14s] English:** It will be overfitting.  
**Translation:** Vocabulary: overfitting: 模型过拟合

**[3706.34s] English:** So you should decrease set of function from which you're picking up one.  
**Translation:** 

**[3713.60s] English:** So you should go somehow to admissible set of function.  
**Translation:** Vocabulary: admissible: 可接受的

**[3717.88s] English:** And this.  
**Translation:** 

**[3720.00s] English:** what about weak convergence  
**Translation:** Vocabulary: convergence: 收敛

**[3721.98s] English:** so but  
**Translation:** 

**[3724.24s] English:** from another point of view  
**Translation:** 

**[3726.94s] English:** to  
**Translation:** 

**[3728.22s] English:** to make  
**Translation:** 

**[3729.42s] English:** admissible set of function  
**Translation:** 

**[3732.50s] English:** you need just a D  
**Translation:** 

**[3734.16s] English:** just function which you will  
**Translation:** 

**[3735.94s] English:** take in inner product  
**Translation:** 

**[3738.66s] English:** which you will  
**Translation:** 

**[3740.56s] English:** measure  
**Translation:** 

**[3741.06s] English:** property of your function  
**Translation:** 

**[3744.28s] English:** and  
**Translation:** 

**[3747.76s] English:** that is how it works  
**Translation:** 

**[3750.80s] English:** no I get it I get it I understand it  
**Translation:** 

**[3752.66s] English:** but do you  
**Translation:** 

**[3753.36s] English:** the reality is  
**Translation:** 

**[3754.90s] English:** let's think about  
**Translation:** 

**[3757.24s] English:** examples  
**Translation:** 

**[3758.56s] English:** you have huge set of function  
**Translation:** 

**[3761.46s] English:** and you have several examples  
**Translation:** 

**[3763.70s] English:** if you  
**Translation:** 

**[3765.10s] English:** just trying to  
**Translation:** 

**[3767.46s] English:** take function  
**Translation:** 

**[3769.70s] English:** which satisfies these examples  
**Translation:** 

**[3772.00s] English:** you still  
**Translation:** 

**[3774.20s] English:** will overfeed  
**Translation:** 

**[3775.34s] English:** you need decrease  
**Translation:** 

**[3777.34s] English:** you need  
**Translation:** 

**[3777.74s] English:** you need decrease  
**Translation:** 

**[3777.76s] English:** admissible set of function  
**Translation:** 

**[3779.20s] English:** absolutely  
**Translation:** 

**[3780.16s] English:** but what  
**Translation:** 

**[3781.52s] English:** say you have  
**Translation:** 

**[3783.26s] English:** more data than functions  
**Translation:** 

**[3786.14s] English:** so  
**Translation:** 

**[3787.02s] English:** sort of consider the  
**Translation:** 

**[3787.90s] English:** I mean maybe not more data than functions  
**Translation:** 

**[3789.80s] English:** because that's  
**Translation:** 

**[3790.64s] English:** impossible  
**Translation:** 

**[3791.48s] English:** impossible  
**Translation:** 

**[3792.06s] English:** but what  
**Translation:** 

**[3793.26s] English:** I was trying to be poetic for a second  
**Translation:** 

**[3795.16s] English:** I mean you have a huge amount of data  
**Translation:** 

**[3797.22s] English:** a huge amount of examples  
**Translation:** 

**[3799.88s] English:** but amount of function  
**Translation:** 

**[3801.72s] English:** can be even  
**Translation:** 

**[3802.56s] English:** bigger I understand  
**Translation:** 

**[3804.36s] English:** everything is  
**Translation:** 

**[3805.56s] English:** there's always  
**Translation:** 

**[3806.44s] English:** there's always a bigger boat  
**Translation:** 

**[3807.74s] English:** in the whole Hilbert space  
**Translation:** 

**[3808.74s] English:** I got you  
**Translation:** Vocabulary: hilbert: 希尔伯特空间

**[3809.74s] English:** but okay  
**Translation:** 

**[3810.74s] English:** but you don't  
**Translation:** 

**[3813.74s] English:** you don't find  
**Translation:** 

**[3814.74s] English:** the world of data  
**Translation:** 

**[3815.74s] English:** to be an interesting  
**Translation:** 

**[3817.74s] English:** optimization space  
**Translation:** 

**[3818.74s] English:** like the  
**Translation:** 

**[3819.74s] English:** the optimization  
**Translation:** Vocabulary: optimization: 优化

**[3820.74s] English:** should be in the space of functions  
**Translation:** 

**[3821.74s] English:** creating admissible set of functions  
**Translation:** 

**[3826.74s] English:** admissible set of functions  
**Translation:** 

**[3827.74s] English:** no  
**Translation:** 

**[3828.74s] English:** you know  
**Translation:** 

**[3829.74s] English:** even from the  
**Translation:** 

**[3830.74s] English:** classical basis theory  
**Translation:** 

**[3831.74s] English:** from structure risk minimization  
**Translation:** Vocabulary: minimization: 最小化

**[3835.74s] English:** you should  
**Translation:** 

**[3836.74s] English:** you should  
**Translation:** 

**[3837.72s] English:** organize  
**Translation:** 

**[3839.72s] English:** functionality  
**Translation:** Vocabulary: functionality: 功能

**[3840.72s] English:** is  
**Translation:** 

**[3842.68s] English:** it  
**Translation:** 

**[3843.72s] English:** transforming  
**Translation:** 

**[3844.72s] English:** each  
**Translation:** 

**[3845.72s] English:** every  
**Translation:** 

**[3846.72s] English:** every  
**Translation:** 

**[3847.72s] English:** each  
**Translation:** 

**[3848.72s] English:** every  
**Translation:** 

**[3849.72s] English:** million  
**Translation:** 

**[3850.72s] English:** million  
**Translation:** 

**[3851.72s] English:** block  
**Translation:** 

**[3852.72s] English:** approaches  
**Translation:** 

**[3853.72s] English:** among  
**Translation:** 

**[3854.72s] English:** all  
**Translation:** 

**[3856.72s] English:** that  
**Translation:** 

**[3857.72s] English:** and  
**Translation:** 

**[3858.72s] English:** awesome  
**Translation:** 

**[3859.72s] English:** biri  
**Translation:** 

**[3860.72s] English:** a  
**Translation:** 

**[3861.72s] English:** c  
**Translation:** 

**[3863.72s] English:** in  
**Translation:** 

**[3864.72s] English:** everything  
**Translation:** 

**[3865.72s] English:** beautiful  
**Translation:** 

**[3840.00s] English:** in the way that they will be useful for you.  
**Translation:** 

**[3846.42s] English:** Right.  
**Translation:** 

**[3847.46s] English:** And that is admissible.  
**Translation:** Vocabulary: admissible: 可接纳的

**[3849.74s] English:** The way you're thinking about useful is you're given a small set of examples.  
**Translation:** 

**[3857.00s] English:** Useful is small.  
**Translation:** 

**[3857.62s] English:** Small set of functions which contain functions I'm looking for.  
**Translation:** 

**[3861.76s] English:** Yeah, but looking for based on the empirical set of small examples.  
**Translation:** Vocabulary: empirical: 经验的

**[3867.60s] English:** Yeah.  
**Translation:** 

**[3868.08s] English:** But that is another story.  
**Translation:** 

**[3869.50s] English:** I don't touch it because I believe that these small examples, it's not too small.  
**Translation:** 

**[3877.36s] English:** Say 60 per class, the law of large numbers works.  
**Translation:** 

**[3881.24s] English:** I don't need uniform law.  
**Translation:** 

**[3883.42s] English:** The story is that in statistics, there are two laws, law of large numbers and uniform law of large numbers.  
**Translation:** 

**[3890.76s] English:** So I want to be in a situation where I use law of large numbers, but not uniform law of large numbers.  
**Translation:** 

**[3898.08s] English:** Right.  
**Translation:** 

**[3898.64s] English:** So 60 is...  
**Translation:** 

**[3899.50s] English:** It's large enough.  
**Translation:** 

**[3901.34s] English:** I hope, no.  
**Translation:** 

**[3902.36s] English:** It still needs some evaluation, some balance.  
**Translation:** 

**[3906.50s] English:** But the idea is the following, that if you trust that, say, this average gives you something close to expectation,  
**Translation:** 

**[3921.08s] English:** so you can talk about that, about this predicate.  
**Translation:** Vocabulary: expectation: 预期; predicate: 谓词

**[3926.22s] English:** And that is basis of human intelligence.  
**Translation:** 

**[3929.50s] English:** Good predicates is the...  
**Translation:** Vocabulary: predicates: 前提

**[3932.10s] English:** The discovery of good predicates is the basis of human intelligence.  
**Translation:** 

**[3934.50s] English:** No, no.  
**Translation:** 

**[3934.82s] English:** It is discovery of your understanding world, of your methodology of understanding world.  
**Translation:** 

**[3944.88s] English:** Because you have several functions which you will apply to reality.  
**Translation:** Vocabulary: methodology: 研究方法

**[3950.96s] English:** Can you say that again?  
**Translation:** 

**[3952.60s] English:** So you're...  
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

**[3961.00s] English:** Then you will apply them to reality, to your data, and you will create in this way predicate,  
**Translation:** 

**[3967.46s] English:** which is useful for your task.  
**Translation:** 

**[3971.64s] English:** But predicate are not related specifically to your task, to this task.  
**Translation:** 

**[3977.90s] English:** It is abstract functions, which being applied to-  
**Translation:** 

**[3983.18s] English:** Many tasks that you might be interested in.  
**Translation:** 

**[3985.18s] English:** It might be many tasks, I don't know.  
**Translation:** 

**[3989.00s] English:** Different tasks.  
**Translation:** 

**[3990.00s] English:** So they should be many tasks, right?  
**Translation:** 

**[3991.56s] English:** Yeah.  
**Translation:** 

**[3992.56s] English:** I believe like in prop case, it was for fairy tales, but it's happened everywhere.  
**Translation:** 

**[3999.24s] English:** Okay.  
**Translation:** 

**[4000.52s] English:** So we talked about images a little bit, but can we talk about Noam Chomsky for a second?  
**Translation:** Vocabulary: chomsky: 乔姆斯基

**[4007.88s] English:** I believe I don't know him very well.  
**Translation:** 

**[4014.24s] English:** Personally, well-  
**Translation:** 

**[4015.24s] English:** Not personally, I don't know.  
**Translation:** 

**[4017.00s] English:** His ideas.  
**Translation:** 

**[4018.00s] English:** His ideas.  
**Translation:** 

**[4019.00s] English:** Well, let me just say.  
**Translation:** 

**[4020.00s] English:** Do you think language, human language, is essential to expressing ideas, as Noam Chomsky  
**Translation:** 

**[4026.72s] English:** believes?  
**Translation:** 

**[4027.72s] English:** So like language is at the core of our formation of predicates, the human language.  
**Translation:** 

**[4034.96s] English:** For me, language and all the story of language is very complicated.  
**Translation:** 

**[4040.70s] English:** I don't understand this, and I'm not ... I thought about ...  
**Translation:** 

**[4044.80s] English:** Nobody does.  
**Translation:** 

**[4045.80s] English:** I'm not ready to work on that, because it's so huge.  
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

**[4057.46s] English:** Not for 21st century.  
**Translation:** 

**[4059.46s] English:** You should learn something, a lot of stuff, from simple task like digital recognition.  
**Translation:** 

**[4065.24s] English:** So you think digital recognition, 2D image ... How would you more abstractly define  
**Translation:** Vocabulary: abstractly: 抽象地

**[4074.24s] English:** digital recognition?  
**Translation:** 

**[4077.24s] English:** It's 2D image.  
**Translation:** 

**[4079.24s] English:** It's 2D image.  
**Translation:** 

**[4080.00s] English:** recognition essentially i mean i like i'm trying to get a sense sort of thinking about it now  
**Translation:** 

**[4089.24s] English:** having worked with mnist forever how how small of a subset is this of the general  
**Translation:** 

**[4096.64s] English:** vision recognition problem and the general intelligence problem is it  
**Translation:** 

**[4101.98s] English:** because yeah is it a giant subset is it not and how far away is language you know let me refer to  
**Translation:** 

**[4112.60s] English:** einstein take the simplest problem as simple as possible but not simpler and this is challenge  
**Translation:** 

**[4121.14s] English:** is simple problem but it's simple by idea but not simple to to get it when you will  
**Translation:** 

**[4130.86s] English:** when you will get it  
**Translation:** 

**[4131.96s] English:** do this you will find some predicate which helps you to do well yeah i mean with that  
**Translation:** 

**[4138.14s] English:** with einstein you can you look at general relativity but that doesn't help you with  
**Translation:** Vocabulary: einstein: 爱因斯坦; predicate: 谓词; relativity: 相对论

**[4145.08s] English:** quantum mechanics that's another story you don't have any universal instrument yes so i'm trying  
**Translation:** 

**[4152.84s] English:** to wonder if uh which space we're in whether the whether handwritten recognition is like  
**Translation:** 

**[4159.46s] English:** general relativity and then language  
**Translation:** 

**[4161.94s] English:** is like quantum mechanics so you're still gonna have to do a lot of mess to to to universalize it but  
**Translation:** Vocabulary: universalize: 普遍化

**[4168.74s] English:** uh i'm trying to see one so what's your intuition why handwritten recognition is easier than language  
**Translation:** 

**[4181.86s] English:** just i think a lot of people would agree with that but if you could elucidate sort of the the intuition  
**Translation:** Vocabulary: elucidate: 阐明; handwritten: 手写; intuition: 直觉

**[4188.66s] English:** of why  
**Translation:** 

**[4191.94s] English:** you don't know you know i don't think in this direction i just thinking in directions that this  
**Translation:** 

**[4198.66s] English:** is problem  
**Translation:** 

**[4200.00s] English:** Which, if we will solve it well, we will create some abstract understanding of images.  
**Translation:** 

**[4217.38s] English:** Maybe not all images.  
**Translation:** 

**[4219.58s] English:** I would like to talk to guys who are doing Unreal Images in Columbia University.  
**Translation:** 

**[4225.78s] English:** What kind of images? Unreal?  
**Translation:** 

**[4227.58s] English:** Real images. What they already predicate, what can be predicated.  
**Translation:** Vocabulary: predicated: 假设

**[4234.70s] English:** Symmetry will play a role in real-life images, in any real-life images, 2D images, let's talk about 2D images.  
**Translation:** 

**[4245.58s] English:** Because that's what we know.  
**Translation:** Vocabulary: symmetry: 对称

**[4251.58s] English:** The neural network was created for 2D images.  
**Translation:** 

**[4255.58s] English:** So the people I know in the  
**Translation:** 

**[4257.56s] English:** vision science, for example, the people study human vision, that they usually go  
**Translation:** 

**[4262.44s] English:** to the world of symbols and like handwritten recognition, but not really.  
**Translation:** 

**[4266.90s] English:** It's other kinds of symbols to study our visual perception system. As far as I  
**Translation:** 

**[4272.02s] English:** know, not much predicate type of thinking is understood about our vision system.  
**Translation:** Vocabulary: predicate: 谓词

**[4276.94s] English:** They did not think in this direction.  
**Translation:** 

**[4279.36s] English:** They don't, yeah. But how do you even begin to think in that direction?  
**Translation:** 

**[4282.94s] English:** That's what I would like to discuss with them.  
**Translation:** 

**[4286.78s] English:** Yeah.  
**Translation:** 

**[4287.56s] English:** Because if we will be able to show that it is what's working, and theoretical scheme,  
**Translation:** 

**[4298.62s] English:** it's not so bad.  
**Translation:** 

**[4300.40s] English:** So the unfortunate, so if we compare to language, language has like letters, finite set of letters  
**Translation:** 

**[4306.48s] English:** and a finite set of ways you can put together those letters. So it feels more amenable to  
**Translation:** Vocabulary: amenable: 易于处理; finite: 有限的

**[4311.94s] English:** kind of analysis. With natural images, there is so many pixels.  
**Translation:** 

**[4317.40s] English:** No, no, no. Letter.  
**Translation:** Vocabulary: pixels: 像素

**[4320.00s] English:** language is much, much more complicated.  
**Translation:** 

**[4323.66s] English:** It involves a lot of different stuff.  
**Translation:** 

**[4327.98s] English:** It's not just understanding of very simple class of tasks.  
**Translation:** 

**[4334.94s] English:** I would like to see lists of tasks where language is involved.  
**Translation:** 

**[4339.68s] English:** Yes, so there's a lot of nice benchmarks now in natural language processing  
**Translation:** 

**[4344.32s] English:** from the very trivial, like understanding the elements of a sentence,  
**Translation:** Vocabulary: benchmarks: 参考标准

**[4350.16s] English:** to question answering, to much more complicated,  
**Translation:** 

**[4353.02s] English:** where you talk about open domain dialogue.  
**Translation:** 

**[4356.00s] English:** The natural question is, with handwritten recognition,  
**Translation:** 

**[4359.14s] English:** it's really the first step of understanding visual information.  
**Translation:** 

**[4364.52s] English:** Right.  
**Translation:** 

**[4367.66s] English:** But even our records show that we're going in the wrong direction  
**Translation:** 

**[4373.38s] English:** because we need 60,000 digits.  
**Translation:** 

**[4376.66s] English:** So even this first step.  
**Translation:** Vocabulary: digits: 位数

**[4378.50s] English:** So forget about talking about the first.  
**Translation:** 

**[4380.00s] English:** This first step should be taken in the right direction.  
**Translation:** 

**[4383.16s] English:** No, no, in the wrong direction because 60,000 is unacceptable.  
**Translation:** 

**[4387.14s] English:** No, I'm saying it should be taken in the right direction  
**Translation:** Vocabulary: unacceptable: 无法接受

**[4390.76s] English:** because 60,000 is not acceptable.  
**Translation:** 

**[4393.60s] English:** You can talk, it's great, we have half a percent of error.  
**Translation:** 

**[4398.38s] English:** And hopefully the step from doing hand recognition using very few examples,  
**Translation:** 

**[4404.58s] English:** the step towards what babies do when they crawl  
**Translation:** 

**[4407.46s] English:** and understand their physical environment.  
**Translation:** 

**[4409.12s] English:** I don't know what babies do.  
**Translation:** 

**[4410.00s] English:** I know you don't know about babies.  
**Translation:** 

**[4411.44s] English:** If you will do from very small examples,  
**Translation:** 

**[4415.24s] English:** you will find principles which are different from what we're using now.  
**Translation:** 

**[4424.78s] English:** And theoretically, it's more or less clear.  
**Translation:** Vocabulary: theoretically: 理论上

**[4428.26s] English:** That means that you will use weak convergence,  
**Translation:** 

**[4432.26s] English:** not just strong convergence.  
**Translation:** Vocabulary: convergence: 收敛

**[4434.14s] English:** Do you think these principles will naturally be human  
**Translation:** 

**[4439.78s] English:** in terms of the way they're used?  
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

**[4461.50s] English:** You gave, like, a predicate of a basic for...  
**Translation:** 

**[4464.62s] English:** For symmetries.  
**Translation:** Vocabulary: predicate: 谓词; symmetries: 对称性

**[4465.72s] English:** Yes, for different symmetries, and you have...  
**Translation:** 

**[4468.20s] English:** For...  
**Translation:** 

**[4469.40s] English:** For degree of symmetries.  
**Translation:** 

**[4470.54s] English:** That is important.  
**Translation:** 

**[4471.92s] English:** Not just symmetry.  
**Translation:** 

**[4473.62s] English:** Exist and doesn't exist.  
**Translation:** 

**[4475.16s] English:** Degree of symmetry.  
**Translation:** 

**[4478.00s] English:** Yeah, for handwritten recognition.  
**Translation:** 

**[4480.94s] English:** No, it's not for handwritten.  
**Translation:** 

**[4482.92s] English:** It's for any images.  
**Translation:** Vocabulary: handwritten: 手写

**[4485.06s] English:** But I would like to apply to handwritten.  
**Translation:** 

**[4487.36s] English:** Right.  
**Translation:** 

**[4488.14s] English:** In theory, it's more general.  
**Translation:** 

**[4489.64s] English:** Okay.  
**Translation:** 

**[4490.36s] English:** Okay.  
**Translation:** 

**[4494.82s] English:** So, a lot of things we've been talking about falls...  
**Translation:** 

**[4499.40s] English:** We've been talking about philosophy a little bit, but also about mathematics and statistics.  
**Translation:** 

**[4505.10s] English:** A lot of it falls into this idea, a universal idea of statistical theory of learning.  
**Translation:** 

**[4511.38s] English:** What is the most beautiful and sort of powerful or essential idea you've come across, even just for yourself personally, in the world of statistics or statistic theory of learning?  
**Translation:** 

**[4525.18s] English:** Probably uniform convergence, which we did.  
**Translation:** 

**[4529.40s] English:** Yes, Alexey Chervenenko.  
**Translation:** 

**[4532.46s] English:** Can you describe universal convergence?  
**Translation:** 

**[4535.70s] English:** You have law of large numbers.  
**Translation:** 

**[4540.00s] English:** So, for any function, expectation of function, average of function converges to expectation.  
**Translation:** Vocabulary: converges: 收敛; expectation: 期望值

**[4547.50s] English:** But if you have set of functions, for any function, it is true.  
**Translation:** 

**[4552.86s] English:** But it should converge simultaneously for all set of functions.  
**Translation:** Vocabulary: converge: 收敛

**[4558.60s] English:** And...  
**Translation:** 

**[4559.40s] English:** I don't know.  
**Translation:** 

**[4560.34s] English:** Yeah.  
**Translation:** 

**[4560.66s] English:** I just think it's a very good idea.  
**Translation:** 

**[4562.14s] English:** I think it's a great idea.  
**Translation:** 

**[4563.12s] English:** So this is a very important topic.  
**Translation:** 

**[4564.22s] English:** I'm sure that the study can give us examples of the evolution of statistics and statistics, things that are more surprising to some of us.  
**Translation:** 

**[4569.38s] English:** So, I'd just like to express that I'm very proud of this project.  
**Translation:** 

**[4572.48s] English:** It's been a great pleasure.  
**Translation:** 

**[4574.20s] English:** I appreciate it.  
**Translation:** 

**[4575.56s] English:** I think it's a very important topic.  
**Translation:** 

**[4576.90s] English:** And it's very useful.  
**Translation:** 

**[4579.02s] English:** So, have a great day.  
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

**[4560.00s] English:** For learning, you need uniform convergence.  
**Translation:** Vocabulary: convergence: 收敛性

**[4566.74s] English:** Just convergence is not enough.  
**Translation:** 

**[4570.58s] English:** Because when you pick up one which gives minimum,  
**Translation:** 

**[4576.58s] English:** you can pick up one function which does not converge,  
**Translation:** 

**[4582.12s] English:** and it will give you the best answer for this function.  
**Translation:** 

**[4590.00s] English:** So, you need uniform convergence to guarantee learning.  
**Translation:** 

**[4594.94s] English:** So, learning does not rely on trivial large numbers.  
**Translation:** 

**[4600.48s] English:** It relies on universal.  
**Translation:** 

**[4602.86s] English:** But the idea of the convergence exists in statistics for a long time.  
**Translation:** 

**[4613.50s] English:** But it is interesting that,  
**Translation:** 

**[4618.88s] English:** as I...  
**Translation:** 

**[4620.00s] English:** I think about myself,  
**Translation:** 

**[4622.12s] English:** how stupid I was 50 years.  
**Translation:** 

**[4625.22s] English:** I did not see weak convergence.  
**Translation:** 

**[4628.02s] English:** I work only on strong convergence.  
**Translation:** 

**[4630.84s] English:** But now I think that most powerful is weak convergence.  
**Translation:** 

**[4634.96s] English:** Because it makes admissible set of functions.  
**Translation:** Vocabulary: admissible: 可接受的

**[4638.44s] English:** And even in all products,  
**Translation:** 

**[4642.62s] English:** when people try to understand recognition about dog law,  
**Translation:** 

**[4648.08s] English:** looks like a dog and so on,  
**Translation:** 

**[4650.00s] English:** they use weak convergence.  
**Translation:** 

**[4652.30s] English:** People in language, they understand this.  
**Translation:** 

**[4655.66s] English:** But when we're trying to create artificial intelligence,  
**Translation:** 

**[4662.02s] English:** we won't inventing different way.  
**Translation:** 

**[4666.06s] English:** We just consider strong convergence.  
**Translation:** 

**[4670.16s] English:** So, reducing the set of admissible functions,  
**Translation:** 

**[4673.02s] English:** you think there should be effort put into understanding  
**Translation:** 

**[4679.04s] English:** properties of  
**Translation:** 

**[4680.00s] English:** weak convergence you know in classical mathematics in gilded space there are only two way two form  
**Translation:** 

**[4689.84s] English:** of convergence strong and weak now we can use both that means that we did everything and  
**Translation:** 

**[4701.36s] English:** it so happened then when we use hilbert space which is very rich space space of continuous  
**Translation:** Vocabulary: convergence: 收敛; hilbert: 希尔伯特

**[4711.06s] English:** functions uh which has an integral and square so we can apply weak and strong convergence for  
**Translation:** 

**[4721.06s] English:** learning and have closed form solution so for computationally simple for me it is sign  
**Translation:** Vocabulary: computationally: 计算上; integral: 积分

**[4728.90s] English:** that it is right way  
**Translation:** 

**[4731.36s] English:** because you you don't need any realistic you just know whatever you want  
**Translation:** 

**[4737.50s] English:** but now the only what left it is concept of what is predicate of predicate but it is not  
**Translation:** 

**[4746.64s] English:** statistics by the way i like the fact that you think the heuristics are a mess that should be  
**Translation:** Vocabulary: heuristics: 启发式; predicate: 谓词

**[4752.70s] English:** removed from the system so closed form solution is the ultimate no it so happened then when you're  
**Translation:** 

**[4760.32s] English:** using  
**Translation:** 

**[4760.70s] English:** you know  
**Translation:** 

**[4761.34s] English:** you know you're using  
**Translation:** 

**[4761.36s] English:** Right, instrument, you have closed-form solution.  
**Translation:** 

**[4766.84s] English:** Do you think intelligence, human-level intelligence, when we create it, will have  
**Translation:** 

**[4779.00s] English:** something like a closed-form solution?  
**Translation:** 

**[4781.52s] English:** You know, now I'm looking on bounds, which I gave bounds for convergence, and when I'm  
**Translation:** 

**[4791.84s] English:** looking for bounds, I'm thinking, what is the most appropriate kernel for this bound?  
**Translation:** 

**[4800.00s] English:** bound would be. So we know that in, say, all our businesses, we use radial basis function.  
**Translation:** Vocabulary: kernel: 核函数; radial: 径向的

**[4811.68s] English:** But looking on the bound, I think that I start to understand that maybe we need to make corrections  
**Translation:** 

**[4818.76s] English:** to radial basis function to be closer, to work better for this bounds. So I'm again  
**Translation:** 

**[4829.54s] English:** trying to understand what type of kernel have best approximation, non-approximation, best  
**Translation:** 

**[4839.92s] English:** fit to this bound.  
**Translation:** Vocabulary: approximation: 近似

**[4842.78s] English:** Sure. So there's a lot of interesting work that could be done in discovering better  
**Translation:** 

**[4847.20s] English:** functions and radial basis functions for the kind of bounds you find.  
**Translation:** 

**[4852.30s] English:** Yeah, but it still comes from... You're looking to mass and trying to understand  
**Translation:** 

**[4859.30s] English:** what...  
**Translation:** 

**[4859.54s] English:** From your own mind, looking at the... I don't know.  
**Translation:** 

**[4862.30s] English:** Yeah, but then I'm trying to understand what will be good for that.  
**Translation:** 

**[4870.78s] English:** Yeah, but to me, there's still a beauty. Again, maybe I'm a descendant of Alan Turing,  
**Translation:** 

**[4876.30s] English:** to heuristics. To me, ultimately, intelligence will be a mess of heuristics. And that's the  
**Translation:** Vocabulary: descendant: 后裔; heuristics: 启发法; turing: 图灵

**[4885.04s] English:** engineering answer, I guess.  
**Translation:** 

**[4887.30s] English:** No, absolutely.  
**Translation:** 

**[4889.30s] English:** Self-driving cars, there's a great guy who will do that. It does not matter what theory  
**Translation:** 

**[4897.70s] English:** behind that. Who has a better feeling have to apply it. But by the way, it is the same  
**Translation:** 

**[4908.16s] English:** story about predicate because you cannot create rule for... Citation is much more than you  
**Translation:** 

**[4915.58s] English:** have rule for that.  
**Translation:** Vocabulary: cannot: 不能; citation: 引用; predicate: 谓语

**[4917.06s] English:** Yeah.  
**Translation:** 

**[4918.06s] English:** Yeah.  
**Translation:** 

**[4919.06s] English:** Yeah.  
**Translation:** 

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

**[4935.06s] English:** Yeah.  
**Translation:** 

**[4936.06s] English:** Yeah.  
**Translation:** 

**[4937.06s] English:** Yeah.  
**Translation:** 

**[4938.06s] English:** Yeah.  
**Translation:** 

**[4939.06s] English:** Yeah.  
**Translation:** 

**[4940.06s] English:** Yeah.  
**Translation:** 

**[4941.06s] English:** Yeah.  
**Translation:** 

**[4942.06s] English:** Yeah.  
**Translation:** 

**[4943.06s] English:** Yeah.  
**Translation:** 

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

**[4920.00s] English:** Maybe you can have more abstract rule, then it will be less literal.  
**Translation:** 

**[4928.82s] English:** It is the same story about ideas and ideas applied to specific cases.  
**Translation:** 

**[4934.80s] English:** But still, you should reach-  
**Translation:** 

**[4937.30s] English:** You cannot avoid this.  
**Translation:** 

**[4938.62s] English:** Yes, of course, but you should still reach for the ideas to understand the science.  
**Translation:** 

**[4942.76s] English:** Yeah.  
**Translation:** 

**[4943.76s] English:** Let me ask, do you think neural networks or functions can be made to reason?  
**Translation:** 

**[4954.62s] English:** What do you think?  
**Translation:** Vocabulary: neural: 神经网络

**[4955.62s] English:** We've been talking about intelligence, but this idea of reasoning, there's an element  
**Translation:** 

**[4961.26s] English:** of sequentially disassembling, interpreting the images.  
**Translation:** Vocabulary: disassembling: 拆解; interpreting: 解释; sequentially: 依次

**[4969.22s] English:** When you think of handwritten recognition.  
**Translation:** 

**[4973.52s] English:** We kind of think that there'll be a single, there's an input and output.  
**Translation:** Vocabulary: handwritten: 手写

**[4977.06s] English:** There's not a recurrence.  
**Translation:** 

**[4978.76s] English:** Yeah.  
**Translation:** Vocabulary: recurrence: 复发

**[4979.76s] English:** What do you think about the idea of recurrence, of going back to memory and thinking  
**Translation:** 

**[4986.40s] English:** through this sort of sequentially mangling the different representations over and over  
**Translation:** Vocabulary: mangling: 扭曲

**[4994.02s] English:** until you arrive at a conclusion?  
**Translation:** 

**[5000.18s] English:** Or is ultimately all that can be wrapped up into a function?  
**Translation:** 

**[5003.02s] English:** No.  
**Translation:** 

**[5003.52s] English:** You're suggesting that let us use this type of algorithm.  
**Translation:** Vocabulary: algorithm: 算法

**[5009.76s] English:** When I start thinking, I, first of all, start to understand what I want.  
**Translation:** 

**[5016.48s] English:** Can I write down what I want?  
**Translation:** 

**[5020.52s] English:** And then I try to formalize.  
**Translation:** 

**[5024.92s] English:** And when I do that, I think I have to solve this problem.  
**Translation:** 

**[5032.02s] English:** And-  
**Translation:** 

**[5033.52s] English:** You know, I did not see it.  
**Translation:** 

**[5040.00s] English:** you need recurrence  
**Translation:** 

**[5043.52s] English:** but  
**Translation:** 

**[5044.36s] English:** do you observe human beings  
**Translation:** 

**[5047.20s] English:** do you try to  
**Translation:** 

**[5049.38s] English:** it's the imitation question right  
**Translation:** 

**[5051.80s] English:** it seems that human beings reason  
**Translation:** Vocabulary: imitation: 模仿

**[5054.02s] English:** this kind of sequentially  
**Translation:** 

**[5056.24s] English:** sort of  
**Translation:** 

**[5059.40s] English:** does that inspire in you  
**Translation:** 

**[5062.22s] English:** a thought that we need to add that  
**Translation:** 

**[5064.04s] English:** into our  
**Translation:** 

**[5065.32s] English:** intelligent  
**Translation:** 

**[5068.10s] English:** systems  
**Translation:** 

**[5068.70s] English:** you're saying  
**Translation:** 

**[5071.44s] English:** you've kind of answered  
**Translation:** 

**[5074.02s] English:** saying until now I haven't seen a need for it  
**Translation:** 

**[5076.44s] English:** and so because of that  
**Translation:** 

**[5078.38s] English:** you don't see a reason to think  
**Translation:** 

**[5080.34s] English:** about it  
**Translation:** 

**[5080.80s] English:** you know most of things I don't understand  
**Translation:** 

**[5084.68s] English:** in reasoning  
**Translation:** 

**[5086.40s] English:** in human  
**Translation:** 

**[5087.22s] English:** it is for me too complicated  
**Translation:** 

**[5090.42s] English:** for me  
**Translation:** 

**[5093.14s] English:** the most difficult part  
**Translation:** 

**[5095.50s] English:** is  
**Translation:** 

**[5097.14s] English:** to ask questions  
**Translation:** 

**[5099.82s] English:** good questions  
**Translation:** 

**[5102.04s] English:** how it works  
**Translation:** 

**[5103.80s] English:** how people  
**Translation:** 

**[5104.90s] English:** asking questions  
**Translation:** 

**[5106.48s] English:** I don't know  
**Translation:** 

**[5109.40s] English:** this  
**Translation:** 

**[5109.78s] English:** you said that machine learning is not only  
**Translation:** 

**[5113.54s] English:** about technical things  
**Translation:** 

**[5114.80s] English:** speaking of questions but it's also about  
**Translation:** 

**[5117.28s] English:** philosophy  
**Translation:** 

**[5119.66s] English:** so  
**Translation:** 

**[5120.46s] English:** what role does philosophy  
**Translation:** 

**[5122.12s] English:** play in machine learning  
**Translation:** 

**[5123.24s] English:** we talked about Plato  
**Translation:** 

**[5124.44s] English:** but generally thinking  
**Translation:** 

**[5126.52s] English:** over  
**Translation:** 

**[5128.10s] English:** in this philosophical way? How does philosophy and math fit together in your mind?  
**Translation:** Vocabulary: philosophical: 哲学的

**[5136.42s] English:** First ideas and then their implementation. It's like predicate, like  
**Translation:** 

**[5143.94s] English:** say admissible set of functions. It comes together, everything. Because  
**Translation:** Vocabulary: admissible: 可接受的; implementation: 实施; predicate: 谓词

**[5151.78s] English:** the first iteration of theory was done 50 years ago, I told that, this is theory.  
**Translation:** 

**[5160.00s] English:** So, everything's there.  
**Translation:** Vocabulary: iteration: 循环版本

**[5162.14s] English:** If you have data, you can, and your set of function is not, has not, have not big capacity.  
**Translation:** 

**[5173.26s] English:** So, low VC dimension, you can do that.  
**Translation:** Vocabulary: dimension: 维度

**[5175.64s] English:** You can make structural risk minimization, control capacity.  
**Translation:** 

**[5181.04s] English:** But you was not able to make admissible set of function good.  
**Translation:** Vocabulary: minimization: 最小化

**[5187.84s] English:** But now, when suddenly realize that we did not use another idea of convergence, which we can, everything comes together.  
**Translation:** 

**[5201.38s] English:** But those are mathematical notions.  
**Translation:** Vocabulary: convergence: 收敛; mathematical: 数学的

**[5203.10s] English:** Philosophy plays a role of simply saying that we should be swimming in the space of ideas.  
**Translation:** 

**[5211.74s] English:** Let's talk what is philosophy.  
**Translation:** 

**[5214.24s] English:** Philosophy means understanding of life.  
**Translation:** 

**[5217.84s] English:** So, understanding of life, say, people like Plato, they understand on very high abstract level of life.  
**Translation:** 

**[5226.96s] English:** So, and whatever I doing, it's just implementation of my understanding of life.  
**Translation:** 

**[5236.34s] English:** But every new step, it is very difficult.  
**Translation:** 

**[5241.84s] English:** For example, to find this idea.  
**Translation:** 

**[5247.84s] English:** That we need big convergence was not simple for me.  
**Translation:** 

**[5260.46s] English:** So, that required thinking about life a little bit.  
**Translation:** 

**[5264.16s] English:** Hard to trace, but there was some thought process.  
**Translation:** 

**[5269.76s] English:** You know, I'm working, I'm thinking about the same problem for 50 years now.  
**Translation:** 

**[5276.72s] English:** And again and again.  
**Translation:** 

**[5278.18s] English:** And again and again.  
**Translation:** 

**[5278.46s] English:** And again.  
**Translation:** 

**[5280.00s] English:** I'm trying to be honest, and that is very important,  
**Translation:** 

**[5282.66s] English:** not to be very enthusiastic,  
**Translation:** 

**[5284.82s] English:** but concentrate on whatever we were not able to achieve,  
**Translation:** 

**[5289.40s] English:** for example, and understand why.  
**Translation:** 

**[5294.16s] English:** And now I understand that because I believe in math,  
**Translation:** 

**[5298.78s] English:** I believe in Wigner's idea.  
**Translation:** 

**[5303.62s] English:** But now when I see that there are only two ways of convergence,  
**Translation:** 

**[5310.48s] English:** and we're using both,  
**Translation:** 

**[5312.86s] English:** that means that we must do as well as people doing.  
**Translation:** 

**[5319.76s] English:** But now exactly in philosophy and what we know about predicate,  
**Translation:** Vocabulary: predicate: 谓语

**[5325.10s] English:** how we understand life, can we describe as a predicate?  
**Translation:** 

**[5331.08s] English:** I thought about that,  
**Translation:** 

**[5334.36s] English:** and that is more or less obvious level of symmetry.  
**Translation:** 

**[5340.80s] English:** But next, I have a feeling it's something about structures.  
**Translation:** Vocabulary: symmetry: 对称

**[5348.98s] English:** But I don't know how to formulate,  
**Translation:** 

**[5351.84s] English:** how to measure a measure of structure and all that stuff.  
**Translation:** 

**[5355.56s] English:** And the guy who will solve this challenge problem,  
**Translation:** 

**[5362.14s] English:** then when we will look at how he did it,  
**Translation:** 

**[5366.10s] English:** probably just only symmetry is not enough.  
**Translation:** 

**[5370.00s] English:** But something like symmetry will be there.  
**Translation:** 

**[5373.72s] English:** Oh, yes, absolutely.  
**Translation:** 

**[5375.18s] English:** Symmetry will be there.  
**Translation:** 

**[5377.24s] English:** Level of symmetry will be there.  
**Translation:** 

**[5380.66s] English:** And level of symmetry, anti-symmetry, diagonal, vertical.  
**Translation:** Vocabulary: diagonal: 对角线; vertical: 垂直

**[5385.18s] English:** I even don't know how you can use in different direction idea of symmetry.  
**Translation:** 

**[5390.60s] English:** It's very general.  
**Translation:** 

**[5392.06s] English:** But it will be there.  
**Translation:** 

**[5394.42s] English:** I think that people are very sensitive to idea of symmetry.  
**Translation:** 

**[5398.14s] English:** But there are several.  
**Translation:** 

**[5400.62s] English:** I don't know.  
**Translation:** 

**[5401.22s] English:** I don't know here,  
**Translation:** 

**[5402.46s] English:** but I'm looking at the  
**Translation:** 

**[5427.60s] English:** one thing.  
**Translation:** 

**[5428.48s] English:** If you're going to ask me,  
**Translation:** 

**[5429.38s] English:** there's only one thing I can do.  
**Translation:** 

**[5429.78s] English:** There's only one way to solve this problem.  
**Translation:** 

**[5429.82s] English:** There is.  
**Translation:** 

**[5400.00s] English:** ideas like symmetry  
**Translation:** 

**[5402.62s] English:** as I would like to learn  
**Translation:** 

**[5406.18s] English:** but  
**Translation:** 

**[5407.20s] English:** you cannot learn just thinking  
**Translation:** 

**[5410.38s] English:** about that  
**Translation:** Vocabulary: cannot: 不能

**[5411.10s] English:** you should do challenging problems  
**Translation:** 

**[5413.86s] English:** and then analyze them  
**Translation:** 

**[5415.50s] English:** why it was  
**Translation:** 

**[5417.44s] English:** able to solve them  
**Translation:** 

**[5419.32s] English:** and then you will see  
**Translation:** 

**[5421.12s] English:** very simple things  
**Translation:** 

**[5423.68s] English:** it's not easy to find  
**Translation:** 

**[5425.20s] English:** even with talking about this  
**Translation:** 

**[5429.50s] English:** every time  
**Translation:** 

**[5430.24s] English:** I was surprised  
**Translation:** 

**[5433.94s] English:** I tried to understand  
**Translation:** 

**[5435.70s] English:** these people describe  
**Translation:** 

**[5437.46s] English:** in language  
**Translation:** 

**[5438.78s] English:** strong convergence  
**Translation:** Vocabulary: convergence: 趋同

**[5441.26s] English:** mechanism for learning  
**Translation:** 

**[5443.00s] English:** I did not see  
**Translation:** 

**[5445.10s] English:** I don't know  
**Translation:** 

**[5445.96s] English:** but weak convergence  
**Translation:** 

**[5447.88s] English:** this dark story  
**Translation:** 

**[5449.82s] English:** and story like that  
**Translation:** 

**[5451.60s] English:** when you will explain  
**Translation:** 

**[5452.74s] English:** to kid you will use weak convergence  
**Translation:** 

**[5456.00s] English:** argument  
**Translation:** 

**[5456.50s] English:** it looks like it does like  
**Translation:** 

**[5459.06s] English:** this  
**Translation:** 

**[5459.40s] English:** this  
**Translation:** 

**[5459.48s] English:** this  
**Translation:** 

**[5459.50s] English:** and that  
**Translation:** 

**[5459.66s] English:** but when you try to  
**Translation:** 

**[5462.38s] English:** formalize  
**Translation:** 

**[5463.32s] English:** you're just ignoring this  
**Translation:** 

**[5465.50s] English:** why 50 years  
**Translation:** 

**[5467.36s] English:** from start of machine learning  
**Translation:** 

**[5470.04s] English:** and that's the role of philosophy  
**Translation:** 

**[5471.24s] English:** I think that maybe  
**Translation:** 

**[5473.46s] English:** I don't know  
**Translation:** 

**[5475.78s] English:** maybe this is theory also  
**Translation:** 

**[5479.90s] English:** we should blame for that  
**Translation:** 

**[5482.68s] English:** because empirical risk  
**Translation:** 

**[5484.40s] English:** minimization  
**Translation:** Vocabulary: empirical: 经验; minimization: 最小化

**[5485.22s] English:** and all this stuff  
**Translation:** 

**[5487.00s] English:** if you read  
**Translation:** 

**[5488.70s] English:** now  
**Translation:** 

**[5489.48s] English:** textbooks  
**Translation:** 

**[5490.48s] English:** they just about bound  
**Translation:** 

**[5492.38s] English:** about empirical risk minimization  
**Translation:** 

**[5494.20s] English:** they don't looking  
**Translation:** 

**[5495.04s] English:** for another problem  
**Translation:** 

**[5498.10s] English:** like admissible set  
**Translation:** 

**[5499.48s] English:** but on the topic of life  
**Translation:** Vocabulary: admissible: 可接受的

**[5503.48s] English:** perhaps  
**Translation:** 

**[5505.44s] English:** we you could talk in Russian  
**Translation:** 

**[5508.48s] English:** for a little bit  
**Translation:** 

**[5509.18s] English:** what's your favorite memory  
**Translation:** 

**[5511.76s] English:** from childhood  
**Translation:** 

**[5512.58s] English:** what's your favorite memory  
**Translation:** 

**[5514.52s] English:** from childhood  
**Translation:** 

**[5515.06s] English:** music  
**Translation:** 

**[5518.10s] English:** music  
**Translation:** 

**[5518.16s] English:** music  
**Translation:** 

**[5518.26s] English:** music  
**Translation:** 

**[5519.46s] English:** how about  
**Translation:** 

**[5520.46s] English:** music  
**Translation:** 

**[5521.46s] English:** music  
**Translation:** 

**[5522.46s] English:** music  
**Translation:** 

**[5523.46s] English:** music  
**Translation:** 

**[5524.46s] English:** music  
**Translation:** 

**[5525.46s] English:** music  
**Translation:** 

**[5526.46s] English:** music  
**Translation:** 

**[5527.46s] English:** music  
**Translation:** 

**[5528.46s] English:** music  
**Translation:** 

**[5529.46s] English:** music  
**Translation:** 

**[5530.46s] English:** music  
**Translation:** 

**[5531.46s] English:** music  
**Translation:** 

**[5532.46s] English:** music  
**Translation:** 

**[5533.46s] English:** music  
**Translation:** 

**[5534.46s] English:** music  
**Translation:** 

**[5535.46s] English:** music  
**Translation:** 

**[5536.46s] English:** music  
**Translation:** 

**[5537.46s] English:** music  
**Translation:** 

**[5538.46s] English:** music  
**Translation:** 

**[5539.46s] English:** music  
**Translation:** 

**[5540.46s] English:** music  
**Translation:** 

**[5541.46s] English:** music  
**Translation:** 

**[5542.46s] English:** music  
**Translation:** 

**[5543.46s] English:** music  
**Translation:** 

**[5544.46s] English:** music  
**Translation:** 

**[5545.46s] English:** music  
**Translation:** 

**[5546.46s] English:** music  
**Translation:** 

**[5547.46s] English:** music  
**Translation:** 

**[5548.46s] English:** music  
**Translation:** 

**[5520.00s] English:** Can you try to answer in Russian?  
**Translation:** 

**[5522.56s] English:** Музыка.  
**Translation:** 

**[5524.80s] English:** Было очень здорово, когда...  
**Translation:** 

**[5527.78s] English:** Какая музыка?  
**Translation:** 

**[5529.88s] English:** Классическая музыка.  
**Translation:** 

**[5531.76s] English:** Какой любимый?  
**Translation:** 

**[5532.50s] English:** Ну, разные композиторы.  
**Translation:** 

**[5535.78s] English:** Сначала это был Вивальди, я, в общем, был удивлен, что так можно.  
**Translation:** 

**[5543.36s] English:** А потом, я когда понял Баха, я, в общем, был совершенно потрясен.  
**Translation:** 

**[5547.14s] English:** Кстати, вот из него я и думаю, что существуют предикаты, типа структуры.  
**Translation:** 

**[5556.60s] English:** В Бахе, ну, конечно.  
**Translation:** 

**[5557.76s] English:** Потому что там просто чувствуется всюду структура.  
**Translation:** 

**[5562.66s] English:** И я не думаю, что разные элементы жизни сильно разделены в смысле предикатов.  
**Translation:** 

**[5573.04s] English:** Всюду структура в живописи, структура в человечестве.  
**Translation:** 

**[5577.14s] English:** В человеческих отношениях структура.  
**Translation:** 

**[5579.62s] English:** Вот как-то найти вот эти вот высокого уровня предикаты.  
**Translation:** 

**[5585.08s] English:** В Бахе и в жизни.  
**Translation:** 

**[5587.36s] English:** Все соединено.  
**Translation:** 

**[5590.52s] English:** Теперь, что мы говорим о Бахе,  
**Translation:** 

**[5594.00s] English:** давайте перейдем к английскому, потому что я люблю Бейтховен и Шопен.  
**Translation:** 

**[5598.22s] English:** Шопен – это другая интересная история.  
**Translation:** 

**[5601.26s] English:** Но Бах, если мы говорим о предикатах,  
**Translation:** 

**[5603.76s] English:** Бах, наверное,  
**Translation:** 

**[5606.66s] English:** имеет,  
**Translation:** 

**[5607.14s] English:** наверное,  
**Translation:** 

**[5608.14s] English:** самые  
**Translation:** 

**[5609.14s] English:** определенные  
**Translation:** 

**[5610.14s] English:** предикаты.  
**Translation:** 

**[5611.14s] English:** Знаешь,  
**Translation:** 

**[5612.14s] English:** очень интересно  
**Translation:** 

**[5613.14s] English:** читать,  
**Translation:** 

**[5614.14s] English:** что  
**Translation:** 

**[5615.14s] English:** критики  
**Translation:** 

**[5616.14s] English:** пишут  
**Translation:** 

**[5617.14s] English:** о Бахе.  
**Translation:** 

**[5618.14s] English:** Какие  
**Translation:** 

**[5619.14s] English:** слова они используют.  
**Translation:** 

**[5620.14s] English:** Они пытаются  
**Translation:** 

**[5621.14s] English:** описать  
**Translation:** 

**[5622.14s] English:** предикаты.  
**Translation:** 

**[5623.14s] English:** Да.  
**Translation:** 

**[5624.14s] English:** И  
**Translation:** 

**[5625.14s] English:** и  
**Translation:** 

**[5626.14s] English:** и  
**Translation:** 

**[5627.14s] English:** и  
**Translation:** 

**[5628.14s] English:** и  
**Translation:** 

**[5629.14s] English:** и  
**Translation:** 

**[5630.14s] English:** и  
**Translation:** 

**[5631.14s] English:** и  
**Translation:** 

**[5632.14s] English:** и  
**Translation:** 

**[5633.14s] English:** и  
**Translation:** 

**[5634.14s] English:** и  
**Translation:** 

**[5635.14s] English:** и  
**Translation:** 

**[5636.14s] English:** Шопен.  
**Translation:** 

**[5636.66s] English:** И  
**Translation:** 

**[5637.66s] English:** и  
**Translation:** 

**[5638.66s] English:** и и  
**Translation:** 

**[5639.66s] English:** Продолжение следует...  
**Translation:** 

**[5640.00s] English:** on that so maybe from this you can describe predicate for digit recognition i will from  
**Translation:** Vocabulary: digit: 数字; predicate: 谓词

**[5648.90s] English:** bach and chopin no no no not from bach and chopin from the critic interpretation of the music yeah  
**Translation:** 

**[5655.14s] English:** when they're trying to explain you music what they use this as they use they describe high  
**Translation:** Vocabulary: chopin: 肖邦

**[5663.84s] English:** level ideas of of platos ideas what behind this music that's brilliant so art is not self  
**Translation:** 

**[5672.84s] English:** explanatory in some sense so you have to try to convert it into ideas it is problems when when  
**Translation:** Vocabulary: explanatory: 易理解的

**[5681.50s] English:** you go from ideas to to the representation it is easy way but when you're trying to go back  
**Translation:** 

**[5689.32s] English:** it is you'll post problems but nevertheless i believe that  
**Translation:** 

**[5693.84s] English:** when you're looking from that even from art you will be able to find predicate for digit recognition  
**Translation:** 

**[5703.60s] English:** that's such a fascinating and powerful notion do you ponder your own mortality  
**Translation:** 

**[5711.44s] English:** do you think about it do you fear it do you draw insight from it  
**Translation:** 

**[5716.72s] English:** about mortality no yeah are you afraid of death  
**Translation:** 

**[5724.74s] English:** not too much not too much  
**Translation:** 

**[5729.52s] English:** it is pity that i will not be able to do something which i think i have a feeling to do that  
**Translation:** 

**[5739.28s] English:** for example i will be very happy to work with guys theoretician from music to write this collection  
**Translation:** 

**[5751.84s] English:** of description but what how they describe music how they use what predicate and from art as well  
**Translation:** Vocabulary: theoretician: 理论家

**[5760.00s] English:** then take what is in common and try to understand predicate which is absolute for everything  
**Translation:** 

**[5768.48s] English:** and then use that for visual recognition and see if there is a connection yeah exactly  
**Translation:** Vocabulary: predicate: 谓词

**[5773.68s] English:** there's still time we've got time  
**Translation:** 

**[5779.04s] English:** we've got time it it it it's take years and years and years yeah it's it's a long way  
**Translation:** 

**[5786.32s] English:** well see you've got the patient mathematic mathematicians mind i think it could be  
**Translation:** 

**[5791.44s] English:** done very quickly and very beautifully i think it's a really elegant idea yeah but also some  
**Translation:** Vocabulary: mathematicians: 数学家

**[5797.04s] English:** of many yeah you know the the most time it is not to make this collection to understand  
**Translation:** 

**[5805.20s] English:** what is the common to think about that once again and again and again and again again but i  
**Translation:** 

**[5811.52s] English:** think sometimes especially just when you say this idea now  
**Translation:** 

**[5815.60s] English:** even just  
**Translation:** 

**[5817.12s] English:** putting together the collection and looking at the different  
**Translation:** 

**[5822.16s] English:** sets of data language trying to interpret music criticize music and images i think there will be  
**Translation:** Vocabulary: interpret: 解释

**[5829.36s] English:** sparks of ideas that will come of course again and again you'll come up with better ideas but  
**Translation:** 

**[5833.52s] English:** even just that notion is a beautiful notion i even have some example so i have friend  
**Translation:** 

**[5845.12s] English:** who was  
**Translation:** 

**[5847.28s] English:** specialist in russian poetry she is professor of russian poetry he did not write  
**Translation:** 

**[5857.92s] English:** poems but she know a lot of stuff she make a book several books and one of them is a collection of  
**Translation:** 

**[5871.92s] English:** russian poetry she have images of russian poetry  
**Translation:** 

**[5877.12s] English:** she collect all images of russian poetry  
**Translation:** 

**[5879.36s] English:** she collect all images of russian poetry  
**Translation:** 

**[5880.00s] English:** And I ask you to do the following, you have NIPS, digit recognition, and you get 100 digits, or maybe less than 100, I don't remember, maybe 50 digits, and try from a poetical point of view, describe every image which you see, using only words of images of Russian poets.  
**Translation:** 

**[5910.00s] English:** And she did it.  
**Translation:** Vocabulary: digit: 数字; digits: 数字; poetical: 诗意

**[5940.00s] English:** And there is an algorithm when you're working using privileged information, you're doing better, much better.  
**Translation:** 

**[5949.46s] English:** So there's something there.  
**Translation:** Vocabulary: algorithm: 算法; privileged: 特权信息

**[5951.24s] English:** And there is, and you see, she unfortunately did it, the collection of digits in poetic descriptions of these digits.  
**Translation:** 

**[5969.26s] English:** Yeah.  
**Translation:** 

**[5969.30s] English:** So there's some.  
**Translation:** 

**[5970.00s] English:** Something there in that poetic description.  
**Translation:** 

**[5972.84s] English:** But I think that there is an abstract ideas on the Plato level of ideas.  
**Translation:** 

**[5980.44s] English:** Yeah, that they're there, that could be discovered.  
**Translation:** 

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
**Translation:** 

**[6005.14s] English:** Right.  
**Translation:** 

**[6005.84s] English:** Let me ask another absurd question.  
**Translation:** 

**[6010.02s] English:** We talked about mortality.  
**Translation:** 

**[6012.64s] English:** We talked about philosophy of life.  
**Translation:** 

**[6014.44s] English:** What do you think is the meaning of life?  
**Translation:** 

**[6017.44s] English:** What's the predicate for mysterious existence here on Earth?  
**Translation:** Vocabulary: predicate: 谓语

**[6023.60s] English:** I don't know.  
**Translation:** 

**[6032.96s] English:** It's very interesting.  
**Translation:** 

**[6035.70s] English:** We have in Russia, I don't know, you know, the guy Strugatsky.  
**Translation:** 

**[6043.00s] English:** They're writing pictures.  
**Translation:** 

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

**[6073.20s] English:** So that's what they're thinking about.  
**Translation:** 

**[6078.00s] English:** So the purpose of life is to create two paths.  
**Translation:** 

**[6083.60s] English:** Two paths.  
**Translation:** 

**[6084.12s] English:** As human societies.  
**Translation:** 

**[6085.98s] English:** Yes.  
**Translation:** 

**[6086.96s] English:** Simple people and more complicated people.  
**Translation:** 

**[6089.88s] English:** Which do you like best?  
**Translation:** 

**[6091.42s] English:** The simple people or the complicated ones?  
**Translation:** 

**[6093.78s] English:** I don't know.  
**Translation:** 

**[6095.62s] English:** It's just his fantasy.  
**Translation:** 

**[6098.44s] English:** But, you know, every week we have a guy who is just a writer and also a theoretic of literature.  
**Translation:** 

**[6111.72s] English:** And he explains.  
**Translation:** Vocabulary: theoretic: 理论家

**[6113.60s] English:** How is he going to write?  
**Translation:** 

**[6118.32s] English:** And how is he going to write?  
**Translation:** 

**[6120.78s] English:** Are you going to write a story entire?  
**Translation:** 

**[6121.02s] English:** Do you go to a library and write what's going on on a paper?  
**Translation:** 

**[6121.14s] English:** How is he going to work on a notebook?  
**Translation:** 

**[6121.54s] English:** And how do you warm up on a desk?  
**Translation:** 

**[6122.08s] English:** How does he a good reader?  
**Translation:** 

**[6122.64s] English:** Do you have a job?  
**Translation:** 

**[6123.22s] English:** Or how is he going to mundial?  
**Translation:** 

**[6123.24s] English:** Because the human difference between this and life has two parts.  
**Translation:** 

**[6123.56s] English:** And when he about five years show up on the internet, he is doing such a great job.  
**Translation:** 

**[6123.60s] English:** He begins toって take notes and he tells.  
**Translation:** 

**[6124.14s] English:** If, for instance, he does the training, he just tells, he brings their assistant,  
**Translation:** 

**[6125.28s] English:** and we'll give you a little secret.  
**Translation:** 

**[6125.60s] English:** He gives a note to that.  
**Translation:** 

**[6125.70s] English:** Because year after year, watching this, you may hear in the chat.  
**Translation:** 

**[6126.06s] English:** It'll come on something and who knows, you might see it here.  
**Translation:** 

**[6120.00s] English:** and i understood that i'm just small kids comparing to him he is very smart guy in  
**Translation:** 

**[6131.36s] English:** understanding life he knows this predicate he knows big blocks of like i i am used every time  
**Translation:** 

**[6141.86s] English:** when i listen to him and he just talking about literature and i think that i was  
**Translation:** Vocabulary: predicate: 谓语

**[6148.94s] English:** surprised uh so the the managers in big companies most of them are guys who study  
**Translation:** 

**[6165.80s] English:** english language and english literature so why because they understand life  
**Translation:** 

**[6174.02s] English:** they understand models and among them  
**Translation:** 

**[6177.78s] English:** my  
**Translation:** 

**[6178.92s] English:** my  
**Translation:** 

**[6178.94s] English:** , there may be many talented critics  
**Translation:** 

**[6183.82s] English:** which just analyzing this and this is big science like  
**Translation:** 

**[6189.02s] English:** prop did this is blocks  
**Translation:** 

**[6193.18s] English:** that's very small  
**Translation:** 

**[6197.34s] English:** it amazes me that you are and continue to be humbled by the brilliance of others  
**Translation:** Vocabulary: brilliance: 卓越

**[6202.86s] English:** i'm very modest about myself i see so smart guys around  
**Translation:** 

**[6208.92s] English:** well let me be immodest for you  
**Translation:** Vocabulary: immodest: 不谦虚

**[6211.72s] English:** you're one of the greatest mathematical statisticians of our time  
**Translation:** 

**[6216.04s] English:** it's truly an honor thank you for talking again  
**Translation:** Vocabulary: mathematical: 数学的; statisticians: 统计学家

**[6218.06s] English:** and lets talk  
**Translation:** 

**[6219.78s] English:** it'm not  
**Translation:** 

**[6222.18s] English:** yeah  
**Translation:** 

**[6224.74s] English:** let's let's talk again when your challenges taken on and solved by grad student  
**Translation:** 

**[6231.84s] English:** especially  
**Translation:** 

**[6234.84s] English:** i hope this will happen  
**Translation:** 

**[6236.74s] English:** maybe music will be involved  
**Translation:** 

**[6238.60s] English:** Vladimir, thank you so much.  
**Translation:** 

**[6240.00s] English:** been thank you very much thanks for listening to this conversation with vladimir vapnik and thank  
**Translation:** 

**[6245.90s] English:** you to our presenting sponsor cash app download it use code lex podcast you'll get ten dollars  
**Translation:** 

**[6252.40s] English:** and ten dollars will go to first an organization that inspires and educates young minds to become  
**Translation:** 

**[6257.40s] English:** science and technology innovators of tomorrow if you enjoy this podcast subscribe on youtube  
**Translation:** Vocabulary: educates: 教育; innovators: 创新者; inspires: 启发; subscribe: 订阅

**[6263.10s] English:** give us five stars on apple podcast support it on patreon or simply connect with me on twitter  
**Translation:** 

**[6268.42s] English:** at lex friedman and now let me leave you with some words from vladimir vapnik  
**Translation:** Vocabulary: friedman: 弗里德曼; vladimir: 弗拉基米尔

**[6274.58s] English:** when solving a problem of interest do not solve a more general problem as an intermediate step  
**Translation:** 

**[6281.44s] English:** thank you for listening i hope to see you next time  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
