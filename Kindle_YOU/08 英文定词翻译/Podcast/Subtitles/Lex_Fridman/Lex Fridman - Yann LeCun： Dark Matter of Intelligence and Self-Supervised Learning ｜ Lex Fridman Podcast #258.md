# Podcast vocabulary notes
Source file: Lex Fridman - Yann LeCun： Dark Matter of Intelligence and Self-Supervised Learning ｜ Lex Fridman Podcast #258.opus

**[0.00s] English:** The following is a conversation with Jan LeCun, his second time on the podcast.  
**Translation:** 

**[4.78s] English:** He is the chief AI scientist at Meta, formerly Facebook, professor at NYU, Turing Award winner,  
**Translation:** Vocabulary: turing: 图灵奖

**[13.08s] English:** one of the seminal figures in the history of machine learning and artificial intelligence,  
**Translation:** 

**[18.46s] English:** and someone who is brilliant and opinionated in the best kind of way.  
**Translation:** Vocabulary: seminal: 开创性的

**[23.50s] English:** And so it's always fun to talk to.  
**Translation:** 

**[25.72s] English:** This is the Lex Friedman Podcast.  
**Translation:** Vocabulary: friedman: 弗里德曼

**[27.74s] English:** To support it, please check out our sponsors in the description.  
**Translation:** 

**[31.24s] English:** And now, here's my conversation with Jan LeCun.  
**Translation:** Vocabulary: sponsors: 赞助商

**[35.72s] English:** You co-wrote the article, Self-Supervised Learning, The Dark Matter of Intelligence.  
**Translation:** 

**[40.88s] English:** Great title, by the way, with Ishan Mizra.  
**Translation:** 

**[43.56s] English:** So let me ask, what is self-supervised learning and why is it the dark matter of intelligence?  
**Translation:** 

**[49.56s] English:** I'll start by the dark matter part.  
**Translation:** 

**[52.96s] English:** There is obviously a kind of learning that humans and animals are,  
**Translation:** 

**[57.74s] English:** are doing that we currently are not reproducing properly with machines, with AI, right?  
**Translation:** 

**[64.66s] English:** So the most popular approaches to machine learning today are, or paradigms, I should say,  
**Translation:** 

**[69.72s] English:** are supervised learning and reinforcement learning.  
**Translation:** Vocabulary: paradigms: 范式; reinforcement: 强化; supervised: 监督

**[72.54s] English:** And they are extremely inefficient.  
**Translation:** 

**[75.24s] English:** Supervised learning requires many samples for learning anything.  
**Translation:** Vocabulary: inefficient: 低效

**[79.82s] English:** And reinforcement learning requires a ridiculously large number of trials and errors for a system to learn anything.  
**Translation:** 

**[87.74s] English:** And that's why we don't have self-driving cars.  
**Translation:** Vocabulary: ridiculously: 极其

**[92.96s] English:** That's a big leap from one to the other.  
**Translation:** 

**[94.78s] English:** Okay, so that to solve difficult problems, you have to have a lot of human annotations for supervised learning to work.  
**Translation:** Vocabulary: annotations: 标注示例

**[104.08s] English:** And to solve those difficult problems with reinforcement learning, you have to have some way to maybe simulate that problem such that you can do that large scale kind of learning that reinforcement learning requires.  
**Translation:** 

**[114.38s] English:** Right.  
**Translation:** Vocabulary: simulate: 模拟

**[114.74s] English:** So how is it that, you know,  
**Translation:** 

**[117.02s] English:** most engineers,  
**Translation:** 

**[117.62s] English:** most teenagers can learn to drive a car in about 20 hours?  
**Translation:** 

**[120.00s] English:** hours of practice, whereas even with millions of hours of simulated practice, a self-driving  
**Translation:** 

**[127.88s] English:** car can't actually learn to drive itself properly.  
**Translation:** 

**[132.20s] English:** And so obviously we're missing something, right?  
**Translation:** 

**[134.26s] English:** And it's quite obvious for a lot of people that the immediate response you get from many  
**Translation:** 

**[139.12s] English:** people is, well, humans use their background knowledge to learn faster.  
**Translation:** 

**[144.80s] English:** And they're right.  
**Translation:** 

**[145.96s] English:** Now how was that background knowledge acquired?  
**Translation:** 

**[148.40s] English:** And that's the big question.  
**Translation:** 

**[150.20s] English:** So now you have to ask, you know, how do babies in their first few months of life learn how  
**Translation:** 

**[155.84s] English:** the world works?  
**Translation:** 

**[157.34s] English:** Mostly by observation, because they can hardly act in the world.  
**Translation:** 

**[161.44s] English:** And they learn an enormous amount of background knowledge about the world.  
**Translation:** 

**[164.14s] English:** That may be the basis of what we call common sense.  
**Translation:** 

**[168.30s] English:** This type of learning, it's not learning a task, it's not being reinforced for anything,  
**Translation:** 

**[173.80s] English:** it's just observing the world and figuring out how it works.  
**Translation:** Vocabulary: reinforced: 强化

**[178.38s] English:** Building world models, learning world models.  
**Translation:** 

**[181.28s] English:** How do we do this?  
**Translation:** 

**[182.42s] English:** And how do we reproduce this in machines?  
**Translation:** 

**[184.60s] English:** So self-supervised learning is one instance or one attempt at trying to reproduce this  
**Translation:** 

**[191.48s] English:** kind of learning.  
**Translation:** 

**[192.48s] English:** Okay.  
**Translation:** 

**[193.48s] English:** So you're looking at just observation, so not even the interacting part of a child.  
**Translation:** 

**[198.82s] English:** It's just sitting there watching mom and dad walk around, pick up stuff, all of that.  
**Translation:** 

**[203.68s] English:** That's what you mean about background knowledge.  
**Translation:** 

**[205.36s] English:** Perhaps.  
**Translation:** 

**[206.36s] English:** Not even watching mom and dad.  
**Translation:** 

**[207.36s] English:** Just, you know, watching.  
**Translation:** 

**[208.36s] English:** Watching the world go by.  
**Translation:** 

**[210.12s] English:** Just having eyes open or having eyes closed, or the very act of opening and closing eyes,  
**Translation:** 

**[214.60s] English:** that the world appears and disappears, all of that basic information.  
**Translation:** 

**[218.02s] English:** And you're saying in order to learn to drive, like the reason humans are able to learn to  
**Translation:** 

**[224.90s] English:** drive quickly, some faster than others, is because of the background knowledge.  
**Translation:** 

**[228.60s] English:** They were able to watch cars operate in the world in the many years leading up to it,  
**Translation:** 

**[233.64s] English:** the physics of basic objects and all that kind of stuff.  
**Translation:** 

**[236.26s] English:** That's right.  
**Translation:** 

**[237.26s] English:** You don't even know, you don't even need to know, you know, how to drive.  
**Translation:** 

**[240.00s] English:** car works right because that you can learn fairly quickly i mean the example i use very often is  
**Translation:** 

**[244.24s] English:** you're driving next to a cliff and you know in advance because of your you know understanding  
**Translation:** 

**[250.48s] English:** of intuitive physics that uh if you turn the wheel to the right the car will veer to the right  
**Translation:** Vocabulary: intuitive: 直觉的

**[254.96s] English:** we'll run off the cliff fall off the cliff and nothing good will come out of this right  
**Translation:** 

**[259.76s] English:** um but if you are a sort of you know tabula rasa reinforcement learning system that doesn't have  
**Translation:** Vocabulary: reinforcement: 强化学习; tabula: 白板理论

**[265.84s] English:** a model of the world you have to repeat falling off this cliff thousands of times before you  
**Translation:** 

**[271.52s] English:** figure out it's a bad idea and then a few more thousand times before you figure out how to not  
**Translation:** 

**[276.08s] English:** do it and then a few more million times before you figure out how to not do it in every situation you  
**Translation:** 

**[280.72s] English:** ever encounter so self-supervised learning still has to have some source of truth being told to  
**Translation:** 

**[288.72s] English:** it by somebody and so you have to figure out a way without human assistance or without significant  
**Translation:** 

**[295.36s] English:** amount of human power to do it and you have to figure out a way without human assistance or  
**Translation:** 

**[295.84s] English:** without human assistance to get that truth from the world so the mystery there is um  
**Translation:** 

**[302.00s] English:** how much signal is there how much truth is there that the world gives you whether it's  
**Translation:** 

**[306.56s] English:** the human world like you watch youtube or something like that or it's the more natural  
**Translation:** 

**[311.92s] English:** world so how much signal is there so here is the trick there is way more signal in sort of a cell  
**Translation:** 

**[319.52s] English:** supervised setting than there is in either a supervised or reinforcement setting and this is  
**Translation:** 

**[324.88s] English:** going to my  
**Translation:** Vocabulary: supervised: 监督学习

**[325.84s] English:** you know analogy of the cake uh the you know look cake has someone that's called it where  
**Translation:** 

**[333.28s] English:** when you try to figure out how much information you ask the machine to predict and how much  
**Translation:** 

**[338.24s] English:** feedback you give the machine at every trial in reinforcement learning you give the machine a  
**Translation:** 

**[342.56s] English:** single scalar you tell the machine you did good you did bad and you and you and you only tell this to  
**Translation:** Vocabulary: scalar: 标量奖励

**[347.84s] English:** the machine once in a while when i say you it could be the universe telling the machine right  
**Translation:** 

**[354.00s] English:** but it's just one scalar  
**Translation:** 

**[355.84s] English:** so as a consequence there is you cannot possibly learn something very complicated without many  
**Translation:** 

**[360.00s] English:** many many trials where you get many many feedbacks of this type supervised learning you you give a  
**Translation:** Vocabulary: cannot: 不可能; feedbacks: 回饋

**[366.96s] English:** few bits to the machine at every every sample let's say you're training a system on you know  
**Translation:** 

**[374.24s] English:** recognizing images on image net there is 1000 categories that a little less than 10 bits of  
**Translation:** 

**[379.04s] English:** information per sample but cell supervised running here is the setting you ideally we don't know how  
**Translation:** 

**[385.60s] English:** to do this yet but ideally you would show a machine a segment of a video and then stop the  
**Translation:** 

**[392.08s] English:** video and ask the machine to predict what's going to happen next and so you let the machine predict  
**Translation:** 

**[398.64s] English:** and then you let time go by and show the machine what actually happened and hope the machine will  
**Translation:** 

**[405.84s] English:** you know learn to do a better job at predicting next time around there's a huge amount of  
**Translation:** 

**[410.40s] English:** information you give the machine because it's an entire video clip  
**Translation:** 

**[414.56s] English:** of  
**Translation:** 

**[415.60s] English:** you know the future after the video clip you fed it um in the first place so both for language and  
**Translation:** 

**[421.28s] English:** for vision there's a subtle seemingly trivial construction but maybe that's representative of  
**Translation:** 

**[428.56s] English:** what is required to create intelligence which is filling the gap so the gaps it sounds dumb but can  
**Translation:** 

**[437.36s] English:** you it's it is possible you can solve all of intelligence in this way just for both language  
**Translation:** 

**[445.20s] English:** just  
**Translation:** 

**[446.32s] English:** give a sentence and continue it or give a sentence and there's a gap in it  
**Translation:** 

**[451.04s] English:** uh some words blanked out and you fill in what words go there for vision you give a sequence  
**Translation:** 

**[457.68s] English:** of images and predict what's going to happen next or you fill in what happened in between  
**Translation:** 

**[463.60s] English:** do you think it's possible that formulation alone as a signal for self-supervised learning  
**Translation:** 

**[470.88s] English:** can solve intelligence for vision and language i think that's our best shot at the moment  
**Translation:** 

**[475.60s] English:** um so whether this will take us all the way to you know  
**Translation:** 

**[480.00s] English:** know human level intelligence or something or just cat level intelligence uh is not clear but  
**Translation:** 

**[485.12s] English:** among all the possible approaches that people have proposed i think it's a bad shot so i think  
**Translation:** 

**[490.98s] English:** this idea of uh an intelligent system filling in the blanks either you know predicting the future  
**Translation:** 

**[498.36s] English:** inferring the past filling in missing information uh you know i'm currently filling the blank of  
**Translation:** Vocabulary: inferring: 推断

**[505.56s] English:** what is behind your head and what you what your head looks like and you know from from the back  
**Translation:** 

**[509.90s] English:** because i have you know basic knowledge about how humans are made and i don't know if you're  
**Translation:** 

**[515.08s] English:** gonna you know what you're gonna say at which point you're gonna speak whether you're gonna  
**Translation:** 

**[517.64s] English:** move your head this way or that way which way you're gonna look but i know you're not gonna  
**Translation:** 

**[521.16s] English:** just dematerialize and reappear three meters uh down the hall uh you know because i know what's  
**Translation:** 

**[527.70s] English:** possible and what's impossible uh according to intuitive physics so you have a model of what's  
**Translation:** Vocabulary: dematerialize: 消失; intuitive: 直觉

**[532.30s] English:** possible and then you'd be very surprised if it happens and then you'll have to reconstruct your  
**Translation:** 

**[536.98s] English:** model right so that that's the model of the world it's  
**Translation:** Vocabulary: reconstruct: 重新构建

**[539.78s] English:** you  
**Translation:** 

**[539.90s] English:** tells you you know what fills in the blanks so given your partial information about the state  
**Translation:** 

**[544.92s] English:** of the world given by your perception uh your your model of the world fills in the missing  
**Translation:** 

**[550.60s] English:** information and that includes predicting the future re-predicting the past uh you know filling  
**Translation:** 

**[556.44s] English:** in things you don't immediately perceive and that doesn't have to be purely generic vision or visual  
**Translation:** 

**[562.68s] English:** information or generic language you can go to specifics like uh predicting what control decision  
**Translation:** Vocabulary: perceive: 感知

**[569.78s] English:** you make when you're driving in a lane you have a sequence of images from a vehicle and then you  
**Translation:** 

**[576.08s] English:** could you have information if you record it on video where the car ended up going so you can go  
**Translation:** 

**[582.30s] English:** back in time and predict where the car went based on the visual information that's very specific  
**Translation:** 

**[587.64s] English:** domain specific right but the question is whether we can come up with sort of a generic uh method  
**Translation:** 

**[594.44s] English:** for you know training machines to do this kind of prediction or filling in the blanks  
**Translation:** 

**[599.78s] English:** so  
**Translation:** 

**[600.00s] English:** Right now, this type of approach has been unbelievably successful in the context of natural language processing.  
**Translation:** 

**[608.00s] English:** Every model in natural language processing is pre-trained in a self-supervised manner to fill in the blanks.  
**Translation:** Vocabulary: unbelievably: 难以置信地

**[613.20s] English:** You show it a sequence of words, you remove 10% of them, and then you train some gigantic neural net to predict the words that are missing.  
**Translation:** 

**[619.06s] English:** And once you've pre-trained that network, you can use the internal representation learned by it as input to something that you trained, supervised, or whatever.  
**Translation:** Vocabulary: gigantic: 巨大的; neural: 神经; supervised: 监督的

**[631.82s] English:** That's been incredibly successful.  
**Translation:** 

**[633.36s] English:** Not so successful in images, although it's making progress.  
**Translation:** 

**[637.66s] English:** And it's based on manual data augmentation.  
**Translation:** 

**[642.42s] English:** We can go into this later.  
**Translation:** Vocabulary: augmentation: 数据扩增

**[643.58s] English:** But what has not been successful yet is training from video.  
**Translation:** 

**[647.02s] English:** So getting a machine to learn, to represent.  
**Translation:** 

**[649.06s] English:** To represent the visual world, for example, by just watching video.  
**Translation:** 

**[652.78s] English:** Nobody has really succeeded in doing this.  
**Translation:** 

**[654.88s] English:** Okay, well, let's kind of give a high-level overview.  
**Translation:** 

**[657.58s] English:** What's the difference in kind and in difficulty between vision and language?  
**Translation:** 

**[663.90s] English:** So you said people haven't been able to really kind of crack the problem of vision open in terms of self-supervised learning.  
**Translation:** 

**[671.96s] English:** But that may not be necessarily because it's fundamentally more difficult.  
**Translation:** Vocabulary: fundamentally: 从根本上

**[675.60s] English:** Maybe, like when we're talking about achieving...  
**Translation:** 

**[678.84s] English:** Like...  
**Translation:** 

**[679.24s] English:** Passing the Turing test in the full spirit of the Turing test in language might be harder than vision.  
**Translation:** 

**[684.96s] English:** That's not obvious.  
**Translation:** Vocabulary: turing: 图灵测试

**[686.54s] English:** So in your view, which is harder?  
**Translation:** 

**[689.20s] English:** Or perhaps are they just the same problem?  
**Translation:** 

**[692.04s] English:** The farther we get to solving each, the more we realize it's all the same thing.  
**Translation:** 

**[696.72s] English:** It's all the same cake.  
**Translation:** 

**[697.60s] English:** I think what I'm looking for are methods that make them look essentially like the same cake.  
**Translation:** 

**[703.56s] English:** But currently, they're not.  
**Translation:** 

**[704.66s] English:** And the main issue with learning world models or learning predictability...  
**Translation:** 

**[708.82s] English:** predictive models  
**Translation:** Vocabulary: predictive: 预测性的

**[710.24s] English:** is that the prediction is never a single thing.  
**Translation:** 

**[715.90s] English:** Because the world is not entirely predictable.  
**Translation:** Vocabulary: predictable: 可预测的

**[719.02s] English:** Yeah.  
**Translation:** 

**[719.30s] English:** It may be deterministic...  
**Translation:** Vocabulary: deterministic: 决定论的

**[720.00s] English:** stochastic, we can get into the philosophical discussion about it, but even if it's deterministic,  
**Translation:** 

**[725.12s] English:** it's not entirely predictable. And so if I play a short video clip and then I ask you to predict  
**Translation:** Vocabulary: stochastic: 随机的

**[732.80s] English:** what's going to happen next, there's many, many plausible continuations for that video clip,  
**Translation:** 

**[738.16s] English:** and the number of continuation grows with the interval of time that you're asking the system  
**Translation:** Vocabulary: continuation: 延续; continuations: 多种延续; plausible: 合理的

**[743.76s] English:** to make a prediction for. And so one big question with self-supervised learning is how you represent  
**Translation:** 

**[751.36s] English:** this uncertainty, how you represent multiple discrete outcomes, how you represent a continuum  
**Translation:** Vocabulary: continuum: 连续体; discrete: 离散的

**[757.04s] English:** of possible outcomes, etc. And if you are a classical machine learning person, you say,  
**Translation:** 

**[765.44s] English:** oh, you just represent a distribution, right? And that we know how to do when we're predicting  
**Translation:** 

**[772.00s] English:** words, missing words in the text, because we know how to do it. And that's what we're going to do.  
**Translation:** 

**[773.68s] English:** And that's what we're going to do. And that's what we're going to do. And that's what we're going to  
**Translation:** 

**[773.74s] English:** do, because you can have a neural net give a score for every word in a dictionary. It's a big list  
**Translation:** 

**[779.90s] English:** of numbers, maybe 100,000 or so. And you can turn them into a probability distribution that tells  
**Translation:** Vocabulary: neural: 神经网络

**[785.58s] English:** you when I say a sentence, the cat is chasing the blank in the kitchen. There are only a few words  
**Translation:** 

**[793.90s] English:** that make sense there. It could be a mouse, or it could be a lizard spot, or something like that.  
**Translation:** Vocabulary: lizard: 蜥蜴

**[799.34s] English:** And if I say the blank is chasing the blank in the savannah, you also have a bunch of plausible  
**Translation:** 

**[807.34s] English:** options for those two words, right? Because you have kind of an underlying reality that you can  
**Translation:** Vocabulary: savannah: 草原

**[813.82s] English:** refer to, to sort of fill in those blanks. So you cannot say for sure in the savannah if it's  
**Translation:** 

**[823.02s] English:** a lion or a cheetah or whatever. You cannot know if it's a zebra or a goo or whatever.  
**Translation:** Vocabulary: cannot: 不能; cheetah: 猎豹

**[829.34s] English:** Wildebeest, same thing. But you can represent the uncertainty by just a long list of numbers.  
**Translation:** 

**[840.00s] English:** If I do the same thing with video and I ask you to predict a video clip, it's not a discrete set of potential frames.  
**Translation:** Vocabulary: wildebeest: 斑马

**[847.40s] English:** You have to have somewhere representing an infinite number of plausible continuations of multiple frames in a high-dimensional continuous space.  
**Translation:** 

**[857.40s] English:** And we just have no idea how to do this properly.  
**Translation:** 

**[860.68s] English:** Finite high-dimensional.  
**Translation:** 

**[863.24s] English:** It's finite high-dimensional, yes.  
**Translation:** Vocabulary: finite: 有限的

**[864.96s] English:** Just like the words, they try to get it down to a small finite set of under a million, something like that.  
**Translation:** 

**[874.22s] English:** Something like that.  
**Translation:** 

**[874.74s] English:** I mean, it's kind of ridiculous that we're doing a distribution over every single possible word for language, and it works.  
**Translation:** 

**[882.82s] English:** It feels like that's a really dumb way to do it.  
**Translation:** 

**[886.16s] English:** It seems to be like there should be some more compressed representation of the distribution over the words.  
**Translation:** 

**[894.96s] English:** You're right about that.  
**Translation:** Vocabulary: compressed: 压缩的

**[896.08s] English:** I agree.  
**Translation:** 

**[896.88s] English:** Do you have any interesting ideas about how to represent all of the reality in a compressed way such that you can form a distribution over it?  
**Translation:** 

**[903.76s] English:** That's one of the big questions.  
**Translation:** 

**[904.90s] English:** How do you do that?  
**Translation:** 

**[906.30s] English:** I mean, another thing that really is stupid about, I shouldn't say stupid, but simplistic about current approaches to self-supervisioning in NLP in text is that not only do you represent a giant distribution over words,  
**Translation:** 

**[923.24s] English:** but for multiple words.  
**Translation:** Vocabulary: simplistic: 简单化

**[924.96s] English:** Those distributions are essentially independent of each other.  
**Translation:** 

**[930.28s] English:** And you don't pay too much of a price for this.  
**Translation:** 

**[933.00s] English:** So the system, in the sentence that I gave earlier, if it gives a certain probability for a lion and a cheetah, and then a certain probability for a gazelle, wildebeest, and zebra, those two probabilities are independent of each other.  
**Translation:** 

**[954.96s] English:** And it's not the case that those things are independent.  
**Translation:** Vocabulary: cheetah: 猎豹; gazelle: 瞪羚; probabilities: 可能性

**[958.04s] English:** Lions actually attack like bigger animals.  
**Translation:** 

**[960.00s] English:** than cheetahs. So, you know, there's a huge independence hypothesis in this process, which  
**Translation:** Vocabulary: cheetahs: 猎豹; hypothesis: 假设

**[966.50s] English:** is not actually true. The reason for this is that we don't know how to represent properly  
**Translation:** 

**[972.36s] English:** distributions over combinatorial sequences of symbols, essentially, because the number  
**Translation:** Vocabulary: combinatorial: 组合的

**[978.06s] English:** grows exponentially with the length of the symbols. And so we have to use tricks for  
**Translation:** 

**[982.54s] English:** this, but those techniques can, you know, get around, like don't even deal with it.  
**Translation:** Vocabulary: exponentially: 成指数地

**[987.90s] English:** So the big question is, like, would there be some sort of abstract latent representation  
**Translation:** 

**[994.20s] English:** of text that would say that, you know, when I switch lion for gazelle, lion for cheetah,  
**Translation:** 

**[1002.06s] English:** I also have to switch zebra for gazelle?  
**Translation:** 

**[1005.54s] English:** Yeah, so this independence assumption, let me throw some criticism at you that I often  
**Translation:** Vocabulary: assumption: 假设

**[1010.76s] English:** hear and see how you respond. So this kind of filling in the blanks is just statistics.  
**Translation:** 

**[1015.82s] English:** You're not learning anything.  
**Translation:** 

**[1017.90s] English:** Like the deep underlying concepts, you're just mimicking stuff from the past. You're  
**Translation:** 

**[1025.76s] English:** not learning anything new such that you can use it to generalize about the world. Or,  
**Translation:** Vocabulary: generalize: 概括; mimicking: 模仿

**[1032.38s] English:** okay, let me just say the crude version, which is just statistics. It's not intelligence.  
**Translation:** 

**[1038.04s] English:** What do you have to say to that? What do you usually say to that if you kind of hear this  
**Translation:** 

**[1041.70s] English:** kind of thing?  
**Translation:** 

**[1042.12s] English:** I don't get into those discussions because they are kind of pointless. So first of all,  
**Translation:** Vocabulary: pointless: 无意义的

**[1047.90s] English:** it's quite possible that intelligence is just statistics. It's just statistics of a particular  
**Translation:** 

**[1051.76s] English:** kind.  
**Translation:** 

**[1052.70s] English:** Yes. But this is the philosophical question. It's kind of, is it possible that intelligence  
**Translation:** 

**[1058.84s] English:** is just statistics?  
**Translation:** Vocabulary: philosophical: 哲学性的

**[1060.26s] English:** Yeah. But what kind of statistics? So if you are asking the question, are the models of  
**Translation:** 

**[1067.94s] English:** the world, the models of the world that we learn, do they have some notion of causality?  
**Translation:** Vocabulary: causality: 因果关系

**[1072.00s] English:** Yes. So if the criticism comes from people who say, you know, current machine learning,  
**Translation:** 

**[1077.90s] English:** systems don't care about causality, which by the way,  
**Translation:** 

**[1080.00s] English:** wrong uh you know i agree with that yeah you should you know your model of the world should  
**Translation:** 

**[1085.44s] English:** have your actions as one of your of the inputs and that will drive you to learn causal models  
**Translation:** 

**[1090.88s] English:** of the world where you know what you know what uh intervention in the world will cause what result  
**Translation:** 

**[1096.48s] English:** or you can do this by observation of other agents uh acting in the world and and observing the  
**Translation:** 

**[1101.28s] English:** effect uh other humans for example so i think you know at some level of description uh intelligence  
**Translation:** 

**[1108.88s] English:** is just statistics uh but that doesn't mean you don't you don't you know you won't have models  
**Translation:** 

**[1115.04s] English:** that have you know deep mechanistic explanation for what goes on uh the question is how do you  
**Translation:** 

**[1120.72s] English:** learn them that's that's the question i'm interested in because you know a lot of people  
**Translation:** Vocabulary: mechanistic: 机械的

**[1126.16s] English:** who actually voice their criticism say that those mechanistic model has to have to come from someplace  
**Translation:** 

**[1132.32s] English:** else they have to come from human designers they have to come from i don't know what and obviously  
**Translation:** Vocabulary: designers: 设计者; someplace: 某个地方

**[1137.04s] English:** we learn them  
**Translation:** 

**[1139.04s] English:** or if we don't learn them as an individual nature learn them for us using evolution so  
**Translation:** 

**[1145.52s] English:** regardless of what you think those processes have been learned somehow so if you look at the  
**Translation:** 

**[1151.52s] English:** the human brain just like when we humans introspect about how the brain works it seems  
**Translation:** Vocabulary: introspect: 自我反省

**[1156.80s] English:** like when we think about what is intelligence we think about the high level stuff like the models  
**Translation:** 

**[1162.96s] English:** we've constructed concepts like cognitive science like concepts of memory and reasoning module almost  
**Translation:** Vocabulary: cognitive: 认知; module: 模块

**[1168.88s] English:** like these high level modules is there is this serve as a good analogy like are we ignoring the uh  
**Translation:** 

**[1179.68s] English:** the dark matter the the basic low level mechanisms just like we ignore the way the operating system  
**Translation:** 

**[1185.36s] English:** works we're just using the uh the the high level software we're ignoring that at the low level  
**Translation:** 

**[1192.64s] English:** the neural network might be doing something like statistics like meaning uh sorry to use this word  
**Translation:** Vocabulary: neural: 神经网络

**[1198.88s] English:** it probably incorrectly  
**Translation:** 

**[1200.00s] English:** crudely but doing this kind of fill in the gap kind of learning and just kind of updating the  
**Translation:** 

**[1204.46s] English:** model constantly in order to be able to support the raw sensory information to predict it and  
**Translation:** 

**[1210.10s] English:** adjust to the prediction when it's wrong but like hyla when we look at our brain at the high level  
**Translation:** 

**[1215.48s] English:** it feels like we're doing like we're playing chess like we're we're like playing with high  
**Translation:** 

**[1220.98s] English:** level concepts and we're stitching them together we're putting them into long-term memory but  
**Translation:** 

**[1226.16s] English:** really what's going underneath is something we're not able to introspect which is this kind of  
**Translation:** 

**[1231.76s] English:** simple large neural network that's just filling in the gaps right well okay so there's a lot of  
**Translation:** 

**[1237.78s] English:** questions there are answers there okay so first of all there's a whole school of thought in  
**Translation:** 

**[1241.88s] English:** neuroscience computational neuroscience in particular that likes the idea of predictive  
**Translation:** Vocabulary: computational: 计算; neuroscience: 神经科学; predictive: 预测性

**[1247.12s] English:** coding which is really related to the idea i was talking about in self-supervised learning  
**Translation:** 

**[1251.74s] English:** so everything is about prediction the essence of intelligence is the ability to predict  
**Translation:** 

**[1255.70s] English:** yeah  
**Translation:** 

**[1256.04s] English:** yeah  
**Translation:** 

**[1256.14s] English:** , and everything the brain does is trying to predict predict everything from everything else  
**Translation:** 

**[1262.06s] English:** okay and that's really sort of the underlying principle if you want that  
**Translation:** 

**[1266.86s] English:** self-supervised learning is trying to kind of reproduce this idea of prediction that's  
**Translation:** 

**[1270.70s] English:** kind of an essential mechanism of task independent learning if you want  
**Translation:** 

**[1276.22s] English:** the next step is what kind of intelligence are you interested in reproducing and of course you  
**Translation:** 

**[1282.22s] English:** know we all think about you know trying to reproduce sort of you know high level  
**Translation:** 

**[1286.02s] English:** cognitive processes in humans but like with machines we're not even at the level of  
**Translation:** 

**[1291.46s] English:** even reproducing the learning processes in a in a cat brain um you know the most intelligent or  
**Translation:** Vocabulary: cognitive: 认知; reproducing: 复制

