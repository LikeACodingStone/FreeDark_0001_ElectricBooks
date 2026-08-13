# Podcast vocabulary notes
Source file: Lex Fridman - Jim Keller： Moore's Law, Microprocessors, and First Principles ｜ Lex Fridman Podcast #70.opus
Improved subtitle: punctuation and vocabulary regenerated from current config.

**[0.00s] English:** The following is a conversation with Jim Keller, legendary microprocessor engineer, who has worked at AMD, Apple, Tesla, and now Intel.  
**Translation:** 

**[9.76s] English:** He's known for his work on AMD K7, K8, K12, and Zen microarchitectures, as well as Apple A4 and A5 processors.  
**Translation:** Vocabulary: keller: 杰姆·凯勒; legendary: 传奇的; microarchitectures: 微架构; microprocessor: 微处理器; processors: 处理器

**[18.12s] English:** And co-author of the specification for the x86-64 instruction set and HyperTransport Interconnect.  
**Translation:** 

**[25.14s] English:** He's a brilliant first-principles engineer, an out-of-the-box thinker, and just an interesting and fun human being to talk to.  
**Translation:** Vocabulary: interconnect: 连接技术; specification: 规范; thinker: 思考者

**[33.44s] English:** This is the Artificial Intelligence Podcast.  
**Translation:** 

**[36.40s] English:** If you enjoy it, subscribe on YouTube, give it 5 stars on Apple Podcasts, follow on Spotify, and support it on Patreon.  
**Translation:** Vocabulary: patreon: 赞助; subscribe: 订阅

**[43.38s] English:** Or simply connect with me on Twitter at @LexFriedman (spelled F-R-I-D-M-A-N).  
**Translation:** 

**[49.10s] English:** I recently started doing ads at the end of the introduction.  
**Translation:** 

**[52.64s] English:** I'll do one or two minutes after introducing the episode.  
**Translation:** 

**[55.14s] English:** And never any ads in the middle that can break the flow of the conversation.  
**Translation:** 

**[59.04s] English:** I hope that works for you and doesn't hurt the listening experience.  
**Translation:** 

**[63.74s] English:** This show is presented by Cash App, the number-one finance app in the App Store.  
**Translation:** 

**[68.54s] English:** I personally use Cash App to send money to friends, but you can also use it to buy, sell, and deposit Bitcoin in just seconds.  
**Translation:** 

**[75.64s] English:** Cash App also has a new investing feature.  
**Translation:** Vocabulary: deposit: 存入

**[78.48s] English:** You can buy fractions of a stock, such as $1 worth, no matter what the stock price is.  
**Translation:** 

**[83.32s] English:** Brokerage services are provided by CashApp.  
**Translation:** Vocabulary: brokerage: 经纪服务; fractions: 股票份额

**[85.14s] English:** CashApp Investing, a subsidiary of Square and a member of SIPC.  
**Translation:** 

**[89.66s] English:** I'm excited to be working with CashApp to support one of my favorite organizations, called FIRST.  
**Translation:** Vocabulary: subsidiary: 子公司

**[95.34s] English:** Best known for their FIRST Robotics and LEGO competitions.  
**Translation:** 

**[98.48s] English:** They educate and inspire hundreds of thousands of students in over 110 countries.  
**Translation:** Vocabulary: robotics: 机器人技术

**[103.58s] English:** And they have a perfect rating on Charity Navigator, which means that donated money is used with maximum effectiveness.  
**Translation:** 

**[110.54s] English:** When you get CashApp from the App Store or Google Play and use code LEX.  
**Translation:** Vocabulary: donated: 捐款; effectiveness: 有效性; navigator: 导航器

**[115.14s] English:** Podcast, you'll get $10, and CashApp will also donate $10 to FIRST.  
**Translation:** 

**[120.00s] English:** Which, again, is an organization that I've personally seen inspire girls and boys to dream of engineering a better world.  
**Translation:** Vocabulary: donate: 捐赠

**[128.08s] English:** And now, here's my conversation with Jim Keller.  
**Translation:** 

**[132.18s] English:** What are the differences and similarities between the human brain and a computer, with the microprocessor at its core?  
**Translation:** Vocabulary: microprocessor: 微处理器

**[139.20s] English:** Let's start with the philosophical question, perhaps.  
**Translation:** 

**[142.28s] English:** Well, since people don't actually understand how human brains work, I think that's true.  
**Translation:** Vocabulary: philosophical: 哲学的

**[149.16s] English:** I think that's true.  
**Translation:** 

**[150.42s] English:** So, it's hard to compare them.  
**Translation:** 

**[152.82s] English:** Computers are; you know, there are really two things.  
**Translation:** 

**[157.28s] English:** There's memory and there's computation, right?  
**Translation:** Vocabulary: computation: 计算

**[160.42s] English:** And to date, almost all computer architectures use global memory, which is a thing, right?  
**Translation:** 

**[167.52s] English:** And then computation, where you pull data and do relatively simple operations on it, and write data back.  
**Translation:** 

**[174.02s] English:** So, it's decoupled in modern computers.  
**Translation:** 

**[177.84s] English:** And you think in the human brain.  
**Translation:** Vocabulary: decoupled: 解耦

**[179.50s] English:** I mean, everything is a mess that's combined together.  
**Translation:** 

**[182.54s] English:** Well, what people observe is that there are, you know, some number of layers of neurons, which have local and global connections.  
**Translation:** Vocabulary: neurons: 神经元

**[189.04s] English:** And information is stored in a distributed fashion.  
**Translation:** 

**[193.52s] English:** And people build things called neural networks in computers, where the information is distributed in some kind of fashion.  
**Translation:** Vocabulary: neural: 神经的

**[202.84s] English:** You know, there's a mathematics behind it.  
**Translation:** 

**[205.12s] English:** I don't know that the understanding of that is super deep.  
**Translation:** 

**[208.12s] English:** The computations we run on them are straightforward computations.  
**Translation:** 

**[213.40s] English:** I don't believe anybody has said that a neuron does this computation.  
**Translation:** Vocabulary: computations: 计算; straightforward: 简单明了

**[218.00s] English:** So, to date, it's hard to compare them, I would say.  
**Translation:** 

**[223.74s] English:** So, let's get into the basics before we zoom back out.  
**Translation:** 

**[228.74s] English:** How do you build a computer from scratch?  
**Translation:** 

**[230.94s] English:** What is a microprocessor?  
**Translation:** Vocabulary: microprocessor: 微处理器; scratch: 从头开始

**[232.76s] English:** What is a microarchitecture?  
**Translation:** 

**[234.12s] English:** What is an instruction set architecture?  
**Translation:** 

**[235.12s] English:** Maybe, even as far back.  
**Translation:** 

**[238.12s] English:** What is a transistor?  
**Translation:** Vocabulary: transistor: 晶体管

**[240.96s] English:** So, the special charm of computer engineering is that there's a relatively good understanding of  
**Translation:** 

**[248.48s] English:** Abstraction layers. So, down at the bottom, you have atoms, and atoms get put together in materials.  
**Translation:** Vocabulary: abstraction: 抽象层

**[254.24s] English:** Like silicon or doped silicon or metal, and we build transistors. On top of that, we build logic.  
**Translation:** 

**[261.92s] English:** Gates, right, and then functional units like an adder, a subtractor, and an instruction parsing unit.  
**Translation:** Vocabulary: doped: 掺杂硅; functional: 功能性的; parsing: 解析; silicon: 硅; subtractor: 减法器; transistors: 晶体管

**[268.64s] English:** And then we assemble those into, you know, processing elements. Modern computers are  
**Translation:** 

**[273.44s] English:** Built out of, you know, probably 10 to 20 locally sourced, you know, organic processing elements or coherent.  
**Translation:** Vocabulary: assemble: 组装; coherent: 协调的

**[281.60s] English:** Processing elements, and then that runs computer programs, right? So there are abstraction layers,  
**Translation:** 

**[287.84s] English:** And then, with software, you know, there's an instruction set you run, and then there's  
**Translation:** 

**[292.12s] English:** Assembly language, C, C++, Java, JavaScript—you know, there are abstraction layers, you know,  
**Translation:** 

**[298.64s] English:** Essentially, from the atom to the data center, right? So, when you build a computer,...  
**Translation:** 

**[306.20s] English:** You know, first there's a target: what's it for? Like, how fast does it have to be? Which,  
**Translation:** 

**[310.28s] English:** You know, today there are a whole bunch of metrics about what that is, and then in an organization,...  
**Translation:** Vocabulary: metrics: 衡量标准

**[315.72s] English:** Of, you know, a thousand people who build a computer, there are lots of different disciplines.  
**Translation:** 

**[322.12s] English:** That you have to operate on. Does that make sense? And so...  
**Translation:** Vocabulary: disciplines: 专业领域

**[325.80s] English:** So, there are a bunch of levels of abstraction.  
**Translation:** 

**[328.64s] English:** In an organization like Intel, and in your own vision, there's a lot of brilliance that comes  
**Translation:** Vocabulary: abstraction: 抽象; brilliance: brilliance

**[337.32s] English:** In every one of those layers, some of it is science, some of it is engineering, some of it is  
**Translation:** 

**[342.20s] English:** Art: What's the most important, if you could pick a favorite, what's the most important layer?  
**Translation:** 

**[349.56s] English:** On these layers of abstraction? Where does the magic enter this hierarchy?  
**Translation:** 

**[353.72s] English:** I don't really care. That's the fun, you know.  
**Translation:** Vocabulary: hierarchy: 等级制度

**[358.64s] English:** I'm somewhat agnostic.  
**Translation:** 

**[360.00s] English:** To that, so I would say that for relatively long periods of time, instruction sets are stable.  
**Translation:** Vocabulary: agnostic: 无所偏袒的

**[366.98s] English:** So, the x86 instruction set, the ARM instruction set—what's an instruction set? So, it says how do  
**Translation:** 

**[374.32s] English:** You encode the basic operations: load, store, multiply, add, subtract, and conditional branch.  
**Translation:** Vocabulary: conditional: 条件; encode: 编码; multiply: 乘法; subtract: 减法

**[379.28s] English:** You know, there aren't that many interesting instructions like if you look at a program.  
**Translation:** 

**[384.68s] English:** And it runs; you know, 90% of the execution is on 25 op codes, you know, 25 instructions, and those...  
**Translation:** Vocabulary: execution: 运行过程

**[392.02s] English:** Are they stable? What does "stable" mean? Intel architecture has been around for 25 years, and it works.  
**Translation:** 

**[398.58s] English:** It works, and that's because the basics are defined a long time ago; right now, the way  
**Translation:** 

**[406.78s] English:** An old computer ran by fetching instructions and executing them in order to do the load.  
**Translation:** 

**[414.38s] English:** Add.  
**Translation:** Vocabulary: executing: 执行; fetching: 获取

**[414.68s] English:** The way a modern computer works is that you fetch large numbers of instructions, say 500.  
**Translation:** 

**[422.82s] English:** And then you find the dependency graph between the instructions, and then you execute.  
**Translation:** Vocabulary: execute: 执行

**[430.34s] English:** Independent units; those little micrographs. So, a modern computer—like people like to say—computers.  
**Translation:** 

**[438.16s] English:** Should be simple and clean, but it turns out the market for simple, complete, clean, slow computers.  
**Translation:** Vocabulary: micrographs: 显微图像

**[444.02s] English:** Is zero.  
**Translation:** 

**[444.68s] English:** Right, we don't sell any simple, clean computers now. You can, however, build one that can be clean.  
**Translation:** 

**[453.22s] English:** But the computer people want to buy, whether for a phone or a data center, fetches a large number.  
**Translation:** 

**[461.54s] English:** Of instructions, the system computes the dependency graph and then executes it in a way that gets the right  
**Translation:** Vocabulary: computes: 计算; executes: 执行; fetches: 获取

**[468.04s] English:** Answers and optimize that graph somehow, yeah? They run deeply out of order and then...  
**Translation:** 

**[474.02s] English:** There are semantics around how memory ordering works, and other things, so the computer sorts of  
**Translation:** Vocabulary: optimize: 优化; semantics: 语义

**[480.00s] English:** Has a bunch of bookkeeping tables that say what order these operations should be performed in.  
**Translation:** 

**[483.96s] English:** Finish in or appear to finish in? But to go fast, you have to fetch a lot of instructions.  
**Translation:** Vocabulary: bookkeeping: 会计记录

**[490.42s] English:** And find all the parallelism. Now, there's a second kind of computer, which we call GPUs today.  
**Translation:** 

**[497.54s] English:** And I call it the difference. There's found parallelism, like you have a program with a  
**Translation:** 

**[502.08s] English:** A lot of dependent instructions. You fetch a bunch, and then you go figure out the dependency graph.  
**Translation:** 

**[506.98s] English:** And you issue instructions out of order. That's because you have one serial narrative to execute.  
**Translation:** Vocabulary: execute: 执行; serial: 串行

**[512.62s] English:** Which, in fact, can be done out of order.  
**Translation:** 

**[515.78s] English:** Did you call it a narrative?  
**Translation:** 

**[517.02s] English:** Yeah.  
**Translation:** 

**[517.80s] English:** Wow.  
**Translation:** 

**[518.54s] English:** So, yeah. Humans think of serial narrative, like reading a book, where there's a sentence after that continues the story.  
**Translation:** 

**[524.26s] English:** Sentence after sentence, and there are paragraphs. Now, you could diagram that. Imagine you diagrammed it.  
**Translation:** Vocabulary: diagrammed: 绘图表示

**[530.40s] English:** It should be proper, and you said that which sentences could be read in any order, without changing the meaning.  
**Translation:** 

**[536.86s] English:** Names?  
**Translation:** 

**[536.98s] English:** Meaning, right?  
**Translation:** 

**[539.68s] English:** That's a fascinating question to ask of a book. Yeah.  
**Translation:** 

**[542.52s] English:** Yeah. You could do that, right? So, some paragraphs could be reordered, and some sentences...  
**Translation:** 

**[546.84s] English:** Can be reordered. You could say, "He is tall and smart and X," right? And it doesn't matter the  
**Translation:** 

**[557.06s] English:** Order of tall and smart. But if you say, "the tall man is wearing a red shirt," what colors?  
**Translation:** 

**[563.46s] English:** You know, like you can create dependencies.  
**Translation:** 

**[566.98s] English:** Right? Right. And so, GPUs, on the other hand, run simple programs on pixels. But you're given:  
**Translation:** 

**[576.02s] English:** Million of them. And the first order: the screen you're looking at doesn't care which order you do.  
**Translation:** Vocabulary: pixels: 像素

**[581.32s] English:** It's called that given parallelism. Simple narratives around the large numbers of things.  
**Translation:** 

**[587.86s] English:** Where you can just say it's parallel because you told me it was.  
**Translation:** Vocabulary: narratives: 故事; parallel: 平行

**[591.98s] English:** So, we found parallelism in the narrative, where the storylines run concurrently.  
**Translation:** 

**[596.06s] English:** Sequential, but you discover like little pockets.  
**Translation:** Vocabulary: concurrently: 同时; sequential: 顺序; storylines: 情节

**[600.00s] English:** Of parallelism versus, turns out there are large pockets of parallelism. So, how hard?  
**Translation:** 

**[604.98s] English:** Is it as simple as just transistor count? Right, so once you crack...  
**Translation:** Vocabulary: transistor: 晶体管

**[609.54s] English:** The problem, you say: "Here's how you fetch ten instructions at a time. Here's how.  
**Translation:** 

**[613.80s] English:** You calculated the dependencies between them. Here's how you describe the:  
**Translation:** 

**[617.46s] English:** Dependencies: Here's you know, these are pieces, right? So I know once you describe...  
**Translation:** 

**[623.82s] English:** The dependencies, then it's just a graph. Sort of, it's an algorithm that finds...  
**Translation:** 

**[629.40s] English:** Well, what is that? I'm sure there's a graph theory/theoretical answer here.  
**Translation:** 

**[634.56s] English:** That's solvable in general programs, modern programs that human beings write.  
**Translation:** Vocabulary: solvable: 可解的

**[641.76s] English:** How much parallelism is there in the next? What does "10x" mean? What you  
**Translation:** 

**[647.72s] English:** Executed in order, versus you would get what's called cycles per instruction,  
**Translation:** 

**[653.94s] English:** It would be about, you know, three instructions: three cycles per.  
**Translation:** 

**[658.86s] English:** Instruction:  
**Translation:** 

**[659.40s] English:** Because of the latency of the operations and stuff, and in a modern  
**Translation:** 

**[663.80s] English:** Computer, excuse it, but it's about 0.2 to 0.25 cycles per instruction.  
**Translation:** Vocabulary: latency: 延迟

**[669.84s] English:** Today, find 10x, and there are two things: one is the found parallelism in the  
**Translation:** 

**[675.56s] English:** Narrative, right, and the other is predictability of the narrative, right?  
**Translation:** 

**[681.86s] English:** Certain operations, they do a bunch of calculations, and if the result is greater than one, do  
**Translation:** 

**[687.16s] English:** This, else, do that.  
**Translation:** 

**[689.40s] English:** That decision is predicted with a high ninety percent accuracy in modern computers.  
**Translation:** 

**[694.58s] English:** Accuracy, so branches happen a lot. So, imagine you have to make a decision.  
**Translation:** 

**[700.48s] English:** Make every six instructions, which is about the average, right? But you want to  
**Translation:** 

**[704.20s] English:** Fetch 500 instructions, figure out the graph, and execute them all in parallel.  
**Translation:** Vocabulary: execute: 执行; parallel: 并行

**[708.70s] English:** Means you have six hundred instructions, and it's every six that you have to fetch it.  
**Translation:** 

**[716.24s] English:** Have to predict ninety-nine out of a hundred branches correctly.  
**Translation:** 

**[719.40s] English:** When it's going to be a complete,  
**Translation:** 

**[720.00s] English:** For that window to be effective,  
**Translation:** 

**[722.32s] English:** Okay, so parallelism: You can't parallelize branches, or you can.  
**Translation:** 

**[728.34s] English:** What does "predict a branch" mean?  
**Translation:** 

**[730.82s] English:** So, imagine you do a computation over and over.  
**Translation:** 

**[733.60s] English:** You're in a loop.  
**Translation:** Vocabulary: computation: 计算

**[734.96s] English:** So, while n is greater than 1, do.  
**Translation:** 

**[738.00s] English:** You.  
**Translation:** 

**[739.20s] English:** And you go through that loop a million times.  
**Translation:** 

