# Podcast vocabulary notes
Source file: Lex Fridman - David Patterson： Computer Architecture and Data Storage ｜ Lex Fridman Podcast #104.opus

**[0.00s] English:** The following is a conversation with David Patterson, Turing Award winner and professor  
**Translation:** 

**[5.36s] English:** of computer science at Berkeley. He's known for pioneering contributions to risk processor  
**Translation:** 

**[10.76s] English:** architecture used by 99% of new chips today and for co-creating RAID storage. The impact that  
**Translation:** 

**[18.88s] English:** these two lines of research and development have had on our world is immeasurable. He's also one  
**Translation:** Vocabulary: immeasurable: 无法衡量

**[25.00s] English:** of the great educators of computer science in the world. His book with John Hennessy is how I  
**Translation:** 

**[29.98s] English:** first learned about and was humbled by the inner workings of machines at the lowest level. Quick  
**Translation:** Vocabulary: educators: 教育家; workings: 工作机制

**[36.20s] English:** summary of the ads. Two sponsors, the Jordan Harbinger Show and Cash App. Please consider  
**Translation:** 

**[42.52s] English:** supporting the podcast by going to jordanharbinger.com slash lex and downloading Cash App  
**Translation:** Vocabulary: jordanharbinger: 乔恩哈伯辛格; sponsors: 赞助商

**[48.48s] English:** and using code lexpodcast. Click on the links, buy the stuff. It's the best way to support the  
**Translation:** 

**[54.98s] English:** podcast and, in general, the journey I'm on in my research and startup. This is the Artificial  
**Translation:** Vocabulary: lexpodcast: 词播客

**[60.44s] English:** Intelligence Podcast. If you enjoy it, subscribe on YouTube, review it with five stars on Apple  
**Translation:** 

**[65.28s] English:** Podcasts, support it on Patreon, or connect with me on Twitter at Lex Friedman, spelled without the  
**Translation:** 

**[71.68s] English:** E, just F-R-I-D-M-A-N. As usual, I'll do a few minutes of ads now and never any ads in the middle  
**Translation:** 

**[78.66s] English:** that can break the flow of the conversation. This episode is supported by the Jordan Harbinger Show.  
**Translation:** Vocabulary: harbinger: 先兆

**[84.98s] English:** Go to jordanharbinger.com slash lex. It's how he knows I sent you. On that page, there's links to  
**Translation:** 

**[91.02s] English:** subscribe to it on Apple Podcasts, Spotify, and everywhere else. I've been binging on this podcast.  
**Translation:** Vocabulary: subscribe: 订阅

**[96.68s] English:** It's amazing. Jordan is a great human being. He gets the best out of his guests, dives deep,  
**Translation:** 

**[101.78s] English:** calls them out when it's needed, and makes the whole thing fun to listen to. He's interviewed  
**Translation:** 

**[106.02s] English:** Kobe Bryant, Mark Cuban, Neil deGrasse Tyson, Garry Kasparov, and many more. I recently listened  
**Translation:** 

**[112.58s] English:** to his conversation with Frank Abagnale. He's a great guy. He's a great guy. He's a great guy. He's a great guy.  
**Translation:** Vocabulary: bryant: 科比; cuban: 卡文; garry: 加里; kasparov: 卡斯帕罗夫; tyson: 泰森

**[114.98s] English:** Author of Catch Me If You Can and one of the world's most famous con men.  
**Translation:** 

**[120.00s] English:** Perfect podcast length and topic for a recent long-distance run that I did.  
**Translation:** 

**[125.92s] English:** Again, go to jordanharbinger.com slash Lex to give him my love and to support this podcast.  
**Translation:** 

**[133.40s] English:** Subscribe also on Apple Podcasts, Spotify, and everywhere else.  
**Translation:** 

**[137.86s] English:** This show is presented by Cash App, the greatest sponsor of this podcast ever and the number one finance app in the App Store.  
**Translation:** 

**[146.22s] English:** When you get it, use code LexPodcast.  
**Translation:** 

**[148.58s] English:** Cash App lets you send money to friends, buy Bitcoin, and invest in the stock market with as little as $1.  
**Translation:** 

**[154.94s] English:** Since Cash App allows you to buy Bitcoin, let me mention that cryptocurrency in the context of the history of money is fascinating.  
**Translation:** Vocabulary: cryptocurrency: 加密货币

**[161.96s] English:** I recommend Ascent of Money as a great book on this history.  
**Translation:** 

**[165.34s] English:** Also, the audiobook is amazing.  
**Translation:** Vocabulary: ascent: 上升; audiobook: 有声书

**[167.74s] English:** Debits and credits on Ledger started around 30,000 years ago.  
**Translation:** 

**[171.46s] English:** The US dollar created over 200 years ago.  
**Translation:** Vocabulary: ledger: 账簿

**[174.14s] English:** And the first decentralized cryptocurrency released just over 10 years ago.  
**Translation:** 

**[177.70s] English:** So given that history, cryptocurrency is still very much in its early days of development.  
**Translation:** Vocabulary: decentralized: 去中心化

**[182.96s] English:** But it's still aiming to and just might redefine the nature of money.  
**Translation:** 

**[187.94s] English:** So again, if you get Cash App from the App Store or Google Play and use the code LexPodcast, you get $10.  
**Translation:** Vocabulary: redefine: 重新定义

**[194.96s] English:** And Cash App will also donate $10 to FIRST, an organization that is helping to advance robotics and STEM education for young people around the world.  
**Translation:** 

**[203.10s] English:** And now, here's my conversation with David Patterson.  
**Translation:** 

**[208.68s] English:** Let's start with the big historical question.  
**Translation:** 

**[211.70s] English:** How have computers changed in the past 50 years at both the fundamental architectural level and in general, in your eyes?  
**Translation:** Vocabulary: architectural: 架构

**[219.12s] English:** Well, the biggest thing that happened was the invention of the microprocessor.  
**Translation:** 

**[223.14s] English:** So computers that used to fill up several rooms could fit inside your cell phone.  
**Translation:** Vocabulary: microprocessor: 微处理器

**[229.82s] English:** And not only did they get smaller, they got a lot faster.  
**Translation:** 

**[234.82s] English:** So they're a million times faster than they were.  
**Translation:** 

**[237.70s] English:** 50 years ago.  
**Translation:** 

**[239.70s] English:** And they're.  
**Translation:** 

**[240.00s] English:** much cheaper and they're ubiquitous uh you know i don't there's 7.8 billion people on this planet  
**Translation:** 

**[246.98s] English:** probably half of them have cell phones right now just remarkable there's probably more  
**Translation:** Vocabulary: ubiquitous: 无处不在

**[253.08s] English:** microprocessors than there are people sure i don't know what the ratio is but i'm sure it's above one  
**Translation:** 

**[258.22s] English:** uh maybe it's 10 to 1 or some number like that what is a microprocessor so uh a way to say what  
**Translation:** 

**[266.64s] English:** a microprocessor is to tell you what's inside a computer so a computer forever has classically had  
**Translation:** 

**[272.34s] English:** five pieces there's input and output which kind of naturally as you'd expect is input is like  
**Translation:** 

**[279.04s] English:** speech or typing and output is displays um there's a memory and like the name sounds it it remembers  
**Translation:** 

**[289.40s] English:** things so it's uh integrated circuits whose job is you put information in and when you ask for it  
**Translation:** Vocabulary: circuits: 集成电路

**[295.18s] English:** comes back out that's memory  
**Translation:** 

**[296.46s] English:** and the third part is the processor uh where the team microprocessor comes from and that has two  
**Translation:** Vocabulary: processor: 处理器

**[302.58s] English:** pieces as well and that is the control which is kind of the brain of the processor and the um  
**Translation:** 

**[311.62s] English:** the what's called the arithmetic unit it's kind of the brawn of the computer so if you think of the  
**Translation:** Vocabulary: arithmetic: 算术; brawn: 力量

**[316.34s] English:** as a human body the arithmetic unit the thing that does the number crunching is the is the body and  
**Translation:** 

**[322.04s] English:** the control is the brain so those five pieces input output memory  
**Translation:** Vocabulary: crunching: 计算

**[325.70s] English:** you  
**Translation:** 

**[326.46s] English:** uh arithmetic unit and control are have been in computers since the very dawn and the last two are  
**Translation:** 

**[334.72s] English:** considered the processor so a microprocessor simply means a processor that fits on a microchip  
**Translation:** 

**[340.42s] English:** and that was invented about you know 40 years ago uh was the first microprocessor it's interesting  
**Translation:** 

**[346.86s] English:** that you refer to the arithmetic unit as the like you connected to the the body and the controllers  
**Translation:** 

**[352.98s] English:** of the brain so i guess i never thought of it that way i think it's kind of like a computer  
**Translation:** 

**[356.46s] English:** the the nice way to think of it because most of the actions the microprocessor  
**Translation:** 

**[360.00s] English:** does in terms of literally sort of computation but the microprocessor does computation it  
**Translation:** Vocabulary: computation: 计算; microprocessor: 微处理器

**[367.58s] English:** processes information and most of the thing it does is basic arithmetic operations what what  
**Translation:** 

**[374.88s] English:** are the operations by the way it's a lot like a calculator you know so there are um add instructions  
**Translation:** 

**[380.94s] English:** subtract instructions multiply and divide and uh kind of the brilliance of the invention of the of  
**Translation:** 

**[389.20s] English:** the micro of the computer or the processor is that it performs very trivial operations but it  
**Translation:** Vocabulary: brilliance: 卓越之处; multiply: 乘法; subtract: 减法

**[396.32s] English:** just performs billions of them per second and uh what we're capable of doing is writing software  
**Translation:** 

**[402.54s] English:** that can take these very trivial instructions and have them create tasks that can do things  
**Translation:** 

**[408.00s] English:** better than human beings can do today just looking back through your career did you anticipate the  
**Translation:** 

**[413.74s] English:** kind of how good we would be able to get at doing these small basic operations  
**Translation:** Vocabulary: anticipate: 预见

**[419.20s] English:** like what like how many surprises along the way where you just kind of sat back  
**Translation:** 

**[424.26s] English:** and said wow that i didn't expect it to go this fast this good well the the fundamental driving  
**Translation:** 

**[431.80s] English:** force is uh what's called moore's law which was named after uh gordon moore who's a berkeley  
**Translation:** 

**[438.54s] English:** alumnus and he made this observation very early in what are called semiconductors and semiconductors  
**Translation:** Vocabulary: alumnus: 校友; berkeley: 伯克利; semiconductors: 半导体

**[445.24s] English:** are these ideas you can build these very simple switches  
**Translation:** 

**[449.20s] English:** and you can put them on these microchips and he made this observation over 50 years ago he looked  
**Translation:** 

**[454.64s] English:** at a few years and said i think what's going to happen is the number of these little switches  
**Translation:** 

**[458.88s] English:** called transistors is going to double every year for the next decade and he said this in 1965 and  
**Translation:** Vocabulary: transistors: 晶体管

**[466.24s] English:** in 1975 he said well maybe it's going to double every two years and that what other people since  
**Translation:** 

**[474.00s] English:** named that moore's law guided the industry and when gordon moore made that prediction  
**Translation:** 

**[479.20s] English:** he he  
**Translation:** 

**[480.00s] English:** wrote a paper back in, I think in the, in the seventies and said, not only did this going to  
**Translation:** 

**[488.12s] English:** happen, he wrote, what would be the implications of that? And in this article from 1965, he,  
**Translation:** 

**[493.66s] English:** he shows ideas like computers being in cars and computers being in something that you would buy  
**Translation:** 

**[501.62s] English:** in the grocery store and stuff like that. So he kind of not only called his shot,  
**Translation:** 

**[506.02s] English:** he called the implications of it. So if you were in, in the computing field, and if you believed  
**Translation:** Vocabulary: computing: 计算机领域; grocery: 杂货店

**[511.90s] English:** Moore's prediction, he kind of said what the, what would be happening in the future. So, so it's not  
**Translation:** 

**[518.18s] English:** kind of, it's at one sense, this is what was predicted and you could imagine it was easy  
**Translation:** 

**[525.32s] English:** to believe that Moore's law was going to continue. And so this would be the implications. On the  
**Translation:** 

**[530.08s] English:** other side, there are these kind of shocking events in your life. Like I remember driving,  
**Translation:** 

**[536.02s] English:** driving in Marin across the Bay in San Francisco and seeing a bulletin board at a local  
**Translation:** 

**[541.92s] English:** civic center and it had a URL on it. And it was like, for all, for all, for the people at the time,  
**Translation:** Vocabulary: civic: 市民的; marin: 马林

**[549.56s] English:** these first URLs, and that's the, you know, WWW select stuff with the HTP, people thought it was  
**Translation:** 

**[555.76s] English:** look, look like alien, alien writing, right? They, you'd see these advertisements and commercials  
**Translation:** Vocabulary: alien: 外星的; commercials: 广告

**[563.50s] English:** or bulletin boards that had this alien writing on it. So for the latest,  
**Translation:** 

**[566.02s] English:** people was like, what the hell is going on here? And for those people in the industry, it was, oh my  
**Translation:** 

**[570.38s] English:** God, this stuff is getting so popular. It's actually leaking out of our nerdy world and into  
**Translation:** 

**[576.84s] English:** the real world. So that, I mean, there was events like that. I think another one was, I remember  
**Translation:** Vocabulary: nerdy: 书呆子的

**[581.50s] English:** with the, in the early days of the personal computer, when we started seeing advertisements  
**Translation:** 

**[585.46s] English:** in magazines for personal computers, like it's so popular that it's made the newspapers. So  
**Translation:** 

**[591.22s] English:** at one hand, you know, Gordon Moore predicted it and you kind of expected it to happen, but,  
**Translation:** 

**[596.02s] English:** when it really hit and you saw it affecting society, it was, it was,  
**Translation:** 

**[600.00s] English:** shocking so maybe uh taking a step back and looking both uh engineering and philosophical  
**Translation:** 

**[607.24s] English:** perspective what what do you see as the layers of abstraction in the computer do you see a computer  
**Translation:** Vocabulary: abstraction: 抽象; philosophical: 哲学的

**[613.32s] English:** as a a set of layers of abstractions yeah i think that's one of the things that uh computer science  
**Translation:** 

**[619.74s] English:** um fundamentals is the these things are really complicated in the way we cope with  
**Translation:** Vocabulary: abstractions: 抽象层; fundamentals: 基础知识

**[625.52s] English:** complicated software and complicated hardware is these layers of abstraction and that simply means  
**Translation:** 

**[631.14s] English:** that we uh you know suspend disbelief and pretend uh that the only thing you know is that layer and  
**Translation:** Vocabulary: disbelief: 不信

**[639.90s] English:** you don't know anything about the layer below it and that's the way we can make very complicated  
**Translation:** 

**[644.14s] English:** things and uh probably it started with hardware that's the way it was done but it's been proven  
**Translation:** 

**[651.18s] English:** extremely useful and you know i would say in a modern computer today  
**Translation:** 

**[655.52s] English:** there might be 10 or 20 layers of abstraction and they're all trying to kind of enforce this  
**Translation:** 

**[660.90s] English:** contract is all you know is this interface there's a set of um commands that you can are allowed to  
**Translation:** 

**[669.54s] English:** use and you stick to those commands and we will faithfully execute that and it's like peeling the  
**Translation:** Vocabulary: faithfully: 忠实地; interface: 接口

**[674.12s] English:** layers of a london of an onion you get down there's a new set of layers and so forth so for  
**Translation:** 

**[679.70s] English:** uh people who want to study computer science the exciting part about it  
**Translation:** 

**[685.52s] English:** is you can uh keep peeling those layers you you take your first course and you might learn to  
**Translation:** 

**[690.88s] English:** program in python and then you can take a follow-on course and you can get it down to  
**Translation:** 

**[695.84s] English:** a lower level language like c and you know you can go and then you can if you want to you can  
**Translation:** 

**[700.80s] English:** start getting into the hardware layers and you keep getting down all the way to that  
**Translation:** 

**[705.52s] English:** transistor that i talked about that gordon moore predicted and you can understand all  
**Translation:** 

**[710.96s] English:** those layers all the way up to the highest level application software so it's uh  
**Translation:** Vocabulary: transistor: 晶体管

**[715.52s] English:** It's a very kind of magnetic field.  
**Translation:** 

**[720.00s] English:** if you're interested you can go into any depth and keep going in particular what's happening  
**Translation:** 

**[726.30s] English:** right now or it's happened in software last 20 years and recently in hardware there's getting  
**Translation:** 

**[731.52s] English:** to be open source versions of all of these things so what open source means is what the engineer  
**Translation:** 

**[738.00s] English:** the programmer designs it's not secret uh the belonging to a company it's out there on the  
**Translation:** 

**[745.44s] English:** world wide web so you can see it so you can look at uh for lots of pieces of software that you use  
**Translation:** 

**[752.84s] English:** you can see exactly what the programmer does if you want to get involved that used to stop at the  
**Translation:** 

**[758.90s] English:** hardware recently there's been an effort to make open source hardware and those interfaces open  
**Translation:** Vocabulary: interfaces: 接口; programmer: 程序员

**[766.04s] English:** so you can see that so instead of before you had to stop at the hardware you can now start going  
**Translation:** 

**[770.32s] English:** layer by layer below that and see what's inside there so it's it's a remarkable  
**Translation:** 

**[775.22s] English:** thing to see and it's a remarkable thing to see and it's a remarkable thing to see and it's a  
**Translation:** 

**[775.42s] English:** time that for the interested individual can really see in great depth what's really going on in the  
**Translation:** 

**[781.60s] English:** computers that power everything uh that we see around us are you thinking also when you say  
**Translation:** 

**[787.18s] English:** open source at the hardware level is this going to the design architecture instruction set level  
**Translation:** 

**[793.76s] English:** or is it going to literally the the you know the manufacturer of the of the actual hardware of the  
**Translation:** 

**[803.42s] English:** actual chips whether that's asics specialized a particular domain or the general yeah so let's  
**Translation:** 

**[808.78s] English:** talk about that a little bit so when you get down to the bottom layer of uh software the way  
**Translation:** 

**[816.08s] English:** software talks to hardware is in a vocabulary and what we call that vocabulary we call that  
**Translation:** 

**[823.44s] English:** the words of that vocabulary called instructions and the technical term uh for the vocabulary is  
**Translation:** 

**[830.26s] English:** instruction set so those instructions are likely  
**Translation:** 

**[833.42s] English:** about earlier there can be instructions like add subtract and multiply divide there's instructions  
**Translation:** 

**[838.68s] English:** to put  
**Translation:** Vocabulary: multiply: 乘法; subtract: 减法

**[840.00s] English:** data into memory, which is called a store instruction, and to get data back, which is  
**Translation:** 

**[844.62s] English:** called a load instructions. And those simple instructions go back to the very dawn of  
**Translation:** 

**[849.74s] English:** computing. And in 1950, the commercial computer had these instructions. So that's the instruction  
**Translation:** 

**[855.64s] English:** set that we're talking about. So up until, I'd say, 10 years ago, these instruction sets were  
**Translation:** 

**[861.80s] English:** all proprietary. So a very popular one is owned by Intel, the one that's in the cloud and in all  
**Translation:** 

**[869.12s] English:** the PCs in the world. Intel owns that instruction set. It's referred to as the x86. There have been  
**Translation:** Vocabulary: proprietary: 专有技术

**[875.80s] English:** a sequence of ones that the first number was called 8086. And since then, there's been a lot  
**Translation:** 

**[881.16s] English:** of numbers, but they all end in 86. So there's been that kind of family of instruction sets.  
**Translation:** 

**[888.12s] English:** And that's proprietary.  
**Translation:** 

**[889.40s] English:** And that's proprietary. The other one that's very popular is from ARM. That kind of powers  
**Translation:** 

**[895.62s] English:** all the cell phones in the world, all the iPads in the world.  
**Translation:** 

