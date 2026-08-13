# Podcast vocabulary notes
Source file: Lex Fridman - David Patterson： Computer Architecture and Data Storage ｜ Lex Fridman Podcast #104.opus
Improved subtitle: punctuation and vocabulary regenerated from current config.

**[0.00s] English:** The following is a conversation with David Patterson, Turing Award winner and professor.  
**Translation:** 

**[5.36s] English:** Of computer science at Berkeley, he is known for pioneering contributions to risk processors.  
**Translation:** 

**[10.76s] English:** Architecture used by 99% of new chips today, and for co-creating RAID storage. The impact that  
**Translation:** 

**[18.88s] English:** These two lines of research and development have had on our world is immeasurable. He's also one  
**Translation:** Vocabulary: immeasurable: 无法衡量的

**[25.00s] English:** Of the great educators of computer science in the world, his book with John Hennessy is how I  
**Translation:** 

**[29.98s] English:** First, I learned about and was humbled by the inner workings of machines at the lowest level. Quick  
**Translation:** Vocabulary: educators: 教育家; humbled: 谦卑; workings: 工作机制

**[36.20s] English:** Summary of the ads: Two sponsors, The Jordan Harbinger Show and Cash App. Please consider.  
**Translation:** 

**[42.52s] English:** Supporting the podcast by going to jordanharbinger.com/lex and downloading Cash App.  
**Translation:** Vocabulary: jordanharbinger: 乔恩·哈伯辛格; sponsors: 赞助商

**[48.48s] English:** And using the code "lexpodcast," click on the links and buy the stuff. It's the best way to support the  
**Translation:** 

**[54.98s] English:** Podcast, and in general, the journey I'm on in my research and startup. This is the artificial  
**Translation:** Vocabulary: lexpodcast: 优惠码

**[60.44s] English:** Intelligence Podcast. If you enjoy it, subscribe on YouTube, and review it with five stars on Apple.  
**Translation:** 

**[65.28s] English:** Podcasts? Support it on Patreon, or connect with me on Twitter at Lex Friedman (spelled without the "e").  
**Translation:** Vocabulary: patreon: 赞助; subscribe: 订阅

**[71.68s] English:** E, just F-R-I-D-M-A-N. As usual, I'll do a few minutes of ads now—and never any ads in the middle.  
**Translation:** 

**[78.66s] English:** That can break the flow of the conversation. This episode is supported by the Jordan Harbinger Show.  
**Translation:** Vocabulary: harbinger: 预兆

**[84.98s] English:** Go to jordanharbinger.com/slash-lex. It's how he knows I sent you. On that page, there are links to  
**Translation:** 

**[91.02s] English:** Subscribe to it on Apple Podcasts, Spotify, and everywhere else. I've been binge-watching this podcast.  
**Translation:** 

**[96.68s] English:** It's amazing. Jordan is a great human being. He gets the best out of his guests and dives deep.  
**Translation:** 

**[101.78s] English:** Calls them out when it's needed, and makes the whole thing fun to listen to. He's interviewed  
**Translation:** 

**[106.02s] English:** Kobe Bryant, Mark Cuban, Neil deGrasse Tyson, Garry Kasparov, and many more. I recently listened.  
**Translation:** 

**[112.58s] English:** To his conversation with Frank Abagnale, he's a great guy. He's a great guy. He's a great guy. He's a great guy.  
**Translation:** Vocabulary: abagnale: 弗兰克·阿巴格内; bryant: 科比·布莱恩特; cuban: 马克·库班; garry: 加里·卡斯帕罗夫; kasparov: 加里·卡斯帕罗夫; tyson: 尼尔·德格拉斯·泰森

**[114.98s] English:** Author of "Catch Me If You Can" and one of the world's most famous con men.  
**Translation:** 

**[120.00s] English:** Perfect podcast length and topic for a recent long-distance run that I did.  
**Translation:** 

**[125.92s] English:** Again, go to jordanharbinger.com/slash/Lex to give him a shoutout and to support this podcast.  
**Translation:** 

**[133.40s] English:** Subscribe also on Apple Podcasts, Spotify, and everywhere else.  
**Translation:** Vocabulary: jordanharbinger: 乔丹·哈布金; shoutout: 点赞支持

**[137.86s] English:** This show is presented by Cash App, the greatest sponsor of this podcast ever, and the number-one finance app in the App Store.  
**Translation:** 

**[146.22s] English:** When you get it, use code Lex Podcast.  
**Translation:** Vocabulary: sponsor: 赞助商

**[148.58s] English:** Cash App lets you send money to friends, buy Bitcoin, and invest in the stock market with as little as $1.  
**Translation:** 

**[154.94s] English:** Since Cash App allows you to buy Bitcoin, let me mention that cryptocurrency in the context of the history of money is fascinating.  
**Translation:** Vocabulary: cryptocurrency: 加密货币

**[161.96s] English:** I recommend "Ascent of Money" as a great book on this history.  
**Translation:** 

**[165.34s] English:** Also, the audiobook is amazing.  
**Translation:** Vocabulary: ascent: 上升; audiobook: 有声书

**[167.74s] English:** Debits and credits on ledgers started around 30,000 years ago.  
**Translation:** 

**[171.46s] English:** The U.S. dollar, created over 200 years ago.  
**Translation:** Vocabulary: debits: 借方; ledgers: 账簿

**[174.14s] English:** And the first decentralized cryptocurrency was released just over 10 years ago.  
**Translation:** 

**[177.70s] English:** So, given that history, cryptocurrency is still very much in its early days of development.  
**Translation:** Vocabulary: decentralized: 去中心化的

**[182.96s] English:** But it's still aiming to, and just might redefine the nature of money.  
**Translation:** 

**[187.94s] English:** So, again, if you get Cash App from the App Store or Google Play and use the code LexPodcast, you get $10.  
**Translation:** Vocabulary: aiming: 瞄准; redefine: 重新定义

**[194.96s] English:** And Cash App will also donate $10 to FIRST, an organization that is helping to advance robotics and STEM education for young people around the world.  
**Translation:** 

**[203.10s] English:** And now, here's my conversation with David Patterson.  
**Translation:** Vocabulary: donate: 捐赠; robotics: 机器人技术

**[208.68s] English:** Let's start with the big historical question.  
**Translation:** 

**[211.70s] English:** How have computers changed in the past 50 years, both at the fundamental architectural level and in general, in your eyes?  
**Translation:** Vocabulary: architectural: 架构的

**[219.12s] English:** Well, the biggest thing that happened was the invention of the microprocessor.  
**Translation:** 

**[223.14s] English:** So, computers that used to fill up several rooms could now fit inside your cellphone.  
**Translation:** Vocabulary: microprocessor: 微处理器

**[229.82s] English:** And not only did they get smaller, they got a lot faster.  
**Translation:** 

**[234.82s] English:** So, they're a million times faster than they were.  
**Translation:** 

**[237.70s] English:** 50 Years Ago.  
**Translation:** 

**[239.70s] English:** And they're.  
**Translation:** 

**[240.00s] English:** Much cheaper, and they're ubiquitous. Uh, you know, I don't think there are 7.8 billion people on this planet.  
**Translation:** 

**[246.98s] English:** Probably half of them have cell phones right now; it's just remarkable that there's probably more.  
**Translation:** Vocabulary: ubiquitous: 无处不在的

**[253.08s] English:** Microprocessors than there are people; sure, I don't know what the ratio is, but I'm sure it's above one.  
**Translation:** 

**[258.22s] English:** Uh, maybe it's 10 to 1 or some number like that. What is a microprocessor, so a way to say what?  
**Translation:** 

**[266.64s] English:** A microprocessor is to tell you what's inside a computer, so a computer, classically, has had:  
**Translation:** 

**[272.34s] English:** Five pieces: there's input and output, which kind of naturally, as you'd expect, is input is like  
**Translation:** 

**[279.04s] English:** Speech or typing, and output is displayed. Um, there's a memory, and like the name sounds, it remembers.  
**Translation:** 

**[289.40s] English:** Things, so it's integrated circuits whose job is to take information in, and when you ask for it,...  
**Translation:** Vocabulary: circuits: 电路; integrated: 集成的

**[295.18s] English:** Comes back out, that's memory.  
**Translation:** 

**[296.46s] English:** And the third part is the processor, uh, where the team microprocessor comes from, and that has two.  
**Translation:** Vocabulary: processor: 处理器

**[302.58s] English:** Pieces as well, and that is the control, which is kind of the brain of the processor, and the um.  
**Translation:** 

**[311.62s] English:** The "arithmetic unit" is kind of the brawn of the computer. So, if you think of the  
**Translation:** Vocabulary: arithmetic: 计算单元; brawn: 计算能力

**[316.34s] English:** As a human body, the arithmetic unit—the thing that does the number crunching—is the brain.  
**Translation:** 

**[322.04s] English:** The control is the brain, so those five pieces: input, output, memory.  
**Translation:** Vocabulary: crunching: 计算

**[325.70s] English:** You.  
**Translation:** 

**[326.46s] English:** Uh, the arithmetic unit and control have been in computers since the very dawn, and the last two are  
**Translation:** 

**[334.72s] English:** Considered the processor, so a microprocessor simply means a processor that fits on a microchip.  
**Translation:** 

**[340.42s] English:** And that was invented about 40 years ago, uh, it was the first microprocessor. It's interesting.  
**Translation:** Vocabulary: microchip: 微芯片; microprocessor: 微处理器

**[346.86s] English:** That you refer to the arithmetic unit as though it were connected to the body and the controllers.  
**Translation:** 

**[352.98s] English:** Of the brain, so I guess I never thought of it that way. I think it's kind of like a computer.  
**Translation:** 

**[356.46s] English:** The nice way to think of it is that most of the actions the microprocessor performs involve...  
**Translation:** 

**[360.00s] English:** Does it in terms of literally sort of computation, but the microprocessor does the computation.  
**Translation:** Vocabulary: computation: 计算

**[367.58s] English:** Processes information, and most of the things it does are basic arithmetic operations. What?  
**Translation:** 

**[374.88s] English:** Are the operations, by the way, it's a lot like a calculator, you know? So there are, um, add instructions.  
**Translation:** Vocabulary: calculator: 计算器

**[380.94s] English:** Subtract, instructions, multiply, and divide, and uh-kind of the brilliance of the invention of the,  
**Translation:** 

**[389.20s] English:** The microprocessor of the computer or the processor is that it performs very trivial operations, but it  
**Translation:** Vocabulary: brilliance: 巧妙之处; multiply: 乘法; processor: 处理器; subtract: 减法; trivial: 简单操作

**[396.32s] English:** Just performs billions of them per second, and what we're capable of doing is writing software.  
**Translation:** 

**[402.54s] English:** That can take these very trivial instructions and have them create tasks that can do things.  
**Translation:** 

**[408.00s] English:** Better than what human beings can do today, just looking back through your career, did you anticipate the  
**Translation:** 

**[413.74s] English:** Kind of how good we would be able to get at doing these small, basic operations.  
**Translation:** Vocabulary: anticipate: 预见

**[419.20s] English:** Like, what, like, how many surprises along the way? Where you just kind of sat back.  
**Translation:** 

**[424.26s] English:** And said, "Wow, that I didn't expect it to go this fast and this good. Well, the fundamental driving...  
**Translation:** 

**[431.80s] English:** Force is, uh, what's called Moore's Law, which was named after Gordon Moore, who's a Berkeley alumnus.  
**Translation:** 

**[438.54s] English:** Alumnus, and he made this observation very early in what are called semiconductors, and semiconductors.  
**Translation:** Vocabulary: alumnus: 校友; berkeley: 伯克利; semiconductors: 半导体

**[445.24s] English:** Are these ideas? You can build these very simple switches.  
**Translation:** 

**[449.20s] English:** And you can put them on these microchips, and he made this observation over 50 years ago; he looked  
**Translation:** Vocabulary: microchips: 集成电路

**[454.64s] English:** At a few years and said, "I think what's going to happen is the number of these little switches...  
**Translation:** 

**[458.88s] English:** Called Moore's Law, is going to double every year for the next decade, and he said this in 1965.  
**Translation:** 

**[466.24s] English:** In 1975, he said, "Well, maybe it's going to double every two years," and that what others have since noted.  
**Translation:** 

**[474.00s] English:** Named after Moore's Law, which guided the industry, and when Gordon Moore made that prediction.  
**Translation:** 

**[479.20s] English:** He he.  
**Translation:** 

**[480.00s] English:** Wrote a paper back in, I think in the 1970s, and said, not only was this going to...  
**Translation:** 

**[488.12s] English:** Happened, he wrote, "What would be the implications of that?" And in this article from 1965, he,  
**Translation:** 

**[493.66s] English:** He shows ideas like computers being in cars, and computers being in something that you would buy.  
**Translation:** Vocabulary: implications: 含义

**[501.62s] English:** In the grocery store and stuff like that. So he kind of not only called his shot.  
**Translation:** 

**[506.02s] English:** He called the implications of it. So, if you were in the computing field, and if you believed,...  
**Translation:** Vocabulary: computing: 计算机; grocery: 杂货

**[511.90s] English:** Moore's prediction, he kind of said what would be happening in the future. So, it's not  
**Translation:** 

**[518.18s] English:** Kind of, it's in one sense what was predicted, and you could imagine it was easy.  
**Translation:** 

**[525.32s] English:** To believe that Moore's Law was going to continue, and so these would be the implications. On the  
**Translation:** 

**[530.08s] English:** On the other side, there are these kinds of shocking events in your life. Like I remember driving,  
**Translation:** 

**[536.02s] English:** Driving in Marin across the Bay in San Francisco, and seeing a bulletin board at a local  
**Translation:** 

**[541.92s] English:** Civic Center, and it had a URL on it. And it was like, for all, for all, for the people at the time.  
**Translation:** Vocabulary: civic: 市民的; marin: 马林县

**[549.56s] English:** These first URLs, and that's the, you know, WWW-select stuff with the HTTP, people thought it was  
**Translation:** 

**[555.76s] English:** Look, it looks like alien writing, right? You'd see these advertisements and commercials.  
**Translation:** Vocabulary: alien: 外星的; commercials: 广告

**[563.50s] English:** Or on bulletin boards that had this alien writing on them. So, for the latest,  
**Translation:** 

**[566.02s] English:** People were like, "What the hell is going on here?" And for those in the industry, it was, "Oh my.  
**Translation:** 

**[570.38s] English:** God, this stuff is getting so popular. It's actually leaking out of our nerdy world and into the mainstream.  
**Translation:** 

**[576.84s] English:** The real world. So, that I mean, there were events like that. I think another one was that I remember.  
**Translation:** Vocabulary: leaking: 渗透; mainstream: 主流; nerdy: 极客的

**[581.50s] English:** With the, in the early days of the personal computer, when we started seeing advertisements,  
**Translation:** 

**[585.46s] English:** In magazines for personal computers, it's so popular that it's made the newspapers. So,  
**Translation:** 

**[591.22s] English:** At one hand, you know, Gordon Moore predicted it, and you kind of expected it to happen, but,  
**Translation:** 

**[596.02s] English:** When it really hit and you saw it affecting society, it was, it was,  
**Translation:** 

**[600.00s] English:** Shocking, so maybe, uh, taking a step back and looking both at engineering and philosophical perspectives.  
**Translation:** 

**[607.24s] English:** Perspective: What do you see as the layers of abstraction in a computer?  
**Translation:** Vocabulary: abstraction: 抽象; perspectives: 视角; philosophical: 哲学的

**[613.32s] English:** As a set of layers of abstractions, I think that's one of the things that computer science is all about.  
**Translation:** 

**[619.74s] English:** Um, fundamentals is that these things are really complicated in the way we cope with.  
**Translation:** Vocabulary: abstractions: 抽象; fundamentals: 基础

**[625.52s] English:** Complicated software and complicated hardware are these layers of abstraction, and that simply means  
**Translation:** 

**[631.14s] English:** That we suspend disbelief and pretend, that the only thing you know is that layer.  
**Translation:** Vocabulary: disbelief: 不信; suspend: 搁置

**[639.90s] English:** You don't know anything about the layer below it, and that's the way we can make things very complicated.  
**Translation:** 

**[644.14s] English:** Things, and uh, probably it started with hardware—that's the way it was done—but it's been proven.  
**Translation:** 

**[651.18s] English:** Extremely useful, and you know, I would say in a modern computer today.  
**Translation:** 

**[655.52s] English:** There might be 10 or 20 layers of abstraction, and they're all trying to kind of enforce this.  
**Translation:** Vocabulary: enforce: 强制实施

**[660.90s] English:** Contract: Is all you know is this interface. There's a set of commands that you can be allowed to.  
**Translation:** 

**[669.54s] English:** Use and you stick to those commands, and we will faithfully execute that. It's like peeling the  
**Translation:** Vocabulary: execute: 执行; faithfully: 忠诚地; interface: 接口

**[674.12s] English:** Layers of a London, like an onion, you get down there's a new set of layers, and so forth, so for.  
**Translation:** 

**[679.70s] English:** Uh, people who want to study computer science—the exciting part about it,  
**Translation:** 

**[685.52s] English:** Is there a way to keep peeling back those layers? You know, you take your first course, and you might learn to  
**Translation:** 

**[690.88s] English:** Program in Python, and then you can take a follow-on course and get it down to.  
**Translation:** Vocabulary: peeling: 剥开

**[695.84s] English:** A lower-level language like C, and you know, you can go and then you can; if you want to, you can.  
**Translation:** 

**[700.80s] English:** Start getting into the hardware layers, and you keep going down all the way to that.  
**Translation:** 

**[705.52s] English:** Transistor that I talked about, that Gordon Moore predicted, and you can understand all.  
**Translation:** 

**[710.96s] English:** Those layers, all the way up to the highest-level application software, so it's uh  
**Translation:** Vocabulary: transistor: 晶体管

**[715.52s] English:** It's a very kind of magnetic field.  
**Translation:** 

**[720.00s] English:** If you're interested, you can go into any depth and keep going, in particular, what's happening.  
**Translation:** 

**[726.30s] English:** Right now, or it's happened in software over the last 20 years, and recently in hardware, there's been getting  
**Translation:** 

**[731.52s] English:** To be open-source versions of all of these things, so what open source means is what the engineer  
**Translation:** 

**[738.00s] English:** The programmer designs it's not a secret; uh, it belongs to a company and it's out there on the  
**Translation:** 

**[745.44s] English:** World Wide Web, so you can see it, so you can look at a lot of pieces of software that you use.  
**Translation:** 

**[752.84s] English:** You can see exactly what the programmer does if you want to get involved; that used to stop at the  
**Translation:** 

**[758.90s] English:** Hardware recently has been an effort to make open-source hardware and those interfaces open.  
**Translation:** Vocabulary: interfaces: 接口; programmer: 程序员

**[766.04s] English:** So, you can see that, instead of having to stop at the hardware store, you can now start going directly.  
**Translation:** 

**[770.32s] English:** Layer by layer, below that, and see what's inside. There's something remarkably interesting there.  
**Translation:** Vocabulary: remarkably: 非常

**[775.22s] English:** It's a remarkable thing to see, and it's truly a remarkable thing to see.  
**Translation:** 

**[775.42s] English:** Time is a great opportunity for the interested individual to see, in great depth, what's really going on.  
**Translation:** 

**[781.60s] English:** Computers that power everything we see around us — are you thinking of them too, when you say...  
**Translation:** 

**[787.18s] English:** Open-source at the hardware level is this going to the design, architecture, and instruction-set level?  
**Translation:** 

**[793.76s] English:** Or is it going to literally, you know, be the manufacturer of the actual hardware?  
**Translation:** 

**[803.42s] English:** Actual chips, whether that's ASICS specialized for a particular domain or the general-purpose kind, so let's  
**Translation:** Vocabulary: manufacturer: 制造商

**[808.78s] English:** Talk about that a little bit, so when you get down to the bottom layer of software, the way  
**Translation:** 

**[816.08s] English:** Software talks to hardware is in a vocabulary, and what we call that vocabulary, we call it.  
**Translation:** 

**[823.44s] English:** The words of that vocabulary are called "instructions," and the technical term for the vocabulary is...  
**Translation:** 

**[830.26s] English:** Instruction set, so those instructions are likely  
**Translation:** 

**[833.42s] English:** About earlier, there can be instructions like add, subtract, and multiply, divide; there's instructions.  
**Translation:** 

**[838.68s] English:** To put,  
**Translation:** Vocabulary: multiply: 乘法; subtract: 减法

**[840.00s] English:** Data into memory, which is called a store instruction, and to get data back, which is  
**Translation:** 

**[844.62s] English:** Called a load, instructions. And those simple instructions go back to the very dawn of  
**Translation:** 

**[849.74s] English:** Computing. And in 1950, the commercial computer had these instructions. So that's the instruction.  
**Translation:** 

**[855.64s] English:** So, up until I'd say 10 years ago, these instruction sets were  
**Translation:** Vocabulary: computing: 计算

**[861.80s] English:** All proprietary. So, a very popular one is owned by Intel—the one that's in the cloud and in all.  
**Translation:** 

**[869.12s] English:** The PCs in the world. Intel owns that instruction set, which is referred to as x86. There have been  
**Translation:** Vocabulary: proprietary: 专有技术

