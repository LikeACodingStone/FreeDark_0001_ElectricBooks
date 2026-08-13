# Podcast vocabulary notes
Source file: Lex Fridman - Yann LeCun： Dark Matter of Intelligence and Self-Supervised Learning ｜ Lex Fridman Podcast #258.opus
Improved subtitle: punctuation and vocabulary regenerated from current config.

**[0.00s] English:** The following is a conversation with Jan LeCun; his second time on the podcast.  
**Translation:** 

**[4.78s] English:** He is the chief AI scientist at Meta (formerly Facebook), professor at NYU, and a Turing Award winner.  
**Translation:** Vocabulary: formerly: 原先; turing: 图灵奖

**[13.08s] English:** One of the seminal figures in the history of machine learning and artificial intelligence,  
**Translation:** 

**[18.46s] English:** And someone who is brilliant and opinionated in the best kind of way.  
**Translation:** Vocabulary: seminal: 开创性的

**[23.50s] English:** And so it's always fun to talk to.  
**Translation:** 

**[25.72s] English:** This is the Lex Friedman Podcast.  
**Translation:** Vocabulary: friedman: 弗里德曼

**[27.74s] English:** To support it, please check out our sponsors in the description.  
**Translation:** 

**[31.24s] English:** And now, here's my conversation with Jan LeCun.  
**Translation:** Vocabulary: sponsors: 赞助商

**[35.72s] English:** You co-wrote the article "Self-Supervised Learning: The Dark Matter of Intelligence.  
**Translation:** 

**[40.88s] English:** Great title, by the way, with Ishan Mizra.  
**Translation:** 

**[43.56s] English:** So, let me ask: What is self-supervised learning, and why is it the dark matter of intelligence?  
**Translation:** 

**[49.56s] English:** I'll start with the dark matter part.  
**Translation:** 

**[52.96s] English:** There is obviously a kind of learning that humans and animals are.  
**Translation:** 

**[57.74s] English:** Are we currently not reproducing properly with machines, with AI, right?  
**Translation:** Vocabulary: reproducing: 复制

**[64.66s] English:** So, the most popular approaches to machine learning today are, or paradigms, I should say.  
**Translation:** 

**[69.72s] English:** Are supervised learning and reinforcement learning.  
**Translation:** Vocabulary: approaches: 方法; paradigms: 范式; reinforcement: 强化; supervised: 监督

**[72.54s] English:** And they are extremely inefficient.  
**Translation:** 

**[75.24s] English:** Supervised learning requires many samples for learning anything.  
**Translation:** Vocabulary: inefficient: 不高效的

**[79.82s] English:** And reinforcement learning requires a ridiculously large number of trials and errors for a system to learn anything.  
**Translation:** 

**[87.74s] English:** And that's why we don't have self-driving cars.  
**Translation:** Vocabulary: ridiculously: 极其

**[92.96s] English:** That's a big leap from one to the other.  
**Translation:** 

**[94.78s] English:** Okay, so to solve difficult problems, you have to have a lot of human annotations for supervised learning to work.  
**Translation:** Vocabulary: annotations: 标注

**[104.08s] English:** And to solve those difficult problems with reinforcement learning, you have to have some way to maybe simulate that problem, such that you can do that large-scale kind of learning that reinforcement learning requires.  
**Translation:** 

**[114.38s] English:** Right.  
**Translation:** Vocabulary: simulate: 模拟

**[114.74s] English:** So, how is it that, you know,  
**Translation:** 

**[117.02s] English:** Most engineers,  
**Translation:** 

**[117.62s] English:** Most teenagers can learn to drive a car in about 20 hours.  
**Translation:** 

**[120.00s] English:** Hours of practice are required, whereas even with millions of hours of simulated practice, a self-driving  
**Translation:** Vocabulary: simulated: 模拟

**[127.88s] English:** A car can't actually learn to drive itself properly.  
**Translation:** 

**[132.20s] English:** And so obviously, we're missing something, right?  
**Translation:** 

**[134.26s] English:** And it's quite obvious for a lot of people that the immediate response you get from many is not what you might expect.  
**Translation:** 

**[139.12s] English:** People, well, use their background knowledge to learn faster.  
**Translation:** 

**[144.80s] English:** And they're right.  
**Translation:** 

**[145.96s] English:** Now, how was that background knowledge acquired?  
**Translation:** 

**[148.40s] English:** And that's the big question.  
**Translation:** 

**[150.20s] English:** So, now you have to ask: How do babies in their first few months of life learn how  
**Translation:** 

**[155.84s] English:** How does the world work?  
**Translation:** 

**[157.34s] English:** Mostly by observation, because they can hardly act in the world.  
**Translation:** 

**[161.44s] English:** And they learn an enormous amount of background knowledge about the world.  
**Translation:** 

**[164.14s] English:** That may be the basis of what we call common sense.  
**Translation:** 

**[168.30s] English:** This type of learning is not about learning a task; it's not about being reinforced for anything.  
**Translation:** 

**[173.80s] English:** It's just observing the world and figuring out how it works.  
**Translation:** Vocabulary: reinforced: 强化

**[178.38s] English:** Building world models, learning world models.  
**Translation:** 

**[181.28s] English:** How do we do this?  
**Translation:** 

**[182.42s] English:** And how do we reproduce this in machines?  
**Translation:** 

**[184.60s] English:** So, self-supervised learning is one instance or one attempt at trying to reproduce this.  
**Translation:** Vocabulary: reproduce: 复制

**[191.48s] English:** Kind of learning.  
**Translation:** 

**[192.48s] English:** Okay.  
**Translation:** 

**[193.48s] English:** So, you're just looking at observation, not even the interacting part of a child.  
**Translation:** 

**[198.82s] English:** It's just sitting there, watching Mom and Dad walk around, pick up stuff, and all of that.  
**Translation:** Vocabulary: interacting: 互动

**[203.68s] English:** That's what you mean by background knowledge.  
**Translation:** 

**[205.36s] English:** Perhaps.  
**Translation:** 

**[206.36s] English:** Not even watching Mom and Dad.  
**Translation:** 

**[207.36s] English:** Just, you know, watching.  
**Translation:** 

**[208.36s] English:** Watching the world go by.  
**Translation:** 

**[210.12s] English:** Just having eyes open or having eyes closed, or the very act of opening and closing eyes,  
**Translation:** 

**[214.60s] English:** That the world appears and disappears: all of that basic information.  
**Translation:** 

**[218.02s] English:** And you're saying that, in order to learn to drive, like, the reason humans are able to learn to  
**Translation:** 

**[224.90s] English:** Drive quickly, some faster than others, is because of the background knowledge.  
**Translation:** 

**[228.60s] English:** They were able to watch cars operate in the world in the many years leading up to it.  
**Translation:** 

**[233.64s] English:** The physics of basic objects, and all that kind of stuff.  
**Translation:** 

**[236.26s] English:** That's right.  
**Translation:** 

**[237.26s] English:** You don't even need to know how to drive.  
**Translation:** 

**[240.00s] English:** Car works right because that you can learn fairly quickly. I mean, the example I use very often is:  
**Translation:** 

**[244.24s] English:** You're driving next to a cliff, and you know in advance, because of your understanding,  
**Translation:** 

**[250.48s] English:** Of intuitive physics, if you turn the wheel to the right, the car will veer to the right.  
**Translation:** Vocabulary: intuitive: 直觉的

**[254.96s] English:** We'll run off the cliff, fall off the cliff, and nothing good will come out of this, right?  
**Translation:** 

**[259.76s] English:** Um, but if you are a sort of tabula rasa reinforcement learning system that doesn't have  
**Translation:** Vocabulary: reinforcement: 强化; tabula: 白板

**[265.84s] English:** A model of the world: you have to repeat falling off this cliff thousands of times before you.  
**Translation:** 

**[271.52s] English:** Figure out it's a bad idea, and then do a few more thousand times before you figure out how to not.  
**Translation:** 

**[276.08s] English:** Do it, and then a few more million times before you figure out how to not do it in every situation you encounter.  
**Translation:** 

**[280.72s] English:** Ever encountered anything like that? Still, self-supervised learning has to have some source of truth being told to.  
**Translation:** Vocabulary: encounter: 遇到; encountered: 遇到

**[288.72s] English:** It by somebody, and so you have to figure out a way without human assistance or without significant  
**Translation:** 

**[295.36s] English:** Amount of human power to do it, and you have to figure out a way without human assistance or  
**Translation:** 

**[295.84s] English:** Without human assistance, we cannot get that truth from the world, so the mystery remains there is...  
**Translation:** 

**[302.00s] English:** How much signal is there, how much truth is there, that the world gives you? Whether it's  
**Translation:** 

**[306.56s] English:** The human world, like you watch YouTube or something like that, or it's more natural.  
**Translation:** 

**[311.92s] English:** World, so how much signal is there? So, here's the trick: there is way more signal in sort of a cell.  
**Translation:** 

**[319.52s] English:** Supervised setting than there is in either a supervised or reinforcement setting, and this is  
**Translation:** 

**[324.88s] English:** Going to my  
**Translation:** Vocabulary: supervised: 监督学习

**[325.84s] English:** You know, the analogy of the cake: uh, the look-alike cake is sometimes called a "mock-moon" or "fake-cake," where.  
**Translation:** 

**[333.28s] English:** When you try to figure out how much information you ask the machine to predict, and how much,  
**Translation:** Vocabulary: analogy: 类比

**[338.24s] English:** Feedback you give the machine at every trial in reinforcement learning is how you give the machine a  
**Translation:** 

**[342.56s] English:** Single scalar, you tell the machine you did good, you did bad, and you; you only tell this to  
**Translation:** Vocabulary: reinforcement: 强化; scalar: 标量

**[347.84s] English:** The machine, once in a while, when I say "you," it could be the universe telling the machine, right?  
**Translation:** 

**[354.00s] English:** But it's just one scalar.  
**Translation:** 

**[355.84s] English:** So, as a consequence, there is no way you can possibly learn something very complicated without many.  
**Translation:** 

**[360.00s] English:** Many, many trials where you get many, many feedbacks of this type. Supervised learning: you give a  
**Translation:** 

**[366.96s] English:** Few bits to the machine at every sample. Let's say, you're training a system, and you know,  
**Translation:** 

**[374.24s] English:** Recognizing images on ImageNet, there are 1,000 categories, which is just a little less than 10 bits.  
**Translation:** 

**[379.04s] English:** Information per sample, but cell-supervised running: here is the setting. You ideally don't know how.  
**Translation:** 

**[385.60s] English:** To do this, yet, but ideally, you would show a machine a segment of a video and then stop.  
**Translation:** 

**[392.08s] English:** Video, and ask the machine to predict what's going to happen next. So, you let the machine predict.  
**Translation:** 

**[398.64s] English:** And then you let time go by, show the machine what actually happened, and hope the machine will  
**Translation:** 

**[405.84s] English:** You know, learn to do a better job at predicting next time around; there's a huge amount of  
**Translation:** 

**[410.40s] English:** Information you give the machine because it's an entire video clip.  
**Translation:** 

**[414.56s] English:** Of  
**Translation:** 

**[415.60s] English:** You know, the future after the video clip you fed it in the first place, so both for language and  
**Translation:** 

**[421.28s] English:** For vision, there's a subtle, seemingly trivial construction, but maybe that's representative of.  
**Translation:** 

**[428.56s] English:** What is required to create intelligence that fills the gap, so the gaps sound dumb, but can?  
**Translation:** Vocabulary: subtle: 微妙; trivial: 琐碎

**[437.36s] English:** You, it's possible that you can solve all of intelligence in this way, just for both language.  
**Translation:** 

**[445.20s] English:** Just  
**Translation:** 

**[446.32s] English:** Give a sentence, and continue it, or give a sentence with a gap in it.  
**Translation:** 

**[451.04s] English:** Uh, some words blanked out, and you fill in what words go there for vision; you give a sequence.  
**Translation:** 

**[457.68s] English:** Of images, and predict what's going to happen next, or you fill in what happened in between.  
**Translation:** 

**[463.60s] English:** Do you think it's possible that formulation alone could be a signal for self-supervised learning?  
**Translation:** 

**[470.88s] English:** Can solve intelligence for vision and language; I think that's our best shot at the moment.  
**Translation:** 

**[475.60s] English:** Um, so, will this take us all the way to, you know,  
**Translation:** 

**[480.00s] English:** Know if it will be human-level intelligence or something just cat-level intelligence, it's not clear, but  
**Translation:** 

**[485.12s] English:** Among all the possible approaches that people have proposed, I think it's a bad shot, so I think  
**Translation:** Vocabulary: approaches: 方法

**[490.98s] English:** This idea of an intelligent system filling in the blanks, either knowing how to predict the future,...  
**Translation:** 

**[498.36s] English:** Inferring the past, filling in missing information—uh, you know, I'm currently filling in the blanks.  
**Translation:** Vocabulary: inferring: 推断

**[505.56s] English:** What is behind your head, and what your head looks like from the back?  
**Translation:** 

**[509.90s] English:** Because I have a basic knowledge about how humans are made, and I don't know if you're  
**Translation:** 

**[515.08s] English:** Gonna, you know, what you're gonna say at which point you're gonna speak whether you're gonna  
**Translation:** 

**[517.64s] English:** Move your head this way or that way — which way you're gonna look, but I know you're not gonna.  
**Translation:** 

**[521.16s] English:** Just dematerialize and reappear three meters down the hall, you know, because I know what's  
**Translation:** 

**[527.70s] English:** Possible and what's impossible, according to intuitive physics, so you have a model of what's  
**Translation:** Vocabulary: dematerialize: 消失; intuitive: 直觉的

**[532.30s] English:** Possible, and then you'd be very surprised if it happens, and then you'll have to reconstruct your.  
**Translation:** 

**[536.98s] English:** Model it right, so that's the model of the world it's.  
**Translation:** Vocabulary: reconstruct: 重新构建

**[539.78s] English:** You.  
**Translation:** 

**[539.90s] English:** Tells you, you know, what fills in the blanks, so given your partial information about the state.  
**Translation:** 

**[544.92s] English:** Of the world, given by your perception or your model of the world, fills in the missing.  
**Translation:** 

**[550.60s] English:** Information, and that includes predicting the future, re-predicting the past—uh—you know, filling  
**Translation:** Vocabulary: perception: 认知或模型

**[556.44s] English:** In things you don't immediately perceive, and that doesn't have to be purely generic vision or visual.  
**Translation:** 

**[562.68s] English:** Information or generic language, you can go to specifics, like, for example, predicting what control decisions will be made.  
**Translation:** Vocabulary: generic: 通用; perceive: 感知

**[569.78s] English:** You make decisions when you're driving in a lane, and you have a sequence of images from a vehicle, and then you  
**Translation:** 

**[576.08s] English:** Could you have information if you record it on video where the car ended up going, so you can go?  
**Translation:** 

**[582.30s] English:** Back in time and predict where the car went based on the very specific visual information.  
**Translation:** 

**[587.64s] English:** Domain-specific, right? But the question is whether we can come up with a sort of generic method.  
**Translation:** 

**[594.44s] English:** For, you know, training machines to do this kind of prediction or filling in the blanks.  
**Translation:** 

**[599.78s] English:** So,  
**Translation:** 

**[600.00s] English:** Right now, this type of approach has been unbelievably successful in the context of natural language processing.  
**Translation:** 

**[608.00s] English:** Every model in natural language processing is pretrained in a self-supervised manner to fill in the blanks.  
**Translation:** Vocabulary: pretrained: 预先训练; unbelievably: 难以置信地

**[613.20s] English:** You show it a sequence of words, you remove 10% of them, and then you train some gigantic neural net to predict the words that are missing.  
**Translation:** 

**[619.06s] English:** And once you've pre-trained that network, you can use the internal representation learned by it as input to something that you trained, supervised, or whatever.  
**Translation:** Vocabulary: gigantic: 巨大的; neural: 神经的; supervised: 监督的

**[631.82s] English:** That's been incredibly successful.  
**Translation:** 

**[633.36s] English:** Not so successful in images, although it's making progress.  
**Translation:** 

**[637.66s] English:** And it's based on manual data augmentation.  
**Translation:** 

**[642.42s] English:** We can go into this later.  
**Translation:** Vocabulary: augmentation: 增加

**[643.58s] English:** But what has not been successful yet is training from video.  
**Translation:** 

**[647.02s] English:** So, getting a machine to learn and represent.  
**Translation:** 

**[649.06s] English:** To represent the visual world, for example, by just watching videos.  
**Translation:** 

**[652.78s] English:** Nobody has really succeeded in doing this.  
**Translation:** 

**[654.88s] English:** Okay, well, let's give a high-level overview.  
**Translation:** 

**[657.58s] English:** What is the difference in kind and in difficulty between vision and language?  
**Translation:** 

**[663.90s] English:** So, you said that people haven't been able to really crack the problem of vision open in terms of self-supervised learning.  
**Translation:** 

**[671.96s] English:** But that may not be necessarily true because it's fundamentally more difficult.  
**Translation:** Vocabulary: fundamentally: 本质上

**[675.60s] English:** Maybe, like when we're talking about achieving...  
**Translation:** 

**[678.84s] English:** Like,...  
**Translation:** 

**[679.24s] English:** Passing the Turing test in the full spirit of the Turing test, in language, might be harder than vision.  
**Translation:** 

**[684.96s] English:** That's not obvious.  
**Translation:** Vocabulary: turing: 图灵测试

**[686.54s] English:** So, in your view, which is harder?  
**Translation:** 

**[689.20s] English:** Or perhaps they are just the same problem?  
**Translation:** 

**[692.04s] English:** The farther we get in solving each one, the more we realize it's all the same thing.  
**Translation:** 

**[696.72s] English:** It's all the same cake.  
**Translation:** 

**[697.60s] English:** I think what I'm looking for are methods that make them look essentially like the same cake.  
**Translation:** 

**[703.56s] English:** But currently, they're not.  
**Translation:** 

**[704.66s] English:** And the main issue with learning world models or learning predictability is...  
**Translation:** 

**[708.82s] English:** Predictive models.  
**Translation:** Vocabulary: predictive: 预测性的

**[710.24s] English:** Is that the prediction is never a single thing?  
**Translation:** 

**[715.90s] English:** Because the world is not entirely predictable.  
**Translation:** Vocabulary: predictable: 可预测的

**[719.02s] English:** Yeah.  
**Translation:** 

**[719.30s] English:** It may be deterministic....  
**Translation:** Vocabulary: deterministic: 决定论的

**[720.00s] English:** Stochastic, we can get into the philosophical discussion about it, but even if it's deterministic,  
**Translation:** 

**[725.12s] English:** It's not entirely predictable. And so, if I play a short video clip and then I ask you to predict,...  
**Translation:** Vocabulary: philosophical: 哲学上的; stochastic: 随机的

**[732.80s] English:** What's going to happen next? There are many, many plausible continuations for that video clip.  
**Translation:** 

**[738.16s] English:** And the number of continuations grows with the interval of time that you're asking the system.  
**Translation:** Vocabulary: continuations: 后续情节; plausible: 合乎情理的

**[743.76s] English:** To make a prediction for, and so one big question with self-supervised learning is how you represent...  
**Translation:** 

**[751.36s] English:** This uncertainty, how you represent multiple discrete outcomes, how you represent a continuum.  
**Translation:** Vocabulary: continuum: 连续体; discrete: 离散的; outcomes: 结果

**[757.04s] English:** Of all possible outcomes, etc. And if you are a classical machine learning person, you say,  
**Translation:** 

**[765.44s] English:** Oh, you just represent a distribution, right? And that's something we know how to do when we're predicting.  
**Translation:** 

**[772.00s] English:** Words, missing words in the text, because we know how to do it. And that's what we're going to do.  
**Translation:** 

**[773.68s] English:** And that's what we're going to do. And that's what we're going to do. And that's what we're going to do.  
**Translation:** 

**[773.74s] English:** Do, because you can have a neural network give a score for every word in a dictionary. It's a big list.  
**Translation:** 

**[779.90s] English:** Of numbers, maybe 100,000 or so, and you can turn them into a probability distribution that tells  
**Translation:** Vocabulary: neural: 神经网络

**[785.58s] English:** You: When I say a sentence, "the cat is chasing the blank in the kitchen." There are only a few words.  
**Translation:** 

**[793.90s] English:** That makes sense there. It could be a mouse, or it could be a lizard spot, or something like that.  
**Translation:** Vocabulary: chasing: 追赶; lizard: 蜥蜴

**[799.34s] English:** And if I say the lion is chasing the gazelle in the savannah, you also have a bunch of plausible  
**Translation:** 

**[807.34s] English:** Options for those two words, right? Because you have, kind of, an underlying reality that you can.  
**Translation:** Vocabulary: gazelle: 羚羊; savannah: 草原

**[813.82s] English:** Refer to this to sort of fill in those blanks. So, you cannot say for sure in the savannah if it's  
**Translation:** 

**[823.02s] English:** A lion, or a cheetah, or whatever. You cannot know if it's a zebra, or a goo, or whatever.  
**Translation:** Vocabulary: cannot: 不能; cheetah: 猎豹

**[829.34s] English:** Wildebeest: Same thing. But you can represent the uncertainty by just a long list of numbers.  
**Translation:** 

**[840.00s] English:** If I do the same thing with video and I ask you to predict a video clip, it's not a discrete set of potential frames.  
**Translation:** Vocabulary: discrete: 离散的

**[847.40s] English:** You have to have something that represents an infinite number of plausible continuations of multiple frames in a high-dimensional, continuous space.  
**Translation:** 

**[857.40s] English:** And we just have no idea how to do this properly.  
**Translation:** Vocabulary: continuations: 后续; infinite: 无限的; plausible: 合理的

**[860.68s] English:** Finite high-dimensional.  
**Translation:** 

**[863.24s] English:** It's finite-high dimensional, yes.  
**Translation:** Vocabulary: finite: 有限的

**[864.96s] English:** Just like with words, they try to get it down to a small, finite set of under a million—something like that.  
**Translation:** 

**[874.22s] English:** Something like that.  
**Translation:** 

**[874.74s] English:** I mean, it's kind of ridiculous that we're doing a distribution over every single possible word for language, and it works.  
**Translation:** 

**[882.82s] English:** It feels like that's a really dumb way to do it.  
**Translation:** 

**[886.16s] English:** It seems that there should be a more compressed representation of the distribution over the words.  
**Translation:** 

**[894.96s] English:** You're right about that.  
**Translation:** Vocabulary: compressed: 压缩的

**[896.08s] English:** I agree.  
**Translation:** 

**[896.88s] English:** Do you have any interesting ideas about how to represent all of the reality in a compressed way, such that you can form a distribution over it?  
**Translation:** 

**[903.76s] English:** That's one of the big questions.  
**Translation:** 

**[904.90s] English:** How do you do that?  
**Translation:** 

**[906.30s] English:** I mean, another thing that's really simplistic about current approaches to self-supervision in NLP for text is that not only do you represent a giant distribution over words,  
**Translation:** 

**[923.24s] English:** But for multiple words.  
**Translation:** Vocabulary: approaches: 方法; simplistic: 简单化

**[924.96s] English:** Those distributions are essentially independent of each other.  
**Translation:** 

**[930.28s] English:** And you don't pay too high a price for this.  
**Translation:** Vocabulary: distributions: 分配

**[933.00s] English:** So, the system, in the sentence that I gave earlier, if it gives a certain probability for a lion and a cheetah, and then a certain probability for a gazelle, wildebeest, and zebra, those two probabilities are independent of each other.  
**Translation:** 

**[954.96s] English:** And it's not the case that those things are independent.  
**Translation:** Vocabulary: cheetah: 猎豹; gazelle: 瞪羚; probabilities: 可能性; wildebeest: 角马

**[958.04s] English:** Lions actually attack like larger animals.  
**Translation:** 

**[960.00s] English:** Than cheetahs. So, you know, there's a huge independence hypothesis in this process, which  
**Translation:** Vocabulary: cheetahs: 猎豹; hypothesis: 假设

**[966.50s] English:** Is not actually true. The reason for this is that we don't know how to represent it properly.  
**Translation:** 

**[972.36s] English:** Distributions over combinatorial sequences of symbols, essentially, because the number  
**Translation:** Vocabulary: combinatorial: 组合的

**[978.06s] English:** Grows exponentially with the length of the symbols. And so, we have to use tricks for.  
**Translation:** 

**[982.54s] English:** This, but those techniques can, you know, get around it, like don't even deal with it.  
**Translation:** Vocabulary: exponentially: 成指数地

**[987.90s] English:** So, the big question is: Would there be some sort of abstract latent representation?  
**Translation:** 

**[994.20s] English:** Of the text that would say that, you know, when I switch lion for gazelle or lion for cheetah,  
**Translation:** 

**[1002.06s] English:** I also have to switch zebra for gazelle?  
**Translation:** 

**[1005.54s] English:** Yeah, so this independence assumption, let me throw some criticism at you that I often do.  
**Translation:** Vocabulary: assumption: 假设

**[1010.76s] English:** Hear and see how you respond. So, this kind of filling in the blanks is just statistics.  
**Translation:** 

**[1015.82s] English:** You're not learning anything.  
**Translation:** 

**[1017.90s] English:** Like the deep underlying concepts, you're just mimicking stuff from the past. You're  
**Translation:** 

**[1025.76s] English:** Not learning anything new, such that you can use it to generalize about the world. Or,  
**Translation:** Vocabulary: generalize: 泛化; mimicking: 模仿

**[1032.38s] English:** Okay, let me just say the crude version, which is just statistics. It's not intelligence.  
**Translation:** 

**[1038.04s] English:** What do you have to say to that? What do you usually say to that if you kind of hear it?  
**Translation:** 

**[1041.70s] English:** What kind of thing?  
**Translation:** 

**[1042.12s] English:** I don't get into those discussions because they are kind of pointless. So, first of all,  
**Translation:** 

**[1047.90s] English:** It's quite possible that intelligence is just statistics. It's just a matter of statistics for a particular  
**Translation:** 

**[1051.76s] English:** Kind.  
**Translation:** 

**[1052.70s] English:** Yes. But this is the philosophical question: is it possible that intelligence  
**Translation:** 

**[1058.84s] English:** Is that just statistics?  
**Translation:** Vocabulary: philosophical: 哲学的

**[1060.26s] English:** Yeah. But what kind of statistics? So, if you are asking whether the models of  
**Translation:** 

**[1067.94s] English:** The world, the models of the world that we learn, do they have any notion of causality?  
**Translation:** Vocabulary: causality: 因果关系

**[1072.00s] English:** Yes. So, if the criticism comes from people who say, you know, current machine learning,  
**Translation:** 

**[1077.90s] English:** Systems don't care about causality, which, by the way,  
**Translation:** 

**[1080.00s] English:** Wrong, uh, you know, I agree with that. Yeah, you should, you know, have a model of the world.  
**Translation:** 

**[1085.44s] English:** Have your actions as one of your inputs, and that will drive you to learn causal models.  
**Translation:** Vocabulary: causal: 因果; inputs: 输入

**[1090.88s] English:** Of the world, where you know what you know what, uh, intervention in the world will cause what result?  
**Translation:** 

**[1096.48s] English:** Or you can do this by observation of other agents acting in the world and observing the  
**Translation:** 

**[1101.28s] English:** Effect on other humans, for example. So, I think you know, at some level of description, intelligence,...  
**Translation:** 

**[1108.88s] English:** Is just statistics, uh, but that doesn't mean you won't have models.  
**Translation:** 

**[1115.04s] English:** That, you know, has a deep mechanistic explanation for what goes on, but the question is: how do you?  
**Translation:** 

**[1120.72s] English:** Learn them—that's the question I'm interested in, because a lot of people...  
**Translation:** Vocabulary: mechanistic: 机械的

**[1126.16s] English:** Who actually voice their criticism say that those mechanistic models have to come from somewhere.  
**Translation:** 

**[1132.32s] English:** Else, they have to come from human designers, or I don't know what, and obviously.  
**Translation:** Vocabulary: designers: 设计者

**[1137.04s] English:** We learn them.  
**Translation:** 

**[1139.04s] English:** Or, if we don't learn them as individuals, nature might learn them for us through evolution.  
**Translation:** 

**[1145.52s] English:** Regardless of what you think, those processes have been learned somehow, so if you look at the  
**Translation:** 

**[1151.52s] English:** The human brain, just like when we humans introspect about how the brain works, it seems.  
**Translation:** Vocabulary: introspect: 自我反省

**[1156.80s] English:** Like when we think about what intelligence is, we think about the high-level stuff like the models.  
**Translation:** 

**[1162.96s] English:** We've constructed concepts like cognitive science, such as concepts of memory and reasoning modules, almost  
**Translation:** Vocabulary: cognitive: 认知; modules: 模块

**[1168.88s] English:** Like these high-level modules, is there a good analogy here? Are we ignoring anything important?  
**Translation:** 

**[1179.68s] English:** The dark matter—the basic low-level mechanisms are just like we ignore the way the operating system works.  
**Translation:** Vocabulary: analogy: 类比

**[1185.36s] English:** Works; we're just using the high-level software, we're ignoring that at the low level.  
**Translation:** 

**[1192.64s] English:** The neural network might be doing something like statistics, like meaning—uh, sorry to use this word.  
**Translation:** Vocabulary: neural: 神经的

**[1198.88s] English:** It probably incorrectly.  
**Translation:** 

**[1200.00s] English:** Crudely, but doing this kind of fill-in-the-gap kind of learning and just kind of updating the...  
**Translation:** Vocabulary: crudely: 粗略地

**[1204.46s] English:** Model constantly, in order to be able to support the raw sensory information and predict it.  
**Translation:** 

**[1210.10s] English:** Adjust to the prediction when it's wrong, but like HYLA, when we look at our brain at the high level.  
**Translation:** Vocabulary: sensory: 感觉的

**[1215.48s] English:** It feels like we're doing this like we're playing chess, like we're playing with high stakes.  
**Translation:** 

**[1220.98s] English:** Levels of concepts, and we're stitching them together. We're putting them into long-term memory, but  
**Translation:** Vocabulary: stakes: 风险; stitching: 缝合

**[1226.16s] English:** Really, what's going on underneath is something we're not able to introspect, which is this kind of...  
**Translation:** 

**[1231.76s] English:** Simple, large neural networks that are just filling in the gaps, right? Well, okay, so there's a lot of  
**Translation:** 

**[1237.78s] English:** Questions, there are answers there. Okay, so first of all, there's a whole school of thought in  
**Translation:** 

**[1241.88s] English:** Neuroscience, particularly computational neuroscience, in particular, that likes the idea of predictive.  
**Translation:** Vocabulary: computational: 计算; neuroscience: 神经科学; predictive: 预测性

**[1247.12s] English:** Coding, which is really related to the idea I was talking about, is in self-supervised learning.  
**Translation:** 

**[1251.74s] English:** So, everything is about prediction. The essence of intelligence is the ability to predict.  
**Translation:** 

**[1255.70s] English:** Yeah.  
**Translation:** 

**[1256.04s] English:** Yeah.  
**Translation:** 

**[1256.14s] English:** And everything the brain does is trying to predict everything from everything else.  
**Translation:** 

**[1262.06s] English:** Okay, and that's really the underlying principle if you want that.  
**Translation:** 

**[1266.86s] English:** Self-supervised learning is trying to kind of reproduce this idea of prediction that's  
**Translation:** 

**[1270.70s] English:** Kind of an essential mechanism for task-independent learning, if you want.  
**Translation:** Vocabulary: reproduce: 复制

**[1276.22s] English:** The next step is: What kind of intelligence are you interested in reproducing, and of course, you  
**Translation:** 

**[1282.22s] English:** We all think about trying to reproduce something at a high level, you know.  
**Translation:** Vocabulary: reproducing: 复制

**[1286.02s] English:** Cognitive processes in humans, but like with machines, we're not even at the level of  
**Translation:** 

**[1291.46s] English:** Even reproducing the learning processes in a cat's brain, um, you know, the most intelligent...  
**Translation:** 