**[1298.02s] English:** intelligent systems don't don't have as much common sense as as a house cat so um how is it  
**Translation:** 

**[1304.18s] English:** that cats learn and you know cats don't do a whole lot of uh reasoning they certainly have causal  
**Translation:** 

**[1308.74s] English:** models they certainly have uh because you know many cats can figure out like how they can act on  
**Translation:** 

**[1314.26s] English:** the world to get what they want um so that's the first step and then the second step is to try to  
**Translation:** 

**[1315.90s] English:** um they certainly have a fantastic model  
**Translation:** 

**[1320.00s] English:** intuitive physics, certainly of the dynamics of their own bodies, but also of praise and things  
**Translation:** Vocabulary: intuitive: 直观的

**[1326.24s] English:** like that. So they're pretty smart. They only do this with about 800 million neurons.  
**Translation:** 

**[1333.52s] English:** We are not anywhere close to reproducing this kind of thing. So to some extent, I could say,  
**Translation:** 

**[1341.20s] English:** let's not even worry about the high-level cognition and long-term planning and reasoning  
**Translation:** 

**[1347.84s] English:** that humans can do until we figure out, can we even reproduce what cats are doing?  
**Translation:** Vocabulary: cognition: 认知

**[1352.40s] English:** Now, that said, this ability to learn world models, I think, is the key to the possibility  
**Translation:** 

**[1360.08s] English:** of learning machines that can also reason. So whenever I give a talk, I say there are three  
**Translation:** 

**[1364.96s] English:** challenges, three main challenges in machine learning. The first one is getting machines to  
**Translation:** 

**[1369.68s] English:** learn to represent the world, and I'm proposing self-supervised learning. The second is getting  
**Translation:** 

**[1376.72s] English:** machines to reason.  
**Translation:** 

**[1377.84s] English:** In ways that are compatible with essentially gradient-based learning, because this is what  
**Translation:** Vocabulary: compatible: 兼容的

**[1382.16s] English:** deep learning is all about, really. And the third one is something we have no idea how to solve,  
**Translation:** 

**[1387.44s] English:** or at least I have no idea how to solve, is can we get machines to learn hierarchical representations  
**Translation:** Vocabulary: hierarchical: 层次分明的

**[1394.32s] English:** of action plans? We know how to train them to learn hierarchical representations of perception,  
**Translation:** 

**[1402.08s] English:** computational nets and things like that, and transformers. But what about action plans? Can we  
**Translation:** Vocabulary: computational: 计算的

**[1406.80s] English:** get them to spontaneity?  
**Translation:** 

**[1407.60s] English:** Spontaneously learn good hierarchical representations of actions.  
**Translation:** Vocabulary: spontaneity: 自发性

**[1410.48s] English:** Also gradient-based.  
**Translation:** 

**[1412.32s] English:** Yeah, all of that needs to be somewhat differentiable so that you can apply  
**Translation:** Vocabulary: differentiable: 可微分的

**[1416.80s] English:** sort of gradient-based learning, which is really what deep learning is about.  
**Translation:** 

**[1422.00s] English:** So it's background, knowledge, ability to reason in a way that's differentiable, that is somehow  
**Translation:** 

**[1432.40s] English:** connected, deeply integrated with that background knowledge, or builds on top of that background  
**Translation:** 

**[1436.80s] English:** knowledge.  
**Translation:** 

**[1437.60s] English:** And then given that background knowledge, be able to make  
**Translation:** 

**[1440.00s] English:** plans right in the world so if you take classical optimal control there's  
**Translation:** Vocabulary: optimal: 最优化的

**[1445.64s] English:** something in classical optimal control called model predictive control and it's  
**Translation:** 

**[1450.76s] English:** you know it's been around since in the early 60s NASA uses that to compute  
**Translation:** Vocabulary: predictive: 预测性

**[1455.18s] English:** trajectories of rockets and the basic idea is that you have a pretty  
**Translation:** 

**[1458.78s] English:** predictive model of the rocket let's say or whatever system you were you intend  
**Translation:** Vocabulary: trajectories: 弹道轨迹

**[1463.88s] English:** to control which given the state of the system at time T and given an action  
**Translation:** 

**[1469.32s] English:** that you're taking the system so for a rocket to be thrust and you know all the  
**Translation:** Vocabulary: thrust: 推力

**[1474.60s] English:** controls you can have it gives you the state of the system at time T plus Delta  
**Translation:** 

**[1478.76s] English:** T right so basically differential equation something like that and if you  
**Translation:** Vocabulary: delta: 变化量; differential: 微分的; equation: 方程

**[1484.88s] English:** have this model and you have this model in the form of some sort of neural net  
**Translation:** 

**[1488.96s] English:** or some sort of set of formula that you can back propagate gradient through you  
**Translation:** Vocabulary: gradient: 梯度; neural: 神经; propagate: 传播

**[1493.70s] English:** can do that and you can do that and you can do that and you can do that and you  
**Translation:** 

**[1493.86s] English:** do what's called model predictive control or gradient based model  
**Translation:** 

**[1497.58s] English:** predictive control so you have you can unroll that that model in time you you  
**Translation:** 

**[1505.20s] English:** you you feed it a hypothesized sequence of actions and then you have some  
**Translation:** Vocabulary: hypothesized: 假设的; unroll: 展开

**[1512.28s] English:** objective function that measures how well at the end of the trajectory the  
**Translation:** 

**[1516.14s] English:** system has succeeded or matched what you wanted to do you know is it a robot harm  
**Translation:** Vocabulary: trajectory: 运动轨迹

**[1520.92s] English:** as you grasp the object you want to grasp if it's  
**Translation:** 

**[1523.68s] English:** a rocket you know are you at the right place near the space station things like  
**Translation:** 

**[1527.94s] English:** that and by back propagation through time and again this was invented in the  
**Translation:** 

**[1532.08s] English:** 1960s by optimal control theorist you can figure out what is the optimal  
**Translation:** Vocabulary: propagation: 反向传播; theorist: 理论家

**[1538.08s] English:** sequence of actions that will you know get my system to the the best final  
**Translation:** 

**[1543.54s] English:** state so that's a form of reasoning it's basically planning and a lot of planning  
**Translation:** 

**[1549.72s] English:** systems in robotics are actually based on this and  
**Translation:** 

**[1553.50s] English:** and you can think of this as a form of reasoning so you know to take the  
**Translation:** 

**[1557.84s] English:** example of the teenager driving a car  
**Translation:** 

**[1560.00s] English:** again you have a pretty good dynamical model of the car it doesn't need to be very accurate but  
**Translation:** Vocabulary: dynamical: 动力学的

**[1564.24s] English:** you know again that if you turn the wheel to the right and there is a cliff you're going to run  
**Translation:** 

**[1568.56s] English:** off the cliff right you don't need to have a very accurate model to predict that and you can run  
**Translation:** 

**[1572.48s] English:** this in your mind and decide not to do it for that reason because you can predict in advance that the  
**Translation:** 

**[1577.52s] English:** result is going to be bad so you can sort of imagine different scenarios and uh and then you  
**Translation:** Vocabulary: scenarios: 情景

**[1582.00s] English:** know employ uh or take the first step in the scenario that is most favorable and then repeat  
**Translation:** 

**[1586.80s] English:** the process of planning that's called receding horizon model predictive control so even all  
**Translation:** Vocabulary: predictive: 预测; receding: 后退

**[1591.12s] English:** those things have names you know going back you know decades um and so if you're not not a you  
**Translation:** 

**[1598.72s] English:** know classical optimal control the model of the world is not generally learned uh this you know  
**Translation:** Vocabulary: optimal: 最优的

**[1603.68s] English:** sometimes a few parameters you have to identify that's called systems identification but but  
**Translation:** 

**[1608.32s] English:** generally the model is mostly deterministic and mostly built by hand so the big question of ai  
**Translation:** Vocabulary: deterministic: 决定论的

**[1615.76s] English:** i think the big challenge  
**Translation:** 

**[1616.80s] English:** of ai for the next decade is how do we get machines to run predictive models to the world  
**Translation:** 

**[1621.84s] English:** that deal with uncertainty and deal with the real world in all this complexity so it's not just the  
**Translation:** 

**[1626.96s] English:** trajectory of a rocket which you can reduce to first principles it's not it's not even just  
**Translation:** Vocabulary: complexity: 复杂性

**[1631.12s] English:** the trajectory of a robot arm which again you can model by you know careful mathematics  
**Translation:** 

**[1636.08s] English:** but it's everything else everything we observe in the world you know people behavior  
**Translation:** 

**[1640.80s] English:** um you know physical systems that involve collective phenomena like water or  
**Translation:** 

**[1646.80s] English:** or you know trees and you know branches in a in a tree or something or or uh like complex things  
**Translation:** 

**[1654.48s] English:** that you know humans have no trouble developing abstract representations and predictive model for  
**Translation:** 

**[1659.60s] English:** but we still don't know how to do with machines where do you put in  
**Translation:** 

**[1662.80s] English:** in these three maybe in the in the planning stages the the game theoretic nature of this world  
**Translation:** 

**[1670.56s] English:** where your actions not only respond to the dynamic nature of the world the environment but also affect  
**Translation:** Vocabulary: theoretic: 理论的

**[1676.80s] English:** it so if there's other humans involved  
**Translation:** 

**[1680.00s] English:** Is this point number four, or is it somehow integrated into the hierarchical representation  
**Translation:** Vocabulary: hierarchical: 层次的

**[1685.18s] English:** of action in your view?  
**Translation:** 

**[1686.38s] English:** I think it's integrated.  
**Translation:** 

**[1687.62s] English:** It's just that now your model of the world has to deal with, you know, it just makes  
**Translation:** 

**[1691.96s] English:** it more complicated, right?  
**Translation:** 

**[1693.16s] English:** The fact that humans are complicated and not easily predictable, that makes your model  
**Translation:** 

**[1698.04s] English:** of the world much more complicated.  
**Translation:** Vocabulary: predictable: 可预测的

**[1700.04s] English:** That much more complicated.  
**Translation:** 

**[1701.04s] English:** Well, there's a chess, I mean, I suppose chess is an analogy, so multi-colonel tree  
**Translation:** 

**[1707.24s] English:** search.  
**Translation:** 

**[1708.24s] English:** Right.  
**Translation:** 

**[1709.24s] English:** There is a I go, you go, I go, you go.  
**Translation:** 

**[1712.18s] English:** Like Andrej Karpathy recently gave a talk at MIT about car doors.  
**Translation:** 

**[1717.92s] English:** I think there's some machine learning too, but mostly car doors.  
**Translation:** 

**[1721.06s] English:** And there's a dynamic nature to the car, like the person opening the door checking.  
**Translation:** 

**[1725.06s] English:** I mean, he wasn't talking about that.  
**Translation:** 

**[1726.96s] English:** He was talking about the perception problem of what the ontology of what defines a car  
**Translation:** Vocabulary: ontology: 本体论

**[1730.60s] English:** door, this big philosophical question.  
**Translation:** 

**[1733.06s] English:** But to me, it was interesting because it's obvious that the person opening the car doors,  
**Translation:** Vocabulary: philosophical: 哲学的

**[1737.36s] English:** they're trying to get out.  
**Translation:** 

**[1738.24s] English:** Like here in New York, trying to get out of the car, you slowing down is going to signal  
**Translation:** 

**[1743.16s] English:** something, you speeding up is going to signal something, and that's a dance.  
**Translation:** 

**[1746.64s] English:** It's an asynchronous chess game.  
**Translation:** Vocabulary: asynchronous: 非同步

**[1750.12s] English:** I don't know.  
**Translation:** 

**[1752.08s] English:** So it feels like it's not just, I mean, I guess you can integrate all of them into one  
**Translation:** Vocabulary: integrate: 合并

**[1759.08s] English:** giant model, like the entirety of these little interactions.  
**Translation:** 

**[1764.00s] English:** Because it's not as complicated as chess, it's just like a little dance.  
**Translation:** Vocabulary: entirety: 全部

**[1767.20s] English:** We do like a little dance together.  
**Translation:** 

**[1768.20s] English:** And then we figure it out.  
**Translation:** 

**[1769.20s] English:** Well, in some ways, it's way more complicated than chess because it's continuous,  
**Translation:** 

**[1775.22s] English:** it's uncertain in a continuous manner.  
**Translation:** 

**[1777.22s] English:** It doesn't feel more complicated.  
**Translation:** 

**[1779.24s] English:** It feels simpler.  
**Translation:** 

**[1780.24s] English:** But it doesn't feel more complicated because that's what we've evolved to solve.  
**Translation:** 

**[1783.78s] English:** This is the kind of problem we've evolved to solve.  
**Translation:** 

**[1785.58s] English:** And so we're good at it because nature has made us good at it.  
**Translation:** 

**[1790.76s] English:** Nature has not made us good at chess.  
**Translation:** 

**[1792.42s] English:** We completely suck at chess.  
**Translation:** 

**[1794.20s] English:** Yeah.  
**Translation:** 

**[1795.20s] English:** In fact, that's why we designed it as a game.  
**Translation:** 

**[1798.00s] English:** It used to be challenging.  
**Translation:** 

**[1800.00s] English:** And if there is something that, you know, recent progress in chess and Go has made us realize is that humans are really terrible at those things, like really bad.  
**Translation:** 

**[1809.04s] English:** You know, there was a story, right, before AlphaGo that, you know, the best Go players thought they were maybe two or three stones behind, you know, an ideal player that they would call God.  
**Translation:** 

**[1820.36s] English:** In fact, no, they are like nine or ten stones behind.  
**Translation:** 

**[1823.66s] English:** I mean, we're just bad.  
**Translation:** 

**[1825.22s] English:** So we're not good at, and it's because we have limited working memory.  
**Translation:** 

**[1829.70s] English:** You know, we're not very good at, like, doing this tree exploration that, you know, computers are much better at doing than we are.  
**Translation:** 

**[1836.70s] English:** But we are much better at learning differentiable models of the world.  
**Translation:** 

**[1840.58s] English:** I mean, I say differentiable in a kind of, you know, I should say not differentiable in the sense that, you know, we run backprop through it, but in the sense that our brain has some mechanism for estimating gradients of some kind.  
**Translation:** Vocabulary: backprop: 反向传播; differentiable: 可微的; estimating: 估计; gradients: 梯度

**[1853.76s] English:** And that's what, you know, makes us efficient.  
**Translation:** 

**[1856.34s] English:** So if you have an agent that consists.  
**Translation:** 

**[1859.70s] English:** Of a model of the world, which, you know, in the human brain is basically the entire front half of your brain, an objective function, which in humans is a combination of two things.  
**Translation:** 

**[1874.32s] English:** There is your sort of intrinsic motivation module, which is in the basal ganglia, you know, at the base of your brain.  
**Translation:** Vocabulary: basal: 底部的; ganglia: 神经节; intrinsic: 内在的; module: 模块

**[1879.84s] English:** That's the thing that measures pain and hunger and things like that, like immediate feelings and emotions.  
**Translation:** 

**[1888.08s] English:** And then there is.  
**Translation:** 

**[1889.70s] English:** You know, the equivalent of what people in reinforcement learning call a critic, which is a sort of module that predicts ahead what the outcome of a of a situation will be.  
**Translation:** 

**[1901.82s] English:** And so it's not a cost function, but it's sort of not an objective function, but it's sort of a, you know, trained predictor of the ultimate objective function.  
**Translation:** Vocabulary: predictor: 预测器

**[1910.88s] English:** And that also is differentiable.  
**Translation:** 

**[1912.46s] English:** And so if all of this is differentiable, your cost function, your your critic, your, you know, your your role model.  
**Translation:** 

**[1919.94s] English:** For those of you with additional questions, please feel free to leave.  
**Translation:** 

**[1923.08s] English:** I'll be happy to answer questions.  
**Translation:** 

**[1923.88s] English:** And I'll see you in our next panel.  
**Translation:** 

**[1920.00s] English:** Then you can use gradient-based type methods to do planning, to do reasoning, to do learning, to do all the things that we'd like an intelligent agent to do.  
**Translation:** 

**[1931.90s] English:** And gradient-based learning, like what's your intuition, that's probably at the core of what can solve intelligence.  
**Translation:** 

**[1938.44s] English:** So you don't need logic-based reasoning in your view.  
**Translation:** Vocabulary: intuition: 直觉

**[1945.14s] English:** I don't know how to make logic-based reasoning compatible with efficient learning.  
**Translation:** 

**[1950.00s] English:** I mean, there is a big question, perhaps a philosophical question.  
**Translation:** Vocabulary: compatible: 兼容; philosophical: 哲学的

**[1953.92s] English:** I mean, it's not that philosophical, but that we can ask is that all the learning algorithms we know from engineering and computer science proceed by optimizing some objective function.  
**Translation:** 

**[1967.88s] English:** So one question we may ask is, does learning in the brain minimize an objective function?  
**Translation:** Vocabulary: optimizing: 最大化

**[1974.34s] English:** I mean, it could be a composite of multiple objective functions, but it's still an objective function.  
**Translation:** 

**[1980.00s] English:** Second, if it does optimize an objective function, does it do it by some sort of gradient estimation?  
**Translation:** Vocabulary: composite: 合成函数; estimation: 估计; gradient: 梯度; optimize: 优化

**[1989.38s] English:** It doesn't need to be backprop, but some way of estimating the gradient in an efficient manner, whose complexity is on the same order of magnitude as actually running the inference.  
**Translation:** 

**[2002.46s] English:** Because you can't afford to do things like perturbing a weight in your brain to figure out what the effect is.  
**Translation:** Vocabulary: backprop: 反向传播; complexity: 复杂度; estimating: 估计; inference: 推理; perturbing: 扰动

**[2007.70s] English:** And then sort of...  
**Translation:** 

**[2010.00s] English:** You can do sort of estimating gradient by perturbation.  
**Translation:** Vocabulary: perturbation: 扰动

**[2013.30s] English:** To me, it seems very implausible that the brain uses some sort of, you know, zeroth order, black box, gradient-free optimization, because it's so much less efficient than gradient optimization.  
**Translation:** 

**[2026.34s] English:** So it has to have a way of estimating gradient.  
**Translation:** Vocabulary: implausible: 不合常理; optimization: 优化

**[2029.22s] English:** Is it possible that some kind of logic-based reasoning emerges in pockets as a useful, like you said, if the brain is an objective function?  
**Translation:** 

**[2038.12s] English:** Maybe it's a mechanism for creating objective functions.  
**Translation:** 

**[2040.00s] English:** functions it's it's a mechanism for um creating knowledge bases for example that can then be  
**Translation:** 

**[2047.12s] English:** queried like maybe it's like an efficient representation of knowledge that's learned  
**Translation:** 

**[2051.28s] English:** in a gradient-based way or something like that well so i think there is a lot of different types  
**Translation:** 

**[2055.84s] English:** of intelligence so first of all i think the type of logical reasoning that we think about  
**Translation:** 

**[2061.12s] English:** that we are you know maybe stemming from you know sort of classical ai of the 1970s and 80s  
**Translation:** 

**[2067.44s] English:** um i think humans use that relatively rarely and are not particularly good at it but we judge each  
**Translation:** Vocabulary: stemming: 源自

**[2075.36s] English:** other based on our ability to uh solve those rare problems it's called an iq test i think so like  
**Translation:** 

**[2082.88s] English:** i'm i'm not very good at chess yes i'm judging you this whole time because well we we actually with  
**Translation:** 

**[2089.84s] English:** your with your uh you know heritage i'm sure you're good at chess no stereotypes not all  
**Translation:** 

**[2095.44s] English:** stereotypes are true  
**Translation:** Vocabulary: stereotypes: 刻板印象

**[2097.84s] English:** well i'm terrible at chess so um you know but i think perhaps uh another type of intelligence  
**Translation:** 

**[2104.56s] English:** that i have is this uh uh you know ability of sort of building models to the world from  
**Translation:** 

**[2110.56s] English:** uh you know reasoning obvious obviously but also also data uh and those those models generally are  
**Translation:** 

**[2117.12s] English:** more kind of analogical right so it's it's uh it's reasoning by simulation and by analogy  
**Translation:** Vocabulary: analogical: 类比的; simulation: 模拟

**[2123.84s] English:** where you use one model to apply to a new situation even though you've never  
**Translation:** 

**[2127.44s] English:** seen that situation you can sort of um connect it to a situation you've encountered before  
**Translation:** Vocabulary: encountered: 遇到过

**[2133.44s] English:** and and your reasoning is more you know akin to some sort of internal simulation so you you're  
**Translation:** 

**[2139.60s] English:** kind of simulating what's happening when you're building i don't know a box out of wood or  
**Translation:** Vocabulary: simulating: 模拟

**[2143.04s] English:** something right you can imagine in advance like what would be the result of you know cutting the  
**Translation:** 

**[2148.00s] English:** wood in this particular way are you going to use you know screws or nails or whatever  
**Translation:** 

**[2152.72s] English:** when you are interacting with someone you also have a model of that person and and sort of interact with  
**Translation:** 

**[2157.44s] English:** that person you know having this  
**Translation:** 

**[2160.00s] English:** model in mind to kind of tell the person what you think is useful to them.  
**Translation:** 

**[2166.10s] English:** I think this ability to construct models of the world is basically the essence of intelligence,  
**Translation:** 

**[2174.00s] English:** and the ability to use it then to plan actions that will fulfill a particular criterion,  
**Translation:** 

**[2183.14s] English:** of course, is necessary as well.  
**Translation:** Vocabulary: criterion: 标准

**[2185.06s] English:** So I'm going to ask you a series of impossible questions as we keep asking, as I've been  
**Translation:** 

**[2189.50s] English:** doing.  
**Translation:** 

**[2190.50s] English:** So if that's the fundamental sort of dark matter of intelligence, this ability to form  
**Translation:** 

**[2195.22s] English:** a background model, what's your intuition about how much knowledge is required?  
**Translation:** Vocabulary: intuition: 直觉

**[2201.76s] English:** You know, I think dark matter, you can put a percentage on it of the composition of the  
**Translation:** 

**[2209.70s] English:** universe and how much of it is dark matter, how much of it is dark energy.  
**Translation:** 

**[2212.74s] English:** How much...  
**Translation:** 

**[2213.74s] English:** How much...  
**Translation:** 

**[2214.74s] English:** How much information do you think is required to be a house cat?  
**Translation:** 

**[2219.50s] English:** So you have to be able to, when you see a box, go in it.  
**Translation:** 

**[2223.02s] English:** When you see a human, compute the most evil action.  
**Translation:** 

**[2226.32s] English:** If there's a thing that's near an edge, you knock it off.  
**Translation:** 

**[2229.76s] English:** All of that, plus the extra stuff you mentioned, which is a great self-awareness of the physics  
**Translation:** 

**[2235.62s] English:** of your own body and the world.  
**Translation:** 

**[2238.84s] English:** How much knowledge is required, do you think, to solve it?  
**Translation:** 

**[2241.18s] English:** I don't even know how to measure an answer.  
**Translation:** 

**[2244.18s] English:** An answer to that question.  
**Translation:** 

**[2245.42s] English:** I'm not sure how to measure it, but whatever it is, it fits in about 800,000 neurons, 800  
**Translation:** 

**[2253.06s] English:** million neurons, sorry.  
**Translation:** 

**[2254.06s] English:** The representation does.  
**Translation:** Vocabulary: neurons: 神经元

**[2255.06s] English:** Everything, all knowledge, everything, right?  
**Translation:** 

**[2256.06s] English:** You know, it's less than a billion.  
**Translation:** 

**[2261.06s] English:** A dog is two billion, but a cat is less than one billion.  
**Translation:** 

**[2265.74s] English:** And so multiply that by a thousand and you get the number of synapses.  
**Translation:** Vocabulary: multiply: 乘法; synapses: 突触

**[2270.38s] English:** And I think almost all of it is learned through this, you know, AI.  
**Translation:** 

**[2271.18s] English:** Yeah.  
**Translation:** 

**[2272.18s] English:** Yeah.  
**Translation:** 

**[2273.18s] English:** Yeah.  
**Translation:** 

**[2274.18s] English:** It's a sort of self-supervised learning.  
**Translation:** 

**[2276.06s] English:** Although, you know, I think a tiny sliver is learned through reinforcement learning.  
**Translation:** Vocabulary: reinforcement: 强化学习

**[2280.00s] English:** certainly very little through classical supervised running, although it's not even clear how  
**Translation:** 

**[2284.34s] English:** supervised running actually works in the biological world.  
**Translation:** Vocabulary: supervised: 监督训练

**[2289.36s] English:** So I think almost all of it is self-supervised running, but it's driven by the sort of ingrained  
**Translation:** 

**[2297.14s] English:** objective functions that a cat or a human have at the base of their brain, which kind  
**Translation:** Vocabulary: ingrained: 根深蒂固

**[2301.84s] English:** of drives their behavior.  
**Translation:** 

**[2305.00s] English:** So nature tells us, you're hungry.  
**Translation:** 

**[2309.56s] English:** It doesn't tell us how to feed ourselves.  
**Translation:** 

**[2312.14s] English:** That's something that the rest of our brain has to figure out, right?  
**Translation:** 

**[2314.80s] English:** Well, it's interesting because there might be more like deeper objective functions  
**Translation:** 

**[2319.60s] English:** underlying the whole thing.  
**Translation:** 

**[2321.44s] English:** So hunger may be some kind of, now you go to like neurobiology, it might be just the  
**Translation:** 

**[2326.74s] English:** brain trying to maintain homeostasis.  
**Translation:** Vocabulary: homeostasis: 稳态; neurobiology: 神经生物学

**[2332.58s] English:** So hunger is just one of the human perceivable symptoms of the brain being unhappy with the  
**Translation:** 

**[2339.54s] English:** way things are currently, because it could be just like one really dumb objective function  
**Translation:** Vocabulary: perceivable: 可感知的

**[2344.10s] English:** at the core.  
**Translation:** 

**[2345.10s] English:** But that's how behavior is driven.  
**Translation:** 

**[2348.78s] English:** The fact that the orbezal ganglia drive us to do things that are different from say an  
**Translation:** 

**[2355.32s] English:** orangutang or certainly a cat is what makes human nature versus orangutang nature versus  
**Translation:** Vocabulary: ganglia: 神经节; orangutang: 猩猩

**[2361.70s] English:** cat nature.  
**Translation:** 

**[2363.40s] English:** So for example, our orbezal ganglia drives us to seek the company.  
**Translation:** 

**[2369.16s] English:** Yeah.  
**Translation:** 

**[2369.54s] English:** Of other humans.  
**Translation:** 

**[2372.30s] English:** And that's because nature has figured out that we need to be social animals for our  
**Translation:** 

**[2376.58s] English:** species to survive.  
**Translation:** 

**[2377.58s] English:** And it's true of many primates.  
**Translation:** 

**[2381.42s] English:** It's not true of orangutangs.  
**Translation:** Vocabulary: orangutangs: 猩猩; primates: 灵长类

**[2382.42s] English:** Orangutangs are solitary animals.  
**Translation:** 

**[2385.00s] English:** They don't seek the company of others.  
**Translation:** Vocabulary: solitary: 独居的

**[2386.96s] English:** In fact, they avoid them.  
**Translation:** 

**[2389.38s] English:** In fact, they scream at them when they come too close because they're territorial.  
**Translation:** Vocabulary: territorial: 领地的

**[2392.84s] English:** Because for their survival, evolution has figured out that's the best thing.  
**Translation:** 

**[2398.10s] English:** I mean, they are occasionally social.  
**Translation:** 

**[2399.16s] English:** Of course.  
**Translation:** 

**[2400.00s] English:** for you know production and stuff like that but but but they're mostly  
**Translation:** 

**[2405.28s] English:** solitary so so all of those behaviors are not part of intelligence you know  
**Translation:** 

**[2409.70s] English:** people say oh you're never gonna have intelligent machines because you know  
**Translation:** 

**[2412.30s] English:** human intelligence is social but then you look at orangutans you look at  
**Translation:** 

**[2415.56s] English:** octopus octopus never know their parents they barely interact with any other and  
**Translation:** Vocabulary: octopus: 海洋生物; orangutans: 猩猩

**[2420.62s] English:** they and they get to be really smart in less and less than a year in like half a  
**Translation:** 

**[2424.54s] English:** year you know in a year there are adults in two years the dead so there  
**Translation:** 

**[2430.96s] English:** are things that we think as humans are intimately linked with intelligence like  
**Translation:** 

**[2435.96s] English:** social interaction like language we think I think we give way too much  
**Translation:** Vocabulary: intimately: 密切地

**[2442.00s] English:** importance to language as a substrate of intelligence as humans because we think  
**Translation:** 

**[2447.38s] English:** our reasoning is so linked with language so for to solve the house cat  
**Translation:** Vocabulary: substrate: 基础介质

**[2452.10s] English:** intelligence problem you think you could do it  
**Translation:** 

**[2454.46s] English:** on a human brain and you could do it on a human brain and you could do it on a  
**Translation:** 

**[2454.52s] English:** desert island you could have pretty much because you have a cat sitting there  
**Translation:** 

**[2460.12s] English:** looking at the waves at the ocean waves and figure a lot of it out it needs to  
**Translation:** 

**[2466.22s] English:** have sort of you know the right set of drives to kind of you know get it to do  
**Translation:** 

**[2472.10s] English:** the thing and learn the appropriate things right but like for example you  
**Translation:** 

**[2476.90s] English:** know baby humans are driven to learn to stand up and walk okay that's kind of  
**Translation:** 

**[2484.44s] English:** this desire is hardwired how to do it precisely is not that's learned but the  
**Translation:** Vocabulary: hardwired: 天生具备

**[2488.70s] English:** desire to to walk move around and stand up that's very simple to hardwire this  
**Translation:** 

**[2496.98s] English:** kind of stuff what oh like the desire to well that's interesting you're hardwired  
**Translation:** Vocabulary: hardwire: 固化连线

**[2503.34s] English:** to want to walk that's not a there's got to be a deeper need for walking I think  
**Translation:** 

**[2510.96s] English:** was probably socially imposed by society they need to walk all the other things  
**Translation:** 

**[2514.36s] English:** they need to walk all the other things  
**Translation:** 

**[2514.42s] English:** they need to walk all the other things the other bipedal like a lot of simple  
**Translation:** Vocabulary: bipedal: 两足的

