# Podcast vocabulary notes
Source file: Lex Fridman - Ishan Misra： Self-Supervised Deep Learning in Computer Vision ｜ Lex Fridman Podcast #206.opus

**[0.00s] English:** The following is a conversation with Ishan Mizra, research scientist at Facebook AI Research,  
**Translation:** 

**[5.94s] English:** who works on self-supervised machine learning in the domain of computer vision, or in other words,  
**Translation:** 

**[12.16s] English:** making AI systems understand the visual world with minimal help from us humans. Transformers  
**Translation:** 

**[18.92s] English:** and self-attention has been successfully used by OpenAI's GPT-3 and other language models to do  
**Translation:** 

**[25.94s] English:** self-supervised learning in the domain of language. Ishan, together with Jan LeCun and others,  
**Translation:** 

**[31.76s] English:** is trying to achieve the same success in the domain of images and video. The goal is to leave  
**Translation:** 

**[37.76s] English:** a robot watching YouTube videos all night and in the morning come back to a much smarter robot.  
**Translation:** 

**[43.56s] English:** I read the blog post, Self-Supervised Learning, the Dark Matter of Intelligence by Ishan and Jan  
**Translation:** 

**[49.40s] English:** LeCun, and then listened to Ishan's appearance on the excellent Machine Learning Street Talk  
**Translation:** 

**[55.92s] English:** podcast, and I knew I had to talk to him. By the way, if you're interested in machine learning  
**Translation:** 

**[61.42s] English:** and AI, I cannot recommend the ML Street Talk podcast highly enough. Those guys are great.  
**Translation:** 

**[69.50s] English:** Quick mention of our sponsors. Onnit, The Information, Grammarly, and Athletic Greens.  
**Translation:** Vocabulary: grammarly: 语法大师; sponsors: 赞助商

**[75.12s] English:** Check them out in the description to support this podcast. As a side note, let me say that for those  
**Translation:** 

**[80.84s] English:** of you who may have been listening for quite a while, this podcast used to be called Artificial  
**Translation:** 

**[85.40s] English:** Intelligence.  
**Translation:** 

**[85.92s] English:** Because my life passion has always been, will always be, artificial intelligence,  
**Translation:** 

**[92.62s] English:** both narrowly and broadly defined. My goal with this podcast is still to have many conversations  
**Translation:** 

**[98.92s] English:** with world-class researchers in AI, math, physics, biology, and all the other sciences.  
**Translation:** Vocabulary: narrowly: 范围狭义

**[104.96s] English:** But I also want to talk to historians, musicians, athletes, and of course, occasionally comedians.  
**Translation:** 

**[111.18s] English:** In fact, I'm trying out doing this podcast three times a week now to give me more,  
**Translation:** 

**[115.92s] English:** freedom with guest selection, and maybe get a chance to have a bit more.  
**Translation:** 

**[120.00s] English:** fun. Speaking of fun, in this conversation, I challenge the listener to count the number of  
**Translation:** 

**[125.04s] English:** times the word banana is mentioned. Ishan and I use the word banana as the canonical example  
**Translation:** 

**[132.12s] English:** at the core of the hard problem of computer vision and, maybe, the hard problem of consciousness.  
**Translation:** Vocabulary: canonical: 标准例证

**[139.56s] English:** This is the Lex Friedman Podcast, and here is my conversation with Ishan Mizra.  
**Translation:** 

**[146.02s] English:** What is self-supervised learning? And, maybe, even give the bigger basics of what is supervised  
**Translation:** Vocabulary: supervised: 监督学习

**[153.66s] English:** and semi-supervised learning. And, maybe, why is self-supervised learning a better term than  
**Translation:** 

**[158.40s] English:** unsupervised learning? Let's start with supervised learning. So, typically, for machine learning  
**Translation:** Vocabulary: unsupervised: 无监督

**[163.22s] English:** systems, the way they're trained is you get a bunch of humans. The humans point out particular  
**Translation:** 

**[168.06s] English:** concepts. So, if it's in the case of images, you want the humans to come and tell you what is  
**Translation:** 

**[172.30s] English:** present in the image, draw boxes around them,  
**Translation:** 

**[176.02s] English:** masks of, like, things, pixels, which are of particular categories or not. For NLP, again,  
**Translation:** Vocabulary: pixels: 像素

**[181.38s] English:** there are, like, lots of these particular tasks, say, about sentiment analysis, about entailment,  
**Translation:** 

**[185.52s] English:** and so on. So, typically, for supervised learning, we get a big corpus of such annotated or labeled  
**Translation:** Vocabulary: annotated: 标注好的; entailment: 蕴含; sentiment: 情感分析

**[190.46s] English:** data, and then we feed that to a system, and the system is really trying to mimic. So, it's taking  
**Translation:** 

**[195.44s] English:** this input of the data and then trying to mimic the output. So, it looks at an image, and the  
**Translation:** 

**[199.90s] English:** human has tagged that this image contains a banana, and now the system is basically trying  
**Translation:** 

**[204.02s] English:** to mimic that. So, that's its learning signal.  
**Translation:** 

**[206.02s] English:** And so, for supervised learning, we try to gather lots of such data, and we train these  
**Translation:** 

**[210.80s] English:** machine learning models to imitate the input or output. And the hope is, basically, by  
**Translation:** 

**[214.66s] English:** doing so, now on unseen or, like, new kinds of data, this model can automatically learn  
**Translation:** 

**[219.94s] English:** to predict these concepts. So, this is a standard sort of supervised setting. For semi-supervised  
**Translation:** 

**[224.90s] English:** setting, the idea typically is that you have, of course, all of the supervised data, but  
**Translation:** 

**[229.44s] English:** you have lots of other data which is unsupervised or which is, like, not labeled. Now, the problem,  
**Translation:** 

**[234.14s] English:** basically, with supervised learning and why you actually have to do this is that you have,  
**Translation:** 

**[236.02s] English:** obviously, all of these alternate sort of learning paradigms as supervised learning  
**Translation:** Vocabulary: paradigms: 学习范式

**[240.00s] English:** does just does not scale so if you look at for computer vision the sort of largest one of the  
**Translation:** 

**[245.20s] English:** most popular data sets is image net right so the entire image net data set has about 22 000 concepts  
**Translation:** 

**[251.60s] English:** and about 14 million images so these concepts are basically just nouns and they're annotated  
**Translation:** 

**[256.72s] English:** on images and this entire data set was a mammoth data collection effort it actually  
**Translation:** Vocabulary: mammoth: 巨大的

**[261.68s] English:** gave rise to a lot of powerful learning algorithms is credited with like sort of the rise of deep  
**Translation:** 

**[265.76s] English:** learning as well but this data set took about 22 human years to collect to annotate and it's  
**Translation:** 

**[272.00s] English:** not even that many concepts right it's not even that many images 14 million is nothing really  
**Translation:** 

**[276.64s] English:** like you have about i think 400 million images or so or even more than that uploaded to  
**Translation:** 

**[280.96s] English:** most of the popular sort of social media websites today so now supervised learning just doesn't  
**Translation:** 

**[285.92s] English:** scale if i want to now annotate more concepts if i want to have this various types of fine  
**Translation:** Vocabulary: annotate: 标注; supervised: 监督

**[290.32s] English:** grain concepts then it won't really scale so now you come up to these sort of different learning  
**Translation:** 

**[294.96s] English:** paradigms first  
**Translation:** 

**[295.76s] English:** example semi-supervised learning where the idea is of course you have this annotated corpus of  
**Translation:** 

**[300.00s] English:** supervised data and you have lots of these unlabeled images and the idea is that the  
**Translation:** Vocabulary: unlabeled: 未标注的

**[304.48s] English:** algorithm should basically try to measure some kind of consistency or really try to measure  
**Translation:** 

**[308.72s] English:** some kind of signal on this sort of unlabeled data to make itself more confident about what  
**Translation:** Vocabulary: algorithm: 算法

**[314.56s] English:** it's really trying to predict so by access to this lots of unlabeled data the idea is that the  
**Translation:** 

**[321.12s] English:** algorithm actually learns to be more confident and actually gets better at predicting these concepts  
**Translation:** 

**[326.72s] English:** and now we come to the other extreme which is like self-supervised learning  
**Translation:** 

**[330.32s] English:** the idea basically is that the machine or the algorithm should really discover  
**Translation:** 

**[334.16s] English:** concepts or discover things about the world or learn representations about the  
**Translation:** 

**[337.76s] English:** world which are useful without access to explicit human supervision so the word  
**Translation:** 

**[342.16s] English:** supervision is still in the term self-supervised so what is the supervision signal and maybe  
**Translation:** 

**[349.36s] English:** that perhaps is when yan macun and you argue that unsupervised is the incorrect terminology here so  
**Translation:** Vocabulary: supervision: 监督信号; terminology: 术语; unsupervised: 无监督

**[355.12s] English:** what is the supervision signal when the humans aren't part of the picture or not  
**Translation:** 

**[360.00s] English:** a big part of the picture right so self-supervised the reason it has the term supervised in itself is  
**Translation:** 

**[366.96s] English:** because you're using the data itself as supervision so because the data serves as its  
**Translation:** 

**[372.02s] English:** own source of supervision it's self-supervised in that way now the reason a lot of people i mean  
**Translation:** 

**[376.64s] English:** we did it in that blog post with yan but a lot of other people have also argued for using this  
**Translation:** 

**[380.70s] English:** term self-supervised so starting from like 94 from virginia desas group uh i think ucsd and  
**Translation:** 

**[386.90s] English:** now she's at ucsd uh jeetendra malik has said this a bunch of times as well so you have supervised  
**Translation:** 

**[392.48s] English:** and then unsupervised basically means everything which is not supervised but that includes stuff  
**Translation:** Vocabulary: jeetendra: 杰特伦德拉; malik: 马利克

**[397.54s] English:** like semi-supervised that includes other like transductive learning lots of other sort of  
**Translation:** 

**[402.04s] English:** settings so that's the reason like now people are preferring this term self-supervised because  
**Translation:** Vocabulary: transductive: 推断性学习

**[407.22s] English:** it explicitly says what's happening the data itself is the source of supervision and any sort  
**Translation:** 

**[412.20s] English:** of learning algorithm which tries to extract just sort of data supervision signals  
**Translation:** Vocabulary: explicitly: 明确地

**[416.88s] English:** from the data itself is a self-supervised algorithm but there is within the data a set of tricks which  
**Translation:** 

**[423.40s] English:** unlock the supervision right so can you give maybe some examples and there's a there's innovation  
**Translation:** 

**[430.08s] English:** ingenuity required to unlock that supervision the data doesn't just speak to you some ground truth  
**Translation:** 

**[435.50s] English:** you have to do some kind of trick uh so i don't know what your favorite domain is so you specifically  
**Translation:** Vocabulary: ingenuity: 巧妙方法

**[440.40s] English:** specialize in visual learning but is there favorite examples maybe in language or other domains  
**Translation:** 

**[446.28s] English:** perhaps  
**Translation:** Vocabulary: specialize: 专注于

**[446.88s] English:** the most successful applications have been in nlp not language processing so the idea basically  
**Translation:** 

**[451.96s] English:** being that you can train models that can you have a sentence and you mask out certain words  
**Translation:** 

**[457.00s] English:** and now these models learn to predict the masked out words so if you have like the cat jumped over  
**Translation:** 

**[462.66s] English:** the dog so you can basically mask out cat and now you are essentially asking the model to predict  
**Translation:** 

**[467.76s] English:** what was missing what did i mask out so the model is going to predict basically a distribution over  
**Translation:** 

**[473.34s] English:** all the possible words that it knows and probably it has like a lot of information about the language  
**Translation:** 

**[476.88s] English:** like if it's a well-trained model it has a sort of higher problem  
**Translation:** 

**[480.00s] English:** density for this word cat for vision i would say the sort of more uh i mean the easier example  
**Translation:** Vocabulary: density: 问题密度

**[487.34s] English:** which is not as widely used these days is basically say for example video prediction  
**Translation:** 

**[491.52s] English:** so video is again a sequence of things so you can ask the model so if you have a video of say 10  
**Translation:** 

**[496.56s] English:** seconds you can feed in the first nine seconds to a model and then ask it hey what happens  
**Translation:** 

**[501.16s] English:** basically in the 10 second can you predict what's going to happen and the idea basically is because  
**Translation:** 

**[506.12s] English:** the model is predicting something about the data itself of course you didn't didn't need any human  
**Translation:** 

**[511.26s] English:** to tell you what was happening because the 10 second video was naturally captured because the  
**Translation:** 

**[515.08s] English:** model is predicting what's happening there it's going to automatically learn something about the  
**Translation:** 

**[519.28s] English:** structure of the world how objects move object permanence and these kinds of things uh so like  
**Translation:** Vocabulary: permanence: 持久性

**[524.30s] English:** if i have something at the edge of the table it will fall down things like these which you really  
**Translation:** 

**[528.58s] English:** don't have to sit and annotate in a supervised learning setting i would have to sit and annotate  
**Translation:** Vocabulary: annotate: 标注; supervised: 监督

**[532.20s] English:** this is a cup now i move this cup this is still a cup and now i move this cup it's  
**Translation:** 

**[536.10s] English:** still a cup and then it falls down and this is a fallen down cup so i won't have to annotate all  
**Translation:** 

**[539.78s] English:** of these things in a self-supervised setting isn't that kind of a brilliant little trick  
**Translation:** 

**[544.34s] English:** of taking a series of data that is consistent and removing one element in that series and then uh  
**Translation:** 

**[552.78s] English:** teaching the algorithm to predict that element isn't that first of all that's quite brilliant  
**Translation:** 

**[559.20s] English:** um it seems to be applicable in anything that has the constraint of being  
**Translation:** Vocabulary: algorithm: 算法; constraint: 约束

**[566.00s] English:** unbiased and unbiased and unbiased and unbiased and unbiased and unbiased and unbiased and  
**Translation:** 

**[566.08s] English:** unbiased and unbiased and unbiased and unbiased uh a sequence that is consistent with the physical  
**Translation:** Vocabulary: unbiased: 公正无私

**[569.28s] English:** reality um the question is are there other tricks like this that can generate the uh  
**Translation:** 

**[576.08s] English:** self-supervision signal so sequence is possibly the most widely used one in nlp  
**Translation:** 

**[581.12s] English:** for vision the one that is actually used for like images which is very popular these days  
**Translation:** 

**[585.76s] English:** is basically taking an image and now taking different crops of that image so you can  
**Translation:** 

**[590.32s] English:** basically decide to crop say the top left corner and you crop say the bottom right corner and  
**Translation:** 

**[595.28s] English:** you can basically decide to crop say the top left corner and you crop say the bottom right corner and asking a network  
**Translation:** 

**[595.98s] English:** asking a network to basically uh present it with a choice saying that okay  
**Translation:** 

**[600.00s] English:** you have this image you have this image are these the same or not and so the idea basically is that  
**Translation:** 

**[605.60s] English:** because different like in an image different parts of the image are going to be related  
**Translation:** 

**[609.68s] English:** so for example if you have a chair and a table basically these things are going to be close by  
**Translation:** 

**[614.88s] English:** versus if you take again if you have like a zoomed in picture of a chair if you're taking different  
**Translation:** 

**[620.08s] English:** crops it's going to be different parts of the chair so the idea basically is that different  
**Translation:** 

**[624.48s] English:** crops of the image are related and so the features or the representations that you get from these  
**Translation:** 

**[628.40s] English:** different crops should also be related so this is possibly the most like widely used trick these  
**Translation:** 

**[632.80s] English:** days for self-supervised learning in computer vision so again using the uh consistency that's  
**Translation:** 

**[638.48s] English:** inherent to physical reality in in visual domain that's you know parts of an image are consistent  
**Translation:** 

**[645.52s] English:** and then in the uh language domain or anything that has sequences like language or something  
**Translation:** 

**[651.44s] English:** that's like a time series then you can chop up parts in time it's similar to the story of uh  
**Translation:** 

**[657.36s] English:** rnns and  
**Translation:** 

**[658.40s] English:** cnn's of rnns and covenants you and jan lacoon wrote the blog post in march 2021 titled  
**Translation:** Vocabulary: covenants: 契约

**[667.52s] English:** self-supervised learning the dark matter of intelligence can you summarize this blog  
**Translation:** 

**[672.16s] English:** post and maybe explain the main idea or set of ideas the blog post was mainly about sort of  
**Translation:** 

**[677.68s] English:** just telling i mean this is really a uh accepted fact i would say for a lot of people now that  
**Translation:** 

**[682.96s] English:** self-supervised learning is something that is going to be a play an important role for machine  
**Translation:** 

**[687.44s] English:** learning algorithms that are going to play an important role for machine learning algorithms that  
**Translation:** 

**[688.32s] English:** come in the future and even now well let me just comment that uh we don't yet have a good  
**Translation:** 

**[694.24s] English:** understanding what dark matter is that's true so the idea the metaphor doesn't exactly transfer  
**Translation:** 

**[701.76s] English:** but maybe maybe it's actually perfectly transfers that we don't know wherever we have an inkling  
**Translation:** Vocabulary: inkling: 模糊概念; metaphor: 比喻; transfers: 转移

**[707.76s] English:** that it'll be a big part of whatever solving intelligence looks like right so i think self  
**Translation:** 

**[712.24s] English:** super obviously i think the way it's done right now is i would say like the first step towards  
**Translation:** 

**[716.48s] English:** what it probably should end up Pun broom and his work ass is probably should end up like learning  
**Translation:** 

**[718.32s] English:** or what it should enable us to do.  
**Translation:** 

**[720.00s] English:** yeah so the idea for that particular piece was self-supervised learning is going to be a very  
**Translation:** 

**[725.58s] English:** powerful way to learn common sense about the world or like stuff that is really hard to label  
**Translation:** 

**[730.18s] English:** for example like is this piece over here heavier than the cup now for all these kinds of things  
**Translation:** 

**[737.44s] English:** you'll have to sit and label these things so supervised learning is clearly not going to scale  
**Translation:** 

**[740.78s] English:** so what is the thing that's actually going to scale it's probably going to be an agent that  
**Translation:** 

**[745.14s] English:** can either actually interact with it to lift it up or observe me doing it so if i'm basically  
**Translation:** 

**[750.64s] English:** lifting these things up it can probably reason about hey this is taking him more time to lift up  
**Translation:** 

**[754.48s] English:** or the velocity is different whereas the velocity for this is different probably this one is heavier  
**Translation:** 

**[758.90s] English:** so essentially by observations of the data you should be able to infer a lot of things about  
**Translation:** 

**[764.36s] English:** the world without someone explicitly telling you this is heavy this is not this is something that  
**Translation:** 

**[769.40s] English:** can pour this is something that cannot pour this is somewhere that you can sit this is not somewhere  
**Translation:** 

**[773.04s] English:** that you can sit but you just mentioned  
**Translation:** 

**[774.96s] English:** you just mentioned that  
**Translation:** 

**[775.14s] English:** ability to interact with the world there's so many questions that are yet to be that are still  
**Translation:** 

**[781.74s] English:** open which is how do you select a set of data over which the self-supervised uh learning process  
**Translation:** 

**[787.66s] English:** works how much interactivity like in the active learning or the machine teaching context is there  
**Translation:** 

**[793.84s] English:** what are the reward signals like how much actual interaction there is with the physical world  
**Translation:** 

**[799.58s] English:** that kind of thing uh so that that's a that could be a huge question and then  
**Translation:** 

**[804.96s] English:** on top of that there's a lot of questions about how do you select a set of data over which the  
**Translation:** 

**[805.12s] English:** self-supervised learning process works how much interactivity like in the active learning or the  
**Translation:** 

**[805.14s] English:** on top of that there's a lot of questions about how do you select a set of data over which the  
**Translation:** 

**[805.64s] English:** self-supervised learning process works how much interactivity like in the active learning or the  
**Translation:** 

**[806.14s] English:** top of that which i have a million questions about which we don't know the answers to but it's worth  
**Translation:** 

**[811.34s] English:** talking about is how much reasoning is involved how much accumulation of knowledge versus something  
**Translation:** Vocabulary: accumulation: 累积知识

**[819.10s] English:** that's more akin to learning or whether that's the the same thing but so we're like it is truly  
**Translation:** 

**[825.66s] English:** dark matter we don't know how exactly to do it yeah but we are i mean a lot of us are actually  
**Translation:** 

**[831.50s] English:** convinced that it's going to be a sort of major thing in machine learning so let me know in the  
**Translation:** 

**[835.12s] English:** let me reframe it then that human supervision cannot be  
**Translation:** Vocabulary: cannot: 不能; reframe: 重新表述; supervision: 监督

**[840.00s] English:** at large scale the source of the solution to intelligence right so there has we the machines  
**Translation:** 

**[845.84s] English:** have to discover the supervision in the natural signal of the world right i mean the other thing  
**Translation:** 

**[850.96s] English:** is also that humans are not particularly good labelers they're not very consistent  
**Translation:** 

**[855.60s] English:** uh for example like what's the difference between a dining table and a table is it just the fact  
**Translation:** Vocabulary: dining: 就餐; labelers: 分类者

**[860.56s] English:** that one like if you just look at a particular table what makes us say one is dining table and  
**Translation:** 

**[864.64s] English:** the other is not uh humans are not particularly consistent they're not like very good sources of  
**Translation:** 

**[869.52s] English:** supervision for a lot of these kind of edge cases so it may be also the fact that if we want  
**Translation:** 

**[875.44s] English:** a like want an algorithm or want a machine to solve a particular task for us we can maybe  
**Translation:** Vocabulary: algorithm: 算法

**[879.92s] English:** just specify the end goal um and like the stuff in between uh we really probably should not be  
**Translation:** 

**[885.52s] English:** specifying because we're not maybe going to confuse it a lot actually well humans can't  
**Translation:** Vocabulary: specifying: 指定外细节

**[890.08s] English:** even answer the meaning of life so we don't i'm not sure if we're good supervisors of the end  
**Translation:** 

**[894.24s] English:** goal either so let me ask you about categories humans are not very good at telling the difference  
**Translation:** Vocabulary: supervisors: 监督者

**[899.52s] English:** is and isn't a table like you mentioned um do you think it's possible let me let me ask you like a  
**Translation:** 

**[906.80s] English:** pretend you're plato um is it possible to create a pretty good taxonomy of objects in the world  
**Translation:** Vocabulary: taxonomy: 分类学

**[916.24s] English:** it seems like a lot of approaches in machine learning kind of assume  
**Translation:** 

**[920.24s] English:** a hopeful vision that it's possible to construct the perfect taxonomy or it exists perhaps out of  
**Translation:** 

**[925.92s] English:** our reach but we can always get closer and closer to it or is that a hopeful vision  
**Translation:** 

**[929.52s] English:** or a hopeless pursuit i think it's hopeless in some way so the thing is for any particular  
**Translation:** 

**[935.20s] English:** categorization that you create if you have a discrete sort of categorization i can always  
**Translation:** 

**[939.20s] English:** take the nearest two concepts or i can take a third concept and i can blend it in and i can  
**Translation:** Vocabulary: categorization: 分类; discrete: 离散

**[942.72s] English:** create a new category yeah so if you were to enumerate n categories i will always find an  
**Translation:** 

**[947.44s] English:** n plus one category for you that's not going to be in the end categories and i can actually create  
**Translation:** Vocabulary: enumerate: 列举

**[951.52s] English:** not just n plus one i can very easily create far more than n categories the thing is a lot of things  
**Translation:** 

**[959.52s] English:** really hard  
**Translation:** 

**[960.00s] English:** for us to come and sit and enumerate all of these out and they compose in various weird ways right  
**Translation:** 

**[965.36s] English:** like you have like a croissant and a donut come together to form a cronut so if you were to like  
**Translation:** Vocabulary: croissant: 羊角面包; donut: 甜甜圈

**[970.60s] English:** enumerate all the foods up until i don't know whenever the cronut was about 10 years ago or 15  
**Translation:** 

**[975.46s] English:** years ago then this entire thing called cronut would not exist yeah i remember there was a  
**Translation:** 

**[980.04s] English:** the most awesome video of a cat wearing a monkey costume  
**Translation:** 

**[983.32s] English:** people should look it up it's great so is that a monkey is that or is that a cat it's a very  
**Translation:** 

**[991.64s] English:** difficult philosophical question so there is a concept of similarity between objects so you think  
**Translation:** 

**[997.72s] English:** that can take us very far just kind of getting a good function a good way to tell which parts  
**Translation:** 

**[1006.42s] English:** of things are similar and which parts of things are very different i think so yeah so you don't  
**Translation:** 

**[1012.74s] English:** necessarily need to know which parts of things are similar and which parts of things are very  
**Translation:** 

**[1013.30s] English:** different you don't need to name everything or assign a name to everything to be able to use it  
**Translation:** 

**[1016.72s] English:** right so there are like lots of shakespeare said that what's in a name what's in the name yeah okay  
**Translation:** 

**[1022.70s] English:** and i mean a lot lots of like for example animals right they don't have necessarily a well-formed  
**Translation:** 

**[1028.04s] English:** like syntactic language but they're able to go about their day perfectly the same thing happens  
**Translation:** Vocabulary: syntactic: 句法的

**[1032.50s] English:** for us so i mean we probably look at things and we figure out oh this is similar to something else  
**Translation:** 

**[1038.46s] English:** that i've seen before and then i can probably learn how to use it so i have a lot of experience  
**Translation:** 

**[1043.28s] English:** with this kind of stuff but i haven't seen all the possible doorknobs in the world but if you show me  
**Translation:** 

**[1048.66s] English:** like i was able to get into this particular place fairly easily i've never seen that particular  
**Translation:** Vocabulary: doorknobs: 门把手

**[1052.40s] English:** doorknob so i of course related to all the doorknobs that i've seen and i know exactly  
**Translation:** 

**[1056.24s] English:** how it's going to open or i have a pretty good idea of how it's going to open and i think this  
**Translation:** Vocabulary: doorknob: 门把手

**[1061.04s] English:** kind of translation between experiences only happens because of similarity because i'm able  
**Translation:** 

**[1065.36s] English:** to relate it to a doorknob if i related it to a hair dryer i would probably be stuck still outside  
**Translation:** 

**[1069.20s] English:** not able to get in again a bit of a philosophical question but  
**Translation:** 

**[1073.28s] English:** is can similarity take us all the way to understanding a thing can having a good function  
**Translation:** Vocabulary: philosophical: 哲学性的

**[1080.00s] English:** that compares objects get us to understand something profound about singular objects  
**Translation:** 

**[1086.42s] English:** i think i'll ask you a question back what does it mean to understand objects  
**Translation:** Vocabulary: profound: 深奥的

**[1090.16s] English:** well let me tell you what that's similar to no uh i so there is there's an idea of sort of  
**Translation:** 

**[1097.26s] English:** reasoning by analogy kind of thing i think understanding is the process of placing that  
**Translation:** 

**[1104.36s] English:** thing in some kind of network of knowledge that you have that it perhaps is fundamentally related  
**Translation:** 

**[1111.62s] English:** to other concepts so it's not like understanding is fundamentally related by like composition of  
**Translation:** Vocabulary: fundamentally: 根本上

**[1118.06s] English:** other concepts and maybe in relation to other concepts um and maybe like deeper and deeper  
**Translation:** 

**[1124.98s] English:** understanding is maybe just adding more edges to that uh to that graph somehow uh so maybe it is  
**Translation:** 

**[1132.80s] English:** a composition of  
**Translation:** 

**[1134.26s] English:** a  
**Translation:** 

**[1134.34s] English:** a  
**Translation:** 

**[1134.36s] English:** I mean ultimately it is I suppose it is a kind of embedding in that wisdom  
**Translation:** Vocabulary: embedding: 嵌入

**[1140.42s] English:** space yeah okay wisdom space is good uh I think I do think right so similarity does  
**Translation:** 

**[1149.08s] English:** get you very very far is it the answer to everything I mean I don't even know what  
**Translation:** 

**[1153.50s] English:** everything is but it's going to take us really far um and I think the thing is things are similar  
**Translation:** 

**[1159.52s] English:** in very different contexts right so an elephant is similar to I don't know I don't know I don't  
**Translation:** 

**[1164.34s] English:** know I don't know lion and some in a different way because they're both four-legged creatures  
**Translation:** 

**[1170.16s] English:** uh they're also land animals but of course they're very different in a lot of different ways so  
**Translation:** 

**[1173.92s] English:** elephants are like herbivores um lions or not so similarity does similarity and particularly  
**Translation:** 

**[1179.44s] English:** dissimilarity also actually helps us understand a lot about things and so that's actually why  
**Translation:** Vocabulary: herbivores: 食草动物

**[1184.80s] English:** I think discrete categorization is very hard just like forming this particular category  
**Translation:** 

**[1189.28s] English:** of elephant and a particular category of lion maybe it's good for like just like taxonomy or  
**Translation:** Vocabulary: categorization: 分类; discrete: 离散; taxonomy: 分类学

**[1194.34s] English:** biological taxonomies. But when it comes to other things which are not as maybe, for example,  
**Translation:** 

**[1200.00s] English:** example like grilled cheese right i have a grilled cheese i dip it in tomato and i keep it outside  
**Translation:** 

**[1203.76s] English:** now is that still a grilled cheese or is that something else right so categorization is still  
**Translation:** 

**[1209.18s] English:** very useful for solving problems but is your intuition then sort of uh the self-supervised  
**Translation:** Vocabulary: intuition: 直觉

**[1215.68s] English:** should be the to borrow jan lakoon's terminology uh should be the cake and then categorization  
**Translation:** 