**[899.12s] English:** And a lot of things that are so-called Internet of Things devices, ARM, and that one is also  
**Translation:** 

**[907.04s] English:** proprietary. ARM will license it to people for a fee, but they own that. So the new idea that  
**Translation:** 

**[913.48s] English:** got started at Berkeley kind of unintentionally 10 years ago is, early in my career, we pioneered  
**Translation:** Vocabulary: berkeley: 伯克利; pioneered: 开创; unintentionally: 无意中

**[921.96s] English:** a way to do these vocabularies instruction sets that was very controversial at the time.  
**Translation:** 

**[927.80s] English:** At the time, in the 19th century, we had a lot of people that were very, very, very, very, very,  
**Translation:** 

**[929.12s] English:** in the 1980s, conventional wisdom was these vocabularies instruction sets should have  
**Translation:** 

**[934.34s] English:** powerful instructions. So polysyllabic kind of words, you can think of that.  
**Translation:** Vocabulary: polysyllabic: 多音节的

**[940.62s] English:** And so instead of just add, subtract, and multiply, they would have polynomial divide or  
**Translation:** 

**[946.18s] English:** sort a list. And the hope was of those powerful vocabularies, that'd make it easier for software.  
**Translation:** 

**[954.48s] English:** So we thought that didn't make sense for microprocessors. There was people  
**Translation:** 

**[958.36s] English:** at Berkeley who were very, very, very, very, very, very, very, very, very, very, very, very, very,  
**Translation:** Vocabulary: microprocessors: 微处理器

**[959.12s] English:** very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very  
**Translation:** 

**[960.00s] English:** IBM, who argued the opposite. And what we called that was a reduced instruction set computer. And  
**Translation:** 

**[966.52s] English:** the abbreviation was RISC. And typical for computer people, we use the abbreviation and  
**Translation:** 

**[972.48s] English:** start pronouncing it. So RISC was the thing. So we said for microprocessors, which with Gordon's  
**Translation:** Vocabulary: abbreviation: 缩写

**[978.00s] English:** Moore is changing really fast, we think it's better to have a pretty simple set of instructions,  
**Translation:** 

**[984.86s] English:** reduced set of instructions, that that would be a better way to build microprocessors since  
**Translation:** 

**[989.78s] English:** they're going to be changing so fast due to Moore's law. And then we'll just use standard  
**Translation:** 

**[994.22s] English:** software to generate more of those simple instructions. And one of the pieces of  
**Translation:** 

**[1002.80s] English:** software that's in that software stack going between these layers of abstractions is called  
**Translation:** 

**[1007.40s] English:** a compiler. And it basically translates. It's a translator between levels. We said the translator  
**Translation:** Vocabulary: abstractions: 抽象层; translator: 翻译器

**[1012.20s] English:** will handle that. So the technical question was, well, since there are these reduced instructions,  
**Translation:** 

**[1019.22s] English:** you have to  
**Translation:** 

**[1019.60s] English:** execute more of them. Yeah, that's right. But maybe you execute them faster. Yeah, that's right.  
**Translation:** 

**[1024.74s] English:** They're simpler, so they go faster, but you have to do more of them. So what's that trade-off look  
**Translation:** 

**[1029.54s] English:** like? And it ended up that we ended up executing maybe 50% more instructions, maybe a third more  
**Translation:** 

**[1037.08s] English:** instructions, but they ran four times faster. So this RISC, controversial RISC ideas proved to be  
**Translation:** 

**[1044.48s] English:** maybe factors of three or four better. I love that this idea was controversial.  
**Translation:** 

**[1049.60s] English:** And almost kind of like rebellious. So that's in the context of what was more  
**Translation:** Vocabulary: rebellious: 叛逆的

**[1055.08s] English:** conventional is the complex instructional set computing. So how would you pronounce that?  
**Translation:** 

**[1061.46s] English:** CISC.  
**Translation:** Vocabulary: computing: 计算机; instructional: 指令的

**[1061.78s] English:** CISC, which is RISC.  
**Translation:** 

**[1063.02s] English:** RISC versus CISC. And believe it or not, this sounds very, very, who cares about this, right?  
**Translation:** 

**[1070.32s] English:** It was violently debated at several conferences. It's like, what's the right way to go? And people  
**Translation:** 

**[1077.44s] English:** thought RISC was, you know, was...  
**Translation:** Vocabulary: conferences: 会议

**[1079.60s] English:** A deal.  
**Translation:** 

**[1080.00s] English:** evolution. We're going to make software worse by making those instructions simpler. And there are  
**Translation:** 

**[1085.12s] English:** fierce debates at several conferences in the 1980s. And then later in the 80s, it kind of  
**Translation:** 

**[1091.58s] English:** settled to these benefits. It's not completely intuitive to me why risk has, for the most part,  
**Translation:** Vocabulary: intuitive: 直观的

**[1098.22s] English:** won. Yeah. So why did that happen? Yeah. Yeah. And maybe I can sort of say a bunch of dumb things  
**Translation:** 

**[1104.30s] English:** that could lay the land for further commentary. So to me, this is kind of interesting thing. If  
**Translation:** 

**[1110.86s] English:** you look at C++ versus C, with modern compilers, you really could write faster code with C++.  
**Translation:** 

**[1118.74s] English:** So relying on the compiler to reduce your complicated code into something simple and fast.  
**Translation:** Vocabulary: compilers: 编译器

**[1124.94s] English:** So to me, comparing risk, maybe this is a dumb question, but why is it that focusing the  
**Translation:** 

**[1133.46s] English:** definition that does not have a risk factor is so important?  
**Translation:** 

**[1134.30s] English:** The design of the instruction set on very few simple instructions in the long run provide  
**Translation:** 

**[1140.78s] English:** faster execution versus coming up with, like you said, a ton of complicated instructions  
**Translation:** 

**[1149.42s] English:** that over time, you know, years, maybe decades, you come up with compilers that can reduce those  
**Translation:** 

**[1156.22s] English:** into simple instructions for you. Yeah. So let's try and split that into two pieces.  
**Translation:** 

**[1161.60s] English:** So if the compiler can do that for you, if the compiler can take, you know, a complicated program  
**Translation:** 

**[1169.16s] English:** and produce simpler instructions, then the programmer doesn't care, right? Programmer,  
**Translation:** Vocabulary: programmer: 编程人员

**[1176.48s] English:** I don't care just how fast is the computer I'm using, how much does it cost? And so what happened  
**Translation:** 

**[1183.78s] English:** kind of in the software industry is right around before the 1980s, critical pieces of software were  
**Translation:** 

**[1190.44s] English:** still written by the computer. And so the computer was able to do that. And so the computer was able  
**Translation:** 

**[1191.60s] English:** to do that. And so the computer was able to do that. And so the computer was able to do that.  
**Translation:** 

**[1191.66s] English:** Not in languages like C or C++, they were written in what's called assembly language,  
**Translation:** 

**[1197.98s] English:** where there's this kind of human's  
**Translation:** 

**[1200.00s] English:** writing exactly at the instructions at the level that a computer can understand. So they were  
**Translation:** 

**[1206.22s] English:** writing add, subtract, multiply, you know, instructions. It's very tedious. But the belief  
**Translation:** Vocabulary: multiply: 乘法; subtract: 减法; tedious: 繁琐

**[1212.88s] English:** was to write this lowest level of software that people use, which are called operating systems,  
**Translation:** 

**[1218.84s] English:** they had to be written in a semi-language because these high-level languages were just too  
**Translation:** 

**[1223.04s] English:** inefficient. They were too slow or the programs would be too big. So that changed with a famous  
**Translation:** 

**[1232.46s] English:** operating system called Unix, which is kind of the grandfather of all the operating systems today.  
**Translation:** Vocabulary: inefficient: 低效

**[1238.80s] English:** So Unix demonstrated that you could write something as complicated as an operating system  
**Translation:** 

**[1243.86s] English:** in a language like C. So once that was true, then that meant we could hide the instruction set  
**Translation:** 

**[1251.54s] English:** from the programmer.  
**Translation:** 

**[1253.04s] English:** And so that meant then it didn't really matter. The programmer didn't have to write  
**Translation:** 

**[1258.64s] English:** lots of these simple instructions. That was up to the compiler. So that was part of our  
**Translation:** 

**[1263.14s] English:** arguments for risk is if you were still writing an assembly language, there's maybe a better case  
**Translation:** 

**[1267.60s] English:** for sys constructions. But if the compiler can do that, it's going to be, you know, that's done  
**Translation:** 

**[1273.12s] English:** once. The computer translates it once. And then every time you run the program, it runs at this  
**Translation:** Vocabulary: constructions: 构造

**[1279.24s] English:** potentially simpler instructions.  
**Translation:** 

**[1282.14s] English:** And so that was  
**Translation:** 

**[1282.96s] English:** the reason why we were able to do that.  
**Translation:** 

**[1283.04s] English:** The debate, right, is because people would acknowledge that the simpler instructions  
**Translation:** 

**[1288.78s] English:** could lead to a faster computer. You can think of monosyllabic instructions. You could say them,  
**Translation:** 

**[1294.26s] English:** you know, if you think of reading, you probably read them faster or say them faster than  
**Translation:** Vocabulary: monosyllabic: 单音节的

**[1298.06s] English:** long instructions. The same thing. That analogy works pretty well for hardware.  
**Translation:** 

**[1302.50s] English:** And as long as you didn't have to read a lot more of those instructions, you could win.  
**Translation:** 

**[1306.90s] English:** So that's that's that's the basic idea for risk.  
**Translation:** 

**[1309.90s] English:** But it's interesting that in that discussion,  
**Translation:** 

**[1312.78s] English:** you know, Unix and see that there's only one step of levels of abstraction from the.  
**Translation:** 

**[1320.00s] English:** code that's really the closest to the machine to the code that's written by human it's uh at least  
**Translation:** Vocabulary: abstraction: 抽象

**[1326.80s] English:** to me again perhaps a dumb intuition but it feels like there might have been more layers sort of  
**Translation:** 

**[1333.68s] English:** different kinds of humans stacked well of each other um so what's true and not true about what  
**Translation:** Vocabulary: intuition: 直觉

**[1339.68s] English:** you said is several of the layers of software like so the the if you here two layers would be  
**Translation:** 

**[1351.20s] English:** suppose we just talk about two layers that would be the operating system like you get from  
**Translation:** 

**[1355.36s] English:** from microsoft or from apple like ios or the windows operating system and let's say  
**Translation:** 

**[1361.92s] English:** applications that run on top of it like word or excel so both the operating system could be  
**Translation:** 

**[1369.44s] English:** written with the operating system but it's not the operating system that's going to be written  
**Translation:** 

**[1369.68s] English:** in c and the application could be written in c so but you could construct those two layers and the  
**Translation:** 

**[1377.04s] English:** applications absolutely do call upon the operating system and the the change was that both of them  
**Translation:** 

**[1382.80s] English:** could be written in higher level languages so it's one step of a translation but you can still build  
**Translation:** 

**[1387.92s] English:** many layers of abstraction of software on top of that and that's how how things are done today so  
**Translation:** 

**[1393.76s] English:** uh still today many of the layers that you'll you'll deal with you may deal with debuggers you  
**Translation:** 

**[1402.32s] English:** may deal with linkers um there's libraries many of those today will be written in c plus plus say uh  
**Translation:** 

**[1412.40s] English:** even though that language is pretty ancient and even the python interpreter is probably written  
**Translation:** Vocabulary: interpreter: 解释器

**[1418.72s] English:** in c or c plus plus so lots of layers there are probably written in these uh  
**Translation:** 

**[1424.32s] English:** some old-fashioned efficient languages that still take one step to produce these instructions  
**Translation:** 

**[1433.36s] English:** produce risk instructions but they're composed each layer of software invokes one another through  
**Translation:** 

**[1439.44s] English:** these  
**Translation:** 

**[1440.00s] English:** interfaces and you can get 10 layers of software that way so in general the risk was developed here  
**Translation:** 

**[1446.48s] English:** berkeley it was uh kind of the three places that were these radicals that advocated for  
**Translation:** Vocabulary: advocated: 提倡; interfaces: 接口; radicals: 激进分子

**[1453.20s] English:** this against the rest of the community were ibm berkeley and stanford uh you're one of these  
**Translation:** 

**[1459.12s] English:** radicals and how radical did you feel how confident did you feel how doubtful were you that  
**Translation:** Vocabulary: doubtful: 怀疑; stanford: 斯坦福大学

**[1469.60s] English:** risk might be the right approach because it may you can also into it that is kind of taking a  
**Translation:** 

**[1474.80s] English:** step back into simplicity not forward into simplicity yeah no it was easy to make uh  
**Translation:** Vocabulary: simplicity: 简单性

**[1482.00s] English:** yeah it was easy to make the argument against it well this was my colleague john hennessey  
**Translation:** 

**[1487.36s] English:** at stanford and i we were both assistant professors and for me i i just believed in  
**Translation:** Vocabulary: colleague: 同事; hennessey: 亨内斯利

**[1493.28s] English:** the power of our ideas i thought what we were saying made sense morris law is going to move fast  
**Translation:** 

**[1500.00s] English:** the other thing that i didn't mention is one of the surprises of these complex instruction sets  
**Translation:** 

**[1505.60s] English:** you could certainly write these complex instructions if the programmer is writing  
**Translation:** 

**[1509.28s] English:** them themselves it turned out to be kind of difficult for the compiler to generate those  
**Translation:** Vocabulary: programmer: 编程人员

**[1514.72s] English:** complex instructions kind of ironically you'd have to find the right circumstances that that  
**Translation:** 

**[1519.92s] English:** just exactly fit this complex instruction it was actually easier for the compiler  
**Translation:** Vocabulary: ironically: 适得其反

**[1523.60s] English:** to generate these simple instructions so not only did these complex instructions make the hardware  
**Translation:** 

**[1529.60s] English:** more difficult to build often the compiler wouldn't even use them and so it's harder to  
**Translation:** 

**[1535.92s] English:** build the compiler doesn't use them that much the simple instructions go better with moore's law  
**Translation:** 

**[1541.60s] English:** that's you know the number of transistors is doubling every every two years so we're gonna  
**Translation:** Vocabulary: transistors: 晶体管

**[1545.68s] English:** have you know the you wanna reduce the time to design the microprocessor that may be more important  
**Translation:** 

**[1551.36s] English:** than these number of instructions so i think we believed in the um that we were right that this  
**Translation:** Vocabulary: microprocessor: 微处理器; wanna: 想要

**[1555.92s] English:** 161 106 00е 00? Wordpress.com  
**Translation:** 

**[1556.98s] English:** 00? Wordpress.com 100tz вaci 100tz вaci 00? Wordpress.com 608 00e 00? Wordpress.com 708 000? Wordpress.com led the way to justification,  
**Translation:** 

**[1557.32s] English:** That this was the best idea then the question  
**Translation:** 

**[1560.00s] English:** became in these debates well yeah that's a good technical idea but in the business world this  
**Translation:** 

**[1565.56s] English:** doesn't matter there's other things that matter it's like uh arguing that uh if there's a standard  
**Translation:** 

**[1571.72s] English:** with the railroad tracks and you've come up with a better with but the whole world is covered in  
**Translation:** 

**[1576.74s] English:** railroad tracks so you'll your ideas have no chance of success right commercial success it  
**Translation:** 

**[1582.30s] English:** was technically right but commercially it'll be insignificant yeah there's it's kind of sad  
**Translation:** Vocabulary: commercially: 商业上

**[1587.04s] English:** that this world the history of human civilization is full of good ideas that uh lost because  
**Translation:** 

**[1594.14s] English:** somebody else came along first with a worse idea and it's good that in the computing world at least  
**Translation:** Vocabulary: computing: 计算机领域

**[1600.24s] English:** some of these have well you could i mean there's probably still cisc people that say uh yeah  
**Translation:** 

**[1605.52s] English:** well and what happened was what was interesting uh intel a bunch of the cisc uh companies with cisc  
**Translation:** 

**[1613.88s] English:** instruction sets of vocabulary they gave up  
**Translation:** 

**[1617.04s] English:** but not intel what intel did to its credit because intel's vocabulary was  
**Translation:** 

**[1624.24s] English:** in the in the personal computer and so that was a very valuable vocabulary because the way we  
**Translation:** 

**[1630.48s] English:** distribute software is in those actual instructions it's in the instructions of that instruction set  
**Translation:** 

**[1636.18s] English:** so uh they they you don't get that source code what the programmers wrote you get after it's  
**Translation:** 

**[1642.06s] English:** been translated into the lowest level that's if you were to get a floppy disk or download  
**Translation:** Vocabulary: floppy: 软盘; programmers: 程序员

**[1646.66s] English:** software you're going to get a floppy disk and you're going to get a floppy disk and you're going  
**Translation:** 

**[1647.02s] English:** to get a floppy disk and you're going to get a floppy disk and you're going to get a floppy disk and so forth so  
**Translation:** 

**[1650.04s] English:** the x86 instruction set was very valuable so what intel did cleverly and amazingly is they had their  
**Translation:** 

**[1658.08s] English:** chips in hardware do a translation step they would take these complex instructions and translate them  
**Translation:** 

**[1664.82s] English:** into essentially in risk instructions in hardware on the fly you know at at gigahertz clock speeds  
**Translation:** 

**[1670.98s] English:** and then any good idea that risk people had they could use and they could still be compatible with  
**Translation:** Vocabulary: compatible: 兼容; gigahertz: 吉赫兹

**[1676.76s] English:** this  
**Translation:** 

**[1677.02s] English:** with this really valuable  
**Translation:** 

**[1680.00s] English:** pc software software base and which also had very high volumes you know 100 million personal  
**Translation:** 

**[1686.24s] English:** computers per year so the cisc architecture in the business world was actually one in in this pc era  
**Translation:** 

**[1695.04s] English:** so just going back to the the time of designing risk when you design an instruction set  
**Translation:** 

**[1706.02s] English:** architecture do you think like a programmer do you think like a microprocessor engineer  
**Translation:** Vocabulary: microprocessor: 微处理器; programmer: 程序员

**[1711.50s] English:** do you think like a artist a philosopher do you think in software and hardware i mean is it art  
**Translation:** 

**[1719.60s] English:** is it science yeah i'd say i think designing a good instruction set is an art and i think you're  
**Translation:** 

**[1726.12s] English:** trying to uh balance um the the simplicity and speed of execution with how well easy  
**Translation:** 

**[1736.00s] English:** you can do it and how well you can do it and how well you can do it and how well you can do it and  
**Translation:** Vocabulary: simplicity: 简单性

**[1736.02s] English:** how easy it will be for compilers to use it right you're trying to create an instruction set  
**Translation:** 

**[1740.40s] English:** that everything in there can be used by compilers there's not things that are missing that'll make  
**Translation:** Vocabulary: compilers: 编译器

**[1747.88s] English:** it difficult for the program to run they run efficiently but you want it to be easy to build  
**Translation:** 

**[1753.30s] English:** as well so it's that kind of so you're thinking i'd say you're thinking hardware trying to find  
**Translation:** Vocabulary: efficiently: 运行高效

**[1757.48s] English:** a hard software compromise that'll work well and and it's uh you know it's you know it's a matter  
**Translation:** 

**[1764.32s] English:** of taste right it's  
**Translation:** 

**[1766.00s] English:** it's kind of fun to build instruction sets it's not that hard to build an instruction set but  
**Translation:** 

**[1771.74s] English:** to build one that catches on and people use you know you have to be you know fortunate to be the  
**Translation:** 

**[1778.10s] English:** right place in the right time or have a design that people really like are you using metrics  
**Translation:** 

**[1783.22s] English:** so is it uh quantifiable because you kind of have to anticipate the kind of programs that people  
**Translation:** Vocabulary: anticipate: 预测; quantifiable: 可量化