**[2517.12s] English:** the other bipedal like a lot of simple  
**Translation:** 

**[2517.14s] English:** the other bipedal like a lot of simple animals that you know probably walk  
**Translation:** 

**[2518.98s] English:** animals that you know probably walk  
**Translation:** 

**[2519.00s] English:** animals that you know probably walk without ever  
**Translation:** 

**[2519.98s] English:** without ever  
**Translation:** 

**[2520.00s] English:** watching any other members of the species it seems like a scary thing to  
**Translation:** 

**[2525.58s] English:** have to do because you suck it by Peter walking at first it seems crawling him  
**Translation:** 

**[2530.26s] English:** is much safer much more like why are you in a hurry well because because you have  
**Translation:** Vocabulary: crawling: 爬行

**[2537.16s] English:** this thing that drives you to do it you know which is sort of part of the sort  
**Translation:** 

**[2542.90s] English:** of human development is that understood actually what not entirely no what is  
**Translation:** 

**[2548.02s] English:** what's the reason to get on two feet it's really hard like most animals  
**Translation:** 

**[2551.48s] English:** don't get on two feet well they get on four feet you know many mammals get on  
**Translation:** 

**[2555.22s] English:** four feet yeah they very quickly some of them extremely quickly but I don't you  
**Translation:** 

**[2559.18s] English:** know like from the last time I've interacted with a table that's much more  
**Translation:** Vocabulary: interacted: 互动过

**[2563.20s] English:** stable than a thing than two legs it's just a really hard problem yeah I mean  
**Translation:** 

**[2566.92s] English:** birds have figured it out with two feet that's what technically we can go into  
**Translation:** 

**[2571.36s] English:** ontology they have four I guess they have two feet they have two feet chickens  
**Translation:** 

**[2575.50s] English:** you know dinosaurs at two feet  
**Translation:** Vocabulary: ontology: 本体论

**[2578.02s] English:** many of them allegedly I'm just now learning that t-rex was eating grass not  
**Translation:** 

**[2584.44s] English:** other animals t-rex might have been a friendly friendly pet what do you think  
**Translation:** Vocabulary: allegedly: 据说

**[2588.52s] English:** about I don't know if you looked at the test for general intelligence at France  
**Translation:** 

**[2594.94s] English:** Rochelle a put together I don't know if you got a chance to look at that kind of  
**Translation:** 

**[2598.42s] English:** thing like what what's your intuition about how to solve like an IQ type of  
**Translation:** 

**[2602.90s] English:** test I don't know I think it's so outside of my radar screen that it's not  
**Translation:** 

**[2607.06s] English:** really I don't know I think it's so outside of my radar screen that it's not really  
**Translation:** 

**[2608.02s] English:** really I don't know I think it's so outside of my radar screen that it's not really relevant I think in the short term I guess  
**Translation:** 

**[2611.32s] English:** relevant I think in the short term I guess  
**Translation:** 

**[2611.34s] English:** relevant I think in the short term I guess one way to ask another way perhaps  
**Translation:** 

**[2614.08s] English:** one way to ask another way perhaps  
**Translation:** 

**[2614.10s] English:** one way to ask another way perhaps more closer to what do you work is like  
**Translation:** 

**[2617.68s] English:** more closer to what do you work is like  
**Translation:** 

**[2617.70s] English:** more closer to what do you work is like how do you solve MNIST with very little  
**Translation:** 

**[2621.38s] English:** how do you solve MNIST with very little  
**Translation:** 

**[2621.40s] English:** how do you solve MNIST with very little example data that's right and that's the  
**Translation:** 

**[2623.94s] English:** example data that's right and that's the  
**Translation:** 

**[2623.96s] English:** example data that's right and that's the answer to this probably is also  
**Translation:** 

**[2625.22s] English:** answer to this probably is also  
**Translation:** 

**[2625.24s] English:** answer to this probably is also running just run to represent images  
**Translation:** 

**[2627.14s] English:** running just run to represent images  
**Translation:** 

**[2627.16s] English:** and then learning to recognize handwritten digits on top of this will only require a few samples.  
**Translation:** Vocabulary: digits: 阿拉伯数字; handwritten: 手写

**[2633.40s] English:** And we observe this in humans, right? You show a young child a picture book with a couple pictures  
**Translation:** 

**[2640.00s] English:** an elephant and that's it the child knows what an elephant is and we we see this today with practical  
**Translation:** 

**[2646.08s] English:** systems that we you know we train image recognition systems with uh enormous amounts of of images  
**Translation:** 

**[2653.52s] English:** either either completely self-supervised or very weakly supervised for example  
**Translation:** Vocabulary: supervised: 监督学习

**[2658.08s] English:** you can uh train a neural net to predict uh whatever hashtag people type on instagram right  
**Translation:** 

**[2663.92s] English:** then you can do this with billions of images because there's billions per day that are showing  
**Translation:** Vocabulary: neural: 神经网络

**[2667.28s] English:** up so the amount of training data there is essentially unlimited and then you take the  
**Translation:** 

**[2673.12s] English:** output representation you know a couple layers down from the output of what the system learned  
**Translation:** 

**[2679.28s] English:** and feed this as input to a classifier for any object in the world that you want and it works  
**Translation:** 

**[2684.00s] English:** pretty well so that's transfer learning okay or weekly supervised transfer learning people are  
**Translation:** 

**[2691.52s] English:** making very very fast progress using self-supervised running for for this kind of scenario as well  
**Translation:** 

**[2697.92s] English:** um and you know my guess is that that's that's going to be the the future for self-supervised  
**Translation:** 

**[2703.20s] English:** learning how much cleaning do you think is needed for filtering um uh malicious signal or what's a  
**Translation:** 

**[2712.40s] English:** better term but like a lot of people use hashtags on instagram to uh get like good seo that doesn't  
**Translation:** Vocabulary: hashtags: 话题标签; malicious: 恶意

**[2720.40s] English:** fully represent the contents of the image like they'll put a picture of a cat and hashtag it  
**Translation:** 

**[2725.20s] English:** with like science awesome  
**Translation:** 

**[2727.52s] English:** fun i don't know all kind of why would you put signs that's not very good seo the way the way my  
**Translation:** 

**[2733.52s] English:** colleagues who worked on this project at uh at facebook now meta meta ai a few years ago  
**Translation:** 

**[2740.40s] English:** dealt with this is that they only selected something like 17 000 tags that correspond to  
**Translation:** 

**[2744.48s] English:** kind of physical things or or situations like you know that has some visual content  
**Translation:** Vocabulary: correspond: 相符

**[2752.24s] English:** so you know you wouldn't have like htbt or anything like that  
**Translation:** 

**[2757.28s] English:** so they they keep a very select set of  
**Translation:** 

**[2760.00s] English:** hashtags yeah okay but it's still it's still on the order of you know ten to  
**Translation:** 

**[2765.40s] English:** twenty thousand so it's fairly large okay can you tell me about data  
**Translation:** 

**[2770.28s] English:** augmentation what the heck is data augmentation and how is it used maybe  
**Translation:** 

**[2774.90s] English:** contrast of learning for for video what are some cool ideas here right so data  
**Translation:** Vocabulary: augmentation: 数据增强

**[2781.36s] English:** augmentation I mean first data augmentation you know is the idea of  
**Translation:** 

**[2784.54s] English:** artificially increasing the size of your training set by distorting the images  
**Translation:** Vocabulary: artificially: 人为地; distorting: 扭曲

**[2789.34s] English:** that you have in ways that don't change the nature of the image right so you  
**Translation:** 

**[2792.52s] English:** take you do in this you can do data augmentation on a list and people have  
**Translation:** 

**[2795.94s] English:** done this since the 1990s right you take a and this digit and you shift it a  
**Translation:** 

**[2800.50s] English:** little bit or you change the size or rotate it skew it you know etc add noise  
**Translation:** Vocabulary: digit: 数字; rotate: 旋转

**[2807.40s] English:** add noise etc and it it works better if you train a supervised classifier with  
**Translation:** 

**[2812.62s] English:** augmented data you're gonna get better results now it's become really  
**Translation:** Vocabulary: augmented: 扩充的数据; supervised: 监督学习

**[2817.54s] English:** interesting over the last  
**Translation:** 

**[2819.34s] English:** couple years because a lot of self supervised learning techniques to  
**Translation:** 

**[2824.34s] English:** pre-trained vision systems are based on data augmentation and the the basic  
**Translation:** 

**[2830.08s] English:** techniques is originally inspired by techniques that I worked on in the early  
**Translation:** 

**[2835.38s] English:** 90s and Jeff Hinton worked on also in the early 90s there were sort of parallel  
**Translation:** 

**[2838.62s] English:** work I used to call this Siamese network so basically you take two identical  
**Translation:** Vocabulary: hinton: Hint恩; siamese: 连体的

**[2844.66s] English:** copies of the same network they share the same weights and you show two  
**Translation:** 

**[2849.34s] English:** different views of the same object either those two different views may  
**Translation:** 

**[2853.24s] English:** have been obtained by data augmentation or maybe it's two different views of the  
**Translation:** 

**[2856.66s] English:** same scene from a camera that you moved or at different times or something like  
**Translation:** 

**[2860.78s] English:** that right or two pictures of the same person things like that and then you  
**Translation:** 

**[2864.88s] English:** train this neural net those two identical copies of this neural net to  
**Translation:** 

**[2868.54s] English:** produce an output representation a vector in such a way that the  
**Translation:** 

**[2873.26s] English:** representation for those two images are as close to each other as possible as I'd done that.  
**Translation:** 

**[2879.34s] English:** So they're identical to each other.  
**Translation:** 

**[2880.00s] English:** possible right because you want the system to basically learn a function that will that will  
**Translation:** 

**[2885.36s] English:** be invariant that will not change whose output will not change when you transform those inputs  
**Translation:** 

**[2890.80s] English:** in in those in those particular ways right so that's easy to do what's complicated is how do  
**Translation:** Vocabulary: invariant: 不变的

**[2897.04s] English:** you make sure that when you show two images that are different the system will produce different  
**Translation:** 

**[2900.48s] English:** things because if you don't have a specific provision for this the system will just ignore  
**Translation:** 

**[2907.12s] English:** the input when you train it it will end up ignoring the input and just produce a constant  
**Translation:** 

**[2911.28s] English:** vector that is the same for every input right yes that's called a collapse now how do you avoid  
**Translation:** 

**[2915.84s] English:** collapse so there's two ideas uh one idea that i proposed in the early 90s with my colleagues at  
**Translation:** 

**[2922.16s] English:** bell labs jane bromley and a couple other people which we now call contrastive learning which is  
**Translation:** Vocabulary: bromley: 布罗梅尔

**[2928.56s] English:** to have negative examples right so you have pairs of images that you know are different  
**Translation:** 

**[2934.24s] English:** and you show them to the network and those two  
**Translation:** 

**[2937.12s] English:** copies and then you you push the two output vectors away from each other  
**Translation:** 

**[2940.96s] English:** and it will eventually guarantee that things that are semantically similar produce similar  
**Translation:** Vocabulary: semantically: 语义上

**[2945.68s] English:** representations and things that are different produce different representations  
**Translation:** 

**[2950.16s] English:** we actually came up with this idea for a project of doing signature verification so we would  
**Translation:** Vocabulary: verification: 验证

**[2955.68s] English:** collect signature signatures from like multiple signatures on the same person and then train a  
**Translation:** 

**[2960.96s] English:** neural net to produce the same representation and then uh you know force the system to produce  
**Translation:** Vocabulary: neural: 神经网络

**[2966.80s] English:** different  
**Translation:** 

**[2967.76s] English:** representation for different signatures um this was actually the the problem was proposed by  
**Translation:** 

**[2973.12s] English:** people from uh what was a subsidiary of a tnt at the time called ncr and they were interested in  
**Translation:** 

**[2979.28s] English:** storing uh representation of the signature on the 80 bytes of the magnetic strip of a credit card  
**Translation:** Vocabulary: bytes: 字节; subsidiary: 子公司

**[2986.48s] English:** so we came up with this idea of having a neural net with 80 outputs you know that we would  
**Translation:** 

**[2990.80s] English:** quantize on bytes so so that we could encode the and that including was then used to compare whether  
**Translation:** Vocabulary: encode: 编码; quantize: 量化

**[2995.60s] English:** the signature matches or not  
**Translation:** 

**[2997.12s] English:** that's right so then you would you know sign it would run  
**Translation:** 

**[3000.00s] English:** neural net and then you would compare the output vector to whatever is stored on your card it  
**Translation:** 

**[3003.52s] English:** actually worked it worked but they ended up not using it um because nobody cares actually i mean  
**Translation:** 

**[3010.32s] English:** the american you know financial payment system is incredibly lax in that respect compared to europe  
**Translation:** 

**[3017.52s] English:** over the signatures what's the purpose of signatures anyway this is very nobody looks  
**Translation:** 

**[3021.44s] English:** at them nobody cares you know it's uh yeah yeah no so uh so that that's contrastive running right  
**Translation:** 

**[3027.68s] English:** so you need positive and negative pairs and the problem with that is that you know even  
**Translation:** 

**[3031.84s] English:** though i had the original paper on this i'm actually not very positive about it because  
**Translation:** 

**[3037.28s] English:** it doesn't work in high dimension if your representation is high dimensional  
**Translation:** Vocabulary: dimension: 维度

**[3040.88s] English:** there's just too many ways for two things to be different and and so you would need lots and lots  
**Translation:** 

**[3045.84s] English:** and lots of negative pairs so there is a particular implementation of this which is relatively recent  
**Translation:** 

**[3051.92s] English:** from actually the google toronto group uh where you know jeffington is the  
**Translation:** 

**[3057.44s] English:** is  
**Translation:** Vocabulary: toronto: 多伦多

**[3057.68s] English:** your member there and it's called simclear simclr and it you know basically a particular way of  
**Translation:** 

**[3064.08s] English:** implementing this idea of contrasting running the particular objective function  
**Translation:** Vocabulary: implementing: 实施; simclear: 简化清晰

**[3068.56s] English:** now what i'm much more enthusiastic about these days is non-contrasting methods so  
**Translation:** 

**[3074.80s] English:** other ways to guarantee that uh the representations would be different for different  
**Translation:** 

**[3082.24s] English:** different inputs and it's actually based on an idea that  
**Translation:** 

**[3087.68s] English:** jeffington proposed in the early 90s with his student at the time sue becker  
**Translation:** Vocabulary: becker: 贝克

**[3091.76s] English:** and it's based on the idea of maximizing the mutual information between the outputs of the  
**Translation:** 

**[3095.04s] English:** two systems you only show positive pairs you only show pairs of images that you know are  
**Translation:** Vocabulary: maximizing: 最大化

**[3099.44s] English:** somewhat similar and you train the two networks to be informative  
**Translation:** 

**[3104.88s] English:** but also to be as informative of each other as possible so basically one representation has to be  
**Translation:** 

**[3111.60s] English:** predictable from the other essentially uh and you know he proposed that idea had you know a lot of  
**Translation:** 

**[3117.68s] English:** a couple of papers in the early 90s.  
**Translation:** Vocabulary: predictable: 可预测的

**[3120.00s] English:** and then nothing was done about it for decades.  
**Translation:** 

**[3123.02s] English:** And I kind of revived this idea together with my postdocs at FAIR,  
**Translation:** Vocabulary: postdocs: 博士后研究人员

**[3128.18s] English:** particularly a postdoc called Stéphane Denis,  
**Translation:** 

**[3129.66s] English:** who is now a junior professor in Finland at the University of Aalto.  
**Translation:** Vocabulary: aalto: 阿alto

**[3134.88s] English:** We came up with something that we called Barlow Twins,  
**Translation:** 

**[3138.92s] English:** and it's a particular way of maximizing the information content of a vector  
**Translation:** Vocabulary: barlow: 巴罗孪生子

**[3144.96s] English:** using some hypotheses.  
**Translation:** 

**[3147.60s] English:** And we have kind of another version of it that's more recent now  
**Translation:** Vocabulary: hypotheses: 假设

**[3152.82s] English:** called VICREG, V-I-C-R-E-G.  
**Translation:** 

**[3154.58s] English:** That means variance, invariance, covariance, regularization.  
**Translation:** Vocabulary: covariance: 协方差; invariance: 不变性; variance: 方差

**[3157.94s] English:** And it's the thing I'm the most excited about in machine learning  
**Translation:** 

**[3160.78s] English:** in the last 15 years.  
**Translation:** 

**[3161.76s] English:** I mean, I'm really, really excited about this.  
**Translation:** 

**[3164.52s] English:** What kind of data augmentation is useful for that non-contrast learning method?  
**Translation:** Vocabulary: augmentation: 增强

**[3170.24s] English:** Are we talking about, does that not matter that much?  
**Translation:** 

**[3172.64s] English:** It seems like a very important part of the step.  
**Translation:** 

**[3175.72s] English:** Yeah.  
**Translation:** 

**[3176.26s] English:** How you generate the images.  
**Translation:** 

**[3177.60s] English:** They're similar, but sufficiently different.  
**Translation:** 

**[3179.66s] English:** Yeah, that's right.  
**Translation:** Vocabulary: sufficiently: 足够地

**[3180.24s] English:** It's an important step, and it's also an annoying step  
**Translation:** 

**[3182.34s] English:** because you need to have that knowledge of what data augmentation you can do  
**Translation:** 

**[3186.76s] English:** that do not change the nature of the object.  
**Translation:** 

**[3190.50s] English:** And so the standard scenario,  
**Translation:** 

**[3193.18s] English:** which a lot of people working in this area are using,  
**Translation:** 

**[3195.42s] English:** is you use the type of distortion.  
**Translation:** Vocabulary: distortion: 扭曲

**[3199.86s] English:** So basically you do geometric distortion.  
**Translation:** 

**[3202.12s] English:** So one basically just shifts the image a little bit.  
**Translation:** Vocabulary: geometric: 几何变形

**[3204.24s] English:** It's called cropping.  
**Translation:** 

**[3205.06s] English:** Another one kind of changes the scale a little bit.  
**Translation:** Vocabulary: cropping: 裁剪

**[3207.76s] English:** Another one kind of rotates it.  
**Translation:** 

**[3209.14s] English:** Another one changes the colors.  
**Translation:** Vocabulary: rotates: 旋转

**[3210.70s] English:** You know, you can do a shift in color balance or something like that.  
**Translation:** 

**[3214.96s] English:** Saturation.  
**Translation:** 

**[3215.76s] English:** Another one sort of blurs it.  
**Translation:** 

**[3217.10s] English:** Another one adds noise.  
**Translation:** 

**[3218.10s] English:** So you have like a catalog of kind of standard things.  
**Translation:** 

**[3221.10s] English:** And people try to use the same ones for different algorithms so that they can compare.  
**Translation:** 

**[3225.88s] English:** But some algorithms, some self-supervised algorithms actually can deal with much bigger,  
**Translation:** 

**[3230.60s] English:** like more aggressive data augmentation, and some don't.  
**Translation:** 

**[3233.50s] English:** So that kind of makes the whole thing difficult.  
**Translation:** 

**[3236.32s] English:** But that's the kind of difference.  
**Translation:** 

**[3237.46s] English:** That's the kind of distortions we're talking about.  
**Translation:** 

**[3238.82s] English:** And that's...  
**Translation:** Vocabulary: distortions: 扭曲现象

**[3240.00s] English:** So you train with those distortions,  
**Translation:** 

**[3243.56s] English:** and then you chop off the last layer  
**Translation:** 

**[3247.30s] English:** or couple layers of the network,  
**Translation:** 

**[3251.14s] English:** and you use the representation as input to a classifier,  
**Translation:** 

**[3253.58s] English:** you train the classifier on ImageNet, let's say,  
**Translation:** 

**[3257.64s] English:** or whatever, and measure the performance.  
**Translation:** 

**[3260.54s] English:** And interestingly enough,  
**Translation:** 

**[3263.12s] English:** the methods that are really good  
**Translation:** 

**[3264.42s] English:** at eliminating the information that is irrelevant,  
**Translation:** 

**[3266.84s] English:** which is the distortions between those images,  
**Translation:** Vocabulary: irrelevant: 无关的

**[3270.00s] English:** do a good job at eliminating it.  
**Translation:** 

**[3272.38s] English:** And as a consequence, you cannot use  
**Translation:** Vocabulary: cannot: 不能

**[3274.96s] English:** the representations in those systems  
**Translation:** 

**[3277.20s] English:** for things like object detection and localization,  
**Translation:** Vocabulary: detection: 检测

**[3279.88s] English:** because that information is gone.  
**Translation:** 

**[3282.60s] English:** So the type of data augmentation you need to do  
**Translation:** 

**[3284.72s] English:** depends on the task you want, eventually,  
**Translation:** 

**[3287.20s] English:** the system to solve.  
**Translation:** 

**[3288.64s] English:** And the type of data augmentation,  
**Translation:** 

**[3290.68s] English:** standard data augmentation that we use today,  
**Translation:** Vocabulary: augmentation: 数据扩增

**[3292.54s] English:** are only appropriate for object recognition  
**Translation:** 

**[3294.68s] English:** or image classification.  
**Translation:** 

**[3296.02s] English:** They're not appropriate for things like...  
**Translation:** 

**[3297.72s] English:** Can you help me out understand  
**Translation:** 

**[3299.04s] English:** what WideLog does?  
**Translation:** 

**[3300.00s] English:** The localization?  
**Translation:** 

**[3300.84s] English:** So you're saying it's just not good at the negative,  
**Translation:** 

**[3303.78s] English:** like at classifying the negative,  
**Translation:** 

**[3305.48s] English:** so that's why it can't be used for the localization?  
**Translation:** 

**[3307.96s] English:** No, it's just that you train the system,  
**Translation:** 

**[3310.38s] English:** you know, you give it an image,  
**Translation:** 

**[3312.40s] English:** and then you give it the same image, shifted and scaled,  
**Translation:** 

**[3315.00s] English:** and you tell it that's the same image.  
**Translation:** 

**[3317.44s] English:** So the system, basically, is trained to eliminate  
**Translation:** 

**[3319.70s] English:** the information about position and size.  
**Translation:** 

**[3322.08s] English:** So now, and now you want to use that  
**Translation:** 

**[3324.80s] English:** to figure out where an object is and what size it is.  
**Translation:** 

**[3327.76s] English:** Like a bounding box, like they'd be able to actually...  
**Translation:** Vocabulary: bounding: 包围框

**[3330.00s] English:** Okay, it can still find the object in the image, it's just not very good at finding the exact boundaries of that object.  
**Translation:** 

**[3337.36s] English:** Interesting, which, you know, that's an interesting sort of philosophical question.  
**Translation:** Vocabulary: philosophical: 哲学的

**[3343.52s] English:** How important is object localization anyway?  
**Translation:** 

**[3346.82s] English:** We're like obsessed by measuring like image segmentation, obsessed by measuring perfectly knowing the boundaries of objects  
**Translation:** Vocabulary: segmentation: 图像分割

**[3354.62s] English:** when arguably that's not that...  
**Translation:** 

**[3360.00s] English:** essential to understanding what are the contents of the scene on the other hand i think evolutionarily  
**Translation:** Vocabulary: arguably: 可以说; evolutionarily: 从进化角度看

**[3365.76s] English:** the first vision systems in animals were basically all about localization very little about  
**Translation:** 

**[3370.80s] English:** recognition and in the human brain you have two separate pathways for um recognizing the nature  
**Translation:** Vocabulary: pathways: 识别路径

**[3378.40s] English:** of a scene or an object and localizing objects so you use the first pathway called eventual pathway  
**Translation:** 

**[3385.20s] English:** for you know telling what you're looking at uh the other path with the dorsal pathway is used  
**Translation:** Vocabulary: dorsal: 背侧路径; eventual: 最终的; pathway: 通路

**[3390.88s] English:** for navigation for grasping for everything else and you know basically a lot of the things you  
**Translation:** 

**[3395.76s] English:** need for survival are localization and detection is similarity learning or contrastive learning  
**Translation:** Vocabulary: grasping: 抓取; navigation: 导航

**[3404.96s] English:** are these non-contrastive methods the same as understanding something just because you know  
**Translation:** 

**[3409.76s] English:** distorted cat is the same as a non-distorted cat does that mean you understand what it means to  
**Translation:** 

**[3415.20s] English:** be a cat to some extent i mean it's a superficial understanding obviously but like what is the  
**Translation:** 

**[3420.72s] English:** ceiling of this method do you think is this just one trick on the path to doing self-supervised  
**Translation:** Vocabulary: superficial: 表面的

**[3426.88s] English:** learning can we go yeah really really far i think we can go really far so if we figure out how to  
**Translation:** 

**[3434.40s] English:** uh use techniques of that type perhaps very different but you know the same nature to  
**Translation:** 

**[3440.32s] English:** train a system from from video to do video prediction essentially  
**Translation:** 

**[3445.76s] English:** i think we'll have a path um you know towards uh you know i wouldn't say unlimited but but a  
**Translation:** 

**[3451.92s] English:** path towards some level of uh you know physical common sense in uh in machines and uh i also think  
**Translation:** 

**[3459.20s] English:** that um that ability to learn how the world works from a sort of high throughput channel like like  
**Translation:** Vocabulary: throughput: 高通量

**[3468.08s] English:** vision is a necessary step towards uh sort of real artificial intelligence  
**Translation:** 

**[3475.20s] English:** in other words i believe in grounded intelligence i don't think we can train a machine to  
**Translation:** 

**[3480.00s] English:** intelligent purely from text because i think the amount of information about the world that's  
**Translation:** 

**[3484.96s] English:** contained in text is tiny compared to what we need to know so for example let's uh and you know  
**Translation:** 

**[3493.76s] English:** people have attempted to do this for for 30 years right the psych project and things like that right  
**Translation:** 

**[3498.32s] English:** of basically kind of writing down all the facts that are known and hoping that some some sort of  
**Translation:** Vocabulary: psych: 心理学

**[3503.52s] English:** common sense will emerge um i think it's basically hopeless but let me take an example you take an  
**Translation:** 

**[3508.64s] English:** object i describe a situation to you i take an object i put it on the table and i push the table  
**Translation:** 

**[3514.80s] English:** it's completely obvious to you that the object will be pushed with the table  
**Translation:** 

**[3518.56s] English:** right because it's sitting on it there's no text in the world i believe that explains this  
**Translation:** 

**[3524.96s] English:** and so if you train a machine as powerful as it could be you know your gpt 5000  
**Translation:** 

**[3532.64s] English:** or whatever it is it's never going to learn about this  
**Translation:** 

**[3537.04s] English:** that information is just never  
**Translation:** 

**[3539.04s] English:** not present in any text well the question like with the psych project the dream i think  
**Translation:** 

**[3543.92s] English:** is to have like like 10 million say facts like that that give you a head start like a parent  
**Translation:** 

**[3554.00s] English:** guiding you now we humans don't need a parent to tell us that the table will move sorry the  
**Translation:** 

**[3559.52s] English:** smartphone will move with the table but we get a lot of guidance in other ways so it's possible  
**Translation:** 

**[3566.48s] English:** that we can give it a quick shortcut what about the rate of emplee here's to the table right so  
**Translation:** Vocabulary: shortcut: 捷径

**[3568.40s] English:** And what about a cat?  
**Translation:** 

**[3569.38s] English:** A cat knows that.  
**Translation:** 

**[3571.06s] English:** No, but they evolved.  
**Translation:** 

**[3573.08s] English:** No, they learn like us.  
**Translation:** 

**[3575.86s] English:** Sorry, the physics of stuff?  
**Translation:** 

**[3577.32s] English:** Yeah.  
**Translation:** 

**[3578.90s] English:** Well, yeah, so you're saying it's –  
**Translation:** 

**[3582.42s] English:** so you're putting a lot of intelligence onto the nurture side, not the nature.  
**Translation:** 

**[3587.12s] English:** Yeah.  
**Translation:** 

**[3587.28s] English:** Because we seem to have –  
**Translation:** 

**[3589.28s] English:** there's a very inefficient, arguably, process of evolution  
**Translation:** 

**[3593.50s] English:** that got us from bacteria to who we are today.  
**Translation:** Vocabulary: arguably: 或许; bacteria: 细菌; inefficient: 低效

**[3596.70s] English:** Okay, started at the bottom, now we're here.  
**Translation:** 

**[3600.00s] English:** So the question is, how fundamental is that, the nature of the whole hardware?  
**Translation:** 

**[3608.50s] English:** And then is there any way to shortcut it if it's fundamental?  
**Translation:** 

**[3612.38s] English:** If it's not, if it's most of intelligence, most of the cool stuff we've been talking about is mostly nurture, mostly trained.  
**Translation:** Vocabulary: nurture: 培养

**[3618.78s] English:** We figure it out by observing the world.  
**Translation:** 

**[3620.32s] English:** We can form that big, beautiful, sexy background model that you're talking about just by sitting there.  
**Translation:** 

**[3627.02s] English:** Then, okay, then you need to, then, like, maybe it is all supervised learning all the way down.  
**Translation:** 

**[3637.86s] English:** It's all supervised learning, sorry.  
**Translation:** Vocabulary: supervised: 监督学习

**[3638.98s] English:** Whatever it is that makes, you know, human intelligence different from other animals, which, you know, a lot of people think is language and logical reasoning and this kind of stuff.  
**Translation:** 

**[3648.32s] English:** It cannot be that complicated because it only popped up in the last million years.  
**Translation:** Vocabulary: cannot: 不可能

**[3653.96s] English:** And, you know, it only involves.  
**Translation:** 

**[3657.02s] English:** You know, less than 1% of our genome might be, which is the difference between human genome and chimps or whatever.  
**Translation:** Vocabulary: chimps: 黑猩猩; genome: 基因组

**[3663.28s] English:** So it can't be that complicated.  
**Translation:** 

**[3666.52s] English:** You know, it can't be that fundamental.  
**Translation:** 

**[3667.90s] English:** I mean, most of the complicated stuff already exists in cats and dogs and, you know, certainly primates, non-human primates.  
**Translation:** 

**[3677.00s] English:** Yeah, that little thing with humans might be just something about social interaction and ability to maintain ideas across, like, a collective of people.  
**Translation:** Vocabulary: primates: 灵长类动物

