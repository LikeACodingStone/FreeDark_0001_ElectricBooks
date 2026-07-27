# Podcast vocabulary notes
Source file: Lex Fridman - John Carmack： Doom, Quake, VR, AGI, Programming, Video Games, and Rockets ｜ Lex Fridman Podcast #309.opus

**[0.00s] English:** I remember the reaction where he had drawn these characters and he was slowly moving around and like people had no experience with 3D navigation.  
**Translation:** 

**[6.86s] English:** It was all still keyboard.  
**Translation:** Vocabulary: navigation: 三维导航

**[7.98s] English:** We didn't even have mice set up at that time, but slowly moving, going up, picked up a key, go to a wall.  
**Translation:** 

**[14.78s] English:** The wall disappears in a little animation and there's a monster like right there.  
**Translation:** 

**[18.62s] English:** And he practically fell out of his chair.  
**Translation:** 

**[20.48s] English:** It was just like, ah, and games just didn't do that.  
**Translation:** 

**[24.74s] English:** You know, the games were the God's eye view.  
**Translation:** 

**[26.86s] English:** You were a little invested in your little guy.  
**Translation:** 

**[28.74s] English:** You can be like, you know, happy or sad when things happen, but you just did not get that kind of startle reaction.  
**Translation:** 

**[35.00s] English:** You weren't inside your face, something in the back of your brain.  
**Translation:** 

**[38.08s] English:** Some reptile brain thing is just going, oh, shit, something just happened.  
**Translation:** 

**[42.36s] English:** And that was one of those early points where it's like, yeah, this is going to make a difference.  
**Translation:** Vocabulary: reptile: 爬行动物

**[47.28s] English:** This is going to be powerful and it's going to matter.  
**Translation:** 

**[51.74s] English:** The following is a conversation with John Carmack, widely considered to be one of the greatest programmers ever.  
**Translation:** 

**[58.94s] English:** He was the co-founder of id Software and the lead programmer on several games that revolutionized the technology,  
**Translation:** 

**[66.36s] English:** the experience and the role of gaming in our society, including Commander Keen, Wolfenstein 3D, Doom and Quake.  
**Translation:** Vocabulary: programmer: 程序员; revolutionized: 革新; wolfenstein: 狼穴

**[75.52s] English:** He spent many years as the CTO of Oculus VR, helping to create portals into virtual worlds and to define the technological path to the metaverse and meta.  
**Translation:** 

**[87.68s] English:** And now.  
**Translation:** 

**[89.04s] English:** He has been shifting some of his attention to the problem of artificial general intelligence.  
**Translation:** 

**[94.86s] English:** This was the longest conversation on this podcast at over five hours.  
**Translation:** Vocabulary: shifting: 转移

**[100.14s] English:** And still, I could talk to John many, many more times.  
**Translation:** 

**[103.80s] English:** And we hope to do just that.  
**Translation:** 

**[106.50s] English:** This is the Lex Friedman podcast.  
**Translation:** 

**[108.66s] English:** To support it, please check out our sponsors in the description.  
**Translation:** Vocabulary: friedman: 弗里德曼; sponsors: 赞助商

**[112.20s] English:** And now, dear friends, here's John Carmack.  
**Translation:** 

**[117.44s] English:** What was the first program?  
**Translation:** 

**[118.74s] English:** You've ever written.  
**Translation:** 

**[120.00s] English:** Do you remember? Yeah, I do. So I remember being in a radio shack going up to the TRS-80 computers  
**Translation:** Vocabulary: shack: 破旧小屋

**[126.38s] English:** and learning just enough to be able to do 10 print John Carmack. And it's kind of interesting how,  
**Translation:** 

**[134.06s] English:** of course, I've, you know, Carnegie and Ritchie kind of standardized Hello World as the first  
**Translation:** Vocabulary: standardized: 标准化

**[139.50s] English:** thing that you do in every computer programming language and every computer, but not having any  
**Translation:** 

**[144.20s] English:** interaction with the cultures of Unix or any other standardized things. It was just like,  
**Translation:** 

**[148.94s] English:** well, what am I going to say? I'm going to say my name. And then you learn how to do GoTo10 and  
**Translation:** 

**[153.24s] English:** have it scroll all off the screen. And that was definitely the first thing that I wound up doing  
**Translation:** Vocabulary: scroll: 滚动

**[158.24s] English:** on a computer. Can I ask you a programming advice? I was always told in the beginning that you're  
**Translation:** 

**[162.96s] English:** not allowed to use GoTo statements. That's really bad programming. Is this correct or not? Jumping  
**Translation:** 

**[167.30s] English:** around code, can we look at the philosophy and the technical aspects of the GoTo statement that  
**Translation:** 

**[173.82s] English:** seems so convenient, but it's supposed to be bad programming? Well, so certainly back in the day  
**Translation:** 

**[177.22s] English:** in basic programming languages,  
**Translation:** 

**[178.94s] English:** you didn't have proper loops. You didn't have four whiles and repeats. You know,  
**Translation:** 

**[182.76s] English:** that was the land of Pascal for people that kind of generally had access to it back then. So  
**Translation:** 

**[187.54s] English:** you had no choice but to use GoTo's. And as you made what were big programs back then,  
**Translation:** Vocabulary: pascal: 帕斯卡

**[193.52s] English:** which were a thousand line basic program is a really big program. They did tend to  
**Translation:** 

**[197.78s] English:** sort of degenerate into madness. You didn't have good editors or code exploration tools.  
**Translation:** Vocabulary: degenerate: 退化

**[203.12s] English:** So you would wind up fixing things in one place, add a little patch. And there's reasons why  
**Translation:** 

**[208.40s] English:** structured programming is so important. And I think that's a really good point.  
**Translation:** 

**[208.94s] English:** Programming generally helps understanding, but GoTo's aren't poisonous. Sometimes they're the  
**Translation:** 

**[214.60s] English:** right thing to do. Usually it's because there's a language feature missing like nested breaks or  
**Translation:** 

**[220.04s] English:** something where it can sometimes be better to do a GoTo cleanup or GoTo error rather than having  
**Translation:** 

**[227.04s] English:** multiple flags, multiple if statements littered throughout things. But it is rare. I mean,  
**Translation:** Vocabulary: cleanup: 清理; littered: 杂乱分布

**[231.96s] English:** if you grep through all of my code right now, I don't think any of my current code bases would  
**Translation:** 

**[237.68s] English:** actually have a GoTo.  
**Translation:** 

**[238.94s] English:** But I  
**Translation:** 

**[240.00s] English:** deep within sort of the technical underpinnings of a major game engine you're going to have some  
**Translation:** Vocabulary: underpinnings: 基础原理

**[244.38s] English:** go-tos in a couple places probably yeah the infrastructure on top of like the closer you  
**Translation:** 

**[250.12s] English:** get to machine code the more go-tos you're going to see the more of these like hacks you're going  
**Translation:** Vocabulary: hacks: 巧妙解决办法

**[254.78s] English:** to see because uh the set of features available to you in low-level programming languages is not  
**Translation:** 

**[260.24s] English:** is limited so print john carmack when is the first time if we could talk about love that you  
**Translation:** 

**[270.22s] English:** fell in love with programming you said like this this is really something special it really was  
**Translation:** 

**[275.52s] English:** something that was one of those love at first sight things where just really from the time  
**Translation:** 

**[279.88s] English:** that i understood what a computer was even i mean i remember looking through old encyclopedias at  
**Translation:** 

**[285.52s] English:** the black and white photos of the ibm mainframes at the reel-to-reel tape decks  
**Translation:** Vocabulary: encyclopedias: 百科全书; mainframes: 大型机

**[290.24s] English:** and for people nowadays it can be a little hard to understand what the world was like then from  
**Translation:** 

**[295.14s] English:** information gathering where i would go to the libraries and there would be a couple books on  
**Translation:** 

**[300.58s] English:** the shelf about computers and they would be very out of date even at that point just not a lot of  
**Translation:** 

**[305.92s] English:** information but i would grab everything that i could find and you know devour everything whenever  
**Translation:** Vocabulary: devour: 贪婪吸收

**[310.84s] English:** time or newsweek had some article about computers i would like cut it out with scissors and put it  
**Translation:** 

**[316.48s] English:** somewhere it just it felt like this magical thing to me this  
**Translation:** Vocabulary: newsweek: 新闻周刊

**[320.16s] English:** you have to put right there and you have to figure out how to replace it and you have to  
**Translation:** 

**[320.22s] English:** weld it in a different way and you know i had a lot of technical questions but like even just in the  
**Translation:** 

**[320.24s] English:** idea that the computer would just do exactly what you told it to. I mean, and there's a little bit  
**Translation:** 

**[325.34s] English:** of the genie monkey's paw sort of issues there where you'd better be really, really careful with  
**Translation:** Vocabulary: genie: 精灵

**[329.86s] English:** what you're telling it to do. But it wasn't going to backtalk you. It wasn't going to have a  
**Translation:** 

**[333.90s] English:** different point of view. It was going to carry out what you told it to do. And if you had the  
**Translation:** Vocabulary: backtalk: 顶嘴

**[338.76s] English:** right commands, you could make it do these pretty magical things. And so what kind of programs did  
**Translation:** 

**[344.84s] English:** you write at first? So beyond the print, John Carmack. So I can remember as going through the  
**Translation:** 

**[350.78s] English:** learning process where you find at the start, you're just learning how to do the most basic  
**Translation:** 

**[355.46s] English:** possible things. And I can remember stuff like a Superman comic that  
**Translation:** 

**[360.00s] English:** Radio Shack commissioned to have, it's like Superman had lost some of his super brain and  
**Translation:** 

**[364.92s] English:** kids had to use Radio Shack TRS-80 computers to do calculations to help him kind of complete his  
**Translation:** Vocabulary: commissioned: 受托制作; shack: 小屋

**[371.14s] English:** heroics. And I'd find little things like that and then get a few basic books to be able to  
**Translation:** 

**[378.42s] English:** kind of work my way up. And again, it was so precious back then. I had a couple books that  
**Translation:** 

**[383.76s] English:** would teach me important things about it. I had one book that I could start to learn a little bit  
**Translation:** 

**[388.98s] English:** of assembly language from, and I'd have a few books on BASIC and some things that I could get  
**Translation:** 

**[393.02s] English:** from the libraries. But my goals in the early days was almost always making games of various  
**Translation:** 

**[399.12s] English:** kinds. I loved the arcade games and the early Atari 2600 games, and being able to do some of  
**Translation:** Vocabulary: arcade: 街机游戏

**[406.30s] English:** those things myself on the computers was very much what I aspired to. And it was a whole journey  
**Translation:** 

**[412.28s] English:** where if you learn normal BASIC, you can't do any kind of an action game. You can write an  
**Translation:** 

**[416.58s] English:** adventure game. You can write things where  
**Translation:** 

**[418.62s] English:** you can do a lot of things, but you can't do any kind of an action game.  
**Translation:** 

**[418.96s] English:** What do you do here? Get sword, attack troll, that type of thing. And that can be done in the  
**Translation:** 

**[424.86s] English:** context of BASIC. But to do things that had moving graphics, there were only the most  
**Translation:** Vocabulary: troll: 怪物

**[430.32s] English:** limited things you could possibly do. You could maybe do breakout or pong or that sort of thing  
**Translation:** 

**[434.90s] English:** in low-resolution graphics. And in fact, one of my first sort of major technical hacks that I was  
**Translation:** Vocabulary: hacks: 技术技巧

**[441.10s] English:** kind of fond of was on the Apple II computers. They had a mode called low-resolution graphics,  
**Translation:** 

**[448.60s] English:** where, of course, all graphics were low-resolution back then. But regular low-resolution graphics,  
**Translation:** 

**[454.10s] English:** it was a grid of 40 by 40 pixels normally, but they could have 16 different colors.  
**Translation:** 

**[459.64s] English:** And I wanted to make a game kind of like the arcade game Vanguard, just a scrolling game.  
**Translation:** Vocabulary: pixels: 像素; scrolling: 滚动; vanguard: 先锋

**[464.92s] English:** And I wanted to just kind of have it scroll vertically up. And I could move a little ship  
**Translation:** 

**[468.64s] English:** around. You could manage to do that in BASIC, but there's no way you could redraw the whole screen.  
**Translation:** Vocabulary: scroll: 滚动; vertically: 垂直地

**[473.22s] English:** And I remember at the time just coming up with what felt like a brainstorm to me,  
**Translation:** 

**[478.14s] English:** where I knew enough.  
**Translation:** 

**[480.00s] English:** about the way the hardware was controlled, where the text screen and the low-resolution  
**Translation:** 

**[484.40s] English:** graphics screen were basically the same thing. And all those computers could scroll their text  
**Translation:** 

**[489.14s] English:** screen reasonably. You could do a listing, and it would scroll things up. And I figured out that I  
**Translation:** 

**[494.24s] English:** could kind of tweak just a couple things that I barely understood to put it into a graphics mode,  
**Translation:** Vocabulary: reasonably: 合乎情理; tweak: 微调

**[499.64s] English:** and I could draw graphics, and then I could just do a line feed at the very bottom of the screen,  
**Translation:** 

**[504.26s] English:** and then the system would scroll it all up using an assembly language routine that I didn't know  
**Translation:** 

**[508.62s] English:** how to write back then. So that was this first great hack that sort of had analogs later on in  
**Translation:** 

**[515.48s] English:** my career for a lot of different things. So I found out that I could draw a screen, I could do  
**Translation:** Vocabulary: analogs: 类似事物

**[519.76s] English:** a line feed at the bottom, it would scroll it up once, I could draw a couple more lines of stuff  
**Translation:** 

**[523.76s] English:** at the bottom, and that was my first way to kind of scroll the screen, which was interesting in  
**Translation:** 

**[530.08s] English:** that that played a big part later on in the id Software days as well.  
**Translation:** 

**[533.16s] English:** So do efficient drawing where you don't have to draw the whole screen,  
**Translation:** 

**[538.62s] English:** but you draw from the bottom using the thing that was designed in the hardware for text output?  
**Translation:** 

**[544.68s] English:** Yeah. Where so much of, until recently, game design was limited by what you could actually  
**Translation:** 

**[552.04s] English:** get the computer to do. Where it's easy to say, like, okay, I want to scroll the screen. You just  
**Translation:** 

**[556.24s] English:** redraw the entire screen at a slight offset. And nowadays, that works just fine. Computers  
**Translation:** 

**[562.08s] English:** are ludicrously fast. But up until a decade ago or so, there were all these  
**Translation:** 

**[568.62s] English:** things everybody wanted to do. But if they knew enough programming to be able to make it happen,  
**Translation:** Vocabulary: ludicrously: 荒谬地

**[573.54s] English:** it would happen too slow to be a good experience, either just ridiculously slow or just slow enough  
**Translation:** 

**[579.34s] English:** that it wasn't fun to experience it like that. So, so much of kind of the first couple decades  
**Translation:** Vocabulary: ridiculously: 极其

**[584.58s] English:** of the programming work that I did was largely figuring out how to do something that everybody  
**Translation:** 

**[589.20s] English:** knows how they want it to happen. It just has to happen two to ten times faster than sort of the  
**Translation:** 

**[594.86s] English:** straightforward way of doing things would make it happen.  
**Translation:** 

**[598.62s] English:** And it's different now because  
**Translation:** Vocabulary: straightforward: 直截了当

**[600.00s] English:** at this point lots of things you can just do in the most naive possible way and it still works  
**Translation:** 

**[605.88s] English:** out you know you don't have nearly the creative limitations or the incentives for optimizing on  
**Translation:** Vocabulary: incentives: 激励; naive: 幼稚; optimizing: 优化

**[611.80s] English:** that level and there's a lot of pros and cons to that but i do generally you know i'm not going to  
**Translation:** 

**[616.60s] English:** do the the angry old man shaking my fist at the clouds bit where back in my day programmers had  
**Translation:** 

**[621.70s] English:** to do real programming you know it's it's amazing that you can just kind of pick an idea and go do  
**Translation:** 

**[627.18s] English:** it right now and you don't have to be some assembly language wizard or deep gpu arcanist  
**Translation:** Vocabulary: arcanist: 神秘专家

**[632.38s] English:** to be able to figure out how to make your wishes happen well there's still see that's true but let  
**Translation:** 

**[638.68s] English:** me put on my old man with a fist hat and say that probably the thing that will define the future  
**Translation:** 

**[645.08s] English:** still requires you to operate at the limits of the current system so we'll probably talk about  
**Translation:** 

**[651.48s] English:** this but if you talk about building the metaverse and building a vr experience that's compelling  
**Translation:** Vocabulary: compelling: 引人入胜; metaverse: 元宇宙

**[656.80s] English:** it's  
**Translation:** 

**[657.18s] English:** it probably requires you to not to go to assembly or maybe not literally but sort of  
**Translation:** 

**[664.26s] English:** spiritually to go to the limits of what the system is capable of and that really was why  
**Translation:** 

**[669.52s] English:** virtual reality was um specifically interesting to me where it had all the ties to you could say  
**Translation:** Vocabulary: spiritually: 精神上

**[675.52s] English:** that even back in the early days i have some old magazine articles that's talking about doom as a  
**Translation:** 

**[680.80s] English:** reality experience back when just seeing anything in 3d uh so you could say that we've been trying  
**Translation:** 

**[686.80s] English:** to build those virtual experiences from the very beginning. And in the modern era of virtual  
**Translation:** 

**[692.00s] English:** reality, especially on the mobile side of things, when it's standalone, you're basically using a  
**Translation:** Vocabulary: standalone: 独立运行

**[696.80s] English:** cell phone chip to be able to produce these very immersive experiences. It does require work. It's  
**Translation:** 

**[703.84s] English:** not at the level of what an old school console game programmer would have operated at, where  
**Translation:** Vocabulary: immersive: 身临其境; programmer: 程序员

**[708.62s] English:** you're looking at hardware registers and you're scheduling all the DMA accesses. But it is still  
**Translation:** 

**[714.20s] English:** definitely a different level than what a web developer or even a PC Steam game developer  
**Translation:** Vocabulary: accesses: 存取请求

**[720.00s] English:** usually has to work at and again it's great there's opportunities for people that want to  
**Translation:** 

**[724.50s] English:** operate at either end of that spectrum there and still provide a lot of value to the world  
**Translation:** 

**[728.24s] English:** let me ask you uh uh sort of a big question about preference what would you say is the best  
**Translation:** 

**[737.20s] English:** programming language your favorite but also the best you've seen throughout your career  
**Translation:** 

**[744.92s] English:** you're considered by many to be the greatest programmer ever i mean it's so difficult to  
**Translation:** 

**[750.68s] English:** place that label on anyone if but if you put it on anyone it's you so let me ask you these kind  
**Translation:** 

**[755.20s] English:** of ridiculous questions of what's the best band of all time but in your case what's the best  
**Translation:** 

**[760.12s] English:** programming language everything has all the caveats about it but so what i use so nowadays  
**Translation:** Vocabulary: caveats: 注意事项

**[765.72s] English:** i i do program a reasonable amount of python for aiml sorts of work uh that's i'm not a native  
**Translation:** 

**[773.22s] English:** python programmer it's something i can't do i'm not a native python programmer i'm not a native  
**Translation:** 

**[774.90s] English:** very late in my career i understand what it's good for you don't dream in python i do not and it has  
**Translation:** 

**[781.58s] English:** some of those things where there's some amazing stats when you say if you just start if you make  
**Translation:** 

**[786.34s] English:** a loop you know a triply nested loop and start doing operations in python you can be thousands  
**Translation:** 

**[792.32s] English:** to potentially a million times slower than a proper gpu tensor operation and these are staggering  
**Translation:** Vocabulary: staggering: 令人震惊; triply: 三重

**[798.98s] English:** numbers you know you can be as much slower as we've almost gotten faster in our uh you know  
**Translation:** 

**[804.06s] English:** our pace of progress and we can be as much slower as we've almost gotten faster in our  
**Translation:** 

**[804.90s] English:** all this other miraculous stuff so your intuition's about inefficiencies within the python  
**Translation:** 

**[809.60s] English:** sort of it keeps hitting me upside the face where it just it's gotten to the point now i understand  
**Translation:** Vocabulary: inefficiencies: 低效现象; miraculous: 奇迹般; upside: 上方

**[814.00s] English:** it's like okay you just can't do a loop if you care about performance in python you have to  
**Translation:** 

**[818.96s] English:** figure out how you can reformat this into some big vector operation or something that's going  
**Translation:** 

**[823.92s] English:** to be done completely within a c++ library but the other hand is it's it's amazingly convenient  
**Translation:** 

**[829.68s] English:** and you just see stuff that people are able to cobble together by you just import a few  
**Translation:** Vocabulary: cobble: 拼凑

**[834.72s] English:** different things and you can do stuff that nobody on earth could do 10 years ago and you can do it  
**Translation:** 

**[839.44s] English:** in a little cook  
**Translation:** 

**[840.00s] English:** book thing that you copy-pasted out of a website. So that is really great. When I'm sitting down to  
**Translation:** 

**[845.82s] English:** do what I consider kind of serious programming, it's still in C++, and it's really kind of a  
**Translation:** 

**[851.74s] English:** C-flavored C++ at that, where I'm not big into the modern template metaprogramming sorts of things.  
**Translation:** 

**[858.62s] English:** I see a lot of train wrecks coming from some of that over-abstraction. I spent a few years really  
**Translation:** Vocabulary: metaprogramming: 元编程; template: 模板

**[865.38s] English:** going kind of deep into the kind of the historical Lisp work, and Haskell, and some of the functional  
**Translation:** 

**[871.66s] English:** programming sides of things. And there is a lot of value there in the way you think about things,  
**Translation:** Vocabulary: haskell: 哈斯克尔语言

**[878.58s] English:** and I changed a lot of the way I write my C and C++ code based on what I learned about  
**Translation:** 

**[883.86s] English:** the value that comes out of not having this random mutable state that you kind of lose track of.  
**Translation:** 

**[890.10s] English:** Because something that many people don't really appreciate until they've been at it for a long  
**Translation:** 

**[895.06s] English:** time...  
**Translation:** 

**[895.38s] English:** Is that it's not the writing of the program initially, it's the whole lifespan of the  
**Translation:** 

**[899.74s] English:** program. And that's when it's not necessarily just how fast you wrote it, or how fast it operates,  
**Translation:** Vocabulary: lifespan: 生命周期

**[905.40s] English:** but it's how can it bend and adapt as situations change. And then the thing that I've really been  
**Translation:** 

**[910.68s] English:** learning in my time at Meta with the Oculus and VR work is, it's also how well it hands off between  
**Translation:** Vocabulary: oculus: Oculus头显

**[917.28s] English:** a continuous kind of revolving door of programmers taking over maintenance and different things, and  
**Translation:** 

**[922.06s] English:** how you get people up to speed in different areas. And there's all these other things that I've learned  
**Translation:** Vocabulary: programmers: 程序员; revolving: 旋转

**[925.36s] English:** in the past, and I think that's really what I've learned in the past, is that it's a really good  
**Translation:** 

**[928.18s] English:** way to get people up to speed. And I think that's really what I've learned in the past, is that it's  
**Translation:** 

**[928.40s] English:** a really good way to get people up to speed. And I think that's really good way to get people up to speed.  
**Translation:** 

**[928.44s] English:** Is C++ a good language for handover between engineers?  
**Translation:** 

**[932.12s] English:** Probably not the best. And there's some really interesting aspects to this, where  
**Translation:** 

**[937.14s] English:** in some cases, languages that are not generally thought well of for many reasons, like C is  
**Translation:** 

**[944.18s] English:** derided pretty broadly that, yes, obviously all of these security flaws that happen with the memory  
**Translation:** 

**[949.10s] English:** and unsafeness and buffer overruns and the things that you've got there. But there is this  
**Translation:** Vocabulary: buffer: 缓冲区; unsafeness: 不安全性

**[954.88s] English:** underappreciated aspect to the language is so simple, anyone can go and  
**Translation:** 

**[960.00s] English:** you know, if you know C, you can generally jump in someplace and not have to learn  
**Translation:** Vocabulary: someplace: 某处; underappreciated: 被忽视

**[963.98s] English:** what paradigms they're using, because there just aren't that many available. I think there's,  
**Translation:** 

**[969.32s] English:** you know, and there's some really, really well written C code, like it's, I find it great that  
**Translation:** Vocabulary: paradigms: 范式

**[974.34s] English:** if I'm messing around with something in OpenBSD, say, I mean, I can be walking around in the  
**Translation:** 

**[978.86s] English:** kernel, and I'm like, I understand everything that's going on here. It's not hard for me to  
**Translation:** Vocabulary: kernel: 内核

**[983.40s] English:** figure out what's I, you know, what I need to do to, you know, make whatever change that I need to,  
**Translation:** 

**[989.10s] English:** while you can have, you know, more significant languages, like the downside of Lisp, where I  
**Translation:** Vocabulary: downside: 缺点

**[995.24s] English:** don't regret the time that I spent with Lisp, I think that it I, it did help, you know, help my  
**Translation:** 

**[1000.46s] English:** thinking about programming in some ways. But the people that are the biggest defenders of Lisp are  
**Translation:** 

**[1005.50s] English:** saying how malleable of a language it is that if you write a huge Lisp program, you've basically  
**Translation:** 

**[1010.60s] English:** invented your own kind of language and structure, because it's not the primitives of the language  
**Translation:** Vocabulary: malleable: 可塑性强; primitives: 基本构建块

**[1015.84s] English:** you're using very much. It's all of the things you've built on top of that.  
**Translation:** 

**[1019.10s] English:** And then a language like Racket, kind of one of the more modern Lisp versions,  
**Translation:** 

**[1023.40s] English:** it's essentially touted as a language for building other languages. And I understand the value of  
**Translation:** 

**[1029.78s] English:** that for a tiny little project. But the idea of that for one of these long term supported by lots  
**Translation:** Vocabulary: touted: 宣传

**[1035.86s] English:** of people kind of horrifies me where all of those abstractions that you're like, okay, you can't  
**Translation:** 

**[1041.24s] English:** touch this code till you educate yourself on all of these things that we've built on top of that.  
**Translation:** Vocabulary: abstractions: 抽象概念; horrifies: 令害怕

**[1046.56s] English:** And it was interesting to see how,  
**Translation:** 

**[1049.10s] English:** when Google made Go, a lot of the criticisms of that are it's like, wow, this is not a state of  
**Translation:** Vocabulary: criticisms: 批评

**[1054.24s] English:** the art language. This language is just so simple and almost crude. And you could see the programming  
**Translation:** 

**[1059.16s] English:** language people just looking down at it. But it does seem to be quite popular as basically saying,  
**Translation:** 

**[1065.16s] English:** this is the good things about C, everybody can just jump right in and use it. You don't need  
**Translation:** 

**[1070.06s] English:** to restructure your brain to write good code in it. So I wish that I had more opportunity for  
**Translation:** Vocabulary: restructure: 重新构建

**[1076.42s] English:** doing some work in Go.  
**Translation:** 

**[1079.10s] English:** Rust is the other  
**Translation:** 

**[1080.00s] English:** modern language that everybody talks about that I'm not fit to pass judgment on. I've done a  
**Translation:** 

**[1085.16s] English:** little bit beyond Hello World. I wrote some video decompression work in Rust just as an exercise,  
**Translation:** Vocabulary: decompression: 数据解压

**[1091.34s] English:** but that was a few years ago and I haven't really used it since. The best programming language is  
**Translation:** 

**[1096.18s] English:** the one that works generally that you're currently using because that's another trap is in almost  
**Translation:** 

**[1101.28s] English:** every case I've seen when people mixed languages on a project, that's a mistake. I would rather  
**Translation:** 

**[1106.64s] English:** stay just in one language so that everybody can work across the entire thing. And we have,  
**Translation:** 

**[1112.66s] English:** I get meta, we have a lot of projects that use kind of React framework. So you've got JavaScript  
**Translation:** 

**[1117.22s] English:** here and then you have C++ for real work. And then you may have Java interfacing with some other  
**Translation:** Vocabulary: interfacing: 接口连接

**[1123.16s] English:** part of the Android system. And those are all kind of horrible things. And that was one thing that  
**Translation:** 

**[1129.38s] English:** I remember talking with Boz at Facebook about it where like, man, I wish we could have just said,  
**Translation:** 

**[1136.04s] English:** we're only hiring people. We're hiring people. We're hiring people. We're hiring people. We're  
**Translation:** 

**[1136.62s] English:** hiring people. We're hiring people. We're hiring people. We're hiring people. We're hiring people. We're  
**Translation:** 

**[1136.64s] English:** C++ programmers. And he just thought from the Facebook meta perspective, well, we just wouldn't  
**Translation:** 

**[1143.24s] English:** be able to find enough. With the thousands of programmers they've got there, it is not necessarily  
**Translation:** Vocabulary: programmers: 程序员

**[1149.62s] English:** a dying breed, but you can sure find a lot more Java or JavaScript programmers. And I kind of  
**Translation:** 

**[1155.86s] English:** mentioned that to Elon one time, and he was kind of flabbergasted about that. It's like, well, you  
**Translation:** Vocabulary: flabbergasted: 惊诧不已

**[1161.70s] English:** go out and you find those programmers and you don't hire the other programmers that don't do the languages  
**Translation:** 

**[1166.62s] English:** that you want to use. But right now, I guess, yeah, they're using JavaScript on a bunch of the  
**Translation:** 

**[1171.16s] English:** SpaceX work for the UI side of things. When you go find UI programmers, they're JavaScript programmers.  
**Translation:** 

**[1176.62s] English:** I wonder if that's because there's a lot of JavaScript programmers, because I do think  
**Translation:** 

**[1180.98s] English:** that great programmers are rare. If you just look at statistics of how many people are using  
**Translation:** 

**[1190.02s] English:** different programming languages, that doesn't tell you the story of what the great programmers  
**Translation:** 

**[1194.70s] English:** are using. And so you have to...  
**Translation:** 

**[1196.54s] English:** To really look at what you were speaking to, which is the fundamental...  
**Translation:** 

**[1200.00s] English:** of a language what does it encourage how does it encourage you to think what kind of systems does  
**Translation:** 

**[1204.40s] English:** it encourage you to build there is something about c++ that has elements of creativity but forces you  
**Translation:** 

**[1211.94s] English:** to be an adult about your programming which it expects you to be an adult it does not force you  
**Translation:** 

**[1217.94s] English:** to and so it's so it brings out people that are willing to be creative in terms of building large  
**Translation:** 

**[1226.74s] English:** systems and coming up with interesting solutions but at the same time have the sort of the good  
**Translation:** 

**[1232.92s] English:** software engineering practices that amend themselves to real world systems let me ask you  
**Translation:** Vocabulary: amend: 修正

**[1239.70s] English:** about this other language javascript so if we you know aliens visit in in thousands of years and  
**Translation:** 

**[1248.12s] English:** humans are long gone something tells me that most of the systems they find will be running javascript  
**Translation:** 

**[1254.62s] English:** i kind of think that if the  
**Translation:** 

**[1256.44s] English:** if we're living in a simulation it's written in javascript um you know for the longest time  
**Translation:** Vocabulary: simulation: 模拟

**[1263.12s] English:** even still javascript didn't get any respect and yet it runs so much of the world and an increasing  
**Translation:** 

**[1270.58s] English:** number of the world is it possible that all everything will be written in javascript one day  
**Translation:** 

**[1276.28s] English:** so the engineering under javascript is really pretty phenomenal uh the the systems that make  
**Translation:** 

**[1283.16s] English:** javascript run as fast as it does right now  
**Translation:** Vocabulary: phenomenal: 卓越的

**[1286.44s] English:** are kind of miracles of modern engineering in many ways it does feel like it is not an optimal  
**Translation:** 

**[1293.82s] English:** language for all the things that it's being used for or an optimal distribution system to  
**Translation:** Vocabulary: optimal: 最理想的

**[1298.38s] English:** build huge apps in something like this uh without type systems and so on um but i think for a lot  
**Translation:** 

**[1306.80s] English:** of people it does reasonably the necessary things it's still a c flavored language it's still a you  
**Translation:** Vocabulary: flavored: 味道; reasonably: 合理地

**[1313.08s] English:** know a braces and semicolon language uh it's not hard to understand it's still a c flavored language  
**Translation:** 

**[1316.44s] English:** it's hard for people to be trained in javascript and then under  
**Translation:** Vocabulary: braces: 花括号; semicolon: 分号

**[1320.00s] English:** the roots of where it came from. I think garbage collection is unequivocally a good thing for most  
**Translation:** 

**[1327.62s] English:** programs to be written in. It's funny that I still, just this morning, I was on, I was seeing  
**Translation:** Vocabulary: unequivocally: 毫无疑问

**[1332.44s] English:** a Twitter thread of a bunch of really senior game dev people arguing about the virtues and costs of  
**Translation:** 

**[1338.10s] English:** garbage collection. And you will run into some people that are top-notch programmers that just  
**Translation:** Vocabulary: programmers: 程序员

**[1342.02s] English:** say, no, this is literally not a good thing. Oh, because it makes you lazy?  
**Translation:** 

**[1345.64s] English:** Yes, that it makes you not think about things. And I do disagree. I think that  
**Translation:** 

**[1350.36s] English:** there is so much objective data on the vulnerabilities that have happened in C and C++  
**Translation:** 

**[1356.74s] English:** programs, sometimes written by the best programmers in the world. It's like nobody is good enough to  
**Translation:** Vocabulary: vulnerabilities: 漏洞

**[1361.84s] English:** avoid ever shooting themselves in the foot with that. You write enough C code, you're going to  
**Translation:** 

**[1366.10s] English:** shoot yourself in the foot. And garbage collection is a very great thing for the vast majority of  
**Translation:** 

**[1371.14s] English:** programs. It's only when you get into the tightest of real-time things that you start  
**Translation:** 

**[1375.34s] English:** saying, it's like, no, the garbage collection has more costs than it has benefits for me there.  
**Translation:** 

**[1379.96s] English:** But that's not 99 plus percent of all the software in the world. So JavaScript is not  
**Translation:** 

**[1386.58s] English:** terrible in those ways. And so much of programming is not the language itself. It's the infrastructure  
**Translation:** 

**[1395.00s] English:** around everyone that surrounds it, all the libraries that you can get and the different  
**Translation:** 

**[1399.42s] English:** stuff that you can, ways you can deploy it, the portability that it gives you. And JavaScript is  
**Translation:** Vocabulary: deploy: 部署; portability: 便携性; surrounds: 围绕

**[1404.92s] English:** really strong. It's a really strong language. It's a really strong language. It's a really strong  
**Translation:** 

**[1405.32s] English:** on a lot of those things where for a long time, and it still does if I look at it, the web stack  
**Translation:** 

**[1411.98s] English:** about everything that has to go when you do something really trivial in JavaScript and it  
**Translation:** 

**[1416.60s] English:** shows up on a web browser to kind of x-ray through that and see everything that has to happen for  
**Translation:** 

**[1422.52s] English:** your one little JavaScript statement to turn into something visible in your web browser.  
**Translation:** 

**[1428.40s] English:** It's very, very disquieting, just the depth of that stack and the fact that so few people  
**Translation:** 

**[1435.32s] English:** can even comprehend all of the levels that are going on there. But  
**Translation:** 

**[1440.00s] English:** It's again, I have to caution myself to not be the in the good old days old man about it, because clearly there's enormous value here.  
**Translation:** Vocabulary: comprehend: 理解

**[1448.80s] English:** The world does run on JavaScript to a pretty good approximation there, and it's not falling apart.  
**Translation:** 

**[1454.48s] English:** There's a bunch of scary stuff where you look at console logs and you just see all of these bad things that are happening, but it's still kind of limping along and nobody really notices.  
**Translation:** Vocabulary: approximation: 近似

**[1463.72s] English:** But so much of my systems design and systems analysis goes around, you should understand what the speed of light is, like what would be the best you could possibly do here.  
**Translation:** 

**[1475.96s] English:** And it sounds horrible, but in a lot of cases, you can be a thousand times off your speed of light velocity for something and it's still be okay.  
**Translation:** 

**[1485.16s] English:** And in fact, it can even sometimes still be the optimal thing in a larger system standpoint, where there's a lot of things that you don't want to have to.  
**Translation:** 

**[1493.72s] English:** Parachute in someone like me to go in and say, make this, this web page run a thousand times faster, you know, make this web app into a, a hardcore native application that starts up in 37 milliseconds and everything responds in less than one frame latency.  
**Translation:** Vocabulary: hardcore: 极致; latency: 延迟; milliseconds: 毫秒; optimal: 最优; standpoint: 视角

**[1510.94s] English:** That's just not necessary.  
**Translation:** 

**[1512.50s] English:** And if somebody wants to go pay me millions of dollars to do software like that, when they can take somebody right out of a bootcamp and say, spin up an application for this.  
**Translation:** Vocabulary: bootcamp: 培训班

**[1521.64s] English:** I often being efficient.  
**Translation:** 

**[1523.72s] English:** Is not really the best metric that's like there's that applies in a lot of areas where it's kind of interesting how a lot of our appliances and everything are all built around energy efficiency, sometimes at the expense of robustness in some other ways or higher costs in other ways where there's interesting things where energy or electricity could become much cheaper in a future world.  
**Translation:** Vocabulary: robustness: 坚固性

**[1546.94s] English:** And that could change our engineering trade-offs for the way we build certain things where you could throw away efficiency and actually go.  
**Translation:** 

**[1553.72s] English:** Get more benefits that actually matter.  
**Translation:** 

**[1556.24s] English:** I mean, that's one of my, you know, I, one of the directions I was considering.  
**Translation:** 

**[1560.00s] English:** swerving into was nuclear energy when i was kind of like what do i want to do next it was either  
**Translation:** Vocabulary: swerving: 转向

**[1564.98s] English:** going to be a cost-effective nuclear fission or artificial general intelligence and one of the  
**Translation:** 

**[1571.84s] English:** one of my pet ideas there is like you know people don't understand how cheap nuclear fuel is and  
**Translation:** Vocabulary: fission: 裂变

**[1578.78s] English:** there would be ways that i you could be a quarter the efficiency or less but if it wound up making  
**Translation:** 

**[1585.64s] English:** your plant 10 times cheaper that could be a radical innovation and something like that  
**Translation:** 

**[1590.84s] English:** so there's like some of these thoughts around like direct fission energy conversion you know  
**Translation:** 

**[1595.48s] English:** fission fragment conversion that you know maybe you build something that doesn't require all the  
**Translation:** 

**[1599.46s] English:** steam turbines and everything even if it winds up being less efficient so that applies a lot  
**Translation:** 

**[1604.12s] English:** in programming where there's always it's always good to know what you could do if you really sat  
**Translation:** Vocabulary: turbines: 蒸汽涡轮机

**[1610.10s] English:** down and took it uh took it far because sometimes there's discontinuities like around user reaction  
**Translation:** 

**[1615.50s] English:** to the energy conversion and so on and so forth and so on and so forth and so on and so on and so  
**Translation:** Vocabulary: discontinuities: 不连续性

**[1615.62s] English:** there are some points where the difference between operating in one second and 750 milliseconds  
**Translation:** 

**[1621.86s] English:** uh not that huge you'll see it in web page statistics but most of the usability stuff  
**Translation:** Vocabulary: milliseconds: 毫秒; usability: 易用性

**[1627.18s] English:** not that great but if you get down to 50 milliseconds then all of a sudden this just  
**Translation:** 

**[1632.08s] English:** feels amazing you know it's just like doing your bidding instantly rather than you're giving it a  
**Translation:** 

**[1636.84s] English:** command twiddling your thumbs waiting for it to respond so sometimes it's important to really  
**Translation:** 

**[1642.04s] English:** crunch hard to get over some threshold but there are  
**Translation:** Vocabulary: crunch: 绞尽脑汁; threshold: 门槛

**[1645.48s] English:** some points where the difference between operating in one second and 750 milliseconds  
**Translation:** 

**[1645.60s] English:** there are broad basins in the value metric for lots of work where it just doesn't pay to even go  
**Translation:** 

**[1651.68s] English:** that extra mile and there are craftsmen that you know they just don't want to buy that and more  
**Translation:** 

**[1656.90s] English:** power to them you know if somebody just wants to say no i'm going to be i'm my pride is in my work  
**Translation:** 

**[1662.64s] English:** i'm never going to do something that's not as good as i could possibly make it i respect that and  
**Translation:** 

**[1667.90s] English:** sometimes i am that person but i try to focus more on the larger value picture and you do pick your  
**Translation:** 

**[1674.78s] English:** battles and you deploy your resources in the play that's going to give you sort of the best user  
**Translation:** 

**[1679.20s] English:** value in the end  
**Translation:** Vocabulary: deploy: 部署

**[1680.00s] English:** Well, if you look at the evolution of life on Earth as a kind of programming effort, it seems like efficiency isn't the thing that's being optimized for.  
**Translation:** 

**[1695.22s] English:** Like natural selection is very inefficient, but it kind of adapts and through the process of adaptations, building more and more complex systems that are more and more intelligent, the final result is kind of pretty interesting.  
**Translation:** Vocabulary: adaptations: 适应性; inefficient: 低效; optimized: 优化

**[1707.78s] English:** And so I think of JavaScript the same way.  
**Translation:** 

**[1710.94s] English:** It's like this giant mess that things naturally die off if they don't work.  
**Translation:** 

**[1716.56s] English:** And if they become useful to people, they kind of naturally live.  
**Translation:** 

**[1720.96s] English:** And then you build this community, large community of people that are generating code and some code is sticky, some is not.  
**Translation:** 

**[1727.98s] English:** And nobody knows the inefficiencies or the efficiencies or the breaking points, like how reliable this code is.  
**Translation:** 

**[1734.90s] English:** And you kind of just run it, assume it works.  
**Translation:** Vocabulary: efficiencies: 效率; inefficiencies: 低效

**[1737.92s] English:** And then get unpleasantly surprised.  
**Translation:** 

**[1740.48s] English:** And then that's kind of the evolutionary process.  
**Translation:** Vocabulary: evolutionary: 进化; unpleasantly: 不愉快地

**[1743.30s] English:** So that's a really good analogy.  
**Translation:** 

**[1744.96s] English:** And we can go a lot of places with that, where in the earliest days of programming, when you had finite, you could count the bytes that you had to work on this.  
**Translation:** Vocabulary: bytes: 字节; finite: 有限的

**[1753.04s] English:** You had all the kind of hackers playing code golf to be one less instruction than the other person's multiply routine to kind of get through.  
**Translation:** 

**[1760.50s] English:** And it was so perfectly crafted.  
**Translation:** Vocabulary: hackers: 黑客; multiply: 乘法

**[1762.92s] English:** It was a crystal piece of artwork when you had a program.  
**Translation:** 

**[1766.30s] English:** Because there just were not.  
**Translation:** Vocabulary: artwork: 艺术品

**[1767.78s] English:** That meant you couldn't afford to be lazy in different ways.  
**Translation:** 

**[1771.12s] English:** And in many ways, I see that as akin to the symbolic AI work, where, again, if you did not have the resources to just say, well, we're going to do billions and billions of programmable weights here.  
**Translation:** Vocabulary: symbolic: 象征性的

**[1782.56s] English:** You have to turn it down into something that is symbolic and crafted like that.  
**Translation:** 

**[1787.30s] English:** But that's definitely not the way DNA and life and biological evolution and things work.  
**Translation:** 

**[1793.90s] English:** On the one hand, it's almost.  
**Translation:** 

**[1797.78s] English:** It's almost humbling how little programming code is.  
**Translation:** Vocabulary: humbling: 令人谦卑

**[1800.00s] English:** our bodies you know we've got a couple billion base pairs and it's like this all fits on a thumb  
**Translation:** 

**[1803.92s] English:** drive for years now and then our brains are even a smaller section of that you've got maybe 50  
**Translation:** 

**[1809.18s] English:** megabytes and this is not like shannon limit perfectly uh information dense uh conveyances  
**Translation:** 

**[1817.02s] English:** here it's like these are messy codes you know they're broken up into amino acids a lot of them  
**Translation:** Vocabulary: amino: 氨基酸; conveyances: 传输方式; megabytes: 兆字节; shannon: 香农

**[1822.04s] English:** don't do important things or they do things in very awkward ways but it is this process of just  
**Translation:** 

**[1828.30s] English:** accumulation on top of things and you need you need scale both you need scale for sort of the  
**Translation:** Vocabulary: accumulation: 累积

**[1834.98s] English:** population for that to work out and in the early days in the the 50s and 60s the the kind of ancient  
**Translation:** 

**[1841.36s] English:** era of computers where you could count when they said like when the internet started even in the  
**Translation:** 

**[1845.82s] English:** 70s there were like 18 hosts or something on it it was this small finite number and you were still  
**Translation:** 

**[1851.04s] English:** optimizing everything to be as good as you possibly could be but now it's billions and billions of  
**Translation:** Vocabulary: optimizing: 优化

**[1856.90s] English:** devices and  
**Translation:** 

**[1858.30s] English:** everything going on and you can have this very much natural evolution going on where lots of  
**Translation:** 

**[1865.14s] English:** things are tried lots of things are blowing up venture capitalists lose their money i when a  
**Translation:** 

**[1869.96s] English:** startup invested in the wrong tech stack and things completely failed or failed to scale  
**Translation:** 

**[1873.98s] English:** but you know but good things do come out of it and it's interesting to see the the mimetic evolution  
**Translation:** 

**[1880.82s] English:** of the way different things happen like mentioning hello world at the beginning it's funny how some  
**Translation:** Vocabulary: mimetic: 模仿的

**[1885.38s] English:** little thing like that where everybody every programmer  
**Translation:** 

**[1888.30s] English:** knows hello world now and that was a completely arbitrary sort of decision that just came out of  
**Translation:** Vocabulary: arbitrary: 随意; programmer: 程序员

**[1893.20s] English:** the the dominance of unix and c and i early examples of things like that so millions of  
**Translation:** 

**[1900.16s] English:** experiments are going on all the time but some things do kind of rise to the top and win the  
**Translation:** 

**[1905.28s] English:** fitness war for whether it's mind space or programming techniques or anything like there's  
**Translation:** 

**[1910.74s] English:** a site on stack exchange called code golf where people compete to write the shortest possible  
**Translation:** 

**[1917.18s] English:** program for particular things and they're doing it all the time and they're doing it all the time and  
**Translation:** 

**[1918.14s] English:** they're doing it all the time and they're doing it all the time and they're doing it all the time and  
**Translation:** 

**[1918.30s] English:** they're doing it all the time and they're doing it all the time and they're doing it all the time and  
**Translation:** 

**[1920.00s] English:** kinds of languages and it's really interesting to see folks kind of their masters of their craft  
**Translation:** 

**[1929.44s] English:** really play with the limits of programming languages it's really beautiful to see and  
**Translation:** 

**[1934.76s] English:** across all the different programming languages you get to see some of these weird programming  
**Translation:** 

**[1939.94s] English:** languages and mainstream ones python difference between python 2 and 3 you get to see the  
**Translation:** 

**[1945.74s] English:** difference between c and c plus plus and java and you get to see javascript all of that and it's it's  
**Translation:** 

**[1951.28s] English:** kind of um inspiring to see how much depth of possibility there is within programming languages  
**Translation:** 

**[1960.54s] English:** that code golf kind of tasks reveal most of us if you do any kind of programming you kind of do  
**Translation:** 

**[1967.08s] English:** boring kind of very vanilla type of code that's the way to build large systems but it's nice to  
**Translation:** 

**[1973.56s] English:** see that the possibility of creative genius  
**Translation:** Vocabulary: vanilla: 普通类型

**[1975.68s] English:** is still within those languages it's laden within those languages so given that given that you are  
**Translation:** 

**[1982.52s] English:** once again one of the greatest programmers ever uh what do you think makes a good programmer  
**Translation:** Vocabulary: laden: 负载; programmers: 程序员

**[1987.74s] English:** maybe a good modern programmer so i just gave a long rant slash lecture at meta uh to the tpm  
**Translation:** 

**[1996.44s] English:** organization and my my biggest point was everything that we're doing really should flow from user  
**Translation:** 

**[2003.74s] English:** value you know all the good things that we're doing should flow from user value and i think  
**Translation:** 

**[2005.66s] English:** we're doing it's like we're we're not technical people it's like you shouldn't be taking pride  
**Translation:** 

**[2010.88s] English:** just in the specific thing like code golf is the sort of thing it's a fun puzzle game but that  
**Translation:** 

**[2015.20s] English:** really should not be a major motivator for you it's like we're solving problems for people or  
**Translation:** Vocabulary: motivator: 激励因素

**[2020.36s] English:** we're providing entertainment to people we're doing something of value to people that's displacing  
**Translation:** 

**[2024.94s] English:** something else in their life so we want to be providing a net value over what they could be  
**Translation:** Vocabulary: displacing: 替代

**[2030.28s] English:** doing uh but instead they're choosing to use our products and that's where i mean it sounds  
**Translation:** 

**[2035.54s] English:** trite or corny but i fundamentally do think that's how you make the world a better place  
**Translation:** Vocabulary: corny: 陈词滥调; fundamentally: 从根本上; trite: 陈词滥调

**[2040.00s] English:** If you have given more value to people than it took you and your team to create, then the world's a better place. People have gone from something of lesser value, chosen to use your product, and their life feels better for that. And if you've produced that economically, that's a really good thing.  
**Translation:** 

**[2058.28s] English:** On the other hand, if you spent ridiculous amounts of money, you've just kind of shoveled a lot of cash into a wood chipper there, and you should maybe not feel so good about what you're doing.  
**Translation:** Vocabulary: economically: 经济地; shoveled: 投入

**[2069.84s] English:** So being proud about a specific architecture or a specific technology or a specific code sequence that you've done, it's great to get a little smile, like a tiny little dopamine hit for that.  
**Translation:** 

**[2081.04s] English:** But the top-level metric should be that you're building things of value.  
**Translation:** Vocabulary: dopamine: 多巴胺

**[2085.48s] English:** Now, you can get into the argument about how you – you know, what?  
**Translation:** 

**[2088.32s] English:** Is user value?  
**Translation:** 

**[2089.38s] English:** How do you actually quantify that?  
**Translation:** 

**[2091.24s] English:** And there can be big arguments about that, but it's easy to be able to say, okay, this pissed-off user there is not getting value from what you're doing.  
**Translation:** Vocabulary: quantify: 量化

**[2099.08s] English:** This user over there with the big smile on their face, the moment of delight when something happened, there's a value that's happened there.  
**Translation:** 

**[2105.82s] English:** I mean, you have to at least accept that there is a concept of user value.  
**Translation:** 

**[2109.88s] English:** Even if you have trouble exactly quantifying it, you can usually make relative arguments about it.  
**Translation:** 

**[2115.48s] English:** Well, this was better than this.  
**Translation:** Vocabulary: quantifying: 量化

**[2117.10s] English:** We've improved things.  
**Translation:** 

**[2118.28s] English:** So, you know, being a servant to the user is your job when you're a developer.  
**Translation:** 

**[2125.20s] English:** You want to be producing something that other people are going to find valuable.  
**Translation:** 

**[2130.12s] English:** And if you are technically inclined, then finding the right levers to be able to pull, to be able to make a design that's going to produce the most value for the least amount of effort.  
**Translation:** Vocabulary: inclined: 技术导向的

**[2141.36s] English:** And it always has to be kind of – there's a ratio there where you – it's a problem at the big tech companies.  
**Translation:** 

**[2147.92s] English:** You know?  
**Translation:** 

**[2148.08s] English:** Whether it's, you know, MetaGoogle, Apple, Microsoft, Amazon, companies that have almost infinite money.  
**Translation:** 

**[2155.02s] English:** I mean, I know their CFO will complain that it's not infinite money.  
**Translation:** 

**[2158.76s] English:** But for most developers…  
**Translation:** 

**[2160.00s] English:** standpoints, it really does feel like it. And it's almost counterintuitive that if you're working  
**Translation:** Vocabulary: counterintuitive: 逆常理; standpoints: 立场

**[2166.38s] English:** hard as a developer on something, there's always this thought, if only I had more resources,  
**Translation:** 

**[2171.10s] English:** more people, more RAM, more megahertz, then my product will be better. And that sense that  
**Translation:** 

**[2177.40s] English:** at certain points, it's certainly true that if you are really hamstrung by this,  
**Translation:** 

**[2182.16s] English:** removing an obstacle will make a better product, make more value. But if you're not making your  
**Translation:** Vocabulary: hamstrung: 束缚住

**[2188.54s] English:** core design decisions in this fiercely competitive way, where you're saying feature A or feature B,  
**Translation:** 

**[2195.52s] English:** you can't just say, let's do both. Because then you're not making a value judgment about them.  
**Translation:** Vocabulary: fiercely: 激烈地

**[2201.18s] English:** You're just saying, well, they both seem good. I don't want to necessarily have to pick out  
**Translation:** 

**[2204.96s] English:** which one is better or how much better and tell team B that, sorry, we're not going to do this  
**Translation:** 

**[2210.96s] English:** because A is more important. But that notion of always having to really critically value what  
**Translation:** 

**[2217.30s] English:** you're doing, your time, the resources.  
**Translation:** Vocabulary: critically: 仔细地

**[2218.54s] English:** You expend even the opportunity cost of doing something else. That's super important.  
**Translation:** 

**[2224.98s] English:** Well, let me ask you about this, the big debates that you're mentioning of how to measure value.  
**Translation:** Vocabulary: expend: 花费

**[2231.58s] English:** Is it possible to measure it numerically? Or can you do the Johnny Ive, the designer route  
**Translation:** 

**[2243.28s] English:** of imagining somebody using a thing?  
**Translation:** Vocabulary: johnny: 乔伊; numerically: 用数字

**[2248.54s] English:** And imagining a smile on their face, imagining the experience of love and joy that you have when  
**Translation:** 

**[2254.70s] English:** you use the thing. That's from a design perspective. Or if you're building more like a  
**Translation:** 

**[2259.12s] English:** lower level thing for like Linux, you imagine a developer that might come across this and use it  
**Translation:** 

**[2265.36s] English:** and become happy and better off because of it. So where do you land on those things? Is it  
**Translation:** 

**[2272.92s] English:** measurable? So I imagine like Meta and Google will probably try to measure the value of that.  
**Translation:** 

**[2278.54s] English:** They'll try to, it's like,  
**Translation:** Vocabulary: measurable: 可衡量的

**[2280.00s] English:** you try to optimize engagement or something let's measure engagement and then i think there is a  
**Translation:** 

**[2284.62s] English:** kind of i mean i admire the designer ethic of like think of a future that's immeasurable  
**Translation:** Vocabulary: immeasurable: 无法衡量; optimize: 优化

**[2292.32s] English:** and you try to make somebody in that future that's different from today happy so i do usually favor  
**Translation:** 

**[2300.00s] English:** if you can get any kind of a metric that's good by all means listen to the data but you can go  
**Translation:** 

**[2306.42s] English:** too far there where we've had problems where it's like hey we had a performance regression because  
**Translation:** 

**[2310.86s] English:** our fancy new telemetry system is doing a bazillion file rights i had to kind of archive  
**Translation:** Vocabulary: bazillion: 无数; regression: 退步; telemetry: 遥测

**[2316.74s] English:** this stuff because we needed to collect information to determine if we were doing  
**Translation:** 

**[2319.88s] English:** you know if our plans were good so when information is available you should never  
**Translation:** 

**[2326.14s] English:** ignore it i mean all actual users using the thing human beings using the thing large number of human  
**Translation:** 

**[2332.18s] English:** beings and you get to see sort of so there's the zero to one problem of when you're doing  
**Translation:** 

**[2336.40s] English:** something really new you do kind of have to make a guess but one of the points that i've been making  
**Translation:** 

**[2341.38s] English:** at meta is we have more than enough users now that anything somebody wants to try in vr we have  
**Translation:** 

**[2348.94s] English:** users that will be interested in that you do not get to make a completely greenfield blue sky pitch  
**Translation:** 

**[2354.82s] English:** and say i'm going to do this because i think it might be interesting i challenge everyone  
**Translation:** Vocabulary: greenfield: 白手起家

**[2359.78s] English:** there are going to be people whether it's you know working in vr on your i'm like on your desktop  
**Translation:** 

**[2366.40s] English:** or communicating with people in different ways or playing the games there are there are going to be  
**Translation:** 

**[2373.00s] English:** probably millions of people or at least in if you pick some tiny niche that we're not in right now  
**Translation:** 

**[2378.46s] English:** there's still going to be thousands of people out there that have the headsets that would be your  
**Translation:** Vocabulary: headsets: 耳机; niche: 细分市场

**[2383.02s] English:** target market and i tell people pay attention to them don't invent fictional users don't you know  
**Translation:** 

**[2388.22s] English:** make an alice bob charlie uh that fits whatever matrix of uh of tendencies that you want to break  
**Translation:** Vocabulary: fictional: 虚构; matrix: 矩阵

**[2394.42s] English:** the market down to because it's a mistake and it's a mistake and it's a mistake and it's a mistake  
**Translation:** 

**[2396.38s] English:** to think about imaginary users when you've got real users  
**Translation:** 

**[2400.00s] English:** that you could be working with. But on the other hand, there is value to having a kind of wholeness  
**Translation:** 

**[2406.88s] English:** of vision for a product. And companies like Meta, they understand the trade-offs where you can have  
**Translation:** 

**[2415.92s] English:** a company like SpaceX or Apple in the Steve Jobs era, where you have a very powerful leading  
**Translation:** 

**[2422.30s] English:** personality that can micromanage at a very low level and can say, it's like, no, that handle  
**Translation:** Vocabulary: micromanage: 细控细管

**[2428.40s] English:** needs to be different, or that icon needs to change the tint there. And they clearly get a  
**Translation:** 

**[2433.86s] English:** lot of value out of it. They also burn through a lot of employees that have horror stories to tell  
**Translation:** 

**[2438.98s] English:** about working there afterwards. My position is that you're at your best when you've got a leader  
**Translation:** 

**[2446.18s] English:** that is at their limit of what they can kind of comprehend of everything below them,  
**Translation:** 

**[2451.18s] English:** and they can have an informed opinion about everything that's going on.  
**Translation:** 

**[2454.96s] English:** And you take somebody, you've got to believe that somebody that has  
**Translation:** 

**[2458.38s] English:** 30, 40 years of experience, you would hope that they've got wisdom that the just-out-of-bootcamp  
**Translation:** 

**[2464.56s] English:** person contributing doesn't have, and that if they're like, well, that's wrong there,  
**Translation:** 

**[2469.12s] English:** you probably shouldn't do it that way, or even just don't do it that way, do it another way.  
**Translation:** 

**[2474.10s] English:** So there's value there, but it can't go beyond a certain level. I mean, I have Steve Jobs stories  
**Translation:** 

**[2480.28s] English:** of him saying things that are just wrong right in front of me about technical things because  
**Translation:** 

**[2484.36s] English:** he was not operating at that level. I am...  
**Translation:** 

**[2488.38s] English:** But when it does work and you do get that kind of passionate leader that's thinking about the  
**Translation:** 

**[2493.04s] English:** entire product and just really deeply cares about not letting anything slip through the cracks,  
**Translation:** 

**[2498.52s] English:** I think that's got a lot of value. But the other side of that is the people saying that, well,  
**Translation:** 

**[2502.70s] English:** we want to have these independent teams that are bubbling up the ideas because  
**Translation:** Vocabulary: bubbling: 涌现

**[2506.36s] English:** it's almost anti-capitalist or anti-free market to say, it's like, I want my great leader to go  
**Translation:** 

**[2513.52s] English:** ahead and dictate all these points there, where clearly free markets bring up things that you  
**Translation:** 

**[2518.06s] English:** don't expect, like in VR.  
**Translation:** 

**[2520.00s] English:** We saw a bunch of things. It didn't turn out at all the way the early people thought were going to be the key applications, and things that would not have been approved by the dark cabal making the decisions about what gets into the store turned out to, in some cases, be extremely successful.  
**Translation:** 

**[2536.72s] English:** I definitely wanted to be there. There was a point where I did make a pitch. It's like, hey, make me VR dictator, and I'll go in and get shit done. It's not in the culture at Meta. They understand the trade-offs, and that's just not the company that they want, the team that they want to do.  
**Translation:** 

**[2556.78s] English:** It's fascinating because VR, and we'll talk about it more, it's still unclear to me in what way VR will change the world.  
**Translation:** Vocabulary: dictator: 独裁者

**[2566.72s] English:** Because it does seem clear that VR will somehow fundamentally transform this world, and it's unclear to me how yet.  
**Translation:** 

**[2574.80s] English:** Let me know when you want to get into that.  
**Translation:** Vocabulary: fundamentally: 从根本上

**[2576.70s] English:** Well, hold on a second. Let's stick to you being the best programmer ever.  
**Translation:** 

**[2582.48s] English:** Okay, in the early days when you didn't have adult responsibilities of leading teams and all that kind of stuff, and you can focus on just being a programmer, what did the productive day in the life of John Carmack...  
**Translation:** 

**[2596.72s] English:** ...look like? How many hours of the keyboard? How much sleep? What was the source of calories that fueled the brain? What was it like? What time did you wake up?  
**Translation:** 

**[2606.50s] English:** So I was able to be remarkably consistent about what was good working conditions for me for a very long time. I was never one of the programmers that would do all-nighters going through work for 20 hours straight. It's like my brain generally starts turning to mush after 12 hours or so.  
**Translation:** Vocabulary: programmers: 程序员; remarkably: 非常

**[2625.60s] English:** Okay.  
**Translation:** 

**[2626.72s] English:** But the hard work is really important, and I would work for decades. I would work 60 hours a week. I would work a 10-hour day six days a week and try to be productive at that.  
**Translation:** 

**[2638.60s] English:** Now, my schedule shifted.  
**Translation:** 

**[2640.00s] English:** it around a fair amount. When I was young without any kids and any other responsibilities, I was on  
**Translation:** 

**[2645.74s] English:** one of those cycling schedules where I'd kind of get in an hour later each day and roll around  
**Translation:** 

**[2650.44s] English:** through the entire time. And I'd wind up kind of pulling in at two or three in the afternoon  
**Translation:** 

**[2655.42s] English:** sometimes and then working again past midnight or two in the morning. And when it was just me  
**Translation:** 

**[2663.54s] English:** trying to make things happen, and I was usually isolated off in my office, people generally didn't  
**Translation:** Vocabulary: isolated: 单独工作

**[2669.18s] English:** bother me much at in, and I could get a lot of programming work done that way. I did settle into  
**Translation:** 

**[2675.86s] English:** a more normal schedule when I was taking kids to school and things like that. So kids were the  
**Translation:** 

**[2681.20s] English:** forcing function that got you to wake up at the same time. It's not clear to me that there was  
**Translation:** 

**[2686.04s] English:** much of a difference in the productivity with that, where I kind of feel if I just get up when  
**Translation:** 

**[2692.28s] English:** I feel like it, it's usually a little later each day. But I just recently made the focusing decision  
**Translation:** 

**[2698.12s] English:** to try to push my schedule.  
**Translation:** 

**[2699.18s] English:** Back a little bit earlier to getting up at eight in the morning and trying to  
**Translation:** 

**[2703.34s] English:** shift things around. I'm often doing experiments with myself about what should I be doing to be  
**Translation:** 

**[2709.82s] English:** more productive. And one of the things that I did realize was happening in recent months where  
**Translation:** 

**[2715.32s] English:** I would go for a walk or a run. I cover like four miles a day. And I would usually do that  
**Translation:** 

**[2723.20s] English:** just as the sun's going down here in Texas now, and it's still really damn hot. But I'd go out at  
**Translation:** 

**[2728.54s] English:** eight in the morning and try to shift things around. And I would usually do that just as the  
**Translation:** Vocabulary: texas: 德克萨斯州

**[2729.18s] English:** sun's going down here in Texas now, and it's still really damn hot. But I'd go out at eight in the  
**Translation:** 

**[2729.24s] English:** morning and try to shift things around. And I would usually do that just as the sun's going down here  
**Translation:** 

**[2729.28s] English:** or something and cover the time there and then the showering. And it was putting a hole in my day  
**Translation:** 

**[2734.52s] English:** where I would have still a couple hours after that. And sometimes my best hours were at night  
**Translation:** 

**[2739.40s] English:** when nobody else is around, nobody's bothering me. But that hole in the day was a problem. So  
**Translation:** 

**[2744.34s] English:** just a couple weeks ago, I made the change to go ahead and say, all right, I'm going to get up a  
**Translation:** 

**[2748.94s] English:** little earlier. I'm going to do a walk or get out there first so I can have more uninterrupted time.  
**Translation:** 

**[2753.66s] English:** So I'm still playing with factors like this as I kind of optimize my  
**Translation:** Vocabulary: optimize: 优化; uninterrupted: 不间断

**[2757.90s] English:** work after that.  
**Translation:** 

**[2759.18s] English:** So I'm still playing with factors like this as I kind of optimize my work after that. So  
**Translation:** 

**[2760.00s] English:** But it's always been, you know, it was 60 hours a week for a very long time.  
**Translation:** 

**[2765.02s] English:** To some degree, I had a little thing in the back of my head where I was almost jealous  
**Translation:** 

**[2768.24s] English:** of some of the programmers that would do these marathon sessions.  
**Translation:** 

**[2771.58s] English:** And I had like Dave Taylor, one of the guys that he had, he would be one of those people  
**Translation:** 

**[2775.14s] English:** that would fall asleep under his desk sometimes and all the kind of classic hacker tropes  
**Translation:** 

**[2779.44s] English:** about things.  
**Translation:** Vocabulary: hacker: 黑客; tropes: 套路

**[2780.08s] English:** And a part of me was like always a little bothered that that wasn't me, that I wouldn't  
**Translation:** 

**[2784.70s] English:** go program 20 hours straight because I'm just, I'm falling apart and not being very  
**Translation:** Vocabulary: bothered: 烦恼

**[2789.74s] English:** effective after 12 hours.  
**Translation:** 

**[2791.90s] English:** I mean, yeah, 12 hour programming, that's fine when you're doing that, but it never,  
**Translation:** 

**[2796.42s] English:** you're not doing smart work much after, at least I'm not, but there's a range of people.  
**Translation:** 

**[2801.04s] English:** I mean, that's something that a lot of people don't really get in their gut where there  
**Translation:** 

**[2804.72s] English:** are people that work on four hours of sleep and are smart and can continue to do good  
**Translation:** 

**[2809.08s] English:** work.  
**Translation:** 

**[2809.52s] English:** But then there's a lot of people that just fall apart.  
**Translation:** 

**[2812.22s] English:** So I do tell people that I.  
**Translation:** 

**[2814.70s] English:** Always try to get eight hours of sleep.  
**Translation:** 

**[2816.42s] English:** It's not this, you know, push yourself harder, get up earlier.  
**Translation:** 

**[2819.66s] English:** I just do worse work where, you know, there's, you can work a hundred hours a week and still  
**Translation:** 

**[2824.96s] English:** get eight hours of sleep if you just kind of prioritize things correctly.  
**Translation:** 

**[2828.78s] English:** But I do believe in working hard, working a lot.  
**Translation:** 

**[2832.06s] English:** I, there was a comment that a game dev made that, that I know there's a backlash against  
**Translation:** Vocabulary: backlash: 逆反情绪

**[2838.22s] English:** really hard work in a lot of cases.  
**Translation:** 

**[2840.28s] English:** And I get into online arguments about this all the time, but it was basically.  
**Translation:** 

**[2844.70s] English:** Saying, yeah, 40 hours a week, that's kind of a part-time job.  
**Translation:** 

**[2847.82s] English:** And if you were really in it, you're doing what you think is important, what you're  
**Translation:** 

**[2852.10s] English:** passionate about working more gets more done.  
**Translation:** 

**[2855.42s] English:** And I, it's just really not possible to argue with that.  
**Translation:** 

**[2859.72s] English:** If you've been around the people that, that work with that level of intensity and just  
**Translation:** 

**[2863.48s] English:** say, it's like, no, they should just stop.  
**Translation:** 

**[2866.04s] English:** And we had, I kind of came back around to that a couple of years ago where I was using  
**Translation:** 

**[2871.70s] English:** the fictional example of, all right.  
**Translation:** Vocabulary: fictional: 虚构的

**[2874.42s] English:** Some people say, they'll say with a straight face, they think, no, you, you are less productive  
**Translation:** 

**[2878.82s] English:** if you work more than 40.  
**Translation:** 

**[2880.00s] English:** hours a week and they're generally misinterpreting things where your your marginal productivity for  
**Translation:** 

**[2885.36s] English:** an hour after eight hours is less than in one of your peak hours but you're not literally getting  
**Translation:** Vocabulary: marginal: 边际的; misinterpreting: 误解

**[2890.40s] English:** less done there is a point where you start breaking things and getting worse worse behavior  
**Translation:** 

**[2895.44s] English:** and everything out of it where you're literally going backwards but it's not at eight or ten or  
**Translation:** Vocabulary: backwards: 倒退

**[2900.16s] English:** twelve hours and the fictional example i would use was imagine there's an asteroid coming to  
**Translation:** 

**[2906.08s] English:** impact you know to to crash into earth destroy all of human life i do you want elon musk or the  
**Translation:** 

**[2913.04s] English:** people working at spacex that are building the interceptor that's going to uh to deflect the  
**Translation:** 

**[2917.64s] English:** asteroid do you want them to clock out at five because damn it they're just going to go do worse  
**Translation:** Vocabulary: asteroid: 小行星; deflect: 偏转; interceptor: 拦截器

**[2922.46s] English:** work if they work another couple hours and you know it seems absurd and that's a hypothetical  
**Translation:** 

**[2928.30s] English:** though and everyone can dismiss that but then when coronavirus was hitting and you have all of these  
**Translation:** Vocabulary: coronavirus: 冠状病毒; hypothetical: 假设的

**[2933.74s] English:** medical personnel that are clearly pushing  
**Translation:** 

**[2936.08s] English:** themselves really really hard and i'd say it's like okay do you want all of these scientists  
**Translation:** 

**[2941.82s] English:** working on treatments and vaccines and caring for all of these people are they really screwing  
**Translation:** 

**[2947.00s] English:** everything up by working more than eight hours a day and of course people say i'm just an asshole  
**Translation:** Vocabulary: asshole: 混蛋; screwing: 搞砸; vaccines: 疫苗

**[2951.50s] English:** to say something like that but it's i you know it's the truth working longer gets more done  
**Translation:** 

**[2957.34s] English:** well so that's kind of uh the layer one but i'd like to also say that at least i believe depending  
**Translation:** 

**[2965.34s] English:** on the person  
**Translation:** 

**[2966.08s] English:** on the task working more and harder will make you better for the for the next week  
**Translation:** 

**[2975.58s] English:** in those peak hours so there's something about a deep dedication to a thing  
**Translation:** 

**[2981.24s] English:** that kind of gets deep in you so it's the the hard work isn't just about the raw hours of  
**Translation:** Vocabulary: dedication: 奉献精神

**[2988.32s] English:** productivity it's the it's the thing it does to you in the in the weeks and months after  
**Translation:** 

**[2996.08s] English:** too you're tempering yourself in some ways and i think  
**Translation:** Vocabulary: tempering: 磨炼

**[3000.00s] English:** You know, it's like Jiro dreams of sushi.  
**Translation:** 

**[3001.80s] English:** If you really dedicate yourself completely to making the sushi, like to really putting in the long hours, day after day after day, you become a true craftsman of the thing you're doing.  
**Translation:** Vocabulary: craftsman: 手工艺人; sushi: 寿司

**[3014.32s] English:** Now, there's, of course, discussions about are you sacrificing a lot of personal relationships?  
**Translation:** 

**[3018.90s] English:** Are you sacrificing a lot of other possible things you could do with that time?  
**Translation:** Vocabulary: sacrificing: 牺牲

**[3022.70s] English:** But if you're talking about purely being a master or a craftsman of your art, that more hours isn't just about doing more.  
**Translation:** 

**[3034.72s] English:** It's about becoming better at the thing you're doing.  
**Translation:** 

**[3037.30s] English:** Yeah, and I don't gainsay anybody that wants to work the minimum amount.  
**Translation:** 

**[3041.14s] English:** They've got other priorities in their life.  
**Translation:** Vocabulary: priorities: 优先事项

**[3042.86s] English:** My only argument that I'm making, it's not that everybody should work hard.  
**Translation:** 

**[3046.96s] English:** It's that if you want to accomplish something, working longer and harder is the path to getting it accomplished.  
**Translation:** 

**[3052.70s] English:** Well, let me ask you about this then, the mythical work-life balance.  
**Translation:** 

**[3060.62s] English:** For an engineer, it seems like that's one of the professions for a programmer where working hard does lead to greater productivity in it.  
**Translation:** Vocabulary: mythical: 神话般的; programmer: 程序员

**[3073.32s] English:** But it also raises the question of sort of personal relationships and all that kind of stuff, family.  
**Translation:** 

**[3081.56s] English:** How are you able?  
**Translation:** 

**[3082.70s] English:** How are you able to find work-life balance?  
**Translation:** 

**[3084.32s] English:** Is there advice you can give, maybe even outside of yourself?  
**Translation:** 

**[3087.60s] English:** Have you been able to arrive at any wisdom on this part in your years of life?  
**Translation:** 

**[3092.34s] English:** I do think that there's a wide range of people where different people have different needs.  
**Translation:** 

**[3096.78s] English:** It's not a one-size-fits-all.  
**Translation:** 

**[3098.78s] English:** I am certainly what works for me.  
**Translation:** 

**[3100.68s] English:** I can tell enough that I'm different than a typical average person in the way things impact me, the things that I want to do.  
**Translation:** 

**[3110.30s] English:** My goals are different.  
**Translation:** 

**[3111.88s] English:** And sort of those.  
**Translation:** 

**[3112.70s] English:** The levers to impact things are different where, you know, I have literally never felt burnout.  
**Translation:** Vocabulary: burnout: 职业倦怠

**[3119.72s] English:** And I know.  
**Translation:** 

**[3120.00s] English:** there's lots of brilliant, smart people that do world-leading work that get burned out,  
**Translation:** 

**[3125.28s] English:** and it's never hit me. I've never been at a point where I'm like, I just don't care about this. I  
**Translation:** 

**[3133.26s] English:** don't want to do this anymore. But I've always had the flexibility to work on lots of interesting  
**Translation:** 

**[3138.12s] English:** things. I can always just turn my gaze to something else and have a great time working on  
**Translation:** 

**[3143.00s] English:** that. And so much of the ability to actually work hard is the ability to have multiple things to  
**Translation:** 

**[3149.08s] English:** choose from and to use your time on the most appropriate thing. There are time periods where  
**Translation:** 

**[3155.36s] English:** it's the best time for me to read a new research paper that I need to really be thinking hard about  
**Translation:** 

**[3160.92s] English:** it. Then there's a time that maybe I should just scan and organize my old notes because I'm just  
**Translation:** 

**[3166.02s] English:** not on top of things. Then there's the time that, all right, let's go bang out a few hundred lines  
**Translation:** 

**[3171.00s] English:** of code for something. So switching between them has been real valuable.  
**Translation:** 

**[3177.24s] English:** So you'll always have kind of joy in your  
**Translation:** 

**[3179.04s] English:** heart.  
**Translation:** 

**[3179.08s] English:** For all the things you're doing. And that is the kind of work-life balance as a first sort of step.  
**Translation:** 

**[3184.78s] English:** Yeah, I do.  
**Translation:** 

**[3185.16s] English:** So you're always happy.  
**Translation:** 

**[3186.34s] English:** I do.  
**Translation:** 

**[3187.28s] English:** Well, happy.  
**Translation:** 

**[3188.46s] English:** Yeah. I mean, that's like, a lot of people would say that often I look like kind of a grim person,  
**Translation:** 

**[3192.56s] English:** you know, with just sitting there with a neutral expression or even like knitted brows and a frown  
**Translation:** Vocabulary: brows: 眉毛; frown: 皱眉

**[3196.82s] English:** on my face as I'm staring at something.  
**Translation:** 

**[3198.94s] English:** That's what happiness looks like for you.  
**Translation:** 

**[3200.70s] English:** Yeah. It's kind of true where that it's like, okay, I'm pushing through this. I'm making  
**Translation:** 

**[3205.80s] English:** progress here. I am, you know, we, I know that it's going to be a lot of work, but I'm going to  
**Translation:** 

**[3209.04s] English:** work for everyone. I know it doesn't work for most people. I am. But what I am always trying to  
**Translation:** 

**[3214.48s] English:** do in those cases is I don't want to let somebody that might be a person like that be told by  
**Translation:** 

**[3219.76s] English:** someone else that no, don't try it. Don't even try that out as an option where I, you know,  
**Translation:** 

**[3225.64s] English:** work-life balance versus kind of your life's work, where there's a small subset of the people that  
**Translation:** 

**[3231.88s] English:** can be very happy being obsessive about things. And, you know, obsession can often get things  
**Translation:** 

**[3238.54s] English:** done that you don't want to do. And I think that's a really good point. I think that's a good point.  
**Translation:** Vocabulary: obsession: 痴迷; obsessive: 执着

**[3239.02s] English:** Just practice.  
**Translation:** 

**[3240.00s] English:** prudent pedestrian work won't or at least won't for a very long time there's legends of uh your  
**Translation:** Vocabulary: pedestrian: 普通行人; prudent: 谨慎

**[3247.72s] English:** nutritional intake uh in the early days uh what can you say about sort of as a you know being a  
**Translation:** 

**[3256.12s] English:** as a kind of athlete so what what was uh the nutrition that fueled i have never been that  
**Translation:** Vocabulary: intake: 摄入; nutritional: 营养的

**[3262.72s] English:** great on i on really paying attention to it where i'm good enough that i don't eat a lot you know  
**Translation:** 

**[3269.56s] English:** i've never been like a big heavy guy but uh it was interesting where one of the things that i can  
**Translation:** 

**[3274.58s] English:** remember being an unhappy teenager not having enough money and like one of the things that  
**Translation:** 

**[3279.50s] English:** bothered me about not having enough money is i couldn't buy pizza whenever i wanted to  
**Translation:** Vocabulary: bothered: 烦扰

**[3283.22s] English:** so i got rich and then i bought a whole lot of pizza that was defining like that's what being  
**Translation:** 

**[3289.00s] English:** rich felt like a lot of little things like i could buy all the pizza and comic books and video games  
**Translation:** 

**[3293.98s] English:** that uh that i wanted to and it really didn't take that much but uh the  
**Translation:** 

**[3299.56s] English:** pizza was one of those things and it's absolutely true that for a long time it did software i had a  
**Translation:** 

**[3304.80s] English:** pizza delivered every single day you know the delivery guy knew me my name and i didn't find  
**Translation:** 

**[3309.96s] English:** out until years later that apparently i was such a good customer that they just never raised the  
**Translation:** 

**[3315.18s] English:** price on me and i was using this six-year-old price for the pizzas that they were still kind  
**Translation:** 

**[3319.68s] English:** of sending my way every day so you were doing um eating once a day or or were you uh it would be  
**Translation:** 

**[3326.28s] English:** spread out you know you have a few pieces of pizza you have some more later on and  
**Translation:** 

**[3329.56s] English:** i'd maybe have something at home i it was one of the nice things that facebook meta is they do  
**Translation:** 

**[3335.40s] English:** they feed you quite well you get a different i guess now it's doordash sorts of things delivered  
**Translation:** 

**[3340.42s] English:** but uh they take care of making sure that everybody does get well fed and i probably had  
**Translation:** Vocabulary: doordash: 送餐服务

**[3345.04s] English:** better food those six years that i was working in the meta office there than i used to before  
**Translation:** 

**[3351.04s] English:** but i it's worked out okay for me my health has always been good i i get a pretty good amount of  
**Translation:** 

**[3356.66s] English:** exercise and and i don't eat to exercise and i don't eat to exercise and i don't eat to exercise  
**Translation:** 

**[3359.56s] English:** and  
**Translation:** 

**[3360.00s] English:** I avoid a lot of other kind of not-so-good-for-you things.  
**Translation:** 

**[3363.64s] English:** So I'm still doing quite well at my age.  
**Translation:** 

**[3365.80s] English:** Did you have a kind of, I don't know, spiritual experience with food or coffee or any of that kind of stuff?  
**Translation:** 

**[3375.10s] English:** I mean, you know, the programming experience, you know, with music or like I listen to Brown Noise on a program  
**Translation:** 

**[3381.86s] English:** or like creating an environment and the things you take into your body,  
**Translation:** 

**[3386.04s] English:** just everything you construct can become a kind of ritual that empowers the whole process of the program.  
**Translation:** Vocabulary: empowers: 赋予力量

**[3392.16s] English:** Did you have that relationship with pizza?  
**Translation:** 

**[3394.28s] English:** It would really be with Diet Coke.  
**Translation:** 

**[3395.98s] English:** I mean, there still is that sense of, you know, drop the can down, crack open the can of Diet Coke.  
**Translation:** 

**[3400.46s] English:** All right, now I mean business.  
**Translation:** 

**[3401.90s] English:** We're getting to work here.  
**Translation:** 

**[3404.00s] English:** Still, to this day, Diet Coke is still a part of it.  
**Translation:** 

**[3406.84s] English:** Yeah, probably eight or nine a day.  
**Translation:** 

**[3409.44s] English:** Nice.  
**Translation:** 

**[3410.06s] English:** Okay, what about your setup?  
**Translation:** 

**[3412.04s] English:** How many screens?  
**Translation:** Vocabulary: setup: 设备配置

**[3413.96s] English:** What kind of keyboard?  
**Translation:** 

**[3414.90s] English:** Is there something interesting?  
**Translation:** 

**[3416.14s] English:** What kind of IDE, Emacs, Vim or something modern?  
**Translation:** 

**[3421.86s] English:** Linux, what operating system, laptop or any interesting thing that brings you joy?  
**Translation:** Vocabulary: emacs: 编辑器

**[3427.08s] English:** So I kind of migrated cultures where early on through all of game dev, there was sort of one culture there,  
**Translation:** 

**[3432.98s] English:** which was really quite distinct from the more the Silicon Valley venture, you know, culture for things.  
**Translation:** Vocabulary: migrated: 迁移

**[3439.04s] English:** It's they're different groups and they have pretty different mores and the way they think about things where  
**Translation:** 

**[3444.22s] English:** and I still do think a lot of the big companies,  
**Translation:** 

**[3446.12s] English:** companies can learn, can learn things from the hardcore game development side of things where it still boggles my mind how I am, how hostile to debuggers and IDEs that so much of them, the kind of big money, get billions of dollars, Silicon Valley, venture backed funds are.  
**Translation:** 

**[3464.46s] English:** Oh, that's interesting.  
**Translation:** Vocabulary: boggles: 难以置信; hardcore: 核心的; hostile: 敌对的

**[3465.12s] English:** Sorry.  
**Translation:** 

**[3465.40s] English:** So you're saying like, like big companies like Google and Meta are hostile to.  
**Translation:** 

**[3469.92s] English:** They are not big on debuggers and IDEs like so much of it is like Emacs, Vim for things.  
**Translation:** 

**[3475.60s] English:** And we just assume that debuggers don't work most of the time.  
**Translation:** 

**[3480.00s] English:** for the systems. And a lot of this comes from a sort of Linux bias on a lot of things where  
**Translation:** 

**[3485.04s] English:** I did come up through the personal computers and then the DOS and then Windows. And it was  
**Translation:** 

**[3492.72s] English:** Borland tools and then Visual Studio. Do you appreciate debuggers?  
**Translation:** 

**[3498.46s] English:** Very much so. I mean, a debugger is how you get a view into a system that's too complicated to  
**Translation:** 

**[3503.12s] English:** understand. I mean, anybody that thinks just read the code and think about it, that's an insane  
**Translation:** 

**[3507.60s] English:** statement. You can't even read all the code on a big system. You have to do experiments on the  
**Translation:** 

**[3513.24s] English:** system. And doing that by adding log statements, recompiling and rerunning it is an incredibly  
**Translation:** 

**[3519.80s] English:** inefficient way of doing it. I mean, yes, you can always get things done, even if you're working  
**Translation:** Vocabulary: inefficient: 低效; recompiling: 重新编译

**[3524.20s] English:** with stone knives and bearskins. That is the mark of a good programmer is that given any tools,  
**Translation:** 

**[3530.34s] English:** you will figure out a way to get it done. But it's amazing what you can do with sometimes much,  
**Translation:** Vocabulary: bearskins: 熊皮; programmer: 程序员

**[3535.94s] English:** much better tools where...  
**Translation:** 

**[3537.60s] English:** Instead of just going through this iterative compile run debug cycle, you have the old Lisp  
**Translation:** Vocabulary: iterative: 迭代的

**[3544.22s] English:** direction of like, you've got a REPL and you're working interactively and doing amazing things  
**Translation:** 

**[3548.04s] English:** there. But in many cases, a debugger has a very powerful user interface that can stop, examine all  
**Translation:** Vocabulary: interface: 用户界面

**[3554.00s] English:** the different things in your program, set all of these different breakpoints. And of course,  
**Translation:** 

**[3557.30s] English:** you can do that with GDB or whatever there. But this is one of the user interface fundamental  
**Translation:** Vocabulary: breakpoints: 断点设置

**[3563.22s] English:** principles where when something is complicated to do, you won't use it.  
**Translation:** 

**[3567.60s] English:** Yeah. And I think that's a really good point. And I think that's a really good point. And I think  
**Translation:** 

**[3568.04s] English:** that's a really good point. And I think that's a really good point. And I think that's a really good  
**Translation:** 

**[3568.28s] English:** point. There's people that will break out GDB when they're at their wits end and they just have beat  
**Translation:** 

**[3572.92s] English:** their head against a problem for so long. But for somebody that kind of grew up in game dev,  
**Translation:** 

**[3577.88s] English:** it's like they were running into the debugger anyways before they even knew there was a problem.  
**Translation:** 

**[3582.28s] English:** And you would just stop and see what was happening. And sometimes you could fix things  
**Translation:** 

**[3586.10s] English:** even before you did one compile cycle. You could be in the debugger and you'd say,  
**Translation:** 

**[3592.24s] English:** well, I'm just going to change this right here. And yep, that did the job and fix it and go on.  
**Translation:** 

**[3597.00s] English:** Yeah.  
**Translation:** 

**[3597.60s] English:** I don't know. GDB is sort of popular.  
**Translation:** 

**[3600.00s] English:** i guess linux debugger uh primarily for c++ they they handle most of the languages but it's you  
**Translation:** 

**[3607.22s] English:** know it's based on c as the the original kind of unix heritage and it's kind of like command line  
**Translation:** 

**[3611.72s] English:** it's not user-friendly it's not it doesn't allow for clean visualizations and you're you're exactly  
**Translation:** Vocabulary: visualizations: 可视化

**[3616.76s] English:** right so that you're using this kind of debugger usually when you're at what's end and there's a  
**Translation:** 

**[3621.68s] English:** problem that you can't figure out why by just looking at the codes you have to find it that's  
**Translation:** 

**[3626.22s] English:** how i guess normal programmers use it but you're saying there should be tools that kind of  
**Translation:** 

**[3630.80s] English:** visualize and help you as part of the programming process just a normal programming process to  
**Translation:** Vocabulary: programmers: 程序员; visualize: 可视化

**[3637.64s] English:** understand the code deeper yeah when i'm working on like my c c++ code i'm always running it from  
**Translation:** 

**[3644.52s] English:** the debugger you know just i type in the code i i run it many times the first thing i do after  
**Translation:** 

**[3649.44s] English:** writing code is set a breakpoint and step through the function now other people will say it's like  
**Translation:** 

**[3654.14s] English:** i do that in my head well  
**Translation:** Vocabulary: breakpoint: 断点

**[3655.80s] English:** you're  
**Translation:** 

**[3656.20s] English:** head is a faulty interpreter of all those things there and i've written brand new code i want to  
**Translation:** Vocabulary: interpreter: 解释器

**[3661.46s] English:** step in there and i'm going to single step through that examine lots of things and see if it's  
**Translation:** 

**[3665.34s] English:** actually doing what i expected it to it is a kind of companion the debugger like you're you're now  
**Translation:** 

**[3673.42s] English:** coding in an interactive way with another being uh the debugger is a kind of dumb being but it's  
**Translation:** 

**[3679.70s] English:** a reliable being that is an interesting question of what role does ai play in that kind of um  
**Translation:** Vocabulary: interactive: 交互式

**[3685.74s] English:** with  
**Translation:** 

**[3686.20s] English:** codex and these kind of ability to generate code that might be you might start having tools that  
**Translation:** Vocabulary: codex: 法典

**[3692.24s] English:** understand the code in interesting deep ways that can work with you i mean there's there's a whole  
**Translation:** 

**[3698.22s] English:** spectrum there from uh static code analyzers and various kind of dynamic tools there up to  
**Translation:** Vocabulary: analyzers: 静态分析器

**[3703.92s] English:** ai that can conceivably grok these programs that no he literally no human can understand they're  
**Translation:** 

**[3709.26s] English:** they're too big too intertwined and too interconnected but it's not beyond the  
**Translation:** Vocabulary: conceivably: 可以想象; interconnected: 相互连接; intertwined: 交织在一起

**[3713.20s] English:** possibility of understanding it's just beyond the possibility of understanding it's just beyond the  
**Translation:** 

**[3716.20s] English:** possibility of understanding it's just beyond what we can hold in our heads as kind of mutable  
**Translation:** 

**[3718.68s] English:** state while we're working on  
**Translation:** 

**[3720.00s] English:** things and and i'm a big proponent again of things like static analyzers and some of that stuff where  
**Translation:** Vocabulary: proponent: 支持者

**[3726.44s] English:** you'll find some people that don't like being scolded by a program for how they've written  
**Translation:** 

**[3732.08s] English:** something where it's like oh i know better and sometimes you do but that was something that  
**Translation:** 

**[3736.72s] English:** i was it was very very valuable for me when and not too many people get an opportunity like this  
**Translation:** 

**[3743.60s] English:** to have this is almost one of those spiritual experiences as a programmer and awakening to  
**Translation:** Vocabulary: awakening: 觉醒; programmer: 程序员

**[3747.84s] English:** i'm the id software code bases were a couple million lines of code and at one point i had  
**Translation:** 

**[3754.12s] English:** used a few of the different analysis tools but i made a point to really go through and scrub the  
**Translation:** Vocabulary: scrub: 仔细检查

**[3760.42s] English:** code base using every tool that i could find and it was eye-opening where we had a reputation for  
**Translation:** 

**[3765.78s] English:** having some of the the most robust strongest code you know where there were some you know great  
**Translation:** Vocabulary: robust: 强壮的

**[3770.34s] English:** things that i remember hearing from like microsoft telling us about crashes on xbox and we had this  
**Translation:** 

**[3775.62s] English:** tiny number that they said were were probably  
**Translation:** 

**[3777.84s] English:** literally hardware errors and then you have other significant titles that just have millions of  
**Translation:** 

**[3783.04s] English:** faults that are getting recorded all the time so i was proud of our code on a lot of levels but when  
**Translation:** 

**[3788.02s] English:** i took this code analysis squeegee through everything it was it was shocking how many  
**Translation:** 

**[3794.98s] English:** errors there were in there things that you can say okay this was this was a copy paste not changing  
**Translation:** Vocabulary: squeegee: 刮水器

**[3800.34s] English:** something right here lots of things that were you know the most the most common problem was  
**Translation:** 

**[3805.52s] English:** something in a printf format string  
**Translation:** 

**[3807.84s] English:** was the wrong data type that could cause crashes there and you know you really want the warnings  
**Translation:** 

**[3812.32s] English:** for things like that then the next most common was missing a check for null that could actually  
**Translation:** 

**[3816.86s] English:** happen that could blow things up and those are obviously like top c c plus plus things everybody  
**Translation:** 

**[3821.90s] English:** has those problems but the long tail of all of the different little things that could go wrong there  
**Translation:** 

**[3827.32s] English:** and we had good programmers and my own code stuff that i'd be looking at it's like oh i wrote that  
**Translation:** 

**[3832.06s] English:** code that's definitely wrong we've been using this for a year and it's this  
**Translation:** 

**[3837.84s] English:** submarine you know this mine sitting there waiting  
**Translation:** 

**[3840.00s] English:** for us to step on. And it was humbling. And I reached the conclusion that anything that can  
**Translation:** Vocabulary: humbling: 令人谦卑

**[3847.82s] English:** be syntactically allowed in your language, it's going to show up eventually in a large enough  
**Translation:** 

**[3854.00s] English:** code base. Good intentions aren't going to keep it from happening. You need automated tools and  
**Translation:** Vocabulary: automated: 自动化; syntactically: 语法上

**[3860.58s] English:** guardrails for things. And those start with things like static types or even type hints in the more  
**Translation:** 

**[3865.86s] English:** dynamic languages. But the people that rebel against that, that basically say, that slows me  
**Translation:** Vocabulary: guardrails: 防护栏

**[3872.60s] English:** down doing that. There's something to that. I get that. I've written, you know, I've cobbled things  
**Translation:** 

**[3876.94s] English:** together in a notebook. I am like, wow, this is great that it just happened. But yeah, that's  
**Translation:** Vocabulary: cobbled: 拼凑

**[3881.84s] English:** kind of sketchy, but it's working fine. I don't care. It does come back to that, that value analysis  
**Translation:** 

**[3886.92s] English:** where sometimes it's right to not care. But when you do care, if it's going to be something that's  
**Translation:** 

**[3892.68s] English:** going to live for years, and it's going to have other people working on it,  
**Translation:** 

**[3895.86s] English:** and it's going to be deployed to millions of people, then you want to use all of these tools.  
**Translation:** Vocabulary: deployed: 部署

**[3901.08s] English:** You want to be told, it's like, no, you've screwed up here, here, and here. And that does require  
**Translation:** 

**[3905.52s] English:** kind of an ego check about things, where you have to be open to the fact that everything that you're  
**Translation:** 

**[3911.96s] English:** doing is just littered with flaws. It's not that, oh, you occasionally have a bad day. It's just  
**Translation:** 

**[3916.94s] English:** whatever stream of code you output, there is going to be a statistical regularity of things that you  
**Translation:** Vocabulary: littered: 满是

**[3922.00s] English:** just make mistakes on. And I do  
**Translation:** 

**[3925.84s] English:** think there's the whole argument about test-driven design and unit testing versus  
**Translation:** 

**[3930.32s] English:** kind of analysis and different things. I am more in favor of the analysis and the stuff that just  
**Translation:** 

**[3936.24s] English:** like you can't run your program until you fix this, rather than you can run it and hopefully  
**Translation:** 

**[3940.76s] English:** a unit test will catch it in some way. Yeah. In my private code, I have asserts everywhere.  
**Translation:** 

**[3946.64s] English:** Yeah. It just, there's something  
**Translation:** 

**[3949.18s] English:** pleasant to me, pleasurable to me about sort of the dictatorial rule of like,  
**Translation:** 

**[3955.18s] English:** this should be the way to do it.  
**Translation:** Vocabulary: dictatorial: 专制的; pleasurable: 令人愉快的

**[3955.84s] English:** This should be true at this point. And too many times.  
**Translation:** 

**[3960.00s] English:** And I've made mistakes that shouldn't have been made. And I would assume I wouldn't be the kind of person that would make that mistake, but I keep making that mistake. Therefore, an assert really catches me, really helps all the time. So I would say like 10 to 20% of my private code just for personal use is probably asserts.  
**Translation:** 

**[3981.28s] English:** And they're active comments. And it's one of those things that in theory, they don't make any difference to the program. And if it was all operating the way you expected it would be, then they will never fire. But even if you have it right, and you wrote the code right initially, then circumstances change. The world outside your program changes.  
**Translation:** 

**[4000.60s] English:** And in fact, that's one of the things where I'm kind of fond in a lot of cases of static array size declarations, where I went through this period where it's like, okay, now we have general collection.  
**Translation:** Vocabulary: declarations: 声明

**[4011.28s] English:** Classes, we should just make everything variable. I because I had this history of in the early days, you get doom, which had some fixed limits on it, then everybody started making crazier and crazier things. And they kept bumping up the different limits, this many lines, this many sectors. And it seemed like a good idea. Well, we should just make this completely generic, it can go kind of go up to whatever. And there's cases where that's the right thing to do. But it also the other aspect of the world changing around you is  
**Translation:** 

**[4041.28s] English:** it's good to be informed when the world has changed more than you thought it would. And if you've got a continuously growing collection, you're never going to find out you might have this quadratic slowdown on something where you thought, oh, I'm only ever going to have a handful of these. But something changes, and there's a new design style. And all of a sudden, you've got 10,000 of them. So I kind of like in many cases, picking a number, some, you know, nice round power of two number, and setting it up in there and having an assert saying it's like, hey, you hit the you hit the  
**Translation:** Vocabulary: quadratic: 二次的; slowdown: 减速

**[4071.28s] English:** limit, you should probably think are the choices that you've made around all of this still relevant? If somebody is using 10 times more than you thought they  
**Translation:** 

**[4080.00s] English:** would yeah this code was originally written with this kind of world view with this kind of set of  
**Translation:** 

**[4085.44s] English:** constraints you were you were you were thinking of the world in this way if something breaks that  
**Translation:** 

**[4090.62s] English:** means you got to rethink the initial stuff and that's it's nice for it to for it for it to do  
**Translation:** Vocabulary: constraints: 限制

**[4095.96s] English:** that is there any stuff like a keyboard or or monitors i'm fairly pedestrian on a lot of that  
**Translation:** 

**[4103.78s] English:** where i i did move to triple monitors like in the last several years ago i had been dual monitor for  
**Translation:** Vocabulary: pedestrian: 普通; triple: 三联

**[4109.04s] English:** a very long time and i am and it was one of those things where probably years later than i should  
**Translation:** 

**[4115.36s] English:** have i'm just like well the video cards now generally have three output ports i should just  
**Translation:** 

**[4119.12s] English:** put the third monitor up there that's been a that's been a pure win i've been very happy with  
**Translation:** 

**[4122.94s] English:** that um but no i don't have fancy keyboard or mouse or anything the key things is an ide that  
**Translation:** 

**[4130.42s] English:** has uh helpful debuggers has helpful tools so it's not the emacs vim route and then die coke yeah so  
**Translation:** 

**[4137.66s] English:** i did spend you know i  
**Translation:** Vocabulary: emacs: 编辑器

**[4139.04s] English:** spent i one of my week-long retreats where i'm like okay i'm gonna make myself use uh it was  
**Translation:** 

**[4144.44s] English:** actually classic vi which i know people will say you should never have done that you should have  
**Translation:** Vocabulary: retreats: 静修时光

**[4147.70s] English:** just used vim uh directly but you know i gave it the good try it's like okay i'm being in  
**Translation:** 

**[4152.78s] English:** kind of classic unix developer mode here and i worked for a week on it i used anki to like teach  
**Translation:** 

**[4160.10s] English:** myself the the different little key combinations for things like that and in the end it was just  
**Translation:** 

**[4164.90s] English:** like all right this was kind of like my civil war reenactment phase you know  
**Translation:** 

**[4169.04s] English:** it's like i'm going out there doing it like they used to in the old days and it was kind of fun in  
**Translation:** 

**[4173.42s] English:** that regard so many people right now but it was screaming as they're listening to this so again  
**Translation:** 

**[4178.90s] English:** the out is that this was not modern vim but still i yes i was very happy to get back to my visual  
**Translation:** 

**[4185.52s] English:** studio at the end yeah i'm actually i struggle with this a lot because so use a kinesis keyboard  
**Translation:** Vocabulary: kinesis: 凯迪斯键盘

**[4192.00s] English:** and um i use emacs primarily and i i feel like i can exactly as you said  
**Translation:** 

**[4199.04s] English:** i can understand the  
**Translation:** 

**[4200.00s] English:** code i can navigate the code there's a lot of stuff you could build within emacs with using  
**Translation:** 

**[4204.38s] English:** lisp you can customize a lot of things for yourself to help you uh introspect the code like  
**Translation:** Vocabulary: introspect: 代码分析; navigate: 浏览代码

**[4210.12s] English:** to help you understand the code and visualize different aspects of the code you can even run  
**Translation:** 

**[4213.64s] English:** debuggers but it's it's work and uh the world moves past you and the better and better ideas  
**Translation:** Vocabulary: visualize: 可视化

**[4220.26s] English:** are constantly being built and that that puts a kind of i need to take the same kind of retreat  
**Translation:** 

**[4227.12s] English:** as you're talking about but now i'm still fighting the civil war i need to kind of move into the 21st  
**Translation:** 

**[4232.94s] English:** century and it does seem like the world is or a large chunk of the world is moving towards visual  
**Translation:** 

**[4237.64s] English:** studio code which is kind of interesting to me against the javascript ecosystem on the one hand  
**Translation:** 

**[4243.10s] English:** and ids are one of those things that you want to be infinitely fast you want them to just kind of  
**Translation:** 

**[4249.22s] English:** immediately respond and like i mean heck i've got there's someone i know i'm an old school game dev  
**Translation:** Vocabulary: infinitely: 无穷地

**[4254.90s] English:** guy that still uses visual studio 6  
**Translation:** 

**[4257.12s] English:** and on a modern computer everything is just absolutely instant on something like that  
**Translation:** 

**[4262.94s] English:** because it was made to work on a computer that's 10 000 or 100 000 times slower so just everything  
**Translation:** 

**[4268.62s] English:** happens immediately and all the modern systems just feel you know they feel so crufty when it's  
**Translation:** 

**[4275.18s] English:** like oh why is this refreshing the screen and moving around and updating over here and something  
**Translation:** 

**[4279.62s] English:** blinks down there and you should update this and there's you know there there are things that we've  
**Translation:** 

**[4285.26s] English:** lost with that incredible flexibility  
**Translation:** 

**[4287.12s] English:** but i have lots of people get tons of value from it and i am super happy that that seems to be  
**Translation:** Vocabulary: flexibility: 灵活性

**[4293.26s] English:** winning over even a lot of the old vim and emacs people that they're kind of like hey visual studio  
**Translation:** 

**[4297.96s] English:** codes maybe you know not so bad i am that may be the final peacekeeping solution where everybody  
**Translation:** Vocabulary: emacs: vim替代; peacekeeping: 维持和平

**[4304.24s] English:** is reasonably happy with i with something like that so can you explain what a dot plan file is  
**Translation:** 

**[4310.44s] English:** and what role that played in your life does it still continue to play a role back in the early  
**Translation:** Vocabulary: reasonably: 较为合理地

**[4316.26s] English:** early days of  
**Translation:** 

**[4317.12s] English:** software i one of our big things that was  
**Translation:** 

**[4320.00s] English:** unique with what we did is I had adopted NextStations or kind of Next Step systems from  
**Translation:** 

**[4325.98s] English:** Steve Jobs' Out in the Woods Away from Apple company. And they were basically, it was kind  
**Translation:** 

**[4334.70s] English:** of interesting because I did not really have a background with the Unix system. So many of the  
**Translation:** 

**[4338.64s] English:** people, they get immersed in that in college. And that sets a lot of cultural expectations for them.  
**Translation:** Vocabulary: immersed: 沉浸其中

**[4347.16s] English:** And I didn't have any of that, but I knew that my background was, I was a huge Apple II fanboy.  
**Translation:** 

**[4354.06s] English:** I was always a little suspicious of the Mac. It was not really what kind of I wanted to go with.  
**Translation:** 

**[4361.32s] English:** But when Steve Jobs left Apple and started Next, this computer did just seem like one of those  
**Translation:** 

**[4366.20s] English:** amazing things from the future where it had all of this cool stuff in it. And we were still,  
**Translation:** 

**[4371.58s] English:** back in those days, working on DOS. Everything blew up. You had reset buttons because your  
**Translation:** 

**[4375.94s] English:** computer would just freeze.  
**Translation:** 

**[4376.92s] English:** If you're doing development work, literally dozens of times a day, your computer was just  
**Translation:** 

**[4380.70s] English:** rebooting constantly. And so this idea of, yes, any of the Unix workstations would have given a  
**Translation:** Vocabulary: rebooting: 重新启动; workstations: 工作站

**[4387.04s] English:** stable development platform where you don't crash and reboot all the time. But Next also had this  
**Translation:** 

**[4393.32s] English:** really amazing graphical interface, and it was great for building tools. And it used Objective-C  
**Translation:** Vocabulary: graphical: 图形的; interface: 接口

**[4399.56s] English:** as kind of an interesting dead end for things like that.  
**Translation:** 

**[4403.38s] English:** Unix-based, it's at Objective-C. So there's a lot of,  
**Translation:** 

**[4406.92s] English:** that became Mac. I mean, the kind of reverse acquisition of Apple by Next, where  
**Translation:** 

**[4411.68s] English:** that took over and became what the modern Mac system is.  
**Translation:** 

**[4415.28s] English:** And defined some of the developer, like the tools and the whole community.  
**Translation:** 

**[4421.52s] English:** Yeah, you've still got, if you're programming on Apple stuff now, there's still all these  
**Translation:** 

**[4424.54s] English:** NS-somethings, which was originally Next Step objects of different kinds of things.  
**Translation:** 

**[4429.40s] English:** But one of the aspects of those Unix systems was they had this notion of a dot plan file,  
**Translation:** 

**[4436.10s] English:** where,  
**Translation:** 

**[4436.92s] English:** a dot file is an invisible file.  
**Translation:** 

**[4440.00s] English:** usually in your home directory or something, and there was a trivial server running on most Unix  
**Translation:** 

**[4444.42s] English:** systems at the time that when somebody ran a trivial little command called finger, you could  
**Translation:** 

**[4450.96s] English:** do finger and then somebody's address. It could be anywhere on the internet if you were connected  
**Translation:** 

**[4455.74s] English:** correctly. Then all that server would do was read the dot plan file in that user's home directory  
**Translation:** 

**[4462.16s] English:** and then just spit it out to you. And originally the idea was that could be whether you're on  
**Translation:** 

**[4467.60s] English:** vacation, what your current project was, it's supposed to be the plan of what you're doing,  
**Translation:** 

**[4472.38s] English:** and people would use it for various purposes. But all it did was dump that file over to the  
**Translation:** 

**[4479.46s] English:** terminal of whoever issued the finger command. And at one point I started just keeping a list of  
**Translation:** 

**[4486.96s] English:** what I was doing in there, which would be what I was working on in the day. And I would have this  
**Translation:** 

**[4491.76s] English:** little syntax I kind of got to myself about, here's something that I'm working on. I put a  
**Translation:** Vocabulary: syntax: 语法规则

**[4497.42s] English:** start. I put a stop sign. I put a stop sign. I put a stop sign. I put a stop sign. I put a stop  
**Translation:** 

**[4497.58s] English:** sign. I put a stop sign. I put a stop sign. I put a stop sign. I put a stop sign. I put a stop sign. I put a,  
**Translation:** 

**[4497.60s] English:** when i finish it i could have a few other little bits of punctuation and at the time it was it  
**Translation:** 

**[4503.04s] English:** started off as being just like my to-do list and it would be these trivial obscure little things  
**Translation:** Vocabulary: obscure: 不显眼的

**[4508.54s] English:** like i you know fixed something with collision detection code made imp fireball do something  
**Translation:** 

**[4514.30s] English:** different and just little one-liners that people that were following the games could kind of  
**Translation:** Vocabulary: collision: 碰撞; detection: 检测; fireball: 火球

**[4518.86s] English:** decipher but i did wind up starting to write much more in-depth things i would have i little notes  
**Translation:** 

**[4526.38s] English:** of thoughts and insights and then i would eventually start having little essays i would  
**Translation:** Vocabulary: decipher: 破译 解读

**[4530.66s] English:** sometimes dump into the dot plan files interspersed with the work logs of things that i was doing  
**Translation:** 

**[4535.78s] English:** so in some ways it was like a super early proto blog where i was just kind of dumping out what i  
**Translation:** Vocabulary: interspersed: 夹杂; proto: 雏形

**[4541.84s] English:** was working on but it was interesting enough that there were a lot of people that i that were  
**Translation:** 

**[4547.92s] English:** interested in this so most of the people didn't have unix workstations so there were the websites  
**Translation:** 

**[4552.24s] English:** back in the day that would follow the doom and quake development that would  
**Translation:** 

**[4556.04s] English:** i  
**Translation:** 

**[4556.36s] English:** would basically make a little service that would go grab all the changes and then  
**Translation:** 

**[4560.00s] English:** people could just get it with a web browser and there was a period where like all of the little  
**Translation:** 

**[4564.62s] English:** kind of dallas gaming diaspora of people that were at all in that orbit there were a couple  
**Translation:** 

**[4570.26s] English:** dozen plan files going on which was and this was some years before blogging really became kind of  
**Translation:** Vocabulary: dallas: 达拉斯; diaspora: 流散群体

**[4576.54s] English:** a thing and it was kind of a i'm a premonition of sort of the way things would go and there was  
**Translation:** 

**[4583.26s] English:** it's all been collected it's available online in different places and it's kind of fun to go back  
**Translation:** 

**[4588.28s] English:** and look through what i was thinking uh what i was doing in the different areas have you had a  
**Translation:** 

**[4592.90s] English:** chance to look back is there some interesting very low level specific to do items maybe things  
**Translation:** 

**[4599.22s] English:** you've never completed all that kind of stuff and high level philosophical essay type of stuff  
**Translation:** 

**[4604.92s] English:** uh there's some yeah there's some good stuff on both where a lot of it was low level nitpicky  
**Translation:** Vocabulary: nitpicky: 吹毛求疵; philosophical: 哲学的

**[4611.30s] English:** details about game dev and um you know i've learned enough things where there's no project  
**Translation:** 

**[4617.22s] English:** that i worked on  
**Translation:** 

**[4618.26s] English:** that i couldn't go back and do a better job on now i mean you just you learn things hopefully  
**Translation:** 

**[4622.72s] English:** if you're doing it right you learn things as you get older and you should be able to do a better  
**Translation:** 

**[4626.52s] English:** job at all of the early things and there's stuff in wolfenstein doom quake that's like oh clearly  
**Translation:** 

**[4632.78s] English:** i i could go back and do a better job at this whether it's something in the rendering engine  
**Translation:** Vocabulary: wolfenstein: id软件

**[4637.38s] English:** side or how i implemented the the monster behaviors or managed resources do you see  
**Translation:** 

**[4642.92s] English:** the flaws in your thinking now yeah looking back yeah i do i mean sometimes i'll get the  
**Translation:** 

**[4648.24s] English:** you know i'll look at it and say yeah i had a pretty clear view of i was doing good work there  
**Translation:** 

**[4653.14s] English:** and i haven't really hit the point where there was another programmer graham divine who was i  
**Translation:** 

**[4659.36s] English:** he had worked at id and seventh guest and and he made some comment one time where he said he looked  
**Translation:** 

**[4664.44s] English:** back at some of his old notes he was like wow i was really smart back then and i i don't hit that  
**Translation:** 

**[4671.12s] English:** so much where i mean i look at it and i always know that yeah there's all the you know with  
**Translation:** 

**[4676.16s] English:** aging you get certain changes in in how you do things and there's a lot of things that you can  
**Translation:** 

**[4678.24s] English:** you you're able to work problems  
**Translation:** 

**[4680.00s] English:** But all of the problems that I've worked, I'm sure that I could do a better job on all of them.  
**Translation:** 

**[4686.50s] English:** Oh, wow.  
**Translation:** 

**[4687.04s] English:** So you can still step right in.  
**Translation:** 

**[4688.46s] English:** If you could travel back in time and talk to that guy, you would teach him a few things.  
**Translation:** 

**[4692.10s] English:** Yeah, absolutely.  
**Translation:** 

**[4694.00s] English:** That's awesome.  
**Translation:** 

**[4695.62s] English:** What about the high-level philosophical stuff?  
**Translation:** 

**[4698.00s] English:** Is there some insights that stand out that you remember?  
**Translation:** 

**[4700.12s] English:** There's things that I was understanding about development and the industry and so on that were in a more primitive stage where I definitely learned a lot more in the later years about business and organization and team structure.  
**Translation:** 

**[4720.96s] English:** There were definitely things that I was not the best person or even a very good person about managing.  
**Translation:** 

**[4729.06s] English:** Like how a team...  
**Translation:** 

**[4730.12s] English:** How a team should operate internally, how people should work together.  
**Translation:** 

**[4733.64s] English:** I was just, you know, just get out of my way and let me work on the code and do this.  
**Translation:** Vocabulary: internally: 内部地

**[4739.38s] English:** And more and more, I've learned how, in the larger scheme of things, how sometimes relatively unimportant some of those things are, where it is this user value generation that's the overarching importance for all of that.  
**Translation:** 

**[4754.02s] English:** And I didn't necessarily have my eye on that ball correctly through a lot of my early research.  
**Translation:** Vocabulary: overarching: 总体上的

**[4760.12s] English:** I was just, you know, just get out of my way and let me work on the code and do this.  
**Translation:** 

**[4760.16s] English:** And more and more, I've learned how, in the larger scheme of things, how sometimes relatively unimportant some of those things are, where it is this user value generation that's the overarching importance for all of that.  
**Translation:** 

**[4760.20s] English:** And there's things that, you know, I could have gotten more out of people handling things in different ways.  
**Translation:** 

**[4767.24s] English:** I could have made, you know, in some ways, more successful products by following things in different ways.  
**Translation:** 

**[4773.92s] English:** There's mistakes that we've made that we couldn't really have known how things would have worked out.  
**Translation:** 

**[4778.60s] English:** But it was interesting to see in later years companies like Activision showing that, hey, you really can just do the same game, make it better every year.  
**Translation:** Vocabulary: activision: 暴雪娱乐

**[4786.60s] English:** And you can look at that from a negative standpoint and say, it's like, oh, that's just being directed.  
**Translation:** 

**[4788.24s] English:** And I think that's a really good point.  
**Translation:** Vocabulary: standpoint: 观点

**[4788.46s] English:** It's like, oh, that's just being derivative and all that.  
**Translation:** 

**[4791.58s] English:** But if you step back again and say, it's like, no, are the people buying it still enjoying it?  
**Translation:** Vocabulary: derivative: 抄袭作品

**[4795.54s] English:** Are they enjoying it more than what they might have bought otherwise?  
**Translation:** 

**[4799.22s] English:** And you can say, no.  
**Translation:** 

**[4800.00s] English:** That's actually a great value creation engine to do that if you're in a position where you  
**Translation:** 

**[4805.10s] English:** can.  
**Translation:** 

**[4806.34s] English:** Don't be forced into reinventing everything just because you think that you need to.  
**Translation:** 

**[4812.74s] English:** Lots of things about business and team stuff that could be done better.  
**Translation:** 

**[4817.12s] English:** But the technical work, the kind of technical visionary type stuff that I laid out, I still  
**Translation:** 

**[4822.68s] English:** feel pretty good about.  
**Translation:** 

**[4823.74s] English:** There are some classic old ones about my defending of OpenGL versus D3D, which turned  
**Translation:** 

**[4830.58s] English:** out to be one of the more probably important momentous things there, where it was always  
**Translation:** 

**[4836.98s] English:** a rearguard action on Windows where Microsoft was just not going to let that win.  
**Translation:** 

**[4842.26s] English:** But when I look back on it now, that fight to keep OpenGL relevant for a number of years  
**Translation:** Vocabulary: rearguard: 防守性行动

**[4847.94s] English:** there meant that OpenGL was there when mobile started happening.  
**Translation:** 

**[4852.28s] English:** And OpenGL ES was the thing that drove all of the acceleration of the mobile industry.  
**Translation:** Vocabulary: acceleration: 加速

**[4858.20s] English:** And it's really only in the last few years as Apple's moved to Metal and some of the  
**Translation:** 

**[4862.96s] English:** other companies have moved to Vulkan that that's moved away.  
**Translation:** 

**[4866.48s] English:** But really stepping back and looking at it, it's like, yeah, I sold tens of millions of  
**Translation:** 

**[4871.50s] English:** games for different things.  
**Translation:** 

**[4873.40s] English:** But billions and billions of devices wound up with an appropriate, capable graphics API  
**Translation:** 

**[4880.82s] English:** due in no small amount.  
**Translation:** 

**[4882.28s] English:** And that's a small part to me thinking that that was really important that we not just  
**Translation:** 

**[4886.28s] English:** give up and use Microsoft's, at that time, really terrible API.  
**Translation:** 

**[4892.82s] English:** The thing about Microsoft is the APIs don't stay terrible.  
**Translation:** 

**[4895.82s] English:** They were terrible at the start, but a few versions on, they were actually quite good.  
**Translation:** 

**[4900.10s] English:** And there was a completely fair argument to be made that by the time DX9 was out, it was  
**Translation:** 

**[4905.32s] English:** probably a better programming environment than OpenGL.  
**Translation:** 

**[4907.88s] English:** But it was still a wonderful, good thing that we had an open standard.  
**Translation:** 

**[4912.28s] English:** That could show up on Linux and Android and iOS, and eventually WebGL still to this day.  
**Translation:** 

**[4918.78s] English:** So that was.  
**Translation:** 

**[4920.00s] English:** That would be on my greatest hits list of things that I kind of pushed with.  
**Translation:** 

**[4924.70s] English:** The impact it had on billions of devices, yes.  
**Translation:** 

**[4927.66s] English:** So let's talk about it.  
**Translation:** 

**[4928.96s] English:** Can you tell the origin story of id Software?  
**Translation:** 

**[4932.36s] English:** Again, one of the greatest game developer companies ever.  
**Translation:** 

**[4936.08s] English:** It created Wolfenstein 3D, games that define my life also in many ways.  
**Translation:** 

**[4942.26s] English:** As a thing that made me realize what computers are capable of in terms of graphics, in terms of performance.  
**Translation:** Vocabulary: wolfenstein: 狼穴

**[4947.74s] English:** It just unlocks something deep in me in understanding what these machines are all about.  
**Translation:** 

**[4954.26s] English:** Games can do that.  
**Translation:** 

**[4955.22s] English:** So Wolfenstein 3D, Doom, Quake, and just all the incredible engineering innovation that went into that.  
**Translation:** 

**[4961.84s] English:** So how did it all start?  
**Translation:** 

**[4964.28s] English:** So I'll caveat up front that I usually don't consider myself the historian of the software side of things.  
**Translation:** 

**[4971.32s] English:** I usually do kind of point people at John Romero for stories about the early days.  
**Translation:** Vocabulary: caveat: 声明保留; romero: 约翰·罗梅罗

**[4977.16s] English:** Where?  
**Translation:** 

**[4977.74s] English:** I've never been, like I've commented that I'm a remarkably unsentimental person in some ways.  
**Translation:** Vocabulary: commented: 评论; remarkably: 非常; unsentimental: 不感性

**[4983.90s] English:** Where I don't really spend a lot of time unless I'm explicitly prodded to go back and think about the early days of things.  
**Translation:** 

**[4990.16s] English:** And I didn't necessarily make the effort to archive everything exactly in my brain.  
**Translation:** Vocabulary: prodded: 被催促

**[4997.18s] English:** And the more that I work on machine learning and AI and the aspects of memory.  
**Translation:** 

**[5000.98s] English:** And how when you go back and polish certain things, it's not necessarily exactly the way it happened.  
**Translation:** 

**[5006.06s] English:** But having said all of that.  
**Translation:** 

**[5007.74s] English:** From my view, the way everything happened that led up to that was.  
**Translation:** 

**[5013.92s] English:** After I was an adult, kind of taking a few college classes, deciding to drop out.  
**Translation:** 

**[5019.72s] English:** I was doing, I was hardscrabble contract programming work.  
**Translation:** Vocabulary: hardscrabble: 艰苦的

**[5023.66s] English:** Really struggling to kind of keep groceries and pay my rent and things.  
**Translation:** 

**[5028.18s] English:** And the company that I was doing the most work for was a company called Soft Disk Publishing.  
**Translation:** Vocabulary: groceries: 食品杂货

**[5032.68s] English:** Which had the sounds bizarre now business model of monthly.  
**Translation:** 

**[5037.74s] English:** Subscription software, you know before.  
**Translation:** 

**[5040.00s] English:** there was an internet that people could connect to and get software, you would pay a certain  
**Translation:** 

**[5045.40s] English:** amount. And every month, they would send you a disk that had some random software on it. And  
**Translation:** 

**[5050.02s] English:** people that were into computers thought this was kind of cool. And they had different ones for  
**Translation:** 

**[5053.86s] English:** the Apple II, the 2GS, the PC, the Mac, the Amiga, lots of different things here.  
**Translation:** Vocabulary: amiga: 阿米加计算机

**[5060.12s] English:** So quirky little business, but I was doing a lot of contract programming for them where I'd write  
**Translation:** 

**[5065.20s] English:** tiny little games and sell them for $300, $500. And one of the things that I was doing, again,  
**Translation:** Vocabulary: quirky: 古怪

**[5072.88s] English:** to keep my head above water here, was I decided that I could make one program and I could port  
**Translation:** 

**[5079.70s] English:** it to multiple systems. So I would write a game like Dark Designs or Catacombs, and I would develop  
**Translation:** Vocabulary: catacombs: 地下墓穴

**[5085.74s] English:** it on the Apple II, the 2GS, and the IBM PC, which apparently was the thing that really kind of  
**Translation:** 

**[5093.16s] English:** piqued the attention of the people.  
**Translation:** Vocabulary: piqued: 引起兴趣

**[5095.20s] English:** working down there, like Jay Wilber was my primary editor, and Tom Hall was a secondary editor. And  
**Translation:** 

**[5101.40s] English:** they kept asking me, it's like, hey, you should come down and work for us here. And I pushed it  
**Translation:** Vocabulary: wilber: 威伯

**[5107.20s] English:** off a couple times because I was really enjoying my freedom of kind of being off on my own, even  
**Translation:** 

**[5111.96s] English:** if I was barely getting by. I loved it. I was doing nothing but programming all day. But I did  
**Translation:** 

**[5118.42s] English:** have enough close scrapes with like, damn, I'm just really out of money that maybe I should get an  
**Translation:** 

**[5124.06s] English:** actual job rather.  
**Translation:** Vocabulary: scrapes: 险些发生的事情

**[5125.20s] English:** than contracting these kind of one at a time things. And, and Jay Wilber was great. He was like  
**Translation:** 

**[5129.78s] English:** FedExing me the checks when I would need them to kind of get over whatever hump I was at. So I took  
**Translation:** Vocabulary: contracting: 签订合同

**[5136.82s] English:** the, I finally took them up on their offer to come down to Shreveport, Louisiana. I was in Kansas  
**Translation:** 

**[5141.96s] English:** City at the time, drove down to, through the Ozarks and everything, down to Louisiana and saw  
**Translation:** Vocabulary: kansas: 堪萨斯; ozarks: 奥扎克山脉; shreveport: 虾维port市

**[5150.30s] English:** the soft disk offices, went through, talked to a bunch of people, met the people I had been working  
**Translation:** 

**[5155.00s] English:** with remotely at that time. But the most important thing for me was I met  
**Translation:** Vocabulary: remotely: 远程地

**[5160.00s] English:** two programmers there, John Romero and Lane Roth, that for the first time ever, I had met programmers  
**Translation:** 

**[5165.74s] English:** that knew more cool stuff than I did, where the world was just different back then. I was in Kansas  
**Translation:** Vocabulary: programmers: 程序员

**[5171.96s] English:** City. It was one of those smartest kid in the school, does all the computer stuff. The teachers  
**Translation:** 

**[5176.32s] English:** don't have anything to teach him. But all I had to learn from was these few books at the library.  
**Translation:** 

**[5181.00s] English:** It was not much at all. And there were some aspects of programming that were kind of black  
**Translation:** 

**[5186.42s] English:** magic to me. It's like, oh, he knows how to format a track on a low-level drive programming  
**Translation:** 

**[5192.48s] English:** interface. And I was still not at all sure I was going to take the job. But I met these  
**Translation:** 

**[5199.48s] English:** awesome programmers that were doing cool stuff. And Romero had worked at Origin Systems. And he  
**Translation:** Vocabulary: interface: 界面

**[5204.56s] English:** had done so many different games ahead of time that I did kind of quickly decide, yeah, I'll go  
**Translation:** 

**[5211.36s] English:** take the job down there. And I settled down there.  
**Translation:** 

**[5216.42s] English:** I moved in and started working on more little projects. And the first kind of big change that  
**Translation:** 

**[5222.08s] English:** happened down there was the company wanted to make a gaming-focused, a PC gaming-focused  
**Translation:** 

**[5226.88s] English:** subscription. Just like all their others, the same formula that they used for everything.  
**Translation:** 

**[5231.82s] English:** Pay a monthly fee, and you'll get a disc with one or two games just every month. And no choice in  
**Translation:** Vocabulary: subscription: 订购服务

**[5237.78s] English:** what you get, but we think it'll be fun. And that was the model they were comfortable with. And  
**Translation:** 

**[5242.06s] English:** they said, all right, we're going to start this Gamers Edge department. And all of us,  
**Translation:** 

**[5246.42s] English:** that were interested in that, like me, Romero, Tom Hall was helping us from his side of things.  
**Translation:** 

**[5252.98s] English:** J would peek in. And we had a few other programmers working with us at the time. And we were going to  
**Translation:** Vocabulary: romero: 罗梅罗

**[5259.70s] English:** just start making games, just the same model. And we dived in, and it was fantastic.  
**Translation:** 

**[5265.38s] English:** You have to make new games.  
**Translation:** 

**[5267.22s] English:** Every month.  
**Translation:** 

**[5267.94s] English:** Every month.  
**Translation:** 

**[5268.82s] English:** Yeah. And this, in retrospect, looking back at it,  
**Translation:** 

**[5272.62s] English:** that sense that I done all this contract programming. And John Romero had done,  
**Translation:** Vocabulary: retrospect: 回顾

**[5276.42s] English:** like far more of this where he had done one of his teaching him  
**Translation:** 

**[5280.00s] English:** himself efforts was he made a game for every letter of the alphabet. It's that sense of like,  
**Translation:** 

**[5284.20s] English:** I'm just going to go make 26 different games, give them a different theme. And you learn so  
**Translation:** 

**[5289.16s] English:** much when you go through and you crank these things out, like on a biweekly, monthly basis,  
**Translation:** Vocabulary: biweekly: 每两周一次; crank: 制作

**[5294.60s] English:** something like that. From start to finish. So it's not like just an idea. It's not just  
**Translation:** 

**[5298.50s] English:** from the very beginning to the very end. It's done. It has to be done. There's no delaying.  
**Translation:** Vocabulary: delaying: 拖延

**[5305.26s] English:** And you've got deadlines. And that kind of rapid iteration pressure cooker environment  
**Translation:** 

**[5311.72s] English:** was super important for all of us developing the skills that brought us to where we eventually  
**Translation:** Vocabulary: deadlines: 截止日期; iteration: 迭代

**[5318.12s] English:** went to. I mean, people would say like in the history of the Beatles, it wasn't them being  
**Translation:** 

**[5322.54s] English:** the Beatles. It was them playing all of these other early works that that opportunity to craft  
**Translation:** Vocabulary: beatles: 甲壳虫乐队

**[5327.46s] English:** all of their skills before they were famous, that was very critical to their later successes.  
**Translation:** 

**[5332.80s] English:** And I think there's a lot of that here where  
**Translation:** 

**[5335.24s] English:** we did these games that nobody remembers, lots of little things that contributed to  
**Translation:** 

**[5341.14s] English:** building up the skill set for the things that eventually did make us famous.  
**Translation:** 

**[5345.60s] English:** Yeah, Dostoevsky wrote The Gambler. I had to write it in a month, just make money.  
**Translation:** 

**[5352.52s] English:** And nobody remembers that probably because he had to figure out because it's literally  
**Translation:** Vocabulary: dostoevsky: 陀思妥耶夫斯基; gambler: 赌徒

**[5356.80s] English:** he didn't have enough time to write it fast enough. So he had to come up with hacks.  
**Translation:** 

**[5363.02s] English:** Literally, it comes down to that point.  
**Translation:** Vocabulary: hacks: 权宜之计

**[5365.24s] English:** Where pressure and limitation of resources is surprisingly important. And it's counterintuitive  
**Translation:** 

**[5371.78s] English:** in a lot of ways where you just think that if you've got all the time in the world, and you've  
**Translation:** Vocabulary: counterintuitive: 逆常理的

**[5375.16s] English:** got all the resources in the world, of course, you're going to get something better. But sometimes  
**Translation:** 

**[5378.94s] English:** it really does work out that the, you know, innovations, mother necessity, and you know,  
**Translation:** Vocabulary: innovations: 创新; necessity: 必要性

**[5384.46s] English:** where you can are resource constraints, and you have to do things when you don't have a choice.  
**Translation:** 

**[5389.28s] English:** It's surprising what you can do.  
**Translation:** Vocabulary: constraints: 资源限制

**[5390.88s] English:** Is there any good games written in that time? Would you say?  
**Translation:** 

**[5393.36s] English:** Some of them are still fun to go back and play.  
**Translation:** 

**[5395.24s] English:** Where you get the, they were, they were all about kind of the  
**Translation:** 

**[5400.00s] English:** more modern term is game feel about how just the exact feel that things it's not the grand strategy  
**Translation:** 

**[5405.42s] English:** of the design but how running and jumping and shooting and those things i feel in the in the  
**Translation:** 

**[5411.26s] English:** moment and some of those are still if you sat down out on you kind of go it's a little bit different  
**Translation:** 

**[5415.98s] English:** it doesn't have the same movement feel but you move over and you're like bang jump bang it's  
**Translation:** 

**[5420.94s] English:** like hey that's kind of cool still so you can get lost in the rhythm of the game like the is that  
**Translation:** 

**[5426.34s] English:** what you mean by feel just like uh there's something about it that pulls you in nowadays  
**Translation:** 

**[5431.70s] English:** again people talk about compulsion loops and things where it's that i am that sense of exactly  
**Translation:** Vocabulary: compulsion: 强迫症

**[5437.14s] English:** what you're doing what your fingers are doing on the keyboard what your eyes are seeing and there  
**Translation:** 

**[5441.50s] English:** are going to be these sequences of things grab the loot shoot the monster jump over the obstacle  
**Translation:** 

**[5445.82s] English:** get to the end of the level these are eternal aspects of game design in a lot of ways but there  
**Translation:** 

**[5451.24s] English:** are better and worse ways to do all of them and we did so many of these games that it was  
**Translation:** 

**[5456.34s] English:** i we got a lot of practice with it so one of the kind of weird things that was happening at this  
**Translation:** 

**[5462.02s] English:** time is john romero was getting some uh some strange fan mail and back in the days this is  
**Translation:** 

**[5467.98s] English:** before email so we literally got letters sometimes and telling him it's like oh i want to talk to you  
**Translation:** 

**[5473.58s] English:** about your games i want to reach out different things and i eventually it turned out that these  
**Translation:** 

**[5480.16s] English:** were all coming from scott miller at apogee software and he was reaching out through  
**Translation:** 

**[5486.34s] English:** he didn't think he could contact john directly that he would get intercepted so he was trying  
**Translation:** Vocabulary: apogee: 顶点; intercepted: 拦截

**[5490.34s] English:** to get him to contact him through like back channel fan mail because he basically was saying  
**Translation:** 

**[5495.42s] English:** hey i'm making all this money on shareware games i want you to make shareware games because he had  
**Translation:** Vocabulary: shareware: 共享软件

**[5501.40s] English:** seen some of the the games that romero had done and you know we looked at scott miller's games and  
**Translation:** 

**[5508.02s] English:** we didn't think they were very good i am we're like that can't be making the kind of money that  
**Translation:** Vocabulary: romero: 罗梅罗

**[5513.22s] English:** he's saying he's making 10 grand or something i am  
**Translation:** 

**[5516.34s] English:** off of this game and we really thought that he was full of shit that it was  
**Translation:** 

**[5520.00s] English:** a lie trying to get to get him into this but so that was kind of going on at i am you know at one  
**Translation:** 

**[5526.50s] English:** level he was and it was funny the moment when romero realized that he had some of these letters  
**Translation:** 

**[5531.46s] English:** pinned up on his wall like all of his fans and then we noticed that they all had the same return  
**Translation:** 

**[5535.36s] English:** address with different names on them which was a little bit of a two-edged sword there  
**Translation:** 

**[5539.54s] English:** trying to figure out the puzzle laid out before him yeah what happened after i kind of coincident  
**Translation:** 

**[5546.12s] English:** with that was i was working on a lot of the new technologies where i was now full on the ibm pc  
**Translation:** Vocabulary: coincident: 巧合

**[5552.92s] English:** for the first time where i was really a long hold out on apple 2 forever and i you know i loved my  
**Translation:** 

**[5558.54s] English:** apple 2 it was the computer i always wished i had when i was growing up and when i finally did have  
**Translation:** 

**[5562.90s] English:** one i was i was kind of clinging on to that well past it's sort of good use by the best computer  
**Translation:** 

**[5568.16s] English:** ever made you would you say um i wouldn't make judgments like that about it but it was positioned  
**Translation:** Vocabulary: clinging: 依恋

**[5573.94s] English:** in such a way especially in the school system  
**Translation:** 

**[5576.10s] English:** that it impacted a whole lot of american programmers at least where there was programs  
**Translation:** Vocabulary: programmers: 程序员

**[5582.06s] English:** that the apple 2s got into the schools and they had enough capability that lots of interesting  
**Translation:** 

**[5586.90s] English:** things happened with them you know in europe it was different you had your amigas and ataris and  
**Translation:** Vocabulary: capability: 能力

**[5591.62s] English:** you know i'm acorns in the uk and things that that had different things but in the united states it  
**Translation:** 

**[5597.14s] English:** was probably the apple 2 made the most impact for a lot of programmers of my generation but so i was  
**Translation:** Vocabulary: acorns: 幼苗

**[5604.10s] English:** really digging into the ibm  
**Translation:** 

**[5605.78s] English:** and this was even more so with the total focus because i'd moved to another city where i didn't  
**Translation:** 

**[5611.26s] English:** know anybody that i wasn't working with uh i had a little apartment and then at soft disk again the  
**Translation:** 

**[5617.00s] English:** things that that drew me to it i had a couple programmers that knew more than i did uh and  
**Translation:** 

**[5622.42s] English:** they had a library they had a set of books and a set of magazines they had a couple years of  
**Translation:** 

**[5627.10s] English:** magazines the old dr dobbs journal and all of these magazines that had information about things  
**Translation:** Vocabulary: dobbs: ドブズ期刊

**[5632.94s] English:** and so i was just in total  
**Translation:** 

**[5635.78s] English:** immersion mode it was eat breathe sleep computer programming particularly  
**Translation:** Vocabulary: immersion: 全沉浸

**[5640.00s] English:** the IBM for everything that I was doing. And I was digging into a lot of these low-level  
**Translation:** 

**[5645.42s] English:** hardware details that people weren't usually paying attention to, the way the IBM EGA cards  
**Translation:** 

**[5651.68s] English:** worked, which was fun for me. I hadn't had experience with things at that level. And back  
**Translation:** 

**[5657.58s] English:** then, you could get hardware documentation just down at the register levels. This is where the  
**Translation:** 

**[5662.50s] English:** CRTC register is. This is how the color registers work and how the different things are applied.  
**Translation:** 

**[5667.76s] English:** And they were designed for a certain reason. They were designed for an application. They had  
**Translation:** 

**[5672.56s] English:** an intended use in mind, but I was starting to look at other ways that they could perhaps be  
**Translation:** 

**[5678.12s] English:** exploited that they weren't initially intended for. Could you comment on, first of all, what  
**Translation:** Vocabulary: exploited: 利用

**[5682.86s] English:** operating system was there? What instructions? What are we talking about? So this was DOS and  
**Translation:** 

**[5689.46s] English:** x86. So 16-bit 8086. The 286s were there, and 386s existed. They were rare. We had a couple  
**Translation:** 

**[5697.42s] English:** for our devices. We had a couple for our devices. We had a couple for our devices. We had a couple  
**Translation:** 

**[5697.74s] English:** for our devices. We had a couple for our devices. We had a couple for our devices. We had a couple  
**Translation:** 

**[5697.76s] English:** for our systems. But we were still targeting the more broad. It was all DOS 16-bit. None of this was  
**Translation:** 

**[5705.70s] English:** kind of DOS extenders and things. How different is it from the systems of today? Is it kind of  
**Translation:** Vocabulary: extenders: 内存扩展

**[5710.06s] English:** a precursor that's similar? Very little. If you open up command.exe or com on Windows,  
**Translation:** 

**[5717.66s] English:** you see some of the remnants of all of that. But it was a different world. It was the 640k  
**Translation:** Vocabulary: precursor: 前身; remnants: 残迹

**[5722.40s] English:** is enough world. And nothing was protected. It crashed all the time. You had  
**Translation:** 

**[5727.10s] English:** TSRs or terminate and stay resident hacks on top of things that would cause configuration  
**Translation:** Vocabulary: configuration: 设置; hacks: 漏洞; terminate: 终止

**[5732.12s] English:** problems. All the hardware was manually configured in your auto exec. So it was a very different  
**Translation:** 

**[5738.72s] English:** world. But the code is still the same, similar. You could still write it. My earliest code there  
**Translation:** Vocabulary: configured: 设置好的

**[5743.56s] English:** was written in Pascal. That was what I had learned at an earlier point. So between BASIC and C++,  
**Translation:** 

**[5750.38s] English:** there was Pascal. So when BASIC assembly language and some of my intermediate stuff was, well,  
**Translation:** Vocabulary: pascal: 帕斯卡

**[5755.80s] English:** you had to for performance. But you had to for performance. So you had to for performance.  
**Translation:** 

**[5757.08s] English:** BASIC was just too slow. So most of the work that  
**Translation:** 

**[5760.00s] English:** i was doing as a contract programmer in my teenage years was uh was assembly language  
**Translation:** 

**[5764.80s] English:** wait you wrote games in assembly yeah complete games in uh in assembly language and it's  
**Translation:** 

**[5771.28s] English:** thousands and thousands of lines of three-letter acronyms for the the instructions that's you don't  
**Translation:** 

**[5777.54s] English:** earn the once again greatest programmer ever label without being able to write a game in assembly  
**Translation:** Vocabulary: acronyms: 缩写; programmer: 程序员

**[5783.06s] English:** okay that's again everybody wrote their everybody serious wrote their games in assembly language it  
**Translation:** 

**[5787.50s] English:** was kind of a serious everybody's serious yeah it was an outlier to use uh pascal a little bit  
**Translation:** 

**[5793.96s] English:** where there was one famous program called wizardry it was like one of the great early role-playing  
**Translation:** 

**[5798.66s] English:** games that was written in pascal but it was almost nothing used pascal there but i did learn pascal  
**Translation:** Vocabulary: wizardry: 巫术游戏

**[5804.76s] English:** and i remember doing all of my like to this day i sketch in data structures when i'm thinking about  
**Translation:** 

**[5810.10s] English:** something i'll you know i'll i'll open up a file and i'll start writing struct definitions for  
**Translation:** Vocabulary: struct: 结构体

**[5814.96s] English:** how data is going to be laid out and  
**Translation:** 

**[5817.50s] English:** pascal was kind of formative to that because i remember designing my rpgs in pascal record  
**Translation:** 

**[5822.20s] English:** structures and things like that and so i had i've gotten a pascal compiler for the apple 2gs that i  
**Translation:** 

**[5828.16s] English:** could work on in the first ibm game that i developed i did in pascal and and that's actually  
**Translation:** 

**[5833.74s] English:** kind of an interesting story again talking about the constraints and resources where i had an apple  
**Translation:** 

**[5839.28s] English:** 2gs i didn't have an ibm pc i wanted to port my applications to ibm because i thought i could make  
**Translation:** Vocabulary: constraints: 限制

**[5845.66s] English:** more money on it so  
**Translation:** 

**[5847.50s] English:** what i wound up doing is i rented a pc for a week and bought a copy of turbopascal and so i had a  
**Translation:** 

**[5854.92s] English:** hard one week and this was cutting into what minimal profit margin i had there but i had this  
**Translation:** 

**[5859.36s] English:** computer for a week i had to get my program ported before i had to return the pc yeah and that was  
**Translation:** 

**[5865.40s] English:** kind of what the first thing that i had done on the ibm pc and what led me to the taking the job  
**Translation:** 

**[5870.50s] English:** at soft disk and turbopascal uh how's that different from regular pascal is a different  
**Translation:** Vocabulary: pascal: 帕斯卡

**[5875.62s] English:** compiler or something like that it was uh it was a different compiler and it was a different compiler  
**Translation:** 

**[5877.50s] English:** It was a product of Borland, which before Microsoft.  
**Translation:** 

**[5880.00s] English:** kind of killed them they were they were the hot stuff developer tools company you had borland  
**Translation:** 

**[5884.82s] English:** turbo pascal turbo c and prologue i mean all the different things but what they did was they took  
**Translation:** Vocabulary: turbo: 加速

**[5891.38s] English:** a supremely pragmatic approach of making something useful it was one of these great examples where  
**Translation:** 

**[5896.40s] English:** pascal was an academic language and you had things like the ucsdp system that wizardry was actually  
**Translation:** Vocabulary: pragmatic: 实用至上; supremely: 极其

**[5903.08s] English:** written in that they did they did manage to make a game with that but it was not a super practical  
**Translation:** 

**[5910.24s] English:** system while turbo pascal was it was called turbo because it was blazingly fast to compile i mean  
**Translation:** 

**[5915.78s] English:** really ridiculously 10 to 20 times faster than most other compilers at the time but it also had  
**Translation:** 

**[5922.46s] English:** very pragmatic access to look you can just poke at the hardware in these different ways and we have  
**Translation:** Vocabulary: compilers: 编译器; ridiculously: 极其

**[5927.28s] English:** libraries that let you do things and it was a pretty good it was a perfectly good way to write  
**Translation:** 

**[5931.96s] English:** games and this is one of the things that i think is really important to me is that it's not just  
**Translation:** 

**[5933.06s] English:** those things where people have talked about different paths that computer development could  
**Translation:** 

**[5937.74s] English:** have taken where c took over the world for reasons that came out of unix and eventually linux and  
**Translation:** 

**[5944.50s] English:** and that was not a foregone conclusion at all and people can make real reasoned rational arguments  
**Translation:** 

**[5950.58s] English:** that the world might have been better if it had gone a pascal route i'm somewhat agnostic on that  
**Translation:** Vocabulary: agnostic: 无所知

**[5956.22s] English:** where i do know from experience it was perfectly good enough to do do that and it had some  
**Translation:** 

**[5961.82s] English:** fundamental improvements  
**Translation:** 

**[5963.02s] English:** like it had range checked arrays as an option there which could avoid many of c's real hazards  
**Translation:** 

**[5969.50s] English:** that happened in a security space but c1 they were basically operating at about the same level  
**Translation:** 

**[5974.58s] English:** of abstraction it was a systems programming language but you said pascal had more emphasis  
**Translation:** 

**[5980.20s] English:** on data structures actually i um in the in the tree of languages did pascal come before c  
**Translation:** 

**[5986.94s] English:** did it they were pretty contemporaneous so pascal's lineage went to modula 2 and eventually  
**Translation:** 

**[5993.02s] English:** on which was another nicholas word i'm i'm kind of experimental language but they were all good  
**Translation:** Vocabulary: contemporaneous: 同时代的; lineage: 血统; modula: 莫杜拉; nicholas: 尼古拉斯

**[5999.80s] English:** enough  
**Translation:** 

**[6000.00s] English:** at that level. Now, some of the classic academic-oriented Pascals were just missing  
**Translation:** Vocabulary: pascals: 帕斯卡

**[6004.84s] English:** fundamental things like, oh, you can't access this core system thing because we're just using  
**Translation:** 

**[6008.84s] English:** it to teach students. But Turbo Pascal showed that only modest changes to it really did make  
**Translation:** Vocabulary: pascal: 帕斯卡; turbo: turbo

**[6014.70s] English:** it a completely capable language. And it had some reasons why you could implement it as a  
**Translation:** 

**[6019.80s] English:** single-pass compiler, so it could be way, way faster, although less scope for optimizations  
**Translation:** Vocabulary: optimizations: 优化

**[6024.28s] English:** if you do it that way. And it did have some range-checking options. It had a little bit  
**Translation:** 

**[6028.96s] English:** better typing capability. You'd have properly typed enums, sorts of things, and other stuff  
**Translation:** Vocabulary: capability: 能力

**[6034.08s] English:** that C lacked. But C was also clearly good enough, and it wound up with a huge inertia  
**Translation:** 

**[6039.48s] English:** from the Unix ecosystem and everything that came with that. And Pascal didn't have garbage collection?  
**Translation:** Vocabulary: inertia: 惯性

**[6043.90s] English:** No, it was not garbage collected. It's the same kind of thing as C. Yeah, same manual. So you  
**Translation:** 

**[6047.30s] English:** could still have your use-after-freeze and all those other problems, but just getting rid of  
**Translation:** 

**[6052.76s] English:** array overruns, at least if you were compiled with that debugging option, certainly would have avoided  
**Translation:** 

**[6057.06s] English:** a lot of problems and could have a lot of problems.  
**Translation:** Vocabulary: compiled: 编译过的

**[6058.96s] English:** So anyways, that was the next thing. I had to learn C, because C was where it seemed like most  
**Translation:** 

**[6064.72s] English:** of the things were going. So I abandoned Pascal, and I started working in C. I started hacking on  
**Translation:** Vocabulary: hacking: 编程

**[6070.48s] English:** these hardware things, dealing with the graphics controllers and the EGA systems. And what we most  
**Translation:** 

**[6077.28s] English:** wanted to do—so at that time, we were sitting in our darkened office playing all the different  
**Translation:** 

**[6083.50s] English:** console video games, and we were figuring out what games do we want to make for our gamers  
**Translation:** 

**[6088.96s] English:** edge product there. And so we had one of the first Super Nintendos sitting there, and we had an  
**Translation:** Vocabulary: nintendos: 任天堂游戏机

**[6095.04s] English:** older Nintendo. We were looking at all those games. And the core thing that those consoles did that you  
**Translation:** 

**[6099.84s] English:** just didn't get on the PC games was this ability to have a massive scrolling world, where most of  
**Translation:** Vocabulary: consoles: 游戏机; scrolling: 滚动

**[6105.60s] English:** the games that you would make on the PC and earlier personal computers would be a static screen. You  
**Translation:** 

**[6111.60s] English:** move little things around on it, and you interact like that. Maybe you go to additional screens as  
**Translation:** 

**[6116.86s] English:** you move. But Arcade—  
**Translation:** 

**[6118.96s] English:** Arcade games and consoles  
**Translation:** Vocabulary: arcade: 街机厅

**[6120.00s] English:** had this wonderful ability to just have a big world that you're slowly moving your window through.  
**Translation:** 

**[6126.24s] English:** And that was, for those types of games, the kind of action, exploration, adventure games,  
**Translation:** 

**[6130.78s] English:** that was a super, super important thing. And PC games just didn't do that. And what I had  
**Translation:** 

**[6137.02s] English:** come across was a couple different techniques for implementing that on the PC. And they're not  
**Translation:** Vocabulary: implementing: 实现

**[6142.88s] English:** hard, complicated things. When I explain them now, they're pretty straightforward,  
**Translation:** 

**[6148.04s] English:** but just nobody was doing. You sound like Einstein describing his five papers. It's  
**Translation:** Vocabulary: einstein: 爱因斯坦; straightforward: 简单明了

**[6152.18s] English:** pretty straightforward. I understand. But they're nevertheless revolutionary. So side-scrolling  
**Translation:** 

**[6156.94s] English:** is a game-changer. Yeah. It's a genius invention. And some of the consoles had different limitations  
**Translation:** 

**[6163.50s] English:** about you could do one but not the other. And there were similar things going on as advancements,  
**Translation:** 

**[6168.42s] English:** even in the console space, where you'd have, like, the original Mario game was just horizontal  
**Translation:** Vocabulary: advancements: 进步; horizontal: 水平; mario: 马里奥

**[6173.92s] English:** scrolling. And then later, Mario games added vertical aspects to it and different things  
**Translation:** 

**[6177.90s] English:** that...  
**Translation:** Vocabulary: vertical: 垂直

**[6178.04s] English:** That you were doing to explore, you know, kind of expand the capabilities there. And so much of  
**Translation:** 

**[6183.62s] English:** the early game design for decades was removing limitations, letting you do things that you  
**Translation:** 

**[6188.82s] English:** envisioned as a designer, you wanted the player to experience, but the hardware just couldn't  
**Translation:** 

**[6193.32s] English:** really, or you didn't know how to make it happen. It felt impossible.  
**Translation:** Vocabulary: envisioned: 构想出

**[6197.56s] English:** You can imagine that you want to create, like, this big world through which you can side-scroll,  
**Translation:** 

**[6203.98s] English:** like, through which you can walk. And then you ask yourself,  
**Translation:** 

**[6207.94s] English:** of course, how do you do that? And then you ask yourself, of course, how do you do that?  
**Translation:** 

**[6208.02s] English:** How do I actually build that in a way that's, like, the latency is low enough,  
**Translation:** Vocabulary: latency: 延迟

**[6214.64s] English:** the hardware can actually deliver that in such a way that it's a compelling experience?  
**Translation:** 

**[6218.80s] English:** Yeah, and we knew what we wanted to do because we were playing all of these console games,  
**Translation:** Vocabulary: compelling: 引人入胜

**[6222.76s] English:** playing all these Nintendo games and arcade games. Clearly, there was a whole world of  
**Translation:** 

**[6226.56s] English:** awesome things there that we just couldn't do on the PC, at least initially. Because every  
**Translation:** 

**[6231.90s] English:** programmer can tell. It's like, if you want to scroll, you can just redraw the whole screen.  
**Translation:** 

**[6235.38s] English:** But then it turns out, well, you're going five frames per second,  
**Translation:** 

**[6238.00s] English:** that's not an interactive  
**Translation:** 

**[6240.00s] English:** fun experience. You want to be going 30 or 60 frames per second or something. And it just didn't  
**Translation:** Vocabulary: interactive: 交互式

**[6245.56s] English:** feel like that was possible. It felt like the PCs had to get five times faster for you to make a  
**Translation:** 

**[6250.86s] English:** playable game there. And interestingly, I wound up with two completely different solutions for  
**Translation:** 

**[6257.20s] English:** the scrolling problem. And this is a theme that runs through everything, where all of these  
**Translation:** 

**[6263.70s] English:** big technical advancements, it turns out there's always a couple different ways of doing them.  
**Translation:** Vocabulary: scrolling: 滚动问题

**[6268.00s] English:** And it's not like you found the one true way of doing it. And we'll see this as we go into 3D  
**Translation:** 

**[6273.66s] English:** games and things later. But so the first set of scrolling tricks that I got was,  
**Translation:** 

**[6280.72s] English:** the hardware had this ability to, you could shift inside the window of memory. So the EGA cards at  
**Translation:** 

**[6288.86s] English:** the time had 256 kilobytes of memory. And it was awkwardly set up in this planar format where  
**Translation:** Vocabulary: awkwardly: 笨拙地; kilobytes: 千字节

**[6295.86s] English:** instead of having 256,  
**Translation:** 

**[6298.00s] English:** or, you know, 24 million colors, you had 16 colors, which is four bits. So you had four bit planes,  
**Translation:** 

**[6304.90s] English:** 64k a piece, of course, 64k is a nice round number for 16 bit addressing. So your graphics card had  
**Translation:** 

**[6311.82s] English:** a 16 bit window that you could look at, and you could tell it to start the video scan out anywhere  
**Translation:** 

**[6318.18s] English:** inside there. So there were a couple games that had taken this approach, if you could make a two  
**Translation:** 

**[6323.02s] English:** by two screen or a one by four screen, and you could do scrolling really easily like that,  
**Translation:** 

**[6328.00s] English:** you could just lay it all out, and just pan around there, but you just couldn't make it any bigger,  
**Translation:** 

**[6332.52s] English:** because that's all the memory that was there. The first insight to the scrolling that I had was,  
**Translation:** 

**[6338.28s] English:** well, if we make a screen that's just one tile larger, you know, and we usually had tiles that  
**Translation:** 

**[6343.68s] English:** were 16 pixels by 16 pixels, the little classic Mario block that you run into, lots of art gets  
**Translation:** Vocabulary: mario: 马里奥; pixels: 像素

**[6349.76s] English:** drawn that way. And your screen is a certain number of tiles. But if you had one little buffer region  
**Translation:** 

**[6355.22s] English:** outside of that, you could easily pan around,  
**Translation:** Vocabulary: buffer: 缓冲区

**[6358.00s] English:** inside that 16-pixel region.  
**Translation:** 

**[6360.00s] English:** That could be perfectly smooth, but then what happens if you get to the edge and you want to  
**Translation:** Vocabulary: pixel: 像素

**[6364.54s] English:** keep going? The first way we did scrolling was what I called adaptive tile refresh, which was  
**Translation:** 

**[6371.16s] English:** really just a matter of you get to the edge and then you go back to the original point and then  
**Translation:** Vocabulary: adaptive: 适应性

**[6376.42s] English:** only change the tiles that are different between where it was. In most of the games at the time,  
**Translation:** 

**[6383.28s] English:** if you think about sort of your classic Super Mario Brothers game, you've got big fields of  
**Translation:** 

**[6388.34s] English:** blue sky, long rows of the same brick texture, and there's a lot of commonality. It's kind of  
**Translation:** 

**[6395.32s] English:** like a data compression thing. If you take the screen and you set it down on top of each other,  
**Translation:** Vocabulary: compression: 数据压缩

**[6399.94s] English:** in general, only about 10% of the tiles were actually different there. So this was a way to  
**Translation:** 

**[6406.50s] English:** go ahead and say, well, I'm going to move it back and then I'm only going to change those  
**Translation:** 

**[6410.90s] English:** 10, 20, whatever percent tiles there. And that meant that it was essentially five times faster  
**Translation:** 

**[6417.44s] English:** than if you were redrawing.  
**Translation:** 

**[6418.34s] English:** All of the tiles. And that worked well enough for us to do a bunch of these games for  
**Translation:** 

**[6423.22s] English:** Gamers Edge. We had a lot of these scrolling games like Slurred Axe and Shadow Knights and  
**Translation:** Vocabulary: scrolling: 卷轴; slurred: 口吃

**[6428.02s] English:** things like that, that we were cranking out at this high rate that had this scrolling effect on it.  
**Translation:** 

**[6433.36s] English:** And it worked well enough. There were design challenges there where if you made, the worst  
**Translation:** Vocabulary: cranking: 快速生产

**[6437.96s] English:** case, if you made a checkerboard over the entire screen, you scroll over one and every single tile  
**Translation:** 

**[6442.60s] English:** changes and your frame rate's now five frames per second because it had to redraw everything.  
**Translation:** Vocabulary: checkerboard: 棋盘; scroll: 滚动

**[6446.82s] English:** So the designers had a  
**Translation:** 

**[6448.32s] English:** little bit that they had to worry about. They had to make these relatively plain looking levels,  
**Translation:** Vocabulary: designers: 设计师

**[6452.54s] English:** but it was still pretty magical. It was something that we hadn't seen before.  
**Translation:** 

**[6457.72s] English:** And the first thing that we wound up doing with that was I had just gotten this working and Tom  
**Translation:** 

**[6464.28s] English:** Hall was sitting there with me and we were looking over at our Super Nintendo on the side there with  
**Translation:** 

**[6470.36s] English:** Super Mario 3 running. And we had the technology, we had the tools set up there and we stayed up  
**Translation:** Vocabulary: mario: 超级玛丽

**[6477.14s] English:** all night.  
**Translation:** 

**[6477.70s] English:** And we basically cloned the first level of  
**Translation:** 

**[6480.00s] English:** super mario brothers performance wise as well yeah and so it and we had our little character  
**Translation:** 

**[6484.68s] English:** running and jumping in there it was you know it wasn't uh it was close to pixel accurate as far  
**Translation:** 

**[6489.08s] English:** as all the uh the backgrounds and everything but the gaming was just stuff that we cobbled together  
**Translation:** 

**[6493.38s] English:** from previous games that i had written i just kind of like really kitbashed the whole thing  
**Translation:** Vocabulary: cobbled: 拼凑; kitbashed: 混搭

**[6497.60s] English:** together to make this demo and that was one of the rare cases when i said i i don't usually do  
**Translation:** 

**[6503.00s] English:** these all night programming things there's probably only two memorable ones that i can  
**Translation:** 

**[6507.44s] English:** think about you know one was the all-nighter to go ahead and get i am to get our dangerous  
**Translation:** 

**[6512.90s] English:** dave and copyright infringement is how we titled it because we had a game called dangerous dave  
**Translation:** Vocabulary: infringement: 侵权

**[6517.10s] English:** was you know running around with the shotgun shooting things uh and we were just taking our  
**Translation:** 

**[6521.60s] English:** most beloved game at the time there the super mario 3 and sort of sticking dave inside that  
**Translation:** Vocabulary: shotgun: 猎枪; sticking: 塞入

**[6526.76s] English:** with this new scrolling technology that was going perfectly smooth for i am you know for the  
**Translation:** 

**[6532.74s] English:** as it ran and tom and i just kind of blearily the next morning  
**Translation:** Vocabulary: blearily: 模糊不清地

**[6537.44s] English:** kind of left and we left a disc on i you know on the desk for john romero and jay wilbur to see and  
**Translation:** 

**[6543.82s] English:** just said run this and we eventually made it back in later in the day and it was you know like they  
**Translation:** Vocabulary: romero: 约翰·罗梅罗; wilbur: 杰·威尔伯

**[6550.56s] English:** grabbed us and pulled us in you know pulled us into the room and that was the point where they  
**Translation:** 

**[6555.06s] English:** were like we got to do something with this you know we're we're going to make a company we're  
**Translation:** 

**[6559.48s] English:** going to go make our own games where this was something that we we were able to just kind of  
**Translation:** 

**[6564.42s] English:** hit them with a hammer of an experience like wow this is just like a game that we're going to  
**Translation:** 

**[6567.44s] English:** so much cooler than what we thought was possible there and initially we tried to get nintendo to  
**Translation:** 

**[6574.16s] English:** to let us make super mario 3 on the pc that's really what we wanted to do we're like hey  
**Translation:** 

**[6579.00s] English:** we can finish this it's line of sight for this will be great and we sent something to nintendo  
**Translation:** 

**[6584.92s] English:** and we heard that it did get looked at in japan i and they just weren't interested in that i but  
**Translation:** 

**[6590.88s] English:** that's another one of those life could have gone a very different way where we could have been  
**Translation:** 

**[6594.50s] English:** like nintendo's house pc team i  
**Translation:** 

**[6597.44s] English:** you know at that point and define the direction of  
**Translation:** 

**[6600.00s] English:** you know uh wolfenstein and uh doom and quake could have been a nintendo creation yeah so at  
**Translation:** Vocabulary: wolfenstein: 狼穴游戏

**[6609.94s] English:** the same time that we were just doing our first scrolling demos i we reached out to scott miller  
**Translation:** 

**[6616.26s] English:** at apogee and said it's like hey we do want to make some games you know these things that you  
**Translation:** Vocabulary: apogee: 阿波罗; demos: 演示; scrolling: 滚动

**[6620.82s] English:** think you want those are those are nothing what do you see what we can actually do now this is  
**Translation:** 

**[6624.82s] English:** going to be amazing and he just like popped right up and sent a check to us where we at that point  
**Translation:** 

**[6630.76s] English:** we still thought he might be a fraud that he was just lying about all of this but he was totally  
**Translation:** 

**[6635.30s] English:** correct on how much money he was making with his shareware titles and this was his his kind of real  
**Translation:** Vocabulary: shareware: 共享软件

**[6641.84s] English:** brainstorm about this where shareware was this idea that software doesn't have a fixed price  
**Translation:** 

**[6647.12s] English:** if you use it you send out of the goodness of your heart some money to the creator and there  
**Translation:** 

**[6652.00s] English:** were a couple utilities that did make some significant success  
**Translation:** 

**[6654.82s] English:** like that but for the most part it didn't really work you know there wasn't much software in a  
**Translation:** Vocabulary: utilities: 公共设施

**[6660.36s] English:** pure shareware model that uh that was successful the apogee innovation was to take something call  
**Translation:** 

**[6667.98s] English:** it shareware split it into three pieces you always made a trilogy and you would put the first piece  
**Translation:** 

**[6673.66s] English:** out but then you buy the whole trilogy for some shareware amount which in reality it meant that  
**Translation:** 

**[6679.84s] English:** the first part was a demo where you kind of like the demo went everywhere for free and you paid  
**Translation:** Vocabulary: trilogy: 三部曲

**[6684.54s] English:** money and you made money and you made money and you made money and you made money and you made  
**Translation:** 

**[6684.80s] English:** money to to get the whole set but it was still played as shareware and we were happy to have the  
**Translation:** 

**[6689.60s] English:** first one go everywhere and it wasn't a crippled demo where the first episode of all these  
**Translation:** 

**[6694.42s] English:** trilogies it was a real complete game and probably 20 times as many people played that part of it  
**Translation:** Vocabulary: crippled: 残缺不全; trilogies: 三部曲

**[6699.82s] English:** thought they had a great game had found fond memories of it but never paid us a dime but  
**Translation:** 

**[6705.70s] English:** enough people were happy with that where it was really quite successful and these early games  
**Translation:** 

**[6711.66s] English:** that we didn't think very much of compared to commercial quality and we didn't think very much  
**Translation:** 

**[6714.80s] English:** games but they were doing really good business some fairly crude things and people  
**Translation:** 

**[6720.00s] English:** It was good business. People enjoyed it, and it wasn't like you were taking a crapshoot on what you were getting. You just played a third of the experience, and you loved it enough to handwrite out a check and put it in an envelope and address it and send it out to Apogee to get the rest of them.  
**Translation:** 

**[6736.58s] English:** It was a really pretty feel-good business prospect there because everybody was happy. They knew what they were getting when they sent it in, and they would send in fan mail. If you're going to the trouble of addressing a letter and filling out an envelope, you write something in it, and there were just the literal bags of fan mail for the shareware games, so people loved them.  
**Translation:** Vocabulary: apogee: 顶峰; crapshoot: 赌博; handwrite: 手写

**[6758.82s] English:** I should mention that for you, the definition of wealth is being able to have pizza whenever you want.  
**Translation:** 

**[6766.58s] English:** For me, there was a dream because I would play shareware games over and over, the part that's free, over and over, and it was a very deeply fulfilling experience.  
**Translation:** Vocabulary: fulfilling: 满足的; shareware: 共享软件

**[6776.42s] English:** I dreamed of a time when I could actually afford the full experience, and this is kind of this dreamland beyond the horizon where you could find out what else is there.  
**Translation:** 

**[6789.04s] English:** In some sense, even just playing the shareware was the limitation.  
**Translation:** Vocabulary: dreamland: 梦幻之地

**[6796.58s] English:** The limitation of that. Life is limited. Eventually, we all die. In that way, shareware was somehow really fulfilling to have this kind of mysterious thing beyond what's free, what was there.  
**Translation:** 

**[6812.16s] English:** I don't know. Maybe it's because a part of my childhood is playing shareware games. That was a really fulfilling experience. It's so interesting how that model still brought joy to so many people, the 20x people that played it.  
**Translation:** 

**[6825.70s] English:** Yeah.  
**Translation:** 

**[6826.58s] English:** I'm very good about that. I would run into people that would say, oh, I loved that game that you had early on, Commander Keen, whatever. No, they meant just the first episode that they got to see everywhere.  
**Translation:** 

**[6838.56s] English:** That's me. I played the crap.  
**Translation:** 

**[6840.00s] English:** and that was all that was all good yeah yeah so we were in this position where scott miller was  
**Translation:** 

**[6847.02s] English:** just fronting us cash saying yeah make you know make a game but i we did not properly pull the  
**Translation:** 

**[6853.46s] English:** trigger and say all right we're going to we're quitting our jobs we were like we're going to do  
**Translation:** 

**[6857.24s] English:** both we're going to keep working at soft disk working on this and then we're going to go ahead  
**Translation:** 

**[6863.12s] English:** and make a new game for apogee at the same time and this eventually did lead to some legal problems  
**Translation:** Vocabulary: apogee: 顶点

**[6869.34s] English:** and we had uh we had trouble it all got worked out in the end but it was not a good call at the  
**Translation:** 

**[6874.66s] English:** time there and your legal mind at the time was not stellar you you were not thinking uh in terms of  
**Translation:** 

**[6881.62s] English:** in legal terms no i i definitely wasn't none of us were uh and in hindsight yeah it's like how did  
**Translation:** 

**[6887.82s] English:** we think we were going to get away with like even using our work computers to write uh write software  
**Translation:** Vocabulary: hindsight: 事后诸葛

**[6892.56s] English:** for you know our our breakaway uh new company it was not a good plan how did commander keen  
**Translation:** 

**[6899.32s] English:** come to be so the design process we would start from we had some idea of what we wanted to do we  
**Translation:** Vocabulary: breakaway: 脱离

**[6906.04s] English:** wanted to do a mario like game it was going to be a side scroller i was going to use the technology  
**Translation:** 

**[6911.56s] English:** we we had some sense of what it would have to look like because of the limitations of this adaptive  
**Translation:** Vocabulary: adaptive: 适应性; mario: 马里奥; scroller: 卷轴

**[6916.12s] English:** tile refresh technology it had to have fields of relatively constant tiles you couldn't just  
**Translation:** 

**[6921.86s] English:** paint up a background and then move that around i the early design or all the design for commander  
**Translation:** 

**[6928.26s] English:** keen really came from the design of the game and the design of the game was the design of the game  
**Translation:** 

**[6929.32s] English:** where he was uh you know he's kind of the main creative mind for the the early ed software stuff  
**Translation:** 

**[6936.88s] English:** where we had an interesting division of things where tom was all creative and design i was all  
**Translation:** 

**[6942.88s] English:** programming john romero was an interesting bridge where he was both a very good programmer and also  
**Translation:** Vocabulary: programmer: 程序员; romero: 罗梅罗

**[6948.14s] English:** a very good designer and artist and kind of straddled between the areas but commander keen  
**Translation:** 

**[6953.36s] English:** was very much tom hall's baby and he came up with all the design and backstory for the game and  
**Translation:** Vocabulary: backstory: 背景故事; straddled: 涉足

**[6959.32s] English:** for the different things  
**Translation:** 

**[6960.00s] English:** of kind of a mad scientist little kid with, you know, building a rocket ship and a zap gun and  
**Translation:** 

**[6967.42s] English:** visiting alien worlds and doing all of this that the background that we lay the game inside of.  
**Translation:** 

**[6973.76s] English:** And there's not a whole lot to any of these things. You know, design for us was always  
**Translation:** Vocabulary: alien: 外星的

**[6977.96s] English:** just what we needed to do to make the game that was going to be so much fun to play.  
**Translation:** 

**[6982.98s] English:** And we made our, we laid out our first trilogy of games, you know, the shareware formula is going to  
**Translation:** Vocabulary: shareware: 共享软件; trilogy: 三部曲

**[6988.26s] English:** be three pieces. We make Mannequin one, two, and three. And we just really started busting on all  
**Translation:** 

**[6995.12s] English:** that work. And it went together really quickly. It was like three months or something that while we  
**Translation:** Vocabulary: mannequin: 人体模型

**[7000.24s] English:** were still making games every month for Gamers Edge, we were sharing technology between that.  
**Translation:** 

**[7005.50s] English:** I'd write a bunch of code for this and we'd just kind of use it for both. Again, not a particularly  
**Translation:** 

**[7009.96s] English:** good idea there that had consequences for us. But in three months, we got our first game out.  
**Translation:** 

**[7017.06s] English:** And all of a sudden,  
**Translation:** 

**[7018.26s] English:** it was three times as successful as the most successful thing Apogee had had before. And we  
**Translation:** 

**[7023.24s] English:** were making like $30,000 a month immediately from the Commander Keen stuff. And that was,  
**Translation:** Vocabulary: apogee: 顶峰

**[7030.70s] English:** again, a surprise to us. It was more than we thought that that was going to make.  
**Translation:** 

**[7035.24s] English:** And we said, well, we're going to certainly roll into another set of titles from this.  
**Translation:** 

**[7039.94s] English:** And in that three months, I had come up with a much better way of doing the scrolling  
**Translation:** 

**[7043.86s] English:** technology that was not the adaptive tile refresh, which in some ways,  
**Translation:** Vocabulary: adaptive: 自适应; scrolling: 滚动

**[7048.14s] English:** was even simpler. And these things, so many of the great ideas of technology are things that are  
**Translation:** 

**[7054.26s] English:** back of the envelope designs. I make this comment about modern machine learning, where all the  
**Translation:** 

**[7059.44s] English:** things that are really important practically in the last decade, each of them fits on the back  
**Translation:** 

**[7063.74s] English:** of an envelope. There are these simple little things. They're not super dense, hard to understand  
**Translation:** 

**[7069.28s] English:** technologies. And so the second scrolling trick was just a matter of like, okay, we know we've  
**Translation:** 

**[7075.98s] English:** got this 64K window.  
**Translation:** 

**[7078.14s] English:** And the question was always like,  
**Translation:** 

**[7080.00s] English:** well you could make a two by two but you can't go off the edge uh but i finally asked well what  
**Translation:** 

**[7086.80s] English:** actually happens if you just go off the edge if you take your start and you say it's like okay  
**Translation:** 

**[7092.56s] English:** i can move over i'm scrolling i can move over i can move down i'm scrolling i get to what should  
**Translation:** 

**[7097.82s] English:** be the bottom of the memory window it's like well what if i just keep going and i say i'm going to  
**Translation:** 

**[7102.52s] English:** start at i you know what happens if i start at fff e at the very end of the the 64k block and it  
**Translation:** 

**[7109.60s] English:** turns out it just wraps back around to the top of the block and i'm like oh well this makes  
**Translation:** 

**[7114.80s] English:** everything easy you can just scroll the screen everywhere and all you have to draw is just one  
**Translation:** Vocabulary: scroll: 滚动

**[7119.00s] English:** new line of tiles whichever thing you expose it might be unaligned off various parts of the  
**Translation:** 

**[7125.06s] English:** of the screen memory but it just works that no longer had the problem of you had to have fields  
**Translation:** Vocabulary: unaligned: 未对齐; whichever: 无论哪个

**[7130.72s] English:** of the similar colors because you doesn't matter what you're doing you could be having a completely  
**Translation:** 

**[7135.68s] English:** unique world and you're just drawing the new strip as it comes on  
**Translation:** 

**[7139.60s] English:** might be like you said unaligned so it can be all over the place and it turns out it doesn't  
**Translation:** 

**[7144.62s] English:** matter i would have two page flipped screens as long as they didn't overlap they moved in series  
**Translation:** 

**[7148.96s] English:** through this uh two-dimensional window of graphics and that was one of those like well this is so  
**Translation:** 

**[7155.12s] English:** simple this just i this just works it's faster i am there it seemed like there was no downside  
**Translation:** 

**[7161.12s] English:** funny thing was i it turned out after we shipped titles with this there were what they called uh  
**Translation:** 

**[7169.60s] English:** the cards that would allow higher resolutions and i and different features that the standard ones  
**Translation:** Vocabulary: resolutions: 分辨率

**[7174.70s] English:** didn't and on some of those cards uh this was a weird compatibility quirk again because nobody  
**Translation:** 

**[7180.80s] English:** thought this was not what it was designed to do and some of those cards had more memory they had  
**Translation:** Vocabulary: compatibility: 兼容性; quirk: 怪异现象

**[7185.92s] English:** more than just 256k in four planes they had 512k or a megabyte and on some of those cards  
**Translation:** 

**[7192.94s] English:** i scroll my window down and then it goes into uninitialized memory that actually exists there  
**Translation:** Vocabulary: megabyte: 兆字节; uninitialized: 未初始化

**[7199.60s] English:** i think back  
**Translation:** 

**[7200.00s] English:** around to the top and then i was in the tough position of do i have to track every single one  
**Translation:** 

**[7205.90s] English:** of these and it was a madhouse back then with there were 20 different video card vendors with  
**Translation:** 

**[7210.88s] English:** all slightly different implementations of their non-standard functionality so either i needed to  
**Translation:** Vocabulary: functionality: 功能; implementations: 实现方式; madhouse: 乱七八糟

**[7216.02s] English:** natively program all of the vga cards there to map in that memory and keep scrolling down through  
**Translation:** 

**[7223.34s] English:** all of that or i kind of punted and took the easy solution of when you finally did run to the edge  
**Translation:** Vocabulary: natively: 本机; punted: 妥协; scrolling: 滚动

**[7229.16s] English:** of the screen i accepted a hitch and just copied the whole screen up there so on some of those  
**Translation:** 

**[7235.00s] English:** those cards it was a compatibility mode in the normal ones when it all worked fine everything  
**Translation:** Vocabulary: hitch: 故障

**[7240.38s] English:** was just beautifully smooth but if you had one of those cards where it did not wrap the way i  
**Translation:** 

**[7245.16s] English:** wanted it to you'd be scrolling around scrolling around and then eventually you'd have a little  
**Translation:** 

**[7250.18s] English:** hitch where 200 milliseconds or something that was not super smooth as it froze a little bit  
**Translation:** 

**[7255.78s] English:** and this was the binary thing is it one of the standards  
**Translation:** Vocabulary: binary: 二进制; milliseconds: 毫秒

**[7259.16s] English:** screens there isn't one of the weird ones the super vga ones yeah okay and so we would default  
**Translation:** 

**[7264.00s] English:** to and i think that was one of those that changed over the kind of course of deployment where early  
**Translation:** Vocabulary: deployment: 部署

**[7269.44s] English:** on we would have a normal mode and then you would have you would enable the compatibility flag if  
**Translation:** 

**[7273.68s] English:** your screen did this crazy flickery thing when you got to a certain point in the game uh and then  
**Translation:** Vocabulary: flickery: 闪烁不定

**[7278.98s] English:** later i think it probably got enabled by default as just more and more of the cards i kind of did  
**Translation:** 

**[7283.96s] English:** not do exactly the right thing and that's the two-edged sword of doing unconventional  
**Translation:** Vocabulary: unconventional: 不常规

**[7289.16s] English:** things with technology where you can find something that nobody thought about doing that  
**Translation:** 

**[7293.46s] English:** kind of scrolling trick when they set up those cards uh but the fact that nobody thought that  
**Translation:** 

**[7297.98s] English:** was the primary reason when i was relying on that then i wound up being broken on some of the later  
**Translation:** 

**[7303.08s] English:** cards let me uh take a bit of a tangent but uh ask you about the hacker ethic uh because you  
**Translation:** Vocabulary: hacker: 黑客; tangent: 旁白

**[7310.52s] English:** share where it's it's an interesting world the world of people that make money business and the  
**Translation:** 

**[7319.16s] English:** world of people that make money business and the world of people that make money builds  
**Translation:** 

**[7320.00s] English:** systems, the engineers. And what is the hacker ethic? You've been a man of the people and you've  
**Translation:** 

**[7329.10s] English:** embodied at least a part of that ethic. What does it mean? What did it mean to you at the time? What  
**Translation:** Vocabulary: embodied: 体现

**[7334.56s] English:** does it mean to you today? So Stephen Levy's book, Hackers, was a really formative book for me  
**Translation:** 

**[7340.18s] English:** as a teenager. I mean, I read it several times and there was all of the great lore of the early  
**Translation:** Vocabulary: hackers: 黑客

**[7346.56s] English:** MIT era of hackers and ending up at the end with, it kind of went through the early MIT hackers and  
**Translation:** 

**[7354.14s] English:** then the Silicon Valley hardware hackers and then the game hackers in part three. And at that time  
**Translation:** 

**[7360.36s] English:** as a teenager, I really was kind of bitter in some ways. Like I thought I was born too late. I  
**Translation:** 

**[7366.36s] English:** thought I missed the window there. And I really thought I belonged in that third section of that  
**Translation:** 

**[7372.28s] English:** book with the game hackers. And they were talking about, you know, the Williams at Sierra,  
**Translation:** 

**[7376.56s] English:** and Origin Systems with Richard Garriott. And it's like, I really wanted to be there. And I knew  
**Translation:** Vocabulary: garriott: 加里奥特

**[7383.22s] English:** that was now a few years in the past. It was not to be. But the early days, especially the early  
**Translation:** 

**[7391.18s] English:** MIT hacker days, talking a lot about this sense of the hacker ethic, that there was this sense that  
**Translation:** 

**[7397.32s] English:** it was about sharing information, being good, not keeping it to yourself, and that it's not a zero  
**Translation:** 

**[7403.90s] English:** sum game. That you, you know, you can share something, but you can't keep it to yourself.  
**Translation:** 

**[7406.54s] English:** You can't share something with another programmer, and it doesn't take it away from you. You know,  
**Translation:** 

**[7410.36s] English:** you, you then have somebody else doing something. And I also think that there's an aspect of it  
**Translation:** Vocabulary: programmer: 程序员

**[7415.88s] English:** where it's this ability to, to take joy in other people's accomplishments, where it's not the  
**Translation:** 

**[7421.82s] English:** cutthroat bit of like, I have to be first, I have to be recognized as the, the one that did this  
**Translation:** Vocabulary: cutthroat: 残酷竞争

**[7427.32s] English:** in some way. But being able to see somebody else do something and say, holy shit, that's amazing,  
**Translation:** 

**[7433.10s] English:** you know, and just taking joy in the ability of something.  
**Translation:** 

**[7436.54s] English:** It's amazing that somebody else does. And  
**Translation:** 

**[7440.00s] English:** The big thing that I was able to do through id Software was this ability to eventually release the source code for most of our, like, all of our really seminal game titles.  
**Translation:** Vocabulary: seminal: 开创性的

**[7450.76s] English:** And that was a, it was a stepping stone process where we were kind of surprised early on where people were able to hack the existing games.  
**Translation:** 

**[7460.04s] English:** And, of course, I had experience with that.  
**Translation:** 

**[7461.62s] English:** I remember hacking my copies of Ultima, so I'd give myself, you know, 9999 gold and raise my levels and, you know, break out the sector editor.  
**Translation:** 

**[7468.90s] English:** And so I was familiar with all of that.  
**Translation:** Vocabulary: hacking: 非法修改

**[7471.08s] English:** So it was just, it was with a smile when I started to see people doing that to our games.  
**Translation:** 

**[7475.54s] English:** I am, you know, making level editors for Commander Keen or hacking up Wolfenstein 3D.  
**Translation:** Vocabulary: wolfenstein: 狼人游戏

**[7481.60s] English:** But I made the pitch internally that we should actually release our own tools for, like, what we did, what we used to create the games.  
**Translation:** 

**[7491.18s] English:** And that was, you know, that was a little bit debatable about, well, you know, will this let other, will it give people a leg up?  
**Translation:** Vocabulary: internally: 内部

**[7497.86s] English:** It's always like, what's that?  
**Translation:** 

**[7498.90s] English:** What's that going to mean for the competition?  
**Translation:** 

**[7500.58s] English:** But the really hard pitch was to actually release the full source code for the games.  
**Translation:** 

**[7506.90s] English:** And it was a balancing act with the other people inside the company where it's interesting how the programmers generally did get, certainly the people that I worked closely with, they did kind of get that hacker ethic bit where you wanted to share your code.  
**Translation:** Vocabulary: balancing: 权衡; hacker: 黑客; programmers: 程序员

**[7524.74s] English:** You were proud of it.  
**Translation:** 

**[7525.76s] English:** You wanted other people to take it, do cool things with it.  
**Translation:** 

**[7528.90s] English:** But interestingly, the broader game industry is a little more hesitant to embrace that than, like, the group of people that we happen to have at id Software, where it was always a little interesting to me seeing how a lot of people in the game modding community were very possessive of their code.  
**Translation:** 

**[7547.64s] English:** They did not want to share their code.  
**Translation:** Vocabulary: hesitant: 犹豫; possessive: 占有

**[7549.30s] English:** They wanted it to be theirs.  
**Translation:** 

**[7550.54s] English:** It was their, you know, claim to fame.  
**Translation:** 

**[7552.50s] English:** And that was much more like what we tended to see with artists, where, you know, the artists understand something about.  
**Translation:** 

**[7558.58s] English:** Credit and I.  
**Translation:** 

**[7560.00s] English:** wanting it to be known as their work. And a lot of the game programmers felt a little bit more  
**Translation:** 

**[7566.24s] English:** like artists than like hacker programmers in that it was about building something that maybe felt  
**Translation:** 

**[7571.78s] English:** more like art to them than the more tool-based and exploration-based kind of hacking culture  
**Translation:** 

**[7577.74s] English:** side of things. It's so interesting that this kind of fear that credit will not be sufficiently  
**Translation:** Vocabulary: sufficiently: 足够地

**[7585.82s] English:** attributed to you. And that's one of the things that I do bump into a lot because I try not to go  
**Translation:** 

**[7593.62s] English:** clean. I mean, it's easy for me to say because so much credit is heaped on me for the id software  
**Translation:** Vocabulary: attributed: 归因于

**[7598.42s] English:** side of things. But when people come up and they want to pick a fight and say, no, it's like that  
**Translation:** 

**[7603.24s] English:** wasn't where first-person gaming came from. And you can point to some of things on obscure titles  
**Translation:** Vocabulary: obscure: 冷门作品

**[7610.12s] English:** that I was never aware of, or like the old Play-Doh systems, or each personal computer had something  
**Translation:** 

**[7615.80s] English:** that was 3D-ish and moving around. And I'm happy to say it's like, no, I mean, I saw Battlezone and  
**Translation:** Vocabulary: battlezone: 战斗地带

**[7622.48s] English:** Star Wars in the arcades. I had seen 3D graphics. I had seen all these things. I'm standing on the  
**Translation:** 

**[7627.54s] English:** shoulders of lots of other people. But sometimes these examples they pull out, it's like, nah,  
**Translation:** 

**[7631.24s] English:** I didn't know that existed. I mean, I had never heard of that before then. That didn't contribute  
**Translation:** 

**[7636.14s] English:** to what I made, but there's plenty of stuff that did. And I think there's good cases to be made  
**Translation:** 

**[7643.20s] English:** that obviously Doom and Quake and Wolfenstein...  
**Translation:** 

**[7645.80s] English:** were formative examples for everything that came after that. But I don't feel the need to go fight  
**Translation:** Vocabulary: wolfenstein: 狼穴游戏

**[7654.12s] English:** and say, claim primacy or initial invention of anything like that. But a lot of people do want  
**Translation:** 

**[7659.96s] English:** to. I think when you fight for the credit in that way, and it does go against the hacker ethic,  
**Translation:** Vocabulary: hacker: 黑客; primacy: 优先权

**[7666.00s] English:** you destroy something fundamental about the culture, about the community that builds cool  
**Translation:** 

**[7670.70s] English:** stuff. I think credit ultimately...  
**Translation:** 

**[7673.26s] English:** So I had this sort of, there's a famous wrestling  
**Translation:** 

**[7680.00s] English:** freestyle wrestling called uh and he always preached that you should just focus  
**Translation:** Vocabulary: freestyle: 自由式; preached: 宣扬; wrestling: 摔跤

**[7687.68s] English:** on the art of the wrestling and let people um write your story however they want uh the  
**Translation:** 

**[7697.04s] English:** the the highest form of the art is just focusing on the art and that's something that is something  
**Translation:** 

**[7701.92s] English:** about the the hacker ethic is just focus on building cool stuff sharing it with other cool  
**Translation:** 

**[7708.16s] English:** people and credit will get assigned correctly uh in the long arc of history yeah and i generally  
**Translation:** 

**[7718.06s] English:** think that's true and you've got i am you know like there's some things there is there's a  
**Translation:** 

**[7723.28s] English:** graphics technique that got labeled carmax reverse i am you know literally named it and it  
**Translation:** 

**[7728.68s] English:** turned out that i wasn't the first person to to figure that out like most scientific things or  
**Translation:** 

**[7733.50s] English:** mathematical things you might have it's like oh this other person had actually done that somewhat  
**Translation:** Vocabulary: mathematical: 数学的

**[7738.16s] English:** and then there's things that get attributed to me like the inverse square root hack that i actually  
**Translation:** 

**[7742.60s] English:** didn't do i flat out that wasn't me and it's like it's weird how the memetic power of the internet  
**Translation:** Vocabulary: attributed: 归因; inverse: 倒数

**[7747.76s] English:** i cannot you're like the mark point of programming yes it's just everything just gets attributed to  
**Translation:** 

**[7753.54s] English:** you now even though you've never sought that the credit of things i mean but part of the the fact  
**Translation:** 

**[7759.72s] English:** that the humility behind that is what uh attracts the attributions let's talk about a game you mean  
**Translation:** 

**[7768.16s] English:** one of the greatest games ever made i know you could talk about doing quake and so on but to me  
**Translation:** Vocabulary: attributions: 归因; humility: 谦逊

**[7771.82s] English:** wolfenstein 3d was like wow it blew my mind that that world like this could exist so how did  
**Translation:** 

**[7779.06s] English:** wolfenstein 3d come to be uh in terms of the programming in terms of the design in terms of  
**Translation:** Vocabulary: wolfenstein: 狼穴游戏

**[7784.66s] English:** some of the memorable technical challenges um and also actually just something you haven't mentioned  
**Translation:** 

**[7790.52s] English:** you know how do these ideas come to be inside your mind  
**Translation:** 

**[7798.16s] English:** the adaptive side scrolling  
**Translation:** 

**[7800.00s] English:** So the solutions to these technical challenges.  
**Translation:** Vocabulary: adaptive: 适应性; scrolling: 滚动

**[7803.10s] English:** So I usually can introspectively pull back pretty detailed accounts of how technology solutions and design choices on my part came to be where I technically we had done two games, 3D games like that before, where Hover Tank was the first one, which had flat shaded walls, but did have the scaled enemies inside it.  
**Translation:** 

**[7825.12s] English:** And then Catacombs 3D, which had textured walls, scaled enemies, and some more functionality like the disappearing walls and some other stuff.  
**Translation:** Vocabulary: catacombs: 墓穴; functionality: 功能; introspectively: 反思地

**[7836.76s] English:** But what's really interesting from a game development standpoint is those games, Catacombs 3D, Hover Tank, and Wolfenstein, they literally used the same code for a lot of the character behavior that a 2D game that I had made earlier called Catacombs did.  
**Translation:** 

**[7853.88s] English:** Where it was an overhand.  
**Translation:** Vocabulary: standpoint: 观点

**[7855.12s] English:** It was an overhead view game, kind of like Gauntlet.  
**Translation:** 

**[7856.82s] English:** You're running around and you can open up doors, pick up items, basic game stuff.  
**Translation:** Vocabulary: gauntlet: 手套赛

**[7861.38s] English:** And the thought was that this exact same game experience just presented in a different perspective.  
**Translation:** 

**[7869.08s] English:** It could be literally the same game, just with a different view into it, would have a dramatically different impact on the players.  
**Translation:** Vocabulary: dramatically: 极大地

**[7876.76s] English:** So it wasn't a true 3D.  
**Translation:** 

**[7880.18s] English:** You're saying that you could kind of fake it.  
**Translation:** 

**[7882.60s] English:** You can scale enemies, meaning things that are far.  
**Translation:** 

**[7885.12s] English:** They're away.  
**Translation:** 

**[7885.82s] English:** You can make them smaller.  
**Translation:** 

**[7887.64s] English:** So the game was a 2D map.  
**Translation:** 

**[7889.88s] English:** All of our games use the same tool for creation.  
**Translation:** 

**[7892.92s] English:** We use the same map editor for creating Keen as Wolfenstein and Hover Tank and Catacombs and all this stuff.  
**Translation:** 

**[7899.20s] English:** So the game was a 2D grid made out of blocks.  
**Translation:** 

**[7902.86s] English:** And you could say, well, these are walls.  
**Translation:** 

**[7904.52s] English:** These are where the enemies start.  
**Translation:** 

**[7905.92s] English:** Then they start moving around.  
**Translation:** 

**[7907.80s] English:** And these early games like Catacombs, you played it strictly in a 2D view.  
**Translation:** 

**[7911.56s] English:** It was a scrolling 2D view.  
**Translation:** 

**[7913.30s] English:** And that was kind of using an adaptive tile refresh.  
**Translation:** 

**[7915.08s] English:** At the time, to be able to do something like that.  
**Translation:** 

**[7918.56s] English:** And then the.  
**Translation:** 

**[7920.00s] English:** that these early games all it did was take the same basic enemy logic but instead of seeing it  
**Translation:** 

**[7925.68s] English:** from the god's eye view on top you were inside it and turning from side to side yawing your view and  
**Translation:** 

**[7931.40s] English:** moving forwards and backwards and side to side uh and it's a striking thing where you always talk  
**Translation:** Vocabulary: backwards: 前后; yawing: 摇晃

**[7936.92s] English:** about wanting to isolate and factor changes in values and this was one of those most pure cases  
**Translation:** 

**[7941.98s] English:** there where the rest of the game changed very little it was our normal kind of change the colors  
**Translation:** 

**[7947.10s] English:** on something and draw a different picture for it but it's kind of the same thing but the perspective  
**Translation:** 

**[7951.64s] English:** changed in a really fundamental way and it was dramatically different i can remember the reactions  
**Translation:** 

**[7957.96s] English:** where the artist uh adrian that had been drawing the pictures for we had a cool big troll thing in  
**Translation:** 

**[7963.66s] English:** catacombs 3d and we had uh these walls that you could get a key and you could make the blocks  
**Translation:** 

**[7969.08s] English:** disappear get really simple stuff blocks could either be there or not there so our idea of a  
**Translation:** 

**[7974.16s] English:** door was being able to make a set of blocks just disappear  
**Translation:** 

**[7977.10s] English:** and i remember the reaction where he had drawn these characters and he was slowly moving around  
**Translation:** 

**[7981.62s] English:** and like people had no experience with 3d navigation it was all still keyboard we didn't  
**Translation:** 

**[7985.70s] English:** even have mice i am set up at that time but slowly moving going up picked up a key go to a wall the  
**Translation:** 

**[7992.40s] English:** wall disappears in a little animation and there's a monster like right there and he practically fell  
**Translation:** 

**[7997.34s] English:** out of his chair it was just like ah and games just didn't do that you know the games were the  
**Translation:** 

**[8003.52s] English:** god's eye view you were a little invested in your little guy you can be like  
**Translation:** 

**[8007.10s] English:** you know happy or sad when things happen but you just did not get that kind of startle reaction  
**Translation:** 

**[8012.36s] English:** you weren't inside your face something in the back of your brain some reptile brain thing is just  
**Translation:** Vocabulary: reptile: 爬行动物

**[8017.30s] English:** going oh shit something just happened and that was one of those early points where it's like  
**Translation:** 

**[8022.50s] English:** yeah this is going to make a difference this is going to be powerful and it's going to matter  
**Translation:** 

**[8027.30s] English:** were you able to imagine that in the idea stage or no so not that exact thing so again we had  
**Translation:** 

**[8034.64s] English:** cases like the arcade games battle zone and the arcade games battle zone and the arcade games battle  
**Translation:** Vocabulary: arcade: 街机

**[8037.10s] English:** zone and star wars that you could kind of see a 3d world  
**Translation:** 

**[8040.00s] English:** and things coming at you and you get some sense of it but nothing had done the kind of worlds that  
**Translation:** 

**[8045.66s] English:** we were doing and the sort of action-based things 3d at the time was really largely about the  
**Translation:** 

**[8052.48s] English:** simulation thoughts and this is something that really might have trended differently if not for  
**Translation:** Vocabulary: simulation: 模拟

**[8058.96s] English:** the id software approach in the games where there were flight simulators there were driving  
**Translation:** 

**[8064.12s] English:** simulators you had like hard drive in and microsoft flight simulator and these were doing 3d and  
**Translation:** Vocabulary: simulator: 模拟器; simulators: 模拟器

**[8070.04s] English:** general purpose 3d and ways that were more flexible than what we were doing with our games but they  
**Translation:** 

**[8076.12s] English:** were looked at as simulations they weren't trying to necessarily be fast or responsive i you know  
**Translation:** 

**[8082.12s] English:** letting you do kind of exciting maneuvers because they were trying to simulate reality and they were  
**Translation:** 

**[8087.06s] English:** taking their cues from the big systems the evans and sutherlands and the silicon graphics that  
**Translation:** Vocabulary: maneuvers: 操作; simulate: 模拟

**[8091.60s] English:** were doing things but we were taking our  
**Translation:** 

**[8094.10s] English:** cues from the console and arcade games you know we wanted things that were sort of quarter eaters  
**Translation:** 

**[8099.40s] English:** that were doing fast-paced things that you could smack you around rather than just smoothly gliding  
**Translation:** 

**[8104.12s] English:** you from place to place so quarter yeah and you know a funny thing is so much that that built into  
**Translation:** Vocabulary: smack: 拍打

**[8111.88s] English:** us that wolfenstein still had lives and you had like one of the biggest power-ups in all these  
**Translation:** 

**[8116.96s] English:** games like was an extra life because you started off with three lives and you lose your lives and  
**Translation:** Vocabulary: wolfenstein: 狼穴游戏

**[8121.68s] English:** then it's game over and there weren't save  
**Translation:** 

**[8124.00s] English:** games and you had like one of the biggest power-ups in all these games like was an extra  
**Translation:** 

**[8124.08s] English:** in most of this stuff it was it sounds almost crazy to say this but it was an innovation in  
**Translation:** 

**[8130.24s] English:** doom to not have lives you know you could just play doom as long as you wanted you just restart  
**Translation:** 

**[8134.48s] English:** at the the start of the level and why not this is like we we aren't trying to take people's  
**Translation:** 

**[8139.34s] English:** quarters they've already paid for the entire game we want them to have a good time and you would  
**Translation:** 

**[8143.96s] English:** have some i you know some old-timer purists that might think that there's something to the epic  
**Translation:** 

**[8148.40s] English:** journey of making it to the end having to restart all the way from the beginning after a certain  
**Translation:** Vocabulary: purists: 守旧派

**[8152.56s] English:** number of tries but no i don't think that's the case i don't think that's the case i don't think  
**Translation:** 

**[8153.98s] English:** more fun is had when you just let people kind of keep trying when they're stuck rather than having  
**Translation:** 

**[8158.64s] English:** to go all the way back and  
**Translation:** 

**[8160.00s] English:** learn different things. So you've recommended the book Game Engine Black Book Wolfenstein 3D for  
**Translation:** 

**[8165.88s] English:** technical exploration of the game. So looking back 30 years, what are some memorable technical  
**Translation:** 

**[8172.20s] English:** innovations that made this perspective shift into this world that's so immersive that scares you  
**Translation:** Vocabulary: immersive: 身临其境; innovations: 创新

**[8178.54s] English:** when a monster appears? What were some things you had to solve? So one of the interesting things  
**Translation:** 

**[8184.06s] English:** that come back to the theme of deadlines and resource constraints, the game Catacombs 3D  
**Translation:** Vocabulary: catacombs: 地下墓穴; constraints: 限制条件; deadlines: 截止日期

**[8189.68s] English:** we shipped, we were supposed to be shipping this for Gamers Edge on a monthly cadence and I had  
**Translation:** 

**[8195.92s] English:** slipped. I was actually late. It slipped like six weeks because this was texture mapped walls doing  
**Translation:** Vocabulary: cadence: 频率

**[8201.80s] English:** stuff that I hadn't done before. And at the six week point, it was still kind of glitchy and buggy.  
**Translation:** 

**[8209.04s] English:** There were things that I knew that if you had a wall that was like almost edge on, you could slide  
**Translation:** Vocabulary: buggy: 程序有 Bug

**[8213.94s] English:** over to it and you could see some things freak out or vanish or not work. And I hated that. I  
**Translation:** 

**[8219.38s] English:** am.  
**Translation:** 

**[8219.68s] English:** But I was up against the wall. We had to ship the game. It was still a lot of fun to play. It was  
**Translation:** 

**[8224.84s] English:** novel. Nobody had seen it. It gave you that startle reflex reaction. So it was worth shipping,  
**Translation:** Vocabulary: reflex: 条件反射

**[8231.00s] English:** but it had these things that I knew were kind of flaky and janky and not what I was really proud of.  
**Translation:** 

**[8237.56s] English:** So one of the things that I did very differently in Wolfenstein was I went,  
**Translation:** Vocabulary: flaky: 不稳定的; wolfenstein: 狼穴

**[8244.04s] English:** Catacombs used almost a conventional thing where you had segments that were one dimensional  
**Translation:** 

**[8249.48s] English:** puzzles. And I had to ship them. And I had to ship them. And I had to ship them. And I had to ship them.  
**Translation:** Vocabulary: segments: 部分

**[8249.66s] English:** And I had to ship them. And I had to ship them. And I had to ship them. And I had to ship them. And I had to ship them.  
**Translation:** 

**[8249.86s] English:** basically that were clipped and backfaced and done kind of like a very crude 3D engine from the  
**Translation:** Vocabulary: backfaced: 背面渲染

**[8256.62s] English:** professionals. But I wasn't getting it done right. I was not doing a good enough job. I didn't really  
**Translation:** 

**[8262.32s] English:** have line of sight to fix it right. There's stuff that, of course, I look back, it's like, oh, it's  
**Translation:** 

**[8267.42s] English:** obvious how to do this and do the math right, do your clipping right, check all of this, how you  
**Translation:** 

**[8272.10s] English:** handle the precision. But I did not know how to do that at that time.  
**Translation:** Vocabulary: clipping: 剪辑正确

**[8275.70s] English:** Was that the first 3D engine you wrote, Catacombs 3D?  
**Translation:** 

**[8278.74s] English:** Yeah.  
**Translation:** 

**[8279.24s] English:** Yeah.  
**Translation:** 

**[8279.36s] English:** Supertank had been a  
**Translation:** Vocabulary: supertank: 超级战舰

**[8280.00s] English:** little bit before that but that had the flat shaded walls so the texture mapping on the walls  
**Translation:** 

**[8284.46s] English:** was what was bringing in some of these challenges that was uh that was hard for me and i couldn't  
**Translation:** 

**[8289.44s] English:** solve it right at the time can you describe what flat shading is and texture mapping so in the the  
**Translation:** 

**[8294.46s] English:** walls were solid color one of 16 colors i'm in hover tank so that's easy it's fast you just  
**Translation:** 

**[8301.12s] English:** draw the solid color for everything texture mapping is what we all see today where you have  
**Translation:** 

**[8306.00s] English:** an image that is stretched and distorted onto the walls or the surfaces that you're working with  
**Translation:** Vocabulary: distorted: 变形

**[8310.86s] English:** um and it was you know it was a long time for me to just figure out how to do that without it  
**Translation:** 

**[8316.72s] English:** distorting in the wrong ways and and i did not get it all exactly right in catacombs and i i had these  
**Translation:** Vocabulary: catacombs: 墓穴; distorting: 失真

**[8323.48s] English:** flaws so that was important enough to me that rather than continuing to bang my head on that  
**Translation:** 

**[8329.32s] English:** when i wasn't positive i was going to get it i went with a completely different approach for  
**Translation:** 

**[8333.78s] English:** drawing for figuring out where the wall  
**Translation:** 

**[8335.98s] English:** was which was a ray casting approach which i had done in catacombs 3d i had a bunch of c code  
**Translation:** 

**[8342.60s] English:** trying to make this work right and it wasn't working right in wolfenstein i wound up going to  
**Translation:** 

**[8348.04s] English:** a very small amount of assembly code so in some ways there should be a slower way of doing it  
**Translation:** 

**[8354.16s] English:** but by making it a smaller amount of work that i could more tightly optimize  
**Translation:** 

**[8358.02s] English:** it worked out and wolfenstein 3d was just absolutely rock solid you know it was  
**Translation:** Vocabulary: optimize: 优化; wolfenstein: 狼人巴菲

**[8363.26s] English:** you know nothing glitched in there the game  
**Translation:** 

**[8365.86s] English:** was just absolutely rock solid you know it was you know nothing glitched in there the game just  
**Translation:** Vocabulary: glitched: 卡顿

**[8365.96s] English:** was pretty much flawless through all of that and i was super proud of that um but eventually like  
**Translation:** 

**[8372.40s] English:** in the later games i went back to the more span based things where i could get more total efficiency  
**Translation:** Vocabulary: flawless: 完美无缺

**[8377.22s] English:** once i really did figure out how to do it so there were two sort of key technical things to  
**Translation:** 

**[8382.78s] English:** wolfenstein one was this ray casting approach which you still to this day you see people go  
**Translation:** 

**[8388.44s] English:** and say let's write a ray casting engine because it's an understandable way of doing things that  
**Translation:** 

**[8393.28s] English:** lets you make games very much like that so you see ray casters in javascript ray casters in python  
**Translation:** Vocabulary: understandable: 容易理解的

**[8398.66s] English:** people that are are  
**Translation:** 

**[8400.00s] English:** basically going and re-implementing that approach to taking a tiled world and casting out into it.  
**Translation:** 

**[8406.50s] English:** It works pretty well, but it's not the fastest way of doing it.  
**Translation:** 

**[8409.28s] English:** Can you describe what ray casting is?  
**Translation:** 

**[8411.18s] English:** So you start off and you've got your screen, which is 320 pixels across at the time,  
**Translation:** 

**[8415.76s] English:** if you haven't sized down the window for greater speed. And at every pixel, there's going to be an  
**Translation:** Vocabulary: pixel: 像素; pixels: 像素

**[8421.84s] English:** angle from you've got your position in the world, and you're going to just run along that angle  
**Translation:** 

**[8426.48s] English:** and keep going until you hit a block. So up to 320 times across there, it's going to throw a  
**Translation:** 

**[8433.12s] English:** cast array out into the world from wherever your origin is until it runs into a wall,  
**Translation:** 

**[8438.64s] English:** and then it can figure out exactly where on the wall it hits. The performance challenge of that  
**Translation:** 

**[8443.64s] English:** is as it's going out, every block it's crossing, it checks, is this a solid wall? So that means  
**Translation:** 

**[8449.96s] English:** that in the early Wolfenstein levels, you're in a small jail cell going out into a small hallway.  
**Translation:** Vocabulary: hallway: 走廊

**[8455.76s] English:** It's super effective.  
**Translation:** 

**[8456.48s] English:** It's super efficient for that because you're only stepping across three or four blocks. But then if  
**Translation:** 

**[8460.66s] English:** somebody makes a room that covers, our maps were limited to 64 by 64 blocks. If you made one room  
**Translation:** 

**[8467.00s] English:** that was nothing but walls at the far space, it would go pretty slow because it would be stepping  
**Translation:** 

**[8471.90s] English:** across 80 tile tests or something along the way.  
**Translation:** 

**[8476.02s] English:** By the way, the physics of our universe seems to be competing in this very thing. So this  
**Translation:** 

**[8479.34s] English:** maps nicely to the actual physics of our world.  
**Translation:** 

**[8483.08s] English:** Yeah, you get-  
**Translation:** 

**[8483.82s] English:** Intuitively.  
**Translation:** 

**[8484.10s] English:** I follow a little bit of something like Stephen Wolfram's,  
**Translation:** Vocabulary: intuitively: 直觉地

**[8486.48s] English:** work on interconnected network information states of that. And it's beyond what I can have  
**Translation:** 

**[8493.36s] English:** an informed opinion on, but it's interesting that people are considering things like that and have  
**Translation:** Vocabulary: interconnected: 相互连接

**[8499.08s] English:** things that can back it up. Yeah, there's whole different sets of interesting stuff there.  
**Translation:** 

**[8505.70s] English:** So Wolfenstein 3D had raycasting.  
**Translation:** Vocabulary: raycasting: 射线投射; wolfenstein: 狼穴

**[8508.28s] English:** So raycasting. And then the other kind of key aspect was what I called compiled scalars,  
**Translation:** 

**[8513.80s] English:** where the idea of,  
**Translation:** Vocabulary: compiled: 编译过的; scalars: 标量

**[8516.48s] English:** you saw this in the earlier classic arcade games like-  
**Translation:** 

**[8520.00s] English:** Space Harrier and stuff where you would take a picture, which is normally drawn directly on the  
**Translation:** Vocabulary: arcade: 街机游戏

**[8524.98s] English:** screen. And then if you have the ability to make it bigger or smaller, big chunky pixels or physically  
**Translation:** 

**[8529.86s] English:** small drop sampled pixels, that's the fundamental aspect of what our characters were doing in these  
**Translation:** Vocabulary: chunky: 粗像素

**[8535.72s] English:** 3D games. You would have, it's just like you might've drawn a tiny little character, but now  
**Translation:** 

**[8539.66s] English:** we can make them really big and make them really small and move it around. That was the limited  
**Translation:** 

**[8544.08s] English:** kind of 3D that we had for characters. To make them turn, there were literally eight different  
**Translation:** 

**[8548.48s] English:** views of them. You didn't actually have a 3D model that would rotate. You just had these cardboard  
**Translation:** Vocabulary: cardboard: 纸板; rotate: 旋转

**[8552.80s] English:** cutouts, but that was good enough for that startle fight reaction. And it was kind of what we had to  
**Translation:** 

**[8558.64s] English:** deal with there. So a straightforward approach to do that, you could just write out your doubly  
**Translation:** Vocabulary: cutouts: 剪裁图案; straightforward: 直截了当

**[8563.80s] English:** nested loop of, you've got your stretch factor and it's like, you've got a point, you stretch by a  
**Translation:** 

**[8568.90s] English:** little bit and it might be on the same pixel. It might be on the next pixel. It might've skipped a  
**Translation:** Vocabulary: pixel: 像素

**[8572.32s] English:** pixel. You can write that out, but it's not going to be fast enough where especially you get a  
**Translation:** 

**[8578.48s] English:** right in your face monster covering almost the entire screen. Doing that with a general purpose  
**Translation:** 

**[8583.76s] English:** scaling routine would have just been much too slow. It would have worked when they're small  
**Translation:** 

**[8587.60s] English:** characters, but then it would get slower and slower as they got closer to you until right  
**Translation:** 

**[8591.66s] English:** at the time when you most care about having a fast reaction time, the game would be chunking down.  
**Translation:** 

**[8597.40s] English:** So the fastest possible way to draw pixels at that time was to, instead of saying,  
**Translation:** Vocabulary: chunking: 分块处理; pixels: 像素

**[8606.04s] English:** I've got a general purpose, I am...  
**Translation:** 

**[8608.48s] English:** Version that can handle any scale. I used a program to make essentially a hundred or more  
**Translation:** 

**[8616.30s] English:** separate little programs that was optimized for, I will take an image and I will draw it 12 pixels  
**Translation:** 

**[8621.74s] English:** tall. I'll take an image, I'll draw it 14 pixels tall, up by every two pixels even for that. So you  
**Translation:** 

**[8628.02s] English:** would have the most optimized code so that in the normal case where most of the world is fairly  
**Translation:** 

**[8634.14s] English:** large, like the pixels are big, we did not have a lot of memory.  
**Translation:** Vocabulary: optimized: 优化过的

**[8638.48s] English:** So in most cases...  
**Translation:** 

**[8640.00s] English:** that meant that you would load a pixel color  
**Translation:** 

**[8642.38s] English:** and then you would store it multiple times.  
**Translation:** 

**[8645.10s] English:** So that was faster than even copying an image  
**Translation:** 

**[8648.90s] English:** in a normal conventional case  
**Translation:** 

**[8650.56s] English:** because most of the time the image is expanded.  
**Translation:** 

**[8653.38s] English:** So instead of doing one read, one write for a simple copy,  
**Translation:** 

**[8656.32s] English:** you might be doing one read and three or four writes  
**Translation:** 

**[8659.04s] English:** as it got really big.  
**Translation:** 

**[8660.72s] English:** And that had the beneficial aspect  
**Translation:** 

**[8662.20s] English:** of just when you needed the performance most,  
**Translation:** 

**[8664.34s] English:** when things are covering the screen,  
**Translation:** 

**[8665.86s] English:** it was giving you the most acceleration for that.  
**Translation:** 

**[8668.40s] English:** And by the way, were you able to understand this  
**Translation:** Vocabulary: acceleration: 加速度

**[8672.40s] English:** through thinking about it  
**Translation:** 

**[8673.74s] English:** or were you testing like the right speed?  
**Translation:** 

**[8676.18s] English:** So this again comes back to,  
**Translation:** 

**[8678.34s] English:** I can find the antecedents for things like this.  
**Translation:** Vocabulary: antecedents: 先行词

**[8681.40s] English:** So back in the Apple II days,  
**Translation:** 

**[8685.08s] English:** the graphics were essentially single bits at a time.  
**Translation:** 

**[8689.78s] English:** And if you wanted to make your little spaceship,  
**Translation:** 

**[8691.76s] English:** if you wanted to make it smoothly go across the world,  
**Translation:** 

**[8694.88s] English:** if you just took the image  
**Translation:** 

**[8695.98s] English:** and you drew it out at the next location,  
**Translation:** 

**[8697.64s] English:** you would move by seven pixels at a time.  
**Translation:** 

**[8699.92s] English:** So it would go chunk, chunk, chunk.  
**Translation:** 

**[8701.18s] English:** If you wanted to make it move smoothly,  
**Translation:** 

**[8703.10s] English:** you actually had to make seven versions of the ship  
**Translation:** 

**[8705.70s] English:** that were pre-shifted.  
**Translation:** 

**[8707.28s] English:** You could write a program that would shift it dynamically,  
**Translation:** Vocabulary: dynamically: 动态地

**[8709.86s] English:** but on a one megahertz processor,  
**Translation:** 

**[8711.32s] English:** that's not going anywhere fast.  
**Translation:** Vocabulary: megahertz: 兆赫; processor: 处理器

**[8713.16s] English:** So if you wanted to do a smooth moving fast action game,  
**Translation:** 

**[8716.62s] English:** you made separate versions of each of these sprites.  
**Translation:** Vocabulary: sprites: 精灵图

**[8720.38s] English:** Now there were a few more tricks you could pull  
**Translation:** 

**[8722.28s] English:** that if it still wasn't fast enough,  
**Translation:** 

**[8724.46s] English:** you could make a compiled shape  
**Translation:** 

**[8726.70s] English:** where,  
**Translation:** Vocabulary: compiled: 编译后的

**[8727.22s] English:** instead of this program that normally copies an image  
**Translation:** 

**[8730.88s] English:** and it says like,  
**Translation:** 

**[8731.72s] English:** get this byte from here,  
**Translation:** 

**[8732.92s] English:** store it here,  
**Translation:** 

**[8733.46s] English:** get this byte,  
**Translation:** 

**[8734.00s] English:** store this byte.  
**Translation:** 

**[8735.00s] English:** If you've got the memory space,  
**Translation:** 

**[8737.22s] English:** you could say,  
**Translation:** 

**[8738.10s] English:** I'm going to write the program  
**Translation:** 

**[8739.46s] English:** that does nothing but draw this shape.  
**Translation:** 

**[8741.66s] English:** It's going to be like,  
**Translation:** 

**[8742.76s] English:** I'm going to load the immediate value 25,  
**Translation:** 

**[8746.12s] English:** you know, which is some bit pattern.  
**Translation:** 

**[8747.66s] English:** And then I'm going to store that at this location,  
**Translation:** 

**[8751.04s] English:** rather than loading something from memory  
**Translation:** 

**[8752.96s] English:** that involved indexing registers  
**Translation:** 

**[8755.10s] English:** and this other slow stuff,  
**Translation:** 

**[8756.56s] English:** you could go,  
**Translation:** 

**[8757.10s] English:** go ahead and say,  
**Translation:** 

**[8757.72s] English:** no, I'm going to hard code the exact values  
**Translation:** 

**[8760.00s] English:** all of the image right into the program and this was always a horrible trade-off there but you  
**Translation:** 

**[8764.28s] English:** didn't have much memory and you didn't have much speed but if you had something that you wanted to  
**Translation:** 

**[8768.44s] English:** go really fast you could turn it into a program and that was you know knowing about that technique  
**Translation:** 

**[8774.44s] English:** is what made me think about some of these unwinding it for the pc where people that didn't come from  
**Translation:** 

**[8779.86s] English:** that background were less likely to think about that i mean there's some deep parallels probably  
**Translation:** 

**[8785.52s] English:** to human cognition as well there's something about optimizing and compressing  
**Translation:** Vocabulary: cognition: 认知; compressing: 压缩; optimizing: 优化

**[8792.40s] English:** the the processing of a new information that requires you to predict the possible ways  
**Translation:** 

**[8799.54s] English:** in which the game or the world might unroll and you have something like compiled scalers always  
**Translation:** Vocabulary: scalers: 缩放器; unroll: 展开

**[8806.78s] English:** there so you have like optimal like you have a prediction of how the world will unroll and you  
**Translation:** 

**[8812.90s] English:** have some kind of optimized  
**Translation:** Vocabulary: optimal: 最佳; optimized: 优化

**[8815.10s] English:** you have a prediction of how the world will unroll and you have some kind of optimized  
**Translation:** 

**[8815.52s] English:** data structure for that prediction and then you can modify if the world turns out to be different  
**Translation:** 

**[8820.98s] English:** you can modify a slight way as far as building out techniques so much of the brain is about  
**Translation:** 

**[8825.50s] English:** the associative context you know they're just when you learn something it's in the context of  
**Translation:** Vocabulary: associative: 联想的

**[8830.12s] English:** something else and you can have faint tiny little hints of things and i do think there are some deep  
**Translation:** 

**[8835.48s] English:** things uh you know around like sparse distributed memories and boosting that's like if you can just  
**Translation:** Vocabulary: boosting: 增强; sparse: 稀疏

**[8839.72s] English:** be slightly above the noise floor of having some hint of something you can have things refined into  
**Translation:** 

**[8845.06s] English:** pulling that out of your brain and then you can modify it and then you can modify it and then you  
**Translation:** Vocabulary: refined: 精炼

**[8845.50s] English:** the memory back up so having a being a programmer and having a toolbox of like all of these things  
**Translation:** 

**[8850.68s] English:** that things that i did in all of these previous lives of programming tasks that still matters to  
**Translation:** Vocabulary: programmer: 程序员; toolbox: 工具箱

**[8855.90s] English:** me about how i'm able to pull up some of these things like in that case it was something i did  
**Translation:** 

**[8860.30s] English:** on the apple to then being relevant for the pc and i have still cases when i would when i would  
**Translation:** 

**[8866.36s] English:** work on mobile development then be like okay i i did something like this back in the the doom days  
**Translation:** 

**[8871.64s] English:** but now it's a different environment but i have still had that tie i can bring it back to the  
**Translation:** 

**[8875.50s] English:** in and i can transform it into what the world needs right now and i i do think that  
**Translation:** 

**[8880.00s] English:** actually one of the very core things with human cognition and brain-like functioning is finding  
**Translation:** 

**[8886.88s] English:** these ways about, your brain is kind of everything everywhere all at once. It is just a set of all  
**Translation:** 

**[8892.48s] English:** of this stuff that is just fetched back by these queries that go into it. And they can just be  
**Translation:** 

**[8897.42s] English:** slightly above the noise floor with random noise in your neurons and synapses that are affecting  
**Translation:** 

**[8901.82s] English:** exactly what gets pulled up. So you're saying some of these very specific solutions for different  
**Translation:** Vocabulary: neurons: 神经元; synapses: 突触

**[8907.04s] English:** games, you find that there's a kernel of a deep idea that's generalizable to other things.  
**Translation:** 

**[8914.74s] English:** Yeah. You can't predict what it's going to be, but that idea of like, I called out that compiled  
**Translation:** Vocabulary: compiled: 整理好的代码; generalizable: 可推广的; kernel: 核心

**[8919.00s] English:** shaders in the forward that I wrote for that, the Game Engine Black Book, as this is, it's kind of  
**Translation:** 

**[8925.46s] English:** an endpoint of unrolling code, but that's one of those things that thinking about that and having  
**Translation:** Vocabulary: endpoint: 终点; shaders: 着色器; unrolling: 展开

**[8930.74s] English:** that in your mind. And I'm sure there are some programmers that hear about that, think about it  
**Translation:** 

**[8935.12s] English:** a little bit. It's kind of the mind blown moment.  
**Translation:** 

**[8937.06s] English:** It's like, oh, you can just turn all of that data into code. And nowadays, you have instruction  
**Translation:** 

**[8942.60s] English:** cache issues and that's not necessarily the best idea, but there are different, it's an idea that  
**Translation:** Vocabulary: cache: 缓存问题

**[8948.20s] English:** has power and has probably relevance in some other areas. Maybe it's in a hardware point of view that  
**Translation:** 

**[8953.20s] English:** there's a way you approach building hardware that has that same, you don't even have to think about  
**Translation:** Vocabulary: relevance: 相关性

**[8957.88s] English:** iterating. You just bake everything all the way into it in one place.  
**Translation:** 

**[8962.34s] English:** What is the story of how you came to program Doom? What are some memorable  
**Translation:** 

**[8966.48s] English:** technical moments that you've had?  
**Translation:** 

**[8967.04s] English:** Challenges or innovations within that game?  
**Translation:** Vocabulary: innovations: 创新

**[8969.90s] English:** So the path that we went after Wolfenstein got out and we were on this crazy arc where  
**Translation:** 

**[8975.82s] English:** Keen 1 through 3, more success than we thought. Keen 4 through 6, even more success. Wolfenstein,  
**Translation:** Vocabulary: wolfenstein: 狼穴

**[8981.76s] English:** even more success. So we were on this crazy trajectory for things. So actually our first  
**Translation:** 

**[8987.10s] English:** box commercial project was a Commander Keen game, but then Wolfenstein was going to have a game  
**Translation:** 

**[8992.68s] English:** called Spear of Destiny, which was a commercial version, 60 new levels.  
**Translation:** 

**[8997.04s] English:** So the rest of the team took the game engine pretty much as  
**Translation:** Vocabulary: spear: 长矛

**[9000.00s] English:** as it was, and started working on that. We got new monsters, but it's basically reskins of the  
**Translation:** 

**[9006.82s] English:** things there. And there's a really interesting aspect about that that I didn't appreciate until  
**Translation:** 

**[9010.70s] English:** much, much later about how Wolfenstein clearly did tap out its limit about what you want to play,  
**Translation:** 

**[9018.24s] English:** all the levels and a couple of our licensed things. There was a hard creative wall that  
**Translation:** 

**[9024.22s] English:** you did not really benefit much by continuing to beat on it. But a game like Doom and other  
**Translation:** 

**[9030.38s] English:** more modern games like Minecraft or something, there's kind of a Turing completeness level of  
**Translation:** Vocabulary: completeness: 完备; turing: 图灵

**[9035.18s] English:** design freedom that you get in games that Wolfenstein clearly sat on one side of.  
**Translation:** 

**[9040.06s] English:** All the creative people in the world could not go and do a masterpiece just with the technology  
**Translation:** Vocabulary: masterpiece: 杰作

**[9045.02s] English:** that Wolfenstein had. Wolfenstein could do Wolfenstein, but you really couldn't do something  
**Translation:** 

**[9049.40s] English:** crazy and different. But it didn't take that much more capability to get to Wolfenstein,  
**Translation:** 

**[9054.22s] English:** with the freeform lines and a little bit more artistic freedom, to get to the point where  
**Translation:** 

**[9059.70s] English:** people still announce new Doom levels today, all these years after, without having completely  
**Translation:** Vocabulary: freeform: 自由风格

**[9064.92s] English:** tapped out the creativity. How did you put it? Turing complete?  
**Translation:** 

**[9068.50s] English:** Turing complete design space. Design space.  
**Translation:** 

**[9070.68s] English:** Where it's like, you know, we have the kind of computational universality on a lot of things.  
**Translation:** 

**[9075.72s] English:** But yeah, there's things where a box can be too small, but above a certain point,  
**Translation:** Vocabulary: computational: 计算的; universality: 普遍性

**[9082.76s] English:** you kind of are at the point where...  
**Translation:** 

**[9084.22s] English:** Where you really have almost unbounded creative ability there.  
**Translation:** Vocabulary: unbounded: 无限制的

**[9088.40s] English:** And Doom was the first time you crossed that line.  
**Translation:** 

**[9091.42s] English:** Yeah, where there were thousands of Doom levels created, and some of them still have something  
**Translation:** 

**[9096.48s] English:** new and interesting to say to the world about it.  
**Translation:** 

**[9098.60s] English:** Is that line... Can you introspect what that line was? Is it in the design space? Is it  
**Translation:** Vocabulary: introspect: 自我反省

**[9105.14s] English:** something about the programming capabilities that you were able to add to the game?  
**Translation:** 

**[9110.80s] English:** So the graphics fidelity was a necessary part.  
**Translation:** Vocabulary: fidelity: 清晰度

**[9114.22s] English:** Because the block limitations in Wolfenstein, what we had right there was...  
**Translation:** 

**[9120.00s] English:** was not enough the full scale blocks although minecraft i really did show that perhaps blocks  
**Translation:** Vocabulary: wolfenstein: id软件

**[9125.84s] English:** i stacked in 3d and at one quarter the scale of that one eighth in volume is then sufficient to  
**Translation:** 

**[9132.46s] English:** have all of that but the the wall-sized blocks that we had in wolfenstein was too much of a  
**Translation:** 

**[9137.60s] English:** creative limitation you know we licensed the technology to a few other teams none of them  
**Translation:** 

**[9142.18s] English:** made you know too much of a of a dent with that it just wasn't enough creative ability but a little  
**Translation:** 

**[9148.00s] English:** bit more whether it was the variable floors and ceilings and arbitrary angles in doom or the  
**Translation:** 

**[9153.70s] English:** smaller voxel blocks in uh in minecraft is then enough to open it up to to just worlds and worlds  
**Translation:** Vocabulary: arbitrary: 随意; ceilings: 天花板

**[9160.28s] English:** of new capabilities what is binary space partitioning so the one one of the technologies  
**Translation:** 

**[9167.22s] English:** yeah so jump around a little bit on the on the story path there yes so while the team was working  
**Translation:** Vocabulary: binary: 二进制; partitioning: 划分

**[9172.18s] English:** on spirit destiny for wolfenstein i am i had we had met another development team raven software  
**Translation:** 

**[9177.94s] English:** and we had met another development team raven software and we had met another development team  
**Translation:** Vocabulary: raven: 乌鸦

**[9177.98s] English:** and we had met another development team raven software and we had met another development team  
**Translation:** 

**[9178.00s] English:** while we were in wisconsin and i they were doing they had rpg background and i i still kind of love  
**Translation:** 

**[9184.46s] English:** that and i offered to do a game engine for for them to let them do a 3d rendered rpg instead of  
**Translation:** 

**[9191.22s] English:** the like most rpg games were kind of hand-drawn they made it look kind of 3d but it was done just  
**Translation:** 

**[9196.40s] English:** all with artist work rather than a real engine and after wolfenstein this was still a tile-based  
**Translation:** 

**[9202.98s] English:** world but i added floors and ceilings and some lighting and the ability to have some sloped  
**Translation:** 

**[9207.22s] English:** floors and different  
**Translation:** 

**[9207.98s] English:** areas and that was my intermediate step for a game called shadowcaster  
**Translation:** Vocabulary: shadowcaster: 影之铸者

**[9211.38s] English:** and it had slowed down enough it was not fast enough to do our type of action things so that  
**Translation:** 

**[9217.96s] English:** they had the screen cropped down a little bit so you couldn't go the full screen width like we  
**Translation:** 

**[9222.56s] English:** would try to do in wolfenstein i am but i learned a lot i got the floors and ceilings and lightings  
**Translation:** 

**[9227.90s] English:** and it looked great they were great artists up there and it was it was an inspiration for us  
**Translation:** Vocabulary: lightings: 照明

**[9232.28s] English:** to look at some of that stuff but i had learned enough from that that i had the plan for the  
**Translation:** 

**[9237.96s] English:** for i knew faster ways to do  
**Translation:** 

**[9240.00s] English:** the the lighting and shadowing and i wanted to do this freeform geometry i wanted to break out of  
**Translation:** 

**[9244.62s] English:** this tile based i'm 90 degree world limitations so we had uh that was when we got our next stations  
**Translation:** Vocabulary: freeform: 自由形狀; geometry: 幾何學

**[9252.02s] English:** and we were working with these higher powered systems and i we built an editor that let us  
**Translation:** 

**[9258.14s] English:** draw kind of arbitrary line segments and i was working hard to try to make something that could  
**Translation:** Vocabulary: segments: 线段

**[9262.98s] English:** render this fast enough i'm you know i was pushing myself pretty hard i and we were we were  
**Translation:** 

**[9270.12s] English:** at a point where we could see some things that looked amazingly cool but it wasn't really fast  
**Translation:** Vocabulary: render: 渲染

**[9274.96s] English:** enough for the way i was doing it i for this flexibility it was no longer i couldn't just  
**Translation:** 

**[9279.92s] English:** raycast into it and i had these very complex sets of lines and simple little worlds were okay but  
**Translation:** Vocabulary: flexibility: 灵活性

**[9285.50s] English:** the cool things that we wanted to do just weren't quite fast enough and i wound up taking a break  
**Translation:** 

**[9291.48s] English:** at that point and  
**Translation:** 

**[9292.82s] English:** i  
**Translation:** 

**[9292.96s] English:** I did the the port i did two ports of our games i wolfenstein to the uh to the super nintendo it  
**Translation:** Vocabulary: wolfenstein: 狼穴

**[9301.16s] English:** was i it was a crazy difficult thing to to do which was an even slower processor it was like  
**Translation:** 

**[9306.18s] English:** two i a couple megahertz uh processor and it had been this whole thing where we had farmed out the  
**Translation:** Vocabulary: megahertz: 兆赫; processor: 处理器

**[9313.10s] English:** i am the work and it wasn't it wasn't going well and i took it back over  
**Translation:** 

**[9319.14s] English:** and trying to make it go fast on there where it really  
**Translation:** 

**[9322.80s] English:** did not have much processing power the pixels were stretched up hugely and it's you know it's  
**Translation:** 

**[9327.62s] English:** pretty ugly when you looked at it but in the end it did come out fast enough to play and still be  
**Translation:** Vocabulary: pixels: 像素

**[9331.96s] English:** kind of fun from that but that was where i started using uh bsp trees or binary space partitioning  
**Translation:** 

**[9338.00s] English:** trees it was one of those things i had to make it faster there it was a stepping stone where it was  
**Translation:** Vocabulary: binary: 二进制; partitioning: 划分

**[9343.60s] English:** reasonably easy to understand in the grid world of wolfenstein where it was all still 90 degree  
**Translation:** 

**[9348.32s] English:** angles i'm bsp trees were i eased myself into the world of wolfenstein and i was able to do a lot of  
**Translation:** Vocabulary: reasonably: 较为容易地

**[9352.78s] English:** it with that and it was a big success um then when i came back to working on doom i had this new tool  
**Translation:** 

**[9359.64s] English:** in my  
**Translation:** 

**[9360.00s] English:** toolbox it was going to be a lot harder with the arbitrary angles of doom this was where  
**Translation:** 

**[9364.44s] English:** i really started grappling with epsilon problems and just you know up until that point i hadn't  
**Translation:** Vocabulary: arbitrary: 随意; epsilon: 微小; grappling: 应对; toolbox: 工具箱

**[9369.92s] English:** really had to deal with the fact that i am so many numeric things this almost felt like a betrayal to  
**Translation:** 

**[9375.12s] English:** me where people had told me that i had mathematicians up on a bit of a pedestal where i was people think  
**Translation:** Vocabulary: betrayal: 背叛; mathematicians: 数学家; numeric: 数字的; pedestal: 高台

**[9381.14s] English:** i'm a math wizard and i'm not i really everything that i did was really done with a solid high  
**Translation:** 

**[9387.20s] English:** school math understanding i you know algebra two trigonometry and i'm that was what got me all the  
**Translation:** Vocabulary: algebra: 代数; trigonometry: 三角学

**[9393.74s] English:** way through doom and quake and all of that of just understanding basics of matrices and knowing it  
**Translation:** 

**[9399.16s] English:** well enough to do something with it what's the epsilon problems you ran into so i when you wind  
**Translation:** Vocabulary: matrices: 矩阵

**[9404.28s] English:** up taking a like a sloped line and you say i'm going to intersect it with another sloped line  
**Translation:** 

**[9409.56s] English:** i am then you wind up with something that's not going to be on these nice grid boundaries  
**Translation:** Vocabulary: intersect: 相交

**[9414.36s] English:** with uh the wolfenstein tile maps were  
**Translation:** 

**[9417.20s] English:** all you've got is horizontal and vertical lines looking at it from above and if you cut one of  
**Translation:** Vocabulary: horizontal: 水平; vertical: 垂直

**[9421.28s] English:** them it's just obvious the other one gets cut exactly at that point but when you have angled  
**Translation:** 

**[9426.02s] English:** lines you're doing a kind of a slope intercept problem and you wind up with rational numbers  
**Translation:** 

**[9430.62s] English:** there where things that are not going to evenly land on an integer or even on any fixed point  
**Translation:** 

**[9436.08s] English:** value that you've got so everything winds up having to snap to some fixed point value so  
**Translation:** Vocabulary: integer: 整数

**[9441.20s] English:** the lines slightly change their angle you wind up if you cut something here this one's going to bend  
**Translation:** 

**[9445.98s] English:** a little this way and it's not going to be on the right side of the line and you wind up with  
**Translation:** 

**[9447.20s] English:** something that's not going to be completely straight and then you come down to all these  
**Translation:** 

**[9450.14s] English:** questions of well this one is is is a point on an angled line you can't answer that in finite  
**Translation:** 

**[9457.08s] English:** precision unless you're doing something with actual rational numbers and later on i did waste  
**Translation:** 

**[9462.30s] English:** far too much time chasing things like that how do you do precise arithmetic with rational numbers  
**Translation:** Vocabulary: arithmetic: 算术

**[9466.72s] English:** and it always blows up eventually you know exponentially as you do it so these are these  
**Translation:** 

**[9471.32s] English:** kind of things are impossible with computers so they're they're possible again there are paths to  
**Translation:** Vocabulary: exponentially: 成倍地

**[9476.52s] English:** do the doing it but it's not going to be completely straight and then you come down to all these  
**Translation:** 

**[9477.20s] English:** but you can't fit them conveniently in any of the numbers  
**Translation:** Vocabulary: conveniently: 方便地

**[9480.00s] English:** is you need to start using big nums  
**Translation:** 

**[9481.74s] English:** and different factor trackings of different things.  
**Translation:** Vocabulary: trackings: 跟踪记录

**[9484.74s] English:** So you have to, if you have any elements of OCD  
**Translation:** 

**[9487.80s] English:** and you want to do something perfectly,  
**Translation:** 

**[9489.80s] English:** you're screwed if you're working with floating point.  
**Translation:** 

**[9492.28s] English:** Yeah.  
**Translation:** 

**[9492.80s] English:** So you had to deal with this for the first time.  
**Translation:** 

**[9495.28s] English:** And there were lots of challenges there about like,  
**Translation:** 

**[9498.44s] English:** okay, they build this cool thing.  
**Translation:** 

**[9500.18s] English:** And the way the BSP trees work  
**Translation:** 

**[9501.82s] English:** is it basically takes the walls  
**Translation:** 

**[9504.00s] English:** and it carves other walls by those walls  
**Translation:** 

**[9506.26s] English:** in this clever way that you can then  
**Translation:** 

**[9508.36s] English:** take all of these fragments  
**Translation:** 

**[9509.88s] English:** and then you can for sure from any given point  
**Translation:** 

**[9512.98s] English:** get an ordering of everything in the world.  
**Translation:** 

**[9515.10s] English:** And you can say, this goes in front of this,  
**Translation:** 

**[9516.80s] English:** goes in front of this,  
**Translation:** 

**[9517.74s] English:** all the way back to the last thing.  
**Translation:** 

**[9520.32s] English:** And that's super valuable for graphics  
**Translation:** 

**[9522.22s] English:** where kind of a classic graphics algorithm  
**Translation:** 

**[9525.08s] English:** would be painter's algorithm.  
**Translation:** 

**[9526.84s] English:** You paint the furthest thing first  
**Translation:** 

**[9528.08s] English:** and then the next thing and then the next thing.  
**Translation:** Vocabulary: furthest: 最远的

**[9530.08s] English:** And then it comes up and it's all perfect for you.  
**Translation:** 

**[9532.58s] English:** That's slow because you don't want to have  
**Translation:** 

**[9534.20s] English:** to have drawn everything like that.  
**Translation:** 

**[9536.10s] English:** But you can also flip it around  
**Translation:** 

**[9537.44s] English:** and draw the closest thing to you.  
**Translation:** 

**[9539.38s] English:** And then if you're clever about it,  
**Translation:** 

**[9541.36s] English:** you can figure out what you need to draw  
**Translation:** 

**[9543.26s] English:** that's visible beyond that.  
**Translation:** 

**[9545.54s] English:** And that's what BSP trees allow you to do.  
**Translation:** 

**[9547.58s] English:** Yeah.  
**Translation:** 

**[9547.88s] English:** So it's combined with a bunch of other things,  
**Translation:** 

**[9550.64s] English:** but it gives you that ordering.  
**Translation:** 

**[9552.00s] English:** It's a clever way of doing things.  
**Translation:** 

**[9553.74s] English:** And I remember I had learned this from  
**Translation:** 

**[9555.82s] English:** one of my graphics Bible at the time,  
**Translation:** 

**[9558.74s] English:** a book called Foley and Van Damme.  
**Translation:** Vocabulary: foley: 录音效果

**[9560.54s] English:** And again, it was a different world back there.  
**Translation:** 

**[9562.20s] English:** There was a small integer number of books.  
**Translation:** Vocabulary: integer: 整数

**[9565.02s] English:** And this book, yeah, this book,  
**Translation:** 

**[9567.44s] English:** it was big fat college,  
**Translation:** 

**[9568.90s] English:** textbook that I had read through many times.  
**Translation:** 

**[9572.52s] English:** I didn't understand everything in it.  
**Translation:** 

**[9574.26s] English:** Some of it wasn't useful to me,  
**Translation:** 

**[9575.88s] English:** but they had the little thing about finite orderings  
**Translation:** Vocabulary: finite: 有限的

**[9579.56s] English:** of you draw a little T-shaped thing  
**Translation:** 

**[9581.48s] English:** and you can say you can make a fixed  
**Translation:** 

**[9583.74s] English:** ahead of time order from this  
**Translation:** 

**[9585.20s] English:** and you can generalize this with the BSP trees.  
**Translation:** Vocabulary: generalize: 概括

**[9588.32s] English:** And I got a little bit more information about that.  
**Translation:** 

**[9590.82s] English:** And it was kind of fun later  
**Translation:** 

**[9591.72s] English:** while I was working on Quake,  
**Translation:** 

**[9593.14s] English:** I got to meet Bruce Naylor,  
**Translation:** 

**[9594.78s] English:** who was one of the original researchers  
**Translation:** 

**[9596.26s] English:** that developed those technologies.  
**Translation:** 

**[9598.90s] English:** As for academic.  
**Translation:** 

**[9600.00s] English:** literature, and that was kind of fun. But I was very much just finding a tool that can help me  
**Translation:** 

**[9604.44s] English:** solve what I was doing. And I was using it in this very crude way in a two-dimensional fashion  
**Translation:** 

**[9609.02s] English:** rather than the general 3D. The epsilon problems got much worse in Quake and three-dimensionals  
**Translation:** Vocabulary: epsilon: 微小误差

**[9613.70s] English:** when things angle in every way. But eventually, I did sort out how to do it reliably on Doom.  
**Translation:** 

**[9620.02s] English:** There were still a few edge cases in Doom that were not absolutely perfect, where they even got  
**Translation:** Vocabulary: reliably: 可靠地

**[9626.08s] English:** terminologies in the communities. Like when you got to something where it was messed up,  
**Translation:** 

**[9629.42s] English:** it was a hall-of-mirrors effect because you'd sweep by and it wouldn't draw something there,  
**Translation:** Vocabulary: terminologies: 术语

**[9633.70s] English:** and you would just wind up with the leftover remnants as you flipped between the two pages.  
**Translation:** 

**[9639.34s] English:** But BSP trees were important for it. But it's, again, worth noting that after we did Doom,  
**Translation:** Vocabulary: leftover: 剩余部分

**[9645.38s] English:** our major competition came from Ken Silverman and his Build Engine, which was used for Duke Nukem  
**Translation:** 

**[9651.14s] English:** 3D and some of the other games for 3D Realms. And he used a completely different technology,  
**Translation:** Vocabulary: silverman: 银曼

**[9656.26s] English:** nothing to do with BSP trees.  
**Translation:** 

**[9659.42s] English:** So there's not just a one true way of doing things. There were critical things about  
**Translation:** 

**[9665.22s] English:** to make any of those games fast. You had to separate your drawing into you drew vertical  
**Translation:** 

**[9670.40s] English:** lines and you drew horizontal lines, just kind of changing exactly what you would draw with them.  
**Translation:** Vocabulary: horizontal: 水平; vertical: 垂直

**[9675.50s] English:** That was critical for the technologies at that time. And all the games that were kind of like  
**Translation:** 

**[9681.42s] English:** that wound up doing something similar. But there were still a bunch of other decisions  
**Translation:** 

**[9685.12s] English:** that could be made. And we made good enough decisions on everything,  
**Translation:** 

**[9689.38s] English:** on Doom. We brought in multiplayer significantly. And it was our first game that was designed to be  
**Translation:** 

**[9695.92s] English:** modified by the user community, where we had this whole setup of our WAD files and PWADs and things  
**Translation:** 

**[9701.42s] English:** that people could build with tools that we released to them. And they eventually rewrote  
**Translation:** Vocabulary: setup: 设置

**[9705.64s] English:** to be better than what we released. But they could build things and you could add it to your  
**Translation:** 

**[9710.14s] English:** game without destructively modifying it, which is what you had to do in all the early games.  
**Translation:** Vocabulary: destructively: 破坏性地; modifying: 修改

**[9714.02s] English:** You literally hacked the data files or the executable before, while Doom was set  
**Translation:** 

**[9719.38s] English:** up in this flexibility.  
**Translation:** Vocabulary: executable: 可执行文件; flexibility: 灵活性; hacked: 破解

**[9720.00s] English:** way so that you could just say run the normal game with this added on on top and it would  
**Translation:** 

**[9725.30s] English:** overlay just the things that you wanted to there would you say that doom was kind of the first  
**Translation:** 

**[9731.24s] English:** true 3d game that you created so no it's still doom would usually be called a two and a half  
**Translation:** 

**[9737.22s] English:** d game where it had three-dimensional points on it and this is another one of these kind of pedantic  
**Translation:** Vocabulary: pedantic: 吹毛求疵

**[9742.00s] English:** things that people love to argue about about what was the first 3d game i still like i'm like every  
**Translation:** 

**[9747.50s] English:** month probably i hear from somebody about well was doom really a 3d game or something i and you  
**Translation:** 

**[9754.20s] English:** know and i give the the point where characters had three coordinates so you had like an x y and z the  
**Translation:** 

**[9760.32s] English:** cacodemon could be coming in very high and come you know and come down towards you i have the  
**Translation:** Vocabulary: cacodemon: 恶鬼; coordinates: 坐标

**[9765.08s] English:** walls had three coordinates on them so on some sense it's a 3d game engine but it was not a  
**Translation:** 

**[9771.32s] English:** fully general 3d game engine you could not i you could not build a pyramid in doom because you  
**Translation:** Vocabulary: pyramid: 金字塔

**[9776.98s] English:** couldn't make a  
**Translation:** 

**[9777.48s] English:** sloped wall i which was slightly different where in that previous shadow caster game i couldn't  
**Translation:** 

**[9782.74s] English:** have vertexes and have a sloped floor there but the changes that i made for doom to get higher  
**Translation:** 

**[9787.70s] English:** speed and a different set of flexibility traded away that ability but you literally couldn't make  
**Translation:** Vocabulary: vertexes: 顶点

**[9792.78s] English:** that you could not i you could make different heights of uh passages but you could not make  
**Translation:** 

**[9798.60s] English:** a bridge over another area you could not go over and above it so it still had some 2d limitations  
**Translation:** 

**[9804.24s] English:** to it that's more about the building versus the actual experience  
**Translation:** 

**[9807.38s] English:** you could not make a bridge over another area you could not go over and above it so it still had some  
**Translation:** 

**[9807.46s] English:** 2d limitations to it so it still had some 2d limitations because the experience is  
**Translation:** 

**[9808.58s] English:** it felt like things would come at you but again you couldn't look up either i am right you know  
**Translation:** 

**[9813.34s] English:** you could only pitch it was four degrees of freedom rather than six degrees of freedom  
**Translation:** 

**[9817.92s] English:** you did not have the ability to tilt your head this way or pitch up and down so that takes us  
**Translation:** 

**[9823.02s] English:** to quake what was the leap there what was some fascinating technical challenges and there were a  
**Translation:** 

**[9830.62s] English:** lot or not challenges but innovations that you've come up with so quake was kind of the first thing  
**Translation:** Vocabulary: innovations: 创新

**[9836.38s] English:** where i did have a lot of experience with the game and i did have a lot of experience with the game  
**Translation:** 

**[9837.46s] English:** because i would have to kind of come face to face with  
**Translation:** 

**[9839.74s] English:** i would have to kind of come face to face with  
**Translation:** 

**[9839.78s] English:** but now i had to push through all theード that you mentioned and thousands of years ago because  
**Translation:** 

**[9843.36s] English:** again i did a huge twist if you look at games you don't literally have to make two or three  
**Translation:** 

**[9857.16s] English:** one you would just every one of the games go to something two you'd have to have a game of  
**Translation:** 

**[9862.06s] English:** your own remember to switch it one to three over and over over and over and over over and over you would  
**Translation:** 

**[9865.64s] English:** have to come face to face with  
**Translation:** 

**[9840.00s] English:** but my limitations, where it was the first thing where I really did kind of give it my all and  
**Translation:** 

**[9845.78s] English:** still come up a little bit short in terms of what and when I wanted to get it done.  
**Translation:** 

**[9851.60s] English:** And the company had some serious stresses through the whole project. And we bit off a lot. So the  
**Translation:** 

**[9859.92s] English:** things that we set out to do was it was going to be really a true 3D engine where it could do  
**Translation:** Vocabulary: stresses: 压力

**[9865.40s] English:** six degree of freedom. You could have all the viewpoints. You could model anything. It had  
**Translation:** 

**[9871.98s] English:** a really remarkable new lighting model with the surface caching and things. That was one of those  
**Translation:** Vocabulary: caching: 缓存; viewpoints: 视角

**[9877.68s] English:** where it was starting to do some things that they weren't doing even on the very high-end systems.  
**Translation:** 

**[9883.36s] English:** And it was going to be completely programmable in the modding standpoint, where the thing that  
**Translation:** Vocabulary: standpoint: 角度

**[9888.86s] English:** you couldn't do in Doom, you could replace almost all of the media, but you couldn't really change  
**Translation:** 

**[9893.64s] English:** the game. There were...  
**Translation:** 

**[9895.40s] English:** There were still some people that were doing the hex editing of the executable, the de-hacked  
**Translation:** 

**[9899.32s] English:** things where you could change a few things about rules. And people made some early capture the  
**Translation:** Vocabulary: executable: 可执行文件

**[9903.74s] English:** flag type things by hacking the executable, but it wasn't really set out to do that.  
**Translation:** 

**[9908.62s] English:** Quake was going to have its own programming language that the game was going to be implemented  
**Translation:** Vocabulary: hacking: 非法修改

**[9912.68s] English:** in it. And that would be able to be overwritten just like any of the media. Code was going to  
**Translation:** 

**[9917.28s] English:** be data for that. And you would be able to have expansion packs that changed fundamental things  
**Translation:** Vocabulary: overwritten: 覆盖

**[9922.30s] English:** and mods and so on. And the...  
**Translation:** 

**[9924.96s] English:** The...  
**Translation:** 

**[9925.40s] English:** Multiplayer was going to be playable over the internet. It was going to support a client server  
**Translation:** 

**[9930.72s] English:** rather than peer-to-peer. So we had the possibility of supporting larger numbers of players in  
**Translation:** 

**[9935.72s] English:** disparate locations with this full flexibility of the programming overrides with full six degree  
**Translation:** 

**[9942.32s] English:** of freedom modeling and viewing. And with this fancy new light mapped kind of surface caching  
**Translation:** Vocabulary: disparate: 不相关; flexibility: 灵活性; overrides: 覆盖设置

**[9948.86s] English:** side, it was a lot. And this was one of those things that if I could go back and tell, you know,  
**Translation:** 

**[9955.20s] English:** tell younger me to do something differently, it would have been to split those innovations up into  
**Translation:** Vocabulary: innovations: 创新

**[9959.84s] English:** two.  
**Translation:** 

**[9960.00s] English:** phases in two separate games will be phase one and phase two so it probably would have been taking  
**Translation:** 

**[9965.36s] English:** the doom rendering engine and bringing in uh the tcp ip uh client server focusing on the multiplayer  
**Translation:** 

**[9971.74s] English:** and the uh the quake c or would have been doom c programming language there so i would have split  
**Translation:** 

**[9977.78s] English:** that into programming language and networking with the same doom engine rather than forcing  
**Translation:** 

**[9982.64s] English:** everybody to go towards the the pen you know the quake engine which really meant getting a pentium  
**Translation:** 

**[9987.30s] English:** you know while it ran on a 486 it was not a great experience there we could have made more people  
**Translation:** 

**[9992.14s] English:** happier and gotten two games done in 50 more time i so speaking of people happier our mutual friend  
**Translation:** 

**[10001.60s] English:** joe rogan it seems like his the the most important uh moment of his life is is uh centered around  
**Translation:** 

**[10008.62s] English:** quake so it was a definitive um part of his life so would he agree with your uh thinking that they  
**Translation:** Vocabulary: definitive: 决定性的

**[10017.30s] English:** should split uh so he is a person who loves quake and played quake a lot would he agree that you  
**Translation:** 

**[10024.54s] English:** should have done the doom engine with and focus on the multiplayer for phase one uh or in your  
**Translation:** 

**[10031.12s] English:** looking back it is is the the 3d world that quake created was also fundamental to the the  
**Translation:** 

**[10038.56s] English:** you know i would say that what would have happened is you would have had a a doom looking but quake  
**Translation:** 

**[10045.74s] English:** feeling uh game  
**Translation:** 

**[10047.30s] English:** eight months earlier and then maybe six months after quake actually shipped then there would  
**Translation:** 

**[10053.52s] English:** have been the full running on a pentium i am six degree of freedom graphics engine type things  
**Translation:** 

**[10058.52s] English:** there so it's not that it wouldn't have it wouldn't have been there it would have been  
**Translation:** 

**[10062.72s] English:** something amazingly cool earlier and then something even cooler somewhat later where i would much  
**Translation:** 

**[10069.02s] English:** rather in have gone and done two one-year development efforts i cycle them through i  
**Translation:** 

**[10075.08s] English:** be a little more pragmatic about that  
**Translation:** 

**[10077.30s] English:** rather than killing us ourselves on the whole  
**Translation:** Vocabulary: pragmatic: 实用

**[10080.00s] English:** development but i would say it's obviously things worked out well in the end but looking back and  
**Translation:** 

**[10086.12s] English:** saying how would i optimize and do things differently that did seem to be a clear case  
**Translation:** 

**[10090.74s] English:** where i going ahead and we had enormous momentum on doom you know we did doom 2 as the kind of  
**Translation:** 

**[10097.74s] English:** commercial boxed version after our shareware success with the original but we could have  
**Translation:** 

**[10102.96s] English:** just made another doom game adding those new features in it would have been huge we would  
**Translation:** 

**[10108.88s] English:** have learned all the same lessons but faster and it would have given six degree of freedom  
**Translation:** 

**[10113.84s] English:** and pentium class systems a little bit more time to get mainstream because we did cut out a lot of  
**Translation:** 

**[10119.68s] English:** people with the hardware requirements for quake was there any dark moments for you personally  
**Translation:** 

**[10124.68s] English:** psychologically in having um in um having such harsh deadlines and having this also  
**Translation:** 

**[10132.62s] English:** difficult technical challenges so i've never really had  
**Translation:** Vocabulary: deadlines: 截止日期; psychologically: 心理上

**[10137.72s] English:** you  
**Translation:** 

**[10138.88s] English:** really dark black places i mean i it i can't necessarily put myself in anyone else's shoes  
**Translation:** 

**[10143.82s] English:** but i understand a lot of people have you have significant challenges with kind of their their  
**Translation:** 

**[10150.86s] English:** mental health and well-being and i've been i've been super stressed i've been you know unhappy as  
**Translation:** 

**[10156.58s] English:** a teenager in various ways but i've never i've never really gone to a very dark place i just  
**Translation:** 

**[10164.12s] English:** seem to be largely immune to what  
**Translation:** Vocabulary: immune: 免疫

**[10168.88s] English:** really wrecks people i mean i've had plenty of time when i'm very unhappy and miserable about  
**Translation:** 

**[10173.16s] English:** something but it's never hit me like you know i believe it winds up hitting some other people  
**Translation:** 

**[10178.58s] English:** i've borne up well under whatever stresses have i'm you know have kind of fallen on me and i've  
**Translation:** 

**[10184.94s] English:** always coped best on that when all i need to do is is usually just kind of bear down on my work  
**Translation:** Vocabulary: stresses: 压力

**[10191.06s] English:** i i pull myself out of whatever hole i might be slipping into by actually making progress  
**Translation:** 

**[10197.06s] English:** i i mean maybe if i was in a football field i could have been a better player for a 정말  
**Translation:** 

**[10197.68s] English:** not a french basketball player but i i think we were all right myself i mean when over and over again so  
**Translation:** 

**[10197.72s] English:** most of the stuff that i hear about that we know is it's just pretty go back and forth with a lot of mindfulness  
**Translation:** 

**[10198.24s] English:** really but i guess given at that point you know yeah go back to the real world i really want to believe in hard hopes instead of  
**Translation:** 

**[10198.88s] English:** position where I was never  
**Translation:** 

**[10200.00s] English:** ever able to make that progress. I could have slid down further, but I've always been in a place  
**Translation:** 

**[10205.22s] English:** where, okay, a little bit more work, maybe I'm in a tough spot here, but I always know if I just  
**Translation:** 

**[10211.48s] English:** keep pushing, eventually I break through and I make progress. I feel good about what I'm doing.  
**Translation:** 

**[10217.02s] English:** And that's been enough for me so far in my life. Have you seen in the distance,  
**Translation:** 

**[10222.16s] English:** uh, like, um, you know, ideas of depression or contemplating suicide? Have you seen those things  
**Translation:** 

**[10229.78s] English:** far? So it was interesting when, when I was a teenager, I was, you know, I, I was probably  
**Translation:** Vocabulary: contemplating: 考虑

**[10235.66s] English:** on some level of troubled youth. I was unhappy most of my teenage, uh, you know, years. I,  
**Translation:** 

**[10240.58s] English:** you know, I really, I wanted to be on my own doing programming all the time. I, you know,  
**Translation:** 

**[10244.52s] English:** as soon as I was 18, 19, even though I was poor, I was doing exactly what I wanted and I was very  
**Translation:** 

**[10249.84s] English:** happy, but high school was not a great time. I was, I was, I was, I was, I was, I was, I was, I was,  
**Translation:** 

**[10252.16s] English:** for me. And I am, I had a conversation with like the school counselor and they're kind of  
**Translation:** 

**[10257.60s] English:** running their script. It's like, okay, it's kind of a weird kid here. Let's carefully probe around.  
**Translation:** 

**[10262.40s] English:** It's like, you know, do you ever think about ending it all? I'm like, no, of course not.  
**Translation:** 

**[10267.48s] English:** Never. Not at all. I, this is temporary. Things are going to be better. I'm, and, and that's  
**Translation:** 

**[10273.56s] English:** always been kind of the case for me. And obviously that's not that way for everyone. And other people  
**Translation:** 

**[10278.78s] English:** do react differently. And what was your, um,  
**Translation:** 

**[10282.16s] English:** what was your escape from the troubled youth? Like, uh, uh, you know, music,  
**Translation:** 

**[10289.46s] English:** video games, books. How did you escape from a world that's full of cruelty and suffering?  
**Translation:** 

**[10297.20s] English:** And that's absurd. Yeah. I mean, I, I was not, you know, I was not a victim of cruelty and  
**Translation:** 

**[10301.34s] English:** suffering. It's like, I was an unhappy, somewhat petulant youth. And, you know, in my point where  
**Translation:** 

**[10305.68s] English:** I, you know, I'm not putting myself up with anybody else's suffering, but I was unhappy  
**Translation:** 

**[10310.88s] English:** objectively.  
**Translation:** Vocabulary: objectively: 客观地

**[10312.16s] English:** And I, the things that I, I did that very much characterized my childhood were I had,  
**Translation:** 

**[10318.46s] English:** um, books, comics.  
**Translation:** 

**[10320.00s] English:** books dungeons and dragons arcade games video games like some of my my fondest childhood memories  
**Translation:** 

**[10326.26s] English:** are the convenience stores the 7-elevens and quick trips because they had a spinner rack of comic  
**Translation:** Vocabulary: arcade: 街机; dragons: 龙; dungeons: 地牢

**[10331.00s] English:** books and they had a little side room with two or three video games arcade games in it and that was  
**Translation:** 

**[10336.74s] English:** uh that was very much my happy place you know if i could i get my comic books and uh if i could go  
**Translation:** 

**[10341.70s] English:** to a library and you know go through those the little zero zero zero section where computer  
**Translation:** 

**[10346.24s] English:** books were supposed to be and there were a few sad little books there but still just being able  
**Translation:** 

**[10350.36s] English:** to sit down and go through that and i read you know i read a ridiculous number of books both  
**Translation:** 

**[10355.94s] English:** fiction and non-fiction as a teenager and i you know as i my rebel my rebelling in high school  
**Translation:** Vocabulary: rebelling: 叛逆

**[10362.72s] English:** was just sitting there with my nose in a book ignoring the class i threw lots of it and teachers  
**Translation:** 

**[10367.40s] English:** had a range of reactions to that some more uh more accepting of it than others i'm with you on that  
**Translation:** 

**[10374.54s] English:** so let us return to quake for  
**Translation:** 

**[10376.22s] English:** a bit with the technical challenges what what um everything together from the from the networking  
**Translation:** 

**[10383.08s] English:** to the the graphics what what are some things you remember that were that were innovations you had  
**Translation:** 

**[10389.74s] English:** to come up with in order to make it all happen yeah so there were a bunch of things on quake  
**Translation:** Vocabulary: innovations: 创新

**[10394.84s] English:** where on the one hand the idea that i built my own programming language to implement the game in  
**Translation:** 

**[10400.70s] English:** looking back and i try to tell people it's like every every high level programmer sometime in  
**Translation:** 

**[10405.96s] English:** their career  
**Translation:** 

**[10406.22s] English:** goes through and they invent their own language it just seems to be a thing that's pretty broadly  
**Translation:** 

**[10409.80s] English:** done people will be like i'm gonna go write a computer programming language and i you know i  
**Translation:** 

**[10415.82s] English:** don't regret having done it but after that i i switched from quake c my quirky little i am pseudo  
**Translation:** Vocabulary: pseudo: 似是而非; quirky: 古怪

**[10422.20s] English:** object orienter entity oriented language there quake 2 went back to using dlls with c and then  
**Translation:** 

**[10428.26s] English:** quake 3 i implemented my own c interpreter or compiler which was a much smarter thing to do  
**Translation:** Vocabulary: interpreter: 解释器; orienter: 导向者

**[10433.18s] English:** that i should have done originally for quake but built my own programming language to implement  
**Translation:** 

**[10436.22s] English:** my own language was an experience i learned a lot from that i am and then  
**Translation:** 

**[10440.00s] English:** There was a generation of game programmers that learned programming with QuakeC, which I feel kind of bad about because, you know, I mean, we give JavaScript a lot of crap, but QuakeC was nothing to write home about there.  
**Translation:** 

**[10452.76s] English:** But it allowed people to do magical things.  
**Translation:** Vocabulary: programmers: 程序员

**[10455.64s] English:** You get into programming not because you love the BNF syntax of a language.  
**Translation:** 

**[10461.40s] English:** It's because the language lets you do something that you cared about.  
**Translation:** Vocabulary: syntax: 语法规则

**[10464.80s] English:** And here, very much, you could do something in a whole beautiful three-dimensional world.  
**Translation:** 

**[10469.50s] English:** And the idea and the fact that the code for the game was out there, you could say, I like the shotgun, but I want it to be more badass.  
**Translation:** Vocabulary: badass: 酷毙了; shotgun: 猎枪

**[10476.12s] English:** You go in there and say, okay, now it does 200 points damage.  
**Translation:** 

**[10479.36s] English:** And then you go around with a big grin on your face blowing up monsters all over the game.  
**Translation:** 

**[10484.10s] English:** So, yeah, it is not what I would do today going back with that language, but that was a big part of it.  
**Translation:** 

**[10491.34s] English:** Learning about the networking stuff, because it's interesting where I learned these things by reading books.  
**Translation:** 

**[10497.52s] English:** So I would get a book on networking.  
**Translation:** 

**[10498.98s] English:** Find something I read all about and learn, okay, packets, they can be, you know, out of order or lost or duplicated.  
**Translation:** Vocabulary: duplicated: 复制的

**[10506.44s] English:** These are all the things that can theoretically happen to packets.  
**Translation:** 

**[10509.18s] English:** So I wind up spending all this time thinking about how do we deal about all of that.  
**Translation:** Vocabulary: theoretically: 理论上

**[10513.12s] English:** And it turns out, of course, in the real world, those are things that, yes, theoretically can happen with multiple routes,  
**Translation:** 

**[10518.00s] English:** but they really aren't things that your 99.999% of your packets have to deal with.  
**Translation:** 

**[10524.86s] English:** So there was learning experiences about lots of that.  
**Translation:** 

**[10528.26s] English:** Like why?  
**Translation:** 

**[10528.98s] English:** Like when TCP is appropriate versus UDP, and how if you do things in UDP, you wind up reinventing TCP badly in almost all cases.  
**Translation:** 

**[10537.90s] English:** So, you know, there's good arguments for using both for different parts of the game process, transitioning from level to level and all.  
**Translation:** Vocabulary: transitioning: 转换

**[10546.68s] English:** But the graphics were the showcase of what Quake was all about.  
**Translation:** 

**[10551.90s] English:** It was this graphics technology that nobody had seen there.  
**Translation:** Vocabulary: showcase: 展示窗口

**[10555.50s] English:** And it was a while before, you know, there were competitive things out there.  
**Translation:** 

**[10558.80s] English:** And  
**Translation:** 

**[10560.00s] English:** it went a long time internally really not working where we were even building levels where uh the  
**Translation:** 

**[10566.86s] English:** game just was not at all shippable with large fractions of the world like disappearing not  
**Translation:** Vocabulary: fractions: 部分; internally: 内部

**[10572.40s] English:** being there i or being really slow in various parts of it and it was this act of faith it's  
**Translation:** 

**[10578.50s] English:** like i think i'm going to be able to fix this i think i'm going to be able to make this work  
**Translation:** 

**[10582.48s] English:** um and lots of stuff changed where the level designers would build something then have to  
**Translation:** 

**[10588.34s] English:** throw it away as something fundamental in the kind of graphics or level technology change  
**Translation:** Vocabulary: designers: 设计人员

**[10592.98s] English:** and the i am so there were two big things that contributed to making it possible at that time  
**Translation:** 

**[10599.78s] English:** frame i am two new things there was certainly hardcore optimized low-level assembly language  
**Translation:** Vocabulary: hardcore: 核心的; optimized: 优化的

**[10605.96s] English:** this was where i had hired michael abrash away from microsoft and he had been one of my early  
**Translation:** 

**[10611.40s] English:** inspirations where that back in the soft disk days the library of magazines that they had  
**Translation:** Vocabulary: abrash: Abrash

**[10616.68s] English:** some of my most treasured  
**Translation:** 

**[10618.34s] English:** ones were michael abrash's articles in dr dobbs journal and it was it was amazing after all of  
**Translation:** Vocabulary: dobbs: 多布斯

**[10625.34s] English:** our success in doom we were able to kind of hit him up and say hey we'd like you to come work at  
**Translation:** 

**[10629.92s] English:** id software and he was in the senior technical role at microsoft and i am you know and he was  
**Translation:** 

**[10635.12s] English:** on track for and this was right when microsoft was starting to take off and i did eventually  
**Translation:** 

**[10639.92s] English:** you know convince him that what we were doing was going to be really amazing with quake it was going  
**Translation:** 

**[10645.08s] English:** to it was going to be something nobody had seen before  
**Translation:** 

**[10648.34s] English:** it had these aspects of what we were talking about we had metaverse talk back then we you know  
**Translation:** Vocabulary: metaverse: 虚拟宇宙

**[10653.66s] English:** we had read snow crash and we were we knew about this and uh michael was i was big into the science  
**Translation:** 

**[10659.56s] English:** fiction and we would talk about all that and kind of spin this tale and it was some of the same  
**Translation:** 

**[10664.38s] English:** conversations that we have today about the metaverse about how you could have different  
**Translation:** 

**[10668.50s] English:** areas linked together by portals and you could have user generated content and changing out all  
**Translation:** 

**[10673.46s] English:** these things so you really were creating the metaverse with quake and we we talked about  
**Translation:** 

**[10678.34s] English:** things like philosophically  
**Translation:** Vocabulary: philosophically: 哲学地

**[10680.00s] English:** as a virtual reality experience.  
**Translation:** 

**[10682.72s] English:** You know, that was the first wave of virtual reality  
**Translation:** 

**[10685.14s] English:** was in the late 80s and early 90s.  
**Translation:** 

**[10687.74s] English:** You had like the Lawnmower Man movie  
**Translation:** 

**[10690.36s] English:** and you had time in Newsweek  
**Translation:** 

**[10691.90s] English:** talking about the early VPL headsets.  
**Translation:** Vocabulary: headsets: 耳机; newsweek: 新闻周刊

**[10694.76s] English:** And of course that cratered so hard  
**Translation:** 

**[10696.76s] English:** that people didn't want to look at virtual reality  
**Translation:** Vocabulary: cratered: 撞击形成坑洞

**[10698.60s] English:** for decades afterwards,  
**Translation:** 

**[10699.84s] English:** where it was just, it was smoke and mirrors.  
**Translation:** 

**[10703.30s] English:** It was not real in the sense  
**Translation:** 

**[10704.78s] English:** that you could actually do something  
**Translation:** 

**[10706.34s] English:** real and valuable with it.  
**Translation:** 

**[10708.24s] English:** But still we had that kind of common set of talking points  
**Translation:** 

**[10712.16s] English:** and we were talking about what these games could become  
**Translation:** 

**[10716.10s] English:** and how you'd like to see people  
**Translation:** 

**[10717.82s] English:** building all of these creative things  
**Translation:** 

**[10719.52s] English:** because we were seeing an explosion of work  
**Translation:** 

**[10721.46s] English:** with Doom at that time  
**Translation:** 

**[10722.56s] English:** where people were doing amazingly cool things.  
**Translation:** 

**[10725.84s] English:** Like we saw cooler levels that we had built  
**Translation:** 

**[10728.06s] English:** coming out of the user community  
**Translation:** 

**[10729.54s] English:** and then people finding ways to, you know,  
**Translation:** 

**[10732.16s] English:** change the characters in different ways.  
**Translation:** 

**[10734.08s] English:** And it was great.  
**Translation:** 

**[10734.72s] English:** And we knew what we were doing in Quake  
**Translation:** 

**[10736.66s] English:** was removing those lags  
**Translation:** 

**[10738.22s] English:** there was some quirky things  
**Translation:** Vocabulary: quirky: 古怪的

**[10740.36s] English:** with a couple of the data types  
**Translation:** 

**[10741.88s] English:** that didn't work right for overriding  
**Translation:** Vocabulary: overriding: 覆盖的

**[10743.84s] English:** and then the core thing about the programming model.  
**Translation:** 

**[10747.34s] English:** And I was definitely going to hit all of those in Quake.  
**Translation:** 

**[10750.62s] English:** But the graphics side of it was,  
**Translation:** 

**[10753.68s] English:** it was still, I knew what I wanted to do  
**Translation:** 

**[10756.82s] English:** and it was one of these hubris things  
**Translation:** 

**[10760.34s] English:** where it's like, well, so far I've been able to  
**Translation:** Vocabulary: hubris: 傲慢

**[10762.38s] English:** kind of kick everything that I set out to go do.  
**Translation:** 

**[10766.22s] English:** But Quake was definitely,  
**Translation:** 

**[10768.22s] English:** a little bit more than could be comfortably chewed  
**Translation:** 

**[10770.90s] English:** at that point.  
**Translation:** 

**[10772.88s] English:** But Michael was one of the strongest programmers  
**Translation:** 

**[10776.70s] English:** and graphics programmers that I knew.  
**Translation:** 

**[10779.20s] English:** And he was one of the people that I trusted  
**Translation:** 

**[10780.70s] English:** to write assembly code, you know, better than I could.  
**Translation:** 

**[10784.42s] English:** And there's a few people that I can point to  
**Translation:** 

**[10786.72s] English:** about things like this  
**Translation:** 

**[10787.70s] English:** where I'm a world-class optimizer.  
**Translation:** 

**[10790.04s] English:** I mean, I make things go fast,  
**Translation:** Vocabulary: optimizer: 优化器

**[10791.82s] English:** but I recognize there's a number of people  
**Translation:** 

**[10794.54s] English:** that can write tighter assembly code,  
**Translation:** 

**[10796.82s] English:** tighter SIMD code,  
**Translation:** 

**[10797.88s] English:** or tighter CUDA code that, you know,  
**Translation:** 

**[10800.00s] English:** than i can write i am you know my best strengths are a little bit more at the system level i mean  
**Translation:** 

**[10805.54s] English:** i'm good at all of that but the most leverage comes from making the decisions that are a little  
**Translation:** Vocabulary: leverage: 影响力

**[10810.74s] English:** bit higher up where you figure out how to change your large scale problems so that these lower  
**Translation:** 

**[10815.98s] English:** level problems are easier to do or it makes it possible to do them in a i'm in a uniquely fast  
**Translation:** Vocabulary: uniquely: 独一无二地

**[10822.60s] English:** way so most of my you know my big wins in a lot of ways from all the way from the early games through  
**Translation:** 

**[10829.06s] English:** you know through vr and the aerospace work that i'm doing and or did and hopefully the ai work  
**Translation:** Vocabulary: aerospace: 航空航天

**[10834.32s] English:** that i'm working on now is finding an angle on something that means you trade off something that  
**Translation:** 

**[10840.50s] English:** you maybe think you need but it turns out you don't need and by making a sacrifice in one place  
**Translation:** Vocabulary: sacrifice: 牺牲

**[10845.56s] English:** you can get big advantages in another place is it clear at which level of the system  
**Translation:** 

**[10850.88s] English:** those big advantages can be gained it's not always clear and that's why the thing that that i try to  
**Translation:** 

**[10858.42s] English:** make one of my  
**Translation:** 

**[10859.04s] English:** core values and i i proselytize to a lot of people is trying to know the entire stack you know trying  
**Translation:** Vocabulary: proselytize: 传教

**[10865.80s] English:** to see through everything that happens and it's almost impossible on like the web browser level  
**Translation:** 

**[10871.28s] English:** of things where there's so many levels to it but you should at least understand what they all are  
**Translation:** 

**[10875.82s] English:** even if you can't understand all the performance characteristics at each level but it goes all  
**Translation:** 

**[10880.90s] English:** the way down to literally the hardware so what does the what is this chip capable of and what  
**Translation:** 

**[10887.06s] English:** is this software that you're writing capable  
**Translation:** 

**[10889.04s] English:** of and then with this architecture you put on top of that then the ecosystem around it all the people  
**Translation:** 

**[10893.92s] English:** that are that are working on it so there are there are all these decisions and they're never  
**Translation:** 

**[10899.40s] English:** made in a globally optimal way but sometimes you can drive a thread of global optimality through it  
**Translation:** Vocabulary: globally: 全球地; optimal: 最优的; optimality: 最优化

**[10905.10s] English:** you can't look at everything it's too complicated but sometimes you can step back up and make a  
**Translation:** 

**[10910.76s] English:** different decision and we kind of went through this on the graphics side on quake where i in  
**Translation:** 

**[10915.40s] English:** some ways it was kind of bad where michael would spend his time  
**Translation:** 

**[10918.40s] English:** writing like i'd i'd  
**Translation:** 

**[10920.00s] English:** rough out the basic routines like okay here's our span rasterizer and he would spend a month  
**Translation:** 

**[10925.32s] English:** writing this you know beautiful cycle optimized piece of assembly language that does you know  
**Translation:** Vocabulary: optimized: 优化; rasterizer: 光栅化器

**[10931.76s] English:** does what i asked it to do and he did it faster than like my original code would do or probably  
**Translation:** 

**[10936.80s] English:** what i would be able to do even if i had spent that month on it uh but then we'd have some cases  
**Translation:** 

**[10941.58s] English:** when i'd be like okay well i figured out at this higher level instead of drawing these in a painter's  
**Translation:** 

**[10947.42s] English:** order here i do a span buffer and it cuts out 30 or 40 of all of these pixels but it means you need  
**Translation:** Vocabulary: buffer: 缓冲区; pixels: 像素

**[10954.78s] English:** to rewrite kind of this interface of all of that and i could tell that wore on him a little bit but  
**Translation:** 

**[10959.56s] English:** in the end it was it was the right thing to do where we wound up changing that rasterization  
**Translation:** Vocabulary: interface: 用户界面; rasterization: 栅格化

**[10964.62s] English:** approach and we wound up with a super optimized assembly language uh core loop and then a good  
**Translation:** 

**[10970.72s] English:** system around it which minimized how much that had to be called and so in order to be able to do this  
**Translation:** Vocabulary: minimized: 减少

**[10975.94s] English:** kind of system level thinking  
**Translation:** 

**[10977.42s] English:** whether we're talking about uh game development aerospace nuclear energy ai vr you have to be able  
**Translation:** Vocabulary: aerospace: 航空航天

**[10988.68s] English:** to understand the hardware the low level software the high level software the design decisions the  
**Translation:** 

**[10995.96s] English:** whole thing the the full stack of it yeah and that's where a lot of these things become possible  
**Translation:** 

**[11001.18s] English:** when you're really when you're bringing the future forward i mean there's a pace that everything just  
**Translation:** 

**[11005.32s] English:** kind of glides towards where we have a lot of  
**Translation:** 

**[11007.42s] English:** progress that's happening at such a different so many different ways you kind of slide towards  
**Translation:** 

**[11011.50s] English:** progress just left to your own programs just get faster for a while it wasn't clear if they were  
**Translation:** 

**[11016.40s] English:** going to get fatter more than they get quicker than they get faster and it cancels out but it  
**Translation:** 

**[11020.96s] English:** is clear now in retrospect now programs just get faster and have gotten faster for a long time but  
**Translation:** Vocabulary: retrospect: 回顾

**[11026.78s] English:** if you want to do something like back at that original uh talking about scrolling games say  
**Translation:** 

**[11032.24s] English:** this needs to be five times faster well we can wait six years  
**Translation:** Vocabulary: scrolling: 滚动游戏

**[11037.42s] English:** and just it'll naturally get that much faster at that  
**Translation:** 

**[11040.00s] English:** time, or you come up with some really clever way of doing it. So there are those opportunities like  
**Translation:** 

**[11045.80s] English:** that in a whole bunch of different areas. Now, most programmers don't need to be thinking about  
**Translation:** 

**[11051.40s] English:** that. There's not that many, you know, there's a lot of opportunities for this, but it's not  
**Translation:** Vocabulary: programmers: 程序员

**[11055.52s] English:** everyone's workaday type stuff. So everyone doesn't have to know how all these things work.  
**Translation:** 

**[11060.32s] English:** They don't have to know how their compiler works, how, you know, the processor chip manages cache  
**Translation:** Vocabulary: cache: 缓存; processor: 处理器; workaday: 日常

**[11065.52s] English:** eviction and all these low-level things. But sometimes there are powerful opportunities  
**Translation:** 

**[11071.12s] English:** that you can look at and say, we can bring the future five years faster. You know, we can do  
**Translation:** Vocabulary: eviction: 驱逐

**[11077.62s] English:** something that, wouldn't it be great if we could do this? Well, we can do it today if we make a  
**Translation:** 

**[11082.70s] English:** certain set of decisions. And it is in some ways smoke and mirrors where you say it's like, Doom  
**Translation:** 

**[11088.70s] English:** was a lot of smoke and mirrors where people thought it was more capable than it actually was,  
**Translation:** 

**[11093.20s] English:** but we picked the right smoke.  
**Translation:** 

**[11095.52s] English:** Smoke and mirrors to deploy in the game where by doing this, people will think that it's more  
**Translation:** 

**[11100.32s] English:** general. We are going to amaze them with what they've got here, and they won't notice that  
**Translation:** Vocabulary: deploy: 部署

**[11105.22s] English:** it doesn't do these other things. So smart decision-making at that point, that's where  
**Translation:** 

**[11110.34s] English:** that kind of global, holistic, top-down view can work. And I'm really a strong believer that  
**Translation:** Vocabulary: believer: 信仰者; holistic: 整体的

**[11120.36s] English:** technology should be sitting at that table, having those discussions, because you do  
**Translation:** 

**[11125.50s] English:** have cases where you say, well, you want to be the Jonathan Ivey or whatever, where it's a pure  
**Translation:** 

**[11129.82s] English:** design solution. And that's, in some cases now, where you truly have almost infinite resources,  
**Translation:** 

**[11137.76s] English:** like if you're trying to do a scrolling game on the PC now, you don't even have to talk to a  
**Translation:** 

**[11142.58s] English:** technology person. You can just have, you know, any intern can make that go run as fast as it  
**Translation:** 

**[11147.80s] English:** needs to there, and it can be completely design-based. But if you're trying to do something  
**Translation:** Vocabulary: intern: 实习生

**[11151.92s] English:** that's hard, either that can't be done for resources, or that can't be done for the  
**Translation:** 

**[11155.50s] English:** VR on a mobile chipset, or that we don't even know how to do yet.  
**Translation:** 

**[11160.00s] English:** artificial general intelligence, it's probably going to be a matter of coming at it from an  
**Translation:** 

**[11164.90s] English:** angle. Like, I mean, for AGI, we have some of like, some of the Hutter principles about how you  
**Translation:** 

**[11169.60s] English:** can, you know, excite or some of that. There are theoretical ways that you can say this is the  
**Translation:** 

**[11173.90s] English:** optimal learning algorithm that can solve everything, but it's completely impractical.  
**Translation:** Vocabulary: algorithm: 算法; excite: 激发; impractical: 不实用; optimal: 最优

**[11178.40s] English:** You know, you just can't do that. So clearly, you have to make some concessions for general  
**Translation:** 

**[11184.10s] English:** intelligence. And nobody knows what the right ones are yet. So people are taking different  
**Translation:** Vocabulary: concessions: 妥协

**[11188.52s] English:** angles of attack. I hope I've got something clever to come up with in that space.  
**Translation:** 

**[11193.70s] English:** It's been surprising to me. And I think perhaps it is a principle of progress that smoke and  
**Translation:** 

**[11199.60s] English:** mirrors somehow is the way you build the future. You kind of, you kind of fake it till you make it  
**Translation:** 

**[11206.32s] English:** and you almost always make it. And I think that's going to be the way we achieve AGI. That's going  
**Translation:** 

**[11210.72s] English:** to be the way we build consciousness into our machines. There's, you know, philosophers debate  
**Translation:** 

**[11217.82s] English:** about that.  
**Translation:** 

**[11218.52s] English:** The Turing test is essentially about faking it till you make it. You start by faking it.  
**Translation:** 

**[11224.62s] English:** And I think that always leads to making it. Because if you look at history,  
**Translation:** Vocabulary: turing: 图灵测试

**[11230.70s] English:** arguments when, as soon as people start talking about qualia and consciousness and Chinese rooms  
**Translation:** 

**[11235.68s] English:** and things, it's like, I just check out. I just don't think there's any value in those  
**Translation:** Vocabulary: qualia: 主观体验

**[11239.26s] English:** conversations. It's just like, go ahead, tell me it's not going to work. I'm going to do my best  
**Translation:** 

**[11243.26s] English:** to try to make it work anyways. I don't know if you work with legged robots. There's a bunch of  
**Translation:** 

**[11247.48s] English:** these.  
**Translation:** 

**[11248.52s] English:** Um, they, they make, they sure as heck make me feel like they're cautious, uh, in a certain way  
**Translation:** 

**[11255.16s] English:** that's not here today, but is, um, you could see the kernel. It's like, uh, the, the, the, the flame,  
**Translation:** 

**[11264.54s] English:** the beginnings of a flame.  
**Translation:** Vocabulary: kernel: 胚芽

**[11266.10s] English:** We don't have line of sight, but there's glimmerings of light in the distance for all of  
**Translation:** 

**[11270.54s] English:** these things.  
**Translation:** Vocabulary: glimmerings: 微弱光芒

**[11271.02s] English:** Yeah. I'm hearing murmuring in a distant room. Um, well, let me ask you a human question here.  
**Translation:** 

**[11276.74s] English:** You, you've, uh,  
**Translation:** Vocabulary: murmuring: 低声议论

**[11277.82s] English:** in the game design space, you've,  
**Translation:** 

**[11280.00s] English:** you've done a lot of incredible work throughout but in terms of game design you have changed the  
**Translation:** 

**[11285.34s] English:** world and there's a few people around you that did the same so famously there's some animosity  
**Translation:** 

**[11290.90s] English:** there's much love but there's some animosity between you and john romero what is at the  
**Translation:** Vocabulary: animosity: 敌意

**[11297.32s] English:** core of that animosity and human tension and so there really hasn't been i for a long time and  
**Translation:** 

**[11304.16s] English:** even at the beginning it's like yes i am i did push romero out of the company and and this is  
**Translation:** 

**[11310.80s] English:** one of the things that i look back if i could go back telling my my younger self i some advice  
**Translation:** 

**[11316.50s] English:** about things the original founding i kind of corporate structure of id software really led  
**Translation:** Vocabulary: founding: 创立

**[11324.46s] English:** to a bunch of problems we started off with us as equal partners and we had a buy sell agreement  
**Translation:** 

**[11330.30s] English:** because we didn't want outsiders to be telling us what to do inside the company  
**Translation:** 

**[11333.90s] English:** and that did lead to a bunch of the problems where i was sitting here going it's like all right  
**Translation:** 

**[11340.34s] English:** i'm i'm working harder than anyone i'm doing these technologies you know nobody's done before  
**Translation:** 

**[11345.84s] English:** but we're all equal partners and then i see you know somebody that's not working as hard and i  
**Translation:** 

**[11351.96s] English:** and it's i mean i can't say i was the most mature about that i was you know 20 something years old  
**Translation:** 

**[11357.90s] English:** and i am and it did it did bother me when i'm like everybody okay we need to all pull together  
**Translation:** 

**[11363.86s] English:** and we've done it before everybody we know we can do this if we get together and we grind it all out  
**Translation:** Vocabulary: grind: 绞尽脑汁

**[11368.94s] English:** but not everybody wanted to do that for for all time you know and i was the youngest one of the  
**Translation:** 

**[11374.80s] English:** crowd there i i had different sets of uh kind of backgrounds and motivations and left at that point  
**Translation:** Vocabulary: motivations: 动机

**[11381.70s] English:** where it was i'm all right either everybody has to be contributing like up to this level or they  
**Translation:** 

**[11388.98s] English:** need to get pushed out was not i am that was not a great situation for me and i'm not a great situation  
**Translation:** 

**[11393.86s] English:** and i look back on it and know that we pushed people out of the company that could have contributed  
**Translation:** 

**[11400.00s] English:** if there was a different framework for them. And the modern kind of Silicon Valley, like,  
**Translation:** 

**[11405.08s] English:** let your stock vest over a time period, and maybe it's non-voting stock and all those different  
**Translation:** 

**[11409.58s] English:** things. We knew nothing about any of that. I mean, we didn't know what we were doing in terms of  
**Translation:** 

**[11414.46s] English:** corporate structure or anything. So if you think the framework was different,  
**Translation:** 

**[11418.40s] English:** some of the human tension could have been a little bit.  
**Translation:** 

**[11420.60s] English:** It almost certainly would have. I mean, I look back at that and it's like even trying to summon  
**Translation:** 

**[11426.50s] English:** up in my mind, it's like, I know I was really, really angry about, you know, like Romero not  
**Translation:** 

**[11433.36s] English:** working as hard as I wanted him to work or not carrying his load on the design for Quake and  
**Translation:** 

**[11439.12s] English:** coming up with things there. But, you know, he was definitely doing things. He made some of the  
**Translation:** 

**[11443.82s] English:** best levels there. He was working with some of our external teams like Raven on the licensing  
**Translation:** 

**[11449.00s] English:** side of things. But there were differences of opinion about it. But he landed, you know,  
**Translation:** Vocabulary: raven: 乌鸦

**[11456.42s] English:** I wouldn't say that he landed on the same level as Romero, but he landed on the same level as  
**Translation:** 

**[11456.48s] English:** Romero. And I think that's a good thing. I think that's a good thing. I think that's a good thing.  
**Translation:** 

**[11456.50s] English:** Right on his feet, he went and he got $20 million from Eidos to go do Ion Storm. And he got to do  
**Translation:** 

**[11462.04s] English:** things his way and spun up three teams simultaneously. Because that was always one  
**Translation:** Vocabulary: eidos: 理念

**[11466.44s] English:** of the challenging things in it where we were doing these single string one project after  
**Translation:** 

**[11472.18s] English:** another. And I think some of them, you know, wanted to grow the company more. And I didn't  
**Translation:** 

**[11477.16s] English:** because I knew people that were saying that, oh, companies turn to shit when you got 50 employees.  
**Translation:** 

**[11482.04s] English:** It's just a different world there. And I loved our little dozen people,  
**Translation:** 

**[11486.48s] English:** working on the projects. But you can look at it and say, well, business realities matter. It's  
**Translation:** 

**[11491.92s] English:** like you're super successful here. And we could take a swing and a miss on something, but you do  
**Translation:** 

**[11496.98s] English:** it a couple times and you're out of luck. There's a reason companies try to have multiple teams  
**Translation:** 

**[11502.96s] English:** running at one time. And so that was, again, something I didn't really appreciate back then.  
**Translation:** 

**[11509.70s] English:** So if you look past all that, you did create some amazing things together.  
**Translation:** 

**[11513.26s] English:** What did you love about John Romero? What did you respect?  
**Translation:** Vocabulary: romero: 罗梅罗

**[11516.48s] English:** And appreciate about him? What did you admire about him? What did you learn from him?  
**Translation:** 

**[11520.00s] English:** when i met him he was the coolest programmer i had ever met i you know he had done all of this  
**Translation:** 

**[11525.14s] English:** stuff he had he had made all of these games he had worked at i've you know one of the companies  
**Translation:** 

**[11529.98s] English:** that i thought was the coolest at origin systems and he knew all this stuff he made things happen  
**Translation:** 

**[11535.46s] English:** fast and he could he was also kind of a polymath about this where he could do he made his own he  
**Translation:** 

**[11540.50s] English:** drew his own art he made his own levels as well as i'm you know he worked on sound design systems  
**Translation:** Vocabulary: polymath: 博学之人

**[11546.08s] English:** on top of actually being a really good programmer and we had you know we went through a little it  
**Translation:** 

**[11552.10s] English:** was kind of fun where one of the early things that we did where there was kind of the young  
**Translation:** 

**[11555.90s] English:** buck bit going in where i was the new guy and he was the kind of the he was the top man programmer  
**Translation:** 

**[11562.50s] English:** at the soft disk area and eventually we had sort of a challenge over the weekend that we were going  
**Translation:** Vocabulary: programmer: 程序员

**[11567.54s] English:** to like race to to implement this game to port one of our pc games back down to the apple 2  
**Translation:** 

**[11572.24s] English:** and that was where we finally kind of became clear it's like okay  
**Translation:** 

**[11576.08s] English:** carmax stands a little bit apart on the programming side of things and uh but romero then  
**Translation:** 

**[11581.10s] English:** very gracefully moved into well he'll work on the tools he'll work on the systems i do some of the  
**Translation:** 

**[11586.68s] English:** game design stuff as well as contributing on uh starting to lead the design aspects of a lot of  
**Translation:** 

**[11591.90s] English:** things so he was you know enormously valuable in the early stuff and so much of doom and even quake  
**Translation:** Vocabulary: enormously: 极其

**[11599.08s] English:** have his stamp on it in a lot of ways but i am you know he wasn't at the same level of focus that  
**Translation:** 

**[11606.08s] English:** i brought to the the work that we were doing there and he really did i we hit such a degree  
**Translation:** 

**[11612.72s] English:** of success that it was all in the press about that the rock star game programmers yeah i mean  
**Translation:** 

**[11618.68s] English:** it's the beatles problem yeah i mean and you know he ate it up and he did personify there was the  
**Translation:** Vocabulary: beatles: 甲壳虫乐队; personify: 化身; programmers: 程序员

**[11623.66s] English:** whole game developers with uh you know with ferraris that i that we had there and i thought  
**Translation:** 

**[11629.68s] English:** that you know that led to some uh some challenges there but so much of the  
**Translation:** Vocabulary: ferraris: 法拉利跑车

**[11636.08s] English:** uh you know the stuff that was great in the games did come from him and i would certainly  
**Translation:** 

**[11640.00s] English:** not take that away from him. And even after we parted ways and he took his swing with Eidos,  
**Translation:** Vocabulary: eidos: 形式

**[11646.88s] English:** in some ways he was ahead of the curve with mobile gaming as well, where one of his companies after  
**Translation:** 

**[11652.90s] English:** Eidos was working on feature phone game development. And I wound up doing some of that  
**Translation:** 

**[11658.96s] English:** just before the iPhone crossing over into the iPhone phase there. And that was something that  
**Translation:** 

**[11664.38s] English:** clearly did turn out to be a huge thing, although he was too early for what he was working on.  
**Translation:** 

**[11669.92s] English:** At that time, we've had pretty cordial relationships where I was happy to talk  
**Translation:** 

**[11675.20s] English:** with him anytime I'd run into him at a conference. I've actually had some other people just say,  
**Translation:** Vocabulary: anytime: 任何时候

**[11680.70s] English:** it's like, oh, you shouldn't go over there and give him the time of day, or felt that  
**Translation:** 

**[11685.34s] English:** Masters of Doom played things up in a way that I shouldn't be too happy with. But I'm okay with  
**Translation:** 

**[11694.02s] English:** all of that. So you've still got love in your heart. Yeah. I mean, I just talked with him  
**Translation:** 

**[11697.86s] English:** like last year.  
**Translation:** 

**[11699.92s] English:** I guess it was even this year about mentioning that I'm going off doing this AI stuff. I'm  
**Translation:** 

**[11704.04s] English:** going big into artificial intelligence. And he had a bunch of ideas for how AI is going to play  
**Translation:** 

**[11710.16s] English:** into gaming and asked if I was interested in collaborating. And it's not in line with what  
**Translation:** 

**[11714.88s] English:** I'm doing, but I do, I wish almost everyone the best. I mean, I know I may not have parted on the  
**Translation:** Vocabulary: collaborating: 合作

**[11721.86s] English:** best of terms with some people, but I was thrilled to see Tom Hall writing VR games now. He wrote,  
**Translation:** 

**[11729.92s] English:** working on a game called Demio, which is really an awesome VR game. It's like Dungeons and Dragons.  
**Translation:** Vocabulary: dragons: 龙; dungeons: 地牢; thrilled: 兴奋

**[11734.92s] English:** We all used to play Dungeons and Dragons together. That was one of the things, that was what we did  
**Translation:** 

**[11738.10s] English:** on Sundays in the early days. I would Dungeon Master and they'd all play. And I, you know,  
**Translation:** Vocabulary: dungeon: 地牢

**[11743.40s] English:** so it really made me smile seeing Tom involved with an RPG game in virtual reality.  
**Translation:** 

**[11749.30s] English:** You were the CTO of Oculus VR since 2013, and maybe less than your involvement a bit in 2019.  
**Translation:** Vocabulary: oculus: Oculus眼镜

**[11759.92s] English:** Yeah, yeah, yeah.  
**Translation:** 

**[11760.00s] English:** Oculus was acquired by Facebook Now Meta in 2014.  
**Translation:** 

**[11764.92s] English:** You've spoken brilliantly about both the low-level details, the experimental design, and the big-picture vision of virtual reality.  
**Translation:** 

**[11771.82s] English:** Let me ask you about the metaverse, the big question here, both philosophically and technically.  
**Translation:** Vocabulary: brilliantly: 精彩地; metaverse: 元宇宙; philosophically: 哲学上

**[11777.98s] English:** How hard is it to build the metaverse?  
**Translation:** 

**[11780.18s] English:** What is the metaverse in your view?  
**Translation:** 

**[11782.64s] English:** You started with discussing and thinking about Quake as a kind of metaverse.  
**Translation:** 

**[11786.10s] English:** As you think about it today, what is the metaverse, the thing that could create this compelling user value, this experience that will change the world, and how hard is it to build it?  
**Translation:** Vocabulary: compelling: 引人入胜的

**[11799.04s] English:** The term comes from Neil Stevenson's book Snow Crash, which many of us had read back in the 90s.  
**Translation:** 

**[11804.62s] English:** It was one of those kind of formative books.  
**Translation:** 

**[11807.60s] English:** There was this sense that the possibilities and the freedom and unlimited capabilities,  
**Translation:** 

**[11816.10s] English:** to build a virtual world that does whatever you want, whatever you ask of it,  
**Translation:** 

**[11820.94s] English:** has been a powerful draw for generations of developers, game developers specifically,  
**Translation:** 

**[11825.66s] English:** and people that are thinking about more general-purpose applications.  
**Translation:** 

**[11829.90s] English:** We were talking about that back in the Doom and Quake days,  
**Translation:** 

**[11833.66s] English:** about how do you wind up with an interconnected set of worlds that you visit from one to another.  
**Translation:** Vocabulary: interconnected: 相互连接

**[11839.28s] English:** As webpages were becoming a thing, you start thinking about what is the interactive 3D-based,  
**Translation:** 

**[11846.10s] English:** equivalent of this, and there were a lot of really bad takes.  
**Translation:** Vocabulary: interactive: 交互式; webpages: 网页

**[11849.86s] English:** You had, like, verbal and virtual reality markup languages,  
**Translation:** 

**[11854.24s] English:** and there's aspects like that that came from people saying,  
**Translation:** Vocabulary: markup: 标记语言

**[11858.26s] English:** well, what kind of capabilities should we develop to enable this?  
**Translation:** 

**[11863.42s] English:** And that kind of capability-first work has usually not panned out very well.  
**Translation:** 

**[11868.70s] English:** On the other hand, we have successful games that started with things like Doom and Quake  
**Translation:** 

**[11873.56s] English:** and communities that formed around those.  
**Translation:** 

**[11876.10s] English:** Whether it was server lists in the early days or, you know, literal portaling.  
**Translation:** 

**[11880.00s] English:** between different games and then modern things that are on completely different order of magnitude  
**Translation:** Vocabulary: portaling: 传送

**[11885.26s] English:** like minecraft and fortnite that have 100 million plus users um you know i still think that that's  
**Translation:** 

**[11892.86s] English:** the right way to go to build the metaverse is you build something that's amazing that people love  
**Translation:** Vocabulary: fortnite: 堡垒之夜; metaverse: 元宇宙

**[11898.16s] English:** and people wind up spending all their time in uh because it's awesome and you expand the  
**Translation:** 

**[11902.80s] English:** capabilities of that so even if it's a very basic experience as long as people minecraft is  
**Translation:** 

**[11908.28s] English:** minecraft is an amazing case study in so many things where what's been able to be done with that  
**Translation:** 

**[11914.14s] English:** is really enlightening and there are other cases where like right now roblox is basically a game  
**Translation:** Vocabulary: enlightening: 启发性的

**[11921.46s] English:** construction kit aimed at kids and that was a capability first play and it's achieving scale  
**Translation:** 

**[11926.20s] English:** that's on the same order of those things so it's not impossible but my preferred bet would be you  
**Translation:** Vocabulary: capability: 能力

**[11933.50s] English:** make something amazing that people love and you make it better and better and that's where i could  
**Translation:** 

**[11937.78s] English:** say  
**Translation:** 

**[11938.28s] English:** we could have gone back and followed a path kind of like that in the early days  
**Translation:** 

**[11942.46s] English:** if you just kind of take the same game whether it's when activision demonstrated that you could  
**Translation:** Vocabulary: activision: 暴雪娱乐

**[11947.40s] English:** make call of duty every year and not only is it not bad people kind of love it and it's a  
**Translation:** 

**[11952.74s] English:** it's very profitable the idea that you could have taken something like that  
**Translation:** 

**[11956.92s] English:** it take a great game release a new version every year that lets the capabilities grow and expand  
**Translation:** 

**[11962.68s] English:** to start saying it's like okay it's a game about running around and shooting things but  
**Translation:** 

**[11967.08s] English:** now you can have a game that's not bad and it's not bad and it's not bad and it's not bad and it's not  
**Translation:** 

**[11968.26s] English:** bad and it's not bad and it's not bad and it's not bad and you can do a lot of things watching it  
**Translation:** 

**[11970.52s] English:** you can add persistence of social sense sign of signs of life or whatever you want to add to it  
**Translation:** 

**[11976.58s] English:** uh i still think that's you know quite a good position to take and i think that  
**Translation:** Vocabulary: persistence: 持久性

**[11982.64s] English:** while meta is doing a bottoms-up capability approach with horizon worlds where it's a fairly  
**Translation:** 

**[11989.14s] English:** general purpose creators can build whatever they want in their sort of thing i am you know it's  
**Translation:** 

**[11995.56s] English:** it's hard to compare and compete with something like  
**Translation:** 

**[11998.26s] English:** Fortnite, which also has...  
**Translation:** 

**[12000.00s] English:** enormous amounts of creativity, even though it was not designed originally as a general purpose  
**Translation:** 

**[12004.58s] English:** sort of thing. So there's, we have examples on both sides. Me personally, I would have bet on  
**Translation:** 

**[12010.84s] English:** trying to do entertainment, valuable destination first and expanding from there.  
**Translation:** 

**[12016.62s] English:** So can you imagine the thing that will be kind of, if we look back a couple of centuries from now  
**Translation:** 

**[12024.90s] English:** and you think about the experiences that marked the singularity, the transition  
**Translation:** 

**[12031.72s] English:** where most of our world moved into virtual reality, what do you think those experiences  
**Translation:** 

**[12039.00s] English:** will look like? So I do think it's going to be kind of like the way the web slowly took over,  
**Translation:** 

**[12044.78s] English:** where you're the frog in the pot of water that's slowly heating up, where having lived through all  
**Translation:** 

**[12050.72s] English:** of that, I remember when it was shocking to start seeing the first  
**Translation:** 

**[12054.88s] English:** website address on a billboard, when you're like, Hey, my computer world is in infecting the real  
**Translation:** Vocabulary: billboard: 广告牌; infecting: 侵入

**[12059.90s] English:** world. You know, this is spreading out in some way, but there's still, when you look back and  
**Translation:** 

**[12065.20s] English:** say, well, what, what made the web take off? And it wasn't a big bang sort of moment there.  
**Translation:** 

**[12071.76s] English:** It was a bunch of little things that turned out not to even be the things that are relevant now  
**Translation:** 

**[12076.82s] English:** that brought them into it. So I wonder if from, I mean, like you said, you're not a historian,  
**Translation:** 

**[12082.48s] English:** so maybe there's a,  
**Translation:** 

**[12084.88s] English:** historian out there that could really identify that moment, the data driven way. It could be  
**Translation:** 

**[12091.14s] English:** like MySpace or something like that. Maybe the first major social network that really reached  
**Translation:** 

**[12097.32s] English:** into non-geek world or something like that. I think that's kind of the fallacy of historians,  
**Translation:** Vocabulary: fallacy: 谬误

**[12104.62s] English:** though, looking for some of those kind of primary dominant causes where so many of these things are  
**Translation:** 

**[12110.98s] English:** like, we see an exponential curve, but it's not because like one thing,  
**Translation:** Vocabulary: exponential: 指数的

**[12114.88s] English:** is going exponential. It's because we have hundreds of little sigmoid curves overlapped on  
**Translation:** 

**[12120.00s] English:** And they just happen to keep adding up so that you've got something kind of going exponential at any given point. But no single one of them was the critical thing. There were dozens and dozens of things. I mean, seeing the transitions of stuff like as obviously MySpace giving way to other things, but even like blogging giving way to social media and getting resurrected in other guises and things that happened there.  
**Translation:** Vocabulary: guises: 形式; overlapped: 重叠; resurrected: 复活; sigmoid: S形; transitions: 转变

**[12144.72s] English:** Dancing baby gif or whatever the all your base now belong to us, whatever those early memes that led to the modern memes and the humor on the different evolution of humor on the Internet.  
**Translation:** 

**[12157.36s] English:** And I'm sure the historians will also write books about from the different website that support to create the infrastructure for that humor, like Reddit and all that kind of stuff.  
**Translation:** 

**[12166.42s] English:** So people will go back and they will name firsts and critical moments, but it's probably going to be a poor approximation of what actually happens.  
**Translation:** 

**[12174.72s] English:** And we've already seen like in the VR space where it didn't play out the way we thought it would in terms of what was going to be like when the modern era of VR basically started with my E3 demo of Doom 3 on the Rift prototype.  
**Translation:** Vocabulary: approximation: 近似; prototype: 原型

**[12188.20s] English:** So we're like first person shooters in VR match made in heaven. Right. And that didn't work out that way at all. They have, you know, they have the most comfort problems with it. And then the most popular virtual reality app is Beat Saber, which nobody predicted back then.  
**Translation:** 

**[12204.72s] English:** What's that make you like from first principles, if you were to like reverse engineer that, why are these like silly fun games?  
**Translation:** Vocabulary: saber: 剑

**[12214.28s] English:** Well, it actually makes very clear sense when you when you analyze it from from hindsight and look at the engineering reasons where it's not just that it was a magical, quirky idea.  
**Translation:** 

**[12225.22s] English:** It was something that played almost perfectly to what turned out to be the real strengths of VR, where the one thing that I really underestimated importance in VR was the importance of VR.  
**Translation:** Vocabulary: hindsight: 事后诸葛; quirky: 古怪的; underestimated: 低估了

**[12234.72s] English:** And so the controllers, you know, I was still thinking we could do a lot more with with the game pad and just the.  
**Translation:** 

**[12240.00s] English:** amazingness of taking any existing game being able to move your head around and look around  
**Translation:** Vocabulary: amazingness: 惊奇之处

**[12243.92s] English:** that that was you know that was really amazing but the controllers uh were super important but  
**Translation:** 

**[12249.12s] English:** the problem is so many things that you do with the controllers just suck it feels like it breaks the  
**Translation:** 

**[12254.40s] English:** illusion like trying to pick up glasses with the controllers where you're like oh use the grip  
**Translation:** 

**[12258.14s] English:** button when you're kind of close and it'll snap into your hand all of those things are unnatural  
**Translation:** Vocabulary: unnatural: 不自然

**[12263.10s] English:** uh actions that you do them and it's still part of the vr experience but beat saber  
**Translation:** 

**[12269.46s] English:** winds up i playing only to the strengths it completely hides all the weaknesses of it  
**Translation:** 

**[12274.62s] English:** because you are holding something in your hand you keep a solid grip on it the whole time  
**Translation:** 

**[12279.06s] English:** it slices through things without ever bumping into things you never get into the point where  
**Translation:** 

**[12283.72s] English:** you know i'm knocking on this table but in vr my hand just goes right through it so you've got  
**Translation:** 

**[12288.62s] English:** something that slices through so it's never your brain telling you oh i should have hit something  
**Translation:** 

**[12294.24s] English:** you've got a lightsaber here it's just you expect it to slice through everything uh audio  
**Translation:** 

**[12299.46s] English:** and music turned out to be a really powerful aspect of virtual reality where you're blocking  
**Translation:** Vocabulary: lightsaber: 光剑

**[12304.32s] English:** the world off and constructing the world around you and i and being something that can run  
**Translation:** 

**[12310.12s] English:** efficiently on even this relatively low powered hardware and can have a valuable loop in a small  
**Translation:** Vocabulary: efficiently: 运行高效地

**[12316.78s] English:** amount of time where a lot of modern games you're supposed to sit down and play it for an hour just  
**Translation:** 

**[12321.62s] English:** to get anywhere sometimes a new game takes an hour to get through the tutorial level  
**Translation:** 

**[12325.10s] English:** and that's not good for vr for a couple reasons you do still have the comfort issues  
**Translation:** 

**[12329.46s] English:** if you're moving around at all but you've also got just you know discomfort from the headset  
**Translation:** 

**[12334.52s] English:** battery lifespan on the mobile versions so having things that do break down into three and four  
**Translation:** 

**[12340.56s] English:** minute windows of play that turns out to be very valuable from a gameplay standpoint so it winds up  
**Translation:** Vocabulary: lifespan: 使用寿命; standpoint: 视角

**[12346.98s] English:** being kind of a perfect storm of all of these things that are really good it doesn't have any  
**Translation:** 

**[12351.00s] English:** of the comfort problems you're not navigating around you're standing still all the stuff flies  
**Translation:** Vocabulary: navigating: 驾驶

**[12355.68s] English:** at you it has placed audio strengths i  
**Translation:** 

**[12359.46s] English:** it adds the  
**Translation:** 

**[12360.00s] English:** whole the whole fitness in vr nobody was thinking about that back in the at the beginning and it  
**Translation:** 

**[12364.70s] English:** turns out that that is an excellent daily fitness thing to be doing if you go play uh an hour of  
**Translation:** 

**[12371.28s] English:** beat saver or supernatural or something that is legit solid exercise uh and it's more fun than  
**Translation:** 

**[12377.60s] English:** doing it just about any other way there so that's kind of the arcade stage of things if i were to  
**Translation:** Vocabulary: arcade: 街机; legit: 真实的; supernatural: 超自然的

**[12384.04s] English:** say with my experience with vr the thing that i think is powerful is the maybe it's not here yet  
**Translation:** 

**[12391.90s] English:** but the degree to which it is immersive in the way that quake is immersive it takes you to another  
**Translation:** Vocabulary: immersive: 身临其境

**[12399.22s] English:** world for me because i'm a fan of role-playing games uh the elder scroll series uh like skyrim  
**Translation:** 

**[12408.82s] English:** or even daggerfall it just takes you to another world and when you're not in that world  
**Translation:** Vocabulary: daggerfall: 刀锋传说; scroll: 手卷

**[12413.86s] English:** you're not in that world you're not in that world  
**Translation:** 

**[12414.02s] English:** you're not in that world you're not in that world you're not in that world you're not in that world  
**Translation:** 

**[12414.04s] English:** you miss not being there and then you just you kind of want to stay there forever because life is  
**Translation:** 

**[12419.64s] English:** shitty the whole point you just want to go to this place is that i there was a there was a time when  
**Translation:** Vocabulary: shitty: 糟糕

**[12427.76s] English:** i we were kind of asked to come up with like what's your view about vr and i am you know my  
**Translation:** 

**[12434.04s] English:** pitch was that it should be better inside the headset than outside it's the world as you want  
**Translation:** Vocabulary: headset: 耳机

**[12438.78s] English:** it yeah and everybody thought that was dystopian and like that's like oh you're just going to  
**Translation:** 

**[12443.80s] English:** forget about the world outside and i don't get that mindset where the idea that if you can make  
**Translation:** Vocabulary: dystopian: 乌托邦式; mindset: 思维模式

**[12450.72s] English:** the world better inside the headset than outside you've just improved the person's life that's  
**Translation:** 

**[12456.52s] English:** has a headset that can wear it and there are plenty of things that we just can't do for  
**Translation:** 

**[12461.46s] English:** everyone in the real world everybody can't have richard branson's private island but everyone  
**Translation:** 

**[12465.28s] English:** can have a private vr island and it can have the things that they want on it and there's a lot of  
**Translation:** 

**[12470.04s] English:** these kind of rivalrous goods in the real world that vr can  
**Translation:** 

**[12473.74s] English:** just forget about the world outside and i don't get that mindset where the idea that if you can  
**Translation:** Vocabulary: rivalrous: 竞争性的

**[12473.78s] English:** just be better at we can do a lot of things like that that can be very very rich so yeah  
**Translation:** 

**[12480.00s] English:** I think it's going to be a positive thing, this world, where people want to go back into their headset, where it can be better than somebody that's living in a tiny apartment can have a palatial estate in virtual reality.  
**Translation:** 

**[12492.04s] English:** They can have all their friends from all over the world come over and visit them without everybody getting on a plane and meeting in some place and dealing with all the other logistics hassles.  
**Translation:** 

**[12501.74s] English:** There is real value in the presence that you can get for remote meetings.  
**Translation:** Vocabulary: hassles: 麻烦

**[12506.40s] English:** It's all the little things that we need to sort out, but those are things that we have line of sight on.  
**Translation:** 

**[12512.88s] English:** People that have been in a good VR meeting using workrooms where you can say, oh, that was better than a Zoom meeting.  
**Translation:** Vocabulary: workrooms: 虚拟会议室

**[12520.38s] English:** But, of course, it's more of a hassle to get into it.  
**Translation:** 

**[12522.98s] English:** Not everyone has a headset.  
**Translation:** Vocabulary: hassle: 麻烦

**[12524.86s] English:** Interoperability is worse.  
**Translation:** 

**[12526.32s] English:** You can't have – you cap out at a certain number.  
**Translation:** Vocabulary: interoperability: 兼容性

**[12528.64s] English:** There's all these things that need to be fixed, but that's one of those things you can look at and say, we know there's value there.  
**Translation:** 

**[12533.94s] English:** We just need to really grind hard.  
**Translation:** Vocabulary: grind: 努力工作

**[12536.40s] English:** File off all the rough edges and make that possible.  
**Translation:** 

**[12539.56s] English:** So you do think we have line of sight because there's a reason, like, I do this podcast in person, for example.  
**Translation:** 

**[12551.00s] English:** Doing it remotely, it's not the same.  
**Translation:** 

**[12554.20s] English:** And if somebody were to ask me why it's not the same, I wouldn't be able to write down exactly why.  
**Translation:** Vocabulary: remotely: 远程地

**[12560.24s] English:** But you're saying that it's possible, whatever the magic is for in-person interaction.  
**Translation:** 

**[12566.86s] English:** That immersiveness of the experience.  
**Translation:** Vocabulary: immersiveness: 沉浸感

**[12570.34s] English:** We are almost there.  
**Translation:** 

**[12572.20s] English:** Yes.  
**Translation:** 

**[12572.72s] English:** So it's a technical problem.  
**Translation:** 

**[12573.80s] English:** So the idea of, like, I'm doing a VR interview with someone.  
**Translation:** 

**[12577.66s] English:** I'm not saying it's here right now, but you can see glimmers of what it should be.  
**Translation:** 

**[12582.60s] English:** And we largely know what would need to be fixed and improved to – like you say, there's a difference between a remote interview doing a podcast over Zoom or something and face-to-face.  
**Translation:** 

**[12594.02s] English:** There's that sense of presence, that immediacy.  
**Translation:** 

**[12596.40s] English:** The super low-latency responsiveness, being able to see all the –  
**Translation:** Vocabulary: immediacy: 即时性; responsiveness: 响应性

**[12600.00s] English:** the subtle things there, just occupying the same field of view. And all of those are things that we  
**Translation:** 

**[12605.14s] English:** absolutely can do in VR. And that simple case of a small meeting with a couple people, that's the  
**Translation:** 

**[12612.06s] English:** much easier case than everybody thinks the Ready Player One multiverse with a thousand people going  
**Translation:** 

**[12616.60s] English:** across a huge bridge to amazing places. That's harder in a lot of other technical ways. Not to  
**Translation:** Vocabulary: multiverse: 多宇宙

**[12622.76s] English:** say we can't also do that, but that's further away and has more challenges. But this small thing  
**Translation:** 

**[12627.54s] English:** about being able to have a meeting with one or a few people and have it feel real, feel like you're  
**Translation:** 

**[12634.54s] English:** there. You have the same interactions and talking with them. You get subtle cues as we start getting  
**Translation:** 

**[12640.18s] English:** eye and face tracking and some of the other things on high-end headsets. A lot of that is going to  
**Translation:** 

**[12645.36s] English:** come over. And it doesn't have to be as good. This is an important thing that people miss where  
**Translation:** 

**[12651.38s] English:** there was a lot of people that, especially rich people, that would look at VR and say it's like,  
**Translation:** 

**[12657.54s] English:** well, this just isn't that good. And I'd say it's like, well, you've already been courtside,  
**Translation:** 

**[12663.02s] English:** backstage, and on pit row, and you've done all of these experiences because you get to do them in  
**Translation:** Vocabulary: backstage: 后台; courtside: 靠近球场

**[12668.06s] English:** real life. But most people don't get to. And even if the experience is only half as good, if it's  
**Translation:** 

**[12673.70s] English:** something that they never would have gotten to do before, it's still a very good thing. And as we  
**Translation:** 

**[12678.18s] English:** can push that number up over time, it has a minimum viable value level when it does something  
**Translation:** 

**[12685.62s] English:** that is valuable enough to people. As long as it's not that good, it's still a very good thing.  
**Translation:** 

**[12687.52s] English:** As long as it's better inside the headset on any metric than it is outside, and people choose to  
**Translation:** 

**[12691.86s] English:** go there, we're on the right path. And we have a value gradient that I'm just always hammering on.  
**Translation:** Vocabulary: gradient: 梯度; hammering: 强调; headset: 耳罩

**[12697.14s] English:** We can just follow this value gradient, just keep making things better, rather than going for that  
**Translation:** 

**[12702.98s] English:** one close your eyes, swing for the fences, kind of silver bullet approach.  
**Translation:** 

**[12708.78s] English:** Well, I wonder if there's a value gradient for in-person meetings. Because if you get that right,  
**Translation:** 

**[12713.16s] English:** I mean, that would change the world. It doesn't need to,  
**Translation:** 

**[12716.14s] English:** I mean, you don't need a ready player one. But  
**Translation:** 

**[12720.00s] English:** I wonder if there's that value gradient you can follow along, because if there is and you follow it, then there'll be a certain like phase shift.  
**Translation:** 

**[12731.44s] English:** It's a certain point where people will shift from from Zoom to this.  
**Translation:** 

**[12738.38s] English:** I wonder what what are the bottlenecks? Is it software? Is it hardware? Is it like is it is it all about latency?  
**Translation:** Vocabulary: bottlenecks: 瓶颈; latency: 延迟

**[12747.40s] English:** So I have big arguments internally about strategic things like that, where I like the next headset that's coming out and that we've made various announcements about is going to be a higher end headset, more expensive, more features.  
**Translation:** 

**[12762.08s] English:** Lots of people want to make those those tradeoffs.  
**Translation:** Vocabulary: internally: 内部; tradeoffs: 权衡取舍

**[12764.72s] English:** I will see what the market has to say about the exact tradeoffs we've made here.  
**Translation:** 

**[12769.46s] English:** But if you want to replace Zoom, you need to have something that everybody has.  
**Translation:** 

**[12774.64s] English:** So you like cheaper?  
**Translation:** 

**[12776.40s] English:** I like cheaper.  
**Translation:** 

**[12777.40s] English:** Because also lighter and cheaper wind up being a virtuous cycle there where expensive and more features tends to also lead towards heavier.  
**Translation:** 

**[12787.34s] English:** And it just kind of goes, it's like, let's add more features.  
**Translation:** Vocabulary: virtuous: 良性循环

**[12789.68s] English:** The features are not, you know, they have physical presence and weight and draw from batteries and all of those things.  
**Translation:** 

**[12796.12s] English:** So I've always favored a lower end, cheaper, faster approach.  
**Translation:** 

**[12801.28s] English:** That's why I was always behind the mobile side of VR rather than the higher end PC headsets.  
**Translation:** 

**[12806.28s] English:** And I think that's.  
**Translation:** 

**[12807.40s] English:** You know, that's proven out well.  
**Translation:** 

**[12809.66s] English:** But there's you always.  
**Translation:** 

**[12811.24s] English:** Ideally, we have a whole range of things.  
**Translation:** 

**[12812.76s] English:** But if you've only got one or two things, it's important that those two things cover the, you know, the scope that you think is most important when we're in a world when it's like cell phones and there's 50 of them on the market covering every conceivable ecological niche you want.  
**Translation:** Vocabulary: conceivable: 可想象的; niche: 细分市场

**[12826.90s] English:** That's going to be great.  
**Translation:** 

**[12827.82s] English:** But we're not going to be there for a while.  
**Translation:** 

**[12830.14s] English:** Where are the bottlenecks?  
**Translation:** 

**[12831.52s] English:** Is it the hardware or the software?  
**Translation:** 

**[12833.40s] English:** Yeah.  
**Translation:** 

**[12833.60s] English:** So right now I am.  
**Translation:** 

**[12835.70s] English:** You can play.  
**Translation:** 

**[12836.36s] English:** You can get.  
**Translation:** 

**[12836.88s] English:** Work rooms on Quest and you can set up these.  
**Translation:** 

**[12840.00s] English:** things and it's a pretty good experience. It's surprisingly good. I haven't tried it. It's  
**Translation:** 

**[12843.88s] English:** surprisingly good. Yeah. The voice latency is better on that than a lot better than a zoom  
**Translation:** 

**[12849.58s] English:** meeting. So you've got a more, a better sense of immediacy there. The expressions that you get from  
**Translation:** Vocabulary: immediacy: 即时性

**[12855.74s] English:** the current hardware with just kind of your controllers and your head is pretty realistic  
**Translation:** 

**[12861.04s] English:** feeling. And you've got a pretty good sense of being there with someone. Are these like, um,  
**Translation:** 

**[12865.58s] English:** um, avatars of people? Like do you, do you get, do you get to see their body and they're sitting  
**Translation:** 

**[12871.54s] English:** around a table and it feel, it feels better than zoom better than you. Yeah. Better than you'd  
**Translation:** Vocabulary: avatars: 化身

**[12876.98s] English:** expect for that. It is definitely. Yeah. I'd say it's, it's quite a bit better than zoom when  
**Translation:** 

**[12882.74s] English:** everything's working. Right. But there's still all the rough edges of the reason zoom became  
**Translation:** 

**[12887.42s] English:** so successful is because they just nailed the usability of everything. It's high quality with  
**Translation:** 

**[12892.28s] English:** absolutely first rate experience.  
**Translation:** Vocabulary: usability: 易用性

**[12894.50s] English:** And we are not there yet with any of the VR stuff I'm trying to, to push hard to get. I,  
**Translation:** 

**[12901.14s] English:** I keep talking about, it's like, it needs to just be one click to make everything happen. And we're  
**Translation:** 

**[12905.32s] English:** getting there in our, our home environment, not the whole workrooms application, but the main home  
**Translation:** 

**[12909.96s] English:** where you can now kind of go over and click an invite. And it still winds up taking five times  
**Translation:** Vocabulary: workrooms: 办公空间

**[12914.80s] English:** longer than it should, but we're getting close to that where you click there, they click on their  
**Translation:** 

**[12920.28s] English:** button and then they're sitting there in this good presence with you.  
**Translation:** 

**[12923.98s] English:** Yeah.  
**Translation:** 

**[12924.12s] English:** But latencies need to get a lot better. User interface needs to get a lot better.  
**Translation:** Vocabulary: interface: 用户界面; latencies: 延迟

**[12928.52s] English:** I'm ubiquity of the headsets needs to get better. We need to have a hundred million of them out  
**Translation:** 

**[12933.44s] English:** there just so that everybody knows somebody that uses this all the time.  
**Translation:** Vocabulary: headsets: 耳机; ubiquity: 无处不在

**[12937.36s] English:** Well, I think it's a virtuous cycle because I do think the interface  
**Translation:** 

**[12942.40s] English:** is the thing that makes or breaks this kind of revolution. It's so interesting how like,  
**Translation:** Vocabulary: virtuous: 良性循环

**[12949.44s] English:** uh, you said one click, but it's also like how you achieve that one click.  
**Translation:** 

**[12952.94s] English:** I don't know. What is, um, can I ask a dark question? Maybe let's keep it outside of  
**Translation:** 

**[12960.00s] English:** but this is about meta but also google and big company are they able to do this kind of thing  
**Translation:** 

**[12967.48s] English:** it seems like let me put on my cranky old man hat is they seem to not do a good job of  
**Translation:** Vocabulary: cranky: 爱发牢骚的

**[12976.00s] English:** creating these user-friendly interfaces as they get bigger and bigger as a company  
**Translation:** 

**[12982.28s] English:** like google has created some of the greatest interfaces ever uh early on and it's i mean  
**Translation:** Vocabulary: interfaces: 人机界面

**[12988.30s] English:** creating gmail just so many brilliant interfaces and it just seems to be getting crappier and  
**Translation:** 

**[12996.06s] English:** crappier at that same with meta same with uh uh microsoft it's just it seems to get worse and  
**Translation:** Vocabulary: crappier: 更糟糕

**[13003.92s] English:** worse at that is this i don't know what is it because you've become more conservative careful  
**Translation:** 

**[13008.08s] English:** risk averse is that why can you speak to that really eye-opening to me working inside a tech  
**Translation:** Vocabulary: averse: 规避风险

**[13014.68s] English:** titan where i am you know i i had  
**Translation:** 

**[13018.24s] English:** my  
**Translation:** Vocabulary: titan: 巨无霸

**[13018.30s] English:** small companies and then we're acquired by a you know a mid-sized game publisher  
**Translation:** 

**[13022.84s] English:** and then uh oculus getting acquired by meta and meta has grown by a factor of many just in the  
**Translation:** Vocabulary: oculus: Oculus头显

**[13029.48s] English:** the eight years since the acquisition so i did not have experience with this and it's  
**Translation:** 

**[13036.98s] English:** it was interesting because i remember like previously my benchmark for uh kind of use of  
**Translation:** Vocabulary: benchmark: 衡量标准

**[13042.34s] English:** resources was some of the government programs i interacted with on the aerospace side  
**Translation:** 

**[13046.40s] English:** and i remember thinking  
**Translation:** Vocabulary: aerospace: 航空航天; interacted: 互动

**[13048.24s] English:** there was okay there's an air force program and they spent 50 million dollars and they didn't  
**Translation:** 

**[13053.18s] English:** they didn't launch anything they didn't even build anything it was just kind of like they i  
**Translation:** 

**[13056.94s] English:** you know they made a bunch of papers and had some parts in uh in a warehouse and nothing came of it  
**Translation:** 

**[13062.14s] English:** it's like 50 million dollars i am and i have i've had to radically recalibrate my sense of  
**Translation:** Vocabulary: radically: 根本上; recalibrate: 重新校准

**[13068.74s] English:** like how much money can be spent with i without a product resources where on the plus side vr has  
**Translation:** 

**[13077.28s] English:** turned out we've been able to do a lot of things and we've been able to do a lot of things and we've  
**Translation:** 

**[13078.24s] English:** been able to do a lot of things and we've built pretty much  
**Translation:** 

**[13080.00s] English:** exactly what you know we just passed the 10-year mark then from my i like my first demo of the rift  
**Translation:** 

**[13086.52s] English:** and if i could have said what i wanted to have it would have been a standalone inside out tracked  
**Translation:** 

**[13092.48s] English:** 4k resolution headset that i that could still plug into a pc for high-end rendering and that's  
**Translation:** Vocabulary: headset: 耳机; standalone: 独立使用

**[13098.78s] English:** exactly what we've got on quest 2 right now first of all let's pause on that with me being cranky  
**Translation:** 

**[13104.10s] English:** and everything it's what meta achieved uh with oculus and so on is incredible i mean this is  
**Translation:** Vocabulary: cranky: 脾气坏的

**[13110.88s] English:** this what when i thought about the future of vr this is what i imagined in terms of hardware i  
**Translation:** 

**[13115.86s] English:** would say and maybe in terms of the experience as well but it's still not there somehow on the  
**Translation:** 

**[13122.32s] English:** one hand we did kind of achieve it and win and we've got we've sold you know we're a success  
**Translation:** 

**[13127.00s] English:** right now but the amount of resources that have gone into it it winds up getting clotted up in  
**Translation:** 

**[13132.96s] English:** accounting where last  
**Translation:** 

**[13134.04s] English:** last  
**Translation:** 

**[13134.08s] English:** last  
**Translation:** 

**[13134.10s] English:** Mark did announce that they spent $10 billion a year, like on Reality Labs.  
**Translation:** 

**[13139.54s] English:** Now, Reality Labs covers a lot.  
**Translation:** 

**[13141.86s] English:** It was, VR was not the large part of it.  
**Translation:** 

**[13144.34s] English:** It also had Portal and Spark and the big AR research efforts.  
**Translation:** 

**[13148.28s] English:** And it's been expanding out to include AI and other things there, where there's a lot  
**Translation:** 

**[13154.28s] English:** going on there.  
**Translation:** 

**[13155.60s] English:** But $10 billion was just a number that I had trouble processing.  
**Translation:** 

**[13160.12s] English:** I feel sick to my stomach thinking about that much money being spent.  
**Translation:** 

**[13165.02s] English:** But that's how they demonstrate commitment to this, where it's not more so than like,  
**Translation:** 

**[13171.28s] English:** yeah, Google goes and cancels all of these projects, different things like that, while  
**Translation:** 

**[13176.28s] English:** Meta is really sticking with the funding of VR and AR is still further out with it.  
**Translation:** Vocabulary: sticking: 坚持

**[13181.92s] English:** So there's something to be said for that.  
**Translation:** 

**[13184.46s] English:** It's not just going to vanish, the work's going in.  
**Translation:** 

**[13186.86s] English:** I just wish it could be, all those resources could be applied.  
**Translation:** 

**[13190.12s] English:** More effectively, because I see all these cases.  
**Translation:** 

**[13193.82s] English:** I point out these examples of how a third party that we're kind of competing with in  
**Translation:** 

**[13198.16s] English:** various ways.  
**Translation:** 

**[13198.94s] English:** There's a number of these examples.  
**Translation:** 

**[13200.00s] English:** And they do work with a tenth of the people that we do internally. And a lot of it comes from, yes, the small company can just go do it, while in a big company, you do have to worry about, is there some SDK internally that you should be using because another team is making it? You have to have your cross-functional group meetups for different things.  
**Translation:** Vocabulary: internally: 内部地

**[13221.86s] English:** You do have more concerns about privacy or diversity and equity and safety of different things, parental issues, and things that a small startup company can just kind of cowboy off and do something interesting.  
**Translation:** 

**[13236.64s] English:** And there's a lot more that is a problem that you have to pay attention to in the big companies, but I'm not willing to believe that we are within even a factor of two or four of what the efficiency could be.  
**Translation:** Vocabulary: cowboy: 粗放经营

**[13247.92s] English:** I am constantly kind of crying out for it.  
**Translation:** 

**[13251.88s] English:** It's like, we can do better than this.  
**Translation:** 

**[13253.52s] English:** Yeah, and you wonder what the mechanisms to unlock that efficiency are.  
**Translation:** 

**[13257.92s] English:** You know, I don't, there is some sense in a large company that, like, an individual engineer might not believe that they can change the world.  
**Translation:** 

**[13267.16s] English:** Maybe you delegate a little bit of the responsibility to be the one who changes the world in a big company.  
**Translation:** 

**[13274.06s] English:** I think, but the reality is, like, the world will get changed by a single engineer anyway.  
**Translation:** Vocabulary: delegate: 授权

**[13280.72s] English:** So if, whether inside Google or inside a startup, it doesn't matter, it's just, like, Google and Meta needs to help those engineers believe they're the ones that are going to decrease that latency, is it'll take one John Carmack, like, the 20-year-old Carmack that's inside Meta right now to change everything.  
**Translation:** 

**[13300.22s] English:** And I try to point that out and push people.  
**Translation:** Vocabulary: latency: 延迟

**[13303.16s] English:** It's like, try to go ahead, and when you see something, because there is, you get the silo mentality where you're like, okay, I know something's not right over there.  
**Translation:** 

**[13310.70s] English:** But that's, I'm staying in my lane here.  
**Translation:** 

**[13313.50s] English:** And there's a couple people that I can, you know, I can think about that are willing to just, like, hop all over the place.  
**Translation:** 

**[13319.64s] English:** Man, I.  
**Translation:** 

**[13320.00s] English:** I treasure them, the people that are just willing to, they're fearless, you know, they will go over  
**Translation:** 

**[13324.72s] English:** and they will go rebuild the kernel and change this distribution and go in and hack the firmware  
**Translation:** Vocabulary: fearless: 无所畏惧; firmware: 固件; kernel: 内核

**[13329.26s] English:** over here to get something done right. And that is relatively rare. You know, there's thousands  
**Translation:** 

**[13334.86s] English:** of developers, and you've got a small handful that are willing to operate at that level. And,  
**Translation:** 

**[13340.10s] English:** you know, and it's potentially risky for them. The politics are, you know, are real in a lot of  
**Translation:** 

**[13344.76s] English:** that. And I'm in the, you know, very much the privileged position of, I am, you know, I'm more  
**Translation:** Vocabulary: privileged: 受优待的

**[13349.92s] English:** or less untouchable there where I've been dinged, like twice for it's like you said something  
**Translation:** 

**[13354.26s] English:** insensitive in that post. And I, and you should probably not say that. But for the most part,  
**Translation:** Vocabulary: dinged: 扣分; insensitive: 冒犯

**[13359.90s] English:** yes, I, you know, I get away with, I, every week, I'm posting something, you know, pretty loud and  
**Translation:** 

**[13365.14s] English:** opinionated in, you know, internally. And I think that's useful for the company. But I'm, yeah,  
**Translation:** Vocabulary: internally: 内部地

**[13372.02s] English:** it's not, it's rare to have a position like that.  
**Translation:** 

**[13374.76s] English:** And I can't necessarily offer advice for how someone can do that. I've...  
**Translation:** 

**[13379.10s] English:** Well, you could offer advice to a company in general to give a little bit of freedom  
**Translation:** 

**[13383.74s] English:** for the young, wild, like the wildest ideas come from the young minds. And so you need to give the  
**Translation:** 

**[13392.00s] English:** young minds freedom to think big and wild and crazy. And for that, they have to be opinionated.  
**Translation:** 

**[13398.14s] English:** They have to be, they have to think crazy ideas and thoughts and,  
**Translation:** 

**[13404.76s] English:** you know, sue them with a full passion without being slowed down by bureaucracy or managers and  
**Translation:** 

**[13409.30s] English:** all that kind of stuff. Obviously, startups really empower that, but big companies could too. And  
**Translation:** Vocabulary: bureaucracy: 官僚主义; empower: 授权; startups: 初创公司

**[13414.36s] English:** that's, that's a design challenge for company, for big companies to see how can you enable that?  
**Translation:** 

**[13420.24s] English:** How can you empower that?  
**Translation:** 

**[13420.98s] English:** Because the big company, there are so many resources there. And they do, you know,  
**Translation:** 

**[13424.82s] English:** amazing things do get accomplished, but there's so much more that could come out of that. And,  
**Translation:** 

**[13430.18s] English:** you know, I'm hope, I'm always hopeful. I'm an optimist in almost everything. You know,  
**Translation:** 

**[13433.20s] English:** I think things can get better. And I think things can get better. And I think things can get better.  
**Translation:** Vocabulary: optimist: 积极乐观的人

**[13434.74s] English:** I think that they can improve things that you go through a path and you're learning kind of what  
**Translation:** 

**[13440.00s] English:** does and doesn't work. And I'm not, I'm not ready to be fatalistic about the kind of the outcome of  
**Translation:** 

**[13445.36s] English:** any of that. Me neither. I know too many good people inside of those large companies that are  
**Translation:** 

**[13450.80s] English:** incredible. You have a friendship with Elon Musk. Often when I talk to him, he'll bring up how  
**Translation:** 

**[13458.18s] English:** incredible of an engineer and just a big picture thinker you are. He has a huge amount of respect  
**Translation:** 

**[13464.10s] English:** for you. I just, I've never been a fly on the wall between the discussion between the two of  
**Translation:** 

**[13470.34s] English:** you. I just wonder, is there something you guys debate, argue about, discuss? Is there some  
**Translation:** 

**[13477.28s] English:** interesting problems that the two of you think about? You come from different worlds. Maybe  
**Translation:** 

**[13482.62s] English:** there's some intersection in aerospace. Maybe there's some intersection in your new efforts  
**Translation:** 

**[13490.14s] English:** in artificial intelligence in terms of thinking. Is there something,  
**Translation:** Vocabulary: aerospace: 航空航天; intersection: 交集

**[13494.10s] English:** interesting you could say about sort of the debates the two of you have?  
**Translation:** 

**[13497.40s] English:** So I think in some ways we do have a kind of similar background where we're almost exactly  
**Translation:** 

**[13502.46s] English:** the same age and we had kind of similar programming backgrounds on the personal computers and,  
**Translation:** 

**[13508.04s] English:** you know, even some of the books that we would read and things that would  
**Translation:** 

**[13511.44s] English:** kind of turn us into the people that we are today. And I think there is a degree of  
**Translation:** 

**[13517.24s] English:** sensibility similarities where, you know, we kind of call bullshit on the same things and kind of  
**Translation:** Vocabulary: bullshit: 胡说八道; sensibility: 理性认知

**[13523.24s] English:** see the same.  
**Translation:** 

**[13524.10s] English:** I think there's opportunities in different technology and there's that sense of, you know,  
**Translation:** 

**[13528.96s] English:** I always talk about the speed of light solutions for things and he's thinking about kind of minimum  
**Translation:** 

**[13533.92s] English:** manufacturing and engineering and operational standpoints for things. And so, I mean, I first  
**Translation:** Vocabulary: standpoints: 立场

**[13541.00s] English:** met Elon right at the start of the aerospace era where I wasn't familiar with, you know,  
**Translation:** 

**[13546.16s] English:** I was still in my game dev bubble. I really wasn't familiar with all the startups that were going and  
**Translation:** Vocabulary: startups: 初创公司

**[13550.74s] English:** being successful and what went on with PayPal and all of his,  
**Translation:** 

**[13554.10s] English:** different companies. But, you know, I met him as I was starting to do Armadillo Aerospace and,  
**Translation:** Vocabulary: armadillo: 犰狳

**[13559.36s] English:** you know, he  
**Translation:** 

**[13560.00s] English:** came down with kind of his right hand propulsion guy and we we talked about rockets you know what  
**Translation:** Vocabulary: propulsion: 推进

**[13565.56s] English:** can we what can we do with this and it was kind of specific things about like how are how are our  
**Translation:** 

**[13570.84s] English:** flight computers set up what are different propellant options i am you know what can happen  
**Translation:** Vocabulary: propellant: 推进剂

**[13575.58s] English:** with different i have different ways of putting things together and then in some ways he was  
**Translation:** 

**[13581.46s] English:** certainly the biggest player in the sort of alt space community that was going on in the early  
**Translation:** 

**[13586.42s] English:** 2000s he was the most well funded although you know his funding in the larger scheme of things  
**Translation:** 

**[13592.82s] English:** compared to a like a nasa or something like that was really tiny uh it was a lot more than i had at  
**Translation:** 

**[13599.74s] English:** the time i but it was interesting i had a point years later when i realized okay my like my  
**Translation:** 

**[13607.08s] English:** financial resources at this point are basically what elon's was when he went all in on spacex and  
**Translation:** 

**[13613.26s] English:** tesla and there's  
**Translation:** 

**[13616.42s] English:** i i think in many corners he does not get uh the respect that he should about being a wealthy  
**Translation:** 

**[13622.52s] English:** person that could just retire and he went all in where he was really going to i you know it he  
**Translation:** 

**[13630.42s] English:** could have gone bust and there's plenty of people you look at the you know the sad i am athletes or  
**Translation:** 

**[13635.70s] English:** or entertainers that had all the money in the world and blew it he could have been the the  
**Translation:** 

**[13639.48s] English:** business case example of that but i you know the the things that he was doing space exploration  
**Translation:** Vocabulary: entertainers: 表演者

**[13646.42s] English:** electrification of transportation on solar city type things these are big world level things and  
**Translation:** 

**[13654.96s] English:** i have a great deal of admiration that he was willing to throw himself so completely into that  
**Translation:** Vocabulary: electrification: 电气化

**[13660.66s] English:** because in contrast with myself i was doing armadillo aerospace with this tightly bounded uh  
**Translation:** 

**[13666.96s] English:** it was john's crazy money uh at the time that had a finite limit on it it was never going to impact  
**Translation:** Vocabulary: aerospace: 航天; finite: 有限

**[13673.00s] English:** me or my family uh if it completely failed  
**Translation:** 

**[13676.42s] English:** and i was still hedging my bets working at id software  
**Translation:** 

**[13680.00s] English:** at the time when he had been, you know, really all in there. And I have a huge amount of respect  
**Translation:** 

**[13687.12s] English:** for that. And people do not, the other thing I get irritated with is people would say, it's like,  
**Translation:** Vocabulary: irritated: 烦躁

**[13691.78s] English:** oh, Elon's just a business guy. You know, he just got like, he was gifted the money and he's just  
**Translation:** 

**[13697.16s] English:** kind of investing in all of this when he was really deeply involved in a lot of the decisions.  
**Translation:** 

**[13703.46s] English:** You know, not all of them were perfect, but I, you know, he cared very much about engine material  
**Translation:** 

**[13709.60s] English:** selection, propellant selection. And I, you know, for years he'd be kind of telling me, it's like,  
**Translation:** Vocabulary: propellant: 推进剂

**[13714.84s] English:** get off that hydrogen peroxide stuff. It's like, you know, liquid oxygen is the, you know,  
**Translation:** 

**[13719.12s] English:** is the only proper oxidizer for this. And I, you know, unlike the times that I've gone through the  
**Translation:** 

**[13725.58s] English:** factories with him, we're talking very detailed things about like how this weld is made, you know,  
**Translation:** 

**[13731.80s] English:** how this sub-assembly goes together.  
**Translation:** 

**[13733.46s] English:** I, you know, what are like startup shutdown behaviors of the different things. So he is,  
**Translation:** 

**[13739.78s] English:** you know, really in there at a very detailed level. And I think that he is the best modern  
**Translation:** Vocabulary: shutdown: 关闭

**[13746.00s] English:** example now of someone that tries to, that can effectively micromanage some decisions on things  
**Translation:** 

**[13751.78s] English:** on both Tesla, you know, and SpaceX to some degree where he cares enough about it. I worry a lot that  
**Translation:** Vocabulary: micromanage: 细琐管理

**[13758.00s] English:** he's stretched too thin, that you get boring company and Neuralink and Twitter and all the  
**Translation:** 

**[13763.40s] English:** other things. And I, you know, I think that he's the best modern example now of someone that can  
**Translation:** 

**[13763.44s] English:** other possible things there where I know I've got, I've got limits on how much I can pay attention to  
**Translation:** 

**[13770.32s] English:** that. I have to kind of box off different amounts of time. And I look back at like at my aerospace  
**Translation:** 

**[13775.62s] English:** side of things. It's like, I did not go all in on that. I did not commit myself at a level that it  
**Translation:** 

**[13780.84s] English:** would have taken to be successful there. And I, yeah, and it's kind of a weird thing, just like  
**Translation:** 

**[13787.16s] English:** having a discussion with him. He's the richest man in the world right now, but he, I, you know,  
**Translation:** 

**[13792.20s] English:** he operates on, you know, he's the richest man in the world right now. And I, you know, he's the  
**Translation:** 

**[13793.38s] English:** on a level that is still very much in my wheelhouse on a technical side of things.  
**Translation:** 

**[13800.00s] English:** Yeah, doing that systems-level type of thinking where you can go to the low-level details and go up high to the big picture.  
**Translation:** Vocabulary: wheelhouse: 擅长领域

**[13807.42s] English:** Do you think in the aerospace arena in the next five, ten years, do you think we're going to put a human on Mars?  
**Translation:** 

**[13816.40s] English:** What do you think is the interesting point?  
**Translation:** Vocabulary: aerospace: 航空航天

**[13820.18s] English:** No, in fact, I made a bet with someone, with a group of people, kind of this, about whether boots on Mars by 2030.  
**Translation:** 

**[13827.56s] English:** And this was kind of a fun story because I was at an Intel-sponsored event, and we had a bunch of just world-class, brilliant people.  
**Translation:** 

**[13837.50s] English:** And we were talking about computing stuff, but the after-dinner conversation was, like, what are some other things?  
**Translation:** 

**[13842.30s] English:** How are they going to go in the future?  
**Translation:** 

**[13843.90s] English:** And one of the ones tossed up on the whiteboard was, like, boots on Mars by 2030.  
**Translation:** 

**[13848.86s] English:** And most of the people in the room thought, yes.  
**Translation:** 

**[13852.06s] English:** They thought that, like, SpaceX is kicking ass.  
**Translation:** 

**[13854.46s] English:** We've got all this possible stuff.  
**Translation:** 

**[13856.20s] English:** It seems like...  
**Translation:** 

**[13857.78s] English:** And I said, no, I think less than 50% chance that it's going to make it there.  
**Translation:** 

**[13865.54s] English:** And people were kind of like, oh, why the pessimism or whatever?  
**Translation:** 

**[13869.44s] English:** And, of course, I'm an optimist at almost everything.  
**Translation:** Vocabulary: optimist: 乐观主义者; pessimism: 悲观主义

**[13872.08s] English:** But for me to be the one kind of outlier saying, no, I don't think so, then I started saying some of the things.  
**Translation:** 

**[13879.14s] English:** I said, well, let's be concrete about it.  
**Translation:** 

**[13881.10s] English:** Let's bet $10,000 that it's not going to happen.  
**Translation:** 

**[13884.18s] English:** And this was really...  
**Translation:** 

**[13887.56s] English:** It was a startling thing to see that, again, a room full of brilliant people.  
**Translation:** 

**[13891.82s] English:** But as soon as, like, money came on the line and they were like, do I want to put $10,000...  
**Translation:** Vocabulary: startling: 令人惊讶的

**[13896.40s] English:** And I was not the richest person in the room.  
**Translation:** 

**[13898.76s] English:** There were people much better off than I was.  
**Translation:** 

**[13901.28s] English:** There was a spectrum.  
**Translation:** 

**[13902.34s] English:** But, you know, as soon as they started thinking, it's like, oh, I could lose money by keeping my position right now.  
**Translation:** 

**[13910.76s] English:** And all these engineers, they engaged their brain.  
**Translation:** 

**[13913.30s] English:** And they started thinking, it's like, okay, launch windows, launch delays.  
**Translation:** 

**[13917.56s] English:** Like, how many times would it take to get this...  
**Translation:** 

**[13920.00s] English:** right? What historical precedents do we have? And then it mostly came down to, it's like,  
**Translation:** Vocabulary: precedents: 先例

**[13925.54s] English:** well, what about in transit by 2030? And then what about different things, or would you go for  
**Translation:** 

**[13932.50s] English:** 2032? But one of the people did go ahead and was optimistic enough to make a bet with me. So I have  
**Translation:** Vocabulary: optimistic: 乐观

**[13938.92s] English:** a $10,000 bet that by 2030, I think it's going to happen shortly thereafter. I think there will  
**Translation:** 

**[13944.88s] English:** probably be infrastructure on Mars by 2030, but I don't think that we'll have humans on Mars on  
**Translation:** Vocabulary: thereafter: 之后

**[13950.66s] English:** 2030. I think it's possible, but I think it's less than a 50% chance. So I felt safe making that bet.  
**Translation:** 

**[13956.92s] English:** Well, I think you had an interesting point. Correct me if I'm wrong. That's a dark one.  
**Translation:** 

**[13962.56s] English:** That should perhaps help people appreciate Elon Musk, which is,  
**Translation:** 

**[13970.62s] English:** in this particular effort, Elon is a critical  
**Translation:** 

**[13974.44s] English:** person.  
**Translation:** 

**[13974.88s] English:** It's critical to the success. SpaceX seems to be critical to humans on Mars by 2030 or  
**Translation:** 

**[13985.48s] English:** thereabouts. So if something happens to Elon, then all of this collapses.  
**Translation:** 

**[13993.72s] English:** And this is in contrast to the other $10,000 bet I made kind of recently, and that was  
**Translation:** Vocabulary: collapses: 崩溃; thereabouts: 大约

**[13999.18s] English:** self-driving cars at like a level five running around cities. And people have kind of  
**Translation:** 

**[14004.44s] English:** nitpicked that, that we probably don't mean exactly level five, but the guy I'm having the  
**Translation:** Vocabulary: nitpicked: 吹毛求疵

**[14008.60s] English:** bet with is we're going to be, we know what we mean about this.  
**Translation:** 

**[14013.16s] English:** Jeff Atwood.  
**Translation:** Vocabulary: atwood: 阿特伍德

**[14013.84s] English:** Yeah. Coding horror and stack overflow and all. But yeah, I mean, it's just, he doesn't think  
**Translation:** 

**[14020.10s] English:** that people are going to be riding around in robo taxis in 2030 in major cities, just like you take  
**Translation:** Vocabulary: overflow: 溢出

**[14026.44s] English:** an Uber now. And I think it will.  
**Translation:** 

**[14028.60s] English:** You think it will.  
**Translation:** 

**[14029.20s] English:** And the difference is everybody looks at this, it's like, oh, but Tesla has been wrong for you.  
**Translation:** 

**[14033.58s] English:** They've been promising it.  
**Translation:** 

**[14034.44s] English:** For years. And it's not here yet. And the reason this is different than the bet with Mars.  
**Translation:** 

**[14040.00s] English:** is mars really is more than is comfortable a bet on elon musk i am you know that is you know that  
**Translation:** 

**[14048.24s] English:** is his thing and he is really going to move heaven and earth to try to make that happen  
**Translation:** 

**[14053.46s] English:** perhaps not even spacex yeah perhaps just elon musk yeah because if if elon went away and spacex  
**Translation:** 

**[14061.06s] English:** went public and got a board of directors i there are more profitable things they could be doing  
**Translation:** 

**[14066.32s] English:** than focusing on human presence on mars so this really is a sort of personal thing there  
**Translation:** Vocabulary: profitable: 有利可图的

**[14072.16s] English:** and in contrast with that self-driving cars have a dozen credible companies working really hard  
**Translation:** 

**[14080.14s] English:** and while yes it's going slower than most people thought it would betting against that is a bet  
**Translation:** 

**[14087.02s] English:** against almost the entire world in terms of all of these companies that have all of these incentives  
**Translation:** 

**[14092.58s] English:** it's not just you know one guy's passion project  
**Translation:** Vocabulary: incentives: 激励措施

**[14096.32s] English:** i and i do think that it is solvable i although there's i recognize it's not a hundred percent  
**Translation:** 

**[14102.08s] English:** chance because it's possible the long tail of self-driving problems winds up being an agi  
**Translation:** Vocabulary: solvable: 可解决的

**[14107.02s] English:** complete problem i think there's plenty of value to mine out of it with narrow ai and i think that  
**Translation:** 

**[14112.50s] English:** it's you know it's going to happen probably more so than people expect but it's that whole sigmoid  
**Translation:** Vocabulary: sigmoid: S形曲线

**[14117.92s] English:** curve where you over you know you overestimate the near-term progress and you underestimate the  
**Translation:** 

**[14122.62s] English:** long-term progress and i think self-driving is going to be like that  
**Translation:** Vocabulary: overestimate: 高估; underestimate: 低估

**[14126.32s] English:** and i think 2030 is still a pretty good bet yeah unfortunately um self-driving is a problem that  
**Translation:** 

**[14135.56s] English:** is safety critical meaning that if if you don't do it well people get hurt but the other side of that  
**Translation:** 

**[14144.42s] English:** is people are terrible drivers so it was it is not going to be that's probably going to be the  
**Translation:** 

**[14149.10s] English:** argument that gets it through is like we can save 10 000 lives a year by taking imperfect self-driving  
**Translation:** 

**[14156.32s] English:** cars and letting them take over a lot of driving responsibilities  
**Translation:** 

**[14160.00s] English:** like, was it 30,000 people a year die in auto accidents right now in America? And a lot of  
**Translation:** 

**[14165.70s] English:** those are preventable. And the problem is you'll have people that every time a Tesla crashes into  
**Translation:** 

**[14170.58s] English:** something, you've got a bunch of people that literally have vested interests shorting Tesla  
**Translation:** Vocabulary: vested: 有利益关系的

**[14174.80s] English:** to come out and make it the worst thing in the world. And people will be fighting against that.  
**Translation:** 

**[14179.52s] English:** But optimist in me again, I think that we will have systems that are statistically safer than  
**Translation:** Vocabulary: optimist: 乐观主义者

**[14185.16s] English:** human drivers. And we will be saving thousands and thousands of lives every year when we can  
**Translation:** 

**[14191.38s] English:** hand over more of those responsibilities to it. I do still think as a person who studied this  
**Translation:** 

**[14196.74s] English:** problem very deeply from a human side as well, it's still an open problem how good slash bad  
**Translation:** 

**[14204.26s] English:** humans are driving. It's a kind of funny thing we say about each other. Oh, humans suck at driving.  
**Translation:** 

**[14212.22s] English:** Everybody except you, of course.  
**Translation:** 

**[14215.16s] English:** We think we're good at driving. But after really studying it, I think you start to notice,  
**Translation:** 

**[14223.10s] English:** because I watched hundreds of hours of humans driving, the projects of this kind of thing,  
**Translation:** 

**[14228.70s] English:** you've noticed that even with the distraction, even with everything else,  
**Translation:** Vocabulary: distraction: 分心事物

**[14233.56s] English:** humans are able to do some incredible things with the attention. Even when you're just  
**Translation:** 

**[14240.10s] English:** looking at the smartphone, just to get cues from the environment, to make less seconds,  
**Translation:** 

**[14245.16s] English:** decisions, to use instinctual type of decisions that actually save your ass time and time and time  
**Translation:** 

**[14251.94s] English:** again, and are able to do that with so much uncertainty around you in such tricky dynamic  
**Translation:** Vocabulary: instinctual: 直觉性的

**[14259.60s] English:** environments. I don't know. I don't know exactly how hard is it to beat that kind of skill of  
**Translation:** 

**[14269.64s] English:** common sense reasoning. This is one of those interesting things that there have been a lot  
**Translation:** 

**[14273.36s] English:** of studies about how...  
**Translation:** 

**[14275.16s] English:** Experts in their field usually underestimate the progress that's going to happen because  
**Translation:** Vocabulary: underestimate: 低估

**[14280.00s] English:** an expert thinks about all the problems they deal with. And they're like, damn, I'm going to have a  
**Translation:** 

**[14284.68s] English:** hard time solving all of this. And they filter out the fact that they are one expert in a field  
**Translation:** 

**[14289.32s] English:** of thousands. And you think about, yeah, I can't do all of that. And you sometimes forget about  
**Translation:** 

**[14294.78s] English:** the scope of the ecosystem that you're embedded in. And if you think back eight years, very  
**Translation:** Vocabulary: embedded: 嵌入其中

**[14299.92s] English:** specifically the state of AI and machine learning, where we had just gotten ResNets probably at that  
**Translation:** 

**[14306.28s] English:** point. And you look at all the amazing, magical things that have happened in eight years.  
**Translation:** 

**[14311.56s] English:** And they do kind of seem to be happening a little faster in recent years also. And you project that  
**Translation:** 

**[14316.88s] English:** eight more years into the future, where again, I think there's a 50% chance we're going to have  
**Translation:** 

**[14321.62s] English:** signs of life of AGI, which we can put through driver's ed if we need to, to actually build  
**Translation:** 

**[14327.22s] English:** self-driving cars. And I think that the narrow systems are going to have real value demonstrated  
**Translation:** 

**[14333.06s] English:** well before then.  
**Translation:** 

**[14335.06s] English:** So signs of life.  
**Translation:** 

**[14336.28s] English:** In AGI, you've mentioned that, okay, first of all, you're one of the most brilliant people  
**Translation:** 

**[14344.22s] English:** on this earth. You could be solving a number of different problems, as you've mentioned.  
**Translation:** 

**[14349.26s] English:** Your mind was attracted to nuclear energy. Obviously, virtual reality with the metaverse  
**Translation:** 

**[14354.54s] English:** is something you could have a tremendous impact on.  
**Translation:** Vocabulary: metaverse: 元宇宙

**[14356.74s] English:** I do want to say a quick thing about nuclear energy, where this is something that  
**Translation:** 

**[14361.94s] English:** this so precisely feels like aerospace.  
**Translation:** 

**[14366.28s] English:** SpaceX, where from everything that I know about all of these, the physics of this stuff hasn't  
**Translation:** 

**[14372.62s] English:** changed. And the reasons why things are expensive now are not fundamental. Somebody should be going  
**Translation:** 

**[14380.58s] English:** into a really hard Elon Musk style at vision, economical vision, not fusion, where the fusion  
**Translation:** 

**[14390.16s] English:** is the kind of the darling of people that want to go and do nuclear because it doesn't have the  
**Translation:** Vocabulary: economical: 经济的

**[14395.86s] English:** taint.  
**Translation:** 

**[14396.28s] English:** That vision has in a lot of people's minds, but it's an almost  
**Translation:** Vocabulary: taint: 污染

**[14400.00s] English:** most absurdly complex thing where nuclear fusion, as you look at the tokamaks or any of the things  
**Translation:** 

**[14406.58s] English:** that people are building, and it's doing all of this infrastructure just at the end of the day  
**Translation:** Vocabulary: absurdly: 荒谬地; tokamaks: 托卡马克

**[14411.12s] English:** to make something hot, so that you can then turn into energy through a conventional power plant.  
**Translation:** 

**[14417.06s] English:** And all of that work, which we think we've got line of sight on, but even if it comes out,  
**Translation:** 

**[14422.02s] English:** then you have to do all of that immensely complex, expensive stuff just to make something hot,  
**Translation:** 

**[14427.26s] English:** where nuclear fission is basically you put these two rocks together, and they get hot all by  
**Translation:** Vocabulary: fission: 裂变; immensely: 极其

**[14432.14s] English:** themselves. That is just that much simpler. It's just orders of magnitude simpler. And the actual  
**Translation:** 

**[14438.94s] English:** rocks, the refined uranium, is not very expensive. It's a couple percent of the cost of electricity.  
**Translation:** Vocabulary: refined: 精炼; uranium: 铀

**[14445.22s] English:** That's why I made that point where you could have something which was five times less efficient  
**Translation:** 

**[14450.28s] English:** than current systems, and if the rest of the plant was a whole bunch cheaper, you could still be  
**Translation:** 

**[14455.38s] English:** super, super valuable.  
**Translation:** 

**[14457.26s] English:** So how much of the pie do you think could be solved by nuclear energy, by fission?  
**Translation:** 

**[14464.40s] English:** So how much could it become the primary source of energy on Earth?  
**Translation:** 

**[14468.82s] English:** It could be most of it. The reserves of uranium, as it stands now, could not power the whole Earth,  
**Translation:** 

**[14473.74s] English:** but you get into breeder reactors and thorium and things like that that you do for conventional  
**Translation:** 

**[14478.60s] English:** fission. There is enough for everything. Now, I mean, solar, photovoltaic has been amazing.  
**Translation:** Vocabulary: photovoltaic: 光伏; thorium: 钍

**[14485.10s] English:** You know, it's, I, I,  
**Translation:** 

**[14487.06s] English:** one of the things that I've been doing is I've been doing a lot of research on,  
**Translation:** 

**[14487.24s] English:** one of the things that I've been doing is I've been doing a lot of research on,  
**Translation:** 

**[14487.26s] English:** one of my current projects is working on an off-grid system, and it's been fun just kind  
**Translation:** 

**[14490.98s] English:** of, again, putting my hands on all the, stripping the wires and wiring things together and doing  
**Translation:** 

**[14495.26s] English:** all of that. And just having followed that a little bit from the outside over the last  
**Translation:** Vocabulary: stripping: 去皮

**[14499.60s] English:** couple decades, there's been semiconductor-like magical progress in what's going on there.  
**Translation:** 

**[14505.98s] English:** So I'm all for all of that, but it doesn't solve everything, and nuclear really still does seem  
**Translation:** 

**[14512.04s] English:** like the smart money bet for what you should be getting for baseband on a lot of things.  
**Translation:** 

**[14516.52s] English:** And solar may be cheaper for, you know, peaking over  
**Translation:** Vocabulary: baseband: 基带

**[14520.00s] English:** air conditioning loads during the summer and things that you can push around in different ways  
**Translation:** 

**[14524.80s] English:** but it's one of those things that's it's just strange how we've had the technology sitting  
**Translation:** 

**[14530.62s] English:** there but these non-technical reasons on the social optics of it has been this major forcing  
**Translation:** 

**[14536.56s] English:** function for something that you know really should be at the the cornerstone of all of the world's  
**Translation:** Vocabulary: cornerstone: 基石; optics: 公众看法

**[14542.48s] English:** concerns with energy it's interesting how the non-technical factors have really dominated  
**Translation:** 

**[14548.38s] English:** something that is so fundamental to kind of the existence of the human race as we know it today  
**Translation:** 

**[14553.80s] English:** and much of the troubles of the world including wars in different parts of the world like ukraine  
**Translation:** 

**[14560.46s] English:** is energy-based and uh yeah it's just sitting right there to be solved  
**Translation:** 

**[14565.26s] English:** that said uh i mean to me personally i think it's clear that if agi were to be achieved that  
**Translation:** 

**[14574.08s] English:** would change the course of human history so agi wise i was  
**Translation:** 

**[14577.98s] English:** you know i was i was i was i was i was i was i was i was i was i was i was i was  
**Translation:** 

**[14578.38s] English:** you know i was making this decision about what do i want to focus on after vr and i'm still working  
**Translation:** 

**[14584.48s] English:** on vr regularly i spend a day a week i kind of consulting with meta and i you know boz  
**Translation:** 

**[14590.80s] English:** styles me the consulting cto is kind of like the sherlock holmes that comes in and  
**Translation:** Vocabulary: consulting: 咨询; sherlock: 福尔摩斯

**[14596.02s] English:** consults on some of the specific tough issues and i'm still pretty passionate about all of that  
**Translation:** 

**[14601.40s] English:** but i have been figuring out how to compartmentalize and force that into a smaller box to  
**Translation:** Vocabulary: compartmentalize: 划分区间; consults: 提供咨询

**[14608.38s] English:** other things and i did come down to this decision between working on economical nuclear fission or  
**Translation:** 

**[14614.78s] English:** artificial general intelligence and uh the fission side of things i've i've got a bunch of interesting  
**Translation:** Vocabulary: economical: 经济的

**[14620.62s] English:** things going that way but it would take that would be a fairly big project thing to do i don't think  
**Translation:** 

**[14627.04s] English:** it needs to be as big as people expect i do think something original spacex sized i you build it  
**Translation:** 

**[14633.62s] English:** power you're building off of it and then the government i think will come around to what you  
**Translation:** 

**[14637.98s] English:** need to is everybody  
**Translation:** 

**[14640.00s] English:** loves an existence proof i think it's possible somebody should be doing this but it's going to  
**Translation:** 

**[14644.70s] English:** involve some politics it's going to involve decent sized teams and a bunch of this cross-functional  
**Translation:** 

**[14649.56s] English:** stuff that i don't love while the artificial general intelligence side of things um it seems  
**Translation:** 

**[14657.16s] English:** to me like this is the highest leverage moment for potentially a single individual potentially  
**Translation:** Vocabulary: leverage: 影响力

**[14665.04s] English:** in the history of the world where the things that we know about the brain about what we can  
**Translation:** 

**[14670.90s] English:** do with artificial intelligence uh nobody can say absolutely on any of these things but i am not a  
**Translation:** 

**[14677.76s] English:** madman for saying that it is likely that the code for artificial general intelligence is going to be  
**Translation:** 

**[14685.22s] English:** tens of thousands of lines of code not millions of lines of code this is code that conceivably  
**Translation:** Vocabulary: conceivably: 想象中; madman: 疯子

**[14691.56s] English:** one individual could write unlike writing a new web  
**Translation:** 

**[14694.88s] English:** browser  
**Translation:** 

**[14695.04s] English:** operating system and based on the progress that ai has machine learning has made in the recent  
**Translation:** 

**[14702.56s] English:** decade it's likely that the important things that we don't know are relatively simple there's  
**Translation:** 

**[14708.92s] English:** probably a handful of things and my bet is that i think there's less than six key insights that  
**Translation:** 

**[14716.76s] English:** need to be made each one of them can probably be written on the back of an envelope we don't know  
**Translation:** 

**[14721.38s] English:** what they are but when they're put together in concert with gpu  
**Translation:** 

**[14725.04s] English:** and the data that we all have access to that we can make something that behaves like a human being  
**Translation:** 

**[14732.80s] English:** or like a living creature and that can then be educated in whatever ways that we need to get to  
**Translation:** 

**[14738.80s] English:** the point where we can have universal remote workers where anything that somebody does  
**Translation:** 

**[14744.50s] English:** mediated by a computer and doesn't require physical interaction um that an agi will be  
**Translation:** 

**[14749.90s] English:** able to do we can already simulate the you know the equivalent of the zoom uh the zoom meetings  
**Translation:** Vocabulary: mediated: 由...介导; simulate: 模拟

**[14754.88s] English:** with avatars and uh synthetic deep fakes and whatnot we can definitely do  
**Translation:** 

**[14760.00s] English:** that. We have superhuman capabilities on any narrow thing that we can formalize and make a  
**Translation:** Vocabulary: avatars: 虚拟化身; synthetic: 合成的; whatnot: 等等

**[14766.76s] English:** loss function for. But there's things we don't know how to do now. But I don't think they are  
**Translation:** 

**[14771.88s] English:** unapproachably hard. Now, that's incredibly hubristic to say that it's like, but I think  
**Translation:** Vocabulary: hubristic: 自大

**[14777.56s] English:** that what I said a couple years ago is a 50% chance that somewhere there will be signs of life  
**Translation:** 

**[14783.36s] English:** of AGI in 2030. And I've probably increased that slightly. I may be at 55, 60% now, because I do  
**Translation:** 

**[14791.14s] English:** think there's a little sense of acceleration there. So I wonder what the, and by the way,  
**Translation:** 

**[14796.52s] English:** you also written that I bet with hindsight, we will find that clear antecedents of all the  
**Translation:** Vocabulary: acceleration: 加速; antecedents: 先例; hindsight: 事后诸葛

**[14802.70s] English:** critical remaining steps for AGI are already buried somewhere in the vast literature of today.  
**Translation:** 

**[14808.42s] English:** So the ideas are already there. I think that's likely the case. One of the things that  
**Translation:** 

**[14813.20s] English:** appears to be the case is that AGI is already buried somewhere in the vast literature of today.  
**Translation:** 

**[14813.34s] English:** to so many people, including me about the promise that AGI is, we know that we're only drinking from  
**Translation:** 

**[14819.94s] English:** a straw from the fire hose of all the information out there. I mean, you look at just in a very  
**Translation:** 

**[14825.90s] English:** narrowly bounded field, like machine learning, like you can't read all the papers that that  
**Translation:** 

**[14830.34s] English:** come out all the time. You can't go back and read all the clever things that people did in the 90s  
**Translation:** 

**[14835.50s] English:** or earlier that people have forgotten about because they didn't pan out at the time when  
**Translation:** 

**[14839.18s] English:** they were trying to do them with 12 neurons. I am. So then, you know, I think that's, I think  
**Translation:** 

**[14843.18s] English:** this idea that, yeah, I think there are gems buried in some of the older literature that was  
**Translation:** Vocabulary: neurons: 神经元

**[14849.04s] English:** not the path taken by everything. And you can see a kind of herd mentality on the things that  
**Translation:** 

**[14854.24s] English:** happen right now. It's almost funny to see, like, oh, Google does something and OpenAI does  
**Translation:** 

**[14858.90s] English:** something, Meta does something. And, you know, they're the same people that all talk to each  
**Translation:** 

**[14863.12s] English:** other and they're all one-upping each other and they're all capable of implementing each other's  
**Translation:** Vocabulary: implementing: 执行

**[14867.46s] English:** work given a month or two after somebody has an announcement of that. But there's a,  
**Translation:** 

**[14873.06s] English:** there's a, there's a, there's a, there's a, there's a, there's a, there's a, there's a,  
**Translation:** 

**[14873.16s] English:** there's a whole world of possible approaches to machine learning. And I think that we probably  
**Translation:** 

**[14879.28s] English:** will in hindsight.  
**Translation:** 

**[14880.00s] English:** site, go back and see. It's like, yeah, that was kind of clearly predicted by this early paper  
**Translation:** 

**[14884.96s] English:** here. And this turns out that if you do this and this and take this result from animal training  
**Translation:** 

**[14891.18s] English:** and this thing from neuroscience over here and put it together and set up this curriculum for  
**Translation:** 

**[14896.22s] English:** them to learn in, that that's kind of what it took. You don't have too many people now that  
**Translation:** Vocabulary: neuroscience: 神经科学

**[14901.60s] English:** are still saying it's not possible or it's going to take hundreds of years. And 10 years ago,  
**Translation:** 

**[14906.38s] English:** you would get a collection of experts and you would have a decent chunk on the margin that  
**Translation:** 

**[14911.50s] English:** either say not possible or a couple hundred years, might be centuries. And the median estimate would  
**Translation:** 

**[14918.06s] English:** be like 50, 70 years. And it's been coming down. And I know with me saying eight years for something  
**Translation:** 

**[14924.08s] English:** that still puts me on the optimistic side, but it's not crazy out in the fringes. And just being  
**Translation:** 

**[14929.82s] English:** able to look at that at a meta level about the trend of the predictions going  
**Translation:** Vocabulary: fringes: 边缘; optimistic: 乐观

**[14936.14s] English:** down.  
**Translation:** 

**[14936.38s] English:** The idea that something could be happening relatively soon. Now, I do not believe in  
**Translation:** 

**[14943.76s] English:** fast takeoffs. That's one of the safety issues that people say it's like, oh, it's going to go  
**Translation:** 

**[14947.50s] English:** foom and the AI is going to take over the world. There's a lot of reasons. I don't think that's  
**Translation:** Vocabulary: takeoffs: 起飞

**[14952.40s] English:** a credible position. And I think that we will go from a point where we start seeing things that  
**Translation:** 

**[14958.64s] English:** credibly look like animals behaviors and have a human voice box wired into them.  
**Translation:** Vocabulary: credible: 可信的; credibly: 可信地

**[14965.44s] English:** It's like I tried to  
**Translation:** 

**[14966.36s] English:** get Elon to say it's like your pig at Neuralink. Give it a human voice box and let it start  
**Translation:** 

**[14971.08s] English:** learning human words. I think animal intelligence is closer to human intelligence than a lot of  
**Translation:** 

**[14977.58s] English:** people like to think. And I think that culture and modalities of IO make the gulf seem a lot  
**Translation:** Vocabulary: modalities: 感知方式

**[14984.26s] English:** bigger than it actually is. There's just that smooth spectrum of how the brain developed and  
**Translation:** 

**[14989.26s] English:** cortexes and scaling of different things going on there.  
**Translation:** Vocabulary: cortexes: 脑皮层

**[14993.00s] English:** Cultural modalities of IO. Yes, languages,  
**Translation:** 

**[14996.36s] English:** the sort of loss in translation.  
**Translation:** 

**[15000.00s] English:** conceals a lot of intelligence and uh so you when you think about signs of life for agi you're  
**Translation:** 

**[15006.92s] English:** thinking about human interpretable signs so the example i give it if we get to the point where  
**Translation:** Vocabulary: conceals: 隐藏; interpretable: 可理解的

**[15012.62s] English:** you've got a learning disabled toddler some some kind of real special needs uh child that can still  
**Translation:** 

**[15018.80s] English:** interact with their favorite tv show and video game and can be trained and learn in some  
**Translation:** Vocabulary: toddler: 学步儿童

**[15024.86s] English:** appreciably human-like way at that point you can deploy an army of engineers cognitive scientists  
**Translation:** 

**[15031.80s] English:** education developmental uh developmental education people and you've got so many advantages there  
**Translation:** Vocabulary: appreciably: 明显地; cognitive: 认知的; deploy: 部署

**[15037.46s] English:** unlike real education where you can do rollbacks and ab testing and you can find a golden path  
**Translation:** 

**[15042.20s] English:** through a curriculum of different things if you get to that point learning disabled toddler i think  
**Translation:** Vocabulary: rollbacks: 回滚

**[15047.82s] English:** that it's uh it's going to be a done deal do you but do you think we'll we'll know when we see it  
**Translation:** 

**[15053.48s] English:** so uh there's  
**Translation:** 

**[15054.86s] English:** there's been a lot of really interesting general learning progress from deep mind uh open the eye  
**Translation:** 

**[15061.10s] English:** a little bit too i tend to believe that tesla autopilot deserves a lot more credit than it's  
**Translation:** 

**[15068.24s] English:** getting for making progress on the general on sort of on the doing the multi-task learning  
**Translation:** 

**[15074.92s] English:** thing and increasing the number of tasks and automating that uh process of uh sort of  
**Translation:** Vocabulary: automating: 自动化

**[15082.56s] English:** learning from the edge discovering the edge  
**Translation:** 

**[15084.84s] English:** cases and learning from the edge cases that is it's really approaching from a different angle  
**Translation:** 

**[15090.20s] English:** the general learning problem of agi but the more clear approach comes from deep mind where you have  
**Translation:** 

**[15096.52s] English:** these kind of game situations and you uh build systems there but i i don't know uh people seem  
**Translation:** 

**[15104.24s] English:** to be quite um yeah there will always be people that just won't believe it and i fundamentally  
**Translation:** 

**[15111.00s] English:** don't care i mean i don't care if they don't believe it i  
**Translation:** Vocabulary: fundamentally: 从根本上

**[15114.84s] English:** you know when it starts doing people's jobs and i mean i don't care about the philosophical zombie  
**Translation:** 

**[15120.00s] English:** Absolutely. But do you think you will notice that something special has happened here? Because to me, I've been noticing a lot of special things. I think a lot of credit should go to DeepMind for AlphaZero. That was truly special.  
**Translation:** 

**[15140.14s] English:** The self-play mechanisms achieve, sort of solve problems that used to be thought unsolvable, like the game of Go. Also, I mean, protein folding, starting to get into that space where learning is doing, at first there's not, it wasn't end-to-end learning, now it's end-to-end learning of a very difficult, previously thought unsolvable problem of protein folding.  
**Translation:** 

**[15164.68s] English:** And so, yeah, where do you think...  
**Translation:** Vocabulary: unsolvable: 无法解决的

**[15170.14s] English:** I think it would be a really magical moment for you.  
**Translation:** 

**[15200.14s] English:** It's not close to a being. It's not close to a being that's going through a lifelong learning process.  
**Translation:** 

**[15207.16s] English:** Do you want something that kind of gives signs of a being? Like, what's the difference between a neural network, a feed-forward neural network, and a being?  
**Translation:** 

**[15220.10s] English:** Fundamentally, the brain is a recurrent neural network generating an action policy. I mean, it's implemented on a biological substrate.  
**Translation:** Vocabulary: neural: 神经的

**[15227.44s] English:** And it's interesting thinking about things like that, where...  
**Translation:** 

**[15230.14s] English:** We know, fundamentally, the brain is not a convolutional neural network or a transformer. Those are specialized things that are very valuable for what we're doing. But it's not the way the brain's...  
**Translation:** Vocabulary: convolutional: 卷积的

**[15240.00s] English:** doing. Now, I do think consciousness and AI in general is a substrate independent mechanism where  
**Translation:** 

**[15246.96s] English:** it doesn't have to be implemented the way the brain is. But if you've only got one existence  
**Translation:** Vocabulary: substrate: 基质

**[15251.22s] English:** proof, there's certainly some value in caring about what it says and does. And so the idea  
**Translation:** 

**[15258.74s] English:** that anything that can be done with a narrow AI that you can quantify up a loss function for  
**Translation:** Vocabulary: quantify: 量化

**[15264.08s] English:** or reward mechanism, you're almost certainly going to be able to produce something that's more  
**Translation:** 

**[15268.90s] English:** resource effective to train and deploy and use in an inference mode, train a whole lot using an  
**Translation:** Vocabulary: deploy: 部署; inference: 推理

**[15274.48s] English:** inference. But a living being is going to be something that's a continuous lifelong learned  
**Translation:** 

**[15280.34s] English:** task agnostic thing. So the lifelong learning is really important too, and the long-term memory.  
**Translation:** 

**[15288.82s] English:** So memory is a big weird part of that puzzle. Yeah, memory is a huge thing. And we've got,  
**Translation:** 

**[15292.92s] English:** again, I have all the respect in the world for the amazing things that are being done now, but  
**Translation:** 

**[15297.42s] English:** sometimes they can be taken.  
**Translation:** 

**[15298.90s] English:** A little bit out of context with things like, there's some smoke and mirrors going on, like the  
**Translation:** 

**[15304.44s] English:** Gato, the recent work, the multitask learning stuff. It's amazing that it's one model that  
**Translation:** 

**[15310.46s] English:** plays all the Atari games as well as doing all of these other things. But of course, it didn't learn  
**Translation:** Vocabulary: multitask: 多任务学习

**[15316.70s] English:** to do all of those. It was instructed in doing that by other reinforcement learners going through  
**Translation:** 

**[15321.78s] English:** and doing that. And even in the case of all the games, it's still going with a specific hand-coded  
**Translation:** Vocabulary: instructed: 指导; reinforcement: 强化

**[15327.80s] English:** reward function.  
**Translation:** 

**[15328.90s] English:** In each of those Atari games, where it's not that, you know, how does it, it just wants to  
**Translation:** 

**[15333.48s] English:** spend its summer afternoon playing Atari because that's the most interesting thing for it. So it's  
**Translation:** 

**[15338.26s] English:** again, not a general, it's not learning the way humans learn. And there's, I believe, a lot of  
**Translation:** 

**[15343.96s] English:** things that are challenging to make a loss function for that you can train through these  
**Translation:** 

**[15349.20s] English:** existing conventional things. We're going to chip away at all the things that people do that we can  
**Translation:** 

**[15355.48s] English:** turn into narrow AI problems.  
**Translation:** 

**[15358.90s] English:** And billions of  
**Translation:** 

**[15360.00s] English:** the trillions of dollars of value are going to be created by that. But there's still going to  
**Translation:** 

**[15364.90s] English:** be a set of things, and we've got questionable cases like the self-driving car, where it's  
**Translation:** Vocabulary: trillions: 万亿

**[15369.86s] English:** possible, it's not my bet, but it's plausible that the long tail could be problematic enough  
**Translation:** 

**[15375.16s] English:** that that really does require a full-on artificial general intelligence. The counter-argument is that  
**Translation:** 

**[15381.44s] English:** data solves almost everything. Everything is an interpolation problem if you have enough data,  
**Translation:** 

**[15385.10s] English:** and Tesla may be able to get enough data from all of their deployed stuff to be able to work like  
**Translation:** Vocabulary: deployed: 部署的; interpolation: 插值

**[15390.62s] English:** that, but maybe not. There are all the other problems about, say, you want to have a strategy  
**Translation:** 

**[15395.74s] English:** meeting, and you want to go ahead and bring in all of your remote workers and your consultants,  
**Translation:** 

**[15401.12s] English:** and you want a world where some of those could be AIs that are talking and interacting with you  
**Translation:** 

**[15407.46s] English:** in an area that is too murky to have a crisp loss function, but they still have things that,  
**Translation:** Vocabulary: murky: 模糊不清

**[15413.44s] English:** on some level, they're...  
**Translation:** 

**[15415.10s] English:** Rewarded on some internal level for building a valuable-to-humans  
**Translation:** 

**[15418.98s] English:** kind of life and ability to interact with things.  
**Translation:** 

**[15423.36s] English:** See, I still think that self-driving cars, solving that problem, will take us very far  
**Translation:** 

**[15429.04s] English:** towards AGI. You might not need AGI, but I am really inspired by what Autopilot is doing.  
**Translation:** 

**[15436.80s] English:** Waymo, some of the other companies, I think Waymo leads the way there. It's also really  
**Translation:** 

**[15442.96s] English:** interesting, but they don't have quite as ambitious...  
**Translation:** 

**[15445.10s] English:** They don't have quite as ambitious of an effort in terms of learning-based,  
**Translation:** 

**[15448.74s] English:** sort of data-hungry approach to driving, which I think is very close to the kind of thing that  
**Translation:** 

**[15454.78s] English:** would take us far towards AGI.  
**Translation:** 

**[15457.42s] English:** Yeah, and it's a funny thing, because as far as I can tell, Elon is completely serious about all  
**Translation:** 

**[15462.54s] English:** of his concerns about AGI being an existential threat. And I tried to draw him out to talk  
**Translation:** Vocabulary: existential: 根本的

**[15468.38s] English:** about AI, and he just didn't want to. And I think that I get that little fatalistic sense from him.  
**Translation:** 

**[15474.34s] English:** It's weird, because...  
**Translation:** 

**[15475.02s] English:** Because his company could very well be the leading company leading towards a lot of that, where...  
**Translation:** 

**[15480.00s] English:** Tesla being a super pragmatic company that's doing things because they really want to solve  
**Translation:** Vocabulary: pragmatic: 实用主义的

**[15485.90s] English:** this actual problem. It's a different vibe than the research-oriented companies where it's a great  
**Translation:** 

**[15491.18s] English:** time to be an AI researcher. You've got your pick of trillion-dollar companies that will pay you to  
**Translation:** 

**[15496.00s] English:** kind of work on the problems you're interested in, but that's not necessarily driving hard towards  
**Translation:** 

**[15500.80s] English:** the core problem of AGI as something that's going to produce a lot of value by doing things that  
**Translation:** 

**[15506.52s] English:** people currently do or would like to do. I mean, I have a million questions to you  
**Translation:** 

**[15512.48s] English:** about your ideas about AGI, but do you think it needs to be embodied? Do you think it needs to  
**Translation:** Vocabulary: embodied: 具象化

**[15519.92s] English:** have a body to start to notice the signs of life and to develop the kind of system that's able  
**Translation:** 

**[15527.22s] English:** to reason, perceive the world in the way that an AGI should and act in the world? So should we be  
**Translation:** Vocabulary: perceive: 感知

**[15534.24s] English:** thinking about robots or can this be achieved?  
**Translation:** 

**[15536.52s] English:** I have a clear opinion on that, and that's that no, it does not need to be embodied in the physical  
**Translation:** 

**[15543.80s] English:** world, where you could say most of my career is about making simulated virtual worlds in games  
**Translation:** 

**[15550.42s] English:** or virtual reality. And so on a fundamental level, I believe that you can make a simulated  
**Translation:** Vocabulary: simulated: 模拟的

**[15555.52s] English:** environment that provides much of the value of what the real environment does. And restricting  
**Translation:** 

**[15560.78s] English:** yourself to operating at real time in the physical world with physical objects, I think, is an  
**Translation:** 

**[15566.18s] English:** enormous handicap. I mean, that's one of the real lessons driven home by all my aerospace work is  
**Translation:** 

**[15571.62s] English:** that, you know, reality is a bitch in so many ways there. We're dealing with all the mechanical  
**Translation:** Vocabulary: aerospace: 航空航天; handicap: 不利因素

**[15577.56s] English:** components, like everything fails, Murphy's law, even if you've done it right before on your fifth  
**Translation:** 

**[15582.34s] English:** one, it might come out differently. So yeah, I think that anybody that is all in on the embodied  
**Translation:** 

**[15589.20s] English:** aspect of it, they are tying a huge weight to their ankles. And I think that I would,  
**Translation:** 

**[15596.18s] English:** almost count them out, anybody that's making that a cornerstone of their belief about it,  
**Translation:** Vocabulary: cornerstone: 基础

**[15600.00s] English:** I would almost write them off as being worried about them getting to AGI first.  
**Translation:** 

**[15604.84s] English:** I was very surprised that Elon's big on the humanoid robots.  
**Translation:** Vocabulary: humanoid: 类人形

**[15609.24s] English:** I mean, like the NASA Robonaut stuff was always almost a gag line.  
**Translation:** 

**[15612.78s] English:** Like, what are you doing, people?  
**Translation:** Vocabulary: robonaut: 机器人外骨骼

**[15614.60s] English:** Well, that's very interesting because he has a very pragmatic view of that.  
**Translation:** 

**[15618.20s] English:** That's just a way to solve a particular problem in a factory.  
**Translation:** Vocabulary: pragmatic: 实用主义

**[15623.68s] English:** Now, I do think that once you have an AGI, robotic bodies, humanoid bodies are going  
**Translation:** 

**[15628.30s] English:** to be enormously valuable.  
**Translation:** Vocabulary: enormously: 极其

**[15629.56s] English:** I just don't think they're helpful getting to AGI.  
**Translation:** 

**[15632.62s] English:** Well, he has a very sort of practical view, which I disagree with and argue with him.  
**Translation:** 

**[15637.44s] English:** But it's a practical view that there's, you know, you could transfer the problem of driving  
**Translation:** 

**[15643.02s] English:** to the problem of robotic manipulation because so much of it is perception.  
**Translation:** Vocabulary: manipulation: 操作

**[15649.90s] English:** It's perception and action, and it's just a different context.  
**Translation:** 

**[15653.08s] English:** And so you can apply all the same kind of data engine learning processes to a different  
**Translation:** 

**[15659.22s] English:** environment.  
**Translation:** 

**[15659.56s] English:** And so why not apply it to the humanoid robot environment?  
**Translation:** 

**[15663.74s] English:** But I think, I do think that there's a certain magic to the embodied robot.  
**Translation:** 

**[15672.54s] English:** That may be the thing that finally convinces people.  
**Translation:** Vocabulary: convinces: 说服; embodied: 具象化

**[15675.48s] English:** Yes.  
**Translation:** 

**[15675.72s] English:** But again, I don't really care that much about convincing people.  
**Translation:** 

**[15678.82s] English:** You know, the world that I'm looking towards is, you know, you go to the website and say,  
**Translation:** 

**[15684.50s] English:** I want five Frank 1As to, you know, to work on my team today.  
**Translation:** 

**[15688.08s] English:** And they all spin up.  
**Translation:** 

**[15689.18s] English:** And they start showing up in your Zoom meetings.  
**Translation:** 

**[15690.90s] English:** To push back, but also to agree with you.  
**Translation:** 

**[15693.66s] English:** But first to push back, I do think you need to convince people for them to welcome that  
**Translation:** 

**[15698.52s] English:** thing into their life.  
**Translation:** 

**[15700.94s] English:** I think there's enough businesses that operate on an objective kind of profit loss sort of  
**Translation:** 

**[15705.86s] English:** basis that, I mean, if you look at how many things, again, talking about the world as  
**Translation:** 

**[15710.80s] English:** an evolutionary space there, when you do have free markets and you have entrepreneurs, you  
**Translation:** Vocabulary: entrepreneurs: 企业家; evolutionary: 进化的

**[15716.68s] English:** are going to have people that are going to be willing to go out and try.  
**Translation:** 

**[15719.02s] English:** And I think you need to push back.  
**Translation:** 

**[15719.78s] English:** I think you need to push back.  
**Translation:** 

**[15720.00s] English:** things and when it proves to be beneficial you know there's fast followers in all sorts of places  
**Translation:** 

**[15725.40s] English:** yeah and and you're saying that i mean you know quake and vr is a kind of embodiment but just in  
**Translation:** 

**[15732.40s] English:** in a digital world and if if you're able to demonstrate if you're able to do something  
**Translation:** Vocabulary: embodiment: 化身

**[15737.44s] English:** productive in that kind of digital reality uh then then agi doesn't need to have a body yeah  
**Translation:** 

**[15746.12s] English:** it's like one of the really practical technical questions that i kind of keep arguing with myself  
**Translation:** 

**[15750.62s] English:** over if you're doing a training and learning and you've got like you can watch sesame street you  
**Translation:** 

**[15756.02s] English:** can play master system games or something is it enough to have just a video feed that that is that  
**Translation:** Vocabulary: sesame: 芝麻

**[15761.60s] English:** video coming in or should it literally be on a virtual tv set in a virtual room even if it's  
**Translation:** 

**[15768.12s] English:** you know a simple room just to have that sense of you're looking at a 2d projection on a screen  
**Translation:** Vocabulary: projection: 屏幕显示

**[15772.88s] English:** versus having the screen beamed directly into your retinas  
**Translation:** 

**[15775.84s] English:** and i you know i think it's possible to maybe get past some of these signs of life of things with the  
**Translation:** 

**[15782.64s] English:** just kind of projected directly into the receptor fields but eventually for more uh kind of human  
**Translation:** 

**[15789.38s] English:** emotional connection for things probably having some vr room with a lot of screens in it for the  
**Translation:** Vocabulary: projected: 投射; receptor: 感受器

**[15795.88s] English:** ai to be learning in is likely helpful it may be a world of different ais interacting with each other  
**Translation:** 

**[15802.04s] English:** self-play i do think is one of the critical things where socialization wise one of the  
**Translation:** 

**[15805.82s] English:** other limitations i set for myself thinking about thing these is i i need something that is at least  
**Translation:** 

**[15812.76s] English:** potentially real time because i want it's nice you can always slow down time you can run on a  
**Translation:** 

**[15818.44s] English:** subscale system and and test an algorithm at some lower level and if you've got extra horsepower  
**Translation:** 

**[15823.60s] English:** running it faster than real time is a great thing but i want to be able to i am to have  
**Translation:** Vocabulary: algorithm: 算法; horsepower: 计算能力; subscale: 缩小比例

**[15829.58s] English:** the ais either socially interact with each other or critically with actual people you're  
**Translation:** 

**[15835.68s] English:** sort of child development psychiatrist that comes in and and interacts and does  
**Translation:** Vocabulary: critically: 严厉地; interacts: 互动; psychiatrist: 精神医生

**[15840.00s] English:** the good boy, bad boy sort of thing as they're going through and exploring different things.  
**Translation:** 

**[15845.92s] English:** And it's nice to, I come back to the value of constraints in a lot of ways. And if I say,  
**Translation:** Vocabulary: constraints: 限制

**[15850.96s] English:** well, one of my constraints is real-time operation. I mean, it might still be a huge  
**Translation:** 

**[15855.46s] English:** data center full of computers, but it should be able to interact on a Zoom meeting with people.  
**Translation:** 

**[15862.24s] English:** And that's how you also do start convincing people, even if it's not a robot body moving  
**Translation:** 

**[15866.14s] English:** around, which eventually gets to irrefutable levels. But if you can go ahead and not just  
**Translation:** Vocabulary: irrefutable: 无可辩驳

**[15871.54s] English:** type back and forth to a GPT bot on something, but you're literally talking to them in an  
**Translation:** 

**[15877.24s] English:** embodied over Zoom form and working through problems with them or exploring situations,  
**Translation:** Vocabulary: embodied: 具象化

**[15883.56s] English:** having conversations that are fully stateful and learned, I think that that's a valuable thing.  
**Translation:** 

**[15890.08s] English:** So I do keep all of my eyes on things that can be implemented within sort of that 30 frames per  
**Translation:** Vocabulary: stateful: 状态相关的

**[15895.82s] English:** second.  
**Translation:** 

**[15896.56s] English:** I kind of work, and I think that's feasible.  
**Translation:** 

**[15899.32s] English:** Do you think the most compelling experiences that first will be for pleasure or for business,  
**Translation:** 

**[15905.82s] English:** as they ask in airports? So meaning, if it's interacting with AI agents, will it be sort of  
**Translation:** Vocabulary: compelling: 引人入胜的

**[15917.20s] English:** like friends, entertainment, almost like a therapist or whatever, that kind of interaction?  
**Translation:** 

**[15926.14s] English:** Or is it in the business setting, something, like you said, brainstorming different ideas?  
**Translation:** Vocabulary: brainstorming: 头脑风暴; therapist: 治疗师

**[15932.06s] English:** Sort of, this is all a different formulation of kind of a Turing test or the spirit of the  
**Translation:** 

**[15936.64s] English:** original Turing test. Where do you think the biggest benefit will first come?  
**Translation:** Vocabulary: turing: 图灵测试

**[15940.64s] English:** So it's going to start off hugely expensive. I mean, you're going to,  
**Translation:** 

**[15944.30s] English:** if we're still all guessing about what compute is going to be necessary, I fall on the side of,  
**Translation:** 

**[15949.16s] English:** I don't think, you run the numbers and you're like 86 billion neurons, 100 trillion synapses.  
**Translation:** 

**[15953.88s] English:** I don't think those all need to be weights.  
**Translation:** 

**[15956.14s] English:** I don't think we need models that are quite that big, evaluated quite that often.  
**Translation:** 

**[15960.00s] English:** I based that on. We've got reasonable estimates of what some parts of the brain do. We don't have  
**Translation:** Vocabulary: evaluated: 评估

**[15966.08s] English:** the neocortex formula, but we kind of get some of the other sensory processing. And it doesn't feel  
**Translation:** 

**[15970.80s] English:** like we need to. We can simulate that in computers for less weights. But still, it's probably going  
**Translation:** Vocabulary: neocortex: 新皮层; simulate: 模拟

**[15977.22s] English:** to be thousands of GPUs to be running a human-level AGI. Depending on how it's implemented,  
**Translation:** 

**[15983.72s] English:** that might give you sort of a clan of 128 kind of run-in batch people, depending on whether they're  
**Translation:** 

**[15989.86s] English:** sparsity in the way the weights and things are set up. If it is a reasonably dense thing,  
**Translation:** 

**[15995.08s] English:** then just the memory bandwidth trade-offs means you get 128 of them at the same time. And either  
**Translation:** Vocabulary: bandwidth: 带宽; reasonably: 较为; sparsity: 稀疏性

**[16000.48s] English:** it's all feeding together, learning in parallel, or kind of all running together, kind of talking  
**Translation:** 

**[16006.04s] English:** to a bunch of people. But still, if you've got thousands of GPUs necessary to run these things,  
**Translation:** 

**[16011.86s] English:** it's going to be kind of expensive, where it might start off $1,000 an hour for even post-development  
**Translation:** 

**[16019.32s] English:** or something.  
**Translation:** 

**[16019.86s] English:** For that, which would be something that you would only use for a business,  
**Translation:** 

**[16024.24s] English:** something where you think they're going to help you make a strategic decision or point out  
**Translation:** 

**[16028.44s] English:** something super important. But I also am completely confident that we will have another  
**Translation:** 

**[16034.22s] English:** factor of $1,000 in cost performance increase in AGI-type calculations.  
**Translation:** 

**[16040.76s] English:** Not in general computing, necessarily, but there's so much more that we can do with  
**Translation:** 

**[16044.62s] English:** packaging, making those right trade-offs, all those same types of things that  
**Translation:** Vocabulary: computing: 计算机技术

**[16048.20s] English:** in the next couple of decades, we're going to be able to do.  
**Translation:** 

**[16049.86s] English:** And then you're down to $1 an hour. And then you're kind of like, well, I should have an  
**Translation:** 

**[16056.64s] English:** entourage of AIs that are following me around, helping me out on anything that I want them to do.  
**Translation:** 

**[16062.92s] English:** That's one interesting trajectory, but I'll push back. So in that case, if you want to pay  
**Translation:** Vocabulary: entourage: 随从; trajectory: 轨迹

**[16070.96s] English:** thousands of dollars, it should actually provide some value. I think it's easier for cheaper to  
**Translation:** 

**[16078.34s] English:** provide value.  
**Translation:** 

**[16079.86s] English:** I think it's easier for cheaper to provide value.  
**Translation:** 

**[16080.00s] English:** to provide value via a dumb AI that will take us towards AGI, to just have a friend.  
**Translation:** 

**[16088.78s] English:** I think there's an ocean of loneliness in the world.  
**Translation:** 

**[16092.44s] English:** And I think an effective friend that doesn't have to be perfect, that doesn't have to be intelligent,  
**Translation:** Vocabulary: loneliness: 孤独

**[16098.06s] English:** that has to be empathic, having emotional intelligence, having ability to remember things, having ability to listen.  
**Translation:** 

**[16106.46s] English:** Most of us don't listen to each other.  
**Translation:** Vocabulary: empathic: 共情的

**[16108.32s] English:** One of the things that love and when you care about somebody, when you love somebody, is when you listen.  
**Translation:** 

**[16114.30s] English:** And that is something we treasure about each other.  
**Translation:** 

**[16117.62s] English:** And if an AI can do that kind of thing, I think that provides a huge amount of value.  
**Translation:** 

**[16124.40s] English:** And very importantly, provides value in its ability to listen and understand versus provide really good advice.  
**Translation:** 

**[16133.64s] English:** I think providing really good advice is another.  
**Translation:** 

**[16138.32s] English:** The next level step that would, I think it's just easier to do companionship.  
**Translation:** Vocabulary: companionship: 同伴陪伴

**[16145.34s] English:** Yeah, I wouldn't disagree.  
**Translation:** 

**[16146.32s] English:** I mean, I think that there's very few things that I would argue can't be reduced to some kind of a narrow AI.  
**Translation:** 

**[16153.90s] English:** I think we can do a trillion dollars of value easily and all the things that can be done there.  
**Translation:** 

**[16158.80s] English:** And a lot of it can be done with smoke and mirrors without having to go the whole thing.  
**Translation:** Vocabulary: trillion: 万亿

**[16162.58s] English:** I mean, there's going to be the equivalent of the Doom version for the AGI.  
**Translation:** 

**[16168.32s] English:** It's not really AGI.  
**Translation:** 

**[16169.82s] English:** It's all smoke and mirrors, but it happens to do enough valuable things that it's enormously useful and valuable to people.  
**Translation:** 

**[16176.66s] English:** But at some point, you do want to get to the point where you have the fully general thing and you stop making bespoke specialized systems for each thing.  
**Translation:** Vocabulary: bespoke: 量身定制; enormously: 极其

**[16184.00s] English:** And you wind up start using the higher level language instead of writing everything in assembly language.  
**Translation:** 

**[16190.10s] English:** What about consciousness?  
**Translation:** 

**[16192.76s] English:** The C word.  
**Translation:** 

**[16194.30s] English:** What do you think that's fundamental to solving AGI?  
**Translation:** 

**[16198.32s] English:** Or is it a quirk?  
**Translation:** 

**[16200.00s] English:** of human cognition? So I think most of the arguments about consciousness don't have a whole  
**Translation:** Vocabulary: cognition: 认知; quirk: 怪癖

**[16207.00s] English:** lot of merit. I think that consciousness is kind of the way the brain feels when it's operating.  
**Translation:** 

**[16214.40s] English:** And this idea that, you know, I do generally subscribe to sort of the pandemonium theories  
**Translation:** Vocabulary: merit: 优点; pandemonium: 混乱; subscribe: 订阅

**[16220.72s] English:** of consciousness where there's all these things bubbling around. And I think of them as kind of  
**Translation:** 

**[16225.50s] English:** slightly randomized, sparse distributed memory bit strings of things that are kind of happening,  
**Translation:** Vocabulary: bubbling: 沸腾; randomized: 随机化; sparse: 稀疏

**[16230.86s] English:** recalling different associative memories. And eventually you get some level of consensus,  
**Translation:** 

**[16235.26s] English:** and it bubbles up to the point of being a conscious thought there. And the little bits  
**Translation:** Vocabulary: associative: 联想; recalling: 回忆

**[16239.46s] English:** of stochasticity that are sitting on in this as it cycles between different things and recalls  
**Translation:** 

**[16244.44s] English:** different memory, that's largely our imagination and creativity. So I don't think there's anything  
**Translation:** Vocabulary: stochasticity: 随机性

**[16250.88s] English:** deeply magical about it, certainly not symbolic. I think it is generally the  
**Translation:** 

**[16255.34s] English:** flow of consciousness. I don't think there's anything deeply magical about it, certainly not  
**Translation:** 

**[16255.48s] English:** symbolic. I think it is generally the flow of consciousness. I don't think there's anything  
**Translation:** 

**[16255.50s] English:** of these associations drawn up with stochastic noise overlaid on top of them. And I think so  
**Translation:** Vocabulary: overlaid: 叠加; stochastic: 随机; symbolic: 象征

**[16263.64s] English:** much of that is like, it depends on what you happen to have in your field of view as some  
**Translation:** 

**[16267.78s] English:** other thought was occurring to you that overlay and blend into the next key that queries your  
**Translation:** 

**[16272.68s] English:** memory for things. And that kind of determines how, you know, how your chain of consciousness goes.  
**Translation:** 

**[16278.04s] English:** So that's kind of the qualia, the subjective experience of it is not essential for intelligence.  
**Translation:** 

**[16284.80s] English:** I don't think so.  
**Translation:** 

**[16285.42s] English:** I don't think there's anything really important there.  
**Translation:** 

**[16288.56s] English:** What about some other human qualities like fear of mortality and stuff like that? Like  
**Translation:** 

**[16292.42s] English:** the fact that this ride ends? Is that important? Like, you know, we've talked so much throughout  
**Translation:** 

**[16299.90s] English:** this conversation about the value of deadlines and constraints. Do you think that's important  
**Translation:** 

**[16305.08s] English:** for intelligence?  
**Translation:** Vocabulary: constraints: 限制; deadlines: 截止日期

**[16305.86s] English:** That's actually a super interesting angle that I don't usually take on that about has  
**Translation:** 

**[16310.10s] English:** death being a deadline that forces you to make better decisions. Because I have heard people  
**Translation:** 

**[16314.88s] English:** talk about it. I've heard people talk about it. I've heard people talk about it. I've heard people  
**Translation:** 

**[16315.40s] English:** talk about how if you have immortality, people are going to stop stop trying and working on things  
**Translation:** Vocabulary: immortality: 永生

**[16320.00s] English:** They've got all the time in the world, but I would say that I don't expect it to be a  
**Translation:** 

**[16326.82s] English:** super critical thing that a sense of mortality and death, impending death, is necessary there  
**Translation:** Vocabulary: impending: 将要来临的

**[16333.46s] English:** because those are things that they do wind up providing reward signals to us, and we  
**Translation:** 

**[16337.74s] English:** will be in control of the reward signals, and there will have to be something fundamental  
**Translation:** 

**[16341.88s] English:** that causes, that engenders curiosity and goal setting and all of that.  
**Translation:** 

**[16346.44s] English:** And something is going to play in there at the reward level, whether it's positive or  
**Translation:** Vocabulary: engenders: 引发

**[16353.28s] English:** negative or both.  
**Translation:** 

**[16354.60s] English:** I don't have any strong opinions on exactly what it's going to be, but that's that type  
**Translation:** 

**[16360.94s] English:** of thing where I doubt that might be one of those half dozen key things that has to be  
**Translation:** 

**[16365.90s] English:** sorted out on exactly what the master reward that's the meta reward over all of the local  
**Translation:** 

**[16372.06s] English:** task-specific rewards have to be.  
**Translation:** 

**[16374.12s] English:** That could be that big negative reward of death.  
**Translation:** 

**[16376.44s] English:** Maybe not death, but ability to walk away from an interaction.  
**Translation:** 

**[16381.36s] English:** So it bothers me when people treat AI systems like servants.  
**Translation:** Vocabulary: servants: 仆人

**[16386.86s] English:** So it doesn't bother me, but I mean, it really is drawing the line between what an AI system  
**Translation:** 

**[16394.62s] English:** could be.  
**Translation:** 

**[16395.62s] English:** It's limiting the possibility of what an AI system could be, it's treating them as justice  
**Translation:** 

**[16398.76s] English:** tools.  
**Translation:** 

**[16399.76s] English:** Now that's, of course, from a narrow AI perspective, there's so many problems that  
**Translation:** 

**[16406.38s] English:** narrow AI could solve, just like you said, as in its form of a tool, but it could also  
**Translation:** 

**[16414.56s] English:** be a being, which is much more than a tool.  
**Translation:** 

**[16418.64s] English:** And to become a being, you have to respect that thing for being a being.  
**Translation:** 

**[16424.14s] English:** And for that, it has to be able to make its own decisions, to walk away, to say, I had  
**Translation:** 

**[16431.06s] English:** enough of you.  
**Translation:** 

**[16431.98s] English:** I would like to break up with you now.  
**Translation:** 

**[16434.50s] English:** You've not treated me well.  
**Translation:** 

**[16436.38s] English:** And I would like to move on.  
**Translation:** 

**[16438.10s] English:** So I think that...  
**Translation:** 

**[16440.00s] English:** actually that choice to end things so i i have a couple things on that so on the one hand i it is  
**Translation:** 

**[16449.72s] English:** kind of disturbing when you see people being like people that are mean to robots and you know mean  
**Translation:** 

**[16454.34s] English:** to alexa and whatever and that seems to speak badly about humanity but there's also the exact  
**Translation:** 

**[16460.40s] English:** opposite side of that where you have so many people that imbue humanity in inanimate objects  
**Translation:** Vocabulary: imbue: 赋予; inanimate: 无生命的

**[16465.76s] English:** or things that are toys or that are are relatively limited so i think there may even  
**Translation:** 

**[16470.50s] English:** be more more danger about people putting more emotional investment into a lot of these proto  
**Translation:** Vocabulary: proto: 原型

**[16475.68s] English:** ais in different ways yeah um and then the ai would manipulate that but but as far as like the  
**Translation:** 

**[16482.78s] English:** i ethnic sides of things i really stay away from any of those discussions or even really thinking  
**Translation:** 

**[16489.56s] English:** about it it's similar with the safety things where i think it's just premature and there's a certain  
**Translation:** 

**[16495.10s] English:** class  
**Translation:** Vocabulary: premature: 为时过早

**[16495.76s] English:** people that enjoy thinking about impractical things, things that are not in the world and  
**Translation:** 

**[16500.88s] English:** of pragmatic effect around you. And I think that, again, because I don't think there's going to be  
**Translation:** Vocabulary: impractical: 不切实际; pragmatic: 实用的

**[16507.38s] English:** a fast takeoff, I think we actually will have time to have these debates when we know the shape of  
**Translation:** 

**[16512.18s] English:** what we're debating. And some people do take a principled approach that they think it's going  
**Translation:** Vocabulary: principled: 原则性强

**[16516.50s] English:** to go too fast, that you really do need to get ahead of it, that you need to be thinking about  
**Translation:** 

**[16520.26s] English:** this because we have slow processes of coming to any kind of consensuses or even coming up with  
**Translation:** Vocabulary: consensuses: 共识

**[16525.28s] English:** ideas about this. And maybe that's true. I wouldn't put any of my money or funding into  
**Translation:** 

**[16533.60s] English:** something like that because I don't think it's a problem yet. And I think that we will have these  
**Translation:** 

**[16538.44s] English:** signs of life when we've got our learning disabled toddler, we should really start talking about some  
**Translation:** 

**[16543.94s] English:** of the safety and ethics issues, but probably not before then. Can you elaborate briefly about why  
**Translation:** Vocabulary: elaborate: 详细说明; toddler: 学步儿

**[16550.42s] English:** you don't think there'll be a fast takeoff? Is there some deep intuition you have about it?  
**Translation:** 

**[16555.28s] English:** Is it because it's grounded in the physical world or why?  
**Translation:** Vocabulary: intuition: 直觉

**[16558.40s] English:** Yeah, so it is my...  
**Translation:** 

**[16560.00s] English:** belief that we're going to start off with something that requires thousands of gpus and i i don't know  
**Translation:** 

**[16566.12s] English:** if you've tried to go get a thousand gpu instance on a cloud anytime recently but these are not  
**Translation:** 

**[16571.22s] English:** things that you can just go spin up hundreds of i there are real challenges to i mean these things  
**Translation:** Vocabulary: anytime: 随时

**[16577.74s] English:** are going to take data centers and data centers take years to build you know and the last few  
**Translation:** 

**[16582.86s] English:** years we've seen a few of them kind of coming up going in different places they're big engineering  
**Translation:** 

**[16587.08s] English:** efforts you can hear people bemoan about the fact that i know the the network was wired all wrong  
**Translation:** 

**[16593.84s] English:** and it took them a month to go unwire it and rewire it the right way these aren't things that  
**Translation:** Vocabulary: bemoan: 抱怨; rewire: 重新布线

**[16598.18s] English:** you can just magic into existence and the ideas of i am like the old tropes about it's going to  
**Translation:** 

**[16604.10s] English:** escape onto the internet and take over other systems there's the fast takeoff ones are clearly  
**Translation:** Vocabulary: tropes: 陈词滥调

**[16609.00s] English:** nonsense because you just can't open tcp connections above a certain rate no matter how smart you are  
**Translation:** 

**[16613.92s] English:** even if you have perfect hacking ability that take over the world  
**Translation:** Vocabulary: hacking: 黑客技术

**[16617.06s] English:** in an instant sort of thing just isn't plausible at all and even if you had access to all of the  
**Translation:** 

**[16622.72s] English:** resources these are going to be specialized systems where you're going to wind up with  
**Translation:** Vocabulary: plausible: 合情合理

**[16628.20s] English:** something that is architected around exactly this chip with this interconnect and it's not  
**Translation:** 

**[16633.50s] English:** just going to be able to be plopped somewhere else now interestingly it is going to be something  
**Translation:** Vocabulary: architected: 设计围绕; interconnect: 连接方式; plopped: 随意放置

**[16638.18s] English:** that the entire um the entire code for all of it will easily fit on a thumb drive that's total  
**Translation:** 

**[16643.88s] English:** spy movie thriller sorts of things where  
**Translation:** 

**[16646.36s] English:** you could  
**Translation:** 

**[16647.04s] English:** have hey we crack the secret to agi and it fits on this thumb drive and anyone could steal it now  
**Translation:** 

**[16652.00s] English:** they're still gonna have to build the right data center to deploy it and have the right kind of  
**Translation:** 

**[16656.00s] English:** life experience curriculum to take it up to the point where it's valuable but the real core of it  
**Translation:** Vocabulary: deploy: 部署

**[16661.10s] English:** the the magic that's going to happen there is going to be very small you know it's again tens  
**Translation:** 

**[16666.04s] English:** of thousands of lines of code not millions of lines of code it is possible to imagine a world  
**Translation:** 

**[16670.66s] English:** as you mentioned in the spy thriller view if it's if it's just a few lines of code  
**Translation:** 

**[16677.04s] English:** i think it's not going to be that easy but it's basically  
**Translation:** 

**[16688.92s] English:** kind of a  
**Translation:** 

**[16691.08s] English:** chick  
**Translation:** Vocabulary: chick: 小鸡

**[16692.86s] English:** you have had some  
**Translation:** 

**[16693.14s] English:** 섹  
**Translation:** 

**[16699.44s] English:** so  
**Translation:** 

**[16701.10s] English:** i  
**Translation:** 

**[16701.64s] English:** think  
**Translation:** 

**[16701.68s] English:** everyone  
**Translation:** 

**[16702.26s] English:** ridge  
**Translation:** 

**[16702.92s] English:** ireland  
**Translation:** 

**[16703.34s] English:** lewis  
**Translation:** 

**[16703.92s] English:** leonard  
**Translation:** 

**[16704.54s] English:** baber  
**Translation:** 

**[16705.18s] English:** barrack  
**Translation:** Vocabulary: barrack: 军营

**[16705.68s] English:** ill  
**Translation:** 

**[16706.14s] English:** lux  
**Translation:** 

**[16706.88s] English:** calvin  
**Translation:** 

**[16706.92s] English:** charcellzing  
**Translation:** Vocabulary: calvin: 卡尔文

**[16680.00s] English:** where the surface of computation is growing,  
**Translation:** 

**[16682.50s] English:** maybe growing exponentially,  
**Translation:** Vocabulary: computation: 计算; exponentially: 成倍地

**[16684.60s] English:** meaning the refrigerators start getting a GPU.  
**Translation:** 

**[16690.34s] English:** And just, first of all, the smartphones,  
**Translation:** 

**[16693.68s] English:** the billions of smartphones.  
**Translation:** 

**[16695.30s] English:** But maybe if there become highways  
**Translation:** 

**[16700.22s] English:** through which code can spread  
**Translation:** 

**[16702.38s] English:** across the entirety of the computation surface,  
**Translation:** Vocabulary: entirety: 整个部分

**[16705.46s] English:** then you don't any longer have to book AWS  
**Translation:** 

**[16709.42s] English:** GPUs.  
**Translation:** 

**[16712.38s] English:** There were real fundamental issues there.  
**Translation:** 

**[16714.08s] English:** When you start getting down to taking an actual problem  
**Translation:** 

**[16716.36s] English:** and putting it on an abstract machine like that,  
**Translation:** 

**[16718.80s] English:** that has not worked out well in practice.  
**Translation:** 

**[16722.48s] English:** And the idea that there was always,  
**Translation:** 

**[16725.26s] English:** like it's always been easy to come up with ways  
**Translation:** 

**[16727.14s] English:** to get compute faster,  
**Translation:** 

**[16728.90s] English:** say more flops or more giga ops or whatever there.  
**Translation:** Vocabulary: flops: 浮点运算

**[16732.40s] English:** That's usually the easy part.  
**Translation:** 

**[16733.98s] English:** But you then have interconnect  
**Translation:** 

**[16735.70s] English:** and then memory for what goes into it.  
**Translation:** 

**[16738.56s] English:** And when you talk about saying, well, cell phones,  
**Translation:** 

**[16741.34s] English:** well, you're limited to like a 5G connection  
**Translation:** 

**[16743.16s] English:** or something on that.  
**Translation:** 

**[16744.42s] English:** And if you say how,  
**Translation:** 

**[16746.44s] English:** if you take your calculation  
**Translation:** 

**[16748.24s] English:** and you factor it across a million cell phones  
**Translation:** 

**[16751.58s] English:** instead of a thousand GPUs in a warehouse,  
**Translation:** 

**[16754.96s] English:** you might be able to have some kind of a substrate like that,  
**Translation:** 

**[16758.02s] English:** but it could be operating then at one one thousandth the speed.  
**Translation:** Vocabulary: substrate: 基底

**[16762.30s] English:** And so, yes, you could have an AGI working there,  
**Translation:** 

**[16764.92s] English:** but it wouldn't be a real time AGI.  
**Translation:** 

**[16766.36s] English:** It would be something that is operating,  
**Translation:** 

**[16768.56s] English:** being at really a snail's pace,  
**Translation:** 

**[16770.64s] English:** you know, much, much slower than kind of human level thought for things.  
**Translation:** 

**[16774.32s] English:** So I'm not worried about that problem.  
**Translation:** 

**[16776.44s] English:** You're transferring the problem into the interconnect,  
**Translation:** 

**[16779.16s] English:** the communication, the shared memory,  
**Translation:** Vocabulary: interconnect: 网络连接; transferring: 转移

**[16781.76s] English:** the collective intelligence aspect of it,  
**Translation:** 

**[16784.20s] English:** which is extremely difficult as well.  
**Translation:** 

**[16786.00s] English:** Yeah, I mean, it's back to the very earliest days of supercomputers.  
**Translation:** 

**[16789.00s] English:** You still have the balance between bandwidth, storage and computation.  
**Translation:** Vocabulary: bandwidth: 带宽; supercomputers: 超级计算机

**[16793.80s] English:** And sometimes they're easier to get one or the other,  
**Translation:** 

**[16796.78s] English:** but it's been remarkably  
**Translation:** Vocabulary: remarkably: 非常

**[16798.38s] English:** constant across all those years.  
**Translation:** 

**[16800.00s] English:** that you still need all three.  
**Translation:** 

**[16803.50s] English:** What do your efforts now,  
**Translation:** 

**[16806.44s] English:** you mentioned to me that you're really committing  
**Translation:** 

**[16809.32s] English:** to AI at this stage.  
**Translation:** 

**[16811.34s] English:** What do you see your life  
**Translation:** 

**[16813.00s] English:** in the next few months, years look like?  
**Translation:** 

**[16815.50s] English:** What do you hope to achieve here?  
**Translation:** 

**[16818.26s] English:** So I literally just this week signed a term sheet  
**Translation:** 

**[16822.32s] English:** to take some investment money for my company  
**Translation:** 

**[16825.20s] English:** where the last two years I had backed off from Meta  
**Translation:** 

**[16829.30s] English:** and I was still doing my consulting CTO role there,  
**Translation:** 

**[16832.34s] English:** but I had styled it as I was going to take  
**Translation:** 

**[16835.12s] English:** the Victorian gentleman scientist route  
**Translation:** Vocabulary: victorian: 维多利亚时代的

**[16837.24s] English:** where I was going to be the wealthy person  
**Translation:** 

**[16840.60s] English:** that was going to go pursue science  
**Translation:** 

**[16842.40s] English:** and learn about this and do experiments.  
**Translation:** 

**[16844.98s] English:** And honestly, I'm surprised there aren't more people  
**Translation:** 

**[16847.34s] English:** like that, that are like me,  
**Translation:** 

**[16849.60s] English:** technical people that made a bunch of money  
**Translation:** 

**[16851.96s] English:** and are interested in some of these,  
**Translation:** 

**[16854.34s] English:** possibly the biggest leverage point in human history.  
**Translation:** Vocabulary: leverage: 杠杆作用

**[16857.38s] English:** I mean, I know of,  
**Translation:** 

**[16858.16s] English:** I've heard of a couple organizations  
**Translation:** 

**[16860.40s] English:** that are basically led by one rich techie guy  
**Translation:** 

**[16863.16s] English:** that gets a few people around him to try to work on this.  
**Translation:** Vocabulary: techie: 技术人员

**[16866.82s] English:** But I'm surprised that there's not more,  
**Translation:** 

**[16868.46s] English:** that there aren't like a dozen of them.  
**Translation:** 

**[16870.94s] English:** I mean, maybe people are still think  
**Translation:** 

**[16873.08s] English:** that it's an unapproachable problem,  
**Translation:** Vocabulary: unapproachable: 难以接近

**[16874.56s] English:** that it's kind of beyond their ability to get a wrench on  
**Translation:** 

**[16877.92s] English:** and have some effect on like whatever startups  
**Translation:** Vocabulary: startups: 创业公司; wrench: 扳手

**[16879.96s] English:** they've run before.  
**Translation:** 

**[16881.74s] English:** But that was my kind of,  
**Translation:** 

**[16884.36s] English:** like with all the stuff I've learned,  
**Translation:** 

**[16885.76s] English:** whether it's gaming, aerospace, whatever,  
**Translation:** Vocabulary: aerospace: 航空航天

**[16888.00s] English:** I go through a larval phase where I'm like,  
**Translation:** 

**[16890.70s] English:** okay, I'm sucking up all of this information,  
**Translation:** Vocabulary: larval: 幼虫阶段

**[16893.04s] English:** trying to see, is this something that I can actually do?  
**Translation:** 

**[16896.52s] English:** Is this something that's practical  
**Translation:** 

**[16898.24s] English:** to devote a large chunk of my life to?  
**Translation:** 

**[16901.22s] English:** And I've gone through that with the AI,  
**Translation:** 

**[16904.32s] English:** machine learning space of things.  
**Translation:** 

**[16906.36s] English:** And I think I've got my arms around it.  
**Translation:** 

**[16909.56s] English:** I've got the measure of it  
**Translation:** 

**[16910.78s] English:** where some of the most brilliant people in the world  
**Translation:** 

**[16913.12s] English:** are working on this problem,  
**Translation:** 

**[16914.42s] English:** but nobody knows exactly the path that it's going on.  
**Translation:** 

**[16918.00s] English:** We're throwing a lot of things at the wall.  
**Translation:** 

**[16920.00s] English:** and seeing what sticks i but i have a you know another interesting thing just learning about  
**Translation:** 

**[16925.86s] English:** all of this the the contingency of your path to knowledge and talking about the associations and  
**Translation:** 

**[16930.44s] English:** the context that you have with them where people that learn in the same path will have similar  
**Translation:** Vocabulary: contingency: 偶然性

**[16936.08s] English:** thought processes and i think it's useful that i come at this from a different background different  
**Translation:** 

**[16941.50s] English:** history than the people that have had the largely academic backgrounds for this where i have huge  
**Translation:** 

**[16947.24s] English:** blind spots that that they could easily point out but i have a different set of experiences in  
**Translation:** 

**[16953.04s] English:** history and approaches to problems and systems engineering that i'm you know that might turn  
**Translation:** 

**[16958.42s] English:** out to be useful and i can afford to take that bet where i'm not going to be destitute i am i was  
**Translation:** 

**[16965.04s] English:** you know i've been i have enough money to fund myself working on this for the rest of my life  
**Translation:** 

**[16969.38s] English:** but what i was finding is that i was i'm i was still not committing where i had a foot firmly  
**Translation:** 

**[16977.04s] English:** in the middle of the road and i was still not committing to it and i was still not committing  
**Translation:** 

**[16977.22s] English:** to it and i was still not committing to it and i was still not committing to it and i was still not committing  
**Translation:** 

**[16977.24s] English:** the vr and meta side of things where in theory i've got i've got a very nice position there i  
**Translation:** 

**[16982.70s] English:** only have to work one day a week for my my consulting role but but i was engaging every  
**Translation:** 

**[16988.22s] English:** day i'd still be like my computers there i'd be going and checking the workplace and notes and  
**Translation:** 

**[16992.40s] English:** testing different things and communicating with people but uh but i did make the the decision  
**Translation:** 

**[16998.60s] English:** recently that no i'm gonna get serious i'm still gonna keep my ties with meta but i am seriously  
**Translation:** 

**[17005.60s] English:** going for the agi  
**Translation:** 

**[17007.22s] English:** side of things and it's actually a really interesting point because a lot of it  
**Translation:** 

**[17011.16s] English:** the machine learning the ai community is quite large but really basically almost everybody has  
**Translation:** 

**[17018.12s] English:** taken the same trajectory through life uh in that community and it's so interesting to have somebody  
**Translation:** Vocabulary: trajectory: 人生轨迹

**[17024.14s] English:** like you which are with a fundamentally different trajectory and that's where the big solutions can  
**Translation:** 

**[17029.00s] English:** come because there's a kind of silo and it's it is a bunch of people kind of following the same  
**Translation:** Vocabulary: fundamentally: 根本上

**[17034.72s] English:** kind of set of ideas and i was really worried  
**Translation:** 

**[17037.20s] English:** that i didn't want to come off as  
**Translation:** 

**[17040.00s] English:** you know, like an arrogant outsider for things where I have all the respect in the world for  
**Translation:** 

**[17044.48s] English:** the work that's, you know, it's been a miracle decade. We're in the midst of a scientific  
**Translation:** Vocabulary: arrogant: 自以为是; outsider: 局外人

**[17048.30s] English:** revolution happening now. And everybody doing this is, you know, these are the Einsteins and  
**Translation:** 

**[17054.18s] English:** Bohrs and whatever's of our modern era. And I was really happy to see that the people that I've sat  
**Translation:** Vocabulary: einsteins: 大科学家

**[17060.54s] English:** down and talked with, everybody does seem to really be quite great about, just happy to talk  
**Translation:** 

**[17065.40s] English:** about things, willing to acknowledge that we don't know what we're doing. We're figuring it out as we  
**Translation:** 

**[17069.78s] English:** go along. And I mean, I've got a, you know, a huge debt on this where this all really started  
**Translation:** 

**[17076.16s] English:** for me because Sam Altman basically tried to recruit me to open AI. And it was at a point  
**Translation:** Vocabulary: altman: 萨姆·阿尔特曼

**[17081.42s] English:** when I didn't know anything about what was really going on in machine learning. And in fact, it's  
**Translation:** 

**[17087.36s] English:** funny how the first time you reached out to me, it's like four years ago for your AI podcast.  
**Translation:** 

**[17091.52s] English:** Yeah, for people, yeah, for people who are listening to this should know that,  
**Translation:** 

**[17099.46s] English:** unfortunately,  
**Translation:** 

**[17099.78s] English:** first of all, obviously, I've been a huge fan of yours for the longest time, but we've agreed to  
**Translation:** 

**[17104.32s] English:** talk like, yeah, like four years ago, back when this was called the Artificial Intelligence  
**Translation:** 

**[17108.62s] English:** Podcast. We wanted to do a thing and you said yes. And then I said, it's like, I don't know  
**Translation:** 

**[17114.10s] English:** anything about modern AI. That's right. I said, I could kind of take an angle on machine perception  
**Translation:** 

**[17118.50s] English:** because I'm doing a lot of that with the sensors and the virtual reality, but we could probably  
**Translation:** 

**[17123.20s] English:** find something to talk about. And that's where, when did Sam talk to you about open AI around the  
**Translation:** 

**[17129.42s] English:** same time?  
**Translation:** 

**[17129.96s] English:** No, it was a little bit, it was a bit after that. So I had done the most basic work. I had kind of  
**Translation:** 

**[17135.58s] English:** done the neural networks from scratch where I had gone and written it all in C just to make sure I  
**Translation:** 

**[17140.58s] English:** understood backpropagation at the lowest level and my nuts and bolts approach. But after Sam  
**Translation:** Vocabulary: backpropagation: 反向传播; neural: 神经

**[17147.00s] English:** approached me, I, you know, it was flattering to think that he thought that I could be useful at  
**Translation:** 

**[17152.80s] English:** open AI largely for kind of like systems optimization sorts of things. I am, you know,  
**Translation:** Vocabulary: flattering: 令人感到荣幸; optimization: 优化

**[17159.08s] English:** without being an expert.  
**Translation:** 

**[17160.00s] English:** But I asked Ilya Setskovor to give me a reading list. And he gave me a binder full of all the papers that like, okay, these are the important things. If you really read and understand all of these, you'll know like 80% of what most of the, you know, the machine language researchers work on.  
**Translation:** Vocabulary: setskovor: 塞特索夫

**[17177.50s] English:** And I went through and I read all those papers multiple times and highlighted them and went through and kind of figured the things out there and then started branching out into my own sets of research on things. And I actually started writing my own experiments and doing kind of figuring out, you know, finding out what I what I don't know what the limits of my knowledge are and starting to get some of my angles of attack on things, the things that I think are a little bit different from, from what people are doing.  
**Translation:** 

**[17204.72s] English:** And I've had a couple years now, like two years.  
**Translation:** Vocabulary: highlighted: 标注外文

**[17207.50s] English:** Since I kind of left the full time position at Meta. And now I've kind of pulled the trigger and said, I'm going to get serious about it. But some of my lessons all the way back to Armadillo Aerospace about how I know I need to be more committed to this where there is that it's both a freedom and a cost in some ways when you know that you're wealthy enough to say it's like this doesn't really mean anything I can, I can spend, you know, I can spend a million dollars a year for the rest of my life.  
**Translation:** 

**[17235.76s] English:** And it doesn't mean anything.  
**Translation:** Vocabulary: aerospace: 航天; armadillo: 装甲龙

**[17237.50s] English:** It's fine.  
**Translation:** 

**[17239.08s] English:** But that is an opportunity to just kind of meander.  
**Translation:** Vocabulary: meander: 漫步

**[17242.72s] English:** And I could see that in myself when I'm doing some things.  
**Translation:** 

**[17245.78s] English:** It's like, oh, this is a kind of interesting, curious thing.  
**Translation:** 

**[17248.46s] English:** Let's look at this for a little while.  
**Translation:** 

**[17249.96s] English:** Let's look at that.  
**Translation:** 

**[17251.00s] English:** It's not really bearing down on the problem.  
**Translation:** 

**[17253.92s] English:** So there's a few things that that I've done that are kind of tactics for myself to make me more effective.  
**Translation:** Vocabulary: tactics: 策略

**[17260.28s] English:** Like one thing I noticed I was not doing well is I had a Google Cloud account with to get GPUs there.  
**Translation:** 

**[17267.50s] English:** And I was finding I was very rarely doing that for no good psychological reasons where I'm like, oh, I can always think of something to do other than to spin up instances and run an experiment.  
**Translation:** 

**[17276.94s] English:** I can keep working on my local Titans or something.  
**Translation:** 

**[17280.00s] English:** But it was really stupid. I mean, it was not a lot of money. I should have been running more experiments there. So I thought to myself, well, I'm going to go buy a quarter million dollar DGX station. I'm going to just like sit it right there. And it's going to mock me if I'm not using it. If the fans aren't running on that thing, I'm not properly utilizing it. And that's been helpful.  
**Translation:** Vocabulary: titans: 巨型机; utilizing: 利用

**[17299.40s] English:** You know, I've done a lot more experiments since then. It's been interesting where I thought I'd be doing all this low level NVLink optimized stuff. But 90% of what I do is just spin up four instances of an experiment with different hyper parameters on it.  
**Translation:** 

**[17312.86s] English:** Oh, interesting. So you're doing like really sort of building up intuition by doing ML experiments of different kinds.  
**Translation:** Vocabulary: hyper: 超参数; intuition: 直觉; optimized: 优化

**[17320.26s] English:** But so the next big thing, though, is I am, you know, I decided that I was going to take some take some investor money because I had.  
**Translation:** 

**[17329.40s] English:** I have an overactive sense of responsibility about other people's money.  
**Translation:** 

**[17333.62s] English:** I am. And it's like I, I don't want I mean, a lot of my my push and my passionate entreaties for things that met are it's like I don't want Zuck to have wasted his money investing in Oculus.  
**Translation:** 

**[17344.78s] English:** I want it to work out. I want it to change the world. I want it to be worth all of this time, money and effort going into it.  
**Translation:** Vocabulary: entreaties: 恳求; oculus: Oculus头盔

**[17352.24s] English:** And I expect that it's going to be that like that with my with my company where it's a huge forcing function.  
**Translation:** 

**[17359.02s] English:** Yeah.  
**Translation:** 

**[17359.40s] English:** I have investment investors that are going to expect something of me.  
**Translation:** 

**[17363.38s] English:** Now, we've all had the conversation that this is a low probability long term bet.  
**Translation:** 

**[17368.28s] English:** It's not something that there's a million things I could do that I would have line of sight on the value proposition for.  
**Translation:** 

**[17374.02s] English:** This isn't that I think there are there are unknown unknowns in the way, but it's one of these things that it's, you know, it's hyper ball, but it's potentially one of the most important things humans ever do.  
**Translation:** 

**[17385.48s] English:** And it's something that I think is within our lifetimes, if not within a decade.  
**Translation:** 

**[17389.40s] English:** I'm to happen.  
**Translation:** Vocabulary: lifetimes: 一生之内

**[17391.66s] English:** So, yeah, this is just now happening like term sheet, like the ink is barely virtual inks, barely dry, drying.  
**Translation:** 

**[17398.78s] English:** I mean, as.  
**Translation:** 

**[17400.00s] English:** mentioned you offline like somebody i admire and um some of you know andre carpati i think the two  
**Translation:** 

**[17405.68s] English:** of you different trajectories in life but approach problems similarly in that he codes stuff from  
**Translation:** Vocabulary: andre: 安德烈; trajectories: 发展路径

**[17411.42s] English:** scratch up all the time and i he's created a bunch of little things outside of um even outside the  
**Translation:** 

**[17419.26s] English:** course at stanford that have been tremendously useful to build up intuition about stuff but also  
**Translation:** Vocabulary: stanford: 斯坦福大学; tremendously: 极其

**[17426.82s] English:** to help people and uh they're all in the realm of ai um do you see yourself potentially doing  
**Translation:** 

**[17433.36s] English:** things like this or built you know not necessarily solving a gigantic problem but on the journey on  
**Translation:** Vocabulary: gigantic: 巨大的

**[17438.70s] English:** the path to that building up intuitions uh and um uh sharing code or ideas or systems  
**Translation:** 

**[17448.34s] English:** that um give inklings of agi but also kind of are useful to people in some way so yeah first of all  
**Translation:** Vocabulary: inklings: 微弱迹象; intuitions: 直觉

**[17456.26s] English:** andre is  
**Translation:** 

**[17456.80s] English:** awesome i learned a lot when i was going through my larval phase from his blog posts and his  
**Translation:** Vocabulary: larval: 幼虫阶段

**[17461.20s] English:** stanford course and you know super valuable i got to meet him first a couple years ago when i was  
**Translation:** 

**[17466.56s] English:** first kind of starting off on my gentleman scientist bit and just uh just a couple months  
**Translation:** 

**[17473.18s] English:** ago when he went out on his sabbatical he stopped by in dallas and we talked for a while and i'm i  
**Translation:** 

**[17478.54s] English:** had a great time with him and then when i heard he actually left tesla i did of course along with  
**Translation:** Vocabulary: dallas: 达拉斯; sabbatical: 休假

**[17482.72s] English:** a hundred other people say hey if you ever want to work with me uh  
**Translation:** 

**[17486.62s] English:** you  
**Translation:** 

**[17486.80s] English:** would be an honor yeah so i'm he thinks that he's going to be doing this educational work but i think  
**Translation:** 

**[17491.86s] English:** someone's going to make him an offer he can't refuse i before he gets too far along on it oh  
**Translation:** 

**[17496.78s] English:** his current interest is educational so yeah um he's a special mind is there something you could  
**Translation:** 

**[17503.62s] English:** speak to what makes him so special so you understand he did he was very much a programmer's  
**Translation:** 

**[17510.10s] English:** programmer that was doing machine learning work rather than it's a different feel than an academic  
**Translation:** 

**[17515.80s] English:** where you can see it in a way that you can't see it in a way that you can't see it in a way that you  
**Translation:** 

**[17516.78s] English:** express corps sometimes where somebody that's really a mathematician  
**Translation:** 

**[17519.90s] English:** he's a realib  
**Translation:** Vocabulary: mathematician: 数学家

**[17537.94s] English:** as a mathematician  
**Translation:** 

**[17544.10s] English:** that's the answer  
**Translation:** 

**[17520.00s] English:** or a statistician at heart and they're they're doing something with machine learning but i you  
**Translation:** 

**[17525.16s] English:** know andre is about getting something done and you could see it in like all of his earliest  
**Translation:** Vocabulary: statistician: 统计学家

**[17529.26s] English:** approaches to it's like okay here's how reinforcement learning works here's how  
**Translation:** 

**[17533.12s] English:** recurrent neural networks work here's how transformers work here's how i am you know  
**Translation:** 

**[17537.88s] English:** crypto works and i am and yeah it's just he's a hacker's you know one of his old posts was like  
**Translation:** 

**[17544.70s] English:** a hacker's guide to machine learning yeah and you know he deprecated that and said don't really pay  
**Translation:** Vocabulary: crypto: 加密货币; deprecated: 废弃

**[17548.56s] English:** attention to what's in here but it's that thought that uh that carries through in a lot of it where  
**Translation:** 

**[17554.04s] English:** it is that back again to that hacker mentality and the hacker ethic with what he's doing and  
**Translation:** Vocabulary: hacker: 黑客

**[17559.00s] English:** in sharing all of it yeah and a lot of his approach to a new thing like like you said  
**Translation:** 

**[17564.44s] English:** larva stage is let me code up the simplest possible thing to build up intuition about it yeah like i  
**Translation:** Vocabulary: intuition: 直觉; larva: 幼虫

**[17570.82s] English:** say i i sketch with structs and things when i'm just thinking about a problem i'm thinking in  
**Translation:** 

**[17575.24s] English:** some degree of code  
**Translation:** 

**[17576.36s] English:** you are  
**Translation:** 

**[17578.56s] English:** also among many things a martial artist both judo and jiu-jitsu how has this helped make you the  
**Translation:** Vocabulary: martial: 武术

**[17585.48s] English:** person you are so i mean i was a competent club player in judo and grappling i mean i was you know  
**Translation:** 

**[17591.82s] English:** by no means any kind of a superstar but it was i went through a few phases with it where i did some  
**Translation:** Vocabulary: competent: 有能力; grappling: 摔跤

**[17598.08s] English:** i when i was quite young a little bit more when i was 17 i am and then i got into it kind of  
**Translation:** 

**[17605.08s] English:** seriously in my mid-30s and you know i went pretty far and i was a little bit more into it  
**Translation:** 

**[17608.56s] English:** and i was you know pretty good at some of the things that i was doing and i did appreciate it  
**Translation:** 

**[17614.06s] English:** quite a bit where i mean on the one hand it's always if you're going to do exercise or something  
**Translation:** 

**[17619.14s] English:** it's a more motivating form of exercise if someone is if someone is crushing you you are  
**Translation:** 

**[17623.84s] English:** like you're motivated to to do something about that to up your attributes and be better about  
**Translation:** Vocabulary: attributes: 身体素质; motivating: 激励的

**[17628.84s] English:** getting out of attributes yes but there's also that sense that i'm you know i was not i was not  
**Translation:** 

**[17636.40s] English:** a sports guy i did do wrestling in  
**Translation:** Vocabulary: wrestling: 摔跤

**[17638.56s] English:** in junior high and i  
**Translation:** 

**[17640.00s] English:** I think I would have been good for me if I'd carried that on into high school and had a little bit more of that. I mean, it's like I, you know, filch a little bit of wrestling vibe with what was going on about embracing the grind and like that push that I associate with the wrestling team that I, in hindsight, I wish I had gone through that and pushed myself that way.  
**Translation:** Vocabulary: embracing: 接纳; filch: 窃取; grind: 磨炼; hindsight: 事后诸葛

**[17661.42s] English:** But even getting back into judo and jujitsu in my mid-30s, as usually the old man on the mat with that, there was still the, you know, the sense that I, you know, working out with the group and having the guys that you're beating each other up with it, but you just feel good coming out of it.  
**Translation:** 

**[17681.80s] English:** And I can remember those driving home, aching in various ways and just thinking it's like, oh, that was that was really great.  
**Translation:** Vocabulary: jujitsu: 柔道

**[17689.62s] English:** And I, you know, it's mixing.  
**Translation:** 

**[17691.42s] English:** With a bunch of people that had nothing to do with any of the things that that I worked with, you know, every once in a while, some would be like, oh, you're the doom guy.  
**Translation:** 

**[17698.40s] English:** And I, but for the most part, it was just different slice of life.  
**Translation:** 

**[17702.54s] English:** I, you know, a good thing.  
**Translation:** 

**[17704.32s] English:** And I, I made the call when I was 40.  
**Translation:** 

**[17707.04s] English:** That's like, maybe I'm getting a little old for this.  
**Translation:** 

**[17709.06s] English:** I had, I had separated a rib and tweaked a few things and I got out without any really bad injuries.  
**Translation:** 

**[17715.50s] English:** And it was like, have I dodged enough bullets?  
**Translation:** Vocabulary: dodged: 避开; tweaked: 调整

**[17718.02s] English:** Should I, you know, should I hang it up?  
**Translation:** 

**[17719.76s] English:** I went back.  
**Translation:** 

**[17720.78s] English:** I've.  
**Translation:** 

**[17721.58s] English:** I've gone a couple of times in the last decade trying to get my kids into it a little bit.  
**Translation:** 

**[17726.00s] English:** I didn't really stick with any of them, but it was fun to get back on the mats.  
**Translation:** 

**[17730.08s] English:** I really hurts for a while when you haven't gone.  
**Translation:** 

**[17732.68s] English:** I gone for a while, but I still debate this pretty constantly.  
**Translation:** 

**[17737.58s] English:** My brother's only a year younger than me and he's going kind of hard in jujitsu right now.  
**Translation:** 

**[17742.02s] English:** And I, you know, he was just, he won a few medals at the last tournament he was at.  
**Translation:** 

**[17746.26s] English:** He's competing.  
**Translation:** 

**[17747.08s] English:** Yeah.  
**Translation:** 

**[17747.26s] English:** And I was thinking, yeah, I guess we're in the executive division.  
**Translation:** 

**[17750.34s] English:** If you're over 50.  
**Translation:** 

**[17751.42s] English:** You know, we're over 45 or something.  
**Translation:** 

**[17753.90s] English:** And it's not out of the question that I go back at some point to do some of this.  
**Translation:** 

**[17758.88s] English:** But again, I'm just.  
**Translation:** 

**[17760.00s] English:** reorganizing my life around more focus probably not going to happen i'm pushing my exercise around  
**Translation:** 

**[17766.84s] English:** to give me longer uninterrupted intellectual focus time pushing it to the beginning or the  
**Translation:** Vocabulary: reorganizing: 重新整理; uninterrupted: 不间断

**[17771.38s] English:** end of running and stuff like that walking yeah yeah running and calisthenics and some things  
**Translation:** 

**[17776.78s] English:** like that but it allows you to still think about a problem but if you're going to a judo club or  
**Translation:** Vocabulary: calisthenics: 体操

**[17781.68s] English:** something you're you've got it fixed it's going to be seven o'clock or whatever ten o'clock on  
**Translation:** 

**[17785.64s] English:** saturday i although i talked about this a little bit when i was on rogan and shortly after that  
**Translation:** 

**[17791.18s] English:** carlos machado did reach out and i had trained with him for years i back in the day and he was  
**Translation:** 

**[17796.78s] English:** like hey we've got kind of a small private club with a bunch of uh kind of executive type people  
**Translation:** 

**[17801.46s] English:** and uh it gets it does tempt me yeah i don't know if you know him but john donahue moved  
**Translation:** 

**[17808.42s] English:** here to austin uh with gordon ryan and a few other folks and he has a very interesting way  
**Translation:** Vocabulary: donahue: 唐纳休

**[17815.02s] English:** very  
**Translation:** 

**[17815.60s] English:** very  
**Translation:** 

**[17815.62s] English:** very  
**Translation:** 

**[17815.64s] English:** deep systematic way of thinking about jiu-jitsu that reveals the the chess of it the the the  
**Translation:** 

**[17823.52s] English:** like the the science of it and i do think about that more as kind of an older person considering  
**Translation:** 

**[17830.20s] English:** the martial arts where i can remember the the very earliest days getting back into judo and i'm like  
**Translation:** 

**[17835.02s] English:** teach me submissions right now you know it's like learn the arm bar learn the choke i but as you get  
**Translation:** 

**[17840.94s] English:** older you start thinking more about it's like okay i really do want to like learn the entire canon of  
**Translation:** 

**[17845.62s] English:** judo it's like are all the different things there and like all the different approaches for it  
**Translation:** 

**[17850.02s] English:** not just the you know if you want to compete there's just a handful of things you learn really  
**Translation:** 

**[17853.96s] English:** really well but sometimes there's interest in learning a little bit more of the scope there and  
**Translation:** 

**[17858.50s] English:** figuring some things out from you know at one point i had wasn't exactly a spreadsheet but i  
**Translation:** Vocabulary: spreadsheet: 电子表格

**[17863.86s] English:** did have a you know a big long text file with like here's the things that i learned and here  
**Translation:** 

**[17868.00s] English:** like ways you chain this together and while when i went back a few years ago it was good to see  
**Translation:** 

**[17874.54s] English:** that i whipped myself up and i was like oh my god i'm not gonna be able to do this again i'm not  
**Translation:** 

**[17875.60s] English:** back into reasonable shape about doing the basic grappling but i know there was a ton of the  
**Translation:** Vocabulary: grappling: 摔跤

**[17880.00s] English:** subtleties that were just that were gone but could probably be brought back reasonably quickly  
**Translation:** 

**[17884.68s] English:** and there's also the benefit i mean you're exceptionally successful now um you're brilliant  
**Translation:** Vocabulary: exceptionally: 特别; reasonably: 合理地; subtleties: 细微之处

**[17892.16s] English:** and the problem the old problem of the ego yeah is uh i still pushed kind of harder than i should  
**Translation:** 

**[17899.98s] English:** i mean that was i was one of those people that i yeah i'm i'm on the smaller side for uh for a lot  
**Translation:** 

**[17905.62s] English:** of the people competing and i would you know i'd go with all the big guys and i'd go hard and i'd  
**Translation:** 

**[17910.88s] English:** push myself a lot and that would be one of those where i would i you know i i'd be dangerous to  
**Translation:** 

**[17917.26s] English:** anyone for first five minutes but then sometimes after that i'm already dead and i knew it was  
**Translation:** 

**[17921.80s] English:** terrible for me because it it made the you know it meant i got less training time with all of that  
**Translation:** 

**[17926.92s] English:** when you go and you just gas out you know relatively quickly there and i like to think  
**Translation:** 

**[17931.72s] English:** that i would be better about that where after i gave up judo i  
**Translation:** 

**[17935.62s] English:** started doing the half marathons and tough butters and things like that and so when i did  
**Translation:** 

**[17939.92s] English:** go back to the the local judo kai club i thought it's like oh i should have better cardio for this  
**Translation:** Vocabulary: marathons: 长跑比赛

**[17944.74s] English:** because i'm i'm a runner now and i do all of this and didn't work out that way it was the same old  
**Translation:** 

**[17949.40s] English:** thing where just push really hard strain really hard and and of course when i worked with good  
**Translation:** 

**[17954.80s] English:** guys like carlos it's like he just the whole flow like water thing is real and he's just like  
**Translation:** 

**[17960.14s] English:** that's true with judo too some of the best people like i've trained with olympic gold medalists and  
**Translation:** Vocabulary: carlos: 卡尔洛斯

**[17965.62s] English:** for some reason with them everything's easier everything is you actually start to feel  
**Translation:** 

**[17972.36s] English:** the science of it the music of it the dance of it that's everything is effortless um you understand  
**Translation:** 

**[17980.32s] English:** that there's an art to it it's not just an exercise it was interesting where i did go to  
**Translation:** 

**[17985.22s] English:** the kodokan in japan i kind of the birthplace of judo and everything and i remember i rolled with  
**Translation:** Vocabulary: birthplace: 诞生地

**[17990.60s] English:** one old guy i didn't you know didn't start standing just started on groundwork nirwaza  
**Translation:** 

**[17995.62s] English:** and it was striking how different it was from carlos he was still he was better than me and  
**Translation:** Vocabulary: groundwork: 基础训练

**[18000.00s] English:** He got my arm and I, you know, I had to tap there, but it was a completely different style  
**Translation:** 

**[18004.82s] English:** where I just felt like I could do nothing.  
**Translation:** 

**[18006.94s] English:** He was just enveloping me and just like slowly ground it down, took my arm and bent it.  
**Translation:** 

**[18011.38s] English:** While with Carlos, you know, he's just loose and free.  
**Translation:** Vocabulary: enveloping: 包围

**[18014.56s] English:** And you always thought like, oh, you're just going to go grab something, but you never  
**Translation:** 

**[18017.42s] English:** had any chance to do it.  
**Translation:** 

**[18018.54s] English:** But it was a very different feeling.  
**Translation:** 

**[18019.94s] English:** That's a good summary of the difference between jujitsu and judo.  
**Translation:** Vocabulary: jujitsu: 柔术

**[18023.28s] English:** In jujitsu, there's, it is a dance and you feel like there's a freedom.  
**Translation:** 

**[18026.32s] English:** And actually, anybody, like Gordon Ryan, one of the best, the best grappler in the  
**Translation:** Vocabulary: grappler: 摔跤手

**[18033.74s] English:** world, no-gi grappler in the world.  
**Translation:** 

**[18035.70s] English:** There's a feeling like you can do anything.  
**Translation:** 

**[18038.34s] English:** But when you actually try to do something, you can't.  
**Translation:** 

**[18041.58s] English:** Just magically doesn't work.  
**Translation:** 

**[18042.88s] English:** But with the best judo players in the world, yeah, it does feel like there's a blanket  
**Translation:** 

**[18047.94s] English:** that weighs a thousand pounds on top of you.  
**Translation:** 

**[18050.16s] English:** And there's not a feeling like you can do anything.  
**Translation:** 

**[18053.30s] English:** You just, you're trapped.  
**Translation:** 

**[18054.62s] English:** And that's a style.  
**Translation:** 

**[18056.32s] English:** That's a difference in the style of martial arts.  
**Translation:** Vocabulary: martial: 武术

**[18059.04s] English:** But it's also, once you start to study, you understand it all has to do with human movement  
**Translation:** 

**[18064.32s] English:** and the physics of it and the leverage and all that kind of stuff.  
**Translation:** Vocabulary: leverage: 杠杆作用

**[18067.08s] English:** And that's like, that's super fascinating.  
**Translation:** 

**[18069.38s] English:** At the end of the day, for me, the biggest benefit is in the humbling aspect.  
**Translation:** Vocabulary: humbling: 使人谦卑

**[18073.62s] English:** When another human being kind of tells you that, you know, there's a hierarchy or there's  
**Translation:** 

**[18081.26s] English:** a, you're not that special.  
**Translation:** Vocabulary: hierarchy: 等级制度

**[18085.12s] English:** Yeah.  
**Translation:** 

**[18085.44s] English:** And in the most extreme case, when you tap to a choke, you are basically living because  
**Translation:** 

**[18090.64s] English:** somebody lets you live.  
**Translation:** 

**[18092.28s] English:** And that's, that is one of those, if you think about it, that is a closer brush with mortality  
**Translation:** 

**[18096.28s] English:** than, than most people consider.  
**Translation:** 

**[18100.46s] English:** And that kind of humbling act is good to take to your work then where it's harder to get  
**Translation:** 

**[18107.04s] English:** humbled, you know?  
**Translation:** 

**[18108.90s] English:** Yeah.  
**Translation:** 

**[18109.14s] English:** Because nobody's, nobody that does any martial art is coming out thinking I'm the best in  
**Translation:** 

**[18112.94s] English:** the world at anything.  
**Translation:** 

**[18114.28s] English:** Yeah.  
**Translation:** 

**[18114.72s] English:** Yeah.  
**Translation:** 

**[18114.74s] English:** Yeah.  
**Translation:** 

**[18114.80s] English:** Yeah.  
**Translation:** 

**[18114.82s] English:** Yeah.  
**Translation:** 

**[18114.84s] English:** Yeah.  
**Translation:** 

**[18114.86s] English:** Yeah.  
**Translation:** 

**[18114.88s] English:** Yeah.  
**Translation:** 

**[18114.90s] English:** Yeah.  
**Translation:** 

**[18114.92s] English:** Yeah.  
**Translation:** 

**[18115.44s] English:** Yeah.  
**Translation:** 

**[18115.54s] English:** Everybody loses.  
**Translation:** 

**[18116.96s] English:** Let me ask you for advice.  
**Translation:** 

**[18119.80s] English:** What advice would you give to someone who's like, oh, I'm a good person.  
**Translation:** 

**[18120.04s] English:** I'm a good person.  
**Translation:** 

**[18120.10s] English:** I'm a good person.  
**Translation:** 

**[18120.16s] English:** I'm a good person.  
**Translation:** 

**[18120.18s] English:** I'm a good person.  
**Translation:** 

**[18120.24s] English:** I'm a good person.  
**Translation:** 

**[18120.00s] English:** advice would you give to young people today uh about life about career how they can have a job  
**Translation:** 

**[18127.20s] English:** how they can have an impact how they can have a life they can be proud of so it was kind of fun  
**Translation:** 

**[18134.08s] English:** i got invited to give the commencement speech back at the i went to college for two semesters  
**Translation:** 

**[18139.66s] English:** and and dropped out and went on to do my tech stuff i but they still wanted me to come back  
**Translation:** 

**[18144.94s] English:** give a commencement speech and i i've got that pinned on my twitter account i still feel good  
**Translation:** 

**[18150.06s] English:** about everything that i said there and you know my my biggest point was that the path for me might  
**Translation:** 

**[18157.14s] English:** not be the path for everyone and in fact the advice the path that i took and even the advice  
**Translation:** 

**[18162.42s] English:** that i would give based on my experience and learnings probably isn't the best advice for  
**Translation:** 

**[18168.00s] English:** everyone because what i did was all about this knowledge in depth it was about not just having  
**Translation:** Vocabulary: learnings: 学习心得

**[18174.46s] English:** this  
**Translation:** 

**[18174.78s] English:** you know  
**Translation:** 

**[18174.92s] English:** this  
**Translation:** 

**[18174.94s] English:** surface level ability to make things do what i want but to really understand them through and  
**Translation:** 

**[18179.54s] English:** through to let me do the systems engineering work and to sometimes find these inefficiencies that can  
**Translation:** 

**[18185.40s] English:** be bypassed and and that the whole world doesn't need that you know most programmers don't your  
**Translation:** Vocabulary: bypassed: 绕过; inefficiencies: 低效; programmers: 程序员

**[18191.52s] English:** engineers of any kind don't necessarily need to do that they need to do a little job that's been  
**Translation:** 

**[18196.30s] English:** parceled out to them i be reliable let people depend on you do quality work with all of that  
**Translation:** Vocabulary: parceled: 分配

**[18202.34s] English:** but people that do have the ability to do that don't necessarily need to do that they need to  
**Translation:** 

**[18204.92s] English:** have an inclination for wanting to to know know things deeper and learn things deeper i'm you know  
**Translation:** Vocabulary: inclination: 兴趣

**[18211.46s] English:** the there are just layers and layers of things out there and it it's amazing it's if you're the right  
**Translation:** 

**[18217.30s] English:** person that is excited about that i the world's never been like this before it's better than ever  
**Translation:** 

**[18223.70s] English:** i mean everything that was wonderful for me is still there and there's whole new worlds to  
**Translation:** 

**[18228.68s] English:** explore on the different things that you can do and that i am you know it's hard work  
**Translation:** 

**[18234.90s] English:** embrace the grind with it and understand as much as you can and then  
**Translation:** 

**[18240.00s] English:** be prepared for opportunities to present themselves where you can't just say, this is my  
**Translation:** Vocabulary: grind: 辛苦工作

**[18245.64s] English:** goal in life and just push at that. I mean, you might be able to do that, but you're going to  
**Translation:** 

**[18249.90s] English:** make more total progress if you say, I'm preparing myself with this broad set of tools. And then I'm  
**Translation:** 

**[18256.28s] English:** being aware of all the way things are changing as I move through the world and as the whole world  
**Translation:** 

**[18261.22s] English:** changes around me, and then looking for opportunities to deploy the tools that you've  
**Translation:** Vocabulary: deploy: 部署

**[18265.66s] English:** built. And there's going to be more and more of those types of things there where an awareness of  
**Translation:** 

**[18272.10s] English:** what's happening, where the inefficiencies are, what things can be done, what's possible versus  
**Translation:** 

**[18277.28s] English:** what's current practice, and then finding those areas where you can go and make an adjustment  
**Translation:** 

**[18282.72s] English:** and make something that may affect millions or billions of people in the world, make it better.  
**Translation:** Vocabulary: adjustment: 调整

**[18289.54s] English:** When, maybe from your own example, how were you able to recognize this about yourself,  
**Translation:** 

**[18294.06s] English:** that you saw the layers?  
**Translation:** 

**[18295.92s] English:** In a particular thing, and you were drawn to discovering deeper and deeper truths about it?  
**Translation:** 

**[18301.68s] English:** Is that something that was obvious to you that you couldn't help? Or is there some  
**Translation:** 

**[18305.28s] English:** actions you had to take to actually allow yourself to dig deep?  
**Translation:** 

**[18308.96s] English:** So in the earliest days of personal computers, I remember the reference manuals, and the very  
**Translation:** 

**[18314.06s] English:** early ones even had schematics of computers in the background, in the back of the books,  
**Translation:** 

**[18319.72s] English:** as well as firmware listings and things. And I could look at that. And at that time,  
**Translation:** Vocabulary: firmware: 固件; schematics: 电路图

**[18324.18s] English:** when I was a younger teenager,  
**Translation:** 

**[18325.66s] English:** I didn't understand a lot of that stuff, how the different things worked. I was pulling out  
**Translation:** 

**[18331.24s] English:** the information that I could get, but I always wanted to know all of that. There was like kind  
**Translation:** 

**[18335.80s] English:** of magical information sitting down there. It's like the elder lore that some gray-beard wizard  
**Translation:** 

**[18341.06s] English:** is the keeper of. And so I always felt that pull for wanting to know more, wanting to explore the  
**Translation:** 

**[18348.40s] English:** mysterious areas there. And that followed right in through all the things that  
**Translation:** 

**[18354.72s] English:** got the value.  
**Translation:** 

**[18355.66s] English:** Exploring the video cards leading to the, you know, the scrolling advantages.  
**Translation:** Vocabulary: scrolling: 滚动

**[18360.00s] English:** you know exploring some of the academic papers and things learning about bsp trees and the  
**Translation:** 

**[18364.84s] English:** different things that that i could do i'm you know with those systems and just that the huge  
**Translation:** 

**[18370.48s] English:** larval phases going through aerospace just reading bookshelves full of books i mean again that point  
**Translation:** 

**[18376.20s] English:** where i have enough money i can buy all the books i want it was it was so valuable there where i was  
**Translation:** Vocabulary: aerospace: 航天领域; larval: 幼虫阶段

**[18382.22s] English:** terrible with my money when i was a kid my mom thought i would always be broke because you know  
**Translation:** 

**[18386.12s] English:** i'd buy my comic books and just be out of money but it was like all the pizza i want all the diet  
**Translation:** 

**[18391.38s] English:** coke i want video games and then books books and it didn't take that much as soon as i was making  
**Translation:** 

**[18397.10s] English:** 27k a year i i felt rich and i was just getting all the things that that i wanted but that sense  
**Translation:** 

**[18403.54s] English:** of you know that books have always been magical to me and that was one of the things that really  
**Translation:** 

**[18407.38s] English:** made me smile is uh andre had said he found you know when he came over to my house he said he  
**Translation:** Vocabulary: andre: 安德烈

**[18411.84s] English:** found my library inspiring just that i have and it was great to see you know i still look  
**Translation:** 

**[18416.10s] English:** at him he's kind of a younger guy i sometimes wonder if younger people these days have the  
**Translation:** 

**[18420.38s] English:** same relationship with books that i do where they were such a cornerstone for me in so many ways  
**Translation:** 

**[18425.56s] English:** but that sense that yeah i always wanted to know it all i know i can't and that was like one of  
**Translation:** Vocabulary: cornerstone: 基石

**[18430.44s] English:** the last things i said you can't know everything but you should convince yourself that you can know  
**Translation:** 

**[18434.72s] English:** anything you know any one particular thing it was created and discovered by humans you can learn it  
**Translation:** 

**[18440.78s] English:** you can find out what you need on there and you can learn it deeply yeah you can drive a nail  
**Translation:** 

**[18446.08s] English:** down through whatever layer cake problem space you've got and learn a cross-section there and  
**Translation:** 

**[18452.10s] English:** not only can you have an impact doing that you can just you can attain happiness doing that  
**Translation:** 

**[18457.60s] English:** there's something so fulfilling about becoming a craftsman of a thing yeah and i don't want to  
**Translation:** Vocabulary: craftsman: 手工艺人; fulfilling: 令人满足

**[18461.96s] English:** tell people that look this is a a good career move just you know grit your teeth and you know  
**Translation:** 

**[18466.76s] English:** and bear it i you know you want people you want and i do think it is possible sometimes to find  
**Translation:** 

**[18472.78s] English:** the joy in something like it might not immediately appeal to you  
**Translation:** 

**[18476.08s] English:** but i had told people early on like in in software times  
**Translation:** 

**[18480.00s] English:** that I, you know, a lot of game developers are in it just because they are so passionate about  
**Translation:** 

**[18485.30s] English:** games. But I was always really more flexible in what appealed to me where I said, I think I could  
**Translation:** Vocabulary: appealed: 吸引我

**[18492.16s] English:** be quite engaged doing operating system work or even database work. I would find the interest in  
**Translation:** 

**[18498.64s] English:** that because I think most things that are significant in the world have a lot of layers  
**Translation:** 

**[18503.62s] English:** and complexity to them and a lot of opportunities hidden within them. So that would probably be the  
**Translation:** 

**[18509.50s] English:** most important thing to encourage to people is that you can like weaponize curiosity. You can  
**Translation:** Vocabulary: complexity: 复杂性; weaponize: 利用

**[18515.70s] English:** deploy your curiosity to find, to kind of like make things useful and valuable to you, even if  
**Translation:** 

**[18521.72s] English:** they don't immediately appear that way. Deploy your curiosity. Yeah, that's very true. We've  
**Translation:** Vocabulary: deploy: 部署

**[18527.52s] English:** mentioned this debate point, whether mortality or fear of mortality is fundamental to creating an  
**Translation:** 

**[18534.28s] English:** AGI, but let's talk about whether it's fundamental to human beings. Do you think  
**Translation:** 

**[18539.34s] English:** about that? Do you think about that? Do you think about that? Do you think about that?  
**Translation:** 

**[18539.48s] English:** Do you think about your own mortality? I really don't. And you probably always have to like take  
**Translation:** 

**[18545.96s] English:** with a grain of salt anything somebody says about fundamental things like that. But I don't think  
**Translation:** 

**[18552.20s] English:** about really aging, impending death, legacy with my children, things like that. And clearly it  
**Translation:** 

**[18560.90s] English:** seems most of the world does a lot, a lot more than I do. So I mean, I think I'm an outlier in  
**Translation:** 

**[18567.42s] English:** that where it's...  
**Translation:** 

**[18569.32s] English:** Yeah, it doesn't wind up being a real part of my thinking and motivation about things.  
**Translation:** 

**[18575.78s] English:** So daily existence is about sort of the people you love and the problems before you.  
**Translation:** 

**[18583.38s] English:** I'm very much focused on what I'm working on right now. I do take that back. There's one  
**Translation:** 

**[18589.30s] English:** aspect where the kind of finiteness of the life does impact me. And that is about thinking about  
**Translation:** Vocabulary: finiteness: 有限性

**[18595.50s] English:** the scope of the problems that I'm working on. When I, you know, when I decide...  
**Translation:** 

**[18599.16s] English:** Decided to work on.  
**Translation:** 

**[18600.00s] English:** When I was like nuclear fission or AGI, these are big ticket things that are impact large  
**Translation:** 

**[18607.20s] English:** fractions of the world.  
**Translation:** Vocabulary: fission: 核裂变; fractions: 部分

**[18608.72s] English:** And I was thinking to myself at some level that, okay, I mean, I may have a couple more  
**Translation:** 

**[18613.78s] English:** swings at bat with me at full capability, but yes, my mental abilities will decay with  
**Translation:** Vocabulary: capability: 能力

**[18621.14s] English:** age, you know, mostly inevitably.  
**Translation:** 

**[18623.26s] English:** I don't think it's a 0% chance that we will address some of that before it becomes a problem  
**Translation:** Vocabulary: inevitably: 必然地

**[18627.94s] English:** for me.  
**Translation:** 

**[18628.40s] English:** I think exciting medical stuff in the next couple of decades, but I do have this kind  
**Translation:** 

**[18633.14s] English:** of vague plan that when I'm not at the top of my game and I don't feel that I'm, you  
**Translation:** 

**[18637.72s] English:** know, in a position to put a dent in the world some way that I'll probably wind up doing  
**Translation:** 

**[18641.90s] English:** some kind of recreational retro programming or I'll, you know, I'll, I'll work on some,  
**Translation:** 

**[18647.06s] English:** I, you know, something that I would not devote my life to now, but I can while away my time  
**Translation:** Vocabulary: recreational: 休闲; retro: 怀旧

**[18652.06s] English:** as the old man gardening in the code worlds.  
**Translation:** 

**[18656.10s] English:** And then to step back even.  
**Translation:** 

**[18658.40s] English:** Uh, bigger, let me ask you about why we're here.  
**Translation:** 

**[18661.90s] English:** We human beings, what's the meaning of it all?  
**Translation:** 

**[18664.78s] English:** What's the meaning of life?  
**Translation:** 

**[18666.06s] English:** John Carmack.  
**Translation:** 

**[18667.06s] English:** So very similar with that last question.  
**Translation:** 

**[18668.86s] English:** I know a lot of people fret about this question a lot, and I just really don't, I really don't  
**Translation:** 

**[18675.04s] English:** give a damn.  
**Translation:** 

**[18675.74s] English:** We are, I, you know, we are biological creatures that happenstance of evolution.  
**Translation:** Vocabulary: happenstance: 偶然性

**[18680.54s] English:** I, you know, we have innate drives that evolution crafted for survival and passing on of genetic  
**Translation:** 

**[18686.96s] English:** codes.  
**Translation:** 

**[18687.64s] English:** I am.  
**Translation:** 

**[18688.60s] English:** I don't, I don't find a lot of value in trying to go much deeper than that.  
**Translation:** 

**[18693.98s] English:** I, I have my motivations, some of which are, you know, some of which are probably genetically  
**Translation:** 

**[18698.18s] English:** coded and many of which are contingent on my upbringing and the path that I've had through  
**Translation:** Vocabulary: contingent: 依赖于; motivations: 动机; upbringing: 养育方式

**[18702.68s] English:** my life.  
**Translation:** 

**[18703.76s] English:** I, I don't run into like spates of depression or Enwe or anything that, uh, that winds up  
**Translation:** Vocabulary: spates: 连续时段

**[18710.84s] English:** being a challenge and forcing a degree of soul searching with things like that.  
**Translation:** 

**[18715.18s] English:** I seem to be okay.  
**Translation:** 

**[18716.74s] English:** I, you know, kind of.  
**Translation:** 

**[18718.40s] English:** Without that.  
**Translation:** 

**[18719.60s] English:** Uh.  
**Translation:** 

**[18720.00s] English:** um as a brilliant ant in the ant colony without looking up to the sky wondering why the hell am  
**Translation:** 

**[18725.86s] English:** i here again yeah so the the why of it the incredible mystery of the fact that we started  
**Translation:** 

**[18734.98s] English:** first of all the origin of life on earth and from that from single cell organisms the entirety of  
**Translation:** Vocabulary: entirety: 全部

**[18741.62s] English:** the evolutionary process took us somehow to this incredibly intelligent thing that is able to  
**Translation:** 

**[18746.80s] English:** build wolfenstein 3d and doom and quake and uh take a crack at the problem of agi and create  
**Translation:** Vocabulary: evolutionary: 进化; wolfenstein: 狼穴

**[18754.12s] English:** things that eventually supersede human beings that doesn't the why of it is um it's been my  
**Translation:** 

**[18763.14s] English:** experience that people that focus on that don't focus on the here and now right in front of them  
**Translation:** Vocabulary: supersede: 取代

**[18769.44s] English:** tend to be less effective i mean it's not 100 you know vision matters to some people but  
**Translation:** 

**[18776.80s] English:** doesn't seem to be a necessary motivator for me and i think that the process of getting there  
**Translation:** Vocabulary: motivator: 激励因素

**[18782.08s] English:** is usually done again it's like the magic of gradient descent people just don't believe that  
**Translation:** 

**[18787.06s] English:** just looking locally gets you to all of these spectacular things that's been you know the  
**Translation:** Vocabulary: gradient: 梯度下降

**[18792.38s] English:** decades of looking at i am really some of the smartest people in the world that would just push  
**Translation:** 

**[18798.44s] English:** back forever against this idea that it's not this grand sophisticated vision of everything but  
**Translation:** Vocabulary: sophisticated: 精巧复杂的

**[18804.44s] English:** little tiny steps local information  
**Translation:** 

**[18806.80s] English:** winds up leading to all the best answers so the meaning of life is uh following locally  
**Translation:** 

**[18813.92s] English:** wherever the gradient descent takes you um this was an incredible conversation officially the  
**Translation:** 

**[18819.88s] English:** longest conversation i've ever done on the podcast uh which means a lot to me because i get to do it  
**Translation:** 

**[18825.86s] English:** with one of my heroes john i can't tell you how much it means to me that you would sit down with  
**Translation:** 

**[18829.84s] English:** me you're an incredible human being um i can't wait what you do next but you've already changed  
**Translation:** 

**[18835.38s] English:** the world you're an inspiration  
**Translation:** 

**[18836.80s] English:** to so many people and again we haven't covered  
**Translation:** 

**[18840.00s] English:** like most of what I was planning to talk about.  
**Translation:** 

**[18843.28s] English:** So I hope we get a chance to talk someday in the future.  
**Translation:** 

**[18846.54s] English:** And I can't wait to see what you do next.  
**Translation:** 

**[18848.46s] English:** Thank you so much again for talking to me.  
**Translation:** 

**[18850.32s] English:** Thank you very much.  
**Translation:** 

**[18851.88s] English:** Thanks for listening to this conversation with John Carmack.  
**Translation:** 

**[18854.60s] English:** To support this podcast,  
**Translation:** 

**[18856.10s] English:** please check out our sponsors in the description.  
**Translation:** Vocabulary: sponsors: 赞助商

**[18858.72s] English:** And now let me leave you with some words  
**Translation:** 

**[18860.62s] English:** from John Carmack himself.  
**Translation:** 

**[18863.50s] English:** Focused hard work is the real key to success.  
**Translation:** 

**[18866.72s] English:** Keep your eyes on the goal  
**Translation:** 

**[18868.42s] English:** and just keep taking the next step towards completing it.  
**Translation:** 

**[18872.04s] English:** If you aren't sure which way to do something,  
**Translation:** 

**[18874.62s] English:** do it both ways and see which works better.  
**Translation:** 

**[18878.34s] English:** Thank you for listening and hope to see you next time.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