**[875.80s] English:** A sequence of ones, where the first number was called 8086. And since then, there has been a lot.  
**Translation:** 

**[881.16s] English:** Of numbers, but they all end in 86. So, there's been that kind of family of instruction sets.  
**Translation:** 

**[888.12s] English:** And that's proprietary.  
**Translation:** 

**[889.40s] English:** And that's proprietary. The other one that's very popular is from ARM. That kind of powers:  
**Translation:** 

**[895.62s] English:** All the cell phones in the world, all the iPads in the world.  
**Translation:** 

**[899.12s] English:** And a lot of things that are so-called Internet of Things devices, ARM, and that one is also.  
**Translation:** 

**[907.04s] English:** Proprietary. ARM will license it to people for a fee, but they own that. So the new idea that...  
**Translation:** 

**[913.48s] English:** Got started at Berkeley kind of unintentionally 10 years ago, early in my career, we pioneered.  
**Translation:** Vocabulary: berkeley: 伯克利; pioneered: 开创; unintentionally: 无意中

**[921.96s] English:** A way to do these vocabulary instruction sets that was very controversial at the time.  
**Translation:** 

**[927.80s] English:** At the time, in the 19th century, we had a lot of people who were very, very, very, very, very,  
**Translation:** 

**[929.12s] English:** In the 1980s, conventional wisdom was that these vocabulary and instruction sets should have  
**Translation:** 

**[934.34s] English:** Powerful instructions. So, polysyllabic kinds of words, you can think of that.  
**Translation:** Vocabulary: conventional: 传统的; polysyllabic: 多音节的

**[940.62s] English:** And so instead of just adding, subtracting, and multiplying, they would have polynomial division or  
**Translation:** 

**[946.18s] English:** Sort a list. And the hope was that these powerful vocabularies would make it easier for software.  
**Translation:** Vocabulary: multiplying: 乘法; polynomial: 多项式; subtracting: 减法

**[954.48s] English:** So, we thought that didn't make sense for microprocessors. There were people  
**Translation:** 

**[958.36s] English:** At Berkeley, who were very, very, very, very, very, very, very, very, very, very, very, very, very,  
**Translation:** Vocabulary: microprocessors: 微处理器

**[959.12s] English:** very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very  
**Translation:** 

**[960.00s] English:** IBM, who argued the opposite. And what we called that was a Reduced Instruction Set Computer (RISC). And  
**Translation:** 

**[966.52s] English:** The abbreviation was RISC. And, typical for computer people, we use the abbreviation and  
**Translation:** 

**[972.48s] English:** Start pronouncing it. So RISC was the thing. So we said, for microprocessors, which with Gordon's  
**Translation:** Vocabulary: abbreviation: 缩写

**[978.00s] English:** Moore is changing really fast. We think it's better to have a pretty simple set of instructions.  
**Translation:** 

**[984.86s] English:** Reduced set of instructions: that would be a better way to build microprocessors since  
**Translation:** 

**[989.78s] English:** They're going to be changing so fast due to Moore's Law, and then we'll just use standard.  
**Translation:** 

**[994.22s] English:** Software to generate more of those simple instructions. And one of the pieces of  
**Translation:** 

**[1002.80s] English:** Software that's in that software stack, going between these layers of abstraction, is called  
**Translation:** 

**[1007.40s] English:** A compiler. And it basically translates: it's a translator between levels. We said the translator.  
**Translation:** Vocabulary: abstraction: 抽象层; translates: 翻译; translator: 翻译器

**[1012.20s] English:** Will handle that. So, the technical question was: Well, since there are these reduced instructions,  
**Translation:** 

**[1019.22s] English:** You have to.  
**Translation:** 

**[1019.60s] English:** Execute more of them, yeah, that's right. But maybe you execute them faster, yeah, that's right.  
**Translation:** 

**[1024.74s] English:** They're simpler, so they go faster, but you have to do more of them. So, what's that trade-off like?  
**Translation:** Vocabulary: execute: 执行

**[1029.54s] English:** Like? And it ended up that we ended up executing maybe 50% more instructions, and maybe a third more.  
**Translation:** 

**[1037.08s] English:** Instructions, but they ran four times faster. So these RISC, controversial RISC ideas proved to be  
**Translation:** 

**[1044.48s] English:** Maybe factors of three or four better. I love that this idea was controversial.  
**Translation:** 

**[1049.60s] English:** And almost kind of like rebellious. So, that's in the context of what was more.  
**Translation:** Vocabulary: rebellious: 叛逆的

**[1055.08s] English:** Conventional is the complex instructional set computing. So, how would you pronounce that?  
**Translation:** 

**[1061.46s] English:** CISC.  
**Translation:** Vocabulary: computing: 计算机; conventional: 传统的; instructional: 教学的

**[1061.78s] English:** CISC, which is RISC.  
**Translation:** 

**[1063.02s] English:** RISC versus CISC. And believe it or not, this sounds very, very boring, right?  
**Translation:** 

**[1070.32s] English:** It was violently debated at several conferences. It's like, "What's the right way to go?" And people,...  
**Translation:** 

**[1077.44s] English:** Thought RISC was, you know, was....  
**Translation:** Vocabulary: conferences: 会议; violently: 激烈地

**[1079.60s] English:** A deal.  
**Translation:** 

**[1080.00s] English:** Evolution. We're going to make software worse by making those instructions simpler. And there are  
**Translation:** 

**[1085.12s] English:** Fierce debates at several conferences in the 1980s. And then, later in the 1980s, it kind of...  
**Translation:** 

**[1091.58s] English:** Settled on these benefits. It's not completely intuitive to me why risk has, for the most part,  
**Translation:** Vocabulary: fierce: 猛烈的; intuitive: 直观的

**[1098.22s] English:** Won. Yeah. So, why did that happen? Yeah, yeah. And maybe I can sort of say a bunch of dumb things.  
**Translation:** 

**[1104.30s] English:** That could lay the groundwork for further commentary. So, to me, this is kind of an interesting thing. If  
**Translation:** Vocabulary: groundwork: 基础

**[1110.86s] English:** You look at C++ versus C, with modern compilers, you could really write faster code with C++.  
**Translation:** 

**[1118.74s] English:** So, relying on the compiler to reduce your complicated code into something simple and fast.  
**Translation:** Vocabulary: compilers: 编译器

**[1124.94s] English:** So, to me, comparing risks: maybe this is a dumb question, but why is it that focusing on them seems to be so important?  
**Translation:** 

**[1133.46s] English:** What is the importance of a definition that does not have a risk factor?  
**Translation:** 

**[1134.30s] English:** The design of the instruction set, with only a few simple instructions, ultimately provides  
**Translation:** 

**[1140.78s] English:** Faster execution versus coming up with, as you said, a ton of complicated instructions.  
**Translation:** Vocabulary: execution: 执行速度

**[1149.42s] English:** That, over time — you know, years, maybe decades — you come up with compilers that can reduce those.  
**Translation:** 

**[1156.22s] English:** Into simple instructions for you. Yeah. So, let's try and split that into two pieces.  
**Translation:** 

**[1161.60s] English:** So, if the compiler can do that for you, if the compiler can take, you know, a complicated program,...  
**Translation:** 

**[1169.16s] English:** And produce simpler instructions, then the programmer doesn't care, right? Programmer,  
**Translation:** Vocabulary: programmer: 编程人员

**[1176.48s] English:** I don't care just how fast the computer I'm using is; how much does it cost? And so what happened?  
**Translation:** 

**[1183.78s] English:** Kind of in the software industry, critical pieces of software were right around before the 1980s.  
**Translation:** 

**[1190.44s] English:** Still written by the computer, and so the computer was able to do that. And so the computer was able  
**Translation:** 

**[1191.60s] English:** To do that, and so the computer was able to do that. And so the computer was able to do that.  
**Translation:** 

**[1191.66s] English:** Not in languages like C or C++, they were written in what's called assembly language.  
**Translation:** 

**[1197.98s] English:** Where there's this kind of human's  
**Translation:** 

**[1200.00s] English:** Writing exactly as instructed, at the level that a computer can understand. So they were.  
**Translation:** 

**[1206.22s] English:** Writing "add," "subtract," "multiply," you know, instructions. It's very tedious. But the belief,...  
**Translation:** Vocabulary: instructed: 按照指示; multiply: 乘法; subtract: 减法; tedious: 繁琐

**[1212.88s] English:** It was to write this lowest-level software that people use, which are called operating systems.  
**Translation:** 

**[1218.84s] English:** They had to be written in a semi-language because these high-level languages were just too  
**Translation:** 

**[1223.04s] English:** Inefficient. They were too slow, or the programs would be too big. So, that changed with a famous  
**Translation:** 

**[1232.46s] English:** Operating system called Unix, which is kind of the grandfather of all the operating systems today.  
**Translation:** Vocabulary: inefficient: 不高效

**[1238.80s] English:** So, Unix demonstrated that you could write something as complicated as an operating system.  
**Translation:** 

**[1243.86s] English:** In a language like C, so once that was true, then that meant we could hide the instruction set.  
**Translation:** 

**[1251.54s] English:** From the programmer.  
**Translation:** 

**[1253.04s] English:** And so, that meant then it didn't really matter. The programmer didn't have to write  
**Translation:** Vocabulary: programmer: 程序员

**[1258.64s] English:** Lots of these simple instructions. That was up to the compiler. So, that was part of our  
**Translation:** 

**[1263.14s] English:** Arguments for using risk are that if you were still writing in assembly language, there might be a better case.  
**Translation:** 

**[1267.60s] English:** For system constructions, but if the compiler can do that, it's going to be, you know, that's done.  
**Translation:** 

**[1273.12s] English:** Once, the computer translates it once. And then, every time you run the program, it runs at this.  
**Translation:** Vocabulary: constructions: 构造; translates: 翻译

**[1279.24s] English:** Potentially simpler instructions.  
**Translation:** 

**[1282.14s] English:** And so that was.  
**Translation:** 

**[1282.96s] English:** The reason why we were able to do that.  
**Translation:** 

**[1283.04s] English:** The debate, right, is because people would acknowledge that the simpler instructions,  
**Translation:** 

**[1288.78s] English:** Could lead to a faster computer. You can think of monosyllabic instructions. You could say them.  
**Translation:** 

**[1294.26s] English:** You know, if you think of reading, you probably read them faster or say them faster than.  
**Translation:** Vocabulary: monosyllabic: 单音节的

**[1298.06s] English:** Long instructions. The same thing. That analogy works pretty well for hardware.  
**Translation:** 

**[1302.50s] English:** And as long as you didn't have to read a lot more of those instructions, you could win.  
**Translation:** Vocabulary: analogy: 类比

**[1306.90s] English:** So, that's the basic idea for risk.  
**Translation:** 

**[1309.90s] English:** But it's interesting that in that discussion,  
**Translation:** 

**[1312.78s] English:** You know, Unix, and see that there's only one step of levels of abstraction from the.  
**Translation:** 

**[1320.00s] English:** Code that's really the closest to the machine, as opposed to code written by humans, is at least  
**Translation:** Vocabulary: abstraction: 抽象

**[1326.80s] English:** To me, again, perhaps a dumb intuition, but it feels like there might have been more layers sort of  
**Translation:** 

**[1333.68s] English:** Different kinds of humans stacked well on top of each other; um, so what's true and not true about that?  
**Translation:** Vocabulary: intuition: 直觉; stacked: 叠加

**[1339.68s] English:** You said that several layers of software are like, so for example, two layers would be  
**Translation:** 

**[1351.20s] English:** Suppose we just talk about two layers. That would be the operating system, like you get from  
**Translation:** 

**[1355.36s] English:** From Microsoft or from Apple, like iOS or the Windows operating system, and let's say.  
**Translation:** 

**[1361.92s] English:** Applications that run on top of it, like Word or Excel, so both the operating system could be.  
**Translation:** 

**[1369.44s] English:** Written with the operating system, but it's not the operating system that's going to be written.  
**Translation:** 

**[1369.68s] English:** In C, and the application could be written in C, so but you could construct those two layers and the  
**Translation:** 

**[1377.04s] English:** Applications absolutely do call upon the operating system, and the change was that both of them.  
**Translation:** 

**[1382.80s] English:** Could be written in higher-level languages, so it's one step of a translation, but you can still build.  
**Translation:** 

**[1387.92s] English:** Many layers of abstraction of software sit on top of that, and that's how things are done today, so  
**Translation:** 

**[1393.76s] English:** Uh, still today, many of the layers that you'll deal with you may deal with debuggers.  
**Translation:** 

**[1402.32s] English:** May deal with linkers, um, there's libraries; many of those today will be written in C++, say, uh.  
**Translation:** 

**[1412.40s] English:** Even though that language is pretty ancient, and even the Python interpreter is probably written  
**Translation:** Vocabulary: interpreter: 解释器; linkers: 链接器

**[1418.72s] English:** In C or C++, so lots of layers are probably written in these, uh,...  
**Translation:** 

**[1424.32s] English:** Some old-fashioned, efficient languages that still take just one step to produce these instructions.  
**Translation:** 

**[1433.36s] English:** Produce risk instructions, but they're composed such that each layer of software invokes one another through.  
**Translation:** 

**[1439.44s] English:** These  
**Translation:** Vocabulary: invokes: 调用

**[1440.00s] English:** Interfaces, and you can get 10 layers of software that way. So, in general, the risk was developed here.  
**Translation:** 

**[1446.48s] English:** Berkeley, it was kind of the three places that were these radicals who advocated for  
**Translation:** Vocabulary: advocated: 提倡; interfaces: 接口; radicals: 激进分子

**[1453.20s] English:** This is against the rest of the community, like IBM, Berkeley, and Stanford. You're one of these.  
**Translation:** 

**[1459.12s] English:** Radicals, and how radical did you feel? How confident did you feel? How doubtful were you that?  
**Translation:** Vocabulary: berkeley: 加州大学伯克利分校; doubtful: 怀疑; stanford: 斯坦福大学

**[1469.60s] English:** Risk might be the right approach because it may allow you to dive in and that is kind of taking a  
**Translation:** 

**[1474.80s] English:** Step back into simplicity, not forward into simplicity, yeah. No, it was easy to make, uh  
**Translation:** Vocabulary: simplicity: 简单性

**[1482.00s] English:** Yeah, it was easy to make the argument against it. Well, this was my colleague John Hennessey.  
**Translation:** 

**[1487.36s] English:** At Stanford, and I were both assistant professors, and for me, I just believed in  
**Translation:** Vocabulary: colleague: 同行

**[1493.28s] English:** The power of our ideas; I thought what we were saying made sense, Morris. Law is going to move fast.  
**Translation:** 

**[1500.00s] English:** The other thing I didn't mention is one of the surprises of these complex instruction sets.  
**Translation:** 

**[1505.60s] English:** You could certainly write these complex instructions if the programmer is writing.  
**Translation:** 

**[1509.28s] English:** It turned out to be kind of difficult for the compiler to generate those.  
**Translation:** Vocabulary: programmer: 编程人员

**[1514.72s] English:** Complex instructions kind of ironically would require finding the right circumstances.  
**Translation:** 

**[1519.92s] English:** Just exactly how to fit this complex instruction, it was actually easier for the compiler.  
**Translation:** Vocabulary: ironically: 反讽地

**[1523.60s] English:** To generate these simple instructions, so not only did the complex instructions make the hardware,  
**Translation:** 

**[1529.60s] English:** More difficult to build, often the compiler wouldn't even use them, and so it's harder to.  
**Translation:** 

**[1535.92s] English:** Build the compiler doesn't use them that much; the simple instructions go better with Moore's Law.  
**Translation:** 

**[1541.60s] English:** That's known as Moore's Law, where the number of transistors on a chip doubles approximately every two years, so we're gonna  
**Translation:** Vocabulary: transistors: 晶体管

**[1545.68s] English:** Have you known that reducing the time to design a microprocessor might be more important?  
**Translation:** 

**[1551.36s] English:** Than these number of instructions, so I think we believed that we were right that this.  
**Translation:** Vocabulary: microprocessor: 微处理器

**[1555.92s] English:** 16:10. WordPress.com  
**Translation:** 

**[1556.98s] English:** Transcript: 00? WordPress.com 10:00 ВАЧИ 10:00 ВАЧИ 00? WordPress.com 6:08 00:00? WordPress.com led the way to justification.  
**Translation:** Vocabulary: transcript: 录音文本

**[1557.32s] English:** That this was the best idea, then the question.  
**Translation:** 

**[1560.00s] English:** Became in these debates, well, yeah, that's a good technical idea, but in the business world, this...  
**Translation:** 

**[1565.56s] English:** It doesn't matter; there are other things that matter. It's like arguing that, if there's a standard,...  
**Translation:** 

**[1571.72s] English:** With the railroad tracks, and you've come up with a better way, but the whole world is covered in.  
**Translation:** 

**[1576.74s] English:** Railroad tracks, so your ideas will have no chance of success — right? Commercial success, it  
**Translation:** 

**[1582.30s] English:** It was technically right, but commercially it'll be insignificant, yeah. There's it's kind of sad.  
**Translation:** Vocabulary: commercially: 商业上; technically: 技术上

**[1587.04s] English:** That in this world, the history of human civilization is full of good ideas that were lost because  
**Translation:** 

**[1594.14s] English:** Somebody else came along first with a worse idea, and it's good that, in the computing world at least.  
**Translation:** Vocabulary: computing: 计算机领域

**[1600.24s] English:** Some of these have, well, you could say that. I mean, there's probably still some Cisco people who say, "Yeah,  
**Translation:** 

**[1605.52s] English:** Well, and what happened was what was interesting: a bunch of the Cisco companies with CISCO.  
**Translation:** Vocabulary: cisco: 思科

**[1613.88s] English:** Instruction sets of vocabulary; they gave up.  
**Translation:** 

**[1617.04s] English:** But not Intel, what Intel did to its credit, because Intel's vocabulary was  
**Translation:** 

**[1624.24s] English:** In the personal computer, and so that was a very valuable vocabulary because the way we  
**Translation:** 

**[1630.48s] English:** Distribute software is in those actual instructions; it's in the instructions of that instruction set.  
**Translation:** 

**[1636.18s] English:** So, uh, they don't give you the source code that the programmers wrote; you get it after it's  
**Translation:** 

**[1642.06s] English:** Been translated into the lowest level; that's if you were to get a floppy disk or download.  
**Translation:** Vocabulary: floppy: 软盘; programmers: 程序员

**[1646.66s] English:** Software: You're going to get a floppy disk, and you're going to get another floppy disk, and you're going  
**Translation:** 

**[1647.02s] English:** To get a floppy disk, and you're going to get a floppy disk, and you're going to get a floppy disk, and so forth.  
**Translation:** 

**[1650.04s] English:** The x86 instruction set was very valuable, so what Intel did cleverly and amazingly is that they had their  
**Translation:** 

**[1658.08s] English:** Chips in hardware do a translation step; they would take these complex instructions and translate them.  
**Translation:** 

**[1664.82s] English:** Into essentially real-time risk instructions for hardware on-the-fly, you know, at gigahertz clock speeds.  
**Translation:** 

**[1670.98s] English:** And then, any good idea that risk people had, they could use, and they could still be compatible with.  
**Translation:** Vocabulary: compatible: 兼容的; gigahertz: 吉赫兹

**[1676.76s] English:** This  
**Translation:** 

**[1677.02s] English:** With this really valuable  
**Translation:** 

**[1680.00s] English:** PC software, software base, and which also had very high volumes—你知道，达到一亿个人左右。  
**Translation:** 

**[1686.24s] English:** Computers per year, so the Cisco architecture in the business world was actually one of the key players in this PC era.  
**Translation:** Vocabulary: cisco: 思科

**[1695.04s] English:** So, just going back to the time of designing risks: when you design an instruction set,...  
**Translation:** 

**[1706.02s] English:** Architecture: Do you think like a programmer, or do you think like a microprocessor engineer?  
**Translation:** Vocabulary: microprocessor: 微处理器; programmer: 程序员

**[1711.50s] English:** Do you think like an artist, a philosopher? Do you think in terms of software and hardware? I mean, is it art?  
**Translation:** 

**[1719.60s] English:** Is it science? Yeah, I'd say so. I think designing a good instruction set is an art, and I think you're  
**Translation:** 

**[1726.12s] English:** Trying to balance the simplicity and speed of execution with how well it is easy.  
**Translation:** 

**[1736.00s] English:** You can do it, and how well you can do it, and how well you can do it, and how well you can do it.  
**Translation:** Vocabulary: execution: 执行; simplicity: 简单

**[1736.02s] English:** How easy will it be for compilers to use it? You're trying to create an instruction set.  
**Translation:** 

**[1740.40s] English:** That everything in there can be used by compilers; there's nothing missing that'll make.  
**Translation:** Vocabulary: compilers: 编译器

**[1747.88s] English:** It can be difficult for the program to run efficiently, but you want it to be easy to build.  
**Translation:** 

**[1753.30s] English:** As well, so it's that kind of thing. So you're thinking? I'd say you're thinking about hardware trying to find.  
**Translation:** Vocabulary: efficiently: 高效地

**[1757.48s] English:** A hard software compromise that'll work well, and it's, you know, it's a matter  
**Translation:** 

**[1764.32s] English:** Of taste, right? It's  
**Translation:** Vocabulary: compromise: 折中方案

