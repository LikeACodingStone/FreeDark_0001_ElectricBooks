# Podcast vocabulary notes
Source file: Lex Fridman - James Gosling： Java, JVM, Emacs, and the Early Days of Computing ｜ Lex Fridman Podcast #126.opus

**[0.00s] English:** The following is a conversation with James Gosling, the founder and lead designer behind  
**Translation:** 

**[4.18s] English:** the Java programming language, which in many indices is the most popular programming language  
**Translation:** 

**[9.62s] English:** in the world, or is always at least in the top two or three. We only had a limited time for  
**Translation:** 

**[15.44s] English:** this conversation, but I'm sure we'll talk again several times in this podcast.  
**Translation:** 

**[19.88s] English:** Quick summary of the sponsors, Public Goods, BetterHelp, and ExpressVPN. Please check out  
**Translation:** 

**[25.38s] English:** these sponsors in the description to get a discount and to support this podcast. As a side  
**Translation:** Vocabulary: sponsors: 赞助商

**[30.38s] English:** note, let me say that Java is the language with which I first learned object-oriented programming,  
**Translation:** 

**[36.40s] English:** and with it, the art and science of software engineering. Also, early on in my undergraduate  
**Translation:** 

**[42.62s] English:** education, I took a course on concurrent programming with Java. Looking back at that time,  
**Translation:** 

**[49.14s] English:** before I fell in love with neural networks, the art of parallel computing was both algorithmic  
**Translation:** 

**[55.38s] English:** and philosophically fascinating to me. The concept of a computer in my mind before then  
**Translation:** 

**[61.34s] English:** was something that does one thing at a time. The idea that we could create an abstraction  
**Translation:** Vocabulary: abstraction: 抽象; philosophically: 哲学地

**[66.90s] English:** of parallelism where you could do many things at the same time while still guaranteeing stability  
**Translation:** 

**[71.90s] English:** and correctness was beautiful. While some folks in college took drugs to expand their mind,  
**Translation:** Vocabulary: correctness: 正确性; guaranteeing: 保证

**[78.34s] English:** I took concurrent programming. If you enjoy this thing, subscribe on YouTube,  
**Translation:** 

**[83.48s] English:** review it with five stars on Apple Podcasts,  
**Translation:** Vocabulary: concurrent: 并行编程; subscribe: 订阅

**[85.62s] English:** follow on Spotify, support it on Patreon, or connect with me on Twitter at Lex Friedman.  
**Translation:** 

**[91.04s] English:** As usual, I'll do a few minutes of ads now and no ads in the middle. I try to make these  
**Translation:** Vocabulary: friedman: 弗里德曼

**[95.58s] English:** interesting, but I do give you timestamps, so go ahead and skip, but please do check out the  
**Translation:** 

**[100.56s] English:** sponsors by clicking the links in the description. It's the best way to support this podcast.  
**Translation:** Vocabulary: timestamps: 时间戳

**[106.64s] English:** This show is sponsored by Public Goods, the one-stop shop for affordable, sustainable,  
**Translation:** 

**[112.06s] English:** healthy household products.  
**Translation:** 

**[114.38s] English:** I take their official,  
**Translation:** 

**[115.38s] English:** and use their toothbrush, for example. Their products often have a minimum  
**Translation:** 

**[120.00s] English:** black and white design that I find to be just beautiful. Some people ask why I wear this black  
**Translation:** 

**[125.42s] English:** suit and tie. There's a simplicity to it that, to me, focuses my mind on the most important bits  
**Translation:** Vocabulary: simplicity: 简单性

**[132.00s] English:** of every moment of every day, pulling only at the thread of the essential in all that life has to  
**Translation:** 

**[138.92s] English:** throw at me. It's not about how I look, it's about how I feel. That's what design is to me,  
**Translation:** 

**[144.24s] English:** creating an inner conscious experience, not an external look. Anyway, Public Goods plants one  
**Translation:** 

**[151.66s] English:** tree for every order placed, which is kind of cool. Visit publicgoods.com slash lex or use code  
**Translation:** Vocabulary: publicgoods: 公共产品

**[157.90s] English:** lex at checkout to get 15 bucks off your first order. This show is also sponsored by BetterHelp,  
**Translation:** 

**[165.16s] English:** spelled H-E-L-P help. Check it out at betterhelp.com slash lex. They figure out what you need and match  
**Translation:** Vocabulary: betterhelp: 更好的帮助; bucks: 美元

**[172.42s] English:** you with a licensed professional.  
**Translation:** 

**[174.24s] English:** I'm a licensed professional therapist in under 48 hours. I chat with the person on there and enjoy  
**Translation:** Vocabulary: therapist: 心理咨询师

**[178.74s] English:** it. Of course, I also regularly talk to David Goggins these days, who is definitely not a  
**Translation:** 

**[185.02s] English:** licensed professional therapist, but he does help me meet his and my demons and become comfortable  
**Translation:** Vocabulary: demons: 内心阴影

**[192.28s] English:** to exist in their presence. Everyone is different, but for me, I think suffering is essential for  
**Translation:** 

**[198.44s] English:** creation, but you can suffer beautifully in a way that doesn't destroy you. I think therapy can  
**Translation:** 

**[204.14s] English:** help you.  
**Translation:** 

**[204.24s] English:** I think therapy can help in whatever form that therapy takes, and I do think that BetterHelp is an  
**Translation:** 

**[208.88s] English:** option worth trying. They're easy, private, affordable, and available worldwide. You can  
**Translation:** 

**[215.34s] English:** communicate by text anytime and schedule weekly audio and video sessions. Check it out at  
**Translation:** 

**[220.70s] English:** betterhelp.com slash lex. This show is also sponsored by ExpressVPN. You can use it to  
**Translation:** 

**[226.90s] English:** unlock movies and shows that are only available in other countries. I did this recently with  
**Translation:** 

**[232.44s] English:** Star Trek Discovery and UK Netflix. I'm a licensed professional therapist, and I think it's  
**Translation:** 

**[234.24s] English:** mostly because I wonder what it's like to live in London. I'm thinking of moving from  
**Translation:** 

**[239.84s] English:** Boston to London. I'm thinking of moving from Boston to London. I'm thinking of moving from  
**Translation:** 

**[240.00s] English:** Austin to a place where I can build the business I've always dreamed of building.  
**Translation:** 

**[244.16s] English:** London is probably not in the top three, but top 10 for sure.  
**Translation:** 

**[248.56s] English:** The number one choice currently is Austin, for many reasons that I'll probably speak  
**Translation:** 

**[253.30s] English:** to another time.  
**Translation:** 

**[254.86s] English:** San Francisco, unfortunately, dropped out from the number one spot, but it's still in  
**Translation:** 

**[259.44s] English:** the running.  
**Translation:** 

**[260.36s] English:** If you have advice, let me know.  
**Translation:** 

**[262.92s] English:** Anyway, check out ExpressVPN.  
**Translation:** 

**[264.32s] English:** It lets you change your location to almost 100 countries, and it's super fast.  
**Translation:** 

**[268.82s] English:** Go to expressvpn.com slash lexpod to get an extra three months of ExpressVPN for free.  
**Translation:** 

**[275.70s] English:** That's expressvpn.com slash lexpod.  
**Translation:** Vocabulary: expressvpn: 快速 vpn

**[280.16s] English:** And now, here's my conversation with James Gosling.  
**Translation:** 

**[284.74s] English:** I've read somewhere that the square root of two is your favorite irrational number.  
**Translation:** Vocabulary: irrational: 无理的

**[289.56s] English:** I have no idea where that got started.  
**Translation:** 

**[293.30s] English:** Is there any truth to it?  
**Translation:** 

**[295.04s] English:** Is there anything in mathematics or numbers that you find beautiful?  
**Translation:** 

**[298.82s] English:** Oh, well, there's lots of things in math that's really beautiful.  
**Translation:** 

**[305.02s] English:** You know, I used to consider myself really good at math, and these days I consider myself  
**Translation:** 

**[310.56s] English:** really bad at math.  
**Translation:** 

**[312.90s] English:** I never really had a thing for the square root of two, but when I was a teenager, there  
**Translation:** 

**[320.98s] English:** was this book called The Dictionary of Curious and Interesting Numbers, which, for some, I  
**Translation:** 

**[328.82s] English:** read through and damn near memorized the whole thing, and I started this weird habit of  
**Translation:** 

**[341.70s] English:** when I was, like, filling out checks, you know, or, you know, paying for things with  
**Translation:** Vocabulary: memorized: 背诵

**[347.72s] English:** credit cards, I would want to make the receipt add up to an interesting number.  
**Translation:** 

**[355.34s] English:** Is there some numbers that stuck with you that just kind of make you feel, you know,  
**Translation:** 

**[358.82s] English:** good?  
**Translation:** 

**[360.00s] English:** all have a story and fortunately i've actually mostly forgotten all of them um are they uh so  
**Translation:** 

**[369.28s] English:** like 42 uh well yeah i mean that one 42 is pretty magical and then the irrationals i mean but is  
**Translation:** 

**[376.48s] English:** there a square root of two story in there somewhere how did that well it's it's like  
**Translation:** Vocabulary: irrationals: 无理数

**[381.84s] English:** the only number that has destroyed a religion in which way well the the pathogorians they they  
**Translation:** 

**[391.76s] English:** believed that all numbers were perfect and you could represent anything as as a as a rational  
**Translation:** 

**[398.48s] English:** number and um in that in that time period um the this proof came out that  
**Translation:** 

**[412.32s] English:** there was no you know rational fraction whose value was equal to the square root of two  
**Translation:** 

**[420.80s] English:** and that that means nothing in this world is perfect not even mathematics well it means that  
**Translation:** 

**[427.76s] English:** your definition of perfect was imperfect well then there's the gato incompleteness theorems in the  
**Translation:** Vocabulary: incompleteness: 不完全; theorems: 定理

**[434.24s] English:** 20th century that ruined it once again for everybody yeah although although although  
**Translation:** 

**[439.76s] English:** girdle's theorem um  
**Translation:** Vocabulary: theorem: 定理

**[441.84s] English:** um you know the lesson i take from girdle's theorem is not that  
**Translation:** 

**[448.32s] English:** you know there are things you can't know which is fundamentally what it says um  
**Translation:** Vocabulary: fundamentally: 本质上

**[455.84s] English:** but you know people want black and white answers they want true or false  
**Translation:** 

**[462.16s] English:** um but if you if you allow a three-state logic that is true false or maybe  
**Translation:** 

**[471.84s] English:** then then life's good i feel like there's a parallel to uh modern political discourse in there  
**Translation:** 

**[478.88s] English:** somewhere but  
**Translation:** 

**[480.00s] English:** Let me ask, so with your kind of early love or appreciation of the beauty of mathematics,  
**Translation:** 

**[491.48s] English:** do you see a parallel between that world and the world of programming?  
**Translation:** 

**[496.40s] English:** You know, programming is all about logical structure,  
**Translation:** 

**[501.62s] English:** understanding the patterns that come out of computation,  
**Translation:** Vocabulary: computation: 计算

**[512.74s] English:** understanding sort of, I mean, it's often like, you know,  
**Translation:** 

**[518.32s] English:** the path through the graph of possibilities to find a short route.  
**Translation:** 

**[525.44s] English:** Meaning like find a short program that gets the job done kind of thing.  
**Translation:** 

**[531.06s] English:** Yeah.  
**Translation:** 

**[531.08s] English:** But.  
**Translation:** 

**[531.62s] English:** So then on the topic of irrational numbers, do you see, do you see programming,  
**Translation:** Vocabulary: irrational: 无理数

**[538.56s] English:** you just painted it so cleanly, it's a little of this trajectory to find like a nice little program,  
**Translation:** 

**[545.08s] English:** but do you see it as fundamentally messy?  
**Translation:** Vocabulary: trajectory: 轨迹

**[548.58s] English:** Maybe unlike mathematics?  
**Translation:** 

**[550.86s] English:** I don't think of it as, I mean, I mean, you know, you watch somebody who's good at math do math.  
**Translation:** 

**[557.10s] English:** And, you know, often it's, it's fairly messy.  
**Translation:** 

**[561.62s] English:** Sometimes it's kind of magical.  
**Translation:** 

**[567.20s] English:** When I was a grad student, one of the students, his name was Jim Sachs, was,  
**Translation:** 

**[577.72s] English:** he had this, this, this, this, this reputation of being sort of a walking, talking human,  
**Translation:** Vocabulary: sachs: 萨克斯

**[586.54s] English:** theorem proving machine.  
**Translation:** 

**[589.00s] English:** And if you were having a hard problem with something,  
**Translation:** Vocabulary: theorem: 定理

**[591.50s] English:** you could do it.  
**Translation:** 

**[591.60s] English:** You could just like a costume in the hall and say, Jim, and, and he would do this, this,  
**Translation:** 

**[598.84s] English:** this funny thing where he.  
**Translation:** 

**[600.00s] English:** would stand up straight his eyes would kind of defocus he'd go uh you know just just like you  
**Translation:** 

**[606.40s] English:** you know like like something in today's movies yeah and then you straighten up and say and log  
**Translation:** 

**[612.40s] English:** in and walk away and and and you go well okay so and login is the answer how did he get there  
**Translation:** Vocabulary: login: 登录; straighten: 整理

**[624.08s] English:** by which time he's you know down the hallway somewhere yeah  
**Translation:** 

**[627.60s] English:** hey there's just the the oracle the black box just gives you the answer yeah and then you have  
**Translation:** Vocabulary: hallway: 走廊

**[632.00s] English:** to figure out the path from the question to the answer i think in one of the videos i watched you  
**Translation:** 

**[638.16s] English:** mentioned uh don knuth uh well at least recommending his uh you know his his book  
**Translation:** Vocabulary: knuth: 高纳德

**[646.00s] English:** is something people should read oh yeah but in terms of you know theoretical computer science  
**Translation:** 

**[653.76s] English:** do you do you see something beautiful  
**Translation:** 

**[657.60s] English:** and inspiring to you speaking of n log n in your work on programming languages  
**Translation:** 

**[663.52s] English:** uh that's in the in the that whole world of algorithms and complexity and you know these  
**Translation:** 

**[670.40s] English:** kinds of more formal mathematical things um or did that not really stick with you in your  
**Translation:** 

**[677.68s] English:** programming life it did stick pretty clearly for me because one of the things that i care about is  
**Translation:** 

**[687.60s] English:** being able to  
**Translation:** 

**[692.56s] English:** sort of look at a piece of code and and be able to prove to myself that it works  
**Translation:** 

**[700.48s] English:** um you know and you know so so for example i find that um i'm i'm at odds with many of the people  
**Translation:** 

**[712.96s] English:** around me over um issues about like  
**Translation:** 

**[718.24s] English:** how you  
**Translation:** 

**[719.76s] English:** look  
**Translation:** 

**[722.56s] English:** so  
**Translation:** 

**[726.56s] English:** i  
**Translation:** 

**[728.56s] English:** i  
**Translation:** 

**[730.56s] English:** i  
**Translation:** 

**[732.56s] English:** i  
**Translation:** 

**[734.56s] English:** i  
**Translation:** 

**[736.56s] English:** i  
**Translation:** 

**[738.56s] English:** i  
**Translation:** 

**[740.56s] English:** i  
**Translation:** 

**[742.56s] English:** i  
**Translation:** 

**[744.56s] English:** i  
**Translation:** 

**[746.56s] English:** i  
**Translation:** 

**[720.00s] English:** layout a piece of software right you know so so software engineers get really cranky about  
**Translation:** 

**[727.98s] English:** how they format their the documents that are the programs you know where they put new lines and  
**Translation:** Vocabulary: cranky: 易怒; layout: 布局

**[733.34s] English:** where they put you know the braces the braces and all the rest of that right and i tend to go for  
**Translation:** 

**[742.22s] English:** a style that's very dense to minimize the white space um yeah well to maximize  
**Translation:** Vocabulary: braces: 牙套; maximize: 最大化

**[752.34s] English:** the amount that i can see at once right so i like to be able to see a whole function  
**Translation:** 

**[759.90s] English:** and to understand what it does rather than have to go scroll scroll scroll and remember right yeah  
**Translation:** Vocabulary: scroll: 滚动查看

**[766.26s] English:** i'm with you on that yeah that's and people don't like that  
**Translation:** 