**[739.38s] English:** You.  
**Translation:** 

**[741.24s] English:** So, every time you look at the branch, you say, "It's probably still greater than 1.  
**Translation:** 

**[741.36s] English:** You.  
**Translation:** 

**[743.42s] English:** Do  
**Translation:** 

**[744.12s] English:** You.  
**Translation:** 

**[744.68s] English:** Do  
**Translation:** 

**[745.28s] English:** You.  
**Translation:** 

**[745.64s] English:** And you're saying you could do that accurately?  
**Translation:** 

**[746.10s] English:** Do  
**Translation:** 

**[746.68s] English:** Do  
**Translation:** 

**[747.42s] English:** Do  
**Translation:** 

**[747.68s] English:** Very accurately.  
**Translation:** 

**[748.00s] English:** Do  
**Translation:** 

**[748.52s] English:** My mind is blown.  
**Translation:** 

**[748.64s] English:** Do  
**Translation:** 

**[749.28s] English:** Do  
**Translation:** 

**[749.36s] English:** Do  
**Translation:** 

**[750.30s] English:** How in the world do you do that?  
**Translation:** 

**[751.48s] English:** Wait a minute.  
**Translation:** 

**[752.50s] English:** Well, you want to know?  
**Translation:** 

**[753.58s] English:** This is really sad.  
**Translation:** 

**[755.42s] English:** 20 years ago, you simply recorded which way the branch went last time and predicted the same thing.  
**Translation:** 

**[762.48s] English:** Right.  
**Translation:** 

**[763.30s] English:** Okay.  
**Translation:** 

**[764.28s] English:** What's the accuracy of that?  
**Translation:** 

**[766.52s] English:** 85%.  
**Translation:** 

**[766.96s] English:** So then somebody said, "Hey, let's keep a couple of bits and have a little counter.  
**Translation:** 

**[773.14s] English:** So, when it predicts one way, we count up and then pin.  
**Translation:** 

**[776.90s] English:** So, say you have a 3-bit counter.  
**Translation:** 

**[778.08s] English:** So, you count.  
**Translation:** 

**[778.52s] English:** You count up, and then you count down.  
**Translation:** 

**[780.80s] English:** And if it's known, you can use the top bit as the sign bit.  
**Translation:** 

**[783.28s] English:** So, you have a 2-bit number.  
**Translation:** 

**[785.08s] English:** So, if it's greater than 1, you predict "taken.  
**Translation:** 

**[787.54s] English:** And if it's less than 1, you predict it won't be taken.  
**Translation:** 

**[790.40s] English:** Right.  
**Translation:** 

**[791.18s] English:** Or less than 0, or whatever the thing is.  
**Translation:** 

**[793.86s] English:** And that got us to 92%.  
**Translation:** 

**[795.90s] English:** Oh.  
**Translation:** 

**[797.26s] English:** Okay.  
**Translation:** 

**[797.66s] English:** No, it gets better.  
**Translation:** 

**[799.42s] English:** This branch depends on how you got there.  
**Translation:** 

**[802.54s] English:** So, if you came down the code one way, you're talking about Bob and Jane.  
**Translation:** 

**[807.80s] English:** Right.  
**Translation:** 

**[808.28s] English:** And then he asked, "Does Bob like Jane?  
**Translation:** 

**[810.44s] English:** It went one way.  
**Translation:** 

**[811.14s] English:** But if you're talking about Bob and Jill, do Bob and Jane like each other?  
**Translation:** 

**[813.86s] English:** You go a different way.  
**Translation:** 

**[815.56s] English:** Right.  
**Translation:** 

**[815.78s] English:** So, that's called history.  
**Translation:** 

**[816.92s] English:** So, you take the history and a counter.  
**Translation:** 

**[819.72s] English:** That's cool.  
**Translation:** 

**[821.16s] English:** But that's not how anything works today.  
**Translation:** 

**[823.30s] English:** They use something that looks a little like a neural network.  
**Translation:** 

**[827.74s] English:** So, modern systems involve taking all the execution flows.  
**Translation:** Vocabulary: execution: 执行; neural: 神经

**[831.98s] English:** And then you do basically deep pattern recognition of how the program is executing.  
**Translation:** 

**[838.28s] English:** And that's what we're talking about.  
**Translation:** Vocabulary: executing: 运行

**[840.00s] English:** And you do that in multiple different ways.  
**Translation:** 

**[843.44s] English:** And you have something that chooses what the best result is.  
**Translation:** 

**[847.38s] English:** There's a little supercomputer inside the computer.  
**Translation:** 

**[850.34s] English:** That's trying to predict the branching.  
**Translation:** Vocabulary: supercomputer: 超级计算机

**[851.58s] English:** That calculates which way branches go.  
**Translation:** 

**[854.24s] English:** So, the effective window that it's worth finding grass in gets bigger.  
**Translation:** Vocabulary: calculates: 计算

**[859.24s] English:** Why was that going to make me sad?  
**Translation:** 

**[861.52s] English:** Because that's amazing.  
**Translation:** 

**[862.84s] English:** It's amazingly complicated.  
**Translation:** 

**[864.40s] English:** Oh, well.  
**Translation:** 

**[865.22s] English:** Well, here's the funny thing.  
**Translation:** 

**[866.84s] English:** So, to get to 85%, it took 1,000 bits.  
**Translation:** 

**[872.54s] English:** To get to 99% takes tens of megabits.  
**Translation:** 

**[878.90s] English:** So, this is one of those.  
**Translation:** 

**[881.06s] English:** To get the result, you know, to get from a window of, say, 50 instructions to 500.  
**Translation:** 

**[887.54s] English:** It took three to four orders of magnitude more bits.  
**Translation:** 

**[892.36s] English:** Now, if you get the prediction of a branch wrong, what happens then?  
**Translation:** 

**[896.16s] English:** It flushes the pipe.  
**Translation:** Vocabulary: flushes: 清空管道

**[897.28s] English:** It flushes the pipe.  
**Translation:** 

**[898.04s] English:** So, it's just the performance cost.  
**Translation:** 

**[899.58s] English:** But it gets even better.  
**Translation:** 

**[900.78s] English:** Yeah.  
**Translation:** 

**[901.20s] English:** So, we're starting to look at stuff that says,  
**Translation:** 

**[903.48s] English:** So, they executed down this path.  
**Translation:** 

**[906.38s] English:** And then you had two ways to go.  
**Translation:** 

**[909.28s] English:** But far, far away, there's something that doesn't matter which path you took.  
**Translation:** 

**[914.52s] English:** So, you took the wrong path.  
**Translation:** 

**[917.70s] English:** You executed a bunch of stuff.  
**Translation:** 

**[920.24s] English:** Then you had the misprediction.  
**Translation:** 

**[921.74s] English:** You backed it up.  
**Translation:** Vocabulary: misprediction: 错误预测

**[922.46s] English:** But you remembered all the results you had already calculated.  
**Translation:** 

**[925.32s] English:** Some of those are just fine.  
**Translation:** 

**[927.36s] English:** Like, if you read a book and you misunderstand a paragraph,  
**Translation:** 

**[930.26s] English:** Your understanding of the next paragraph is sometimes invariant to that understanding.  
**Translation:** Vocabulary: invariant: 不变的; misunderstand: 误解

**[935.70s] English:** Sometimes it depends on that.  
**Translation:** 

**[938.32s] English:** And you can kind of anticipate that invariance.  
**Translation:** Vocabulary: anticipate: 预知; invariance: 不变性

**[943.24s] English:** Yeah, well, you can keep track of whether the data changed.  
**Translation:** 

**[947.42s] English:** And so, when you come back to a piece of code,  
**Translation:** 

**[949.26s] English:** Should you calculate it again, or do the same thing?  
**Translation:** 

**[951.78s] English:** Okay, how much of this is art, and how much of it is science?  
**Translation:** 

**[955.28s] English:** Because it sounds...  
**Translation:** 

**[956.84s] English:** Pretty complicated.  
**Translation:** 

**[959.02s] English:** Well, how do you describe it?  
**Translation:** 

**[960.00s] English:** Situation: So, imagine you come to a point in the road where you have to make a decision, yeah? Right?  
**Translation:** 

**[964.72s] English:** And you have a bunch of knowledge about which way to go, maybe you have a map. So you want to go the  
**Translation:** 

**[970.00s] English:** The shortest way, or do you want to go the fastest way, or you want to take the nicest road? So it's  
**Translation:** 

**[975.62s] English:** There's some set of data, right? So, imagine you're doing something complicated, like building a  
**Translation:** 

**[980.20s] English:** Computer, and there are hundreds of decision points, all with hundreds of possible ways to go, and the  
**Translation:** 

**[988.04s] English:** Ways you pick, interact, and do things in a complicated way, right? And then you have to pick the right spot, right?  
**Translation:** 

**[996.00s] English:** That order, signs: I don't know; you avoided the question. You just described Robert Frost.  
**Translation:** 

**[1000.88s] English:** Poem "The Road Not Taken" by Robert Frost: I described the problem we face as computer designers, that's what.  
**Translation:** 

**[1009.30s] English:** It's all poetry, okay? Great, yeah. I don't know how to describe that because some people are just very good.  
**Translation:** Vocabulary: designers: 设计师

**[1016.34s] English:** At making those intuitive leaps.  
**Translation:** 

**[1017.84s] English:** It seems like the combinations of things some people are less good at, but they're really.  
**Translation:** Vocabulary: intuitive: 直觉的

**[1022.88s] English:** Good at evaluating the alternatives, right? And everybody has a different way to do it.  
**Translation:** 

**[1028.58s] English:** And some people can't make those leaps, but they're really good at analyzing it.  
**Translation:** 

**[1033.58s] English:** So, when you see computers are designed by teams of people who have very different skill sets,...  
**Translation:** 

**[1038.14s] English:** And a good team has lots of different kinds of people. I suspect you would describe some of them.  
**Translation:** 

**[1046.22s] English:** As artistic,  
**Translation:** 

**[1047.84s] English:** Right, but not very many, unfortunately. Or fortunately, well, you know, computer design.  
**Translation:** 

**[1056.04s] English:** It's 99 percent perspiration, and the one percent inspiration is really important.  
**Translation:** 

**[1063.00s] English:** But you still need the 99%. Yeah, you got to do a lot of work, and then there are interesting things.  
**Translation:** Vocabulary: perspiration: 汗水

**[1069.98s] English:** Things to do at every level that stack, so at the end of the day, if you run the same program:  
**Translation:** 

**[1076.94s] English:** Multiple times, you're going to have to do a lot of work, and then you're going to have to do a lot of  
**Translation:** 

**[1077.84s] English:** Stuff, so that's part of the difference between where the  
**Translation:** 

**[1080.00s] English:** Same result? Is there some room for fuzziness there? That's a math problem, so if you run a  
**Translation:** Vocabulary: fuzziness: 模糊性

**[1087.70s] English:** Correct C program: The definition is, every time you run it, you get the same answer, yeah.  
**Translation:** 

**[1092.86s] English:** Well, that's a math statement, but that's a language-definitional statement.  
**Translation:** 

**[1096.84s] English:** So, yes, for years when people first started doing 3D acceleration of graphics.  
**Translation:** 

**[1102.52s] English:** You could run the same scene multiple times and get different answers, right? And then some.  
**Translation:** 

**[1111.20s] English:** People thought that was okay, and some people thought it was a bad idea, and then when the  
**Translation:** 

**[1115.80s] English:** HBC World used GPUs for calculations; they thought it was a really bad idea, okay? Now,  
**Translation:** 

**[1122.40s] English:** In modern AI stuff, people are looking at networks where the precision of the data is low enough.  
**Translation:** 

**[1130.48s] English:** That the data is somewhat noisy.  
**Translation:** 

**[1132.52s] English:** And the observation is that the input data is unbelievably noisy, so why should the calculation?  
**Translation:** 

**[1138.64s] English:** Be not noisy, and people have experimented with algorithms that can get faster answers by.  
**Translation:** Vocabulary: experimented: 尝试; unbelievably: 难以置信地

**[1144.54s] English:** Being noisy, like as the network starts to converge, if you look at the computation graph, it starts out  
**Translation:** 

**[1150.02s] English:** Really wide, and then it gets narrower. And you can say, "Is that last little bit that important?  
**Translation:** Vocabulary: computation: 计算; converge: 收敛; narrower: 更窄

**[1154.54s] English:** Should I start the graph on the next wrap/rev before we whittle it all the way down to the?  
**Translation:** 

**[1159.74s] English:** Answer correctly, so you can create algorithms.  
**Translation:** Vocabulary: whittle: 削细

**[1162.36s] English:** That are really noisy, and the observation is that the input data is unbelievably noisy. So, why should  
**Translation:** 

**[1162.50s] English:** I'll start the graph on the next wrap-around revolution before we whittle it all the way down to the answer.  
**Translation:** 

**[1163.50s] English:** Right, so you can create algorithms that are noisy now, if you're developing something and every time  
**Translation:** 

**[1165.90s] English:** You run it, you get a different answer. It's really annoying, and so most people think—even today.  
**Translation:** 

**[1173.82s] English:** Every time you run the program, you get the same answer. No, I know, but the question is, that's the  
**Translation:** 

**[1178.86s] English:** Formal definition of a programming language: there is a definition of languages that don't get the  
**Translation:** 

**[1185.02s] English:** Same answer, but people who use those always want something because you get a bad answer.  
**Translation:** 

**[1190.70s] English:** Then you're wondering if it's because of the programming language or is it because of the  
**Translation:** 

**[1192.34s] English:** Right, of something in the algorithm, or because of this, and so everybody wants a little switch.  
**Translation:** 

**[1196.72s] English:** That says, "No matter what, yeah, do it deterministically.  
**Translation:** Vocabulary: algorithm: 算法; deterministically: 确定地

**[1200.00s] English:** And it's really weird because almost everything going into modern calculations is noisy.  
**Translation:** 

**[1205.36s] English:** So, why do the answers have to be so clear?  
**Translation:** 

**[1208.00s] English:** Right, so where do you stand?  
**Translation:** 

**[1209.58s] English:** I design computers for people who run programs.  
**Translation:** 

**[1212.52s] English:** So, if somebody says they want a deterministic answer, like most people do.  
**Translation:** 

**[1218.36s] English:** Can you deliver a deterministic answer? I guess that's the question.  
**Translation:** Vocabulary: deterministic: 决定论的

**[1222.20s] English:** Yeah, hopefully, sure.  
**Translation:** 

**[1222.92s] English:** What people don't realize is that you get a deterministic answer, even though the execution flow is very undeterministic.  
**Translation:** Vocabulary: execution: 执行; undeterministic: 不可预测的

**[1230.80s] English:** So, you run this program a hundred times, and it never runs the same way twice, ever.  
**Translation:** 

**[1236.04s] English:** And the answer arrives at the same answer.  
**Translation:** 

**[1237.92s] English:** But it gets the same answer every time.  
**Translation:** 

**[1239.20s] English:** It's just amazing.  
**Translation:** 

**[1241.28s] English:** Okay, you've achieved in the eyes of many people a legend status as a chip architect.  
**Translation:** 

**[1252.60s] English:** Yes.  
**Translation:** 

**[1252.92s] English:** What design creation are you most proud of?  
**Translation:** 

**[1256.16s] English:** Perhaps because it was challenging, because of its impact, or because of the set of brilliant ideas involved in bringing it to life.  
**Translation:** 

**[1266.78s] English:** I find that description odd.  
**Translation:** 

**[1270.12s] English:** And I have two small children, and I promise you, they think it's hilarious.  
**Translation:** Vocabulary: hilarious: 非常好笑

**[1275.96s] English:** This question.  
**Translation:** 

**[1276.70s] English:** Yeah.  
**Translation:** 

**[1277.14s] English:** I do it for them.  
**Translation:** 

**[1278.26s] English:** So, I'm really interested in building computers.  
**Translation:** 

**[1282.92s] English:** And I've worked with really, really smart people.  
**Translation:** 

**[1287.14s] English:** I'm not unbelievably smart.  
**Translation:** Vocabulary: unbelievably: 难以置信地

**[1289.68s] English:** I'm fascinated by how they go together—both as a thing to do and as an endeavor that people pursue.  
**Translation:** 

**[1298.16s] English:** How do people and computers go together?  
**Translation:** Vocabulary: endeavor: 努力; fascinated: 着迷

**[1300.00s] English:** Yeah.  
**Translation:** 

**[1300.52s] English:** Like how people think and build a computer.  
**Translation:** 

**[1303.80s] English:** And I find that sometimes the best computer architects aren't that interested in people, or the best people managers aren't that good at designing computers.  
**Translation:** 

**[1312.92s] English:** So, the whole stack of human beings is fascinating—managers, individual engineers.  
**Translation:** 

**[1318.80s] English:** Yeah, yeah.  
**Translation:** 

**[1320.00s] English:** Yeah, I said I realized after a lot of years of building computers—where you sort of build them out of transistors, logic gates, functional units, and computational elements—that you could think of people the same way.  
**Translation:** Vocabulary: computational: 计算; functional: 功能; transistors: 晶体管

**[1330.76s] English:** So, people are functional units.  
**Translation:** 

**[1332.38s] English:** And then you could think of organizational design as a computer architectural problem.  
**Translation:** Vocabulary: architectural: 架构的

**[1336.52s] English:** And then it was like, "Oh, that's super cool" because the people are all different, just like the computational elements are all different.  
**Translation:** 

**[1343.62s] English:** And they like to do different things.  
**Translation:** 

**[1345.34s] English:** And so, I had a lot of fun reframing how I think about organizations.  
**Translation:** 

**[1351.44s] English:** Just like with computers, we were saying that execution paths can have a lot of different paths that end up at the same good destination.  
**Translation:** Vocabulary: execution: 执行路径; reframing: 重新思考

**[1361.58s] English:** So, what have you learned about the human abstraction from individual functional units to the broader organizational structure?  
**Translation:** 

**[1371.82s] English:** What does it take to create something special?  
**Translation:** Vocabulary: abstraction: 抽象

**[1374.74s] English:** Well.  
**Translation:** 

**[1376.34s] English:** Most people don't think simply enough.  
**Translation:** 

**[1379.88s] English:** All right.  
**Translation:** 

**[1380.60s] English:** So, do you know the difference between a recipe and an understanding?  
**Translation:** Vocabulary: recipe: 烹饪方法

**[1385.92s] English:** There's probably a philosophical description of this.  
**Translation:** 