**[1766.00s] English:** It's kind of fun to build instruction sets. It's not that hard to build an instruction set, but  
**Translation:** 

**[1771.74s] English:** To build one that catches on and people use, you know, you have to be, you know, fortunate to be.  
**Translation:** 

**[1778.10s] English:** Right place at the right time, or have a design that people really like—are you using metrics?  
**Translation:** 

**[1783.22s] English:** So, is it quantifiable? Because you kind of have to anticipate the kinds of programs that people will use.  
**Translation:** Vocabulary: anticipate: 预估; metrics: 指标; quantifiable: 可量化

**[1789.18s] English:** Write, yeah, ahead of time. So, can you use numbers? Can you use metrics? Can you quantify?  
**Translation:** 

**[1795.26s] English:** Something ahead of time is kind of fun to build, whether it's instruction sets or anything else.  
**Translation:** Vocabulary: quantify: 量化

**[1795.98s] English:** Ahead of time, or is this again the art part where you're kind of like, "No, it's uh  
**Translation:** 

**[1800.00s] English:** A big change, kind of what happened, I think, from Hennessy's and my perspective in the 1980s, was going from really relying on taste and hunches to something more quantifiable.  
**Translation:** 

**[1816.58s] English:** And in fact, he and I wrote a textbook at the end of the 1980s called "Computer Architecture: A Quantitative Approach.  
**Translation:** 

**[1823.36s] English:** I heard of that. And it's the thing; it had a pretty big impact in the field because we went from textbooks that kind of listed, "so here's what this computer does," and "here's the pros and cons," and "here's what this computer does" and "pros and cons," to something where there were formulas and equations where you could measure things.  
**Translation:** Vocabulary: equations: 数学方程; formulas: 公式; quantitative: 定量的

**[1842.30s] English:** So, specifically for instruction sets, what we do—and some other fields do—is to agree upon a set of programs, which we call benchmarks.  
**Translation:** 

**[1853.36s] English:** And a suite of programs, and then you develop both the hardware and the compiler. You get numbers on how well your computer performs, given its instruction set, how well you implemented it in your microprocessor, and how good your compilers are.  
**Translation:** Vocabulary: benchmarks: 参考基准; compilers: 编译器; implemented: 实现; microprocessor: 微处理器

**[1872.64s] English:** In computer architecture, you know, we grade on a curve rather than on an absolute scale, using professor's terms.  
**Translation:** 

**[1879.22s] English:** So, when you say these programs run this fast, well, that's kind of incorrect.  
**Translation:** 

**[1883.36s] English:** It's interesting, but how do you know it's better?  
**Translation:** 

**[1885.22s] English:** Well, you compare it to other computers of the same time.  
**Translation:** 

**[1888.62s] English:** So, the best way we know how to make it into a kind of more scientific and experimental and quantitative approach is to compare yourself to other computers of the same era that have the same access and the same kind of technology on commonly agreed-upon benchmark programs.  
**Translation:** 

**[1905.62s] English:** So, maybe to toss up two possible directions we can go: one is what are the different trade-offs in designing?  
**Translation:** Vocabulary: benchmark: 参考基准; quantitative: 量化指标

**[1913.36s] English:** Architecture is, we've been talking about risk and risk, but perhaps a little bit more detail in terms of specifics.  
**Translation:** 

**[1920.00s] English:** Features that you were thinking about, and the other side is what are the metrics that you're  
**Translation:** Vocabulary: metrics: 衡量标准

**[1925.18s] English:** Thinking about when looking at these trade-offs, yeah, let's talk about the metrics. So, during these...  
**Translation:** 

**[1932.28s] English:** Debates: We actually had a hard time explaining and convincing people about the ideas.  
**Translation:** 

**[1937.14s] English:** Partly, we didn't have a formula to explain it, and a few years into it, we hit upon the formula.  
**Translation:** 

**[1943.18s] English:** That helped explain what was going on, and I think if we can do this, see how it works, orally.  
**Translation:** Vocabulary: orally: 口头地

**[1949.84s] English:** So, uh, the way you can do it orally is: Let's see. So, fundamentally, the way you do it is:  
**Translation:** 

**[1958.78s] English:** Measure performance is how long it takes a program to run. If you have 10 programs,  
**Translation:** Vocabulary: fundamentally: 本质上

**[1964.92s] English:** And typically, these benchmarks were sweet because you'd want to have 10 programs, so they could  
**Translation:** 

**[1969.24s] English:** Represent lots of different applications, so for these 10 programs, how long did it take to run?  
**Translation:** Vocabulary: benchmarks: 参考标准

**[1973.78s] English:** Well, now when you're trying to explain why it took so long, you could factor in how long it takes a  
**Translation:** 

**[1979.18s] English:** Program to run.  
**Translation:** 

**[1979.84s] English:** Into three factors: the first one is how many instructions did it take to execute.  
**Translation:** 

**[1986.84s] English:** So, that's what we've been talking about: you know, the instructions from the academy, how.  
**Translation:** Vocabulary: execute: 执行

**[1991.36s] English:** Many did it take? All right, the next question is: How long did each instruction take to run?  
**Translation:** 

**[1997.70s] English:** On average, you'd multiply the number of instructions by how long it took to run.  
**Translation:** Vocabulary: multiply: 相乘

**[2002.68s] English:** And that gets you how much time, okay? So that's but now let's look at this metric of how long did  
**Translation:** 

**[2008.76s] English:** It takes the instruction to run.  
**Translation:** Vocabulary: metric: 衡量标准

**[2009.84s] English:** Well, it turns out that the way we can build computers today is that they all have a clock, and you've seen  
**Translation:** 

**[2015.92s] English:** This: When you buy a microprocessor, it'll say 3.1 gigahertz or 2.5 gigahertz, and so on.  
**Translation:** Vocabulary: gigahertz: 吉赫兹; microprocessor: 微处理器

**[2022.62s] English:** Gigahertz is good. Well, what that is, is the speed of the clock. So, 2.5 gigahertz turns out to be:  
**Translation:** 

**[2029.80s] English:** Four billionths of an instruction, or four nanoseconds, so that's the clock cycle time.  
**Translation:** Vocabulary: billionths: 十亿分之一; nanoseconds: 纳秒

**[2034.90s] English:** But there's another factor, which is what's the average number of clocked.  
**Translation:** 

**[2039.84s] English:** Cycles  
**Translation:** 

**[2040.00s] English:** It takes per instruction. So it's the number of instructions, average number of clock cycles.  
**Translation:** 

**[2044.80s] English:** And the clock cycle time. So, in these risk-sys debates, they would concentrate on, but risk,...  
**Translation:** 

**[2051.50s] English:** Needs to take more instructions. And we'd argue that maybe the clock cycle is faster. But what?  
**Translation:** 

**[2057.14s] English:** The real big difference was the number of clock cycles per instruction.  
**Translation:** 

**[2061.30s] English:** Per instruction, that's fascinating. What about the beautiful mess of parallelism in the whole?  
**Translation:** 

**[2066.20s] English:** Picture? Parallelism, which has to do with, say, how many instructions could execute in parallel.  
**Translation:** Vocabulary: parallel: 并行

**[2071.20s] English:** And things like that. You could think of that as affecting the clock cycles per instruction.  
**Translation:** 

**[2075.56s] English:** Because it's the average clock cycles per instruction. So, when you're running a program,  
**Translation:** 

**[2079.42s] English:** If it took 100 billion instructions, and on average, it took two clock cycles per instruction,  
**Translation:** 

**[2086.00s] English:** And they were four nanoseconds; you could multiply that out and see how long it took to run.  
**Translation:** 

**[2089.70s] English:** And there are all kinds of tricks to try and reduce the number of clock cycles per instruction.  
**Translation:** 

**[2095.34s] English:** But it turns...  
**Translation:** 

**[2096.20s] English:** It turned out that the way they would do these complex instructions is that they would actually build  
**Translation:** 

**[2100.76s] English:** What we would call an interpreter, and a simpler, very simple hardware interpreter. But it turned  
**Translation:** Vocabulary: interpreter: 解释器

**[2106.46s] English:** Out that for the sys constructions, if you had to use one of those interpreters, it would be like:  
**Translation:** 

**[2111.46s] English:** 10 clock cycles per instruction, where the risk constructions could be two. So there would be this:  
**Translation:** Vocabulary: constructions: 构造; interpreters: 解释器

**[2116.80s] English:** Factor of five advantage in clock cycles per instruction. We have to execute, say, 25 or 50%.  
**Translation:** 

**[2122.80s] English:** More instructions. So that's where the win would come. And then you could make an argument.  
**Translation:** Vocabulary: execute: 执行

**[2126.20s] English:** Whether the clock cycle times are the same or not, but pointing out that we could divide  
**Translation:** 

**[2130.86s] English:** The benchmark results, time per program, were divided into three factors. And the biggest difference was in  
**Translation:** Vocabulary: benchmark: 参考标准

**[2136.68s] English:** Risk and Sys was the clock cycles per... you execute a few more instructions, but the clock  
**Translation:** 

**[2141.22s] English:** Cycles per instruction is much less. And that was what this debate was about.... Once we made that argument,...  
**Translation:** 

**[2147.48s] English:** Then people said, "Oh, okay, I get it." And so we went from... It was outrageously controversial in...  
**Translation:** 

**[2155.32s] English:** 1982.  
**Translation:** 

**[2156.20s] English:** That maybe by 1984 or so, people said, "Oh, yeah.  
**Translation:** 

**[2160.00s] English:** Technically, they've got a good argument. What are the instructions in the risk instruction set?  
**Translation:** Vocabulary: technically: 在技术上

**[2166.22s] English:** Just to get an intuition? Okay. In 1995, I was asked to predict the future of what microprocessor.  
**Translation:** 

**[2174.08s] English:** Future. So, I'd seen these predictions, and usually people predict something outrageous.  
**Translation:** Vocabulary: intuition: 直觉; microprocessor: 微处理器; outrageous: 离谱的

**[2180.58s] English:** Just to be entertaining, right? And so, my prediction for 2020 was: things are  
**Translation:** 

**[2186.54s] English:** Going to be pretty much the same, they're going to look very familiar to what they are—and they are.  
**Translation:** Vocabulary: entertaining: 有趣

**[2190.78s] English:** And if you were to read the article, you'd know that the things I said are pretty much true. The  
**Translation:** 

**[2194.92s] English:** Instructions that have been around forever are kind of the same, and that's outrageous.  
**Translation:** 

**[2199.32s] English:** Prediction, actually. Yeah. Given how fast computers have been growing, well, and you know,  
**Translation:** 

**[2202.78s] English:** Morse Law was going to go on for 25 more years, we thought. You know, who knows? But kind of the  
**Translation:** 

**[2208.38s] English:** Surprising thing, in fact, Hennessy and I won the ACM/IEEE Turing Award for both.  
**Translation:** 

**[2215.98s] English:** The risk control, and the risk control. And, you know, we're going to be talking about the  
**Translation:** Vocabulary: turing: 图灵

**[2216.54s] English:** Construction set contributions, and for that textbook I mentioned. But, you know, we're  
**Translation:** 

**[2220.50s] English:** Surprised that here we are, 35-40 years later after we did our work. And the conventionalism,...  
**Translation:** Vocabulary: conventionalism: 传统主义

**[2230.30s] English:** Of the best way to do instruction sets is still those risk construction sets that look very  
**Translation:** 

**[2235.14s] English:** Similar to what we looked like, you know, we did in the 1980s. So, those surprisingly, there haven't been  
**Translation:** 

**[2241.22s] English:** Been some radical new idea, even though we have, you know, a million times as many transitions.  
**Translation:** 

**[2246.54s] English:** Features as we had back then. But what are the basic constructions, and how did they change over?  
**Translation:** Vocabulary: constructions: 基本结构; transitions: 转换过程

**[2252.62s] English:** The years? So, are we talking about addition, subtraction? These are the... Okay, the specific...  
**Translation:** 

**[2257.06s] English:** So, the things that are in a calculator are also in a computer. So, any of the buttons that are in the  
**Translation:** Vocabulary: calculator: 计算器; subtraction: 减法

**[2263.12s] English:** Calculator in the computer. So, if there's a memory function key, and as I said, those are  
**Translation:** 

**[2269.18s] English:** Turning something into a form that can be stored in memory is called a store, and bringing something back from memory is called a load.  
**Translation:** 

**[2272.60s] English:** Just a quick tangent. When you say "memory," what does that mean?  
**Translation:** 

**[2276.54s] English:** Well, I told you there were five pieces in a computer.  
**Translation:** Vocabulary: tangent: 旁枝逸出

**[2280.60s] English:** And if you remember, on a calculator, there's a memory key.  
**Translation:** 

**[2283.46s] English:** So, you want to have an intermediate calculation and bring it back later.  
**Translation:** 

**[2286.50s] English:** So, you'd hit the memory plus key (M+), maybe, and it would put that into memory.  
**Translation:** 

**[2290.88s] English:** And then you'd hit an RM like recurrent maintenance, and then bring it back into the display.  
**Translation:** Vocabulary: recurrent: 反复发生的

**[2295.12s] English:** So, you don't have to type it.  
**Translation:** 

**[2296.24s] English:** You don't have to write it down and bring it back again.  
**Translation:** 

**[2297.92s] English:** So, that's exactly what memory is.  
**Translation:** 

**[2299.68s] English:** You can put things into it as temporary storage, and bring it back when you need it later.  
**Translation:** 

**[2305.32s] English:** So, that's memory and loads and stores.  
**Translation:** 

**[2307.22s] English:** But the big thing—the difference between a computer and a calculator—is that the computer can make decisions.  
**Translation:** 

**[2314.84s] English:** And amazingly, decisions are as simple as: is this value less than zero, or is this value bigger than that value?  
**Translation:** 

**[2323.02s] English:** So there are those instructions, which are called conditional branch instructions, and it is these that give computers all their power.  
**Translation:** Vocabulary: conditional: 条件

**[2329.88s] English:** If you were in the early days of computing before what's called the general-purpose microprocessor,  
**Translation:** 

**[2335.14s] English:** People would write these instructions.  
**Translation:** Vocabulary: computing: 计算; microprocessor: 微处理器

**[2337.84s] English:** Kind of in hardware, but it couldn't make decisions.  
**Translation:** 

**[2341.64s] English:** It would just do the same thing over and over again.  
**Translation:** 

**[2345.44s] English:** With the power of having branch instructions, it can look at things and make decisions automatically.  
**Translation:** 

**[2350.50s] English:** And it can make these decisions, you know, billions of times per second.  
**Translation:** 

**[2353.66s] English:** And amazingly enough, we can get, thanks to advanced machine learning,  
**Translation:** 

**[2358.12s] English:** We can create programs that can do something smarter than what human beings can do.  
**Translation:** 

**[2362.82s] English:** But if you go down that very basic level, it's the instructions that are the keys.  
**Translation:** 

**[2367.04s] English:** It's on the calculator, plus the ability to make decisions based on these conditional branch instructions.  
**Translation:** Vocabulary: calculator: 计算器

**[2371.96s] English:** And all decisions fundamentally can be reduced down to these branch instructions.  
**Translation:** 

**[2376.78s] English:** Yeah.  
**Translation:** Vocabulary: fundamentally: 本质上

**[2377.10s] English:** So, in fact, and so, you know, going way back in the stack, back to, you know,  
**Translation:** 

**[2382.34s] English:** We did four risk projects at Berkeley in the 1980s.  
**Translation:** Vocabulary: berkeley: 加州大学伯克利分校

**[2385.60s] English:** They did a couple of studies at Stanford in the 1980s.  
**Translation:** 

**[2388.64s] English:** In 2010, we decided we wanted to do a new instruction set.  
**Translation:** Vocabulary: stanford: 斯坦福大学

**[2393.82s] English:** Learning from the mistakes of those risk architectures in 1980.  
**Translation:** 

**[2397.04s] English:** And that was done here at Berkeley.  
**Translation:** 

**[2400.00s] English:** Almost exactly 10 years ago, and the people who did it—I participated, but Krista Sanovich and  
**Translation:** 

**[2406.74s] English:** Others drove it. They called it RISC-V, to honor the four RISC projects of the 1980s.  
**Translation:** 

**[2413.62s] English:** So, what does RISC-V involve? RISC-V is another instruction set architecture. It's  
**Translation:** 

**[2420.42s] English:** Learned from the mistakes of the past, but it still has: if you look at the, there's a core.  
**Translation:** 

**[2424.98s] English:** A set of instructions. It's very similar to the simplest architectures from the 1980s.  
**Translation:** 

**[2429.56s] English:** And the big difference about RISC-V is that it's open. So, I talked earlier about proprietary versus  
**Translation:** Vocabulary: proprietary: 私有产权的

**[2435.76s] English:** Open software. So, this is an instruction set — so it's a vocabulary. It's not hardware.  
**Translation:** 

**[2445.12s] English:** But by having an open instruction set, we can have open-source implementations.  
**Translation:** Vocabulary: implementations: 实现方式

**[2450.28s] English:** Open-source processors that people can use.  
**Translation:** 

**[2453.56s] English:** Where do you see that?  
**Translation:** Vocabulary: processors: 处理器

**[2454.98s] English:** Going, it's a really exciting possibility, but just like in Scientific American,  
**Translation:** 

**[2460.22s] English:** If you were to predict 10, 20, or 30 years from now, that kind of ability to utilize open source...  
**Translation:** 

**[2467.20s] English:** Instruction sets architectures like RISC-V: What kind of possibilities might they unlock?  
**Translation:** 

**[2473.72s] English:** Yeah, and so just to make it clear, because this is confusing, the specification of RISC-V is  
**Translation:** Vocabulary: specification: 规范; unlock: 解锁

**[2480.42s] English:** Something that's like in a textbook. There are books about it. So that's what,  
**Translation:** 

**[2484.98s] English:** Defining an interface. There's also the way you build hardware, which is often written in specialized languages.  
**Translation:** Vocabulary: interface: 接口

**[2491.68s] English:** They're kind of like C, but they're specialized for hardware that gets translated into hardware.  
**Translation:** 

**[2498.24s] English:** And so, these implementations of this specification are what are open source. They're written,...  
**Translation:** 

**[2504.48s] English:** In something that's called Verilog or VHDL, but it's put up on the web, just like you can see the.  
**Translation:** 

**[2510.84s] English:** C++ Code for Linux on the Web.  
**Translation:** Vocabulary: verilog: 硬件描述语言

**[2514.78s] English:** So, that's what it's called.  
**Translation:** 

**[2514.96s] English:** That's the open instruction set that enables open-source implementations.  
**Translation:** 

**[2520.00s] English:** Of RISC-V. They can literally build a processor using this instruction set. People are doing it.  
**Translation:** 

**[2525.24s] English:** Are. So, what happened to us that the story was developed here for our use to do our  
**Translation:** Vocabulary: processor: 处理器

**[2530.42s] English:** Research. And we made it; we licensed it under the Berkeley Software Distribution License, like a lot.  
**Translation:** 

**[2536.56s] English:** Of things get licensed here, so other academics would not be afraid to use it. And  
**Translation:** Vocabulary: berkeley: 伯克利

**[2540.98s] English:** Then, around 2014, we started getting complaints that we were using it in our research and in our  
**Translation:** 

**[2547.66s] English:** Courses, and we got complaints from people in industries. Why did you change your instructions?  
**Translation:** 

**[2552.68s] English:** Set between the fall and the spring semester? And, well, we get complaints from industry time.  
**Translation:** 

**[2558.66s] English:** Why the hell do you care what we do with our instruction set? And then, when we talked to...  
**Translation:** 

**[2562.86s] English:** They, we found out, there was this thirst for this idea of an open instruction set architecture. And  
**Translation:** 

**[2567.78s] English:** They had been looking for one. They stumbled upon ours at Berkeley, thought it was, boy,  
**Translation:** Vocabulary: stumbled: 偶然发现; thirst: 强烈需求

**[2572.84s] English:** This looks great. We should use this one. And so, once we realized there was,  
**Translation:** 

**[2577.66s] English:** This need for an open instruction set architecture, we thought it was a great idea. And then we  
**Translation:** 

**[2582.40s] English:** Started supporting it and trying to make it happen. So, this was kind of something we accidentally stumbled into.  
**Translation:** 

**[2588.56s] English:** This is exactly what we needed, and our timing was good. So it's really taking off. There's, you know,  
**Translation:** Vocabulary: timing: 时机

**[2596.84s] English:** Universities are good at starting things, but they're not good at sustaining things. So, like  
**Translation:** 

**[2600.58s] English:** Linux has a Linux Foundation. There's a RISC-V Foundation that we started. There's,  
**Translation:** Vocabulary: sustaining: 维持

**[2606.28s] English:** Annual conferences. And there's a RISC-V Foundation that we started. And there's a RISC-V Foundation.  
**Translation:** 

**[2607.64s] English:** That we started. And the first one was done, I think, in January of 2015. And the one that was just  
**Translation:** Vocabulary: conferences: 会议

**[2612.52s] English:** Last December, it had 50 people at it. And the one last December had, I don't know,  
**Translation:** 

**[2618.82s] English:** 1,700 people were at it, and the companies were excited all over the world. So, if predicting into the  
**Translation:** 