**[772.22s] English:** yeah i've i've had i've had you know multiple times when engineering teams have  
**Translation:** 

**[778.82s] English:** uh staged what was effectively an intervention  
**Translation:** 

**[783.22s] English:** um you know where they they invite me to a meeting and everybody's arrived before me  
**Translation:** 

**[792.00s] English:** and they all look at me and say james about your coding style  
**Translation:** 

**[796.88s] English:** i'm sort of an odd  
**Translation:** 

**[802.22s] English:** person to be programming because i don't think very well verbally  
**Translation:** 

**[809.08s] English:** um i am just naturally a slow reader  
**Translation:** Vocabulary: verbally: 口头地

**[815.22s] English:** um i'm what most people would call a visual thinker so when you think about a program what  
**Translation:** 

**[823.72s] English:** what do you see i see pictures right so when i look at a piece of code on a piece of paper  
**Translation:** 

**[831.34s] English:** it's  
**Translation:** 

**[832.22s] English:** it very quickly gets transformed into a picture  
**Translation:** 

**[835.46s] English:** um and you know it's almost like  
**Translation:** 

**[840.00s] English:** a piece of machinery with you know this connected to that and like these gears yeah yeah i i see  
**Translation:** Vocabulary: machinery: 机器设备

**[849.60s] English:** them more more like that than i see the the the the sort of verbal structure or the lexical  
**Translation:** 

**[856.64s] English:** structure of of letters so then when you look at the program that's why you want to see it all in  
**Translation:** Vocabulary: lexical: 词法的

**[860.96s] English:** the same place then you can just map it to something visual yeah just kind of like like  
**Translation:** 

**[865.68s] English:** it leaps off the page at me and yeah what are the inputs where the outputs what the heck is  
**Translation:** 

**[871.28s] English:** this thing doing yeah yeah getting a whole vision of it can we uh go back into your memory memory  
**Translation:** 

**[880.24s] English:** long-term memory access what's the first program you've ever written  
**Translation:** 

**[887.28s] English:** oh i have no idea what the first one was i mean i i know the first machine that i  
**Translation:** 

**[895.36s] English:** learned  
**Translation:** 

**[895.68s] English:** that i learned to program on what is it was a a pdp8  
**Translation:** 

**[902.88s] English:** um at the university of calgary do you remember the specs oh yeah it so so the thing had  
**Translation:** Vocabulary: calgary: 卡尔加里; specs: 规格

**[910.88s] English:** 4k of ram nice 12-bit words the clock rate was um it was about a third of a megahertz  
**Translation:** 

**[925.68s] English:** oh so i didn't even get to the to the m okay yeah yeah so you know we're we're like 10 000 times  
**Translation:** 

**[934.64s] English:** faster these days um and was this kind of like a super compute like a serious computer for no the  
**Translation:** 

**[942.88s] English:** pdpi was the the first thing that people were calling like mini computer got it they were  
**Translation:** 

**[951.52s] English:** sort of inexpensive enough that that a university lab could  
**Translation:** 

**[955.68s] English:** maybe afford to buy one and was there time  
**Translation:** 

**[959.92s] English:** to  
**Translation:** 

**[962.88s] English:** do  
**Translation:** 

**[966.88s] English:** you  
**Translation:** 

**[966.96s] English:** know  
**Translation:** 

**[968.88s] English:** so  
**Translation:** 

**[970.88s] English:** i'm  
**Translation:** 

**[972.88s] English:** i'm  
**Translation:** 

**[974.88s] English:** i'm  
**Translation:** 

**[976.88s] English:** i'm  
**Translation:** 

**[978.88s] English:** i'm  
**Translation:** 

**[980.88s] English:** i'm  
**Translation:** 

**[982.88s] English:** i'm  
**Translation:** 

**[984.88s] English:** i'm  
**Translation:** 

**[984.96s] English:** i'm  
**Translation:** 

**[985.04s] English:** i'm  
**Translation:** 

**[985.12s] English:** i'm  
**Translation:** 

**[985.20s] English:** i'm  
**Translation:** 

**[985.28s] English:** i'm  
**Translation:** 

**[985.36s] English:** i'm  
**Translation:** 

**[985.60s] English:** i'm  
**Translation:** 

**[960.00s] English:** sharing all that kind of stuff um there there actually was a time sharing os for that but  
**Translation:** 

**[967.12s] English:** it wasn't used really widely the machine that i learned on was one that was  
**Translation:** 

**[974.32s] English:** kind of hidden in the back corner of the of the computer center um and it was it was bought as a  
**Translation:** 

**[986.08s] English:** as part of a a um project to do computer networking um but  
**Translation:** 

**[996.64s] English:** you know they didn't actually use it very much it was mostly just kind of sitting there  
**Translation:** 

**[1002.08s] English:** and it was kind of sitting there and i noticed it was just kind of sitting there and  
**Translation:** 

**[1007.60s] English:** so i started fooling around with it and nobody seemed to mind so i just kept doing that and  
**Translation:** 

**[1016.08s] English:** had a keyboard and like a monitor oh this is way before monitors were common  
**Translation:** 

**[1022.48s] English:** so it was it was literally a model 33 teletype okay with a paper tape reader  
**Translation:** 

**[1031.92s] English:** okay so the user interface wasn't very good yeah yeah it was it was the first computer ever  
**Translation:** Vocabulary: interface: 用户界面; teletype: 电报机

**[1039.04s] English:** built with integrated circuits but by integrated circuits i mean that they would  
**Translation:** 

**[1046.08s] English:** have like 10 or 12 transistors on one piece of silicon nice not the 10 or 12 billion  
**Translation:** Vocabulary: circuits: 电路; transistors: 晶体管

**[1055.92s] English:** that machines have today so what does that i mean feel like if you remember those i mean did you  
**Translation:** 

**[1065.28s] English:** have kind of inklings of the the magic of exponential kind of improvement of moore's law  
**Translation:** Vocabulary: exponential: 指数的; inklings: 预感

**[1072.72s] English:** of the potential of the future that was at your fingertips  
**Translation:** 

**[1076.08s] English:** dips kind of thing or was it just a cool yeah it was just a toy  
**Translation:** 

**[1080.00s] English:** You know, I had always liked building stuff, but one of the problems with building stuff is that you need to have parts.  
**Translation:** 

**[1088.78s] English:** You know, you need to have pieces of wood or wire or switches or stuff like that, and those all cost money.  
**Translation:** 

**[1096.90s] English:** And here you could build quite a lot of things.  
**Translation:** 

**[1097.90s] English:** You could build arbitrarily complicated things, and I didn't need any physical materials.  
**Translation:** Vocabulary: arbitrarily: 任意地

**[1104.80s] English:** It required no money.  
**Translation:** 

**[1107.12s] English:** That's a good way to put programming.  
**Translation:** 

**[1108.86s] English:** You're right.  
**Translation:** 

**[1109.40s] English:** If you love building things, it's completely accessible.  
**Translation:** 

**[1117.24s] English:** You don't need anything.  
**Translation:** 

**[1118.84s] English:** Anybody from anywhere could just build something really cool.  
**Translation:** 

**[1121.56s] English:** Yeah.  
**Translation:** 

**[1122.08s] English:** Yeah.  
**Translation:** 

**[1122.96s] English:** If you've got access to a computer, you can build all kinds of crazy stuff.  
**Translation:** 

**[1131.34s] English:** And, you know, when you were somebody like me who had, like,  
**Translation:** 

**[1139.40s] English:** really no money, and, I mean, I remember just lusting after being able to buy, like, a transistor, you know,  
**Translation:** 

**[1155.70s] English:** and when I would do sort of electronics kind of projects, they were mostly made, done by, like, dumpster diving for trash, you know,  
**Translation:** Vocabulary: lusting: 渴望; transistor: 晶体管

**[1167.36s] English:** and, you know, one of my big hobbies.  
**Translation:** 

**[1169.40s] English:** One of my big hobbies when I was a kid, when I was a kid, when I was a kid, when I was a kid, when I was a kid, when I was a kid,  
**Translation:** 

**[1171.12s] English:** was discarded relay racks from the back of the phone company switching center.  
**Translation:** 

**[1177.46s] English:** Oh, nice.  
**Translation:** 

**[1178.52s] English:** That was the big memorable treasure.  
**Translation:** 

**[1181.44s] English:** Oh, yeah.  
**Translation:** 

**[1182.14s] English:** Yeah.  
**Translation:** 

**[1182.44s] English:** That was a really...  
**Translation:** 

**[1183.32s] English:** What did you use that for?  
**Translation:** 

**[1184.82s] English:** I built a machine that played tic-tac-toe.  
**Translation:** 

**[1190.34s] English:** Nice.  
**Translation:** 

**[1191.22s] English:** Out of relays.  
**Translation:** 

**[1191.98s] English:** Because, of course, the thing that was really hard was that all the relays required a specific voltage.  
**Translation:** 

**[1199.40s] English:** Yeah.  
**Translation:** Vocabulary: voltage: 电压

**[1199.52s] English:** Right.  
**Translation:** 

**[1200.00s] English:** But getting a power supply that would do that voltage was pretty hard.  
**Translation:** 

**[1206.18s] English:** And since I had a bunch of trashed television sets, I had to sort of cobble together something that was wrong but worked.  
**Translation:** 

**[1219.00s] English:** So, I was actually running these relays at 300 volts, and none of the electrical connections were properly sealed off.  
**Translation:** Vocabulary: cobble: 凑合; volts: 伏特

**[1232.30s] English:** I'm surprised you survived that period of your life.  
**Translation:** 

**[1236.38s] English:** Oh, for so many reasons.  
**Translation:** 

**[1238.44s] English:** For so many reasons.  
**Translation:** 

**[1240.50s] English:** I mean, it's pretty common for teenage geeks to discover, oh, thermite.  
**Translation:** Vocabulary: geeks: 极客; thermite: 热能剂

**[1247.38s] English:** That's real easy to make.  
**Translation:** 

**[1249.98s] English:** Yeah.  
**Translation:** 

**[1250.90s] English:** Well, I'm glad you did.  
**Translation:** 

**[1252.78s] English:** But do you remember what program in Calgary that you wrote, anything that stands out?  
**Translation:** Vocabulary: calgary: 卡尔加里

**[1261.84s] English:** And what language?  
**Translation:** 

**[1263.78s] English:** Well, so, mostly, anything of any size was assembly code.  
**Translation:** 

**[1274.62s] English:** And actually, before I learned assembly code, there was this programming language.  
**Translation:** 

**[1279.00s] English:** There was a language on the PDP-8 called Focal 5.  
**Translation:** 

**[1282.66s] English:** And Focal 5 was kind of like a really stripped-down Fortran.  
**Translation:** 

**[1288.76s] English:** And I remember playing, you know, building programs that did things like play Blackjack or Solitaire or...  
**Translation:** Vocabulary: solitaire: 单人纸牌游戏

**[1302.06s] English:** And for some reason or other, the things that I really liked were ones where they were just like plotting graphs.  
**Translation:** 

**[1309.00s] English:** So, something with, like, a function or a data, and then you'd plot it.  
**Translation:** Vocabulary: plotting: 绘制图表

**[1315.50s] English:** Yeah.  
**Translation:** 

**[1316.78s] English:** Yeah, I did a bunch of those things.  
**Translation:** 

**[1319.22s] English:** And...  
**Translation:** 

**[1320.00s] English:** Ooh, pretty pictures.  
**Translation:** 

**[1322.86s] English:** And so this would like print out, again, no monitors.  
**Translation:** 

**[1327.38s] English:** Right.  
**Translation:** 

**[1327.78s] English:** So it was like on a teletype.  
**Translation:** 

**[1331.48s] English:** Yeah.  
**Translation:** Vocabulary: teletype: 电报机

**[1332.82s] English:** So it's using something that's kind of like a typewriter and then using those to plot functions.  
**Translation:** 

**[1341.72s] English:** So when, I apologize to romanticize things, but when did you first fall in love with programming?  
**Translation:** Vocabulary: typewriter: 打字机

**[1351.62s] English:** You know, what was the first programming language?  
**Translation:** 

**[1354.22s] English:** Like as a serious, maybe software engineer, where you thought this is a beautiful thing?  
**Translation:** 

**[1360.00s] English:** I guess I never really thought of any particular language as being like beautiful because it was never really about the language for me.  
**Translation:** 

**[1367.84s] English:** It was about what you could do with it.  
**Translation:** 

**[1371.72s] English:** And, you know, even today, you know, people try to get me into arguments about particular forms of syntax or this or that.  
**Translation:** 

**[1380.50s] English:** And I'm like, who cares?  
**Translation:** Vocabulary: syntax: 句法

**[1383.00s] English:** You know, it's about what you can do, not how you spell the word.  
**Translation:** 

**[1390.56s] English:** And, you know, so back in those days, I learned like PL1 and Fortran and COBOL.  
**Translation:** 

**[1397.44s] English:** And, you know, by the time that people were...  
**Translation:** 

**[1402.04s] English:** Willing to hire me to do stuff, you know, it was mostly assembly code and, you know, PGP8 assembly code and Fortran code and control data assembly code for like the CDC 6400, which was an early, I guess, supercomputer.  
**Translation:** 

**[1422.74s] English:** Even though that supercomputer has less compute power than my phone by a lot.  
**Translation:** 

**[1430.16s] English:** And that was mostly...  
**Translation:** 

**[1431.72s] English:** Like you said, Fortran world.  
**Translation:** 

**[1434.94s] English:** That said, you've also showed appreciation for the greatest language.  
**Translation:** 

**[1440.00s] English:** ever that i think everyone agrees is lisp um well lisp is definitely on my list  
**Translation:** 

**[1447.30s] English:** of the greatest ones that have existed is it at number one or i mean um are you i mean you know  
**Translation:** 

**[1456.46s] English:** that you know the thing is that it's that you know i wouldn't put it number one no is it the  
**Translation:** 

**[1463.90s] English:** parentheses what uh um what do you know what do you not love about lisp um  
**Translation:** Vocabulary: parentheses: 圆括号

**[1471.88s] English:** well i guess the number one thing to not love about it is so freaking many parentheses yeah  
**Translation:** 

**[1479.24s] English:** um on the on the love thing is you know out of those tons of parentheses you actually get  
**Translation:** Vocabulary: freaking: damn

**[1488.80s] English:** an interesting language structure and i've always thought that there was a friendlier  
**Translation:** 

**[1493.90s] English:** version of lisp hiding out there somewhere um but i've never really spent much time  
**Translation:** Vocabulary: friendlier: 更亲切的

**[1500.76s] English:** thinking about thinking about it but you know so like like up the food chain for me um  
**Translation:** 

**[1508.56s] English:** then from lisp is simula which a very small number of people have ever used  
**Translation:** Vocabulary: simula: 模拟语言

**[1515.76s] English:** but a lot of people i think had a huge influence right yeah the programming but  
**Translation:** 

**[1520.84s] English:** in the simula i apologize  
**Translation:** 

**[1523.90s] English:** if i'm wrong on this but is that one of the first functional languages um or no no it was it was it  
**Translation:** 

**[1529.52s] English:** was the first object-oriented programming language got it it's really where object-oriented and  
**Translation:** 

**[1535.68s] English:** languages sort of came together um and it was also the the language where co-routines first  
**Translation:** 

**[1545.66s] English:** showed up as a part of the language so you could have a programming style that was  
**Translation:** 

**[1552.50s] English:** um  
**Translation:** 

**[1552.90s] English:** you could have a programming style that was  
**Translation:** 

**[1553.86s] English:** you could have a programming style that was  
**Translation:** 

**[1553.88s] English:** you could think of it as multi uh sort of multi-threaded with a lot of parallel parallelism  
**Translation:** 

**[1560.00s] English:** really there's ideas of parallelism in there yeah yeah so that was that was  
**Translation:** 

**[1567.06s] English:** back at you know itself so the first stimulus back was simula 67 for him like  
**Translation:** 

**[1573.24s] English:** 1967 yeah Wow so it had it had co routines which are almost threads the  
**Translation:** 

**[1582.10s] English:** the thing about co routines is that they don't have true concurrency so you can  
**Translation:** Vocabulary: concurrency: 并行执行

