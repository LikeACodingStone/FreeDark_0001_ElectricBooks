# Podcast vocabulary notes
Source file: Lex Fridman - Ishan Misra： Self-Supervised Deep Learning in Computer Vision ｜ Lex Fridman Podcast #206.opus
Improved subtitle: punctuation and vocabulary regenerated from current config.

**[0.00s] English:** The following is a conversation with Ishan Mizra, research scientist at Facebook AI Research.  
**Translation:** 

**[5.94s] English:** Who works on self-supervised machine learning in the domain of computer vision, or in other words,  
**Translation:** 

**[12.16s] English:** Making AI systems understand the visual world with minimal help from us humans. Transformers.  
**Translation:** 

**[18.92s] English:** And self-attention has been successfully used by OpenAI's GPT-3 and other language models to do.  
**Translation:** Vocabulary: minimal: 最少的

**[25.94s] English:** Self-supervised learning in the domain of language. Ishan, together with Jan LeCun and others,  
**Translation:** 

**[31.76s] English:** Is trying to achieve the same success in the domain of images and video. The goal is to leave  
**Translation:** 

**[37.76s] English:** A robot watching YouTube videos all night, and in the morning comes back to a much smarter robot.  
**Translation:** 

**[43.56s] English:** I read the blog post "Self-Supervised Learning: The Dark Matter of Intelligence" by Ishan and Jan.  
**Translation:** 

**[49.40s] English:** LeCun, and then listened to Ishan's appearance on the excellent "Machine Learning Street Talk.  
**Translation:** 

**[55.92s] English:** Podcast, and I knew I had to talk to him. By the way, if you're interested in machine learning,...  
**Translation:** 

**[61.42s] English:** And AI, I cannot recommend the ML Street Talk podcast highly enough. Those guys are great.  
**Translation:** 

**[69.50s] English:** Quick mention of our sponsors: Onnit, The Information, Grammarly, and Athletic Greens.  
**Translation:** Vocabulary: grammarly: 语法检查软件; sponsors: 赞助商

**[75.12s] English:** Check them out in the description to support this podcast. As a side note, let me say that for those  
**Translation:** 

**[80.84s] English:** Of those of you who may have been listening for quite a while, this podcast used to be called Artificial.  
**Translation:** 

**[85.40s] English:** Intelligence.  
**Translation:** 

**[85.92s] English:** Because my life passion has always been, will always be, artificial intelligence.  
**Translation:** 

**[92.62s] English:** Both, narrowly and broadly defined, my goal with this podcast is still to have many conversations.  
**Translation:** 

**[98.92s] English:** With world-class researchers in AI, math, physics, biology, and all the other sciences.  
**Translation:** Vocabulary: broadly: 广泛地

**[104.96s] English:** But I also want to talk to historians, musicians, athletes, and, of course, occasionally comedians.  
**Translation:** 

**[111.18s] English:** In fact, I'm trying out doing this podcast three times a week now to give me more.  
**Translation:** Vocabulary: comedians: 喜剧演员

**[115.92s] English:** Freedom with guest selection, and maybe get a chance to have a bit more.  
**Translation:** 

**[120.00s] English:** Fun. Speaking of fun, in this conversation, I challenge the listener to count the number of  
**Translation:** Vocabulary: listener: 听众

**[125.04s] English:** Times the word "banana" is mentioned. Ishan and I use the word banana as the canonical example.  
**Translation:** 

**[132.12s] English:** At the core of the hard problem of computer vision, and maybe the hard problem of consciousness.  
**Translation:** Vocabulary: canonical: 标准例证; consciousness: 意识

**[139.56s] English:** This is the Lex Friedman Podcast, and here is my conversation with Ishan Mizra.  
**Translation:** 

**[146.02s] English:** What is self-supervised learning? And maybe even give an overview of what supervised learning is.  
**Translation:** 

**[153.66s] English:** And semi-supervised learning. And, maybe, why is self-supervised learning a better term than...  
**Translation:** 

**[158.40s] English:** Unsupervised learning? Let's start with supervised learning. So, typically, for machine learning,...  
**Translation:** Vocabulary: supervised: 有监督的; unsupervised: 无监督的

**[163.22s] English:** Systems are trained by getting a bunch of humans to point out particular features or data points.  
**Translation:** 

**[168.06s] English:** Concepts. So, if it's in the case of images, you want the humans to come and tell you what is.  
**Translation:** 

**[172.30s] English:** Present in the image, draw boxes around them.  
**Translation:** 

**[176.02s] English:** Masks of, like, things, pixels, which are of particular categories or not. For NLP, again,  
**Translation:** Vocabulary: pixels: 像素

**[181.38s] English:** There are, like, lots of these particular tasks, such as sentiment analysis and entailment.  
**Translation:** 

**[185.52s] English:** And so on. So, typically, for supervised learning, we get a large corpus of such annotated or labeled  
**Translation:** Vocabulary: annotated: 标注过的; corpus: 语料库; entailment: 蕴含; labeled: 标记过的; sentiment: 情感分析

**[190.46s] English:** Data, and then we feed that to a system, and the system is really trying to mimic. So, it's taking,...  
**Translation:** 

**[195.44s] English:** This input of the data and then trying to mimic the output. So, it looks at an image, and the  
**Translation:** 

**[199.90s] English:** Human has tagged that this image contains a banana, and now the system is basically trying...  
**Translation:** 

**[204.02s] English:** To mimic that, so that's its learning signal.  
**Translation:** Vocabulary: tagged: 标注了

**[206.02s] English:** And so, for supervised learning, we try to gather lots of such data, and we train these models using that data.  
**Translation:** 

**[210.80s] English:** Machine learning models to imitate the input or output. And the hope is, basically, by:  
**Translation:** Vocabulary: imitate: 模仿

**[214.66s] English:** Doing so, now on unseen or, like, new kinds of data, this model can automatically learn.  
**Translation:** 

**[219.94s] English:** To predict these concepts, so this is a standard, sort of, supervised setting. For semi-supervised,...  
**Translation:** 

**[224.90s] English:** Setting, the idea typically is that you have, of course, all of the supervised data, but...  
**Translation:** 

**[229.44s] English:** You have lots of other data which is unsupervised or which is, like, not labeled. Now, the problem,  
**Translation:** 

**[234.14s] English:** Basically, with supervised learning, and why you actually have to do this is that you have,  
**Translation:** 

**[236.02s] English:** Obviously, all of these are alternative sorts of learning paradigms, such as supervised learning.  
**Translation:** Vocabulary: paradigms: 范式

**[240.00s] English:** Does not scale, so if you look at the largest ones in computer vision, it just doesn't work.  
**Translation:** 

**[245.20s] English:** Most popular data sets is ImageNet, right? So, the entire ImageNet data set has about 22,000 concepts.  
**Translation:** 

**[251.60s] English:** And, about 14 million images, so these concepts are basically just nouns and they're annotated.  
**Translation:** 

**[256.72s] English:** On images, and this entire data set was a mammoth data collection effort; it actually  
**Translation:** Vocabulary: mammoth: 巨大的

**[261.68s] English:** Gave rise to a lot of powerful learning algorithms, is credited with, sort of, the rise of deep.  
**Translation:** 

**[265.76s] English:** Learning as well, but this data set took about 22 human years to collect and annotate, and it's  
**Translation:** Vocabulary: annotate: 标注

**[272.00s] English:** Not even that many concepts; right? It's not even that many images—14 million is nothing, really.  
**Translation:** 

**[276.64s] English:** Like you have, you have about 400 million images or so, or even more than that, uploaded to  
**Translation:** 

**[280.96s] English:** Most of the popular social media websites today, however, don't just rely on supervised learning anymore.  
**Translation:** 

**[285.92s] English:** Scale, if I want to, now annotate more concepts; if I want to have this various types of fine.  
**Translation:** Vocabulary: supervised: 监督学习

**[290.32s] English:** Grain concepts, then it won't really scale. So, now you come up to these sorts of different learning.  
**Translation:** 

**[294.96s] English:** Paradigms, first.  
**Translation:** 

**[295.76s] English:** Example of semi-supervised learning, where the idea is, of course, you have this annotated corpus of  
**Translation:** 

**[300.00s] English:** Supervised data, and you have lots of these unlabeled images, and the idea is that the  
**Translation:** Vocabulary: annotated: 标注过的; corpus: 语料库; unlabeled: 未标注

**[304.48s] English:** An algorithm should basically try to measure some kind of consistency, or really try to measure.  
**Translation:** 

**[308.72s] English:** Some kind of signal on this sort of unlabeled data to make itself more confident about what.  
**Translation:** Vocabulary: algorithm: 算法

**[314.56s] English:** It's really trying to predict, so by accessing a lot of unlabeled data, the idea is that the  
**Translation:** 

**[321.12s] English:** An algorithm actually learns to be more confident and gets better at predicting these concepts.  
**Translation:** Vocabulary: accessing: 访问外存数据

**[326.72s] English:** And now, we come to the other extreme, which is like self-supervised learning.  
**Translation:** 

**[330.32s] English:** The idea basically is that the machine or the algorithm should really discover  
**Translation:** 

**[334.16s] English:** Concepts, or discover things about the world, or learn representations about the  
**Translation:** 

**[337.76s] English:** World, which are useful without access to explicit human supervision, so the words:  
**Translation:** Vocabulary: explicit: 明确; representations: 表示; supervision: 监督

**[342.16s] English:** Supervision is still in the term "self-supervised." So, what is the supervision signal? Maybe  
**Translation:** 

**[349.36s] English:** That, perhaps, is when Yan Macun and you argue that "unsupervised" is the incorrect terminology here so.  
**Translation:** Vocabulary: terminology: 术语; unsupervised: 无监督

**[355.12s] English:** What is the supervision signal when the humans aren't part of the picture, or not?  
**Translation:** 

**[360.00s] English:** A big part of the picture, right? So, self-supervised: the reason it has the term "supervised" in itself is  
**Translation:** 

**[366.96s] English:** Because you're using the data itself as supervision, so because the data serves as its own guide.  
**Translation:** 

**[372.02s] English:** Own source of supervision is self-supervised in that way. Now, the reason a lot of people, I mean,...  
**Translation:** 

**[376.64s] English:** We did it in that blog post with Yan, but a lot of other people have also argued for using this.  
**Translation:** 

**[380.70s] English:** Term "self-supervised": So, starting from around 1994 from Virginia DeSa's group at UCSD, I think.  
**Translation:** 

**[386.90s] English:** Now, she's at UCSD. Uh, Jeetendra Malik has said this a bunch of times as well, so you have supervised.  
**Translation:** 

**[392.48s] English:** And then, unsupervised basically means everything which is not supervised, but that includes stuff.  
**Translation:** Vocabulary: jeetendra: 杰特伦德拉; malik: Malik; supervised: 监督学习

**[397.54s] English:** Like semi-supervised, that includes other types like transductive learning, lots of other sorts of  
**Translation:** 

**[402.04s] English:** Settings, so that's the reason why people are now preferring this term "self-supervised.  
**Translation:** Vocabulary: transductive: 推断学习

**[407.22s] English:** It explicitly says that what's happening: the data itself is the source of supervision, and any sort  
**Translation:** 

**[412.20s] English:** Of learning algorithms, which try to extract just sort of data supervision signals.  
**Translation:** Vocabulary: explicitly: 明确地; extract: 提取

**[416.88s] English:** From the data itself, a self-supervised algorithm is used, but there is also a set of tricks within the data.  
**Translation:** 

**[423.40s] English:** Unlock the supervision right. So, can you give maybe some examples? And there's a lot of innovation.  
**Translation:** Vocabulary: algorithm: 算法; supervision: 监督; unlock: 解锁

**[430.08s] English:** Ingenuity is required to unlock that supervision. The data doesn't just speak to you; some ground truth is needed.  
**Translation:** 

**[435.50s] English:** You have to do some kind of trick, uh. So I don't know what your favorite domain is, so you specifically...  
**Translation:** Vocabulary: ingenuity: 巧妙构思

**[440.40s] English:** Specialize in visual learning, but are there any favorite examples, maybe in language or other domains?  
**Translation:** 

**[446.28s] English:** Perhaps.  
**Translation:** Vocabulary: specialize: 专注于

**[446.88s] English:** The most successful applications have been in NLP, not language processing. So, the idea basically...  
**Translation:** 

**[451.96s] English:** Being that you can train models that allow you to have a sentence and mask out certain words,  
**Translation:** 

**[457.00s] English:** And now, these models learn to predict the masked-out words. So, if you have something like "the cat jumped over,  
**Translation:** 

**[462.66s] English:** The dog, so you can basically mask out the cat, and now you are essentially asking the model to predict.  
**Translation:** 

**[467.76s] English:** What was missing? What did I mask out, so the model is going to predict basically a distribution over?  
**Translation:** 

**[473.34s] English:** All the possible words that it knows, and probably it has a lot of information about the language.  
**Translation:** 

**[476.88s] English:** Like, if it's a well-trained model, it has a sort of higher performance.  
**Translation:** 

**[480.00s] English:** Density for this word, "cat," for vision, I would say the sort of more, uh, easier example.  
**Translation:** 

**[487.34s] English:** Which is not as widely used these days is basically, say, for example, video prediction.  
**Translation:** 

**[491.52s] English:** So, video is again a sequence of things. So, you can ask the model: if you have a video of, say, 10  
**Translation:** 

**[496.56s] English:** In just the first nine seconds, you can feed information into the model and then ask, "What happens?  
**Translation:** 

**[501.16s] English:** Basically, in just 10 seconds, can you predict what's going to happen? And the idea is because  
**Translation:** 

**[506.12s] English:** The model is predicting something about the data itself, of course, you didn't need any human intervention.  
**Translation:** 

**[511.26s] English:** To tell you what was happening, because the 10-second video was naturally captured because the  
**Translation:** 

**[515.08s] English:** The model is predicting what's happening there; it's going to automatically learn something about the  
**Translation:** 

**[519.28s] English:** Structure of the world, how objects move, object permanence, and these kinds of things—uh, so like:  
**Translation:** Vocabulary: permanence: 持久性

**[524.30s] English:** If I have something at the edge of the table, it will fall down, things like these, which you really  
**Translation:** 

**[528.58s] English:** Don't have to sit and annotate in a supervised learning setting; I would have to sit and annotate.  
**Translation:** Vocabulary: annotate: 标注; supervised: 监督

**[532.20s] English:** This is a cup. Now, I move this cup. This is still a cup, and now I move this cup; it's  
**Translation:** 

**[536.10s] English:** Still, there's a cup, and then it falls down. This is a fallen cup, so I won't have to annotate all of it.  
**Translation:** 

**[539.78s] English:** Of these things in a self-supervised setting, isn't that kind of a brilliant little trick?  
**Translation:** 

**[544.34s] English:** Of taking a series of consistent data, and removing one element from that series, and then...  
**Translation:** 

**[552.78s] English:** Teaching the algorithm to predict that element isn't that, first of all, quite brilliant.  
**Translation:** 

**[559.20s] English:** Um, it seems to be applicable in anything that has the constraint of being  
**Translation:** Vocabulary: algorithm: 计算方法; constraint: 限制条件

**[566.00s] English:** Unbiased, unbiased, and unbiased.  
**Translation:** 

**[566.08s] English:** Unbiased, unbiased, and unbiased—a sequence that is consistent with the physical.  
**Translation:** Vocabulary: unbiased: 无偏见的

**[569.28s] English:** Reality, um, the question is: Are there other tricks like this that can generate the uh  
**Translation:** 

**[576.08s] English:** Self-supervised signal, so sequence is possibly the most widely used one in NLP.  
**Translation:** 

**[581.12s] English:** For vision, the one that is actually used for like images, which is very popular these days.  
**Translation:** 

**[585.76s] English:** Is basically taking an image and now taking different crops of that image, so you can.  
**Translation:** 

**[590.32s] English:** Basically, decide to crop the top left corner, and you can also crop the bottom right corner.  
**Translation:** 

**[595.28s] English:** You can basically decide to crop, say, the top left corner, and then crop, say, the bottom right corner, and ask a network.  
**Translation:** 

**[595.98s] English:** Asking a network to basically present it with a choice, saying that okay,  
**Translation:** 

**[600.00s] English:** You have this image. Are these the same, or not? And so, the idea basically is that...  
**Translation:** 

**[605.60s] English:** Because, in an image, different parts of the image are going to be related.  
**Translation:** 

**[609.68s] English:** So, for example, if you have a chair and a table, basically these things are going to be close by.  
**Translation:** 

**[614.88s] English:** Versus, if you take a zoomed-in picture of a chair, if you're taking different  
**Translation:** 

**[620.08s] English:** Crops: It's going to be different parts of the chair, so the idea basically is that different...  
**Translation:** 

**[624.48s] English:** Crops of the image are related, and so the features or the representations that you get from these  
**Translation:** 

**[628.40s] English:** Different crops should also be rotated, so this is possibly the most widely used trick; these  
**Translation:** Vocabulary: representations: 表示; rotated: 旋转

**[632.80s] English:** Days for self-supervised learning in computer vision, so again using the consistency that's  
**Translation:** 

**[638.48s] English:** Inherent to physical reality in the visual domain is that parts of an image are consistent.  
**Translation:** 

**[645.52s] English:** And then, in the language domain or anything that has sequences, like language, or something.  
**Translation:** 

**[651.44s] English:** That's like a time series, then you can chop up parts over time. It's similar to the story of...  
**Translation:** 

**[657.36s] English:** RNNs and  
**Translation:** 

**[658.40s] English:** CNN's "On RNNs and Covenants": You and Jan Lacoon wrote the blog post in March 2021, titled  
**Translation:** Vocabulary: covenants: 担保条款

**[667.52s] English:** Self-Supervised Learning: The Dark Matter of Intelligence. Can You Summarize This Blog?  
**Translation:** 

**[672.16s] English:** Post, and maybe explain the main idea or set of ideas the blog post was mainly about, sort of.  
**Translation:** 

**[677.68s] English:** Just telling, I mean, this is really an accepted fact, I would say, for a lot of people now that.  
**Translation:** 

**[682.96s] English:** Self-supervised learning is something that is going to play an important role for machines.  
**Translation:** 

**[687.44s] English:** Learning algorithms that are going to play an important role in machine learning algorithms that  
**Translation:** 

**[688.32s] English:** Come in the future, and even now, well, let me just comment that we don't yet have a good  
**Translation:** 

**[694.24s] English:** Understanding what dark matter is, that's true, so the idea and the metaphor don't exactly transfer.  
**Translation:** 

**[701.76s] English:** But maybe, maybe it's actually perfectly fine that we don't know wherever we have an inkling.  
**Translation:** Vocabulary: inkling: 模糊的概念; metaphor: 比喻

**[707.76s] English:** That it'll be a big part of whatever solving intelligence looks like, right? So I think self.  
**Translation:** 

**[712.24s] English:** Super obviously, I think the way it's done right now is, I would say, like the first step towards.  
**Translation:** 

**[716.48s] English:** What it probably should end up being is Pun Broom and his work ass is probably going to end up like learning.  
**Translation:** 

**[718.32s] English:** Or what it should enable us to do.  
**Translation:** 

**[720.00s] English:** Yeah, so the idea for that particular piece was that self-supervised learning is going to be a very  
**Translation:** 

**[725.58s] English:** A powerful way to learn common sense about the world, or stuff that is really hard to label.  
**Translation:** 

**[730.18s] English:** For example, like is this piece over here heavier than the cup? Now, for all these kinds of things.  
**Translation:** 

**[737.44s] English:** You'll have to sit and label these things, so supervised learning is clearly not going to scale.  
**Translation:** Vocabulary: supervised: 监督学习

**[740.78s] English:** So, what is the thing that's actually going to scale? It's probably going to be an agent that  
**Translation:** 

**[745.14s] English:** Can either actually interact with it to lift it up, or observe me doing it. So, if I'm basically...  
**Translation:** 

**[750.64s] English:** Lifting these things up, it can probably reason about: hey, this is taking him more time to lift up.  
**Translation:** 

**[754.48s] English:** Or the velocity is different, whereas the velocity for this is different—probably because this one is heavier.  
**Translation:** 

**[758.90s] English:** So, essentially, by observing the data, you should be able to infer a lot of things about.  
**Translation:** 

**[764.36s] English:** The world, without someone explicitly telling you this, is heavy. This is not just something that;  
**Translation:** 

**[769.40s] English:** Can pour this is something that cannot be poured. This is somewhere that you can sit. This is not somewhere.  
**Translation:** 

**[773.04s] English:** That you can sit, but you just mentioned  
**Translation:** 

**[774.96s] English:** You just mentioned that  
**Translation:** 

**[775.14s] English:** Ability to interact with the world—there are so many questions that are yet to be answered and still.  
**Translation:** 

**[781.74s] English:** Open, which is how do you select a set of data over which the self-supervised learning process?  
**Translation:** 

**[787.66s] English:** Works: How much interactivity, like in the active learning or the machine teaching context, is there?  
**Translation:** 

**[793.84s] English:** What are the reward signals like, and how much actual interaction is there with the physical world?  
**Translation:** 

**[799.58s] English:** That kind of thing, uh, so that's a big question, and then  
**Translation:** 

**[804.96s] English:** On top of that, there are a lot of questions about how you select a set of data over which the  
**Translation:** 

**[805.12s] English:** Self-supervised learning processes work, how much interactivity is similar to that in active learning or the  
**Translation:** 

**[805.14s] English:** On top of that, there are a lot of questions about how you select a set of data over which the  
**Translation:** 

**[805.64s] English:** Self-supervised learning processes work, how much interactivity is similar to that in active learning or the  
**Translation:** 

**[806.14s] English:** At the top of that, which I have a million questions about which we don't know the answers to, but it's worth  
**Translation:** 

**[811.34s] English:** Talking about is how much reasoning is involved, how much accumulation of knowledge versus something.  
**Translation:** Vocabulary: accumulation: 累积知识

**[819.10s] English:** That's more akin to learning, or whether that's the same thing. But we're like, it is truly...  
**Translation:** 

**[825.66s] English:** Dark matter—we don't know how exactly to do it, yeah, but we are—I mean, a lot of us are actually.  
**Translation:** 

**[831.50s] English:** Convinced that it's going to be a sort of major thing in machine learning, so let me know in the  
**Translation:** 

**[835.12s] English:** Let me reframe it, then: human supervision cannot be  
**Translation:** Vocabulary: cannot: 不能; reframe: 重新表述; supervision: 监督

**[840.00s] English:** At a large scale, the source of the solution to intelligence is right there. So, we have the machines.  
**Translation:** 

**[845.84s] English:** Have to discover the supervision in the natural signals of the world, right? I mean, the other thing.  
**Translation:** 

**[850.96s] English:** Is also that humans are not particularly good labelers; they're not very consistent.  
**Translation:** 

**[855.60s] English:** Uh, for example, like what's the difference between a dining table and a table? Is it just the fact,  
**Translation:** Vocabulary: dining: 就餐; labelers: 贴标签者

**[860.56s] English:** That one: If you just look at a particular table, what makes us say one is a dining table and  
**Translation:** 

**[864.64s] English:** The other is not that humans are not particularly consistent; they're not very good sources of.  
**Translation:** 

**[869.52s] English:** Supervision for a lot of these kinds of edge cases, so it may also be the fact that if we want,...  
**Translation:** 

**[875.44s] English:** Like, wanting an algorithm or wanting a machine to solve a particular task for us, we can maybe  
**Translation:** Vocabulary: algorithm: 计算方法

**[879.92s] English:** Just specify the end goal, um, and like the stuff in between, uh, we really probably shouldn't be.  
**Translation:** 

**[885.52s] English:** Specifying, because we're not necessarily going to confuse it a lot, actually; well, humans can't.  
**Translation:** Vocabulary: specify: 明确说明; specifying: 明确说明

**[890.08s] English:** Even answering the meaning of life, so we don't; I'm not sure if we're good supervisors at the end.  
**Translation:** 

**[894.24s] English:** Goal: Either, so let me ask you about categories—humans are not very good at telling the difference.  
**Translation:** Vocabulary: supervisors: 监督者

**[899.52s] English:** Is or isn't a table like you mentioned? Um, do you think it's possible? Let me ask you this:  
**Translation:** 

**[906.80s] English:** Pretend you're Plato: Is it possible to create a pretty good taxonomy of objects in the world?  
**Translation:** Vocabulary: taxonomy: 分类学

**[916.24s] English:** It seems like a lot of approaches in machine learning kind of assume  
**Translation:** 

**[920.24s] English:** A hopeful vision that it's possible to construct the perfect taxonomy, or perhaps it exists out of  
**Translation:** Vocabulary: approaches: 方法

**[925.92s] English:** Our reach, but we can always get closer and closer to it, or is that a hopeful vision?  
**Translation:** 

**[929.52s] English:** Or, a hopeless pursuit—I think it's hopeless in some way. So, the thing is, for any particular  
**Translation:** Vocabulary: pursuit: 追求

**[935.20s] English:** Categorization that you create, if you have a discrete, sort of categorization, I can always  
**Translation:** 

**[939.20s] English:** Take the nearest two concepts, or I can take a third concept and blend it in, and I can  
**Translation:** Vocabulary: categorization: 分类; discrete: 离散的

**[942.72s] English:** Create a new category, yeah. So, if you were to enumerate n categories, I will always find an  
**Translation:** 

**[947.44s] English:** N+1 category for you, that's not going to be in the final categories, and I can actually create  
**Translation:** Vocabulary: enumerate: 列举

**[951.52s] English:** Not just N+1, I can very easily create far more than N categories. The thing is, a lot of things...  
**Translation:** 

**[959.52s] English:** It was really hard.  
**Translation:** 

**[960.00s] English:** For us to come and sit and enumerate all of these out, and they compose in various weird ways, right?  
**Translation:** 

**[965.36s] English:** Like, you have a croissant and a donut come together to form a cronut, so if you were to  
**Translation:** Vocabulary: compose: 组成; croissant: 羊角面包; donut: 甜甜圈

**[970.60s] English:** Enumerate all the foods up until I don't know—whether the cronut was around 10 years ago or 15.  
**Translation:** 

**[975.46s] English:** Years ago, then this entire thing called cronut wouldn't have existed. Yeah, I remember there was a  
**Translation:** 

**[980.04s] English:** The most awesome video of a cat wearing a monkey costume.  
**Translation:** 

**[983.32s] English:** People should look it up; it's great! So, is that a monkey? Is that or is that a cat? It's a very  
**Translation:** Vocabulary: costume: 服装

**[991.64s] English:** Difficult philosophical question: so, there is a concept of similarity between objects, so you think?  
**Translation:** 

**[997.72s] English:** That can take us very far, just kind of getting a good function and a good way to tell which parts.  
**Translation:** Vocabulary: philosophical: 哲学的; similarity: 相似性

**[1006.42s] English:** Of things, some are similar and which parts of things are very different. I think so; yeah, so you don't.  
**Translation:** 

**[1012.74s] English:** Necessarily, we do not need to know which parts of things are similar and which parts of things are very.  
**Translation:** 

**[1013.30s] English:** Different; you don't need to name everything or assign a name to everything to be able to use it.  
**Translation:** 

**[1016.72s] English:** Right, so there are lots of things Shakespeare said, like "What's in a name?" Yeah, okay.  
**Translation:** Vocabulary: assign: 分配

**[1022.70s] English:** And I mean, a lot—lots of, like, for example, animals; they don't have necessarily a well-formed  
**Translation:** 

**[1028.04s] English:** Like with a syntactic language, but they're able to go about their day as usual. The same thing happens.  
**Translation:** Vocabulary: syntactic: 句法的

**[1032.50s] English:** For us, so I mean, we probably look at things and figure out, "Oh, this is similar to something else.  
**Translation:** 

**[1038.46s] English:** That I've seen before, and then I can probably learn how to use it. So, I have a lot of experience.  
**Translation:** 

**[1043.28s] English:** With this kind of stuff, but I haven't seen all the possible doorknobs in the world. But if you show me,...  
**Translation:** 

**[1048.66s] English:** Like I was able to get into this particular place fairly easily, I've never seen that particular  
**Translation:** Vocabulary: doorknobs: 门把手

**[1052.40s] English:** Doorknob—so, I of course, related to all the doorknobs that I've seen, and I know exactly.  
**Translation:** 

**[1056.24s] English:** How it's going to open, I have a pretty good idea of how it's going to open, and I think this.  
**Translation:** Vocabulary: doorknob: 门把手

**[1061.04s] English:** Kind of translation between experiences only happens because of similarity, because I'm able  
**Translation:** 

**[1065.36s] English:** To relate it to a doorknob, if I related it to a hair dryer, I would probably be stuck still outside.  
**Translation:** 

**[1069.20s] English:** Not able to get in again; a bit of a philosophical question, but  
**Translation:** 

**[1073.28s] English:** Is there a similarity that can take us all the way to understanding a thing, or do we need more than just its function?  
**Translation:** 

**[1080.00s] English:** That compares objects gets us to understand something profound about singular objects.  
**Translation:** 

**[1086.42s] English:** I think I'll ask you a question back: What does it mean to understand objects?  
**Translation:** Vocabulary: profound: 深奥的

**[1090.16s] English:** Well, let me tell you what—that's similar to, no, uh, I suppose there's an idea of sort of  
**Translation:** 

**[1097.26s] English:** Reasoning by analogy, kind of thing—I think understanding is the process of placing that.  
**Translation:** Vocabulary: analogy: 类比

**[1104.36s] English:** Thing in some kind of network of knowledge that you have; it perhaps is fundamentally related.  
**Translation:** 

**[1111.62s] English:** To other concepts, so it's not like understanding is fundamentally related by the composition of.  
**Translation:** Vocabulary: fundamentally: 根本上

**[1118.06s] English:** Other concepts, and maybe in relation to other concepts; um, and maybe like deeper and deeper.  
**Translation:** 

**[1124.98s] English:** Understanding might be just adding more edges to that graph, somehow. So, maybe it is.  
**Translation:** 

**[1132.80s] English:** A composition of  
**Translation:** 

**[1134.26s] English:** A  
**Translation:** 

**[1134.34s] English:** A  
**Translation:** 

**[1134.36s] English:** I mean, ultimately, it is, I suppose, a kind of embedding in that wisdom.  
**Translation:** Vocabulary: embedding: 嵌入

**[1140.42s] English:** Space, yeah, okay, wisdom is good. Uh, I think—I do think—that's right. So, similarity does.  
**Translation:** 

**[1149.08s] English:** Get you very, very far is it the answer to everything? I mean, I don't even know what.  
**Translation:** 

**[1153.50s] English:** Everything is, but it's going to take us really far. Um, and I think the thing is, things are similar.  
**Translation:** 

**[1159.52s] English:** In very different contexts, right? So, an elephant is similar to—I don't know; I don't know; I don't.  
**Translation:** 

**[1164.34s] English:** I don't know lions and some other creatures in a different way because they're both four-legged creatures.  
**Translation:** 

**[1170.16s] English:** Uh, they're also land animals, but of course, they're very different in many different ways, so...  
**Translation:** 

**[1173.92s] English:** Elephants are like herbivores, um, similar to lions in some ways, but particularly...  
**Translation:** 

**[1179.44s] English:** Dissimilarity also actually helps us understand a lot about things, and so that's actually why.  
**Translation:** Vocabulary: herbivores: 食草动物

**[1184.80s] English:** I think discrete categorization is very hard, just like forming this particular category.  
**Translation:** 

**[1189.28s] English:** Of elephants and a particular category of lions, maybe it's good for, just like taxonomy, or  
**Translation:** Vocabulary: categorization: 分类; discrete: 离散的; taxonomy: 分类学

**[1194.34s] English:** Biological taxonomies. But when it comes to other things, which are not as clearly defined, for example,  
**Translation:** 