**[2624.96s] English:** Future, you know, if we were doing 25 years, I would predict that RISC-V will be, you know,  
**Translation:** 

**[2631.12s] English:** Possibly the most popular instruction set architecture out there, because it's a pretty  
**Translation:** 

**[2637.64s] English:** Popular instruction set architecture, and it's open and free.  
**Translation:** 

**[2640.00s] English:** And there's no reason why lots of people shouldn't use it.  
**Translation:** 

**[2644.36s] English:** And there are benefits, just like Linux was so popular today compared to 20 years ago.  
**Translation:** 

**[2652.24s] English:** And, you know, the fact that you can get access to it for free, you can modify it, and you can improve it—for all those same arguments.  
**Translation:** 

**[2659.90s] English:** And so, people collaborate to make it a better system for everyone to use.  
**Translation:** 

**[2663.76s] English:** And that works in software. And I expect the same thing will happen in hardware.  
**Translation:** Vocabulary: collaborate: 合作

**[2666.98s] English:** Sure. So, if you look at ARM, Intel, MIPS—if you look at just the lay of the land—and what do you think, just for me, because I'm not familiar with how difficult this kind of transition would be, and how much challenge it would entail.  
**Translation:** 

**[2688.02s] English:** Do you see? Let me ask my dumb question in another way.  
**Translation:** Vocabulary: entail: 包含

**[2692.38s] English:** No, that's where I know you're headed.  
**Translation:** 

**[2695.24s] English:** Well, there's a bunch.  
**Translation:** 

**[2696.30s] English:** I think the thing.  
**Translation:** 

**[2696.98s] English:** You point out that there are these proprietary, very popular instruction sets, such as x86.  
**Translation:** 

**[2702.58s] English:** And so, how do we move to RISC-V potentially in the span of 5, 10, or 20 years, given that the devices, the way we use them (IoT, mobile devices, and the cloud), keep changing?  
**Translation:** 

**[2719.84s] English:** Well, part of it—a big piece of it—is the software stack.  
**Translation:** 

**[2725.74s] English:** And what, right?  
**Translation:** 

**[2727.02s] English:** Now, looking forward, there seem to be three important markets.  
**Translation:** 

**[2731.06s] English:** There's the cloud.  
**Translation:** 

**[2733.10s] English:** And then, the cloud is simply companies like Alibaba and Amazon, Google, Microsoft, having these giant data centers with tens of thousands of servers in perhaps a hundred of these data centers all over the world.  
**Translation:** 

**[2750.32s] English:** And that's what the cloud is.  
**Translation:** 

**[2751.40s] English:** So, the computer that dominates the cloud is the x86 instruction set.  
**Translation:** Vocabulary: dominates: 占据主导

**[2755.94s] English:** So, the instruction.  
**Translation:** 

**[2756.90s] English:** Okay.  
**Translation:** 

**[2756.98s] English:** Or the instruction sets used in the cloud are X86.  
**Translation:** 

**[2760.00s] English:** Almost 100% of that today is x86.  
**Translation:** 

**[2764.80s] English:** The other big things are cell phones and laptops.  
**Translation:** 

**[2769.56s] English:** Those are the big things today.  
**Translation:** Vocabulary: laptops: 笔记本电脑

**[2770.90s] English:** I mean, the PC is also dominated by the x86 Instruction Set, but those sales are dwindling.  
**Translation:** 

**[2777.20s] English:** You know, there are maybe 200 million PCs a year, and one and a half billion phones a year.  
**Translation:** Vocabulary: dominated: 被支配; dwindling: 减少

**[2783.88s] English:** There's numbers like that.  
**Translation:** 

**[2784.86s] English:** So, for the phones, that's dominated by ARM.  
**Translation:** 

**[2790.28s] English:** And one reason I talked about the software stacks is that the third category is the Internet of Things, which is basically embedded devices, things in your cars, in your microwaves, everywhere.  
**Translation:** 

**[2803.14s] English:** So, what's different about those three categories is that for the cloud, the software that runs in the cloud is determined by these companies: Alibaba, Amazon, Google, and Microsoft.  
**Translation:** Vocabulary: embedded: 嵌入式的; microwaves: 微波炉; stacks: 软件栈

**[2813.68s] English:** So, they control that software stack.  
**Translation:** 

**[2816.86s] English:** For the cell phones, there's both.  
**Translation:** 

**[2819.48s] English:** For Android and Apple, there's software they supply, but both of them have marketplaces where anybody in the world can build software.  
**Translation:** 

**[2827.06s] English:** And that software is translated or compiled down and shipped in the vocabulary of ARM.  
**Translation:** Vocabulary: compiled: 编译; marketplaces: 应用市场

**[2835.18s] English:** So, that's what's referred to as binary-compatible because the actual instructions are turned into binary numbers and shipped around the world.  
**Translation:** 

**[2844.90s] English:** And so, just a quick interruption.  
**Translation:** Vocabulary: binary: 二进制; interruption: 中断

**[2847.26s] English:** So, ARM: What is ARM?  
**Translation:** 

**[2849.48s] English:** ARM is an instruction set, like a risk-based one.  
**Translation:** 

**[2852.72s] English:** Yeah, it's a risk-based instruction set.  
**Translation:** 

**[2854.12s] English:** It's a proprietary one.  
**Translation:** Vocabulary: proprietary: 私有的

**[2855.38s] English:** ARM stands for Advanced Risk Machine.  
**Translation:** 

**[2860.70s] English:** ARM is the name of the company.  
**Translation:** 

**[2862.38s] English:** So, it's a proprietary risk architecture.  
**Translation:** 

**[2865.68s] English:** And it's been around for a while, and is surely the most popular instruction set in the world right now.  
**Translation:** 

**[2871.64s] English:** Every year, billions of chips are using the ARM design in this post-PC era.  
**Translation:** 

**[2878.44s] English:** Was it one of the?  
**Translation:** 

**[2879.40s] English:** Yeah.  
**Translation:** 

**[2879.46s] English:** Early Risk.  
**Translation:** 

**[2880.00s] English:** Adopters of the RISC idea?  
**Translation:** 

**[2882.46s] English:** The first ARM goes back.  
**Translation:** Vocabulary: adopters: 采纳者

**[2884.18s] English:** I don't know; it's around 86 or so.  
**Translation:** 

**[2885.66s] English:** So, Berkeley did their work instead.  
**Translation:** Vocabulary: berkeley: 伯克利大学

**[2887.40s] English:** In the early 1980s.  
**Translation:** 

**[2888.82s] English:** The ARM guys needed an instruction set.  
**Translation:** 

**[2891.52s] English:** And they read our papers.  
**Translation:** 

**[2893.12s] English:** And it heavily influenced them.  
**Translation:** 

**[2897.16s] English:** So, getting back to my story,  
**Translation:** 

**[2898.12s] English:** What about the Internet of Things?  
**Translation:** 

**[2899.08s] English:** Well, software is not shipped.  
**Translation:** 

**[2900.54s] English:** In the Internet of Things.  
**Translation:** 

**[2901.26s] English:** It's the embedded device.  
**Translation:** 

**[2904.70s] English:** People control that software stack.  
**Translation:** Vocabulary: embedded: 内置的

**[2906.88s] English:** So, the opportunities for RISC are numerous.  
**Translation:** 

**[2909.88s] English:** Everyone thinks,  
**Translation:** 

**[2911.10s] English:** Is it in the Internet of Things?  
**Translation:** 

**[2912.66s] English:** Embedded things, because  
**Translation:** 

**[2913.68s] English:** There's no dominant player.  
**Translation:** 

**[2915.50s] English:** Like there is in the cloud.  
**Translation:** Vocabulary: dominant: 占据优势

**[2916.74s] English:** For the smartphones.  
**Translation:** 

**[2919.92s] English:** And it doesn't have a lot.  
**Translation:** 

**[2922.74s] English:** Of licenses associated with  
**Translation:** 

**[2924.14s] English:** And you can enhance the instruction.  
**Translation:** Vocabulary: enhance: 提高

**[2925.82s] English:** Set if you want.  
**Translation:** 

**[2927.06s] English:** And people have looked.  
**Translation:** 

**[2930.34s] English:** At instruction sets, and think,...  
**Translation:** 

**[2931.34s] English:** It's a very good instruction set.  
**Translation:** 

**[2932.88s] English:** So, it appears to be very popular there.  
**Translation:** 

**[2935.46s] English:** It's possible that in the cloud,  
**Translation:** 

**[2939.20s] English:** People,  
**Translation:** 

**[2939.88s] English:** Those companies control.  
**Translation:** 

**[2940.92s] English:** Their software stacks.  
**Translation:** 

**[2941.84s] English:** So, it's possible.  
**Translation:** Vocabulary: stacks: 堆积

**[2943.62s] English:** That they would decide.  
**Translation:** 

**[2945.62s] English:** To use RISC-V.  
**Translation:** 

**[2946.44s] English:** If we're talking about 10,  
**Translation:** 

**[2947.34s] English:** And in 20 years from now.  
**Translation:** 

**[2949.66s] English:** The one that would be harder.  
**Translation:** 

**[2950.60s] English:** Would be the cell phones.  
**Translation:** 

**[2951.80s] English:** Since people ship software,  
**Translation:** 

**[2953.06s] English:** In the ARM instruction set.  
**Translation:** 

**[2955.06s] English:** That you'd think,  
**Translation:** 

**[2955.78s] English:** Be the more difficult one.  
**Translation:** 

**[2957.42s] English:** But if RISC-V really catches on,  
**Translation:** 

**[2959.64s] English:** In a period of a decade,  
**Translation:** 

**[2962.28s] English:** You can imagine.  
**Translation:** 

**[2962.76s] English:** That's changing over, too.  
**Translation:** 

**[2964.48s] English:** Do you have a sense?  
**Translation:** 

**[2964.98s] English:** Why is RISC-V or ARM dominated?  
**Translation:** Vocabulary: dominated: 占据主导地位

**[2967.70s] English:** You mentioned these three categories.  
**Translation:** 

**[2969.00s] English:** Why did ARM dominate?  
**Translation:** Vocabulary: dominate: 占据主导地位

**[2971.32s] English:** Why does it dominate?  
**Translation:** 

**[2972.20s] English:** The mobile device space?  
**Translation:** 

**[2974.06s] English:** And maybe my naive intuition.  
**Translation:** 

**[2977.66s] English:** Is that there are some aspects?  
**Translation:** Vocabulary: intuition: 直觉; naive: 天真

**[2979.04s] English:** Of power efficiency.  
**Translation:** 

**[2980.04s] English:** That are important.  
**Translation:** 

**[2980.94s] English:** That somehow come along with RISC.  
**Translation:** 

**[2983.18s] English:** Well, part of it is.  
**Translation:** 

**[2984.22s] English:** For these old SISC instruction sets,  
**Translation:** 

**[2987.56s] English:** Like in the x86,  
**Translation:** 

**[2992.12s] English:** It was more expensive.  
**Translation:** 

**[2994.02s] English:** To these,  
**Translation:** 

**[2997.06s] English:** You know, they're older.  
**Translation:** 

**[2998.00s] English:** So they,  
**Translation:** 

**[2999.00s] English:** They have a disadvantage.  
**Translation:** 

**[3000.00s] English:** Because they were designed 40 years ago. But also, they have to translate from system constructions to RISC constructions on the fly. And that costs both silicon area; the chips are bigger to be able to do that, and it uses more power.  
**Translation:** Vocabulary: constructions: 架构; silicon: 硅片

**[3015.14s] English:** So, ARM, which has followed this RISC philosophy, is seen to be much more energy-efficient. And in today's computer world, both in the cloud and cell phones and other things, the limiting resource isn't the number of transistors you can fit on the chip.  
**Translation:** 

**[3033.38s] English:** It's how much power you can dissipate for your application. So, by having a reduced instruction set, it's possible to have simpler hardware, which is more energy-efficient.  
**Translation:** Vocabulary: dissipate: 散发; transistors: 晶体管

**[3045.14s] English:** And energy efficiency is incredibly important in the cloud. When you have tens of thousands of computers in a data center, you want the most energy-efficient ones there as well.  
**Translation:** 

**[3054.68s] English:** And, of course, for embedded things running off of batteries, you want them to be energy-efficient, and cell phones too.  
**Translation:** Vocabulary: embedded: 嵌入式

**[3059.96s] English:** So, I think it's believed that there's an energy disadvantage to using these more complex instruction set architectures.  
**Translation:** 

**[3071.36s] English:** So, the other aspect of this is if we look at Apple and Qualcomm.  
**Translation:** Vocabulary: qualcomm: 高通

**[3075.14s] English:** Samsung, Huawei, all use the ARM architecture, and yet the performance of the systems varies.  
**Translation:** 

**[3082.30s] English:** I mean, I don't know whose opinion you take, but Apple, for some reason, seems to perform better in terms of these implementations and architectures.  
**Translation:** Vocabulary: implementations: 实现方式

**[3090.64s] English:** So, where's the magic? Enter the picture.  
**Translation:** 

**[3093.14s] English:** How does that happen? Yeah, so what ARM pioneered was a new business model.  
**Translation:** Vocabulary: pioneered: 开创

**[3096.68s] English:** They said, "Well, here's our proprietary instruction set, and we'll give you two ways to do it.  
**Translation:** 

**[3103.88s] English:** Either we'll give you...  
**Translation:** Vocabulary: proprietary: 专有技术

**[3105.14s] English:** We'll give you one of these implementations, written in something like C called Verilog, and you can just use ours.  
**Translation:** 

**[3111.46s] English:** Well, you have to pay money for that.  
**Translation:** Vocabulary: verilog: 硬件描述语言

**[3113.76s] English:** Not only will we give you their...  
**Translation:** 

**[3116.08s] English:** We'll license you to do that, or you could design your own.  
**Translation:** 

**[3120.00s] English:** So, we're talking about numbers like tens of millions of dollars to have the right to design your own since the instruction set belongs to them.  
**Translation:** 

**[3128.90s] English:** So, Apple got one of those: the right to build their own.  
**Translation:** 

**[3133.06s] English:** Most of the other companies that build phones like Android just get one of the ARM designs to do it themselves.  
**Translation:** 

**[3140.96s] English:** So, Apple developed a really good microprocessor design team.  
**Translation:** Vocabulary: microprocessor: 微处理器

**[3146.14s] English:** And they, you know, acquired a very good team that was building other microprocessors and brought them into the company to build their designs.  
**Translation:** 

**[3156.24s] English:** So, the instruction sets are the same.  
**Translation:** Vocabulary: microprocessors: 微处理器

**[3158.16s] English:** The specifications are the same.  
**Translation:** 

**[3159.60s] English:** But their hardware design is much more efficient than I think everybody else's.  
**Translation:** 

**[3164.84s] English:** And that's given Apple an advantage in the marketplace, as the iPhones tend to be faster than most everyone else's.  
**Translation:** 

**[3176.14s] English:** It would be nice to be able to jump around and kind of explore different little sides of this.  
**Translation:** Vocabulary: marketplace: 商品市场

**[3182.64s] English:** But let me ask one sort of romanticized question.  
**Translation:** 

**[3185.68s] English:** What is the most beautiful aspect or idea of the RISC instruction set or this work that you've done, in your opinion?  
**Translation:** 

**[3194.14s] English:** You know, I was always attracted to the idea of small being beautiful.  
**Translation:** 

**[3201.30s] English:** Is that the temptation in engineering?  
**Translation:** Vocabulary: temptation: 诱惑

**[3204.96s] English:** It's kind of easy.  
**Translation:** 

**[3206.14s] English:** To make things more complicated.  
**Translation:** 

**[3208.00s] English:** It's harder to come up with a simple, elegant solution. It's more difficult, surprisingly, to come up with one.  
**Translation:** 

**[3213.90s] English:** And I think that there are a bunch of small features of RISC in general that you can see where keeping it simpler makes it more elegant.  
**Translation:** Vocabulary: elegant: 优雅的

**[3225.62s] English:** Specifically in RISC-V, which I was kind of the mentor in the program, but it was really driven by Krista Osanovic and two grad students, Andrew Waterman and Yen-Sip Lee.  
**Translation:** 

**[3235.34s] English:** And I think that the most important thing about RISC-V is that they hit upon this idea of having.  
**Translation:** Vocabulary: mentor: 指导者; waterman: 沃特曼

**[3239.16s] English:** I think that the most important thing about RISC-V is that they hit upon this idea of having.  
**Translation:** 

**[3240.00s] English:** A subset of instructions, nice and simple, like 40-ish instructions, that  
**Translation:** 

**[3247.68s] English:** All software, including the software stack for RISC-V, can run just on those 40 instructions.  
**Translation:** 

**[3253.88s] English:** And then they provide optional features that could accelerate performance instructions.  
**Translation:** Vocabulary: accelerate: 加速; optional: 可选的

**[3260.56s] English:** That, if you needed them, could be very helpful, but you don't need to have them. And that's a new,  
**Translation:** 

**[3265.30s] English:** Really, a new idea. So RISC-V has right now maybe five optional subsets that you can pull in.  
**Translation:** 

**[3272.92s] English:** But the software runs without them. If you just want to build the core 40 instructions,  
**Translation:** 

**[3278.22s] English:** That's fine. You can do that. So, this is fantastic educationally: you can explain  
**Translation:** Vocabulary: educationally: 教育上地

**[3284.20s] English:** Computers: You only have to explain 40 instructions and not thousands of them. Also, if you invent,...  
**Translation:** 

**[3289.68s] English:** Some wild and crazy new technologies, like biological computing, you know.  
**Translation:** Vocabulary: computing: 计算

**[3295.30s] English:** You'd like a nice, simple instruction set. And you can have it with RISC-V, if you implement those cores.  
**Translation:** 

**[3301.48s] English:** Instructions: You can run some really interesting programs on top of that. So,this  
**Translation:** Vocabulary: implement: 实现

**[3305.64s] English:** The idea of a core set of instructions that the software stack runs on, and then optional features.  
**Translation:** 

**[3311.52s] English:** That if you turn them on, the compilers will use, but you don't have to—I think—is a powerful idea.  
**Translation:** Vocabulary: compilers: 编译器

**[3317.90s] English:** What has happened in the past with proprietary instruction sets is that when they add new instructions,  
**Translation:** 

**[3324.88s] English:** It becomes a required piece, and so all microprocessors in the future have to use those.  
**Translation:** Vocabulary: microprocessors: 微处理器; proprietary: 专有技术

**[3332.84s] English:** Instructions. So, it's kind of like: for a lot of people, as they get older, they gain weight.  
**Translation:** 

**[3337.58s] English:** Right? That weight and age are correlated. And so you can see these instructions getting.  
**Translation:** Vocabulary: correlated: 相关

**[3343.64s] English:** Bigger and bigger as they get older. So, RISC-V lets you be as slim as you are when you're young.  
**Translation:** 

**[3349.50s] English:** Teenager, and you only have to add these extra features if you're really going to use them.  
**Translation:** 

**[3353.84s] English:** Rather than every...  
**Translation:** 

**[3354.88s] English:** You have no choice; you have to keep growing with the instruction set.  
**Translation:** 

**[3358.30s] English:** I don't know if the analogy holds up, but that's...  
**Translation:** 

**[3360.00s] English:** Beautiful notion, uh, that there's almost like a nudge toward here's the simple core.  
**Translation:** Vocabulary: analogy: 类比; nudge: 暗示

**[3365.82s] English:** That's the essential, yeah. I think the surprising thing is still that, if we brought back...  
**Translation:** 

**[3372.12s] English:** The pioneers from the 1950s and showed them the instructions that they'd understand.  
**Translation:** Vocabulary: pioneers: 早期开拓者

**[3376.54s] English:** It: They'd say, "Wow, that doesn't look that different." Well, you know, I'm surprised, and it's there.  
**Translation:** 

**[3383.14s] English:** May be something you know to talk about philosophical things, I mean, there may be.  
**Translation:** Vocabulary: philosophical: 哲学的

**[3386.96s] English:** Something powerful about those—you know, around 40 or 50 instructions—that's all you need are these commands.  
**Translation:** 

**[3396.36s] English:** Like these instructions that we talked about, and that is sufficient to build or bring about.  
**Translation:** 

**[3402.48s] English:** You know, artificial intelligence, and so it's remarkably surprising to me that it's actually quite complicated.  
**Translation:** 

**[3411.36s] English:** As it is to build these things, uh, you know, a microprocessor.  
**Translation:** Vocabulary: microprocessor: 微处理器; remarkably: 非常

**[3416.96s] English:** Where the line widths are narrower than the wavelength of light, you know, is this amazing.  
**Translation:** 

**[3424.04s] English:** Technologies, at some fundamental level, the commands that software executes are really  
**Translation:** Vocabulary: executes: 运行; narrower: 更窄; wavelength: 波长; widths: 宽度

**[3429.10s] English:** Pretty straightforward, and haven't changed that much in decades, uh, which is a surprising thing.  
**Translation:** 

**[3434.84s] English:** Outcome: So, underlying all computation, all Turing machines, and all artificial intelligence systems.  
**Translation:** Vocabulary: computation: 计算; straightforward: 直截了当; turing: 图灵

**[3441.52s] English:** Perhaps there might be a very simple instruction set, like Risk 5, or it's yeah, I'm  
**Translation:** 

**[3446.94s] English:** I mean, I that's kind of what I said—I was interested to see, I had another more senior...  
**Translation:** 