**[1587.68s] English:** get away without really complex locking you can't use of Lee do co routines on a  
**Translation:** 

**[1596.38s] English:** on the multi-core machine or if you try to do core routines on the multi-core  
**Translation:** 

**[1602.56s] English:** mute machine you don't actually get to use the multiple cores at it either that  
**Translation:** 

**[1608.92s] English:** are you you know because you start then having to get into the universe of you  
**Translation:** 

**[1615.22s] English:** know semaphores and locks and things like that  
**Translation:** 

**[1617.68s] English:** but you know in terms of the the style of programming you could write code and  
**Translation:** Vocabulary: semaphores: 信号量

**[1627.10s] English:** think think of it as being multi-threaded the the mental model was  
**Translation:** 

**[1633.82s] English:** very much a multi-threaded one and all kinds of problems you could approach  
**Translation:** 

**[1639.16s] English:** very differently to return to the world of this for a brief moment you  
**Translation:** 

**[1648.30s] English:** nice to see you in late Octoberrek you at CMU you've you wrote a version of  
**Translation:** 

**[1654.14s] English:** Vmax yeah that I think was very impactful on the history of Vmax what  
**Translation:** 

**[1661.30s] English:** was your motivation for doing so at that time so that was in like 85 or 86 I had  
**Translation:** 

**[1674.10s] English:** been using Unix for a few years and  
**Translation:** 

**[1677.68s] English:** And, um,  
**Translation:** 

**[1680.00s] English:** Most of the editing was this tool called EDI, which was sort of an ancestor of VI.  
**Translation:** 

**[1690.50s] English:** Is it a pretty good editor?  
**Translation:** 

**[1693.18s] English:** Not a good editor?  
**Translation:** 

**[1693.98s] English:** Well, if what you're using, if your input device is a teletype, it's pretty good.  
**Translation:** Vocabulary: teletype: 电报机

**[1701.36s] English:** But it's certainly more humane than TECO, which was kind of the common thing in a lot of the DEC universe at the time.  
**Translation:** 

**[1712.44s] English:** TECO is spelled T-K?  
**Translation:** 

**[1714.60s] English:** No, TECO, T-E-C-O, the text editor and corrector.  
**Translation:** 

**[1719.62s] English:** Corrector, wow, so many features.  
**Translation:** 

**[1723.28s] English:** And the original Emacs came out as, so Emacs stands for editor macros.  
**Translation:** 

**[1731.36s] English:** And TECO had a way of writing macros.  
**Translation:** Vocabulary: emacs: emacs编辑器; macros: 宏命令

**[1736.68s] English:** And so the original Emacs from MIT sort of started out as a collection of macros for TECO.  
**Translation:** 

**[1746.96s] English:** But then, you know, the sort of Emacs style got popular originally at MIT.  
**Translation:** 

**[1754.68s] English:** And then people did a few other implementations of Emacs.  
**Translation:** 

**[1761.36s] English:** That were, you know, the code base was entirely different.  
**Translation:** Vocabulary: implementations: 实现版本

**[1765.98s] English:** But it was sort of the philosophical style of the original Emacs.  
**Translation:** 

**[1770.84s] English:** What was the philosophy of Emacs?  
**Translation:** Vocabulary: philosophical: 哲学思想

**[1773.24s] English:** And by the way, were all the implementations always in C?  
**Translation:** 

**[1776.76s] English:** No.  
**Translation:** 

**[1777.60s] English:** And how does Lisp fit into the picture?  
**Translation:** 

**[1779.70s] English:** No, so the very first Emacs was written as a bunch of macros for the TECO text editor.  
**Translation:** 

**[1786.40s] English:** Wow, that's so interesting.  
**Translation:** 

**[1787.60s] English:** And the macro language.  
**Translation:** Vocabulary: macro: 宏命令

**[1791.36s] English:** The macro language for TECO was probably the most ridiculously obscure format.  
**Translation:** 

**[1798.90s] English:** You know, if you just look.  
**Translation:** Vocabulary: obscure: 晦涩; ridiculously: 荒谬地

**[1800.00s] English:** a tico program on a on a page you think it was just random characters it really looks like just  
**Translation:** 

**[1807.60s] English:** line noise just kind of like latex or something oh worse way worse than latex way way worse than  
**Translation:** Vocabulary: latex: 排版乱码

**[1816.08s] English:** latex um but you know if you use tico a lot which i did the the tico was completely optimized for  
**Translation:** 

**[1826.32s] English:** touch typing at high speed um so there were no two character commands well there were a few but  
**Translation:** Vocabulary: optimized: 优化

**[1837.20s] English:** mostly they were just one character so every character on the keyboard was a separate command  
**Translation:** 

**[1842.56s] English:** um and actually every character on the keyboard was usually two or three com commands because you  
**Translation:** 

**[1849.20s] English:** know you hit shift and control and all of those things you know it's just a way of very tightly  
**Translation:** 

**[1854.48s] English:** encoding it  
**Translation:** Vocabulary: encoding: 编码

**[1856.48s] English:** and mostly what emacs did was it made that that visual right so one way to think of tico is use  
**Translation:** 

**[1867.84s] English:** emacs with your eyes closed um where you have to maintain a mental model of you know sort of  
**Translation:** Vocabulary: emacs: 编辑器

**[1878.72s] English:** a mental image of your document you have to go okay so the the cursor is between the a and the  
**Translation:** 

**[1886.32s] English:** e and i want to exchange those so i do these these things right so it it almost it is almost exactly  
**Translation:** 

**[1896.32s] English:** the emacs command set well it's roughly approximate roughly the same as emacs command set  
**Translation:** 

**[1902.72s] English:** but using emacs with your eyes closed  
**Translation:** Vocabulary: approximate: 大致相当于

**[1907.76s] English:** so what emacs you know part of what emacs added to the whole thing was was being able to visually see  
**Translation:** 

**[1916.32s] English:** what you were editing um in a form that  
**Translation:** 

**[1920.00s] English:** that matched your document.  
**Translation:** 

**[1925.50s] English:** And a lot of things changed in the command set.  
**Translation:** 

**[1932.00s] English:** Because it was programmable, it was really flexible.  
**Translation:** 

**[1936.02s] English:** You could add new commands for all kinds of things.  
**Translation:** 

**[1938.54s] English:** And then people rewrote Emacs multiple times in Lisp.  
**Translation:** 

**[1944.76s] English:** There was one done at MIT for the Lisp machine.  
**Translation:** 

**[1948.20s] English:** There was one done for Multics.  
**Translation:** 

**[1951.56s] English:** And one summer, I got a summer job  
**Translation:** Vocabulary: multics: mú lǐ cī sī

**[1955.10s] English:** to work on the Pascal compiler for Multics.  
**Translation:** 

**[1960.36s] English:** And that was actually the first time I used Emacs.  
**Translation:** Vocabulary: pascal: 帕斯卡

**[1966.26s] English:** And so.  
**Translation:** 

**[1967.52s] English:** To write the compilers.  
**Translation:** Vocabulary: compilers: 编译器

**[1968.90s] English:** You've worked on compilers, too.  
**Translation:** 

**[1970.48s] English:** It's fascinating.  
**Translation:** 

**[1972.26s] English:** Yeah, so I did a lot of work.  
**Translation:** 

**[1975.68s] English:** I mean, I spent like a really intense,  
**Translation:** 

**[1978.18s] English:** three months working on this Pascal compiler.  
**Translation:** 

**[1983.46s] English:** Basically living in Emacs.  
**Translation:** 

**[1985.36s] English:** And it was the one written in Mac Lisp by Bernie Greenberg.  
**Translation:** 

**[1991.38s] English:** And I thought, wow, this is just a way better way to do editing.  
**Translation:** Vocabulary: greenberg: 格林伯格

**[1999.18s] English:** And then I got back to CMU, where we had kind of one  
**Translation:** 

**[2004.16s] English:** of everything and two of a bunch of things.  
**Translation:** 

**[2007.54s] English:** And four of a few things.  
**Translation:** 

**[2008.92s] English:** And since I mostly worked in the Unix universe,  
**Translation:** 

**[2014.92s] English:** and Unix didn't have an Emacs, I decided  
**Translation:** 

**[2018.10s] English:** that I needed to fix that problem.  
**Translation:** Vocabulary: emacs: 编辑器

**[2021.54s] English:** So I wrote this implementation of Emacs in C.  
**Translation:** 

**[2026.54s] English:** Because at the time, C was really the only language  
**Translation:** Vocabulary: implementation: 实现

**[2029.74s] English:** that worked on Unix.  
**Translation:** 

**[2034.54s] English:** And you were comfortable with C as well?  
**Translation:** 

**[2036.94s] English:** Yeah.  
**Translation:** 

**[2037.54s] English:** Oh, yeah.  
**Translation:** 

**[2038.04s] English:** At that point?  
**Translation:** 

**[2039.20s] English:** Yeah.  
**Translation:** 

**[2039.70s] English:** At that time.  
**Translation:** 

**[2040.00s] English:** i had done a lot of c coding that this was in like 86 um and you know it was running well enough to  
**Translation:** 

**[2053.12s] English:** be used for me to use it to edit itself within a month or two and um then it kind of  
**Translation:** 

**[2060.80s] English:** took over the university and and then spread and then yeah and then it went outside the  
**Translation:** 

**[2067.20s] English:** and largely because unix kind of took over the research community on the on the on the arpanet  
**Translation:** 

**[2078.16s] English:** then and emacs was was kind of the best editor out there it kind of took over and there was a  
**Translation:** Vocabulary: arpanet: 阿帕网

**[2085.76s] English:** actually a brief period where um i actually had login ids on every non-military host on the on  
**Translation:** 

**[2095.76s] English:** the arpanet  
**Translation:** Vocabulary: login: 登录

**[2097.20s] English:** um you know because people would say oh can we install this and and i'd like well  
**Translation:** 

**[2105.60s] English:** yeah but you'll need some help  
**Translation:** 

**[2109.20s] English:** uh the days when security wasn't uh when nobody cared nobody cared yeah you can ask briefly  
**Translation:** 

**[2117.60s] English:** what were those early days of arpanet and the internet like what was uh what i mean  
**Translation:** 

**[2125.60s] English:** did you uh again  
**Translation:** 

**[2127.20s] English:** sorry for the silly question but could you have possibly imagined  
**Translation:** 

**[2131.92s] English:** that uh the the internet would look like what it is today you know some of it is remarkably unchanged  
**Translation:** 

**[2142.40s] English:** so like one of the things that i noticed really early on  
**Translation:** Vocabulary: remarkably: 非常; unchanged: 未变

**[2147.36s] English:** um at you know when i was in at carnegie mellon was that a lot of social life  
**Translation:** 

**[2157.20s] English:** became centered around the arpanet  
**Translation:** Vocabulary: carnegie: 卡内基; mellon: 梅隆

**[2168.40s] English:** so  
**Translation:** 

**[2175.76s] English:** what i mean by that is that i know schumann said that he was very interested in our app but i didn't  
**Translation:** 

**[2180.00s] English:** understand him and i'm kind of wondering why you think that's what he was trying to get at and i'm  
**Translation:** 

**[2182.48s] English:** more interested in the idea that we use a server that's kind of like a product or something like that  
**Translation:** 

**[2184.22s] English:** but i think that you know something like that to me was that there was this idea that i wanted to focus on  
**Translation:** 

**[2185.36s] English:** this project and then i would say okay that's all we're gonna do we're gonna take this project and we're going to  
**Translation:** 

**[2160.00s] English:** And so things like, you know, between email and text messaging, because, you know, text messaging was a part of the ARPANET really early on.  
**Translation:** 

**[2171.24s] English:** There were no cell phones, but, you know, you're sitting at a terminal and you're typing stuff.  
**Translation:** 

**[2177.26s] English:** And essentially email or like what is just like like a one line message.  
**Translation:** 

**[2182.14s] English:** Right. So. So. So. Oh, cool. So like chat, like chat.  
**Translation:** 

**[2186.40s] English:** Yeah. Right. So it's like like sending a one line message to somebody. Right.  
**Translation:** 

**[2191.78s] English:** And and so pretty much everything from, you know, arranging lunch to going out on dates, you know, was all like driven by social media.  
**Translation:** 

**[2207.92s] English:** Social media. Right. In the in the in the 80s.  
**Translation:** 

**[2212.92s] English:** Easier than phone calls. Yeah.  
**Translation:** 

**[2214.38s] English:** You know, and.  
**Translation:** 

**[2216.40s] English:** My life had gotten to where, you know, I was, you know, living on social media, you know, from like the early mid 80s.  
**Translation:** 

**[2231.04s] English:** And and so when when it sort of transformed into the Internet and social media explodes, I was kind of like, what's the big deal?  
**Translation:** 

**[2240.88s] English:** Yeah, it's just a scale thing. It's it's right.  
**Translation:** Vocabulary: explodes: 爆发

**[2244.70s] English:** The scale thing.  
**Translation:** 

**[2246.40s] English:** It's just astonishing.  
**Translation:** Vocabulary: astonishing: 令人惊讶的

**[2247.86s] English:** Yeah.  
**Translation:** 

**[2249.12s] English:** But the fundamentals in some ways.  
**Translation:** Vocabulary: fundamentals: 基础原则

**[2252.02s] English:** The fundamentals of have have hardly changed.  
**Translation:** 

**[2256.16s] English:** And, you know, the the technologies behind the networking have changed significantly.  
**Translation:** 

**[2262.50s] English:** The you know, the the the watershed moment of, you know, going from the internet to the Internet and then people starting to just scale.  
**Translation:** 

**[2276.18s] English:** And scale and scale.  
**Translation:** Vocabulary: watershed: 转折点

**[2277.30s] English:** I mean, the the.  
**Translation:** 

**[2280.00s] English:** the scaling that happened in the early 90s and the way that so many vested interests  
**Translation:** Vocabulary: vested: 有既得利益的

**[2289.56s] English:** fought the internet oh who oh interesting what was the oh because you can't really control the  
**Translation:** 

**[2296.90s] English:** internet yeah so the internet so so so fundamentally the you know the cable tv  
**Translation:** Vocabulary: fundamentally: 从根本上

**[2305.06s] English:** companies and broadcasters and phone companies um you know at the deepest fibers of their being  
**Translation:** 

**[2315.46s] English:** they hated the internet but it was often kind of a funny thing because  
**Translation:** Vocabulary: broadcasters: 电视台

**[2324.26s] English:** um you know so so so think of a cable company right most of the employees  
**Translation:** 

**[2335.06s] English:** of the cable company their job is getting tv shows movies or whatever out to their customers  
**Translation:** 

**[2345.62s] English:** they view their business as serving their customers  
**Translation:** 

**[2351.60s] English:** um but as you climb up the hierarchy in the in the cable companies that view shifts because  
**Translation:** Vocabulary: hierarchy: 等级结构

**[2363.24s] English:** um  
**Translation:** 

**[2363.74s] English:** um  
**Translation:** 

**[2365.06s] English:** Thank you  
**Translation:** 

**[2372.50s] English:** always been selling eyeballs to advertisers right um and you know that view of of like a cable company  
**Translation:** Vocabulary: advertisers: 广告商; eyeballs: 观众数量

**[2385.04s] English:** didn't really dawn on most people who worked at the cable companies but you know we you know I  
**Translation:** 

**[2393.60s] English:** had various dust-ups  
**Translation:** 

**[2395.06s] English:** with various cable companies, where you could see in the stratified layer  
**Translation:** 

**[2400.00s] English:** of the corporation that that this this this this this view of you know the reason that you have  
**Translation:** Vocabulary: stratified: 分层的

**[2407.92s] English:** you know cable tv is to capture eyeballs you know they're they didn't see it that way well  
**Translation:** 

**[2415.44s] English:** so so the people who the most the people who worked at the phone company  
**Translation:** 

**[2419.76s] English:** are at the cable companies their view was that their their job was getting delightful content  
**Translation:** 

**[2428.08s] English:** out to their customers and their customers would pay for them would pay for that higher up  
**Translation:** 

**[2434.64s] English:** they viewed this as as a way of attracting eyeballs to them and and then what they were  
**Translation:** 

**[2444.72s] English:** really doing was selling the eyeballs that were glued to their content to the advertisers to the  
**Translation:** 

**[2452.48s] English:** advertisers yeah and so the internet was a competition in that sense right and and  
**Translation:** 

