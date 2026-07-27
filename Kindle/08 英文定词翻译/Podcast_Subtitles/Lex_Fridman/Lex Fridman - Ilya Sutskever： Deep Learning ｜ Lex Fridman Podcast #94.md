# Podcast vocabulary notes
Source file: Lex Fridman - Ilya Sutskever： Deep Learning ｜ Lex Fridman Podcast #94.opus

**[0.00s] English:** The following is a conversation with Ilya Setskever, co-founder and chief scientist of OpenAI,  
**Translation:** 

**[5.88s] English:** one of the most cited computer scientists in history with over 165,000 citations,  
**Translation:** Vocabulary: citations: 引用次数; cited: 被引证

**[13.14s] English:** and to me, one of the most brilliant and insightful minds ever in the field of deep learning.  
**Translation:** 

**[19.58s] English:** There are very few people in this world who I would rather talk to and brainstorm with about deep learning,  
**Translation:** 

**[24.84s] English:** intelligence, and life in general than Ilya, on and off the mic.  
**Translation:** 

**[30.62s] English:** This was an honor and a pleasure.  
**Translation:** 

**[33.74s] English:** This conversation was recorded before the outbreak of the pandemic.  
**Translation:** 

**[37.14s] English:** For everyone feeling the medical, psychological, and financial burden of this crisis, I'm sending love your way.  
**Translation:** Vocabulary: outbreak: 爆发; pandemic: pandemic

**[43.16s] English:** Stay strong. We're in this together. We'll beat this thing.  
**Translation:** 

**[46.84s] English:** This is the Artificial Intelligence Podcast.  
**Translation:** 

**[49.54s] English:** If you enjoy it, subscribe on YouTube, review it with five stars on Apple Podcasts,  
**Translation:** 

**[53.92s] English:** support it on Patreon.  
**Translation:** Vocabulary: subscribe: 订阅

**[55.18s] English:** Or simply connect with me on Twitter at Lex Friedman, spelled F-R-I-D-M-A-N.  
**Translation:** 

**[60.38s] English:** As usual, I'll do a few minutes of ads now and never any ads in the middle that can break the flow of the conversation.  
**Translation:** Vocabulary: friedman: 弗里德曼

**[66.52s] English:** I hope that works for you and doesn't hurt the listening experience.  
**Translation:** 

**[70.68s] English:** This show is presented by Cash App, the number one finance app in the App Store.  
**Translation:** 

**[75.62s] English:** When you get it, use code LEXPODCAST.  
**Translation:** 

**[78.62s] English:** Cash App lets you send money to friends, buy Bitcoin, invest in the stock market with as little as $1.  
**Translation:** 

**[84.84s] English:** Since Cash App allows you to buy Bitcoin, let me mention that cryptocurrency in the context of the history of money is fascinating.  
**Translation:** 

**[92.98s] English:** I recommend Ascent of Money as a great book on this history.  
**Translation:** Vocabulary: ascent: 上升; cryptocurrency: 加密货币

**[96.80s] English:** Both the book and audiobook are great.  
**Translation:** 

**[99.52s] English:** Debits and credits on Ledgers started around 30,000 years ago.  
**Translation:** Vocabulary: audiobook: 有声书; ledgers: 账簿

**[103.86s] English:** The US dollar created over 200 years ago.  
**Translation:** 

**[107.24s] English:** And Bitcoin, the first decentralized cryptocurrency, released just over 10 years ago.  
**Translation:** Vocabulary: decentralized: 去中心化

**[111.56s] English:** So given that history, cryptocurrency is still very important.  
**Translation:** 

**[114.82s] English:** Not very much in its early days of development, but it's still aiming to, and just might, redefine.  
**Translation:** Vocabulary: redefine: 重新定义

**[120.00s] English:** the nature of money. So again, if you get Cash App from the App Store or Google Play and use the code  
**Translation:** 

**[125.92s] English:** LexPodcast, you get $10 and Cash App will also donate $10 to FIRST, an organization that is  
**Translation:** 

**[133.52s] English:** helping advance robotics and STEM education for young people around the world. And now,  
**Translation:** 

**[138.96s] English:** here's my conversation with Ilya Setskever. You were one of the three authors with Alex  
**Translation:** 

**[145.74s] English:** Krzyzewski, Jeff Hinton of the famed AlexNet paper that is arguably the paper that marked  
**Translation:** 

**[153.38s] English:** the big catalytic moment that launched the deep learning revolution. At that time, take us back  
**Translation:** Vocabulary: arguably: 或许; catalytic: 催化剂

**[159.02s] English:** to that time. What was your intuition about neural networks, about the representational  
**Translation:** 

**[163.78s] English:** power of neural networks? And maybe you can mention, how did that evolve over the next few  
**Translation:** Vocabulary: intuition: 直觉; neural: 神经; representational: 表示能力

**[169.96s] English:** years up to today, over the 10 years? Yeah, I can answer that question. At some  
**Translation:** 

**[175.66s] English:** point, I was in the middle of a crisis. I was in a crisis. I was in a crisis. I was in a crisis.  
**Translation:** 

**[175.72s] English:** At some point in about 2010 or 2011, I connected two facts in my mind. Basically,  
**Translation:** 

**[183.92s] English:** the realization was this. At some point, we realized that we can train very large,  
**Translation:** Vocabulary: realization: 觉悟

**[191.16s] English:** I shouldn't say very, you know, they were tiny by today's standards, but  
**Translation:** 

**[193.56s] English:** large and deep neural networks end-to-end with back propagation. At some point,  
**Translation:** Vocabulary: propagation: 反向传播

**[200.52s] English:** different people obtained this result. I obtained this result. The first moment in which  
**Translation:** 

**[205.64s] English:** I realized that deep neural networks are powerful was when James Martens invented the Hessian free  
**Translation:** Vocabulary: hessian: 海森矩阵; martens: 马特恩

**[211.40s] English:** optimizer in 2010. And he trained a 10-layer neural network end-to-end without pre-training  
**Translation:** 

**[218.08s] English:** from scratch. And when that happened, I thought, this is it. Because if you can train a big neural  
**Translation:** Vocabulary: optimizer: 优化器

**[225.16s] English:** network, a big neural network can represent very complicated function. Because if you have a  
**Translation:** 

**[234.84s] English:** brain to run for some number of milliseconds, neuron firings are slow.  
**Translation:** Vocabulary: milliseconds: 毫秒; neuron: 神经元

**[240.00s] English:** And so in maybe 100 milliseconds, your neurons only fire 10 times.  
**Translation:** 

**[244.68s] English:** So it's also kind of like 10 layers.  
**Translation:** Vocabulary: neurons: 神经元

**[246.64s] English:** And in 100 milliseconds, you can perfectly recognize any object.  
**Translation:** 

**[250.50s] English:** So I already had the idea then that we need to train a very big neural network on lots of supervised data.  
**Translation:** Vocabulary: supervised: 监督学习

**[258.08s] English:** And then it must succeed because we can find the best neural network.  
**Translation:** 

**[261.32s] English:** And then there's also theory that if you have more data than parameters, you won't overfit.  
**Translation:** 

**[265.20s] English:** Today, we know that actually this theory is very incomplete and you won't overfit even if you have less data than parameters.  
**Translation:** 

**[270.40s] English:** But definitely, if you have more data than parameters, you won't overfit.  
**Translation:** Vocabulary: incomplete: 不完整

**[273.38s] English:** So the fact that neural networks were heavily overparameterized wasn't discouraging to you?  
**Translation:** 

**[279.14s] English:** So you were thinking about the theory that the number of parameters, the fact there's a huge number of parameters is okay?  
**Translation:** Vocabulary: discouraging: 令人灰心; overparameterized: 参数过多

**[285.22s] English:** It's going to be okay?  
**Translation:** 

**[285.92s] English:** I mean, there was some evidence before that it was okay-ish.  
**Translation:** 

**[288.32s] English:** But the theory was that if you had a big data set and a big neural net, it was going to work.  
**Translation:** 

**[292.76s] English:** The overparameterization just didn't really work.  
**Translation:** Vocabulary: neural: 神经网络; overparameterization: 参数过拟合

**[295.20s] English:** It didn't figure much as a problem.  
**Translation:** 

**[297.10s] English:** I thought, well, with images, you're just going to add some data augmentation and it's going to be okay.  
**Translation:** Vocabulary: augmentation: 数据增强

**[300.40s] English:** So where was any doubt coming from?  
**Translation:** 

**[302.44s] English:** The main doubt was, can we have enough compute to train a big enough neural net?  
**Translation:** 

**[306.42s] English:** With backpropagation.  
**Translation:** 

**[307.84s] English:** Backpropagation, I thought, would work.  
**Translation:** Vocabulary: backpropagation: 反向传播

**[309.46s] English:** The thing which wasn't clear was whether there would be enough compute to get a very convincing result.  
**Translation:** 

**[314.10s] English:** And then at some point, Alex Kerzhetsky wrote these insanely fast CUDA kernels for training convolutional neural nets.  
**Translation:** Vocabulary: convolutional: 卷积; kernels: 内核

**[319.10s] English:** And that was, bam, let's do this.  
**Translation:** 

**[320.92s] English:** Let's get ImageNet and it's going to be the greatest thing.  
**Translation:** 

**[323.60s] English:** Was your intuition?  
**Translation:** 

**[324.44s] English:** Most of your intuition from empirical results by you and by others?  
**Translation:** Vocabulary: empirical: 经验的; intuition: 直觉

**[329.48s] English:** So, like, just actually demonstrating that a piece of program can train a 10-layer neural network?  
**Translation:** 

**[334.42s] English:** Or was there some pen and paper or marker and whiteboard thinking intuition?  
**Translation:** Vocabulary: whiteboard: 白板

**[341.28s] English:** Because you just connected a 10-layer large neural network to the brain.  
**Translation:** 

**[345.48s] English:** So you just mentioned the brain.  
**Translation:** 

**[346.52s] English:** So in your intuition about neural networks, does the human brain come into play as an intuition builder?  
**Translation:** 

**[353.84s] English:** Definitely.  
**Translation:** 

**[354.44s] English:** I mean, you know, you've got to be precise with these analogies between artificial neural networks in the brain.  
**Translation:** 

**[360.00s] English:** But there is no question that the brain is a huge source of intuition and inspiration for deep learning researchers since all the way from Rosenblatt in the 60s.  
**Translation:** Vocabulary: analogies: 类比

**[370.86s] English:** Like, if you look at the whole idea of a neural network is directly inspired by the brain.  
**Translation:** 

**[375.36s] English:** You had people like McCallum and Pitts who were saying, hey, you got these neurons in the brain.  
**Translation:** Vocabulary: neurons: 神经元

**[382.10s] English:** And hey, we recently learned about the computer and automata.  
**Translation:** 

**[384.32s] English:** Can we use some ideas from the computer and automata to design some kind of computational object that's going to be simple, computational, and kind of like the brain?  
**Translation:** Vocabulary: automata: 自动机; computational: 计算的

**[392.72s] English:** And they invented the neuron.  
**Translation:** 

**[394.18s] English:** So they were inspired by it back then.  
**Translation:** Vocabulary: neuron: 神经元

**[395.70s] English:** Then you had the convolutional neural network from Fukushima.  
**Translation:** 

**[398.66s] English:** And then later, Jan Lekan, who said, hey, if you limit the receptive fields of a neural network, it's going to be especially suitable for images, as it turned out to be true.  
**Translation:** Vocabulary: fukushima: 福岛; receptive: 接受范围

**[406.92s] English:** So there was a very small number of examples where analogies to the brain were successful.  
**Translation:** 

**[412.42s] English:** And I thought, well, probably energy.  
**Translation:** 

**[414.32s] English:** Artificial neuron is not that different from the brain if you squint hard enough.  
**Translation:** 

**[417.64s] English:** So let's just assume it is and roll with it.  
**Translation:** Vocabulary: squint: 眯眼看

**[420.76s] English:** So we're now at a time where deep learning is very successful.  
**Translation:** 

**[423.56s] English:** So let us squint less and say, let's open our eyes and say, what to you is an interesting difference between the human brain?  
**Translation:** 

**[433.72s] English:** Now, I know you're probably not an expert, neither a neuroscientist and you're a biologist.  
**Translation:** 

**[438.24s] English:** But loosely speaking, what's the difference between the human brain and artificial neural networks?  
**Translation:** Vocabulary: biologist: 生物学家; neural: 神经; neuroscientist: 神经科学家

**[442.36s] English:** That's interesting to you.  
**Translation:** 

**[443.64s] English:** For the next decade or two.  
**Translation:** 

**[445.94s] English:** That's a good question to ask.  
**Translation:** 

**[447.42s] English:** What is an interesting difference between the brain and our artificial neural networks?  
**Translation:** 

**[452.84s] English:** So I feel like today, artificial neural networks, so we all agree that there are certain dimensions in which the human brain vastly outperforms our models.  
**Translation:** 

**[462.92s] English:** But I also think that there are some ways in which our artificial neural networks have a number of very important advantages over the brain.  
**Translation:** Vocabulary: dimensions: 方面

**[470.02s] English:** Looking at the advantages versus disadvantages is a good way to figure.  
**Translation:** 

**[473.64s] English:** Out what is the important difference.  
**Translation:** 

**[475.62s] English:** So the brain uses spikes, which may or may not be important.  
**Translation:** 

**[480.00s] English:** Yes, that's a really interesting question.  
**Translation:** 

**[481.40s] English:** Do you think it's important or not?  
**Translation:** 

**[483.58s] English:** That's one big architectural difference between artificial neural networks.  
**Translation:** Vocabulary: architectural: 建筑结构的

**[488.08s] English:** It's hard to tell, but my prior is not very high, and I can say why.  
**Translation:** 

**[493.24s] English:** You know, there are people who are interested in spiking neural networks,  
**Translation:** Vocabulary: spiking: 尖峰编码

**[495.38s] English:** and basically what they figured out is that they need to simulate  
**Translation:** 

**[499.14s] English:** the non-spiking neural networks in spikes.  
**Translation:** Vocabulary: simulate: 模拟; spikes: 尖峰

**[502.42s] English:** And that's how they're going to make them work.  
**Translation:** 

**[504.30s] English:** If you don't simulate the non-spiking neural networks in spikes,  
**Translation:** 

**[506.90s] English:** it's not going to work, because the question is, why should it work?  
**Translation:** 

**[509.28s] English:** And that connects to questions around backpropagation  
**Translation:** Vocabulary: backpropagation: 反向传播

**[511.44s] English:** and questions around deep learning.  
**Translation:** 

**[514.70s] English:** You've got this giant neural network.  
**Translation:** 

**[516.84s] English:** Why should it work at all?  
**Translation:** 

**[518.44s] English:** Why should the learning rule work at all?  
**Translation:** 

**[523.02s] English:** It's not a self-evident question, especially if you,  
**Translation:** 

**[525.62s] English:** let's say if you were just starting in the field and you read the very early papers,  
**Translation:** 

**[529.26s] English:** you can say, hey, people are saying, let's build neural networks.  
**Translation:** 

**[533.48s] English:** That's a great idea, because the brain is a neural network,  
**Translation:** 

**[535.90s] English:** so it would be useful to build neural networks.  
**Translation:** 

**[537.74s] English:** Now, let's figure out.  
**Translation:** 

**[539.28s] English:** How to train them?  
**Translation:** 

**[540.38s] English:** It should be possible to train them, probably, but how?  
**Translation:** 

**[543.48s] English:** And so the big idea is the cost function.  
**Translation:** 

**[547.10s] English:** That's the big idea.  
**Translation:** 

**[548.70s] English:** The cost function is a way of measuring the performance of the system  
**Translation:** 

**[552.36s] English:** according to some measure.  
**Translation:** 

**[555.04s] English:** By the way, that is a big, actually, let me think.  
**Translation:** 

**[557.22s] English:** Is that one, a difficult idea to arrive at?  
**Translation:** 

**[561.20s] English:** And how big of an idea is that?  
**Translation:** 

**[562.74s] English:** That there's a single cost function.  
**Translation:** 

**[567.40s] English:** Sorry, let me take a pause.  
**Translation:** 

**[569.28s] English:** Supervised learning, a difficult concept to come to.  
**Translation:** Vocabulary: supervised: 监督学习

**[573.28s] English:** I don't know.  
**Translation:** 

**[574.42s] English:** All concepts are very easy in retrospect.  
**Translation:** Vocabulary: retrospect: 回顾

**[576.46s] English:** Yeah, that's what, it seems trivial now, but I,  
**Translation:** 

**[578.90s] English:** because the reason I asked that, and we'll talk about it,  
**Translation:** 

**[581.44s] English:** because is there other things?  
**Translation:** 

**[583.42s] English:** Is there things that don't necessarily have a cost function,  
**Translation:** 

**[587.16s] English:** maybe have many cost functions, or maybe have dynamic cost functions,  
**Translation:** 

**[590.76s] English:** or maybe a totally different kind of architectures?  
**Translation:** 

**[593.96s] English:** Because we have to think like that in order to arrive at something new, right?  
**Translation:** 

**[597.94s] English:** So the only, so the good example,  
**Translation:** 

**[599.28s] English:** the examples of things.  
**Translation:** 

