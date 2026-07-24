# Podcast vocabulary notes
Source file: Lex Fridman - Jim Keller： Moore's Law, Microprocessors, and First Principles ｜ Lex Fridman Podcast #70.opus

**[0.00s] English:** The following is a conversation with Jim Keller, legendary microprocessor engineer who has worked at AMD, Apple, Tesla, and now Intel.  
**Translation:** 

**[9.76s] English:** He's known for his work on AMD K7, K8, K12, and Zen microarchitectures, Apple A4 and A5 processors,  
**Translation:** Vocabulary: keller: 凯勒; microarchitectures: 微架构; microprocessor: 微处理器; processors: 处理器

**[18.12s] English:** and co-author of the specification for the x86-64 instruction set and HyperTransport Interconnect.  
**Translation:** 

**[25.14s] English:** He's a brilliant first principles engineer, an out-of-the-box thinker, and just an interesting and fun human being to talk to.  
**Translation:** Vocabulary: interconnect: 连接网络; specification: 规范说明

**[33.44s] English:** This is the Artificial Intelligence Podcast.  
**Translation:** 

**[36.40s] English:** If you enjoy it, subscribe on YouTube, give it 5 stars on Apple Podcasts, follow on Spotify, support it on Patreon,  
**Translation:** Vocabulary: subscribe: 订阅

**[43.38s] English:** or simply connect with me on Twitter at Lex Friedman, spelled F-R-I-D-M-A-N.  
**Translation:** 

**[49.10s] English:** I recently started doing ads at the end of the introduction.  
**Translation:** Vocabulary: friedman: 弗里德曼

**[52.64s] English:** I'll do one or two minutes after introducing the episode.  
**Translation:** 

**[55.14s] English:** And never any ads in the middle that can break the flow of the conversation.  
**Translation:** 

**[59.04s] English:** I hope that works for you and doesn't hurt the listening experience.  
**Translation:** 

**[63.74s] English:** This show is presented by Cash App, the number one finance app in the App Store.  
**Translation:** 

**[68.54s] English:** I personally use Cash App to send money to friends, but you can also use it to buy, sell, and deposit Bitcoin in just seconds.  
**Translation:** 

**[75.64s] English:** Cash App also has a new investing feature.  
**Translation:** 

**[78.48s] English:** You can buy fractions of a stock, say $1 worth, no matter what the stock price is.  
**Translation:** 

**[83.32s] English:** Brokers services are provided by CashApp.  
**Translation:** Vocabulary: fractions: 股票部分

**[85.14s] English:** CashApp Investing, a subsidiary of Square and member SIPC.  
**Translation:** 

**[89.66s] English:** I'm excited to be working with CashApp to support one of my favorite organizations called FIRST,  
**Translation:** Vocabulary: subsidiary: 子公司

**[95.34s] English:** best known for their FIRST robotics and Lego competitions.  
**Translation:** 

**[98.48s] English:** They educate and inspire hundreds of thousands of students in over 110 countries  
**Translation:** 

**[103.58s] English:** and have a perfect rating on Charity Navigator, which means that donated money is used to maximum effectiveness.  
**Translation:** 

**[110.54s] English:** When you get CashApp from the App Store or Google Play and use code Lex,  
**Translation:** Vocabulary: effectiveness: 有效性; navigator: 导航器

**[115.14s] English:** PODCAST, you'll get $10 and CashApp will also donate $10 to FIRST.  
**Translation:** 

**[120.00s] English:** which again is an organization that I've personally seen inspire girls and boys to dream of engineering a better world.  
**Translation:** 

**[128.08s] English:** And now, here's my conversation with Jim Keller.  
**Translation:** 

**[132.18s] English:** What are the differences and similarities between the human brain and a computer with the microprocessor at its core?  
**Translation:** 

**[139.20s] English:** Let's start with the philosophical question, perhaps.  
**Translation:** 

**[142.28s] English:** Well, since people don't actually understand how human brains work, I think that's true.  
**Translation:** Vocabulary: philosophical: 哲学的

**[149.16s] English:** I think that's true.  
**Translation:** 

**[150.42s] English:** So, it's hard to compare them.  
**Translation:** 

**[152.82s] English:** Computers are, you know, there's really two things.  
**Translation:** 

**[157.28s] English:** There's memory and there's computation, right?  
**Translation:** Vocabulary: computation: 计算

**[160.42s] English:** And to date, almost all computer architectures are global memory, which is a thing, right?  
**Translation:** 

**[167.52s] English:** And then computation, where you pull data and you do relatively simple operations on it and write data back.  
**Translation:** 

**[174.02s] English:** So, it's decoupled in modern computers.  
**Translation:** 

**[177.84s] English:** And you think in the human brain.  
**Translation:** Vocabulary: decoupled: 解耦

**[179.50s] English:** I mean, everything's a mess that's combined together.  
**Translation:** 

**[182.54s] English:** Well, what people observe is there's, you know, some number of layers of neurons, which have local and global connections.  
**Translation:** Vocabulary: neurons: 神经元

**[189.04s] English:** And information is stored in some distributed fashion.  
**Translation:** 

**[193.52s] English:** And people build things called neural networks in computers, where the information is distributed in some kind of fashion.  
**Translation:** Vocabulary: neural: 神经的

**[202.84s] English:** You know, there's a mathematics behind it.  
**Translation:** 

**[205.12s] English:** I don't know that the understanding of that is super deep.  
**Translation:** 

**[208.12s] English:** The computations we run on those are straightforward computations.  
**Translation:** 

**[213.40s] English:** I don't believe anybody has said a neuron does this computation.  
**Translation:** Vocabulary: computations: 计算; straightforward: 简单明了

**[218.00s] English:** So, to date, it's hard to compare them, I would say.  
**Translation:** 

**[223.74s] English:** So, let's get into the basics before we zoom back out.  
**Translation:** 

**[228.74s] English:** How do you build a computer from scratch?  
**Translation:** 

**[230.94s] English:** What is a microprocessor?  
**Translation:** Vocabulary: microprocessor: 微处理器

**[232.76s] English:** What is a microarchitecture?  
**Translation:** 

**[234.12s] English:** What's an instruction set architecture?  
**Translation:** 

**[235.12s] English:** Maybe even as far back.  
**Translation:** 

**[238.12s] English:** What is a transistor?  
**Translation:** Vocabulary: transistor: 晶体管

**[240.96s] English:** So the special charm of computer engineering is there's a relatively good understanding of  
**Translation:** 

**[248.48s] English:** abstraction layers. So down at the bottom, you have atoms, and atoms get put together in materials  
**Translation:** Vocabulary: abstraction: 抽象

**[254.24s] English:** like silicon or dope silicon or metal, and we build transistors. On top of that, we build logic  
**Translation:** 

**[261.92s] English:** gates, right, and then functional units like an adder, a subtractor, an instruction parsing unit,  
**Translation:** Vocabulary: parsing: 解析; subtractor: 减法器; transistors: 晶体管

**[268.64s] English:** and then we assemble those into, you know, processing elements. Modern computers are  
**Translation:** 

**[273.44s] English:** built out of, you know, probably 10 to 20 locally, you know, organic processing elements or coherent  
**Translation:** Vocabulary: assemble: 组装; coherent: 协调

**[281.60s] English:** processing elements, and then that runs computer programs, right? So there's abstraction layers,  
**Translation:** 

**[287.84s] English:** and then software, you know, there's an instruction set you run, and then there's  
**Translation:** 

**[292.12s] English:** assembly language, C, C++, Java, JavaScript, you know, there's abstraction layers, you know,  
**Translation:** 

**[298.64s] English:** essentially from the atom to the data center, right? So when you build a computer,  
**Translation:** 

**[306.20s] English:** you know, first there's a target, like, what's it for? Like, how fast does it have to be? Which,  
**Translation:** 

**[310.28s] English:** you know, today there's a whole bunch of metrics about what that is. And then in an organization  
**Translation:** 

**[315.72s] English:** of, you know, a thousand people who build a computer, there's lots of different disciplines  
**Translation:** 

**[322.12s] English:** that you have to operate on. Does that make sense? And so...  
**Translation:** Vocabulary: disciplines: 专业领域

**[325.80s] English:** So there's a bunch of levels of abstraction.  
**Translation:** 

**[328.64s] English:** In an organization like Intel, and in your own vision, there's a lot of brilliance that comes  
**Translation:** Vocabulary: brilliance: 卓越智慧

**[337.32s] English:** in at every one of those layers. Some of it is science, some of it is engineering, some of it is  
**Translation:** 

**[342.20s] English:** art. What's the most, if you could pick favorites, what's the most important, your favorite layer  
**Translation:** 

**[349.56s] English:** on these layers of abstractions? Where does the magic enter this hierarchy?  
**Translation:** 

**[353.72s] English:** I don't really care. That's the fun, you know,  
**Translation:** Vocabulary: abstractions: 抽象; hierarchy: 层次

**[358.64s] English:** I'm somewhat agnostic.  
**Translation:** 

**[360.00s] English:** to that so i would say for relatively long periods of time instruction sets are stable  
**Translation:** Vocabulary: agnostic: 无所偏袒的

**[366.98s] English:** so the x86 instruction set the arm instruction set what's an instruction set so it says how do  
**Translation:** 

**[374.32s] English:** you encode the basic operations load store multiply add subtract conditional branch  
**Translation:** Vocabulary: conditional: 条件分支; encode: 编码; multiply: 乘法; subtract: 减法

**[379.28s] English:** you know there aren't that many interesting instructions like if you look at a program  
**Translation:** 

**[384.68s] English:** and it runs you know 90 of the execution is on 25 op codes you know 25 instructions and those  
**Translation:** 

**[392.02s] English:** are stable right what does it mean stable intel architecture has been around for 25 years it works  
**Translation:** 

**[398.58s] English:** it works and that's because the basics you know are defined a long time ago right now the way  
**Translation:** 

**[406.78s] English:** an old computer ran is you fetched instructions and you executed them in order do the load do the  
**Translation:** 

**[414.38s] English:** add  
**Translation:** 

**[414.68s] English:** the way a modern computer works is you fetch large numbers of instructions say 500  
**Translation:** 

**[422.82s] English:** and then you find the dependency graph between the instructions and then you you execute in  
**Translation:** 

**[430.34s] English:** independent units those little micrographs so a modern computer like people like to say computers  
**Translation:** 

**[438.16s] English:** should be simple and clean but it turns out the market for simple complete clean slow computers  
**Translation:** 

**[444.02s] English:** is zero  
**Translation:** 

**[444.68s] English:** right we don't sell any simple clean computers now you can there's how you build it can be clean  
**Translation:** 

**[453.22s] English:** but the computer people want to buy that's say in a phone or data center fetches a large number  
**Translation:** 

**[461.54s] English:** of instructions computes the dependency graph and then executes it in a way that gets the right  
**Translation:** Vocabulary: computes: 计算; executes: 执行

**[468.04s] English:** answers and optimize that graph somehow yeah they run deeply out of order and then  
**Translation:** 

**[474.02s] English:** there's semantics around how memory ordering works and other things work so the computer sort of  
**Translation:** Vocabulary: optimize: 优化; semantics: 语义

**[480.00s] English:** has a bunch of bookkeeping tables that says, what order should these operations  
**Translation:** 

**[483.96s] English:** finish in or appear to finish in? But to go fast, you have to fetch a lot of instructions  
**Translation:** Vocabulary: bookkeeping: 会计记录

**[490.42s] English:** and find all the parallelism. Now, there's a second kind of computer, which we call GPUs today,  
**Translation:** 

**[497.54s] English:** and I call it the difference. There's found parallelism, like you have a program with a  
**Translation:** 

**[502.08s] English:** lot of dependent instructions. You fetch a bunch, and then you go figure out the dependency graph,  
**Translation:** 

**[506.98s] English:** and you issue instructions out of order. That's because you have one serial narrative to execute,  
**Translation:** 

**[512.62s] English:** which, in fact, can be done out of order.  
**Translation:** 

**[515.78s] English:** Did you call it a narrative?  
**Translation:** 

**[517.02s] English:** Yeah.  
**Translation:** 

**[517.80s] English:** Wow.  
**Translation:** 

**[518.54s] English:** So, yeah. So, humans think of serial narrative. So, read a book, right? There's a sentence after  
**Translation:** 

**[524.26s] English:** sentence after sentence, and there's paragraphs. Now, you could diagram that. Imagine you diagrammed  
**Translation:** Vocabulary: diagrammed: 绘图表示

**[530.40s] English:** it properly, and you said, which sentences could be read in any order, any order without changing  
**Translation:** 

**[536.86s] English:** names?  
**Translation:** 

**[536.98s] English:** Meaning, right?  
**Translation:** 

**[539.68s] English:** That's a fascinating question to ask of a book. Yeah.  
**Translation:** 

**[542.52s] English:** Yeah. You could do that, right? So, some paragraphs could be reordered. Some sentences  
**Translation:** 

**[546.84s] English:** can be reordered. You could say, he is tall and smart and X, right? And it doesn't matter the  
**Translation:** 

**[557.06s] English:** order of tall and smart. But if you say, the tall man is wearing a red shirt, what colors,  
**Translation:** 

**[563.46s] English:** you know, like you can create dependencies.  
**Translation:** 

**[566.98s] English:** Right? Right. And so, GPUs, on the other hand, run simple programs on pixels. But you're given a  
**Translation:** 

**[576.02s] English:** million of them. And the first order, the screen you're looking at doesn't care which order you do  
**Translation:** Vocabulary: pixels: 像素

**[581.32s] English:** it in. So, I call that given parallelism. Simple narratives around the large numbers of things,  
**Translation:** 

**[587.86s] English:** where you can just say, it's parallel because you told me it was.  
**Translation:** 

**[591.98s] English:** So, found parallelism, where the narrative is  
**Translation:** 

**[596.06s] English:** sequential, but you discover like little pockets.  
**Translation:** Vocabulary: sequential: 顺序的

**[600.00s] English:** of parallelism versus turns out large pockets of parallelism large so how hard  
**Translation:** 

**[604.98s] English:** is it to this how hard is it that's just transistor count right so once you crack  
**Translation:** 

**[609.54s] English:** the problem you say here's how you fetch ten instructions at a time here's how  
**Translation:** 

**[613.80s] English:** you calculated the dependencies between them here's how you describe the  
**Translation:** 

**[617.46s] English:** dependencies here's you know these are pieces right so I know once you describe  
**Translation:** 

**[623.82s] English:** the dependencies then it's just a graph sort of it's an algorithm that finds  
**Translation:** Vocabulary: algorithm: 算法

**[629.40s] English:** well what is that I'm sure there's a graph theory the theoretical answer here  
**Translation:** 

**[634.56s] English:** that's solvable in general programs modern programs that human beings write  
**Translation:** Vocabulary: solvable: 可解的

**[641.76s] English:** how much found parallelism is there in the next what does 10x mean what you  
**Translation:** 

**[647.72s] English:** executed in order versus you would get what's called cycles per instruction and  
**Translation:** 

**[653.94s] English:** it would be about you know three instructions three cycles per  
**Translation:** 

**[658.86s] English:** instruction  
**Translation:** 

**[659.40s] English:** because of the latency of the operations and stuff and in a modern  
**Translation:** 

**[663.80s] English:** computer excuse it but like 0.2 0.25 cycles per instruction so it's about we  
**Translation:** Vocabulary: latency: 延迟

**[669.84s] English:** today find 10x and there's two things one is the found parallelism in the  
**Translation:** 

**[675.56s] English:** narrative right and the other is to predictability of the narrative right so  
**Translation:** 

**[681.86s] English:** certain operations they do a bunch of calculations and if greater than one do  
**Translation:** 

**[687.16s] English:** this else do that  
**Translation:** 

**[689.40s] English:** that that decision is predicted in modern computers to high ninety percent  
**Translation:** 

**[694.58s] English:** accuracy so branches happen a lot so imagine you have you have a decision to  
**Translation:** 

**[700.48s] English:** make every six instructions which is about the average right but you want to  
**Translation:** 

**[704.20s] English:** fetch 500 instructions figure out the graph and execute them all parallel that  
**Translation:** 

**[708.70s] English:** means you have six hundred instructions and it's every six you have to fetch you  
**Translation:** 

**[716.24s] English:** have to predict ninety nine out of a hundred branches correctly  
**Translation:** 

**[719.40s] English:** when it's going to be a complete  
**Translation:** 

**[738.00s] English:** you  
**Translation:** 

**[739.38s] English:** you  
**Translation:** 

**[741.36s] English:** you  
**Translation:** 

**[743.42s] English:** do  
**Translation:** 

**[744.12s] English:** you  
**Translation:** 

**[744.68s] English:** do  
**Translation:** 

**[745.28s] English:** you  
**Translation:** 

**[746.10s] English:** do  
**Translation:** 

**[746.68s] English:** do  
**Translation:** 