**[1298.02s] English:** Intelligent systems don't have as much common sense as a house cat, so how is it?  
**Translation:** 

**[1304.18s] English:** That cats learn, and you know, cats don't do a whole lot of uh reasoning; they certainly have causal.  
**Translation:** Vocabulary: causal: 因果的

**[1308.74s] English:** Models, they certainly have, uh, because you know, many cats can figure out how they can act on.  
**Translation:** 

**[1314.26s] English:** The world to get what they want, um, so that's the first step, and then the second step is to try to.  
**Translation:** 

**[1315.90s] English:** Um, they certainly have a fantastic model.  
**Translation:** 

**[1320.00s] English:** Intuitive physics, certainly of the dynamics of their own bodies, but also of praise and things.  
**Translation:** Vocabulary: intuitive: 直觉的

**[1326.24s] English:** Like that, so they're pretty smart. They only do this with about 800 million neurons.  
**Translation:** 

**[1333.52s] English:** We are not anywhere close to reproducing this kind of thing. So, to some extent, I could say,  
**Translation:** Vocabulary: neurons: 神经元

**[1341.20s] English:** Let's not even worry about high-level cognition, long-term planning, and reasoning.  
**Translation:** 

**[1347.84s] English:** That humans can do until we figure it out, can we even reproduce what cats are doing?  
**Translation:** Vocabulary: cognition: 认知

**[1352.40s] English:** Now, that said, this ability to learn world models is, I think, the key to the possibility.  
**Translation:** 

**[1360.08s] English:** Of learning machines that can also reason. So, whenever I give a talk, I say there are three  
**Translation:** 

**[1364.96s] English:** Challenges: Three main challenges in machine learning. The first one is getting machines to  
**Translation:** 

**[1369.68s] English:** Learn to represent the world, and I'm proposing self-supervised learning. The second is getting...  
**Translation:** 

**[1376.72s] English:** Machines to reason.  
**Translation:** 

**[1377.84s] English:** In ways that are compatible with essentially gradient-based learning, because this is what,  
**Translation:** Vocabulary: compatible: 兼容的

**[1382.16s] English:** Deep learning is all about, really. And the third one is something we have no idea how to solve.  
**Translation:** 

**[1387.44s] English:** Or, at least, I have no idea how to solve: is it possible for us to get machines to learn hierarchical representations?  
**Translation:** 

**[1394.32s] English:** Of action plans? We know how to train them to learn hierarchical representations of perception.  
**Translation:** 

**[1402.08s] English:** Computational nets and things like that, and transformers. But what about action plans? Can we  
**Translation:** Vocabulary: computational: 计算的; hierarchical: 分层的; perception: 感知; representations: 表示

**[1406.80s] English:** Get them to spontaneity?  
**Translation:** 

**[1407.60s] English:** Spontaneously Learn Good Hierarchical Representations of Actions.  
**Translation:** Vocabulary: spontaneity: 自发性

**[1410.48s] English:** Also, gradient-based.  
**Translation:** 

**[1412.32s] English:** Yeah, all of that needs to be somewhat differentiable so that you can apply.  
**Translation:** Vocabulary: differentiable: 可微分的

**[1416.80s] English:** Sort of gradient-based learning, which is really what deep learning is about.  
**Translation:** 

**[1422.00s] English:** So, it's background, knowledge, ability to reason in a way that's differentiable—that is, somehow  
**Translation:** 

**[1432.40s] English:** Connected, deeply integrated with that background knowledge, or builds on top of it.  
**Translation:** 

**[1436.80s] English:** Knowledge.  
**Translation:** Vocabulary: integrated: 融合的

**[1437.60s] English:** And then, given that background knowledge, be able to make  
**Translation:** 

**[1440.00s] English:** Plans, right? In the world, so if you take classical optimal control, there's  
**Translation:** Vocabulary: optimal: 最优化的

**[1445.64s] English:** Something in classical optimal control, called Model Predictive Control, and it's  
**Translation:** 

**[1450.76s] English:** You know, it's been around since the early '60s, and NASA uses that to compute.  
**Translation:** Vocabulary: compute: 计算; predictive: 预测性的

**[1455.18s] English:** Trajectories of rockets, and the basic idea is that you have a pretty  
**Translation:** 

**[1458.78s] English:** Predictive model of the rocket, let's say, or whatever system you intended.  
**Translation:** Vocabulary: rockets: 火箭; trajectories: 轨迹

**[1463.88s] English:** To control which, given the state of the system at time T and given an action.  
**Translation:** 

**[1469.32s] English:** That you're taking the system so that for a rocket to be thrust, and you know, all the  
**Translation:** Vocabulary: thrust: 推力

**[1474.60s] English:** Controls: You can have it give you the state of the system at time T + Δ.  
**Translation:** 

**[1478.76s] English:** Sure, here is the improved version: "Okay, so basically, a differential equation, something like that, and if you  
**Translation:** Vocabulary: differential: 差量的; equation: 方程

**[1484.88s] English:** Have this model, and you have this model in the form of some sort of neural net.  
**Translation:** 

**[1488.96s] English:** Or some sort of set of formulas that you can backpropagate gradients through you.  
**Translation:** Vocabulary: backpropagate: 反向传播; formulas: 公式; gradients: 梯度; neural: 神经

**[1493.70s] English:** Can do that, and you can do that, and you can do that, and you can do that, and you  
**Translation:** 

**[1493.86s] English:** Do what's called model predictive control, or gradient-based model.  
**Translation:** 

**[1497.58s] English:** Predictive control, so you can unroll that model in time.  
**Translation:** 

**[1505.20s] English:** You feed it a hypothesized sequence of actions, and then you have some  
**Translation:** Vocabulary: hypothesized: 假设的; unroll: 展开

**[1512.28s] English:** Objective function that measures how well, at the end of the trajectory, the  
**Translation:** 

**[1516.14s] English:** The system has succeeded or matched what you wanted, right? You know, is it a case of a robot harming anything?  
**Translation:** Vocabulary: harming: 伤害; trajectory: 轨迹

**[1520.92s] English:** As you grasp the object you want to grasp, if it's  
**Translation:** 

**[1523.68s] English:** A rocket, you know? Are you at the right place near the space station? Things like...  
**Translation:** 

**[1527.94s] English:** That, and by backpropagation through time. And again, this was invented in the  
**Translation:** 

**[1532.08s] English:** In the 1960s, an optimal control theorist could figure out what is the optimal  
**Translation:** Vocabulary: backpropagation: 反向传播; optimal: 最优; theorist: 理论家

**[1538.08s] English:** Sequence of actions that will, you know, get my system to the best final state.  
**Translation:** 

**[1543.54s] English:** State, so that's a form of reasoning; it's basically planning, and a lot of planning.  
**Translation:** 

**[1549.72s] English:** Systems in robotics are actually based on this, and  
**Translation:** 

**[1553.50s] English:** And you can think of this as a form of reasoning, so you know to take the  
**Translation:** Vocabulary: robotics: 机器人技术

**[1557.84s] English:** Example of the teenager driving a car.  
**Translation:** 

**[1560.00s] English:** Again, you have a pretty good dynamic model of the car; it doesn't need to be very accurate, but  
**Translation:** 

**[1564.24s] English:** You know, again, that if you turn the wheel to the right and there's a cliff, you're going to run into it.  
**Translation:** 

**[1568.56s] English:** Off the cliff, right? You don't need to have a very accurate model to predict that, and you can run.  
**Translation:** 

**[1572.48s] English:** This in your mind, and decide not to do it for that reason, because you can predict in advance that the  
**Translation:** 

**[1577.52s] English:** The result is going to be bad, so you can sort of imagine different scenarios and then you...  
**Translation:** Vocabulary: scenarios: 情景

**[1582.00s] English:** Know which employment opportunity or take the first step in the scenario that is most favorable, and then repeat.  
**Translation:** 

**[1586.80s] English:** The process of planning, which is called receding horizon model predictive control, so even all  
**Translation:** 

**[1591.12s] English:** Those things have names, you know, going back several decades, and so if you're not familiar with them,  
**Translation:** 

**[1598.72s] English:** Know that in classical optimal control, the model of the world is not generally learned; this, you know.  
**Translation:** 

**[1603.68s] English:** Sometimes, a few parameters you have to identify—that's called system identification—but  
**Translation:** 

**[1608.32s] English:** Generally, the model is mostly deterministic and mostly built by hand. So, the big question in AI is...  
**Translation:** Vocabulary: deterministic: 决定论的; identification: 识别

**[1615.76s] English:** I think the big challenge is  
**Translation:** 

**[1616.80s] English:** Of AI for the next decade is: How do we get machines to run predictive models in the world?  
**Translation:** Vocabulary: predictive: 预测的

**[1621.84s] English:** That deals with uncertainty and the real world in all this complexity, so it's not just the  
**Translation:** 

**[1626.96s] English:** The trajectory of a rocket, which you can reduce to first principles, is not—it's not—even just,  
**Translation:** Vocabulary: complexity: 复杂性; trajectory: 轨迹

**[1631.12s] English:** The trajectory of a robot arm, which again you can model by careful mathematics.  
**Translation:** 

**[1636.08s] English:** But it's everything else we observe in the world, you know, like people's behavior.  
**Translation:** 

**[1640.80s] English:** Um, you know, physical systems that involve collective phenomena, like water or  
**Translation:** 

**[1646.80s] English:** Or, you know, trees and branches in a tree or something, or like complex things.  
**Translation:** 

**[1654.48s] English:** That you know, humans have no trouble developing abstract representations and predictive models for  
**Translation:** 

**[1659.60s] English:** But we still don't know how to deal with machines. Where do you even begin?  
**Translation:** Vocabulary: representations: 抽象表示

**[1662.80s] English:** In these three, maybe in the planning stages, the game-theoretic nature of this world.  
**Translation:** 

**[1670.56s] English:** Where do your actions not only respond to the dynamic nature of the world and the environment, but also affect?  
**Translation:** 

**[1676.80s] English:** It seems that if there are other humans involved,  
**Translation:** 

**[1680.00s] English:** Is this point number four, or is it somehow integrated into the hierarchical representation?  
**Translation:** Vocabulary: hierarchical: 等级的; integrated: 整合的

**[1685.18s] English:** Of action, in your view?  
**Translation:** 

**[1686.38s] English:** I think it's integrated.  
**Translation:** 

**[1687.62s] English:** It's just that now your model of the world has to deal with: you know, it just makes  
**Translation:** 

**[1691.96s] English:** It's more complicated, right?  
**Translation:** 

**[1693.16s] English:** The fact that humans are complicated and not easily predictable makes your model  
**Translation:** 

**[1698.04s] English:** Of the world, much more complicated.  
**Translation:** Vocabulary: predictable: 可预测的

**[1700.04s] English:** That's much more complicated.  
**Translation:** 

**[1701.04s] English:** Well, there's a chess problem, I mean, I suppose chess is an analogy, so it's like a multi-colonel tree.  
**Translation:** Vocabulary: analogy: 类比

**[1707.24s] English:** Search.  
**Translation:** 

**[1708.24s] English:** Right.  
**Translation:** 

**[1709.24s] English:** There is a "I go, you go; I go, you go.  
**Translation:** 

**[1712.18s] English:** Like Andrej Karpathy recently gave a talk at MIT about car doors.  
**Translation:** 

**[1717.92s] English:** I think there's some machine learning too, but mostly it's about car doors.  
**Translation:** 

**[1721.06s] English:** And there's a dynamic nature to the car, like the person opening the door checking.  
**Translation:** 

**[1725.06s] English:** I mean, he wasn't talking about that.  
**Translation:** 

**[1726.96s] English:** He was talking about the perception problem of what the ontology of what defines a car.  
**Translation:** Vocabulary: ontology: 本体论; perception: 感知

**[1730.60s] English:** Door, this big philosophical question.  
**Translation:** 

**[1733.06s] English:** But to me, it was interesting because it's obvious that the person opening the car doors,  
**Translation:** Vocabulary: philosophical: 哲学的

**[1737.36s] English:** They're trying to get out.  
**Translation:** 

**[1738.24s] English:** Like here in New York, trying to get out of the car, you slowing down is going to signal  
**Translation:** 

**[1743.16s] English:** Something, you speeding up is going to signal something, and that's a dance.  
**Translation:** 

**[1746.64s] English:** It's an asynchronous chess game.  
**Translation:** Vocabulary: asynchronous: 不同时序的

**[1750.12s] English:** I don't know.  
**Translation:** 

**[1752.08s] English:** So it feels like it's not just; I mean, I guess you can integrate all of them into one.  
**Translation:** Vocabulary: integrate: 合并

**[1759.08s] English:** Giant model, like the entirety of these little interactions.  
**Translation:** 

**[1764.00s] English:** Because it's not as complicated as chess, it's just like a little dance.  
**Translation:** Vocabulary: entirety: 全部

**[1767.20s] English:** We do like a little dance together.  
**Translation:** 

**[1768.20s] English:** And then we figure it out.  
**Translation:** 

**[1769.20s] English:** Well, in some ways, it's way more complicated than chess because it's continuous.  
**Translation:** 

**[1775.22s] English:** It's uncertain in a continuous manner.  
**Translation:** 

**[1777.22s] English:** It doesn't feel any more complicated.  
**Translation:** 

**[1779.24s] English:** It feels simpler.  
**Translation:** 

**[1780.24s] English:** But it doesn't feel more complicated because that's what we've evolved to solve.  
**Translation:** 

**[1783.78s] English:** This is the kind of problem we've evolved to solve.  
**Translation:** Vocabulary: evolved: 进化

**[1785.58s] English:** And so, we're good at it because nature has made us good at it.  
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

**[1800.00s] English:** And if there is something that, you know, recent progress in chess and Go has made us realize is that humans are really terrible at those things—like, really bad.  
**Translation:** 

**[1809.04s] English:** You know, there was a story before AlphaGo that the best Go players thought they might be two or three stones behind an ideal player they would call God.  
**Translation:** 

**[1820.36s] English:** In fact, no; they are actually around nine or ten stones behind.  
**Translation:** 

**[1823.66s] English:** I mean, we're just bad.  
**Translation:** 

**[1825.22s] English:** So, we're not good at it, and it's because we have limited working memory.  
**Translation:** 

**[1829.70s] English:** You know, we're not very good at, like, doing this tree exploration—that's much better left to computers than we are.  
**Translation:** 

**[1836.70s] English:** But we are much better at learning differentiable models of the world.  
**Translation:** 

**[1840.58s] English:** I mean, I say "differentiable" in a kind of way; you know, I should say "not differentiable" in the sense that, you know, we run backprop through it, but in the sense that our brain has some mechanism for estimating gradients of some kind.  
**Translation:** Vocabulary: backprop: 反向传播; differentiable: 可微的; estimating: 估计; gradients: 梯度

**[1853.76s] English:** And that's what makes us efficient.  
**Translation:** 

**[1856.34s] English:** So, if you have an agent that consists,...  
**Translation:** 

**[1859.70s] English:** Of a model of the world, which, you know, in the human brain is basically the entire front half of the brain, an objective function, which in humans is a combination of two things.  
**Translation:** 

**[1874.32s] English:** There is your sort of intrinsic motivation module, which is in the basal ganglia, at the base of your brain.  
**Translation:** Vocabulary: basal: 底部的; ganglia: 神经节; intrinsic: 内在的; module: 模块

**[1879.84s] English:** That's the thing that measures pain and hunger, and things like that—immediate feelings and emotions.  
**Translation:** 

**[1888.08s] English:** And then there is.  
**Translation:** 

**[1889.70s] English:** You know, the equivalent of what people in reinforcement learning call a critic, which is a sort of module that predicts the outcome of a situation ahead.  
**Translation:** 

**[1901.82s] English:** And so it's not a cost function, but it's sort of not an objective function, but it's sort of a trained predictor of the ultimate objective function.  
**Translation:** Vocabulary: predictor: 预测器

**[1910.88s] English:** And that is also differentiable.  
**Translation:** 

**[1912.46s] English:** And so, if all of this is differentiable, your cost function, your critic, and your role model.  
**Translation:** 

**[1919.94s] English:** For those of you with additional questions, please feel free to stay.  
**Translation:** 

**[1920.00s] English:** Then you can use gradient-based methods to do planning, to do reasoning, to do learning, and to do all the things we'd like an intelligent agent to do.  
**Translation:** 

**[1923.08s] English:** I'll be happy to answer questions.  
**Translation:** 

**[1923.88s] English:** And I'll see you in our next panel.  
**Translation:** 

**[1931.90s] English:** And gradient-based learning—like, what's your intuition? That's probably at the core of what can solve intelligence.  
**Translation:** 

**[1938.44s] English:** So, you don't need logic-based reasoning, in your view.  
**Translation:** Vocabulary: intuition: 直觉

**[1945.14s] English:** I don't know how to make logic-based reasoning compatible with efficient learning.  
**Translation:** 

**[1950.00s] English:** I mean, there is a big question—perhaps a philosophical one.  
**Translation:** Vocabulary: compatible: 能共存的; philosophical: 哲学性的

**[1953.92s] English:** I mean, it's not that philosophical, but rather that we can ask whether all the learning algorithms we know from engineering and computer science proceed by optimizing some objective function.  
**Translation:** 

**[1967.88s] English:** So, one question we may ask is: Does learning in the brain minimize an objective function?  
**Translation:** Vocabulary: optimizing: 使最优化

**[1974.34s] English:** I mean, it could be a composite of multiple objective functions, but it's still an objective function.  
**Translation:** 

**[1980.00s] English:** Second, if it does optimize an objective function, does it do it by some sort of gradient estimation?  
**Translation:** Vocabulary: composite: 合成函数; estimation: 估计; gradient: 梯度; optimize: 优化

**[1989.38s] English:** It doesn't need to be backprop, but some way of estimating the gradient in an efficient manner, whose complexity is on the same order of magnitude as actually running the inference.  
**Translation:** 

**[2002.46s] English:** Because you can't afford to do things like perturbing a weight in your brain to figure out what the effect is.  
**Translation:** Vocabulary: backprop: 反向传播; complexity: 复杂度; estimating: 估计; inference: 推理; perturbing: 扰动

**[2007.70s] English:** And then, sort of,...  
**Translation:** 

**[2010.00s] English:** You can do a sort of estimating gradient by perturbation.  
**Translation:** Vocabulary: perturbation: 扰动

**[2013.30s] English:** To me, it seems very implausible that the brain uses some sort of zeroth-order, black-box, gradient-free optimization, because it's so much less efficient than gradient optimization.  
**Translation:** 

**[2026.34s] English:** So, it has to have a way of estimating gradients.  
**Translation:** Vocabulary: gradients: 梯度; implausible: 不可信; optimization: 优化

**[2029.22s] English:** Is it possible that some kind of logic-based reasoning emerges in pockets as a useful tool, like you said, if the brain is an objective function?  
**Translation:** 

**[2038.12s] English:** Maybe it's a mechanism for creating objective functions.  
**Translation:** Vocabulary: emerges: 出现

**[2040.00s] English:** Functions: It's a mechanism for creating knowledge bases, for example, that can then be  
**Translation:** 

**[2047.12s] English:** Queried, like maybe it's an efficient representation of knowledge that's learned.  
**Translation:** Vocabulary: queried: 查询

**[2051.28s] English:** In a gradient-based way, or something like that. Well, so I think there are a lot of different types.  
**Translation:** 

**[2055.84s] English:** Of intelligence, so first of all, I think the type of logical reasoning that we think about,...  
**Translation:** 

**[2061.12s] English:** That we are, you know, maybe stemming from sort of classical AI of the 1970s and 80s.  
**Translation:** 

**[2067.44s] English:** Um, I think humans use that relatively rarely and are not particularly good at it, but we judge each other based on it a lot.  
**Translation:** Vocabulary: stemming: 源自

**[2075.36s] English:** Other, based on our ability to solve those rare problems, it's called an IQ test, I think. So, like.  
**Translation:** 

**[2082.88s] English:** I'm not very good at chess, yes. I've been judging you the whole time, because... we actually...  
**Translation:** 

**[2089.84s] English:** Your heritage, I'm sure, makes you good at chess. No stereotypes, not all.  
**Translation:** 

**[2095.44s] English:** Stereotypes are true.  
**Translation:** Vocabulary: stereotypes: 刻板印象

**[2097.84s] English:** Well, I'm terrible at chess, so, um, you know, but I think perhaps another type of intelligence might be more important.  
**Translation:** 

**[2104.56s] English:** That I have is this, uh, you know, ability of sort of building models to the world from.  
**Translation:** 

**[2110.56s] English:** Uh, you know, reasoning is obvious, obviously, but also data, and those models generally are.  
**Translation:** 

**[2117.12s] English:** More like analogical reasoning, right? So it's reasoning by simulation and by analogy.  
**Translation:** Vocabulary: analogical: 类比的; analogy: 类比

**[2123.84s] English:** Where you use one model to apply to a new situation, even though you've never  
**Translation:** 

**[2127.44s] English:** Seen that situation, you can sort of connect it to a situation you've encountered before.  
**Translation:** Vocabulary: encountered: 遇到过

**[2133.44s] English:** And your reasoning is more, you know, akin to some sort of internal simulation, so you're  
**Translation:** 

**[2139.60s] English:** Kind of simulating what's happening when you're building, I don't know, a box out of wood or  
**Translation:** Vocabulary: simulating: 模拟

**[2143.04s] English:** Something, right? You can imagine in advance, like what would be the result of, you know, cutting the  
**Translation:** 

**[2148.00s] English:** Wood in this particular way, are you going to use screws or nails or whatever?  
**Translation:** 

**[2152.72s] English:** When you are interacting with someone, you also have a model of that person and sort of interact with it.  
**Translation:** 

**[2157.44s] English:** That person, you know, having this.  
**Translation:** Vocabulary: interacting: 互动

**[2160.00s] English:** Model in mind to kind of tell the person what you think is useful to them.  
**Translation:** 

**[2166.10s] English:** I think this ability to construct models of the world is basically the essence of intelligence.  
**Translation:** 

**[2174.00s] English:** And the ability to use it to plan actions that will fulfill a particular criterion.  
**Translation:** 

**[2183.14s] English:** Of course, it is necessary as well.  
**Translation:** Vocabulary: criterion: 标准; fulfill: 满足

**[2185.06s] English:** So, I'm going to ask you a series of impossible questions. As we keep asking, as I've been  
**Translation:** 

**[2189.50s] English:** Doing.  
**Translation:** 

**[2190.50s] English:** So, if that's the fundamental sort of dark matter of intelligence — this ability to form  
**Translation:** 

**[2195.22s] English:** A background model: What's your intuition about how much knowledge is required?  
**Translation:** Vocabulary: intuition: 直觉

**[2201.76s] English:** You know, I think dark matter makes up a significant percentage of the composition of the  
**Translation:** 

**[2209.70s] English:** The universe and how much of it is dark matter, how much of it is dark energy.  
**Translation:** 

**[2212.74s] English:** How much...?  
**Translation:** 

**[2213.74s] English:** How much...?  
**Translation:** 

**[2214.74s] English:** How much information do you think is required to be a house cat?  
**Translation:** 

**[2219.50s] English:** So, you have to be able to, when you see a box, go inside it.  
**Translation:** 

**[2223.02s] English:** When you see a human, compute the most evil action.  
**Translation:** 

**[2226.32s] English:** If there's something near an edge, you knock it off.  
**Translation:** Vocabulary: compute: 计算

**[2229.76s] English:** All of that, plus the extra stuff you mentioned, which is great self-awareness of the physics.  
**Translation:** 

**[2235.62s] English:** Of your own body, and the world.  
**Translation:** 

**[2238.84s] English:** How much knowledge is required, do you think, to solve it?  
**Translation:** 

**[2241.18s] English:** I don't even know how to measure an answer.  
**Translation:** 

**[2244.18s] English:** An answer to that question.  
**Translation:** 

**[2245.42s] English:** I'm not sure how to measure it, but whatever it is, it fits in about 800,000 neurons. 800  
**Translation:** Vocabulary: neurons: 神经元

**[2253.06s] English:** Million neurons, sorry.  
**Translation:** 

**[2254.06s] English:** The representation does.  
**Translation:** 

**[2255.06s] English:** Everything, all knowledge—right?  
**Translation:** 

**[2256.06s] English:** You know, it's less than a billion.  
**Translation:** 

**[2261.06s] English:** A dog is two billion, but a cat is less than one billion.  
**Translation:** 

**[2265.74s] English:** And so, multiply that by a thousand, and you get the number of synapses.  
**Translation:** Vocabulary: multiply: 相乘; synapses: 神经元连接

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
**Translation:** Vocabulary: reinforcement: 强化学习; sliver: 一小部分

**[2280.00s] English:** Certainly, very little through classical supervised training, although it's not even clear how.  
**Translation:** 

**[2284.34s] English:** Supervised running actually works in the biological world.  
**Translation:** Vocabulary: supervised: 监督式

**[2289.36s] English:** So, I think almost all of it is self-supervised running, but it's driven by the sort of ingrained  
**Translation:** 

**[2297.14s] English:** Objective functions that a cat or a human have at the base of their brain, which kind?  
**Translation:** Vocabulary: ingrained: 根深蒂固的

**[2301.84s] English:** Of what drives their behavior.  
**Translation:** 

**[2305.00s] English:** So nature tells us, "You're hungry.  
**Translation:** 

**[2309.56s] English:** It doesn't tell us how to feed ourselves.  
**Translation:** 

**[2312.14s] English:** That's something that the rest of our brain has to figure out, right?  
**Translation:** 

**[2314.80s] English:** Well, it's interesting because there might be more—like, deeper objective functions.  
**Translation:** 

**[2319.60s] English:** Underlying the whole thing.  
**Translation:** 

**[2321.44s] English:** So, hunger may be some kind of thing, now you go to like neurobiology, and it might be just the  
**Translation:** 

**[2326.74s] English:** Brain trying to maintain homeostasis.  
**Translation:** Vocabulary: homeostasis: 稳态; neurobiology: 神经生物学

**[2332.58s] English:** So, hunger is just one of the human-perceivable symptoms of the brain being unhappy with the  
**Translation:** 

**[2339.54s] English:** Way things are currently, because it could be just like one really dumb objective function.  
**Translation:** 

**[2344.10s] English:** At the core.  
**Translation:** 

**[2345.10s] English:** But that's how behavior is driven.  
**Translation:** 

**[2348.78s] English:** The fact that the orbeza ganglia drive us to do things that are different from, say, an  
**Translation:** 

**[2355.32s] English:** Orangutan—or certainly a cat—is what makes human nature versus orangutan nature versus.  
**Translation:** Vocabulary: ganglia: 神经节; orangutan: 猩猩

**[2361.70s] English:** Cat, nature.  
**Translation:** 

**[2363.40s] English:** So, for example, our orbiculare ganglia drive us to seek company.  
**Translation:** Vocabulary: orbiculare: 环状神经节

**[2369.16s] English:** Yeah.  
**Translation:** 

**[2369.54s] English:** Of other humans.  
**Translation:** 

**[2372.30s] English:** And that's because nature has figured out that we need to be social animals for our  
**Translation:** 

**[2376.58s] English:** Species to survive.  
**Translation:** 

**[2377.58s] English:** And it's true of many primates.  
**Translation:** 

**[2381.42s] English:** It's not true of orangutans.  
**Translation:** Vocabulary: orangutans: 猩猩; primates: 灵长类动物

**[2382.42s] English:** Orangutans are solitary animals.  
**Translation:** 

**[2385.00s] English:** They don't seek the company of others.  
**Translation:** Vocabulary: solitary: 独居的

**[2386.96s] English:** In fact, they avoid them.  
**Translation:** 

**[2389.38s] English:** In fact, they scream at them when they come too close because they are territorial.  
**Translation:** Vocabulary: territorial: 领地的

**[2392.84s] English:** Because, for their survival, evolution has figured out that's the best thing.  
**Translation:** 

**[2398.10s] English:** I mean, they are occasionally social.  
**Translation:** 

**[2399.16s] English:** Of course.  
**Translation:** 

**[2400.00s] English:** For you know, production and stuff like that, but they're mostly  
**Translation:** 

**[2405.28s] English:** Solitary, so so, all of those behaviors are not part of intelligence, you know.  
**Translation:** 

**[2409.70s] English:** People say, "Oh, you're never gonna have intelligent machines because you know...  
**Translation:** 

**[2412.30s] English:** Human intelligence is social, but then you look at orangutans; you look at  
**Translation:** 

**[2415.56s] English:** Octopuses never know their parents; they barely interact with any other.  
**Translation:** Vocabulary: octopuses: 八爪鱼

**[2420.62s] English:** They and they get to be really smart in less than a year, in about half a year.  
**Translation:** 

**[2424.54s] English:** In a year, you know, there are adults, and in two years, the dead ones. So there.  
**Translation:** 

**[2430.96s] English:** Are there things that we think of as humans being intimately linked with intelligence, like  
**Translation:** 

**[2435.96s] English:** Social interaction, like language, we think, we give way too much.  
**Translation:** Vocabulary: intimately: 密切地

**[2442.00s] English:** Importance to language as a substrate of intelligence, as humans because we think,  
**Translation:** 

**[2447.38s] English:** Our reasoning is so linked with language, so for us to solve the house cat problem,...  
**Translation:** Vocabulary: substrate: 基础介质

**[2452.10s] English:** Intelligence: Problem, you think you could do it?  
**Translation:** 

**[2454.46s] English:** On a human brain, and you could do it on a human brain, and you could do it on a  
**Translation:** 

**[2454.52s] English:** Desert island? You could have pretty much, because you have a cat sitting there.  
**Translation:** 

**[2460.12s] English:** Looking at the waves at the ocean, I figure a lot of it out; it needs to.  
**Translation:** 

**[2466.22s] English:** Have sort of, you know, the right set of drives to kind of get it to do.  
**Translation:** 

**[2472.10s] English:** The thing, and learn the appropriate things, right? But, for example, you  
**Translation:** 

**[2476.90s] English:** Know, baby humans are driven to learn to stand up and walk. Okay, that's kind of  
**Translation:** 

**[2484.44s] English:** This desire is hard-wired. How to do it precisely, however, is not that well-learned.  
**Translation:** Vocabulary: precisely: 精确地

**[2488.70s] English:** Desire to walk, move around, and stand up—that's very simple to hardwire this.  
**Translation:** 

**[2496.98s] English:** Kind of stuff, what? Oh, like the desire to—well, that's interesting; you're hard-wired.  
**Translation:** Vocabulary: hardwire: 固化

**[2503.34s] English:** To want to walk, that's not just a passing fancy; there's got to be a deeper need for walking, I think.  
**Translation:** 

**[2510.96s] English:** Was probably socially imposed by society; they need to walk, all the other things.  
**Translation:** Vocabulary: imposed: 强加的

**[2514.36s] English:** They need to walk all the other dogs.  
**Translation:** 

**[2514.42s] English:** They need to walk, all the other things, like a lot of simple bipedals.  
**Translation:** Vocabulary: bipedals: 两足生物

**[2517.12s] English:** The other bipedal, like a lot of simple.  
**Translation:** 

**[2517.14s] English:** The other bipedal, like a lot of simple animals that you know, probably walk.  
**Translation:** Vocabulary: bipedal: 两足的

**[2518.98s] English:** Animals that you know probably walk.  
**Translation:** 

**[2519.00s] English:** Animals that you know probably walk without ever  
**Translation:** 

**[2519.98s] English:** Without ever,  
**Translation:** 

**[2520.00s] English:** Watching any other members of the species, it seems like a scary thing to.  
**Translation:** 

**[2525.58s] English:** Have to do because you suck it, by Peter. Walking at first, it seems like he's crawling.  
**Translation:** 

**[2530.26s] English:** Is much safer, much more like. Why are you in a hurry? Well, because... because you have.  
**Translation:** Vocabulary: crawling: 爬行

**[2537.16s] English:** This thing that drives you to do it, you know, which is sort of part of the sort  
**Translation:** 