**[600.00s] English:** don't have clear cost functions are GANs. In a GAN, you have a game. So instead of thinking of  
**Translation:** 

**[606.48s] English:** a cost function where you know that you have an algorithm gradient descent, which will optimize  
**Translation:** 

**[612.72s] English:** the cost function, and then you can reason about the behavior of your system in terms of what it  
**Translation:** Vocabulary: algorithm: 算法; gradient: 梯度; optimize: 优化

**[617.04s] English:** optimizes. With a GAN, you say, I have a game and I'll reason about the behavior of the system in  
**Translation:** 

**[622.16s] English:** terms of the equilibrium of the game. But it's all about coming up with these mathematical objects  
**Translation:** Vocabulary: equilibrium: 平衡; mathematical: 数学的; optimizes: 优化

**[626.40s] English:** that help us reason about the behavior of our system. Right, that's really interesting. Yeah,  
**Translation:** 

**[631.28s] English:** so GAN is the only one. The cost function is emergent from the comparison.  
**Translation:** Vocabulary: emergent: 自然产生

**[637.52s] English:** I don't know if it has a cost function. I don't know if it's meaningful to talk about the cost  
**Translation:** 

**[640.32s] English:** function of a GAN. It's kind of like the cost function of biological evolution or the cost  
**Translation:** 

**[644.24s] English:** function of the economy. You can talk about regions to which it will go towards, but I don't  
**Translation:** 

**[655.36s] English:** think the cost function analysis  
**Translation:** 

**[656.40s] English:** is the most useful. That's really interesting. So if evolution doesn't really have a cost function,  
**Translation:** 

**[662.56s] English:** like a cost function based on something akin to our mathematical conception of a cost function,  
**Translation:** Vocabulary: conception: 概念

**[671.12s] English:** then do you think cost functions in deep learning are holding us back?  
**Translation:** 

**[675.04s] English:** Yeah, so you just kind of mentioned that cost function is a nice first profound idea.  
**Translation:** Vocabulary: profound: 深奥的

**[681.28s] English:** Do you think that's a good idea? Do you think it's an idea we'll go past?  
**Translation:** 

**[686.56s] English:** So self-play starts to touch on that a little bit in reinforcement learning systems.  
**Translation:** Vocabulary: reinforcement: 强化

**[691.60s] English:** That's right. Self-play and also ideas around exploration where you're trying to  
**Translation:** 

**[695.84s] English:** take action that superlines a predictor. I am a big fan of cost functions. I think cost functions  
**Translation:** Vocabulary: predictor: 预测器

**[701.12s] English:** are great and they serve us really well and I think that whenever we can do things  
**Translation:** 

**[704.56s] English:** with cost functions we should. And you know, maybe there is a chance that we will come up with some  
**Translation:** 

**[710.16s] English:** yet another profound way of looking at things that will involve cost functions in a less central way.  
**Translation:** 

**[715.36s] English:** but i don't know i think cost functions are i mean  
**Translation:** 

**[720.00s] English:** I would not bet against cost functions.  
**Translation:** 

**[722.76s] English:** Is there other things about the brain that pop into your mind that might be different and interesting for us to consider in designing artificial neural networks?  
**Translation:** Vocabulary: neural: 神经的

**[733.42s] English:** So we talked about spiking a little bit.  
**Translation:** 

**[736.22s] English:** I mean, one thing which may potentially be useful, I think people, neuroscientists, have figured out something about the learning rule of the brain.  
**Translation:** Vocabulary: neuroscientists: 神经科学家; spiking: 突触激发

**[742.26s] English:** Or I'm talking about spike time independent plasticity, and it would be nice if some people were to study that in simulation.  
**Translation:** 

**[747.64s] English:** Wait, sorry, spike time independent plasticity?  
**Translation:** Vocabulary: simulation: 模拟; spike: 尖峰

**[750.90s] English:** Yeah, that's right.  
**Translation:** 

**[751.32s] English:** What's that?  
**Translation:** 

**[751.76s] English:** STD.  
**Translation:** 

**[752.34s] English:** It's a particular learning rule that uses spike timing to figure out how to determine how to update the synapses.  
**Translation:** Vocabulary: synapses: 突触

**[759.56s] English:** So it's kind of like if a synapse fires into the neuron before the neuron fires, then it strengthens the synapse.  
**Translation:** 

**[766.00s] English:** And if the synapse fires into the neuron shortly after the neuron fired, then it weakens the synapse.  
**Translation:** Vocabulary: neuron: 神经元; strengthens: 增强; synapse: 突触

**[770.70s] English:** Something along this line.  
**Translation:** 

**[772.10s] English:** I'm 90% sure it's right.  
**Translation:** 

**[773.64s] English:** So if I said something wrong here, don't.  
**Translation:** 

**[777.04s] English:** Don't.  
**Translation:** 

**[777.64s] English:** Don't get too angry.  
**Translation:** 

**[779.04s] English:** But you sounded brilliant while saying it.  
**Translation:** 

**[781.06s] English:** But the timing, that's one thing that's missing.  
**Translation:** 

**[784.28s] English:** The temporal dynamics is not captured.  
**Translation:** Vocabulary: temporal: 时间相关的

**[787.40s] English:** I think that's like a fundamental property of the brain is the timing of the signals.  
**Translation:** 

**[793.30s] English:** Well, you have recurrent neural networks.  
**Translation:** Vocabulary: recurrent: 循环神经网络

**[795.46s] English:** But you think of that as, I mean, that's a very crude, simplified, what's that called?  
**Translation:** 

**[803.52s] English:** There's a clock, I guess, to recurrent neural networks.  
**Translation:** 

**[807.64s] English:** It seems like the brain is the continuous version of that, the generalization, where all possible timings are possible.  
**Translation:** 

**[815.88s] English:** And then within those timings is contained some information.  
**Translation:** Vocabulary: generalization: 概括外推

**[819.94s] English:** You think recurrent neural networks, the recurrence in recurrent neural networks can capture the same kind of phenomena as the timing that seems to be important for the brain, in the firing of neurons in the brain.  
**Translation:** 

**[835.64s] English:** I mean, I think.  
**Translation:** Vocabulary: neurons: 神经元; recurrence: 重复性

**[837.46s] English:** I think recurrent neural networks are amazing.  
**Translation:** 

**[840.00s] English:** amazing and they can do i think they can do anything we'd want them to we'd want a system  
**Translation:** 

**[846.52s] English:** to do right now recurrent neural networks have been superseded by transformers but maybe  
**Translation:** 

**[850.86s] English:** one day they'll make a comeback maybe they'll be back we'll see let me uh in a small tangent say  
**Translation:** Vocabulary: comeback: 东山再起; neural: 神经; superseded: 取代; tangent: 旁白

**[857.58s] English:** do you think they'll be back so so much of uh the breakthroughs recently that we'll talk about on  
**Translation:** 

**[862.32s] English:** natural language processing and language modeling has been with transformers that don't emphasize  
**Translation:** Vocabulary: breakthroughs: 重大进展

**[868.98s] English:** recurrence do you think recurrence will make a comeback well some kind of recurrence i think  
**Translation:** 

**[875.40s] English:** very likely recurrent neural networks for pros as they're typically thought of for processing  
**Translation:** 

**[881.96s] English:** sequences i think it's also possible what is to you a recurrent neural network in generally  
**Translation:** 

**[888.36s] English:** speaking i guess what is a recurrent neural network you have a neural network which maintains  
**Translation:** 

**[892.22s] English:** a high dimensional hidden state and then when an observation arrives it updates its high dimensional  
**Translation:** 

**[898.62s] English:** hidden state  
**Translation:** 

**[898.98s] English:** through its connections in some way so do you think you know that's what like expert systems  
**Translation:** 

**[906.98s] English:** did right symbolic ai uh the knowledge based growing a knowledge base is is maintaining a  
**Translation:** Vocabulary: symbolic: 符号化的

**[915.82s] English:** hidden state which is its knowledge base and is growing it by sequential processing do you think  
**Translation:** 

**[920.60s] English:** of it more generally in that way or is it simply is it the more constrained form that of  
**Translation:** Vocabulary: constrained: 限制较多; sequential: 顺序的

**[928.98s] English:** a hidden state with certain kind of gating units that we think of as today with lsdms and that  
**Translation:** 

**[934.26s] English:** i mean the hidden state is technically what you described the the hidden state that goes inside  
**Translation:** 

**[938.34s] English:** the lstm or the rnn or something like this but then what should be contained you know if you  
**Translation:** 

**[943.30s] English:** want to make the expert system and analogy i'm not i mean you could say that the knowledge is stored  
**Translation:** 

**[950.02s] English:** in the connections and then the short-term processing is done in the in the hidden state  
**Translation:** 

**[956.18s] English:** yes could you say that yeah so  
**Translation:** 

**[958.98s] English:** sort of do you think  
**Translation:** 

**[960.00s] English:** there's a future of building large scale knowledge bases within the neural networks definitely  
**Translation:** 

**[968.88s] English:** so we're going to pause on that confidence because i want to explore that well let me zoom back out  
**Translation:** 

**[974.08s] English:** and ask back to the history of image net neural networks have been around for many decades as  
**Translation:** Vocabulary: neural: 神经网络

**[981.36s] English:** you mentioned what do you think were the key ideas that led to their success that image net moment  
**Translation:** 

**[987.28s] English:** and beyond the the success in the past 10 years okay so the question is to make sure i didn't miss  
**Translation:** 

**[994.48s] English:** anything the key ideas that led to the success of deep learning over the past 10 years exactly even  
**Translation:** 

**[1000.16s] English:** though the fundamental thing behind deep learning has been around for much longer so the key idea  
**Translation:** 

**[1009.28s] English:** about deep learning or rather this the key fact about deep learning before deep learning started  
**Translation:** 

**[1016.64s] English:** to be successful  
**Translation:** 

**[1018.08s] English:** is that it was underestimated people who worked in machine learning simply didn't think that  
**Translation:** 

**[1024.16s] English:** neural networks could do much people didn't believe that large neural networks could be  
**Translation:** Vocabulary: underestimated: 低估的

**[1028.96s] English:** trained people thought that well there was lots of there was a lot of debate going on in machine  
**Translation:** 

**[1035.20s] English:** learning about what are the right methods and so on and people were arguing because  
**Translation:** 

**[1039.44s] English:** there were no there were there were no there was no way to get hard facts and by that i mean  
**Translation:** 

**[1044.24s] English:** there were no benchmarks which were truly hard that if you  
**Translation:** Vocabulary: benchmarks: 参考标准

**[1047.28s] English:** do really well on them then you can say look  
**Translation:** 

**[1050.32s] English:** here is my system that's when you switch from that's when this field becomes a little bit more  
**Translation:** 

**[1057.36s] English:** of an engineering field so in terms of deep learning to answer the question directly the  
**Translation:** 

**[1062.24s] English:** ideas were all there the thing that was missing was a lot of supervised data and a lot of compute  
**Translation:** Vocabulary: supervised: 监督学习

**[1069.60s] English:** once you have a lot of supervised data and a lot of compute then there is a third thing which is  
**Translation:** 

**[1073.60s] English:** needed as well and that is conviction conviction that if you don't have the message that you don't  
**Translation:** 

**[1077.08s] English:** But if you take the right stuff, which already exists,  
**Translation:** 

**[1080.00s] English:** and apply and mix a lot of data and a lot of compute that it will, in fact, work.  
**Translation:** 

**[1085.96s] English:** And so that was the missing piece.  
**Translation:** 

**[1087.80s] English:** It was you needed the data, you needed the compute, which showed up in terms of GPUs,  
**Translation:** 

**[1093.92s] English:** and you needed the conviction to realize that you need to mix them together.  
**Translation:** 

**[1098.06s] English:** So that's really interesting.  
**Translation:** 

**[1099.18s] English:** So I guess the presence of compute and the presence of supervised data  
**Translation:** 

**[1104.92s] English:** allowed the empirical evidence to do the convincing of the majority of the computer science community.  
**Translation:** Vocabulary: empirical: 实证的

**[1111.96s] English:** So I guess there's a key moment with Jitendra Malik and Alyosha Efros, who were very skeptical, right?  
**Translation:** 

**[1122.34s] English:** And then there's a Jeffrey Hinton that was the opposite of skeptical.  
**Translation:** Vocabulary: alyosha: 艾利奥什; hinton: 希顿; jeffrey: 杰弗里; jitendra: 吉特endar; malik: 马利克; skeptical: 怀疑的

**[1126.62s] English:** And there was a convincing moment.  
**Translation:** 

**[1128.06s] English:** And I think ImageNet served as that moment.  
**Translation:** 

**[1130.38s] English:** That's right.  
**Translation:** 

**[1130.84s] English:** And it represented this kind of where the big pillars of computers,  
**Translation:** 

**[1134.92s] English:** the computer vision community, kind of the wizards got together.  
**Translation:** 

**[1139.78s] English:** And then all of a sudden there was a shift.  
**Translation:** 

**[1141.72s] English:** And it's not enough for the ideas to all be there and the compute to be there.  
**Translation:** 

**[1146.40s] English:** It's for it to convince the cynicism that existed.  
**Translation:** Vocabulary: cynicism: 怀疑论

**[1151.12s] English:** It's interesting that people just didn't believe for a couple of decades.  
**Translation:** 

**[1155.98s] English:** Yeah, well, but it's more than that.  
**Translation:** 

**[1158.60s] English:** It's kind of, when put this way, it sounds like, well, you know,  
**Translation:** 

**[1161.72s] English:** those silly people who didn't believe.  
**Translation:** 

**[1164.36s] English:** What were they?  
**Translation:** 

**[1164.92s] English:** What were they missing?  
**Translation:** 

**[1165.52s] English:** But in reality, things were confusing because neural networks really did not work on anything.  
**Translation:** 

**[1170.20s] English:** And they were not the best method on pretty much anything as well.  
**Translation:** Vocabulary: neural: 神经网络

**[1173.54s] English:** And it was pretty rational to say, yeah, this stuff doesn't have any traction.  
**Translation:** 

**[1179.56s] English:** And that's why you need to have these very hard tasks, which are,  
**Translation:** 

**[1182.74s] English:** which produce undeniable evidence.  
**Translation:** 

**[1184.90s] English:** And that's how we make progress.  
**Translation:** Vocabulary: undeniable: 无可争议的

**[1186.94s] English:** And that's why the field is making progress today, because we have these hard benchmarks,  
**Translation:** 

**[1190.66s] English:** which represent true progress.  
**Translation:** Vocabulary: benchmarks: 标准

**[1192.78s] English:** And so, and this is why we were able to.  
**Translation:** 

**[1194.36s] English:** We are able to avoid endless debate.  
**Translation:** 

**[1198.32s] English:** So incredibly, you've.  
**Translation:** 

**[1200.00s] English:** some of the biggest recent ideas in ai in computer vision language natural language  
**Translation:** 

**[1206.20s] English:** processing reinforcement learning sort of everything in between maybe not gans  
**Translation:** 

**[1212.18s] English:** is there there may not be a topic you haven't touched and of course the the fundamental science  
**Translation:** Vocabulary: reinforcement: 强化

**[1217.90s] English:** of deep learning what is the difference to you between vision language and as in reinforcement  
**Translation:** 

**[1225.54s] English:** learning action as learning problems and what are the commonalities do you see them as all  
**Translation:** 

**[1230.38s] English:** interconnected are they fundamentally different domains that require different approaches  
**Translation:** 

**[1236.40s] English:** okay that's a good question machine learning is a field with a lot of unity a huge amount of unity  
**Translation:** Vocabulary: interconnected: 相互连接

**[1242.98s] English:** what do you mean by unity like overlap of ideas overlap of ideas overlap of principles in fact  
**Translation:** 

**[1250.44s] English:** there is only one or two or three principles which are very very simple and then they apply  
**Translation:** 

**[1255.52s] English:** in almost the same way in almost the same way to the different modalities to the different problems  
**Translation:** 

**[1260.90s] English:** and that's why today when someone writes a paper on improving optimization of deep learning and  
**Translation:** Vocabulary: modalities: 不同形式; optimization: 优化

**[1266.40s] English:** vision it improves the different nlp applications and it improves the different reinforcement  
**Translation:** 

**[1270.42s] English:** learning applications reinforcement learn so i would say that computer vision and nlp are very  
**Translation:** 

**[1276.98s] English:** similar to each other today they differ in that they have slightly different architectures we  
**Translation:** 

**[1282.26s] English:** use transformers in nlp and we use convolutional neural networks  
**Translation:** Vocabulary: convolutional: 卷积的

**[1285.28s] English:** you  
**Translation:** 

**[1285.52s] English:** envision. But it's also possible that one day this will change and everything will be unified  
**Translation:** Vocabulary: envision: 构想

**[1290.38s] English:** with a single architecture. Because if you go back a few years ago in natural language processing,  
**Translation:** 

**[1296.64s] English:** there were a huge number of architectures for every different tiny problem had its own architecture.  
**Translation:** 

**[1303.22s] English:** Today, there's just one transformer for all those different tasks. And if you go back in time even  
**Translation:** 

**[1308.94s] English:** more, you had even more and more fragmentation and every little problem in AI had its own little  
**Translation:** Vocabulary: fragmentation: 碎片化

**[1314.70s] English:** subspecialization and little set of collection of skills, people who would know how to engineer  
**Translation:** 