**[3452.60s] English:** Faculty colleague, and he had written something in Scientific American and, you know, his 25 years.  
**Translation:** 

**[3459.92s] English:** In the future, he turned out to say that when I was a young professor, "Yep, I checked it.  
**Translation:** Vocabulary: colleague: 同行

**[3464.52s] English:** And so, I was interested to see how that was going to turn out for me, and it's pretty much held up, uh.  
**Translation:** 

**[3470.24s] English:** Pretty well, but yeah, so there's probably some, I mean, there must be.  
**Translation:** 

**[3476.94s] English:** Uh, those instructions that we're capable of.  
**Translation:** 

**[3480.00s] English:** Of creating intelligence from pretty primitive operations.  
**Translation:** 

**[3487.06s] English:** And just doing them really fast.  
**Translation:** 

**[3489.42s] English:** You kind of mentioned a different,  
**Translation:** 

**[3491.98s] English:** Maybe a radical computational medium like biological.  
**Translation:** 

**[3495.28s] English:** And there are other ideas.  
**Translation:** Vocabulary: computational: 计算的

**[3496.44s] English:** So, there are a lot of spaces in ASIC.  
**Translation:** 

**[3498.50s] English:** So, it's domain-specific.  
**Translation:** 

**[3500.58s] English:** And then there could be quantum computers.  
**Translation:** 

**[3502.10s] English:** And so, we can think of all of those different mediums.  
**Translation:** Vocabulary: mediums: 媒介; quantum: 量子

**[3505.76s] English:** And types of computation.  
**Translation:** 

**[3507.40s] English:** What's the connection between swapping out  
**Translation:** Vocabulary: swapping: 替换

**[3510.74s] English:** Different hardware systems in the instruction set?  
**Translation:** 

**[3514.72s] English:** Do you see those as disjoint?  
**Translation:** Vocabulary: disjoint: 不相连

**[3516.06s] English:** Or are they fundamentally coupled?  
**Translation:** 

**[3517.58s] English:** Yeah, so, if we go back to the history,  
**Translation:** Vocabulary: fundamentally: 从根本上

**[3523.80s] English:** When Moore's Law is in full effect,  
**Translation:** 

**[3525.44s] English:** And you're getting twice as many transistors.  
**Translation:** Vocabulary: transistors: 晶体管

**[3528.14s] English:** Every couple of years,  
**Translation:** 

**[3530.96s] English:** Kind of the challenge for computer designers.  
**Translation:** Vocabulary: designers: 设计师

**[3533.00s] English:** How can we take advantage of that?  
**Translation:** 

**[3534.54s] English:** How can we turn those transistors?  
**Translation:** 

**[3536.12s] English:** Into better computers?  
**Translation:** 

**[3537.38s] English:** We can't turn those computers faster, typically.  
**Translation:** 

**[3541.70s] English:** And so there was an era,  
**Translation:** 

**[3544.30s] English:** I guess in the 1980s and 1990s,  
**Translation:** 

**[3546.42s] English:** Where computers were doubling performance every 18 months.  
**Translation:** 

**[3552.02s] English:** And if you weren't around then,  
**Translation:** Vocabulary: doubling: 成倍增长

**[3554.16s] English:** What would happen is, you had your computer  
**Translation:** 

**[3558.52s] English:** And your friend's computer,  
**Translation:** 

**[3559.52s] English:** Which was like a year or a year-and-a-half newer.  
**Translation:** 

**[3561.82s] English:** And it was much faster than your computer.  
**Translation:** 

**[3564.02s] English:** And he or she could get their work done.  
**Translation:** 

**[3567.04s] English:** Their computers were perfectly good, but they threw them away to buy a newer computer because the  
**Translation:** 

**[3573.28s] English:** Computer, one or two years later, was so much faster. So, that's what the world was like in the '80s, and  
**Translation:** 

**[3579.14s] English:** In the 90s, it was common with the slowing down of Moore's Law, but that's no longer true right now.  
**Translation:** 

**[3586.20s] English:** Not with those desk-side computers with the laptops; I only get a new one when it breaks.  
**Translation:** 

**[3591.44s] English:** Right, oh, damn! The disc broke, or this display broke. I gotta buy a new computer, but before you...  
**Translation:** Vocabulary: laptops: 便携式电脑

**[3596.72s] English:** Would throw them away because it just was so  
**Translation:** 

**[3600.00s] English:** Sluggish compared to the latest computers. So that's, you know, a huge change from what's  
**Translation:** Vocabulary: sluggish: 反应慢

**[3609.06s] English:** Gone on. So, but since this lasted for decades, it affected both programmers and maybe all of society.  
**Translation:** 

**[3616.36s] English:** Is used to computers getting faster regularly. We now believe, those of us who are in computer.  
**Translation:** 

**[3623.40s] English:** Design, it's called computer architecture, that the path forward is instead to add accelerators.  
**Translation:** 

**[3630.32s] English:** That only works well for certain applications. So, since Moore's law is slowing down,  
**Translation:** 

**[3640.00s] English:** We don't think general-purpose computers are going to get a lot faster. So, the Intel  
**Translation:** 

**[3644.58s] English:** Processors of the world are not going to have been getting a lot faster. They've been  
**Translation:** Vocabulary: processors: 处理器

**[3649.30s] English:** Barely improving, like a few percent a year. It used to be,  
**Translation:** 

**[3652.62s] English:** Doubling every day.  
**Translation:** Vocabulary: doubling: 每天翻倍

**[3653.40s] English:** 18 months, and now it's doubling every 20 years. So it was just shocking. So, to be able to deliver,...  
**Translation:** 

**[3658.82s] English:** On what Moore's law used to do, we think what's going to happen, and what is happening right now, is  
**Translation:** 

**[3663.98s] English:** People are adding accelerators to their microprocessors that only work well for some domains.  
**Translation:** 

**[3671.94s] English:** And by sheer coincidence, at the same time that this is happening, there has been a revolution in  
**Translation:** Vocabulary: accelerators: 加速器; coincidence: 巧合; microprocessors: 微处理器

**[3678.72s] English:** Artificial intelligence, called machine learning. So,  
**Translation:** 

**[3682.14s] English:** With, as I'm sure your other guests have said, AI had these two competing schools of thought.  
**Translation:** 

**[3690.44s] English:** Thought is that we could figure out artificial intelligence by just writing the rules top-down.  
**Translation:** 

**[3695.36s] English:** Or that was wrong. You had to look at the data and infer what the rules are—the machine learning.  
**Translation:** 

**[3701.16s] English:** And what's happened in the last decade or eight years is that machine learning has won.  
**Translation:** 

**[3707.32s] English:** And it turns out that machine learning—the hardware you build for machine learning—  
**Translation:** 

**[3712.14s] English:** Is pretty much matrix multiplication. The matrix multiply is a key feature in how machine learning is done.  
**Translation:** 

**[3720.64s] English:** So, that's a godsend for computer designers.  
**Translation:** Vocabulary: designers: 设计师; godsend: 及时雨; matrix: 矩阵; multiplication: 乘法; multiply: 相乘

**[3724.10s] English:** We know how to make matrix multiplication run really fast.  
**Translation:** 

**[3727.68s] English:** So, general-purpose microprocessors are slowing down.  
**Translation:** 

**[3730.22s] English:** We're adding accelerators for machine learning.  
**Translation:** 

**[3732.08s] English:** That fundamentally are doing matrix multiplications.  
**Translation:** Vocabulary: fundamentally: 本质上; multiplications: 乘法运算

**[3734.88s] English:** Much more efficiently.  
**Translation:** 

**[3735.80s] English:** Than general-purpose computers have done.  
**Translation:** Vocabulary: efficiently: 高效地

**[3737.82s] English:** So, we have to come up with a new way to accelerate things.  
**Translation:** 

**[3741.58s] English:** The danger of only accelerating one application.  
**Translation:** Vocabulary: accelerate: 加快; accelerating: 加速

**[3743.66s] English:** Is how important is that application?  
**Translation:** 

**[3745.64s] English:** Turns out, machine learning gets used.  
**Translation:** 

**[3748.24s] English:** For all kinds of things.  
**Translation:** 

**[3749.44s] English:** So, serendipitously, we found something to accelerate.  
**Translation:** Vocabulary: serendipitously: 偶然地

**[3754.30s] English:** That's widely applicable.  
**Translation:** 

**[3757.22s] English:** And we don't even.  
**Translation:** 

**[3758.24s] English:** We're in the middle of this revolution in machine learning.  
**Translation:** 

**[3760.30s] English:** We're not sure what the limits of machine learning are.  
**Translation:** 

**[3762.66s] English:** So, this has been a kind of a godsend.  
**Translation:** 

**[3765.76s] English:** If you're going to be able to deliver,  
**Translation:** 

**[3768.58s] English:** On improved performance,  
**Translation:** 

**[3770.12s] English:** As long as people are moving their programs,...  
**Translation:** 

**[3773.86s] English:** To be embracing more machine learning,  
**Translation:** 

**[3776.30s] English:** We know how to give them more performance.  
**Translation:** Vocabulary: embracing: 接纳

**[3778.46s] English:** Even as more.  
**Translation:** 

**[3779.26s] English:** Of course, the law is slowing down.  
**Translation:** 

**[3780.58s] English:** And counterintuitively,  
**Translation:** 

**[3782.30s] English:** The machine learning mechanism,  
**Translation:** Vocabulary: counterintuitively: 出乎意料地

**[3785.54s] English:** You can say it is domain-specific.  
**Translation:** 

**[3787.36s] English:** But because it's leveraging data,  
**Translation:** Vocabulary: leveraging: 利用

**[3789.94s] English:** It's actually very broad.  
**Translation:** 

**[3792.54s] English:** In terms of the domains it could be applied in.  
**Translation:** 

**[3798.50s] English:** Yeah, that's exactly right.  
**Translation:** 

**[3799.80s] English:** Sort of, it's almost like,  
**Translation:** 

**[3801.94s] English:** People sometimes talk about the idea of Software 2.0.  
**Translation:** 

**[3805.08s] English:** We're almost taking another step up.  
**Translation:** 

**[3807.86s] English:** In the abstraction layer.  
**Translation:** 

**[3809.26s] English:** I mean, designing machine learning systems.  
**Translation:** Vocabulary: abstraction: 抽象

**[3812.44s] English:** Because now you're programming in the space of data.  
**Translation:** 

**[3815.38s] English:** In the space of hyperparameters.  
**Translation:** Vocabulary: hyperparameters: 超参数

**[3816.92s] English:** It's changing fundamentally the nature of programming.  
**Translation:** 

**[3820.38s] English:** And so, the specialized devices that accelerate performance,  
**Translation:** Vocabulary: fundamentally: 从根本上

**[3824.90s] English:** Especially neural network-based machine learning systems,  
**Translation:** 

**[3827.44s] English:** Might become the new general.  
**Translation:** Vocabulary: neural: 神经网络

**[3830.26s] English:** Yeah, so the thing that's interesting to point out is,  
**Translation:** 

**[3833.66s] English:** These are not tied together.  
**Translation:** 

**[3837.74s] English:** The enthusiasm,  
**Translation:** 

**[3839.26s] English:** The enthusiasm about machine learning,  
**Translation:** 

**[3840.00s] English:** Learning about creating programs driven by data, we should figure out the answers.  
**Translation:** 

**[3845.08s] English:** From data rather than a top-down approach, which is classically the way most programming is done.  
**Translation:** 

**[3850.04s] English:** Done, and the way artificial intelligence used to be done.  
**Translation:** 

**[3852.42s] English:** That's a movement that's going on at the same time.  
**Translation:** 

**[3856.10s] English:** Coincidentally, and the first word in machine learning is "machines," right?  
**Translation:** 

**[3860.24s] English:** So, that's going to increase the demand for computing because instead of programmers being  
**Translation:** Vocabulary: computing: 计算; programmers: 程序员

**[3866.36s] English:** Smart writing those things down, we're going to instead use computers to examine a lot.  
**Translation:** 

**[3871.10s] English:** Of data, we can kind of create the programs.  
**Translation:** 

**[3873.12s] English:** That's the idea.  
**Translation:** 

**[3875.48s] English:** And remarkably, this gets used for all kinds of things very successfully.  
**Translation:** Vocabulary: remarkably: 非常地

**[3879.76s] English:** The image recognition, the language translation, the game playing, and it gets into pieces.  
**Translation:** 

**[3887.22s] English:** Of the software stack, like databases and stuff like that.  
**Translation:** Vocabulary: databases: 数据库

**[3890.40s] English:** We're not quite sure how general-purpose it is, but that's going on independently of this.  
**Translation:** 

**[3893.96s] English:** Hardware stuff.  
**Translation:** Vocabulary: independently: 自主地

**[3895.00s] English:** What's happening on the hardware side?  
**Translation:** 

**[3896.36s] English:** It's Moore's law is slowing down right when we need a lot more cycles.  
**Translation:** 

**[3900.04s] English:** It's failing us right when we need it, because there's going to be a greater increase in  
**Translation:** 

**[3905.98s] English:** Computing.  
**Translation:** 

**[3907.02s] English:** And then there's this idea that we're going to do so-called domain-specific.  
**Translation:** 

**[3910.50s] English:** Here's a domain where your greatest fear is that you'll make this one thing work, and that'll  
**Translation:** 

**[3916.86s] English:** Help 5% of the people in the world.  
**Translation:** 

**[3919.72s] English:** Well, this looks like it's a very general-purpose thing.  
**Translation:** 

**[3922.98s] English:** So, the timing is fortuitous.  
**Translation:** 

**[3925.04s] English:** That, if we can,...  
**Translation:** Vocabulary: fortuitous: 侥幸的; timing: 时机

**[3926.36s] English:** Perhaps, if we can keep building hardware that will accelerate machine learning, the  
**Translation:** 

**[3932.32s] English:** Neural networks that will beat the timing will be right.  
**Translation:** Vocabulary: accelerate: 加速; neural: 神经网络

**[3936.60s] English:** That neural network revolution will transform software—the so-called Software 2.0.  
**Translation:** 

**[3943.38s] English:** And the software of the future will be very different from the software of the past.  
**Translation:** 

**[3947.28s] English:** And just as our microprocessors, even though we're still going to have that same basic  
**Translation:** 

**[3951.60s] English:** Risk instructions to run big pieces of the software stack, like user interfaces.  
**Translation:** Vocabulary: interfaces: 人机界面; microprocessors: 微处理器

**[3956.36s] English:** And stuff like that, we can accelerate the...  
**Translation:** 

**[3960.00s] English:** Kind of a small piece that's computationally intensive. It's not lots of lines of code.  
**Translation:** Vocabulary: computationally: 计算上

**[3964.04s] English:** But it takes a lot of cycles to run that code—that's going to be the accelerator piece.  
**Translation:** 

**[3969.12s] English:** So, that's what makes this, from a computer designer's perspective, really interesting.  
**Translation:** Vocabulary: accelerator: 加速器

**[3975.26s] English:** Decade. What Hennessy and I talked about in the title of our Turing-Warn speech is a new golden  
**Translation:** 

**[3981.34s] English:** Age. We see this as a very exciting decade, much like when we were assistant professors and the  
**Translation:** Vocabulary: hennessy: 汉尼西

**[3989.62s] English:** RIS stuff was going on. That was a very exciting time. It was where we were changing what was  
**Translation:** 

**[3993.02s] English:** Going on, we see this happening again. Tremendous opportunities for people because we're fundamentally  
**Translation:** Vocabulary: fundamentally: 从根本上

**[3999.90s] English:** Changing how software is built and how we are running it.  
**Translation:** 

**[4002.90s] English:** So, which layer of the abstraction do you think most of the acceleration might be happening?  
**Translation:** Vocabulary: abstraction: 抽象; acceleration: 加速

**[4007.92s] English:** If you look ahead over the next 10 years, Google is working on a lot of exciting stuff with the TPU.  
**Translation:** 

**[4013.58s] English:** There's something closer to the hardware. There could be optimizations around.  
**Translation:** Vocabulary: optimizations: 优化

**[4017.26s] English:** The...  
**Translation:** 

**[4017.82s] English:** A lot closer to the instruction set. There could be optimization at the compiler level. It could  
**Translation:** Vocabulary: optimization: 优化

**[4023.20s] English:** Be even at the higher-level software stack.  
**Translation:** 

**[4026.28s] English:** Yeah, it's going to be... If you think about the old RIS-SYS debate, it was software vs. hardware.  
**Translation:** 

**[4033.22s] English:** Was the compiler improving, as well as the architecture? And that's likely.  
**Translation:** 

**[4039.50s] English:** To be the way things are now, with machine learning, they're using domain-specific languages.  
**Translation:** 

**[4046.32s] English:** The languages, like,...  
**Translation:** 

**[4048.22s] English:** TensorFlow and PyTorch are very popular among machine learning practitioners. Those are...  
**Translation:** Vocabulary: practitioners: 从业者

**[4054.06s] English:** Raising the level of abstraction, it's easier for people to write machine learning code in these.  
**Translation:** 

**[4058.62s] English:** Domain-specific languages like PyTorch and TensorFlow.  
**Translation:** 

**[4063.82s] English:** So, where most of the optimization might be happening?  
**Translation:** 

**[4065.82s] English:** Yeah. And so there will be both the compiler piece and the hardware piece underneath it. So, as you...  
**Translation:** Vocabulary: underneath: 在...下面

**[4072.38s] English:** Kind of the fatal flaw for hardware people is to create really great hardware, but not have the software to match.  
**Translation:** 

**[4077.82s] English:** Best of them, and I think that brought along the compilers, and what we're...  
**Translation:** 

**[4080.00s] English:** Seeing right now in the marketplace, because of this enthusiasm around hardware for machine learning,  
**Translation:** 

**[4085.30s] English:** Learning is getting, you know, probably billions of dollars invested in startup companies. We're  
**Translation:** Vocabulary: marketplace: 商品市场

**[4091.14s] English:** Seeing startup companies go belly up because they focused on the hardware but didn't bring  
**Translation:** 

**[4096.52s] English:** The software stack along. We talked about benchmarks earlier. So, I participated in  
**Translation:** Vocabulary: benchmarks: 参考标准

**[4103.38s] English:** Machine learning didn't really have a set of benchmarks. I think just two years ago,  
**Translation:** 

**[4107.44s] English:** They didn't have a set of benchmarks. And we've created something called MLPerf, which is  
**Translation:** 

**[4111.64s] English:** Machine Learning Benchmark Suite. And pretty much the companies who didn't invest in the software,...  
**Translation:** 

**[4118.34s] English:** Stack couldn't run MLPerf very well. And the ones who did invest in the software stack did. And we're  
**Translation:** Vocabulary: benchmark: 衡量标准

**[4124.08s] English:** Seeing, you know, like kind of in computer architecture, this is what happens: you have  
**Translation:** 

**[4127.48s] English:** These arguments about risk versus risk. People spend billions of dollars in the marketplace to.  
**Translation:** 

**[4131.56s] English:** See who wins. And it's not a perfect comparison, but it kind of sorts things out. And we're seeing...  
**Translation:** 

**[4137.04s] English:** Companies that are doing it, and we're seeing them do it.  
**Translation:** 

**[4137.42s] English:** Companies that are doing it, and we're seeing them do it.  
**Translation:** 

**[4137.44s] English:** Go out of business. And then, there's a company in Israel called Habana.  
**Translation:** Vocabulary: habana: 海巴纳公司

**[4144.60s] English:** They came up with machine learning accelerators. They had good MLPerf scores. Intel had acquired...  
**Translation:** 

**[4152.16s] English:** A company previously called Nirvana a couple of years ago did not reveal their MLPerf scores.  
**Translation:** Vocabulary: accelerators: 加速器; nirvana: 涅槃

**[4157.40s] English:** Which was suspicious. But a month ago, Intel announced that they are canceling the Nirvana.  
**Translation:** 

**[4163.10s] English:** Product line. And they bought Habana for $2 billion. And they're canceling the Nirvana.  
**Translation:** Vocabulary: canceling: 取消; suspicious: 可疑

**[4167.42s] English:** Intel is going to be shipping Habana chips, which have hardware and software and run the MLPerf.  
**Translation:** 

**[4173.38s] English:** Programs pretty well, and that's going to be their product line of the future.  
**Translation:** 

**[4177.14s] English:** Brilliant. So, maybe just to linger briefly on MLPerf. I love metrics. I love standards that  
**Translation:** 

**[4182.70s] English:** Everyone can gather around. What are some interesting aspects of that portfolio of metrics?  
**Translation:** Vocabulary: linger: 停留; metrics: 指标; portfolio: 组合

**[4188.98s] English:** Well, one of the interesting metrics is what we thought it was, you know, we,  
**Translation:** 

**[4194.12s] English:** I was involved in the start. You know, we,  
**Translation:** 

**[4196.98s] English:** Peter Mattson is leading the effort from Google. Google,  
**Translation:** 

**[4200.00s] English:** Got it off the ground, but we had to reach out to competitors and say, "There's no benchmarks here.  
**Translation:** Vocabulary: benchmarks: 衡量标准

**[4206.32s] English:** This, we think, is bad for the field. It would be much better if we looked at examples like in the  
**Translation:** 