**[1389.12s] English:** So, imagine you're going to make a loaf of bread.  
**Translation:** Vocabulary: philosophical: 哲学上的

**[1391.00s] English:** The recipe says: Get some flour, add some water, add some yeast, mix it up, let it rise, put it in a pan, and put it in the oven.  
**Translation:** 

**[1399.14s] English:** It's a recipe.  
**Translation:** Vocabulary: yeast: 发酵粉

**[1401.16s] English:** Understanding Bread.  
**Translation:** 

**[1402.84s] English:** You can understand biology and supply chain.  
**Translation:** 

**[1405.68s] English:** You know, grain grinders, yeast, physics, and thermodynamics.  
**Translation:** 

**[1413.80s] English:** Like, there are so many levels of understanding there.  
**Translation:** Vocabulary: grinders: 磨粉机; thermodynamics: 热力学

**[1417.22s] English:** And then, when people build and design things, they frequently are executing some stack of recipes.  
**Translation:** 

**[1424.38s] English:** Right.  
**Translation:** Vocabulary: executing: 执行; recipes: 食谱

**[1425.18s] English:** And the problem with that is that the recipes all have limited scope.  
**Translation:** 

**[1428.88s] English:** Like, if you have a really good recipe book for making bread, it won't tell you anything about how to make an omelet.  
**Translation:** 

**[1434.34s] English:** Right.  
**Translation:** 

**[1434.82s] English:** But.  
**Translation:** 

**[1435.08s] English:** If you have a deep understanding of cooking,  
**Translation:** 

**[1438.32s] English:** Right.  
**Translation:** 

**[1439.16s] English:** Then, bread.  
**Translation:** 

**[1439.92s] English:** Bread.  
**Translation:** 

**[1440.00s] English:** Omelets, you know, sandwich—you know, there's a different way of viewing everything.  
**Translation:** 

**[1446.54s] English:** And most people, when you get to be an expert at something, you know you're hoping to  
**Translation:** 

**[1454.64s] English:** Achieve a deeper understanding, not just a large set of recipes to go execute; it's interesting to.  
**Translation:** 

**[1461.86s] English:** Walk groups of people because executing recipes is unbelievably efficient if that's what you want to do.  
**Translation:** Vocabulary: execute: 执行; unbelievably: 难以置信地

**[1468.96s] English:** If it's not what you want to do, you're really stuck, and that difference is crucial.  
**Translation:** 

**[1476.78s] English:** And everyone has a balance of, let's say, deeper understanding and recipes, and some people are really  
**Translation:** Vocabulary: crucial: 至关重要的

**[1481.78s] English:** Good at recognizing when the problem is to understand something deeply, deeply does that.  
**Translation:** 

**[1487.82s] English:** It makes total sense. It's deeply understood at every stage of development, isn't it?  
**Translation:** 

**[1493.94s] English:** On the team, needed, well, this goes back to the art versus science question: sure.  
**Translation:** 

**[1498.96s] English:** If you constantly unpack everything for deeper understanding, you never get anything done.  
**Translation:** Vocabulary: unpack: 深入分析

**[1503.20s] English:** Right, and if you don't unpack your understanding when you need to, you'll do the wrong thing.  
**Translation:** 

**[1508.24s] English:** And then, at every juncture, like human beings—these really weird things, because  
**Translation:** Vocabulary: juncture: 关键时刻

**[1513.60s] English:** Everything you tell them has a million possible outputs, right, and then they all interact in a  
**Translation:** 

**[1519.46s] English:** Hilarious way, and then having some intuition about what to tell them what you do when.  
**Translation:** Vocabulary: hilarious: 滑稽; intuition: 直觉; outputs: 输出

**[1525.14s] English:** Do you intervene? When do you not? It's complicated.  
**Translation:** 

**[1528.96s] English:** Right, so it's essentially computationally unsolvable, yeah, it's an  
**Translation:** Vocabulary: computationally: 计算上; intervene: 干涉; unsolvable: 无法解决的

**[1534.00s] English:** Intractable problem, sure humans are a mess, but uh, with deep understanding, do you mean also?  
**Translation:** 

**[1542.88s] English:** Sort of fundamental questions, like what is a computer, or why something works the way it does.  
**Translation:** Vocabulary: intractable: 难以解决的

**[1554.46s] English:** Questions: Why are we even building this? For what purpose or reason?  
**Translation:** 

**[1558.96s] English:** Do you mean?  
**Translation:** 

**[1560.00s] English:** More like going towards the fundamental limits of physics, sort of really getting into the core.  
**Translation:** 

**[1566.50s] English:** Of the science, well, in terms of building a computer, think simple; think a little simpler.  
**Translation:** 

**[1571.04s] English:** So, the common practice is to build a computer, and then when somebody says they want to make it 10% better.  
**Translation:** 

**[1576.26s] English:** Faster, you'll go in and say, "All right, I need to make this buffer bigger, and maybe I'll add an ad.  
**Translation:** Vocabulary: buffer: 缓存

**[1581.90s] English:** Unit, or you know, I have this thing that's three instructions wide. I'm going to make it four.  
**Translation:** 

**[1586.22s] English:** Instructions are wide, and what you see is that each piece gets incrementally more complicated.  
**Translation:** Vocabulary: incrementally: 逐步地

**[1592.28s] English:** Right, and then at some point you hit this limit; like adding another feature or buffer doesn't...  
**Translation:** 

**[1599.40s] English:** It seems to make it any faster, and then people say that's because it's a fundamental limit.  
**Translation:** 

**[1604.40s] English:** And then somebody else will look at it and say, "Well, actually, the way you divided the problem up...  
**Translation:** 

**[1609.20s] English:** And the way that different features are interacting is limiting you, and it has to be  
**Translation:** Vocabulary: interacting: 相互作用

**[1613.62s] English:** Rethought, rewritten, and right.  
**Translation:** 

**[1616.22s] English:** So, then you refactor it and rewrite it, and what people commonly find is that the rewrite is not only  
**Translation:** Vocabulary: refactor: 重構; rewrite: 重寫; rewritten: 已重寫

**[1621.46s] English:** Faster, but half as complicated from scratch. Yes, so how often in your career, but have you seen?  
**Translation:** 

**[1628.42s] English:** As needed, maybe more generally, to just throw the whole thing out — this is where I'm.  
**Translation:** Vocabulary: scratch: 从头开始

**[1635.22s] English:** On one end, it's every three to five years. Which end are you on? Wait, rewrite more often.  
**Translation:** 

**[1642.14s] English:** Rewrite, and three to five years is so—if you want to really make  
**Translation:** 

**[1646.22s] English:** A lot of progress is made in computer architecture every five years, so you should consider doing one from scratch.  
**Translation:** 

**[1651.90s] English:** So, where does the x86_64 standard come in? Or, how often do you write?  
**Translation:** 

**[1659.42s] English:** I was a co-author of that spec in '98. That's 20 years ago, yeah, so it's still around.  
**Translation:** 

**[1666.14s] English:** Instruction sets have been extended quite a few times, yes, and instruction sets are less  
**Translation:** 

**[1671.90s] English:** Interesting, than the implementation underneath, there's been on x86.  
**Translation:** 

**[1676.22s] English:** Architecture: Intel has designed a few, aimed at designing a few.  
**Translation:** Vocabulary: implementation: 实现; underneath: 在...下面

**[1680.00s] English:** Very different architectures, and I don't want to go into too much detail about how often, but  
**Translation:** 

**[1687.68s] English:** There's a tendency to rewrite it every, you know, 10 years, and it really should be every five.  
**Translation:** 

**[1693.92s] English:** So, you're saying you're an outlier in that sense, and you rewrite it more often.  
**Translation:** 

**[1699.86s] English:** Well, and here's something that isn't that scary, yeah? Of course, well, scary to who? To everybody involved, because.  
**Translation:** Vocabulary: rewrite: 重写

**[1707.00s] English:** Like you said, repeating the recipe is efficient; companies want to make money, well, no individual...  
**Translation:** 

**[1715.04s] English:** Juniors want to succeed, so you want to incrementally improve and increase the buffer from three to four.  
**Translation:** 

**[1721.00s] English:** Well, this is where you get into diminishing returns curves. I think Steve Jobs said this right.  
**Translation:** 

**[1726.84s] English:** So, every time you have a project and you start here, and it goes up, but then there are diminishing returns.  
**Translation:** Vocabulary: diminishing: 递减的

**[1731.74s] English:** And to get to the next level, you have to do a new one, and the initial starting point.  
**Translation:** 

**[1736.42s] English:** Will be  
**Translation:** 

**[1737.00s] English:** Be lower than the old optimization point, but it'll get higher. So now you have two kinds of fear.  
**Translation:** 

**[1743.24s] English:** Short-term disaster and long-term disaster. You're grown-ups, right? Like, you know, people.  
**Translation:** Vocabulary: optimization: 优化

**[1752.40s] English:** With quarterly business objectives, they're terrified about changing everything, yeah, and...  
**Translation:** 

**[1758.00s] English:** People who are trying to run a business or build a computer for a long-term objective.  
**Translation:** Vocabulary: objectives: 目标

**[1763.32s] English:** Know that the short-term limitations block them from long-term success, so if you look at  
**Translation:** 

**[1770.28s] English:** Leaders of companies that had really good long-term success, every time they saw that they  
**Translation:** 

**[1776.40s] English:** Had to redo something they did, and so somebody has to speak up, or you do multiple projects in.  
**Translation:** 

**[1782.44s] English:** Parallel, like you optimize the old one while you build a new one, and but the marketing guys are  
**Translation:** Vocabulary: optimize: 优化; parallel: 并行

**[1787.70s] English:** Always like, make a promise to me that the new computer is faster on every single thing, and the computer.  
**Translation:** 

**[1793.18s] English:** Are  
**Translation:** 

**[1793.30s] English:** The architect says, "Well, the new computer will be faster on average.  
**Translation:** 

**[1795.92s] English:** But there's a distribution of results and performance, and you'll have  
**Translation:** 

**[1800.00s] English:** Outliers that are slower, and that's very hard because they have one customer who cares about.  
**Translation:** 

**[1804.18s] English:** That one. So, speaking of the long-term, for over 50 years now, Moore's Law has served as  
**Translation:** 

**[1810.22s] English:** For me, and millions of others, Berlin is an inspiring beacon of what an amazing future could be.  
**Translation:** 

**[1816.92s] English:** Engineers can build, yeah, I'm just making your kids laugh all day today. That was great, so uh, first,...  
**Translation:** Vocabulary: beacon: 灯塔

**[1825.38s] English:** In your eyes, what is Moore's Law if you could define it for people who don't know?  
**Translation:** 

**[1829.34s] English:** Well, the simple statement from Gordon Moore was that the number of transistors doubles every  
**Translation:** Vocabulary: transistors: 晶体管

**[1836.20s] English:** Two years, something like that, and then my operational model is to increase the performance.  
**Translation:** 

**[1844.84s] English:** Of computers by 2x every two or three years, and it's wigged around substantially over time.  
**Translation:** 

**[1851.04s] English:** And also, in how we deliver performance, has changed.  
**Translation:** 

**[1854.88s] English:** But the  
**Translation:** 

**[1859.34s] English:** The idea was to double the transistors every two years. The current cadence is something like they call it a  
**Translation:** 

**[1866.34s] English:** Shrink factor like 0.6 every two years, which is not 0.5, but that's referring strictly again.  
**Translation:** Vocabulary: cadence: 节奏; shrink: 缩小; strictly: 严格地

**[1873.72s] English:** To the original definition of transistor count and shrink factors, just getting them smaller.  
**Translation:** 

**[1878.34s] English:** Small and smaller, well, as you use for a constant chip area; right? If you make the transistor smaller,  
**Translation:** Vocabulary: transistor: 晶体管

**[1883.18s] English:** By 0.6, then you get one over 0.6 more transistors. So, can you linger on it a little longer? What's the  
**Translation:** 

**[1889.34s] English:** What's the broader definition of Moore's Law, in your opinion?  
**Translation:** Vocabulary: linger: 停留

**[1893.42s] English:** When you mention "perf," how do you think of performance, just broadly? What's a good way to think about it?  
**Translation:** 

**[1900.22s] English:** Moore's Law, well, first of all, so I've been aware of Moore's Law for 30 years.  
**Translation:** 

**[1906.96s] English:** In which sense, well, I've been designing computers for 40 years. You're just watching it before your eyes.  
**Translation:** 

**[1915.06s] English:** Well, and somewhere where I became aware of it, I was also informed that I'm  
**Translation:** 

**[1919.34s] English:** Moore's law was going to...  
**Translation:** 

**[1920.00s] English:** To die in 10 to 15 years, and I thought that was true at first, but then after 10 years, it was going...  
**Translation:** 

**[1925.56s] English:** To die in 10 to 15 years, and then at one point it was going to die in five years, and then it went...  
**Translation:** 

**[1930.20s] English:** Back up to 10 years, and at some point, I decided not to worry about that particular prognostication.  
**Translation:** Vocabulary: prognostication: 预测

**[1936.08s] English:** For the rest of my life, which is fun, and then I joined Intel, and everyone said Moore's Law.  
**Translation:** 

**[1941.94s] English:** Is dead, and I thought that's sad because it's the Moore's Law company, and it's not dead and it's  
**Translation:** 

**[1947.22s] English:** Always, it's been said we're going to die, and you know, humans like these apocryphal kinds of statements like,  
**Translation:** 

**[1953.62s] English:** We'll run out of food, or run out of air, or run out of room, or run out of something, you know.  
**Translation:** Vocabulary: apocryphal: 未经证实的

**[1959.00s] English:** Right, but it's still incredible that it's lived for as long as it has, and yes, there are many people.  
**Translation:** 

**[1966.24s] English:** Who believe now that Moore's Law is dead, you know, they can join the last 50 years of people.  
**Translation:** 

**[1973.14s] English:** Yeah, there's a long tradition, but why do you think?  
**Translation:** 

**[1977.20s] English:** If you can, in text, try to understand why you think it's not dead. Well, for now, let's just  
**Translation:** 

**[1984.28s] English:** Think, um, people think Moore's law is just about transistors getting smaller, but actually, there's more to it than that.  
**Translation:** 

**[1989.96s] English:** There's literally thousands of innovations, and almost all of those innovations have their own  
**Translation:** Vocabulary: innovations: 创新; transistors: 晶体管

**[1994.84s] English:** Diminishing return curves: so, if you graph it, it looks like a cascade of diminishing return curves.  
**Translation:** 

**[2000.78s] English:** I don't know what to call that, but the result is an exponential curve, but at least it has.  
**Translation:** Vocabulary: cascade: 瀑布; diminishing: 递减的; exponential: 指数的

**[2007.18s] English:** Been so, and we keep inventing new things. So, if you're an expert in one of the things on a  
**Translation:** 

**[2013.02s] English:** Diminishing return curve, right? And you can see its plateau. You will probably tell people, "Well, this is...  
**Translation:** Vocabulary: plateau: 饱和阶段

**[2020.62s] English:** This is done, meanwhile, some other pile of people are doing something different, so that's that's  
**Translation:** 

**[2027.02s] English:** Just normal, so then there's the observation of how small a switching device could be.  
**Translation:** 

**[2033.90s] English:** So, a modern transistor is something like one thousand by one thousand by one thousand.  
**Translation:** 

**[2037.18s] English:** Atoms, right? And  
**Translation:** Vocabulary: transistor: 晶体管

**[2040.00s] English:** And you get quantum effects down around 2 to 10 atoms.  
**Translation:** 

**[2044.34s] English:** So, you can imagine a transistor as small as 10 by 10 by 10.  
**Translation:** Vocabulary: quantum: 量子

**[2048.14s] English:** So that's a million times smaller.  
**Translation:** 

**[2051.90s] English:** And then, the quantum computational people are working away at how to use quantum effects.  
**Translation:** Vocabulary: computational: 计算的

**[2059.56s] English:** So,...  
**Translation:** 

**[2060.08s] English:** 1,000 by 1,000 by 1,000.  
**Translation:** 

**[2061.88s] English:** Atoms.  
**Translation:** 

**[2063.42s] English:** That's a really clean way of putting it.  
**Translation:** 

**[2066.60s] English:** Well, a fan, like a modern transistor, if you look at the fan,  
**Translation:** 

**[2069.70s] English:** It's like 120 atoms wide, but we can make it thinner.  
**Translation:** 

**[2073.42s] English:** And then there's a gate wrapped around it, and then there's spacing.  
**Translation:** 

**[2076.62s] English:** There's a whole bunch of geometry.  
**Translation:** Vocabulary: geometry: 几何

**[2078.94s] English:** And, you know, a competent transistor designer could count the atoms in every single direction.  
**Translation:** 

**[2087.64s] English:** Like, there are techniques now that allow us to already put down atoms in a single atomic layer.  
**Translation:** 

**[2092.82s] English:** And you can place atoms if you want to.  
**Translation:** 

**[2095.58s] English:** It's just, you know, from a manufacturing process.  
**Translation:** 

**[2099.46s] English:** If you're going to put atoms in a single atomic layer,  
**Translation:** 

**[2099.70s] English:** Placing an atom takes 10 minutes, and you need to put, you know,...  
**Translation:** 

**[2103.80s] English:** It would take a long time to gather 10 to the 23rd atoms to make a computer.  
**Translation:** 

**[2108.82s] English:** So the methods are, you know, both shrinking things.  
**Translation:** Vocabulary: shrinking: 缩小

**[2112.68s] English:** And then coming up with effective ways to control what's happening.  
**Translation:** 

**[2118.04s] English:** Manufacture stably and cheaply.  
**Translation:** Vocabulary: cheaply: 便宜地; manufacture: 生产; stably: 稳定地

**[2120.02s] English:** Yeah.  
**Translation:** 

**[2121.04s] English:** So, the innovation stack is pretty broad.  
**Translation:** 

**[2123.60s] English:** You know, there's equipment, there's optics, there's chemistry.  
**Translation:** 

**[2126.68s] English:** There's physics, there's materials science,  
**Translation:** Vocabulary: optics: 光学

**[2128.98s] English:** There's metallurgy.  
**Translation:** 

**[2130.70s] English:** There are lots of ideas about when you put different materials together,  
**Translation:** Vocabulary: metallurgy: 冶金学

**[2133.70s] English:** How do they interact? Are they stable? Are they stable over temperature?  
**Translation:** 

**[2137.96s] English:** You know, are they repeatable?  
**Translation:** 

