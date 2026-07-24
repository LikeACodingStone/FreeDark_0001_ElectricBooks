# Podcast vocabulary notes
Source file: Lex Fridman - Brendan Eich： JavaScript, Firefox, Mozilla, and Brave ｜ Lex Fridman Podcast #160.opus

**[0.00s] English:** The following is a conversation with Brendan Eich, creator of the JavaScript programming language, co-founder of Mozilla, which created the Firefox browser, and now co-founder and CEO of Brave Software, which has created the Brave browser.  
**Translation:** 

**[15.42s] English:** Each of these are revolutionary technologies.  
**Translation:** 

**[18.46s] English:** JavaScript is one of the most widely used and impactful programming languages in the world.  
**Translation:** 

**[24.24s] English:** Firefox pioneered many browser ideas that we love today or even take for granted today.  
**Translation:** 

**[31.42s] English:** And Brave is looking to revolutionize not only the browser, but content creation online and the nature of the Internet to make it fundamentally about respecting people's control over their data.  
**Translation:** 

**[43.38s] English:** Quick mention of our sponsors.  
**Translation:** Vocabulary: fundamentally: 从根本上; revolutionize: 革新; sponsors: 赞助商

**[45.46s] English:** The Jordan Harbinger Show, Sun Basket Meal Delivery Service, BetterHelp Online Therapy, and 8Sleep Self-Cooling Mattress.  
**Translation:** 

**[53.42s] English:** Click the link.  
**Translation:** Vocabulary: harbinger: 先兆; mattress: 床垫

**[54.24s] English:** Click the sponsor links to get a discount and to support this podcast.  
**Translation:** 

**[58.08s] English:** As a side note, let me say that there's a tension between theory and engineering that I've been thinking a lot about.  
**Translation:** 

**[65.20s] English:** I tweeted something like, good execution is more important than a good idea, but one helps the other.  
**Translation:** 

**[71.78s] English:** I think the wording of that sucks, but what I mean is a good idea is a must.  
**Translation:** 

**[76.96s] English:** But in my experience, good ideas are in abundance.  
**Translation:** 

**[80.76s] English:** Good execution, on the other hand, is rare.  
**Translation:** 

**[83.42s] English:** I think some of you are familiar with the term good execution.  
**Translation:** 

**[84.22s] English:** Getting that mix of good timing, good idea, and good execution is essential.  
**Translation:** 

**[88.16s] English:** Getting that mix right is tough.  
**Translation:** 

**[89.96s] English:** And Brendan, somehow, multiple times in his career, did just that.  
**Translation:** Vocabulary: brendan: 布兰登

**[94.22s] English:** I'm starting to believe it's more art than science, like most interesting things in life.  
**Translation:** 

**[99.18s] English:** If you enjoy this thing, subscribe on YouTube, review it on Apple Podcasts, follow it on Spotify, support it on Patreon, or connect with me on Twitter at Lex Friedman.  
**Translation:** Vocabulary: subscribe: 订阅

**[108.80s] English:** And now, here's my conversation with Brendan Eich.  
**Translation:** 

**[113.14s] English:** When did you first start?  
**Translation:** 

**[114.22s] English:** Fall in love with programming.  
**Translation:** 

**[115.88s] English:** I didn't program a lot when I was in high school, but I had a friend who had a Commodore.  
**Translation:** Vocabulary: commodore: 家用电脑

**[120.00s] English:** pet and after we saw star wars he said hey let's make a basic uh program that does the death star  
**Translation:** 

**[126.84s] English:** trench run and it was just you know simple 2d graphics and i didn't know what i was doing so  
**Translation:** Vocabulary: trench: 战壕

**[131.90s] English:** i just helped him out uh on the math and stuff like that i was a math and science kid i was  
**Translation:** 

**[136.32s] English:** really into uh the hp calculators of the early mid 70s these were the rpn they were really  
**Translation:** Vocabulary: calculators: 计算器

**[142.02s] English:** strongly built and as all right goldfinger instead of gold divinely heavy there's probably some gold  
**Translation:** 

**[148.14s] English:** in them too gold metalization but they were awesome calculators and they had all the  
**Translation:** Vocabulary: divinely: 神一般; goldfinger: 金手指

**[152.12s] English:** scientific functions so i was really into that um so i aimed towards physics um i was a little  
**Translation:** 

**[159.04s] English:** late for the i think the you know the 20th century golden age and i read a lot of science fiction so  
**Translation:** 

**[163.86s] English:** i was like yeah it's on the hyper drives and warp drives and uh physics was not going to get there  
**Translation:** 

**[169.18s] English:** quickly and i started hacking on computers while i was studying physics as an undergraduate  
**Translation:** Vocabulary: hacking: 编程; hyper: 高速; undergraduate: 本科生

**[174.18s] English:** at santa clara university and um  
**Translation:** 

**[178.14s] English:** you know i dodged the fortran bullet because i was in the science department instead of the  
**Translation:** Vocabulary: clara: 圣克拉拉; dodged: 躲过

**[182.36s] English:** engineering department where they still did fortran card decks i think they had an auto  
**Translation:** 

**[186.42s] English:** collator but uh we were using pascal and uh i got one of the first portable c compilers uh  
**Translation:** Vocabulary: collator: 自动分类机; compilers: 编译器; pascal: 帕斯卡语言

**[194.20s] English:** ports to the deck mini computers we were using and i i fell in love with programming just based on  
**Translation:** 

**[200.38s] English:** um you know procedural abstraction uh pascal just what now would be considered a  
**Translation:** Vocabulary: abstraction: 抽象

**[208.14s] English:** old school like structured programming from the 70s um nicholas veert the creator of pascal was a  
**Translation:** 

**[213.78s] English:** good writer and a good pedagogue right he always at eth would do these courses where it's like  
**Translation:** Vocabulary: pedagogue: 教育家

**[218.66s] English:** build your own computer build your own compiler build your own operating system scratch yeah kind  
**Translation:** 

**[223.76s] English:** of and uh i know some people who are grad students under him instead he was um he would torture the  
**Translation:** 

**[230.16s] English:** students with things like this custom email system that had 25 word limit and uh things like that i  
**Translation:** 

**[236.94s] English:** unfortunately dodged the fortran bullet because i was in the science department and i was in the  
**Translation:** 

**[238.14s] English:** college both the pascal and the fortran bullet  
**Translation:** 

**[240.00s] English:** Could you maybe linger on the Pascal?  
**Translation:** 

**[244.68s] English:** What kind of programming language was it?  
**Translation:** 

**[246.36s] English:** What is it reminiscent of today?  
**Translation:** Vocabulary: reminiscent: 类似

**[248.18s] English:** Because it sounds like it may have had an impact on your own trajectory.  
**Translation:** 

**[252.62s] English:** Yeah, it was in the ALGOL family.  
**Translation:** Vocabulary: trajectory: 人生轨迹

**[254.54s] English:** And ALGOL was the big successful language design and compiler project in the 60s.  
**Translation:** 

**[262.96s] English:** It had a successor called ALGOL 68, which was ambitious but not as successful.  
**Translation:** 

**[266.90s] English:** But Pascal was kind of a wordy procedures and functions language.  
**Translation:** 

**[272.38s] English:** It distinguished between functions, which return a value, and procedures, which don't, which just compute.  
**Translation:** Vocabulary: wordy: 啰嗦的

**[277.92s] English:** And you could say that whole ALGOL family went into Ada.  
**Translation:** 

**[282.54s] English:** Pascal had a second life thanks to Borland with Turbo Pascal, which was hugely successful.  
**Translation:** Vocabulary: turbo: 涡轮增压

**[288.42s] English:** I think in large part due to Anders Helzberg, who then went to Microsoft and did C Sharp and done that with his team there.  
**Translation:** 

**[294.44s] English:** And it's done really well.  
**Translation:** Vocabulary: helzberg: 赫尔兹伯格

**[295.26s] English:** Doing TypeScript.  
**Translation:** 

**[296.54s] English:** Type JavaScript.  
**Translation:** 

**[297.72s] English:** So, yeah, there's a lineage here.  
**Translation:** 

**[300.58s] English:** But I was also interested in C and Unix by the time I was an undergrad because people were bringing Unix up on all sorts of hardware.  
**Translation:** Vocabulary: lineage: 血统; undergrad: 本科生

**[308.80s] English:** I had some friends who were doing their own wire-wrapped computers, 6820 maybe.  
**Translation:** 

**[314.52s] English:** And I was wire-wrapping for my engineering course, 6809 or something simpler, building a computer on a board.  
**Translation:** 

**[322.54s] English:** And I wanted to build a more ambitious one and port Unix to it, but I picked the wrong processor.  
**Translation:** 

**[327.00s] English:** I picked the National Semiconductor NS16032, which was this amazing, you know, CISC, complex instruction set computer.  
**Translation:** Vocabulary: processor: 处理器; semiconductor: 半导体

**[337.10s] English:** And not the reduced instruction set computers that were just being contemplated into the mid-'80s.  
**Translation:** 

**[343.50s] English:** And RISC ultimately won out.  
**Translation:** Vocabulary: contemplated: 考虑

**[345.38s] English:** RISC won in some ways.  
**Translation:** 

**[346.36s] English:** It dissolved into, you have both.  
**Translation:** 

**[349.04s] English:** Now you have these superscalar architectures where, like, Intel has kept probably too much backward compatibility at the instruction level.  
**Translation:** 

**[356.28s] English:** But that's just, there's a front end that parses that into these, you know, these wires.  
**Translation:** Vocabulary: backward: 落后; compatibility: 兼容性; parses: 解析; superscalar: 超标量

**[360.00s] English:** internal instruction. So the very long instruction word research that was also interesting at the  
**Translation:** 

**[366.58s] English:** time kind of became the microarchitecture inside the backward compatible Intel. But I picked the  
**Translation:** Vocabulary: compatible: 兼容的; microarchitecture: 微架构

**[371.98s] English:** national semi chip and it never got made successfully. It was full of bugs and I never  
**Translation:** 

**[376.62s] English:** could have brought it up. But I went on out of physics after three years into math computer  
**Translation:** 

**[382.14s] English:** science. And like I said, I did it because I saw I was being sort of childlike and naive about  
**Translation:** 

**[387.94s] English:** physics. And I thought, meanwhile, the valley is go go for computers, the Apple to write the PC,  
**Translation:** Vocabulary: childlike: 幼稚; naive: 天真

**[395.14s] English:** the Intel 8086, 8088 based PC, IBM, you know, gave Microsoft the future for, you know, somewhat fishy  
**Translation:** 

**[405.86s] English:** deal. So it was wide open in the computing space. But in physics, you were as optimistic about  
**Translation:** Vocabulary: computing: 计算机领域; fishy: 可疑交易; optimistic: 充满希望

**[411.58s] English:** physics. No, I mean, I was one of three brothers who were all in the same grade. I have a twin.  
**Translation:** 

**[417.68s] English:** And  
**Translation:** 

**[417.86s] English:** I  
**Translation:** 

**[417.94s] English:** younger brother who skipped second grade and was with us the whole time after that. And, you know,  
**Translation:** 

**[423.84s] English:** he went on, he actually studied under Kip Thorne at Caltech. But he also didn't, he ended up in  
**Translation:** 

**[429.14s] English:** software physics.  
**Translation:** Vocabulary: caltech: 加州理工学院

**[432.00s] English:** Does it make you sad that theoretical physics, even with string theory, hasn't really had any  
**Translation:** 

**[439.00s] English:** foundational breakthroughs in the latter part of the 20th century?  
**Translation:** Vocabulary: breakthroughs: 重大进展; foundational: 基础性的

**[443.00s] English:** Yeah, in fact, I'd say the problem is theory over experiment. I would say,  
**Translation:** 

**[447.62s] English:** you know, we need more Aristotle and less Plato. You know, mathematics is not all physical. There are  
**Translation:** Vocabulary: aristotle: 亚里士多德

**[453.94s] English:** lots of mathematics that cannot be realized, as far as I know, in this world. So to understand the  
**Translation:** 

**[459.54s] English:** world, you need to do experiments. You need to not just dream up inductive theories that could have  
**Translation:** Vocabulary: cannot: 不能; inductive: 归纳

**[465.76s] English:** lots of alternative theories competing with them, with no way to decide between them, except  
**Translation:** 

**[470.34s] English:** aesthetics, which is not a good guide, in my opinion.  
**Translation:** Vocabulary: aesthetics: 审美

**[472.82s] English:** I don't know if you are friends with or have a relationship with Elon Musk.  
**Translation:** 

**[476.98s] English:** Where's the...  
**Translation:** 

**[477.62s] English:** In terms of, like, what you would love to see in the future?  
**Translation:** 

**[480.00s] English:** to see our society investing in building up is it closer to elon or is it closer to  
**Translation:** 

**[485.78s] English:** feynman and einstein and those well those gentlemen are no longer with us and i think  
**Translation:** 

**[491.04s] English:** that's noticed so like i said the real glory days of physics the famous pictures from germany  
**Translation:** 

**[495.76s] English:** before the second war were uh just a fantastic assembly of brains um you know schrodinger and  
**Translation:** 

**[502.52s] English:** einstein and physics i think took a wrong turn that maybe all all of um i would say western  
**Translation:** Vocabulary: einstein: 爱因斯坦; schrodinger: 薛定谔

**[509.40s] English:** science took in going for models over reality right you see this in all sorts of fields now  
**Translation:** 

**[515.46s] English:** we can build models that are very predictive and generative and then we build actual devices or you  
**Translation:** Vocabulary: generative: 生成性的; predictive: 预测性的

**[520.64s] English:** know semiconductors things like that that's that's good i'm not dismissing that uh we need good  
**Translation:** 

**[524.86s] English:** models we need to experiment and prove them and and test them but the problem i've seen in physics  
**Translation:** Vocabulary: dismissing: 忽视; semiconductors: 半导体

**[531.56s] English:** which you see certainly in economics um the dismal science and you see surprisingly in other so-called  
**Translation:** 

**[539.40s] English:** models that um don't really have to be um tested against reality they can instead become policy  
**Translation:** Vocabulary: dismal: 悲观的

**[547.10s] English:** tools or they can become like i said uh one of a large family of alternate theories that could be  
**Translation:** 

**[553.74s] English:** as predictive but nobody's doing the winnowing out that's such an interesting tension in society  
**Translation:** Vocabulary: winnowing: 筛选

**[558.60s] English:** you see this in even the softer sciences which have a deep love for like psychology you see this  
**Translation:** 

**[564.92s] English:** in epidemiology now with the virus absolutely it's this tension of  
**Translation:** Vocabulary: epidemiology: 流行病学

**[569.40s] English:** you know how much of the world can we understand through just a beautifully fit model and then at  
**Translation:** 

**[575.58s] English:** the same time my main work is in machine learning where it's like there is no provable thing usually  
**Translation:** Vocabulary: provable: 可证明的

**[583.86s] English:** it's just it's kind of you it's all about just getting the right data set and getting tricks and  
**Translation:** 

**[588.78s] English:** so on and there's this tension even in my own soul of like i go i grew up on theoretical computer  
**Translation:** 

**[594.50s] English:** science like i love the approximation algorithms like all of the  
**Translation:** 

**[599.40s] English:** that like  
**Translation:** Vocabulary: approximation: 近似算法

**[600.00s] English:** different complexity classes just those little puzzles i mean i don't know do you to you as  
**Translation:** 

**[605.90s] English:** somebody who was in math and computer science and then ended up going into places where you  
**Translation:** 

**[611.74s] English:** engineer some of the most impactful things in this world do you see the p versus np all that  
**Translation:** 

**[619.06s] English:** whole space is interesting at all yeah uh it's it's not that useful in practice right people are  
**Translation:** 

**[625.04s] English:** using it uh with sort of crypto analysis or asymptotic arguments about you know can can we  
**Translation:** 

**[631.44s] English:** have a quantum resistant crypto algorithm things like that which may not be practical right if you  
**Translation:** Vocabulary: algorithm: 算法; asymptotic: 渐近的; crypto: 加密; resistant: 抗御的

**[636.84s] English:** if you follow mikhail diakonov or gil kalai there are big questions about how  
**Translation:** 

**[641.76s] English:** how quantum computing will scale up um how practical it will be is that something that  
**Translation:** Vocabulary: computing: 计算

**[647.44s] English:** you think about quantum computing and not except for spare time like you said i'm not using this  
**Translation:** 

**[652.56s] English:** kind of computer science in practice because  
**Translation:** 

**[655.04s] English:** almost everything now is engineering um and finding ways to get um computers to be more  
**Translation:** 

**[662.38s] English:** useful for people which goes from you know design problems which are really kind of an art like  
**Translation:** 

**[667.62s] English:** you've said anything you can't automate is an art yeah well um we can have you know machine learning  
**Translation:** 

**[672.36s] English:** composed music and it can imitate you can train it it can sound kind of decent but maybe lacking  
**Translation:** Vocabulary: automate: 自动化

**[676.90s] English:** that je ne sais quoi but you know user interface still i think requires uh human art so speaking  
**Translation:** 

**[684.12s] English:** of things that  
**Translation:** Vocabulary: interface: 用户界面

**[685.04s] English:** uh didn't follow a perfect theory and model uh javascript so there's two things one had an  
**Translation:** 

**[691.80s] English:** impact on the world at a huge scale obviously and it's also still is one of probably the most  
**Translation:** 

**[699.42s] English:** popular programming language in the world so can we go back to the origin story uh can you tell  
**Translation:** 

**[705.76s] English:** the story of how javascript was created yeah i was at sulking graphics after graduate school  
**Translation:** Vocabulary: sulking: 沮丧

**[710.84s] English:** for seven years and it got to be big and successful in  
**Translation:** 

**[715.04s] English:** universalized and political and i thought um kind of bored  
**Translation:** Vocabulary: universalized: 普遍化的

**[720.00s] English:** and a friend who'd been there went to one of the last of the super companies the super startups in  
**Translation:** 

**[726.16s] English:** in the early 90s there were several i suppose general magic was a little after that around  
**Translation:** Vocabulary: startups: 初创公司

**[730.98s] English:** the same time but micro unity was that company that i went to and it was because my friend uh  
**Translation:** 

**[736.30s] English:** jeff weinstein had gone there from silicon graphics he recruited me and micro unity was  
**Translation:** Vocabulary: recruited: 招募

**[741.24s] English:** doing everything so this was like the ultimate sort of pretend grad school it was doing a new fab  
**Translation:** 

**[747.10s] English:** new semiconductor process it was doing new um analog and digital circuits on the same very  
**Translation:** Vocabulary: analog: 模拟电路

**[753.76s] English:** large but not wafer scale chip originally it was um five centimeters on a side it was it was really  
**Translation:** 

**[760.86s] English:** hot too so i needed a water cooler um it was a cray killer and then they shrunk it and they  
**Translation:** Vocabulary: wafer: 薄片

**[766.40s] English:** tried to do a home sort of media processor that was essentially a barrel processor but you could  
**Translation:** 

**[772.18s] English:** think of um trying to do all the things that we now see in modern architecture  
**Translation:** Vocabulary: processor: 处理器

**[777.10s] English:** architectures uh with short vector instructions and um sort of wide instructions or multiple issue  
**Translation:** 

**[783.88s] English:** uh and and doing a lot of the stuff in software because the second iteration the set-top box was  
**Translation:** Vocabulary: iteration: 迭代

**[790.18s] English:** really for avoiding the cost to the cable company of rolling the trucks out to replace your garbage  
**Translation:** 

**[795.96s] English:** general atlantic set-top box with a slightly newer less less uh garbagey one so if you could  
**Translation:** Vocabulary: garbagey: 陈旧的

**[801.60s] English:** have software upgradable um set-top boxes the cable companies uh thought they could save a lot  
**Translation:** 

**[805.84s] English:** of money and add features  
**Translation:** Vocabulary: upgradable: 可升级的

**[807.10s] English:** is this assembly or which level of this it was like we were writing in in um we were using gcc  
**Translation:** 

**[813.66s] English:** we're writing c++ and c uh somebody i i worked with their um really very smart guy hired from a  
**Translation:** 

**[820.46s] English:** sort of wall street um hotshot programming consultancy did his own hardware design as  
**Translation:** 

**[826.40s] English:** well as software and we were working on how to make uh not only short vector units but general  
**Translation:** Vocabulary: consultancy: 咨询公司; hotshot: 天才人物

**[831.20s] English:** bit shufflers and permuters so you could do things like um uh you know crypto algorithms  
**Translation:** 

**[837.10s] English:** and you could do uh demodulation of  
**Translation:** Vocabulary: crypto: 加密算法; demodulation: 解调; permuters: 排列; shufflers: 洗牌

**[840.00s] English:** the cable you know complex uh quadrature amplitude modulated signal so you're basically taking a to  
**Translation:** 

**[847.20s] English:** d converters dumping things in buffers and then doing the rest in software all the framing and  
**Translation:** Vocabulary: amplitude: 幅度

**[851.84s] English:** the reed solomon and viterbi and all that error correction so that was really great learning  
**Translation:** 

**[855.48s] English:** experience but it was not going to work it was doing too many risky things at once right if you  
**Translation:** 

**[858.94s] English:** as jim clark said to me when i hopped to netscape after three years at micro unity he said oh yeah  
**Translation:** 

**[863.74s] English:** you do 10 things each one in 10 odds it's going to be one in 10 billion right  
**Translation:** Vocabulary: netscape: 网景公司

**[868.00s] English:** um the multiplication principle so you know netscape was already a rocket and i passed the  
**Translation:** 

**[874.16s] English:** chance to go there in 1994 i knew the founders because i worked at sgi clark's company could  
**Translation:** Vocabulary: founders: 创立者; multiplication: 乘法

**[880.12s] English:** you pause for a second in netscape uh when was the launch of this rocket what uh 94 um 94 was  
**Translation:** 

**[886.32s] English:** the launch of netscape and i went there in early 95 in april okay but oh so you said you missed  
**Translation:** 

**[891.52s] English:** the launch well i missed the the the first floor employment opportunity but the ipo was was august  
**Translation:** 

**[897.42s] English:** 1995  
**Translation:** 

**[898.00s] English:** so i was there for that how obvious was it the netscape was like world changing uh what was the  
**Translation:** 

**[902.72s] English:** layout was netscape one of the first big browsers yes so when i was at micro unity still in 93 we  
**Translation:** Vocabulary: browsers: 浏览器; layout: 布局

**[909.36s] English:** saw a browser called mosaic and up till then we'd used email and we'd used usenet the nntp protocol  
**Translation:** 

**[915.68s] English:** we'd use news readers we used ftp we used all these old internet protocols all relying on the  
**Translation:** Vocabulary: usenet: 新闻组

**[921.56s] English:** dns and tcp ip and udp for that matter um when i was at silicon graphics we brought up the whole  
**Translation:** 

**[927.46s] English:** stack right so i was there for that so i was there for that so i was there for that so i was there for  
**Translation:** 

**[928.00s] English:** it we had to you know discover how how to find the ethernet addresses on your network and then  
**Translation:** 

**[932.62s] English:** find ip addresses for them our protocol all that stuff and it was great because nobody knew in the  
**Translation:** Vocabulary: ethernet: 以太网

**[938.20s] English:** 80s what was going to win all the proprietary stacks like ibm sna and deck net and all these  
**Translation:** 

**[944.14s] English:** other protocols were saying it's we're going to do it or it's going to be heterogeneous future and  
**Translation:** Vocabulary: heterogeneous: 异构的; proprietary: 专有的

**[948.22s] English:** instead it was you know berkeley unix and the tcp ip stack that dated back to the arpanet that won  
**Translation:** 

**[954.56s] English:** and i think we knew it we all knew it at sj but the sales were not so good and we didn't know it was going to win  
**Translation:** Vocabulary: arpanet: 阿帕网; berkeley: 伯克利

**[958.00s] English:** else people didn't. And so they kept  
**Translation:** 

**[960.00s] English:** trying to get multiple network stacks interoperating but in the end uh it won and so that was the  
**Translation:** Vocabulary: interoperating: 相互兼容

**[965.98s] English:** internet and it was email and texty and it was used very texty and then uh tim berners-lee did  
**Translation:** 

**[972.24s] English:** his thing but i don't think i was paying attention and i think the date when he first did it or when  
**Translation:** 

**[976.64s] English:** he wrote the famous email has been pushed back to 89 but i noticed a mosaic in 93 because one of the  
**Translation:** 

**[982.88s] English:** things that mark andreason and eric bina did at ncsa was they innovated on on the html early html  
**Translation:** Vocabulary: innovated: 创新; mosaic: 马赛克

**[990.86s] English:** standard they in particular mark sent this email saying hey everybody we think you should be able  
**Translation:** 

**[994.32s] English:** to put an image in a page and you know when he sent that eric bina had already written the code  
**Translation:** 

**[998.96s] English:** and you know i talked to tim berners-lee more recently just a few years ago and he was like  
**Translation:** 

**[1003.04s] English:** oh we had another way of doing it and then yeah it didn't work out because mark shipped his  
**Translation:** 

**[1006.94s] English:** in mosaic and this convinced me of several things one the internet meant there was a  
**Translation:** 

**[1012.80s] English:** huge amount of traffic and a huge amount of traffic and a huge amount of traffic and a  
**Translation:** 

**[1012.86s] English:** huge first mover advantage and being fast getting on first mattered a lot and so you know richard  
**Translation:** 

**[1018.92s] English:** gabriel of scheme and poetry fame has written about this the famous poetry what's poetry uh  
**Translation:** Vocabulary: gabriel: 加布里埃尔

**[1024.64s] English:** well he's a poet uh actual poetry no no i mean he's the founder of lucid which is where jamie  
**Translation:** 

**[1030.82s] English:** zawinski worked before netscape and lucid was doing you know compilers and lucid emacs which  
**Translation:** 

**[1036.42s] English:** was a fork of emacs famously jamie fighting against richard stallman stalmax um and so  
**Translation:** 

**[1042.78s] English:** richard gabriel you know very very brainy computer guy but also a poet but he wrote a nice essay that  
**Translation:** Vocabulary: brainy: 聪明; emacs: 编辑器; stallman: 斯托尔曼

**[1047.52s] English:** gets abused all the time in fact jamie's put a kind of warning in front of his version of it on  
**Translation:** 

**[1051.64s] English:** his site jwc.org called worse is better and this is about survival advantage of software in the  
**Translation:** 

**[1058.62s] English:** network world in my opinion it's about unix it started out being framed as unix and lisp good  
**Translation:** 

**[1063.82s] English:** news bad news because all the list people the mit people were like oh you know this is the crown  
**Translation:** 

**[1068.68s] English:** jewel right uh scheme this is fabergé egg or common list this is the crown jewel scheme this is the  
**Translation:** 

**[1072.76s] English:** giant cathedral of course we're going to win this is civilization and those you know those  
**Translation:** Vocabulary: cathedral: 大教堂

**[1076.74s] English:** farmers in new jersey to borrow from the sopranos this  
**Translation:** 

**[1080.00s] English:** down at bell labs they're just you know there's nothing sound there it's all hacking yeah um well  
**Translation:** Vocabulary: hacking: 非法入侵; sopranos: 黑帮剧

**[1085.34s] English:** guess what one wow so you're saying this is a fundamental like principle of the internet is  
**Translation:** 

**[1093.04s] English:** moving fast winds you could say in in almost any network system like in biological evolution you  
**Translation:** 

**[1098.30s] English:** see successful allele sweet populations and they don't always have um you know they aren't free of  
**Translation:** 

**[1103.96s] English:** flaws that heterozygous advantage right you can get both parents uh give you the the gene variant  
**Translation:** Vocabulary: allele: 等位基因; heterozygous: 杂合的

**[1110.02s] English:** and you get sickle cell anemia right but but if one of them does you're more resistant to malaria  
**Translation:** 

**[1114.30s] English:** and so this isn't um a beautiful process except at large scale and then you realize that because  
**Translation:** Vocabulary: anemia: 贫血; resistant: 有抵抗力; sickle: 镰刀状的

**[1120.64s] English:** it moves fast and can adapt it it can win and people still struggle with this i i used to  
**Translation:** 

**[1127.26s] English:** struggle with this because javascript was done in such a hurry and the force of web compatibility  
**Translation:** Vocabulary: compatibility: 兼容性

**[1131.82s] English:** meant early mistakes couldn't be  
**Translation:** 

**[1133.96s] English:** fixed and even the standards process injected new mistakes as it will  
**Translation:** 

**[1138.20s] English:** uh but often standards bodies go back and making compatible changes you can't do that with the web  
**Translation:** 

**[1142.98s] English:** it's more like again like biology you you preserve what still works you don't want to break  
**Translation:** Vocabulary: compatible: 兼容的

**[1147.92s] English:** atp metabolism or whatever so um you have to kind of resign yourself to  
**Translation:** 

**[1153.22s] English:** the reality of um worse is better being enshrined in actual design points you might not like  
**Translation:** Vocabulary: enshrined: 确立; metabolism: 代谢

**[1163.04s] English:** and that happened with  
**Translation:** 

**[1163.94s] English:** javascript and i'm way over it but uh it also i think was a huge advantage why javascript has  
**Translation:** 

**[1169.66s] English:** kind of swept a lot of programming domains um people will say oh it's not because of merit well  
**Translation:** 

**[1175.00s] English:** you're right but we also improved it over time in the standards body i spent 20 years doing that  
**Translation:** 

**[1178.80s] English:** and uh you don't get that choice it's like i'm not saying that that was the best language i'm  
**Translation:** 

**[1185.46s] English:** just saying that was the right time to do it and i like to say the alternative was not to do it i  
**Translation:** 

**[1190.32s] English:** could have told netscape i can't do this it's too rushed and it would have been better to do it in  
**Translation:** 

**[1193.94s] English:** visual basic script it would have been bad uh so that's a good way to present the alternative but  
**Translation:** Vocabulary: netscape: 网景浏览器

**[1200.00s] English:** So it was a Netscape, and you have written it in how many days, and why was it only that many days, and what was the goal and the underlying principles in your mind at the time?  
**Translation:** 

**[1209.58s] English:** So the whole – I'm sort of describing worse is better in a frenetic way because it fit the model of Netscape.  
**Translation:** Vocabulary: frenetic: 狂热的

**[1214.82s] English:** When it was known that Jim Clark and Marc Andreessen were founding Netscape, and they did the first release in 1994, that browser took over from Mosaic.  
**Translation:** 

**[1224.82s] English:** In fact, that's why Mozilla is called that.  
**Translation:** Vocabulary: andreessen: 马科斯; founding: 创办; mosaic: 摩zilla

**[1227.14s] English:** It's the Mosaic killer.  
**Translation:** 

**[1228.30s] English:** It's like the giant monster that kills Mosaic.  
**Translation:** 

**[1230.10s] English:** That's awesome.  
**Translation:** 

**[1230.64s] English:** And they knew that – it wasn't that – again, it's not like you're doing advanced scientific research that is changing the world.  
**Translation:** 

**[1237.28s] English:** You're more like taking down the last iteration on the browser Marc did, which had images and other importances before he stopped working on it.  
**Translation:** 

**[1245.88s] English:** And you're making Netscape the new thing that has images, plug-ins, which was the way to do video back in the day.  
**Translation:** Vocabulary: importances: 重要元素; iteration: 版本

**[1251.64s] English:** It had something that's kind of died now for tiled windows called frames and framesets.  
**Translation:** 

**[1256.82s] English:** Oh, yeah, yeah, yeah, yeah.  
**Translation:** Vocabulary: framesets: 框架集

**[1257.84s] English:** It had HTML tables.  
**Translation:** 

**[1258.80s] English:** That was new.  
**Translation:** 

**[1259.26s] English:** Eric Bina did that.  
**Translation:** 

**[1260.00s] English:** He did tables in Netscape 1.1.  
**Translation:** 

**[1261.58s] English:** So when I got there, they were heading toward IPO.  
**Translation:** 

**[1265.02s] English:** Clark wanted to IPO early.  
**Translation:** 

**[1266.46s] English:** I think his instinct was right.  
**Translation:** 

**[1267.62s] English:** And that kicked off the whole dot-com era, right?  
**Translation:** Vocabulary: instinct: 直觉

**[1270.18s] English:** There was a recession in the U.S. in 91.  
**Translation:** 

**[1272.96s] English:** You can see old Law & Order reruns where they talk about the recession and how hard it's hitting New Yorkers.  
**Translation:** Vocabulary: recession: 经济衰退

**[1278.06s] English:** And after that, Greenspan really goosed things at the Federal Reserve, and technology had been sort of fermenting in a way that came together with the Internet.  
**Translation:** 

**[1286.26s] English:** And Netscape made it possible to do pets.com.  
**Translation:** Vocabulary: fermenting: 酝酿; goosed: 刺激

**[1290.00s] English:** You have to do eBay to get people to recognize a URL on a billboard and then type it in when they get home.  
**Translation:** 

**[1296.04s] English:** And that was huge.  
**Translation:** Vocabulary: billboard: 户外广告牌

**[1297.46s] English:** That was so fast-moving a rocket that Mark and the engineering team there thought, we need to make this a programmable browser, not just a document viewer, not just a video.  
**Translation:** 

**[1310.70s] English:** It was all HTML with images and tables and also, like you said, frames.  
**Translation:** 

**[1315.32s] English:** Early plug-ins.  
**Translation:** 

**[1316.02s] English:** There's no dynamic element at all.  
**Translation:** 

**[1317.86s] English:** Yeah.  
**Translation:** 

**[1318.00s] English:** The most dynamism you get was from a plug-in.  
**Translation:** Vocabulary: dynamism: 动力

**[1320.00s] English:** there are a few of them then flash didn't exist at that point uh it was i think um  
**Translation:** 

**[1325.20s] English:** java applets yet or no well that's the thing we did the deal with sun in fact i was recruited to  
**Translation:** Vocabulary: recruited: 被招募

**[1331.08s] English:** go do scheme in the browser remember guys stealing gerald sussman's beautiful list variant i was  
**Translation:** 

**[1336.94s] English:** going to do it in the browser because my friends from sgi thought hey we like scheme you like  
**Translation:** Vocabulary: gerald: 杰拉德

**[1340.56s] English:** scheme and i'm like i hardly ever use scheme it's not really used in industry except in sort of  
**Translation:** 

**[1344.30s] English:** silos um but i like it okay i'll come do scheme in the browser i have a slide from my 2017 uh talk  
**Translation:** Vocabulary: silos: 信息孤岛

**[1352.62s] English:** where i have bruce willis crawling through the duct and die hard come out to the coast have a  
**Translation:** 

**[1357.46s] English:** lot of fun come on do scheme in the browser um but when i got there there was no scheme in the  
**Translation:** Vocabulary: crawling: 爬行; willis: 威尔士

**[1361.88s] English:** browser because they'd started a deal with sun microsystems and my best contact there was bill  
**Translation:** 

**[1366.62s] English:** joy who i admired as a berkeley unix founder and you know sun founder uh and bill got the idea of  
**Translation:** Vocabulary: berkeley: 伯克利

**[1372.42s] English:** making the browser programmable too and so the  
**Translation:** 

**[1374.30s] English:** idea main idea was to put the java vm which at that point was not really easy to embed into  
**Translation:** Vocabulary: embed: 嵌入

**[1380.80s] English:** netscape including the netscape version on windows that was still most popular which was the 16-bit  
**Translation:** 

**[1386.82s] English:** windows 3-1 which was going away microsoft was coming out with windows 95 and everyone was  
**Translation:** Vocabulary: netscape: 网景浏览器

**[1392.18s] English:** afraid they were going to do you know internet explorer i guess two at that point three the next  
**Translation:** 

**[1396.74s] English:** year they already bought uh or invested in somehow spyglass this other company that shot out from  
**Translation:** Vocabulary: explorer: 浏览器; spyglass: 望远镜

**[1403.14s] English:** ncsa  
**Translation:** 

**[1404.30s] English:** at university of illinois um and in fact microsoft had tried to buy netscape in late 94 before i got  
**Translation:** 

**[1410.84s] English:** there and i heard about this later i heard they offered way too little money and so you know  
**Translation:** 

**[1415.98s] English:** jim barksdale and jim clark said get out of here pound sand but then they realized oh this is going  
**Translation:** Vocabulary: barksdale: 巴克赛尔

**[1423.00s] English:** to hurt us because now they're going to copy us didn't happen right away i'm not sure when gates  
**Translation:** 

**[1427.20s] English:** internet tidal wave memo was written that's the famous memo he wrote when bill gates realized that  
**Translation:** Vocabulary: tidal: 潮汐的

**[1434.30s] English:** there would be no data on this old copy aol path or copy compu serve path a project called blackbird  
**Translation:** 

**[1440.00s] English:** presumably after the sr71 i don't know but they were going to make a you know dial-up service  
**Translation:** Vocabulary: presumably: 推测

**[1445.28s] English:** with a custom content language stack and custom rendering it wasn't the web um you know they could  
**Translation:** 

**[1451.28s] English:** have content partners uh they have a lot of money but it still wasn't to scale the web it wasn't  
**Translation:** 

**[1456.18s] English:** going to be compelling and gates realized this and he turned the company on a dime and they  
**Translation:** 

**[1460.36s] English:** couldn't buy netscape again i'm not sure the timing so they decided to copy it and  
**Translation:** Vocabulary: compelling: 有说服力的

**[1464.80s] English:** once we realized that everybody inside netscape felt even more urgency and more of a frenetic mood  
**Translation:** 

**[1470.28s] English:** and so my chance to do scheme disappeared when the java deal started brewing but there was still a  
**Translation:** Vocabulary: brewing: 酝酿; frenetic: 狂热的; urgency: 紧迫感