**[1223.48s] English:** the classification the maybe the supervised like layer should be just like the thing on top the  
**Translation:** Vocabulary: supervised: 监督式; terminology: 术语

**[1229.20s] English:** cherry or the icing or whatever so if you make it the cake it gets in the way of learning if you  
**Translation:** 

**[1235.68s] English:** make it the cake then you don't you won't be able to sit and annotate everything that's as simple as  
**Translation:** Vocabulary: annotate: 注释

**[1240.36s] English:** it is like that's my very practical view on it it's just uh i mean in my phd i sat down and  
**Translation:** 

**[1245.48s] English:** annotated like a bunch of cards for one of my projects and very quickly i was just like it was  
**Translation:** Vocabulary: annotated: 标注

**[1250.14s] English:** in a video and i was basically drawing boxes around all these cards and i think i spent about  
**Translation:** 

**[1254.56s] English:** a week doing all of that and i barely got anything done and basically this was i think  
**Translation:** 

**[1259.20s] English:** first year of my phd or like second year of my master's and then by the end of it i'm like okay  
**Translation:** 

**[1263.96s] English:** this is just hopeless i can keep doing it and when i done that uh someone came up to me and  
**Translation:** 

**[1268.58s] English:** they basically told me oh this is a pickup truck this is not a car and that's like aha this actually  
**Translation:** 

**[1274.34s] English:** makes sense because a pickup truck is not really like what was i annotating was i annotating  
**Translation:** Vocabulary: pickup: 皮卡

**[1277.60s] English:** anything that is mobile or was i annotating particular sedans or was i annotating suvs  
**Translation:** 

**[1282.56s] English:** what was i doing by the way the annotation was bounding boxes boxes yeah there's so many deep  
**Translation:** Vocabulary: annotating: 标注; annotation: 注释; bounding: 边界; sedans: 轿车

**[1289.20s] English:** questions here that you you're almost cheating your way out of by doing self-supervised learning  
**Translation:** 

**[1293.42s] English:** by the way which is like what makes for an object as opposed to solve intelligence maybe you don't  
**Translation:** 

**[1299.74s] English:** ever need to answer that question i mean this is the question that anyone that's ever done  
**Translation:** 

**[1304.64s] English:** annotation because it's so painful gets to ask like why am i doing a um drawing very careful  
**Translation:** 

**[1312.72s] English:** line around this object like what what what is the value i remember when i first saw semantic  
**Translation:** 

**[1319.20s] English:** annotation  
**Translation:** Vocabulary: semantic: 语义标注

**[1320.00s] English:** where you have uh like instant segmentation where you have a very exact line around the object in  
**Translation:** 

**[1328.42s] English:** the 2d plane of a fundamentally 3d object projected on a 2d plane so you're drawing a line around a  
**Translation:** Vocabulary: fundamentally: 本质上; projected: 投影; segmentation: 分割

**[1334.98s] English:** car that might be occluded there might be another thing in front of it but you're still drawing the  
**Translation:** 

**[1339.94s] English:** line of of the part of the car that you see how is that the car what why is that the car like i  
**Translation:** Vocabulary: occluded: 遮挡的

**[1348.18s] English:** had like an existential crisis every time like how is that going to help us understand a soft  
**Translation:** 

**[1353.92s] English:** computer vision i'm not sure i have a good answer to what's better and i'm not sure i share the  
**Translation:** Vocabulary: existential: 存在主义的

**[1359.46s] English:** confidence that you have that um self-supervised learning can take us far i think i'm more and  
**Translation:** 

**[1368.00s] English:** more convinced that it's a very important component but i still feel like we need to  
**Translation:** 

**[1372.12s] English:** understand what makes like this this uh like  
**Translation:** 

**[1377.92s] English:** like this uh like this uh like this uh like this uh like this uh like this uh like this uh like  
**Translation:** 

**[1378.16s] English:** dream of maybe what it's called like symbolic ai of of arriving like once you have this common  
**Translation:** 

**[1384.28s] English:** sense base be able to play with these concepts and build graphs or hierarchies of concepts on top  
**Translation:** Vocabulary: hierarchies: 层次结构; symbolic: 符号化的

**[1393.18s] English:** in order to then uh like form a a deep sense of this three-dimensional world or four-dimensional  
**Translation:** 

**[1401.14s] English:** world and be able to reason and then project that onto 2d plane in order to interpret a 2d image  
**Translation:** Vocabulary: interpret: 解释

**[1407.82s] English:** can i ask you just an uh out there question i remember i think i think andre kapati had a blog  
**Translation:** 

**[1414.60s] English:** post about computer vision uh like being really hard i forgot what the title was but it's many  
**Translation:** Vocabulary: andre: 安德烈

**[1420.50s] English:** many years ago and he had i think president obama stepping on a scale and there was humor and there's  
**Translation:** 

**[1425.84s] English:** a bunch of people laughing and whatever and uh the interesting there's a lot of interesting things  
**Translation:** 

**[1431.10s] English:** about that image and i think andre highlighted a bunch of things about the image that us humans  
**Translation:** 

**[1436.50s] English:** are able to immediately understand and i think that's a really good question and i think that's  
**Translation:** Vocabulary: highlighted: 强调

**[1437.82s] English:** a really good question and i think that's a really good question and i think that's a really good  
**Translation:** 

**[1440.00s] English:** gravity and that you can you have the concept of a weight you have a you immediately project  
**Translation:** Vocabulary: gravity: 重力

**[1446.00s] English:** because of our knowledge of pose and how human bodies are constructed you understand how the  
**Translation:** 

**[1451.88s] English:** forces are being applied with the human body uh they're really interesting other thing that you're  
**Translation:** 

**[1456.36s] English:** able to understand there's multiple people looking at each other in the image uh you're able to have  
**Translation:** 

**[1461.16s] English:** a mental model of what the people are thinking about you're able to infer like oh this person  
**Translation:** 

**[1466.06s] English:** is probably thinks like is laughing at how humorous the situation is and this person is  
**Translation:** 

**[1472.50s] English:** confused about what the situation is because they're looking this way we're able to infer all  
**Translation:** 

**[1476.64s] English:** of that so that's human vision how difficult is computer vision like in order to achieve that  
**Translation:** 

**[1486.64s] English:** level of understanding and maybe how big of a part does self-supervised learning play in that  
**Translation:** 

**[1493.68s] English:** do you think and do you still you know  
**Translation:** 

**[1496.06s] English:** back that was like over a decade ago i think andre and i think a lot of people agreed as  
**Translation:** 

**[1501.10s] English:** computer vision is really hard do you still think computer vision is really hard i think it is yes  
**Translation:** 

**[1506.94s] English:** and getting to that kind of understanding i mean it's really out there so if you ask me to solve  
**Translation:** 

**[1513.64s] English:** just that particular problem i can do it the supervised learning route i can always construct  
**Translation:** 

**[1518.30s] English:** a data set and basically predict oh is there humor in this or not and of course i can do it actually  
**Translation:** Vocabulary: supervised: 监督学习

**[1522.80s] English:** that's a good question do you think you can okay okay do you think you can do  
**Translation:** 

**[1526.04s] English:** human supervised annotation of humor to some extent yes i'm sure it'll work i mean it won't be  
**Translation:** Vocabulary: annotation: 注释

**[1531.58s] English:** it won't be as bad as like randomly guessing i'm sure it can still predict whether it's humorous  
**Translation:** 

**[1536.16s] English:** or not in some way yeah maybe like reddit upvotes is the signal i don't know i mean it won't do a  
**Translation:** 

**[1541.98s] English:** great job but it'll do something it may actually be like it may find certain things which are not  
**Translation:** 

**[1546.44s] English:** humorous humorous as well which is going to be bad for us but i mean it'll do a it won't be random  
**Translation:** 

**[1551.74s] English:** yeah kind of like my sense of humor okay so fine so you're going to do a little bit of a  
**Translation:** 

**[1556.04s] English:** that particular problem yes but the general problem you're saying is hard  
**Translation:** 

**[1560.00s] English:** problem is hard. And I mean, self supervised learning is not the answer to everything.  
**Translation:** 

**[1563.98s] English:** Of course it's not. I think if you have machines that are going to communicate with humans  
**Translation:** 

**[1568.20s] English:** at the end of it, you want to understand what the algorithm is doing, right? You want it  
**Translation:** 

**[1571.24s] English:** to be able to produce an output that you can decipher, that you can understand, or it's  
**Translation:** Vocabulary: algorithm: 算法; decipher: 破译

**[1575.82s] English:** actually useful for something else, which again is a human. So at some point in this  
**Translation:** 

**[1581.06s] English:** sort of entire loop, a human steps in and now this human needs to understand what's  
**Translation:** 

**[1585.46s] English:** going on. And at that point, this entire notion of language or semantics really comes in.  
**Translation:** 

**[1590.00s] English:** If the machine just spits out something and if we can't understand it, then it's not really  
**Translation:** Vocabulary: semantics: 语义; spits: 吐出

**[1594.76s] English:** that useful for us. So self supervised learning is probably going to be useful for a lot of  
**Translation:** 

**[1599.06s] English:** the things before that part, before the machine really needs to communicate a particular kind  
**Translation:** 

**[1603.80s] English:** of output with a human. Because, I mean, otherwise, how is it going to do that without language?  
**Translation:** 

**[1610.10s] English:** Or some kind of communication. But you're saying that it's possible to build a big base  
**Translation:** 

**[1614.14s] English:** of understanding or whatever, of what's the better...  
**Translation:** 

**[1617.94s] English:** Concepts.  
**Translation:** 

**[1618.94s] English:** Concepts.  
**Translation:** 

**[1619.94s] English:** Yeah.  
**Translation:** 

**[1620.94s] English:** Like common sense concepts.  
**Translation:** 

**[1621.94s] English:** Right.  
**Translation:** 

**[1622.94s] English:** Supervised learning in the context of computer vision is something you focused on, but that's  
**Translation:** 

**[1627.82s] English:** a really hard domain and it's kind of the cutting edge of what we're, as a community,  
**Translation:** 

**[1631.86s] English:** working on today. Can we take a little bit of a step back and look at language? Can you  
**Translation:** 

**[1636.52s] English:** summarize the history of success of self supervised learning in natural language processing, language  
**Translation:** Vocabulary: summarize: 概括历史

**[1642.88s] English:** modeling? What are transformers? What is the masking, the sentence completion that you  
**Translation:** 

**[1648.88s] English:** mentioned before? How does it lead us to understand anything? Semantic meaning of words, syntactic  
**Translation:** Vocabulary: semantic: 语义; syntactic: 句法

**[1655.40s] English:** role of words and sentences?  
**Translation:** 

**[1657.74s] English:** So I'm of course not the expert in NLP. I kind of follow it a little bit from the sides.  
**Translation:** 

**[1663.60s] English:** So the main sort of reason why all of this masking stuff works is I think it's called  
**Translation:** 

**[1668.46s] English:** the distributional hypothesis in NLP. The idea basically being that words that occur  
**Translation:** Vocabulary: distributional: 分布论; hypothesis: 假设

**[1672.98s] English:** in the same context should have similar meaning. So if you have the blank jumped over the blank,  
**Translation:** 

**[1677.88s] English:** it basically  
**Translation:** 

**[1680.00s] English:** whatever is like in the first blank is basically an object that can actually jump is going to be  
**Translation:** 

**[1684.76s] English:** something that can jump so a cat or a dog or i don't know sheep something all of these things  
**Translation:** 

**[1688.90s] English:** can basically be in that particular context and now so essentially the idea is that if you have  
**Translation:** 

**[1694.06s] English:** words that are in the same context and you predict them you're going to learn lots of useful things  
**Translation:** 

**[1699.94s] English:** about how words are related because you're predicting by looking at their context what  
**Translation:** 

**[1703.66s] English:** the word is going to be so in this particular case the blank jumped over the fence so now if  
**Translation:** 

**[1708.76s] English:** it's a sheep the sheep jumped over the fence the dog jumped over the fence so essentially the  
**Translation:** 

**[1713.46s] English:** algorithm or the representation basically puts together these two concepts together so it says  
**Translation:** Vocabulary: algorithm: 算法

**[1718.02s] English:** okay dogs are going to be kind of related to sheep because both of them occur in the same context  
**Translation:** 

**[1722.06s] English:** of course now you can decide depending on your particular application downstream you can say  
**Translation:** 

**[1727.12s] English:** dogs are absolutely not related to sheep because well i don't i really care about you know dog food  
**Translation:** 

**[1732.02s] English:** for example i'm a dog food person and i really want to give this dog food to this particular  
**Translation:** 

**[1736.12s] English:** animal so depending on what  
**Translation:** 

**[1738.66s] English:** you're  
**Translation:** 

**[1738.76s] English:** your downstream application is of course this notion of similarity or this notion or this  
**Translation:** 

**[1743.38s] English:** common sense that you've learned may not be applicable but the point is basically that this  
**Translation:** 

**[1747.18s] English:** just predicting what the blanks are is going to take you really really far so there's a nice  
**Translation:** 

**[1752.74s] English:** feature of language that the number of words in a particular language is very large but it's  
**Translation:** 

**[1760.10s] English:** finite and it's actually not that large in the grand scheme of things i i still gotta because  
**Translation:** 

**[1765.28s] English:** we take it for granted so first of all when you say masking you're talking about a language that  
**Translation:** Vocabulary: finite: 有限的

**[1768.66s] English:** is very complex and then you're talking about this very process of the blank of removing words from  
**Translation:** 

**[1772.68s] English:** a sentence and then having the knowledge of what word went there in the initial data set that's the  
**Translation:** 

**[1778.86s] English:** ground truth that you're training on and then you're asking the neural network to predict what  
**Translation:** 

**[1784.26s] English:** goes there that that's that's like a little trick yeah it's a really powerful trick the question is  
**Translation:** Vocabulary: neural: 神经网络

**[1791.56s] English:** how far that takes us and the other question is is there other tricks because to me it's very possible  
**Translation:** 

**[1798.66s] English:** there's other very fascinating  
**Translation:** 

**[1800.00s] English:** tricks. I'll give you an example. In autonomous driving, there's a bunch of tricks that give you  
**Translation:** 

**[1807.52s] English:** the self-supervised signal back. For example, very similar to sentences, but not really, which is  
**Translation:** Vocabulary: autonomous: 自主

**[1816.82s] English:** you have signals from humans driving the car, because a lot of us drive cars to places. And so  
**Translation:** 

**[1824.16s] English:** you can ask the neural network to predict what's going to happen in the next two seconds,  
**Translation:** 

**[1830.00s] English:** for a safe navigation through the environment. And the signal comes from the fact that you also  
**Translation:** 

**[1836.82s] English:** have knowledge of what happened in the next two seconds, because you have video of the data.  
**Translation:** 

**[1842.04s] English:** The question in autonomous driving, as it is in language, can we learn how to drive autonomously  
**Translation:** 

**[1849.88s] English:** based on that kind of self-supervision? Probably the answer is no. The question is, how good can  
**Translation:** Vocabulary: autonomously: 自主地

**[1857.02s] English:** we get? And the same with language. How good can we get?  
**Translation:** 

**[1860.00s] English:** And are there other tricks? We get sometimes super excited by this trick that works really  
**Translation:** 

**[1865.30s] English:** well. But I wonder, it's almost like mining for gold. I wonder how many signals there are in the  
**Translation:** 

**[1872.44s] English:** data that could be leveraged, that are like there. I just want to kind of linger on that, because  
**Translation:** Vocabulary: leveraged: 利用

**[1878.90s] English:** sometimes it's easy to think that maybe this masking process is self-supervised learning.  
**Translation:** 

**[1884.02s] English:** No, it's only one method. So there could be many, many other methods, many,  
**Translation:** 

**[1890.00s] English:** many key methods, maybe interesting ways to leverage human computation in very interesting  
**Translation:** 

**[1896.46s] English:** ways that might actually border on semi-supervised learning, something like that. Obviously,  
**Translation:** Vocabulary: computation: 计算; leverage: 利用

**[1901.48s] English:** the internet is generated by humans at the end of the day. So all that to say is, what's your sense  
**Translation:** 

**[1908.10s] English:** in this particular context of language? How far can that masking process take us?  
**Translation:** 

**[1914.34s] English:** So it has stood the test of time, right? I mean, so word-to-vec, the initial sort of NLP technique  
**Translation:** 

**[1919.68s] English:** that was used to do that. So it has stood the test of time, right? I mean, so word-to-vec,  
**Translation:** 

**[1919.98s] English:** the initial sort of NLP technique that was used to do that. So it has stood the test of time, right?  
**Translation:** 

**[1920.00s] English:** using this to now, for example, like all the BERT and all these big models that we get,  
**Translation:** 

**[1925.76s] English:** BERT and Roberta, for example, all of them are still sort of based on the same principle of  
**Translation:** 

**[1929.60s] English:** masking. It's taken us really far. I mean, you can actually do things like, oh, these two sentences  
**Translation:** 

**[1935.20s] English:** are similar or not, whether this particular sentence follows this other sentence in terms  
**Translation:** 

**[1938.88s] English:** of logic, so entailment. You can do a lot of these things with just this masking trick.  
**Translation:** Vocabulary: entailment: 推论关系

**[1944.72s] English:** So I'm not sure if I can predict how far it can take us, because when it first came out,  
**Translation:** 

**[1949.60s] English:** when Word2vec was out, I don't think a lot of us would have imagined that this would actually help  
**Translation:** 

**[1955.12s] English:** us do some kind of entailment problems really that well. And so just the fact that by just scaling up  
**Translation:** 

**[1960.80s] English:** the amount of data that we're training on and using better and more powerful neural network  
**Translation:** Vocabulary: neural: 神经网络

**[1965.04s] English:** architectures has taken us from that to this is just showing you how maybe poor predictors we are,  
**Translation:** 

**[1972.96s] English:** as humans, how poor we are at predicting how successful a particular technique is going to be.  
**Translation:** Vocabulary: predictors: 预测者

**[1977.20s] English:** So I think I can say something now, but like 10 years,  
**Translation:** 

**[1979.60s] English:** from now, I look completely stupid basically predicting this.  
**Translation:** 

**[1982.16s] English:** In the language domain, is there something in your work that you find useful and insightful  
**Translation:** 

**[1989.44s] English:** and transferable to computer vision, but also just, I don't know, beautiful and profound that  
**Translation:** Vocabulary: profound: 深奥; transferable: 可移植

**[1995.76s] English:** I think carries through to the vision domain? I mean, the idea of masking has been  
**Translation:** 

**[2000.24s] English:** very powerful. It has been used in vision as well for predicting, like you say, the next sort of,  
**Translation:** 

**[2005.20s] English:** if you have n sort of frames and you predict what's going to happen in the next frame. So  
**Translation:** 

**[2009.60s] English:** that's been very powerful. In terms of modeling, like in just terms in terms of architecture,  
**Translation:** 

**[2014.00s] English:** I think you would have asked about transformers a while back. That has really become, like it has  
**Translation:** 

**[2018.96s] English:** become super exciting for computer vision now. Like in the past, I would say year and a half,  
**Translation:** 

**[2022.96s] English:** it's become really powerful. What's a transformer?  
**Translation:** 

**[2025.44s] English:** Right. I mean, the core part of a transformer is something called the self-attention model.  
**Translation:** 

**[2029.20s] English:** So it came out of Google. And the idea basically is that if you have n elements,  
**Translation:** 

**[2033.92s] English:** what you're creating is a way for all of these n elements to talk to each other.  
**Translation:** 

**[2039.60s] English:** Is that you  
**Translation:** 

**[2040.00s] English:** are paying attention each element is paying attention to each of the other element and  
**Translation:** 

**[2045.22s] English:** basically by doing this it's really trying to figure out you're basically getting a much better  
**Translation:** 

**[2050.62s] English:** view of the data so for example if you have a sentence of like four words the point is if you  
**Translation:** 

**[2055.22s] English:** get a representation or a feature for this entire sentence it's constructed in a way such that each  
**Translation:** 

**[2060.70s] English:** word has paid attention to everything else now the reason it's like different from say what you  
**Translation:** 

**[2066.38s] English:** would do in a conf net is basically that in the content you would only pay attention to a local  
**Translation:** 

**[2070.84s] English:** window so each word would only pay attention to its next neighbor or like one neighbor after that  
**Translation:** 

**[2075.84s] English:** and the same thing goes for images and images you would basically pay attention to pixels in a three  
**Translation:** 

**[2080.46s] English:** cross three or a seven cross seven neighborhood and that's it whereas with the transformer the  
**Translation:** Vocabulary: pixels: 像素

**[2084.74s] English:** that self-attention mainly the sort of idea is that each element needs to pay attention to each  
**Translation:** 

**[2089.88s] English:** other element and when you say attention maybe another way to phrase that is you're considering  
**Translation:** 

**[2094.90s] English:** a  
**Translation:** 

**[2095.96s] English:** a context a wide context in terms of the wide context of the sentence in understanding  
**Translation:** 

**[2102.26s] English:** the meaning of a particular word and in computer vision that's understanding a larger context to  
**Translation:** 

**[2107.94s] English:** understand the local pattern of a particular local part of an image right so basically if  
**Translation:** 

**[2114.00s] English:** you have say again a banana in the image you're looking at the full image first so whether it's  
**Translation:** 

**[2119.12s] English:** like you know you're looking at all the pixels that are of a kitchen of a dining table and so  
**Translation:** Vocabulary: dining: 就餐

**[2123.40s] English:** on and then you're basically looking at the banana also  
**Translation:** 

**[2125.96s] English:** yeah by the way in terms of if we were to train the funny classifier there's something funny about  
**Translation:** 

**[2130.20s] English:** the word banana just going to anticipate that my my i am wearing a banana shirt so yeah is there  
**Translation:** 

**[2136.50s] English:** bananas on it okay so masking has worked for the vision context as well and so this transformer  
**Translation:** Vocabulary: anticipate: 预先料到

**[2143.30s] English:** idea has worked as well so basically looking at all the elements to understand a particular element  
**Translation:** 

**[2147.48s] English:** has been really powerful in vision the reason is like a lot of things when you're looking at them  
**Translation:** 

**[2152.76s] English:** in isolation so if you look at just a blob of pixels so antonio  
**Translation:** 

**[2155.96s] English:** toralba at mit used to have this like really famous image which i looked at when i was a  
**Translation:** 

**[2160.00s] English:** PhD student where he would basically have a blob of pixels and he would ask you hey what is this  
**Translation:** 

**[2164.30s] English:** and it looked basically like a shoe or like it could look like a tv remote it could look like  
**Translation:** 

**[2169.34s] English:** anything and it turns out it was a beer bottle but I'm not sure it was one of these three things  
**Translation:** 

**[2174.00s] English:** but basically he showed you the full picture and then it was very obvious what it was but the point  
**Translation:** 

**[2177.96s] English:** is but just by looking at that particular local window you couldn't figure out yeah because of  
**Translation:** 

**[2182.12s] English:** resolution because of other things it's just not easy always to just figure out by looking at just  
**Translation:** 

**[2186.76s] English:** the neighborhood of pixels what these pixels are yeah and the same thing happens for language as  
**Translation:** 

**[2191.08s] English:** well for the parameters that have to learn something about the data you need to give it  
**Translation:** 

**[2196.04s] English:** the capacity to learn the essential things like if it's not actually able to receive the signal at  
**Translation:** 

**[2201.84s] English:** all then it's not going to be able to learn that signal and in order to understand images and to  
**Translation:** 

**[2206.04s] English:** understand language you have to be able to see words in their full context okay what is harder  
**Translation:** 

**[2212.62s] English:** to solve vision or language visual intelligence or linguistic intelligence  
**Translation:** Vocabulary: linguistic: 语言智能

**[2216.76s] English:** so I'm going to say computer vision is harder my reason for this is basically that language of  
**Translation:** 

**[2223.36s] English:** course has a big structure to it because we developed it whereas vision is something that  
**Translation:** 

**[2228.22s] English:** is common in a lot of animals everyone is able to get by a lot of these animals on earth are  
**Translation:** 

**[2232.92s] English:** actually able to get by without language and a lot of these animals we also deem to be intelligent  
**Translation:** 

**[2237.76s] English:** so clearly intelligence does have like a visual component to it and yes of course in the case of  
**Translation:** 

**[2243.94s] English:** humans it of course also has a linguistic component but it means that we can't really  
**Translation:** 

**[2246.76s] English:** get by without language so it means that there is something far more fundamental about vision  
**Translation:** 

**[2250.60s] English:** than there is about language and I'm sorry to anyone who disagrees but yes this is what I feel  
**Translation:** 

**[2254.92s] English:** so that's being a little bit reflected in the challenges that have to do with the the progress  
**Translation:** 

**[2261.52s] English:** of self-supervised learning would you say or is that just the peculiar accidents of the progress  
**Translation:** 

**[2267.04s] English:** of the AI community that we focused on link or we discovered self-attention and transformers in the  
**Translation:** 

**[2272.62s] English:** context of language first so like the self-supervised learning success was actually  
**Translation:** 

**[2276.76s] English:** uh for vision has not much to do with the Transformers part  
**Translation:** 

**[2280.00s] English:** I would say it's actually been independent a little bit.  
**Translation:** 

**[2282.52s] English:** I think it's just that the signal  
**Translation:** 

**[2284.00s] English:** was a little bit different for vision  
**Translation:** 

**[2286.82s] English:** than there was for like NLP  
**Translation:** 

**[2288.16s] English:** and probably NLP folks discovered it before.  
**Translation:** 

**[2291.30s] English:** So for vision, the main success  
**Translation:** 

**[2292.74s] English:** has basically been this like crop so far,  
**Translation:** 

**[2294.88s] English:** like taking different crops of images.  
**Translation:** 

**[2296.88s] English:** Whereas for NLP, it was this masking thing.  
**Translation:** 

**[2298.98s] English:** But also the level of success  
**Translation:** 

**[2300.50s] English:** is still much higher for language.  
**Translation:** 

**[2302.12s] English:** It has, so that has a lot to do with,  
**Translation:** 

**[2304.82s] English:** I mean, I can get into a lot of details  
**Translation:** 

**[2306.96s] English:** for this particular question.  
**Translation:** 

**[2308.06s] English:** Let's go for it, okay.  
**Translation:** 

**[2309.06s] English:** So the first thing is language is very structured.  
**Translation:** 

**[2312.30s] English:** So you are going to produce a distribution  
**Translation:** 

**[2314.10s] English:** over a finite vocabulary.  
**Translation:** 

**[2315.96s] English:** English has a finite number of words.  
**Translation:** Vocabulary: finite: 有限的

**[2317.72s] English:** It's actually not that large.  
**Translation:** 

**[2319.30s] English:** And you need to produce basically,  
**Translation:** 

**[2321.68s] English:** when you're doing this masking thing,  
**Translation:** 

**[2322.82s] English:** all you need to do is basically tell me  
**Translation:** 

**[2324.20s] English:** which one of these like 50,000 words it is.  
**Translation:** 

**[2326.48s] English:** That's it.  
**Translation:** 

**[2327.32s] English:** Now for vision, let's imagine doing the same thing.  
**Translation:** 

**[2329.58s] English:** Okay, we're basically going to blank out  
**Translation:** 

**[2331.52s] English:** a particular part of the image  
**Translation:** 

**[2332.64s] English:** and we ask the network or this neural network  
**Translation:** 

**[2334.72s] English:** to predict what is present in this missing patch.  
**Translation:** 

**[2338.12s] English:** It's combinatorially like,  
**Translation:** Vocabulary: combinatorially: 组合地

**[2339.06s] English:** it's very large, right?  
**Translation:** 

**[2340.00s] English:** You have 256 pixel values.  
**Translation:** Vocabulary: pixel: 像素

**[2342.58s] English:** If you're even producing basically a seven cross seven  
**Translation:** 

**[2344.90s] English:** or a 14 cross 14, like window of pixels  
**Translation:** Vocabulary: pixels: 像素

**[2348.04s] English:** at each of these 169 or each of these 49 locations,  
**Translation:** 

**[2351.38s] English:** you have 256 values to predict.  
**Translation:** 

**[2353.80s] English:** And so it's really, really large.  
**Translation:** 

**[2355.32s] English:** And very quickly, the kind of like prediction problems  
**Translation:** 

**[2359.04s] English:** that we are setting up are going to be extremely  
**Translation:** 

**[2360.88s] English:** like intractable for us.  
**Translation:** Vocabulary: intractable: 难以解决

**[2362.82s] English:** And so the thing is for NLP,  
**Translation:** 

**[2364.00s] English:** it has been really successful  
**Translation:** 

**[2365.06s] English:** because we are very good at predicting,  
**Translation:** 

**[2367.60s] English:** like doing this,  
**Translation:** 

**[2368.50s] English:** like distribution over a finite set.  
**Translation:** 

**[2370.90s] English:** And the problem is when this set becomes really large,  
**Translation:** 

**[2373.56s] English:** we are going to become really, really bad  
**Translation:** 

**[2375.62s] English:** at making these predictions  
**Translation:** 

**[2377.06s] English:** and at solving basically this particular set of problems.  
**Translation:** 

**[2381.10s] English:** So if you were to do it exactly in this same way  
**Translation:** 

**[2384.26s] English:** as NLP for vision, there is very limited success.  
**Translation:** 

**[2387.10s] English:** The way stuff is working right now  
**Translation:** 

**[2389.02s] English:** is actually not by predicting these masks.  
**Translation:** 

**[2391.72s] English:** It's basically by saying that you take these two  
**Translation:** 

**[2393.72s] English:** like crops from the image,  
**Translation:** 