**[2542.90s] English:** Of human development, is that understood? Actually, what is not entirely clear.  
**Translation:** 

**[2548.02s] English:** What's the reason to get on two feet? It's really hard, like most animals.  
**Translation:** 

**[2551.48s] English:** Don't get on their two feet well; they get on all fours. You know, many mammals get on.  
**Translation:** Vocabulary: mammals: 哺乳动物

**[2555.22s] English:** Four feet, yeah. They very quickly, some of them extremely quickly, but I don't you.  
**Translation:** 

**[2559.18s] English:** Know, like, from the last time I've interacted with a table that's much more.  
**Translation:** Vocabulary: interacted: 接触过

**[2563.20s] English:** Stable than a thing, than two legs—it's just a really hard problem, yeah. I mean,...  
**Translation:** 

**[2566.92s] English:** Birds have figured it out with two feet—that's what, technically, we can go into.  
**Translation:** Vocabulary: technically: 从技术上说

**[2571.36s] English:** Ontology: They have four (I guess they have) two feet. Chickens.  
**Translation:** 

**[2575.50s] English:** You know, dinosaurs could be as small as two feet.  
**Translation:** 

**[2578.02s] English:** Many of them allegedly, I'm just now learning, that T-Rex was eating grass, not  
**Translation:** 

**[2584.44s] English:** Other animals, T-Rex might have been a friendly, friendly pet. What do you think?  
**Translation:** Vocabulary: allegedly: 据说

**[2588.52s] English:** About, I don't know if you looked at the test for general intelligence in France.  
**Translation:** 

**[2594.94s] English:** Rochelle has put together something I don't know if you had a chance to look at yet.  
**Translation:** 

**[2598.42s] English:** Thing like, what's your intuition about how to solve something like an IQ-type question?  
**Translation:** 

**[2602.90s] English:** Test: I don't know. I think it's so outside my radar screen that it's not.  
**Translation:** Vocabulary: intuition: 直觉

**[2607.06s] English:** Really, I don't know. I think it's so outside my radar screen that it's not really...  
**Translation:** 

**[2608.02s] English:** Really, I don't know. I think it's so outside my radar screen that it's not really relevant. I think, in the short term, I guess.  
**Translation:** 

**[2611.32s] English:** Relevant, I think, in the short term, I guess.  
**Translation:** 

**[2611.34s] English:** Relevant, I think, in the short term, I guess one way to ask might be another way perhaps.  
**Translation:** 

**[2614.08s] English:** One way to ask: Perhaps another way?  
**Translation:** 

**[2614.10s] English:** One way to ask might be: "Perhaps a more close-to-the-mark question would be, 'How do you work?  
**Translation:** 

**[2617.68s] English:** More specifically, what is your work like?  
**Translation:** 

**[2617.70s] English:** More specifically, what does your work entail, and how do you solve MNIST with very little data?  
**Translation:** Vocabulary: entail: 包括

**[2621.38s] English:** How do you solve MNIST with very little?  
**Translation:** 

**[2621.40s] English:** How do you solve MNIST with very little example data? That's right, and that's the  
**Translation:** 

**[2623.94s] English:** Example data: that's right, and that's the.  
**Translation:** 

**[2623.96s] English:** Example data: That's right, and that's the answer. This is probably also.  
**Translation:** 

**[2625.22s] English:** The answer to this, probably, is also  
**Translation:** 

**[2625.24s] English:** The answer to this probably is "also running, just run" to represent images.  
**Translation:** 

**[2627.14s] English:** Running, just run to represent images.  
**Translation:** 

**[2627.16s] English:** And then, learning to recognize handwritten digits will only require a few samples.  
**Translation:** Vocabulary: digits: 手写数字; handwritten: 手写

**[2633.40s] English:** And we observe this in humans, right? You show a young child a picture book with a few pictures,...  
**Translation:** 

**[2640.00s] English:** An elephant, and that's it. The child knows what an elephant is, and we see this today with practical examples.  
**Translation:** 

**[2646.08s] English:** Systems that we, you know, we train image recognition systems with enormous amounts of images.  
**Translation:** 

**[2653.52s] English:** Either completely self-supervised or very weakly supervised, for example.  
**Translation:** Vocabulary: supervised: 监督; weakly: 弱

**[2658.08s] English:** You can train a neural net to predict whatever hashtag people type on Instagram, right?  
**Translation:** 

**[2663.92s] English:** Then you can do this with billions of images because there are billions per day being shown.  
**Translation:** Vocabulary: neural: 神经网络

**[2667.28s] English:** Up, so the amount of training data there is essentially unlimited, and then you take the  
**Translation:** 

**[2673.12s] English:** Output representation, you know, a couple layers down from the output of what the system learned.  
**Translation:** Vocabulary: unlimited: 无限制的

**[2679.28s] English:** And feed this as input to a classifier for any object in the world, and it works.  
**Translation:** 

**[2684.00s] English:** Pretty well, so that's transfer learning, okay? Or weekly supervised transfer learning; people are.  
**Translation:** 

**[2691.52s] English:** Making very, very fast progress using self-supervised learning for this kind of scenario as well.  
**Translation:** 

**[2697.92s] English:** Um, and you know, my guess is that that's going to be the future for self-supervised.  
**Translation:** Vocabulary: scenario: 场景

**[2703.20s] English:** Learning how much cleaning do you think is needed for filtering out malicious signals, or what's a  
**Translation:** 

**[2712.40s] English:** Better, though, is that many people use hashtags on Instagram to get good SEO that doesn't  
**Translation:** Vocabulary: filtering: 过滤; hashtags: 话题标签; malicious: 恶意的

**[2720.40s] English:** Fully, they will represent the contents of the image by putting a picture of a cat and hashtagging it.  
**Translation:** 

**[2725.20s] English:** With, like, science is awesome!  
**Translation:** Vocabulary: contents: 图像内容; hashtagging: 添加标签

**[2727.52s] English:** Fun, I don't know, all kinds of why would you put signs; that's not very good for SEO. The way the way my...  
**Translation:** 

**[2733.52s] English:** Colleagues who worked on this project at Facebook, now Meta AI, a few years ago.  
**Translation:** Vocabulary: colleagues: 同事

**[2740.40s] English:** Dealt with this is that they only selected about 17,000 tags that correspond to  
**Translation:** 

**[2744.48s] English:** Kind of physical things or situations, like you know, that have some visual content.  
**Translation:** Vocabulary: correspond: 相符

**[2752.24s] English:** So, you know, you wouldn't have had HTBT or anything like that.  
**Translation:** 

**[2757.28s] English:** So they keep a very select set of  
**Translation:** 

**[2760.00s] English:** Hashtags, yeah, okay, but it's still, it's still on the order of you know, ten to  
**Translation:** 

**[2765.40s] English:** Twenty thousand—it's fairly large, okay. Can you tell me about the data?  
**Translation:** 

**[2770.28s] English:** Augmentation: What the heck is data augmentation, and how is it used? Maybe.  
**Translation:** 

**[2774.90s] English:** Contrast of learning for videos: What are some cool ideas here, right? So, data.  
**Translation:** Vocabulary: augmentation: 数据增强

**[2781.36s] English:** Augmentation: I mean, first, data augmentation is the idea of  
**Translation:** 

**[2784.54s] English:** Artificially increasing the size of your training set by distorting the images.  
**Translation:** Vocabulary: artificially: 人为地; distorting: 扭曲

**[2789.34s] English:** That's how you can do it in ways that don't change the nature of the image, right? So you  
**Translation:** 

**[2792.52s] English:** Take you through this: you can do data augmentation on a list, and people have  
**Translation:** 

**[2795.94s] English:** Done this since the 1990s, right? You take a digit and you shift it by.  
**Translation:** 

**[2800.50s] English:** Little bit, or you can change the size, rotate it, skew it, you know, etc., and add noise.  
**Translation:** Vocabulary: digit: 位数; rotate: 旋转

**[2807.40s] English:** Add noise, etc., and it works better if you train a supervised classifier with.  
**Translation:** 

**[2812.62s] English:** Augmented data, you're gonna get better results. Now, it's become really  
**Translation:** Vocabulary: augmented: 扩充的数据; supervised: 监督学习的

**[2817.54s] English:** Interesting over the last  
**Translation:** 

**[2819.34s] English:** Couple of years because a lot of self-supervised learning techniques have been developed.  
**Translation:** 

**[2824.34s] English:** Pre-trained vision systems are based on data augmentation and the basic.  
**Translation:** 

**[2830.08s] English:** Techniques are originally inspired by techniques that I worked on in the early  
**Translation:** 

**[2835.38s] English:** In the 1990s, Jeff Hinton worked on it as well. In the early 1990s, there were sort of parallel developments.  
**Translation:** 

**[2838.62s] English:** Work: I used to call this Siamese network, so basically, you take two identical  
**Translation:** Vocabulary: hinton: Hinttin; identical: 相同的; parallel: 并行的; siamese: 双胞胎

**[2844.66s] English:** Copies of the same network they share the same weights, and you show two.  
**Translation:** 

**[2849.34s] English:** Different views of the same object; either, those two different views may,...  
**Translation:** 

**[2853.24s] English:** Have been obtained by data augmentation, or maybe it's two different views of the  
**Translation:** 

**[2856.66s] English:** Same scene from a camera that you moved, or at different times, or something like that.  
**Translation:** Vocabulary: augmentation: 数据增强

**[2860.78s] English:** That, or two pictures of the same person, things like that, and then you  
**Translation:** 

**[2864.88s] English:** Train these neural nets, those two identical copies of this neural net to.  
**Translation:** 

**[2868.54s] English:** Produce an output representation as a vector in such a way that the  
**Translation:** 

**[2873.26s] English:** The representation for those two images is as close to each other as possible, as I had done that.  
**Translation:** 

**[2879.34s] English:** So, they are identical to each other.  
**Translation:** 

**[2880.00s] English:** Possible, right? Because you want the system to basically learn a function that will.  
**Translation:** 

**[2885.36s] English:** Be invariant, that will not change, whose output will not change when you transform those inputs.  
**Translation:** 

**[2890.80s] English:** In those particular ways, right? So that's easy to do. What's complicated is how do  
**Translation:** Vocabulary: inputs: 输入; invariant: 不变的

**[2897.04s] English:** You make sure that when you show two images that are different, the system will produce different results.  
**Translation:** 

**[2900.48s] English:** Things, because if you don't have a specific provision for this, the system will just ignore it.  
**Translation:** Vocabulary: provision: 规定

**[2907.12s] English:** The input, when you train it, will end up ignoring the input and just produce a constant.  
**Translation:** 

**[2911.28s] English:** Vector that is the same for every input, right? Yes, that's called a collapse. Now, how do you avoid it?  
**Translation:** Vocabulary: collapse: 坍缩

**[2915.84s] English:** Collapse. So, there are two ideas. Uh, one idea that I proposed in the early '90s with my colleagues at  
**Translation:** 

**[2922.16s] English:** Bell Labs, Jane Bromley, and a couple of other people, which we now call contrastive learning, which is  
**Translation:** Vocabulary: bromley: 布罗梅尔; colleagues: 同事

**[2928.56s] English:** To have negative examples, right? So you have pairs of images that you know are different.  
**Translation:** 

**[2934.24s] English:** And you show them to the network, and those two...  
**Translation:** 

**[2937.12s] English:** Copies, and then you push the two output vectors away from each other.  
**Translation:** 

**[2940.96s] English:** And it will eventually guarantee that things that are semantically similar produce similar results.  
**Translation:** Vocabulary: semantically: 从语义上; vectors: 向量

**[2945.68s] English:** Representations and things that are different produce different representations.  
**Translation:** 

**[2950.16s] English:** We actually came up with this idea for a project on doing signature verification, so we would  
**Translation:** Vocabulary: representations: 表现; verification: 验证

**[2955.68s] English:** Collect signatures from multiple people, including signatures from the same individual, and then train a  
**Translation:** 

**[2960.96s] English:** Neural net to produce the same representation, and then, you know, force the system to produce.  
**Translation:** Vocabulary: neural: 神经网络

**[2966.80s] English:** Different.  
**Translation:** 

**[2967.76s] English:** Representation for different signatures, um, this was actually the problem proposed by  
**Translation:** 

**[2973.12s] English:** People from what was then a subsidiary of TNT, called NCR, and they were interested in  
**Translation:** 

**[2979.28s] English:** Storing a representation of the signature on the 80-byte magnetic strip of a credit card.  
**Translation:** Vocabulary: subsidiary: 子公司

**[2986.48s] English:** So, we came up with the idea of having a neural network with 80 outputs, you know?  
**Translation:** 

**[2990.80s] English:** Quantize on bytes, so that we could encode it, and that was then used to compare whether.  
**Translation:** Vocabulary: bytes: 字节; encode: 编码; outputs: 输出; quantize: 量化

**[2995.60s] English:** The signature matches, or not?  
**Translation:** 

**[2997.12s] English:** That's right, so then you would know sign it and run.  
**Translation:** 

**[3000.00s] English:** Neural net, and then you would compare the output vector to whatever is stored on your card.  
**Translation:** 

**[3003.52s] English:** Actually, it worked, but they ended up not using it because nobody really cared, actually.  
**Translation:** 

**[3010.32s] English:** The American, you know, financial payment system is incredibly lax in that respect compared to Europe.  
**Translation:** 

**[3017.52s] English:** Over the signatures, what's the purpose of signatures anyway? This is very nobody looks.  
**Translation:** 

**[3021.44s] English:** At them, nobody cares, you know? It's, uh, yeah, yeah, no, so, uh, so that's contrasting, running right.  
**Translation:** 

**[3027.68s] English:** So, you need positive and negative pairs, and the problem with that is that you know, even  
**Translation:** 

**[3031.84s] English:** Though I had the original paper on this, I'm actually not very positive about it because.  
**Translation:** 

**[3037.28s] English:** It doesn't work in high dimensions if your representation is high-dimensional.  
**Translation:** Vocabulary: dimensions: 维度

**[3040.88s] English:** There are just too many ways for two things to be different, and so you would need lots and lots.  
**Translation:** 

**[3045.84s] English:** And lots of negative pairs; so, there is a particular implementation of this, which is relatively recent.  
**Translation:** Vocabulary: implementation: 实施方案

**[3051.92s] English:** From actually the Google Toronto group, uh, where you know Jeffington is the  
**Translation:** 

**[3057.44s] English:** Is  
**Translation:** Vocabulary: toronto: 多伦多

**[3057.68s] English:** Your member is called SimClear (SIMCLR), and it's basically a particular way of  
**Translation:** 

**[3064.08s] English:** Implementing this idea of contrasting running the particular objective function,  
**Translation:** Vocabulary: implementing: 实现

**[3068.56s] English:** Now, what I'm much more enthusiastic about these days are non-contrastive methods, so  
**Translation:** 

**[3074.80s] English:** Other ways to guarantee that the representations would be different for different users.  
**Translation:** 

**[3082.24s] English:** Different inputs, and it's actually based on an idea that  
**Translation:** 

**[3087.68s] English:** Jeffington proposed in the early '90s, with his student at the time, Sue Becker.  
**Translation:** Vocabulary: becker: 贝克; inputs: 输入

**[3091.76s] English:** And it's based on the idea of maximizing the mutual information between the outputs of the  
**Translation:** 

**[3095.04s] English:** Two systems: you only show positive pairs; you only show pairs of images that you know are  
**Translation:** Vocabulary: maximizing: 最大化; outputs: 输出

**[3099.44s] English:** Somewhat similar, and you train the two networks to be informative.  
**Translation:** 

**[3104.88s] English:** But also to be as informative as possible of each other, so basically one representation has to be  
**Translation:** Vocabulary: informative: 富有信息的

**[3111.60s] English:** Predictable from the other, essentially, and you know, he proposed that idea had you know a lot of.  
**Translation:** 

**[3117.68s] English:** A couple of papers in the early '90s.  
**Translation:** Vocabulary: predictable: 可预见的

**[3120.00s] English:** And then, nothing was done about it for decades.  
**Translation:** 

**[3123.02s] English:** And I kind of revived this idea together with my postdocs at FAIR.  
**Translation:** Vocabulary: postdocs: 博士后; revived: 重提

**[3128.18s] English:** Particularly, a postdoc called Stéphane Denis,  
**Translation:** 

**[3129.66s] English:** Who is now a junior professor in Finland at the University of Aalto.  
**Translation:** Vocabulary: aalto: 阿alto大学; finland: 芬兰; postdoc: 博士后

**[3134.88s] English:** We came up with something that we called "Barlow Twins.  
**Translation:** 

**[3138.92s] English:** And it's a particular way of maximizing the information content of a vector.  
**Translation:** Vocabulary: barlow: 巴洛孪生

**[3144.96s] English:** Using some hypotheses.  
**Translation:** 

**[3147.60s] English:** And we have a kind of another version of it that's more recent now.  
**Translation:** Vocabulary: hypotheses: 假设

**[3152.82s] English:** Called VICREG, V-I-C-R-E-G.  
**Translation:** 

**[3154.58s] English:** That means variance, invariance, covariance, and regularization.  
**Translation:** Vocabulary: covariance: 协方差; invariance: 不变性; variance: 方差

**[3157.94s] English:** And it's the thing I'm the most excited about in machine learning.  
**Translation:** 

**[3160.78s] English:** In the last 15 years.  
**Translation:** 

**[3161.76s] English:** I mean, I'm really, really excited about this.  
**Translation:** 

**[3164.52s] English:** What kind of data augmentation is useful for that non-contrastive learning method?  
**Translation:** Vocabulary: augmentation: 增强

**[3170.24s] English:** Are we talking about that, or does that not matter much?  
**Translation:** 

**[3172.64s] English:** It seems like a very important part of the step.  
**Translation:** 

**[3175.72s] English:** Yeah.  
**Translation:** 

**[3176.26s] English:** How do you generate the images?  
**Translation:** 

**[3177.60s] English:** They're similar, but sufficiently different.  
**Translation:** 

**[3179.66s] English:** Yeah, that's right.  
**Translation:** Vocabulary: sufficiently: 足够地

**[3180.24s] English:** It's an important step, and it's also an annoying step.  
**Translation:** 

**[3182.34s] English:** Because you need to have that knowledge of what data augmentation you can do.  
**Translation:** 

**[3186.76s] English:** That do not change the nature of the object.  
**Translation:** 

**[3190.50s] English:** And so, the standard scenario,  
**Translation:** Vocabulary: scenario: 情景

**[3193.18s] English:** Which a lot of people working in this area are using.  
**Translation:** 

**[3195.42s] English:** Is it the type of distortion you're using?  
**Translation:** Vocabulary: distortion: 扭曲

**[3199.86s] English:** So, basically, you do geometric distortion.  
**Translation:** 

**[3202.12s] English:** So, one basically just shifts the image a little bit.  
**Translation:** Vocabulary: geometric: 几何; shifts: 移动

**[3204.24s] English:** It's called cropping.  
**Translation:** 

**[3205.06s] English:** Another one kind of changes the scale a little bit.  
**Translation:** Vocabulary: cropping: 裁剪

**[3207.76s] English:** Another one kind of rotates it.  
**Translation:** 

**[3209.14s] English:** Another one changes the colors.  
**Translation:** Vocabulary: rotates: 旋转

**[3210.70s] English:** You know, you can do a shift in color balance, or something like that.  
**Translation:** 

**[3214.96s] English:** Saturation.  
**Translation:** 

**[3215.76s] English:** Another one sort of blurs it.  
**Translation:** 

**[3217.10s] English:** Another one adds noise.  
**Translation:** 

**[3218.10s] English:** So, you have a catalog of kind of standard things.  
**Translation:** 

**[3221.10s] English:** And people try to use the same ones for different algorithms so that they can compare.  
**Translation:** Vocabulary: catalog: 目录

**[3225.88s] English:** But some algorithms, particularly self-supervised ones, can deal with much bigger,  
**Translation:** 

**[3230.60s] English:** Like more aggressive data augmentation, and some don't.  
**Translation:** 

**[3233.50s] English:** So, that kind of makes the whole thing difficult.  
**Translation:** 

**[3236.32s] English:** But that's the kind of difference.  
**Translation:** 

**[3237.46s] English:** That's the kind of distortion we're talking about.  
**Translation:** 

**[3238.82s] English:** And that's...  
**Translation:** 

**[3240.00s] English:** So, you train with those distortions.  
**Translation:** 

**[3243.56s] English:** And then you chop off the last layer.  
**Translation:** 

**[3247.30s] English:** Or a couple layers of the network,  
**Translation:** 

**[3251.14s] English:** And you use the representation as input to a classifier.  
**Translation:** 

**[3253.58s] English:** You train the classifier on ImageNet, let's say,  
**Translation:** 

**[3257.64s] English:** Or whatever, and measure the performance.  
**Translation:** 

**[3260.54s] English:** And interestingly enough,  
**Translation:** 

**[3263.12s] English:** The methods that are really good.  
**Translation:** 

**[3264.42s] English:** At eliminating the information that is irrelevant,  
**Translation:** 

**[3266.84s] English:** Which is the distortion between those images?  
**Translation:** Vocabulary: irrelevant: 无关的

**[3270.00s] English:** Do a good job at eliminating it.  
**Translation:** 

**[3272.38s] English:** And as a consequence, you cannot use.  
**Translation:** Vocabulary: cannot: 不能

**[3274.96s] English:** The representations in those systems.  
**Translation:** 

**[3277.20s] English:** For things like object detection and localization,  
**Translation:** Vocabulary: detection: 检测; representations: 表示

**[3279.88s] English:** Because that information is gone.  
**Translation:** 

**[3282.60s] English:** So, the type of data augmentation you need to do...  
**Translation:** Vocabulary: augmentation: 增加

**[3284.72s] English:** Depends on the task you want, eventually,  
**Translation:** 

**[3287.20s] English:** The system to solve.  
**Translation:** 

**[3288.64s] English:** And the type of data augmentation,  
**Translation:** 

**[3290.68s] English:** Standard data augmentation that we use today,  
**Translation:** 

**[3292.54s] English:** Are only appropriate for object recognition.  
**Translation:** 

**[3294.68s] English:** For image classification.  
**Translation:** Vocabulary: classification: 类别识别

**[3296.02s] English:** They're not appropriate for things like:  
**Translation:** 

**[3297.72s] English:** Can you help me out understand?  
**Translation:** 

**[3299.04s] English:** What does WideLog do?  
**Translation:** 

**[3300.00s] English:** The localization?  
**Translation:** 

**[3300.84s] English:** So, you're saying it's just not good at the negative.  
**Translation:** 

**[3303.78s] English:** Like at classifying the negative,  
**Translation:** 

**[3305.48s] English:** So, that's why it can't be used for localization?  
**Translation:** 

**[3307.96s] English:** No, it's just that you train the system.  
**Translation:** 

**[3310.38s] English:** You know, you give it an image,  
**Translation:** 

**[3312.40s] English:** And then you give it the same image, shifted and scaled.  
**Translation:** Vocabulary: shifted: 移动后的

**[3315.00s] English:** And you tell it that's the same image.  
**Translation:** 

**[3317.44s] English:** So the system is trained to eliminate  
**Translation:** 

**[3319.70s] English:** The information about position and size.  
**Translation:** 

**[3322.08s] English:** So now, and now you want to use that?  
**Translation:** 

**[3324.80s] English:** To figure out where an object is and what size it is.  
**Translation:** 

**[3327.76s] English:** Like a bounding box, they'd be able to actually...  
**Translation:** Vocabulary: bounding: 包围框

**[3330.00s] English:** Okay, it can still find the object in the image, but it's just not very good at finding the exact boundaries of that object.  
**Translation:** 

**[3337.36s] English:** Interesting; which, you know, is an interesting sort of philosophical question.  
**Translation:** Vocabulary: philosophical: 哲学上的

**[3343.52s] English:** How important is object localization, anyway?  
**Translation:** 

**[3346.82s] English:** We're like obsessed with measuring image segmentation, obsessed with knowing the boundaries of objects perfectly.  
**Translation:** Vocabulary: obsessed: 着迷; segmentation: 分割

**[3354.62s] English:** When, arguably, that's not really that...  
**Translation:** 

**[3360.00s] English:** Essential to understanding, what are the contents of the scene? On the other hand, I think evolutionarily,  
**Translation:** Vocabulary: contents: 内容; evolutionarily: 进化地

**[3365.76s] English:** The first vision systems in animals were basically all about localization; very little about anything else.  
**Translation:** 

**[3370.80s] English:** Recognition, and in the human brain, you have two separate pathways for recognizing the nature  
**Translation:** Vocabulary: pathways: 识别路径

**[3378.40s] English:** Of a scene or an object, and localizing objects, so you use the first pathway called the Eventual Pathway.  
**Translation:** 

**[3385.20s] English:** For, you know, telling what you're looking at, the other path with the dorsal pathway is used.  
**Translation:** Vocabulary: dorsal: 背侧; eventual: 最终的; pathway: 通路

**[3390.88s] English:** For navigation, for grasping, for everything else, and you know, basically a lot of the things you.  
**Translation:** 

**[3395.76s] English:** The need for survival involves localization and detection, which can be achieved through similarity learning or contrastive learning.  
**Translation:** Vocabulary: detection: 检测; grasping: 抓取; navigation: 导航; similarity: 相似性

**[3404.96s] English:** Are these non-contrastive methods the same as understanding something just because you know?  
**Translation:** 

**[3409.76s] English:** Does a distorted cat image mean the same as a non-distorted cat image? Does that mean you understand what it means to?  
**Translation:** Vocabulary: distorted: 变形的

**[3415.20s] English:** Be a cat, to some extent. I mean, it's a superficial understanding, obviously, but like, what is the  
**Translation:** 

**[3420.72s] English:** Ceiling of this method, do you think this is just one trick on the path to doing self-supervised?  
**Translation:** Vocabulary: ceiling: 上限; superficial: 表面的

**[3426.88s] English:** Learning, can we go really far? I think we can go really far. So, if we figure out how to,...  
**Translation:** 

**[3434.40s] English:** Uh, use techniques of that type, perhaps very different, but you know, the same nature to.  
**Translation:** 

**[3440.32s] English:** Train a system from video to do video prediction essentially.  
**Translation:** 

**[3445.76s] English:** I think we'll have a path, um, you know, towards, you know, I wouldn't say unlimited, but but a  
**Translation:** Vocabulary: unlimited: 无限制的

**[3451.92s] English:** Path towards some level of, you know, physical common sense in machines, and I also think,  
**Translation:** 

**[3459.20s] English:** That, um, ability to learn how the world works from a sort of high-throughput channel, like,  
**Translation:** 

**[3468.08s] English:** Vision is a necessary step toward sort of real artificial intelligence.  
**Translation:** 

**[3475.20s] English:** In other words, I believe in grounded intelligence; I don't think we can train a machine to  
**Translation:** 

**[3480.00s] English:** Intelligent purely from text, because I think the amount of information about the world that's  
**Translation:** 

**[3484.96s] English:** Contained in the text is tiny compared to what we need to know. So, for example, let's say you know.  
**Translation:** 

**[3493.76s] English:** People have attempted to do this for 30 years, right? The Psych project and things like that, right?  
**Translation:** 

**[3498.32s] English:** Of basically kind of writing down all the facts that are known, and hoping that some sort of pattern will emerge.  
**Translation:** Vocabulary: psych: 心理学

**[3503.52s] English:** Common sense will emerge, I think, but it's basically hopeless. Let me take an example: you take an  
**Translation:** 

**[3508.64s] English:** Object, I describe a situation to you. I take an object, I put it on the table, and I push the table.  
**Translation:** 

**[3514.80s] English:** It's completely obvious to you that the object will be pushed with the table.  
**Translation:** 

**[3518.56s] English:** Right, because it's sitting there, on it, there's no text in the world I believe that explains this.  
**Translation:** 

**[3524.96s] English:** And so, if you train a machine as powerful as it could be, you know, GPT-5000.  
**Translation:** 

**[3532.64s] English:** Or, whatever it is, it's never going to learn about this.  
**Translation:** 

**[3537.04s] English:** That information is just never.  
**Translation:** 

**[3539.04s] English:** Not present in any text, well, the question like with the psych project: the dream. I think.  
**Translation:** 

**[3543.92s] English:** Is to have, like, 10 million facts like that, which give you a head start, like a parent.  
**Translation:** 

**[3554.00s] English:** Guiding you now, we humans don't need a parent to tell us that the table will move. Sorry, the  
**Translation:** 

**[3559.52s] English:** Smartphone will move with the table, but we get a lot of guidance in other ways, so it's possible.  
**Translation:** 

**[3566.48s] English:** That we can give it a quick shortcut, what about the employee rate? Here's to the table, right? So,  
**Translation:** Vocabulary: shortcut: 捷径

**[3568.40s] English:** And what about a cat?  
**Translation:** 

**[3569.38s] English:** A cat knows that.  
**Translation:** 

**[3571.06s] English:** No, but they evolved.  
**Translation:** 

**[3573.08s] English:** No, they learn like us.  
**Translation:** Vocabulary: evolved: 进化

**[3575.86s] English:** Sorry, the physics of stuff?  
**Translation:** 

**[3577.32s] English:** Yeah.  
**Translation:** 

**[3578.90s] English:** Well, yeah, so you're saying it's—  
**Translation:** 

**[3582.42s] English:** So, you're putting a lot of intelligence on the nurture side, not the nature.  
**Translation:** 

**[3587.12s] English:** Yeah.  
**Translation:** 

**[3587.28s] English:** Because we seem to have—  
**Translation:** 

**[3589.28s] English:** There's a very inefficient, arguably, process of evolution.  
**Translation:** 

**[3593.50s] English:** That got us from bacteria to who we are today.  
**Translation:** Vocabulary: arguably: 可能地说; bacteria: 细菌; inefficient: 低效的

**[3596.70s] English:** Okay, started at the bottom, now we're here.  
**Translation:** 

**[3600.00s] English:** So, the question is: How fundamental is that to the nature of the whole hardware?  
**Translation:** 

**[3608.50s] English:** And then, is there any way to shortcut it if it's fundamental?  
**Translation:** 

**[3612.38s] English:** If it's not, most of the intelligence we've been talking about is mostly nurture and mostly trained.  
**Translation:** Vocabulary: nurture: 培养

**[3618.78s] English:** We figure it out by observing the world.  
**Translation:** 

**[3620.32s] English:** We can form that big, beautiful, sexy background model that you're talking about just by sitting there.  
**Translation:** 

**[3627.02s] English:** Then, okay, then you need to consider that it might be all supervised learning all the way down.  
**Translation:** 

**[3637.86s] English:** It's all supervised learning, sorry.  
**Translation:** Vocabulary: supervised: 监督学习

**[3638.98s] English:** Whatever it is that makes human intelligence different from other animals—well, you know, a lot of people think it's language and logical reasoning and this kind of stuff.  
**Translation:** 

**[3648.32s] English:** It cannot be that complicated, because it only popped up in the last million years.  
**Translation:** Vocabulary: cannot: 不可能

**[3653.96s] English:** And, you know, it only involves.  
**Translation:** 

**[3657.02s] English:** You know, less than 1% of our genome might be what makes the difference between the human genome and chimps or whatever.  
**Translation:** Vocabulary: chimps: 黑猩猩; genome: 基因组

**[3663.28s] English:** So, it can't be that complicated.  
**Translation:** 

**[3666.52s] English:** You know, it can't be that fundamental.  
**Translation:** 

**[3667.90s] English:** I mean, most of the complicated stuff already exists in cats and dogs, and, you know, certainly in non-human primates.  
**Translation:** 

**[3677.00s] English:** Yeah, that little thing with humans might be just something about social interaction and ability to maintain ideas across, like, a collective of people.  
**Translation:** Vocabulary: primates: 灵长类动物

**[3687.02s] English:** It sounds very dramatic and very impressive, but it probably isn't, mechanistically speaking.  
**Translation:** 

**[3693.32s] English:** It is, but we're not there yet.  
**Translation:** Vocabulary: mechanistically: 机械地