**[2140.58s] English:** You know, there are literally thousands of technologies involved.  
**Translation:** 

**[2145.12s] English:** But just for the shrinking, you don't think we're quite yet close to the fundamental limits of physics?  
**Translation:** 

**[2150.86s] English:** I did a talk on Mars law, and I asked for a roadmap to a path of 100%.  
**Translation:** 

**[2154.64s] English:** And after two weeks, they said we only got to 50%.  
**Translation:** Vocabulary: roadmap: 规划图

**[2158.80s] English:** 100? What, sorry?  
**Translation:** 

**[2159.72s] English:** 100.  
**Translation:** 

**[2160.00s] English:** X shrinks by 100; X shrunk, we only got to 50, and I said, "Why don't you give it another two weeks?  
**Translation:** 

**[2164.80s] English:** Well, here's the thing about Moore's Law, right? So I believe that the next 10 or 20 years will see  
**Translation:** Vocabulary: shrinks: 缩小; shrunk: 已经缩小

**[2174.26s] English:** Shrinking is going to happen right now. As a computer designer, there's two stances.  
**Translation:** 

**[2180.26s] English:** You think it's going to shrink, in which case you're designing and thinking about architecture.  
**Translation:** Vocabulary: shrink: 缩小; stances: 立场

**[2186.02s] English:** In a way that you'll use more transistors, or conversely, not be swamped by the complexity of,  
**Translation:** 

**[2192.96s] English:** All the transistors, you get right; you have to have a strategy, you know, so you're not open.  
**Translation:** Vocabulary: complexity: 复杂性; conversely: 相反地; swamped: 淹没; transistors: 晶体管

**[2200.50s] English:** To the possibility, and waiting for the possibility of a whole new army of transistors ready to work.  
**Translation:** 

**[2205.84s] English:** I'm expecting more transistors every two or three years by a number large enough.  
**Translation:** 

**[2212.00s] English:** That's how you think about design, and how you think about architecture, has to change.  
**Translation:** 

**[2216.02s] English:** Like, imagine you're building brick buildings out of bricks, and every year the bricks...  
**Translation:** 

**[2222.04s] English:** Are they half the size, or every two years? Well, if you kept building bricks the same way, you know, so many...  
**Translation:** 

**[2228.72s] English:** Bricks per person per day: the amount of time to build a building would go up exponentially.  
**Translation:** 

**[2234.68s] English:** Right, right. But if you said, "I know that's coming, so now I'm going to design equipment that moves,  
**Translation:** 

**[2241.46s] English:** Bricks are faster and use them better, because maybe you're getting something out of the smaller bricks more.  
**Translation:** 

**[2245.50s] English:** Strength.  
**Translation:** 

**[2246.02s] English:** Inner walls, you know, require less material efficiency out of that, so once you have a roadmap with what's  
**Translation:** Vocabulary: roadmap: 规划图

**[2251.92s] English:** Going to happen, transistors are going to get smaller, and we're going to get more of them than you.  
**Translation:** 

**[2257.06s] English:** Design all this collateral around it to take advantage of it, and also to cope with it.  
**Translation:** Vocabulary: collateral: 辅助设备

**[2262.56s] English:** That's the thing; people don't understand. It's like, if I didn't believe in Moore's Law, and then  
**Translation:** 

**[2266.52s] English:** Moore's Law, with its increasing number of transistors, showed up, and my design teams were all drowned. So, what's the hardest?  
**Translation:** 

**[2273.78s] English:** Part of this  
**Translation:** 

**[2276.02s] English:** I mean, even if you just look historically throughout  
**Translation:** Vocabulary: historically: 按历史

**[2280.00s] English:** Your career: What's the thing that fundamentally changes when you add more?  
**Translation:** 

**[2286.08s] English:** Transistors in the task of designing an architecture, well, there are two  
**Translation:** Vocabulary: fundamentally: 从根本上; transistors: 晶体管

**[2291.66s] English:** Constants, right? One is that people don't get smarter, I think. By the way, there's some science showing  
**Translation:** 

**[2297.20s] English:** That we do get smarter because of nutrition, however, yeah. Sorry to bring that up, yes.  
**Translation:** Vocabulary: constants: 不变因素

**[2302.80s] English:** Yeah, familiar with it. Nobody understands it. Nobody knows if it's still going on, so that's a  
**Translation:** 

**[2306.76s] English:** Or whether it's real or not, but yeah, I sort of anyway, but not, I would believe for the most part.  
**Translation:** 

**[2313.38s] English:** People aren't getting much smarter; the evidence doesn't support it. That's right, and then teams...  
**Translation:** 

**[2318.48s] English:** Can't grow that much, right? So, human beings understand, you know, we're really good in teams, of  
**Translation:** 

**[2324.48s] English:** 10: You know, up to teams of 100, they can know each other. Beyond that, you have to have organizational structures in place.  
**Translation:** 

**[2329.60s] English:** Boundaries, so you're kind of like you have those, are pretty hard constraints, right? So then you have...  
**Translation:** Vocabulary: constraints: 限制

**[2335.30s] English:** To divide and conquer, like  
**Translation:** 

**[2336.76s] English:** As the designs get bigger, you have to divide it into pieces. You know the power of abstraction.  
**Translation:** Vocabulary: abstraction: 抽象

**[2341.72s] English:** Layers is really high. We used to build computers out of transistors, now we have a team that turns.  
**Translation:** 

**[2347.40s] English:** Transistors into logic cells, and another team that turns them into functional units.  
**Translation:** Vocabulary: functional: 功能性的

**[2350.82s] English:** One that turns into computers, right? So we have abstraction layers in there, and you have to think.  
**Translation:** 

**[2358.50s] English:** About when do you shift gears? On that, we also use faster computers to build even faster ones.  
**Translation:** 

**[2363.86s] English:** So, some algorithms run twice as fast on new computers.  
**Translation:** 

**[2366.76s] English:** But a lot of algorithms are O(n^2), so you know, a computer with twice as many transistors and it  
**Translation:** Vocabulary: transistors: 晶体管

**[2373.70s] English:** Might take four times as long to run, so you have to refactor the software, like simply using.  
**Translation:** 

**[2380.06s] English:** Faster computers to build bigger computers doesn't work, so you have to think about all these things.  
**Translation:** Vocabulary: refactor: 重构代码

**[2386.14s] English:** So, in terms of computing performance, and the exciting possibility that more powerful computers  
**Translation:** 

**[2390.62s] English:** Bring is shrinking the thing we've just been talking about.  
**Translation:** Vocabulary: computing: 计算; shrinking: 缩小

**[2394.92s] English:** One of the things we've been talking about is the fact that we're not going to be able to  
**Translation:** 

**[2396.76s] English:** Clean up our DB Center and get the hardware right away. It's not going to be perfect, so but.  
**Translation:** 

**[2398.92s] English:** It's going to happen, and maybe one day Olivia will be able to get the hardware right away.  
**Translation:** 

**[2400.00s] English:** Advancement in performance, or are there other directions you're interested in, like?  
**Translation:** Vocabulary: advancement: 进步

**[2404.24s] English:** Like in the direction of enforcing given parallelism, or like doing massive parallelism in,...  
**Translation:** 

**[2412.30s] English:** Terms of many, many CPUs, you know, stacking CPUs on top of each other, that kind of...  
**Translation:** Vocabulary: enforcing: 强制; stacking: 堆叠

**[2419.04s] English:** Parallelism, or any kind of well-thought-out approach, might be considered differently. For instance, older computers, you know, were slower.  
**Translation:** 

**[2424.60s] English:** Computers: You said "A equals B plus C times D." Pretty simple, right? And then we made faster computers.  
**Translation:** Vocabulary: equals: 等于

**[2432.52s] English:** With vector units, you can do proper equations and matrices, and then modern AI.  
**Translation:** 

**[2440.12s] English:** Computations, or like convolutional neural networks, where you convolve one large data set against  
**Translation:** Vocabulary: computations: 计算; convolutional: 卷积; convolve: 卷积; equations: 方程; matrices: 矩阵; neural: 神经

**[2445.74s] English:** Another, and so there's sort of a hierarchy in mathematics, you know, from simple equations to  
**Translation:** 

**[2453.16s] English:** Linear equations to matrix equations, and so on and so forth.  
**Translation:** Vocabulary: hierarchy: 等级体系; linear: 线性的; matrix: 矩阵

**[2454.60s] English:** To deeper kinds of computation, and the data sets are getting so big that people are thinking of  
**Translation:** 

**[2461.56s] English:** Data as a topology problem: you know, data is organized in some immense shape, and then the  
**Translation:** Vocabulary: computation: 计算; immense: 巨大的; topology: 拓扑

**[2468.52s] English:** Computation, which sort of wants to get data from an immense shape and do some computation on it.  
**Translation:** 

**[2474.60s] English:** So, the computers have allowed people to have algorithms go much, much further.  
**Translation:** 

**[2482.04s] English:** So, that paper you referred to.  
**Translation:** 

**[2484.58s] English:** To the paper, they talked about, you know, like when AI started, it was applying rule sets to something.  
**Translation:** 

**[2490.86s] English:** That's a very simple computational situation, and then when they did the first chess thing, they  
**Translation:** 

**[2498.00s] English:** They solved deep searches, so they have a huge database of moves and results from deep searches, but it's still  
**Translation:** Vocabulary: computational: 计算的

**[2505.40s] English:** Just a search right now, we take large numbers of images and we use them to train these weight sets.  
**Translation:** 

**[2513.86s] English:** That we use to train these weight sets, that we use to train these weight sets, that we use to train.  
**Translation:** 

**[2514.56s] English:** That we use to train these weight sets, that we use to train these weight sets. Where we convolve across.  
**Translation:** 

**[2515.92s] English:** Where we convolve, it's a completely different kind of phenomenon. We call that AI.  
**Translation:** 

**[2520.00s] English:** Now, they're doing the next generation.  
**Translation:** 

**[2522.42s] English:** And if you look at it, they're going up this mathematical graph, right?  
**Translation:** Vocabulary: mathematical: 数学的

**[2527.36s] English:** And then, computations—both computation and data sets—support going up that graph.  
**Translation:** 

**[2533.94s] English:** Yeah, the kind of computation that might, I mean, I would argue that all of it is still a form of search, right?  
**Translation:** Vocabulary: computations: 计算

**[2539.62s] English:** Just like you said, a topology problem with data sets.  
**Translation:** 

**[2542.80s] English:** He's searching the data sets for valuable data.  
**Translation:** Vocabulary: topology: 数据结构问题

**[2546.86s] English:** And also, the actual optimization of neural networks is a kind of search for the...  
**Translation:** 

**[2553.02s] English:** I don't know.  
**Translation:** Vocabulary: neural: 神经元; optimization: 优化

**[2553.34s] English:** If you had looked at the inner layers of finding a cat, it's not a search.  
**Translation:** 

**[2559.12s] English:** It's a set of endless projections.  
**Translation:** Vocabulary: projections: 预测

**[2561.34s] English:** So, you know, a projection: here's a shadow of this phone, right?  
**Translation:** 

**[2565.52s] English:** And then you can have a shadow of that on something, a shadow on that of something.  
**Translation:** Vocabulary: projection: 投影像

**[2569.24s] English:** If you look in the layers, you'll see that this layer actually describes pointy ears.  
**Translation:** 

**[2573.46s] English:** And round, eye-ness and fuzziness.  
**Translation:** Vocabulary: fuzziness: 毛茸茸; pointy: 尖尖的

**[2576.26s] English:** But the...  
**Translation:** 

**[2576.86s] English:** The computation to tease out the attributes is not a search.  
**Translation:** Vocabulary: attributes: 特征; computation: 计算

**[2583.78s] English:** Right, I mean....  
**Translation:** 

**[2584.46s] English:** Like the inference part might be search, but the training is not search.  
**Translation:** Vocabulary: inference: 推断

**[2587.44s] English:** Okay, well,...  
**Translation:** 

**[2587.92s] English:** And then, in deep networks, they look at layers and they don't even know it's represented.  
**Translation:** 

**[2594.10s] English:** And yet, if you take the layers out, it doesn't work.  
**Translation:** 

**[2596.58s] English:** Okay, so...  
**Translation:** 

**[2597.32s] English:** So, I don't think it's a search.  
**Translation:** 

**[2598.84s] English:** All right, well,...  
**Translation:** 

**[2599.50s] English:** But you have to talk to a mathematician about what that actually is.  
**Translation:** 

**[2602.66s] English:** Well, we could disagree, but the...  
**Translation:** Vocabulary: mathematician: 数学家

**[2605.58s] English:** It's just a matter of semantics.  
**Translation:** 

**[2606.98s] English:** I think it's not...  
**Translation:** Vocabulary: semantics: 语义

**[2607.92s] English:** But it's certainly not....  
**Translation:** 

**[2609.02s] English:** I would say it's absolutely not a matter of semantics, but...  
**Translation:** 

**[2611.80s] English:** Okay.  
**Translation:** 

**[2613.40s] English:** All right; well, if you want to go there.  
**Translation:** 

**[2616.78s] English:** So, optimization to me is search.  
**Translation:** 

**[2618.96s] English:** And we're trying to optimize the ability of a neural network to detect cat ears.  
**Translation:** Vocabulary: detect: 识别; optimize: 优化

**[2625.92s] English:** And the difference between chess and the space is,  
**Translation:** 

**[2631.16s] English:** The incredibly multidimensional, hundred-thousand-dimensional space that,  
**Translation:** Vocabulary: multidimensional: 多维度的

**[2636.86s] English:** You know, networks are trying to optimize over is nothing like....  
**Translation:** 

**[2640.00s] English:** The chessboard database is a totally different kind of thing, and okay, in that sense.  
**Translation:** Vocabulary: chessboard: 棋盘

**[2645.62s] English:** You can say, "Yeah, yeah, it loses. I can see how you might say that. The funny thing is,  
**Translation:** 

**[2652.26s] English:** The difference between given search space and found search space, right? Exactly. Maybe that's  
**Translation:** 

**[2657.84s] English:** A different way—that's a beautiful way to put it. Okay, but what's your sense in terms of...  
**Translation:** 

**[2661.98s] English:** Of the basic mathematical operations and the architectures of computer hardware that enables  
**Translation:** Vocabulary: mathematical: 数学的

**[2668.52s] English:** Those operations, do you see the CPUs of today still being a really core part of executing?  
**Translation:** 

**[2675.90s] English:** Those mathematical operations, yes. Well, the operations you know continue to be add and subtract.  
**Translation:** Vocabulary: executing: 运行; subtract: 减法

**[2682.02s] English:** Load, store, compare, and branch—it's remarkable how interesting these building blocks are.  
**Translation:** 

**[2688.70s] English:** Of course, if you know about computers or transistors and you know about atoms, so you've got atoms, transistors, and computers.  
**Translation:** Vocabulary: transistors: 晶体管

**[2693.92s] English:** Logic gates, computers—right? You know, functional units and computers.  
**Translation:** 

**[2698.52s] English:** Building blocks of mathematics at some level are things like adds, subtracts, and multiplies, but  
**Translation:** Vocabulary: functional: 功能性的; multiplies: 乘法; subtracts: 减法

**[2704.62s] English:** The space mathematics can describe is, I think, essentially infinite, but the computers that run  
**Translation:** 

**[2713.08s] English:** The algorithms are still doing the same things. Now, a given algorithm might say, "I need sparse data.  
**Translation:** Vocabulary: algorithm: 计算方法; infinite: 无限的; sparse: 稀疏的

**[2720.16s] English:** Or I need 32-bit data, or I need, you know, something like a convolution operation that naturally takes...  
**Translation:** 

**[2728.52s] English:** Data multiplies it and sums it up in a certain way. So, for example, the data types in TensorFlow imply an  
**Translation:** Vocabulary: convolution: 卷积操作

**[2735.96s] English:** Optimization set, but when you go right down and look at the computers, it's OR gates doing ANDs.  
**Translation:** 

**[2741.72s] English:** And it multiplies like that, hasn't changed much. Now, the quantum researchers think they're going to  
**Translation:** Vocabulary: optimization: 优化; quantum: 量子

**[2748.90s] English:** Change that radically, and then there are people who think about analog computing, because you look in  
**Translation:** 

**[2752.66s] English:** The brain, and it seems to be more analog-ish, you know, that maybe there's a way to do that more.  
**Translation:** Vocabulary: analog: 模拟的; computing: 计算; radically: 根本上

**[2758.52s] English:** Efficiently, but we have  
**Translation:** 

**[2760.00s] English:** A million X on computation, and I don't know the reference or the relationship between computational.  
**Translation:** Vocabulary: computation: 计算; computational: 计算相关的; efficiently: 高效地

**[2769.00s] English:** Let's say, in terms of intensity and ability to hit mathematical abstractions, I don't know.  
**Translation:** 

**[2776.06s] English:** Anybody has described that, but it's just like what you saw in AI — you went from rule sets to simple search.  
**Translation:** 

**[2782.92s] English:** To perform a complex search, to say nothing of finding searches like those, are you kidding me? That's orders of magnitude more computation.  
**Translation:** 

**[2789.90s] English:** To do, and as we get the next two orders of magnitude, like a friend Roger Godori said, like  
**Translation:** 

**[2796.58s] English:** Every order of magnitude changes the computation fundamentally, changing what the computation is.  
**Translation:** 

**[2802.42s] English:** Doing, yeah, oh, you know, the expression: "The difference in quantity is the difference in kind.  
**Translation:** Vocabulary: fundamentally: 从根本上

**[2807.94s] English:** You know the difference between an ant and an anthill, or a neuron and a brain?  
**Translation:** 

**[2814.36s] English:** You know, there's an indefinable place where the  
**Translation:** Vocabulary: anthill: 蚁巢; indefinable: 难以界定; neuron: 神经元

**[2819.28s] English:** The quantity  
**Translation:** 

**[2819.90s] English:** Quantity changed the quality, right? And we've seen that happen in mathematics multiple times.  
**Translation:** 

**[2825.16s] English:** You know, my guess is it's going to keep happening. So, in your sense, is yeah, if you focus,...  
**Translation:** 

**[2830.78s] English:** Head down and shrinking the transistor; let's not just head down—we're aware of the software.  
**Translation:** Vocabulary: shrinking: 缩小; transistor: 晶体管

**[2837.86s] English:** Stacks that are running under heavy computational loads, and we're kind of pondering what to do with them.  
**Translation:** 