**[2395.20s] English:** you get a feature representation from it.  
**Translation:** 

**[2397.12s] English:** And just saying that these two features,  
**Translation:** 

**[2398.50s] English:** so they're like vectors,  
**Translation:** 

**[2400.00s] English:** just saying that the distance between these vectors should be small and so it's a very  
**Translation:** 

**[2404.60s] English:** different way of learning uh from the visual signal than there is from nlp okay the other  
**Translation:** 

**[2409.64s] English:** reason is the distributional hypothesis that we talked about for nlp right so a word given its  
**Translation:** 

**[2414.56s] English:** context basically the context actually supplies a lot of meaning to the word now because there  
**Translation:** Vocabulary: distributional: 分布假设; hypothesis: 假说

**[2419.74s] English:** are just finite number finite number of words and there is a finite way in like which we compose  
**Translation:** 

**[2424.62s] English:** them of course and the same thing holds for pixels but in language there's a lot of structure right  
**Translation:** 

**[2429.74s] English:** so i always say whatever the dash jumped over the fence for example there are lots of these  
**Translation:** 

**[2434.76s] English:** sentences that you'll get and from this you can actually look at this particular sentence might  
**Translation:** 

**[2439.90s] English:** occur in a lot of different contexts as well this exact same sentence might occur in a different  
**Translation:** 

**[2443.26s] English:** context so the sheep jumped over the fence the cat jumped over the fence the dog jumped over the  
**Translation:** 

**[2447.52s] English:** fence so you immediately get a lot of these words which are because this particular token itself has  
**Translation:** 

**[2452.84s] English:** so much meaning you get a lot of these tokens or these words which are actually going to have a  
**Translation:** Vocabulary: token: 令牌

**[2456.86s] English:** have sort of this related meaning across given this context  
**Translation:** 

**[2459.74s] English:** whereas for vision it's much harder because just by like pure like the way we capture images  
**Translation:** 

**[2465.50s] English:** lighting can be different um there might be like different noise in the sensor so the thing is  
**Translation:** 

**[2470.22s] English:** you're capturing a physical phenomenon and then you're basically going through a very complicated  
**Translation:** Vocabulary: sensor: 传感器

**[2474.54s] English:** pipeline of like image processing and then you're translating that into some kind of like digital  
**Translation:** 

**[2479.10s] English:** signal whereas with language you write it down and you transfer it to a digital signal almost  
**Translation:** Vocabulary: pipeline: 管道流程

**[2485.26s] English:** like it's a lossless like transfer and each of these tokens are very very well defined  
**Translation:** 

**[2489.74s] English:** there could be a little bit of an argument there because language as written down is a projection  
**Translation:** Vocabulary: lossless: 无损传输; projection: 投影

**[2497.02s] English:** of thought this is one of the open questions is if you perfectly can solve language are you getting  
**Translation:** 

**[2506.82s] English:** close to being able to solve you know easily with flying colors past the touring test kind of thing  
**Translation:** 

**[2512.34s] English:** so that's it's similar uh but different than the computer vision problem is in the 2d plane  
**Translation:** 

**[2519.74s] English:** is a  
**Translation:** 

**[2520.00s] English:** projection with three-dimensional world so perhaps there are similar uh similar problems there maybe  
**Translation:** 

**[2525.84s] English:** this i mean i think what i'm saying is nlp is not easy of course don't get me wrong like abstract  
**Translation:** 

**[2530.72s] English:** thought expressed in knowledge uh or knowledge basically expressed in language is really hard  
**Translation:** 

**[2535.40s] English:** to understand right i mean we've been communicating with language for so long and it's it is of course  
**Translation:** 

**[2540.34s] English:** a very complicated concept the thing is uh at least getting like some somewhat reasonable um  
**Translation:** 

**[2547.12s] English:** like being able to solve some kind of reasonable tasks with language i would say slightly easier  
**Translation:** 

**[2552.02s] English:** than it is with computer vision yeah i would say yeah so that that's well put i would say  
**Translation:** 

**[2556.96s] English:** getting impressive performance on language is uh easier that i feel like for both language  
**Translation:** 

**[2564.52s] English:** and computer vision there's going to be this wall of like that you like uh this hump you have to  
**Translation:** 

**[2571.18s] English:** overcome to achieve superhuman level performance or human level performance  
**Translation:** 

**[2577.12s] English:** like for language if that wall is farther away so you can get pretty nice you can do a lot of tricks  
**Translation:** 

**[2583.46s] English:** you can show really impressive performance you can even fool people that you're uh tweeting or  
**Translation:** Vocabulary: tweeting: 发推

**[2589.76s] English:** you're right blog post writing or your question answering uh is has intelligence behind it but to  
**Translation:** 

**[2597.48s] English:** truly demonstrate understanding of dialogue of continuous long-form dialogue that would require  
**Translation:** 

**[2606.52s] English:** perhaps  
**Translation:** 

**[2607.12s] English:** big breakthroughs in the same way in computer vision i think the big breakthroughs need to  
**Translation:** Vocabulary: breakthroughs: 重大进展

**[2612.64s] English:** happen earlier to to achieve uh impressive performance this might be a good place to uh  
**Translation:** 

**[2617.92s] English:** you already mentioned it but what is contrastive learning and what are energy-based models  
**Translation:** 

**[2623.32s] English:** contrastive learning is sort of the a paradigm of learning where the idea is that you are learning  
**Translation:** 

**[2629.48s] English:** this embedding space or so you're learning this sort of vector space of all your concepts and the  
**Translation:** Vocabulary: embedding: 嵌入; paradigm: 范式

**[2634.76s] English:** way you learn that is basically by contrasting so the idea is that you are learning this embedding  
**Translation:** 

**[2637.10s] English:** space or so you are learning this sort of vector space of all your concepts and the way you learn  
**Translation:** 

**[2637.12s] English:** this idea is that you have a sample you have another sample  
**Translation:** 

**[2640.00s] English:** that's related to it. So that's called a positive. And you have another sample that's not related to  
**Translation:** 

**[2644.98s] English:** it. So that's negative. So for example, let's just take an NLP or a simple example in computer  
**Translation:** 

**[2650.66s] English:** vision. So you have an image of a cat, you have an image of a dog. And for whatever application  
**Translation:** 

**[2655.94s] English:** that you're doing, say you're trying to figure out what pets are, you're saying that these two  
**Translation:** 

**[2659.56s] English:** images are related. So image of a cat and dog are related. But now you have another third image of a  
**Translation:** 

**[2664.18s] English:** banana, because you don't like that word. So now you basically have this banana.  
**Translation:** 

**[2668.86s] English:** Thank you for speaking to the crowd.  
**Translation:** 

**[2670.70s] English:** And so you take both of these images, and you take the image from the cat, the image from the dog,  
**Translation:** 

**[2675.14s] English:** you get a feature from both of them. And now what you're training the network to do is basically  
**Translation:** 

**[2678.56s] English:** pull both of these features together, while pushing them away from the feature of a banana.  
**Translation:** 

**[2684.50s] English:** So this is the contrastive part. So you're contrasting against the banana.  
**Translation:** 

**[2687.72s] English:** So there's always this notion of a negative and a positive.  
**Translation:** 

**[2691.34s] English:** Now, energy based models are like, like one way that Jan sort of explains a lot of these methods. So  
**Translation:** 

**[2698.06s] English:** Jan basically,  
**Translation:** 

**[2698.86s] English:** I think a couple of years or more than that, like when I joined Facebook, Jan used to keep mentioning  
**Translation:** 

**[2703.68s] English:** this word energy based models. And of course, I had no idea what he was talking about. So then one  
**Translation:** 

**[2707.70s] English:** day, I caught him in one of the conference rooms. And I'm like, Can you please tell me what this is?  
**Translation:** 

**[2711.20s] English:** So then, like very patiently, he sat down with like a marker and a whiteboard. And his idea  
**Translation:** 

**[2717.06s] English:** basically is that rather than talking about probability distributions, you can talk about  
**Translation:** Vocabulary: patiently: 耐心地; whiteboard: 白板

**[2720.94s] English:** energies of models. So models are trying to minimize certain energies in certain space,  
**Translation:** 

**[2724.66s] English:** or they're trying to maximize a certain kind of energy.  
**Translation:** Vocabulary: energies: 能量; maximize: 最大化

**[2727.88s] English:** And the idea basically is that you can explain a lot of the contrast of models GANs, for example,  
**Translation:** 

**[2733.06s] English:** which are like generative adversarial networks. A lot of these modern learning methods or VAEs,  
**Translation:** Vocabulary: adversarial: 对抗; generative: 生成

**[2738.26s] English:** which are variational autoencoders, you can really explain them very nicely in terms of an energy  
**Translation:** 

**[2742.66s] English:** function that they're trying to minimize or maximize. And so by putting this common sort of  
**Translation:** Vocabulary: autoencoders: 自动编码器

**[2747.62s] English:** language for all of these models, what looks very different in machine learning that VAEs are very  
**Translation:** 

**[2752.74s] English:** different from what GANs are are very, very different from what contrast models are, you actually  
**Translation:** 

**[2756.52s] English:** get a sense of  
**Translation:** 

**[2757.20s] English:** of like, oh, these are actually very, very related.  
**Translation:** 

**[2760.00s] English:** it's just that the way or the mechanism in which they're sort of maximizing or minimizing this  
**Translation:** 

**[2764.80s] English:** energy function is slightly different it's revealing the the commonalities between all  
**Translation:** Vocabulary: maximizing: 最大化; minimizing: 最小化

**[2769.20s] English:** these approaches and putting a sexy word on top of it like energy and so similarities two things  
**Translation:** 

**[2774.80s] English:** that are similar have low energy like the low energy signifying similarity right exactly so  
**Translation:** Vocabulary: signifying: 表示

**[2781.52s] English:** basically the idea is that if you were to imagine like the embedding as a manifold a 2d manifold  
**Translation:** 

**[2786.32s] English:** you would get a hill or like a high sort of peak in the energy manifold wherever two things are  
**Translation:** Vocabulary: embedding: 嵌入表示; manifold: 流形

**[2791.36s] English:** not related and basically you would have like a dip where two things are are related so you'd  
**Translation:** 

**[2795.60s] English:** get a dip in the manner and uh in the self supervised context how do you know two things  
**Translation:** Vocabulary: supervised: 监督学习

**[2801.44s] English:** are related and two things are not related right so this is where all the sort of ingenuity or  
**Translation:** 

**[2806.48s] English:** tricks comes in right so for example like uh you can take the fill in the blank problem or you can  
**Translation:** Vocabulary: ingenuity: 聪明才智

**[2812.40s] English:** take in the context problem and what you can say is two words that are in the same context  
**Translation:** 

**[2816.32s] English:** are related two words that are in different contexts are not related for images basically  
**Translation:** 

**[2821.12s] English:** two crops from the same image are related and whereas a third image is not related at all or  
**Translation:** 

**[2825.92s] English:** for a video it can be two frames from that video related because they're likely to contain the same  
**Translation:** 

**[2830.48s] English:** sort of concepts in them whereas a third frame from a different video is not related so it  
**Translation:** 

**[2835.68s] English:** basically is it's a very general term contrasting learning has nothing really to do with self  
**Translation:** 

**[2839.60s] English:** supervised learning it actually is very popular in for example like any kind of metric learning  
**Translation:** 

**[2844.64s] English:** or any kind of embedding learning  
**Translation:** 

**[2846.32s] English:** learning so it's also used in supervised learning it's all and the thing is because we are not  
**Translation:** 

**[2850.96s] English:** really using labels to get these positive or negative pairs it can basically also be used  
**Translation:** 

**[2855.68s] English:** for self-supervised learning so you mentioned one of the ideas in the vision context to uh  
**Translation:** 

**[2862.00s] English:** that works is to have different crops so you could think of that as a way to sort of manipulating the  
**Translation:** Vocabulary: manipulating: 操控

**[2868.56s] English:** data to generate uh examples that are similar obviously uh there's a bunch of other techniques  
**Translation:** 

**[2875.68s] English:** you mentioned  
**Translation:** 

**[2876.32s] English:** for example you could think of lighting as a very you know in images lighting  
**Translation:** 

**[2880.00s] English:** something that varies a lot, and you can artificially change those kinds of things.  
**Translation:** Vocabulary: artificially: 人工地

**[2884.52s] English:** There's the whole broad field of data augmentation, which manipulates images in order to increase  
**Translation:** 

**[2891.10s] English:** arbitrarily the size of the data set. First of all, what is data augmentation? And second of all,  
**Translation:** Vocabulary: arbitrarily: 随意; augmentation: 增加; manipulates: 处理

**[2896.50s] English:** what's the role of data augmentation in self-supervised learning and contrastive learning?  
**Translation:** 

**[2902.06s] English:** So data augmentation is just a way, like you said, it's basically a way to augment the data.  
**Translation:** 

**[2906.52s] English:** So you have, say, N samples, and what you do is you basically define some kind of transforms for  
**Translation:** 

**[2911.42s] English:** the sample. So you take your, say, image, and then you define a transform where you can just  
**Translation:** Vocabulary: transforms: 变换

**[2915.54s] English:** increase, say, the colors, like the colors or the brightness of the image, or increase or  
**Translation:** 

**[2920.04s] English:** decrease the contrast of the image, for example, or take different crops of it. So data augmentation  
**Translation:** 

**[2925.32s] English:** is just a process to basically perturb the data or augment the data, right? And so it has played  
**Translation:** 

**[2932.26s] English:** a fundamental role for computer vision, for self-supervised learning especially.  
**Translation:** Vocabulary: perturb: 扰乱数据

**[2936.52s] English:** The way most of the current methods work, contrastive or otherwise, is by taking an  
**Translation:** 

**[2941.80s] English:** image, in the case of images, is by taking an image and then computing basically two  
**Translation:** Vocabulary: computing: 计算

**[2947.04s] English:** perturbations of it. So these can be two different crops of the image with, like, different types of  
**Translation:** 

**[2952.42s] English:** lighting or different contrasts or different colors. So you jitter the colors a little bit  
**Translation:** Vocabulary: jitter: 抖动; perturbations: 扰动

**[2956.70s] English:** and so on. And now the idea is basically because it's the same object or because it's, like,  
**Translation:** 

**[2962.56s] English:** related concepts in both of these perturbations, you want the features from  
**Translation:** 

**[2966.52s] English:** both of these perturbations to be similar. So now you can use a variety of different ways to  
**Translation:** 

**[2971.62s] English:** enforce this constraint, like these features being similar. You can do this by contrastive  
**Translation:** Vocabulary: constraint: 约束

**[2975.64s] English:** learning. So basically, both of these things are positives, a third sort of image is negative.  
**Translation:** 

**[2980.26s] English:** You can do this basically by, like, clustering. For example, you can say that both of these images  
**Translation:** Vocabulary: clustering: 聚类; positives: 积极面

**[2986.38s] English:** should, the features from both of these images should belong in the same cluster because they're  
**Translation:** 

**[2990.04s] English:** related, whereas image, like, another image should belong to a different cluster. So there's a  
**Translation:** Vocabulary: cluster: 聚类

**[2994.36s] English:** variety of different ways to basically enforce  
**Translation:** 

**[2996.52s] English:** particular constraint. By the way, when you say features, it means...  
**Translation:** 

**[3000.00s] English:** There's a very large neural network that extracting patterns from the image and the kind of patterns it extracts should be either identical or very similar.  
**Translation:** 

**[3008.02s] English:** Right.  
**Translation:** Vocabulary: extracting: 提取; extracts: 提取; neural: 神经

**[3008.36s] English:** That's what that means.  
**Translation:** 

**[3009.22s] English:** So the neural network basically takes in the image and then outputs a set of like basically a vector of like numbers.  
**Translation:** 

**[3016.64s] English:** And that's the feature.  
**Translation:** 

**[3017.46s] English:** And you want this feature for both of these like different crops that you computed to be similar.  
**Translation:** Vocabulary: computed: 计算得出的

**[3022.12s] English:** So you want this vector to be identical in its like entries, for example.  
**Translation:** 

**[3025.90s] English:** Be like literally close in this multidimensional space to each other.  
**Translation:** Vocabulary: multidimensional: 多维的

**[3030.80s] English:** Right.  
**Translation:** 

**[3031.34s] English:** And like you said, close can mean part of the same cluster or something like that in this large space.  
**Translation:** 

**[3037.44s] English:** First of all, I wonder if there is connection to the way humans learn to this.  
**Translation:** 

**[3043.68s] English:** Almost like maybe subconsciously.  
**Translation:** Vocabulary: subconsciously: 潜意识地

**[3047.60s] English:** In order to understand a thing, you kind of have to see it from two, three multiple angles.  
**Translation:** 

**[3054.24s] English:** I wonder.  
**Translation:** 

**[3055.16s] English:** I have a lot of friends who are neuroscientists maybe and cognitive scientists.  
**Translation:** 

**[3060.06s] English:** I wonder if that's in there somewhere.  
**Translation:** Vocabulary: cognitive: 认知; neuroscientists: 神经科学家

**[3063.24s] English:** Like in order for us to place a concept in its proper place, we have to basically crop it in all kinds of ways.  
**Translation:** 

**[3072.08s] English:** Do basic data augmentation on it in whatever very clever ways that the brain likes to do.  
**Translation:** Vocabulary: augmentation: 数据增强

**[3077.70s] English:** Right.  
**Translation:** 

**[3078.62s] English:** Like spinning around in our mind somehow that is very effective.  
**Translation:** Vocabulary: spinning: 头晕

**[3082.80s] English:** So I think for some of them, we like need to do it.  
**Translation:** 

**[3085.10s] English:** Right.  
**Translation:** 

**[3085.32s] English:** Like babies, for example, pick up objects, like move them, put them close to their eye and whatnot.  
**Translation:** 

**[3089.76s] English:** Yeah.  
**Translation:** Vocabulary: whatnot: 诸如此类

**[3090.06s] English:** But for certain other things, actually, we are good at imagining it as well.  
**Translation:** 

**[3093.48s] English:** Right.  
**Translation:** 

**[3093.80s] English:** So if you, I have never seen, for example, an elephant from the top.  
**Translation:** 

**[3096.92s] English:** I've never basically looked at it from like top down.  
**Translation:** 

**[3099.16s] English:** Yeah.  
**Translation:** 

**[3099.32s] English:** But if you showed me a picture of it, I could very well tell you that that's an elephant.  
**Translation:** 

**[3103.58s] English:** So I think some of it, we're just like, we naturally build it or transfer it from other objects that we've seen to imagine what it's going to look like.  
**Translation:** 

**[3110.92s] English:** Has anyone done that with augmentation?  
**Translation:** 

**[3113.50s] English:** Like imagine.  
**Translation:** 

**[3115.14s] English:** Imagine all the possible things that are occluded or not there.  
**Translation:** Vocabulary: occluded: 被遮挡的

**[3119.52s] English:** Yeah.  
**Translation:** 

**[3120.00s] English:** not just like normal things like wild things but they're nevertheless physically consistent  
**Translation:** 

**[3125.56s] English:** so i mean people do kind of like occlusion based augmentation as well so you place in like a random  
**Translation:** 

**[3133.36s] English:** like box gray box to sort of mask out a certain part of the image and the thing is basically  
**Translation:** Vocabulary: occlusion: 遮挡

**[3138.74s] English:** you're kind of occluding it for example you place it say on half of a person's face so basically  
**Translation:** 

**[3144.10s] English:** saying that you know something below their nose is occluded because it's grayed out so no i meant  
**Translation:** Vocabulary: occluding: 遮挡

**[3149.42s] English:** like you have like what is it a table and you can't see behind the table and you imagine there's  
**Translation:** 

**[3155.14s] English:** a bunch of elves with bananas behind the table like i wonder if there's useful to have a wild  
**Translation:** Vocabulary: elves: 精灵

**[3162.38s] English:** imagination for the network because that's possible well maybe not elves but like puppies  
**Translation:** 

**[3167.12s] English:** and kittens or something like that just have a wild imagination and like constantly be generating  
**Translation:** 

**[3173.74s] English:** that wild imagination because in in terms of data augmentation that's currently applied it's super  
**Translation:** 

**[3179.06s] English:** ultra  
**Translation:** Vocabulary: ultra: 超级

**[3179.40s] English:** very boring it's very basic data augmentation i wonder if i wonder if there's a benefit to being  
**Translation:** 

**[3185.64s] English:** wildly imaginable while trying to be uh consistent with physical reality i think it's a kind of a  
**Translation:** Vocabulary: imaginable: 可想象的

**[3192.76s] English:** chicken and egg problem right because to have like amazing data augmentation you need to understand  
**Translation:** 

**[3197.02s] English:** what the scene is right and what we're trying to do data augmentation to learn what a scene is  
**Translation:** Vocabulary: augmentation: 增加

**[3201.50s] English:** anyway so it's basically it just keeps going on before you understand it just put l's with bananas  
**Translation:** 

**[3205.88s] English:** until you know it's not to be true  
**Translation:** 

**[3209.40s] English:** just like children have a wild imagination until the adults ruin it all okay so what are the  
**Translation:** 

**[3215.32s] English:** different kinds of data augmentation that you seem to be effective in visual intelligence for  
**Translation:** 

**[3220.96s] English:** like visual it's a lot of these image filtering operations so like blurring the image you know  
**Translation:** 

**[3226.78s] English:** all the kind of instagram filters that you can think of so like arbitrarily like make the red  
**Translation:** Vocabulary: arbitrarily: 随意; blurring: 模糊

**[3231.58s] English:** super red make the green super greens like saturate the image rotation cropping rotation cropping  
**Translation:** 

**[3238.08s] English:** exactly all of these kind of things  
**Translation:** Vocabulary: cropping: 裁剪

**[3239.40s] English:** Like you said,  
**Translation:** 

**[3240.00s] English:** lighting is a really interesting one yes to me like that feels like really complicated to do so  
**Translation:** 

**[3244.80s] English:** i mean they don't the augmentations that we work on aren't like that involved they're not going to  
**Translation:** 

**[3249.38s] English:** be like physically realistic versions of lighting it's not that you're assuming that there's a light  
**Translation:** Vocabulary: augmentations: 增强功能

**[3253.20s] English:** source up and then you're moving it to the right and then what does the thing look like it's really  
**Translation:** 

**[3257.34s] English:** more about like brightness of the image overall brightness of the image or overall contrast of  
**Translation:** 

**[3261.50s] English:** the image and so on but this is a really important point to me i always thought that data augmentation  
**Translation:** 

**[3268.22s] English:** holds an important key to big improvements in machine learning and it seems that it is an  
**Translation:** 

**[3275.64s] English:** important aspect of self-supervised learning so i wonder if there's big improvements to be achieved  
**Translation:** 

**[3282.18s] English:** on much more intelligent kinds of data augmentation for example currently maybe you can correct me if  
**Translation:** 

**[3289.34s] English:** i'm wrong data augmentation is not parametrized yeah you're not learning you're not learning to  
**Translation:** 

**[3295.36s] English:** me it seems like data augmentation  
**Translation:** Vocabulary: parametrized: 参数化

**[3298.22s] English:** potentially should involve more learning than the learning process itself right um you're almost like  
**Translation:** 

**[3306.14s] English:** thinking of like generative kind of it's the elves with bananas you're trying to it's like very active  
**Translation:** Vocabulary: elves: 精灵; generative: 生成的

**[3312.32s] English:** imagination of messing with the world and teaching that mechanism for messing with the world to be  
**Translation:** 

**[3318.02s] English:** realistic right um because that feels like i mean it's imagination it's just as you said it things  
**Translation:** 

**[3325.96s] English:** it feels like us humans are able to  
**Translation:** 

**[3328.22s] English:** um maybe sometimes subconsciously imagine before we see the thing imagine what we're expecting to  
**Translation:** Vocabulary: subconsciously: 潜意识地

**[3334.54s] English:** see like maybe several options and especially we probably forgot but when we're younger  
**Translation:** 

**[3339.70s] English:** probably the possibilities were wild they're more numerous and then as we get older we become to  
**Translation:** 

**[3345.86s] English:** understand the world and uh are the possibilities of what we might see becomes less and less and  
**Translation:** 

**[3352.02s] English:** less so i wonder if you think there's a lot of breakthroughs yet to be had in data augmentation  
**Translation:** Vocabulary: augmentation: 数据增强; breakthroughs: 突破

**[3356.88s] English:** and maybe also can you just comment on that because i think that's a really important point  
**Translation:** 

**[3358.22s] English:** comment on the stuff we have is that  
**Translation:** 

**[3360.00s] English:** at a big part of self-supervised learning.  
**Translation:** 

**[3362.14s] English:** Yes, so data augmentation is like  
**Translation:** 

**[3363.84s] English:** key to self-supervised learning.  
**Translation:** 

**[3365.54s] English:** That has like the kind of augmentation that we're using  
**Translation:** 

**[3368.34s] English:** and basically the fact that we're trying to learn  
**Translation:** 

**[3371.04s] English:** these neural networks that are predicting these features  
**Translation:** Vocabulary: neural: 神经网络

**[3373.94s] English:** from images that are robust under data augmentation  
**Translation:** 

**[3377.10s] English:** has been the key for visual self-supervised learning.  
**Translation:** Vocabulary: robust: 健壮的

**[3379.56s] English:** And they play a fairly fundamental role to it.  
**Translation:** 

**[3382.40s] English:** Now, the irony of all of this is that  
**Translation:** Vocabulary: irony: 讽刺

**[3384.60s] English:** for like deep learning purists will say  
**Translation:** 

**[3386.72s] English:** the entire point of deep learning  
**Translation:** Vocabulary: purists: 理论派

**[3388.38s] English:** is that you feed in the pixels to the neural network  
**Translation:** 

**[3391.16s] English:** and it should figure out the patterns on its own.  
**Translation:** Vocabulary: pixels: 像素

**[3393.14s] English:** So if it really wants to look at edges,  
**Translation:** 

**[3394.46s] English:** it should look at edges.  
**Translation:** 

**[3395.64s] English:** You shouldn't really go and hand craft  
**Translation:** 

**[3397.44s] English:** these tech features, right?  
**Translation:** 

**[3398.60s] English:** You shouldn't go tell it that look at edges.  
**Translation:** 

**[3401.16s] English:** So data augmentation should basically  
**Translation:** 

**[3403.10s] English:** be in the same category, right?  
**Translation:** 

**[3404.42s] English:** Why should we tell the network  
**Translation:** 

**[3406.06s] English:** or tell this entire learning paradigm  
**Translation:** 

**[3408.20s] English:** what kinds of data augmentation that we're looking for?  
**Translation:** Vocabulary: paradigm: 范式

**[3410.86s] English:** We are encoding a very sort of human specific bias there  
**Translation:** 

**[3415.20s] English:** that we know things are,  
**Translation:** Vocabulary: encoding: 编码

**[3417.26s] English:** like if you change  
**Translation:** 

**[3418.28s] English:** the contrast of the image,  
**Translation:** 

**[3419.22s] English:** it should still be an apple  
**Translation:** 

**[3420.26s] English:** or it should still see apple, not banana.  
**Translation:** 

**[3422.24s] English:** And basically if we change like colors,  
**Translation:** 

**[3425.88s] English:** it should still be the same kind of concept.  
**Translation:** 

**[3428.06s] English:** Of course, this is not one,  
**Translation:** 

**[3429.90s] English:** this is doesn't feel like super satisfactory  
**Translation:** Vocabulary: satisfactory: 令人满意

**[3432.50s] English:** because a lot of our human knowledge  
**Translation:** 

**[3434.56s] English:** or our human supervision  
**Translation:** Vocabulary: supervision: 监督

**[3435.78s] English:** is actually going into the data augmentation.  
**Translation:** 

**[3437.60s] English:** So although we are calling it self-supervised learning,  
**Translation:** 

**[3439.66s] English:** a lot of the human knowledge is actually being encoded  
**Translation:** 

**[3441.90s] English:** in the data augmentation process.  
**Translation:** Vocabulary: encoded: 编码

**[3443.52s] English:** So it's really like we've kind of sneaked away  
**Translation:** 

**[3445.50s] English:** the supervision at the input.  
**Translation:** 

**[3447.12s] English:** And we are like really  
**Translation:** 

**[3447.96s] English:** designing these nice list of data augmentations  
**Translation:** Vocabulary: augmentations: 数据增强

**[3450.34s] English:** that are working very well.  
**Translation:** 

**[3451.64s] English:** Of course, the idea is that it's much easier  
**Translation:** 

**[3453.72s] English:** to design a list of data augmentation than it is to do.  
**Translation:** 

**[3456.60s] English:** So humans are doing nevertheless,  
**Translation:** 

**[3458.16s] English:** doing less and less work  
**Translation:** 

**[3459.64s] English:** and maybe leveraging their creativity more and more.  
**Translation:** 

**[3462.60s] English:** And when we say data augmentation is not parameterized,  
**Translation:** 

**[3465.08s] English:** it means it's not part of the learning process.  
**Translation:** Vocabulary: parameterized: 参数化

**[3468.18s] English:** Do you think it's possible to integrate  
**Translation:** 

**[3470.54s] English:** some of the data augmentation into the learning process?  
**Translation:** 

**[3473.28s] English:** I think so.  
**Translation:** 

**[3474.12s] English:** I think so.  
**Translation:** 

**[3474.96s] English:** And in fact, it will be really beneficial for us.  
**Translation:** 

**[3477.42s] English:** Because a lot of these data augmentation that we use  
**Translation:** Vocabulary: augmentation: 数据扩增