**[747.42s] English:** do  
**Translation:** 

**[748.00s] English:** do  
**Translation:** 

**[748.64s] English:** do  
**Translation:** 

**[749.28s] English:** do  
**Translation:** 

**[749.36s] English:** do  
**Translation:** 

**[720.00s] English:** For that window to be effective.  
**Translation:** 

**[722.32s] English:** Okay, so parallelism, you can't parallelize branches, or you can.  
**Translation:** 

**[728.34s] English:** What does predict a branch mean?  
**Translation:** 

**[730.82s] English:** So imagine you do a computation over and over.  
**Translation:** 

**[733.60s] English:** You're in a loop.  
**Translation:** Vocabulary: computation: 计算

**[734.96s] English:** So while n is greater than 1, do.  
**Translation:** 

**[739.20s] English:** And you go through that loop a million times.  
**Translation:** 

**[741.24s] English:** So every time you look at the branch, you say, it's probably still greater than 1.  
**Translation:** 

**[745.64s] English:** And you're saying you could do that accurately.  
**Translation:** 

**[747.68s] English:** Very accurately.  
**Translation:** 

**[748.52s] English:** My mind is blown.  
**Translation:** 

**[750.30s] English:** How the heck do you do that?  
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

**[766.96s] English:** So then somebody said, hey, let's keep a couple of bits and have a little counter.  
**Translation:** 

**[773.14s] English:** So when it predicts one way, we count up and then pins.  
**Translation:** 

**[776.90s] English:** So say you have a 3-bit counter.  
**Translation:** 

**[778.08s] English:** So you count.  
**Translation:** 

**[778.52s] English:** You count up and then you count down.  
**Translation:** 

**[780.80s] English:** And if it's, you know, you can use the top bit as the sign bit.  
**Translation:** 

**[783.28s] English:** So you have a sign 2-bit number.  
**Translation:** 

**[785.08s] English:** So if it's greater than 1, you predict taken.  
**Translation:** 

**[787.54s] English:** And less than 1, you predict not taken.  
**Translation:** 

**[790.40s] English:** Right.  
**Translation:** 

**[791.18s] English:** Or less than 0, whatever the thing is.  
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

**[802.54s] English:** So if you came down the code one way, you're talking about Bob and Jane.  
**Translation:** 

**[807.80s] English:** Right.  
**Translation:** 

**[808.28s] English:** And then said, does Bob like Jane?  
**Translation:** 

**[810.44s] English:** It went one way.  
**Translation:** 

**[811.14s] English:** But if you're talking about Bob and Jill, does Bob like Jane?  
**Translation:** 

**[813.86s] English:** You go a different way.  
**Translation:** 

**[815.56s] English:** Right.  
**Translation:** 

**[815.78s] English:** So that's called history.  
**Translation:** 

**[816.92s] English:** So you take the history and a counter.  
**Translation:** 

**[819.72s] English:** That's cool.  
**Translation:** 

**[821.16s] English:** But that's not how anything works today.  
**Translation:** 

**[823.30s] English:** They use something that looks a little like a neural network.  
**Translation:** 

**[827.74s] English:** So modern, you take all the execution flows.  
**Translation:** Vocabulary: neural: 神经网络

**[831.98s] English:** And then you do basically deep pattern recognition of how the program is executing.  
**Translation:** 

**[838.28s] English:** And that's what we're talking about.  
**Translation:** 

**[840.00s] English:** And you do that multiple different ways.  
**Translation:** 

**[843.44s] English:** And you have something that chooses what the best result is.  
**Translation:** 

**[847.38s] English:** There's a little supercomputer inside the computer.  
**Translation:** 

**[850.34s] English:** That's trying to predict the branching.  
**Translation:** Vocabulary: supercomputer: 超级计算机

**[851.58s] English:** That calculates which way branches go.  
**Translation:** 

**[854.24s] English:** So the effective window that it's worth finding grass in gets bigger.  
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

**[866.84s] English:** So to get to 85% took 1,000 bits.  
**Translation:** 

**[872.54s] English:** To get to 99% takes tens of megabits.  
**Translation:** 

**[878.90s] English:** So this is one of those.  
**Translation:** 

**[881.06s] English:** To get the result, you know, to get from a window of, say, 50 instructions to 500,  
**Translation:** 

**[887.54s] English:** it took three orders of magnitude or four orders of magnitude more bits.  
**Translation:** 

**[892.36s] English:** Now, if you get the prediction of a branch wrong, what happens then?  
**Translation:** 

**[896.16s] English:** It flushes the pipe.  
**Translation:** Vocabulary: flushes: 清空管道

**[897.28s] English:** It flushes the pipe.  
**Translation:** 

**[898.04s] English:** So it's just the performance cost.  
**Translation:** 

**[899.58s] English:** But it gets even better.  
**Translation:** 

**[900.78s] English:** Yeah.  
**Translation:** 

**[901.20s] English:** So we're starting to look at stuff that says,  
**Translation:** 

**[903.48s] English:** so they executed down this path.  
**Translation:** 

**[906.38s] English:** And then you had two ways to go.  
**Translation:** 

**[909.28s] English:** But far, far away, there's something that doesn't matter which path you went.  
**Translation:** 

**[914.52s] English:** So you took the wrong path.  
**Translation:** 

**[917.70s] English:** You executed a bunch of stuff.  
**Translation:** 

**[920.24s] English:** Then you had the mispredicting.  
**Translation:** 

**[921.74s] English:** You backed it up.  
**Translation:** Vocabulary: mispredicting: 错误预测

**[922.46s] English:** But you remembered all the results you already calculated.  
**Translation:** 

**[925.32s] English:** Some of those are just fine.  
**Translation:** 

**[927.36s] English:** Like, if you read a book and you misunderstand a paragraph,  
**Translation:** 

**[930.26s] English:** your understanding of the next paragraph sometimes is invariant to that understanding.  
**Translation:** Vocabulary: invariant: 不变; misunderstand: 误解

**[935.70s] English:** Sometimes it depends on it.  
**Translation:** 

**[938.32s] English:** And you can kind of anticipate that invariance.  
**Translation:** Vocabulary: anticipate: 预知; invariance: 不变性

**[943.24s] English:** Yeah, well, you can keep track of whether the data changed.  
**Translation:** 

**[947.42s] English:** And so when you come back to a piece of code,  
**Translation:** 

**[949.26s] English:** should you calculate it again or do the same thing?  
**Translation:** 

**[951.78s] English:** Okay, how much of this is art and how much of it is science?  
**Translation:** 

**[955.28s] English:** Because it sounds...  
**Translation:** 

**[956.84s] English:** Pretty complicated.  
**Translation:** 

**[959.02s] English:** Well, how do you describe it?  
**Translation:** 

**[960.00s] English:** situation so imagine you come to a point in the road where you have to make a decision yeah right  
**Translation:** 

**[964.72s] English:** and you have a bunch of knowledge about which way to go maybe you have a map so you want to go the  
**Translation:** 

**[970.00s] English:** shortest way or do you want to go the fastest way or you want to take the nicest road so it's  
**Translation:** 

**[975.62s] English:** there's some set of data right so imagine you're doing something complicated like building a  
**Translation:** 

**[980.20s] English:** computer and there's hundreds of decision points all with hundreds of possible ways to go and the  
**Translation:** 

**[988.04s] English:** ways you pick interact in a complicated way right and then you have to pick the right spot right so  
**Translation:** 

**[996.00s] English:** that order signs I don't know you avoided the question you just described the Robert Frost  
**Translation:** 

**[1000.88s] English:** poem road less taken I described the Robert Frost problem uh that's what we do as computer designers  
**Translation:** 

**[1009.30s] English:** it's all poetry okay great yeah I don't know how to describe that because some people are very good  
**Translation:** Vocabulary: designers: 设计师

**[1016.34s] English:** at making those intuitive leaps  
**Translation:** 

**[1017.84s] English:** it seems like the combinations of things some people are less good at it but they're really  
**Translation:** Vocabulary: intuitive: 直觉的

**[1022.88s] English:** good at evaluating the alternatives right and everybody has a different way to do it  
**Translation:** 

**[1028.58s] English:** and some people can't make those leaps but they're really good at analyzing it  
**Translation:** 

**[1033.58s] English:** so when you see computers are designed by teams of people who have very different skill sets  
**Translation:** 

**[1038.14s] English:** and a good team has lots of different kinds of people I suspect you would describe some of them  
**Translation:** 

**[1046.22s] English:** as artistic  
**Translation:** 

**[1047.84s] English:** right but not very many unfortunately or fortunately well you know computer design  
**Translation:** 

**[1056.04s] English:** is hard it's 99 percent perspiration and the one percent inspiration is really important  
**Translation:** 

**[1063.00s] English:** but you still need the 99 yeah you got to do a lot of work and then there's there are interesting  
**Translation:** Vocabulary: perspiration: 汗水

**[1069.98s] English:** things to do at every level that stack so at the end of the day if you run the same program  
**Translation:** 

**[1076.94s] English:** multiple times you're going to have to do a lot of work and then you're going to have to do a lot of  
**Translation:** 

**[1077.84s] English:** stuff so that's part of the difference of where the  
**Translation:** 

**[1080.00s] English:** same result is is there some room for fuzziness there that's a math problem so if you run a  
**Translation:** Vocabulary: fuzziness: 模糊性

**[1087.70s] English:** correct c program the definition is every time you run it you get the same answer yeah that  
**Translation:** 

**[1092.86s] English:** well that's a math statement but that's a that's a language definitional statement  
**Translation:** Vocabulary: definitional: 定义性的

**[1096.84s] English:** so yes for years when people did when we first did 3d acceleration of graphics  
**Translation:** 

**[1102.52s] English:** you could run the same scene multiple times and get different answers right right and then some  
**Translation:** 

**[1111.20s] English:** people thought that was okay and some people thought it was a bad idea and then when the  
**Translation:** 

**[1115.80s] English:** hbc world used gpus for calculations they thought it was a really bad idea okay now  
**Translation:** 

**[1122.40s] English:** in modern ai stuff people are looking at networks where the precision of the data is low enough  
**Translation:** 

**[1130.48s] English:** that the data is somewhat noisy  
**Translation:** 

**[1132.52s] English:** and the observation is the input data is unbelievably noisy so why should the calculation  
**Translation:** 

**[1138.64s] English:** be not noisy and people have experimented with algorithms that say can get faster answers by  
**Translation:** Vocabulary: experimented: 尝试; unbelievably: 极其

**[1144.54s] English:** being noisy like as the network starts to converge if you look at the computation graph it starts out  
**Translation:** 

**[1150.02s] English:** really wide and then it gets narrower and you can say is that last little bit that important or  
**Translation:** Vocabulary: computation: 计算; converge: 收敛; narrower: 更窄

**[1154.54s] English:** should i start the graph on the next wrap rev before we whittle it all the way down to the  
**Translation:** 

**[1159.74s] English:** answer right so you can create algorithms  
**Translation:** Vocabulary: whittle: 削减

**[1162.36s] English:** that are really noisy and the observation is the input data is unbelievably noisy so why should  
**Translation:** 

**[1162.50s] English:** i start the graph on the next wrap rev before we whittle it all the way down to the answer  
**Translation:** 

**[1163.50s] English:** right so you can create algorithms that are noisy now if you're developing something and every time  
**Translation:** 

**[1165.90s] English:** you run it you get a different answer it's really annoying and so most people think even today  
**Translation:** 

**[1173.82s] English:** every time you run the program you get the same answer no i know but the the question is that's the  
**Translation:** 

**[1178.86s] English:** formal definition of a programming language there is a definition of languages that don't get the  
**Translation:** 

**[1185.02s] English:** same answer but people who use those you always want something because you get a bad answer and  
**Translation:** 

**[1190.70s] English:** then you're wondering is it because of the programming language or is it because of the  
**Translation:** 

**[1192.34s] English:** right of something in the algorithm or because of this and so everybody wants a little switch  
**Translation:** 

**[1196.72s] English:** that says no matter what yeah do it deterministically  
**Translation:** Vocabulary: algorithm: 算法; deterministically: 确定地

**[1200.00s] English:** And it's really weird because almost everything going into modern calculations is noisy.  
**Translation:** 

**[1205.36s] English:** So why do the answers have to be so clear?  
**Translation:** 

**[1208.00s] English:** Right, so where do you stand?  
**Translation:** 

**[1209.58s] English:** I design computers for people who run programs.  
**Translation:** 

**[1212.52s] English:** So if somebody says, I want a deterministic answer, like most people want that.  
**Translation:** 

**[1218.36s] English:** Can you deliver a deterministic answer, I guess is the question.  
**Translation:** Vocabulary: deterministic: 确定性的

**[1222.20s] English:** Yeah, hopefully, sure.  
**Translation:** 

**[1222.92s] English:** What people don't realize is you get a deterministic answer even though the execution flow is very undeterministic.  
**Translation:** Vocabulary: undeterministic: 不可预测的

**[1230.80s] English:** So you run this program a hundred times, it never runs the same way twice, ever.  
**Translation:** 

**[1236.04s] English:** And the answer, it arrives at the same answer.  
**Translation:** 

**[1237.92s] English:** But it gets the same answer every time.  
**Translation:** 

**[1239.20s] English:** It's just amazing.  
**Translation:** 

**[1241.28s] English:** Okay, you've achieved in the eyes of many people, a legend status as a chip architect.  
**Translation:** 

**[1252.60s] English:** Yes.  
**Translation:** 

**[1252.92s] English:** What design creation are you most proud of?  
**Translation:** 

**[1256.16s] English:** Perhaps because it was challenging, because of its impact, or because of the set of brilliant ideas that were involved in bringing it to life.  
**Translation:** 

**[1266.78s] English:** I find that description odd.  
**Translation:** 

**[1270.12s] English:** And I have two small children, and I promise you, they think it's hilarious.  
**Translation:** 

**[1275.96s] English:** This question.  
**Translation:** 

**[1276.70s] English:** Yeah.  
**Translation:** 

**[1277.14s] English:** I do it for them.  
**Translation:** 

**[1278.26s] English:** So I'm really interested in building computers.  
**Translation:** 

**[1282.92s] English:** And I've worked with really, really smart people.  
**Translation:** 

**[1287.14s] English:** I'm not unbelievably smart.  
**Translation:** Vocabulary: unbelievably: 难以置信地

**[1289.68s] English:** I'm fascinated by how they go together, both as a thing to do and as an endeavor that people do.  
**Translation:** 

**[1298.16s] English:** How people and computers go together?  
**Translation:** Vocabulary: endeavor: 努力; fascinated: 着迷

**[1300.00s] English:** Yeah.  
**Translation:** 

**[1300.52s] English:** Like how people think and build a computer.  
**Translation:** 

**[1303.80s] English:** And I find sometimes that the best computer architects aren't that interested in people, or the best people managers aren't that good at designing computers.  
**Translation:** 

**[1312.92s] English:** So the whole stack of human beings is fascinating, so the managers, the individual engineers.  
**Translation:** 

**[1318.80s] English:** Yeah, yeah.  
**Translation:** 

**[1320.00s] English:** Yeah, I said I realized after a lot of years of building computers where you sort of build them out of transistors, logic gates, functional units, computational elements, that you could think of people the same way.  
**Translation:** Vocabulary: computational: 计算; transistors: 晶体管

**[1330.76s] English:** So people are functional units.  
**Translation:** 

**[1332.38s] English:** And then you could think of organizational design as a computer architectural problem.  
**Translation:** Vocabulary: architectural: 建筑结构的

**[1336.52s] English:** And then it was like, oh, that's super cool because the people are all different, just like the computational elements are all different.  
**Translation:** 

**[1343.62s] English:** And they like to do different things.  
**Translation:** 

**[1345.34s] English:** And so I had a lot of fun reframing how I think about organizations.  
**Translation:** 

**[1351.44s] English:** Just like with computers, we were saying execution paths, you can have a lot of different paths that end up at the same good destination.  
**Translation:** Vocabulary: reframing: 重新思考

**[1361.58s] English:** So what have you learned about the human abstractions from individual functional human units to the broader organization?  
**Translation:** 

**[1371.82s] English:** What does it take to create something special?  
**Translation:** Vocabulary: abstractions: 抽象概念

**[1374.74s] English:** Well.  
**Translation:** 

**[1376.34s] English:** Most people don't think simple enough.  
**Translation:** 

**[1379.88s] English:** All right.  
**Translation:** 

**[1380.60s] English:** So do you know the difference between a recipe and the understanding?  
**Translation:** 

**[1385.92s] English:** There's probably a philosophical description of this.  
**Translation:** 

**[1389.12s] English:** So imagine you're going to make a loaf of bread.  
**Translation:** Vocabulary: philosophical: 哲学上的

**[1391.00s] English:** The recipe says get some flour, add some water, add some yeast, mix it up, let it rise, put it in a pan, put it in the oven.  
**Translation:** 