**[1476.58s] English:** chance to do a companion language to java because java was a compiled is a compiled language it's  
**Translation:** 

**[1482.82s] English:** evolved and improved quite a lot since then too but it was for sort of serious advanced programmers  
**Translation:** Vocabulary: compiled: 编译语言; programmers: 程序员

**[1488.44s] English:** that cost a certain salary or hourly rate and people observed bill joy observed and i  
**Translation:** 

**[1494.30s] English:** mark  
**Translation:** 

**[1494.78s] English:** andreason and i observed that in a mature stack like microsoft you really benefit from having a  
**Translation:** 

**[1499.20s] English:** scripting language like visual basic which became visual basic script in ie3 but didn't take on  
**Translation:** 

**[1504.74s] English:** didn't take over and kill javascript that you need two languages one is for the component writers who  
**Translation:** 

**[1510.24s] English:** are higher price and more expert and the other is for uh scripters certified public accountants  
**Translation:** Vocabulary: accountants: 会计师; scripters: 脚本编写者

**[1518.32s] English:** designers graphic designers with some programming inclination anybody amateurs doesn't matter there's  
**Translation:** 

**[1523.66s] English:** uh  
**Translation:** Vocabulary: amateurs: 爱好者; designers: 设计师; inclination: 倾向

**[1524.28s] English:** much more demotic uh approach there for programming the components together gluing them together  
**Translation:** 

**[1529.44s] English:** some people say duct tape language which i don't really like but we saw bill joy and mark andreason  
**Translation:** Vocabulary: demotic: 通俗; gluing: 粘合

**[1535.84s] English:** and i we saw the need for companion language and the gleeman or i was to call it javascript i didn't  
**Translation:** 

**[1540.66s] English:** like it that was marketing's plan mark called it mocha which i liked and netscape marketing i think  
**Translation:** Vocabulary: mocha: 摩卡; netscape: 网景

**[1546.50s] English:** didn't like that so they said oh there's some trademark in some software somewhere that uses  
**Translation:** 

**[1550.46s] English:** mocha so we can't use that and they tried live script in august and they said oh there's some  
**Translation:** Vocabulary: trademark: 注册商标

**[1554.28s] English:** that didn't last and then finally we got the trademark license in december 1995 but the work i  
**Translation:** 

**[1559.34s] English:** did  
**Translation:** 

**[1560.00s] English:** To prove that it could be done was important because I came in in April and even then Netscape was growing so fast that they couldn't find an open hiring requisition in the client team for me.  
**Translation:** 

**[1572.34s] English:** So they hired me into the server team and I worked for a month on server team on what became HTTP 1.1.  
**Translation:** Vocabulary: requisition: 采购申请

**[1578.52s] English:** So I was actually I had done protocol work at Silicon Graphics with Greg Chesson, former Bell Labs intern, grad student intern who knew all the Unix founders.  
**Translation:** 

**[1586.90s] English:** And Greg was very interested in taking protocols to the next level with VLSI because he thought that CPUs wouldn't wouldn't scale up.  
**Translation:** Vocabulary: founders: 创立者; intern: 实习生

**[1595.56s] English:** He was mistaken in that. Unfortunately, Moore's law more than kept up.  
**Translation:** 

**[1599.12s] English:** And you have, you know, gigabit Ethernet running with conventional processors.  
**Translation:** Vocabulary: ethernet: 以太网; gigabit: 千兆; processors: 处理器

**[1602.36s] English:** But I worked on protocols at SGI as well as Unix kernel hacking and NFS and things like that.  
**Translation:** 

**[1609.00s] English:** So I I came into Netscape to work on the server side for a month.  
**Translation:** Vocabulary: hacking: 编程; kernel: 内核

**[1613.44s] English:** But I was I was thinking the whole time, what should this language be like?  
**Translation:** 

**[1616.34s] English:** Should it be?  
**Translation:** 

**[1616.90s] English:** Should it be easy to use?  
**Translation:** 

**[1618.54s] English:** Might it syntax even be more like natural language, like Hyper Talk, which is Bill Atkinson's language in HyperCard?  
**Translation:** Vocabulary: hyper: 超媒体; syntax: 语法规则

**[1625.88s] English:** If you have ever used HyperCard on an early Mac.  
**Translation:** 

**[1628.84s] English:** And I thought, well, I'd like to do that.  
**Translation:** 

**[1632.08s] English:** But my management is saying, make it look like Java, which looks like C from a distance.  
**Translation:** 

**[1637.56s] English:** What does that mean?  
**Translation:** 

**[1638.50s] English:** Is it braces?  
**Translation:** 

**[1639.28s] English:** We're talking about visually.  
**Translation:** Vocabulary: braces: 牙套

**[1640.50s] English:** Yeah.  
**Translation:** 

**[1640.78s] English:** I mean, like what management do they understand what they don't?  
**Translation:** 

**[1644.58s] English:** Marketing didn't know, but management did.  
**Translation:** 

**[1646.50s] English:** Like Rick Shell, the VP of engineering, knew.  
**Translation:** 

**[1649.66s] English:** And we had a plan even that was if you have this companion language, you're going to glue things together between Java and JavaScript.  
**Translation:** 

**[1655.68s] English:** So you're going to have commerce in memory in the heap with data types.  
**Translation:** 

**[1660.20s] English:** So you're going to want some of the data types in Java to reflect in JavaScript.  
**Translation:** 

**[1663.86s] English:** You're going to want the primitive types that Java unfortunately separated from objects.  
**Translation:** 

**[1667.40s] English:** So at least some of them number double, let's call it in Java's terms from the C term for double precision floating point or string.  
**Translation:** 

**[1676.50s] English:** Or Booleans.  
**Translation:** Vocabulary: booleans: 布尔类型

**[1677.86s] English:** And.  
**Translation:** 

**[1679.66s] English:** And.  
**Translation:** 

**[1680.00s] English:** um objects and so right away there was this constraint looking like java meant kind of the  
**Translation:** 

**[1686.70s] English:** c curly brace syntax but also some of the data types and objects like objects and so on all  
**Translation:** Vocabulary: brace: 花括号; constraint: 限制

**[1690.94s] English:** that kind of stuff thought it called comparison operator garbage collection all that stuff yeah  
**Translation:** 

**[1694.62s] English:** uh even the bitwise operators and the shift operators including the unsigned right shift  
**Translation:** Vocabulary: bitwise: 位运算

**[1699.50s] English:** which java had because it didn't have unsigned integer types it said if you want to do unsigned  
**Translation:** 

**[1704.08s] English:** operations use an operator and that turned out to be important much later i'll tell that story  
**Translation:** Vocabulary: integer: 整数

**[1708.08s] English:** five time but um javascript inherited a set of uh operators the expression grammar the statement  
**Translation:** 

**[1716.68s] English:** grammar up to a point from java but i wanted a functional language i wanted scheme a little bit  
**Translation:** Vocabulary: inherited: 继承

**[1722.34s] English:** of scheme even though it wasn't as clean as scheme i wanted you had a love sorry to drop you had a  
**Translation:** 

**[1726.46s] English:** love for scheme and lisp that that that functional language yes i wanted first class functions  
**Translation:** 

**[1731.36s] English:** because i i saw the need for callbacks in the browser where it's a single threaded program  
**Translation:** 

**[1735.64s] English:** all the early browsers were single threaded and it's the right  
**Translation:** Vocabulary: browsers: 浏览器; callbacks: 回调函数; threaded: 线程化的

**[1737.90s] English:** model  
**Translation:** 

**[1738.06s] English:** for users most users weren't ready for mutual exclusion and threading so in a single threaded  
**Translation:** Vocabulary: exclusion: 互斥; threading: 线程

**[1743.34s] English:** world you you cannot block the user interface so you have to use a callback and run later and  
**Translation:** 

**[1747.76s] English:** the without getting too fancy and trying to capture the continuation like call cc does in  
**Translation:** Vocabulary: callback: 回调; cannot: 不能; continuation: 续传; interface: 接口

**[1752.94s] English:** scheme i thought i'll just make it easy to have fun arcs first class functions you pass you know  
**Translation:** 

**[1758.18s] English:** downward and it can call back it'd be called back um and java didn't have that at the time  
**Translation:** 

**[1763.44s] English:** it had it took forever to get proper first class functions uh lamb does now  
**Translation:** 

**[1768.06s] English:** into into java java seven or eight i think it did have concurrency right from the from the very  
**Translation:** Vocabulary: concurrency: 并行性

**[1773.04s] English:** beginning but you're you were thinking that the javascript in the browser would not have the  
**Translation:** 

**[1777.70s] English:** luxury of being concurrent that's right and the reason was java was going to run in the plugins  
**Translation:** Vocabulary: concurrent: 并发

**[1782.38s] English:** we could fork threads and go go to town but the main action in the browser was in the single  
**Translation:** 

**[1787.42s] English:** threaded program the single unix process on on unix or windows uh and it was where you had to  
**Translation:** 

**[1793.48s] English:** service the event loop and then go you know do things respond to the network lay out some html's  
**Translation:** 

**[1798.06s] English:** render it turn you know  
**Translation:** Vocabulary: render: 渲染

**[1800.00s] English:** widths into heights by filling containers boxes uh the early what became the css box model uh and  
**Translation:** 

**[1806.28s] English:** run scripts to you know make the thing livelier respond to user input uh and all that event  
**Translation:** 

**[1812.34s] English:** driven programming was in part like hypercard because hypercard had this on event name syntax  
**Translation:** 

**[1819.00s] English:** and so that's why you have in javascript on click run together as the name of the event handler  
**Translation:** Vocabulary: hypercard: 超媒体; syntax: 语法规则

**[1823.50s] English:** and there's some funny ones on mouse over and on mouse out people still complain about those but  
**Translation:** 

**[1828.28s] English:** you know um there are many more events now over the years standardized but it was a mix of event  
**Translation:** Vocabulary: standardized: 标准化的

**[1833.64s] English:** driven single threaded programming because it had to run in the main thread of the browser where the  
**Translation:** 

**[1838.38s] English:** action is and java never got there which meant java could not interact easily or quickly or  
**Translation:** 

**[1843.84s] English:** in a nested way with the document with the objects reflected from the html document with  
**Translation:** 

**[1849.24s] English:** the tables and forms and so on and that that is one of the reasons i think javascript survived  
**Translation:** 

**[1854.38s] English:** and java kind of died java was in this plug-in prison it essentially was confined to a  
**Translation:** 

**[1858.26s] English:** rectangle the applet rectangle and while we we even built a next year uh nick thompson a friend  
**Translation:** Vocabulary: confined: 限制; rectangle: 矩形

**[1864.02s] English:** from sgi who was an intern grad student at cmu at the time built the first version of live connect  
**Translation:** 

**[1870.12s] English:** to glue java and javascript together to deliver on that vision where you do have commerce between the  
**Translation:** Vocabulary: intern: 实习生

**[1875.14s] English:** the data types in the heap um did it work it worked but you were java was in charge javascript  
**Translation:** 

**[1881.58s] English:** was in charge and java was just these components these helper you might as well do everything in  
**Translation:** 

**[1885.30s] English:** javascript what happened over time it's like an evolutionary filter it just  
**Translation:** 

**[1888.26s] English:** kind of who needs the plug-in and in fact sun mismanaged java as a plug-in they they thought  
**Translation:** Vocabulary: evolutionary: 进化; mismanaged: 管理不善

**[1893.62s] English:** oh netscape is giving us the distribution vehicle and we don't care about the browser it's just  
**Translation:** 

**[1898.62s] English:** about getting java out there and that was a big miscalculation they then tried because microsoft's  
**Translation:** Vocabulary: miscalculation: 判断失误; netscape: 网景浏览器

**[1903.08s] English:** killing netscape after years they tried getting into microsoft and you may remember there was a  
**Translation:** 

**[1907.00s] English:** sun microsoft deal which famously blew up and and microsoft kicked java out of windows and that's  
**Translation:** 

**[1915.16s] English:** when they really pulled the trigger i think they already evaluated it and liked it  
**Translation:** 

**[1918.26s] English:** and i think that's a really good point and i think that's a really good point i think that's a really good point  
**Translation:** Vocabulary: evaluated: 评估过后

**[1920.00s] English:** and, you know, C sharp and decided we're going to just not have Java.  
**Translation:** 

**[1924.14s] English:** We don't want, you know, any of that sun stuff.  
**Translation:** 

**[1926.48s] English:** We don't want the patent risk.  
**Translation:** 

**[1927.56s] English:** We don't want, I'm not sure what the fights were about.  
**Translation:** Vocabulary: patent: 专利

**[1930.08s] English:** There was some patent angle to it, I think.  
**Translation:** 

**[1932.34s] English:** And up till then, Microsoft had been using Java components like in Outlook web access,  
**Translation:** 

**[1939.18s] English:** which had a lot of JavaScript to be a web mail, like hotmail, like user interface.  
**Translation:** 

**[1942.98s] English:** They had to call the mail server through HTTP, and they used a Java object to do this.  
**Translation:** Vocabulary: interface: 用户界面

**[1951.40s] English:** And when they gave the boot to Sun, they suddenly other, you know, the left hand gave the boot  
**Translation:** 

**[1957.08s] English:** and the right hand said, we better do something else in Outlook web access.  
**Translation:** 

**[1960.08s] English:** What are we going to do?  
**Translation:** 

**[1960.94s] English:** And they said, let's just add an ActiveX component, which is their own native way of embedding  
**Translation:** Vocabulary: embedding: 嵌入

**[1965.98s] English:** things in languages.  
**Translation:** 

**[1966.74s] English:** And we'll make it, it'll be what became XML HTTP request, which is now a web stand.  
**Translation:** 

**[1972.98s] English:** For calling asynchronously, and it's been replaced by the fetch API in HTML5 or HTML  
**Translation:** 

**[1978.74s] English:** living document.  
**Translation:** Vocabulary: asynchronously: 异步地

**[1979.48s] English:** But this whole lineage goes back to Java being successfully the loser and getting kicked  
**Translation:** 

**[1984.30s] English:** out.  
**Translation:** Vocabulary: lineage: 血统

**[1984.80s] English:** And after Microsoft kicked it out, it was a plugin and you would find it required for  
**Translation:** 

**[1989.26s] English:** like smart card banking in Nordic countries where that was mandated by law, but really  
**Translation:** Vocabulary: mandated: 法律规定; nordic: 北欧国家

**[1995.02s] English:** didn't get used much.  
**Translation:** 

**[1996.16s] English:** Or, you know, there were pilots who used it for flight information, but Flash, which  
**Translation:** 

**[2002.98s] English:** Netscape could have bought, but fortunately didn't.  
**Translation:** 

**[2005.72s] English:** Fortunately didn't.  
**Translation:** 

**[2006.54s] English:** Yeah, we would have screwed it up.  
**Translation:** 

**[2007.86s] English:** I mean.  
**Translation:** 

**[2008.04s] English:** What year are we talking about with Flash?  
**Translation:** 

**[2009.48s] English:** I think after the IPO.  
**Translation:** 

**[2010.70s] English:** So it was probably late 95 and.  
**Translation:** 

**[2012.44s] English:** Oh, Flash was around.  
**Translation:** 

**[2013.32s] English:** Was it Adobe?  
**Translation:** 

**[2014.16s] English:** No, it wasn't.  
**Translation:** 

**[2014.60s] English:** No, it was, it was called Future Splash.  
**Translation:** 

**[2016.40s] English:** And it was these brothers, Jonathan Gay, I think his name was.  
**Translation:** 

**[2019.38s] English:** And he, he came knocking and the marketing guy at Netscape who was screening the technology  
**Translation:** 

**[2025.28s] English:** partners or wannabe acquisitions was brutal.  
**Translation:** Vocabulary: acquisitions: 收购; brutal: 严厉

**[2027.86s] English:** And just everybody wanted to get in on the Netscape, you know, stock gravy train.  
**Translation:** 

**[2031.16s] English:** And he sent them packing.  
**Translation:** Vocabulary: netscape: 网景公司

**[2032.24s] English:** And they, they ended up selling the Macromedia and Macromedia was where Flash was created.  
**Translation:** 

**[2037.26s] English:** And the good thing about Macromedia was it was a.  
**Translation:** Vocabulary: macromedia: 宏媒体

**[2040.00s] English:** um tool company so it invested in you know the best ideas i think which are still somewhat lost  
**Translation:** 

**[2047.02s] English:** to us of flash the timeline animation has sort of been a mutable function uh over time they had  
**Translation:** 

**[2053.94s] English:** the tooling around that too like that dream weaver there's a flash flash director there were a bunch  
**Translation:** 

**[2058.50s] English:** of them yeah i mean yeah they that was a flash builder was one of the last ones these tools were  
**Translation:** Vocabulary: weaver: 织工

**[2063.56s] English:** used by real artists and you know special effects people and designers all the restaurant websites  
**Translation:** 

**[2068.50s] English:** around 2005 were done in flash which was you know we were trying to do hml5 at the same time  
**Translation:** Vocabulary: designers: 设计师

**[2073.90s] English:** that was the firefox era we were trying to make the web capable enough you didn't need flash but  
**Translation:** 

**[2078.60s] English:** if you recall you go to a restaurant it's like this is kind of like a game or something it's  
**Translation:** 

**[2082.44s] English:** like a flash all the font looks small and you didn't like flash from the beginning you're like  
**Translation:** 

**[2086.10s] English:** this is this doesn't feel right not really i actually admire flash's technology and i'm pretty  
**Translation:** 

**[2090.64s] English:** pragmatic about these things and i i realized that you know it doesn't matter if you're dealt a bad  
**Translation:** 

**[2096.14s] English:** hand like javascript was a rush job  
**Translation:** Vocabulary: pragmatic: 实际可行

**[2098.50s] English:** if you have flash as a plugin and you can invest in the tools and make it pretty good uh you should  
**Translation:** 

**[2103.96s] English:** you should make it better for your users and grow it as best you can and what happened with the  
**Translation:** 

**[2108.10s] English:** browser due to microsoft's monopoly abuse for which they were convicted and you know um even  
**Translation:** 

**[2114.42s] English:** after that until i think firefox and then chrome was people kept saying oh the web can't do x can't  
**Translation:** Vocabulary: convicted: 判罪; monopoly: 垄断

**[2120.20s] English:** do y we'll have to have a plugin we'll have to have a new approach well we'll clean the slate  
**Translation:** 

**[2125.36s] English:** and have a new web and everyone who said that  
**Translation:** Vocabulary: slate: 重新开始

**[2128.50s] English:** failed and the reason they failed is because there's too much value in the web this huge  
**Translation:** 

**[2133.24s] English:** network and the worse is better principle means that you can not only start bad which they all  
**Translation:** 

**[2138.28s] English:** sneer at but get on first and get wide distribution get sort of evolutionary advantage in priority of  
**Translation:** 

**[2146.24s] English:** place but you can also improve it over time yes and so if you're going to improve flash and for  
**Translation:** Vocabulary: evolutionary: 进化

**[2151.54s] English:** some reason flash is now out of favor steve job said you can't have flash on the iphone that was  
**Translation:** 

**[2155.18s] English:** probably the death now put your energy into javascript and that  
**Translation:** 

**[2158.50s] English:** happened right so we we did things  
**Translation:** 

**[2160.00s] English:** mozilla with adobe to improve which bought my macro media to improve flash and to improve the  
**Translation:** Vocabulary: macro: 宏命令

**[2165.50s] English:** version of javascript that was in flash we tried to standardize that oh that's right i'm getting  
**Translation:** 

**[2169.72s] English:** ahead of myself that was es4 yeah that's that's right can we just rewind to the magical like  
**Translation:** Vocabulary: standardize: 制定标准

**[2175.36s] English:** you know it's a special moment in the history of all of computing it's uh we'll talk about it later  
**Translation:** 

**[2181.12s] English:** but it's arguable it's possible that the entirety of the world will run on javascript at some point  
**Translation:** Vocabulary: arguable: 可争议的; computing: 计算; entirety: 全部

**[2186.82s] English:** so like it's like those are those days it would be it would be interesting if you could just  
**Translation:** 

**[2191.78s] English:** describe actually zooming in on the how the cake was baked uh from the you know the the several  
**Translation:** 

**[2200.02s] English:** days that you were working on it what was on your mind uh how much coffee were you drinking  
**Translation:** 

**[2204.72s] English:** were you nervous why you're freaking out i'll try to remember it i mean you're right there  
**Translation:** Vocabulary: freaking: 焦虑

**[2209.28s] English:** are these pregnant moments you see in hindsight maybe they're overrated but like hegel sees  
**Translation:** 

**[2213.54s] English:** napoleon on horseback right at jena and says there's the world  
**Translation:** Vocabulary: hegel: 黑格尔; hindsight: 事后; horseback: 马背; napoleon: 拿破仑

**[2216.80s] English:** spirit uh on horse um and uh i knew that there was a chance to do it mark knew and he was my  
**Translation:** 

**[2225.72s] English:** you know executive sponsor and he was the one you know sort of brainstorming how the  
**Translation:** 

**[2231.28s] English:** javascript should be right there in the page that was important for him to say that because i i  
**Translation:** 

**[2235.24s] English:** thought so too but a lot of people were like oh you can't write programming language in the middle  
**Translation:** 

**[2239.00s] English:** of the markup and indeed there are problems if you did it naively you'd see the code laid out  
**Translation:** 

**[2243.52s] English:** as like random gibberish so i had to figure out how to hide that that was  
**Translation:** Vocabulary: gibberish: 无意义的乱码; markup: 标记语言; naively: 天真地

**[2246.80s] English:** a challenge is that is that a breakthrough idea i mean so you mark thinking about this idea that  
**Translation:** 

**[2252.68s] English:** you just inject code in the middle of the mark of the web page yeah it was considered kind of  
**Translation:** 

**[2257.54s] English:** heretical there was an sgml guru i forget his name but he corresponded with me and at first he  
**Translation:** 

**[2261.50s] English:** was angry he's like you should have used a marked section why didn't you use a marked section and i  
**Translation:** Vocabulary: corresponded: 通信

**[2266.06s] English:** said well sgm marked sections are not part of html by the way and they're not supported in the browser  
**Translation:** 

**[2270.22s] English:** and so i did some hack that was equivalent and over time you could do the proper sgml thing  
**Translation:** 

**[2276.80s] English:** and it was again sort of of evolutionary necessity it was almost  
**Translation:** 

**[2280.00s] English:** like introgression like like you know the the idea um which uh limar ghoulish i think helped  
**Translation:** Vocabulary: evolutionary: 进化; introgression: 基因渗入; necessity: 必要性

**[2286.34s] English:** get across that uh we have to consider mutualism biology that maybe you know mitochondria were  
**Translation:** 

**[2292.36s] English:** ancient uh prokaryotes that got into the cell and became beneficial um somehow uh the same sort of  
**Translation:** Vocabulary: mitochondria: 线粒体; mutualism: 互利共生; prokaryotes: 原核生物

**[2299.84s] English:** thinking applies uh you have to embed javascript in html it's going to be a good virus it won't  
**Translation:** 

**[2304.94s] English:** the code the code becomes data in the sense it just gets carried carried along but is there is  
**Translation:** Vocabulary: embed: 嵌入

**[2310.92s] English:** there's the side of the so you were focusing on the netscape at that time doesn't the browser  
**Translation:** 

**[2315.74s] English:** have to support interpret correctly this a mix of html and whatever code i had to hide it from  
**Translation:** Vocabulary: interpret: 解释; netscape: 网景浏览器

**[2322.08s] English:** old browsers including netscape 1-1 which was predominant then so i used uh an html comment  
**Translation:** 

**[2327.06s] English:** but the inside the container that comment lived in the script tag which is a new element i could  
**Translation:** Vocabulary: browsers: 浏览器; predominant: 占主导地位

**[2332.20s] English:** make different semantics in netscape 2  
**Translation:** 

**[2334.22s] English:** where  
**Translation:** Vocabulary: semantics: 语义

**[2334.94s] English:** those html comment delimiters instead of being multi-line brackets became one line  
**Translation:** 

**[2339.40s] English:** or essentially one line so you wrote so javascript was written the programming language was written  
**Translation:** Vocabulary: brackets: 括号; delimiters: 分隔符

**[2343.80s] English:** as a comment a comment for old browsers and a set of brackets that were ignored with real code for  
**Translation:** 

**[2349.70s] English:** new and it was this two-way comment hiding hack as i called it that was absolutely necessary for  
**Translation:** 

**[2354.92s] English:** us to get off the ground we couldn't have bootstrapped javascript without it we didn't  
**Translation:** 

**[2357.98s] English:** have scripts that were loaded from a separate file the only scripts in netscape 2 were inline  
**Translation:** Vocabulary: bootstrapped: 自我提升; inline: 内联

**[2361.96s] English:** in the document what were the challenges here what what  
**Translation:** 

**[2364.70s] English:** like the the the the the the the the the the the the the the the the the the the the the the  
**Translation:** 

**[2364.92s] English:** the the the the the the the the the the the the the the the the the the the the the you  
**Translation:** 

**[2371.76s] English:** know typing  
**Translation:** 

**[2377.08s] English:** garbage collectors garbage collection i didn't have time to write a garbage collector so i just i  
**Translation:** 

**[2387.12s] English:** didn't at first so the thing was using essentially arenas or what gnu calls obj pools and just would  
**Translation:** Vocabulary: collector: 垃圾收集者; collectors: 垃圾收集者

**[2388.72s] English:** run out of memory eventually and i added reference counting in a hurry after the 10 days in which i  
**Translation:** 

**[2389.72s] English:** hacked so after i was in the server team doing httpasti and thinking about the language i finally  
**Translation:** Vocabulary: hacked: 临时编写

**[2389.78s] English:** got transferred to the client team in early may and that's when i you know i got the go sign from  
**Translation:** 

**[2392.76s] English:** website and i still save it so at this point i was like yeah i need my endthere or this like yeah  
**Translation:** Vocabulary: endthere: 结束在那里

**[2394.04s] English:** do you malbeau 你 stadium rome blood they say love every fucking time and if they use mem근 on speech  
**Translation:** 

**[2394.76s] English:** from mark and it was like we can't wait because people inside netscape are doubting even people  
**Translation:** Vocabulary: doubting: 怀疑

**[2400.00s] English:** inside Sun are definitely doubting.  
**Translation:** 

**[2401.90s] English:** Bill Joy was the champion,  
**Translation:** 

**[2403.00s] English:** but he was like alone in that  
**Translation:** 

**[2404.58s] English:** in seeing there was a role for JavaScript  
**Translation:** 

**[2407.00s] English:** as the, as I call it, the sidekick language,  
**Translation:** 

**[2410.52s] English:** robbing the boy hostage.  
**Translation:** Vocabulary: sidekick: 辅助者

**[2412.76s] English:** Frank Miller put it in the Dark Knight Returns.  
**Translation:** 

**[2416.36s] English:** That there was this silly little language  
**Translation:** 

**[2418.50s] English:** that would be the glue language  
**Translation:** 

**[2419.48s] English:** and it could become important over time.  
**Translation:** 

**[2421.02s] English:** And you were better off having that complementarity,  
**Translation:** 

**[2423.92s] English:** that pairing of languages,  
**Translation:** Vocabulary: complementarity: 互补性

**[2424.98s] English:** just like Microsoft stacked it  
**Translation:** 

**[2426.92s] English:** with Visual C++ and Visual Basic.  
**Translation:** 

**[2428.66s] English:** So what was the big moment of I'm done?  
**Translation:** 

**[2432.90s] English:** So I had to do a demo.  
**Translation:** 

**[2434.48s] English:** I forget the dates.  
**Translation:** 

**[2435.58s] English:** I think I, for a history of programming languages,  
**Translation:** 

**[2438.34s] English:** paid for the Ellen Wurst Brock,  
**Translation:** 

**[2440.02s] English:** did with my help.  
**Translation:** Vocabulary: brock: 布罗克; wurst: 香肠

**[2440.82s] English:** He did a lot of the writing.  
**Translation:** 

**[2442.38s] English:** I think it was the 10 days  
**Translation:** 

**[2445.00s] English:** from like Thursday evening  
**Translation:** 

**[2447.24s] English:** through to the following weeks,  
**Translation:** 

**[2450.06s] English:** you know, the whole of that week  
**Translation:** 

**[2451.46s] English:** and then into the Monday.  
**Translation:** 

**[2452.44s] English:** Did you get sleep?  
**Translation:** 

**[2453.30s] English:** Not enough.  
**Translation:** 

**[2454.06s] English:** And I was really going fast  
**Translation:** 

**[2456.20s] English:** because I'd already used a lot of,  
**Translation:** 

**[2457.86s] English:** you know,  
**Translation:** 

**[2458.66s] English:** C compiler and front-end compiler knowledge  
**Translation:** 

**[2462.24s] English:** that I'd gained from undergraduate school.  
**Translation:** 

**[2464.68s] English:** When I started getting into computing  
**Translation:** Vocabulary: computing: 计算机科学; undergraduate: 本科生

**[2466.00s] English:** as a renegade physics major,  
**Translation:** 

**[2469.70s] English:** people were formalizing more efficient  
**Translation:** Vocabulary: renegade: 叛逆者

**[2472.48s] English:** bottom-up grammars,  
**Translation:** 

**[2474.70s] English:** parsers for bottom-up languages.  
**Translation:** Vocabulary: parsers: 解析器

**[2476.80s] English:** Really, LALR1 was the big thing.  
**Translation:** 

**[2479.62s] English:** And I studied all this  
**Translation:** 

**[2480.58s] English:** and learned how to parse them.  
**Translation:** 

**[2482.44s] English:** And in the end,  
**Translation:** Vocabulary: parse: 解析

**[2483.76s] English:** if you're doing C languages,  
**Translation:** 

**[2484.98s] English:** you often do what Dennis Ritchie did anyway,  
**Translation:** Vocabulary: ritchie: 里奇

**[2488.66s] English:** which is a recursive descent parser.  
**Translation:** 

**[2491.30s] English:** You can hand code it.  
**Translation:** Vocabulary: parser: 解析器; recursive: 递归的

**[2492.34s] English:** And I did that for JavaScript  
**Translation:** 

**[2493.94s] English:** in a blazing hurry.  
**Translation:** 

**[2496.30s] English:** Mostly got it right.  
**Translation:** 

**[2497.28s] English:** I didn't, you know,  
**Translation:** 

**[2498.00s] English:** have precedence inversion problems  
**Translation:** 

**[2499.52s] English:** or other bugs,  
**Translation:** Vocabulary: inversion: 倒置; precedence: 优先级

**[2500.16s] English:** but I copied a lot from Java and C.  
**Translation:** 

**[2503.08s] English:** And I tried to keep things simple,  
**Translation:** 

**[2505.18s] English:** like the equality operator  
**Translation:** 

**[2506.38s] English:** in those 10 days sprint  
**Translation:** 

**[2508.60s] English:** between two objects  
**Translation:** 

**[2510.48s] English:** of different dynamic type said,  
**Translation:** 

**[2512.42s] English:** no, they're not equal.  
**Translation:** 

**[2513.16s] English:** Their types are different.  
**Translation:** 

**[2514.12s] English:** And then after that,  
**Translation:** 

**[2515.66s] English:** I had internal early adopters  
**Translation:** Vocabulary: adopters: 早期使用者

**[2517.54s] English:** and they were using,  
**Translation:** 

**[2518.46s] English:** JavaScript to like match  
**Translation:** 

**[2520.00s] English:** a number against a database field that had been stringized.  
**Translation:** 

**[2523.88s] English:** And they said, oh, can't we just have implicit conversion?  
**Translation:** Vocabulary: implicit: 隐含转换; stringized: 字符串化

**[2526.06s] English:** And like an idiot, I agreed.  
**Translation:** 

**[2527.66s] English:** I gave them what they wanted.  
**Translation:** 

**[2528.62s] English:** I was trying to please them and get adoption.  
**Translation:** 

**[2530.30s] English:** And that broke what equivalence relation nature there was to the double equal.  
**Translation:** Vocabulary: equivalence: 等价关系

**[2539.28s] English:** There are some edge cases with not a number that break that too.  
**Translation:** 

**[2543.38s] English:** But it really broke it.  
**Translation:** 

**[2545.00s] English:** Having implicit conversions in the operator is something that people still roast me over.  
**Translation:** 

**[2549.14s] English:** So let's talk about two things.  
**Translation:** Vocabulary: conversions: 隐式转换

**[2551.76s] English:** One, it sounds like the comparison operator, the equality operator, is the thing that you regret.  
**Translation:** 

**[2558.82s] English:** So maybe can you...  
**Translation:** 

**[2559.74s] English:** Making it sloppy.  
**Translation:** 

**[2560.56s] English:** Making it sloppy.  
**Translation:** 

**[2561.32s] English:** So what is the biggest thing you regret in those 10 days?  
**Translation:** 

**[2565.12s] English:** And what is the biggest thing you're proud of?  
**Translation:** 

**[2567.46s] English:** So that making it sloppy came after the 10 days.  
**Translation:** 

**[2569.68s] English:** And my lesson there, which I've tweeted, is when people come to you saying,  
**Translation:** 

**[2573.18s] English:** can you please make it sloppy or add this cute feature?  
**Translation:** 

**[2576.04s] English:** The answer should be no.  
**Translation:** 

**[2577.38s] English:** And I should have known that because I think,  
**Translation:** 

**[2579.20s] English:** Niklaus Wirth, one of my heroes, said,  
**Translation:** 

**[2581.18s] English:** the essence of design is leaving things out.  
**Translation:** 

**[2584.30s] English:** But during the 10 days, I also, like I said,  
**Translation:** 

**[2586.16s] English:** I was in such a hurry, I left out garbage collection.  
**Translation:** 

**[2588.36s] English:** Came back to haunt me, but I got reference counting in in time  
**Translation:** 

**[2591.14s] English:** that people weren't running out of memory right away on long-lived JavaScript.  
**Translation:** 

**[2595.94s] English:** What happens when you don't have garbage collection and you have objects?  
**Translation:** 

**[2598.54s] English:** Well, you just run out of memory.  
**Translation:** 

**[2601.16s] English:** And, you know...  
**Translation:** 

**[2601.72s] English:** Love it.  
**Translation:** 

**[2602.24s] English:** At first, you write a short script and the page doesn't last long or it doesn't do a lot.  
**Translation:** 

**[2605.90s] English:** It's okay.  
**Translation:** 

**[2606.28s] English:** Oh, I see. Yeah, yeah.  
**Translation:** 

**[2607.10s] English:** But if you're writing a game or something and you're...  
**Translation:** 

**[2609.00s] English:** Doing event-based allocation, you run out of memory.  
**Translation:** Vocabulary: allocation: 分配

**[2611.62s] English:** And this was noticed in the summer of 1995 and people were like,  
**Translation:** 

**[2614.98s] English:** what's going on?  
**Translation:** 

**[2615.60s] English:** Oh, yeah, I got to get...  
**Translation:** 

**[2616.64s] English:** I better go back and do reference counting.  
**Translation:** 

**[2618.58s] English:** And then the problem with reference counting is you're writing the language in the runtime in C,  
**Translation:** 

**[2623.12s] English:** an unsafe language.  
**Translation:** Vocabulary: runtime: 运行时

**[2624.38s] English:** And if you're reference counting and you overflow the counter,  
**Translation:** 

**[2627.40s] English:** you mismanage it so it goes high, it gets stuck high,  
**Translation:** Vocabulary: mismanage: 管理不当; overflow: 溢出

**[2629.66s] English:** you leak memory again and you run out.  
**Translation:** 

**[2631.50s] English:** If you underflow it, you pre-memory that's still in use.  
**Translation:** Vocabulary: underflow: 溢出

**[2636.20s] English:** And even then, we knew what all the...  
**Translation:** 

**[2639.00s] English:** Security hackers...  
**Translation:** Vocabulary: hackers: 黑客

**[2640.00s] English:** came to know that you therefore have a potentially a remote code execution vulnerability because this  
**Translation:** 

**[2646.00s] English:** is before things like non-executable heap memory and stack defenses against taking over memory so  
**Translation:** Vocabulary: vulnerability: 漏洞

**[2654.88s] English:** if you can from the the remote side write some html and javascript that just happens to exploit  
**Translation:** 

**[2660.48s] English:** a bug in memory safety like it causes javascript to underflow a reference counter and the script  
**Translation:** 

**[2665.36s] English:** still has its hands on that object and it's trying to call a method on it and there's some kind of  
**Translation:** 

**[2669.52s] English:** lookup function table in the object but you've managed to stuff the heap with strings that  
**Translation:** Vocabulary: lookup: 查找表

**[2675.60s] English:** forge their own look-alike for the function table you can call some other code and this was a problem  
**Translation:** 

**[2682.80s] English:** right away so security you know javascript upped the ante java had this problem too but in its own  
**Translation:** Vocabulary: forge: 铸造

**[2688.00s] English:** vm and it just was you know a separate headache for son to worry about we had this problem in  
**Translation:** 

**[2694.32s] English:** netscape right away so netscape 2 came out after my 10 days and after these you know  
**Translation:** Vocabulary: netscape: 网景浏览器

**[2699.52s] English:** follow-on work to embed um javascript better in the browser and to add garbage or collection  
**Translation:** 

**[2704.88s] English:** through reference counting really i call it reference counting and get it shipped we had  
**Translation:** Vocabulary: embed: 嵌入

**[2709.68s] English:** a bunch of dot releases where we fix security bugs like maniacs but what is the thing you're  
**Translation:** 

**[2715.76s] English:** you know when you sit back on a porch and just look out into the sunset what are you  
**Translation:** Vocabulary: maniacs: 狂热者