**[1789.18s] English:** write yeah ahead of time so is that can you use numbers can you use metrics can you quantify  
**Translation:** 

**[1795.26s] English:** something ahead of time so that's kind of fun to build instruction sets it's kind of fun to build  
**Translation:** Vocabulary: quantify: 量化

**[1795.98s] English:** ahead of time or is this again that's the art part where you're kind of no it's uh  
**Translation:** 

**[1800.00s] English:** A big change, kind of what happened, I think, from Hennessy's and my perspective in the 1980s, what happened was going from kind of really, you know, taste and hunches to quantifiable.  
**Translation:** 

**[1816.58s] English:** And in fact, he and I wrote a textbook at the end of the 1980s called Computer Architecture, a Quantitative Approach.  
**Translation:** 

**[1823.36s] English:** I heard of that. And it's the thing, it had a pretty big impact in the field because we went from textbooks that kind of listed, so here's what this computer does, and here's the pros and cons, and here's what this computer does and pros and cons, to something where there were formulas and equations where you could measure things.  
**Translation:** Vocabulary: equations: 数学方程; formulas: 公式; quantitative: 定量的

**[1842.30s] English:** So specifically for instruction sets, what we do and some other fields do is we agree upon a set of programs, which we call benchmarks.  
**Translation:** 

**[1853.36s] English:** And a suite of programs, and then you develop both the hardware and the compiler, and you get numbers on how well your computer does, given its instruction set and how well you implemented it in your microprocessor and how good your compilers are.  
**Translation:** Vocabulary: benchmarks: 参考测试; microprocessor: 微处理器

**[1872.64s] English:** In computer architecture, you know, using professor's terms, we grade on a curve rather than grade on an absolute scale.  
**Translation:** 

**[1879.22s] English:** So when you say, you know, these programs run this fast, well, that's kind of incorrect.  
**Translation:** 

**[1883.36s] English:** It's interesting, but how do you know it's better?  
**Translation:** 

**[1885.22s] English:** Well, you compare it to other computers of the same time.  
**Translation:** 

**[1888.62s] English:** So the best way we know how to make, turn it into a kind of more science and experimental and quantitative is to compare yourself to other computers of the same era that have the same access, the same kind of technology on commonly agreed benchmark programs.  
**Translation:** 

**[1905.62s] English:** So maybe to toss up two possible directions we can go, one is what are the different trade-offs in designing?  
**Translation:** Vocabulary: benchmark: 参考标准

**[1913.36s] English:** Architecture is, we've been already talking about risk and risk, but maybe a little bit more detail in terms of specific.  
**Translation:** 

**[1920.00s] English:** features that you were thinking about and the other side is what are the metrics that you're  
**Translation:** 

**[1925.18s] English:** thinking about when looking at these trade-offs yeah let's talk about the metrics so during these  
**Translation:** 

**[1932.28s] English:** debates we actually had kind of a hard time explaining convincing people the ideas and  
**Translation:** 

**[1937.14s] English:** partly we didn't have a formula to explain it and a few years into it we hit upon the formula  
**Translation:** 

**[1943.18s] English:** that helped explain what was going on and um i think if we can do this see how it works orally  
**Translation:** 

**[1949.84s] English:** so uh the is if i can do a formula orally let's see so the uh so fundamentally uh the way you  
**Translation:** 

**[1958.78s] English:** measure performance is how long does it take a program to run a program if you have 10 programs  
**Translation:** Vocabulary: fundamentally: 根本上

**[1964.92s] English:** and typically these benchmarks were sweet because you'd want to have 10 programs so they could  
**Translation:** 

**[1969.24s] English:** represent lots of different applications so for these 10 programs how long did it take to run  
**Translation:** 

**[1973.78s] English:** well now when you're trying to explain why it took so long you could factor how long it takes a  
**Translation:** 

**[1979.18s] English:** program to run  
**Translation:** 

**[1979.84s] English:** into three factors uh one of the first one is how many instructions did it take to execute  
**Translation:** 

**[1986.84s] English:** so that's the that's the what we've been talking about you know the instructions of academy how  
**Translation:** 

**[1991.36s] English:** many did it take all right the next question is how long did each instruction take to run  
**Translation:** 

**[1997.70s] English:** on average so you'd multiply the number of instructions times how long it took to run  
**Translation:** Vocabulary: multiply: 相乘

**[2002.68s] English:** and that gets you how time okay so that's but now let's look at this metric of how long did  
**Translation:** 

**[2008.76s] English:** it take the instruction to run  
**Translation:** 

**[2009.84s] English:** well it turns out the way we could build computers today is they all have a clock and you've seen  
**Translation:** 

**[2015.92s] English:** this when you if you buy a microprocessor it'll say 3.1 gigahertz or 2.5 gigahertz and more  
**Translation:** Vocabulary: gigahertz: 吉赫兹; microprocessor: 微处理器

**[2022.62s] English:** gigahertz is good well what that is is the speed of the clock so 2.5 gigahertz turns out to be  
**Translation:** 

**[2029.80s] English:** four billionths of instruction or four nanoseconds so that's the clock cycle time  
**Translation:** Vocabulary: billionths: 十亿分之一; nanoseconds: 纳秒

**[2034.90s] English:** but there's another factor which is what's the average number of clocked  
**Translation:** 

**[2039.84s] English:** cycles  
**Translation:** 

**[2040.00s] English:** it takes per instruction. So it's number of instructions, average number of clock cycles,  
**Translation:** 

**[2044.80s] English:** and the clock cycle time. So in these risk-sys debates, they would concentrate on, but risk  
**Translation:** 

**[2051.50s] English:** needs to take more instructions. And we'd argue that maybe the clock cycle is faster. But what  
**Translation:** 

**[2057.14s] English:** the real big difference was, was the number of clock cycles per instruction.  
**Translation:** 

**[2061.30s] English:** Per instruction, that's fascinating. What about the beautiful mess of parallelism in the whole  
**Translation:** 

**[2066.20s] English:** picture? Parallelism, which has to do with, say, how many instructions could execute in parallel  
**Translation:** 

**[2071.20s] English:** and things like that. You could think of that as affecting the clock cycles per instruction,  
**Translation:** 

**[2075.56s] English:** because it's the average clock cycles per instruction. So when you're running a program,  
**Translation:** 

**[2079.42s] English:** if it took 100 billion instructions, and on average, it took two clock cycles per instruction,  
**Translation:** 

**[2086.00s] English:** and they were four nanoseconds, you could multiply that out and see how long it took to run.  
**Translation:** 

**[2089.70s] English:** And there's all kinds of tricks to try and reduce the number of clock cycles per instruction.  
**Translation:** 

**[2095.34s] English:** But it turns...  
**Translation:** 

**[2096.20s] English:** It turned out that the way they would do these complex instructions is they would actually build  
**Translation:** 

**[2100.76s] English:** what we would call an interpreter, and a simpler, a very simple hardware interpreter. But it turned  
**Translation:** Vocabulary: interpreter: 解释器

**[2106.46s] English:** out that for the sys constructions, if you had to use one of those interpreters, it would be like  
**Translation:** 

**[2111.46s] English:** 10 clock cycles per instruction, where the risk constructions could be two. So there'd be this  
**Translation:** Vocabulary: constructions: 构造; interpreters: 解释器

**[2116.80s] English:** factor of five advantage in clock cycles per instruction. We have to execute, say, 25 or 50%  
**Translation:** 

**[2122.80s] English:** more instructions. So that's where the win would come. And then you could make an argument,  
**Translation:** 

**[2126.20s] English:** whether the clock cycle times are the same or not. But pointing out that we could divide  
**Translation:** 

**[2130.86s] English:** the benchmark results, time per program, into three factors. And the biggest difference in  
**Translation:** Vocabulary: benchmark: 参考基准

**[2136.68s] English:** risk and sys was the clock cycles per... You execute a few more instructions, but the clock  
**Translation:** 

**[2141.22s] English:** cycles per instruction is much less. And that was what this debate... Once we made that argument,  
**Translation:** 

**[2147.48s] English:** then people said, oh, okay, I get it. And so we went from... It was outrageously controversial in  
**Translation:** 

**[2155.32s] English:** 1982.  
**Translation:** 

**[2156.20s] English:** That maybe probably by 1984 or so, people said, oh, yeah.  
**Translation:** 

**[2160.00s] English:** technically, they've got a good argument. What are the instructions in the risk instruction set,  
**Translation:** 

**[2166.22s] English:** just to get an intuition? Okay. 1995, I was asked to predict the future of what microprocessor  
**Translation:** 

**[2174.08s] English:** future. So, I'd seen these predictions, and usually people predict something outrageous  
**Translation:** Vocabulary: intuition: 直觉; microprocessor: 微处理器; outrageous: 离谱的

**[2180.58s] English:** just to be entertaining, right? And so, my prediction for 2020 was, you know, things are  
**Translation:** 

**[2186.54s] English:** going to be pretty much, they're going to look very familiar to what they are, and they are.  
**Translation:** 

**[2190.78s] English:** And if you were to read the article, you know, the things I said are pretty much true. The  
**Translation:** 

**[2194.92s] English:** instructions that have been around forever are kind of the same. And that's the outrageous  
**Translation:** 

**[2199.32s] English:** prediction, actually. Yeah. Given how fast computers have been growing. Well, and, you know,  
**Translation:** 

**[2202.78s] English:** Morse law was going to go on, we thought, for 25 more years. You know, who knows? But kind of the  
**Translation:** 

**[2208.38s] English:** surprising thing, in fact, you know, Hennessy and I, you know, won the ACM AM Touring Award for both  
**Translation:** 

**[2215.98s] English:** the risk control and the risk control. And, you know, we're going to be talking about the  
**Translation:** Vocabulary: hennessy: 汉尼森

**[2216.54s] English:** construction set contributions and for that textbook I mentioned. But, you know, we're  
**Translation:** 

**[2220.50s] English:** surprised that here we are 35, 40 years later after we did our work. And the conventionalism  
**Translation:** Vocabulary: conventionalism: 惯例主义

**[2230.30s] English:** of the best way to do instruction sets is still those risk construction sets that look very  
**Translation:** 

**[2235.14s] English:** similar to what we looked like, you know, we did in the 1980s. So, those, surprisingly, there hasn't  
**Translation:** 

**[2241.22s] English:** been some radical new idea, even though we have, you know, a million times as many transition  
**Translation:** 

**[2246.54s] English:** features as we had back then. But what are the basic constructions and how did they change over  
**Translation:** Vocabulary: constructions: 基本结构

**[2252.62s] English:** the years? So, are we talking about addition, subtraction? These are the... Okay, the specific...  
**Translation:** 

**[2257.06s] English:** So, the things that are in a calculator are in a computer. So, any of the buttons that are in the  
**Translation:** Vocabulary: subtraction: 减法

**[2263.12s] English:** calculator in the computer. So, if there's a memory function key, and like I said, those are  
**Translation:** 

**[2269.18s] English:** turns into putting something in memory is called a store, brings something back, it's called load.  
**Translation:** 

**[2272.60s] English:** Just a quick tangent. When you say memory, what does memory mean?  
**Translation:** 

**[2276.54s] English:** Well, I told you there were five pieces of a computer.  
**Translation:** Vocabulary: tangent: 旁枝逸出

**[2280.60s] English:** And if you remember in a calculator, there's a memory key.  
**Translation:** 

**[2283.46s] English:** So you want to have intermediate calculation and bring it back later.  
**Translation:** 

**[2286.50s] English:** So you'd hit the memory plus key, M plus maybe, and it would put that into memory.  
**Translation:** 

**[2290.88s] English:** And then you'd hit an RM like recurrent instruction and then bring it back into the display.  
**Translation:** Vocabulary: recurrent: 循环指令

**[2295.12s] English:** So you don't have to type it.  
**Translation:** 

**[2296.24s] English:** You don't have to write it down and bring it back again.  
**Translation:** 

**[2297.92s] English:** So that's exactly what memory is.  
**Translation:** 

**[2299.68s] English:** You can put things into it as temporary storage and bring it back when you need it later.  
**Translation:** 

**[2305.32s] English:** So that's memory and loads and stores.  
**Translation:** 

**[2307.22s] English:** But the big thing, the difference between a computer and a calculator is that the computer can make decisions.  
**Translation:** 

**[2314.84s] English:** And amazingly, decisions are as simple as, is this value less than zero or is this value bigger than that value?  
**Translation:** 

**[2323.02s] English:** So there's those instructions, which are called conditional branch instructions, is what give computers all its power.  
**Translation:** Vocabulary: conditional: 条件

**[2329.88s] English:** If you were in the early days of computing before what's called the general purpose microprocessor,  
**Translation:** 

**[2335.14s] English:** people would write these instructions.  
**Translation:** Vocabulary: computing: 计算; microprocessor: 微处理器

**[2337.84s] English:** Kind of in hardware, but it couldn't make decisions.  
**Translation:** 

**[2341.64s] English:** It would just, it would do the same thing over and over again.  
**Translation:** 

**[2345.44s] English:** With the power of having branch instructions, it can look at things and make decisions automatically.  
**Translation:** 

**[2350.50s] English:** And it can make these decisions, you know, billions of times per second.  
**Translation:** 

**[2353.66s] English:** And amazingly enough, we can get, you know, thanks to advanced machine learning,  
**Translation:** 

**[2358.12s] English:** we can create programs that can do something smarter than human beings can do.  
**Translation:** 

**[2362.82s] English:** But if you go down that very basic level, it's the instructions are the keys.  
**Translation:** 

**[2367.04s] English:** It's on the calculator plus the ability to make decisions of these conditional branch instructions.  
**Translation:** 

**[2371.96s] English:** And all decisions fundamentally can be reduced down to these branch instructions.  
**Translation:** 

**[2376.78s] English:** Yeah.  
**Translation:** Vocabulary: fundamentally: 从根本上

**[2377.10s] English:** So in fact, and so, you know, going way back in the stack, back to, you know,  
**Translation:** 

**[2382.34s] English:** we did four risk projects at Berkeley in the 1980s.  
**Translation:** Vocabulary: berkeley: 伯克利

**[2385.60s] English:** They did a couple at Stanford in the 1980s.  
**Translation:** 

**[2388.64s] English:** In 2010, we decided we wanted to do a new instruction set,  
**Translation:** Vocabulary: stanford: 斯坦福大学

**[2393.82s] English:** learning from the mistakes of those risk architectures in 1980.  
**Translation:** 

**[2397.04s] English:** And that was done here at Berkeley.  
**Translation:** 

**[2400.00s] English:** almost exactly 10 years ago, and the people who did it, I participated, but Krista Sanovich and  
**Translation:** 

**[2406.74s] English:** others drove it. They called it RISC-V to honor the four RISC projects of the 1980s.  
**Translation:** 

**[2413.62s] English:** So what does RISC-V involve? So RISC-V is another instruction set of vocabulary. It's  
**Translation:** 

**[2420.42s] English:** learned from the mistakes of the past, but it still has, if you look at the, there's a core  
**Translation:** 

**[2424.98s] English:** set of instructions. It's very similar to the simplest architectures from the 1980s,  
**Translation:** 

**[2429.56s] English:** and the big difference about RISC-V is it's open. So I talked earlier about proprietary versus  
**Translation:** Vocabulary: proprietary: 私有产权

**[2435.76s] English:** open software. So this is an instruction set, so it's a vocabulary. It's not hardware,  
**Translation:** 

**[2445.12s] English:** but by having an open instruction set, we can have open source implementations,  
**Translation:** Vocabulary: implementations: 实现方式

**[2450.28s] English:** open source processors that people can use.  
**Translation:** 

**[2453.56s] English:** Where do you see that?  
**Translation:** Vocabulary: processors: 处理器

**[2454.98s] English:** Going, it's a really exciting possibility, but just like in the Scientific American,  
**Translation:** 

**[2460.22s] English:** if you were to predict 10, 20, 30 years from now, that kind of ability to utilize open source  
**Translation:** 

**[2467.20s] English:** instruction set architectures like RISC-V, what kind of possibilities might that unlock?  
**Translation:** 

**[2473.72s] English:** Yeah, and so just to make it clear, because this is confusing, the specification of RISC-V is  
**Translation:** Vocabulary: specification: 规范说明

**[2480.42s] English:** something that's like in a textbook. There's books about it. So that's what,  
**Translation:** 

**[2484.98s] English:** defining an interface. There's also the way you build hardware is you write it in languages.  
**Translation:** Vocabulary: interface: 接口规范

**[2491.68s] English:** They're kind of like C, but they're specialized for hardware that gets translated into hardware.  
**Translation:** 

**[2498.24s] English:** And so these implementations of this specification are what are the open source. So they're written  
**Translation:** 

**[2504.48s] English:** in something that's called Verilog or VHDL, but it's put up on the web, just like you can see the  
**Translation:** 

**[2510.84s] English:** C++ code for Linux on the web.  
**Translation:** 

**[2514.78s] English:** So that's what it's called.  
**Translation:** 

**[2514.96s] English:** That's the open instruction set enables open source implementations.  
**Translation:** 

**[2520.00s] English:** of RISC-V. They can literally build a processor using this instruction set. People are, people  
**Translation:** 

**[2525.24s] English:** are. So what happened to us that the story was, this was developed here for our use to do our  
**Translation:** Vocabulary: processor: 处理器

**[2530.42s] English:** research. And we made it, we licensed under the Berkeley software distribution license, like a lot  
**Translation:** 

**[2536.56s] English:** of things get licensed here. So other academics use it, they wouldn't be afraid to use it. And  
**Translation:** Vocabulary: berkeley: 伯克利

**[2540.98s] English:** then about 2014, we started getting complaints that we were using it in our research and in our  
**Translation:** 

**[2547.66s] English:** courses. And we got complaints from people in industries. Why did you change your instruction  
**Translation:** 

**[2552.68s] English:** set between the fall and the spring semester? And well, we get complaints from industrial time.  
**Translation:** 

**[2558.66s] English:** Why the hell do you care what we do with our instruction set? And then when we talked to  
**Translation:** 

**[2562.86s] English:** them, we found out there was this thirst for this idea of an open instruction set architecture. And  
**Translation:** 

**[2567.78s] English:** they had been looking for one. They stumbled upon ours at Berkeley, thought it was, boy,  
**Translation:** 

**[2572.84s] English:** this looks great. We should use this one. And so once we realized there was,  
**Translation:** 

**[2577.66s] English:** this need for an open instruction set architecture, we thought that's a great idea. And then we  
**Translation:** 

**[2582.40s] English:** started supporting it and tried to make it happen. So this was kind of, we accidentally stumbled into  
**Translation:** 

**[2588.56s] English:** this, into this need and our timing was good. And so it's really taking off. There's, you know,  
**Translation:** 

**[2596.84s] English:** universities are good at starting things, but they're not good at sustaining things. So like  
**Translation:** 

**[2600.58s] English:** Linux has a Linux foundation. There's a RISC-V foundation that we started. There's, there's an  
**Translation:** Vocabulary: sustaining: 维持

**[2606.28s] English:** annual conferences. And there's a RISC-V foundation that we started. And there's a RISC-V foundation  
**Translation:** 

**[2607.64s] English:** that we started. And the first one was done, I think, January of 2015. And the one that was just  
**Translation:** Vocabulary: conferences: 年度会议

**[2612.52s] English:** last December in it, you know, it had 50 people at it. And the one last December had, I don't know,  
**Translation:** 

**[2618.82s] English:** 1700 people were at it and the companies excited all over the world. So if predicting into the  
**Translation:** 

**[2624.96s] English:** future, you know, if we were doing 25 years, I would predict that RISC-V will be, you know,  
**Translation:** 

**[2631.12s] English:** possibly the most popular instruction set architecture out there because it's a pretty  
**Translation:** 

**[2637.64s] English:** popular instruction set architecture and it's open and free.  
**Translation:** 

**[2640.00s] English:** And there's no reason lots of people shouldn't use it.  
**Translation:** 