**[1200.00s] English:** Example, like grilled cheese: I have a grilled cheese, I dip it in tomato, and I keep it outside.  
**Translation:** Vocabulary: taxonomies: 分类体系

**[1203.76s] English:** Now, is that still a grilled cheese, or is that something else? Right? So, categorization is still...  
**Translation:** 

**[1209.18s] English:** Very useful for solving problems, but is your intuition then sort of self-supervised?  
**Translation:** Vocabulary: intuition: 直觉

**[1215.68s] English:** Should be "the" to borrow Jan Lakoon's terminology, uh, "should be the cake," and then categorization.  
**Translation:** 

**[1223.48s] English:** The classification, maybe the supervised learning layer should be just like the thing on top.  
**Translation:** Vocabulary: classification: 分类; supervised: 监督; terminology: 术语

**[1229.20s] English:** Cherry, or the icing, or whatever. So, if you make it the cake, it gets in the way of learning if you...  
**Translation:** 

**[1235.68s] English:** Make it the cake, then you won't be able to sit and annotate everything. That's as simple as.  
**Translation:** Vocabulary: annotate: 注释; cherry: 樱桃

**[1240.36s] English:** It is like, that's my very practical view on it. It's just, uh, I mean, in my PhD, I sat down and  
**Translation:** 

**[1245.48s] English:** Annotated like a bunch of cards for one of my projects, and very quickly I was just like, "It was...  
**Translation:** Vocabulary: annotated: 注解

**[1250.14s] English:** In a video, I was basically drawing boxes around all these cards, and I think I spent about  
**Translation:** 

**[1254.56s] English:** A week doing all of that, and I barely got anything done. And basically, this was, I think,...  
**Translation:** 

**[1259.20s] English:** First year of my PhD, or like second year of my master's, and then by the end of it, I'm like okay.  
**Translation:** 

**[1263.96s] English:** This is just hopeless. I can keep doing it, and when I'm done that, uh, someone came up to me and  
**Translation:** 

**[1268.58s] English:** They basically told me, "Oh, this is a pickup truck; this is not a car," and that's like, "aha, this actually.  
**Translation:** 

**[1274.34s] English:** It makes sense because a pickup truck is not really what I was annotating; I was annotating something else.  
**Translation:** Vocabulary: annotating: 标注; pickup: 皮卡

**[1277.60s] English:** Anything that is mobile, or were we annotating particular sedans or SUVs?  
**Translation:** 

**[1282.56s] English:** What was I doing, by the way? The annotation was using bounding boxes, boxes. Yeah, there are so many deep.  
**Translation:** Vocabulary: annotation: 注解; bounding: 边界; sedans: 轿车

**[1289.20s] English:** Questions here that you're almost cheating your way out of by doing self-supervised learning.  
**Translation:** 

**[1293.42s] English:** By the way, what makes for an object, as opposed to something with solve intelligence, maybe you don't.  
**Translation:** Vocabulary: cheating: 作弊

**[1299.74s] English:** Ever need to answer that question? I mean, this is the question that anyone who's ever done  
**Translation:** 

**[1304.64s] English:** Annotation, because it's so painful, gets to ask, "Why am I doing this? A drawing, very careful.  
**Translation:** 

**[1312.72s] English:** Line around this object, like what, what is the value? I remember when I first saw semantic.  
**Translation:** 

**[1319.20s] English:** Annotation:  
**Translation:** Vocabulary: semantic: 语义的

**[1320.00s] English:** Where you have, for example, instant segmentation where you have a very exact line around the object,  
**Translation:** 

**[1328.42s] English:** The 2D plane of a fundamentally 3D object projected on a 2D plane, so you're drawing a line around a  
**Translation:** Vocabulary: fundamentally: 本质上; projected: 投影; segmentation: 分割

**[1334.98s] English:** Car that might be occluded, there might be another thing in front of it, but you're still drawing.  
**Translation:** 

**[1339.94s] English:** A line of the part of the car that you see: how is that the car? What makes that car look like it does?  
**Translation:** Vocabulary: occluded: 遮挡的

**[1348.18s] English:** Had a like an existential crisis every time, like, how is that going to help us understand a soft?  
**Translation:** 

**[1353.92s] English:** Computer vision—I'm not sure I have a good answer to what's better, and I'm not sure I share the  
**Translation:** Vocabulary: existential: 存在主义的

**[1359.46s] English:** Confidence that you have that self-supervised learning can take us far, I think, I'm more and  
**Translation:** 

**[1368.00s] English:** More convinced that it's a very important component, but I still feel like we need to.  
**Translation:** 

**[1372.12s] English:** Understand what makes it like this, uh?  
**Translation:** 

**[1377.92s] English:** Like this, uh, like this, uh, like this, uh, like this, uh, like this, uh, like this, uh, like this.  
**Translation:** 

**[1378.16s] English:** Dream of maybe what it's called, like symbolic AI, of arriving. Once you have this common...  
**Translation:** 

**[1384.28s] English:** Sense, you can base it on being able to play with these concepts and build graphs or hierarchies of concepts on top.  
**Translation:** Vocabulary: graphs: 图表; hierarchies: 层次结构; symbolic: 符号化的

**[1393.18s] English:** In order to then, like, form a deep sense of this three-dimensional world or four-dimensional.  
**Translation:** 

**[1401.14s] English:** World, and be able to reason and then project that onto a 2D plane in order to interpret a 2D image.  
**Translation:** Vocabulary: interpret: 解释

**[1407.82s] English:** Can I ask you just an out-of-the-blue question? I remember, I think, that Andre Kap릭 had a blog.  
**Translation:** 

**[1414.60s] English:** Post about computer vision, uh, like being really hard. I forgot what the title was, but it's many.  
**Translation:** Vocabulary: andre: 安德烈

**[1420.50s] English:** Many years ago, he had President Obama stepping on a scale, and there was humor; and there's  
**Translation:** 

**[1425.84s] English:** A bunch of people laughing, and whatever, and uh, the interesting thing is there are a lot of interesting things.  
**Translation:** Vocabulary: obama: 奥巴马

**[1431.10s] English:** About that image, and I think Andre highlighted a bunch of things about the image that us humans  
**Translation:** 

**[1436.50s] English:** Are we able to immediately understand, and I think that's a really good question, and I think that's  
**Translation:** Vocabulary: highlighted: 强调

**[1437.82s] English:** A really good question, and I think that's a really good question, and I think that's a really good one.  
**Translation:** 

**[1440.00s] English:** Gravity, and that you can have the concept of weight; you have an immediate projection.  
**Translation:** Vocabulary: gravity: 重力; projection: 投射

**[1446.00s] English:** Because of our knowledge of pose and how human bodies are constructed, you understand how the  
**Translation:** 

**[1451.88s] English:** Forces are being applied with the human body; they're really interesting. Other things that you're  
**Translation:** 

**[1456.36s] English:** Able to understand there's multiple people looking at each other in the image; uh, you're able to have  
**Translation:** 

**[1461.16s] English:** A mental model of what the people are thinking, you're able to infer, like "oh, this person...  
**Translation:** 

**[1466.06s] English:** Is probably thinking that it's pretty humorous and laughing at the situation, and this person is  
**Translation:** 

**[1472.50s] English:** Confused about what the situation is, because they're looking this way, we're able to infer all.  
**Translation:** Vocabulary: humorous: 幽默的

**[1476.64s] English:** Of that, so that's human vision. How difficult is computer vision? Like, in order to achieve that.  
**Translation:** 

**[1486.64s] English:** Level of understanding, and maybe how big of a part does self-supervised learning play in that?  
**Translation:** 

**[1493.68s] English:** Do you think, and do you still, you know?  
**Translation:** 

**[1496.06s] English:** Back, that was like over a decade ago. I think Andre and I think a lot of people agreed as.  
**Translation:** Vocabulary: andre: 安德烈

**[1501.10s] English:** Computer vision is really hard. Do you still think computer vision is really hard? I think it is, yes.  
**Translation:** 

**[1506.94s] English:** And getting to that kind of understanding, I mean, it's really out there. So, if you ask me to solve...  
**Translation:** 

**[1513.64s] English:** Just that particular problem, I can do it the supervised learning route; I can always construct.  
**Translation:** 

**[1518.30s] English:** A dataset, and basically predict: Oh, is there humor in this or not? And of course, I can do it actually.  
**Translation:** Vocabulary: dataset: 数据集; supervised: 监督

**[1522.80s] English:** That's a good question. Do you think you can okay, okay, do you think you can do?  
**Translation:** 

**[1526.04s] English:** Human-supervised annotation of humor, to some extent, yes, I'm sure it'll work. I mean, it won't be  
**Translation:** Vocabulary: annotation: 注释

**[1531.58s] English:** It won't be as bad as randomly guessing, I'm sure it can still predict whether it's humorous.  
**Translation:** 

**[1536.16s] English:** Or, in some way, yeah, maybe like Reddit upvotes is the signal. I don't know; I mean, it won't do a  
**Translation:** Vocabulary: upvotes: 投票支持

**[1541.98s] English:** Great job, but it will do something; it may actually find certain things that are not  
**Translation:** 

**[1546.44s] English:** Humorous, humorous as well, which is going to be bad for us, but I mean, it won't be random.  
**Translation:** 

**[1551.74s] English:** Yeah, kind of like my sense of humor, okay. So, fine. So, you're going to do a little bit of a  
**Translation:** 

**[1556.04s] English:** That particular problem, yes, but the general problem you're saying is hard.  
**Translation:** 

**[1560.00s] English:** The problem is hard. And I mean, self-supervised learning is not the answer to everything.  
**Translation:** 

**[1563.98s] English:** Of course, it's not. I think if you have machines that are going to communicate with humans,...  
**Translation:** 

**[1568.20s] English:** At the end of it, you want to understand what the algorithm is doing, right? You want it  
**Translation:** 

**[1571.24s] English:** To be able to produce an output that you can decipher, that you can understand, or it's  
**Translation:** Vocabulary: algorithm: 计算方法; decipher: 解读

**[1575.82s] English:** Actually, it can be useful for something else, which, again, is a human. So, at some point in this,...  
**Translation:** 

**[1581.06s] English:** Sort of an entire loop: a human steps in, and now this human needs to understand what's  
**Translation:** 

**[1585.46s] English:** Going on, and at that point, this entire notion of language or semantics really comes in.  
**Translation:** 

**[1590.00s] English:** If the machine just spits out something and if we can't understand it, then it's not really useful.  
**Translation:** Vocabulary: semantics: 语义; spits: 吐出

**[1594.76s] English:** That's useful for us. So, self-supervised learning is probably going to be useful for a lot of  
**Translation:** 

**[1599.06s] English:** The things before that part, before the machine really needs to communicate a particular kind,  
**Translation:** 

**[1603.80s] English:** Of output with a human. Because, I mean, otherwise, how is it going to do that without language?  
**Translation:** 

**[1610.10s] English:** Or some kind of communication. But you're saying that it's possible to build a big base.  
**Translation:** 

**[1614.14s] English:** Of understanding or whatever, of what's the better...  
**Translation:** 

**[1617.94s] English:** Concepts.  
**Translation:** 

**[1618.94s] English:** Concepts.  
**Translation:** 

**[1619.94s] English:** Yeah.  
**Translation:** 

**[1620.94s] English:** Like common-sense concepts.  
**Translation:** 

**[1621.94s] English:** Right.  
**Translation:** 

**[1622.94s] English:** Supervised learning in the context of computer vision is something you focused on, but that's  
**Translation:** 

**[1627.82s] English:** A really hard domain, and it's kind of the cutting edge of what we're, as a community,  
**Translation:** Vocabulary: supervised: 监督学习

**[1631.86s] English:** Working on today, can we take a little bit of a step back and look at language? Can you  
**Translation:** 

**[1636.52s] English:** Summarize the history of success of self-supervised learning in natural language processing.  
**Translation:** 

**[1642.88s] English:** Modeling? What are transformers? What is the masking, the sentence completion that you use for?  
**Translation:** 

**[1648.88s] English:** Mentioned before? How does it lead us to understand anything? Semantic meaning of words, syntactic...  
**Translation:** Vocabulary: completion: 句子完成; masking: 遮罩; semantic: 语义; syntactic: 句法

**[1655.40s] English:** The role of words and sentences?  
**Translation:** 

**[1657.74s] English:** So, I'm of course not an expert in NLP. I kind of follow it a little bit from the side.  
**Translation:** 

**[1663.60s] English:** So, the main reason why all of this masking stuff works, I think, is called  
**Translation:** 

**[1668.46s] English:** The Distributional Hypothesis in NLP: the idea basically being that words that occur  
**Translation:** Vocabulary: distributional: 分布的; hypothesis: 假设

**[1672.98s] English:** In the same context, they should have a similar meaning. So if you have "the blank jumped over the blank,  
**Translation:** 

**[1677.88s] English:** It basically  
**Translation:** 

**[1680.00s] English:** Whatever, in the first blank, is basically an object that can actually jump is going to be  
**Translation:** 

**[1684.76s] English:** Something that can jump, like a cat or a dog or, I don't know, sheep—something like all of these things.  
**Translation:** 

**[1688.90s] English:** Can basically be in that particular context, and now so essentially the idea is that if you have  
**Translation:** 

**[1694.06s] English:** Words that are in the same context, and you predict them, you're going to learn lots of useful things.  
**Translation:** 

**[1699.94s] English:** About how words are related, because you're predicting by looking at their context what  
**Translation:** 

**[1703.66s] English:** The word is "so" in this particular case, the blank jumped over the fence, so now if  
**Translation:** 

**[1708.76s] English:** It's a sheep. The sheep jumped over the fence. The dog jumped over the fence, so essentially,  
**Translation:** 

**[1713.46s] English:** Algorithm or the representation basically puts together these two concepts together, so it says:  
**Translation:** Vocabulary: algorithm: 算法

**[1718.02s] English:** Okay, dogs are going to be kind of related to sheep because both of them occur in the same context.  
**Translation:** 

**[1722.06s] English:** Of course, now you can decide, depending on your particular application, downstream, you can say.  
**Translation:** Vocabulary: downstream: 下游的

**[1727.12s] English:** Dogs are absolutely not related to sheep, because, well, I don't really care— you know, about dog food.  
**Translation:** 

**[1732.02s] English:** For example, I'm a dog food person, and I really want to give this dog food to this particular  
**Translation:** 

**[1736.12s] English:** Animal, so depending on what  
**Translation:** 

**[1738.66s] English:** You're  
**Translation:** 

**[1738.76s] English:** Your downstream application, of course, involves this notion of similarity or this notion or that notion.  
**Translation:** 

**[1743.38s] English:** Common sense that you've learned may not be applicable, but the point is basically that this.  
**Translation:** Vocabulary: similarity: 相似性

**[1747.18s] English:** Just predicting what the blanks are is going to take you really, really far. So there's a nice  
**Translation:** 

**[1752.74s] English:** A feature of language is that the number of words in a particular language is very large, but it's  
**Translation:** 

**[1760.10s] English:** Finite, and it's actually not that large in the grand scheme of things. I still have to.  
**Translation:** 

**[1765.28s] English:** We take it for granted, so first of all, when you say "masking," you're talking about a language that  
**Translation:** Vocabulary: finite: 有限的; masking: 遮掩

**[1768.66s] English:** Is very complex, and then you're talking about this very process of removing words from.  
**Translation:** 

**[1772.68s] English:** A sentence, and then having the knowledge of what word went there in the initial data set—that's  
**Translation:** 

**[1778.86s] English:** Ground truth that you're training on, and then you're asking the neural network to predict what  
**Translation:** 

**[1784.26s] English:** Goes there that that's like a little trick, yeah? It's a really powerful trick. The question is,...  
**Translation:** Vocabulary: neural: 神经网络

**[1791.56s] English:** How far does that take us, and the other question is: Is there other tricks? Because to me, it's very possible.  
**Translation:** 

**[1798.66s] English:** There's other very fascinating  
**Translation:** 

**[1800.00s] English:** Tricks. I'll give you an example. In autonomous driving, there are a bunch of tricks that give you  
**Translation:** 

**[1807.52s] English:** The self-supervised signal back. For example, very similar to sentences, but not exactly the same, which is  
**Translation:** Vocabulary: autonomous: 自主的

**[1816.82s] English:** You have signals from humans driving the car, because a lot of us drive cars to places. And so,...  
**Translation:** 

**[1824.16s] English:** You can ask the neural network to predict what's going to happen in the next two seconds.  
**Translation:** 

**[1830.00s] English:** For a safe navigation through the environment, and the signal comes from the fact that you also.  
**Translation:** 

**[1836.82s] English:** Have knowledge of what happened in the next two seconds, because you have video of the data.  
**Translation:** 

**[1842.04s] English:** The question in autonomous driving, as it is in language, is: Can we learn how to drive autonomously?  
**Translation:** 

**[1849.88s] English:** Based on that kind of self-supervision? Probably the answer is no. The question is: how good can it be?  
**Translation:** Vocabulary: autonomously: 自主地

**[1857.02s] English:** We get? And the same with language: how good can we get?  
**Translation:** 

**[1860.00s] English:** And are there other tricks? We get sometimes super excited by this trick that works really well.  
**Translation:** 

**[1865.30s] English:** Well, but I wonder; it's almost like mining for gold. I wonder how many signals there are in the  
**Translation:** 

**[1872.44s] English:** Data that could be leveraged is right there. I just want to kind of linger on that, because  
**Translation:** Vocabulary: leveraged: 利用; linger: 停留

**[1878.90s] English:** Sometimes it's easy to think that maybe this masking process is self-supervised learning.  
**Translation:** 

**[1884.02s] English:** No, it's only one method. So there could be many, many other methods, many,...  
**Translation:** 

**[1890.00s] English:** Many key methods, maybe interesting ways to leverage human computation in very interesting ways.  
**Translation:** 

**[1896.46s] English:** Ways that might actually border on semi-supervised learning, something like that. Obviously,  
**Translation:** Vocabulary: computation: 计算; leverage: 利用

**[1901.48s] English:** The Internet is generated by humans, at the end of the day. So, all that to say is: what's your sense?  
**Translation:** 

**[1908.10s] English:** In this particular context of language, how far can that masking process take us?  
**Translation:** Vocabulary: masking: 掩饰过程

**[1914.34s] English:** So it has stood the test of time, right? I mean, Word2Vec, the initial sort of NLP technique,...  
**Translation:** 

**[1919.68s] English:** That was used to do that. So it has stood the test of time, right? I mean, so Word2Vec,  
**Translation:** 

**[1919.98s] English:** The initial sort of NLP technique that was used to do that. So it has stood the test of time, right?  
**Translation:** 

**[1920.00s] English:** Using this, for example, like all the BERT and all these big models that we get,  
**Translation:** 

**[1925.76s] English:** BERT and RoBERTa, for example, all of them are still sort of based on the same principle of  
**Translation:** 

**[1929.60s] English:** Masking. It's taken us really far. I mean, you can actually do things like these two sentences.  
**Translation:** 

**[1935.20s] English:** Are they similar or not, whether this particular sentence follows this other sentence in terms of  
**Translation:** 

**[1938.88s] English:** Of logic, so entailment. You can do a lot of these things with just this masking trick.  
**Translation:** Vocabulary: entailment: 推论关系

**[1944.72s] English:** So, I'm not sure if I can predict how far it can take us, because when it first came out,  
**Translation:** 

**[1949.60s] English:** When Word2vec was released, I don't think a lot of us would have imagined that it would actually help.  
**Translation:** 

**[1955.12s] English:** We do some kind of entailment problems really well. And so, just the fact that by just scaling up,  
**Translation:** 

**[1960.80s] English:** The amount of data that we're training on, and using better and more powerful neural networks,  
**Translation:** Vocabulary: neural: 神经网络

**[1965.04s] English:** Architectures have taken us from that to this, is just showing you how maybe poor predictors we are.  
**Translation:** 

**[1972.96s] English:** As humans, how poor we are at predicting how successful a particular technique is going to be.  
**Translation:** Vocabulary: predictors: 预测者

**[1977.20s] English:** So, I think I can say something now, but like 10 years...  
**Translation:** 

**[1979.60s] English:** From now on, I look completely stupid basically predicting this.  
**Translation:** 

**[1982.16s] English:** In the language domain, is there something in your work that you find useful and insightful?  
**Translation:** 

**[1989.44s] English:** And it's both transferable to computer vision, but also just, I don't know, beautiful and profound.  
**Translation:** Vocabulary: profound: 深奥; transferable: 可移植

**[1995.76s] English:** I think it carries through to the vision domain? I mean, the idea of masking has been  
**Translation:** 

**[2000.24s] English:** Very powerful. It has been used in vision tasks as well for predicting, like you say, the next sort of.  
**Translation:** Vocabulary: masking: 遮罩技术

**[2005.20s] English:** If you have n sorts of frames and you predict what's going to happen in the next frame, so  
**Translation:** 

**[2009.60s] English:** That's been very powerful. In terms of modeling, and just in terms of architecture,  
**Translation:** 

**[2014.00s] English:** I think you would have asked about transformers a while back. That has really become like it has.  
**Translation:** 

**[2018.96s] English:** Became super exciting for computer vision, now. Like in the past, I would say, about a year and a half.  
**Translation:** 

**[2022.96s] English:** It's become really powerful. What's a transformer?  
**Translation:** 

**[2025.44s] English:** Right. I mean, the core part of a transformer is something called the self-attention model.  
**Translation:** 

**[2029.20s] English:** So it came out of Google. And the idea basically is that if you have n elements,  
**Translation:** 

**[2033.92s] English:** What you're creating is a way for all of these N elements to talk to each other.  
**Translation:** 

**[2039.60s] English:** Is that you?  
**Translation:** 

**[2040.00s] English:** Are they paying attention? Each element is paying attention to each of the other elements, and  
**Translation:** 

**[2045.22s] English:** Basically, by doing this, it's really trying to figure out that you're basically getting a much better.  
**Translation:** 

**[2050.62s] English:** View of the data, so for example, if you have a sentence of like four words, the point is if you  
**Translation:** 

**[2055.22s] English:** Get a representation or a feature for this entire sentence; it's constructed in a way such that each  
**Translation:** 

**[2060.70s] English:** Words have paid attention to everything else, now the reason it's like is different from what you  
**Translation:** 

**[2066.38s] English:** Would do in a conf call is basically that in the content, you would only pay attention to a local.  
**Translation:** 

**[2070.84s] English:** Window, so each word would only pay attention to its next neighbor or, like, one neighbor after that.  
**Translation:** 

**[2075.84s] English:** And the same thing goes for images, and images you would basically pay attention to pixels in a three-dimensional space.  
**Translation:** 

**[2080.46s] English:** Cross three or a seven, cross seven neighborhood, and that's it. Whereas with the transformer,  
**Translation:** Vocabulary: pixels: 像素

**[2084.74s] English:** That self-attention mainly involves the idea that each element needs to pay attention to each  
**Translation:** 

**[2089.88s] English:** Other element, and when you say "attention," maybe another way to phrase that is you're considering.  
**Translation:** 

**[2094.90s] English:** A  
**Translation:** 

**[2095.96s] English:** A wide context is important in understanding the sentence.  
**Translation:** 

**[2102.26s] English:** The meaning of a particular word, and in computer vision, that's understanding a larger context to.  
**Translation:** 

**[2107.94s] English:** Understand the local pattern of a particular part of an image, right? So basically, if  
**Translation:** 

**[2114.00s] English:** You have to say "again, a banana" in the image you're looking at. Make sure you've seen the full image first, so whether it's  
**Translation:** 

**[2119.12s] English:** Like, you know, you're looking at all the pixels that make up a kitchen with a dining table and so  
**Translation:** Vocabulary: dining: 餐桌上的

**[2123.40s] English:** On, and then you're basically looking at the banana, also.  
**Translation:** 

**[2125.96s] English:** Yeah, by the way, in terms of if we were to train the funny classifier, there's something funny about  
**Translation:** 

**[2130.20s] English:** The word "banana" just going to anticipate that I'm wearing a banana shirt, so yeah, is there?  
**Translation:** 

**[2136.50s] English:** Bananas on it, okay. So, masking has worked for the vision context as well, and so this transformer.  
**Translation:** Vocabulary: anticipate: 预料; masking: 遮罩

**[2143.30s] English:** The idea has worked as well, so basically, looking at all the elements to understand a particular element.  
**Translation:** 

**[2147.48s] English:** Has been really powerful in vision. The reason is, like a lot of things, when you're looking at them.  
**Translation:** 

**[2152.76s] English:** In isolation, so if you look at just a blob of pixels, so Antonio.  
**Translation:** 

**[2155.96s] English:** Toralba at MIT used to have this really famous image, which I looked at when I was a  
**Translation:** 

**[2160.00s] English:** Ph.D. student, where he would basically have a blob of pixels and would ask you, "Hey, what is this?  
**Translation:** 

**[2164.30s] English:** And it looked basically like a shoe, or like it could look like a TV remote.  
**Translation:** Vocabulary: pixels: 像素

**[2169.34s] English:** Anything, and it turned out it was a beer bottle, but I'm not sure if it was one of these three things.  
**Translation:** 

**[2174.00s] English:** But basically, he showed you the full picture, and then it was very obvious what it was. But the point...  
**Translation:** 

**[2177.96s] English:** Is but, just by looking at that particular local window, you couldn't figure it out, yeah, because of  
**Translation:** 

**[2182.12s] English:** Resolution, because of other things, it's just not easy to figure out by looking at it all the time.  
**Translation:** 

**[2186.76s] English:** The neighborhood of pixels: what these pixels are, yeah, and the same thing happens for language as.  
**Translation:** 

**[2191.08s] English:** Well, for the parameters that have to learn something about the data, you need to give it  
**Translation:** 

**[2196.04s] English:** The capacity to learn the essential things, like if it's not actually able to receive the signal at  
**Translation:** 

**[2201.84s] English:** All then, it's not going to be able to learn that signal. And in order to understand images and to  
**Translation:** 

**[2206.04s] English:** Understand language, you have to be able to see words in their full context. Okay, what is harder?  
**Translation:** 

**[2212.62s] English:** To solve vision or language, visual intelligence or linguistic intelligence.  
**Translation:** Vocabulary: linguistic: 语言相关的

**[2216.76s] English:** So, I'm going to say that computer vision is harder. My reason for this is basically that, language,  
**Translation:** 

**[2223.36s] English:** The course has a big structure to it because we developed it, whereas vision is something that  
**Translation:** 

**[2228.22s] English:** It's common in a lot of animals, and everyone is able to get by with a lot of these animals on Earth are.  
**Translation:** 

**[2232.92s] English:** Actually, they are able to get by without language, and a lot of these animals we also deem to be intelligent.  
**Translation:** 

**[2237.76s] English:** So, clearly, intelligence does have a visual component to it, and yes, of course, in the case of.  
**Translation:** 

**[2243.94s] English:** Humans, of course, also have a linguistic component, but it means that we can't really  
**Translation:** 

**[2246.76s] English:** Get by without language, so it means that there is something far more fundamental about vision.  
**Translation:** 

**[2250.60s] English:** Than there is about language, and I'm sorry to anyone who disagrees, but yes, this is what I feel.  
**Translation:** 

**[2254.92s] English:** So, that's being a little bit reflected in the challenges that have to do with the progress.  
**Translation:** 

**[2261.52s] English:** Of self-supervised learning, would you say, or is that just the peculiar accidents of progress?  
**Translation:** Vocabulary: peculiar: 特殊的

**[2267.04s] English:** Of the AI community that we focused on, we discovered self-attention and transformers in the  
**Translation:** 

**[2272.62s] English:** Context of language, first, so like the self-supervised learning success was actually  
**Translation:** 

**[2276.76s] English:** Uh, for vision, there's not much to do with the Transformers part.  
**Translation:** 

**[2280.00s] English:** I would say it's actually been independent, at least to some degree.  
**Translation:** 

**[2282.52s] English:** I think it's just that the signal is weak.  
**Translation:** 

**[2284.00s] English:** It was a little bit different for vision.  
**Translation:** 

**[2286.82s] English:** Than there was for, like, NLP.  
**Translation:** 

**[2288.16s] English:** And probably NLP folks discovered it before.  
**Translation:** 

**[2291.30s] English:** So, for vision, the main success  
**Translation:** 

**[2292.74s] English:** Has basically been this crop, so far.  
**Translation:** 

**[2294.88s] English:** Like taking different crops of images.  
**Translation:** 

**[2296.88s] English:** Whereas, for NLP, it was this masking thing.  
**Translation:** Vocabulary: masking: 遮蔽

**[2298.98s] English:** But also, the level of success.  
**Translation:** 

**[2300.50s] English:** Is still much higher for language.  
**Translation:** 

**[2302.12s] English:** It has, so that has a lot to do with,  
**Translation:** 

**[2304.82s] English:** I mean, I can get into a lot of details.  
**Translation:** 

**[2306.96s] English:** For this particular question.  
**Translation:** 

**[2308.06s] English:** Let's go for it, okay?  
**Translation:** 

**[2309.06s] English:** So, the first thing is that language is very structured.  
**Translation:** 

**[2312.30s] English:** So, you are going to produce a distribution.  
**Translation:** 

**[2314.10s] English:** Over a finite vocabulary.  
**Translation:** 

**[2315.96s] English:** English has a finite number of words.  
**Translation:** Vocabulary: finite: 有限的

**[2317.72s] English:** It's actually not that large.  
**Translation:** 

**[2319.30s] English:** And you need to produce, basically,  
**Translation:** 

**[2321.68s] English:** When you're doing this masking thing,  
**Translation:** 

**[2322.82s] English:** All you need to do is basically tell me.  
**Translation:** 

**[2324.20s] English:** Which one of these has around 50,000 words?  
**Translation:** 

**[2326.48s] English:** That's it.  
**Translation:** 

**[2327.32s] English:** Now, for vision, let's imagine doing the same thing.  
**Translation:** 

**[2329.58s] English:** Okay, we're basically going to black out  
**Translation:** 

**[2331.52s] English:** A particular part of the image.  
**Translation:** 

**[2332.64s] English:** And we ask the network, or this neural network,  
**Translation:** Vocabulary: neural: 神经网络

**[2334.72s] English:** To predict what is present in this missing patch.  
**Translation:** 

**[2338.12s] English:** It's combinatorially like,...  
**Translation:** Vocabulary: combinatorially: 组合地

**[2339.06s] English:** It's very large, right?  
**Translation:** 

**[2340.00s] English:** You have 256 pixel values.  
**Translation:** Vocabulary: pixel: 像素

**[2342.58s] English:** If you're even producing a basic 7x7 matrix,  
**Translation:** 

**[2344.90s] English:** For a 14x14, like a window of pixels.  
**Translation:** Vocabulary: matrix: 矩阵; pixels: 像素

**[2348.04s] English:** At each of these 169 or each of these 49 locations,  
**Translation:** 

**[2351.38s] English:** You have 256 values to predict.  
**Translation:** 

**[2353.80s] English:** And so it's really, really large.  
**Translation:** 

**[2355.32s] English:** And very quickly, the kind of like prediction problems,...  
**Translation:** 

**[2359.04s] English:** That we are setting up are going to be extremely  
**Translation:** 

**[2360.88s] English:** Like intractable for us.  
**Translation:** Vocabulary: intractable: 难以解决的

**[2362.82s] English:** And so the thing is for NLP:  
**Translation:** 

**[2364.00s] English:** It has been really successful.  
**Translation:** 

**[2365.06s] English:** Because we are very good at predicting.  
**Translation:** 

**[2367.60s] English:** Like doing this,  
**Translation:** 

**[2368.50s] English:** Like distribution over a finite set.  
**Translation:** 

**[2370.90s] English:** And the problem is when this set becomes really large,  
**Translation:** 

**[2373.56s] English:** We are going to become really, really bad.  
**Translation:** 

**[2375.62s] English:** At making these predictions.  
**Translation:** 