**[1399.14s] English:** It's a recipe.  
**Translation:** 

**[1401.16s] English:** Understanding bread.  
**Translation:** 

**[1402.84s] English:** You can understand biology, supply chain.  
**Translation:** 

**[1405.68s] English:** You know, grain grinders, yeast, physics, you know, thermodynamics.  
**Translation:** 

**[1413.80s] English:** Like there's so many levels of understanding there.  
**Translation:** Vocabulary: grinders: 磨粉机; thermodynamics: 热力学; yeast: 酵母

**[1417.22s] English:** And then when people build and design things, they frequently are executing some stack of recipes.  
**Translation:** 

**[1424.38s] English:** Right.  
**Translation:** Vocabulary: executing: 执行

**[1425.18s] English:** And the problem with that is the recipes all have limited scope.  
**Translation:** 

**[1428.88s] English:** Like if you have a really good recipe book for making bread, it won't tell you anything about how to make an omelet.  
**Translation:** 

**[1434.34s] English:** Right.  
**Translation:** 

**[1434.82s] English:** But.  
**Translation:** 

**[1435.08s] English:** If you have a deep understanding of cooking.  
**Translation:** 

**[1438.32s] English:** Right.  
**Translation:** 

**[1439.16s] English:** Then bread.  
**Translation:** 

**[1439.92s] English:** Bread.  
**Translation:** 

**[1440.00s] English:** omelets you know sandwich you know there's there's a different you know way of viewing everything  
**Translation:** 

**[1446.54s] English:** and most people when you get to be an expert at something you know you're you're hoping to  
**Translation:** 

**[1454.64s] English:** achieve deeper understanding not just a large set of recipes to go execute and it's interesting to  
**Translation:** 

**[1461.86s] English:** walk groups of people because executing recipes is unbelievably efficient if it's what you want to do  
**Translation:** 

**[1468.96s] English:** if it's not what you want to do you're really stuck and and that difference is crucial and  
**Translation:** 

**[1476.78s] English:** and everybody has a balance of let's say deeper understanding recipes and some people are really  
**Translation:** 

**[1481.78s] English:** good at recognizing when the problem is to understand something deeply deeply does that  
**Translation:** 

**[1487.82s] English:** make sense it totally makes sense uh does it every stage of development deep on understanding  
**Translation:** 

**[1493.94s] English:** on the team needed well this goes back to the art versus science question sure  
**Translation:** 

**[1498.96s] English:** if you constantly unpack everything for deeper understanding you never get anything done  
**Translation:** 

**[1503.20s] English:** right and if you don't unpack understanding when you need to you'll do the wrong thing  
**Translation:** 

**[1508.24s] English:** and then at every juncture like human beings are these really weird things because  
**Translation:** Vocabulary: juncture: 转折点

**[1513.60s] English:** everything you tell them has a million possible outputs right and then they all interact in a  
**Translation:** 

**[1519.46s] English:** hilarious way and then having some intuition about what do you tell them what you do when  
**Translation:** Vocabulary: intuition: 直觉

**[1525.14s] English:** do you intervene when do you not it's it's complicated  
**Translation:** 

**[1528.96s] English:** right so it's it's you know essentially computationally unsolvable yeah it's an  
**Translation:** Vocabulary: computationally: 计算上; intervene: 干预; unsolvable: 无法解决

**[1534.00s] English:** intractable problem sure humans are a mess but uh with deep understanding do you mean also  
**Translation:** 

**[1542.88s] English:** sort of fundamental questions of uh things like what is a computer like or why like the why  
**Translation:** Vocabulary: intractable: 难以解决

**[1554.46s] English:** questions why are we even building this like of purpose or  
**Translation:** 

**[1558.96s] English:** do you mean  
**Translation:** 

**[1560.00s] English:** more like going towards the fundamental limits of physics sort of really getting into the core  
**Translation:** 

**[1566.50s] English:** of the science well in terms of building a computer think simple think a little simpler  
**Translation:** 

**[1571.04s] English:** so common practice is you build a computer and then when somebody says i want to make it 10  
**Translation:** 

**[1576.26s] English:** faster you'll go in and say all right i need to make this buffer bigger and maybe i'll add an ad  
**Translation:** Vocabulary: buffer: 缓存

**[1581.90s] English:** unit or you know i have this thing that's three instructions wide i'm going to make it four  
**Translation:** 

**[1586.22s] English:** instructions wide and what you see is each piece gets incrementally more complicated  
**Translation:** Vocabulary: incrementally: 逐步地

**[1592.28s] English:** right and then at some point you hit this limit like adding another feature or buffer doesn't  
**Translation:** 

**[1599.40s] English:** seem to make it any faster and then people say well that's because it's a fundamental limit  
**Translation:** 

**[1604.40s] English:** and then somebody else will look at it and say well actually the way you divided the problem up  
**Translation:** 

**[1609.20s] English:** and the way that different features are interacting is limiting you and it has to be  
**Translation:** 

**[1613.62s] English:** rethought rewritten right  
**Translation:** 

**[1616.22s] English:** so then you refactor it and rewrite it and what people commonly find is the rewrite is not only  
**Translation:** Vocabulary: refactor: 重构; rewritten: 重写

**[1621.46s] English:** faster but half as complicated from scratch yes so how often in your career but just have you seen  
**Translation:** 

**[1628.42s] English:** as needed maybe more generally to just throw the whole out the whole thing out this is where i'm  
**Translation:** 

**[1635.22s] English:** on one end of it every three to five years which end are you on wait rewrite more often  
**Translation:** 

**[1642.14s] English:** rewrite and three to five years is so if you want to really make  
**Translation:** 

**[1646.22s] English:** a lot of progress on computer architecture every five years you should do one from scratch  
**Translation:** 

**[1651.90s] English:** so where does the x86 64 standard come in or what how often do you i wrote the  
**Translation:** 

**[1659.42s] English:** i was the co-author of that spec in 98. that's 20 years ago yeah so that's still around the  
**Translation:** 

**[1666.14s] English:** instruction set itself has been extended quite a few times yes and instruction sets are less  
**Translation:** 

**[1671.90s] English:** interesting than the implementation underneath there's been on x86  
**Translation:** 

**[1676.22s] English:** architecture intel's designed a few aims designed a few  
**Translation:** Vocabulary: implementation: 实现方式

**[1680.00s] English:** very different architectures and i don't want to go into too much of the detail about how often but  
**Translation:** 

**[1687.68s] English:** there's a tendency to rewrite it every you know 10 years and it really should be every five  
**Translation:** 

**[1693.92s] English:** so you're saying you're an outlier in that sense in the more often rewrite more often  
**Translation:** 

**[1699.86s] English:** well and here's isn't that scary yeah of course well scary to who to uh everybody involved because  
**Translation:** 

**[1707.00s] English:** like you said repeating the recipe is efficient companies want to make money well no individual  
**Translation:** 

**[1715.04s] English:** juniors want to succeed so you want to incrementally improve increase the buffer from three to four  
**Translation:** Vocabulary: buffer: 缓冲; incrementally: 逐步

**[1721.00s] English:** well this is where you get into diminishing return curves i think steve job said this right  
**Translation:** 

**[1726.84s] English:** so every you have a project and you start here and it goes up and they have diminishing return  
**Translation:** 

**[1731.74s] English:** and to get to the next level you have to do a new one and the initial starting point  
**Translation:** 

**[1736.42s] English:** will be  
**Translation:** 

**[1737.00s] English:** be lower than the old optimization point but it'll get higher so now you have two kinds of fear  
**Translation:** 

**[1743.24s] English:** short-term disaster and long-term disaster and you're you're grown-ups right like you know people  
**Translation:** Vocabulary: optimization: 优化

**[1752.40s] English:** with a quarter by quarter business objective are terrified about changing everything yeah and  
**Translation:** 

**[1758.00s] English:** people who are trying to run a business or build a computer for a long-term objective  
**Translation:** 

**[1763.32s] English:** know that the short-term limitations block them from the long-term success so if you look at  
**Translation:** 

**[1770.28s] English:** leaders of companies that had really good long-term success every time they saw that they  
**Translation:** 

**[1776.40s] English:** had to redo something they did and so somebody has to speak up or you do multiple projects in  
**Translation:** 

**[1782.44s] English:** parallel like you optimize the old one while you build a new one and but the marketing guys are  
**Translation:** 

**[1787.70s] English:** always like make promise me that the new computer is faster on every single thing and the computer  
**Translation:** 

**[1793.18s] English:** are  
**Translation:** 

**[1793.30s] English:** the architects says well the new computer will be faster on the average  
**Translation:** 

**[1795.92s] English:** but there's a distribution of results and performance and you'll have  
**Translation:** 

**[1800.00s] English:** outliers that are slower and that's very hard because they have one customer who cares about  
**Translation:** 

**[1804.18s] English:** that one so speaking of the long term for over 50 years now moore's law has served a  
**Translation:** 

**[1810.22s] English:** for me and millions of others as an inspiring beacon of what kind of amazing future berlin  
**Translation:** 

**[1816.92s] English:** engineers can build yep i'm just making your kids laugh all of today that was great so uh first  
**Translation:** Vocabulary: beacon: 灯塔

**[1825.38s] English:** in your eyes what is moore's law if you could define for people who don't know  
**Translation:** 

**[1829.34s] English:** well the the simple statement was from gordon moore was double the number of transistors every  
**Translation:** Vocabulary: transistors: 晶体管

**[1836.20s] English:** two years something like that and then my operational model is we increase the performance  
**Translation:** 

**[1844.84s] English:** of computers by 2x every two or three years and it's wiggled around substantially over time  
**Translation:** Vocabulary: wiggled: 波动

**[1851.04s] English:** and also in how we deliver performance has changed  
**Translation:** 

**[1854.88s] English:** but the  
**Translation:** 

**[1859.34s] English:** idea was 2x the transistors every two years the current cadence is something like they call it a  
**Translation:** 

**[1866.34s] English:** shrink factor like 0.6 every two years which is not 0.5 but that that's referring strictly again  
**Translation:** Vocabulary: cadence: 节奏

**[1873.72s] English:** to the original definition of transistor count and shrink factors just getting them smaller  
**Translation:** 

**[1878.34s] English:** small and small well as you use for a constant chip area right if you make the transistor smaller  
**Translation:** Vocabulary: transistor: 晶体管

**[1883.18s] English:** by 0.6 then you get one over 0.6 more transistors so can you linger on it a little longer what's the  
**Translation:** 

**[1889.34s] English:** what's the broader what do you think should be the broader definition of moore's law  
**Translation:** 

**[1893.42s] English:** when you mention perf how you think of performance just broadly what's a good way to think about  
**Translation:** 

**[1900.22s] English:** moore's law well first of all so i i've been aware of moore's law for 30 years  
**Translation:** 

**[1906.96s] English:** in which sense well i've been designing computers for 40. you're just watching it before your eyes  
**Translation:** 

**[1915.06s] English:** well and somewhere where i became aware of it i was also informed i'm  
**Translation:** 

**[1919.34s] English:** Moore's law was going to  
**Translation:** 

**[1920.00s] English:** to die in 10 to 15 years and i thought that was true at first but then after 10 years it was going  
**Translation:** 

**[1925.56s] English:** to die in 10 to 15 years and then at one point it was going to die in five years and then it went  
**Translation:** 

**[1930.20s] English:** back up to 10 years and at some point i decided not to worry about that particular prognostication  
**Translation:** Vocabulary: prognostication: 预测

**[1936.08s] English:** for the rest of my life which is which is fun and then i joined intel and everybody said moore's law  
**Translation:** 

**[1941.94s] English:** is dead and i thought that's sad because it's the moore's law company and it's not dead and it's  
**Translation:** 

**[1947.22s] English:** always been going to die and you know humans like these apocryphal kind of statements like  
**Translation:** 

**[1953.62s] English:** we'll run out of food or run out of air or run out of room or run out of you know something  
**Translation:** Vocabulary: apocryphal: 未证实的

**[1959.00s] English:** right but it's still incredible that it's lived for as long as it has and yes there's many people  
**Translation:** 

**[1966.24s] English:** who believe now that moore's law is dead you know they can join the last 50 years of people  
**Translation:** 

**[1973.14s] English:** yeah there's a long tradition but uh why do you think  
**Translation:** 

**[1977.20s] English:** if you can in text try to understand why do you think it's not dead well for currently let's just  
**Translation:** 

**[1984.28s] English:** think um people think moore's law is one thing transistors get smaller but actually under the  
**Translation:** 

**[1989.96s] English:** sheet there's literally thousands of innovations and almost all those innovations have their own  
**Translation:** Vocabulary: innovations: 创新; transistors: 晶体管

**[1994.84s] English:** diminishing return curves so if you graph it it looks like a cascade of diminishing return curves  
**Translation:** 

**[2000.78s] English:** i don't know what to call that but the result is an exponential curve but at least it has  
**Translation:** Vocabulary: diminishing: 递减; exponential: 指数的

**[2007.18s] English:** been so and we keep inventing new things so if you're an expert in one of the things on a  
**Translation:** 

**[2013.02s] English:** diminishing return curve right and you can see its plateau you will probably tell people well this is  
**Translation:** Vocabulary: plateau: 平台期

**[2020.62s] English:** this is done meanwhile some other pile of people are are doing something different so that's that's  
**Translation:** 

**[2027.02s] English:** just normal so then there's the observation of how small could a switching device be  
**Translation:** 

**[2033.90s] English:** so a modern transistor is something like a thousand by a thousand by a thousand  
**Translation:** 

**[2037.18s] English:** atoms right and  
**Translation:** Vocabulary: transistor: 晶体管

**[2040.00s] English:** And you get quantum effects down around 2 to 10 atoms.  
**Translation:** 

**[2044.34s] English:** So you can imagine a transistor as small as 10 by 10 by 10.  
**Translation:** 

**[2048.14s] English:** So that's a million times smaller.  
**Translation:** 

**[2051.90s] English:** And then the quantum computational people are working away at how to use quantum effects.  
**Translation:** Vocabulary: computational: 计算的

**[2059.56s] English:** So...  
**Translation:** 

**[2060.08s] English:** 1,000 by 1,000 by 1,000.  
**Translation:** 

**[2061.88s] English:** Atoms.  
**Translation:** 

**[2063.42s] English:** That's a really clean way of putting it.  
**Translation:** 

**[2066.60s] English:** Well, a fan, like a modern transistor, if you look at the fan,  
**Translation:** 

**[2069.70s] English:** it's like 120 atoms wide, but we can make that thinner.  
**Translation:** 

**[2073.42s] English:** And then there's a gate wrapped around it, and then there's spacing.  
**Translation:** 

**[2076.62s] English:** There's a whole bunch of geometry.  
**Translation:** Vocabulary: geometry: 几何

**[2078.94s] English:** And, you know, a competent transistor designer could count both atoms in every single direction.  
**Translation:** 

**[2087.64s] English:** Like, there's techniques now to already put down atoms in a single atomic layer.  
**Translation:** Vocabulary: competent: 有能力的

**[2092.82s] English:** And you can place atoms if you want to.  
**Translation:** 

**[2095.58s] English:** It's just, you know, from a manufacturing process,  
**Translation:** 

**[2099.46s] English:** if you're going to put atoms in a single atomic layer,  
**Translation:** 

**[2099.70s] English:** placing an atom takes 10 minutes, and you need to put, you know,  
**Translation:** 

**[2103.80s] English:** 10 to the 23rd atoms together to make a computer, it would take a long time.  
**Translation:** 

**[2108.82s] English:** So the methods are, you know, both shrinking things  
**Translation:** Vocabulary: shrinking: 缩小

**[2112.68s] English:** and then coming up with effective ways to control what's happening.  
**Translation:** 

**[2118.04s] English:** Manufacture stably and cheaply.  
**Translation:** Vocabulary: cheaply: 价格低廉; manufacture: 生产; stably: 稳定

**[2120.02s] English:** Yeah.  
**Translation:** 

**[2121.04s] English:** So the innovation stack's pretty broad.  
**Translation:** 

**[2123.60s] English:** You know, there's equipment, there's optics, there's chemistry,  
**Translation:** 

**[2126.68s] English:** there's physics, there's material science,  
**Translation:** Vocabulary: optics: 光学

**[2128.98s] English:** there's metallurgy.  
**Translation:** 

**[2130.70s] English:** There's lots of ideas about when you put different materials together,  
**Translation:** Vocabulary: metallurgy: 金属工艺

**[2133.70s] English:** how do they interact, are they stable, are they stable over temperature?  
**Translation:** 

**[2137.96s] English:** You know, like, are they repeatable?  
**Translation:** 

**[2140.58s] English:** You know, there's, like, literally thousands of technologies involved.  
**Translation:** 