**[3687.02s] English:** It sounds very dramatic and very impressive, but it probably isn't, mechanistically speaking.  
**Translation:** 

**[3693.32s] English:** It is, but we're not there yet.  
**Translation:** Vocabulary: mechanistically: 机械地

**[3694.66s] English:** Like, you know, we have, I mean, this is number 634, you know, in the list of problems we have to solve.  
**Translation:** 

**[3703.38s] English:** So basic physics of the world is number one.  
**Translation:** 

**[3706.88s] English:** What do you, just a quick tangent on data augmentation.  
**Translation:** 

**[3711.62s] English:** So a lot of it is hard coded versus learned.  
**Translation:** Vocabulary: augmentation: 数据增强; tangent: 旁白

**[3717.02s] English:** Do you have any intuition that maybe.  
**Translation:** 

**[3720.00s] English:** be there could be some weird data augmentation like generative type of data augmentation like  
**Translation:** Vocabulary: generative: 生成式; intuition: 直觉

**[3726.28s] English:** doing something weird to images which then improves the the similarity learning process  
**Translation:** 

**[3732.80s] English:** so not just kind of dumb simple distortions but by you shaking your head just saying that  
**Translation:** Vocabulary: distortions: 扭曲变形

**[3738.88s] English:** even simple distortions are enough i think no i think data augmentation is a temporary necessary  
**Translation:** 

**[3744.42s] English:** evil so what people are working on now is is two things one is uh the type of self-supervised  
**Translation:** 

**[3751.60s] English:** learning like trying to to translate the type of self-supervised learning people use in language  
**Translation:** 

**[3756.64s] English:** translating these two images which is basically a denoising autoencoder method right so you you  
**Translation:** Vocabulary: autoencoder: 自动编码器; denoising: 去噪

**[3762.36s] English:** take an image you you block you mask some parts of it and then you you train some giant neural  
**Translation:** 

**[3769.32s] English:** net to reconstruct the parts that you've that are that are missing and until  
**Translation:** Vocabulary: neural: 神经网络; reconstruct: 重建

**[3774.28s] English:** until  
**Translation:** 

**[3774.40s] English:** very recently there was no there was no working methods for that uh all the autoencoder type  
**Translation:** 

**[3780.24s] English:** methods for images weren't producing very good representation but there's a paper now coming  
**Translation:** 

**[3784.64s] English:** out of uh the fair group in menlo park that actually works very well so that doesn't  
**Translation:** 

**[3791.14s] English:** require data augmentation that requires only masking okay only masking for images uh okay  
**Translation:** 

**[3798.44s] English:** right so you mask part of the image and you train a system which you know in this case is a  
**Translation:** 

**[3803.98s] English:** transformer  
**Translation:** 

**[3804.26s] English:** because you you can you can the transformer represents the image as uh non-overlapping  
**Translation:** 

**[3810.36s] English:** patches so it's easy to mask patches and things like that okay then my question transfers to that  
**Translation:** 

**[3815.24s] English:** problem then masking like why should the mask be a square or rectangle yeah so it doesn't matter  
**Translation:** Vocabulary: rectangle: 矩形; transfers: 转移

**[3820.76s] English:** like you know i think we're gonna come up probably in the future with sort of uh you know ways to  
**Translation:** 

**[3826.74s] English:** mask that are you know kind of random essentially well i mean they are random already but no no but  
**Translation:** 

**[3833.48s] English:** like something  
**Translation:** 

**[3834.14s] English:** that's challenging like optimally challenging so like  
**Translation:** Vocabulary: optimally: 最佳地

**[3840.00s] English:** mean maybe it's a metaphor that doesn't apply but you're it seems like there's  
**Translation:** 

**[3844.56s] English:** an data augmentation or masking there's an interactive element with it like  
**Translation:** Vocabulary: augmentation: 数据增强; interactive: 互动元素; metaphor: 比喻

**[3849.96s] English:** you're almost like playing with an image yeah and like it's like the way we play  
**Translation:** 

**[3854.10s] English:** with an image in our minds now it's like dropout it's like boson machine training  
**Translation:** Vocabulary: boson: 玻色子

**[3857.94s] English:** you you know every every every time you see a percept you also you you can you  
**Translation:** 

**[3865.20s] English:** can perturb it in some way and then the the principle of the training procedure  
**Translation:** Vocabulary: percept: 感知; perturb: 干扰

**[3870.70s] English:** is to minimize the difference of the output or the representation between the  
**Translation:** 

**[3875.70s] English:** the clean version and the corrupted version essentially right and you can do  
**Translation:** Vocabulary: corrupted: 损坏的数据

**[3881.22s] English:** this in real time right so you know boson machine work like this right you  
**Translation:** 

**[3884.38s] English:** you you show a percept you tell the machine that's a good combination of  
**Translation:** 

**[3888.72s] English:** activities or your input neurons and then you either  
**Translation:** 

**[3895.20s] English:** let them go their merry way without clamping them to values or you only do  
**Translation:** Vocabulary: clamping: 固定; neurons: 神经元

**[3900.60s] English:** this with a subset yeah and what you're doing is you're training the system so  
**Translation:** 

**[3904.76s] English:** that the the stable state of the entire network is the same regardless of  
**Translation:** 

**[3909.16s] English:** whether it sees the entire input or whether it sees only part of it you know  
**Translation:** 

**[3914.04s] English:** denoising autoencoder method is basically the same thing right you you're  
**Translation:** Vocabulary: autoencoder: 自动编码器; denoising: 去噪

**[3917.16s] English:** you're training a system to reproduce the input the complete inputs and  
**Translation:** 

**[3920.54s] English:** filling the blanks regardless of which which parts are missing and that's  
**Translation:** 

**[3924.32s] English:** really the underlying principle of the system.  
**Translation:** 

**[3925.20s] English:** And you could imagine sort of even in the brain some sort of neural principle  
**Translation:** Vocabulary: neural: 神经的

**[3929.34s] English:** where you know neurons gonna oscillate right so they they take their activity  
**Translation:** 

**[3934.54s] English:** and then temporarily they kind of shut off to you know force the rest of the  
**Translation:** Vocabulary: oscillate: 振荡; temporarily: 暂时

**[3939.02s] English:** system to basically reconstruct the input without their help you know and and  
**Translation:** 

**[3945.36s] English:** and I mean you can imagine you know possibly you know more or less  
**Translation:** Vocabulary: reconstruct: 重新构建

**[3949.50s] English:** biologically plausible processes.  
**Translation:** 

**[3950.96s] English:** Something like that and I guess with this denoising auto encoder and  
**Translation:** Vocabulary: biologically: 生物学上; plausible: 合乎情理

**[3955.20s] English:** masking and data augmentation you don't have to worry about being super  
**Translation:** 

**[3960.00s] English:** efficient you can just do as much as you want yeah and get better over time because i was thinking  
**Translation:** 

**[3966.72s] English:** like you might want to be clever about the way you do all these procedures you know but that's only  
**Translation:** 

**[3973.84s] English:** it's somehow costly to do every iteration but it's not really not really maybe and then there is you  
**Translation:** Vocabulary: iteration: 迭代

**[3980.96s] English:** know data augmentation without explicit data augmentation is data augmentation by waiting  
**Translation:** 

**[3985.44s] English:** which is you know the the sort of video prediction um you're observing a video clip  
**Translation:** Vocabulary: augmentation: 增加; explicit: 明确

**[3991.36s] English:** observing the you know the the continuation of that video clip and try you try to learn a  
**Translation:** 

**[3997.04s] English:** representation using those joint embedding architectures in such a way that the representation  
**Translation:** Vocabulary: continuation: 延续; embedding: 嵌入

**[4001.76s] English:** of the future clip is easily predictable from the representation of the of the observed clip  
**Translation:** 

**[4008.48s] English:** do you think youtube has enough raw data from which to learn how to be a cat  
**Translation:** Vocabulary: predictable: 可预测的

**[4016.24s] English:** i think so so the the amount of data is not the constraint no it would require some selection  
**Translation:** 

**[4023.12s] English:** i think some some selection of you know maybe the right type of data you don't go down the  
**Translation:** Vocabulary: constraint: 限制

**[4029.12s] English:** rabbit hole of just cat videos that might you might need to watch some lectures or something  
**Translation:** 

**[4034.48s] English:** no you wouldn't how meta would that be if it like watches lectures about intelligence and  
**Translation:** 

**[4041.36s] English:** then learns watches your lectures in nyu and learns from that how to  
**Translation:** 

**[4045.44s] English:** be intelligent i don't think there would be enough what's your um do you find multi-modal learning  
**Translation:** 

**[4052.72s] English:** interesting we've been talking about visual language like combining those together maybe  
**Translation:** 

**[4056.72s] English:** audio all those kinds of things there's a lot of things that i find interesting in the short term  
**Translation:** 

**[4061.04s] English:** but are not addressing the important problem that i think are really kind of the big challenges so i  
**Translation:** 

**[4066.88s] English:** think you know things like multitasking learning continual learning uh you know adversarial issues  
**Translation:** Vocabulary: adversarial: 对抗问题; continual: 持续学习; multitasking: 多任务处理

**[4074.24s] English:** i mean those have you know really important to you yeah thank you very much that's really interesting  
**Translation:** 

**[4074.32s] English:** i mean those have you know really important to you yeah thank you very much that's really  
**Translation:** 

**[4075.36s] English:** great practical interests in the relatively short term, possibly.  
**Translation:** 

**[4080.00s] English:** But I don't think they're fundamental, you know, active learning, even to some extent  
**Translation:** 

**[4083.32s] English:** reinforcement learning.  
**Translation:** 

**[4084.32s] English:** I think those things will become either obsolete or useless or easy once we figure out how  
**Translation:** Vocabulary: obsolete: 过时; reinforcement: 强化

**[4093.12s] English:** to do self-supervised representation learning or learning predictive world models.  
**Translation:** 

**[4099.42s] English:** And so I think that's what, you know, the entire community should be focusing on.  
**Translation:** Vocabulary: predictive: 预测性的

**[4104.50s] English:** At least people who are interested in sort of fundamental questions or, you know, really  
**Translation:** 

**[4107.42s] English:** kind of pushing the envelope of AI towards the next stage.  
**Translation:** 

**[4110.66s] English:** But of course, there's like a huge amount of, you know, very interesting work to do  
**Translation:** 

**[4114.30s] English:** in sort of practical questions that have, you know, short-term impact.  
**Translation:** 

**[4117.66s] English:** Well, you know, it's difficult to talk about the temporal scale because all of human  
**Translation:** 

**[4123.62s] English:** civilization will eventually be destroyed because the sun will die out.  
**Translation:** Vocabulary: temporal: 时间的

**[4128.66s] English:** And even if Elon Musk is successful, multi-planetary colonization across the galaxy, eventually  
**Translation:** 

**[4135.52s] English:** the entirety of it will just become obsolete.  
**Translation:** Vocabulary: colonization: 殖民; entirety: 全部; galaxy: 星系

**[4137.40s] English:** It's going to take a while though.  
**Translation:** 

**[4142.72s] English:** But what I'm saying is then that logic can be used to say it's all meaningless.  
**Translation:** Vocabulary: meaningless: 无意义

**[4147.38s] English:** I'm saying all that to say that multitask learning might be, you're calling it practical  
**Translation:** 

**[4155.38s] English:** or pragmatic or whatever.  
**Translation:** Vocabulary: multitask: 多任务; pragmatic: 实用

**[4157.50s] English:** That might be the thing that achieves something very akin to intelligence while we're trying  
**Translation:** 

**[4163.84s] English:** to solve the more general problem of self-supervision.  
**Translation:** 

**[4166.64s] English:** The problem of self-supervised learning of background knowledge.  
**Translation:** 

**[4169.58s] English:** So the reason I bring that up, maybe one way to ask that question, I've been very impressed  
**Translation:** 

**[4173.98s] English:** by what Tesla Autopilot team is doing.  
**Translation:** 

**[4176.02s] English:** I don't know if you've got any chance to glance at this particular one example of multitask  
**Translation:** 

**[4181.20s] English:** learning where they're literally taking the problem, like, I don't know, Charles Darwin  
**Translation:** 

**[4186.68s] English:** starts studying animals.  
**Translation:** Vocabulary: darwin: 达尔文

**[4189.04s] English:** They're studying the problem of driving and asking, okay, what are all the things you  
**Translation:** 

**[4193.40s] English:** have to perceive?  
**Translation:** Vocabulary: perceive: 感知

**[4195.42s] English:** And the way they do it.  
**Translation:** 

**[4196.08s] English:** They're studying the problem of driving and asking, okay, what are all the things you have to perceive?  
**Translation:** 

**[4196.64s] English:** And the way they're solving it is one, there's an ontology where you're bringing that to  
**Translation:** 

**[4200.00s] English:** table so you're formulating a bunch of different tasks it's like over 100 tasks or something like  
**Translation:** Vocabulary: ontology: 本体论

**[4204.00s] English:** that that they're involved in driving and then they're deploying it and then getting data back  
**Translation:** 

**[4208.72s] English:** from people that run into trouble and they're trying to figure out do we add tasks do we like  
**Translation:** Vocabulary: deploying: 部署

**[4213.58s] English:** we focus on each individual task separately sure in fact half so the i would say i'll classify  
**Translation:** 

**[4218.82s] English:** andre kapathi's talking to is so one was about doors and the other one about how much image net  
**Translation:** Vocabulary: classify: 分类

**[4224.14s] English:** sucks he kept going back and forth on those two topics which image net sucks meaning you can't  
**Translation:** 

**[4231.32s] English:** just use a single benchmark there's so like you you have to have like a giant suite of benchmarks  
**Translation:** Vocabulary: benchmark: 参考标准; benchmarks: 多个参考标准

**[4237.80s] English:** to understand how well your your system actually i agree with him i mean he's uh he's a very sensible  
**Translation:** 

**[4242.46s] English:** guy um now okay it's it's very clear that if you're faced with a an engineering problem that  
**Translation:** Vocabulary: sensible: 理智的

**[4249.76s] English:** you need to solve in a relatively short time particularly if you have it almost  
**Translation:** 

**[4253.98s] English:** breathing down your neck you're gonna have to take shortcuts right you you you might think  
**Translation:** Vocabulary: shortcuts: 捷径

**[4259.02s] English:** about the the fact that the the the right thing to do and the long-term solution involves you know  
**Translation:** 

**[4264.46s] English:** some fancy self-supervisioning but you have you know you're almost breathing on your neck uh and  
**Translation:** 

**[4270.54s] English:** you know this involves uh you know human lives and so you you have to basically just do the  
**Translation:** 

**[4277.58s] English:** systematic uh engineering and you know uh fine tuning and refinements and trial and error  
**Translation:** Vocabulary: refinements: 改进

**[4283.98s] English:** and and all that stuff um there's nothing wrong with that that's that's called engineering that's  
**Translation:** 

**[4288.70s] English:** called you know uh putting technology out uh in the in the world um and and you have to kind of  
**Translation:** 

**[4297.74s] English:** ironclad it before before you do this you know um uh so much for you know grand grand ideas and  
**Translation:** 

**[4305.42s] English:** principles um but you know i'm placing myself sort of you know some you know upstream of the  
**Translation:** Vocabulary: ironclad: 坚不可摧

**[4313.98s] English:** screen or quite a bit upstream of this your play don't think about platonic forms your platonic  
**Translation:** 

**[4320.00s] English:** eventually I want that stuff to get used but it's okay if it takes five or ten  
**Translation:** Vocabulary: platonic: 理念

**[4326.62s] English:** years for the community to realize this is the right thing to do I've I've done  
**Translation:** 

**[4330.08s] English:** this before it's been the case before that you know I've made that case I mean  
**Translation:** 

**[4334.64s] English:** if you look back in the mid-2000s for example and you ask yourself the  
**Translation:** 

**[4338.62s] English:** question okay I want to recognize cars or faces or whatever you know I can use  
**Translation:** 

**[4344.96s] English:** convolutional net so I can use a more conventional kind of computer vision  
**Translation:** 

**[4349.08s] English:** techniques you know using interest point detectors or a shift density  
**Translation:** Vocabulary: convolutional: 卷积网络; density: 密度; detectors: 检测器

**[4353.04s] English:** features and you know sticking an SVM on top at that time the data sets were so  
**Translation:** 

**[4357.02s] English:** small that those methods that use more and engineering work better than  
**Translation:** Vocabulary: sticking: 附加

**[4363.12s] English:** confidence there's just not enough data for comments and comments were were a  
**Translation:** 

**[4366.78s] English:** little a little slow with the kind of hardware that was available at the time  
**Translation:** 

**[4369.84s] English:** and there was a sea change when basically when you know data sets  
**Translation:** 

**[4376.00s] English:** became bigger and and GPUs became available that that's  
**Translation:** 

**[4378.96s] English:** what I'm talking about.  
**Translation:** 

**[4379.08s] English:** you know the two of the main factors that basically made people  
**Translation:** 

**[4384.30s] English:** change their change their mind and you can you can look at the history of like  
**Translation:** 

**[4391.98s] English:** all sub branches of AI or pattern recognition and there's a similar  
**Translation:** 

**[4397.50s] English:** trajectory followed by techniques where people start by you know engineering the  
**Translation:** 

**[4402.78s] English:** head out of it you know be it optical character recognition  
**Translation:** Vocabulary: trajectory: 发展趋势

**[4409.08s] English:** speech recognition computer vision like image recognition in general natural language  
**Translation:** 

**[4415.02s] English:** understanding like you know translation things like that right you start to engineer the hell out  
**Translation:** 

**[4419.28s] English:** of it you start to acquire all the knowledge the prior knowledge you know about image formation  
**Translation:** 

**[4424.68s] English:** about you know the shape of characters about you know morphological operations about like  
**Translation:** Vocabulary: morphological: 形态学的

**[4430.14s] English:** feature extraction Fourier transforms you know vernicle moments you know whatever right people  
**Translation:** 

**[4434.82s] English:** have come up with thousands of ways of representing images so that they could be easily  
**Translation:** Vocabulary: extraction: 特征提取; fourier: 傅里叶; transforms: 变换

**[4439.08s] English:** uh uh  
**Translation:** 

**[4440.00s] English:** classified afterwards. Same for speech recognition, right? There is, you know, it took decades  
**Translation:** 

**[4444.62s] English:** for people to figure out a good front end to pre-process a speech signal so that, you  
**Translation:** 

**[4450.32s] English:** know, the information about what is being said is preserved, but most of the information  
**Translation:** 

**[4454.40s] English:** about the identity of the speaker is gone. You know, contextual coefficients or whatever,  
**Translation:** 

**[4461.38s] English:** right? And same for text, right? You do named entity recognition and you parse and you do  
**Translation:** Vocabulary: coefficients: 系数; parse: 解析

**[4469.38s] English:** tagging of the parts of speech and you do this sort of tree representation of clauses  
**Translation:** 

**[4476.62s] English:** and all that stuff right before you can do anything. So that's how it starts, right?  
**Translation:** 

**[4484.92s] English:** Just engineer the hell out of it. And then you start having data and maybe you have more  
**Translation:** 

**[4490.38s] English:** powerful computers. Maybe you know something about statistical learning. So you start using  
**Translation:** 

**[4494.06s] English:** machine learning and it's usually a small sliver on top of your kind of handcrafted  
**Translation:** 

**[4497.46s] English:** system where, you know, you extract.  
**Translation:** Vocabulary: handcrafted: 手工制作

**[4499.38s] English:** Features by hand. Okay. And now, you know, nowadays the standard way of doing this is  
**Translation:** 

**[4503.88s] English:** that you train the entire thing end to end with a deep learning system and it learns  
**Translation:** 

**[4506.88s] English:** its own features and, you know, speech recognition systems nowadays, OCR systems are completely  
**Translation:** 

**[4513.44s] English:** end to end. It's, you know, it's some giant neural net that takes raw waveforms and produces  
**Translation:** Vocabulary: neural: 神经网络; waveforms: 波形

**[4519.54s] English:** a sequence of characters coming out. And it's just a huge neural net, right? There's no,  
**Translation:** 

**[4523.62s] English:** you know, Markov model, there's no language model that is explicit other than, you know,  
**Translation:** Vocabulary: explicit: 明确; markov: 马尔可夫

**[4529.38s] English:** trained in the, in the sort of neural language model, if you want. Same for translation,  
**Translation:** 

**[4533.14s] English:** same for all kinds of stuff. So you see this continuous evolution from, you know, less  
**Translation:** 

**[4539.88s] English:** and less handcrafting and more and more learning. And I think, I mean, it's true in biology  
**Translation:** 

**[4548.96s] English:** as well.  
**Translation:** Vocabulary: handcrafting: 手工制作

**[4549.96s] English:** So, I mean, we might disagree about this, maybe not in this one little piece at the  
**Translation:** 

**[4556.72s] English:** end, you mentioned active learning.  
**Translation:** 

**[4559.38s] English:** It's  
**Translation:** 

**[4560.00s] English:** It feels like active learning, which is the selection of data, and also the interactivity, needs to be part of this giant neural network.  
**Translation:** 

**[4566.86s] English:** You cannot just be an observer to do self-supervised learning.  
**Translation:** 

**[4569.62s] English:** Well, self-supervised learning is just a word, but whatever this giant stack of a neural network that's automatically learning, it feels…  
**Translation:** 

**[4580.78s] English:** My intuition is that you have to have a system, whether it's a physical robot or a digital robot, that's interacting with the world and doing so in a flawed way and improving over time.  
**Translation:** 

**[4596.54s] English:** In order to form the self-supervised learning, well, you can't just give it a giant sea of data.  
**Translation:** Vocabulary: intuition: 直觉

**[4605.00s] English:** Okay, I agree and I disagree.  
**Translation:** 

**[4606.70s] English:** I agree in the sense that I think…  
**Translation:** 

**[4610.00s] English:** I agree.  
**Translation:** 

**[4610.66s] English:** I agree.  
**Translation:** 

**[4610.76s] English:** I agree.  
**Translation:** 

**[4610.78s] English:** I agree in two ways.  
**Translation:** 

**[4612.06s] English:** The first way I agree is that if you want, and you certainly need, a causal model of the world that allows you to predict the consequences of your actions, to train that model, you need to take actions.  
**Translation:** 

**[4622.66s] English:** You need to be able to act in a world and see the effect for you to learn causal models of the world.  
**Translation:** 

**[4628.36s] English:** So that's not obvious because you can observe others.  
**Translation:** 

**[4631.52s] English:** You can observe others.  
**Translation:** 

**[4632.18s] English:** And you can infer that they're similar to you, and then you can learn from that.  
**Translation:** 

**[4635.86s] English:** Yeah, but then you have to kind of hardwire that part, mirror neurons and all that stuff.  
**Translation:** Vocabulary: hardwire: 固化; neurons: 神经元

**[4640.34s] English:** And it's not clear to me how you would do this in a machine.  
**Translation:** 

**[4644.62s] English:** So I think the action part would be necessary for having causal models of the world.  
**Translation:** 

**[4653.08s] English:** The second reason it may be necessary or at least more efficient is that active learning basically goes for the jiggler of what you don't know.  
**Translation:** 

**[4665.02s] English:** There's obvious areas of uncertainty about your world.  
**Translation:** 

**[4670.06s] English:** And about how the world behaves.  
**Translation:** 

**[4673.06s] English:** And you can resolve this uncertainty by systematic exploration of that part that you don't know.  
**Translation:** 

**[4680.00s] English:** and if you know that you don't know then you know it makes you curious you kind  
**Translation:** 

**[4683.32s] English:** of look into situations that and you know across the animal world the  
**Translation:** 

**[4689.30s] English:** different species at different levels of curiosity right yeah depending on how  
**Translation:** 

**[4694.40s] English:** they build right so you know cats and rats are incredibly curious dogs not so  
**Translation:** 

**[4699.26s] English:** much mean less yeah so it could be useful to have that kind of curiosity so  
**Translation:** 

**[4704.04s] English:** it'd be useful but curiosity just makes the process faster it doesn't make the  
**Translation:** 

**[4707.56s] English:** process exist the so what process what learning process is it that active  
**Translation:** 

**[4716.00s] English:** learning makes more efficient and I'm asking that first question you know you  
**Translation:** 

**[4723.28s] English:** know we haven't answered that question yet so you know I worry about active  
**Translation:** 

**[4726.40s] English:** learning once this question is the more fundamental question to ask and if  
**Translation:** 

**[4731.50s] English:** active learning or interaction increases the efficiency of the learning see  
**Translation:** 

**[4737.20s] English:** sometimes  
**Translation:** 

**[4737.54s] English:** it becomes very different if the increase is several orders of magnitude  
**Translation:** 

**[4742.82s] English:** right like that's true but fundamentally is still the same thing and building up  
**Translation:** Vocabulary: fundamentally: 本质上

**[4749.12s] English:** the intuition about how to in a self-supervised way to construct  
**Translation:** 

**[4752.96s] English:** background models efficient or inefficient is is the core problem what  
**Translation:** Vocabulary: inefficient: 不高效; intuition: 直觉

**[4758.78s] English:** do you think about your show banjos talking about consciousness and all of  
**Translation:** 

**[4763.46s] English:** these kinds of concepts okay I don't know what consciousness is  
**Translation:** Vocabulary: banjos: 班卓琴

**[4767.18s] English:** okay I don't know what consciousness is  
**Translation:** 

**[4767.54s] English:** but it's a good opener and to some extent a lot of the things that are said  
**Translation:** 

**[4774.44s] English:** about consciousness remind me of the questions people were asking themselves  
**Translation:** 

**[4778.40s] English:** in the 18th century or 17th century when they discovered that you know how the  
**Translation:** 

**[4784.28s] English:** eye works and the fact that the image at the back of the eye was upside down  
**Translation:** 

**[4788.90s] English:** right because you have a lens and and so on your retina the image that forms is  
**Translation:** 

**[4793.48s] English:** an image of the world but it's upside down how is it that you see right side up  
**Translation:** 

**[4797.54s] English:** and you know with what we know today in  
**Translation:** Vocabulary: upside: 倒过来的

**[4800.00s] English:** science, we realize this question doesn't make any sense or is kind of ridiculous in  
**Translation:** 

**[4805.54s] English:** some way, right?  
**Translation:** 

**[4806.54s] English:** So I think a lot of what is said about consciousness is of that nature.  
**Translation:** 

**[4809.10s] English:** Now that said, there is a lot of really smart people for whom I have a lot of respect who  
**Translation:** 

**[4813.86s] English:** are talking about this topic, people like David Chalmers, who is a colleague of mine  
**Translation:** 

**[4817.28s] English:** at NYU.  
**Translation:** Vocabulary: chalmers: 查姆斯; colleague: 同事

**[4819.68s] English:** I have kind of an unorthodox, folk, speculative hypothesis about consciousness.  
**Translation:** 

**[4829.32s] English:** So we're talking about this idea of world model, and I think our entire prefrontal cortex  
**Translation:** Vocabulary: cortex: 大脑皮层; hypothesis: 假设; speculative: 推测的; unorthodox: 非传统的

**[4835.46s] English:** basically is the engine for our world model.  
**Translation:** 

**[4840.94s] English:** But when we are attending at a particular situation, we're focused on that situation,  
**Translation:** 

**[4846.18s] English:** we basically cannot attend to anything else.  
**Translation:** 

**[4848.74s] English:** And that seems to suggest that we basically have only one world model engine in our prefrontal  
**Translation:** Vocabulary: cannot: 不能

**[4857.70s] English:** cortex.  
**Translation:** 

**[4858.70s] English:** Okay.  
**Translation:** 

**[4859.32s] English:** So that engine is configurable to the situation at hand.  
**Translation:** 

**[4862.72s] English:** So we are building a box out of wood, or we are driving down the highway playing chess.  
**Translation:** Vocabulary: configurable: 可配置的

**[4869.70s] English:** We basically have a single model of the world that we configure into the situation at hand,  
**Translation:** 

**[4875.46s] English:** which is why we can only attend to one task at a time.  
**Translation:** Vocabulary: configure: 设置

**[4879.30s] English:** Now if there is a task that we do repeatedly, it goes from the sort of deliberate reasoning  
**Translation:** 

**[4885.88s] English:** using model of the world and prediction, and perhaps something like model predictive control,  
**Translation:** Vocabulary: deliberate: 深思熟虑; predictive: 预测性的

**[4888.70s] English:** which I was talking about earlier, to something that is more subconscious that becomes automatic.  
**Translation:** 

**[4894.50s] English:** So I don't know if you've ever played against a chess grandmaster.  
**Translation:** Vocabulary: grandmaster: 特级大师; subconscious: 潜意识

**[4899.18s] English:** I get wiped out in 10 plays, right?  
**Translation:** 

**[4904.12s] English:** And I have to think about my move for 15 minutes, and the person in front of me, the grandmaster,  
**Translation:** 

**[4912.70s] English:** would just react within seconds, right?  
**Translation:** 

**[4916.58s] English:** He doesn't need to think about it.  
**Translation:** 

**[4918.58s] English:** That's become part of the subconscious.  
**Translation:** 

**[4920.00s] English:** because it's basically just pattern recognition  
**Translation:** 

**[4922.64s] English:** at this point.  
**Translation:** 

**[4924.76s] English:** Same, the first few hours you drive a car,  
**Translation:** 

**[4927.72s] English:** you're really attentive, you can't do anything else.  
**Translation:** 

**[4929.80s] English:** And then after 20, 30 hours of practice, 50 hours,  
**Translation:** Vocabulary: attentive: 专心

**[4933.50s] English:** it's subconscious, you can talk to the person next to you,  
**Translation:** 

**[4935.72s] English:** things like that, right?  
**Translation:** 

**[4937.04s] English:** Unless the situation becomes unpredictable,  
**Translation:** 

**[4939.06s] English:** and then you have to stop talking.  
**Translation:** 

**[4941.06s] English:** So that suggests you only have one model in your head.  
**Translation:** 

**[4944.66s] English:** And it might suggest the idea that consciousness basically  
**Translation:** 

**[4948.34s] English:** is the module that configures this world model of yours.  
**Translation:** 

**[4951.96s] English:** You need to have some sort of executive overseer  
**Translation:** Vocabulary: configures: 配置; module: 模块; overseer: 监督者

**[4956.50s] English:** that configures your world model for the situation at hand.  
**Translation:** 