**[2377.06s] English:** And at solving, basically, this particular set of problems.  
**Translation:** 

**[2381.10s] English:** So, if you were to do it exactly in this same way,...  
**Translation:** 

**[2384.26s] English:** As NLP for vision, there has been very limited success.  
**Translation:** 

**[2387.10s] English:** The way stuff is working right now.  
**Translation:** 

**[2389.02s] English:** Is actually not by predicting these masks.  
**Translation:** 

**[2391.72s] English:** It's basically done by saying that you take these two  
**Translation:** 

**[2393.72s] English:** Like crops from the image,  
**Translation:** 

**[2395.20s] English:** You get a feature representation from it.  
**Translation:** 

**[2397.12s] English:** And just saying that these two features,  
**Translation:** 

**[2398.50s] English:** So they're like vectors.  
**Translation:** Vocabulary: vectors: 向量

**[2400.00s] English:** Just saying that the distance between these vectors should be small, and so it's a very  
**Translation:** 

**[2404.60s] English:** Different ways of learning, uh, from visual signals than from NLP, okay, the other.  
**Translation:** 

**[2409.64s] English:** The reason is the distributional hypothesis that we talked about for NLP, right? So a word's meaning is determined by the company it keeps.  
**Translation:** 

**[2414.56s] English:** Context basically supplies a lot of meaning to the word now, because there  
**Translation:** Vocabulary: distributional: 分布假设; hypothesis: 假设

**[2419.74s] English:** There are just a finite number of words, and there is a finite number of ways in which we can compose them.  
**Translation:** 

**[2424.62s] English:** They, of course, and the same thing holds for pixels, but in language, there's a lot of structure, right?  
**Translation:** Vocabulary: compose: 构成; finite: 有限的

**[2429.74s] English:** So, I always say, "whatever the dash jumped over the fence," for example, there are lots of these.  
**Translation:** 

**[2434.76s] English:** Sentences that you'll get, and from this, you can actually look at this particular sentence:  
**Translation:** 

**[2439.90s] English:** Occur in a lot of different contexts, as well. This exact same sentence might occur in a different...  
**Translation:** 

**[2443.26s] English:** Context: So, the sheep jumped over the fence. The cat jumped over the fence. The dog jumped over the fence.  
**Translation:** 

**[2447.52s] English:** Fence, so you immediately get a lot of these words, which are because this particular token itself has.  
**Translation:** 

**[2452.84s] English:** So, there's a lot of meaning in these tokens or words, which are actually going to have a  
**Translation:** Vocabulary: token: 令牌

**[2456.86s] English:** Have a sort of related meaning across, given this context.  
**Translation:** 

**[2459.74s] English:** Whereas, for vision, it's much harder because just by the way we capture images,  
**Translation:** 

**[2465.50s] English:** Lighting can be different, um, there might be like different noise in the sensor, so the thing is:  
**Translation:** 

**[2470.22s] English:** You're capturing a physical phenomenon, and then you're basically going through a very complicated process.  
**Translation:** Vocabulary: lighting: 照明; sensor: 传感器

**[2474.54s] English:** Pipeline of image processing, and then you're translating that into some kind of digital format.  
**Translation:** 

**[2479.10s] English:** Signal, whereas with language, you write it down and you transfer it to a digital signal almost.  
**Translation:** Vocabulary: pipeline: 处理流程; translating: 转换

**[2485.26s] English:** Like it's a lossless transfer, and each of these tokens is very well-defined.  
**Translation:** 

**[2489.74s] English:** There could be a little bit of an argument there because language, as written down, is a projection.  
**Translation:** Vocabulary: lossless: 无损; projection: 投影

**[2497.02s] English:** Of course, this is one of the open questions: if you could perfectly solve language, are you getting closer to true AI?  
**Translation:** 

**[2506.82s] English:** Close to being able to solve, you know, easily with flying colors; past the touring test, kind of thing.  
**Translation:** 

**[2512.34s] English:** So, that's it—it's similar, but different than the computer vision problem, which is in the 2D plane.  
**Translation:** 

**[2519.74s] English:** Is a  
**Translation:** 

**[2520.00s] English:** Projection with three-dimensional worlds: so, perhaps there are similar, similar problems there, maybe.  
**Translation:** 

**[2525.84s] English:** This, I mean, I think what I'm saying is that NLP is not easy, of course. Don't get me wrong; like, abstract.  
**Translation:** 

**[2530.72s] English:** Thought expressed in knowledge, or knowledge basically expressed in language, is really hard.  
**Translation:** 

**[2535.40s] English:** To understand, I mean, we've been communicating with language for so long, and it is, of course,  
**Translation:** 

**[2540.34s] English:** A very complicated concept. The thing is, at least we're getting some somewhat reasonable ideas.  
**Translation:** 

**[2547.12s] English:** Like being able to solve some kind of reasonable tasks with language, I would say it's slightly easier.  
**Translation:** 

**[2552.02s] English:** Than it is with computer vision, yeah. I would say, yeah. So that's well put, I would say.  
**Translation:** 

**[2556.96s] English:** Getting impressive performance on language is, I feel, easier than I thought it would be for both.  
**Translation:** 

**[2564.52s] English:** And in computer vision, there's going to be this wall of, like, a hump you have to  
**Translation:** 

**[2571.18s] English:** Overcome to achieve superhuman-level performance or human-level performance.  
**Translation:** 

**[2577.12s] English:** Like, for language, if that wall is farther away, so you can get pretty nice results and you can do a lot of tricks.  
**Translation:** 

**[2583.46s] English:** You can show really impressive performance, and you can even fool people into thinking you're tweeting or  
**Translation:** Vocabulary: tweeting: 发推文

**[2589.76s] English:** You're right; blog post writing or question answering does have intelligence behind it, but to  
**Translation:** 

**[2597.48s] English:** Truly demonstrate understanding of dialogue in a continuous, long-form conversation that would require  
**Translation:** 

**[2606.52s] English:** Perhaps.  
**Translation:** 

**[2607.12s] English:** Big breakthroughs in the same way have been made in computer vision, I think the big breakthroughs need to  
**Translation:** Vocabulary: breakthroughs: 重大进展

**[2612.64s] English:** Happen earlier to achieve an impressive performance? This might be a good place to start.  
**Translation:** 

**[2617.92s] English:** You already mentioned it, but what is contrastive learning and what are energy-based models?  
**Translation:** 

**[2623.32s] English:** Contrastive learning is sort of a paradigm of learning where the idea is that you are learning  
**Translation:** 

**[2629.48s] English:** This embedding space, or so you're learning this sort of vector space of all your concepts and the  
**Translation:** Vocabulary: embedding: 嵌入; paradigm: 范式

**[2634.76s] English:** The way you learn that is basically by contrasting, so the idea is that you are learning this embedding.  
**Translation:** 

**[2637.10s] English:** Space, or so it seems, you are learning this sort of vector space of all your concepts and the way you learn.  
**Translation:** 

**[2637.12s] English:** This idea is that you have a sample, you have another sample.  
**Translation:** 

**[2640.00s] English:** That's related to it, so that's called a positive. And you have another sample that's not related to  
**Translation:** 

**[2644.98s] English:** It's negative. So, for example, let's just take an NLP task or a simple example in computing.  
**Translation:** 

**[2650.66s] English:** Vision. So, you have an image of a cat, and you have an image of a dog. And for whatever application,  
**Translation:** Vocabulary: computing: 计算

**[2655.94s] English:** That you're doing, say you're trying to figure out what pets are; you're saying that these two  
**Translation:** 

**[2659.56s] English:** Images are related. So, the image of a cat and dog are related. But now you have another third image of a  
**Translation:** 

**[2664.18s] English:** Banana, because you don't like that word. So now you basically have this banana.  
**Translation:** 

**[2668.86s] English:** Thank you for speaking to the crowd.  
**Translation:** 

**[2670.70s] English:** And so you take both of these images: the image from the cat, the image from the dog.  
**Translation:** 

**[2675.14s] English:** You get a feature from both of them. And now, what you're training the network to do is basically  
**Translation:** 

**[2678.56s] English:** Pull both of these features together while pushing them away from the feature of a banana.  
**Translation:** 

**[2684.50s] English:** So, this is the contrastive part. So, you're contrasting against the banana.  
**Translation:** 

**[2687.72s] English:** So, there's always this notion of a negative and a positive.  
**Translation:** 

**[2691.34s] English:** Now, energy-based models are like one way that Jan sorts of explains a lot of these methods. So,  
**Translation:** 

**[2698.06s] English:** Jan basically,  
**Translation:** 

**[2698.86s] English:** I think a couple of years—or maybe even more—than that, like when I joined Facebook, Jan used to keep mentioning  
**Translation:** 

**[2703.68s] English:** This is about energy-based models. And, of course, I had no idea what he was talking about. So then,  
**Translation:** 

**[2707.70s] English:** On that day, I caught him in one of the conference rooms. And I asked, "Can you please tell me what this is?  
**Translation:** 

**[2711.20s] English:** So then, like very patiently, he sat down with a marker and a whiteboard. And his idea...  
**Translation:** 

**[2717.06s] English:** Basically, it is that rather than talking about probability distributions, you can talk about  
**Translation:** Vocabulary: distributions: 概率分布; patiently: 耐心地; whiteboard: 白板

**[2720.94s] English:** Energies of models. So, models are trying to minimize certain energies in a specific space.  
**Translation:** 

**[2724.66s] English:** Or they're trying to maximize a certain kind of energy.  
**Translation:** Vocabulary: energies: 能量; maximize: 最大化

**[2727.88s] English:** And the idea basically is that you can explain a lot of the contrast between models like GANs, for example.  
**Translation:** 

**[2733.06s] English:** Which are like generative adversarial networks. A lot of these modern learning methods, or VAEs,  
**Translation:** Vocabulary: adversarial: 对抗的

**[2738.26s] English:** Which are variational autoencoders, you can really explain them very nicely in terms of an energy function.  
**Translation:** 

**[2742.66s] English:** Function that they're trying to minimize or maximize. And so, by putting this common sort of  
**Translation:** Vocabulary: autoencoders: 自动编码器

**[2747.62s] English:** Language for all of these models, what looks very different in machine learning is that VAEs are very  
**Translation:** 

**[2752.74s] English:** Different from what GANs are, they are very, very different from what contrastive models are; you actually  
**Translation:** 

**[2756.52s] English:** Get a sense of.  
**Translation:** 

**[2757.20s] English:** Of, like, oh, these are actually very, very related.  
**Translation:** 

**[2760.00s] English:** It's just that the way or the mechanism in which they're sort of maximizing or minimizing this.  
**Translation:** 

**[2764.80s] English:** The energy function is slightly different; it's revealing the commonalities between all.  
**Translation:** Vocabulary: maximizing: 最大化; minimizing: 最小化

**[2769.20s] English:** These approaches, and putting a sexy word on top of it like "energy," and so similarities between two things.  
**Translation:** 

**[2774.80s] English:** That are similar have low energy, like the low energy signifying similarity, right? Exactly, so.  
**Translation:** Vocabulary: approaches: 方法; signifying: 表示; similarity: 相似性

**[2781.52s] English:** Basically, the idea is that if you were to imagine the embedding as a manifold, a 2D manifold.  
**Translation:** 

**[2786.32s] English:** You would get a hill or, like, a high sort of peak in the energy manifold wherever two things are.  
**Translation:** Vocabulary: embedding: 嵌入; manifold: 流形

**[2791.36s] English:** Not related, and basically, you would have a dip where two things are related, so you'd  
**Translation:** 

**[2795.60s] English:** Get a dip in the manner, and in the self-supervised context, how do you know two things?  
**Translation:** 

**[2801.44s] English:** Are related, and two things are not related, right? So, this is where all the sort of ingenuity or  
**Translation:** 

**[2806.48s] English:** Tricks come in handy, right? For example, like uh, you can take a fill-in-the-blank problem, or you can  
**Translation:** 

**[2812.40s] English:** Take in the context, problem, and what you can say are two words that are in the same context.  
**Translation:** 

**[2816.32s] English:** Are related two words that are in different contexts are not related, for images, basically.  
**Translation:** 

**[2821.12s] English:** Two crops from the same image are related, and whereas a third image is not related at all, or  
**Translation:** 

**[2825.92s] English:** For a video, it can be two frames from that video related because they're likely to contain the same.  
**Translation:** 

**[2830.48s] English:** Sort of, these concepts are present in them, whereas a third frame from a different video is not related at all.  
**Translation:** 

**[2835.68s] English:** Basically, it's a very general term contrasting learning; it has nothing really to do with self.  
**Translation:** 

**[2839.60s] English:** Supervised learning is actually very popular, for example, in any kind of metric learning.  
**Translation:** 

**[2844.64s] English:** Or any kind of embedding learning.  
**Translation:** Vocabulary: metric: 度量; supervised: 监督

**[2846.32s] English:** Learning is also used in supervised learning, and the thing is, because we are not.  
**Translation:** 

**[2850.96s] English:** Really, using labels to get these positive or negative pairs, it can basically also be used.  
**Translation:** Vocabulary: labels: 标记

**[2855.68s] English:** For self-supervised learning, so you mentioned one of the ideas in the vision context to, uh  
**Translation:** 

**[2862.00s] English:** That works is to have different crops, so you could think of that as a way to sort of manipulate the  
**Translation:** Vocabulary: manipulate: 操控

**[2868.56s] English:** Data to generate examples that are similar, obviously, there are a bunch of other techniques.  
**Translation:** 

**[2875.68s] English:** You mentioned  
**Translation:** 

**[2876.32s] English:** For example, you could think of lighting as a very important element in images.  
**Translation:** 

**[2880.00s] English:** Something that varies a lot, and you can artificially change those kinds of things.  
**Translation:** Vocabulary: artificially: 人工地; lighting: 照明

**[2884.52s] English:** There's the whole broad field of data augmentation, which manipulates images in order to increase  
**Translation:** 

**[2891.10s] English:** Arbitrarily, the size of the dataset. First of all, what is data augmentation? And secondly,  
**Translation:** Vocabulary: arbitrarily: 随意; augmentation: 增加; dataset: 数据集; manipulates: 变换

**[2896.50s] English:** What's the role of data augmentation in self-supervised learning and contrastive learning?  
**Translation:** 

**[2902.06s] English:** So, data augmentation is just a way, as you said, it's basically a way to augment the data.  
**Translation:** Vocabulary: augment: 增加

**[2906.52s] English:** So, you have, say, N samples, and what you do is you basically define some kind of transforms for  
**Translation:** 

**[2911.42s] English:** The sample. So, you take your, say, image, and then you define a transform where you can just  
**Translation:** Vocabulary: transforms: 转换

**[2915.54s] English:** Increase, say, the colors, like the colors or the brightness of the image, or increase or  
**Translation:** 

**[2920.04s] English:** Decrease the contrast of the image, for example, or take different crops of it. So, data augmentation,...  
**Translation:** 

**[2925.32s] English:** Is just a process to basically perturb the data or augment the data, right? And so it has played  
**Translation:** 

**[2932.26s] English:** A fundamental role for computer vision, particularly for self-supervised learning.  
**Translation:** Vocabulary: perturb: 扰乱数据

**[2936.52s] English:** The way most current methods work—contrastive or otherwise—is by taking an  
**Translation:** 

**[2941.80s] English:** In the case of images, it is done by taking an image and then computing, basically, two  
**Translation:** Vocabulary: computing: 计算

**[2947.04s] English:** Perturbations of it. So, these can be two different crops of the image with, like, different types of  
**Translation:** 

**[2952.42s] English:** Lighting, or different contrasts, or different colors. So, you jitter the colors a little bit.  
**Translation:** Vocabulary: jitter: 轻微抖动; perturbations: 扰动

**[2956.70s] English:** And so on. And now, the idea is basically because it's the same object, or because it's, like,  
**Translation:** 

**[2962.56s] English:** Related concepts in both of these perturbations, you want the features from.  
**Translation:** 

**[2966.52s] English:** Both of these perturbations are similar. So, now you can use a variety of different ways to  
**Translation:** 

**[2971.62s] English:** Enforce this constraint, like ensuring these features are similar. You can do this by contrastive.  
**Translation:** Vocabulary: constraint: 限制; enforce: 实施

**[2975.64s] English:** Learning. So, basically, both of these things are positives. A third, sort of image, is negative.  
**Translation:** 

**[2980.26s] English:** You can do this basically by, like, clustering. For example, you can say that both of these images are similar because they share certain features.  
**Translation:** Vocabulary: clustering: 聚类; positives: 积极面

**[2986.38s] English:** Should the features from both of these images belong in the same cluster because they're?  
**Translation:** 

**[2990.04s] English:** Related, whereas an image like another image should belong to a different cluster. So there's a  
**Translation:** Vocabulary: cluster: 聚类

**[2994.36s] English:** Variety of different ways to basically enforce.  
**Translation:** 

**[2996.52s] English:** Particular constraint. By the way, when you say "features," it means...  
**Translation:** 

**[3000.00s] English:** There's a very large neural network that extracts patterns from the image, and the kinds of patterns it extracts should be either identical or very similar.  
**Translation:** 

**[3008.02s] English:** Right.  
**Translation:** Vocabulary: extracts: 提取; identical: 完全相同; neural: 神经的

**[3008.36s] English:** That's what that means.  
**Translation:** 

**[3009.22s] English:** So, the neural network basically takes in an image and then outputs a set of numbers, essentially a vector of values.  
**Translation:** Vocabulary: outputs: 输出

**[3016.64s] English:** And that's the feature.  
**Translation:** 

**[3017.46s] English:** And you want this feature for both of these, like different crops that you computed to be similar.  
**Translation:** Vocabulary: computed: 计算得出的

**[3022.12s] English:** So, you want this vector to be identical in its corresponding entries, for example.  
**Translation:** 

**[3025.90s] English:** Be like, literally close in this multidimensional space to each other.  
**Translation:** Vocabulary: corresponding: 相应的; multidimensional: 多维的

**[3030.80s] English:** Right.  
**Translation:** 

**[3031.34s] English:** And, as you said, "close" can mean part of the same cluster or something like that in this large space.  
**Translation:** 

**[3037.44s] English:** First of all, I wonder if there is a connection to the way humans learn to this.  
**Translation:** 

**[3043.68s] English:** Almost, like maybe subconsciously.  
**Translation:** Vocabulary: subconsciously: 潜意识地

**[3047.60s] English:** In order to understand a thing, you kind of have to see it from two, three, or multiple angles.  
**Translation:** 

**[3054.24s] English:** I wonder.  
**Translation:** 

**[3055.16s] English:** I have a lot of friends who are neuroscientists, maybe and cognitive scientists.  
**Translation:** 

**[3060.06s] English:** I wonder if that's in there somewhere.  
**Translation:** Vocabulary: cognitive: 认知; neuroscientists: 神经科学家

**[3063.24s] English:** Like, in order for us to place a concept in its proper place, we have to basically crop it in all kinds of ways.  
**Translation:** 

**[3072.08s] English:** Do basic data augmentation on it in whatever very clever ways that the brain likes to do.  
**Translation:** Vocabulary: augmentation: 扩充

**[3077.70s] English:** Right.  
**Translation:** 

**[3078.62s] English:** Like spinning around in our minds, somehow that is very effective.  
**Translation:** Vocabulary: spinning: 脑海里旋转

**[3082.80s] English:** So, I think for some of them, we'll need to do it.  
**Translation:** 

**[3085.10s] English:** Right.  
**Translation:** 

**[3085.32s] English:** Like babies, for example, they pick up objects, move them around, put them close to their eyes, and so on.  
**Translation:** 

**[3089.76s] English:** Yeah.  
**Translation:** 

**[3090.06s] English:** But for certain other things, actually, we are good at imagining them as well.  
**Translation:** 

**[3093.48s] English:** Right.  
**Translation:** 

**[3093.80s] English:** So, if you, I have never seen, for example, an elephant from the top.  
**Translation:** 

**[3096.92s] English:** I've never really looked at it from a top-down perspective.  
**Translation:** 

**[3099.16s] English:** Yeah.  
**Translation:** 

**[3099.32s] English:** But if you showed me a picture of it, I could very well tell you that it's an elephant.  
**Translation:** 

**[3103.58s] English:** So, I think some of it, we're just like we naturally build it or transfer it from other objects that we've seen to imagine what it's going to look like.  
**Translation:** 

**[3110.92s] English:** Has anyone done that with augmentation?  
**Translation:** 

**[3113.50s] English:** Like, imagine.  
**Translation:** 

**[3115.14s] English:** Imagine all the possible things that are occluded or not there.  
**Translation:** Vocabulary: occluded: 被遮挡的

**[3119.52s] English:** Yeah.  
**Translation:** 

**[3120.00s] English:** Not just like normal things, like wild things, but they're nevertheless physically consistent.  
**Translation:** 

**[3125.56s] English:** So, I mean, people do kind of like occlusion-based augmentation as well, so you place in like a random  
**Translation:** 

**[3133.36s] English:** Like a gray box, to sort of mask out a certain part of the image, and the thing is basically  
**Translation:** 

**[3138.74s] English:** You're kind of occluding it, for example, you place it, say, on half of a person's face, so basically,...  
**Translation:** 

**[3144.10s] English:** Saying that you know something below their nose is occluded, because it's grayed out. So, I meant  
**Translation:** Vocabulary: occluding: 遮挡

**[3149.42s] English:** Like, you have this table, and you can't see behind it, and you imagine there's  
**Translation:** 

**[3155.14s] English:** A bunch of elves with bananas behind the table. I wonder if there's any use in having a wild.  
**Translation:** Vocabulary: elves: 小精灵

**[3162.38s] English:** Imagination for the network, because that's possible—well, maybe not elves, but like puppies.  
**Translation:** 

**[3167.12s] English:** And kittens, or something like that, just have a wild imagination and like to constantly be generating.  
**Translation:** Vocabulary: kittens: 小猫; puppies: 小狗

**[3173.74s] English:** That wild imagination, because in terms of data augmentation, it's currently super.  
**Translation:** 

**[3179.06s] English:** Ultra  
**Translation:** Vocabulary: augmentation: 数据增强; ultra: 超凡的

**[3179.40s] English:** Very boring; it's very basic data augmentation. I wonder if there's any benefit to being  
**Translation:** 

**[3185.64s] English:** Wildlyimaginablewhiletryingtobeuhconsistentwithphysicalreality, Ithinkit'sakindofa  
**Translation:** Vocabulary: wildlyimaginablewhiletryingtobeuhconsistentwithphysicalreality: 天马行空又不失现实

**[3192.76s] English:** Chicken and egg problem, right? Because to have amazing data augmentation, you need to understand  
**Translation:** 

**[3197.02s] English:** What the scene is, and what we're trying to do is data augmentation to learn what a scene is.  
**Translation:** 

**[3201.50s] English:** Anyway, so it's basically just keeps going on before you understand it, just put L's with bananas.  
**Translation:** 

**[3205.88s] English:** Until you know it's not to be true.  
**Translation:** 

**[3209.40s] English:** Just like children have a wild imagination until the adults ruin it all, okay? So, what are the  
**Translation:** 

**[3215.32s] English:** Different kinds of data augmentation that seem to be effective in visual intelligence for  
**Translation:** 

**[3220.96s] English:** Like visual, it's a lot of these image-filtering operations, such as blurring the image, you know.  
**Translation:** 

**[3226.78s] English:** All the kinds of Instagram filters that you can think of, so like arbitrarily, like make the red  
**Translation:** Vocabulary: arbitrarily: 随意; blurring: 模糊

**[3231.58s] English:** Super red makes the green super saturated, like rotating and cropping the image, then rotating and cropping it again.  
**Translation:** 

**[3238.08s] English:** Exactly, all of these kinds of things.  
**Translation:** Vocabulary: cropping: 裁剪; rotating: 旋转

**[3239.40s] English:** Like you said,  
**Translation:** 

**[3240.00s] English:** Lighting is a really interesting one, yes. To me, it feels like something really complicated to do so.  
**Translation:** Vocabulary: lighting: 照明

**[3244.80s] English:** I mean, they don't; the augmentations that we work on aren't that involved. They're not going to  
**Translation:** 

**[3249.38s] English:** It's like physically realistic versions of lighting; it's not that you're assuming that there's a light.  
**Translation:** Vocabulary: augmentations: 增强外设

**[3253.20s] English:** Source up, and then you're moving it to the right. And then, what does the thing look like? It's really  
**Translation:** 

**[3257.34s] English:** More about the brightness of the image, overall brightness of the image, or overall contrast of the image.  
**Translation:** 

**[3261.50s] English:** The image, and so on, but this is a really important point to me. I always thought that data augmentation  
**Translation:** 

**[3268.22s] English:** Holds an important key to big improvements in machine learning, and it seems that it is an  
**Translation:** Vocabulary: augmentation: 增加

**[3275.64s] English:** An important aspect of self-supervised learning, so I wonder if there are significant improvements to be achieved.  
**Translation:** 

**[3282.18s] English:** On much more intelligent kinds of data augmentation, for example, currently, maybe you can correct me if I'm wrong.  
**Translation:** 

**[3289.34s] English:** I'm wrong; data augmentation is not parametrized, yeah. You're not learning, you're not learning to.  
**Translation:** 

**[3295.36s] English:** It seems like data augmentation,  
**Translation:** Vocabulary: parametrized: 参数化

**[3298.22s] English:** Potentially, it should involve more learning than the learning process itself. Right? Um, you're almost like  
**Translation:** 

**[3306.14s] English:** Thinking of something like a generative kind of thing, it's like elves with bananas—you're trying to make it very active.  
**Translation:** Vocabulary: elves: 小精灵; generative: 生成的

**[3312.32s] English:** Imagination of messing with the world, and teaching that mechanism for messing with the world to be...  
**Translation:** 

**[3318.02s] English:** Realistic, right? Um, because that feels like—I mean, it's imagination. It's just, as you said, things.  
**Translation:** Vocabulary: messing: 捣乱

**[3325.96s] English:** It feels like us humans are able to  
**Translation:** 

**[3328.22s] English:** Um, maybe sometimes, subconsciously, we imagine what we're expecting to see before we actually see the thing.  
**Translation:** Vocabulary: subconsciously: 潜意识地

**[3334.54s] English:** See, like maybe there are several options, and especially we probably forgot something, but when we're younger,...  
**Translation:** 

**[3339.70s] English:** Probably, the possibilities were wild; there are more of them, and as we get older, we become less open to them.  
**Translation:** 

**[3345.86s] English:** Understand the world, and the possibilities of what we might see become less and less.  
**Translation:** 

**[3352.02s] English:** Less so, I wonder if you think there are many breakthroughs yet to be had in data augmentation.  
**Translation:** Vocabulary: augmentation: 增加; breakthroughs: 突破

**[3356.88s] English:** And maybe also, can you just comment on that because I think that's a really important point.  
**Translation:** 

**[3358.22s] English:** Comment on the stuff we have is that:  
**Translation:** 

**[3360.00s] English:** At a big part of self-supervised learning.  
**Translation:** 

**[3362.14s] English:** Yes, so data augmentation is like  
**Translation:** 

**[3363.84s] English:** Key to self-supervised learning.  
**Translation:** 

**[3365.54s] English:** That has the kind of augmentation we're using.  
**Translation:** 

**[3368.34s] English:** And basically, the fact that we're trying to learn,...  
**Translation:** 

**[3371.04s] English:** These neural networks that are predicting these features.  
**Translation:** Vocabulary: neural: 神经的

**[3373.94s] English:** From images that are robust under data augmentation.  
**Translation:** 

**[3377.10s] English:** Has been the key for visual self-supervised learning.  
**Translation:** Vocabulary: robust: 健壮的

**[3379.56s] English:** And they play a fairly fundamental role in it.  
**Translation:** 

**[3382.40s] English:** Now, the irony of all of this is that.  
**Translation:** Vocabulary: irony: 讽刺

**[3384.60s] English:** For, like, deep learning purists will say  
**Translation:** 

**[3386.72s] English:** The entire point of deep learning,  
**Translation:** Vocabulary: purists: 执着者

**[3388.38s] English:** Is that you feed in the pixels to the neural network?  
**Translation:** 

**[3391.16s] English:** And it should figure out the patterns on its own.  
**Translation:** Vocabulary: pixels: 像素

**[3393.14s] English:** So, if it really wants to look at edges,  
**Translation:** 

**[3394.46s] English:** It should look at the edges.  
**Translation:** 

**[3395.64s] English:** You shouldn't really go and handcraft  
**Translation:** 

**[3397.44s] English:** These tech features, right?  
**Translation:** Vocabulary: handcraft: 手工制作

**[3398.60s] English:** You shouldn't go tell it, "look at the edges.  
**Translation:** 

**[3401.16s] English:** So, data augmentation should basically  
**Translation:** 

**[3403.10s] English:** Be in the same category, right?  
**Translation:** 

**[3404.42s] English:** Why should we tell the network?  
**Translation:** 

**[3406.06s] English:** Or tell me more about this entire learning paradigm.  
**Translation:** 

**[3408.20s] English:** What kinds of data augmentation are we looking for?  
**Translation:** Vocabulary: paradigm: 范式

**[3410.86s] English:** We are encoding a very human-specific bias there.  
**Translation:** 

**[3415.20s] English:** That we know things are,  
**Translation:** Vocabulary: encoding: 编码

**[3417.26s] English:** Like, if you change,...  
**Translation:** 

**[3418.28s] English:** The contrast of the image,  
**Translation:** 

**[3419.22s] English:** It should still be an apple.  
**Translation:** 

**[3420.26s] English:** Or it should still see an apple, not a banana.  
**Translation:** 

**[3422.24s] English:** And basically, if we change the colors,  
**Translation:** 

**[3425.88s] English:** It should still be the same kind of concept.  
**Translation:** 

**[3428.06s] English:** Of course, this is not just one.  
**Translation:** 

**[3429.90s] English:** This is doesn't feel like super satisfactory.  
**Translation:** Vocabulary: satisfactory: 令人满意的

**[3432.50s] English:** Because a lot of our human knowledge,  
**Translation:** 

**[3434.56s] English:** For our human supervision.  
**Translation:** Vocabulary: supervision: 监督

**[3435.78s] English:** Is actually going into the data augmentation.  
**Translation:** 

**[3437.60s] English:** So, although we are calling it self-supervised learning,  
**Translation:** Vocabulary: augmentation: 增加

**[3439.66s] English:** A lot of the human knowledge is actually being encoded.  
**Translation:** 

**[3441.90s] English:** In the data augmentation process.  
**Translation:** Vocabulary: encoded: 编码

**[3443.52s] English:** So, it's really like we've kind of sneaked away.  
**Translation:** 

**[3445.50s] English:** The supervision at the input.  
**Translation:** Vocabulary: sneaked: 偷偷离开

**[3447.12s] English:** And we are, like, really  
**Translation:** 

**[3447.96s] English:** Designing these nice list of data augmentations.  
**Translation:** Vocabulary: augmentations: 数据增强

**[3450.34s] English:** That are working very well.  
**Translation:** 

**[3451.64s] English:** Of course, the idea is that it's much easier.  
**Translation:** 

**[3453.72s] English:** To design a list of data augmentation techniques is more challenging than it is to do.  
**Translation:** 

**[3456.60s] English:** So, humans are doing, nevertheless,...  
**Translation:** 

**[3458.16s] English:** Doing less and less work.  
**Translation:** 

**[3459.64s] English:** And maybe leveraging their creativity more and more.  
**Translation:** Vocabulary: leveraging: 利用

**[3462.60s] English:** And when we say data augmentation is not parameterized,...  
**Translation:** 

**[3465.08s] English:** It means it's not part of the learning process.  
**Translation:** Vocabulary: parameterized: 参数化的

**[3468.18s] English:** Do you think it's possible to integrate?  
**Translation:** 