**[2145.12s] English:** But just for the shrinking, you don't think we're quite yet close to the fundamental limits of physics?  
**Translation:** 

**[2150.86s] English:** I did a talk on Mars law, and I asked for a roadmap to a path of 100.  
**Translation:** 

**[2154.64s] English:** And after two weeks, they said we only got to 50.  
**Translation:** 

**[2158.80s] English:** 100 what, sorry?  
**Translation:** 

**[2159.72s] English:** 100.  
**Translation:** 

**[2160.00s] English:** x shrink 100 x shrink we only got to 50 and i said why don't you give it another two weeks  
**Translation:** 

**[2164.80s] English:** well here's the thing about moore's law right so i believe that the next 10 or 20 years of  
**Translation:** 

**[2174.26s] English:** shrinking is going to happen right now as a computer designer there's you have two stances  
**Translation:** 

**[2180.26s] English:** you think it's going to shrink in which case you're designing and thinking about architecture  
**Translation:** Vocabulary: stances: 立场

**[2186.02s] English:** in a way that you'll use more transistors or conversely not be swamped by the complexity of  
**Translation:** 

**[2192.96s] English:** all the transistors you get right you have to have a strategy you know so you're you're open  
**Translation:** Vocabulary: complexity: 复杂性; conversely: 相反地; swamped: 淹没; transistors: 晶体管

**[2200.50s] English:** to the possibility and waiting for the possibility of a whole new army of transistors ready to work  
**Translation:** 

**[2205.84s] English:** i'm expecting expecting more transistors every two or three years by a number large enough  
**Translation:** 

**[2212.00s] English:** that how you think about design how you think about architecture has to change  
**Translation:** 

**[2216.02s] English:** like imagine you're you you build built brick buildings out of bricks and every year the bricks  
**Translation:** 

**[2222.04s] English:** are half the size or every two years well if you kept building bricks the same way you know so many  
**Translation:** 

**[2228.72s] English:** bricks per person per day the amount of time to build a building would go up exponentially  
**Translation:** 

**[2234.68s] English:** right right but if you said i know that's coming so now i'm going to design equipment that moves  
**Translation:** 

**[2241.46s] English:** bricks faster uses them better because maybe you're getting something out of the smaller bricks more  
**Translation:** 

**[2245.50s] English:** strength  
**Translation:** 

**[2246.02s] English:** inner walls you know less material efficiency out of that so once you have a roadmap with what's  
**Translation:** 

**[2251.92s] English:** going to happen transistors they're going to get we're going to get more of them then you  
**Translation:** 

**[2257.06s] English:** design all this collateral around it to take advantage of it and also to cope with it like  
**Translation:** Vocabulary: collateral: 辅助设施

**[2262.56s] English:** that's the thing people don't understand it's like if i didn't believe in moore's law and then  
**Translation:** 

**[2266.52s] English:** moore's law transistors showed up my design teams were all drowned so what's the what's the hardest  
**Translation:** 

**[2273.78s] English:** part of this  
**Translation:** 

**[2276.02s] English:** i mean even if you just look historically throughout  
**Translation:** Vocabulary: historically: 历史上

**[2280.00s] English:** your career what's what's the thing what fundamentally changes when you add more  
**Translation:** 

**[2286.08s] English:** transistors in in the task of uh designing an architecture well there's there's two  
**Translation:** Vocabulary: fundamentally: 从根本上

**[2291.66s] English:** constants right one is people don't get smarter i think by the way there's some science showing  
**Translation:** 

**[2297.20s] English:** that we do get smarter because of nutrition whatever yeah sorry to bring that effect yes  
**Translation:** Vocabulary: constants: 不变量

**[2302.80s] English:** yeah familiar with it nobody understands it nobody knows if it's still going on so that's a  
**Translation:** 

**[2306.76s] English:** or whether it's real or not but yeah i sort of anyway but not i would believe for the most part  
**Translation:** 

**[2313.38s] English:** people aren't getting much smarter the evidence doesn't support it that's right and then teams  
**Translation:** 

**[2318.48s] English:** can't grow that much right right so human beings understand you know we're really good in teams of  
**Translation:** 

**[2324.48s] English:** 10 you know up to teams of 100 they can know each other beyond that you have to have organizational  
**Translation:** 

**[2329.60s] English:** boundaries so you're kind of you have those are pretty hard constraints right so then you have  
**Translation:** Vocabulary: constraints: 限制

**[2335.30s] English:** to divide and conquer like  
**Translation:** 

**[2336.76s] English:** as the designs get bigger you have to divide it into pieces you know the power of abstraction  
**Translation:** Vocabulary: abstraction: 抽象

**[2341.72s] English:** layers is really high we used to build computers out of transistors now we have a team that turns  
**Translation:** 

**[2347.40s] English:** transistors into logic cells and another team that turns them into functional units another  
**Translation:** Vocabulary: transistors: 晶体管

**[2350.82s] English:** one that turns into computers right so we have abstraction layers in there and you have to think  
**Translation:** 

**[2358.50s] English:** about when do you shift gears on that we also use faster computers to build faster computers  
**Translation:** 

**[2363.86s] English:** so some algorithms run twice as fast on new computers  
**Translation:** 

**[2366.76s] English:** but a lot of algorithms are n squared so you know a computer with twice as many transistors and it  
**Translation:** 

**[2373.70s] English:** might take four times times as long to run so you have to refactor the software like simply using  
**Translation:** 

**[2380.06s] English:** faster computers to build bigger computers doesn't work so so you have to think about all these things  
**Translation:** Vocabulary: refactor: 重构代码

**[2386.14s] English:** so in terms of computing performance and the exciting possibility that more powerful computers  
**Translation:** 

**[2390.62s] English:** bring is shrinking the thing we've just been talking about  
**Translation:** Vocabulary: computing: 计算; shrinking: 缩小

**[2394.92s] English:** one of the things that we've been talking about is the fact that we're not going to be able to  
**Translation:** 

**[2396.76s] English:** clean up our DB Center and get the hardware right away it's not going to be perfect so but  
**Translation:** 

**[2398.92s] English:** it's going to happen and maybe one day olivia will be able to get the hardware right away  
**Translation:** 

**[2400.00s] English:** advancement in performance or is there other directions that you're interested in like  
**Translation:** Vocabulary: advancement: 进步

**[2404.24s] English:** like in the direction of sort of enforcing given parallelism or like doing massive parallelism in  
**Translation:** 

**[2412.30s] English:** terms of many many cpus you know stacking cpus on top of each other that kind of that kind of  
**Translation:** Vocabulary: enforcing: 强制执行; stacking: 堆叠

**[2419.04s] English:** parallelism or any kind of well think about it a different way so old computers you know slow  
**Translation:** 

**[2424.60s] English:** computers you said a equal b plus c times d pretty simple right and then we made faster computers  
**Translation:** 

**[2432.52s] English:** with vector units and you can do proper equations and matrices right and then modern like ai  
**Translation:** 

**[2440.12s] English:** computations or like convolutional neural networks where you convolve one large data set against  
**Translation:** 

**[2445.74s] English:** another and so there's sort of this hierarchy of mathematics you know from simple equation to  
**Translation:** 

**[2453.16s] English:** linear equations to matrix equations and so on and so forth and so on and so on and so on and so on  
**Translation:** Vocabulary: equation: 方程; equations: 方程; hierarchy: 层次; matrix: 矩阵

**[2454.60s] English:** to deeper kind of computation and the data sets are getting so big that people are thinking of  
**Translation:** 

**[2461.56s] English:** data as a topology problem you know data is organized in some immense shape and then the  
**Translation:** Vocabulary: computation: 计算; immense: 巨大; topology: 拓扑

**[2468.52s] English:** computation which sort of wants to be get data from immense shape and do some computation on it  
**Translation:** 

**[2474.60s] English:** so the what computers have allowed people to do is have algorithms go much much further  
**Translation:** 

**[2482.04s] English:** so that that paper you you refer  
**Translation:** 

**[2484.58s] English:** to the paper they talked about you know like when ai started it was apply rule sets to something  
**Translation:** 

**[2490.86s] English:** that's a very simple computational situation and then when they did first chess thing they  
**Translation:** 

**[2498.00s] English:** they solved deep searches so have a huge database of moves and results deep search but it's still  
**Translation:** Vocabulary: computational: 计算的

**[2505.40s] English:** just a search right now we we take large numbers of images and we use it to train these weight sets  
**Translation:** 

**[2513.86s] English:** that we use to train these weight sets that we use to train these weight sets that we use to train  
**Translation:** 

**[2514.56s] English:** that we use to train these weight sets that we use to train these weight sets Where we convolve across  
**Translation:** 

**[2515.92s] English:** where we convolve across it's a completely different kind of phenomena we call that ai  
**Translation:** Vocabulary: convolve: 卷积

**[2520.00s] English:** Now they're doing the next generation.  
**Translation:** 

**[2522.42s] English:** And if you look at it, they're going up this mathematical graph, right?  
**Translation:** Vocabulary: mathematical: 数学的

**[2527.36s] English:** And then computations, both computation and data sets support going up that graph.  
**Translation:** 

**[2533.94s] English:** Yeah, the kind of computation that might, I mean, I would argue that all of it is still a search, right?  
**Translation:** Vocabulary: computations: 计算

**[2539.62s] English:** Just like you said, a topology problem of data sets,  
**Translation:** 

**[2542.80s] English:** he's searching the data sets for valuable data  
**Translation:** 

**[2546.86s] English:** and also the actual optimization of neural networks is a kind of search for the...  
**Translation:** 

**[2553.02s] English:** I don't know.  
**Translation:** Vocabulary: neural: 神经; optimization: 优化

**[2553.34s] English:** If you had looked at the inner layers of finding a cat, it's not a search.  
**Translation:** 

**[2559.12s] English:** It's a set of endless projections.  
**Translation:** Vocabulary: projections: 预测

**[2561.34s] English:** So, you know, a projection, here's a shadow of this phone, right?  
**Translation:** 

**[2565.52s] English:** And then you can have a shadow of that on something, a shadow on that of something.  
**Translation:** Vocabulary: projection: 投影像

**[2569.24s] English:** If you look in the layers, you'll see this layer actually describes pointy ears  
**Translation:** 

**[2573.46s] English:** and round eyeness and fuzziness.  
**Translation:** Vocabulary: fuzziness: 毛茸茸; pointy: 尖尖的

**[2576.26s] English:** But the...  
**Translation:** 

**[2576.86s] English:** The computation to tease out the attributes is not search.  
**Translation:** Vocabulary: attributes: 属性

**[2583.78s] English:** Right, I mean...  
**Translation:** 

**[2584.46s] English:** Like the inference part might be search, but the training is not search.  
**Translation:** Vocabulary: inference: 推断

**[2587.44s] English:** Okay, well...  
**Translation:** 

**[2587.92s] English:** And then in deep networks, they look at layers and they don't even know it's represented.  
**Translation:** 

**[2594.10s] English:** And yet, if you take the layers out, it doesn't work.  
**Translation:** 

**[2596.58s] English:** Okay, so...  
**Translation:** 

**[2597.32s] English:** So, I don't think it's search.  
**Translation:** 

**[2598.84s] English:** All right, well...  
**Translation:** 

**[2599.50s] English:** But you have to talk to a mathematician about what that actually is.  
**Translation:** 

**[2602.66s] English:** Well, we could disagree, but the...  
**Translation:** Vocabulary: mathematician: 数学家

**[2605.58s] English:** It's just semantic.  
**Translation:** 

**[2606.98s] English:** I think it's not...  
**Translation:** Vocabulary: semantic: 语义的

**[2607.92s] English:** But it's certainly not...  
**Translation:** 

**[2609.02s] English:** I would say it's absolutely not semantics, but...  
**Translation:** Vocabulary: semantics: 语义

**[2611.80s] English:** Okay.  
**Translation:** 

**[2613.40s] English:** All right, well, if you want to go there.  
**Translation:** 

**[2616.78s] English:** So, optimization to me is search.  
**Translation:** 

**[2618.96s] English:** And we're trying to optimize the ability of a neural network to detect cat ears.  
**Translation:** Vocabulary: optimize: 优化

**[2625.92s] English:** And the difference between chess and the space,  
**Translation:** 

**[2631.16s] English:** the incredibly multidimensional, hundred-thousand-dimensional space that,  
**Translation:** Vocabulary: multidimensional: 多维的

**[2636.86s] English:** you know, networks are trying to optimize over is nothing like...  
**Translation:** 

**[2640.00s] English:** the chessboard database so it's a totally different kind of thing and okay in that sense  
**Translation:** Vocabulary: chessboard: 棋盘

**[2645.62s] English:** you can say yeah yeah it loses i can see how you you might say if if you the funny thing is it's  
**Translation:** 

**[2652.26s] English:** the difference between given search space and found search space right exactly yeah maybe that's  
**Translation:** 

**[2657.84s] English:** a different way that's a beautiful way to put it okay but you're saying what's your sense in terms  
**Translation:** 

**[2661.98s] English:** of the basic mathematical operations and the architectures computer hardware that enables  
**Translation:** Vocabulary: mathematical: 数学的

**[2668.52s] English:** those operations do you see the cpus of today still being a really core part of executing  
**Translation:** 

**[2675.90s] English:** those mathematical operations yes well the operations you know continue to be add subtract  
**Translation:** Vocabulary: executing: 执行; subtract: 减法

**[2682.02s] English:** load store compare and branch it's it's remarkable so it's it's interesting that the building blocks  
**Translation:** 

**[2688.70s] English:** of you know computers or transistors and you know under that atoms so you got atoms transistors  
**Translation:** Vocabulary: transistors: 晶体管

**[2693.92s] English:** logic gates computers right you know functional units and computers  
**Translation:** 

**[2698.52s] English:** building blocks of mathematics at some level are things like ads and subtracts and multiplies but  
**Translation:** Vocabulary: multiplies: 乘法; subtracts: 减法

**[2704.62s] English:** the the space mathematics can describe is i think essentially infinite but the computers that run  
**Translation:** 

**[2713.08s] English:** the algorithms are still doing the same things now a given algorithm might say i need sparse data  
**Translation:** Vocabulary: algorithm: 算法; sparse: 稀疏数据

**[2720.16s] English:** or i need 32-bit data or i need you know um like a convolution operation that naturally takes  
**Translation:** 

**[2728.52s] English:** data multiplies it and sums it up a certain way so the like the data types in tensorflow imply an  
**Translation:** Vocabulary: convolution: 卷积操作

**[2735.96s] English:** optimization set but when you go right down and look at the computers it's an or gates doing ads  
**Translation:** 

**[2741.72s] English:** and multiplies like like that hasn't changed much now the quantum researchers think they're going to  
**Translation:** Vocabulary: optimization: 优化

**[2748.90s] English:** change that radically and then there's people who think about analog computing because you look in  
**Translation:** 

**[2752.66s] English:** the brain and it seems to be more analog ish you know that maybe there's a way to do that more  
**Translation:** Vocabulary: analog: 模拟; computing: 计算; radically: 根本上

**[2758.52s] English:** efficiently but we have  
**Translation:** 

**[2760.00s] English:** a million x on computation and i don't know the reference the relationship between computational  
**Translation:** Vocabulary: computation: 计算; computational: 计算的; efficiently: 高效地

**[2769.00s] English:** let's say intensity and ability to hit mathematical abstractions i don't know  
**Translation:** 

**[2776.06s] English:** anybody's described that but but just like you saw in ai you went from rule sets to simple search  
**Translation:** Vocabulary: abstractions: 抽象概念

**[2782.92s] English:** to complex search to say found search like those are you know orders of magnitude more computation  
**Translation:** 

**[2789.90s] English:** to do and as we get the next two orders of magnitude like a friend roger godori said like  
**Translation:** 

**[2796.58s] English:** every order of magnitude changes the computation fundamentally changes what the computation is  
**Translation:** 

**[2802.42s] English:** doing yeah oh you know the expression the difference in quantity is the difference in kind  
**Translation:** Vocabulary: fundamentally: 从根本上

**[2807.94s] English:** you know the difference between ant and anthill right or neuron and brain  
**Translation:** 

**[2814.36s] English:** you know there's there's there's there's indefinable place where the  
**Translation:** Vocabulary: anthill: 蚁巢; indefinable: 难以界定; neuron: 神经元

**[2819.28s] English:** the quantity  
**Translation:** 

**[2819.90s] English:** quantity changed the quality right and we've seen that happen in mathematics multiple times and  
**Translation:** 

**[2825.16s] English:** you know my my guess is it's going to keep happening so in your sense is yeah if you focus  
**Translation:** 

**[2830.78s] English:** head down and shrinking the transistor let's not just head down we're aware of the software  
**Translation:** Vocabulary: shrinking: 缩小; transistor: 晶体管

**[2837.86s] English:** stacks that are running in the computational loads and we're kind of pondering what do you do with a  
**Translation:** 