**[2458.08s] English:** and and they were right well yeah um i mean there there was one proposal that we  
**Translation:** 

**[2466.56s] English:** sent that that we one detailed proposal that we um wrote up you know back at that sun in the  
**Translation:** 

**[2475.84s] English:** in the early 90s that was essentially like look anybody you know with it with internet  
**Translation:** 

**[2481.44s] English:** technologies anybody can become provider of of content so  
**Translation:** 

**[2488.96s] English:** you could be distributing home movies to your parents or your cousins or your who are anywhere  
**Translation:** 

**[2498.80s] English:** else right so anybody can become a publisher wow you were thinking about that already yeah  
**Translation:** 

**[2505.60s] English:** yeah that was that that was like in the in the early 90s yeah and we thought this would be great  
**Translation:** 

**[2512.88s] English:** you could you know and the kind of content we were thinking about at the time was like  
**Translation:** 

**[2518.96s] English:** you know  
**Translation:** 

**[2526.56s] English:** you  
**Translation:** 

**[2520.00s] English:** movies kids essays um you know stuff from like grocery stores or you know you know that the  
**Translation:** Vocabulary: grocery: 杂货店

**[2530.04s] English:** or a or a restaurant that they could actually like start sending information about out and um  
**Translation:** 

**[2539.42s] English:** that's brilliant and and the the the the reaction of the cable companies was like fuck no  
**Translation:** 

**[2547.86s] English:** because because then we're out of business what is it about companies that because they could have  
**Translation:** 

**[2557.72s] English:** just they could have been ahead of that wave they could have listened to that and they could  
**Translation:** 

**[2562.28s] English:** they didn't see a path to revenue you know there's there's somewhere in there there's a lesson for  
**Translation:** 

**[2568.68s] English:** like big companies right like to to listen to to try to anticipate the the renegade the out there  
**Translation:** Vocabulary: anticipate: 预见; renegade: 异见者

**[2576.62s] English:** out of the box  
**Translation:** 

**[2577.86s] English:** people like yourself in the early days writing proposals about what this could possibly be  
**Translation:** 

**[2583.40s] English:** well and that you know that you know it wasn't you know if you're in a in a position where you're  
**Translation:** 

**[2589.02s] English:** making truckloads of money off of a particular business model um you know the the the the the  
**Translation:** Vocabulary: truckloads: 巨额

**[2601.74s] English:** the whole um thought of like you know leaping the chasm right you know  
**Translation:** 

**[2607.86s] English:** you can see oh new models that are more effective are emerging right so like digital cameras  
**Translation:** Vocabulary: chasm: 鸿沟

**[2618.54s] English:** versus film cameras um you know i mean why take the leap  
**Translation:** 

**[2625.38s] English:** why why take the leap because you're making so much money off of film and um you know in my past at sun one of  
**Translation:** 

**[2636.50s] English:** the big australian studios uh who was my uh the writer anda that still lives you know as an epcotJesus is working on it,sell me his dieser ,history of schism in her Kalasauder interview over 30 years an important point of registration  
**Translation:** 

**[2637.86s] English:** customers was Kodak.  
**Translation:** Vocabulary: kodak: 柯达; schism: 分裂

**[2640.00s] English:** up interacting with folks from Kodak quite a lot and they actually had a big um digital camera  
**Translation:** 

**[2648.64s] English:** research and you know digital imaging business or development group and they knew that that you  
**Translation:** 

**[2660.54s] English:** know you you know you just look at the at the trend lines and you look at um you know the  
**Translation:** 

**[2667.04s] English:** emerging quality of of of these you know digital cameras and you know you can just plot on the  
**Translation:** 

**[2676.78s] English:** graph you know and it's like you know sure film is better today but you know digital is is is is  
**Translation:** 

**[2689.14s] English:** improving like this the lines are going to cross and and you know the point at which the lines cross  
**Translation:** 

**[2697.04s] English:** is going to be a collapse in their business and they could see that right they absolutely knew  
**Translation:** 

**[2706.88s] English:** that the problem is that you know up to the point where they hit the wall they were making truck  
**Translation:** 

**[2713.96s] English:** loads of money yeah right and when they did the math um it never started to make sense for them to  
**Translation:** 

**[2727.04s] English:** kind of lead the charge and part of the issues for a lot of companies for this kind of stuff  
**Translation:** 

**[2734.84s] English:** is that um you know if you're going to leap over a chasm like that like like with Kodak going from  
**Translation:** 

**[2742.10s] English:** from film to digital that's a transition that's going to take a while right we had we had fights  
**Translation:** Vocabulary: chasm: 深渊

**[2751.10s] English:** like this with people over like smart cards the smart cards fights were just ludicrous  
**Translation:** 

**[2757.04s] English:** but that's where visionary leadership comes in right  
**Translation:** Vocabulary: visionary: 有远见的

**[2760.00s] English:** Somebody needs to roll in and say, then take the leap.  
**Translation:** 

**[2764.74s] English:** Well, it's partly take the leap, but it's also partly take the hit.  
**Translation:** 

**[2769.48s] English:** Take the hit.  
**Translation:** 

**[2770.32s] English:** Right.  
**Translation:** 

**[2770.50s] English:** So you can draw the graphs you want that show that if we leap from here, on our present trajectory, we're doing this and there's a cliff.  
**Translation:** 

**[2782.32s] English:** If we force ourselves into a transition and we proactively do that, we can be on the next wave.  
**Translation:** Vocabulary: proactively: 主动地; trajectory: 轨迹

**[2793.42s] English:** But there will be a period when we're in a trough.  
**Translation:** 

**[2799.04s] English:** And pretty much always there ends up being a trough as you leap the chasm.  
**Translation:** Vocabulary: trough: 低谷

**[2805.02s] English:** But the way that public companies work on this planet.  
**Translation:** 

**[2812.32s] English:** They're reporting every quarter.  
**Translation:** 

**[2815.92s] English:** And the one thing that a CEO must never do is take a big hit.  
**Translation:** 

**[2822.70s] English:** Take a big hit.  
**Translation:** 

**[2824.26s] English:** Over some quarter.  
**Translation:** 

**[2826.00s] English:** And many of these transitions involve a big hit for a period of time.  
**Translation:** Vocabulary: transitions: 转变时期

**[2835.04s] English:** You know, one, two, three quarters.  
**Translation:** 

**[2837.70s] English:** And so you get some companies.  
**Translation:** 

**[2842.32s] English:** And, you know, like Tesla and Amazon are really good examples of companies that take huge hits.  
**Translation:** 

**[2851.90s] English:** But they have the luxury of being able to ignore the stock market for a little while.  
**Translation:** 

**[2858.24s] English:** And that's not so true today, really.  
**Translation:** 

**[2862.18s] English:** But, you know, in the early days of both of those companies.  
**Translation:** 

**[2868.06s] English:** You know, like, like, like, like, like they both did this.  
**Translation:** 

**[2872.18s] English:** You know, I don't care about the quarterly reports.  
**Translation:** 

**[2877.78s] English:** I care about how many, how many happy customers.  
**Translation:** 

**[2880.00s] English:** as we have yeah right and having as many happy customers as possible can often be  
**Translation:** 

**[2887.60s] English:** um an enemy of the bottom line yeah so how do they make that work i mean amazon operated the  
**Translation:** 

**[2894.16s] English:** negative for a long time it's like investing into the future right but you know you know so  
**Translation:** 

**[2900.40s] English:** amazon and google and tesla and facebook a lot of those had what it what amounted to patient money  
**Translation:** 

**[2908.64s] English:** um often because the there's there's like a charismatic central figure who has a really  
**Translation:** Vocabulary: charismatic: 魅力十足的

**[2918.00s] English:** large block of stock and they can just make it so so what uh on that topic just maybe it's a  
**Translation:** 

**[2928.48s] English:** small tangent but uh you've gotten the chance to work with some pretty big leaders what are  
**Translation:** Vocabulary: tangent: 旁枝话题

**[2933.66s] English:** your thoughts about on tesla side elon musk leadership on the amazon side  
**Translation:** 

**[2938.64s] English:** jeff bezos all of these folks with large amounts of stock and vision in their company i mean their  
**Translation:** 

**[2945.34s] English:** founders yeah either either complete founders or like early on folks and uh they're they hit  
**Translation:** 

**[2953.26s] English:** amazon have taken leap a lot of leaps uh and believe you know uh that probably at the time  
**Translation:** Vocabulary: founders: 创立者

**[2960.06s] English:** people would criticize as like what is this bookstore thing why yeah and and you know  
**Translation:** 

**[2968.64s] English:** bezos had a vision and he had the ability to just follow it lots of people have visions and  
**Translation:** 

**[2978.74s] English:** you know the average vision is completely idiotic and you crash and burn  
**Translation:** 

**[2983.26s] English:** um you know the the silicon valley um crash and burn rate is pretty high um and they're not they  
**Translation:** 

**[2993.10s] English:** don't necessarily crash and burn because they were dumb ideas but you know often it's it's just timing  
**Translation:** 

**[2998.64s] English:** um  
**Translation:** 

**[3000.00s] English:** in luck and you know you take companies like like like tesla um and and and and and really  
**Translation:** 

**[3009.68s] English:** you know the the original tesla um you know sort of pre um elon was kind of doing sort of okay  
**Translation:** 

**[3021.20s] English:** but but but he just drove them and because he had a really strong vision you know he would he would  
**Translation:** 

**[3032.98s] English:** make calls that were always you know or well mostly pretty good i mean the model x was kind  
**Translation:** 

**[3042.42s] English:** of a goofball thing to do but he did it boldly anyway like there's so many people that just said  
**Translation:** 

**[3049.44s] English:** like there's so many people that  
**Translation:** Vocabulary: goofball: 笨蛋行为

**[3051.20s] English:** oppose them on the in the falconwind door like the door yeah from the engineering perspective  
**Translation:** 

**[3055.60s] English:** those doors are ridiculous it's like yeah they're they are a complete travesty but but they're  
**Translation:** Vocabulary: falconwind: 猎风门; travesty: 荒谬之作

**[3061.54s] English:** but they're exactly the symbol of what great leadership is which is like you have a vision  
**Translation:** 

**[3067.38s] English:** and you just go like if you're gonna do something stupid make it really stupid yeah and go all in  
**Translation:** 

**[3073.16s] English:** yeah yeah and and you know to to my credit he's a really sharp guy  
**Translation:** 

**[3081.20s] English:** right so going back in time a little bit to steve jobs yeah you know steve jobs was a similar sort  
**Translation:** 

**[3088.96s] English:** of character who had a strong vision and was really really smart and he you know and he wasn't  
**Translation:** 

**[3095.52s] English:** smart about the technology parts of things but but so he he was really sharp about the  
**Translation:** 

**[3102.80s] English:** the the sort of human relationship between you know the relationship between humans and  
**Translation:** 

**[3111.00s] English:** objects and and and and and and and and and and and and and and and and and and and and and  
**Translation:** 

**[3111.20s] English:** and and and and and and and and and but he was a jerk you know  
**Translation:** 

**[3120.00s] English:** right can we just linger on that a little bit like people say he's a jerk  
**Translation:** 

**[3124.04s] English:** um is that a feature or a bug well that's that's that's the question right so you take people like  
**Translation:** 

**[3132.56s] English:** steve um who was really hard on people and and the and so the question is was he really was he  
**Translation:** 

**[3143.30s] English:** needlessly hard on people or was he just making people reach to to meet his vision  
**Translation:** 

**[3153.28s] English:** and you could kind of spin it either way um well the results tell a story you know he's uh  
**Translation:** Vocabulary: needlessly: 多余地

**[3164.82s] English:** he through whatever jerk ways he had he made people often do the best work of their life  
**Translation:** 

**[3171.48s] English:** yeah yeah and that was  
**Translation:** 

**[3173.04s] English:** absolutely  
**Translation:** 

**[3173.30s] English:** true and you know i interviewed with him several times um i did you know various negotiations with  
**Translation:** 

**[3183.36s] English:** him and um even though kind of personally i liked him i could never work for him  
**Translation:** 

**[3198.24s] English:** what why do you think uh that what can you put into  
**Translation:** 

**[3203.04s] English:** into words the kind of tension that you feel would be um destructive as opposed to constructive  
**Translation:** 

**[3210.20s] English:** oh he he'd yell at people he'd call them names um and you don't like that no  
**Translation:** 

**[3220.40s] English:** no i don't i don't think you need to do that yeah um and  
**Translation:** 

**[3227.30s] English:** and you know he you know i think you know i think i think i think i think i think i think i think i  
**Translation:** 

**[3233.04s] English:** agree with地  
**Translation:** 

**[3258.10s] English:** you  
**Translation:** 

**[3258.50s] English:** you  
**Translation:** 

**[3259.60s] English:** you  
**Translation:** 

**[3261.02s] English:** you  
**Translation:** 

**[3261.10s] English:** you  
**Translation:** 

**[3261.28s] English:** you  
**Translation:** 

**[3262.86s] English:** you  
**Translation:** 

**[3262.88s] English:** you  
**Translation:** 

**[3262.90s] English:** you  
**Translation:** 

**[3262.94s] English:** you  
**Translation:** 

**[3262.98s] English:** you  
**Translation:** 

**[3263.00s] English:** you  
**Translation:** 

**[3240.56s] English:** there's too far and i think he was on the wrong side of the line  
**Translation:** 

**[3244.64s] English:** and i've never worked for musk i know a number of people who have  
**Translation:** 

**[3250.16s] English:** many of them that have said and it's you know shows up in the press a lot that  
**Translation:** 

**[3255.20s] English:** that musk is kind of that way and one of the things that i sort of loathe about silicon  
**Translation:** 

**[3262.40s] English:** valley these days is that um a lot of the high-flying successes are run by people who  
**Translation:** Vocabulary: loathe: 厌恶

**[3270.32s] English:** are complete jerks um and but it seems like there's been become this there's come this this  
**Translation:** 

**[3278.00s] English:** sort of mythology out of steve jobs that the reason that he succeeded was because he was  
**Translation:** Vocabulary: jerks: 无赖; mythology: 神话

**[3287.44s] English:** super hard on people and and and and and  
**Translation:** 

**[3292.40s] English:** and and in a number of corners people start going oh if i want to succeed i need to be a real jerk  
**Translation:** 

**[3300.88s] English:** yeah right and and and that for me just does not compute  
**Translation:** 

**[3305.44s] English:** i mean i know a lot of successful people who are not jerks who are perfectly fine people  
**Translation:** 

**[3313.12s] English:** um you know they they tend to not be in the public eye  
**Translation:** 

**[3320.80s] English:** the the the  
**Translation:** 

**[3322.40s] English:** general public somehow lifts the jerks up into the into the hero status right well they because  
**Translation:** 

**[3329.60s] English:** they're they do things that get them in the press yeah and you know the people who um  
**Translation:** 

**[3339.60s] English:** you know don't  
**Translation:** 

**[3343.04s] English:** do the kind of things that spill into the press um yeah just uh talk to chris ladner  
**Translation:** Vocabulary: ladner: 拉德纳

**[3350.80s] English:** um  
**Translation:** 

**[3353.12s] English:** for the second time he's a super nice guy  
**Translation:** 

**[3356.64s] English:** just an example of this kind of kind of individual that's in the background  
**Translation:** 

**[3371.84s] English:** you  
**Translation:** 

**[3360.00s] English:** I feel like he's behind like a million technologies, but he also talked about the jerkiness of some of the folks.  
**Translation:** 

**[3366.98s] English:** Yeah.  
**Translation:** Vocabulary: jerkiness: 卡顿感

**[3367.48s] English:** Yeah.  
**Translation:** 

**[3367.96s] English:** And the fact that being a jerk has become your required style.  
**Translation:** 

**[3372.98s] English:** But one thing I maybe want to ask on that is maybe to push back a little bit.  
**Translation:** 

**[3377.82s] English:** So there's the jerk side, but there's also, if I were to criticize what I've seen in Silicon Valley, which is almost the resistance to working hard.  
**Translation:** 

**[3386.80s] English:** So on the jerkiness side, so Postee Jobs and Elon kind of push people to work really hard to do.  
**Translation:** 

**[3401.94s] English:** And it's a question whether it's possible to do that nicely.  
**Translation:** 