**[3470.54s] English:** Some of the data augmentation techniques into the learning process?  
**Translation:** Vocabulary: integrate: 合并使用

**[3473.28s] English:** I think so.  
**Translation:** 

**[3474.12s] English:** I think so.  
**Translation:** 

**[3474.96s] English:** And in fact, it will be really beneficial for us.  
**Translation:** 

**[3477.42s] English:** Because a lot of these data augmentation techniques we use,  
**Translation:** Vocabulary: beneficial: 有益的

**[3480.00s] English:** Vision can be very extreme, for example, like when you have certain concepts—again, a banana—you take the  
**Translation:** 

**[3487.60s] English:** Banana, and then basically you change the color of the banana, right? So you make it a purple banana.  
**Translation:** 

**[3492.24s] English:** Now, this data augmentation process is actually independent of it and has no notion of what.  
**Translation:** 

**[3497.84s] English:** Is present in the image, so it can change this color arbitrarily. It can make it a red banana, as  
**Translation:** Vocabulary: arbitrarily: 随意地

**[3501.60s] English:** Well, and now what we're doing is we're telling the neural network that this red banana, and so on.  
**Translation:** 

**[3507.60s] English:** Of this image, which has the red banana, and a crop of this image where I change the color to purple.  
**Translation:** 

**[3511.36s] English:** Banana should be the feature, and it should be the same now. Bananas aren't red or purple mostly, so really.  
**Translation:** 

**[3517.20s] English:** The data augmentation process should take into account what is present in the image and what are  
**Translation:** 

**[3521.52s] English:** The kinds of physical realities that are possible shouldn't be completely independent of the  
**Translation:** 

**[3525.36s] English:** Image, so you might get big gains if you do subtle augmentation instead of being drastic and unrealistic.  
**Translation:** Vocabulary: augmentation: 增强; drastic: 激进; realities: 现实; subtle: 微妙; unrealistic: 不切实际

**[3532.24s] English:** Augmentation, right? Realistic. I'm not sure if it's subtle, but like realistic for sure.  
**Translation:** 

**[3537.60s] English:** Even subtle augmentation will give you big benefits, exactly. And it will be like for  
**Translation:** 

**[3544.00s] English:** Particular domains you might actually see, like if, for example, now we're doing medical imaging.  
**Translation:** 

**[3548.72s] English:** There are going to be certain kinds of geometric augmentations that are not really  
**Translation:** Vocabulary: augmentations: 增强; geometric: 几何的

**[3552.16s] English:** Going to be very valid for the human body, so if you were to actually loop in data augmentation.  
**Translation:** 

**[3558.16s] English:** Into the learning process, it will actually be much more useful. Now, this actually does take.  
**Translation:** 

**[3562.96s] English:** Us to maybe a semi-supervised kind of setting, because you do want to understand.  
**Translation:** 

**[3567.36s] English:** What is it that you're trying to solve? So, currently, self-supervised learning kind of...  
**Translation:** 

**[3571.12s] English:** Operates in the wild, right? So, you do the self-supervised learning, you're and the purists.  
**Translation:** 

**[3575.84s] English:** And all of us basically say that, okay, this should learn useful representations, and they should be  
**Translation:** Vocabulary: purists: 纯粹主义者; representations: 表示

**[3579.84s] English:** Useful for any kind of end task, no matter if it's like banana recognition or like autonomous driving.  
**Translation:** 

**[3586.08s] English:** Now, it's a tall order. Maybe the first baby step for us should be.  
**Translation:** Vocabulary: autonomous: 自主的

**[3590.08s] English:** That's okay if you're trying to incorporate this data augmentation into the learning process.  
**Translation:** 

**[3593.84s] English:** Then, we at least need to have some sense of what we're trying to do. Are we trying to...  
**Translation:** Vocabulary: incorporate: 合并

**[3597.36s] English:** Distinguish between different types of bananas, or are we trying to?  
**Translation:** 

**[3600.00s] English:** To distinguish between a banana and an apple? Or are we trying to do all of these things at once?  
**Translation:** 

**[3604.38s] English:** And so, some notion of what happens at the end might actually help us do much better at this.  
**Translation:** 

**[3610.30s] English:** Side, let me ask you a ridiculous question. If I were to give you, like, a black box—like, a choice—  
**Translation:** 

**[3616.84s] English:** To have an arbitrary large dataset of real, natural data versus really good data augmentation.  
**Translation:** 

**[3625.28s] English:** Algorithms, which would you like to train in a self-supervised way on? So, natural data from the  
**Translation:** Vocabulary: arbitrary: 随意; augmentation: 增强; dataset: 数据集

**[3632.52s] English:** Internet, arbitrary large, so unlimited data. Or it's like more controlled, good data augmentation.  
**Translation:** 

**[3641.60s] English:** On a finite data set, the thing is, like, because our learning algorithms for vision right now,...  
**Translation:** Vocabulary: finite: 有穷的

**[3646.66s] English:** Really, we can rely on data augmentation, even if you were to give me an infinite source of like  
**Translation:** 

**[3651.86s] English:** Image data; I still need a good data augmentation algorithm.  
**Translation:** Vocabulary: algorithm: 算法; infinite: 无限的

**[3654.50s] English:** You need something.  
**Translation:** 

**[3655.28s] English:** Something that tells you that two things are similar.  
**Translation:** 

**[3657.44s] English:** Right. And so, because you've given me an arbitrarily large data set, I still need to use  
**Translation:** 

**[3662.44s] English:** Data augmentation to take that image, construct like these two perturbations of it, and then learn.  
**Translation:** Vocabulary: arbitrarily: 随意; perturbations: 扰动

**[3667.46s] English:** From it, so the thing is that our learning paradigm is very primitive right now. Even if you were to give  
**Translation:** 

**[3672.98s] English:** Me, lots of images, it's still not really useful. A good data augmentation algorithm is actually  
**Translation:** Vocabulary: paradigm: 范式

**[3676.76s] English:** Going to be more useful. So, you can reduce the amount of data you give me by like:  
**Translation:** 

**[3681.96s] English:** 10 times. But if you were to give me a good data augmentation algorithm, that would be more useful.  
**Translation:** 

**[3685.26s] English:** Probably do better than giving me 10 times the size of that data. But me having to rely on something like a very  
**Translation:** 

**[3691.22s] English:** Primitive data augmentation algorithm.  
**Translation:** 

**[3692.56s] English:** Like through tagging and all those kinds of things, is there a way to discover things that are semantically related?  
**Translation:** 

**[3698.16s] English:** Similar on the Internet? Obviously, there is, but it might be extremely noisy, and the difference might be  
**Translation:** Vocabulary: semantically: 语义上; tagging: 标签化

**[3704.90s] English:** Farther away than you would be comfortable with.  
**Translation:** 

**[3707.76s] English:** So, I mean, yes, tagging will help you a lot. It'll actually go a very long way in figuring out what images are.  
**Translation:** 

**[3712.68s] English:** Related or not, and then so.  
**Translation:** 

**[3715.26s] English:** But then the purists would argue that when you're using human tags, because these tags are:  
**Translation:** Vocabulary: purists: 完美主义者

**[3720.00s] English:** Like, is it really self-supervised learning now because you're using human tags to?  
**Translation:** 

**[3725.36s] English:** Figure out which images are similar to the hashtag #noFilter, as that means a lot of things. Yes, I mean there.  
**Translation:** 

**[3731.52s] English:** Are certain tags which are going to be applicable pretty much to anything, so they're pretty useless.  
**Translation:** 

**[3736.88s] English:** For learning, yeah, but I mean, certain tags are actually like an eye-filter, for example, or the  
**Translation:** 

**[3742.72s] English:** Taj Mahal, for example, these tags are like very indicative of what's going on, and they are, I mean.  
**Translation:** 

**[3747.84s] English:** They are human supervision, yeah. This is one of the tasks of discovering from human-generated.  
**Translation:** Vocabulary: indicative: 表明; supervision: 监督

**[3753.20s] English:** Data strong signals that could be leveraged, much like humans do, for self-supervision.  
**Translation:** 

**[3760.48s] English:** Much work has already been done, like many years ago, when there was something that was called... I guess "human.  
**Translation:** Vocabulary: leveraged: 利用

**[3765.68s] English:** Computation back in the day, humans were doing so much work; it's exciting to discover.  
**Translation:** 

**[3772.40s] English:** Ways to leverage the work they're doing to teach machines without any extra effort from them.  
**Translation:** Vocabulary: computation: 计算; leverage: 利用

**[3777.84s] English:** An example could be, like we said, driving humans driving and machines can learn from the driving.  
**Translation:** 

**[3782.88s] English:** I always hope that there could be some supervision signal discovered in video games, because there's  
**Translation:** 

**[3788.56s] English:** So, with so many people playing video games, it feels like so much effort is put into them.  
**Translation:** 

**[3795.92s] English:** Into playing video games, and you can design video games somewhat.  
**Translation:** 

**[3801.04s] English:** Cheaper, right? To include whatever signals you want—it feels like that could be leveraged somehow, so...  
**Translation:** 

**[3807.84s] English:** People are using that, like there are actually folks right here at UT Austin, like Philip Graham.  
**Translation:** 

**[3811.68s] English:** Bull is a professor at UT Austin. He's been working on video games as a source of  
**Translation:** 

**[3816.88s] English:** Supervision—I mean, it's really fun, like as a PhD student getting to basically play video games.  
**Translation:** 

**[3821.84s] English:** All day, yeah, but so I do hope that kind of thing scales and, like, ultimately boils down to.  
**Translation:** 

**[3826.96s] English:** Discovering some undeniably very good signals—it's like masking in NLP, but that said, there's  
**Translation:** Vocabulary: masking: 遮掩; undeniably: 无疑地

**[3835.60s] English:** Non-contrastive methods, right?  
**Translation:** 

**[3837.84s] English:** Do non-contrastive energy.  
**Translation:** 

**[3840.00s] English:** Based on self-supervised learning methods look like,  
**Translation:** 

**[3843.56s] English:** And why are they promising?  
**Translation:** 

**[3845.68s] English:** So, like I said about contrastive learning,  
**Translation:** 

**[3847.84s] English:** You have this notion of a positive and a negative.  
**Translation:** 

**[3850.76s] English:** Now, the thing is, this entire learning paradigm,...  
**Translation:** 

**[3853.66s] English:** Really, it requires access to a lot of negatives.  
**Translation:** Vocabulary: paradigm: 范式

**[3857.20s] English:** To learn a good sort of feature space.  
**Translation:** 

**[3859.08s] English:** The idea is: if I tell you, okay,  
**Translation:** 

**[3861.70s] English:** So, a cat and a dog are similar,  
**Translation:** 

**[3863.72s] English:** And they're very different from a banana.  
**Translation:** 

**[3865.72s] English:** The thing is, this is a fairly simple analogy, right?  
**Translation:** 

**[3868.04s] English:** Because bananas look visually very different,  
**Translation:** Vocabulary: analogy: 类比; visually: 视觉上

**[3870.90s] English:** From what cats and dogs do.  
**Translation:** 

**[3872.48s] English:** So, very quickly: if this is the only source of supervision,...  
**Translation:** Vocabulary: supervision: 监督

**[3875.06s] English:** That I'm giving you, your learning is not going to be like,  
**Translation:** 

**[3878.14s] English:** After a point, the neural network  
**Translation:** Vocabulary: neural: 神经的

**[3879.80s] English:** Is really not going to learn a lot,  
**Translation:** 

**[3881.70s] English:** Because the negative feedback you're getting,  
**Translation:** 

**[3883.02s] English:** It's going to be so random.  
**Translation:** 

**[3883.94s] English:** So it can be, oh, a cat and a dog are similar,  
**Translation:** 

**[3886.70s] English:** But they're very different from a Volkswagen Beetle.  
**Translation:** 

**[3889.94s] English:** Now, this car looks very different from these animals again.  
**Translation:** Vocabulary: beetle: 甲壳虫; volkswagen: 大众汽车

**[3892.98s] English:** So, the thing is, in contrast to learning,  
**Translation:** 

**[3894.94s] English:** The quality of the negative sample really matters a lot.  
**Translation:** 

**[3898.04s] English:** And so, what has happened is basically,...  
**Translation:** 

**[3900.34s] English:** That typically, these methods that are contrastive really  
**Translation:** 

**[3903.14s] English:** Requires access to lots of negatives, which  
**Translation:** 

**[3905.16s] English:** Becomes harder and harder to sort of scale.  
**Translation:** 

**[3906.98s] English:** When designing an alerting algorithm.  
**Translation:** 

**[3909.04s] English:** So, that's been one of the reasons why.  
**Translation:** Vocabulary: alerting: 预警; algorithm: 算法

**[3911.12s] English:** Non-contrastive methods have become popular.  
**Translation:** 

**[3913.72s] English:** And why people think they're going to be more useful.  
**Translation:** 

**[3916.50s] English:** So, a non-contrastive method, for example,  
**Translation:** 

**[3918.50s] English:** Like clustering is one non-contrastive method.  
**Translation:** Vocabulary: clustering: 聚类

**[3920.92s] English:** The idea, basically, is that you have two of these samples.  
**Translation:** 

**[3924.88s] English:** So, the cat and dog are two crops in this image.  
**Translation:** 

**[3927.70s] English:** They belong to the same cluster.  
**Translation:** 

**[3930.44s] English:** And so essentially, you're basically.  
**Translation:** Vocabulary: cluster: 聚类

**[3932.08s] English:** Doing clustering online when you're learning this network,...  
**Translation:** 

**[3934.84s] English:** And which is very different from having access.  
**Translation:** 

**[3936.70s] English:** To a lot of negatives, explicitly.  
**Translation:** 

**[3938.92s] English:** The other way, which has become really popular,  
**Translation:** Vocabulary: explicitly: 明确地

**[3940.84s] English:** Is something called self-distillation?  
**Translation:** 

**[3943.14s] English:** So, the idea basically is that you have a teacher network.  
**Translation:** 

**[3945.70s] English:** And a student network.  
**Translation:** 

**[3947.52s] English:** And the teacher network produces a feature,  
**Translation:** 

**[3949.54s] English:** So, it takes in the image.  
**Translation:** 

**[3951.10s] English:** And basically, the neural network figures out the patterns.  
**Translation:** 

**[3953.68s] English:** Gets the feature out.  
**Translation:** 

**[3955.06s] English:** And there's another neural network, which  
**Translation:** 

**[3956.90s] English:** Is the student neural network, and that also produces a feature.  
**Translation:** 

**[3960.00s] English:** Now, all you're doing is basically saying that the features produced by the teacher network and the  
**Translation:** Vocabulary: neural: 神经网络

**[3964.00s] English:** The student network should be very similar; that's it. There is no notion of a negative anymore.  
**Translation:** 

**[3969.04s] English:** And that's it; so it's all about similarity maximization between these two features.  
**Translation:** Vocabulary: maximization: 最大化; similarity: 相似性

**[3973.52s] English:** And so, all I need to do now is figure out how to have these two sorts of parallel networks.  
**Translation:** 

**[3978.64s] English:** Student networks and teacher networks, and basically, researchers have figured out very  
**Translation:** Vocabulary: parallel: 并行

**[3983.12s] English:** Cheap methods to do this, so you can actually have, for free, really two types of neural networks.  
**Translation:** 

**[3988.00s] English:** Uh, they're kind of related, but they're different enough that you can actually basically have a  
**Translation:** 

**[3992.72s] English:** Learning problem setup so you can ensure that they always remain different enough.  
**Translation:** 

**[3998.08s] English:** So, the thing doesn't collapse into something boring, exactly. So, the main sort of enemy of  
**Translation:** Vocabulary: collapse: 崩溃; setup: 设置

**[4003.12s] English:** Self-supervised learning: Any kind of similarity maximization technique can be prone to collapse, right?  
**Translation:** 

**[4007.68s] English:** Collapse means that you learn the same feature representation for all demons in the world, which  
**Translation:** 

**[4013.20s] English:** Is completely useless; everything is a banana; everything is a cat.  
**Translation:** 

**[4017.20s] English:** Everything is a car.  
**Translation:** 

**[4018.00s] English:** Yeah.  
**Translation:** 

**[4019.04s] English:** And so, all we need to do is basically come up with ways to prevent collapse in contrastive learning.  
**Translation:** 

**[4024.00s] English:** Is one way of doing it, and then, for example, like clustering, or self-distillation, or other ways of.  
**Translation:** 

**[4028.32s] English:** Doing it, we also had a recent paper where we used de-correlation between two sets.  
**Translation:** Vocabulary: clustering: 聚类

**[4034.80s] English:** Of features to prevent collapse, so that's inspired a little bit by, like, Horace Barlow's neuroscience.  
**Translation:** 

**[4039.36s] English:** Principles.  
**Translation:** Vocabulary: horace: 霍尔塞; neuroscience: 神经科学

**[4040.64s] English:** By the way, I should comment that whoever counts the number of times the word "banana" appears.  
**Translation:** 

**[4047.04s] English:** Cat and dog were used against them by terrorism, or although they were, in fact, in the USA, in the  
**Translation:** 

**[4047.98s] English:** In this conversation, "wins the internet.  
**Translation:** 

**[4050.08s] English:** I wish you luck.  
**Translation:** 

**[4052.26s] English:** What is SWAV, and what is the main improvement proposed?  
**Translation:** 

**[4056.68s] English:** In the paper on supervised learning of visual features.  
**Translation:** Vocabulary: supervised: 监督学习

**[4060.16s] English:** By contrasting cluster assignments?  
**Translation:** 

**[4063.08s] English:** SWAV basically is a clustering-based technique.  
**Translation:** Vocabulary: cluster: 聚类

**[4066.22s] English:** Which is for the same thing, again.  
**Translation:** 

**[4068.02s] English:** For self-supervised learning in vision,  
**Translation:** 

**[4070.74s] English:** Where we have two crops.  
**Translation:** 

**[4072.52s] English:** And the idea basically is that you want the features  
**Translation:** 

**[4075.18s] English:** From these two crops of an image.  
**Translation:** 

**[4076.56s] English:** To lie in the same cluster, and basically,  
**Translation:** 

**[4080.00s] English:** The crops that are coming from different images will be in different clusters.  
**Translation:** 

**[4083.76s] English:** Now, typically, if you were to do this clustering,  
**Translation:** Vocabulary: clusters: 聚类

**[4087.18s] English:** You would perform clustering offline.  
**Translation:** 

**[4089.32s] English:** What that means is, if you have a dataset of n examples,  
**Translation:** Vocabulary: dataset: 数据集

**[4093.10s] English:** You would run over all of these n examples.  
**Translation:** 

**[4095.38s] English:** Get features for them, perform clustering,  
**Translation:** 

**[4097.56s] English:** So, basically, get some clusters.  
**Translation:** 

**[4099.30s] English:** And then, repeat the process again.  
**Translation:** 

**[4101.92s] English:** So, this is offline basically, because I need to do  
**Translation:** 

**[4103.98s] English:** One pass through the data to compute its clusters.  
**Translation:** Vocabulary: compute: 计算

**[4106.88s] English:** Suave is basically just a simple way of doing this online.  
**Translation:** 

**[4109.92s] English:** So, as you're going through the data,  
**Translation:** Vocabulary: suave: 优雅的

**[4111.82s] English:** You're actually computing these clusters online.  
**Translation:** 

**[4114.52s] English:** Of course, there are a lot of tricks involved in how to.  
**Translation:** Vocabulary: computing: 计算

**[4117.72s] English:** Do this in a robust manner without collapsing.  
**Translation:** 

**[4120.04s] English:** But this is the key idea.  
**Translation:** 

**[4122.38s] English:** Is there a nice way to say what is  
**Translation:** 

**[4124.38s] English:** The key methodology of the clustering that enables that?  
**Translation:** Vocabulary: clustering: 聚类; methodology: 方法论

**[4127.36s] English:** Right. So the idea basically is that when you have n samples,  
**Translation:** 

**[4132.54s] English:** We assume that we have access to,  
**Translation:** 

**[4135.04s] English:** There are always K clusters in a dataset.  
**Translation:** 

**[4136.88s] English:** K is a fixed number.  
**Translation:** 

**[4137.90s] English:** So, for example, k is 3,000.  
**Translation:** 

**[4139.90s] English:** So, when you look at any small number of examples,  
**Translation:** 

**[4144.74s] English:** All of them must belong to one of these K clusters.  
**Translation:** 

**[4147.80s] English:** We impose this equi-partition constraint.  
**Translation:** Vocabulary: constraint: 限制; impose: 施加

**[4150.30s] English:** What this means is that, basically,  
**Translation:** 

**[4154.42s] English:** Your entire set of N samples should be  
**Translation:** 

**[4157.24s] English:** Equally partitioned into k clusters.  
**Translation:** 

**[4159.34s] English:** So, all your k clusters have  
**Translation:** Vocabulary: partitioned: 划分

**[4160.64s] English:** Equal contribution to these N samples.  
**Translation:** 

**[4164.20s] English:** This ensures that we never collapse.  
**Translation:** 

**[4166.32s] English:** So, collapse can be viewed as  
**Translation:** 

**[4167.94s] English:** A way in which all samples belong to one cluster.  
**Translation:** Vocabulary: collapse: 聚为一类

**[4170.50s] English:** So, if all features become the same,  
**Translation:** 

**[4173.06s] English:** Then you have basically just one mega-cluster.  
**Translation:** 

**[4175.16s] English:** You don't even have like 10 clusters or 3,000 clusters.  
**Translation:** 

**[4177.82s] English:** So, SWAV basically ensures that at each point,  
**Translation:** Vocabulary: clusters: 聚类; ensures: 确保

**[4181.00s] English:** All these 3,000 clusters are being used in the clustering process.  
**Translation:** 

**[4184.82s] English:** That's it. Basically, just figure out how to do this online, and again,  
**Translation:** 

**[4189.86s] English:** Basically, just make sure that two crops from  
**Translation:** 

**[4191.74s] English:** The same image belongs to the same cluster, and others don't.  
**Translation:** Vocabulary: cluster: 聚类

**[4195.34s] English:** The fact that they have a fixed k makes things simpler.  
**Translation:** 

**[4198.66s] English:** Fixed K makes things simpler.  
**Translation:** 

**[4200.00s] English:** Our clustering is not like really hard clustering; it's soft clustering, so basically you can be  
**Translation:** 

**[4204.78s] English:** Point 2 to cluster number one, and point 8 to cluster number two, so it's not really hard.  
**Translation:** Vocabulary: clustering: 聚类

**[4209.26s] English:** So, essentially, even though we have around 3,000 clusters, we can actually represent a lot of  
**Translation:** 

**[4214.20s] English:** Clusters: What is SEER (S-E-E-R) and what are the key results and insights in the paper on self-supervised learning?  
**Translation:** 

**[4224.08s] English:** Pre-training of visual features in the wild: What is this big, beautiful Seer system? SEER, so I'll  
**Translation:** 

**[4232.00s] English:** First, go to Suave because Suave is actually one of the key components for Seer, so Suave was.  
**Translation:** Vocabulary: suave: 优雅

**[4236.70s] English:** When we used Suave, it was demonstrated on ImageNet, so typically like self-supervised methods.  
**Translation:** 

**[4242.48s] English:** The way we operate is kind of like in the research community, where we "cheat" a bit by using ImageNet.  
**Translation:** 

**[4248.04s] English:** Which, of course, I talked about as having lots of labels, and then we throw away the labels like  
**Translation:** 

**[4253.12s] English:** Throw away all the hard.  
**Translation:** 

**[4254.06s] English:** Work that went behind basically the labeling process, and we pretend that it is self-like.  
**Translation:** 

**[4258.64s] English:** Unsupervised, but the problem here is that we have issues when, like, we collected these images.  
**Translation:** Vocabulary: labeling: 标注; unsupervised: 无监督

**[4264.28s] English:** The ImageNet dataset has a particular distribution of concepts, right? So these images are very curated.  
**Translation:** 

**[4271.46s] English:** And what that means is, these images, of course, belong to a certain set of noun concepts, and also,...  
**Translation:** Vocabulary: curated: 精心挑选的; dataset: 数据集

**[4278.12s] English:** ImageNet has this bias that all images contain an object which is, like, very big and it's typically  
**Translation:** 

**[4283.08s] English:** In the center,  
**Translation:** 

**[4283.66s] English:** Mm-hmm.  
**Translation:** 

**[4284.04s] English:** So, when you're talking about a dog, it's a well-framed dog, it's towards the center of the image.  
**Translation:** 

**[4288.20s] English:** So, a lot of the data augmentation, a lot of the sort of hidden assumptions, and self-supervised methods.  
**Translation:** 

**[4292.12s] English:** Learning, uh, actually really exploits this bias in ImageNet, and so a lot of my work has centered around that.  
**Translation:** Vocabulary: assumptions: 隐含假设; augmentation: 数据扩增; exploits: 利用偏见

**[4299.80s] English:** Of work from other people always uses ImageNet sort of as the benchmark to show the success of.  
**Translation:** 

**[4304.20s] English:** Self-supervised learning: So, you're implying that there are particular limitations to this kind of  
**Translation:** Vocabulary: benchmark: 标准; implying: 暗示

**[4308.04s] English:** Data set: Yes, I mean it's basically because our data augmentation is that we designed, uh, like in the  
**Translation:** 

**[4314.04s] English:** Like all data augmentation that we designed for self-supervised learning and vision, they are kind of  
**Translation:** 

**[4317.96s] English:** Overfed to ImageNet, but yeah.  
**Translation:** 

**[4320.00s] English:** You're saying a little bit hard-coded, like the cropping parameters—the exact cropping parameters, the kind.  
**Translation:** Vocabulary: cropping: 裁剪

**[4325.92s] English:** Of the lighting that we're using, the kind of blurring that we're using, yeah, but you would, uh, for a more  
**Translation:** 

**[4330.64s] English:** In the wild dataset, you would need to be clever or more careful in setting the range of.  
**Translation:** Vocabulary: blurring: 模糊; lighting: 照明

**[4336.96s] English:** Parameters and those kinds of things. So, for SEER, our main goal was twofold: one, basically to move,...  
**Translation:** 

**[4342.48s] English:** Away from ImageNet for training, uh, so the images that we used were like uncurated images now.  
**Translation:** Vocabulary: twofold: 两方面; uncurated: 未整理的

**[4347.76s] English:** There's a lot of debate whether they're actually curated or not, but I'll talk about that later. Uh,...  
**Translation:** 

**[4352.32s] English:** But the idea was basically these are going to be random Internet images, uh, that we are not going  
**Translation:** Vocabulary: curated: 精选的

**[4357.12s] English:** To filter out based on particular categories, so we did not say that, oh, images that belong to  
**Translation:** 

**[4362.32s] English:** Dogs and cats should be the only images that come in this data set, banana and basically other images.  
**Translation:** 

**[4369.28s] English:** Should be thrown out, so we didn't do any of that. These are random Internet images, and of course,  
**Translation:** 

**[4374.32s] English:** It also goes back to the problem of scale that you talked about, so these...  
**Translation:** 

**[4377.76s] English:** Were basically about a billion or so images, and for context, ImageNet, the ImageNet version,  
**Translation:** 

**[4382.16s] English:** That we used was one million images earlier, so this is basically going up by three orders of magnitude.  
**Translation:** 

**[4386.40s] English:** More importantly, the idea was basically to see if we can train a very large convolutional model in a  
**Translation:** 

**[4391.92s] English:** Self-supervised, on this uncurated but really large set of images, and how well would this model?  
**Translation:** Vocabulary: convolutional: 卷积的

**[4397.44s] English:** Does self-supervised learning really overfit to ImageNet, or can it actually work in the wild?  
**Translation:** 

**[4403.76s] English:** And it was also out of curiosity what kinds of things this model will learn; will it  
**Translation:** Vocabulary: overfit: 过度拟合

**[4407.76s] English:** Actually, we would still be able to figure out different types of objects and so on.  
**Translation:** 

**[4412.24s] English:** Be particularly certain kinds of tasks, it would actually do better than an image-trained model, and so for Seer.  
**Translation:** 

**[4418.96s] English:** One of our main findings was that we can actually train very large models in a completely  
**Translation:** 

**[4423.76s] English:** Self-supervised way on lots of Internet images, without really necessarily filtering them out.  
**Translation:** Vocabulary: filtering: 筛选

**[4428.40s] English:** Which was, in itself, a good thing, because it's a fairly simple process, right? So you get images.  
**Translation:** 

**[4432.96s] English:** Which are uploaded, and you basically can immediately use them to train a model in an  
**Translation:** 

**[4437.76s] English:** Environment where you don't really need to sit and filter them out, these images.  
**Translation:** 

**[4440.00s] English:** Images can be cartoons; these can be memes.  
**Translation:** 

**[4442.06s] English:** These can be actual pictures uploaded by people.  
**Translation:** 

**[4444.50s] English:** And you don't really care about what these images are.  
**Translation:** 

**[4446.20s] English:** You don't even care about what concepts they contain.  
**Translation:** 

**[4448.56s] English:** So, this was a very simple setup.  
**Translation:** Vocabulary: setup: 布置

**[4450.32s] English:** What image selection mechanism would you say?  
**Translation:** 

**[4452.92s] English:** Is there anything inherently involved in some aspect of the process?  
**Translation:** 

**[4458.88s] English:** So, you're kind of implying that there's almost none,  
**Translation:** 

**[4461.34s] English:** But what is there, would you say?  
**Translation:** Vocabulary: implying: 暗示

**[4463.66s] English:** If you were to introspect?  
**Translation:** 

**[4465.00s] English:** Right, so it's not like uncured can basically,  
**Translation:** Vocabulary: introspect: 自我反省

**[4468.52s] English:** Like, one way of imagining "uncurated" is basically:  
**Translation:** 

**[4470.86s] English:** You have cameras that can take pictures.  
**Translation:** Vocabulary: uncurated: 未经筛选的

**[4473.80s] English:** At random viewpoints.  
**Translation:** 

**[4475.24s] English:** When people upload pictures to the Internet,  
**Translation:** Vocabulary: viewpoints: 视角

**[4477.44s] English:** They are typically going to care about the framing of it.  
**Translation:** 

**[4480.36s] English:** They're not going to upload, say,  
**Translation:** Vocabulary: framing: 构架

**[4481.90s] English:** The picture is a zoomed-in view of a wall, for example.  
**Translation:** 

**[4483.86s] English:** Well, when we say "Internet,  
**Translation:** 

**[4484.96s] English:** Do you mean social networks?  
**Translation:** 

**[4486.14s] English:** Yes. Okay.  
**Translation:** 

**[4487.20s] English:** So, these are not going to be like pictures.  
**Translation:** 

**[4488.74s] English:** Of, like, a zoomed-in table or a zoomed-in wall.  
**Translation:** 

**[4491.44s] English:** So, it's not really completely uncensored.  
**Translation:** 

**[4493.20s] English:** Because people do have the tendency for photographer's bias,  
**Translation:** Vocabulary: uncensored: 未审查

**[4495.86s] English:** Where they do want to keep things,  
**Translation:** 

**[4497.08s] English:** Towards the center, a little bit,  
**Translation:** 

**[4498.50s] English:** Or, like, really have you know,  
**Translation:** 

**[4500.16s] English:** Nice-looking things, and so on, in the picture.  
**Translation:** 

**[4502.54s] English:** So, that's the kind of bias that typically exists.  
**Translation:** 

**[4505.54s] English:** In this data set and also the user base, right?  
**Translation:** 

**[4507.60s] English:** You're not going to get lots of pictures.  
**Translation:** 

**[4509.22s] English:** From different parts of the world,  
**Translation:** 

**[4510.42s] English:** Because there are certain parts of the world,  
**Translation:** 

**[4512.00s] English:** Where people may not actually be uploading  
**Translation:** Vocabulary: uploading: 上传

**[4514.20s] English:** A lot of pictures to the Internet.  
**Translation:** 