**[4960.60s] English:** And that leads to the really curious concept  
**Translation:** 

**[4963.76s] English:** that consciousness is not a consequence  
**Translation:** 

**[4966.04s] English:** of the power of our minds, but of the limitation  
**Translation:** 

**[4968.66s] English:** of our brains.  
**Translation:** 

**[4970.10s] English:** Because we have only one world model, we have to be conscious.  
**Translation:** 

**[4973.72s] English:** If we had as many world models as the situations we encounter,  
**Translation:** 

**[4978.34s] English:** then we could do all of them simultaneously,  
**Translation:** 

**[4980.74s] English:** and we wouldn't need this sort of executive control  
**Translation:** 

**[4982.94s] English:** that we call consciousness.  
**Translation:** 

**[4984.52s] English:** Yeah, interesting.  
**Translation:** 

**[4985.36s] English:** And somehow, maybe that executive controller,  
**Translation:** 

**[4988.96s] English:** I mean, the hard problem of consciousness,  
**Translation:** 

**[4990.94s] English:** there's some kind of chemicals in biology  
**Translation:** 

**[4992.86s] English:** that's creating a feeling, like it feels to experience  
**Translation:** 

**[4996.76s] English:** some of these things.  
**Translation:** 

**[4998.92s] English:** That's kind of the hard question is, what the heck is that,  
**Translation:** 

**[5003.42s] English:** and why is that useful?  
**Translation:** 

**[5004.72s] English:** Maybe the more pragmatic question,  
**Translation:** 

**[5006.18s] English:** why is it useful to feel like?  
**Translation:** Vocabulary: pragmatic: 实用导向的

**[5008.34s] English:** This is really you experiencing this versus just  
**Translation:** 

**[5011.88s] English:** like information being processed.  
**Translation:** Vocabulary: processed: 加工过的

**[5015.90s] English:** It could be just a very nice side effect of the way we evolved  
**Translation:** 

**[5021.72s] English:** that it's just very useful to feel a sense of ownership  
**Translation:** 

**[5028.56s] English:** to the decisions you make, to the perceptions you make,  
**Translation:** 

**[5031.14s] English:** to the model you're trying to maintain.  
**Translation:** Vocabulary: perceptions: 认知

**[5033.12s] English:** Like you own this thing, and it's the only one you got.  
**Translation:** 

**[5036.22s] English:** And if you lose it, it's going to really suck.  
**Translation:** 

**[5037.78s] English:** Yeah.  
**Translation:** 

**[5038.34s] English:** And so you should really send  
**Translation:** 

**[5040.00s] English:** the brain some signals about it what ideas do you believe might be true that  
**Translation:** 

**[5047.00s] English:** most or at least many people disagree with you with let's say in the space of  
**Translation:** 

**[5052.24s] English:** machine learning well depends who you talk about but I think so certainly  
**Translation:** 

**[5057.40s] English:** there is a bunch of people who are nativist right who think that a lot of  
**Translation:** Vocabulary: nativist: 天赋论者

**[5062.00s] English:** the basic things about the world are kind of hardwired in our you know minds  
**Translation:** 

**[5065.68s] English:** things like you know the world is three-dimensional for example is that  
**Translation:** Vocabulary: hardwired: 天生具备

**[5069.16s] English:** hardwired things like you know object permanence is something that we learn  
**Translation:** 

**[5073.74s] English:** you know before the age of three months or so or are we born with it and there  
**Translation:** Vocabulary: permanence: 持久性

**[5079.64s] English:** are you know very disagree you know white disagreement among the you know a  
**Translation:** 

**[5083.44s] English:** cognitive scientist for this I think those things are actually very simple to  
**Translation:** 

**[5088.12s] English:** learn you know is it the case that the oriented edge detectors in v1 are  
**Translation:** 

**[5094.30s] English:** learned or are they hardwired I think they are learned they might be learned  
**Translation:** Vocabulary: detectors: 检测器; oriented: 定向的

**[5097.84s] English:** before both because it's really  
**Translation:** 

**[5099.14s] English:** easy to generate signals from the retina that actually will train edge detectors  
**Translation:** 

**[5102.96s] English:** so and again those are things that can be learned within minutes of opening your  
**Translation:** 

**[5108.98s] English:** eyes right I mean you know since the 1990s we have algorithms that can learn  
**Translation:** 

**[5114.40s] English:** oriented edge detectors completely unsupervised with the equivalent of a  
**Translation:** 

**[5118.10s] English:** few minutes of real time so so those things have to be learned there's also  
**Translation:** Vocabulary: unsupervised: 无人监督

**[5123.08s] English:** those you know MIT experiments where you kind of plug the optical nerve on the  
**Translation:** 

**[5129.14s] English:** baby ferret right and that or the toy cortex become visual cortex  
**Translation:** Vocabulary: cortex: 皮层; ferret: 水貂

**[5132.16s] English:** essentially so you know clearly there's running taking place there so you know I  
**Translation:** 

**[5138.68s] English:** think a lot of what people think are so basic that they need to be hardwired I  
**Translation:** 

**[5142.64s] English:** think a lot of those things are learned because they are easy to run Jesus so  
**Translation:** 

**[5146.38s] English:** you put a lot of value in the power of learning what kind of things do you  
**Translation:** 

**[5150.90s] English:** suspect might not be learned is there something that could not be learned so  
**Translation:** 

**[5156.18s] English:** your intrinsic drives are not learned they're not learned they're not learned  
**Translation:** Vocabulary: intrinsic: 内在的

**[5157.02s] English:** there's something that could not be learned so your intrinsic drives are not learned  
**Translation:** 

**[5159.14s] English:** they're  
**Translation:** 

**[5160.00s] English:** are the things that you know make humans uh human or make you know cats different from dogs right  
**Translation:** 

**[5167.28s] English:** it's the the basic drives that are kind of hardwired in our basal ganglia um i mean there  
**Translation:** Vocabulary: basal: 底部的; ganglia: 神经节

**[5173.12s] English:** are people who are working on on this kind of stuff that's called intrinsic motivation in the  
**Translation:** 

**[5176.32s] English:** context of reinforcement learning so these are objective functions where the reward doesn't  
**Translation:** Vocabulary: reinforcement: 强化

**[5180.80s] English:** come from the external world it's computed by your own brain your own brain computes  
**Translation:** 

**[5185.44s] English:** whether you're happy or not right it measures your degree of uh comfort or in comfort uh and and  
**Translation:** Vocabulary: computed: 计算得出; computes: 计算得出

**[5194.48s] English:** because it's your brain computing this presumably knows also how to estimate gradients of this right  
**Translation:** 

**[5198.64s] English:** so um so it's easier to to learn when your objective is is intrinsic um so that has to  
**Translation:** Vocabulary: computing: 计算; gradients: 梯度; presumably: 大概

**[5207.84s] English:** be hardwired uh the critic that makes long-term prediction of the outcome which is the eventual  
**Translation:** 

**[5214.80s] English:** result of this  
**Translation:** Vocabulary: eventual: 最终的; hardwired: 固有的

**[5215.44s] English:** is that's learned uh and perception is learned and your model of the world is learned but let  
**Translation:** 

**[5221.28s] English:** me take take an example of you know why the critic i mean example of how the critic may be learned  
**Translation:** 

**[5226.00s] English:** right if i uh if i come to you um you know i reach across the table and i pinch your arm right  
**Translation:** 

**[5233.20s] English:** complete surprise for you you would not have expected this i was expecting that the hotel but  
**Translation:** Vocabulary: pinch: 捏一下

**[5237.36s] English:** yes right let's say for the sake of the story yes um okay your basal ganglia is gonna light up because  
**Translation:** 

**[5245.44s] English:** it's gonna hurt right um and now your model of the world includes the fact that  
**Translation:** 

**[5250.96s] English:** i may pinch you if i approach my uh my uh don't trust humans right my hand to your arm so  
**Translation:** 

**[5258.24s] English:** if i try again you're gonna recoil and that's your critic  
**Translation:** 

**[5262.00s] English:** uh your predictive you know your predictor of your uh ultimate pain uh uh system that predicts  
**Translation:** 

**[5271.04s] English:** that something bad is gonna happen and you recoil right to avoid it so even that can be learned that  
**Translation:** Vocabulary: predictive: 预测性的; predictor: 预测者

**[5275.44s] English:** is learned definitely this is what allows you also to uh you know define sub goals  
**Translation:** 

**[5280.00s] English:** right so the fact that you know you're a school child you wake up in the morning  
**Translation:** 

**[5285.94s] English:** and you go to school and you know it's not because you necessarily like waking  
**Translation:** 

**[5291.46s] English:** up early and going to school but you know that there is a long-term objective  
**Translation:** 

**[5294.62s] English:** you're trying to optimize so Ernest Becker I'm not sure if you're familiar  
**Translation:** 

**[5297.82s] English:** with the philosopher he wrote the book denial of death and his idea is that one  
**Translation:** Vocabulary: becker: 贝克尔; optimize: 优化

**[5302.36s] English:** of the core motivations of human beings our terror of death our fear of death  
**Translation:** 

**[5306.40s] English:** that's what makes us unique from cats cats are just surviving they do not have  
**Translation:** 

**[5311.46s] English:** a deep under like a cognizance introspection that over the horizon is  
**Translation:** 

**[5320.48s] English:** the end and he says that I mean there's a terror management theory that just all  
**Translation:** Vocabulary: cognizance: 知觉; introspection: 内省

**[5324.96s] English:** these psychological experiments that show basically this idea that all of  
**Translation:** 

**[5331.98s] English:** human civilization everything we create is kind of trying to  
**Translation:** 

**[5336.18s] English:** forget the idea that we are all human beings and that we are all human beings  
**Translation:** 

**[5336.38s] English:** get if even for a brief moment that we're going to die when when do you  
**Translation:** 

**[5341.42s] English:** think humans understand that they're going to die is it learned early on also  
**Translation:** 

**[5347.20s] English:** like I don't know at what point I mean it's a it's a question like you know at  
**Translation:** 

**[5352.98s] English:** what point do you realize that you know what death really is and I think most  
**Translation:** 

**[5357.14s] English:** people don't actually realize what death is right I mean most people believe that  
**Translation:** 

**[5360.26s] English:** you go to heaven or something right so the so to push back on that what Ernest  
**Translation:** 

**[5364.82s] English:** Becker says and  
**Translation:** 

**[5366.16s] English:** um Sheldon Solomon all of those folks and I find those ideas a little bit  
**Translation:** 

**[5370.86s] English:** compelling is that there is moments in life early in life a lot of this fun  
**Translation:** Vocabulary: compelling: 有吸引力的

**[5374.96s] English:** happens early in life when you are when you do deeply experience the terror of  
**Translation:** 

**[5382.26s] English:** this realization and all the things you think about about religion all those  
**Translation:** Vocabulary: realization: 觉悟

**[5386.22s] English:** kinds of things that would kind of think about more like teenage years and later  
**Translation:** 

**[5389.90s] English:** we're talking about way earlier no it's like seven or eight years something like  
**Translation:** 

**[5393.60s] English:** that yeah you realize  
**Translation:** 

**[5395.94s] English:** holy crap this is like the mystery the  
**Translation:** 

**[5400.00s] English:** Like, it's almost like you're a little prey, a little baby deer sitting in the darkness of the jungle, the woods, looking all around you.  
**Translation:** 

**[5408.08s] English:** There's darkness full of terror.  
**Translation:** 

**[5409.60s] English:** I mean, that realization says, okay, I'm going to go back in the comfort of my mind where there is a deep meaning, where there is a maybe like pretend I'm immortal in however way, however kind of idea I can construct to help me understand that I'm immortal.  
**Translation:** 

**[5427.16s] English:** Religion helps with that.  
**Translation:** Vocabulary: immortal: 长生不老

**[5428.36s] English:** You can delude yourself in all kinds of ways, like lose yourself in the busyness of each day, have little goals in mind, all those kinds of things to think that it's going to go on forever.  
**Translation:** 

**[5438.18s] English:** And you kind of know you're going to die, yeah, and it's going to be sad, but you don't really understand that you're going to die.  
**Translation:** Vocabulary: delude: 自我欺骗

**[5445.18s] English:** And so that's their idea.  
**Translation:** 

**[5446.40s] English:** And I find that compelling because it does seem to be a core unique aspect of human nature that we're able to really understand that this life is fine.  
**Translation:** 

**[5458.36s] English:** That seems important.  
**Translation:** 

**[5460.90s] English:** There's a bunch of different things there.  
**Translation:** 

**[5462.30s] English:** So first of all, I don't think there is a qualitative difference between us and cats in the term.  
**Translation:** 

**[5467.42s] English:** I think the difference is that we just have a better long-term ability to predict in the long term.  
**Translation:** Vocabulary: qualitative: 质量上的

**[5474.78s] English:** And so we have a better understanding of other world works.  
**Translation:** 

**[5477.38s] English:** So we have better understanding of finiteness of life and things like that.  
**Translation:** Vocabulary: finiteness: 有限性

**[5481.00s] English:** So we have a better planning engine than cats?  
**Translation:** 

**[5483.50s] English:** Yeah.  
**Translation:** 

**[5484.40s] English:** Okay.  
**Translation:** 

**[5485.52s] English:** What's the motivation for planning?  
**Translation:** 

**[5488.36s] English:** Well, I think it's just a side effect of the fact that we have just a better planning engine because it makes us, as I said, you know, the essence of intelligence is the ability to predict.  
**Translation:** 

**[5497.44s] English:** And so because we're smarter, as a side effect, we also have this ability to kind of make predictions about our own future existence or lack thereof.  
**Translation:** Vocabulary: thereof: 其结果

**[5508.12s] English:** You say religion helps with that.  
**Translation:** 

**[5510.52s] English:** I think religion hurts, actually.  
**Translation:** 

**[5512.64s] English:** It makes people worry about, like, you know, what's going to happen after their death, etc.  
**Translation:** 

**[5517.10s] English:** If you believe that.  
**Translation:** 

**[5518.36s] English:** You know, you just don't.  
**Translation:** 

**[5520.00s] English:** exists after death like you know it solves completely the problem at least you're saying  
**Translation:** 

**[5523.22s] English:** if you don't believe in god you don't worry about what happens after death yeah i don't know you  
**Translation:** 

**[5528.98s] English:** worry about the about uh you know this life because that's the only one you have i think it's  
**Translation:** 

**[5534.80s] English:** well i don't know i don't know if i were to say what ernest becker says and i would say i agree  
**Translation:** 

**[5538.48s] English:** with him more uh than not is uh you do deeply worry uh if you if you believe there's no god  
**Translation:** Vocabulary: becker: 贝克尔

**[5547.80s] English:** there's still a deep worry like of the mystery of it all like how does that make any sense that  
**Translation:** 

**[5554.06s] English:** it just ends i don't think we can truly understand that this right i mean so much of our life the  
**Translation:** 

**[5561.24s] English:** consciousness the ego is uh invested in this in this being and then science keeps bringing  
**Translation:** 

**[5568.74s] English:** humanity down from its pedestal and that's just another another example of it that's wonderful  
**Translation:** Vocabulary: pedestal: 高台

**[5575.44s] English:** but for us individual humans  
**Translation:** 

**[5577.66s] English:** we don't like to be brought down from a pedestal you're saying like what but see you're fine with  
**Translation:** 

**[5582.86s] English:** it because well so what ernest becker would say is you're fine with it because that's just a more  
**Translation:** 

**[5587.36s] English:** peaceful existence for you but you're not really fine you're hiding from in fact some of the people  
**Translation:** 

**[5591.94s] English:** that experience the deepest trauma uh that earlier in life they often before they seek  
**Translation:** 

**[5598.42s] English:** extensive therapy will say that i'm fine it's like when you talk to people who are truly angry  
**Translation:** Vocabulary: trauma: 创伤

**[5603.30s] English:** how are you doing i'm fine the question is what's going on  
**Translation:** 

**[5607.66s] English:** now i had a near-death experience i had a very bad uh motorbike accident when i was 17. so  
**Translation:** Vocabulary: motorbike: 摩托车

**[5614.86s] English:** but that didn't have any impact on my reflection on that topic so i'm basically just playing a bit  
**Translation:** 

**[5622.14s] English:** of devil's advocate pushing back on wondering is it truly possible to accept death and the  
**Translation:** Vocabulary: advocate: 辩护者

**[5627.98s] English:** flip side that's more interesting i think for ai and robotics is how important is it to have  
**Translation:** 

**[5634.46s] English:** this as one of the suite of motivations is to  
**Translation:** 

**[5637.66s] English:** uh not just  
**Translation:** 

**[5640.00s] English:** avoid falling off the roof or something like that but ponder the the end of the ride  
**Translation:** 

**[5650.08s] English:** if you listen to the stoics it's uh it's a great motivator it adds a sense of urgency so maybe  
**Translation:** 

**[5657.84s] English:** to truly fear death or be cognizant of it might give a deeper meaning and urgency to the moment  
**Translation:** Vocabulary: cognizant: 意识到; motivator: 激励; stoics: 斯多葛; urgency: 紧迫感

**[5666.32s] English:** to live fully maybe i don't disagree with that i mean i think what motivates me here is uh  
**Translation:** 

**[5676.64s] English:** you know knowing more about about human nature i mean i think uh human nature and human intelligence  
**Translation:** Vocabulary: motivates: 激励

**[5681.60s] English:** is a big mystery it's a scientific mystery uh in addition to you know philosophical and  
**Translation:** 

**[5687.84s] English:** etc but you know i'm a true believer in science so um and and and i do have kind of a belief that  
**Translation:** Vocabulary: believer: 信仰者; philosophical: 哲学的

**[5696.32s] English:** for complex systems like like the brain and the mind the the way to understand it is to try to  
**Translation:** 

**[5703.52s] English:** reproduce it with you know artifacts that you build because you know what's essential to it  
**Translation:** Vocabulary: artifacts: 人工制品

**[5708.72s] English:** when you try to build it you know the same way um i've used this analogy before with you i believe  
**Translation:** 

**[5714.24s] English:** the same way we we only started to understand uh aerodynamics when we started building airplanes  
**Translation:** Vocabulary: aerodynamics: 空气动力学

**[5719.20s] English:** and that helped us understand how birds fly you know so i think there's kind of a similar process  
**Translation:** 

**[5725.12s] English:** here where  
**Translation:** 

**[5726.32s] English:** we don't have a theory of a full theory of intelligence but building you know intelligent  
**Translation:** 

**[5731.04s] English:** artifacts will help us perhaps develop some you know underlying theory that uh encompasses not  
**Translation:** Vocabulary: encompasses: 包容

**[5737.12s] English:** just artificial implements but also uh human and biological intelligence in general so you're an  
**Translation:** 

**[5744.08s] English:** interesting person to ask this question about sort of all kinds of different other intelligent  
**Translation:** Vocabulary: implements: 工具

**[5750.00s] English:** entities or intelligences what are your thoughts about kind of like the touring  
**Translation:** 

**[5756.32s] English:** or the chinese room question if we  
**Translation:** 

**[5760.00s] English:** create an AI system that exhibits a lot of properties  
**Translation:** 

**[5764.16s] English:** of intelligence and consciousness,  
**Translation:** Vocabulary: exhibits: 表现

**[5767.56s] English:** how comfortable are you thinking of that entity  
**Translation:** 

**[5770.26s] English:** as intelligent or conscious?  
**Translation:** 

**[5772.64s] English:** So you're trying to build now systems  
**Translation:** 

**[5774.62s] English:** that have intelligence,  
**Translation:** 

**[5775.60s] English:** and there's metrics about their performance,  
**Translation:** 

**[5777.46s] English:** but that metric is external.  
**Translation:** 

**[5782.56s] English:** Okay, so are you okay calling a thing intelligent,  
**Translation:** 

**[5786.48s] English:** or are you going to be like most humans  
**Translation:** 

**[5789.06s] English:** and be once again unhappy to be brought down  
**Translation:** 

**[5792.68s] English:** from a pedestal of consciousness slash intelligence?  
**Translation:** Vocabulary: pedestal: 高台

**[5794.92s] English:** No, I'll be very happy to understand  
**Translation:** 

**[5801.26s] English:** more about human nature, human mind, and human intelligence  
**Translation:** 

**[5805.50s] English:** through the construction of machines  
**Translation:** 

**[5807.20s] English:** that have similar abilities.  
**Translation:** 

**[5810.56s] English:** And if a consequence of this is to bring down humanity  
**Translation:** 

**[5814.50s] English:** one notch down from its already low pedestal,  
**Translation:** Vocabulary: notch: 档次

**[5818.00s] English:** I'm just fine with it.  
**Translation:** 

**[5819.04s] English:** That's just the reality of life.  
**Translation:** 

**[5821.30s] English:** So I'm fine with that.  
**Translation:** 

**[5822.42s] English:** Now, you were asking me about things that,  
**Translation:** 

**[5824.96s] English:** opinions I have that a lot of people may disagree with.  
**Translation:** 

**[5827.88s] English:** I think,  
**Translation:** 

**[5831.62s] English:** if we think about the design  
**Translation:** 

**[5832.72s] English:** of an autonomous intelligence system,  
**Translation:** Vocabulary: autonomous: 自主的

**[5834.20s] English:** so assuming that we are somewhat successful at some level  
**Translation:** 

**[5838.64s] English:** of getting machines to learn models of the world,  
**Translation:** 

**[5840.40s] English:** predictive models of the world,  
**Translation:** 

**[5842.54s] English:** we build intrinsic motivation objective functions  
**Translation:** Vocabulary: intrinsic: 内在的; predictive: 预测性的

**[5845.80s] English:** to drive the behavior of that system.  
**Translation:** 

**[5848.12s] English:** The system also has  
**Translation:** 

**[5849.04s] English:** perception modules that allows it  
**Translation:** 

**[5850.92s] English:** to estimate the state of the world,  
**Translation:** 

**[5852.78s] English:** and then have some way of figuring out  
**Translation:** 

**[5854.60s] English:** the sequence of actions to optimize a particular objective.  
**Translation:** 

**[5859.28s] English:** If it has a critic of the type that I was describing before,  
**Translation:** 

**[5862.70s] English:** the thing that makes you recoil your arm  
**Translation:** 

**[5864.58s] English:** the second time I try to pinch you,  
**Translation:** 

**[5868.56s] English:** intelligent autonomous machine will have emotions.  
**Translation:** Vocabulary: pinch: 捏一下

**[5871.66s] English:** I think emotions are an integral part  
**Translation:** 

**[5874.02s] English:** of autonomous intelligence.  
**Translation:** Vocabulary: integral: 不可或缺的

**[5876.36s] English:** If you have an intelligent system,  
**Translation:** 

**[5878.42s] English:** that is driven.  
**Translation:** 

**[5880.00s] English:** by uh intrinsic motivation by objectives if it has a critic that allows it to predict in advance  
**Translation:** 

**[5887.52s] English:** whether the outcome of a of a situation is going to be good or bad is going to have emotions it's  
**Translation:** 

**[5892.16s] English:** going to have fear yes when it predicts that the outcome is going to is going to be bad  
**Translation:** 

**[5898.08s] English:** and and something to avoid is going to have elation when it predicts it's going to be good  
**Translation:** Vocabulary: elation: 欣喜若狂

**[5901.84s] English:** um if it has drives to relate with humans um you know in some ways the way humans have um you know  
**Translation:** 

**[5912.64s] English:** it's it's gonna be social right and so it's gonna have emotions about attachment and and things of  
**Translation:** 

**[5918.08s] English:** that type so um so i think uh you know the the sort of sci-fi thing where you know you see commander  
**Translation:** 

**[5926.24s] English:** data like having an emotion chip that you can turn off right um i think that's ridiculous so  
**Translation:** 

**[5931.84s] English:** so i mean here's the difficult philosophical social question do you think there will be a time  
**Translation:** 

**[5939.92s] English:** like a civil rights movement for robots where um okay forget the movement but a discussion  
**Translation:** Vocabulary: philosophical: 哲学的

**[5946.48s] English:** like the supreme court that particular kinds of robots you know particular kinds of systems  
**Translation:** 

**[5955.60s] English:** um deserve the same rights as humans because they can suffer just as humans can  
**Translation:** 

**[5962.80s] English:** all those kinds of things well perhaps perhaps not like imagine that humans were  
**Translation:** 

**[5969.20s] English:** that that you could uh you know die and be restored like you know you could be sort of  
**Translation:** 

**[5974.96s] English:** you know be 3d reprinted and you know your brain could be reconstructed in its finest details  
**Translation:** 

**[5980.56s] English:** our ideas of rights will change in that case if you can always just  
**Translation:** Vocabulary: reconstructed: 重建; reprinted: 复制

**[5985.76s] English:** there's always a backup you could always restore maybe like the importance of murder will go down  
**Translation:** 

**[5990.96s] English:** one notch  
**Translation:** Vocabulary: notch: 档次

**[5991.84s] English:** that's right but also the uh your your you know desire to do dangerous things like you know you  
**Translation:** 

**[5999.12s] English:** know doing sky  
**Translation:** 

**[6000.00s] English:** diving or or you know uh or or you know race car driving yeah you know car racing or that kind of  
**Translation:** 

**[6006.96s] English:** stuff you know would probably increase or or you know airplane aerobatics or that kind of stuff  
**Translation:** Vocabulary: aerobatics: 飞机特技

**[6011.76s] English:** right it would be fine to do a lot of those things or explore you know dangerous areas and things  
**Translation:** 

**[6016.96s] English:** like that it would kind of change your relationship so now it's very likely that robots would be like  
**Translation:** 

**[6022.00s] English:** that because you know they'll be based on perhaps technology that is somewhat similar to today's  
**Translation:** 

**[6029.60s] English:** technology and you can you can always have a backup so it's possible i don't know if you like  
**Translation:** 

**[6035.12s] English:** video games but there's a there's a game called diablo and um oh my my sons are huge fans of this  
**Translation:** 

**[6041.84s] English:** yes uh and in fact they made a game that's inspired by it awesome like built a game my three  
**Translation:** Vocabulary: diablo: Diablo游戏

**[6049.68s] English:** sons have a game design studio between them yeah that's awesome they came out with a game they just  
**Translation:** 

**[6054.48s] English:** came out last year no this was last year uh early last year about a year ago that's awesome but so  
**Translation:** 

**[6059.60s] English:** i don't know if you've heard of it but it's a game called diablo there's a something called hardcore  
**Translation:** 

**[6064.40s] English:** mode which if you die there's no you're gone right that's it and so it's possible with ai systems  
**Translation:** 

**[6073.04s] English:** for them to be able to operate successfully and for us to treat them in a certain way because  
**Translation:** 

**[6078.24s] English:** they have to be integrated in human society they have to be able to die no copies allowed in fact  
**Translation:** 

**[6085.04s] English:** copying is illegal it's possible with humans as well like cloning will be illegal even when it's  
**Translation:** 

**[6089.44s] English:** done right so it's possible with humans as well like cloning will be illegal even when it's done  
**Translation:** 

**[6093.52s] English:** right so it's possible with humans as well like cloning will be illegal even when it's done right  
**Translation:** 

**[6096.24s] English:** but then it's what we were talking about with computers that you will be able to copy you right  
**Translation:** 

**[6100.72s] English:** you'll be able to perfectly save pickle the the the mind state and it's possible that that would  
**Translation:** 

**[6108.32s] English:** be illegal because that goes against um that will destroy the motivations of the system okay so  
**Translation:** Vocabulary: motivations: 激励机制

**[6116.32s] English:** let's say you you have a domestic robot okay  
**Translation:** 

**[6119.44s] English:** let's say you you have a domestic robot okay  
**Translation:** 

**[6120.00s] English:** sometime in the future yes and uh the domestic robot you know comes to you kind of somewhat  
**Translation:** 

**[6126.36s] English:** pre-trained you know it can do a bunch of things yes but it has a particular personality that makes  
**Translation:** 

**[6130.82s] English:** it slightly different from the other robots because that makes them more interesting  
**Translation:** 

**[6133.76s] English:** and then because it's you know it's lived with you for five years you've you've grown some  
**Translation:** 

**[6138.96s] English:** attachment to it and vice versa and it's learned a lot about you or maybe it's not a household  
**Translation:** 

**[6145.44s] English:** robot maybe it's uh maybe it's a virtual assistant that lives in your you know augmented reality  
**Translation:** Vocabulary: augmented: 增强

**[6150.40s] English:** glasses or whatever right uh you know the the her movie type thing right um and that system to some  
**Translation:** 

**[6158.64s] English:** extent that the intelligence in that system is a bit like your child or maybe your phd student  
**Translation:** 

**[6165.60s] English:** in the sense that there's a lot of you in that in that machine now right yeah and so if it were  
**Translation:** 

**[6172.24s] English:** a living thing you would do this for free  
**Translation:** 

**[6175.44s] English:** if you want right if it's your child your child can you know then uh live his or her own life and  
**Translation:** 

**[6181.84s] English:** you know the fact that they learn stuff from you doesn't mean that you have any ownership of it  
**Translation:** 

**[6185.76s] English:** right yeah but if it's a robot uh that you've trained perhaps you have some uh intellectual  
**Translation:** 

**[6192.32s] English:** property claim about intellectual property oh i thought you meant like uh permanence value in the  
**Translation:** Vocabulary: permanence: 持久性

**[6198.32s] English:** sense that's part of use in well there's permanence value right so you would lose a lot if that robot  
**Translation:** 

**[6203.68s] English:** were to be destroyed and you you had no background  
**Translation:** 

**[6205.44s] English:** up you would lose a lot you know a lot of investment you know kind of like a  
**Translation:** 

**[6209.36s] English:** uh you know a person dying you know um that that a friend of a friend of you is dying or a co-worker  
**Translation:** 

**[6215.52s] English:** or something like that um but also uh you have like intellectual property rights in the sense  
**Translation:** 

**[6222.80s] English:** that that that system is fine-tuned to your particular existence so that's now a very  
**Translation:** 

**[6228.48s] English:** unique instantiation of that original background model whatever it was that arrived another issue  
**Translation:** 

**[6235.44s] English:** right because now imagine that that robot has its own kind of  
**Translation:** Vocabulary: instantiation: 实例化

**[6240.00s] English:** volition and decides to work on someone else yes or kind of you know thinks life  
**Translation:** 