**[3694.66s] English:** Like, you know, we have—I mean, this is number 634 on the list of problems we have to solve, you know.  
**Translation:** 

**[3703.38s] English:** So, basic physics of the world is number one.  
**Translation:** 

**[3706.88s] English:** What do you think about data augmentation? Just a quick tangent.  
**Translation:** 

**[3711.62s] English:** So, a lot of it is hard-coded versus learned.  
**Translation:** Vocabulary: augmentation: 数据增强

**[3717.02s] English:** Do you have any intuition that maybe?  
**Translation:** 

**[3720.00s] English:** There could be some weird data augmentation, like generative-type data augmentation, like  
**Translation:** Vocabulary: intuition: 直觉

**[3726.28s] English:** Doing something weird to images, which then improves the similarity learning process.  
**Translation:** 

**[3732.80s] English:** So, not just kind of dumb and simple distortions, but by you shaking your head and just saying that.  
**Translation:** Vocabulary: distortions: 扭曲; similarity: 相似性

**[3738.88s] English:** Even simple distortions are enough, I think. No, I think data augmentation is a temporarily necessary solution.  
**Translation:** 

**[3744.42s] English:** Evil, so what people are working on now is two things: one is the type of self-supervised  
**Translation:** Vocabulary: temporarily: 暂时

**[3751.60s] English:** Learning is like trying to translate the type of self-supervised learning people use in language.  
**Translation:** 

**[3756.64s] English:** Translating these two images, which is basically a denoising autoencoder method, right? So, you see...  
**Translation:** Vocabulary: autoencoder: 自动编码器; denoising: 去噪; translating: 翻译

**[3762.36s] English:** Take an image, you block and mask some parts of it, and then you train some giant neural networks.  
**Translation:** 

**[3769.32s] English:** Net, we need to reconstruct the parts that are missing, and until  
**Translation:** Vocabulary: neural: 神经元; reconstruct: 重建

**[3774.28s] English:** Until  
**Translation:** 

**[3774.40s] English:** Very recently, there were no working methods for that; all the autoencoder types.  
**Translation:** 

**[3780.24s] English:** Methods for images weren't producing very good representations, but there's a paper now coming.  
**Translation:** 

**[3784.64s] English:** Out of the fair group in Menlo Park, that actually works very well, so that doesn't.  
**Translation:** Vocabulary: menlo: Men洛; representations: 表现

**[3791.14s] English:** Require data augmentation that requires only masking, okay? Only masking for images, okay.  
**Translation:** 

**[3798.44s] English:** Right, so you mask part of the image and you train a system which you know, in this case, is a  
**Translation:** Vocabulary: augmentation: 增加; masking: 遮罩

**[3803.98s] English:** Transformer.  
**Translation:** 

**[3804.26s] English:** Because you can represent the image as non-overlapping using a transformer.  
**Translation:** 

**[3810.36s] English:** Patches, so it's easy to mask patches and things like that, okay. Then my question transfers to that.  
**Translation:** 

**[3815.24s] English:** The problem, then, is that masking should not be limited to squares or rectangles. So, it doesn't matter what shape it is.  
**Translation:** Vocabulary: patches: 补丁; rectangles: 矩形; transfers: 转移

**[3820.76s] English:** Like, you know, I think we're gonna come up, probably in the future, with sort of ways to  
**Translation:** 

**[3826.74s] English:** Mask that are you know kind of random, essentially. Well, I mean, they are random already, but no, no, but.  
**Translation:** 

**[3833.48s] English:** Like something.  
**Translation:** 

**[3834.14s] English:** That's challenging, like optimally challenging, so like  
**Translation:** Vocabulary: optimally: 最优化地

**[3840.00s] English:** Mean, maybe it's a metaphor that doesn't apply, but you're; it seems like there's  
**Translation:** 

**[3844.56s] English:** An data augmentation or masking technique involves an interactive element with it, like  
**Translation:** Vocabulary: interactive: 交互式; metaphor: 比喻

**[3849.96s] English:** You're almost like playing with an image, yeah, and it's like the way we play.  
**Translation:** 

**[3854.10s] English:** With an image in our minds, now it's like dropout; it's like boson machine training.  
**Translation:** Vocabulary: boson: 玻色子; dropout: 丢层

**[3857.94s] English:** You know, every time you see a percept, you can also...  
**Translation:** 

**[3865.20s] English:** Can we perturb it in some way, and then the principle of the training procedure?  
**Translation:** Vocabulary: percept: 感知; perturb: 扰乱

**[3870.70s] English:** Is to minimize the difference between the output or the representation and the target.  
**Translation:** 

**[3875.70s] English:** The clean version and the corrupted version, essentially, and you can do  
**Translation:** Vocabulary: corrupted: 损坏的

**[3881.22s] English:** This is happening in real time, right? So you know, Boson machines work like this, right?  
**Translation:** 

**[3884.38s] English:** You show it a percept, and you tell the machine that's a good combination of.  
**Translation:** 

**[3888.72s] English:** Activities or your input neurons, and then you either  
**Translation:** 

**[3895.20s] English:** Let them go their merry way without clamping them to values, or you only do.  
**Translation:** Vocabulary: clamping: 固定; neurons: 神经元

**[3900.60s] English:** This with a subset, yeah, and what you're doing is training the system so  
**Translation:** 

**[3904.76s] English:** That the stable state of the entire network is the same, regardless of  
**Translation:** 

**[3909.16s] English:** Whether it sees the entire input or whether it sees only part of it, you know.  
**Translation:** 

**[3914.04s] English:** Denoising autoencoder method is basically the same thing, right? You're  
**Translation:** Vocabulary: autoencoder: 自动编码器; denoising: 去噪

**[3917.16s] English:** You're training a system to reproduce the input, the complete inputs, and  
**Translation:** 

**[3920.54s] English:** Filling the blanks, regardless of which parts are missing, and that's  
**Translation:** Vocabulary: inputs: 输入; reproduce: 复制

**[3924.32s] English:** Really, the underlying principle of the system.  
**Translation:** 

**[3925.20s] English:** And you could imagine, sort of, even in the brain, some sort of neural principle.  
**Translation:** Vocabulary: neural: 神经的

**[3929.34s] English:** Where you know, neurons are going to oscillate, right? So they take their activity.  
**Translation:** 

**[3934.54s] English:** And then, temporarily, they kind of shut off, you know, to force the rest of the  
**Translation:** Vocabulary: oscillate: 振荡; temporarily: 暂时

**[3939.02s] English:** System to basically reconstruct the input without their help, you know, and  
**Translation:** 

**[3945.36s] English:** And I mean, you can imagine—you know, possibly, you know, more or less.  
**Translation:** Vocabulary: reconstruct: 重新构建

**[3949.50s] English:** Biologically plausible processes.  
**Translation:** 

**[3950.96s] English:** Something like that, and I guess with this denoising autoencoder and  
**Translation:** Vocabulary: biologically: 生物学上; plausible: 合乎情理的

**[3955.20s] English:** Masking and data augmentation: you don't have to worry about being super.  
**Translation:** 

**[3960.00s] English:** Efficient, you can just do as much as you want, yeah, and get better over time. Because I was thinking...  
**Translation:** Vocabulary: augmentation: 增强; masking: 遮掩

**[3966.72s] English:** Like you might want to be clever about the way you do all these procedures, you know, but that's only  
**Translation:** 

**[3973.84s] English:** It's somehow costly to do every iteration, but it's not really that bad. Maybe and then there is you.  
**Translation:** Vocabulary: costly: 昂贵; iteration: 迭代

**[3980.96s] English:** Know, data augmentation without explicit data augmentation is data augmentation by waiting.  
**Translation:** 

**[3985.44s] English:** Which is, you know, the sort of video prediction thing where you're observing a video clip.  
**Translation:** Vocabulary: explicit: 明确的

**[3991.36s] English:** Observing the continuation of that video clip, and trying to learn from it.  
**Translation:** 

**[3997.04s] English:** Representation using those joint embedding architectures, in such a way that the representation,...  
**Translation:** Vocabulary: continuation: 延续; embedding: 嵌入

**[4001.76s] English:** Of the future clip is easily predictable from the representation of the observed clip.  
**Translation:** 

**[4008.48s] English:** Do you think YouTube has enough raw data from which to learn how to be a cat?  
**Translation:** Vocabulary: predictable: 可预测的

**[4016.24s] English:** I think so. So, the amount of data is not the constraint; no, it would require some selection.  
**Translation:** 

**[4023.12s] English:** I think, with the right type of data, you might avoid going down that path.  
**Translation:** Vocabulary: constraint: 限制

**[4029.12s] English:** Rabbit hole of just cat videos; that might make you need to watch some lectures or something.  
**Translation:** 

**[4034.48s] English:** No, you wouldn't. How meta would that be if it watched lectures about intelligence and  
**Translation:** 

**[4041.36s] English:** Then, he learns by watching your lectures at NYU and learns from that how to.  
**Translation:** 

**[4045.44s] English:** Be intelligent, I don't think there would be enough. What's your um, do you find multi-modal learning?  
**Translation:** 

**[4052.72s] English:** Interesting, we've been talking about visual language like combining those together, maybe.  
**Translation:** 

**[4056.72s] English:** Audio: All those kinds of things—there are a lot of things that I find interesting in the short term.  
**Translation:** 

**[4061.04s] English:** But they are not addressing the important problem that I think are really the big challenges, so I  
**Translation:** 

**[4066.88s] English:** Think you know things like multitasking, learning, continual learning—uh, you know, adversarial issues.  
**Translation:** Vocabulary: adversarial: 对抗性的; continual: 持续的; multitasking: 多任务处理

**[4074.24s] English:** I mean, those have you known, really important to you, yeah? Thank you very much. That's really interesting.  
**Translation:** 

**[4074.32s] English:** I mean, those have you known, really important to you, yeah? Thank you very much. That's really  
**Translation:** 

**[4075.36s] English:** Great practical interests in the relatively short term, possibly.  
**Translation:** 

**[4080.00s] English:** But I don't think they're fundamental, you know. Active learning, even to some extent,  
**Translation:** 

**[4083.32s] English:** Reinforcement learning.  
**Translation:** 

**[4084.32s] English:** I think those things will become either obsolete or useless, or easy once we figure out how.  
**Translation:** Vocabulary: obsolete: 过时的

**[4093.12s] English:** To do self-supervised representation learning or learning predictive world models.  
**Translation:** 

**[4099.42s] English:** And so I think that's what the entire community should be focusing on.  
**Translation:** Vocabulary: predictive: 预测性的

**[4104.50s] English:** At least people who are interested in fundamental questions or, you know, really  
**Translation:** 

**[4107.42s] English:** Kind of pushing the envelope of AI toward the next stage.  
**Translation:** 

**[4110.66s] English:** But of course, there's a huge amount of very interesting work to do.  
**Translation:** 

**[4114.30s] English:** In sort-of practical questions that have, you know, short-term impact.  
**Translation:** 

**[4117.66s] English:** Well, you know, it's difficult to talk about the temporal scale because all of human  
**Translation:** 

**[4123.62s] English:** Civilization will eventually be destroyed because the Sun will die out.  
**Translation:** Vocabulary: temporal: 时间的

**[4128.66s] English:** And even if Elon Musk is successful, multi-planetary colonization across the galaxy, eventually,...  
**Translation:** 

**[4135.52s] English:** The entirety of it will just become obsolete.  
**Translation:** Vocabulary: colonization: 殖民; entirety: 全部; galaxy: 星系

**[4137.40s] English:** It's going to take a while, though.  
**Translation:** 

**[4142.72s] English:** But what I'm saying is that then logic can be used to say it's all meaningless.  
**Translation:** Vocabulary: meaningless: 无意义的

**[4147.38s] English:** I'm saying all that to say that multitask learning might be what you're calling practical.  
**Translation:** 

**[4155.38s] English:** Or, pragmatic, or whatever.  
**Translation:** Vocabulary: multitask: 多任务; pragmatic: 实用的

**[4157.50s] English:** That might be the thing that achieves something very akin to intelligence while we're trying.  
**Translation:** 

**[4163.84s] English:** To solve the more general problem of self-supervision.  
**Translation:** 

**[4166.64s] English:** The problem of self-supervised learning of background knowledge.  
**Translation:** 

**[4169.58s] English:** So, the reason I bring that up: maybe one way to ask that question, I've been very impressed,...  
**Translation:** 

**[4173.98s] English:** By what the Tesla Autopilot team is doing.  
**Translation:** 

**[4176.02s] English:** I don't know if you've had any chance to glance at this particular example of multitasking.  
**Translation:** Vocabulary: multitasking: 多任务处理

**[4181.20s] English:** Learning where they're literally taking the problem, like, I don't know, Charles Darwin.  
**Translation:** 

**[4186.68s] English:** Starts studying animals.  
**Translation:** Vocabulary: darwin: 达尔文

**[4189.04s] English:** They're studying the problem of driving and asking: okay, what are all the things you  
**Translation:** 

**[4193.40s] English:** Have to perceive?  
**Translation:** Vocabulary: perceive: 感知

**[4195.42s] English:** And the way they do it.  
**Translation:** 

**[4196.08s] English:** They're studying the problem of driving and asking: okay, what are all the things you have to perceive?  
**Translation:** 

**[4196.64s] English:** And the way they're solving it is one, there's an ontology where you're bringing that in.  
**Translation:** 

**[4200.00s] English:** Table, so you're formulating a bunch of different tasks; it's like over 100 tasks or something like that.  
**Translation:** Vocabulary: ontology: 本体论

**[4204.00s] English:** That they're involved in driving, and then deploying it, and getting data back.  
**Translation:** 

**[4208.72s] English:** From people who run into trouble and they're trying to figure out: do we add tasks, or do we like?  
**Translation:** Vocabulary: deploying: 部署

**[4213.58s] English:** We focus on each individual task separately, sure. In fact, I would say I'll classify  
**Translation:** 

**[4218.82s] English:** Andre Kaparithi's talking to is so one was about doors, and the other one was about how much ImageNet.  
**Translation:** 

**[4224.14s] English:** Sucks; he kept going back and forth on those two topics. Which ImageNet, sucks—meaning, you can't  
**Translation:** 

**[4231.32s] English:** Just use a single benchmark. There's no need for a giant suite of benchmarks.  
**Translation:** Vocabulary: benchmark: 参考标准

**[4237.80s] English:** To understand how well your system actually works, I agree with him; I mean, he's a very sensible guy.  
**Translation:** 

**[4242.46s] English:** Guy, um, now okay, it's very clear that if you're faced with an engineering problem that  
**Translation:** Vocabulary: sensible: 理智的

**[4249.76s] English:** You need to solve it in a relatively short time, particularly if you have it almost.  
**Translation:** 

**[4253.98s] English:** Breathing down your neck, you're gonna have to take shortcuts, right? You might think,...  
**Translation:** 

**[4259.02s] English:** About the fact that the right thing to do and the long-term solution involves, you know,  
**Translation:** 

**[4264.46s] English:** Some fancy self-supervision, but you know, you're almost breathing down your neck, uh, and  
**Translation:** 

**[4270.54s] English:** You know, this involves human lives, and so you have to basically just do what needs to be done.  
**Translation:** 

**[4277.58s] English:** Systematic engineering, and you know, fine-tuning, refinements, and trial and error.  
**Translation:** Vocabulary: refinements: 精细调整

**[4283.98s] English:** And, and all that stuff—um, there's nothing wrong with that. That's called engineering, that's.  
**Translation:** 

**[4288.70s] English:** Called, you know, uh, putting technology out in the world, um, and you have to kind of  
**Translation:** 

**[4297.74s] English:** Ironclad it before you do this, you know, um, so much for those grand ideas and...  
**Translation:** 

**[4305.42s] English:** Principles, um, but you know, I'm placing myself, sort of, you know, upstream of the...  
**Translation:** Vocabulary: ironclad: 坚如磐石; upstream: 上游

**[4313.98s] English:** Screen, or quite a bit upstream of this, your play; don't think about Platonic forms, your Platonic.  
**Translation:** 

**[4320.00s] English:** Eventually, I want that stuff to get used, but it's okay if it takes five or ten years.  
**Translation:** Vocabulary: platonic: 理念的

**[4326.62s] English:** Years for the community to realize this is the right thing to do, I've I've done.  
**Translation:** 

**[4330.08s] English:** This is before it's been the case before that, you know, I've made that case. I mean.  
**Translation:** 

**[4334.64s] English:** If you look back in the mid-2000s, for example, and you ask yourself the  
**Translation:** 

**[4338.62s] English:** Question: Okay, I want to recognize cars or faces, or whatever. You know, I can use...  
**Translation:** 

**[4344.96s] English:** Convolutional nets, so I can use a more conventional kind of computer vision.  
**Translation:** 

**[4349.08s] English:** Techniques you know, using interest point detectors or shift density.  
**Translation:** Vocabulary: conventional: 传统的; convolutional: 卷积的; density: 密度; detectors: 检测器

**[4353.04s] English:** Features, and you know, sticking an SVM on top. At that time, the datasets were so  
**Translation:** 

**[4357.02s] English:** Small-scale methods that use more engineering tend to work better than those.  
**Translation:** Vocabulary: datasets: 数据集; sticking: 添加

**[4363.12s] English:** Confidence: There's just not enough data for comments, and comments were...  
**Translation:** 

**[4366.78s] English:** Little, a little, was slow with the kind of hardware that was available at the time.  
**Translation:** 

**[4369.84s] English:** And there was a sea change when, basically, when you know, data sets  
**Translation:** 

**[4376.00s] English:** Became bigger, and as GPUs became available, that's  
**Translation:** 

**[4378.96s] English:** What I'm talking about.  
**Translation:** 

**[4379.08s] English:** You know, the two main factors that basically made people  
**Translation:** 

**[4384.30s] English:** Change their minds, and you can look at the history of like  
**Translation:** 

**[4391.98s] English:** All sub-branches of AI or pattern recognition, and there's a similar  
**Translation:** 

**[4397.50s] English:** Trajectory followed by techniques, where people start by, you know, engineering the  
**Translation:** 

**[4402.78s] English:** Head out of it, you know—be it optical character recognition.  
**Translation:** Vocabulary: optical: 光学; trajectory: 轨迹

**[4409.08s] English:** Speech recognition, computer vision (like image recognition) in general, and natural language processing.  
**Translation:** 

**[4415.02s] English:** Understanding, like you know, translation things like that—right? You start to engineer the hell out of it.  
**Translation:** 

**[4419.28s] English:** Of it, you start to acquire all the knowledge, the prior knowledge you know about image formation.  
**Translation:** 

**[4424.68s] English:** About, you know, the shape of characters; about, you know, morphological operations; about, like,  
**Translation:** Vocabulary: morphological: 形态学的

**[4430.14s] English:** Feature extraction, Fourier transforms, you know, Vernicle moments, you know, whatever—right, people?  
**Translation:** 

**[4434.82s] English:** Have come up with thousands of ways of representing images so that they could be easily.  
**Translation:** Vocabulary: extraction: 特征提取; fourier: 傅里叶; transforms: 变换

**[4439.08s] English:** Uh, uh.  
**Translation:** 

**[4440.00s] English:** Classified afterwards. Same for speech recognition, right? It took decades, you know.  
**Translation:** 

**[4444.62s] English:** For people to figure out a good frontend to preprocess a speech signal so that,  
**Translation:** 

**[4450.32s] English:** Know, the information about what is being said is preserved, but most of the information,  
**Translation:** Vocabulary: frontend: 前端; preprocess: 预处理

**[4454.40s] English:** About the identity of the speaker is gone. You know, contextual coefficients or whatever.  
**Translation:** 

**[4461.38s] English:** Right? And for text, right? You do named entity recognition, and you parse, and you do  
**Translation:** Vocabulary: coefficients: 系数; parse: 解析

**[4469.38s] English:** Tagging of the parts of speech, and you do this sort of tree representation of clauses.  
**Translation:** 

**[4476.62s] English:** And all that stuff right before you can do anything. So that's how it starts, right?  
**Translation:** Vocabulary: clauses: 句子成分; tagging: 标注

**[4484.92s] English:** Just engineer the hell out of it. And then, you start having data, and maybe you have more.  
**Translation:** 

**[4490.38s] English:** Powerful computers. Maybe you know something about statistical learning. So, you start using.  
**Translation:** 

**[4494.06s] English:** Machine learning, and it's usually a small sliver on top of your kind of handcrafted  
**Translation:** 

**[4497.46s] English:** A system where, you know, you extract.  
**Translation:** Vocabulary: extract: 提取; handcrafted: 手工制作; sliver: 薄片

**[4499.38s] English:** Features by hand. Okay. And now, you know, nowadays, the standard way of doing this is  
**Translation:** 

**[4503.88s] English:** That you train the entire thing end-to-end with a deep learning system, and it learns,  
**Translation:** 

**[4506.88s] English:** Its own features, and, you know, speech recognition systems nowadays; OCR systems are completely  
**Translation:** 

**[4513.44s] English:** End-to-end. It's, you know, some giant neural net that takes raw waveforms and produces.  
**Translation:** Vocabulary: neural: 神经; waveforms: 波形

**[4519.54s] English:** A sequence of characters is coming out. And it's just a huge neural net, right? There's no,  
**Translation:** 

**[4523.62s] English:** You know, Markov models, there's no language model that is explicit, other than, you know,  
**Translation:** Vocabulary: explicit: 明确的; markov: 马尔可夫

**[4529.38s] English:** Trained in the sort of neural language model, if you want. Same for translation.  
**Translation:** 

**[4533.14s] English:** Same for all kinds of stuff. So you see this continuous evolution from, you know, less.  
**Translation:** 

**[4539.88s] English:** And less handcrafting and more and more learning. And I think, I mean, it's true in biology.  
**Translation:** 

**[4548.96s] English:** As well.  
**Translation:** Vocabulary: handcrafting: 手工制作

**[4549.96s] English:** So, I mean, we might disagree about this, maybe not in this one little piece at the  
**Translation:** 

**[4556.72s] English:** At the end, you mentioned active learning.  
**Translation:** 

**[4559.38s] English:** It's  
**Translation:** 

**[4560.00s] English:** It feels like active learning, which involves the selection of data and also the interactivity, needs to be part of this giant neural network.  
**Translation:** 

**[4566.86s] English:** You cannot just be an observer to do self-supervised learning.  
**Translation:** 

**[4569.62s] English:** Well, self-supervised learning is just a word, but whatever this giant stack of a neural network that's automatically learning, it feels...  
**Translation:** 

**[4580.78s] English:** My intuition is that you have to have a system—whether it's a physical robot or a digital one—that's interacting with the world and doing so in a flawed way, but improving over time.  
**Translation:** 

**[4596.54s] English:** In order to form self-supervised learning, you can't just give it a giant sea of data.  
**Translation:** Vocabulary: flawed: 有缺陷的; interacting: 互动; intuition: 直觉

**[4605.00s] English:** Okay, I agree and I disagree.  
**Translation:** 

**[4606.70s] English:** I agree, in the sense that I think...  
**Translation:** 

**[4610.00s] English:** I agree.  
**Translation:** 

**[4610.66s] English:** I agree.  
**Translation:** 

**[4610.76s] English:** I agree.  
**Translation:** 

**[4610.78s] English:** I agree in two ways.  
**Translation:** 

**[4612.06s] English:** The first way I agree is that, if you want—and you certainly need—a causal model of the world that allows you to predict the consequences of your actions, you need to take actions to train that model.  
**Translation:** 

**[4622.66s] English:** You need to be able to act in the world and see the effects for you to learn causal models of the world.  
**Translation:** Vocabulary: causal: 因果的

**[4628.36s] English:** So, that's not obvious because you can observe others.  
**Translation:** 

**[4631.52s] English:** You can observe others.  
**Translation:** 

**[4632.18s] English:** And you can infer that they're similar to you, and then you can learn from that.  
**Translation:** 

**[4635.86s] English:** Yeah, but then you have to kind of hardwire that part, mirror neurons and all that stuff.  
**Translation:** Vocabulary: hardwire: 固化; neurons: 神经元

**[4640.34s] English:** And it's not clear to me how you would do this in a machine.  
**Translation:** 

**[4644.62s] English:** So, I think the action part would be necessary for having causal models of the world.  
**Translation:** 

**[4653.08s] English:** The second reason it may be necessary, or at least more efficient, is that active learning basically targets the gaps in what you don't know.  
**Translation:** 

**[4665.02s] English:** There are obvious areas of uncertainty about your world.  
**Translation:** 

**[4670.06s] English:** And about how the world behaves.  
**Translation:** 

**[4673.06s] English:** And you can resolve this uncertainty by systematically exploring the part that you don't know.  
**Translation:** Vocabulary: behaves: 表现

**[4680.00s] English:** And if you know that you don't know, then you know it makes you curious — kind of.  
**Translation:** 

**[4683.32s] English:** Of course, let's look into situations that, and you know, across the animal world, the  
**Translation:** 

**[4689.30s] English:** Different species have different levels of curiosity, right? Yeah, depending on how.  
**Translation:** 

**[4694.40s] English:** They build right, so you know, cats and rats are incredibly curious, but dogs aren't so much.  
**Translation:** 

**[4699.26s] English:** Much means less, yeah? So it could be useful to have that kind of curiosity.  
**Translation:** 

**[4704.04s] English:** It would be useful, but curiosity just makes the process faster; it doesn't make the  
**Translation:** 

**[4707.56s] English:** Process exists, so what process is it that actively learns?  
**Translation:** 

**[4716.00s] English:** Learning makes it more efficient, and I'm asking that first question, you know.  
**Translation:** Vocabulary: actively: 积极地

**[4723.28s] English:** We haven't answered that question yet, so I worry about active.  
**Translation:** 

**[4726.40s] English:** Learning, once you ask this question, is the more fundamental question to ask, and if  
**Translation:** 

**[4731.50s] English:** Active learning or interaction increases the efficiency of the learning, see?  
**Translation:** 

**[4737.20s] English:** Sometimes  
**Translation:** 

**[4737.54s] English:** It becomes very different if the increase is several orders of magnitude.  
**Translation:** 

**[4742.82s] English:** Right, like that's true, but fundamentally it's still the same thing, and building up.  
**Translation:** Vocabulary: fundamentally: 本质上

**[4749.12s] English:** The intuition about how to construct in a self-supervised way to:  
**Translation:** 

**[4752.96s] English:** Background models: efficient or inefficient is the core problem.  
**Translation:** Vocabulary: inefficient: 不高效; intuition: 直觉

**[4758.78s] English:** Do you think about your show, Banjo's Talking, and all of its discussions about consciousness?  
**Translation:** 

**[4763.46s] English:** These kinds of concepts, okay. I don't know what consciousness is.  
**Translation:** Vocabulary: consciousness: 觉醒

**[4767.18s] English:** Okay, I don't know what consciousness is.  
**Translation:** 

**[4767.54s] English:** But it's a good opener, and to some extent, a lot of the things that are said.  
**Translation:** 

**[4774.44s] English:** About consciousness, remind me of the questions people were asking themselves.  
**Translation:** 

**[4778.40s] English:** In the 18th or 17th century, when they discovered how,  
**Translation:** 

**[4784.28s] English:** The eye works, and the fact is that the image at the back of the eye is upside down.  
**Translation:** 

**[4788.90s] English:** Right, because you have a lens, and so on, your retina forms an image.  
**Translation:** Vocabulary: retina: 视网膜; upside: 倒置的

**[4793.48s] English:** An image of the world, but it's upside down. How is it that you see right side up?  
**Translation:** 

**[4797.54s] English:** And you know, with what we know today,  
**Translation:** 

**[4800.00s] English:** Science, we realize this question doesn't make any sense or is kind of ridiculous.  
**Translation:** 

**[4805.54s] English:** Some way, right?  
**Translation:** 

**[4806.54s] English:** So, I think a lot of what is said about consciousness is of that nature.  
**Translation:** 

**[4809.10s] English:** Now, that said, there are a lot of really smart people for whom I have a lot of respect who  
**Translation:** 

**[4813.86s] English:** We are talking about this topic, people like David Chalmers, who is a colleague of mine.  
**Translation:** 

**[4817.28s] English:** At NYU.  
**Translation:** Vocabulary: chalmers: 查尔默斯; colleague: 同事

**[4819.68s] English:** I have kind of an unorthodox, folk, speculative hypothesis about consciousness.  
**Translation:** 

**[4829.32s] English:** So, we're talking about this idea of a world model, and I think our entire prefrontal cortex,  
**Translation:** Vocabulary: cortex: 大脑皮层; hypothesis: 假设; speculative: 推测性的; unorthodox: 非传统的

**[4835.46s] English:** Basically, it is the engine for our world model.  
**Translation:** 

**[4840.94s] English:** But when we are attending to a particular situation, we're focused on that situation.  
**Translation:** 

**[4846.18s] English:** We basically cannot attend to anything else.  
**Translation:** 

**[4848.74s] English:** And that seems to suggest that we basically have only one world-model engine in our prefrontal.  
**Translation:** 

**[4857.70s] English:** Cortex.  
**Translation:** 

**[4858.70s] English:** Okay.  
**Translation:** 

**[4859.32s] English:** So, that engine is configurable to the situation at hand.  
**Translation:** 

**[4862.72s] English:** So, we are building a box out of wood, or we are driving down the highway playing chess.  
**Translation:** Vocabulary: configurable: 可配置的

**[4869.70s] English:** We basically have a single model of the world that we configure into the situation at hand.  
**Translation:** 

**[4875.46s] English:** Which is why we can only attend to one task at a time.  
**Translation:** Vocabulary: configure: 设置

**[4879.30s] English:** Now, if there is a task that we do repeatedly, it goes from the sort of deliberate reasoning,...  
**Translation:** 

**[4885.88s] English:** Using a model of the world and prediction, and perhaps something like model predictive control.  
**Translation:** Vocabulary: deliberate: 深思熟虑的; predictive: 预测性的

**[4888.70s] English:** Which I was talking about earlier, it becomes something that is more subconscious and automatically happens.  
**Translation:** 

**[4894.50s] English:** So, I don't know if you've ever played against a chess grandmaster.  
**Translation:** Vocabulary: grandmaster: 特级大师; subconscious: 潜意识

**[4899.18s] English:** I get wiped out in 10 plays, right?  
**Translation:** 

**[4904.12s] English:** And I have to think about my move for 15 minutes, and the person in front of me, the grandmaster,...  
**Translation:** 

**[4912.70s] English:** Would just react within seconds, right?  
**Translation:** 

**[4916.58s] English:** He doesn't need to think about it.  
**Translation:** 

**[4918.58s] English:** That's become part of the subconscious.  
**Translation:** 

**[4920.00s] English:** Because it's basically just pattern recognition.  
**Translation:** 

**[4922.64s] English:** At this point.  
**Translation:** 

**[4924.76s] English:** The same is true for the first few hours of driving a car,  
**Translation:** 

**[4927.72s] English:** You're really attentive; you can't do anything else.  
**Translation:** 

**[4929.80s] English:** And then, after 20 to 30 hours of practice, 50 hours,  
**Translation:** Vocabulary: attentive: 专心的

**[4933.50s] English:** It's subconscious; you can talk to the person next to you.  
**Translation:** 

**[4935.72s] English:** Things like that, right?  
**Translation:** 

**[4937.04s] English:** Unless the situation becomes unpredictable,  
**Translation:** 

**[4939.06s] English:** And then you have to stop talking.  
**Translation:** Vocabulary: unpredictable: 无法预料的

**[4941.06s] English:** So, that suggests you only have one model in your head.  
**Translation:** 

**[4944.66s] English:** And it might suggest the idea that consciousness basically  
**Translation:** Vocabulary: consciousness: 醒觉状态

**[4948.34s] English:** Is the module that configures this world model of yours?  
**Translation:** 

**[4951.96s] English:** You need to have some sort of executive overseer.  
**Translation:** Vocabulary: configures: 配置; module: 模块; overseer: 监督者

**[4956.50s] English:** That configures your world model for the situation at hand.  
**Translation:** 