**[4515.32s] English:** Or they may not even have access to a lot of Internet.  
**Translation:** 

**[4517.26s] English:** So, this is a giant dataset and a giant neural network.  
**Translation:** 

**[4521.64s] English:** I don't think we've talked about what architectures.  
**Translation:** Vocabulary: dataset: 数据集; neural: 神经的

**[4524.68s] English:** Works well for SSL, especially for self-supervised data.  
**Translation:** 

**[4528.50s] English:** What is self-supervised learning?  
**Translation:** 

**[4530.16s] English:** For SERE and for SWAB,  
**Translation:** 

**[4531.42s] English:** We were using convolutional networks.  
**Translation:** Vocabulary: convolutional: 卷积的

**[4533.12s] English:** But recently, in a work called Dyno,  
**Translation:** 

**[4534.88s] English:** We've basically started using transformers for vision.  
**Translation:** 

**[4537.46s] English:** Both seem to work really well.  
**Translation:** 

**[4539.26s] English:** ConNets and Transformers,  
**Translation:** 

**[4540.50s] English:** And depending on what you want to do,  
**Translation:** 

**[4541.84s] English:** You might choose to use a particular formulation.  
**Translation:** 

**[4544.26s] English:** So for SERE, it was a ConvNet.  
**Translation:** 

**[4546.00s] English:** It was particularly a RegNet model,  
**Translation:** 

**[4548.16s] English:** Which was also work from Facebook.  
**Translation:** 

**[4550.38s] English:** RegNets are like really good when it comes to compute.  
**Translation:** Vocabulary: compute: 计算

**[4553.26s] English:** Versus, like, accuracy.  
**Translation:** 

**[4555.46s] English:** So, because it was a very efficient model,  
**Translation:** 

**[4557.56s] English:** Compute and memory,  
**Translation:** 

**[4558.26s] English:** It was efficient and  
**Translation:** 

**[4560.00s] English:** Basically, it worked really well in terms of scaling, so we used a very large RegNet model.  
**Translation:** 

**[4564.14s] English:** And trained it on the built-in images. Can you maybe quickly comment on what RegNets are?  
**Translation:** 

**[4568.34s] English:** Uh, it comes from this paper on designing network design spaces—right? It's just super interesting.  
**Translation:** 

**[4574.42s] English:** Concept that emphasizes how to create efficient neural networks, especially large ones, so  
**Translation:** Vocabulary: emphasizes: 强调

**[4579.68s] English:** One of the key takeaways from this paper, which the authors like to emphasize whenever you hear them, is:  
**Translation:** 

**[4583.34s] English:** Present this work, they keep saying that is a lot of neural networks are characterized in terms of  
**Translation:** Vocabulary: emphasize: 强调; takeaways: 要点

**[4588.42s] English:** FLOPs, right? Flops basically refer to floating-point operations, and people really love to use them.  
**Translation:** 

**[4592.58s] English:** Flops to say this model is like really computationally heavy, or like our model is.  
**Translation:** Vocabulary: computationally: 计算上; flops: 浮点运算

**[4597.14s] English:** Computationally cheap, and so on. Now it turns out that FLOPS are really not a good indicator of how  
**Translation:** 

**[4602.38s] English:** Well, a particular network is like how efficient it is, really, and what a better indicator is.  
**Translation:** Vocabulary: indicator: 衡量指标

**[4608.10s] English:** The activation or the memory that is being used by this particular model, and so designing like  
**Translation:** 

**[4613.94s] English:** One of the key findings from this paper was basically that you need to design network families.  
**Translation:** 

**[4618.14s] English:** And you need to design network families, and you need to design network families.  
**Translation:** 

**[4618.42s] English:** Or, neural network architectures that are actually very efficient in the memory space as well.  
**Translation:** Vocabulary: neural: 神经网络

**[4622.92s] English:** Just in terms of pure flops, RegNet is basically a network architecture family that came out of this.  
**Translation:** 

**[4628.20s] English:** Paper that is particularly good at both flops and the sort of memory required for it, and of course,  
**Translation:** 

**[4633.80s] English:** It builds upon earlier work, like ResNet, being the more popular inspiration.  
**Translation:** 

**[4638.44s] English:** For it, where you have residual connections, but one of the things in this work is basically they  
**Translation:** Vocabulary: residual: 剩余的

**[4642.40s] English:** Also, use like squeeze-excitation blocks; so it's a lot of nice, sort of technical innovation in all of that.  
**Translation:** 

**[4647.32s] English:** This, from prior work, and then you can see that the network architecture family is basically a.  
**Translation:** 

**[4648.14s] English:** Prior work and a lot of the ingenuity of these particular authors in how to combine these.  
**Translation:** 

**[4652.42s] English:** Multiple building blocks, but the key constraint was optimized for both FLOPs and memory when you're  
**Translation:** Vocabulary: constraint: 限制; ingenuity: 创造力; optimized: 优化

**[4657.54s] English:** Basically, do this: don't just look at flops, and that allows you to have a sort of very  
**Translation:** 

**[4663.14s] English:** Large networks through this process can optimize for low latency, right? Also, in general.  
**Translation:** Vocabulary: latency: 延迟; optimize: 优化

**[4671.94s] English:** In terms of pure hardware, they fit very well on GPU memory, yeah, so they can be really powerful.  
**Translation:** 

**[4677.22s] English:** Neural network architectures can be like really powerful.  
**Translation:** 

**[4678.14s] English:** With lots of parameters, lots of FLOPs.  
**Translation:** 

**[4680.00s] English:** But also, because they're like efficient in terms of the amount of memory that they're using, you can  
**Translation:** 

**[4684.16s] English:** Actually, you can fit a lot of these models on a single GPU, for example, even very large ones.  
**Translation:** 

**[4689.44s] English:** Would you say that the choice of architecture matters more than the choice of maybe data?  
**Translation:** 

**[4696.80s] English:** Augmentation techniques: Is there a possibility to say what matters more? You kind of imply that.  
**Translation:** 

**[4702.88s] English:** You can probably go really far with just using basic Conv Nets, all right? I think data like data.  
**Translation:** Vocabulary: augmentation: 增强技术

**[4709.60s] English:** And data augmentation; the algorithm being used for the self-supervised training matters a lot.  
**Translation:** 

**[4713.84s] English:** More than just the particular kind of architecture, with different types of architecture, you get different results.  
**Translation:** Vocabulary: algorithm: 算法

**[4718.56s] English:** Like properties in the resulting sort of representation, but really I mean the secret.  
**Translation:** 

**[4723.20s] English:** Sauce is in the data augmentation and the algorithm being used to train them.  
**Translation:** 

**[4726.88s] English:** The architectures, I mean, at this point, a lot of them perform very similarly, depending on like  
**Translation:** 

**[4732.16s] English:** The particular task that you care about, they have certain advantages and disadvantages. Is there?  
**Translation:** 

**[4736.64s] English:** Something interesting can be said about what it takes with data augmentation techniques.  
**Translation:** 

**[4739.60s] English:** Sears is training a giant neural network, which involves a huge amount of data—a huge amount.  
**Translation:** Vocabulary: neural: 神经

**[4744.66s] English:** Neural networks: Is there anything interesting to be said about how to effectively train something like?  
**Translation:** 

**[4749.62s] English:** That's fast; lots of GPOS, okay. So, I mean, so the model was like a billion parameters, yeah, uh, and it was  
**Translation:** 

**[4759.22s] English:** Trained on a billion images, yeah. So, basically, the same number of parameters as the  
**Translation:** 

**[4763.60s] English:** Number of images, and it took a while. I don't remember the exact number; it's in the paper, uh.  
**Translation:** 

**[4768.54s] English:** But it took a while, I guess. I'm trying to get at is: when you're thinking of scaling this kind  
**Translation:** 

**[4778.20s] English:** One of the exciting possibilities of self-supervised learning is several orders of magnitude improvement.  
**Translation:** 

**[4785.28s] English:** Of magnitude scaling of everything, both the neural network and the size of the data.  
**Translation:** 

**[4790.14s] English:** And so, the question is: Do you think there are some interesting tricks for doing large-scale?  
**Translation:** 

**[4796.76s] English:** Distributed computing, or is it?  
**Translation:** 

**[4798.54s] English:** Or is that really outside?  
**Translation:** Vocabulary: computing: 计算

**[4800.00s] English:** Even deep learning, which is more about hardware engineering, I think, is becoming increasingly focused on other aspects as well.  
**Translation:** 

**[4805.84s] English:** This is a lot of systems, though, that are designed basically taking into account the machine.  
**Translation:** 

**[4811.60s] English:** Learning needs rights, so yes, because whenever you're doing this kind of distributed training.  
**Translation:** 

**[4815.36s] English:** There is a lot of intercommunication between nodes, so gradients or the model parameters are  
**Translation:** Vocabulary: gradients: 梯度; intercommunication: 节点间通信

**[4819.60s] English:** Being passed, so you really want to minimize communication costs when you really want to.  
**Translation:** 

**[4823.36s] English:** Scale these models up, uh, you want basically to be able to do as much with a limited amount of  
**Translation:** 

**[4830.24s] English:** Communication as much as possible, so currently, like a dominant paradigm is synchronized, sort of.  
**Translation:** 

**[4834.40s] English:** Training: So, essentially, after every gradient step, all you basically have is  
**Translation:** Vocabulary: dominant: 主流; gradient: 梯度; paradigm: 范式; synchronized: 同步

**[4840.24s] English:** Synchronization step between all the sort of compute chips that you are working with.  
**Translation:** 

**[4845.52s] English:** I think asynchronous training was popular, but it doesn't seem to perform as well.  
**Translation:** Vocabulary: asynchronous: 非同步; compute: 计算; synchronization: 同步

**[4850.24s] English:** But, in general, I think that's sort of the.  
**Translation:** 

**[4853.36s] English:** I guess it's all outside my scope as well, yeah. But well, the main thing is to minimize the  
**Translation:** 

**[4858.64s] English:** Amount of synchronization steps that you have, yeah—that has been the key takeaway, at least in my experience.  
**Translation:** 

**[4863.84s] English:** Experience the others; I have no idea about how to design the chip. Yeah, there are very few things that.  
**Translation:** Vocabulary: takeaway: 主要收获

**[4868.56s] English:** I see, Jim Killer's eyes light up as much as talking about giant computers doing something like that.  
**Translation:** 

**[4875.84s] English:** Fast communication is crucial when you're talking to well, when they're training machine learning systems.  
**Translation:** Vocabulary: crucial: 至关重要

**[4881.12s] English:** What is Vissel? (v-i-s)  
**Translation:** 

**[4883.36s] English:** Sure, here is the improved version: "SL: The PyTorch-based SSL library—what are the use cases that you might have, basically?  
**Translation:** 

**[4890.80s] English:** Was born out of a lot of us at Facebook doing self-supervised learning research, so it's a common  
**Translation:** 

**[4895.92s] English:** Framework in which we have a lot of self-supervised learning methods implemented.  
**Translation:** Vocabulary: implemented: 实现

**[4900.40s] English:** For vision, it's also something that has within itself a benchmark of tasks that you can evaluate.  
**Translation:** 

**[4906.72s] English:** Self-supervised representations: On this, the use case is basically for anyone who's either trying  
**Translation:** Vocabulary: benchmark: 衡量标准; evaluate: 评估; representations: 表示

**[4913.36s] English:** To develop a self-supervised model, or train their self-supervised model, or a researcher who's trying...  
**Translation:** 

**[4917.92s] English:** To build a new self-supervised technique.  
**Translation:** 

**[4920.00s] English:** To be all of these things, uh, so as a researcher, before whistleblowing, for example, or like when we started.  
**Translation:** 

**[4925.18s] English:** Doing this work fairly seriously at Facebook, it was very hard for us to go and implement everything.  
**Translation:** 

**[4930.26s] English:** Self-supervised learning model; test it out in a more consistent manner, the experimental.  
**Translation:** 

**[4935.28s] English:** Setup was very different across different groups, uh, even when someone said that they were reporting.  
**Translation:** Vocabulary: setup: 实验配置

**[4940.34s] English:** ImageNet accuracy could mean lots of different things, so with Whistle, we tried to really sort of  
**Translation:** 

**[4944.66s] English:** Standardize that as much as possible, and there was a paper, like we did in 2019, just about benchmarking.  
**Translation:** Vocabulary: benchmarking: 基准测试; standardize: 标准化

**[4949.34s] English:** And so, Whistle basically builds upon a lot of the work that we did on this kind of thing.  
**Translation:** 

**[4954.06s] English:** Benchmarking, and then every time we try to come up with a self-supervised learning method.  
**Translation:** Vocabulary: whistle: 哨子

**[4958.82s] English:** A lot of us try to push that into the whistle, as well, just so that it basically is like the central.  
**Translation:** 

**[4962.96s] English:** Piece where a lot of these methods can reside; just out of curiosity, people may be, um, so certainly.  
**Translation:** Vocabulary: reside: 存在

**[4969.72s] English:** Outside of Facebook, but just researchers or even people who know how to program in Python.  
**Translation:** 

**[4974.76s] English:** And know how to use PyTorch, uh, what would be the use case? What would be an example?  
**Translation:** 

**[4979.18s] English:** A fundamental use case for people who are using Python and know how to use PyTorch.  
**Translation:** 

**[4979.32s] English:** A fun thing to play around with, like a whistle. Self-supervised.  
**Translation:** 

**[4985.42s] English:** Learning: On that note, would you say there's a good "hello, world" program? Like, is it always about big size?  
**Translation:** 

**[4992.14s] English:** That's important to have, or are there fun, little smaller-scale playgrounds to play around with?  
**Translation:** 

**[4999.88s] English:** We're trying to, like, uh, push something toward that. I think there are a few setups out there.  
**Translation:** 

**[5004.24s] English:** But nothing like a super-standard on the smaller scale. I mean, ImageNet in itself is actually  
**Translation:** Vocabulary: setups: 设置

**[5008.38s] English:** Pretty big, also.  
**Translation:** 

**[5009.16s] English:** So, that is not something which is very feasible for a lot of people, but we are trying to push it anyway.  
**Translation:** Vocabulary: feasible: 可行的

**[5014.66s] English:** Up with smaller, sort of, use cases. The thing is, at a smaller scale, a lot of the observations...  
**Translation:** 

**[5020.14s] English:** Or, for a lot of the algorithms that work, they don't necessarily translate into the medium or the  
**Translation:** 

**[5023.96s] English:** Larger scale, so it's really tricky to come up with a good small-scale setup where a lot of  
**Translation:** 

**[5027.96s] English:** Your empirical observations will really translate to the other setup, so it's been really  
**Translation:** Vocabulary: empirical: 实验性的; setup: 方案; tricky: 棘手的

**[5032.04s] English:** Challenging, uh, I've been trying to do that for a little bit as well because it does take time.  
**Translation:** 

**[5035.74s] English:** To train stuff on Image Net, it does take time to train on more images, but it's really  
**Translation:** 

**[5039.16s] English:** Easy to take out of a space to, like, make those overcast shapes, like, some sort of...  
**Translation:** 

**[5040.00s] English:** But pretty much every time I've tried to do that, it's been unsuccessful because all the observations I draw from my set of experiments on a smaller data set don't translate into ImageNet or don't translate into another sort of data set.  
**Translation:** Vocabulary: experiments: 实验; overcast: 阴天; unsuccessful: 不成功

**[5051.78s] English:** So, it's been hard for us to figure this one out, but it's an important problem.  
**Translation:** 

**[5055.20s] English:** So, there's this really interesting idea of learning across multiple modalities.  
**Translation:** Vocabulary: modalities: 多种感知方式

**[5059.86s] English:** You have a CVPR 2021 best paper candidate titled "Audiovisual Instance Discrimination with Cross-Modal Agreement.  
**Translation:** 

**[5062.98s] English:** It's nice, isn't it?  
**Translation:** Vocabulary: audiovisual: 视听的

**[5065.06s] English:** Áis.  
**Translation:** 

**[5068.60s] English:** Um.  
**Translation:** 

**[5069.02s] English:** He  
**Translation:** 

**[5069.04s] English:** He  
**Translation:** 

**[5069.14s] English:** He  
**Translation:** 

**[5071.18s] English:** What are the key results and insights in this paper, and what can you say, in general, about the promise and power of multimodal learning?  
**Translation:** Vocabulary: multimodal: 多种模态的

**[5077.60s] English:** For this paper, it actually came as a little bit of a shock to me at how well it worked, so I can describe what the problem setup was.  
**Translation:** 

**[5083.86s] English:** So, it's been used in the past by lots of folks, like, for example, Andrew Owens from MIT and Alyosha Efros from Berkeley.  
**Translation:** Vocabulary: alyosha: 艾利奥沙; berkeley: 伯克利

**[5089.86s] English:** And Rosa Sermon from Oxford.  
**Translation:** 

**[5091.14s] English:** So, a lot of these people have been showing results in this.  
**Translation:** Vocabulary: sermon: 布道

**[5094.06s] English:** Of course, I was aware of this result, but I wasn't really sure how well it would work in practice for, like, other sorts of downstream tasks.  
**Translation:** 

**[5100.58s] English:** So the results kept getting better, and I wasn't sure if, like, a lot of our insights from self-supervised learning would translate into this multimodal learning problem.  
**Translation:** Vocabulary: downstream: 后续任务

**[5108.28s] English:** So, multimodal learning is when you have multiple modalities.  
**Translation:** 

**[5115.08s] English:** That's not even close.  
**Translation:** 

**[5116.96s] English:** Okay, so the particular modalities that we work with.  
**Translation:** 

**[5119.86s] English:** In this work, there were audio and video.  
**Translation:** 

**[5122.02s] English:** So, the idea was basically: if you have a video and its corresponding audio track, and you want to use both of these signals (the audio signal and the video signal) to learn a good representation for video and a good representation for audio.  
**Translation:** 

**[5132.62s] English:** Like this podcast!  
**Translation:** 

**[5133.68s] English:** Like this podcast!  
**Translation:** 

**[5134.62s] English:** Exactly.  
**Translation:** 

**[5135.46s] English:** So, what we did in this work was basically to train two different neural networks: one on the video signal, and one on the audio signal.  
**Translation:** 

**[5141.94s] English:** And what we wanted is basically that the features we get from both of these neural networks should be similar.  
**Translation:** Vocabulary: neural: 神经网络

**[5146.38s] English:** Yeah.  
**Translation:** 

**[5146.76s] English:** So, it should basically be able to produce the same kinds of features.  
**Translation:** 

**[5149.86s] English:** From the video, and the same kinds of features from the audio.  
**Translation:** 

**[5152.74s] English:** Now, why is this useful?  
**Translation:** 

**[5153.76s] English:** Well, for a lot of these objects that we have, there is a characteristic sound, right?  
**Translation:** 

**[5157.78s] English:** So, trains, when they go by, make a particular sound.  
**Translation:** Vocabulary: characteristic: 特征的

**[5160.00s] English:** Kind of sounds boats make a particular kind of sound, people when they're jumping around will.  
**Translation:** 

**[5163.98s] English:** Like, shouting "whatever bananas" doesn't make a sound, so you can't learn anything about bananas that way.  
**Translation:** 

**[5169.14s] English:** Or, when humans mention bananas, well, yes, when they say the word "banana," then so you can't trust.  
**Translation:** 

**[5174.30s] English:** Basically, anything that comes out of a human's mouth is a source of audio that is useless.  
**Translation:** 

**[5178.74s] English:** So, the typical use case is basically like, for example, someone playing a musical instrument.  
**Translation:** 

**[5182.30s] English:** So, guitars have a particular kind of sound, and so on. Because a lot of these things are correlated.  
**Translation:** Vocabulary: correlated: 相关的

**[5186.76s] English:** The idea in multimodal learning is to take these two kinds of modalities, video and audio.  
**Translation:** 

**[5190.88s] English:** And learn a common embedding space, a common feature space where both of these related.  
**Translation:** Vocabulary: embedding: 嵌入; modalities: 模态; multimodal: 多模态

**[5195.50s] English:** Modalities can basically be close together, and again, you use contrastive learning for this.  
**Translation:** 

**[5200.26s] English:** So, in contrastive learning, basically the video and the corresponding audio are positives.  
**Translation:** Vocabulary: corresponding: 匹配的; positives: 正样本

**[5205.62s] English:** You can take any other video or any other audio, and that becomes a negative. So, basically, that's  
**Translation:** 

**[5210.86s] English:** It's just a simple application of contrastive learning, and the main sort of finding from this work.  
**Translation:** 

**[5215.30s] English:** For us,  
**Translation:** 

**[5215.66s] English:** Was basically that you can actually learn very, very powerful feature representations very, very  
**Translation:** Vocabulary: representations: 特征表示

**[5221.14s] English:** Powerful video representations, so you can learn the sort of video network that we ended up learning.  
**Translation:** 

**[5226.22s] English:** Can actually be used for downstream, for example, recognizing human actions or recognizing.  
**Translation:** Vocabulary: downstream: 下游应用

**[5231.64s] English:** Different types of sounds, for example. So, this was sort of the key finding: can you give a kind of an  
**Translation:** 

**[5238.78s] English:** Example of a human action, or like, just so we can build up intuition about what kind of thing, right? So  
**Translation:** Vocabulary: intuition: 直觉

**[5244.70s] English:** There is a  
**Translation:** 

**[5245.66s] English:** This dataset, called Kinetics, for example, has over 400 different types of human actions so.  
**Translation:** 

**[5249.40s] English:** People jumping, people, you know, doing different kinds of sports or different types of swimming.  
**Translation:** 

**[5253.96s] English:** So, like different strokes and swimming, uh, golf, and so on; there are just different types.  
**Translation:** Vocabulary: strokes: 游泳姿势

**[5259.14s] English:** Of actions right there, and the point is: this kind of video network that you learn in a self-supervised manner.  
**Translation:** 

**[5263.76s] English:** Way can be used very easily to kind of recognize these different types of actions; uh, it can also  
**Translation:** 

**[5269.36s] English:** Be used for recognizing different types of objects, uh, and what we did is we tried to visualize whether.  
**Translation:** 

**[5274.92s] English:** The network can  
**Translation:** Vocabulary: visualize: 想象

**[5275.58s] English:** Figure out where the sound is coming from, so basically, give it a video.  
**Translation:** 

**[5280.00s] English:** Basically, it's like a person just strumming a guitar, but of course, there is no audio in this.  
**Translation:** Vocabulary: strumming: 弹奏吉他

**[5284.56s] English:** And now, you give it this sound of a guitar, and you ask, "Basically, try to visualize where...  
**Translation:** 

**[5288.88s] English:** The network is where the network thinks the sound is coming from, and it can kind of basically draw.  
**Translation:** 

**[5293.84s] English:** Like, when you visualize it, you can see that it's basically focusing on the guitar. Yeah, that's so.  
**Translation:** 

**[5298.16s] English:** And the same thing, for example, for certain people's voices, like famous celebrities' voices.  
**Translation:** 

**[5302.80s] English:** It can actually figure out where their mouth is, so it can actually distinguish.  
**Translation:** 

**[5307.12s] English:** Different people's voices, for example, a little bit as well, without that ever being annotated.  
**Translation:** Vocabulary: annotated: 标注过的

**[5312.88s] English:** In any way, right? So, this is all that it had discovered. We never... like, we never pointed it out.  
**Translation:** 

**[5317.20s] English:** That this is a guitar and this is the kind of sound it produces; it can actually naturally.  
**Translation:** 

**[5320.80s] English:** Figure that out because it's seen so many correlations between this sound and that.  
**Translation:** 

**[5324.72s] English:** Kind of like an object, that it basically learns to associate this sound with this kind of an object.  
**Translation:** Vocabulary: correlations: 相关性

**[5329.92s] English:** Yeah, that's really fascinating, right? That's really interesting. So, the idea with this kind of  
**Translation:** 

**[5334.72s] English:** The network is then fine-tuned for a particular task.  
**Translation:** 

**[5337.12s] English:** Task right; so, this is forming like a really good knowledge base within a neural network based on.  
**Translation:** 

**[5343.28s] English:** Which you could then train a little bit more to accomplish a specific task, well, exactly so you.  
**Translation:** Vocabulary: neural: 神经元的

**[5349.28s] English:** Don't need a lot of videos of humans doing actions annotated; you can just use a few of them to.  
**Translation:** 

**[5353.92s] English:** Basically, get your recognition: how much insight do you draw from the fact that you can figure it out?  
**Translation:** 

**[5359.52s] English:** Um, where the sound is coming from; I'm trying to see. So that's kind of very... It's very CVAP.  
**Translation:** 

**[5367.12s] English:** Are they beautiful, right? It's a cool little insight. I wonder how profound that is, you know.  
**Translation:** Vocabulary: profound: 深刻的

**[5374.16s] English:** Does it speak to the idea that, somehow, multiple modalities are much bigger than the  
**Translation:** 

**[5382.56s] English:** Sum of their parts, or is it really, really useful to have multiple modalities, or is it just that?  
**Translation:** Vocabulary: modalities: 多种表现形式

**[5388.64s] English:** A cool thing is that there are parts of our world that can be revealed, or effectively explored.  
**Translation:** 

**[5397.12s] English:** Through multiple modalities, but most of it is really  
**Translation:** 

**[5400.00s] English:** All about vision, or about one of the modalities, I would say a little tending more towards the  
**Translation:** 

**[5407.32s] English:** Second part: So, most of it can be sort of figured out with one modality, but having an extra modality helps.  
**Translation:** Vocabulary: modality: 感觉方式; tending: 倾向

**[5411.98s] English:** Always helps you, yeah. So, in this case, for example, like one thing is when you're observing  
**Translation:** 

**[5418.26s] English:** Someone is cutting something, and you don't have any sort of sound there—whether it's an apple or  
**Translation:** 

**[5423.76s] English:** Whether it's an onion, it's very hard to figure that out, but if you hear someone cutting it, it's  
**Translation:** 

**[5428.42s] English:** Very easy to figure it out because apples and onions make a very different kind of, uh, different.  
**Translation:** 

**[5432.62s] English:** Kind of a characteristic sound when they're cut, yeah. So you really figure this out based on audio; it's  
**Translation:** 

**[5437.06s] English:** Much easier, so your life will become much easier when you have access to different kinds of  
**Translation:** Vocabulary: characteristic: 特征

**[5441.32s] English:** Modalities, and the other thing is: so, I like to relate it in this way—it may be like completely.  
**Translation:** 

**[5445.98s] English:** Wrong, but uh, the distributional hypothesis in NLP, right? Where context basically gives kind of  
**Translation:** Vocabulary: distributional: 分布的; hypothesis: 假设

**[5451.54s] English:** Meaning to that word sounds kind of does that, too, right? So if you have the same sound, so that's the  
**Translation:** 

**[5457.66s] English:** Same context.  
**Translation:** 

**[5458.42s] English:** Across different videos, you're very likely to be observing the same kind of concept, yeah, so that's  
**Translation:** 

**[5463.30s] English:** The kind of reason why it figures out the guitar thing, right? It'll observe the same sound across...  
**Translation:** 

**[5468.58s] English:** Multiple different videos, and it figures out maybe this is the common factor that's actually doing it.  
**Translation:** 

**[5473.14s] English:** I wonder. I used to have this argument with my dad a bunch.  
**Translation:** 

**[5477.46s] English:** For creating general intelligence, whether or not smell is an important factor, if that's  
**Translation:** 

**[5483.94s] English:** Important sensory information; mostly, we're talking about like falling in love with an.  
**Translation:** Vocabulary: sensory: 感觉的

**[5487.78s] English:** AI system  
**Translation:** 

**[5488.42s] English:** And for him, smell and touch are important, and I was arguing that they're not at all unimportant.  
**Translation:** 

**[5494.30s] English:** It's nice and everything, but like, you can fall in love with just the language, really, but voice is very...  
**Translation:** 

**[5499.66s] English:** Powerful and vision are next, and smell is not that important. Can I ask you about this process of...  
**Translation:** 

**[5505.96s] English:** Active learning, you mentioned interactivity; is there any value within self-supervised?  
**Translation:** 

**[5515.58s] English:** Learning context to select:  
**Translation:** 

**[5518.42s] English:** Parts of the data.  
**Translation:** 

**[5520.00s] English:** In intelligent ways, such that they would most benefit the learning process, right? So, I think so.  
**Translation:** 

**[5527.42s] English:** I think, I mean, I know I'm talking to an active learning fan here, so of course I know the answer.  
**Translation:** 

**[5531.98s] English:** First, you're talking about bananas, and now you're talking about active learning—I love it!  
**Translation:** 

**[5536.08s] English:** I think Gianna Coon told me that active learning is not that interesting.  
**Translation:** 

**[5539.58s] English:** I and I think, at that time, I didn't want to argue with him too much, but when we talked again.  
**Translation:** 

**[5545.54s] English:** That's we're going to spend three hours arguing about active learning. My sense was you can go.  
**Translation:** 

**[5549.78s] English:** Extremely far with active learning, you know, perhaps farther than anything else, like the  
**Translation:** 

**[5555.28s] English:** To me, there's this kind of intuition that similar to data augmentation, you can get a lot.  
**Translation:** 

**[5562.28s] English:** From the data, from intelligent optimization of its usage, I'm trying to speak generally.  
**Translation:** Vocabulary: augmentation: 增加; intuition: 直觉; optimization: 优化

**[5572.46s] English:** In such a way that includes data augmentation and active learning, there's something about  
**Translation:** 

**[5578.32s] English:** Maybe interactive exploration.  
**Translation:** Vocabulary: interactive: 交互式

**[5579.76s] English:** Of the data that, um, at least this part of the solution to intelligence is like an important part.  
**Translation:** 

**[5586.42s] English:** I don't know what your thoughts are on active learning in general, but I actually really like it.  
**Translation:** 

**[5590.60s] English:** Learning: So, back in the day, we did this largely ignored CVPR paper called "Learning by Asking.  
**Translation:** 

**[5595.52s] English:** Questions, so the idea was basically that you would train an agent to ask a question about  
**Translation:** 

**[5599.38s] English:** The image, it would get an answer, and basically then it would update itself; it would see the  
**Translation:** 

**[5603.92s] English:** Next, it would decide what's the next hardest question that I can ask to learn the most.  
**Translation:** 

**[5608.14s] English:** And the idea was basically to train an agent that would ask a question about the image and  
**Translation:** 

**[5609.76s] English:** Basically, because it was being smart about the kinds of questions it was asking, it would learn.  
**Translation:** 

**[5614.10s] English:** In fewer samples, it would be more efficient at using data, and we did find to some extent that.  
**Translation:** 

**[5619.52s] English:** It was actually better than randomly asking questions. Kind of a weird thing about active.  
**Translation:** 

**[5623.16s] English:** Learning is also a chicken-and-egg problem, because when you look at an image to ask a good  
**Translation:** 

**[5627.80s] English:** Question about the image; you need to understand something about the image, right? You can't ask a  
**Translation:** 

**[5631.48s] English:** Completely, arbitrarily, and random, this question might not even apply to that particular image, so there is  
**Translation:** 

**[5635.92s] English:** Some amount of understanding or knowledge that basically keeps getting built when you're doing  
**Translation:** Vocabulary: arbitrarily: 随意地

**[5639.76s] English:** That  
**Translation:** 

**[5640.00s] English:** So, I think active learning by itself is really good.  
**Translation:** 

**[5644.78s] English:** And the main thing we need to figure out is basically how we come up with a technique.  
**Translation:** 

**[5649.64s] English:** To first model what the model knows, and also model what the model does not know.  
**Translation:** 

**[5656.02s] English:** I think that's the sort of beauty of it, right?  
**Translation:** 

**[5658.68s] English:** Because, when you know that there are certain things you don't know anything about,  
**Translation:** 

**[5662.34s] English:** Asking a question about those concepts is actually going to bring you the most value.  
**Translation:** 