**[6245.46s] English:** with you is sort of untenable or whatever right now all the other things  
**Translation:** Vocabulary: volition: 意志

**[6250.66s] English:** that that system learned from you you know how can you like you know delete  
**Translation:** 

**[6257.10s] English:** all the personal information that that system knows about you yeah I mean that  
**Translation:** 

**[6260.92s] English:** would be kind of an ethical question like you know can you erase the the mind  
**Translation:** 

**[6264.66s] English:** of a intelligent robot to protect your your privacy yeah you can't do this with  
**Translation:** 

**[6270.60s] English:** humans you can ask them to shut up but that you don't have complete power over  
**Translation:** 

**[6275.28s] English:** them can't erase humans yeah it's the problem the relationships you know that  
**Translation:** Vocabulary: erase: 抹去

**[6279.24s] English:** you break up you can't you can't erase the other human with robots I think it  
**Translation:** 

**[6283.80s] English:** will have to be the same thing with robots that that risk that there has to  
**Translation:** 

**[6288.76s] English:** be some risk to our interactions to truly experience them  
**Translation:** 

**[6294.64s] English:** deeply it feels like so you have to be able to lose your robot friend and that  
**Translation:** 

**[6300.20s] English:** robot friend to go tweeting about how much of an asshole you were but then are  
**Translation:** 

**[6304.90s] English:** you allowed to you know murder the robot to protect your private information  
**Translation:** Vocabulary: asshole: 混蛋; tweeting: 发推特

**[6308.68s] English:** probably decides to leave I have this intuition that for robots with with  
**Translation:** 

**[6313.06s] English:** certain like it's almost like regulation if you declare your robot to be let's  
**Translation:** Vocabulary: intuition: 直觉

**[6319.36s] English:** call it sentient or something like that like this this robot is designed for  
**Translation:** 

**[6323.20s] English:** human interaction then you're not allowed to do that because you're not  
**Translation:** Vocabulary: sentient: 有感知的

**[6324.58s] English:** allowed to these robots it's the same as murdering other humans well but what  
**Translation:** 

**[6328.74s] English:** about you do a backup of the robot did you preserve on the hard drive or the  
**Translation:** 

**[6332.78s] English:** equivalent in the future that might be illegal it's like it's a that higher  
**Translation:** 

**[6335.74s] English:** state piety piracy is illegal it's your own it's your own robot right but I can't  
**Translation:** 

**[6340.38s] English:** you don't but then but then you can wipe out his brain so the this robot doesn't  
**Translation:** 

**[6346.28s] English:** know anything about you anymore but you still have technically is still in  
**Translation:** 

**[6349.90s] English:** existence because you backed it up and then they'll be these great speeches at  
**Translation:** 

**[6353.62s] English:** the Supreme Court by the حضرة  
**Translation:** 

**[6354.58s] English:** saying oh sure you can erase the mind of the robot just like you can erase the mind of a human  
**Translation:** 

**[6360.00s] English:** We both can suffer.  
**Translation:** 

**[6361.08s] English:** There'll be some epic, like, Obama-type character with a speech that we, like, the robots and the humans are the same.  
**Translation:** 

**[6368.52s] English:** We can both suffer.  
**Translation:** 

**[6369.86s] English:** We can both hope.  
**Translation:** 

**[6371.38s] English:** We can both, all of those kinds of things, raise families, all that kind of stuff.  
**Translation:** 

**[6377.70s] English:** It's interesting for these, just like you said, emotion seems to be a fascinatingly powerful aspect of human interaction, human-robot interaction.  
**Translation:** 

**[6386.82s] English:** And if they're able to exhibit emotions, at the end of the day, that's probably going to have us deeply consider human rights, like what we value in humans, what we value in other animals.  
**Translation:** Vocabulary: fascinatingly: 非常迷人地

**[6400.28s] English:** That's why robots and AI is great.  
**Translation:** 

**[6402.18s] English:** It makes us ask really good questions.  
**Translation:** 

**[6404.30s] English:** Ask the hard questions, yeah.  
**Translation:** 

**[6405.44s] English:** But you asked about the Chinese room-type argument, you know, is it real, if it looks real?  
**Translation:** 

**[6410.94s] English:** Yeah.  
**Translation:** 

**[6411.42s] English:** I think the Chinese room argument is a ridiculous one.  
**Translation:** 

**[6414.82s] English:** So for people who don't know, Chinese room.  
**Translation:** 

**[6416.82s] English:** Chinese room is, you can, I don't even know how to formulate it well.  
**Translation:** 

**[6420.76s] English:** But basically, you can mimic the behavior of an intelligent system by just following a giant algorithm codebook that tells you exactly how to respond in exactly each case.  
**Translation:** 

**[6432.90s] English:** But is that really intelligent?  
**Translation:** Vocabulary: algorithm: 算法; codebook: 代码手册

**[6434.66s] English:** It's like a giant look-up table.  
**Translation:** 

**[6436.50s] English:** When this person says this, you answer this.  
**Translation:** 

**[6438.58s] English:** When this person says this, you answer this.  
**Translation:** 

**[6442.04s] English:** And if you understand how that works, you have this giant, nearly infinite look-up table.  
**Translation:** 

**[6447.06s] English:** Is that really intelligence?  
**Translation:** 

**[6448.60s] English:** Because intelligence seems to be a mechanism that's much more interesting and complex than this look-up table.  
**Translation:** 

**[6454.58s] English:** I don't think so.  
**Translation:** 

**[6455.16s] English:** So, I mean, the real question comes down to, do you think, you know, you can mechanize intelligence in some way, even if that involves learning?  
**Translation:** 

**[6467.20s] English:** And the answer is, of course, yes.  
**Translation:** 

**[6469.24s] English:** There's no question.  
**Translation:** 

**[6470.68s] English:** There's a second question then, which is, assuming you can reproduce intelligence.  
**Translation:** 

**[6476.82s] English:** And sort of different hardware than biological hardware, you know, like computers.  
**Translation:** 

**[6480.00s] English:** others, can you match human intelligence in all the domains in which humans are intelligent?  
**Translation:** 

**[6493.04s] English:** Is it possible, right?  
**Translation:** 

**[6494.04s] English:** So that's the hypothesis of strong AI.  
**Translation:** 

**[6497.12s] English:** The answer to this, in my opinion, is an unqualified yes, this will as well happen at some point.  
**Translation:** Vocabulary: hypothesis: 假设; unqualified: 无保留的

**[6502.44s] English:** There's no question that machines at some point will become more intelligent than humans  
**Translation:** 

**[6506.52s] English:** in all domains where humans are intelligent.  
**Translation:** 

**[6508.68s] English:** This is not for tomorrow, it's going to take a long time, regardless of what Elon and others  
**Translation:** 

**[6515.74s] English:** have claimed or believed.  
**Translation:** 

**[6518.26s] English:** This is a lot harder than many of those guys think it is, and many of those guys who thought  
**Translation:** 

**[6524.60s] English:** it was simpler than that five years ago now think it's hard because it's been five years  
**Translation:** 

**[6529.78s] English:** and they realize it's going to take a lot longer.  
**Translation:** 

**[6533.52s] English:** That includes a bunch of people at DeepMind, for example, but-  
**Translation:** 

**[6535.36s] English:** Oh, interesting.  
**Translation:** 

**[6536.36s] English:** I haven't actually touched base with the DeepMind.  
**Translation:** 

**[6538.66s] English:** DeepMind folks, but some of it, Elon or Demis Hassabis, I mean, sometimes in your role,  
**Translation:** 

**[6545.88s] English:** you have to kind of create deadlines that are nearer than farther away to kind of create  
**Translation:** Vocabulary: deadlines: 截止日期; hassabis: 哈萨斯

**[6551.58s] English:** an urgency because you have to believe the impossible is possible in order to accomplish  
**Translation:** 

**[6556.12s] English:** it.  
**Translation:** Vocabulary: urgency: 急迫感

**[6557.12s] English:** And there's, of course, a flip side to that coin, but it's a weird, you can't be too cynical  
**Translation:** 

**[6561.20s] English:** if you want to get something done.  
**Translation:** Vocabulary: cynical: 怀疑一切

**[6562.60s] English:** Absolutely.  
**Translation:** 

**[6563.60s] English:** I agree with that.  
**Translation:** 

**[6564.60s] English:** But I mean, you have to inspire people to work on sort of ambitious things.  
**Translation:** 

**[6568.66s] English:** So, you know, it's certainly a lot harder than we believe, but there's no question  
**Translation:** 

**[6576.16s] English:** in my mind that this will happen.  
**Translation:** 

**[6578.28s] English:** And now, you know, people are kind of worried about what does that mean for humans.  
**Translation:** 

**[6582.98s] English:** They are going to be brought down from their pedestal, you know, a bunch of notches with  
**Translation:** 

**[6587.82s] English:** that.  
**Translation:** Vocabulary: notches: 刻度; pedestal: 高台

**[6588.82s] English:** And, you know, is that going to be good or bad?  
**Translation:** 

**[6591.66s] English:** I mean, it's just going to give more power, right?  
**Translation:** 

**[6593.56s] English:** It's an amplifier for human intelligence, really.  
**Translation:** 

**[6595.92s] English:** So, speaking of doing cool, ambitious things.  
**Translation:** Vocabulary: amplifier: 增强器

**[6598.32s] English:** Fair enough.  
**Translation:** 

**[6599.32s] English:** Thank you.  
**Translation:** 

**[6600.00s] English:** FAIR, the Facebook AI research group, has recently celebrated its eighth birthday.  
**Translation:** 

**[6605.58s] English:** Or maybe you can correct me on that.  
**Translation:** 

**[6608.36s] English:** Looking back, what has been the successes, the failures, the lessons learned from the eight years of FAIR?  
**Translation:** 

**[6614.40s] English:** And maybe you can also give context of where does the newly minted Meta AI fit into how does it relate to FAIR?  
**Translation:** 

**[6622.60s] English:** Right. So let me tell you a little bit about the organization of all this.  
**Translation:** 

**[6625.02s] English:** Yes. Yeah, FAIR was created almost exactly eight years ago.  
**Translation:** 

**[6630.04s] English:** It wasn't called FAIR yet. It took that name a few months later.  
**Translation:** 

**[6634.58s] English:** And at the time I joined Facebook, there was a group called the AI group that had about 12 engineers and a few scientists, like, you know, 10 engineers and two scientists or something like that.  
**Translation:** 

**[6646.86s] English:** I ran it for three and a half years as a director.  
**Translation:** 

**[6650.28s] English:** You know, hired the first few scientists and kind of set up the culture and organized it.  
**Translation:** 

**[6655.02s] English:** You know, explained to the Facebook leadership what fundamental research was about and how it can work within industry and how it needs to be open and everything.  
**Translation:** 

**[6667.24s] English:** And I think it's been an unqualified success in the sense that FAIR has simultaneously produced, you know, top level research and advanced the science and the technology, provided tools, open source tools like PyTorch and many others.  
**Translation:** Vocabulary: unqualified: 无保留的

**[6685.02s] English:** But at the same time, has had a direct or mostly indirect impact on Facebook at the time, now Meta, in the sense that a lot of systems that are that Meta is built around now are based on research projects that started at FAIR.  
**Translation:** 

**[6707.96s] English:** So if you were to take out, you know, deep learning out of Facebook services now and Meta more generally.  
**Translation:** 

**[6715.02s] English:** I mean, the company would literally crumble.  
**Translation:** 

**[6717.74s] English:** I mean, it's completely built around.  
**Translation:** Vocabulary: crumble: 瓦解

**[6720.00s] English:** around AI these days.  
**Translation:** 

**[6721.48s] English:** And it's really essential to the operations.  
**Translation:** 

**[6724.00s] English:** So what happened after three and a half years  
**Translation:** 

**[6726.64s] English:** is that I changed role, I became chief scientist.  
**Translation:** 

**[6730.22s] English:** So I'm not doing day-to-day management of FAIR anymore.  
**Translation:** 

**[6734.90s] English:** I'm more of a kind of, you know,  
**Translation:** 

**[6737.12s] English:** think about strategy and things like that.  
**Translation:** 

**[6738.88s] English:** And I carry my, I conduct my own research.  
**Translation:** 

**[6741.46s] English:** I've, you know, my own kind of research group  
**Translation:** 

**[6743.34s] English:** working on self-supervised learning and things like this,  
**Translation:** 

**[6745.32s] English:** which I didn't have time to do when I was director.  
**Translation:** 

**[6748.24s] English:** So now FAIR is run by Joël Pinot and Antoine Borde,  
**Translation:** Vocabulary: antoine: 波德; pinot: 皮诺

**[6754.20s] English:** together, because FAIR is kind of split in two now.  
**Translation:** 

**[6756.34s] English:** There's something called FAIR Labs,  
**Translation:** 

**[6757.86s] English:** which is sort of bottom-up, science-driven research,  
**Translation:** 

**[6760.94s] English:** and FAIR Excel, which is slightly more organized  
**Translation:** 

**[6763.48s] English:** for bigger projects that require a little more kind of focus  
**Translation:** 

**[6767.68s] English:** and more engineering support and things like that.  
**Translation:** 

**[6769.78s] English:** So Joël leads FAIR Lab and Antoine Borde leads FAIR Excel.  
**Translation:** 

**[6772.88s] English:** Where are they located?  
**Translation:** 

**[6774.68s] English:** All over?  
**Translation:** 

**[6775.52s] English:** It's delocalized all over.  
**Translation:** Vocabulary: delocalized: 分散化

**[6776.60s] English:** Okay.  
**Translation:** 

**[6777.98s] English:** So there's no question that the leadership of the company  
**Translation:** 

**[6782.54s] English:** believes that this was a very worthwhile investment.  
**Translation:** 

**[6786.56s] English:** And what that means is that it's there for the long run, right?  
**Translation:** 

**[6793.08s] English:** So there is, if you want to talk in these terms,  
**Translation:** 

**[6796.80s] English:** which I don't like, there's a business model, if you want,  
**Translation:** 

**[6799.56s] English:** where FAIR, despite being a very fundamental research lab,  
**Translation:** 

**[6803.60s] English:** brings a lot of value to the company,  
**Translation:** 

**[6805.30s] English:** either mostly indirectly through other groups.  
**Translation:** 

**[6807.98s] English:** Mm-hmm.  
**Translation:** 

**[6809.88s] English:** Now, what happened three and a half years ago  
**Translation:** 

**[6811.56s] English:** when I stepped down was also the creation of Facebook AI,  
**Translation:** 

**[6814.60s] English:** which was basically a larger organization  
**Translation:** 

**[6817.68s] English:** that covers FAIR, so FAIR is included in it,  
**Translation:** 

**[6821.70s] English:** but also has other organizations that are focused  
**Translation:** 

**[6826.26s] English:** on applied research or advanced development of AI technology  
**Translation:** 

**[6831.22s] English:** that is more focused on the products of the company.  
**Translation:** 

**[6834.68s] English:** So less emphasis on fundamental research.  
**Translation:** 

**[6836.66s] English:** Less fundamental.  
**Translation:** 

**[6837.50s] English:** There's still research.  
**Translation:** 

**[6838.34s] English:** I mean, there's a lot of papers coming out of those  
**Translation:** 

**[6840.00s] English:** organizations and people are awesome and wonderful to interact with, but it serves as a way to  
**Translation:** 

**[6851.82s] English:** scale up, if you want, AI technology, which may be very experimental and sort of lab prototypes  
**Translation:** 

**[6859.34s] English:** into things that are usable.  
**Translation:** Vocabulary: prototypes: 样品; usable: 可用的

**[6860.34s] English:** So FAIR is a subset of Meta AI.  
**Translation:** 

**[6863.16s] English:** Is FAIR become like KFC, it'll just keep the F, nobody cares what the F stands for?  
**Translation:** 

**[6868.80s] English:** We'll know soon enough, probably by the end of 2021.  
**Translation:** 

**[6874.56s] English:** I mean, this is not a giant change, MAIR, FAIR.  
**Translation:** 

**[6877.98s] English:** Well, MAIR doesn't sound too good, but the brand people are kind of deciding on  
**Translation:** 

**[6882.74s] English:** this and they've been hesitating for a while now and they tell us they're going to come  
**Translation:** Vocabulary: hesitating: 犹豫不决

**[6887.50s] English:** up with an answer as to whether FAIR is going to change name or whether we're going to change  
**Translation:** 

**[6891.30s] English:** just the meaning of the F.  
**Translation:** 

**[6892.30s] English:** Oh, that's a good call.  
**Translation:** 

**[6894.16s] English:** I will keep FAIR and change the meaning of the F.  
**Translation:** 

**[6896.12s] English:** That would be my preference.  
**Translation:** 

**[6897.62s] English:** I would turn the F.  
**Translation:** 

**[6898.62s] English:** Okay.  
**Translation:** 

**[6898.78s] English:** Turn the F into fundamental.  
**Translation:** 

**[6899.78s] English:** Oh, that's good.  
**Translation:** 

**[6900.78s] English:** Fundamental AI research.  
**Translation:** 

**[6901.78s] English:** Oh, that's really good.  
**Translation:** 

**[6902.78s] English:** Yeah, yeah.  
**Translation:** 

**[6903.78s] English:** Within Meta AI.  
**Translation:** 

**[6904.78s] English:** So this would be-  
**Translation:** 

**[6905.78s] English:** Meta FAIR.  
**Translation:** 

**[6906.78s] English:** Meta FAIR.  
**Translation:** 

**[6907.78s] English:** Yeah.  
**Translation:** 

**[6908.78s] English:** But people will call it FAIR, right?  
**Translation:** 

**[6909.78s] English:** Yeah, exactly.  
**Translation:** 

**[6910.78s] English:** I like it.  
**Translation:** 

**[6911.78s] English:** And now Meta AI is part of the Reality Lab.  
**Translation:** 

**[6916.82s] English:** So Meta now, the new Facebook is called Meta and it's kind of divided into Facebook, Instagram,  
**Translation:** 

**[6928.60s] English:** and Twitter.  
**Translation:** 

**[6929.60s] English:** And Reality Lab.  
**Translation:** 

**[6930.60s] English:** And Reality Lab is about AR, VR, telepresence, communication technology, and stuff like that.  
**Translation:** 

**[6940.60s] English:** It's kind of the...  
**Translation:** Vocabulary: telepresence: 远程存在感

**[6941.60s] English:** You can think of it as the sort of a combination of sort of new products and technology part  
**Translation:** 

**[6949.60s] English:** of Meta.  
**Translation:** 

**[6950.60s] English:** Is that where the touch sensing for robots I saw that you were posting about, that's...  
**Translation:** 

**[6955.60s] English:** But touch sensing for robots is part of FAIR, actually.  
**Translation:** 

**[6957.60s] English:** Oh, it is?  
**Translation:** 

**[6958.60s] English:** Okay, cool.  
**Translation:** 

**[6959.60s] English:** Yeah.  
**Translation:** 

**[6960.00s] English:** No, but there is the other way, the haptic glove, right?  
**Translation:** Vocabulary: haptic: 触觉的

**[6965.72s] English:** Yes, that's more Reality Lab.  
**Translation:** 

**[6967.64s] English:** That's Reality Lab research.  
**Translation:** 

**[6970.64s] English:** Reality Lab research.  
**Translation:** 

**[6971.76s] English:** By the way, the touch sensors are super interesting.  
**Translation:** 

**[6974.42s] English:** Like integrating that modality into the whole sensing suite is very interesting.  
**Translation:** 

**[6980.24s] English:** So what do you think about the metaverse?  
**Translation:** Vocabulary: integrating: 整合; metaverse: 元宇宙; modality: 模态

**[6983.58s] English:** What do you think about this whole kind of expansion of the view of the role of Facebook and meta in the world?  
**Translation:** 

**[6990.94s] English:** Well, metaverse really should be thought of as the next step in the Internet, right?  
**Translation:** 

**[6995.36s] English:** Sort of trying to kind of, you know, make the experience more compelling of, you know, being connected either with other people or with content.  
**Translation:** 

**[7009.18s] English:** And, you know, we are evolved and trained to...  
**Translation:** Vocabulary: compelling: 有吸引力的

**[7013.58s] English:** Evolve in, you know, 3D environments where, you know, we can see other people, we can talk to them when we're near them or, you know, an other viewer far away can't hear us, you know, things like that, right?  
**Translation:** 

**[7025.04s] English:** So there's a lot of social conventions that exist in the real world that we can try to transpose.  
**Translation:** Vocabulary: conventions: 社会规范; environments: 环境; transpose: 转移

**[7030.84s] English:** Now, what is going to be eventually the...  
**Translation:** 

**[7035.02s] English:** How compelling is it going to be?  
**Translation:** 

**[7036.18s] English:** Like, you know, is it going to be the case that people are going to be willing to do this if they have to wear, you know, a huge pair of goggles?  
**Translation:** 

**[7043.58s] English:** Well, all day, maybe not.  
**Translation:** Vocabulary: goggles: 护目镜

**[7046.40s] English:** But then again, if the experience is sufficiently compelling, maybe so.  
**Translation:** 

**[7050.28s] English:** Or if the device that you have to wear is just basically a pair of glasses, you know, and technology makes sufficient progress for that.  
**Translation:** Vocabulary: sufficiently: 足够地

**[7057.80s] English:** You know, AR is a much easier concept to grasp that you're going to have, you know, augmented reality glasses that basically contain some sort of, you know, virtual assistant that can help you in your daily lives.  
**Translation:** 

**[7070.36s] English:** But at the same time with AR, you have to contend with reality.  
**Translation:** Vocabulary: augmented: 增强; contend: 应对

**[7073.58s] English:** With VR, you can completely detach yourself from reality, so it gives you freedom.  
**Translation:** 

**[7077.20s] English:** It might be easier to design worlds in VR.  
**Translation:** 

**[7080.00s] English:** Yeah, but you can imagine, you know, the metaverse being a mix, right?  
**Translation:** 

**[7086.54s] English:** Or like you can have objects that exist in the metaverse that, you know, pop up on top of the real world or only exist in virtual reality.  
**Translation:** 

**[7094.10s] English:** Okay, let me ask the hard question.  
**Translation:** 

**[7097.00s] English:** Because all of this was easy.  
**Translation:** 

**[7098.24s] English:** This was easy.  
**Translation:** 

**[7099.16s] English:** Okay, the Facebook, now Meta, the social network has been painted by the media as net negative for society, even destructive and evil at times.  
**Translation:** 

**[7110.60s] English:** You've pushed back against this, defending Facebook.  
**Translation:** 

**[7114.02s] English:** Can you explain your defense?  
**Translation:** 

**[7116.58s] English:** Yeah, so the description, the company that is being described in some media is not the company we know when we work inside.  
**Translation:** 

**[7127.02s] English:** And, you know…  
**Translation:** 

**[7129.16s] English:** It could be claimed that a lot of employees are uninformed about what really goes on in the company.  
**Translation:** 

**[7134.60s] English:** But, you know, I'm a vice president.  
**Translation:** Vocabulary: uninformed: 信息不足

**[7136.30s] English:** I mean, I have a pretty good vision of what goes on.  
**Translation:** 

**[7138.70s] English:** You know, I don't know everything, obviously.  
**Translation:** 

**[7140.20s] English:** I'm not involved in everything, but certainly not in decision about, like, you know, content moderation or anything like this.  
**Translation:** 

**[7146.04s] English:** But I have some decent vision of what goes on.  
**Translation:** Vocabulary: moderation: 调节

**[7150.20s] English:** And this evil that is being described, I just don't see it.  
**Translation:** 

**[7153.70s] English:** And then, you know, I think there is an easy story to buy, which is…  
**Translation:** 

**[7159.16s] English:** that, you know, all the bad things in the world and, you know, the reason your friend believe crazy stuff, you know, there's an easy scapegoat, right?  
**Translation:** 

**[7168.42s] English:** In social media in general, Facebook in particular.  
**Translation:** Vocabulary: scapegoat: 替罪羊

**[7174.46s] English:** We have to look at the data.  
**Translation:** 

**[7175.48s] English:** Like, is it the case that Facebook, for example, polarizes people politically?  
**Translation:** Vocabulary: polarizes: 分化; politically: 政治地

**[7182.70s] English:** Are there academic studies that show this?  
**Translation:** 

**[7185.20s] English:** Is it the case that, you know, teenagers think that Facebook is a good thing?  
**Translation:** 

**[7188.28s] English:** Yeah, I think so.  
**Translation:** 

**[7189.00s] English:** They think of themselves less if they use Instagram more.  
**Translation:** 

**[7192.12s] English:** Is it the case that, you know, people get more riled up against, you know, opposite sides?  
**Translation:** 

**[7200.00s] English:** a in a debate or political opinion if they if they are more on facebook or if they are less  
**Translation:** Vocabulary: riled: 激怒

**[7205.60s] English:** and uh study after study show that none of this is true this is independent studies by  
**Translation:** 

**[7211.84s] English:** academic they're not funded by facebook or meta um you know studied by stanford by some of my  
**Translation:** 

**[7217.36s] English:** colleagues at nyu actually with whom i have no connection um you know there's a study recently  
**Translation:** 

**[7222.48s] English:** they they paid people i think it was in um in in former yugoslavia i'm not exactly sure in what  
**Translation:** Vocabulary: yugoslavia: 南斯拉夫

**[7231.12s] English:** what part but they paid people to not use facebook for a while in the period  
**Translation:** 

**[7238.56s] English:** before the anniversary of the srebrenica massacres right so you know people get riled up like should  
**Translation:** Vocabulary: massacres: 大规模屠杀; srebrenica: 斯雷布雷尼察

**[7245.20s] English:** you know should we have a celebration i mean a memorial kind of celebration for it or not  
**Translation:** 

**[7250.88s] English:** so they paid a bunch of people  
**Translation:** 

**[7252.48s] English:** to not use facebook for a few weeks it turns out that those people ended up being more  
**Translation:** 

**[7260.24s] English:** polarized than they were at the beginning and the people who were more on facebook were less  
**Translation:** Vocabulary: polarized: 立场极端化

**[7264.00s] English:** polarized um there's a study you know from stanford of uh economists at stanford that  
**Translation:** 

**[7271.20s] English:** tried to identify the causes of uh increasing polarization in the us  
**Translation:** Vocabulary: economists: 经济学家; polarization: 极化

**[7275.92s] English:** and it's been going on for 40 years before you know mark zuckerberg was born yeah uh continuously  
**Translation:** 

**[7282.48s] English:** and um and uh so if there is a cause it's not facebook or social media so you could say if  
**Translation:** 

**[7288.08s] English:** social media just accelerated but no i mean it's basically a continuous uh evolution by some measure  
**Translation:** 

**[7293.68s] English:** of polarization in the us and then you compare this with other countries like uh uh the the the  
**Translation:** Vocabulary: accelerated: 加速

**[7300.08s] English:** west half of germany because you can go 40 years in the east east side or denmark or or other  
**Translation:** 

**[7306.08s] English:** countries uh and they use facebook just as much and they're not getting more polarized they're  
**Translation:** 

**[7310.56s] English:** are getting less polarized. So if you want to look for a causal relationship there,  
**Translation:** 

**[7317.52s] English:** you can find a scapegoat, but you can't find a cause.  
**Translation:** Vocabulary: scapegoat: 替罪羊

**[7320.00s] English:** you want to fix the problem you have to find the right cause and what rise me up is that people now  
**Translation:** 

**[7325.44s] English:** are accusing facebook of bad deeds that are done by others and those others are we're not doing  
**Translation:** 

**[7330.64s] English:** anything about them and by the way those others include uh the owner of the wall street journal  
**Translation:** 

**[7335.52s] English:** in which all of those papers were published so i should mention that i'm talking to shrep mike  
**Translation:** 

**[7340.48s] English:** shrep for on this podcast and also mark zuckerberg and probably these conversations can have with  
**Translation:** 

**[7344.96s] English:** them uh because it's very interesting to me even if facebook has some measurable negative effect  
**Translation:** Vocabulary: measurable: 可测量的; zuckerberg: 扎克伯格

**[7351.76s] English:** you can't just consider that in isolation you have to consider about all the positive ways it  
**Translation:** 

**[7356.16s] English:** connects us so like every technology people it's a question you can't just say like uh there's an  
**Translation:** 

**[7362.16s] English:** increase in division yes probably google search engine has created increase in division we have  
**Translation:** 

**[7368.00s] English:** to consider about how much information are brought to the world like i'm sure wikipedia created more  
**Translation:** 

**[7373.04s] English:** division if you just look at the division  
**Translation:** 

**[7374.96s] English:** and we have to look at the full context of the world and they didn't make a better world  
**Translation:** 

**[7379.52s] English:** the printing press has created more difference right exactly i mean  
**Translation:** 

**[7382.96s] English:** so you know when the printing press was invented uh the first books that were that were printed  
**Translation:** 

**[7389.20s] English:** were things like the bible and that allowed people to read the bible by themselves not get the  
**Translation:** 

**[7394.08s] English:** message uniquely from priests in europe and that created you know the protestant movement and 200  
**Translation:** Vocabulary: uniquely: 独有地

**[7401.20s] English:** years of religious persecution and wars so that's a bad side effect  
**Translation:** 

**[7404.96s] English:** of the printing press you know social networks aren't being nearly as bad  
**Translation:** Vocabulary: persecution: 迫害

**[7408.32s] English:** as the printing press but nobody would say the printing press was a bad idea  
**Translation:** 

**[7413.44s] English:** yeah a lot of this perception and there's a lot of different incentives operating here  
**Translation:** Vocabulary: incentives: 激励因素

**[7418.48s] English:** maybe a quick comment since you're one of the top leaders at facebook and in at meta sorry  
**Translation:** 

**[7424.32s] English:** that's in the tech space i'm sure facebook involves a lot of incredible technological  
**Translation:** 

**[7431.36s] English:** challenges that need to be solved a lot of it probably is on the computer infrastructure and  
**Translation:** 

**[7434.96s] English:** the hardware the I mean it's just a huge amount maybe can you give me a call  
**Translation:** 

**[7440.00s] English:** context about how much of Shrepp's life is AI and how much of it is low-level compute,  
**Translation:** 

**[7446.32s] English:** how much of it is flying all around doing business stuff, and the same with Mark Zuckerberg?  
**Translation:** 

**[7452.16s] English:** They really focus on AI. Certainly, in the run-up of the Creation Affair and for at least  
**Translation:** 