**[2843.32s] English:** A petabyte of memory that wants to be accessed in a sparse way, and have you know the kind of  
**Translation:** Vocabulary: accessed: 被访问; computational: 计算的; petabyte: 拍字节; pondering: 考虑; sparse: 稀疏的; stacks: 堆栈

**[2848.58s] English:** Calculations AI  
**Translation:** 

**[2849.90s] English:** Programmers want there to be a dialogue and interaction, but when you go  
**Translation:** Vocabulary: programmers: 程序员

**[2855.46s] English:** In the computer chip, you know, you find adders, subtractors, and multipliers, and  
**Translation:** 

**[2861.58s] English:** So, if you zoom out, then, as you mentioned (Rich Sutton), the idea that most of the development...  
**Translation:** Vocabulary: adders: 加法器; multipliers: 乘法器; subtractors: 减法器

**[2868.46s] English:** In the last many decades, advances in AI research have come from just leveraging computation and just.  
**Translation:** 

**[2874.72s] English:** The simple algorithms are waiting for the computation to improve.  
**Translation:** Vocabulary: advances: 进步; computation: 计算; leveraging: 利用

**[2879.90s] English:** And you know, that's already out there. Please get really into it.  
**Translation:** 

**[2880.00s] English:** Well, software guys have a thing that they call the problem of early optimization.  
**Translation:** Vocabulary: optimization: 优化

**[2886.14s] English:** Right.  
**Translation:** 

**[2886.90s] English:** So, you write a big software stack, and if you start optimizing, like the first thing you write, the odds of that being the performance limiter are low.  
**Translation:** Vocabulary: limiter: 限制器; optimizing: 优化

**[2895.10s] English:** Right.  
**Translation:** 

**[2895.28s] English:** But when you get the whole thing working, can you make it 2x faster by optimizing the right things?  
**Translation:** 

**[2899.20s] English:** Problem.  
**Translation:** 

**[2899.26s] English:** You.  
**Translation:** 

**[2899.90s] English:** Sure.  
**Translation:** 

**[2900.96s] English:** While you're optimizing that, could you have written a new software stack, which would have been a better choice?  
**Translation:** 

**[2904.42s] English:** You.  
**Translation:** 

**[2905.96s] English:** Maybe.  
**Translation:** 

**[2907.00s] English:** Now, you have creative tension.  
**Translation:** 

**[2907.94s] English:** G  
**Translation:** 

**[2908.00s] English:** But the whole time, as you're doing the writing, that's the software we're talking about.  
**Translation:** 

**[2909.26s] English:** G  
**Translation:** 

**[2909.78s] English:** F  
**Translation:** 

**[2909.86s] English:** F  
**Translation:** 

**[2909.88s] English:** F  
**Translation:** 

**[2914.82s] English:** The hardware underneath gets faster and faster.  
**Translation:** Vocabulary: underneath: 在下面

**[2916.70s] English:** Well, it goes back to Moore's Law.  
**Translation:** 

**[2918.00s] English:** If Moore's Law is going to continue, then your AI research should expect that to show up.  
**Translation:** 

**[2925.88s] English:** And then you make a slightly different set of choices.  
**Translation:** 

**[2927.66s] English:** Then we've hit the wall.  
**Translation:** 

**[2929.82s] English:** Nothing's going to happen.  
**Translation:** 

**[2931.18s] English:** And from here, it's just us rewriting algorithms.  
**Translation:** Vocabulary: rewriting: 修改

**[2934.90s] English:** Like, that seems like a failed strategy for the last 30 years.  
**Translation:** 

**[2938.00s] English:** Moore's Law is dead.  
**Translation:** 

**[2939.96s] English:** So, can you just linger on it?  
**Translation:** 

**[2943.00s] English:** I think you've answered it, but I'll just ask the same dumb question over and over.  
**Translation:** Vocabulary: linger: 逗留

**[2946.88s] English:** So, why do you think Moore's Law is not going to die?  
**Translation:** 

**[2952.42s] English:** Which is the most promising, exciting possibility for why it won't die in the next 5 to 10 years?  
**Translation:** 

**[2958.04s] English:** So, is it the continued shrinking of the transistor, or is it another S-curve that steps in and it totally sort of...  
**Translation:** 

**[2965.50s] English:** Well, the shrinking of the transistor is literally...  
**Translation:** Vocabulary: shrinking: 缩小; transistor: 晶体管

**[2968.00s] English:** It's literally thousands of innovations.  
**Translation:** 

**[2970.16s] English:** Right.  
**Translation:** Vocabulary: innovations: 创新

**[2970.50s] English:** So, there are stacks of S-curves in there.  
**Translation:** 

**[2973.00s] English:** There's a whole bunch of S-curves just kind of running their course, and being reinvented with new things.  
**Translation:** Vocabulary: stacks: 堆积的

**[2980.60s] English:** You know, the semiconductor fabricators and technologists have all announced what's called nanowires.  
**Translation:** 

**[2987.46s] English:** So, they took a fin, which had a gate around it, and turned that into little wires so you have better control of it.  
**Translation:** Vocabulary: fabricators: 半导体制造商; nanowires: 纳米线; semiconductor: 半导体; technologists: 技术专家

**[2993.98s] English:** And they're smaller.  
**Translation:** 

**[2995.40s] English:** And then, from there, there are some obvious steps about how to...  
**Translation:** 

**[2997.96s] English:** How to shrink that?  
**Translation:** 

**[2999.32s] English:** So, the metal...  
**Translation:** Vocabulary: shrink: 收缩

**[3000.00s] English:** Allergies around wire stacks and stuff have very obvious abilities to shrink.  
**Translation:** 

**[3007.26s] English:** And, you know, there's a whole combination of things to do there.  
**Translation:** Vocabulary: allergies: 过敏反应

**[3011.10s] English:** Your sense is that we're going to get a lot of this innovation from just that shrinking.  
**Translation:** 

**[3016.60s] English:** Yeah, like a factor of 100 is a lot.  
**Translation:** 

**[3019.12s] English:** Yeah, I would say that's incredible.  
**Translation:** 

**[3022.18s] English:** And it's totally unknown.  
**Translation:** 

**[3023.72s] English:** It's only 10 or 15 years.  
**Translation:** 

**[3025.02s] English:** Now, you're smart, and you might know, but to me, it's totally unpredictable what that 100x would bring in terms of the nature of the computation that people would be doing.  
**Translation:** Vocabulary: computation: 计算; unpredictable: 不可预测

**[3034.24s] English:** Yeah, are you familiar with Bell's Law?  
**Translation:** 

**[3036.98s] English:** So, for a long time, it was mainframes, minis, workstations, PCs, and mobile devices.  
**Translation:** Vocabulary: mainframes: 大型机; workstations: 工作站

**[3042.58s] English:** Moore's Law drove faster, smaller computers, right?  
**Translation:** 

**[3046.18s] English:** And then, when we were thinking about Moore's Law, Raja Gidori said that every 10x generates a new computation.  
**Translation:** Vocabulary: generates: 产生

**[3053.12s] English:** So, scalar.  
**Translation:** 

**[3055.02s] English:** Vector, matrix, topological computation, right?  
**Translation:** Vocabulary: matrix: 矩阵; scalar: 标量; topological: 拓扑的

**[3061.00s] English:** And if you go look at the industry trends, there were mainframes, minicomputers, and PCs.  
**Translation:** 

**[3067.08s] English:** And then the Internet took off.  
**Translation:** Vocabulary: minicomputers: 小型计算机

**[3068.90s] English:** And then we got mobile devices.  
**Translation:** 

**[3070.70s] English:** And now, we're building 5G wireless with one-millisecond latency.  
**Translation:** Vocabulary: latency: 延迟; wireless: 无线

**[3074.56s] English:** And people are starting to think about the smart world where everything knows you, recognizes you.  
**Translation:** 

**[3082.42s] English:** Like the transformations are going to be.  
**Translation:** Vocabulary: transformations: 变化

**[3085.36s] English:** Like, unpredictable.  
**Translation:** 

**[3087.14s] English:** How does it make you feel that you're one of the key architects of this kind of future?  
**Translation:** 

**[3095.10s] English:** So, we're not talking about the architects or the high-level people who build the Angry Birds apps and Snapchat.  
**Translation:** 

**[3103.42s] English:** Angry Bird apps.  
**Translation:** 

**[3104.74s] English:** Who knows?  
**Translation:** 

**[3105.18s] English:** Maybe that's the whole point of the universe.  
**Translation:** 

**[3107.26s] English:** I'm going to take a stand on that and the attention-distracting nature of mobile phones.  
**Translation:** 

**[3112.80s] English:** I'll take a stand.  
**Translation:** 

**[3113.80s] English:** But, anyway, in terms of...  
**Translation:** 

**[3115.00s] English:** I don't think that matters much.  
**Translation:** 

**[3117.58s] English:** The side effects of...  
**Translation:** 

**[3120.00s] English:** Smartphones, or the attention distraction — which part? Well, who knows? You know, where this is all headed.  
**Translation:** Vocabulary: distraction: 注意力分散

**[3125.76s] English:** Leading, it's changing so fast. Wait, so back when my parents used to yell at my sisters for hiding.  
**Translation:** 

**[3130.02s] English:** In the closet, with a wired phone with a dial on it. Stop talking to your friends all day, right?  
**Translation:** Vocabulary: closet: 壁橱

**[3134.90s] English:** Now, my wife yells at my kids for talking to their friends all day on text.  
**Translation:** 

**[3139.48s] English:** It looks the same to me. It's always just echoes of the same thing, okay? But you are the one of the  
**Translation:** Vocabulary: echoes: 回声

**[3145.84s] English:** Key people are architecting the hardware of this future. How does that make you feel? Do you feel  
**Translation:** 

**[3150.82s] English:** Responsible, do you feel excited? So, we're in a social context, so there are billions of people.  
**Translation:** Vocabulary: architecting: 设计

**[3159.14s] English:** On this planet, there are literally millions of people working on technology. I feel lucky to be.  
**Translation:** 

**[3167.06s] English:** You know, what I do and getting paid for it, and there's an interest in it, but there's  
**Translation:** 

**[3173.16s] English:** So many things are going on in parallel, it's  
**Translation:** 

**[3175.84s] English:** Like the actions are so unpredictable; if I weren't here, somebody else would do it.  
**Translation:** Vocabulary: parallel: 并行; unpredictable: 不可预测

**[3180.08s] English:** The vectors of all these different things are happening all the time.  
**Translation:** 

**[3184.58s] English:** You know, I'm sure some philosopher or metaphysicists are wondering about  
**Translation:** Vocabulary: vectors: 向量

**[3192.42s] English:** How we transform our world, so you can't deny the fact that these tools, whether  
**Translation:** 

**[3199.36s] English:** That these tools are changing our world. That's right.  
**Translation:** 

**[3204.94s] English:** So, do you think?  
**Translation:** 

**[3205.84s] English:** It's changing for the better. Somebody I read this thing recently; it said the two disciplines...  
**Translation:** Vocabulary: disciplines: 学科

**[3213.52s] English:** With the highest GRE scores in college, physics and philosophy are right, and they're both sort of  
**Translation:** 

**[3220.58s] English:** Trying to answer the question, "Why is there anything at all?" and the philosophers, you know,  
**Translation:** Vocabulary: philosophers: 哲学家

**[3225.50s] English:** Are on the kind of theological side, and the physicists are obviously on the, you know, the  
**Translation:** 

**[3230.64s] English:** Material side, and there are a hundred billion galaxies, with each galaxy containing a hundred billion stars.  
**Translation:** Vocabulary: galaxies: 星系; galaxy: 星系; physicists: 物理学家; theological: 神学的

**[3235.84s] English:** A hundred billion stars? It seems a bit repetitive, at best.  
**Translation:** 

**[3240.00s] English:** So, I guess there's a lot of talk about us reaching 10 billion people, and it's hard to say exactly when that will happen.  
**Translation:** Vocabulary: repetitive: 重复的

**[3247.60s] English:** All for if that's what you're asking, yeah. I guess I am. Do tend to or significantly increase?  
**Translation:** 

**[3253.84s] English:** In complexity, and I'm curious about how computation, like in our world and our physical world, works.  
**Translation:** Vocabulary: complexity: 复杂性; computation: 计算

**[3262.72s] English:** The world inherently generates mathematics; it's kind of obvious, right? So, we have XYZ coordinates.  
**Translation:** 

**[3268.16s] English:** You take a sphere, you make it bigger, and you get a surface area that grows by \( r^2 \).  
**Translation:** Vocabulary: coordinates: 坐标; generates: 产生

**[3273.48s] English:** Like it, generally, it generates mathematics and the mathematicians and the physicists.  
**Translation:** 

**[3278.04s] English:** Have been having a lot of fun talking to each other for years, and computation has been  
**Translation:** Vocabulary: mathematicians: 数学家

**[3282.86s] English:** Let's say, relatively pedestrian-like computation in terms of mathematics has been doing binary.  
**Translation:** 

**[3290.04s] English:** Binary algebra, while those guys have been gallivanting through the other realms of possibility.  
**Translation:** Vocabulary: algebra: 代数

**[3298.16s] English:** Now, recently, the computer lets you do mathematical computations that are  
**Translation:** 

**[3305.00s] English:** Sophisticated enough that nobody understands how the answers came out; right machine learning.  
**Translation:** Vocabulary: computations: 计算; mathematical: 数学的; sophisticated: 复杂的

**[3310.62s] English:** Machine learning: Yeah, it used to be that you get a dataset, you guess at a function, the function...  
**Translation:** 

**[3317.20s] English:** Is considered physics if it's predictive of new functions, new data sets, and modern applications.  
**Translation:** Vocabulary: dataset: 数据集; predictive: 预测性的

**[3323.48s] English:** You can take a large data set, and you can take a large data set, and you can take a large data set.  
**Translation:** 

**[3328.16s] English:** With no intuition about what it is, we use machine learning to find a pattern that has no function.  
**Translation:** Vocabulary: intuition: 直觉

**[3333.72s] English:** Right, and it can arrive at results that I don't know if they're completely mathematically.  
**Translation:** 

**[3339.00s] English:** Descriptive, so computation has kind of done something interesting compared to A = B + C.  
**Translation:** Vocabulary: computation: 计算; descriptive: 描述性; mathematically: 数学上

**[3347.08s] English:** There's something reminiscent of that step from the basic operations of addition.  
**Translation:** 

**[3354.68s] English:** To take a step towards neural networks that's reminiscent of what  
**Translation:** Vocabulary: neural: 神经; reminiscent: 类似

**[3358.04s] English:** We've been doing it for years and years and years and years and years and years and years and years.  
**Translation:** 

**[3358.10s] English:** And, year after year after year after year after year after year after year after year after year after year.  
**Translation:** 

**[3358.14s] English:** And, year after year for eons, life on Earth at its origins was...  
**Translation:** 

**[3360.00s] English:** Doing, do you think we're creating something that might be the next step in our evolution through creating artificial...?  
**Translation:** 

**[3365.92s] English:** Intelligence systems—that is, I don't know. There's so much in the universe already; it's hard.  
**Translation:** 

**[3371.34s] English:** To say where we stand, like in this whole thing, humans are working on additional abstraction.  
**Translation:** Vocabulary: abstraction: 抽象

**[3376.84s] English:** Layers and possibilities, yeah; it appears so. Does that mean that human beings don't need dogs?  
**Translation:** 

**[3383.14s] English:** Know, no, like, like, there are so many things that are simultaneously interesting and useful.  
**Translation:** 

**[3390.08s] English:** But you've seen throughout your career greater and greater levels of abstraction.  
**Translation:** 

**[3394.58s] English:** Built-in artificial machines, right? Do you think, when you look at humans, you think...  
**Translation:** 

**[3402.30s] English:** Look at all the life on Earth as a single organism, building this.  
**Translation:** 

**[3405.76s] English:** This machine can be understood with greater and greater levels of abstraction, do you think humans are the peak?  
**Translation:** Vocabulary: organism: 生物体

**[3412.10s] English:** The top  
**Translation:** 

**[3413.12s] English:** Of the food chain in this long arc of history on Earth, or do you think we're just somewhere in the  
**Translation:** 

**[3419.84s] English:** Middle are we? We are discussing the basic functional operations of a CPU, and a C++ program.  
**Translation:** 

**[3427.96s] English:** The Python program, or with a neural network—like, somebody's you know, people have calculated.  
**Translation:** Vocabulary: functional: 功能的

**[3432.76s] English:** Like, how many operations does the brain do? Something you know, I've seen the number 10 to...  
**Translation:** 

**[3437.10s] English:** The 18th, about a bunch of times, arrived differently. So, could you make a computer that did 10 to...  
**Translation:** 

**[3442.72s] English:** The 20th operation, yes, sure. Do you think we're going to do that now? Is there something magical?  
**Translation:** 

**[3449.16s] English:** About how brains compute things, I don't know. You know, my personal experience is interesting.  
**Translation:** Vocabulary: compute: 计算

**[3455.10s] English:** Because you know, you think you know how you think, and then you have all these ideas, and you can't  
**Translation:** 

**[3459.36s] English:** Figure out how they happened, and if you meditate, you know what you can be aware of.  
**Translation:** Vocabulary: meditate: 冥想

**[3467.02s] English:** It's interesting, so I don't know if brains are magical or not—you know, the physical...  
**Translation:** 

**[3472.72s] English:** Evidence says no, lots of people's personal experience says yes, so what would be funny—as if?  
**Translation:** 

**[3480.00s] English:** Brains are magical, and yet we can make brains with more computation. You know, I don't know what.  
**Translation:** 

**[3485.28s] English:** To say about that, but what do you think? Uh, magic is an emergent phenomenon. What would be... I have let.  
**Translation:** Vocabulary: computation: 计算; emergent: 涌现的

**[3491.78s] English:** Me, I have no explanation. Let me ask Jim Keller: In your view, what is consciousness?  
**Translation:** 

**[3497.34s] English:** With consciousness, yeah, like what, you know, consciousness, love things that are these.  
**Translation:** Vocabulary: consciousness: 觉醒

**[3506.32s] English:** Deeply human things that seem to emerge from our brain are that we'll be able to  
**Translation:** 

**[3511.38s] English:** Make codes in chips that get faster and faster and faster and faster—that's like a 10-hour process.  
**Translation:** 

**[3519.00s] English:** Conversation: Nobody really knows. Can you summarize it in a couple of words? Um, many people.  
**Translation:** 