**[5666.56s] English:** I think that's the sort of key challenge.  
**Translation:** 

**[5668.46s] English:** Now, self-supervised learning by itself—like selecting data for it and so on—is actually  
**Translation:** 

**[5671.84s] English:** Really useful.  
**Translation:** Vocabulary: selecting: 挑选数据

**[5672.84s] English:** But I think that's a very narrow view of looking at active learning, right?  
**Translation:** 

**[5675.14s] English:** If you look at it more broadly, it is basically about whether the model has knowledge about N.  
**Translation:** Vocabulary: broadly: 宽泛地

**[5680.40s] English:** Concepts, and it is weak basically about certain things.  
**Translation:** 

**[5683.96s] English:** So, it needs to ask questions either to discover new concepts or to basically increase its knowledge.  
**Translation:** 

**[5688.88s] English:** Knowledge about these N concepts.  
**Translation:** 

**[5690.22s] English:** So, at that level, it's a very powerful technique.  
**Translation:** 

**[5693.18s] English:** I actually do think it's going to be really useful.  
**Translation:** 

**[5696.78s] English:** Even in simple things, such as data.  
**Translation:** 

**[5698.44s] English:** Data labeling is super useful.  
**Translation:** 

**[5700.40s] English:** So, here is one simple way that you can use active learning.  
**Translation:** Vocabulary: labeling: 标注

**[5704.38s] English:** For example, you have your self-supervised model, which is very good at predicting similarities.  
**Translation:** 

**[5708.72s] English:** And the dissimilarities between things.  
**Translation:** 

**[5710.92s] English:** And so, if you label a picture as basically a banana, now you know that all the images  
**Translation:** 

**[5717.68s] English:** That are very similar to this image are also likely to contain bananas.  
**Translation:** 

**[5721.64s] English:** So, probably, when you want to understand what else a banana is, you're not going to use  
**Translation:** 

**[5725.92s] English:** These other images.  
**Translation:** 

**[5726.92s] English:** You're actually going to use an image.  
**Translation:** 

**[5727.82s] English:** You're actually going to use an image that is not completely dissimilar, but somewhere...  
**Translation:** 

**[5731.84s] English:** In between, which is not super similar to this image, but not super dissimilar either.  
**Translation:** 

**[5735.78s] English:** And that's going to tell you a lot more about what this concept of a banana is.  
**Translation:** 

**[5739.64s] English:** So, that's kind of a heuristic.  
**Translation:** 

**[5741.88s] English:** I wonder if it's possible to also learn ways to discover the most likely and most beneficial options.  
**Translation:** Vocabulary: beneficial: 有益的; heuristic: 启发式的方法

**[5752.34s] English:** Image.  
**Translation:** 

**[5753.64s] English:** So, not just looking at something that's somewhat similar to a banana.  
**Translation:** 

**[5756.66s] English:** Yeah.  
**Translation:** 

**[5757.82s] English:** It's not just looking at a thing that's somewhat similar to a banana, but not exactly like one.  
**Translation:** 

**[5760.00s] English:** But have some kind of more complicated learning system.  
**Translation:** 

**[5763.58s] English:** Like, learned discovery mechanism.  
**Translation:** 

**[5767.10s] English:** That tells you what image to look for.  
**Translation:** 

**[5769.46s] English:** Like how, yeah, like actually in a self-supervised way,  
**Translation:** 

**[5774.38s] English:** Learning strictly a function that says,  
**Translation:** 

**[5777.32s] English:** Is this image going to be very useful to me?  
**Translation:** Vocabulary: strictly: 严格地

**[5780.60s] English:** Given what I currently know?  
**Translation:** 

**[5782.16s] English:** I think there is a lot of synergy there.  
**Translation:** Vocabulary: synergy: 协同效应

**[5784.04s] English:** It's just that, I think, yeah, it's going to be explored.  
**Translation:** 

**[5787.70s] English:** I think that's very much related to that,  
**Translation:** 

**[5789.42s] English:** I kind of think of what Tesla Autopilot is doing.  
**Translation:** 

**[5793.64s] English:** Currently, as a form of active learning.  
**Translation:** 

**[5796.90s] English:** There's something that Andrej Kapati and his team  
**Translation:** 

**[5799.28s] English:** Are you calling a data engine?  
**Translation:** 

**[5801.30s] English:** Yes.  
**Translation:** 

**[5802.14s] English:** So, you're basically deploying a bunch of instantiations.  
**Translation:** Vocabulary: deploying: 部署; instantiations: 实例化

**[5805.68s] English:** Of a neural network into the wild,  
**Translation:** 

**[5807.82s] English:** And they're collecting a bunch of edge cases.  
**Translation:** 

**[5810.70s] English:** That are then sent back for annotation for particular,  
**Translation:** 

**[5814.00s] English:** And edge cases, as defined, are near failure.  
**Translation:** Vocabulary: annotation: 注释

**[5816.74s] English:** Or, some weirdness.  
**Translation:** 

**[5818.80s] English:** On a particular task that's then sent back.  
**Translation:** Vocabulary: weirdness: 怪异情况

**[5821.42s] English:** It's that, not exactly a banana,  
**Translation:** 

**[5824.02s] English:** But almost all banana cases were sent back for annotation.  
**Translation:** 

**[5827.26s] English:** And then there's a loop that keeps going.  
**Translation:** 

**[5829.22s] English:** And you keep retraining and retraining.  
**Translation:** 

**[5831.62s] English:** And the active learning step there:  
**Translation:** 

**[5833.30s] English:** Or, however, you want to call it,  
**Translation:** 

**[5834.82s] English:** The cars themselves are sending you back the data.  
**Translation:** 

**[5839.12s] English:** What in the world happened here?  
**Translation:** 

**[5840.78s] English:** This was weird.  
**Translation:** 

**[5842.84s] English:** What are your thoughts about that sort of deployment?  
**Translation:** Vocabulary: deployment: 部署

**[5846.46s] English:** Of neural networks in the wild?  
**Translation:** 

**[5848.80s] English:** I think it's great to ask a question.  
**Translation:** Vocabulary: neural: 神经的

**[5850.80s] English:** First is your thoughts, and maybe, if you want to comment,  
**Translation:** 

**[5853.86s] English:** Is there any application for autonomous driving?  
**Translation:** Vocabulary: autonomous: 自主

**[5856.98s] English:** Like computer vision-based autonomous driving,  
**Translation:** 

**[5860.18s] English:** Applications of Self-Supervised Learning  
**Translation:** 

**[5862.08s] English:** In the context of computer vision-based autonomous driving?  
**Translation:** 

**[5867.56s] English:** So, I think so.  
**Translation:** 

**[5868.40s] English:** I think, for self-supervised learning to be used,  
**Translation:** 

**[5870.08s] English:** In autonomous driving, there are lots of opportunities.  
**Translation:** 

**[5871.82s] English:** I mean, just like pure consistency in predictions.  
**Translation:** 

**[5874.90s] English:** Is one way, right?  
**Translation:** 

**[5875.86s] English:** So, because you have this nice,  
**Translation:** 

**[5878.46s] English:** Nice sequence of,  
**Translation:** 

**[5880.00s] English:** Data that is coming in from a video stream, of course, associated with the actions that say,...  
**Translation:** 

**[5884.40s] English:** The car takes you can form a very nice predictive model of what's happening, so for example, like all  
**Translation:** Vocabulary: predictive: 预测性的

**[5889.82s] English:** The way, uh, like one possible way in which they're figuring out what data to get labeled.  
**Translation:** 

**[5895.34s] English:** Is basically through prediction uncertainty, right? So you predict that the car was going to turn.  
**Translation:** Vocabulary: labeled: 标注过的

**[5899.92s] English:** Right, so this was the action that was going to happen in shadow mode, and now the driver,...  
**Translation:** 

**[5903.88s] English:** Turned left, and this was a really big surprise. So, basically, by forming these good  
**Translation:** 

**[5908.94s] English:** Predictive models—you are, I mean, these are kind of self-supervised models, right? Prediction models.  
**Translation:** 

**[5913.42s] English:** Are basically being trained just by looking at what's going to happen next and asking them to.  
**Translation:** 

**[5917.42s] English:** Predict what's going to happen next, so I would say this is really one use of self-supervised.  
**Translation:** 

**[5921.42s] English:** Learning it's a predictive model, and you're learning a predictive model basically just by  
**Translation:** 

**[5925.30s] English:** Looking at what data you have, is there something about that active learning context that you noticed?  
**Translation:** 

**[5930.70s] English:** You can find insights from, like, that kind of deployment of the system, seeing cases where  
**Translation:** 

**[5935.98s] English:** It doesn't perform as you expected.  
**Translation:** 

**[5938.94s] English:** And then retraining the system based on that—I think that really resonates with me.  
**Translation:** 

**[5942.90s] English:** Uh, it's super smart to do it that way because, I mean, the thing is with any kind of practical  
**Translation:** 

**[5949.04s] English:** System, like autonomous driving, there are those edge cases that are actually  
**Translation:** Vocabulary: autonomous: 自主的

**[5953.42s] English:** The problem, right? I mean, highway driving or like freeway driving has basically been  
**Translation:** 

**[5958.32s] English:** Like there has been a lot of success in that particular part of autonomous driving for a long time.  
**Translation:** Vocabulary: freeway: 高速公路

**[5962.26s] English:** Time, I would say, like since the '80s or something. Now, the point is, all these failure cases are the  
**Translation:** 

**[5968.94s] English:** Sort of, one reason why autonomous driving hasn't come to be as super super mainstream is that...  
**Translation:** 

**[5973.26s] English:** Available, like in every possible car right now, and so basically by really scaling this problem.  
**Translation:** 

**[5977.90s] English:** Out by really trying to get all of these edge cases out as quickly as possible, and then just...  
**Translation:** 

**[5982.30s] English:** Like using those to improve your model—that's super smart—and prediction uncertainty, too.  
**Translation:** 

**[5986.62s] English:** That's one really nice way of doing it, but let me put you on the spot.  
**Translation:** 

**[5991.98s] English:** So, uh, we mentioned offline Gitandra. He thinks that the Tesla computer vision approach, or really  
**Translation:** 

**[5998.94s] English:** Is a really good approach for autonomous driving.  
**Translation:** 

**[6000.00s] English:** Driving is very far away. How many years away? If you have to bet all your money on it, are we?  
**Translation:** 

**[6007.36s] English:** To solving autonomous driving, this kind of computer vision-only machine learning-based approach is needed.  
**Translation:** 

**[6012.84s] English:** Approach, okay. So, what does solving autonomous driving mean? Does it mean solving it in the  
**Translation:** 

**[6016.84s] English:** U.S., does it mean solving it in India? Because I can tell you that very different types of driving.  
**Translation:** 

**[6020.56s] English:** Happening, not in India or Russia, but in the United States: autonomous. So, what does solving mean here?  
**Translation:** 

**[6028.46s] English:** Uh, when the car says it has control, it is fully liable. You can go to sleep.  
**Translation:** 

**[6035.48s] English:** Is driving by itself, so this is highway and city driving, but not everywhere—mostly everywhere.  
**Translation:** 

**[6041.66s] English:** And it's let's say significantly better, like five times fewer accidents than humans.  
**Translation:** 

**[6050.00s] English:** Sufficiently safer, such that the public feels that the transition is, you know, enticing.  
**Translation:** 

**[6057.38s] English:** Beneficial both for  
**Translation:** Vocabulary: beneficial: 有益的; enticing: 诱人的; sufficiently: 足够地

**[6058.44s] English:** Safety and financial matters, and all those kinds of things. Okay, so first disclaimer: I'm not an expert in this area.  
**Translation:** 

**[6063.12s] English:** Autonomous driving: so, let me put it out there. I would say, at least five to ten years.  
**Translation:** 

**[6068.16s] English:** This is my guess from then on, yeah. I'm actually very impressed when I sat  
**Translation:** 

**[6075.52s] English:** In a friend's Tesla recently, and of course, like, uh, looking at it, it basically  
**Translation:** 

**[6081.04s] English:** Shows all the detections and everything the car is doing as you're driving by, and that's super.  
**Translation:** 

**[6085.32s] English:** Distracting for me as a person, because all I keep looking at,...  
**Translation:** Vocabulary: detections: 检测; distracting: 分散注意力的

**[6088.44s] English:** It is like the bounding boxes and the cars it's tracking, and it's really impressive, especially.  
**Translation:** 

**[6092.34s] English:** When it's raining, and it's able to do that—that was the most impressive part for me. It's actually  
**Translation:** Vocabulary: bounding: 界限

**[6096.66s] English:** Able to get through rain and do that, and one of the reasons why, like a lot of us believed, and I  
**Translation:** 

**[6102.66s] English:** Would put myself in that category is LiDAR-based, uh, technology for autonomous driving.  
**Translation:** Vocabulary: autonomous: 自主

**[6107.76s] English:** Was the key driver right? So, Waymo was using it for the longest time, and Tesla then decided to go.  
**Translation:** 

**[6112.26s] English:** This completely other route, that oh, we're not going to even use LiDAR; so their initial system,...  
**Translation:** 

**[6118.44s] English:** Was based, and now they're actually moving to a  
**Translation:** 

**[6120.00s] English:** Completely, like, a vision-based system, and so that was just like it sounded — completely crazy, like.  
**Translation:** 

**[6125.04s] English:** LIDAR is very useful in cases where you have low visibility, of course, it comes with its own set...  
**Translation:** 

**[6130.62s] English:** Of course, but now to see that happen in a live Tesla just proves  
**Translation:** Vocabulary: visibility: 能见度

**[6136.44s] English:** Everyone, wrong, I would say, in a way, and that's just working really well. I think there were also.  
**Translation:** 

**[6141.66s] English:** Like a lot of advancements in camera technology, now there were things I knew about when I was at CMU.  
**Translation:** Vocabulary: advancements: 进步

**[6146.46s] English:** Was a particular kind of camera that had been developed, which was really good at basically low-light conditions.  
**Translation:** 

**[6152.10s] English:** Visibility settings: So, like lots of snow and lots of rain, it could actually still have a very  
**Translation:** 

**[6156.12s] English:** Reasonable visibility, and I think there are lots of these kinds of innovations that will happen.  
**Translation:** 

**[6160.14s] English:** The sensor side itself, which is actually going to make this very easy in the future, and so maybe.  
**Translation:** Vocabulary: innovations: 创新; sensor: 传感器

**[6164.52s] English:** That's actually why I'm more optimistic about vision-based autonomous driving.  
**Translation:** 

**[6169.14s] English:** Just want to call it self-supervised driving, but vision-based autonomous driving is the reason.  
**Translation:** Vocabulary: optimistic: 乐观

**[6174.12s] English:** I'm quite optimistic about it because I think there are going to be  
**Translation:** 

**[6176.44s] English:** Lots of advances on the sensor side itself, so acquiring this data, we're actually going to  
**Translation:** Vocabulary: advances: 进步

**[6181.42s] English:** Get much better about it, and then, of course, when we're able to scale out and get all of these...  
**Translation:** 

**[6185.98s] English:** Edge cases, as Andre described, I think that's going to make us go very far away, yeah.  
**Translation:** Vocabulary: andre: 安德烈

**[6192.04s] English:** So, I'm very much with you on the five to ten years—maybe 10 years—but you made it.  
**Translation:** 

**[6199.96s] English:** I'm not sure how you made it sound, but for some people, that seems like it might be really far.  
**Translation:** 

**[6204.88s] English:** Away, and then for other people.  
**Translation:** 

**[6206.44s] English:** Uh, it might seem like very close, but there are a lot of fundamental questions about how much game theory.  
**Translation:** 

**[6214.90s] English:** Is this really just a simple collision avoidance problem, and how much more to it is there?  
**Translation:** 

**[6222.82s] English:** Of it is, uh, you're still interacting with other humans in the scene, and you're trying to create.  
**Translation:** Vocabulary: collision: 碰撞; interacting: 互动

**[6228.10s] English:** An experience that's compelling, so you want to get from point A to point B quickly, you want to:  
**Translation:** 

**[6233.62s] English:** Navigate the scene in a safe way, but you also want to show  
**Translation:** Vocabulary: compelling: 引人入胜; navigate: 导航

**[6236.44s] English:** Some level of aggression, because, uh,...  
**Translation:** 

**[6240.00s] English:** Well, certainly, this is why you're screwed in India.  
**Translation:** Vocabulary: aggression: 攻击性

**[6241.88s] English:** Because you have to show aggression.  
**Translation:** 

**[6243.20s] English:** Or Jersey, or New Jersey.  
**Translation:** 

**[6246.68s] English:** So, like, New York, or basically any major city.  
**Translation:** 

**[6251.24s] English:** But I think it's probably Elon that I talked about the most.  
**Translation:** 

**[6254.86s] English:** Which is surprising given the level at which they are not considering human beings.  
**Translation:** 

**[6259.58s] English:** As a huge problem in this, it serves as a source of problems.  
**Translation:** 

**[6262.92s] English:** Like, driving is fundamentally a robot-to-robot interaction.  
**Translation:** 

**[6268.50s] English:** Versus the environmental problem.  
**Translation:** Vocabulary: fundamentally: 本质上

**[6270.98s] English:** Versus, like, you know, you can just consider humans not part of the problem.  
**Translation:** 

**[6275.06s] English:** I used to think that humans are almost certainly something that has to be modeled really well.  
**Translation:** Vocabulary: modeled: 建模

**[6281.26s] English:** Pedestrians, cyclists, and humans inside other cars,  
**Translation:** 

**[6284.38s] English:** You have to have, like, mental models for them.  
**Translation:** Vocabulary: cyclists: 骑自行车的人; pedestrians: 行人

**[6286.30s] English:** You cannot just see it as objects.  
**Translation:** 

**[6288.20s] English:** But more and more, it's like the same kind of intuition.  
**Translation:** 

**[6292.92s] English:** Breaking down what self-supervised learning does,  
**Translation:** 

**[6296.10s] English:** Which is, well, maybe through learning,  
**Translation:** 

**[6298.66s] English:** You'll get all the human, like, human information you need, right?  
**Translation:** 

**[6304.46s] English:** Like, maybe you'll get it just with enough data.  
**Translation:** 

**[6307.46s] English:** You don't need to have explicitly good models of human behavior.  
**Translation:** 

**[6310.84s] English:** Maybe you get it through the data.  
**Translation:** Vocabulary: explicitly: 明确地

**[6312.34s] English:** So, I mean, my skepticism also stems from knowing a lot of automotive companies.  
**Translation:** 

**[6315.80s] English:** And how difficult it is to be innovative.  
**Translation:** Vocabulary: automotive: 汽车相关的; innovative: 创新的; skepticism: 怀疑主义

**[6318.32s] English:** I was skeptical that they would be able to do it at scale.  
**Translation:** 

**[6322.06s] English:** To control.  
**Translation:** Vocabulary: skeptical: 怀疑的

**[6322.92s] English:** Convert the driving scene across the world into a digital form.  
**Translation:** 

**[6328.78s] English:** Such that you can create this data engine at scale.  
**Translation:** Vocabulary: convert: 转换

**[6333.08s] English:** And the fact that Tesla is, at least, getting there.  
**Translation:** 

**[6336.24s] English:** Or, if they are already there, makes me think that  
**Translation:** 

**[6340.78s] English:** It's now starting to be coupled to this self-supervised learning vision.  
**Translation:** 

**[6347.58s] English:** Which is like, if that's going to work,  
**Translation:** 

**[6349.86s] English:** If, through this purely mechanical process, you can get really far,  
**Translation:** 

**[6352.92s] English:** Then, maybe you can solve it that way.  
**Translation:** 

**[6354.76s] English:** I don't know.  
**Translation:** 

**[6355.40s] English:** I tend to believe we don't give enough credit.  
**Translation:** 

**[6360.00s] English:** To the amazing thing about humans is how they are both at driving and at supervising autonomous systems.  
**Translation:** 

**[6368.34s] English:** And also, we don't have this kind of driver sensing inside Teslas. I wish we did, and I wish there was much more of it.  
**Translation:** Vocabulary: autonomous: 自主; sensing: 感知; supervising: 监督; teslas: 特斯拉

**[6376.18s] English:** And much deeper consideration of human factors, like understanding psychology and drowsiness, and  
**Translation:** 

**[6384.76s] English:** All those kinds of things, when the car does more and more of the work, how to keep utilizing,...  
**Translation:** Vocabulary: drowsiness: 嗜睡; utilizing: 利用

**[6391.76s] English:** Little human supervision was needed to keep this whole thing safe; I mean, it's a fascinating project.  
**Translation:** 

**[6395.98s] English:** Dance of human-robot interaction: to me, autonomous driving has been a human-robot partnership for a long time.  
**Translation:** Vocabulary: supervision: 监管

**[6403.02s] English:** Interaction problem; it is not a robotics problem or computer vision problem, as you have to have  
**Translation:** 

**[6408.88s] English:** Human in the loop, but so, which is why I think it's 10 years plus, but I do think there'll be.  
**Translation:** Vocabulary: robotics: 机器人技术

**[6414.54s] English:** A  
**Translation:** 

**[6414.74s] English:** A bunch of cities and contexts where you know, uh, geo-restricted content will work really, really damn well.  
**Translation:** 

**[6421.34s] English:** Well, yeah, so I think for me, like, it's five if I'm being optimistic, and it's going to be five for a while.  
**Translation:** 

**[6426.34s] English:** Lots of cases, and 10 or more—yeah, I agree with you. Ten or more, basically, if we want to recover most of...  
**Translation:** 

**[6432.74s] English:** Say "contiguous United States" or something. Oh, interesting! So, my optimistic estimate is five.  
**Translation:** 

**[6438.42s] English:** Pessimistic is 30/30. I have a long tail on this one; I've watched enough driving videos.  
**Translation:** Vocabulary: contiguous: 相连的; estimate: 估计; optimistic: 乐观; pessimistic: 悲观

**[6444.56s] English:** Watched enough pedestrians to think: like, we may be okay, but there's still a small part of me that's not sure.  
**Translation:** 

**[6451.36s] English:** Like a pretty big part of me thinks we'll have to build AGI to solve driving.  
**Translation:** Vocabulary: pedestrians: 行人

**[6456.90s] English:** Oh, well, like there's something to me because humans are part of the picture deeply, part of the  
**Translation:** 

**[6462.64s] English:** Picture, and also human society is part of the picture, in that human life is at stake.  
**Translation:** 

**[6467.38s] English:** Anytime a robot kills a human, it's not clear to me that that's not a problem that.  
**Translation:** 

**[6474.56s] English:** Machine learning will also have to solve, yeah, like it has to; you have to integrate that into the  
**Translation:** Vocabulary: anytime: 任何时间; integrate: 整合

**[6479.72s] English:** The whole thing.  
**Translation:** 

**[6480.00s] English:** Just like Facebook or social networks, you know, one thing is to say how to make a really good  
**Translation:** 

**[6485.06s] English:** Recommender system, and then the other thing is to integrate that into the recommender system.  
**Translation:** 

**[6489.98s] English:** All the journalists that will write articles about that recommender system have to consider  
**Translation:** Vocabulary: recommender: 推荐系统

**[6494.98s] English:** The society within which the AI system operates, and in order to, you know, like politicians too.  
**Translation:** 

**[6500.94s] English:** This is there's regulatory stuff for autonomous driving, right? It's kind of fascinating that the  
**Translation:** Vocabulary: autonomous: 自主; regulatory: 监管

**[6505.82s] English:** More successful your AI system becomes, the more it gets integrated into society, and the more  
**Translation:** 

**[6512.06s] English:** Precious politicians, and the public, and the clickbait journalists, and all the different  
**Translation:** Vocabulary: clickbait: 诱饵式标题; integrated: 融合

**[6517.00s] English:** Fascinating forces of our society start acting on it, and then it's no longer "how good you are.  
**Translation:** 

**[6522.20s] English:** Doing the initial task is also how well you navigate human nature, which is a  
**Translation:** Vocabulary: navigate: 驾驭

**[6528.40s] English:** Fascinating space! What do you think are the limits of deep learning? If you allow me, we'll zoom out a bit.  
**Translation:** 

**[6534.14s] English:** A little bit into the big question.  
**Translation:** 

**[6535.80s] English:** Of artificial intelligence, you said that self-supervised learning is the "dark matter" of intelligence, but  
**Translation:** 

**[6543.08s] English:** There could be more. What do you think about the limits of self-supervised learning and just learning in general?  
**Translation:** 

**[6548.86s] English:** General deep learning, I think, is particularly like self-supervised.  
**Translation:** 

**[6553.88s] English:** Learning is, I would say, a little bit more vague right now, so I wouldn't like for something.  
**Translation:** 

**[6557.94s] English:** That's so vague; it's hard to predict what its limits are going to be, but, as I said, I  
**Translation:** 

**[6562.86s] English:** Think anywhere you want to; you know, interact with humans.  
**Translation:** 

**[6565.80s] English:** Even if you're learning something that's self-supervised, then you're going to have to  
**Translation:** 

**[6568.52s] English:** Put in some deep learning to be able to communicate with the human, and then when you're learning.  
**Translation:** 

**[6571.70s] English:** That self-supervised learning kind of hits a boundary very quickly because you need to have an  
**Translation:** 

**[6575.12s] English:** Interface to be able to communicate with the human, so really, like, if you have just like vacuous  
**Translation:** Vocabulary: interface: 人机接口; vacuous: 空洞

**[6579.86s] English:** Concepts, or like nebulous concepts discovered by a network—it's very hard to  
**Translation:** 

**[6584.90s] English:** Communicate those with a human, without like inserting some kind of human knowledge or some.  
**Translation:** 

**[6588.06s] English:** Kind of like human bias, there in general. I think for deep learning, the biggest challenge is just  
**Translation:** 

**[6593.64s] English:** Like data efficiency.  
**Translation:** 

**[6595.80s] English:** Once, like one image, of a, you know?  
**Translation:** 

**[6600.00s] English:** Or, however you want to call it, like any concept,  
**Translation:** 

**[6602.52s] English:** It's really hard for these methods to generalize.  
**Translation:** 

**[6604.80s] English:** By looking at just one or two samples of things.  
**Translation:** Vocabulary: generalize: 泛化

**[6607.70s] English:** And that has been a real challenge.  
**Translation:** 

**[6609.74s] English:** And I think that's actually why these edge cases,  
**Translation:** 

**[6611.66s] English:** For example, for Tesla, they are actually that important.  
**Translation:** 

**[6614.52s] English:** Because, if you see just one instance of the car failing,...  
**Translation:** 

**[6618.04s] English:** And if you just annotate that,  
**Translation:** 

**[6619.30s] English:** And you get that into your dataset.  
**Translation:** Vocabulary: annotate: 标注; dataset: 数据集

**[6621.92s] English:** You have a very limited guarantee.  
**Translation:** 

**[6623.56s] English:** That it's not going to happen again.  
**Translation:** 

**[6625.14s] English:** And you're actually going to be able to recognize.  
**Translation:** 

**[6626.74s] English:** This kind of instance in a very different scenario.  
**Translation:** Vocabulary: scenario: 场景

**[6628.62s] English:** So, like, when it was snowing,  
**Translation:** 

**[6630.30s] English:** So, you got that thing labeled when it was snowing.  
**Translation:** Vocabulary: labeled: 标记了

**[6632.04s] English:** But now, when it's raining,  
**Translation:** 

**[6633.22s] English:** You're actually not able to get it.  
**Translation:** 

**[6634.64s] English:** Or, you basically have the same scenario.  
**Translation:** 

**[6636.60s] English:** In a different part of the world,  
**Translation:** 

**[6637.44s] English:** So, the lighting was different, or so on.  
**Translation:** 

**[6639.12s] English:** So, it's just really hard for these models.  
**Translation:** Vocabulary: lighting: 照明

**[6641.02s] English:** Like deep learning, especially, to do that.  
**Translation:** 

**[6642.72s] English:** What's your intuition?  
**Translation:** Vocabulary: intuition: 直觉

**[6643.56s] English:** How do we solve the handwritten digit recognition problem?  
**Translation:** 

**[6647.58s] English:** When we only have one example for each number?  
**Translation:** Vocabulary: digit: 阿拉伯数字; handwritten: 手写

**[6651.22s] English:** It feels like humans are using something like learning.  
**Translation:** 

**[6654.72s] English:** Right, I think it's,  
**Translation:** 

**[6656.02s] English:** We are good at transferring knowledge.  
**Translation:** 

**[6658.38s] English:** A little bit.  
**Translation:** Vocabulary: transferring: 转移

**[6659.26s] English:** We are just better at, like,  
**Translation:** 

**[6661.24s] English:** For a lot of these problems,  
**Translation:** 

**[6662.64s] English:** Where we are generalizing from a single sample,  
**Translation:** 

**[6664.84s] English:** Or recognizing from a single sample,  
**Translation:** Vocabulary: generalizing: 概括外推

**[6666.94s] English:** We are using a lot of our own domain knowledge.  
**Translation:** 

**[6668.74s] English:** And a lot of our inductive bias.  
**Translation:** Vocabulary: inductive: 归纳的

**[6670.34s] English:** Into that one sample, we can generalize it.  
**Translation:** 

**[6672.30s] English:** So, I've never seen you write the number nine, for example.  
**Translation:** 

**[6675.32s] English:** And if you were to write it, I would still get it.  
**Translation:** 

**[6677.44s] English:** And if you were to write a different kind of alphabet:  
**Translation:** 

**[6679.28s] English:** And like, write it in two different ways.  
**Translation:** 

**[6680.82s] English:** I would still probably be able to figure it out.  
**Translation:** 

**[6682.32s] English:** That these are the same two characters.  
**Translation:** 

**[6684.70s] English:** It's just that I have been very used.  
**Translation:** 

**[6686.28s] English:** To seeing handwritten digits in my life.  
**Translation:** 

**[6688.16s] English:** The other sort of problem with any deep learning system is...  
**Translation:** Vocabulary: digits: 手写数字

**[6691.34s] English:** Or any kind of machine learning system.  
**Translation:** 

**[6692.70s] English:** It's like its guarantees, right?  
**Translation:** Vocabulary: guarantees: 保证

**[6694.16s] English:** There are no guarantees for it.  
**Translation:** 

**[6695.86s] English:** Now, you can argue that humans  
**Translation:** 

**[6696.94s] English:** Also, don't have any guarantees.  
**Translation:** 

**[6698.16s] English:** Like, there is no guarantee that I can recognize a cat.  
**Translation:** 

**[6701.12s] English:** In every scenario.  
**Translation:** 

**[6702.24s] English:** I'm sure there are going to be lots of cats.  
**Translation:** 

**[6703.90s] English:** That I don't recognize,  
**Translation:** 

**[6705.04s] English:** Lots of scenarios in which I don't recognize cats in general.  
**Translation:** Vocabulary: scenarios: 情景

**[6708.10s] English:** But I think from there,  
**Translation:** 

**[6710.26s] English:** From just an application perspective,  
**Translation:** 

**[6712.84s] English:** You do need guarantees, right?  
**Translation:** 

**[6714.74s] English:** We call these things algorithms.  
**Translation:** 

**[6716.94s] English:** Now, algorithms,  
**Translation:** 

**[6718.16s] English:** Traditional CS algorithms have guarantees.  
**Translation:** 

**[6720.00s] English:** Sorting is a guarantee.  
**Translation:** 

**[6721.50s] English:** If you were to call sort on a particular array of numbers,  
**Translation:** Vocabulary: sorting: 排序

**[6725.64s] English:** You are guaranteed that it's going to be sorted.  
**Translation:** 

**[6727.66s] English:** Otherwise, it's a bug.  
**Translation:** Vocabulary: guaranteed: 有保证的

**[6729.34s] English:** Now, for machine learning,  
**Translation:** 