**[7461.72s] English:** a year after that, if not more, Mark was very, very much focused on AI and was spending quite  
**Translation:** 

**[7467.68s] English:** a lot of effort on it, and that's his style. When he gets interested in something, he reads  
**Translation:** 

**[7472.34s] English:** everything about it. He read some of my papers, for example, before I joined. He learned a  
**Translation:** 

**[7481.36s] English:** lot about it.  
**Translation:** 

**[7482.36s] English:** That'd be great if he sent you notes.  
**Translation:** 

**[7487.98s] English:** Shrepp was really into it also. Shrepp has something I've tried to preserve  
**Translation:** 

**[7497.56s] English:** all along.  
**Translation:** 

**[7497.68s] English:** also, despite my not-so-young age, which is a sense of wonder about science and technology,  
**Translation:** 

**[7503.28s] English:** and he certainly has that. He's also a wonderful person in terms of, as a manager, dealing  
**Translation:** 

**[7510.86s] English:** with people and everything. Marc also, actually. They're very human people. In the case of  
**Translation:** 

**[7518.48s] English:** Marc, it's shockingly human, given his trajectory. I mean, the personality of him that is painted  
**Translation:** Vocabulary: shockingly: 惊人地; trajectory: 轨迹

**[7527.60s] English:** in the press is just completely wrong.  
**Translation:** 

**[7529.56s] English:** Yeah. But you have to know how to play the press. I put some of that responsibility  
**Translation:** 

**[7534.92s] English:** on him, too. It's like the conductor of an orchestra. You have to play the press and  
**Translation:** 

**[7545.60s] English:** the public in a certain kind of way where you convey  
**Translation:** Vocabulary: conductor: 指挥家

**[7548.46s] English:** your true self to them, if there's a depth of kindness to you.  
**Translation:** 

**[7551.46s] English:** It's hard. And he's probably not the best at it. So, yeah.  
**Translation:** 

**[7555.22s] English:** You have to learn. And it's sad to see... I'll talk to him.  
**Translation:** 

**[7560.00s] English:** about it but the strep is slowly stepping down it's always uh sad to see folks sort of be there  
**Translation:** Vocabulary: strep: 链球菌

**[7567.44s] English:** for a long time and slowly i guess time you know i think he's i think he's done the thing he  
**Translation:** 

**[7573.84s] English:** set out to do and you know he's he's got you know uh family priorities and stuff like that and  
**Translation:** Vocabulary: priorities: 优先事项

**[7582.16s] English:** um i understand you know after 13 years or something it's been a good run which in silicon  
**Translation:** 

**[7589.68s] English:** valley is basically a lifetime yeah you know because you know it's dog years so uh in europe's  
**Translation:** 

**[7596.00s] English:** the conference just wrapped up uh let me just go back to something else you posted the paper you  
**Translation:** 

**[7601.76s] English:** co-authored was rejected from europe's as you said proudly in quotes rejected can you joke yeah i  
**Translation:** 

**[7609.20s] English:** know uh can you describe this paper and like what was the idea in it and also maybe this is a good  
**Translation:** 

**[7619.68s] English:** example of what was the idea in it and what are the pros and cons what works and what doesn't about  
**Translation:** 

**[7624.80s] English:** the review process yeah let me talk about the paper first i'll talk about the review talk about  
**Translation:** 

**[7629.28s] English:** the review process uh afterwards um the paper is called vicreg so this is i mentioned that before  
**Translation:** 

**[7635.36s] English:** variance invariance covariance regularization and it's a technique a non-contrastive learning  
**Translation:** 

**[7640.64s] English:** technique for what i call joint embedding architecture so sami's nets are an example  
**Translation:** Vocabulary: covariance: 协方差; embedding: 嵌入; invariance: 不变性; variance: 方差

**[7646.16s] English:** of joint embedding architecture so a gentleman in architecture is uh  
**Translation:** 

**[7649.68s] English:** a beginner in architecture so he's an amateur in architecture he's an amateur in the field  
**Translation:** Vocabulary: amateur: 初学者

**[7652.64s] English:** of joint embedding architecture so he's a beginner in architecture so he's a beginner in architecture  
**Translation:** 

**[7656.32s] English:** if you want to do self-supervised learning you can you can do it by prediction  
**Translation:** 

**[7661.28s] English:** so let's say you want to train your system to predict video right you show it a video clip and  
**Translation:** 

**[7666.08s] English:** uh and you train the system to predict the next the continuation of that video clip now because  
**Translation:** Vocabulary: continuation: 后续内容

**[7670.80s] English:** you need to handle uncertainty because there are many you know many continuations that are plausible  
**Translation:** 

**[7676.40s] English:** you need to have you need to handle this in some way you need to have  
**Translation:** Vocabulary: continuations: 后续情况; plausible: 合乎情理的

**[7679.68s] English:** Thanks for watching!  
**Translation:** 

**[7680.00s] English:** And the way, the only way I know to do this is through what's called a latent variable.  
**Translation:** 

**[7685.44s] English:** So you have some sort of hidden vector of a variable that you can vary over a set or draw from a distribution.  
**Translation:** 

**[7692.56s] English:** And as you vary this vector over a set, the output, the prediction varies over a set of plausible predictions.  
**Translation:** 

**[7698.48s] English:** Okay, so that's called, I call this a generative latent variable model.  
**Translation:** 

**[7703.88s] English:** Got it.  
**Translation:** Vocabulary: generative: 生成模型

**[7704.74s] English:** Okay.  
**Translation:** 

**[7705.24s] English:** Now there is an alternative to this to handle uncertainty.  
**Translation:** 

**[7707.86s] English:** And instead of directly predicting the next frames of the clip, you also run those through another neural net.  
**Translation:** 

**[7720.54s] English:** So you now have two neural nets, one that looks at the, you know, the initial segment of the video clip.  
**Translation:** Vocabulary: neural: 神经网络

**[7728.56s] English:** And another one that looks at the continuation during training, right?  
**Translation:** 

**[7733.24s] English:** And what you're trying to do is learn a representation of.  
**Translation:** 

**[7737.86s] English:** Those two video clips that is maximally informative about the video clips themselves, but it's such that you can predict the representation of the second video clip from the representation of the first one easily.  
**Translation:** 

**[7751.24s] English:** Okay.  
**Translation:** Vocabulary: maximally: 最大程度上

**[7752.26s] English:** And you can sort of formalize this in terms of maximizing mutual information and some stuff like that, but it doesn't matter.  
**Translation:** 

**[7757.36s] English:** Uh, what you want is, uh, informative, representative represent, you know, informative representations of the two video clips that are mutually predictable.  
**Translation:** Vocabulary: maximizing: 最大化; predictable: 可预测的

**[7767.86s] English:** Uh, but that means is that there's a lot of details in the second video clips that are irrelevant.  
**Translation:** 

**[7773.50s] English:** Uh, you know, um, I, let's say a video clip consists in, you know, a camera panning the scene.  
**Translation:** Vocabulary: irrelevant: 无关紧要

**[7781.72s] English:** Uh, there's going to be a piece of that room that is going to be revealed and I can somewhat predict what the, what that room is going to look like.  
**Translation:** 

**[7788.08s] English:** But I may not be able to predict the details of the texture of the ground and where the tiles are ending and stuff like that.  
**Translation:** 

**[7794.32s] English:** Right?  
**Translation:** 

**[7794.54s] English:** So those are irrelevant details that perhaps.  
**Translation:** 

**[7797.16s] English:** My representation will eliminate.  
**Translation:** 

**[7799.40s] English:** And so.  
**Translation:** 

**[7800.00s] English:** So what I need is to train this second neural net in such a way that whenever the continuation video clip varies over all the plausible continuations, the representation doesn't change.  
**Translation:** 

**[7815.62s] English:** Got it.  
**Translation:** Vocabulary: continuation: 后续内容; continuations: 多种可能的后续; plausible: 合理的

**[7816.22s] English:** Okay.  
**Translation:** 

**[7816.90s] English:** Yeah, yeah.  
**Translation:** 

**[7817.56s] English:** Got it.  
**Translation:** 

**[7818.20s] English:** Over the space of representations, doing the same kind of thing as you're doing with similarity learning.  
**Translation:** 

**[7824.24s] English:** Right.  
**Translation:** 

**[7825.40s] English:** Yeah.  
**Translation:** 

**[7825.60s] English:** So these are two ways to handle multimodality in a prediction, right?  
**Translation:** 

**[7829.54s] English:** In the first way, you parameterize the prediction with a latent variable, but you predict pixels, essentially, right?  
**Translation:** Vocabulary: multimodality: 多模态; parameterize: 参数化; pixels: 像素

**[7835.74s] English:** In the second one, you don't predict pixels.  
**Translation:** 

**[7838.40s] English:** You predict an abstract representation of pixels, and you guarantee that this abstract representation has as much information as possible about the input, but sort of drops all the stuff that you really can't predict, essentially.  
**Translation:** 

**[7851.70s] English:** I used to be a big fan of the first approach.  
**Translation:** 

**[7853.58s] English:** And in fact, in this paper with Ishan Mishra, this blog post, The Dark Matter of Intelligence, I was kind of advocating for this.  
**Translation:** Vocabulary: advocating: 提倡

**[7859.54s] English:** And in the last year and a half, I've completely changed my mind.  
**Translation:** 

**[7862.80s] English:** I'm now a big fan of the second one.  
**Translation:** 

**[7865.20s] English:** And it's because of a small collection of algorithms that have been proposed over the last year and a half or so, two years, to do this, including vCrag.  
**Translation:** 

**[7877.56s] English:** Its predecessor called Barlow-Twins, which I mentioned, a method from our friends at DeepMind called BYOL, and there's a bunch of others now that kind of work similarly.  
**Translation:** Vocabulary: predecessor: 前任版本

**[7889.64s] English:** So they're all based on this idea of joint embedding.  
**Translation:** 

**[7892.62s] English:** Some of them have an explicit criterion that is an approximation of mutual information.  
**Translation:** Vocabulary: approximation: 近似; criterion: 标准; embedding: 嵌入; explicit: 明确

**[7896.54s] English:** Some others at BYOL work, but we don't really know why.  
**Translation:** 

**[7899.42s] English:** And there's been, like, lots of theoretical papers about why BYOL works.  
**Translation:** 

**[7902.38s] English:** No, it's not that, because we take it out and it still works, and blah, blah, blah.  
**Translation:** 

**[7905.92s] English:** I mean, so there's, like, a big debate.  
**Translation:** 

**[7908.04s] English:** But the important point is that we now have a collection of non-contrastive joint embedding methods, which I think is the best thing since sliced bread.  
**Translation:** 

**[7916.46s] English:** So I'm super excited about this, because I think...  
**Translation:** 

**[7919.54s] English:** It's so big.  
**Translation:** 

**[7920.00s] English:** shot for techniques that would allow us to kind of build predictive world models and at the same  
**Translation:** Vocabulary: predictive: 预测性的

**[7927.04s] English:** time learn hierarchical representations of the world where what matters about the world is  
**Translation:** 

**[7931.20s] English:** preserved and what is irrelevant is eliminated and by the way the representations the before and  
**Translation:** Vocabulary: hierarchical: 层次分明的; irrelevant: 无关的

**[7936.32s] English:** after is across in the space in a sequence of images or is it for single images uh it would be  
**Translation:** 

**[7942.64s] English:** either for a single image for a sequence it doesn't have to be images this could be applied  
**Translation:** 

**[7946.08s] English:** to text this could be applied to just about any signal i'm looking at you know i'm looking for  
**Translation:** 

**[7951.20s] English:** methods that are generally applicable that are not specific to you know one particular modality  
**Translation:** Vocabulary: modality: 检测方式

**[7955.76s] English:** you know it could be audio or whatever got it so what's the story behind this paper this this  
**Translation:** 

**[7960.16s] English:** paper is what is is describing one of the one such method this is vic rec method so this is co-authored  
**Translation:** 

**[7965.36s] English:** uh the first author is a student uh called adrian bound who is a resident phd student at fair paris  
**Translation:** 

**[7972.48s] English:** who is co-advised by me and jean pons  
**Translation:** Vocabulary: adrian: 艾德里安

**[7976.08s] English:** uh professor at economic superior also a research director at inria so this is wonderful program in  
**Translation:** 

**[7983.12s] English:** france where phd students can basically do their phd in industry and that's kind of what what's  
**Translation:** Vocabulary: inria: 法国国家科研中心

**[7988.08s] English:** happening here um and this paper is a follow-up on uh the this bottle twin paper by my former  
**Translation:** 

**[7996.48s] English:** postdoc now stephanie with lijing and and yorish montar and a bunch of other people from from fair  
**Translation:** Vocabulary: stephanie: 斯蒂芬妮

**[8004.56s] English:** and one of the main  
**Translation:** 

**[8006.08s] English:** criticisms from reviewers is that v craig is not different enough from bottle twins but  
**Translation:** Vocabulary: craig: 克雷格; criticisms: 批评

**[8012.88s] English:** you know my impression is that it's you know bottle twins with a few bugs fixed essentially and  
**Translation:** 

**[8020.24s] English:** uh in the end this is what people will use right so but you know i'm used to stuff yeah that i  
**Translation:** 

**[8027.12s] English:** submit being rejected for so it might be rejected and actually exceptionally well cited because  
**Translation:** 

**[8031.36s] English:** people use it well it's already decided like a bunch of times so i mean the the the question is  
**Translation:** Vocabulary: cited: 被引用; exceptionally: 非常

**[8036.08s] English:** then to the deeper question about peer review and conference  
**Translation:** 

**[8040.00s] English:** I mean, computer science is a field that's kind of unique that the conference is highly prized.  
**Translation:** 

**[8044.94s] English:** That's one.  
**Translation:** 

**[8046.12s] English:** And it's interesting because the peer review process there is similar, I suppose, to journals, but it's accelerated significantly.  
**Translation:** 

**[8053.62s] English:** Well, not significantly, but it goes fast.  
**Translation:** 

**[8056.42s] English:** And it's a nice way to get stuff out quickly, to peer review it quickly, go to present it quickly to the community.  
**Translation:** 

**[8062.68s] English:** So not quickly, but quicker.  
**Translation:** 

**[8065.10s] English:** Yeah.  
**Translation:** 

**[8065.26s] English:** But nevertheless, it has many of the same flaws of peer review because it's a limited number of people look at it.  
**Translation:** 

**[8071.50s] English:** There's bias.  
**Translation:** 

**[8072.68s] English:** If you want to do new ideas, you're going to get pushback.  
**Translation:** 

**[8078.06s] English:** There's self-interested people that kind of can infer who submitted it and kind of be cranky about it, all that kind of stuff.  
**Translation:** Vocabulary: cranky: 爱发脾气; pushback: 反对

**[8087.72s] English:** Yeah.  
**Translation:** 

**[8087.98s] English:** I mean, there's a lot of social phenomena there.  
**Translation:** 

**[8090.66s] English:** There's one social phenomenon, which is that because the field has been growing exponentially,  
**Translation:** 

**[8095.26s] English:** the vast majority of people in the field are extremely junior.  
**Translation:** Vocabulary: exponentially: 成倍地

**[8100.46s] English:** So as a consequence, and that's just a consequence of the field growing, right?  
**Translation:** 

**[8104.90s] English:** So as the size of the field kind of starts saturating, you will have less of that problem of reviewers being very inexperienced.  
**Translation:** Vocabulary: inexperienced: 缺乏经验

**[8115.32s] English:** A consequence of this is that young reviewers, I mean, there's a phenomenon which is that reviewers try to make their life easy  
**Translation:** 

**[8124.50s] English:** and to make their life easier.  
**Translation:** 

**[8125.24s] English:** Yeah.  
**Translation:** 

**[8125.28s] English:** And to make their life easy when reviewing a paper is very simple.  
**Translation:** 

**[8128.02s] English:** You just have to find a flaw in the paper, right?  
**Translation:** 

**[8130.02s] English:** So basically, they see their task as finding flaws in papers.  
**Translation:** 

**[8134.56s] English:** And most papers have flaws, even the good ones.  
**Translation:** 

**[8137.84s] English:** So it's easy to do that.  
**Translation:** 

**[8141.62s] English:** Your job is easier as a reviewer if you just focus on this.  
**Translation:** 

**[8146.40s] English:** But what's important is, like, is there a new idea in that paper that is likely to influence?  
**Translation:** 

**[8153.74s] English:** It doesn't matter if the experiment...  
**Translation:** 

**[8155.24s] English:** If the experiments are not that great, if the protocol is, you know, so...  
**Translation:** 

**[8160.00s] English:** So, you know, things like that, as long as there is a worthy idea in it that will influence  
**Translation:** 

**[8166.06s] English:** the way people think about the problem, even if they make it better, you know, eventually  
**Translation:** 

**[8171.16s] English:** I think that's really what makes a paper useful.  
**Translation:** 

**[8175.60s] English:** And so this combination of social phenomena creates a disease that has plagued, you know,  
**Translation:** 

**[8184.30s] English:** other fields in the past, like speech recognition, where basically, you know, people chase numbers  
**Translation:** 

**[8188.42s] English:** on benchmarks, and it's much easier to get a paper accepted if it brings an incremental  
**Translation:** Vocabulary: benchmarks: 评测标准; incremental: 增量的

**[8196.36s] English:** improvement on a sort of mainstream, well-accepted method or problem.  
**Translation:** 

**[8204.24s] English:** And those are, to me, boring papers.  
**Translation:** 

**[8206.00s] English:** I mean, they're not useless, right, because industry, you know, strives on those kind  
**Translation:** 

**[8211.16s] English:** of progress, but they're not the one that I'm interested in, in terms of like new concepts  
**Translation:** 

**[8215.18s] English:** and new ideas.  
**Translation:** 

**[8216.18s] English:** So, papers that are really useful.  
**Translation:** 

**[8218.18s] English:** Yeah.  
**Translation:** 

**[8218.38s] English:** Yeah.  
**Translation:** 

**[8218.42s] English:** Trying to strike kind of new advances generally don't make it.  
**Translation:** 

**[8222.36s] English:** Now, thankfully, we have archive.  
**Translation:** 

**[8224.04s] English:** Archive, exactly.  
**Translation:** 

**[8225.40s] English:** And then there's open review type of situations where you, and then, I mean, Twitter's a kind  
**Translation:** 

**[8230.26s] English:** of open review.  
**Translation:** 

**[8231.26s] English:** I'm a huge believer that reviews should be done by thousands of people, not two people.  
**Translation:** Vocabulary: believer: 相信者

**[8235.66s] English:** I agree.  
**Translation:** 

**[8236.66s] English:** And so archive, like, do you see a future where a lot of really strong papers, it's  
**Translation:** 

**[8241.32s] English:** already the present, but a growing future where it'll just be archive, and you're presenting  
**Translation:** 

**[8248.38s] English:** an ongoing continuous conference called Twitter slash the Internet slash Archive Sanity.  
**Translation:** 

**[8251.38s] English:** Andre just released a new version.  
**Translation:** 

**[8252.38s] English:** So, just not, you know, not being so elitist about this particular gating.  
**Translation:** Vocabulary: elitist: 精英主义

**[8253.38s] English:** It's not a question of being elitist or not.  
**Translation:** 

**[8254.38s] English:** It's a question of being basically recommendation and approvals for people who don't see themselves  
**Translation:** Vocabulary: approvals: 批准

**[8255.38s] English:** as having the ability to do so by themselves, right?  
**Translation:** 

**[8256.38s] English:** And so it saves time, right?  
**Translation:** 

**[8257.38s] English:** If you rely on, you know, the fact that you can't just say, you know, we're going to  
**Translation:** 

**[8258.38s] English:** do this and we're going to do that.  
**Translation:** 

**[8259.38s] English:** You know, we're going to do that.  
**Translation:** 

**[8260.38s] English:** You know, I think the fact that you can't just say, you know, we're going to do this  
**Translation:** 

**[8261.38s] English:** and we're going to do that, right?  
**Translation:** 

**[8262.38s] English:** It's not a question of being elitist, it's a question of being, you know, you're going  
**Translation:** 

**[8263.38s] English:** to do this and we're going to do that.  
**Translation:** 

**[8264.38s] English:** It's not a question of being elitist or not.  
**Translation:** 

**[8265.38s] English:** It's a question of being basically recommendation and approvals for people who don't see themselves  
**Translation:** 

**[8273.28s] English:** as having the ability to do so by themselves, right?  
**Translation:** 

**[8275.76s] English:** And so it saves time, right?  
**Translation:** 

**[8277.34s] English:** If you rely on other people's opinion.  
**Translation:** 

**[8280.00s] English:** you trust those people or those groups to evaluate a paper for you that saves you time because you  
**Translation:** 

**[8290.16s] English:** know you don't have to like scrutinize uh the paper as much you know it is brought to your  
**Translation:** Vocabulary: evaluate: 评估; scrutinize: 细查

**[8294.32s] English:** attention i mean it's the whole idea of sort of you know collective recommender system right  
**Translation:** 

**[8298.64s] English:** so i actually thought about this a lot um you know about 10 15 years ago because there were  
**Translation:** Vocabulary: recommender: 推荐系统

**[8304.40s] English:** discussions at nips and you know and we're about to create iclear with yosha benjo and so i wrote  
**Translation:** 

**[8311.92s] English:** a document um kind of describing a reviewing system which basically was you know you post  
**Translation:** 

**[8318.24s] English:** your paper on some repository let's say archive or now could be open review and then you can form  
**Translation:** 

**[8324.48s] English:** uh a reviewing entity which is equivalent to a reviewing board you know of a journal or  
**Translation:** Vocabulary: repository: 资料库

**[8331.52s] English:** program committee of a conference you have to list  
**Translation:** 

**[8334.40s] English:** the members and then that group reviewing entity can choose to review a particular paper  
**Translation:** 

**[8342.40s] English:** spontaneously or not there is no exclusive relationship anymore between  
**Translation:** 

**[8346.16s] English:** a paper and a venue or reviewing entity any reviewing entity can review any paper  
**Translation:** Vocabulary: spontaneously: 自行其是

**[8352.64s] English:** or may choose not to uh and then you know give an evaluation it's not published not  
**Translation:** 

**[8357.44s] English:** published it's just an evaluation and a comment which would be public signed by the reviewing  
**Translation:** 

**[8362.56s] English:** entity and  
**Translation:** 

**[8364.40s] English:** if it's signed by a reviewing entity you know it's one of the members of reviewing entity so  
**Translation:** 

**[8367.84s] English:** if the reviewing entity is you know lex friedman's uh you know preferred papers right you know it's  
**Translation:** 

**[8374.00s] English:** lex friedman writing a review yes what so for me one that's a beautiful uh system i think but  
**Translation:** Vocabulary: friedman: 莱克斯·弗里德曼

**[8381.44s] English:** what's in addition to that it feels like there should be a reputation system for the reviewers  
**Translation:** 

**[8387.36s] English:** for the reviewing entities not the reviewers individually the reviewing entities sure  
**Translation:** Vocabulary: individually: 单独地

**[8391.60s] English:** but even that within that the reviewers too because uh  
**Translation:** 

**[8394.40s] English:** i is there's another thing here it's not just the reputation it's an incentive  
**Translation:** Vocabulary: incentive: 激励

**[8400.00s] English:** for an individual person to do great right now in in the academic setting the incentive is kind of  
**Translation:** 

**[8406.30s] English:** internal just wanting to do a good job but honestly that's not a strong enough incentive  
**Translation:** 

**[8411.10s] English:** to do a really good job in reading a paper and finding the beautiful amidst the mistakes and  
**Translation:** 

**[8415.96s] English:** the flaws and all that kind of stuff right like if you're the person that first discovered  
**Translation:** Vocabulary: amidst: 在……之中

**[8420.26s] English:** a powerful paper and you get to be proud of that discovery then that gives a huge incentive to you  
**Translation:** 

**[8427.50s] English:** that's that's a big part of my proposal actually you I describe that as you know if if your  
**Translation:** 

**[8432.12s] English:** evaluation of papers is predictive of future success yes okay then your reputation should  
**Translation:** 

**[8438.78s] English:** go up as a reviewing entity so yeah exactly I mean that that I even had a master student who  
**Translation:** Vocabulary: predictive: 预测性的

**[8446.40s] English:** is a master student in library science and computer science actually kind of work out  
**Translation:** 

**[8451.24s] English:** exactly how that should work with formulas and everything but so in terms of implementation do  
**Translation:** Vocabulary: formulas: 公式; implementation: 实现

**[8456.88s] English:** you think that's something  
**Translation:** 

**[8457.48s] English:** that's doable I mean I've been sort of you know talking about this to sort of various people like  
**Translation:** Vocabulary: doable: 可行的

**[8462.40s] English:** you know Andrew McCallum who started open review and the reason why we picked open review for iClear  
**Translation:** 

**[8468.52s] English:** initially even though it was very early for them is because my hope was that iClear where it was  
**Translation:** 

**[8474.70s] English:** eventually going to kind of inaugurate this type of system so iClear kept the idea of open reviews  
**Translation:** 

**[8481.84s] English:** so where the reviews are you know published with the paper which I think is very useful  
**Translation:** Vocabulary: inaugurate: 正式启用

**[8487.18s] English:** but  
**Translation:** 

**[8487.48s] English:** yeah but in many ways that's kind of reverted to kind of more of a conventional type conferences  
**Translation:** Vocabulary: conferences: 会议; reverted: 回归

**[8493.12s] English:** for everything else and that I mean I I don't run iClear I'm just the president of the foundation  
**Translation:** 

**[8501.24s] English:** but um you know people who run it should make decisions about how to run it and I'm not going  
**Translation:** 

**[8506.26s] English:** to tell them because there are volunteers and I'm really thankful that they do that so but I'm  
**Translation:** 

**[8512.02s] English:** saddened by the fact that we're not being innovative enough yeah I mean just to say yeah I love it  
**Translation:** 

**[8517.48s] English:** I hope that changes, yeah.  
**Translation:** 

**[8520.00s] English:** Because the communication of science broadly, but the communication of computer science  
**Translation:** 

**[8523.44s] English:** ideas is how you make those ideas have impact, I think.  
**Translation:** 

**[8528.24s] English:** Yeah.  
**Translation:** 

**[8529.24s] English:** And I think a lot of this is because people have in their mind kind of an objective, which  
**Translation:** 

**[8536.34s] English:** is fairness for authors and the ability to count points, basically, and give credits  
**Translation:** 

**[8543.44s] English:** accurately.  
**Translation:** 

**[8544.94s] English:** But that comes at the expense of the progress of science.  
**Translation:** 

**[8548.94s] English:** So to some extent, we're slowing down the progress of science.  
**Translation:** 

**[8551.50s] English:** And are we actually achieving fairness?  
**Translation:** 

**[8553.84s] English:** And we're not achieving fairness.  
**Translation:** 

**[8555.94s] English:** We still have biases.  
**Translation:** 

**[8558.14s] English:** We're doing a double blind review, but the biases are still there.  
**Translation:** 

**[8564.38s] English:** There are different kinds of biases.  
**Translation:** 

**[8566.18s] English:** You write that the phenomenon of emergence, collective behavior exhibited by a large collection  
**Translation:** 

**[8571.58s] English:** of simple elements in interaction, is one of the things that got you into neural nets  
**Translation:** Vocabulary: emergence: 涌现; exhibited: 表现; neural: 神经

**[8576.68s] English:** in the first place.  
**Translation:** 

**[8577.68s] English:** I love cellular automata.  
**Translation:** Vocabulary: automata: 自动机; cellular: 细胞状

**[8578.68s] English:** I love it.  
**Translation:** 

**[8578.94s] English:** I love simple interacting elements and the things that emerge from them.  
**Translation:** 

**[8584.08s] English:** Do you think we understand how complex systems can emerge from such simple components that  
**Translation:** 

**[8589.84s] English:** interact simply?  
**Translation:** 

**[8590.84s] English:** No, we don't.  
**Translation:** 

**[8592.42s] English:** It's a big mystery.  
**Translation:** 

**[8593.42s] English:** Also, it's a mystery for physicists.  
**Translation:** 

**[8594.42s] English:** It's a mystery for biologists.  
**Translation:** Vocabulary: biologists: 生物学家; physicists: 物理学家

**[8598.02s] English:** How is it that the universe around us seems to be increasing in complexity and not decreasing?  
**Translation:** 

**[8604.74s] English:** I mean, that is a kind of curious property.  
**Translation:** Vocabulary: complexity: 复杂性

**[8608.68s] English:** Even though there are many theories about physics that despite the second law of thermodynamics,  
**Translation:** 

**[8618.38s] English:** evolution and learning, etc., seems to be, at least locally, to increase complexity,  
**Translation:** Vocabulary: thermodynamics: 热力学

**[8623.58s] English:** not decrease it.  
**Translation:** 

**[8624.58s] English:** So perhaps the ultimate purpose of the universe is to just get more complex.  
**Translation:** 

**[8628.84s] English:** Have these small pockets of beautiful complexity.  
**Translation:** 

**[8632.74s] English:** Does cellular automata, do these kinds of emergence and complexity, do they have a way  
**Translation:** 

**[8635.44s] English:** to do that?  
**Translation:** 

**[8636.44s] English:** Is that the answer?  
**Translation:** 

**[8637.44s] English:** It's a big question.  
**Translation:** 

**[8638.44s] English:** and complex systems give you  
**Translation:** 

**[8640.00s] English:** some intuition or guide your understanding of machine learning systems and neural networks  
**Translation:** 

**[8646.16s] English:** and so on or are these for you right now disparate concepts well it got it got me into it you know i  
**Translation:** Vocabulary: intuition: 直觉

**[8651.36s] English:** uh i discovered the existence of uh the perceptron when i was a college student um you know by reading  
**Translation:** 

**[8658.88s] English:** a book on it was a debate between chomsky and piaget and seymour pepper from mit he was kind  
**Translation:** Vocabulary: perceptron: 感知器

**[8664.56s] English:** of singing the praise of the perceptron in that book and i i the first time i heard about the  
**Translation:** 

**[8669.04s] English:** learning machine right so i started digging the literature and i found those paper those books  
**Translation:** 

**[8673.36s] English:** which were basically trans transcription of you know workshops or conferences from the 50s and 60s  
**Translation:** 