**[2843.32s] English:** petabyte of memory that wants to be accessed in a sparse way and have you know the kind of  
**Translation:** Vocabulary: accessed: 被访问; petabyte: 拍字节; pondering: 思考; sparse: 稀疏

**[2848.58s] English:** calculations ai  
**Translation:** 

**[2849.90s] English:** programmers want so there's a there's a dialogue and interaction but when you go  
**Translation:** Vocabulary: programmers: 程序员

**[2855.46s] English:** in the computer chip you know you find adders and subtractors and multipliers and  
**Translation:** 

**[2861.58s] English:** so if you zoom out then with as you mentioned rich sutton the idea that most of the development  
**Translation:** Vocabulary: multipliers: 乘法器; subtractors: 减法器

**[2868.46s] English:** in the last many decades in ai research came from just leveraging computation and just  
**Translation:** 

**[2874.72s] English:** the simple algorithms waiting for the computation to improve  
**Translation:** Vocabulary: leveraging: 利用

**[2879.90s] English:** and you know that the that is already already around like please get really into the  
**Translation:** 

**[2899.20s] English:** problem  
**Translation:** 

**[2899.26s] English:** you  
**Translation:** 

**[2904.42s] English:** you  
**Translation:** 

**[2907.94s] English:** g  
**Translation:** 

**[2909.26s] English:** g  
**Translation:** 

**[2909.78s] English:** f  
**Translation:** 

**[2909.86s] English:** f  
**Translation:** 

**[2909.88s] English:** f  
**Translation:** 

**[2880.00s] English:** Well, software guys have a thing that they call the problem of early optimization.  
**Translation:** 

**[2886.14s] English:** Right.  
**Translation:** 

**[2886.90s] English:** So you write a big software stack, and if you start optimizing, like, the first thing you write, the odds of that being the performance limiter is low.  
**Translation:** 

**[2895.10s] English:** Right.  
**Translation:** 

**[2895.28s] English:** But when you get the whole thing working, can you make it 2x faster by optimizing the right things?  
**Translation:** Vocabulary: optimizing: 优化

**[2899.90s] English:** Sure.  
**Translation:** 

**[2900.96s] English:** While you're optimizing that, could you have written a new software stack, which would have been a better choice?  
**Translation:** 

**[2905.96s] English:** Maybe.  
**Translation:** 

**[2907.00s] English:** Now you have creative tension.  
**Translation:** 

**[2908.00s] English:** But the whole time, as you're doing the writing, that's the software we're talking about.  
**Translation:** 

**[2914.82s] English:** The hardware underneath gets faster and faster.  
**Translation:** 

**[2916.70s] English:** Well, it goes back to the Moore's Law.  
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
**Translation:** Vocabulary: rewriting: 修改算法

**[2934.90s] English:** Like, that seems like a failed strategy for the last 30 years.  
**Translation:** 

**[2938.00s] English:** Moore's Law is death.  
**Translation:** 

**[2939.96s] English:** So can you just linger on it?  
**Translation:** 

**[2943.00s] English:** I think you've answered it, but I'll just ask the same dumb question over and over.  
**Translation:** 

**[2946.88s] English:** So why do you think Moore's Law is not going to die?  
**Translation:** 

**[2952.42s] English:** Which is the most promising, exciting possibility of why it won't die in the next 5, 10 years?  
**Translation:** 

**[2958.04s] English:** So is it the continued shrinking of the transistor, or is it another S-curve that steps in and it totally sort of…  
**Translation:** 

**[2965.50s] English:** Well, the shrinking of the transistor is literally…  
**Translation:** Vocabulary: shrinking: 缩小; transistor: 晶体管

**[2968.00s] English:** It's literally thousands of innovations.  
**Translation:** 

**[2970.16s] English:** Right.  
**Translation:** Vocabulary: innovations: 创新

**[2970.50s] English:** So there's stacks of S-curves in there.  
**Translation:** 

**[2973.00s] English:** There's a whole bunch of S-curves just kind of running their course and being reinvented and new things.  
**Translation:** 

**[2980.60s] English:** You know, the semiconductor fabricators and technologists have all announced what's called nanowires.  
**Translation:** 

**[2987.46s] English:** So they took a fin, which had a gate around it, and turned that into little wires so you have better control of that.  
**Translation:** Vocabulary: fabricators: 半导体制造商; nanowires: 纳米线; semiconductor: 半导体; technologists: 技术专家

**[2993.98s] English:** And they're smaller.  
**Translation:** 

**[2995.40s] English:** And then from there, there are some obvious steps about how to…  
**Translation:** 

**[2997.96s] English:** How to shrink that.  
**Translation:** 

**[2999.32s] English:** So the metal…  
**Translation:** 

**[3000.00s] English:** Allergy around wire stacks and stuff has very obvious abilities to shrink.  
**Translation:** 

**[3007.26s] English:** And, you know, there's a whole combination of things there to do.  
**Translation:** Vocabulary: allergy: 过敏

**[3011.10s] English:** Your sense is that we're going to get a lot if this innovation from just that shrinking.  
**Translation:** 

**[3016.60s] English:** Yeah, like a factor of 100 is a lot.  
**Translation:** 

**[3019.12s] English:** Yeah, I would say that's incredible.  
**Translation:** 

**[3022.18s] English:** And it's totally unknown.  
**Translation:** 

**[3023.72s] English:** It's only 10 or 15 years.  
**Translation:** 

**[3025.02s] English:** Now, you're smart and you might know, but to me, it's totally unpredictable what that 100x would bring in terms of the nature of the computation that people would be.  
**Translation:** Vocabulary: computation: 计算

**[3034.24s] English:** Yeah, are you familiar with Bell's Law?  
**Translation:** 

**[3036.98s] English:** So, for a long time, it was mainframes, minis, workstation, PC, mobile.  
**Translation:** Vocabulary: mainframes: 大型机; workstation: 工作站

**[3042.58s] English:** Moore's Law drove faster, smaller computers, right?  
**Translation:** 

**[3046.18s] English:** And then when we were thinking about Moore's Law, Raja Gidori said every 10x generates a new computation.  
**Translation:** 

**[3053.12s] English:** So, scalar.  
**Translation:** 

**[3055.02s] English:** Vector, matrix, topological computation, right?  
**Translation:** Vocabulary: matrix: 矩阵; scalar: 标量; topological: 拓扑的

**[3061.00s] English:** And if you go look at the industry trends, there was, you know, mainframes and minicomputers and PCs.  
**Translation:** 

**[3067.08s] English:** And then the internet took off.  
**Translation:** Vocabulary: minicomputers: 小型计算机

**[3068.90s] English:** And then we got mobile devices.  
**Translation:** 

**[3070.70s] English:** And now we're building 5G wireless with one millisecond latency.  
**Translation:** Vocabulary: latency: 延迟; millisecond: 毫秒; wireless: 无线

**[3074.56s] English:** And people are starting to think about the smart world where everything knows you, recognizes you.  
**Translation:** 

**[3082.42s] English:** Like the transformations are going to be.  
**Translation:** Vocabulary: transformations: 变化

**[3085.36s] English:** Like unpredictable.  
**Translation:** 

**[3087.14s] English:** How does it make you feel that you're one of the key architects of this kind of future?  
**Translation:** 

**[3095.10s] English:** So, we're not talking about the architects of the high-level people who build the Angry Bird apps and Snapchat.  
**Translation:** 

**[3103.42s] English:** Angry Bird apps.  
**Translation:** 

**[3104.74s] English:** Who knows?  
**Translation:** 

**[3105.18s] English:** Maybe that's the whole point of the universe.  
**Translation:** 

**[3107.26s] English:** I'm going to take a stand at that and the attention-distracting nature of mobile phones.  
**Translation:** 

**[3112.80s] English:** I'll take a stand.  
**Translation:** 

**[3113.80s] English:** But anyway, in terms of...  
**Translation:** 

**[3115.00s] English:** I don't think that matters much.  
**Translation:** 

**[3117.58s] English:** The side effects of...  
**Translation:** 

**[3120.00s] English:** smartphones or the attention distraction which part well who knows you know where this is all  
**Translation:** Vocabulary: distraction: 注意力分散

**[3125.76s] English:** leading it's changing so fast wait so back my parents used to yell at my sisters for hiding  
**Translation:** 

**[3130.02s] English:** in the closet with a wired phone with a dial on it stop talking to your friends all day right  
**Translation:** Vocabulary: closet: 壁橱

**[3134.90s] English:** now my wife yells at my kids for talking to their friends all day on text  
**Translation:** 

**[3139.48s] English:** it looks the same to me it's always it's echoes of the same thing okay but you are the one of the  
**Translation:** 

**[3145.84s] English:** key people architecting the hardware of this future how does that make you feel do you feel  
**Translation:** 

**[3150.82s] English:** responsible do you feel excited so we're we're in a social context so there's billions of people  
**Translation:** Vocabulary: architecting: 设计

**[3159.14s] English:** on this planet there are literally millions of people working on technology i feel lucky to to be  
**Translation:** 

**[3167.06s] English:** you know what doing what i do and getting paid for it and there's an interest in it but there's  
**Translation:** 

**[3173.16s] English:** so many things going on in parallel it's  
**Translation:** 

**[3175.84s] English:** like the actions are so unpredictable if i wasn't here somebody else would do it  
**Translation:** 

**[3180.08s] English:** the the vectors of all these different things are happening all the time  
**Translation:** 

**[3184.58s] English:** you know there's a i'm sure some philosopher or meta philosophers you know wondering about  
**Translation:** 

**[3192.42s] English:** how we transform our world so you can't deny the fact that these tools whether  
**Translation:** 

**[3199.36s] English:** that these tools are changing our world that's right  
**Translation:** 

**[3204.94s] English:** so do you think  
**Translation:** 

**[3205.84s] English:** it's changing for the better somebody i read this thing recently it said the p the two disciplines  
**Translation:** Vocabulary: disciplines: 学科领域

**[3213.52s] English:** with the highest gre scores in college are physics and philosophy right and they're both sort of  
**Translation:** 

**[3220.58s] English:** trying to answer the question why is there anything right and the philosophers you know  
**Translation:** 

**[3225.50s] English:** are on the kind of theological side and the physicists are obviously on the you know the  
**Translation:** 

**[3230.64s] English:** material side and there's a hundred billion galaxies with a hundred billion galaxies and  
**Translation:** Vocabulary: galaxies: 星系; physicists: 物理学家; theological: 神学的

**[3235.84s] English:** a hundred billion stars it seems well repetitive at best  
**Translation:** 

**[3240.00s] English:** so i you know there's there's on our way to 10 billion people i mean it's hard to say what it's  
**Translation:** Vocabulary: repetitive: 陈词滥调

**[3247.60s] English:** all for if that's what you're asking yeah i guess i guess i am do tend to or significantly increases  
**Translation:** 

**[3253.84s] English:** in complexity and i'm i'm curious about how computation like like our world our physical  
**Translation:** Vocabulary: complexity: 复杂性; computation: 计算

**[3262.72s] English:** world inherently generates mathematics it's kind of obvious right so we have xyz coordinates  
**Translation:** 

**[3268.16s] English:** you take a sphere you make it bigger you get a surface that falls you know grows by r squared  
**Translation:** 

**[3273.48s] English:** like it generally generates mathematics and the mathematicians and the physicists  
**Translation:** 

**[3278.04s] English:** have been having a lot of fun talking to each other for years and computation has been  
**Translation:** Vocabulary: mathematicians: 数学家

**[3282.86s] English:** let's say relatively pedestrian like computation in terms of mathematics has been doing binary  
**Translation:** 

**[3290.04s] English:** binary algebra while those guys have been gallivanting through the other realms of possibility  
**Translation:** Vocabulary: algebra: 代数; binary: 二进制; pedestrian: 普通

**[3298.16s] English:** now recently the computation lets you do mathematic mathematical computations that are  
**Translation:** 

**[3305.00s] English:** sophisticated enough that nobody understands how the answers came out right machine learning  
**Translation:** Vocabulary: computations: 计算; mathematical: 数学的; sophisticated: 复杂的

**[3310.62s] English:** machine learning yeah it used to be you get data set you guess at a function the function  
**Translation:** 

**[3317.20s] English:** is considered physics if it's predictive of new functions new data sets modern  
**Translation:** Vocabulary: predictive: 预测性的

**[3323.48s] English:** you can take a large data set and you can take a large data set and you can take a large data set  
**Translation:** 

**[3328.16s] English:** with no intuition about what it is and use machine learning to find a pattern that has no function  
**Translation:** Vocabulary: intuition: 直觉

**[3333.72s] English:** right and it can arrive at results that i don't know if they're completely mathematically  
**Translation:** 

**[3339.00s] English:** describable so computation has kind of done something interesting compared to a equal b plus c  
**Translation:** Vocabulary: describable: 可描述; mathematically: 数学上

**[3347.08s] English:** there's something reminiscent of that step from the the basic operations of addition  
**Translation:** 

**[3354.68s] English:** to taking a step towards neural networks that's reminiscent of what  
**Translation:** Vocabulary: neural: 神经网络; reminiscent: 类似

**[3358.04s] English:** we've been doing for years and years and years and years and years and years and years and years  
**Translation:** 

**[3358.10s] English:** and years and years and years and years and years and years and years and years and years and years  
**Translation:** 

**[3358.14s] English:** and years and years and years and years and years and years and years and years life on earth at its origins was  
**Translation:** 

**[3360.00s] English:** doing do you think we're creating sort of the next step in our evolution in in creating artificial  
**Translation:** 

**[3365.92s] English:** intelligence systems that will i don't know i mean there's so much in the universe already it's hard  
**Translation:** 

**[3371.34s] English:** to say where we stand like in this whole thing human beings working on additional abstraction  
**Translation:** Vocabulary: abstraction: 抽象

**[3376.84s] English:** layers and possibilities yeah it appears so does that mean that human beings don't need dogs you  
**Translation:** 

**[3383.14s] English:** know no like like there's so many things that are all simultaneously interesting and useful  
**Translation:** 

**[3390.08s] English:** but you've seen throughout your career you've seen greater and greater level abstractions  
**Translation:** 

**[3394.58s] English:** built in artificial machines right do you think when you look at humans you think  
**Translation:** Vocabulary: abstractions: 抽象层次

**[3402.30s] English:** look at all the life on earth as a single organism building this  
**Translation:** 

**[3405.76s] English:** thing this machine with greater and greater levels of abstraction do you think humans are the peak  
**Translation:** 

**[3412.10s] English:** the top  
**Translation:** 

**[3413.12s] English:** of the food chain in this long arc of history on earth or do you think we're just somewhere in the  
**Translation:** 

**[3419.84s] English:** middle are we are we the basic functional operations of a cpu are we the c++ program  
**Translation:** 

**[3427.96s] English:** the python program or with the neural network like somebody's you know people have calculated  
**Translation:** 

**[3432.76s] English:** like how many operations does the brain do something you know i've seen the number 10 to  
**Translation:** 

**[3437.10s] English:** the 18th about a bunch of times arrived different ways so could you make a computer that did 10 to  
**Translation:** 

**[3442.72s] English:** the 20th operation yes sure do you think we're going to do that now is there something magical  
**Translation:** 

**[3449.16s] English:** about how brains compute things i don't know you know my personal experience is is interesting  
**Translation:** 

**[3455.10s] English:** because you know you think you know how you think and then you have all these ideas and you can't  
**Translation:** 

**[3459.36s] English:** figure out how they happened and if you meditate you know the like what what you can be aware of  
**Translation:** 

**[3467.02s] English:** is interesting so i don't know if brains are magical or not you know the physical  
**Translation:** 

**[3472.72s] English:** evidence says no lots of people's personal experience says yes so what would be funny as if  
**Translation:** 

**[3480.00s] English:** brains are magical and yet we can make brains with more computation you know i don't know what  
**Translation:** 

**[3485.28s] English:** to say about that but what do you think uh magic is an emergent phenomena what would be i have let  
**Translation:** Vocabulary: computation: 计算; emergent: 涌现

**[3491.78s] English:** me i have no explanation let me ask jim keller of what what what in your view is consciousness  
**Translation:** 

**[3497.34s] English:** with with consciousness yeah like what uh you know consciousness uh love things that are these  
**Translation:** Vocabulary: keller: 凯勒

**[3506.32s] English:** deeply human things that seems to emerge from our brain is that something that we'll be able to  
**Translation:** 

**[3511.38s] English:** make in code in chips that get faster and faster and faster and faster that's like a 10 hour  
**Translation:** 

**[3519.00s] English:** conversation nobody really knows can you summarize it in a couple of a couple of words um many people  
**Translation:** 

**[3526.00s] English:** have observed that organisms run at lots of different levels right if you had two neurons  
**Translation:** Vocabulary: neurons: 神经元; summarize: 概括