**[4960.60s] English:** And that leads to the really curious concept.  
**Translation:** 

**[4963.76s] English:** That consciousness is not a consequence.  
**Translation:** 

**[4966.04s] English:** Of the power of our minds, but of the limitation,...  
**Translation:** 

**[4968.66s] English:** Of our brains.  
**Translation:** 

**[4970.10s] English:** Because we have only one world model, we have to be conscious.  
**Translation:** 

**[4973.72s] English:** If we had as many world models as the situations we encounter,  
**Translation:** 

**[4978.34s] English:** Then we could do all of them simultaneously.  
**Translation:** Vocabulary: encounter: 遇到的情况

**[4980.74s] English:** And we wouldn't need this sort of executive control.  
**Translation:** 

**[4982.94s] English:** That is what we call consciousness.  
**Translation:** 

**[4984.52s] English:** Yeah, that's interesting.  
**Translation:** 

**[4985.36s] English:** And somehow, maybe that executive controller,  
**Translation:** 

**[4988.96s] English:** I mean, the hard problem of consciousness.  
**Translation:** 

**[4990.94s] English:** There's some kind of chemicals in biology.  
**Translation:** 

**[4992.86s] English:** That's creating a feeling, like it feels to experience.  
**Translation:** 

**[4996.76s] English:** Some of these things.  
**Translation:** 

**[4998.92s] English:** That's kind of a hard question: what the heck is that?  
**Translation:** 

**[5003.42s] English:** And why is that useful?  
**Translation:** 

**[5004.72s] English:** Maybe the more pragmatic question is,  
**Translation:** 

**[5006.18s] English:** Why is it useful to feel like?  
**Translation:** Vocabulary: pragmatic: 实用的

**[5008.34s] English:** This is really what you're experiencing, versus just  
**Translation:** 

**[5011.88s] English:** Like information being processed.  
**Translation:** Vocabulary: processed: 加工过的

**[5015.90s] English:** It could be just a very nice side effect of the way we evolved.  
**Translation:** 

**[5021.72s] English:** That it's just very useful to feel a sense of ownership.  
**Translation:** Vocabulary: evolved: 进化

**[5028.56s] English:** To the decisions you make, to the perceptions you form,  
**Translation:** 

**[5031.14s] English:** To the model you're trying to maintain.  
**Translation:** Vocabulary: perceptions: 认知

**[5033.12s] English:** Like you own this thing, and it's the only one you've got.  
**Translation:** 

**[5036.22s] English:** And if you lose it, it's going to really suck.  
**Translation:** 

**[5037.78s] English:** Yeah.  
**Translation:** 

**[5038.34s] English:** And so, you should really send.  
**Translation:** 

**[5040.00s] English:** The brain receives some signals about it. What ideas do you believe might be true?  
**Translation:** 

**[5047.00s] English:** Most, or at least many people, disagree with you, especially in the space of  
**Translation:** 

**[5052.24s] English:** Machine learning, well, depends on who you're talking about, but I think so—certainly.  
**Translation:** 

**[5057.40s] English:** There is a bunch of people who are nativist right who think that a lot of  
**Translation:** Vocabulary: nativist: 主张先天决定论的人

**[5062.00s] English:** The basic things about the world are kind of hardwired in our minds.  
**Translation:** 

**[5065.68s] English:** Things, like you know, the world is three-dimensional, for example.  
**Translation:** Vocabulary: hardwired: 天生具备的

**[5069.16s] English:** Hard-wired things, like you know, object permanence, is something that we learn.  
**Translation:** 

**[5073.74s] English:** You know, before the age of three months or so, or are we born with it, and there?  
**Translation:** Vocabulary: permanence: 持久性

**[5079.64s] English:** Are you know, very disagree? You know, white disagreement among the you know, a  
**Translation:** 

**[5083.44s] English:** Cognitive scientist: For this, I think those things are actually very simple to.  
**Translation:** Vocabulary: cognitive: 认知; disagreement: 不同意

**[5088.12s] English:** Learn, you know, is it the case that the oriented edge detectors in V1 are  
**Translation:** 

**[5094.30s] English:** Learned, or are they hard-wired? I think they are learned; they might be learned.  
**Translation:** Vocabulary: detectors: 检测器; oriented: 定向的

**[5097.84s] English:** Before both, because it's really  
**Translation:** 

**[5099.14s] English:** Easy to generate signals from the retina that actually will train edge detectors.  
**Translation:** Vocabulary: retina: 视网膜

**[5102.96s] English:** So, and again, those are things that can be learned within minutes of opening your.  
**Translation:** 

**[5108.98s] English:** Eyes right; I mean, you know, since the 1990s, we have algorithms that can learn.  
**Translation:** 

**[5114.40s] English:** Oriented edge detectors are completely unsupervised, with the equivalent of a  
**Translation:** 

**[5118.10s] English:** Few minutes of real time, so those things have to be learned. There's also  
**Translation:** Vocabulary: unsupervised: 无需监督的

**[5123.08s] English:** Those, you know, are the MIT experiments where you kind of plug the optical nerve in.  
**Translation:** 

**[5129.14s] English:** Baby ferret, right? And that or the toy becomes the visual cortex.  
**Translation:** Vocabulary: cortex: 皮层; experiments: 实验; ferret: 水貂; optical: 光学的

**[5132.16s] English:** Essentially, so you know, clearly there's running taking place there, so you know, I.  
**Translation:** 

**[5138.68s] English:** Think a lot of what people think are so basic that they need to be hard-wired, I  
**Translation:** 

**[5142.64s] English:** Think a lot of those things are learned because they are easy to run, Jesus, so.  
**Translation:** 

**[5146.38s] English:** You put a lot of value in the power of learning. What kinds of things do you?  
**Translation:** 

**[5150.90s] English:** Suspect: Might not be learned; is there something that could not be learned so?  
**Translation:** 

**[5156.18s] English:** Your intrinsic drives are not learned; they're not learned, and they're not learned.  
**Translation:** Vocabulary: intrinsic: 内在的

**[5157.02s] English:** There's something that could not be learned, so your intrinsic drives are not learned.  
**Translation:** 

**[5159.14s] English:** They're  
**Translation:** 

**[5160.00s] English:** Are the things that you know make humans, um, human, or make you know, cats different from dogs, right?  
**Translation:** 

**[5167.28s] English:** It's the basic drives that are kind of hardwired in our basal ganglia, um, I mean, there  
**Translation:** Vocabulary: basal: 底部的; ganglia: 神经节; hardwired: 固有的

**[5173.12s] English:** Are there people who are working on this kind of stuff that's called intrinsic motivation in the?  
**Translation:** 

**[5176.32s] English:** In the context of reinforcement learning, so these are objective functions where the reward doesn't  
**Translation:** Vocabulary: reinforcement: 强化

**[5180.80s] English:** Come from the external world; it's computed by your own brain, which computes  
**Translation:** 

**[5185.44s] English:** Whether you're happy or not, it measures your degree of comfort or discomfort, and...  
**Translation:** Vocabulary: computed: 计算得出

**[5194.48s] English:** Because it's your brain computing this, presumably it also knows how to estimate gradients of this, right?  
**Translation:** 

**[5198.64s] English:** So, um, it's easier to learn when your objective is intrinsic. Um, that has to  
**Translation:** Vocabulary: computing: 计算; estimate: 估计; gradients: 梯度; presumably: 大概

**[5207.84s] English:** Be hard-wired, uh, the critic that makes long-term predictions of the outcome, which is the eventual.  
**Translation:** 

**[5214.80s] English:** Result of this:  
**Translation:** Vocabulary: eventual: 最终的

**[5215.44s] English:** Is that learned, uh, and perception is learned, and your model of the world is learned, but let  
**Translation:** 

**[5221.28s] English:** Me, for example, take an instance of how the critic might be learned.  
**Translation:** Vocabulary: perception: 感知

**[5226.00s] English:** Right, if I come to you, uh, you know, I reach across the table and pinch your arm, right?  
**Translation:** 

**[5233.20s] English:** Complete surprise for you; you would not have expected this. I was expecting that the hotel, but...  
**Translation:** Vocabulary: pinch: 捏一下

**[5237.36s] English:** Yes, right. Let's say, for the sake of the story: Yes, um, okay, your basal ganglia is going to light up because  
**Translation:** 

**[5245.44s] English:** It's gonna hurt, right? Um, and now your model of the world includes the fact that.  
**Translation:** 

**[5250.96s] English:** I might pinch you if I approach, my uh, my don't trust humans, right? My hand to your arm, so.  
**Translation:** 

**[5258.24s] English:** If I try again, you're gonna recoil, and that's your critic.  
**Translation:** Vocabulary: recoil: 缩回

**[5262.00s] English:** Uh, your predictor of your ultimate pain, you know, system that predicts,  
**Translation:** 

**[5271.04s] English:** That something bad is going to happen, and you recoil right to avoid it. So, even that can be learned.  
**Translation:** Vocabulary: predictor: 预测器

**[5275.44s] English:** Is learned definitely; this is what allows you also to, you know, define sub-goals.  
**Translation:** 

**[5280.00s] English:** Right, so the fact that you know you're a schoolchild, you wake up in the morning.  
**Translation:** 

**[5285.94s] English:** And you go to school, and you know it's not because you necessarily like waking up.  
**Translation:** 

**[5291.46s] English:** Up early and going to school, but you know that there is a long-term objective.  
**Translation:** 

**[5294.62s] English:** You're trying to optimize, so Ernest Becker—I'm not sure if you're familiar.  
**Translation:** 

**[5297.82s] English:** With the philosopher, he wrote the book "Denial of Death," and his idea is that one  
**Translation:** Vocabulary: becker: 贝克; denial: 否认; ernest: 埃rn斯特; optimize: 优化

**[5302.36s] English:** Of the core motivations of human beings, our terror of death, our fear of death,...  
**Translation:** 

**[5306.40s] English:** That's what makes us unique. From cats, they are just surviving; they do not have.  
**Translation:** Vocabulary: motivations: 驱动力

**[5311.46s] English:** A deep, underwater like a cognizance of introspection that over the horizon is.  
**Translation:** 

**[5320.48s] English:** The end, and he says that I mean, there's a terror management theory that just all  
**Translation:** Vocabulary: cognizance: 知觉; introspection: 内省

**[5324.96s] English:** These psychological experiments that show, basically, this idea that all of  
**Translation:** 

**[5331.98s] English:** Human civilization: Everything we create is kind of trying to,  
**Translation:** Vocabulary: experiments: 实验

**[5336.18s] English:** Forget the idea that we are all human beings, and that we are all human beings.  
**Translation:** 

**[5336.38s] English:** Get it, even for a brief moment, that we're going to die. When do you  
**Translation:** 

**[5341.42s] English:** Think humans understand that they're going to die? Is it learned early on, too?  
**Translation:** 

**[5347.20s] English:** Like, I don't know at what point, I mean, it's a question—like, you know, at  
**Translation:** 

**[5352.98s] English:** What point do you realize that you know what death really is, and I think most...  
**Translation:** 

**[5357.14s] English:** People don't actually realize what death is, right? I mean, most people believe that  
**Translation:** 

**[5360.26s] English:** You go to heaven, or something, right? So, to push back on that, what Ernest...  
**Translation:** 

**[5364.82s] English:** Becker says, and  
**Translation:** 

**[5366.16s] English:** Um, Sheldon Solomon, all of those folks, and I find those ideas a little bit  
**Translation:** 

**[5370.86s] English:** Compelling is that there are moments in life, especially early in life, a lot of which are fun.  
**Translation:** Vocabulary: compelling: 有吸引力的

**[5374.96s] English:** Happens early in life, when you deeply experience the terror of.  
**Translation:** 

**[5382.26s] English:** This realization and all the things you think about regarding religion — all those  
**Translation:** Vocabulary: realization: 觉悟

**[5386.22s] English:** Kinds of things that would kind of make you think more, like teenage years and later.  
**Translation:** 

**[5389.90s] English:** We're talking about way earlier; no, it's like seven or eight years, something like that.  
**Translation:** 

**[5393.60s] English:** That, yeah, you realize  
**Translation:** 

**[5395.94s] English:** Holy crap, this is like the mystery the  
**Translation:** 

**[5400.00s] English:** Like, it's almost like you're a little prey, a little baby deer sitting in the darkness of the jungle or the woods, looking all around you.  
**Translation:** 

**[5408.08s] English:** There's darkness, full of terror.  
**Translation:** 

**[5409.60s] English:** I mean, that realization says, "Okay, I'm going to go back into the comfort of my mind where there is a deep meaning. Where there is a maybe—pretend I'm immortal in however way or however kind of idea I can construct—to help me understand that I'm immortal.  
**Translation:** 

**[5427.16s] English:** Religion helps with that.  
**Translation:** Vocabulary: immortal: 永生

**[5428.36s] English:** You can delude yourself in all kinds of ways, like losing yourself in the busyness of each day, having little goals in mind—all those kinds of things—to think that it's going to go on forever.  
**Translation:** 

**[5438.18s] English:** And you kind of know you're going to die, yeah, and it's going to be sad, but you don't really understand that you're going to die.  
**Translation:** Vocabulary: delude: 自我欺骗

**[5445.18s] English:** And so, that's their idea.  
**Translation:** 

**[5446.40s] English:** And I find that compelling, because it does seem to be a core, unique aspect of human nature that we're able to really understand that this life is fine.  
**Translation:** 

**[5458.36s] English:** That seems important.  
**Translation:** 

**[5460.90s] English:** There are a bunch of different things there.  
**Translation:** 

**[5462.30s] English:** So, first of all, I don't think there is a qualitative difference between us and cats in terms.  
**Translation:** 

**[5467.42s] English:** I think the difference is that we just have a better long-term ability to predict in the long term.  
**Translation:** Vocabulary: qualitative: 质量上的

**[5474.78s] English:** And so, we have a better understanding of other worlds' works.  
**Translation:** 

**[5477.38s] English:** So, we have a better understanding of the finiteness of life and things like that.  
**Translation:** Vocabulary: finiteness: 有限性

**[5481.00s] English:** So, we have a better planning engine than cats?  
**Translation:** 

**[5483.50s] English:** Yeah.  
**Translation:** 

**[5484.40s] English:** Okay.  
**Translation:** 

**[5485.52s] English:** What's the motivation for planning?  
**Translation:** 

**[5488.36s] English:** Well, I think it's just a side effect of the fact that we have a better planning engine, because it makes us, as I said, you know, the essence of intelligence is the ability to predict.  
**Translation:** 

**[5497.44s] English:** And so, because we're smarter, as a side effect, we also have this ability to kind of make predictions about our own future existence or lack thereof.  
**Translation:** Vocabulary: thereof: 其结果

**[5508.12s] English:** You say religion helps with that.  
**Translation:** 

**[5510.52s] English:** I think religion hurts, actually.  
**Translation:** 

**[5512.64s] English:** It makes people worry about, like, what's going to happen after their death, etc.  
**Translation:** 

**[5517.10s] English:** If you believe that.  
**Translation:** 

**[5518.36s] English:** You know, you just don't.  
**Translation:** 

**[5520.00s] English:** Exists after death, like you know, it solves the problem completely—at least you're saying.  
**Translation:** 

**[5523.22s] English:** If you don't believe in God, you don't worry about what happens after death, yeah? I don't know, you.  
**Translation:** 

**[5528.98s] English:** Worry about this life because that's the only one you have, I think.  
**Translation:** 

**[5534.80s] English:** Well, I don't know. If I were to say what Ernest Becker says, I would say I agree.  
**Translation:** 

**[5538.48s] English:** With him more or less, you do deeply worry if you believe there's no God.  
**Translation:** Vocabulary: becker: 贝克; ernest: 埃德蒙

**[5547.80s] English:** There's still a deep worry about the mystery of it all: like, how does that make any sense?  
**Translation:** 

**[5554.06s] English:** It just ends; I don't think we can truly understand that, right? So much of our life, the  
**Translation:** 

**[5561.24s] English:** Consciousness, the ego is invested in this being, and then science keeps bringing  
**Translation:** 

**[5568.74s] English:** Humanity has been taken down from its pedestal, and that's just another example of it—that's wonderful.  
**Translation:** Vocabulary: pedestal: 地位

**[5575.44s] English:** But for us individual humans,  
**Translation:** 

**[5577.66s] English:** We don't like to be brought down from a pedestal. You're saying, "like what?" But see, you're fine with it.  
**Translation:** 

**[5582.86s] English:** It's because, well, so what Ernest Becker would say is you're fine with it because that's just a more  
**Translation:** 

**[5587.36s] English:** Peaceful existence for you, but you're not really fine. You're hiding from, in fact, some of the people.  
**Translation:** 

**[5591.94s] English:** That experience the deepest trauma; often, they have already gone through it earlier in life before they seek help.  
**Translation:** 

**[5598.42s] English:** Extensive therapy will say I'm fine, it's like when you talk to people who are truly angry.  
**Translation:** Vocabulary: trauma: 创伤

**[5603.30s] English:** How are you doing? I'm fine. The question is, what's going on?  
**Translation:** 

**[5607.66s] English:** Now, I had a near-death experience; I had a very bad motorcycle accident when I was 17. So,  
**Translation:** 

**[5614.86s] English:** But that didn't have any impact on my reflection on that topic, so I'm basically just playing a bit.  
**Translation:** 

**[5622.14s] English:** Of devil's advocate, pushing back: Is it truly possible to accept death and the  
**Translation:** Vocabulary: advocate: 提倡者

**[5627.98s] English:** Flip side: That's more interesting, I think, for AI and robotics is how important is it to have  
**Translation:** 

**[5634.46s] English:** This is one of the suite of motivations, is to  
**Translation:** Vocabulary: motivations: 驱动力; robotics: 机器人学

**[5637.66s] English:** Uh, not just.  
**Translation:** 

**[5640.00s] English:** Avoid falling off the roof, or something like that, but ponder the end of the ride.  
**Translation:** Vocabulary: ponder: 思考

**[5650.08s] English:** If you listen to the Stoics, it's a great motivator. It adds a sense of urgency, so maybe.  
**Translation:** 

**[5657.84s] English:** To truly fear death, or be cognizant of it, might give a deeper meaning and urgency to the moment.  
**Translation:** Vocabulary: cognizant: 意识到; motivator: 激励; stoics: 斯多葛派; urgency: 紧迫感

**[5666.32s] English:** To live fully, maybe I don't disagree with that. I mean, I think what motivates me here is uh  
**Translation:** 

**[5676.64s] English:** You know, knowing more about human nature — I mean, I think human nature and human intelligence,...  
**Translation:** Vocabulary: motivates: 激励

**[5681.60s] English:** Is a big mystery; it's a scientific mystery, in addition to you know, philosophical and  
**Translation:** 

**[5687.84s] English:** Etc., but you know, I'm a true believer in science, so, and I do have kind of a belief that,...  
**Translation:** Vocabulary: believer: 信仰者; philosophical: 哲学的

**[5696.32s] English:** For complex systems like the brain and the mind, the way to understand it is to try to  
**Translation:** 

**[5703.52s] English:** Reproduce it with you know, artifacts that you build, because you know what's essential to it.  
**Translation:** Vocabulary: artifacts: 人工制品; reproduce: 复制

**[5708.72s] English:** When you try to build it, you know, the same way, um, I've used this analogy before with you, I believe.  
**Translation:** 

**[5714.24s] English:** The same way we only started to understand aerodynamics when we started building airplanes.  
**Translation:** Vocabulary: aerodynamics: 空气动力学; analogy: 类比

**[5719.20s] English:** And that helped us understand how birds fly, you know, so I think there's kind of a similar process.  
**Translation:** 

**[5725.12s] English:** Here, where  
**Translation:** 

**[5726.32s] English:** We don't have a full theory of intelligence, but building something that's truly intelligent.  
**Translation:** 

**[5731.04s] English:** Artifacts will help us, perhaps, develop some underlying theory that encompasses not  
**Translation:** Vocabulary: encompasses: 包括

**[5737.12s] English:** Just like artificial implements, but also human and biological intelligence in general. So, you're an  
**Translation:** 

**[5744.08s] English:** Interesting person to ask this question about, sort of, all kinds of different other intelligences.  
**Translation:** Vocabulary: implements: 工具

**[5750.00s] English:** Entities or intelligences, what are your thoughts about kind of like the touring?  
**Translation:** 

**[5756.32s] English:** Or, the Chinese Room question: if we  
**Translation:** 

**[5760.00s] English:** Create an AI system that exhibits a lot of properties.  
**Translation:** 

**[5764.16s] English:** Of intelligence and consciousness,  
**Translation:** Vocabulary: consciousness: 觉醒; exhibits: 展现

**[5767.56s] English:** How comfortable are you thinking of that entity?  
**Translation:** 

**[5770.26s] English:** As intelligent, or conscious?  
**Translation:** 

**[5772.64s] English:** So, you're trying to build new systems now.  
**Translation:** 

**[5774.62s] English:** That have intelligence,  
**Translation:** 

**[5775.60s] English:** And there are metrics about their performance.  
**Translation:** 

**[5777.46s] English:** But that metric is external.  
**Translation:** Vocabulary: metric: 衡量标准; metrics: 衡量指标

**[5782.56s] English:** Okay, so are you okay with calling a thing intelligent?  
**Translation:** 

**[5786.48s] English:** Or are you going to be like most humans?  
**Translation:** 

**[5789.06s] English:** And be once again unhappy to be brought down.  
**Translation:** 

**[5792.68s] English:** From a pedestal of consciousness/slash/intelligence?  
**Translation:** Vocabulary: pedestal: 基座

**[5794.92s] English:** No, I'll be very happy to understand.  
**Translation:** 

**[5801.26s] English:** More about human nature, human mind, and human intelligence.  
**Translation:** 

**[5805.50s] English:** Through the construction of machines,  
**Translation:** 

**[5807.20s] English:** That have similar abilities.  
**Translation:** 

**[5810.56s] English:** And, if one consequence of this is to bring down humanity,...  
**Translation:** 

**[5814.50s] English:** One notch down from its already low pedestal,  
**Translation:** Vocabulary: notch: 档次

**[5818.00s] English:** I'm just fine with it.  
**Translation:** 

**[5819.04s] English:** That's just the reality of life.  
**Translation:** 

**[5821.30s] English:** So, I'm fine with that.  
**Translation:** 

**[5822.42s] English:** Now, you were asking me about things that,  
**Translation:** 

**[5824.96s] English:** Opinions I have that a lot of people may disagree with.  
**Translation:** 

**[5827.88s] English:** I think,  
**Translation:** 

**[5831.62s] English:** If we think about the design,  
**Translation:** 

**[5832.72s] English:** Of an autonomous intelligence system,  
**Translation:** Vocabulary: autonomous: 自主的

**[5834.20s] English:** So, assuming that we are somewhat successful at some level.  
**Translation:** 

**[5838.64s] English:** Of getting machines to learn models of the world,  
**Translation:** 

**[5840.40s] English:** Predictive models of the world,  
**Translation:** 

**[5842.54s] English:** We build intrinsic motivation objectives.  
**Translation:** Vocabulary: intrinsic: 内在的; objectives: 目标; predictive: 预测性的

**[5845.80s] English:** To drive the behavior of that system.  
**Translation:** 

**[5848.12s] English:** The system also has:  
**Translation:** 

**[5849.04s] English:** Perception modules that allow it  
**Translation:** 

**[5850.92s] English:** To estimate the state of the world,  
**Translation:** 

**[5852.78s] English:** And then, have some way of figuring out.  
**Translation:** 

**[5854.60s] English:** The sequence of actions to optimize a particular objective.  
**Translation:** Vocabulary: optimize: 优化

**[5859.28s] English:** If it has a critic of the type that I was describing before,  
**Translation:** 

**[5862.70s] English:** The thing that makes you recoil your arm.  
**Translation:** Vocabulary: recoil: 后退

**[5864.58s] English:** The second time I try to pinch you,  
**Translation:** 

**[5868.56s] English:** An intelligent autonomous machine will have emotions.  
**Translation:** Vocabulary: pinch: 捏

**[5871.66s] English:** I think emotions are an integral part.  
**Translation:** 

**[5874.02s] English:** Of autonomous intelligence.  
**Translation:** Vocabulary: integral: 必不可少的

**[5876.36s] English:** If you have an intelligent system,  
**Translation:** 

**[5878.42s] English:** That is driven.  
**Translation:** 

**[5880.00s] English:** By intrinsic motivation, by objectives, if it has a critic that allows it to predict in advance.  
**Translation:** 

**[5887.52s] English:** Whether the outcome of a situation is going to be good or bad is going to have emotions attached to it.  
**Translation:** 

**[5892.16s] English:** Going to have fear, yes, when it predicts that the outcome is going to be bad.  
**Translation:** 

**[5898.08s] English:** And something to avoid is getting elated when it predicts it will be good.  
**Translation:** Vocabulary: elated: 欣喜若狂

**[5901.84s] English:** Um, if it has drives to relate with humans, you know, in some ways, the way humans have, you know,  
**Translation:** 

**[5912.64s] English:** It's going to be social, right? And so it's gonna have emotions about attachment and things of that nature.  
**Translation:** 

**[5918.08s] English:** That type, so um, so I think you know, the sort of sci-fi thing where you see a commander  
**Translation:** 

**[5926.24s] English:** Data, like having an emotion chip that you can turn off—right? I think that's ridiculous, so...  
**Translation:** 

**[5931.84s] English:** So, I mean, here's the difficult philosophical and social question: Do you think there will be a time...  
**Translation:** 

**[5939.92s] English:** Like a civil rights movement for robots, where... um, okay, forget the movement, but a discussion.  
**Translation:** Vocabulary: philosophical: 哲学的

**[5946.48s] English:** Like the Supreme Court, that particular kind of robot, you know, particular kinds of systems,...  
**Translation:** 

**[5955.60s] English:** Um, they deserve the same rights as humans because they can suffer just as humans can.  
**Translation:** 

**[5962.80s] English:** All those kinds of things—well, perhaps, perhaps not, like imagine that humans were.  
**Translation:** 

**[5969.20s] English:** That you could, you know, die and be restored, like you could be sort of  
**Translation:** 

**[5974.96s] English:** You know, it could be 3D printed and your brain could be reconstructed in its finest details.  
**Translation:** 

**[5980.56s] English:** Our ideas of rights will change in that case, if you can always just.  
**Translation:** Vocabulary: reconstructed: 重建

**[5985.76s] English:** There's always a backup, you could always restore. Maybe that's why the importance of having one won't go down.  
**Translation:** 

**[5990.96s] English:** One notch.  
**Translation:** Vocabulary: backup: 备用方案; notch: 刻度

**[5991.84s] English:** That's right, but also your desire to do dangerous things, like you know, jumping out of planes or something.  
**Translation:** 

**[5999.12s] English:** Know what doing in the sky?  
**Translation:** 

**[6000.00s] English:** Diving, or you know, uh, or you know, race car driving—yeah, you know, car racing—or that kind of thing.  
**Translation:** 

**[6006.96s] English:** Stuff you know would probably increase, or, you know, airplane aerobatics or that kind of stuff.  
**Translation:** Vocabulary: aerobatics: 飞机特技

**[6011.76s] English:** Right, it would be fine to do a lot of those things or explore, you know, dangerous areas and things.  
**Translation:** 

**[6016.96s] English:** Like that, it would kind of change your relationship, so now it's very likely that robots would be like:  
**Translation:** 

**[6022.00s] English:** That, because you know, they'll be based on perhaps technology that is somewhat similar to today's.  
**Translation:** 

**[6029.60s] English:** Technology, and you can always have a backup. So, it's possible—I don't know if you like—  
**Translation:** 

**[6035.12s] English:** Video games, but there's a game called Diablo, and uh, oh, my sons are huge fans of this.  
**Translation:** 

**[6041.84s] English:** Yes, uh, and in fact, they made a game that's inspired by it—awesome! Like, they built a game for my three.  
**Translation:** Vocabulary: diablo: 恶魔之魂

**[6049.68s] English:** Sons have a game design studio between them. Yeah, that's awesome! They came out with a game, and they just...  
**Translation:** 

**[6054.48s] English:** Came out last year, no, this was last year — uh, early last year, about a year ago. That's awesome, but so...  
**Translation:** 

**[6059.60s] English:** I don't know if you've heard of it, but it's a game called Diablo. There's something called Hardcore.  
**Translation:** 

**[6064.40s] English:** Mode: If you die, there's no you're gone, right? That's it, and so it's possible with AI systems.  
**Translation:** Vocabulary: hardcore: hardcore模式

**[6073.04s] English:** For them to operate successfully and for us to treat them in a certain way, because  
**Translation:** 

**[6078.24s] English:** They have to be integrated into human society; they have to be able to die. No copies allowed, in fact.  
**Translation:** Vocabulary: integrated: 融合

**[6085.04s] English:** Copying is illegal, and it's possible with humans as well. Like cloning, will be illegal even when it's  
**Translation:** 

**[6089.44s] English:** Done right, so it's possible with humans as well; like cloning will be illegal even when it's done.  
**Translation:** 

**[6093.52s] English:** Right, so it's possible with humans as well; cloning will be illegal, even when it's done right.  
**Translation:** 

**[6096.24s] English:** But then, it's what we were talking about with computers: you'll be able to copy you right.  
**Translation:** 

**[6100.72s] English:** You'll be able to perfectly save and pickle the mind state, and it's possible that that would.  
**Translation:** 

**[6108.32s] English:** Be illegal because that goes against it, and that will destroy the motivations of the system, okay? So,  
**Translation:** Vocabulary: motivations: 驱动力; pickle: 保存

**[6116.32s] English:** Let's say you have a domestic robot, okay?  
**Translation:** 

**[6119.44s] English:** Let's say you have a domestic robot, okay?  
**Translation:** 

**[6120.00s] English:** Sometime in the future, yes, and the domestic robot you know comes to you, kind of somewhat.  
**Translation:** 

**[6126.36s] English:** Pre-trained, you know, it can do a bunch of things, yes, but it has a particular personality that makes  
**Translation:** 

**[6130.82s] English:** It is slightly different from the other robots, because that makes them more interesting.  
**Translation:** 

**[6133.76s] English:** And then, because it's lived with you for five years, you've grown some.  
**Translation:** 

**[6138.96s] English:** Attachment to it, and vice versa; and it's learned a lot about you, or maybe it's not a household.  
**Translation:** 

**[6145.44s] English:** Robot: Maybe it's a virtual assistant that lives in your, you know, augmented reality.  
**Translation:** Vocabulary: augmented: 增强; versa: 互相

**[6150.40s] English:** Glasses, or whatever, right? Uh, you know, the movie-type thing, right? Um, and that system—to some.  
**Translation:** 

**[6158.64s] English:** The extent that the intelligence in that system is a bit like your child, or maybe your PhD student.  
**Translation:** 

**[6165.60s] English:** In the sense that there's a lot of you in that machine now, right? Yeah, and so if it were...  
**Translation:** 

**[6172.24s] English:** A living thing, you would do this for free.  
**Translation:** 

**[6175.44s] English:** If you want your child to be able to live his or her own life, then you know, uh,...  
**Translation:** 

**[6181.84s] English:** You know, the fact that they learn stuff from you doesn't mean that you have any ownership of it.  
**Translation:** 

**[6185.76s] English:** Right, yeah, but if it's a robot that you've trained, perhaps you have some intellectual property concerns there.  
**Translation:** 

**[6192.32s] English:** Property claim about intellectual property? Oh, I thought you meant something like a permanence value in the  
**Translation:** Vocabulary: permanence: 持久性

**[6198.32s] English:** Sense is part of the use, in well, there's permanence value, right? So, you would lose a lot if that robot.  
**Translation:** 

**[6203.68s] English:** Were to be destroyed, and you had no background.  
**Translation:** 

**[6205.44s] English:** Up, you would lose a lot, you know. A lot of investment, you know, kind of like a  
**Translation:** 

**[6209.36s] English:** Uh, you know, a person dying—you know, um—that a friend of a friend of yours is dying, or a coworker.  
**Translation:** Vocabulary: coworker: 同事