**[8679.76s] English:** about self-organizing systems so there were there was a series of conferences on self-organizing  
**Translation:** Vocabulary: conferences: 研讨会; transcription: 录音

**[8685.28s] English:** systems and the these books on this some of them are you can actually get them at the internet  
**Translation:** 

**[8690.72s] English:** archive you know the digital version uh and there are like uh fascinating articles in there by  
**Translation:** 

**[8698.16s] English:** there's a guy who's named  
**Translation:** 

**[8699.04s] English:** has been largely forgotten heinz von forster he's a german physicist who immigrated to the us  
**Translation:** Vocabulary: forster: 冯施特; heinz: 海因茨; immigrated: 移民; physicist: 物理学家

**[8706.16s] English:** and uh worked on self-organizing systems uh in the in the 50s and in the 60s he created  
**Translation:** 

**[8712.72s] English:** at university of illinois urbana-champaign he created the biological computer laboratory bcl  
**Translation:** 

**[8718.72s] English:** which was you know all about neural nets unfortunately that was kind of towards the end  
**Translation:** 

**[8723.28s] English:** of the popularity of neural nets so that that lab never kind of strived very much but but he wrote a  
**Translation:** 

**[8729.04s] English:** several papers about self-organization and the mystery of self-organization an example he has is  
**Translation:** 

**[8735.36s] English:** you take imagine you are in space there's no gravity you have a big box with magnets in it  
**Translation:** Vocabulary: gravity: 重力; magnets: 磁铁

**[8741.12s] English:** okay you know kind of rectangular magnets with north pole on one end so that's well on the other  
**Translation:** 

**[8746.48s] English:** end you shake the box gently and the magnets will kind of stick to themselves and probably form a  
**Translation:** Vocabulary: rectangular: 长方形的

**[8751.28s] English:** complex structure um you know spontaneously you know that could be an example of self-organization  
**Translation:** 

**[8757.20s] English:** but you know you have lots of examples neural nets are an example of that kind of thing so that's why we're here today.  
**Translation:** Vocabulary: neural: 神经; spontaneously: 自发地

**[8759.04s] English:** example of self-organization.  
**Translation:** 

**[8760.00s] English:** to you know in many respect and it's a it's a bit of a mystery um you know how like what what is  
**Translation:** 

**[8767.86s] English:** possible with this um you know pattern formation in physical systems in chaotic system and things  
**Translation:** 

**[8773.20s] English:** like that you know you know the emergence of life you know things like that so you know how does  
**Translation:** Vocabulary: emergence: 涌现

**[8777.68s] English:** how does that happen it's a it's a big puzzle for for physicists as well it feels like understanding  
**Translation:** 

**[8783.56s] English:** this the the mathematics of emergence in some constrained situations might help us create  
**Translation:** Vocabulary: constrained: 限制条件; physicists: 物理学家

**[8790.68s] English:** intelligence like uh help us add a little spice to the systems because um you seem to be able to  
**Translation:** 

**[8798.46s] English:** in complex systems with emergence to be able to get a lot from little and so that seems like a  
**Translation:** 

**[8805.74s] English:** shortcut to get big leaps in performance but um but there's there's a missing theoretical concept  
**Translation:** 

**[8813.38s] English:** concept  
**Translation:** Vocabulary: shortcut: 捷径

**[8813.54s] English:** that we are we don't have yeah uh and it's uh it's something also i've been fascinated by since  
**Translation:** 

**[8818.74s] English:** my undergrad days and it's how you measure complexity right so we don't actually have  
**Translation:** Vocabulary: complexity: 复杂性; fascinated: 着迷; undergrad: 本科生

**[8825.58s] English:** good ways of measuring or at least we don't have good ways of interpreting the measures that we  
**Translation:** 

**[8830.62s] English:** we have at our disposal like how do you measure the complexity of something right so there's all  
**Translation:** Vocabulary: disposal: 处理; interpreting: 解释

**[8834.94s] English:** those things you know like you know karmagor of chaiting solomon of complexity of you know the  
**Translation:** 

**[8839.54s] English:** length of the shortest program that would generate a bit string can be thought of as  
**Translation:** Vocabulary: chaiting: 查廷

**[8843.36s] English:** you know the length of the shortest program that would generate a bit string can be thought of as  
**Translation:** 

**[8843.54s] English:** the complexity of that bit string right um i've been fascinated by that concept the problem with  
**Translation:** 

**[8848.58s] English:** that is that uh that complexity is defined up to a constant which can be very large  
**Translation:** 

**[8855.78s] English:** right uh there's there are similar concepts that are derived from you know uh you know bayesian  
**Translation:** Vocabulary: bayesian: 贝叶斯的

**[8861.38s] English:** probability theory where you know the complexity of something is uh the negative log of its  
**Translation:** 

**[8867.62s] English:** probability essentially right and you have a complete equivalence between the two things  
**Translation:** Vocabulary: equivalence: 等价关系

**[8872.10s] English:** and there you would think you know the probability of something is the negative log of its probability  
**Translation:** 

**[8873.36s] English:** of something is the negative log of its probability is something that's well defined mathematically  
**Translation:** 

**[8876.08s] English:** is something that's well defined mathematically which means complexity is well defined  
**Translation:** 

**[8878.00s] English:** which means complexity is well defined but it's not true you need to have a model of  
**Translation:** 

**[8879.76s] English:** but it's not true you need to have a model of  
**Translation:** 

**[8880.00s] English:** of the distribution. You may need to have a prior if you're doing Bayesian inference,  
**Translation:** Vocabulary: inference: 推断

**[8884.96s] English:** and the prior plays the same role as the choice of the computer with which you measure your  
**Translation:** 

**[8888.72s] English:** Kolmogorov complexity. And so every measure of complexity we have has some arbitrariness in it.  
**Translation:** Vocabulary: arbitrariness: 随意性; kolmogorov: 科莫洛夫

**[8896.16s] English:** You know, an additive constant which can be arbitrarily large. And so, you know,  
**Translation:** 

**[8902.08s] English:** how can we come up with a good theory of how things become more complex if we don't have a  
**Translation:** Vocabulary: additive: 加法的; arbitrarily: 任意地

**[8905.84s] English:** good measure of complexity? Yeah, which we need for one way that people study this in the space  
**Translation:** 

**[8911.84s] English:** of biology, the people that study the origin of life or try to recreate the life in the laboratory.  
**Translation:** Vocabulary: recreate: 重创

**[8917.76s] English:** And the more interesting one is the alien one is when we go to other planets,  
**Translation:** 

**[8921.92s] English:** how do we recognize this life? Because, you know, complexity, we associate complexity,  
**Translation:** Vocabulary: alien: 外星的

**[8927.44s] English:** maybe some level of mobility with life. You know, we have to be able to like have concrete  
**Translation:** 

**[8934.64s] English:** algorithms for  
**Translation:** Vocabulary: mobility: 流动性

**[8935.84s] English:** for like measuring the level of complexity we see in order to know the difference between life and  
**Translation:** 

**[8942.24s] English:** non-life. And the problem is that complexity is in the eye of the beholder. So let me give  
**Translation:** Vocabulary: beholder: 观察者; complexity: 复杂性

**[8947.04s] English:** you an example. If I if I give you an image of the MNIST digits, right, and I flip through MNIST  
**Translation:** 

**[8955.04s] English:** digits, there is some obviously some structure to it because local structure, you know,  
**Translation:** Vocabulary: digits: 手写体数字

**[8960.88s] English:** neighboring pixels are correlated across the entire dataset.  
**Translation:** 

**[8965.84s] English:** Now imagine that,  
**Translation:** Vocabulary: correlated: 相关联的

**[8968.16s] English:** I apply a random permutation to all the pixels,  
**Translation:** 

**[8972.48s] English:** a fixed random permutation now I show you those images, they will look,  
**Translation:** Vocabulary: permutation: 排列; pixels: 像素

**[8977.28s] English:** you know, really disorganized to you, more complex.  
**Translation:** 

**[8981.04s] English:** In fact, they're not more complex in absolute terms. They're exactly the same as originally,  
**Translation:** Vocabulary: disorganized: 杂乱无章

**[8985.20s] English:** right? And if you knew what the permutation was, you know, you could undo the permutation.  
**Translation:** 

**[8990.08s] English:** Now, imagine I give you special glasses that undo the permutation. Now, all of a sudden,  
**Translation:** 

**[8995.84s] English:** complicated become simple right so if you have two  
**Translation:** 

**[9000.00s] English:** if you have you know humans on one end and then another race of aliens that sees the universe with  
**Translation:** 

**[9004.80s] English:** permutation glasses yeah with the permutation glasses what we perceive as simple to them is  
**Translation:** 

**[9010.32s] English:** hardly complicated it's probably heat yeah heat yeah okay and what they perceive as simple to us  
**Translation:** Vocabulary: perceive: 感知

**[9015.84s] English:** is is random uh fluctuation it's heat yeah so truly in the eye of the beholder it depends  
**Translation:** 

**[9023.04s] English:** what kind of glasses you're wearing right depends what kind of algorithm you're running in your  
**Translation:** Vocabulary: algorithm: 计算方法; fluctuation: 波动

**[9027.04s] English:** perception system so i don't think we'll have a theory of intelligence self-organization  
**Translation:** 

**[9032.08s] English:** evolution things like this until we have a good handle on a notion of complexity which we know is  
**Translation:** 

**[9039.12s] English:** in the high the eye of the beholder yeah it's sad to think that we might not be able to detect or  
**Translation:** 

**[9045.04s] English:** interact with alien species because we're wearing different glasses um because their notion of  
**Translation:** Vocabulary: alien: 外星的

**[9050.88s] English:** locality might be different from ours yeah this actually connects with uh fascinating questions  
**Translation:** 

**[9055.12s] English:** in physics at the moment like modern physics  
**Translation:** 

**[9057.44s] English:** uh quantum physics like you know questions about like you know can we recover the information  
**Translation:** 

**[9062.40s] English:** that's lost in a black hole and things like this right and uh and that relies on notions  
**Translation:** 

**[9066.88s] English:** of complexity um yeah which you know i find i find this fascinating can you describe your  
**Translation:** 

**[9072.40s] English:** personal quest to build an expressive electronic wind instrument ewi what is it what does it take  
**Translation:** Vocabulary: complexity: 复杂性; expressive: 富有表现力

**[9082.08s] English:** to uh to build it well i'm a tinker i like building things  
**Translation:** 

**[9086.24s] English:** uh i like  
**Translation:** Vocabulary: tinker: 修修补补

**[9087.04s] English:** things with combinations of electronics and you know mechanical stuff you know I  
**Translation:** 

**[9092.62s] English:** have a bunch of different hobbies but you know probably my first one was  
**Translation:** 

**[9097.12s] English:** little was building model airplanes and stuff like that and I still do that to  
**Translation:** 

**[9100.48s] English:** some extent but also electronics I taught myself electronics before I  
**Translation:** 

**[9104.10s] English:** studied it and the reason I taught myself electronics is because of music  
**Translation:** 

**[9109.12s] English:** my cousin was inspiring electronic musician and he had an analog  
**Translation:** Vocabulary: analog: 模拟的

**[9113.92s] English:** synthesizer and I was you know basically modifying it for him and  
**Translation:** 

**[9118.06s] English:** building sequencers and stuff like that right for  
**Translation:** Vocabulary: modifying: 修改; sequencers: 序列发生器; synthesizer: 合成器

**[9120.00s] English:** him i was i was in high school when i was doing this that's the interesting like progressive rock  
**Translation:** 

**[9124.64s] English:** like 80s like what's what's the greatest band of all time according to yama koon oh there's too  
**Translation:** 

**[9130.32s] English:** many of them but you know it's a combination of uh uh you know my vision orchestra uh weather report  
**Translation:** 

**[9139.84s] English:** yes genesis uh you know yes genesis free peter gabriel uh-huh um gentle giant you know things  
**Translation:** Vocabulary: gabriel: 彼得·加布里埃尔

**[9148.24s] English:** like that great okay so this uh this love of electronics and this love of music combined  
**Translation:** 

**[9153.68s] English:** together right so i was actually trying to play uh baroque and renaissance music and i played in a  
**Translation:** Vocabulary: baroque: 巴洛克; renaissance: 文艺复兴

**[9161.44s] English:** orchestra when i was in high school and first years of college and i played the recorder  
**Translation:** 

**[9166.80s] English:** chrome horn a little bit of oboe you know things like that so i'm a wind instrument player but i  
**Translation:** 

**[9172.56s] English:** always wanted to play improvised music even though i don't know anything about it and the only way i  
**Translation:** 

**[9177.20s] English:** figured you know  
**Translation:** Vocabulary: improvised: 即兴演奏

**[9178.24s] English:** short of like learning to play a saxophone was to play electronic wind instruments so they behave  
**Translation:** 

**[9184.40s] English:** the fingering is similar to a saxophone but you know you have wide variety of sound because you  
**Translation:** Vocabulary: fingering: 指法; saxophone: 萨克斯

**[9189.20s] English:** control the synthesizer with it so i had a bunch of those you know going back to the late 80s  
**Translation:** 

**[9195.44s] English:** from either yamaha or akai they they're both kind of the main manufacturers of those so they were  
**Translation:** Vocabulary: yamaha: 雅马哈

**[9202.80s] English:** classically you know going back several decades but i've never been completely satisfied with them  
**Translation:** 

**[9208.24s] English:** so i'm not going to be going back to them but i'm gonna let you know that it's a really good instrument  
**Translation:** 

**[9211.04s] English:** and you know those things you know are somewhat expressive i mean they measure the breath  
**Translation:** 

**[9214.16s] English:** pressure they measure the lip pressure and you know uh you have various parameters you can you  
**Translation:** Vocabulary: expressive: 表达性

**[9220.16s] English:** can vary it with fingers but they they they're not really as expressive as a acoustic instrument right  
**Translation:** 

**[9226.16s] English:** you um you hear john coltrane play two notes and you hear you know it's john coltrane you know it's  
**Translation:** Vocabulary: acoustic: 共鸣箱

**[9230.96s] English:** got a unique sound uh or or mys davis right you can hear it's mys davis uh playing the trumpet  
**Translation:** 

**[9238.24s] English:** the the sound  
**Translation:** 

**[9240.40s] English:** reflects their you know physiognomy basically the shape of the vocal track  
**Translation:** 

**[9248.00s] English:** kind of shapes the the sound so how do you do this with uh electronic instrument and i was um  
**Translation:** Vocabulary: physiognomy: 面部特征; vocal: 声音

**[9253.68s] English:** many years ago i met a guy called david wessel he he was a professor at berkeley and created the  
**Translation:** 

**[9260.72s] English:** center for like you know music technology there and he was interested in that question  
**Translation:** 

**[9264.64s] English:** and so i kept kind of thinking about this for many years and finally because of kovid you know  
**Translation:** 

**[9270.34s] English:** i was at home i was in my workshop my workshop serves also as my kind of zoom uh room and and  
**Translation:** 

**[9276.44s] English:** home office and this is in new jersey in new jersey and um i started uh really being serious  
**Translation:** 

**[9282.84s] English:** about you know building my own ue instrument what else is going on in that new jersey workshop is  
**Translation:** 

**[9288.28s] English:** there some is some some crazy stuff you built like just or or like left on the workshop floor  
**Translation:** 

**[9293.84s] English:** left  
**Translation:** 

**[9294.64s] English:** behind a lot of crazy stuff is uh you know electronics with built with microcontrollers  
**Translation:** 

**[9300.20s] English:** of various kinds and you know weird flying contraptions um so you still love flying  
**Translation:** Vocabulary: contraptions: 奇怪的装置; microcontrollers: 微控制器

**[9308.52s] English:** it's a family disease my uh my dad got me into it when i was a kid and uh he was building  
**Translation:** 

**[9315.00s] English:** model airplanes when he was a kid and uh and he was a mechanical engineer he taught himself  
**Translation:** 

**[9320.20s] English:** electronics also so he he built his early radio control systems in the  
**Translation:** 

**[9324.64s] English:** 60s early 70s  
**Translation:** 

**[9327.96s] English:** um  
**Translation:** 

**[9329.64s] English:** and so that that what got me into i mean he got me into kind of you know engineering  
**Translation:** 

**[9333.84s] English:** and science and technology you also have an interest in appreciation of flight in other  
**Translation:** 

**[9336.74s] English:** forms like with drones quadigraphers or do you yeah is it is it model airplane the  
**Translation:** Vocabulary: drones: 无人机

**[9344.60s] English:** you know i i you know before drones were you know kind of a consumer product  
**Translation:** 

**[9349.36s] English:** um you know i've got my own you know with also building a microcontroller with uh javascoops  
**Translation:** Vocabulary: javascoops: Java旋翼; microcontroller: 微控制器

**[9354.64s] English:** parameters for stabilization, writing the firmware for it, you know.  
**Translation:** 

**[9357.72s] English:** And then when it became kind of a standard thing you could buy, it was boring.  
**Translation:** Vocabulary: firmware: 固件; stabilization: 稳定

**[9360.00s] English:** you know i stopped doing it it was not fun anymore um yeah you were doing it before it was  
**Translation:** 

**[9365.82s] English:** cool yeah what uh advice would you give to a young person today in high school in college that  
**Translation:** 

**[9371.64s] English:** dreams of doing something big like yann lecun like let's talk in the space of intelligence  
**Translation:** 

**[9378.30s] English:** dreams of having a chance to solve some fundamental problem in space of intelligence  
**Translation:** 

**[9383.22s] English:** both for their career and just in life being somebody who was a part of creating something  
**Translation:** 

**[9389.38s] English:** special so try to get interested by big questions things like you know what is intelligence uh  
**Translation:** 

**[9398.38s] English:** what is the universe made of what's life all about things like that um like even like crazy  
**Translation:** 

**[9406.08s] English:** big questions like um what's time like nobody knows what time is um and uh and then learn  
**Translation:** 

**[9416.60s] English:** basic things like basic methods  
**Translation:** 

**[9419.38s] English:** either from math from physics or from engineering uh things that have a long shelf life um like if  
**Translation:** 

**[9425.88s] English:** you have a choice between like you know learning uh you know mobile programming on iphone or quantum  
**Translation:** 

**[9433.06s] English:** mechanics take quantum mechanics um because you're going to learn things that you have no idea exist  
**Translation:** 

**[9439.74s] English:** and you may not you never you know you may never be a quantum physicist but you will learn about  
**Translation:** 

**[9446.04s] English:** path integrals and path integrals are used uh everywhere it's the same way you can learn about  
**Translation:** Vocabulary: integrals: 积分; physicist: 物理学家

**[9449.38s] English:** the same formula that you use for you know bayesian integration and stuff like that  
**Translation:** 

**[9453.38s] English:** so the ideas the little ideas within quantum mechanics within some of these kind of more  
**Translation:** Vocabulary: bayesian: 贝叶斯

**[9459.68s] English:** solidified fields will have a longer shelf life they'll you'll somehow use indirectly  
**Translation:** 

**[9465.70s] English:** in in your work learn classical mechanics like you learn about lagrangians for example  
**Translation:** Vocabulary: lagrangians: 拉格朗日方程; solidified: 固化

**[9471.46s] English:** which is like a huge hugely useful concept you know for all kinds of different things  
**Translation:** 

**[9476.38s] English:** uh  
**Translation:** 

**[9477.38s] English:** learn uh statistical physics uh you know you're going to learn about quantum mechanics you're  
**Translation:** 

**[9478.38s] English:** going to learn about quantum mechanics you know you're going to learn about quantum mechanics  
**Translation:** 

**[9479.38s] English:** because  
**Translation:** 

**[9480.00s] English:** all the math that comes out for machine learning  
**Translation:** 

**[9484.18s] English:** basically comes out of, was figured out by statistical physicists  
**Translation:** 

**[9488.22s] English:** in the late 19th, early 20th century.  
**Translation:** Vocabulary: physicists: 物理学家

**[9490.62s] English:** And for some of them, actually more recently,  
**Translation:** 

**[9494.40s] English:** by people like Giorgio Parisi, who just got the Nobel Prize  
**Translation:** Vocabulary: nobel: 诺贝尔奖

**[9497.44s] English:** for the replica method, among other things.  
**Translation:** 

**[9500.16s] English:** It's used for a lot of different things.  
**Translation:** 

**[9503.24s] English:** Variational inference, that math comes from statistical physics.  
**Translation:** 

**[9507.34s] English:** So a lot of those kind of, you know, basic courses,  
**Translation:** Vocabulary: inference: 推理; variational: 变分的

**[9514.00s] English:** you know, if you do electrical engineering,  
**Translation:** 

**[9516.26s] English:** you take signal processing, you'll learn about Fourier transforms.  
**Translation:** Vocabulary: fourier: 傅里叶; transforms: 变换

**[9519.56s] English:** Again, something super useful.  
**Translation:** 

**[9521.68s] English:** It's at the basis of things like graph neural nets,  
**Translation:** Vocabulary: neural: 神经的

**[9524.70s] English:** which is an entirely new sub-area of, you know, AI machine learning,  
**Translation:** 

**[9530.18s] English:** deep learning, which I think is super promising  
**Translation:** 

**[9532.00s] English:** for all kinds of applications.  
**Translation:** 

**[9534.12s] English:** Something very promising, if you're more interested in applications,  
**Translation:** 

**[9536.68s] English:** is the application.  
**Translation:** 

**[9537.34s] English:** So if you're interested in applications of AI machine learning  
**Translation:** 

**[9538.84s] English:** and deep learning to science, or to science  
**Translation:** 

**[9543.70s] English:** that can help solve big problems in the world.  
**Translation:** 

**[9545.56s] English:** I have colleagues at Meta, at FAIR,  
**Translation:** 

**[9549.28s] English:** who started this project called Open Catalyst.  
**Translation:** Vocabulary: catalyst: 催化剂

**[9551.32s] English:** And it's an open project collaborative.  
**Translation:** 

**[9553.94s] English:** And the idea is to use deep learning  
**Translation:** Vocabulary: collaborative: 协作开发

**[9556.70s] English:** to help design new chemical compounds or materials  
**Translation:** 

**[9561.98s] English:** that would facilitate the separation of hydrogen from oxygen.  
**Translation:** Vocabulary: facilitate: 促进

**[9565.04s] English:** If you can efficiently separate hydrogen from oxygen,  
**Translation:** 

**[9566.68s] English:** if you can efficiently separate oxygen from hydrogen with electricity,  
**Translation:** Vocabulary: efficiently: 高效地

**[9570.98s] English:** you solve climate change.  
**Translation:** 

**[9573.44s] English:** It's as simple as that.  
**Translation:** 

**[9574.46s] English:** Because you cover, you know, some random desert with solar panels,  
**Translation:** 

**[9580.76s] English:** and you have them work all day, produce hydrogen,  
**Translation:** 

**[9583.40s] English:** and then you ship the hydrogen wherever it's needed.  
**Translation:** 

**[9585.34s] English:** You don't need anything else.  
**Translation:** 

**[9588.52s] English:** You know, you have controllable power that's, you know,  
**Translation:** 

**[9594.10s] English:** can be transported anywhere.  
**Translation:** Vocabulary: transported: 运输

**[9595.64s] English:** So if we can do something like this,  
**Translation:** 

**[9596.52s] English:** we can do it.  
**Translation:** 

**[9596.62s] English:** We can do it.  
**Translation:** 

**[9596.64s] English:** We can do it.  
**Translation:** 

**[9596.66s] English:** If we have a large-scale, efficient...  
**Translation:** 

**[9600.00s] English:** uh energy storage technology like producing hydrogen uh we solve climate change here's  
**Translation:** 

**[9606.72s] English:** another way to solve climate change is figuring out how to make fusion work now the problem with  
**Translation:** 

**[9610.96s] English:** fusion is that you make a super hot plasma and the plasma is unstable and you can't control it maybe  
**Translation:** Vocabulary: plasma: 等离子体; unstable: 不稳定的

**[9616.32s] English:** with deep learning you can find controllers that will stabilize plasma and make you know practical  
**Translation:** 

**[9620.08s] English:** fusion reactors i mean that's very speculative but you know it's worth trying because um you know it  
**Translation:** Vocabulary: speculative: 推测性的; stabilize: 稳定

**[9626.72s] English:** uh the payoff is huge there's a group at google working on this led by john platt so control uh  
**Translation:** 

**[9632.32s] English:** convert as many problems in science and physics and biology and chemistry into a into a learnable  
**Translation:** Vocabulary: payoff: 收益

**[9639.28s] English:** problem and see if a machine can learn it right i mean there's properties of uh you know complex  
**Translation:** 

**[9644.48s] English:** materials that we don't understand from first principle for example right so you know if we  
**Translation:** 

**[9649.36s] English:** could design uh new um you know new materials uh we could make more efficient batteries you know  
**Translation:** 

**[9656.72s] English:** we could make uh maybe faster electronics we could i mean there's a lot of things we can imagine  
**Translation:** 

**[9661.12s] English:** uh doing or you know lighter uh materials for for cars or airplanes or things like that maybe better  
**Translation:** 

**[9666.80s] English:** fuel cells i mean there's all kinds of stuff we can imagine if we had good fuel cells hydrogen  
**Translation:** 

**[9670.80s] English:** fuel cells uh we could use them to power airplanes and you know uh transportation wouldn't be uh or  
**Translation:** 

**[9676.32s] English:** cars and we wouldn't have a emission problem uh co2 emission problems for for air transportation  
**Translation:** Vocabulary: emission: 排放

**[9683.92s] English:** anymore so there's a lot of those things i think  
**Translation:** 

**[9686.72s] English:** where ai you know can be used it and and this is not even talking about all the sort of medicine  
**Translation:** 

**[9692.88s] English:** biology and and everything like that right you know like protein folding you know figuring out  
**Translation:** 

**[9699.04s] English:** like how can you design your proteins that it sticks to another protein at a particular site  
**Translation:** 

**[9702.72s] English:** because that's how you design drugs in the end um so you know deep learning would be useful  
**Translation:** 

**[9707.44s] English:** although this and those are kind of you know would be sort of enormous progress if we could  
**Translation:** 

**[9712.08s] English:** use it for that here's an example if you take um this is like from  
**Translation:** 

**[9716.72s] English:** recent material physics you take a monoatomic  
**Translation:** Vocabulary: monoatomic: 单原子的

**[9720.00s] English:** layer of graphene right so it's just carbon on an hexagonal mesh and you make this single  
**Translation:** 

**[9726.72s] English:** single atom thick you put another one on top you twist them by some magic number of degrees  
**Translation:** Vocabulary: graphene: 石墨烯; hexagonal: 六边形

**[9732.96s] English:** three degrees or something it becomes superconductor nobody has any idea why  
**Translation:** 

**[9740.72s] English:** uh i want to know how that was discovered but that's the kind of thing that machine learning  
**Translation:** 

**[9743.76s] English:** can actually discover these well things maybe not but but there is a hint perhaps that with  
**Translation:** 

**[9749.68s] English:** machine learning we would train a system to basically be a phenomenological model of  
**Translation:** Vocabulary: phenomenological: 现象学的

**[9755.28s] English:** some complex emergent phenomenon which you know superconductivity is one of those uh  
**Translation:** 

**[9762.32s] English:** where you know think this collective phenomenon is too difficult to describe from first principles  
**Translation:** Vocabulary: emergent: 涌现; superconductivity: 超导性

**[9766.80s] English:** with the current you know the usual sort of you know reductionist type method but we could have  
**Translation:** 

**[9774.00s] English:** deep learning systems that predict the properties of a system from a description of it after being  
**Translation:** Vocabulary: reductionist: 还原论的

**[9779.44s] English:** trained  
**Translation:** 

**[9779.68s] English:** with sufficiently uh many uh samples um this guy pascal fuad dpfl he has a startup company  
**Translation:** Vocabulary: sufficiently: 足够地

**[9788.00s] English:** um that where he basically trained a convolutional net essentially to predict the aerodynamic  
**Translation:** 

**[9795.92s] English:** properties of solids and you can generate as much data as you want by just running  
**Translation:** Vocabulary: aerodynamic: 气动学; convolutional: 卷积的

**[9800.48s] English:** competition-free dynamics right so you give a like a wing airfoil or something shape of some kind  
**Translation:** 

**[9809.68s] English:** and you run competition-free dynamics you get as a result the drag and you know uh lift and all that  
**Translation:** Vocabulary: airfoil: 机翼外形

**[9816.80s] English:** stuff right and you can you can generate lots of data train a neural net to make those predictions  
**Translation:** 

**[9821.60s] English:** and now what you have is a differentiable model of let's say drag and lift as a function of the  
**Translation:** Vocabulary: differentiable: 可微分的

**[9827.68s] English:** shape of that solid and so you can do background and design you can optimize the shape so you get  
**Translation:** 

**[9831.76s] English:** the properties you want um yeah that's incredible that's incredible and on top of all that probably  
**Translation:** 

**[9839.68s] English:** should  
**Translation:** 

**[9840.00s] English:** read a little bit of literature and a little bit of history for inspiration and for wisdom  
**Translation:** 

**[9846.16s] English:** because after all all of these technologies will have to work in the human world yes  
**Translation:** 

**[9850.46s] English:** and the human world is complicated it is sadly yeah and this is um an amazing conversation i'm  
**Translation:** 

**[9858.48s] English:** really honored that you would talk with me today thank you for all the amazing work you're doing  
**Translation:** 

**[9862.14s] English:** at fair at meta and thank you for being so passionate after all these years about everything  
**Translation:** 

**[9867.96s] English:** that's going on you're you're a beacon of hope for the machine learning community and thank you  
**Translation:** 

**[9872.28s] English:** so much for spending your valuable time with me today that was awesome thanks for having me on  
**Translation:** Vocabulary: beacon: 灯塔

**[9876.24s] English:** that was it was a pleasure thanks for listening to this conversation with jan lacoon to support  
**Translation:** 

**[9881.80s] English:** this podcast please check out our sponsors in the description and now let me leave you with some  
**Translation:** Vocabulary: sponsors: 赞助商

**[9887.28s] English:** words from isaac asimov your assumptions are your windows in the world scrub them off every once in  
**Translation:** 

**[9895.20s] English:** a while or the light won't come in  
**Translation:** Vocabulary: assumptions: 前提; scrub: 擦拭

**[9897.96s] English:** thank you for listening and hope to see you next time  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