**[3532.30s] English:** somebody said you'd have one sensory neuron and one motor neuron  
**Translation:** 

**[3535.10s] English:** right  
**Translation:** Vocabulary: neuron: 神经元

**[3536.42s] English:** so we move towards things and away from things and we have physical integrity and safety or not  
**Translation:** 

**[3541.64s] English:** right and then if you look at the animal kingdom you can see brains that are a little more  
**Translation:** 

**[3547.10s] English:** complicated and at some point there's a planning system and then there's an emotional system that's  
**Translation:** 

**[3552.72s] English:** you know happy about being safe or unhappy about being threatened right and then our brains have  
**Translation:** 

**[3559.22s] English:** massive numbers of structures you know like planning and movement and thinking and feeling  
**Translation:** 

**[3565.48s] English:** and drive  
**Translation:** 

**[3566.32s] English:** and emotions and we seem to have multiple layers of thinking systems and we have a brain a dream  
**Translation:** 

**[3572.38s] English:** system that nobody understands whatsoever which i find completely hilarious and  
**Translation:** 

**[3577.82s] English:** you can think in a way that those systems are more independent and you can observe you know  
**Translation:** 

**[3586.76s] English:** the different parts of yourself can observe them i don't know which one's magical i don't know which  
**Translation:** 

**[3592.02s] English:** one's not computational so  
**Translation:** 

**[3596.32s] English:** Is it possible that it's all computation?  
**Translation:** Vocabulary: computational: 计算相关的

**[3598.88s] English:** Probably.  
**Translation:** 

**[3600.00s] English:** Is there a limit to computation?  
**Translation:** 

**[3601.50s] English:** I don't think so.  
**Translation:** 

**[3603.12s] English:** Do you think the universe is a computer?  
**Translation:** 

**[3607.04s] English:** It's a weird kind of computer,  
**Translation:** 

**[3609.24s] English:** because if it was a computer,  
**Translation:** 

**[3612.16s] English:** like when they do calculations on what it,  
**Translation:** 

**[3615.06s] English:** how much calculation it takes to describe quantum effects  
**Translation:** 

**[3618.28s] English:** is unbelievably high.  
**Translation:** 

**[3620.58s] English:** So if it was a computer,  
**Translation:** Vocabulary: unbelievably: 难以置信地

**[3622.24s] English:** wouldn't you have built it out of something  
**Translation:** 

**[3623.44s] English:** that was easier to compute?  
**Translation:** 

**[3626.24s] English:** That's a funny system.  
**Translation:** 

**[3628.82s] English:** But then the simulation guys have pointed out  
**Translation:** Vocabulary: simulation: 模拟系统

**[3631.26s] English:** that the rules are kind of interesting.  
**Translation:** 

**[3632.76s] English:** Like when you look really close, it's uncertain.  
**Translation:** 

**[3635.06s] English:** And the speed of light says you can only look so far,  
**Translation:** 

**[3637.56s] English:** and things can't be simultaneous,  
**Translation:** Vocabulary: simultaneous: 同时发生

**[3639.16s] English:** except for the odd entanglement problem  
**Translation:** 

**[3641.14s] English:** where they seem to be.  
**Translation:** Vocabulary: entanglement: 纠缠问题

**[3642.50s] English:** Like the rules are all kind of weird.  
**Translation:** 

**[3645.10s] English:** And somebody said physics is like having 50 equations  
**Translation:** Vocabulary: equations: 方程式

**[3648.68s] English:** with 50 variables to define 50 variables.  
**Translation:** 

**[3652.28s] English:** Like, you know, it's, you know,  
**Translation:** 

**[3655.20s] English:** like physics itself has been a shit show  
**Translation:** 

**[3656.90s] English:** for thousands of years.  
**Translation:** 

**[3658.82s] English:** It seems odd when you get to the corners of everything.  
**Translation:** 

**[3661.52s] English:** You know, it's either uncomputable  
**Translation:** Vocabulary: uncomputable: 无法计算的

**[3663.52s] English:** or undefinable or uncertain.  
**Translation:** 

**[3667.28s] English:** It's almost like the designers of the simulation  
**Translation:** Vocabulary: designers: 设计者; undefinable: 无法定义

**[3669.20s] English:** are trying to prevent us from understanding it perfectly.  
**Translation:** 

**[3672.96s] English:** But also the things that require calculations  
**Translation:** 

**[3675.96s] English:** require so much calculation  
**Translation:** 

**[3677.56s] English:** that our idea of the universe of a computer is absurd  
**Translation:** 

**[3680.70s] English:** because every single little bit of it  
**Translation:** 

**[3682.88s] English:** takes all the computation in the universe to figure out.  
**Translation:** 

**[3686.32s] English:** So that's a weird kind of computer.  
**Translation:** 

**[3688.16s] English:** You know, you say,  
**Translation:** 

**[3688.66s] English:** the simulation is running in the computer,  
**Translation:** 

**[3690.80s] English:** which has, by definition, infinite computation.  
**Translation:** Vocabulary: computation: 计算

**[3694.46s] English:** Not infinite.  
**Translation:** 

**[3695.40s] English:** Oh, you mean if the universe is infinite?  
**Translation:** 

**[3697.52s] English:** Yeah.  
**Translation:** 

**[3698.28s] English:** Well, every little piece of our universe  
**Translation:** 

**[3700.34s] English:** seems to take infinite computation to figure out.  
**Translation:** 

**[3703.26s] English:** Not infinite, just a lot.  
**Translation:** 

**[3704.20s] English:** Well, a lot's a pretty big number.  
**Translation:** 

**[3706.08s] English:** Compute this little teeny spot,  
**Translation:** Vocabulary: teeny: 微小的

**[3708.16s] English:** takes all the mass in the local  
**Translation:** 

**[3711.02s] English:** one light year by one light year space.  
**Translation:** 

**[3713.50s] English:** It's close enough to infinite.  
**Translation:** 

**[3714.96s] English:** Oh, it's a heck of a computer if it is one.  
**Translation:** 

**[3716.58s] English:** I know.  
**Translation:** 

**[3716.94s] English:** It's a weird.  
**Translation:** 

**[3718.66s] English:** It's a weird description.  
**Translation:** 

**[3720.00s] English:** the simulation description seems to to break when you look closely at it but the rules of the  
**Translation:** 

**[3725.52s] English:** universe seem to imply something's up that seems a little arbitrary the whole the universe the whole  
**Translation:** 

**[3732.40s] English:** thing the the laws of physics yeah it just seems like like how did it come out to be yeah the way  
**Translation:** Vocabulary: arbitrary: 随意

**[3739.60s] English:** it is but lots of people talk about that it's you know it's like i said the two smartest groups of  
**Translation:** 

**[3744.00s] English:** humans are working on the same problem from different different aspects and they're both  
**Translation:** 

**[3748.16s] English:** complete failures so that's that's kind of cool they might succeed eventually well after  
**Translation:** 

**[3755.84s] English:** two thousand years the trend isn't good oh two thousand years is nothing in the span of the  
**Translation:** 

**[3760.40s] English:** history of the universe so we have some time but the next thousand years doesn't look good either  
**Translation:** 

**[3765.20s] English:** so that's what everybody says at every stage but uh with moore's law as you've just described not  
**Translation:** 

**[3771.52s] English:** being dead the exponential growth of technology the future seems pretty incredible well it'll be  
**Translation:** 

**[3778.08s] English:** a little bit different but it's a little bit different but it's a little bit different but  
**Translation:** Vocabulary: exponential: 指数的

**[3778.14s] English:** interesting that's for sure that's right so what are your thoughts on ray kurzweil's sense that  
**Translation:** 

**[3783.90s] English:** exponential improvement and technology will continue indefinitely that is that how you see  
**Translation:** 

**[3789.18s] English:** moore's law do you see moore's law more broadly in the sense that technology of all kinds  
**Translation:** 

**[3796.86s] English:** has a way of stacking s curves on top of each other where it'll be exponential and  
**Translation:** Vocabulary: stacking: 叠加

**[3803.18s] English:** then we'll see all kinds of what does an exponential of a million mean that's that's  
**Translation:** 

**[3808.06s] English:** a pretty amazing number and that's just for a local little piece of silicon now let's imagine you say  
**Translation:** 

**[3814.46s] English:** decided to get a thousand tons of silicon to collaborate in one computer at a million times  
**Translation:** 

**[3822.30s] English:** the density like now now you're talking i don't know 10 to the 20th more computation power  
**Translation:** Vocabulary: collaborate: 合作; computation: 计算; density: 密度

**[3829.66s] English:** than our current already unbelievably fast computers  
**Translation:** 

**[3833.90s] English:** like nobody knows what that's going to mean you know the sci-fi guy is called you know computronium  
**Translation:** Vocabulary: unbelievably: 难以置信地

**[3838.06s] English:** like when  
**Translation:** 

**[3840.00s] English:** a local civilization turns the nearby star into a computer right like i don't think that's true but  
**Translation:** 

**[3846.64s] English:** so just even when you shrink a transistor the that's only one dimension the ripple effects of  
**Translation:** 

**[3853.68s] English:** that like people tend to think about computers as a cost problem right so computers are made  
**Translation:** Vocabulary: dimension: 维度; ripple: 影响; transistor: 晶体管

**[3858.48s] English:** out of silicon and minor amounts of metals and you know this and that none of those things cost  
**Translation:** 

**[3865.68s] English:** any money like there's plenty of sand like like you could just turn the beach and a little bit  
**Translation:** 

**[3871.60s] English:** ocean water into computers so all the cost is in the equipment to do it and the trend on equipment  
**Translation:** 

**[3877.84s] English:** is once you figure out how to build the equipment the trend of cost is zero elon said first you  
**Translation:** 

**[3882.72s] English:** figure out what configuration you want the atoms in and then how to put them there right yeah  
**Translation:** 

**[3890.80s] English:** because well what here's the you know his his great insight is people are how  
**Translation:** Vocabulary: configuration: 结构设置

**[3895.68s] English:** to build a computer and they're not constrained i have this thing i know how it works and then  
**Translation:** 

**[3901.84s] English:** little tweaks to that will generate something as opposed to what do i actually want and then  
**Translation:** Vocabulary: constrained: 限制; tweaks: 微调

**[3907.36s] English:** figure out how to build it it's a very different mindset and almost nobody has it obviously  
**Translation:** 

**[3914.32s] English:** well let me ask on that topic you were one of the key early people in the development of autopilot  
**Translation:** Vocabulary: mindset: 思维模式

**[3921.36s] English:** at least in the hardware side elon musk believes that autopilot and vehicle autonomy if you just  
**Translation:** 

**[3925.60s] English:** look at that problem can follow this kind of exponential improvement in terms of the ha the  
**Translation:** Vocabulary: autonomy: 自主性; exponential: 指数的

**[3930.88s] English:** how question that we're talking about there's no reason why you can't what are your thoughts  
**Translation:** 

**[3935.60s] English:** on this particular space of vehicle autonomy and you're a part of it and elon musk's and tesla's  
**Translation:** 

**[3943.92s] English:** vision for well the computer you need to build was straightforward and you could argue well does  
**Translation:** 

**[3950.00s] English:** it need to be two times faster or five times or ten times but that's just a matter of fact  
**Translation:** Vocabulary: straightforward: 简单明了

**[3955.60s] English:** time or price in the short run so that's that's not a big deal  
**Translation:** 

**[3960.00s] English:** You don't have to be especially smart to drive a car.  
**Translation:** 

**[3963.18s] English:** So it's not like a super hard problem.  
**Translation:** 

**[3965.72s] English:** I mean, the big problem with safety is attention,  
**Translation:** 

**[3967.88s] English:** which computers are really good at, not skills.  
**Translation:** 

**[3972.68s] English:** Well, let me push back on one.  
**Translation:** 

**[3975.30s] English:** You say everything you said is correct,  
**Translation:** 

**[3976.88s] English:** but we as humans tend to take for granted  
**Translation:** 

**[3984.18s] English:** how incredible our vision system is.  
**Translation:** 

**[3987.44s] English:** You can drive a car with 20-50 vision.  
**Translation:** 

**[3990.56s] English:** And you can train a neural network  
**Translation:** 

**[3992.04s] English:** to extract the distance of any object  
**Translation:** 

**[3994.56s] English:** and the shape of any surface from a video and data.  
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
**Translation:** Vocabulary: detecting: 检测对象

**[4010.52s] English:** It's understanding the scene.  
**Translation:** 

**[4012.34s] English:** And it's being able to do it in a way that doesn't make errors.  
**Translation:** 

**[4016.58s] English:** So the beautiful thing about the human vision system  
**Translation:** 

**[4019.40s] English:** is...  
**Translation:** 

**[4020.00s] English:** And our entire brain around the whole thing  
**Translation:** 

**[4022.22s] English:** is we're able to fill in the gaps.  
**Translation:** 

**[4025.24s] English:** It's not just about perfectly detecting cars.  
**Translation:** 

**[4028.00s] English:** It's inferring the occluded cars.  
**Translation:** Vocabulary: inferring: 推断; occluded: 被遮挡的

**[4030.06s] English:** It's trying to...  
**Translation:** 

**[4030.70s] English:** It's understanding the physics.  
**Translation:** 

**[4032.28s] English:** I think that's mostly a data problem.  
**Translation:** 

**[4034.46s] English:** So you think what data would compute  
**Translation:** 

**[4037.42s] English:** with improvement in computation,  
**Translation:** 

**[4039.20s] English:** with improvement in collection?  
**Translation:** Vocabulary: computation: 计算

**[4040.68s] English:** Well, there is a...  
**Translation:** 

**[4041.36s] English:** When you're driving a car and somebody cuts you off,  
**Translation:** 

**[4043.62s] English:** your brain has theories about why they did it.  
**Translation:** 

**[4046.16s] English:** They're a bad person.  
**Translation:** 

**[4047.50s] English:** They're distracted.  
**Translation:** 

**[4048.64s] English:** They're dumb.  
**Translation:** Vocabulary: distracted: 心不在焉

**[4050.00s] English:** You know, you can listen to yourself.  
**Translation:** 

**[4051.92s] English:** Right.  
**Translation:** 

**[4052.74s] English:** So, you know, if you think that narrative is important  
**Translation:** 

**[4056.88s] English:** to be able to successfully drive a car,  
**Translation:** 

**[4058.86s] English:** then current autopilot systems can't do it.  
**Translation:** 

**[4061.66s] English:** But if cars are ballistic things with tracks  
**Translation:** Vocabulary: ballistic: 弹道的

**[4064.28s] English:** and probabilistic changes of speed and direction,  
**Translation:** 

**[4067.30s] English:** and roads are fixed and given, by the way,  
**Translation:** Vocabulary: probabilistic: 概率性的

**[4069.90s] English:** they don't change dynamically, right?  
**Translation:** 

**[4073.22s] English:** You can map the world really thoroughly.  
**Translation:** Vocabulary: dynamically: 随时间变化

**[4075.52s] English:** You can place every object really thoroughly.  
**Translation:** 

**[4080.00s] English:** right you can calculate trajectories of things really thoroughly right but everything you said  
**Translation:** Vocabulary: trajectories: 运动轨迹

**[4088.42s] English:** about really thoroughly has a different degree of difficulty so and you could say at some point  
**Translation:** 

**[4094.66s] English:** computer autonomous systems will be way better at things that humans are lousy at like they'll be  
**Translation:** Vocabulary: autonomous: 自主的

**[4100.98s] English:** better at attention they'll always remember there was a pothole in the road that humans keep  
**Translation:** 

**[4105.84s] English:** forgetting about they'll remember that this set of roads has these weirdo lines on it that the  
**Translation:** Vocabulary: pothole: 坑洼; weirdo: 怪人

**[4111.62s] English:** computers figured out once and and especially if they get updates so if somebody changes a given  
**Translation:** 

**[4116.88s] English:** right like the key to robots and stuff somebody said is to maximize the givens  
**Translation:** Vocabulary: maximize: 最大化

**[4123.76s] English:** right right right so so having a robot pick up this bottle cap is way easier to put a red dot  
**Translation:** 

**[4129.18s] English:** on the top because then you have to figure out you know and if you want to do a certain thing  
**Translation:** 

**[4134.06s] English:** with it you know maximize the givens  
**Translation:** 

**[4135.84s] English:** is the thing and autonomous systems are happily maximizing the givens like like humans when you  
**Translation:** Vocabulary: maximizing: 最大化

**[4142.42s] English:** drive someplace new you remember it because you're processing it the whole time and after  
**Translation:** 

**[4147.18s] English:** the 50th time you drove to work you get to work you don't know how you got there right you're on  
**Translation:** Vocabulary: someplace: 某个地方

**[4151.72s] English:** autopilot right autonomous cars are always on autopilot but the cars have no theories about  
**Translation:** 

**[4159.16s] English:** why they got cut off or why they're in traffic so they also never stop paying attention right so  
**Translation:** 