**[3480.00s] English:** vision are very extreme for example like when you have certain concepts again a banana you take the  
**Translation:** 

**[3487.60s] English:** banana and then basically you change the color of the banana right so you make it a purple banana  
**Translation:** 

**[3492.24s] English:** now this data augmentation process is actually independent of the like it has no notion of what  
**Translation:** 

**[3497.84s] English:** is present in the image so it can change this color arbitrarily it can make it a red banana as  
**Translation:** Vocabulary: arbitrarily: 任意地

**[3501.60s] English:** well and now what we're doing is we're telling the neural network that this red banana and uh so crop  
**Translation:** 

**[3507.60s] English:** of this image which has the red banana and a crop of this image where i change the color to a purple  
**Translation:** 

**[3511.36s] English:** banana should be the features should be the same now bananas aren't red or purple mostly so really  
**Translation:** 

**[3517.20s] English:** the data augmentation process should take into account what is present in the image and what are  
**Translation:** 

**[3521.52s] English:** the kinds of physical realities that are possible it shouldn't be completely independent of the  
**Translation:** 

**[3525.36s] English:** image so you might get big gains if you instead of being drastic do subtle augmentation but realistic  
**Translation:** Vocabulary: drastic: 剧烈的

**[3532.24s] English:** augmentation right realistic i'm not sure if it's subtle but like realistic for sure if it's  
**Translation:** 

**[3537.60s] English:** even subtle augmentation will give you big benefits exactly yeah and it will be like for  
**Translation:** 

**[3544.00s] English:** particular domains you might actually see like if for example now we're doing medical imaging  
**Translation:** 

**[3548.72s] English:** there are going to be certain kinds of like geometric augmentations which are not really  
**Translation:** Vocabulary: geometric: 几何的

**[3552.16s] English:** going to be very valid for the human body so if you were to like actually loop in data augmentation  
**Translation:** 

**[3558.16s] English:** into the learning process it will actually be much more useful now this actually does take  
**Translation:** 

**[3562.96s] English:** us to maybe a semi-supervised kind of a setting because you do want to understand  
**Translation:** 

**[3567.36s] English:** what is it that you're trying to solve so currently self-supervised learning kind of  
**Translation:** 

**[3571.12s] English:** operates in the wild right so you do the self-supervised learning you re and the purists  
**Translation:** 

**[3575.84s] English:** and all of us basically say that okay this should learn useful representations and they should be  
**Translation:** Vocabulary: purists: 纯粹主义者

**[3579.84s] English:** useful for any kind of end task no matter it's like banana recognition or like autonomous driving  
**Translation:** 

**[3586.08s] English:** now it's a tall order maybe the first baby step for us should be  
**Translation:** Vocabulary: autonomous: 自主的

**[3590.08s] English:** that okay if you're trying to loop in this data augmentation into the learning process  
**Translation:** 

**[3593.84s] English:** then we at least need to have some sense of what we're trying to do are we trying to  
**Translation:** 

**[3597.36s] English:** distinguish between different types of bananas or are we trying to  
**Translation:** 

**[3600.00s] English:** to distinguish between banana and apple? Or are we trying to do all of these things at once?  
**Translation:** 

**[3604.38s] English:** And so some notion of like what happens at the end might actually help us do much better at this  
**Translation:** 

**[3610.30s] English:** side. Let me ask you a ridiculous question. If I were to give you like a black box, like a choice  
**Translation:** 

**[3616.84s] English:** to have an arbitrary large data set of real natural data versus really good data augmentation  
**Translation:** 

**[3625.28s] English:** algorithms, which would you like to train in a self-supervised way on? So natural data from the  
**Translation:** Vocabulary: arbitrary: 随意; augmentation: 增强

**[3632.52s] English:** internet, arbitrary large, so unlimited data. Or it's like more controlled, good data augmentation  
**Translation:** 

**[3641.60s] English:** on the finite data set. The thing is like because our learning algorithms for vision right now  
**Translation:** Vocabulary: finite: 有限的

**[3646.66s] English:** really rely on data augmentation, even if you were to give me like an infinite source of like  
**Translation:** 

**[3651.86s] English:** image data, I still need a good data augmentation algorithm.  
**Translation:** Vocabulary: algorithm: 算法

**[3654.50s] English:** You need something.  
**Translation:** 

**[3655.28s] English:** Something that tells you that two things are similar.  
**Translation:** 

**[3657.44s] English:** Right. And so something, because you've given me an arbitrarily large data set, I still need to use  
**Translation:** 

**[3662.44s] English:** data augmentation to take that image, construct like these two perturbations of it, and then learn  
**Translation:** Vocabulary: arbitrarily: 随意; perturbations: 扰动

**[3667.46s] English:** from it. So the thing is our learning paradigm is very primitive right now. Even if you were to give  
**Translation:** 

**[3672.98s] English:** me lots of images, it's still not really useful. A good data augmentation algorithm is actually  
**Translation:** Vocabulary: paradigm: 范式

**[3676.76s] English:** going to be more useful. So you can like reduce down the amount of data that you give me by like  
**Translation:** 

**[3681.96s] English:** 10 times. But if you were to give me a good data augmentation algorithm, that would be more useful.  
**Translation:** 

**[3685.26s] English:** Probably do better than giving me like 10 times the size of that data. But me having to rely on like a very  
**Translation:** 

**[3691.22s] English:** primitive data augmentation algorithm.  
**Translation:** 

**[3692.56s] English:** Like through tagging and all those kinds of things. Is there a way to discover things that are semantically  
**Translation:** 

**[3698.16s] English:** similar on the Internet? Obviously there is, but it might be extremely noisy and the difference might be  
**Translation:** Vocabulary: semantically: 语义上

**[3704.90s] English:** farther away than you would be comfortable with.  
**Translation:** 

**[3707.76s] English:** So, I mean, yes, tagging will help you a lot. It'll actually go a very long way in figuring out what images are  
**Translation:** 

**[3712.68s] English:** related or not. And then so.  
**Translation:** 

**[3715.26s] English:** But then the purists would argue that when you're using human tags, because these tags are  
**Translation:** Vocabulary: purists: 完美主义者

**[3720.00s] English:** like supervision is it really really self-supervised learning now because you're using human tags to  
**Translation:** 

**[3725.36s] English:** figure out which images are like similar hashtag no filter means a lot of things yes i mean there  
**Translation:** Vocabulary: supervision: 监督

**[3731.52s] English:** are certain tags which are going to be applicable pretty much to anything so they're pretty useless  
**Translation:** 

**[3736.88s] English:** for learning yeah but i mean certain tags are actually like the eye filter for example or the  
**Translation:** 

**[3742.72s] English:** taj mahal for example these tags are like very indicative of what's going on and they are i mean  
**Translation:** 

**[3747.84s] English:** they are human supervision yeah this is one of the tasks of discovering from human generated  
**Translation:** Vocabulary: indicative: 表明

**[3753.20s] English:** data strong signals that could be leveraged uh for self-supervision like humans are doing so  
**Translation:** 

**[3760.48s] English:** much work already like many years ago there was something that was called i guess human  
**Translation:** Vocabulary: leveraged: 利用

**[3765.68s] English:** computation back in the day humans are doing so much work it's it'd be exciting to discover  
**Translation:** 

**[3772.40s] English:** ways to leverage the work they're doing to teach machines without any extra effort from them  
**Translation:** Vocabulary: computation: 计算; leverage: 利用

**[3777.84s] English:** an example could be like we said driving humans driving and machines can learn from the driving  
**Translation:** 

**[3782.88s] English:** i always hope that there could be some supervision signal discovered in video games because there's  
**Translation:** 

**[3788.56s] English:** so many people that play video games that it feels like so much effort is put into video games  
**Translation:** 

**[3795.92s] English:** into playing video games and you can design video games somewhat  
**Translation:** 

**[3801.04s] English:** cheaply right to include whatever signals you want it feels like uh that could be leveraged somehow so  
**Translation:** 

**[3807.84s] English:** people are using that like there are actually folks right here in ut austin like philip graham  
**Translation:** Vocabulary: cheaply: 便宜地

**[3811.68s] English:** bull is a professor at ut austin uh he's been like working on video games uh as a source of  
**Translation:** 

**[3816.88s] English:** supervision i mean it's it's really fun like as a phd student getting to basically play video games  
**Translation:** 

**[3821.84s] English:** all day yeah but so i do hope that kind of thing scales and like ultimately boils down to  
**Translation:** 

**[3826.96s] English:** discovering some undeniably very good signal it's like masking in nlp but that said there's  
**Translation:** Vocabulary: undeniably: 无可否认地

**[3835.60s] English:** non-contrastive methods right  
**Translation:** 

**[3837.84s] English:** do non-contrastive energy  
**Translation:** 

**[3840.00s] English:** based self-supervised learning methods look like,  
**Translation:** 

**[3843.56s] English:** and why are they promising?  
**Translation:** 

**[3845.68s] English:** So, like I said about contrastive learning,  
**Translation:** 

**[3847.84s] English:** you have this notion of a positive and a negative.  
**Translation:** 

**[3850.76s] English:** Now, the thing is, this entire learning paradigm  
**Translation:** 

**[3853.66s] English:** really requires access to a lot of negatives  
**Translation:** Vocabulary: paradigm: 范式

**[3857.20s] English:** to learn a good sort of feature space.  
**Translation:** 

**[3859.08s] English:** The idea is if I tell you, okay,  
**Translation:** 

**[3861.70s] English:** so a cat and a dog are similar,  
**Translation:** 

**[3863.72s] English:** and they're very different from a banana.  
**Translation:** 

**[3865.72s] English:** The thing is, this is a fairly simple analogy, right?  
**Translation:** 

**[3868.04s] English:** Because bananas look visually very different  
**Translation:** 

**[3870.90s] English:** from what cats and dogs do.  
**Translation:** 

**[3872.48s] English:** So very quickly, if this is the only source of supervision  
**Translation:** Vocabulary: supervision: 监督

**[3875.06s] English:** that I'm giving you, your learning is not going to be like,  
**Translation:** 

**[3878.14s] English:** after a point, the neural network  
**Translation:** Vocabulary: neural: 神经网络

**[3879.80s] English:** is really not going to learn a lot,  
**Translation:** 

**[3881.70s] English:** because the negative that you're getting  
**Translation:** 

**[3883.02s] English:** is going to be so random.  
**Translation:** 

**[3883.94s] English:** So it can be, oh, a cat and a dog are similar,  
**Translation:** 

**[3886.70s] English:** but they're very different from a Volkswagen Beetle.  
**Translation:** 

**[3889.94s] English:** Now, this car looks very different from these animals again.  
**Translation:** Vocabulary: beetle: 甲壳虫; volkswagen: 大众汽车

**[3892.98s] English:** So the thing is, in contrast to learning,  
**Translation:** 

**[3894.94s] English:** the quality of the negative sample really matters a lot.  
**Translation:** 

**[3898.04s] English:** And so what has happened is basically  
**Translation:** 

**[3900.34s] English:** that typically these methods that are contrastive really  
**Translation:** 

**[3903.14s] English:** require access to lots of negatives, which  
**Translation:** 

**[3905.16s] English:** becomes harder and harder to sort of scale  
**Translation:** 

**[3906.98s] English:** when designing alerting algorithm.  
**Translation:** 

**[3909.04s] English:** So that's been one of the reasons why  
**Translation:** Vocabulary: alerting: 告警; algorithm: 算法

**[3911.12s] English:** non-contrastive methods have become popular  
**Translation:** 

**[3913.72s] English:** and why people think that they're going to be more useful.  
**Translation:** 

**[3916.50s] English:** So a non-contrastive method, for example,  
**Translation:** 

**[3918.50s] English:** like clustering is one non-contrastive method.  
**Translation:** Vocabulary: clustering: 聚类方法

**[3920.92s] English:** The idea basically being that you have two of these samples.  
**Translation:** 

**[3924.88s] English:** So the cat and dog are two crops of this image.  
**Translation:** 

**[3927.70s] English:** They belong to the same cluster.  
**Translation:** 

**[3930.44s] English:** And so essentially, you're basically  
**Translation:** Vocabulary: cluster: 聚类

**[3932.08s] English:** doing clustering online when you're learning this network,  
**Translation:** 

**[3934.84s] English:** and which is very different from having access  
**Translation:** 

**[3936.70s] English:** to a lot of negatives explicitly.  
**Translation:** 

**[3938.92s] English:** The other way which has become really popular  
**Translation:** Vocabulary: explicitly: 明确地

**[3940.84s] English:** is something called self-distillation.  
**Translation:** 

**[3943.14s] English:** So the idea basically is that you have a teacher network  
**Translation:** 

**[3945.70s] English:** and a student network.  
**Translation:** 

**[3947.52s] English:** And the teacher network produces a feature,  
**Translation:** 

**[3949.54s] English:** so it takes in the image.  
**Translation:** 

**[3951.10s] English:** And basically, the neural network figures out the patterns,  
**Translation:** 

**[3953.68s] English:** gets the feature out.  
**Translation:** 

**[3955.06s] English:** And there's another neural network, which  
**Translation:** 

**[3956.90s] English:** is the student neural network, and that also produces a feature.  
**Translation:** 

**[3960.00s] English:** now all you're doing is basically saying that the features produced by the teacher network and the  
**Translation:** 

**[3964.00s] English:** student network should be very similar that's it there is no notion of a negative anymore  
**Translation:** 

**[3969.04s] English:** and that's it so it's all about similarity maximization between these two features  
**Translation:** Vocabulary: maximization: 最大化

**[3973.52s] English:** and so all i need to now do is figure out how to have these two sorts of parallel networks a  
**Translation:** 

**[3978.64s] English:** student network and a teacher network and basically researchers have figured out very  
**Translation:** 

**[3983.12s] English:** cheap methods to do this so you can actually have for free really two types of neural networks  
**Translation:** 

**[3988.00s] English:** uh they're kind of related but they're different enough that you can actually basically have a  
**Translation:** 

**[3992.72s] English:** learning problem set up so you can ensure that they always remain different enough  
**Translation:** 

**[3998.08s] English:** so the thing doesn't collapse into something boring exactly so the main sort of enemy of  
**Translation:** 

**[4003.12s] English:** self-supervised learning any kind of similarity maximization technique is collapse right so  
**Translation:** 

**[4007.68s] English:** collapse means that you learn the same feature representation for all demons in the world which  
**Translation:** Vocabulary: demons: 样本

**[4013.20s] English:** is completely useless everything is a banana everything is a banana everything is a cat  
**Translation:** 

**[4017.20s] English:** everything is a car  
**Translation:** 

**[4018.00s] English:** yeah  
**Translation:** 

**[4019.04s] English:** and so all we need to do is basically come up with ways to prevent collapse contrastive learning  
**Translation:** 

**[4024.00s] English:** is one way of doing it and then for example like clustering or self-distillation or other ways of  
**Translation:** 

**[4028.32s] English:** doing it we also had a recent paper where we used like de-correlation between like two sets  
**Translation:** 

**[4034.80s] English:** of features to prevent collapse so that's inspired a little bit by like horace barlow's neuroscience  
**Translation:** 

**[4039.36s] English:** principles  
**Translation:** Vocabulary: horace: 霍尔塞; neuroscience: 神经科学

**[4040.64s] English:** by the way i should comment that whoever counts the number of times than the word banana apple  
**Translation:** 

**[4047.04s] English:** cat and dog were used against them by terrorism or although they were in fact in the USA in the  
**Translation:** 

**[4047.98s] English:** in this conversation, wins the internet.  
**Translation:** 

**[4050.08s] English:** I wish you luck.  
**Translation:** 

**[4052.26s] English:** What is SWAV and the main improvement proposed  
**Translation:** 

**[4056.68s] English:** in the paper on supervised learning of visual features  
**Translation:** Vocabulary: supervised: 监督学习

**[4060.16s] English:** by contrasting cluster assignments?  
**Translation:** 

**[4063.08s] English:** SWAV basically is a clustering-based technique,  
**Translation:** Vocabulary: cluster: 聚类

**[4066.22s] English:** which is for, again, the same thing  
**Translation:** 

**[4068.02s] English:** for self-supervised learning in vision,  
**Translation:** 

**[4070.74s] English:** where we have two crops.  
**Translation:** 

**[4072.52s] English:** And the idea basically is that you want the features  
**Translation:** 

**[4075.18s] English:** from these two crops of an image  
**Translation:** 

**[4076.56s] English:** to lie in the same cluster and basically  
**Translation:** 

**[4080.00s] English:** the crops that are coming from different images to be in different clusters.  
**Translation:** 

**[4083.76s] English:** Now, typically, if you were to do this clustering,  
**Translation:** Vocabulary: clustering: 聚类; clusters: 聚类

**[4087.18s] English:** you would perform clustering offline.  
**Translation:** 

**[4089.32s] English:** What that means is, if you have a dataset of n examples,  
**Translation:** Vocabulary: dataset: 数据集

**[4093.10s] English:** you would run over all of these n examples,  
**Translation:** 

**[4095.38s] English:** get features for them, perform clustering,  
**Translation:** 

**[4097.56s] English:** so basically get some clusters,  
**Translation:** 

**[4099.30s] English:** and then repeat the process again.  
**Translation:** 

**[4101.92s] English:** So this is offline basically because I need to do  
**Translation:** 

**[4103.98s] English:** one pass through the data to compute its clusters.  
**Translation:** 

**[4106.88s] English:** Suave is basically just a simple way of doing this online.  
**Translation:** 

**[4109.92s] English:** So as you're going through the data,  
**Translation:** Vocabulary: suave: 优雅

**[4111.82s] English:** you're actually computing these clusters online.  
**Translation:** 

**[4114.52s] English:** Of course, there is a lot of tricks involved in how to  
**Translation:** Vocabulary: computing: 计算

**[4117.72s] English:** do this in a robust manner without collapsing,  
**Translation:** 

**[4120.04s] English:** but this is the key idea to it.  
**Translation:** 

**[4122.38s] English:** Is there a nice way to say what is  
**Translation:** 

**[4124.38s] English:** the key methodology of the clustering that enables that?  
**Translation:** Vocabulary: methodology: 方法论

**[4127.36s] English:** Right. So the idea basically is that when you have n samples,  
**Translation:** 

**[4132.54s] English:** we assume that we have access to,  
**Translation:** 

**[4135.04s] English:** there are always k clusters in a dataset.  
**Translation:** 

**[4136.88s] English:** K is a fixed number.  
**Translation:** 

**[4137.90s] English:** So for example, k is 3,000.  
**Translation:** 

**[4139.90s] English:** So when you look at any small number of examples,  
**Translation:** 

**[4144.74s] English:** all of them must belong to one of these k clusters.  
**Translation:** 

**[4147.80s] English:** We impose this equi-partition constraint.  
**Translation:** Vocabulary: constraint: 限制条件

**[4150.30s] English:** What this means is that basically,  
**Translation:** 

**[4154.42s] English:** your entire set of n samples should be  
**Translation:** 

**[4157.24s] English:** equally partitioned into k clusters.  
**Translation:** 

**[4159.34s] English:** So all your k clusters have  
**Translation:** Vocabulary: partitioned: 划分

**[4160.64s] English:** equal contribution to these n samples.  
**Translation:** 

**[4164.20s] English:** This ensures that we never collapse.  
**Translation:** 

**[4166.32s] English:** So collapse can be viewed as  
**Translation:** 

**[4167.94s] English:** a way in which all samples belong to one cluster.  
**Translation:** 

**[4170.50s] English:** So if all features become the same,  
**Translation:** 

**[4173.06s] English:** then you have basically just one mega cluster.  
**Translation:** 

**[4175.16s] English:** You don't even have like 10 clusters or 3,000 clusters.  
**Translation:** 

**[4177.82s] English:** So SWAV basically ensures that at each point,  
**Translation:** 

**[4181.00s] English:** all these 3,000 clusters are being used in the clustering process.  
**Translation:** 

**[4184.82s] English:** That's it. Basically, just figure out how to do this online and again,  
**Translation:** 

**[4189.86s] English:** basically just make sure that two crops from  
**Translation:** 

**[4191.74s] English:** the same image belong to the same cluster and others don't.  
**Translation:** Vocabulary: cluster: 聚类

**[4195.34s] English:** The fact they have a fixed k makes things simpler.  
**Translation:** 

**[4198.66s] English:** Fixed k makes things simpler.  
**Translation:** 

**[4200.00s] English:** our clustering is not like really hard clustering it's soft clustering so basically you can be  
**Translation:** 

**[4204.78s] English:** point two to cluster number one and point eight to cluster number two so it's not really hard  
**Translation:** Vocabulary: clustering: 聚类

**[4209.26s] English:** so essentially even though we have like 3 000 clusters we can actually represent a lot of  
**Translation:** 

**[4214.20s] English:** clusters what is seer s-e-e-r and what are the key results and insights in the paper self-supervised  
**Translation:** Vocabulary: clusters: 聚类

**[4224.08s] English:** pre-training of visual features in the wild what is this big beautiful seer system seer so i'll  
**Translation:** 

**[4232.00s] English:** first go to suave because suave is actually like one of the key components for seer so suave was  
**Translation:** Vocabulary: suave: 优雅

**[4236.70s] English:** when we use suave it was demonstrated on image net so typically like self-supervised methods  
**Translation:** 

**[4242.48s] English:** the way we sort of operate is like in the research community we kind of cheat so we take image net  
**Translation:** 

**[4248.04s] English:** which of course i talked about as having lots of labels and then we throw away the labels like  
**Translation:** 

**[4253.12s] English:** throw away all the hard  
**Translation:** 

**[4254.06s] English:** work that went behind basically the labeling process and we pretend that it is self like  
**Translation:** 

**[4258.64s] English:** unsupervised but the problem here is that we have when like when we collected these images  
**Translation:** Vocabulary: labeling: 标注; unsupervised: 无监督

**[4264.28s] English:** the image net data set has a particular distribution of concepts right so these images are very curated  
**Translation:** 

**[4271.46s] English:** and what that means is these images of course belong to a certain set of noun concepts and also  
**Translation:** 

**[4278.12s] English:** image net has this bias that all images contain an object which is like very big and it's typically  
**Translation:** 

**[4283.08s] English:** in the center  
**Translation:** 

**[4283.66s] English:** mm-hmm  
**Translation:** 

**[4284.04s] English:** so when you're talking about a dog it's a well-framed dog it's towards the center of the image  
**Translation:** 

**[4288.20s] English:** so a lot of the data augmentation a lot of the sort of hidden assumptions and self-supervised  
**Translation:** 

**[4292.12s] English:** learning uh actually really uh exploit this bias of image net and so i mean a lot of my work a lot  
**Translation:** Vocabulary: assumptions: 假设; augmentation: 增强

**[4299.80s] English:** of work from other people always uses image net sort of as the benchmark to show the success of  
**Translation:** 

**[4304.20s] English:** self-supervised learning so you're implying that there's particular limitations to this kind of  
**Translation:** Vocabulary: benchmark: 衡量标准; implying: 暗示

**[4308.04s] English:** data set yes i mean it's basically because our data augmentation is that we designed uh like in the  
**Translation:** 

**[4314.04s] English:** like all data augmentation that we designed for self-supervised learning and vision are kind of  
**Translation:** 

**[4317.96s] English:** overfed to image net but yeah  
**Translation:** 

**[4320.00s] English:** you're saying a little bit hard-coded like the cropping exactly the cropping parameters the kind  
**Translation:** Vocabulary: cropping: 裁剪参数

**[4325.92s] English:** of lighting that we're using the kind of blurring that we're using yeah but you would uh for a more  
**Translation:** 

**[4330.64s] English:** in the wild data set you would need to be uh clever or more careful in setting the range of  
**Translation:** Vocabulary: blurring: 模糊处理

**[4336.96s] English:** parameters and those kinds of things so for seer our main goal was twofold one basically to move  
**Translation:** 

**[4342.48s] English:** away from image net for training uh so the images that we used were like uncurated images now  
**Translation:** Vocabulary: twofold: 双重的; uncurated: 未整理的

**[4347.76s] English:** there's a lot of debate whether they're actually curated or not but i'll talk about that later uh  
**Translation:** 

**[4352.32s] English:** but the idea was basically these are going to be random internet images uh that we are not going  
**Translation:** 

**[4357.12s] English:** to filter out based on like particular categories so we did not say that oh images that belong to  
**Translation:** 

**[4362.32s] English:** dogs and cats should be the only images that come in this data set banana and basically other images  
**Translation:** 

**[4369.28s] English:** should be thrown out so we didn't do any of that so these are random internet images and of course  
**Translation:** 

**[4374.32s] English:** it also goes back to like the problem of scale that you talked about so these  
**Translation:** 

**[4377.76s] English:** were basically about a billion or so images and for context image net uh the image net version  
**Translation:** 

**[4382.16s] English:** that we use was one million images earlier so this is basically going like three orders of magnitude  
**Translation:** 

**[4386.40s] English:** more the idea was basically to see if we can train a very large convolutional model in a  
**Translation:** 

**[4391.92s] English:** self-supervised way on this uncurated but really large set of images and how well would this model  
**Translation:** Vocabulary: convolutional: 卷积的

**[4397.44s] English:** do so is self-supervised learning really overfit to image net or or can it actually work in the wild  
**Translation:** 

**[4403.76s] English:** and it was also out of curiosity what kind of things will this model learn will it  
**Translation:** 

**[4407.76s] English:** actually be able to still figure out you know different types of objects and so on would there  
**Translation:** 

**[4412.24s] English:** be particular kinds of tasks it would actually do better than an image train model and so for seer  
**Translation:** 

**[4418.96s] English:** one of our main findings was that we can actually train very large models in a completely  
**Translation:** 

**[4423.76s] English:** self-supervised way on lots of internet images without really necessarily filtering them out  
**Translation:** 

**[4428.40s] English:** which was in itself a good thing because it's a fairly simple process right so you get images  
**Translation:** 

**[4432.96s] English:** which are uploaded and you basically can immediately use them to train a model in an  
**Translation:** 

**[4437.76s] English:** environment where you don't really need to sit and filter them out these images  
**Translation:** 

**[4440.00s] English:** Images can be cartoons, these can be memes,  
**Translation:** 

**[4442.06s] English:** these can be actual pictures uploaded by people,  
**Translation:** 

**[4444.50s] English:** and you don't really care about what these images are,  
**Translation:** 

**[4446.20s] English:** you don't even care about what concepts they contain.  
**Translation:** 

**[4448.56s] English:** So this was a very sort of simple setup.  
**Translation:** Vocabulary: setup: 布置

**[4450.32s] English:** What image selection mechanism would you say  
**Translation:** 

**[4452.92s] English:** is there like inherent in some aspect of the process?  
**Translation:** 

**[4458.88s] English:** So you're kind of implying that there's almost none,  
**Translation:** 

**[4461.34s] English:** but what is there, would you say,  
**Translation:** Vocabulary: implying: 暗示

**[4463.66s] English:** if you were to introspect?  
**Translation:** 

**[4465.00s] English:** Right, so it's not like, uncurated can basically,  
**Translation:** Vocabulary: introspect: 自我反省; uncurated: 未经筛选

**[4468.52s] English:** like one way of imagining uncurated is basically  
**Translation:** 

**[4470.86s] English:** you have like cameras that can take pictures  
**Translation:** 

**[4473.80s] English:** at random viewpoints.  
**Translation:** 

**[4475.24s] English:** When people upload pictures to the internet,  
**Translation:** Vocabulary: viewpoints: 随机视角

**[4477.44s] English:** they are typically going to care about the framing of it,  
**Translation:** 

**[4480.36s] English:** they're not going to upload, say,  
**Translation:** 

**[4481.90s] English:** the picture of a zoomed in wall, for example.  
**Translation:** 

**[4483.86s] English:** Well, when we say internet,  
**Translation:** 

**[4484.96s] English:** do you mean social networks?  
**Translation:** 

**[4486.14s] English:** Yes. Okay.  
**Translation:** 

**[4487.20s] English:** So these are not going to be like pictures  
**Translation:** 

**[4488.74s] English:** of like a zoomed in table or a zoomed in wall.  
**Translation:** 

**[4491.44s] English:** So it's not really completely uncurated  
**Translation:** 

**[4493.20s] English:** because people do have the like photographer's bias,  
**Translation:** 

**[4495.86s] English:** where they do want to keep things  
**Translation:** 

**[4497.08s] English:** towards the center a little bit,  
**Translation:** 

**[4498.50s] English:** or like really have like, you know,  
**Translation:** 

**[4500.16s] English:** nice looking things and so on in the picture.  
**Translation:** 

**[4502.54s] English:** So that's the kind of bias that typically exists  
**Translation:** 

**[4505.54s] English:** in this data set and also the user base, right?  
**Translation:** 

**[4507.60s] English:** You're not going to get lots of pictures  
**Translation:** 

**[4509.22s] English:** from different parts of the world  
**Translation:** 

**[4510.42s] English:** because there are certain parts of the world  
**Translation:** 

**[4512.00s] English:** where people may not actually be uploading  
**Translation:** Vocabulary: uploading: 上传

**[4514.20s] English:** a lot of pictures to the internet  
**Translation:** 

**[4515.32s] English:** or may not even have access to a lot of internet.  
**Translation:** 

**[4517.26s] English:** So this is a giant data set and a giant neural network.  
**Translation:** 

**[4521.64s] English:** I don't think we've talked about what architectures  
**Translation:** Vocabulary: neural: 神经网络

**[4524.68s] English:** work well for SSL, for self-supervised data.  
**Translation:** 

**[4528.50s] English:** What is self-supervised learning?  
**Translation:** 