**[2644.36s] English:** And there's benefits, just like Linux is so popular today compared to 20 years ago.  
**Translation:** 

**[2652.24s] English:** And, you know, the fact that you can get access to it for free, you can modify it, you can improve it for all those same arguments.  
**Translation:** 

**[2659.90s] English:** And so people collaborate to make it a better system for everybody to use.  
**Translation:** 

**[2663.76s] English:** And that works in software. And I expect the same thing will happen in hardware.  
**Translation:** Vocabulary: collaborate: 合作

**[2666.98s] English:** Sure. So if you look at ARM, Intel, MIPS, if you look at just the lay of the land, and what do you think, just for me, because I'm not familiar how difficult this kind of transition would, how much challenges this kind of transition would entail.  
**Translation:** 

**[2688.02s] English:** Do you see, let me ask my dumb question in another way.  
**Translation:** Vocabulary: entail: 包含

**[2692.38s] English:** No, that's, I know where you're headed.  
**Translation:** 

**[2695.24s] English:** Well, there's a bunch.  
**Translation:** 

**[2696.30s] English:** I think the thing.  
**Translation:** 

**[2696.98s] English:** You point out there's, there's these proprietary, very popular proprietary instruction sets, the x86.  
**Translation:** Vocabulary: proprietary: 专有技术

**[2702.58s] English:** And so how do we move to RISC-V potentially in sort of in the span of 5, 10, 20 years, a kind of unification in given that the devices, the kind of way we use devices, IoT, mobile devices, and the cloud is keeps changing.  
**Translation:** 

**[2719.84s] English:** Well, part of it, a big piece of it is the software stack.  
**Translation:** Vocabulary: unification: 统一

**[2725.74s] English:** And what, right.  
**Translation:** 

**[2727.02s] English:** Now, looking forward, there seem to be three important markets.  
**Translation:** 

**[2731.06s] English:** There's the cloud.  
**Translation:** 

**[2733.10s] English:** And then the cloud is simply companies like Alibaba and Amazon and Google, Microsoft, having these giant data centers with tens of thousands of servers in maybe a, maybe a hundred of these data centers all over the world.  
**Translation:** 

**[2750.32s] English:** And that's what the cloud is.  
**Translation:** 

**[2751.40s] English:** So the computer that dominates the cloud is the x86 instruction set.  
**Translation:** Vocabulary: dominates: 占据主导

**[2755.94s] English:** So the instruction.  
**Translation:** 

**[2756.90s] English:** Okay.  
**Translation:** 

**[2756.98s] English:** Or the instruction sets used in the cloud are the x86.  
**Translation:** 

**[2760.00s] English:** Almost 100% of that today is x86.  
**Translation:** 

**[2764.80s] English:** The other big thing are cell phones and laptops.  
**Translation:** 

**[2769.56s] English:** Those are the big things today.  
**Translation:** 

**[2770.90s] English:** I mean, the PC is also dominated by the x86 Instructure Set, but those sales are dwindling.  
**Translation:** 

**[2777.20s] English:** You know, there's maybe 200 million PCs a year, and there's one and a half billion phones a year.  
**Translation:** Vocabulary: dwindling: 减少

**[2783.88s] English:** There's numbers like that.  
**Translation:** 

**[2784.86s] English:** So for the phones, that's dominated by ARM.  
**Translation:** 

**[2790.28s] English:** And a reason that I talked about the software stacks, and the third category is Internet of Things, which is basically embedded devices, things in your cars, in your microwaves, everywhere.  
**Translation:** 

**[2803.14s] English:** So what's different about those three categories is for the cloud, the software that runs in the cloud is determined by these companies, Alibaba, Amazon, Google, Microsoft.  
**Translation:** Vocabulary: embedded: 嵌入式; microwaves: 微波炉

**[2813.68s] English:** So they control that software stack.  
**Translation:** 

**[2816.86s] English:** For the cell phones, there's both.  
**Translation:** 

**[2819.48s] English:** For Android and Apple, there's software they supply, but both of them have marketplaces where anybody in the world can build software.  
**Translation:** 

**[2827.06s] English:** And that software is translated or compiled down and shipped in the vocabulary of ARM.  
**Translation:** Vocabulary: compiled: 编译; marketplaces: 应用市场

**[2835.18s] English:** So that's what's referred to as binary compatible because the actual instructions are turned into numbers, binary numbers, and shipped around the world.  
**Translation:** 

**[2844.90s] English:** And so just a quick interruption.  
**Translation:** Vocabulary: binary: 二进制; compatible: 兼容; interruption: 中断

**[2847.26s] English:** So ARM, what is ARM?  
**Translation:** 

**[2849.48s] English:** ARM is an instruction set, like a risk-based instruction set.  
**Translation:** 

**[2852.72s] English:** Yeah, it's a risk-based instruction set.  
**Translation:** 

**[2854.12s] English:** It's a proprietary one.  
**Translation:** Vocabulary: proprietary: 专有技术

**[2855.38s] English:** ARM stands for Advanced Risk Machine.  
**Translation:** 

**[2860.70s] English:** ARM is the name where the company is.  
**Translation:** 

**[2862.38s] English:** So it's a proprietary risk architecture.  
**Translation:** 

**[2865.68s] English:** And it's been around for a while and is surely the most popular instruction set in the world right now.  
**Translation:** 

**[2871.64s] English:** Every year, billions of chips are using the ARM design in this post-PC era.  
**Translation:** 

**[2878.44s] English:** Was it one of the?  
**Translation:** 

**[2879.40s] English:** Yeah.  
**Translation:** 

**[2879.46s] English:** Early risk.  
**Translation:** 

**[2880.00s] English:** adopters of the RISC idea?  
**Translation:** 

**[2882.46s] English:** The first ARM goes back,  
**Translation:** Vocabulary: adopters: 采纳者

**[2884.18s] English:** I don't know, 86 or so.  
**Translation:** 

**[2885.66s] English:** So Berkeley instead did their work  
**Translation:** Vocabulary: berkeley: 伯克利

**[2887.40s] English:** in the early 80s.  
**Translation:** 

**[2888.82s] English:** The ARM guys needed an instruction set  
**Translation:** 

**[2891.52s] English:** and they read our papers  
**Translation:** 

**[2893.12s] English:** and it heavily influenced them.  
**Translation:** 

**[2897.16s] English:** So getting back to my story,  
**Translation:** 

**[2898.12s] English:** what about Internet of Things?  
**Translation:** 

**[2899.08s] English:** Well, software is not shipped  
**Translation:** 

**[2900.54s] English:** in Internet of Things.  
**Translation:** 

**[2901.26s] English:** It's the embedded device.  
**Translation:** 

**[2904.70s] English:** People control that software stack.  
**Translation:** 

**[2906.88s] English:** So the opportunities for RISC  
**Translation:** 

**[2909.88s] English:** 5, everybody thinks,  
**Translation:** 

**[2911.10s] English:** is in the Internet of Things  
**Translation:** 

**[2912.66s] English:** embedded things because  
**Translation:** 

**[2913.68s] English:** there's no dominant player  
**Translation:** 

**[2915.50s] English:** like there is in the cloud  
**Translation:** 

**[2916.74s] English:** or the smartphones.  
**Translation:** 

**[2919.92s] English:** And it doesn't have a lot  
**Translation:** 

**[2922.74s] English:** of licenses associated with  
**Translation:** 

**[2924.14s] English:** and you can enhance the instruction  
**Translation:** 

**[2925.82s] English:** set if you want.  
**Translation:** 

**[2927.06s] English:** And people have looked  
**Translation:** 

**[2930.34s] English:** at instruction sets and think  
**Translation:** 

**[2931.34s] English:** it's a very good instruction set.  
**Translation:** 

**[2932.88s] English:** So it appears to be very popular there.  
**Translation:** 

**[2935.46s] English:** It's possible that in the cloud,  
**Translation:** 

**[2939.20s] English:** people,  
**Translation:** 

**[2939.88s] English:** those companies control  
**Translation:** 

**[2940.92s] English:** their software stacks  
**Translation:** 

**[2941.84s] English:** so that it's possible  
**Translation:** 

**[2943.62s] English:** that they would decide  
**Translation:** 

**[2945.62s] English:** to use RISC-V  
**Translation:** 

**[2946.44s] English:** if we're talking about 10  
**Translation:** 

**[2947.34s] English:** and 20 years in the future.  
**Translation:** 

**[2949.66s] English:** The one that would be harder  
**Translation:** 

**[2950.60s] English:** would be the cell phones  
**Translation:** 

**[2951.80s] English:** since people ship software  
**Translation:** 

**[2953.06s] English:** in the ARM instruction set.  
**Translation:** 

**[2955.06s] English:** That you'd think  
**Translation:** 

**[2955.78s] English:** be the more difficult one.  
**Translation:** 

**[2957.42s] English:** But if RISC-V really catches on  
**Translation:** 

**[2959.64s] English:** in a period of a decade,  
**Translation:** 

**[2962.28s] English:** you can imagine  
**Translation:** 

**[2962.76s] English:** that's changing over too.  
**Translation:** 

**[2964.48s] English:** Do you have a sense  
**Translation:** 

**[2964.98s] English:** why RISC-V or ARM is dominated?  
**Translation:** 

**[2967.70s] English:** You mentioned these three categories.  
**Translation:** 

**[2969.00s] English:** Why did ARM dominate?  
**Translation:** Vocabulary: dominate: 占据优势

**[2971.32s] English:** Why does it dominate  
**Translation:** 

**[2972.20s] English:** the mobile device space?  
**Translation:** 

**[2974.06s] English:** And maybe my naive intuition  
**Translation:** 

**[2977.66s] English:** is that there's some aspects  
**Translation:** Vocabulary: intuition: 直觉; naive: 天真

**[2979.04s] English:** of power efficiency  
**Translation:** 

**[2980.04s] English:** that are important  
**Translation:** 

**[2980.94s] English:** that somehow come along with RISC.  
**Translation:** 

**[2983.18s] English:** Well, part of it is  
**Translation:** 

**[2984.22s] English:** for these old SISC instruction sets  
**Translation:** 

**[2987.56s] English:** like in the x86,  
**Translation:** 

**[2992.12s] English:** it was more expensive  
**Translation:** 

**[2994.02s] English:** to these,  
**Translation:** 

**[2997.06s] English:** you know, they're older.  
**Translation:** 

**[2998.00s] English:** So they,  
**Translation:** 

**[2999.00s] English:** they have disadvantage  
**Translation:** 

**[3000.00s] English:** Because they were designed 40 years ago. But also they have to translate in hardware from sys constructions to RISC constructions on the fly. And that costs both silicon area, the chips are bigger to be able to do that, and it uses more power.  
**Translation:** Vocabulary: constructions: 体系结构

**[3015.14s] English:** So ARM, which has followed this RISC philosophy, is seen to be much more energy efficient. And in today's computer world, both in the cloud and cell phone and other things, the limiting resource isn't the number of transistors you can fit in the chip.  
**Translation:** 

**[3033.38s] English:** It's how much power can you dissipate for your application. So by having a reduced instruction set, that's possible to have simpler hardware, which is more energy efficient.  
**Translation:** Vocabulary: dissipate: 散发; transistors: 晶体管

**[3045.14s] English:** And energy efficiency is incredibly important in the cloud. When you have tens of thousands of computers in a data center, you want to have the most energy efficient ones there as well.  
**Translation:** 

**[3054.68s] English:** And of course, for embedded things running off of batteries, you want those to be energy efficient, and the cell phones too.  
**Translation:** 

**[3059.96s] English:** So I think it's believed that there's an energy disadvantage of using these more complex instruction set architectures.  
**Translation:** 

**[3071.36s] English:** So the other aspect of this is, if we look at Apple, Qualcomm.  
**Translation:** Vocabulary: qualcomm: 高通

**[3075.14s] English:** Samsung, Huawei, all use the ARM architecture, and yet the performance of the systems varies.  
**Translation:** 

**[3082.30s] English:** I mean, I don't know whose opinion you take on, but Apple, for some reason, seems to perform better in terms of these implementations, these architectures.  
**Translation:** Vocabulary: implementations: 实现方式

**[3090.64s] English:** So where's the magic? Enter the picture.  
**Translation:** 

**[3093.14s] English:** How does that happen? Yeah, so what ARM pioneered was a new business model.  
**Translation:** Vocabulary: pioneered: 开创模式

**[3096.68s] English:** They said, well, here's our proprietary instruction set, and we'll give you two ways to do it.  
**Translation:** 

**[3103.88s] English:** Either we'll give you...  
**Translation:** Vocabulary: proprietary: 专有技术

**[3105.14s] English:** We'll give you one of these implementations written in things like C called Verilog, and you can just use ours.  
**Translation:** 

**[3111.46s] English:** Well, you have to pay money for that.  
**Translation:** 

**[3113.76s] English:** Not only will we give you their...  
**Translation:** 

**[3116.08s] English:** We'll license you to do that, or you could design your own.  
**Translation:** 

**[3120.00s] English:** So we're talking about numbers like tens of millions of dollars to have the right to design your own since the instruction set belongs to them.  
**Translation:** 

**[3128.90s] English:** So Apple got one of those, the right to build their own.  
**Translation:** 

**[3133.06s] English:** Most of the other people who build like Android phones just get one of the designs from ARM to do it themselves.  
**Translation:** 

**[3140.96s] English:** So Apple developed a really good microprocessor design team.  
**Translation:** Vocabulary: microprocessor: 微处理器

**[3146.14s] English:** And they, you know, acquired a very good team that was building other microprocessors and brought them into the company to build their designs.  
**Translation:** 

**[3156.24s] English:** So the instruction sets are the same.  
**Translation:** Vocabulary: microprocessors: 微处理器

**[3158.16s] English:** The specifications are the same.  
**Translation:** 

**[3159.60s] English:** But their hardware design is much more efficient than I think everybody else's.  
**Translation:** 

**[3164.84s] English:** And that's given Apple an advantage in the marketplace in that the iPhones tend to be faster than most everybody else's.  
**Translation:** 

**[3176.14s] English:** It'd be nice to be able to jump around and kind of explore different little sides of this.  
**Translation:** Vocabulary: marketplace: 商品市场

**[3182.64s] English:** But let me ask one sort of romanticized question.  
**Translation:** 

**[3185.68s] English:** What to you is the most beautiful aspect or idea of RISC instruction set or instruction sets or this work that you've done?  
**Translation:** 

**[3194.14s] English:** You know, I was always attracted to the idea of, you know, small is beautiful.  
**Translation:** 

**[3201.30s] English:** Is that the temptation in engineering.  
**Translation:** Vocabulary: temptation: 诱惑

**[3204.96s] English:** It's kind of easy.  
**Translation:** 

**[3206.14s] English:** To make things more complicated.  
**Translation:** 

**[3208.00s] English:** It's harder to come up with a it's more difficult, surprisingly, to come up with a simple, elegant solution.  
**Translation:** 

**[3213.90s] English:** And I think that there's a bunch of small features of of RISC in general that, you know, where you can see this examples of keeping it simpler makes it more elegant.  
**Translation:** 

**[3225.62s] English:** Specifically in RISC-V, which, you know, I'm I was kind of the mentor in the program, but it was really driven by Krista Osanovic and two grad students, Andrew Waterman and Yen-Sip Lee.  
**Translation:** 

**[3235.34s] English:** And I think that the most important thing about RISC-V is they hit upon this idea of having.  
**Translation:** 

**[3239.16s] English:** I think that the most important thing about RISC-V is they hit upon this idea of having.  
**Translation:** 

**[3240.00s] English:** a subset of instructions, nice, simple subset instructions, like 40-ish instructions that  
**Translation:** 

**[3247.68s] English:** all software, the software stack for RISC-V can run just on those 40 instructions.  
**Translation:** 

**[3253.88s] English:** And then they provide optional features that could accelerate the performance instructions  
**Translation:** Vocabulary: accelerate: 加速; optional: 可选

**[3260.56s] English:** that if you needed them could be very helpful, but you don't need to have them. And that's a new,  
**Translation:** 

**[3265.30s] English:** really a new idea. So RISC-V has right now maybe five optional subsets that you can pull in,  
**Translation:** 

**[3272.92s] English:** but the software runs without them. If you just want to build the, just the core 40 instructions,  
**Translation:** 

**[3278.22s] English:** that's fine. You can do that. So this is fantastic educationally is that you can explain  
**Translation:** Vocabulary: educationally: 教育上

**[3284.20s] English:** computers. You only have to explain 40 instructions and not thousands of them. Also, if you invent  
**Translation:** 

**[3289.68s] English:** some wild and crazy new technology, like, you know, biological computing,  
**Translation:** Vocabulary: computing: 计算

**[3295.30s] English:** you'd like a nice, simple instruction set. And you can, RISC-V, if you implement those core  
**Translation:** 

**[3301.48s] English:** instructions, you can run, you know, really interesting programs on top of that. So this  
**Translation:** 

**[3305.64s] English:** idea of a core set of instructions that the software stack runs on, and then optional features  
**Translation:** 

**[3311.52s] English:** that if you turn them on, the compilers will use, but you don't have to, I think is a powerful idea.  
**Translation:** Vocabulary: compilers: 编译器

**[3317.90s] English:** What's happened in the past for the proprietary instruction sets is when they add new instructions,  
**Translation:** 

**[3324.88s] English:** it becomes required piece. And so that all, all microprocessors in the future have to use those  
**Translation:** Vocabulary: microprocessors: 微处理器; proprietary: 专有技术

**[3332.84s] English:** instructions. So it's kind of like, for a lot of people, as they get older, they gain weight,  
**Translation:** 

**[3337.58s] English:** right? That weight and age are correlated. And so you can see these instruction sets get getting  
**Translation:** Vocabulary: correlated: 相关联的

**[3343.64s] English:** bigger and bigger as they get older. So RISC-V, you know, lets you be as slim as you're as a  
**Translation:** 

**[3349.50s] English:** teenager, and you only have to add these extra features if you're really going to use them,  
**Translation:** 

**[3353.84s] English:** rather than every...  
**Translation:** 

**[3354.88s] English:** You have no choice. You have to keep growing with the instruction set.  
**Translation:** 

**[3358.30s] English:** I don't know if the analogy holds up, but that's...  
**Translation:** 

**[3360.00s] English:** beautiful notion uh that there's it's almost like a nudge towards here's the simple core  
**Translation:** Vocabulary: nudge: 轻微提示

**[3365.82s] English:** that's the essential yeah i think the surprising thing is still if we if we brought back you know  
**Translation:** 

**[3372.12s] English:** the pioneers from the 1950s and showed them the instructions that architectures they'd understand  
**Translation:** Vocabulary: pioneers: 先驱者

**[3376.54s] English:** it they'd say wow that doesn't look that different well you know i'm surprised and it's there's it  
**Translation:** 

**[3383.14s] English:** may be something you know to talk about philosophical things i mean there may be  
**Translation:** Vocabulary: philosophical: 哲学的

**[3386.96s] English:** something powerful about those you know 40 or 50 instructions that all you need is these commands  
**Translation:** 

**[3396.36s] English:** like these instructions that we talked about and that is sufficient to build uh to bring about  
**Translation:** 

**[3402.48s] English:** you know artificial intelligence and so it's a remarkable surprising to me that is complicated  
**Translation:** 

**[3411.36s] English:** as it is to build these things uh you know uh a microprocessor  
**Translation:** 

**[3416.96s] English:** where the line widths are narrower than the wavelength of light you know is this amazing  
**Translation:** 

**[3424.04s] English:** technologies at some fundamental level uh the commands that software executes are really  
**Translation:** Vocabulary: executes: 执行; narrower: 更窄; wavelength: 波长

**[3429.10s] English:** pretty straightforward and haven't changed that much in in decades uh which what a surprising  
**Translation:** 

**[3434.84s] English:** outcome so underlying all computation all touring machines all artificial intelligence systems  
**Translation:** Vocabulary: computation: 计算; straightforward: 简单明了