**[3405.76s] English:** But one of the things that bothers me, maybe I'm just a Russian and just kind of romanticize the whole suffering thing.  
**Translation:** 

**[3412.84s] English:** But I think working hard is essential.  
**Translation:** 

**[3415.84s] English:** It's essential for accomplishing anything interesting, like really hard.  
**Translation:** 

**[3420.30s] English:** And in the parlance of Silicon Valley, it's probably too hard.  
**Translation:** Vocabulary: accomplishing: 完成; parlance: 行话

**[3424.82s] English:** This idea of that you should work smart, not hard, often to me sounds like you should be lazy.  
**Translation:** 

**[3432.68s] English:** Because, of course, you want to be able to work smart.  
**Translation:** 

**[3435.30s] English:** Of course, you want to be maximally efficient.  
**Translation:** 

**[3438.16s] English:** But in order to discover the efficient path, like we're talking about with the short programs.  
**Translation:** Vocabulary: maximally: 最大程度上

**[3441.76s] English:** Yeah.  
**Translation:** 

**[3443.12s] English:** Well, you know, the smart.  
**Translation:** 

**[3445.84s] English:** Smart, hard thing isn't an either or.  
**Translation:** 

**[3448.76s] English:** It's an and.  
**Translation:** 

**[3449.60s] English:** It's an and, yeah.  
**Translation:** 

**[3450.70s] English:** Right.  
**Translation:** 

**[3451.84s] English:** And, you know, the people who say you should work smart, not hard, they pretty much always fail.  
**Translation:** 

**[3464.38s] English:** Yeah.  
**Translation:** 

**[3465.02s] English:** Thank you.  
**Translation:** 

**[3466.02s] English:** Right.  
**Translation:** 

**[3466.68s] English:** I mean, that's just a recipe for disaster.  
**Translation:** 

**[3469.62s] English:** I mean, there are there are counterexamples, but they're more people.  
**Translation:** Vocabulary: counterexamples: 反例

**[3475.84s] English:** Who benefited from the luck.  
**Translation:** 

**[3478.56s] English:** And you're saying, yeah, exactly.  
**Translation:** Vocabulary: benefited: 受益

**[3480.00s] English:** Luck and timing, like you said, is often an essential thing.  
**Translation:** 

**[3484.70s] English:** But you're saying you can push people to work hard and do incredible work without being nasty.  
**Translation:** 

**[3493.64s] English:** Yeah, without being nasty.  
**Translation:** 

**[3494.58s] English:** I think Google is a good example of the leadership of Google throughout its history has been a pretty good example of not being nasty and being kind.  
**Translation:** 

**[3508.54s] English:** I mean, the twins, Larry and Sergey, are both pretty nice people.  
**Translation:** 

**[3517.62s] English:** Sander Pichaz, very nice.  
**Translation:** 

**[3519.68s] English:** Yeah.  
**Translation:** 

**[3519.94s] English:** Yeah, and, you know, it's a culture of people who work really, really hard.  
**Translation:** 

**[3529.26s] English:** Let me ask maybe a little bit of a tense question.  
**Translation:** 

**[3533.98s] English:** We're talking about Emacs.  
**Translation:** Vocabulary: emacs: emacs编辑器

**[3536.12s] English:** It seems like you've done some incredible.  
**Translation:** 

**[3538.54s] English:** So outside of Java, you've done some incredible work that didn't become as popular as it could have because of, like, licensing issues and open source and, like, type of issues.  
**Translation:** 

**[3551.52s] English:** What are your thoughts about that entire mess?  
**Translation:** 

**[3558.78s] English:** Like, what's about open source now in retrospect, looking back, about licensing, about open sourcing?  
**Translation:** Vocabulary: retrospect: 回顾; sourcing: 采购

**[3566.58s] English:** Do you think?  
**Translation:** 

**[3568.54s] English:** Do you think open source is a good thing, a bad thing?  
**Translation:** 

**[3573.36s] English:** Do you have regrets?  
**Translation:** 

**[3575.54s] English:** Do you have wisdom that you've learned from that whole experience?  
**Translation:** 

**[3579.92s] English:** So in general, I'm a big fan of open source.  
**Translation:** 

**[3585.18s] English:** The way that it can be used to build communities and promote the development of things and promote collaboration and all of that is really pretty grand.  
**Translation:** 

**[3597.52s] English:** Yeah.  
**Translation:** 

**[3598.54s] English:** So yeah.  
**Translation:** 

**[3598.94s] English:** Yeah, I want to be part of thosesofss together.  
**Translation:** 

**[3599.52s] English:** I'm a big fan.  
**Translation:** 

**[3600.28s] English:** Yep.  
**Translation:** 

**[3600.76s] English:** So.  
**Translation:** 

**[3601.26s] English:** I'm also proud of my colleague who, like, is the new trustee in the donut group.  
**Translation:** 

**[3604.62s] English:** He Ocean.  
**Translation:** Vocabulary: colleague: 同事; donut: 甜甜圈

**[3606.00s] English:** Yeah.  
**Translation:** 

**[3606.52s] English:** And if I don't join the chat actually tomorrow we want to actually have a conversation about those so I'll end it there.  
**Translation:** 

**[3609.08s] English:** Okay.  
**Translation:** 

**[3609.24s] English:** Hopefully we can talk about that.  
**Translation:** 

**[3610.38s] English:** Thank you so much, Dan.  
**Translation:** 

**[3612.44s] English:** Wonderful.  
**Translation:** 

**[3613.68s] English:** So amazing.  
**Translation:** 

**[3616.58s] English:** Thank you so much, Dan.  
**Translation:** 

**[3618.34s] English:** Yeah.  
**Translation:** 

**[3618.68s] English:** Thank you.  
**Translation:** 

**[3619.30s] English:** posible que os consultationas y vos, or con la visitele, el 410.  
**Translation:** 

**[3619.76s] English:** You're welcome a favor.  
**Translation:** Vocabulary: consultationas: 咨询; visitele: 访问

**[3620.60s] English:** Same to you.  
**Translation:** 

**[3621.06s] English:** You are my friend and I would never forget it if I were to know where you live.  
**Translation:** 

**[3622.98s] English:** Yeah, exactly.  
**Translation:** 

**[3600.00s] English:** And open source turns into a religion that says all things must be open source.  
**Translation:** 

**[3607.74s] English:** I get kind of weird about that because it's sort of like saying, you know, some versions of that end up saying that all software engineers must take a vow of poverty.  
**Translation:** 

**[3624.04s] English:** Right.  
**Translation:** 

**[3625.28s] English:** Right.  
**Translation:** 

**[3625.76s] English:** As though it's unethical to have money.  
**Translation:** Vocabulary: unethical: 不合伦理

**[3630.00s] English:** Yeah.  
**Translation:** 

**[3631.12s] English:** To build a company.  
**Translation:** 

**[3633.24s] English:** Right.  
**Translation:** 

**[3634.46s] English:** And, you know, there's a slice of me that actually kind of buys into that.  
**Translation:** 

**[3640.56s] English:** Right.  
**Translation:** 

**[3641.42s] English:** Because, you know, people who make billions of dollars off of like a patent and the patent came from like, you know, literally a stroke of lightning that hits you as you lie.  
**Translation:** Vocabulary: patent: 专利

**[3659.26s] English:** Half awake in bed.  
**Translation:** 

**[3662.28s] English:** Yeah, that's lucky.  
**Translation:** 

**[3663.78s] English:** Good for you.  
**Translation:** 

**[3665.78s] English:** The way that that sometimes sort of explodes into something that looks to me a lot like exploitation.  
**Translation:** Vocabulary: explodes: 爆发; exploitation: 剥削

**[3673.80s] English:** You know, you see a lot of that in in in like the the drug industry.  
**Translation:** 

**[3681.68s] English:** You know, when.  
**Translation:** 

**[3683.82s] English:** You know, when you've got a got got medications that cost.  
**Translation:** 

**[3688.54s] English:** You know, cost.  
**Translation:** Vocabulary: medications: 药品

**[3689.30s] English:** You like one hundred dollars a day.  
**Translation:** 

**[3691.92s] English:** And it's like.  
**Translation:** 

**[3694.22s] English:** No.  
**Translation:** 

**[3696.80s] English:** Yeah.  
**Translation:** 

**[3697.00s] English:** So the the interesting thing about sort of open source, what bothers me is when something is not open source and because of that, it's a worse product.  
**Translation:** 

**[3711.22s] English:** Yeah.  
**Translation:** 

**[3711.76s] English:** So, like, I mean, if I look at your just implementation of Emax, like that could have been the dominant implementation.  
**Translation:** 

**[3719.02s] English:** Like.  
**Translation:** Vocabulary: implementation: 实现方式

**[3719.20s] English:** Yeah.  
**Translation:** 

**[3719.24s] English:** I use Emax.  
**Translation:** 

**[3720.00s] English:** That's my main ID.  
**Translation:** 

**[3721.26s] English:** I apologize to the world, but I still love it.  
**Translation:** 

**[3725.00s] English:** And, you know, I could have been using your implementation of Emacs.  
**Translation:** 

**[3731.42s] English:** And why aren't I?  
**Translation:** Vocabulary: emacs: 编辑器

**[3733.58s] English:** So are you using the GNU Emacs?  
**Translation:** 

**[3736.24s] English:** I guess the default on Linux is that GNU.  
**Translation:** 

**[3738.46s] English:** Yeah, and that, through a strange passage, started out as the one that I wrote.  
**Translation:** 

**[3744.48s] English:** Exactly.  
**Translation:** 

**[3745.12s] English:** So it still has...  
**Translation:** 

**[3747.46s] English:** Right.  
**Translation:** 

**[3747.70s] English:** Yeah.  
**Translation:** 

**[3747.80s] English:** Well, and part of that was because, you know, in, you know, the last couple of years of grad school, it became really clear to me that I was either going to be Mr. Emacs forever, or I was going to graduate.  
**Translation:** 

**[3771.14s] English:** Got it.  
**Translation:** 

**[3772.14s] English:** I couldn't actually do both.  
**Translation:** 

**[3775.92s] English:** Was that a hard decision?  
**Translation:** 

**[3777.80s] English:** That's so interesting to think about you as a...  
**Translation:** 

**[3780.30s] English:** Like, it's a different trajectory that could have happened.  
**Translation:** 

**[3782.80s] English:** Yeah.  
**Translation:** Vocabulary: trajectory: 轨迹

**[3783.50s] English:** That's fascinating.  
**Translation:** 

**[3785.70s] English:** You know, and maybe, you know, I could be fabulously wealthy today if I had become Mr. Emacs, and Emacs had mushroomed into a series of text processing applications and all kinds of stuff.  
**Translation:** Vocabulary: fabulously: 极其富有

**[3800.22s] English:** And, you know, I would have, you know...  
**Translation:** 

**[3804.28s] English:** But I have a long history.  
**Translation:** 

**[3807.80s] English:** I have a long history of financially suboptimal decisions, because I didn't want that life, right?  
**Translation:** 

**[3818.40s] English:** And, you know, I went to grad school because I wanted to graduate.  
**Translation:** Vocabulary: financially: 经济上; suboptimal: 次优的

**[3827.18s] English:** And, you know, being Mr. Emacs for a while was kind of fun.  
**Translation:** 

**[3837.80s] English:** And then it kind of became...  
**Translation:** 

**[3840.00s] English:** not fun not fun um and you know when it was not fun and i was you know there was no way i could  
**Translation:** 

**[3851.30s] English:** you know pay my rent right yeah and and i was like okay do i carry on as a grad student as a  
**Translation:** 

**[3861.90s] English:** you know i you know i had a research assistantship and i was sort of living off of that and i was  
**Translation:** 

**[3868.16s] English:** trying to do my you know i was doing all my ra where all my ra you know being grad student work  
**Translation:** Vocabulary: assistantship: 助教职位

**[3875.06s] English:** and being mr emacs all at the same time um and and i i decided to pick one  
**Translation:** 

**[3883.78s] English:** and one of the things that i did at the time was i went around you know all the people i knew on the  
**Translation:** Vocabulary: emacs: 编辑器

**[3892.70s] English:** the arpanet who might be able to to to take over looking after  
**Translation:** 

**[3898.16s] English:** emacs and um pretty much everybody said yeah i got a day job so so i actually found you know  
**Translation:** Vocabulary: arpanet: 阿帕网

**[3910.40s] English:** two folks and a couple of folks in a garage in new jersey um complete with a dog  
**Translation:** 

**[3918.80s] English:** um who were willing to take it over but they were going to have to charge money um but my  
**Translation:** 

**[3926.80s] English:** deal with them was that they would  
**Translation:** 

**[3928.16s] English:** um only that they would make it free for universities and schools and stuff  
**Translation:** 

**[3934.96s] English:** and they said sure and you know that upset some people so you have some now i don't know  
**Translation:** 

**[3942.56s] English:** the full history of this but i think it's kind of uh interesting you have some tension with  
**Translation:** 

**[3949.92s] English:** mr richard stallman um over the and he kind of represents this kind of like like you mentioned  
**Translation:** 

**[3957.84s] English:** free  
**Translation:** Vocabulary: stallman: 斯托曼

**[3958.00s] English:** and he kind of represents this kind of like like free software  
**Translation:** 

**[3960.00s] English:** uh sort of a dogmatic focus on yeah all all all information must be free must be free so what  
**Translation:** Vocabulary: dogmatic: 教条主义的

**[3971.38s] English:** is there an interesting way to uh paint a picture of the disagreement you have with  
**Translation:** 

**[3978.42s] English:** richard through the years my my basic opposition is that you know when you say information must be  
**Translation:** 

**[3987.38s] English:** free uh to a really extreme form that turns into you know all people whose job is the production of  
**Translation:** 

**[4001.16s] English:** everything from movies to software um they must all take a vow of poverty  
**Translation:** 

**[4014.26s] English:** because information must be free and that's  
**Translation:** 

**[4017.38s] English:** that doesn't work for me right and and i and i don't i don't want to be wildly rich i am  
**Translation:** 

**[4025.62s] English:** not wildly rich um i do okay um  
**Translation:** 

**[4031.82s] English:** but i do actually you know you know i've you know i can feed my children yeah i totally  
**Translation:** 

**[4041.36s] English:** agree with you i it does just make me sad that sometimes the closing of the source  
**Translation:** 

**[4047.38s] English:** for some reason the people that like a bureaucracy begins to build and sometimes it doesn't it hurts  
**Translation:** Vocabulary: bureaucracy: 官僚体系

**[4056.72s] English:** the product oh absolutely absolutely it's always sad and there's and there is a there is a balance  
**Translation:** 

**[4064.02s] English:** in there there's a balance um and you know it's it's not hard hard over you know rapacious  
**Translation:** 

**[4077.38s] English:** and it's and it's not hard over in the other  
**Translation:** 

**[4080.00s] English:** direction um and you know a lot of the the open source movement they they have been managing to  
**Translation:** 

**[4090.20s] English:** find a path to um actually making money right so doing things like service and support works for  
**Translation:** 

**[4099.70s] English:** a lot of people um you know and there are some some ways where it's it's kind of um  
**Translation:** 

**[4109.80s] English:** some of them are are a little a little perverse right so as  
**Translation:** 

**[4117.82s] English:** you know a part of things like this sarbanes-oxley act and various people's  
**Translation:** Vocabulary: perverse: 扭曲的

**[4124.84s] English:** interpretations of all kinds of accounting principles um and this is kind of a worldwide  
**Translation:** 

**[4131.28s] English:** thing but if you've got a a corporation that is depending on some piece of software um  
**Translation:** Vocabulary: interpretations: 解释

**[4138.92s] English:** um  
**Translation:** 

**[4138.98s] English:** um  
**Translation:** 

**[4139.02s] English:** um  
**Translation:** 

**[4139.04s] English:** um  
**Translation:** 

**[4139.06s] English:** um  
**Translation:** 

**[4139.08s] English:** um  
**Translation:** 

**[4139.10s] English:** um  
**Translation:** 

**[4139.12s] English:** um  
**Translation:** 

**[4139.14s] English:** um  
**Translation:** 

**[4139.16s] English:** um  
**Translation:** 

**[4139.18s] English:** um  
**Translation:** 

**[4139.20s] English:** um  
**Translation:** 