**[6215.52s] English:** Or something like that, um, but also, uh, you have intellectual property rights in the sense that  
**Translation:** 

**[6222.80s] English:** That system is fine-tuned to your particular existence, so that's now a very  
**Translation:** 

**[6228.48s] English:** Unique instantiation of that original background model; whatever it was, that arrived—another issue.  
**Translation:** 

**[6235.44s] English:** Right, because now imagine that the robot has its own kind of  
**Translation:** Vocabulary: instantiation: 实例

**[6240.00s] English:** Volition and decides to work on someone else, yes, or kind of you know, thinks life.  
**Translation:** 

**[6245.46s] English:** With you is sort of untenable or whatever right now, all the other things.  
**Translation:** Vocabulary: volition: 意志

**[6250.66s] English:** That system learned from you, you know. How can you delete it, you know?  
**Translation:** 

**[6257.10s] English:** All the personal information that the system knows about you, yeah, I mean that.  
**Translation:** 

**[6260.92s] English:** Would be kind of an ethical question, like, you know, can you erase the mind?  
**Translation:** 

**[6264.66s] English:** Of a smart robot to protect your privacy, yeah, you can't do this with.  
**Translation:** Vocabulary: erase: 删除

**[6270.60s] English:** Humans, you can ask them to shut up, but you don't have complete power over them.  
**Translation:** 

**[6275.28s] English:** They can't erase humans, yeah. It's the problem with the relationships, you know.  
**Translation:** 

**[6279.24s] English:** You break up, you can't erase the other person with robots. I think it.  
**Translation:** 

**[6283.80s] English:** Will have to be the same thing with robots: that, that risk, that there has to  
**Translation:** 

**[6288.76s] English:** There is some risk to our interactions, but that's necessary to truly experience them.  
**Translation:** 

**[6294.64s] English:** Deeply, it feels like, so you have to be able to lose your robot friend, and that  
**Translation:** 

**[6300.20s] English:** Robot friend to go tweeting about how much of an asshole you were, but then are  
**Translation:** 

**[6304.90s] English:** You are allowed, you know, to murder the robot to protect your private information.  
**Translation:** Vocabulary: asshole: 混蛋; tweeting: 发推特

**[6308.68s] English:** Probably, it decides to leave. I have this intuition that for robots, with  
**Translation:** 

**[6313.06s] English:** Certainly, it's almost like a regulation if you declare your robot to be.  
**Translation:** Vocabulary: intuition: 直觉

**[6319.36s] English:** Call it sentient, or something like that; this robot is designed for.  
**Translation:** 

**[6323.20s] English:** Human interaction, then, you're not allowed to do that because you're not.  
**Translation:** Vocabulary: sentient: 有感知的

**[6324.58s] English:** Allowed to, these robots is the same as murdering other humans, well, but what?  
**Translation:** 

**[6328.74s] English:** About you, do a backup of the robot. Did you preserve it on the hard drive or the  
**Translation:** 

**[6332.78s] English:** Equivalent in the future, that might be illegal, it's like it's a higher.  
**Translation:** 

**[6335.74s] English:** State: Piety piracy is illegal. It's your own, it's your own robot, right? But I can't.  
**Translation:** Vocabulary: piracy: 侵权

**[6340.38s] English:** You don't, but then, but then you can wipe out his brain, so the robot doesn't.  
**Translation:** 

**[6346.28s] English:** Know anything about you anymore, but you still have, technically, is still in.  
**Translation:** Vocabulary: technically: 理论上

**[6349.90s] English:** Existence, because you backed it up, and then there will be these great speeches at  
**Translation:** 

**[6353.62s] English:** The Supreme Court by the حضرة  
**Translation:** 

**[6354.58s] English:** Saying, "Oh, sure, you can erase the mind of the robot just like you can erase the mind of a human.  
**Translation:** 

**[6360.00s] English:** We both can suffer.  
**Translation:** Vocabulary: erase: 擦除

**[6361.08s] English:** There'll be some epic, like, Obama-type character with a speech that we, like, the robots and the humans are the same.  
**Translation:** 

**[6368.52s] English:** We can both suffer.  
**Translation:** 

**[6369.86s] English:** We can both hope.  
**Translation:** 

**[6371.38s] English:** We can do all those kinds of things, raise families, and all that kind of stuff.  
**Translation:** 

**[6377.70s] English:** It's interesting, just like you said, that emotions seem to be a fascinatingly powerful aspect of human interaction and human-robot interaction.  
**Translation:** 

**[6386.82s] English:** And if they are able to exhibit emotions, at the end of the day, that's probably going to have us deeply consider human rights, like what we value in humans and what we value in other animals.  
**Translation:** Vocabulary: exhibit: 展示; fascinatingly: 令人着迷地

**[6400.28s] English:** That's why robots and AI are great.  
**Translation:** 

**[6402.18s] English:** It makes us ask really good questions.  
**Translation:** 

**[6404.30s] English:** Ask the hard questions, yeah.  
**Translation:** 

**[6405.44s] English:** But you asked about the Chinese room-type argument: is it real if it looks real?  
**Translation:** 

**[6410.94s] English:** Yeah.  
**Translation:** 

**[6411.42s] English:** I think the Chinese room argument is a ridiculous one.  
**Translation:** 

**[6414.82s] English:** So, for people who don't know, there's the Chinese room.  
**Translation:** 

**[6416.82s] English:** The Chinese room is a concept I don't even know how to formulate well.  
**Translation:** 

**[6420.76s] English:** But basically, you can mimic the behavior of an intelligent system by just following a giant algorithm codebook that tells you exactly how to respond in every case.  
**Translation:** 

**[6432.90s] English:** But is that really intelligent?  
**Translation:** Vocabulary: algorithm: 计算方法; codebook: 代码手册

**[6434.66s] English:** It's like a giant lookup table.  
**Translation:** 

**[6436.50s] English:** When this person says this, you answer with this.  
**Translation:** 

**[6438.58s] English:** When this person says this, you answer with this.  
**Translation:** 

**[6442.04s] English:** And if you understand how that works, you have this giant, nearly infinite lookup table.  
**Translation:** Vocabulary: infinite: 无尽的

**[6447.06s] English:** Is that really intelligence?  
**Translation:** 

**[6448.60s] English:** Because intelligence seems to be a mechanism that's much more interesting and complex than a look-up table.  
**Translation:** 

**[6454.58s] English:** I don't think so.  
**Translation:** 

**[6455.16s] English:** So, I mean, the real question comes down to: Do you think you can mechanize intelligence in some way, even if that involves learning?  
**Translation:** 

**[6467.20s] English:** And the answer is: of course, yes.  
**Translation:** 

**[6469.24s] English:** There's no question.  
**Translation:** 

**[6470.68s] English:** There's a second question, then, which is: Assuming you can reproduce intelligence.  
**Translation:** 

**[6476.82s] English:** And sort of different hardware than biological hardware, you know, like computers.  
**Translation:** Vocabulary: reproduce: 复制

**[6480.00s] English:** Others, can you match human intelligence in all the domains in which humans are intelligent?  
**Translation:** 

**[6493.04s] English:** Is it possible, right?  
**Translation:** 

**[6494.04s] English:** So, that's the hypothesis of strong AI.  
**Translation:** 

**[6497.12s] English:** The answer to this, in my opinion, is an unqualified yes; this will also happen at some point.  
**Translation:** Vocabulary: hypothesis: 假设; unqualified: 无保留的

**[6502.44s] English:** There's no question that machines, at some point, will become more intelligent than humans.  
**Translation:** 

**[6506.52s] English:** In all domains where humans are intelligent.  
**Translation:** 

**[6508.68s] English:** This is not for tomorrow; it's going to take a long time, regardless of what Elon and others say.  
**Translation:** 

**[6515.74s] English:** Have claimed or believed.  
**Translation:** 

**[6518.26s] English:** This is a lot harder than many of those guys think it is, and many of those guys who thought  
**Translation:** 

**[6524.60s] English:** It was simpler than that five years ago. Now, think it's hard because it's been five years.  
**Translation:** 

**[6529.78s] English:** And they realize it's going to take a lot longer.  
**Translation:** 

**[6533.52s] English:** That includes a bunch of people at DeepMind, for example, but,...  
**Translation:** 

**[6535.36s] English:** Oh, interesting.  
**Translation:** 

**[6536.36s] English:** I haven't actually touched base with DeepMind.  
**Translation:** 

**[6538.66s] English:** DeepMind folks, but some of it, Elon or Demis Hassabis (I mean), sometimes in your roles,  
**Translation:** 

**[6545.88s] English:** You have to kind of create deadlines that are nearer, rather than farther away, to kind of create  
**Translation:** Vocabulary: deadlines: 截止日期; hassabis: 哈萨布

**[6551.58s] English:** An urgency, because you have to believe the impossible is possible in order to accomplish  
**Translation:** 

**[6556.12s] English:** It.  
**Translation:** Vocabulary: urgency: 急迫性

**[6557.12s] English:** And there's, of course, a flip side to that coin, but it's a weird thing: you can't be too cynical.  
**Translation:** 

**[6561.20s] English:** If you want to get something done.  
**Translation:** Vocabulary: cynical: 怀疑一切的

**[6562.60s] English:** Absolutely.  
**Translation:** 

**[6563.60s] English:** I agree with that.  
**Translation:** 

**[6564.60s] English:** But I mean, you have to inspire people to work on sort of ambitious things.  
**Translation:** 

**[6568.66s] English:** So, you know, it's certainly a lot harder than we believe, but there's no question about that.  
**Translation:** 

**[6576.16s] English:** In my mind, this will happen.  
**Translation:** 

**[6578.28s] English:** And now, people are kind of worried about what that means for humans.  
**Translation:** 

**[6582.98s] English:** They are going to be brought down from their pedestal, you know—a bunch of notches with  
**Translation:** 

**[6587.82s] English:** That.  
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

**[6600.00s] English:** FAIR, the Facebook AI Research group, has recently celebrated its eighth birthday.  
**Translation:** 

**[6605.58s] English:** Or, maybe, you can correct me on that.  
**Translation:** Vocabulary: eighth: 第八个

**[6608.36s] English:** Looking back, what have been the successes, the failures, and the lessons learned from the eight years of FAIR?  
**Translation:** 

**[6614.40s] English:** And maybe you can also give some context on where the newly minted Meta AI fits into how it relates to FAIR?  
**Translation:** Vocabulary: minted: 新成立的

**[6622.60s] English:** Right. So, let me tell you a little bit about the organization of all this.  
**Translation:** 

**[6625.02s] English:** Yes. Yeah, FAIR was created almost exactly eight years ago.  
**Translation:** 

**[6630.04s] English:** It wasn't called FAIR yet. It took on that name a few months later.  
**Translation:** 

**[6634.58s] English:** And at the time I joined Facebook, there was a group called the AI group that had about 12 engineers and a few scientists—like, you know, 10 engineers and two scientists—or something like that.  
**Translation:** 

**[6646.86s] English:** I ran it for three and a half years as a director.  
**Translation:** 

**[6650.28s] English:** You know, we hired the first few scientists and kind of set up the culture and organized it.  
**Translation:** 

**[6655.02s] English:** You know, I explained to the Facebook leadership what fundamental research was about and how it can work within industry, and how it needs to be open and everything.  
**Translation:** 

**[6667.24s] English:** And I think it's been an unqualified success in the sense that FAIR has simultaneously produced top-level research, advanced the science and technology, provided tools—open-source tools like PyTorch—and many others.  
**Translation:** Vocabulary: unqualified: 无保留的

**[6685.02s] English:** But at the same time, it has had a direct or mostly indirect impact on Facebook, at the time, now Meta, in the sense that a lot of the systems that Meta is built around now are based on research projects that started at FAIR.  
**Translation:** 

**[6707.96s] English:** So, if you were to take deep learning out of Facebook's services now and Meta more generally.  
**Translation:** 

**[6715.02s] English:** I mean, the company would literally crumble.  
**Translation:** 

**[6717.74s] English:** I mean, it's completely built around.  
**Translation:** Vocabulary: crumble: 崩塌

**[6720.00s] English:** Around AI these days.  
**Translation:** 

**[6721.48s] English:** And it's really essential to the operations.  
**Translation:** 

**[6724.00s] English:** So, what happened after three and a half years?  
**Translation:** 

**[6726.64s] English:** Is that I changed roles and became chief scientist.  
**Translation:** 

**[6730.22s] English:** So, I'm not doing day-to-day management of FAIR anymore.  
**Translation:** 

**[6734.90s] English:** I'm more of a kind of, you know.  
**Translation:** 

**[6737.12s] English:** Think about strategy and things like that.  
**Translation:** 

**[6738.88s] English:** And I carry out my own research.  
**Translation:** 

**[6741.46s] English:** I've, you know, my own kind of research group.  
**Translation:** 

**[6743.34s] English:** Working on self-supervised learning and things like this,  
**Translation:** 

**[6745.32s] English:** Which I didn't have time to do when I was director.  
**Translation:** 

**[6748.24s] English:** So now, FAIR is run by Joël Pinot and Antoine Borde.  
**Translation:** 

**[6754.20s] English:** Together, because FAIR is kind of split in two now.  
**Translation:** 

**[6756.34s] English:** There's something called FAIR Labs.  
**Translation:** 

**[6757.86s] English:** Which is sort of bottom-up, science-driven research.  
**Translation:** 

**[6760.94s] English:** And FAIR Excel, which is slightly more organized.  
**Translation:** 

**[6763.48s] English:** For bigger projects that require a little more focused effort.  
**Translation:** 

**[6767.68s] English:** And more engineering support, and things like that.  
**Translation:** 

**[6769.78s] English:** So, Joël leads the FAIR Lab, and Antoine Borde leads the FAIR Excel.  
**Translation:** 

**[6772.88s] English:** Where are they located?  
**Translation:** 

**[6774.68s] English:** All over?  
**Translation:** 

**[6775.52s] English:** It's delocalized all over.  
**Translation:** Vocabulary: delocalized: 分散化

**[6776.60s] English:** Okay.  
**Translation:** 

**[6777.98s] English:** So, there's no question that the leadership of the company  
**Translation:** 

**[6782.54s] English:** Believes that this was a very worthwhile investment.  
**Translation:** 

**[6786.56s] English:** And what that means is that it's there for the long run, right?  
**Translation:** 

**[6793.08s] English:** So, there is, if you want to talk in these terms,  
**Translation:** 

**[6796.80s] English:** Which I don't like, there's a business model; if you want,  
**Translation:** 

**[6799.56s] English:** Where FAIR, despite being a very fundamental research lab,  
**Translation:** 

**[6803.60s] English:** Brings a lot of value to the company,  
**Translation:** 

**[6805.30s] English:** Either it is mostly indirect through other groups.  
**Translation:** 

**[6807.98s] English:** Mm-hmm.  
**Translation:** 

**[6809.88s] English:** Now, what happened three and a half years ago?  
**Translation:** 

**[6811.56s] English:** When I stepped down, it was also the time when Facebook AI was created.  
**Translation:** 

**[6814.60s] English:** Which was basically a larger organization.  
**Translation:** 

**[6817.68s] English:** That covers FAIR, so FAIR is included in it.  
**Translation:** 

**[6821.70s] English:** But also has other organizations that are focused.  
**Translation:** 

**[6826.26s] English:** On Applied Research or Advanced Development of AI Technology  
**Translation:** 

**[6831.22s] English:** That is more focused on the company's products.  
**Translation:** 

**[6834.68s] English:** So, less emphasis on fundamental research.  
**Translation:** 

**[6836.66s] English:** Less Fundamental.  
**Translation:** 

**[6837.50s] English:** There's still more research.  
**Translation:** 

**[6838.34s] English:** I mean, there are a lot of papers coming out of those.  
**Translation:** 

**[6840.00s] English:** Organizations and people are awesome and wonderful to interact with, but it serves as a way to  
**Translation:** 

**[6851.82s] English:** Scale up, if you want, AI technology, which may be very experimental and sort of lab prototypes.  
**Translation:** 

**[6859.34s] English:** Into things that are usable.  
**Translation:** Vocabulary: prototypes: 样品; usable: 可用的

**[6860.34s] English:** So, FAIR is a subset of Meta AI.  
**Translation:** 

**[6863.16s] English:** Is "FAIR" become like KFC, it'll just keep the "F," nobody cares what the "F" stands for?  
**Translation:** 

**[6868.80s] English:** We'll know soon enough; probably by the end of 2021.  
**Translation:** 

**[6874.56s] English:** I mean, this is not a giant change: MAIR, FAIR.  
**Translation:** 

**[6877.98s] English:** Well, "MAIR" doesn't sound too good, but the brand people are kind of deciding on.  
**Translation:** 

**[6882.74s] English:** This, and they've been hesitating for a while now, and they tell us they're going to come.  
**Translation:** Vocabulary: hesitating: 犹豫不决

**[6887.50s] English:** Up with an answer as to whether FAIR is going to change its name or whether we're going to change.  
**Translation:** 

**[6891.30s] English:** Just the meaning of the F.  
**Translation:** 

**[6892.30s] English:** Oh, that's a good call.  
**Translation:** 

**[6894.16s] English:** I will keep FAIR, and change the meaning of the F.  
**Translation:** 

**[6896.12s] English:** That would be my preference.  
**Translation:** 

**[6897.62s] English:** I would turn the F.  
**Translation:** 

**[6898.62s] English:** Okay.  
**Translation:** 

**[6898.78s] English:** Turn the "F" into "fundamental.  
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

**[6904.78s] English:** So, this would be:  
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

**[6911.78s] English:** And now, Meta AI is part of the Reality Lab.  
**Translation:** 

**[6916.82s] English:** So, Meta (now known as Facebook) is called Meta and it's kind of divided into Facebook, Instagram,  
**Translation:** 

**[6928.60s] English:** And Twitter.  
**Translation:** 

**[6929.60s] English:** And Reality Lab.  
**Translation:** 

**[6930.60s] English:** And Reality Lab is about AR, VR, telepresence, communication technology, and stuff like that.  
**Translation:** 

**[6940.60s] English:** It's kind of the...  
**Translation:** Vocabulary: telepresence: 远程存在感

**[6941.60s] English:** You can think of it as a combination of new products and technology.  
**Translation:** 

**[6949.60s] English:** Of Meta.  
**Translation:** 

**[6950.60s] English:** Is that where the touch-sensing technology for robots, I saw that you were posting about? That's...  
**Translation:** 

**[6955.60s] English:** But touch sensing for robots is part of FAIR, actually.  
**Translation:** Vocabulary: sensing: 感知

**[6957.60s] English:** Oh, it is?  
**Translation:** 

**[6958.60s] English:** Okay, cool.  
**Translation:** 

**[6959.60s] English:** Yeah.  
**Translation:** 

**[6960.00s] English:** No, but there's the other way—the haptic glove, right?  
**Translation:** Vocabulary: haptic: 触觉的

**[6965.72s] English:** Yes, that's more from Reality Lab.  
**Translation:** 

**[6967.64s] English:** That's Reality Lab research.  
**Translation:** 

**[6970.64s] English:** Reality Lab Research.  
**Translation:** 

**[6971.76s] English:** By the way, the touch sensors are super interesting.  
**Translation:** Vocabulary: sensors: 传感器

**[6974.42s] English:** Like integrating that modality into the whole sensing suite is very interesting.  
**Translation:** 

**[6980.24s] English:** So, what do you think about the metaverse?  
**Translation:** Vocabulary: integrating: 融合; metaverse: 元宇宙; modality: 模态

**[6983.58s] English:** What do you think about this whole expansion of the view of the role of Facebook and Meta in the world?  
**Translation:** 

**[6990.94s] English:** Well, the metaverse really should be thought of as the next step in the internet, right?  
**Translation:** 

**[6995.36s] English:** Sort of trying to make the experience more compelling by connecting either with other people or with content, you know.  
**Translation:** 

**[7009.18s] English:** And, you know, we are evolved and trained to....  
**Translation:** Vocabulary: compelling: 有吸引力的; evolved: 进化的

**[7013.58s] English:** Evolve in 3D environments where, you know, we can see other people. We can talk to them when we're near them, or, you know, an other viewer far away can't hear us—things like that, right?  
**Translation:** 

**[7025.04s] English:** So, there are a lot of social conventions that exist in the real world that we can try to transpose.  
**Translation:** Vocabulary: conventions: 社交规范; environments: 环境; evolve: 进化; transpose: 转移; viewer: 观众

**[7030.84s] English:** Now, what is going to be eventually the ...  
**Translation:** 

**[7035.02s] English:** How compelling is it going to be?  
**Translation:** 

**[7036.18s] English:** Like, you know, is it going to be the case that people are going to be willing to do this if they have to wear, you know, a huge pair of goggles?  
**Translation:** 

**[7043.58s] English:** Well, all day, maybe not.  
**Translation:** Vocabulary: goggles: 护目镜

**[7046.40s] English:** But then again, if the experience is sufficiently compelling, maybe so.  
**Translation:** 

**[7050.28s] English:** Or, if the device that you have to wear is just basically a pair of glasses, and technology makes sufficient progress for that.  
**Translation:** Vocabulary: sufficiently: 足够地

**[7057.80s] English:** You know, AR is a much easier concept to grasp; that you're going to have, you know, augmented reality glasses that basically contain some sort of, you know, virtual assistant that can help you in your daily lives.  
**Translation:** 

**[7070.36s] English:** But at the same time, with AR, you have to contend with reality.  
**Translation:** Vocabulary: augmented: 增强; contend: 应对

**[7073.58s] English:** With VR, you can completely detach yourself from reality, so it gives you freedom.  
**Translation:** 

**[7077.20s] English:** It might be easier to design worlds in VR.  
**Translation:** Vocabulary: detach: 脱离

**[7080.00s] English:** Yeah, but you can imagine, you know, the metaverse being a mix, right?  
**Translation:** 

**[7086.54s] English:** Or, like, you can have objects that exist in the metaverse that pop up on top of the real world or only exist in virtual reality.  
**Translation:** Vocabulary: metaverse: 多元宇宙

**[7094.10s] English:** Okay, let me ask the hard question.  
**Translation:** 

**[7097.00s] English:** Because all of this was easy.  
**Translation:** 

**[7098.24s] English:** This was easy.  
**Translation:** 

**[7099.16s] English:** Okay, the Facebook, now Meta, the social network, has been painted by the media as net-negative for society, even destructive and evil at times.  
**Translation:** 

**[7110.60s] English:** You've pushed back against this, defending Facebook.  
**Translation:** 

**[7114.02s] English:** Can you explain your defense?  
**Translation:** 

**[7116.58s] English:** Yeah, so the description of the company that is being described in some media is not the same as the company we know when we work inside.  
**Translation:** 

**[7127.02s] English:** And, you know,...  
**Translation:** 

**[7129.16s] English:** It could be claimed that a lot of employees are uninformed about what really goes on in the company.  
**Translation:** 

**[7134.60s] English:** But, you know, I'm a vice president.  
**Translation:** Vocabulary: uninformed: 知识不足的

**[7136.30s] English:** I mean, I have a pretty good vision of what goes on.  
**Translation:** 

**[7138.70s] English:** You know, I don't know everything, obviously.  
**Translation:** 

**[7140.20s] English:** I'm not involved in everything, but certainly not in decisions about, like, you know, content moderation or anything like that.  
**Translation:** 

**[7146.04s] English:** But I have a decent vision of what goes on.  
**Translation:** Vocabulary: moderation: 调节

**[7150.20s] English:** And this evil that is being described, I just don't see it.  
**Translation:** 

**[7153.70s] English:** And then, you know, I think there is an easy story to buy, which is....  
**Translation:** 

**[7159.16s] English:** That, you know, all the bad things in the world, and, you know, the reason your friend believes crazy stuff, you know, there's an easy scapegoat, right?  
**Translation:** 

**[7168.42s] English:** In social media, in general, Facebook, in particular.  
**Translation:** Vocabulary: scapegoat: 替罪羊

**[7174.46s] English:** We have to look at the data.  
**Translation:** 

**[7175.48s] English:** Like, is it the case that Facebook, for example, polarizes people politically?  
**Translation:** Vocabulary: polarizes: 分化; politically: 政治地

**[7182.70s] English:** Are there any academic studies that show this?  
**Translation:** 

**[7185.20s] English:** Is it the case that teenagers think Facebook is a good thing?  
**Translation:** 

**[7188.28s] English:** Yeah, I think so.  
**Translation:** 

**[7189.00s] English:** They think of themselves less if they use Instagram more.  
**Translation:** 

**[7192.12s] English:** Is it the case that people get more riled up against opposite sides, you know?  
**Translation:** 

**[7200.00s] English:** In a debate or political opinion, people tend to be more active on Facebook or less so.  
**Translation:** Vocabulary: riled: 激怒

**[7205.60s] English:** And, uh, studies after studies show that none of this is true. This is independent studies by  
**Translation:** 

**[7211.84s] English:** Academic institutions are not funded by Facebook or Meta, you know, but are studied by Stanford and some others.  
**Translation:** Vocabulary: stanford: 斯坦福大学

**[7217.36s] English:** Colleagues at NYU, actually with whom I have no connection, you know, there's a study recently.  
**Translation:** 

**[7222.48s] English:** They paid people, I think it was in former Yugoslavia, I'm not exactly sure in what.  
**Translation:** Vocabulary: colleagues: 同事; yugoslavia: 南斯拉夫

**[7231.12s] English:** What part did they pay people to not use Facebook for a while during the period?  
**Translation:** 

**[7238.56s] English:** Before the anniversary of the Srebrenica massacres, right? So, you know, people get riled up—like, should  
**Translation:** Vocabulary: massacres: 大规模屠杀; srebrenica: 斯雷布雷尼察

**[7245.20s] English:** You know, should we have a celebration—kind of a memorial celebration—for it or not?  
**Translation:** 

**[7250.88s] English:** So, they paid a bunch of people.  
**Translation:** 

**[7252.48s] English:** To not use Facebook for a few weeks, it turns out that those people ended up being more.  
**Translation:** 

**[7260.24s] English:** Polarized than they were at the beginning, and the people who were more on Facebook were less.  
**Translation:** Vocabulary: polarized: 立场对立

**[7264.00s] English:** Polarized: Um, there's a study you know from Stanford of economists at Stanford that  
**Translation:** 

**[7271.20s] English:** Tried to identify the causes of increasing polarization in the US.  
**Translation:** Vocabulary: economists: 经济学家; polarization: 极化

**[7275.92s] English:** And it's been going on for 40 years before you know, Mark Zuckerberg was born, yeah, uh, continuously.  
**Translation:** 

**[7282.48s] English:** And, um, and uh, so if there is a cause, it's not Facebook or social media, so you could say if.  
**Translation:** 

**[7288.08s] English:** Social media has just accelerated, but no; I mean, it's basically a continuous, uh, evolution by some measure.  
**Translation:** 

**[7293.68s] English:** Of polarization in the U.S., and then you compare this with other countries, like, uh, the United Kingdom.  
**Translation:** Vocabulary: accelerated: 加速

**[7300.08s] English:** West half of Germany, because you can go 40 years in the east, East Side or Denmark or other.  
**Translation:** 

**[7306.08s] English:** Countries, uh, and they use Facebook just as much, and they're not getting more polarized.  
**Translation:** Vocabulary: denmark: 丹麦

**[7310.56s] English:** Are we getting less polarized? So, if you want to look for a causal relationship there,  
**Translation:** 

**[7317.52s] English:** You can find a scapegoat, but you can't find a cause.  
**Translation:** Vocabulary: causal: 因果的; scapegoat: 替罪羊

**[7320.00s] English:** You want to fix the problem, you have to find the right cause, and what rises me up is that people now  
**Translation:** 

**[7325.44s] English:** Are accusing Facebook of bad deeds that are done by others, and those others are not doing.  
**Translation:** 

**[7330.64s] English:** Anything about them, and by the way, those others include, uh, the owner of The Wall Street Journal.  
**Translation:** 

**[7335.52s] English:** In which all of those papers were published, so I should mention that I'm talking to ShREP Mike.  
**Translation:** 

**[7340.48s] English:** Shreep on this podcast, and also Mark Zuckerberg—and probably these conversations can have.  
**Translation:** 

**[7344.96s] English:** They, uh, because it's very interesting to me, even if Facebook has some measurable negative effects.  
**Translation:** Vocabulary: measurable: 可衡量的; zuckerberg: 扎克伯格

**[7351.76s] English:** You can't just consider that in isolation; you have to consider all the positive ways it affects things.  
**Translation:** 

**[7356.16s] English:** Connects us, so, like, every technology — people, it's a question you can't just say, "like, uh, there's an  
**Translation:** 

**[7362.16s] English:** An increase in division, yes. Probably Google's search engine has created an increase in division; we have.  
**Translation:** 

**[7368.00s] English:** To consider how much information is brought to the world, I'm sure Wikipedia has created more.  
**Translation:** 

**[7373.04s] English:** Division: If you just look at the division.  
**Translation:** 

**[7374.96s] English:** And we have to look at the full context of the world, and they didn't make a better world.  
**Translation:** 

**[7379.52s] English:** The printing press has created more differences, right? Exactly; I mean,...  
**Translation:** 

**[7382.96s] English:** So, you know, when the printing press was invented, the first books that were printed...  
**Translation:** 

**[7389.20s] English:** Were things like the Bible and that allowed people to read the Bible by themselves not get the  
**Translation:** 

**[7394.08s] English:** Message uniquely from priests in Europe, and that created, you know, the Protestant movement, and 200.  
**Translation:** 

**[7401.20s] English:** Years of religious persecution and wars, so that's a bad side effect.  
**Translation:** 

**[7404.96s] English:** Of the printing press, you know, social networks aren't being nearly as bad.  
**Translation:** Vocabulary: persecution: 迫害

**[7408.32s] English:** As with the printing press, but nobody would say the printing press was a bad idea.  
**Translation:** 

**[7413.44s] English:** Yeah, a lot of this perception, and there are a lot of different incentives operating here.  
**Translation:** Vocabulary: incentives: 激励; perception: 看法

**[7418.48s] English:** Maybe a quick comment since you're one of the top leaders at Facebook and in at Meta, sorry.  
**Translation:** 

**[7424.32s] English:** That's in the tech space; I'm sure Facebook involves a lot of incredible technology.  
**Translation:** 

**[7431.36s] English:** Challenges that need to be solved; a lot of it probably is on the computer infrastructure, and  
**Translation:** 

**[7434.96s] English:** The hardware, I mean, it's just a huge amount. Maybe you could give me a call.  
**Translation:** 

**[7440.00s] English:** Context about how much of Shrepp's life is AI, and how much of it is low-level compute,  
**Translation:** 

**[7446.32s] English:** How much of it is flying all around doing business stuff, and the same with Mark Zuckerberg?  
**Translation:** Vocabulary: compute: 计算; zuckerberg: 扎克伯格

**[7452.16s] English:** They really focus on AI. Certainly, in the run-up to the Creation Affair, and for at least  
**Translation:** 

**[7461.72s] English:** A year after that, if not more, Mark was very, very much focused on AI and was spending quite a bit of time on it.  
**Translation:** 

**[7467.68s] English:** A lot of effort into it, and that's his style. When he gets interested in something, he reads  
**Translation:** 

**[7472.34s] English:** Everything about it. He read some of my papers, for example, before I joined. He learned,  
**Translation:** 

**[7481.36s] English:** Lots about it.  
**Translation:** 

**[7482.36s] English:** That would be great if he sent you notes.  
**Translation:** 

**[7487.98s] English:** Shrepp was really into it, too. Shrepp has something I've tried to preserve.  
**Translation:** 

**[7497.56s] English:** All along.  
**Translation:** 

**[7497.68s] English:** Also, despite my not-so-young age, there is still a sense of wonder about science and technology.  
**Translation:** 

**[7503.28s] English:** And he certainly has that. He's also a wonderful person in terms of how he manages and deals with people.  
**Translation:** 