**[4210.56s] English:** Risk days, there was an effort to create something for the people in the risk community who got together.  
**Translation:** 

**[4216.10s] English:** Competitors got together; we're building risk microprocessors to agree on a set of benchmarks.  
**Translation:** 

**[4220.16s] English:** That were called Spec, and that was good for the industry, is rather before the different risks.  
**Translation:** 

**[4225.68s] English:** Architectures were arguing; well, you can believe my performance, others, but those other guys are...  
**Translation:** 

**[4229.26s] English:** Liars, and that didn't do any good. So, we agreed on a set of benchmarks, and then we could figure out  
**Translation:** 

**[4235.56s] English:** Who was faster between the various risk architectures, but it was a little bit faster.  
**Translation:** 

**[4239.16s] English:** But that grew the market, rather than people being afraid to buy anything, so we argued.  
**Translation:** 

**[4243.82s] English:** The same thing would happen with ML Perf, you know, companies like NVIDIA were, you know,  
**Translation:** 

**[4248.70s] English:** Worried that it was some kind of trap, but eventually we all got together to create a  
**Translation:** 

**[4253.28s] English:** A set of benchmarks, and do the right thing right. And we agree on the results, and so we can.  
**Translation:** 

**[4259.24s] English:** See whether TPUs, GPUs, or CPUs are really faster and how much faster, and I think from  
**Translation:** 

**[4266.04s] English:** An engineer's perspective: as long as the results are fair, you can live with it, okay?  
**Translation:** 

**[4271.58s] English:** You kind of tip your hat to your colleagues at another institution; they did a better job.  
**Translation:** Vocabulary: colleagues: 同行同事

**[4276.54s] English:** Than us, what you hate is if it's false, right? They're making claims, and it's just  
**Translation:** 

**[4281.02s] English:** Marketing bullshit, and you know, is affecting sales, so you, from an engineer's  
**Translation:** Vocabulary: bullshit: 胡说八道

**[4285.46s] English:** Perspective: As long as it's a fair comparison, and we don't come in first place, they're going to...  
**Translation:** 

**[4289.24s] English:** Say, "That's too bad, but it's fair." So, we wanted to create that environment for ML Perf, and so now,...  
**Translation:** 

**[4294.92s] English:** Uh, there are 10 universities I mean, 10 companies and 50 companies involved, so pretty much ML Perf has...  
**Translation:** 

**[4303.96s] English:** Is this the way you measure machine learning performance? Um, and it didn't exist even two...  
**Translation:** 

**[4310.76s] English:** Years ago, one of the cool things I enjoy about the Internet has a few downsides, but  
**Translation:** 

**[4316.44s] English:** One of the nice things is that people can see.  
**Translation:** Vocabulary: downsides: 缺点

**[4319.24s] English:** See through.  
**Translation:** 

**[4320.00s] English:** A little better with the presence of these kinds of metrics; it's really nice. Companies like...  
**Translation:** Vocabulary: metrics: 指标

**[4325.40s] English:** Google, Facebook, and Twitter—now it's the cool thing to do—is to put your engineers forward.  
**Translation:** 

**[4331.10s] English:** To actually show off how well you do on these metrics, there's not really a sort of... well, there's  
**Translation:** 

**[4337.68s] English:** Less of a desire to do marketing; less so, I am. Am I sort of naive? No, I think what I was trying to say was...  
**Translation:** 

**[4344.38s] English:** Understand that you know what's changed from the '80s in this era, I think, because of things like  
**Translation:** Vocabulary: naive: 幼稚

**[4349.58s] English:** Social networking, Twitter, and stuff like that—if you put up, you know, bullshit stuff.  
**Translation:** 

**[4355.62s] English:** Right, that's just you know, purposely misleading you to think that you can get a  
**Translation:** Vocabulary: misleading: 误导; purposely: 故意

**[4361.60s] English:** Violent reaction on social media, pointing out the flaws in your arguments, right? And so from a  
**Translation:** 

**[4368.10s] English:** From a marketing perspective, you have to be careful today that you didn't have to be as careful in the past.  
**Translation:** 

**[4374.38s] English:** Be people who put out the word about the flaws, and you can get the message out about what you're saying.  
**Translation:** 

**[4379.58s] English:** Much more easily today than in the past, you used to say it was easier to get away with it.  
**Translation:** 

**[4384.36s] English:** And the other thing that's been happening in terms of serving off engineers is just  
**Translation:** 

**[4389.18s] English:** In the software side, people have largely embraced open-source software; it was 20 years ago that this began to happen.  
**Translation:** Vocabulary: embraced: 接受

**[4398.20s] English:** A dirty word at Microsoft, and today, Microsoft is one of the big proponents of open-source software.  
**Translation:** 

**[4403.24s] English:** Kind of, that's the standard way most software gets built, which really shows off your engineers.  
**Translation:** Vocabulary: proponents: 支持者

**[4409.58s] English:** You can see, if you look at the source code, that you can see who is making the commits and who's making.  
**Translation:** 

**[4415.30s] English:** The improvements? Who are the engineers at all these companies who are, you know, really  
**Translation:** Vocabulary: commits: 提交的代码

**[4421.82s] English:** Uh, great; uh, programmers and engineers are making really solid contributions, which enhances their  
**Translation:** 

**[4428.02s] English:** Reputations and the reputation of the companies, so, but that's of course not everywhere like in.  
**Translation:** Vocabulary: enhances: 提升; programmers: 程序员; reputations: 声誉

**[4433.12s] English:** The space I work more in is autonomous vehicles, and they're still considered machinery.  
**Translation:** 

**[4439.58s] English:** Of hype.  
**Translation:** Vocabulary: autonomous: 自主; machinery: 机械

**[4440.00s] English:** Marketing is still very strong there, and there's less willingness to be open in this kind of open.  
**Translation:** 

**[4445.20s] English:** Source, way, and sort of benchmark; so ML Perf represents the machine learning world is much.  
**Translation:** Vocabulary: benchmark: 参考标准

**[4450.82s] English:** Better being open-source about holding itself to standards of different amounts of incredible.  
**Translation:** 

**[4456.14s] English:** Benchmarks in terms of the different computer vision and natural language processing tasks, is  
**Translation:** Vocabulary: benchmarks: 衡量标准

**[4462.60s] English:** Incredible, you know, historically it wasn't always that way. Um, I had a graduate student.  
**Translation:** 

**[4468.26s] English:** Working with me, David Martin, so far in computer science, benchmarking has been around forever.  
**Translation:** Vocabulary: benchmarking: 性能测试; historically: 历史上

**[4474.68s] English:** So, uh, computer architecture, databases, uh, maybe operating systems, uh, benchmarks are  
**Translation:** 

**[4483.14s] English:** Uh, the way you measure progress, but uh, he was working with me, and then started working with...  
**Translation:** Vocabulary: databases: 数据库

**[4488.78s] English:** Jitendra Malik, and he's from the computer vision space. I guess you've  
**Translation:** 

**[4493.72s] English:** Interviewed Jandra and uh, David Martin told me they don't have.  
**Translation:** Vocabulary: jitendra: 吉特伦达; malik: 马利克

**[4498.24s] English:** Benchmarks. Everybody has their own vision algorithm, and the way that mine looks, here's my image.  
**Translation:** 

**[4503.14s] English:** Look at how well I do. And everyone had their own image. So, David Martin, back when he did his  
**Translation:** Vocabulary: algorithm: 计算方法

**[4509.08s] English:** Dissertation, he figured out a way to do benchmarks. He had a bunch of graduate students identify  
**Translation:** 

**[4514.08s] English:** Images, and then we ran benchmarks to see which algorithms ran well. And that was, as far as I  
**Translation:** Vocabulary: dissertation: 论文

**[4519.58s] English:** Know, kind of the first time people did benchmarks in computer vision, and which was predicated on all,  
**Translation:** 

**[4526.76s] English:** You know, the things that eventually led to ImageNet and stuff like that. But then, you know,  
**Translation:** Vocabulary: predicated: 基于

**[4530.08s] English:** The vision community got religion. And then, once we got as far as ImageNet, that really let the guys  
**Translation:** 

**[4537.50s] English:** In Toronto, they were able to win the ImageNet competition. And then, you know, that changed the whole world.  
**Translation:** Vocabulary: toronto: 多伦多

**[4543.92s] English:** It's a scary step, actually, because when you enter the world of benchmarks, you actually have  
**Translation:** 

**[4548.68s] English:** To be good at participating, as opposed to, yeah, you just believe you're the best.  
**Translation:** Vocabulary: benchmarks: 评价标准

**[4555.10s] English:** In the world.  
**Translation:** 

**[4556.76s] English:** Yeah. And I think the people weren't purposely.  
**Translation:** Vocabulary: purposely: 故意地

**[4560.00s] English:** Misleading, I think. If you don't have benchmarks, I mean, how do you know? You could have...  
**Translation:** 

**[4565.08s] English:** Your intuition is kind of like the way we used to do computer architecture: your intuition is that...  
**Translation:** Vocabulary: intuition: 直觉; misleading: 误导

**[4569.86s] English:** This is the right instruction set to do this job, I believe. In my experience, my hunch is that's true.  
**Translation:** 

**[4575.76s] English:** We had to get things more quantitative, uh, to make progress, and so I just don't know how.  
**Translation:** Vocabulary: hunch: 直觉; quantitative: 量化

**[4583.52s] English:** You know, in fields that don't have benchmarks, I don't understand how they figure out how they're doing.  
**Translation:** 

**[4587.96s] English:** Making progress, we're kind of in the "vacuum tube" days of quantum computing. What are your thoughts?  
**Translation:** Vocabulary: computing: 计算; quantum: 量子; vacuum: 真空

**[4595.30s] English:** In this wholly different kind of space of architectures, uh, you know, I actually, you know,  
**Translation:** 

**[4600.94s] English:** Quantum computing, uh, is an idea that has been around for a while, and I actually thought, "Well, I sure hope...  
**Translation:** 

**[4605.70s] English:** Uh, I retired before I had to start teaching this. I'd say because I talk about giving these talks.  
**Translation:** 

**[4613.22s] English:** About the slowing of Morse Law, and, you know, when we need to.  
**Translation:** Vocabulary: morse: 莫尔斯电码

**[4617.64s] English:** Uh  
**Translation:** 

**[4617.96s] English:** Change by doing domain-specific accelerators, uh, common questions: say, what about quantum?  
**Translation:** 

**[4622.80s] English:** Computing the reason that comes up; it's in the news all the time, so I think it's important to keep it hard.  
**Translation:** 

**[4627.78s] English:** A thing to keep in mind is that quantum computing is not right around the corner; there have been  
**Translation:** 

**[4632.52s] English:** Two national reports: one by the National Center for Engineering Education, another by the Computing Consortium.  
**Translation:** 

**[4637.84s] English:** Where they did a frank assessment of quantum computing, and uh, both of those reports said you  
**Translation:** Vocabulary: consortium: 联盟

**[4645.00s] English:** Know, as far as we can tell, before you get  
**Translation:** 

**[4647.64s] English:** Error corrected quantum computing is a decade away, so I think of it like nuclear fusion, right?  
**Translation:** Vocabulary: fusion: 核聚变

**[4653.58s] English:** There have been people who've been excited about nuclear fusion for a long time. If we ever get it to work,  
**Translation:** 

**[4657.66s] English:** Fusion is going to be fantastic for the world. I'm glad people are working on it, but you know.  
**Translation:** 

**[4662.52s] English:** It's not right around the corner, though. Those two reports suggest that it will probably be 2030 before.  
**Translation:** 

**[4669.58s] English:** Quantum computing is something that could happen, and when it does happen, you know, this is.  
**Translation:** Vocabulary: computing: 计算; quantum: 量子

**[4676.44s] English:** Going to be big science.  
**Translation:** 

**[4677.52s] English:** This stuff, you know, is micro.  
**Translation:** 

**[4680.00s] English:** Kelvin: Almost absolute zero—things that, if they vibrate or if a truck goes by, won't work, right?  
**Translation:** 

**[4685.84s] English:** So, this will be in data center stuff. We're not going to have a quantum cellphone. And it's  
**Translation:** Vocabulary: kelvin: 开尔文; vibrate: 振动

**[4691.68s] English:** Probably a 2030 kind of thing. So I'm happy that other people are working on it, but just,...  
**Translation:** 

**[4697.02s] English:** You know, it's hard with all the news about it not to think that it's right around the corner.  
**Translation:** 

**[4702.54s] English:** And that's why we need to do something as Moore's law is slowing down, to provide the  
**Translation:** 

**[4706.90s] English:** Computing, keep computing getting better for this next decade. And, you know, we shouldn't.  
**Translation:** 

**[4712.68s] English:** Be betting on quantum computing, or expecting it to deliver in the next few years?  
**Translation:** 

**[4719.74s] English:** Years. It's probably further off. You know, I'd be happy to be wrong. It'd be great if quantum...  
**Translation:** 

**[4724.60s] English:** Computing is going to be commercially viable, but it will be a set of applications. It's not a general  
**Translation:** 

**[4729.58s] English:** Purpose computation. So it's going to do some amazing things, but there will be a lot of things  
**Translation:** Vocabulary: commercially: 商业上; computation: 计算; viable: 可行的

**[4734.72s] English:** That probably, you know, the,  
**Translation:** 

**[4736.90s] English:** The old-fashioned computers are going to keep doing better for quite a while.  
**Translation:** 

**[4740.94s] English:** And there will be a teenager 50 years from now watching this video saying,  
**Translation:** 

**[4744.88s] English:** Look how silly David Patterson was saying.  
**Translation:** 

**[4748.02s] English:** No, I just said I said 2030. I didn't say I didn't say never.  
**Translation:** 

**[4752.16s] English:** We're not going to have quantum cell phones. So, he's going to be watching it on a regular cell phone.  
**Translation:** Vocabulary: quantum: 量子

**[4755.62s] English:** Well, I mean, I think this is such a significant development, given that we've had Moore's Law, I just  
**Translation:** 

**[4761.08s] English:** I feel comfortable trying to do projects that are thinking about the next decade.  
**Translation:** 

**[4766.90s] English:** I admire people who are trying to do things that are 30 years out, but  
**Translation:** 

**[4769.70s] English:** It's such a fast-moving field. Ugh, I just don't know how to; I'm not good enough to figure it out.  
**Translation:** 

**[4776.46s] English:** What will the problem be in 30 years? Ugh, you know, 10 years is hard enough for...  
**Translation:** 

**[4780.66s] English:** So, maybe if it's possible to untangle your intuition a little bit, I spoke with Jim Keller.  
**Translation:** Vocabulary: intuition: 直觉; untangle: 理清

**[4786.30s] English:** I don't know if you're familiar with Jim. He's trying to sort of, uh,...  
**Translation:** 

**[4791.60s] English:** Be a little bit rebellious and to try to think that, um, he quotes me as being,  
**Translation:** Vocabulary: quotes: 引用; rebellious: 叛逆

**[4796.10s] English:** Wrong. Yeah. So, this is what you're asking for, by the way.  
**Translation:** 

**[4800.00s] English:** For the record, Jim talks about his intuition that Moore's law is not, in fact, dead yet, and that it may continue for some time to come.  
**Translation:** 

**[4811.86s] English:** What are your thoughts about Jim's ideas in this space?  
**Translation:** 

**[4814.86s] English:** Yeah, this is just marketing.  
**Translation:** 

**[4817.38s] English:** So, what Gordon Moore said is a quantitative prediction.  
**Translation:** 

**[4821.58s] English:** We can check the facts, right? Which is doubling the number of transistors every two years.  
**Translation:** Vocabulary: doubling: 翻倍; quantitative: 量化的; transistors: 晶体管

**[4827.30s] English:** So we can look back at Intel for the last five years and ask: Let's look at DRAM chips six years ago.  
**Translation:** 

**[4836.42s] English:** So that would be three two-year periods.  
**Translation:** 

**[4839.78s] English:** So, then, our DRAM chips have eight times as many transistors as they did six years ago.  
**Translation:** 

**[4845.68s] English:** We can look up Intel microprocessors from six years ago.  
**Translation:** Vocabulary: microprocessors: 微处理器

**[4849.64s] English:** If Moore's law continues, it should have eight times as many transistors as six years ago.  
**Translation:** 

**[4856.38s] English:** The answer?  
**Translation:** 

**[4857.34s] English:** In both those cases, it's no.  
**Translation:** 

**[4859.20s] English:** The problem has been because Moore's law was kind of genuinely embraced by the semiconductor industry, as they would make investments in similar equipment to make Moore's law come true.  
**Translation:** 

**[4873.86s] English:** Semiconductors improving and Moore's law are often considered the same thing.  
**Translation:** 

**[4879.40s] English:** So, when I say, and I'm factually correct, that Moore's law is no longer holding, we are not doubling the transistors.  
**Translation:** 

**[4887.30s] English:** The downside for a company like Intel is that people think it means the company has stopped, and that technology has no longer improved.  
**Translation:** 

**[4898.04s] English:** And so, Jim is trying to counteract the impression that semiconductors are frozen in 2019 and will never get better.  
**Translation:** Vocabulary: counteract: 抵消; downside: 不利方面; semiconductors: 半导体

**[4911.24s] English:** So, I never said that.  
**Translation:** 

**[4912.84s] English:** All I said was, "Moore's law is no more.  
**Translation:** 

**[4916.68s] English:** And I am.  
**Translation:** 

**[4917.30s] English:** Strictly looking at the number of transistors.  
**Translation:** Vocabulary: strictly: 严格地; transistors: 晶体管

**[4919.34s] English:** Because that's what.  
**Translation:** 

**[4920.00s] English:** Moore's law is. There's been an aura associated with Moore's law, that  
**Translation:** 

**[4928.04s] English:** They've enjoyed it for 50 years, about. Look at the field we're in. We're doubling transistors every  
**Translation:** 

**[4933.90s] English:** Two years. What an amazing field! It's an amazing thing that they were able to pull it off.  
**Translation:** Vocabulary: doubling: 翻倍

**[4938.08s] English:** But, even as Gordon Moore said, "you know, no exponential can last forever." It lasted for 50 years.  
**Translation:** 

**[4942.58s] English:** Years, which is amazing, and this has had a huge impact on the industry because of these changes that.  
**Translation:** Vocabulary: exponential: 指数的

**[4948.16s] English:** We've been talking about it. So he claims, because he's trying to act, he says, "you know, Patterson.  
**Translation:** 

**[4954.30s] English:** Says, "Moore's law is no more." And look at that; it's still going. And TSMC, they say,...  
**Translation:** 

**[4960.62s] English:** It's no longer true, but there's quantitative evidence that Moore's law is not continuing. So what I say,...  
**Translation:** 

**[4966.28s] English:** Now, to try and clarify, okay, I understand the perception problem when I say Moore's law stopped. Okay. So  
**Translation:** Vocabulary: clarify: 澄清; perception: 认知; quantitative: 定量的

**[4973.84s] English:** Now, I say Moore's law is slowing down. And I think, Jim,...  
**Translation:** 

**[4978.16s] English:** Which is another way of saying that, if he's predicting every two years, and I say it's  
**Translation:** 

**[4982.36s] English:** Slowing down, then that's another way of saying it doesn't hold anymore. And, and I think Jim.  
**Translation:** 

**[4986.94s] English:** Wouldn't disagree that it's slowing down because that sounds like things are still getting  
**Translation:** 

**[4993.24s] English:** Better, just not as fast, which is another way of saying Moore's law isn't working anymore.  
**Translation:** 

**[4998.62s] English:** It's still good for marketing, but, but what's your opinion? You're not interested in expanding the market, are you?  
**Translation:** 

**[5004.12s] English:** Definition of Moore's Law, sort of, naturally.  
**Translation:** 

**[5008.16s] English:** The educator, you know, is this like modern politics? Does everybody get their  
**Translation:** Vocabulary: educator: 教育者

**[5013.14s] English:** Own facts? Or do we have, you know, Moore's law was a crisp, you know, a more formal statement, it was Carver Mead.  
**Translation:** 

**[5020.36s] English:** Looked at his observation, Moore's observations, a drawing on a log, log scale, a straight line.  
**Translation:** Vocabulary: carver: 雕刻家

**[5025.98s] English:** And that's what Moore's law is. There's another thing Intel did for a while,  
**Translation:** 

**[5031.92s] English:** Interestingly, before Jim joined them, they said, "Oh, no; Moore's law isn't the number of doublings.  
**Translation:** Vocabulary: doublings: 倍增

**[5037.08s] English:** Isn't really,  
**Translation:** 

**[5038.16s] English:** Doubling transistors every two years.  
**Translation:** Vocabulary: doubling: 翻倍; transistors: 晶体管

**[5040.00s] English:** Moore's law is that the cost of an individual transistor goes down, cutting in half every two years.  
**Translation:** 

**[5048.02s] English:** Now, that's not what he said, but they reinterpreted it because they believed that the cost of transistors was continuing to drop, even if they couldn't get twice as many chips.  
**Translation:** Vocabulary: reinterpreted: 重新解释; transistor: 晶体管

**[5058.50s] English:** Many people in industry have told me that's not true anymore: that, in more recent and more complicated technologies, the actual cost of a transistor has gone up.  
**Translation:** 

**[5067.56s] English:** So, even a corollary might not be true, but certainly, you know, Moore's law—that was the beauty of Moore's law.  
**Translation:** Vocabulary: corollary: 推论