**[2720.16s] English:** most proud of from those 10 days i think the first class functions shines i think  
**Translation:** 

**[2724.00s] English:** especially since java didn't have it and it was somewhat unusual the ski made it in somehow uh  
**Translation:** 

**[2729.52s] English:** At the end of the day, in spirit, I mean, people complain because scheme has, you know, minimalism, it has, you know, six or seven special forms, it has hygienic macros, it has call CC, it has sort of a beautiful, complete set of forms to make the Lambda calculus pleasant to use in practice. And JavaScript is, you know, kind of multi paradigm or shambolic.  
**Translation:** 

**[2754.94s] English:** Just a small tangent, you mentioned Marc Andreessen, it sounds like  
**Translation:** Vocabulary: andreessen: 安德森; calculus: 算术; hygienic: 卫生的; lambda: 兰姆达; macros: 宏; minimalism: 极简主义; paradigm: 范式; shambolic: 混乱的; tangent: 旁白

**[2760.00s] English:** like in bill joy but staying on mark it sounds like he had an impact on you in that he sort of  
**Translation:** 

**[2767.44s] English:** believed in what you were doing there can you can you talk about like what role mark had in your  
**Translation:** 

**[2771.44s] English:** life yeah we would meet at the um the peninsula creamery in downtown palo alto and mark was just  
**Translation:** 

**[2778.44s] English:** fresh out of you know grad school or whatever he was doing and he was a big dude and he got fitter  
**Translation:** Vocabulary: creamery: 奶制品厂; peninsula: 半岛

**[2784.22s] English:** later uh he had hair he he would order giant milkshakes and burgers and we would meet there  
**Translation:** 

**[2789.56s] English:** and brainstorm about what to do and it was very direct because we didn't have much time the the  
**Translation:** Vocabulary: milkshakes: 奶昔

**[2795.26s] English:** sort of we didn't talk about it the implication was microsoft's coming after us mark was saying  
**Translation:** 

**[2799.74s] English:** things boldly pre-ipo like netscape plus java kills windows right this is ambitious make a  
**Translation:** Vocabulary: implication: 暗示

**[2805.90s] English:** browser programmable it becomes the new runtime for programs it's the meta os or it's the replacement  
**Translation:** 

**[2810.96s] English:** os um but he still saw value in javascript yes even though he was saying that and java was the  
**Translation:** Vocabulary: runtime: 运行时环境

**[2816.70s] English:** big name hence the trademark license uh  
**Translation:** 

**[2819.56s] English:** he saw javascript as important and he even thought what if we got i told this in other  
**Translation:** 

**[2824.30s] English:** interviews i can say he thought what if we had uh my friend kip hickman who'd been at  
**Translation:** 

**[2828.70s] English:** netscape from the beginning and who was a colonel hacker at sgi when i joined  
**Translation:** Vocabulary: hacker: 电脑高手; netscape: 网景浏览器

**[2832.22s] English:** he started writing his own jvm before we consummated the sun deal and got our hands on  
**Translation:** 

**[2837.08s] English:** their code and the java compiler java c which arthur van hoff had written very nice code  
**Translation:** Vocabulary: consummated: 正式获得

**[2842.80s] English:** was all written in java it was self-hosted or so-called bootstrap and so we could use that  
**Translation:** 

**[2849.56s] English:** run the bytecode from the the sun uh jvm running the self-hosted compiler to emit the bytecode  
**Translation:** Vocabulary: bootstrap: 启动代码; bytecode: 字节码

**[2857.16s] English:** so once we could bootstrap into kip's vm we wouldn't need sun and mark was like well maybe  
**Translation:** 

**[2861.50s] English:** we can just you know ditch sun or kip's java vm or if you're a javascript vm we now we need  
**Translation:** Vocabulary: ditch: 抛弃

**[2867.80s] English:** graphics so mark was thinking far ahead because he knew you could do things with html and images  
**Translation:** 

**[2873.22s] English:** but at some point you really want like dynamics or yeah three-dimensional like even sgi had already  
**Translation:** 

**[2879.56s] English:** downfall  
**Translation:** 

**[2880.00s] English:** Because the first floor VLSI team there had gone off to do 3DFX and all these other companies that made the graphics card on your PC, right?  
**Translation:** Vocabulary: downfall: 衰落

**[2887.56s] English:** Doom was big and Quake.  
**Translation:** 

**[2889.38s] English:** And so we were all playing Quake.  
**Translation:** 

**[2890.68s] English:** I was old, so I was terrible.  
**Translation:** 

**[2892.58s] English:** But why not put that graphics capability on the web?  
**Translation:** Vocabulary: capability: 能力

**[2896.34s] English:** And in fact, it finally happened at Mozilla with Firefox era with Vlad Vukichevich taking OpenGL ES and reflecting it as WebGL.  
**Translation:** 

**[2903.94s] English:** But OpenGL ES is the mobile version of OpenGL, which is a standard based on SGI GL.  
**Translation:** 

**[2910.34s] English:** So there's this whole lineage of graphics libraries or really graphics languages for what became the GPU.  
**Translation:** 

**[2916.32s] English:** And Mark was thinking ahead.  
**Translation:** Vocabulary: lineage: 传承

**[2917.32s] English:** He's like, we need graphics too.  
**Translation:** 

**[2918.56s] English:** And I thought, okay, I can try to get somebody I knew at SGI, but he's a grad student at MIT.  
**Translation:** 

**[2922.62s] English:** He was studying under Barbara Liskoff.  
**Translation:** 

**[2924.34s] English:** He laughed when he heard about this later.  
**Translation:** 

**[2926.14s] English:** Andrew Myers, he's at Cornell, long time, I think he's a full professor.  
**Translation:** 

**[2930.00s] English:** And Mark said, great, we'll get him.  
**Translation:** Vocabulary: myers: 迈尔斯

**[2931.94s] English:** I'm not sure he's going to come.  
**Translation:** 

**[2933.08s] English:** We'll throw money.  
**Translation:** 

**[2933.76s] English:** You know, stock options.  
**Translation:** 

**[2934.92s] English:** We never did it.  
**Translation:** 

**[2936.12s] English:** And they did the Sun deal.  
**Translation:** 

**[2937.70s] English:** So Kip Nobly put aside his own JVM and we used the Sun JVM.  
**Translation:** Vocabulary: nobly: 高尚地

**[2942.48s] English:** So that was an ambitious period.  
**Translation:** 

**[2943.96s] English:** And Mark was very generative because he was pushing hard.  
**Translation:** Vocabulary: generative: 富有创造力的

**[2946.60s] English:** He was ambitious and he wanted to have Netscape possibly be in control of the ball.  
**Translation:** 

**[2953.60s] English:** Maybe you can speak to this dance of Netscape versus Internet Explorer.  
**Translation:** Vocabulary: explorer: 浏览器; netscape: 网景

**[2962.08s] English:** You've thrown some.  
**Translation:** 

**[2963.76s] English:** Loving words towards Microsoft throughout this conversation.  
**Translation:** 

**[2966.64s] English:** But that's a theme with the Steve Jobs had a similar sort of commentary from a big sort of philosophical principle perspective.  
**Translation:** 

**[2974.48s] English:** Can you comment on like the approach that Microsoft has taken with Internet Explorer from IE1 to Edge today?  
**Translation:** Vocabulary: philosophical: 哲学思想

**[2982.10s] English:** Is there something that you see as valuable that they're doing in the in the occasional copying and that kind of stuff?  
**Translation:** 

**[2989.56s] English:** Or is it is the world worse off?  
**Translation:** 

**[2993.26s] English:** Because Internet Explorer exists.  
**Translation:** 

**[2995.30s] English:** So I'm going to segment this into historical eras because I think Microsoft is today with Satya is quite a different.  
**Translation:** 

**[3000.00s] English:** company and what they're doing with edge is different but back then um gates you know  
**Translation:** 

**[3004.70s] English:** aggressive character not really original in my view uh not an originator steve jobs famously  
**Translation:** Vocabulary: originator: 首创者

**[3010.48s] English:** said once he doesn't have any taste and i don't mean this in a small way he has no taste  
**Translation:** 

**[3014.46s] English:** you can see this apple at the time had beautiful typography and you know ligatures and kerning and  
**Translation:** Vocabulary: kerning: 字距调整; ligatures: 连字; typography: 排版

**[3020.84s] English:** the fonts looked great and windows had this sort of ugly system font that was carefully  
**Translation:** 

**[3025.74s] English:** aligned with pixels so it didn't get what what is it i'm sorry to keep interrupting but why did  
**Translation:** Vocabulary: aligned: 对齐; fonts: 字体; interrupting: 打断; pixels: 像素

**[3030.60s] English:** why was internet explorer winning throughout the history of these competitions distribution  
**Translation:** 

**[3034.76s] English:** distribution matters more than anything and this is why um you know even now we're seeing in the  
**Translation:** 

**[3039.94s] English:** browser wars edge doing better because it's being foisted on people of windows we have windows 10  
**Translation:** 

**[3044.06s] English:** boxes at home we have some windows 7 boxes we or laptops we keep running too because we  
**Translation:** Vocabulary: foisted: 强加

**[3048.58s] English:** we don't connect them to the internet generally but um but but uh once you have that operating  
**Translation:** 

**[3054.96s] English:** system  
**Translation:** 

**[3055.28s] English:** you can you can force you know edge and apple did it with safari too it's not unique to microsoft  
**Translation:** 

**[3060.94s] English:** that's sad but distribution matters and that's why uh i think ie was going to win that's why  
**Translation:** 

**[3067.42s] English:** everybody at netscape felt we're doomed this was something michael toy and jamie would say we're  
**Translation:** 

**[3071.28s] English:** doomed um but for a while there we had a chance and we innovated in netscape too we did a big  
**Translation:** Vocabulary: innovated: 创新

**[3076.64s] English:** platform push java and javascript and uh plugins more plugins and um you know more html table  
**Translation:** 

**[3084.50s] English:** features and  
**Translation:** 

**[3085.22s] English:** and really started making a programmable stack out of what were pretty static web languages and  
**Translation:** 

**[3091.00s] English:** even in the beta releases netscape two people were using javascript to build what you would  
**Translation:** Vocabulary: netscape: 网景浏览器

**[3095.16s] English:** call single page applications like gmail and they were using javascript locally to compute things and  
**Translation:** 

**[3100.48s] English:** to call the server on a hidden frame in the background so it was prefiguring a lot of what  
**Translation:** 

**[3105.40s] English:** came later as ajax or dynamic javascript dynamic html so people saw that i mean even when they saw  
**Translation:** 

**[3110.38s] English:** it yeah that's kind of um i don't know from my perspective that seems quite brilliant this is a  
**Translation:** 

**[3115.22s] English:** seems like really innovative that you would have code run in the browser it did impress me with  
**Translation:** 

**[3120.00s] English:** something which I learned later about from Eric von Hippel of MIT, which is user innovation  
**Translation:** Vocabulary: hippel: 冯·霍普尔

**[3125.36s] English:** networks, lead user effects, that throwing out JavaScript, even though we weren't doing open  
**Translation:** 

**[3130.08s] English:** source, we were doing beta releases early and permissively with Netscape, getting early developer  
**Translation:** Vocabulary: permissively: 宽松地

**[3135.42s] English:** feedback, absolutely critical. I loved it. I did some of that with SGI with some of the products I  
**Translation:** 

**[3139.92s] English:** worked on, but it really came to the fore in Netscape. And that culminated in Mozilla, where  
**Translation:** Vocabulary: culminated: 达到顶点

**[3143.86s] English:** you're dealing with developers all the time and early adopters, lead users. But the lead users  
**Translation:** 

**[3148.24s] English:** helped improve JavaScript, even in those last few betas where I could hardly change things. I was  
**Translation:** Vocabulary: adopters: 早期采用者

**[3152.74s] English:** under pretty rigid change control. So we're talking about just a small collection of individuals that  
**Translation:** 

**[3156.98s] English:** are just like upfront. A guy named Bill Dortch. You can find his work in the web archive still  
**Translation:** 

**[3161.02s] English:** from 1996. It's a single page application. It's an artist gallery of mountain art. He uses JavaScript.  
**Translation:** 

**[3167.14s] English:** It doesn't quite work. He uses JavaScript locally. He uses a local database. What you would think of  
**Translation:** 

**[3171.26s] English:** now is JSON, but it's all pure JavaScript code, a bunch of objects being constructed. That's so cool.  
**Translation:** 

**[3177.14s] English:** So how is...  
**Translation:** 

**[3178.24s] English:** If you can do sort of a big sweeping progress of JavaScript, how has JavaScript changed over the  
**Translation:** 

**[3184.94s] English:** years? Any of you from those early 10 days with a quick addition of garbage collection and fixes  
**Translation:** Vocabulary: sweeping: 全面的

**[3189.80s] English:** around security, how has this evolution that now it's taken over the world?  
**Translation:** 

**[3195.14s] English:** It's been a bumpy ride because the standards body got shut down after Microsoft, I think,  
**Translation:** Vocabulary: bumpy: 坎坷的

**[3200.42s] English:** took over the web and then felt punished by the US v. Microsoft antitrust case.  
**Translation:** 

**[3205.36s] English:** Can you speak to the standard body?  
**Translation:** Vocabulary: antitrust: 反垄断机构

**[3207.00s] English:** That was a fun ride too.  
**Translation:** 

**[3208.24s] English:** Because Netscape had taken the lead with the web and HTML innovations like frames and framesets,  
**Translation:** Vocabulary: framesets: 框架集; innovations: 创新

**[3216.44s] English:** tables, and the W3C was sort of off even then sort of in SGML land heading toward XML  
**Translation:** 

**[3221.16s] English:** la-la land. I'm going to be a little harsh on it.  
**Translation:** 

**[3224.50s] English:** What's SGML? I'm sorry.  
**Translation:** 

**[3225.58s] English:** SGML was the precursor markup language to HTML. It was sort of the more extensible  
**Translation:** Vocabulary: extensible: 可扩展的; markup: 标记; precursor: 前身

**[3230.74s] English:** standard generalized markup language. It was a...  
**Translation:** 

**[3235.08s] English:** XML-like...  
**Translation:** Vocabulary: generalized: 普遍化的

**[3235.88s] English:** Pointy brackets, but it had all sorts of elaborate syntax.  
**Translation:** 

**[3238.24s] English:** We're doing different...  
**Translation:** Vocabulary: brackets: 尖括号; elaborate: 复杂; pointy: 尖锐; syntax: 语法

**[3240.00s] English:** different semantics. And this is why I think, you know, TBL and others who wanted to do the semantic web then took XML forward. But they had this, or some of them anyway, had this strange idea they could replace the web with XML or that they would upgrade the web to be XML. And it couldn't be done. Worse is better had concrete meaning. The web was very forgiving of HTML, including sort of minor syntax errors that could be error corrected.  
**Translation:** 

**[3266.36s] English:** Like error correction isn't generally done in programming languages.  
**Translation:** Vocabulary: semantic: 语义; semantics: 语义学

**[3269.28s] English:** Right. That's another amazing thing about HTML is like, it's more like biology than programming.  
**Translation:** 

**[3274.88s] English:** Yeah, exactly. And so XML was in its standard form, super strict and could never have admitted, you know, the kind of users who are committing these errors. And the funniest part was Microsoft said, hey, we're doing XML. But the way they put it in Internet Explorer under the default media type, put it through the HTML error corrector.  
**Translation:** Vocabulary: explorer: 互联网探索者

**[3293.74s] English:** Oh, wow.  
**Translation:** 

**[3294.70s] English:** So they kind of bastardized it.  
**Translation:** Vocabulary: bastardized: 歪曲

**[3296.36s] English:** To make it popular and usable and accessible. And so XML as a pure, you know, thing was never going to take over. And the W3C was kind of not fully functional because Netscape wasn't cooperating with them.  
**Translation:** 

**[3309.40s] English:** We thought about where to take JavaScript and we realized our standards guru, Carl Cargill, realized there was a European standards body that had already given Microsoft fits by standardizing parts of the Windows 3.1 API, which European governments insisted on.  
**Translation:** Vocabulary: cargill: 卡尔·卡格; cooperating: 合作; netscape: 网景; standardizing: 标准化; usable: 可用的

**[3324.04s] English:** They said, Microsoft, we can't use your operating system.  
**Translation:** 

**[3326.20s] English:** We can't do anything without some standards. And Microsoft said, you know, here's our docs. And the government said, no, we need a European standard. So this body called the European Computer Manufacturers Association, ECMA, which eventually became global and became a proper noun instead of an acronym.  
**Translation:** Vocabulary: acronym: 缩写

**[3341.08s] English:** Right. It's just one capital E now with a lowercase CMA.  
**Translation:** 

**[3344.74s] English:** Right. And as one of the early Microsoft guys I met when we first convened a working group to talk about JavaScript said, it sounds like a skin disease.  
**Translation:** Vocabulary: convened: 召集; lowercase: 小写

**[3353.24s] English:** But it gave, I mean, maybe you'll speak to that.  
**Translation:** 

**[3356.20s] English:** But it gave the name to JavaScript of ECMAScript.  
**Translation:** 

**[3358.90s] English:** That was the standard name because.  
**Translation:** 

**[3360.00s] English:** Because Java was a trademark of Suns.  
**Translation:** Vocabulary: trademark: 注册商标

**[3362.84s] English:** They were so aggressive.  
**Translation:** 

**[3363.76s] English:** They were sending cease and desist letters to people whose Middle European heritage meant their surname was Javanko.  
**Translation:** 

**[3370.82s] English:** And they called their website Javanko.com.  
**Translation:** 

**[3373.06s] English:** And Sun would send them a letter saying, you're using JAVA at the start of your domain name.  
**Translation:** 

**[3376.82s] English:** You must cease and desist.  
**Translation:** 

**[3378.54s] English:** I love marketing more than anything else in this world.  
**Translation:** 

**[3381.98s] English:** So ECMAScript and now is popularly named as ES plus version.  
**Translation:** 

**[3387.32s] English:** I would say people use JS more than anything.  
**Translation:** 

**[3389.74s] English:** People still say JavaScript.  
**Translation:** 

**[3391.18s] English:** JavaScript is in all the books.  
**Translation:** 

**[3392.60s] English:** So, I mean, when you're referring to it, it's usually JavaScript.  
**Translation:** 

**[3394.88s] English:** And when you want to refer to a version of JavaScript, you'll say ES6, ES5.  
**Translation:** 

**[3399.14s] English:** Yes.  
**Translation:** 

**[3399.52s] English:** Or now they've gone to years, which is kind of confusing because it's an offset of 2009.  
**Translation:** 

**[3405.74s] English:** ES6 is ES2016.  
**Translation:** 

**[3410.52s] English:** Yeah, it doesn't match the years perfectly.  
**Translation:** 

**[3412.70s] English:** Yeah.  
**Translation:** 

**[3412.82s] English:** So what were the choices made and how did JavaScript evolve here?  
**Translation:** 

**[3418.04s] English:** So we took this.  
**Translation:** 

**[3419.54s] English:** This new standards body, which had, we thought, sort of a proven record of standing up to Microsoft.  
**Translation:** 

**[3425.42s] English:** But Microsoft sent a lot of people.  
**Translation:** 

**[3427.56s] English:** They sent some people who were pretty good.  
**Translation:** 

**[3430.66s] English:** And then when they realized that I was there and Netscape was not going to, you know, just bend over and do whatever they wanted, they sent somebody really good.  
**Translation:** 

**[3437.30s] English:** And he was a smart guy.  
**Translation:** Vocabulary: netscape: 网景公司

**[3437.92s] English:** He did a lot of the work on the first draft of the spec.  
**Translation:** 

**[3440.86s] English:** Sean Katzenberger, he's left Microsoft.  
**Translation:** 

**[3442.86s] English:** He even did what I sort of did.  
**Translation:** 

**[3445.26s] English:** He told his bosses, stop bugging me to do other things.  
**Translation:** 

**[3447.94s] English:** I'm focused on this.  
**Translation:** 

**[3448.90s] English:** Because it took a lot of focused work to create the first draft of the spec.  
**Translation:** 

**[3452.14s] English:** And I was still holding, I was spinning almost all the plates.  
**Translation:** 

**[3454.92s] English:** I had, like, part-time help in certain areas.  
**Translation:** Vocabulary: spinning: 旋转

**[3457.10s] English:** And on the front-end integrations, I had the front-end guys.  
**Translation:** 

**[3460.14s] English:** But I couldn't take as much time as Sean was to write the draft spec.  
**Translation:** Vocabulary: integrations: 集成

**[3463.70s] English:** But I had to participate because I was essentially helping write down what the language did.  
**Translation:** 

**[3468.08s] English:** And in areas where we didn't like what it did and Microsoft didn't agree, we sometimes got away with slight changes.  
**Translation:** 

**[3474.70s] English:** And that's the story of standards.  
**Translation:** 

**[3475.86s] English:** You have different implementations.  
**Translation:** Vocabulary: implementations: 实施方案

**[3478.06s] English:** And depending on their market.  
**Translation:** 

**[3478.90s] English:** And depending on their market power.  
**Translation:** 

**[3480.00s] English:** interoperate where you have agreement and where they don't the dominant one usually sets the  
**Translation:** 

**[3484.34s] English:** de facto standard and then you should probably reflect that into the de jure standard  
**Translation:** Vocabulary: facto: 实际上; interoperate: 协同工作

**[3488.64s] English:** and this happened with javascript uh over time as netscape went down and microsoft went up  
**Translation:** 

**[3493.56s] English:** we did the first edition of the standard um codified in 1997 in france we had a trip to  
**Translation:** Vocabulary: codified: 制定成文

**[3499.58s] English:** nice uh which was very memorable for any interesting reason or just because it's nice  
**Translation:** 

**[3504.34s] English:** and and ekma's european and ibm and others were you know there uh mike kalasha and ibm fellow was  
**Translation:** 

**[3510.76s] English:** a britisher and we the the guy who ran ekma at the time jan vandenbell was quite a uh a raconteur  
**Translation:** 

**[3517.66s] English:** and a very fun guy and he had us out for you know the great you know fuidamere the boyabays and  
**Translation:** Vocabulary: raconteur: 说故事的人

**[3523.28s] English:** was the standardization process beautiful or painful that those early days you as a designer  
**Translation:** 

**[3528.12s] English:** it was painful because it was rushed now guy steel was contributed by sun so even more than sean you  
**Translation:** Vocabulary: standardization: 标准化过程

**[3533.70s] English:** had this giant  
**Translation:** 

**[3534.32s] English:** brain guy steel helping bringing some of that scheme magic he even brought richard  
**Translation:** 

**[3538.10s] English:** gabriel for fun and richard wrote the fourth clause of the standard which is kind of an intro  
**Translation:** 

**[3543.78s] English:** to what javascript's all about so we had some really good people and we didn't fight too much  
**Translation:** Vocabulary: intro: 介绍

**[3549.04s] English:** there was some tension where i was fixing bugs and i was late to a meeting and sean katzenberger  
**Translation:** 

**[3553.72s] English:** microsoft was actually mad like where is he we need him and when i got there i saw that only  
**Translation:** Vocabulary: katzenberger: 卡特森贝格

**[3559.48s] English:** he saw this sort of off by one bug and somewhere in the spec and then i saw it too and i said  
**Translation:** 

**[3564.28s] English:** sorry  
**Translation:** 

**[3564.32s] English:** there's a fence post bug there and then we kind of locked eyes and we realized we were on the same  
**Translation:** 

**[3568.02s] English:** page and we kind of he wasn't mad anymore what were the features that are being like struggled  
**Translation:** Vocabulary: struggled: 挣扎

**[3572.56s] English:** over and debated and thought about and it was mainly writing down what worked and what we  
**Translation:** 

**[3576.80s] English:** we thought should work in the edge cases that didn't interoperate or that seemed wrong uh but  
**Translation:** 

**[3581.68s] English:** we were already laying the groundwork for the future editions that i was already implementing  
**Translation:** 

**[3585.76s] English:** i was still trying to lead the standard by using the dominant market power to write the code that  
**Translation:** Vocabulary: groundwork: 基础工作; implementing: 实施

**[3591.48s] English:** actually shipped so the de facto standard would lead the de jure standard to the de jure standard  
**Translation:** 

**[3594.32s] English:** and i was putting in the the missing you know function forms that i didn't have time for in the  
**Translation:** 

**[3600.00s] English:** so this is the engineering mindset versus the theoretician so you didn't want to create the  
**Translation:** 

**[3604.46s] English:** perfect language but one that was the popular and chipped and all that kind of stuff and you  
**Translation:** Vocabulary: mindset: 思维模式; theoretician: 理论家

**[3607.72s] English:** could say there was i was standing on the shoulders of giants so there was a staged process where i  
**Translation:** 

**[3611.40s] English:** had to hold back things that were well designed by others in other languages and i could imitate  
**Translation:** 

**[3616.74s] English:** but i couldn't do them all in the 10 days so they came in in 1996 in 97 and they came into the  
**Translation:** 

**[3623.82s] English:** third edition of the standard which was finalized in 1999 but at that point netscape had been sold  
**Translation:** Vocabulary: netscape: 网景浏览器

**[3629.78s] English:** to aol and was which was a decent exit considering and uh you know had previously been mercilessly  
**Translation:** 

**[3636.74s] English:** crushed that netscape was selling the browser along with server software that it had acquired  
**Translation:** Vocabulary: mercilessly: 残酷地

**[3641.46s] English:** after its ipo and microsoft was just underpricing it so there was no way to compete with that  
**Translation:** 

**[3647.40s] English:** microsoft was also you know making internet explorer the default browser in windows which  
**Translation:** Vocabulary: explorer: 浏览器; underpricing: 低价销售

**[3653.32s] English:** is called tying and antitrust law and they were doing even more brutal things there's a famous  
**Translation:** 

**[3657.82s] English:** investor he did very  
**Translation:** Vocabulary: antitrust: 反垄断; brutal: 残忍; investor: 投资者

**[3659.76s] English:** well on google so he's a billionaire ram sriram and he was sales guy or head of sales at netscape  
**Translation:** 

**[3664.58s] English:** and he got off the phone looking ashen faced after compact called and said uh microsoft just told us  
**Translation:** Vocabulary: billionaire: 亿万富翁

**[3671.50s] English:** they're going to pull our windows license if we ship netscape as the default browser wow this is  
**Translation:** 

**[3675.90s] English:** so there's some bullying going on it was totally material in the antitrust case but but javascript  
**Translation:** Vocabulary: bullying: 恃强凌弱

**[3681.40s] English:** escaped into the standard setting where there was fairly good cooperation microsoft had a really  
**Translation:** 

**[3686.12s] English:** good guy on it and you know guy steel was there for a time and and  
**Translation:** 

**[3689.76s] English:** there was some good work but after the antitrust case and you know netscape kind of dissolving  
**Translation:** 

**[3696.92s] English:** into aol and not really going anywhere quickly mozilla took years to really bring up um the  
**Translation:** Vocabulary: dissolving: 解散

**[3702.64s] English:** standard froze and by 2003 even though they've been sort of noodling around with advanced versions  
**Translation:** 

**[3707.50s] English:** javascript 2 i'd given the keys to the kingdom to another mit grad baltimore horwatt very big  
**Translation:** Vocabulary: noodling: 摸索

**[3713.34s] English:** brain and still at google i think he won the putnam in 86 so he's yeah very mathematical  
**Translation:** 

**[3719.76s] English:** piece  
**Translation:** Vocabulary: mathematical: 数学的

**[3720.00s] English:** He designed this successor language, JavaScript 2, but it only showed up in mutated form in Microsoft's ASP.NET server side, and it didn't last there.  
**Translation:** 

**[3731.04s] English:** And it showed up in Flash, and that's what became ActionScript 3.  
**Translation:** Vocabulary: mutated: 变异

**[3734.24s] English:** Ah, ActionScript.  
**Translation:** 

**[3735.88s] English:** Interesting.  
**Translation:** 

**[3736.94s] English:** And then Flash, of course, declined.  
**Translation:** 

**[3738.62s] English:** And so how did we arrive at ES6, where it's like there's so many, where everyone, okay, there's this history of JavaScript that people were, it was just like cool when you're like having,  
**Translation:** 

**[3750.00s] English:** you know, drinking beers to talk crap about JavaScript.  
**Translation:** 

**[3752.48s] English:** Everyone loves to hate, like people who are married say, ah, marriage sucks, is they just want to let off some steam, even though everyone uses the language.  
**Translation:** 

**[3760.86s] English:** But ES6, it's become this like reputable, like it fixed major pain points, I think.  
**Translation:** 

**[3769.14s] English:** It added things to the language and added something that was already in ES5 strict mode, but made it implicit in class bodies and module bodies.  
**Translation:** Vocabulary: implicit: 隐含; module: 模块

**[3776.88s] English:** It was a big jump, but it accumulated some of the ES6.  
**Translation:** 

**[3780.00s] English:** It's four designs that we'd done with Adobe for what we hoped would be the fourth edition of TecnaScript that were supposed to fold in some of these old JavaScript 2 ideas that had come into ActionScript 3.  
**Translation:** Vocabulary: accumulated: 积累

**[3792.76s] English:** So you look at the family tree and you see these forks, and the main ones are the ones that go into Adobe Flash, acquired from Acromedia, and the one that went into the server side of Microsoft's stack, which kind of died.  
**Translation:** 

**[3806.78s] English:** And then trying to bring them back into the standard and not quite succeeding.  
**Translation:** Vocabulary: acromedia: 阿克罗梅德

**[3810.00s] English:** So ES4 was mothballed, but all the good parts that everyone liked made it into ES6.  
**Translation:** 

**[3815.92s] English:** And so that was a success.  
**Translation:** Vocabulary: mothballed: 停止使用

**[3817.04s] English:** And I said earlier I had the wrong year.  
**Translation:** 

**[3818.36s] English:** I think it's 2015, so it's off by...  
**Translation:** 

**[3820.36s] English:** For ES6.  
**Translation:** 

**[3822.38s] English:** Yeah, it was done, finalized in 2015.  
**Translation:** 

**[3824.30s] English:** It took a little longer than we hoped, because ES5 was 2009, and that was a smaller increment from ES3.  
**Translation:** 

**[3831.54s] English:** We skipped four again.  
**Translation:** Vocabulary: increment: 增加量

**[3832.32s] English:** We mothballed it.  
**Translation:** 

**[3833.54s] English:** And we had a split in the committee where some people said, you know, ES4 is too big.  
**Translation:** 

**[3837.50s] English:** We're going to work on incremental improvements.  
**Translation:** 

**[3839.44s] English:** No new stuff.  
**Translation:** Vocabulary: incremental: 逐步的

**[3840.00s] English:** syntax in particular they promised not quite true but uh they they added a bunch of interesting apis  
**Translation:** 

**[3846.24s] English:** alan weir sprock my co-author of the hobble paper and he was at microsoft at the time i ended up  
**Translation:** Vocabulary: hobble: 束缚; syntax: 句法

**[3851.44s] English:** hiring with mozilla he wanted to get to mozilla and and keep doing the sort of editoring editor  
**Translation:** 

**[3857.76s] English:** job of the javascript standard ecma script um and when we got es6 done it was it was a little late  
**Translation:** Vocabulary: editoring: 编辑工作

**[3864.56s] English:** 2015 and we switched to year numbers so people still call it es6 i call es6 yeah but if you  
**Translation:** 

**[3870.38s] English:** remember you know off by nine plus 2000 yeah i mean es6 is such a big job i mean like you said  
**Translation:** 

**[3876.94s] English:** there's a third that connects all of it but es6 is when it's like became this language that it  
**Translation:** 

**[3881.80s] English:** almost feels ready to take over the world completely more programming in the large  
**Translation:** 

**[3886.18s] English:** features more yeah features you need for larger teams and it software engineering microsoft did  
**Translation:** 

**[3890.80s] English:** something smart too they uh anders and company um  
**Translation:** 

**[3894.56s] English:** luke hoban who's left microsoft also did typescript and they realized uh something i think  
**Translation:** 

**[3900.34s] English:** that glad brock has also popularized and and uh he was involved in darted google if you don't worry  
**Translation:** Vocabulary: hoban: 霍班; popularized: 推广

**[3907.38s] English:** about soundness in the type system you don't try to enforce the type checks at runtime in particular  
**Translation:** 

**[3911.74s] English:** just use it as sort of a warning system a tool time type system you can still have a lot of value  
**Translation:** Vocabulary: runtime: 运行时; soundness: 一致性

**[3916.14s] English:** for developers especially in large projects so typescript's been a roaring success for microsoft  
**Translation:** 

**[3921.20s] English:** what do you think about type what do you think about typescript is it  
**Translation:** 

**[3924.56s] English:** adding confusion or is it ultimately beneficial i think it's beneficial now it's technically a  
**Translation:** 

**[3929.82s] English:** superset of javascript so of course i love it right the shortest uh javascript program is still  
**Translation:** 

**[3935.78s] English:** a typescript program any javascript program is a typescript program which is brilliant because  
**Translation:** 

**[3939.22s] English:** then you can start incrementally adding type annotations getting warnings yes learning how  
**Translation:** Vocabulary: annotations: 注释; incrementally: 逐步地

**[3943.34s] English:** to use them microsoft's had to kind of look around corners at the standards body and guess how  
**Translation:** 

**[3948.66s] English:** their version of modules or decorators should work and and the standards body then may  
**Translation:** Vocabulary: decorators: 装饰器

**[3954.56s] English:** be able to do things a bit so i think they're obligated with typescript either to carry their  
**Translation:** 

**[3958.66s] English:** own version or to  
**Translation:** Vocabulary: obligated: 有责任

**[3960.00s] English:** bring it back with incompatible changes toward the standard over time.  
**Translation:** 

**[3963.26s] English:** And I think they've played generally fair there.  
**Translation:** Vocabulary: incompatible: 不兼容

**[3965.38s] English:** There's some sentiment that why don't they standardize TypeScript?  
**Translation:** 

**[3967.96s] English:** Well, they've been clear they don't want to.  
**Translation:** Vocabulary: sentiment: 公众看法; standardize: 规范化

**[3969.78s] English:** They have a proprietary investment.  
**Translation:** 

**[3971.26s] English:** It's valuable.  
**Translation:** 

**[3971.86s] English:** They have control of the ball.  
**Translation:** 

**[3973.40s] English:** And in some ways, you can say the same thing to any of the other big companies in the standards body.  
**Translation:** 

**[3978.08s] English:** Why doesn't Google standardize its stuff?  
**Translation:** 

**[3980.28s] English:** So you think it'll continue being like a kind of dance partner to JavaScript, to the base JavaScript?  
**Translation:** 

**[3985.46s] English:** There's a hope that at some point, if they keep reconverging it and the standard doesn't break them and goes in a good direction,  
**Translation:** 

**[3991.98s] English:** we will get at least the annotation syntax and some semantics around them.  
**Translation:** Vocabulary: annotation: 注解; semantics: 语义; syntax: 语法

**[3997.02s] English:** Because when you're talking about type annotations, they're generally on parameters and return values and variable declarations.  
**Translation:** 

**[4004.00s] English:** They're cast operators.  
**Translation:** Vocabulary: declarations: 变量声明

**[4005.46s] English:** You want that syntax to be reserved, and you want it to work the same in all engines.  
**Translation:** 

**[4009.68s] English:** And this is where ideas like Gilad's pluggable type systems might be good,  
**Translation:** Vocabulary: pluggable: 可插拔的

**[4014.24s] English:** though then you could create the same.  
**Translation:** 

**[4015.46s] English:** Same problem you have with Lisp and Scheme, where there's a bunch of macro libraries,  
**Translation:** Vocabulary: macro: 宏外设

**[4018.54s] English:** and they don't agree, and you have conflicts between them.  
**Translation:** 

**[4021.80s] English:** But pluggable type systems could be one way to standardize this.  
**Translation:** 

**[4024.94s] English:** What do you think about the giant ecosystem of frameworks in JavaScript?  
**Translation:** 

**[4029.82s] English:** It feels like, because this is a side effect of how many people use JavaScript,  
**Translation:** 

**[4035.52s] English:** a lot of entrepreneurial spirit create their own JavaScript frameworks,  
**Translation:** 

**[4042.04s] English:** and they're actually awesome.  
**Translation:** Vocabulary: entrepreneurial: 创业精神

**[4044.56s] English:** In all different ways, and that, this is an interesting question about almost like philosophically about biological system and evolution,  
**Translation:** 

**[4055.24s] English:** all that kind of stuff.  
**Translation:** Vocabulary: philosophically: 哲学地

**[4056.12s] English:** Do you see that as good or should it, like, should some of them die out quicker?  
**Translation:** 

**[4060.32s] English:** I think that maybe they should.  
**Translation:** 

**[4061.86s] English:** Now, jQuery was a very clever thing.  
**Translation:** 

**[4064.82s] English:** John Resig made this library that was sort of query and do and blended sort of CSS selector syntax with JavaScript sort of object graph or DOM querying,  
**Translation:** Vocabulary: querying: 查询; selector: 选择器

**[4073.00s] English:** and made it very easy for people.  
**Translation:** 

**[4074.56s] English:** Do things almost like they were learning jQuery as its own language, as a domain-specific language, and  
**Translation:** 

**[4080.00s] English:** That, I think, reflected in part the difficulty of using the document object model, these APIs that were originally designed in the 90s for Java as well as JavaScript.  
**Translation:** 

**[4088.46s] English:** They're very object-oriented or even procedural.  
**Translation:** 

**[4091.78s] English:** They're very kind of verbose.  
**Translation:** 

**[4093.40s] English:** And it took like a constructor call and three different, you know, hokey-pokey dances to do something, whereas in jQuery, it's just one line, right?  
**Translation:** Vocabulary: constructor: 构造函数; verbose: 啰嗦