**[1320.00s] English:** other features now it's all been subsumed by deep learning we have this unification and so i expect  
**Translation:** Vocabulary: subspecialization: 专科细分; unification: 统一

**[1325.68s] English:** vision to become unified with natural language as well or rather i shouldn't say expect i think  
**Translation:** 

**[1329.76s] English:** it's possible i don't want to be too sure because i think on the conventional neural  
**Translation:** Vocabulary: neural: 神经网络

**[1333.60s] English:** it is very computationally efficient rl is different rl does require slightly different  
**Translation:** 

**[1338.32s] English:** techniques because you really do need to take action you really do need to do something about  
**Translation:** Vocabulary: computationally: 计算上

**[1342.96s] English:** exploration your variance is much higher but i think there is a lot of unity even there  
**Translation:** 

**[1347.52s] English:** and i would expect for example that at some point there will be some  
**Translation:** Vocabulary: variance: 差异

**[1352.40s] English:** broader unification between rl and supervised learning where somehow the rl will be making  
**Translation:** 

**[1356.56s] English:** decisions to make the supervised learning go better and it will be i imagine one big  
**Translation:** Vocabulary: supervised: 监督学习

**[1360.96s] English:** black box and you just throw every you know you shovel shovel things into it and it just  
**Translation:** 

**[1365.44s] English:** figures out what to do with whatever you shovel at it i mean reinforcement learning has  
**Translation:** Vocabulary: reinforcement: 强化学习; shovel: 铲子

**[1369.76s] English:** some aspects of language and vision combined almost there's elements of a long-term  
**Translation:** 

**[1377.20s] English:** memory  
**Translation:** 

**[1377.52s] English:** that you should be utilizing and there's elements of a really rich sensory space  
**Translation:** 

**[1382.88s] English:** so it seems like the it's like the union of the two or something like that i'd say something  
**Translation:** 

**[1389.04s] English:** slightly differently i'd say that reinforcement learning is neither but it naturally interfaces  
**Translation:** 

**[1394.72s] English:** and integrates with the two of them you think action is fundamentally different so yeah what  
**Translation:** Vocabulary: fundamentally: 从根本上; integrates: 整合; interfaces: 接口

**[1399.84s] English:** is interesting about what is unique about policy of learning to act well so one example for instance  
**Translation:** 

**[1407.20s] English:** is that when you learn to act you are fundamentally in a non-stationary world because as your actions  
**Translation:** 

**[1414.32s] English:** change the things you see start changing you you experience the world in a different way and this  
**Translation:** 

**[1421.28s] English:** is not the case for the more traditional static problem where you have a some distribution and  
**Translation:** 

**[1426.08s] English:** you just apply a model to that distribution you think it's a fundamentally different problem or  
**Translation:** 

**[1430.96s] English:** is it just a more difficult general it's a generalization of the problem of understanding i mean  
**Translation:** Vocabulary: generalization: 泛化

**[1437.20s] English:** it's it's it's a question of definitions almost there is  
**Translation:** 

**[1440.00s] English:** huge amount of commonality for sure. You take gradients, you try to approximate gradients in  
**Translation:** Vocabulary: approximate: 近似; gradients: 梯度

**[1445.28s] English:** both cases. In the case of reinforcement learning, you have some tools to reduce the variance of the  
**Translation:** 

**[1450.16s] English:** gradients. You do that. There's lots of commonality. You use the same neural net  
**Translation:** Vocabulary: neural: 神经网络

**[1454.88s] English:** in both cases. You compute the gradient, you apply Adam in both cases.  
**Translation:** 

**[1460.64s] English:** So, I mean, there's lots in common for sure, but there are some small differences which are not  
**Translation:** Vocabulary: gradient: 梯度

**[1467.44s] English:** completely insignificant. It's really just a matter of your point of view, what frame of  
**Translation:** 

**[1471.68s] English:** reference, how much do you want to zoom in or out as you look at these problems.  
**Translation:** 

**[1477.04s] English:** Which problem do you think is harder? So people like Noam Chomsky believe that language is  
**Translation:** 

**[1482.16s] English:** fundamental to everything. So it underlies everything. Do you think language understanding  
**Translation:** Vocabulary: chomsky: 乔姆斯基

**[1487.92s] English:** is harder than visual scene understanding or vice versa?  
**Translation:** 

**[1492.32s] English:** I think that asking if a problem is hard is slightly wrong.  
**Translation:** 

**[1495.92s] English:** I think the question is a little bit wrong.  
**Translation:** 

**[1497.44s] English:** I want to explain why. So what does it mean for a problem to be hard?  
**Translation:** 

**[1504.16s] English:** Okay. The non-interesting, dumb answer to that is there's a benchmark and there's a human level  
**Translation:** 

**[1511.52s] English:** performance on that benchmark. And how is the effort required to reach the human level benchmark?  
**Translation:** Vocabulary: benchmark: 参考标准

**[1518.88s] English:** So from the perspective of how much until we get to human level on a very good benchmark.  
**Translation:** 

**[1526.00s] English:** Yeah. I know  
**Translation:** 

**[1527.44s] English:** I understand what you mean by that. So what I was going to say that a lot of it depends on,  
**Translation:** 

**[1532.08s] English:** once you solve a problem, it stops being hard and that's always true. But if something is hard or not  
**Translation:** 

**[1537.60s] English:** depends on what our tools can do today. So you say today through human level, language understanding  
**Translation:** 

**[1544.64s] English:** and visual perception are hard in the sense that there is no way of solving the problem completely  
**Translation:** 

**[1550.24s] English:** in the next three months. So I agree with that statement. Beyond that, my guess would be as good  
**Translation:** 

**[1556.08s] English:** as yours. I don't know. Okay.  
**Translation:** 

**[1557.28s] English:** Oh, okay. So you don't have a fundamental intuition.  
**Translation:** 

**[1560.00s] English:** about how hard language understanding is i think i i know i changed my mind i'd say language is  
**Translation:** Vocabulary: intuition: 直觉

**[1564.94s] English:** probably going to be harder i mean it depends on how you define it like if you mean absolute  
**Translation:** 

**[1570.30s] English:** top-notch 100 language understanding i'll go with language and so but then if i show you a piece of  
**Translation:** 

**[1577.36s] English:** paper with letters on it is that you see what i mean it's like you have a vision system you say  
**Translation:** 

**[1582.82s] English:** it's the best human level vision system i show you i open a book and i show you letters will it  
**Translation:** 

**[1589.04s] English:** understand how these letters form into word and sentences and meaning is this part of the vision  
**Translation:** 

**[1593.06s] English:** problem where does vision end and language begin yeah so chomsky would say it starts at language  
**Translation:** 

**[1598.10s] English:** so vision is just a little example of the kind of structure and you know fundamental hierarchy  
**Translation:** 

**[1605.88s] English:** of ideas that's already represented in our brain somehow that's represented through language but  
**Translation:** Vocabulary: hierarchy: 等级结构

**[1611.62s] English:** where does vision stop and language begin that's a really  
**Translation:** 

**[1619.04s] English:** interesting uh question  
**Translation:** 

**[1623.18s] English:** so one possibility is that it's impossible to achieve really deep understanding  
**Translation:** 

**[1631.52s] English:** in either images or language without basically using the same kind of system  
**Translation:** 

**[1637.72s] English:** so you're going to get the other for free i think i think it's pretty likely that yes if we can  
**Translation:** 

**[1643.54s] English:** get one we probably our machine learning is probably that good that we can get the other  
**Translation:** 

**[1647.18s] English:** but it's not 100 i'm not 100% sure but i'm not 100% sure but i'm not 100% sure but i'm not 100% sure  
**Translation:** 

**[1649.04s] English:** and also i think a lot a lot of it really does depend on your definitions  
**Translation:** 

**[1656.60s] English:** definitions of like perfect vision because really you know reading is vision but should it count  
**Translation:** 

**[1664.44s] English:** yeah to me so my definition is if a system looked at an image and then a system looked  
**Translation:** 

**[1670.68s] English:** at a piece of text and then told me something about that and i was really impressed that's relative  
**Translation:** 

**[1679.04s] English:** you'll be impressed  
**Translation:** 

**[1680.00s] English:** for half an hour and then you're going to say well i mean all the systems do that but here's  
**Translation:** 

**[1683.76s] English:** the thing they don't do yeah but i don't have that with humans humans continue to impress me  
**Translation:** 

**[1688.72s] English:** is that true well the ones okay so i'm a fan of monogamy so i like the idea of marrying somebody  
**Translation:** 

**[1695.84s] English:** being with them for several decades so i believe in the fact that yes it's possible to have  
**Translation:** Vocabulary: monogamy: 一夫一妻制

**[1700.80s] English:** somebody continuously giving you uh pleasurable interesting witty new ideas friends yeah i think  
**Translation:** 

**[1709.36s] English:** i think so they continue to surprise you the surprise it's um you know that injection of  
**Translation:** Vocabulary: injection: 注入; pleasurable: 愉快的

**[1716.16s] English:** randomness it seems to be uh it seems to be a nice source of yeah continued  
**Translation:** 

**[1725.84s] English:** uh inspiration like the the wit the humor i think yeah that that the that would be  
**Translation:** Vocabulary: randomness: 随机性

**[1733.52s] English:** it's a very subjective test but i think if you have enough humans in the room yeah i  
**Translation:** 

**[1739.20s] English:** i  
**Translation:** 

**[1739.36s] English:** understand what you mean yeah i feel like i i misunderstood what you meant by impressing you  
**Translation:** 

**[1742.96s] English:** i thought you meant to impress you with its intelligence with how how with how good valid  
**Translation:** 

**[1748.48s] English:** understands um an image i thought you meant something like i'm gonna show it a really  
**Translation:** 

**[1752.40s] English:** complicated image and it's gonna get it right and you're gonna say wow that's really cool our  
**Translation:** 

**[1755.76s] English:** systems of you know january 2020 have not been doing that yeah no i i think it all boils down to  
**Translation:** 

**[1762.16s] English:** like the reason people click like on stuff on the internet which is like it makes them laugh so it's  
**Translation:** 

**[1768.48s] English:** like humor  
**Translation:** 

**[1769.76s] English:** or wit yeah or insight i'm sure we'll get it get that as well so forgive the romanticized question  
**Translation:** 

**[1778.08s] English:** but looking back to you what is the most beautiful or surprising idea in deep learning or ai in  
**Translation:** 

**[1784.80s] English:** general you've come across so i think the most beautiful thing about deep learning is that it  
**Translation:** 

**[1789.60s] English:** actually works and i mean it because you got these ideas you got the little  
**Translation:** 

**[1793.92s] English:** neural network you got the back propagation algorithm  
**Translation:** Vocabulary: algorithm: 算法; neural: 神经; propagation: 传播

**[1798.80s] English:** and then you  
**Translation:** 

**[1799.20s] English:** got some theories  
**Translation:** 

**[1800.00s] English:** as to you know this is kind of like the brain so maybe if you make it large if you make the  
**Translation:** 

**[1804.08s] English:** neural network large and you train it on a lot of data then it will do the same function that the  
**Translation:** 

**[1808.94s] English:** brain does and it turns out to be true that's crazy and now we just train these neural networks  
**Translation:** 

**[1814.08s] English:** and you make them larger and they keep getting better and i find it unbelievable i find it  
**Translation:** 

**[1818.26s] English:** unbelievable that this whole ai stuff with neural networks works have you built up an intuition of  
**Translation:** 

**[1824.04s] English:** why are there little bits and pieces of intuitions of insights of why this whole thing works  
**Translation:** Vocabulary: intuition: 直觉; intuitions: 直觉

**[1830.30s] English:** i mean some definitely well we know that optimization we now have good you know  
**Translation:** 

**[1836.42s] English:** we've taken we've had lots of empirical you know huge amounts of empirical reasons to believe that  
**Translation:** Vocabulary: empirical: 经验的; optimization: 优化

**[1842.82s] English:** optimization should work on all most problems we care about do you have insights of what so  
**Translation:** 

**[1848.84s] English:** you just said empirical evidence is most of your  
**Translation:** 

**[1852.02s] English:** you  
**Translation:** 

**[1854.04s] English:** sort of empirical evidence kind of convinces you it's like evolution is empirical it shows you  
**Translation:** Vocabulary: convinces: 证明

**[1860.90s] English:** that look this evolutionary process seems to be a good way to design organisms that survive in  
**Translation:** 

**[1867.00s] English:** their environment but it doesn't really get you to the insights of how the whole thing works i think  
**Translation:** Vocabulary: evolutionary: 进化

**[1874.20s] English:** it's a good analogy is physics you know how you say hey let's do some physics calculation and  
**Translation:** 

**[1879.20s] English:** come up with some new physics theory and make some prediction but then you got around the experiment  
**Translation:** 

**[1882.92s] English:** you know how you say hey let's do some physics calculation and come up with some new physics  
**Translation:** 

**[1884.02s] English:** you know, you got to run the experiment, it's important. So it's a bit the same here,  
**Translation:** 

**[1887.44s] English:** except that maybe sometimes the experiment came before the theory. But it still is the case,  
**Translation:** 

**[1892.10s] English:** you know, you have some data, and you come up with some prediction, you say, yeah, let's make  
**Translation:** 

**[1895.80s] English:** a big neural network, let's train it, and it's going to work much better than anything before  
**Translation:** 

**[1899.68s] English:** it, and it will, in fact, continue to get better as you make it larger. And it turns out to be  
**Translation:** 

**[1903.44s] English:** true. That's, that's amazing when a theory is validated like this, you know, it's not a  
**Translation:** 

**[1908.00s] English:** mathematical theory, it's more of a biological theory almost. So I think there are not terrible  
**Translation:** Vocabulary: mathematical: 数学的; validated: 验证

**[1913.42s] English:** analogies between deep learning and biology. I would say it's like the geometric mean of  
**Translation:** 

**[1917.66s] English:** biology and physics, that's deep learning.  
**Translation:** Vocabulary: analogies: 类比; geometric: 几何

**[1920.00s] English:** the geometric mean of biology and physics i think i'm going to need a few hours to wrap my head  
**Translation:** 

**[1925.72s] English:** around that uh because just to find the geometric just to find uh the set of what biology represents  
**Translation:** 

**[1936.02s] English:** well biology in biology things are really complicated and theories are really really  
**Translation:** 

**[1940.58s] English:** it's really hard to have good predictive theory and if in physics the theories are too good  
**Translation:** Vocabulary: predictive: 可预测的

**[1944.66s] English:** in theory in physics people make these super precise theories which make these amazing  
**Translation:** 

**[1948.54s] English:** predictions and in machine learning we're kind of in between kind of in between but it'd be nice  
**Translation:** 

**[1953.74s] English:** if machine learning somehow helped us discover the unification of the two as opposed to sort of  
**Translation:** 

**[1958.44s] English:** the in-between but you're right that's you're you're kind of trying to juggle both so do you  
**Translation:** Vocabulary: juggle: 兼顾; unification: 统一

**[1965.62s] English:** think there are still beautiful and mysterious properties in neural networks that are yet to  
**Translation:** 

**[1969.36s] English:** be discovered definitely i think that we are still massively underestimating deep learning  
**Translation:** Vocabulary: neural: 神经; underestimating: 低估

**[1973.98s] English:** what do you think it will look like like what  
**Translation:** 

**[1977.32s] English:** find your  
**Translation:** 

**[1978.54s] English:** i would have done it yeah so uh but if you look at all the progress from the past 10 years i would  
**Translation:** 

**[1985.42s] English:** say most of it i would say there have been a few cases where some were things that felt like really  
**Translation:** 

**[1991.40s] English:** new ideas showed up but by and large it was every year we thought okay deep learning goes this far  
**Translation:** 

**[1996.94s] English:** nope it actually goes further and then the next year okay now you now this is this is big deep  
**Translation:** 

**[2002.16s] English:** learning we are really done nope goes further it just keeps going further each year so that  
**Translation:** 

**[2006.26s] English:** means that we keep underestimating we keep not understanding it and we keep not understanding it  
**Translation:** 

**[2008.54s] English:** has surprising properties all the time do you think it's getting harder and harder  
**Translation:** 

**[2013.42s] English:** to make progress need to make progress it depends on what you mean i think the field will continue  
**Translation:** 

**[2017.66s] English:** to make very robust progress for quite a while i think for individual researchers especially people  
**Translation:** 

**[2023.42s] English:** who are doing research it can be harder because there is a very large number of researchers right  
**Translation:** Vocabulary: robust: 强壮的

**[2028.86s] English:** now i think that if you have a lot of compute then you can make a lot of very interesting  
**Translation:** 

**[2034.06s] English:** discoveries but then you have to deal with the challenge of  
**Translation:** 

**[2038.54s] English:** managing a huge computer  
**Translation:** 

**[2040.00s] English:** a huge cluster huge compute cluster to run your experiments it's a little bit harder so i'm asking  
**Translation:** Vocabulary: cluster: 计算集群

**[2044.12s] English:** all these questions that nobody knows the answer to but you're one of the smartest people i know  
**Translation:** 

**[2048.28s] English:** so i'm gonna keep asking the so let's imagine all the breakthroughs that happen in the next 30 years  
**Translation:** Vocabulary: breakthroughs: 重大突破