**[3526.00s] English:** I have observed that organisms run at lots of different levels. Right? If you had two neurons,  
**Translation:** Vocabulary: neurons: 神经元; summarize: 概括

**[3532.30s] English:** Somebody said you'd have one sensory neuron and one motor neuron.  
**Translation:** 

**[3535.10s] English:** Right.  
**Translation:** Vocabulary: neuron: 神经元; sensory: 感觉的

**[3536.42s] English:** So, we move toward things and away from things, and we have physical integrity and safety—or not.  
**Translation:** 

**[3541.64s] English:** Right, and then if you look at the animal kingdom, you can see brains that are a little more  
**Translation:** 

**[3547.10s] English:** Complicated, and at some point there's a planning system, and then there's an emotional system that's  
**Translation:** 

**[3552.72s] English:** You know, we're happy about being safe or unhappy about being threatened, right? And then our brains have  
**Translation:** 

**[3559.22s] English:** Massive numbers of structures, you know, like planning, and movement, and thinking, and feeling.  
**Translation:** 

**[3565.48s] English:** And drive.  
**Translation:** 

**[3566.32s] English:** And emotions, and we seem to have multiple layers of thinking systems. We have a brain—and a dream.  
**Translation:** 

**[3572.38s] English:** System that nobody understands whatsoever, which I find completely hilarious, and  
**Translation:** Vocabulary: hilarious: 滑稽

**[3577.82s] English:** You can think of those systems as more independent, and you can observe them that way.  
**Translation:** 

**[3586.76s] English:** The different parts of yourself can observe them. I don't know which one's magical; I don't know which.  
**Translation:** 

**[3592.02s] English:** One's not computational, so  
**Translation:** 

**[3596.32s] English:** Is it possible that it's all computation?  
**Translation:** Vocabulary: computation: 计算; computational: 计算的

**[3598.88s] English:** Probably.  
**Translation:** 

**[3600.00s] English:** Is there a limit to computation?  
**Translation:** 

**[3601.50s] English:** I don't think so.  
**Translation:** 

**[3603.12s] English:** Do you think the universe is a computer?  
**Translation:** 

**[3607.04s] English:** It's a weird kind of computer.  
**Translation:** 

**[3609.24s] English:** Because if it were a computer,  
**Translation:** 

**[3612.16s] English:** Like when they do calculations on what it,  
**Translation:** 

**[3615.06s] English:** How much calculation does it take to describe quantum effects?  
**Translation:** 

**[3618.28s] English:** It is unbelievably high.  
**Translation:** 

**[3620.58s] English:** So, if it were a computer,  
**Translation:** Vocabulary: unbelievably: 难以置信地

**[3622.24s] English:** Wouldn't you have built it out of something?  
**Translation:** 

**[3623.44s] English:** That was easier to compute?  
**Translation:** Vocabulary: compute: 计算

**[3626.24s] English:** That's a funny system.  
**Translation:** 

**[3628.82s] English:** But then, the simulation guys have pointed out  
**Translation:** 

**[3631.26s] English:** That the rules are kind of interesting.  
**Translation:** 

**[3632.76s] English:** Like when you look really close, it's uncertain.  
**Translation:** 

**[3635.06s] English:** And the speed of light says you can only look so far.  
**Translation:** 

**[3637.56s] English:** And things can't be simultaneous.  
**Translation:** Vocabulary: simultaneous: 同时发生

**[3639.16s] English:** Except for the odd entanglement problem.  
**Translation:** 

**[3641.14s] English:** Where they seem to be.  
**Translation:** Vocabulary: entanglement: 纠缠

**[3642.50s] English:** Like the rules are all kind of weird.  
**Translation:** 

**[3645.10s] English:** And someone said, "Physics is like having 50 equations.  
**Translation:** Vocabulary: equations: 方程式

**[3648.68s] English:** With 50 variables, we need to define 50 variables.  
**Translation:** 

**[3652.28s] English:** Like, you know, it's you know,  
**Translation:** 

**[3655.20s] English:** Like physics itself has been a shit show.  
**Translation:** 

**[3656.90s] English:** For thousands of years.  
**Translation:** 

**[3658.82s] English:** It seems odd when you get to the corners of everything.  
**Translation:** 

**[3661.52s] English:** You know, it's either uncomputable.  
**Translation:** Vocabulary: uncomputable: 无法计算的

**[3663.52s] English:** Or undefined or uncertain.  
**Translation:** 

**[3667.28s] English:** It's almost like the designers of the simulation.  
**Translation:** Vocabulary: designers: 设计者; undefined: 未定义

**[3669.20s] English:** They are trying to prevent us from understanding it perfectly.  
**Translation:** 

**[3672.96s] English:** But also the things that require calculations.  
**Translation:** 

**[3675.96s] English:** Requires so much calculation.  
**Translation:** 

**[3677.56s] English:** That our idea of the universe of a computer is absurd.  
**Translation:** Vocabulary: absurd: 荒谬

**[3680.70s] English:** Because every single little bit of it  
**Translation:** 

**[3682.88s] English:** It takes all the computation in the universe to figure it out.  
**Translation:** Vocabulary: computation: 计算

**[3686.32s] English:** So, that's a weird kind of computer.  
**Translation:** 

**[3688.16s] English:** You know, you say,  
**Translation:** 

**[3688.66s] English:** The simulation is running on the computer.  
**Translation:** 

**[3690.80s] English:** Which has, by definition, infinite computation.  
**Translation:** Vocabulary: infinite: 无尽的

**[3694.46s] English:** Not infinite.  
**Translation:** 

**[3695.40s] English:** Oh, you mean if the universe is infinite?  
**Translation:** 

**[3697.52s] English:** Yeah.  
**Translation:** 

**[3698.28s] English:** Well, every little piece of our universe,  
**Translation:** 

**[3700.34s] English:** It seems to take an infinite amount of computation to figure out.  
**Translation:** 

**[3703.26s] English:** Not infinite, just a lot.  
**Translation:** 

**[3704.20s] English:** Well, a lot is a pretty big number.  
**Translation:** 

**[3706.08s] English:** Compute this little teeny spot.  
**Translation:** Vocabulary: compute: 计算; teeny: 微小的

**[3708.16s] English:** Takes all the mass in the local  
**Translation:** 

**[3711.02s] English:** One light year by one light year, space.  
**Translation:** 

**[3713.50s] English:** It's close enough to infinite.  
**Translation:** 

**[3714.96s] English:** Oh, it's a heck of a computer if it is one.  
**Translation:** 

**[3716.58s] English:** I know.  
**Translation:** 

**[3716.94s] English:** It's weird.  
**Translation:** 

**[3718.66s] English:** It's a weird description.  
**Translation:** 

**[3720.00s] English:** The simulation description seems to break when you look closely at it, but the rules of the  
**Translation:** 

**[3725.52s] English:** The universe seems to imply something's up, that seems a little arbitrary. The whole...  
**Translation:** 

**[3732.40s] English:** Thing, the laws of physics, yeah. It just seems like, how did it come out to be? Yeah, the way.  
**Translation:** Vocabulary: arbitrary: 随意的

**[3739.60s] English:** It is, but lots of people talk about that. It's you know, it's like I said, the two smartest groups of  
**Translation:** 

**[3744.00s] English:** Humans are working on the same problem from different aspects, and they're both  
**Translation:** 

**[3748.16s] English:** Complete failures, so that's kind of cool. They might succeed eventually, well after.  
**Translation:** 

**[3755.84s] English:** Two thousand years, the trend isn't good. Oh, two thousand years is nothing in the span of history.  
**Translation:** 

**[3760.40s] English:** History of the universe: so, we have some time, but the next thousand years don't look good either.  
**Translation:** 

**[3765.20s] English:** So, that's what everybody says at every stage, but uh, with Moore's Law as you've just described, not  
**Translation:** 

**[3771.52s] English:** Being dead, the exponential growth of technology makes the future seem pretty incredible. Well, it'll be  
**Translation:** 

**[3778.08s] English:** A little bit different, but it's a little bit different, but it's a little bit different.  
**Translation:** Vocabulary: exponential: 指数的

**[3778.14s] English:** Interesting, that's for sure. That's right. So, what are your thoughts on Ray Kurzweil's sense that?  
**Translation:** 

**[3783.90s] English:** Exponential improvement in technology will continue indefinitely, that is how you see it.  
**Translation:** Vocabulary: indefinitely: 无期限地

**[3789.18s] English:** Moore's Law, do you see Moore's law more broadly in the sense that technology of all kinds?  
**Translation:** 

**[3796.86s] English:** Has a way of stacking S-curves on top of each other, where it'll be exponential and  
**Translation:** Vocabulary: broadly: 广泛地; stacking: 叠加

**[3803.18s] English:** Then we'll see all kinds of what an exponential of a million means—that's that's  
**Translation:** 

**[3808.06s] English:** A pretty amazing number, and that's just for a local little piece of silicon. Now, let's imagine you say.  
**Translation:** 

**[3814.46s] English:** Decided to get a thousand tons of silicon to collaborate in one computer, at a million times.  
**Translation:** 

**[3822.30s] English:** The density, like now—now you're talking—I don't know, 10 to the 20th more computational power.  
**Translation:** Vocabulary: collaborate: 合作; computational: 计算的; density: 密度; silicon: 硅

**[3829.66s] English:** Than our current, already unbelievably fast computers.  
**Translation:** 

**[3833.90s] English:** Like, nobody knows what that's going to mean. You know, the sci-fi guy is called "computronium.  
**Translation:** Vocabulary: unbelievably: 难以置信地

**[3838.06s] English:** Like when  
**Translation:** 

**[3840.00s] English:** A local civilization turns the nearby star into a computer, right? I don't think that's true, but...  
**Translation:** 

**[3846.64s] English:** So, just when you shrink a transistor, that's only one dimension; the ripple effects of this can be significant.  
**Translation:** 

**[3853.68s] English:** That, like, people tend to think about computers as a cost problem—right? So, computers are made  
**Translation:** Vocabulary: dimension: 维度; ripple: 影响; shrink: 缩小; transistor: 晶体管

**[3858.48s] English:** Out of silicon and minor amounts of metals, and you know, this and that—none of those things cost.  
**Translation:** 

**[3865.68s] English:** Any money, like there's plenty of sand; you could just turn the beach a little bit.  
**Translation:** 

**[3871.60s] English:** Ocean water into computers, so all the cost is in the equipment to do it, and the trend on equipment.  
**Translation:** 

**[3877.84s] English:** Is it true that once you figure out how to build the equipment, the trend of cost is zero? Elon said, "First you...  
**Translation:** 

**[3882.72s] English:** Figure out what configuration you want the atoms in, and then how to put them there, right? Yes.  
**Translation:** 

**[3890.80s] English:** Because, well, what's his great insight is that people are how.  
**Translation:** Vocabulary: configuration: 结构设置

**[3895.68s] English:** To build a computer, and they're not constrained. I have this thing; I know how it works, and then...  
**Translation:** 

**[3901.84s] English:** Little tweaks to that will generate something, as opposed to what I actually want, and then.  
**Translation:** Vocabulary: constrained: 受限制; tweaks: 小调整

**[3907.36s] English:** Figure out how to build it; it's a very different mindset, and almost nobody has it, obviously.  
**Translation:** 

**[3914.32s] English:** Well, let me ask about that topic. You were one of the key early people in the development of autopilot.  
**Translation:** Vocabulary: mindset: 思维模式

**[3921.36s] English:** At least, on the hardware side, Elon Musk believes that autopilot and vehicle autonomy can be achieved if you just  
**Translation:** 

**[3925.60s] English:** Look at that problem; it can follow this kind of exponential improvement in terms of the HA the.  
**Translation:** Vocabulary: autonomy: 自主性; exponential: 指数的

**[3930.88s] English:** How about that question? We're talking about it, so there's no reason why you can't share your thoughts. What are your thoughts?  
**Translation:** 

**[3935.60s] English:** On this particular space of vehicle autonomy, and you're a part of it, and Elon Musk's and Tesla's.  
**Translation:** 

**[3943.92s] English:** Vision for the computer you needed to build was straightforward, and you could argue that it was well-designed.  
**Translation:** 

**[3950.00s] English:** It needs to be at least two times faster, or five times, or ten times, but that's just a matter of fact.  
**Translation:** 

**[3955.60s] English:** Time or price in the short run; so that's not a big deal.  
**Translation:** 

**[3960.00s] English:** You don't have to be especially smart to drive a car.  
**Translation:** 

**[3963.18s] English:** So, it's not like a super-hard problem.  
**Translation:** 

**[3965.72s] English:** I mean, the big problem with safety is attention.  
**Translation:** 

**[3967.88s] English:** Which computers are really good at, not skills.  
**Translation:** 

**[3972.68s] English:** Well, let me push back on that one.  
**Translation:** 

**[3975.30s] English:** You say that everything you said is correct.  
**Translation:** 

**[3976.88s] English:** But we, as humans, tend to take for granted.  
**Translation:** 

**[3984.18s] English:** How incredible our vision system is.  
**Translation:** 

**[3987.44s] English:** You can drive a car with 20-50 vision.  
**Translation:** 

**[3990.56s] English:** And you can train a neural network.  
**Translation:** 

**[3992.04s] English:** To extract the distance of any object,  
**Translation:** Vocabulary: extract: 提取; neural: 神经

**[3994.56s] English:** And the shape of any surface from a video and data.  
**Translation:** 

**[3998.76s] English:** It's really simple.  
**Translation:** 

**[4000.26s] English:** No, it's not simple.  
**Translation:** 

**[4001.72s] English:** That's a simple data problem.  
**Translation:** 

**[4003.98s] English:** It's not simple.  
**Translation:** 

**[4007.86s] English:** Because it's not just detecting objects.  
**Translation:** Vocabulary: detecting: 检测

**[4010.52s] English:** It's understanding the scene.  
**Translation:** 

**[4012.34s] English:** And it's being able to do it in a way that doesn't make errors.  
**Translation:** 

**[4016.58s] English:** So, the beautiful thing about the human vision system.  
**Translation:** 

**[4019.40s] English:** Is...  
**Translation:** 

**[4020.00s] English:** And our entire brain is around the whole thing.  
**Translation:** 

**[4022.22s] English:** We are able to fill in the gaps.  
**Translation:** 

**[4025.24s] English:** It's not just about perfectly detecting cars.  
**Translation:** 

**[4028.00s] English:** It's inferring the occluded cars.  
**Translation:** Vocabulary: inferring: 推断; occluded: 被遮挡的

**[4030.06s] English:** It's trying to....  
**Translation:** 

**[4030.70s] English:** It's understanding the physics.  
**Translation:** 

**[4032.28s] English:** I think that's mostly a data problem.  
**Translation:** 

**[4034.46s] English:** So, you think what data would compute?  
**Translation:** Vocabulary: compute: 计算

**[4037.42s] English:** With improvements in computation,  
**Translation:** 

**[4039.20s] English:** With improvement in collection?  
**Translation:** Vocabulary: computation: 计算

**[4040.68s] English:** Well, there is a....  
**Translation:** 

**[4041.36s] English:** When you're driving a car and somebody cuts you off,  
**Translation:** 

**[4043.62s] English:** Your brain has theories about why they did it.  
**Translation:** 

**[4046.16s] English:** They're a bad person.  
**Translation:** 

**[4047.50s] English:** They're distracted.  
**Translation:** 

**[4048.64s] English:** They're dumb.  
**Translation:** Vocabulary: distracted: 分心的

**[4050.00s] English:** You know, you can listen to yourself.  
**Translation:** 

**[4051.92s] English:** Right.  
**Translation:** 

**[4052.74s] English:** So, you know, if you think that narrative is important,...  
**Translation:** 

**[4056.88s] English:** To be able to successfully drive a car,  
**Translation:** 

**[4058.86s] English:** Then, current autopilot systems can't do it.  
**Translation:** 

**[4061.66s] English:** But if cars are ballistic things with tracks,  
**Translation:** Vocabulary: ballistic: 弹道的

**[4064.28s] English:** And probabilistic changes in speed and direction,  
**Translation:** 

**[4067.30s] English:** And roads are fixed and given, by the way.  
**Translation:** Vocabulary: probabilistic: 概率性的

**[4069.90s] English:** They don't change dynamically, right?  
**Translation:** 

**[4073.22s] English:** You can map the world really thoroughly.  
**Translation:** Vocabulary: thoroughly: 详细地

**[4075.52s] English:** You can place every object really thoroughly.  
**Translation:** 

**[4080.00s] English:** Right, you can calculate trajectories of things really thoroughly, right? But everything you said,...  
**Translation:** Vocabulary: trajectories: 轨迹

**[4088.42s] English:** About really thoroughly having a different degree of difficulty, so you could say, at some point,  
**Translation:** 

**[4094.66s] English:** Computer autonomous systems will be way better at things that humans are lousy at, like they'll be  
**Translation:** Vocabulary: autonomous: 自主的

**[4100.98s] English:** Better at attention, they'll always remember there was a pothole in the road that humans keep.  
**Translation:** 

**[4105.84s] English:** Forgetting about it, they'll remember that this set of roads has these weird lines on it.  
**Translation:** Vocabulary: pothole: 道路坑洞

**[4111.62s] English:** Computers figured out once, and especially if they get updates. So, if somebody changes a given...  
**Translation:** 

**[4116.88s] English:** Right, like the key to robots and stuff, someone said, is to maximize the given resources.  
**Translation:** Vocabulary: maximize: 最大化

**[4123.76s] English:** Right, right, right. So, having a robot pick up this bottle cap is way easier than putting a red dot.  
**Translation:** 

**[4129.18s] English:** On the top, because then you have to figure out what you know, and if you want to do a certain thing.  
**Translation:** 

**[4134.06s] English:** With it, you know, maximize the given opportunities.  
**Translation:** 

**[4135.84s] English:** Is the thing, and autonomous systems are happily maximizing the givens, like humans, when you  
**Translation:** Vocabulary: maximizing: 最大化

**[4142.42s] English:** Drive somewhere new, and you remember it because you're processing it the whole time, and after.  
**Translation:** 

**[4147.18s] English:** The 50th time you drove to work, you got to work, and you don't know how you got there. Right? You're on.  
**Translation:** 

**[4151.72s] English:** Autopilot, right? Autonomous cars are always on autopilot, but the cars have no theories about.  
**Translation:** 

**[4159.16s] English:** Why they got cut off or why they're in traffic, so they also never stop paying attention, right? So  
**Translation:** 