**[4100.72s] English:** So that fed back finally into the standards.  
**Translation:** 

**[4104.12s] English:** It didn't mean we standardized jQuery.  
**Translation:** Vocabulary: standardized: 制定标准

**[4105.84s] English:** It wasn't quite that concise.  
**Translation:** 

**[4106.98s] English:** But you find now with the modern standards that we were working on in the HTML5 sort of effort, that things became simpler.  
**Translation:** Vocabulary: concise: 简洁明了

**[4115.86s] English:** The Fetch API and the Query Selector API, Document.QuerySelector, a lot of things can be done now in raw JavaScript that you would make more concise and terse in jQuery.  
**Translation:** 

**[4126.50s] English:** But it's not bad.  
**Translation:** Vocabulary: terse: 简洁明了

**[4128.02s] English:** It's pretty good.  
**Translation:** 

**[4128.76s] English:** Whereas in the old DOM of 15 years ago, it was just too verbose.  
**Translation:** 

**[4131.92s] English:** So maybe the frameworks were born kind of because JavaScript lagged.  
**Translation:** 

**[4137.16s] English:** Some of the features of jQuery.  
**Translation:** Vocabulary: lagged: 滞后

**[4139.24s] English:** And so like now that JavaScript is swallowing what jQuery was, then the frameworks will only the ones that truly add value will stick around and the other ones will die out.  
**Translation:** 

**[4148.94s] English:** And that highlights also this division between the core language JavaScript, which can show up in other places like Node.js on the server side, and the browser-specific APIs or the document object model APIs, which are even managed by the W3C, the standards body that was off in XML La La Land when we were doing real JavaScript standards in ECMA.  
**Translation:** 

**[4166.98s] English:** And you have this division of labor, division of responsibility, and division of style and sort of aesthetics, and also speed.  
**Translation:** 

**[4177.14s] English:** So the document object model really stagnated after Microsoft kind of de-invested in the web.  
**Translation:** Vocabulary: aesthetics: 审美; stagnated: 停滞

**[4183.58s] English:** And Microsoft did something in their haste in the spirit of Netscape, doing things quickly and getting on first, called DHTML.  
**Translation:** 

**[4189.78s] English:** And some of their innovations that were like an alternative document object model didn't really get standardized until HTML5.  
**Translation:** Vocabulary: innovations: 创新

**[4196.30s] English:** DHTML5.  
**Translation:** 

**[4196.78s] English:** DHTML5.  
**Translation:** 

**[4196.84s] English:** DHTML5.  
**Translation:** 

**[4196.96s] English:** DHTML5.  
**Translation:** 

**[4196.98s] English:** And we pragmatists at Opera at the time...  
**Translation:** 

**[4200.00s] English:** Ian Hickson, who went to Google, Apple, and Mozilla said,  
**Translation:** Vocabulary: pragmatists: 实用主义者

**[4203.94s] English:** XML is not going to replace HTML.  
**Translation:** 

**[4207.14s] English:** HTML4 is too old.  
**Translation:** 

**[4208.68s] English:** Let's standardize HTML5 based on all this good stuff,  
**Translation:** 

**[4212.14s] English:** including that DHTML variant, dynamic HTML.  
**Translation:** Vocabulary: standardize: 制定标准

**[4215.04s] English:** HTML5, it feels like to me, maybe you can correct me,  
**Translation:** 

**[4218.14s] English:** like a beautiful piece of design work.  
**Translation:** 

**[4221.78s] English:** It's not often with web stuff you have this breath of just like,  
**Translation:** 

**[4227.36s] English:** oh, whoever did this.  
**Translation:** 

**[4228.60s] English:** It just feels good.  
**Translation:** 

**[4231.86s] English:** What are your thoughts about HTML?  
**Translation:** 

**[4233.92s] English:** Am I being too romantic?  
**Translation:** 

**[4236.12s] English:** A little bit.  
**Translation:** 

**[4236.76s] English:** Are there flaws, fundamental flaws to it that I'm just not aware of?  
**Translation:** 

**[4240.70s] English:** My old friend Hicksy did a great job.  
**Translation:** 

**[4242.54s] English:** He was another renegade physics student,  
**Translation:** 

**[4245.64s] English:** and he was basically a QA guy at Opera,  
**Translation:** Vocabulary: renegade: 叛逆者

**[4247.98s] English:** but he obviously trained physics student and someone who could write,  
**Translation:** 

**[4254.18s] English:** a Britisher.  
**Translation:** 

**[4254.62s] English:** He developed test suites,  
**Translation:** 

**[4257.86s] English:** and he started thinking,  
**Translation:** 

**[4258.66s] English:** about them more axiomatically.  
**Translation:** 

**[4260.90s] English:** Now this can be good because you can sort of systematize in a way that makes a better HTML,  
**Translation:** Vocabulary: axiomatically: 公理般地

**[4266.02s] English:** or you can get caught in the pragmatism of saying,  
**Translation:** 

**[4268.08s] English:** well, we have to handle all of these edge cases.  
**Translation:** Vocabulary: pragmatism: 实用主义

**[4269.82s] English:** So we're just going to have sort of a test matrix.  
**Translation:** 

**[4272.56s] English:** And if the matrix is large,  
**Translation:** Vocabulary: matrix: 矩阵

**[4273.98s] English:** it will not be beautiful by many people's lights.  
**Translation:** 

**[4275.84s] English:** Everyone likes to minimize along their preferred dimensions,  
**Translation:** Vocabulary: dimensions: 标准

**[4279.30s] English:** the seven special forms and scheme or whatever.  
**Translation:** 

**[4281.62s] English:** But reality is HTML needs to be big.  
**Translation:** 

**[4287.12s] English:** It's kind of shambolic.  
**Translation:** 

**[4288.08s] English:** It's,  
**Translation:** Vocabulary: shambolic: 乱七八糟

**[4288.60s] English:** a creative multi-paradigm and Hicksy did a good job.  
**Translation:** 

**[4291.78s] English:** I would say with a bunch of it.  
**Translation:** 

**[4294.36s] English:** Other people came in,  
**Translation:** 

**[4295.38s] English:** in the spirit of Ian Hickson to do HTML5 work and they've carried on that effort.  
**Translation:** 

**[4300.24s] English:** And it's a,  
**Translation:** 

**[4300.90s] English:** so it's a mix of pragmatism,  
**Translation:** 

**[4302.76s] English:** de facto standards from the past being sort of combined or written down for the first time,  
**Translation:** 

**[4307.56s] English:** and then rethought in a way that has a simpler syntax,  
**Translation:** Vocabulary: facto: 实际上; syntax: 语法

**[4310.26s] English:** like the fetch API instead of XMLHttpRequest.  
**Translation:** 

**[4314.10s] English:** This video too,  
**Translation:** 

**[4314.98s] English:** as well.  
**Translation:** 

**[4315.38s] English:** It ultimately,  
**Translation:** 

**[4316.52s] English:** it feels like maybe you can correct me.  
**Translation:** 

**[4318.06s] English:** It feels like it was the nail in the coffin.  
**Translation:** 

**[4320.00s] English:** in a flash steve jobs saying no flash on the iphone in my opinion was the actual state to the  
**Translation:** 

**[4325.18s] English:** heart but but well i'm not sure what trope you want to use this flash was a zombie for until  
**Translation:** Vocabulary: trope: 陈词滥调; zombie: 僵尸

**[4331.12s] English:** just this year right or last year i think last year was the end of flash in main browsers um  
**Translation:** 

**[4335.78s] English:** but jobs really did the death blow and uh yeah you're right we had to make html5 competitive  
**Translation:** Vocabulary: browsers: 浏览器

**[4342.50s] English:** i still don't think we got that beautiful timeline animation the timeline thing so you like the time  
**Translation:** 

**[4348.36s] English:** i mean me from uh you know i used to animate all kinds of stuff inside flash plus there's a  
**Translation:** 

**[4353.36s] English:** programming element yes it was a little bit i don't know if you can comment on that but to me  
**Translation:** 

**[4358.80s] English:** it was a little bit like go-to statement like in a sense that there's a little bit too chaotic  
**Translation:** 

**[4363.96s] English:** like it didn't uh that ocd part of me as a programmer wasn't satisfied by flash it feels  
**Translation:** 

**[4370.52s] English:** like there was bugs that were introduced through the animation process that i couldn't debug easily  
**Translation:** 

**[4375.28s] English:** yes i heard that too i i didn't use it so i'm  
**Translation:** 

**[4377.68s] English:** doing the  
**Translation:** 

**[4378.36s] English:** grass is greener thing here yeah the thing i like i liked about the animation model was that it was  
**Translation:** 

**[4382.62s] English:** this immutable function of time so you could time warp and you could if you dodge these bugs or  
**Translation:** Vocabulary: dodge: 躲避; immutable: 不可变的

**[4387.42s] English:** worked carefully you could really make it sing in ways that i think still a little challenging with  
**Translation:** 

**[4391.88s] English:** web uh animation standards but uh or just using raw canvas and webgl um but there's so many tools  
**Translation:** 

**[4399.00s] English:** now that maybe it doesn't matter and and yet we had to you know do video we had to do uh webgl and  
**Translation:** 

**[4405.82s] English:** then evolve it um we had to do webgl and then evolve it and then we had to do webgl and then  
**Translation:** 

**[4408.36s] English:** use audio um but once we did all these things that helped flash uh die thanks to steve gubb's  
**Translation:** 

**[4415.16s] English:** we had something that um people didn't realize we had that vision that mark anderson had this  
**Translation:** 

**[4421.42s] English:** this graphics cable bowl to the metal uh portable runtime and we at mozilla realized this and we  
**Translation:** 

**[4429.64s] English:** we saw javascript was something that you could compile to adobe had somebody in the adobe labs  
**Translation:** Vocabulary: runtime: 运行时环境

**[4435.00s] English:** doing this too he had a project called alchemy we had somebody who's now going to be doing this so  
**Translation:** 

**[4438.20s] English:** we had to do something that was something that was a little bit different than the ark allein project  
**Translation:** Vocabulary: alchemy: 炼金术

**[4438.28s] English:** and that's something that we had to do at the end and i think that that's something that we had to do  
**Translation:** 

**[4438.30s] English:** sort of do a lot in the middle a lot in the middle of early july we had to get the addition to the  
**Translation:** 

**[4438.36s] English:** Google.  
**Translation:** 

**[4440.00s] English:** own zakai who did his own llvm based compiler that would take c or c plus plus and it would  
**Translation:** 

**[4445.26s] English:** emit javascript and you would think this is crazy you're going from this sort of machine types low  
**Translation:** 

**[4450.00s] English:** level you know controlled memory allocation language to this garbage collected dynamically  
**Translation:** Vocabulary: allocation: 内存分配; dynamically: 动态地

**[4455.10s] English:** typed uh high level higher level language but alone sort of just phenomenologically carved  
**Translation:** 

**[4461.92s] English:** nature of the joint and found the forms that were fast in javascript and then with dave herman who  
**Translation:** Vocabulary: phenomenologically: 现象地

**[4467.56s] English:** i'd recruited from northeastern university who was a type theorist and um luke wagner who's still  
**Translation:** 

**[4473.00s] English:** at mozilla who was the compiler guy and the jet guy they figured out how to codify what i wanted  
**Translation:** Vocabulary: recruited: 招聘; theorist: 理论家

**[4479.74s] English:** done into a typed subset of javascript called asm js and this is a strange thing to think about  
**Translation:** 

**[4485.62s] English:** because it doesn't have new syntax the types are casts that occur in dominator positions in the  
**Translation:** Vocabulary: dominator: 支配者; syntax: 语法规则

**[4492.90s] English:** control flow graph so it's like a hack on javascript and it's a subset and it uses those  
**Translation:** 

**[4497.38s] English:** bit  
**Translation:** 

**[4497.54s] English:** operators that i talked about copying from java to basically cast numeric types which are double  
**Translation:** 

**[4505.10s] English:** precision flowing point into integers and so inside javascript in the kernel semantics are  
**Translation:** Vocabulary: integers: 整数; kernel: 内核; numeric: 数值; semantics: 语义

**[4510.78s] English:** integers and if you use these operators if a compiler emits them in the right places  
**Translation:** 

**[4514.88s] English:** you can then treat them as typed values typed memory locations and you can type check your  
**Translation:** Vocabulary: emits: 生成

**[4521.50s] English:** program you can not only type check it you can compile it this is all in sort of linear time oh  
**Translation:** 

**[4526.56s] English:** and  
**Translation:** 

**[4526.76s] English:** you can compile it to have deterministic performance it doesn't touch the garbage  
**Translation:** 

**[4531.40s] English:** collector it calls a bunch of functions that come from the c functions or c++ code that you're  
**Translation:** Vocabulary: collector: 垃圾回收; deterministic: 确定性

**[4536.54s] English:** compiling and you can make the epic unreal engine go in 30 frames a second yeah and when we did this  
**Translation:** 

**[4544.64s] English:** in 2013 in the fall you know tim sweeney i'm at um didn't think it could be done quickly i thought  
**Translation:** Vocabulary: compiling: 编译

**[4550.24s] English:** it would take years and the team went to raleigh to epic and in four days they had unreal engine  
**Translation:** 

**[4556.76s] English:** ported by pressing a compile button right they had to but  
**Translation:** Vocabulary: raleigh: 罗利

**[4560.00s] English:** They had to have WebGL, which came from OpenGL, ES, which came from OpenGL, which came from Silicon Graphics GL.  
**Translation:** 

**[4565.92s] English:** They had to have WebAudio, so they could map OpenAL, which was another audio library standard, to WebAudio, which was kind of a Chrome idiosyncratic thing.  
**Translation:** Vocabulary: idiosyncratic: 特有特性

**[4574.58s] English:** But they could make it work.  
**Translation:** 

**[4576.34s] English:** And they had to have Asm.js for fast C++ to JavaScript.  
**Translation:** 

**[4581.16s] English:** And if you didn't have that fast compiler step, the JavaScript you'd write by hand trying to do an Unreal game would be too big and too slow.  
**Translation:** 

**[4589.70s] English:** It would touch the garbage collector.  
**Translation:** 

**[4591.40s] English:** It would not keep up with 30 frames a second on the hardware, 2013 hardware.  
**Translation:** 

**[4595.62s] English:** So we demoed that at – this must have been fall 2012 now that I think about it.  
**Translation:** 

**[4600.40s] English:** Because we demoed it at GDC, Game Developer Conference 2013, and people were stunned.  
**Translation:** 

**[4605.42s] English:** It's like Unreal Engine, Unreal Tournament running in my browser window.  
**Translation:** 

**[4608.86s] English:** No plugin, no Flash, no Java, no –  
**Translation:** 

**[4619.70s] English:** Like C++.  
**Translation:** 

**[4621.40s] English:** Yeah.  
**Translation:** 

**[4621.82s] English:** And even before then, you had the fast JavaScript VMs in 2008 when Chrome came out.  
**Translation:** 

**[4626.18s] English:** Just before it came out, Mozilla, my friend Andreas Gall and I and others hacked out TraceMonkey, our trace-based JIT.  
**Translation:** 

**[4634.48s] English:** The Squirrel Fish Extreme team at Apple did their JIT.  
**Translation:** Vocabulary: hacked: 编写; squirrel: 火狐

**[4638.60s] English:** And we were all competing on these crazy performance benchmarks.  
**Translation:** 

**[4641.84s] English:** It was a little bit too much tuning of the benchmark.  
**Translation:** Vocabulary: benchmark: 性能基准; benchmarks: 性能基准

**[4643.60s] English:** But JavaScript started getting fast, and developers started noticing it.  
**Translation:** 

**[4646.66s] English:** But it was still kind of its own high-level language.  
**Translation:** 

**[4649.70s] English:** It was garbage collection.  
**Translation:** 

**[4650.40s] English:** The Asm.js step helped us go further because until we really proved the concept, people were still saying, well, JavaScript's okay.  
**Translation:** 

**[4659.36s] English:** It's getting faster thanks to V8.  
**Translation:** 

**[4661.00s] English:** Everybody gave Google credit, especially Google.  
**Translation:** 

**[4663.24s] English:** But we need something to kill Flash.  
**Translation:** 

**[4664.90s] English:** Let's use the portable native client code that Google had acquired, native client, which is a separate lineage for taking basically C code, compiling it into a software fault-isolated container of some sort using some kind of virtualization technique.  
**Translation:** Vocabulary: compiling: 编译; lineage: 分支; virtualization: 虚拟化

**[4679.70s] English:** And we were able to do it, and we were able to do it, and we were able to do it.  
**Translation:** 

**[4680.00s] English:** Maybe it can even be in process and still be memory safe.  
**Translation:** 

**[4682.54s] English:** That would be awesome.  
**Translation:** 

**[4683.06s] English:** But they ended up using process isolation too.  
**Translation:** 

**[4684.84s] English:** And that kind of weakened it.  
**Translation:** 

**[4686.54s] English:** And in the end, it was like portable native client.  
**Translation:** Vocabulary: weakened: 削弱了

**[4688.60s] English:** Okay, you know, meet the new boss.  
**Translation:** 

**[4690.48s] English:** Same as the old boss.  
**Translation:** 

**[4691.02s] English:** This is the Google Flash, right?  
**Translation:** 

**[4693.04s] English:** But when we did Asm.js and we showed Unreal Engine working, I think it was only a matter of time before Google threw in the towel.  
**Translation:** 

**[4699.80s] English:** And in fact, everybody agreed in spring of 2015, we're going to take what was proven by Asm.js and make a new syntax, a binary syntax.  
**Translation:** 

**[4707.90s] English:** It's efficient that loads into the same JavaScript VM that JavaScript loads into.  
**Translation:** Vocabulary: binary: 二进制; syntax: 语法

**[4712.70s] English:** So there'll be two source languages, one VM, very important, one garbage collector, one memory manager, one set of compiler stages.  
**Translation:** 

**[4720.48s] English:** And that's called WebAssembly.  
**Translation:** Vocabulary: collector: 垃圾回收器

**[4722.16s] English:** And that's the successor to Asm.js.  
**Translation:** 

**[4724.32s] English:** And it's important that it have binary syntax because at the end of the day, especially on mobile, if you're downloading JavaScript, even if you're using LZ compression on the wire, that's cool.  
**Translation:** Vocabulary: compression: 压缩

**[4732.38s] English:** But you've got to blow it out into memory and then parse the silly eight character function keyword that I picked.  
**Translation:** 

**[4737.90s] English:** And when I should have used something shorter, I picked it because of awk, the Unix tool.  
**Translation:** Vocabulary: keyword: 功能关键字; parse: 解析

**[4744.22s] English:** So anyways, I'm not following.  
**Translation:** 

**[4745.70s] English:** I want to, but I'm not following the awk thread.  
**Translation:** 

**[4748.18s] English:** Yeah, don't worry about it.  
**Translation:** 

**[4749.48s] English:** Is it surprising to you that how damn fast JavaScript is these days?  
**Translation:** 

**[4754.70s] English:** I mean, like, you've been through the whole journey.  
**Translation:** 

**[4756.76s] English:** I know every step of the way, but is it like, I mean, it feels incredible.  
**Translation:** 

**[4762.16s] English:** It does.  
**Translation:** 

**[4762.44s] English:** So the funny thing is, computer science is this big karmic wheel, right?  
**Translation:** Vocabulary: karmic: 因果的

**[4766.76s] English:** Wheel of Fortuna.  
**Translation:** 

**[4767.90s] English:** And in the 97, I was loaned by Netscape to do due diligence for Sun in their acquisition of Anamorphic, which was David Unger and friends, people, Craig, I'm forgetting his name.  
**Translation:** Vocabulary: anamorphic: 变形的; fortuna: 命运; netscape: 网景; unger: 乌nger

**[4786.18s] English:** He went to Microsoft.  
**Translation:** 

**[4787.38s] English:** These Stanford language buffs who had taken Smalltalk and then David created Self as a simpler sort of Smalltalk language and made really fast.  
**Translation:** Vocabulary: buffs: 狂热爱好者; smalltalk: 聊天; stanford: 斯坦福

**[4797.90s] English:** Just in time compiling VMs for them.  
**Translation:** 

**[4800.00s] English:** them and they you know well ahead of java hotspot or javascript v8 or any of these modern vms  
**Translation:** Vocabulary: compiling: 编译

**[4807.02s] English:** figured out how to make dynamic code fast because small talk is dynamic language right it has  
**Translation:** 

**[4813.22s] English:** classes it has i think more lockdown declarative syntax than javascript but it's fundamentally  
**Translation:** Vocabulary: declarative: 声明式的; fundamentally: 本质上

**[4817.96s] English:** dynamic you don't declare the types um but you could infer the types as the program runs and  
**Translation:** 

**[4824.22s] English:** you start to form these ideas about what types are actually flowing through key operations and  
**Translation:** 

**[4829.14s] English:** you form little so-called polymorphic inline caches that are optimized machine code the cache  
**Translation:** 

**[4836.02s] English:** is the machine code that assumes it does a quick check to make sure the type is right and if it's  
**Translation:** Vocabulary: cache: 缓存; caches: 缓存; inline: 内联; optimized: 优化; polymorphic: 多态

**[4840.52s] English:** not right it bails to the interpreter and if it is right you go pretty fast and that short test  
**Translation:** 

**[4845.82s] English:** is a predicted branch so things are things are pretty quick all that amazing stuff i knew about  
**Translation:** Vocabulary: bails: 放弃; interpreter: 解释者

**[4850.70s] English:** in the 90s and i i didn't have time to do it and anamorphic got bought by sun and they did hotspot  
**Translation:** 

**[4857.06s] English:** and you needed that even in java  
**Translation:** 

**[4858.96s] English:** because  
**Translation:** 

**[4859.14s] English:** at scale java has some dynamic aspects due to invoke interface you can have basically  
**Translation:** Vocabulary: interface: 接口

**[4865.14s] English:** collections of java code where you don't know at at the time each each module or package is compiled  
**Translation:** 

**[4871.92s] English:** exactly what's being called what what subclass or what implementation of an interface is being  
**Translation:** Vocabulary: compiled: 编译; implementation: 实现; module: 模块

**[4877.08s] English:** called and so you want to optimize using this sort of dynamic polymorphic caching there too  
**Translation:** 

**[4881.50s] English:** and they did that in hotspot it's amazing amazing beast i've met like 13 people who all claim they  
**Translation:** Vocabulary: caching: 缓存; optimize: 优化

**[4886.26s] English:** created it i think i think one of them maybe  
**Translation:** 

**[4888.96s] English:** deserve credit more than others um but uh i didn't get to do that in javascript and when we knew that  
**Translation:** 

**[4896.20s] English:** that google uh was going to do their own browser which we knew at mozilla around 2006 um i also  
**Translation:** 

**[4902.74s] English:** met the team that did v8 and it turns out it was lars bach who was one of the young engineers from  
**Translation:** 

**[4907.86s] English:** anamorphic who got acquired by sun and so lars is like the one of the world's expert on these kinds  
**Translation:** 

**[4913.42s] English:** of virtual machines and he picked my brains about javascript i could tell he didn't like it at the  
**Translation:** 

**[4917.76s] English:** time but he had the time to do it and he was like i'm gonna do that and he did that and he did that  
**Translation:** 

**[4918.80s] English:** one day he had to do it for the first time and not give it to me because he just didn't know what he was doing  
**Translation:** 

**[4918.82s] English:** he had to do it for the first time and for the first time and he didn't know what he was doing  
**Translation:** 

**[4918.96s] English:** do it.  
**Translation:** 

**[4920.00s] English:** Oh, really? Interesting.  
**Translation:** 

**[4921.36s] English:** Yeah, in 2006, lunch at Google's campus.  
**Translation:** 

**[4923.88s] English:** And then I had another friend who was DevRel at Chrome,  
**Translation:** 

**[4926.94s] English:** and he said, yeah, we don't know what they're doing.  
**Translation:** 

**[4928.28s] English:** This is getting 2007 to fall, getting toward 2008.  
**Translation:** 

**[4931.76s] English:** We're trying to get Chrome out,  
**Translation:** 

**[4932.96s] English:** and we don't know what's going on with the V8 team.  
**Translation:** 

**[4934.50s] English:** They're off in Aarhus, Denmark,  
**Translation:** Vocabulary: aarhus: 阿arhus

**[4936.42s] English:** rewriting their engine four times, which is good.  
**Translation:** 

**[4939.24s] English:** That's the right way to do this kind of development.  
**Translation:** Vocabulary: rewriting: 重新编写

**[4942.02s] English:** They were learning JavaScript, including all its quirks,  
**Translation:** 

**[4944.20s] English:** which they came to hate, the fire of a thousand suns,  
**Translation:** Vocabulary: quirks: 怪异之处

**[4946.92s] English:** which is one of the reasons that Lars and company did Dart,  
**Translation:** 

**[4949.42s] English:** their own language, but they also made the language fast.  
**Translation:** 

**[4952.98s] English:** And meanwhile, we knew this was happening,  
**Translation:** 

**[4955.10s] English:** so we got our act together with TraceMonkey,  
**Translation:** 

**[4958.46s] English:** our tracing JIT at Mozilla, and Apple, I think, was also aware,  
**Translation:** 

**[4961.88s] English:** and so they were doing their own JIT.  
**Translation:** 

**[4962.96s] English:** So the era of JITed fast JavaScript in 2008  
**Translation:** 

**[4965.90s] English:** had this prehistory going back to Smalltalk itself and Anamorphic.  
**Translation:** Vocabulary: anamorphic: 变形的; prehistory: 前历史; smalltalk: 小talk

**[4971.04s] English:** And again, the lineage is interesting  
**Translation:** 

**[4972.98s] English:** because you had Lars at Anamorphic,  
**Translation:** Vocabulary: lineage: 血统

**[4974.44s] English:** and then he ends up at Google.  
**Translation:** 

**[4975.64s] English:** Yeah, and today we have an incredibly fast language  
**Translation:** 

**[4979.42s] English:** that, like you said, still, you know, without hate,  
**Translation:** 

**[4983.70s] English:** you can't have love.  
**Translation:** 

**[4984.92s] English:** So I think there's both love and hate for this dance,  
**Translation:** 

**[4989.34s] English:** this rich, complex dance of JavaScript throughout its history.  
**Translation:** 

**[4992.88s] English:** There's a dialectic, for sure.  
**Translation:** 

**[4995.06s] English:** Today, JavaScript is the most popular language in the world.  
**Translation:** Vocabulary: dialectic: 辩证法

**[5000.10s] English:** Why? By many measures.  
**Translation:** 

**[5002.92s] English:** Why do you think that is?  
**Translation:** 

**[5004.66s] English:** Is there some fundamental ideas  
**Translation:** 

**[5007.42s] English:** that you've already spoken about?  
**Translation:** 

**[5009.42s] English:** A little bit, but sort of broader  
**Translation:** 

**[5010.62s] English:** that you think is the most popular language in the world?  
**Translation:** 

**[5012.80s] English:** So I think I did, you know, by doing first-class functions  
**Translation:** 

**[5015.96s] English:** and taking the good parts of the C operator hierarchy  
**Translation:** Vocabulary: hierarchy: 等级体系

**[5020.60s] English:** and just keeping things simple enough,  
**Translation:** 

**[5024.04s] English:** maybe it could have been simpler,  
**Translation:** 

**[5025.12s] English:** but I had to make it look like Java  
**Translation:** 

**[5027.24s] English:** and interoperate with Java,  
**Translation:** Vocabulary: interoperate: 互相操作

**[5028.82s] English:** that there was, you know, inherent goodness,  
**Translation:** 

**[5032.74s] English:** Aristotelian quality there.  
**Translation:** Vocabulary: aristotelian: 亚里士多德的

**[5034.28s] English:** And people perceive that even through all the quirks and warts.  
**Translation:** 

**[5037.78s] English:** And then over time, working on it with the standards,  
**Translation:** Vocabulary: perceive: 感知; warts: 缺点

**[5039.42s] English:** the standards body,  
**Translation:** 

**[5040.00s] English:** Working on it, not only as a core language, but in the context of HTML5 and making the browser better.  
**Translation:** 

**[5046.64s] English:** Listening to the developers, thinking about, this is something that Nick Thompson wrote nicely about on the Hacker News.  
**Translation:** 

**[5052.02s] English:** I was very flattered.  
**Translation:** Vocabulary: flattered: 受宠若惊; hacker: 黑客

**[5052.58s] English:** He said, Java was this thing where the experts were writing the code and it was compiled and you had to declare all your types.  
**Translation:** 

**[5057.88s] English:** And Sun didn't really give a damn about the average programmer who wanted to build real web apps, dynamic things.  
**Translation:** Vocabulary: compiled: 编译; programmer: 程序员

**[5064.40s] English:** And I was in there, meanwhile, doing a bunch of people's jobs, making JavaScript survive those early years when it was kind of touch and go, right?  
**Translation:** 

**[5073.54s] English:** JavaScript was considered Mickey Mouse language.  
**Translation:** Vocabulary: mickey: 米老鼠

**[5076.12s] English:** It was for annoyances like the scrolling text at the bottom of the browser in the status bar.  
**Translation:** 

**[5080.66s] English:** But I kept listening to developers, working with them and trying to make it run in that single threaded event loop in a useful way.  
**Translation:** Vocabulary: annoyances: 烦人事情; scrolling: 滚动文本; threaded: 线程模式

**[5087.70s] English:** And I think that forged something that people have come to love.  
**Translation:** 

**[5091.16s] English:** Now, you don't always love the best thing, right?  
**Translation:** 

**[5093.64s] English:** I talked about.  
**Translation:** 

**[5094.40s] English:** I talked about Shakespeare sonnet about my mistress eyes are nothing like the sun or the scene from Josh Whedon's film Serenity at the end where the actual piece in the score by David Newman is called Love, where Captain Mal is teaching River Tam about how to pilot the ship.  
**Translation:** Vocabulary: mistress: 女主人; serenity: 宁静

**[5113.84s] English:** And she's a super genius, super soldier.  
**Translation:** 

**[5115.36s] English:** She knows how to do it already.  
**Translation:** 

**[5116.94s] English:** And he's basically talking about how you have to love the ship, because if you don't, it's going to kill you.  
**Translation:** 

**[5121.74s] English:** And then the piece falls off the ship.  
**Translation:** 

**[5123.54s] English:** It's kind of like Java.  
**Translation:** 

**[5124.52s] English:** Script.  
**Translation:** 

**[5125.82s] English:** You have to love it.  
**Translation:** 

**[5126.72s] English:** You have to love it because now people say we're stuck with it because it got this priority of place.  
**Translation:** 

**[5131.56s] English:** But there's love underpinning that.  
**Translation:** 

**[5133.54s] English:** And actually, the listening to developers, that's kind of beautiful.  
**Translation:** Vocabulary: underpinning: 支撑

**[5136.72s] English:** There's most successful products in this world with all the messes, with all the flaws.  
**Translation:** 

**[5143.08s] English:** Perhaps the flaws themselves are actual features, but that's a whole nother.  
**Translation:** Vocabulary: nother: 另一个

**[5146.62s] English:** That's a discussion about love.  
**Translation:** 

**[5148.34s] English:** But underneath it, there's something that just connects with people and has to keep connecting.  
**Translation:** 

**[5153.36s] English:** If JavaScript.  
**Translation:** 

**[5154.40s] English:** Kind of went off in this.  
**Translation:** 

**[5155.70s] English:** People sometimes complain about ES6.  
**Translation:** 

**[5157.26s] English:** Oh, you put classes in JavaScript.  
**Translation:** 

**[5158.68s] English:** I hate classes.  
**Translation:** 

**[5159.42s] English:** You know, you've ruined it.  
**Translation:** 

**[5160.00s] English:** But it's it's not true. It's a dynamic language. Smalltalk had classes. Python has classes.  
**Translation:** 

**[5166.80s] English:** There are lots of Lisp variants that have classy systems, common Lisp.  
**Translation:** Vocabulary: classy: 优雅的; smalltalk: 聊天

**[5172.38s] English:** So, you know, people who don't reject it based on some sort of fashion judgment do use it and do interact with the standards body.  
**Translation:** 

**[5183.18s] English:** The standards body is competing browser vendors mainly, but also now big companies that use JavaScript heavily, the PayPals and other such companies, Salesforce.  
**Translation:** Vocabulary: salesforce: 销售力

**[5193.04s] English:** And they have to cater to web developers.  
**Translation:** 

**[5196.26s] English:** They have to hire developers who know JavaScript.  
**Translation:** 

**[5199.00s] English:** They have to keep their engines up to the latest standard.  
**Translation:** 

**[5203.06s] English:** And this creates all this sort of social structure around JavaScript that is unusual.  
**Translation:** 

**[5207.64s] English:** I mean, you get C++ buffs that follow the inner workings of, you know, C++.  
**Translation:** 

**[5213.18s] English:** And what is it now? Twenty one something.  
**Translation:** Vocabulary: buffs: 狂热爱好者; workings: 运作原理

**[5215.68s] English:** I don't know. I've lost track.  
**Translation:** 

**[5217.48s] English:** But it's a more rarefied group.  
**Translation:** 

**[5218.98s] English:** It's more like the old language, you know, gray hairs, whereas JavaScript is a younger and more vibrant, large crowd.  
**Translation:** 

**[5227.56s] English:** There's a community feel to it.  
**Translation:** Vocabulary: vibrant: 充满活力的

**[5229.18s] English:** There's echoes.  
**Translation:** 

**[5230.34s] English:** Perhaps I don't want to draw too many similarities.  
**Translation:** 

**[5233.96s] English:** Maybe you can comment on it.  
**Translation:** 

**[5235.20s] English:** There's a C++ is like Wall Street and JavaScript is like Wall Street bets from the recent events.  
**Translation:** 

**[5242.36s] English:** It's like.  
**Translation:** 

**[5243.18s] English:** There's a chaotic community of all.  
**Translation:** 

**[5244.94s] English:** And there's some power from that distributed crowd of people that it's more demotic.  
**Translation:** 

**[5251.30s] English:** It's more of the people.  
**Translation:** Vocabulary: demotic: 平民的

**[5252.62s] English:** It lets people in without requiring these credentials.  
**Translation:** 

**[5256.10s] English:** I remember in the late 90s into the noughties, people were all getting Java credentials.  
**Translation:** Vocabulary: credentials: 资格证明; noughties: 零十年代

**[5260.14s] English:** And I knew people and friends, new people who became Java programmers.  
**Translation:** 

**[5264.14s] English:** And you knew they really should have been like nature guides or pilots.  
**Translation:** Vocabulary: programmers: 程序员

**[5267.38s] English:** They hated programming, but they thought, I got to make money.  
**Translation:** 

**[5269.94s] English:** I'm going to become a Java programmer.  
**Translation:** Vocabulary: programmer: 程序员

**[5271.68s] English:** Do you have some?  
**Translation:** 

**[5272.78s] English:** Because it's such a monumental moment in our current history.  
**Translation:** 

**[5276.00s] English:** As a quick aside, do you have thoughts about this?  
**Translation:** 

**[5280.00s] English:** huge distributed crowdsourced financial happenings uh with wall street bets that's like nobody could  
**Translation:** Vocabulary: crowdsourced: 众包

**[5287.74s] English:** have well you could have predicted but the scale and the impact of this kind of emergent behavior  
**Translation:** 

**[5293.04s] English:** from independent parties that could happen like i said my own um experience with the dismal science  
**Translation:** 

**[5299.18s] English:** uh as with physics led me to reject a lot of bad models and you know economics was always  
**Translation:** 

**[5304.32s] English:** compromised by politics but political economy um you could also argue that it was it used to be a  
**Translation:** Vocabulary: compromised: 妥协

**[5309.92s] English:** branch of moral philosophy so it was concerned with the good and it became divorced and became  
**Translation:** 

**[5314.30s] English:** sort of in this quasi-newtonian way just about everything's just running by itself don't worry  
**Translation:** 

**[5319.46s] English:** about it you know this monopoly is crushing your netscape company but that's just nature  
**Translation:** 

**[5323.02s] English:** and economics couldn't or doesn't really have good models for the wall street bets subreddit  
**Translation:** Vocabulary: monopoly: 市场垄断; netscape: 网景; subreddit: 子版块

**[5328.78s] English:** you know they they know how to squeeze a short right so um the amazing thing is you have um  
**Translation:** 

**[5335.80s] English:** robin hood app which was again supposedly for the demos for the  
**Translation:** Vocabulary: demos: 演示

**[5339.92s] English:** people yeah and eliminated the fee through various kinds of um you know straddles or some  
**Translation:** 

**[5346.66s] English:** kind of um spread operation that helped them eliminate the fee or eat the fee and in fact  
**Translation:** Vocabulary: straddles: 跨式操作

**[5352.34s] English:** you know as a broker in these days because it takes two days to settle there's counterparty  
**Translation:** 

**[5356.54s] English:** risk as as they found out and um so the wall street bets uh people you know the the memes  
**Translation:** Vocabulary: counterparty: 交易对方

**[5363.98s] English:** are like the terminator robot with the six hundred dollar stimmy check and then the hedge  
**Translation:** 

**[5369.92s] English:** funds the the little girl hiding under the desk um there there is a problem which i talked about  
**Translation:** Vocabulary: terminator: 终结者

**[5375.92s] English:** in the recent podcast which i'm conscious of from the history of the web and that is you could say  
**Translation:** 

**[5380.32s] English:** it's monopoly which antitrust wasn't enforced after usb microsoft for a long time and um a lot  
**Translation:** Vocabulary: antitrust: 反垄断; enforced: 执行