**[4139.22s] English:** um  
**Translation:** 

**[4139.24s] English:** um  
**Translation:** 

**[4139.26s] English:** um  
**Translation:** 

**[4139.28s] English:** um  
**Translation:** 

**[4139.30s] English:** um  
**Translation:** 

**[4139.32s] English:** um  
**Translation:** 

**[4139.34s] English:** um  
**Translation:** 

**[4139.38s] English:** um  
**Translation:** 

**[4139.40s] English:** um  
**Translation:** 

**[4139.80s] English:** um  
**Translation:** 

**[4140.64s] English:** um  
**Translation:** 

**[4141.02s] English:** um  
**Translation:** 

**[4148.02s] English:** um  
**Translation:** 

**[4150.06s] English:** um  
**Translation:** 

**[4150.08s] English:** um  
**Translation:** 

**[4150.10s] English:** um  
**Translation:** 

**[4150.14s] English:** um  
**Translation:** 

**[4150.30s] English:** um  
**Translation:** 

**[4150.32s] English:** um  
**Translation:** 

**[4150.38s] English:** um  
**Translation:** 

**[4150.40s] English:** on  
**Translation:** 

**[4150.94s] English:** on  
**Translation:** 

**[4151.04s] English:** then  
**Translation:** 

**[4152.22s] English:** that's bad  
**Translation:** 

**[4154.28s] English:** you know so so so you know if you've got a if you've got a database you need to pay for support  
**Translation:** 

**[4161.62s] English:** and and so but there's a difference between you know the the sort of support contract  
**Translation:** 

**[4169.34s] English:** contracts that you know the average open source database uh producer charges and what somebody  
**Translation:** 

**[4179.46s] English:** who is truly rapacious like oracle charges yes it's a it's a balance like you said it is it is  
**Translation:** 

**[4187.62s] English:** absolutely a balance and you know there are there are a lot of a lot of different ways  
**Translation:** 

**[4196.08s] English:** to make you know the math  
**Translation:** 

**[4200.00s] English:** work out for everybody um and you know the the very you know  
**Translation:** 

**[4209.86s] English:** unbalanced sort of you know like like the winner takes all thing that that happens in so much of  
**Translation:** Vocabulary: unbalanced: 不平衡

**[4220.04s] English:** of modern commerce um that just doesn't work for me either i know you've talked about this  
**Translation:** 

**[4228.92s] English:** in quite a few places but you have created one of the most popular programming languages in the  
**Translation:** 

**[4237.82s] English:** world uh this is the programming language that i first learned about object-oriented programming  
**Translation:** 

**[4244.50s] English:** with uh you know i think it's a programming language that a lot of people use in a lot of  
**Translation:** 

**[4251.34s] English:** different places and millions of devices today java so the absurd  
**Translation:** 

**[4258.92s] English:** question but can you tell the origin story of java so a long time ago at sun in about 1990 there  
**Translation:** 

**[4267.50s] English:** was a group of us who were kind of worried that there was stuff going on in the universe of  
**Translation:** 

**[4278.06s] English:** computing that the computing industry was missing out on um and so a a few of us started  
**Translation:** 

**[4288.92s] English:** this project at sun that really got going i mean we started talking about it in 1990 and it really  
**Translation:** 

**[4295.26s] English:** got going in 91 um and it was all about you know what was happening in terms of you know computing  
**Translation:** Vocabulary: computing: 计算机技术

**[4307.04s] English:** hardware you know processors and networking and all of that that was outside of the computer  
**Translation:** 

**[4313.80s] English:** industry and that was everything from the the the  
**Translation:** Vocabulary: processors: 处理器

**[4318.92s] English:** sort of early glimmers  
**Translation:** 

**[4320.00s] English:** of cell phones that were happening then to, you know,  
**Translation:** Vocabulary: glimmers: 微光

**[4324.92s] English:** you look at elevators and locomotives and process control systems  
**Translation:** 

**[4331.14s] English:** in factories and all kinds of audio equipment and video equipment.  
**Translation:** Vocabulary: locomotives: 火车

**[4340.28s] English:** They all had processors in them and they were all doing stuff with them.  
**Translation:** 

**[4343.70s] English:** And it sort of felt like there was something going on there  
**Translation:** 

**[4350.74s] English:** that we needed to understand.  
**Translation:** 

**[4355.64s] English:** So C and C++ was in the air already.  
**Translation:** 

**[4359.00s] English:** Oh, no, C and C++ absolutely owned the universe at that time.  
**Translation:** 

**[4363.06s] English:** Everything was written in C and C++.  
**Translation:** 

**[4365.16s] English:** So where was the hunch that there was a need for a revolution?  
**Translation:** 

**[4368.40s] English:** Well, so the need for a revolution was not about a language.  
**Translation:** Vocabulary: hunch: 直觉

**[4373.70s] English:** It was about, it was just as simple and vague as  
**Translation:** 

**[4378.84s] English:** there are things happening out there.  
**Translation:** 

**[4383.84s] English:** We need to understand them.  
**Translation:** 

**[4384.94s] English:** We need to understand them.  
**Translation:** 

**[4387.50s] English:** And so a few of us went on several somewhat epic road trips.  
**Translation:** 

**[4399.44s] English:** Literal road trips?  
**Translation:** 

**[4400.68s] English:** Literal road trips.  
**Translation:** 

**[4401.78s] English:** It's like get on an airplane.  
**Translation:** 

**[4403.16s] English:** Go to Japan.  
**Translation:** 

**[4404.86s] English:** Visit, you know, Toshiba and Sharp and Mitsubishi and Sony  
**Translation:** Vocabulary: mitsubishi: 三菱; toshiba: 东芝

**[4411.62s] English:** and all of these folks.  
**Translation:** 

**[4413.94s] English:** And, you know, because we worked for Sun,  
**Translation:** 

**[4416.48s] English:** we had, you know, folks who were willing to, like, give us introductions.  
**Translation:** 

**[4422.10s] English:** You know, we visited, you know, Samsung and, you know,  
**Translation:** Vocabulary: introductions: 引荐

**[4428.62s] English:** a bunch of Korean companies and we went all over Europe.  
**Translation:** 

**[4431.24s] English:** We went to, you know.  
**Translation:** Vocabulary: korean: 韩国的

**[4433.16s] English:** Places like Philips and Siemens and Thompson and.  
**Translation:** 

**[4438.02s] English:** What did you see there?  
**Translation:** 

**[4439.76s] English:** You know.  
**Translation:** 

**[4440.00s] English:** for me the one of the things that sort of leapt out was that they were doing all the usual computer  
**Translation:** 

**[4446.32s] English:** computer things that people had been doing like 20 years before the thing that really leapt out  
**Translation:** 

**[4452.46s] English:** to me was that they were sort of reinventing computer networking and they were making all  
**Translation:** 

**[4462.20s] English:** the mistakes that people in the computer industry had had made and since i'd been doing a lot of work  
**Translation:** 

**[4470.86s] English:** in in the networking area you know you know we'd go and you know visit you know company x they  
**Translation:** 

**[4477.32s] English:** described this networking thing that they were doing and just without any thought i could i could  
**Translation:** 

**[4482.88s] English:** tell them like the 25 things that were going to be complete disasters with that thing that they  
**Translation:** 

**[4489.32s] English:** were doing um  
**Translation:** 

**[4491.32s] English:** um  
**Translation:** 

**[4491.36s] English:** um  
**Translation:** 

**[4491.38s] English:** um  
**Translation:** 

**[4491.40s] English:** um  
**Translation:** 

**[4491.42s] English:** um  
**Translation:** 

**[4491.44s] English:** um  
**Translation:** 

**[4491.46s] English:** um  
**Translation:** 

**[4491.48s] English:** um  
**Translation:** 

**[4491.50s] English:** um  
**Translation:** 

**[4491.52s] English:** um  
**Translation:** 

**[4491.54s] English:** um  
**Translation:** 

**[4491.56s] English:** um  
**Translation:** 

**[4491.58s] English:** um  
**Translation:** 

**[4491.60s] English:** um  
**Translation:** 

**[4491.62s] English:** um  
**Translation:** 

**[4491.64s] English:** um  
**Translation:** 

**[4491.66s] English:** um  
**Translation:** 

**[4491.68s] English:** um  
**Translation:** 

**[4491.70s] English:** um  
**Translation:** 

**[4491.74s] English:** um  
**Translation:** 

**[4491.80s] English:** um  
**Translation:** 

**[4492.20s] English:** um  
**Translation:** 

**[4492.86s] English:** and i don't know whether that had any impact on any of them but but but that particular story of  
**Translation:** 

**[4498.34s] English:** you know sort of repeating the disasters of the computer science industry um was there and we  
**Translation:** 

**[4507.76s] English:** and one of the things we thought was well maybe we could do something useful here with like  
**Translation:** 

**[4513.76s] English:** bringing them forward somewhat but but also at the same time  
**Translation:** 

**[4521.62s] English:** um  
**Translation:** 

**[4522.06s] English:** a bunch of things from from these you know mostly consumer electronics companies um and  
**Translation:** 

**[4534.30s] English:** you know high on the list was that  
**Translation:** 

**[4539.42s] English:** they viewed their like relationship with the customer as sacred um they they were never ever  
**Translation:** 

**[4548.22s] English:** willing to make trade-offs between for for safety right so one of the things that had  
**Translation:** 

**[4560.00s] English:** always made me nervous in the computer industry was that um people were willing to make trade-offs  
**Translation:** 

**[4570.32s] English:** in reliability to get performance um you know the the you know they want faster fast it breaks a  
**Translation:** 

**[4579.30s] English:** little more often because it's fast you know you maybe you run it a little hotter than you should  
**Translation:** 

**[4583.78s] English:** or like like the one that always blew my mind was the way that um the folks at at at cray  
**Translation:** 

**[4592.34s] English:** supercomputers got their division to be really fast was that they did newton rafson approximations  
**Translation:** 

**[4602.72s] English:** and so you know the bottom several bits of you know a over b were essentially random numbers  
**Translation:** Vocabulary: approximations: 近似计算; supercomputers: 超级计算机

**[4613.78s] English:** um what could possibly go wrong what could go wrong right and you know  
**Translation:** 

**[4621.94s] English:** just figuring out how to nail the bottom bit um how to make sure that you know if you put a piece  
**Translation:** 

**[4632.40s] English:** of toast in a toaster it's not going to kill the customer it's not going to burst into flames and  
**Translation:** 

**[4640.48s] English:** burn the house down so those are  
**Translation:** 

**[4643.28s] English:** you  
**Translation:** 

**[4643.76s] English:** guess those are the the principles that were inspiring but how did uh from the days of  
**Translation:** 

**[4649.72s] English:** uh java is called oak because of a tree outside the window story that a lot of people know  
**Translation:** 

**[4656.16s] English:** how did it become this incredible like powerful language well so it was a bunch of things so we  
**Translation:** 

**[4667.24s] English:** you know after all that we started you know the way that we decided that we could understand  
**Translation:** 

**[4672.74s] English:** things better  
**Translation:** 

**[4673.76s] English:** was by building a demo building a prototype of something got it so  
**Translation:** 

**[4680.00s] English:** um kind of because it was easy and fun we decided to build a control system for some  
**Translation:** 

**[4686.88s] English:** home electronics you know tv vcr that kind of stuff and as we were building it we you know we  
**Translation:** 

**[4694.96s] English:** we sort of discovered that there were some things about standard practice in c programming that um  
**Translation:** 

**[4702.72s] English:** were really getting in the way and and it wasn't it wasn't exactly you know because we were  
**Translation:** 

**[4710.56s] English:** writing this all this c code and c plus plus code that that we couldn't write it to do the  
**Translation:** 

**[4717.12s] English:** right thing but that um one of the things that was weird in the group was that we had  
**Translation:** 

**[4724.16s] English:** um a guy who's who's who's you know his sort of top level job was he was a business guy  
**Translation:** 

**[4732.72s] English:** know he was sort of an mba kind of person you know think about business plans and all of that  
**Translation:** 

**[4738.72s] English:** and you know there were a bunch of things that were kind of you know and we would talk about  
**Translation:** 

**[4746.16s] English:** things that were going wrong and um or things were going wrong things were going right and  
**Translation:** 

**[4752.40s] English:** you know as we thought about you know things like like the requirements for security and safety um  
**Translation:** 

**[4760.08s] English:** some low-level details in c like  
**Translation:** 

**[4762.72s] English:** naked pointers yeah and you know so so back in the early 90s um it was well understood  
**Translation:** 

**[4775.28s] English:** that you know the number one source of like security vulnerabilities is pointers was just  
**Translation:** 

**[4782.72s] English:** pointers was just bugs yeah right and it was like you know 50 60 70 percent of all security  
**Translation:** Vocabulary: vulnerabilities: 安全漏洞

**[4791.44s] English:** vulnerabilities were  
**Translation:** 

**[4792.72s] English:** bugs and the vast majority of them were like buffer overflows so you're like we have to fix this  
**Translation:** Vocabulary: buffer: 缓冲区; overflows: 溢出

**[4800.00s] English:** we have to make sure that this cannot happen and that was kind of the original thing for me was  
**Translation:** 

**[4807.62s] English:** this cannot this cannot continue and one of the things i find really entertaining this year was  
**Translation:** Vocabulary: cannot: 不能

**[4817.10s] English:** i forget which rag published it but there was this article that came out that was  
**Translation:** 

**[4825.58s] English:** um an examination it was sort of the result of of an examination of all the security  
**Translation:** 

**[4832.12s] English:** vulnerabilities in chrome and chrome is like a giant piece of c++ code and 60 or 70 percent  
**Translation:** 

**[4840.98s] English:** of all the security vulnerabilities were stupid pointer tricks and i thought it's 30 years later  
**Translation:** 

**[4851.44s] English:** and we're still there still there and we're still there  
**Translation:** 

**[4855.58s] English:** and you know i you know that's one of those you know slap your forehead and and and just just just  
**Translation:** 

**[4863.70s] English:** want to cry so would you attribute uh or is that too much of a simplification but would you  
**Translation:** 

**[4869.68s] English:** attribute the creation of java to uh to c pointers um obvious problem well i mean that was that was  
**Translation:** Vocabulary: attribute: 归因; simplification: 简化

**[4878.24s] English:** one of the the trigger points and currency you've mentioned concurrency was a big deal  
**Translation:** 

**[4885.58s] English:** um you know because when your interacting with people you know the last thing you ever want to  
**Translation:** Vocabulary: concurrency: 并行性

**[4892.34s] English:** see is is the thing like waiting and you know issues about the software development process  
**Translation:** 

**[4900.58s] English:** you know when faults happen can you recover from them  
**Translation:** 

**[4905.46s] English:** what can you do to make it easier to create and eliminate complex data structures  
**Translation:** 

**[4913.30s] English:** what can you do to  
**Translation:** 

**[4915.58s] English:** to fix one of the most common C problems we  
**Translation:** 

**[4920.00s] English:** is storage leaks um and it's it's evil twin the um the the freed but still being used piece of  
**Translation:** 

**[4933.12s] English:** piece of memory you know you free something and then you keep using it oh yeah you know so so  
**Translation:** 

**[4939.84s] English:** when i was originally thinking about that i was thinking about that in terms of of sort of safety  
**Translation:** 

**[4945.36s] English:** and security issues and one of the things i sort of came to believe came to understand was that it  
**Translation:** 

**[4951.44s] English:** wasn't just about safety and security but it was about um developer velocity right so and i got  
**Translation:** 

**[4961.44s] English:** really religious about this because at that point i had spent an ungodly amount of my life  
**Translation:** 

**[4969.60s] English:** hunting down mystery pointer bugs yeah and  
**Translation:** 

**[4975.36s] English:** you know like like two-thirds of my time as a software developer was you know because the  
**Translation:** 

**[4982.40s] English:** mystery pointer bugs tend to be the hardest to find because they tend to be very very statistical  
**Translation:** 

**[4991.76s] English:** the ones that hurt you know they're you know they're like a one in a million chance  
**Translation:** 

**[4997.36s] English:** um and but nevertheless create an infinite amount of suffering right because when you're  
**Translation:** 

**[5005.36s] English:** a billion operations a second yeah you know i'm one in a million chance means it's gonna happen  
**Translation:** 