**[5077.18s] English:** It was a very simple idea, like E = mc², right?  
**Translation:** 

**[5080.56s] English:** It was like, "Wow, what an amazing prediction!  
**Translation:** 

**[5083.54s] English:** It's so easy to understand.  
**Translation:** 

**[5084.96s] English:** The implications are amazing.  
**Translation:** Vocabulary: implications: 暗示意义

**[5086.50s] English:** And that's why it was so famous as a prediction.  
**Translation:** 

**[5090.10s] English:** And this reinterpretation of what it meant and changing is, you know, is revisionist history.  
**Translation:** Vocabulary: reinterpretation: 重新解释; revisionist: 修正主义者

**[5096.14s] English:** And I agree.  
**Translation:** 

**[5098.00s] English:** I'd be happy.  
**Translation:** 

**[5100.28s] English:** And they're not claiming there's a new Moore's Law.  
**Translation:** 

**[5102.80s] English:** They're not saying, by the way; it's every three years, instead of every two years.  
**Translation:** 

**[5108.44s] English:** I don't think they want to say that.  
**Translation:** 

**[5111.08s] English:** I think what's going to happen is that each new technology generation is going to get a little bit slower.  
**Translation:** 

**[5115.62s] English:** So, it is slowing down.  
**Translation:** 

**[5118.66s] English:** The improvements won't be as great.  
**Translation:** 

**[5121.12s] English:** And that's why we need to do new things.  
**Translation:** 

**[5122.92s] English:** Yeah, I don't like how the idea of Moore's law is tied up with marketing.  
**Translation:** 

**[5127.80s] English:** It would be nice if...  
**Translation:** 

**[5129.92s] English:** Whether it's marketing or it's...  
**Translation:** 

**[5132.10s] English:** Well, it could be affecting business, but it could also be infecting the imagination of engineers.  
**Translation:** 

**[5138.14s] English:** If Intel employees actually believe that we're frozen in 2019, well, that would be bad for Intel.  
**Translation:** Vocabulary: infecting: 感染

**[5146.22s] English:** Not just Intel, but everybody.  
**Translation:** 

**[5148.94s] English:** Moore's law is inspiring to everyone.  
**Translation:** 

**[5152.66s] English:** But what's happening right now is that we're talking to people in...  
**Translation:** 

**[5156.66s] English:** Who are working in national offices.  
**Translation:** 

**[5159.56s] English:** And...  
**Translation:** 

**[5160.00s] English:** Stuff like that, a lot of the computer science community is unaware that this is going on, right?  
**Translation:** 

**[5165.22s] English:** That we are in an era that's going to need radical change, even at lower levels, that could affect the whole.  
**Translation:** 

**[5170.76s] English:** Software stack: This, um, you know, if Intel, if you're using cloud stuff and the servers that,...  
**Translation:** 

**[5179.62s] English:** You'll get next year's servers that are basically only a little bit faster than the servers you have this year.  
**Translation:** 

**[5183.32s] English:** You need to know that, and we need to start innovating to start delivering on it if.  
**Translation:** Vocabulary: innovating: 创新

**[5190.14s] English:** You're counting on your software; it's going to get a lot more features, assuming the  
**Translation:** 

**[5193.90s] English:** Computers can get faster—that's not true. So, are you going to have to start making your software more efficient?  
**Translation:** 

**[5197.72s] English:** Stacks more efficient, are you going to have to start learning about machine learning? So it's  
**Translation:** 

**[5201.84s] English:** You know, it's kind of a warning or call for arms that the world is changing right now.  
**Translation:** Vocabulary: stacks: 堆积起来的牌

**[5207.78s] English:** And a lot of people, including many Computer Science PhDs, are unaware of that, so a way to  
**Translation:** 

**[5213.24s] English:** Transform the world is to start innovating and to start delivering on it, so it's kind of  
**Translation:** 

**[5213.32s] English:** Get their attention is to say that Morse Law is slowing down, and that's going to affect your.  
**Translation:** 

**[5218.48s] English:** Assumptions, and, you know, we're trying to get the word out, and when companies like TSMC  
**Translation:** Vocabulary: assumptions: 假设

**[5223.18s] English:** And Intel say, "Oh, no, no, no, Morse Law is fine." Then people think, "Okay, I don't have to change my.  
**Translation:** 

**[5228.96s] English:** Behavior: I'll just get the next servers, and you know, if they start doing measurements, they'll...  
**Translation:** Vocabulary: morse: 莫尔斯电码

**[5233.90s] English:** Realize what's going on, it would be nice to have some transparency and metrics for the layperson.  
**Translation:** 

**[5239.24s] English:** To be able to know if computers are getting faster,  
**Translation:** Vocabulary: layperson: 普通人士; metrics: 衡量标准

**[5243.24s] English:** Yeah, there are a bunch of most people kind of use clock rate as a measure of.  
**Translation:** 

**[5251.18s] English:** Performance, you know, it's not a perfect one, but if you've noticed, clock rates are more or less the  
**Translation:** 

**[5255.80s] English:** Same as they were five years ago, computers are a little better, but they haven't made  
**Translation:** 

**[5262.42s] English:** Zero progress, but they've made some small progress, so there are some indications out there.  
**Translation:** Vocabulary: indications: 迹象

**[5266.68s] English:** Our behavior, right? Nobody buys the next laptop because it's so much faster than the laptop from  
**Translation:** 

**[5272.38s] English:** The past.  
**Translation:** Vocabulary: laptop: 笔记本电脑

**[5273.24s] English:** For cell phones, I think... I don't know why people buy new cell phones.  
**Translation:** 

**[5280.00s] English:** You know, because a new one's been announced. The cameras are better, but that's kind of demeaning.  
**Translation:** 

**[5284.20s] English:** Specific, right? They're putting special-purpose hardware to make the processing of images go much更快地处理图像。  
**Translation:** 

**[5289.54s] English:** Better. So that's the way they're doing it. They're not particularly concerned about it; it's just not a priority.  
**Translation:** 

**[5294.96s] English:** The ARM process is twice as fast as much they've added accelerators to help the experience.  
**Translation:** 

**[5301.30s] English:** Of the phone. Can we talk a little bit about one other exciting space? Arguably, it's at the same level of  
**Translation:** Vocabulary: accelerators: 加速器; arguably: 可以说

**[5308.84s] English:** Impact as your work with RISC is to RAID. In 1988, you co-authored a paper, "A Case for Redundant  
**Translation:** 

**[5319.38s] English:** Erase of Inexpensive Disks, hence RAID (Redundant Array of Independent Disks). So that's where you introduced the idea of RAID.  
**Translation:** Vocabulary: erase: 删除; redundant: 冗余

**[5327.48s] English:** Incredible that that little (I mean, little) paper kind of had this ripple effect and had a  
**Translation:** 

**[5334.28s] English:** Really, a revolutionary effect. So, first, what is RAID?  
**Translation:** 

**[5338.06s] English:** What is RAID?  
**Translation:** 

**[5338.84s] English:** So, this is work I did with my colleague, Randy Katz, and a star graduate student.  
**Translation:** Vocabulary: colleague: 同事

**[5343.60s] English:** Garth Gibson: So we had just done the fourth-generation RISC project, and Randy Katz,  
**Translation:** 

**[5351.70s] English:** Which had an early Apple Macintosh computer, at this time everything was done with floppy disks.  
**Translation:** Vocabulary: floppy: 软盘; gibson: 吉尔伯特; macintosh: 麦金塔

**[5360.16s] English:** Which are old technologies that could store things that didn't have much capacity? And you had to  
**Translation:** 

**[5368.06s] English:** Get anything done, you're always sticking your little floppy disk in and out, because they didn't  
**Translation:** Vocabulary: sticking: 插入

**[5372.78s] English:** They have a lot of capacity. But they started building what are called hard disk drives, which is magnetic.  
**Translation:** 

**[5378.28s] English:** Material that can remember information for storage on a Mac. And Randy asked the question when he saw.  
**Translation:** 

**[5385.84s] English:** This disk next to his Mac, gee, these are brand-new small things. Before that, for the big computers,  
**Translation:** 

**[5393.98s] English:** The disk would be the size of a washing machine.  
**Translation:** 

**[5398.06s] English:** The disk would be the size of something the size of a碟片的大小会和一个  
**Translation:** 

**[5400.00s] English:** Kind of the size of a book, or so.  
**Translation:** 

**[5402.46s] English:** He says, "I wonder what we could do with that.  
**Translation:** 

**[5403.76s] English:** Well, Randy was involved.  
**Translation:** 

**[5407.14s] English:** In the fourth-generation RISC project  
**Translation:** 

**[5410.58s] English:** Here at Berkeley in the '80s.  
**Translation:** Vocabulary: berkeley: 加州大学伯克利分校

**[5411.72s] English:** So, we figured out a way.  
**Translation:** 

**[5413.08s] English:** How to make the computational part?  
**Translation:** Vocabulary: computational: 计算相关的

**[5414.70s] English:** The processor part went a lot faster.  
**Translation:** 

**[5416.54s] English:** But what about the storage part?  
**Translation:** Vocabulary: processor: 中央处理器

**[5419.00s] English:** Can we do something to make it faster?  
**Translation:** 

**[5420.78s] English:** So, we hit upon the idea.  
**Translation:** 

**[5422.58s] English:** Of taking a lot of these disks,  
**Translation:** 

**[5425.24s] English:** Developed for personal computers.  
**Translation:** 

**[5426.50s] English:** And Macintoshes.  
**Translation:** 

**[5427.28s] English:** And putting many of them together.  
**Translation:** Vocabulary: macintoshes: 苹果电脑

**[5429.28s] English:** Instead of one of these,  
**Translation:** 

**[5430.02s] English:** Washing Machine: Size Matters.  
**Translation:** 

**[5431.78s] English:** And so, we wrote the first draft of the paper.  
**Translation:** 

**[5434.46s] English:** And we'd have 40 of these little PC disks.  
**Translation:** 

**[5436.70s] English:** Instead of one of these,  
**Translation:** 

**[5438.60s] English:** Washing Machine: Size Matters.  
**Translation:** 

**[5440.68s] English:** And they would be much cheaper.  
**Translation:** 

**[5441.84s] English:** Because they're made for PCs.  
**Translation:** 

**[5443.78s] English:** And they could actually kind of be faster.  
**Translation:** 

**[5445.36s] English:** Because there were 40 of them.  
**Translation:** 

**[5446.48s] English:** Rather than one of them.  
**Translation:** 

**[5448.20s] English:** And so, we wrote a paper like that.  
**Translation:** 

**[5449.44s] English:** And we sent it to one of our  
**Translation:** 

**[5450.68s] English:** Former Berkeley students at IBM.  
**Translation:** 

**[5452.40s] English:** And he said, "Well, this is all great and good,  
**Translation:** 

**[5453.80s] English:** But what about the reliability of these things?  
**Translation:** Vocabulary: reliability: 可靠性

**[5456.16s] English:** Now, you have 40 of these devices.  
**Translation:** 

**[5458.58s] English:** Each of them is kind of PC quality.  
**Translation:** 

**[5461.02s] English:** So, they're not as good.  
**Translation:** 

**[5462.08s] English:** As these IBM washing machines.  
**Translation:** 

**[5463.96s] English:** IBM dominated the storage market at its genesis.  
**Translation:** 

**[5468.52s] English:** So, the reliability is going to be awful.  
**Translation:** Vocabulary: dominated: 占据主导地位

**[5470.62s] English:** And so, when we calculated it out,  
**Translation:** 

**[5472.34s] English:** Instead of it breaking on average once a year,  
**Translation:** 

**[5475.52s] English:** It would break every two weeks.  
**Translation:** 

**[5477.44s] English:** So, we thought about the idea.  
**Translation:** 

**[5479.62s] English:** And he said, "Well,  
**Translation:** 

**[5480.94s] English:** We have to address the reliability.  
**Translation:** 

**[5482.76s] English:** So, we did it originally for performance.  
**Translation:** 

**[5484.38s] English:** But we had to do reliability.  
**Translation:** 

**[5485.80s] English:** So, the name is "redundant array.  
**Translation:** 

**[5488.20s] English:** Of inexperienced people,  
**Translation:** Vocabulary: inexperienced: 缺乏经验的; redundant: 冗余的

**[5488.98s] English:** Is an array of these disks.  
**Translation:** 

**[5491.02s] English:** Inexpensive, like for PCs.  
**Translation:** 

**[5492.80s] English:** But we have extra copies.  
**Translation:** 

**[5494.80s] English:** So, if one breaks,...  
**Translation:** 

**[5496.86s] English:** We won't lose all the information.  
**Translation:** 

**[5498.20s] English:** We'll have enough redundancy.  
**Translation:** Vocabulary: redundancy: 备份

**[5499.82s] English:** That we could let some break.  
**Translation:** 

**[5501.56s] English:** And we can still preserve the information.  
**Translation:** 

**[5503.24s] English:** So, the name is an array of inexpensive disks.  
**Translation:** 

**[5505.58s] English:** This is a collection of these PCs.  
**Translation:** 

**[5507.94s] English:** And the R part of the name.  
**Translation:** 

**[5509.62s] English:** It was the redundancy.  
**Translation:** 

**[5511.36s] English:** So, they'd be reliable.  
**Translation:** 

**[5512.28s] English:** And it turns out that if you put a modest number  
**Translation:** Vocabulary: modest: 谦逊的

**[5514.34s] English:** Of extra disks in one of these arrays,  
**Translation:** 

**[5516.34s] English:** It could actually not only be.  
**Translation:** Vocabulary: arrays: 磁盘阵列

**[5518.14s] English:** As it is faster and cheaper,  
**Translation:** 

**[5520.00s] English:** That one of these washing machine disks,  
**Translation:** 

**[5521.46s] English:** It could be actually more reliable.  
**Translation:** 

**[5522.94s] English:** Because you could have a couple of breaks.  
**Translation:** 

**[5525.22s] English:** Even with these cheap disks,  
**Translation:** 

**[5526.70s] English:** Whereas, one failure with the washing machine thing,...  
**Translation:** 

**[5528.90s] English:** It would knock it out.  
**Translation:** 

**[5530.64s] English:** Did you have a sense, just like with RISC?  
**Translation:** 

**[5532.72s] English:** That in the 30 years that followed,  
**Translation:** 

**[5537.50s] English:** RAID would take over as a mechanism for storage?  
**Translation:** 

**[5542.06s] English:** I'd say I'm naturally an optimist.  
**Translation:** 

**[5546.40s] English:** But I thought our ideas were right.  
**Translation:** Vocabulary: optimist: 积极的人

**[5550.50s] English:** I thought kind of like Moore's Law,  
**Translation:** 

**[5552.96s] English:** It seemed to me,  
**Translation:** 

**[5553.92s] English:** If you looked at the history of disk drives,  
**Translation:** 

**[5555.96s] English:** They went from washing-machine-size things.  
**Translation:** 

**[5557.98s] English:** And they were getting smaller and smaller.  
**Translation:** 

**[5559.58s] English:** And the volumes were with the smaller disk drives.  
**Translation:** 

**[5563.18s] English:** Because that's where the PCs were.  
**Translation:** 

**[5565.22s] English:** So, we thought that was a technological trend.  
**Translation:** 

**[5567.74s] English:** That disk drives,  
**Translation:** 

**[5569.48s] English:** The volume of disk drives was going to be  
**Translation:** 

**[5572.22s] English:** Getting smaller and smaller devices,  
**Translation:** 

**[5574.36s] English:** Which were true.  
**Translation:** 

**[5574.98s] English:** They were the size of a.  
**Translation:** 

**[5576.40s] English:** I don't know.  
**Translation:** 

**[5577.22s] English:** Eight inches in diameter.  
**Translation:** 

**[5578.54s] English:** Then, five inches.  
**Translation:** 

**[5579.48s] English:** Then they are three inches in diameter.  
**Translation:** 

**[5581.26s] English:** And so, it made sense to figure out.  
**Translation:** 

**[5583.90s] English:** How to deal with things in an array of disks.  
**Translation:** 

**[5586.20s] English:** So, I think it was one of those things.  
**Translation:** 

**[5587.68s] English:** Where, logically, we think the technological forces  
**Translation:** 

**[5591.84s] English:** We were on our side.  
**Translation:** Vocabulary: logically: 合乎逻辑地

**[5592.98s] English:** That it made sense.  
**Translation:** 

**[5594.70s] English:** So, we expected it to catch on.  
**Translation:** 

**[5596.98s] English:** But there was that same kind of business question.  
**Translation:** 

**[5599.86s] English:** You know, IBM was the big pusher of these disk drives.  
**Translation:** 

**[5602.66s] English:** In the real world,  
**Translation:** 

**[5604.60s] English:** Where the technical advantage gets turned  
**Translation:** 

**[5606.28s] English:** Into the technology advantage.  
**Translation:** 

**[5606.40s] English:** To a business advantage, or not.  
**Translation:** 

**[5608.48s] English:** It proved to be true.  
**Translation:** 

**[5609.92s] English:** It did.  
**Translation:** 

**[5610.30s] English:** And so, you know,  
**Translation:** 

**[5611.56s] English:** We thought we were sound technically.  
**Translation:** Vocabulary: technically: 技术上

**[5613.40s] English:** And it was unclear whether the business side,  
**Translation:** 

**[5616.68s] English:** But we kind of,  
**Translation:** 

**[5617.60s] English:** As academics,  
**Translation:** 

**[5618.38s] English:** We believe that technology should win.  
**Translation:** 

**[5620.22s] English:** And it did.  
**Translation:** 

**[5622.02s] English:** And if you look at those 30 years,  
**Translation:** 

**[5624.28s] English:** Just from your perspective,  
**Translation:** 

**[5625.88s] English:** Are there any interesting developments?  
**Translation:** 

**[5627.16s] English:** In the space of storage  
**Translation:** 

**[5628.30s] English:** That has happened in that time?  
**Translation:** 

**[5630.40s] English:** Yeah.  
**Translation:** 

**[5630.68s] English:** The big thing that happened was,  
**Translation:** 

**[5632.20s] English:** Well, a couple of things happened.  
**Translation:** 

**[5634.08s] English:** What we did had a modest amount of storage.  
**Translation:** Vocabulary: modest: 不多

**[5636.28s] English:** So, as a redundancy,  
**Translation:** 

**[5639.34s] English:** As people,  
**Translation:** 

**[5640.00s] English:** People built bigger and bigger storage systems.  
**Translation:** 

**[5642.38s] English:** They've added more redundancy so they could add more failures.  
**Translation:** Vocabulary: redundancy: 多余的备份

**[5645.90s] English:** And the biggest thing that happened in storage is that, for decades, it was based on things physically spinning, called hard disk drives.  
**Translation:** 

**[5655.62s] English:** We used to turn on your computer, and it would make a noise.  
**Translation:** Vocabulary: spinning: 硬盘旋转

**[5658.56s] English:** What that noise was was the disk drive spinning.  
**Translation:** 

**[5661.40s] English:** And they were rotating at about 60 revolutions per second.  
**Translation:** Vocabulary: revolutions: 每秒转动次数; rotating: 旋转

**[5665.56s] English:** And it's like, if you remember vinyl records—those are what they looked like.  
**Translation:** 

**[5672.86s] English:** And there was a needle, like on a vinyl record, reading it.  
**Translation:** Vocabulary: vinyl: 乙烯基唱片

**[5676.30s] English:** So, the big drive change is switching that over to a semiconductor technology called flash.  
**Translation:** 

**[5681.04s] English:** So, within the last decade or so, the fraction of all the computers in the world using semiconductors for storage has been increasing.  
**Translation:** Vocabulary: semiconductor: 半导体; semiconductors: 半导体

**[5691.16s] English:** The flash drive, instead of being magnetic,  
**Translation:** 

**[5694.36s] English:** They are optical, and they are, well, a semiconductor writing of information into very dense areas, which has been a huge difference.  
**Translation:** Vocabulary: optical: 激光读写

**[5705.58s] English:** So, all the cell phones in the world use flash.  
**Translation:** 

**[5708.04s] English:** Most of the laptops use flash, while all the embedded devices use flash instead of storage.  
**Translation:** Vocabulary: embedded: 嵌入式; laptops: 笔记本电脑

**[5712.84s] English:** Still in the cloud, magnetic disks are more economical than flash, but they use both in the cloud.  
**Translation:** 

**[5720.22s] English:** So, it's been a huge change in the storage industry.  
**Translation:** Vocabulary: economical: 经济的

**[5723.04s] English:** This, the,  
**Translation:** 

**[5724.48s] English:** Of switching from primarily disk to being primarily semiconductor.  
**Translation:** 

**[5728.46s] English:** For the individual disks, but the RAID mechanism still applies to those different kinds of disks.  
**Translation:** 

**[5732.66s] English:** Yes, the people will still use RAID ideas because it's kind of what's different, you know—kind of interesting, kind of psychologically—if you think about it.  
**Translation:** Vocabulary: psychologically: 心理上

**[5743.72s] English:** People have always worried about the reliability of computing, since the earliest days.  
**Translation:** 

**[5747.04s] English:** So, kind of, but if we're talking about computation, if your computer makes a mistake in,  
**Translation:** Vocabulary: computation: 计算; computing: 计算; reliability: 可靠性