**[2053.86s] English:** in deep learning do you think most of those breakthroughs can be done by one person with  
**Translation:** 

**[2059.78s] English:** one computer sort of in the space of breakthroughs do you think compute will be uh compute and large  
**Translation:** 

**[2068.76s] English:** efforts will be necessary i mean i can't be sure when you say one computer you mean how large  
**Translation:** 

**[2078.08s] English:** uh you're uh you're clever i mean one one gpu i see i think it's pretty unlikely  
**Translation:** 

**[2085.70s] English:** i think it's pretty unlikely i think that there are many the stack of deep learning is starting  
**Translation:** 

**[2092.50s] English:** to be quite deep if you look at it you've got all the way from the idea  
**Translation:** 

**[2098.76s] English:** the systems to build the data sets the distributed programming the building the actual cluster  
**Translation:** 

**[2105.88s] English:** the gpu programming putting it all together so now the stack is getting really deep and i think  
**Translation:** 

**[2110.92s] English:** becomes it can be quite hard for a single person to become to be world class in every single layer  
**Translation:** 

**[2116.84s] English:** of the stack what about uh what like vladimir vapnik really insists on is taking mnist and  
**Translation:** 

**[2123.32s] English:** trying to learn from very few examples so being able to learn more efficiently  
**Translation:** 

**[2128.76s] English:** do you think that's there'll be breakthroughs in that space that would may not need a huge compute  
**Translation:** 

**[2134.40s] English:** i think there will be a very i think there will be a large number of breakthroughs in general that  
**Translation:** 

**[2138.54s] English:** will not need a huge amount of compute so maybe i should clarify that i think that some breakthroughs  
**Translation:** 

**[2143.66s] English:** will require a lot of compute and i think building systems which actually do things will require a  
**Translation:** 

**[2149.14s] English:** huge amount of compute that one is pretty obvious if you want to do x right and x requires a huge  
**Translation:** 

**[2154.34s] English:** neural net you got to get a huge neural net but i think there will be lots of  
**Translation:** 

**[2158.76s] English:** i think there is lots of  
**Translation:** Vocabulary: neural: 神经网络

**[2160.00s] English:** room for very important work being done by small groups and individuals can you maybe sort of on  
**Translation:** 

**[2166.50s] English:** the topic of the the science of deep learning talk about one of the recent papers that you've  
**Translation:** 

**[2172.72s] English:** released sure the deep double descent where bigger models and more data hurt i think it's a really  
**Translation:** 

**[2178.82s] English:** interesting paper can you can you describe the main idea and yeah definitely so what happened  
**Translation:** 

**[2184.34s] English:** is that some over over the years some small number of researchers noticed that it is kind of weird  
**Translation:** 

**[2190.28s] English:** that when you make the neural network larger it works better and it seems to go in contradiction  
**Translation:** Vocabulary: contradiction: 矛盾

**[2193.22s] English:** with statistical ideas and then some people made an analysis showing that actually you got this  
**Translation:** 

**[2197.74s] English:** double descent bump and what we've done was to show that double descent occurs for all for pretty  
**Translation:** 

**[2203.72s] English:** much all practical deep learning systems and that it'll be also so can you step back um what's the  
**Translation:** 

**[2212.04s] English:** x-axis and the y-axis of a double descent bump  
**Translation:** 

**[2214.34s] English:** okay great so you can you can look you can do things like you can take your neural network  
**Translation:** 

**[2223.68s] English:** and you can start increasing its size slowly while keeping your data set fixed  
**Translation:** 

**[2228.74s] English:** so if you increase the size of the neural network slowly and if you don't do early stopping that's a  
**Translation:** 

**[2237.16s] English:** pretty important detail then when the neural network is really small you make it larger  
**Translation:** 

**[2243.14s] English:** you get a very rapid  
**Translation:** 

**[2244.28s] English:** increase in performance then you continue to make it larger and at some point performance will get  
**Translation:** 

**[2248.26s] English:** worse and it gets and it gets the worst exactly at the point at which it achieves zero training  
**Translation:** 

**[2255.82s] English:** error precisely zero training loss and then as you make it large it starts to get better again  
**Translation:** 

**[2260.56s] English:** and it's kind of counterintuitive because you'd expect deep learning phenomena to be  
**Translation:** 

**[2265.02s] English:** monotonic and it's hard to be sure what it means but it also occurs in in the case of linear  
**Translation:** Vocabulary: counterintuitive: 违反直觉; monotonic: 单调的

**[2272.24s] English:** classifiers and the intuition basically becomes more and more important and it's hard to be sure  
**Translation:** 

**[2274.28s] English:** what it means but it also occurs in in the case of linear classifiers and the intuition basically  
**Translation:** Vocabulary: intuition: 直觉

**[2275.02s] English:** becomes more and more important and it's hard to be sure what it means but it's hard to be sure  
**Translation:** 

**[2277.00s] English:** when you when you have a lot when you have  
**Translation:** 

**[2280.00s] English:** A large data set and a small model, then small, tiny, random.  
**Translation:** 

**[2284.92s] English:** So basically, what is overfitting?  
**Translation:** Vocabulary: overfitting: 模型过拟合

**[2287.20s] English:** Overfitting is when your model is somehow very sensitive to the small, random, unimportant stuff in your data set.  
**Translation:** 

**[2296.02s] English:** In the training data set.  
**Translation:** 

**[2296.96s] English:** In the training data set, precisely.  
**Translation:** 

**[2298.90s] English:** So if you have a small model and you have a big data set, and there may be some random thing, you know, some training cases are randomly in the data set and others may not be there.  
**Translation:** 

**[2308.56s] English:** But the small model is kind of insensitive to this randomness because there is pretty much no uncertainty about the model when the data set is large.  
**Translation:** 

**[2318.40s] English:** So, okay.  
**Translation:** Vocabulary: insensitive: 不敏感; randomness: 随机性

**[2318.92s] English:** So at the very basic level, to me, it is the most surprising thing that neural networks don't overfit every time very quickly before ever being able to learn anything.  
**Translation:** 

**[2334.08s] English:** The huge number of parameters.  
**Translation:** Vocabulary: neural: 神经网络

**[2336.04s] English:** So here is, so there is one way.  
**Translation:** 

**[2337.52s] English:** Okay.  
**Translation:** 

**[2337.72s] English:** So maybe.  
**Translation:** 

**[2338.26s] English:** So let me try to give the explanation and maybe that will be, that will work.  
**Translation:** 

**[2342.08s] English:** So you've got a huge neural network.  
**Translation:** 

**[2343.62s] English:** Let's suppose you've got a, you are, you have a huge neural network, you have a huge number of parameters.  
**Translation:** 

**[2349.46s] English:** And now let's pretend everything is linear, which is not, let's just pretend.  
**Translation:** 

**[2352.92s] English:** Then there is this big subspace where your neural network achieves zero error.  
**Translation:** Vocabulary: subspace: 子空间

**[2358.10s] English:** And SGT is going to find approximately the point.  
**Translation:** 

**[2361.84s] English:** That's right.  
**Translation:** 

**[2362.78s] English:** Approximately the point with the smallest norm in that subspace.  
**Translation:** 

**[2366.46s] English:** Okay.  
**Translation:** 

**[2367.14s] English:** And that cannot.  
**Translation:** 

**[2368.26s] English:** It can also be proven to be insensitive to the small randomness in the data when the dimensionality is high, but when the dimensionality of the data is equal to the dimensionality of the model, then there is a one-to-one correspondence between all the data sets and the models.  
**Translation:** Vocabulary: correspondence: 对应关系; dimensionality: 维数

**[2384.08s] English:** So small changes in the data set actually lead to large changes in the model.  
**Translation:** 

**[2387.34s] English:** And that's why performance gets worse.  
**Translation:** 

**[2388.76s] English:** So this is the best explanation, more or less.  
**Translation:** 

**[2392.06s] English:** So then it would be good for the model to have more parameters.  
**Translation:** 

**[2396.38s] English:** So to be bigger than a data set.  
**Translation:** 

**[2398.60s] English:** That's right.  
**Translation:** 

**[2399.08s] English:** But only if you.  
**Translation:** 

**[2400.00s] English:** early stop if you introduce early stop in your regularization you can make the double descent  
**Translation:** 

**[2404.08s] English:** bump almost completely disappear what is early stop early stopping is when you train your model  
**Translation:** 

**[2409.76s] English:** and you monitor your test your validation performance and then if at some point validation  
**Translation:** Vocabulary: validation: 验证性能

**[2414.64s] English:** performance starts to get worse you say okay let's stop training if you're good you're good you're  
**Translation:** 

**[2418.80s] English:** good enough so the the magic happens after after that moment so you don't want to do the early  
**Translation:** 

**[2424.16s] English:** stopping well if you don't do the early stop and you get this very you get a very pronounced double  
**Translation:** 

**[2428.48s] English:** descent do you have any intuition why this happens double descent oh sorry stopping no  
**Translation:** Vocabulary: intuition: 直觉

**[2435.84s] English:** the double descent so the oh yeah so i try let's see the intuition is basically is this that when  
**Translation:** 

**[2442.08s] English:** the data set has as many degrees of freedom as the model then there is a one-to-one correspondence  
**Translation:** 

**[2448.96s] English:** between them and so small changes to the data set leads to noticeable changes in the model  
**Translation:** 

**[2454.88s] English:** so your model is very sensitive to all the randomness it is unable to  
**Translation:** Vocabulary: randomness: 随机性

**[2458.48s] English:** discard it whereas it turns out that when you have a lot more data than parameters or a lot  
**Translation:** 

**[2466.08s] English:** more parameters than data the resulting solution will be insensitive to small changes in the data  
**Translation:** Vocabulary: insensitive: 不敏感

**[2470.96s] English:** set so it's able to that's nicely put discard the small changes the the randomness exactly the the  
**Translation:** 

**[2478.24s] English:** the spurious correlation which you don't want jeff hinton suggested we need to throw back  
**Translation:** Vocabulary: correlation: 虚假关联; spurious: 虚假的

**[2484.00s] English:** propagation we already kind of talked about this a little bit but he suggested that we just throw  
**Translation:** 

**[2487.84s] English:** and start over i mean of course some of that is a little bit um wit and humor but what do you think  
**Translation:** Vocabulary: propagation: 传播

**[2496.08s] English:** what could be an alternative method of training neural networks well the thing that he said  
**Translation:** 

**[2500.68s] English:** precisely is that to the extent that you can't find backpropagation in the brain it's worth  
**Translation:** 

**[2505.68s] English:** seeing if we can learn something from how the brain learns but backpropagation is very useful  
**Translation:** 

**[2510.44s] English:** and we should keep using it oh you're saying that once we discover the mechanism of learning in the  
**Translation:** Vocabulary: backpropagation: 反向传播

**[2515.88s] English:** brain or any aspects of that mechanism we should also try to implement that  
**Translation:** 

**[2520.00s] English:** neural networks if it turns out that we can't find backpropagation in the brain if we can't  
**Translation:** 

**[2524.46s] English:** find backpropagation in the brain well so i guess your answer to that is backpropagation is pretty  
**Translation:** 

**[2532.92s] English:** damn useful so why are we complaining i mean i i personally am a big fan of backpropagation i think  
**Translation:** 

**[2538.62s] English:** it's a great algorithm because it solves an extremely fundamental problem which is finding  
**Translation:** 

**[2543.62s] English:** a neural circuit subject to some constraints and i don't see that problem going away so that's why i  
**Translation:** 

**[2551.34s] English:** i really i think it's pretty unlikely that you'll have anything which is going to be  
**Translation:** 

**[2556.72s] English:** dramatically different it could happen but i wouldn't bet on it right now  
**Translation:** Vocabulary: dramatically: 剧烈地

**[2561.74s] English:** so let me ask a sort of big picture question do you think can do you think neural networks  
**Translation:** 

**[2569.84s] English:** can be made to reason why not well  
**Translation:** Vocabulary: neural: 神经的

**[2573.52s] English:** you  
**Translation:** 

**[2573.62s] English:** if you look for example at alpha go or alpha zero the neural network of alpha zero plays go  
**Translation:** Vocabulary: alpha: 阿尔法

**[2581.14s] English:** which which we all agree is a game that requires reasoning better than 99.9 of all humans just the  
**Translation:** 

**[2588.84s] English:** neural network without the search just the neural network itself doesn't that give us an existence  
**Translation:** 

**[2594.52s] English:** proof that neural networks can reason to push back and disagree a little bit we all agree that  
**Translation:** 

**[2600.78s] English:** go is reasoning i think  
**Translation:** 

**[2603.52s] English:** i i agree i don't think it's a trivial so obviously reasoning like intelligence is a  
**Translation:** 

**[2609.68s] English:** is a loose gray area term a little bit maybe you disagree with that but yes i think it has  
**Translation:** 

**[2616.40s] English:** some of the same elements of reasoning reasoning is almost like akin to search right there's a  
**Translation:** 

**[2623.36s] English:** sequential element of stepwise consideration of possibilities and sort of building on top of those  
**Translation:** Vocabulary: sequential: 顺序的; stepwise: 逐步的

**[2633.36s] English:** those possibilities in a sequential manner  
**Translation:** 

**[2635.14s] English:** until you arrive at some insight.  
**Translation:** 

**[2637.66s] English:** So yeah, I guess plain go is kind of like  
**Translation:** 

**[2640.00s] English:** that and when you have a single neural network doing that without search that's kind of like  
**Translation:** 

**[2644.68s] English:** that so there's an existent proof in a particular constrained environment that a process akin to  
**Translation:** 

**[2650.20s] English:** what many people call reasoning exists but more general kind of reasoning so off the board there  
**Translation:** Vocabulary: constrained: 限定的

**[2659.02s] English:** is one other existence proof oh boy which one us humans yes okay all right so do you think  
**Translation:** 

**[2666.90s] English:** the architecture that will allow neural networks to reason will look similar to  
**Translation:** 

**[2674.90s] English:** the neural network architectures we have today i think it will i think well i don't want to make  
**Translation:** 

**[2681.42s] English:** two overly definitive statements i think it's definitely possible that the neural networks  
**Translation:** Vocabulary: definitive: 定论

**[2687.70s] English:** that will produce the reasoning breakthroughs of the future will be very similar to the  
**Translation:** 

**[2691.92s] English:** architecture that exists today maybe a little bit more recurrent maybe a little bit deeper  
**Translation:** Vocabulary: breakthroughs: 重大突破; recurrent: 循环的

**[2696.90s] English:** but like these these neural nets are so insanely powerful why wouldn't they be able to learn to  
**Translation:** 

**[2704.36s] English:** reason humans can reason so why can't neural networks so do you think the kind of stuff  
**Translation:** Vocabulary: neural: 神经网络

**[2710.32s] English:** we've seen neural networks do is a kind of just weak reasoning so it's not a fundamentally  
**Translation:** 

**[2715.44s] English:** different process again this is stuff we don't nobody knows the answer to so when it comes to  
**Translation:** Vocabulary: fundamentally: 从根本上

**[2720.94s] English:** our neural networks i would think which i would say is that neural networks are capable of reasoning  
**Translation:** 

**[2726.90s] English:** but if you train a neural network on a task which doesn't require reasoning it's not going to  
**Translation:** 

**[2733.20s] English:** reason this is a well-known effect where the neural network will solve exactly the is will  
**Translation:** 

**[2738.42s] English:** solve the problem that you pose in front of it in the easiest way possible right that takes us to  
**Translation:** 

**[2746.36s] English:** the to one of the brilliant sort of ways you describe neural networks which is uh you've  
**Translation:** 

**[2754.46s] English:** referred to neural networks as the search for small circuits  
**Translation:** Vocabulary: circuits: 电路

**[2756.90s] English:** and maybe  
**Translation:** 

**[2760.00s] English:** general intelligence as the search for small programs, which I found as a metaphor very  
**Translation:** Vocabulary: metaphor: 比喻

**[2766.04s] English:** compelling. Can you elaborate on that difference? Yeah. So, the thing which I said precisely was  
**Translation:** 

**[2772.68s] English:** that if you can find the shortest program that outputs the data at your disposal,  
**Translation:** Vocabulary: compelling: 有说服力的; disposal: 处理; elaborate: 详述

**[2780.58s] English:** then you will be able to use it to make the best prediction possible.  
**Translation:** 

**[2783.96s] English:** Mm-hmm. And that's a theoretical statement, which can be proved mathematically.  
**Translation:** Vocabulary: mathematically: 用数学方法

**[2787.98s] English:** Now, you can also prove mathematically that finding the shortest program which generates  
**Translation:** 

**[2794.46s] English:** some data is not a computable operation. No finite amount of compute can do this.  
**Translation:** Vocabulary: computable: 可计算的; finite: 有限的

**[2802.84s] English:** So then, with neural networks, neural networks are the next best thing that actually works in  
**Translation:** 

**[2808.86s] English:** practice. We are not able to find the shortest program which generates our data, but we are able  
**Translation:** 

**[2816.50s] English:** to find...  
**Translation:** 

**[2817.98s] English:** You know, a small, but now that statement should be amended, even a large circuit, which fits our  
**Translation:** 

**[2823.74s] English:** data in some way. Well, I think what you meant by the small circuit is the smallest needed circuit.  
**Translation:** 