**[5013.60s] English:** um and and so i got really religious about this thing about you know making it so that if  
**Translation:** 

**[5020.08s] English:** something fails it fails immediately and visibly and you know one of the the the things that was a  
**Translation:** 

**[5030.08s] English:** a real attraction of java to lots of development shops was that you know we get our code  
**Translation:** 

**[5036.96s] English:** up and running twice as fast  
**Translation:** 

**[5040.00s] English:** You mean like the entirety of the development process, debugging, all that kind of stuff?  
**Translation:** Vocabulary: entirety: 全部过程

**[5044.88s] English:** Yeah, so if you measure time from you first touch fingers to keyboard until you get your first demo out, not much different.  
**Translation:** 

**[5060.40s] English:** But if you look from fingers touching keyboard to solid piece of software that you could release in production, it would be way faster.  
**Translation:** 

**[5072.14s] English:** And I think what people don't often realize is there's things that really slow you down.  
**Translation:** 

**[5076.90s] English:** Like the hard to catch bugs probably is the thing that really slows down that.  
**Translation:** 

**[5083.18s] English:** It really slows things down.  
**Translation:** 

**[5085.22s] English:** But also, one of the things that you get out of object orientation.  
**Translation:** Vocabulary: orientation: 面向对象

**[5090.40s] English:** And programming is a strict methodology about what are the interfaces between things.  
**Translation:** 

**[5096.06s] English:** And being really clear about how parts relate to each other.  
**Translation:** Vocabulary: interfaces: 接口; methodology: 方法论

**[5101.56s] English:** And what that helps with is so many times what people do is they kind of like sneak around the side.  
**Translation:** 

**[5112.06s] English:** So if you've built something and people are using it and you say, well, okay.  
**Translation:** 

**[5119.94s] English:** You know, I've built this.  
**Translation:** 

**[5120.38s] English:** You know, I've built this.  
**Translation:** 

**[5120.40s] English:** You know, I've built this thing.  
**Translation:** 

**[5121.42s] English:** You use it this way.  
**Translation:** 

**[5123.42s] English:** And then you change it in such a way that it still does what you said it does.  
**Translation:** 

**[5128.52s] English:** It just does it a little bit different.  
**Translation:** 

**[5130.22s] English:** Then you find out that somebody out there was sneaking around the side.  
**Translation:** 

**[5135.28s] English:** They sort of tunneled in a back door.  
**Translation:** Vocabulary: sneaking: 偷偷摸摸; tunneled: 挖洞进入

**[5138.06s] English:** And this person, their code broke.  
**Translation:** 

**[5141.86s] English:** And because they were sneaking through a side door.  
**Translation:** 

**[5146.18s] English:** And normally the attitude is, dummy.  
**Translation:** 

**[5155.80s] English:** But a lot of times, you know.  
**Translation:** Vocabulary: dummy: 笨蛋

**[5160.00s] English:** you can't get away you can't you can't just slap their hand and tell them to  
**Translation:** 

**[5165.20s] English:** not do that because you know it's you know somebody's you know some banks you  
**Translation:** 

**[5174.92s] English:** know account reconciliation system that that you know some developer decided oh  
**Translation:** 

**[5180.76s] English:** I'm lazy you know I'll just sneak through the back door and because the  
**Translation:** Vocabulary: reconciliation: 对账

**[5185.22s] English:** language allows it I mean you can't even write at them and and so one of the  
**Translation:** 

**[5189.72s] English:** things I did that that on the one hand upset a bunch of people who is that I  
**Translation:** 

**[5194.16s] English:** made it so that you really couldn't go through back doors right so so the whole  
**Translation:** 

**[5199.20s] English:** point of that was to say if you need you know if the interface here isn't right  
**Translation:** Vocabulary: interface: 用户界面

**[5206.22s] English:** the wrong way to deal with that is is to go through a back door yeah the right  
**Translation:** 

**[5211.68s] English:** way to deal with it is to walk up to the developer of this thing and say change  
**Translation:** 

**[5216.10s] English:** the interface fix it yep right and and so it was kind  
**Translation:** 

**[5219.72s] English:** of like a social engineering thing and the brilliant and people ended up  
**Translation:** 

**[5225.02s] English:** of discovering that that really made a difference in terms of you know and and  
**Translation:** 

**[5232.54s] English:** and and a bunch of this stuff you know if you're just like screwing around  
**Translation:** Vocabulary: screwing: 胡闹

**[5235.74s] English:** writing your own like you know class project scale stuff a lot of stuff  
**Translation:** 

**[5241.34s] English:** doesn't isn't quite so so important because you know you're you know both  
**Translation:** 

**[5249.72s] English:** Um, but, you know, when you're building, you know, sort of larger, more complex pieces of software that have a lot of people working on them, and especially when they like span organizations, um, you know, having, having really clear, having clarity about how that sort of gets structured, um, saves your life.  
**Translation:** 

**[5273.70s] English:** Yeah. Um, and, you know, especially, you know, there, there's so much software.  
**Translation:** 

**[5280.00s] English:** with it is fundamentally untestable you know and you know until you do the real thing right it's  
**Translation:** 

**[5288.28s] English:** better to write good code in the beginning as opposed to writing crappy code and then trying  
**Translation:** Vocabulary: crappy: 糟糕的; fundamentally: 从根本上

**[5294.10s] English:** to fix it and yeah trying to scramble and figure out and through testing figure out where the bugs  
**Translation:** 

**[5299.94s] English:** are yeah it's just like it's like it's like which shortcut caused yeah that rocket to not get where  
**Translation:** Vocabulary: scramble: 乱搞; shortcut: 捷径

**[5309.02s] English:** it was needed to go so i think one of the most beautiful ideas uh philosophically and technically  
**Translation:** 

**[5318.94s] English:** is uh of a virtual machine the java virtual machine well again apologize to romanticize  
**Translation:** Vocabulary: philosophically: 哲学上

**[5327.06s] English:** things but uh uh how did the idea of the jvm come to be how to you radical of an idea it is because  
**Translation:** 

**[5336.54s] English:** it seems to me to be just  
**Translation:** 

**[5339.02s] English:** a really interesting idea in the history of programming so and what is it so the java  
**Translation:** 

**[5346.20s] English:** virtual machine you can think of it in different ways um because it was carefully designed to have  
**Translation:** 

**[5357.44s] English:** different ways of viewing it so one view of it that most people don't really realize is there  
**Translation:** 

**[5364.74s] English:** is that you can  
**Translation:** 

**[5366.30s] English:** um  
**Translation:** 

**[5369.02s] English:** view it as sort of an encoding of the abstract syntax tree in reverse polish notation  
**Translation:** Vocabulary: encoding: 编码; syntax: 语法

**[5377.66s] English:** um i don't know if that makes any sense at all i could explain it and that would blow all over  
**Translation:** 

**[5383.58s] English:** time yeah um but the other way to think of it um and the way that it ends up being explained  
**Translation:** 

**[5389.98s] English:** is that it's it's like the the instruction set of an abstract machine that's designed such that you  
**Translation:** 

**[5398.70s] English:** can  
**Translation:** 

**[5399.02s] English:** to  
**Translation:** 

**[5400.00s] English:** that abstract machine to a physical machine and the reason that that's important so if you wind  
**Translation:** 

**[5408.68s] English:** back to the early 90s when we were talking to all of these these companies doing consumer electronics  
**Translation:** 

**[5416.44s] English:** and you talk to the purchasing people there were interesting conversations with purchasing so if  
**Translation:** Vocabulary: purchasing: 采购部门

**[5428.08s] English:** you look at how you know these you know these devices come together they're the sheet metal  
**Translation:** 

**[5433.84s] English:** and gears and circuit boards and capacitors and resistors and stuff and everything you buy has  
**Translation:** Vocabulary: capacitors: 电容器; resistors: 电阻器

**[5443.96s] English:** multiple sources right so you can buy a capacitor from here you can buy a capacitor from there  
**Translation:** 

**[5452.12s] English:** and you've got kind of a market so you know so that the you can actually get a  
**Translation:** 

**[5458.08s] English:** decent price for a capacitor um but cpus and particularly in the early 90s  
**Translation:** 

**[5469.64s] English:** um cpus were all different and all proprietary so if you use the chip from intel  
**Translation:** Vocabulary: capacitor: 电容器; proprietary: 专有技术

**[5480.26s] English:** you had to be an intel customer for the end of till the end of time  
**Translation:** 

**[5488.08s] English:** because if you wrote a bunch of software you know when you wrote software using  
**Translation:** 

**[5493.36s] English:** whatever technique you wanted and c was particularly bad about this big because  
**Translation:** 

**[5500.00s] English:** there was a lot of properties of the underlying machine that came through  
**Translation:** 

**[5507.24s] English:** so you were stuck so the code you wrote you were stuck to that particular machine you were stuck  
**Translation:** 

**[5512.26s] English:** to that particular machine which meant that they couldn't decide you know  
**Translation:** 

**[5518.08s] English:** what the hell is screwing us  
**Translation:** 

**[5520.00s] English:** I'll start buying chips from, you know, Bob's Better Chips.  
**Translation:** Vocabulary: screwing: 坑害

**[5527.88s] English:** This drove the purchasing people absolutely insane.  
**Translation:** 

**[5535.50s] English:** That they were welded into this decision.  
**Translation:** Vocabulary: welded: 固定

**[5540.26s] English:** And they would have to make this decision before the first line of software was written.  
**Translation:** 

**[5545.84s] English:** It's funny that you're talking about the purchasing people.  
**Translation:** Vocabulary: purchasing: 采购人员

**[5548.12s] English:** So that's one perspective, right?  
**Translation:** 

**[5549.50s] English:** There's a lot of other perspectives that all probably hated this idea.  
**Translation:** Vocabulary: perspectives: 观点

**[5555.18s] English:** Right.  
**Translation:** 

**[5555.42s] English:** But from a technical aspect, just like the creation of an abstraction layer that's agnostic to the underlying machine from the perspective of the developer.  
**Translation:** Vocabulary: abstraction: 抽象层; agnostic: 无关外在

**[5568.30s] English:** I mean, that's brilliant.  
**Translation:** 

**[5570.38s] English:** Well, and, you know, so that's like across the spectrum of providers of chips.  
**Translation:** 

**[5578.02s] English:** But then there's also the...  
**Translation:** 

**[5579.48s] English:** The time thing.  
**Translation:** 

**[5580.80s] English:** Because, you know, as you went from one generation to the next generation to the next generation, they were all different.  
**Translation:** 

**[5587.60s] English:** And you would often have to rewrite your software.  
**Translation:** 

**[5590.12s] English:** Oh, you mean generations of machines of different kinds?  
**Translation:** 

**[5594.96s] English:** Yeah.  
**Translation:** 

**[5594.98s] English:** So, like, one of the things that sucked about a year out of my life was when San went from the Motorola 68010 processor to the 68010.  
**Translation:** 

**[5609.48s] English:** So, like, one of the things that sucked about a year out of my life was when San went from the Motorola 68010 processor to the 68010 processor.  
**Translation:** Vocabulary: motorola: 摩托罗拉; processor: 处理器

**[5610.80s] English:** And they had a number of differences.  
**Translation:** 

**[5614.00s] English:** And one of them hit us really hard.  
**Translation:** 

**[5616.72s] English:** And I ended up being the point guy on the worst case of where the new instruction cache architecture hurt us.  
**Translation:** 

**[5629.18s] English:** Well, okay.  
**Translation:** Vocabulary: cache: 缓存

**[5629.90s] English:** So, I mean, so when did this idea...  
**Translation:** 

**[5632.76s] English:** I mean, okay.  
**Translation:** 

**[5633.32s] English:** So, yeah, you articulate a really clear fundamental problem in all of computing.  
**Translation:** 

**[5638.56s] English:** Right.  
**Translation:** Vocabulary: articulate: 表达; computing: 计算

**[5638.96s] English:** But how...  
**Translation:** 

**[5640.00s] English:** Where do you get the guts to think we can actually solve this?  
**Translation:** 

**[5644.56s] English:** You know, in our conversations with, you know, all these vendors, you know, these problems started to show up.  
**Translation:** 

**[5653.92s] English:** And I kind of had this epiphany because it reminded me of a summer job that I had had in grad school.  
**Translation:** Vocabulary: epiphany: 顿悟

**[5670.00s] English:** So, back in grad school, my thesis advisor, well, I had two thesis advisors for bizarre reasons.  
**Translation:** 

**[5682.64s] English:** One of them was a guy named Raj Reddy.  
**Translation:** Vocabulary: reddy: 拉迪

**[5684.92s] English:** The other one was Bob Sproul.  
**Translation:** 

**[5688.50s] English:** And Raj, I love Raj.  
**Translation:** Vocabulary: sproul: 斯普罗尔

**[5693.02s] English:** I really love both of them.  
**Translation:** 

**[5693.92s] English:** Raj is amazing.  
**Translation:** 

**[5696.24s] English:** So, the...  
**Translation:** 

**[5700.00s] English:** The department had bought a bunch of, like, early workstations from a company called Three Rivers Computer Company.  
**Translation:** Vocabulary: workstations: 工作站

**[5711.24s] English:** And Three Rivers Computer Company was a bunch of electrical engineers who wanted to do as little software as possible.  
**Translation:** 

**[5718.86s] English:** So, they knew that they'd need to have, like, compilers and an OS and stuff like that.  
**Translation:** 

**[5724.36s] English:** And they didn't want to do any of that.  
**Translation:** 

**[5726.52s] English:** And they wanted to do that for as close to zero money as possible.  
**Translation:** 

**[5730.00s] English:** So, what they did was they built a machine whose instruction set was literally the bytecode for UCSD Pascal, the P code.  
**Translation:** 

**[5751.94s] English:** And so, we had a bunch of software that was written for this machine.  
**Translation:** Vocabulary: bytecode: 字节码; pascal: 帕斯卡

**[5760.00s] English:** um and for various reasons you know the company wasn't doing terrifically well we had all the  
**Translation:** 

**[5768.96s] English:** software on these machines and we wanted it to run on other machines principally the vax and um  
**Translation:** Vocabulary: principally: 主要地; terrifically: 糟糕地

**[5777.06s] English:** and so raj asked me if i could come up with a way to port all of this software  
**Translation:** 

**[5787.08s] English:** translate from the from from from the the the the perk machines to vaxes  
**Translation:** 

**[5793.28s] English:** and and i think he you know what he had in mind was something that would translate from like  
**Translation:** 

**[5803.28s] English:** pascal to c or pascal to i actually at those times pretty much it was you could translate to c or  
**Translation:** 

**[5814.78s] English:** c and if you didn't like translating to c  
**Translation:** 

**[5817.08s] English:** you could translate to c um there was you know it's you know it's like the the henry ford  
**Translation:** 

**[5824.10s] English:** you know any color you want it just as long as it's black um and and i went that's really hard  
**Translation:** 

**[5833.44s] English:** um and and i and i noticed that you know and i was like looking at stuff and i went  
**Translation:** 

**[5841.98s] English:** oh i bet i could rewrite the p code into vax assembly  
**Translation:** 

**[5847.08s] English:** code  
**Translation:** 

**[5847.52s] English:** and and then i started to realize that you know there were some properties of p code that made  
**Translation:** 

**[5856.26s] English:** that really easy some properties that made it really hard so i ended up writing this thing  
**Translation:** 

**[5862.74s] English:** that translated from from p code on the three rivers perks into assembly code on the vax  
**Translation:** 

**[5872.06s] English:** and i actually got higher quality code  
**Translation:** Vocabulary: perks: 福利

**[5877.08s] English:** than the c compiler  
**Translation:** 

**[5880.00s] English:** And so so everything just got really fast.  
**Translation:** 

**[5883.28s] English:** It was really easy.  
**Translation:** 

**[5884.26s] English:** It was like, wow, I thought that was a sleazy hack because I was lazy.  
**Translation:** Vocabulary: sleazy: 卑鄙

**[5890.44s] English:** And in actual fact, it worked really well.  
**Translation:** 

**[5894.42s] English:** And I and I tried to convince people that that was maybe a good thesis topic.  
**Translation:** 

**[5899.94s] English:** Yeah.  
**Translation:** 

**[5901.38s] English:** And nobody was was, you know, it was like, nah, really?  
**Translation:** 