**[3441.52s] English:** perhaps might be a very simple instruction set like like a risk five or it's yeah i'm  
**Translation:** 

**[3446.94s] English:** i mean i that's kind of what i said i was interested to see i had another more senior  
**Translation:** 

**[3452.60s] English:** faculty colleague and he he had written something in scientific american and uh you know his 25 years  
**Translation:** 

**[3459.92s] English:** in the future and his turned out about when i was a young professor and he said yep i checked it  
**Translation:** 

**[3464.52s] English:** and so i was interested to see how that was going to turn out for me and it's pretty held up uh  
**Translation:** 

**[3470.24s] English:** pretty well but yeah so there's there's probably there's some i you know there's there must be  
**Translation:** 

**[3476.94s] English:** uh those instructions that we're capable of  
**Translation:** 

**[3480.00s] English:** of creating intelligence from pretty primitive operations  
**Translation:** 

**[3487.06s] English:** and just doing them really fast.  
**Translation:** 

**[3489.42s] English:** You kind of mentioned a different,  
**Translation:** 

**[3491.98s] English:** maybe radical computational medium like biological,  
**Translation:** 

**[3495.28s] English:** and there's other ideas.  
**Translation:** Vocabulary: computational: 计算的

**[3496.44s] English:** So there's a lot of spaces in ASIC,  
**Translation:** 

**[3498.50s] English:** so it's domain-specific,  
**Translation:** 

**[3500.58s] English:** and then there could be quantum computers,  
**Translation:** 

**[3502.10s] English:** and so we can think of all of those different mediums  
**Translation:** 

**[3505.76s] English:** and types of computation.  
**Translation:** 

**[3507.40s] English:** What's the connection between swapping out  
**Translation:** Vocabulary: swapping: 替换

**[3510.74s] English:** different hardware systems in the instruction set?  
**Translation:** 

**[3514.72s] English:** Do you see those as disjoint,  
**Translation:** Vocabulary: disjoint: 不相连

**[3516.06s] English:** or are they fundamentally coupled?  
**Translation:** 

**[3517.58s] English:** Yeah, so kind of if we go back to the history,  
**Translation:** Vocabulary: fundamentally: 从根本上

**[3523.80s] English:** when Moore's Law is in full effect  
**Translation:** 

**[3525.44s] English:** and you're getting twice as many transistors  
**Translation:** Vocabulary: transistors: 晶体管

**[3528.14s] English:** every couple of years,  
**Translation:** 

**[3530.96s] English:** kind of the challenge for computer designers  
**Translation:** Vocabulary: designers: 设计师

**[3533.00s] English:** is how can we take advantage of that?  
**Translation:** 

**[3534.54s] English:** How can we turn those transistors  
**Translation:** 

**[3536.12s] English:** into better computers?  
**Translation:** 

**[3537.38s] English:** We can't turn those computers faster, typically,  
**Translation:** 

**[3541.70s] English:** and so there was an era,  
**Translation:** 

**[3544.30s] English:** I guess in the 80s and 90s,  
**Translation:** 

**[3546.42s] English:** where computers were doubling performance every 18 months.  
**Translation:** 

**[3552.02s] English:** And if you weren't around then,  
**Translation:** 

**[3554.16s] English:** what would happen is you had your computer  
**Translation:** 

**[3558.52s] English:** and your friend's computer,  
**Translation:** 

**[3559.52s] English:** which was like a year or a year-and-a-half newer,  
**Translation:** 

**[3561.82s] English:** and it was much faster than your computer,  
**Translation:** 

**[3564.02s] English:** and he or she could get their work done,  
**Translation:** 

**[3567.04s] English:** their computers perfectly good computers and threw them away to buy a newer computer because the  
**Translation:** 

**[3573.28s] English:** computer one or two years later was so much faster so that's what the world was like in the 80s and  
**Translation:** 

**[3579.14s] English:** 90s well with the slowing down of moore's law that's no longer true right now with you know  
**Translation:** 

**[3586.20s] English:** not with that desk side computers with the laptops i only get a new desk a laptop when it breaks  
**Translation:** 

**[3591.44s] English:** right oh damn the disc broke or this display broke i gotta buy a new computer but before you  
**Translation:** 

**[3596.72s] English:** would throw them away because it just they were just so  
**Translation:** 

**[3600.00s] English:** sluggish compared to the latest computers. So that's, you know, that's a huge change of what's  
**Translation:** Vocabulary: sluggish: 反应慢

**[3609.06s] English:** gone on. So, but since this lasted for decades, kind of programmers and maybe all of society  
**Translation:** 

**[3616.36s] English:** is used to computers getting faster regularly. We now believe, those of us who are in computer  
**Translation:** 

**[3623.40s] English:** design, it's called computer architecture, that the path forward is instead is to add accelerators  
**Translation:** 

**[3630.32s] English:** that only work well for certain applications. So since Moore's law is slowing down,  
**Translation:** 

**[3640.00s] English:** we don't think general purpose computers are going to get a lot faster. So the Intel  
**Translation:** 

**[3644.58s] English:** processors of the world are not going to, haven't been getting a lot faster. They've been  
**Translation:** 

**[3649.30s] English:** barely improving, like a few percent a year. It used to be  
**Translation:** 

**[3652.62s] English:** doubling every day.  
**Translation:** 

**[3653.40s] English:** 18 months, and now it's doubling every 20 years. So it was just shocking. So to be able to deliver  
**Translation:** 

**[3658.82s] English:** on what Moore's law used to do, we think what's going to happen, what is happening right now is  
**Translation:** 

**[3663.98s] English:** people adding accelerators to their microprocessors that only work well for some domains.  
**Translation:** 

**[3671.94s] English:** And by sheer coincidence, at the same time that this is happening, has been this revolution in  
**Translation:** Vocabulary: accelerators: 加速器; coincidence: 巧合; microprocessors: 微处理器

**[3678.72s] English:** artificial intelligence called machine learning. So  
**Translation:** 

**[3682.14s] English:** with, as I'm sure your other guests have said, you know, AI had these two competing schools of  
**Translation:** 

**[3690.44s] English:** thought is that we could figure out artificial intelligence by just writing the rules top down,  
**Translation:** 

**[3695.36s] English:** or that was wrong. You had to look at data and infer what the rules are, the machine learning,  
**Translation:** 

**[3701.16s] English:** and what's happened in the last decade or eight years is machine learning has won.  
**Translation:** 

**[3707.32s] English:** And it turns out that machine learning, the hardware you build for machine learning,  
**Translation:** 

**[3712.14s] English:** is pretty much multiply. The matrix multiply is a key feature for the way machine learning is done.  
**Translation:** 

**[3720.64s] English:** So that's a godsend for computer designers.  
**Translation:** Vocabulary: designers: 设计师; godsend: 及时雨; matrix: 矩阵; multiply: 乘法

**[3724.10s] English:** We know how to make matrix multiply run really fast.  
**Translation:** 

**[3727.68s] English:** So general purpose microprocessors are slowing down.  
**Translation:** 

**[3730.22s] English:** We're adding accelerators for machine learning  
**Translation:** 

**[3732.08s] English:** that fundamentally are doing matrix multiplies  
**Translation:** Vocabulary: fundamentally: 本质上; multiplies: 乘法运算

**[3734.88s] English:** much more efficiently  
**Translation:** 

**[3735.80s] English:** than general purpose computers have done.  
**Translation:** Vocabulary: efficiently: 高效地

**[3737.82s] English:** So we have to come up with a new way to accelerate things.  
**Translation:** 

**[3741.58s] English:** The danger of only accelerating one application  
**Translation:** Vocabulary: accelerate: 加速; accelerating: 加速

**[3743.66s] English:** is how important is that application.  
**Translation:** 

**[3745.64s] English:** Turns out machine learning gets used  
**Translation:** 

**[3748.24s] English:** for all kinds of things.  
**Translation:** 

**[3749.44s] English:** So serendipitously we found something to accelerate  
**Translation:** Vocabulary: serendipitously: 偶然地

**[3754.30s] English:** that's widely applicable.  
**Translation:** 

**[3757.22s] English:** And we don't even,  
**Translation:** 

**[3758.24s] English:** we're in the middle of this revolution of machine learning.  
**Translation:** 

**[3760.30s] English:** We're not sure what the limits of machine learning are.  
**Translation:** 

**[3762.66s] English:** So this has been a kind of a godsend.  
**Translation:** 

**[3765.76s] English:** If you're going to be able to deliver  
**Translation:** 

**[3768.58s] English:** on improved performance,  
**Translation:** 

**[3770.12s] English:** as long as people are moving their programs  
**Translation:** 

**[3773.86s] English:** to be embracing more machine learning,  
**Translation:** 

**[3776.30s] English:** we know how to give them more performance  
**Translation:** Vocabulary: embracing: 接纳

**[3778.46s] English:** even as more.  
**Translation:** 

**[3779.26s] English:** Of course, law is slowing down.  
**Translation:** 

**[3780.58s] English:** And counterintuitively,  
**Translation:** 

**[3782.30s] English:** the machine learning mechanism,  
**Translation:** Vocabulary: counterintuitively: 出乎意料地

**[3785.54s] English:** you can say is domain specific,  
**Translation:** 

**[3787.36s] English:** but because it's leveraging data,  
**Translation:** Vocabulary: leveraging: 利用

**[3789.94s] English:** it's actually could be very broad  
**Translation:** 

**[3792.54s] English:** in terms of the domains it could be applied in.  
**Translation:** 

**[3798.50s] English:** Yeah, that's exactly right.  
**Translation:** 

**[3799.80s] English:** Sort of, it's almost sort of,  
**Translation:** 

**[3801.94s] English:** people sometimes talk about the idea of software 2.0.  
**Translation:** 

**[3805.08s] English:** We're almost taking another step up  
**Translation:** 

**[3807.86s] English:** in the abstraction layer.  
**Translation:** 

**[3809.26s] English:** I mean, designing machine learning systems  
**Translation:** 

**[3812.44s] English:** because now you're programming in the space of data,  
**Translation:** 

**[3815.38s] English:** in the space of hyperparameters.  
**Translation:** Vocabulary: hyperparameters: 超参数

**[3816.92s] English:** It's changing fundamentally the nature of programming.  
**Translation:** 

**[3820.38s] English:** And so the specialized devices that accelerate the performance,  
**Translation:** 

**[3824.90s] English:** especially neural network-based machine learning systems,  
**Translation:** 

**[3827.44s] English:** might become the new general.  
**Translation:** Vocabulary: neural: 神经网络

**[3830.26s] English:** Yeah, so the thing that's interesting to point out,  
**Translation:** 

**[3833.66s] English:** these are not tied together.  
**Translation:** 

**[3837.74s] English:** The enthusiasm,  
**Translation:** 

**[3839.26s] English:** the enthusiasm about machine learning,  
**Translation:** 

**[3840.00s] English:** learning about creating programs driven from data that we should figure out the answers  
**Translation:** 

**[3845.08s] English:** from data rather than kind of top down, which is classically the way most programming is  
**Translation:** 

**[3850.04s] English:** done and the way artificial intelligence used to be done.  
**Translation:** 

**[3852.42s] English:** That's a movement that's going on at the same time.  
**Translation:** 

**[3856.10s] English:** Coincidentally, and the first word in machine learning is machines, right?  
**Translation:** 

**[3860.24s] English:** So that's going to increase the demand for computing because instead of programmers being  
**Translation:** Vocabulary: computing: 计算; programmers: 程序员

**[3866.36s] English:** smart writing those things down, we're going to instead use computers to examine a lot  
**Translation:** 

**[3871.10s] English:** of data to kind of create the programs.  
**Translation:** 

**[3873.12s] English:** That's the idea.  
**Translation:** 

**[3875.48s] English:** And remarkably, this gets used for all kinds of things very successfully.  
**Translation:** Vocabulary: remarkably: 非常地

**[3879.76s] English:** The image recognition, the language translation, the game playing, and it gets into pieces  
**Translation:** 

**[3887.22s] English:** of the software stack like databases and stuff like that.  
**Translation:** Vocabulary: databases: 数据库

**[3890.40s] English:** We're not quite sure how general purpose it is, but that's going on independent of this  
**Translation:** 

**[3893.96s] English:** hardware stuff.  
**Translation:** 

**[3895.00s] English:** What's happening on the hardware side?  
**Translation:** 

**[3896.36s] English:** It's Moore's law is slowing down right when we need a lot more cycles.  
**Translation:** 

**[3900.04s] English:** It's failing us right when we need it because there's going to be a greater increase in  
**Translation:** 

**[3905.98s] English:** computing.  
**Translation:** 

**[3907.02s] English:** And then this idea that we're going to do so-called domain specific.  
**Translation:** 

**[3910.50s] English:** Here's a domain that your greatest fear is you'll make this one thing work and that'll  
**Translation:** 

**[3916.86s] English:** help 5% of the people in the world.  
**Translation:** 

**[3919.72s] English:** Well, this looks like it's a very general purpose thing.  
**Translation:** 

**[3922.98s] English:** So the timing is fortuitous.  
**Translation:** 

**[3925.04s] English:** That if we can...  
**Translation:** Vocabulary: fortuitous: 巧合的

**[3926.36s] English:** Perhaps if we can keep building hardware that will accelerate machine learning, the  
**Translation:** 

**[3932.32s] English:** neural networks, that'll beat the timing will be right.  
**Translation:** Vocabulary: accelerate: 加速

**[3936.60s] English:** That neural network revolution will transform software, the so-called software 2.0.  
**Translation:** 

**[3943.38s] English:** And the software of the future will be very different from the software of the past.  
**Translation:** 

**[3947.28s] English:** And just as our microprocessors, even though we're still going to have that same basic  
**Translation:** 

**[3951.60s] English:** risk instructions to run big pieces of the software stack like user interfaces.  
**Translation:** Vocabulary: interfaces: 用户界面; microprocessors: 微处理器

**[3956.36s] English:** And stuff like that, we can accelerate the...  
**Translation:** 

**[3960.00s] English:** kind of the small piece that's computationally impensive. It's not lots of lines of code,  
**Translation:** Vocabulary: computationally: 计算上

**[3964.04s] English:** but it takes a lot of cycles to run that code, that that's going to be the accelerator piece.  
**Translation:** 

**[3969.12s] English:** So that's what makes this, from a computer designer's perspective, a really interesting  
**Translation:** 

**[3975.26s] English:** decade. What Hennessy and I talked about in the title of our Turing-Warn speech is a new golden  
**Translation:** 

**[3981.34s] English:** age. We see this as a very exciting decade, much like when we were assistant professors and the  
**Translation:** Vocabulary: hennessy: 汉尼西

**[3989.62s] English:** RIS stuff was going on. That was a very exciting time. It was where we were changing what was  
**Translation:** 

**[3993.02s] English:** going on. We see this happening again. Tremendous opportunities of people because we're fundamentally  
**Translation:** Vocabulary: fundamentally: 从根本上

**[3999.90s] English:** changing how software is built and how we're running it.  
**Translation:** 

**[4002.90s] English:** So which layer of the abstraction do you think most of the acceleration might be happening?  
**Translation:** Vocabulary: abstraction: 抽象层; acceleration: 加速层

**[4007.92s] English:** If you look in the next 10 years, Google is working on a lot of exciting stuff with the TPU.  
**Translation:** 

**[4013.58s] English:** There's closer to the hardware. There could be optimizations around  
**Translation:** Vocabulary: optimizations: 优化

**[4017.26s] English:** the...  
**Translation:** 

**[4017.82s] English:** A lot closer to the instruction set. There could be optimization at the compiler level. It could  
**Translation:** Vocabulary: optimization: 优化

**[4023.20s] English:** be even at the higher level software stack.  
**Translation:** 

**[4026.28s] English:** Yeah, it's going to be... If you think about the old RIS-SYS debate, it was software hardware. It  
**Translation:** 

**[4033.22s] English:** was the compilers improving as well as the architecture improving. And that's likely  
**Translation:** 

**[4039.50s] English:** to be the way things are now. With machine learning, they're using domain-specific languages,  
**Translation:** Vocabulary: compilers: 编译器

**[4046.32s] English:** the languages like...  
**Translation:** 

**[4048.22s] English:** TensorFlow and PyTorch are very popular with the machine learning people. Those are...  
**Translation:** 

**[4054.06s] English:** Raising the level of abstraction, it's easier for people to write machine learning in these  
**Translation:** 

**[4058.62s] English:** domain-specific languages like PyTorch and TensorFlow.  
**Translation:** 

**[4063.82s] English:** So where most of the optimization might be happening?  
**Translation:** 

**[4065.82s] English:** Yeah. And so there'll be both the compiler piece and the hardware piece underneath it. So as you...  
**Translation:** 

**[4072.38s] English:** Kind of the fatal flaw for hardware people is to create really great hardware, but not have the  
**Translation:** 

**[4077.82s] English:** best of them. And I think that brought along the compilers and what we're...  
**Translation:** 

**[4080.00s] English:** seeing right now in the marketplace because of this enthusiasm around hardware for machine  
**Translation:** 

**[4085.30s] English:** learning is getting, you know, probably billions of dollars invested in startup companies. We're  
**Translation:** Vocabulary: marketplace: 商品市场

**[4091.14s] English:** seeing startup companies go belly up because they focused on the hardware but didn't bring  
**Translation:** 

**[4096.52s] English:** the software stack along. We talked about benchmarks earlier. So I participated in  
**Translation:** Vocabulary: benchmarks: 参考标准

**[4103.38s] English:** machine learning, didn't really have a set of benchmarks. I think just two years ago,  
**Translation:** 

**[4107.44s] English:** they didn't have a set of benchmarks. And we've created something called MLPerf, which is  
**Translation:** 

**[4111.64s] English:** machine learning benchmark suite. And pretty much the companies who didn't invest in the software  
**Translation:** 

**[4118.34s] English:** stack couldn't run MLPerf very well. And the ones who did invest in software stack did. And we're  
**Translation:** Vocabulary: benchmark: 性能基准

**[4124.08s] English:** seeing, you know, like kind of in computer architecture, this is what happens. You have  
**Translation:** 

**[4127.48s] English:** these arguments about risk versus risk. People spend billions of dollars in the marketplace to  
**Translation:** 

**[4131.56s] English:** see who wins. And it's not a perfect comparison, but it kind of sorts things out. And we're seeing  
**Translation:** 

**[4137.04s] English:** companies that are doing it. And we're seeing companies that are doing it. And we're seeing  
**Translation:** 

**[4137.42s] English:** companies that are doing it. And we're seeing companies that are doing it. And we're seeing  
**Translation:** 

**[4137.44s] English:** go out of business. And then companies like, there's a company in Israel called Habana.  
**Translation:** Vocabulary: habana: 海巴纳

**[4144.60s] English:** They came up with machine learning accelerators. They had good MLPerf scores. Intel had acquired  
**Translation:** 

**[4152.16s] English:** a company earlier called Nirvana a couple of years ago. They didn't reveal their MLPerf scores,  
**Translation:** Vocabulary: accelerators: 加速器

**[4157.40s] English:** which was suspicious. But a month ago, Intel announced that they're canceling the Nirvana  
**Translation:** 

**[4163.10s] English:** product line. And they bought Habana for $2 billion. And they're canceling the Nirvana  
**Translation:** Vocabulary: canceling: 取消; nirvana: 极乐世界

**[4167.42s] English:** Intel's going to be shipping Habana chips, which have hardware and software and run the MLPerf  
**Translation:** 

**[4173.38s] English:** programs pretty well. And that's going to be their product line of the future.  
**Translation:** 

**[4177.14s] English:** Brilliant. So maybe just to linger briefly on MLPerf. I love metrics. I love standards that  
**Translation:** 

**[4182.70s] English:** everyone can gather around. What are some interesting aspects of that portfolio of metrics?  
**Translation:** 