**[2829.90s] English:** Well, the thing which I would change now, back then, I really haven't fully internalized the  
**Translation:** Vocabulary: internalized: 内化

**[2835.82s] English:** over-parameterized results. The things we know about over-parameterized neural nets,  
**Translation:** 

**[2840.46s] English:** now I would phrase it as a large circuit whose weights contain a small amount of information,  
**Translation:** Vocabulary: neural: 神经的

**[2847.98s] English:** I think, is what's going on. If you imagine the training process of a neural network as you slowly  
**Translation:** 

**[2852.14s] English:** transmit entropy from the data set to the parameters, then somehow the amount of information  
**Translation:** Vocabulary: entropy: 混乱度; transmit: 传递

**[2859.64s] English:** in the weights ends up being not very large, which would explain why they generalize so well.  
**Translation:** 

**[2865.34s] English:** So the large circuit might be one that's helpful for the generalization?  
**Translation:** Vocabulary: generalization: 泛化; generalize: 泛化

**[2871.88s] English:** Yeah, something like this.  
**Translation:** 

**[2872.76s] English:** Okay. But do you see it important to be able to...  
**Translation:** 

**[2880.00s] English:** try to learn something like programs i mean if we can definitely i think it's kind of the answer is  
**Translation:** 

**[2886.62s] English:** kind of yes if we can do it we should do things that we can do it it's it's the reason we are  
**Translation:** 

**[2892.78s] English:** pushing on deep learning the fundamental reason the the root cause is that we are able to train  
**Translation:** 

**[2899.78s] English:** them so in other words training comes first we've got our pillar which is the training pillar  
**Translation:** Vocabulary: pillar: 支柱

**[2906.68s] English:** and now we are trying to contort our neural networks around the training pillar we got to  
**Translation:** 

**[2911.28s] English:** stay trainable this is an info this is an invariant we cannot violate and so being trainable means  
**Translation:** 

**[2919.28s] English:** starting from scratch knowing nothing you can actually pretty quickly converge towards knowing  
**Translation:** 

**[2924.00s] English:** a lot or even slowly but it means that given the resources at your disposal  
**Translation:** Vocabulary: converge: 趋于一致; disposal: 处置

**[2930.28s] English:** you can train the neural net and get it to achieve useful performance yeah that's a pillar  
**Translation:** 

**[2936.30s] English:** we can't  
**Translation:** 

**[2936.66s] English:** move away from that's right because if you can whereas if you say hey let's find the shortest  
**Translation:** 

**[2940.42s] English:** program well we can't do that so it doesn't matter how useful that would be we can't do it so we  
**Translation:** 

**[2947.46s] English:** won't so do you think you kind of mentioned that the neural networks are good at finding small  
**Translation:** 

**[2951.54s] English:** circuits or large circuits do you think then the matter of finding small programs is just the data  
**Translation:** Vocabulary: circuits: 电路

**[2958.50s] English:** no so the sorry not not the size or character the qual the the type of data sort of ask giving it  
**Translation:** 

**[2967.86s] English:** programs well i think the thing is that right now finding there are no good precedents of people  
**Translation:** Vocabulary: precedents: 先例

**[2974.90s] English:** successfully finding programs really well and so the way you'd find programs is you'd train a deep  
**Translation:** 

**[2982.20s] English:** neural network to do it basically right which is which is the right way to go about it but there's  
**Translation:** Vocabulary: neural: 神经网络

**[2988.48s] English:** not good uh illustrations of that yes hasn't been done yet but in principle it should be possible  
**Translation:** 

**[2993.98s] English:** can you elaborate a little bit what's your insight in principle  
**Translation:** Vocabulary: elaborate: 详细说明; illustrations: 示例

**[3000.00s] English:** put another way you don't see why it's not possible well it's kind of like more it's more  
**Translation:** 

**[3006.72s] English:** a statement of i think that it's i think that it's unwise to bet against deep learning and  
**Translation:** 

**[3013.56s] English:** if it's a fun if it's a cognitive function that humans seem to be able to do then  
**Translation:** 

**[3018.96s] English:** it doesn't take too long for some deep neural net to pop up that can do it too  
**Translation:** 

**[3024.36s] English:** yeah i'm i'm there with you i can i've i've stopped betting against neural networks at this  
**Translation:** 

**[3032.42s] English:** point because they continue to surprise us what about long-term memory can neural networks have  
**Translation:** 

**[3038.10s] English:** long-term memory or something like knowledge basis so being able to aggregate important  
**Translation:** 

**[3044.86s] English:** information over long periods of time that would then serve as useful sort of representations of  
**Translation:** Vocabulary: aggregate: 汇集

**[3053.34s] English:** states  
**Translation:** 

**[3054.36s] English:** that uh you can make decisions by so have a long-term context based on which you're making  
**Translation:** 

**[3060.30s] English:** the decision so in some sense the parameters already do that the parameters are an aggregation  
**Translation:** 

**[3067.38s] English:** of the day of the neuron of the entirety of the neural net experience and so they count as the  
**Translation:** Vocabulary: aggregation: 聚合; entirety: 全部; neuron: 神经元

**[3071.84s] English:** long as long form long-term knowledge and people have trained various neural nets to act as  
**Translation:** 

**[3078.28s] English:** knowledge bases and you know investigated with invest people have investigated language models  
**Translation:** 

**[3082.88s] English:** as knowledge bases so  
**Translation:** 

**[3084.36s] English:** there is work there is work there yeah but in some sense do you think in every sense do you think  
**Translation:** 

**[3090.18s] English:** there's a it's it's all just a matter of coming up with a better mechanism of forgetting the useless  
**Translation:** 

**[3097.66s] English:** stuff and remembering the useful stuff because right now i mean there's not been mechanisms that  
**Translation:** 

**[3103.20s] English:** do remember really long-term information what do you mean by that precisely precisely i like i like  
**Translation:** 

**[3110.44s] English:** the word precisely so  
**Translation:** 

**[3114.36s] English:** i'm thinking of the kind of compression of information that knowledge bases represent  
**Translation:** 

**[3119.94s] English:** yeah  
**Translation:** Vocabulary: compression: 信息压缩

**[3121.50s] English:** yeah  
**Translation:** 

**[3122.30s] English:** yeah  
**Translation:** 

**[3123.44s] English:** yeah  
**Translation:** 

**[3125.98s] English:** yeah  
**Translation:** 

**[3127.94s] English:** yeah  
**Translation:** 

**[3130.24s] English:** yeah  
**Translation:** 

**[3132.34s] English:** yeah  
**Translation:** 

**[3134.02s] English:** yeah  
**Translation:** 

**[3136.72s] English:** yeah  
**Translation:** 

**[3139.82s] English:** yeah  
**Translation:** 

**[3140.88s] English:** yeah  
**Translation:** 

**[3142.38s] English:** yeah  
**Translation:** 

**[3143.34s] English:** yeah  
**Translation:** 

**[3120.00s] English:** sort of creating a now i apologize for my sort of human centric thinking about  
**Translation:** 

**[3127.14s] English:** what knowledge is because neural networks aren't interpretable necessarily with the kind of  
**Translation:** 

**[3133.52s] English:** knowledge they have discovered but a good example for me is knowledge bases being able to build up  
**Translation:** Vocabulary: interpretable: 可解释的; neural: 神经的

**[3139.70s] English:** over time something like the knowledge that wikipedia represents it's a really compressed  
**Translation:** 

**[3145.34s] English:** structured knowledge base obviously not the actual wikipedia or the language but like a  
**Translation:** Vocabulary: compressed: 压缩的

**[3154.80s] English:** semantic web the dream that semantic web represented so it's a really nice compressed  
**Translation:** 

**[3159.20s] English:** knowledge base or something akin to that in the non-interpretable sense as neural networks would  
**Translation:** Vocabulary: semantic: 语义的

**[3166.36s] English:** have well the neural networks would be non-interpretable if you look at their rates but  
**Translation:** 

**[3169.72s] English:** their outputs should be very interpretable okay so yeah how do you how do you make  
**Translation:** 

**[3173.84s] English:** very smart  
**Translation:** 

**[3175.20s] English:** neural networks like language models interpretable well you ask them to generate some text and the  
**Translation:** 

**[3180.44s] English:** text it would generally be interpretable do you find that the epitome of interpretability like  
**Translation:** 

**[3184.90s] English:** can you do better like can you because you can't okay i'd like to know what does it know what  
**Translation:** Vocabulary: epitome: 典范; interpretability: 可解释性

**[3190.58s] English:** doesn't know i would like the neural network to come up with examples where it it's completely  
**Translation:** 

**[3196.94s] English:** dumb and examples where it's completely brilliant and the only way i know how to do that now is to  
**Translation:** 

**[3202.64s] English:** generate a lot of examples and use my  
**Translation:** 

**[3205.02s] English:** you  
**Translation:** 

**[3205.20s] English:** mean judgment but it would be nice if and you know had some aware self-awareness about yeah  
**Translation:** 

**[3211.82s] English:** 100 100 i'm a big believer in self-awareness and i think that i think i think neural net  
**Translation:** 

**[3219.24s] English:** self-awareness will allow for things like the capabilities like the ones you described like  
**Translation:** 

**[3223.92s] English:** for them to know what they know and what they don't know and for them to know where to invest  
**Translation:** 

**[3228.64s] English:** to increase their skills most optimally and to your question of interpretability there are actually  
**Translation:** 

**[3232.58s] English:** two answers to that question one answer is you know you're not going to be able to interpretability  
**Translation:** Vocabulary: optimally: 最优化地

**[3235.20s] English:** you know we have the neural net so we can analyze the neurons and we can try to understand what the  
**Translation:** 

**[3240.00s] English:** different layers mean. And you can actually do that and OpenAI has done some work on that.  
**Translation:** Vocabulary: neurons: 神经元

**[3246.00s] English:** But there is a different answer, which is that, I would say that's the human centric  
**Translation:** 

**[3251.02s] English:** answer where you say, you know, you look at a human being, you can't read, you know, how  
**Translation:** 

**[3257.12s] English:** do you know what a human being is thinking? You ask them, you say, Hey, what do you think  
**Translation:** 

**[3260.04s] English:** about this? What do you think about that? And you get some answers.  
**Translation:** 

**[3264.16s] English:** The answers you get are sticky in the sense you already have a mental model. You already  
**Translation:** 

**[3268.26s] English:** have a mental model of that human being. You already have an understanding of a big conception  
**Translation:** Vocabulary: conception: 概念

**[3277.12s] English:** of that human being, how they think, what they know, how they see the world. And then  
**Translation:** 

**[3281.88s] English:** everything you ask, you're adding onto that. And that stickiness seems to be, that's one  
**Translation:** 

**[3290.16s] English:** of the really interesting qualities of the human being is that information is sticky.  
**Translation:** 

**[3295.82s] English:** You seem to remember the useful stuff, aggregate it well.  
**Translation:** Vocabulary: aggregate: 聚合

**[3298.24s] English:** And forget most of the information that's not useful. That process, but that's also  
**Translation:** 

**[3304.26s] English:** pretty similar to the process that neural networks do. It's just that neural networks  
**Translation:** Vocabulary: neural: 神经网络

**[3308.06s] English:** are much crappier at this time. It doesn't seem to be fundamentally that different. But  
**Translation:** 

**[3313.66s] English:** just to stick on reasoning for a little longer, you said, why not? Why can't I reason? What's  
**Translation:** Vocabulary: crappier: 更糟糕; fundamentally: 本质上

**[3320.12s] English:** a good, impressive feat, benchmark to you of reasoning?  
**Translation:** 

**[3327.68s] English:** That you'll be important.  
**Translation:** Vocabulary: benchmark: 标准

**[3328.24s] English:** I'm impressed by if neural networks were able to do. Is that something you already have  
**Translation:** 

**[3331.62s] English:** in mind?  
**Translation:** 

**[3332.62s] English:** Well, I think writing really good code. I think proving really hard theorems. Solving  
**Translation:** 

**[3340.58s] English:** open-ended problems with out-of-the-box solutions.  
**Translation:** Vocabulary: theorems: 定理

**[3346.16s] English:** And sort of theorem-type mathematical problems.  
**Translation:** 

**[3349.12s] English:** Yeah. I think those ones are a very natural example as well. If you can prove an unproven  
**Translation:** Vocabulary: mathematical: 数学的; unproven: 未证明

**[3354.06s] English:** theorem, then it's hard to argue you don't reason.  
**Translation:** 

**[3357.68s] English:** And so, by the way, and this comes back to the point about the hardware.  
**Translation:** Vocabulary: theorem: 定理

**[3360.00s] English:** results you know if you got a heart if you have machine learning deep learning as a field is very  
**Translation:** 

**[3365.54s] English:** fortunate because we have the ability to sometimes produce these unambiguous results and when they  
**Translation:** Vocabulary: unambiguous: 明确无误

**[3371.28s] English:** happen the debate changes the conversation changes it's a converse we have the ability to produce  
**Translation:** 

**[3377.04s] English:** conversation changing results conversation and then of course just like you said people kind of  
**Translation:** Vocabulary: converse: 相反的谈话

**[3382.26s] English:** take that for granted say that wasn't actually a hard problem well i mean at some point we'll  
**Translation:** 

**[3386.50s] English:** probably run out of heart problems yeah that whole mortality thing is kind of kind of a sticky  
**Translation:** 

**[3393.18s] English:** problem that we haven't quite figured out maybe we'll solve that one i think one of the fascinating  
**Translation:** 

**[3398.76s] English:** things in your entire body of work but also the work at open ai recently one of the conversation  
**Translation:** 

**[3403.86s] English:** changers has been in the world of language models can you briefly kind of try to describe the recent  
**Translation:** 

**[3410.62s] English:** history of using neural networks in the domain of language and text well there's been lots of history  
**Translation:** 

**[3415.82s] English:** you  
**Translation:** 

**[3416.50s] English:** think i think the elman network was was a was a small tiny recurrent neural network applied to  
**Translation:** Vocabulary: elman: 埃姆兰网络; recurrent: 循环的

**[3421.74s] English:** language back in the 80s so the history is really you know fairly long at least and the thing that  
**Translation:** 

**[3430.14s] English:** started the thing that changed the trajectory of neural networks and language is the thing that  
**Translation:** Vocabulary: neural: 神经; trajectory: 轨迹

**[3436.38s] English:** changed the trajectory of all deep learning and that's data and compute so suddenly you move from  
**Translation:** 

**[3441.10s] English:** small language models which learn a little bit and with language models in particular you can  
**Translation:** 

**[3446.50s] English:** understand the signal and how it's actually apoyable and also the dislike to language methods  
**Translation:** 

**[3452.66s] English:** and as you will see you can sort of understand there's a very clear explanation for why they need  
**Translation:** Vocabulary: apoyable: 可支持的

**[3457.14s] English:** to be large to be good because they're trying to predict the next word so we don't when you don't  
**Translation:** 

**[3462.90s] English:** know anything you'll notice very very broad stroke surface level patterns like sometimes there are  
**Translation:** 

**[3470.74s] English:** characters and there is a space between those characters you'll notice this pattern and you'll  
**Translation:** 

**[3474.50s] English:** notice that sometimes there is a comma and then the next character is a capital letter you'll notice that pattern eventually you may start to notice that there are certain words or  
**Translation:** 

**[3476.26s] English:** words orン  
**Translation:** 

**[3476.30s] English:** occur often you may notice that spellings are a thing you may notice  
**Translation:** Vocabulary: spellings: 拼写方式

**[3480.00s] English:** syntax. And when you get really good at all these, you start to notice the semantics.  
**Translation:** 

**[3485.94s] English:** You start to notice the facts. But for that to happen, the language model needs to be  
**Translation:** Vocabulary: semantics: 语义; syntax: 句法

**[3490.14s] English:** larger.  
**Translation:** 

**[3491.14s] English:** So let's linger on that, because that's where you and Noam Chomsky disagree. So you  
**Translation:** Vocabulary: chomsky: 乔姆斯基

**[3499.58s] English:** think we're actually taking incremental steps, a sort of larger network, larger compute will  
**Translation:** 

**[3505.78s] English:** be able to get to the semantics, be able to understand language without what Noam likes  
**Translation:** Vocabulary: incremental: 逐步的

**[3514.56s] English:** to sort of think of as fundamental understandings of the structure of language, like imposing  
**Translation:** 

**[3521.92s] English:** your theory of language onto the learning mechanism. So you're saying the learning,  
**Translation:** Vocabulary: imposing: 强加; understandings: 理解

**[3528.10s] English:** you can learn from raw data the mechanism that underlies language.  
**Translation:** 

**[3533.28s] English:** Well, I think it's possible.  
**Translation:** 

**[3535.78s] English:** It's pretty likely.  
**Translation:** 

**[3536.86s] English:** But I also want to say that I don't really know precisely what Chomsky means when he  
**Translation:** 

**[3544.58s] English:** talks about... you said something about imposing your structure on language. I'm not 100% sure  
**Translation:** 

**[3549.80s] English:** what he means, but empirically, it seems that when you inspect those larger language models,  
**Translation:** Vocabulary: empirically: 根据经验

**[3554.72s] English:** they exhibit signs of understanding the semantics, whereas the smaller language models do not.  
**Translation:** 