**[7510.86s] English:** With people and everything. Marc, as well. They're very human people. In the case of  
**Translation:** 

**[7518.48s] English:** Marc, it's shockingly human, given his trajectory. I mean, the personality of him that is painted,...  
**Translation:** Vocabulary: shockingly: 惊人地; trajectory: 轨迹

**[7527.60s] English:** In the press is just completely wrong.  
**Translation:** 

**[7529.56s] English:** Yeah, but you have to know how to play the press. I put some of that responsibility on him.  
**Translation:** 

**[7534.92s] English:** On him, too. It's like the conductor of an orchestra; you have to play the presses.  
**Translation:** 

**[7545.60s] English:** The public, in a certain kind of way, where you convey  
**Translation:** Vocabulary: conductor: 乐队指挥; presses: 印刷机

**[7548.46s] English:** Your true self to them, if there's a depth of kindness in you.  
**Translation:** 

**[7551.46s] English:** It's hard. And he's probably not the best at it. So, yeah.  
**Translation:** 

**[7555.22s] English:** You have to learn. And it's sad to see,... I'll talk to him.  
**Translation:** 

**[7560.00s] English:** About it, but the strep is slowly stepping down. It's always uh sad to see folks sort of be there.  
**Translation:** Vocabulary: strep: 链球菌

**[7567.44s] English:** For a long time, and slowly, I guess. Time, you know—I think he's done the thing he needed to do.  
**Translation:** 

**[7573.84s] English:** Set out to do, and you know, he's got you know, uh, family priorities and stuff like that, and  
**Translation:** Vocabulary: priorities: 优先事项

**[7582.16s] English:** Um, I understand; you know, after 13 years or so, it's been a good run, which in silicon.  
**Translation:** 

**[7589.68s] English:** Valley is basically a lifetime, yeah. You know, because you know it's dog years, so in Europe's.  
**Translation:** 

**[7596.00s] English:** The conference just wrapped up. Uh, let me just go back to something else. You posted the paper you?  
**Translation:** 

**[7601.76s] English:** Co-authored was rejected from Europe's, as you said proudly, "in quotes, rejected." Can you joke, yeah? I  
**Translation:** Vocabulary: proudly: 自豪地; quotes: 引号

**[7609.20s] English:** Know, uh, can you describe this paper and, like, what was the idea behind it? And also, maybe, this is a good  
**Translation:** 

**[7619.68s] English:** Example of what the idea was in it, and what are the pros and cons, what works and what doesn't about  
**Translation:** 

**[7624.80s] English:** The review process: yeah, let me talk about the paper first. I'll talk about the review.  
**Translation:** 

**[7629.28s] English:** The review process, uh, afterwards, um, the paper is called VicReg; so, I mentioned that before.  
**Translation:** 

**[7635.36s] English:** Variance, Invariance, Covariance, Regularization, and it's a technique for non-contrastive learning.  
**Translation:** 

**[7640.64s] English:** Technique for what I call joint embedding architecture, so Sami's nets are an example.  
**Translation:** Vocabulary: covariance: 协方差; embedding: 嵌入; invariance: 不变性; variance: 方差

**[7646.16s] English:** Of joint embedding architecture, so a gentleman in architecture is uh  
**Translation:** 

**[7649.68s] English:** A beginner in architecture, so he's an amateur in the field.  
**Translation:** Vocabulary: amateur: 初学者

**[7652.64s] English:** Of joint embedding architecture, so he's a beginner in architecture.  
**Translation:** 

**[7656.32s] English:** If you want to do self-supervised learning, you can do it by prediction.  
**Translation:** 

**[7661.28s] English:** So, let's say you want to train your system to predict video. You show it a video clip and  
**Translation:** 

**[7666.08s] English:** Uh, and you train the system to predict the next continuation of that video clip, now because  
**Translation:** Vocabulary: continuation: 后续

**[7670.80s] English:** You need to handle uncertainty because there are many, you know, plausible continuations that are possible.  
**Translation:** 

**[7676.40s] English:** You need to handle this in some way, and you need to have.  
**Translation:** Vocabulary: continuations: 后续情况; plausible: 合乎情理的

**[7679.68s] English:** Thanks for watching!  
**Translation:** 

**[7680.00s] English:** And the way—the only way I know—to do this is through what's called a latent variable.  
**Translation:** 

**[7685.44s] English:** So, you have some sort of hidden vector of a variable that you can vary over a set or draw from a distribution.  
**Translation:** 

**[7692.56s] English:** And as you vary this vector over a set, the output (the prediction) varies over a set of plausible predictions.  
**Translation:** 

**[7698.48s] English:** Okay, so that's called a generative latent variable model. I call it that.  
**Translation:** 

**[7703.88s] English:** Got it.  
**Translation:** Vocabulary: generative: 生成的

**[7704.74s] English:** Okay.  
**Translation:** 

**[7705.24s] English:** Now, there is an alternative to this to handle uncertainty.  
**Translation:** 

**[7707.86s] English:** And instead of directly predicting the next frames of the clip, you also run those through another neural network.  
**Translation:** 

**[7720.54s] English:** So, you now have two neural nets: one that looks at the initial segment of the video clip.  
**Translation:** Vocabulary: neural: 神经网络; segment: 片段

**[7728.56s] English:** And another one that looks at the continuation during training, right?  
**Translation:** 

**[7733.24s] English:** And what you're trying to do is learn a representation of.  
**Translation:** 

**[7737.86s] English:** Those two video clips are maximally informative about the video clips themselves, but it's such that you can predict the representation of the second video clip from the representation of the first one easily.  
**Translation:** 

**[7751.24s] English:** Okay.  
**Translation:** Vocabulary: informative: 有信息量的

**[7752.26s] English:** And you can sort of formalize this in terms of maximizing mutual information and some stuff like that, but it doesn't matter.  
**Translation:** 

**[7757.36s] English:** Uh, what you want is, uh, informative and representative, you know, informative and representative representations of the two video clips that are mutually predictive.  
**Translation:** Vocabulary: maximizing: 最大化; mutually: 相互; predictive: 可预测的; representations: 表示

**[7767.86s] English:** Uh, but that means there are a lot of details in the second video clips that are irrelevant.  
**Translation:** 

**[7773.50s] English:** Uh, you know, um, I'll say that a video clip consists of, you know, a camera panning the scene.  
**Translation:** Vocabulary: irrelevant: 无关的

**[7781.72s] English:** Uh, there's going to be a piece of that room that is going to be revealed, and I can somewhat predict what the room is going to look like.  
**Translation:** 

**[7788.08s] English:** But I may not be able to predict the details of the texture of the ground and where the tiles are ending, and stuff like that.  
**Translation:** 

**[7794.32s] English:** Right?  
**Translation:** 

**[7794.54s] English:** So, those are irrelevant details that perhaps.  
**Translation:** 

**[7797.16s] English:** My representation will eliminate.  
**Translation:** 

**[7799.40s] English:** And so.  
**Translation:** 

**[7800.00s] English:** So, what I need is to train this second neural net in such a way that, whenever the continuation video clip varies over all the plausible continuations, the representation doesn't change.  
**Translation:** 

**[7815.62s] English:** Got it.  
**Translation:** Vocabulary: continuation: 后续; continuations: 多种可能的后续; neural: 神经; plausible: 合理的

**[7816.22s] English:** Okay.  
**Translation:** 

**[7816.90s] English:** Yeah, yeah.  
**Translation:** 

**[7817.56s] English:** Got it.  
**Translation:** 

**[7818.20s] English:** Over the span of representations, doing the same kind of thing as you are doing with similarity learning.  
**Translation:** Vocabulary: similarity: 相似性

**[7824.24s] English:** Right.  
**Translation:** 

**[7825.40s] English:** Yeah.  
**Translation:** 

**[7825.60s] English:** So, these are two ways to handle multimodality in a prediction, right?  
**Translation:** 

**[7829.54s] English:** In the first way, you parameterize the prediction with a latent variable, but you predict pixels, essentially, right?  
**Translation:** Vocabulary: multimodality: 多种模态; parameterize: 参数化; pixels: 像素

**[7835.74s] English:** In the second one, you don't predict pixels.  
**Translation:** 

**[7838.40s] English:** You predict an abstract representation of pixels, and you guarantee that this abstract representation has as much information as possible about the input, but sort of drops all the stuff that you really can't predict, essentially.  
**Translation:** 

**[7851.70s] English:** I used to be a big fan of the first approach.  
**Translation:** 

**[7853.58s] English:** And, in fact, in this paper with Ishan Mishra and this blog post, "The Dark Matter of Intelligence," I was kind of advocating for this.  
**Translation:** Vocabulary: advocating: 提倡

**[7859.54s] English:** And in the last year and a half, I've completely changed my mind.  
**Translation:** 

**[7862.80s] English:** I'm now a big fan of the second one.  
**Translation:** 

**[7865.20s] English:** And it's because of a small collection of algorithms that have been proposed over the last year and a half or so, including vCrag.  
**Translation:** 

**[7877.56s] English:** Its predecessor, called Barlow-Twins, which I mentioned, is a method from our friends at DeepMind called BYOL, and there are now a bunch of others that kind of work similarly.  
**Translation:** Vocabulary: predecessor: 前一个版本

**[7889.64s] English:** So, they're all based on this idea of joint embedding.  
**Translation:** 

**[7892.62s] English:** Some of them have an explicit criterion that is an approximation of mutual information.  
**Translation:** Vocabulary: approximation: 近似; criterion: 标准; embedding: 嵌入; explicit: 明确的

**[7896.54s] English:** Some others work at BYOL, but we don't really know why.  
**Translation:** 

**[7899.42s] English:** And there have been, like, lots of theoretical papers about why BYOL works.  
**Translation:** 

**[7902.38s] English:** No, it's not that, because we take it out and it still works, and blah, blah, blah.  
**Translation:** 

**[7905.92s] English:** I mean, so there's like a big debate.  
**Translation:** 

**[7908.04s] English:** But the important point is that we now have a collection of non-contrastive joint embedding methods, which I think is the best thing since sliced bread.  
**Translation:** 

**[7916.46s] English:** So, I'm super excited about this, because I think...  
**Translation:** Vocabulary: sliced: 切片面包

**[7919.54s] English:** It's so big.  
**Translation:** 

**[7920.00s] English:** Shot for techniques that would allow us to kind of build predictive world models, and at the same  
**Translation:** Vocabulary: predictive: 预测性的

**[7927.04s] English:** Time to learn hierarchical representations of the world, where what matters about the world is  
**Translation:** 

**[7931.20s] English:** Preserved, and what is irrelevant is eliminated. By the way, the representations—the before and  
**Translation:** Vocabulary: hierarchical: 层次分明的; irrelevant: 无关的; representations: 表示方式

**[7936.32s] English:** After that, is it across in the space in a sequence of images, or is it for single images? It would be  
**Translation:** 

**[7942.64s] English:** Either for a single image or a sequence, it doesn't have to be images; this could be applied.  
**Translation:** 

**[7946.08s] English:** To text, this could be applied to just about any signal. I'm looking at it, you know, I'm looking for...  
**Translation:** 

**[7951.20s] English:** Methods that are generally applicable and not specific to one particular modality.  
**Translation:** Vocabulary: modality: 方式

**[7955.76s] English:** You know, it could be audio or whatever. Got it, so what's the story behind this paper? This...  
**Translation:** 

**[7960.16s] English:** Paper is what is describing one of the methods, this being the VicRec method, so this is co-authored.  
**Translation:** 

**[7965.36s] English:** Uh, the first author is a student, uh, named Adrian Bound, who is a resident PhD student at Paris Sorbonne University.  
**Translation:** 

**[7972.48s] English:** Who is co-advised by me and Jean Pons?  
**Translation:** Vocabulary: adrian: 阿德里安; sorbonne: 索邦大学

**[7976.08s] English:** Uh, Professor at Economic Superior, also a Research Director at INRIA. So, this is a wonderful program in.  
**Translation:** 

**[7983.12s] English:** France, where PhD students can basically do their PhD in industry, and that's kind of what it's like.  
**Translation:** 

**[7988.08s] English:** Happening here, um, and this paper is a follow-up on the bottle-twin paper by my former  
**Translation:** 

**[7996.48s] English:** Postdoc now, Stephanie with Lijing and Yorish Montar, and a bunch of other people from Fair.  
**Translation:** Vocabulary: postdoc: 博士后

**[8004.56s] English:** And one of the main  
**Translation:** 

**[8006.08s] English:** Criticisms from reviewers is that V. Craig is not different enough from the Bottle Twins, but  
**Translation:** 

**[8012.88s] English:** You know, my impression is that it's basically bottle twins with a few bugs fixed.  
**Translation:** 

**[8020.24s] English:** In the end, this is what people will use, right? So, but you know, I'm used to stuff, yeah.  
**Translation:** 

**[8027.12s] English:** Submit, being rejected for so it might be rejected, and actually exceptionally well-cited because.  
**Translation:** 

**[8031.36s] English:** People use it well; it's already decided, like a bunch of times. So, I mean, the question is...  
**Translation:** Vocabulary: exceptionally: 特别地; submit: 提交

**[8036.08s] English:** Then, there's the deeper question about peer review and conferences.  
**Translation:** 

**[8040.00s] English:** I mean, computer science is a field that's kind of unique in that the conference is highly prized.  
**Translation:** Vocabulary: conferences: 学术会议; prized: 受重视

**[8044.94s] English:** That's one.  
**Translation:** 

**[8046.12s] English:** And it's interesting because the peer review process there is similar, I suppose, to journals, but it's accelerated significantly.  
**Translation:** 

**[8053.62s] English:** Well, not significantly, but it goes fast.  
**Translation:** 

**[8056.42s] English:** And it's a nice way to get stuff out quickly, to peer-review it quickly, and go on to present it quickly to the community.  
**Translation:** 

**[8062.68s] English:** So, not quickly, but quicker.  
**Translation:** 

**[8065.10s] English:** Yeah.  
**Translation:** 

**[8065.26s] English:** But, nevertheless, it has many of the same flaws as peer review because it's a limited number of people who look at it.  
**Translation:** 

**[8071.50s] English:** There's bias.  
**Translation:** 

**[8072.68s] English:** If you want to do new ideas, you're going to get pushback.  
**Translation:** 

**[8078.06s] English:** There are self-interested people who can infer who submitted it and be cranky about it, and all that kind of stuff.  
**Translation:** Vocabulary: cranky: 爱发脾气; pushback: 反对意见

**[8087.72s] English:** Yeah.  
**Translation:** 

**[8087.98s] English:** I mean, there are a lot of social phenomena there.  
**Translation:** 

**[8090.66s] English:** There's one social phenomenon: which is that, because the field has been growing exponentially,  
**Translation:** 

**[8095.26s] English:** The vast majority of people in the field are extremely junior.  
**Translation:** Vocabulary: exponentially: 成指数地

**[8100.46s] English:** So, as a consequence, and that's just a consequence of the field growing, right?  
**Translation:** 

**[8104.90s] English:** So, as the size of the field starts to saturate, you will have less of that problem of reviewers being very inexperienced.  
**Translation:** Vocabulary: inexperienced: 缺乏经验的

**[8115.32s] English:** A consequence of this is that young reviewers; I mean, there's a phenomenon where reviewers try to make their lives easy.  
**Translation:** 

**[8124.50s] English:** And to make their life easier.  
**Translation:** 

**[8125.24s] English:** Yeah.  
**Translation:** 

**[8125.28s] English:** And to make their life easy when reviewing a paper, it is very simple.  
**Translation:** 

**[8128.02s] English:** You just have to find a flaw in the paper, right?  
**Translation:** 

**[8130.02s] English:** So, basically, they see their task as finding flaws in papers.  
**Translation:** 

**[8134.56s] English:** And most papers have flaws, even the good ones.  
**Translation:** 

**[8137.84s] English:** So, it's easy to do that.  
**Translation:** 

**[8141.62s] English:** Your job is easier as a reviewer, if you just focus on this.  
**Translation:** 

**[8146.40s] English:** But what's important is: Is there a new idea in that paper that is likely to influence?  
**Translation:** 

**[8153.74s] English:** It doesn't matter if the experiment...  
**Translation:** 

**[8155.24s] English:** If the experiments aren't that great, if the protocol is, you know, so...  
**Translation:** Vocabulary: experiments: 实验

**[8160.00s] English:** So, you know, things like that, as long as there is a worthy idea in it that will influence...  
**Translation:** 

**[8166.06s] English:** The way people think about the problem, even if they make it better, you know, eventually.  
**Translation:** 

**[8171.16s] English:** I think that's really what makes a paper useful.  
**Translation:** 

**[8175.60s] English:** And so, this combination of social phenomena creates a disease that has plagued, you know,  
**Translation:** Vocabulary: plagued: 困扰

**[8184.30s] English:** Other fields in the past, like speech recognition, where basically, people have chased numbers.  
**Translation:** 

**[8188.42s] English:** On benchmarks, and it's much easier to get a paper accepted if it brings an incremental improvement.  
**Translation:** Vocabulary: benchmarks: 评估标准; chased: 追求; incremental: 增量的

**[8196.36s] English:** Improvement on a sort of mainstream, well-accepted method or problem.  
**Translation:** 

**[8204.24s] English:** And those, to me, are boring papers.  
**Translation:** 

**[8206.00s] English:** I mean, they're not useless, right? Because industry, you know, strives on those kinds  
**Translation:** 

**[8211.16s] English:** Of progress, but they're not the ones that I'm interested in, in terms of new concepts.  
**Translation:** 

**[8215.18s] English:** And new ideas.  
**Translation:** 

**[8216.18s] English:** So, papers that are really useful.  
**Translation:** 

**[8218.18s] English:** Yeah.  
**Translation:** 

**[8218.38s] English:** Yeah.  
**Translation:** 

**[8218.42s] English:** Trying to strike kind of new advances generally don't make it.  
**Translation:** 

**[8222.36s] English:** Now, thankfully, we have archives.  
**Translation:** Vocabulary: advances: 进展; archives: 档案

**[8224.04s] English:** Archive, exactly.  
**Translation:** 

**[8225.40s] English:** And then there's open review-type situations, where you and then, I mean, Twitter's a kind  
**Translation:** Vocabulary: archive: 存档

**[8230.26s] English:** Of open review.  
**Translation:** 

**[8231.26s] English:** I'm a huge believer that reviews should be done by thousands of people, not just two.  
**Translation:** Vocabulary: believer: 相信者

**[8235.66s] English:** I agree.  
**Translation:** 

**[8236.66s] English:** And so, archive: Do you see a future where a lot of really strong papers are?  
**Translation:** 

**[8241.32s] English:** Already in the present, but a growing future where it'll just be an archive, and you're presenting.  
**Translation:** 

**[8248.38s] English:** An ongoing, continuous conference called "Twitter/Internet/Archive Sanity.  
**Translation:** 

**[8251.38s] English:** Andre just released a new version.  
**Translation:** 

**[8252.38s] English:** So, just not being so elitist about this particular gatekeeping.  
**Translation:** Vocabulary: elitist: 等级主义; gatekeeping: 把关

**[8253.38s] English:** It's not a question of being elitist or not.  
**Translation:** 

**[8254.38s] English:** It's a question of being, basically, a recommendation and approval process for people who don't see themselves  
**Translation:** Vocabulary: recommendation: 推荐

**[8255.38s] English:** As they have the ability to do so by themselves, right?  
**Translation:** 

**[8256.38s] English:** And so it saves time, right?  
**Translation:** 

**[8257.38s] English:** If you rely on the fact that you can't just say, "we're going" to do it.  
**Translation:** 

**[8258.38s] English:** Do this, and we're going to do that.  
**Translation:** 

**[8259.38s] English:** You know, we're going to do that.  
**Translation:** 

**[8260.38s] English:** You know, I think the fact that you can't just say, "We're going to do this,  
**Translation:** 

**[8261.38s] English:** And we're going to do that, right?  
**Translation:** 

**[8262.38s] English:** It's not a question of being elitist; it's a question of being, you know, justified in our approach.  
**Translation:** 

**[8263.38s] English:** To do this, and we're going to do that.  
**Translation:** 

**[8264.38s] English:** It's not a question of being elitist or not.  
**Translation:** 

**[8265.38s] English:** It's a question of being, basically, a recommendation and approval process for people who don't see themselves  
**Translation:** 

**[8273.28s] English:** As they have the ability to do so by themselves, right?  
**Translation:** 

**[8275.76s] English:** And so it saves time, right?  
**Translation:** 

**[8277.34s] English:** If you rely on other people's opinions.  
**Translation:** 

**[8280.00s] English:** You trust those people or those groups to evaluate a paper for you, saving you time because you  
**Translation:** 

**[8290.16s] English:** Know that you don't have to scrutinize the paper too much, you know; it is brought to your attention.  
**Translation:** Vocabulary: evaluate: 评估; scrutinize: 仔细检查

**[8294.32s] English:** Attention; I mean, it's the whole idea of a sort of you-know collective recommender system, right?  
**Translation:** 

**[8298.64s] English:** So, I actually thought about this a lot, um, you know, about 10 to 15 years ago, because there were  
**Translation:** Vocabulary: recommender: 推荐系统

**[8304.40s] English:** Discussions at NIPS, and you know, we're about to create iClear with Yosha Benjo, and so I wrote.  
**Translation:** 

**[8311.92s] English:** A document, kind of describing a reviewing system, which basically was: you know, you post,...  
**Translation:** 

**[8318.24s] English:** Your paper on, say, a repository like an archive, could be open review, and then you can form  
**Translation:** 

**[8324.48s] English:** Uh, a reviewing entity, which is equivalent to a reviewing board, you know, of a journal or  
**Translation:** Vocabulary: archive: 文献收藏; repository: 存储库

**[8331.52s] English:** Program Committee of a conference, you have to list:  
**Translation:** 

**[8334.40s] English:** The members, and then that group reviewing entity, can choose to review a particular paper.  
**Translation:** 

**[8342.40s] English:** Spontaneously, or not, there is no longer an exclusive relationship anymore between  
**Translation:** 

**[8346.16s] English:** A paper and a venue (or reviewing entity) can be reviewed by any reviewing entity.  
**Translation:** Vocabulary: spontaneously: 自行其是

**[8352.64s] English:** Or, they may choose not to, and then you know, give an evaluation; it's not published.  
**Translation:** 

**[8357.44s] English:** Published, it's just an evaluation and a comment which would be public, signed by the reviewer.  
**Translation:** Vocabulary: evaluation: 评估

**[8362.56s] English:** Entity and  
**Translation:** 

**[8364.40s] English:** If it's signed by a reviewing entity, you know it's one of the members of the reviewing entity, so  
**Translation:** 

**[8367.84s] English:** If the reviewing entity is, for example, Lex Friedman's preferred papers, right, it's  
**Translation:** 

**[8374.00s] English:** Lex Friedman writing a review, yes? What, so for me, one that's a beautiful, uh, system, I think.  
**Translation:** Vocabulary: friedman: 弗里德曼

**[8381.44s] English:** What's in addition to that, it feels like there should be a reputation system for the reviewers.  
**Translation:** 

**[8387.36s] English:** For the reviewing entities, not the reviewers individually, the reviewing entities sure.  
**Translation:** Vocabulary: individually: 单独地

**[8391.60s] English:** But even that, within that, the reviewers, too, because uh  
**Translation:** 

**[8394.40s] English:** There's another thing here; it's not just the reputation, it's an incentive.  
**Translation:** Vocabulary: incentive: 激励

**[8400.00s] English:** For an individual person to do great right now in the academic setting, the incentive is kind of  
**Translation:** 

**[8406.30s] English:** Internal employees just want to do a good job, but honestly, that's not a strong enough incentive.  
**Translation:** 

**[8411.10s] English:** To do a really good job in reading a paper and finding the beautiful amidst the mistakes,  
**Translation:** 

**[8415.96s] English:** The flaws, and all that kind of stuff, right? Like, if you're the person who first discovered...  
**Translation:** Vocabulary: amidst: 在……之中

**[8420.26s] English:** A powerful paper, and you get to be proud of that discovery; then that gives a huge incentive to you.  
**Translation:** 

**[8427.50s] English:** That's a big part of my proposal, actually. You know, I describe that as...  
**Translation:** 

**[8432.12s] English:** Evaluation of papers is predictive of future success, yes. Okay, then your reputation should  
**Translation:** 

**[8438.78s] English:** Go up as a reviewing entity, so yeah, exactly. I mean, that—that I even had a master's student who  
**Translation:** Vocabulary: evaluation: 评估; predictive: 预测性的

**[8446.40s] English:** Is a master's student in library science and computer science actually kind of working out?  
**Translation:** 

**[8451.24s] English:** Exactly, how that should work with formulas and everything, but so in terms of implementation, do  
**Translation:** Vocabulary: formulas: 公式; implementation: 实现

**[8456.88s] English:** You think that's something?  
**Translation:** 

**[8457.48s] English:** That's doable. I mean, I've been sort of talking about this to various people, like...  
**Translation:** Vocabulary: doable: 可行的

**[8462.40s] English:** You know, Andrew McCallum, who started open review, and the reason why we picked open review for iClear.  
**Translation:** 

**[8468.52s] English:** Initially, even though it was very early for them, is because my hope was that I could clear where it was.  
**Translation:** 

**[8474.70s] English:** Eventually, we're going to kind of inaugurate this type of system, so iClear kept the idea of open reviews.  
**Translation:** 

**[8481.84s] English:** So, where the reviews are published with the paper, which I think is very useful.  
**Translation:** Vocabulary: inaugurate: 正式启用

**[8487.18s] English:** But  
**Translation:** 

**[8487.48s] English:** Yeah, but in many ways, that's kind of reverted to more of a conventional type of conference.  
**Translation:** Vocabulary: conventional: 传统的; reverted: 回归

**[8493.12s] English:** For everything else, and that I mean—I don't run iClear; I'm just the president of the foundation.  
**Translation:** 

**[8501.24s] English:** But, um, you know, people who run it should make decisions about how to run it, and I'm not going.  
**Translation:** 

**[8506.26s] English:** To tell them, because there are volunteers, and I'm really thankful that they do that. So, but I'm  
**Translation:** 

**[8512.02s] English:** Saddened by the fact that we're not being innovative enough, yeah. I mean, just to say, "Yeah, I love it.  
**Translation:** Vocabulary: innovative: 有创新的

**[8517.48s] English:** I hope that changes, yeah.  
**Translation:** 

**[8520.00s] English:** Because the communication of science is broad, but the communication of computer science,  
**Translation:** 

**[8523.44s] English:** Ideas is how you make those ideas have impact, I think.  
**Translation:** 

**[8528.24s] English:** Yeah.  
**Translation:** 

**[8529.24s] English:** And I think a lot of this is because people have in their minds kind of an objective, which  
**Translation:** 

**[8536.34s] English:** Is fairness for authors and the ability to count points, basically, and give credits?  
**Translation:** 

**[8543.44s] English:** Accurately.  
**Translation:** 

**[8544.94s] English:** But that comes at the expense of the progress of science.  
**Translation:** 

**[8548.94s] English:** So, to some extent, we're slowing down the progress of science.  
**Translation:** 

**[8551.50s] English:** And are we actually achieving fairness?  
**Translation:** 

**[8553.84s] English:** And we're not achieving fairness.  
**Translation:** 

**[8555.94s] English:** We still have biases.  
**Translation:** Vocabulary: biases: 偏见

**[8558.14s] English:** We're doing a double-blind review, but the biases are still there.  
**Translation:** 

**[8564.38s] English:** There are different kinds of biases.  
**Translation:** 

**[8566.18s] English:** You write that the phenomenon of emergence, which is collective behavior exhibited by a large collection,  
**Translation:** 

**[8571.58s] English:** Of simple elements in interaction, that's one of the things that got you into neural nets.  
**Translation:** Vocabulary: emergence: 涌现; exhibited: 表现; neural: 神经

**[8576.68s] English:** In the first place.  
**Translation:** 

**[8577.68s] English:** I love cellular automata.  
**Translation:** Vocabulary: automata: 自动机; cellular: 细胞的

**[8578.68s] English:** I love it.  
**Translation:** 

**[8578.94s] English:** I love simple interacting elements, and the things that emerge from them.  
**Translation:** Vocabulary: interacting: 交互

**[8584.08s] English:** Do you think we understand how complex systems can emerge from such simple components?  
**Translation:** 

**[8589.84s] English:** Interact simply?  
**Translation:** 

**[8590.84s] English:** No, we don't.  
**Translation:** 

**[8592.42s] English:** It's a big mystery.  
**Translation:** 

**[8593.42s] English:** Also, it's a mystery for physicists.  
**Translation:** 

**[8594.42s] English:** It's a mystery for biologists.  
**Translation:** Vocabulary: biologists: 生物学家; physicists: 物理学家

**[8598.02s] English:** How is it that the universe around us seems to be increasing in complexity, and not decreasing?  
**Translation:** 

**[8604.74s] English:** I mean, that is a kind of curious property.  
**Translation:** Vocabulary: complexity: 复杂性; decreasing: 减少

**[8608.68s] English:** Even though there are many theories about physics that defy the second law of thermodynamics,  
**Translation:** 

**[8618.38s] English:** Evolution and learning, etc., seem to be, at least locally, to increase complexity.  
**Translation:** Vocabulary: thermodynamics: 热力学

**[8623.58s] English:** Not decrease it.  
**Translation:** 

**[8624.58s] English:** So, perhaps the ultimate purpose of the universe is to just get more complex.  
**Translation:** 

**[8628.84s] English:** These have small pockets of beautiful complexity.  
**Translation:** 

**[8632.74s] English:** Does cellular automata, in these kinds of emergence and complexity, have a way?  
**Translation:** 

**[8635.44s] English:** To do that?  
**Translation:** 

**[8636.44s] English:** Is that the answer?  
**Translation:** 

**[8637.44s] English:** It's a big question.  
**Translation:** 

**[8638.44s] English:** And complex systems give you  
**Translation:** 

**[8640.00s] English:** Some intuition or guidance can help you understand machine learning systems and neural networks.  
**Translation:** 

**[8646.16s] English:** And so on, or are these for you right now disparate concepts? Well, it got me thinking, you know.  
**Translation:** Vocabulary: intuition: 直觉

**[8651.36s] English:** Uh, I discovered the existence of the perceptron when I was a college student, you know, by reading.  
**Translation:** 

**[8658.88s] English:** A book on it was a debate between Chomsky and Piaget, and Seymour Pepper from MIT; he was kind.  
**Translation:** Vocabulary: chomsky: 诺姆·乔姆斯基; perceptron: 感知器; piaget: 让·皮亚杰; seymour: 西摩尔

**[8664.56s] English:** Of singing the praise of the perceptron in that book, and I, for the first time, heard about it.  
**Translation:** 

**[8669.04s] English:** Learning machines, right? So I started digging through the literature and found those papers and books.  
**Translation:** 

**[8673.36s] English:** Which were basically transcriptions of known workshops or conferences from the 1950s and 1960s.  
**Translation:** 

**[8679.76s] English:** About self-organizing systems, so there was a series of conferences on self-organizing.  
**Translation:** Vocabulary: conferences: 研讨会; transcriptions: 记录

**[8685.28s] English:** Systems and theses books on this; some of them are you can actually get them at the Internet.  
**Translation:** 

**[8690.72s] English:** Archive, you know, the digital version, and there are some fascinating articles in there by...  
**Translation:** Vocabulary: archive: 文献收藏

**[8698.16s] English:** There's a guy who's named  
**Translation:** 

**[8699.04s] English:** Heinz von Foerster, a German physicist who immigrated to the U.S., has been largely forgotten.  
**Translation:** Vocabulary: foerster: 冯·福斯特; heinz: 海因茨; immigrated: 移民; physicist: 物理学家

**[8706.16s] English:** And, uh, he worked on self-organizing systems in the 1950s and 1960s. He created  
**Translation:** 

**[8712.72s] English:** At the University of Illinois Urbana-Champaign, he created the Biological Computer Laboratory (BCL).  
**Translation:** 