**[4188.98s] English:** Well, one of the interesting metrics is, you know, what we thought it was, you know, we,  
**Translation:** 

**[4194.12s] English:** I was involved in the start. You know, we,  
**Translation:** 

**[4196.98s] English:** Peter Mattson is leading the effort from Google. Google  
**Translation:** 

**[4200.00s] English:** got it off the ground but we had to reach out to competitors and say um there's no benchmarks here  
**Translation:** 

**[4206.32s] English:** this we think this is bad for the field it'll be much better if we look at examples like in the  
**Translation:** 

**[4210.56s] English:** risk days there was an effort to create a for the the people in the risk community got together  
**Translation:** 

**[4216.10s] English:** competitors got together we're building risk microprocessors to agree on a set of benchmarks  
**Translation:** 

**[4220.16s] English:** that were called spec and that was good for the industry is rather before the different risk  
**Translation:** Vocabulary: benchmarks: 参考标准; microprocessors: 微处理器

**[4225.68s] English:** architectures were arguing well you can believe my performance others but those other guys are  
**Translation:** 

**[4229.26s] English:** liars and that didn't do any good so we agreed on a set of benchmarks and then we could figure out  
**Translation:** 

**[4235.56s] English:** who was faster between the various risk architectures but it was a little bit faster  
**Translation:** 

**[4239.16s] English:** but that grew the market rather than you know people were afraid to buy anything so we argued  
**Translation:** 

**[4243.82s] English:** the same thing would happen with ml perf you know companies like nvidia were you know maybe  
**Translation:** 

**[4248.70s] English:** worried that it was some kind of trap but eventually we all got together to create a  
**Translation:** 

**[4253.28s] English:** set of benchmarks and do the right thing right and we agree on the results and so we can  
**Translation:** 

**[4259.24s] English:** see whether tpus or gpus or cpus are really faster and how much the faster and i think from  
**Translation:** 

**[4266.04s] English:** an engineer's perspective as long as the results are fair you're you can live with it okay you know  
**Translation:** 

**[4271.58s] English:** you kind of tip your hat to to your colleagues at another institution boy they did a better job  
**Translation:** 

**[4276.54s] English:** than us what you what you hate is if it's it's false right they're making claims and it's just  
**Translation:** 

**[4281.02s] English:** marketing bullshit and you know and that's affecting sales so you from an engineer's  
**Translation:** Vocabulary: bullshit: 胡说八道

**[4285.46s] English:** perspective as long as it's a fair comparison and we don't come in first place they're going to  
**Translation:** 

**[4289.24s] English:** say that's too bad but it's fair so we wanted to create that environment for ml perf and so now  
**Translation:** 

**[4294.92s] English:** uh there's 10 companies i mean 10 universities and 50 companies involved so pretty much ml perf has uh  
**Translation:** 

**[4303.96s] English:** is this is the way you measure machine learning uh performance um and and it didn't exist even two  
**Translation:** 

**[4310.76s] English:** years ago one of the cool things that i enjoy about the internet has a few downsides but  
**Translation:** 

**[4316.44s] English:** one of the nice things is um people can see  
**Translation:** Vocabulary: downsides: 缺点

**[4319.24s] English:** see through  
**Translation:** 

**[4320.00s] English:** a little better with the presence of these kinds of metrics it's so it's really nice companies like  
**Translation:** 

**[4325.40s] English:** google and facebook and twitter now it's the cool thing to do is to put your engineers forward and  
**Translation:** 

**[4331.10s] English:** to actually show off how well you do on these metrics there's not sort of um it well there's  
**Translation:** 

**[4337.68s] English:** less of a desire to do marketing less so am i am i sort of naive no i think what i was trying to  
**Translation:** 

**[4344.38s] English:** understand that you know what's changed from the 80s in this era i think uh because of things like  
**Translation:** Vocabulary: naive: 幼稚

**[4349.58s] English:** social networking twitter and stuff like that if you if you put up you know uh bullshit stuff  
**Translation:** 

**[4355.62s] English:** right that's just you know miss purposely misleading you know that you you can get a  
**Translation:** Vocabulary: misleading: 误导; purposely: 故意

**[4361.60s] English:** violent reaction in social media pointing out the flaws in your arguments right and so from a  
**Translation:** 

**[4368.10s] English:** marketing perspective you have to be careful today that you didn't have to be careful that uh there'll  
**Translation:** 

**[4374.38s] English:** be people who who put out the flaw you can get the word out about the flaws and what you're saying  
**Translation:** 

**[4379.58s] English:** much more easily today than in the past you used to be it used to be easier to get away with it  
**Translation:** 

**[4384.36s] English:** and the other thing that's been happening in terms of serving off engineers is just  
**Translation:** 

**[4389.18s] English:** in the software side people have largely embraced open source software it it was 20 years ago it was  
**Translation:** Vocabulary: embraced: 接受

**[4398.20s] English:** a dirty word at microsoft and today microsoft is one of the big proponents of open source software  
**Translation:** 

**[4403.24s] English:** kind of that's the standard way most software gets built which really shows off your engineers  
**Translation:** Vocabulary: proponents: 支持者

**[4409.58s] English:** you can see if you look at the source code you can see who are making the commits who's making  
**Translation:** 

**[4415.30s] English:** the improvements who are the engineers at all these companies who are uh are you know really  
**Translation:** 

**[4421.82s] English:** uh great uh programmers and engineers and making really solid contributions which enhances their  
**Translation:** 

**[4428.02s] English:** reputations and the reputation of the companies so but that's of course not everywhere like in  
**Translation:** Vocabulary: enhances: 提升; programmers: 程序员; reputations: 声誉

**[4433.12s] English:** the space that i work more in is autonomous vehicles and they're still the machinery  
**Translation:** 

**[4439.58s] English:** of hype  
**Translation:** Vocabulary: autonomous: 自主; machinery: 机器

**[4440.00s] English:** marketing is still very strong there and there's less willingness to be open in this kind of open  
**Translation:** 

**[4445.20s] English:** source way and sort of benchmark so ml perf is represents the machine learning world is much  
**Translation:** Vocabulary: benchmark: 参考标准

**[4450.82s] English:** better being open source about holding itself to standards of different the amount of incredible  
**Translation:** 

**[4456.14s] English:** benchmarks in terms of the different computer vision natural language processing uh tasks is  
**Translation:** Vocabulary: benchmarks: 参考标准

**[4462.60s] English:** incredible it you know historically it wasn't always that way um i had a graduate student  
**Translation:** 

**[4468.26s] English:** working with me david martin so for in computer in some fields benchmarking has been around forever  
**Translation:** Vocabulary: benchmarking: 性能测试; historically: 历史上

**[4474.68s] English:** so uh computer architecture databases uh maybe operating systems uh benchmarks are  
**Translation:** 

**[4483.14s] English:** uh the way you measure progress but uh he was working with me and then started working with  
**Translation:** Vocabulary: databases: 数据库

**[4488.78s] English:** jitendra malik and he's jitendra malik and computer vision space who i guess you've  
**Translation:** 

**[4493.72s] English:** interviewed jandra and uh david martin told me they don't have  
**Translation:** 

**[4498.24s] English:** benchmarks. Everybody has their own vision algorithm and the way that my, here's my image,  
**Translation:** 

**[4503.14s] English:** look at how well I do. And everybody had their own image. So David Martin, back when he did his  
**Translation:** Vocabulary: algorithm: 计算方法

**[4509.08s] English:** dissertation, figured out a way to do benchmarks. He had a bunch of graduate students identify  
**Translation:** 

**[4514.08s] English:** images and then ran benchmarks to see which algorithms run well. And that was, as far as I  
**Translation:** Vocabulary: dissertation: 论文

**[4519.58s] English:** know, kind of the first time people did benchmarks in computer vision and which was predated all,  
**Translation:** 

**[4526.76s] English:** you know, the things that eventually led to ImageNet and stuff like that. But then, you know,  
**Translation:** Vocabulary: predated: 早于

**[4530.08s] English:** the vision community got religion. And then once we got as far as ImageNet, then that let the guys  
**Translation:** 

**[4537.50s] English:** in Toronto be able to win the ImageNet competition. And then, you know, that changed the whole world.  
**Translation:** Vocabulary: toronto: 多伦多

**[4543.92s] English:** It's a scary step, actually, because when you enter the world of benchmarks, you actually have  
**Translation:** 

**[4548.68s] English:** to be good to participate as opposed to, yeah, you can just, you just believe you're the best  
**Translation:** 

**[4555.10s] English:** in the world.  
**Translation:** 

**[4556.76s] English:** Yeah. And I think the people, I think they weren't purposely  
**Translation:** Vocabulary: purposely: 故意

**[4560.00s] English:** misleading i think if you don't have benchmarks i mean how do you know you know you could have  
**Translation:** 

**[4565.08s] English:** your intuition it's kind of like the way we used to do computer architecture your intuition is that  
**Translation:** Vocabulary: intuition: 直觉; misleading: 误导

**[4569.86s] English:** this is the right instruction set to do this job i believe in my experience my hunch is that's true  
**Translation:** 

**[4575.76s] English:** we had to get to make things more quantitative uh to make progress and so i just don't know how  
**Translation:** Vocabulary: hunch: 直觉; quantitative: 量化

**[4583.52s] English:** you know in fields that don't have benchmarks i don't understand how they figure out how they're  
**Translation:** 

**[4587.96s] English:** making progress we're kind of in the vacuum tube days of quantum computing what are your thoughts  
**Translation:** Vocabulary: benchmarks: 参考标准; computing: 计算; vacuum: 真空

**[4595.30s] English:** in this wholly different kind of space of architectures uh you know i actually you know  
**Translation:** 

**[4600.94s] English:** quantum computing uh is idea has been around for a while and i actually thought well i sure hope  
**Translation:** 

**[4605.70s] English:** uh i retire before i have to start teaching this uh i'd say because i talk about give these talks  
**Translation:** 

**[4613.22s] English:** about the slowing of morse law and um you know when we need to  
**Translation:** Vocabulary: morse: 莫尔斯电码

**[4617.64s] English:** uh  
**Translation:** 

**[4617.96s] English:** change by uh doing domain specific accelerators uh common questions say what about quantum  
**Translation:** 

**[4622.80s] English:** computing the reason that comes up it's in the news all the time so i think to keep in the hard  
**Translation:** 

**[4627.78s] English:** thing to keep in mind is quantum computing is not right around the corner uh there have been  
**Translation:** 

**[4632.52s] English:** two national reports one by the national campus of engineering another by the computing consortium  
**Translation:** 

**[4637.84s] English:** where they did a frank assessment of of quantum computing and uh both of those reports said you  
**Translation:** Vocabulary: consortium: 联盟

**[4645.00s] English:** know as far as we can tell before you get  
**Translation:** 

**[4647.64s] English:** error corrected quantum computing it's a decade away so i think of it like nuclear fusion right  
**Translation:** 

**[4653.58s] English:** there have been people who've been excited about nuclear fusion a long time if we ever get nuclear  
**Translation:** 

**[4657.66s] English:** fusion it's going to be fantastic for the world i'm glad people are working on it but you know  
**Translation:** 

**[4662.52s] English:** it's not right around the corner uh the those two reports to me say probably it'll be 2030 before  
**Translation:** 

**[4669.58s] English:** quantum computing is a uh something that could happen and when it does happen you know this is  
**Translation:** 

**[4676.44s] English:** going to be big science  
**Translation:** 

**[4677.52s] English:** stuff this is uh you know micro  
**Translation:** 

**[4680.00s] English:** Kelvin, almost absolute zero things that if they vibrate, if truck goes by, it won't work, right?  
**Translation:** 

**[4685.84s] English:** So this will be in data center stuff. We're not going to have a quantum cell phone. And it's  
**Translation:** Vocabulary: kelvin: Kelvin温度

**[4691.68s] English:** probably a 2030 kind of thing. So I'm happy that other people are working on it, but just,  
**Translation:** 

**[4697.02s] English:** you know, it's hard with all the news about it, not to think that it's right around the corner.  
**Translation:** 

**[4702.54s] English:** And that's why we need to do something as Moore's law is slowing down to provide the  
**Translation:** 

**[4706.90s] English:** computing, keep computing getting better for this next decade. And, you know, we shouldn't  
**Translation:** 

**[4712.68s] English:** be betting on quantum computing or expecting quantum computing to deliver in the next few  
**Translation:** 

**[4719.74s] English:** years. It's probably further off. You know, I'd be happy to be wrong. It'd be great if quantum  
**Translation:** Vocabulary: computing: 计算

**[4724.60s] English:** computing is going to commercially viable, but it will be a set of applications. It's not a general  
**Translation:** 

**[4729.58s] English:** purpose computation. So it's going to do some amazing things, but there'll be a lot of things  
**Translation:** Vocabulary: commercially: 商业上; computation: 计算

**[4734.72s] English:** that probably, you know, the,  
**Translation:** 

**[4736.90s] English:** the old fashioned computers are going to keep doing better for quite a while.  
**Translation:** 

**[4740.94s] English:** And there'll be a teenager 50 years from now watching this video saying,  
**Translation:** 

**[4744.88s] English:** look how silly David Patterson was saying.  
**Translation:** 

**[4748.02s] English:** No, I just said, I said 2030. I didn't say, I didn't say never.  
**Translation:** 

**[4752.16s] English:** We're not going to have quantum cell phones. So he's going to be watching it on a quantum cell phone.  
**Translation:** 

**[4755.62s] English:** Well, I mean, I think this is such a, you know, given that we've had Moore's law, I just,  
**Translation:** 

**[4761.08s] English:** I feel comfortable trying to do projects that are thinking about the next decade.  
**Translation:** 

**[4766.90s] English:** I admire people who are trying to do things that are 30 years out, but  
**Translation:** 

**[4769.70s] English:** it's such a fast moving field. Uh, I just don't know how to, I I'm not good enough to figure out  
**Translation:** 

**[4776.46s] English:** what, what's the problem is going to be in 30 years. Uh, you know, 10 years is hard enough for  
**Translation:** 

**[4780.66s] English:** me. So maybe if, if it's possible to untangle your intuition a little bit, I spoke with Jim Keller.  
**Translation:** Vocabulary: intuition: 直觉; untangle: 理清

**[4786.30s] English:** I don't know if you're familiar with Jim and he, he, he is trying to sort of, uh,  
**Translation:** 

**[4791.60s] English:** be a little bit rebellious and to try to think that, um, he, he quotes me as being,  
**Translation:** Vocabulary: rebellious: 叛逆

**[4796.10s] English:** wrong. Yeah. So this, this is what are your, by the way, for,  
**Translation:** 

**[4800.00s] English:** For the record, Jim talks about that he has an intuition that Moore's law is not, in fact, dead yet, and that it may continue for some time to come.  
**Translation:** 

**[4811.86s] English:** What are your thoughts about Jim's ideas in this space?  
**Translation:** 

**[4814.86s] English:** Yeah, this is just marketing.  
**Translation:** 

**[4817.38s] English:** So what Gordon Moore said is a quantitative prediction.  
**Translation:** 

**[4821.58s] English:** We can check the facts, right, which is doubling the number of transistors every two years.  
**Translation:** Vocabulary: quantitative: 数量预测; transistors: 晶体管

**[4827.30s] English:** So we can look back at Intel for the last five years and ask him, let's look at DRAM chips six years ago.  
**Translation:** 

**[4836.42s] English:** So that would be three two-year periods.  
**Translation:** 

**[4839.78s] English:** So then our DRAM chips have eight times as many transistors as they did six years ago.  
**Translation:** 

**[4845.68s] English:** We can look up Intel microprocessors six years ago.  
**Translation:** Vocabulary: microprocessors: 微处理器

**[4849.64s] English:** If Moore's law is continuing, it should have eight times as many transistors as six years ago.  
**Translation:** 

**[4856.38s] English:** The answer?  
**Translation:** 

**[4857.34s] English:** In both those cases, it's no.  
**Translation:** 

**[4859.20s] English:** The problem has been because Moore's law was kind of genuinely embraced by the semiconductor industry as they would make investments in similar equipment to make Moore's law come true.  
**Translation:** Vocabulary: embraced: 被接纳; semiconductor: 半导体

**[4873.86s] English:** Semiconductor improving and Moore's law, in many people's minds, are the same thing.  
**Translation:** 

**[4879.40s] English:** So when I say, and I'm factually correct, that Moore's law is no longer holds, we are not doubling the transistors.  
**Translation:** 

**[4887.30s] English:** The downside for a company like Intel is people think that means it's stopped, that technology has no longer improved.  
**Translation:** 

**[4898.04s] English:** And so Jim is trying to counteract the impression that semiconductors are frozen in 2019, are never going to get better.  
**Translation:** Vocabulary: counteract: 抵消; downside: 不利方面; semiconductors: 半导体

**[4911.24s] English:** So I never said that.  
**Translation:** 

**[4912.84s] English:** All I said was Moore's law is no more.  
**Translation:** 

**[4916.68s] English:** And I'm.  
**Translation:** 

**[4917.30s] English:** Strictly looking at the number of transistors.  
**Translation:** 

**[4919.34s] English:** Because that's what.  
**Translation:** 

**[4920.00s] English:** Moore's law is. There's the, I don't know, there's been this aura associated with Moore's law that  
**Translation:** 

**[4928.04s] English:** they've enjoyed for 50 years about, look at the field we're in. We're doubling transistors every  
**Translation:** 

**[4933.90s] English:** two years. What an amazing field, which is an amazing thing that they were able to pull off.  
**Translation:** 

**[4938.08s] English:** But even as Gordon Moore said, you know, no exponential can last forever. It lasted for 50  
**Translation:** 

**[4942.58s] English:** years, which is amazing. And this is a huge impact on the industry because of these changes that  
**Translation:** Vocabulary: exponential: 指数增长

**[4948.16s] English:** we've been talking about. So he claims, because he's trying to act, he claims, you know, Patterson  
**Translation:** 

**[4954.30s] English:** says, Moore's law is no more. And look at all, look at it. It's still going. And TSMC, they say  
**Translation:** Vocabulary: patterson: 帕特森

**[4960.62s] English:** it's no longer. But there's quantitative evidence that Moore's law is not continuing. So what I say  
**Translation:** 

**[4966.28s] English:** now to try and, okay, I understand the perception problem when I say Moore's law stopped. Okay. So  
**Translation:** Vocabulary: quantitative: 数量上的

**[4973.84s] English:** now I say Moore's law is slowing down. And I think Jim,  
**Translation:** 

**[4978.16s] English:** which is another way of, if he's, if it's predicting every two years and I say it's  
**Translation:** 

**[4982.36s] English:** slowing down, then that's another way of saying it doesn't hold anymore. And, and I think Jim  
**Translation:** 

**[4986.94s] English:** wouldn't disagree that it's slowing down because that sounds like it's, things are still getting  
**Translation:** 

**[4993.24s] English:** better, just not as fast, which is another way of saying Moore's law isn't working anymore.  
**Translation:** 

**[4998.62s] English:** It's still good for marketing, but, but what's your, you're not, you don't like expanding the  
**Translation:** 

**[5004.12s] English:** definition of Moore's law sort of naturally.  
**Translation:** 

**[5008.16s] English:** The educator, you know, are, you know, is this like modern politics? Does everybody get their  
**Translation:** Vocabulary: educator: 教育者

**[5013.14s] English:** own facts? Or do we have, you know, Moore's law was a crisp, you know, a more, it was Carver Mead  
**Translation:** 

**[5020.36s] English:** looked at his observation, Moore's observations, a drawing on a log, log scale, a straight line.  
**Translation:** 

**[5025.98s] English:** And that's what the definition of Moore's law is. There's this other, what Intel did for a while,  
**Translation:** 

**[5031.92s] English:** interestingly, before Jim joined them, they said, oh no, Moore's law isn't the number of doubling,  
**Translation:** 

**[5037.08s] English:** isn't really,  
**Translation:** 