**[3558.34s] English:** We've seen that a few years ago when we did work on the sentiment neuron. We trained a  
**Translation:** Vocabulary: neuron: 神经元; sentiment: 情绪

**[3562.46s] English:** small, you know, smallish LSTM to predict the semantics.  
**Translation:** 

**[3565.56s] English:** So, you know, you can predict the next character in Amazon reviews. And we noticed that when  
**Translation:** Vocabulary: smallish: 较小的

**[3569.72s] English:** you increase the size of the LSTM from 500 LSTM cells to 4,000 LSTM cells, then one of  
**Translation:** 

**[3575.74s] English:** the neurons starts to represent the sentiment of the article, of, sorry, of the review.  
**Translation:** Vocabulary: neurons: 神经元

**[3582.14s] English:** Now why is that? Sentiment is a pretty semantic attribute. It's not a syntactic attribute.  
**Translation:** 

**[3587.02s] English:** And for people who might not know, I don't know if that's a standard term, but sentiment  
**Translation:** Vocabulary: attribute: 属性; semantic: 语义; syntactic: 句法

**[3590.06s] English:** is whether it's a positive or a negative review.  
**Translation:** 

**[3592.20s] English:** That's right. Like, is the person happy with something or is the person unhappy with something?  
**Translation:** 

**[3594.64s] English:** Yeah.  
**Translation:** 

**[3595.56s] English:** And so here we had very clear evidence that a small neural  
**Translation:** 

**[3600.00s] English:** net does not capture sentiment while a large neural net does and why is that well our theory  
**Translation:** 

**[3605.44s] English:** is that at some point you run out of syntax to models you start to gotta focus on something else  
**Translation:** Vocabulary: neural: 神经网络

**[3610.96s] English:** and with size you quickly run out of syntax to model and then you really start to focus on the  
**Translation:** 

**[3617.44s] English:** semantics this would be the idea that's right and so i don't i don't want to imply that our models  
**Translation:** Vocabulary: semantics: 语义; syntax: 句法

**[3622.08s] English:** have complete semantic understanding because that's not true but they definitely are showing  
**Translation:** 

**[3627.76s] English:** signs of semantic understanding partial semantic understanding but the smaller models do not show  
**Translation:** 

**[3632.48s] English:** that those signs can you take a step back and say what is gpt2 which is one of the big language  
**Translation:** 

**[3639.92s] English:** models that was the conversation changer in the past couple years yes so so gpt2 is a transformer  
**Translation:** 

**[3648.00s] English:** with one and a half billion parameters that was trained on on about 40 billion tokens of text  
**Translation:** 

**[3656.16s] English:** which were obtained  
**Translation:** 

**[3657.76s] English:** from web pages that were linked to from reddit articles with more than three upvotes and what's  
**Translation:** 

**[3662.56s] English:** the transformer the transformer is the most important advance in neural network architectures  
**Translation:** 

**[3668.00s] English:** in recent history what is attention maybe too because i think that's an interesting idea not  
**Translation:** 

**[3673.36s] English:** necessarily sort of technically speaking but the idea of attention versus maybe what recurrent networks  
**Translation:** Vocabulary: recurrent: 循环神经网络

**[3680.48s] English:** represent yeah so the thing is the transformer is a combination of multiple ideas simultaneously of  
**Translation:** 

**[3685.84s] English:** which attention is one  
**Translation:** 

**[3687.92s] English:** do you think attention is the key no it's a key but it's not the key the transformer is successful  
**Translation:** 

**[3694.40s] English:** because it is the simultaneous combination of multiple ideas and if you were to remove either  
**Translation:** Vocabulary: simultaneous: 同时发生

**[3698.64s] English:** idea it would be much less successful so the transformer uses a lot of attention but attention  
**Translation:** 

**[3704.24s] English:** existed for a few years so that can't be the main innovation the transformer is designed in such a  
**Translation:** 

**[3712.08s] English:** way that it runs really fast on the gpu and that makes a huge amount of difference  
**Translation:** 

**[3717.76s] English:** this is one thing the second thing  
**Translation:** 

**[3720.00s] English:** is that transformer is not recurrent and that is really important too because it is more shallow  
**Translation:** 

**[3726.24s] English:** and therefore much easier to optimize so in other words it uses attention it is it is a really great  
**Translation:** Vocabulary: optimize: 优化

**[3732.40s] English:** fit to the gpu and it is not recurrent so therefore less deep and easier to optimize  
**Translation:** 

**[3737.76s] English:** and the combination of those factors make it successful so now it makes it makes great use  
**Translation:** 

**[3742.88s] English:** of your gpu it allows you to achieve better results for the same amount of compute and  
**Translation:** 

**[3748.64s] English:** that's why it's successful were you surprised how well transformers worked and gpt2 worked  
**Translation:** 

**[3756.00s] English:** so you worked on language you've had a lot of great ideas before transformers came about in  
**Translation:** 

**[3761.68s] English:** language so you got to see the whole set of revolutions before and after were you surprised  
**Translation:** Vocabulary: revolutions: 变革

**[3767.44s] English:** yeah a little a little yeah i mean it's hard it's hard to remember because you adapt really quickly  
**Translation:** 

**[3774.32s] English:** but it definitely was surprising it definitely was in fact i'll you know what i'll  
**Translation:** 

**[3778.96s] English:** i'll retract my statement it was it was pretty amazing it was just amazing to see generate this  
**Translation:** 

**[3784.40s] English:** text of this and you know you gotta keep in mind that we've seen at that time we've seen all this  
**Translation:** 

**[3789.20s] English:** progress in gans in improving you know the samples produced by gans were just amazing you have these  
**Translation:** 

**[3795.04s] English:** realistic faces but text hasn't really moved that much and suddenly we moved from you know whatever  
**Translation:** 

**[3800.72s] English:** gans were in 2015 to the best most amazing gans in one step right and i was really stunning even  
**Translation:** 

**[3808.64s] English:** for myself to see that and and not even to think about the data it's really amazing and i know  
**Translation:** 

**[3814.64s] English:** it's been a really hard and really powerful step for me and you know that's not a really  
**Translation:** 

**[3818.56s] English:** big deal but i think when you start to look again basically you start to get to know how  
**Translation:** 

**[3822.80s] English:** it works because you're able to predict yes you train a big language model of course you should  
**Translation:** 

**[3826.88s] English:** get this but then to see it with your own eyes it's something else and yet we adapt really quickly  
**Translation:** 

**[3832.40s] English:** and now there's uh sort of some cognitive scientists write articles saying that gpt2 models  
**Translation:** 

**[3836.96s] English:** don't truly understand language so we adapt quickly to how amazing the fact that they're able to model the language so well is so what do you think is the bar well how is the bar?  
**Translation:** 

**[3838.64s] English:** For what?  
**Translation:** 

**[3839.44s] English:** For...  
**Translation:** 

**[3840.00s] English:** pressing us that it i don't know do you think that bar will continuously be moved definitely  
**Translation:** 

**[3846.54s] English:** i think when you start to see really dramatic economic impact that's when i think that's in  
**Translation:** 

**[3852.60s] English:** some sense the next barrier because right now if you think about the work in ai it's really  
**Translation:** 

**[3857.34s] English:** confusing it's really hard to know what to make of all these advances it's kind of like okay  
**Translation:** 

**[3863.46s] English:** you got an advance and now you can do more things and you got another improvement and you got  
**Translation:** 

**[3869.36s] English:** another cool demo at some point i think people who are outside of ai they can no longer distinguish  
**Translation:** 

**[3877.52s] English:** this progress anymore so we were talking offline about translating russian to english and how  
**Translation:** 

**[3882.40s] English:** there's a lot of brilliant work in russian that the rest of the world doesn't know about that's  
**Translation:** 

**[3886.68s] English:** true for chinese it's true for a lot of for a lot of scientists and just artistic work in general  
**Translation:** 

**[3891.68s] English:** do you think translation is the place where we're going to see sort of economic  
**Translation:** 

**[3895.48s] English:** big impact i don't know i think i think there is a huge  
**Translation:** 

**[3899.34s] English:** I mean, first of all, I want to point out that translation already today is huge.  
**Translation:** 

**[3905.58s] English:** I think billions of people interact with big chunks of the Internet primarily through translation.  
**Translation:** 

**[3911.18s] English:** So translation is already huge, and it's hugely, hugely positive, too.  
**Translation:** 

**[3916.28s] English:** I think self-driving is going to be hugely impactful.  
**Translation:** 

**[3920.44s] English:** And that's, you know, it's unknown exactly when it happens.  
**Translation:** 

**[3924.48s] English:** But again, I would not bet against deep learning.  
**Translation:** 

**[3926.92s] English:** So there's deep learning in general.  
**Translation:** 

**[3929.98s] English:** Deep learning for self-driving.  
**Translation:** 

**[3931.86s] English:** Yes, deep learning for self-driving.  
**Translation:** 

**[3933.14s] English:** But I was talking about sort of language models.  
**Translation:** 

**[3935.28s] English:** I see.  
**Translation:** 

**[3936.16s] English:** I veered off a little bit.  
**Translation:** 

**[3938.16s] English:** Just to check, you're not seeing a connection between driving and language?  
**Translation:** Vocabulary: veered: 偏离

**[3941.14s] English:** No, no.  
**Translation:** 

**[3941.68s] English:** Okay.  
**Translation:** 

**[3942.34s] English:** Or rather, both use neural nets.  
**Translation:** 

**[3944.16s] English:** That would be a poetic connection.  
**Translation:** Vocabulary: neural: 神经网络

**[3945.58s] English:** I think there might be some.  
**Translation:** 

**[3947.10s] English:** Like you said, there might be some kind of unification towards a kind of multitask transformers  
**Translation:** Vocabulary: multitask: 多任务; unification: 统一

**[3954.20s] English:** that can take on both language and vision tasks.  
**Translation:** 

**[3958.22s] English:** That would be an interesting.  
**Translation:** 

**[3959.68s] English:** That's awesome.  
**Translation:** 

**[3959.86s] English:** Thank you, bag.  
**Translation:** 

**[3960.06s] English:** You're welcome.  
**Translation:** 

**[3960.76s] English:** You're welcome.  
**Translation:** 

**[3962.58s] English:** Bye-bye.  
**Translation:** 

**[3963.36s] English:** Bye-bye.  
**Translation:** 

**[3963.54s] English:** Bye-bye.  
**Translation:** 

**[3963.80s] English:** Bye.  
**Translation:** 

**[3963.82s] English:** Bye.  
**Translation:** 

**[3960.00s] English:** Unification.  
**Translation:** 

**[3961.38s] English:** Let's see, what can I ask about GPT-2 more?  
**Translation:** 

**[3964.90s] English:** It's simple.  
**Translation:** 

**[3965.62s] English:** There's not much to ask.  
**Translation:** 

**[3967.32s] English:** You take a transform, you make it bigger, you give it more data,  
**Translation:** 

**[3970.68s] English:** and suddenly it does all those amazing things.  
**Translation:** 

**[3972.64s] English:** Yeah, one of the beautiful things is that GPT,  
**Translation:** 

**[3974.92s] English:** the transformers are fundamentally simple to explain, to train.  
**Translation:** 

**[3980.02s] English:** Do you think bigger will continue to show better results in language?  
**Translation:** Vocabulary: fundamentally: 本质上

**[3986.94s] English:** Probably.  
**Translation:** 

**[3987.38s] English:** Sort of like, what are the next steps with GPT-2, do you think?  
**Translation:** 

**[3991.40s] English:** I mean, I think for sure seeing what larger versions can do is one direction.  
**Translation:** 

**[3997.64s] English:** Also, I mean, there are many questions.  
**Translation:** 

**[4001.22s] English:** There's one question which I'm curious about, and that's the following.  
**Translation:** 

**[4003.90s] English:** So right now, GPT-2, so we fitted all this data from the internet,  
**Translation:** 

**[4006.94s] English:** which means that it needs to memorize all those random facts  
**Translation:** 

**[4009.38s] English:** about everything in the internet.  
**Translation:** Vocabulary: memorize: 记忆

**[4011.76s] English:** And it would be nice if the model could somehow use it  
**Translation:** 

**[4017.24s] English:** so that it can be used in the internet.  
**Translation:** 

**[4017.36s] English:** It needs to have its own intelligence to decide what data it wants to accept  
**Translation:** 

**[4021.62s] English:** and what data it wants to reject.  
**Translation:** 

**[4023.40s] English:** Just like people.  
**Translation:** 

**[4024.30s] English:** People don't learn all data indiscriminately.  
**Translation:** Vocabulary: indiscriminately: 不分好坏

**[4027.16s] English:** We are super selective about what we learn.  
**Translation:** 

**[4029.88s] English:** And I think this kind of active learning, I think, would be very nice to have.  
**Translation:** Vocabulary: selective: 挑拣的

**[4034.28s] English:** Yeah, listen, I love active learning.  
**Translation:** 

**[4036.80s] English:** So let me ask, does the selection of data,  
**Translation:** 

**[4041.06s] English:** can you just elaborate that a little bit more?  
**Translation:** 

**[4042.94s] English:** Do you think the selection of data is,  
**Translation:** Vocabulary: elaborate: 详细说明

**[4046.10s] English:** like, I have this kind of sense that the optimization of how you select data,  
**Translation:** 

**[4053.82s] English:** so the active learning process is going to be a place for a lot of breakthroughs,  
**Translation:** Vocabulary: breakthroughs: 重大突破; optimization: 优化

**[4060.00s] English:** even in the near future,  
**Translation:** 

**[4062.10s] English:** because there hasn't been many breakthroughs there that are public.  
**Translation:** 

**[4064.90s] English:** I feel like there might be private breakthroughs that companies keep to themselves  
**Translation:** 

**[4068.90s] English:** because the fundamental problem has to be solved  
**Translation:** 

**[4071.00s] English:** if you want to solve self-driving, if you want to solve a particular task.  
**Translation:** 

**[4074.74s] English:** What do you think about the space in general?  
**Translation:** 

**[4077.84s] English:** Yeah, so I think that for something like active learning,  
**Translation:** 

**[4080.00s] English:** or in fact for any kind of capability like active learning the thing that it really needs is a  
**Translation:** Vocabulary: capability: 能力

**[4084.80s] English:** problem it needs a problem that requires it it's very hard to do research about the capability if  
**Translation:** 

**[4092.16s] English:** you don't have a task because then what's going to happen is you will come up with an artificial task  
**Translation:** 

**[4096.22s] English:** get good results but not really convince anyone right like we're now past the stage where  
**Translation:** 

**[4103.34s] English:** getting a result on MNIST some clever formulation of MNIST will convince people that's right in fact  
**Translation:** 

**[4111.52s] English:** you could quite easily come up with a simple active learning scheme on MNIST and get a 10x  
**Translation:** 

**[4116.10s] English:** speed up but then so what and I think that with active learning there needs the need  
**Translation:** 

**[4122.56s] English:** active learning will naturally arise as there are as problems that require it to pop up  
**Translation:** 

**[4128.32s] English:** that's how I would that's my my take on it  
**Translation:** 

**[4131.76s] English:** there's another  
**Translation:** 

**[4133.32s] English:** interesting thing that OpenAI has brought up with GPT-2 which is when you create a powerful  
**Translation:** 

**[4139.46s] English:** artificial intelligence system and it was unclear what kind of detrimental once you release GPT-2  
**Translation:** 

**[4146.56s] English:** what kind of detrimental effect it will have because if you have an a model that can generate  
**Translation:** 

**[4152.00s] English:** pretty realistic text you can start to imagine that you know on the it would be used by bots in  
**Translation:** 

**[4158.40s] English:** some some way that we can't even imagine so like there's this nervousness about what  
**Translation:** Vocabulary: nervousness: 焦虑感

**[4163.30s] English:** it's possible to do so you you did a really kind of brave and I think profound thing which  
**Translation:** 

**[4168.18s] English:** is started conversation about this like how do we release powerful artificial intelligence  
**Translation:** Vocabulary: profound: 深思熟虑的

**[4174.10s] English:** models to the public if we do it all how do we privately discuss with other even competitors  
**Translation:** 

**[4182.04s] English:** about how we manage the use of the systems and so on so from that this whole experience  
**Translation:** Vocabulary: privately: 私下里

**[4187.90s] English:** you release the report on it but in general are there any insights that you've gathered  
**Translation:** 

**[4192.44s] English:** from just thinking about this about how you release models like this I mean I think that my take on  
**Translation:** 

**[4200.00s] English:** this is that the field of AI has been in a state of childhood and now it's exiting that state and  
**Translation:** 

**[4206.92s] English:** it's entering a state of maturity. What that means is that AI is very successful and also very  
**Translation:** Vocabulary: maturity: 成熟期

**[4212.88s] English:** impactful and its impact is not only large but it's also growing and so for that reason it seems  
**Translation:** 

**[4220.48s] English:** wise to start thinking about the impact of our systems before releasing them maybe a little bit  
**Translation:** 

**[4226.50s] English:** too soon rather than a little bit too late and with the case of GPT-2 like I mentioned earlier  
**Translation:** 

**[4232.42s] English:** the results really were stunning and it seemed plausible it didn't seem certain it seemed  
**Translation:** Vocabulary: plausible: 合情合理

**[4238.98s] English:** plausible that something like GPT-2 could easily use to reduce the cost of disinformation  
**Translation:** 