**[8718.72s] English:** Which was, you know, all about neural nets. Unfortunately, that was kind of towards the end.  
**Translation:** 

**[8723.28s] English:** Of the popularity of neural nets, so that that lab never really strove very much, but he wrote a  
**Translation:** Vocabulary: neural: 神经; popularity: 流行度; strove: 努力

**[8729.04s] English:** Several papers about self-organization and the mystery of self-organization; an example he has is:  
**Translation:** 

**[8735.36s] English:** You take, imagine you are in space, where there's no gravity. You have a big box with magnets in it.  
**Translation:** Vocabulary: gravity: 重力; magnets: 磁铁

**[8741.12s] English:** Okay, you know, kind of rectangular magnets with a north pole on one end, so that's well, on the other.  
**Translation:** 

**[8746.48s] English:** End. You shake the box gently, and the magnets will kind of stick to themselves and probably form a  
**Translation:** Vocabulary: gently: 轻轻地; rectangular: 长方形的

**[8751.28s] English:** Complex structures, um, you know, can spontaneously arise through self-organization, you know.  
**Translation:** 

**[8757.20s] English:** But, you know, you have lots of examples; neural nets are an example of that kind of thing. So, that's why we're here today.  
**Translation:** Vocabulary: spontaneously: 自行形成

**[8759.04s] English:** Example of self-organization.  
**Translation:** 

**[8760.00s] English:** To you know, in many respects, and it's a bit of a mystery, you know, how like what is  
**Translation:** 

**[8767.86s] English:** Possible with this, you know, pattern formation in physical systems in chaotic systems and things.  
**Translation:** 

**[8773.20s] English:** Like that, you know, such as the emergence of life, and things like that. So, you know, how does  
**Translation:** Vocabulary: chaotic: 无序的; emergence: 出现

**[8777.68s] English:** How does that happen? It's a big puzzle for physicists, as well. It feels like understanding...  
**Translation:** 

**[8783.56s] English:** This is the mathematics of emergence in some constrained situations, which might help us create.  
**Translation:** Vocabulary: constrained: 限制条件; physicists: 物理学家

**[8790.68s] English:** Intelligence, like uh, helps us add a little spice to the systems because, um, you seem to be able to  
**Translation:** 

**[8798.46s] English:** In complex systems with emergence, to be able to get a lot from little, and so that seems like a  
**Translation:** 

**[8805.74s] English:** A shortcut to get big leaps in performance, but, um, but there's a missing theoretical concept.  
**Translation:** 

**[8813.38s] English:** Concept:  
**Translation:** Vocabulary: shortcut: 捷径

**[8813.54s] English:** That we are, we don't have, yeah. Uh, and it's something that has also fascinated me since.  
**Translation:** 

**[8818.74s] English:** My undergrad days, and it's how you measure complexity, right? So we don't actually have...  
**Translation:** Vocabulary: complexity: 复杂性; fascinated: 着迷; undergrad: 本科

**[8825.58s] English:** Good ways of measuring, or at least we don't have good ways of interpreting the measures that we  
**Translation:** 

**[8830.62s] English:** We have at our disposal, like how do you measure the complexity of something, right? So there's all  
**Translation:** Vocabulary: disposal: 处理; interpreting: 解释

**[8834.94s] English:** Those things, you know, like Karma GOR of Chaiting Solomon of complexity, you know, the  
**Translation:** 

**[8839.54s] English:** The length of the shortest program that would generate a bit string can be thought of as  
**Translation:** Vocabulary: chaiting: 奇廷; karma: 因果; solomon: 所罗门

**[8843.36s] English:** You know, the length of the shortest program that would generate a bit string can be thought of as  
**Translation:** 

**[8843.54s] English:** The complexity of that bit string, right? Um, I've been fascinated by that concept. The problem with...  
**Translation:** 

**[8848.58s] English:** That is, that complexity is defined up to a constant, which can be very large.  
**Translation:** 

**[8855.78s] English:** Right, uh, there are similar concepts that are derived from, you know, Bayesian.  
**Translation:** Vocabulary: bayesian: 贝叶斯的

**[8861.38s] English:** Probability theory, where you know the complexity of something is the negative log of its probability.  
**Translation:** 

**[8867.62s] English:** Probability is essentially right, and you have a complete equivalence between the two things.  
**Translation:** Vocabulary: equivalence: 等价关系

**[8872.10s] English:** And there, you would think that the probability of something is the negative log of its probability.  
**Translation:** 

**[8873.36s] English:** Of something is the negative log of its probability, which is something that's well-defined mathematically.  
**Translation:** Vocabulary: mathematically: 数学上

**[8876.08s] English:** Is something that's well-defined mathematically, which means complexity is well-defined.  
**Translation:** 

**[8878.00s] English:** Which means complexity is well-defined, but it's not true that you need to have a model of.  
**Translation:** 

**[8879.76s] English:** But it's not true; you need to have a model of  
**Translation:** 

**[8880.00s] English:** Of the distribution. You may need to have a prior if you're doing Bayesian inference.  
**Translation:** Vocabulary: inference: 推断

**[8884.96s] English:** And the prior plays the same role as the choice of the computer with which you measure your results.  
**Translation:** 

**[8888.72s] English:** Kolmogorov complexity. And so, every measure of complexity we have has some arbitrariness in it.  
**Translation:** Vocabulary: arbitrariness: 随意性; kolmogorov: 科莫洛夫

**[8896.16s] English:** You know, an additive constant which can be arbitrarily large. And so, you know,  
**Translation:** 

**[8902.08s] English:** How can we come up with a good theory of how things become more complex if we don't have a  
**Translation:** Vocabulary: additive: 加法的; arbitrarily: 任意地

**[8905.84s] English:** Good measure of complexity? Yeah, which we need for one way that people study this in the space.  
**Translation:** 

**[8911.84s] English:** Of biology, the people who study the origin of life or try to recreate life in the laboratory.  
**Translation:** Vocabulary: complexity: 复杂性; recreate: 重建

**[8917.76s] English:** And the more interesting one is the alien one: when we go to other planets,  
**Translation:** 

**[8921.92s] English:** How do we recognize this life? Because, you know, complexity—we associate complexity,...  
**Translation:** Vocabulary: alien: 外星的

**[8927.44s] English:** Maybe some level of mobility with life. You know, we have to be able to, like, have concrete.  
**Translation:** 

**[8934.64s] English:** Algorithms for  
**Translation:** Vocabulary: mobility: 流动性

**[8935.84s] English:** For example, measuring the level of complexity is key to knowing the difference between life and  
**Translation:** 

**[8942.24s] English:** Non-life, and the problem is that complexity is in the eye of the beholder. So, let me give  
**Translation:** Vocabulary: beholder: 观察者

**[8947.04s] English:** You: An example. If I give you an image of the MNIST digits, right, and I flip through MNIST,  
**Translation:** 

**[8955.04s] English:** Digits, there is some obvious structure to it because of local structure, you know.  
**Translation:** Vocabulary: digits: 手写体数字

**[8960.88s] English:** Neighboring pixels are correlated across the entire dataset.  
**Translation:** 

**[8965.84s] English:** Now, imagine that,  
**Translation:** Vocabulary: correlated: 相关的; dataset: 数据集; neighboring: 相邻的; pixels: 像素

**[8968.16s] English:** I apply a random permutation to all the pixels.  
**Translation:** 

**[8972.48s] English:** A fixed random permutation; now, I'll show you those images, and they will look,  
**Translation:** Vocabulary: permutation: 排列

**[8977.28s] English:** You know, it's really disorganized to you, and more complex.  
**Translation:** 

**[8981.04s] English:** In fact, they're not more complex in absolute terms. They're exactly the same as originally.  
**Translation:** Vocabulary: disorganized: 杂乱无章

**[8985.20s] English:** Right? And if you knew what the permutation was, you could undo the permutation.  
**Translation:** 

**[8990.08s] English:** Now, imagine I give you special glasses that undo the permutation. Suddenly,  
**Translation:** 

**[8995.84s] English:** Complicated can become simple, right? So, if you have two...  
**Translation:** 

**[9000.00s] English:** If you have, you know, humans on one end, and then another race of aliens that sees the universe with,...  
**Translation:** Vocabulary: aliens: 外星生物

**[9004.80s] English:** Permutation glasses: Yeah, with the permutation glasses, what we perceive as simple to them is...  
**Translation:** 

**[9010.32s] English:** Hardly complicated; it's probably heat, yeah? Heat, yeah? Okay, and what they perceive as simple to us.  
**Translation:** Vocabulary: perceive: 感知

**[9015.84s] English:** Is it a random fluctuation? It's due to heat, yeah. So, truly, it's in the eye of the beholder; it depends.  
**Translation:** 

**[9023.04s] English:** What kind of glasses are you wearing, right? It depends on what kind of algorithm you're running in your  
**Translation:** Vocabulary: algorithm: 计算方法; beholder: 观察者; fluctuation: 波动

**[9027.04s] English:** Perception system, so I don't think we'll have a theory of intelligence self-organization.  
**Translation:** 

**[9032.08s] English:** Evolution, things like this, until we have a good handle on a notion of complexity, which we know is  
**Translation:** Vocabulary: complexity: 复杂性; perception: 感知

**[9039.12s] English:** In the eye of the beholder, yeah. It's sad to think that we might not be able to detect or  
**Translation:** 

**[9045.04s] English:** Interact with alien species because we're wearing different glasses, um, because their notion of  
**Translation:** Vocabulary: alien: 外星的; detect: 发现

**[9050.88s] English:** Locality might be different from ours, yeah. This actually connects with some fascinating questions.  
**Translation:** 

**[9055.12s] English:** In physics, at the moment, like modern physics.  
**Translation:** 

**[9057.44s] English:** Uh, quantum physics—like, you know, questions about whether we can recover the information, you know?  
**Translation:** 

**[9062.40s] English:** That's lost in a black hole, and things like this — right? And that relies on notions,...  
**Translation:** Vocabulary: notions: 概念; quantum: 量子

**[9066.88s] English:** Of complexity, um, yeah. I find this fascinating. Can you describe your approach?  
**Translation:** 

**[9072.40s] English:** Personal quest to build an expressive electronic wind instrument (EWI). What is it? What does it take?  
**Translation:** Vocabulary: expressive: 富有表现力的

**[9082.08s] English:** To build it well, I'm a tinkerer; I like building things.  
**Translation:** 

**[9086.24s] English:** Uh, I like  
**Translation:** Vocabulary: tinkerer: 修修补补的人

**[9087.04s] English:** Things with combinations of electronics and you know, mechanical stuff, you know, I  
**Translation:** 

**[9092.62s] English:** Have a bunch of different hobbies, but you know, probably my first one was.  
**Translation:** Vocabulary: electronics: 电子设备

**[9097.12s] English:** Little was building model airplanes and stuff like that, and I still do that to.  
**Translation:** 

**[9100.48s] English:** Some extent, but also electronics: I taught myself electronics before I  
**Translation:** 

**[9104.10s] English:** Studied it, and the reason I taught myself electronics is because of music.  
**Translation:** 

**[9109.12s] English:** My cousin was an inspiring electronic musician, and he had an analog  
**Translation:** Vocabulary: analog: 模拟的

**[9113.92s] English:** Transcript: Synthesizer, and I was, you know, basically modifying it for him and...  
**Translation:** 

**[9118.06s] English:** Building sequencers and stuff like that, right?  
**Translation:** Vocabulary: modifying: 修改; sequencers: sequencer; synthesizer: 合成器; transcript: 录音文本

**[9120.00s] English:** Heim, I was in high school when I was doing this. That's the interesting part—like progressive rock.  
**Translation:** 

**[9124.64s] English:** Like, in the '80s, what's the greatest band of all time according to Yama Koon? Oh, there's too...  
**Translation:** 

**[9130.32s] English:** Many of them, but you know, it's a combination of my vision, orchestra, and weather report.  
**Translation:** 

**[9139.84s] English:** Yes, Genesis, uh, you know, yes, Genesis with Peter Gabriel, uh-huh, Um, Gentle Giant, you know, things.  
**Translation:** Vocabulary: gabriel: 盖布勒

**[9148.24s] English:** Like that, great. Okay, so this love of electronics and this love of music combined.  
**Translation:** 

**[9153.68s] English:** Together, right? So, I was actually trying to play some Baroque and Renaissance music, and I played in a  
**Translation:** Vocabulary: baroque: 巴洛克; renaissance: 文艺复兴

**[9161.44s] English:** Orchestra when I was in high school and the first years of college, and I played the recorder.  
**Translation:** 

**[9166.80s] English:** Chrome horn, a little bit of oboe, you know, things like that. So, I'm a wind instrument player, but I  
**Translation:** 

**[9172.56s] English:** Always wanted to play improvised music, even though I don't know anything about it, and the only way I  
**Translation:** 

**[9177.20s] English:** Figured, you know.  
**Translation:** Vocabulary: improvised: 即兴演奏

**[9178.24s] English:** Short of learning to play a saxophone, playing electronic wind instruments is similar in that they behave differently.  
**Translation:** 

**[9184.40s] English:** The fingering is similar to a saxophone, but you know you have a wide variety of sounds because you  
**Translation:** Vocabulary: fingering: 指法; saxophone: 萨克斯

**[9189.20s] English:** Control the synthesizer with it, so I had a bunch of those—you know—going back to the late 80s.  
**Translation:** 

**[9195.44s] English:** From either Yamaha or Akai; they're both kind of the main manufacturers of those, so they were.  
**Translation:** Vocabulary: yamaha: 雅马哈

**[9202.80s] English:** Classically, you know, going back several decades, but I've never been completely satisfied with them.  
**Translation:** 

**[9208.24s] English:** So, I'm not going to be going back to them, but I'm gonna let you know that it's a really good instrument.  
**Translation:** 

**[9211.04s] English:** And you know, those things are somewhat expressive; I mean, they measure the breath.  
**Translation:** 

**[9214.16s] English:** Pressure: They measure lip pressure, and you know, you have various parameters you can adjust.  
**Translation:** Vocabulary: expressive: 有表现力的

**[9220.16s] English:** Can vary it with fingers, but they're not really as expressive as an acoustic instrument, right?  
**Translation:** 

**[9226.16s] English:** You hear John Coltrane play two notes, and you know it's him; you can recognize his style instantly.  
**Translation:** Vocabulary: acoustic: 共鸣; instantly: 立刻

**[9230.96s] English:** Got a unique sound, huh? Or maybe Davis, right? You can hear it's Davis playing the trumpet.  
**Translation:** 

**[9238.24s] English:** The sound  
**Translation:** Vocabulary: trumpet: 小号

**[9240.40s] English:** Reflects their, you know, physiognomy — basically the shape of the vocal tract.  
**Translation:** 

**[9248.00s] English:** Kind of shapes the sound, so how do you do this with an electronic instrument? And I was...  
**Translation:** Vocabulary: physiognomy: 面部特征; vocal: 声音的

**[9253.68s] English:** Many years ago, I met a guy called David Wessel. He was a professor at Berkeley and created the  
**Translation:** 

**[9260.72s] English:** Center for music technology, you know, there and he was interested in that question.  
**Translation:** Vocabulary: berkeley: 加州大学伯克利分校

**[9264.64s] English:** And so I kept kind of thinking about this for many years, and finally, because of COVID, you know.  
**Translation:** 

**[9270.34s] English:** I was at home, in my workshop, which also serves as my kind of Zoom room, and...  
**Translation:** 

**[9276.44s] English:** Home office, and this is in New Jersey. In New Jersey, and um, I started being really serious.  
**Translation:** 

**[9282.84s] English:** About, you know, building my own UE instrument. What else is going on in that New Jersey workshop?  
**Translation:** 

**[9288.28s] English:** There's some crazy stuff you built, like just left on the workshop floor.  
**Translation:** 

**[9293.84s] English:** Left.  
**Translation:** 

**[9294.64s] English:** Behind a lot of crazy stuff is, you know, electronics with microcontrollers built in.  
**Translation:** 

**[9300.20s] English:** Of various kinds, and you know, weird flying contraptions—um, so you still love flying?  
**Translation:** Vocabulary: contraptions: 奇怪的飞行装置; electronics: 电子设备; microcontrollers: 微控制器

**[9308.52s] English:** It's a family disease. My dad got me into it when I was a kid, and he was building.  
**Translation:** 

**[9315.00s] English:** Model airplanes when he was a kid, and he was a mechanical engineer who taught himself.  
**Translation:** 

**[9320.20s] English:** Electronics, however, so he built his early radio control systems in the  
**Translation:** 

**[9324.64s] English:** 1960s, early 1970s  
**Translation:** 

**[9327.96s] English:** Um.  
**Translation:** 

**[9329.64s] English:** And so, that's what got me into, I mean, he got me into kind of you know, engineering.  
**Translation:** 

**[9333.84s] English:** And science and technology, you also have an interest in the appreciation of flight in other.  
**Translation:** 

**[9336.74s] English:** Forms like drones, quadcopters, or is it model airplanes?  
**Translation:** Vocabulary: drones: 无人驾驶飞行器; quadcopters: 四轴飞行器

**[9344.60s] English:** You know, I mean, before drones were really a consumer product,  
**Translation:** 

**[9349.36s] English:** Um, you know, I've got my own project going too, building a microcontroller with uh JavaScoops.  
**Translation:** 

**[9354.64s] English:** Parameters for stabilization, writing the firmware for it, you know.  
**Translation:** 

**[9357.72s] English:** And then, when it became a standard thing you could buy, it was boring.  
**Translation:** Vocabulary: firmware: 固件; stabilization: 稳定

**[9360.00s] English:** You know, I stopped doing it; it wasn't fun anymore. Um, yeah, you were doing it before; it was...  
**Translation:** 

**[9365.82s] English:** Cool, yeah. What kind of advice would you give to a young person today, whether they're in high school or college?  
**Translation:** 

**[9371.64s] English:** Dreams of doing something big, like Yann LeCun—let's talk about the space of intelligence.  
**Translation:** 

**[9378.30s] English:** Dreams of having a chance to solve some fundamental problems in the space of intelligence.  
**Translation:** 

**[9383.22s] English:** Both for their career and just in life, being somebody who was a part of creating something.  
**Translation:** 

**[9389.38s] English:** Special, so try to get interested in big questions, things like, you know, what is intelligence?  
**Translation:** 

**[9398.38s] English:** What is the universe made of? What's life all about? Things like that, um, like even crazy.  
**Translation:** 

**[9406.08s] English:** Big questions, like "what's time like?" — nobody knows what time is. And then learn,...  
**Translation:** 

**[9416.60s] English:** Basic things, like basic methods.  
**Translation:** 

**[9419.38s] English:** Either from math, from physics, or from engineering — things that have a long shelf life — um, like if:  
**Translation:** 

**[9425.88s] English:** You have a choice between, like, you know, learning mobile programming on iPhone or quantum.  
**Translation:** 

**[9433.06s] English:** Mechanics take quantum mechanics, um, because you're going to learn things that you have no idea exist.  
**Translation:** Vocabulary: quantum: 量子力学

**[9439.74s] English:** And you may not, you never know, you may never be a quantum physicist, but you will learn about.  
**Translation:** 

**[9446.04s] English:** Path integrals and path integrals are used everywhere; it's the same way you can learn about.  
**Translation:** Vocabulary: integrals: 积分; physicist: 物理学家

**[9449.38s] English:** The same formula that you use, you know, for Bayesian integration and stuff like that.  
**Translation:** 

**[9453.38s] English:** So, the ideas—the little ideas—within quantum mechanics, within some of these kinds of more  
**Translation:** Vocabulary: bayesian: 贝叶斯的

**[9459.68s] English:** Solidified fields will have a longer shelf life; they'll somehow be used indirectly.  
**Translation:** 

**[9465.70s] English:** In your work, learn classical mechanics, like you learn about Lagrangians, for example.  
**Translation:** Vocabulary: lagrangians: 拉格朗日方程; solidified: 固化

**[9471.46s] English:** Which is like a huge, hugely useful concept, you know, for all kinds of different things.  
**Translation:** 

**[9476.38s] English:** Uh  
**Translation:** Vocabulary: hugely: 非常地

**[9477.38s] English:** Learn, uh, about statistical physics; you know, you're going to learn about quantum mechanics, too.  
**Translation:** 

**[9478.38s] English:** Going to learn about quantum mechanics, you know? You're going to learn about quantum mechanics.  
**Translation:** 

**[9479.38s] English:** Because  
**Translation:** 

**[9480.00s] English:** All the math that comes out for machine learning.  
**Translation:** 

**[9484.18s] English:** Basically, it comes out of what was figured out by statistical physicists.  
**Translation:** 

**[9488.22s] English:** In the late 19th, early 20th century.  
**Translation:** Vocabulary: physicists: 物理学家

**[9490.62s] English:** And for some of them, actually, more recently,  
**Translation:** 

**[9494.40s] English:** By people like Giorgio Parisi, who just got the Nobel Prize.  
**Translation:** Vocabulary: nobel: 诺贝尔奖

**[9497.44s] English:** For the replica method, among other things.  
**Translation:** 

**[9500.16s] English:** It's used for a lot of different things.  
**Translation:** Vocabulary: replica: 复制品

**[9503.24s] English:** Variational inference: that math comes from statistical physics.  
**Translation:** 

**[9507.34s] English:** So, a lot of those kinds of basic courses,  
**Translation:** Vocabulary: inference: 推断; variational: 变分的

**[9514.00s] English:** You know, if you do electrical engineering,  
**Translation:** 

**[9516.26s] English:** You take signal processing, and you'll learn about Fourier transforms.  
**Translation:** Vocabulary: fourier: 傅里叶; transforms: 变换

**[9519.56s] English:** Again, something super useful.  
**Translation:** 

**[9521.68s] English:** It's at the basis of things like graph neural networks,  
**Translation:** Vocabulary: neural: 神经的

**[9524.70s] English:** Which is an entirely new sub-area of you know AI machine learning,  
**Translation:** 

**[9530.18s] English:** Deep learning, which I think is super promising.  
**Translation:** 

**[9532.00s] English:** For all kinds of applications.  
**Translation:** 

**[9534.12s] English:** Something very promising, if you're more interested in applications,  
**Translation:** 

**[9536.68s] English:** Is the application?  
**Translation:** 

**[9537.34s] English:** So, if you're interested in applications of AI machine learning,...  
**Translation:** 

**[9538.84s] English:** And deep learning to science, or to the sciences.  
**Translation:** 

**[9543.70s] English:** That can help solve big problems in the world.  
**Translation:** 

**[9545.56s] English:** I have colleagues at Meta, at FAIR.  
**Translation:** 

**[9549.28s] English:** Who started this project called Open Catalyst?  
**Translation:** Vocabulary: catalyst: 催化剂; colleagues: 同事

**[9551.32s] English:** And it's an open, collaborative project.  
**Translation:** 

**[9553.94s] English:** And the idea is to use deep learning.  
**Translation:** Vocabulary: collaborative: 合作的

**[9556.70s] English:** To help design new chemical compounds or materials.  
**Translation:** 

**[9561.98s] English:** That would facilitate the separation of hydrogen from oxygen.  
**Translation:** Vocabulary: facilitate: 促进分离

**[9565.04s] English:** If you can efficiently separate hydrogen from oxygen,  
**Translation:** 

**[9566.68s] English:** If you can efficiently separate oxygen from hydrogen with electricity,  
**Translation:** Vocabulary: efficiently: 高效率地

**[9570.98s] English:** You can solve climate change.  
**Translation:** 

**[9573.44s] English:** It's as simple as that.  
**Translation:** 

**[9574.46s] English:** Because you cover, you know, some random desert with solar panels,  
**Translation:** 

**[9580.76s] English:** And you have them work all day to produce hydrogen.  
**Translation:** Vocabulary: panels: 太阳能板

**[9583.40s] English:** And then you ship the hydrogen wherever it's needed.  
**Translation:** 

**[9585.34s] English:** You don't need anything else.  
**Translation:** 

**[9588.52s] English:** You know, you have controllable power that's, you know,  
**Translation:** 

**[9594.10s] English:** Can be transported anywhere.  
**Translation:** Vocabulary: transported: 运输

**[9595.64s] English:** So, if we can do something like this,  
**Translation:** 

**[9596.52s] English:** We can do it.  
**Translation:** 

**[9596.62s] English:** We can do it.  
**Translation:** 

**[9596.64s] English:** We can do it.  
**Translation:** 

**[9596.66s] English:** If we have a large-scale, efficient,...  
**Translation:** 

**[9600.00s] English:** Uh, energy storage technology like producing hydrogen—uh, we solve climate change here.  
**Translation:** 

**[9606.72s] English:** Another way to solve climate change is figuring out how to make fusion work. Now, the problem with  
**Translation:** 

**[9610.96s] English:** Fusion is that you make a super-hot plasma, and the plasma is unstable and you can't control it, maybe.  
**Translation:** Vocabulary: fusion: 核聚变; plasma: 等离子体; unstable: 不稳定的

**[9616.32s] English:** With deep learning, you can find controllers that will stabilize plasma and make it practically feasible.  
**Translation:** 

**[9620.08s] English:** Fusion reactors—I mean, that's very speculative, but you know, it's worth trying because, um, you know.  
**Translation:** Vocabulary: feasible: 可行的; practically: 实际上; speculative: 推测性的; stabilize: 稳定

**[9626.72s] English:** Uh, the payoff is huge. There's a group at Google working on this, led by John Platt, so control...  
**Translation:** 

**[9632.32s] English:** Convert as many problems in science, physics, biology, and chemistry into something learnable.  
**Translation:** Vocabulary: convert: 转化为; payoff: 回报

**[9639.28s] English:** Problem, and see if a machine can learn it right. I mean, there are properties of, you know, complex...  
**Translation:** 

**[9644.48s] English:** Materials that we don't understand from first principles, for example, so you know, if we  
**Translation:** 

**[9649.36s] English:** Could design new materials, uh, you know, we could make more efficient batteries, you know.  
**Translation:** 

**[9656.72s] English:** We could make faster electronics, or maybe even more efficient ones. We could imagine a lot of things.  
**Translation:** Vocabulary: electronics: 电子设备

**[9661.12s] English:** Uh, doing or you know, lighter materials for cars or airplanes or things like that, maybe better.  
**Translation:** 

**[9666.80s] English:** Fuel cells—I mean, there's all kinds of stuff we can imagine if we had good fuel cells with hydrogen.  
**Translation:** 

**[9670.80s] English:** Fuel cells, uh, we could use them to power airplanes, and you know, uh, transportation wouldn't be, or  
**Translation:** 

**[9676.32s] English:** Cars, and we wouldn't have an emissions problem — especially CO2 emissions — for air transportation.  
**Translation:** 

**[9683.92s] English:** Anymore, so there are a lot of those things, I think.  
**Translation:** 

**[9686.72s] English:** Where AI can be used, it and this is not even talking about all the sorts of medicine.  
**Translation:** 

**[9692.88s] English:** Biology, and everything like that—right? You know, like protein folding, you know, figuring out...  
**Translation:** 

**[9699.04s] English:** Like, how can you design your proteins to stick to another protein at a particular site?  
**Translation:** 

**[9702.72s] English:** Because that's how you design drugs in the end, um, so deep learning would be useful.  
**Translation:** 

**[9707.44s] English:** Although "this" and "those" are kind of you know, would be sort of enormous progress if we could.  
**Translation:** 

**[9712.08s] English:** Use it for that. Here's an example: if you take, um, this is like from.  
**Translation:** 

**[9716.72s] English:** Recent material physics involves studying monoatomic.  
**Translation:** Vocabulary: monoatomic: 单原子的

**[9720.00s] English:** Layer of graphene, right? So it's just carbon in a hexagonal mesh, and you make this single-layer sheet.  
**Translation:** 

**[9726.72s] English:** Single-atom thick, you put another one on top, and you twist them by some magic number of degrees.  
**Translation:** Vocabulary: graphene: 石墨烯; hexagonal: 六边形的

**[9732.96s] English:** Three degrees or so, it becomes a superconductor. Nobody has any idea why.  
**Translation:** 

**[9740.72s] English:** Uh, I want to know how that was discovered, but that's the kind of thing that machine learning can be used for.  
**Translation:** Vocabulary: superconductor: 超导体

**[9743.76s] English:** Can actually discover these well things, maybe not, but there is a hint, perhaps, that with...  
**Translation:** 

**[9749.68s] English:** Machine learning: we would train a system to basically be a phenomenological model of.  
**Translation:** Vocabulary: phenomenological: 现象学的

**[9755.28s] English:** Some complex emergent phenomena, which you know, superconductivity is one of those, uh,...  
**Translation:** 

**[9762.32s] English:** Where do you think this collective phenomenon is too difficult to describe from first principles?  
**Translation:** Vocabulary: emergent: 涌现; superconductivity: 超导性

**[9766.80s] English:** With the current, you know, the usual sort of reductionist-type method, but we could have...  
**Translation:** 

**[9774.00s] English:** Deep learning systems that predict the properties of a system from a description of it after being trained on relevant data.  
**Translation:** 

**[9779.44s] English:** Trained  
**Translation:** 

**[9779.68s] English:** With sufficiently many samples, this guy Pascal Fuad from his startup company...  
**Translation:** Vocabulary: pascal: 帕斯卡; sufficiently: 足够地

**[9788.00s] English:** Um, that's where he basically trained a convolutional net essentially to predict the aerodynamic.  
**Translation:** 

**[9795.92s] English:** Properties of solids, and you can generate as much data as you want by just running  
**Translation:** 

**[9800.48s] English:** Competition-free dynamics, right? So, you give it a shape like a wing airfoil or something of that kind.  
**Translation:** 

**[9809.68s] English:** And you run competition-free dynamics, you get as a result the drag, and you know, uh, lift, and all that.  
**Translation:** Vocabulary: airfoil: 机翼截面

**[9816.80s] English:** Stuff it right, and you can generate lots of data to train a neural net to make those predictions.  
**Translation:** 

**[9821.60s] English:** And now, what you have is a differentiable model of, let's say, drag and lift as a function of the  
**Translation:** Vocabulary: differentiable: 可微分的; neural: 神经的

**[9827.68s] English:** Shape of that solid, and so you can do background and design; you can optimize the shape so you get  
**Translation:** 

**[9831.76s] English:** The properties you want, um, yeah, that's incredible—that's incredible—and on top of all that, probably...  
**Translation:** 

**[9839.68s] English:** Should  
**Translation:** 

**[9840.00s] English:** Read a little bit of literature and a little bit of history for inspiration and for wisdom.  
**Translation:** 

**[9846.16s] English:** Because, after all, all of these technologies will have to work in the human world, yes.  
**Translation:** 

**[9850.46s] English:** And the human world is complicated; it is sadly, yes. And this is, um, an amazing conversation. I'm  
**Translation:** 

**[9858.48s] English:** Really, I'm honored that you would talk with me today. Thank you for all the amazing work you're doing!  
**Translation:** 

**[9862.14s] English:** At the fair at Meta, and thank you for being so passionate about everything after all these years.  
**Translation:** Vocabulary: passionate: 热情的

**[9867.96s] English:** That's going on; you're a beacon of hope for the machine learning community, and thank you.  
**Translation:** 

**[9872.28s] English:** So much for spending your valuable time with me today; that was awesome! Thanks for having me on.  
**Translation:** Vocabulary: beacon: 灯塔

**[9876.24s] English:** That was it; it was a pleasure. Thanks for listening to this conversation with Jan Lacoon to support.  
**Translation:** 

**[9881.80s] English:** This podcast: please, check out our sponsors in the description, and now let me leave you with some.  
**Translation:** Vocabulary: sponsors: 赞助商

**[9887.28s] English:** Words from Isaac Asimov: "Your assumptions are your windows on the world. Scrub them off every once in a while to get a clearer view.  
**Translation:** 

**[9895.20s] English:** A while, or the light won't come in.  
**Translation:** Vocabulary: assumptions: 假定; scrub: 清洗

**[9897.96s] English:** Thank you for listening, and hope to see you next time.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