**[6730.18s] English:** It's very hard to characterize this.  
**Translation:** Vocabulary: characterize: 描述

**[6732.48s] English:** We know for a fact that a cat recognition model,  
**Translation:** 

**[6735.48s] English:** Is not going to recognize cats.  
**Translation:** 

**[6737.08s] English:** Every cat in the world, in every circumstance.  
**Translation:** 

**[6739.76s] English:** I think most people would agree with that statement.  
**Translation:** Vocabulary: circumstance: 情况

**[6742.08s] English:** But we are still okay with it.  
**Translation:** 

**[6743.64s] English:** We still don't call this a bug.  
**Translation:** 

**[6745.44s] English:** As in traditional computer science or traditional science,  
**Translation:** 

**[6748.06s] English:** If you have this kind of failure case existing,  
**Translation:** 

**[6750.02s] English:** Then you think of it as if something is wrong.  
**Translation:** 

**[6753.26s] English:** I think there is this sort of notion.  
**Translation:** 

**[6754.60s] English:** Of nebulous correctness in machine learning,  
**Translation:** 

**[6757.10s] English:** And that's something we just need.  
**Translation:** Vocabulary: correctness: 正确性; nebulous: 模糊的

**[6757.98s] English:** To be very comfortable with.  
**Translation:** 

**[6759.56s] English:** And for deep learning,  
**Translation:** 

**[6760.62s] English:** Or, like, for a lot of these machine learning algorithms,  
**Translation:** 

**[6762.78s] English:** It's not clear how we characterize.  
**Translation:** 

**[6764.78s] English:** This notion of correctness.  
**Translation:** 

**[6766.40s] English:** I think limitations in our understanding,  
**Translation:** 

**[6768.22s] English:** Or, at least, a limitation in our phrasing of this.  
**Translation:** 

**[6771.24s] English:** And, if we were to come up with better ways,...  
**Translation:** Vocabulary: phrasing: 表达方式

**[6773.16s] English:** To understand this limitation,  
**Translation:** 

**[6775.14s] English:** Then it would actually help us a lot.  
**Translation:** 

**[6777.26s] English:** Do you think there's  
**Translation:** 

**[6778.04s] English:** A distinction between the concept of learning,  
**Translation:** 

**[6781.82s] English:** And what is the concept of reasoning?  
**Translation:** 

**[6784.26s] English:** Do you think it's possible for neural networks to reason?  
**Translation:** Vocabulary: neural: 神经的

**[6790.30s] English:** So, I think of it slightly differently.  
**Translation:** 

**[6791.66s] English:** So, for me, learning is whenever I can make a snap judgment.  
**Translation:** 

**[6796.06s] English:** So, if you show me a picture of a dog,  
**Translation:** 

**[6797.20s] English:** I can immediately say, "It's a dog.  
**Translation:** 

**[6798.88s] English:** But if you give me, like, a puzzle,  
**Translation:** 

**[6800.42s] English:** You know, like whatever, a Goldberg machine.  
**Translation:** Vocabulary: goldberg: 复杂装置

**[6803.46s] English:** Of like things going to happen,  
**Translation:** 

**[6804.96s] English:** Then I have to reason.  
**Translation:** 

**[6805.80s] English:** Because I've never seen it before; it's a very complicated setup.  
**Translation:** 

**[6807.60s] English:** I've never seen that particular setup.  
**Translation:** Vocabulary: setup: 装置

**[6809.34s] English:** And I really need to, you know, draw and imagine.  
**Translation:** 

**[6811.84s] English:** In my head, I'm trying to figure out what's going to happen.  
**Translation:** 

**[6814.68s] English:** So, I think, yes, neural networks are really good.  
**Translation:** 

**[6816.86s] English:** At recognition, but they're not very good at reasoning.  
**Translation:** 

**[6821.20s] English:** Because they're like, if they've seen something before.  
**Translation:** 

**[6824.14s] English:** Have you seen something similar before?  
**Translation:** 

**[6825.82s] English:** They're very good at making those sorts of snap judgments.  
**Translation:** 

**[6828.16s] English:** But if you were to give them a very complicated thing,  
**Translation:** Vocabulary: judgments: 快速判断

**[6830.74s] English:** That they've not seen before,  
**Translation:** 

**[6832.52s] English:** They have very limited ability right now.  
**Translation:** 

**[6835.36s] English:** To compose different things.  
**Translation:** 

**[6836.60s] English:** I've seen this particular part before; I've seen it before.  
**Translation:** Vocabulary: compose: 组合

**[6840.00s] English:** And now, probably, they're going to work in tandem.  
**Translation:** 

**[6842.86s] English:** It's very hard for them to come up with these kinds of things.  
**Translation:** Vocabulary: tandem: 同频协作

**[6845.02s] English:** Well, there's a certain aspect to reasoning that you can maybe convert into the process of programming.  
**Translation:** 

**[6851.92s] English:** And so, there's the whole field of program synthesis.  
**Translation:** Vocabulary: convert: 转换; synthesis: 合成

**[6854.40s] English:** And people have been applying machine learning to the problem of program synthesis.  
**Translation:** 

**[6859.02s] English:** And the question is: You know, can the step of composition be learned, why can't it be learned?  
**Translation:** 

**[6863.92s] English:** You know, this step of building things on top of it, like little intuitions and concepts on top of each other.  
**Translation:** 

**[6872.88s] English:** Can that be learnable?  
**Translation:** Vocabulary: intuitions: 直觉

**[6875.14s] English:** What's your intuition there?  
**Translation:** 

**[6876.82s] English:** Or, like, I guess, a similar set of techniques, do you think that would be applicable?  
**Translation:** 

**[6882.06s] English:** So, I think it is, of course, learnable because, like us, humans are prime examples of individuals that have learned this, right?  
**Translation:** 

**[6889.48s] English:** Like humans have learned this.  
**Translation:** 

**[6890.78s] English:** So, it is, of course, a technique that is very easy to learn.  
**Translation:** 

**[6893.92s] English:** I think we're hitting a wall with current machine learning because, basically, once the network learns all this information, we're not able to figure out how well it will generalize to an unseen thing.  
**Translation:** Vocabulary: generalize: 泛化能力

**[6910.28s] English:** And we have no, a priori, way of characterizing that.  
**Translation:** 

**[6914.70s] English:** And I think that's basically telling us a lot about, like, a lot about the fact that we really don't know what this model has learned and how well it's going to generalize.  
**Translation:** Vocabulary: priori: 先验的

**[6923.92s] English:** There's also a sense in which it feels like we humans may not be aware of how much like background knowledge, how good our background model is, and how much knowledge we just have slowly building on top of each other.  
**Translation:** 

**[6941.50s] English:** It feels like neural networks are constantly throwing stuff out.  
**Translation:** Vocabulary: neural: 神经的

**[6944.00s] English:** Like, you'll do some incredible thing where you're learning a particular task in computer vision.  
**Translation:** 

**[6948.88s] English:** You celebrate your state-of-the-art successes, and you throw that out.  
**Translation:** 

**[6952.54s] English:** It feels like.  
**Translation:** 

**[6953.92s] English:** You're never using stuff you've learned for your future successes in other domains.  
**Translation:** 

**[6960.00s] English:** And humans are obviously doing that exceptionally well: still throwing stuff away in their minds, but keeping certain kernels of truth.  
**Translation:** 

**[6967.74s] English:** Right. So, I think we're like continual learning is sort of the paradigm for this in machine learning.  
**Translation:** Vocabulary: continual: 持续; exceptionally: 非常; kernels: 核心; paradigm: 范式

**[6972.08s] English:** And I don't think it's a very well-explored paradigm.  
**Translation:** 

**[6974.38s] English:** Yeah.  
**Translation:** 

**[6975.06s] English:** We have issues like catastrophic forgetting in deep learning, for example, which is one of the standard problems.  
**Translation:** 

**[6980.34s] English:** The thing is, basically, that if you train a network to recognize dogs and then train the same network to recognize cats, it basically forgets how to recognize dogs.  
**Translation:** Vocabulary: catastrophic: 灾难性的

**[6989.12s] English:** So, it forgets very quickly.  
**Translation:** 

**[6991.02s] English:** I mean, and whereas a human, if you were to teach someone to recognize dogs and then to recognize cats, they don't forget immediately how to recognize these dogs.  
**Translation:** 

**[6998.52s] English:** I think that's basically what you're trying to get.  
**Translation:** 

**[7000.76s] English:** Yeah, I just wonder if there are long-term memory mechanisms or mechanisms that store not just memories, but concepts that allow you to reason and compose them.  
**Translation:** Vocabulary: compose: 组成

**[7016.98s] English:** If those things will look very different.  
**Translation:** 

**[7019.12s] English:** Or, if you can do that within a single neural network with some particular architectural quirks, that seems to be a really open problem.  
**Translation:** Vocabulary: architectural: 架构; quirks: 怪异特性

**[7027.94s] English:** And of course, I go up and down on that because there's something so compelling to the symbolic AI or to the ideas of logic-based sort of expert systems.  
**Translation:** 

**[7040.52s] English:** You have a series of human-interpretable facts that build on top of each other.  
**Translation:** Vocabulary: compelling: 有吸引力的; symbolic: 象征性的

**[7043.86s] English:** It's really annoying, like with self-supervised learning that.  
**Translation:** 

**[7049.12s] English:** The AI is not very explainable; like, you can't really understand all the beautiful things it has learned.  
**Translation:** 

**[7055.68s] English:** You can't ask it like questions.  
**Translation:** 

**[7058.48s] English:** But then again, maybe that's a stupid thing for us humans to want.  
**Translation:** 

**[7062.50s] English:** But I think whenever we try to understand it, we're putting our own subjective human bias into it.  
**Translation:** 

**[7067.90s] English:** Yeah.  
**Translation:** 

**[7068.44s] English:** And I think that's the sort of problem with self-supervised learning.  
**Translation:** 

**[7071.14s] English:** The goal is that it should learn naturally from the data.  
**Translation:** 

**[7074.40s] English:** So, now if you try to understand it, you are using your own preconceived notions of.  
**Translation:** 

**[7079.00s] English:** What?  
**Translation:** Vocabulary: notions: 先入为主的观念; preconceived: 先入为主的

**[7079.12s] English:** What this model has:  
**Translation:** 

**[7080.00s] English:** Learned, and that's the problem. High-level question: What do you think it takes to build a system?  
**Translation:** 

**[7087.84s] English:** With superhuman, maybe let's say human-level or superhuman-level general intelligence, we've  
**Translation:** 

**[7093.84s] English:** Already kind of started talking about this, but what's your intuition like? Does the thing have...  
**Translation:** Vocabulary: intuition: 直觉

**[7098.72s] English:** To have a body, does it have to interact richly with the world? Does it have to have?  
**Translation:** 

**[7106.40s] English:** Some more human elements, like self-awareness—I think emotion—is something which  
**Translation:** 

**[7113.68s] English:** Is like it's not really attributed typically in standard machine learning; it's not something we  
**Translation:** 

**[7118.96s] English:** Think about it: there is NLP, there is vision, but there is no emotion; emotion is never a part.  
**Translation:** Vocabulary: attributed: 归因

**[7123.60s] English:** Of all of this, and that just seems a little bit weird to me. I think the reason, basically, being  
**Translation:** 

**[7128.24s] English:** That there is surprise, and like, basically, emotions are one of the reasons why they arise.  
**Translation:** 

**[7135.04s] English:** What happens, and what you expect.  
**Translation:** 

**[7136.40s] English:** To happen, right there is like a mismatch between these things, and so that gives rise to something like I can.  
**Translation:** 

**[7141.36s] English:** Either I can be surprised, or I can be saddened, or I can be happy—and all of this, and so.  
**Translation:** 

**[7146.88s] English:** This basically indicates that I already have a predictive model in my head, and something that  
**Translation:** Vocabulary: predictive: 预测性的

**[7150.80s] English:** I predicted, or something I thought was likely to happen, and then there was something.  
**Translation:** 

**[7154.40s] English:** That I observed: there was a disconnect between these two things, and that  
**Translation:** Vocabulary: disconnect: 不一致

**[7158.64s] English:** Basically, it's like maybe one of the reasons I like you has a lot of emotions, yeah. I think so.  
**Translation:** 

**[7166.40s] English:** I think a lot about Lisa Feldman Barrett's idea of emotion, but  
**Translation:** 

**[7172.08s] English:** I have a sense that emotion, primarily in the way we think about it, which is the display of emotion.  
**Translation:** 

**[7180.32s] English:** Is a communication mechanism between humans, so it's essentially a part of basic human interaction.  
**Translation:** 

**[7186.40s] English:** Interaction: Um, an important part, but just the part, so it's like, I would throw it in there.  
**Translation:** 

**[7193.44s] English:** Um, into the full mix of  
**Translation:** 

**[7196.40s] English:** Communication and, to me, communication.  
**Translation:** 

**[7200.00s] English:** Can be done with objects that don't look at all like humans, okay. I've seen our ability to  
**Translation:** 

**[7206.70s] English:** Anthropomorphize our ability to connect with things that look like a rumba, and our ability to connect.  
**Translation:** 

**[7211.70s] English:** First, let's talk about other biological systems, like dogs, and our ability to love them.  
**Translation:** Vocabulary: anthropomorphize: 赋予拟人化; rumba: 伦巴舞

**[7217.54s] English:** Are very different from humans, but they do display emotion, right? I mean, dogs do display  
**Translation:** 

**[7222.16s] English:** Emotion, so they don't have to be anthropomorphic to display the kind of emotion that.  
**Translation:** Vocabulary: anthropomorphic: 拟人化的

**[7227.68s] English:** We don't exactly, so I mean, but then the word "emotion" starts to lose its meaning, so then we have to be  
**Translation:** 

**[7234.60s] English:** I guess specific but, yeah. So, have rich, flavorful communication, communication, yeah, yeah. So, like,  
**Translation:** Vocabulary: flavorful: 有层次感的

**[7240.84s] English:** Yes, it's full of emotion, it's full of wit and humor, and all those kinds of things.  
**Translation:** 

**[7250.02s] English:** Yeah, so exactly. So you're talking about like flavors, right? Okay, let's follow that up so  
**Translation:** Vocabulary: flavors: 口味

**[7255.54s] English:** There's content, and then there is flavor, and I'm talking.  
**Translation:** 

**[7257.62s] English:** Yeah.  
**Translation:** 

**[7257.68s] English:** Do you think it needs to have a body? Do you think it should be able to interact with the physical world?  
**Translation:** 

**[7262.98s] English:** I think you can understand the physical world without being able to directly interact with it, and I don't.  
**Translation:** 

**[7267.30s] English:** Think so, yeah. I think at some point we will need to bite the bullet and actually interact with the  
**Translation:** 

**[7271.68s] English:** Physical, as much as I like working on passive computer vision where I just sit in my armchair.  
**Translation:** 

**[7277.04s] English:** Chair, and look at videos and learn—I do think that we will need to have some kind of embodiment.  
**Translation:** 

**[7282.40s] English:** Or, for some kind of interaction to figure out things about the world, what about consciousness?  
**Translation:** Vocabulary: consciousness: 觉醒; embodiment: 具身

**[7287.62s] English:** You think: How often do you think about consciousness when you think about your work?  
**Translation:** 

**[7293.40s] English:** You could think of it as the more simple thing of self-awareness, of being aware that you are a  
**Translation:** 

**[7301.68s] English:** Perceiving, sensing, acting — things in this world, or you can think about the bigger version of.  
**Translation:** 

**[7310.16s] English:** That, which is consciousness, is having it feel like something to be that entity.  
**Translation:** Vocabulary: perceiving: 感知; sensing: 感知

**[7317.62s] English:** Active experience of being in this world, so I think of.  
**Translation:** 

**[7320.00s] English:** Self-awareness, a little bit more than this, like the broader goal of it, because I think self-awareness...  
**Translation:** 

**[7324.86s] English:** Is pretty critical for any kind of AGI or whatever you want to call it.  
**Translation:** 

**[7330.26s] English:** We'll build because it needs to contextualize what it is and what role it's playing with respect to...  
**Translation:** 

**[7336.20s] English:** All the other things that exist around it, I think, require self-awareness; it needs to understand.  
**Translation:** 

**[7340.54s] English:** That it's an autonomous car, right? And what does that mean? What are its limitations? What are the  
**Translation:** Vocabulary: autonomous: 自主的

**[7346.96s] English:** Things that it is supposed to do, and so on. What is its role, in some way or another? I mean, so I mean this.  
**Translation:** 

**[7353.26s] English:** These are the kinds of things that we kind of expect from it, I would say, and so that's the  
**Translation:** 

**[7358.38s] English:** Level of self-awareness that I would say is basically required—at least, if not more than that.  
**Translation:** 

**[7363.30s] English:** Yeah, I tend to, on the emotional side, believe that it has to be able to display.  
**Translation:** 

**[7369.86s] English:** Consciousness: Display consciousness. What do you mean by that? Meaning, like for us humans to connect.  
**Translation:** 

**[7376.02s] English:** With each other.  
**Translation:** Vocabulary: consciousness: 觉醒

**[7376.96s] English:** Or, to connect with other living entities, I think we need to feel like, in order for us to truly  
**Translation:** 

**[7386.40s] English:** Feel like there's another being there; we have to believe that they're conscious, and so.  
**Translation:** 

**[7391.86s] English:** We won't ever connect with something that doesn't have elements of consciousness. Now, I tend to think,...  
**Translation:** 

**[7398.26s] English:** That's easier to achieve than it may sound because we anthropomorphize stuff so easily, like  
**Translation:** Vocabulary: anthropomorphize: 赋予人类特征

**[7405.90s] English:** You have a  
**Translation:** 

**[7406.94s] English:** Mug that just like has wheels and likes to rotate every once in a while and makes a sound, I think.  
**Translation:** Vocabulary: rotate: 旋转

**[7412.32s] English:** A couple of days in, especially if you're not hanging out with humans, you  
**Translation:** 

**[7419.62s] English:** Might start to believe that mug on wheels is conscious, so I think we anthropomorphize pretty.  
**Translation:** 

**[7424.26s] English:** Effectively, as human beings, but I do think that it's in the same bucket that we'll call  
**Translation:** 

**[7429.84s] English:** Emotion that shows that, uh, you're, you know, I think of consciousness as the capacity to  
**Translation:** 

**[7436.74s] English:** Suffer, and to live, and to live, and to live, and to live, and to live, and to live, and to live.  
**Translation:** 

**[7436.94s] English:** And to live, and to live, and to live, and to live, and to live, and to live, and to live, and to live, and  
**Translation:** 

**[7437.94s] English:** To live, and to live, and to live, and to live, and to live, and to live, and to live, and to live, and to live.  
**Translation:** 

**[7438.94s] English:** And to live, and to live, and to live, and to live, and to live, and to live, and to live, and to live.  
**Translation:** 

**[7439.94s] English:** And to live, and to live, and to live, and to live, and to live, and to live, and to live, and to live.  
**Translation:** 

**[7440.00s] English:** Able to feel things in the world and to communicate that to others, I think that's a really powerful experience.  
**Translation:** 

**[7440.94s] English:** And to live, and to live, and to live, and to live, and to live, and to live, and to live, and to live, and to live.  
**Translation:** 

**[7441.94s] English:** And to live, and to live, and to live, and to live, and to live, and to live, and to live, and to live, and to live.  
**Translation:** 

**[7442.94s] English:** And to live, and to live, and to live, and to live, and to live, and to live, and to live, and to live, and to live.  
**Translation:** 

**[7448.04s] English:** A way to interact with humans, and in order to create an AGI system, I believe you should be able  
**Translation:** 

**[7455.32s] English:** To richly interact with humans, like humans would need to want to interact with you, it can't.  
**Translation:** 

**[7461.66s] English:** It's like self-supervised learning versus the idea that a robot shouldn't have to  
**Translation:** 

**[7468.84s] English:** Pay you to interact with me, so it should be a natural, fun thing, and then you're going to  
**Translation:** 

**[7474.58s] English:** Scale up significantly how much interaction it gets, yeah. It's the Alexa Prize, which they're  
**Translation:** 

**[7481.28s] English:** Trying to get me to be a judge on their contest? I'll see if I want to do that, but their...  
**Translation:** 

**[7486.66s] English:** The challenge is to talk to you and make the judge sufficiently interested that the  
**Translation:** Vocabulary: sufficiently: 足够地

**[7494.32s] English:** Human keeps talking to Alexa for 20 minutes, to Alexa, yeah.  
**Translation:** 

**[7498.84s] English:** Right now, they're not even close to that because it just gets so boring when you're like, when...  
**Translation:** 

**[7502.94s] English:** The intelligence is not there; it gets very uninteresting to talk to it, and so the robot needs better programming.  
**Translation:** 

**[7508.14s] English:** To be interesting, and one of the ways it can be interesting is by displaying the capacity to love.  
**Translation:** Vocabulary: uninteresting: 没意思

**[7513.30s] English:** To suffer, I would say that essentially means the capacity to display consciousness, like it.  
**Translation:** 

**[7521.20s] English:** Is an entity much like a human being, of course. What that really means, I don't know if that's  
**Translation:** Vocabulary: consciousness: 觉醒能力

**[7528.84s] English:** A robotics problem, or some kind of problem that we're not yet even aware—like if it is truly a...  
**Translation:** 

**[7534.10s] English:** Hard problem of consciousness; I tend to maybe optimistically think it's a problem we can pretty  
**Translation:** Vocabulary: optimistically: 乐观地; robotics: 机器人学

**[7540.46s] English:** Effectively, "fake it till we make it" so we can display a lot of human-like elements for a while.  
**Translation:** 

**[7545.90s] English:** And that will be sufficient to form really close connections with humans.  
**Translation:** 

**[7550.46s] English:** What to use the most beautiful idea in self-supervised learning, like when you sit back.  
**Translation:** 

**[7556.88s] English:** With, uh, I don't know. I don't know. I don't know. I don't know. I don't know. I don't know. I don't know.  
**Translation:** 

**[7558.84s] English:** With a glass of wine.  
**Translation:** 

**[7560.00s] English:** And I sit in an armchair by a fireplace, just thinking how beautiful this world is.  
**Translation:** Vocabulary: fireplace: 壁炉

**[7568.52s] English:** Get to explore is what do you think is especially beautiful? The idea that, like,  
**Translation:** 

**[7574.56s] English:** Object-level: What objects are in some notion of objectness emerges from these models, just like.  
**Translation:** Vocabulary: emerges: 出现; objectness: 对象感

**[7581.70s] English:** Self-supervised learning, so for example, like the DINO paper, that  
**Translation:** 

**[7589.14s] English:** I was a part of at Facebook is that, um, the object sorts of boundaries emerge from these representations.  
**Translation:** 

**[7595.16s] English:** So, if you have a dog running in the field, the boundaries around the dog are the network.  
**Translation:** 

**[7600.06s] English:** Basically, we can figure out what the boundaries of this dog are automatically.  
**Translation:** 

**[7604.28s] English:** And it was never trained to do that; it was never trained to, uh, no one taught it that this is a dog.  
**Translation:** 

**[7610.94s] English:** And these pixels belong to a dog; it's able to group these things together automatically, so  
**Translation:** Vocabulary: pixels: 像素

**[7615.16s] English:** That's one, and I think, in general, that entire notion that  
**Translation:** 

**[7618.30s] English:** This dumb idea is that you take, like, these two crops of an image and then you say that the features...  
**Translation:** 

**[7623.10s] English:** It should be similar, that has resulted in something like this, where the model is able to figure out.  
**Translation:** 

**[7627.88s] English:** What the dog pixels are, and so on, just seems like such a surprise. Um, and I don't think a  
**Translation:** 

**[7634.76s] English:** A lot of us don't even understand how that is happening, and it's something we are  
**Translation:** 

**[7639.14s] English:** Taking for granted, perhaps a lot in terms of how we're setting up these algorithms, but it's  
**Translation:** 

**[7644.62s] English:** Just, it's a very beautiful and powerful idea. So, it's really fundamentally telling us the  
**Translation:** 

**[7648.30s] English:** Something about that: there is so much signal in the pixels that we can be super dumb about it.  
**Translation:** Vocabulary: fundamentally: 本质上

**[7654.04s] English:** About how we're setting up the self-supervising problem, and despite being super dumb about it,  
**Translation:** 

**[7659.42s] English:** We'll actually get something very good, uh, that is able to do  
**Translation:** 

**[7663.92s] English:** Very, like, surprising things. I wonder if there are other, like, objects or concepts that can  
**Translation:** 

**[7669.60s] English:** Emerge: I don't know if you follow François Chollet; he had the competition for intelligence.  
**Translation:** Vocabulary: chollet: 乔勒特

**[7678.30s] English:** Kind of like an IQ test, but from a  
**Translation:** 

**[7680.00s] English:** Means, but for an IQ test, you have to have a few concepts that you want to apply; one of them is  
**Translation:** 

**[7685.98s] English:** Objectness: I wonder if those concepts can emerge through self-supervised learning on billions of.  
**Translation:** 

**[7693.52s] English:** Images, I think, something like object permanence can definitely emerge, right? So, that's like a  
**Translation:** Vocabulary: objectness: 物体性; permanence: 持久性

**[7698.00s] English:** A fundamental concept which we have, perhaps, not been conveying through images or videos — but that's another concept.  
**Translation:** 

**[7702.74s] English:** That should be emergent from it, because it's not something that, like, we don't teach humans that.  
**Translation:** Vocabulary: conveying: 传递; emergent: 自然产生

**[7708.54s] English:** This isn't like about this concept of object permanence; it actually emerges, and  
**Translation:** 

**[7712.70s] English:** Same thing for, like, animals like dogs; I think actually permanence automatically is something.  
**Translation:** Vocabulary: emerges: 出现

**[7716.72s] English:** That they are born with, so I think it should emerge from the data. It should emerge basically.  
**Translation:** 

**[7721.32s] English:** Very quickly, I wonder if ideas like symmetry and rotation might emerge.  
**Translation:** Vocabulary: symmetry: 对称

**[7727.18s] English:** So, I think rotation probably is a good idea, yes, yeah. Rotation, I mean, there are some constraints, but...  
**Translation:** 

**[7732.88s] English:** Architecture itself, right? But it's interesting if all of them could be.  
**Translation:** 

**[7738.54s] English:** Like counting was another one; you know, being able to kind of understand that there are multiples.  
**Translation:** 

**[7745.66s] English:** Objects of the same kind in the image, and be able to count them. I wonder if all of that could be done.  
**Translation:** Vocabulary: multiples: 倍数

**[7751.78s] English:** Constructed correctly, they can emerge, because then you can transfer those concepts to um.  
**Translation:** 

**[7757.04s] English:** To then interpret images at a deeper level, right? I do believe it should be possible.  
**Translation:** Vocabulary: interpret: 解释

**[7764.10s] English:** You don't know yet, but I do think it's not that far in the realm of possibility.  
**Translation:** 

**[7768.54s] English:** Yeah, that would be interesting if using self-supervised learning on images.  
**Translation:** 

**[7772.72s] English:** Can then be applied to solving those kinds of IQ tests, which seem currently to be kind of  
**Translation:** 

**[7777.94s] English:** Impossible: What idea do you believe might be true that most people think is not true?  
**Translation:** 

**[7786.10s] English:** Or, don't agree with you on that. Is there something like that? So, this is going to be a little...  
**Translation:** 

**[7791.66s] English:** Controversial, but okay, sure. I don't believe in simulation—like, actually using simulation to do.  
**Translation:** 

**[7796.78s] English:** Things very much.  
**Translation:** 

**[7798.54s] English:** Just to clarify, because  
**Translation:** Vocabulary: clarify: 澄清

**[7800.00s] English:** This is a podcast, so you talk about whether we're living in a simulation. Often, you're referring to it.  
**Translation:** 

**[7805.20s] English:** Referring to using simulation to construct worlds that you then leverage for machine learning, right?  
**Translation:** Vocabulary: leverage: 利用

**[7810.54s] English:** Yeah, for example, like one example would be training an autonomous car driving system.  
**Translation:** 

**[7815.60s] English:** Basically, first build a simulator that builds the environment of the world, and then you  
**Translation:** Vocabulary: autonomous: 自主; simulator: 模拟器

**[7820.22s] English:** Basically, we have a lot of data to train our machine learning system, so I believe it.  
**Translation:** 

**[7826.92s] English:** Is possible, but I think it's a really expensive way of doing things, uh, and at the end of it, you  
**Translation:** 

**[7832.66s] English:** Do we need the real world? So, I'm not sure. Maybe for certain settings, like maybe the payout is so  
**Translation:** 

**[7838.40s] English:** Large, like for autonomous driving, the payout is so large that you can actually invest that much.  
**Translation:** Vocabulary: payout: 赔偿金

**[7842.26s] English:** Money to build it, but I think, as a general sort of principle, it does not apply to a lot of concepts.  
**Translation:** 

**[7846.94s] English:** You can't really build simulations of everything; uh, not only because, like, it's expensive.  
**Translation:** Vocabulary: simulations: 模拟

**[7851.42s] English:** Because, a second, it's also not possible for a lot of things. Uh, so, in general, like, there is a lot of  
**Translation:** 

**[7856.92s] English:** Um, like there's a lot of work on using synthetic data and synthetic simulators, I  
**Translation:** Vocabulary: simulators: 模拟器; synthetic: 合成的

**[7862.26s] English:** Generally, I am not very into that. So you're saying it's very challenging?  
**Translation:** 

**[7867.16s] English:** Visually, we like to correctly simulate the lighting and all those kinds of effects.  
**Translation:** Vocabulary: lighting: 照明; simulate: 模拟; visually: 视觉上

**[7873.30s] English:** I mean, I mean, all these companies that you have, like Pixar and, well, all these.  
**Translation:** 

**[7878.14s] English:** Companies are, if they're all about this kind of computer graphics stuff, it's really about accuracy a lot.  
**Translation:** 

**[7883.10s] English:** Of them is about accurately trying to figure out how the lighting.  
**Translation:** 

**[7886.92s] English:** Is and like how things reflect off of one another, and so on, and like how sparkly things look, and  
**Translation:** Vocabulary: sparkly: 闪耀的

**[7891.92s] English:** So, it's a very hard problem. So, do we really need to solve that first to be able to, like, do  
**Translation:** 

**[7898.16s] English:** Computer vision, probably not, and for me, in the context of autonomous driving, it's very tempting.  
**Translation:** Vocabulary: autonomous: 自主的; tempting: 有吸引力的

**[7905.68s] English:** To be able to use simulation, right? Because it's a safety-critical application, but the other  
**Translation:** 

**[7911.98s] English:** Limitation of simulation: That, perhaps, is a bigger one than the  
**Translation:** 

**[7916.92s] English:** Visual limitations are the behaviors of objects.  
**Translation:** 

**[7920.00s] English:** Because the way you're ultimately interested is in edge cases, and the  
**Translation:** 

**[7924.14s] English:** The question is: How well can you generate edge cases in simulation, especially with?  
**Translation:** 

**[7929.40s] English:** Human behavior: I think another problem is like for autonomous driving, right?  
**Translation:** 

**[7933.44s] English:** It's a constantly changing world, so autonomous driving, for example, might look very different in 10 years from now.  
**Translation:** 

**[7938.12s] English:** Now, like, there are lots of autonomous cars, but they're still going to be  
**Translation:** 

**[7941.60s] English:** Humans, yeah, so now 50% of the agents say, which are humans, 50% of the  
**Translation:** 

**[7945.92s] English:** Agents that are autonomous, like car-driving agents, so now the mixture is:  
**Translation:** Vocabulary: mixture: 混合物

**[7949.28s] English:** Changed, so now the kinds of behaviors that you actually expect from the other.  
**Translation:** 

**[7952.76s] English:** Other agents or other cars on the road that are actually going to be very  
**Translation:** 