**[5754.36s] English:** The computer says, "We have ways to check and say, oh, we screwed up, we made a mistake.  
**Translation:** 

**[5760.00s] English:** What happens is that, if a program that was running crashes, you have to redo it, which is a hassle for storage.  
**Translation:** Vocabulary: hassle: 麻烦

**[5766.74s] English:** If you've sent important information away and it loses that information, you go nuts, yeah. This is  
**Translation:** 

**[5775.08s] English:** The worst, oh my God! So if you have a laptop and you're not backing it up on the cloud or something,...  
**Translation:** Vocabulary: laptop: 笔记本电脑

**[5780.52s] English:** Like this, and your disk drive might break, which it can do, and you'll lose all that information, and you just  
**Translation:** 

**[5786.84s] English:** Go crazy, right? So, the importance of reliability for storage is tremendously higher than the  
**Translation:** Vocabulary: tremendously: 极其

**[5792.08s] English:** The importance of reliability in computation, because of the consequences, is so obvious. Yes, so rates and ideas are crucial.  
**Translation:** 

**[5797.78s] English:** Are still very popular, even with the switch to newer technologies, although you know, flash drives are more  
**Translation:** Vocabulary: crucial: 至关重要的

**[5802.74s] English:** Reliable, you know, if you're not doing anything like backing it up to get some redundancy, so  
**Translation:** 

**[5808.56s] English:** They handle it; you're taking great risks, you said, for you and possibly for many.  
**Translation:** Vocabulary: redundancy: 备份

**[5816.84s] English:** Other people who are doing research don't conflict with each other, as one might suspect, and in fact,  
**Translation:** 

**[5821.88s] English:** They kind of complement each other, so maybe a question I have is: How has teaching helped you?  
**Translation:** 

**[5827.28s] English:** In your research, or just in your entirety as a person who both teaches and does research,  
**Translation:** 

**[5834.98s] English:** Thinks and creates new ideas in this world, yes. I think what happens is that when you're  
**Translation:** Vocabulary: entirety: 整体

**[5841.06s] English:** A college student, you know, there's this kind of tenure system, and doing research, so kind of...  
**Translation:** 

**[5845.36s] English:** This model that  
**Translation:** 

**[5846.84s] English:** Uh, you know, it's popular in America, I think America really made it happen. Is we can attract these.  
**Translation:** 

**[5852.54s] English:** Really, a great faculty for research universities because they get to do research as well as teach.  
**Translation:** 

**[5858.20s] English:** And that, especially in fast-moving fields, this means people are up to date and they're teaching.  
**Translation:** 

**[5862.60s] English:** Those kinds of things, so, but when you run into a really bad professor or teacher,  
**Translation:** 

**[5867.48s] English:** I think the students think well, this guy must be a great researcher because why else could he be?  
**Translation:** 

**[5873.04s] English:** Here, so as I know, I've been a professor for a long time after 40 years at Berkeley.  
**Translation:** Vocabulary: berkeley: 加州大学伯克利分校

**[5876.84s] English:** At Berkeley, we had a retirement party, and I got a chance to reflect and look back.  
**Translation:** 

**[5880.00s] English:** At some things, that is not my experience. I saw a photograph of five of us in the department who  
**Translation:** 

**[5888.28s] English:** Won the Distinguished Teaching Award from campus, a very high honor. I've got one of those, one of  
**Translation:** 

**[5893.12s] English:** The highest honors. So there are five of us in that picture: Manuel Blum, Richard Karp,  
**Translation:** Vocabulary: distinguished: 卓越的

**[5901.30s] English:** Me, Randy Kass, and John Osterhout, contemporaries of mine. I mentioned Randy already. All of us are  
**Translation:** 

**[5907.06s] English:** In the National Academy of Engineering. We've all won the Distinguished Teaching Award, Blum.  
**Translation:** Vocabulary: contemporaries: 同时代的人; randy: Rand Kass的昵称

**[5912.96s] English:** Karp, and I, all have Turing Awards, the highest award in computing. So that's the opposite.  
**Translation:** 

**[5921.62s] English:** Right? What happens is they're highly correlated. So, probably the other way to think of it,  
**Translation:** Vocabulary: computing: 计算; correlated: 相关; turing: 图灵

**[5928.88s] English:** If you're very successful in everything you do, it's not an either-or.  
**Translation:** 

**[5934.72s] English:** But it's an interesting question whether it's  
**Translation:** 

**[5936.84s] English:** Specific, or not?  
**Translation:** 

**[5937.06s] English:** Specifically, that's probably true, but specifically for teaching, if there's something  
**Translation:** 

**[5940.90s] English:** In teaching, that's the Richard Feyman idea: is there something about teaching that actually  
**Translation:** 

**[5946.80s] English:** Does it make your research make you think deeper and more outside the box and more insightful?  
**Translation:** 

**[5952.76s] English:** Absolutely. I was going to bring up Feynman. I mean, he criticized the Institute of Advanced Study.  
**Translation:** 

**[5956.46s] English:** Studies. The Institute for Advanced Study was this thing created near Princeton.  
**Translation:** Vocabulary: feynman: 费曼; princeton: 普林斯顿

**[5961.48s] English:** Where Einstein and all these smart people went. And when he was invited, he thought it was a  
**Translation:** 

**[5966.36s] English:** Terrible idea.  
**Translation:** Vocabulary: einstein: 爱因斯坦

**[5967.06s] English:** This is a university. It was supposed to be heaven, right? A university without any teaching.  
**Translation:** 

**[5972.66s] English:** But he thought it was a mistake. It's getting up in front of the classroom and having to explain things to  
**Translation:** 

**[5977.00s] English:** Students and having them ask questions like, "Well, why is that true?" makes you stop and think.  
**Translation:** 

**[5981.96s] English:** So he thought, and I agree: I think that interaction between a great research university,...  
**Translation:** 

**[5988.50s] English:** And having students with bright young minds asking hard questions the whole time is synergistic.  
**Translation:** 

**[5994.84s] English:** And a university without teaching,  
**Translation:** Vocabulary: synergistic: 相互促进的

**[5996.84s] English:** Teaching wouldn't be as vital.  
**Translation:** 

**[6000.00s] English:** And it's an exciting place, and I think it helps stimulate the research. Another romanticized idea.  
**Translation:** Vocabulary: stimulate: 激发

**[6007.62s] English:** Question, but what's your favorite concept or idea to teach? What inspires you, or you see as particularly impactful?  
**Translation:** 

**[6014.00s] English:** Inspire the students—is there something that pops to mind, or does it put the fear of God in them? I don't.  
**Translation:** Vocabulary: inspires: 鼓舞

**[6019.22s] English:** Know which is most effective, uh, I mean, in general, I think people are surprised; I've seen  
**Translation:** 

**[6025.66s] English:** A lot of people who don't think they like teaching often come and give guest lectures or teach a course.  
**Translation:** 

**[6031.68s] English:** And get hooked on seeing the lights turn on when people finally understand something you can explain to them.  
**Translation:** 

**[6037.74s] English:** They don't understand, and suddenly they get something, you know—that's that's not that's  
**Translation:** Vocabulary: hooked: 上瘾

**[6042.76s] English:** Important and difficult, and just seeing the lights turn on is a real satisfaction.  
**Translation:** 

**[6048.06s] English:** There, I don't think there's any specific example of that; it's just the general joy of.  
**Translation:** 

**[6055.40s] English:** Seeing  
**Translation:** 

**[6055.66s] English:** Them, uh, seeing them understand, I have to talk about this because I've wrestled with martial arts.  
**Translation:** Vocabulary: martial: 武术; wrestled: 挣扎

**[6063.24s] English:** Arts, yeah, of course I love wrestling; I'm a huge fan. I'm Russian, so I've definitely talked to Dan.  
**Translation:** 

**[6068.92s] English:** Gable, on oh, yeah. Guest, so I know Yang Gable was my era kind of guy. So you wrestled at UCLA, among  
**Translation:** Vocabulary: gable: 山墙; wrestling: 摔跤

**[6077.00s] English:** Many other things you've done in your life, competitively in sports and science, and so on, you've  
**Translation:** 

**[6081.88s] English:** You've wrestled, maybe, again, continuing.  
**Translation:** Vocabulary: competitively: 竞争地

**[6085.40s] English:** With the romanticized questions, but uh, what have you learned about life? Yeah, and maybe even science.  
**Translation:** 

**[6090.76s] English:** From wrestling or from, yeah, that's actually fact. I wrestled at UCLA but also at El Camino Community College.  
**Translation:** Vocabulary: camino: 小路

**[6097.68s] English:** College, and just right now, we were in the state of California; we were state champions at El Camino.  
**Translation:** 

**[6103.68s] English:** And, in fact, I was talking to my mom, and I got into UCLA, but I decided to go to the community college.  
**Translation:** Vocabulary: california: 加利福尼亚州

**[6110.02s] English:** College: which is it's much harder to go to UCLA than the community college, and I asked, "Well, I've...  
**Translation:** 

**[6115.40s] English:** Got to go to the community college, and I said, "Why did I make that decision?" Because I thought it was  
**Translation:** 

**[6117.08s] English:** Because of my girlfriend, she said, "Well, it was the girlfriend," and you thought there.  
**Translation:** 

**[6120.00s] English:** The wrestling team was really good, and we were right—we had a great wrestling team. We actually, uh,  
**Translation:** 

**[6126.02s] English:** We wrestled against UCLA at a tournament, and we beat UCLA. It is a community college, which is just  
**Translation:** 

**[6132.04s] English:** Freshmen and sophomores, and the part of reason I brought this up is that I'm going to go; they've  
**Translation:** Vocabulary: freshmen: 大一学生; sophomores: 大二学生

**[6136.70s] English:** Invited me back to El Camino to give a lecture next month, and so I'm meeting with my friend.  
**Translation:** 

**[6145.32s] English:** Who was on the wrestling team, and uh, that we're still together; we're right now reaching out to.  
**Translation:** 

**[6150.00s] English:** Other members of the wrestling team we can get together for a reunion, but in terms of me, it was  
**Translation:** 

**[6155.30s] English:** A huge difference. I was, I was both. I was kind of the age cutoff; it was December 1st, and so  
**Translation:** Vocabulary: cutoff: 截止日期; wrestling: 摔跤

**[6161.54s] English:** I was almost always the youngest person in my class, and I matured later on. You know, our family...  
**Translation:** 

**[6168.96s] English:** Matured later, so I was almost always the smallest guy, so you know, I took kind of a nerdy approach.  
**Translation:** Vocabulary: matured: 成熟; nerdy: 书呆子

**[6174.92s] English:** Courses:  
**Translation:** 

**[6175.32s] English:** But I was wrestling, so wrestling was huge for my self-confidence in high school.  
**Translation:** 

**[6182.12s] English:** And then, you know, I kind of got bigger at El Camino and in college, and so I had this, uh,...  
**Translation:** 

**[6187.98s] English:** Of physical self-confidence, and it's translated into research self-confidence, uh, and also.  
**Translation:** Vocabulary: camino: 朝圣之路

**[6198.34s] English:** Kind of, I've had this feeling even today in my 70s; you know, if something  
**Translation:** 

**[6205.32s] English:** If something is going on in the streets that is bad, physically, I'm not going to ignore it; right?  
**Translation:** 

**[6209.46s] English:** Going to stand up and try and straighten that out, and that kind of confidence just carries through.  
**Translation:** 

**[6214.22s] English:** The entirety of your life, yeah, and the same thing happens intellectually if there's something  
**Translation:** Vocabulary: entirety: 全部; intellectually: 在智力上; straighten: 整理

**[6218.42s] English:** Going on, where people are saying something that's not true, I feel it's my job to stand up and just  
**Translation:** 

**[6224.00s] English:** Like I would in the street, if there's something going on, like somebody attacking some woman or  
**Translation:** 

**[6228.16s] English:** Something I'm not standing by and letting that get away, so I feel it's my job to stand up.  
**Translation:** 

**[6233.50s] English:** So, it's kind of ironically translated.  
**Translation:** Vocabulary: ironically: 反讽地

**[6235.32s] English:** The other things that turned out great for both: I had a really great college experience, and  
**Translation:** 

**[6240.00s] English:** High school coaches. And they believed, even though wrestling is an individual sport,  
**Translation:** Vocabulary: wrestling: 摔跤

**[6244.94s] English:** That we would be more successful as a team if we bonded together and did things that we would support.  
**Translation:** 

**[6250.28s] English:** Each other, rather than everybody. You know, in wrestling, it's a one-on-one, and you could be  
**Translation:** Vocabulary: bonded: 团结

**[6254.24s] English:** Everybody's on their own, but he felt that if we bonded as a team, we'd succeed. So I kind of picked up.  
**Translation:** 

**[6259.74s] English:** Those skills of how to form successful teams, and how do you apply them, came from wrestling. And so I think one of  
**Translation:** 

**[6265.72s] English:** Most people would say, "One of my strengths is that I can create large teams of faculty.  
**Translation:** 

**[6272.16s] English:** Faculty and grad students pull together for a common goal, and you know, often are successful.  
**Translation:** 

**[6278.02s] English:** At it. But I got both of those things from wrestling. Also, I think I heard this line about.  
**Translation:** 

**[6284.20s] English:** If people are in a kind of sport with physical contact, like  
**Translation:** 

**[6290.08s] English:** Wrestling or football and stuff like that, people are a little bit more, you know, assertive or  
**Translation:** 

**[6295.04s] English:** Something.  
**Translation:** Vocabulary: assertive: 有主見的

**[6295.72s] English:** And so, I think that also comes through as, you know, I wasn't shy away from  
**Translation:** 

**[6302.16s] English:** The risk-sys debates, you know, I enjoyed taking on the arguments and stuff like that. So,  
**Translation:** 

**[6307.44s] English:** It was, it was. I'm really glad I did wrestling. I think it was really good for my self-image and  
**Translation:** 

**[6312.90s] English:** I learned a lot from it. So I think that's, you know, sports done well; there's really  
**Translation:** 

**[6317.88s] English:** Lots of positives you can take from it, like leadership, you know, how to form teams.  
**Translation:** 

**[6324.50s] English:** And how to be successful.  
**Translation:** Vocabulary: positives: 积极方面

**[6325.72s] English:** So, we've talked a lot about metrics. There's a really cool thing in terms of bench press and weightlifting.  
**Translation:** 

**[6331.44s] English:** Pounds, years, and metric — that you've developed, that we don't have time to talk about, but it's a...  
**Translation:** Vocabulary: metric: 衡量标准; metrics: 指标; weightlifting: 举重

**[6335.48s] English:** Really cool one that people should look into. It's rethinking the way we think about metrics and...  
**Translation:** 

**[6339.66s] English:** Weightlifting. But let me talk about metrics more broadly, since that appeals to you in all forms.  
**Translation:** Vocabulary: appeals: 有吸引力; broadly: 广泛地

**[6345.46s] English:** Let's look at the most ridiculous, the biggest question of the meaning of life.  
**Translation:** 

**[6350.32s] English:** If you were to try to put metrics on a life well-lived, what would those metrics be?  
**Translation:** 

**[6355.72s] English:** Yeah, a friend of mine, Randy Katz, said this: He said,  
**Translation:** 

**[6360.00s] English:** And, you know, when it's time to sign off, it's not the number of zeros in your bank account that matters.  
**Translation:** 

**[6368.54s] English:** It's the number of inches in the obituary in The New York Times.  
**Translation:** 

**[6372.48s] English:** As he said it, I think, you know, having and, you know, this is a cliché: people don't die wishing they'd spent more time in the office.  
**Translation:** Vocabulary: obituary: 讣告

**[6382.32s] English:** Right. As I reflect upon my career, there have been, you know, a half a dozen or a dozen things.  
**Translation:** 

**[6389.42s] English:** I'd say I've been proud of a lot of them, but they're not papers or scientific results.  
**Translation:** 

**[6393.66s] English:** Certainly, my family—my wife and we have been married for more than 50 years—with kids and grandchildren.  
**Translation:** 

**[6400.14s] English:** That's really precious, education-wise. I've done a lot of those things.  
**Translation:** 

**[6404.38s] English:** I'm very proud of books and courses.  
**Translation:** 

**[6408.90s] English:** I did some work with underrepresented groups that was effective.  
**Translation:** Vocabulary: underrepresented: 少数群体

**[6412.82s] English:** So, it was interesting to see what things I reflected on.  
**Translation:** 

**[6415.94s] English:** You know, I had hundreds of papers.  
**Translation:** 

**[6418.38s] English:** But some of them.  
**Translation:** 

**[6419.54s] English:** Some of them were the papers like the risk and rate stuff that I'm proud of, but a lot of them were—or were not—those things.  
**Translation:** 

**[6424.42s] English:** So, people who just spend their lives going after the dollars or all the papers in the world, you know, that's probably not the stuff you'll care about later.  
**Translation:** 

**[6435.84s] English:** When I was just getting the offer from Berkeley before I showed up, I read a book where they interviewed a lot of people and from all walks of life.  
**Translation:** Vocabulary: berkeley: 加州大学伯克利分校

**[6445.48s] English:** And what I got out of that book was that the people who felt good about what they did were the people.  
**Translation:** 

**[6449.42s] English:** Who affected people, as opposed to things that were more transitory.  
**Translation:** Vocabulary: transitory: 短暂的

**[6452.92s] English:** So, I came into this job assuming that it wasn't going to be the papers or relationships with the people over time that I would value.  
**Translation:** 

**[6461.32s] English:** And that was a correct assessment.  
**Translation:** 

**[6462.90s] English:** Right. It's the people you work with, the people you can influence, and the people you can help—that are the things you feel good about towards the end of your career.  
**Translation:** 

**[6470.52s] English:** It's not the stuff that's more transitory.  
**Translation:** 

**[6474.24s] English:** I don't think there's a better way to end it than talking about your family.  
**Translation:** 

**[6478.28s] English:** The over 50.  
**Translation:** 

**[6480.00s] English:** Years of being married to your childhood sweetheart.  
**Translation:** 

**[6482.78s] English:** One thing I could add is: when you tell people you've been married for 50 years, they want to know why.  
**Translation:** 

**[6488.04s] English:** How?  
**Translation:** 

**[6488.68s] English:** Why?  
**Translation:** 

**[6489.14s] English:** I can tell you the nine magic words that you need to say to your partner to keep a good relationship.  
**Translation:** 

**[6495.90s] English:** And the nine magic words are, "I was wrong.  
**Translation:** 

**[6498.82s] English:** You were right.  
**Translation:** 

**[6500.10s] English:** I love you.  
**Translation:** 

**[6501.12s] English:** Okay.  
**Translation:** 

**[6501.64s] English:** And you've got to say all nine.  
**Translation:** 

**[6502.80s] English:** You can't say, "I was wrong.  
**Translation:** 

**[6504.34s] English:** You were right.  
**Translation:** 

**[6504.84s] English:** You're a jerk.  
**Translation:** 

**[6505.34s] English:** You can't say that.  
**Translation:** 

**[6506.70s] English:** So, freely acknowledging that you made a mistake, the other person was right, and that you love them, really gets over a lot of bumps in the road.  
**Translation:** 

**[6516.58s] English:** So, that's what I pass along.  
**Translation:** Vocabulary: acknowledging: 承认

**[6518.50s] English:** Beautifully put.  
**Translation:** 

**[6519.54s] English:** David, it's a huge honor.  
**Translation:** 

**[6521.36s] English:** Thank you so much for the book you've written, for the research you've done, for changing the world.  
**Translation:** 

**[6525.12s] English:** Thank you for talking today.  
**Translation:** 

**[6525.98s] English:** Thanks for the interview.  
**Translation:** 

**[6527.82s] English:** Thanks for listening to this conversation with David Patterson.  
**Translation:** 

**[6530.36s] English:** And thank you to our sponsors, The Jordan Harbinger Show and Cash App.  
**Translation:** 

**[6536.70s] English:** Please consider supporting this podcast by going to jordanharbinger.com/Lex and downloading Cash App and using code LexPodcast.  
**Translation:** Vocabulary: harbinger: 预兆; jordanharbinger: 乔恩哈伯; sponsors: 赞助商

**[6545.74s] English:** Click the links, buy the stuff.  
**Translation:** 

**[6548.12s] English:** It's the best way to support this podcast and the journey I'm on.  
**Translation:** 

**[6551.74s] English:** If you enjoy this thing, subscribe on YouTube, leave a review with 5,000 views, have a podcast, support it on Patreon, or connect with me on Twitter at @LexFriedman (spelled without the E).  
**Translation:** 

**[6563.26s] English:** Try to figure out how to do that.  
**Translation:** Vocabulary: patreon: Patreon支持; subscribe: 订阅

**[6564.72s] English:** It's just F-R-I-D-M-A-N.  
**Translation:** 

**[6567.40s] English:** And now, let me leave you with some words from Henry David Thoreau.  
**Translation:** Vocabulary: thoreau: 梭罗

**[6572.10s] English:** Our life is fretted away by detail.  
**Translation:** 

**[6575.86s] English:** Simplify.  
**Translation:** Vocabulary: fretted: 消磨; simplify: 简化

**[6577.08s] English:** Simplify.  
**Translation:** 

**[6578.76s] English:** Thank you for listening, and I hope to see you next time.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