**[5386.34s] English:** of this was due to the money interests buying control of politicians and you know in plato's  
**Translation:** 

**[5392.80s] English:** five regimes that's oligarchy that's that's that's where we are and now we're seeing a fight  
**Translation:** 

**[5398.00s] English:** against the oligarchs i don't know if it'll work but you're doing it you're doing it you're doing it  
**Translation:** 

**[5399.92s] English:** down  
**Translation:** 

**[5400.00s] English:** seeing it and it's also kind of hackerish right it's got a hacker ethos you know hey robin hood  
**Translation:** 

**[5404.88s] English:** no fees oh interesting hey you know um i could buy a fraction of a share in this thing or i can  
**Translation:** Vocabulary: ethos: 精神; hacker: 黑客; hackerish: 黑客风格

**[5409.82s] English:** keep buying with my stimulus check so uh i mentioned hegel seeing napoleon on the horse  
**Translation:** 

**[5416.36s] English:** hegel also talked about the the cunning of reason that you have the sort of you know god sees history  
**Translation:** Vocabulary: cunning: 诡计; napoleon: 拿破仑; stimulus: 刺激

**[5422.10s] English:** in full and if you believe in god or you know we don't know the future but there's always this sort  
**Translation:** 

**[5427.40s] English:** of fly in the ointment this uh unintended consequence uh that confounds the best um plans  
**Translation:** Vocabulary: confounds: 使困惑; ointment: 膏霜; unintended: 未预见的

**[5433.54s] English:** of the powers that be and we're living through it that's i'm glad it's not you know street warfare  
**Translation:** 

**[5439.38s] English:** or or mechanized warfare because it has been in the past um uh it's it's more like soft power  
**Translation:** 

**[5446.36s] English:** yes and uh people are fighting back do you think it's possible so the javascript used to be uh for  
**Translation:** 

**[5454.96s] English:** the front end of the web it's  
**Translation:** 

**[5457.40s] English:** now increasingly so being used for back end like running stuff that's like behind the scenes  
**Translation:** 

**[5465.32s] English:** and it's also starting to be used uh quite a bit for things like tensorflow js so starting to  
**Translation:** 

**[5472.86s] English:** actually use like these heavy duty applications that are using neural networks machine learning  
**Translation:** 

**[5477.62s] English:** and so on in the browser is it possible in 10 20 30 years that basically most of the world runs on  
**Translation:** Vocabulary: neural: 神经网络

**[5487.06s] English:** javascript  
**Translation:** 

**[5487.40s] English:** this is a dystopia and a nightmare to some people um when i when we did asthma json web assembly i  
**Translation:** Vocabulary: dystopia: 乌托邦的反面

**[5494.98s] English:** would joke and meme people with scenes like neo waking up in his pod in the matrix and he's all  
**Translation:** 

**[5499.94s] English:** skinny and weak and hairless um and you know you realize in the future that you're living in some  
**Translation:** Vocabulary: hairless: 无毛; matrix: 矩阵; skinny: 瘦弱

**[5507.04s] English:** simulation that it's all running on javascript and you just scream forever um it's possible  
**Translation:** 

**[5512.50s] English:** gary bernhardt uh does these funny talks he did watch js and then he did this  
**Translation:** Vocabulary: simulation: 模拟

**[5517.40s] English:** uh life and death of javascript i think it's called where he  
**Translation:** 

**[5520.00s] English:** He took some clever ideas that actually have a thread of credibility to them.  
**Translation:** Vocabulary: credibility: 可信性

**[5525.36s] English:** But I mentioned software fault isolation.  
**Translation:** 

**[5529.06s] English:** In the old days when we were using computers, we said we're going to use the Unix monolithic monitor.  
**Translation:** Vocabulary: monolithic: 整体的

**[5534.16s] English:** And it's the privileged program.  
**Translation:** 

**[5535.78s] English:** This is before you even had hardware rings of protection.  
**Translation:** 

**[5538.44s] English:** Some of the early 60s operating systems used hardware protection zones.  
**Translation:** 

**[5542.22s] English:** But Unix is privileged, and the program that runs user code in a process is hosted.  
**Translation:** Vocabulary: privileged: 特权拥有

**[5550.32s] English:** It's the guest in the host.  
**Translation:** 

**[5551.76s] English:** And you get to suspend it.  
**Translation:** 

**[5553.64s] English:** You get to kill it.  
**Translation:** 

**[5555.04s] English:** If it crashes, it doesn't take down the whole OS.  
**Translation:** 

**[5557.28s] English:** It's a wonderful idea.  
**Translation:** 

**[5559.74s] English:** But the call into the kernel is expensive, the system call, so-called.  
**Translation:** Vocabulary: kernel: 内核

**[5563.78s] English:** And this has even been optimized now for things like getting the time of day so it doesn't actually enter the kernel.  
**Translation:** 

**[5569.64s] English:** And meanwhile, hardware architecture.  
**Translation:** Vocabulary: optimized: 优化

**[5572.22s] English:** And virtualization techniques have gone in a different direction, even to the point where you can do software fault isolation very cheaply without entering the operating system kernel.  
**Translation:** 

**[5580.72s] English:** And so you get unikernels and exokernels and very lightweight VMs.  
**Translation:** Vocabulary: cheaply: 便宜地; exokernels: 外核; lightweight: 轻量级; unikernels: 单内核; virtualization: 虚拟化

**[5584.46s] English:** And so Gary took this idea and said, JavaScript will take over computing because the system call boundary is too expensive.  
**Translation:** 

**[5591.68s] English:** So everything ends up in JavaScript with these lighter weight isolation enforcement mechanisms.  
**Translation:** Vocabulary: computing: 计算

**[5596.60s] English:** It's not totally beyond belief.  
**Translation:** 

**[5599.42s] English:** It's VWAP assembly, too.  
**Translation:** 

**[5600.68s] English:** So it's nice to ask you sort of for advice.  
**Translation:** 

**[5605.26s] English:** There's so many people that are interested in starting to learning about programming, getting into this world.  
**Translation:** 

**[5611.00s] English:** Is there some number of languages, three to five programming languages that you would recommend people learn?  
**Translation:** 

**[5618.20s] English:** Or maybe a broader advice on how to get started in programming?  
**Translation:** 

**[5624.00s] English:** Well, so you asked about machine learning.  
**Translation:** 

**[5625.32s] English:** And JavaScript is a general purpose language.  
**Translation:** 

**[5627.92s] English:** And it's a language that's not...  
**Translation:** 

**[5630.68s] English:** Not that great for doing, you know, matrix operations or doing parallel programming, I would say.  
**Translation:** Vocabulary: matrix: 矩阵

**[5640.00s] English:** some extensions or some libraries that have some magic in them so if someone wanted to you know  
**Translation:** 

**[5646.06s] English:** learn um there are amazing languages in sort of the apl family that are very useful for i would  
**Translation:** Vocabulary: extensions: 插件

**[5652.52s] English:** say linear algebra which gets to a lot of the kernels and machine learning and so apl had like  
**Translation:** 

**[5658.22s] English:** j and then k and their k variants because the guy that did k is still going and he's  
**Translation:** Vocabulary: algebra: 线性代数; kernels: 核函数

**[5665.14s] English:** proprietary but he's still innovating there um there are you know python is used so people talk  
**Translation:** 

**[5670.86s] English:** about tennis for js well it's not that surprising because python was heavily used for machine  
**Translation:** Vocabulary: innovating: 创新; proprietary: 专有

**[5675.96s] English:** learning and python was always you know they didn't have this fast just-in-time compiler  
**Translation:** 

**[5680.50s] English:** tradition there were some projects that tried this and some of them were interesting um  
**Translation:** 

**[5685.18s] English:** pi pi was interesting but um the philosophy with python was all you need to go fast write a c  
**Translation:** 

**[5691.26s] English:** plugin and drop into c code um so i think  
**Translation:** 

**[5694.98s] English:** people  
**Translation:** 

**[5695.12s] English:** should look at multiple languages because there are different tools in the belt if you're trying  
**Translation:** 

**[5700.36s] English:** to do supervision or rapid prototyping you want a dynamic language you want to throw things together  
**Translation:** 

**[5704.88s] English:** and see what works if you're trying to go down to the metal very fast well i'm an old c hacker but  
**Translation:** Vocabulary: hacker: 编程高手; prototyping: 原型制作; supervision: 监督

**[5710.86s] English:** i was also the sponsor executive sponsor of rust at mozilla and rust is now escaped  
**Translation:** 

**[5715.32s] English:** you know from that sort of nest uh where it was born to be adopted by a bunch of companies to  
**Translation:** 

**[5721.50s] English:** have a foundation in the works uh some of the key core team members are working  
**Translation:** 

**[5724.96s] English:** now at amazon and other places so it looks like rust has reached escape velocity and rust is an  
**Translation:** 

**[5730.56s] English:** interesting language because one of our goals there one of the reasons i sponsored it was  
**Translation:** 

**[5734.32s] English:** we were all tired of seeing those remote code execution vulnerabilities due to c and c plus plus  
**Translation:** Vocabulary: vulnerabilities: 漏洞

**[5740.00s] English:** and we thought can we have a sort of safety property through a type and effect system or  
**Translation:** 

**[5745.84s] English:** an ownership system and rust has that and that ownership system is interesting because it doesn't  
**Translation:** 

**[5750.40s] English:** just give you memory safety there's a sort of theorem for free a dual that falls out for  
**Translation:** 

**[5754.80s] English:** protection against data races so rust is better for low-level programming you  
**Translation:** Vocabulary: theorem: 定理

**[5760.00s] English:** limit your unsafe code where you do have to be unsafe uh and you can prove certain facts about  
**Translation:** 

**[5764.60s] English:** memory safety and race condition uh avoidance and so i think people should learn these new languages  
**Translation:** 

**[5771.20s] English:** i think go is is a great language i admire you know the unix uh people who did that ken still  
**Translation:** 

**[5777.00s] English:** was involved rob pike of course um david uh what's his name and other people um go is a huge success  
**Translation:** 

**[5784.70s] English:** um really on the server side anywhere you have um you know a lot of networking to do and it's  
**Translation:** 

**[5790.88s] English:** garbage collected but it's also very pragmatic it has that sort of c flavor as an old c hacker i  
**Translation:** Vocabulary: pragmatic: 实用主义的

**[5796.16s] English:** can't get used to the fact that they swap the type and declarator in the declaration order i haven't  
**Translation:** 

**[5801.44s] English:** used rust but this is one of the most respected and loved languages currently so it's yeah and  
**Translation:** Vocabulary: declarator: 声明符

**[5806.64s] English:** it's still young you look at these things javascript is now considered old um it's gone  
**Translation:** 

**[5811.48s] English:** to so many versions that you can fall in love with it all over again  
**Translation:** 

**[5814.62s] English:** you  
**Translation:** 

**[5814.70s] English:** 25 plus years you know it's it's it's an adult uh it should be out of the house but um it could  
**Translation:** 

**[5821.64s] English:** be around another 25 years cannot rule it out so rust will be around for a long time the longer  
**Translation:** 

**[5826.60s] English:** you're around the more likely you're lindy and you're around you know a lot of people ask me  
**Translation:** Vocabulary: cannot: 不可能; lindy: 林迪

**[5831.24s] English:** like uh i i'm i'm often torn between recommending either python or javascript as the first language  
**Translation:** 

**[5837.26s] English:** to play with because i mean it's difficult because it's so easy to do javascript incorrectly  
**Translation:** 

**[5844.70s] English:** it's much uh it's much easier to do it correctly these days or like well like learn about programming  
**Translation:** 

**[5851.04s] English:** but the the cool thing about javascript is that you can create stuff that will put a smile on your  
**Translation:** 

**[5857.80s] English:** face like as a as a developer you can create stuff and it'll visually look like something  
**Translation:** 

**[5862.94s] English:** and it'll do stuff and it makes you feel good it makes you fall in love with programming  
**Translation:** 

**[5866.94s] English:** with python you could do the same it's a little slower and with c plus plus it takes  
**Translation:** 

**[5870.64s] English:** five to ten years to write a program that actually does something yeah so like  
**Translation:** 

**[5874.70s] English:** there's that tension between is JavaScript the right first step or is it Python?  
**Translation:** 

**[5880.00s] English:** I've been going back and forth on those two.  
**Translation:** 

**[5881.86s] English:** I have my Python, right?  
**Translation:** 

**[5882.74s] English:** It came from a lineage of ABC,  
**Translation:** Vocabulary: lineage: 血统

**[5885.32s] English:** which was a pedagogical language in the Netherlands.  
**Translation:** 

**[5889.74s] English:** And it was a good teaching language too.  
**Translation:** Vocabulary: pedagogical: 教学的

**[5896.72s] English:** I think it is a good teaching language.  
**Translation:** 

**[5897.86s] English:** And it's a little more restrictive in that if you misspell something  
**Translation:** Vocabulary: misspell: 错拼

**[5901.74s] English:** in a way that JavaScript might let run, let reach runtime,  
**Translation:** 

**[5905.86s] English:** it'll get stopped at syntax check in Python.  
**Translation:** Vocabulary: runtime: 运行时; syntax: 语法

**[5910.48s] English:** That's good for beginners.  
**Translation:** 

**[5911.78s] English:** I think the sloppiness that some people object to,  
**Translation:** Vocabulary: sloppiness: 马虎态度

**[5914.76s] English:** like people were just tweeting at me, having just learned JavaScript,  
**Translation:** 

**[5918.64s] English:** they said, I can take a number and I can index into it  
**Translation:** Vocabulary: tweeting: 发推

**[5921.10s] English:** and get undefined out of it as a property.  
**Translation:** 

**[5922.98s] English:** And why is that?  
**Translation:** Vocabulary: undefined: 未定义

**[5923.78s] English:** A number is not an object.  
**Translation:** 

**[5925.02s] English:** And I explained why it is, because like in Java,  
**Translation:** 

**[5927.30s] English:** the primitive types, which unfortunately are not objects,  
**Translation:** 

**[5929.76s] English:** can be automatically boxed or wrapped by an object.  
**Translation:** 

**[5932.94s] English:** And I made that implicit.  
**Translation:** 

**[5935.16s] English:** In Java,  
**Translation:** Vocabulary: implicit: 含蓄的

**[5935.86s] English:** it's typed and you have to declare things and you'll get type errors.  
**Translation:** 

**[5940.36s] English:** But there are cases in Java where you get auto-boxing or auto-wrapping  
**Translation:** 

**[5943.52s] English:** because you've declared that you want it.  
**Translation:** 

**[5945.74s] English:** In JavaScript, it just happens.  
**Translation:** 

**[5947.62s] English:** And so once I explain it, I'm like, oh, wow, I get it.  
**Translation:** 

**[5950.24s] English:** But it also means that you can commit a blunder that just...  
**Translation:** Vocabulary: blunder: 失误

**[5953.60s] English:** You don't get punished for it, you don't detect.  
**Translation:** 

**[5955.52s] English:** You get an undefined value and you don't know where it came from.  
**Translation:** 

**[5959.66s] English:** I've been reading a lot about military history recently.  
**Translation:** 

**[5963.26s] English:** And one way to paint the picture of browser,  
**Translation:** 

**[5965.86s] English:** internet browsers, is through the various wars throughout its history.  
**Translation:** 

**[5970.54s] English:** I don't know if that's a useful way to look at it,  
**Translation:** 

**[5972.30s] English:** but we've already talked a little bit about Netscape and Internet Explorer  
**Translation:** 

**[5975.78s] English:** in the early days.  
**Translation:** Vocabulary: explorer: 浏览器; netscape: 网景

**[5978.34s] English:** Can you tell the story of the different wars,  
**Translation:** 

**[5981.24s] English:** if that's at all an interesting way to look at it,  
**Translation:** 

**[5983.42s] English:** of the 90s and to today?  
**Translation:** 

**[5986.44s] English:** Yeah.  
**Translation:** 

**[5986.82s] English:** So I mentioned that Microsoft, which was convicted for it,  
**Translation:** 

**[5990.46s] English:** did abuse its monopoly,  
**Translation:** Vocabulary: convicted: 被判罪; monopoly: 垄断

**[5991.58s] English:** but they had a pretty good team by the time they did IE4.  
**Translation:** 

**[5995.00s] English:** And Netscape,  
**Translation:** 

**[5995.90s] English:** unfortunately, I was like second floor  
**Translation:** 

**[5997.84s] English:** and I was friends with all the first floor people,  
**Translation:** 

**[5999.50s] English:** the front end guys.  
**Translation:** 

**[6000.00s] English:** who did the javascript event hookup and things like that um that that team was fairly burnt out  
**Translation:** Vocabulary: hookup: 连接

**[6007.48s] English:** and i think having gone public uh the upper management wanted to buy a bunch of companies  
**Translation:** 

**[6013.22s] English:** to try to go head to head with microsoft didn't work but buying a bunch of companies usually  
**Translation:** 

**[6018.14s] English:** doesn't work i think the modern sort of approach it roughly is like mark zuckerberg uh took which  
**Translation:** 

**[6025.44s] English:** is to keep them at arm's length and let them do their thing and now that he's pulling whatsapp in  
**Translation:** 

**[6029.86s] English:** and people are fleeing it because it's tied into the ad surveillance but um you know for a while  
**Translation:** 

**[6036.20s] English:** they're keeping it separate really does work because you bought it for its value it's complimentary  
**Translation:** Vocabulary: complimentary: 免费提供的

**[6039.58s] English:** and you're not messing with it with netscape when they bought a bunch of companies they had  
**Translation:** 

**[6043.94s] English:** some of the first floor people or the founders burned out they had um newcomers who wanted their  
**Translation:** Vocabulary: founders: 创始团队; newcomers: 新加入者

**[6049.26s] English:** turn to do the browser and they hadn't really done browsers or understood them and so netscape  
**Translation:** 

**[6055.28s] English:** four was originally supposed to be three and it was so late they renumbered it when we did a three  
**Translation:** Vocabulary: browsers: 浏览器; renumbered: 重新编号

**[6059.42s] English:** release  
**Translation:** 

**[6059.86s] English:** jamie and a few others put some extra effort into uh secure mind was supported in the mail  
**Translation:** 

**[6064.86s] English:** built-in mail program um and that's a four was late and it was only on windows at first and  
**Translation:** 

**[6072.22s] English:** microsoft had really started doing better like they do they copy and the first version is trash  
**Translation:** 

**[6077.20s] English:** and the second one you're starting to feel a threat and the third one you can tell what's  
**Translation:** 

**[6081.00s] English:** going to happen and the fourth one's good and plus there's the benefit like you said that it  
**Translation:** 

**[6084.54s] English:** comes as a default browser yes and and yet netscape screwing it up and microsoft  
**Translation:** 

**[6089.86s] English:** really putting some quality people on it i4 was good on windows it was good and they did the  
**Translation:** Vocabulary: screwing: 搞砸

**[6095.12s] English:** dynamic html innovations they uh scott isaac's my old buddy a former accountant who programmed in  
**Translation:** 

**[6101.90s] English:** basic and became what microsoft calls a program manager which is kind of an elevated position it's  
**Translation:** Vocabulary: elevated: 提升的; innovations: 创新

**[6107.26s] English:** um you can be a programmer or an engineer track but you switch to it and you sort of  
**Translation:** 

**[6111.68s] English:** lead a lot of design and standards efforts and so scott isaac put in a lot of those  
**Translation:** 

**[6116.38s] English:** uh funky dhtml apis that didn't quite  
**Translation:** 

**[6119.86s] English:** you  
**Translation:** 

**[6120.00s] English:** have the same flavor as the stuff that i did and neither of them was like the later sort of  
**Translation:** 

**[6124.64s] English:** verbose java like dom w3c standardized but i4 was pretty darn good we i remember a friend scott  
**Translation:** Vocabulary: standardized: 标准化; verbose: 啰嗦

**[6131.52s] English:** firman and i got invited by scott isaacs to uh gordon beers in san jose they were doing a preview  
**Translation:** 

**[6138.16s] English:** of ie4 this must have been 1997 and scott said yeah we've got here's the new graphics stuff we're  
**Translation:** 

**[6145.12s] English:** doing we've got something like your netscape layers um we've got vml a vector markup language  
**Translation:** 

**[6151.36s] English:** you know we can do like virtual reality and scott and i looked at each other and said we're doomed  
**Translation:** Vocabulary: markup: 标记; netscape: 网景

**[6155.92s] English:** right microsoft was starting to fire in all cylinders so i have to give them credit for that  
**Translation:** 

**[6160.32s] English:** even though they abused their market power and maybe you know i shouldn't give them credit for  
**Translation:** Vocabulary: cylinders: 全速运转

**[6164.32s] English:** having the resources to hire talented people but they did a credible job on ie4 what really was bad  
**Translation:** 

**[6169.76s] English:** was that phase of the browser wars ended with monopoly and perhaps due to the answer  
**Translation:** Vocabulary: credible: 可信的; monopoly: 垄断

**[6175.12s] English:** trust case perhaps due to regulation in europe perhaps just due to microsoft not liking dealing  
**Translation:** 

**[6181.20s] English:** with standardization they they let it rot they just abandoned it i5 five five um i6 later but  
**Translation:** Vocabulary: standardization: 标准化

**[6190.96s] English:** these were not well maintained they had a lot of security bugs  
**Translation:** 

**[6194.24s] English:** it was really closed and outdated too even though it's getting updated it's just weird browsers  
**Translation:** Vocabulary: browsers: 浏览器; outdated: 过时

**[6199.44s] English:** like mozilla and then firefox were adding tabs opera had a version of tabs and uh they  
**Translation:** 

**[6205.12s] English:** didn't add tabs and they pop up blocking something i should have done from the start people realized  
**Translation:** 

**[6209.44s] English:** that you can tell when the user clicks something and it goes in javascript to open a little window  
**Translation:** 

**[6214.24s] English:** that you can sort of inspect the stack and see that the click originated that and it's probably  
**Translation:** Vocabulary: originated: 起源于

**[6218.64s] English:** okay whereas if you're just loading a script and it opens a new window that's a spam technique and  
**Translation:** 

**[6223.84s] English:** you should block it tabs were brilliant innovation like you said opera had it but like i remember  
**Translation:** 

**[6229.60s] English:** i fully switched to firefox the moment it was i remember like the moments of  
**Translation:** 

**[6235.12s] English:** first using tabs on firefox and like not liking it like for the first few minutes  
**Translation:** 

**[6240.00s] English:** and then like wait a minute you get the groove yeah you get the groove and you understand i mean  
**Translation:** 

**[6245.36s] English:** so that timing what year was this uh so because uh also as a aspiring web designer i uh used table  
**Translation:** Vocabulary: aspiring: 有志向的; groove: 节奏感

**[6253.14s] English:** so we didn't mention layout or css much there's also a change in the way like the frames were  
**Translation:** 

**[6259.52s] English:** going away yeah so there's a change in the way websites looked and behaved and all that kind of  
**Translation:** Vocabulary: layout: 页面布局

**[6264.88s] English:** stuff css finally which microsoft embraced with i4 and netscape never really did right uh css  
**Translation:** 

**[6271.04s] English:** became a better standard over time for doing table layout that relieved you of the need to use what  
**Translation:** Vocabulary: embraced: 接纳; relieved: 减轻

**[6277.08s] English:** are called spacer gifs yeah spacer gifs right images yeah you would throw into space out tables  
**Translation:** 

**[6282.60s] English:** um you know the the typographic power of the web has gotten better but it's still not on the level  
**Translation:** Vocabulary: typographic: 排版

**[6288.48s] English:** of pdf and you can't do advanced typography but um it's gotten really better and even then tables  
**Translation:** 

**[6294.08s] English:** were getting better  
**Translation:** 

**[6294.64s] English:** if you were using firefox that would have been 2004 because it was called firebird until  
**Translation:** 

**[6298.82s] English:** earlier that year five no yeah i think uh it wasn't well three i don't remember it was a  
**Translation:** Vocabulary: firebird: 火鸟浏览器

**[6304.04s] English:** fiber which had tabs uh we had tabs the whole way so yeah so it started out as mozilla slash  
**Translation:** 

**[6308.84s] English:** browser it became in 2002 became phoenix there's a bios that has an embedded version of ie and  
**Translation:** Vocabulary: embedded: 嵌入的

**[6314.78s] English:** they said we're called phoenix technologies you can't use phoenix and so we said okay we'll call  
**Translation:** 

**[6318.52s] English:** it firebird and then this australian centered open source database project started really like  
**Translation:** 

**[6324.64s] English:** in the true mad max style just screaming at us saying you can't use firebird and i had to sort of  
**Translation:** 

**[6329.62s] English:** be the ambassador and say okay we're going to rename and like we don't believe you shouldn't  
**Translation:** Vocabulary: rename: 改名

**[6332.50s] English:** use that we hate you and then we renamed it to firefox and they're like ah we love you and then  
**Translation:** 

**[6338.40s] English:** i don't haven't heard of them ever since but firefox was a clever name we had to think of  
**Translation:** Vocabulary: renamed: 改名

**[6342.50s] English:** something distinctive we wanted to keep the fire going and it turns out there's a red panda right  
**Translation:** 

**[6348.12s] English:** it's a nickname for so that's the second set of browser second browser wars so how did you  
**Translation:** Vocabulary: panda: 红熊猫

**[6354.64s] English:** firefox born how's mozilla born is there a there's a  
**Translation:** 

**[6360.00s] English:** Long story there, too.  
**Translation:** 

**[6361.08s] English:** So Netscape got acquired by AOL, which, as I say, was a reasonable happy ending for a lot of people because Netscape otherwise was going to go out of business because Microsoft was just killing its market.  
**Translation:** 

**[6370.72s] English:** There was no way to charge for a browser.  
**Translation:** Vocabulary: netscape: 网景浏览器

**[6372.56s] English:** Windows came with IE.  
**Translation:** 

**[6374.78s] English:** IE4 was pretty good, and Netscape 4 wasn't that good.  
**Translation:** 

**[6377.46s] English:** It took a while to get better.  
**Translation:** 

**[6380.12s] English:** But the Netscape executive said, let's do an open source escape pod.  
**Translation:** 

**[6384.66s] English:** And like in Star Wars and New Hope, the gunner won't shoot it because there's no life forms on board, right?  
**Translation:** 

**[6390.00s] English:** It's not a threat.  
**Translation:** 

**[6391.16s] English:** And so we did Mozilla in 1998, and it looked like it was going to initially give the world an open source browser.  
**Translation:** 

**[6400.04s] English:** But it's really hard to get people to work on this sort of hairball that had been hacked up over, by that point, four years.  
**Translation:** Vocabulary: hacked: 修改过多; hairball: 一团糟

**[6406.86s] English:** It also couldn't have the crypto module for secure sockets, so-called, or now transport layer security.  
**Translation:** 

**[6412.64s] English:** That was an electronic munition.  
**Translation:** Vocabulary: crypto: 加密; module: 模块; munition: 武器; sockets: 套接字

**[6414.22s] English:** We were not allowed to release that in the full 1024-bit key strength.  
**Translation:** 

**[6420.00s] English:** And yet people, one of whom I happened to meet previously at SGI when I went on a sales support engineering trip, Tim Hudson in Brisbane, Australia, and Eric A. Young, did what became OpenSSL.  
**Translation:** Vocabulary: brisbane: 布里斯班

**[6436.40s] English:** It was called SSL-EAY after Eric's initials.  
**Translation:** 

**[6439.56s] English:** And Tim and Eric took their OpenSSL outside of the purview of the NSA and the Department of Commerce, and they stuck it into Mozilla's code.  
**Translation:** Vocabulary: initials: 初始字母; purview: 管辖范围

**[6448.82s] English:** And that was perhaps the best hack.  
**Translation:** 

**[6450.00s] English:** That was done in the first few months after we open sourced the browser.  
**Translation:** 

**[6454.40s] English:** We had other problems.  
**Translation:** 

**[6455.38s] English:** The politics inside Netscape were riven by these acquisitions.  
**Translation:** Vocabulary: acquisitions: 收购; riven: 分裂

**[6458.20s] English:** So the one acquisition that kind of messed up Netscape 4 also wanted to keep doing a proprietary mail and groupware program, not Jamie Zawinski's mail program that was in Netscape 2 and 3.  
**Translation:** 

**[6470.08s] English:** And they held it back from open source.  
**Translation:** Vocabulary: groupware: 办公软件; proprietary: 私有软件

**[6471.84s] English:** We didn't have a mail program.  
**Translation:** 

**[6472.76s] English:** It was just a browser.  
**Translation:** 

**[6474.34s] English:** We didn't know what AOL would do to us.  
**Translation:** 

**[6476.70s] English:** Turns out they didn't interfere with us for a long time.  
**Translation:** Vocabulary: interfere: 干涉

**[6479.18s] English:** But Netscape.  
**Translation:** 

**[6480.00s] English:** wasn't the best steward of mozilla we were operating mozilla as a pirate ship without a  
**Translation:** Vocabulary: steward: 管理者

**[6485.70s] English:** legal entity so most of us worked for netscape under a separate organization and um initially  
**Translation:** 

**[6493.08s] English:** uh the first engineering manager tom paquin of netscape was the mozilla founding manager  
**Translation:** Vocabulary: founding: 创立; netscape: 网景

**[6498.70s] English:** but he he left pretty quickly and he left me as the acting manager which is more like method acting  
**Translation:** 

**[6504.24s] English:** in my case and um and i i did that was my first management stint but then um someone who'd written  
**Translation:** Vocabulary: stint: 任期

**[6511.06s] English:** the licenses mitchell baker she was a lawyer at netscape she was involved in the open source  
**Translation:** 

**[6515.60s] English:** license uh decision making and the actual writing and construction of those licenses that was  
**Translation:** 

**[6520.54s] English:** mitchell's job netscape public license and the truly open mozilla public license and there were  
**Translation:** 

**[6525.98s] English:** two because netscape needed because of some encumbered code needed some special rights but  
**Translation:** Vocabulary: encumbered: 受限制的

**[6529.62s] English:** that went away over time mitchell was always interested in mozilla and she came back from  
**Translation:** 

**[6533.52s] English:** maternity leave  
**Translation:** Vocabulary: maternity: 产假

**[6534.24s] English:** she said i'll be the manager if you want and jamie and i said sure and then jamie quit he  
**Translation:** 

**[6538.56s] English:** quit after a year he said this didn't work i'm sorry you know he acted like it was a total  
**Translation:** Vocabulary: jamie: 示例人物

**[6543.90s] English:** failure because mozilla didn't restart the browser market but there's no way it could have right  
**Translation:** 

**[6549.18s] English:** netscape was still shipping variants of netscape 4 which was based on the old code mozilla was  
**Translation:** 

**[6556.42s] English:** trying to re-architect code to make greenfield for developers so it was one of my big goals  
**Translation:** 

**[6560.80s] English:** it wasn't a technical goal so much as again a social goal  
**Translation:** Vocabulary: greenfield: 空白项目

**[6563.52s] English:** people wanted a more standard spaced browser they wanted a less of a hairball that had been  
**Translation:** 

**[6568.26s] English:** hacked on by x grad students starting four years prior so we said we're going to make a modular  
**Translation:** Vocabulary: hacked: 随意修改; hairball: 一团糟; modular: 模块化

**[6574.26s] English:** code base we're going to use a variant or an open source version of microsoft's component object  
**Translation:** 

**[6578.86s] English:** model has reference counting and standardized v tables virtual calls and c++ and we're going to  
**Translation:** Vocabulary: standardized: 标准化的

**[6585.86s] English:** use uh javascript we're going to have a bridge between those two so you can script those  
**Translation:** 

**[6589.64s] English:** components just like java components um we're going to make a module that's going to be a  
**Translation:** Vocabulary: module: 模块

**[6593.52s] English:** portable front end with a markup language for the user user interface not tables not html but  
**Translation:** 

**[6598.74s] English:** custom you know menu  
**Translation:** Vocabulary: interface: 用户界面; markup: 标记语言

**[6600.00s] English:** and dropdowns and toolbars.  
**Translation:** 

**[6602.36s] English:** And that was called Zool,  
**Translation:** Vocabulary: dropdowns: 下拉菜单; toolbars: 工具栏

**[6604.30s] English:** XML user interface language.  
**Translation:** 

**[6606.08s] English:** And some real talent on the Netscape side  
**Translation:** 

**[6607.62s] English:** delivered that.  
**Translation:** 

**[6608.28s] English:** Dave Hyatt, who was instrumental in Zool,  
**Translation:** Vocabulary: hyatt: 海特

**[6611.34s] English:** Chris Watterson, Joe Hewitt, Blake Ross.  
**Translation:** 

**[6615.86s] English:** And Blake was an intern.  
**Translation:** Vocabulary: blake: 布莱克; intern: 实习生; watterson: 沃特森

**[6617.84s] English:** He was like a high school-aged intern at Netscape.  
**Translation:** 

**[6620.32s] English:** And at some point,  
**Translation:** Vocabulary: netscape: 网景公司

**[6621.62s] English:** we were innovating rapidly in the Mozilla world  
**Translation:** 

**[6624.76s] English:** and Netscape was still caught up  
**Translation:** Vocabulary: innovating: 不断创新

**[6626.94s] English:** in this management mess from these acquisitions  
**Translation:** 

**[6629.16s] English:** and it wasn't delivering.  
**Translation:** 

**[6630.54s] English:** And every year they were wondering  
**Translation:** 

**[6631.78s] English:** if AOL was going to come  
**Translation:** 

**[6632.76s] English:** and start beheading the executives  
**Translation:** 

**[6634.08s] English:** because it doesn't do anything useful.  
**Translation:** Vocabulary: beheading: 砍头; executives: 高管

**[6636.04s] English:** And there was this thought  
**Translation:** 

**[6636.80s] English:** you should take the Netscape browser engine  
**Translation:** 

**[6638.82s] English:** and put it in the Windows AOL client,  
**Translation:** 

**[6640.74s] English:** which was the dial-up client  
**Translation:** 

**[6641.84s] English:** that all the increasingly aging users of AOL were using.  
**Translation:** 

**[6645.34s] English:** Never happened.  
**Translation:** 

**[6646.20s] English:** And it would have been too big a change.  
**Translation:** 

**[6648.10s] English:** So it wasn't clear why AOL bought Netscape,  
**Translation:** 

**[6649.84s] English:** but as I said, they left it alone,  
**Translation:** 

**[6650.90s] English:** but Netscape didn't leave Mozilla alone.  
**Translation:** 

**[6653.34s] English:** And so in 2001,  
**Translation:** 

**[6657.18s] English:** Mitchell called me up and said,  
**Translation:** 

**[6658.42s] English:** I'm no longer,  
**Translation:** 

**[6659.16s] English:** I'm no longer employed.  
**Translation:** 

**[6659.80s] English:** And I was like, what, you quit?  
**Translation:** 

**[6660.88s] English:** No, no, this wasn't my choice.  
**Translation:** 

**[6662.32s] English:** And there was a layoff,  
**Translation:** 

**[6663.70s] English:** which maybe accidentally or on purpose  
**Translation:** Vocabulary: layoff: 裁员

**[6665.76s] English:** got rid of Mitchell.  
**Translation:** 

**[6666.58s] English:** But the funny thing was,  
**Translation:** 

**[6667.42s] English:** we had an open source project.  
**Translation:** 

**[6668.68s] English:** We had a lot of the engineers on staff on our side  
**Translation:** 

**[6671.14s] English:** and we had people we'd hired  
**Translation:** 

**[6674.22s] English:** through the Mozilla community  
**Translation:** 

**[6675.10s] English:** who were top-notch.  
**Translation:** 

**[6676.32s] English:** They'd risen, you know,  
**Translation:** 

**[6677.32s] English:** they came in high quality,  
**Translation:** 

**[6678.62s] English:** they knew the code  
**Translation:** 

**[6679.16s] English:** and they actually were better than the average  
**Translation:** 

**[6681.00s] English:** or median hire of Netscape.  
**Translation:** 

**[6683.36s] English:** And so the funny thing was  
**Translation:** 

**[6685.26s] English:** the executive who thought  
**Translation:** 

**[6687.80s] English:** they'd gotten rid of Mitchell  
**Translation:** 

**[6688.88s] English:** in the layoff  
**Translation:** 

**[6689.44s] English:** on the next week's community call  
**Translation:** 

**[6691.66s] English:** around Mozilla and what to do,  
**Translation:** 

**[6693.42s] English:** there's Mitchell.  
**Translation:** 

**[6695.10s] English:** And so this showed  
**Translation:** 

**[6695.64s] English:** you can kind of transcend your,  
**Translation:** 

**[6697.18s] English:** you know,  
**Translation:** Vocabulary: transcend: 超越

**[6698.42s] English:** boundaries of corporate open source  
**Translation:** 

**[6700.12s] English:** if you get a project  
**Translation:** 

**[6701.18s] English:** that has enough loyalty,  
**Translation:** 

**[6702.56s] English:** even among the paid staff,  
**Translation:** 

**[6703.76s] English:** because we had outside people contributing.  
**Translation:** 

**[6705.56s] English:** We had people at Red Hat  
**Translation:** 

**[6707.10s] English:** and a few other places,  
**Translation:** 

**[6707.82s] English:** but the majority of the hackers  
**Translation:** Vocabulary: hackers: 黑客

**[6709.26s] English:** were employed by Netscape.  
**Translation:** 

**[6710.34s] English:** But a lot of them at that point  
**Translation:** 

**[6711.72s] English:** had come from the community  
**Translation:** 

**[6713.04s] English:** and others got the community  
**Translation:** 

**[6714.70s] English:** and wanted to work with it.  
**Translation:** 

**[6715.94s] English:** And it was really the weakest engineers  
**Translation:** 