**[4165.84s] English:** i tend to believe you do have to have theories mental models of other people  
**Translation:** 

**[4169.54s] English:** uh especially with pedestrian cyclists but also with other cars so everything you said  
**Translation:** 

**[4175.54s] English:** is uh like is actually essential to driving driving is a lot more complicated than people  
**Translation:** 

**[4181.02s] English:** realize i think so sort of to push back slightly but to cut into traffic right yeah you can't just  
**Translation:** 

**[4187.50s] English:** wait for a gap you have to be somewhat aggressive you'll be surprised how simple the calculation for  
**Translation:** 

**[4192.22s] English:** that is i may be on that particular point but there's a lot of people who are trying to figure  
**Translation:** 

**[4195.18s] English:** out what's going on in the city and they're trying to figure out what's going on in the city and they're  
**Translation:** 

**[4195.68s] English:** trying to figure out what's going on in the city and they're trying to figure out what's going on in the city and they're  
**Translation:** 

**[4195.84s] English:** trying to figure out what's going on in the city and they're trying to figure out what's going on in the city  
**Translation:** 

**[4196.64s] English:** yeah i i i think what's going on in the city that's that i think i like that strife too  
**Translation:** Vocabulary: strife: 争端

**[4200.00s] English:** back i would be surprised you know what yeah i'll just say where i stand i would be very surprised  
**Translation:** 

**[4204.06s] English:** but i think it's you might be surprised how complicated it is that i say i tell people  
**Translation:** 

**[4210.62s] English:** like progress disappoints in the short run surprises in the long run it's very possible  
**Translation:** 

**[4214.80s] English:** yeah i suspect in 10 years it'll be just like taken for granted yeah probably but you're probably  
**Translation:** Vocabulary: disappoints: 令人失望

**[4221.16s] English:** right and i'll look like it's going to be a 50 solution that nobody cares about it's like gps  
**Translation:** 

**[4225.70s] English:** is like wow gps is we have satellites in space yeah that tell you where your location is it was  
**Translation:** 

**[4231.22s] English:** a really big deal now everything has a gps in it yeah that's true but i i do think that systems  
**Translation:** 

**[4235.90s] English:** that involve human behavior are more complicated than we give them credit for so we can do  
**Translation:** 

**[4241.90s] English:** incredible things with technology that don't involve humans but when you think humans are  
**Translation:** 

**[4246.06s] English:** less complicated than people you know frequently ascribe maybe i feel we tend to operate out of  
**Translation:** Vocabulary: ascribe: 归因

**[4252.44s] English:** large numbers of patterns and just keep doing it over and over  
**Translation:** 

**[4255.70s] English:** but i can't trust you because you're a human that's something something a human would say  
**Translation:** 

**[4260.24s] English:** but my hope is on the point you've made is even if no matter who's right even there i'm hoping that  
**Translation:** 

**[4269.80s] English:** there's a lot of things that humans aren't good at that machines are definitely good at like you  
**Translation:** 

**[4273.62s] English:** said attention and things like that well they'll be so much better that the overall picture of  
**Translation:** 

**[4278.78s] English:** safety and autonomy will be obviously cars will be safer even if they're not as good i'm a big  
**Translation:** Vocabulary: autonomy: 自主权

**[4285.04s] English:** believer in safety  
**Translation:** 

**[4285.70s] English:** i mean there are already the current safety systems like cruise control that doesn't let  
**Translation:** Vocabulary: believer: 信仰者

**[4291.06s] English:** you run into people and lane keeping there are so many features that you just look at the Pareto of  
**Translation:** 

**[4296.54s] English:** accidents and knocking off like 80 of them is you know super doable just to linger on the  
**Translation:** Vocabulary: doable: 可行的; pareto: 帕累托图

**[4303.76s] English:** autopilot team and the efforts there the it seems to be that there's a very intense  
**Translation:** 

**[4310.56s] English:** scrutiny by the media and the public in terms of safety the pressure the bar  
**Translation:** Vocabulary: scrutiny: 审查

**[4315.70s] English:** and the safety of the vehicle and the safety of the vehicle and the safety of the vehicle  
**Translation:** 

**[4320.00s] English:** there working on the hardware and trying to build a system that builds a safe vehicle and so on  
**Translation:** 

**[4326.46s] English:** what was your sense about that pressure is it unfair is it expected of new technology  
**Translation:** 

**[4331.54s] English:** yeah it seems reasonable i was interested i talked to both american and european regulators  
**Translation:** 

**[4336.46s] English:** and i was worried that the regulations would write into the rules technology solutions  
**Translation:** 

**[4344.38s] English:** like modern brake systems imply hydraulic brakes so if you read the regulations to meet the letter  
**Translation:** 

**[4353.14s] English:** of the law for brakes it sort of has to be hydraulic right and the regulator said they're  
**Translation:** 

**[4359.66s] English:** they're interested in the use cases like a head-on crash an offset crash don't hit pedestrians don't  
**Translation:** Vocabulary: hydraulic: 液压; pedestrians: 行人; regulator: 调节器

**[4365.90s] English:** run into people don't leave the road don't run a red light or a stoplight they were very much into  
**Translation:** 

**[4371.32s] English:** the scenarios and you know and they had  
**Translation:** Vocabulary: scenarios: 情景; stoplight: 红绿灯

**[4374.38s] English:** they had all the data about which scenarios injured or killed the most people  
**Translation:** 

**[4379.26s] English:** and for the most part those conversations were like what's the right thing to do to take the  
**Translation:** 

**[4387.10s] English:** next step now elon's very interested also in the the benefits of autonomous driving or freeing  
**Translation:** 

**[4393.34s] English:** people's time and attention as well as safety um and i think that's also an interesting thing but  
**Translation:** Vocabulary: autonomous: 自主

**[4401.74s] English:** you know building autonomous systems  
**Translation:** 

**[4404.38s] English:** they're safe and safer than people seemed since the goal is to be tannic safer than people  
**Translation:** 

**[4409.98s] English:** having the bar to be safer than people and scrutinizing accidents seems  
**Translation:** 

**[4415.26s] English:** philosophically you know correct so i think that's a good thing what are is is different than the  
**Translation:** Vocabulary: philosophically: 从哲学角度看; scrutinizing: 仔细审查

**[4424.54s] English:** things that you worked at the intel amd apple with autopilot chip design and hardware design  
**Translation:** 

**[4433.26s] English:** what are interesting or  
**Translation:** 

**[4434.38s] English:** challenging aspects of building this specialized kind of computing system in the automotive space  
**Translation:** 

**[4440.00s] English:** I mean, there's two tricks to building an automotive computer.  
**Translation:** Vocabulary: automotive: 汽车相关的; computing: 计算

**[4442.76s] English:** One is the software team, the machine learning team,  
**Translation:** 

**[4446.94s] English:** is developing algorithms that are changing fast.  
**Translation:** 

**[4450.56s] English:** So as you're building the accelerator,  
**Translation:** 

**[4454.06s] English:** you have this worry or intuition that the algorithms will change enough  
**Translation:** Vocabulary: accelerator: 加速器; intuition: 直觉

**[4458.40s] English:** that the accelerator will be the wrong one.  
**Translation:** 

**[4462.48s] English:** And there's the generic thing,  
**Translation:** 

**[4464.62s] English:** which is if you build a really good general-purpose computer,  
**Translation:** 

**[4467.22s] English:** say its performance is one,  
**Translation:** 

**[4468.96s] English:** and then GPU guys will deliver about 5x the performance  
**Translation:** 

**[4473.36s] English:** for the same amount of silicon,  
**Translation:** 

**[4475.74s] English:** because instead of discovering parallelism, you're given parallelism.  
**Translation:** 

**[4479.28s] English:** And then special accelerators get another 2 to 5x on top of a GPU,  
**Translation:** 

**[4485.42s] English:** because you say, I know the math is always 8-bit integers  
**Translation:** 

**[4488.76s] English:** into 32-bit accumulators,  
**Translation:** Vocabulary: accumulators: 累加器; integers: 整数

**[4491.04s] English:** and the operations are the subset of mathematical possibilities.  
**Translation:** 

**[4495.16s] English:** So, you know, AI accelerators have a,  
**Translation:** Vocabulary: accelerators: 加速器; mathematical: 数学的

**[4498.96s] English:** claimed performance benefit over GPUs  
**Translation:** 

**[4501.72s] English:** because in the narrow math space you're nailing the algorithm.  
**Translation:** Vocabulary: algorithm: 算法

**[4507.08s] English:** Now, you still try to make it programmable,  
**Translation:** 

**[4510.00s] English:** but the AI field is changing really fast.  
**Translation:** 

**[4513.24s] English:** So there's a, you know, there's a little creative tension there of,  
**Translation:** 

**[4517.26s] English:** I want the acceleration afforded by specialization  
**Translation:** Vocabulary: acceleration: 加速; afforded: 提供

**[4520.56s] English:** without being over-specialized so that the new algorithm is so much more effective  
**Translation:** 

**[4525.54s] English:** that you would have been better off on a GPU.  
**Translation:** 

**[4527.90s] English:** So there is a tension there.  
**Translation:** 

**[4529.60s] English:** To build a good computer for an application like automotive,  
**Translation:** 

**[4534.06s] English:** there's all kinds of sensor inputs and safety processors and a bunch of stuff.  
**Translation:** 

**[4539.14s] English:** So one of Elon's goals is to make it super affordable.  
**Translation:** Vocabulary: processors: 处理器; sensor: 传感器

**[4542.18s] English:** So every car gets an autopilot computer.  
**Translation:** 

**[4544.80s] English:** So some of the recent startups you look at,  
**Translation:** Vocabulary: startups: 新兴企业

**[4546.48s] English:** and they have a server in the trunk,  
**Translation:** 

**[4548.28s] English:** because they're saying, I'm going to build this autopilot computer  
**Translation:** 

**[4550.58s] English:** that replaces the driver.  
**Translation:** 

**[4552.16s] English:** So their cost budget's $10,000 or $20,000.  
**Translation:** 

**[4555.10s] English:** And Elon's constraint was, I'm going to put one in every car,  
**Translation:** 

**[4558.68s] English:** whether people buy autopilot or not,  
**Translation:** Vocabulary: constraint: 限制

**[4560.00s] English:** him striping or not so the the cost constraint he had in mind was great right and to hit that  
**Translation:** 

**[4566.72s] English:** you had to think about the system design that's complicated it's it's fun you know it's like  
**Translation:** Vocabulary: striping: 条带写

**[4570.72s] English:** it's like it's krestman's work like you know a violin maker right you can say stradivarius  
**Translation:** 

**[4575.44s] English:** is this incredible thing the musicians are incredible but the guy making the violin you  
**Translation:** Vocabulary: stradivarius: 斯特拉迪瓦里

**[4580.16s] English:** know picked wood and sanded it and then he cut it you know and he glued it you know and he waited  
**Translation:** 

**[4586.24s] English:** for the right day so that when you put the finish on it it didn't you know do something dumb that's  
**Translation:** Vocabulary: glued: 粘合

**[4591.68s] English:** craftsman's work right you may be a genius craftsman because you have the best techniques  
**Translation:** 

**[4596.64s] English:** and you discover a new one but most engineering's craftsman's work and humans really like to do that  
**Translation:** Vocabulary: craftsman: 手工艺人

**[4604.08s] English:** you know smart humans no everybody all humans i don't know i used to i dug ditches when i was in  
**Translation:** 

**[4609.84s] English:** college i got really good at it satisfying yeah so digging dishes is also craftsman yeah of course  
**Translation:** Vocabulary: ditches: 沟渠

**[4616.88s] English:** oh so there's an expression called complex mastery behavior so when you're learning something  
**Translation:** 

**[4621.92s] English:** that's fun because you're learning something when you do something it's road and simple it's not  
**Translation:** 

**[4625.84s] English:** that satisfying but if the steps that you have to do are complicated and you're good at them  
**Translation:** 

**[4631.68s] English:** it's satisfying to do them and then if you're intrigued by it all as you're doing them you  
**Translation:** Vocabulary: intrigued: 好奇

**[4637.68s] English:** sometimes learn new things that you can raise your game but krestman's work is good and engineers  
**Translation:** 

**[4645.04s] English:** like engineering is complex  
**Translation:** 

**[4646.24s] English:** complicated enough that you have to learn a lot of skills and then a lot of what you do is then  
**Translation:** 

**[4650.74s] English:** craftsman's work which is fun autonomous driving building a very resource constrained computer so  
**Translation:** Vocabulary: autonomous: 自主的; constrained: 受限的

**[4657.92s] English:** computer has to be cheap enough that put in every single car that's essentially boils down to  
**Translation:** 

**[4663.10s] English:** craftsman's work it's engineering you know there's thoughtful decisions and problems to solve and  
**Translation:** Vocabulary: thoughtful: 深思熟虑的

**[4669.08s] English:** trade-offs to make you need 10 camera imports or eight you know you're building for the current  
**Translation:** 

**[4674.18s] English:** car the next one you know how do you do the safety stuff you know there's there's a whole bunch of  
**Translation:** 

**[4679.24s] English:** details  
**Translation:** 

**[4680.00s] English:** but it's fun but it's not like i'm building a new type of neural network which has a new  
**Translation:** 

**[4685.28s] English:** mathematics and a new computer to work you know that that's like there's a there's more invention  
**Translation:** 

**[4690.74s] English:** than that but the rejection to practice once you pick the architecture you look inside and what do  
**Translation:** Vocabulary: rejection: 拒绝

**[4696.36s] English:** you see adders and multipliers and memories and you know the basics so computers is always this  
**Translation:** 

**[4703.38s] English:** this weird set of abstraction layers of ideas and thinking that reduction to practice  
**Translation:** Vocabulary: abstraction: 抽象; multipliers: 乘法器

**[4708.62s] English:** is transistors and wires and you know pretty basic stuff and that's an interesting phenomena  
**Translation:** 

**[4716.02s] English:** by the way that like factory work like lots of people think factory work is road assembly stuff  
**Translation:** Vocabulary: transistors: 晶体管

**[4721.66s] English:** i've been on the assembly line like the people who work there really like it it's a really great job  
**Translation:** 

**[4727.30s] English:** it's really complicated putting cars together is hard right and and the car is moving and the parts  
**Translation:** 

**[4732.84s] English:** are moving and sometimes the parts are damaged and you have to coordinate putting all the stuff  
**Translation:** 

**[4736.98s] English:** together and people are good at it  
**Translation:** Vocabulary: coordinate: 协调

**[4738.62s] English:** they're good at it and i remember one day i went to work and the line was shut down for some reason  
**Translation:** 

**[4743.78s] English:** and some of the guys sitting around were really bummed because they they had reorganized a bunch  
**Translation:** 

**[4748.66s] English:** of stuff and they were going to hit a new record for the number of cars built that day and they  
**Translation:** 

**[4752.98s] English:** were all gung-ho to do it and these were big tough buggers and uh you know but what they did  
**Translation:** 

**[4758.36s] English:** was complicated and you couldn't do it yeah and i mean well after a while you could but you'd have  
**Translation:** 

**[4763.24s] English:** to work your way up because you know like putting the bright what's called the brights the  
**Translation:** 

**[4768.62s] English:** the trim on a car on a moving assembly line where it has to be attached 25 places in a minute and a  
**Translation:** 

**[4775.20s] English:** half is unbelievably complicated and and and human beings can do it's really good i think that's  
**Translation:** Vocabulary: unbelievably: 难以置信地

**[4782.86s] English:** harder than driving a car by the way putting together working working in a factory uh too  
**Translation:** 

**[4788.80s] English:** smart people can disagree yeah i think driving a car well we'll get you in the factory someday and  
**Translation:** 

**[4796.28s] English:** then we'll see how you do not for us humans driving a car i think it's a good idea to do it  
**Translation:** 

**[4798.62s] English:** a car is easy i'm saying  
**Translation:** 

**[4800.00s] English:** building a machine that drives a car is not easy no okay okay driving a car is easy for humans  
**Translation:** 

**[4807.34s] English:** because we've been evolving for billions of years drive cars yeah i noticed the pale with the cars  
**Translation:** 

**[4814.44s] English:** are super cool oh now you join the rest of the internet and mocking me okay i just yeah yeah  
**Translation:** 

**[4823.26s] English:** intrigued by your you know your anthropology yeah it's uh i have to go dig into that there's  
**Translation:** Vocabulary: anthropology: 人类学; intrigued: 好奇

**[4829.14s] English:** some inaccuracies there yes okay but in general what have you learned in terms of um thinking about  
**Translation:** 

**[4840.18s] English:** passion craftsmanship tension chaos you know the whole mess of it what have you learned  
**Translation:** Vocabulary: craftsmanship: 手工艺; inaccuracies: 不准确

**[4852.06s] English:** have taken away from your time working with elon musk working at tesla which is known to be a place  
**Translation:** 