**[5038.16s] English:** doubling transistors every two years.  
**Translation:** Vocabulary: transistors: 晶体管

**[5040.00s] English:** Moore's law is the cost of the individual transistor going down, cutting in half every two years.  
**Translation:** 

**[5048.02s] English:** Now, that's not what he said, but they reinterpreted it because they believed that the cost of transistors was continuing to drop, even if they couldn't get twice as many chips.  
**Translation:** Vocabulary: reinterpreted: 重新解释; transistor: 晶体管

**[5058.50s] English:** Many people in industry have told me that's not true anymore, that basically in more recent technologies that got more complicated, the actual cost of transistor went up.  
**Translation:** 

**[5067.56s] English:** So, even a corollary might not be true, but certainly, you know, Moore's law, that was the beauty of Moore's law.  
**Translation:** Vocabulary: corollary: 推论

**[5077.18s] English:** It was a very simple, it's like E equals MC squared, right?  
**Translation:** 

**[5080.56s] English:** It was like, wow, what an amazing prediction.  
**Translation:** 

**[5083.54s] English:** It's so easy to understand.  
**Translation:** 

**[5084.96s] English:** The implications are amazing.  
**Translation:** 

**[5086.50s] English:** And that's why it was so famous as a prediction.  
**Translation:** 

**[5090.10s] English:** And this reinterpretation of what it meant and changing is, you know, is revisionist history.  
**Translation:** Vocabulary: reinterpretation: 重新解释; revisionist: 修正主义者

**[5096.14s] English:** And I agree.  
**Translation:** 

**[5098.00s] English:** I'd be happy.  
**Translation:** 

**[5100.28s] English:** And they're not claiming there's a new Moore's law.  
**Translation:** 

**[5102.80s] English:** They're not saying, by the way, it's instead of every two years, it's every three years.  
**Translation:** 

**[5108.44s] English:** I don't think they want to say that.  
**Translation:** 

**[5111.08s] English:** I think what's going to happen is the new technology generations, each one's going to get a little bit slower.  
**Translation:** 

**[5115.62s] English:** So, it is slowing down.  
**Translation:** 

**[5118.66s] English:** The improvements won't be as great.  
**Translation:** 

**[5121.12s] English:** And that's why we need to do new things.  
**Translation:** 

**[5122.92s] English:** Yeah, I don't like that the idea of Moore's law is tied up with marketing.  
**Translation:** 

**[5127.80s] English:** It would be nice if…  
**Translation:** 

**[5129.92s] English:** Whether it's marketing or it's…  
**Translation:** 

**[5132.10s] English:** Well, it could be affecting business, but it could also be infecting the imagination of engineers.  
**Translation:** 

**[5138.14s] English:** If Intel employees actually believe that we're frozen in 2019, well, that would be bad for Intel.  
**Translation:** Vocabulary: infecting: 感染

**[5146.22s] English:** Not just Intel, but everybody.  
**Translation:** 

**[5148.94s] English:** Moore's law is inspiring to everybody.  
**Translation:** 

**[5152.66s] English:** But what's happening right now, talking to people in…  
**Translation:** 

**[5156.66s] English:** Who have working in national offices.  
**Translation:** 

**[5159.56s] English:** And…  
**Translation:** 

**[5160.00s] English:** stuff like that a lot of the computer science community is unaware that this is going on right  
**Translation:** 

**[5165.22s] English:** that we are in an era that's going to need radical change at lower levels that could affect the whole  
**Translation:** 

**[5170.76s] English:** software stack this um you know if if if intel uh if you're using cloud stuff and the servers that  
**Translation:** 

**[5179.62s] English:** you get next year are basically only a little bit faster than the servers you got this year  
**Translation:** 

**[5183.32s] English:** you need to know that and we need to start innovating um uh to start delivering on it if  
**Translation:** Vocabulary: innovating: 创新

**[5190.14s] English:** you're counting on your software your software going to get a lot more features assuming the  
**Translation:** 

**[5193.90s] English:** computers can get faster that's not true so are you going to have to start making your software  
**Translation:** 

**[5197.72s] English:** stack more efficient are you going to have to start learning about machine learning so it's  
**Translation:** 

**[5201.84s] English:** you know it's kind of a it's a warning or call for arms that the world is changing right now  
**Translation:** 

**[5207.78s] English:** and a lot of people a lot of computer science phds are unaware of that so a way to  
**Translation:** 

**[5213.24s] English:** transform the world is to start innovating and to start delivering on it so it's kind of  
**Translation:** 

**[5213.32s] English:** get their attention is to say that morse law is slowing down and that's going to affect your  
**Translation:** 

**[5218.48s] English:** assumptions and uh you know we're trying to get the word out and when companies like tsmc  
**Translation:** Vocabulary: assumptions: 假设

**[5223.18s] English:** and intel say oh no no no morse law is fine then people think okay i don't have to change my  
**Translation:** 

**[5228.96s] English:** behavior i'll just get the next servers and you know if they start doing measurements they'll  
**Translation:** Vocabulary: morse: 莫尔斯电码

**[5233.90s] English:** realize what's going on it'd be nice to have some transparency and metrics for for the lay person  
**Translation:** 

**[5239.24s] English:** to be able to know if computers are getting faster  
**Translation:** 

**[5243.24s] English:** yeah there are there are a bunch of most people kind of use clock rate uh as a as a measure of  
**Translation:** 

**[5251.18s] English:** performance you know it's not a perfect one but if you've noticed clock rates are more or less the  
**Translation:** 

**[5255.80s] English:** same as they were five years ago computers are a little better than they aren't they haven't made  
**Translation:** 

**[5262.42s] English:** zero progress but they've made small progress so you there's some indications out there and then  
**Translation:** 

**[5266.68s] English:** our behavior right nobody buys the next laptop because it's so much faster than the laptop from  
**Translation:** 

**[5272.38s] English:** the past  
**Translation:** 

**[5273.24s] English:** for cell phones i think uh i don't know why people buy new cell phones  
**Translation:** 

**[5280.00s] English:** you know, because a new one's announced. The cameras are better, but that's kind of domain  
**Translation:** 

**[5284.20s] English:** specific, right? They're putting special purpose hardware to make the processing of images go much  
**Translation:** 

**[5289.54s] English:** better. So that's the way they're doing it. They're not particularly, it's not that the  
**Translation:** 

**[5294.96s] English:** ARM process in there is twice as fast as much as they've added accelerators to help the experience  
**Translation:** 

**[5301.30s] English:** of the phone. Can we talk a little bit about one other exciting space, arguably the same level of  
**Translation:** Vocabulary: accelerators: 加速器; arguably: 可以说

**[5308.84s] English:** impact as your work with RISC is RAID. In 1988, you co-authored a paper, A Case for Redundant  
**Translation:** 

**[5319.38s] English:** Erase of Inexpensive Disks, hence R-A-I-D, RAID. So that's where you introduced the idea of RAID.  
**Translation:** Vocabulary: erase: 删除; redundant: 冗余

**[5327.48s] English:** Incredible that that little, I mean little, that paper kind of had this ripple effect and had a  
**Translation:** 

**[5334.28s] English:** really revolutionary effect. So first, what is RAID?  
**Translation:** Vocabulary: ripple: 波及效应

**[5338.06s] English:** What is RAID?  
**Translation:** 

**[5338.84s] English:** So this is work I did with my colleague, Randy Katz, and a star graduate student,  
**Translation:** Vocabulary: colleague: 同事

**[5343.60s] English:** Garth Gibson. So we had just done the fourth generation RISC project. And Randy Katz,  
**Translation:** 

**[5351.70s] English:** which had an early Apple Macintosh computer, at this time, everything was done with floppy disks,  
**Translation:** Vocabulary: floppy: 软盘; gibson: 吉布森; macintosh: 麦金塔

**[5360.16s] English:** which are old technologies that could store things that didn't have much capacity. And you had to  
**Translation:** 

**[5368.06s] English:** get any work done, you're always sticking your little floppy disk in and out, because they didn't  
**Translation:** Vocabulary: sticking: 插入

**[5372.78s] English:** have much capacity. But they started building what are called hard disk drives, which is magnetic  
**Translation:** 

**[5378.28s] English:** material that can remember information storage for the Mac. And Randy asked the question when he saw  
**Translation:** Vocabulary: randy: 兰迪

**[5385.84s] English:** this disk next to his Mac, gee, these are brand new small things. Before that, for the big computers,  
**Translation:** 

**[5393.98s] English:** the disk would be the size of washing machines.  
**Translation:** 

**[5398.06s] English:** The disk would be the size of something the size of a  
**Translation:** 

**[5400.00s] English:** kind of the size of a book or so.  
**Translation:** 

**[5402.46s] English:** He says, I wonder what we could do with that.  
**Translation:** 

**[5403.76s] English:** Well, Randy was involved  
**Translation:** 

**[5407.14s] English:** in the fourth generation RISC project  
**Translation:** 

**[5410.58s] English:** here at Berkeley in the 80s.  
**Translation:** Vocabulary: berkeley: 伯克利

**[5411.72s] English:** So we figured out a way  
**Translation:** 

**[5413.08s] English:** how to make the computation part,  
**Translation:** Vocabulary: computation: 计算

**[5414.70s] English:** the processor part go a lot faster.  
**Translation:** 

**[5416.54s] English:** But what about the storage part?  
**Translation:** 

**[5419.00s] English:** Can we do something to make it faster?  
**Translation:** 

**[5420.78s] English:** So we hit upon the idea  
**Translation:** 

**[5422.58s] English:** of taking a lot of these disks  
**Translation:** 

**[5425.24s] English:** developed for personal computers  
**Translation:** 

**[5426.50s] English:** and Macintoshes  
**Translation:** 

**[5427.28s] English:** and putting many of them together  
**Translation:** Vocabulary: macintoshes: 苹果电脑

**[5429.28s] English:** instead of one of these  
**Translation:** 

**[5430.02s] English:** washing machine size things.  
**Translation:** 

**[5431.78s] English:** And so we wrote the first draft of the paper  
**Translation:** 

**[5434.46s] English:** and we'd have 40 of these little PC disks  
**Translation:** 

**[5436.70s] English:** instead of one of these  
**Translation:** 

**[5438.60s] English:** washing machine size things.  
**Translation:** 

**[5440.68s] English:** And they would be much cheaper  
**Translation:** 

**[5441.84s] English:** because they're made for PCs.  
**Translation:** 

**[5443.78s] English:** And they could actually kind of be faster  
**Translation:** 

**[5445.36s] English:** because there was 40 of them  
**Translation:** 

**[5446.48s] English:** rather than one of them.  
**Translation:** 

**[5448.20s] English:** And so we wrote a paper like that  
**Translation:** 

**[5449.44s] English:** and sent it to one of our  
**Translation:** 

**[5450.68s] English:** former Berkeley students at IBM.  
**Translation:** 

**[5452.40s] English:** And he said, well, this is all great and good,  
**Translation:** 

**[5453.80s] English:** but what about the reliability of these things?  
**Translation:** Vocabulary: reliability: 可靠性

**[5456.16s] English:** Now you have 40 of these devices,  
**Translation:** 

**[5458.58s] English:** each of which are kind of PC quality.  
**Translation:** 

**[5461.02s] English:** So they're not as good  
**Translation:** 

**[5462.08s] English:** as these IBM washing machines.  
**Translation:** 

**[5463.96s] English:** IBM dominated the storage genesis.  
**Translation:** 

**[5468.52s] English:** So the reliability is going to be awful.  
**Translation:** 

**[5470.62s] English:** And so when we calculated it out,  
**Translation:** 

**[5472.34s] English:** instead of it breaking on average once a year,  
**Translation:** 

**[5475.52s] English:** it would break every two weeks.  
**Translation:** 

**[5477.44s] English:** So we thought about the idea  
**Translation:** 

**[5479.62s] English:** and said, well,  
**Translation:** 

**[5480.94s] English:** we got to address the reliability.  
**Translation:** 

**[5482.76s] English:** So we did it originally performance,  
**Translation:** 

**[5484.38s] English:** but we had to do reliability.  
**Translation:** 

**[5485.80s] English:** So the name redundant array  
**Translation:** 

**[5488.20s] English:** of inexperienced people,  
**Translation:** Vocabulary: inexperienced: 缺乏经验; redundant: 冗余

**[5488.98s] English:** is array of these disks,  
**Translation:** 

**[5491.02s] English:** inexpensive like for PCs,  
**Translation:** 

**[5492.80s] English:** but we have extra copies.  
**Translation:** 

**[5494.80s] English:** So if one breaks,  
**Translation:** 

**[5496.86s] English:** we won't lose all the information.  
**Translation:** 

**[5498.20s] English:** We'll have enough redundancy  
**Translation:** 

**[5499.82s] English:** that we could let some break  
**Translation:** 

**[5501.56s] English:** and we can still preserve the information.  
**Translation:** 

**[5503.24s] English:** So the name is an array of inexpensive disks.  
**Translation:** 

**[5505.58s] English:** This is a collection of these PCs  
**Translation:** 

**[5507.94s] English:** and the R part of the name  
**Translation:** 

**[5509.62s] English:** was the redundancy.  
**Translation:** 

**[5511.36s] English:** So they'd be reliable.  
**Translation:** 

**[5512.28s] English:** And it turns out if you put a modest number  
**Translation:** 

**[5514.34s] English:** of extra disks in one of these arrays,  
**Translation:** 

**[5516.34s] English:** it could actually not only be  
**Translation:** 

**[5518.14s] English:** as faster and cheaper,  
**Translation:** 

**[5520.00s] English:** that one of these washing machine disks,  
**Translation:** 

**[5521.46s] English:** it could be actually more reliable  
**Translation:** 

**[5522.94s] English:** because you could have a couple of breaks  
**Translation:** 

**[5525.22s] English:** even with these cheap disks,  
**Translation:** 

**[5526.70s] English:** whereas one failure with the washing machine thing  
**Translation:** 

**[5528.90s] English:** would knock it out.  
**Translation:** 

**[5530.64s] English:** Did you have a sense just like with RISC  
**Translation:** 

**[5532.72s] English:** that in the 30 years that followed,  
**Translation:** 

**[5537.50s] English:** RAID would take over as a mechanism for storage?  
**Translation:** 

**[5542.06s] English:** I'd say, I think I'm naturally an optimist,  
**Translation:** 

**[5546.40s] English:** but I thought our ideas were right.  
**Translation:** Vocabulary: optimist: 积极乐观的人

**[5550.50s] English:** I thought kind of like Moore's law,  
**Translation:** 

**[5552.96s] English:** it seemed to me,  
**Translation:** 

**[5553.92s] English:** if you looked at the history of the disk drives,  
**Translation:** 

**[5555.96s] English:** they went from washing machine size things  
**Translation:** 

**[5557.98s] English:** and they were getting smaller and smaller  
**Translation:** 

**[5559.58s] English:** and the volumes were with the smaller disk drives  
**Translation:** 

**[5563.18s] English:** because that's where the PCs were.  
**Translation:** 

**[5565.22s] English:** So we thought that was a technological trend  
**Translation:** 

**[5567.74s] English:** that disk drives,  
**Translation:** 

**[5569.48s] English:** the volume of disk drives was going to be  
**Translation:** 

**[5572.22s] English:** getting smaller and smaller devices,  
**Translation:** 

**[5574.36s] English:** which were true.  
**Translation:** 

**[5574.98s] English:** They were the size of a,  
**Translation:** 

**[5576.40s] English:** I don't know,  
**Translation:** 

**[5577.22s] English:** eight inches diameter,  
**Translation:** 

**[5578.54s] English:** then five inches,  
**Translation:** 

**[5579.48s] English:** then three inches in diameters.  
**Translation:** 

**[5581.26s] English:** And so that it made sense to figure out  
**Translation:** 

**[5583.90s] English:** how to deal things with an array of disks.  
**Translation:** 

**[5586.20s] English:** So I think it was one of those things  
**Translation:** 

**[5587.68s] English:** where logically we think the technological forces  
**Translation:** 

**[5591.84s] English:** were on our side,  
**Translation:** Vocabulary: logically: 合乎逻辑地

**[5592.98s] English:** that it made sense.  
**Translation:** 

**[5594.70s] English:** So we expected it to catch on,  
**Translation:** 

**[5596.98s] English:** but there was that same kind of business question.  
**Translation:** 

**[5599.86s] English:** You know, IBM was the big pusher of these disk drives  
**Translation:** 

**[5602.66s] English:** in the real world  
**Translation:** 

**[5604.60s] English:** where the technical advantage get turned  
**Translation:** 

**[5606.28s] English:** into the technology advantage.  
**Translation:** 

**[5606.40s] English:** To a business advantage or not.  
**Translation:** 

**[5608.48s] English:** It proved to be true.  
**Translation:** 

**[5609.92s] English:** It did.  
**Translation:** 

**[5610.30s] English:** And so, you know,  
**Translation:** 

**[5611.56s] English:** we thought we were sound technically  
**Translation:** 

**[5613.40s] English:** and it was unclear whether the business side,  
**Translation:** 

**[5616.68s] English:** but we kind of,  
**Translation:** 

**[5617.60s] English:** as academics,  
**Translation:** 

**[5618.38s] English:** we believe that technology should win.  
**Translation:** 

**[5620.22s] English:** And it did.  
**Translation:** 

**[5622.02s] English:** And if you look at those 30 years,  
**Translation:** 

**[5624.28s] English:** just from your perspective,  
**Translation:** 

**[5625.88s] English:** are there interesting developments  
**Translation:** 

**[5627.16s] English:** in the space of storage  
**Translation:** 

**[5628.30s] English:** that have happened in that time?  
**Translation:** 

**[5630.40s] English:** Yeah.  
**Translation:** 

**[5630.68s] English:** The big thing that happened,  
**Translation:** 

**[5632.20s] English:** well, a couple of things that happened.  
**Translation:** 

**[5634.08s] English:** What we did had a modest amount of storage,  
**Translation:** 

**[5636.28s] English:** so as redundancy,  
**Translation:** 

**[5639.34s] English:** as people,  
**Translation:** 

**[5640.00s] English:** People built bigger and bigger storage systems.  
**Translation:** 

**[5642.38s] English:** They've added more redundancy so they could add more failures.  
**Translation:** 

**[5645.90s] English:** And the biggest thing that happened in storage is for decades, it was based on things physically spinning called hard disk drives.  
**Translation:** 

**[5655.62s] English:** We used to turn on your computer and it would make a noise.  
**Translation:** Vocabulary: spinning: 旋转

**[5658.56s] English:** What that noise was, was the disk drive spinning.  
**Translation:** 

**[5661.40s] English:** And they were rotating at like 60 revolutions per second.  
**Translation:** Vocabulary: revolutions: 转动; rotating: 旋转

**[5665.56s] English:** And it's like, if you remember the vinyl records, if you've ever seen those, that's what it looked like.  
**Translation:** 

**[5672.86s] English:** And there was like a needle like on a vinyl record that was reading it.  
**Translation:** Vocabulary: vinyl: 乙烯基

**[5676.30s] English:** So the big drive change is switching that over to a semiconductor technology called flash.  
**Translation:** 

**[5681.04s] English:** So within the last, I'd say about decade, is increasing fraction of all the computers in the world are using semiconductor for storage.  
**Translation:** Vocabulary: semiconductor: 半导体

**[5691.16s] English:** The flash drive, instead of being magnetic,  
**Translation:** 

**[5694.36s] English:** they're optical, they're, well, they're a semiconductor writing of information into very densely, and that's been a huge difference.  
**Translation:** 

**[5705.58s] English:** So all the cell phones in the world use flash.  
**Translation:** 

**[5708.04s] English:** Most of the laptops use flash, all the embedded devices use flash instead of storage.  
**Translation:** 

**[5712.84s] English:** Still in the cloud, magnetic disks are more economical than flash, but they use both in the cloud.  
**Translation:** 