**[4530.16s] English:** For SERE and for SWAB,  
**Translation:** 

**[4531.42s] English:** we were using convolutional networks,  
**Translation:** Vocabulary: convolutional: 卷积的

**[4533.12s] English:** but recently in a work called Dyno,  
**Translation:** 

**[4534.88s] English:** we've basically started using transformers for vision.  
**Translation:** 

**[4537.46s] English:** Both seem to work really well,  
**Translation:** 

**[4539.26s] English:** ConNets and transformers,  
**Translation:** 

**[4540.50s] English:** and depending on what you want to do,  
**Translation:** 

**[4541.84s] English:** you might choose to use a particular formulation.  
**Translation:** 

**[4544.26s] English:** So for SERE, it was a ConvNet.  
**Translation:** 

**[4546.00s] English:** It was particularly a RegNet model,  
**Translation:** 

**[4548.16s] English:** which was also work from Facebook.  
**Translation:** 

**[4550.38s] English:** RegNets are like really good when it comes to compute  
**Translation:** 

**[4553.26s] English:** versus like accuracy.  
**Translation:** 

**[4555.46s] English:** So because it was a very efficient model,  
**Translation:** 

**[4557.56s] English:** compute and memory,  
**Translation:** 

**[4558.26s] English:** it was efficient and  
**Translation:** 

**[4560.00s] English:** basically it worked really well in terms of scaling so we used a very large regnet model  
**Translation:** 

**[4564.14s] English:** and trained it on the built-in images can you maybe quickly comment on what reg nets are  
**Translation:** 

**[4568.34s] English:** uh it comes from this paper designing network design spaces right it's just super interesting  
**Translation:** 

**[4574.42s] English:** concept that emphasizes on how to create efficient neural networks right large neural networks so  
**Translation:** 

**[4579.68s] English:** one of the sort of key takeaways from this paper which the authors like whenever you hear them  
**Translation:** 

**[4583.34s] English:** present this work they keep saying is a lot of neural networks are characterized in terms of  
**Translation:** Vocabulary: takeaways: 主要收获

**[4588.42s] English:** flops right flops basically being the floating point operations and people really love to use  
**Translation:** 

**[4592.58s] English:** flops to say this model is like really computationally heavy or like our model is  
**Translation:** Vocabulary: computationally: 计算上; flops: 浮点运算

**[4597.14s] English:** computationally cheap and so on now it turns out that flops are really not a good indicator of how  
**Translation:** 

**[4602.38s] English:** well a particular network is like how efficient it is really and what a better indicator is is  
**Translation:** 

**[4608.10s] English:** the activation or the memory that is being used by this particular model and so designing like  
**Translation:** 

**[4613.94s] English:** one of the key findings from this paper was basically that you need to design network families  
**Translation:** 

**[4618.14s] English:** and you need to design network families and you need to design network families  
**Translation:** 

**[4618.42s] English:** or neural network architectures that are actually very efficient in the memory space as well not  
**Translation:** 

**[4622.92s] English:** just in terms of pure flops so regnet is basically a network architecture family that came out of this  
**Translation:** 

**[4628.20s] English:** paper that is particularly good at both flops and the sort of memory required for it and of course  
**Translation:** 

**[4633.80s] English:** it builds upon like a earlier work like resnet being like the sort of more popular inspiration  
**Translation:** 

**[4638.44s] English:** for it where you have residual connections but one of the things in this work is basically they  
**Translation:** Vocabulary: residual: 剩余的

**[4642.40s] English:** also use like squeeze excitation blocks so it's a lot of nice sort of technical innovation in all of  
**Translation:** 

**[4647.32s] English:** this uh from prior work and then you can see that the network architecture family is basically a  
**Translation:** Vocabulary: excitation: 激发

**[4648.14s] English:** prior work and a lot of the ingenuity of these particular authors in how to combine these  
**Translation:** 

**[4652.42s] English:** multiple building blocks but the key constraint was optimized for both flops and memory when you're  
**Translation:** Vocabulary: constraint: 约束; ingenuity: 创造力; optimized: 优化

**[4657.54s] English:** basically doing this don't just look at flops and that allows you to what have a sort of have very  
**Translation:** 

**[4663.14s] English:** large networks through this process uh can optimize for low like for efficiency right also in just in  
**Translation:** Vocabulary: optimize: 优化

**[4671.94s] English:** terms of pure hardware they fit very well on gpu memory yeah so they can be like really powerful  
**Translation:** 

**[4677.22s] English:** neural network architectures they can be like really powerful neural network architectures  
**Translation:** Vocabulary: neural: 神经的

**[4678.14s] English:** with lots of parameters lots of flops  
**Translation:** 

**[4680.00s] English:** but also because they're like efficient in terms of the amount of memory that they're using you can  
**Translation:** 

**[4684.16s] English:** actually fit a lot of these on like you can fit a very large model on a single gpu for example  
**Translation:** 

**[4689.44s] English:** would you say that the choice of uh architecture matters more than the choice of maybe data  
**Translation:** 

**[4696.80s] English:** augmentation techniques is is there a possibility to say what matters more you kind of imply that  
**Translation:** 

**[4702.88s] English:** you can probably go really far with just using basic conv nets all right i think data like data  
**Translation:** Vocabulary: augmentation: 增加

**[4709.60s] English:** and data augmentation the algorithm being used for the self-supervised training matters a lot  
**Translation:** 

**[4713.84s] English:** more than the particular kind of architecture with different types of architecture you get different  
**Translation:** Vocabulary: algorithm: 算法

**[4718.56s] English:** like properties in the resulting sort of representation but really i mean the secret  
**Translation:** 

**[4723.20s] English:** sauce is in the data augmentation and the algorithm being used to train them  
**Translation:** 

**[4726.88s] English:** the architectures i mean at this point a lot of them perform very similarly uh depending on like  
**Translation:** 

**[4732.16s] English:** the particular task that you care about they have certain advantages and disadvantages is there  
**Translation:** 

**[4736.64s] English:** something interesting to be said about what it takes with the data augmentation techniques  
**Translation:** 

**[4739.60s] English:** sears to train a giant neural network you're talking about a huge amount of data a huge  
**Translation:** 

**[4744.66s] English:** neural network is there something interesting to be said of how to effectively train something like  
**Translation:** 

**[4749.62s] English:** that fast lots of gpos okay so i mean so the model was like a billion parameters yeah uh and it was  
**Translation:** 

**[4759.22s] English:** trained on a billion images yeah so if like basically the same number of parameters as the  
**Translation:** 

**[4763.60s] English:** number of images and it took a while uh i don't remember the exact number it's in the paper uh  
**Translation:** 

**[4768.54s] English:** but it took a while i guess i'm trying to get at is uh when you're thinking of scaling this kind  
**Translation:** 

**[4778.20s] English:** of thing i mean one of the exciting possibilities of self-supervised learning is the several orders  
**Translation:** 

**[4785.28s] English:** of magnitude scaling of everything both both the neural network and the size of the data  
**Translation:** 

**[4790.14s] English:** and so the question is do you think there are some interesting tricks to do large-scale  
**Translation:** 

**[4796.76s] English:** distributed compute or is it  
**Translation:** 

**[4798.54s] English:** or is that really outside  
**Translation:** 

**[4800.00s] English:** even deep learning that's more about like hardware engineering i think more and more there is like  
**Translation:** 

**[4805.84s] English:** this a lot of like systems uh are designed basically taking into account the machine  
**Translation:** 

**[4811.60s] English:** learning needs right so yeah because when whenever you're doing this kind of distributed training  
**Translation:** 

**[4815.36s] English:** there is a lot of intercommunication between nodes so like gradients or the model parameters are  
**Translation:** Vocabulary: gradients: 梯度; intercommunication: 节点间通信

**[4819.60s] English:** being passed so you really want to minimize communication costs when you really want to  
**Translation:** 

**[4823.36s] English:** scale these models up uh you want basically to be able to do as much like as limited amount of  
**Translation:** 

**[4830.24s] English:** communication as possible so currently like a dominant paradigm is synchronized uh sort of  
**Translation:** 

**[4834.40s] English:** training so essentially after every sort of gradient step all you basically have like a  
**Translation:** Vocabulary: gradient: 梯度; paradigm: 范式; synchronized: 同步

**[4840.24s] English:** synchronization step between all the sort of uh compute chips that you're going on with  
**Translation:** 

**[4845.52s] English:** i think asynchronous training was popular but it doesn't seem to perform as well  
**Translation:** Vocabulary: asynchronous: 非同步; synchronization: 同步

**[4850.24s] English:** but in general i think that's sort of the  
**Translation:** 

**[4853.36s] English:** i guess it's all outside my scope as well yeah but well the main thing is like minimize the  
**Translation:** 

**[4858.64s] English:** amount of uh synchronization steps that you have yeah that has been the key takeaway at least in my  
**Translation:** 

**[4863.84s] English:** experience the others i have no idea about how to design the chip yeah there's very few things that  
**Translation:** Vocabulary: takeaway: 主要收获

**[4868.56s] English:** i see uh jim killer's eyes light up as much as talking about giant computers doing um like that  
**Translation:** 

**[4875.84s] English:** fast communication that you're talking to well when they're training machine learning uh systems  
**Translation:** 

**[4881.12s] English:** what is vissel v-i-s  
**Translation:** 

**[4883.36s] English:** s-l the uh pytorch based ssl library what are the use cases that you might have whistle basically  
**Translation:** 

**[4890.80s] English:** was born out of a lot of us at facebook doing the self-supervised learning research so it's a common  
**Translation:** 

**[4895.92s] English:** framework uh in which we have like a lot of self-supervised learning methods implemented  
**Translation:** 

**[4900.40s] English:** for vision uh it's also it has in itself like a benchmark of tasks that you can evaluate the  
**Translation:** 

**[4906.72s] English:** self-supervised representations on so the use case for it is basically for anyone who's either trying  
**Translation:** Vocabulary: benchmark: 衡量标准; evaluate: 评估

**[4913.36s] English:** to develop a self-supervised model or train their self-supervised model or a researcher who's trying  
**Translation:** 

**[4917.92s] English:** to build a new self-supervised technique  
**Translation:** 

**[4920.00s] English:** to be all of these things uh so as a researcher before whistle for example or like when we started  
**Translation:** 

**[4925.18s] English:** doing this work fairly seriously at facebook it was very hard for us to go and implement every  
**Translation:** 

**[4930.26s] English:** self-supervised learning model test it out in a like sort of consistent manner the experimental  
**Translation:** 

**[4935.28s] English:** setup was very different across different groups uh even when someone said that they were reporting  
**Translation:** Vocabulary: setup: 实验设置

**[4940.34s] English:** image net accuracy it could mean lots of different things so with whistle we tried to really sort of  
**Translation:** 

**[4944.66s] English:** standardize that as much as possible and there was a paper like we did in 2019 just about benchmarking  
**Translation:** Vocabulary: benchmarking: 基准测试; standardize: 标准化

**[4949.34s] English:** and so whistle basically builds upon a lot of like this kind of work that we did about like  
**Translation:** 

**[4954.06s] English:** benchmarking and then every time we try to like we come up with a self-supervised learning method  
**Translation:** 

**[4958.82s] English:** a lot of us try to push that into whistle as well just so that it basically is like the central  
**Translation:** 

**[4962.96s] English:** piece where a lot of these methods can reside just out of curiosity people may be um so certainly  
**Translation:** Vocabulary: reside: 存在

**[4969.72s] English:** outside of facebook but just researchers or just even people that know how to program in python  
**Translation:** 

**[4974.76s] English:** and know how to use pytorch uh what would be the use case what would be a  
**Translation:** 

**[4979.18s] English:** fundamental use case for people who are using python and know how to use pytorch  
**Translation:** 

**[4979.32s] English:** thing to play around with whistle on like what's a fun thing to play around with self-supervised  
**Translation:** 

**[4985.42s] English:** learning on would you say is there a good hello world program like is is it always about big size  
**Translation:** 

**[4992.14s] English:** that's important to have or is there fun little smaller case playgrounds to play around with so  
**Translation:** 

**[4999.88s] English:** we're trying to like uh push something towards that i think there are a few setups out there  
**Translation:** 

**[5004.24s] English:** but nothing like super standard on the smaller scale i mean image net in itself is actually  
**Translation:** Vocabulary: setups: 设置

**[5008.38s] English:** pretty big also  
**Translation:** 

**[5009.16s] English:** so that is not something which is like feasible for a lot of people but we are trying to like push  
**Translation:** Vocabulary: feasible: 可行的

**[5014.66s] English:** up with like smaller sort of use cases the thing is uh at a smaller scale a lot of the observations  
**Translation:** 

**[5020.14s] English:** or a lot of the algorithms that work don't necessarily translate into the medium or the  
**Translation:** 

**[5023.96s] English:** larger scale so it's really tricky to come up with a good small scale setup where a lot of  
**Translation:** 

**[5027.96s] English:** your empirical observations will really translate to uh the other setup so it's been really  
**Translation:** Vocabulary: empirical: 经验的

**[5032.04s] English:** challenging uh i've been trying to do that for a little bit as well because it does take time  
**Translation:** 

**[5035.74s] English:** to train stuff on image net it does take time to train on like more more images but it's really  
**Translation:** 

**[5039.16s] English:** easy to take out of a space to like make those overcast shapes like some sort of��  
**Translation:** 

**[5062.98s] English:** ��게요  
**Translation:** Vocabulary: overcast: 阴天

**[5065.06s] English:** áis  
**Translation:** 

**[5068.60s] English:** um  
**Translation:** 

**[5069.02s] English:** h  
**Translation:** 

**[5069.04s] English:** h  
**Translation:** 

**[5069.14s] English:** h  
**Translation:** 

**[5040.00s] English:** But pretty much every time I've tried to do that, it's been unsuccessful because all the observations I draw from my set of experiments on a smaller data set don't translate into ImageNet or don't translate into another sort of data set.  
**Translation:** Vocabulary: unsuccessful: 不成功

**[5051.78s] English:** So it's been hard for us to figure this one out, but it's an important problem.  
**Translation:** 

**[5055.20s] English:** So there's this really interesting idea of learning across multiple modalities.  
**Translation:** Vocabulary: modalities: 多种感知方式

**[5059.86s] English:** You have a CVPR 2021 best paper candidate titled Audiovisual Instance Discrimination with Cross-Modal Agreement.  
**Translation:** 

**[5071.18s] English:** What are the key results, insights in this paper, and what can you say in general about the promise and power of multimodal learning?  
**Translation:** Vocabulary: audiovisual: 视听; multimodal: 多模态

**[5077.60s] English:** For this paper, it actually came as a little bit of a shock to me at how well it worked, so I can describe what the problem setup was.  
**Translation:** 

**[5083.86s] English:** So it's been used in the past by lots of folks, like, for example, Andrew Owens from MIT, Alyosha Efros from Berkeley.  
**Translation:** Vocabulary: alyosha: 艾利奥沙; berkeley: 伯克利; setup: 设置

**[5089.86s] English:** And Rosa Sermon from Oxford.  
**Translation:** 

**[5091.14s] English:** So a lot of these people have been sort of showing results in this.  
**Translation:** Vocabulary: sermon: 布道演说

**[5094.06s] English:** Of course, I was aware of this result, but I wasn't really sure how well it would work in practice for, like, other sort of downstream tasks.  
**Translation:** 

**[5100.58s] English:** So the results kept getting better, and I wasn't sure if, like, a lot of our insights from self-supervised learning would translate into this multimodal learning problem.  
**Translation:** 

**[5108.28s] English:** So multimodal learning is when you have, like, when you have multiple modalities.  
**Translation:** 

**[5115.08s] English:** That's not even close.  
**Translation:** 

**[5116.96s] English:** Okay, so the particular modalities that we work with.  
**Translation:** 

**[5119.86s] English:** On in this work were audio and video.  
**Translation:** 

**[5122.02s] English:** So the idea was basically if you have a video, you have its corresponding audio track, and you want to use both of these signals, the audio signal and the video signal, to learn a good representation for video and good representation for audio.  
**Translation:** 

**[5132.62s] English:** Like this podcast.  
**Translation:** 

**[5133.68s] English:** Like this podcast.  
**Translation:** 

**[5134.62s] English:** Exactly.  
**Translation:** 

**[5135.46s] English:** So what we did in this work was basically train two different neural networks, one on the video signal, one on the audio signal.  
**Translation:** 

**[5141.94s] English:** And what we wanted is basically the features that we get from both of these neural networks should be similar.  
**Translation:** Vocabulary: neural: 神经网络

**[5146.38s] English:** Yeah.  
**Translation:** 

**[5146.76s] English:** So it should basically be able to produce the same kinds of features.  
**Translation:** 

**[5149.86s] English:** From the video and the same kinds of features from the audio.  
**Translation:** 

**[5152.74s] English:** Now, why is this useful?  
**Translation:** 

**[5153.76s] English:** Well, for a lot of these objects that we have, there is a characteristic sound, right?  
**Translation:** 

**[5157.78s] English:** So trains, when they go by, they make a particular sound.  
**Translation:** Vocabulary: characteristic: 特征的

**[5160.00s] English:** kind of sound boats make a particular kind of sound people when they're jumping around will  
**Translation:** 

**[5163.98s] English:** like shout whatever bananas don't make a sound so well you can't learn anything about bananas there  
**Translation:** 

**[5169.14s] English:** or when humans mention bananas well yes when they say the word banana then so you can't trust  
**Translation:** 

**[5174.30s] English:** basically anything that comes out of a human's mouth as a source that source of audio is useless  
**Translation:** 

**[5178.74s] English:** so the typical use case is basically like for example someone playing a musical instrument  
**Translation:** 

**[5182.30s] English:** so guitars have a particular kind of sound and so on so because a lot of these things are correlated  
**Translation:** Vocabulary: correlated: 相关联的

**[5186.76s] English:** the idea in multimodal learning is to take these two kinds of modalities video and audio  
**Translation:** 

**[5190.88s] English:** and learn a common embedding space a common feature space where both of these related  
**Translation:** Vocabulary: embedding: 嵌入; modalities: 模态

**[5195.50s] English:** modalities can basically be close together and again you use contrastive learning for this  
**Translation:** 

**[5200.26s] English:** so in contrastive learning basically the video and the corresponding audio are positives and  
**Translation:** Vocabulary: positives: 正样本

**[5205.62s] English:** you can take any other video or any other audio and that becomes a negative and so basically that's  
**Translation:** 

**[5210.86s] English:** it it's just a simple application of contrastive learning the main sort of finding from this work  
**Translation:** 

**[5215.30s] English:** for us  
**Translation:** 

**[5215.66s] English:** was basically that you can actually learn very very powerful feature representations very very  
**Translation:** 

**[5221.14s] English:** powerful video representations so you can learn the sort of video network that we ended up learning  
**Translation:** 

**[5226.22s] English:** can actually be used for downstream for for example recognizing human actions or recognizing  
**Translation:** 

**[5231.64s] English:** different types of sounds for example so this was sort of the key finding can you give kind of an  
**Translation:** 

**[5238.78s] English:** example of a human action or like just so we can build up intuition of what kind of thing right so  
**Translation:** Vocabulary: intuition: 直觉

**[5244.70s] English:** there is a  
**Translation:** 

**[5245.66s] English:** this data set called kinetics for example which has like 400 different types of human actions so  
**Translation:** Vocabulary: kinetics: 动能数据集

**[5249.40s] English:** people jumping people you know doing different kinds of sports or different types of swimming  
**Translation:** 

**[5253.96s] English:** so like different strokes and swimming uh golf and so on so there are like just different types  
**Translation:** 

**[5259.14s] English:** of actions right there and the point is this kind of video network that you learn in a self-supervised  
**Translation:** 

**[5263.76s] English:** way can be used very easily to kind of recognize these different types of actions uh it can also  
**Translation:** 

**[5269.36s] English:** be used for recognizing different types of objects uh and what we did is we tried to visualize whether  
**Translation:** 

**[5274.92s] English:** the network can  
**Translation:** Vocabulary: visualize: 可视化

**[5275.58s] English:** figure out where the sound is coming from so basically give it a video and  
**Translation:** 

**[5280.00s] English:** basically play of say of a person just strumming a guitar but of course there is no audio in this  
**Translation:** Vocabulary: strumming: 弹拨

**[5284.56s] English:** and now you give it this sound of a guitar and you ask like basically try to visualize where  
**Translation:** 

**[5288.88s] English:** the network is where the network thinks the sound is coming from and it can kind of basically draw  
**Translation:** 

**[5293.84s] English:** like when you visualize it you can see that it's basically focusing on the guitar yeah that's so  
**Translation:** 

**[5298.16s] English:** and the same thing uh for example for certain people's voices like famous celebrities voices  
**Translation:** 

**[5302.80s] English:** it can actually figure out where their like where their mouth is so it can actually distinguish  
**Translation:** 

**[5307.12s] English:** different uh people's voices for example a little bit as well without that ever being uh annotated  
**Translation:** Vocabulary: annotated: 标注过的

**[5312.88s] English:** in any way right so this is all what it had discovered we never like we never pointed out  
**Translation:** 

**[5317.20s] English:** that this is a guitar and this is the kind of sound it produces it can actually naturally  
**Translation:** 

**[5320.80s] English:** figure that out because it's seen so many correlations of this sound coming with this  
**Translation:** 

**[5324.72s] English:** kind of like an object that it basically learns to associate this sound with this kind of an object  
**Translation:** Vocabulary: correlations: 相关性

**[5329.92s] English:** yeah that's that's really fascinating right that's really interesting so the idea with this kind of  
**Translation:** 

**[5334.72s] English:** network is then you then fine-tune it for a particular  
**Translation:** 

**[5337.12s] English:** task right so this is forming like a really good knowledge base within a neural network based on  
**Translation:** 

**[5343.28s] English:** which you could then train a little bit more to accomplish a specific task well exactly so you  
**Translation:** Vocabulary: neural: 神经网络

**[5349.28s] English:** don't need a lot of videos of humans doing actions annotated you can just use a few of them to  
**Translation:** 

**[5353.92s] English:** basically get your recognition how much insight do you draw from the fact that you can figure out  
**Translation:** 

**[5359.52s] English:** um where the sound is coming from i'm trying to see so that's kind of very it's very cvp  
**Translation:** 

**[5367.12s] English:** are beautiful right it's it's a cool little insight i wonder how profound that is you know  
**Translation:** Vocabulary: profound: 深奥

**[5374.16s] English:** does it speak to the idea that uh multiple modalities are somehow much bigger than the  
**Translation:** 

**[5382.56s] English:** sum of their parts or is it really really useful to have multiple modalities or is it just that  
**Translation:** Vocabulary: modalities: 多种表现形式

**[5388.64s] English:** cool thing that there's parts of our world that are uh can be revealed uh like um effectively  
**Translation:** 

**[5397.12s] English:** through multiple modalities but most of it is really  
**Translation:** 

**[5400.00s] English:** all about vision or about one of the modalities i would say a little um tending more towards the  
**Translation:** 

**[5407.32s] English:** second part so most of it can be sort of figured out with one modality but having an extra modality  
**Translation:** Vocabulary: modality: 检查方式

**[5411.98s] English:** always helps you yeah so in this case for example like one uh thing is when you're if you observe  
**Translation:** 

**[5418.26s] English:** someone cutting something and you don't have any sort of sound there whether it's an apple or  
**Translation:** 

**[5423.76s] English:** whether it's an onion it's very hard to figure that out but if you hear someone cutting it it's  
**Translation:** 

**[5428.42s] English:** very easy to figure it out because apples and onions make a very different kind of uh different  
**Translation:** 

**[5432.62s] English:** kind of characteristic sound when they're cut yeah so you really figure this out based on audio it's  
**Translation:** 

**[5437.06s] English:** much easier so your life will become much easier when you have access to different kinds of  
**Translation:** Vocabulary: characteristic: 特征

**[5441.32s] English:** modalities and the other thing is so i like to relate it in this way it may be like completely  
**Translation:** 

**[5445.98s] English:** wrong but uh the distributional hypothesis in nlp right where context basically gives kind of  
**Translation:** Vocabulary: distributional: 分布假设; hypothesis: 假设

**[5451.54s] English:** meaning to that word sound kind of does that too right so if you have the same sound so that's the  
**Translation:** 

**[5457.66s] English:** same context  
**Translation:** 

**[5458.42s] English:** across different videos you're very likely to be observing the same kind of concept yeah so that's  
**Translation:** 

**[5463.30s] English:** the kind of reason why it figures out the guitar thing right it'll observe the same sound across  
**Translation:** 

**[5468.58s] English:** multiple different videos and it figures out maybe this is the common factor that's actually doing it  
**Translation:** 

**[5473.14s] English:** i wonder i used to have this argument with my dad a bunch  
**Translation:** 

**[5477.46s] English:** for creating general intelligence whether uh smell is an important uh like if if that's  
**Translation:** 

**[5483.94s] English:** important sensory information mostly we're talking about like falling in love with an  
**Translation:** 

**[5487.78s] English:** ai system  
**Translation:** 

**[5488.42s] English:** and for for him smell and touch are important and i was arguing that it's not at all it's important  
**Translation:** 

**[5494.30s] English:** it's nice and everything but like you can fall in love with just language really but voice is very  
**Translation:** 

**[5499.66s] English:** powerful and vision is next and smell is not that important can i ask you about this process of uh  
**Translation:** 

**[5505.96s] English:** active learning you mentioned interactivity right is there some value within the self-supervised  
**Translation:** 

**[5515.58s] English:** learning context to select  
**Translation:** 

**[5518.42s] English:** parts of the data  
**Translation:** 

**[5520.00s] English:** in intelligent ways such that they would most benefit the learning process right so i think so  
**Translation:** 

**[5527.42s] English:** i think i mean i know i'm talking to an active learning fan here so of course i know the answer  
**Translation:** 

**[5531.98s] English:** first you're talking bananas and now you're talking about active learning i love it  
**Translation:** 

**[5536.08s] English:** i think gianna coon told me that active learning is not that interesting  
**Translation:** 

**[5539.58s] English:** i and i think i would back back then i didn't want to argue with him too much but when we talk again  
**Translation:** Vocabulary: gianna: 乔安娜

**[5545.54s] English:** that's we're going to spend three hours arguing about active learning my sense was you can go  
**Translation:** 

**[5549.78s] English:** extremely far with active learning you know perhaps farther than anything else like the  
**Translation:** 

**[5555.28s] English:** to me there's this kind of intuition that similar to data augmentation you can get a lot  
**Translation:** 

**[5562.28s] English:** from the data from intelligent optimized usage of the data right i i'm trying to speak generally  
**Translation:** Vocabulary: augmentation: 数据扩增; intuition: 直觉; optimized: 优化

**[5572.46s] English:** in such a way that includes data augmentation and active learning that there's something about  
**Translation:** 

**[5578.32s] English:** maybe interactive exploration  
**Translation:** Vocabulary: interactive: 交互式

**[5579.76s] English:** of the data that um at least this part of the solution to intelligence like an important part  
**Translation:** 

**[5586.42s] English:** i don't know what your thoughts are on active learning in general i actually really like active  
**Translation:** 

**[5590.60s] English:** learning so back in the day we did this largely ignored cvpr paper called learning by asking  
**Translation:** 

**[5595.52s] English:** questions so the idea was basically you would train an agent that would ask a question about  
**Translation:** 

**[5599.38s] English:** the image it would get an answer and basically then it would update itself it would see the  
**Translation:** 

**[5603.92s] English:** next image it would decide what's the next hardest question that i can ask to learn the most  
**Translation:** 

**[5608.14s] English:** and the idea was basically to train an agent that would ask a question about the image and  
**Translation:** 

**[5609.76s] English:** basically because it was being smart about the kinds of questions it was asking it would learn  
**Translation:** 

**[5614.10s] English:** in fewer samples it would be more efficient at using data and we did find to some extent that  
**Translation:** 

**[5619.52s] English:** it was actually better than randomly asking questions kind of weird thing about active  
**Translation:** 

**[5623.16s] English:** learning is it's also a chicken and egg problem because when you look at an image to ask a good  
**Translation:** 

**[5627.80s] English:** question about the image you need to understand something about the image right you can't ask a  
**Translation:** 

**[5631.48s] English:** completely arbitrarily random question it may not even apply to that particular image so there is  
**Translation:** 

**[5635.92s] English:** some amount of understanding or knowledge that basically keeps getting built when you're doing  
**Translation:** 

**[5639.76s] English:** that  
**Translation:** 

**[5640.00s] English:** So, I think active learning by itself is really good.  
**Translation:** 

**[5644.78s] English:** And the main thing we need to figure out is basically how do we come up with a technique  
**Translation:** 

**[5649.64s] English:** to first model what the model knows and also model what the model does not know.  
**Translation:** 

**[5656.02s] English:** I think that's the sort of beauty of it, right?  
**Translation:** 

**[5658.68s] English:** Because when you know that there are certain things that you don't know anything about,  
**Translation:** 

**[5662.34s] English:** asking a question about those concepts is actually going to bring you the most value.  
**Translation:** 

**[5666.56s] English:** I think that's the sort of key challenge.  
**Translation:** 

**[5668.46s] English:** Now, self-supervised learning by itself, like selecting data for it and so on, that's actually  
**Translation:** 

**[5671.84s] English:** really useful.  
**Translation:** Vocabulary: selecting: 选择数据

**[5672.84s] English:** But I think that's a very narrow view of looking at active learning, right?  
**Translation:** 

**[5675.14s] English:** If you look at it more broadly, it is basically about if the model has a knowledge about N  
**Translation:** 