**[4244.98s] English:** and so there was a question of what's the best way to release it and a staged release seemed  
**Translation:** Vocabulary: disinformation: 虚假信息

**[4251.10s] English:** logical. A small model was released and there was time to see the  
**Translation:** 

**[4256.50s] English:** many people use these models in lots of cool ways there've been lots of really cool applications  
**Translation:** 

**[4261.08s] English:** there haven't been any negative application that we know of and so eventually it was released but  
**Translation:** 

**[4267.70s] English:** also other people replicated similar models. That's an interesting question though that we  
**Translation:** 

**[4271.56s] English:** know of. So in your view staged release is at least part of the answer to the question of how do we  
**Translation:** 

**[4280.42s] English:** how what do we do once we create a system like this?  
**Translation:** 

**[4285.98s] English:** It's part of the question.  
**Translation:** 

**[4286.50s] English:** Is there any other insights like say you don't want to release the model at all because it's  
**Translation:** 

**[4292.86s] English:** useful to you for whatever the business is? Well there are plenty of people don't release  
**Translation:** 

**[4297.92s] English:** models already. Right of course but is there some moral ethical responsibility when you have a very  
**Translation:** 

**[4305.34s] English:** powerful model to sort of communicate like just as you said when you had GPT-2 it was unclear how  
**Translation:** 

**[4312.56s] English:** much it could be used for misinformation. It's an open question.  
**Translation:** Vocabulary: misinformation: 虚假信息

**[4315.14s] English:** And getting an answer to that might require that you talk to other release.  
**Translation:** 

**[4320.00s] English:** smart people that are outside of your particular group.  
**Translation:** 

**[4325.12s] English:** Please tell me there's some optimistic pathway for people across the world  
**Translation:** 

**[4330.42s] English:** to collaborate on these kinds of cases.  
**Translation:** Vocabulary: collaborate: 合作; optimistic: 乐观; pathway: 途径

**[4334.26s] English:** Or is it still really difficult from one company to talk to another company?  
**Translation:** 

**[4338.98s] English:** So it's definitely possible.  
**Translation:** 

**[4341.18s] English:** It's definitely possible to discuss these kind of models with colleagues elsewhere  
**Translation:** 

**[4347.52s] English:** and to get their take on what to do.  
**Translation:** 

**[4352.22s] English:** How hard is it, though?  
**Translation:** 

**[4353.60s] English:** I mean...  
**Translation:** 

**[4355.58s] English:** Do you see that happening?  
**Translation:** 

**[4357.88s] English:** I think that's a place where it's important to gradually build trust between companies.  
**Translation:** 

**[4363.14s] English:** Because ultimately, all the AI developers are building technology  
**Translation:** 

**[4367.86s] English:** which is going to be increasingly more powerful.  
**Translation:** 

**[4370.92s] English:** And so it's...  
**Translation:** 

**[4373.86s] English:** The way to think about it is that ultimately we're all in it together.  
**Translation:** 

**[4378.40s] English:** Yeah, it's...  
**Translation:** 

**[4379.64s] English:** I tend to believe in the better angels of our nature,  
**Translation:** 

**[4384.44s] English:** but I do hope that when you build a really powerful AI system in a particular domain,  
**Translation:** 

**[4392.36s] English:** that you also think about the potential negative consequences of...  
**Translation:** 

**[4397.96s] English:** Yeah.  
**Translation:** 

**[4401.94s] English:** It's an interesting and scary possibility that there will be a race for AI development  
**Translation:** 

**[4407.16s] English:** that will...  
**Translation:** 

**[4407.52s] English:** That would push people to close that development  
**Translation:** 

**[4409.80s] English:** and not share ideas with others.  
**Translation:** 

**[4413.20s] English:** I don't love this.  
**Translation:** 

**[4414.58s] English:** I've been a pure academic for 10 years.  
**Translation:** 

**[4416.66s] English:** I really like sharing ideas and it's fun.  
**Translation:** 

**[4418.88s] English:** It's exciting.  
**Translation:** 

**[4421.32s] English:** What do you think it takes to...  
**Translation:** 

**[4422.72s] English:** Let's talk about AGI a little bit.  
**Translation:** 

**[4424.26s] English:** What do you think it takes to build a system of human-level intelligence?  
**Translation:** 

**[4427.92s] English:** We talked about reasoning.  
**Translation:** 

**[4429.18s] English:** We talked about long-term memory.  
**Translation:** 

**[4431.34s] English:** But in general, what does it take, do you think?  
**Translation:** 

**[4433.74s] English:** Well, I can't be sure.  
**Translation:** 

**[4435.82s] English:** But I think that deep learning plus maybe...  
**Translation:** 

**[4440.00s] English:** be another small idea do you think self-play will be involved sort of like you've spoken about the  
**Translation:** 

**[4447.16s] English:** powerful mechanism of self-play where systems learn by sort of uh exploring the world in a  
**Translation:** 

**[4455.56s] English:** competitive setting against other entities that are similarly skilled as them and so incrementally  
**Translation:** Vocabulary: incrementally: 逐步地

**[4461.68s] English:** improve in this way do you think self-play will be a component of building an agi system  
**Translation:** 

**[4466.46s] English:** um yeah so what i would say to build agi i think is going to be deep learning plus some ideas  
**Translation:** 

**[4474.16s] English:** and i think self-play will be one of those ideas i think that that is a very  
**Translation:** 

**[4480.14s] English:** self-play has this amazing property that it can surprise us  
**Translation:** 

**[4486.24s] English:** in truly novel ways for example like we i mean pretty much every self-play system  
**Translation:** 

**[4496.46s] English:** both are dota bot i don't know if openai had a release about multi-agent where you had two  
**Translation:** 

**[4503.46s] English:** little agents were playing hide and seek and of course also alpha zero they were all produced  
**Translation:** 

**[4509.20s] English:** surprising behaviors they all produce behaviors that we didn't expect they are creative solutions  
**Translation:** Vocabulary: alpha: 阿尔法

**[4514.34s] English:** to problems and that seems like an important part of agi that our systems don't exhibit routinely  
**Translation:** 

**[4520.48s] English:** right now and so that's why i like this area i like this direction because of its ability to  
**Translation:** Vocabulary: routinely: 常规地

**[4526.46s] English:** surprise us to surprise us and an agi system would surprise us fundamentally yes but and to be precise  
**Translation:** 

**[4532.46s] English:** not just not just a random surprise but to find the surprising solution to a problem that's also  
**Translation:** 

**[4538.14s] English:** useful right now a lot of the self-play mechanisms have been used in the game context or at least in  
**Translation:** 

**[4546.38s] English:** the simulation context how much how much how far along the path to egi do you think will be done in  
**Translation:** Vocabulary: simulation: 模拟

**[4555.82s] English:** simulation  
**Translation:** 

**[4556.46s] English:** how much faith promise do you have in  
**Translation:** 

**[4560.00s] English:** simulation versus having to have a system that operates in the real world whether it's the real  
**Translation:** 

**[4567.04s] English:** world of digital real world data or real world like actual physical world of robotics i don't  
**Translation:** 

**[4573.28s] English:** think it's an either or i think simulation is a tool and it helps it has certain strengths and  
**Translation:** 

**[4578.64s] English:** certain weaknesses and we should use it yeah but okay i understand that that's um that's true  
**Translation:** 

**[4590.24s] English:** but one of the criticisms of self-play one of the criticisms of reinforcement learning is one of the  
**Translation:** 

**[4596.16s] English:** the its current power its current results while amazing have been demonstrated in a simulated  
**Translation:** Vocabulary: criticisms: 批评; reinforcement: 强化学习; simulated: 模拟的

**[4603.68s] English:** environments or very constrained physical environments do you think it's possible to  
**Translation:** 

**[4607.36s] English:** escape them escape the simulated environments and be able to learn in non-simulated environments  
**Translation:** Vocabulary: constrained: 限制性强; environments: 环境

**[4613.20s] English:** or do you think it's possible to also just simulate in the photorealistic and  
**Translation:** 

**[4619.60s] English:** physical  
**Translation:** Vocabulary: photorealistic: 照片级真实; simulate: 模拟

**[4620.00s] English:** realistic way the real world in a way that we can solve real problems with self-play  
**Translation:** 

**[4625.28s] English:** in simulation so i think that transfer from simulation to the real world is definitely  
**Translation:** 

**[4630.88s] English:** possible and has been exhibited many times in by many different groups it's been especially  
**Translation:** 

**[4636.64s] English:** successful in vision also open ai in the summer has demonstrated a robot hand which was trained  
**Translation:** Vocabulary: exhibited: 展出过

**[4643.04s] English:** entirely in simulation in a certain way that allowed for sim to real transfer to occur  
**Translation:** 

**[4648.16s] English:** is this stuff for the rubric yep that's right and  
**Translation:** Vocabulary: rubric: 评分标准

**[4652.64s] English:** i was unaware that was trained in simulation was training simulation entirely really so it wasn't  
**Translation:** 

**[4658.32s] English:** in the physical the hand wasn't trained no one hundred percent of the training was done in  
**Translation:** 

**[4663.52s] English:** simulation and the policy that was learned in simulation was trained to be very adaptive  
**Translation:** 

**[4668.88s] English:** so adaptive that when you transfer it it could very quickly adapt to the physical  
**Translation:** Vocabulary: adaptive: 适应性强; simulation: 模拟

**[4672.72s] English:** to the physical world so the kind of perturbations with the giraffe or whatever the heck it was  
**Translation:** 

**[4678.16s] English:** was those weren't, were those  
**Translation:** Vocabulary: perturbations: 干扰因素

**[4680.00s] English:** part of the simulation well the simulation was generally so the the simulation was trained to be  
**Translation:** 

**[4686.40s] English:** robust to many different things but not the kind of perturbations we've had in the video so  
**Translation:** 

**[4691.12s] English:** it's never been trained with a glove it's never been trained with a uh stuffed giraffe so in  
**Translation:** 

**[4697.44s] English:** theory these are novel perturbations correct it's not in theory in practice that those are novel  
**Translation:** 

**[4702.56s] English:** perturbations well that's okay that's a clean small scale but clean example of a transfer from  
**Translation:** 

**[4709.92s] English:** the simulated world to the physical world yeah and i will also say that i expect the transfer  
**Translation:** 

**[4714.80s] English:** capabilities of deep learning to increase in general and the better the transfer capabilities  
**Translation:** 

**[4719.76s] English:** are the more useful simulation will become because then you could take you could experience something  
**Translation:** 

**[4727.04s] English:** in simulation and then learn a moral of the story which you could then carry with you to the real  
**Translation:** 

**[4731.92s] English:** world  
**Translation:** 

**[4732.56s] English:** right as humans do all the time and they play computer games  
**Translation:** 

**[4736.88s] English:** so let me ask sort of a embodied question staying on agi for a sec  
**Translation:** Vocabulary: embodied: 体现

**[4744.56s] English:** do you think uh agis is that we need to have a body we need to have some of those human elements  
**Translation:** 

**[4749.44s] English:** of self-awareness consciousness sort of fear of mortality sort of self-preservation in the  
**Translation:** 

**[4756.72s] English:** physical space which comes with having a body i think having a body will be useful  
**Translation:** 

**[4762.56s] English:** i don't think it's necessary but i think it's very useful to have a body for sure because you can  
**Translation:** 

**[4767.04s] English:** learn a whole new you can learn things which cannot be learned without a body  
**Translation:** 

**[4772.64s] English:** but at the same time i think that you can if you don't have a body you could  
**Translation:** Vocabulary: cannot: 不能

**[4776.32s] English:** compensate for it and still succeed you think so yes well there is evidence for this for example  
**Translation:** 

**[4781.84s] English:** there are many people who were born deaf and blind and they were able to compensate for  
**Translation:** 

**[4786.96s] English:** the lack of modalities i'm thinking about helen kaler specifically  
**Translation:** 

**[4792.56s] English:** to physically interact with the world and if you're not able to i mean i actually was getting it maybe  
**Translation:** Vocabulary: modalities: 感觉方式

**[4800.00s] English:** Let me ask on the more particular, I'm not sure if it's connected to having a body or not,  
**Translation:** 

**[4805.34s] English:** but the idea of consciousness, and a more constrained version of that is self-awareness.  
**Translation:** Vocabulary: constrained: 限制

**[4811.22s] English:** Do you think an AGI system should have consciousness?  
**Translation:** 

**[4815.94s] English:** We can't define consciousness.  
**Translation:** 

**[4817.34s] English:** Whatever the heck you think consciousness is.  
**Translation:** 

**[4819.42s] English:** Yeah, hard question to answer, given how hard it is to define it.  
**Translation:** 

**[4824.38s] English:** Do you think it's useful to think about?  
**Translation:** 

**[4826.48s] English:** I mean, it's definitely interesting.  
**Translation:** 

**[4828.40s] English:** It's fascinating.  
**Translation:** 

**[4828.94s] English:** I think it's definitely possible that our systems will be conscious.  
**Translation:** 

**[4834.06s] English:** Do you think that's an emergent thing that just comes from...  
**Translation:** 

**[4836.36s] English:** Do you think consciousness could emerge from the representation that's stored within neural networks?  
**Translation:** Vocabulary: emergent: 涌现; neural: 神经

**[4840.86s] English:** So that it naturally just emerges when you become more and more...  
**Translation:** 

**[4845.00s] English:** You're able to represent more and more of the world?  
**Translation:** 

**[4847.04s] English:** Well, I'd make the following argument, which is humans are conscious.  
**Translation:** 

**[4853.42s] English:** And if you believe that artificial neural nets are sufficiently similar to the brain,  
**Translation:** Vocabulary: sufficiently: 足够地

**[4858.94s] English:** then there should at least exist artificial neural nets you should be conscious to.  
**Translation:** 

**[4864.06s] English:** You're leaning on that existence proof pretty heavily.  
**Translation:** 

**[4866.76s] English:** Okay.  
**Translation:** 

**[4870.32s] English:** That's the best answer I can give.  
**Translation:** 

**[4872.12s] English:** No, I know.  
**Translation:** 

**[4873.34s] English:** I know.  
**Translation:** 

**[4874.46s] English:** I know.  
**Translation:** 

**[4875.90s] English:** There's still an open question if there's not some magic in the brain that we're not...  
**Translation:** 

**[4880.74s] English:** I mean, I don't mean a non-materialistic magic,  
**Translation:** 

**[4884.06s] English:** but that the brain might be a lot more complicated and interesting than we give it credit for.  
**Translation:** 

**[4888.94s] English:** If that's the case, then it should show up.  
**Translation:** 

**[4892.64s] English:** And at some point, we will find out that we can't continue to make progress.  
**Translation:** 

**[4896.60s] English:** But I think it's unlikely.  
**Translation:** 

**[4898.46s] English:** So we talk about consciousness,  
**Translation:** 

**[4900.20s] English:** but let me talk about another poorly defined concept of intelligence.  
**Translation:** 

**[4904.48s] English:** Again, we've talked about reasoning.  
**Translation:** 

**[4906.80s] English:** We've talked about memory.  
**Translation:** 

**[4908.06s] English:** What do you think is a good test of intelligence for you?  
**Translation:** 

**[4911.54s] English:** Are you impressed by the test that Alan Turing formulated with the imitation game with natural language?  
**Translation:** 

**[4918.32s] English:** Is there...  
**Translation:** Vocabulary: imitation: 模仿; turing: 图灵

**[4918.94s] English:** Something...  
**Translation:** 

**[4920.00s] English:** in your mind that you will be deeply impressed by if a system was able to do i mean lots of things  
**Translation:** 

**[4927.84s] English:** there's certain there's certain frontier there is a certain frontier of capabilities today  
**Translation:** 

**[4932.32s] English:** yeah and there exists things outside of that frontier and i would be impressed by any such  
**Translation:** Vocabulary: frontier: 技术边界

**[4938.16s] English:** thing for example i would be impressed by a deep learning system which solves a very pedestrian you  
**Translation:** 

**[4946.08s] English:** know pedestrian task like machine translation or computer vision task or something which never  
**Translation:** 

**[4952.16s] English:** makes mistake a human wouldn't make under any circumstances i think that is something which  
**Translation:** 

**[4958.64s] English:** have not yet been demonstrated and i would find it very impressive yeah so right now they make  
**Translation:** 

**[4963.76s] English:** mistakes in diff they might be more accurate than human beings but they still they make a different  
**Translation:** 

**[4968.08s] English:** set of mistakes so my my i would guess that a lot of the skepticism that some people have about deep  
**Translation:** Vocabulary: skepticism: 怀疑态度

**[4974.88s] English:** learning is when they make a mistake they make a mistake they make a mistake they make a mistake  
**Translation:** 

**[4976.06s] English:** they look at their mistakes and they say well those mistakes they make no sense like if you  
**Translation:** 

**[4980.54s] English:** understood the concept you wouldn't make that mistake us and i think that changing that would be  
**Translation:** 

**[4987.34s] English:** would would that would inspire me that would be yes this is this this is this is progress  
**Translation:** 

**[4992.38s] English:** yeah that's that's a really nice way to put it but i also just don't like that human instinct to  
**Translation:** 

**[4999.58s] English:** criticize a model is not intelligent that's the same instinct as we do when we criticize  
**Translation:** Vocabulary: instinct: 本能