**[5720.22s] English:** So it's been a huge change in the storage industry.  
**Translation:** Vocabulary: economical: 经济的

**[5723.04s] English:** This, the,  
**Translation:** 

**[5724.48s] English:** of switching from primarily disk to being primarily semiconductor.  
**Translation:** 

**[5728.46s] English:** For the individual disks, but still the RAID mechanism applies to those different kinds of disks.  
**Translation:** 

**[5732.66s] English:** Yes, the people will still use RAID ideas because it's kind of what's different, you know, kind of interesting, kind of psychologically, if you think about it.  
**Translation:** Vocabulary: psychologically: 心理上

**[5743.72s] English:** People have always worried about the reliability of computing since the earliest days.  
**Translation:** 

**[5747.04s] English:** So kind of, but if we're talking about computation, if your computer makes a mistake in,  
**Translation:** Vocabulary: computation: 计算; computing: 计算; reliability: 可靠性

**[5754.36s] English:** the computer says we, the computer has ways to check and say, oh, we screwed up, we made a mistake.  
**Translation:** 

**[5760.00s] English:** what happens is that program that was running uh you have to redo it which is a hassle for storage  
**Translation:** Vocabulary: hassle: 麻烦

**[5766.74s] English:** if you've sent important information away and it loses that information you go nuts yeah this is  
**Translation:** 

**[5775.08s] English:** the worst oh my god so if you have a laptop and you're not backing it up on the cloud or something  
**Translation:** 

**[5780.52s] English:** like this and your disk drive breaks which it can do you'll lose all that information and you just  
**Translation:** 

**[5786.84s] English:** go crazy right so the importance of reliability for storage is tremendously higher than the  
**Translation:** Vocabulary: tremendously: 极其

**[5792.08s] English:** importance of reliability for computation because of the consequences of it so yes so rate ideas are  
**Translation:** 

**[5797.78s] English:** are still very popular even with the switch of the technology although you know flash drives are more  
**Translation:** 

**[5802.74s] English:** reliable you know if you're not doing anything like backing it up to get some redundancy so  
**Translation:** 

**[5808.56s] English:** they handle it you're you're you're taking great risks you said that for you and possibly for many  
**Translation:** 

**[5816.84s] English:** other people who are doing research don't conflict with each other as one might suspect and in fact  
**Translation:** 

**[5821.88s] English:** they kind of complement each other so maybe a question i have is how has teaching helped you  
**Translation:** 

**[5827.28s] English:** in your research or just in your entirety as a person who both teaches and does research and just  
**Translation:** 

**[5834.98s] English:** thinks and creates new ideas in this world yes i think um i think what happens is is when you're  
**Translation:** Vocabulary: entirety: 整体

**[5841.06s] English:** a college student you know there's this kind of tenure system and doing research so kind of  
**Translation:** 

**[5845.36s] English:** this model that  
**Translation:** 

**[5846.84s] English:** uh you know is popular in america i think america really made it happen is we can attract these  
**Translation:** 

**[5852.54s] English:** really great faculty to research universities because they get to do research as well as teach  
**Translation:** 

**[5858.20s] English:** and that especially in fast-moving fields this means people are up to date and they're teaching  
**Translation:** 

**[5862.60s] English:** those kind of things so but when you run into a really bad professor a really bad teacher  
**Translation:** 

**[5867.48s] English:** i think the students think well this guy must be a great researcher because why else could he be  
**Translation:** 

**[5873.04s] English:** here so as i you know i i after 40 years at berkeley i've been a professor for a long time  
**Translation:** 

**[5876.84s] English:** at berkeley we had a retirement party and i got a chance to reflect and i looked back  
**Translation:** 

**[5880.00s] English:** at some things. That is not my experience. I saw a photograph of five of us in the department who  
**Translation:** 

**[5888.28s] English:** won the Distinguished Teaching Award from campus, a very high honor. I've got one of those, one of  
**Translation:** 

**[5893.12s] English:** the highest honors. So there are five of us on that picture. There's Manuel Blum, Richard Karp,  
**Translation:** Vocabulary: manuel: 布卢姆

**[5901.30s] English:** me, Randy Kass, and John Osterhout, contemporaries of mine. I mentioned Randy already. All of us are  
**Translation:** 

**[5907.06s] English:** in the National Academy of Engineering. We've all won the Distinguished Teaching Award. Blum,  
**Translation:** Vocabulary: contemporaries: 同时代的人; randy: Rand Kass

**[5912.96s] English:** Karp, and I all have Turing Awards, the highest award in computing. So that's the opposite,  
**Translation:** 

**[5921.62s] English:** right? What happens is they're highly correlated. So probably the other way to think of it,  
**Translation:** Vocabulary: computing: 计算机; correlated: 相关; turing: 图灵

**[5928.88s] English:** if you're very successful people, maybe successful at everything they do, it's not an either or.  
**Translation:** 

**[5934.72s] English:** But it's an interesting question whether it's  
**Translation:** 

**[5936.84s] English:** specific or not.  
**Translation:** 

**[5937.06s] English:** Specifically, that's probably true, but specifically for teaching, if there's something  
**Translation:** 

**[5940.90s] English:** in teaching that, it's the Richard Feynman idea, is there something about teaching that actually  
**Translation:** 

**[5946.80s] English:** makes your research, makes you think deeper and more outside the box and more insightful?  
**Translation:** 

**[5952.76s] English:** Absolutely. I was going to bring up Feynman. I mean, he criticized the Institute of Advanced  
**Translation:** 

**[5956.46s] English:** Studies. So the Institute of Advanced Studies was this thing that was created near Princeton  
**Translation:** Vocabulary: feynman: 费曼; princeton: 普林斯顿

**[5961.48s] English:** where Einstein and all these smart people went. And when he was invited, he thought it was a  
**Translation:** 

**[5966.36s] English:** terrible idea.  
**Translation:** Vocabulary: einstein: 爱因斯坦

**[5967.06s] English:** This is a university. It was supposed to be heaven, right? A university without any teaching.  
**Translation:** 

**[5972.66s] English:** But he thought it was a mistake. It's getting up in the classroom and having to explain things to  
**Translation:** 

**[5977.00s] English:** students and having them ask questions like, well, why is that true? Makes you stop and think.  
**Translation:** 

**[5981.96s] English:** So he thought, and I agree, I think that interaction between a great research university  
**Translation:** 

**[5988.50s] English:** and having students with bright young minds asking hard questions the whole time is synergistic.  
**Translation:** 

**[5994.84s] English:** And a university without teaching,  
**Translation:** Vocabulary: synergistic: 相辅相成

**[5996.84s] English:** teaching wouldn't be as vital.  
**Translation:** 

**[6000.00s] English:** uh and exciting a place and i think it helps stimulate the the research another romanticized  
**Translation:** Vocabulary: stimulate: 激发

**[6007.62s] English:** question but what's your uh favorite concept or idea to teach what inspires you or you see  
**Translation:** 

**[6014.00s] English:** inspire the students is there something that pops to mind or or puts the fear of god in them i don't  
**Translation:** Vocabulary: inspires: 激励

**[6019.22s] English:** know whichever is most effective uh i mean in general i think people are surprised i've seen  
**Translation:** 

**[6025.66s] English:** a lot of people who don't think they like teaching uh come come give guest lectures or teach a course  
**Translation:** Vocabulary: whichever: 任一

**[6031.68s] English:** and get hooked on seeing the lights turn on right is people you can explain something to people that  
**Translation:** 

**[6037.74s] English:** they don't understand and suddenly they get something you know that's that's not that's  
**Translation:** 

**[6042.76s] English:** important and difficult and just seeing the lights turn on is a you know it's a real satisfaction  
**Translation:** 

**[6048.06s] English:** there i don't think there's any uh in a specific example of that it's just the general joy of  
**Translation:** 

**[6055.40s] English:** seeing  
**Translation:** 

**[6055.66s] English:** them uh seeing them understand i have to talk about this because i've wrestled i do martial  
**Translation:** Vocabulary: martial: 武术; wrestled: 挣扎

**[6063.24s] English:** arts yeah of course i love wrestling i'm a huge i'm russian so i oh sure i have talked to dan  
**Translation:** 

**[6068.92s] English:** gable on oh yeah guest so i know yan gable was my era kind of guy so you wrestled at ucla among  
**Translation:** Vocabulary: gable: 房山; wrestling: 摔跤

**[6077.00s] English:** many other things you've done in your life uh competitively in sports and science so on you've  
**Translation:** 

**[6081.88s] English:** you've wrestled maybe again continuing  
**Translation:** Vocabulary: competitively: 竞争地

**[6085.40s] English:** with the romanticized questions but uh what have you learned about life yeah and maybe even science  
**Translation:** 

**[6090.76s] English:** from wrestling or from yeah that's in fact um i wrestled at ucla but also at el camino community  
**Translation:** Vocabulary: camino: 小径

**[6097.68s] English:** college and just right now we were in the state of california we were state champions at el camino  
**Translation:** 

**[6103.68s] English:** and in fact i was talking to my mom and uh i got into ucla but i decided to go to the community  
**Translation:** Vocabulary: california: 加利福尼亚

**[6110.02s] English:** college which is it's much harder to go to ucla than the community college and i asked well i've  
**Translation:** 

**[6115.40s] English:** got to go to the community college and i said why did i make the decision because i thought it was  
**Translation:** 

**[6117.08s] English:** because of my girlfriend she said well it was the girlfriend and and you thought there  
**Translation:** 

**[6120.00s] English:** wrestling team was really good and we were right we had a great wrestling team we we actually uh  
**Translation:** 

**[6126.02s] English:** wrestled against ucla at a tournament and we beat ucla it is a community college which is just  
**Translation:** 

**[6132.04s] English:** freshmen and sophomores and the part of reason i brought this up is i'm going to go they've  
**Translation:** Vocabulary: freshmen: 大一学生; sophomores: 大二学生

**[6136.70s] English:** invited me back at el camino to give a uh a lecture next month and so i'm we've my friend  
**Translation:** 

**[6145.32s] English:** who was on the wrestling team and uh that we're still together we're right now reaching out to  
**Translation:** 

**[6150.00s] English:** other members of the wrestling team we can get together for a reunion but in terms of me it was  
**Translation:** 

**[6155.30s] English:** a huge difference i was i was both i was kind of the age cut off i was it was december 1st and so  
**Translation:** 

**[6161.54s] English:** i was almost always the youngest person in my class and i matured later on you know our family  
**Translation:** 

**[6168.96s] English:** matured later so i was almost always the smallest guy so you know i took you know kind of nerdy  
**Translation:** Vocabulary: nerdy: 书呆子

**[6174.92s] English:** courses  
**Translation:** 

**[6175.32s] English:** but i was wrestling so wrestling was huge for my uh you know self-confidence in uh high school  
**Translation:** 

**[6182.12s] English:** and then you know i kind of got bigger at el camino and in college and so i had this uh kind  
**Translation:** 

**[6187.98s] English:** of physical self-confidence and it's translated into research self-confidence uh and uh and also  
**Translation:** 

**[6198.34s] English:** kind of i've had this feeling even today in my 70s you know if something  
**Translation:** 

**[6205.32s] English:** if something going on in the streets that is bad physically i'm not going to ignore it right i'm  
**Translation:** 

**[6209.46s] English:** going to stand up and try and straighten that out and that kind of confidence just carries through  
**Translation:** 

**[6214.22s] English:** the entirety of your life yeah and and the same things happens intellectually if there's something  
**Translation:** Vocabulary: entirety: 整个部分; intellectually: 智力上; straighten: 整理

**[6218.42s] English:** going on where people are saying something that's not true i feel it's my job to stand up and just  
**Translation:** 

**[6224.00s] English:** like i would in the street if there's something going on somebody attacking some woman or  
**Translation:** 

**[6228.16s] English:** something i'm not i'm not standing by and letting that get away so i feel it's my job to stand up  
**Translation:** 

**[6233.50s] English:** so it's kind of ironically translated  
**Translation:** Vocabulary: ironically: 反讽地

**[6235.32s] English:** the other things that turned out for both i had really great college and  
**Translation:** 

**[6240.00s] English:** high school coaches. And they believed, even though wrestling is an individual sport,  
**Translation:** Vocabulary: wrestling: 摔跤

**[6244.94s] English:** that we would be more successful as a team if we bonded together, do things that we would support  
**Translation:** 

**[6250.28s] English:** each other rather than everybody, you know, in wrestling, it's a one-on-one and you could be  
**Translation:** 

**[6254.24s] English:** everybody's on their own, but he felt if we bonded as a team, we'd succeed. So I kind of picked up  
**Translation:** 

**[6259.74s] English:** those skills of how to form successful teams and how do you, from wrestling. And so I think one of  
**Translation:** 

**[6265.72s] English:** most people would say, one of my strengths is I can create teams of faculty, large teams of  
**Translation:** 

**[6272.16s] English:** faculty, grad students pull all together for a common goal and, you know, and often be successful  
**Translation:** 

**[6278.02s] English:** at it. But I got, I got both of those things from wrestling. Also, I think I heard this line about  
**Translation:** 

**[6284.20s] English:** if people are in kind of, you know, collision, you know, sports with physical contact, like  
**Translation:** Vocabulary: collision: 碰撞

**[6290.08s] English:** wrestling or football and stuff like that, people are a little bit more, you know, assertive or  
**Translation:** 

**[6295.04s] English:** something.  
**Translation:** Vocabulary: assertive: 自信

**[6295.72s] English:** And so I think, I think that also comes through as, you know, in, I was, I didn't shy away from  
**Translation:** 

**[6302.16s] English:** the risk-sys debates, you know, I was, I enjoyed taking on the arguments and stuff like that. So  
**Translation:** 

**[6307.44s] English:** it was, it was, I'm really glad I did wrestling. I think it was really good for my self-image and  
**Translation:** 

**[6312.90s] English:** I learned a lot from it. So I think that's, you know, sports done well, you know, there's really  
**Translation:** 

**[6317.88s] English:** lots of positives you can take about it, leadership, you know, how to, how to form teams  
**Translation:** 

**[6324.50s] English:** and how, how to be successful.  
**Translation:** Vocabulary: positives: 积极方面

**[6325.72s] English:** So we've talked about metrics a lot. There's a really cool, in terms of bench press and weightlifting  
**Translation:** 

**[6331.44s] English:** pound years metric that you've developed that we don't have time to talk about, but it's a, it's a  
**Translation:** Vocabulary: weightlifting: 举重

**[6335.48s] English:** really cool one that people should look into. It's rethinking the way we think about metrics and  
**Translation:** 

**[6339.66s] English:** weightlifting. But let me talk about metrics more broadly, since that appeals to you in all forms.  
**Translation:** 

**[6345.46s] English:** Let's look at the most ridiculous, the biggest question of the meaning of life.  
**Translation:** 

**[6350.32s] English:** If you were to try to put metrics on a life well-lived, what would those metrics be?  
**Translation:** 

**[6355.72s] English:** Yeah, a friend of mine, Randy Katz said this, he said,  
**Translation:** 

**[6360.00s] English:** And, you know, when when it's time to sign off, it's it's the measure isn't the number of zeros in your bank account.  
**Translation:** 

**[6368.54s] English:** It's the number of inches in the obituary in The New York Times.  
**Translation:** 

**[6372.48s] English:** As he said it, I think, you know, having and, you know, this is a cliche is that people don't die wishing they'd spent more time in the office.  
**Translation:** Vocabulary: obituary: 讣告

**[6382.32s] English:** Right. As I reflect upon my career, there have been, you know, a half a dozen or a dozen things.  
**Translation:** 

**[6389.42s] English:** I'd say I've been proud of a lot of them aren't papers or scientific results.  
**Translation:** 

**[6393.66s] English:** Certainly my family, my wife, we've been married more than 50 years, kids and grandkids.  
**Translation:** 

**[6400.14s] English:** That's really precious education things I've done.  
**Translation:** Vocabulary: grandkids: 孙子女

**[6404.38s] English:** I'm very proud of, you know, books and courses.  
**Translation:** 

**[6408.90s] English:** I did some help with underrepresented groups that was effective.  
**Translation:** Vocabulary: underrepresented: 少数群体

**[6412.82s] English:** So it was interesting to see what were the things I reflected.  
**Translation:** 

**[6415.94s] English:** You know, I had hundreds of papers.  
**Translation:** 

**[6418.38s] English:** But some of them.  
**Translation:** 

**[6419.54s] English:** Some of them were the papers like the risk and rate stuff that I'm proud of, but a lot of them were or were not those things.  
**Translation:** 

**[6424.42s] English:** So people who are just spend their lives, you know, going after the dollars or going after all the papers in the world, you know, that's probably not the things that are afterwards you're going to care about.  
**Translation:** 

**[6435.84s] English:** When I was just when I got the offer from Berkeley before I showed up, I read a book where they interviewed a lot of people and all works of life.  
**Translation:** 

**[6445.48s] English:** And what I got out of that book was the people who felt good about what they did was the people.  
**Translation:** 

**[6449.42s] English:** Who affected people as opposed to things that were more transitory.  
**Translation:** Vocabulary: transitory: 短暂的

**[6452.92s] English:** So I came into this job assuming that it wasn't going to be the papers is going to be relationships with the people over time that I would I would value.  
**Translation:** 

**[6461.32s] English:** And that was a correct assessment.  
**Translation:** 

**[6462.90s] English:** Right. It's it's the people you work with, the people you can influence, the people you can help is the things that you feel good about towards the end of your career.  
**Translation:** 

**[6470.52s] English:** It's not not the stuff that's more transitory.  
**Translation:** 

**[6474.24s] English:** I don't think there's a better way to end it than talking about your family.  
**Translation:** 

**[6478.28s] English:** The over 50.  
**Translation:** 

**[6480.00s] English:** Years of being married to your childhood sweetheart.  
**Translation:** 

**[6482.78s] English:** One thing I could add is when you tell people you've been married 50 years, they want to know why.  
**Translation:** 

**[6488.04s] English:** How?  
**Translation:** 

**[6488.68s] English:** Why?  
**Translation:** 

**[6489.14s] English:** I can tell you the nine magic words that you need to say to your partner to keep a good relationship.  
**Translation:** 

**[6495.90s] English:** And the nine magic words are, I was wrong.  
**Translation:** 

**[6498.82s] English:** You were right.  
**Translation:** 

**[6500.10s] English:** I love you.  
**Translation:** 

**[6501.12s] English:** Okay.  
**Translation:** 

**[6501.64s] English:** And you got to say all nine.  
**Translation:** 

**[6502.80s] English:** You can't say, I was wrong.  
**Translation:** 

**[6504.34s] English:** You were right.  
**Translation:** 

**[6504.84s] English:** You're a jerk.  
**Translation:** 

**[6505.34s] English:** You can't say that.  
**Translation:** 

**[6506.70s] English:** So freely acknowledging that you made a mistake, the other person was right, and that you love them really gets over a lot of bumps in the road.  
**Translation:** 

**[6516.58s] English:** So that's what I pass along.  
**Translation:** 

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

**[6536.70s] English:** Please consider supporting this podcast by going to jordanharbinger.com slash Lex and downloading Cash App and using code LexPodcast.  
**Translation:** Vocabulary: harbinger: 先兆; jordanharbinger: 乔恩哈伯; sponsors: 赞助商

**[6545.74s] English:** Click the links, buy the stuff.  
**Translation:** 

**[6548.12s] English:** It's the best way to support this podcast and the journey I'm on.  
**Translation:** 

**[6551.74s] English:** If you enjoy this thing, subscribe on YouTube, review it with 5,000, have a podcast, support it on Patreon, or connect with me on Twitter at Lex Friedman, spelled without the E.  
**Translation:** 

**[6563.26s] English:** Try to figure out how to do that.  
**Translation:** Vocabulary: subscribe: 订阅

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

**[6578.76s] English:** Thank you for listening and hope to see you next time.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