**[5680.40s] English:** concepts and it is weak basically about certain things.  
**Translation:** 

**[5683.96s] English:** So it needs to ask questions either to discover new concepts or to basically increase its  
**Translation:** 

**[5688.88s] English:** knowledge about these N concepts.  
**Translation:** 

**[5690.22s] English:** So at that level, it's a very powerful technique.  
**Translation:** 

**[5693.18s] English:** I actually do think it's going to be really useful.  
**Translation:** 

**[5696.78s] English:** Even in simple things such as data.  
**Translation:** 

**[5698.44s] English:** Data labeling, it's super useful.  
**Translation:** 

**[5700.40s] English:** So here is like one simple way that you can use active learning.  
**Translation:** Vocabulary: labeling: 标注

**[5704.38s] English:** For example, you have your self-supervised model, which is very good at predicting similarities  
**Translation:** 

**[5708.72s] English:** and dissimilarities between things.  
**Translation:** 

**[5710.92s] English:** And so if you label a picture as basically, say, a banana, now you know that all the images  
**Translation:** 

**[5717.68s] English:** that are very similar to this image are also likely to contain bananas.  
**Translation:** 

**[5721.64s] English:** So probably when you want to understand what else is a banana, you're not going to use  
**Translation:** 

**[5725.92s] English:** these other images.  
**Translation:** 

**[5726.92s] English:** You're actually going to use an image.  
**Translation:** 

**[5727.82s] English:** You're actually going to use an image that is not completely dissimilar, but somewhere  
**Translation:** 

**[5731.84s] English:** in between, which is not super similar to this image, but not super dissimilar either.  
**Translation:** 

**[5735.78s] English:** And that's going to tell you a lot more about what this concept of a banana is.  
**Translation:** 

**[5739.64s] English:** So that's kind of a heuristic.  
**Translation:** 

**[5741.88s] English:** I wonder if it's possible to also learn ways to discover the most likely, the most beneficial  
**Translation:** Vocabulary: heuristic: 启发式方法

**[5752.34s] English:** image.  
**Translation:** 

**[5753.64s] English:** So not just looking at a thing that's somewhat similar to a banana.  
**Translation:** 

**[5756.66s] English:** Yeah.  
**Translation:** 

**[5757.82s] English:** It's not just looking at a thing that's somewhat similar to a banana, but not exactly similar.  
**Translation:** 

**[5760.00s] English:** but have some kind of more complicated learning system,  
**Translation:** 

**[5763.58s] English:** like learned discovery mechanism  
**Translation:** 

**[5767.10s] English:** that tells you what image to look for.  
**Translation:** 

**[5769.46s] English:** Like how, yeah, like actually in a self-supervised way,  
**Translation:** 

**[5774.38s] English:** learning strictly a function that says,  
**Translation:** 

**[5777.32s] English:** is this image going to be very useful to me  
**Translation:** 

**[5780.60s] English:** given what I currently know?  
**Translation:** 

**[5782.16s] English:** I think there is a lot of synergy there.  
**Translation:** Vocabulary: synergy: 协同效应

**[5784.04s] English:** It's just, I think, yeah, it's going to be explored.  
**Translation:** 

**[5787.70s] English:** I think very much related to that,  
**Translation:** 

**[5789.42s] English:** I kind of think of what Tesla Autopilot is doing  
**Translation:** 

**[5793.64s] English:** currently as kind of active learning.  
**Translation:** 

**[5796.90s] English:** There's something that Andrej Kapati and their team  
**Translation:** 

**[5799.28s] English:** are calling a data engine.  
**Translation:** 

**[5801.30s] English:** Yes.  
**Translation:** 

**[5802.14s] English:** So you're basically deploying a bunch of instantiations  
**Translation:** Vocabulary: deploying: 部署; instantiations: 实例化

**[5805.68s] English:** of a neural network into the wild,  
**Translation:** 

**[5807.82s] English:** and they're collecting a bunch of edge cases  
**Translation:** 

**[5810.70s] English:** that are then sent back for annotation for particular,  
**Translation:** 

**[5814.00s] English:** and edge cases as defined as near failure  
**Translation:** Vocabulary: annotation: 注释

**[5816.74s] English:** or some weirdness  
**Translation:** 

**[5818.80s] English:** on a particular task that's then sent back.  
**Translation:** Vocabulary: weirdness: 怪异情况

**[5821.42s] English:** It's that, not exactly a banana,  
**Translation:** 

**[5824.02s] English:** but almost a banana cases sent back for annotation.  
**Translation:** 

**[5827.26s] English:** And then there's this loop that keeps going  
**Translation:** 

**[5829.22s] English:** and you keep retraining and retraining.  
**Translation:** 

**[5831.62s] English:** And the active learning step there,  
**Translation:** 

**[5833.30s] English:** or whatever you want to call it,  
**Translation:** 

**[5834.82s] English:** is the cars themselves that are sending you back the data.  
**Translation:** 

**[5839.12s] English:** Like what the hell happened here?  
**Translation:** 

**[5840.78s] English:** This was weird.  
**Translation:** 

**[5842.84s] English:** What are your thoughts about that sort of deployment  
**Translation:** Vocabulary: deployment: 部署

**[5846.46s] English:** of neural networks in the wild?  
**Translation:** 

**[5848.80s] English:** I think it's great to ask a question.  
**Translation:** 

**[5850.80s] English:** First is your thoughts, and maybe if you want to comment,  
**Translation:** 

**[5853.86s] English:** is there applications for autonomous driving,  
**Translation:** Vocabulary: autonomous: 自主

**[5856.98s] English:** like computer vision-based autonomous driving,  
**Translation:** 

**[5860.18s] English:** applications of self-supervised learning  
**Translation:** 

**[5862.08s] English:** in the context of computer vision-based autonomous driving?  
**Translation:** 

**[5867.56s] English:** So I think so.  
**Translation:** 

**[5868.40s] English:** I think for self-supervised learning to be used  
**Translation:** 

**[5870.08s] English:** in autonomous driving, there are lots of opportunities.  
**Translation:** 

**[5871.82s] English:** I mean, just like pure consistency in predictions  
**Translation:** 

**[5874.90s] English:** is one way, right?  
**Translation:** 

**[5875.86s] English:** So because you have this nice,  
**Translation:** 

**[5878.46s] English:** nice sequence of,  
**Translation:** 

**[5880.00s] English:** data that is coming in a video stream of it associated of course with the actions that say  
**Translation:** 

**[5884.40s] English:** the car took you can form a very nice predictive model of what's happening so for example like all  
**Translation:** Vocabulary: predictive: 预测性的

**[5889.82s] English:** the way uh like one way possibly in which how they're figuring out what data to get labeled  
**Translation:** 

**[5895.34s] English:** is basically through prediction uncertainty right so you predict that the car was going to turn  
**Translation:** 

**[5899.92s] English:** right so this was the action that was going to happen say in the shadow mode and now the driver  
**Translation:** 

**[5903.88s] English:** turned left and this was this is a really big surprise so basically by forming these good  
**Translation:** 

**[5908.94s] English:** predictive models you are i mean these are kind of self-supervised models right prediction models  
**Translation:** 

**[5913.42s] English:** are basically being trained just by looking at what's going to happen next and asking them to  
**Translation:** 

**[5917.42s] English:** predict what's going to happen next so i would say this is really like one use of self-supervised  
**Translation:** 

**[5921.42s] English:** learning it's a predictive model and you're learning a predictive model basically just by  
**Translation:** 

**[5925.30s] English:** looking at what data you have is there something about that active learning context that that you  
**Translation:** 

**[5930.70s] English:** you find insights from like that kind of deployment of the system seeing cases where  
**Translation:** 

**[5935.98s] English:** it doesn't perform as you expected  
**Translation:** 

**[5938.94s] English:** and then retraining the system based on that i think that i mean that really resonates with me  
**Translation:** 

**[5942.90s] English:** uh it's super smart to do it that way because i mean the thing is with any kind of like practical  
**Translation:** 

**[5949.04s] English:** system like uh autonomous driving there are those those edge cases are the things that are actually  
**Translation:** 

**[5953.42s] English:** the problem right i mean highway driving uh or like freeway driving has basically been  
**Translation:** 

**[5958.32s] English:** like there has been a lot of success in that particular part of autonomous driving for a long  
**Translation:** Vocabulary: freeway: 高速公路

**[5962.26s] English:** time i would say like since the 80s or something now the point is all these failure cases are the  
**Translation:** 

**[5968.94s] English:** sort of reason why autonomous driving hasn't come it hasn't become like super super mainstream and  
**Translation:** Vocabulary: mainstream: 主流

**[5973.26s] English:** available like in every possible car right now and so basically by really scaling this problem  
**Translation:** 

**[5977.90s] English:** out by really trying to get all of these edge cases out as quickly as possible and then just  
**Translation:** 

**[5982.30s] English:** like using those to improve your model that's super smart uh and prediction uncertainty to  
**Translation:** 

**[5986.62s] English:** do that is like one really nice way of doing it uh let me put you on the spot  
**Translation:** 

**[5991.98s] English:** so uh we mentioned offline gitandra um he thinks that the tesla computer vision approach or really  
**Translation:** 

**[5998.94s] English:** is a really good approach for autonomous driving  
**Translation:** Vocabulary: autonomous: 自主

**[6000.00s] English:** driving is very far away how many years away if you have to bet all your money on it are we  
**Translation:** 

**[6007.36s] English:** to solving autonomous driving with this kind of computer vision only machine learning based  
**Translation:** 

**[6012.84s] English:** approach okay so what does solving autonomous driving mean does it mean solving it in the  
**Translation:** 

**[6016.84s] English:** u.s does it mean solving it in india because i can tell you that very different types of driving  
**Translation:** 

**[6020.56s] English:** happening not india not russia in the united states autonomous so what solving means is  
**Translation:** 

**[6028.46s] English:** uh when the car says it has control it is fully liable you can you can go to sleep  
**Translation:** 

**[6035.48s] English:** is driving by itself so this is highway and city driving but not everywhere but mostly everywhere  
**Translation:** 

**[6041.66s] English:** and it's let's say significantly better like say five times less accidents than humans  
**Translation:** 

**[6050.00s] English:** sufficiently safer such that the public feels like that uh transition is you know enticing  
**Translation:** 

**[6057.38s] English:** beneficial both for  
**Translation:** Vocabulary: enticing: 诱人的; sufficiently: 足够

**[6058.44s] English:** safety and financial and all those kinds of things okay so first disclaimer i'm not an expert in  
**Translation:** 

**[6063.12s] English:** autonomous driving so let me put it out there uh i would say like at least five to ten years  
**Translation:** 

**[6068.16s] English:** this is this would be my like guess from now then yeah i'm actually very impressed like when i sat  
**Translation:** 

**[6075.52s] English:** in a friend's tesla recently and of course like uh looking so it can on the screen it basically  
**Translation:** 

**[6081.04s] English:** shows all the detections and everything the car is doing as you're driving by and that's super  
**Translation:** 

**[6085.32s] English:** distracting for me as a person because all i keep looking at  
**Translation:** Vocabulary: detections: 检测结果; distracting: 分散注意力的

**[6088.44s] English:** is like the bounding boxes and the cars it's tracking and it's really impressive like especially  
**Translation:** 

**[6092.34s] English:** when it's raining and it's able to do that that was the most impressive part for me it's actually  
**Translation:** Vocabulary: bounding: 跳跃

**[6096.66s] English:** able to get through rain and do that and one of the reasons why like a lot of us believed and i  
**Translation:** 

**[6102.66s] English:** would put myself in that category is lidar based uh sort of uh technology for autonomous driving  
**Translation:** 

**[6107.76s] English:** was the key driver right so waymo was using it for the longest time and tesla then decided to go  
**Translation:** 

**[6112.26s] English:** this completely other route that oh we're not going to even use lidar so their initial system  
**Translation:** 

**[6118.44s] English:** was based and now they're actually moving to a  
**Translation:** 

**[6120.00s] English:** completely like vision-based system and so that was just like it sounded completely crazy like  
**Translation:** 

**[6125.04s] English:** lidar is very useful in cases where you have low visibility uh of course it comes with its own set  
**Translation:** 

**[6130.62s] English:** of complications but now to see that happen in like on a live Tesla that basically just proves  
**Translation:** Vocabulary: visibility: 能见度

**[6136.44s] English:** everyone wrong I would say in a way and that's just working really well I think there were also  
**Translation:** 

**[6141.66s] English:** like a lot of Advancements in camera technology now there were like I know at CMU when I was there  
**Translation:** Vocabulary: advancements: 进步

**[6146.46s] English:** was a particular kind of camera that had been developed that was really good at basically low  
**Translation:** 

**[6152.10s] English:** visibility settings so like lots of snow and lots of rain it could actually still have a very  
**Translation:** 

**[6156.12s] English:** reasonable visibility and I think there are lots of these kinds of innovations that will happen on  
**Translation:** 

**[6160.14s] English:** the sensor side itself which is actually going to make this very easy in the future and so maybe  
**Translation:** Vocabulary: innovations: 创新; sensor: 传感器

**[6164.52s] English:** that's actually why I'm more optimistic about vision-based self like autonomous driving I  
**Translation:** 

**[6169.14s] English:** just want to call it self-supervised driving but vision-based autonomous driving that's the reason  
**Translation:** Vocabulary: autonomous: 自主; optimistic: 乐观

**[6174.12s] English:** I'm quite optimistic about it because I think there are going to be  
**Translation:** 

**[6176.44s] English:** lots of these Advances on the sensor side itself so acquiring this data we're actually going to  
**Translation:** 

**[6181.42s] English:** get much better about it and then of course when once we're able to scale out and get all of these  
**Translation:** 

**[6185.98s] English:** edge cases in as like Andre described I think that's going to make us go very far away yeah  
**Translation:** Vocabulary: andre: 安德烈

**[6192.04s] English:** so I'm it's funny I'm very much with you on the five to ten years maybe 10 years but you made it  
**Translation:** 

**[6199.96s] English:** I'm not sure how you made it sound but for some people that seem that might seem like really far  
**Translation:** 

**[6204.88s] English:** away and then for other people  
**Translation:** 

**[6206.44s] English:** uh it might seem like very close there's a lot of fundamental questions about how much game theory  
**Translation:** 

**[6214.90s] English:** is in this whole thing so like how much is is this simply uh collision avoidance problem and how much  
**Translation:** 

**[6222.82s] English:** of it is uh you're still interacting with other humans in the scene and you're trying to create  
**Translation:** 

**[6228.10s] English:** an experience that's compelling so you want to get from point A to point B quickly you want to  
**Translation:** 

**[6233.62s] English:** navigate the scene in a safe way but you also want to show  
**Translation:** Vocabulary: compelling: 引人入胜; navigate: 导航

**[6236.44s] English:** some level of aggression because uh  
**Translation:** 

**[6240.00s] English:** Well, certainly this is why you're screwed in India  
**Translation:** Vocabulary: aggression: 攻击性

**[6241.88s] English:** because you have to show aggression.  
**Translation:** 

**[6243.20s] English:** Or Jersey, or New Jersey.  
**Translation:** 

**[6246.68s] English:** So like, or New York, or basically any major city.  
**Translation:** 

**[6251.24s] English:** But I think it's probably Elon that I talked the most about this,  
**Translation:** 

**[6254.86s] English:** which is surprised the level of which they're not considering human beings  
**Translation:** 

**[6259.58s] English:** as a huge problem in this, as a source of problem.  
**Translation:** 

**[6262.92s] English:** Like the driving is fundamentally a robot on robot  
**Translation:** 

**[6268.50s] English:** versus the environment problem  
**Translation:** Vocabulary: fundamentally: 从根本上

**[6270.98s] English:** versus like, you know, you can just consider humans not part of the problem.  
**Translation:** 

**[6275.06s] English:** I used to think humans are almost certainly have to be modeled really well.  
**Translation:** 

**[6281.26s] English:** Pedestrians and cyclists and humans inside other cars,  
**Translation:** 

**[6284.38s] English:** you have to have like mental models for them.  
**Translation:** Vocabulary: cyclists: 骑自行车的人; pedestrians: 行人

**[6286.30s] English:** You cannot just see it as objects.  
**Translation:** 

**[6288.20s] English:** But more and more, it's like the, it's the same kind of intuition.  
**Translation:** Vocabulary: cannot: 不能; intuition: 直觉

**[6292.92s] English:** Breaking thing that self-supervised learning does,  
**Translation:** 

**[6296.10s] English:** which is, well, maybe through the learning,  
**Translation:** 

**[6298.66s] English:** you'll get all the human, like human information you need, right?  
**Translation:** 

**[6304.46s] English:** Like maybe you'll get it just with enough data.  
**Translation:** 

**[6307.46s] English:** You don't need to have explicit good models of human behavior.  
**Translation:** 

**[6310.84s] English:** Maybe you get it through the data.  
**Translation:** Vocabulary: explicit: 明确的

**[6312.34s] English:** So, I mean, my skepticism also just knowing a lot of automotive companies  
**Translation:** 

**[6315.80s] English:** and how difficult it is to be innovative.  
**Translation:** Vocabulary: automotive: 汽车; skepticism: 怀疑

**[6318.32s] English:** I was skeptical that they would be able at scale  
**Translation:** 

**[6322.06s] English:** to control.  
**Translation:** Vocabulary: skeptical: 怀疑的

**[6322.92s] English:** Convert the driving scene across the world into digital form  
**Translation:** 

**[6328.78s] English:** such that you can create this data engine at scale.  
**Translation:** 

**[6333.08s] English:** And the fact that Tesla is at least getting there  
**Translation:** 

**[6336.24s] English:** or are already there makes me think that  
**Translation:** 

**[6340.78s] English:** it's now starting to be coupled to this self-supervised learning vision,  
**Translation:** 

**[6347.58s] English:** which is like, if that's going to work,  
**Translation:** 

**[6349.86s] English:** if through purely this process, you can get really far,  
**Translation:** 

**[6352.92s] English:** then maybe you can solve driving that way.  
**Translation:** 

**[6354.76s] English:** I don't know.  
**Translation:** 

**[6355.40s] English:** I tend to believe we don't give enough credit.  
**Translation:** 

**[6360.00s] English:** to the to the how amazing humans are both at driving and at supervising autonomous systems  
**Translation:** 

**[6368.34s] English:** and also we don't this is i wish we were i wish there was much more driver sensing inside teslas  
**Translation:** Vocabulary: autonomous: 自主; supervising: 监督; teslas: 特斯拉

**[6376.18s] English:** and much deeper consideration of human factors like understanding psychology and drowsiness and  
**Translation:** 

**[6384.76s] English:** all those kinds of things when the car does more and more of the work how to uh keep utilizing the  
**Translation:** Vocabulary: drowsiness: 嗜睡; utilizing: 利用

**[6391.76s] English:** little human supervision that i needed to keep this whole thing safe i mean it's a fascinating  
**Translation:** 

**[6395.98s] English:** dance of human robot interaction to me autonomous driving for a long time is a human robot  
**Translation:** Vocabulary: supervision: 监督

**[6403.02s] English:** interaction problem it is not a robotics problem or computer vision problem like you have to have  
**Translation:** 

**[6408.88s] English:** human in the loop but so which is why i think it's 10 years plus but i do think there'll be  
**Translation:** 

**[6414.54s] English:** a  
**Translation:** 

**[6414.74s] English:** bunch of cities and contexts where you know uh geo-restricted it will work really really damn  
**Translation:** 

**[6421.34s] English:** well yeah so i think for me like it's five if i'm being optimistic and it's going to be five for a  
**Translation:** 

**[6426.34s] English:** lot of cases and 10 plus yeah i agree with you 10 plus basically uh if we want to recover most of  
**Translation:** Vocabulary: optimistic: 乐观的

**[6432.74s] English:** say contiguous united states or something oh interesting so my my optimistic is five and  
**Translation:** 

**[6438.42s] English:** pessimistic is 30 30 i have a long tail on this one i've watched enough driving videos i've  
**Translation:** Vocabulary: contiguous: 相连的; pessimistic: 悲观的

**[6444.56s] English:** watched enough pedestrians to think like we may be like there's a small part of me still not a  
**Translation:** 

**[6451.36s] English:** like a pretty big part of me that thinks we will have to build agi to solve driving  
**Translation:** Vocabulary: pedestrians: 行人

**[6456.90s] English:** oh well like there's something to me like because humans are part of the picture deeply part of the  
**Translation:** 

**[6462.64s] English:** picture and also human society is part of the picture in that human life is at stake  
**Translation:** 

**[6467.38s] English:** anytime a robot kills a human it's not clear to me that that's not a problem that  
**Translation:** 

**[6474.56s] English:** machine learning will also have to solve yeah like it has to it you have to integrate that into the  
**Translation:** Vocabulary: anytime: 任何时间; integrate: 整合

**[6479.72s] English:** whole thing  
**Translation:** 

**[6480.00s] English:** just like facebook or social networks you know one thing is to say how to make a really good  
**Translation:** 

**[6485.06s] English:** recommender system and then the other thing is to integrate into that recommender system  
**Translation:** 

**[6489.98s] English:** all the journalists that will write articles about that recommender system like you have to consider  
**Translation:** Vocabulary: recommender: 推荐系统

**[6494.98s] English:** the society within which the ai system operates and in order to and like politicians too you know  
**Translation:** 

**[6500.94s] English:** this is there's regulatory stuff for autonomous driving right it's kind of fascinating that the  
**Translation:** Vocabulary: autonomous: 自主

**[6505.82s] English:** more successful your ai system becomes the more it gets integrated in society and the more  
**Translation:** 

**[6512.06s] English:** precious politicians and the public and the clickbait journalists and the all the different  
**Translation:** Vocabulary: clickbait: 标题党

**[6517.00s] English:** fascinating forces of our society start acting on it and then it's no longer how good you are  
**Translation:** 

**[6522.20s] English:** doing the initial task it's also how good you are navigating human nature which uh which is a  
**Translation:** Vocabulary: navigating: 驾驭外力

**[6528.40s] English:** fascinating space what do you think are the limits of deep learning if you allow me we'll zoom out a  
**Translation:** 

**[6534.14s] English:** little bit into the big question  
**Translation:** 

**[6535.80s] English:** of artificial intelligence you said dark matter of intelligence is self-supervised learning but  
**Translation:** 

**[6543.08s] English:** there could be more what do you think the limits of self-supervised learning and just learning in  
**Translation:** 

**[6548.86s] English:** general deep learning are i think like for deep learning in particular because self-supervised  
**Translation:** 

**[6553.88s] English:** learning is i would say a little bit more uh vague right now so i wouldn't like for something  
**Translation:** 

**[6557.94s] English:** that's so vague it's hard to predict what its limits are going to be but like like i said i  
**Translation:** 

**[6562.86s] English:** think anywhere you want to you know interact with humans  
**Translation:** 

**[6565.80s] English:** even if you're learning something that's self-supervised then you're going to have to  
**Translation:** 

**[6568.52s] English:** put in some deep learning to be able to communicate with the human um and then when you're learning  
**Translation:** 

**[6571.70s] English:** that self-supervised learning kind of hits a hits a boundary very quickly because you need to have an  
**Translation:** 

**[6575.12s] English:** interface to be able to communicate with the human so really like uh if you have just like vacuous  
**Translation:** Vocabulary: interface: 人机接口; vacuous: 空洞

**[6579.86s] English:** concepts or like just like nebulous concepts discovered by a network uh it's very hard to  
**Translation:** 

**[6584.90s] English:** communicate those with a human without like inserting some kind of human knowledge or some  
**Translation:** Vocabulary: inserting: 插入; nebulous: 模糊

**[6588.06s] English:** kind of like human bias there in general i think for deep learning the biggest challenge is just  
**Translation:** 

**[6593.64s] English:** like data efficiency  
**Translation:** 

**[6595.80s] English:** once, like one image of a, like, I don't know.  
**Translation:** 

**[6600.00s] English:** or whatever you want to call it, like any concept,  
**Translation:** 

**[6602.52s] English:** it's really hard for these methods to generalize  
**Translation:** 

**[6604.80s] English:** by looking at just one or two samples of things.  
**Translation:** Vocabulary: generalize: 泛化

**[6607.70s] English:** And that has been a real challenge.  
**Translation:** 

**[6609.74s] English:** And I think that's actually why like these edge cases,  
**Translation:** 

**[6611.66s] English:** for example, for Tesla are actually that important.  
**Translation:** 

**[6614.52s] English:** Because if you see just one instance of the car failing,  
**Translation:** 

**[6618.04s] English:** and if you just annotate that  
**Translation:** 

**[6619.30s] English:** and you get that into your dataset,  
**Translation:** Vocabulary: annotate: 标注; dataset: 数据集

**[6621.92s] English:** you have like very limited guarantee  
**Translation:** 

**[6623.56s] English:** that it's not going to happen again.  
**Translation:** 

**[6625.14s] English:** And you're actually going to be able to recognize  
**Translation:** 

**[6626.74s] English:** this kind of instance in a very different scenario.  
**Translation:** 

**[6628.62s] English:** So like when it was snowing,  
**Translation:** 

**[6630.30s] English:** so you got that thing labeled when it was snowing,  
**Translation:** 

**[6632.04s] English:** but now when it's raining,  
**Translation:** 

**[6633.22s] English:** you're actually not able to get it.  
**Translation:** 

**[6634.64s] English:** Or you basically have the same scenario  
**Translation:** 

**[6636.60s] English:** in a different part of the world,  
**Translation:** 

**[6637.44s] English:** so the lighting was different or so on.  
**Translation:** 

**[6639.12s] English:** So it's just really hard for these models,  
**Translation:** 

**[6641.02s] English:** like deep learning especially, to do that.  
**Translation:** 

**[6642.72s] English:** What's your intuition?  
**Translation:** Vocabulary: intuition: 直觉

**[6643.56s] English:** How do we solve handwritten digit recognition problem  
**Translation:** 

**[6647.58s] English:** when we only have one example for each number?  
**Translation:** Vocabulary: digit: 阿拉伯数字; handwritten: 手写

**[6651.22s] English:** It feels like humans are using something like learning.  
**Translation:** 

**[6654.72s] English:** Right, I think it's,  
**Translation:** 

**[6656.02s] English:** we are good at transferring knowledge  
**Translation:** 

**[6658.38s] English:** a little bit.  
**Translation:** 

**[6659.26s] English:** We are just better at like,  
**Translation:** 

**[6661.24s] English:** for a lot of these problems  
**Translation:** 

**[6662.64s] English:** where we are generalizing from a single sample,  
**Translation:** 

**[6664.84s] English:** or recognizing from a single sample,  
**Translation:** Vocabulary: generalizing: 从单一样本外推

**[6666.94s] English:** we are using a lot of our own domain knowledge  
**Translation:** 

**[6668.74s] English:** and a lot of our like inductive bias  
**Translation:** Vocabulary: inductive: 归纳的

**[6670.34s] English:** into that one sample to generalize it.  
**Translation:** 

**[6672.30s] English:** So I've never seen you write the number nine, for example.  
**Translation:** 

**[6675.32s] English:** And if you were to write it, I would still get it.  
**Translation:** 

**[6677.44s] English:** And if you were to write a different kind of alphabet  
**Translation:** 

**[6679.28s] English:** and like write it in two different ways,  
**Translation:** 

**[6680.82s] English:** I would still probably be able to figure out  
**Translation:** 

**[6682.32s] English:** that these are the same two characters.  
**Translation:** 

**[6684.70s] English:** It's just that I have been very used  
**Translation:** 

**[6686.28s] English:** to seeing handwritten digits in my life.  
**Translation:** 

**[6688.16s] English:** The other sort of problem with any deep learning system  
**Translation:** Vocabulary: digits: 手写数字

**[6691.34s] English:** or any kind of machine learning system  
**Translation:** 

**[6692.70s] English:** is like it's guarantees, right?  
**Translation:** Vocabulary: guarantees: 保证

**[6694.16s] English:** There are no guarantees for it.  
**Translation:** 

**[6695.86s] English:** Now you can argue that humans  
**Translation:** 

**[6696.94s] English:** also don't have any guarantees.  
**Translation:** 

**[6698.16s] English:** Like there is no guarantee that I can recognize a cat  
**Translation:** 

**[6701.12s] English:** in every scenario.  
**Translation:** 

**[6702.24s] English:** I'm sure there are going to be lots of cats  
**Translation:** 

**[6703.90s] English:** that I don't recognize,  
**Translation:** 

**[6705.04s] English:** lots of scenarios in which I don't recognize cats in general.  
**Translation:** Vocabulary: scenarios: 情景

**[6708.10s] English:** But I think from like,  
**Translation:** 

**[6710.26s] English:** from just a sort of application perspective,  
**Translation:** 

**[6712.84s] English:** you do need guarantees, right?  
**Translation:** 

**[6714.74s] English:** We call these things algorithms.  
**Translation:** 

**[6716.94s] English:** Now algorithms,  
**Translation:** 

**[6718.16s] English:** traditional CS algorithms have guarantees.  
**Translation:** 

**[6720.00s] English:** sorting is a guarantee.  
**Translation:** 

**[6721.50s] English:** If you were to call sort on a particular array of numbers,  
**Translation:** 

**[6725.64s] English:** you are guaranteed that it's going to be sorted.  
**Translation:** 

**[6727.66s] English:** Otherwise, it's a bug.  
**Translation:** 

**[6729.34s] English:** Now for machine learning,  
**Translation:** 

**[6730.18s] English:** it's very hard to characterize this.  
**Translation:** Vocabulary: characterize: 描述