**[4165.84s] English:** I tend to believe you do have to have theories or mental models of other people.  
**Translation:** 

**[4169.54s] English:** Uh, especially with pedestrians and cyclists, but also with other cars—so, everything you said.  
**Translation:** 

**[4175.54s] English:** Is actually essential to driving, which is a lot more complicated than people think.  
**Translation:** 

**[4181.02s] English:** Realize, I think, so sort of to push back slightly, but to cut into traffic — right? You can't just.  
**Translation:** 

**[4187.50s] English:** Wait for a gap; you have to be somewhat aggressive. You'll be surprised how simple the calculation is.  
**Translation:** 

**[4192.22s] English:** That is, I may be on that particular point, but there are a lot of people who are trying to figure it out.  
**Translation:** 

**[4195.18s] English:** What's going on in the city, and they're trying to figure it out.  
**Translation:** 

**[4195.68s] English:** Trying to figure out what's going on in the city, and they're trying to figure out what's going on in the city, and they're  
**Translation:** 

**[4195.84s] English:** Trying to figure out what's going on in the city, and they're trying to figure out what's going on in the city.  
**Translation:** 

**[4196.64s] English:** Yeah, I think what's going on in the city is that I like that sense of strife too.  
**Translation:** Vocabulary: strife: 争端

**[4200.00s] English:** Back, I would be surprised, you know? Yeah, I'll just say where I stand: I would be very surprised.  
**Translation:** 

**[4204.06s] English:** But I think it's you might be surprised how complicated it is. That I say, I tell people.  
**Translation:** 

**[4210.62s] English:** Like progress disappoints in the short run, but surprises in the long run; it's very possible.  
**Translation:** 

**[4214.80s] English:** Yeah, I suspect in 10 years it'll be just taken for granted, yeah, probably, but you're probably  
**Translation:** Vocabulary: disappoints: 让人失望

**[4221.16s] English:** Right, and I'll look like it's going to be a 50/50 solution that nobody cares about. It's like GPS.  
**Translation:** 

**[4225.70s] English:** Is like, wow, GPS is we have satellites in space, yeah, that tell you where your location is; it was  
**Translation:** 

**[4231.22s] English:** A really big deal, now everything has a GPS in it, yeah, that's true, but I do think that systems...  
**Translation:** 

**[4235.90s] English:** That involves human behavior are more complicated than we give them credit for, so we can do  
**Translation:** 

**[4241.90s] English:** Incredible things with technology that don't involve humans, but when you think humans are  
**Translation:** 

**[4246.06s] English:** Less complicated than people you know frequently ascribe, maybe I feel we tend to operate out of.  
**Translation:** Vocabulary: ascribe: 归因

**[4252.44s] English:** Large numbers of patterns, and just keep doing it over and over.  
**Translation:** 

**[4255.70s] English:** But I can't trust you because you're a human—that's something a human would say.  
**Translation:** 

**[4260.24s] English:** But my hope is on the point you've made: even if nobody is right, even there, I'm hoping that.  
**Translation:** 

**[4269.80s] English:** There are a lot of things that humans aren't good at that machines are definitely good at, like you  
**Translation:** 

**[4273.62s] English:** Said, "Attention and things like that will be so much better, making the overall picture much clearer.  
**Translation:** 

**[4278.78s] English:** Safety and autonomy will be obviously key, as cars will be safer even if they're not as good. I'm a big  
**Translation:** Vocabulary: autonomy: 自主权

**[4285.04s] English:** Believer in safety.  
**Translation:** 

**[4285.70s] English:** I mean, there are already current safety systems like cruise control that don't let  
**Translation:** Vocabulary: believer: 信仰者

**[4291.06s] English:** You run into people and lane-keeping; there are so many features that you just look at the Pareto.  
**Translation:** 

**[4296.54s] English:** Accidents and knocking off like 80% of them is, you know, super doable; just to linger on the  
**Translation:** Vocabulary: doable: 可行; linger: 逗留; pareto: 帕累托图

**[4303.76s] English:** The autopilot team and their efforts seem to be very intense.  
**Translation:** 

**[4310.56s] English:** Scrutiny by the media and the public, in terms of safety, puts pressure on the bar.  
**Translation:** Vocabulary: scrutiny: 审视

**[4315.70s] English:** And the safety of the vehicle, and the safety of the vehicle, and the safety of the vehicle.  
**Translation:** 

**[4320.00s] English:** There, they are working on the hardware and trying to build a system that builds a safe vehicle, and so on.  
**Translation:** 

**[4326.46s] English:** What was your sense about that pressure—is it unfair, is it expected of new technology?  
**Translation:** 

**[4331.54s] English:** Yeah, it seems reasonable. I was interested, so I talked to both American and European regulators.  
**Translation:** 

**[4336.46s] English:** And I was worried that the regulations would write into the rules technology solutions.  
**Translation:** 

**[4344.38s] English:** Like modern brake systems imply hydraulic brakes, so if you read the regulations, they meet the letter.  
**Translation:** 

**[4353.14s] English:** Of the law for brakes, it sort of has to be hydraulic, right? And the regulator said they're  
**Translation:** 

**[4359.66s] English:** They're interested in the use cases, like a head-on crash, an offset crash; don't hit pedestrians.  
**Translation:** Vocabulary: hydraulic: 液压; offset: 偏置; pedestrians: 行人; regulator: 调节器

**[4365.90s] English:** Run into people; don't leave the road, don't run a red light or a stoplight. They were very much into it.  
**Translation:** 

**[4371.32s] English:** The scenarios, and you know, and they had.  
**Translation:** Vocabulary: scenarios: 情景; stoplight: 信号灯

**[4374.38s] English:** They had all the data about which scenarios injured or killed the most people.  
**Translation:** 

**[4379.26s] English:** And, for the most part, those conversations were like, "What's the right thing to do to take the?  
**Translation:** 

**[4387.10s] English:** Next, Elon is very interested in the benefits of autonomous driving or freeing.  
**Translation:** 

**[4393.34s] English:** People's time and attention, as well as safety, is also an interesting thing, but...  
**Translation:** Vocabulary: autonomous: 自主的

**[4401.74s] English:** You know, building autonomous systems,...  
**Translation:** 

**[4404.38s] English:** They're safe and safer than people seem, since the goal is to be tangibly safer than people.  
**Translation:** Vocabulary: tangibly: 实实在在地

**[4409.98s] English:** Having the bar set to be safer than people and scrutinizing accidents seems  
**Translation:** 

**[4415.26s] English:** Philosophically, you know, it's correct, so I think that's a good thing. What is different than the?  
**Translation:** Vocabulary: philosophically: 从哲学角度看; scrutinizing: 审查

**[4424.54s] English:** Things that you worked on at Intel, AMD, and Apple, including autopilot chip design and hardware design.  
**Translation:** 

**[4433.26s] English:** What are interesting or  
**Translation:** 

**[4434.38s] English:** Challenging aspects of building this specialized kind of computing system in the automotive space.  
**Translation:** 

**[4440.00s] English:** I mean, there are two tricks to building an automotive computer.  
**Translation:** Vocabulary: automotive: 汽车相关的; computing: 计算

**[4442.76s] English:** One is the software team, the machine learning team,  
**Translation:** 

**[4446.94s] English:** Is developing algorithms that are changing rapidly.  
**Translation:** 

**[4450.56s] English:** So, as you're building the accelerator,...  
**Translation:** 

**[4454.06s] English:** You have this worry or intuition that the algorithms will change enough.  
**Translation:** Vocabulary: accelerator: 加速器; intuition: 直觉

**[4458.40s] English:** That the accelerator will be the wrong one.  
**Translation:** 

**[4462.48s] English:** And there's the generic thing.  
**Translation:** Vocabulary: generic: 通用的

**[4464.62s] English:** Which is, if you build a really good general-purpose computer,  
**Translation:** 

**[4467.22s] English:** Say its performance is one.  
**Translation:** 

**[4468.96s] English:** And then, GPU guys will deliver about 5x the performance.  
**Translation:** 

**[4473.36s] English:** For the same amount of silicon,  
**Translation:** 

**[4475.74s] English:** Because instead of discovering parallelism, you're given parallelism.  
**Translation:** 

**[4479.28s] English:** And then special accelerators get another 2 to 5x on top of a GPU.  
**Translation:** Vocabulary: accelerators: 加速器

**[4485.42s] English:** Because you say, "I know the math is always 8-bit integers.  
**Translation:** 

**[4488.76s] English:** Into 32-bit accumulators.  
**Translation:** Vocabulary: accumulators: 累加器; integers: 整数

**[4491.04s] English:** And the operations are a subset of mathematical possibilities.  
**Translation:** 

**[4495.16s] English:** So, you know, AI accelerators have a,  
**Translation:** Vocabulary: mathematical: 数学的

**[4498.96s] English:** Claimed performance benefit over GPUs.  
**Translation:** 

**[4501.72s] English:** Because, in the narrow math space, you're nailing the algorithm.  
**Translation:** Vocabulary: algorithm: 算法; nailing: 攻克

**[4507.08s] English:** Now, you still try to make it programmable.  
**Translation:** 

**[4510.00s] English:** But the AI field is changing really fast.  
**Translation:** 

**[4513.24s] English:** So there's a little creative tension there, you know.  
**Translation:** 

**[4517.26s] English:** I want the acceleration afforded by specialization.  
**Translation:** Vocabulary: acceleration: 加速; afforded: 提供

**[4520.56s] English:** Without becoming overly specialized, so that the new algorithm is much more effective.  
**Translation:** 

**[4525.54s] English:** That you would have been better off on a GPU.  
**Translation:** Vocabulary: overly: 过于

**[4527.90s] English:** So, there is a tension there.  
**Translation:** 

**[4529.60s] English:** To build a good computer for an application like automotive,  
**Translation:** Vocabulary: automotive: 汽车相关的

**[4534.06s] English:** There are all kinds of sensor inputs, safety processors, and a bunch of stuff.  
**Translation:** 

**[4539.14s] English:** So, one of Elon's goals is to make it super affordable.  
**Translation:** Vocabulary: affordable: 易负担的; inputs: 输入; processors: 处理器; sensor: 传感器

**[4542.18s] English:** So, every car gets an autopilot computer.  
**Translation:** 

**[4544.80s] English:** So, some of the recent startups you look at,  
**Translation:** Vocabulary: startups: 新兴企业

**[4546.48s] English:** And they have a server in the trunk.  
**Translation:** 

**[4548.28s] English:** Because they're saying, "I'm going to build this autopilot computer.  
**Translation:** 

**[4550.58s] English:** That replaces the driver.  
**Translation:** 

**[4552.16s] English:** So their cost budget is $10,000 or $20,000.  
**Translation:** 

**[4555.10s] English:** And Elon's constraint was: I'm going to put one in every car.  
**Translation:** 

**[4558.68s] English:** Whether people buy autopilot or not,  
**Translation:** Vocabulary: constraint: 限制

**[4560.00s] English:** Him striping, or not—so the cost constraint he had in mind was great, right—and to hit that.  
**Translation:** 

**[4566.72s] English:** You had to think about the system design; that's complicated, it's fun, you know, it's like...  
**Translation:** Vocabulary: striping: 条带化

**[4570.72s] English:** It's like Krestmann's work, like you know, a violin maker—right? You can say Stradivarius.  
**Translation:** 

**[4575.44s] English:** Is this incredible thing? The musicians are incredible, but the guy making the violin you  
**Translation:** Vocabulary: stradivarius: 斯特拉迪瓦里小提琴

**[4580.16s] English:** Know, he picked the wood, sanded it, and then he cut it. You know, and he glued it. You know, and he waited.  
**Translation:** 

**[4586.24s] English:** For the right day, so that when you put the finishing touches on it, you don't know, do something dumb that's  
**Translation:** Vocabulary: glued: 粘合; sanded: 打磨

**[4591.68s] English:** Craftsman's work, right? You may be a genius craftsman because you have the best techniques.  
**Translation:** 

**[4596.64s] English:** And you discover a new one, but most engineers' craftsmanship and humans really like to do that.  
**Translation:** Vocabulary: craftsman: 手工艺人; craftsmanship: 手工技艺

**[4604.08s] English:** You know, smart humans aren't everybody; all humans aren't like that. I don't know; I used to dig ditches when I was in.  
**Translation:** 

**[4609.84s] English:** College, I got really good at it. Satisfying, yeah! So, digging dishes is also a craft, yeah, of course.  
**Translation:** Vocabulary: ditches: 水沟

**[4616.88s] English:** Oh, so there's an expression called "complex mastery behavior." So when you're learning something,...  
**Translation:** 

**[4621.92s] English:** That's fun because you're learning something when you do something; it's road and simple, it's not.  
**Translation:** Vocabulary: mastery: 精通

**[4625.84s] English:** That's satisfying, but if the steps that you have to do are complicated and you're good at them.  
**Translation:** 

**[4631.68s] English:** It's satisfying to do them, and then if you're intrigued by it all as you're doing them, you  
**Translation:** Vocabulary: intrigued: 好奇

**[4637.68s] English:** Sometimes, you can learn new things that will help you raise your game, but Krestman's work is good and engineers.  
**Translation:** 

**[4645.04s] English:** Like engineering is complex.  
**Translation:** 

**[4646.24s] English:** Complicated enough that you have to learn a lot of skills, and then a lot of what you do is then  
**Translation:** 

**[4650.74s] English:** Craftsman's work, which is fun: autonomous driving, building a very resource-constrained computer, so  
**Translation:** Vocabulary: autonomous: 自主

**[4657.92s] English:** The computer has to be cheap enough to put in every single car, which essentially boils down to:  
**Translation:** 

**[4663.10s] English:** Craftsman's work is engineering, you know—there's thoughtful decisions and problems to solve, and  
**Translation:** Vocabulary: thoughtful: 周到的

**[4669.08s] English:** Trade-offs to make: do you need 10 camera imports, or eight? You know, you're building for the current...  
**Translation:** 

**[4674.18s] English:** Car: The next one, you know, how do you do the safety stuff? You know, there's a whole bunch of it.  
**Translation:** Vocabulary: imports: 进口

**[4679.24s] English:** Details.  
**Translation:** 

**[4680.00s] English:** But it's fun, but it's not like I'm building a new type of neural network which has a new  
**Translation:** Vocabulary: neural: 神经的

**[4685.28s] English:** Mathematics and a new computer to work — you know, that's like there's more invention.  
**Translation:** 

**[4690.74s] English:** Than that, but the rejection to practice once you pick the architecture, you look inside and what do?  
**Translation:** Vocabulary: rejection: 拒绝

**[4696.36s] English:** You see, adders, multipliers, and memories, and you know the basics. So computers are always like this.  
**Translation:** 

**[4703.38s] English:** This weird set of abstraction layers, ideas, and thinking reduces to practice.  
**Translation:** Vocabulary: abstraction: 抽象; adders: 加法器; multipliers: 乘法器

**[4708.62s] English:** Is it transistors and wires, and you know, pretty basic stuff? And that's an interesting phenomenon.  
**Translation:** 

**[4716.02s] English:** By the way, that kind of factory work, like a lot of people think factory work is just about assembling things on an assembly line.  
**Translation:** Vocabulary: assembling: 组装; transistors: 晶体管

**[4721.66s] English:** I've been on the assembly line, and like the people who work there, I really like it; it's a really great job.  
**Translation:** 

**[4727.30s] English:** It's really complicated putting cars together; it's hard, right? And the car is moving, and the parts.  
**Translation:** 

**[4732.84s] English:** Are moving, and sometimes the parts get damaged, and you have to coordinate putting all the stuff back together.  
**Translation:** 

**[4736.98s] English:** Together, and people are good at it.  
**Translation:** Vocabulary: coordinate: 协调

**[4738.62s] English:** They're good at it, and I remember one day I went to work and the line was shut down for some reason.  
**Translation:** 

**[4743.78s] English:** And some of the guys sitting around were really bummed because they had reorganized a bunch.  
**Translation:** Vocabulary: bummed: 沮丧; reorganized: 重新组织

**[4748.66s] English:** Of stuff, and they were going to hit a new record for the number of cars built that day, and they  
**Translation:** 

**[4752.98s] English:** We were all gung-ho to do it, and these were big, tough guys, and you know, but what they did.  
**Translation:** 

**[4758.36s] English:** Was complicated, and you couldn't do it. Yeah, and I mean, well, after a while, you could, but you'd have...  
**Translation:** 

**[4763.24s] English:** To work your way up, because you know, like putting on the brights.  
**Translation:** 

**[4768.62s] English:** The trim on a car on a moving assembly line, where it has to be attached 25 places in a minute and a...  
**Translation:** 

**[4775.20s] English:** Half of it is unbelievably complicated, and humans can do it — it's really good, I think that's.  
**Translation:** Vocabulary: unbelievably: 难以置信地

**[4782.86s] English:** Harder than driving a car, by the way. Putting together working parts in a factory, uh, too.  
**Translation:** 

**[4788.80s] English:** Smart people can disagree, yeah. I think driving a car? Well, we'll get you in the factory someday, and...  
**Translation:** 

**[4796.28s] English:** Then we'll see how you do not for us, humans, driving a car. I think it's a good idea to do it.  
**Translation:** 

**[4798.62s] English:** A car is easy, I'm saying.  
**Translation:** 

**[4800.00s] English:** Building a machine that drives a car is not easy, okay? Driving a car is easy for humans.  
**Translation:** 

**[4807.34s] English:** Because we've been evolving for billions of years, drive cars, yeah, I noticed the paleontologist with the cars.  
**Translation:** Vocabulary: evolving: 进化; paleontologist: 古生物学家

**[4814.44s] English:** Are super cool, oh! Now you join the rest of the internet mocking me, okay? I just... yeah, yeah.  
**Translation:** 

**[4823.26s] English:** Intrigued by your, you know, your anthropology? Yeah, it's uh, I have to go dig into that there's  
**Translation:** Vocabulary: anthropology: 人类学; intrigued: 好奇; mocking: 嘲笑

**[4829.14s] English:** Some inaccuracies there, yes. Okay, but in general, what have you learned in terms of thinking about?  
**Translation:** 

**[4840.18s] English:** Passion, craftsmanship, tension, chaos — you know, the whole mess of it. What have you learned?  
**Translation:** Vocabulary: craftsmanship: 技艺; inaccuracies: 不准确之处

**[4852.06s] English:** Have taken away from your time working with Elon Musk at Tesla, which is known to be a place  
**Translation:** 