**[7955.94s] English:** Different, and as the proportion of autonomous cars to humans increases.  
**Translation:** 

**[7959.54s] English:** Keeps changing this behavior will actually change a lot. So, now if you were  
**Translation:** 

**[7963.26s] English:** To build a simulator based on what we have today, you don't  
**Translation:** 

**[7966.74s] English:** Have that many autonomous cars on the road, so you try to make all of the  
**Translation:** Vocabulary: simulator: 模拟器

**[7969.86s] English:** Other agents in that simulator behave as humans, but that's not really going to.  
**Translation:** 

**[7973.94s] English:** Hold true, 10, 15, 20, 30 years from now: Do you think we're living in a simulation?  
**Translation:** 

**[7978.78s] English:** No.  
**Translation:** 

**[7979.28s] English:** No, how hard is it? This is why I think it's an interesting question: how hard is it?  
**Translation:** 

**[7985.40s] English:** It would be great to build a video game like a virtual reality game where it is so real, you'd forget  
**Translation:** 

**[7993.08s] English:** Like ultra-realistic, to where you can't tell the difference, but it's so  
**Translation:** 

**[7998.36s] English:** Nice, that you just want to stay there. You just want to stay there and you  
**Translation:** 

**[8003.16s] English:** Don't want to come back? Do you think that's anything that's doable within our  
**Translation:** Vocabulary: doable: 可行的

**[8008.26s] English:** Lifetime  
**Translation:** 

**[8009.28s] English:** Within our lifetime, probably. Yeah, have you been told they live alone? Does that make  
**Translation:** 

**[8016.46s] English:** You're sad that there will be a population of kids that basically spend  
**Translation:** 

**[8022.78s] English:** Ninety-five percent, ninety-nine percent of their time in a virtual world, very  
**Translation:** 

**[8030.30s] English:** Very hard question to answer for certain people; it might be something that they  
**Translation:** 

**[8036.02s] English:** Really, I derive a lot of value from there. I have a lot of enjoyment in what I love within my life.  
**Translation:** Vocabulary: derive: 获取

**[8038.78s] English:** Enjoyment and like happiness.  
**Translation:** 

**[8040.00s] English:** Out of nowhere, and maybe the real world wasn't giving them that, which is why they did that, so maybe it was just a reaction.  
**Translation:** 

**[8044.46s] English:** Is good for certain people, so ultimately, if it maximizes happiness, right? I think you judge, yeah.  
**Translation:** 

**[8051.00s] English:** I think if it's making people happy, maybe it's okay. Again, I think it's this is a very hard.  
**Translation:** Vocabulary: maximizes: 使最大化

**[8056.22s] English:** Question: Uh, so, like, you've been a part of a lot of amazing papers. What advice would you give?  
**Translation:** 

**[8064.58s] English:** Give them something about what it takes to write a good paper for grad students who are writing papers now.  
**Translation:** 

**[8071.12s] English:** There, um, are there common things that you've learned along the way that you think it takes?  
**Translation:** 

**[8075.42s] English:** Both for a good idea and a good paper, right? So I think I've picked up both of these.  
**Translation:** 

**[8084.34s] English:** Like lots of people I've worked with in the past, so one of them is picking the right problem to.  
**Translation:** 

**[8088.78s] English:** Work on research is as important as finding the solution to it, so  
**Translation:** 

**[8093.94s] English:** You.  
**Translation:** 

**[8094.58s] English:** I mean, there are multiple reasons for this. So, one is that there are certain problems that can  
**Translation:** 

**[8099.24s] English:** Actually, it can be solved within a particular timeframe. So, if you want to work on finding...  
**Translation:** 

**[8104.90s] English:** The meaning of life—this is a great problem. I think most people would agree with that, but do  
**Translation:** Vocabulary: timeframe: 时间框架

**[8110.36s] English:** You believe that your talents and the energy you'll spend on it will make a meaningful difference.  
**Translation:** 

**[8115.38s] English:** Like, make some kind of meaningful progress in your lifetime. If you are optimistic about it, then like,...  
**Translation:** Vocabulary: optimistic: 乐观的

**[8120.56s] English:** Go ahead; that's why I started this podcast. I keep asking people about the meaning of life, and I'm hoping...  
**Translation:** 

**[8124.58s] English:** Not okay, either. That's okay; I'll do it longer because not okay. I hope every opportunity comes.  
**Translation:** 

**[8126.34s] English:** By episode, like 220, I'll figure it out so.  
**Translation:** 

**[8130.74s] English:** Not too many episodes left to go, all right? Maybe today—I don't know—but you're right. So that's uh  
**Translation:** 

**[8137.50s] English:** Seems intractable at the moment, right? So I think it's just the fact that, if you're starting a  
**Translation:** 

**[8142.24s] English:** For example, what is one problem that you want to focus on that you think is interesting?  
**Translation:** Vocabulary: intractable: 难以解决的

**[8147.10s] English:** Enough, uh, and you will be able to make a reasonable amount of headway into it that you think you'll  
**Translation:** 

**[8151.44s] English:** Doing a PhD for so long, in that kind of a time frame.  
**Translation:** Vocabulary: headway: 进展

**[8154.36s] English:** Second part, which is what excites you genuinely.  
**Translation:** 

**[8156.44s] English:** So, you shouldn't just pick problems that you are not excited about because as a  
**Translation:** Vocabulary: excites: 激发兴趣; genuinely: 真正地

**[8160.00s] English:** As a grad student or a researcher, you really need to be passionate about it to continue doing that.  
**Translation:** 

**[8164.48s] English:** Because there are so many other things that you could be doing in life, so you really need to  
**Translation:** Vocabulary: passionate: 热情的

**[8167.62s] English:** Believe in that, to be able to do that for that long in terms of papers, I think the one thing.  
**Translation:** 

**[8172.58s] English:** That I've learned is that in the past, whenever I used to write things, and even now,...  
**Translation:** 

**[8178.22s] English:** Whenever I do that, I try to cram in a lot of things into the paper, whereas what really matters,...  
**Translation:** 

**[8182.58s] English:** Is just pushing one simple idea—that's it; that's all, because that's the paper is going to be like.  
**Translation:** 

**[8189.90s] English:** Whatever, eight or nine pages. If you keep cramming in lots of ideas, it's really hard for the single.  
**Translation:** 

**[8195.88s] English:** Thing that you believe in to stand out, so if you really try to just focus, especially in terms,...  
**Translation:** Vocabulary: cramming: 填塞内容

**[8201.42s] English:** Of writing, really try to focus on one particular idea and articulate it out in multiple different ways.  
**Translation:** 

**[8205.90s] English:** Ways, it's far more valuable to the reader, as well, and basically, to the reader, of course, because  
**Translation:** Vocabulary: articulate: 表达

**[8211.72s] English:** They get to know that this particular idea is associated with this paper, and also for you.  
**Translation:** 

**[8216.82s] English:** Because, uh, you have like when you write about a  
**Translation:** 

**[8219.88s] English:** Idea in different ways, you think about it more deeply. So, as a grad student, I used to always  
**Translation:** 

**[8224.26s] English:** Wait until the last week or so to write the paper, because I used to  
**Translation:** 

**[8229.72s] English:** Always believe that doing the experiments was actually the bigger part of research than writing.  
**Translation:** 

**[8233.70s] English:** And my advisor always told me that you should start writing very early on. And I thought,  
**Translation:** Vocabulary: experiments: 实验

**[8237.08s] English:** Oh, it doesn't matter. I don't know what he's talking about. But I think more and more,  
**Translation:** 

**[8240.74s] English:** I realized that's the case. Like, whenever I write something about what I'm doing, I actually think much more carefully about it.  
**Translation:** 

**[8245.08s] English:** Better about it. And so, if you start writing earlier, early on, you actually, I think,  
**Translation:** 

**[8250.02s] English:** Get better ideas, or at least you figure out like holes in your theory or like particular ones.  
**Translation:** 

**[8254.84s] English:** Experiments that you should run to plug those holes, and so on. Yeah, I'm continually surprised.  
**Translation:** 

**[8260.06s] English:** How many really good papers, throughout history, are quite short and quite simple?  
**Translation:** 

**[8267.90s] English:** And there's a lesson in that. Like, if you want to dream about writing a paper that changes the world,...  
**Translation:** 

**[8273.56s] English:** And you want to go back and forth, you can do it.  
**Translation:** 

**[8275.08s] English:** By example, they're usually simple.  
**Translation:** 

**[8277.98s] English:** Yeah, yeah.  
**Translation:** 

**[8278.94s] English:** And that's...  
**Translation:** 

**[8280.00s] English:** It's not about cramming or focusing on one idea and thinking deeply.  
**Translation:** Vocabulary: cramming: 死记硬背

**[8287.14s] English:** And you're right that the writing process itself reveals the idea.  
**Translation:** 

**[8292.22s] English:** It challenges you to really think about what the idea is that explains it and the thread that ties it all together.  
**Translation:** 

**[8298.66s] English:** And so, a lot of famous researchers I know actually would start off by writing the introduction of the paper, even before the experiments were conducted.  
**Translation:** 

**[8310.00s] English:** With zero experiments, in.  
**Translation:** 

**[8311.88s] English:** Because that at least helps them figure out what they're trying to solve and how it fits into the context of things right now.  
**Translation:** 

**[8318.68s] English:** And that would really guide their entire research.  
**Translation:** 

**[8320.68s] English:** So, a lot of them would actually first write an intro with zero experiments included, and that's how they would start projects.  
**Translation:** 

**[8325.78s] English:** Some basic questions about people, maybe for those who are more like beginners in this field.  
**Translation:** Vocabulary: experiments: 实验; intro: 简介

**[8331.86s] English:** What's the best programming language to learn if you're interested in machine learning?  
**Translation:** 

**[8336.24s] English:** I would say Python, just because it's the easiest one to learn.  
**Translation:** 

**[8340.00s] English:** And a lot of programming in machine learning happens in Python.  
**Translation:** 

**[8345.06s] English:** So, if you don't know any other programming language, Python is actually going to get you a long way.  
**Translation:** 

**[8349.58s] English:** Yeah, it seems like it's a toss-up question because it seems like Python is so much dominating the space now.  
**Translation:** 

**[8356.54s] English:** But I wonder if there's an interesting alternative.  
**Translation:** Vocabulary: dominating: 占据主导

**[8358.50s] English:** Obviously, there's Swift, and there are a lot of interesting alternatives popping up, even JavaScript or R, more so for data science applications.  
**Translation:** 

**[8368.66s] English:** But it seems like Python.  
**Translation:** 

**[8370.00s] English:** Python is more and more being used to teach an introduction to programming at universities.  
**Translation:** 

**[8375.78s] English:** So, it just combines everything very nicely.  
**Translation:** Vocabulary: nicely: 恰当地

**[8379.54s] English:** Even harder question.  
**Translation:** 

**[8381.88s] English:** What are the pros and cons of PyTorch versus TensorFlow?  
**Translation:** 

**[8385.66s] English:** I see.  
**Translation:** 

**[8388.10s] English:** Okay.  
**Translation:** 

**[8388.94s] English:** You can go with no comment.  
**Translation:** 

**[8391.26s] English:** So, as a disclaimer to this, the last time I used TensorFlow was probably about four years ago.  
**Translation:** 

**[8396.42s] English:** And so it was, right when it had come out.  
**Translation:** 

**[8397.88s] English:** Because, so I started.  
**Translation:** 

**[8400.00s] English:** In 2014 or so, we started working on deep learning.  
**Translation:** 

**[8402.66s] English:** And the dominant framework for us then.  
**Translation:** Vocabulary: dominant: 主要的

**[8406.42s] English:** For vision was Cafe, which was out of Berkeley.  
**Translation:** 

**[8409.04s] English:** And we used Cafe a lot; it was really nice.  
**Translation:** Vocabulary: berkeley: 伯克利

**[8412.12s] English:** And then TensorFlow came in.  
**Translation:** 

**[8413.36s] English:** Which was basically like Python, first.  
**Translation:** 

**[8415.10s] English:** So, Cafe was mainly in C++.  
**Translation:** 

**[8417.04s] English:** And it had a very loose, kind of Python binding.  
**Translation:** Vocabulary: binding: 绑定

**[8419.04s] English:** So, Python wasn't really the first language you would use.  
**Translation:** 

**[8421.34s] English:** You would really use either MATLAB or C++.  
**Translation:** 

**[8424.70s] English:** To like get stuff done in the cafe.  
**Translation:** 

**[8428.24s] English:** And then, Python became popular, of course.  
**Translation:** 

**[8429.68s] English:** A little bit later.  
**Translation:** 

**[8430.94s] English:** So, TensorFlow was basically around that time.  
**Translation:** 

**[8432.62s] English:** So, in 2015 and 2016, is when I last used it.  
**Translation:** 

**[8436.12s] English:** It's been a while.  
**Translation:** 

**[8437.20s] English:** And then what? Did you use Torch, or did you?  
**Translation:** 

**[8440.60s] English:** So then I moved to LuaTorch, which was the Torch implementation in Lua.  
**Translation:** Vocabulary: implementation: 实现

**[8444.02s] English:** And then in 2017, I think it was basically pretty much.  
**Translation:** 

**[8446.78s] English:** To PyTorch completely.  
**Translation:** 

**[8448.42s] English:** Oh, interesting! So, you went to Lua? Cool.  
**Translation:** 

**[8450.52s] English:** Yeah.  
**Translation:** 

**[8451.48s] English:** Huh, so you were there before it was cool.  
**Translation:** 

**[8454.20s] English:** Yeah, I mean, LuaTorch was really good.  
**Translation:** 

**[8456.32s] English:** Because it,  
**Translation:** 

**[8458.24s] English:** It actually allowed you to do.  
**Translation:** 

**[8459.24s] English:** A lot of different kinds of things.  
**Translation:** 

**[8461.34s] English:** So, which café was very rigid in terms of its structure?  
**Translation:** 

**[8463.90s] English:** Like you would create a neural network once, and that's it.  
**Translation:** 

**[8466.80s] English:** Whereas, if you wanted very dynamic graphs and so on,  
**Translation:** Vocabulary: graphs: 图表; neural: 神经

**[8469.32s] English:** It was very hard to do that.  
**Translation:** 

**[8470.22s] English:** And LuaTorch was much more friendly for all of these things.  
**Translation:** 

**[8473.56s] English:** Okay, so in terms of PyTorch and TensorFlow,  
**Translation:** 

**[8475.60s] English:** My personal bias is PyTorch.  
**Translation:** 

**[8477.28s] English:** Just because I've been using it longer,...  
**Translation:** 

**[8479.08s] English:** And I'm more familiar with it.  
**Translation:** 

**[8480.78s] English:** And also, PyTorch is much easier to debug.  
**Translation:** 

**[8483.56s] English:** This is what I find because it's imperative, in nature.  
**Translation:** Vocabulary: imperative: 必不可少的

**[8486.30s] English:** Compared to something like TensorFlow, which is not imperative.  
**Translation:** 

**[8488.24s] English:** But that's telling you a lot, that basically.  
**Translation:** 

**[8490.48s] English:** The imperative design is sort of a way,  
**Translation:** 

**[8493.32s] English:** In which a lot of people are taught programming.  
**Translation:** 

**[8495.22s] English:** And that's what actually makes debugging easier for them.  
**Translation:** 

**[8498.14s] English:** So, like, I learned programming in C++.  
**Translation:** 

**[8500.48s] English:** And so, for me, imperative programming is more natural.  
**Translation:** 

**[8504.04s] English:** Do you think it's good to have?  
**Translation:** 

**[8505.28s] English:** Of these two communities, is this kind of competition?  
**Translation:** 

**[8508.48s] English:** I think PyTorch is kind of becoming more and more dominant.  
**Translation:** Vocabulary: dominant: 占据优势

**[8511.50s] English:** In the research community,  
**Translation:** 

**[8512.50s] English:** But TensorFlow is still very popular.  
**Translation:** 

**[8514.58s] English:** In the more sort of application-oriented machine learning community.  
**Translation:** 

**[8517.90s] English:** So, do you think it's good to have that kind  
**Translation:** 

**[8520.00s] English:** Split in code bases, or, um, so like the benefit there is that the competition challenges the library.  
**Translation:** 

**[8527.10s] English:** Developers to step up their game, yeah, but the downside is that there are these code bases, uh, that are  
**Translation:** Vocabulary: downside: 缺点

**[8533.22s] English:** In different libraries, right? So I think the downside is that, for a lot of research,  
**Translation:** 

**[8538.22s] English:** Code that's released in one framework, and if you're using the other one, it's really hard.  
**Translation:** 

**[8541.20s] English:** To really build on top of it, but thankfully, the open-source community in machine learning is  
**Translation:** 

**[8546.46s] English:** Amazing, so yeah, whenever something pops up in TensorFlow, you wait a few days and someone  
**Translation:** 

**[8552.12s] English:** Who's like super sharp will actually come and translate that particular code base into PyTorch.  
**Translation:** 

**[8556.08s] English:** And it will basically have figured that all those nooks and crannies out, so the open-source.  
**Translation:** Vocabulary: crannies: 角落; nooks: 角落

**[8560.72s] English:** The community is amazing, and they really like to figure out this gap. So, I think in terms of like,  
**Translation:** 

**[8566.38s] English:** Having these two frameworks, or multiple ones, I think — of course, there are different use cases, so there  
**Translation:** 

**[8570.00s] English:** Are there going to be benefits to using one or the other framework? And, as you said, I think competition is good.  
**Translation:** 

**[8574.18s] English:** Just healthy, because both of them are going to have a lot of benefits from using one or the other.  
**Translation:** 

**[8576.44s] English:** So, I think it's really important to have a lot of these frameworks or, you know, all of these.  
**Translation:** 

**[8578.44s] English:** Frameworks really sort of keep learning from each other and keep incorporating different things to.  
**Translation:** Vocabulary: incorporating: 吸收

**[8581.80s] English:** Just make them better and better. What advice would you have for someone new to machine learning?  
**Translation:** 

**[8588.44s] English:** You know, uh, maybe just started or haven't even started but are curious about it, and who want  
**Translation:** 

**[8593.16s] English:** To get in the field, don't be afraid to get your hands dirty — I think that's the main thing. So if  
**Translation:** 

**[8597.72s] English:** Something doesn't work. Like, really drill into why things aren't working. Can you elaborate?  
**Translation:** Vocabulary: elaborate: 详细说明

**[8603.08s] English:** What "your hands are dirty" means, right? So, for example,  
**Translation:** 

**[8606.20s] English:** Like, if you want to get your hands dirty, you can get your hands dirty.  
**Translation:** 

**[8606.36s] English:** Like, if you want to get your hands dirty, you can get your hands dirty.  
**Translation:** 

**[8606.42s] English:** Like, if an algorithm isn't converging when you're trying to train the network, whatever.  
**Translation:** Vocabulary: algorithm: 算法; converging: 收敛

**[8610.26s] English:** Than trying to Google the answer or trying to do something like really spend those 5, 8, 10  
**Translation:** 

**[8615.54s] English:** 15, 20, however many hours, really trying to figure it out yourself, because in that process,...  
**Translation:** 

**[8619.78s] English:** You'll actually learn a lot more, yeah. Uh, googling is, of course, like a good way to solve it when you  
**Translation:** 

**[8624.74s] English:** Need a quick answer, but I think initially, especially like when you're starting out.  
**Translation:** Vocabulary: googling: google搜索

**[8628.18s] English:** It's much nicer to figure things out by yourself, and I just say that from experience.  
**Translation:** 

**[8632.82s] English:** Because, like, when I started out, there weren't a lot of resources, so we would have to rely on each other a lot.  
**Translation:** 

**[8636.34s] English:** The lab — a lot of us liked it, as we would look up to senior students.  
**Translation:** 

**[8640.00s] English:** And the senior students were, of course, busy.  
**Translation:** 

**[8641.40s] English:** And they would be like, "Hey, why don't you go figure it out?  
**Translation:** 

**[8643.08s] English:** Because I just don't have the time.  
**Translation:** 

**[8644.32s] English:** I'm working on my dissertation, or whatever.  
**Translation:** 

**[8646.42s] English:** I'll find other PhD students.  
**Translation:** Vocabulary: dissertation: 论文

**[8647.70s] English:** And so, then we would sit down and just try to figure it out.  
**Translation:** 

**[8650.46s] English:** And that, I think, really helped me.  
**Translation:** 

**[8652.40s] English:** That has really helped me figure a lot of things out.  
**Translation:** 

**[8654.78s] English:** I think, in general, if I were to generalize that,  
**Translation:** Vocabulary: generalize: 概括

**[8658.64s] English:** I feel like persevering through any kind of struggle.  
**Translation:** 

**[8661.92s] English:** On a thing you care about is good.  
**Translation:** Vocabulary: persevering: 坚持不懈

**[8665.32s] English:** So, you're basically trying to make it seem like it's good to,...  
**Translation:** 

**[8668.66s] English:** You know, spend time debugging.  
**Translation:** 

**[8670.76s] English:** But really, any kind of struggle, whatever form it takes.  
**Translation:** 

**[8673.64s] English:** It could be just googling a lot.  
**Translation:** 

**[8676.06s] English:** Just basically anything; just sticking with it.  
**Translation:** 

**[8678.68s] English:** And going through the hard thing.  
**Translation:** Vocabulary: sticking: 坚持

**[8679.84s] English:** That could take the form of implementing stuff from scratch.  
**Translation:** 

**[8683.16s] English:** It could take the form of re-implementing.  
**Translation:** Vocabulary: implementing: 执行; scratch: 从头开始

**[8685.58s] English:** With different libraries or different programming languages.  
**Translation:** 

**[8689.02s] English:** It could take a lot of different forms.  
**Translation:** 

**[8690.62s] English:** But struggle is good for the soul.  
**Translation:** 

**[8693.50s] English:** So, like in Pittsburgh, where I did my PhD,  
**Translation:** 

**[8695.86s] English:** The thing was, it used to snow a lot.  
**Translation:** 

**[8697.26s] English:** Yeah.  
**Translation:** 

**[8698.04s] English:** And so.  
**Translation:** 

**[8698.76s] English:** When it was snowy, you really couldn't do much.  
**Translation:** 

**[8700.96s] English:** So, the thing that a lot of people said is that snow builds character.  
**Translation:** 

**[8705.14s] English:** Because when it's snowing, you can't do anything else.  
**Translation:** 

**[8707.44s] English:** You focus on work.  
**Translation:** 

**[8709.10s] English:** Do you have any general advice for people?  
**Translation:** 

**[8710.86s] English:** You've already been exceptionally successful.  
**Translation:** 

**[8712.62s] English:** You're young.  
**Translation:** Vocabulary: exceptionally: 特别地

**[8713.42s] English:** But, do you have any advice for young people starting out in college?  
**Translation:** 

**[8716.18s] English:** Or maybe in high school?  
**Translation:** 

**[8717.84s] English:** You know, advice for their career, and advice for their life.  
**Translation:** 

**[8721.08s] English:** How to pave a successful path in career and life?  
**Translation:** 

**[8725.64s] English:** I would say, just be hungry.  
**Translation:** 

**[8727.18s] English:** Like always, be hungry.  
**Translation:** 

**[8728.36s] English:** Be hungry for what you want.  
**Translation:** 

**[8729.58s] English:** And I think I've been inspired by a lot of people who are just driven.  
**Translation:** 

**[8734.36s] English:** And who really like go for what they want, no matter what.  
**Translation:** 

**[8737.60s] English:** Like, you shouldn't want it.  
**Translation:** 

**[8739.36s] English:** You should need it.  
**Translation:** 

**[8740.40s] English:** So, if you need something, you basically go to the ends to make it work.  
**Translation:** 

**[8744.28s] English:** How do you know when you come across something that's like you need?  
**Translation:** 

**[8751.04s] English:** I think there's not going to be any single thing that you'll need.  
**Translation:** 

**[8753.66s] English:** There are going to be different types of things that you need.  
**Translation:** 

**[8755.28s] English:** But whenever you need something, you just go and push for it.  
**Translation:** 

**[8757.58s] English:** And of course, once you may not get it,  
**Translation:** 

**[8760.00s] English:** Or, you may find that this was not even the thing you were looking for; it might be something different.  
**Translation:** 

**[8763.38s] English:** Thing, but the point is, like, you're pushing through things, and that actually gives you  
**Translation:** 

**[8767.36s] English:** Brings a lot of skills and brings a lot of, uh, like building a certain kind of attitude which will  
**Translation:** 

**[8773.14s] English:** Probably help you get the other thing once you figure out what's really the thing that you want.  
**Translation:** 

**[8777.84s] English:** Yeah, I think a lot of people are kind of afraid of that, because one, it's a fear.  
**Translation:** 

**[8783.62s] English:** Of commitment, and two: there are so many amazing things in this world that you almost don't want to  
**Translation:** 

**[8787.66s] English:** Miss out on all the other amazing things by committing to this one thing, so I think a lot.  
**Translation:** 

**[8791.72s] English:** Of it has to do with just allowing yourself to, uh, like notice that thing and just go all the way.  
**Translation:** 

**[8800.58s] English:** With it, I mean, I also like failure, right? So, yeah, I know this is like super cheesy that you know.  
**Translation:** Vocabulary: cheesy: 俗气的

**[8806.80s] English:** Failure is something that you should be prepared for, and so on, but I do think—I mean, especially.  
**Translation:** 

**[8811.92s] English:** In research, for example, failure is something that happens almost every day.  
**Translation:** 

**[8816.74s] English:** Experimental.  
**Translation:** 

**[8817.66s] English:** Failing and not working, and so you really need to be so used to it that you need to have a thick skin.  
**Translation:** 

**[8823.24s] English:** But, and only through basically getting through it, is when you find the one thing that's  
**Translation:** 

**[8828.46s] English:** Actually, working like Thomas Edison was like having one person do it all, right? So I really like when I was  
**Translation:** Vocabulary: edison: 爱迪生

**[8833.42s] English:** A kid; I used to really read about how he uh found the filament for the light bulb, and then  
**Translation:** 

**[8839.02s] English:** He, I think, was like he tried 990 things that didn't work or something of the sort, yeah.  
**Translation:** Vocabulary: filament: 灯丝

**[8844.50s] English:** Then they asked him, "Like, so, what did you learn? Uh, because all of these...  
**Translation:** 

**[8847.66s] English:** Are failed experiments, and then he says, "Oh, these 990 things don't work," and I know that. Did you know?  
**Translation:** 

**[8852.60s] English:** That I mean, that's really inspiring. Uh, so you've spent a few years on this earth performing a  
**Translation:** 

**[8859.14s] English:** Self-supervised, um, is a kind of learning process. Have you figured out the meaning of life yet?  
**Translation:** 

**[8865.58s] English:** I told you I'm doing this podcast to try to get the answer. I'm hoping you could tell me what it is.  
**Translation:** 

**[8870.96s] English:** You think the meaning of it all is, uh? I don't think I figured that out. No, I have no idea.  
**Translation:** 

**[8877.66s] English:** Uh, do you think, uh  
**Translation:** 

**[8880.00s] English:** Do you think AI will help us figure it out?  
**Translation:** 

**[8882.50s] English:** Do you think there's no answer?  
**Translation:** 

**[8883.86s] English:** The whole point is to keep searching.  
**Translation:** 

**[8885.50s] English:** I think it's an endless sort of quest for us.  
**Translation:** 

**[8888.80s] English:** I don't think AI will help us there.  
**Translation:** 

**[8890.56s] English:** This is like a very hard, hard, hard question.  
**Translation:** 

**[8893.50s] English:** Which has so many humans tried to answer.  
**Translation:** 

**[8895.40s] English:** Well, that's the interesting thing about the difference between AI and humans.  
**Translation:** 

**[8899.44s] English:** Humans don't seem to know what the hell they're doing.  
**Translation:** 

**[8901.30s] English:** And AI is almost always operating under well-defined objective functions.  
**Translation:** 

**[8907.12s] English:** And I wonder whether our lack of ability,  
**Translation:** 

**[8913.54s] English:** To define good long-term objective functions.  
**Translation:** 

**[8917.10s] English:** Or introspect what the objective function under which we operate is.  
**Translation:** Vocabulary: introspect: 自我反思

**[8921.94s] English:** If that's a feature, or a bug.  
**Translation:** 

**[8924.30s] English:** I would say it's a feature.  
**Translation:** 

**[8925.10s] English:** Because then, everyone actually has very different kinds of objective functions.  
**Translation:** 

**[8928.28s] English:** That they're optimizing.  
**Translation:** Vocabulary: optimizing: 最大化

**[8929.12s] English:** And those objective functions evolve and change dramatically.  
**Translation:** 

**[8932.54s] English:** Through the course of their life.  
**Translation:** Vocabulary: evolve: 演变

**[8933.90s] English:** That's actually what makes us interesting, right?  
**Translation:** 

**[8936.36s] English:** Otherwise,  
**Translation:** 

**[8937.12s] English:** If everyone was doing the exact same thing,  
**Translation:** 

**[8939.10s] English:** That would be pretty boring.  
**Translation:** 

**[8940.46s] English:** We do want people with different kinds of perspectives.  
**Translation:** 

**[8943.80s] English:** Also, people evolve continuously.  
**Translation:** Vocabulary: perspectives: 观点

**[8946.24s] English:** That's, I would say, the biggest feature of being human.  
**Translation:** 

**[8949.30s] English:** And then we get to the ones that die.  
**Translation:** 

**[8951.08s] English:** Because they do something stupid.  
**Translation:** 

**[8952.52s] English:** We get to watch that, see it, and learn from it.  
**Translation:** 

**[8955.54s] English:** And as a species,  
**Translation:** 

**[8957.74s] English:** We take that lesson and become better and better.  
**Translation:** 

**[8961.84s] English:** Because of all the dumb people in the world.  
**Translation:** 

**[8964.22s] English:** That died doing something wild.  
**Translation:** 

**[8967.12s] English:** And beautiful.  
**Translation:** 

**[8969.06s] English:** Ishan, thank you so much for this incredible conversation.  
**Translation:** 

**[8971.76s] English:** We did a depth-first search.  
**Translation:** 

**[8973.98s] English:** Through the space of machine learning,  
**Translation:** 

**[8977.80s] English:** And it was fun and fascinating.  
**Translation:** 

**[8981.70s] English:** So, it's really an honor to meet you.  
**Translation:** 

**[8983.94s] English:** And it was a really awesome conversation.  
**Translation:** 

**[8985.78s] English:** Thanks for coming down today and talking with me.  
**Translation:** 

**[8988.00s] English:** Thanks, Lex.  
**Translation:** 

**[8988.60s] English:** I mean, I've listened to you.  
**Translation:** 

**[8990.24s] English:** I told you it was unreal for me to actually meet you in person.  
**Translation:** 

**[8992.94s] English:** And I'm so happy to be here.  
**Translation:** 

**[8994.12s] English:** Thank you.  
**Translation:** 

**[8994.96s] English:** Thanks, man.  
**Translation:** 

**[8996.46s] English:** Thanks for listening.  
**Translation:** 

**[8997.00s] English:** Thanks for listening.  
**Translation:** 

**[8997.12s] English:** Thanks for listening to this conversation with Ishan Mizra.  
**Translation:** 

**[8999.34s] English:** And thank you to...  
**Translation:** 

**[9000.00s] English:** On it, the information about Grammarly and Athletic Greens. Check them out in the description to  
**Translation:** 

**[9006.88s] English:** Support this podcast. And now, let me leave you with some words from Arthur C. Clarke.  
**Translation:** Vocabulary: grammarly: 语法检查软件

**[9012.48s] English:** Any sufficiently advanced technology is indistinguishable from magic.  
**Translation:** 

**[9017.84s] English:** Thank you for listening, and I hope to see you next time.  
**Translation:** Vocabulary: sufficiently: 足够地


<!-- TRANSCRIPTION_COMPLETE -->