**[6732.48s] English:** We know for a fact that a cat recognition model  
**Translation:** 

**[6735.48s] English:** is not going to recognize cats,  
**Translation:** 

**[6737.08s] English:** every cat in the world in every circumstance.  
**Translation:** 

**[6739.76s] English:** I think most people would agree with that statement.  
**Translation:** Vocabulary: circumstance: 情况

**[6742.08s] English:** But we are still okay with it.  
**Translation:** 

**[6743.64s] English:** We still don't call this as a bug.  
**Translation:** 

**[6745.44s] English:** As in traditional computer science or traditional science,  
**Translation:** 

**[6748.06s] English:** if you have this kind of failure case existing,  
**Translation:** 

**[6750.02s] English:** then you think of it as like something is wrong.  
**Translation:** 

**[6753.26s] English:** I think there is this sort of notion  
**Translation:** 

**[6754.60s] English:** of nebulous correctness for machine learning,  
**Translation:** 

**[6757.10s] English:** and that's something we just need  
**Translation:** Vocabulary: correctness: 正确性; nebulous: 模糊的

**[6757.98s] English:** to be very comfortable with.  
**Translation:** 

**[6759.56s] English:** And for deep learning,  
**Translation:** 

**[6760.62s] English:** or like for a lot of these machine learning algorithms,  
**Translation:** 

**[6762.78s] English:** it's not clear how do we characterize  
**Translation:** 

**[6764.78s] English:** this notion of correctness.  
**Translation:** 

**[6766.40s] English:** I think limitation in our understanding,  
**Translation:** 

**[6768.22s] English:** or at least a limitation in our phrasing of this.  
**Translation:** 

**[6771.24s] English:** And if we were to come up with better ways  
**Translation:** Vocabulary: phrasing: 表达方式

**[6773.16s] English:** to understand this limitation,  
**Translation:** 

**[6775.14s] English:** then it would actually help us a lot.  
**Translation:** 

**[6777.26s] English:** Do you think there's  
**Translation:** 

**[6778.04s] English:** a distinction between the concept of learning  
**Translation:** 

**[6781.82s] English:** and the concept of reasoning?  
**Translation:** 

**[6784.26s] English:** Do you think it's possible for neural networks to reason?  
**Translation:** 

**[6790.30s] English:** So I think of it slightly differently.  
**Translation:** 

**[6791.66s] English:** So for me, learning is whenever I can make a snap judgment.  
**Translation:** 

**[6796.06s] English:** So if you show me a picture of a dog,  
**Translation:** 

**[6797.20s] English:** I can immediately say it's a dog.  
**Translation:** 

**[6798.88s] English:** But if you give me like a puzzle,  
**Translation:** 

**[6800.42s] English:** you know, like whatever, a Goldsberg machine  
**Translation:** Vocabulary: goldsberg: 高斯伯格

**[6803.46s] English:** of like things going to happen,  
**Translation:** 

**[6804.96s] English:** then I have to reason.  
**Translation:** 

**[6805.80s] English:** Because I've never, it's a very complicated setup.  
**Translation:** 

**[6807.60s] English:** I've never seen that particular setup,  
**Translation:** Vocabulary: setup: 安装配置

**[6809.34s] English:** and I really need to, you know, draw and like imagine  
**Translation:** 

**[6811.84s] English:** in my head what's going to happen to figure it out.  
**Translation:** 

**[6814.68s] English:** So I think, yes, neural networks are really good  
**Translation:** 

**[6816.86s] English:** at recognition, but they're not very good at reasoning.  
**Translation:** Vocabulary: neural: 神经的

**[6821.20s] English:** Because they're like if they have seen something before  
**Translation:** 

**[6824.14s] English:** or seen something similar before,  
**Translation:** 

**[6825.82s] English:** they're very good at making those sort of snap judgments.  
**Translation:** 

**[6828.16s] English:** But if you were to give them a very complicated thing  
**Translation:** 

**[6830.74s] English:** that they've not seen before,  
**Translation:** 

**[6832.52s] English:** they have very limited ability right now  
**Translation:** 

**[6835.36s] English:** to compose different things.  
**Translation:** 

**[6836.60s] English:** I've seen this particular part before, I've seen this particular part before.  
**Translation:** 

**[6840.00s] English:** And now probably like this is how they're going to work in tandem.  
**Translation:** 

**[6842.86s] English:** It's very hard for them to come up with these kinds of things.  
**Translation:** Vocabulary: tandem: 并肩工作

**[6845.02s] English:** Well, there's a certain aspect to reasoning that you can maybe convert into the process of programming.  
**Translation:** 

**[6851.92s] English:** And so there's the whole field of program synthesis.  
**Translation:** Vocabulary: synthesis: 合成

**[6854.40s] English:** And people have been applying machine learning to the problem of program synthesis.  
**Translation:** 

**[6859.02s] English:** And the question is, you know, can they, the step of composition, why can't that be learned?  
**Translation:** 

**[6863.92s] English:** You know, this step of like building things on top of it, like little intuitions, concepts on top of each other.  
**Translation:** 

**[6872.88s] English:** Can that be learnable?  
**Translation:** Vocabulary: intuitions: 直觉

**[6875.14s] English:** What's your intuition there?  
**Translation:** 

**[6876.82s] English:** Or like, I guess, similar set of techniques, do you think that would be applicable?  
**Translation:** 

**[6882.06s] English:** So I think it is, of course, it is learnable because like we are prime examples of machines that have like or individuals that have learned this, right?  
**Translation:** 

**[6889.48s] English:** Like humans have learned this.  
**Translation:** 

**[6890.78s] English:** So it is, of course, it is a technique that is very easy to learn.  
**Translation:** 

**[6893.92s] English:** I think where we are kind of hitting a wall, basically, with like current machine learning is the fact that when the network learns all of this information, we basically are not able to figure out how well it's going to generalize to an unseen thing.  
**Translation:** Vocabulary: generalize: 泛化能力

**[6910.28s] English:** And we have no, like a priori, no way of characterizing that.  
**Translation:** 

**[6914.70s] English:** And I think that's basically telling us a lot about, like a lot about the fact that we really don't know what this model has learned and how well it's basically, because we don't know how well it's going to generalize.  
**Translation:** 

**[6923.92s] English:** There's also a sense in which it feels like we humans may not be aware of how much like background, how good our background model is, how much knowledge we just have slowly building on top of each other.  
**Translation:** 

**[6941.50s] English:** It feels like neural networks are constantly throwing stuff out.  
**Translation:** Vocabulary: neural: 神经的

**[6944.00s] English:** Like you'll do some incredible thing where you're learning a particular task in computer vision.  
**Translation:** 

**[6948.88s] English:** You celebrate your state of the art successes and you throw that out.  
**Translation:** 

**[6952.54s] English:** Like it feels like.  
**Translation:** 

**[6953.92s] English:** You're never using stuff you've learned for your future successes in other domains.  
**Translation:** 

**[6960.00s] English:** And humans are obviously doing that exceptionally well, still throwing stuff away in their mind, but keeping certain kernels of truth.  
**Translation:** 

**[6967.74s] English:** Right. So I think we're like continual learning is sort of the paradigm for this in machine learning.  
**Translation:** Vocabulary: continual: 持续不断; exceptionally: 极其; kernels: 核心; paradigm: 范式

**[6972.08s] English:** And I don't think it's a very well explored paradigm.  
**Translation:** 

**[6974.38s] English:** Yeah.  
**Translation:** 

**[6975.06s] English:** We have like things in deep learning, for example, catastrophic forgetting is like one of the standard things.  
**Translation:** 

**[6980.34s] English:** The thing basically being that if you teach a network like to recognize dogs and now you teach that same network to recognize cats, it basically forgets how to recognize dogs.  
**Translation:** Vocabulary: catastrophic: 灾难性的

**[6989.12s] English:** So it forgets very quickly.  
**Translation:** 

**[6991.02s] English:** I mean, and whereas a human, if you were to teach someone to recognize dogs and then to recognize cats, they don't forget immediately how to recognize these dogs.  
**Translation:** 

**[6998.52s] English:** I think that's basically sort of what you're trying to get.  
**Translation:** 

**[7000.76s] English:** Yeah, I just I wonder if like the long term memory mechanisms or the mechanisms that store not just memories, but concepts that allow you to reason and compose concepts.  
**Translation:** 

**[7016.98s] English:** If those things will look very different.  
**Translation:** 

**[7019.12s] English:** Or if you can do that within a single neural network with some particular sort of architecture quirks, that seems to be a really open problem.  
**Translation:** Vocabulary: quirks: 特殊结构

**[7027.94s] English:** And of course, I go up and down on that because it's there's something so compelling to the to the symbolic AI or to the ideas of logic based sort of expert systems.  
**Translation:** 

**[7040.52s] English:** You have like human interpretable facts that built on top of each other.  
**Translation:** Vocabulary: compelling: 有吸引力的; interpretable: 可理解的; symbolic: 象征性的

**[7043.86s] English:** It's really annoying, like with self supervised learning that.  
**Translation:** 

**[7049.12s] English:** The AI is not very explainable, like you can't like understand all the beautiful thing is as has learned.  
**Translation:** Vocabulary: supervised: 监督学习

**[7055.68s] English:** You can't ask it like questions.  
**Translation:** 

**[7058.48s] English:** But then again, maybe that's a stupid thing for us humans to want.  
**Translation:** 

**[7062.50s] English:** But I think whenever we try to like understand it, we're putting our own subjective human bias into it.  
**Translation:** 

**[7067.90s] English:** Yeah.  
**Translation:** 

**[7068.44s] English:** And I think that's the sort of problem with self supervised learning.  
**Translation:** 

**[7071.14s] English:** The goal is that it should learn naturally from the data.  
**Translation:** 

**[7074.40s] English:** So now if you try to understand it, you are using your you're using your own preconceived notions of.  
**Translation:** 

**[7079.00s] English:** What?  
**Translation:** Vocabulary: preconceived: 先入为主

**[7079.12s] English:** What this model has.  
**Translation:** 

**[7080.00s] English:** learned and that's the problem high level question what do you think it takes to build a uh system  
**Translation:** 

**[7087.84s] English:** with superhuman maybe let's say human level or superhuman level general intelligence we've  
**Translation:** 

**[7093.84s] English:** already kind of started talking about this but what's your intuition like does the thing have  
**Translation:** Vocabulary: intuition: 直觉

**[7098.72s] English:** to have a body does it does it have to interact richly with the world uh does it have to have  
**Translation:** 

**[7106.40s] English:** some more human elements like self-awareness i think emotion i think emotion is something which  
**Translation:** 

**[7113.68s] English:** is like it's not really attributed typically in standard machine learning it's not something we  
**Translation:** 

**[7118.96s] English:** think about like there is nlp there is vision there is no like emotion emotion is never a part  
**Translation:** Vocabulary: attributed: 归因

**[7123.60s] English:** of all of this and that just seems a little bit weird to me i think the reason basically being  
**Translation:** 

**[7128.24s] English:** that there is surprise and like basically emotion is like one of the reasons emotions arise is like  
**Translation:** 

**[7135.04s] English:** what happens and what you expect  
**Translation:** 

**[7136.40s] English:** to happen right there is like a mismatch between these things and so that gives rise like i can  
**Translation:** 

**[7141.36s] English:** either be surprised or i can be saddened or i can be happy and all of this and so  
**Translation:** 

**[7146.88s] English:** this basically indicates that i already have a predictive model in my head and something that  
**Translation:** Vocabulary: predictive: 预测性的

**[7150.80s] English:** i predicted or something that i thought was likely to happen and then there was something  
**Translation:** 

**[7154.40s] English:** that i observed that happened there was a disconnect between these two things and that  
**Translation:** Vocabulary: disconnect: 不符

**[7158.64s] English:** basically is like maybe one of the reasons i like you have a lot of emotions yeah i i think so i  
**Translation:** 

**[7166.40s] English:** think a lot about like lisa feldman barrett i think that's an interesting concept of emotion but  
**Translation:** Vocabulary: barrett: 巴雷特; feldman: 费尔德曼

**[7172.08s] English:** i have a sense that emotion primarily in the way we think about it which is the display of emotion  
**Translation:** 

**[7180.32s] English:** is a communication mechanism between humans so it's it's a part of basically human to human  
**Translation:** 

**[7186.40s] English:** interaction um an important part but just the part so it's like it i would throw it into the  
**Translation:** 

**[7193.44s] English:** um into the full mix of  
**Translation:** 

**[7196.40s] English:** communication and to me communication  
**Translation:** 

**[7200.00s] English:** can be done with objects that don't look at all like humans okay i've seen our ability to  
**Translation:** 

**[7206.70s] English:** anthropomorphize our ability to connect with things that look like a rumba our ability to connect  
**Translation:** 

**[7211.70s] English:** first of all let's talk about other biological systems like dogs our ability to love things that  
**Translation:** Vocabulary: anthropomorphize: 拟人化; rumba: 伦巴舞

**[7217.54s] English:** are very different than humans but they do display emotion right i mean dogs do display  
**Translation:** 

**[7222.16s] English:** emotion so they don't have to be anthropomorphic for them to like display the kind of emotion that  
**Translation:** Vocabulary: anthropomorphic: 拟人化的

**[7227.68s] English:** we don't exactly so i mean but then the word emotion starts to lose um so then we have to be  
**Translation:** 

**[7234.60s] English:** i guess specific but yeah so have rich flavorful communication communication yeah yeah so like  
**Translation:** Vocabulary: flavorful: 味蕾丰富的

**[7240.84s] English:** yes it's full of emotion it's full of uh wit and humor and uh moods and all those kinds of things  
**Translation:** 

**[7250.02s] English:** yeah so exactly so you're talking about like flavor flavor yeah okay let's follow that so  
**Translation:** 

**[7255.54s] English:** there's content and then there is flavor and i'm talking  
**Translation:** 

**[7257.62s] English:** yeah  
**Translation:** 

**[7257.68s] English:** do you think it needs to have a body do you think like to interact with the physical world do you  
**Translation:** 

**[7262.98s] English:** think you can understand the physical world without being able to directly interact with it i don't  
**Translation:** 

**[7267.30s] English:** think so yeah i think at some point we will need to bite the bullet and actually interact with the  
**Translation:** 

**[7271.68s] English:** physical as much as i like working on like passive computer vision where i just like sit in my arm  
**Translation:** 

**[7277.04s] English:** chair and look at videos and learn i do think that uh we will need to have some kind of embodiment  
**Translation:** 

**[7282.40s] English:** or some kind of interaction to figure out things about the world what about conscious  
**Translation:** Vocabulary: embodiment: 实体表现

**[7287.62s] English:** you think you think how often do you think about consciousness when you think about your work  
**Translation:** 

**[7293.40s] English:** you could think of it as the more simple thing of self-awareness of of being aware that you are a  
**Translation:** 

**[7301.68s] English:** perceiving sensing acting thing in this world or you can think about the bigger thing version of  
**Translation:** 

**[7310.16s] English:** that which is consciousness which is having it feel like something to be that entity the  
**Translation:** Vocabulary: perceiving: 感知

**[7317.62s] English:** active experience of being in this world so i think of  
**Translation:** 

**[7320.00s] English:** self-awareness a little bit more than this like the broader goal of it because i think self-awareness  
**Translation:** 

**[7324.86s] English:** is pretty critical for like any kind of like any kind of agi or whatever you want to call it that  
**Translation:** 

**[7330.26s] English:** we'll build because it needs to contextualize what it is and what role it's playing with respect to  
**Translation:** 

**[7336.20s] English:** all the other things that exist around it i think that requires self-awareness it needs to understand  
**Translation:** 

**[7340.54s] English:** that it's an autonomous car right and what does that mean what are its limitations what are the  
**Translation:** Vocabulary: autonomous: 自主的

**[7346.96s] English:** things that it is supposed to do and so on what is its role in some way or i mean so i mean this  
**Translation:** 

**[7353.26s] English:** these are the kind of things that we kind of expect from it i would say and so that's the  
**Translation:** 

**[7358.38s] English:** level of self-awareness that's i would say basically required at least if not more than that  
**Translation:** 

**[7363.30s] English:** yeah i tend to on the emotion side believe that it has to have it has to be able to display  
**Translation:** 

**[7369.86s] English:** consciousness display consciousness what do you mean by that meaning like for us humans to connect  
**Translation:** 

**[7376.02s] English:** with each other  
**Translation:** 

**[7376.96s] English:** or to connect with other living entities i think we need to feel like in order for us to uh truly  
**Translation:** 

**[7386.40s] English:** feel like that there's another being there we have to believe that they're conscious and so  
**Translation:** 

**[7391.86s] English:** we won't ever connect with something that doesn't have elements of consciousness now i tend to think  
**Translation:** 

**[7398.26s] English:** that that's easier to achieve than it may sound because we anthropomorphize stuff so hard like  
**Translation:** 

**[7405.90s] English:** you have a  
**Translation:** 

**[7406.94s] English:** mug that just like has wheels and like rotates every once in a while and makes a sound i think  
**Translation:** Vocabulary: rotates: 旋转

**[7412.32s] English:** a couple days in especially if you're uh if you're if you don't hang out with humans you  
**Translation:** 

**[7419.62s] English:** might start to believe that mug on wheels is conscious so i think we anthropomorphize pretty  
**Translation:** Vocabulary: anthropomorphize: 赋予人类特征

**[7424.26s] English:** effectively as human beings but i do think that it's it's in the same bucket that we'll call  
**Translation:** 

**[7429.84s] English:** emotion that show that uh you're you know i think of consciousness as the capacity to  
**Translation:** 

**[7436.74s] English:** suffer and to live and to live and to live and to live and to live and to live and to live and to live  
**Translation:** 

**[7436.94s] English:** and to live and to live and to live and to live and to live and to live and to live and to live and  
**Translation:** 

**[7437.94s] English:** to live and to live and to live and to live and to live and to live and to live and to live and to live  
**Translation:** 

**[7438.94s] English:** and to live and to live and to live and to live and to live and to live and to live and to live  
**Translation:** 

**[7439.94s] English:** and to live and to live and to live and to live and to live and to live and to live and to live  
**Translation:** 

**[7440.94s] English:** and to live and to live and to live and to live and to live and to live and to live and to live and to live  
**Translation:** 

**[7441.94s] English:** and to live and to live and to live and to live and to live and to live and to live and to live and to live  
**Translation:** 

**[7442.94s] English:** and to live and to live and to live and to live and to live and to live and to live and to live and to live  
**Translation:** 

**[7440.00s] English:** able to feel things in the world and to communicate that to others um i think that's a really powerful  
**Translation:** 

**[7448.04s] English:** way to um interact with humans and in order to create an agi system i believe you should be able  
**Translation:** 

**[7455.32s] English:** to richly interact with humans like humans would need to want to interact with you like it can't  
**Translation:** 

**[7461.66s] English:** be like it's it's the um self-supervised learning versus like uh like the robot shouldn't have to  
**Translation:** 

**[7468.84s] English:** pay you to interact with me so like it should be a natural fun thing and then you're going to  
**Translation:** 

**[7474.58s] English:** scale up significantly how much uh interaction it gets yeah it's the alexa prize which they're  
**Translation:** 

**[7481.28s] English:** trying to get me to be a judge on their uh contest i'll see if i want to do that but their their  
**Translation:** 

**[7486.66s] English:** challenge is to uh talk to you make the judge make the human sufficiently interested that the  
**Translation:** Vocabulary: sufficiently: 足够地

**[7494.32s] English:** human keeps talking for 20 minutes to alexa to alexa yeah  
**Translation:** 

**[7498.84s] English:** right now they're not even close to that because it just gets so boring when you're like when when  
**Translation:** 

**[7502.94s] English:** the intelligence is not there it gets very not interesting to talk to it and so the robot needs  
**Translation:** 

**[7508.14s] English:** to be interesting and one of the ways it can be interesting is display the capacity to to love  
**Translation:** 

**[7513.30s] English:** to suffer and i would say that essentially means the the capacity to display consciousness like it  
**Translation:** 

**[7521.20s] English:** is an entity much like a human being of course what that really means i don't know if that's  
**Translation:** 

**[7528.84s] English:** a robotics problem or some kind of problem that we're not yet even aware like if it is truly a  
**Translation:** 

**[7534.10s] English:** hard problem of consciousness i tend to maybe optimistically think it's a um we can pretty  
**Translation:** 

**[7540.46s] English:** effectively fake it till we make it so we can display a lot of human-like elements for a while  
**Translation:** 

**[7545.90s] English:** and that will be sufficient to form really close connections with humans  
**Translation:** 

**[7550.46s] English:** what to use the most beautiful idea in self-supervised learning like when you sit back  
**Translation:** 

**[7556.88s] English:** with uh i don't know i don't know i don't know i don't know i don't know i don't know i don't know  
**Translation:** 

**[7558.84s] English:** with a glass of wine  
**Translation:** 

**[7560.00s] English:** and armchair and just at a fireplace just thinking how beautiful this world that you  
**Translation:** Vocabulary: fireplace: 壁炉

**[7568.52s] English:** get to explore is what do you think is the especially beautiful idea the fact that like  
**Translation:** 

**[7574.56s] English:** object level what objects are in some notion of objectness emerges from these models by just like  
**Translation:** Vocabulary: objectness: 物体感知

**[7581.70s] English:** self-supervised learning so for example like um one of the things like the dino paper uh that  
**Translation:** 

**[7589.14s] English:** i was a part of at facebook is um the object sort of boundaries emerge from these representations  
**Translation:** 

**[7595.16s] English:** so if you have like a dog running in the field the boundaries around the dog the network is  
**Translation:** 

**[7600.06s] English:** basically able to figure out uh what the boundaries of this dog are automatically  
**Translation:** 

**[7604.28s] English:** and it was never trained to do that it was never trained to uh no one taught it that this is a dog  
**Translation:** 

**[7610.94s] English:** and these pixels belong to a dog it's able to group these things together automatically so  
**Translation:** Vocabulary: pixels: 像素

**[7615.16s] English:** that's one and i think in general that entire notion that  
**Translation:** 

**[7618.30s] English:** this dumb idea that you take like these two crops of an image and then you say that the features  
**Translation:** 

**[7623.10s] English:** should be similar that has resulted in something like this like the model is able to figure out  
**Translation:** 

**[7627.88s] English:** what the dog pixels are and so on that just seems like so surprising um and i mean i don't think a  
**Translation:** 

**[7634.76s] English:** lot of us even understand what how that is happening really and it's something we are  
**Translation:** 

**[7639.14s] English:** taking for granted uh maybe like a lot in terms of how we're setting up these algorithms but it's  
**Translation:** 

**[7644.62s] English:** just it's a very beautiful and powerful idea so it's really fundamentally telling us the  
**Translation:** 

**[7648.30s] English:** something about that there is so much signal in the pixels that we can be super dumb about it  
**Translation:** Vocabulary: fundamentally: 从根本上

**[7654.04s] English:** about how we're setting up the self-supervailing problem and despite being like super dumb about it  
**Translation:** 

**[7659.42s] English:** we'll actually get very good uh like we'll actually get something that uh is able to do  
**Translation:** 

**[7663.92s] English:** very like surprising things i wonder if there's other like objectness of other concepts that can  
**Translation:** 

**[7669.60s] English:** emerge i don't know if you follow francois chole he had the competition for intelligence  
**Translation:** 

**[7678.30s] English:** kind of like an iq test but from a  
**Translation:** 

**[7680.00s] English:** means but for an iq test you have to have a few concepts that you want to apply one of them is  
**Translation:** 

**[7685.98s] English:** objectness i wonder if those concepts can emerge through self-supervised learning on billions of  
**Translation:** 

**[7693.52s] English:** images i think something like object permanence can definitely emerge right so that's like a  
**Translation:** Vocabulary: permanence: 持久性

**[7698.00s] English:** fundamental concept which we have maybe not through images through video but that's another concept  
**Translation:** 

**[7702.74s] English:** that should be emergent from it because it's not something that like you we don't teach humans that  
**Translation:** Vocabulary: emergent: 自然产生

**[7708.54s] English:** this isn't this is like about this concept of object permanence it actually emerges and the  
**Translation:** 

**[7712.70s] English:** same thing for like animals like dogs i think actually permanence automatically is something  
**Translation:** 

**[7716.72s] English:** that they are born with so i think it should emerge from the data it should emerge basically  
**Translation:** 

**[7721.32s] English:** very quickly i wonder if ideas like symmetry rotation these kinds of things might emerge  
**Translation:** Vocabulary: symmetry: 对称

**[7727.18s] English:** so i think rotation probably yes yeah rotation yes i mean there's some constraints in the  
**Translation:** 

**[7732.88s] English:** architecture itself right but it's interesting if all of them could be  
**Translation:** 

**[7738.54s] English:** like counting was another one you know being able to kind of understand that there's multiple  
**Translation:** 

**[7745.66s] English:** objects of the same kind in the image and be able to count them i wonder if all of that could be if  
**Translation:** 

**[7751.78s] English:** constructed correctly they can emerge because then you can transfer those concepts to um  
**Translation:** 

**[7757.04s] English:** to then interpret images at a deeper level right counting i do believe i mean should be possible  
**Translation:** Vocabulary: interpret: 解释

**[7764.10s] English:** you don't know like yet but i do think it's not that far in the realm of possible  
**Translation:** 

**[7768.54s] English:** yeah that'd be interesting if using self-supervised learning on images  
**Translation:** 

**[7772.72s] English:** can then be applied to then solving those kinds of iq tests which seem currently to be kind of  
**Translation:** 

**[7777.94s] English:** impossible what idea do you believe might be true that most people think is not true  
**Translation:** 

**[7786.10s] English:** or don't agree with you on is there something like that so this is going to be a little  
**Translation:** 

**[7791.66s] English:** controversial but okay sure i don't believe in simulation like actually using simulation to do  
**Translation:** Vocabulary: simulation: 模拟

**[7796.78s] English:** things very much  
**Translation:** 

**[7798.54s] English:** just to clarify because  
**Translation:** 

**[7800.00s] English:** this is a podcast so you talk about are we living in a simulation often you're referring you're  
**Translation:** 

**[7805.20s] English:** referring to using simulation to construct worlds that you then leverage for machine learning right  
**Translation:** Vocabulary: leverage: 利用

**[7810.54s] English:** yeah for example like one example would be like to train an autonomous car driving system you  
**Translation:** 

**[7815.60s] English:** basically first build a simulator which builds like the environment of the world and then you  
**Translation:** Vocabulary: autonomous: 自主; simulator: 模拟器

**[7820.22s] English:** basically have a lot of like you train your machine learning system in that so i believe it  
**Translation:** 

**[7826.92s] English:** is possible but i think it's a really expensive way of doing things uh and at the end of it you  
**Translation:** 

**[7832.66s] English:** do need the real world so i'm not sure so maybe for certain settings like maybe the payout is so  
**Translation:** 

**[7838.40s] English:** large like for autonomous driving the payout is so large that you can actually invest that much  
**Translation:** Vocabulary: payout: 赔偿金

**[7842.26s] English:** money to build it but i think as a general sort of principle it does not apply to a lot of concepts  
**Translation:** 

**[7846.94s] English:** you can't really build simulations of everything uh not only because like one it's expensive  
**Translation:** 

**[7851.42s] English:** because a second it's also not possible for a lot of things uh so in general like there is a lot of  
**Translation:** 

**[7856.92s] English:** um like there's a lot of work on like using synthetic data and like synthetic simulators i  
**Translation:** Vocabulary: simulators: 模拟器; synthetic: 合成的

**[7862.26s] English:** generally am not very uh like i don't believe in that so you're saying it's very challenging  
**Translation:** 

**[7867.16s] English:** visually like to correctly like simulate the visual like the lighting all those kinds of  
**Translation:** Vocabulary: simulate: 模拟

**[7873.30s] English:** i mean i mean all these companies that you have right so like pixar and like whatever all these  
**Translation:** 

**[7878.14s] English:** companies are if they're all this like computer graphic stuff is really about accurately a lot  
**Translation:** 

**[7883.10s] English:** of them is about like accurately trying to figure out how the lighting  
**Translation:** 

**[7886.92s] English:** is and like how things reflect off of one another and so on and like how sparkly things look and  
**Translation:** 

**[7891.92s] English:** so on so it's a very hard problem so do we really need to solve that first to be able to like do  
**Translation:** 

**[7898.16s] English:** computer vision probably not and for me in the context of autonomous driving it's very tempting  
**Translation:** 

**[7905.68s] English:** to be able to use simulation right because it's a safety critical application but the other  
**Translation:** 

**[7911.98s] English:** limitation of simulation that perhaps is it's a bigger one than the  
**Translation:** Vocabulary: simulation: 模拟

**[7916.92s] English:** visual limitation is the behavior of objects  
**Translation:** 

**[7920.00s] English:** because the so you're ultimately interested in edge cases and the  
**Translation:** 

**[7924.14s] English:** question is how well can you generate edge cases in simulation especially with  
**Translation:** 

**[7929.40s] English:** human behavior I think another problem is like for autonomous driving right  
**Translation:** 

**[7933.44s] English:** it's a constantly changing world so say autonomous driving like in 10 years from  
**Translation:** 

**[7938.12s] English:** now like there are lots of autonomous cars but they're still going to be  
**Translation:** 

**[7941.60s] English:** humans yeah so now there are 50% of the agents say which are humans 50% of the  
**Translation:** 

**[7945.92s] English:** agents that are autonomous like car driving agents so now the mixture is  
**Translation:** Vocabulary: autonomous: 自主的

**[7949.28s] English:** changed so now the kinds of behaviors that you actually expect from the other  
**Translation:** 