**[4859.12s] English:** Of chaos, innovation, and craftsmanship, and I really like the way he thought; you think you have  
**Translation:** 

**[4866.90s] English:** An understanding about what first principles of something is, and then you talk to Elon about it.  
**Translation:** 

**[4871.50s] English:** And you didn't scratch the surface, you know; he has a deep belief that no matter what,  
**Translation:** 

**[4878.18s] English:** Do is a local maximum, right? And I had a friend who invented a better electric motor, and uh,  
**Translation:** 

**[4884.94s] English:** It was much better than what we were using, and one day he came by and said, "You know, I'm  
**Translation:** 

**[4889.12s] English:** A little disappointed because, you know, this is really great, and you didn't seem that impressed.  
**Translation:** 

**[4893.18s] English:** And I said, "You know, when the super-intelligent aliens come, are they going to be looking for you?  
**Translation:** Vocabulary: aliens: 外星人

**[4898.28s] English:** Like, where is he? The guy who built the motor, yeah, probably not, you know? Like, like, the like.  
**Translation:** 

**[4906.04s] English:** But doing interesting work that's both innovative and, let's say, a craftsman's work on the current.  
**Translation:** Vocabulary: innovative: 创新的

**[4911.24s] English:** The thing is really satisfying, and it's good. And that's cool. Then Elon was good taking.  
**Translation:** 

**[4919.12s] English:** Like, what's the deep  
**Translation:** 

**[4920.00s] English:** First, let's be clear: you know, you know, you know, that that.  
**Translation:** 

**[4926.40s] English:** You know, the ability to look at it without assumptions and how constraints are super wild.  
**Translation:** Vocabulary: assumptions: 前提; constraints: 限制

**[4934.08s] English:** You know, we build a rocket ship and use that same car, and you know, everything—and that's super fun!  
**Translation:** 

**[4940.72s] English:** And he's into it, too. Like when they first landed two SpaceX rockets on Tesla, we had a video.  
**Translation:** Vocabulary: rockets: 火箭

**[4946.72s] English:** Projector in the big room, and like 500 people came down; when they landed, everybody cheered.  
**Translation:** 

**[4951.20s] English:** And some people cried, "It was so cool!" Yeah, all right, but how did you do that? Well, it was super.  
**Translation:** Vocabulary: projector: 投影仪

**[4958.72s] English:** Hard, and then people say, "Well, it's chaotic really to get out of all your assumptions you think.  
**Translation:** 

**[4964.80s] English:** That's not going to be unbelievably painful, and is Elong tough, yeah. Probably the people will look back on.  
**Translation:** Vocabulary: chaotic: 混乱; elong: 拉长; unbelievably: 难以置信地

**[4976.72s] English:** That experience to go take apart so many layers of assumptions can be super fun, sometimes.  
**Translation:** 

**[4984.24s] English:** Painful, so it could be emotionally and intellectually painful throughout the entire process.  
**Translation:** Vocabulary: intellectually: 在智力上

**[4988.64s] English:** Is just stripping away assumptions, yeah. Imagine 99% of your thought process is protecting your  
**Translation:** 

**[4994.24s] English:** Self-conception, and 98% of that is wrong. Yeah, now you've got the math right. How do you think?  
**Translation:** Vocabulary: stripping: 去除

**[5002.88s] English:** You're feeling when you get back into that one bit that's useful.  
**Translation:** 

**[5006.72s] English:** And now you're open, and you have the ability to do something different.  
**Translation:** 

**[5012.40s] English:** I don't know if I got the math right; it might be 99.9%.  
**Translation:** 

**[5016.24s] English:** It ain't 50%. Imagining it's 50% is hard enough, yeah.  
**Translation:** 

**[5024.08s] English:** Now, for a long time, I've suspected you could get better — like you can think better.  
**Translation:** 

**[5030.00s] English:** More clearly, you can take things apart, and there are lots of examples of that—people who do that.  
**Translation:** Vocabulary: suspected: 怀疑

**[5036.72s] English:** So, and Elon is an example.  
**Translation:** 

**[5040.00s] English:** Of that, apparently, you are an example, so I don't know if I am fun to talk to.  
**Translation:** 

**[5046.48s] English:** Certainly, I've learned a lot of stuff. Right, well, here's the other thing: it's like I joke, like  
**Translation:** 

**[5051.44s] English:** I read books, and people think, "Oh, you read books? Well, no, I've read a couple of books a week for 55.  
**Translation:** 

**[5059.12s] English:** Years, wow! Well, maybe fifty because I didn't learn to read until I was eight or something.  
**Translation:** 

**[5063.52s] English:** And, uh, and it turns out that when people write books, they often take 20 years of their life where they  
**Translation:** 

**[5071.52s] English:** Passionately, I did something and reduced it to 200 pages — that's kind of fun. Then, you go online and...  
**Translation:** 

**[5079.04s] English:** You can find out who wrote the best books, and who, you know, is kind of wild. So, there's this...  
**Translation:** Vocabulary: passionately: 充满热情地

**[5083.92s] English:** Wild selection process, and then you can read it and, for the most part, understand it, and then you  
**Translation:** 

**[5090.26s] English:** Can go apply it, like I went to one company I thought  
**Translation:** 

**[5093.52s] English:** I haven't managed much before, so I read 20 management books and I started talking to  
**Translation:** 

**[5098.42s] English:** They and basically compared to all the VPS running around, I'd run Night Read 19 more management books.  
**Translation:** 

**[5104.14s] English:** Than anybody else, it wasn't even that hard, and half the stuff worked on the first try.  
**Translation:** 

**[5111.42s] English:** Even rocket science, but at the core of that is questioning the assumptions—or sort of entering.  
**Translation:** Vocabulary: assumptions: 前提

**[5119.34s] English:** The thinking, first-person principles, thinking sort of looking at the  
**Translation:** 

**[5123.52s] English:** The reality of the situation, and using that knowledge to apply it, so yeah, so I  
**Translation:** 

**[5129.36s] English:** Would say my brain has this idea that you can question first assumptions, and but I can go days  
**Translation:** 

**[5136.88s] English:** At a time, and forget that; and you have to kind of circle back to that observation because it is...  
**Translation:** 

**[5143.36s] English:** Because it's hard and challenging. Well, it's hard to just keep it front and center because you know.  
**Translation:** 

**[5147.82s] English:** You operate on so many levels all the time, and you know, getting this done takes priority or...  
**Translation:** 

**[5153.52s] English:** You know, being happy takes priority, or you know, screwing around takes priority, like  
**Translation:** 

**[5160.00s] English:** Like, how you go through life is complicated.  
**Translation:** Vocabulary: screwing: 胡闹

**[5162.64s] English:** Yeah.  
**Translation:** 

**[5162.96s] English:** And then you remember, oh, yeah, I could really think in first principles.  
**Translation:** 

**[5166.50s] English:** Oh, shit, that's tiring, you know.  
**Translation:** 

**[5169.34s] English:** But you do it for a while, and that's kind of cool.  
**Translation:** Vocabulary: tiring: 累的

**[5172.32s] English:** So, just as a last question—in your sense, from the big picture and first principles: Do you think, you kind of answered it already, but do you think autonomous driving is something we can solve on a timeline of years?  
**Translation:** 

**[5188.56s] English:** So, one, two, three, five, and ten years, as opposed to a century.  
**Translation:** 

**[5193.90s] English:** Yeah, definitely.  
**Translation:** 

**[5195.10s] English:** Just to linger on it a little longer, where's the confidence coming from?  
**Translation:** Vocabulary: linger: 停留

**[5200.08s] English:** Is it the fundamentals of the problem, the fundamentals of building the hardware and the software?  
**Translation:** 

**[5206.32s] English:** As a computational problem, understanding ballistics, roles, and topography seems pretty solvable.  
**Translation:** Vocabulary: ballistics: 弹道学; computational: 计算的; fundamentals: 基础; solvable: 可解决的; topography: 地形学

**[5216.10s] English:** I mean, and you can see this, you know, like.  
**Translation:** 

**[5218.56s] English:** Like speech recognition, for a long time, people were doing, you know, frequency and domain analysis, and all kinds of stuff.  
**Translation:** 

**[5224.34s] English:** And that didn't work at all, right?  
**Translation:** 

**[5227.04s] English:** And then they did some deep learning about it, and it worked great.  
**Translation:** 

**[5231.26s] English:** And it took multiple iterations.  
**Translation:** 

**[5234.44s] English:** And, you know, autonomous driving is way past the frequency analysis point.  
**Translation:** Vocabulary: autonomous: 自主; iterations: 迭代

**[5240.62s] English:** You know, use radar; don't run into things.  
**Translation:** 

**[5243.58s] English:** And the data gathering is going up, and the computation is going up, and the algorithm understanding is going up.  
**Translation:** Vocabulary: algorithm: 算法; computation: 计算

**[5248.60s] English:** And there's a whole bunch of problems getting solved like that.  
**Translation:** 

**[5251.64s] English:** The data side is really powerful, but I disagree with both you and Elon.  
**Translation:** 

**[5255.54s] English:** I'll tell Elon, once again as I did before, that when you add human beings into the picture, it's no longer a ballistics problem.  
**Translation:** 

**[5265.68s] English:** It's something more complicated.  
**Translation:** 

**[5267.52s] English:** But I could be very well proven wrong.  
**Translation:** 

**[5270.20s] English:** Yeah, cars are highly damped in terms of the rate of change.  
**Translation:** Vocabulary: damped: 减振的

**[5273.92s] English:** Like the steering system is really slow compared to a computer.  
**Translation:** 

**[5277.70s] English:** The accelerators.  
**Translation:** Vocabulary: accelerators: 加速器; steering: 转向系统

**[5278.56s] English:** The acceleration is really slow.  
**Translation:** 

**[5280.00s] English:** Yeah, on a certain time scale, like a ballistic time scale, but human behavior—I don't know.  
**Translation:** Vocabulary: acceleration: 加速度; ballistic: 弹道的

**[5285.56s] English:** It, yeah, I shouldn't say beings are really slow, too. We weirdly operate you know, half a second.  
**Translation:** 

**[5291.92s] English:** Behind reality, I'll be really understanding that one. Either it's pretty funny, yeah, yeah, so.  
**Translation:** Vocabulary: weirdly: 奇怪地

**[5298.80s] English:** Yeah, we'll be very well; could be surprised, and I think with the rate of improvement in all aspects.  
**Translation:** 

**[5305.92s] English:** On both the compute, and the software and hardware, there are going to be pleasant surprises.  
**Translation:** Vocabulary: compute: 计算

**[5311.00s] English:** All over the place, speaking of unpleasant surprises, many people have worries about.  
**Translation:** 

**[5318.18s] English:** A singularity in the development of AI? Forgive me for such a question. Yeah, when AI improves,...  
**Translation:** 

**[5325.26s] English:** Exponential growth and reaches a point of superhuman-level general intelligence, you know, beyond the  
**Translation:** 

**[5331.74s] English:** There's no looking back, do you share this worry about existential threats?  
**Translation:** Vocabulary: exponential: 指数的

**[5335.92s] English:** From artificial intelligence, from computers becoming superhuman-level intelligent, no, not.  
**Translation:** 

**[5342.30s] English:** Really, you know, like we already have a very stratified society, and then if you look at  
**Translation:** Vocabulary: stratified: 阶层分明的

**[5348.32s] English:** The whole animal kingdom, with its incredible range of capabilities, abilities, and interests—and you know, some are smarter than others.  
**Translation:** 

**[5354.22s] English:** People have their niche, and you know, normal people have their niche, and craftsmen have their niche.  
**Translation:** Vocabulary: capabilities: 能力; craftsmen: 工匠; niche: 专长

**[5359.58s] English:** And you know, animals have their niche. I suspect that the domains of interest...  
**Translation:** 

**[5365.90s] English:** For things that you know are astronomically different, like the whole something getting 10 times smarter than...  
**Translation:** Vocabulary: astronomically: 极其

**[5372.08s] English:** We used to want to track us all down because we liked to have coffee at Starbucks, but it doesn't anymore.  
**Translation:** 

**[5377.92s] English:** Seems plausible, no? Is there an existential problem that how do you live in a world where there's  
**Translation:** Vocabulary: plausible: 合乎情理的

**[5382.82s] English:** Something way smarter than you, and you base your kind of self-esteem on being the smartest.  
**Translation:** 

**[5388.06s] English:** Local person, well, there's what point one percent of the population who thinks that because the rest  
**Translation:** 

**[5393.10s] English:** Of the population has been dealing with it since they were born.  
**Translation:** 

**[5395.90s] English:** So, the breadth of possible  
**Translation:** 

**[5400.00s] English:** Experience that can be interesting is really big, and you know, superintelligence seems likely.  
**Translation:** 

**[5410.32s] English:** Although we still don't know if we're magical, but I suspect we're not, and it seems likely that  
**Translation:** Vocabulary: superintelligence: 超级智能

**[5417.52s] English:** It will create possibilities that are interesting for us, and its interests will be interesting.  
**Translation:** 

**[5423.68s] English:** For that, for whatever it is, it's not obvious why its interests would somehow want to fight over it.  
**Translation:** 

**[5430.92s] English:** Some square foot of dirt, or you know, whatever you know—the usual fears are about, so you don't think.  
**Translation:** 

**[5438.22s] English:** You'll inherit some of the darker aspects of human nature, depending on how you think about reality.  
**Translation:** Vocabulary: inherit: 继承

**[5443.82s] English:** Is constructed so that, for whatever reason, human beings are in, let's say, a state of creative tension and.  
**Translation:** 

**[5451.56s] English:** Opposition with both our good and  
**Translation:** 

**[5453.68s] English:** Bad forces, like there are lots of philosophical understandings of that.  
**Translation:** 

**[5457.88s] English:** Right, I don't know why that would be different. So, do you think the evil is necessary for the good?  
**Translation:** Vocabulary: philosophical: 哲学的; understandings: 理解

**[5465.70s] English:** I mean, the tension—I don't know about evil, but like, we live in a competitive world where...  
**Translation:** 

**[5471.86s] English:** Your goodness is somebody else's right, you know. Evil, you know, there's the malignant part of it.  
**Translation:** 

**[5479.22s] English:** But that seems to be self-limiting, although occasionally.  
**Translation:** 

**[5483.46s] English:** It's not so much of a malignant part of it, but it's a self-limiting part of it.  
**Translation:** 

**[5483.66s] English:** Although occasionally it's not so much of a malignant part of it, but it's a self-limiting part of it.  
**Translation:** 

**[5483.68s] English:** It's super horrible, but yes, there's a debate over ideas, and some people have different views.  
**Translation:** 

**[5491.52s] English:** Beliefs, and that debate itself is a process so at arriving at something, yeah, and why.  
**Translation:** 

**[5498.08s] English:** Wouldn't that continue, yeah? Yeah, just you, but you don't think that whole process will leave humans?  
**Translation:** 

**[5503.82s] English:** Behind, in a way that's emotionally painful, yes, for the 0.1 percent.  
**Translation:** 

**[5510.32s] English:** They'll be, you know, why isn't it already painful for a large percentage of the population?  
**Translation:** 

**[5513.66s] English:** And it is, I mean, society does have a lot of stress around the one percent and all of this.  
**Translation:** 

**[5520.00s] English:** About that, but you know, everyone has a lot of stress in their life about what they find.  
**Translation:** 

**[5524.48s] English:** Satisfying and, you know, knowing yourself seems to be the proper dictum, and pursue something that.  
**Translation:** 

**[5532.24s] English:** Making your life meaningful seems proper, and there are so many avenues for that—like there's so  
**Translation:** Vocabulary: avenues: 途径; dictum: 格言

**[5539.80s] English:** Much unexplored space at every single level, you know. I'm somewhat jaded, though, I called my nephew.  
**Translation:** 

**[5548.50s] English:** Optimist, and you know, so there's a beautiful tension in that label, but if you were to  
**Translation:** Vocabulary: optimist: 乐观主义者; unexplored: 未探索

**[5559.08s] English:** Look back at your life and, uh, could relive a moment or a set of moments because there were the  
**Translation:** 

**[5566.66s] English:** Happiest times of your life, outside of family, what would that be?  
**Translation:** Vocabulary: relive: 重新体验

**[5572.36s] English:** I don't want to relive any moments I like that.  
**Translation:** 

**[5577.34s] English:** I like that.  
**Translation:** 

**[5578.50s] English:** A situation where you have some amount of optimism, and then the anxiety of the unknown.  
**Translation:** 

**[5584.50s] English:** So, you love the unknown and the mystery of it. I don't know about the mystery, but it sure gets your  
**Translation:** Vocabulary: optimism: 积极心态

**[5591.94s] English:** Blood pumping, what do you think is the meaning of this whole thing?  
**Translation:** 

**[5595.76s] English:** Of life on this pale blue dot, it seems to be what it does; like the universe, for whatever reason.  
**Translation:** 

**[5608.50s] English:** Makes atoms, which make us do stuff, figure out things, and explore things.  
**Translation:** 

**[5617.16s] English:** That's just what it is. It's not just, yeah, it is. Yeah, Jim; I don't think there's a better place to.  
**Translation:** 

**[5626.34s] English:** End it; it's a huge honor, and uh, well, that's super fun. Thank you so much for talking today! All right.  
**Translation:** 

**[5632.70s] English:** Great, thanks for listening to this conversation, and thank you to our presenting sponsor, Cash.  
**Translation:** Vocabulary: sponsor: 赞助商

**[5638.50s] English:** App: Download it.  
**Translation:** 

**[5640.00s] English:** Use code LEXPODCAST; you'll get $10, and $10 will go to FIRST, a STEM education nonprofit that  
**Translation:** Vocabulary: nonprofit: 非盈利组织

**[5646.58s] English:** Inspires hundreds of thousands of young minds to become future leaders and innovators. If you  
**Translation:** 

**[5652.42s] English:** Enjoy this podcast! Subscribe on YouTube, give it five stars on Apple Podcasts, and follow on Spotify.  
**Translation:** Vocabulary: innovators: 创新者; inspires: 启发; subscribe: 订阅

**[5658.32s] English:** Support it on Patreon, or simply connect with me on Twitter. And now, let me leave you with  
**Translation:** 

**[5663.84s] English:** Some words of wisdom from Gordon Moore: If everything you try works, you aren't trying.  
**Translation:** Vocabulary: patreon: Patreon支持者

**[5669.86s] English:** Hard enough. Thank you for listening, and hope to see you next time.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