**[6717.28s] English:** at Netscape who didn't like Mozilla.  
**Translation:** 

**[6718.88s] English:** And didn't like.  
**Translation:** 

**[6720.00s] English:** the the crucible of competing with the the better uh programmers so if the project is good enough  
**Translation:** 

**[6725.34s] English:** it will rise the phoenix will rise out of the that's exactly right and so we had this this  
**Translation:** Vocabulary: crucible: 试炼之地; programmers: 程序员

**[6729.94s] English:** mozilla code base that was getting better in fact i think at some point in 2002 when we declared  
**Translation:** 

**[6734.12s] English:** mozilla 1.0 i engineered a roadmap that successively through similar sort of six week  
**Translation:** 

**[6740.00s] English:** five week releases like we all do with browser releases nowadays chrome does and firefox um  
**Translation:** 

**[6745.54s] English:** three weeks we we we got to a point where we said you know what it doesn't suck this is like  
**Translation:** 

**[6750.82s] English:** the 1.0 that you want to release because if you hold it back any longer to polish it you're denying  
**Translation:** 

**[6755.80s] English:** others the ability to use it's like pro engineer the mechanical cad tool embedded the code they  
**Translation:** Vocabulary: embedded: 嵌入的

**[6760.84s] English:** embedded the layout engine um and mozilla 1.0 was like a netscape communication suite we at that  
**Translation:** 

**[6767.30s] English:** point gotten mail people to reintegrate mail and news and we had an editor for html and it felt  
**Translation:** Vocabulary: layout: 布局; reintegrate: 重新整合

**[6774.30s] English:** like a 90s suite  
**Translation:** 

**[6775.54s] English:** suiteware um and it felt kind of bloated and the people who were taking that mozilla open source  
**Translation:** Vocabulary: bloated: 臃肿; suiteware: 办公软件

**[6782.02s] English:** and then adding netscape flavor to it were not calling the shots right and they were also under  
**Translation:** 

**[6787.26s] English:** al's thumb a little bit and that they said well we should probably put the al instant messenger  
**Translation:** Vocabulary: messenger: 即时通讯; netscape: 网景

**[6791.86s] English:** chiclet on the toolbar and we should put the icq the other messaging system that al had acquired  
**Translation:** 

**[6796.98s] English:** we should put the icq you know button on the toolbar and pretty soon netscape looked like  
**Translation:** 

**[6801.50s] English:** a bit of a nascar badge to fruition mozilla and that  
**Translation:** 

**[6805.34s] English:** you know i think that's the the the the the the the the the the the the the the the the the the  
**Translation:** Vocabulary: nascar: 纳斯卡赛车标志

**[6805.54s] English:** also made mozilla more popular and and yet um they they had you know contrived to um fire or lay  
**Translation:** 

**[6813.96s] English:** off the leader and and and we carried on with an open source structure where mozilla was still you  
**Translation:** Vocabulary: contrived: 刻意的

**[6819.98s] English:** know mitchell was calling sort of management or uh project level shots and i was calling technical  
**Translation:** 

**[6825.20s] English:** shots and um we we had a popular suite but we thought why not make it just a browser because  
**Translation:** 

**[6832.98s] English:** it'll be simpler it'll do one job well  
**Translation:** 

**[6835.54s] English:** and even then we can strip it down by having extensions so dave hyatt and  
**Translation:** Vocabulary: extensions: 插件

**[6840.00s] English:** Blake Ross, the high school-aged intern, did the first version, which was called Mozilla slash browser.  
**Translation:** 

**[6847.10s] English:** It was a small group of us, Ian Hicks and Asa Dotzler, me, Joe Hewitt and Hyatt and Blake.  
**Translation:** Vocabulary: blake: 布莱克; hewitt: Hewitt; hicks: 希克斯; hyatt: 海耶特; intern: 实习生

**[6854.60s] English:** And Hyatt was really the senior hacker.  
**Translation:** 

**[6856.54s] English:** He'd done all these things like amazing cross-platform menus through the user interface market language.  
**Translation:** Vocabulary: hacker: 黑客; interface: 界面

**[6863.14s] English:** And he knew how to do tab browsing.  
**Translation:** 

**[6864.66s] English:** He'd implemented it natively on macOS at the time in Camino, originally called Chimera.  
**Translation:** Vocabulary: browsing: 浏览; chimera: 怪兽; natively: 原生

**[6872.14s] English:** He'd written multiple implementations, which was a thing programmers should do.  
**Translation:** 

**[6876.38s] English:** It's like the V8 team did for those missing years when the rest of the Chrome team's like, where's V8?  
**Translation:** Vocabulary: implementations: 实现版本; programmers: 程序员

**[6882.00s] English:** In fact, Dave's wife, Rebecca, told me a story about when they were at UIUC.  
**Translation:** 

**[6885.86s] English:** They were also University of Illinois grad students.  
**Translation:** Vocabulary: rebecca: 瑞贝卡

**[6889.18s] English:** There was an assignment.  
**Translation:** 

**[6890.34s] English:** It was a programming assignment.  
**Translation:** 

**[6891.30s] English:** It was supposed to be due at the end of the semester.  
**Translation:** 

**[6893.54s] English:** And Dave's friend...  
**Translation:** 

**[6894.66s] English:** And Dave's friend was this, I'm going to go think and I'm going to design and I'm going to make this platonic perfect form of the program.  
**Translation:** 

**[6901.32s] English:** And then I'm going to write it at the end when it's due.  
**Translation:** Vocabulary: platonic: 纯理论的

**[6903.72s] English:** And Hyatt just went in and started hacking.  
**Translation:** 

**[6905.16s] English:** He wrote one version.  
**Translation:** Vocabulary: hacking: 非法入侵

**[6905.94s] English:** He wrote a second version, a third version.  
**Translation:** 

**[6907.96s] English:** End of the semester comes around.  
**Translation:** 

**[6909.24s] English:** The friend's not doing too well.  
**Translation:** 

**[6910.92s] English:** It wasn't perfect and it wasn't written.  
**Translation:** 

**[6913.02s] English:** I'm not sure how that story ended for him, but Dave's version was a fifth iteration.  
**Translation:** 

**[6917.08s] English:** It was great.  
**Translation:** Vocabulary: iteration: 修改版本

**[6918.18s] English:** And so he'd done that with everything you need in a tabbed browser.  
**Translation:** 

**[6921.48s] English:** And this really showed well in Phoenix.  
**Translation:** 

**[6924.66s] English:** Called Phoenix and I had to rename two more times.  
**Translation:** 

**[6928.18s] English:** And, you know, Blake went to Stanford.  
**Translation:** Vocabulary: rename: 改名; stanford: 斯坦福大学

**[6930.78s] English:** He became a Stanford student and couldn't work on it.  
**Translation:** 

**[6933.88s] English:** Dave Hyatt went to Apple in 2001.  
**Translation:** 

**[6936.60s] English:** He was one of the founding Safari team members.  
**Translation:** 

**[6939.50s] English:** Interesting.  
**Translation:** Vocabulary: founding: 创始的

**[6940.14s] English:** Wow.  
**Translation:** 

**[6940.44s] English:** But he was still blogging about tabbed browsing.  
**Translation:** 

**[6943.56s] English:** I think Apple at some point said...  
**Translation:** 

**[6944.62s] English:** Does Safari have tabbed browsing?  
**Translation:** 

**[6946.08s] English:** Yeah.  
**Translation:** 

**[6946.54s] English:** But it was because of Hyatt.  
**Translation:** 

**[6948.00s] English:** Hyatt was quite a feather in their cap.  
**Translation:** 

**[6949.50s] English:** Don Melton, who had been the engineering manager for Safari from the beginning.  
**Translation:** Vocabulary: melton: 唐纳德·梅尔顿

**[6954.66s] English:** Had been in Netscape also.  
**Translation:** 

**[6956.62s] English:** And so this is a diaspora of talent.  
**Translation:** Vocabulary: diaspora: 流散; netscape: 网景

**[6959.14s] English:** And yet Hyatt...  
**Translation:** 

**[6960.00s] English:** was still kind of writing blog posts about how to do tabs right and at some point apple said don't  
**Translation:** 

**[6964.48s] English:** don't blog about that that's our proprietary tab technology and it's like no it's not it was an  
**Translation:** 

**[6968.90s] English:** opera and i've refined it um so we had to replace people and we had ben goodger uh new zealander we  
**Translation:** Vocabulary: proprietary: 专有技术; refined: 改进; zealander: 新西兰人

**[6977.30s] English:** hired at netscape and he stepped in to be the firefox lead and we also had this weird circumstance  
**Translation:** 

**[6983.08s] English:** where aol finally did notice that netscape was kind of a albatross that they bought it for no  
**Translation:** Vocabulary: albatross: 累赘; circumstance: 情况

**[6989.34s] English:** particular benefit and even then the aol politics were also heinous sort of east coast politics i  
**Translation:** 

**[6995.40s] English:** remember taking two trips there because i was a principal engineer and so us principal engineers  
**Translation:** Vocabulary: heinous: 罪恶深重的

**[6998.80s] English:** got trotted out to do dog and pony shows in dulles virginia and the uh the aol upper management was  
**Translation:** 

**[7005.30s] English:** very east coast in flavor and they were at that time merging with time warner which did not go  
**Translation:** Vocabulary: trotted: 被展示

**[7010.00s] English:** well so one of these years we went out there and we were all doing dog and pony shows and there  
**Translation:** 

**[7013.58s] English:** were these characters that were sort of like marketing guys one of them was wearing a cravat  
**Translation:** Vocabulary: cravat: 领结

**[7017.48s] English:** and they were one was named reggie  
**Translation:** 

**[7019.34s] English:** and they were they were they were very um you rather than non-you or they were like what's  
**Translation:** Vocabulary: reggie: 瑞吉

**[7026.86s] English:** what stillman's metropolitan film uhb um urban haute bourgeoisie um they were haute bourgeois  
**Translation:** 

**[7035.42s] English:** they were um funny and they were kind of useless and kind of preppy and then the next year we went  
**Translation:** Vocabulary: bourgeois: 资产阶级; bourgeoisie: 资产阶级; haute: 上流的; preppy: 整洁的

**[7041.14s] English:** back and i said where's reggie and it's like oh reggie's not here anymore because time warner  
**Translation:** 

**[7044.86s] English:** realized that the merger wasn't in their interest either and then the sort of knives came out  
**Translation:** 

**[7049.34s] English:** and this was these these mergers rarely work right this is very difficult you get these giant  
**Translation:** 

**[7053.22s] English:** companies and they think there's going to be synergy that was the 90s late 90s watch word  
**Translation:** Vocabulary: synergy: 协同效应

**[7057.14s] English:** and there wasn't synergy with aol buying netscape and there wasn't synergy with time warner but did  
**Translation:** 

**[7061.40s] English:** aol ever really work was it ever really cool like the same kind of fire and excitement that  
**Translation:** 

**[7066.62s] English:** firefox eventually created was that ever there in aol aol was the right time to do a dial-up service  
**Translation:** 

**[7074.80s] English:** that got distribution by basically leaflet bombing compact discs right on  
**Translation:** 

**[7079.34s] English:** the country  
**Translation:** 

**[7080.00s] English:** and they beat out CompuServe and the other ones, Prodigy,  
**Translation:** Vocabulary: prodigy: 奇才

**[7085.30s] English:** and then the web happened.  
**Translation:** 

**[7087.04s] English:** And so you had almost like this isolated continent,  
**Translation:** Vocabulary: isolated: 孤立的

**[7091.08s] English:** like some of the evolutionary biologists I follow  
**Translation:** 

**[7093.56s] English:** make fun of the funny large mammal,  
**Translation:** Vocabulary: biologists: 生物学家; evolutionary: 进化; mammal: 哺乳动物

**[7096.94s] English:** you know, marsupial mammals of Australia,  
**Translation:** 

**[7099.94s] English:** how silly they are.  
**Translation:** Vocabulary: mammals: 哺乳动物; marsupial: 有袋动物

**[7101.42s] English:** So AOL is like Australia.  
**Translation:** 

**[7104.02s] English:** And you saw it over time because they kept aging  
**Translation:** 

**[7106.32s] English:** and they were using AOL to get online  
**Translation:** 

**[7108.08s] English:** and they couldn't really use a web browser.  
**Translation:** 

**[7110.50s] English:** And it became sort of a valued cohort  
**Translation:** 

**[7113.26s] English:** because they still have relatively high socioeconomic status  
**Translation:** Vocabulary: cohort: 同辈群体; socioeconomic: 社会经济

**[7116.14s] English:** and they have grandchildren, but it's going away.  
**Translation:** 

**[7118.46s] English:** It's dying at some point.  
**Translation:** 

**[7119.56s] English:** Towards the end of the aughts, that decade,  
**Translation:** 

**[7122.14s] English:** and then to the decade 2010 plus,  
**Translation:** 

**[7126.10s] English:** that Firefox became this incredible...  
**Translation:** 

**[7128.70s] English:** I forget when Chrome came out, but...  
**Translation:** 

**[7130.42s] English:** 2008, September.  
**Translation:** 

**[7131.14s] English:** 2008, but Firefox was the sexy, cool thing  
**Translation:** 

**[7134.56s] English:** that represented a lot of the cutting-edge technologies  
**Translation:** 

**[7137.38s] English:** and all that kind of stuff.  
**Translation:** 

**[7138.08s] English:** Web 2.  
**Translation:** 

**[7139.02s] English:** It was amazing.  
**Translation:** 

**[7140.22s] English:** Tim O'Reilly and John Battelle did the first Web 2 conference,  
**Translation:** 

**[7143.38s] English:** which eventually became huge and they split it.  
**Translation:** Vocabulary: battelle: 巴特利

**[7145.40s] English:** But that was in 2004.  
**Translation:** 

**[7146.70s] English:** That's right when Firefox was out.  
**Translation:** 

**[7148.58s] English:** Craigslist was huge.  
**Translation:** 

**[7150.24s] English:** It was killing classified revenue for newspapers.  
**Translation:** Vocabulary: craigslist: 分类广告网站

**[7152.48s] English:** But there was just this ferment.  
**Translation:** 

**[7154.48s] English:** People were starting...  
**Translation:** Vocabulary: ferment: 动荡

**[7155.16s] English:** Wikipedia along there somewhere?  
**Translation:** 

**[7156.64s] English:** Gmail was already done and it was an impressive web mail.  
**Translation:** 

**[7159.78s] English:** There were others before it, like Hotmail,  
**Translation:** 

**[7161.14s] English:** but Gmail was really impressive from Google.  
**Translation:** 

**[7162.92s] English:** And Google Maps.  
**Translation:** 

**[7163.88s] English:** People started seeing what could be done.  
**Translation:** 

**[7165.82s] English:** They thought, how can you drag the map around?  
**Translation:** 

**[7168.66s] English:** How does that work?  
**Translation:** 

**[7169.72s] English:** And it was all JavaScript and images.  
**Translation:** 

**[7172.12s] English:** So Gmail was 2003, 2004?  
**Translation:** 

**[7174.44s] English:** Yeah, I think it actually started quite early.  
**Translation:** 

**[7176.26s] English:** It might have been 2002 or 2003.  
**Translation:** 

**[7177.36s] English:** But by the time we started dealing with Google and Firefox  
**Translation:** 

**[7179.92s] English:** to get the search deal,  
**Translation:** 

**[7181.10s] English:** which was the main revenue source for Mozilla,  
**Translation:** 

**[7183.40s] English:** and still is,  
**Translation:** 

**[7184.72s] English:** 2004, early,  
**Translation:** 

**[7186.68s] English:** Sergey Brin, one of his trusted engineer guys,  
**Translation:** 

**[7189.76s] English:** Fritz Schneider, made contact with me at Mozilla.  
**Translation:** 

**[7191.96s] English:** And we started talking and we realized  
**Translation:** Vocabulary: fritz: 弗里茨; schneider: 施耐德

**[7194.16s] English:** search and browser need each other.  
**Translation:** 

**[7196.76s] English:** And this is deeply true.  
**Translation:** 

**[7198.08s] English:** This is still true.  
**Translation:** 

**[7199.62s] English:** This is what we're talking about.  
**Translation:** 

**[7200.00s] English:** why a lot of the search engines have their own browsers.  
**Translation:** 

**[7202.28s] English:** Yeah, so in case people don't know,  
**Translation:** Vocabulary: browsers: 浏览器

**[7203.68s] English:** the main revenue source for the browser  
**Translation:** 

**[7205.62s] English:** is the default search engine,  
**Translation:** 

**[7207.28s] English:** which is kind of incredible to think about,  
**Translation:** 

**[7209.28s] English:** that that is the revenue source.  
**Translation:** 

**[7211.50s] English:** It's a little bit sad.  
**Translation:** 

**[7212.62s] English:** Yeah, it leads to this capture or kill effect  
**Translation:** 

**[7214.62s] English:** where you have the search engine own its own browser  
**Translation:** 

**[7217.04s] English:** and other browsers may struggle to get distribution,  
**Translation:** 

**[7221.30s] English:** we talked about earlier.  
**Translation:** 

**[7222.66s] English:** So where, and you said you've figured out  
**Translation:** 

**[7226.84s] English:** that Google is working on its own browser at some point.  
**Translation:** 

**[7229.78s] English:** 2006, yeah.  
**Translation:** 

**[7230.72s] English:** 2006, so would you say Firefox versus,  
**Translation:** 

**[7233.24s] English:** was Internet Explorer part of the war here  
**Translation:** Vocabulary: explorer: 浏览器

**[7235.40s] English:** or was it Firefox versus Chrome?  
**Translation:** 

**[7237.30s] English:** So Firefox didn't quite cause Microsoft to reconvene IE.  
**Translation:** Vocabulary: reconvene: 重新召开

**[7240.90s] English:** They did do IE7 and I remember being on a plane  
**Translation:** 

**[7244.60s] English:** back from the standards meeting,  
**Translation:** 

**[7246.22s] English:** JavaScript standards meeting from Seattle, from Redmond,  
**Translation:** 

**[7248.98s] English:** and there was some Microsoft guy in front of me.  
**Translation:** Vocabulary: redmond: 雷德蒙; seattle: 西雅图

**[7252.00s] English:** It turns out my wife knew him from her past life  
**Translation:** 

**[7254.94s] English:** before we married and he was just this bearded big guy  
**Translation:** 

**[7258.20s] English:** and he was like, we should have just,  
**Translation:** 

**[7259.78s] English:** killed Firefox in the cradle.  
**Translation:** Vocabulary: cradle: 摇篮

**[7261.52s] English:** All we needed to do was add popup locking in and tabs  
**Translation:** 

**[7264.16s] English:** and we could have made Internet Explorer kill Firefox.  
**Translation:** 

**[7266.18s] English:** And it's like, shoulda, coulda, woulda, pal.  
**Translation:** 

**[7267.82s] English:** And I was right behind him overhearing this.  
**Translation:** Vocabulary: overhearing: 偷听

**[7270.30s] English:** But they didn't, they were slow and IE7 wasn't that great  
**Translation:** 

**[7273.54s] English:** and what really got them started, I think, was Chrome.  
**Translation:** 

**[7278.44s] English:** And I talked to Larry Page in 2005, I think I said,  
**Translation:** 

**[7282.80s] English:** we're talking about the Firefox relationship,  
**Translation:** 

**[7284.50s] English:** but he was also saying, what about WebKit?  
**Translation:** 

**[7286.12s] English:** This was Apple's version of the old caged email.  
**Translation:** 

**[7289.78s] English:** Oh, engine from, from Linux, the KDE side of Linux  
**Translation:** 

**[7294.18s] English:** that was used in the Conqueror browser,  
**Translation:** Vocabulary: conqueror: 征服者浏览器

**[7295.76s] English:** all spelled with Ks, that Apple had forked.  
**Translation:** 

**[7298.14s] English:** And, and in 2005 was when Apple's principals,  
**Translation:** Vocabulary: principals: 主要人物

**[7301.68s] English:** including Dave Hyatt, Maciej Stachowiak,  
**Translation:** 

**[7303.40s] English:** some of my friends who are still there said,  
**Translation:** Vocabulary: hyatt: 戴夫·海特; stachowiak: 斯塔乔维克

**[7305.20s] English:** we must stop patch bombing this poor KD, KHML project.  
**Translation:** 

**[7308.54s] English:** We should make a proper Mozilla-like organization,  
**Translation:** 

**[7310.90s] English:** webkit.org.  
**Translation:** 

**[7311.80s] English:** Now it wasn't a separate nonprofit or anything.  
**Translation:** Vocabulary: nonprofit: 非盈利机构

**[7313.72s] English:** It was still Apple, it was Apple controlled,  
**Translation:** 

**[7315.22s] English:** but they made their fork first class  
**Translation:** 

**[7318.16s] English:** and they made it be something  
**Translation:** 

**[7319.60s] English:** that they all wanted.  
**Translation:** 

**[7320.00s] English:** worked in and lived in and that was before chrome and then chrome larry page said what about webcam  
**Translation:** 

**[7325.60s] English:** i said yeah it's nice i have friends who work on it you might use that if you do your own browser  
**Translation:** 

**[7329.46s] English:** why don't you do your own browser don't worry about firefox you should do your own browser  
**Translation:** 

**[7332.82s] English:** you can have your own you know opinion of how it should work and and sure enough they did so by  
**Translation:** 

**[7337.40s] English:** 2006 we knew they'd been working on it some of the some of my friends who'd been at netscape  
**Translation:** 

**[7340.94s] English:** did the original demo and the demo wasn't what you thought it didn't have the fast javascript  
**Translation:** Vocabulary: netscape: 网景浏览器

**[7345.10s] English:** that was still off in denmark and on a farm um did it have tabs it had tabs because all  
**Translation:** 

**[7351.44s] English:** browsers had tabs at this point and it had uh this software fault isolation i mentioned it  
**Translation:** Vocabulary: browsers: 浏览器

**[7357.50s] English:** was through process isolation so in theory each tab has some operating system process and so  
**Translation:** 

**[7363.96s] English:** what's going to take your tab down well webkit has bugs that can crash it but flash was still  
**Translation:** 

**[7369.36s] English:** big then all the restaurant sites remember and flash crashed a lot so the demo that i heard about  
**Translation:** 

**[7374.90s] English:** my  
**Translation:** 

**[7375.08s] English:** friends x netscape x as a lot of people did inside google was the sad tab they showed an  
**Translation:** 

**[7381.20s] English:** early version of chrome which is this bare bones tab browser they loaded a site with a known flash  
**Translation:** 

**[7385.84s] English:** bone and then suddenly flash crashes and everyone expected the whole browser to go down but instead  
**Translation:** 

**[7391.22s] English:** you got this little sad face in the tab and you could reload it and there it is again so this was  
**Translation:** 

**[7395.20s] English:** this was uh an improvement it was a real move for security it was based on you know a company  
**Translation:** 

**[7401.02s] English:** that acquired called green border that had some really big brains like olfar erlingson  
**Translation:** Vocabulary: erlingson: 埃林松

**[7405.08s] English:** i think was involved and they had done some exotic uh security stuff but they ended up simplifying it  
**Translation:** 

**[7410.02s] English:** to this process isolation and um it was good and firefox didn't have it at the time so we were  
**Translation:** Vocabulary: simplifying: 简化

**[7417.06s] English:** still struggling with you know uh security bugs um so we knew chrome was coming but it took two  
**Translation:** 

**[7423.48s] English:** more years to come out and at the time we were still getting you know the google search revenue  
**Translation:** 

**[7428.18s] English:** we were still um making google the default engine and firefox was still growing firefox grew i think  
**Translation:** 

**[7434.20s] English:** until 2011.  
**Translation:** 

**[7435.08s] English:** that was when it peaked and as it started falling it was because of chrome  
**Translation:** 

**[7440.00s] English:** came out in 2008 and it was a comic book that leaked accidentally that showed some of the people  
**Translation:** 

**[7444.72s] English:** who worked on it. Lars Bach was in there and so on. It was kind of soft launch because they didn't  
**Translation:** 

**[7449.58s] English:** market it heavily. They didn't push distribution, but Google had reason to worry about distribution  
**Translation:** 

**[7454.68s] English:** because Microsoft was, you know, doing a search engine Bing since 2007. In fact, when they came  
**Translation:** 

**[7461.22s] English:** out with Bing, Google was worried that Microsoft would just brute force switch the default browser  
**Translation:** Vocabulary: brute: 粗暴

**[7466.88s] English:** in everyone's Internet Explorer or even Firefox on Windows to Bing from Google. And Microsoft  
**Translation:** 

**[7473.78s] English:** wasn't, I think, ready to dare the antitrust cops that way, even though they'd gone to sleep.  
**Translation:** Vocabulary: antitrust: 反垄断; explorer: 浏览器

**[7479.06s] English:** And I don't think Bing was ready either. But just in case it happens, Sundar Pichai,  
**Translation:** 

**[7485.26s] English:** who rose very well based on this work, was sort of in charge of getting distribution deals. And  
**Translation:** 

**[7490.66s] English:** he got Google Toolbar and Google Desktop Search distribution. And remember those pieces of  
**Translation:** 

**[7496.46s] English:** software?  
**Translation:** 

**[7496.88s] English:** Those were like desktop extensions, toolbars, or operating system extensions for doing desktop  
**Translation:** 

**[7502.60s] English:** search in your local files. Kind of like Mac OS Spotlight, right?  
**Translation:** Vocabulary: extensions: 扩展; spotlight: 桌面搜索; toolbars: 工具栏

**[7505.98s] English:** Sadly, they all died.  
**Translation:** 

**[7507.30s] English:** They all died. And there were some features that we still missed that didn't make it into Chrome.  
**Translation:** 

**[7510.44s] English:** But Sundar got OEMs to bundle those. And then he got enough of those deals that by 2007 or 2008,  
**Translation:** 

**[7517.28s] English:** Google felt, well, if Bing, Microsoft does the worst and tries to force Bing,  
**Translation:** Vocabulary: bundle: 捆绑销售

**[7521.72s] English:** we can reach in and reset it with that point of presence. So that was, you know, good for Sundar's  
**Translation:** 

**[7526.88s] English:** career. And it was good for Google, but it never came to pass that they had to defend. Microsoft  
**Translation:** 

**[7531.02s] English:** was still, you know, slow. And by the time they saw Chrome come out, then they did what would have  
**Translation:** 

**[7536.44s] English:** been IE9. And then they said, we're going to have a fast JavaScript engine to Chakra, Chakra Core.  
**Translation:** Vocabulary: chakra: 磁器引擎

**[7541.48s] English:** And they did okay. They were another process isolated, fast JavaScript browser, tab browser.  
**Translation:** 

**[7549.08s] English:** So it sounds like there's a deep fundamental coupling of search engine and browser that's  
**Translation:** Vocabulary: isolated: 独立运行

**[7554.02s] English:** mixing this whole thing up. And obviously, Firefox,  
**Translation:** 

**[7556.88s] English:** doesn't have a search engine.  
**Translation:** 

**[7560.00s] English:** That's like, I mean, you're partnering with somebody, with a search engine, with Yahoo or with Google or so on.  
**Translation:** 

**[7568.74s] English:** They tried Yahoo.  
**Translation:** Vocabulary: yahoo: 雅虎

**[7569.30s] English:** That was unfortunate because I think even though Marissa Mayer talked about it, she never pulled it off.  
**Translation:** 

**[7575.82s] English:** They never restored the search team that had been laid off.  
**Translation:** 

**[7579.58s] English:** I believe Carol Bartz was running Yahoo when Carol said, I've got to get rid of one of three expensive things.  
**Translation:** 

**[7584.52s] English:** I'm going to get rid of search.  
**Translation:** Vocabulary: carol: 卡罗尔

**[7586.02s] English:** And those researchers went to Google and Microsoft.  
**Translation:** 

**[7589.44s] English:** And there was no way to put Yahoo search back together.  
**Translation:** 

**[7592.52s] English:** So when Firefox tried switching all their users who'd stuck with a default from Google to Yahoo, it was like mid-December 2014, a bunch of users said, what just happened to my Firefox?  
**Translation:** 

**[7604.06s] English:** And others didn't notice right away, but over time they did.  
**Translation:** 

**[7606.32s] English:** And so over the next year, the traffic just went away for Yahoo.  
**Translation:** 

**[7611.24s] English:** And yet they were obliged.  
**Translation:** Vocabulary: obliged: 被迫

**[7613.46s] English:** I understand it.  
**Translation:** 

**[7614.18s] English:** I don't have inside knowledge, but this is leaked out and Danny Sullivan's written about it.  
**Translation:** Vocabulary: danny: 丹尼

**[7618.28s] English:** Search Engine Land.  
**Translation:** 

**[7618.88s] English:** And I think the deal was like fixed payments to Mozilla.  
**Translation:** 

**[7621.52s] English:** So Mozilla was getting a bunch of money for traffic that wasn't staying because users were resetting their default.  
**Translation:** 

**[7626.36s] English:** And this shows how defaults are important, but they have to be good enough that the user doesn't override them.  
**Translation:** Vocabulary: override: 覆盖取消

**[7632.68s] English:** And, you know, a lot of the commercial value in popular apps is what are the default settings?  
**Translation:** 

**[7638.06s] English:** What is the default search?  
**Translation:** 

**[7639.94s] English:** But oftentimes there's something just like you said.  
**Translation:** 

**[7641.90s] English:** I mean, if there's something compelling, that's also can beat out the default like tab browsing and so on.  
**Translation:** Vocabulary: browsing: 浏览; compelling: 吸引人的; oftentimes: 经常

**[7648.66s] English:** Yes.  
**Translation:** 

**[7648.88s] English:** And that's where, I mean, we'll talk about Brave browser.  
**Translation:** 

**[7652.34s] English:** It feels like now we're in this third stage where there's Chrome, Firefox, Edge, I guess it's called, and Brave.  
**Translation:** 

**[7664.56s] English:** And these all seem like really exciting, I don't know, innovative browsers.  
**Translation:** Vocabulary: browsers: 浏览器

**[7670.60s] English:** They're all kind of copying off of each other, picking up the good stuff.  
**Translation:** 

**[7673.76s] English:** There's evolution again, especially on tracking protection.  
**Translation:** 

**[7676.10s] English:** So privacy is this sort of global.  
**Translation:** 

**[7678.88s] English:** Right.  
**Translation:** 

**[7679.68s] English:** Right.  
**Translation:** 

**[7680.00s] English:** wave that's rising. I like to call it a wave because it's a large, somewhat chaotic structure.  
**Translation:** 

**[7686.80s] English:** It's not a unitary good. You can't say, I'm buying privacy for $3. I'm paying $3 for privacy. Some  
**Translation:** 

**[7692.84s] English:** people think a VPN does this and are disappointed when it fails them. But often people use VPNs for  
**Translation:** 

**[7698.20s] English:** region unlocking video or getting the US Netflix catalog. But privacy is not a unitary good. It's  
**Translation:** 

**[7704.84s] English:** complex and people are understanding it only over time and as they get burned. But there's a  
**Translation:** Vocabulary: unlocking: 解锁

**[7710.00s] English:** genie that's not going back in the bottle there. People are fed up. Apple has responded to this.  
**Translation:** 

**[7714.74s] English:** Apple was always making Safari, I think, more of a privacy branded browser from the very beginning.  
**Translation:** Vocabulary: genie: 瓶子中的精灵

**[7720.26s] English:** I think this is probably Steve Jobs. Safari had private windows, private tabs before  
**Translation:** 

**[7725.94s] English:** Firefox did. And these are only private in the sense that they don't leave local  
**Translation:** 

**[7731.38s] English:** traces if you don't want them to. Turns out Safari does keep them around between shutdown.  
**Translation:** 

**[7737.12s] English:** But the canonical model is no local traces after...  
**Translation:** Vocabulary: canonical: 标准模型; shutdown: 关机

**[7740.00s] English:** You close the private window, no leftover traces that you went to some site that you were  
**Translation:** 

**[7745.42s] English:** embarrassed by or bought a gift for somebody you wanted to keep secret.  
**Translation:** Vocabulary: leftover: 剩余

**[7749.92s] English:** But there's still some level of tracking.  
**Translation:** 

**[7751.82s] English:** There's network tracking. Network privacy is not guaranteed at all because you're using the same  
**Translation:** 

**[7757.96s] English:** internet and ISP as a public window, a non-private window. But Safari had that early on. They also  
**Translation:** 

**[7763.22s] English:** had a cookie blocking policy that might take a little explaining. If you know what a cookie is,  
**Translation:** 

**[7769.76s] English:** it's a little bit of a cookie. It's a little bit of a cookie. It's a little bit of a cookie.  
**Translation:** 

**[7770.00s] English:** It's a little bit of storage in the browser indexed by the name of the site.  
**Translation:** 

**[7773.34s] English:** And it's really only the main name of the site, like bfa.com or something like npr.org.  
**Translation:** 

**[7783.52s] English:** Every site can store some information in a cookie. Every time it's contacted by the browser,  
**Translation:** 

**[7788.60s] English:** the previous version is sent back. And in the response from the server, the cookie's updated.  
**Translation:** 

**[7794.02s] English:** So it's this little bit of storage in the browser that the site can keep updating and it can store  
**Translation:** 

**[7800.00s] English:** encrypted version of your login credentials with a timestamp so you can stay logged in without  
**Translation:** 

**[7806.12s] English:** having to retype your password every time you navigate which is how it would be if you didn't  
**Translation:** Vocabulary: credentials: 登录凭据; encrypted: 加密的; login: 登录; navigate: 浏览; retype: 重新输入; timestamp: 时间戳

**[7810.30s] English:** have cookies the web protocols uh especially in the 90s are so-called stateless protocols so  
**Translation:** 

**[7816.22s] English:** go to your bank you log in you go from your login confirmed page to your account view  
**Translation:** Vocabulary: stateless: 无状态的

**[7822.00s] English:** if you didn't have a cookie you'd be logging in again every time you type in so so that was a  
**Translation:** 

**[7827.06s] English:** great thing about cookies lou montulli did it in a hurry in 1994 before i joined that scape and he  
**Translation:** 

**[7831.02s] English:** did it for really holding that kind of credential um but even then there was the image element  
**Translation:** 

**[7837.46s] English:** embedded in the page and the image gets fetched possibly from a different server and that request  
**Translation:** Vocabulary: credential: 资格证明; embedded: 嵌入的

**[7842.76s] English:** carries the last cookie which could be empty at first and the response carries the updated cookie  
**Translation:** 

**[7847.58s] English:** so just by having images and cookies you got tracking because that image server can be  
**Translation:** 

**[7851.86s] English:** serving a little one by one pixel and they still use the word pixel on ad tech  
**Translation:** 

**[7855.88s] English:** and that pixel  
**Translation:** Vocabulary: pixel: 像素

**[7856.98s] English:** can be served from the same server embedded differently with different url spellings in  
**Translation:** 

**[7862.38s] English:** the new york times and espn and as you go from one to the other the image server can say i haven't  
**Translation:** Vocabulary: spellings: 拼写方式

**[7867.32s] English:** got a cookie for you it's empty initially i'm going to assign you user number one two three  
**Translation:** 

**[7870.86s] English:** four i'm going to put a database entry in and i see by the way i always fetch the name of the  
**Translation:** 

**[7875.02s] English:** path part of the url that i was in the new york times so you're a new york times reader and then  
**Translation:** 

**[7879.32s] English:** you hit espn same thing and the database gets updated and the number user one two three four  
**Translation:** 

**[7884.36s] English:** indexes in the database to a profile of you  
**Translation:** 

**[7886.98s] English:** have been tracked  
**Translation:** 

**[7888.20s] English:** this was not intended and it was too late to undo by the time i got the netscape i think  
**Translation:** 

**[7893.04s] English:** lou wanted to do twinkies he called them and he was trying to solve several problems he  
**Translation:** Vocabulary: netscape: 网景浏览器; twinkies: twinkies

**[7897.54s] English:** wanted them to be bigger because initially cookies had a short size limit i think he  
**Translation:** 

**[7900.80s] English:** wanted to solve the third-party problem but tom paquin the engineering manager said nope  
**Translation:** 

**[7905.66s] English:** no twinkies just cookies we're done you're done son and um that's how a lot of that stuff  
**Translation:** 

**[7911.42s] English:** was that's how javascript you know um got frozen like a flying amber in some ways with  
**Translation:** Vocabulary: amber: 琥珀

**[7915.98s] English:** sloppy equality operator that i made because the early adopters and the cookie got stuck  
**Translation:** 

**[7920.00s] English:** with this tracking hazard and then because javascripts can be like images they're embedded  
**Translation:** Vocabulary: adopters: 早期采用者; javascripts: 脚本

**[7924.62s] English:** in the page by the time in netscape 3 i made that work uh you can get a request with the last cookie  
**Translation:** 

**[7930.38s] English:** value and the response updates it that's a tracking mechanism and that's why you don't even need  
**Translation:** 

**[7934.06s] English:** images to track now you just use scripts so this whole tracking uh economy evolved and it it it  
**Translation:** 

**[7940.94s] English:** depended on these accidents of the 90s these unintended consequences well it created some  
**Translation:** Vocabulary: unintended: 意外结果

**[7946.20s] English:** of the richest companies in the world right i mean it's the social media all i got was t-shirts  
**Translation:** 

**[7949.68s] English:** all i got is this crappy t-shirt yeah yeah uh i mean uh so that's that's the fundamental problem  
**Translation:** Vocabulary: crappy: 糟糕的

**[7958.34s] English:** the world is facing now they're looking at what social media has created and they're looking  
**Translation:** 

**[7962.76s] English:** at and like a world is looking at itself in the mirror and uh seeing that privacy is actually  
**Translation:** 