**[7952.76s] English:** other agents or other cars on the road that are actually going to be very  
**Translation:** 

**[7955.94s] English:** different and as the proportion of the number of autonomous cars to humans  
**Translation:** 

**[7959.54s] English:** keeps changing this behavior will actually change a lot so now if you were  
**Translation:** 

**[7963.26s] English:** to build a simulator based on just like right now to build them today you don't  
**Translation:** 

**[7966.74s] English:** have that many autonomous cars on the road so you try to like make all of the  
**Translation:** Vocabulary: simulator: 模拟器

**[7969.86s] English:** other agents in that simulator behave as humans but that's not really going to  
**Translation:** 

**[7973.94s] English:** hold true 10 15 20 30 years from now do you think we're living in simulation  
**Translation:** 

**[7978.78s] English:** no  
**Translation:** 

**[7979.28s] English:** no how hard is it this is why I think it's an interesting question how hard is  
**Translation:** 

**[7985.40s] English:** it to build a video game like virtual reality game where it is so real forget  
**Translation:** 

**[7993.08s] English:** like ultra realistic to where you can't tell the difference but like it's so  
**Translation:** Vocabulary: ultra: 超现实

**[7998.36s] English:** nice that you just want to stay there you just want to stay there and you  
**Translation:** 

**[8003.16s] English:** don't want to come back do you think that's anything that's doable within our  
**Translation:** Vocabulary: doable: 可行的

**[8008.26s] English:** lifetime  
**Translation:** 

**[8009.28s] English:** within our lifetime probably yeah are you told they live alone does that make  
**Translation:** 

**[8016.46s] English:** you sad that there will be like like population of kids that basically spend  
**Translation:** 

**[8022.78s] English:** ninety five percent ninety nine percent of their time in a virtual world very  
**Translation:** 

**[8030.30s] English:** very hard question to answer for certain people it might be something that they  
**Translation:** 

**[8036.02s] English:** really derive a lot of value out of there I have a lot of enjoyment of what I love within my life.  
**Translation:** 

**[8038.78s] English:** enjoyment and like happiness  
**Translation:** 

**[8040.00s] English:** out of and maybe the real world wasn't giving them that that's why they did that so maybe it  
**Translation:** 

**[8044.46s] English:** is good for certain people so ultimately if it maximizes happiness right i think you judge yeah  
**Translation:** 

**[8051.00s] English:** i think if it's making people happy maybe it's okay uh again i think it's this is a very hard  
**Translation:** Vocabulary: maximizes: 最大化

**[8056.22s] English:** question uh so like you've uh you've been a part of a lot of amazing papers what advice would you  
**Translation:** 

**[8064.58s] English:** give to somebody on uh what it takes to write a good paper grad students writing papers now is  
**Translation:** 

**[8071.12s] English:** there um is there common things that you've learned along the way that you think it takes  
**Translation:** 

**[8075.42s] English:** both for a good idea and a good paper right so i think um both of these i've picked up from  
**Translation:** 

**[8084.34s] English:** like lots of people i've worked with in the past so one of them is picking the right problem to  
**Translation:** 

**[8088.78s] English:** work on in research is as important as like this like finding the solution to it so  
**Translation:** 

**[8093.94s] English:** you  
**Translation:** 

**[8094.58s] English:** i mean there are multiple reasons for this so one is that there are certain problems that can  
**Translation:** 

**[8099.24s] English:** actually be solved uh in in a particular time frame so now say you want to work on finding  
**Translation:** 

**[8104.90s] English:** the meaning of life this is a great problem i think most people will agree with that but do  
**Translation:** 

**[8110.36s] English:** you believe that you your talents and like the energy that you'll spend on it will make a meaning  
**Translation:** 

**[8115.38s] English:** like make some kind of meaningful progress in your lifetime if you are optimistic about it then like  
**Translation:** 

**[8120.56s] English:** go ahead that's why i started this podcast i keep asking people about the meaning of life i'm hoping  
**Translation:** 

**[8124.58s] English:** not okay either that's okay i will do it longer because not okay i hope every opportunity comes  
**Translation:** 

**[8126.34s] English:** by episode like 220 i'll figure it out so  
**Translation:** 

**[8130.74s] English:** not too many episodes to go all right maybe today i don't know but you're right so that that's uh  
**Translation:** 

**[8137.50s] English:** seems intractable at the moment right so i think it's just the fact of like if you're starting a  
**Translation:** 

**[8142.24s] English:** phd for example what is one problem that you want to focus on that you do think is interesting  
**Translation:** Vocabulary: intractable: 难以解决

**[8147.10s] English:** enough uh and you will be able to make a reasonable amount of headway into it that you think you'll  
**Translation:** 

**[8151.44s] English:** be doing a phd for so in that kind of a time frame  
**Translation:** 

**[8154.36s] English:** second part, which is what excites you genuinely.  
**Translation:** 

**[8156.44s] English:** So you shouldn't just pick problems that you are not excited about because as a  
**Translation:** Vocabulary: excites: 激发兴趣

**[8160.00s] English:** grad student or as a researcher you really need to be passionate about it to continue doing that  
**Translation:** 

**[8164.48s] English:** because there are so many other things that you could be doing in life so you really need to  
**Translation:** 

**[8167.62s] English:** believe in that to be able to do that for that long in terms of papers i think the one thing  
**Translation:** 

**[8172.58s] English:** that i've learned is i've like in the past whenever i used to write things and even now  
**Translation:** 

**[8178.22s] English:** whenever i do that i try to cram in a lot of things into the paper whereas what really matters  
**Translation:** 

**[8182.58s] English:** is just pushing one simple idea that's it that's all because that's the paper is going to be like  
**Translation:** 

**[8189.90s] English:** whatever eight or nine pages if you keep cramming in lots of ideas it's really hard for the single  
**Translation:** 

**[8195.88s] English:** thing that you believe in to stand out so if you really try to just focus like especially in terms  
**Translation:** Vocabulary: cramming: 填塞内容

**[8201.42s] English:** of writing really try to focus on one particular idea and articulate it out in multiple different  
**Translation:** 

**[8205.90s] English:** ways it's far more valuable to the reader as well and basically uh to the reader of course because  
**Translation:** Vocabulary: articulate: 表达清晰

**[8211.72s] English:** they get to they know that this particular idea is associated with this paper and also for you  
**Translation:** 

**[8216.82s] English:** because uh you have like when you write about a  
**Translation:** 

**[8219.88s] English:** idea in different ways, you think about it more deeply. So as a grad student, I used to always  
**Translation:** 

**[8224.26s] English:** wait to it, like maybe in the last week or whatever to write the paper, because I used to  
**Translation:** 

**[8229.72s] English:** always believe that doing the experiments was actually the bigger part of research than writing.  
**Translation:** 

**[8233.70s] English:** And my advisor always told me that you should start writing very early on. And I thought,  
**Translation:** 

**[8237.08s] English:** oh, it doesn't matter. I don't know what he's talking about. But I think more and more,  
**Translation:** 

**[8240.74s] English:** I realized that's the case. Like whenever I write something that I'm doing, I actually think much  
**Translation:** 

**[8245.08s] English:** better about it. And so if you start writing earlier, early on, you actually, I think,  
**Translation:** 

**[8250.02s] English:** get better ideas, or at least you figure out like holes in your theory or like particular  
**Translation:** 

**[8254.84s] English:** experiments that you should run to plug those holes and so on. Yeah, I'm continually surprised  
**Translation:** 

**[8260.06s] English:** how many really good papers throughout history are quite short and quite simple.  
**Translation:** 

**[8267.90s] English:** And there's a lesson to that. Like if you want to dream about writing a paper that changes the world  
**Translation:** 

**[8273.56s] English:** and you want to go back and forth, you can do it.  
**Translation:** 

**[8275.08s] English:** By example, they're usually simple.  
**Translation:** 

**[8277.98s] English:** Yeah, yeah.  
**Translation:** 

**[8278.94s] English:** And that's...  
**Translation:** 

**[8280.00s] English:** It's not cramming or it's focusing on one idea and thinking deeply.  
**Translation:** 

**[8287.14s] English:** And you're right that the writing process itself reveals the idea.  
**Translation:** 

**[8292.22s] English:** It challenges you to really think about what is the idea that explains it, the thread that ties it all together.  
**Translation:** 

**[8298.66s] English:** And so a lot of famous researchers I know actually would start off, like, first, even before the experiments were in, a lot of them would actually start with writing the introduction of the paper.  
**Translation:** 

**[8310.00s] English:** With zero experiments in.  
**Translation:** 

**[8311.88s] English:** Because that at least helps them figure out what they're trying to solve and how it fits in the context of things right now.  
**Translation:** 

**[8318.68s] English:** And that would really guide their entire research.  
**Translation:** 

**[8320.68s] English:** So a lot of them would actually first write an intros with zero experiments in and that's how they would start projects.  
**Translation:** 

**[8325.78s] English:** Some basic questions about people maybe that are more like beginners in this field.  
**Translation:** Vocabulary: intros: 引言

**[8331.86s] English:** What's the best programming language to learn if you're interested in machine learning?  
**Translation:** 

**[8336.24s] English:** I would say Python just because it's the easiest one to learn.  
**Translation:** 

**[8340.00s] English:** And also a lot of programming in machine learning happens in Python.  
**Translation:** 

**[8345.06s] English:** So if you don't know any other programming language, Python is actually going to get you a long way.  
**Translation:** 

**[8349.58s] English:** Yeah, it seems like sort of it's a toss-up question because it seems like Python is so much dominating the space now.  
**Translation:** 

**[8356.54s] English:** But I wonder if there's an interesting alternative.  
**Translation:** Vocabulary: dominating: 占据主导

**[8358.50s] English:** Obviously, there's Swift and there's a lot of interesting alternatives popping up, even JavaScript or R, more like for the data science applications.  
**Translation:** 

**[8368.66s] English:** But it seems like Python.  
**Translation:** 

**[8370.00s] English:** Python, more and more is actually being used to teach like introduction of programming at universities.  
**Translation:** 

**[8375.78s] English:** So it just combines everything very nicely.  
**Translation:** 

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

**[8391.26s] English:** So a disclaimer to this is that the last time I used TensorFlow was probably like four years ago.  
**Translation:** 

**[8396.42s] English:** And so it was right when it had come out.  
**Translation:** 

**[8397.88s] English:** Because so I started.  
**Translation:** 

**[8400.00s] English:** on like deep learning in 2014 or so.  
**Translation:** 

**[8402.66s] English:** And the dominant sort of framework for us then  
**Translation:** 

**[8406.42s] English:** for vision was Cafe, which was out of Berkeley.  
**Translation:** 

**[8409.04s] English:** And we used Cafe a lot, it was really nice.  
**Translation:** Vocabulary: berkeley: 伯克利

**[8412.12s] English:** And then TensorFlow came in,  
**Translation:** 

**[8413.36s] English:** which was basically like Python first.  
**Translation:** 

**[8415.10s] English:** So Cafe was mainly C++  
**Translation:** 

**[8417.04s] English:** and it had like very loose kind of Python binding.  
**Translation:** 

**[8419.04s] English:** So Python wasn't really the first language you would use.  
**Translation:** 

**[8421.34s] English:** You would really use either MATLAB or C++  
**Translation:** 

**[8424.70s] English:** to like get stuff done in like Cafe.  
**Translation:** 

**[8428.24s] English:** And then Python, of course, became popular  
**Translation:** 

**[8429.68s] English:** a little bit later.  
**Translation:** 

**[8430.94s] English:** So TensorFlow was basically around that time.  
**Translation:** 

**[8432.62s] English:** So 2015, 2016 is when I last used it.  
**Translation:** 

**[8436.12s] English:** It's been a while.  
**Translation:** 

**[8437.20s] English:** And then what, did you use Torch or did you?  
**Translation:** 

**[8440.60s] English:** So then I moved to LuaTorch, which was the Torch in Lua.  
**Translation:** 

**[8444.02s] English:** And then in 2017, I think basically pretty much  
**Translation:** 

**[8446.78s] English:** to PyTorch completely.  
**Translation:** 

**[8448.42s] English:** Oh, interesting, so you went to Lua, cool.  
**Translation:** 

**[8450.52s] English:** Yeah.  
**Translation:** 

**[8451.48s] English:** Huh, so you were there before it was cool.  
**Translation:** 

**[8454.20s] English:** Yeah, I mean, so LuaTorch was really good  
**Translation:** 

**[8456.32s] English:** because it,  
**Translation:** 

**[8458.24s] English:** it actually allowed you to do  
**Translation:** 

**[8459.24s] English:** a lot of different kinds of things.  
**Translation:** 

**[8461.34s] English:** So which Cafe was very rigid in terms of its structure.  
**Translation:** 

**[8463.90s] English:** Like you would create a neural network once and that's it.  
**Translation:** 

**[8466.80s] English:** Whereas if you wanted like very dynamic graphs and so on,  
**Translation:** Vocabulary: neural: 神经网络

**[8469.32s] English:** it was very hard to do that.  
**Translation:** 

**[8470.22s] English:** And LuaTorch was much more friendly for all of these things.  
**Translation:** 

**[8473.56s] English:** Okay, so in terms of PyTorch and TensorFlow,  
**Translation:** 

**[8475.60s] English:** my personal bias is PyTorch  
**Translation:** 

**[8477.28s] English:** just because I've been using it longer  
**Translation:** 

**[8479.08s] English:** and I'm more familiar with it.  
**Translation:** 

**[8480.78s] English:** And also that PyTorch is much easier to debug  
**Translation:** 

**[8483.56s] English:** is what I find because it's imperative in nature  
**Translation:** Vocabulary: imperative: 命令式的

**[8486.30s] English:** compared to like TensorFlow, which is not imperative.  
**Translation:** 

**[8488.24s] English:** But that's telling you a lot that basically  
**Translation:** 

**[8490.48s] English:** the imperative design is sort of a way  
**Translation:** 

**[8493.32s] English:** in which a lot of people are taught programming  
**Translation:** 

**[8495.22s] English:** and that's what actually makes debugging easier for them.  
**Translation:** 

**[8498.14s] English:** So like I learned programming in C++  
**Translation:** 

**[8500.48s] English:** and so for me, imperative way of programming is more natural.  
**Translation:** 

**[8504.04s] English:** Do you think it's good to have  
**Translation:** 

**[8505.28s] English:** kind of these two communities, this kind of competition?  
**Translation:** 

**[8508.48s] English:** I think PyTorch is kind of more and more becoming dominant  
**Translation:** 

**[8511.50s] English:** in the research community,  
**Translation:** 

**[8512.50s] English:** but TensorFlow is still very popular  
**Translation:** 

**[8514.58s] English:** in the more sort of application machine learning community.  
**Translation:** 

**[8517.90s] English:** So do you think it's good to have that kind  
**Translation:** 

**[8520.00s] English:** split in code bases or um so like the benefit there is the competition challenges the library  
**Translation:** 

**[8527.10s] English:** developers to step up their game yeah but the downside is there's these code bases uh that are  
**Translation:** Vocabulary: downside: 缺点

**[8533.22s] English:** in different different libraries right so i think the downside is that i mean for a lot of research  
**Translation:** 

**[8538.22s] English:** code that's released in one framework and if you're using the other one it's really hard  
**Translation:** 

**[8541.20s] English:** to like really build on top of it but thankfully the open source community in machine learning is  
**Translation:** 

**[8546.46s] English:** amazing so yeah whenever like something pops up in tensorflow uh you wait a few days and someone  
**Translation:** 

**[8552.12s] English:** who's like super sharp will actually come and translate that particular code base into pytorch  
**Translation:** 

**[8556.08s] English:** and it will and basically have figured that all those nooks and crannies out so the open source  
**Translation:** Vocabulary: crannies: 角落; nooks: 角落

**[8560.72s] English:** community is amazing and they really like figure out this uh gap uh so i think in terms of like  
**Translation:** 

**[8566.38s] English:** having these two frameworks or multiple i think of course there are different use cases so there  
**Translation:** 

**[8570.00s] English:** are going to be benefits to using one or the other framework and like you said i think competition is  
**Translation:** 

**[8574.18s] English:** just healthy because uh both of them are going to have a lot of benefits to using one or the other  
**Translation:** 

**[8576.44s] English:** so i think it's really important to have a lot of these frameworks keep or like all of these  
**Translation:** 

**[8578.44s] English:** frameworks really sort of keep learning from each other and keep incorporating different things to  
**Translation:** Vocabulary: incorporating: 吸收

**[8581.80s] English:** just make them better and better what advice would you have for someone new to machine learning  
**Translation:** 

**[8588.44s] English:** you know uh maybe just started or haven't even started but are curious about it and who want  
**Translation:** 

**[8593.16s] English:** to get in the field don't be afraid to get your hands dirty i think that's the main thing so if  
**Translation:** 

**[8597.72s] English:** something doesn't work like really drill into why things are not working can you elaborate  
**Translation:** Vocabulary: elaborate: 详细说明

**[8603.08s] English:** what your hands dirty means right so for example  
**Translation:** 

**[8606.20s] English:** like if you want to get your hands dirty you can get your hands dirty you can get your hands dirty  
**Translation:** 

**[8606.36s] English:** like if you want to get your hands dirty you can get your hands dirty you can get your hands dirty  
**Translation:** 

**[8606.42s] English:** like if an algorithm if you try to train the network and it's not converging whatever rather  
**Translation:** Vocabulary: algorithm: 算法; converging: 收敛

**[8610.26s] English:** than trying to like google the answer or trying to do something like really spend those like 5 8 10  
**Translation:** 

**[8615.54s] English:** 15 20 whatever number of hours really trying to figure it out yourself because in that process  
**Translation:** 

**[8619.78s] English:** you'll actually learn a lot more yeah uh googling is of course like a good way to solve it when you  
**Translation:** 

**[8624.74s] English:** need a quick answer but i think initially especially like when you're starting out  
**Translation:** Vocabulary: googling: 上网搜索

**[8628.18s] English:** it's much nicer to like figure things out by yourself and i just say that from experience  
**Translation:** 

**[8632.82s] English:** because like when i started out there were not a lot of resources so we would like in  
**Translation:** 

**[8636.34s] English:** the lab a lot of us like we would look up to senior students and  
**Translation:** 

**[8640.00s] English:** And the senior students were, of course, busy.  
**Translation:** 

**[8641.40s] English:** And they would be like, hey, why don't you go figure it out?  
**Translation:** 

**[8643.08s] English:** Because I just don't have the time.  
**Translation:** 

**[8644.32s] English:** I'm working on my dissertation or whatever.  
**Translation:** 

**[8646.42s] English:** I'll find other PhD students.  
**Translation:** Vocabulary: dissertation: 论文

**[8647.70s] English:** And so then we would sit down and just try to figure it out.  
**Translation:** 

**[8650.46s] English:** And that, I think, really helped me.  
**Translation:** 

**[8652.40s] English:** That has really helped me figure a lot of things out.  
**Translation:** 

**[8654.78s] English:** I think in general, if I were to generalize that,  
**Translation:** Vocabulary: generalize: 概括

**[8658.64s] English:** I feel like persevering through any kind of struggle  
**Translation:** 

**[8661.92s] English:** on a thing you care about is good.  
**Translation:** Vocabulary: persevering: 坚持不懈

**[8665.32s] English:** So you're basically, you try to make it seem like it's good to,  
**Translation:** 

**[8668.66s] English:** you know, spend time debugging.  
**Translation:** 

**[8670.76s] English:** But really, any kind of struggle, whatever form that takes.  
**Translation:** 

**[8673.64s] English:** It could be just Googling a lot.  
**Translation:** 

**[8676.06s] English:** Just basically anything, just sticking with it  
**Translation:** 

**[8678.68s] English:** and going through the hard thing.  
**Translation:** Vocabulary: sticking: 坚持不懈

**[8679.84s] English:** That could take a form of implementing stuff from scratch.  
**Translation:** 

**[8683.16s] English:** It could take the form of re-implementing  
**Translation:** Vocabulary: implementing: 实施

**[8685.58s] English:** with different libraries or different programming languages.  
**Translation:** 

**[8689.02s] English:** It could take a lot of different forms.  
**Translation:** 

**[8690.62s] English:** But struggle is good for the soul.  
**Translation:** 

**[8693.50s] English:** So like in Pittsburgh, where I did my PhD,  
**Translation:** 

**[8695.86s] English:** the thing was it used to snow a lot.  
**Translation:** 

**[8697.26s] English:** Yeah.  
**Translation:** 

**[8698.04s] English:** And so.  
**Translation:** 

**[8698.76s] English:** When it was snowed, you really couldn't do much.  
**Translation:** 

**[8700.96s] English:** So the thing that a lot of people said was snow builds character.  
**Translation:** 

**[8705.14s] English:** Because when it's snowing, you can't do anything else.  
**Translation:** 

**[8707.44s] English:** You focus on work.  
**Translation:** 

**[8709.10s] English:** Do you have advice in general for people?  
**Translation:** 

**[8710.86s] English:** You've already exceptionally successful.  
**Translation:** 

**[8712.62s] English:** You're young.  
**Translation:** Vocabulary: exceptionally: 特别地

**[8713.42s] English:** But do you have advice for young people starting out in college  
**Translation:** 

**[8716.18s] English:** or maybe in high school?  
**Translation:** 

**[8717.84s] English:** You know, advice for their career, advice for their life,  
**Translation:** 

**[8721.08s] English:** how to pave a successful path in career and life?  
**Translation:** 

**[8725.64s] English:** I would say just be hungry.  
**Translation:** 

**[8727.18s] English:** Like always be hungry.  
**Translation:** 

**[8728.36s] English:** Be hungry for what you want.  
**Translation:** 

**[8729.58s] English:** And I think like I've been inspired by a lot of people who are just like driven  
**Translation:** 

**[8734.36s] English:** and who really like go for what they want, no matter what.  
**Translation:** 

**[8737.60s] English:** Like you shouldn't want it.  
**Translation:** 

**[8739.36s] English:** You should need it.  
**Translation:** 

**[8740.40s] English:** So if you need something, you basically go towards the ends to make it work.  
**Translation:** 

**[8744.28s] English:** How do you know when you come across a thing that that's like you need?  
**Translation:** 

**[8751.04s] English:** I think there's not going to be any single thing that you're going to need.  
**Translation:** 

**[8753.66s] English:** There are going to be different types of things that you need.  
**Translation:** 

**[8755.28s] English:** But whenever you need something, you just go push for it.  
**Translation:** 

**[8757.58s] English:** And of course, once you you may not get it,  
**Translation:** 

**[8760.00s] English:** or you may find that this was not even the thing that you were looking for it might be a different  
**Translation:** 

**[8763.38s] English:** thing but the point is like you're pushing through things and that actually gives you  
**Translation:** 

**[8767.36s] English:** brings a lot of skills and brings a lot of uh like build a certain kind of attitude which will  
**Translation:** 

**[8773.14s] English:** probably help you get the other thing once you figure out what's really the thing that you want  
**Translation:** 

**[8777.84s] English:** yeah i think a lot of people are i've noticed the kind of afraid of that is because one it's a fear  
**Translation:** 

**[8783.62s] English:** of commitment and two there's so many amazing things in this world you almost don't want to  
**Translation:** 

**[8787.66s] English:** miss out on all the other amazing things by committing to this one thing so i think a lot  
**Translation:** 

**[8791.72s] English:** of it has to do with just allowing yourself to uh like notice that thing and uh just go all the way  
**Translation:** 

**[8800.58s] English:** with it i mean i also like failure right so yeah i know this is like super cheesy that you know  
**Translation:** Vocabulary: cheesy: 俗气

**[8806.80s] English:** failure is something that you should be prepared for and so on but i do think i mean especially  
**Translation:** 

**[8811.92s] English:** in research for example failure is something that happens almost like almost every day is like  
**Translation:** 

**[8816.74s] English:** experimental  
**Translation:** 

**[8817.66s] English:** failing and not working and so you really need to be so used to it you need to have a thick skin  
**Translation:** 

**[8823.24s] English:** but and only basically through like when you get through it is when you find the one thing that's  
**Translation:** 

**[8828.46s] English:** actually working like thomas edison was like one person like that right so i really like when i was  
**Translation:** Vocabulary: edison: 爱迪生

**[8833.42s] English:** a kid i used to really read about how he uh found like the filament the light bulb filament and then  
**Translation:** 

**[8839.02s] English:** he i think his thing was like he tried 990 things that didn't work or something of the sort yeah and  
**Translation:** Vocabulary: filament: 灯丝

**[8844.50s] English:** then they asked him like so what did you learn uh because all of these  
**Translation:** 

**[8847.66s] English:** are failed experiments and then he says oh these 990 things don't work and i know that did you know  
**Translation:** 

**[8852.60s] English:** that i mean that's really inspiring uh so you spent a few years on this earth performing a  
**Translation:** 

**[8859.14s] English:** self-supervised um kind of learning process have you figured out the meaning of life yet  
**Translation:** 

**[8865.58s] English:** i told you i'm doing this podcast to try to get the answer i'm hoping you could tell me what do  
**Translation:** 

**[8870.96s] English:** you think the meaning of it all is uh i don't think i figured this out no i have no idea  
**Translation:** 

**[8877.66s] English:** uh do you think uh  
**Translation:** 

**[8880.00s] English:** Do you think AI will help us figure it out?  
**Translation:** 

**[8882.50s] English:** Or do you think there's no answer?  
**Translation:** 

**[8883.86s] English:** The whole point is to keep searching.  
**Translation:** 

**[8885.50s] English:** I think it's an endless sort of quest for us.  
**Translation:** 

**[8888.80s] English:** I don't think AI will help us there.  
**Translation:** 

**[8890.56s] English:** This is like a very hard, hard, hard question  
**Translation:** 

**[8893.50s] English:** which so many humans have tried to answer.  
**Translation:** 

**[8895.40s] English:** Well, that's the interesting thing about the difference between AI and humans.  
**Translation:** 

**[8899.44s] English:** Humans don't seem to know what the hell they're doing.  
**Translation:** 

**[8901.30s] English:** And AI is almost always operating under well-defined objective functions.  
**Translation:** 

**[8907.12s] English:** And I wonder whether our lack of ability  
**Translation:** 

**[8913.54s] English:** to define good long-term objective functions  
**Translation:** 

**[8917.10s] English:** or introspect what is the objective function under which we operate,  
**Translation:** Vocabulary: introspect: 自我反思

**[8921.94s] English:** if that's a feature or a bug.  
**Translation:** 

**[8924.30s] English:** I would say it's a feature  
**Translation:** 

**[8925.10s] English:** because then everyone actually has very different kinds of objective functions  
**Translation:** 

**[8928.28s] English:** that they're optimizing.  
**Translation:** 

**[8929.12s] English:** And those objective functions evolve and change dramatically  
**Translation:** 

**[8932.54s] English:** through the course of their life.  
**Translation:** Vocabulary: dramatically: 剧烈地

**[8933.90s] English:** That's actually what makes us interesting, right?  
**Translation:** 

**[8936.36s] English:** Otherwise,  
**Translation:** 

**[8937.12s] English:** if everyone was doing the exact same thing,  
**Translation:** 

**[8939.10s] English:** that would be pretty boring.  
**Translation:** 

**[8940.46s] English:** We do want people with different kinds of perspectives.  
**Translation:** 

**[8943.80s] English:** Also, people evolve continuously.  
**Translation:** Vocabulary: perspectives: 观点

**[8946.24s] English:** That's, I would say, the biggest feature of being human.  
**Translation:** 

**[8949.30s] English:** And then we get to the ones that die  
**Translation:** 

**[8951.08s] English:** because they do something stupid.  
**Translation:** 

**[8952.52s] English:** We get to watch that, see it, and learn from it.  
**Translation:** 

**[8955.54s] English:** And as a species,  
**Translation:** 

**[8957.74s] English:** we take that lesson and become better and better  
**Translation:** 

**[8961.84s] English:** because of all the dumb people in the world  
**Translation:** 

**[8964.22s] English:** that died doing something wild.  
**Translation:** 

**[8967.12s] English:** And beautiful.  
**Translation:** 

**[8969.06s] English:** Ishan, thank you so much for this incredible conversation.  
**Translation:** 

**[8971.76s] English:** We did a depth-first search  
**Translation:** 

**[8973.98s] English:** through the space of machine learning,  
**Translation:** 

**[8977.80s] English:** and it was fun and fascinating.  
**Translation:** 

**[8981.70s] English:** So it's really an honor to meet you,  
**Translation:** 

**[8983.94s] English:** and it was a really awesome conversation.  
**Translation:** 

**[8985.78s] English:** Thanks for coming down today and talking with me.  
**Translation:** 

**[8988.00s] English:** Thanks, Lex.  
**Translation:** 

**[8988.60s] English:** I mean, I've listened to you.  
**Translation:** 

**[8990.24s] English:** I told you it was unreal for me to actually meet you in person,  
**Translation:** 

**[8992.94s] English:** and I'm so happy to be here.  
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

**[9000.00s] English:** on it, the information, Grammarly and Athletic Greens. Check them out in the description to  
**Translation:** 

**[9006.88s] English:** support this podcast. And now, let me leave you with some words from Arthur C. Clarke.  
**Translation:** Vocabulary: grammarly: 语法检查

**[9012.48s] English:** Any sufficiently advanced technology is indistinguishable from magic.  
**Translation:** 

**[9017.84s] English:** Thank you for listening and hope to see you next time.  
**Translation:** Vocabulary: sufficiently: 足够地


<!-- TRANSCRIPTION_COMPLETE -->