**[5906.70s] English:** I mean, it's kind of a brilliant idea, right?  
**Translation:** 

**[5912.32s] English:** Maybe you didn't have the you weren't able to articulate the big picture of it.  
**Translation:** Vocabulary: articulate: 表达清楚

**[5917.28s] English:** Yeah.  
**Translation:** 

**[5917.86s] English:** And I think, you know, that was a key part.  
**Translation:** 

**[5922.76s] English:** But so then, you know, clock comes forward a few years and it's like we've got to be able to, you know, that, you know, that, you know, if they want to be able to switch from, you know, this weird microprocessor to that.  
**Translation:** 

**[5936.70s] English:** Weird and totally different microprocessor.  
**Translation:** 

**[5939.36s] English:** How do you do that?  
**Translation:** 

**[5940.40s] English:** And I kind of went, oh, maybe by doing something kind of in the space of, you know, Pascal P code, you know, I could do like multiple translators.  
**Translation:** Vocabulary: pascal: 帕斯卡编程语言; translators: 翻译器

**[5955.08s] English:** And I spent some time thinking about that and thinking about, you know, what worked and what didn't work when I did the the the P code to Vax translator.  
**Translation:** 

**[5964.12s] English:** And I talked to some of the folks who were involved in Smalltalk because Smalltalk also did a Vite code.  
**Translation:** Vocabulary: smalltalk: 面向对象编程; translator: 代码转换器

**[5974.92s] English:** And and then I kind of went, yeah, let's that I want to do that.  
**Translation:** 

**[5980.84s] English:** Yeah.  
**Translation:** 

**[5981.28s] English:** Because that, you know, and it had the the other advantage that you could either interpret it or compile it.  
**Translation:** 

**[5991.82s] English:** And interpreters are usually.  
**Translation:** Vocabulary: interpret: 翻译; interpreters: 译员

**[5994.12s] English:** Easier to do, but not as fast as a compiler.  
**Translation:** 

**[6000.00s] English:** so i figured good i can be lazy again um you know you know sometimes i think that most of  
**Translation:** 

**[6007.84s] English:** my good ideas are um driven by laziness and often i find that people some of people's  
**Translation:** 

**[6014.80s] English:** stupidest ideas are because they're insufficiently lazy um yeah they just want to build something  
**Translation:** Vocabulary: insufficiently: 不够懒; stupidest: 最愚蠢

**[6022.80s] English:** really complicated it's like it doesn't need to be that complicated yeah and so and so that's how  
**Translation:** 

**[6028.40s] English:** that came out and um you know but that also turned into kind of a you know almost a religious  
**Translation:** 

**[6038.52s] English:** position on my part which was which got me in in several other fights so like like one of the  
**Translation:** 

**[6046.02s] English:** things that was a real difference was the way that arithmetic worked um you know once upon a time  
**Translation:** Vocabulary: arithmetic: 算术

**[6058.40s] English:** it wasn't always just two's complement arithmetic there were some machines that had one's complement  
**Translation:** 

**[6063.44s] English:** arithmetic which was like almost anything built by cdc um and occasionally there were machines  
**Translation:** 

**[6070.48s] English:** that were decimal arithmetic and and i was like this is crazy you know pretty much two's complement  
**Translation:** 

**[6080.24s] English:** integer arithmetic has one so just let's just do that just do that  
**Translation:** Vocabulary: decimal: 十进制; integer: 整数

**[6088.40s] English:** you know the other places where there was a lot of variability was in the way that floating point  
**Translation:** 

**[6092.72s] English:** behaved um and that was causing people throughout the software industry much pain because you  
**Translation:** Vocabulary: variability: 变化性

**[6103.68s] English:** couldn't do a numerical computing library that would work on cdc and then have it work on an  
**Translation:** 

**[6109.84s] English:** ibm machine and work on a on a deck machine um and and as a as a part of that whole struggle  
**Translation:** Vocabulary: computing: 计算; numerical: 数值的

**[6117.52s] English:** there had been this  
**Translation:** 

**[6118.40s] English:** this big  
**Translation:** 

**[6120.00s] English:** of work on floating-point standards, and this thing emerged that can be called IEEE 754,  
**Translation:** 

**[6131.80s] English:** which is the floating-point standard that pretty much has taken over the entire universe.  
**Translation:** 

**[6140.58s] English:** And at the time I was doing Java, it had pretty much completed taking over the universe.  
**Translation:** 

**[6145.80s] English:** There were still a few pockets of holdouts, but I was like, you know, it's important to  
**Translation:** Vocabulary: holdouts: 坚持者

**[6151.90s] English:** be able to say what two plus two means.  
**Translation:** 

**[6158.20s] English:** And so I went that.  
**Translation:** 

**[6162.88s] English:** And one of the ways that I got into fights with people was that there were a few machines  
**Translation:** 

**[6168.96s] English:** that did not implement IEEE 754 correctly.  
**Translation:** 

**[6175.68s] English:** Of course.  
**Translation:** 

**[6175.80s] English:** Of course.  
**Translation:** 

**[6176.80s] English:** That's all short-term kind of fights.  
**Translation:** 

**[6178.48s] English:** I think in the long term, I think this vision has won out.  
**Translation:** 

**[6182.84s] English:** Yeah.  
**Translation:** 

**[6183.96s] English:** And I think it's, you know, and it worked out over time.  
**Translation:** 

**[6186.44s] English:** I mean, the biggest fights were with Intel because they had done some strange things  
**Translation:** 

**[6194.18s] English:** with rounding.  
**Translation:** Vocabulary: rounding: 四舍五入

**[6195.18s] English:** They had done some strange things with their transcendental functions, which turned into  
**Translation:** 

**[6201.10s] English:** a mushroom cloud of, you know, weirdness.  
**Translation:** Vocabulary: transcendental: 超越函数; weirdness: 怪异现象

**[6204.68s] English:** Yeah.  
**Translation:** 

**[6205.68s] English:** In the name of optimization.  
**Translation:** Vocabulary: optimization: 优化

**[6206.68s] English:** But from the perspective of the developer, that's not that's not good.  
**Translation:** 

**[6207.68s] English:** Well, their issues with transcendental functions were just stupid.  
**Translation:** 

**[6208.68s] English:** OK.  
**Translation:** 

**[6209.68s] English:** So that's that's not even a trade off.  
**Translation:** 

**[6210.68s] English:** That's just absolutely.  
**Translation:** 

**[6211.68s] English:** Yeah.  
**Translation:** 

**[6212.68s] English:** They were they were doing range reduction in for sine and cosine using a slightly wrong  
**Translation:** 

**[6213.68s] English:** value for Pi.  
**Translation:** Vocabulary: cosine: 余弦

**[6214.68s] English:** Got it.  
**Translation:** 

**[6215.68s] English:** Well, ten minutes.  
**Translation:** 

**[6216.68s] English:** So in the interest of time, two questions.  
**Translation:** 

**[6217.68s] English:** So one about Android.  
**Translation:** 

**[6218.68s] English:** One about life.  
**Translation:** 

**[6219.68s] English:** All right.  
**Translation:** 

**[6220.68s] English:** So, you know, you know, the challenge I have with the cloud is that I know that the cloud  
**Translation:** 

**[6221.68s] English:** is not that good.  
**Translation:** 

**[6222.68s] English:** And I don't know that you can actually do that.  
**Translation:** 

**[6223.68s] English:** It's not that it's not as good as it is.  
**Translation:** 

**[6224.68s] English:** Right.  
**Translation:** 

**[6225.68s] English:** I mean, I've probably done it a couple of times.  
**Translation:** 

**[6226.68s] English:** wrong value for pi got it go ahead 10 minutes so in the interest of time  
**Translation:** 

**[6232.68s] English:** two questions so one about android one about life uh so one i mean we could talk for  
**Translation:** 

**[6240.00s] English:** are many more hours i hope uh eventually we might talk again but i gotta ask you about android  
**Translation:** 

**[6246.58s] English:** and the use of java there because it's one of the many places where java  
**Translation:** 

**[6252.78s] English:** just has a huge impact on this world just on your opinion is there things that make you happy  
**Translation:** 

**[6260.78s] English:** uh about the way and uh java is used in the android world and are there things that  
**Translation:** 

**[6267.08s] English:** you wish were different i i don't know how to do a short answer to that um but i have to do a short  
**Translation:** 

**[6273.66s] English:** answer to that so you know i'm happy that they did it um java had been running on cell phones  
**Translation:** 

**[6280.68s] English:** at that time for quite a few years and it worked really really well um there were things about  
**Translation:** 

**[6286.98s] English:** how they did it and and in particular um various ways that they  
**Translation:** 

**[6295.42s] English:** kind of  
**Translation:** 

**[6297.08s] English:** you know violated all kinds of contracts the guy who who led it andy rubin  
**Translation:** Vocabulary: rubin: 安迪·鲁宾; violated: 违反

**[6302.98s] English:** he crossed a lot of lines there's some lines crossed yeah lines were crossed  
**Translation:** 

**[6308.96s] English:** that have since you know mushroomed into giant court cases um and you know they didn't need to  
**Translation:** 

**[6318.94s] English:** do that and in fact it would have been so much cheaper for them to not cross lines  
**Translation:** 

**[6324.86s] English:** i mean i suppose they didn't anticipate  
**Translation:** Vocabulary: anticipate: 预料到

**[6327.08s] English:** the the success uh of this whole endeavor um or do you think at that time it was already clear  
**Translation:** 

**[6336.40s] English:** that this is uh it's going to blow up i i guess i i i i sort of came to believe that it didn't matter  
**Translation:** Vocabulary: endeavor: 努力

**[6342.70s] English:** what andy did it was going to blow up okay okay you see he's he you know i kind of started to  
**Translation:** 

**[6351.72s] English:** think of him as as as like a manufacturer of bombs  
**Translation:** 

**[6357.08s] English:** uh yeah  
**Translation:** 

**[6360.00s] English:** Some of the best things in this world come about through a little bit of explosive.  
**Translation:** Vocabulary: explosive: 爆炸物

**[6365.74s] English:** Well, and some of the worst.  
**Translation:** 

**[6367.04s] English:** And some of the worst, beautifully put.  
**Translation:** 

**[6369.10s] English:** But is there, and like you said, I mean, does that make you proud that Java is in millions?  
**Translation:** 

**[6379.14s] English:** I mean, it could be billions of devices.  
**Translation:** 

**[6381.50s] English:** Yeah.  
**Translation:** 

**[6382.00s] English:** Well, I mean, it was in billions of phones before Android came along.  
**Translation:** 

**[6386.46s] English:** And, you know, I'm just as proud as, you know, of the way that, like, the smart card standards adopted Java.  
**Translation:** 

**[6399.26s] English:** And they did, you know, everybody involved in that did a really good job.  
**Translation:** 

**[6403.24s] English:** And that's, you know, billions and billions.  
**Translation:** 

**[6408.40s] English:** That's crazy.  
**Translation:** 

**[6409.44s] English:** The SIM cards, you know, the SIM cards in your pocket.  
**Translation:** 

**[6413.34s] English:** Yeah, I mean, it's...  
**Translation:** 

**[6414.64s] English:** I've been outside of that world for a decade.  
**Translation:** 

**[6416.70s] English:** So, I don't know how that has evolved.  
**Translation:** 

**[6420.34s] English:** But, you know, it's just been crazy.  
**Translation:** 

**[6424.56s] English:** So, on that topic, let me ask, again, there's a million technical things we could talk about.  
**Translation:** 

**[6432.44s] English:** But let me ask the absurd, the old philosophical question about life.  
**Translation:** 

**[6439.84s] English:** What do you hope when you look back at your life and people talk about you around the world?  
**Translation:** Vocabulary: philosophical: 哲学的

**[6446.68s] English:** And people write about you 500 years from now?  
**Translation:** 

**[6449.60s] English:** What do you hope your legacy is?  
**Translation:** 

**[6454.58s] English:** People not being afraid to take a leap of faith.  
**Translation:** 

**[6459.92s] English:** I mean, you know, I've got this kind of weird history of doing weird stuff and...  
**Translation:** 

**[6467.58s] English:** It worked out pretty damn well.  
**Translation:** 

**[6469.32s] English:** It worked out, right?  
**Translation:** 

**[6470.92s] English:** And I think some of the weirder stuff that I've done...  
**Translation:** 

**[6474.36s] English:** Um...  
**Translation:** 

**[6475.02s] English:** Has been the coolest.  
**Translation:** 

**[6477.00s] English:** And some of it...  
**Translation:** 

**[6478.14s] English:** Some of it crashed and burned.  
**Translation:** 

**[6479.80s] English:** And...  
**Translation:** 

**[6480.00s] English:** um you know you know i think well over half of the stuff that i've done has crashed and burned  
**Translation:** 

**[6486.84s] English:** um which has occasionally been really annoying but still you kept doing it but yeah yeah yeah  
**Translation:** 

**[6495.84s] English:** and you know there you know even when things crash and burn you you at least learn something  
**Translation:** 

**[6500.72s] English:** from it by way of advice you know people developers engineers scientists are just people  
**Translation:** 

**[6508.74s] English:** who are young uh to look up to you what advice would you give them how to uh how to approach  
**Translation:** 

**[6516.66s] English:** their life don't be afraid of risk it's okay to do stupid things once  
**Translation:** 

**[6521.88s] English:** maybe about a couple times you know you you know you get you get a pass on the the first time or  
**Translation:** 

**[6530.72s] English:** two that you do something stupid you know the third or fourth time yeah not so much yeah um  
**Translation:** 

**[6538.74s] English:** but also you know i don't know why but really early on i started to think about  
**Translation:** 

**[6549.22s] English:** um ethical choices in my life um and because i a big science fiction fan  
**Translation:** 

**[6557.64s] English:** um i i i got to thinking about like just about every technical decision i make  
**Translation:** 

**[6566.66s] English:** in terms of i don't know  
**Translation:** 

**[6568.74s] English:** you want you know are you building blade runner or star trek  
**Translation:** 

**[6573.62s] English:** which one's better which which future would you rather live in you know so what's the what's the  
**Translation:** 

**[6579.62s] English:** answer to that well i would i would sure rather live in the universe of star trek yeah that opens  
**Translation:** 

**[6586.50s] English:** up a whole topic about ai but that's a really interesting yeah yeah yeah it's a really  
**Translation:** 

**[6592.18s] English:** interesting idea so your favorite ai system would be data uh from uh from star trek as opposed to  
**Translation:** 

**[6598.74s] English:** would it be more concerned about like your own thinking about it like even with the  
**Translation:** 

**[6601.94s] English:** own thinking of the universe if you did because that's not the the only way to provide that  
**Translation:** 

**[6603.54s] English:** information the only way to do this would be to apologize to the universe um and i think i  
**Translation:** 

**[6610.14s] English:** think that's that's not a really good uh answer to that question and i'm gonna go ahead and  
**Translation:** 

**[6612.82s] English:** wrap it up and i'll get back to you as we go and i'll see you guys next time  
**Translation:** 

**[6600.00s] English:** sky net yeah beautifully put i don't think there's a better way to end it james i can't say enough  
**Translation:** 

**[6607.20s] English:** how much of an honor it is to meet you to talk to you thanks so much for wasting your time with me  
**Translation:** 

**[6611.54s] English:** today uh not a waste at all thanks james all right thanks thanks for listening to this conversation  
**Translation:** 

**[6617.98s] English:** with james gosling and thank you to our sponsors public goods better help and express vpn please  
**Translation:** Vocabulary: sponsors: 赞助商

**[6624.50s] English:** check out these sponsors in the description to get a discount and to support this podcast  
**Translation:** 

**[6629.64s] English:** if you enjoy this thing subscribe on youtube review it with five stars on apple podcast  
**Translation:** Vocabulary: subscribe: 订阅

**[6634.52s] English:** follow on spotify support on patreon or connect with me on twitter at lex friedman and now let  
**Translation:** 

**[6641.48s] English:** me leave you with some words from james gosling one of the toughest things about life is making  
**Translation:** Vocabulary: friedman: 莱克斯·弗里德曼; gosling: 詹姆斯·戈斯林; toughest: 最难的

**[6647.38s] English:** choices thank you for listening and hope to see you next time  
**Translation:** 

**[6659.64s] English:** you  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