**[7969.50s] English:** something as opposed to like a nice thing to have it's something that is actually should be  
**Translation:** 

**[7976.54s] English:** fundamental to the way we interact with the world  
**Translation:** 

**[7979.12s] English:** as part of our tooling and that's where the brave browser comes in and i suppose others as well  
**Translation:** 

**[7985.06s] English:** playing with this idea but brave is at the forefront of that so maybe can you like describe  
**Translation:** Vocabulary: forefront: 前沿

**[7989.88s] English:** what brave is yes and what are its key principles and uh what's broken what is it brave trying to  
**Translation:** 

**[7995.74s] English:** fix so when i realized that these accidents like the third-party cookie the image or script that's  
**Translation:** 

**[8001.36s] English:** tracking you or the um this javascripts that can do it invisibly now that all this stuff wasn't  
**Translation:** 

**[8007.18s] English:** intended and the javascripts that can do it invisibly now that all this stuff wasn't intended  
**Translation:** Vocabulary: invisibly: 看不见地

**[8007.66s] English:** and the javascripts that can do it invisibly now that all this stuff wasn't intended and the  
**Translation:** 

**[8009.10s] English:** that firefox had supported extensions that block some of these things i thought  
**Translation:** Vocabulary: extensions: 插件

**[8012.94s] English:** probably we should have browsers just block some of these things by default these were  
**Translation:** 

**[8017.92s] English:** not intended and they're now unsafe they're tracking you there could be data breaches  
**Translation:** Vocabulary: breaches: 数据泄露; browsers: 浏览器

**[8021.56s] English:** malware distribution um you know bullying and psyops and other attacks on people um  
**Translation:** 

**[8029.06s] English:** block that stuff block that javascript i'm dr frankenstein i've got a monster here  
**Translation:** 

**[8034.28s] English:** but obviously you go to gmail there's so much a script there to make that amazing web client  
**Translation:** 

**[8039.10s] English:** but obviously you go to gmail there's so much a script there to make that amazing web client  
**Translation:** 

**[8040.00s] English:** okay, that's first party JavaScript. So how do you tell the first from the third party? And it's not  
**Translation:** 

**[8044.42s] English:** easy. It's not a matter of just what's embedded from a different server because a lot of publishers  
**Translation:** Vocabulary: embedded: 嵌入的

**[8049.68s] English:** use benign scripts from unrelated domains or apparently unrelated domains. So you end up  
**Translation:** 

**[8054.80s] English:** having to develop a sort of human and machine learning practice around blocking. And at Brave,  
**Translation:** Vocabulary: benign: 良性

**[8061.10s] English:** we did that from the start and built a research team to help drive it and automate it. We realized  
**Translation:** 

**[8066.16s] English:** that protecting people needed machine learning. And around 2017 spring, I talked to my friends  
**Translation:** Vocabulary: automate: 自动化

**[8071.36s] English:** at Apple about this too. And they were also doing what they call intelligent tracking prevention,  
**Translation:** 

**[8076.12s] English:** which uses local machine learning in the browser. And the funny thing is, you know,  
**Translation:** 

**[8081.62s] English:** great minds think alike. They were taking their third party cookie blocker that was in Safari  
**Translation:** 

**[8085.36s] English:** from the old days and making it not have a big loophole. Because what they did was in 2003,  
**Translation:** Vocabulary: loophole: 漏洞

**[8091.04s] English:** when Safari came out, they said, we're going to block cookies that are from those third party  
**Translation:** 

**[8095.94s] English:** embedded elements where you've never visited that site before. So I'm going to pick an ad company  
**Translation:** 

**[8101.32s] English:** that got sold to AT&T. So I'm not picking on anybody unfairly. AppNexus.com. Have you ever  
**Translation:** 

**[8105.46s] English:** been to AppNexus.com? I've never been there, but I guarantee you 10 years ago, you probably had,  
**Translation:** Vocabulary: unfairly: 不公平地

**[8110.16s] English:** if you're using Firefox, you had a cookie, third party cookie, because you're being tracked by them.  
**Translation:** 

**[8114.74s] English:** And they were using that cookie to build up a profile of you. In Safari, as long as the user  
**Translation:** 

**[8119.28s] English:** never went to AppNexus, that cookie would not be set. And that was a real move for privacy early on  
**Translation:** 

**[8125.24s] English:** when Java was first launched. And that's what we're doing. And that's what we're doing. And that's  
**Translation:** 

**[8125.94s] English:** still around in Safari. But it had this loophole that if you do go to AppNexus, then why it's okay  
**Translation:** 

**[8131.44s] English:** to be a third party cookie. And so AppNexus did something very naughty. They took their ad partners  
**Translation:** 

**[8136.72s] English:** that put the actual ad you click on. And they said, hey, add a little script so that when somebody  
**Translation:** 

**[8142.00s] English:** clicks on the ad before it goes to your landing page, redirect to AppNexus and we'll redirect to  
**Translation:** 

**[8146.44s] English:** the landing page. And by doing that, they set a first party cookie and they got whitelisted. So  
**Translation:** 

**[8150.04s] English:** as a loophole, they exploited intelligent tracking prevention in Safari was sophisticated enough to  
**Translation:** Vocabulary: exploited: 利用; sophisticated: 复杂; whitelisted: 列入白名单

**[8155.12s] English:** counteract this and it did other things and it's evolved since they did. And we've evolved.  
**Translation:** 

**[8160.00s] English:** brave too and so when i say machine and human learning there's a real um set of techniques  
**Translation:** Vocabulary: counteract: 抵消

**[8165.22s] English:** here they have to fight this is a fascinating problem fingerprinting right anytime you have  
**Translation:** 

**[8168.96s] English:** a little bit of storage in the browser associated with a website if the bad guy can get 32 websites  
**Translation:** Vocabulary: anytime: 任何时间; fingerprinting: 指纹识别

**[8175.28s] English:** each one has a bit of storage that's 32 bits you can turn the bit on or off you can make  
**Translation:** 

**[8180.16s] English:** four billion numbers you can make an identifier it's called a super cookie sometimes uh it's a  
**Translation:** Vocabulary: identifier: 标识符

**[8185.36s] English:** there are weaker ways that are statistical they're called fingerprinting you have to block  
**Translation:** 

**[8190.26s] English:** all of them and you have to not only automate you want to work in the web standards body to  
**Translation:** Vocabulary: automate: 自动化

**[8195.26s] English:** put privacy in by default by design from the get-go not added as an afterthought or  
**Translation:** 

**[8200.70s] English:** you know go hog wild with new web apis that add a bunch more local storage or fingerprint surface  
**Translation:** Vocabulary: afterthought: 事后想法; fingerprint: 指纹识别

**[8206.50s] English:** area and that's been a struggle too because guess who's the new microsoft in the standards body it's  
**Translation:** 

**[8211.84s] English:** google and they're not in favor of privacy  
**Translation:** 

**[8215.36s] English:** first they they want to do privacy their way only under i would say market pressure but with apple  
**Translation:** 

**[8222.02s] English:** uh and with brave leading the way we we block third-party cookies almost without exception so  
**Translation:** 

**[8226.50s] English:** we've just blocked them and that gives us a very strong privacy uh benefit but it also means some  
**Translation:** 

**[8232.36s] English:** sites just don't work right embedded youtube videos might not work right so we're adapting  
**Translation:** 

**[8236.94s] English:** in similar way to apple's done with itp to make um third-party cookies blocked but to sort of  
**Translation:** 

**[8244.14s] English:** simulate the  
**Translation:** Vocabulary: simulate: 模拟

**[8245.36s] English:** what looks like a working third-party cookie for the site it essentially tries to partition each  
**Translation:** 

**[8251.84s] English:** site and its third parties into its own sort of cookie jar got it and so and like like you said is  
**Translation:** Vocabulary: partition: 划分

**[8257.18s] English:** this both like a human uh fine-tuning issue and a machine learning problem so and as you as the  
**Translation:** 

**[8263.50s] English:** humans learn then they train the machine learning but you know uh maybe google side or including  
**Translation:** 

**[8269.40s] English:** google there's millions of dollars if not be billions of dollars to be made from  
**Translation:** 

**[8275.36s] English:** fighting the ways of brave that's right and it's been uh interesting  
**Translation:** 

**[8280.00s] English:** change from when we started in 2015 when we started you know ad blocking extensions adblock  
**Translation:** 

**[8284.74s] English:** plus was one of the big ones that started on firefox in 2006 i believe had gotten to a certain  
**Translation:** Vocabulary: extensions: 扩展程序

**[8289.60s] English:** level of use around the world and browsers like uc web uc browser in asia had some amount of ad  
**Translation:** 

**[8295.22s] English:** blocking built in and on by default so a page fair was a startup uh and they measured ad blocking  
**Translation:** Vocabulary: browsers: 浏览器

**[8302.40s] English:** adoption and they tried to say hey publishers you're you know 30 of the visitors to uh pitchfork  
**Translation:** 

**[8309.54s] English:** or wire to kind of nas properties are using ad blockers if we can somehow convince them to lower  
**Translation:** Vocabulary: pitchfork: 反讽例

**[8314.72s] English:** their ad blocking for your site that could be like a 43 lift right um and three sevenths well  
**Translation:** 

**[8322.30s] English:** that's easier said than done and page fair and others source point that many others tried to  
**Translation:** 

**[8327.04s] English:** either smuggle ads through or cajole the user into letting you know ads appear and it didn't  
**Translation:** 

**[8332.68s] English:** really work and meanwhile the ad blocking adoption has just continued intelligent tracking prevention  
**Translation:** Vocabulary: cajole: 哄骗; smuggle: 走私

**[8336.76s] English:** safari in 2017  
**Translation:** 

**[8339.54s] English:** the ad blocker has been a rave from 2016 on with very strong cookie blocking and other protections  
**Translation:** 

**[8343.82s] English:** and this this is not going away the publishers used to rage against it like we would try to say  
**Translation:** 

**[8349.58s] English:** we can help you you're dealing with users who are already blocking all your ads we can try to put  
**Translation:** 

**[8355.26s] English:** back uh some economics that help the user and you that led to the basic attention token that we  
**Translation:** 

**[8360.16s] English:** started with bitcoin we can be your friend don't don't just fingerprint us as an ad blocker and  
**Translation:** Vocabulary: fingerprint: 追踪记录; token: 令牌币

**[8365.06s] English:** treat us as an enemy but in 2015 or 16 it was like nah you're an ad blocker you're not an ad blocker  
**Translation:** 

**[8369.54s] English:** get out of here i hate you and by 2017 or 18 it's like something's happening the ad blocking is not  
**Translation:** 

**[8374.50s] English:** stopping and we're all getting sort of pulled on the google's plantation through amp amp or you  
**Translation:** 

**[8381.84s] English:** know we're getting killed by the google ad system we use because it's taking all the revenue or you  
**Translation:** 

**[8386.92s] English:** know it's permitting or some other vendors we use are permitting ad fraud and so a fake new york  
**Translation:** 

**[8391.46s] English:** times is getting paid by the marketer running an ad that a bot clicks on and the real new york times  
**Translation:** 

**[8398.06s] English:** it's supposed to get that it doesn't get it it's supposed to get that it doesn't get it it doesn't  
**Translation:** 

**[8399.54s] English:** get it  
**Translation:** 

**[8405.70s] English:** you  
**Translation:** 

**[8400.00s] English:** and there's something really broken about that kind of system and that that fraud is mediated  
**Translation:** Vocabulary: mediated: 调和

**[8405.60s] English:** through google's ad exchange which is the biggest of them all and google takes a fee there's a flip  
**Translation:** 

**[8410.30s] English:** side of that which is malware distribution malvertising where fake advertisers put malware  
**Translation:** Vocabulary: advertisers: 广告商; malvertising: 恶意广告

**[8415.60s] English:** payloads in or exploit kit loaders in javascript and they smuggle them in ads onto real publisher  
**Translation:** 

**[8421.40s] English:** pages the ad exchange takes the fee now i'm not a lawyer i'm not going to say this is a rico  
**Translation:** Vocabulary: payloads: 载荷

**[8426.60s] English:** predicate but why is the ad exchange facilitating fraud and malware distribution and taking a fee  
**Translation:** 

**[8431.98s] English:** it's not right as opposed to just fighting this is the really interesting thing about brave is  
**Translation:** Vocabulary: facilitating: 促进; predicate: 谓词

**[8435.80s] English:** as opposed to just fighting and then being treated like an ad blocker you're providing an alternate  
**Translation:** 

**[8441.16s] English:** there's a there's a philosophical idea here that might change the nature of the internet with the  
**Translation:** Vocabulary: philosophical: 哲学上的

**[8447.82s] English:** basic attention token yes maybe what is basic attention token bat and how does it work okay  
**Translation:** 

**[8455.44s] English:** i'll tell the story first  
**Translation:** 

**[8456.58s] English:** by saying how i came to it i realized for a long time at firefox we were dependent on this google  
**Translation:** 

**[8462.20s] English:** search deal and i thought you know now that chrome's out maybe that's going to go away  
**Translation:** 

**[8466.80s] English:** and they just at some point google will say you know firefox you know like old yeller you saved  
**Translation:** 

**[8473.42s] English:** me from the rabid beast now you have to shoot you in the head yeah done your job sad but true goodbye  
**Translation:** Vocabulary: goodbye: 再见; rabid: 狂躁的; yeller: 小黄人

**[8478.94s] English:** and what could we do and i think this mozilla doesn't know what to do this is something that  
**Translation:** 

**[8484.98s] English:** i couldn't solve there and i don't think they can solve it  
**Translation:** 

**[8486.58s] English:** but i thought why is the browser the sort of passive servant of these big tech companies  
**Translation:** 

**[8492.18s] English:** why is it a blind runtime for ad tech javascripts including from google why doesn't it block some  
**Translation:** Vocabulary: javascripts: 脚本; runtime: 运行时

**[8499.14s] English:** and if it blocks some why can't it reconnect users readers fans with publishers creators  
**Translation:** 

**[8506.46s] English:** websites uh why can't it help people make direct payments or even possibly get an ad revenue share  
**Translation:** Vocabulary: reconnect: 重新连接

**[8513.90s] English:** for private ads that are placed in the browser the ads are the same thing they're the same thing they're  
**Translation:** 

**[8516.58s] English:** all placed in the browser some people have this sort of model that the server's painting  
**Translation:** 

**[8520.00s] English:** ad into some flash combined package or into some giant image, and then it all gets sent down.  
**Translation:** 

**[8527.62s] English:** That's not how it works. All the ads you see on the web are placed in your browser by calling out  
**Translation:** 

**[8532.12s] English:** to various ad tech partners, and Google's among them. And so if you block those scripts, you break  
**Translation:** 

**[8538.38s] English:** the advertising flow of money from the brands and their agencies to the publishers. And if you want  
**Translation:** 

**[8547.10s] English:** to reconnect it directly with the user, you have limited choices. The user generally isn't going to  
**Translation:** 

**[8551.48s] English:** sign up with a ACH bank connection or a credit card. The publisher isn't going to sign up the  
**Translation:** 

**[8557.02s] English:** user except as a subscriber, and then they're going to overcharge you because they want you  
**Translation:** 

**[8560.52s] English:** to cross-subsidize all the content and buy more than you read and all that stuff. People are doing  
**Translation:** Vocabulary: overcharge: 漫天要价; subscriber: 付费用户

**[8565.92s] English:** great who are big names like New York Times and The Washington Post, but how many subscriptions  
**Translation:** 

**[8569.74s] English:** are you as a user going to pay for? This is why startups like Tony Hale's Scroll are trying to do  
**Translation:** Vocabulary: scroll: 滚动新闻; startups: 初创公司

**[8574.84s] English:** a portable subscription system.  
**Translation:** 

**[8577.10s] English:** By the way, just on a small tangent there, even the New York Times, it's really annoying how  
**Translation:** Vocabulary: subscription: 订阅; tangent: 旁白

**[8581.08s] English:** difficult it is just to subscribe. There's way too many clicks.  
**Translation:** 

**[8584.60s] English:** They don't make it easy. I had friends a few years ago, I think they fixed this, who would pay for  
**Translation:** Vocabulary: subscribe: 订阅

**[8587.58s] English:** the paper, and then they'd go online and they'd get upcharged for the digital, and there was no  
**Translation:** 

**[8592.76s] English:** break. There was no connection between them. But publishers are not that technical, and they can't  
**Translation:** Vocabulary: upcharged: 多收费

**[8598.46s] English:** all get you to subscribe. You can't have 1,000 subscriptions. So for a long time, people talked  
**Translation:** 

**[8602.34s] English:** about micropayments. There was Blendle and other ones which came to the US but didn't grow.  
**Translation:** 

**[8607.10s] English:** And I thought, if you have just a browser and it's protecting you by blocking all this ad tech  
**Translation:** 

**[8611.84s] English:** tracking junk, it can provide you an option that uses cryptocurrency to let you support your  
**Translation:** Vocabulary: cryptocurrency: 加密货币

**[8617.78s] English:** favorite sites and even YouTube channels. And that we prototyped with Bitcoin. And that meant the  
**Translation:** 

**[8623.42s] English:** user had to be of means to contribute and willing to contribute. But it could be done on the Bitcoin  
**Translation:** Vocabulary: prototyped: 原型

**[8628.54s] English:** blockchain, and it could be fairly efficient, even though Bitcoin went through a period when we had  
**Translation:** 

**[8632.52s] English:** this prototype running in 2016 into 2017, where Bitcoin was very congested.  
**Translation:** Vocabulary: congested: 拥堵; prototype: 原型

**[8637.10s] English:** And very slow to confirm, and the fees got very high.  
**Translation:** 

**[8640.00s] English:** Um, and a lot of users who were not Bitcoin maximalist or even experienced, we helped  
**Translation:** Vocabulary: maximalist: 比特币极客

**[8645.44s] English:** them out by embedding a Coinbase buy widget and they had the income to buy, but it was  
**Translation:** 

**[8649.72s] English:** hard.  
**Translation:** Vocabulary: coinbase: 加密货币交易所; embedding: 嵌入; widget: 小部件

**[8650.14s] English:** It was like, do I buy $5 a month?  
**Translation:** 

**[8652.12s] English:** But the fee is like $4.50.  
**Translation:** 

**[8654.08s] English:** I better buy in larger batches, right?  
**Translation:** 

**[8656.10s] English:** And they're like, I don't want to own that much Bitcoin.  
**Translation:** 

**[8658.40s] English:** So it became this, this painful thing.  
**Translation:** 

**[8660.90s] English:** And the real idea that I had of private ads that pay the user a rev share couldn't be  
**Translation:** 

**[8666.34s] English:** realized alone in that kind of system.  
**Translation:** 

**[8670.36s] English:** In these cryptocurrency systems, especially with the blockchain, we switched to Ethereum.  
**Translation:** Vocabulary: ethereum: 以太坊

**[8675.18s] English:** You can have smart contracts.  
**Translation:** 

**[8676.94s] English:** The Bitcoin system is not turned complete.  
**Translation:** 

**[8679.00s] English:** So what you can do with the script is more limited, but you can still do sort of clever  
**Translation:** 

**[8683.38s] English:** things.  
**Translation:** 

**[8683.88s] English:** Um, even with Bitcoin script, what we wanted to do was sort of a three-sided ecosystem.  
**Translation:** 

**[8689.14s] English:** We wanted users, creators or publishers and advertisers, and we wanted the advertisers  
**Translation:** Vocabulary: advertisers: 广告商

**[8694.96s] English:** to put money in just like they do today, but without going through the Googles and the  
**Translation:** 

**[8699.24s] English:** app next.  
**Translation:** 

**[8700.08s] English:** This isn't all these other ad tech companies because those companies take out a huge cut.  
**Translation:** 

**[8704.14s] English:** The guardian in the UK once did an experiment for a month.  
**Translation:** 

**[8707.00s] English:** They bought out their own ad space.  
**Translation:** 

**[8708.48s] English:** They put in a pound and they were paid 30 pence.  
**Translation:** 

**[8711.36s] English:** 70% was coming out to the intermediary vendors they were using.  
**Translation:** 

**[8715.84s] English:** Um, and that's like the opposite of what the app store does.  
**Translation:** Vocabulary: intermediary: 中间商

**[8719.30s] English:** The app store takes 30% and gives the publisher 70%.  
**Translation:** 

**[8722.20s] English:** So pretty broken in the old days of the superstation TBS, the media, um, owner would get 85%.  
**Translation:** Vocabulary: superstation: 超级电视频道

**[8729.84s] English:** So these splits have become really unbalanced and the middle players, the, the ad tech vendors  
**Translation:** 

**[8735.66s] English:** are taking out way too much money and they're, they're doing something worse, which has been  
**Translation:** Vocabulary: unbalanced: 不平衡

**[8739.34s] English:** noticed.  
**Translation:** 

**[8740.34s] English:** They're, they're letting, um, not just the malware vendors, but also the ad fraud side,  
**Translation:** 

**[8745.60s] English:** which fakes the publishers and clickbait merchants, uh, come in and steal traffic from good sites.  
**Translation:** 

**[8753.42s] English:** Because once you have a certain audience identified at one site, Jason Calacanis told me this about  
**Translation:** Vocabulary: calacanis: 卡拉坎尼斯; clickbait: 诱饵标题

**[8757.64s] English:** his experience with, I guess it was in gadget.  
**Translation:** 

**[8759.84s] English:** Uh,  
**Translation:** Vocabulary: gadget: 小玩意儿

**[8760.00s] English:** I can't remember which site he was running, but once he started using an ad partner that was sharing his audience information across multiple sites, he saw his competitors stealing all his traffic.  
**Translation:** 

**[8769.78s] English:** And then what's worse is the clickbait sites that just have much cheaper rates steal all that traffic.  
**Translation:** 

**[8775.52s] English:** And that facilitates fraud, it facilitates fake news, all sorts of problems.  
**Translation:** 

**[8781.86s] English:** So Grave blocks it, and then we give users the ability to give back.  
**Translation:** Vocabulary: facilitates: 促进

**[8786.14s] English:** And because we invented the basic attention token in Ethereum, we can do this three-way split, and we can give users a share of the revenue.  
**Translation:** 

**[8793.82s] English:** And if they want to take it out, they can.  
**Translation:** Vocabulary: ethereum: 以太坊; token: 代币

**[8795.74s] English:** Now, unfortunately for us and for all of blockchain, the regulators are saying, we're going to have to know who you are.  
**Translation:** 

**[8801.24s] English:** There's the Treasury Department's FinCEN agency.  
**Translation:** Vocabulary: regulators: 监管机构

**[8807.40s] English:** There's the Office of Foreign Asset Control's OFAC.  
**Translation:** 

**[8810.76s] English:** There's the other regulators in the federal government that take over.  
**Translation:** 

**[8816.14s] English:** There's a very dark look at things like money laundering and sending money to someone named Osama bin Laden.  
**Translation:** 

**[8821.38s] English:** So compliance starts to come in.  
**Translation:** Vocabulary: laden: 装载; laundering: 洗钱

**[8823.52s] English:** And even now, they're threatening for pure Bitcoin, sending to some address.  
**Translation:** 

**[8827.76s] English:** If you're a Coinbase, you're going to have to know who's at that address.  
**Translation:** Vocabulary: coinbase: 比特币矿工奖励

**[8831.42s] English:** Like the actual identities of people involved.  
**Translation:** 

**[8833.90s] English:** Now, with Coinbase members, you sign up and they know you, and they comply with the regulations.  
**Translation:** 

**[8836.98s] English:** They're a regulated money services business.  
**Translation:** 

**[8841.32s] English:** But if somebody's using their own self-custody, so-called,  
**Translation:** Vocabulary: regulated: 受监管的

**[8846.14s] English:** self-custodial wallet, where they have the hardware private key and they're not named and they want to send to that address,  
**Translation:** 

**[8853.58s] English:** our friends in the federal government are talking about requiring at some threshold, knowing who that is.  
**Translation:** Vocabulary: threshold: 门槛

**[8857.52s] English:** So some threshold that's unreasonable.  
**Translation:** 

**[8860.42s] English:** It's not that big.  
**Translation:** Vocabulary: unreasonable: 不合情理

**[8862.14s] English:** Yeah.  
**Translation:** 

**[8862.64s] English:** I don't know how this will play out.  
**Translation:** 

**[8863.48s] English:** I think crypto is here to stay.  
**Translation:** 

**[8864.80s] English:** I think the beauty of being able to send peer to peer without any bank in the middle, without any huge wire charge and two day delay and all that nonsense is beautiful.  
**Translation:** Vocabulary: crypto: 加密货币

**[8872.96s] English:** And I've used it and I love it.  
**Translation:** 

**[8874.28s] English:** But we're pragmatists that are brave about crypto.  
**Translation:** Vocabulary: pragmatists: 实用主义者

**[8876.14s] English:** And we realize that anything like a revenue split, we can't.  
**Translation:** 

**[8880.00s] English:** facilitate without being licensed in a certain way, and it requires knowing who the user is.  
**Translation:** Vocabulary: facilitate: 促进

**[8883.64s] English:** So our default mode doesn't know who the user is. It instead imputes to the user's browser  
**Translation:** 

**[8888.76s] English:** some of the revenue and allows that browser to steer it back to the creators. And we do have  
**Translation:** 

**[8895.38s] English:** to identify the creators. But as things improve, and who knows how it'll play out,  
**Translation:** 

**[8900.58s] English:** there should come a day when this full vision can be done more fully on a blockchain. But regulations  
**Translation:** 

**[8906.50s] English:** and the practicalities of today's blockchains, which are not that fast and not anonymous over  
**Translation:** 

**[8912.36s] English:** time, you fingerprint yourself over time, we do some of this with the browser.  
**Translation:** Vocabulary: blockchains: 区块链; fingerprint: 留下痕迹; practicalities: 实用性

**[8916.30s] English:** So one of the ideas of the basic attention token is to make a hybrid system that's stronger than  
**Translation:** 

**[8922.60s] English:** blockchain alone. It's the browser and the blockchain. And the browser is this trusted  
**Translation:** Vocabulary: token: 令牌

**[8927.36s] English:** endpoint software. It's this universal app. Everyone uses browsers. The bigger the screen,  
**Translation:** 

**[8931.94s] English:** the more you're in the browser and the less you install fat clients for things.  
**Translation:** Vocabulary: browsers: 浏览器; endpoint: 端点

**[8935.66s] English:** I use  
**Translation:** 

**[8936.42s] English:** Slack on macOS, and it's like a browser. It's based on an Electron framework we used to use.  
**Translation:** 

**[8942.16s] English:** And it's just, it's not that great. Some of the people at Brave use Slack in Brave as a-  
**Translation:** 

**[8947.70s] English:** In the browser, yeah.  
**Translation:** 

**[8948.42s] English:** In the browser, yeah.  
**Translation:** 

**[8949.00s] English:** I use that often, yeah.  
**Translation:** 

**[8950.22s] English:** And I noticed on the iPad, I use apps less. The smaller the screen,  
**Translation:** 

**[8954.82s] English:** the browser got handicapped by Apple and Android both. And it also can be slower or not have the  
**Translation:** 

**[8961.58s] English:** right affordances to your interface with the security limited APIs.  
**Translation:** 

**[8966.42s] English:** But in principle, with the right permissioning, you can make the web browser just as good as any app.  
**Translation:** Vocabulary: affordances: 功能提示; interface: 界面; permissioning: 权限管理

**[8971.68s] English:** You make it be a super app. And that's part of our mission at Brave. So we want to have the  
**Translation:** 

**[8976.40s] English:** economics that got captured by these big tech companies through tracking and through social  
**Translation:** 

**[8980.64s] English:** networks. We want to block that for your own safety and then let you opt into a cleaner world  
**Translation:** 

**[8985.00s] English:** where you keep your data defended in your browser and you can actually realize value from it.  
**Translation:** 

**[8989.82s] English:** So the way our ad system works, I mentioned it being private, but how does that work?  
**Translation:** 

**[8993.06s] English:** We don't see your data at all. All browsers,  
**Translation:** 

**[8995.62s] English:** are sort of the mother of all data feeds, your history, all your searches at all.  
**Translation:** 

**[9000.00s] English:** engines each engine sees the queries you send to it but it doesn't see the others but the browser  
**Translation:** 

**[9003.96s] English:** sees them all machine learning in the browser that you can opt into can study all that in a  
**Translation:** 

**[9008.84s] English:** very complete way and do a better job than google does google has you know cookie and scripts across  
**Translation:** 

**[9014.52s] English:** the web from acquiring double click they have youtube they have android they have search which  
**Translation:** 

**[9019.80s] English:** is still their big revenue lane but they don't see everything the browser sees everything and  
**Translation:** 

**[9023.84s] English:** if it can do a good job locally and this is not advanced machine learning this is not tensorflow  
**Translation:** 

**[9027.92s] English:** this is like svms now naive bays then you can match intense signals intense signals from those  
**Translation:** Vocabulary: naive: 幼稚

**[9036.52s] English:** data fees searches the queries the history how much you're scrolling down a page how much you  
**Translation:** 

**[9042.16s] English:** redid a search it's all blind browser algorithm we don't see that data and then pick the best  
**Translation:** Vocabulary: algorithm: 算法; scrolling: 滚动

**[9048.18s] English:** ad from a fixed catalog per day and the catalog is fixed across a large population per day and  
**Translation:** 

**[9053.52s] English:** only updates the date once a day because new offers come in and old ones where  
**Translation:** 

**[9057.12s] English:** sometimes  
**Translation:** 

**[9057.88s] English:** every week or every month and that catalog and there can be many such catalogs is sold by our  
**Translation:** Vocabulary: catalogs: 目录册

**[9064.46s] English:** direct sales team and so we're making an anonymous audience available to advertisers without the  
**Translation:** 

**[9070.64s] English:** advertisers tracking them instead each browser is a little machine learning system that's picking  
**Translation:** Vocabulary: advertisers: 广告商

**[9075.72s] English:** the best catalog entry now the catalog is not the ads those are big right it's a video or a web page  
**Translation:** 

**[9080.32s] English:** it's just the link to an edge cache and there are many such edge caches we're not trying to  
**Translation:** Vocabulary: cache: 缓存; caches: 缓存

**[9084.50s] English:** protect them from seeing your ip address it's not really feasible we could use tor but we don't yet  
**Translation:** 

**[9089.32s] English:** and some keywords about the ad so it's basically like metadata and a link and that's what the  
**Translation:** Vocabulary: feasible: 可行; keywords: 关键词; metadata: 元数据

**[9095.42s] English:** catalog consists of and that's what the machine learning picks and the machine learning is  
**Translation:** 

**[9098.50s] English:** learning about you specifically locally yes in order to choose from the catalog of different ads  
**Translation:** 

**[9103.78s] English:** couldn't this possibly be like a multi-billion dollar isn't this taking on the google ad ad  
**Translation:** 

**[9110.90s] English:** so like what i mean one question to ask  
**Translation:** 

**[9113.78s] English:** there seems to be some really profound ideas here that that are different than what the internet  
**Translation:** 

**[9120.00s] English:** grown up to be if brave or something like brave the idea is the fundamental philosophical ideas  
**Translation:** Vocabulary: philosophical: 哲学的; profound: 深邃的

**[9127.46s] English:** underlying brave win out and runs 95 of the internet how does that change uh the what what  
**Translation:** 

**[9137.70s] English:** are the major things these changes about the internet so social networks and then the creatives  
**Translation:** Vocabulary: creatives: 创意人士

**[9141.56s] English:** like youtube creators and all that kind of stuff so let's talk about that first of all if brave  
**Translation:** 

**[9145.20s] English:** gets 95 i'm going to demand a recount because i i won't believe it uh i don't know i i think uh  
**Translation:** 

**[9150.90s] English:** we're trying to put things into web standards that can be standardized across browsers so  
**Translation:** 

**[9155.16s] English:** the main value of brave will be the trust users have in us and our ability to give the best deal  
**Translation:** Vocabulary: browsers: 浏览器; standardized: 标准化

**[9160.80s] English:** to users so 70 of the gross ad revenue we give to the user and if they go through that kyc process  
**Translation:** 

**[9167.58s] English:** i mentioned they can take it out they can also give it back they could take some out give the  
**Translation:** 

**[9170.82s] English:** rest back they can add basic attention tokens to give back some of them  
**Translation:** 

**[9175.14s] English:** they can take some out give the rest back they can add basic attention tokens to give back  
**Translation:** 

**[9175.18s] English:** and turn off the ads because you just don't like ads but they put in 20 a month so i believe  
**Translation:** 

**[9179.38s] English:** zuko of zcash frame does that and that's very generous because the browser is just anonymously  
**Translation:** Vocabulary: anonymously: 匿名地

**[9183.98s] English:** based on his browsing sort of keeping score on how much time he spent on this video on that website  
**Translation:** 

**[9189.00s] English:** and if those sites verify in sort of a like getting a domain certificate fashion they can  
**Translation:** Vocabulary: browsing: 浏览; verify: 验证

**[9195.48s] English:** get paid they can get uh part of his 20 a month so that vision could go big and if it does i hope  
**Translation:** 

**[9202.12s] English:** it's across multiple browsers i don't know that uh they'll all be able to get paid but i think  
**Translation:** 

**[9205.16s] English:** they'll all compete well on the quality of the ads the quality of the ad blocking and tracking  
**Translation:** 

**[9209.48s] English:** protection those those are subject to competition it'll take a while to standardize them but i think  
**Translation:** 

**[9214.10s] English:** that would be a better world it would have less counterparty risk fewer fee takers in the middle  
**Translation:** 

**[9219.68s] English:** really just the browser we're taking 30 percent um sort of the app store app store split and if  
**Translation:** Vocabulary: counterparty: 交易对手; takers: 收费方

**[9225.02s] English:** we get bigger maybe we can take even less social networks creators if you look at youtubers a lot  
**Translation:** 

**[9231.02s] English:** of them are the indies that are getting some size are getting sponsored by the internet and they're  
**Translation:** Vocabulary: indies: 独立创作者; youtubers: 视频创作者

**[9235.10s] English:** doing a lot of sponsorship deals uh they're using patreon they're encouraging people  
**Translation:** 

**[9240.00s] English:** to subscribe and give them regular money through patreon but that centralized your patreon so  
**Translation:** Vocabulary: sponsorship: 赞助; subscribe: 订阅

**[9246.18s] English:** there's censorship hazards there's a five percent fee what if that were web standard what if brave  
**Translation:** 

**[9251.50s] English:** pioneered at first and we took three percent and we did it in a way that was through your browser  
**Translation:** Vocabulary: censorship: 审查制度; pioneered: 开创

**[9257.32s] English:** so we couldn't censor it um that's brilliant yeah do you think it could be standardized the cross  
**Translation:** 

**[9262.18s] English:** browsers can like internet explorer come in again and uh the protocols are easy to copy and that  
**Translation:** Vocabulary: censor: 审查; explorer: 浏览器

**[9268.14s] English:** are meant to be interoperable so it's there's a risk there and the loyal users might be tricked  
**Translation:** 

**[9273.28s] English:** into leaving you or they might because of that distribution power you might end up getting  
**Translation:** Vocabulary: interoperable: 可以互操作的

**[9277.02s] English:** stomped um i don't know i can't predict the future i think antitrust is back on the case finally in  
**Translation:** 

**[9281.84s] English:** the u.s and and certainly in europe gg comp is doing its thing so i'm hopeful that we'll have  
**Translation:** Vocabulary: antitrust: 反垄断

**[9286.40s] English:** a period of innovation uh you know people were talking like elizabeth warren was talking about  
**Translation:** 

**[9290.76s] English:** breaking up the tech tech companies very clearly um now she didn't win and i suspect that won't  
**Translation:** 

**[9296.20s] English:** happen but i also suspect that google might be smart  
**Translation:** 

**[9298.14s] English:** enough to see they should do something more than just put privacy perfume on chrome they should  
**Translation:** 

**[9303.62s] English:** maybe get rid of double click or something divest something i don't know it might happen so so brave  
**Translation:** 

**[9308.62s] English:** might inspire google to completely change the way they're doing things they're already doing  
**Translation:** 

**[9312.24s] English:** something you may have read about called the privacy sandbox or um flock which they have this  
**Translation:** 

**[9318.22s] English:** bird metaphor going um turtle dove um fledge but these these these systems have been very googly  
**Translation:** Vocabulary: fledge: 雏鸟; googly: 怪异; metaphor: 比喻; sandbox: 沙箱

**[9325.48s] English:** kind of over engineered and yet  
**Translation:** 

**[9327.20s] English:** depending on differential privacy which has weakness over time if you know how that works  
**Translation:** Vocabulary: differential: 差分

**[9331.32s] English:** it's kind of injecting noise to hide you in a crowd but over time an adversary can pull you  
**Translation:** 

**[9336.30s] English:** out of the crowd this doesn't look like it's going to become a standard like apple brave mozilla we're  
**Translation:** Vocabulary: adversary: 对手; injecting: 注入

**[9342.04s] English:** not going to just say oh google you saved us you've invented the privacy sandbox so we'll all  
**Translation:** 

**[9346.38s] English:** just adopt it not going to be that easy it's going to be more like pieces of what we do in  
**Translation:** 

**[9351.08s] English:** brave this anonymous ad matching or the blind signature cryptography we use to confirm the ad  
**Translation:** 

**[9356.22s] English:** impressions that's going to be a standard for us so i think it's going to be a standard for us  
**Translation:** Vocabulary: cryptography: 加密技术

**[9357.20s] English:** david chum's invention that could get  
**Translation:** 