**[4859.12s] English:** of chaos innovation craftsmanship and i really like the way he thought like you think you have  
**Translation:** 

**[4866.90s] English:** an understanding about what first principles of something is and then you talk to elon about it  
**Translation:** 

**[4871.50s] English:** and you you didn't scratch the surface you know he he has a deep belief that no matter what you  
**Translation:** 

**[4878.18s] English:** do is a local maximum right and i had a friend he invented a better electric motor and uh it  
**Translation:** 

**[4884.94s] English:** was like a lot better than what we were using and one day he came by he said you know i'm  
**Translation:** 

**[4889.12s] English:** a little disappointed because you know this is really great and you didn't seem that impressed  
**Translation:** 

**[4893.18s] English:** and i said you know when the super intelligent aliens come are they going to be looking for you  
**Translation:** 

**[4898.28s] English:** like where is he the guy who built the motor yeah probably not you know like like the like  
**Translation:** 

**[4906.04s] English:** but doing interesting work that's both innovative and let's say craftsman's work on the current  
**Translation:** 

**[4911.24s] English:** thing is really satisfying and it's good and and that's cool and then elon was good taking  
**Translation:** 

**[4919.12s] English:** like what's the deep  
**Translation:** 

**[4920.00s] English:** first principle oh no what's really no what's really you know you know you know that that  
**Translation:** 

**[4926.40s] English:** you know ability to look at it without assumptions and and how constraints is super wild  
**Translation:** Vocabulary: assumptions: 前提; constraints: 限制

**[4934.08s] English:** you know we build rocket ship and using that same car and you know everything and that's super fun  
**Translation:** 

**[4940.72s] English:** and he's into it too like when they first landed two spacex rockets to tesla we had a video  
**Translation:** 

**[4946.72s] English:** projector in the big room and like 500 people came down and when they landed everybody cheered  
**Translation:** 

**[4951.20s] English:** and some people cried it was so cool yeah all right but how did you do that well it was super  
**Translation:** Vocabulary: projector: 投影仪

**[4958.72s] English:** hard and then people say well it's chaotic really to get out of all your assumptions you think  
**Translation:** 

**[4964.80s] English:** that's not going to be unbelievably painful and is elon tough yeah probably the people look back on  
**Translation:** Vocabulary: unbelievably: 难以置信地

**[4976.72s] English:** that experience to go take apart that many layers of assumptions sometimes super fun sometimes  
**Translation:** 

**[4984.24s] English:** painful so it could be emotionally and intellectually painful that whole process  
**Translation:** Vocabulary: intellectually: 智力上

**[4988.64s] English:** is just stripping away assumptions yeah imagine 99 of your thought process is protecting your  
**Translation:** 

**[4994.24s] English:** self-conception and 98 of that's wrong yeah now you got the math right how do you think  
**Translation:** Vocabulary: stripping: 去除

**[5002.88s] English:** you're feeling when you get back into that one bit that's useful  
**Translation:** 

**[5006.72s] English:** and now you're open and you have the ability to do something different  
**Translation:** 

**[5012.40s] English:** i don't know if i got the math right it might be 99.9 but  
**Translation:** 

**[5016.24s] English:** it ain't 50. imagining it that 50 percent is hard enough yeah  
**Translation:** 

**[5024.08s] English:** now for a long time i've suspected you could get better like you can think better you can think  
**Translation:** 

**[5030.00s] English:** more clearly you can take things apart and there's lots of examples of that people who do that  
**Translation:** 

**[5036.72s] English:** so and elon is an example  
**Translation:** 

**[5040.00s] English:** of that apparently you are an example so i don't know if i am i'm fun to talk to  
**Translation:** 

**[5046.48s] English:** certainly i've learned a lot of stuff right well here's the other thing is like i joke like like  
**Translation:** 

**[5051.44s] English:** i read books and people think oh you read books well no i've read a couple books a week for 55  
**Translation:** 

**[5059.12s] English:** years wow well maybe 50 because i didn't read learn to read until i was eight or something  
**Translation:** 

**[5063.52s] English:** and uh and it turns out when people write books they often take 20 years of their life where they  
**Translation:** 

**[5071.52s] English:** passionately did something reduce it to 200 pages that's kind of fun and then go you go online and  
**Translation:** 

**[5079.04s] English:** you can find out who wrote the best books and who like you know that's kind of wild so there's this  
**Translation:** Vocabulary: passionately: 热情地

**[5083.92s] English:** wild selection process and then you can read it and for the most part understand it and then you  
**Translation:** 

**[5090.26s] English:** can go apply it like i went to one company i thought  
**Translation:** 

**[5093.52s] English:** i haven't managed much before so i read 20 management books and i started talking to  
**Translation:** 

**[5098.42s] English:** them and basically compared to all the vps running around i'd run night read 19 more management books  
**Translation:** 

**[5104.14s] English:** than anybody else it wasn't even that hard and half the stuff worked like first time it wasn't  
**Translation:** 

**[5111.42s] English:** even rocket science but at the core of that is questioning the assumptions or sort of entering  
**Translation:** Vocabulary: assumptions: 前提

**[5119.34s] English:** the thinking first person principles thinking sort of looking at the  
**Translation:** 

**[5123.52s] English:** reality of the situation and using using that knowledge applying that knowledge so yeah so i  
**Translation:** 

**[5129.36s] English:** would say my brain has this idea that you can question first assumptions and but i can go days  
**Translation:** 

**[5136.88s] English:** at a time and forget that and you have to kind of like circle back that observation because it is  
**Translation:** 

**[5143.36s] English:** because it's hard challenging well it's hard to just keep it front and center because you know  
**Translation:** 

**[5147.82s] English:** you're you operate on so many levels all the time and you know getting this done takes priority or  
**Translation:** 

**[5153.52s] English:** you know being happy takes priority or you know screwing around takes priority like  
**Translation:** 

**[5160.00s] English:** Like, how you go through life is complicated.  
**Translation:** Vocabulary: screwing: 胡闹

**[5162.64s] English:** Yeah.  
**Translation:** 

**[5162.96s] English:** And then you remember, oh, yeah, I could really think first principles.  
**Translation:** 

**[5166.50s] English:** Oh, shit, that's tiring, you know.  
**Translation:** 

**[5169.34s] English:** But you do for a while, and that's kind of cool.  
**Translation:** 

**[5172.32s] English:** So just as a last question in your sense, from the big picture, from the first principles, do you think, you kind of answered it already, but do you think autonomous driving is something we can solve on a timeline of years?  
**Translation:** 

**[5188.56s] English:** So one, two, three, five, ten years, as opposed to a century.  
**Translation:** 

**[5193.90s] English:** Yeah, definitely.  
**Translation:** 

**[5195.10s] English:** Just to linger on it a little longer, where's the confidence coming from?  
**Translation:** 

**[5200.08s] English:** Is it the fundamentals of the problem, the fundamentals of building the hardware and the software?  
**Translation:** 

**[5206.32s] English:** As a computational problem, understanding ballistics, roles, topography, it seems pretty solvable.  
**Translation:** Vocabulary: ballistics: 弹道学; computational: 计算的; fundamentals: 基础; solvable: 可解的; topography: 地形学

**[5216.10s] English:** I mean, and you can see this, you know, like.  
**Translation:** 

**[5218.56s] English:** Like speech recognition, for a long time, people were doing, you know, frequency and domain analysis and all kinds of stuff.  
**Translation:** 

**[5224.34s] English:** And that didn't work for, at all, right?  
**Translation:** 

**[5227.04s] English:** And then they did deep learning about it, and it worked great.  
**Translation:** 

**[5231.26s] English:** And it took multiple iterations.  
**Translation:** 

**[5234.44s] English:** And, you know, autonomous driving is way past the frequency analysis point.  
**Translation:** Vocabulary: autonomous: 自主; iterations: 迭代

**[5240.62s] English:** You know, use radar, don't run into things.  
**Translation:** 

**[5243.58s] English:** And the data gathering is going up, and the computation is going up, and the algorithm understanding is going up.  
**Translation:** Vocabulary: algorithm: 算法; computation: 计算

**[5248.60s] English:** And there's a whole bunch of problems getting solved like that.  
**Translation:** 

**[5251.64s] English:** The data side is really powerful, but I disagree with both you and Elon.  
**Translation:** 

**[5255.54s] English:** I'll tell Elon once again, as I did before, that when you add human beings into the picture, it's no longer a ballistics problem.  
**Translation:** 

**[5265.68s] English:** It's something more complicated.  
**Translation:** 

**[5267.52s] English:** But I could be very well proven wrong.  
**Translation:** 

**[5270.20s] English:** Yeah, cars are highly damped in terms of rate of change.  
**Translation:** 

**[5273.92s] English:** Like the steering system is really slow compared to a computer.  
**Translation:** 

**[5277.70s] English:** The accelerators.  
**Translation:** Vocabulary: accelerators: 加速器; steering: 转向系统

**[5278.56s] English:** The acceleration is really slow.  
**Translation:** 

**[5280.00s] English:** yeah on a certain time scale on a ballistics time scale but human behavior i don't know  
**Translation:** Vocabulary: acceleration: 加速度

**[5285.56s] English:** it yeah i shouldn't say beings are really slow too we weirdly we operate you know half a second  
**Translation:** 

**[5291.92s] English:** behind reality i'll be really understands that one either it's pretty funny yeah yeah so  
**Translation:** 

**[5298.80s] English:** yeah we'll be very well could be surprised and i think with the rate of improvement on all aspects  
**Translation:** 

**[5305.92s] English:** on both the compute and the the software and the hardware there's going to be pleasant surprises  
**Translation:** 

**[5311.00s] English:** all over the place speaking of unpleasant surprises many people have worries about  
**Translation:** 

**[5318.18s] English:** a singularity in the development of ai forgive me for such questions yeah when ai improves  
**Translation:** 

**[5325.26s] English:** exponential and reaches a point of superhuman level general intelligence you know beyond the  
**Translation:** 

**[5331.74s] English:** point there's no looking back do you share this worry of existential threats  
**Translation:** Vocabulary: exponential: 指数的

**[5335.92s] English:** from artificial intelligence from computers becoming superhuman level intelligent no not  
**Translation:** 

**[5342.30s] English:** really you know like we already have a very stratified society and then if you look at  
**Translation:** Vocabulary: stratified: 阶层分明的

**[5348.32s] English:** the whole animal kingdom of capabilities and abilities and interests and you know smart  
**Translation:** 

**[5354.22s] English:** people have their niche and you know normal people have their niche and craftsmen's have their niche  
**Translation:** Vocabulary: niche: 专长领域

**[5359.58s] English:** and you know animals have their niche i suspect that the domains of interest  
**Translation:** 

**[5365.90s] English:** for things that you know astronomically different like the whole something got 10 times smarter than  
**Translation:** Vocabulary: astronomically: 极其

**[5372.08s] English:** us and wanted to track us all down because what we like to have coffee at starbucks like it doesn't  
**Translation:** 

**[5377.92s] English:** seem plausible no is there an existential problem that how do you live in a world where there's  
**Translation:** Vocabulary: existential: 存在主义; plausible: 合情合理

**[5382.82s] English:** something way smarter than you and you you based your kind of self-esteem on being the smartest  
**Translation:** 

**[5388.06s] English:** local person well there's what point one percent of the population who thinks that because the rest  
**Translation:** 

**[5393.10s] English:** of the population has been dealing with it since they were born  
**Translation:** 

**[5395.90s] English:** so the the the breadth of possible  
**Translation:** 

**[5400.00s] English:** experience that can be interesting is really big and you know super intelligence seems likely  
**Translation:** 

**[5410.32s] English:** although we still don't know if we're magical but i suspect we're not and it seems likely that  
**Translation:** 

**[5417.52s] English:** it'll create possibilities that are interesting for us and it's its interests will be interesting  
**Translation:** 

**[5423.68s] English:** for that for whatever it is it's not obvious why its interests would somehow want to fight over  
**Translation:** 

**[5430.92s] English:** some square foot of dirt or you know whatever you know the usual fears are about so you don't think  
**Translation:** 

**[5438.22s] English:** you'll inherit some of the darker aspects of human nature depends on how you think reality  
**Translation:** 

**[5443.82s] English:** is constructed so for for whatever reason human beings are in let's say creative tension and  
**Translation:** 

**[5451.56s] English:** opposition with both our good and  
**Translation:** 

**[5453.68s] English:** bad forces like there's lots of philosophical understanding of that  
**Translation:** 

**[5457.88s] English:** right i don't know why that would be different so you think the evil is is necessary for the good  
**Translation:** Vocabulary: philosophical: 哲学的

**[5465.70s] English:** i mean the tension i don't know about evil but like we live in a competitive world where  
**Translation:** 

**[5471.86s] English:** your good is somebody else's right you know evil you know there's there's the malignant part of it  
**Translation:** 

**[5479.22s] English:** but that seems to be self-limiting although occasionally  
**Translation:** 

**[5483.46s] English:** it's not so much of a malignant part of it but it's a self-limiting part of it  
**Translation:** Vocabulary: malignant: 恶性

**[5483.66s] English:** although occasionally it's not so much of a malignant part of it but it's a self-limiting part of it  
**Translation:** 

**[5483.68s] English:** it's it's super horrible but yes there's a debate over ideas and some people have different  
**Translation:** 

**[5491.52s] English:** beliefs and that that debate itself is a process so the at arriving at something yeah and why  
**Translation:** 

**[5498.08s] English:** wouldn't that continue yeah yeah just you but you don't think that whole process will leave humans  
**Translation:** 

**[5503.82s] English:** behind in a way that's painful emotionally painful yes for the one for the 0.1 percent  
**Translation:** 

**[5510.32s] English:** they'll be you know why isn't it already painful for a large percentage of the population  
**Translation:** 

**[5513.66s] English:** and it is i mean society does have a lot of stress in it about the one percent and about to this and  
**Translation:** 

**[5520.00s] English:** about that but you know everybody has a lot of stress in their life about what they find  
**Translation:** 

**[5524.48s] English:** satisfying and and you know know yourself seems to be the proper dictum and pursue something that  
**Translation:** 

**[5532.24s] English:** makes your life meaningful seems proper and there's so many avenues on that like there's so  
**Translation:** Vocabulary: dictum: 格言

**[5539.80s] English:** much unexplored space at every single level you know i'm somewhat of my nephew called me a jaded  
**Translation:** 

**[5548.50s] English:** optimist and you know so it's there's a beautiful tension that uh in that label but if you were to  
**Translation:** Vocabulary: optimist: 乐观主义者; unexplored: 未探索

**[5559.08s] English:** look back at your life and uh could relive a moment a set of moments because there were the  
**Translation:** 

**[5566.66s] English:** happiest times of your life outside of family what would that be  
**Translation:** Vocabulary: relive: 重温

**[5572.36s] English:** i don't want to relive any moments i like that  
**Translation:** 

**[5577.34s] English:** i like that  
**Translation:** 

**[5578.50s] English:** situation where you have some amount of optimism and then the the anxiety of the unknown  
**Translation:** 

**[5584.50s] English:** so you love the unknown the the mystery of it i don't know about the mystery it sure gets your  
**Translation:** Vocabulary: optimism: 乐观

**[5591.94s] English:** blood pumping what do you think is the meaning of this whole thing  
**Translation:** 

**[5595.76s] English:** of life on this pale blue dot it seems to be what it does like the universe for whatever reason  
**Translation:** 

**[5608.50s] English:** makes atoms which makes us which we do stuff and we figure out things and we explore things and  
**Translation:** 

**[5617.16s] English:** that's just what it is it's not just yeah it is yeah jim i don't think there's a better place to  
**Translation:** 

**[5626.34s] English:** end it it's a huge honor and uh well that's super fun thank you so much for talking today all right  
**Translation:** 

**[5632.70s] English:** great thanks for listening to this conversation and thank you to our presenting sponsor cash  
**Translation:** 

**[5638.50s] English:** app download it  
**Translation:** 

**[5640.00s] English:** Use code LEXPODCAST, you'll get $10 and $10 will go to FIRST, a STEM education nonprofit that  
**Translation:** Vocabulary: nonprofit: 非营利组织

**[5646.58s] English:** inspires hundreds of thousands of young minds to become future leaders and innovators. If you  
**Translation:** 

**[5652.42s] English:** enjoy this podcast, subscribe on YouTube, give it five stars on Apple Podcasts, follow on Spotify,  
**Translation:** Vocabulary: innovators: 创新者; inspires: 启发; subscribe: 订阅

**[5658.32s] English:** support it on Patreon, or simply connect with me on Twitter. And now, let me leave you with  
**Translation:** 

**[5663.84s] English:** some words of wisdom from Gordon Moore. If everything you try works, you aren't trying  
**Translation:** 

**[5669.86s] English:** hard enough. Thank you for listening and hope to see you next time.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