**[5004.30s] English:** any group of  
**Translation:** 

**[5006.06s] English:** creatures as the other because it's very possible that gpt2 is much smarter than human beings at  
**Translation:** 

**[5015.42s] English:** many things that's definitely true it has a lot more breadth of knowledge yes breadth of knowledge  
**Translation:** 

**[5020.86s] English:** and even and even perhaps depth on certain topics it's kind of hard to judge what depth means but  
**Translation:** 

**[5028.62s] English:** there's definitely a sense in which humans don't make mistakes that these models do yes the same is  
**Translation:** 

**[5035.74s] English:** applied to autonomous vehicles the same is probably going to continue being applied to a lot  
**Translation:** 

**[5040.00s] English:** of artificial intelligence systems we find this is the annoying this is the process of in the 21st  
**Translation:** 

**[5046.44s] English:** century the process of analyzing the progress of ai is the search for one case where the system  
**Translation:** 

**[5052.70s] English:** fails in a big way where humans would not and then many people writing articles about it and then  
**Translation:** 

**[5061.04s] English:** broadly as a as a the public generally gets convinced that the system is not intelligent  
**Translation:** 

**[5066.16s] English:** and we like pacify ourselves by thinking it's not intelligent because of this one  
**Translation:** 

**[5070.76s] English:** anecdotal case and this can seems to continue happening yeah i mean there is truth to that  
**Translation:** Vocabulary: anecdotal: 个例

**[5076.10s] English:** though there's people although i'm sure that plenty of people are also extremely impressed  
**Translation:** 

**[5079.14s] English:** by the system that exists today but i think this connects to the earlier point we discussed that  
**Translation:** 

**[5083.38s] English:** it's just confusing to judge progress in ai yeah and you know you have a new robot demonstrating  
**Translation:** 

**[5090.10s] English:** something how impressed should you be and and i think that people will start to be impressed  
**Translation:** 

**[5095.92s] English:** once they see it and i think that's the key to it and i think that's the key to it and i think  
**Translation:** 

**[5096.14s] English:** once ai starts to really move the needle on the gdp so you're one of the people that might be able  
**Translation:** 

**[5102.00s] English:** to create an ags system here not you but you and open ai if if you do create an ags system  
**Translation:** 

**[5108.76s] English:** and you get to spend sort of the evening with it him her what would you talk about do you think  
**Translation:** 

**[5116.52s] English:** the very first time the first time well the first time i would just  
**Translation:** 

**[5120.92s] English:** i would just ask all kinds of questions and try to make it to get it to make a mistake and  
**Translation:** 

**[5125.90s] English:** i would be amazed that it doesn't make mistakes and just keep keep asking broad okay what kind of  
**Translation:** 

**[5133.58s] English:** questions do you think would they be factual or would they be personal emotional psychological  
**Translation:** 

**[5140.86s] English:** what do you think all of the above would you ask for advice definitely i mean why why would  
**Translation:** 

**[5150.22s] English:** i limit myself talking to a system like this now again let me emphasize the fact  
**Translation:** 

**[5155.90s] English:** that you truly are one of the people that might be in the room where this happens  
**Translation:** 

**[5160.00s] English:** so let me ask a sort of a profound question about um i've just talked to a stalin historian  
**Translation:** Vocabulary: profound: 深奥; stalin: 斯大林

**[5168.12s] English:** i've been talking to a lot of people who are studying power abraham lincoln said nearly all  
**Translation:** 

**[5175.48s] English:** men can stand adversity but if you want to test a man's character give him power i would say the  
**Translation:** Vocabulary: adversity: 逆境

**[5182.54s] English:** power of the 21st century maybe the 22nd but hopefully the 21st would be the creation of an  
**Translation:** 

**[5189.42s] English:** agi system and the people who have control direct possession and control of the agi system  
**Translation:** 

**[5195.98s] English:** so what do you think after spending that evening having a discussion with the agi system  
**Translation:** 

**[5203.28s] English:** what do you think you would do well the ideal world i'd like to imagine  
**Translation:** 

**[5208.86s] English:** is one where humanity are like the board the board members of a company  
**Translation:** 

**[5218.54s] English:** where they  
**Translation:** 

**[5219.40s] English:** AGI is the CEO. So it would be, I would like, the picture which I would imagine is you have  
**Translation:** 

**[5229.00s] English:** some kind of different entities, different countries or cities, and the people that live  
**Translation:** 

**[5235.34s] English:** there vote for what the AGI that represents them should do, and an AGI that represents  
**Translation:** 

**[5240.00s] English:** them goes and does it. I think a picture like that, I find very appealing. And you could  
**Translation:** Vocabulary: appealing: 有吸引力的

**[5246.56s] English:** have multiple, you would have an AGI for a city, for a country, and it would be trying  
**Translation:** 

**[5252.36s] English:** to, in effect, take the democratic process to the next level.  
**Translation:** 

**[5255.86s] English:** And the board can almost fire the CEO.  
**Translation:** 

**[5258.70s] English:** Essentially. Press the reset button, say.  
**Translation:** 

**[5260.72s] English:** Press the reset button.  
**Translation:** 

**[5261.28s] English:** Re-randomize the parameters.  
**Translation:** 

**[5262.76s] English:** Well, let me sort of, that's actually, okay, that's a beautiful vision, I think, as long  
**Translation:** 

**[5269.44s] English:** as it's possible to press the reset button. Do you think it will always be possible to  
**Translation:** 

**[5275.08s] English:** press the reset button?  
**Translation:** 

**[5275.84s] English:** So I think that it's definitely really possible to build.  
**Translation:** 

**[5280.00s] English:** so you're talking so the question that i really understand from you is will we will humans or  
**Translation:** 

**[5289.02s] English:** humans people have control over the ai systems that they build yes and my answer is it's definitely  
**Translation:** 

**[5296.60s] English:** possible to build ai systems which will want to be controlled by their humans wow that's part of  
**Translation:** 

**[5302.74s] English:** their so it's not that just they can't help but be controlled but that's that's um the they exist  
**Translation:** 

**[5310.86s] English:** the one of the objectives of their existence is to be controlled in the same way that human parents  
**Translation:** 

**[5317.46s] English:** generally want to help their children they want their children to succeed it's not a burden for  
**Translation:** 

**[5325.28s] English:** them they are excited to help the children and to feed them and to dress them and to  
**Translation:** 

**[5330.40s] English:** take care of them  
**Translation:** 

**[5331.74s] English:** and i believe with high conviction that the same will be possible for an agi it will be possible  
**Translation:** 

**[5339.38s] English:** to program an agi to design it in such a way that it will have a similar deep drive that it will be  
**Translation:** 

**[5345.34s] English:** delighted to fulfill and the drive will be to help humans flourish but let me take a step back  
**Translation:** 

**[5352.64s] English:** to that moment where you create the agi system i think this is a really crucial moment  
**Translation:** Vocabulary: flourish: 繁荣发展

**[5356.94s] English:** and between that moment  
**Translation:** 

**[5361.28s] English:** and  
**Translation:** 

**[5361.74s] English:** the the democratic board members with the agi at the head there has to be a relinquishing of power  
**Translation:** 

**[5371.18s] English:** so george washington despite all the bad things he did one of the big things he did is he  
**Translation:** 

**[5377.92s] English:** relinquished power he first of all didn't want to be president and even when he became president  
**Translation:** 

**[5383.60s] English:** he gave he didn't keep just serving as most dictators do for indefinitely do you see yourself  
**Translation:** Vocabulary: dictators: 独裁者; indefinitely: 无期限; relinquished: 放弃

**[5391.74s] English:** being able to relinquish control over an agi system given how much power you can have over the world  
**Translation:** 

**[5398.82s] English:** at first finance  
**Translation:** Vocabulary: relinquish: 放弃控制

**[5400.00s] English:** just make a lot of money right and then control by having possession as a gi system i'd find it  
**Translation:** 

**[5407.96s] English:** trivial to do that i'd find it trivial to relinquish this this kind of i mean you know  
**Translation:** 

**[5412.92s] English:** the kind of scenario you are describing sounds terrifying to me that's all i would absolutely  
**Translation:** 

**[5419.66s] English:** not want to be in that position do you think you represent the majority or the minority  
**Translation:** Vocabulary: terrifying: 令人恐惧

**[5426.44s] English:** of people in the ai community well i mean it's an open question an important one  
**Translation:** 

**[5432.72s] English:** are most people good is another way to ask it so i don't know if most people are good but  
**Translation:** 

**[5439.76s] English:** i think that when it really counts people can be better than we think  
**Translation:** 

**[5445.86s] English:** that's beautifully put yeah are there specific mechanism you can think of of aligning ai gene  
**Translation:** Vocabulary: aligning: 对齐

**[5452.80s] English:** values to human values is that do you think about these problems  
**Translation:** 

**[5456.44s] English:** of continued alignment as we develop the ai systems yeah definitely in some sense  
**Translation:** Vocabulary: alignment: 对齐

**[5463.56s] English:** the kind of question which you are asking is so if you were to translate the question to today's  
**Translation:** 

**[5469.68s] English:** terms yes it would be a question about how to get an rl agent that's optimizing a value function  
**Translation:** 

**[5478.86s] English:** which itself is learned and if you look at humans humans are like that because the  
**Translation:** 

**[5483.78s] English:** reward function the value function of humans is not the value function of humans  
**Translation:** 

**[5486.44s] English:** is not external it is internal that's right and there are definite ideas of how to train  
**Translation:** 

**[5495.46s] English:** a value function basically an objective you know and as objective as possible perception  
**Translation:** 

**[5500.94s] English:** system that will be trained separately to recognize to internalize human judgments on  
**Translation:** 

**[5509.98s] English:** different situations and then that component would then be integrated as the value as the  
**Translation:** Vocabulary: internalize: 吸收

**[5515.44s] English:** base value function  
**Translation:** 

**[5516.44s] English:** for some more more capable rl system you could imagine a process  
**Translation:** 

**[5520.00s] English:** this i'm not saying this is the process i'm saying this is an example of the kind of thing you could  
**Translation:** 

**[5525.20s] English:** do so on that topic of the objective functions of human existence what do you what do you think  
**Translation:** 

**[5532.88s] English:** is the objective function that's implicit in human existence what's the meaning of life oh  
**Translation:** 

**[5539.04s] English:** i think the question is is wrong in some way i think that the question implies that there is an  
**Translation:** Vocabulary: implicit: 含蓄的

**[5554.26s] English:** there is an objective answer which is an external answer you know your meaning of life is x  
**Translation:** 

**[5557.80s] English:** i think what's going on is that we exist and that's amazing and we should try to make the  
**Translation:** 

**[5565.12s] English:** most of it and try to maximize our own value and enjoyment of  
**Translation:** 

**[5569.02s] English:** of our own value and enjoyment of our own value and enjoyment of our own value and enjoyment of  
**Translation:** 

**[5569.04s] English:** a very short time while we do exist it's it's funny because action does require an objective  
**Translation:** 

**[5575.62s] English:** function it's definitely there in some form but it's difficult to make it explicit and maybe  
**Translation:** Vocabulary: explicit: 明确

**[5581.38s] English:** impossible to make it explicit i guess is what you're getting at and that's an interesting  
**Translation:** 

**[5584.66s] English:** fact of an rl environment well but i was making a slightly different point is that humans want  
**Translation:** 

**[5592.44s] English:** things and their wants create the drives that cause them to you know our wants are our objective  
**Translation:** 

**[5599.02s] English:** functions our individual objective functions we can later decide that we want to change that what  
**Translation:** 

**[5604.52s] English:** we wanted before is no longer good and you want something else yes but they're so dynamic there's  
**Translation:** 

**[5609.12s] English:** got to be some underlying sort of freud there's things there's like sexual stuff there's people  
**Translation:** 

**[5614.28s] English:** think it's the fear of fear of death and there's also uh the desire for knowledge and you know all  
**Translation:** 

**[5620.68s] English:** these kinds of things uh procreation the sort of all the evolutionary arguments it seems to be  
**Translation:** Vocabulary: evolutionary: 进化论的; procreation: 繁衍

**[5626.92s] English:** there might be some kind of fundamental objective  
**Translation:** 

**[5629.00s] English:** function from from which everything else um emerges but it seems like that's very i mean i  
**Translation:** 

**[5636.12s] English:** think i think i think that probably is an evolutionary objective function which is to  
**Translation:** 

**[5639.24s] English:** survive and procreate  
**Translation:** Vocabulary: procreate: 繁衍

**[5640.00s] English:** and make sure you make your children succeed that would be my guess but it doesn't give an answer to  
**Translation:** 

**[5646.42s] English:** the question what's the meaning of life i think you can see how humans are part of this big process  
**Translation:** 

**[5652.54s] English:** this ancient process we are we are we exist on a small planet and that's it so given that we exist  
**Translation:** 

**[5662.98s] English:** try to make the most of it and try to enjoy more and suffer less as much as we can let me ask two  
**Translation:** 

**[5669.62s] English:** silly questions about life one do you have regrets moments that if you went back you would  
**Translation:** 

**[5677.96s] English:** do differently and two are there moments that you're especially proud of that made you truly  
**Translation:** 

**[5682.96s] English:** happy so i can answer that i can answer both questions of course there are there's a huge  
**Translation:** 

**[5689.28s] English:** number of choices and decisions that i've made that with the benefit of hindsight i wouldn't  
**Translation:** 

**[5694.46s] English:** have made them and i do experience some regret but you know i try to take solace  
**Translation:** 

**[5699.62s] English:** in the knowledge that at the time i did the best i could and in terms of things that i'm proud of  
**Translation:** Vocabulary: solace: 慰藉

**[5704.32s] English:** there are i'm very fortunate to have things i'm proud to have done things i'm proud of  
**Translation:** 

**[5707.46s] English:** and they made me happy from for some time but i don't think that that is the source of happiness  
**Translation:** 

**[5713.20s] English:** so your academic accomplishments all the papers you're one of the most cited people in the world  
**Translation:** 

**[5719.36s] English:** all the breakthroughs i mentioned in computer vision and language and so on  
**Translation:** Vocabulary: breakthroughs: 重大突破; cited: 被引用

**[5723.52s] English:** is what is the source of happiness and pride for you  
**Translation:** 

**[5729.62s] English:** i mean all those things are a source of pride for sure i'm very ungrateful for having done all those  
**Translation:** Vocabulary: ungrateful: 不知感恩

**[5734.18s] English:** things and it was very fun to do them but happiness comes but you know you can happiness well my  
**Translation:** 

**[5741.16s] English:** current view is that happiness comes from our to a lot to a very large degree from the way we look  
**Translation:** 

**[5746.38s] English:** at things you know you can have a simple meal and be quite happy as a result or you can talk to  
**Translation:** 

**[5751.96s] English:** someone and be happy as a result as well or conversely you can have a meal and be disappointed  
**Translation:** Vocabulary: conversely: 相反地

**[5758.04s] English:** that the meal wasn't a better meal  
**Translation:** 

**[5759.62s] English:** you  
**Translation:** 

**[5760.00s] English:** So I think a lot of happiness comes from that.  
**Translation:** 

**[5762.36s] English:** But I'm not sure.  
**Translation:** 

**[5762.96s] English:** I don't want to be too confident.  
**Translation:** 

**[5765.30s] English:** Being humble in the face of the uncertainty seems to be also part of this whole happiness thing.  
**Translation:** 

**[5771.94s] English:** Well, I don't think there's a better way to end it than meaning of life and discussions of happiness.  
**Translation:** 

**[5778.02s] English:** So, Ilya, thank you so much.  
**Translation:** 

**[5779.72s] English:** You've given me a few incredible ideas.  
**Translation:** 

**[5782.62s] English:** You've given the world many incredible ideas.  
**Translation:** 

**[5784.86s] English:** I really appreciate it.  
**Translation:** 

**[5785.74s] English:** And thanks for talking today.  
**Translation:** 

**[5787.48s] English:** Yeah, thanks for stopping by.  
**Translation:** 

**[5788.70s] English:** I really enjoyed it.  
**Translation:** 

**[5790.22s] English:** Thanks for listening to this conversation with Ilya Setskever.  
**Translation:** 

**[5792.98s] English:** And thank you to our presenting sponsor, Cash App.  
**Translation:** 

**[5796.30s] English:** Please consider supporting the podcast by downloading Cash App and using the code LEXPODCAST.  
**Translation:** 

**[5802.50s] English:** If you enjoy this podcast, subscribe on YouTube, review it with five stars on Apple Podcasts,  
**Translation:** 

**[5807.94s] English:** support it on Patreon, or simply connect with me on Twitter at Lex Friedman.  
**Translation:** 

**[5813.64s] English:** And now, let me leave you with some words from Alan Turing on machine learning.  
**Translation:** Vocabulary: friedman: 弗里德曼; turing: 图灵

**[5818.56s] English:** Instead of trying to produce a program to simulate the adult mind, why not rather try to produce one which simulates the child?  
**Translation:** 

**[5828.24s] English:** If this were then subjected to an appropriate course of education, one would obtain the adult brain.  
**Translation:** Vocabulary: simulate: 模仿; simulates: 模拟

**[5835.92s] English:** Thank you for listening and hope to see you next time.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