**[9360.00s] English:** In fact, some of that is being standardized. Even Google's in favor of so-called trust tokens, which are Xiaomi and blind signature certs. But they're not using them for ad confirmations because they don't want to blow up their own business. And they need to let some of the publishers they serve have other ad tech scripts on the page. And so they're kind of caught. And this is something I realized doing Brave.  
**Translation:** Vocabulary: confirmations: 确认; standardized: 标准化

**[9379.78s] English:** I thought, what's Google's innovator's dilemma apart from just being mature and having trouble innovating? It's that they have come to depend on this ad tech system that has all these vendors that publishers rely on because publishers aren't technical enough.  
**Translation:** 

**[9396.26s] English:** And I feel for the publishers, but I realized the users have to come first. And if you give the users a better browser that's faster, then you'll get enough users to give back or support publishers.  
**Translation:** Vocabulary: innovating: 创新

**[9407.02s] English:** The speed and the battery savings and the data plan savings are significant. There's so much bad JavaScript involved in ad tech that if you block it, you sort of chop off what's called the programmatic waterfall, which chains a bunch of requests.  
**Translation:** 

**[9418.96s] English:** Yeah, that's one of the incredible things about Brave. I guess you're saying you should attribute it to the fact that the messy JavaScript, no offense, is, I mean, Brave just feels faster, even than, I mean, Chrome was fast.  
**Translation:** Vocabulary: attribute: 归因于

**[9436.30s] English:** One of the things that it was, like, impressive is it showed that browsers could be really fast. And Brave is even faster than that, which is incredible.  
**Translation:** 

**[9443.88s] English:** Because we block so much. And it saves the network, which means data plan. It saves battery because the radio consumes your battery when it's running more to do those requests.  
**Translation:** Vocabulary: browsers: 浏览器; consumes: 消耗

**[9451.38s] English:** And it's just stunning how many there are. Like, some of my Google friends were like, oh, that's just that bad site. They'll fix it. And you actually do a survey of webpages. They're mostly like that.  
**Translation:** 

**[9459.80s] English:** I know Google engineers could make everything super efficient, but they can't, especially in antitrust court, do it.  
**Translation:** Vocabulary: antitrust: 反垄断; webpages: 网页

**[9465.72s] English:** They cannot take it.  
**Translation:** 

**[9466.30s] English:** They can't take over all the publishers and do that. They're trying with Accelerated Mobile Profile, AMP. They're trying to pull publishers. They're like, oh, you poor publishers don't know how to make your pages fast. Put them on our AMP system. We'll give you extra placement in the search care.  
**Translation:** Vocabulary: accelerated: 加速; cannot: 不能; placement: 位置

**[9480.00s] English:** so that's an antitrust problem for one but it's also publishers we talk to hate it because it  
**Translation:** 

**[9484.66s] English:** degrades their brand now they look like a gig writer wrote a piece that's got google's framing  
**Translation:** Vocabulary: degrades: 降低

**[9490.02s] English:** an amp url on top of it and they're trying to fix that too but it just looks like a google's  
**Translation:** 

**[9495.64s] English:** borgifying all these publishers and they don't want to be plugged into the borg cube they want  
**Translation:** Vocabulary: borgifying: 同质化

**[9499.26s] English:** to build up their own brand and have loyal readers so you know i'm in favor of giving the users power  
**Translation:** 

**[9505.44s] English:** to help all the publishers in this little platoons and the creators and so we talked about patreon  
**Translation:** Vocabulary: platoons: 小团体

**[9510.74s] English:** what about social networks well they're inherently like search a global algorithm you're trying to  
**Translation:** 

**[9516.20s] English:** find friends of friends you're doing the transitive closure of a graph induced by this friend of  
**Translation:** Vocabulary: algorithm: 算法; transitive: 传递的

**[9520.28s] English:** relation but you should own your friend relation you should own your posts they shouldn't be owned  
**Translation:** 

**[9528.04s] English:** by somebody else who can take them down or censor them and your friend relations you should be able  
**Translation:** Vocabulary: censor: 审查

**[9532.46s] English:** to find those friends on other networks and that's why i've tweeted about this i  
**Translation:** 

**[9535.42s] English:** haven't built it yet what if the browser could keep track of those for you what if the browser  
**Translation:** 

**[9540.36s] English:** could maybe combine facebook and twitter and you could find your friends on both and you could  
**Translation:** 

**[9545.66s] English:** have a sort of that relationship is not owned by facebook or twitter it's owned by you  
**Translation:** 

**[9550.90s] English:** they don't have terms of use and they'll say they own it but if they zap you on one and you're still  
**Translation:** 

**[9556.06s] English:** on the other your friends find you and the browser could preserve a combined view you could resurrect  
**Translation:** Vocabulary: resurrect: 复活

**[9561.54s] English:** almost across networks it's something i want to maybe  
**Translation:** 

**[9565.42s] English:** quickly ask you about on that front there's been a quite a lot of um centralized we talked about  
**Translation:** 

**[9572.02s] English:** wall street bets and then uh robin hood has been centralized banning of different accounts and  
**Translation:** 

**[9579.60s] English:** removing like parlor for example from aws and this kind of overreach of centralized control  
**Translation:** Vocabulary: parlor: 聊天室

**[9585.68s] English:** is your hope that it's possible to like what are your thoughts about that in general is it  
**Translation:** 

**[9591.30s] English:** and is it possible to create tools that give  
**Translation:** 

**[9595.42s] English:** individual people the power to fight back against overreach of such control  
**Translation:** 

**[9600.00s] English:** So we're talking about oligarchy, I do think, and that if it controls a nation state, that's  
**Translation:** 

**[9604.84s] English:** formidable. It's the tax and the police power, the military power. It means that you may have  
**Translation:** 

**[9609.40s] English:** the Great Firewall of China. You may have people in China who are jailed because of their tweets,  
**Translation:** Vocabulary: firewall: 防火墙; formidable: 强大; tweets: 推特

**[9614.44s] English:** right? This is a serious threat. I can't minimize it or say that we'll win. I don't know how it's  
**Translation:** 

**[9619.10s] English:** going to go. But I do think, like I said earlier about the cunning of reason, people find ways  
**Translation:** Vocabulary: cunning: 机巧

**[9623.40s] English:** around things. The internet routes around censorship. And this is not to endorse any  
**Translation:** 

**[9627.50s] English:** particular bad faction. One of the things that happens when you try to wave the free speech flag  
**Translation:** Vocabulary: censorship: 审查制度

**[9632.16s] English:** too much, you say, I'm not going to censor anything, and you get colonized by terrible,  
**Translation:** 

**[9636.56s] English:** terrible people, I guess. I don't care if you call them neo-Nazis. Some of them could be doing  
**Translation:** 

**[9640.60s] English:** illegal things. And you don't want them colonizing because it'll ruin your reputation and destroy  
**Translation:** 

**[9645.46s] English:** your business. So what you really want is that kind of user-first subsidiarity, that subjectivity.  
**Translation:** Vocabulary: colonizing: 殖民; subsidiarity: 分权

**[9651.46s] English:** I want my social networks to be composited in some multi-social user interface where I  
**Translation:** 

**[9657.46s] English:** don't...  
**Translation:** Vocabulary: composited: 合成; interface: 界面

**[9657.48s] English:** I don't lose track of people across networks. And if they leave one or they get banned from one,  
**Translation:** 

**[9661.62s] English:** I can find them on another. I can still sort of thread them together.  
**Translation:** 

**[9664.14s] English:** Yeah, that's brilliant.  
**Translation:** 

**[9665.06s] English:** And this didn't happen because browsers got captured by the central powers.  
**Translation:** Vocabulary: browsers: 浏览器

**[9669.90s] English:** Why did they get captured? Mostly because of search. And search is a central algorithm.  
**Translation:** 

**[9673.78s] English:** So Larry Page said this too many years ago. He said, with search, you're giving up a little  
**Translation:** Vocabulary: algorithm: 算法

**[9677.26s] English:** privacy by handing the query over to us. And we'll error correct it. Alan Eustace used to be a Google  
**Translation:** 

**[9683.00s] English:** executive. He said, oh, yeah, we used to laugh. They'd all be doing typos, and they'd be typing  
**Translation:** Vocabulary: typos: 打字错误

**[9687.40s] English:** them.  
**Translation:** 

**[9687.48s] English:** And we're like, no, dummy, type that query. And it's like, okay, Google, you might want to dial  
**Translation:** Vocabulary: dummy: 笨蛋

**[9691.98s] English:** back that ego a little bit. But yes, you do see all the queries, and you can improve them, and  
**Translation:** 

**[9696.24s] English:** you can find the best results. And that was Google's forte. When we did the Firefox deal in  
**Translation:** 

**[9700.14s] English:** 2004, Google was really good. And over time, SEO, which is an adversarial game, and Google itself,  
**Translation:** 

**[9707.70s] English:** buying all these companies and crowding its own results page with its own tied-in stuff,  
**Translation:** Vocabulary: adversarial: 对抗性质

**[9713.18s] English:** the YouTube code.  
**Translation:** 

**[9713.86s] English:** It's a slipper slope that happens when you have control over the results.  
**Translation:** 

**[9717.40s] English:** Control over these kinds of really important mechanisms.  
**Translation:** 

**[9720.00s] English:** Yeah. Monopoly capitalism or cartel. You get this with the Robin Hoods and the hedge funds. You get sort of the money interests take over and kind of abuse their power and wear out their welcome. So how do you get around that? You have to have either new land to go to, which some people's ancestors, not mine, did to found the country. I'm mostly Irish-German.  
**Translation:** Vocabulary: capitalism: 资本主义; cartel: 卡特尔; monopoly: 垄断

**[9742.00s] English:** You have new virtual space people go to, and that requires an ISP or a colo center or Amazon to host you. It requires domain name registrar who will not strike you. And so when Parler was taken down, I thought that was egregious. Parler, it was not well designed. And I tried it out because I tried all these things, but I didn't use it.  
**Translation:** 

**[9766.58s] English:** And I also felt they were being unfairly scored for not moderating because you can find tweets to this day.  
**Translation:** 

**[9772.00s] English:** Yeah.  
**Translation:** 

**[9772.48s] English:** Or horrendous and threaten all sorts of violence. Whereas Twitter, why isn't Twitter being taken down? But so it was very selective. It was the insiders who have the power are going to take out the newcomer. And it looked bad. It's sort of like the hedge funds sorting GameStop. It looked bad. You know, you're seeing a piece in Time Magazine this week that's like basically saying, yeah, we interfere with the election, but it was great. Aren't we good? I don't know if you've seen this piece yet.  
**Translation:** Vocabulary: horrendous: 恐怖的; insiders: 内部人员; interfere: 干预; newcomer: 新来者; selective: 选择性的; threaten: 威胁

**[9795.64s] English:** No, I haven't.  
**Translation:** 

**[9796.38s] English:** If you tried to say that as a Trump supporter in November after the election, you'd get banned.  
**Translation:** 

**[9802.00s] English:** But now Time in its Twitter account is saying, you know, we saved the day. It's AFL-CIO and big business, the Better Business Bureau got together and kept Trump from spreading fake news. So the country's kind of broken. I don't know how to fix that. The oligarchs have run wild in my opinion. And big tech is in the antitrust dock. What's going to happen? I don't think they get out. I think some of the DOJ and certainly the state cases, because there's separate cases, are not going to go away just because somebody got elected differently.  
**Translation:** 

**[9832.00s] English:** And these are career prosecutors and they have a strong case. And Google's smart. Microsoft almost got split up, right? The judge.  
**Translation:** Vocabulary: antitrust: 反垄断; oligarchs: 寡头; prosecutors: 检察官

**[9840.00s] English:** Thomas Penfield Jackson.  
**Translation:** 

**[9842.04s] English:** He overreached.  
**Translation:** Vocabulary: penfield: 彭菲尔德

**[9842.72s] English:** He didn't hold a hearing about the remedy.  
**Translation:** 

**[9844.98s] English:** He just said, I'm going to break you up.  
**Translation:** 

**[9846.78s] English:** And Microsoft appealed, and the higher-level court said,  
**Translation:** 

**[9850.00s] English:** go back and figure this out.  
**Translation:** Vocabulary: appealed: 提起上诉

**[9851.58s] English:** You're not breaking them up.  
**Translation:** 

**[9852.30s] English:** You didn't even hold a hearing.  
**Translation:** 

**[9853.58s] English:** And when they got back, Microsoft said, let's settle.  
**Translation:** 

**[9856.02s] English:** Let's settle.  
**Translation:** 

**[9856.50s] English:** We don't want to get broken up.  
**Translation:** 

**[9857.58s] English:** Because Jackson was going to make the OpsCo,  
**Translation:** 

**[9860.36s] English:** the operating system company, and the AppsCo office,  
**Translation:** 

**[9863.26s] English:** Word and Excel.  
**Translation:** 

**[9864.82s] English:** And that would have been a huge blow to Microsoft.  
**Translation:** 

**[9867.26s] English:** But ultimately, I don't know if you're optimistic or cynical  
**Translation:** Vocabulary: cynical: 悲观; optimistic: 乐观

**[9871.46s] English:** about the possibility of breaking up big tech.  
**Translation:** 

**[9874.46s] English:** To me, I'm optimistic that tools like Brave,  
**Translation:** 

**[9879.92s] English:** I love the idea of owning your friendships.  
**Translation:** 

**[9882.28s] English:** Users more and more owning the stuff is the only real way.  
**Translation:** 

**[9886.34s] English:** Unfortunately, it's like the Wall Street bet subreddit  
**Translation:** 

**[9888.48s] English:** is the only real way to fight the centralized power.  
**Translation:** Vocabulary: subreddit: 子版块

**[9891.10s] English:** You can't break them up through regulation.  
**Translation:** 

**[9892.78s] English:** It's very difficult.  
**Translation:** 

**[9893.20s] English:** Certainly, I don't want to wait for the law.  
**Translation:** 

**[9895.24s] English:** Netscape was long dead, or acquired,  
**Translation:** Vocabulary: netscape: 网景浏览器

**[9897.12s] English:** by AOL, and effectively dead.  
**Translation:** 

**[9898.44s] English:** It was only Mozilla that returned Firefox to the market  
**Translation:** 

**[9901.32s] English:** by the time that the US v. Microsoft case was finally settled  
**Translation:** 

**[9905.32s] English:** and the penalties were put in place.  
**Translation:** 

**[9907.50s] English:** And yet, antitrust has a role to play.  
**Translation:** 

**[9911.08s] English:** Those penalties caused Microsoft to kind of turn away from the web.  
**Translation:** 

**[9914.24s] English:** They did Windows Vista, and they thought,  
**Translation:** 

**[9916.08s] English:** the web's too painful.  
**Translation:** Vocabulary: vista: 视野

**[9916.90s] English:** We got punished in court, and we had to standardize things  
**Translation:** 

**[9919.68s] English:** with those icky standards people.  
**Translation:** Vocabulary: standardize: 规范化

**[9921.08s] English:** So they ran back to proprietary lock-in,  
**Translation:** 

**[9923.48s] English:** and Windows Vista flopped.  
**Translation:** Vocabulary: flopped: 失败; proprietary: 专有

**[9924.66s] English:** It was late.  
**Translation:** 

**[9925.14s] English:** It was bloated.  
**Translation:** Vocabulary: bloated: 腹胀

**[9926.58s] English:** Long.  
**Translation:** 

**[9927.12s] English:** Now, what I was going to say,  
**Translation:** 

**[9929.50s] English:** Google's smart enough.  
**Translation:** 

**[9930.40s] English:** They won't get split up.  
**Translation:** 

**[9931.64s] English:** They'll split something out to get off the hook, I think.  
**Translation:** 

**[9935.58s] English:** This is a complicated subject,  
**Translation:** 

**[9937.54s] English:** but I, myself, was so...  
**Translation:** 

**[9940.06s] English:** I decided to journey out from the world  
**Translation:** 

**[9943.18s] English:** of being a researcher at MIT  
**Translation:** 

**[9944.90s] English:** and potentially doing a startup myself.  
**Translation:** 

**[9948.60s] English:** And I've been thinking of, you know,  
**Translation:** 

**[9951.36s] English:** I wanted to come to Silicon Valley to do so.  
**Translation:** 

**[9953.66s] English:** It's the land of the entrepreneur.  
**Translation:** 

**[9955.30s] English:** And there's...  
**Translation:** Vocabulary: entrepreneur: 企业家

**[9956.58s] English:** A lot of my friends,  
**Translation:** 

**[9957.62s] English:** a lot of them are successfully having a...  
**Translation:** 

**[9960.00s] English:** entrepreneurs themselves, has said, do not come to Silicon Valley. You ran amazing teams of  
**Translation:** 

**[9968.60s] English:** engineers. You started a lot of successful businesses. I wondered if you could comment on  
**Translation:** Vocabulary: entrepreneurs: 企业家

**[9973.94s] English:** why a lot of people are leaving California. Is there something that could be fixed about  
**Translation:** 

**[9978.90s] English:** California? If you were starting a business today, would you consider somewhere else like Austin  
**Translation:** 

**[9985.42s] English:** or some other place? Or is Silicon Valley still, is it just a little lull? Everybody's being  
**Translation:** 

**[9991.44s] English:** overdramatic during this particular year of the coronavirus and so on? I think even Austin's  
**Translation:** Vocabulary: coronavirus: 冠状病毒; overdramatic: 夸大其词

**[9997.32s] English:** getting overheated, I hear. And I've had relatives and friends move to Texas within the last few  
**Translation:** 

**[10003.02s] English:** months. So Texas as a whole is a big place. And people are moving to Florida. There's a big  
**Translation:** Vocabulary: texas: 德克萨斯州

**[10008.88s] English:** movement toward Miami, Peter Thiel, Keith Barber, all these people. The mayor has been very  
**Translation:** 

**[10014.36s] English:** businesslike.  
**Translation:** Vocabulary: businesslike: 商务风格; miami: 迈阿密

**[10015.42s] English:** Which I think is just good politics. America is fundamentally a commercial republic. So you  
**Translation:** 

**[10020.80s] English:** would think this would be what's happening. For a long time, California was the golden state. I  
**Translation:** Vocabulary: california: 加利福尼亚; fundamentally: 本质上

**[10024.50s] English:** came here in late 76 when I was a teenager. It's in crushing debt due to the lockdowns. It's got  
**Translation:** 

**[10032.08s] English:** the highest taxes. That's got to matter. People will do high taxes. It's got likely fires every  
**Translation:** Vocabulary: lockdowns: 封城

**[10039.88s] English:** year because of the deadfall. It's not global warming. It's because the forests weren't managed  
**Translation:** 

**[10044.12s] English:** like they had been in the first part of the pandemic. It's because the forests weren't  
**Translation:** Vocabulary: deadfall: 倒木; pandemic: 疫情

**[10045.40s] English:** managed like they had been in the first part of the pandemic.  
**Translation:** 

**[10046.00s] English:** Just, I would say, corruption at all levels, especially up to the governor, who famously was  
**Translation:** 

**[10053.32s] English:** eating at the French Laundry and claimed the outside was inside and they were out in masks  
**Translation:** 

**[10057.40s] English:** off and it was great. Do what I say, not what I do. Rules for thee, but not for me. When you see  
**Translation:** 

**[10066.22s] English:** that in leadership, people either run or they get rid of the leadership. So there's a recall drive,  
**Translation:** 

**[10071.30s] English:** which is about to reach the threshold. Or in the old days, they get their guns.  
**Translation:** Vocabulary: threshold: 门槛

**[10075.40s] English:** Right. You don't put up with this junk. But ultimately, the thing that made  
**Translation:** 

**[10080.00s] English:** silicon valley a special place it gave freedom to like young kids entrepreneurs young minds  
**Translation:** 

**[10086.68s] English:** brave minds to think bold to try different stuff i mean even if the taxes are high  
**Translation:** 

**[10092.32s] English:** so outside of financial stuff outside of all of that housing super expensive housing so it's hard  
**Translation:** 

**[10098.56s] English:** okay everything about this was narrow and they didn't plan the roads right yeah they got rid of  
**Translation:** 

**[10104.02s] English:** public transportation in la like the who framed roger rabbit cartoon show they used to have trolley  
**Translation:** 

**[10108.90s] English:** cars portland too yeah the oil companies and the dod conspired to build highways and make cars  
**Translation:** 

**[10114.76s] English:** dominant and the rights of way are long gone like elon's gonna go underground i wish him well that's  
**Translation:** Vocabulary: conspired: 勾结

**[10120.88s] English:** probably the only way to do it now yeah but it's still a place do you think it's possible that  
**Translation:** 

**[10125.84s] English:** silicon valley is still a place where magic happens where the next google is built where  
**Translation:** 

**[10129.58s] English:** the next i mean brave is built where uh i think all good things come to an end i think the problem  
**Translation:** 

**[10135.44s] English:** is silicon valley had strong network effects through stanford  
**Translation:** 

**[10138.64s] English:** through  
**Translation:** 

**[10138.88s] English:** uh the angel investor networks and the wealth effect and originally you have to give the federal  
**Translation:** Vocabulary: investor: 投资者

**[10144.54s] English:** government credit like the arpanet was a government project let's not kid ourselves this wasn't wild  
**Translation:** 

**[10149.06s] English:** free market you know libertarian capitalism this was all cold war stuff um you had uh out of the  
**Translation:** Vocabulary: arpanet: 阿帕网; capitalism: 资本主义; libertarian: 自由放任

**[10155.52s] English:** academia you had shockley and then the the traders aid and fairchild and intel and but now  
**Translation:** 

**[10161.60s] English:** you know when's the last fab that was built in the valley micro unity might have been the last  
**Translation:** Vocabulary: academia: 学术界; fairchild: 费尔柴尔德; shockley: Shockley

**[10166.28s] English:** i don't know i haven't followed but we built a fab in sunnyvale  
**Translation:** 

**[10168.88s] English:** and uh in micro unity in starting early 90s and now the fabs are overseas um and the one thing that  
**Translation:** Vocabulary: sunnyvale: 桑尼韦尔

**[10178.22s] English:** i would say that the oligarchs have intentionally done in both parties is sort of labor and  
**Translation:** 

**[10184.24s] English:** environmental protection law arbitrage by going where the labor is cheaper and the environmental  
**Translation:** Vocabulary: arbitrage: 套利; oligarchs: 寡头

**[10188.06s] English:** laws aren't as strict and you know that's polluted the hell out of parts of china but it's made  
**Translation:** 

**[10192.52s] English:** things you can make cheaper junk and uh this this is not uh this is not a story that's over yet  
**Translation:** 

**[10198.88s] English:** so what is so  
**Translation:** 

**[10200.00s] English:** for now it's for the network effect the the brain trust of who you know the parties the stanford um  
**Translation:** Vocabulary: stanford: 斯坦福大学

**[10207.08s] English:** sort of network that's fragile too over time i'm afraid right stanford a lot of good professors  
**Translation:** 

**[10214.58s] English:** are like uh they still filter you know mainly based on socioeconomic status but it's kind of  
**Translation:** Vocabulary: fragile: 易碎; socioeconomic: 社会经济

**[10220.30s] English:** a skate school i had a friend uh hired out of harvard 20 years ago at netscape and we talked  
**Translation:** 

**[10227.80s] English:** about harvard and he said yeah there's still professors who grade on the curb and i said oh  
**Translation:** Vocabulary: netscape: 网景浏览器

**[10231.06s] English:** yeah i don't think they're any doing that at stanford and he said yo it was shocking some of  
**Translation:** 

**[10235.30s] English:** the students got c's and d's and they were crying it's like yes that's right the the precious deers  
**Translation:** 

**[10239.54s] English:** can't take that at stanford so they get a's and b's yeah now you look at china and people say  
**Translation:** 

**[10245.00s] English:** we all about china they true of russia too a lot of math science training a lot of engineering a  
**Translation:** 

**[10250.72s] English:** lot of people who are doing their coursework to get the a's and b's so um i'm going to  
**Translation:** 

**[10257.78s] English:** american i'm born on the fourth of july really fourth of july yeah wow and america as i say  
**Translation:** Vocabulary: coursework: 课程作业

**[10263.34s] English:** fundamentally is a commercial republic you can try to make it something else you can say it's  
**Translation:** 

**[10266.80s] English:** the new atlantis and mystify it you could you could talk about it in a more i think correct  
**Translation:** Vocabulary: atlantis: 失落的城邦; fundamentally: 本质上

**[10271.04s] English:** way which is 13 colonies that grew and then there's a lot of local or original design anyway  
**Translation:** 

**[10276.66s] English:** the federal federalist papers talk about this is a lot of subsidiarity but that's that's been eroded  
**Translation:** Vocabulary: eroded: 侵蚀; subsidiarity: 地方自治

**[10283.28s] English:** over time and like i say a lot of the offshoring is hurt so what happened  
**Translation:** 

**[10287.78s] English:** with coronavirus people working from home and at first it was funny because i have friends at  
**Translation:** Vocabulary: coronavirus: 冠状病毒; offshoring: 海外外包

**[10291.80s] English:** google who used to grumble that not only did they have to come into the office if they joined a  
**Translation:** 

**[10296.18s] English:** different team that was centered in a different office they had to move or you know if if if the  
**Translation:** Vocabulary: grumble: 抱怨

**[10300.40s] English:** va team was reconstituted in munich which it was after lars bach just got tired of javascript  
**Translation:** 

**[10305.90s] English:** that they hired in munich or they hired phds in germany and moved them to munich  
**Translation:** Vocabulary: munich: 慕尼黑; reconstituted: 重组

**[10309.90s] English:** with coronavirus everyone's working from home and it's like what a relief i can work for google  
**Translation:** 

**[10313.80s] English:** from home but then the next shoe dropped and people started asking mark zuckerberg  
**Translation:** Vocabulary: zuckerberg: 扎克伯格

**[10317.78s] English:** hey can i move to my  
**Translation:** 

**[10320.00s] English:** hometown in the midwest yeah and he said okay and they said oh can i keep getting my silicon valley  
**Translation:** 

**[10323.98s] English:** pay no we're going to figure out what your cost of living there is and we're going to adjust your  
**Translation:** 

**[10329.22s] English:** pay accordingly and and these colonies and these little mini experiments that all combine to the  
**Translation:** Vocabulary: accordingly: 相应地

**[10333.90s] English:** big giant experiment i i have a i don't know i have this uh vision of america which the country  
**Translation:** 

**[10340.46s] English:** i was born in russia like i said here and this is truly a wonderful country i um i wasn't born  
**Translation:** 

**[10345.58s] English:** on the 4th of july people still flee here people still flee i still and i'm uh red-blooded american  
**Translation:** 

**[10351.08s] English:** at this point and i have a sense that we figured it out somehow if silicon valley burns another  
**Translation:** 

**[10357.06s] English:** place will come up in this place that even more innovation and people will move and the remote  
**Translation:** 

**[10363.20s] English:** work might change fundamentally how we work or might not it might just give you the freedom to  
**Translation:** 

**[10368.54s] English:** then create many other small silicon valleys throughout the place like austin included but  
**Translation:** 

**[10373.58s] English:** other places as well and we  
**Translation:** 

**[10375.58s] English:** somehow figure it figure it out and uh i think that's that's true that there will be more  
**Translation:** 

**[10381.06s] English:** mobility and maybe new places that come up i don't know if silicon valley has you know passed  
**Translation:** Vocabulary: mobility: 流动性

**[10386.82s] English:** some sell-by date because um it did hurt the coronavirus hurt the lockdowns hurt in the fact  
**Translation:** 

**[10392.94s] English:** in the sense that part of what keeps things going is social and so a lot of young people  
**Translation:** Vocabulary: lockdowns: 封控措施

**[10396.90s] English:** even before coronavirus moved to san francisco it was very strange to watch because in the 80s we  
**Translation:** 

**[10401.78s] English:** all lived in the valley and it was less populated and san francisco was  
**Translation:** 

**[10405.56s] English:** grungier it was more like dirty harry in the 70s yes but but by the 90s uh and jamie runs a  
**Translation:** 

**[10411.22s] English:** nightclub there and he's talked about this you had sort of wealthy tech people moving in south  
**Translation:** Vocabulary: grungier: 更邋遢; nightclub: 夜总会

**[10415.38s] English:** of market fancy townhouses being built and uh that's continued in such a point that it's almost  
**Translation:** 

**[10420.48s] English:** like what's the movie by the south african director nels jody foster up in the space colony uh matt  
**Translation:** Vocabulary: foster: 傅斯特; townhouses: 联排别墅

**[10426.24s] English:** damon is the guy on the earth who has to go up and anyway it's about the stratification it's  
**Translation:** 

**[10430.58s] English:** about the great inequality the people in the space station have like amazing medical auto  
**Translation:** Vocabulary: inequality: 不平等; stratification: 阶层划分

**[10435.56s] English:** can extend their life or save them cure cancer people on earth are all suffering ground down  
**Translation:** 

**[10440.00s] English:** in poverty um and uh you know that sort of happened while i was here you saw a lot of money  
**Translation:** 

**[10447.84s] English:** drive prices up along the narrow peninsula and the single people wanted nightlife so they were  
**Translation:** 

**[10453.42s] English:** in the city and the condos in the city got super expensive and you i know even google friends who  
**Translation:** Vocabulary: condos: 公寓; nightlife: 夜生活; peninsula: 半岛

**[10458.74s] English:** are you know socially responsible say we should have more housing built we should have yes in my  
**Translation:** 

**[10463.64s] English:** backyard not not in my backyard but that's not happening as far as i can tell and from the  
**Translation:** Vocabulary: backyard: 后院

**[10469.46s] English:** government to the incumbent you know landowners and renters it's just not happening and that has  
**Translation:** 

**[10476.62s] English:** to drive people away i i appreciate that people come here and you should wait for the prices to  
**Translation:** Vocabulary: incumbent: 现任者; landowners: 地主

**[10481.24s] English:** moderate they will but um but a lot of people are going to go where the prices are lower  
**Translation:** 

**[10486.22s] English:** you uh and sorry for silly questions here but just looking back you have created things  
**Translation:** 

**[10494.10s] English:** have been part of creating things that have transformed this world the world of  
**Translation:** 

**[10499.46s] English:** technology perhaps more than almost anything else um but you're still a human being and uh  
**Translation:** 

**[10508.64s] English:** unfortunately this ride ends do you ever think about your own mortality not too much i mean i'm  
**Translation:** 

**[10514.96s] English:** i'm a roman catholic so i am not afraid of death i think a lot of people who um have problems with  
**Translation:** 

**[10523.74s] English:** death are suffering from some  
**Translation:** 

**[10529.46s] English:** lack of either faith in their transcending death or maybe they don't have children or they feel  
**Translation:** Vocabulary: transcending: 超越死亡

**[10535.18s] English:** like you know they get later in life and they feel like they they've missed opportunities to  
**Translation:** 

**[10539.34s] English:** do something that endures and i i sympathize with a lot because i i'm old i got married fairly old  
**Translation:** Vocabulary: sympathize: 同情

**[10544.36s] English:** so i i understand all that i nothing human is alien to me as terence said uh but um i don't  
**Translation:** 

**[10553.06s] English:** fear it no what do you hope your legacy is yeah it's gonna be javascript i think no i think  
**Translation:** Vocabulary: alien: 陌生

**[10559.46s] English:** you know  
**Translation:** 

**[10560.00s] English:** My legacy has more to do with my children and their children.  
**Translation:** 

**[10563.52s] English:** I think it also has to do with web standards.  
**Translation:** 

**[10566.42s] English:** It has to do with things like Brave.  
**Translation:** 

**[10568.26s] English:** The things we did with Firefox, when we did, you know, I'm not going to oversell Brave,  
**Translation:** 

**[10573.04s] English:** but I think Brave is important and we will continue to prove this in a way that counts  
**Translation:** Vocabulary: oversell: 夸大宣传

**[10576.60s] English:** for many decades to come.  
**Translation:** 

**[10578.12s] English:** But even Firefox, whatever its future fortune, showed you can restart the browser market.  
**Translation:** 

**[10583.16s] English:** This thing you said about people opting out and routing around, you don't need everybody  
**Translation:** 

**[10587.92s] English:** to do that.  
**Translation:** Vocabulary: opting: 选择退出; routing: 绕行

**[10588.50s] English:** It's more like Taleb's stubborn minorities that do that.  
**Translation:** 

**[10591.20s] English:** It's the lead users, Eric von Hippel's lead users.  
**Translation:** 

**[10593.54s] English:** You can be a few percent, you can tilt the market.  
**Translation:** 

**[10596.30s] English:** And that can be done in spite of the incumbents, the moneyed interests not being in favor of  
**Translation:** Vocabulary: incumbents: 在任者

**[10601.02s] English:** what you're doing.  
**Translation:** 

**[10601.60s] English:** So I think what we do with Firefox won't be forgotten and it needs to be done more.  
**Translation:** 

**[10606.38s] English:** And we're doing it with Brave.  
**Translation:** 

**[10607.12s] English:** And you could argue that other projects are doing it.  
**Translation:** 

**[10608.80s] English:** In some ways, blockchain is doing it.  
**Translation:** 

**[10610.44s] English:** The Robinhood takedown, the use of Robinhood by the Wall Street bets kids.  
**Translation:** Vocabulary: robinhood: 典范; takedown: 突袭行动

**[10618.02s] English:** It's similar.  
**Translation:** 

**[10619.20s] English:** So yeah, that kind of spirit endures.  
**Translation:** 

**[10621.34s] English:** And I think in some ways it's American, right?  
**Translation:** 

**[10624.98s] English:** It's not hard revolutionary.  
**Translation:** 

**[10626.54s] English:** It's not trying to burn the past and destroy everything.  
**Translation:** 

**[10628.68s] English:** It's more like we have these certain, let's say, rights.  
**Translation:** 

**[10635.22s] English:** We have duties too.  
**Translation:** 

**[10636.24s] English:** So there's some debate about which comes first in American jurisprudence and the founding  
**Translation:** Vocabulary: founding: 创立; jurisprudence: 法学

**[10639.78s] English:** documents.  
**Translation:** 

**[10640.48s] English:** But as long as things are working, we'll be like pragmatic Americans, like de Tocqueville  
**Translation:** Vocabulary: pragmatic: 实用主义

**[10647.48s] English:** described.  
**Translation:** 

**[10648.02s] English:** But if things get too out of whack for one reason or another, too unequal, too oligarchic  
**Translation:** Vocabulary: oligarchic: 寡头统治; unequal: 不平等

**[10654.14s] English:** and abusive, we're going to assert our rights.  
**Translation:** 

**[10657.18s] English:** And even a few of us can do it.  
**Translation:** Vocabulary: abusive: 虐待的

**[10658.88s] English:** And even in the American Revolution, it was the minority who fought and put their lives,  
**Translation:** 

**[10664.10s] English:** treasure and sacred honor at stake.  
**Translation:** 

**[10665.68s] English:** It was a bunch of people went to Upper Canada, I think it was called, Ontario.  
**Translation:** 

**[10671.16s] English:** Yeah, that's a beautiful thing.  
**Translation:** 

**[10672.40s] English:** I mean, that is at the core where your work stands for is that a few people can have the  
**Translation:** 

**[10677.02s] English:** power to transform society.  
**Translation:** 

**[10680.00s] English:** with just a few radical ideas, with just a little bit of code,  
**Translation:** 

**[10683.32s] English:** changed the world.  
**Translation:** 

**[10684.56s] English:** Got to do it.  
**Translation:** 

**[10685.10s] English:** And that's empowering, and that is the American way.  
**Translation:** 

**[10687.22s] English:** That's why this country is, I believe, the greatest country.  
**Translation:** 

**[10690.16s] English:** I know that's not over-remeditated too much,  
**Translation:** 

**[10693.02s] English:** but I think some special things have already happened in this country  
**Translation:** 

**[10697.42s] English:** and will continue to happen.  
**Translation:** 

**[10698.58s] English:** And that spirit can continue no matter who comes here.  
**Translation:** 

**[10702.28s] English:** They can adopt those folk ways and that spirit.  
**Translation:** 

**[10705.58s] English:** Brandon, I can't tell you how much I was freaking out,  
**Translation:** 

**[10708.34s] English:** how much of an honor it is to talk to you.  
**Translation:** Vocabulary: freaking: 恐慌

**[10710.24s] English:** You're an incredible human being.  
**Translation:** 

**[10711.42s] English:** This is one of my favorite conversations ever.  
**Translation:** 

**[10713.50s] English:** Thank you so much for wasting all this time with me.  
**Translation:** 

**[10715.62s] English:** I really appreciate it.  
**Translation:** 

**[10716.58s] English:** Oh, it seems like a breeze.  
**Translation:** 

**[10717.84s] English:** My pleasure.  
**Translation:** 

**[10719.48s] English:** Thank you for listening to this conversation with Brandon Eich.  
**Translation:** 

**[10722.50s] English:** And thank you to our sponsors,  
**Translation:** Vocabulary: sponsors: 赞助商

**[10724.12s] English:** Jordan Harbinger Show, Sun Basket Meal Delivery Service,  
**Translation:** 

**[10728.46s] English:** BetterHelp Online Therapy, and 8Sleep Self-Cooling Mattress.  
**Translation:** Vocabulary: mattress: 床垫

**[10732.72s] English:** Click the sponsor links to get a discount and to support this podcast.  
**Translation:** 

**[10736.96s] English:** And now, let me leave you.  
**Translation:** 

**[10738.34s] English:** Let me leave you with some words from Jeff Atwood.  
**Translation:** 

**[10740.62s] English:** Any app that can be written in JavaScript  
**Translation:** 

**[10742.90s] English:** will eventually be written in JavaScript.  
**Translation:** 

**[10746.64s] English:** Thank you for listening and hope to see you next time.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
