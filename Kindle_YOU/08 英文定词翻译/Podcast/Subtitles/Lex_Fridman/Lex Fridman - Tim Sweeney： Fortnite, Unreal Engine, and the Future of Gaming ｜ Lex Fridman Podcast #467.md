# Podcast vocabulary notes
Source file: Lex Fridman - Tim Sweeney： Fortnite, Unreal Engine, and the Future of Gaming ｜ Lex Fridman Podcast #467.opus

**[0.00s] English:** Humans are by far the hardest part of computer graphics because millions of years of evolution  
**Translation:** 

**[5.62s] English:** have given us dedicated brain systems to detect patterns and faces and infer emotions and intent  
**Translation:** 

**[12.24s] English:** because cavemen had to, when they see a stranger, determine whether they were likely friendly or  
**Translation:** 

**[17.26s] English:** they might be trying to kill them. And so people in the world have extraordinarily detailed  
**Translation:** Vocabulary: cavemen: 穴居人; extraordinarily: 非常

**[22.76s] English:** expectations of a face, and we can notice imperfections, especially perfections arising  
**Translation:** 

**[27.74s] English:** from computer graphics limitations. Okay, one part is capturing humans, and so we've got really  
**Translation:** 

**[33.18s] English:** advanced, dedicated hardware that puts a human in a capture sphere with dozens of cameras and  
**Translation:** 

**[39.70s] English:** them taking high-resolution, high-frame-rate video of them as they go through a range of motions.  
**Translation:** 

**[44.90s] English:** And then capturing the human face is complicated because the nuanced detail of our faces and how  
**Translation:** 

**[49.10s] English:** all the muscles and sinews and fat work together to give us different expressions. So it's not only  
**Translation:** Vocabulary: nuanced: 细腻; sinews: 肌腱

**[54.12s] English:** about the shape of a person's face, but it's also about the entire range of motion that they're  
**Translation:** 

**[57.72s] English:** going to go through. So that's the data problem. There's a lot of other problems of computer  
**Translation:** 

**[61.76s] English:** graphics. There's technology for rendering hair, which is really hard because you can't render  
**Translation:** 

**[66.20s] English:** every... Again, we know the laws of physics. It would be easy to just render every hair. It would  
**Translation:** Vocabulary: render: 渲染

**[69.90s] English:** just be a billion times too slow. So you need approximations that capture the net effect of hair  
**Translation:** 

**[75.34s] English:** on rendering and on pixels without calculating every single interaction of every light with  
**Translation:** Vocabulary: approximations: 近似值; pixels: 像素

**[81.12s] English:** every strand of hair. That's one part of it. There's detailed features for different parts  
**Translation:** 

**[85.68s] English:** of faces. There's subsurface scattering.  
**Translation:** Vocabulary: scattering: 散射; subsurface: 次表层

**[87.72s] English:** Because we think of humans as opaque, but really our skin is light travels through it. It's not  
**Translation:** 

**[93.72s] English:** completely opaque. And the way in which light travels through skin has a huge impact on our  
**Translation:** Vocabulary: opaque: 不透明的

**[97.74s] English:** appearance. And this is why there's no way you can paint a mannequin to look realistic for a human.  
**Translation:** 

**[102.96s] English:** It's just a solid surface. And we'll never have the sort of detail you see.  
**Translation:** Vocabulary: mannequin: 人体模型

**[108.74s] English:** That kind of blew my mind, like thinking through that. I think I heard that sort of the oiliness  
**Translation:** 

**[114.40s] English:** of the skin creates very specific  
**Translation:** Vocabulary: oiliness: 皮肤油腻

**[117.72s] English:** nuance, complex.  
**Translation:** 

**[120.00s] English:** reflections. And then some light is absorbed and travels through the skin. And that creates  
**Translation:** Vocabulary: nuance: 细微差别

**[126.26s] English:** textures that our human eye is able to perceive. And it creates the thing that we consider  
**Translation:** 

**[131.32s] English:** human, whatever that is. All of that while considering all the muscles involved in making  
**Translation:** Vocabulary: perceive: 感知

**[138.46s] English:** the nuanced expression, just the subtle squinting of the eyes or the subtle formation of a smile.  
**Translation:** 

**[145.46s] English:** It's the subtlety of human faces that you have to capture. The difference between a real smile  
**Translation:** Vocabulary: squinting: 眯眼; subtlety: 微妙

**[150.46s] English:** and a fake smile. But the way to show the beginning of a formation of a smile that actually  
**Translation:** 

**[156.80s] English:** reveals a deep sadness. All of that. When I watch a human face, I can read that. I can see that.  
**Translation:** 

**[163.86s] English:** You have to have the tools that in real time can render something like that. And that's incredibly  
**Translation:** 

**[169.82s] English:** difficult. That's right. Getting faces right requires the interplay of literally dozens of  
**Translation:** 

**[174.50s] English:** different systems.  
**Translation:** 

**[175.46s] English:** Aspects of computer graphics. And if any one of them is wrong, your eye is completely drawn to  
**Translation:** 

**[181.18s] English:** that. And you find it on the wrong side of Uncanny Valley.  
**Translation:** 

**[186.38s] English:** The following is a conversation with Tim Sweeney, a legendary video game programmer,  
**Translation:** 

**[191.66s] English:** founder and CEO of Epic Games that created many incredible games and technologies, including  
**Translation:** 

**[197.48s] English:** the Unreal Engine and Fortnite, which both revolutionized the video game industry and  
**Translation:** Vocabulary: fortnite: 堡垒之夜; revolutionized: 革新

**[203.86s] English:** the experience.  
**Translation:** 

**[205.46s] English:** Playing and creating video games. This is the Lex Friedman Podcast. To support it,  
**Translation:** 

**[212.28s] English:** please check out our sponsors in the description. And now, dear friends, here's Tim Sweeney.  
**Translation:** 

**[218.84s] English:** When did you first fall in love with computers? And maybe with programming?  
**Translation:** Vocabulary: sponsors: 赞助商; sweeney: 斯威尼

**[223.48s] English:** I had a brother, Steve Sweeney, who was 16 years older than me. And at some point when I was a  
**Translation:** 

**[229.38s] English:** little kid, he went off to work in California for a tech company. And he'd gotten one of the first  
**Translation:** 

**[234.28s] English:** IBM PCs.  
**Translation:** 

**[235.48s] English:** And so for one summer, I think I was about 11, I went to visit him in California for my first  
**Translation:** Vocabulary: california: 加利福尼亚

**[239.94s] English:** life.  
**Translation:** 

**[240.00s] English:** trip away from my family just to hang out with him and he had this brand new IBM computer and I  
**Translation:** 

**[244.90s] English:** learned to program over the course of a few days in BASIC. I was just blown away with the capabilities  
**Translation:** 

**[249.98s] English:** of computers at the time. It was unbelievable what they could accomplish and I was just hooked from  
**Translation:** 

**[255.36s] English:** that point onward and very much wanted to be a programmer. Do you remember what you wrote in  
**Translation:** 

**[260.54s] English:** BASIC? Is it a video game type thing? Is it like for loop some numerical thing? Do you remember?  
**Translation:** Vocabulary: numerical: 数字相关; onward: 从那时起; programmer: 程序员

**[267.04s] English:** Yeah, it's funny. I have a perfectly vivid memory of all the first things I learned to  
**Translation:** 

**[272.42s] English:** program. I have a hard time remembering people's names, but code really sticks with me.  
**Translation:** 

**[277.82s] English:** Every step and every challenge, there were lessons learned. Some of which I've come to  
**Translation:** 

**[282.30s] English:** realize were just like me getting over some learning hurdles, but other things were actually  
**Translation:** Vocabulary: hurdles: 障碍

**[286.88s] English:** shortcomings of programming languages and the realization that there are actually better ways  
**Translation:** 

**[291.96s] English:** than what a programmer is learning to program for the first time. A lot of what they're  
**Translation:** Vocabulary: realization: 觉悟; shortcomings: 不足

**[296.54s] English:** facing,  
**Translation:** 

**[297.04s] English:** isn't the challenge of learning a new art. It's the friction introduced by failures of programming  
**Translation:** 

**[302.90s] English:** language design. I've constantly come back to those early lessons there as I've progressed and  
**Translation:** 

**[308.46s] English:** done more and more things, including building programming languages.  
**Translation:** Vocabulary: progressed: 发展

**[311.86s] English:** Yeah, the friction and the pain is the guide to learning in programming. If I were to describe  
**Translation:** 

**[319.28s] English:** programming journey, that would be marked by pain. That pain, you shouldn't escape the pain. The pain  
**Translation:** 

**[326.46s] English:** is the guide to learning in programming. If I were to describe programming journey,  
**Translation:** 

**[327.02s] English:** the pain is the guide to oleję rat theaters or anything like that.  
**Translation:** 

**[327.52s] English:** But because of all the challenges in my life, there's really no where you can find my own  
**Translation:** 

**[333.16s] English:** purpose in it.  
**Translation:** 

**[333.66s] English:** Tom Ceculis  
**Translation:** 

**[338.46s] English:** At an early age, I was a big involved in programming, as I said. I knew it was  
**Translation:** 

**[343.70s] English:** difficult to use the auctions that the ATL to a woman wrote. I was there for a month and  
**Translation:** 

**[346.32s] English:** a half, which is widely anticipated. And as you can see here, I had ambiente that is similar  
**Translation:** Vocabulary: ambiente: 环境; auctions: 拍卖

**[349.56s] English:** the ASPUM of AI.  
**Translation:** 

**[350.30s] English:** But I'm pretty sure my customer is in a very different situation than most generations  
**Translation:** 

**[352.02s] English:** for me.  
**Translation:** 

**[352.44s] English:** My uni is in South America, which is also an asristic area. I did my master's in  
**Translation:** 

**[356.10s] English:** exercise for half a year before I left. Kim  
**Translation:** 

**[356.34s] English:** went to a course, Menschen Langen Terrains for a national competition. 2007-209  
**Translation:** Vocabulary: terrains: 地形

**[356.48s] English:** It took about a couple hours to build and tune.  
**Translation:** 

**[360.00s] English:** And I went from there. But I built a lot of things. I built databases at different points. I built a programming language and a full compiler for a language like Pascal, because I didn't know where you went to buy one of those. So I made my own.  
**Translation:** Vocabulary: databases: 数据库; pascal: 帕斯卡语言

**[372.36s] English:** And one of the fun things of that time was bulletin boards. Before we had the internet in the hands of consumers, you used your modem and you dialed into a local phone number and connected to whoever was running the computer there.  
**Translation:** 

**[387.54s] English:** And every town or city had hundreds of these bulletin boards run by different people with their own personalities and teams. And so I spent a lot of time building a bulletin board program and learning how to deal with database management and user interface and dealing with multiple users concurrently and things.  
**Translation:** Vocabulary: concurrently: 同时; interface: 界面

**[401.70s] English:** And so...  
**Translation:** 

**[402.36s] English:** I probably spent about 10 or 15,000 hours writing code just on my own as a kid between like age 10 and age 20 before I actually shipped a program to the outside world.  
**Translation:** 

**[416.10s] English:** 10 to 15,000 hours. What was the value of the hours as a kid you put in in programming that led to the success you've had in later life? Maybe this is by way of advice to younger people in terms of how they allocate the hours of their early life.  
**Translation:** 

**[432.36s] English:** Yeah, you know, it's not just hours. It's really striving to learn, to understand what knowledge you have, what knowledge you lack, and to continually do experiments and work on projects that improve your knowledge base.  
**Translation:** Vocabulary: allocate: 分配; striving: 努力

**[447.02s] English:** And I didn't do this with a great amount of structure or planning. I was rather just going from project to project doing things that I thought would be fun and cool.  
**Translation:** 

**[454.92s] English:** And with each project, I learned new things, you know, learning about how to store and manage data, learning how to deal with advanced data structures.  
**Translation:** 

**[461.50s] English:** How to...  
**Translation:** 

**[461.70s] English:** How to write complex programs that have deeply nested data and control flow.  
**Translation:** 

**[467.74s] English:** Each one of those, you know, provided a lesson which were later essential.  
**Translation:** 

**[472.84s] English:** You know, in 1991, I released my first game.  
**Translation:** 

**[476.36s] English:** And over the course of that decade, we went from...  
**Translation:** 

**[480.00s] English:** You know, zero commercial releases to the first generation Unreal Engine.  
**Translation:** 

**[483.86s] English:** But, you know, this was largely just using the knowledge that I'd built up over the previous decade, just doing fun hobby projects.  
**Translation:** 

**[490.80s] English:** And if I hadn't done all that work, there's no way I could have ever built the things that came later.  
**Translation:** 

**[495.28s] English:** All the experimentation and all the exploration somehow contributed, somehow made sense later on.  
**Translation:** 

**[503.44s] English:** Like all of that is integrated somehow in the stuff you build.  
**Translation:** Vocabulary: experimentation: 实验

**[506.28s] English:** It's funny how life works.  
**Translation:** 

**[507.34s] English:** Like the pieces kind of come together eventually.  
**Translation:** 

**[512.72s] English:** Yeah, you know, there are definitely karate kid moments.  
**Translation:** 

**[515.24s] English:** Because, you know, all this time I was learning math in high school and in college.  
**Translation:** Vocabulary: karate: 武术

**[520.32s] English:** I studied mechanical engineering.  
**Translation:** 

**[521.74s] English:** And so, you know, you learn all kinds of math, vector calculus and vector math and matrices.  
**Translation:** Vocabulary: calculus: 微积分; matrices: 矩阵

**[528.38s] English:** And, you know, all these related fields, physics and stress and strain and how to, you know, deal with complex physical systems.  
**Translation:** 

**[536.34s] English:** And, yeah, I wasn't really sure how engineers would actually make use of that knowledge.  
**Translation:** 

**[542.58s] English:** Do you just like forget about it when you actually go off to do work?  
**Translation:** 

**[545.90s] English:** Or is it, do you write down equations on paper?  
**Translation:** Vocabulary: equations: 方程式

**[547.82s] English:** It was actually not clear as an early engineering student what you do.  
**Translation:** 

**[551.92s] English:** But when I started writing the first generation Unreal Engine and I was dealing with 3D math, I was like, wait, I know this stuff.  
**Translation:** 

**[556.74s] English:** I learned this.  
**Translation:** 

**[558.12s] English:** And, you know, so, you know, suddenly like the karate kid, you know, you get to paint the fence and wax the car and suddenly put all the pieces together into.  
**Translation:** 

**[566.34s] English:** You know, a 3D engine based on a whole lot of accumulated programming language and math knowledge.  
**Translation:** 

**[571.34s] English:** Often knowledge gained without ever anticipating that I might use it in that way.  
**Translation:** Vocabulary: accumulated: 累积; anticipating: 预期

**[576.74s] English:** Also, I think what's useful is over and over learning a hard thing.  
**Translation:** 

**[583.72s] English:** And then showing to yourself, you know, that you can do it, that you can learn a hard thing.  
**Translation:** 

**[590.40s] English:** So then when you come to having to write a 3D engine that in ways that haven't.  
**Translation:** 

**[596.34s] English:** Been done before, you're like, I've been here.  
**Translation:** 

**[600.00s] English:** I've been here in this experience.  
**Translation:** 

**[601.74s] English:** I don't know what to do, but we'll figure it out.  
**Translation:** 

**[604.20s] English:** We'll learn.  
**Translation:** 

**[604.88s] English:** I'll learn all the necessary components.  
**Translation:** 

**[606.76s] English:** So just not being afraid of something new.  
**Translation:** 

**[610.30s] English:** That's right.  
**Translation:** 

**[610.94s] English:** And constantly striving to make connections between these fields and look for their applications.  
**Translation:** 

**[615.80s] English:** Long after I'd shipped on Unreal Engine, it was like going back through an engineering textbook and looking at, oh, yeah, I used that.  
**Translation:** Vocabulary: striving: 努力

**[621.16s] English:** I used that.  
**Translation:** 

**[621.64s] English:** I used that.  
**Translation:** 

**[621.96s] English:** And then I got to the section on eigenvalues.  
**Translation:** 

**[624.38s] English:** I'm like, I don't know what the hell this is.  
**Translation:** Vocabulary: eigenvalues: 特征值

**[626.10s] English:** But, you know, it turns out eigenvectors and eigenvalues were the critical breakthrough that made the Google search engine technology work and stand apart from the rest because they found if you threw all the links that exist in the web and, you know, links from and to different sites and you put them in a giant matrix and you conclude it, you found the dominant eigenvalues, then those eigenvectors described the best search results for different things.  
**Translation:** 

**[649.82s] English:** And so constantly picking up knowledge and looking for ways to put it together is the thing.  
**Translation:** Vocabulary: eigenvectors: 特征向量; matrix: 矩阵

**[656.10s] English:** And if you aspire to be a programmer, you've got to write a lot of code and you've got to continually learn new things and improve.  
**Translation:** 

**[662.84s] English:** And if you want to be an artist, you've got to continually draw artwork of all styles and all kinds and constantly push yourself to learn more and more because you never know exactly what you're going to end up doing in the long run.  
**Translation:** Vocabulary: artwork: 艺术品; programmer: 程序员

**[674.74s] English:** But the more knowledge you have and the more skills, the more chance you have putting it together and being successful.  
**Translation:** 

**[680.16s] English:** And whether you're a programmer or an artist, you should probably take linear algebra, even though it doesn't make sense at the time.  
**Translation:** Vocabulary: algebra: 代数

**[685.22s] English:** I found.  
**Translation:** 

**[686.10s] English:** Getting engineering, an engineering degree and then never working in an engineering field, you know, just being a computer programmer was immensely valuable.  
**Translation:** Vocabulary: immensely: 极其

**[694.86s] English:** You know, I went to University of Maryland, which for some disciplines, it's kind of known as a party school, but they work the engineers to death, worked really hard.  
**Translation:** 

**[702.46s] English:** And if you learn any engineering discipline, you learn massive amounts of math and you learn the rigor of problem solving.  
**Translation:** Vocabulary: disciplines: 专业; rigor: 严谨

**[707.92s] English:** You know, not just what you find from the Wikipedia article, but going through all the exercises of solving complex problems and building.  
**Translation:** 

**[716.10s] English:** You know, you have to go through a series of solutions to derive an answer.  
**Translation:** 

**[719.32s] English:** It's it's.  
**Translation:** 

**[720.00s] English:** and it is it embodies the knowledge that you need as a programmer and you know people often go to  
**Translation:** Vocabulary: embodies: 体现

**[725.38s] English:** university and think okay my goal here is to get good grades so i get a diploma and i prove to an  
**Translation:** 

**[729.02s] English:** employer they're invaluable like no that's just kind of the superficial bookkeeping of the  
**Translation:** Vocabulary: bookkeeping: 会计记录; invaluable: 无价的; superficial: 表面的

**[734.42s] English:** university the real purpose of all of this is to learn and whether you learn formally or you learn  
**Translation:** 

**[740.20s] English:** on your own it's the learnings that are really valuable in a career um and especially if you're  
**Translation:** Vocabulary: learnings: 学习收获

**[745.30s] English:** going to be an entrepreneur it's really knowing the stuff that matters and not having the  
**Translation:** 

**[748.98s] English:** the diplomas and uh yeah there's ever more pressure to make a build rebuild society more  
**Translation:** Vocabulary: diplomas: 文凭; entrepreneur: 企业家

**[755.24s] English:** and more around credentials do you have this certificate do you have that proof but like you  
**Translation:** 

**[759.58s] English:** know companies that are focused on just building great products and doing great things uh gravitate  
**Translation:** Vocabulary: credentials: 证明资质; gravitate: 趋向

**[765.48s] English:** towards people who do the great work yeah one of the great things about youth is uh there's more  
**Translation:** 

**[773.42s] English:** freedom there's just more time to learn and people when they go to high school they sometimes think  
**Translation:** 

**[778.74s] English:** wow  
**Translation:** 

**[778.96s] English:** i can't wait to get out of this and be an adult and be free but it's not quite freedom when you  
**Translation:** 

**[785.78s] English:** get a job you start a family all wonderful things you get less more and more busy in less and less  
**Translation:** 

**[792.16s] English:** time to learn in the general sense learn whatever the hell you want that that is a wonderful time  
**Translation:** 

**[799.02s] English:** in life the the teenage years the early 20s the 20s when you could just learn random shit yeah  
**Translation:** 

**[805.90s] English:** you know i think this is something that's kind of changing in america  
**Translation:** 

**[808.96s] English:** um there's so much focus on grades and homework and um structure around kids lives you know when  
**Translation:** 

**[815.38s] English:** i was growing up you know my mom would feed me and my neighbors yeah my their my neighbors and  
**Translation:** 

**[819.80s] English:** moms would feed them breakfast and they'd you know be like well be back by dark um yeah and  
**Translation:** 

**[825.46s] English:** you know we'd go out and we'd play and we'd do all sorts of things we'd you know explore the  
**Translation:** 

**[829.68s] English:** woods we'd build go-karts we'd uh you know salvage old pieces of electronics and build  
**Translation:** 

**[834.34s] English:** you know what we thought were our space ship spacecraft control panels um for the  
**Translation:** Vocabulary: salvage: 回收利用; spacecraft: 宇宙飞船

**[838.96s] English:** you know the fix  
**Translation:** 

**[840.00s] English:** spaceships we were building as play and uh we'd have an enormous amount of freedom and uh you know  
**Translation:** 

**[845.28s] English:** from basically being a little kid through um through the time i went off to college um it had  
**Translation:** 

**[851.94s] English:** an enormous amount of free time and some people just use that and waste it and watch tv some  
**Translation:** 

**[856.34s] English:** people socialized um and some people really got into serious projects uh so many people at all  
**Translation:** 

**[862.70s] English:** times were doing cool things you know i was programming i was learning to build things i was  
**Translation:** Vocabulary: socialized: 社交

**[866.40s] English:** uh you know before i was releasing games to the world i'd be like yeah having neighborhood folks  
**Translation:** 

**[871.76s] English:** over to play the things i was working on and check them out and sometimes they're impressed  
**Translation:** 

**[875.52s] English:** and sometimes they weren't um and they'd have their own projects and often we'd have spare  
**Translation:** 

**[879.76s] English:** time jobs and everybody was entrepreneurial like everybody you know had a side gig sometimes you  
**Translation:** 

**[884.62s] English:** go around and mow people's lawns or you'd you know you know rake the leaves up and you know  
**Translation:** 

**[889.74s] English:** earn money and the freedom there and uh the organic learning that occurred there i think  
**Translation:** 

**[896.00s] English:** is something that  
**Translation:** 

**[896.40s] English:** is really critical to the american experience i i worry is increasingly going away as  
**Translation:** 

**[900.86s] English:** society is ever more protective and sheltering um and makes it harder to get these experiences  
**Translation:** 

**[906.50s] English:** so on the video game side when did you first fall in love with video games  
**Translation:** Vocabulary: sheltering: 庇护

**[913.16s] English:** i've had a funny relationship with games because my real aspiration has always been to program  
**Translation:** 

**[921.22s] English:** cool stuff i get more enjoyment of programming than anything else in the world um  
**Translation:** Vocabulary: aspiration: 抱负

**[926.40s] English:** and so you know that my first really too formative experience with games  
**Translation:** 

**[931.02s] English:** we're playing this game called adventure for the atari 2600 it was like you moved this dot around  
**Translation:** 

**[937.96s] English:** the screen and picked up objects like swords and fought dragons and invaded castles and solved  
**Translation:** 

**[943.58s] English:** puzzles very very simple iconic stuff you know rather than realistic graphics and then the other  
**Translation:** Vocabulary: dragons: 龙

**[948.94s] English:** game that really got immersed in was zork which was a text adventure game it would tell you where  
**Translation:** 

**[954.10s] English:** you are and what you see and you type in commands like zork and then you'd be like oh my god i'm so  
**Translation:** Vocabulary: immersed: 全身心投入

**[956.26s] English:** like go north or pick up sword or open door and explore a world  
**Translation:** 

**[960.00s] English:** that way so the game didn't have any graphics but in your mind you had this elaborate picture of  
**Translation:** Vocabulary: elaborate: 详细描绘

**[965.18s] English:** what you were seeing there and uh it really brought in inspired imagination more than other  
**Translation:** 

**[970.34s] English:** things and playing those games led me to often want to learn to program everything i saw there  
**Translation:** 

**[975.16s] English:** and that drove a lot of my programming i learned how to move a player around the screen i learned  
**Translation:** 

**[980.40s] English:** how to you know build a design tool so i could build castles and save them off and play them  
**Translation:** 

**[985.42s] English:** in a game and i realized there was a separation between the tools that you use to build a game  
**Translation:** 

**[988.92s] English:** and the game itself and that if the more powerful tools you had the more creativity you could  
**Translation:** 

**[993.28s] English:** unleash in yourself or others um and you know i learned all the programming techniques that  
**Translation:** 

**[998.36s] English:** supported games how to parse text you know pick up sword and go north how do you make that sentence  
**Translation:** Vocabulary: parse: 解析

**[1004.92s] English:** into an actual series of commands on the computer um and that was really really exciting um i have  
**Translation:** 

**[1012.14s] English:** to say until the time that fortnite came out i played video games primarily to learn what they  
**Translation:** Vocabulary: fortnite: Fortnite

**[1016.74s] English:** were doing so i could go off and do that myself  
**Translation:** 

**[1018.44s] English:** um  
**Translation:** 

**[1018.92s] English:** you know i'd sit down you know when wolfenstein came out and then doom came out um you know i'd  
**Translation:** 

**[1024.86s] English:** go through and look at pixel by pixel i'd move the mouse very slightly and look exactly what  
**Translation:** Vocabulary: pixel: 像素; wolfenstein: 狼穴

**[1028.70s] English:** was happening to figure out that's great what technique was being used there that was a puzzle  
**Translation:** 

**[1033.08s] English:** solving at a grand scale and it was so fun uh so so take me there in the early 90s so you launched  
**Translation:** 

**[1040.62s] English:** epic games in 1991 so you're the writing of your first big video game uh zzt  
**Translation:** 

**[1048.92s] English:** develop a terminal macbook pur Slowpoint  
**Translation:** 

**[1049.48s] English:** what was it like what was the technical challenge was the psychological challenge of building that  
**Translation:** 

**[1054.78s] English:** was a funny project because i didn't start out to build a video game  
**Translation:** 

**[1067.70s] English:** um i just moved from an apple to that so my brother bought my family an apple too right after i visited in california  
**Translation:** 

**[1073.48s] English:** so i've been programming on that for a few years learned a lot of techniques but weren't many apple  
**Translation:** Vocabulary: california: 加利福尼亚

**[1078.70s] English:** of my own.  
**Translation:** 

**[1080.00s] English:** was learning to program and i realized i needed a text editor so i started writing a text editor  
**Translation:** 

**[1083.84s] English:** you know a text editor is a program to edit text files you have logic to move the cursor around and  
**Translation:** 

**[1089.52s] English:** let people type things and backspace and delete and do all those you know mundane actions and  
**Translation:** Vocabulary: backspace: 退格; mundane: 平凡

**[1094.48s] English:** you know one night i was like i'd finished it up and i was like well okay i have a text editor but  
**Translation:** 

**[1098.92s] English:** this is pretty boring and so i made the cursor uh into a smiley face character and i had the  
**Translation:** Vocabulary: smiley: 笑脸

**[1103.82s] English:** like different characters you could place in this document perform different gameplay actions some  
**Translation:** 

**[1108.68s] English:** would be walls and some would kill you and some would be moving objects that could fly around the  
**Translation:** 

**[1113.58s] English:** screen and so this text editor i made evolved into a little game editor so i was building these levels  
**Translation:** 

**[1118.18s] English:** for a game i put a lot of time into like building an editor in a primitive set of objects about 20  
**Translation:** 

**[1125.02s] English:** or 30 different objects enough to build a really cool and compelling game but not so many that  
**Translation:** 

**[1129.22s] English:** players would lose track of what they're seeing i started off just building different game levels  
**Translation:** Vocabulary: compelling: 引人入胜

**[1133.98s] English:** you know the idea is you'd be on a series of board they'd be connected by you know going north  
**Translation:** 

**[1138.36s] English:** you know you'd be on a series of boards and you'd be on a series of boards and you'd be on a series  
**Translation:** 

**[1138.68s] English:** bath the end of the current board would take you to a new one if it was open or maybe it was  
**Translation:** 

**[1142.40s] English:** blocked and you couldn't go there i built this whole game world around that and you know this  
**Translation:** 

**[1146.74s] English:** was the game that became zct and uh i was having fun with it uh building it and playing it but i  
**Translation:** 

**[1152.20s] English:** didn't know if it really worked so uh did this experiment i started inviting neighbors over like  
**Translation:** 

**[1157.44s] English:** some adults some kids of all different ages and sat them down from it and say like here's a game  
**Translation:** 

**[1161.20s] English:** i made uh figure it out yeah and you know i had to force myself not to tell them what they need to  
**Translation:** 

**[1166.96s] English:** do right because i really wanted to do it and i had to force myself not to tell them what they  
**Translation:** 

**[1168.66s] English:** wanted to learn if if they were able to uh you know discover it all for themselves you know today  
**Translation:** 

**[1173.62s] English:** we would call this uh you know user experience test um and there's a whole field of research  
**Translation:** 

**[1178.32s] English:** around user experience research but back then it was just inviting some kids over to play the game  
**Translation:** 

**[1182.36s] English:** i took notes about what they got stuck on and what they enjoyed and where they felt bored um and just  
**Translation:** 

**[1187.98s] English:** iteratively polished the game until i felt it was good and i put it out um and released it on well  
**Translation:** Vocabulary: polished: 打磨完善

**[1192.86s] English:** this was before the internet so there were board and boards i upload it to a bunch of local bulletin  
**Translation:** 

**[1196.66s] English:** boards and uh from there it started to work and i started to build it and i started to build it  
**Translation:** 

**[1198.66s] English:** because you know  
**Translation:** 

**[1200.00s] English:** the way to build up cred for bulletin board users was to upload new files and  
**Translation:** 

**[1203.94s] English:** to claim that,  
**Translation:** 

**[1204.86s] English:** Hey,  
**Translation:** 

**[1204.94s] English:** I was the first that brought this to you.  
**Translation:** 

**[1206.88s] English:** And,  
**Translation:** 

**[1207.32s] English:** uh,  
**Translation:** 

**[1207.42s] English:** you know,  
**Translation:** 

**[1207.60s] English:** so there was a natural tendency of the software to spread.  
**Translation:** 

**[1210.22s] English:** I decided to use the share or model,  
**Translation:** 

**[1212.06s] English:** you know,  
**Translation:** 

**[1212.22s] English:** so I didn't just build this one game.  
**Translation:** 

**[1214.14s] English:** I built a trilogy of three games.  
**Translation:** 

**[1216.80s] English:** Um,  
**Translation:** Vocabulary: trilogy: 三部曲

**[1217.42s] English:** I released the first one for free and I said,  
**Translation:** 

**[1219.86s] English:** Hey,  
**Translation:** 

**[1220.00s] English:** if you'd like this by the two sequels.  
**Translation:** 

**[1221.86s] English:** Um,  
**Translation:** Vocabulary: sequels: 后续作品

**[1222.68s] English:** and I,  
**Translation:** 

**[1223.46s] English:** I included my parents mailing address and,  
**Translation:** 

**[1225.76s] English:** uh,  
**Translation:** 

**[1226.34s] English:** said,  
**Translation:** 

**[1226.60s] English:** you know,  
**Translation:** 

**[1226.76s] English:** send us $30 and,  
**Translation:** 

**[1228.50s] English:** you can get the sequels to this game.  
**Translation:** 

**[1229.78s] English:** And,  
**Translation:** 

**[1230.06s] English:** uh,  
**Translation:** 

**[1230.18s] English:** the check started coming in,  
**Translation:** 

**[1231.34s] English:** uh,  
**Translation:** 

**[1231.54s] English:** within a few days.  
**Translation:** 

**[1232.98s] English:** It was making like getting three or four orders a day.  
**Translation:** 

**[1235.86s] English:** I was making like a hundred dollars a day.  
**Translation:** 

**[1237.48s] English:** I'm like,  
**Translation:** 

**[1237.72s] English:** Ooh,  
**Translation:** 

**[1237.94s] English:** I'm rich.  
**Translation:** 

**[1239.02s] English:** Cause you know,  
**Translation:** 

**[1239.80s] English:** being a 20 year old,  
**Translation:** 

**[1240.60s] English:** that was like a pretty big deal.  
**Translation:** 

**[1243.10s] English:** What did that feel like?  
**Translation:** 

**[1244.30s] English:** Just getting money and probably feeling this immense success from something you've created.  
**Translation:** Vocabulary: immense: 巨大

**[1251.46s] English:** Well,  
**Translation:** 

**[1252.02s] English:** yeah,  
**Translation:** 

**[1252.38s] English:** I looked at money always just as a tool to help you fund accomplishing cool things.  
**Translation:** 

**[1257.44s] English:** Um,  
**Translation:** Vocabulary: accomplishing: 完成目标

**[1258.06s] English:** and you know,  
**Translation:** 

**[1259.06s] English:** having enough,  
**Translation:** 

**[1259.64s] English:** to do the things you want to do is the critical thing.  
**Translation:** 

**[1262.16s] English:** Um,  
**Translation:** 

**[1263.02s] English:** it's always been just very utilitarian,  
**Translation:** 

**[1264.92s] English:** but the knowledge that other people all around the country and then,  
**Translation:** Vocabulary: utilitarian: 实用主义

**[1267.96s] English:** you know,  
**Translation:** 

**[1268.16s] English:** in a month later,  
**Translation:** 

**[1269.12s] English:** all around the world were playing the game.  
**Translation:** 

**[1270.64s] English:** That was,  
**Translation:** 

**[1271.22s] English:** that was mind boggling,  
**Translation:** 

**[1273.08s] English:** you know,  
**Translation:** Vocabulary: boggling: 令人困惑的

**[1273.30s] English:** that me like this,  
**Translation:** 

**[1274.16s] English:** the soul kid who'd put out a game on a local bulletin board,  
**Translation:** 

**[1277.26s] English:** uh,  
**Translation:** 

**[1277.48s] English:** could be doing international business and chipping discs all over the world,  
**Translation:** Vocabulary: chipping: 削片

**[1280.94s] English:** um,  
**Translation:** 

**[1281.84s] English:** to players,  
**Translation:** 

**[1282.50s] English:** you know,  
**Translation:** 

**[1282.68s] English:** because the software is spreading on its own.  
**Translation:** 

**[1285.20s] English:** Well,  
**Translation:** 

**[1285.32s] English:** it's just magical.  
**Translation:** 

**[1286.14s] English:** Like that.  
**Translation:** 

**[1287.08s] English:** And that was a new thing for software.  
**Translation:** 

**[1288.44s] English:** Like that did not happen with mechanics.  
**Translation:** 

**[1289.64s] English:** Like you manufactured one,  
**Translation:** 

**[1292.02s] English:** you sold it to somebody and they had it.  
**Translation:** 

**[1293.62s] English:** And that was it.  
**Translation:** 

**[1294.22s] English:** But software could spread.  
**Translation:** 

**[1296.08s] English:** that was just really cool to see.  
**Translation:** 

**[1297.20s] English:** And it made me realize there's really no upward limit on the potential for  
**Translation:** 

**[1300.26s] English:** business like that.  
**Translation:** 

**[1301.42s] English:** You know,  
**Translation:** 

**[1302.12s] English:** we saw Microsoft is a big juggernaut company at the time,  
**Translation:** Vocabulary: juggernaut: 巨无霸企业

**[1305.36s] English:** but it's like,  
**Translation:** 

**[1305.68s] English:** Hey,  
**Translation:** 

**[1305.90s] English:** you know,  
**Translation:** 

**[1306.86s] English:** if Epic does games good enough,  
**Translation:** 

**[1308.06s] English:** you know,  
**Translation:** 

**[1308.22s] English:** we could accomplish what they've accomplished with operating systems.  
**Translation:** 

**[1311.48s] English:** And the sky was the limit.  
**Translation:** 

**[1312.82s] English:** Uh,  
**Translation:** 

**[1313.04s] English:** and I think this is the age we live in now.  
**Translation:** 

**[1315.76s] English:** It's,  
**Translation:** 

**[1316.52s] English:** you don't have to be an industrialist manufacturing.  
**Translation:** 

**[1319.32s] English:** Um,  
**Translation:** 

**[1319.60s] English:** you know,  
**Translation:** 

**[1319.62s] English:** you don't have to be an industrialist manufacturing.  
**Translation:** 

**[1319.64s] English:** This is cool.  
**Translation:** 

**[1320.00s] English:** products anybody who builds anything digitally if it's good enough you can reach the entire world  
**Translation:** Vocabulary: digitally: 以数字方式

**[1325.28s] English:** and build the you know next microsoft or meta or apple or google or or epic games it's such a cool  
**Translation:** 

**[1332.68s] English:** origin story though you start out building a text editor so you're looking at this project you're  
**Translation:** 

**[1337.96s] English:** playing around with it you're building up the tools it's it's just an inspiring moment because  
**Translation:** 

**[1345.56s] English:** a lot of us start out building a project and to allow yourself to see the potential  
**Translation:** 

**[1352.56s] English:** pivots the potential trajectories that can go is really nice to sit back allow yourself to be bored  
**Translation:** 

**[1359.52s] English:** and like ah i'm gonna go this way i mean that's like a crossroads you came to a crossroads i mean  
**Translation:** Vocabulary: pivots: 转折点; trajectories: 轨迹

**[1366.72s] English:** you built uh you know compilers you design your own programming language but compilers databases  
**Translation:** 

**[1372.68s] English:** all these things you mentioned and  
**Translation:** Vocabulary: compilers: 编译器; databases: 数据库

**[1375.38s] English:** you  
**Translation:** 

**[1375.56s] English:** started building a text editor and they here came to this crossroad i'm gonna make this fun  
**Translation:** Vocabulary: crossroad: 十字路口

**[1381.88s] English:** and then from there you know one of the most legendary gaming companies was created it's  
**Translation:** 

**[1387.54s] English:** kind of cool like that that that's an inspiring thing for sort of developers like be open to the  
**Translation:** 

**[1393.66s] English:** possibility of creating something you didn't plan to create and just go with it right that's cool  
**Translation:** 

**[1399.68s] English:** yeah and it was a bunch of learnings emerged really quickly there the neat thing i did with  
**Translation:** Vocabulary: learnings: 学习收获

**[1405.04s] English:** czt  
**Translation:** 

**[1405.38s] English:** was i didn't just release the game i also released the editor with it i built this tool so i could make  
**Translation:** 

**[1410.74s] English:** these zct boards that people could play but i also gave it to all the players themselves and um  
**Translation:** 

**[1415.60s] English:** you know like 30 years later i still run into people you know when i go to a game industry  
**Translation:** 

**[1419.86s] English:** event it was like you know i grew up playing zzt and you know here's an adult who grew up playing  
**Translation:** 

**[1425.06s] English:** my game and it was because it enabled anybody to become a creator too it had you know this  
**Translation:** 

**[1430.44s] English:** little board editor and it also had a little scripting language so you could learn a little  
**Translation:** 

**[1433.44s] English:** bit of programming in it too and um  
**Translation:** 

**[1435.38s] English:** it kind of impressed and it really set a formative principle that  
**Translation:** 

**[1440.00s] English:** Epic, which was that, you know, the company's mission is to make awesome entertainment,  
**Translation:** 

**[1444.68s] English:** but also awesome tools and to share those tools with everybody so that they can build  
**Translation:** 

**[1448.72s] English:** their own amazing things too.  
**Translation:** 

**[1449.92s] English:** And, you know, when we got into Unreal Engine a few years later, the interplay between us  
**Translation:** 

**[1455.78s] English:** building a game and us building tools that were widely used by others was a critical  
**Translation:** 

**[1460.56s] English:** part of that.  
**Translation:** 

**[1461.12s] English:** And I think that's the sole reason that Epic has been massively successful.  
**Translation:** 

**[1464.96s] English:** And actually, the reason that we've survived all of this time is that by serving both  
**Translation:** 

**[1468.94s] English:** creators and gamers, we've been able to weather the ups and downs of the game industry.  
**Translation:** 

**[1474.40s] English:** It's a brutal place for companies.  
**Translation:** 

**[1477.66s] English:** We've been able to survive every financial downturn.  
**Translation:** Vocabulary: brutal: 残酷的

**[1480.28s] English:** And sometimes the engine's been funding the business because we didn't have a game.  
**Translation:** 

**[1483.66s] English:** And sometimes the games have been funding the business.  
**Translation:** 

**[1485.82s] English:** And it really set a principle in our culture that's persevered and is continually brought  
**Translation:** 

**[1491.98s] English:** to the forefront.  
**Translation:** Vocabulary: forefront: 最前沿; persevered: 坚持

**[1493.12s] English:** But on the editor front, that's such a fascinating philosophy that you always allow people to  
**Translation:** 

**[1498.50s] English:** create.  
**Translation:** 

**[1498.94s] English:** Create their own worlds.  
**Translation:** 

**[1501.36s] English:** You have an engine from which you simulate the world that the game is in.  
**Translation:** Vocabulary: simulate: 模拟

**[1507.06s] English:** You have the actual game.  
**Translation:** 

**[1509.02s] English:** And you also have the freedom for creators to create various, you know, in Fortnite,  
**Translation:** Vocabulary: fortnite: 堡垒之夜

**[1514.90s] English:** islands of their own.  
**Translation:** 

**[1517.98s] English:** So it's like with everything you ship, that freedom to create is always there.  
**Translation:** 

**[1522.00s] English:** That's really interesting.  
**Translation:** 

**[1523.72s] English:** Yeah.  
**Translation:** 

**[1524.48s] English:** And it's something we aim to do more and more fully over time, you know, in the course  
**Translation:** 

**[1528.50s] English:** of building Fortnite.  
**Translation:** 

**[1529.56s] English:** We've built a lot of other tools that are useful for us, too, because it's not just  
**Translation:** 

**[1532.66s] English:** a game powered by Unreal Engine, but it's also, you know, a social ecosystem where people  
**Translation:** 

**[1538.06s] English:** can make friends and voice chat and get together and party.  
**Translation:** 

**[1540.92s] English:** So we've opened up all of those social features into Epic Online Services.  
**Translation:** 

**[1544.80s] English:** And we give them away to all developers for free because we all benefit from growth in  
**Translation:** 

**[1548.28s] English:** that user base.  
**Translation:** 

**[1550.42s] English:** And, you know, our goal is ultimately to build the company's products on the same technology  
**Translation:** 

**[1554.76s] English:** that we share with everybody else and to help that foster a bigger and bigger, you know,  
**Translation:** Vocabulary: foster: 促进

**[1558.48s] English:** ecosystem over time.  
**Translation:** 

**[1560.00s] English:** everybody benefits if we could just linger on the 90s uh so you said bulletin boards maybe you can  
**Translation:** 

**[1568.32s] English:** explain what that's like and also explain the birth of the internet what that was like what  
**Translation:** 

**[1573.52s] English:** was the what was the internet like in the 90s so the internet is a funny thing it started out as  
**Translation:** 

**[1578.98s] English:** this defense department um research project called the arpanet the advanced research project agency  
**Translation:** 

**[1584.56s] English:** network and um it was kind of like this revered secret thing uh that became more and more open as  
**Translation:** Vocabulary: arpanet: 高级研究项目网

**[1591.16s] English:** they connected universities uh universities connected to the internet in the you know mid  
**Translation:** 

**[1596.04s] English:** 1980s and so if you were at a prestigious institution with access to computers you could  
**Translation:** Vocabulary: prestigious: 有名望的

**[1601.02s] English:** get on there but the consumer back then we just had these modems you know this thing you plug into  
**Translation:** 

**[1605.42s] English:** your phone line um and it dials up a phone number and then you know it sends wild sound effects over  
**Translation:** 

**[1611.48s] English:** the over the telephone line to send digital  
**Translation:** 

**[1614.50s] English:** sound effects over the telephone line to send digital sound effects over the telephone line to  
**Translation:** 

**[1614.54s] English:** signals back and forth and these were really slow three you know the first modem i had was 300  
**Translation:** 

**[1619.22s] English:** boards that means 30 characters per second of data so you're like sitting there watching a sentence  
**Translation:** 

**[1624.50s] English:** like slowly emerge character by character as you're going online but yeah that's how we got online and  
**Translation:** 

**[1629.28s] English:** we talked with each other so you dial up to a local bulletin board it'll be run by a person  
**Translation:** 

**[1633.44s] English:** usually they have a computer or two sitting in their kitchen or something that's running the  
**Translation:** 

**[1637.48s] English:** bulletin board and um they have a small community of a few hundred users all competing to connect  
**Translation:** 

**[1642.38s] English:** to that one phone line um it was awful  
**Translation:** 

**[1644.48s] English:** and busy and you couldn't get in and uh the more popular wooden boards were hardest to get to  
**Translation:** 

**[1648.40s] English:** um nice but you had all kinds of communities developed you know and you could see like there  
**Translation:** 

**[1652.40s] English:** was the programming communities where people talked about programming there was the news  
**Translation:** 

**[1656.72s] English:** and events you know uh community i was lived in the outskirts of washington dc so that was like a  
**Translation:** 

**[1661.76s] English:** big thing but then there was like the pirate community where they're sharing pirated apple  
**Translation:** Vocabulary: outskirts: 郊区

**[1665.52s] English:** two games and you know a very different uh community ethos and mantras out there but all  
**Translation:** 

**[1671.92s] English:** you know all really nice and also very small um  
**Translation:** Vocabulary: ethos: 价值观; mantras: 座右铭

**[1674.48s] English:** These things, these wooden boards couldn't grow to the size of Facebook because your phone line couldn't take that many calls.  
**Translation:** 

**[1680.00s] English:** um and you know then uh then later in the 1990s the the internet which had been fostered in these  
**Translation:** 

**[1686.62s] English:** colleges started opening up to the public and anybody could connect to it and suddenly the  
**Translation:** 

**[1690.86s] English:** world took on a life of its own it became much much easier to reach global audience faster  
**Translation:** 

**[1695.50s] English:** and you would start shipping games to the internet which is a bit of a crazy thing to do  
**Translation:** 

**[1701.62s] English:** because you're supposed to have like a you know a physical copy but to post on the internet it's  
**Translation:** 

**[1707.44s] English:** pretty innovative even shareware is pretty innovative yeah you know it's been a funny  
**Translation:** 

**[1712.10s] English:** transition for the game business you know epic started out making shareware games distributed  
**Translation:** Vocabulary: shareware: 共享软件

**[1715.82s] English:** digitally um but you know as the first 3d games took off like wolfenstein and doom from id software  
**Translation:** 

**[1722.60s] English:** and then unreal from us um took off you know to reach a huge audience of millions of users we had  
**Translation:** Vocabulary: digitally: 以数字方式; wolfenstein: 狼人杀

**[1728.00s] English:** to go into retail stores so we worked with a retail publisher and they made a box and put cd  
**Translation:** 

**[1731.84s] English:** roms in the box and um and you know then the world started transitioning back to digitally  
**Translation:** Vocabulary: transitioning: 转变

**[1736.64s] English:** like  
**Translation:** 

**[1737.22s] English:** and that transition didn't start well right the initial transition of gaming to digital was  
**Translation:** 

**[1742.64s] English:** all bit torrent all piracy um and you know there are horror stories about games that would uh you  
**Translation:** 

**[1748.28s] English:** know sell like a hundred thousand copies but have two million users um because most people pirated  
**Translation:** 

**[1754.02s] English:** it um and then you know steam came along and introduced digital distribution and uh made  
**Translation:** 

**[1760.20s] English:** digital distribution of legit games so convenient um that most players moved away from piracy  
**Translation:** Vocabulary: legit: 正版

**[1766.02s] English:** towards that and uh  
**Translation:** 

**[1767.22s] English:** and you know their practices were then followed by others and the early digital industry uh  
**Translation:** 

**[1772.54s] English:** took form yeah it's fascinating i mean pirates do lead the way for innovation  
**Translation:** 

**[1777.50s] English:** the same as the story of spotify you basically i think most people when they derive value from  
**Translation:** 

**[1784.98s] English:** things like video games want to pay for those video games they just want it to be easy and so  
**Translation:** 

**[1791.14s] English:** that the same thing with music with spotify uh but maybe just staying in the 90s and then you know  
**Translation:** 

**[1797.22s] English:** they're going to be a lot of indie game developers  
**Translation:** 

**[1800.00s] English:** who listened to us talking today can you uh go back to that mindset and try to derive some wisdom  
**Translation:** Vocabulary: indie: 独立游戏开发者; mindset: 思维方式

**[1806.58s] English:** and advice to those folks when you were just a solo developer maybe just a small group of people  
**Translation:** 

**[1812.98s] English:** uh creating your early games that eventually became this uh huge gaming company but in the  
**Translation:** 

**[1821.92s] English:** early days what what uh what were you going through what were the ups and downs uh what  
**Translation:** 

**[1828.12s] English:** did it take to sort of stay strong and persevere well you know one of the critical things that epic  
**Translation:** 

**[1834.18s] English:** always worked hard to do was to make something different um that nobody else was doing um and to  
**Translation:** 

**[1841.02s] English:** try to satisfy a small audience rather than competing globally with the game juggernauts  
**Translation:** Vocabulary: globally: 全世界; juggernauts: 巨头

**[1846.06s] English:** you know back in the 1990s epic was new but electronic arts and activision and the other  
**Translation:** 

**[1851.06s] English:** big publishers had been around for a decade and they were huge companies um it had giant retail  
**Translation:** Vocabulary: activision: 动视

**[1856.44s] English:** distribution networks  
**Translation:** 

**[1857.62s] English:** you know if i tried to make a game and then convince them to publish it i i doubt i could  
**Translation:** 

**[1863.10s] English:** have had a chance and i doubt uh that if even if i made a successful game that i would have made  
**Translation:** 

**[1868.18s] English:** much money from it though they might have um and you know so the really unique angle to epic then  
**Translation:** 

**[1873.14s] English:** was shareware and that was just the idea that if we distribute our game differently then we can  
**Translation:** 

**[1877.54s] English:** reach a much larger audience than these bigger competitors by virtue of this first episode of  
**Translation:** Vocabulary: shareware: 共享软件

**[1882.28s] English:** the game being free you know it was kind of the advent of what later became free to play um  
**Translation:** 

**[1887.62s] English:** and the logic of that is just as true now as it was then it's if the thing is free and anybody can  
**Translation:** 

**[1893.90s] English:** get into it then it's going to spread from friend to friend as people bring you know their real world  
**Translation:** 

**[1899.12s] English:** friends into into the games they're playing and uh you know have the opportunity to build up a  
**Translation:** 

**[1903.66s] English:** community around that you know so the other lesson there was minimize the friction of people  
**Translation:** 

**[1908.26s] English:** getting into your game make it easy to get into and make it fun and i think the other well i was  
**Translation:** Vocabulary: friction: 阻力

**[1914.10s] English:** very fortunate zzt was a funny game it was not like  
**Translation:** 

**[1917.62s] English:** much like any other game it was it had much worse  
**Translation:** 

**[1920.00s] English:** Because it was all just text characters, smiley faces and, you know, other Greek letters and things participating in this game simulation. They were kind of iconic representations of characters rather than real ones. And, you know, this was decades into the age of real graphical games with interesting graphics.  
**Translation:** 

**[1937.54s] English:** And so it wasn't even trying to compete in that area, but it was able to compete in a different area, which is that, you know, it wasn't just my, the three games that I'd made and shipped as a trilogy that were successful and drove the success of the product.  
**Translation:** Vocabulary: graphical: 图形的; simulation: 模拟; smiley: 笑脸; trilogy: 三部曲

**[1951.54s] English:** It was the fact that I released an editor and there's a whole community around it.  
**Translation:** 

**[1955.14s] English:** And you see that trend has repeated itself.  
**Translation:** 

**[1957.72s] English:** Like there was, you know, ZZT was one of it.  
**Translation:** 

**[1960.38s] English:** Before that, there was Bill Budge's pinball construction set.  
**Translation:** Vocabulary: pinball: 弹珠游戏

**[1963.16s] English:** That was a 1980s Apple game that let users build their own pinball tables.  
**Translation:** 

**[1966.64s] English:** And since then, you've had some of the world's most successful games follow that path.  
**Translation:** 

**[1970.92s] English:** Like Minecraft, you can build your own stuff.  
**Translation:** 

**[1972.92s] English:** Roblox, you know, Fortnite Creative and Unreal Editor for Fortnite.  
**Translation:** Vocabulary: fortnite: 堡垒之夜

**[1976.64s] English:** You know, games that become platforms for other people to build stuff was a real opportunity.  
**Translation:** 

**[1982.12s] English:** You know, I think the big thing to realize is for indie developers right now is like there's massive, massive competition in every major genre.  
**Translation:** Vocabulary: indie: 独立开发者

**[1990.48s] English:** And it's very unlikely that unless you just happen to be the world's best at a particular thing,  
**Translation:** 

**[1995.64s] English:** that you're going to release a game.  
**Translation:** 

**[1996.72s] English:** And then existing highly competitive genre and win a much better chance of success is releasing something that hasn't been done before.  
**Translation:** 

**[2005.82s] English:** Being really unique and reaching an audience, even if big or medium size or small, reaching an audience and becoming really popular with that.  
**Translation:** 

**[2013.60s] English:** Making some money from it and being able to reinvest and then expand towards your ultimate dream.  
**Translation:** 

**[2018.28s] English:** I think the one shot go from idea to commercial success at massive scale is a lot less likely.  
**Translation:** Vocabulary: reinvest: 再投资

**[2026.64s] English:** than the multi-step process of continually build better and better stuff over time until you get into a position of excellence.  
**Translation:** 

**[2034.54s] English:** And constantly try to do something that others aren't doing.  
**Translation:** 

**[2038.46s] English:** Yeah, that's right.  
**Translation:** 

**[2040.00s] English:** at every market um there's a few markets where the current leader came late to the space um usually  
**Translation:** 

**[2046.48s] English:** because the the prior leader failed so horribly um but most of the time that you know the company  
**Translation:** 

**[2052.48s] English:** that's succeeding and winning in a market is the first or second entrant there um they've just  
**Translation:** Vocabulary: entrant: 初入者; horribly: 糟糕地

**[2057.76s] English:** continually buoyed their success great advice and fascinating but on a human level was it lonely  
**Translation:** 

**[2064.56s] English:** was it scary you sitting there as a developer i'd say it was uh it was the opposite of lonely  
**Translation:** Vocabulary: buoyed: 支撑

**[2072.14s] English:** because uh you know the thing that spurred me to actually release this was seeing kids playing the  
**Translation:** 

**[2077.94s] English:** game in my neighborhood and having fun i mean like this is really good um and seeing them enjoying it  
**Translation:** 

**[2082.78s] English:** and laughing and pointing at the screen and you know getting together and just wanting to play  
**Translation:** 

**[2086.78s] English:** more um yeah and the human element was always pervasive you know because i i did not only  
**Translation:** Vocabulary: pervasive: 无处不在

**[2093.38s] English:** receive orders but people would actually  
**Translation:** 

**[2094.56s] English:** write letters you know we wrote letters back then in the 1990s um people would say how much  
**Translation:** 

**[2098.98s] English:** they were enjoying the game and how their kids were playing the game and so on and so on um  
**Translation:** 

**[2102.84s] English:** so you know they felt very connected um and you know i think a lot of businesses have to make  
**Translation:** 

**[2108.70s] English:** scary decisions uh because you're spending you know potentially all the money you have to take  
**Translation:** 

**[2113.46s] English:** a shot at something that you're not sure will succeed uh i was very fortunate starting a  
**Translation:** 

**[2118.28s] English:** business like this because it didn't really need any capital the capital was well the several  
**Translation:** 

**[2122.58s] English:** thousand dollars in computers i'd bought by mowing  
**Translation:** Vocabulary: mowing: 割草

**[2124.48s] English:** lawns  
**Translation:** 

**[2124.56s] English:** um and it wasn't much risk if that hadn't succeeded i guess i could have figured out  
**Translation:** 

**[2130.32s] English:** how people get mechanical engineering jobs and pursued that but um once it took off and once the  
**Translation:** 

**[2135.42s] English:** once the orders started coming in and people started writing letters saying they're enjoying  
**Translation:** 

**[2139.68s] English:** the game i knew i was going to go all out and try to build a company there and succeed and  
**Translation:** 

**[2143.72s] English:** that was like going to be you know my big goal so i'm sure people know but uh epic games was  
**Translation:** 

**[2151.60s] English:** created in 1991 and went on to uh  
**Translation:** 

**[2154.56s] English:** transform the gaming industry several times uh one of which is unreal engine  
**Translation:** 

**[2160.00s] English:** so let's talk to the origin story of that you said that when wolfenstein and doom came out  
**Translation:** 

**[2167.58s] English:** that changed everything so take me to that moment yeah that that was a very interesting time epic  
**Translation:** Vocabulary: wolfenstein: 狼穴游戏

**[2174.28s] English:** had uh after my first couple of games that had recruited developers you know usually college  
**Translation:** 

**[2180.70s] English:** students high school students who are just working on their own had real skills uh but didn't have an  
**Translation:** Vocabulary: recruited: 招募

**[2184.74s] English:** outlet for their work um epic had been matchmaking the best artists and programmers together from all  
**Translation:** 

**[2189.56s] English:** over the world like chas jackrabbit was cliff bluzinski a high school kid in california who  
**Translation:** Vocabulary: bluzinski: 布卢兹金; california: 加利福尼亚; jackrabbit: 兔鹿; matchmaking: 牵线搭桥; programmers: 程序员

**[2194.58s] English:** made a really cool adventure game together with arian brucey a demo coder from holland who'd make  
**Translation:** 

**[2199.52s] English:** amazing graphical stuff and had built a 2d game engine um and connected them together and a  
**Translation:** Vocabulary: arian: 阿里安; graphical: 图形的

**[2205.44s] English:** musician robert allen in california and they you know by telephone and modem and so on we're we're  
**Translation:** 

**[2210.74s] English:** building these little 2d games and having quite a lot of success you know there are a bunch of  
**Translation:** 

**[2214.90s] English:** people making thousands of dollars a month while they're still students um and royalties  
**Translation:** 

**[2219.42s] English:** for the game and so on and so on and so on and so on and so on and so on and so on and so on  
**Translation:** Vocabulary: royalties: 版税

**[2219.54s] English:** epic was kind of producing and by coordinating people with people and publishing um through  
**Translation:** 

**[2225.14s] English:** shareware um and that was all going great uh the company had a little office and we were you know  
**Translation:** Vocabulary: coordinating: 协调; shareware: 共享软件

**[2231.50s] English:** copying floppy floppy disks and mailing them out but um when wolfenstein came out we realized like  
**Translation:** 

**[2237.56s] English:** the future of gaming is going to be 3d um it there had been a lot of experiments in 3d before that  
**Translation:** Vocabulary: floppy: 软盘

**[2244.14s] English:** hadn't been great you know there were 2d mate there are 3d renderings of mazes that were not  
**Translation:** 

**[2249.54s] English:** and you were always looking north south east or west um and then there were vector graphics with  
**Translation:** Vocabulary: mazes: 迷宫; renderings: 渲染

**[2254.38s] English:** little wire frames moving around and things but uh you know wolfenstein was the first game that was  
**Translation:** 

**[2259.78s] English:** fast enough you know running at 30 frames per second it really felt immersive it felt like  
**Translation:** 

**[2264.14s] English:** you were there like you were you know in this castle wolfenstein fighting nazis and that was  
**Translation:** 

**[2269.24s] English:** a really amazing and immersive experience 3d graphics were pretty primitive then id software  
**Translation:** Vocabulary: immersive: 身临其境; nazis: 纳粹

**[2273.94s] English:** followed shockingly fast with doom which was much much more capable 3d engine and it was a lot more  
**Translation:** 

**[2279.54s] English:** efficient which had  
**Translation:** Vocabulary: shockingly: 出乎意料地

**[2280.00s] English:** you know stairs and though it was still what we call two and a half d it was environments that  
**Translation:** 

**[2285.94s] English:** were very realistic textures that were very realistic uh you know a form of lighting uh  
**Translation:** 

**[2290.10s] English:** that was approximate but incredibly realistic and a just such great artistry and sound effects it  
**Translation:** 

**[2295.52s] English:** it fueled completely visceral um and and real um yeah you might you might look at it today from a  
**Translation:** Vocabulary: approximate: 大致; artistry: 艺术; visceral: 直觉的

**[2303.00s] English:** you know point of view of a modern uh you know game player with uh you know 20 teraflops of  
**Translation:** 

**[2308.94s] English:** computing power in your device and say oh that's not very impressive but it was amazing at the  
**Translation:** Vocabulary: computing: 计算; teraflops: 万亿次浮点

**[2312.74s] English:** time i mean for me just decided to to pause on that i think wolfenstein was one of the most uh  
**Translation:** 

**[2320.72s] English:** amazing moments of my own life just being able to like you said in real time move about a  
**Translation:** Vocabulary: wolfenstein: 狼穴游戏

**[2326.22s] English:** three-dimensional world i just remember just like just moving around just in like what is that  
**Translation:** 

**[2334.96s] English:** feeling like  
**Translation:** 

**[2335.86s] English:** i mean you  
**Translation:** 

**[2338.92s] English:** feel transported into another world you feel that you're there yeah and especially when you turn the  
**Translation:** Vocabulary: transported: 心灵遨游

**[2344.08s] English:** lights down in your room and you turn the sound up on your speakers and it will scare you uh and  
**Translation:** 

**[2350.42s] English:** you'll you'll feel like you know that fireball that's coming at you is going to kill you uh  
**Translation:** 

**[2354.46s] English:** that was an amazing time because we hadn't experienced that before there was nothing like  
**Translation:** 

**[2358.74s] English:** that uh you know you'd watch a movie a scary movie or whatever you know it was just this thing that  
**Translation:** 

**[2365.60s] English:** was happening this was you this was you in a 3d world  
**Translation:** 

**[2368.92s] English:** so uh how did that how did that change epic this realization that the future of gaming is going to  
**Translation:** Vocabulary: realization: 觉悟

**[2374.70s] English:** be 3d well at first i was really depressed i think because yeah the wizardry of doom especially was  
**Translation:** 

**[2382.06s] English:** so incredible that i gave up on programming for like six months i was like i don't ever be able  
**Translation:** Vocabulary: wizardry: 神奇魔力

**[2386.56s] English:** to compete with this i have no idea what we're going to do um we just keep making 3d 2d games  
**Translation:** 

**[2390.40s] English:** and hope that the business goes on but um uh that was the nature of carmax wizardry he had done  
**Translation:** 

**[2396.06s] English:** things that were like not just one in the future but like a lot of things that were like a lot of  
**Translation:** 

**[2398.92s] English:** innovation leap ahead but like  
**Translation:** 

**[2400.00s] English:** a dozen simultaneously interplaying in a way that you couldn't pick them apart into their component  
**Translation:** 

**[2404.54s] English:** pieces but um funny thing happened michael abrash a long timer in computer graphics wrote a book  
**Translation:** 

**[2410.94s] English:** on the techniques for 3d graphics and texture mapping and he wrote some articles in a in one  
**Translation:** 

**[2419.10s] English:** of the programming magazines of the day and um explained it and showed assembly code to do  
**Translation:** 

**[2423.80s] English:** texture mapping you know drawing these 3d graphics on the screen and it's actually really simple  
**Translation:** 

**[2427.48s] English:** stuff i was like oh i can do that and uh and you know so a bunch of us at epic independently went  
**Translation:** Vocabulary: independently: 独立地

**[2433.66s] English:** off and wrote our started writing our own 3d graphics code to figure it out and um uh we found  
**Translation:** 

**[2439.50s] English:** at one point we had a number of people dabbling in this doing different parts of it and uh at that  
**Translation:** Vocabulary: dabbling: 涉足

**[2443.38s] English:** point we decide okay this is 3d graphics and 3d gaming is going to completely change the world we  
**Translation:** 

**[2448.76s] English:** need to go all in on this and so we took the best people from our best 2d game development teams and  
**Translation:** 

**[2452.72s] English:** put them all together to make a 3d game um we didn't really know what we were doing at the time  
**Translation:** 

**[2457.42s] English:** none of us had ever shipped a 3d game and most of us were still learning but um everybody was like  
**Translation:** 

**[2461.96s] English:** trying different disciplines to see what they were best at and um it was a combination of a bunch of  
**Translation:** 

**[2467.26s] English:** people who came together to make unreal i'd initially volunteered to make the 3d editor  
**Translation:** Vocabulary: disciplines: 学科领域; volunteered: 自愿参与

**[2471.72s] English:** um for the thing and james schmaltz had made epic pinball epic pinball now that wasn't a crazy game  
**Translation:** 

**[2477.14s] English:** this was one of the 2d sharer games he made it while he was in college and he was making like  
**Translation:** Vocabulary: pinball: 弹珠游戏; sharer: 分享者

**[2481.60s] English:** thirty thousand dollars a month from you know the royalties from this game because everybody had  
**Translation:** 

**[2487.10s] English:** wanted it  
**Translation:** Vocabulary: royalties: 版税

**[2487.42s] English:** an awesome pinball game massively successful but uh he was he was a multi-disciplinary person he  
**Translation:** 

**[2494.74s] English:** wrote the code for the game the art for the game and did basically everything and and the code was  
**Translation:** Vocabulary: massively: 极其

**[2499.04s] English:** 30 000 lines of assembly language and so uh he was initially going to write the 3d engine um  
**Translation:** 

**[2505.52s] English:** and i was going to write the editor and he sent me the his code so i could integrate into the  
**Translation:** Vocabulary: integrate: 合并

**[2510.06s] English:** editor it was like just a giant pile of assembly code why don't i just write this myself and so  
**Translation:** 

**[2516.22s] English:** james instead started going off and on and i was like why don't i just write this myself  
**Translation:** 

**[2517.42s] English:** and building 3d models and 3d animations using the tool  
**Translation:** 

**[2520.00s] English:** at the time.  
**Translation:** Vocabulary: animations: 动画

**[2520.76s] English:** And so Cliff, who had done a lot of design work  
**Translation:** 

**[2524.08s] English:** and built the levels on Jazz Jacket,  
**Translation:** 

**[2525.64s] English:** went off and started learning basics of level design.  
**Translation:** 

**[2528.04s] English:** And so I was writing this editor,  
**Translation:** 

**[2529.36s] English:** and Cliff Blizinski was customer number one for it,  
**Translation:** 

**[2532.38s] English:** starting to go off and build levels.  
**Translation:** 

**[2533.84s] English:** And James Schmaltz was building awesome creatures,  
**Translation:** 

**[2536.14s] English:** sending them to me.  
**Translation:** 

**[2536.94s] English:** I'd get them implemented in game.  
**Translation:** 

**[2538.36s] English:** And we brought in an animator to bring them into life.  
**Translation:** Vocabulary: animator: 动画师

**[2540.56s] English:** And we brought in more and more people  
**Translation:** 

**[2542.56s] English:** until at the peak of Unreal 1 development,  
**Translation:** 

**[2544.94s] English:** we had about 20 people working on it, which  
**Translation:** 

**[2547.60s] English:** was a huge team for the time.  
**Translation:** 

**[2548.98s] English:** And it was really stretching Epic's finances nearly  
**Translation:** 

**[2551.62s] English:** to the breaking point.  
**Translation:** Vocabulary: finances: 财务状况

**[2553.66s] English:** We barely survived and almost ran out of money  
**Translation:** 

**[2556.12s] English:** a number of times, but somehow we always pulled through.  
**Translation:** 

**[2558.80s] English:** And it was a crazy project, because it  
**Translation:** 

**[2560.96s] English:** was 3 and 1 half years of development in a game  
**Translation:** 

**[2563.08s] English:** that we always thought was six months from shipping.  
**Translation:** 

**[2566.62s] English:** And it was like 3 and 1 half years of 70 or 80 hour weeks  
**Translation:** 

**[2572.04s] English:** for most everybody working on the project,  
**Translation:** 

**[2575.50s] English:** not even knowing what problems we'd need to solve next,  
**Translation:** 

**[2577.84s] English:** because we were so immersed.  
**Translation:** 

**[2578.96s] English:** And the current ones.  
**Translation:** Vocabulary: immersed: 全神贯注

**[2580.34s] English:** Were there moments when you were losing hope  
**Translation:** 

**[2582.30s] English:** that this might take too long and the company will run out  
**Translation:** 

**[2585.84s] English:** of money?  
**Translation:** 

**[2588.20s] English:** We were always very financially stressed,  
**Translation:** Vocabulary: financially: 经济上

**[2590.68s] English:** so I was continually worried about that.  
**Translation:** 

**[2592.76s] English:** I had total confidence that we'd work out  
**Translation:** 

**[2594.56s] English:** all the technical and artistic problems,  
**Translation:** 

**[2596.42s] English:** because we knew the pieces.  
**Translation:** 

**[2598.92s] English:** And it was largely a matter of typing code in and solving  
**Translation:** 

**[2602.98s] English:** some problems.  
**Translation:** 

**[2604.44s] English:** And we knew we could ship a version of it.  
**Translation:** 

**[2606.64s] English:** And the thing that was really interesting  
**Translation:** 

**[2608.64s] English:** was the ongoing discovery of new techniques as we went.  
**Translation:** 

**[2613.02s] English:** Because at the time, Quake had shipped,  
**Translation:** 

**[2615.06s] English:** it had a little bit of dynamic lighting.  
**Translation:** 

**[2617.52s] English:** Unreal really pushed dynamic lighting much harder  
**Translation:** 

**[2619.98s] English:** than anybody else had done before.  
**Translation:** 

**[2622.14s] English:** We've been colored dynamic lights with some shadow casting  
**Translation:** 

**[2625.56s] English:** capabilities statically, or moving lights without shadows,  
**Translation:** 

**[2629.22s] English:** and figured out how to do volumetric fog,  
**Translation:** Vocabulary: statically: 固定地; volumetric: 体积的

**[2631.88s] English:** so you could have foggy areas that were full of lights,  
**Translation:** 

**[2634.40s] English:** and you could have a little bit of light  
**Translation:** 

**[2635.92s] English:** in the middle of the room.  
**Translation:** 

**[2637.02s] English:** And it was a lot of fun.  
**Translation:** 

**[2637.76s] English:** It was a lot of fun.  
**Translation:** 

**[2638.48s] English:** And you get the kind of glow of the light  
**Translation:** 

**[2640.00s] English:** standing out in the fog and affecting the appearance of the level a whole lot of amazing  
**Translation:** 

**[2645.10s] English:** techniques came together to build a game you know made a number of leaps ahead of the state of the  
**Translation:** 

**[2649.76s] English:** art at the time um uh yeah it was really crazy but like i think most companies wouldn't have  
**Translation:** 

**[2658.80s] English:** survived that but the sheer talent of the people involved made it possible and that's epic has  
**Translation:** 

**[2665.44s] English:** often done things that most companies will have failed at and we succeed like not because of  
**Translation:** 

**[2670.68s] English:** awesome management or awesome planning or awesome financing but because of the sheer talent and  
**Translation:** 

**[2675.22s] English:** willpower of the people involved to make it happen uh what about the uh interdisciplinary aspect of  
**Translation:** 

**[2681.20s] English:** it like you said sort of artists engineers or programmers designers all of them working  
**Translation:** Vocabulary: designers: 设计师; interdisciplinary: 跨学科的; programmers: 程序员; willpower: 意志力

**[2688.68s] English:** together what what what was that the 20 people what was the dynamic they're like working insane  
**Translation:** 

**[2694.54s] English:** hours  
**Translation:** 

**[2695.44s] English:** like what was it like to sort of make a team like that work together  
**Translation:** 

**[2699.48s] English:** well as an orchestra to to actually deliver the game yeah that that's one of the really unique  
**Translation:** 

**[2706.28s] English:** things to exist in gaming not in normal big tech companies which are just engineering and business  
**Translation:** 

**[2712.46s] English:** driven but gaming really does require all the best people across all the creative disciplines  
**Translation:** Vocabulary: disciplines: 学科领域

**[2718.80s] English:** working together um and you know epic could run organically by recruiting people with awesome  
**Translation:** 

**[2725.18s] English:** talents and you know and i think that's one of the things that's really important to me is that  
**Translation:** Vocabulary: organically: 自然发展; recruiting: 招聘

**[2725.42s] English:** um we were we always had a limited budget we could never pay to hire you know bid up people's  
**Translation:** 

**[2731.68s] English:** salaries and hire them away by paying them more we just had to find awesome people who were  
**Translation:** Vocabulary: salaries: 工资

**[2735.56s] English:** at the beginning of their career and put them together and um you know so everybody was very  
**Translation:** 

**[2740.08s] English:** new to this um and uh didn't have any assumptions about how companies worked and so you know you put  
**Translation:** Vocabulary: assumptions: 先入为主

**[2746.02s] English:** all these people together and um you know that it was really a constant interplay of talent as  
**Translation:** 

**[2751.52s] English:** people were learning how to work together as a team um like nobody had management  
**Translation:** 

**[2755.42s] English:** experience most people hadn't shipped a game before they worked with epic um  
**Translation:** 

**[2760.00s] English:** And we were figuring out as we went.  
**Translation:** 

**[2762.66s] English:** But it was a constant iterative cycle.  
**Translation:** 

**[2764.46s] English:** You know, we'd make several new versions of the game every day.  
**Translation:** Vocabulary: iterative: 循环改进

**[2767.62s] English:** Read a new compile, introduce a new feature, or fix some bugs, get it to the artist.  
**Translation:** 

**[2771.76s] English:** The artist improved their levels, continued building stuff.  
**Translation:** 

**[2775.42s] English:** And then we see what they're doing in their levels, like, ah, I see what you need now.  
**Translation:** 

**[2778.64s] English:** We'd constantly be improving the tools.  
**Translation:** 

**[2780.42s] English:** And just the iterative process and the speed at which that improves products is the critical element to success in games.  
**Translation:** 

**[2786.64s] English:** The slower the iteration cycle, if you make a build every week and you go through one iteration every week,  
**Translation:** Vocabulary: iteration: 迭代过程

**[2792.94s] English:** you're going to be way, way, way worse by the end of your project than a game company that makes new stuff every day.  
**Translation:** 

**[2799.70s] English:** And that was the magic that happened together.  
**Translation:** 

**[2802.54s] English:** And there was really nothing but passion and everybody's individual dedication to it that made it work.  
**Translation:** 

**[2809.04s] English:** I heard you still program, but how much programming were you doing back then?  
**Translation:** Vocabulary: dedication: 奉献精神

**[2813.24s] English:** You mentioned hours, probably insane hours.  
**Translation:** 

**[2816.26s] English:** So, like, it'd be almost fun to talk about your setup.  
**Translation:** Vocabulary: setup: 安装配置

**[2820.42s] English:** What a day in the life of Tim Sweeney in the 90s when you're building Unreal look like.  
**Translation:** 

**[2827.30s] English:** Well, we'd all gravitated towards a schedule, a work schedule that maximized productivity.  
**Translation:** Vocabulary: gravitated: 趋向; maximized: 最大化

**[2833.64s] English:** And that usually meant waking up late.  
**Translation:** 

**[2835.26s] English:** I'd get to, like, usually get to work around noon.  
**Translation:** 

**[2838.66s] English:** I'd usually work till, like, 2 a.m. or so, 3 a.m. sometimes.  
**Translation:** 

**[2844.56s] English:** And, you know, I didn't...  
**Translation:** 

**[2846.26s] English:** I didn't have anything else going on in my life.  
**Translation:** 

**[2847.80s] English:** So, I usually just work and sleep and occasional eating.  
**Translation:** 

**[2851.30s] English:** And I found I always needed eight or nine hours of sleep a night.  
**Translation:** 

**[2856.36s] English:** Without good sleep, I would just become a zombie and wouldn't be nearly at my best.  
**Translation:** Vocabulary: zombie: 行尸走肉

**[2860.04s] English:** So, I always needed to get sleep.  
**Translation:** 

**[2861.30s] English:** But I didn't need anything else going on.  
**Translation:** 

**[2862.82s] English:** So, I just...  
**Translation:** 

**[2863.30s] English:** The programming itself was so energizing and drawing.  
**Translation:** Vocabulary: energizing: 提神的

**[2867.66s] English:** Yeah, so it was, you know, three and a half years of that during the project.  
**Translation:** 

**[2871.78s] English:** Mostly spent programming.  
**Translation:** 

**[2873.60s] English:** I'd say probably 60 hours a week of programming.  
**Translation:** 

**[2876.26s] English:** Five hours a week of coordinating with other people and iterating.  
**Translation:** Vocabulary: coordinating: 协调工作

**[2880.00s] English:** and, you know, sitting down with them and looking at what's going on in screen  
**Translation:** 

**[2882.84s] English:** and figuring out what they needed, maybe five hours of business stuff.  
**Translation:** 

**[2887.32s] English:** You know, there's a good division at Labor then.  
**Translation:** 

**[2890.72s] English:** I didn't have a big executive team, but it was, like, basically myself  
**Translation:** 

**[2893.40s] English:** running the technical and development part of the company  
**Translation:** 

**[2896.88s] English:** and Mark Raine running the business part of it, doing deals  
**Translation:** 

**[2900.20s] English:** and, you know, maxing out his credit card and going around the world  
**Translation:** 

**[2904.02s] English:** bringing in sources of revenue to keep the company funded.  
**Translation:** 

**[2907.68s] English:** What programming language are we talking about, C?  
**Translation:** 

**[2909.38s] English:** Because you mentioned there's this pile of assembly.  
**Translation:** 

**[2912.44s] English:** What was your decision in choosing the programming language  
**Translation:** 

**[2915.64s] English:** that Unreal Engine would be written in?  
**Translation:** 

**[2919.54s] English:** I'd grown up learning with Pascal as my favorite language.  
**Translation:** 

**[2923.40s] English:** In order to just get maximum performance  
**Translation:** Vocabulary: pascal: 帕斯卡

**[2926.50s] English:** and get the latest operating system features,  
**Translation:** 

**[2928.76s] English:** I had to move to C for my second game, Joel of the Jungle,  
**Translation:** 

**[2932.80s] English:** a little Nintendo-style platformer.  
**Translation:** 

**[2934.62s] English:** And so when I started Unreal Engine, it was on 16-bit Windows  
**Translation:** Vocabulary: platformer: 平台游戏

**[2938.06s] English:** using the C programming.  
**Translation:** 

**[2939.38s] English:** And over the course of the first year, it moved to 32-bit,  
**Translation:** 

**[2945.12s] English:** using these DOS extenders and then using Windows NT,  
**Translation:** 

**[2950.46s] English:** and I moved to the C++ language.  
**Translation:** Vocabulary: extenders: dos扩展器

**[2952.54s] English:** And just because it simplified the code so much,  
**Translation:** 

**[2956.20s] English:** went from a really complicated pile of code to a much simpler one,  
**Translation:** 

**[2960.76s] English:** making that transition.  
**Translation:** 

**[2962.84s] English:** And so almost the entirety of Unreal Engine development,  
**Translation:** Vocabulary: entirety: 全部

**[2965.46s] English:** about two and a half years of it, was all on C++, 32-bit.  
**Translation:** 

**[2968.42s] English:** It's completely state-of-the-art.  
**Translation:** 

**[2969.38s] English:** And 32-bit protected mode was kind of a magical thing,  
**Translation:** 

**[2974.10s] English:** having come from the days when computers were much less reliable  
**Translation:** 

**[2976.70s] English:** and crashed all the time.  
**Translation:** 

**[2978.26s] English:** Yeah, and it turned out to be a pretty good bet,  
**Translation:** 

**[2979.72s] English:** because C++, out of all those languages,  
**Translation:** 

**[2982.66s] English:** ended up being the dominant performance-oriented language  
**Translation:** 

**[2988.16s] English:** that survives to this day.  
**Translation:** 

**[2990.62s] English:** Yeah, yeah.  
**Translation:** 

**[2991.98s] English:** It's because it solves all the problems at scale,  
**Translation:** 

**[2996.16s] English:** often through manual pain,  
**Translation:** 

**[2998.00s] English:** but always solves them.  
**Translation:** 

**[2999.38s] English:** And...  
**Translation:** 

**[3000.00s] English:** And a lot of other languages do better in a lot of, like, theoretical aspects and are better for some usage cases, but you can't do everything, and that's very limiting.  
**Translation:** 

**[3010.48s] English:** All right, so ridiculous questions, but, like, did you have one monitor, two monitors?  
**Translation:** 

**[3018.30s] English:** Were you picky on the keyboard?  
**Translation:** 

**[3021.02s] English:** Were you picky on the chair?  
**Translation:** 

**[3022.62s] English:** What are we talking about?  
**Translation:** 

**[3023.64s] English:** Let's paint a picture.  
**Translation:** 

**[3025.88s] English:** Okay, I went through a big transition there.  
**Translation:** 

**[3027.36s] English:** So I started out being pretty lazy.  
**Translation:** 

**[3029.32s] English:** I'd had a bunch of, like, I bought used computers because you'd often get them at half the price of a new one.  
**Translation:** 

**[3033.84s] English:** They'd be good enough.  
**Translation:** 

**[3034.82s] English:** So I had this old 486 I was developing on.  
**Translation:** 

**[3038.48s] English:** I guess it was a 15-inch monitor at the time.  
**Translation:** 

**[3041.40s] English:** It was a poor workstation setup, but it was very economical.  
**Translation:** 

**[3045.78s] English:** And so as we started on Unreal, I realized that, like, I had to write a ton of code.  
**Translation:** Vocabulary: economical: 经济实惠; setup: 设置; workstation: 工作站

**[3050.62s] English:** I had to write at absolute maximum productivity.  
**Translation:** 

**[3052.62s] English:** So I had to rearrange my entire life around delivering maximum output.  
**Translation:** Vocabulary: rearrange: 重新安排

**[3057.14s] English:** And so at that point, I realized, like, actually,  
**Translation:** 

**[3059.26s] English:** it's probably a good idea to have a computer that can do that.  
**Translation:** 

**[3059.30s] English:** So I had to rearrange my entire life around delivering maximum output.  
**Translation:** 

**[3059.32s] English:** So spending money on getting good equipment was a good investment.  
**Translation:** 

**[3062.36s] English:** And we're not talking about millions of dollars here, or billions if you're building a GPU farm.  
**Translation:** 

**[3066.40s] English:** We're just talking about buying some basic hardware.  
**Translation:** 

**[3069.12s] English:** And so I bought the biggest CRT you could buy at the time, because this was a CRT.  
**Translation:** 

**[3073.18s] English:** It was 24 inches.  
**Translation:** 

**[3074.34s] English:** It weighed, like, 100 pounds.  
**Translation:** 

**[3077.08s] English:** I had back pain for a week after I installed it.  
**Translation:** 

**[3080.06s] English:** But it got me 1920 by 1200 view in 1996.  
**Translation:** 

**[3088.10s] English:** In 1996.  
**Translation:** 

**[3088.72s] English:** That was pretty good.  
**Translation:** 

**[3089.30s] English:** That was pretty cool.  
**Translation:** 

**[3089.94s] English:** So I upgraded to a 90 megahertz Pentium and did a lot of programming on that.  
**Translation:** 

**[3093.54s] English:** It was on the 90 megahertz Pentium.  
**Translation:** Vocabulary: megahertz: 兆赫; upgraded: 升级

**[3094.96s] English:** These were the main consumer computers at the time.  
**Translation:** 

**[3097.04s] English:** And I'd optimized the Unreal Engine software render on that, which was, you know,  
**Translation:** Vocabulary: optimized: 优化; render: 渲染

**[3101.58s] English:** the Pentium was the first super scaler architecture in consumer computing.  
**Translation:** 

**[3106.42s] English:** It could run up to two instructions at a time.  
**Translation:** Vocabulary: computing: 计算机; scaler: 缩放

**[3109.66s] English:** And if you wrote your assembly code very carefully, you could get absolute maximum throughput.  
**Translation:** 

**[3114.68s] English:** So I'd gotten my texture mapping code down to six CPUs.  
**Translation:** Vocabulary: throughput: 最大吞吐量

**[3119.30s] English:** So I'm pretty comfortable.  
**Translation:** 

**[3121.14s] English:** And that's really what I've been doing for a long time.  
**Translation:** 

**[3124.02s] English:** So like I said, I've been doing this for a long time.  
**Translation:** 

**[3126.98s] English:** But I've been doing this for like almost four years.  
**Translation:** 

**[3129.14s] English:** And I'd go on and on and on and on and on and on.  
**Translation:** 

**[3131.28s] English:** But these things were called X-Files.  
**Translation:** 

**[3132.74s] English:** So while I was doing this, I'm just like, that's it.  
**Translation:** 

**[3134.86s] English:** I'm just going to go ahead and get this time.  
**Translation:** 

**[3136.66s] English:** I don't know what happened.  
**Translation:** 

**[3138.44s] English:** I was like, this is what I want to do.  
**Translation:** 

**[3141.54s] English:** But I get to be like a pro gamer.  
**Translation:** 

**[3143.90s] English:** And I'm like, dude, I can do this.  
**Translation:** Vocabulary: gamer: 电子游戏玩家

**[3145.68s] English:** Honestly, that is, you know.  
**Translation:** 

**[3147.96s] English:** You know, that's a good thing.  
**Translation:** 

**[3148.98s] English:** It's cool.  
**Translation:** 

**[3149.22s] English:** It's cool.  
**Translation:** 

**[3120.00s] English:** surprising 11 instructions um and uh you know that was required for every pixel on the screen  
**Translation:** 

**[3125.30s] English:** and that was just enough performance to deliver that um but i'd uh dill came out with the the  
**Translation:** 

**[3130.70s] English:** these new workstations and until i just launched the penny and pro the first out of order processor  
**Translation:** 

**[3135.82s] English:** um and so i i like basically bought the absolute maximum configuration that money can buy  
**Translation:** Vocabulary: configuration: 配置; processor: 处理器; workstations: 工作站

**[3141.82s] English:** it cost seven thousand dollars i had a gigabyte of memory in 1996 um 200 megahertz cpu so it like  
**Translation:** 

**[3149.96s] English:** tripled the speed of compiles and just made me massively more productive so that's why i was  
**Translation:** Vocabulary: compiles: 编译; gigabyte: 吉字节; massively: 大幅

**[3153.92s] English:** using throughout unreal engine uh development and shipped with that by the way people in the 90s  
**Translation:** 

**[3158.90s] English:** would have been blown away by this workstation i love it yeah yeah were you um in writing were  
**Translation:** 

**[3165.38s] English:** you considering the hardware much was there a sense like uh so you know for people don't know  
**Translation:** 

**[3170.44s] English:** unreal engine rendering i guess is all software doesn't use the hardware but were you trying to  
**Translation:** 

**[3175.96s] English:** optimize as i understand maybe you can correct me but like were you trying to  
**Translation:** 

**[3179.82s] English:** optimize the software for the hardware for the hardware for the hardware for the hardware for  
**Translation:** Vocabulary: optimize: 优化

**[3179.94s] English:** the hardware at all well um at the time so we did most unreal engine development before the first  
**Translation:** 

**[3187.36s] English:** real gpus came out um and uh you know the 3d effects voodoo one the first gpu that actually  
**Translation:** 

**[3193.86s] English:** delivered serious performance compared to software rendering um the first gpu that was really gainful  
**Translation:** 

**[3198.88s] English:** um came in the end of the development and we supported it really quickly but it was not the  
**Translation:** 

**[3203.46s] English:** target all along and so development was focused on just building there are two parts of the engine  
**Translation:** 

**[3208.80s] English:** right there's all the game  
**Translation:** 

**[3209.80s] English:** play systems um that manage the simulation and physics and so on that's all written in very high  
**Translation:** 

**[3215.02s] English:** level c++ code um and maintainability is as much of a goal as performance um you know because we  
**Translation:** Vocabulary: maintainability: 可维护性; simulation: 模拟

**[3222.20s] English:** had to build massive amounts of systems over time uh but the one thing that was really a bottleneck  
**Translation:** 

**[3227.86s] English:** was graphics you know the the cost of rendering a single pixel was really high and so you had to  
**Translation:** Vocabulary: bottleneck: 瓶颈; pixel: 像素

**[3232.96s] English:** do everything you possibly could to optimize the rendering of pixels on screen and you know so we  
**Translation:** 

**[3238.10s] English:** were talking about how many cpu cycles you had to do to optimize the rendering of pixels on screen  
**Translation:** Vocabulary: pixels: 屏幕像素

**[3239.80s] English:** so we were talking about how many cpu cycles you had to do to optimize the rendering of pixels on screen  
**Translation:** 

**[3240.00s] English:** You know, when you say your CPU runs at a gigahertz or whatever, that's a, you know, a billion instructions per second.  
**Translation:** Vocabulary: gigahertz: 吉赫兹

**[3247.46s] English:** How many instructions do you need to run to to get a pixel on screen?  
**Translation:** 

**[3251.00s] English:** And so there is a constant challenge to optimize that down.  
**Translation:** 

**[3254.90s] English:** And, you know, there is also a competition among all of the graphics programmers who often send emails, you know, like bragging to each other about what new technique they've discovered, you know, to try to get the cost down.  
**Translation:** 

**[3264.70s] English:** And Abrash's original articles took like 12 CPU cycles to render a pixel.  
**Translation:** Vocabulary: bragging: 吹嘘; programmers: 程序员; render: 渲染

**[3269.30s] English:** And, you know, everybody else had figured out how to get it to like down to six or sometimes even four cycles.  
**Translation:** 

**[3275.08s] English:** And, you know, that involved lots of different tradeoffs of caching and memory hierarchy and so on.  
**Translation:** Vocabulary: caching: 缓存; hierarchy: 层次; tradeoffs: 权衡

**[3279.62s] English:** It was just like a magical time where a human could actually understand exactly what the CPU was doing under the hood and could write code that exactly targeted that.  
**Translation:** 

**[3289.12s] English:** And that's largely lost now.  
**Translation:** 

**[3290.60s] English:** When we talk about optimization software now, it's largely about heuristics.  
**Translation:** 

**[3294.70s] English:** And statistically, you know, this memory access is likely to hit the cache.  
**Translation:** Vocabulary: cache: 缓存; heuristics: 启发式; optimization: 优化

**[3300.58s] English:** And, you know, this algorithm is faster than that algorithm.  
**Translation:** 

**[3303.74s] English:** Because CPUs now have such advanced out-of-order execution that you really can't micromanage what's happening on an instruction-by-instruction basis.  
**Translation:** Vocabulary: algorithm: 算法; micromanage: 细控

**[3311.20s] English:** You can only manage the aggregate performance of code.  
**Translation:** 

**[3314.54s] English:** And so there's kind of this lost art.  
**Translation:** Vocabulary: aggregate: 汇总

**[3316.72s] English:** Some people miss it.  
**Translation:** 

**[3317.46s] English:** Some people don't.  
**Translation:** 

**[3318.72s] English:** In which the programmer had absolute control over the machine and could work miracles.  
**Translation:** 

**[3324.70s] English:** And in special cases, if you tried.  
**Translation:** Vocabulary: programmer: 程序员

**[3327.08s] English:** It seems like there's still value to that art when it comes to GPUs and ASICs.  
**Translation:** 

**[3333.54s] English:** So basically trying to understand the nuances of the hardware and how to truly, truly optimize it.  
**Translation:** Vocabulary: nuances: 细微差别; optimize: 优化

**[3339.94s] English:** Whether it's for machine learning applications or for ultra-realistic, real-time graphics applications.  
**Translation:** 

**[3346.78s] English:** Is that true?  
**Translation:** 

**[3348.80s] English:** Yeah, that's absolutely so.  
**Translation:** 

**[3351.86s] English:** You know, the optimization problems have just moved around.  
**Translation:** 

**[3354.70s] English:** In a system like Nanite, the virtualized micro-polygon geometry...  
**Translation:** 

**[3360.00s] English:** A system that Brian Karras, a brilliant engineer with HAPEC, built was just one of those multi-year optimization efforts that required him understanding everything from the highest levels to the lowest levels of the hardware  
**Translation:** Vocabulary: geometry: 几何; virtualized: 虚拟化

**[3375.22s] English:** to figure out how to make this breakthrough technique work in a way that was actually maximally performant on GPUs.  
**Translation:** 

**[3383.22s] English:** And so Nanai is the system we'll jump around in time.  
**Translation:** 

**[3386.28s] English:** That takes us to today with Unreal Engine 5.  
**Translation:** 

**[3388.90s] English:** It's the system that does the geometry.  
**Translation:** 

**[3392.48s] English:** Yeah.  
**Translation:** 

**[3392.66s] English:** So rendering the world sort of geometrically.  
**Translation:** Vocabulary: geometrically: 几何地

**[3394.44s] English:** There's many layers to this.  
**Translation:** 

**[3395.70s] English:** We'll probably sneak up to each of those.  
**Translation:** 

**[3399.44s] English:** But one, you have to actually create the geometry of the world around you and do that in real time and really efficiently.  
**Translation:** 

**[3404.88s] English:** There's a bunch of different ways to optimize that.  
**Translation:** 

**[3408.18s] English:** Can you just speak to it?  
**Translation:** 

**[3409.42s] English:** Yeah.  
**Translation:** 

**[3409.66s] English:** You know, with the advanced art tools we have today, it's really easy to create a scene with billions of polygons.  
**Translation:** 

**[3415.62s] English:** The hard part is how to render it efficiently.  
**Translation:** Vocabulary: efficiently: 高效地; polygons: 多边形; render: 渲染

**[3417.52s] English:** Because you can't render billions of polygons in a frame.  
**Translation:** 

**[3421.04s] English:** Basically, you want to render an image that's indistinguishable from the full detailed geometry if you rendered it at ridiculous cost.  
**Translation:** 

**[3428.82s] English:** And so the challenge is how to simplify every component of the rendering, you know, the geometry, the lighting and so on, down to real time techniques.  
**Translation:** 

**[3437.44s] English:** They're efficient.  
**Translation:** Vocabulary: simplify: 简化

**[3438.72s] English:** They capture a realistic view of what's around you.  
**Translation:** 

**[3441.90s] English:** And so when an object is up close to you, you want to render it with a lot more polygons than when it's far away.  
**Translation:** 

**[3446.80s] English:** But one of the cool principles of mathematics is the Nyquist sampling theorem.  
**Translation:** 

**[3451.18s] English:** It says if you're trying to reconstruct a signal, there's a limit to the amount of data you need to bother capturing.  
**Translation:** Vocabulary: nyquist: 奈奎斯特; reconstruct: 重建; theorem: 定理

**[3458.70s] English:** If you want to render a texture at a certain resolution, then you never need more than twice the pixels than in the texture that you have on the screen.  
**Translation:** 

**[3467.48s] English:** And that's called the Nyquist limit.  
**Translation:** Vocabulary: pixels: 像素

**[3468.92s] English:** And so one of the challenges of computer graphics is given the need to render objects at extreme close up distances and extreme far away distances.  
**Translation:** 

**[3476.50s] English:** You always want to be able to generate the right amount of geometry so that you have enough.  
**Translation:** 

**[3480.00s] English:** to be indistinguishable from reality, but not any more than necessary.  
**Translation:** 

**[3485.48s] English:** And with geometry, the idea is that if you render two triangles per pixel,  
**Translation:** Vocabulary: geometry: 几何; pixel: 像素; triangles: 三角形

**[3490.20s] English:** you should get an image that is indistinguishable from thousands of triangles per pixel.  
**Translation:** 

**[3497.22s] English:** But if you render less than two triangles per pixel,  
**Translation:** 

**[3499.02s] English:** you're going to start to see visible artifacts of the loss.  
**Translation:** 

**[3502.50s] English:** And GPUs have this amazing hardware in a lot of different pipelines,  
**Translation:** Vocabulary: artifacts: 可见瑕疵; pipelines: 处理管道

**[3505.96s] English:** but it's all very fixed function.  
**Translation:** 

**[3507.04s] English:** There's pixel shader hardware, there's geometry processing hardware,  
**Translation:** Vocabulary: shader: 着色器

**[3510.80s] English:** and then there's triangle rasterization hardware.  
**Translation:** 

**[3513.66s] English:** One of the limits of GPUs is that the triangle rasterizers are built for pretty large triangles.  
**Translation:** Vocabulary: rasterization: 栅格化; rasterizers: 栅格化器; triangle: 三角形

**[3517.72s] English:** If you're building a triangle or rendering a triangle with 10 pixels, that's pretty efficient.  
**Translation:** 

**[3521.74s] English:** But if you're building or rendering a triangle with one pixel, it's very inefficient.  
**Translation:** Vocabulary: inefficient: 低效的

**[3525.94s] English:** So one of the breakthroughs Brian made was to design an entire pipeline  
**Translation:** 

**[3529.60s] English:** for avoiding the rasterization hardware in the GPU  
**Translation:** Vocabulary: breakthroughs: 重大突破; pipeline: 处理管道

**[3532.94s] English:** and just going straight to pixels and calculating,  
**Translation:** 

**[3537.04s] English:** what should be done with that pixel as a result of some ray tracing  
**Translation:** 

**[3540.08s] English:** and geometry intersection calculations done in a pixel shader.  
**Translation:** 

**[3545.84s] English:** So instead of using the triangle pipeline, we're just using the pixel pipeline  
**Translation:** Vocabulary: intersection: 交点计算

**[3549.32s] English:** and getting a better result.  
**Translation:** 

**[3552.80s] English:** Because of the limitations of the triangle rasterizer in the GPUs, that's fascinating.  
**Translation:** Vocabulary: rasterizer: 扫描转换器

**[3557.82s] English:** Because, as you described, you need the tiny triangles for the detail,  
**Translation:** 

**[3563.18s] English:** for the stuff that's up close.  
**Translation:** 

**[3564.74s] English:** I mean, this might seem obvious to people,  
**Translation:** 

**[3566.80s] English:** but it's not.  
**Translation:** 

**[3566.86s] English:** It's not.  
**Translation:** 

**[3566.96s] English:** It's not.  
**Translation:** 

**[3567.00s] English:** It's not.  
**Translation:** 

**[3567.04s] English:** It's not just stuff up close.  
**Translation:** 

**[3569.82s] English:** It depends on where you're looking.  
**Translation:** 

**[3573.08s] English:** The human eye and the human focus and the human attention mechanism  
**Translation:** 

**[3576.42s] English:** defines how much detail you want to show.  
**Translation:** 

**[3582.20s] English:** Because the thing that the human is likely to be giving attention to,  
**Translation:** 

**[3587.36s] English:** you want that to be super high resolution.  
**Translation:** 

**[3589.72s] English:** And everything else, including due to distance,  
**Translation:** 

**[3592.76s] English:** can have less geometry and less texture, less information in it.  
**Translation:** 

**[3596.66s] English:** Yeah.  
**Translation:** 

**[3597.00s] English:** Yeah, that's right.  
**Translation:** 

**[3598.04s] English:** But there's a lot of challenges like that.  
**Translation:** 

**[3599.58s] English:** It turns out...  
**Translation:** 

**[3600.00s] English:** It's a lot easier to render one frame that looks perfect  
**Translation:** Vocabulary: render: 渲染

**[3602.32s] English:** than it is to render a series of frames in motion that look perfect.  
**Translation:** 

**[3607.48s] English:** A lot of the problems with the earlier algorithms  
**Translation:** 

**[3609.64s] English:** that aspired to do this sort of thing was popping.  
**Translation:** 

**[3613.50s] English:** You'd be running some number of triangles for a while  
**Translation:** Vocabulary: triangles: 三角形

**[3615.96s] English:** and then you'd switch to a different number of triangles  
**Translation:** 

**[3617.68s] English:** and you'd see a visible transition  
**Translation:** 

**[3619.12s] English:** and the screen would look like it got shaken up.  
**Translation:** 

**[3622.82s] English:** It's a disturbing artifact that distracts you from the game.  
**Translation:** Vocabulary: artifact: 瑕疵; distracts: 分散注意力

**[3625.68s] English:** So one of the magical trade-offs of Danite  
**Translation:** 

**[3627.92s] English:** was how to avoid all of the visible transitions  
**Translation:** Vocabulary: transitions: 变换过程

**[3630.58s] English:** and get them down to a point where,  
**Translation:** 

**[3634.34s] English:** though they exist statistically,  
**Translation:** 

**[3636.24s] English:** they're not really perceptible to a person looking at it.  
**Translation:** 

**[3638.84s] English:** You look at something like Danite,  
**Translation:** Vocabulary: danite: 丹イト; perceptible: 可感知的

**[3640.56s] English:** I mean, there's a nice blog post,  
**Translation:** 

**[3642.14s] English:** there's nice descriptions about the details,  
**Translation:** 

**[3643.74s] English:** but you can tell even under the details  
**Translation:** 

**[3645.56s] English:** there's just incredible engineering that goes on.  
**Translation:** 

**[3648.20s] English:** It's so cool.  
**Translation:** 

**[3648.72s] English:** It's so cool how underneath this,  
**Translation:** 

**[3652.22s] English:** the actual experience of beautiful detailed scenery,  
**Translation:** 

**[3657.92s] English:** there's just incredible engineering  
**Translation:** 

**[3659.76s] English:** to bring to you simulation,  
**Translation:** 

**[3662.72s] English:** ultra-realistic simulation of reality in real time,  
**Translation:** Vocabulary: simulation: 模拟

**[3666.80s] English:** like lights changing everything.  
**Translation:** 

**[3669.86s] English:** And then it just takes you back  
**Translation:** 

**[3671.62s] English:** to that feeling I had with Wolfenstein,  
**Translation:** 

**[3674.98s] English:** but like more.  
**Translation:** Vocabulary: wolfenstein: 狼穴行动

**[3676.78s] English:** And you can completely lose yourself in that world  
**Translation:** 

**[3679.32s] English:** and you would forget that this real world exists.  
**Translation:** 

**[3682.44s] English:** What is the real world anyway?  
**Translation:** 

**[3683.84s] English:** So that coupling of great engineering  
**Translation:** 

**[3687.56s] English:** and...  
**Translation:** 

**[3687.92s] English:** And great storytelling in terms of just feeling  
**Translation:** Vocabulary: storytelling: 讲故事的艺术

**[3690.84s] English:** is super cool.  
**Translation:** 

**[3692.24s] English:** It's great to know.  
**Translation:** 

**[3693.42s] English:** It's great to know that there's these teams behind it.  
**Translation:** 

**[3696.74s] English:** And it's cool that you're also releasing  
**Translation:** 

**[3698.54s] English:** a bunch of details around it.  
**Translation:** 

**[3700.32s] English:** At least for folks like me,  
**Translation:** 

**[3701.62s] English:** it's inspiring to see.  
**Translation:** 

**[3704.94s] English:** So Unreal Engine is this fascinating creation.  
**Translation:** 

**[3709.00s] English:** It's a big, bold, crazy bet that you made.  
**Translation:** 

**[3711.22s] English:** Maybe it's good to actually explain  
**Translation:** 

**[3712.44s] English:** what Unreal Engine is for people sort of outside this world.  
**Translation:** 

**[3717.28s] English:** I would say it...  
**Translation:** 

**[3720.00s] English:** transform the gaming industry but that was a big bet in 1995 that uh most of the effort  
**Translation:** 

**[3726.96s] English:** would be on creating the gaming engine not the game yeah unreal engine is a big bundle of code  
**Translation:** Vocabulary: bundle: 捆绑软件

**[3734.74s] English:** and tools a huge software package um that provides all the functions you need to build any sort of a  
**Translation:** 

**[3741.54s] English:** 3d graphics application um game developers use it to make games and that's the predominant use  
**Translation:** Vocabulary: predominant: 主要的

**[3747.24s] English:** but it's also used in hollywood film and television production to create 3d scenery  
**Translation:** 

**[3752.34s] English:** in real time for production sets to do pre-visualization it's used by car makers  
**Translation:** 

**[3759.26s] English:** to visualize their cars before they're constructed or manufactured it's used by architects to  
**Translation:** 

**[3766.28s] English:** preview buildings before they're made and industrial designers of all sorts and it provides  
**Translation:** Vocabulary: designers: 设计师; visualize: 可视化

**[3771.76s] English:** you know the all the 3d simulation features you need both for creating highly realistic 3d  
**Translation:** 

**[3777.06s] English:** graphics and for creating 3d graphics and for creating 3d graphics and for creating 3d graphics  
**Translation:** 

**[3777.24s] English:** but also physics and interactions between objects and making things happen like you might  
**Translation:** 

**[3783.76s] English:** see in the real world and supports a huge variety of styles from  
**Translation:** 

**[3787.96s] English:** pixar stylized movies to cell shading to photorealism and it can be used for anything  
**Translation:** 

**[3795.18s] English:** that needs a needs real-time 3d graphics including humans that populate those three-dimensional  
**Translation:** Vocabulary: photorealism: 照片写实主义; stylized: 风格化

**[3800.60s] English:** worlds and we'll probably talk a bunch of the details involved in the  
**Translation:** 

**[3807.06s] English:** uh in the process of creation creating ultra realistic humans because we humans care about  
**Translation:** Vocabulary: ultra: 超乎寻常的

**[3813.66s] English:** how other humans look and how they convey emotion and express how they speak all that kind of stuff  
**Translation:** 

**[3819.48s] English:** but so yes it's the 3d objects that are static the 3d objects that are dynamic and uh on the  
**Translation:** 

**[3828.78s] English:** dynamic front including humans that are ultra dynamic so all of that you have to create this  
**Translation:** 

**[3836.38s] English:** engine that's going to be able to create this engine that's going to be able to create this  
**Translation:** 

**[3837.06s] English:** engine that's going to be able to create this engine that simulates that world the world as we  
**Translation:** 

**[3840.00s] English:** this beautiful world that we know and love okay so that but you know you're early so here you see  
**Translation:** Vocabulary: simulates: 模仿

**[3847.20s] English:** doom and you're trying to create this world and trying to create an engine that would not just  
**Translation:** 

**[3852.32s] English:** power unreal the video game but future video games so how do you go about it what are you thinking  
**Translation:** 

**[3859.14s] English:** and that that i should sort of linger on that that is a crazy bet that we're going to build an engine  
**Translation:** 

**[3864.66s] English:** as a company yeah well you know the philosophy began with zzt and continued onward um we're not  
**Translation:** 

**[3872.90s] English:** just building a game for players to play we're also building tools that could be used for for  
**Translation:** 

**[3879.14s] English:** building that game or any other game and catering to all the artists and designers who had used the  
**Translation:** Vocabulary: catering: 迎合需求

**[3884.40s] English:** tool and so that philosophy started at the very early parts of unreal development um i was building  
**Translation:** 

**[3891.58s] English:** the tools uh for you know level designers  
**Translation:** Vocabulary: designers: 设计师

**[3894.64s] English:** like cliff bozinski and artists like james schmaltz um and uh you know as we began marketing  
**Translation:** 

**[3901.08s] English:** the game thinking it was six months away we were constantly uh releasing screenshots and things  
**Translation:** Vocabulary: bozinski: 博金斯基; schmaltz: 施马尔茨

**[3905.72s] English:** like that um other companies started calling us and saying they wanted to build 3d games too  
**Translation:** 

**[3910.20s] English:** um but they didn't have the expertise for that and they wanted to license our 3d engine um and  
**Translation:** 

**[3916.06s] English:** this was one of the coolest uh pivots in epics history uh microprose called up mark rain or  
**Translation:** 

**[3922.06s] English:** you know vice president and longtime uh  
**Translation:** Vocabulary: epics: 史诗; longtime: 长期; microprose: 微程序; pivots: 转折点

**[3924.64s] English:** business guy and uh said they wanted to license our engine and mark rain was like oh  
**Translation:** 

**[3928.96s] English:** what you want to license what what an engine what's the what what engine and they explained  
**Translation:** 

**[3933.74s] English:** to him what they wanted to license he said oh that engine yeah yeah that's very expensive  
**Translation:** 

**[3936.72s] English:** but uh this was one of the critical things that kept epic going through that three and a half  
**Translation:** 

**[3942.70s] English:** years uh we're starting to license our engine out to other developers microprose took two licenses  
**Translation:** 

**[3948.40s] English:** and we got in half a million dollars from that um and uh company gt interactive licensed  
**Translation:** Vocabulary: interactive: 互动的

**[3954.64s] English:** our engine uh to build uh another game and uh we got paid for that and so we  
**Translation:** 

**[3960.00s] English:** We had this revenue stream funding the development of Unreal Engine from other games that were being built by other developers.  
**Translation:** 

**[3965.58s] English:** And because they were the lifeline for the company, we took the engine business very seriously from the start.  
**Translation:** 

**[3971.60s] English:** We set up mailing lists so that our partners could ask us questions.  
**Translation:** Vocabulary: lifeline: 生命线

**[3976.54s] English:** And all the developers and artists working on our games were participating and helping customers.  
**Translation:** 

**[3981.92s] English:** Everybody took that very seriously because it was our funding source.  
**Translation:** 

**[3984.76s] English:** And that's kind of set this dual spirit of Epic of building technology and supporting game developers simultaneous with building games and supporting gamers.  
**Translation:** 

**[3993.44s] English:** It's continued onward and just grown over time.  
**Translation:** Vocabulary: onward: 向前; simultaneous: 同时

**[3996.76s] English:** Can you just go back to that, you programming?  
**Translation:** 

**[4000.28s] English:** What are some interesting technical challenges you had to overcome?  
**Translation:** 

**[4003.28s] English:** You mentioned dynamic lighting.  
**Translation:** 

**[4005.14s] English:** Create this three-dimensional world and try to figure out the puzzle of how you actually do that.  
**Translation:** 

**[4011.36s] English:** At a time when nobody...  
**Translation:** 

**[4013.36s] English:** Carmack and you doing this kind of thing.  
**Translation:** 

**[4019.14s] English:** It's a totally open wild west.  
**Translation:** 

**[4022.08s] English:** So what are some interesting technical challenges you had to try to solve?  
**Translation:** 

**[4026.80s] English:** There's a lot.  
**Translation:** 

**[4028.04s] English:** Some of them are visible on screen and some are behind the scenes and still require a lot of innovation.  
**Translation:** 

**[4034.24s] English:** All the graphical techniques were really interesting challenges.  
**Translation:** 

**[4038.64s] English:** And Unreal Engine, in those early days, went a lot further.  
**Translation:** Vocabulary: graphical: 图形的

**[4043.36s] English:** And the Quake Engine and building environments using constructive solid geometry with a real-time editor.  
**Translation:** 

**[4049.64s] English:** And that was a really interesting technical challenge.  
**Translation:** Vocabulary: environments: 环境; geometry: 几何

**[4053.78s] English:** The idea is building is extremely tedious if you are only adding objects to the world.  
**Translation:** 

**[4061.16s] English:** If you want to build a door, then you need to add a dozen different pieces of door frames and add a bunch of different walls together to fit together in the right shape.  
**Translation:** Vocabulary: tedious: 单调乏味

**[4067.52s] English:** It sure would be easier if you could just start with a wall and subtract the door out.  
**Translation:** 

**[4072.22s] English:** And so we had this way of...  
**Translation:** Vocabulary: subtract: 减去

**[4073.36s] English:** Adding geometry to the world and subtracting geometry.  
**Translation:** 

**[4075.84s] English:** And the engine would perform all of the calculations on that.  
**Translation:** Vocabulary: subtracting: 减去

**[4080.00s] English:** And this is something that I'd been anticipating was possible for a long time.  
**Translation:** 

**[4084.58s] English:** But when I finally got around to it, it took this 30-hour coding session to figure out all the special cases of the code that needed to be implemented to make that work.  
**Translation:** Vocabulary: anticipating: 预期已久

**[4093.22s] English:** But in the course of 30 hours, I got Constructive Solid Geometry up and running.  
**Translation:** 

**[4098.52s] English:** I started doing that, handed it to James Schmaltz the next time we were together.  
**Translation:** 

**[4103.06s] English:** And then I was like, OK, I think you're cheating here.  
**Translation:** 

**[4105.10s] English:** So you create a giant torus and then add another giant torus interlocked with it.  
**Translation:** 

**[4110.14s] English:** And then subtracted a cylinder from it and created this really advanced composite object with just three operations.  
**Translation:** 

**[4117.50s] English:** He was like, whoa, I can't believe this.  
**Translation:** Vocabulary: composite: 复合; cylinder: 圆柱; subtracted: 减去

**[4118.90s] English:** It's like, yeah, we figured it out.  
**Translation:** 

**[4121.50s] English:** And that was cool to see for the first time.  
**Translation:** 

**[4123.34s] English:** It was probably the first time somebody had done Constructive Solid Geometry in real time.  
**Translation:** 

**[4127.24s] English:** But it was also a really useful artist tool that all the artists appreciated and immediately began making use of.  
**Translation:** 

**[4132.54s] English:** Can you actually speak to that, the 30-hour session?  
**Translation:** 

**[4134.84s] English:** I mean, this is not, from everything I know about computational geometry, doing this kind of thing.  
**Translation:** Vocabulary: computational: 计算的

**[4139.06s] English:** From your perspective, that's not easy.  
**Translation:** 

**[4143.46s] English:** That's, what is it, the uncertainty, the open questions involved, the, like, I mean, even just on the algorithm front, how to do that efficiently.  
**Translation:** Vocabulary: algorithm: 算法; efficiently: 高效地

**[4158.36s] English:** And then plus the usual programming thing of debugging, like suffering through the trickiness of it.  
**Translation:** 

**[4165.96s] English:** And we don't have really, at that time, you don't have the tooling.  
**Translation:** Vocabulary: trickiness: 复杂性

**[4169.06s] English:** You don't have the tooling to really visualize everything that's going on really well.  
**Translation:** 

**[4172.30s] English:** And you probably, like, are using some crappy editor.  
**Translation:** Vocabulary: crappy: 糟糕的; visualize: 可视化

**[4174.72s] English:** I mean, there's just a lot of, like, friction here.  
**Translation:** 

**[4177.58s] English:** So the 30-hour session is one that's probably rough.  
**Translation:** 

**[4182.36s] English:** It's a rough one.  
**Translation:** 

**[4184.30s] English:** Your brain works in different ways depending on your state, right?  
**Translation:** 

**[4189.32s] English:** Right.  
**Translation:** 

**[4189.70s] English:** There are some things that require really working on a problem fresh, where you've put together a bunch of logical pieces.  
**Translation:** 

**[4197.00s] English:** And now you just need to write a whole lot of code.  
**Translation:** 

**[4199.06s] English:** It all works.  
**Translation:** 

**[4200.00s] English:** together and you know plumb a whole lot of data between a whole lot of different algorithms um  
**Translation:** 

**[4205.44s] English:** but you know i think our brains have vastly more horsepower than we're able to  
**Translation:** Vocabulary: horsepower: 动力; plumb: 深入

**[4210.16s] English:** directly access by thinking of what code to type next um and you know after you've been working  
**Translation:** 

**[4218.16s] English:** for a very long time you can get into a sleep deprived state where you have much much more  
**Translation:** 

**[4222.54s] English:** direct access to that low level knowledge that's great yeah you know because you know there's  
**Translation:** 

**[4227.72s] English:** symptoms they're well studied of sleep deprivation one of them is um short-term memory loss and so  
**Translation:** Vocabulary: deprivation: 剥夺

**[4232.04s] English:** you're working without like the easy recall of the code you just typed uh but your brain is then  
**Translation:** 

**[4237.76s] English:** freed to to think about other problems and uh and you know i'd build up this intuition over a very  
**Translation:** Vocabulary: intuition: 直觉

**[4243.32s] English:** long period of time you know so the foundation for the subject is the binary space partitioning  
**Translation:** 

**[4249.06s] English:** tree this data structure invaded by a computer science graphics researcher bruce nailer carmack  
**Translation:** Vocabulary: binary: 二进制; partitioning: 划分

**[4254.58s] English:** had picked up on that and had used the technique in  
**Translation:** 

**[4257.28s] English:** in  
**Translation:** 

**[4257.70s] English:** doom uh to really great effect um and and i picked up on that and the underlying was using  
**Translation:** 

**[4263.36s] English:** this technique for all of its graphics and rendering but it uh yeah it was just additive  
**Translation:** Vocabulary: additive: 累加的

**[4268.10s] English:** geometry everywhere and it had a lot of overlapping polygons and was pretty inefficient um  
**Translation:** 

**[4272.60s] English:** you know so i had the idea that if we had a bsp tree there was a really efficient way to do  
**Translation:** Vocabulary: geometry: 几何; inefficient: 低效; overlapping: 重叠; polygons: 多边形

**[4276.82s] English:** constructive solid geometry and to do that you had to break down the ways that different pieces  
**Translation:** 

**[4282.24s] English:** of geometry can fit together i broke it down into like 14 different cases um and most of the cases  
**Translation:** 

**[4287.70s] English:** are pretty simple crank them out um anyways i got towards the end you know there were some pretty  
**Translation:** 

**[4292.56s] English:** complicated things like what how do you do with coplanar polygons they're in the same plane yeah  
**Translation:** Vocabulary: coplanar: 在同一平面; crank: 生产

**[4297.58s] English:** and pointing in the same direction versus the other direction in what cases should you keep  
**Translation:** 

**[4301.54s] English:** them in what cases should you eliminate them and and so on and so on to create really efficient  
**Translation:** 

**[4305.50s] English:** geometry output and you know just plowing through it uh eventually through mostly a deduction but  
**Translation:** 

**[4312.78s] English:** some trial and error to like sometimes you just have to try the possibilities and see what works  
**Translation:** Vocabulary: deduction: 推理; plowing: 钻研

**[4317.70s] English:** yeah i cranked it out and it worked and the next  
**Translation:** 

**[4320.00s] English:** day i came in like kind of weary and i was like oh wow this actually did work it wasn't just a dream  
**Translation:** 

**[4324.34s] English:** so you're considering the edge cases also i mean that's the problem with geometry is like  
**Translation:** 

**[4328.38s] English:** there's probably just gonna be all kinds of weird polygons that you have to see you're like thinking  
**Translation:** 

**[4333.10s] English:** you're imagining the edge cases and trying to see how do i not create inefficiencies in this  
**Translation:** 

**[4340.72s] English:** algorithm while still considering the edge cases allowing for the edge cases yeah you know it's  
**Translation:** Vocabulary: algorithm: 算法; inefficiencies: 低效性

**[4345.86s] English:** pretty easy to write software that's like 99 correct it's the one percent that's the really  
**Translation:** 

**[4351.16s] English:** hard part and where the devil lies in the details what about like lighting is there other interesting  
**Translation:** 

**[4357.66s] English:** well the funny answer is like we know the laws of physics so it's actually really easy to do  
**Translation:** 

**[4362.60s] English:** everything in computer graphics but uh the direct solution of the laws of physics is immensely slow  
**Translation:** Vocabulary: immensely: 极其

**[4368.94s] English:** and so what we're finding are approximations rather than complete solutions um because you  
**Translation:** 

**[4374.48s] English:** need something that's a million times faster  
**Translation:** Vocabulary: approximations: 近似解

**[4375.86s] English:** than the brute force answer we should say that the the physics of the scene is you just take a  
**Translation:** 

**[4382.44s] English:** bunch of photons bounce them around that's how light works yeah that's going to be very inefficient  
**Translation:** Vocabulary: brute: 粗暴; photons: 光子

**[4387.66s] English:** because there's it's a lot of bouncing and a lot of photons yeah yeah photon tracing is the subject  
**Translation:** 

**[4394.26s] English:** matter that does brute force calculation of pixels on a screen from all of the light in the scene and  
**Translation:** Vocabulary: bouncing: 反射; photon: 光子; pixels: 像素

**[4400.14s] English:** it works and it's correct and it just is an implementation of laws of physics and it's  
**Translation:** 

**[4405.04s] English:** millions or billions of times faster than the brute force answer we should say that the physics of  
**Translation:** Vocabulary: implementation: 实现

**[4405.84s] English:** the scene is millions or billions of times slower than what we do but carmack had figured out uh how  
**Translation:** 

**[4410.16s] English:** to do uh really cool lighting algorithms including real-time lighting with objects moving around um  
**Translation:** 

**[4416.42s] English:** and uh i hadn't taken it very far so with unreal engine i'd i'd realize like it's we don't have  
**Translation:** 

**[4423.18s] English:** nearly enough computing performance on our cpu to compute the light of every pixel on the screen  
**Translation:** Vocabulary: computing: 计算; pixel: 像素

**[4428.88s] English:** from all the light sources that affect it um yeah we're at a six cycle texture mapper and we couldn't  
**Translation:** 

**[4434.64s] English:** afford 30 more cycles and we couldn't afford 30 more cycles and we couldn't afford 30 more cycles  
**Translation:** 

**[4435.84s] English:** for lighting and so the answer had to be some approximation and uh  
**Translation:** 

**[4440.00s] English:** The one that Carmack had picked up on in the Quake engine was light mapping.  
**Translation:** Vocabulary: approximation: 近似值

**[4443.78s] English:** Instead of calculating all the lighting on every pixel,  
**Translation:** 

**[4447.06s] English:** what if we made a big texture that we placed over all the walls in the scene that was like wallpaper?  
**Translation:** Vocabulary: wallpaper: 墙纸

**[4453.12s] English:** And what if we say at every foot, we're going to compute a lighting value  
**Translation:** 

**[4455.80s] English:** for just that one foot grid on the object rather than computing it everywhere?  
**Translation:** 

**[4461.68s] English:** And then what if we just linear interpolate that over the course of it?  
**Translation:** 

**[4465.64s] English:** You know, you get a lighting solution that actually works pretty well  
**Translation:** Vocabulary: interpolate: 插值

**[4469.18s] English:** and is fast enough to work.  
**Translation:** 

**[4471.14s] English:** And so a lot of Unreal Engine's lighting techniques were based on light mapping.  
**Translation:** 

**[4474.44s] English:** We introduced colored lighting.  
**Translation:** 

**[4476.60s] English:** So you could have colored light sources.  
**Translation:** 

**[4478.48s] English:** Then we realized, oh, since we're doing this and we're doing it on light maps,  
**Translation:** 

**[4481.64s] English:** we can actually do some pretty expensive calculations, hundreds of cycles,  
**Translation:** 

**[4484.94s] English:** since we're only calculating it for every one foot of world space rather than every pixel.  
**Translation:** 

**[4489.56s] English:** And so we introduced a whole bunch of elaborate lighting effects,  
**Translation:** Vocabulary: elaborate: 复杂细致的

**[4492.82s] English:** like torch flickering and, you know, the caustic effects of water bouncing off of the surface.  
**Translation:** 

**[4499.18s] English:** And so on, and pulsing lights and blinking lights and everything else,  
**Translation:** Vocabulary: blinking: 闪烁; caustic: 腐蚀性; flickering: 闪烁

**[4503.48s] English:** and created a system.  
**Translation:** 

**[4504.26s] English:** I created a system for compositing them together.  
**Translation:** Vocabulary: compositing: 合成

**[4506.30s] English:** So if you had an arbitrary number of light sources, they could all do that.  
**Translation:** 

**[4510.04s] English:** And then I implemented a shadowing algorithm.  
**Translation:** Vocabulary: algorithm: 算法; arbitrary: 任意的

**[4513.88s] English:** You know, if you cast a ray from a light to a point on a surface  
**Translation:** 

**[4518.46s] English:** and see whether it intersects in the other geometry,  
**Translation:** Vocabulary: geometry: 几何; intersects: 相交

**[4521.22s] English:** if it doesn't intersect, then the light hits the object.  
**Translation:** 

**[4523.94s] English:** And if it does intersect, then the light hits something else first.  
**Translation:** Vocabulary: intersect: 相交

**[4527.02s] English:** And that pixel on the object should be darkened.  
**Translation:** 

**[4529.18s] English:** So I built a real-time version of this, and it ran at about a half a frame a second.  
**Translation:** 

**[4536.76s] English:** So I was running around at half a frame a second,  
**Translation:** 

**[4538.88s] English:** like shooting out light projectiles and looking at dynamic lighting.  
**Translation:** Vocabulary: projectiles: 投射物

**[4541.76s] English:** It was like, someday computers will be fast enough for this, but not today.  
**Translation:** 

**[4546.50s] English:** So I made a non-real-time version that pre-calculates all the lighting  
**Translation:** 

**[4549.46s] English:** and realized, oh, wait, if you pre-calculated the shadowing in an object,  
**Translation:** 

**[4552.68s] English:** you can still apply the lighting dynamically as long as the light's not moving.  
**Translation:** 

**[4556.08s] English:** So you could do torch flickering with shadows.  
**Translation:** 

**[4558.62s] English:** And, you know,  
**Translation:** 

**[4559.18s] English:** I figured out all of this.  
**Translation:** 

**[4560.00s] English:** cases of dynamic and static lighting that were actually practical on a computer at the time and  
**Translation:** 

**[4563.84s] English:** expose them to artists and this was the wonderful thing i was just like typing in these little  
**Translation:** 

**[4568.76s] English:** features uh exposing them to artists and every day they'd find like a drop down with some more  
**Translation:** 

**[4573.28s] English:** lighting options available to them and they'd start using them and they do things that i never  
**Translation:** 

**[4576.72s] English:** thought possible and this was always the coolest thing as a programmer building an engine you  
**Translation:** Vocabulary: programmer: 编程人员

**[4581.78s] English:** you might think you know the implications of the feature you're building but artists are so clever  
**Translation:** 

**[4586.90s] English:** that you always find that you've built the capability of doing vastly more than you ever  
**Translation:** Vocabulary: capability: 能力

**[4591.02s] English:** anticipated as they start to use combinations of features together in concert to do ever more  
**Translation:** 

**[4596.02s] English:** amazing things that's the genius of artists is they're given constraints and within those  
**Translation:** Vocabulary: constraints: 限制

**[4600.44s] English:** constraints they create something you could have never possibly imagined given the constraints  
**Translation:** 

**[4605.34s] English:** that's such a beautiful coupling between engineering and artistry and art that's right  
**Translation:** 

**[4612.08s] English:** and it's timeless you know what would the renaissance painters do with paints and what do  
**Translation:** 

**[4616.40s] English:** what do you do with paints and what do you do with paints and what do you do with paints and what do  
**Translation:** Vocabulary: renaissance: 文艺复兴; timeless: 永恒的

**[4616.88s] English:** the early game artists do with uh early engines you know everybody's figuring out the capabilities  
**Translation:** 

**[4622.24s] English:** of their medium and you're seeing a revolution this is blowing my mind this is all fun what  
**Translation:** 

**[4627.66s] English:** about fog you mentioned fog that i don't even know how do you even do fog so you mentioned  
**Translation:** 

**[4633.44s] English:** unreal so the first version had fog yeah it was a funny thing um uh so this graphics hardware  
**Translation:** 

**[4641.72s] English:** company had just started up in finland and they released a screenshot of what their gpu was doing  
**Translation:** 

**[4646.06s] English:** and they showed a screen shot of what their gpu was doing and they showed a screen shot of what  
**Translation:** 

**[4646.86s] English:** their gpu was doing and they showed a screen shot of what their gpu was doing and they showed a  
**Translation:** 

**[4647.42s] English:** photothelometric fog so you had a foggy room with some light sources in it and when that happens in  
**Translation:** Vocabulary: photothelometric: 光强计量的

**[4653.12s] English:** the real world what you see are glows around the lights as the light brightens the fog around it  
**Translation:** 

**[4658.16s] English:** but the brightening of the fog diminishes over time because the fog absorbs some lighting and  
**Translation:** Vocabulary: diminishes: 减弱

**[4662.12s] English:** so the further you get away from the light the more uh the more fall off there is and you know  
**Translation:** 

**[4667.36s] English:** you have a bunch of colored lights overlapping together in a space like that the effect is just  
**Translation:** Vocabulary: overlapping: 重叠

**[4671.52s] English:** absolutely magical you know like being out on a foggy light with street lamps above it's something  
**Translation:** 

**[4676.86s] English:** surreal and look just beautiful so it's like oh my god they figured out how to do  
**Translation:** Vocabulary: surreal: 超现实的

**[4680.00s] English:** real-time value metric fog i have to figure it out myself and so that was another like 30 hour  
**Translation:** 

**[4685.10s] English:** coding session um nice but but like at the core i realized okay what's happening here is we have  
**Translation:** 

**[4691.24s] English:** this lighting function i'm saying the light at a particular point in space is like you know  
**Translation:** 

**[4697.32s] English:** falling off with the inverse square of the light uh light the distance from the light source right  
**Translation:** Vocabulary: inverse: 反比

**[4701.90s] English:** the inverse square is all from isaac newton which applies to lighting i had to realize was that the  
**Translation:** 

**[4707.08s] English:** way the fog interacted with the light was that you calculate the view from your eye's position  
**Translation:** Vocabulary: interacted: 相互作用

**[4712.06s] English:** to a point on the surface in the world um it's going through fog and you're accumulating more  
**Translation:** 

**[4716.22s] English:** and more light as a function of the amount of light illuminating the fog at that point in time  
**Translation:** Vocabulary: accumulating: 累积; illuminating: 照射

**[4720.74s] English:** and so well you know i'd studied that in mechanical engineering without even knowing it that's the  
**Translation:** 

**[4726.70s] English:** line integral you know you have an integral over a line of some function well this is exactly what  
**Translation:** Vocabulary: integral: 积分

**[4730.90s] English:** it's for it's for accumulating values of a function over a continuous space and time and  
**Translation:** 

**[4735.68s] English:** you know i  
**Translation:** 

**[4737.08s] English:** did a bunch of math and uh realized that oh wow the integral uh and i looked in a reference book  
**Translation:** 

**[4742.16s] English:** of all the integrals and you know thankfully people had solved them all and i realized the  
**Translation:** Vocabulary: integrals: 积分

**[4746.06s] English:** integral of you know this transformed one over r squared is turns out to be solved by the arc  
**Translation:** 

**[4751.66s] English:** tangent of r uh and so you know if you calculate the some parameters based on the position of the  
**Translation:** Vocabulary: tangent: 正切

**[4758.48s] English:** eye and the position of the surface uh point you're ultimately seeing um then you calculate  
**Translation:** 

**[4763.24s] English:** exactly how much fog you can accumulate from that but of course you can't do that  
**Translation:** 

**[4767.02s] English:** perfectly you can't do that perfectly you can't do that perfectly you can't do that perfectly  
**Translation:** 

**[4767.06s] English:** per pixel because that's hundreds of cycles of cpu time and so what we had to do is calculate  
**Translation:** Vocabulary: pixel: 像素

**[4771.60s] English:** volumetric fog on um on something equivalent to a light map but uh calculating fog every square  
**Translation:** 

**[4778.42s] English:** meter in the world um and so you know we had enough performance for that built uh volumetric  
**Translation:** Vocabulary: volumetric: 体积的

**[4784.42s] English:** lighting and gave it to the artists and they started building magically detailed levels  
**Translation:** 

**[4788.14s] English:** with volumetric fog and in real time and then um you know decades later i was talking to one of the  
**Translation:** 

**[4793.98s] English:** engineers who'd worked on that hardware and asked about their volumetric fog  
**Translation:** 

**[4797.06s] English:** and told him how it inspired me to um uh  
**Translation:** 

**[4800.00s] English:** to you know figure out how to do it in real time myself he was like oh no we cheated we just  
**Translation:** 

**[4804.62s] English:** rendered it out of 3d studio max that's awesome that is so awesome that is so inspiring on so  
**Translation:** 

**[4809.94s] English:** many levels yeah that you saw that maybe it's possible even if it was kind of smoke and mirrors  
**Translation:** 

**[4816.60s] English:** and then you actually made it happen it's so it's so inspiring to hear these kind of stories when  
**Translation:** 

**[4822.94s] English:** when there's so much uncertainty and you figure out and so many constraints and you figure out  
**Translation:** 

**[4828.26s] English:** how to bring it to life in real time and create this this world that unreal did um maybe if we  
**Translation:** Vocabulary: constraints: 限制条件

**[4833.48s] English:** could just pause since you mentioned john carmack a few times as a fellow pioneer in the game  
**Translation:** 

**[4839.28s] English:** industry at that time what do you admire about john john singularly has this intense dedication  
**Translation:** Vocabulary: dedication: 专注

**[4848.22s] English:** to getting the best result from his code and having absolutely no attachment to pass code  
**Translation:** 

**[4857.26s] English:** and sometimes  
**Translation:** 

**[4858.26s] English:** the legendary things he did the end result was an absolute breakthrough in real-time computer  
**Translation:** 

**[4863.04s] English:** graphics weren't his first try they were like his seventh or eighth try after he'd done something  
**Translation:** 

**[4869.06s] English:** time and time again tried it found a better approach thrown out the old one built it again  
**Translation:** 

**[4874.08s] English:** and continually rewrote his code until he found the absolute best solution to a problem  
**Translation:** 

**[4877.88s] English:** and you know i think that that stands as a lesson for every programmer to pick up on when something  
**Translation:** 

**[4883.56s] English:** is really really important um its performance is absolutely critical to the  
**Translation:** 

**[4888.26s] English:** or its quality or its capabilities just iterate on it until you've achieved perfection and don't  
**Translation:** 

**[4895.30s] English:** settle for the first or second solution is good enough and it's you know the result of that both  
**Translation:** 

**[4902.20s] English:** you and him sort of define the future of gaming of gaming worlds it's so beautiful to see it's like  
**Translation:** 

**[4909.34s] English:** it's just fascinating it's inspiring because like under so much uncertainty under so many  
**Translation:** 

**[4915.04s] English:** constraints you figure out you figure out a way  
**Translation:** 

**[4918.26s] English:** and that you know actually continues to  
**Translation:** 

**[4920.00s] English:** this day because yes the hardware is improved incredibly but in order to create an ultra  
**Translation:** 

**[4928.94s] English:** realistic uh highly dynamic real-time rendering of the world around us it's still really really  
**Translation:** Vocabulary: ultra: 超凡

**[4935.98s] English:** difficult and there's all these kinds of optimization like you mentioned maybe you can  
**Translation:** 

**[4940.20s] English:** speak to that unreal engine one journey from one to 5.5 or 0.6 now uh what for for 30 years  
**Translation:** Vocabulary: optimization: 优化

**[4951.82s] English:** you've been creating virtual worlds what's it like evolving a game engine for those 30 years  
**Translation:** 

**[4958.82s] English:** when they're when the hardware under you is is improving exponentially what are some things  
**Translation:** Vocabulary: evolving: 不断进化; exponentially: 指数地

**[4965.16s] English:** that changed and what are some universal truths that have not changed  
**Translation:** 

**[4969.08s] English:** it's been a lot of fun  
**Translation:** 

**[4970.18s] English:** it's been an astonishing experience nobody 30 years ago had anticipated that we'd see  
**Translation:** 

**[4974.98s] English:** the performance gains in hardware that we've actually seen that time frame it's something like  
**Translation:** Vocabulary: astonishing: 令人惊讶的

**[4979.48s] English:** a hundred thousand times higher cpu performance between multiple cores and higher clock rates  
**Translation:** 

**[4984.50s] English:** and more parallelism like you know if if we had an aviation then we'd be like taking a trip to  
**Translation:** 

**[4990.60s] English:** neighboring stars off of zentari yeah exactly um and uh in in graphics it's been even more so  
**Translation:** 

**[4998.70s] English:** it's something like literally  
**Translation:** Vocabulary: neighboring: 相邻的

**[4999.74s] English:** 10 years ago  
**Translation:** 

**[5000.16s] English:** 10 million times more net usable gpu performance than we had uh back running on a penny m90 cpu  
**Translation:** Vocabulary: usable: 可用的

**[5006.38s] English:** um all in 30 years and um you know it's really made me appreciate that over the generations  
**Translation:** 

**[5013.16s] English:** some areas of our engine development have absolutely kept up with technology um and  
**Translation:** 

**[5019.24s] English:** you know the the rendering team that works on unreal engine are the real miracle workers there  
**Translation:** 

**[5022.98s] English:** just about every generation of unreal uh we've replaced most of the rendering code  
**Translation:** 

**[5029.04s] English:** um  
**Translation:** 

**[5030.16s] English:** and you know the the different leaders and different points and times and the different  
**Translation:** 

**[5034.52s] English:** luminaries have built systems that were absolutely rethought um and optimized  
**Translation:** 

**[5040.00s] English:** for the latest generation of hardware.  
**Translation:** Vocabulary: luminaries: 知名人士; optimized: 优化

**[5042.78s] English:** Unreal Engine 1 was built for software rendering,  
**Translation:** 

**[5045.16s] English:** and then the Voodoo 1 came along late in the cycle,  
**Translation:** Vocabulary: voodoo: oodoo

**[5047.36s] English:** and we had support for it, but it wasn't fully capable and utilized.  
**Translation:** 

**[5052.32s] English:** Unreal Engine 2 was about bringing all the latest GPU hardware acceleration features  
**Translation:** Vocabulary: acceleration: 硬件加速; utilized: 被利用

**[5056.40s] English:** to the engine and keeping forward and building some new features  
**Translation:** 

**[5059.64s] English:** like vehicles and a few other capabilities.  
**Translation:** 

**[5065.26s] English:** And this was in the early GPU era,  
**Translation:** 

**[5067.40s] English:** before GPUs had really broken out of everybody's expectations of Moore's Law.  
**Translation:** 

**[5074.10s] English:** But that breakout occurred with DirectX 9  
**Translation:** 

**[5076.32s] English:** and the capabilities of programmable shaders.  
**Translation:** Vocabulary: breakout: 突然爆发; shaders: 着色器

**[5079.36s] English:** Once you had control of writing code running on the GPU  
**Translation:** 

**[5082.16s] English:** that could color every pixel on the screen,  
**Translation:** Vocabulary: pixel: 屏幕像素

**[5085.26s] English:** and that GPU code was literally a factor of 100 times faster  
**Translation:** 

**[5088.56s] English:** than the equivalent code I wrote a few years earlier on the Pentium 90.  
**Translation:** 

**[5094.10s] English:** And so that DirectX 9 generation  
**Translation:** 

**[5096.72s] English:** was a great example of how we could do that.  
**Translation:** 

**[5097.40s] English:** A godsend.  
**Translation:** 

**[5098.56s] English:** And Andrew Scheiderker, a longtime Epic Luminary,  
**Translation:** Vocabulary: godsend: 意外之财; longtime: 长期的; luminary: 名人

**[5101.26s] English:** wrote the core of the Unreal Engine 3 render  
**Translation:** 

**[5104.24s] English:** around real-time pixel shading, real-time lighting,  
**Translation:** Vocabulary: render: 渲染

**[5109.34s] English:** being able to do dynamic shadows using several different techniques,  
**Translation:** 

**[5113.56s] English:** and multi-thread the render to support bits of the early dual-core CPUs  
**Translation:** 

**[5120.20s] English:** that were starting to show up at the time.  
**Translation:** 

**[5123.02s] English:** And it was a massive, massive graphical upgrade.  
**Translation:** Vocabulary: graphical: 图形的

**[5125.24s] English:** Unreal Engine 4 made a number of improvements  
**Translation:** 

**[5129.60s] English:** and just continued to add features  
**Translation:** 

**[5131.66s] English:** to give artists more and more options for lighting  
**Translation:** 

**[5135.32s] English:** and for geometry that created realism.  
**Translation:** Vocabulary: geometry: 几何形状

**[5139.36s] English:** But then I think probably our biggest single level of leap  
**Translation:** 

**[5143.16s] English:** came with Unreal Engine 5  
**Translation:** 

**[5144.46s] English:** with the Nanite Micropolygon geometry solution  
**Translation:** 

**[5147.72s] English:** and with Lumen, the global illumination lighting solution,  
**Translation:** Vocabulary: illumination: 照明; lumen: 流明; micropolygon: 微多边形

**[5151.44s] English:** which I think really bridged the gap  
**Translation:** 

**[5153.74s] English:** from the original Unreal Engine 5.  
**Translation:** 

**[5154.38s] English:** And I think that's a big thing.  
**Translation:** 

**[5154.56s] English:** And I think that's a big thing.  
**Translation:** 

**[5154.60s] English:** And I think that's a big thing.  
**Translation:** 

**[5154.70s] English:** And I think that's a big thing.  
**Translation:** 

**[5154.78s] English:** And I think that's a big thing.  
**Translation:** 

**[5154.80s] English:** And I think that's a big thing.  
**Translation:** 

**[5154.82s] English:** And I think that's a big thing.  
**Translation:** 

**[5155.24s] English:** And I think that's a big thing.  
**Translation:** 

**[5155.28s] English:** And I think that's a big thing.  
**Translation:** 

**[5155.36s] English:** And I think that's a big thing.  
**Translation:** 

**[5155.78s] English:** And I think that's a big thing.  
**Translation:** 

**[5156.16s] English:** And I think that's a big thing.  
**Translation:** 

**[5156.18s] English:** And I think that's a big thing.  
**Translation:** 

**[5156.28s] English:** And I think that's a big thing.  
**Translation:** 

**[5156.30s] English:** And I think that's a big thing.  
**Translation:** 

**[5156.34s] English:** And I think that's a big thing.  
**Translation:** 

**[5156.40s] English:** And I think that's a big thing.  
**Translation:** 

**[5156.44s] English:** And I think that's a big thing.  
**Translation:** 

**[5156.46s] English:** And I think that's a big thing.  
**Translation:** 

**[5156.52s] English:** And I think that's a big thing.  
**Translation:** 

**[5156.64s] English:** And I think that's a big thing.  
**Translation:** 

**[5156.96s] English:** And I think that's a big thing.  
**Translation:** 

**[5157.02s] English:** And I think that's a big thing.  
**Translation:** 

**[5157.06s] English:** And I think that's a big thing.  
**Translation:** 

**[5157.10s] English:** And I think that's a big thing.  
**Translation:** 

**[5157.16s] English:** And I think that's a big thing.  
**Translation:** 

**[5157.18s] English:** And I think that's a big thing.  
**Translation:** 

**[5157.26s] English:** computer graphics to, you know.  
**Translation:** 

**[5160.00s] English:** total observable photorealism um for artists who wanted to create that um and so that's been  
**Translation:** 

**[5166.54s] English:** the evolution and the progress on the graphics side is absolutely astonishing as it is on the  
**Translation:** Vocabulary: astonishing: 令人惊讶; observable: 可观测的; photorealism: 照片写实主义

**[5171.78s] English:** audio side in a number of other areas but parts of the engine also haven't changed all that much  
**Translation:** 

**[5176.30s] English:** since the version i wrote um and shipped in 1998 um you know the file management system  
**Translation:** 

**[5183.26s] English:** has been optimized a number of times but it hasn't been completely rethought um  
**Translation:** 

**[5187.68s] English:** and the networking system the ways uh that uh clients and servers talk together and negotiate  
**Translation:** 

**[5193.58s] English:** game state uh is still an evolution of the thing i wrote um and you know it's feeling kind of dated  
**Translation:** 

**[5198.90s] English:** now uh you still see networking bugs in fortnite where like for some reason when you're spectating  
**Translation:** Vocabulary: fortnite: 堡垒之夜; spectating: 观战

**[5203.86s] English:** you're not seeing some parameters update well that's uh that's because of the loss lossful  
**Translation:** 

**[5208.20s] English:** nature of that networking model and uh you know and the biggest limitation that's built up over  
**Translation:** 

**[5213.26s] English:** time is the single-threaded nature of game simulation in unreal engine  
**Translation:** 

**[5217.32s] English:** we run a single-threaded simulation you know if you have a 16 core cpu we're using one core  
**Translation:** Vocabulary: simulation: 模拟

**[5222.74s] English:** for game simulation um and running with the complicated game logic because single-thread  
**Translation:** 

**[5227.18s] English:** programming is orders of magnitude easier than multi-thread programming and we didn't want to  
**Translation:** 

**[5232.22s] English:** burden either ourselves or our partners or the community with the complications of multi-threading  
**Translation:** 

**[5237.98s] English:** um and you know over time that becomes an increasing limitation you know so we're really  
**Translation:** 

**[5244.16s] English:** thinking about and working on the next generation of technology  
**Translation:** 

**[5247.32s] English:** and you know being unreal engine six and that's the generation we're actually going to go and  
**Translation:** 

**[5251.88s] English:** address a number of the really core limitations that have been with us over the history of unreal  
**Translation:** 

**[5256.20s] English:** engine and and get those on the you know a better foundation that um in the modern world deserves  
**Translation:** 

**[5262.08s] English:** given everything that's been learned in the field of computing in that time frame that's a  
**Translation:** 

**[5266.64s] English:** terrifyingly challenging uh engineering problem and it seems like every version of unreal engine  
**Translation:** Vocabulary: computing: 计算机; terrifyingly: 令人恐惧地

**[5273.28s] English:** um the amazing teams behind it and the  
**Translation:** 

**[5277.32s] English:** engineers behind it are willing to just throw away most of the code  
**Translation:** 

**[5280.00s] English:** or maybe i'm being a little bit too dramatic but basically throw away the the old approaches like  
**Translation:** 

**[5286.24s] English:** you mentioned with carmack and uh start again like like with nanite and lumen just keep keep  
**Translation:** Vocabulary: lumen: 光线追踪技术

**[5294.40s] English:** optimizing to the current hardware but even like rethinking how it's all done but rethink going  
**Translation:** 

**[5300.80s] English:** from single threaded to multi-threaded oh boy that's terrifying and that's in part we'll talk  
**Translation:** Vocabulary: optimizing: 优化; terrifying: 恐怖; threaded: 线程

**[5306.22s] English:** about it why maybe you have to rethink the even the programming language that's being used  
**Translation:** 

**[5311.24s] English:** to rethink a lot of things that's fascinating can we just stick on the unreal engine 5 so i  
**Translation:** 

**[5317.78s] English:** watched i watched a bunch of stuff but the state of unreal in ggc 2024  
**Translation:** 

**[5322.98s] English:** i can't i was uh uh just giggling with excitement watching some of this stuff  
**Translation:** Vocabulary: giggling: 咯咯笑

**[5330.72s] English:** so just if we can talk about different things here just to nerd out a little bit  
**Translation:** 

**[5336.22s] English:** so people should go watch this video they they they talked about the dirt  
**Translation:** 

**[5340.84s] English:** uh just the ultra realistic and this is for uh marvel 1943 uh which is kind of putting the  
**Translation:** 

**[5350.06s] English:** marvel universe into nazi occupied france uh in the winter so there's snow and you know that  
**Translation:** Vocabulary: marvel: 惊奇; ultra: 超现实

**[5359.76s] English:** that's a moment in history that's a very intense moment in history and it really creates a  
**Translation:** 

**[5366.22s] English:** and puts you there there's so much to that including the snow but just you know looking  
**Translation:** 

**[5372.64s] English:** at the dirt is a really nice way to show like how do you add a lot of details to the scene  
**Translation:** 

**[5382.14s] English:** in real time that like gives this experience like infinite detail like this is real this is  
**Translation:** 

**[5392.98s] English:** super real and then i think in the talk they  
**Translation:** 

**[5396.22s] English:** describe like what it what's entailed in the uh the  
**Translation:** Vocabulary: entailed: 包含

**[5400.00s] English:** the generation of the geometry what's entailed in the lighting all that kind of stuff maybe can you  
**Translation:** 

**[5405.48s] English:** speak about dirt what's what what are what are the components for people who might not know in like  
**Translation:** Vocabulary: geometry: 几何

**[5412.82s] English:** creating this ultra realistic the texture the lighting the geometry all of that like how  
**Translation:** 

**[5419.58s] English:** nanite how lumen all come together in this beautiful orchestra to paint in real time  
**Translation:** Vocabulary: lumen: 光线追踪

**[5424.30s] English:** the dirt in nazi occupied france in 1943 yeah there's a lot happening here on screen and uh  
**Translation:** 

**[5432.54s] English:** you know the real hero of of this image isn't uh epic it's the artists and technical artists who  
**Translation:** 

**[5438.08s] English:** work together to build this environment because it and the reason we showed it at gdc was it went  
**Translation:** 

**[5443.74s] English:** way way beyond what we uh realized the system was capable of doing um you know largely because of  
**Translation:** 

**[5448.86s] English:** their brilliance and this is the magic of computer graphics there's not one feature that makes this  
**Translation:** 

**[5453.54s] English:** cool there's  
**Translation:** Vocabulary: brilliance: 卓越

**[5454.28s] English:** a dozen technical features that each interplay um and because of the ways that they interplay with  
**Translation:** 

**[5460.30s] English:** each other you really don't it's hard to actually identify the individual components of it one thing  
**Translation:** 

**[5466.16s] English:** that's happening here that's really critical oh yeah now we're seeing it being turned off is uh  
**Translation:** 

**[5470.28s] English:** the lighting happening the lumen lighting system that's powering the scene is doing different kinds  
**Translation:** 

**[5477.08s] English:** of lighting calculations at different scales this was the work of uh daniel wright uh following  
**Translation:** 

**[5482.96s] English:** a decade of  
**Translation:** 

**[5484.28s] English:** moving the state of the art of lighting forward but his his theory which uh was rather controversial  
**Translation:** 

**[5490.56s] English:** at the time was that if you have enough uh levels of lighting uh calculation um then you can get  
**Translation:** 

**[5497.60s] English:** everything global illumination working everywhere from the absolute highest levels of a scene you  
**Translation:** 

**[5503.42s] English:** know that buildings are casting correct shadows all the way down to details like you see on the  
**Translation:** 

**[5507.32s] English:** dirt here uh all working in concert and without distinguishable boundaries so there is a good  
**Translation:** 

**[5513.22s] English:** decade of  
**Translation:** 

**[5514.28s] English:** of foundational work there to make the lighting work in particular when you see the very detailed  
**Translation:** 

**[5520.00s] English:** shadows uh interplaying between the you know the ice and the dirt there uh that's screen space  
**Translation:** Vocabulary: foundational: 基础的

**[5525.96s] English:** sliding uh there's actually shadow calculation going on uh not based on the world but on the  
**Translation:** 

**[5534.34s] English:** pixels on the screen uh because that is the only way that we could possibly do those calculations  
**Translation:** Vocabulary: pixels: 屏幕像素

**[5539.18s] English:** fast enough running them in a pixel shader yeah watch this watch the when you add the objects  
**Translation:** 

**[5544.98s] English:** when you add the textures the different layering all the shadows that have to be computed yeah boy  
**Translation:** Vocabulary: computed: 计算; layering: 层叠; pixel: 像素; shader: 着色器

**[5551.28s] English:** that shadowing is the amazing thing but you know the reason that works is counterintuitive when  
**Translation:** 

**[5557.34s] English:** somebody first explained it to me i was like that's really clever but i don't think that will  
**Translation:** Vocabulary: counterintuitive: 违反直觉的

**[5561.10s] English:** work uh yeah but it does work because if you observe uh the positions of incoming lights and  
**Translation:** 

**[5567.40s] English:** uh you know the z coordinates of the different pixels on the screen you can figure out how  
**Translation:** Vocabulary: coordinates: 坐标; incoming: 入射的

**[5571.80s] English:** your geometry there is likely to occlude other  
**Translation:** 

**[5574.80s] English:** you  
**Translation:** Vocabulary: geometry: 几何; occlude: 遮挡

**[5574.98s] English:** and even though it's only an approximation and that isn't perfect uh it looks perfectly good to  
**Translation:** 

**[5580.62s] English:** the human eye and gives you the subtle shadowing um that you see in a scene like this that it makes  
**Translation:** Vocabulary: approximation: 近似

**[5586.82s] English:** it look highly realistic and the shadowing influences other things there's also some  
**Translation:** 

**[5592.82s] English:** really interesting things happening with the color here and i'm not even sure what's causing  
**Translation:** 

**[5597.16s] English:** you know it looks like this color is bleeding from some parts of the snow onto other parts  
**Translation:** 

**[5601.56s] English:** of the snow it looks like there's some subsurface scattering  
**Translation:** Vocabulary: scattering: 散射; subsurface: 次生的

**[5604.80s] English:** going on i'm not even sure if that's being used in this scene and then there's a material layering  
**Translation:** 

**[5610.96s] English:** system for laying down you know layers of material dirt and snow and other things uh all making that  
**Translation:** 

**[5618.60s] English:** work and then there's the light bouncing off of uh the geometry which is another system for lighting  
**Translation:** 

**[5623.74s] English:** on top of the uh global illumination system what about reflections too is that is that count as uh  
**Translation:** Vocabulary: bouncing: 反射; illumination: 照明

**[5630.78s] English:** the light bounce so there's a light bouncing off of stuff to light it up in different interesting  
**Translation:** 

**[5634.64s] English:** ways but then there's also actually literal reflections in like we're looking at a puddle  
**Translation:** Vocabulary: puddle: 水坑

**[5640.00s] English:** in the dirt yeah yeah that's right but the engine supports a number of different reflection  
**Translation:** 

**[5645.12s] English:** techniques one is calculating basically textures that reflect they capture all the lighting in  
**Translation:** 

**[5650.38s] English:** the scene and then bouncing that off of uh texture maps so you can see different lights bouncing off  
**Translation:** 

**[5656.28s] English:** of different pixels in different ways and then there's individual lighting uh casting reflections  
**Translation:** Vocabulary: pixels: 像素

**[5661.18s] English:** off of things too and a lot of this is under the control of designers and you know one of the  
**Translation:** 

**[5666.24s] English:** things that's yet a yet to do problem for the future is uh you don't just like press a few  
**Translation:** Vocabulary: designers: 设计师

**[5671.36s] English:** buttons and this kind of scene magically appears this is a lot of work from some highly skilled  
**Translation:** 

**[5675.68s] English:** people not only building out this particular scene but in setting up the material layers so that you  
**Translation:** 

**[5680.36s] English:** get the dirt with the ice layered on top and all the reflections working and they need to make a  
**Translation:** 

**[5684.70s] English:** number of technical art decisions to make this work and if a novice who hadn't you know worked  
**Translation:** 

**[5690.10s] English:** very hard built the kind of scene like this it wouldn't look nearly as good so one of the  
**Translation:** 

**[5694.18s] English:** challenges we have is to make building this scene a little bit more difficult and i think that's  
**Translation:** 

**[5696.22s] English:** kind of a quality level even easier and more seamless and automatic you'd like to just build  
**Translation:** 

**[5701.16s] English:** a scene and say use this material here and have this appearance come out of it yeah and i mean  
**Translation:** Vocabulary: seamless: 天衣无缝

**[5707.04s] English:** once you create the scene you could do things i remember where they said like can you turn off the  
**Translation:** 

**[5712.22s] English:** headlights uh i forget you could control the lighting i mean all of this we should say  
**Translation:** 

**[5718.24s] English:** like this is dynamic so you can change the position of the light you can turn on the  
**Translation:** 

**[5723.84s] English:** lights and off the lights that's incredible  
**Translation:** 

**[5726.22s] English:** so this is all real time  
**Translation:** 

**[5728.70s] English:** the geometry the lighting the textures all of it real time this is this is the power of  
**Translation:** Vocabulary: geometry: 几何图形

**[5736.78s] English:** awesome technical art three decades of feature development and uh like you have to credit to  
**Translation:** 

**[5742.48s] English:** also to the 20 teraflops of graphics performance that nvidia is delivering thanks nvidia  
**Translation:** 

**[5749.22s] English:** yeah 90 megahertz to this 90 megahertz is 90 megaflops this is 20  
**Translation:** 

**[5756.22s] English:** megaflops that's a big change that's a lot so one of the  
**Translation:** Vocabulary: megahertz: 兆赫兹

**[5760.00s] English:** One of the other things that they talk about in the presentation is about snow.  
**Translation:** 

**[5763.58s] English:** If you're talking about 1943 in Nazi Germany in the winter, you have to create a feeling, one of which is the season, the winter, the cold.  
**Translation:** 

**[5778.04s] English:** You have to cover everything in snow, and here shown is the ability to control how much snow covers the objects.  
**Translation:** 

**[5787.46s] English:** The ability to do that for the artist is incredible.  
**Translation:** 

**[5793.64s] English:** Just to control how much snow is in the scene dynamically like that.  
**Translation:** 

**[5798.80s] English:** That's cool.  
**Translation:** Vocabulary: dynamically: 动态地

**[5800.10s] English:** Yeah.  
**Translation:** 

**[5800.72s] English:** That's really cool.  
**Translation:** 

**[5801.82s] English:** It's a cool system for material layering and a dozen pieces coming together here.  
**Translation:** 

**[5806.02s] English:** You also notice there's fogginess and there's some hot objects emanating fog.  
**Translation:** Vocabulary: emanating: 散发; layering: 分层

**[5810.22s] English:** An artist did that.  
**Translation:** 

**[5811.74s] English:** That didn't just arise automatically.  
**Translation:** 

**[5814.46s] English:** That's called material layering.  
**Translation:** 

**[5816.18s] English:** An artist creates it.  
**Translation:** 

**[5817.48s] English:** Different materials are able to layer the scene with it.  
**Translation:** 

**[5822.70s] English:** Yeah.  
**Translation:** 

**[5822.88s] English:** Layer materials on top of each other and see how much of each material should be protruding in different places with the engine handling transitions and things like that.  
**Translation:** 

**[5830.56s] English:** That's on top of the geometry that creates the structure of the scene and all the occlusions that have to be computed.  
**Translation:** Vocabulary: computed: 计算出的; occlusions: 遮挡; protruding: 突出; transitions: 过渡

**[5837.98s] English:** Okay.  
**Translation:** 

**[5838.50s] English:** I got to go to the other one that was just blowing my mind, which is smoke.  
**Translation:** 

**[5845.00s] English:** Let me see.  
**Translation:** 

**[5845.80s] English:** That.  
**Translation:** 

**[5846.64s] English:** Look at that.  
**Translation:** 

**[5847.46s] English:** Yeah.  
**Translation:** 

**[5847.94s] English:** Yeah.  
**Translation:** 

**[5850.00s] English:** Oh.  
**Translation:** 

**[5853.22s] English:** There's a fire.  
**Translation:** 

**[5854.86s] English:** There's a fire in a trash can with the smoke and the shadows, the lighting and the shadows interplaying on the smoke.  
**Translation:** 

**[5865.72s] English:** This is real time.  
**Translation:** 

**[5868.34s] English:** Yeah.  
**Translation:** 

**[5868.60s] English:** That's all real time.  
**Translation:** 

**[5869.76s] English:** What the hell?  
**Translation:** 

**[5871.40s] English:** How do you do that?  
**Translation:** 

**[5873.22s] English:** How do you do the smoke?  
**Translation:** 

**[5874.90s] English:** Well, there's a really powerful particle system underneath.  
**Translation:** 

**[5877.94s] English:** It's providing the technological.  
**Translation:** Vocabulary: particle: 粒子

**[5879.76s] English:** Yeah.  
**Translation:** 

**[5880.00s] English:** foundations for this sort of thing but there's awesome artistry on top of that  
**Translation:** Vocabulary: artistry: 艺术造诣

**[5884.22s] English:** and an awesome physics engine powering it um it's hard to tell exactly which piece is doing what  
**Translation:** 

**[5890.88s] English:** um but you have several different particle systems there there's one for the um fire and then there's  
**Translation:** 

**[5895.98s] English:** another one for the smoke coming out of it um the really interesting thing happening with the  
**Translation:** 

**[5901.34s] English:** smoke here is that it's occluding light you know there's calculation of how the light should  
**Translation:** Vocabulary: occluding: 遮挡光线

**[5906.26s] English:** diminish as it travels through smoke and so you're seeing the lighting on the smoke being  
**Translation:** 

**[5909.66s] English:** the really interesting thing and there have been a lot of attempts but this is this was the first  
**Translation:** Vocabulary: diminish: 减弱

**[5914.82s] English:** demo where i felt felt like this kind of smoke had really no longer looked like a video game  
**Translation:** 

**[5921.40s] English:** it looked like just you know a burning trash can uh billowing out dark smoke um and uh yeah it's  
**Translation:** Vocabulary: billowing: 翻滚

**[5929.18s] English:** a it's the artist's sophistication um it's a very very very large part of it so yeah again it's the  
**Translation:** 

**[5935.80s] English:** interplay video  
**Translation:** Vocabulary: sophistication: 复杂性

**[5936.26s] English:** between the tooling and the and the artists but yeah like that i could i could watch that for a  
**Translation:** 

**[5941.66s] English:** long time i mean there's there's something magical uh sitting around a fire in in real life and just  
**Translation:** 

**[5949.12s] English:** watching the fire and the smoke i mean humans have been doing that for i don't know um hundreds  
**Translation:** 

**[5954.76s] English:** of thousands of years maybe uh and then that same i was i was just staring at that and uh i wish the  
**Translation:** 

**[5962.26s] English:** people would just stop talking and i could just watch the fire  
**Translation:** 

**[5965.04s] English:** infinitely  
**Translation:** Vocabulary: infinitely: 无穷地

**[5966.26s] English:** and that i mean that's immersion that's like i want to be in that i want to sit around that  
**Translation:** 

**[5970.54s] English:** trash can with the fire and the smoke and and watch i mean be warm my because i was also feeling  
**Translation:** Vocabulary: immersion: 沉浸体验

**[5975.76s] English:** cold because of the snow you're like you really get immersed into the thing i mean it's so  
**Translation:** 

**[5980.18s] English:** beautiful it's true art it's true art it's just really wonderfully done um but okay so i gotta  
**Translation:** Vocabulary: immersed: 全身心投入

**[5986.30s] English:** ask you about the humans we we talked about what's it like to create the scenes but you know  
**Translation:** 

**[5993.90s] English:** creating realistic humans is really tough  
**Translation:** 

**[5996.26s] English:** can you speak to that how to create  
**Translation:** 

**[6000.00s] English:** ultra-realistic humans. So you have an actor behind this to convey emotion, show the nuances  
**Translation:** Vocabulary: nuances: 细微差别

**[6006.62s] English:** and the details of the faces. And maybe this is a good opportunity to also mention metahuman  
**Translation:** 

**[6011.64s] English:** creator that's part of Unreal Engine. Yeah, that's right. Humans are by far the hardest part  
**Translation:** Vocabulary: metahuman: 超人类

**[6016.78s] English:** of computer graphics because millions of years of evolution have given us dedicated brain systems  
**Translation:** 

**[6022.76s] English:** to detect patterns and faces and infer emotions and intent. Because cavemen had to, when they  
**Translation:** Vocabulary: cavemen: 穴居人

**[6029.50s] English:** see a stranger, determine whether they were likely friendly or they might be trying to kill them.  
**Translation:** 

**[6034.54s] English:** And so humans, we people in the world have extraordinarily detailed expectations of a face  
**Translation:** 

**[6041.38s] English:** and we can notice imperfections, especially perfections arising from computer graphics  
**Translation:** 

**[6046.20s] English:** limitations. But it becomes by far the hardest problem. So the metahumans effort is part of a  
**Translation:** Vocabulary: metahumans: 超人类

**[6052.80s] English:** decades-long initiative that Vlad Mostilovich, the most talented digital humans, visionary,  
**Translation:** 

**[6059.50s] English:** in the world has been working on for generations and generations of games, serving individual  
**Translation:** Vocabulary: mostilovich: 莫斯特洛夫; visionary: 远见卓识的人

**[6067.08s] English:** clients around the game industry for a while and then joining Epic as part of the three-lateral team  
**Translation:** 

**[6071.54s] English:** and leading now a worldwide effort to build all the technologies required to make digital humans  
**Translation:** 

**[6076.92s] English:** realistic. Okay, one part is capturing humans. And so they've built really advanced, dedicated  
**Translation:** 

**[6082.04s] English:** hardware that puts a human in a capture sphere with dozens of cameras in them, taking high  
**Translation:** 

**[6088.32s] English:** resolution, high frame rate video. And so it's a really advanced, dedicated hardware that puts a  
**Translation:** 

**[6089.44s] English:** video of them as they go through a range of motions. And then capturing the human face is  
**Translation:** 

**[6094.30s] English:** complicated because the nuanced detail of our faces and how the muscles and sinews and fat  
**Translation:** 

**[6098.80s] English:** work together to give us different expressions. So it's not only about the shape of a person's  
**Translation:** Vocabulary: nuanced: 细腻; sinews: 肌腱

**[6103.28s] English:** face, but it's also about the entire range of motion that they might go through. Capturing  
**Translation:** 

**[6107.14s] English:** one human requires a few hours of capture work in a dedicated environment like that, then  
**Translation:** 

**[6112.66s] English:** thousands of hours of processing work to capture a precise and real-time replicatable  
**Translation:** 

**[6119.42s] English:** version of that image.  
**Translation:** Vocabulary: replicatable: 可复制的

**[6120.00s] English:** human in in the environment and so one of the things that it's done is just capturing an actor  
**Translation:** 

**[6125.46s] English:** or actress in the real world and then using them in a video game but the much more interesting  
**Translation:** 

**[6128.90s] English:** thing going on is capturing thousands of humans to form a data set whose goal is to encompass the  
**Translation:** 

**[6135.06s] English:** entire range of faces in all of humanity um so you know going around every culture every continent  
**Translation:** Vocabulary: encompass: 囊括

**[6140.44s] English:** every age and every face of variety uh and capturing representative people so the entire  
**Translation:** 

**[6146.28s] English:** range of faces is represented um and then being able to combine and merge those together to enable  
**Translation:** 

**[6153.38s] English:** recreating an arbitrary face that the system's never seen before so you know one of the ideas  
**Translation:** 

**[6158.48s] English:** is capture uh giant amounts of this high precision data and then you use it to reconstruct uh a face  
**Translation:** Vocabulary: arbitrary: 随机; reconstruct: 重建; recreating: 重现

**[6165.22s] English:** at a consumer level like maybe you know take an iphone photo of somebody's face and then capture  
**Translation:** 

**[6171.20s] English:** a very accurate depiction of that not by synthesizing it then and there on that device  
**Translation:** Vocabulary: depiction: 描绘; synthesizing: 合成

**[6176.28s] English:** all the known details of human faces to accurately capture the most accurate representation of that  
**Translation:** 

**[6181.66s] English:** so that's the data problem there's a lot of other problems of computer graphics you know  
**Translation:** 

**[6186.16s] English:** there's technology for rendering hair which is really hard because you can't render every  
**Translation:** 

**[6190.08s] English:** again we know the laws of physics it would be easy to just render every hair it would just be a  
**Translation:** Vocabulary: render: 渲染

**[6193.84s] English:** billion times too slow um so you need approximations that capture the net effect of hair on rendering  
**Translation:** 

**[6200.20s] English:** and on pixels without calculating every single interaction of every light with every strand of  
**Translation:** Vocabulary: approximations: 近似值; pixels: 像素

**[6205.36s] English:** hair um  
**Translation:** 

**[6206.28s] English:** that's one part of it there's detailed features for different parts of faces  
**Translation:** 

**[6209.88s] English:** they're subsurface scattering because we think of humans as opaque but really our skin is  
**Translation:** 

**[6215.24s] English:** light travels through it it's not completely opaque and the way in which light travels  
**Translation:** Vocabulary: opaque: 不透明; scattering: 散射; subsurface: 次表层

**[6219.64s] English:** through skin has a huge impact on our appearance and this is why there's no way you can paint a  
**Translation:** 

**[6223.98s] English:** mannequin to look realistic for a human you know it's just a solid surface um and we'll never have  
**Translation:** Vocabulary: mannequin: 人体模型

**[6230.16s] English:** the sort of detail you see we should actually just linger on that that kind of blew my mind  
**Translation:** 

**[6235.48s] English:** like thinking through the whole thing and i think that's a really good point i think it's a really  
**Translation:** 

**[6236.28s] English:** good point to think through that i think i heard that sort of the oil  
**Translation:** 

**[6240.00s] English:** oiliness of the skin creates very specific nuanced complex reflections and then some light  
**Translation:** Vocabulary: nuanced: 细腻差别; oiliness: 油脂性

**[6248.92s] English:** is absorbed and travels through the skin and that creates would it be fair to say like micro shadows  
**Translation:** 

**[6254.68s] English:** or something it creates like textures that are humanized able to perceive and it creates the  
**Translation:** Vocabulary: humanized: 人性化; perceive: 感知

**[6260.04s] English:** thing that we consider human whatever that is and so like you have to compute both that the reflection  
**Translation:** 

**[6266.12s] English:** how light interacts with the oiliness of the skin and how it is also absorbed in and all of that  
**Translation:** Vocabulary: interacts: 相互作用

**[6273.34s] English:** while considering the muscle all the muscles involved in making the nuanced expression  
**Translation:** 

**[6278.58s] English:** just the subtle squinting of the eyes or the subtle formation of a smile it's a stupid annoying  
**Translation:** Vocabulary: squinting: 眯眼

**[6286.02s] English:** subtlety of human faces that you have to capture like the difference between a real smile and a  
**Translation:** 

**[6290.72s] English:** fake smile man i love human faces i love humans in general but the way to show like  
**Translation:** Vocabulary: subtlety: 细微差别

**[6295.62s] English:** beginning of the day  
**Translation:** 

**[6296.10s] English:** beginning of a formation of a smile that actually reveals a deep sadness all of that like when i  
**Translation:** 

**[6302.52s] English:** watch a human face i can like read that i could see that again this is the engineering and the  
**Translation:** 

**[6308.56s] English:** artist you have to have the tools that in real time can render something like that and that's  
**Translation:** 

**[6314.88s] English:** incredibly difficult but anyway sorry so yeah so there's a lot of this kind of complexity in even  
**Translation:** 

**[6320.58s] English:** just the lighting of a face that's right getting faces right requires the interplay of literally  
**Translation:** 

**[6326.00s] English:** face to face to face to face to face to face to face to face to face to face to face to face to face  
**Translation:** 

**[6326.08s] English:** dozens of different systems and aspects of computer graphics and if any one of them is  
**Translation:** 

**[6330.54s] English:** wrong your eye is completely drawn to that and you find it on the wrong side of uncannily valley  
**Translation:** 

**[6337.12s] English:** so the level of perfection needed in this area is vastly vastly higher than you know world  
**Translation:** Vocabulary: uncannily: 怪异地

**[6343.68s] English:** rendering or grass or any of these other things um you know if the shadows on a on a work of  
**Translation:** 

**[6350.46s] English:** architecture are slightly wrong you're pretty perfect game with it actually your brain doesn't  
**Translation:** 

**[6355.78s] English:** really care that much but if anything wrong with the human and the it's uh  
**Translation:** 

**[6360.00s] English:** It's totally jarring.  
**Translation:** 

**[6361.58s] English:** Can you speak more to the creation of digital humans with MetaHuman,  
**Translation:** 

**[6365.46s] English:** both on the editor side and sort of bringing it to life side?  
**Translation:** 

**[6369.26s] English:** It seems like, because I've watched a bunch of videos,  
**Translation:** 

**[6371.50s] English:** a bunch of individual developers doing it,  
**Translation:** 

**[6374.92s] English:** it's not too difficult to bring a human to life  
**Translation:** 

**[6378.16s] English:** using the tooling that Unreal Engine Editor provides.  
**Translation:** 

**[6384.32s] English:** There are two main tools.  
**Translation:** 

**[6385.74s] English:** So, you know, compared to the old days  
**Translation:** 

**[6388.20s] English:** where every face was created by hand by an artist from scratch,  
**Translation:** 

**[6392.24s] English:** one is the MetaHuman Creator tool for creating faces  
**Translation:** 

**[6395.22s] English:** where you have a huge number of parameters you can adjust  
**Translation:** 

**[6397.78s] English:** to create a unique human  
**Translation:** 

**[6399.52s] English:** by adjusting all the different capabilities of them.  
**Translation:** 

**[6402.40s] English:** You can then get that out of MetaHuman Creator into Unreal Engine  
**Translation:** 

**[6405.52s] English:** and then you can add all kinds of computer graphics features  
**Translation:** 

**[6408.40s] English:** that are in the engine.  
**Translation:** 

**[6411.56s] English:** You could add clothing using the cloth simulation system  
**Translation:** 

**[6414.30s] English:** and you can adjust the hair  
**Translation:** Vocabulary: simulation: 模拟

**[6415.58s] English:** and all these other parameters on the thing.  
**Translation:** 

**[6419.22s] English:** And then there's MetaHuman Animator,  
**Translation:** Vocabulary: animator: 动画师

**[6420.96s] English:** a tool for animating a human based on a facial capture,  
**Translation:** 

**[6424.44s] English:** which can be done on a device as simple as like an iPhone  
**Translation:** Vocabulary: animating: 动画制作; facial: 面部捕捉

**[6426.64s] English:** and transfers the captured animation to the human you want,  
**Translation:** 

**[6431.24s] English:** which is not straightforward.  
**Translation:** Vocabulary: transfers: 转移

**[6432.66s] English:** If the actor has one face shape  
**Translation:** 

**[6434.72s] English:** and the character on screen has another face shape,  
**Translation:** 

**[6436.88s] English:** the translation that needs to be done from the actor to the face  
**Translation:** 

**[6439.28s] English:** is actually really sophisticated and non-obvious.  
**Translation:** Vocabulary: sophisticated: 复杂精巧

**[6441.30s] English:** And if you just applied it literally,  
**Translation:** 

**[6443.14s] English:** then it would be completely wrong.  
**Translation:** 

**[6445.58s] English:** From your point of view.  
**Translation:** 

**[6446.98s] English:** So those are the main tools that people are using now.  
**Translation:** 

**[6449.74s] English:** And then within the Unreal Engine,  
**Translation:** 

**[6451.36s] English:** then you have a face  
**Translation:** 

**[6452.32s] English:** and you can do absolutely anything you want to it.  
**Translation:** 

**[6454.76s] English:** And you could also, you know,  
**Translation:** 

**[6456.04s] English:** if you decide to go outside of the MetaHuman geometry pipeline,  
**Translation:** 

**[6459.08s] English:** you could build your own face,  
**Translation:** Vocabulary: geometry: 几何; pipeline: 管道

**[6460.16s] English:** like any creature of any sort  
**Translation:** 

**[6462.10s] English:** and then use the animation tools to animate it.  
**Translation:** 

**[6465.62s] English:** But yeah, this is 30 years into a project  
**Translation:** 

**[6467.84s] English:** that's probably like 50 years in total  
**Translation:** 

**[6470.22s] English:** to get to absolute photorealism  
**Translation:** 

**[6471.92s] English:** and controllability for absolutely everything.  
**Translation:** 

**[6474.02s] English:** So there's vast amounts of work still,  
**Translation:** 

**[6475.58s] English:** to do and we don't feel like we've solved the problem at all.  
**Translation:** 

**[6479.36s] English:** We've just given...  
**Translation:** 

**[6480.00s] English:** All right, it's a big productivity multiplier and a quality multiplier, but this is not in a state that we would say is done.  
**Translation:** Vocabulary: multiplier: 倍增器

**[6487.38s] English:** But nevertheless, I've seen people use it really effectively.  
**Translation:** 

**[6490.08s] English:** I saw almost like plugins, maybe external services where you can get the faces to approximate the mouth movements required to speak a thing.  
**Translation:** 

**[6500.72s] English:** So like that, that's a really useful feature.  
**Translation:** 

**[6504.52s] English:** Yeah, that's right.  
**Translation:** 

**[6505.44s] English:** When you have an artist or actor in your studio and you're recording a specific performance, you can just capture their facial motion and apply it.  
**Translation:** 

**[6511.90s] English:** But if all you have is a voice recording or you're generating a voice recording or it's parametric or procedural or AI generated,  
**Translation:** Vocabulary: parametric: 参数化的

**[6519.04s] English:** then you need the system to translate that speech not only to movement of the mouth and lips, but also to facial expressions and the whole intent.  
**Translation:** 

**[6527.08s] English:** When we're speaking, it's our whole face that's active and emoting in different ways.  
**Translation:** Vocabulary: emoting: 表情表达

**[6531.28s] English:** And it's not just a mechanical motion of the pieces.  
**Translation:** 

**[6534.82s] English:** So we've...  
**Translation:** 

**[6535.42s] English:** We spoke a bit about Nanite, so the magic behind the virtualized geometry system.  
**Translation:** 

**[6540.74s] English:** But can you speak a little bit to Lumen and in general what it takes to dynamically light in all the complicated ways, the faces, the scenes that we discussed?  
**Translation:** Vocabulary: dynamically: 动态地; lumen: 光通量; virtualized: 虚拟化

**[6550.18s] English:** Like what are some interesting things to you that made the magic of it happen?  
**Translation:** 

**[6555.50s] English:** Lumen is a system for global illumination.  
**Translation:** Vocabulary: illumination: 照明效果

**[6557.94s] English:** It's supposed to calculate the interaction of light with the entire scene in a way that mimics reality.  
**Translation:** 

**[6565.42s] English:** The first generation of engines that did lighting just said,  
**Translation:** 

**[6568.94s] English:** well, the light casts light and the surfaces it hits are lit and the surfaces it doesn't directly hit are dark.  
**Translation:** 

**[6574.78s] English:** And that's just all the techniques we have.  
**Translation:** 

**[6577.28s] English:** So you'd have an area that wasn't hit by any light being completely black.  
**Translation:** 

**[6581.40s] English:** But in reality, light bounces around the entire scene dynamically.  
**Translation:** 

**[6585.68s] English:** When a light hits a red wall, then most of the blue and green light is absorbed,  
**Translation:** 

**[6592.12s] English:** but the red light reflects off and now is hitting other things.  
**Translation:** 

**[6594.98s] English:** And so if you...  
**Translation:** 

**[6595.30s] English:** A red wall with a white floor, light is bouncing off of the red wall into the floor.  
**Translation:** Vocabulary: bouncing: 反弹

**[6600.00s] English:** now the floor is being turned red. And so the entire bouncing of light around the scene through  
**Translation:** 

**[6606.12s] English:** multiple bounces is the critical challenge to solve here. And again, laws of physics are known,  
**Translation:** 

**[6611.42s] English:** and so the complete solution to this was written down in the 1950s, I think. The real magic here  
**Translation:** 

**[6618.80s] English:** in Lumen is this system that Daniel Wright developed over the course of many years,  
**Translation:** 

**[6623.92s] English:** based on ideas formed over a longer period of time, to calculate the way lighting bounces  
**Translation:** 

**[6628.52s] English:** around at different scales, ranging from the scale of miles or kilometers down to the scale of  
**Translation:** 

**[6635.36s] English:** pixels and millimeters, and to not only calculate at each level, but integrate it seamlessly at  
**Translation:** 

**[6641.82s] English:** each level to give the appearance of completely seamless and accurate lighting. And previous  
**Translation:** Vocabulary: integrate: 融为一体; millimeters: 毫米; pixels: 像素; seamless: 天衣无缝; seamlessly: 无缝地

**[6647.98s] English:** techniques were highly specialized, and artists had to make a decision for each light about exactly  
**Translation:** 

**[6652.32s] English:** what it did. The goal in a lot of the practice with the light now is you build a scene, you place  
**Translation:** 

**[6657.22s] English:** lights in it, and it just works.  
**Translation:** 

**[6658.52s] English:** Um, to make it that much easier.  
**Translation:** 

**[6661.40s] English:** Yeah, I mean, we're watching says I'd recommend people go through this blog post. Like, look at  
**Translation:** 

**[6666.24s] English:** that. So dynamically, I mean, we should say that so there's the indoors and the outdoors and to be  
**Translation:** Vocabulary: dynamically: 动态地

**[6671.20s] English:** able to dynamically compute the impact of outdoor light. Just look at that. Look how gorgeous that  
**Translation:** 

**[6677.60s] English:** is. Yeah, just the lighting. Like, look, we're looking now at an image of a cave. So external  
**Translation:** 

**[6684.88s] English:** light lighting this, the intricate complexity of an inside and outside.  
**Translation:** 

**[6688.52s] English:** of a cave. Yeah, that light in the real world goes through a lot of bounces, and the effects of it are  
**Translation:** Vocabulary: complexity: 复杂性

**[6694.58s] English:** very, very subtle. But when they're not there, you miss them. Often, a person can't point out why a  
**Translation:** 

**[6700.16s] English:** scene is wrong, but they know it looks wrong. And it's the lack of the subtle lighting cues that  
**Translation:** 

**[6704.08s] English:** we're seeing here.  
**Translation:** 

**[6705.28s] English:** And, you know, for great because we mentioned for great video games, but also for great films,  
**Translation:** 

**[6710.30s] English:** lighting can make a film and we're just looking at sort of a very dramatic lighting of a scene.  
**Translation:** 

**[6716.18s] English:** They can imagine stepping into the scene at your  
**Translation:** 

**[6718.52s] English:** it's exciting.  
**Translation:** 

**[6720.00s] English:** terrifying and all of that has to do with light the interplay between light and darkness  
**Translation:** Vocabulary: terrifying: 令人恐惧的

**[6726.36s] English:** it's incredible it's really truly truly incredible like light is everything  
**Translation:** 

**[6730.62s] English:** and then to put the power of the tooling in the hands of an artist that is really special yeah  
**Translation:** 

**[6736.50s] English:** the industry's gone through a massive evolution and there's so many supporting systems to make  
**Translation:** 

**[6741.72s] English:** this awesome um and always artists we're looking at reflections on smooth surfaces oh boy oh boy  
**Translation:** 

**[6752.28s] English:** look at how gorgeous that is yeah that's right and you have to appreciate the algorithms are  
**Translation:** 

**[6758.32s] English:** doing quite a lot here uh you can have a you know a scene with a huge number of not just lights but  
**Translation:** 

**[6763.60s] English:** also bright objects who reflect light off of them every one of those has to be captured in the  
**Translation:** 

**[6768.54s] English:** reflections in order for it to be realistic and you know you can't calculate the amount of light  
**Translation:** 

**[6771.70s] English:** you can calculate every photon in the scene and so you need really detailed approximations and  
**Translation:** 

**[6777.28s] English:** that's the field of computer graphics it's about increasingly effective approximations of the laws  
**Translation:** Vocabulary: approximations: 近似方法; photon: 光子

**[6781.90s] English:** of physics which are just totally intractable but the result of that Graphics is a feeling is an  
**Translation:** 

**[6787.18s] English:** experience by the viewer and it's just to me as a fan of well let's say beauty in the world it's  
**Translation:** Vocabulary: intractable: 难以解决

**[6794.14s] English:** it's exciting that we can create that synthetically artificially uh via graphics and that just  
**Translation:** 

**[6801.04s] English:** it  
**Translation:** Vocabulary: artificially: 人工地; synthetically: 合成地

**[6801.64s] English:** blows wide open the possibilities of storytelling so outside of video games a lot of people are  
**Translation:** 

**[6807.44s] English:** using unreal engine for movies for films uh and big congrats i saw wars over a short film  
**Translation:** Vocabulary: congrats: 祝贺; storytelling: 讲故事

**[6814.30s] English:** that was made with unreal engine won an oscar so you can add that to the uh to the resume  
**Translation:** 

**[6821.98s] English:** so that's huge you know an oscar winning film made with unreal engine so what uh what do you  
**Translation:** Vocabulary: oscar: 奥斯卡奖

**[6829.16s] English:** see is the future of um the use of unreal engine and creating stories in the in the film industry  
**Translation:** 

**[6835.98s] English:** increasing capabilities and productivity um  
**Translation:** 

**[6840.00s] English:** Yeah, the limiting factor in every one of these businesses is cost.  
**Translation:** 

**[6845.20s] English:** And the more the engine can make their jobs easier, the more power that brings them.  
**Translation:** 

**[6850.84s] English:** One of the big revolutions we've seen in Hollywood is moving away from doing computer graphics integration  
**Translation:** 

**[6857.04s] English:** into a human scene with green screens to moving to these large LED wall panels.  
**Translation:** Vocabulary: revolutions: 重大变革

**[6863.84s] English:** They're displaying real-time computer graphics powered by the Unreal Engine.  
**Translation:** 

**[6867.88s] English:** And that's a massive improvement in quality.  
**Translation:** 

**[6869.76s] English:** You can recognize the old green screen movies because the lighting on the characters is just wrong.  
**Translation:** 

**[6875.12s] English:** And as much as they try to fix it up, it never really works.  
**Translation:** 

**[6878.12s] English:** When you're filming in front of an LED panel with LED light emitters in front of you as well,  
**Translation:** 

**[6883.02s] English:** the actor not only picks up all the lighting from the actual natural scene that they're supposed to appear in in the movie,  
**Translation:** Vocabulary: emitters: 发光体

**[6888.24s] English:** but they also can look around and see it, and they're aware of exactly what set they're acting in.  
**Translation:** 

**[6892.96s] English:** And just the overall end result is that much higher.  
**Translation:** 

**[6895.42s] English:** It's as much because the actors are able to do their jobs better,  
**Translation:** 

**[6898.62s] English:** seeing the scene they're in, because the technology is enabling a better lighting calculation  
**Translation:** 

**[6903.88s] English:** and a better interplay of virtual light and real-world light to make the end result awesome.  
**Translation:** 

**[6909.44s] English:** So there's a lot of excitement around generative AI.  
**Translation:** Vocabulary: generative: 生成式

**[6912.88s] English:** What do you think is the future of the interplay between what a human artist creates  
**Translation:** 

**[6918.40s] English:** and what an AI system can create in Unreal Engine?  
**Translation:** 

**[6922.86s] English:** I think a lot of people in the industry are overly optimistic about the rate of progress of AI  
**Translation:** 

**[6928.10s] English:** for video and other things like that.  
**Translation:** Vocabulary: optimistic: 过于乐观

**[6930.20s] English:** The real problem is consistency.  
**Translation:** 

**[6932.00s] English:** Like, spurting out an image is really high quality.  
**Translation:** Vocabulary: spurting: 喷出

**[6933.92s] English:** But with video, over the course of seeing all the AI approaches have consistency issues  
**Translation:** 

**[6939.94s] English:** going from one place to another.  
**Translation:** 

**[6941.22s] English:** And I don't think that those will just be remedied easily.  
**Translation:** 

**[6945.08s] English:** Fundamentally, AI just doesn't have anything resembling an understanding of the entire scene they're in,  
**Translation:** Vocabulary: fundamentally: 从根本上; remedied: 解决

**[6952.18s] English:** the entire arc of the movie or plot they're in, and the entirety of the world around them.  
**Translation:** 

**[6958.10s] English:** And how it might affect the scene.  
**Translation:** Vocabulary: entirety: 全部

**[6960.00s] English:** um whereas game engines have that um exactly where they need to be and so i think what we're  
**Translation:** 

**[6966.38s] English:** going to see in the space of world-class high quality productions isn't just everybody moves  
**Translation:** 

**[6971.80s] English:** to ai and a large part of the human uh creatives contributing to that are obsolete i think what  
**Translation:** 

**[6977.96s] English:** we're going to see is ai becoming a multiplying force on the power of human creatives making them  
**Translation:** Vocabulary: creatives: 创造性人才; multiplying: 增强; obsolete: 过时

**[6983.20s] English:** able to create better stuff more quickly um and with higher quality and results i think  
**Translation:** 

**[6988.58s] English:** unlike the fields of generative 2d art and um generative text i think the future of ai is  
**Translation:** 

**[6995.84s] English:** much more complex and nuanced and i think your interview with mark zuckerberg conducting in vr  
**Translation:** 

**[7001.00s] English:** was a really good first example of this uh so you did this vr discussion it was capturing your faces  
**Translation:** Vocabulary: conducting: 进行; nuanced: 细腻

**[7008.16s] English:** uh and then rendering a completely 3d computer graphics model of your faces and then the end  
**Translation:** 

**[7015.22s] English:** result was patched up by an ai image enhancer  
**Translation:** Vocabulary: enhancer: 图像增强器

**[7017.80s] English:** it was  
**Translation:** 

**[7018.56s] English:** able to add an awful lot of the missing subtleties that are lost by normal computer graphics  
**Translation:** Vocabulary: subtleties: 细微差别

**[7023.44s] English:** rendering and that's the first step you know you can imagine the output of unreal engine being  
**Translation:** 

**[7029.14s] English:** enhanced by an ai pixel shading post processor is one thing you can imagine creation of objects  
**Translation:** Vocabulary: pixel: 像素; processor: 处理器

**[7035.44s] English:** being enhanced especially mashing up high quality objects have already been created like epic's  
**Translation:** 

**[7041.96s] English:** quixel team went around the world and scanned tens of thousands of real world objects at  
**Translation:** 

**[7046.38s] English:** extremely high levels of quality a day of everything  
**Translation:** 

**[7048.56s] English:** from rocks to trees to archaeological finds and so on all captured there and we have an  
**Translation:** Vocabulary: archaeological: 考古的

**[7055.12s] English:** awesome library of them  
**Translation:** 

**[7056.24s] English:** on the fab content site what's missing is the ability to create arbitrary amounts of new content  
**Translation:** Vocabulary: arbitrary: 任意的

**[7061.66s] English:** and i think using data like that and ai to create completely new trees that meet your  
**Translation:** 

**[7068.36s] English:** specification from all the knowledge it has built up of high quality scan trees it's going  
**Translation:** Vocabulary: specification: 具体要求

**[7072.14s] English:** to be really valuable thing but you know i don't see this this reducing the need for people to respond to hardware or whatever you can do in life if you are Problem Maker or a Sharpshooter or whatever kind of laundromat can have human ensure system systems or computers that come into life using hardware  
**Translation:** 

**[7074.48s] English:** um I have recently been exposed to this task group where I realized that no graph was going to be a good sensor or providedics forecast program within sapt Такard  
**Translation:** Vocabulary: laundromat: 洗衣店; sensor: 传感器; sharpshooter: 神枪手

**[7075.68s] English:** see this reducing the need for people or the role of people.  
**Translation:** 

**[7080.00s] English:** Rather, I think it actually is probably an enhancer on that.  
**Translation:** 

**[7082.94s] English:** I can't help but think when I go on Amazon and Netflix to watch a movie, there's an awful lot of linear content.  
**Translation:** 

**[7088.72s] English:** And most of it isn't very good because of the limitations of the media and the budgets and of other things.  
**Translation:** 

**[7096.80s] English:** If we can use AI as an enhancer on that, then everybody's going to have even more opportunity than they have now.  
**Translation:** 

**[7102.84s] English:** And every single technological revolution has changed the way that people work, but it's ultimately created more opportunity for people.  
**Translation:** 

**[7110.60s] English:** And there are pundits predicting that this might be the last, but I think just the opposite.  
**Translation:** 

**[7115.12s] English:** I'm an optimist on this and an optimist that it's going to create opportunity for everyone.  
**Translation:** Vocabulary: optimist: 乐观主义者; pundits: 评论家

**[7119.76s] English:** Do you think it will be possible to use generative AI to create dynamic objects, like you mentioned trees, in the Unreal Engine?  
**Translation:** 

**[7132.84s] English:** In the Unreal Engine world, so create meshes and textures and empower the creator to create faster.  
**Translation:** Vocabulary: empower: 赋予权力; generative: 生成的

**[7140.26s] English:** Use meta knobs, like hyperparameters versus very nuanced, where you can control much faster the look of a face, the look of a tree, all that kind of stuff.  
**Translation:** 

**[7150.62s] English:** Yeah, I think that's the central challenge of the next decade of game engines and AI for content creation of all sorts.  
**Translation:** Vocabulary: hyperparameters: 超参数; knobs: 旋钮; nuanced: 细腻

**[7158.42s] English:** Because you have two very different models of the world that are emerging.  
**Translation:** 

**[7161.96s] English:** There's the CMU.  
**Translation:** 

**[7162.84s] English:** There's the machine graph.  
**Translation:** 

**[7163.70s] English:** The technical term we use to describe the set of all of the objects in the world in a 3D world maintained by Unreal Engine or another engine.  
**Translation:** 

**[7171.74s] English:** So in the videos you saw, it's the rocks and the trees and the snow and the bridge and the people and all of these things.  
**Translation:** 

**[7178.12s] English:** And each one has enormous amounts of data attached to it.  
**Translation:** 

**[7181.38s] English:** Some are like texture maps.  
**Translation:** 

**[7182.68s] English:** Some are sound files.  
**Translation:** 

**[7184.64s] English:** Some are animation files.  
**Translation:** 

**[7187.02s] English:** And enormous amounts of detail, all stored there in that procedure in this computer.  
**Translation:** 

**[7191.86s] English:** Precise computer graphics.  
**Translation:** 

**[7192.84s] English:** Graphics representation that enables rendering it from any perspective with any settings and so on.  
**Translation:** 

**[7196.94s] English:** It's a completely general system that...  
**Translation:** 

**[7200.00s] English:** It has complete context about the state of the world at any point, and so you can always precisely reproduce it. If you play the same scene 10 times in a row, it's always the same. It's never randomly changing. You're like, oh, no, why did this character's face change midstream? But it's also rather limited because you have to build everything manually, and it's costly, and it's time-consuming, and it requires expertise.  
**Translation:** Vocabulary: midstream: 中途

**[7220.10s] English:** And then you have this other model of the world, which is what AI sees or thinks. If we could peer into what's really happening and its parameters, there's something like the mushy connections of neurons in a brain.  
**Translation:** 

**[7232.26s] English:** It has a vast amount of knowledge about the world and about graphics and about images and about people and about everything else. It's stored in a human, incomprehensible form, but it can be extracted through queries, like asking it to produce an image from a prompt or a video from a prompt or whatever.  
**Translation:** Vocabulary: extracted: 提取; incomprehensible: 难以理解; mushy: 模糊不清; neurons: 神经元

**[7250.10s] English:** But the huge problem with that is it's very mushy data. We don't know how to give it a command that will give us a precise result.  
**Translation:** 

**[7260.74s] English:** And if it produces one image one time and we change our prompt slightly, it might produce something completely different. We are unable to art direct it.  
**Translation:** 

**[7267.64s] English:** And so it's this completely untamed tool. I think when we figure out more and more ways to merge these and connect these two together, you can imagine AI enhancing the process of content creation.  
**Translation:** 

**[7280.10s] English:** And so let's look at the AI and the AI and the AI and the AI and the AI and the AI and the AI and the AI and the AI and the AI and the AI and the AI and the AI.  
**Translation:** Vocabulary: enhancing: 提升; untamed: 未驯服

**[7281.18s] English:** In a traditional scene representation, you can imagine the scene representation being shared with the AI. So the AI not only sees a prompt, but also here's a list of all of the objects in the world and the characteristics and so on.  
**Translation:** 

**[7292.18s] English:** It can learn more about how those objects should move and interact.  
**Translation:** 

**[7295.78s] English:** If you get a constant feedback cycle going back and forth between an engine and AI, I think you can get the best of both worlds.  
**Translation:** 

**[7302.00s] English:** Stable scenes, but also the higher productivity of being able to get content out and the ability to select specific parts of it and art direct.  
**Translation:** 

**[7310.10s] English:** those um and have those art directions stick and be recognized as part of this permanent  
**Translation:** 

**[7315.44s] English:** scene representation yeah i can't wait until ai can operate not  
**Translation:** 

**[7320.00s] English:** Not in the space of pixels, but in the space of scene graphs, creating objects in the scene graph, whether it's like you mentioned audio or any of the things that you mentioned about that empower the creator.  
**Translation:** 

**[7333.62s] English:** Yeah, that's a super exciting future.  
**Translation:** Vocabulary: empower: 赋予权力

**[7335.86s] English:** I wonder if you could speak to a fear that people have on this topic of artists, engineers, fear of losing their jobs, being replaced by AI.  
**Translation:** 

**[7350.00s] English:** Are there words of hope that you could offer them?  
**Translation:** 

**[7352.88s] English:** This is certainly the most extreme example of it because AI is just so far ahead of prior technologies.  
**Translation:** 

**[7358.08s] English:** But similar fears were had in every other industry.  
**Translation:** 

**[7361.18s] English:** There's a fear that digital music synthesis would obsolete musicians.  
**Translation:** 

**[7367.54s] English:** And there's a very brief period of time in which songs with digital music instruments, like the early mini-mugs and Yamaha synthesizers, weren't allowed to win certain music industry awards because they weren't considered real music.  
**Translation:** 

**[7380.00s] English:** And then, you know, over time, the people were educated and realized, oh, these are just instruments people are playing and they're controlling them the same way they did before.  
**Translation:** 

**[7389.02s] English:** There are similar questions about, is, you know, computer art built in Photoshop really art?  
**Translation:** 

**[7395.26s] English:** Or is it just, you know, goofy computer stuff?  
**Translation:** 

**[7397.60s] English:** And, you know, I think nowadays digital artists have gained respect.  
**Translation:** Vocabulary: goofy: 愚蠢的

**[7400.54s] English:** And I think, you know, if you look at just the tools that have existed in Photoshop, some of them are pretty sophisticated.  
**Translation:** 

**[7406.28s] English:** And nowadays they have AI features.  
**Translation:** Vocabulary: sophisticated: 复杂高级

**[7407.96s] English:** But I think AI is ultimately going to be another tool.  
**Translation:** 

**[7409.94s] English:** And, you know, I think it's going to become a more powerful, directable, and human-serving tool in the future.  
**Translation:** Vocabulary: directable: 可控的

**[7418.14s] English:** And I think a lot of the alienation comes from the prompt either being immensely powerful at giving you an entire creation, but then being completely unwilling to let you control the nuances of it.  
**Translation:** 

**[7429.58s] English:** That feels alienating.  
**Translation:** Vocabulary: alienating: 使人疏远; alienation: 疏远感; immensely: 极其; nuances: 细微之处; unwilling: 不愿意

**[7430.84s] English:** You give it an image, but you're like, you know, replace the image of, replace this part of it with this thing, or make that object green.  
**Translation:** 

**[7437.72s] English:** And it just, like, it can't do it.  
**Translation:** 

**[7439.62s] English:** Often.  
**Translation:** 

**[7439.94s] English:** It can't do it.  
**Translation:** 

**[7440.00s] English:** can't be convinced with any number of words uh in the prompt and that makes it feel like the  
**Translation:** 

**[7444.46s] English:** computer is taking control away from us um you know humans and artists um and is refusing to  
**Translation:** 

**[7450.58s] English:** do what we want and has its own opinions right it feels like a competitor i think when when we have  
**Translation:** 

**[7456.12s] English:** much much much more nuanced control of it and artists can go in and just you know like you know  
**Translation:** Vocabulary: nuanced: 细致入微

**[7459.88s] English:** let's enhance this object do this do that do that i'll feel it's a you know like some of the tools  
**Translation:** 

**[7464.04s] English:** they exist in photoshop which are in some ways compared to a paintbrush or superpowers already  
**Translation:** Vocabulary: paintbrush: 画笔; superpowers: 超能力

**[7468.38s] English:** um ai will come to feel like that too and will increasingly serve creators creating and  
**Translation:** 

**[7473.78s] English:** enhancing a work in a way that feels just a natural extension of their own you know their  
**Translation:** Vocabulary: enhancing: 提升

**[7478.46s] English:** own bodies and and minds and of course there is a real human pain to layoffs and there is a hype  
**Translation:** 

**[7485.44s] English:** around ai and then companies might try to implement ai systems and so doing layoff a bunch of folks  
**Translation:** Vocabulary: layoff: 裁员; layoffs: 裁员

**[7494.02s] English:** and that the pain that those folks feel is real i think  
**Translation:** 

**[7497.86s] English:** you  
**Translation:** 

**[7498.38s] English:** there's always going to be pain with these kinds of transformation that's happening and it's a  
**Translation:** 

**[7502.46s] English:** terrible pain pain in general and the human experience is terrible but i think i'm personally  
**Translation:** 

**[7510.00s] English:** excited by the human ai collaboration as you've described in this whole process so i think if you  
**Translation:** 

**[7517.30s] English:** just keep being open to using the tools constantly trying the cutting edge tools how they can make  
**Translation:** 

**[7522.64s] English:** you more productive how can they empower you as a creator as an artist or as an engineer  
**Translation:** 

**[7528.38s] English:** i think you're going to just keep winning yeah there's a lot of complicated  
**Translation:** Vocabulary: empower: 授权

**[7534.10s] English:** trends underway and it can be hard to break them down and distinguish them i think a lot of people  
**Translation:** 

**[7539.60s] English:** like the the theories that get the biggest traction on social media often don't capture  
**Translation:** Vocabulary: underway: 已经开始

**[7544.38s] English:** the real underlying motive forces at play there but yeah i think ai involved in code production  
**Translation:** 

**[7552.02s] English:** will probably create a net benefit for the need for humanity to be involved in coding  
**Translation:** 

**[7556.56s] English:** it may change parts of jobs  
**Translation:** 

**[7558.38s] English:** i don't think it's gonna  
**Translation:** 

**[7560.00s] English:** obsolete anybody who's willing to learn new ways of doing things. And it's always been this way.  
**Translation:** 

**[7565.68s] English:** And I think that there's also a lot of overhype in AI. AI is really great at spewing out code  
**Translation:** Vocabulary: obsolete: 过时; overhype: 过度炒作; spewing: 喷出

**[7570.08s] English:** that does something that a million GitHub repositories already do, because it's kind  
**Translation:** 

**[7573.92s] English:** of learned the underlying pattern. It's notoriously hard to get to do something new  
**Translation:** Vocabulary: repositories: 代码仓库

**[7577.84s] English:** that hasn't been done before, especially when it's a complex task. And the bigger amount of  
**Translation:** 

**[7584.42s] English:** code you ask AI for, the more it leaves you with just a massive code that sort of works, right?  
**Translation:** 

**[7589.08s] English:** And that's the problem with code. It's like 99% works, but the 1%. It might be harder to get to  
**Translation:** 

**[7594.22s] English:** 100% with AI than with hand coding. And everybody who's looking at this topic should actually try  
**Translation:** 

**[7599.40s] English:** using the coding assistants on hard problems and see how they do there.  
**Translation:** 

**[7603.46s] English:** Yeah, I think for me personally, it makes it more fun and faster to generate boilerplate code.  
**Translation:** Vocabulary: boilerplate: 模板代码

**[7610.18s] English:** So I can focus on the harder decisions, harder big picture decisions and  
**Translation:** 

**[7613.70s] English:** harder innovative decisions and all that kind of stuff.  
**Translation:** 

**[7617.14s] English:** And it just makes programming more fun.  
**Translation:** 

**[7619.08s] English:** It's fun for me because I feel less lonely.  
**Translation:** 

**[7622.82s] English:** Yeah.  
**Translation:** 

**[7624.02s] English:** I have, like, even when it gives the wrong code, I get like,  
**Translation:** 

**[7629.22s] English:** oh, okay, well, that's a way to do it. That's interesting. And then you could talk to it.  
**Translation:** 

**[7634.40s] English:** Maybe that shows something about the programming experience that it is in part sometimes a bit  
**Translation:** 

**[7639.94s] English:** lonely.  
**Translation:** 

**[7640.70s] English:** The topic of boilerplate code is an interesting one, because like,  
**Translation:** 

**[7644.60s] English:** the mere existence of boilerplate code is a failure of programming language and  
**Translation:** 

**[7648.34s] English:** of the  
**Translation:** 

**[7649.08s] English:** idea of creating software modules, right?  
**Translation:** 

**[7651.54s] English:** You know, you ask AI to create a sorting function. Great.  
**Translation:** 

**[7654.20s] English:** Now you have another sorting function that might be buggy, alongside the million others that different  
**Translation:** 

**[7658.62s] English:** people have written, it'll be better to have a sorting function that's been written and tested and  
**Translation:** Vocabulary: buggy: 有 Bug 的

**[7662.40s] English:** optimized, and everybody relies on it. And more modular software, I think, will actually reduce the  
**Translation:** 

**[7669.48s] English:** opportunity of AI because, you know, people doing programming work will largely be solving unique  
**Translation:** Vocabulary: modular: 模块化的; optimized: 优化的

**[7674.12s] English:** problems. They're actually hard problems in themselves and not just connecting other widgets.  
**Translation:** 

**[7679.08s] English:** Yeah, I think  
**Translation:** Vocabulary: widgets: 小部件

**[7680.00s] English:** As in many cases, AI will just help improve the human systems by shining a mirror to ourselves.  
**Translation:** 

**[7687.10s] English:** I have to apologize for the pothead question ahead of time, but let's talk about the metaverse broadly.  
**Translation:** Vocabulary: metaverse: 虚拟宇宙

**[7693.20s] English:** You've been a big proponent of the idea of the metaverse.  
**Translation:** 

**[7696.50s] English:** We'll talk more specifically what that means today, but we've been talking about simulating reality better and better and better.  
**Translation:** Vocabulary: proponent: 支持者; simulating: 模拟

**[7705.52s] English:** So the pothead question is, what does it take to simulate reality better?  
**Translation:** 

**[7710.00s] English:** To the level we see around us today, how far away from that are we to simulate this ultra-realistic, immersive, fun reality that Earth is?  
**Translation:** Vocabulary: immersive: 身临其境; simulate: 模拟

**[7724.34s] English:** What does it take?  
**Translation:** 

**[7725.76s] English:** We're going to get shockingly close over the coming years, certainly less than 20 years.  
**Translation:** Vocabulary: shockingly: 令人惊讶地

**[7730.04s] English:** If you look at the progress, what areas where we have achieved total photorealism and what areas where we fall short,  
**Translation:** 

**[7735.88s] English:** we're getting very close in all non-human interactions.  
**Translation:** 

**[7739.64s] English:** You see in the world, walking through a jungle or a city, all the lighting, it's very close.  
**Translation:** 

**[7745.60s] English:** And that might be just a few years away.  
**Translation:** 

**[7747.12s] English:** But then all the problems that involve humans, human dialogue and intent have a much, much, much higher bar that they need to meet to satisfy our brains and convince us that they're realistic or real.  
**Translation:** 

**[7760.70s] English:** And I think that's going to be the primary challenge of graphics development and simulation development over the coming decade.  
**Translation:** 

**[7767.24s] English:** So the realistic humans.  
**Translation:** 

**[7769.02s] English:** That's going to be the bottom line.  
**Translation:** 

**[7771.32s] English:** Yeah.  
**Translation:** 

**[7771.64s] English:** So and visual and behavior, too.  
**Translation:** 

**[7774.86s] English:** So everything.  
**Translation:** 

**[7775.94s] English:** Yeah.  
**Translation:** 

**[7776.50s] English:** I was asked about this about 10 years ago.  
**Translation:** 

**[7778.22s] English:** And I said that even if you gave us an infinite amount of computing power, we couldn't simulate realistic humans because we simply don't have the algorithms.  
**Translation:** Vocabulary: computing: 计算

**[7785.74s] English:** We have no idea how to simulate human intelligence.  
**Translation:** 

**[7789.64s] English:** And that was absolutely the case then.  
**Translation:** 

**[7791.64s] English:** But it's not really true anymore.  
**Translation:** 

**[7793.52s] English:** You know, what we're seeing with generative text AI is not only at a level that you could say.  
**Translation:** Vocabulary: generative: 生成式

**[7799.02s] English:** It's actually.  
**Translation:** 

**[7800.00s] English:** doing a pretty good job of simulating human, at least humans at the text level, not at the  
**Translation:** 

**[7805.30s] English:** emotional level yet, but at least at the level of words spoken, and find more and more ways of  
**Translation:** 

**[7810.40s] English:** training on more and more scenarios. You might have a very, very compelling human simulation  
**Translation:** Vocabulary: compelling: 极具说服力; scenarios: 情景; simulation: 模拟

**[7815.78s] English:** going on in the next five years, even. I'm not saying it's a good idea, but I think the arc of  
**Translation:** 

**[7822.38s] English:** the technology is inextricably heading in that way, and it's heading at a shocking, shocking rate.  
**Translation:** Vocabulary: inextricably: 无法摆脱

**[7826.78s] English:** We don't say this enough, but the current state of LLMs, if you put Alan Turing in conversation  
**Translation:** 

**[7836.20s] English:** with Chad GPT, it really passes the Turing test, almost definitively passes the Turing test.  
**Translation:** Vocabulary: definitively: 毫无疑问; turing: 图灵测试

**[7844.42s] English:** Of course, we keep raising the bar, well, the Turing test is not real, it's not a useful test,  
**Translation:** 

**[7848.70s] English:** whatever. We just keep raising the bar for AI, where it's always going to be lesser than. But  
**Translation:** 

**[7855.40s] English:** yeah, you have...  
**Translation:** 

**[7856.78s] English:** You have increasingly ultra-realistic faces and bodies, combined with increasingly moving and  
**Translation:** 

**[7864.10s] English:** powerful, full of emotion, speech, text. I work with this amazing company called LLM Labs that  
**Translation:** 

**[7871.28s] English:** does text-to-speech well. There's companies that specialize in bringing text to life.  
**Translation:** Vocabulary: specialize: 专门从事

**[7876.40s] English:** That's going to increase. Different companies do that very well.  
**Translation:** 

**[7879.70s] English:** And so, and then all of a sudden, you have this synthetically created  
**Translation:** Vocabulary: synthetically: 人工合成

**[7884.80s] English:** scene where humans...  
**Translation:** 

**[7886.78s] English:** Human is speaking, and you're moved to the point of tears because of this scene. Beautifully lit  
**Translation:** 

**[7893.02s] English:** face in the full darkness, the emotion, the drama of the scene. Yeah, I think... So you're saying  
**Translation:** 

**[7900.64s] English:** five, 10 years, maybe 20.  
**Translation:** 

**[7902.70s] English:** Yeah, absolutely. We'll definitely see it in our lifetimes.  
**Translation:** 

**[7906.64s] English:** Increasing the level of potheadness in my question, do you think we might live in a simulation?  
**Translation:** Vocabulary: lifetimes: 一生; potheadness: 大麻文化

**[7913.76s] English:** And if we do or don't,  
**Translation:** 

**[7915.90s] English:** how hard would it be to build such a simulation where we're fully...  
**Translation:** 

**[7920.00s] English:** convinced we're in it well i don't think that these questions are necessarily unanswerable i  
**Translation:** 

**[7926.84s] English:** think i'd like to see more actual effort to to ascertain like what is the underlying mechanism  
**Translation:** Vocabulary: ascertain: 确定

**[7932.24s] English:** of the universe and i don't think we're here for no reason at all i think the world's a pretty  
**Translation:** 

**[7937.44s] English:** cool place and uh the fact that we can exist and you know the laws of physics and especially a  
**Translation:** 

**[7942.74s] English:** standard model of physics and all the parameters that lead to you know these atoms and life  
**Translation:** 

**[7948.30s] English:** evolving in the presence of thermodynamic gradients that's really cool um and i think  
**Translation:** Vocabulary: evolving: 演化; gradients: 梯度; thermodynamic: 热力学的

**[7953.90s] English:** it's a worthy field to study more about that holistically i don't know the question of uh  
**Translation:** 

**[7958.64s] English:** are we living in a simulation ourselves always boils down to well if we are living in a simulation  
**Translation:** Vocabulary: holistically: 全面地; simulation: 模拟

**[7963.80s] English:** what are they living in because at some point there has to be some base reality or you know  
**Translation:** 

**[7968.30s] English:** one of the philosophical theories that was put forth seriously was that there is no physical  
**Translation:** Vocabulary: philosophical: 哲学的

**[7973.68s] English:** reality um if you have a system of equations um you know such as the law  
**Translation:** 

**[7978.28s] English:** of physics uh then all possible evolutions of dynamical systems under those equations  
**Translation:** Vocabulary: dynamical: 动力学的; equations: 方程; evolutions: 演化

**[7983.56s] English:** kind of have a physical reality so we just are kind of a manifestation of laws of math  
**Translation:** 

**[7987.76s] English:** rather than needing an actual universe around us i don't know i like dabbling in that philosophy  
**Translation:** Vocabulary: dabbling: 涉猎; manifestation: 显现

**[7994.04s] English:** and as we get cai becoming smarter and smarter and we get closer and closer to really capturing  
**Translation:** 

**[7998.64s] English:** the full laws of physics these questions become quite a lot more compelling you know you start  
**Translation:** Vocabulary: compelling: 有吸引力的

**[8003.52s] English:** to think if we're not living in a simulation what are the things about the  
**Translation:** 

**[8008.28s] English:** reality that are not simulatable so what are the big mysteries around us it feels like the  
**Translation:** Vocabulary: simulatable: 可模拟的

**[8015.08s] English:** physics is simulatable it feels like a lot of the incredible stuff that we talked about  
**Translation:** 

**[8019.50s] English:** while super nice seems simulatable but then there's the the flame of consciousness the feeling  
**Translation:** 

**[8027.92s] English:** of it whatever that is that lights up in our eyes as humans maybe that's not simulatable maybe that  
**Translation:** 

**[8034.14s] English:** is the thing maybe maybe that's a thread that connects to the explanation of the  
**Translation:** 

**[8038.28s] English:** mechanism as you said  
**Translation:** 

**[8040.00s] English:** of the universe that's really important to understand and we're completely clueless about  
**Translation:** Vocabulary: clueless: 一无所知

**[8043.68s] English:** that mechanism well i mean a lot of the religious texts sneak up on what that mechanism is but we're  
**Translation:** 

**[8050.58s] English:** still mostly clueless we only have these like leaps of faith and believing what that mechanism  
**Translation:** 

**[8055.28s] English:** might be so you know the whole idea of nested simulations perhaps yeah given a sufficiently  
**Translation:** 

**[8061.74s] English:** advanced technology is kind of mooted uh such that if you wanted to simulate another reality  
**Translation:** Vocabulary: mooted: 讨论的; simulate: 模拟; sufficiently: 足够

**[8067.30s] English:** you're kind of just actually creating the reality um you're doing uh you know quantum  
**Translation:** 

**[8072.08s] English:** mechanical operations that would produce the same result anyway and you're running them at  
**Translation:** 

**[8075.94s] English:** full performance so it's not really a nested simulation it's just another thing that's  
**Translation:** 

**[8081.12s] English:** happening in the universe so that would be interesting but i think it's ultimately a  
**Translation:** Vocabulary: simulation: 模拟

**[8085.80s] English:** theological question and because it's no longer cool to deal with theology as part of science  
**Translation:** 

**[8090.86s] English:** there's not been much work on that you can't publish uh uh results on those topics uh in  
**Translation:** Vocabulary: theological: 神学的

**[8097.28s] English:** a respected physics journal so i think it's kind of been set aside but it's interesting to note  
**Translation:** 

**[8102.68s] English:** that the laws of quantum mechanics themselves have a place for you know god or souls or whatever  
**Translation:** 

**[8107.56s] English:** external source of input you might want to attach to such a thing and that um you know that there's  
**Translation:** 

**[8114.34s] English:** this idea of quantum waves function collapse that when we you know look at a quantum system  
**Translation:** 

**[8119.02s] English:** evolving and perfect superposition of many possibilities and you go to observe it you  
**Translation:** 

**[8122.82s] English:** actually just see a specific possibility the in the multi-slit experiment the light ultimate  
**Translation:** Vocabulary: evolving: 演变; superposition: 叠加态

**[8127.26s] English:** ends up being observed going through one slit or the other and that's a place where there's this  
**Translation:** 

**[8132.56s] English:** random number being injected into everything around us um you know trillions of trillions  
**Translation:** Vocabulary: trillions: 万亿

**[8137.56s] English:** of trillions of times per second and everything we're observing um and if you want to attach some  
**Translation:** 

**[8142.24s] English:** external input well there's a place and it could be seriously accessible through the rigors of  
**Translation:** Vocabulary: rigors: 严酷条件

**[8149.00s] English:** science but we just know so little there yeah it's funny and in that area we know nothing more than  
**Translation:** 

**[8155.28s] English:** um cavemen knew  
**Translation:** Vocabulary: cavemen: 穴居人

**[8157.26s] English:** whatsoever we know the laws of quantum mechanics and we have  
**Translation:** 

**[8160.00s] English:** computers that may be soon more advanced  
**Translation:** 

**[8163.06s] English:** than we are, but we just don't have  
**Translation:** 

**[8165.12s] English:** any answers to the fundamental questions  
**Translation:** 

**[8167.02s] English:** about  
**Translation:** 

**[8167.38s] English:** life, the universe,  
**Translation:** 

**[8171.06s] English:** and everything.  
**Translation:** 

**[8172.56s] English:** Do you think, sort of more practically,  
**Translation:** 

**[8174.82s] English:** do you think we'll create video  
**Translation:** 

**[8177.04s] English:** games,  
**Translation:** 

**[8178.86s] English:** video game worlds  
**Translation:** 

**[8180.18s] English:** of the metaverse variety in which humans  
**Translation:** Vocabulary: metaverse: 元宇宙

**[8184.88s] English:** will want to stay?  
**Translation:** 

**[8188.06s] English:** So,  
**Translation:** 

**[8188.30s] English:** I mean, to me,  
**Translation:** 

**[8190.44s] English:** this kind of discussion of a simulated reality,  
**Translation:** Vocabulary: simulated: 模拟的

**[8192.72s] English:** the real test of immersion is  
**Translation:** 

**[8194.30s] English:** like not wanting to  
**Translation:** Vocabulary: immersion: 全身心投入

**[8196.38s] English:** go back to the real world.  
**Translation:** 

**[8198.18s] English:** As a perfectly healthy,  
**Translation:** 

**[8200.50s] English:** excited, normal human  
**Translation:** 

**[8202.30s] English:** being, choosing  
**Translation:** 

**[8204.16s] English:** to stay in that world.  
**Translation:** 

**[8206.74s] English:** How hard is that, do you think?  
**Translation:** 

**[8208.88s] English:** Well, I think the technology  
**Translation:** 

**[8209.92s] English:** is coming, and then there's a human  
**Translation:** 

**[8212.38s] English:** question of, should we  
**Translation:** 

**[8213.34s] English:** go that far?  
**Translation:** 

**[8214.80s] English:** Should we? Yeah.  
**Translation:** 

**[8216.42s] English:** Certainly as a game developer ourselves,  
**Translation:** 

**[8218.30s] English:** Epic doesn't aspire to that. We make fun  
**Translation:** 

**[8220.30s] English:** games. And, you know,  
**Translation:** 

**[8222.34s] English:** the ultimate manifestation that we found is  
**Translation:** 

**[8224.22s] English:** fun games that people play together to have fun  
**Translation:** Vocabulary: manifestation: 表现形式

**[8226.36s] English:** in between, you know, work and the other  
**Translation:** 

**[8228.30s] English:** things in their real lives.  
**Translation:** 

**[8230.20s] English:** But as the simulations get more and more realistic  
**Translation:** 

**[8232.30s] English:** and the capabilities become more and more real,  
**Translation:** 

**[8234.54s] English:** I think we have to ask ourselves some hard  
**Translation:** 

**[8236.26s] English:** questions about how should humanity  
**Translation:** 

**[8238.24s] English:** operate in that space?  
**Translation:** 

**[8240.16s] English:** What are the limits that we should go to and  
**Translation:** 

**[8241.92s] English:** what are the limits we should set?  
**Translation:** 

**[8243.92s] English:** Yeah, I think there's  
**Translation:** 

**[8244.62s] English:** going to be some hard questions, and I think  
**Translation:** 

**[8248.30s] English:** maybe I'm just being  
**Translation:** 

**[8250.56s] English:** human-centric  
**Translation:** 

**[8252.50s] English:** here, but there should probably be some  
**Translation:** 

**[8254.34s] English:** legal bounds on  
**Translation:** 

**[8255.72s] English:** two things.  
**Translation:** 

**[8258.24s] English:** Sort of not creating a reality in which  
**Translation:** 

**[8260.38s] English:** humans would want to stay too long.  
**Translation:** 

**[8262.92s] English:** Sort of, yeah, focusing more on the  
**Translation:** 

**[8264.40s] English:** game side.  
**Translation:** 

**[8265.98s] English:** And more importantly,  
**Translation:** 

**[8268.28s] English:** not creating  
**Translation:** 

**[8271.72s] English:** simulations of  
**Translation:** 

**[8274.26s] English:** humans that could suffer.  
**Translation:** 

**[8278.30s] English:** To me, you know, as we  
**Translation:** 

**[8280.00s] English:** talked about creating ultra-realistic humans, eventually  
**Translation:** 

**[8283.82s] English:** that means creating humans that can suffer, that can fall in love  
**Translation:** 

**[8287.84s] English:** and experience heartbreak and loss, that can fear death.  
**Translation:** Vocabulary: heartbreak: 心碎

**[8293.04s] English:** And the more you simulate that to the full  
**Translation:** 

**[8295.84s] English:** reality of the human condition, the more you get to this place where you  
**Translation:** Vocabulary: simulate: 模拟

**[8299.86s] English:** have assimilated humans that is able to suffer.  
**Translation:** 

**[8303.72s] English:** I think, legally speaking, I think you have to get to a place where that's not allowed.  
**Translation:** Vocabulary: assimilated: 同化

**[8308.12s] English:** Like there is a line you can't cross.  
**Translation:** 

**[8311.84s] English:** And that's a hard thing for humans to  
**Translation:** 

**[8314.38s] English:** deal with. That's going to be some interesting Supreme Court cases.  
**Translation:** 

**[8320.68s] English:** Once you create a human sufficiently realistic  
**Translation:** Vocabulary: sufficiently: 足够地

**[8324.20s] English:** to where they can suffer, means that human can be  
**Translation:** 

**[8328.00s] English:** tortured and do  
**Translation:** Vocabulary: tortured: 遭受折磨

**[8330.40s] English:** terrible things to that human that's artificial, quote unquote.  
**Translation:** 

**[8336.06s] English:** But boy, that's a  
**Translation:** Vocabulary: unquote: 引号外

**[8338.12s] English:** that still feels wrong. I don't know what that is, but it feels wrong  
**Translation:** 

**[8343.80s] English:** to torture a simulated  
**Translation:** Vocabulary: simulated: 模拟的

**[8347.74s] English:** human. Now, when you play a video game  
**Translation:** 

**[8351.98s] English:** and it's a shooter and everybody's having fun, that doesn't feel  
**Translation:** 

**[8355.86s] English:** wrong. But there's a line. And that's going to be  
**Translation:** 

**[8359.62s] English:** a fascinating line for the Supreme Court to explore.  
**Translation:** 

**[8363.58s] English:** Oh man, what an exciting future we're living in, huh?  
**Translation:** 

**[8368.12s] English:** You know, I think the thing to appreciate is game developers have just generally been  
**Translation:** 

**[8372.10s] English:** on the good spirited side of things. If you look at the worst  
**Translation:** 

**[8376.08s] English:** things that people do in popular video games today,  
**Translation:** 

**[8380.14s] English:** it's like, what, Uraba Bank and GTA? It's clearly fictional and all and fun  
**Translation:** 

**[8383.98s] English:** and not serious and over the top.  
**Translation:** Vocabulary: fictional: 虚构的

**[8387.44s] English:** I think, yeah, as things get more realistic, especially simulation of humans,  
**Translation:** 

**[8392.86s] English:** yeah, there are some hard questions that will have to be answered there.  
**Translation:** Vocabulary: simulation: 模拟

**[8395.56s] English:** But I think the thing that all game developers,  
**Translation:** 

**[8398.12s] English:** need to remember is we're here to  
**Translation:** 

**[8400.00s] English:** make people's lives better by entertaining them providing them with fun um and a diversion from  
**Translation:** 

**[8405.48s] English:** other things and being a part of their lives and not not trying to be too big or being too much  
**Translation:** Vocabulary: diversion: 消遣

**[8412.86s] English:** and not trying to provide an alternate to reality but to just provide a fun source of entertainment  
**Translation:** 

**[8418.46s] English:** like the many other things that people do uh do for fun so uh you've spoken like i mentioned about  
**Translation:** 

**[8423.86s] English:** the metaverse for many years let's step back what is the metaverse and speaking of fun  
**Translation:** 

**[8429.42s] English:** uh you know fortnight you know just hundreds of millions of people just enjoying themselves in  
**Translation:** Vocabulary: fortnight: 周末; metaverse: 虚拟世界

**[8439.46s] English:** this huge scale social game you could call it a metaverse maybe you can describe the different  
**Translation:** 

**[8446.14s] English:** flavors the layers of uh how you see what the metaverse is you know the metaverse is an idea  
**Translation:** 

**[8453.60s] English:** who's dot christ goes up and down depending on who says what yeah on what day um and uh  
**Translation:** 

**[8459.18s] English:** it  
**Translation:** 

**[8459.40s] English:** some have a an ability to drive it way down by opening their mouths um but ultimately this is  
**Translation:** 

**[8465.54s] English:** about uh multiplayer social gaming experiences you and your friends getting together in a 3d world  
**Translation:** 

**[8473.56s] English:** and having fun together in any way you want um you know if you're playing fortnite battle royale  
**Translation:** 

**[8478.40s] English:** i can my view that is capturing the essence of the metaverse and it's especially in fortnite  
**Translation:** Vocabulary: fortnite: 堡垒之夜

**[8482.70s] English:** when we got sony on board so that all players on all platforms in fortnite could play together  
**Translation:** 

**[8487.58s] English:** could voice chat together and be part of a single game experience it really took on a new nature  
**Translation:** 

**[8493.50s] English:** which was not just like a multiplayer game and you know with heritage from doom but also  
**Translation:** 

**[8498.64s] English:** a true social experience between you and your friends um and you know fortnite battle royale  
**Translation:** 

**[8504.76s] English:** is just one manifestation of that another one is like rec room vr where you're standing around in  
**Translation:** 

**[8508.86s] English:** vr with friends playing billiards and or shooting hoops and or doing other like light  
**Translation:** Vocabulary: billiards: 台球; hoops: 篮筐; manifestation: 表现

**[8512.78s] English:** entertainment things i think every game that has  
**Translation:** 

**[8515.42s] English:** a huge number of players  
**Translation:** 

**[8517.58s] English:** who play together socially as part of their  
**Translation:** 

**[8520.00s] English:** you know entertainment lives um i think is is really getting at the core essence of the vision  
**Translation:** 

**[8527.28s] English:** you know aspiration for the metaverse and you know we're still in the very early days of it  
**Translation:** 

**[8531.68s] English:** uh you know i was on the internet in like 1992 or so and uh you know it was a pretty bare-bones  
**Translation:** Vocabulary: aspiration: 向往

**[8538.84s] English:** thing i think when we look back at the state of gaming today we'll realize that we there's a lot  
**Translation:** 

**[8545.06s] English:** further to go to get to the ultimate version of it but you know i think it's all on track and i think  
**Translation:** 

**[8550.00s] English:** it was the time we released fortnite battle royale and started playing together all of  
**Translation:** 

**[8554.50s] English:** all the people at epic and squads and experiencing that world that we realized that this trend was  
**Translation:** 

**[8558.78s] English:** afoot and we needed to do everything we could to give to bring in other creators so that anybody  
**Translation:** 

**[8563.14s] English:** could uh you know pile on to the work we were doing by creating their own worlds um for through  
**Translation:** Vocabulary: afoot: 已经开始

**[8569.80s] English:** fortnite creative and uefn and and creating more games and more genres that people could play and  
**Translation:** 

**[8575.08s] English:** ever expanding the repertoire of fun yeah it i would love to sort of talk about the  
**Translation:** 

**[8579.98s] English:** different aspects of that a little bit more because you know epic has created a lot of amazing  
**Translation:** 

**[8584.02s] English:** games unreal tournament gears of war but the game that i think it's fair to say that transformed the  
**Translation:** 

**[8589.16s] English:** gaming industry was fortnite fortnite battle royale especially can you explain the origin  
**Translation:** 

**[8593.90s] English:** story of fortnite well fortnite has humble beginnings um in 2011 we just uh uh been in  
**Translation:** 

**[8603.48s] English:** the final days of finishing one of the gears of war games and um we'll have to explore ideas for  
**Translation:** 

**[8609.98s] English:** games uh and we had a general idea that we would like to build you know some smaller games online  
**Translation:** 

**[8616.28s] English:** games in order to learn more about uh you know that space uh and not just have one single massive  
**Translation:** 

**[8623.40s] English:** game in production at all times and only one um and so everybody in the company was given a week  
**Translation:** 

**[8628.50s] English:** to form a team and work with whichever co-workers they wanted and uh and build a game um you know  
**Translation:** 

**[8634.38s] English:** using unreal engine so you can actually build something pretty interesting in a week and  
**Translation:** Vocabulary: whichever: 任意的

**[8639.98s] English:** so it was a success and that's the story why it's so important and i think it's important that  
**Translation:** 

**[8644.42s] English:** you guys support the community and the podcast is going to help you guys because we are so  
**Translation:** 

**[8648.12s] English:** grateful that you guys are doing it and you guys are supporting someone that feels that way and  
**Translation:** 

**[8651.48s] English:** that's been a really great thing to do so thank you guys for watching and have a great weekend  
**Translation:** 

**[8655.66s] English:** thank you guys for watching and have a great weekend  
**Translation:** 

**[8640.00s] English:** version of what became fortnight the very first version of it had a different art style but it  
**Translation:** Vocabulary: fortnight: 两周时间

**[8644.68s] English:** had the idea at the core that you're going to build forts by day using this building system  
**Translation:** 

**[8649.38s] English:** then night would come and you defend the forts against zombies and you know the longer you could  
**Translation:** Vocabulary: zombies: 丧尸

**[8653.86s] English:** go the more elaborate forts you could build and the more survival uh you know waves you could  
**Translation:** 

**[8658.02s] English:** withstand and it would get cooler and cooler with time nice and uh you know that game was in  
**Translation:** Vocabulary: elaborate: 复杂; withstand: 承受

**[8663.06s] English:** development for a very long time we always saw the potential just the building aspect of it was  
**Translation:** 

**[8668.52s] English:** incredibly fun but we made different pivots at different times at one point we moved to the  
**Translation:** Vocabulary: pivots: 转变

**[8673.94s] English:** current fortnight art style away from kind of more of a realistic style um made it you know  
**Translation:** 

**[8678.86s] English:** more in the pixar vein of you know cool stylized characters what was that decision like as we  
**Translation:** Vocabulary: stylized: 夸张风格

**[8685.04s] English:** mentioned gears of war is this like incredible like shows off the graphics to the fullest  
**Translation:** 

**[8691.24s] English:** different than the artistic style of fortnight it's amazing that the same company would make  
**Translation:** 

**[8697.28s] English:** this like fun silly  
**Translation:** 

**[8698.52s] English:** graphic style of fortnight you know people come to epic because they want to work with the best  
**Translation:** 

**[8703.74s] English:** people in the world and the artists bring a lot of different personal art aspirations and style  
**Translation:** 

**[8708.02s] English:** capabilities and many of them are very multi-talented can produce photo real content or  
**Translation:** Vocabulary: aspirations: 理想

**[8711.74s] English:** highly stylized content and a lot of the best artists on fortnight were a lot of the best  
**Translation:** 

**[8716.72s] English:** artists on gears of war to uh change styles but continue doing awesome work we'd realize that  
**Translation:** 

**[8722.36s] English:** fortnight could be really mainstream and it could be a game people play for a long time and so having  
**Translation:** 

**[8726.12s] English:** a you know more visually pleasing art style that's  
**Translation:** 

**[8728.52s] English:** you know not as stressful as like a call of duty game where you're constantly like pixel hunting  
**Translation:** 

**[8733.00s] English:** you know a dark scene for uh you know somebody's rifle scope that was the goal so you know a few  
**Translation:** Vocabulary: pixel: 像素

**[8739.48s] English:** of the artists got through and defined new art style and we moved to it and uh at different  
**Translation:** 

**[8743.44s] English:** points it evolved towards being kind of like a light mmo like destiny um with rather complex  
**Translation:** 

**[8748.30s] English:** rpg and stat systems um and that evolved into a you know kind of an umo like tower defense game  
**Translation:** 

**[8754.86s] English:** um mmo only in that persistence of items and stats  
**Translation:** Vocabulary: persistence: 持久性

**[8758.52s] English:** um you know which people  
**Translation:** 

**[8760.00s] English:** became Fortnite Save the World mode, which we launched in early 2017.  
**Translation:** Vocabulary: fortnite: 堡垒之夜

**[8765.08s] English:** And it was a moderate success.  
**Translation:** 

**[8766.62s] English:** You know, it paid its budget, and we'd come out ahead.  
**Translation:** 

**[8769.66s] English:** And then at the same time, the Battle Royale genre was booming.  
**Translation:** 

**[8773.10s] English:** PUBG had just come out.  
**Translation:** 

**[8774.14s] English:** Tons of people at Epic were playing that.  
**Translation:** 

**[8775.60s] English:** They were like, oh, this would be so cool if it had Fortnite building.  
**Translation:** 

**[8778.58s] English:** And so we assembled a team in a war room, you know, like 30 people in one big room.  
**Translation:** 

**[8783.88s] English:** And, you know, they worked insanely hard for four weeks to build Battle Royale.  
**Translation:** Vocabulary: assembled: 组建

**[8788.04s] English:** So the nice thing is all the content for Fortnite had been built over the previous seven years.  
**Translation:** 

**[8792.52s] English:** They had a huge library of content, but no gameplay of the type they wanted.  
**Translation:** 

**[8795.96s] English:** So they had to build it all in that four weeks and ship it.  
**Translation:** 

**[8798.36s] English:** And that put Epic on an exponential growth curve where we went from 300 employees to thousands of employees  
**Translation:** Vocabulary: exponential: 指数的

**[8805.76s] English:** and went from about $100 million in revenue to billions of dollars in revenue  
**Translation:** 

**[8809.70s] English:** and, you know, kind of became the center of the gaming world at the time.  
**Translation:** 

**[8813.68s] English:** Can you actually speak to the technical challenge of going from,  
**Translation:** 

**[8818.04s] English:** from mostly a not online, large-scale gaming platform  
**Translation:** 

**[8824.62s] English:** to being able to support with Battle Royale a huge number of people playing with each other at the same exact time?  
**Translation:** 

**[8832.44s] English:** Like, what's the technical, I mean, four weeks, what's the technical challenges there that had to be overcome?  
**Translation:** 

**[8837.48s] English:** Since 2012, we've been building online backend systems to support player accounts and login  
**Translation:** 

**[8842.42s] English:** and, you know, all of the different systems that are needed to make a multiplayer game.  
**Translation:** Vocabulary: login: 登录

**[8846.48s] English:** And we've been building them to be scalable.  
**Translation:** 

**[8848.04s] English:** And by some miracle, we built them stably enough that they were able to scale up.  
**Translation:** Vocabulary: scalable: 可扩展的; stably: 稳定地

**[8853.66s] English:** And, you know, so the online team was responsible for patching that code,  
**Translation:** 

**[8856.64s] English:** spent a year of intense work getting it to scale from like 40,000 concurrent users to 15 million concurrent users.  
**Translation:** Vocabulary: concurrent: 同时在线; patching: 修复

**[8865.88s] English:** Yeah, I mean, there's scaling, there's scaling. That's a lot.  
**Translation:** 

**[8868.98s] English:** That's immense. But they'd done such an awesome job of building the foundations that it was tractable.  
**Translation:** Vocabulary: immense: 巨大; tractable: 可处理的

**[8875.32s] English:** It was doable.  
**Translation:** 

**[8875.78s] English:** If they hadn't done that, then the company would have died.  
**Translation:** Vocabulary: doable: 可行的

**[8880.00s] English:** you know, Fortnite just wouldn't have been playable  
**Translation:** 

**[8881.50s] English:** and the whole thing would have failed.  
**Translation:** Vocabulary: fortnite: 堡垒之夜

**[8883.64s] English:** I mean, there's just so much detail there  
**Translation:** 

**[8885.78s] English:** that makes all the difference  
**Translation:** 

**[8887.86s] English:** because, I mean, that's what Spotify has talked about,  
**Translation:** 

**[8890.98s] English:** that, like, the latency,  
**Translation:** Vocabulary: latency: 延迟

**[8895.20s] English:** it's like how quickly you can deliver the song  
**Translation:** 

**[8898.54s] English:** changes the product from being this shitty thing  
**Translation:** Vocabulary: shitty: 糟糕的

**[8902.54s] English:** that I'd rather pirate the songs to,  
**Translation:** 

**[8904.90s] English:** like, this is good enough to where I really enjoy the experience  
**Translation:** 

**[8907.68s] English:** and I want to use it.  
**Translation:** 

**[8908.64s] English:** And so, like, yeah, that's really important  
**Translation:** 

**[8912.26s] English:** to create an experience for 15 million concurrent users  
**Translation:** 

**[8917.04s] English:** to where they're not, where it's not lagging,  
**Translation:** Vocabulary: lagging: 延迟

**[8920.56s] English:** where it actually works, right?  
**Translation:** 

**[8923.36s] English:** Is there something you could say to the server,  
**Translation:** 

**[8926.48s] English:** like, how difficult that is to pull off?  
**Translation:** 

**[8930.10s] English:** You know, the trend nowadays for building online services  
**Translation:** 

**[8932.74s] English:** is microservices.  
**Translation:** 

**[8934.28s] English:** There's not one big server that handles  
**Translation:** Vocabulary: microservices: 微服务

**[8936.20s] English:** all the interactions with Fortnite.  
**Translation:** 

**[8938.64s] English:** There's game servers running 100-player game instances  
**Translation:** 

**[8941.96s] English:** for each Battle Royale session.  
**Translation:** 

**[8944.06s] English:** And then there's an account server  
**Translation:** 

**[8946.66s] English:** and many instances of it all talking to a shared database.  
**Translation:** 

**[8949.28s] English:** And there's hundreds of different microservices  
**Translation:** 

**[8951.02s] English:** talking to each other.  
**Translation:** 

**[8952.90s] English:** And so scaling is a matter of identifying  
**Translation:** Vocabulary: identifying: 识别

**[8954.52s] English:** what are the bottlenecks in that system  
**Translation:** 

**[8956.10s] English:** and making sure that each one can scale  
**Translation:** Vocabulary: bottlenecks: 瓶颈

**[8958.72s] English:** and has enough redundancy to be able to handle the load.  
**Translation:** 

**[8964.32s] English:** I mean, thank God for Amazon Web Services and cloud hosting  
**Translation:** 

**[8967.56s] English:** because that's...  
**Translation:** 

**[8968.64s] English:** It went to 15 million concurrent users  
**Translation:** 

**[8970.84s] English:** without buying any server hardware.  
**Translation:** 

**[8973.30s] English:** We were able to just call up Amazon and say,  
**Translation:** 

**[8976.08s] English:** we need more.  
**Translation:** 

**[8977.36s] English:** And there was a period of time there  
**Translation:** 

**[8978.66s] English:** where Fortnite was undergoing this exponential growth  
**Translation:** 

**[8980.80s] English:** and we'd find, like, one week we ran out of servers in Brazil  
**Translation:** Vocabulary: exponential: 成倍的

**[8984.14s] English:** during a heavy weekend of play.  
**Translation:** 

**[8985.98s] English:** And next week, we had an even heavier weekend of play  
**Translation:** 

**[8989.08s] English:** and there were servers to handle it.  
**Translation:** 

**[8990.70s] English:** Like, somebody at Amazon had drop-shipped, you know,  
**Translation:** 

**[8993.68s] English:** millions of dollars of server hardware into Brazil  
**Translation:** 

**[8996.58s] English:** and turned it on just in time for Fortnite.  
**Translation:** 

**[8998.64s] English:** Fortnite to need it.  
**Translation:** 

**[9000.00s] English:** And, you know, there are a lot of unsung heroes in that story, many of whom we've never heard of.  
**Translation:** 

**[9005.46s] English:** Yeah, I mean, behind AWS, many unsung heroes.  
**Translation:** 

**[9010.60s] English:** It's like so much of those folks who run the modern Internet, all the incredible services, the games, the services that we take for granted are currently being run on AWS or were originally, and Google Cloud and so on.  
**Translation:** 

**[9025.10s] English:** But, yeah, can you speak to how much money Fortnite made?  
**Translation:** 

**[9032.16s] English:** So this is one of the greatest successes in the history of video games also.  
**Translation:** Vocabulary: fortnite: 堡垒之夜

**[9036.58s] English:** Fortnite makes billions of dollars a year.  
**Translation:** 

**[9039.98s] English:** And that's the majority of Epic's revenue.  
**Translation:** 

**[9042.62s] English:** We have a robust business around Unreal Engine licensing, Rocket League and Fall Guys, and some other tools like the Fab Content Marketplace.  
**Translation:** 

**[9050.86s] English:** But the majority of it is Fortnite.  
**Translation:** Vocabulary: marketplace: 内容市场; robust: 强大

**[9053.18s] English:** Because we've chosen to reinvest heavily.  
**Translation:** 

**[9055.10s] English:** And building what we think is the future of technology.  
**Translation:** 

**[9058.06s] English:** We're spending more every year than we're making.  
**Translation:** 

**[9061.28s] English:** And for a bit of time, we were spending over a billion dollars a year more than we were making.  
**Translation:** 

**[9065.54s] English:** And we found that to be unsustainable.  
**Translation:** 

**[9067.66s] English:** And we went through some painful layoffs at that time.  
**Translation:** Vocabulary: layoffs: 裁员; unsustainable: 不可持续

**[9071.40s] English:** And then we stabilized.  
**Translation:** 

**[9072.54s] English:** And now we're spending several hundred million dollars a year more than we're making, which we can very well afford to do because we have billions of dollars in the bank.  
**Translation:** Vocabulary: stabilized: 稳定下来

**[9079.74s] English:** You know, thanks to a combination of the profits we made when we were a very small company with a very big game.  
**Translation:** 

**[9085.10s] English:** And because of the investment we've raised, we're not an oil well pumping oil out of the ground where we discovered oil.  
**Translation:** 

**[9091.14s] English:** We are growing to be a future technology powerhouse.  
**Translation:** 

**[9094.78s] English:** And we think the 3D space and the future of real-time 3D simulations is going to be one of the major facets of technology for humanity.  
**Translation:** Vocabulary: facets: 方面; powerhouse: 强国

**[9102.78s] English:** And we're all in investing in that.  
**Translation:** 

**[9105.18s] English:** Yeah, it's exciting to see that investing in a long-term future sort of taking the risk of doing the research and defining the next chapter of Epic.  
**Translation:** 

**[9113.26s] English:** So using the successes of the data.  
**Translation:** 

**[9115.10s] English:** Today to invest into the successes of tomorrow that might look very different, like completely different.  
**Translation:** 

**[9120.00s] English:** And part of that is investing in the developments, the research and the innovation in Unreal Engine.  
**Translation:** 

**[9127.90s] English:** That's right. We're a company that can start working on a project knowing that we won't reach fruition or make any money from it at all for three years, four years, five years.  
**Translation:** 

**[9138.54s] English:** We're totally OK with that. And, you know, that's the cycle that's fueled our growth over time.  
**Translation:** 

**[9143.80s] English:** It's constantly investing in the future and being a serious company that's doing serious R&D side by side with shipping and maintaining products and earning money from them.  
**Translation:** 

**[9154.28s] English:** So can you speak to, I mean, there's several directions here.  
**Translation:** 

**[9157.58s] English:** So one of them, sort of the future evolution of this idea of the metaverse, so potentially creating communities.  
**Translation:** Vocabulary: metaverse: 虚拟世界

**[9167.60s] English:** So Fortnite is this incredible, huge community of humans.  
**Translation:** 

**[9173.80s] English:** You're interacting, but your vision is to go outside of just one game.  
**Translation:** Vocabulary: fortnite: 堡垒之夜

**[9179.70s] English:** So what is the kinds of standards that you're thinking about building such that people can sort of have an identity, almost travel between games and that kind of thing?  
**Translation:** 

**[9191.46s] English:** Let me start with the present of gaming and why it sucks.  
**Translation:** 

**[9195.08s] English:** That's a good start. Sure.  
**Translation:** 

**[9197.34s] English:** Fortnite is an awesome thing. You go into Fortnite, there's, you know, 100 million monthly active users there.  
**Translation:** 

**[9202.68s] English:** There's a huge number of your own.  
**Translation:** 

**[9203.80s] English:** Your friends are there.  
**Translation:** 

**[9204.46s] English:** You can play with them, go from experience to experience seamlessly without leaving the app.  
**Translation:** 

**[9209.34s] English:** There are 100,000 different islands you can play on, and some of them are really awesome, and there are constant new ones coming out and constant things to do.  
**Translation:** Vocabulary: seamlessly: 流畅地

**[9217.90s] English:** If you want to play Roblox, all right, you quit out of the Fortnite app, you launch the Roblox app, different program, different friend system, different account names.  
**Translation:** 

**[9225.90s] English:** Your username in Fortnite and your username in Roblox are different names, and they're not connected to each other.  
**Translation:** 

**[9229.98s] English:** So you have to remake all of your friends and then find different things to play.  
**Translation:** 

**[9233.70s] English:** And now the controls are different, so you have to relearn how, you know, the joystick, mouse, keyboard, controller work.  
**Translation:** Vocabulary: joystick: 操纵杆; remake: 重做

**[9240.00s] English:** in that experience and you have to go from place to place and you buy some stuff in fortnight and  
**Translation:** 

**[9244.06s] English:** it's really cool and you can use it anywhere in fortnight and then you go in roblox and you don't  
**Translation:** Vocabulary: fortnight: 两周

**[9247.70s] English:** have that stuff you have to buy different stuff and that stuff only works in roblox and same with  
**Translation:** 

**[9251.98s] English:** call of duty it's another isolated place um and same with world of warcraft and same with league  
**Translation:** Vocabulary: isolated: 孤立的; warcraft: 战争艺术

**[9257.36s] English:** of legends and every other every place you go is its own unique place different friends different  
**Translation:** 

**[9261.82s] English:** account names different people and there's no social cohesion between them at all and long  
**Translation:** Vocabulary: cohesion: 凝聚力

**[9267.06s] English:** time ago consoles set out to solve this problem by creating their console wide friend system and  
**Translation:** 

**[9271.80s] English:** account so your friend on playstation in one game is your friends on playstation another game but  
**Translation:** Vocabulary: consoles: 游戏机

**[9275.74s] English:** only on playstation if you're on xbox you can't see playstation friends and so you have two  
**Translation:** 

**[9281.40s] English:** basically orthogonal and cross-cutting uh divisions of the world into fiefdoms uh you know  
**Translation:** Vocabulary: fiefdoms: 领地; orthogonal: 垂直

**[9288.06s] English:** which were not created with bad intentions but arose and are you know separated isolated islands  
**Translation:** 

**[9294.28s] English:** one is the platforms and their social services  
**Translation:** 

**[9297.04s] English:** xbox playstation nintendo it's steam epic if you add it to the list and the other is these  
**Translation:** 

**[9302.38s] English:** different games people play and you know because of this weird historical artifact we're we're left  
**Translation:** Vocabulary: artifact: 历史遗物

**[9309.92s] English:** in a world where people can't seamlessly move from games to games bringing their friends and  
**Translation:** 

**[9313.68s] English:** their stuff so the solution to this is to federate and connect all the systems together all the  
**Translation:** 

**[9320.08s] English:** players on all the different platforms can be recognized by their name um and put the at sign  
**Translation:** 

**[9325.44s] English:** in it so your xbox names  
**Translation:** 

**[9327.04s] English:** and your fortnite or epic names and your steam names can all live together and interoperate  
**Translation:** 

**[9332.00s] English:** together in a single space so unifying the social ecosystems is one thing that needs to happen  
**Translation:** Vocabulary: fortnite: 堡垒之夜; interoperate: 协同工作; unifying: 统一

**[9336.28s] English:** the next and bigger challenge is to unify the economies too now i'm not talking about like  
**Translation:** 

**[9344.14s] English:** a sword you have in world of warcraft should work in fortnite every game yeah every game's  
**Translation:** 

**[9350.12s] English:** going to have its own gameplay rules and a lot of games are going to have stuff that only works in  
**Translation:** 

**[9353.74s] English:** them but you know there's a huge set of games that are going to have stuff that only works in them  
**Translation:** 

**[9357.04s] English:** but you know there's a huge set of games that are going to have stuff that only works in them  
**Translation:** 

**[9357.06s] English:** have in common the idea of a cosmetic system  
**Translation:** Vocabulary: cosmetic: 外观系统

**[9360.00s] English:** that does not affect gameplay outcomes,  
**Translation:** 

**[9362.90s] English:** but is purely cool looks and cool appearances.  
**Translation:** 

**[9367.98s] English:** Most of the major multiplayer games have them.  
**Translation:** 

**[9371.50s] English:** And if you look at games,  
**Translation:** 

**[9373.52s] English:** you could probably bundle together about 70% of them  
**Translation:** 

**[9375.78s] English:** and say they're similar enough that they could actually interoperate.  
**Translation:** Vocabulary: bundle: 捆绑在一起

**[9378.84s] English:** You could own an outfit in Fortnite,  
**Translation:** 

**[9380.46s] English:** own an outfit in Roblox,  
**Translation:** 

**[9382.46s] English:** and own the same outfit in maybe Call of Duty,  
**Translation:** 

**[9385.04s] English:** and maybe 100 or 200 other games,  
**Translation:** 

**[9388.22s] English:** and actually expect they would work together.  
**Translation:** 

**[9390.76s] English:** And you find other kinds of items are probably interoperable too,  
**Translation:** Vocabulary: interoperable: 可以互操作的

**[9393.62s] English:** like Fortnite has car outfits,  
**Translation:** 

**[9395.26s] English:** so you can buy different appearances of a car.  
**Translation:** 

**[9399.28s] English:** And when you find a physical car in the world of Fortnite,  
**Translation:** 

**[9401.20s] English:** if you're the first person to get into it in that session,  
**Translation:** 

**[9403.96s] English:** boom, it takes on your chosen car cosmetic.  
**Translation:** 

**[9408.20s] English:** And now you have a cool car.  
**Translation:** 

**[9409.86s] English:** It's identifiable as yours.  
**Translation:** 

**[9412.64s] English:** We realized early on with Fortnite  
**Translation:** Vocabulary: identifiable: 可识别的

**[9415.30s] English:** that the key to making Fortnite work as a creator economy  
**Translation:** 

**[9418.18s] English:** was to open up the revenue from the item shop  
**Translation:** 

**[9421.58s] English:** to all of those sources of engagement, right?  
**Translation:** 

**[9423.64s] English:** There are two big things happening in Fortnite  
**Translation:** 

**[9426.62s] English:** that make it work as a product and as a business.  
**Translation:** 

**[9429.00s] English:** One is the game modes, Fortnite Battle Royale,  
**Translation:** 

**[9431.94s] English:** and all of the user modes and everything else  
**Translation:** 

**[9433.56s] English:** are sources of engagement.  
**Translation:** 

**[9434.68s] English:** People play there because it's super fun.  
**Translation:** 

**[9437.28s] English:** And because they're playing there,  
**Translation:** 

**[9438.98s] English:** they're willing to buy cool stuff  
**Translation:** 

**[9440.74s] English:** to make their character look cooler.  
**Translation:** 

**[9443.88s] English:** And so you have all of these sources of engagement,  
**Translation:** 

**[9445.66s] English:** but the sources of engagement don't make money directly.  
**Translation:** 

**[9448.18s] English:** You can't spend money in Fortnite Battle Royale  
**Translation:** 

**[9450.46s] English:** to buy a game item.  
**Translation:** 

**[9452.64s] English:** Like everything's, you know,  
**Translation:** 

**[9453.66s] English:** the gameplay is not pay to win  
**Translation:** 

**[9454.94s] English:** and it's all just a game.  
**Translation:** 

**[9457.06s] English:** So we make money from the item shop.  
**Translation:** 

**[9459.84s] English:** And the item shop only exists  
**Translation:** 

**[9461.58s] English:** because of the sources of engagement.  
**Translation:** 

**[9463.52s] English:** If you weren't playing Battle Royale,  
**Translation:** 

**[9464.70s] English:** trust me, nobody would want to buy a Fortnite outfit.  
**Translation:** Vocabulary: fortnite: 不朽战士

**[9466.64s] English:** If you weren't playing any Fortnite games,  
**Translation:** 

**[9468.06s] English:** why would you buy Fortnite outfits?  
**Translation:** 

**[9469.96s] English:** And so you have all the revenue in this item shop economy  
**Translation:** 

**[9473.02s] English:** and all the engagement in this engagement economy.  
**Translation:** 

**[9475.64s] English:** And the thing that magically makes  
**Translation:** 

**[9476.86s] English:** the Fortnite creator economy work,  
**Translation:** 

**[9478.18s] English:** is revenue sharing.  
**Translation:** 

**[9480.00s] English:** spending according to sources  
**Translation:** 

**[9482.02s] English:** of engagement by engagement.  
**Translation:** 

**[9483.78s] English:** If you buy an item and you've played  
**Translation:** 

**[9486.02s] English:** 40% of your time in Battle Royale  
**Translation:** 

**[9488.16s] English:** and 60% of your time in these user  
**Translation:** 

**[9489.96s] English:** modes, the money you spent, the  
**Translation:** 

**[9491.96s] English:** portion of that that's profit can be separated  
**Translation:** 

**[9494.08s] English:** out and paid out to all the different  
**Translation:** 

**[9495.82s] English:** creators who participate in that economy.  
**Translation:** 

**[9498.44s] English:** And that's why Fortnite scaled up to a  
**Translation:** 

**[9499.94s] English:** $400 million creator  
**Translation:** 

**[9501.92s] English:** economy so far and is growing.  
**Translation:** 

**[9504.00s] English:** It's amazing. One of the really critical  
**Translation:** 

**[9505.82s] English:** things we aim to do in designing  
**Translation:** 

**[9508.00s] English:** that is ensure it's a creator economy that's  
**Translation:** 

**[9510.00s] English:** could scale to other companies,  
**Translation:** 

**[9512.10s] English:** other ecosystems, and say  
**Translation:** 

**[9514.02s] English:** right now we have many industry  
**Translation:** 

**[9516.18s] English:** standards bodies. One  
**Translation:** 

**[9517.94s] English:** standardized game ratings,  
**Translation:** 

**[9519.88s] English:** age ratings of games, another standardized  
**Translation:** Vocabulary: standardized: 标准化的

**[9522.06s] English:** file formats for  
**Translation:** 

**[9524.08s] English:** the web, another standardizing  
**Translation:** Vocabulary: standardizing: 标准化

**[9526.34s] English:** file formats for 3D  
**Translation:** 

**[9527.54s] English:** like Kronos Groups and the Metaverse Standards Forum.  
**Translation:** Vocabulary: kronos: kronos时序; metaverse: 元宇宙

**[9530.72s] English:** If we had a standards body  
**Translation:** 

**[9532.16s] English:** standardize what are  
**Translation:** Vocabulary: standardize: 制定标准

**[9533.96s] English:** portable outfits in games,  
**Translation:** 

**[9535.90s] English:** game outfits you could buy in one game  
**Translation:** 

**[9537.88s] English:** that work in another, what are their  
**Translation:** 

**[9539.72s] English:** dimensions and what are their capabilities  
**Translation:** Vocabulary: dimensions: 尺寸

**[9541.86s] English:** and what can you do and what can't  
**Translation:** 

**[9543.92s] English:** you do and so on.  
**Translation:** 

**[9545.80s] English:** Then you could have an item economy where  
**Translation:** 

**[9547.92s] English:** every game agrees to respect  
**Translation:** 

**[9549.92s] English:** each other's item purchases of  
**Translation:** 

**[9551.96s] English:** that sort. And revenue is shared between  
**Translation:** 

**[9554.04s] English:** ecosystems as well. That would be  
**Translation:** 

**[9555.90s] English:** incredible. That would be so amazing.  
**Translation:** 

**[9558.44s] English:** Is there, first of all,  
**Translation:** 

**[9559.60s] English:** it seems silly  
**Translation:** 

**[9561.04s] English:** maybe for people who don't  
**Translation:** 

**[9563.88s] English:** play video games, but an outfit is an  
**Translation:** 

**[9565.78s] English:** important, if an outfit  
**Translation:** 

**[9567.88s] English:** can be persistent across  
**Translation:** Vocabulary: persistent: 持久的

**[9569.64s] English:** video games.  
**Translation:** 

**[9571.78s] English:** I mean, I don't know. What's the purpose  
**Translation:** 

**[9573.86s] English:** of life? Why do we  
**Translation:** 

**[9575.80s] English:** wear clothing? Clothing is a  
**Translation:** 

**[9577.80s] English:** part of our identity.  
**Translation:** 

**[9579.70s] English:** It's how we present ourselves to the world.  
**Translation:** 

**[9581.76s] English:** I wear this stupid suit and tie.  
**Translation:** 

**[9584.32s] English:** It feels good. It feels good when I  
**Translation:** 

**[9585.72s] English:** put it on.  
**Translation:** 

**[9587.42s] English:** Even the other outfit, I have two outfits.  
**Translation:** 

**[9590.04s] English:** This and then a black t-shirt  
**Translation:** 

**[9591.84s] English:** and jeans.  
**Translation:** 

**[9593.78s] English:** It feels good to wear that. It feels  
**Translation:** 

**[9595.76s] English:** like me when I look in the mirror. Okay,  
**Translation:** 

**[9597.66s] English:** I know that guy.  
**Translation:** 

**[9599.64s] English:** Beautiful.  
**Translation:** 

**[9600.00s] English:** to have that outfit go from game to game to game maybe across the years that would be wonderful  
**Translation:** 

**[9605.40s] English:** the i wonder if you could just even comment could there also be another standardization about  
**Translation:** Vocabulary: standardization: 标准化

**[9612.14s] English:** the value so for more complicated items so you know take a sword from diablo  
**Translation:** 

**[9619.40s] English:** and transfer to a gun in fortnite but based on the value some you know some generic concept of  
**Translation:** Vocabulary: diablo: Diablo游戏; fortnite: 堡垒之夜

**[9629.06s] English:** money so the value of a thing in one game versus the value of a thing in another game  
**Translation:** 

**[9634.66s] English:** where you're almost operating in this in the in the space of value versus the actual  
**Translation:** 

**[9639.42s] English:** items or is that already getting too um too general i think this can be done um  
**Translation:** 

**[9648.18s] English:** you know we did a lot of analysis of the fortnite economy and found that um some fortnite  
**Translation:** 

**[9655.98s] English:** experiences lead to or correlate with  
**Translation:** 

**[9659.06s] English:** higher spending than others um and you know battle royale uh is relatively strong in that area  
**Translation:** Vocabulary: correlate: 相关联

**[9667.08s] English:** because you see your character from behind and uh see all of your other characters from the front  
**Translation:** 

**[9672.14s] English:** and you have lots of opportunities to really see who you are and to emote and to interact with other  
**Translation:** Vocabulary: emote: 表达情感

**[9676.34s] English:** players um and a lot of games uh have that characteristic one one funny anomaly stood  
**Translation:** 

**[9683.44s] English:** out there's this game that was one of the big breakthroughs in fortnite only up  
**Translation:** Vocabulary: anomaly: 异常; breakthroughs: 突破; characteristic: 特征

**[9687.54s] English:** it's a game where you just climb  
**Translation:** 

**[9689.06s] English:** up and up by following uh paths of stacks of objects and things it was uh just stupid fun  
**Translation:** 

**[9694.24s] English:** everybody loved um we found people weren't spending a lot of money uh on outfits when  
**Translation:** 

**[9700.60s] English:** they were playing only up and it's kind of intuitive actually like you're not seeing  
**Translation:** Vocabulary: intuitive: 直观的

**[9704.24s] English:** other players like if you see anything like you're you're seeing their butt as you're like  
**Translation:** 

**[9708.14s] English:** trying to catch up to them jumping from object to object um and they're above you um and so you  
**Translation:** 

**[9713.24s] English:** know it wasn't a mode that showed off outfits very much but you could you know you can determine the  
**Translation:** 

**[9719.06s] English:** direction between uh  
**Translation:** 

**[9720.00s] English:** a game mode and spending that's so fascinating i mean fortnite is this gigantic economy where  
**Translation:** 

**[9725.98s] English:** you could do those kinds of studies you can understand markets the digital markets as they  
**Translation:** Vocabulary: gigantic: 巨大的

**[9730.20s] English:** emerge amongst humans and what they value and from that value you can probably have a very stable  
**Translation:** 

**[9735.44s] English:** kind of money that emerges yeah i think so you don't need like an alternate currency system you  
**Translation:** 

**[9741.20s] English:** know unfortunately a bunch of ideas have been conflated because people are trying to hype up  
**Translation:** 

**[9744.90s] English:** different things but you know this idea of large-scale multiplayer social gaming um you  
**Translation:** Vocabulary: conflated: 混淆

**[9750.30s] English:** know that notion of the metaverse uh you know there's 600 to 800 million people playing that  
**Translation:** 

**[9757.38s] English:** kind of game every month um so like you know that's real and that's happening and it's you  
**Translation:** Vocabulary: metaverse: 虚拟世界

**[9761.20s] English:** know very much underway uh vr has a much smaller audience i don't think you need vr to have  
**Translation:** 

**[9766.38s] English:** anything like this vr is hardware that may or may not enhance the experience for some usage cases  
**Translation:** Vocabulary: underway: 已经启动

**[9771.68s] English:** for some it will probably be better and for some it will probably be worse but  
**Translation:** 

**[9774.80s] English:** certainly there's not any uh set of battle royale players uh flocking to uh flocking to vr um the  
**Translation:** Vocabulary: flocking: 蜂拥

**[9782.58s] English:** other thing is nft is it's like you know trying to equate digital or cryptocurrency to to the  
**Translation:** 

**[9789.32s] English:** metaverse it's like well you know it's just a way of denoting money or value exchange um you can do  
**Translation:** Vocabulary: cryptocurrency: 加密货币; equate: 等同于

**[9795.92s] English:** that with money or you can do it with nfts or whatever but there's nothing about this future  
**Translation:** 

**[9800.54s] English:** digital economy that fundamentally requires cryptocurrency or whatever what you need is  
**Translation:** Vocabulary: fundamentally: 本质上

**[9804.78s] English:** interoperability interoperability can happen through a blockchain it can happen through a  
**Translation:** 

**[9808.74s] English:** database it can happen through standards bodies what's defining standards and protocols and we've  
**Translation:** Vocabulary: interoperability: 不同系统互通

**[9813.24s] English:** been doing it for hundreds of years since the railroads were standardized and um you know it's  
**Translation:** 

**[9818.94s] English:** not something that totally requires a novel technological solution yeah i mean even on the  
**Translation:** 

**[9827.24s] English:** topic of cryptocurrency it's it's very frustrating  
**Translation:** 

**[9829.62s] English:** you  
**Translation:** Vocabulary: frustrating: 令人沮丧的

**[9830.54s] English:** you know blockchain and crypto is a really powerful  
**Translation:** 

**[9834.26s] English:** technology that i think can enable a lot of the things we're talking  
**Translation:** Vocabulary: crypto: 加密货币

**[9840.00s] English:** about but so many people use it to try to to try to make money to create these bubbles and they the  
**Translation:** 

**[9846.96s] English:** hype and the meme coins and that's on and so forth that becomes much less about that that uh uh drifts  
**Translation:** 

**[9854.14s] English:** far away and rapidly from things that are actually of value which is the experience of playing  
**Translation:** 

**[9861.42s] English:** fortnite and how you look when you play battle royale that's i mean it sounds ridiculous to say  
**Translation:** Vocabulary: fortnite: 堡垒之夜

**[9866.44s] English:** but it's true that's valuable that's that's like you know you have like gold in the physical space  
**Translation:** 

**[9872.42s] English:** we know that holds value uh how how your outfit looks like in fortnite that as as you're saying  
**Translation:** 

**[9880.54s] English:** provably holds value and so you want to connect like a standard uh definition of money value  
**Translation:** 

**[9890.18s] English:** to that and not let it become this hype thing which nfts that you mentioned  
**Translation:** Vocabulary: provably: 可以证明地

**[9896.32s] English:** are  
**Translation:** 

**[9896.44s] English:** just become that it like it quickly drifts away into the land of when people trying to buy and  
**Translation:** 

**[9901.84s] English:** sell and try to make money versus like staying close to the thing that people actually value  
**Translation:** 

**[9907.28s] English:** forget the money it's more about exchanging valuable experiences or things of value  
**Translation:** 

**[9913.48s] English:** so you can uh play fortnite and then go to another video game and continue the valuable  
**Translation:** 

**[9922.80s] English:** experience and then come back to fortnite and do that kind of thing  
**Translation:** 

**[9925.82s] English:** so  
**Translation:** 

**[9926.44s] English:** you're saying this there might be a way to do that and to to basically create standards the  
**Translation:** 

**[9933.74s] English:** way the web has different standards for for displaying websites and all this kind of stuff  
**Translation:** 

**[9940.34s] English:** or the the communication that's required on the networking side so all the different standards  
**Translation:** 

**[9944.64s] English:** that make the web work there need to be those kinds of standards like what what would those  
**Translation:** 

**[9949.74s] English:** those standards look like to enable the metaverse we need a lot of different things um the one area  
**Translation:** Vocabulary: metaverse: 元宇宙

**[9955.40s] English:** where the standards probably  
**Translation:** 

**[9956.32s] English:** have been very successful in creating working standards implemented by all the major  
**Translation:** 

**[9960.00s] English:** engines today is in low-level file formats for data interchange you know the web has png files  
**Translation:** 

**[9966.48s] English:** for 2d images and mp3 files for audio and 3d has the pixar usd file format the universal scene  
**Translation:** Vocabulary: interchange: 信息交换

**[9976.42s] English:** description which is a description of the scene graph the entire set of objects in the scene and  
**Translation:** 

**[9980.66s] English:** all of their parameters so that any engine that supports those features could import that and  
**Translation:** 

**[9984.98s] English:** then render the same scene as the engine they came from you know large parts of this work across  
**Translation:** 

**[9990.24s] English:** unreal engine unity and blender and all these 3d packages of different sorts and there's the gl tf  
**Translation:** Vocabulary: render: 渲染

**[9996.52s] English:** texture format which stores textures and geometry and other low-level data for 3d objects you know  
**Translation:** 

**[10002.38s] English:** when you see a fortnite character that file format together with the image file formats can store  
**Translation:** Vocabulary: fortnite: 堡垒之夜; geometry: 几何数据

**[10007.30s] English:** their static appearance their uh you know the shape of their body um even their animations  
**Translation:** 

**[10013.20s] English:** and their different poses  
**Translation:** Vocabulary: animations: 动作

**[10014.74s] English:** and the appearance of them the different standard file formats could store their all the sounds they  
**Translation:** 

**[10020.16s] English:** make and their emotes but we're still missing a bunch of pieces um the biggest missing piece is  
**Translation:** 

**[10025.40s] English:** the programming language that's uh at the center of standardizing the matterverse now um if you  
**Translation:** 

**[10030.44s] English:** look at the web the web is a combination of a bunch of different technologies the two biggest  
**Translation:** Vocabulary: matterverse: 物质宇宙; standardizing: 标准化

**[10035.34s] English:** ones are html which describes the 2d scene graph or the you know 2d layout of controls and objects  
**Translation:** 

**[10042.92s] English:** on the web page um  
**Translation:** Vocabulary: layout: 布局

**[10044.74s] English:** and but that's just static data it's just a non-moving non-animating web page and then you  
**Translation:** 

**[10049.88s] English:** have the javascript programming language which is used to manipulate that to display things to the  
**Translation:** Vocabulary: manipulate: 操作

**[10054.64s] English:** user and to implement anything you could implement in code so it's a little programming language that  
**Translation:** 

**[10059.06s] English:** runs in your web browser um and the metaverse needs something that performs that similar role  
**Translation:** 

**[10064.10s] English:** but the metaverse and 3d gaming in general needs something that's rather more powerful more safe  
**Translation:** 

**[10071.72s] English:** more scalable and uh more capable than java 3d and 3d gaming in general needs something that's  
**Translation:** Vocabulary: metaverse: 元宇宙; scalable: 可扩展的

**[10074.74s] English:** more powerful than java script because the metaverse is actually a more difficult technical  
**Translation:** 

**[10077.88s] English:** problem than a web page  
**Translation:** 

**[10080.00s] English:** A web page, like an app, is just a single bundle of code and content that somebody, a company, has prepared.  
**Translation:** 

**[10088.66s] English:** And they release it, and it stays exactly what it is until they release a new version.  
**Translation:** Vocabulary: bundle: 代码内容包

**[10092.56s] English:** And it's upgraded from version to version as it goes.  
**Translation:** 

**[10095.58s] English:** But the metaverse needs to be a composite of code and content built by millions of different people that could potentially form a seamless world together.  
**Translation:** Vocabulary: composite: 合成一体; seamless: 无缝连接; upgraded: 升级

**[10104.70s] English:** Yes, fully distributed, collaborative. First of all, also the amount of data.  
**Translation:** 

**[10112.44s] English:** I mean, it doesn't have to be that way, but websites are showing very little information.  
**Translation:** Vocabulary: collaborative: 协作的

**[10118.60s] English:** The metaverse, even when it looks like something like Fortnite, just the amount of information that's conveyed in the scene graph as the individual players are collaborating is a huge, huge, huge amount.  
**Translation:** 

**[10134.12s] English:** Yeah.  
**Translation:** Vocabulary: collaborating: 合作; conveyed: 传递; fortnite: 堡垒之夜

**[10134.70s] English:** The highest detail of Fortnite updates amount to about 60 gigabytes of data.  
**Translation:** 

**[10140.66s] English:** And, you know, that's just a small part of what exists in the Fortnite creative economy.  
**Translation:** Vocabulary: gigabytes: 吉字节

**[10145.22s] English:** And if you look at what this might be in a decade as standards emerge, you might have exabytes of data out there.  
**Translation:** 

**[10152.44s] English:** Fortnite Battle Royale is, I don't think, the ultimate manifestation of gameplay that will ever be invented.  
**Translation:** Vocabulary: exabytes: 万亿字节; manifestation: 表现形式

**[10157.70s] English:** What we've seen time and time again is that as we gain more technical capabilities, graphics get specialized.  
**Translation:** 

**[10164.70s] English:** More capable CPUs become more performant.  
**Translation:** 

**[10167.72s] English:** You know, web services become ever more scalable.  
**Translation:** 

**[10171.60s] English:** We see new genres of games that emerge that weren't possible before.  
**Translation:** 

**[10175.44s] English:** And, you know, Doom ushered in the era of Deathmatch, the first time 3D multiplayer game was even possible at all.  
**Translation:** 

**[10182.68s] English:** You know, the early Battle Royale games, starting about 10 years, 15 years ago, only became possible back then.  
**Translation:** 

**[10190.02s] English:** You couldn't have built one 20 years ago because you just couldn't have rendered an environment.  
**Translation:** 

**[10194.26s] English:** That's as large as a VR game with that many players with that level of interaction and performance.  
**Translation:** 

**[10199.48s] English:** It was just.  
**Translation:** 

**[10200.00s] English:** not possible to run it so you got a certain level of technical capabilities and the genre came out  
**Translation:** 

**[10205.04s] English:** that proved to be by far the best shooter genre ever invented but i think there are numerous  
**Translation:** 

**[10209.76s] English:** numerous more genres some of which are better than any of the existing ones that will be invented as  
**Translation:** 

**[10214.08s] English:** we get more and more capabilities you know some of the capabilities we're lacking now are the ability  
**Translation:** 

**[10219.18s] English:** to build environments uh and game simulations that span more than work than a single company  
**Translation:** 

**[10226.16s] English:** can possibly create and you know you see kind of the birth of that idea in fortnite and roblox  
**Translation:** 

**[10230.44s] English:** where there are tens of thousands of creators each building content users are playing meaningful  
**Translation:** 

**[10234.30s] English:** amounts of it all and so there's an ecosystem that's scaled larger than company but it's still  
**Translation:** 

**[10239.34s] English:** very much you go into one island and you play that creator's work the other direction of its  
**Translation:** 

**[10243.36s] English:** scalability is putting more and more of people's work together in a seamless continuous play space  
**Translation:** 

**[10248.28s] English:** if for games where that makes sense you know you can imagine a a game taking place in an environment  
**Translation:** Vocabulary: scalability: 可扩展性; seamless: 无缝的

**[10254.92s] English:** that's the size of  
**Translation:** 

**[10256.08s] English:** you know you can imagine a a game taking place in an environment that's the size of  
**Translation:** 

**[10256.14s] English:** you know you can imagine a a game taking place in an environment that's the size of  
**Translation:** 

**[10256.16s] English:** a continent or earth um in which you can like go from place to place and then see different areas  
**Translation:** 

**[10262.96s] English:** which are maintained by different people as you go into different spaces the game rules are  
**Translation:** 

**[10267.00s] English:** customized according to that and you can go from experience to experience and instead of having  
**Translation:** 

**[10272.42s] English:** just one company's authorship ever present wherever you are you know you'd see you'd be  
**Translation:** 

**[10277.44s] English:** driving a car built by one person carrying weapons built by 20 other people um and you know taking  
**Translation:** Vocabulary: authorship: 独创性

**[10284.08s] English:** place in a simulation in an environment that's  
**Translation:** 

**[10286.14s] English:** built by thousands of other people uh you know and working for separate companies or their own  
**Translation:** Vocabulary: simulation: 模拟环境

**[10291.12s] English:** you know entrepreneurs or uh indies or enthusiasts all working together simultaneously and we totally  
**Translation:** 

**[10297.96s] English:** lack the programming foundations for that uh you know the the kinds of code you would need to write  
**Translation:** Vocabulary: entrepreneurs: 企业家; indies: 独立制作者

**[10302.82s] English:** now are uh to make that happen or just not practical and so we're investing massively  
**Translation:** 

**[10307.78s] English:** in building new programming language technologies around verse and our proposed standards uh for  
**Translation:** Vocabulary: massively: 大规模地

**[10312.90s] English:** you know future metaverse programming uh that we hope will solve  
**Translation:** 

**[10316.06s] English:** those kinds of problems and make that kind of world possible  
**Translation:** Vocabulary: metaverse: 虚拟宇宙

**[10320.00s] English:** So, first of all, that's a super exciting future where, you know, it's not hundreds or thousands.  
**Translation:** 

**[10327.86s] English:** It's millions of creators that can just create different small or big elements of a world as big as Earth.  
**Translation:** 

**[10338.02s] English:** Just if you sort of close your eyes and imagine that world, that's really exciting.  
**Translation:** 

**[10342.96s] English:** Where it's not a centralized company controlling the release of a particular island or so on.  
**Translation:** 

**[10348.72s] English:** It's people constantly dynamically modifying all the islands of reality in this digital world.  
**Translation:** 

**[10357.32s] English:** So, if you could speak to some of the technologies that can enable that.  
**Translation:** Vocabulary: dynamically: 不断变化; modifying: 修改

**[10362.38s] English:** You mentioned the verse programming language.  
**Translation:** 

**[10364.36s] English:** First of all, also, how legit is it for you, CEO of Epic Games, to be a co-author?  
**Translation:** Vocabulary: legit: 合法合规

**[10371.48s] English:** The programming language theorists are losing their mind.  
**Translation:** 

**[10376.18s] English:** So, co-author on a paper that's described.  
**Translation:** Vocabulary: theorists: 理论家

**[10378.88s] English:** Some of the sort of nuanced details of a programming language.  
**Translation:** 

**[10381.54s] English:** So, maybe you could speak to this programming language called Verse.  
**Translation:** Vocabulary: nuanced: 细腻的

**[10385.80s] English:** It's a functional logic language.  
**Translation:** 

**[10389.78s] English:** What are some cool features of Verse?  
**Translation:** 

**[10392.70s] English:** Verse is a programming language that we're building for large-scale simulation programming.  
**Translation:** 

**[10398.48s] English:** It's designed to make it easy to write code that can scale up to not only you building a Fortnite island,  
**Translation:** Vocabulary: fortnite: 堡垒之夜

**[10406.74s] English:** but you building.  
**Translation:** 

**[10408.72s] English:** Modules or components that can be used by millions of other programmers and co-exist in a huge environment.  
**Translation:** Vocabulary: programmers: 程序员

**[10414.72s] English:** And also can scale up to a huge scale simulation.  
**Translation:** 

**[10418.78s] English:** Some games will be small.  
**Translation:** Vocabulary: simulation: 模拟

**[10420.16s] English:** Battle Royale might find that 100 players is actually optimal.  
**Translation:** 

**[10425.32s] English:** It might be the 1,000 player version of Battle Royale would be worse.  
**Translation:** 

**[10428.04s] English:** But I bet there are 1,000 million and tens of million player experiences.  
**Translation:** 

**[10433.58s] English:** They're even better than that that will yet to be discovered.  
**Translation:** 

**[10436.62s] English:** And so...  
**Translation:** 

**[10437.02s] English:** Wait a minute.  
**Translation:** 

**[10437.90s] English:** Tens of millions...  
**Translation:** 

**[10440.00s] English:** of players together?  
**Translation:** 

**[10443.16s] English:** Sure.  
**Translation:** 

**[10443.58s] English:** We've had Fortnite events  
**Translation:** 

**[10445.38s] English:** that have attracted  
**Translation:** 

**[10446.08s] English:** 15 million concurrent users,  
**Translation:** Vocabulary: concurrent: 同时在线的

**[10448.50s] English:** but the fact that  
**Translation:** 

**[10449.98s] English:** they're all divided up  
**Translation:** 

**[10451.34s] English:** into servers  
**Translation:** 

**[10452.12s] English:** with 100 players each  
**Translation:** 

**[10453.34s] English:** for those events  
**Translation:** 

**[10454.14s] English:** isn't really a positive.  
**Translation:** 

**[10456.04s] English:** It's just a limitation  
**Translation:** 

**[10457.04s] English:** of the technology.  
**Translation:** 

**[10458.72s] English:** Tracing back to Unreal Engine 1  
**Translation:** 

**[10460.20s] English:** and its single-threading decisions,  
**Translation:** 

**[10462.68s] English:** if we could build a concert  
**Translation:** 

**[10463.92s] English:** where all the concert participants,  
**Translation:** 

**[10465.96s] English:** potentially tens of millions of them,  
**Translation:** 

**[10467.26s] English:** could participate together  
**Translation:** 

**[10468.30s] English:** simultaneously and see  
**Translation:** 

**[10469.50s] English:** that there's that massive crowd  
**Translation:** 

**[10470.86s] English:** and they could all do  
**Translation:** 

**[10472.10s] English:** interesting things  
**Translation:** 

**[10472.80s] English:** and interact with each other,  
**Translation:** 

**[10473.94s] English:** that would be way cooler.  
**Translation:** 

**[10475.56s] English:** Sorry, I'm just loading it in.  
**Translation:** 

**[10478.82s] English:** Just imagining together  
**Translation:** 

**[10480.58s] English:** in one scene graph  
**Translation:** 

**[10483.94s] English:** 10 million people interacting.  
**Translation:** 

**[10487.20s] English:** What a cool world that is.  
**Translation:** 

**[10489.04s] English:** Sure.  
**Translation:** 

**[10489.50s] English:** Well, you have 10 million people.  
**Translation:** 

**[10490.86s] English:** You have less than 10 million pixels  
**Translation:** Vocabulary: pixels: 像素

**[10492.24s] English:** on your screen,  
**Translation:** 

**[10493.00s] English:** so as the Nyquist sampling theorem says,  
**Translation:** Vocabulary: nyquist: 奈奎斯特; theorem: 采样定理

**[10495.02s] English:** it says that you don't need  
**Translation:** 

**[10496.26s] English:** full overhead for every player.  
**Translation:** 

**[10497.70s] English:** You need to render the players  
**Translation:** 

**[10498.70s] English:** you're around you  
**Translation:** Vocabulary: render: 呈现

**[10499.30s] English:** in some approximation  
**Translation:** 

**[10500.20s] English:** of everything else.  
**Translation:** Vocabulary: approximation: 近似

**[10501.14s] English:** Yeah, Tim, but there's also  
**Translation:** 

**[10502.00s] English:** a networking component.  
**Translation:** 

**[10503.46s] English:** Like, you're speaking  
**Translation:** 

**[10505.00s] English:** to the rendering,  
**Translation:** 

**[10505.98s] English:** but like, oh boy.  
**Translation:** 

**[10508.26s] English:** There's a lot of work  
**Translation:** 

**[10509.02s] English:** that has to happen there,  
**Translation:** 

**[10509.90s] English:** but you know,  
**Translation:** 

**[10510.38s] English:** this is what we do for a living.  
**Translation:** 

**[10511.64s] English:** We solve hard problems.  
**Translation:** 

**[10512.34s] English:** I understand.  
**Translation:** 

**[10513.10s] English:** Because if they're easy,  
**Translation:** 

**[10514.20s] English:** then other people  
**Translation:** 

**[10514.76s] English:** could have solved them already.  
**Translation:** 

**[10516.08s] English:** That's really cool, though.  
**Translation:** 

**[10517.30s] English:** Just sort of the possibility,  
**Translation:** 

**[10519.12s] English:** the vision of that  
**Translation:** 

**[10519.88s] English:** is really cool.  
**Translation:** 

**[10521.00s] English:** Even just, you know,  
**Translation:** 

**[10521.94s] English:** even 100,000 people  
**Translation:** 

**[10523.36s] English:** or like bring 10,000 together  
**Translation:** 

**[10525.68s] English:** just to, I mean,  
**Translation:** 

**[10527.02s] English:** there's a reason  
**Translation:** 

**[10529.30s] English:** in the physical world  
**Translation:** 

**[10530.32s] English:** when you go to a concert  
**Translation:** 

**[10531.34s] English:** and you have all those people  
**Translation:** 

**[10533.12s] English:** around you, that energy,  
**Translation:** 

**[10534.44s] English:** or you go to a football game,  
**Translation:** 

**[10536.40s] English:** that energy is unlike anything else.  
**Translation:** 

**[10538.76s] English:** And if you can bring that energy  
**Translation:** 

**[10540.84s] English:** to the digital world,  
**Translation:** 

**[10541.98s] English:** that's amazing.  
**Translation:** 

**[10543.32s] English:** Yeah.  
**Translation:** 

**[10543.68s] English:** But anyway, so, sorry.  
**Translation:** 

**[10544.86s] English:** So what, on the technology side  
**Translation:** 

**[10546.70s] English:** of bringing that to life,  
**Translation:** 

**[10548.42s] English:** on the programming language side,  
**Translation:** 

**[10550.86s] English:** can you continue,  
**Translation:** 

**[10552.50s] English:** as I rudely interrupt you,  
**Translation:** 

**[10554.18s] English:** talking about Verse?  
**Translation:** 

**[10555.64s] English:** Verse is a functional logic language  
**Translation:** 

**[10557.52s] English:** because we think that that's the way  
**Translation:** 

**[10559.04s] English:** to make the most  
**Translation:** 

**[10560.00s] English:** simple and powerful language simultaneously.  
**Translation:** 

**[10564.74s] English:** Back in the 1970s, the programming language designer  
**Translation:** 

**[10568.88s] English:** who built Pascal, one of the early programming languages,  
**Translation:** Vocabulary: pascal: 帕斯卡

**[10573.78s] English:** Niklaus Wirth, or Nicholas Wirth, as Americans might call him,  
**Translation:** 

**[10578.48s] English:** stated this principle that a programming language  
**Translation:** Vocabulary: nicholas: 尼古拉斯; niklaus: 尼科劳斯; wirth: 魏尔特

**[10580.48s] English:** should achieve a high degree of power,  
**Translation:** 

**[10583.44s] English:** not by having a lot of features,  
**Translation:** 

**[10585.26s] English:** but by having a small number of features that work together  
**Translation:** 

**[10588.36s] English:** and can be composed together arbitrarily,  
**Translation:** Vocabulary: arbitrarily: 任意地

**[10591.44s] English:** so that you have to learn a relatively small set of things,  
**Translation:** 

**[10594.72s] English:** and then the real knowledge comes as you learn ways to combine them  
**Translation:** 

**[10599.84s] English:** to achieve bigger and bigger programs.  
**Translation:** 

**[10601.96s] English:** And so there's a long history to the field of programming languages,  
**Translation:** 

**[10605.46s] English:** but in the 1950s, the first programming language designers  
**Translation:** 

**[10608.84s] English:** got together and built the first standardized language called ALGOL.  
**Translation:** Vocabulary: designers: 程序设计者; standardized: 标准化

**[10611.82s] English:** And there was this meeting in 1956, very few people even know about it,  
**Translation:** 

**[10616.42s] English:** but it's where all the major foundations  
**Translation:** 

**[10618.16s] English:** of programming language were built.  
**Translation:** 

**[10618.36s] English:** And that's where all the major foundations of modern programming languages  
**Translation:** 

**[10619.54s] English:** were decided on, that the C family of languages inherited,  
**Translation:** 

**[10623.40s] English:** and so we're very much living in a world that was defined by them.  
**Translation:** Vocabulary: inherited: 继承自

**[10626.74s] English:** And thankfully, they got a whole lot of things right.  
**Translation:** 

**[10628.92s] English:** They defined how functions should work, how variables should work,  
**Translation:** 

**[10632.28s] English:** and how recursion should work, and thank God they got those things right.  
**Translation:** 

**[10636.16s] English:** But they got a few things wrong, versus trying to fix those,  
**Translation:** Vocabulary: recursion: 递归

**[10640.14s] English:** and that's the functional logic part of it.  
**Translation:** 

**[10642.36s] English:** The interesting thing about functional logic languages  
**Translation:** 

**[10645.10s] English:** is that in an old-school language, an expression,  
**Translation:** 

**[10648.36s] English:** an expression produces a value.  
**Translation:** 

**[10650.36s] English:** In a functional logic language, an expression can produce zero, one,  
**Translation:** 

**[10653.90s] English:** or multiple values.  
**Translation:** 

**[10655.44s] English:** If it produces zero values, we might say it fails,  
**Translation:** 

**[10657.66s] English:** and if it produces one value, we say it succeeds,  
**Translation:** 

**[10659.76s] English:** and if it produces multiple values,  
**Translation:** 

**[10661.02s] English:** then it's kind of providing a set of values you could iterate over.  
**Translation:** 

**[10664.96s] English:** And so there are a bunch of features in today's programming languages  
**Translation:** 

**[10668.00s] English:** that were defined in an ad hoc way without really thinking this through,  
**Translation:** 

**[10671.54s] English:** this zero, one, or many values way,  
**Translation:** 

**[10673.82s] English:** and that's the problem that functional logic languages address.  
**Translation:** 

**[10677.24s] English:** And the most basic example is, you know,  
**Translation:** 

**[10678.16s] English:** the example is an if statement in the programming.  
**Translation:** 

**[10680.00s] English:** language if some condition holds then do this thing otherwise do that thing and in the language  
**Translation:** 

**[10686.38s] English:** today this is done with variables of type boolean or expressions that produce booleans we have  
**Translation:** Vocabulary: boolean: 布尔值

**[10692.82s] English:** boolean value variables that are either true or false we have expressions that evaluate to  
**Translation:** 

**[10698.02s] English:** booleans and so you can express the condition as a bunch of these features together but you've lost  
**Translation:** Vocabulary: booleans: 布尔值; evaluate: 评估

**[10703.70s] English:** any computation you've done in in doing that boolean expression evaluation so in a functional  
**Translation:** 

**[10708.92s] English:** logic language your condition wouldn't do that it would either succeed and produce a value or it  
**Translation:** Vocabulary: computation: 计算

**[10715.20s] English:** would fail if it succeeds it goes to the then branch your operation succeeded now you're  
**Translation:** 

**[10720.10s] English:** operating you know running this one batch of code and if your expression failed then you go to the  
**Translation:** 

**[10724.56s] English:** else branch but the exciting thing about that is your expression that succeeds or fails can produce  
**Translation:** 

**[10730.04s] English:** values uh and bind variables um that are then accessed by the then branch so you can write a  
**Translation:** Vocabulary: accessed: 被访问

**[10735.88s] English:** conditional where you can only get to the inside of the condition  
**Translation:** 

**[10738.90s] English:** um the then if a bunch of variables have successfully been bound to variables so it  
**Translation:** Vocabulary: conditional: 条件

**[10743.46s] English:** lets you test if some conditions hold and then use the results of those tests um and that gives  
**Translation:** 

**[10748.30s] English:** you a much higher level of reliability um and then a for loop um in a traditional language  
**Translation:** Vocabulary: reliability: 可靠性

**[10754.70s] English:** it's just a bunch of imperative code that's woven together to produce a bunch of values iteratively  
**Translation:** 

**[10759.34s] English:** it's uh it's rather awkward to do complicated things in for loops and so you often end up with  
**Translation:** Vocabulary: imperative: 命令式的

**[10764.08s] English:** these ever more complicated constructs built to work around that like iterators and other things  
**Translation:** 

**[10768.90s] English:** the idea of functional logic languages is your for loop can just produce  
**Translation:** Vocabulary: constructs: 构造

**[10772.06s] English:** multiple values and if it produces zero values you go through iterate zero iterations and it  
**Translation:** 

**[10777.48s] English:** produces a bunch of values you go through all those as your iterations rather than having a  
**Translation:** Vocabulary: iterations: 迭代次数

**[10782.24s] English:** bunch of nested loops you can write arbitrary things that look like sql queries in a condition  
**Translation:** 

**[10787.72s] English:** or in a for loop that bind a bunch of variables do a bunch of tests produce a bunch of a series  
**Translation:** Vocabulary: arbitrary: 任意

**[10793.00s] English:** of results and in some order that you're iterating over and then you can handle all of them and  
**Translation:** 

**[10797.88s] English:** produce a bunch of results and then you can write arbitrary things that look like sql queries and  
**Translation:** 

**[10798.90s] English:** in some order that you're iterating over and then you can write arbitrary things that look like  
**Translation:** 

**[10799.90s] English:** sql queries and in some order that you're iterating over and then you can write arbitrary things that  
**Translation:** 

**[10800.00s] English:** I've gained the power of SQL queries, you know, large complex queries over data structures in a language that is much simpler in which your code is just performing simple iterative operations.  
**Translation:** 

**[10812.14s] English:** And so it kind of gives you the best of databases and of regular programming in a much more uniform way.  
**Translation:** Vocabulary: databases: 数据库; iterative: 迭代的

**[10818.00s] English:** And the power of this is now users can write functions that not only produce a value, you can write functions that might fail.  
**Translation:** 

**[10824.52s] English:** And so you can write a function that answers a question.  
**Translation:** 

**[10827.18s] English:** And the answer can be either yes, and my value is this or no.  
**Translation:** 

**[10831.78s] English:** And you can combine these together into arbitrary queries.  
**Translation:** 

**[10835.18s] English:** And if you like, the funny thing is that this is not how C++ works.  
**Translation:** 

**[10839.16s] English:** And so when we have epic programmers moving over from C++ and writing their first verse code, they try to write C++ code and verse style.  
**Translation:** Vocabulary: programmers: 程序员

**[10846.30s] English:** And it actually ends up being kind of convoluted code that's worse than good C++ or good verse.  
**Translation:** 

**[10853.16s] English:** But after a few months, they get up to speed and they're writing really awesome code that's tighter and more complex.  
**Translation:** Vocabulary: convoluted: 复杂难懂

**[10857.30s] English:** And with users who've never programmed before, but are learning programming for the first time in the context of Fortnite, it's really fascinating.  
**Translation:** 

**[10866.90s] English:** You see, these users are learning this kind of as it becomes their intuition.  
**Translation:** Vocabulary: fortnite: 堡垒之夜; intuition: 直觉

**[10871.54s] English:** They just assume programming works this way.  
**Translation:** 

**[10873.38s] English:** And they're writing way more advanced and interesting for loops and conditions than we're often writing internally because they've kind of got the core concepts.  
**Translation:** Vocabulary: internally: 内部使用

**[10881.92s] English:** Yeah, I mean, you said a lot of really interesting stuff.  
**Translation:** 

**[10884.22s] English:** First of all, it's very interesting that there's a bunch of people.  
**Translation:** 

**[10886.62s] English:** A lot of people learning programming for the first time with verse, which is a very different way to look at programming.  
**Translation:** 

**[10896.12s] English:** And in some deep sense, as you're saying, a very intuitive way to learn programming.  
**Translation:** Vocabulary: intuitive: 直观的

**[10901.74s] English:** But there's a lot of properties about this being a logical language.  
**Translation:** 

**[10906.18s] English:** One of which, well, we could maybe speak also about confluence, but also correctness.  
**Translation:** Vocabulary: confluence: 一致性; correctness: 正确性

**[10915.64s] English:** So.  
**Translation:** 

**[10916.62s] English:** Being able to prove the correctness of a code.  
**Translation:** 

**[10920.00s] English:** It's basically easier to write bug-free code.  
**Translation:** 

**[10926.30s] English:** Can you just speak to that and the importance of that  
**Translation:** 

**[10928.94s] English:** when you're building the metaverse?  
**Translation:** 

**[10932.70s] English:** Yeah, right.  
**Translation:** Vocabulary: metaverse: 元宇宙

**[10933.38s] English:** So the challenge with the metaverse is, first of all,  
**Translation:** 

**[10936.44s] English:** that it's a huge base of code that's evolving over time  
**Translation:** Vocabulary: evolving: 不断演变

**[10939.64s] English:** and written by many authors.  
**Translation:** 

**[10940.74s] English:** So you might see every second a new module is updated somewhere,  
**Translation:** Vocabulary: module: 模块

**[10944.40s] English:** and you expect in this live, ever-running simulation  
**Translation:** 

**[10946.66s] English:** that never shuts down, for everything to upgrade live in place.  
**Translation:** Vocabulary: simulation: 模拟

**[10951.32s] English:** And so one critical component of that is the ability to release an update  
**Translation:** 

**[10956.98s] English:** to something you've already published  
**Translation:** 

**[10958.42s] English:** and be sure that it's backwards compatible  
**Translation:** 

**[10960.30s] English:** with the one that you've already released.  
**Translation:** Vocabulary: backwards: 较旧的; compatible: 兼容的

**[10963.10s] English:** And that's essentially a type-checking problem,  
**Translation:** 

**[10965.68s] English:** checking that your new interface is backwards compatible with your old one.  
**Translation:** Vocabulary: interface: 接口

**[10968.68s] English:** And that comes down to the type system of the language.  
**Translation:** 

**[10971.54s] English:** There's been a lot of very interesting research on type systems over the years,  
**Translation:** 

**[10975.32s] English:** most of which hasn't ever made it into the C++ programming language, unfortunately.  
**Translation:** 

**[10981.10s] English:** But you see several branches of that whole field.  
**Translation:** 

**[10984.16s] English:** One of the really interesting things that Java and C Sharp did in the early days  
**Translation:** 

**[10987.96s] English:** and then later abandoned and didn't bother update  
**Translation:** 

**[10990.14s] English:** was defining a very rigorous set of rules for  
**Translation:** 

**[10992.80s] English:** if you publish a module with one set of types today,  
**Translation:** Vocabulary: rigorous: 严格

**[10997.48s] English:** then what changes can you make to that module  
**Translation:** 

**[10999.90s] English:** for your future updates to it that don't break backwards compatibility?  
**Translation:** Vocabulary: compatibility: 兼容性

**[11003.80s] English:** And that's a problem for type-checking.  
**Translation:** 

**[11005.32s] English:** You know, like say you have a function that promises to return some integer.  
**Translation:** Vocabulary: integer: 整数

**[11008.40s] English:** Well, in the future, you could say that returns some natural number  
**Translation:** 

**[11011.46s] English:** because every natural number is an integer.  
**Translation:** 

**[11012.86s] English:** So that's a backwards compatible change.  
**Translation:** 

**[11014.28s] English:** But you can't say it returns a rational number  
**Translation:** 

**[11015.94s] English:** because some rational numbers are not integers.  
**Translation:** 

**[11018.20s] English:** So the system ought to reject that kind of change.  
**Translation:** Vocabulary: integers: 整数

**[11023.38s] English:** But the much, much, much more interesting thing about type-checking  
**Translation:** 

**[11026.40s] English:** was the realization, it was actually made in the 1930s,  
**Translation:** Vocabulary: realization: 认识

**[11030.56s] English:** that if you design a programming language type system in a very particular way,  
**Translation:** 

**[11034.20s] English:** then it becomes a very complex system.  
**Translation:** 

**[11035.30s] English:** It becomes not only useful for expressing types of variables.  
**Translation:** 

**[11040.00s] English:** A traditional thing every type system does is say, like, variable X is of type integer.  
**Translation:** 

**[11045.54s] English:** But if you design a type system in a certain way, then your types can express theorems, like mathematical theorems.  
**Translation:** 

**[11052.20s] English:** You know, the Pythagorean theorem is a cool one.  
**Translation:** Vocabulary: mathematical: 数学的; pythagorean: 毕达哥拉斯; theorem: 定理; theorems: 定理

**[11054.98s] English:** One theorem you might set up in a program is like the theorem that this function takes an array of integers and returns an array of the same integers, but the result is sorted.  
**Translation:** 

**[11065.66s] English:** If you express that as a theorem and you follow this system of type theory, then you can actually require that anybody who writes that sorting function to prove that it has actually sorted its result.  
**Translation:** 

**[11078.28s] English:** And so you have types or theorems, and values constructed a certain way can be proofs of those theorems.  
**Translation:** 

**[11085.40s] English:** And nowadays in mathematical literature, you see more and more theorems are being proven mechanically.  
**Translation:** 

**[11091.38s] English:** Mathematicians are proving theorems in a way that is verified by computer to be a correct proof.  
**Translation:** 

**[11096.26s] English:** In the old days of math, people would write down, like, language.  
**Translation:** Vocabulary: mathematicians: 数学家; verified: 验证正确

**[11099.40s] English:** If you look at all of Euclid's theorems, it was just language.  
**Translation:** 

**[11102.32s] English:** It was just writing in ancient Greek to say the steps of the proof to convince the reader that the thing is true.  
**Translation:** 

**[11108.20s] English:** Starting in the 1930s, mathematicians moved towards rigorous formal proofs in which there's a series of steps that can be mechanically verified.  
**Translation:** 

**[11117.46s] English:** They're proving things.  
**Translation:** Vocabulary: mechanically: 机械地; rigorous: 严谨的

**[11118.16s] English:** And when mathematicians say they've done a computer proof of a theorem, what they really mean is they've written the program in a proof language.  
**Translation:** 

**[11125.66s] English:** Like, Lean is a theorem prover, COQ is a theorem prover, and there are several others.  
**Translation:** 

**[11130.66s] English:** It means they've written a mechanical proof in that language that a computer has checked so that it's impossible to lie.  
**Translation:** 

**[11138.22s] English:** If you say that you've proven a thing and the computer verifies it, then it's definitely true.  
**Translation:** Vocabulary: verifies: 验证正确

**[11144.66s] English:** And, you know, this is a feature of mathematical proof languages, but it's also an idea that's making its way into programming languages gradually over time.  
**Translation:** 

**[11153.00s] English:** And our aim for Verse is to be the first mainstream.  
**Translation:** Vocabulary: mainstream: 主流

**[11155.66s] English:** programming language that fully adopts that approach and that technique.  
**Translation:** 

**[11160.00s] English:** And not only adopts it, but adopts it in a way that's really user-friendly, so you don't have to do that.  
**Translation:** 

**[11165.44s] English:** And the idea of this is that you want gradually more information to be incorporated in the types of variables.  
**Translation:** 

**[11172.38s] English:** The property you want of a programming language is that if your compiler accepts your program and doesn't beep and tell you there is an error, then your program should work.  
**Translation:** 

**[11181.26s] English:** Now, there are all kinds of ways humans can make mistakes there, so we'll never achieve that ideal.  
**Translation:** 

**[11186.60s] English:** But we can get closer and closer to it by having more and more language features that enable the compiler to catch more human coding errors and tell the user what went wrong.  
**Translation:** 

**[11197.16s] English:** And that becomes extremely important in the metaverse.  
**Translation:** 

**[11200.26s] English:** The cost of fixing a bug that's made it through to runtime and is in users' hands, the cost of fixing a bug in a shipping program is hundreds of times higher than fixing a bug that you've just observed as you're running your code yourself.  
**Translation:** Vocabulary: metaverse: 元宇宙; runtime: 运行时

**[11214.94s] English:** When it's running on your computer,  
**Translation:** 

**[11216.60s] English:** you just fix a line of code and your bug's fixed.  
**Translation:** 

**[11219.54s] English:** When you have to fix it live, you have to release a patch, you have to release patch notes, you have to test the patch, you have to check for all the other bugs that might have been introduced, and everything becomes vastly, vastly more expensive.  
**Translation:** 

**[11229.38s] English:** So, you know, the real aim of the verse program and approach is to catch all of these errors at compile time and make the metaverse a very reliable place.  
**Translation:** 

**[11238.06s] English:** Do you see a world where, like, at compile time, you could prove that the program is correct in some sense of correctness?  
**Translation:** 

**[11245.34s] English:** Proving things becomes...  
**Translation:** 

**[11246.60s] English:** Commentatorially harder as they get larger, right?  
**Translation:** 

**[11248.92s] English:** Right.  
**Translation:** 

**[11249.04s] English:** And so the really important thing about this whole field is that you should be able to adopt these capabilities gradually and apply it where you really need it.  
**Translation:** 

**[11257.64s] English:** Like, if you're writing something like a cryptography algorithm, that's a good place to prove stuff.  
**Translation:** Vocabulary: algorithm: 算法; cryptography: 密码学

**[11263.34s] English:** If you're writing a data decompressor that's going to be used by an entire ecosystem, like, proving that that doesn't overrun memory is actually really important.  
**Translation:** 

**[11271.98s] English:** And a lot of the reason that security vulnerabilities happen today is because...  
**Translation:** Vocabulary: decompressor: 数据解压程序; vulnerabilities: 安全漏洞

**[11276.60s] English:** In a different language, a compiler could have caught, were not caught, and...  
**Translation:** 

**[11280.00s] English:** C because it just doesn't have this feature.  
**Translation:** 

**[11284.38s] English:** We shouldn't see this as scary. Everybody working in a typed language like C  
**Translation:** 

**[11288.00s] English:** or C Sharp or Java is proving theorems all the time.  
**Translation:** Vocabulary: theorems: 定理

**[11292.58s] English:** If you have a variable of type integer and you assign some value to it,  
**Translation:** 

**[11295.94s] English:** you've proven to the compiler that that value was an integer because otherwise it would have rejected  
**Translation:** Vocabulary: integer: 整数

**[11300.10s] English:** it. And so as we add more and more advanced proofs,  
**Translation:** 

**[11303.84s] English:** we'll get compositional properties falling out of our systems that  
**Translation:** Vocabulary: compositional: 组合性质

**[11307.86s] English:** are easy to use and people prefer to use.  
**Translation:** 

**[11312.02s] English:** And we might think in the future where we have AI helping us write certain kinds of  
**Translation:** 

**[11315.92s] English:** code, the big problem with AI is you ask it to do something and  
**Translation:** 

**[11319.20s] English:** ask you to write a fragment of code that does something, it might give you a perfectly valid  
**Translation:** 

**[11323.70s] English:** fragment of code that compiles but does the wrong thing.  
**Translation:** 

**[11327.30s] English:** And if we had languages where you could say, write a function that sorts  
**Translation:** Vocabulary: compiles: 编译通过

**[11331.76s] English:** this array and prove that it did that, it could actually  
**Translation:** 

**[11335.88s] English:** rewrite the proof.  
**Translation:** 

**[11337.86s] English:** If the compiler didn't beep with it, you could trust that it was actually sorting the array  
**Translation:** 

**[11342.04s] English:** and otherwise you could go back to the AI and say, well, that didn't work.  
**Translation:** 

**[11345.72s] English:** But getting to the point where we know that our programs do what we say they're going to do  
**Translation:** 

**[11349.84s] English:** or think they're going to do is a very important thing.  
**Translation:** 

**[11352.66s] English:** And by the way, I should mention that you sent me a note about Curry-Howard correspondence, which I went down  
**Translation:** 

**[11357.96s] English:** a rabbit hole in it. That's a whole fascinating field, which shows  
**Translation:** Vocabulary: correspondence: 对应关系

**[11361.74s] English:** the mathematical relationship between programs and proofs.  
**Translation:** 

**[11364.94s] English:** That's right. This is a result from the 1930s. It's one of the most  
**Translation:** 

**[11367.78s] English:** important results of computer science that almost nobody knows  
**Translation:** 

**[11371.82s] English:** about. But they did this rigorous breakdown of type systems  
**Translation:** Vocabulary: rigorous: 严谨的

**[11375.76s] English:** and the 1930s formulation of programming and  
**Translation:** 

**[11379.82s] English:** established that everything you can prove  
**Translation:** 

**[11384.06s] English:** in mathematical logic, you can prove within a type system  
**Translation:** 

**[11387.64s] English:** if it has certain features. And, you know, if you  
**Translation:** Vocabulary: mathematical: 数学的

**[11391.86s] English:** break down what is a proof, well, a proof that integers exist is some  
**Translation:** 

**[11395.78s] English:** integer. Like, 5 is a proof that integers.  
**Translation:** 

**[11397.78s] English:** So when you have, you know,  
**Translation:** 

**[11400.00s] English:** something like var x int, and you say x equals 5,  
**Translation:** 

**[11402.42s] English:** well, you're proving to the compiler that 5 is an integer.  
**Translation:** 

**[11405.10s] English:** You know, that comes as a second-hand nature,  
**Translation:** 

**[11406.62s] English:** but you can prove more advanced things.  
**Translation:** 

**[11409.02s] English:** You know, if you want to prove that a pair of things are true,  
**Translation:** 

**[11412.28s] English:** like theorem A is true and theorem B is true,  
**Translation:** 

**[11414.64s] English:** then you need to provide a pair of values,  
**Translation:** Vocabulary: theorem: 定理

**[11416.76s] English:** one that proves theorem A and one that proves theorem B,  
**Translation:** 

**[11419.50s] English:** and that's the conjunctive law of proofs,  
**Translation:** Vocabulary: conjunctive: 联合的

**[11421.18s] English:** and there's a disjunctive law, too,  
**Translation:** 

**[11422.76s] English:** and then there's an implication law for proofs,  
**Translation:** Vocabulary: disjunctive: 相斥的; implication: 推导

**[11426.54s] English:** and it turns out that that's really satisfied by functions.  
**Translation:** 

**[11431.68s] English:** When you write a function in a programming language,  
**Translation:** 

**[11433.24s] English:** you're saying, if you give me this thing, I will give you that thing.  
**Translation:** 

**[11436.20s] English:** If you give me a parameter of type something,  
**Translation:** 

**[11438.20s] English:** then I'll give you a result of some other type,  
**Translation:** 

**[11440.44s] English:** and if you write that, by writing that function,  
**Translation:** 

**[11442.88s] English:** you're proving that given one of these things,  
**Translation:** 

**[11444.46s] English:** you can produce another thing, and that's a proof of an implication.  
**Translation:** 

**[11447.46s] English:** With only, like, seven laws,  
**Translation:** 

**[11449.30s] English:** you can construct all of mathematical logic in a type system,  
**Translation:** 

**[11454.30s] English:** and, you know, one of the important things  
**Translation:** 

**[11456.22s] English:** for programmers,  
**Translation:** Vocabulary: programmers: 程序员

**[11456.54s] English:** for programming languages that hasn't been given enough attention  
**Translation:** 

**[11458.80s] English:** is some aspects of programming languages are just subjective.  
**Translation:** 

**[11463.02s] English:** They're just machinations of the programming language designer, you know.  
**Translation:** 

**[11466.86s] English:** Guido van Rossum decided that Python  
**Translation:** Vocabulary: guido: 古德·范·罗苏姆; machinations: 权谋术数

**[11468.90s] English:** should support indentation a certain way,  
**Translation:** 

**[11471.60s] English:** and, you know, as long as you're dealing with things  
**Translation:** Vocabulary: indentation: 缩进

**[11473.42s] English:** like human notation and naming of things,  
**Translation:** 

**[11475.22s] English:** there's always going to be that subjective layer,  
**Translation:** 

**[11477.80s] English:** but there are other parts of programming languages  
**Translation:** 

**[11479.94s] English:** that are not subjective but should be fundamental,  
**Translation:** 

**[11484.30s] English:** and when you look at type systems,  
**Translation:** 

**[11486.54s] English:** there is a way to do type systems  
**Translation:** 

**[11488.30s] English:** that gives you mathematical proofs,  
**Translation:** 

**[11490.16s] English:** and every other way of type systems  
**Translation:** 

**[11492.40s] English:** that doesn't give you mathematical proofs is just worse  
**Translation:** 

**[11494.72s] English:** and should ultimately be rejected.  
**Translation:** 

**[11497.98s] English:** And so I think one of the jobs of computing  
**Translation:** 

**[11499.76s] English:** is to identify, like,  
**Translation:** 

**[11501.84s] English:** what have we actually done right in the past  
**Translation:** 

**[11503.62s] English:** and what have we done wrong,  
**Translation:** 

**[11504.74s] English:** and for everything we've done wrong,  
**Translation:** 

**[11506.20s] English:** actually going back and fixing it.  
**Translation:** 

**[11508.52s] English:** Otherwise, we just keep accumulating so much cruft  
**Translation:** 

**[11510.84s] English:** that our systems eventually are crushed  
**Translation:** Vocabulary: accumulating: 累积

**[11513.20s] English:** under their own complexity.  
**Translation:** 

**[11515.04s] English:** And, you know, there have been massive,  
**Translation:** 

**[11516.54s] English:** massive announcements of horrible vulnerabilities  
**Translation:** 

**[11518.70s] English:** in software and services.  
**Translation:** Vocabulary: vulnerabilities: 软件缺陷

**[11520.00s] English:** over the past year um you know it turns out like some nation-state backdoored a bunch of teleco's  
**Translation:** 

**[11526.12s] English:** surveillance systems for wiretaps like huge problem there but you know ultimately when you  
**Translation:** Vocabulary: backdoored: 植入后门; wiretaps: 窃听器

**[11532.52s] English:** break it down it's probably because of some buffer overrun and some c program like these uh these  
**Translation:** 

**[11537.18s] English:** decisions about programming languages have long-term implications it's really fascinating  
**Translation:** Vocabulary: buffer: 缓冲区

**[11542.16s] English:** that in building these systems that hundreds of millions of people use you're rethinking about  
**Translation:** 

**[11547.10s] English:** like how do you actually build it from first principles so i should mention that uh versus  
**Translation:** 

**[11551.74s] English:** primary design goals it should be simple enough to learn as a first-time programmer general enough  
**Translation:** 

**[11556.02s] English:** for writing any kind of code and data productive in the context of building iterating and shipping  
**Translation:** Vocabulary: programmer: 编程人员

**[11561.48s] English:** a project in the team setting statically verified to catch as many categories of runtime problems as  
**Translation:** 

**[11567.54s] English:** possible compile time as we were talking about performant for real-time open world multiplayer  
**Translation:** Vocabulary: runtime: 运行时; statically: 静态地; verified: 验证

**[11573.56s] English:** games we didn't really quite talk about performance maybe i could  
**Translation:** 

**[11577.08s] English:** ask you about that in a second complete so that every feature of the language supports  
**Translation:** 

**[11580.92s] English:** programmer abstraction over that feature timeless built for the needs of today and for foreseeable  
**Translation:** 

**[11586.86s] English:** future needs yeah and and then there's some design goals that we talked about that is strongly  
**Translation:** Vocabulary: abstraction: 抽象; foreseeable: 可预见的; timeless: 永恒的

**[11591.76s] English:** typed multi-paradigm to use the best of functional programming object-oriented programming imperative  
**Translation:** 

**[11597.48s] English:** programming so it's as deterministic as possible you know if you run it over and over it runs in  
**Translation:** Vocabulary: deterministic: 可预测的; imperative: 命令式的

**[11603.66s] English:** exact same way you know failable expressions as you  
**Translation:** 

**[11607.08s] English:** talked about it's super fascinating there's so many cool features in this uh speculative execution  
**Translation:** Vocabulary: failable: 可失败的; speculative: 推测性的

**[11611.94s] English:** concurrency maybe can you talk about concurrency like what is it about verse that allows for  
**Translation:** 

**[11618.78s] English:** concurrency at the scale that you need this is the one biggest technical problem that uh we're working  
**Translation:** Vocabulary: concurrency: 并行性

**[11627.48s] English:** to solve in this generation and that is taming concurrency so that any ordinary programmer can  
**Translation:** 

**[11635.34s] English:** achieve it by just writing  
**Translation:** 

**[11636.92s] English:** Ordinary code.  
**Translation:** 

**[11637.94s] English:** It's hard.  
**Translation:** 

**[11638.70s] English:** You know?  
**Translation:** 

**[11639.20s] English:** Yeah.  
**Translation:** 

**[11639.68s] English:** Programming.  
**Translation:** 

**[11640.00s] English:** on a single-threaded computer is hard enough, but it is completely predictable. If you have a  
**Translation:** Vocabulary: predictable: 可预测的

**[11644.32s] English:** language that's deterministic and you run the same code over and over, it's always going to do exactly  
**Translation:** 

**[11649.86s] English:** the same thing, and there's no unpredictability about what might happen, right? You're reading  
**Translation:** 

**[11654.10s] English:** and writing variables in some order, and you're always going to see it behave the same. The problem  
**Translation:** 

**[11659.52s] English:** is when you introduce multiple threads or multiple nodes in a data center all working together on a  
**Translation:** 

**[11664.26s] English:** single problem is that they each want to read and write different pieces of data and change the  
**Translation:** 

**[11669.26s] English:** state of the world as they go, and still almost all concurrency in real-world programs today is  
**Translation:** 

**[11676.48s] English:** achieved manually. Programmers are writing this code that might run in multiple threads very, very  
**Translation:** 

**[11682.42s] English:** carefully so that they are negotiating among each thread to get access to data in a way that's going  
**Translation:** Vocabulary: programmers: 程序员

**[11689.82s] English:** to give them predictable results, and it's incredibly hard. It's so hard that we've, in five  
**Translation:** 

**[11698.18s] English:** generations of Unreal Engine,  
**Translation:** 

**[11699.26s] English:** every single generation decided we're not going to try to scale up all of our gameplay code to  
**Translation:** 

**[11704.68s] English:** multiple threads manually. It's just much, much, much too likely to go wrong, not only for  
**Translation:** 

**[11710.12s] English:** ourselves, but for every partner company who licenses Unreal Engine and tries to use it for  
**Translation:** 

**[11714.24s] English:** building a game. It's just a massive foot gun. There's a variety of solutions to concurrency  
**Translation:** 

**[11720.02s] English:** that are all rather suboptimal. One attempted solution was like, just don't try to solve this  
**Translation:** 

**[11726.16s] English:** problem at all. Let's break our program down into microservices.  
**Translation:** Vocabulary: microservices: 微服务; suboptimal: 次优的

**[11729.26s] English:** Almost all online websites of massive scale, like amazons.com, work with hundreds of microservices  
**Translation:** 

**[11735.54s] English:** where different servers negotiate with each other by sending messages to each other. By programmers  
**Translation:** Vocabulary: amazons: 亚马逊

**[11740.10s] English:** writing those things very carefully, they eventually get to being able to take your orders  
**Translation:** 

**[11743.90s] English:** and not make a mess of them reliably. But this is totally not scalable to the metaverse, where you  
**Translation:** Vocabulary: metaverse: 元宇宙; reliably: 可靠地; scalable: 可扩展的

**[11751.00s] English:** have millions of programmers who are mostly not going to be computer scientists. They're mostly  
**Translation:** 

**[11754.90s] English:** going to be hobbyists and enthusiasts and first-time programmers doing stuff for fun.  
**Translation:** 

**[11759.26s] English:** That's not going to happen.  
**Translation:** 

**[11760.00s] English:** never going to work for them because they'll never be able to envision all the different dependencies  
**Translation:** Vocabulary: envision: 想象

**[11763.52s] English:** between different computations they're running in parallel.  
**Translation:** 

**[11767.10s] English:** It turns out that there was some amazing foundational work done in the 1980s  
**Translation:** Vocabulary: computations: 计算; foundational: 基础的

**[11772.04s] English:** that was made very real by a paper on Haskell concurrency  
**Translation:** 

**[11775.22s] English:** composable memory transactions is the name of the paper. It describes the system  
**Translation:** Vocabulary: composable: 可组合的; concurrency: 并发; haskell: 哈斯克尔

**[11780.20s] English:** for transactional updates to programs.  
**Translation:** 

**[11784.50s] English:** The idea of a transaction is  
**Translation:** 

**[11786.26s] English:** a transaction is a block of code that does a bunch of  
**Translation:** 

**[11792.20s] English:** operations on memory. It might read, it might write, it might process an order, it might accept an order  
**Translation:** 

**[11796.38s] English:** or reject an order. It might transfer money between one bank  
**Translation:** 

**[11800.36s] English:** account and another. It might make conditional decisions like, oh, you asked to transfer  
**Translation:** Vocabulary: conditional: 条件性的

**[11804.30s] English:** $100 from your account to this guy's account. We're going to see if you have  
**Translation:** 

**[11808.38s] English:** $100. If you don't, we're going to reject it. If you have $100,  
**Translation:** 

**[11812.02s] English:** we're going to take $100 out of your account and add it to this other guy's account  
**Translation:** 

**[11815.46s] English:** without transactions. If everybody's just randomly adding and subtracting each  
**Translation:** Vocabulary: subtracting: 减去

**[11819.88s] English:** other's bank balances, then you might have somebody read a bank balance, subtract $100, and write  
**Translation:** 

**[11823.92s] English:** it out. But in the meantime, somebody has written something else in the meantime. And so you might get  
**Translation:** Vocabulary: balances: 账户余额; meantime: 其间; subtract: 减去

**[11827.94s] English:** inconsistent bank balances arising if you don't have a way  
**Translation:** 

**[11831.96s] English:** of ensuring that these all run in a specific order.  
**Translation:** 

**[11836.16s] English:** So the idea of transactions is its way of dividing an entire program  
**Translation:** 

**[11839.74s] English:** into self-contained updates that  
**Translation:** 

**[11843.76s] English:** do an arbitrary amount of computation, but must run in a single-threaded  
**Translation:** 

**[11847.90s] English:** manner. And in the case of a game engine, that's a gameplay object update.  
**Translation:** Vocabulary: arbitrary: 任意; computation: 计算

**[11851.72s] English:** When you're playing Fortnite, you see a gameplay object. Every other player is a gameplay object.  
**Translation:** 

**[11856.16s] English:** Every enemy is a gameplay object. Every rocket and projectile and car  
**Translation:** Vocabulary: fortnite: 堡垒之夜; projectile: 投射物

**[11859.64s] English:** and thing you see moving around and interacting, it's not just a fixed, static part of the world.  
**Translation:** 

**[11864.02s] English:** That's a separate game object. And each of those objects is updated  
**Translation:** 

**[11867.68s] English:** at a rate of one update per frame, at 60 frames per second.  
**Translation:** 

**[11872.14s] English:** And so then, in the course of the game, you're going to have a game that's going to be  
**Translation:** 

**[11873.74s] English:** a Fortnite Battle Royale gameplay. You have tens of thousands of object updates  
**Translation:** 

**[11877.22s] English:** happening every frame, with 100 players.  
**Translation:** 

**[11880.00s] English:** a simulation with billions of players you'd have a whole lot more than that so right now that's  
**Translation:** 

**[11884.72s] English:** done single threaded yeah that's done single threadedly in each game session this is why  
**Translation:** Vocabulary: simulation: 模拟; threaded: 线程; threadedly: 地使用线程

**[11888.24s] English:** fortnite is 100 players limitation if you absolutely maxed out a server maybe today  
**Translation:** 

**[11893.20s] English:** you could get it up to 140 or something but you know it's not going to thousands or millions or  
**Translation:** 

**[11897.68s] English:** billions and so what we need is a technique for magically automatically scaling our code  
**Translation:** 

**[11903.02s] English:** to that and transactions are the idea and the idea is a transaction is a granule of code that  
**Translation:** Vocabulary: granule: 细粒度

**[11909.06s] English:** runs its entirety and so the idea of this transactional memory concept is that we're  
**Translation:** 

**[11914.70s] English:** going to have programmers write completely ordinary code reads and writes variables in  
**Translation:** Vocabulary: entirety: 全程; programmers: 程序员

**[11918.70s] English:** the completely ordinary way and they're not going to have to worry about concurrency at all  
**Translation:** 

**[11921.96s] English:** and then the system like today a program a computer just runs your program there's no  
**Translation:** Vocabulary: concurrency: 并发

**[11926.92s] English:** amount of speculation going on at the programming language level the idea of transactions is since  
**Translation:** 

**[11932.02s] English:** we have a bunch of operations we need to know we apply we apply a large set of them concurrently  
**Translation:** Vocabulary: concurrently: 同时进行; speculation: 猜测

**[11939.06s] English:** but instead of each one reading and writing from global memory shared by all in which case they  
**Translation:** 

**[11943.42s] English:** might be reading and writing and uh and contending with each other for the same data and might be  
**Translation:** Vocabulary: contending: 争用

**[11949.36s] English:** doing contradictory things to it we're going to track all of our rights locally we're not going  
**Translation:** 

**[11954.74s] English:** to write data change we're not going to write changes out to global memory we're going to keep  
**Translation:** Vocabulary: contradictory: 矛盾的

**[11958.50s] English:** track of it in a buffer that's just for that one transaction so we're going to be it's going to  
**Translation:** 

**[11963.30s] English:** look to that code exactly as if it's running on the global system affecting global game state  
**Translation:** Vocabulary: buffer: 缓冲区

**[11969.06s] English:** it's going to be set aside and buffered up for consideration later we're going to run  
**Translation:** 

**[11975.98s] English:** hundred tens or hundreds or thousands of the updates concurrently we're going to see which  
**Translation:** Vocabulary: buffered: 缓冲

**[11979.92s] English:** ones had read write conflicts because if two transactions don't read and write any of the  
**Translation:** 

**[11984.60s] English:** same data then you could have run them in either order or simultaneously and it wouldn't have  
**Translation:** 

**[11990.18s] English:** changed the end result yeah the order doesn't matter i mean this is so fascinating to imagine  
**Translation:** 

**[11994.98s] English:** this kind of system and arbitrarily  
**Translation:** Vocabulary: arbitrarily: 随意地

**[11999.06s] English:** current running  
**Translation:** 

**[12000.00s] English:** millions of updates in parallel of gameplay objects that's that's the thing that enables  
**Translation:** 

**[12008.18s] English:** the thing that we're talking about which is you know tens of millions of people together in one  
**Translation:** 

**[12012.06s] English:** scene yeah exactly and the key is that you're running these updates speculatively and you're  
**Translation:** Vocabulary: speculatively: 推测性地

**[12016.14s] English:** not committing their changes to memory until you're sure that they're free of conflict so  
**Translation:** 

**[12020.96s] English:** you might update 10 000 objects you might find 9 000 of them were conflict free so you apply those  
**Translation:** 

**[12026.92s] English:** 9 000 objects updates to memory and they could have run in any order and it wouldn't have changed  
**Translation:** 

**[12033.36s] English:** the result now there's a thousand objects left over now you have to run those again try them  
**Translation:** 

**[12037.52s] English:** may interleave in a different way to to get them to eventually commit to memory and in the meantime  
**Translation:** 

**[12043.78s] English:** you just throw all their computations away and redo them later and by doing this like removing  
**Translation:** Vocabulary: computations: 计算; interleave: 交替进行; meantime: 其间

**[12049.34s] English:** this from being a programming problem for the programmer to deal with to being a language  
**Translation:** 

**[12053.24s] English:** problem for us language designers to deal with and  
**Translation:** Vocabulary: designers: 设计者; programmer: 程序员

**[12056.70s] English:** we're moving a vast amount of pain that would be imposed on a million people instead to  
**Translation:** 

**[12061.82s] English:** a vast amount of pain and imposed on a small number of people have to actually make this work  
**Translation:** 

**[12066.02s] English:** that's amazing that's really incredible um so what's the state of things with verse and  
**Translation:** 

**[12071.44s] English:** i guess what you're outlining is if and hopefully it is successful this would be a big part of  
**Translation:** Vocabulary: outlining: 提纲

**[12078.00s] English:** unreal engine 6 so what's the timeline where do we stand today well there's a lot going on in  
**Translation:** 

**[12084.40s] English:** parallel the key thing with verse is that we  
**Translation:** 

**[12086.70s] English:** have been specifying the like what we think is the ultimate version of the language with all the  
**Translation:** 

**[12091.96s] English:** features we want whereas we've been shipping uh more more modest versions of language over time  
**Translation:** Vocabulary: specifying: 指定

**[12098.78s] English:** and we've released dozens of updates to it over the past year and a half um and the idea is that  
**Translation:** 

**[12105.28s] English:** the shipping version that we it gains more and more features over time but each maintaining  
**Translation:** 

**[12109.58s] English:** backwards compatibility with old versions and each continuing to improve and approach the  
**Translation:** 

**[12113.76s] English:** ultimate version of it as we go and we've been doing this  
**Translation:** Vocabulary: backwards: 向后; compatibility: 兼容性

**[12116.70s] English:** experiment entirely within the world of unreal editor for  
**Translation:** 

**[12120.00s] English:** for now. We want to test this and iterate with Fortnite creators in just the metaverse usage  
**Translation:** Vocabulary: fortnite: 堡垒之夜; metaverse: 元宇宙

**[12125.82s] English:** case before we make it available to all of our partners using Unreal Engine for all of their  
**Translation:** 

**[12130.16s] English:** projects. And the idea is to iteratively improve it and build it out. Because right now, UEFN has  
**Translation:** 

**[12135.92s] English:** relatively few features for programming. It needs a lot more. And everything we add makes the world  
**Translation:** 

**[12141.10s] English:** a much better place for Fortnite creators. And we're adding major, major new APIs every few  
**Translation:** 

**[12146.06s] English:** months throughout the course of this year. Whereas Unreal Engine licensees who are building  
**Translation:** 

**[12151.00s] English:** standalone games already have access to the full engine through C++. They have massive,  
**Translation:** Vocabulary: standalone: 独立运行的

**[12155.64s] English:** massive expectations of an API. And so we can't release this to them until we've built up all the  
**Translation:** 

**[12161.34s] English:** essential features that they'll need for building their gameplay in the future. And so, you know,  
**Translation:** 

**[12166.60s] English:** we have these two different tendrils of progress. There's Unreal Engine 5 for game developers,  
**Translation:** 

**[12170.74s] English:** and there's Unreal Engine 5 targeting the Fortnite community. And there's,  
**Translation:** Vocabulary: tendrils: 分支

**[12176.06s] English:** different bits of development that are only in one area of it that aren't applied to both. Like,  
**Translation:** 

**[12180.12s] English:** not all of the Unreal Engine 5 features are actually available in Fortnite, because some  
**Translation:** 

**[12183.42s] English:** of them we haven't figured out, or haven't gotten to the point where we can deploy them to all seven  
**Translation:** 

**[12187.76s] English:** platforms in a platform-independent way. And so the place where all of these different threads  
**Translation:** Vocabulary: deploy: 部署

**[12193.28s] English:** of development come together is Unreal Engine 6. And it's a few years away. We don't have an exact  
**Translation:** 

**[12197.82s] English:** time frame. But, you know, we could be seeing preview versions of it perhaps two to three years  
**Translation:** 

**[12204.46s] English:** from now. And we're making connections.  
**Translation:** 

**[12206.06s] English:** And we're making continuous progress towards it.  
**Translation:** 

**[12207.90s] English:** So that's really nice. So there's this ultimate version of a language that you're constantly  
**Translation:** 

**[12211.18s] English:** working on and thinking through. Then there's the shipped version of the language that's used by a  
**Translation:** 

**[12219.22s] English:** large number of people, but still in the constrained environment of the Unreal Editor for Fortnite,  
**Translation:** 

**[12225.36s] English:** so for the Fortnite game. And then there awaits the more general Unreal Editor, Unreal Engine,  
**Translation:** Vocabulary: constrained: 限制较多

**[12234.16s] English:** for the game.  
**Translation:** 

**[12236.06s] English:** The lessons learned in the Fortnite context to be integrated in the more general  
**Translation:** 

**[12240.00s] English:** context of creating simulated worlds for all kinds of games including fortnite it's a really  
**Translation:** 

**[12246.08s] English:** nice setup because you're you're both it's a testing ground of the language in fortnite  
**Translation:** Vocabulary: fortnite: 堡垒之夜; setup: 配置; simulated: 模拟

**[12250.26s] English:** and you're keeping an eye on what the ultimate thing will look like also necessary to to deliver  
**Translation:** 

**[12256.96s] English:** all the features that we mentioned brilliant you know the aim for ue6 is to bring the best of both  
**Translation:** 

**[12262.06s] English:** worlds together a much easier gameplay programming for the fortnite community and for licensees  
**Translation:** 

**[12267.02s] English:** more scalability to large-scale simulations of all sorts greater ease of use meaning it will be  
**Translation:** Vocabulary: scalability: 可扩展性

**[12274.18s] English:** easier to hire programmers who are familiar with and experienced with the thing but also ensure  
**Translation:** 

**[12280.04s] English:** that every game developer has the full deployment capabilities so they can build a game once and  
**Translation:** Vocabulary: deployment: 部署能力; programmers: 程序员

**[12285.82s] English:** then ship it anywhere like the ultimate version of this enables a game developer to build a game of  
**Translation:** 

**[12291.06s] English:** any sort um either or simultaneously both ship it into fortnite as a fortnite island that players  
**Translation:** 

**[12297.00s] English:** can go into bring their fortnite items and cosmetics and interoperate properly or ship as  
**Translation:** 

**[12302.88s] English:** a standalone game or both um if they ship as a standalone game they shouldn't be missing out on  
**Translation:** Vocabulary: cosmetics: 化妆品; interoperate: 互联互通; standalone: 独立版本

**[12307.98s] English:** the you know open economy either because in this time frame we'll have opened up the fortnite item  
**Translation:** 

**[12313.28s] English:** economy to third-party developers of all sort um hopefully they're a standards body but there  
**Translation:** 

**[12318.60s] English:** might be multiple phases of it so that um if you choose to ship a standalone game you can still  
**Translation:** 

**[12324.16s] English:** choose to uh you know have fortnite items working  
**Translation:** 

**[12327.00s] English:** your game and have your game items work in fortnite and have your item economy integrated  
**Translation:** 

**[12330.94s] English:** with the overall metaverse economy and make and solve the really core problem that of the game  
**Translation:** Vocabulary: metaverse: 元宇宙

**[12337.02s] English:** industry that matthew ball has been documenting over the past few years yeah by the way matthew  
**Translation:** 

**[12341.02s] English:** ball has been really helpful it's a great he wrote a really great book that i recommend people  
**Translation:** Vocabulary: documenting: 记录

**[12344.86s] English:** check out there's an updated version let me just ask for because again there's a bunch of indie  
**Translation:** 

**[12350.20s] English:** developers listening to this i saw that a lot of solo developers out there they're using unreal  
**Translation:** Vocabulary: indie: 独立开发者

**[12356.24s] English:** engine that  
**Translation:** 

**[12357.00s] English:** are basically creating video games solo i saw  
**Translation:** 

**[12360.00s] English:** uh can highly recommend it's great choo-choo charles it's a great video game uh gavin eisenbeiss  
**Translation:** 

**[12369.54s] English:** he uh great guy he solo created this game that's i think quite popular i believe he says he used  
**Translation:** Vocabulary: eisenbeiss: 艾森贝格; gavin: 加文

**[12377.58s] English:** visuals he didn't even use c++ he used visual scripting he used blueprints yeah to create it  
**Translation:** 

**[12382.52s] English:** okay so i mean all that to say people should go check it out support indie developers support  
**Translation:** Vocabulary: blueprints: 蓝图

**[12387.48s] English:** gavin support everybody like that i think it's important to say because there's so much genius  
**Translation:** 

**[12392.12s] English:** and artistry out there that we want to support the crazy dreamers out there anyway all that to say  
**Translation:** Vocabulary: artistry: 艺术才能

**[12399.64s] English:** what are the ways you think epic can support indie developers like that people like gavin  
**Translation:** 

**[12406.14s] English:** like give them superpowers to create games from which they can make at the very least enough money  
**Translation:** Vocabulary: superpowers: 超能力

**[12413.00s] English:** that they can keep doing their art yeah well that's really  
**Translation:** 

**[12417.42s] English:** a good question i think it's a good question i think it's a good question i think it's a good  
**Translation:** 

**[12417.46s] English:** about productivity uh because to be successful with a game you have to have a great game um  
**Translation:** 

**[12423.74s] English:** if you're targeting a if you're building a type of game that nobody's ever built before you might  
**Translation:** 

**[12428.50s] English:** be able to build a smaller simpler game than if you're competing in a massive genre that has huge  
**Translation:** 

**[12432.36s] English:** expectations but it's all about enabling somebody to do that in a reasonable amount of time that  
**Translation:** 

**[12437.26s] English:** they can spend and to be able to finish it and chip it and maintain it successfully the tools  
**Translation:** 

**[12441.60s] English:** are a big part of that having the tools be as productive as possible um there are a lot of  
**Translation:** 

**[12446.10s] English:** other facets as well like everything is a game and it's a game and it's a game and it's a game  
**Translation:** 

**[12447.40s] English:** having a content marketplace is a big thing um you know just off the shelf piles of content some  
**Translation:** Vocabulary: facets: 方面; marketplace: 市场

**[12453.64s] English:** free some paid built by other creators uh can enable a small indie team to to build a big game  
**Translation:** 

**[12460.18s] English:** uh and just be able to focus on the unique content of the game being able to write their gameplay  
**Translation:** 

**[12464.90s] English:** and lay out their environments the way they want but not have to build every tree and rock  
**Translation:** 

**[12469.06s] English:** um yeah because somebody's already built one and theirs is probably  
**Translation:** 

**[12472.60s] English:** like you know perfectly suitable for your game and over time there'll be a lot of people who'll be  
**Translation:** 

**[12477.40s] English:** you know there's also a lot of indie  
**Translation:** Vocabulary: indie: 独立游戏

**[12480.00s] English:** uh developers living as content creators they'll be releasing content on fab marketplace or the  
**Translation:** 

**[12484.72s] English:** unity asset store and earn a living for that but specialization of labor is a really really  
**Translation:** Vocabulary: asset: 资产

**[12490.24s] English:** valuable thing in the early days pretty much one person would build one game like that's how a lot  
**Translation:** 

**[12494.80s] English:** of the games were built in the 1980s over time you had a separation where artists became specialized  
**Translation:** 

**[12500.00s] English:** and then programmers and then gameplay programmers and engine programmers now you have technical  
**Translation:** 

**[12503.52s] English:** iris and you have you know dozens of different specialties contributing to a triple a 3d game now  
**Translation:** Vocabulary: programmers: 程序员; specialties: 专业领域; triple: 三重

**[12509.60s] English:** and the more we can modularize uh those bits of content um see you could get something off the  
**Translation:** 

**[12515.28s] English:** shelf rather than having to build it um or have the you know engine synthesize it for you uh the  
**Translation:** Vocabulary: modularize: 模块化; synthesize: 合成

**[12521.36s] English:** more we can enable creators to create stuff fast and successfully so we should talk about the the  
**Translation:** 

**[12528.72s] English:** fact that amongst many other things you've been uh philosophically and spiritually battling  
**Translation:** Vocabulary: philosophically: 在哲学上; spiritually: 精神上

**[12537.04s] English:** monopolies in general  
**Translation:** 

**[12539.60s] English:** sort of uh one of which is sort of the apple uh marketplace that charges 30 from developers  
**Translation:** Vocabulary: monopolies: 独家垄断

**[12549.60s] English:** can you speak uh about this this idea that um you believe that apple and other companies  
**Translation:** 

**[12559.28s] English:** valve should not be charging that that kind of revenue cut  
**Translation:** Vocabulary: valve: 阀门

**[12563.36s] English:** sure well let's let's start from a very basic principle of computing the first computer i owned  
**Translation:** 

**[12569.60s] English:** was an apple ii plus you know designed by steve wozniak and marketed by apple and then an ibm pc  
**Translation:** 

**[12575.20s] English:** and in those days anybody could write code your computer literally turned on with a programming  
**Translation:** 

**[12581.36s] English:** language prompt in front of you you had to actually do work to not write a program and  
**Translation:** 

**[12585.20s] English:** to instead run somebody else's program that was incredibly empowering and anybody could write  
**Translation:** 

**[12589.68s] English:** a program anybody could put on a floppy disk anybody could share it with their friends  
**Translation:** Vocabulary: empowering: 赋权; floppy: 软盘

**[12593.76s] English:** anybody could make copies of that put it in a store they could sell it they could build a  
**Translation:** 

**[12597.68s] English:** business around it and they were comfortable with it and they were able to sell it and they were  
**Translation:** 

**[12599.60s] English:** completely  
**Translation:** 

**[12600.00s] English:** able to without seeking any big tech corporations permission do whatever they want even from ibm  
**Translation:** 

**[12607.46s] English:** remember ibm was the dominant computer company on earth at the time that they released ibm pc  
**Translation:** 

**[12612.54s] English:** as an open platform and you know so it's really been firmly implanted in my mind that this is  
**Translation:** 

**[12617.78s] English:** this was a magical and wonderful time of unmatched economic progress uh for technology  
**Translation:** 

**[12625.96s] English:** in the entire world um and you know over time the big companies have realized that they could  
**Translation:** 

**[12632.92s] English:** shut down and just block software makers from releasing software on their own and block software  
**Translation:** 

**[12639.60s] English:** makers from doing business with customers directly um and i've always viewed this practice as  
**Translation:** 

**[12646.84s] English:** terribly abusive because when you buy a computer you you spend or a phone um you spend good money  
**Translation:** 

**[12652.88s] English:** on it it's your money you spent on that phone and now you own that  
**Translation:** 

**[12655.96s] English:** And there's absolutely no reason that Apple should block you from installing apps from other developers directly, if you want, going to their web page or writing your own apps without their permission and running them yourself without having to get a developer account, without having to go through their bureaucracy.  
**Translation:** 

**[12675.00s] English:** And there's no reason that any consumer who gets an app shouldn't be able to do business directly with the developer of the consumer. You already bought that phone. Why should Apple be adding a 30% junk fee to all commerce you do? And why do they selectively apply it to some things and not others?  
**Translation:** Vocabulary: bureaucracy: 官僚主义; selectively: 选择性地

**[12693.40s] English:** I've always viewed this as deeply abusive and that it shuts down the competitive engine that once fueled the app and software economy.  
**Translation:** 

**[12701.80s] English:** It's still a vibrant, competitive engine on Windows.  
**Translation:** Vocabulary: abusive: 虐待性的; vibrant: 充满活力的

**[12704.54s] English:** And I...  
**Translation:** 

**[12705.00s] English:** On the internet, but it's no longer with mobile apps because these stores have popped up and they don't provide any useful value to the user. Yes, they're a search function to find software, but there's no reason other companies couldn't build a better one.  
**Translation:** 

**[12720.00s] English:** I bet if you had Steam or if you had Valve build Steam for iPhone,  
**Translation:** 

**[12723.52s] English:** I bet Steam for iPhone would be a much better app store than the iOS app store.  
**Translation:** Vocabulary: valve: 阀阀公司

**[12727.20s] English:** And a lot of people would use it.  
**Translation:** 

**[12729.10s] English:** And that Apple would be forced to build a better app store in competition  
**Translation:** 

**[12732.56s] English:** and that everybody would improve their products as a result.  
**Translation:** 

**[12736.28s] English:** But, you know, Apple and Google shutting down the competitive engine  
**Translation:** 

**[12739.32s] English:** that drives the software economy has massive implications for everything.  
**Translation:** 

**[12745.28s] English:** And, you know, one of them is reshaping the nature of mobile apps to be,  
**Translation:** 

**[12750.00s] English:** really offensive to gamer sensibilities.  
**Translation:** 

**[12752.54s] English:** You know, if you go on console,  
**Translation:** Vocabulary: gamer: 游戏玩家; sensibilities: 敏感性

**[12754.06s] English:** the best console games you see listed on the storefronts,  
**Translation:** 

**[12758.38s] English:** the best console games that you see reviewed are awesome games  
**Translation:** Vocabulary: storefronts: 商店橱窗

**[12761.60s] English:** that really have a lot of creative merit.  
**Translation:** 

**[12764.14s] English:** The ones that sell the best are really enormous values for their money  
**Translation:** Vocabulary: merit: 价值

**[12768.62s] English:** and are the product of an immense amount of work.  
**Translation:** 

**[12772.48s] English:** You don't see that on iPhone.  
**Translation:** Vocabulary: immense: 巨大

**[12774.52s] English:** The top apps on iPhone, the top games on iPhone at almost all times  
**Translation:** 

**[12778.34s] English:** are these ridiculously good games.  
**Translation:** Vocabulary: ridiculously: 极其

**[12780.00s] English:** They're really greedy, high monetizing, you know, whale games,  
**Translation:** 

**[12783.28s] English:** which are pervaded with pay-to-win and loot box practices.  
**Translation:** Vocabulary: monetizing: 盈利导向; pervaded: 充斥着

**[12786.58s] English:** You know, they have a sort of a legalized form of gambling.  
**Translation:** 

**[12790.26s] English:** And, you know, these games are not driven by fun.  
**Translation:** Vocabulary: legalized: 合法化的

**[12792.76s] English:** They're driven by manipulation of the players to greedy ends.  
**Translation:** 

**[12798.16s] English:** And, you know, it's very hard for the fun-based games to actually succeed there.  
**Translation:** Vocabulary: manipulation: 操控

**[12803.14s] English:** And, you know, the costs of operating these online games now are enormously high.  
**Translation:** 

**[12807.04s] English:** So you have a game that's based on fun.  
**Translation:** Vocabulary: enormously: 极其

**[12808.62s] English:** It's not loot box heavy.  
**Translation:** 

**[12810.00s] English:** You know, you have to pay 30% of your revenue to Apple  
**Translation:** 

**[12813.56s] English:** in order to just get access to the platform.  
**Translation:** 

**[12816.70s] English:** And 30% is way, way, way more than most game companies make in profits right now.  
**Translation:** 

**[12821.74s] English:** And so if that fee is more than the profit from a natural company,  
**Translation:** 

**[12825.72s] English:** then they can only stay in business by raising prices.  
**Translation:** 

**[12828.34s] English:** So these 30% fees are raising prices of all digital goods.  
**Translation:** 

**[12831.32s] English:** It's just inflationary as a force in the economy.  
**Translation:** Vocabulary: inflationary: 通货膨胀的

**[12835.22s] English:** That's just the first direct tax.  
**Translation:** 

**[12837.22s] English:** But then to reach users, when a user searches for,  
**Translation:** 

**[12840.00s] English:** before Apple blocked  
**Translation:** 

**[12842.52s] English:** Fortnite on iOS, when a user searched for  
**Translation:** Vocabulary: fortnite: 堡垒之夜

**[12844.36s] English:** Fortnite, the first result was always some  
**Translation:** 

**[12846.40s] English:** competing game. That's  
**Translation:** 

**[12848.48s] English:** utterly anti-user. You search  
**Translation:** 

**[12850.50s] English:** for Steam for a game, and if that game's on Steam,  
**Translation:** 

**[12852.84s] English:** it's the first result, always,  
**Translation:** 

**[12854.86s] English:** because Steam's not getting  
**Translation:** 

**[12856.34s] English:** inshittified with advertising. Apple  
**Translation:** 

**[12858.44s] English:** is. And they do that  
**Translation:** 

**[12860.56s] English:** so they can make even more than 30%.  
**Translation:** 

**[12862.22s] English:** So if you want to be the first search result  
**Translation:** 

**[12864.62s] English:** for your game, you're probably paying more, like 45%.  
**Translation:** 

**[12866.96s] English:** If you want to reach users on social  
**Translation:** 

**[12868.68s] English:** media, you're paying another 20%.  
**Translation:** 

**[12870.54s] English:** So literally something like 70%  
**Translation:** 

**[12872.52s] English:** of the revenue for your game is just  
**Translation:** 

**[12874.48s] English:** going into junk fees to  
**Translation:** 

**[12876.56s] English:** acquire users and get them in your game.  
**Translation:** 

**[12878.72s] English:** And the money that's left over is only  
**Translation:** 

**[12880.46s] English:** enough to fund these  
**Translation:** 

**[12881.44s] English:** games with rather abusive practices  
**Translation:** Vocabulary: abusive: 虐待性的

**[12884.64s] English:** that do not look to normal gamers like games  
**Translation:** 

**[12886.68s] English:** for the most part. Now, there are some exceptions.  
**Translation:** Vocabulary: exceptions: 特例

**[12888.34s] English:** There are some great games on iOS, and there are some games  
**Translation:** 

**[12890.44s] English:** with good practices, but  
**Translation:** 

**[12891.64s] English:** the engine has been really corrupted  
**Translation:** 

**[12894.28s] English:** in a way that competition would fix  
**Translation:** Vocabulary: corrupted: 破坏

**[12896.04s] English:** if you unleashed lots of competing stores  
**Translation:** 

**[12898.12s] English:** on iOS, then you'd have lots  
**Translation:** Vocabulary: unleashed: 释放

**[12900.36s] English:** of awesome options, and you'd have much better deals  
**Translation:** 

**[12902.36s] English:** and much better prices.  
**Translation:** 

**[12903.86s] English:** I had a quick chat with Matthew, and he asked  
**Translation:** 

**[12906.38s] English:** me to ask you this question of  
**Translation:** 

**[12907.54s] English:** why don't more companies fight  
**Translation:** 

**[12910.28s] English:** Apple in the way, openly and totally  
**Translation:** 

**[12912.48s] English:** as Epic has been?  
**Translation:** 

**[12914.94s] English:** What makes you,  
**Translation:** 

**[12916.22s] English:** what makes Epic so unique in this regard?  
**Translation:** 

**[12918.52s] English:** And I should say, I think  
**Translation:** 

**[12919.92s] English:** everything you said, I agree with  
**Translation:** 

**[12922.32s] English:** fully. I think what Apple is doing is just  
**Translation:** 

**[12924.54s] English:** wrong.  
**Translation:** 

**[12926.64s] English:** I think Apple, in many  
**Translation:** 

**[12927.88s] English:** dimensions, is an incredible company.  
**Translation:** 

**[12930.24s] English:** They have brought  
**Translation:** Vocabulary: dimensions: 维度

**[12931.14s] English:** so much good for the world. In this  
**Translation:** 

**[12934.24s] English:** regard,  
**Translation:** 

**[12935.82s] English:** I just think it's straight up wrong  
**Translation:** 

**[12938.18s] English:** what they're doing. They're not  
**Translation:** 

**[12940.08s] English:** providing the value of  
**Translation:** 

**[12942.02s] English:** 30%. And even  
**Translation:** 

**[12944.10s] English:** if they were,  
**Translation:** 

**[12945.88s] English:** the monopolization, the centralized  
**Translation:** Vocabulary: monopolization: 垄断

**[12947.68s] English:** control without competition is  
**Translation:** 

**[12949.90s] English:** wrong. Anyway, why are  
**Translation:** 

**[12951.96s] English:** you fearlessly fighting  
**Translation:** 

**[12953.56s] English:** Apple on this, and other companies don't  
**Translation:** Vocabulary: fearlessly: 无所畏惧地

**[12955.84s] English:** seem to want to step up?  
**Translation:** 

**[12957.88s] English:** All companies are terrified.  
**Translation:** 

**[12960.00s] English:** fight of apple um because apple can destroy their business um epic was in a unique position with  
**Translation:** 

**[12968.10s] English:** fortnite first of all having the you know the biggest game in the world at the time we started  
**Translation:** Vocabulary: fortnite: 堡垒之夜

**[12972.66s] English:** the fight with apple um and second of all having a majority of our users playing on pc and console  
**Translation:** 

**[12979.08s] English:** meant that if we lost access to ios during a fight then we would still be able to survive  
**Translation:** 

**[12984.18s] English:** um that said i pick apart uh spotify facebook you name the top 10 mobile apps i think none of them  
**Translation:** 

**[12993.28s] English:** would be able to survive without apple like literally their business would be destroyed  
**Translation:** 

**[12997.32s] English:** if apple blocked access to them um and apple is incredibly clear with developers that they're  
**Translation:** 

**[13005.52s] English:** willing to deprive uh all users of access to any app if they get in a fight um and if you know if  
**Translation:** 

**[13012.42s] English:** you look at how they dealt with epic they  
**Translation:** 

**[13013.98s] English:** were not just legally maneuvering with the intent of winning the court case against us they were  
**Translation:** Vocabulary: maneuvering: 运筹帷幄

**[13019.80s] English:** also sending a message to all developers in the world we will destroy your business or we will  
**Translation:** 

**[13023.88s] English:** try our best uh if you fight us and a very small number of vocal developers have been willing to  
**Translation:** Vocabulary: vocal: 声音大的

**[13029.30s] English:** speak up and apple was actually refrained from crushing their businesses when they weren't um  
**Translation:** 

**[13035.16s] English:** violating any apple policies and that took a bit of discipline which i think is also about  
**Translation:** Vocabulary: refrained: 克制; violating: 违反

**[13041.42s] English:** amount of calculation by apple that they  
**Translation:** 

**[13043.86s] English:** could  
**Translation:** 

**[13043.98s] English:** didn't survive being seen as the company killer um if you criticize this will crush your company  
**Translation:** 

**[13048.86s] English:** um but you know the other thing apple has that they can and will readily deploy against every  
**Translation:** Vocabulary: deploy: 部署

**[13055.08s] English:** developer is soft power when they take 30 and advertising is so expensive soft power by apple  
**Translation:** 

**[13062.08s] English:** like approving your updates faster or slowing down all of your updates by a couple weeks  
**Translation:** Vocabulary: approving: 批准

**[13066.72s] English:** can also have a dramatic effect on your ability to compete successfully and apple has a very long  
**Translation:** 

**[13072.50s] English:** history of playing cat and mouse and i think that's a very important part of the game and i  
**Translation:** 

**[13073.98s] English:** think that's one level that if you want to profit from all the mouse games for the you want to  
**Translation:** 

**[13075.98s] English:** bullish affordability for your exit evasion experience you're going to have to play multiple  
**Translation:** Vocabulary: affordability: 承受能力; bullish: 看涨; evasion: 规避

**[13093.14s] English:** months and it means like being  
**Translation:** 

**[13094.18s] English:** equal with alt involved and determine if a company wants toир because you're pro- juegos  
**Translation:** 

**[13098.10s] English:** and you know that stuff so you instantly insist on playing every single one and now it's okay and  
**Translation:** 

**[13080.00s] English:** down on the updates so they're they've been slowing down updates for several major tech  
**Translation:** 

**[13084.10s] English:** companies uh sometimes for weeks sometimes for months without all going under the radar because  
**Translation:** 

**[13088.70s] English:** everybody's afraid to challenge them publicly um and so apple is wielding a soft power can change  
**Translation:** Vocabulary: wielding: 使用

**[13094.56s] English:** a company's economics for the worse enough to deter almost any public company and you know epic  
**Translation:** 

**[13100.16s] English:** is in the fight because i firmly believe that something like the metaverse will only arise it's  
**Translation:** Vocabulary: deter: 阻止; metaverse: 元宇宙

**[13104.72s] English:** something like a billion plus user you know real-time 3d social ecosystem that grows to  
**Translation:** 

**[13112.14s] English:** encompass potentially all or most major games by all major developers tied together into an open  
**Translation:** 

**[13118.56s] English:** economy where they all participate as peers and they all compete to give users the best deals  
**Translation:** 

**[13123.14s] English:** and they grow and you know do business with their customers directly that thing can only exist  
**Translation:** 

**[13129.64s] English:** if the apple and google gatekeeping monopolies are lifted  
**Translation:** 

**[13134.72s] English:** and it's not just the 30 fees the 30 fees are economically ruinous but they impose other  
**Translation:** Vocabulary: economically: 经济上; gatekeeping: 把关; monopolies: 垄断

**[13140.06s] English:** levels of control apple prevents all web browsers on ios from implementing web standards better than  
**Translation:** 

**[13145.68s] English:** apple does so apple has really limited data storage capabilities um and uh 3d graphics  
**Translation:** Vocabulary: browsers: 浏览器; implementing: 实现

**[13153.48s] English:** capabilities on you know the ios web apis so apis you can access from web apps running within a web  
**Translation:** 

**[13159.40s] English:** browser and you know that's to intentionally cripple those apps so to ensure they can't  
**Translation:** 

**[13163.72s] English:** possibly compete  
**Translation:** 

**[13164.72s] English:** uh with native apps and by depriving web apps of those features they prevent web apps from being  
**Translation:** Vocabulary: depriving: 剥夺

**[13171.06s] English:** competing with native apps well you know apple if they treat the metaverse the way they treat the  
**Translation:** 

**[13176.10s] English:** web they'll say you can only use apple's metaverse engine unreal engine is disallowed um and then they  
**Translation:** 

**[13182.06s] English:** can impose all their own limitations on the metaverse to force all commerce through apple  
**Translation:** 

**[13185.84s] English:** or force it to be so uncompetitive and lousy um that it can't compete and you know they have this  
**Translation:** Vocabulary: uncompetitive: 缺乏竞争力

**[13192.12s] English:** giant array of these anti-competitive techniques they use to compete with native apps and they're  
**Translation:** 

**[13194.72s] English:** they use to disadvantage other app developers um you know saying only apple can build certain kinds  
**Translation:** 

**[13199.86s] English:** of  
**Translation:** 

**[13200.00s] English:** apps where only Apple can integrate certain features in Europe,  
**Translation:** Vocabulary: integrate: 整合

**[13203.62s] English:** even where the DMA law requires Apple to allow competing stores.  
**Translation:** 

**[13207.22s] English:** They say a store can only be a store.  
**Translation:** 

**[13209.20s] English:** You can't build a store into Facebook.  
**Translation:** 

**[13211.20s] English:** You can't build a social network into a store.  
**Translation:** 

**[13213.34s] English:** A store must only be a store because a store that's more than a store  
**Translation:** 

**[13216.18s] English:** might be able to compete with us more effectively.  
**Translation:** 

**[13219.12s] English:** It's just a giant, you know, to use the Soviet term,  
**Translation:** 

**[13222.68s] English:** it's a defense in depth strategy where they've constructed a massive series of barriers.  
**Translation:** Vocabulary: barriers: 防御屏障

**[13227.42s] English:** Each are fatal to any attempt to compete effectively.  
**Translation:** 

**[13230.00s] English:** So that even if one barrier is overcome,  
**Translation:** 

**[13232.10s] English:** the others remain in place and shut down the whole scheme.  
**Translation:** 

**[13234.78s] English:** And that's playing out in Europe where Apple has enabled us to launch the Epic Games Store,  
**Translation:** 

**[13238.94s] English:** but has made it so difficult and uncompetitive,  
**Translation:** 

**[13243.06s] English:** both for Epic and for clients who we want to do business with,  
**Translation:** 

**[13246.34s] English:** that it has no chance of success until the European Union starts to really enforce the DMA law  
**Translation:** 

**[13252.04s] English:** and impose harsh and serious penalties on Apple to force compliance.  
**Translation:** 

**[13256.68s] English:** I think it should be said, and once again, I think it's wrong.  
**Translation:** 

**[13260.00s] English:** What they're doing there, and I hope there's public pressure and government pressure  
**Translation:** 

**[13264.00s] English:** for them to open up the platform.  
**Translation:** 

**[13268.14s] English:** I believe as a person who loves Apple, I believe this is also good for Apple.  
**Translation:** 

**[13278.04s] English:** There's the natural thing in companies to want to close and control and crush competition.  
**Translation:** 

**[13285.06s] English:** But like Apple is full of brilliant engineers.  
**Translation:** 

**[13288.16s] English:** Open it up and win.  
**Translation:** 

**[13290.00s] English:** It's going to create the right kind of competitive incentive to make the Apple Store better.  
**Translation:** Vocabulary: incentive: 激励

**[13296.82s] English:** Because they're great at creating great interfaces.  
**Translation:** 

**[13300.70s] English:** But competition will sharpen the sword.  
**Translation:** Vocabulary: interfaces: 人机界面

**[13302.94s] English:** I mean, it's just going to make everything much better.  
**Translation:** 

**[13306.32s] English:** So I do hope there's a lot of public pressure.  
**Translation:** 

**[13308.68s] English:** And I deeply appreciate that you're speaking out in this way,  
**Translation:** 

**[13311.70s] English:** sort of putting that pressure and letting people know,  
**Translation:** 

**[13316.24s] English:** like it's okay to say that this is wrong.  
**Translation:** 

**[13318.10s] English:** Thanks.  
**Translation:** 

**[13318.88s] English:** Yeah.  
**Translation:** 

**[13319.02s] English:** Competition makes everybody.  
**Translation:** 

**[13320.00s] English:** better uh you have a monopoly that's forced to compete suddenly the monopolies products get much  
**Translation:** 

**[13324.52s] English:** better the offerings to consumers get much better you see so many areas where apple could be the  
**Translation:** Vocabulary: monopolies: 独家经营; monopoly: 垄断

**[13330.18s] English:** best uh but what they have is just really really lousy and it's this old guard of leadership who  
**Translation:** 

**[13335.02s] English:** is clinging to these old policies turning themselves into the enemy of every developer  
**Translation:** Vocabulary: clinging: 死守

**[13340.30s] English:** every regulator and i think it's ultimately massively to their detriment and i can't wait  
**Translation:** 

**[13344.78s] English:** for a new generation to come in and you know paint a bright path to the future we were epic  
**Translation:** Vocabulary: massively: 巨大地; regulator: 监管者

**[13349.78s] English:** was an awesome partnership apple uh for more than a decade of demos and partnership and technology  
**Translation:** 

**[13356.42s] English:** usage together and we did amazing things together i'd love nothing more than to uh to have that  
**Translation:** Vocabulary: demos: 演示

**[13361.74s] English:** apple uh you know bringing back steve wozniak's original views just the apple 2 is such an amazing  
**Translation:** 

**[13369.88s] English:** thing it's a completely open platform the the manual to the apple 2 included a listing for all  
**Translation:** 

**[13375.56s] English:** the roms the source code to the roms so you could understand exactly what was happening there and  
**Translation:** 

**[13379.30s] English:** you could  
**Translation:** 

**[13379.66s] English:** you could  
**Translation:** 

**[13379.76s] English:** you could  
**Translation:** 

**[13379.78s] English:** learn from it included a hardware schematic of the entire computer so you could learn how to make a  
**Translation:** 

**[13384.96s] English:** peripheral and plug it in an open ecosystem and that's the awesome apple that that company would  
**Translation:** Vocabulary: peripheral: 外设; schematic: 原理图

**[13390.20s] English:** be the best company in the world again i think the current one is just on the wrong side of history  
**Translation:** 

**[13396.00s] English:** and needs to change well i hope epic and apple find a path forward together and flourishing  
**Translation:** Vocabulary: flourishing: 繁荣昌盛

**[13402.16s] English:** together and apple embraces competition better one of the things i admire about this conversation  
**Translation:** 

**[13408.06s] English:** that you mentioned steam  
**Translation:** Vocabulary: embraces: 接纳

**[13409.56s] English:** a bunch  
**Translation:** 

**[13410.30s] English:** with kind words supportive and basically never mentioned epic game store i love that so i really  
**Translation:** 

**[13418.16s] English:** love that it really embodies the fact that you want variety you want freedom uh for people to  
**Translation:** 

**[13425.88s] English:** choose the best thing and and and and in so doing create this large network of humans interacting  
**Translation:** Vocabulary: embodies: 体现

**[13433.28s] English:** freely with each other okay that said uh one of the competitive pressures that i've had in the  
**Translation:** 

**[13439.54s] English:** epic is  
**Translation:** 

**[13440.38s] English:** has also harnessing the tbsp you know i do  
**Translation:** 

**[13447.64s] English:** about min esquire i don't know  
**Translation:** Vocabulary: esquire: 先生; harnessing: 利用

**[13450.40s] English:** really  
**Translation:** 

**[13451.62s] English:** great  
**Translation:** 

**[13455.50s] English:** did i  
**Translation:** 

**[13457.58s] English:** change  
**Translation:** 

**[13460.24s] English:** yeah  
**Translation:** 

**[13461.30s] English:** it had  
**Translation:** 

**[13464.14s] English:** completely  
**Translation:** 

**[13464.72s] English:** changed  
**Translation:** 

**[13465.70s] English:** but it doesn't mean  
**Translation:** 

**[13466.48s] English:** but the  
**Translation:** 

**[13467.50s] English:** not  
**Translation:** 

**[13469.04s] English:** app  
**Translation:** 

**[13440.00s] English:** created a few years ago was by launching the epic game store and instead of steam's 30 percent  
**Translation:** 

**[13446.90s] English:** revenue cut you went with 12 percent revenue cut creating the competitive pressure saying you know  
**Translation:** 

**[13454.24s] English:** listen this shouldn't be that high of a cut and uh which i thought was like amazing this is this  
**Translation:** 

**[13463.34s] English:** is a brilliant idea and i think it still is a brilliant idea it's wonderful now in preparing  
**Translation:** 

**[13467.56s] English:** for this conversation i looked on the internet and i saw there's a lot of criticism of uh egs  
**Translation:** 

**[13473.74s] English:** epic game store uh first of all i should say the internet  
**Translation:** 

**[13477.74s] English:** is full of drama and criticism like there's just not enough celebrating of awesome shit that let's  
**Translation:** 

**[13487.18s] English:** if i can ask the internet as a blob one request can we just celebrate  
**Translation:** 

**[13491.50s] English:** awesome shit and also criticize but just like there's not enough celebration anyway  
**Translation:** 

**[13496.52s] English:** the  
**Translation:** 

**[13497.56s] English:** the two uh directions of criticism is just straight up the launcher interface is clunky  
**Translation:** 

**[13504.82s] English:** and lacks a lot of the features of steam and then the second uh set of criticism is  
**Translation:** Vocabulary: clunky: 笨拙; interface: 界面; launcher: 启动器

**[13510.96s] English:** the exclusive contracts which uh were made with some of the games that are on epic game store  
**Translation:** 

**[13521.52s] English:** so first huge props on the 12 percent maybe you could speak to the vision of that  
**Translation:** Vocabulary: props: 表扬

**[13526.72s] English:** and second  
**Translation:** 

**[13527.56s] English:** can you comment on those two criticisms uh sure yeah uh i think yeah one of the reasons that  
**Translation:** Vocabulary: criticisms: 批评

**[13535.10s] English:** people characterize the epic games launcher as clunky is because like the epic games launcher  
**Translation:** 

**[13540.52s] English:** is clunky um and we need to improve this um you know there's a lot of work going on there and um  
**Translation:** Vocabulary: characterize: 形容

**[13547.98s] English:** you know i wish we'd gotten better at addressing quality of life features uh and prioritize them  
**Translation:** 

**[13554.04s] English:** above uh all the other features you know because steam has a lot of the features that are on epic  
**Translation:** Vocabulary: prioritize: 优先考虑

**[13557.56s] English:** He has 15 years of built-up work.  
**Translation:** 

**[13560.00s] English:** by many of the best programmers in the whole industry working on that.  
**Translation:** Vocabulary: programmers: 程序员

**[13563.38s] English:** A much larger team working on Steam and a lot more time working on it.  
**Translation:** 

**[13569.04s] English:** And so we've had to make a lot of prioritization decisions  
**Translation:** Vocabulary: prioritization: 优先级设定

**[13571.42s] English:** about what do we support with the Epic Games Store and when.  
**Translation:** 

**[13575.12s] English:** A lot of the time it's been supporting commercial features like merchandising,  
**Translation:** Vocabulary: merchandising: 商品销售

**[13578.66s] English:** offering multiple versions of a game for sale,  
**Translation:** 

**[13580.78s] English:** and offering upgrades from the regular edition, the deluxe edition,  
**Translation:** Vocabulary: deluxe: 豪华版

**[13583.84s] English:** and other things that partners work.  
**Translation:** 

**[13585.72s] English:** And other priorities have been quality of life and launcher load times  
**Translation:** Vocabulary: priorities: 优先事项

**[13589.42s] English:** and other things, and we've not put enough emphasis  
**Translation:** 

**[13592.08s] English:** on the quality of life features.  
**Translation:** 

**[13594.32s] English:** We've recognized this very clearly multiple times  
**Translation:** 

**[13597.12s] English:** and we've gone through multiple refactorings.  
**Translation:** Vocabulary: refactorings: 重构

**[13598.78s] English:** But that's definitely been a disappointment to us and to a lot of users.  
**Translation:** 

**[13604.40s] English:** And I think one thing it took us a while to realize was it's non-uniform.  
**Translation:** 

**[13609.76s] English:** Depending on your proximity to a CDN and the size of your game collection,  
**Translation:** 

**[13614.40s] English:** it can be either awesome or really clunky.  
**Translation:** Vocabulary: proximity: 距离

**[13618.10s] English:** And the users for it.  
**Translation:** 

**[13619.42s] English:** And when it's really clunky, other people, I think, are a large part of the complaints.  
**Translation:** 

**[13625.28s] English:** They're going to speak up.  
**Translation:** 

**[13626.52s] English:** And I should also say that the Steam launcher, for a long time,  
**Translation:** 

**[13630.48s] English:** from my memory but also just looking online, was also very clunky in the beginning.  
**Translation:** 

**[13635.12s] English:** Yeah, and one of the criticisms of Epic Games Store from the beginning  
**Translation:** Vocabulary: clunky: 笨拙的

**[13639.68s] English:** was you don't have all of the features of Steam.  
**Translation:** 

**[13641.54s] English:** But we very much don't want to have all of the features of Steam.  
**Translation:** 

**[13644.18s] English:** Steam has forums dedicated to your game.  
**Translation:** 

**[13646.26s] English:** And we decide we don't want to create forums.  
**Translation:** 

**[13648.80s] English:** And our partners,  
**Translation:** 

**[13649.46s] English:** when we talked to them,  
**Translation:** 

**[13650.20s] English:** generally didn't want us to create Epic Games Store forums for their games  
**Translation:** 

**[13653.00s] English:** because there's already channels that they prefer to them.  
**Translation:** 

**[13656.62s] English:** There's social media and a number of platforms.  
**Translation:** 

**[13658.88s] English:** And there's Reddit.  
**Translation:** 

**[13659.62s] English:** And there's lots of places for gamers to discuss their game.  
**Translation:** 

**[13662.96s] English:** And they prefer those discussions to be there.  
**Translation:** 

**[13665.72s] English:** And so it's very much not our goal to mimic everything in Steam.  
**Translation:** 

**[13669.44s] English:** But we do want to have all of the convenience features  
**Translation:** 

**[13671.70s] English:** that makes it easy and fun to use as Steam.  
**Translation:** 

**[13674.70s] English:** So there's a long journey ahead.  
**Translation:** 

**[13677.00s] English:** But we continue to reinvest in it.  
**Translation:** 

**[13678.86s] English:** And, you know,  
**Translation:** Vocabulary: reinvest: 重新投资

**[13679.42s] English:** we're working.  
**Translation:** 

**[13680.00s] English:** to build a multi-billion dollar business there and think we'll succeed um already at the epic  
**Translation:** 

**[13685.22s] English:** game store uh it supports an immense amount of epic games commerce and fortnite on pc um now on  
**Translation:** 

**[13692.76s] English:** android and ios and the european union too um so it's a forever facet of the industry and we are  
**Translation:** Vocabulary: facet: 方面; fortnite: 堡垒之夜; immense: 庞大

**[13698.04s] English:** never losing heart in it um and we think at some point you know i really feel that the benefits of  
**Translation:** 

**[13703.90s] English:** the epic games approach are going to outweigh the benefits of the steam approach especially  
**Translation:** 

**[13708.28s] English:** as gaming becomes multi-platform one of the things that really sucks for all gamers is that  
**Translation:** 

**[13713.90s] English:** you know you have a lot of friends in the real world somehow everyone has different platforms  
**Translation:** 

**[13719.18s] English:** your steam friends aren't connected to your xbox friends and they're not connected to your  
**Translation:** 

**[13723.68s] English:** playstation friends your nintendo friends and so you're very much bottling up pc gaming into a  
**Translation:** 

**[13729.46s] English:** kind of a hardcore group of pc only folks and making all the other aspects of it difficult  
**Translation:** 

**[13734.44s] English:** you know a lot of games have flocked towards discord which is a mess in its  
**Translation:** Vocabulary: hardcore: 极端爱好者

**[13738.26s] English:** self can now your steam name is not your discord name and that's not your playstation name and so  
**Translation:** 

**[13741.92s] English:** now you have three two people in a game and they have four different identities and that sucks um  
**Translation:** 

**[13747.40s] English:** you know our aim for that is you know with epic online services and the social systems that we  
**Translation:** 

**[13752.50s] English:** built uh for fortnite opened up to all developers to have cross-platform social features be super  
**Translation:** 

**[13758.76s] English:** easy and free for all developers this is not something we're trying to gatekeep or rent seek  
**Translation:** 

**[13762.82s] English:** on um or lock people into it's just a way that we're making social gaming  
**Translation:** Vocabulary: gatekeep: 把关收费

**[13768.26s] English:** easier for everybody as more and more games follow the fortnite approach of being multi-platform  
**Translation:** 

**[13772.92s] English:** especially multiplayer games you know metcast law is a very real phenomena in the industry it's the  
**Translation:** 

**[13778.40s] English:** thing that's upending some games and causing growth in other games it is the number one trend  
**Translation:** 

**[13784.66s] English:** for pervading the world of gaming today and it says that you know your game is quadratically  
**Translation:** Vocabulary: pervading: 渗透; quadratically: 二次地

**[13790.48s] English:** more valuable the more percentage of a user's real world friends they can connect to um your game  
**Translation:** 

**[13796.26s] English:** vastly benefits  
**Translation:** 

**[13798.26s] English:** by connecting all of its players together  
**Translation:** 

**[13800.00s] English:** and not segregating them off  
**Translation:** 

**[13801.84s] English:** into different online platform populations and so on.  
**Translation:** 

**[13805.28s] English:** And so I think the future trend is in that direction.  
**Translation:** 

**[13808.26s] English:** I wish Valve had opened up Steamworks  
**Translation:** 

**[13810.06s] English:** to just work on all platforms.  
**Translation:** Vocabulary: steamworks: 蒸汽机; valve: 阀门

**[13811.38s] English:** They could have easily done it.  
**Translation:** 

**[13813.24s] English:** We did it.  
**Translation:** 

**[13814.72s] English:** But they seem to be using it as a lever  
**Translation:** 

**[13816.82s] English:** to keep people locked into the Steam PC game store.  
**Translation:** Vocabulary: lever: 杠杆

**[13820.76s] English:** And that's going to be a long-running battle  
**Translation:** 

**[13825.20s] English:** because there's always a very toxic group of Steam users.  
**Translation:** 

**[13827.98s] English:** They even created an entire subreddit  
**Translation:** 

**[13830.04s] English:** dedicated to criticizing Epic on our store.  
**Translation:** Vocabulary: subreddit: 子版块

**[13833.28s] English:** And they create basically harassment campaigns at times  
**Translation:** 

**[13836.28s] English:** against developers who use Epic Online services.  
**Translation:** Vocabulary: harassment: 骚扰

**[13841.62s] English:** Developers do that so they can connect their players  
**Translation:** 

**[13843.62s] English:** across platforms and have friends across platforms  
**Translation:** 

**[13845.84s] English:** and voices across platforms.  
**Translation:** 

**[13847.56s] English:** But suddenly that's trying to be turned into a negative.  
**Translation:** 

**[13852.68s] English:** It's clear that Epic wants developers to win,  
**Translation:** 

**[13857.56s] English:** wants...  
**Translation:** 

**[13857.98s] English:** gamers to win,  
**Translation:** 

**[13860.08s] English:** and wants Steam to do awesome also.  
**Translation:** 

**[13863.60s] English:** And in the competition between Steam and Epic Game Store,  
**Translation:** 

**[13868.64s] English:** like, create awesome stuff together.  
**Translation:** 

**[13871.98s] English:** I mean, it's obvious to me,  
**Translation:** 

**[13874.30s] English:** if you don't read the stuff online,  
**Translation:** 

**[13876.14s] English:** but online it's like there is this just negativity  
**Translation:** 

**[13881.12s] English:** that I don't think is constructive in general.  
**Translation:** Vocabulary: negativity: 消极

**[13884.90s] English:** And I should give a big sort of...  
**Translation:** 

**[13887.98s] English:** positive thank you and props  
**Translation:** Vocabulary: props: 表扬

**[13890.72s] English:** for the push to multi-platform  
**Translation:** 

**[13893.56s] English:** that was always there for Fortnite.  
**Translation:** Vocabulary: fortnite: 堡垒之夜

**[13897.84s] English:** Perhaps before the pressure that Epic created  
**Translation:** 

**[13900.88s] English:** on breaking the barriers of Xbox and PlayStation and PC  
**Translation:** Vocabulary: barriers: 障碍

**[13904.68s] English:** and being multi-platform.  
**Translation:** 

**[13908.24s] English:** Like, I got a chance to play with Fortnite a little bit with you  
**Translation:** 

**[13910.78s] English:** and all the people in the group.  
**Translation:** 

**[13912.60s] English:** By the way, awesome interface.  
**Translation:** Vocabulary: interface: 用户界面

**[13914.64s] English:** Audio chat, really fun.  
**Translation:** 

**[13916.64s] English:** But you could see, like,  
**Translation:** 

**[13917.56s] English:** a couple of PC folks at PlayStation...  
**Translation:** 

**[13920.00s] English:** person xbox person all together you can't really tell what they're using except for a little icon  
**Translation:** 

**[13925.32s] English:** and it's it's nice it's like all those barriers that we've created with these platforms  
**Translation:** 

**[13930.38s] English:** are gone and you creating the pressure with uh with epic game store and just everything you're  
**Translation:** 

**[13937.28s] English:** doing with this with fortnite platform uh it's really nice there's no reason to create these  
**Translation:** 

**[13942.60s] English:** silos because ultimately you should put the gamer first and uh let everybody interact  
**Translation:** Vocabulary: gamer: 玩家; silos: 信息孤岛

**[13948.78s] English:** uh with with with actual real life friends and make new friends across the entire network of  
**Translation:** 

**[13954.16s] English:** humans so anyway thank you for that thank you for creating that pressure oh thanks yeah that was an  
**Translation:** 

**[13960.10s] English:** interesting time sony had a long-running policy preventing cross-platform play uh and we had a  
**Translation:** 

**[13966.68s] English:** long series of conversations which uh got pretty harsh towards the end um but so many sony  
**Translation:** 

**[13973.08s] English:** ultimately came around and they opened up playstation and you know through a series of  
**Translation:** 

**[13977.76s] English:** private conversations  
**Translation:** 

**[13978.78s] English:** they did the right thing um and not only that our partnership with sony has increased uh  
**Translation:** 

**[13982.60s] English:** you know since that argument back in 2018 and uh we've gotten closer and closer and done ever more  
**Translation:** 

**[13988.36s] English:** things with you know sony you know brand ip like the characters from god of war and other games  
**Translation:** 

**[13993.78s] English:** coming into fortnite um and you know all kinds of crossovers massive unreal engine adoption and  
**Translation:** Vocabulary: crossovers: 跨平台联动

**[13999.36s] English:** sony for making games for making movies at sony pictures music partnerships with sony music um  
**Translation:** 

**[14004.86s] English:** that's been an absolutely wonderful relationship i think  
**Translation:** Vocabulary: partnerships: 合作关系

**[14008.78s] English:** that stands as a an awesome example of a company that you know because of historic reasons got  
**Translation:** 

**[14014.60s] English:** uh stuck with a policy that no longer made sense for the future and um you know following a serious  
**Translation:** 

**[14020.50s] English:** discussion with a close partner righted it and did an awesome thing and now sony is much better  
**Translation:** 

**[14025.54s] English:** off and epic's better off and all game developers are better off and the whole console industry  
**Translation:** 

**[14029.16s] English:** i think it's a lot stronger now than it would have been if you know these silos had continued  
**Translation:** 

**[14033.80s] English:** playing out and despite the kind of potential concern that like  
**Translation:** 

**[14038.78s] English:** maybe blocking  
**Translation:** 

**[14040.00s] English:** platform play with xbox gave sony advantage you know sony's actually grown uh in market share  
**Translation:** 

**[14045.00s] English:** relative to xbox since that time and so you can't say that anything but good goodness came of that  
**Translation:** 

**[14050.56s] English:** that time i think a better version of apple would have received uh the email i sent to senior apple  
**Translation:** 

**[14058.72s] English:** management and been like huh there's an issue here we should have a discussion we should reconsider  
**Translation:** 

**[14063.14s] English:** this we should listen and you know they didn't and that's why uh we're in the midst of a five-year  
**Translation:** Vocabulary: reconsider: 重新考虑

**[14069.08s] English:** battle with apple and in you know the hopefully uh they're still the early days of a 15 plus year  
**Translation:** 

**[14076.80s] English:** partnership with sony come on apple we love you apple do a little bit better the second line of  
**Translation:** 

**[14083.94s] English:** criticism that i mentioned the exclusive contracts with some of the games uh can you just speak to  
**Translation:** 

**[14088.92s] English:** that because in so much of the journey of epic you've been sort of against exclusivity let's  
**Translation:** Vocabulary: exclusivity: 独家发行

**[14094.36s] English:** back up and talk about the principles at work here uh apple apple force  
**Translation:** 

**[14099.06s] English:** forcing other companies to use their payment service is a cursive decision by apple  
**Translation:** Vocabulary: cursive: 草率

**[14104.72s] English:** but if apple convinced other developers to use their payment service by offering benefits or a  
**Translation:** 

**[14114.90s] English:** better deal uh or funding or any other positive incentive then that would be perfectly fine  
**Translation:** Vocabulary: incentive: 激励

**[14119.92s] English:** one is preventing competition and the other is actual competition um epic has never forced any  
**Translation:** 

**[14127.92s] English:** developer to use their payment service to use their payment service to use their payment service  
**Translation:** 

**[14129.06s] English:** into any sort of exclusivity relationship rather we've offered developers uh payment um or incentives  
**Translation:** 

**[14135.70s] English:** or marketing or any number of things of value to them um in exchange for coming to our store  
**Translation:** Vocabulary: incentives: 激励措施

**[14140.14s] English:** exclusively and it's their game uh so it's entirely and rightfully up to them to decide  
**Translation:** 

**[14148.22s] English:** how to distribute it um and to make the decisions about their business it's their game if they want  
**Translation:** 

**[14153.62s] English:** to distribute it through steam they can if they want to distribute it through epic exclusively  
**Translation:** 

**[14157.42s] English:** they can if they want to distribute it through steam they can if they want to distribute it  
**Translation:** 

**[14159.06s] English:** through both  
**Translation:** 

**[14160.00s] English:** then they could do that as well.  
**Translation:** 

**[14162.78s] English:** And if we pay them money or other things of value  
**Translation:** 

**[14165.70s] English:** in exchange for them coming exclusively to the Epic Games Store,  
**Translation:** 

**[14168.52s] English:** I think that's their right.  
**Translation:** 

**[14169.58s] English:** And this is an example of Epic, an underdog,  
**Translation:** 

**[14173.46s] English:** with a tiny fraction of Steam's market share,  
**Translation:** 

**[14175.96s] English:** working to proactively compete with Steam  
**Translation:** 

**[14178.88s] English:** by offering a better supply of games.  
**Translation:** 

**[14181.14s] English:** And some consumers who prefer Steam  
**Translation:** 

**[14183.36s] English:** might prefer that the game be on Steam,  
**Translation:** 

**[14185.48s] English:** but the developer in each case has decided  
**Translation:** 

**[14188.16s] English:** that they believe they would benefit more  
**Translation:** 

**[14191.16s] English:** by doing this exclusive deal in exchange for benefits  
**Translation:** 

**[14193.64s] English:** than by being on Steam.  
**Translation:** 

**[14195.60s] English:** And one of the key exhibits in the Epic Google trial  
**Translation:** Vocabulary: exhibits: 证据

**[14199.20s] English:** was its opening exhibit,  
**Translation:** 

**[14201.10s] English:** which was trying to point out to the jury in the trial  
**Translation:** 

**[14205.22s] English:** the benefits of exclusives.  
**Translation:** 

**[14208.00s] English:** Like, imagine a new store popping up.  
**Translation:** Vocabulary: exclusives: 独家商品

**[14210.88s] English:** The store has a big sign outside of it.  
**Translation:** 

**[14213.02s] English:** We're the new store.  
**Translation:** 

**[14214.88s] English:** We have everything that the other store has,  
**Translation:** 

**[14217.04s] English:** and it's at the same price.  
**Translation:** 

**[14218.84s] English:** Are you going to go to the new store?  
**Translation:** 

**[14220.44s] English:** No.  
**Translation:** 

**[14221.30s] English:** You know, nobody's going to switch from Steam  
**Translation:** 

**[14223.06s] English:** if Steam has all the same games as the competing store  
**Translation:** 

**[14226.06s] English:** and everything's priced just the same.  
**Translation:** 

**[14228.62s] English:** And so we looked at initially two ways  
**Translation:** 

**[14230.80s] English:** of competing with Steam strongly.  
**Translation:** 

**[14232.24s] English:** We wanted to sell games at a better price than Steam.  
**Translation:** 

**[14236.42s] English:** By agreeing on the amount of money we pay each game developer,  
**Translation:** 

**[14240.28s] English:** you know, if the game's going to sell for $50  
**Translation:** 

**[14242.68s] English:** and we take 12%,  
**Translation:** 

**[14243.98s] English:** we'd actually lower the price  
**Translation:** 

**[14246.02s] English:** and potentially even lower the price.  
**Translation:** 

**[14248.14s] English:** And lose some money to offer a better deal.  
**Translation:** 

**[14249.90s] English:** Well, you know, we tried to pursue this,  
**Translation:** 

**[14253.46s] English:** but very quickly, every developer told us  
**Translation:** 

**[14257.64s] English:** that they wouldn't agree to better pricing  
**Translation:** 

**[14259.78s] English:** because if they did,  
**Translation:** 

**[14261.66s] English:** then Steam would stop giving them, you know,  
**Translation:** 

**[14263.68s] English:** marketing featuring and benefits  
**Translation:** 

**[14265.26s] English:** and the console makers would be mad  
**Translation:** 

**[14266.78s] English:** and all their relationships would be harmed.  
**Translation:** 

**[14270.30s] English:** You know, so there's an undercurrent  
**Translation:** 

**[14271.74s] English:** of powerful platforms and ecosystems  
**Translation:** Vocabulary: undercurrent: 暗流

**[14275.02s] English:** encouraging developers not to compete on price.  
**Translation:** 

**[14277.62s] English:** So not being able to compete on price.  
**Translation:** 

**[14280.00s] English:** we decided to compete on supply by doing exclusive deals.  
**Translation:** 

**[14283.24s] English:** And we signed a lot of them, paid developers lots and lots of money.  
**Translation:** 

**[14286.44s] English:** I think we distributed over a billion dollars in net expenditures to developers  
**Translation:** 

**[14290.96s] English:** beyond the revenue we actually made from games  
**Translation:** 

**[14295.18s] English:** in order to get a whole lot of exclusive games.  
**Translation:** 

**[14297.66s] English:** Some were successful, some weren't.  
**Translation:** 

**[14299.34s] English:** Borderlands did awesomely on the Epic Games Store,  
**Translation:** 

**[14301.76s] English:** and we and Gearbox felt that it did just as well through Epic  
**Translation:** Vocabulary: awesomely: 非常出色; borderlands: 边疆之地; gearbox: 变速箱

**[14305.98s] English:** as it would have done on Steam,  
**Translation:** 

**[14307.70s] English:** because the players who wanted Borderlands wanted Borderlands,  
**Translation:** 

**[14311.08s] English:** and they came and got it.  
**Translation:** 

**[14312.44s] English:** Whereas a lot of other games, some smaller games especially,  
**Translation:** 

**[14314.80s] English:** that didn't have a dedicated audience that was absolutely going to play the game,  
**Translation:** 

**[14318.56s] English:** typically benefited from exposure on Steam.  
**Translation:** 

**[14320.82s] English:** They were reaching an audience they wouldn't have reached organically,  
**Translation:** 

**[14323.42s] English:** and so some of them, in the end, we and they concluded that they did worse  
**Translation:** Vocabulary: organically: 自然地

**[14327.22s] English:** by being on the Epic Games Store exclusively  
**Translation:** 

**[14329.54s] English:** in terms of reaching fewer customers.  
**Translation:** 

**[14332.80s] English:** And so we had these limited-time exclusives.  
**Translation:** 

**[14335.44s] English:** When they ran out, they put their games on Steam,  
**Translation:** Vocabulary: exclusives: 限时独占版

**[14337.12s] English:** and lots of data was gathered to understand what worked.  
**Translation:** 

**[14340.72s] English:** And so this worked well for some games, didn't work for other games,  
**Translation:** 

**[14343.38s] English:** but companies seeking to compete,  
**Translation:** 

**[14349.74s] English:** especially underdogs seeking to compete,  
**Translation:** Vocabulary: underdogs: 弱者

**[14351.70s] English:** have to offer some unique value,  
**Translation:** 

**[14353.30s] English:** have to offer something that's not available through the competitors.  
**Translation:** 

**[14357.30s] English:** And I get that Steam users who just prefer using Steam and buying games on Steam  
**Translation:** 

**[14360.42s] English:** when they have their library in one place don't like this,  
**Translation:** 

**[14362.84s] English:** but you're never going to have competition for better deals  
**Translation:** 

**[14365.36s] English:** if you don't support...  
**Translation:** 

**[14367.12s] English:** the competitive mechanisms that allow competitors to come about.  
**Translation:** 

**[14370.68s] English:** I think if Valve were forced, through Epic Games Store's success,  
**Translation:** Vocabulary: valve: 阀门

**[14374.00s] English:** to compete with Epic Games Store,  
**Translation:** 

**[14375.50s] English:** then developers would be getting a better deal,  
**Translation:** 

**[14377.68s] English:** consumers would be getting a better deal,  
**Translation:** 

**[14379.50s] English:** and these 30% fees would be driven down quite a lot  
**Translation:** 

**[14382.48s] English:** towards the actual costs that are required to support the stores.  
**Translation:** 

**[14386.62s] English:** Yeah, I mean, there's a lot to be said there.  
**Translation:** 

**[14390.08s] English:** You know, I've gotten to watch Spotify try to do this with podcasts.  
**Translation:** 

**[14396.88s] English:** You know,  
**Translation:** 

**[14397.04s] English:** I've gotten to watch Spotify try to do this with podcasts.  
**Translation:** 

**[14397.10s] English:** enter as the underdog into the space  
**Translation:** Vocabulary: underdog: 弱者

**[14399.22s] English:** and try to...  
**Translation:** 

**[14400.00s] English:** You know, they made exclusive deals with, for example, with Joe Rogan, where the podcast would only be published on Spotify.  
**Translation:** 

**[14408.98s] English:** I personally think long term, what I would love to see for EGS, for Epic Game Store, is to not do any exclusivity.  
**Translation:** 

**[14419.00s] English:** Similar to what Spotify is doing now, even with Joe Rogan, they let go.  
**Translation:** Vocabulary: exclusivity: 独家发行

**[14422.78s] English:** It's wide open. And instead compete on the space of just the non-clunkiness of the interface.  
**Translation:** 

**[14433.66s] English:** Because the foundation of what Epic Game Store represents with 12% is just philosophically.  
**Translation:** Vocabulary: interface: 用户界面; philosophically: 从根本上

**[14443.74s] English:** So you're also competing on the sort of spiritual realm of what it stands for ethically.  
**Translation:** 

**[14449.16s] English:** That's also a really powerful way to win.  
**Translation:** Vocabulary: ethically: 道德上

**[14452.92s] English:** So now that there's enough number of people using Epic Game Store, like to drift away, to move away from exclusivity,  
**Translation:** 

**[14462.32s] English:** it's understandable that it's needed for the competition, for the underdog to enter the scene.  
**Translation:** Vocabulary: drift: 偏离; understandable: 可以理解

**[14468.00s] English:** But it goes against the sort of the freedom, the free spirit of choice that I think you represent in a lot of the decisions you've made,  
**Translation:** 

**[14476.20s] English:** which is making the games cross-platform.  
**Translation:** 

**[14479.58s] English:** And just, yes, giving freedom to the...  
**Translation:** 

**[14482.78s] English:** Developers giving freedom to the gamers to choose.  
**Translation:** 

**[14486.32s] English:** So in that way, I think exclusivity a little bit goes against that.  
**Translation:** 

**[14490.24s] English:** Well, here's the conundrum.  
**Translation:** Vocabulary: conundrum: 难题

**[14492.78s] English:** The exercise of soft power by all of the competing stores has made it intractable for almost any developer to offer a better price through the Epic Game Store than through Steam.  
**Translation:** 

**[14505.34s] English:** You can imagine that if the effect of Epic revenue sharing 12% to developers was that games just cost...  
**Translation:** Vocabulary: intractable: 无法解决

**[14512.78s] English:** 22% less on Epic Games...  
**Translation:** 

**[14515.16s] English:** Sorry, 18% less on Epic Game Store, that that would actually start...  
**Translation:** 

**[14520.00s] English:** to reshape consumer behavior significantly.  
**Translation:** 

**[14522.22s] English:** People would start coming here for the better deals.  
**Translation:** Vocabulary: reshape: 重塑

**[14524.74s] English:** But if, like, Steam giving developers nasty phone calls  
**Translation:** 

**[14527.98s] English:** and so on when they propose to do that  
**Translation:** 

**[14530.44s] English:** prevents developers from passing on savings to consumer,  
**Translation:** 

**[14535.16s] English:** then what's the mechanism that drives users  
**Translation:** 

**[14539.40s] English:** away from the incumbent store  
**Translation:** 

**[14541.38s] English:** to the store that offers a better deal?  
**Translation:** Vocabulary: incumbent: 现任的

**[14543.72s] English:** If basically developers are fearful  
**Translation:** 

**[14546.06s] English:** of competing on price through stores,  
**Translation:** 

**[14548.92s] English:** what can possibly be done to get a dominant store  
**Translation:** 

**[14553.24s] English:** with something like 90% of revenue share  
**Translation:** 

**[14557.06s] English:** among multi-publisher stores in line  
**Translation:** 

**[14563.50s] English:** so that a much, much smaller store can compete?  
**Translation:** 

**[14567.28s] English:** I think some answer is required there.  
**Translation:** 

**[14570.28s] English:** A better UI is great.  
**Translation:** 

**[14572.00s] English:** Steam is super polished.  
**Translation:** 

**[14573.06s] English:** Epic Games Store and Time will hopefully be as polished.  
**Translation:** Vocabulary: polished: 打磨得光滑

**[14577.88s] English:** How does that...  
**Translation:** 

**[14578.92s] English:** How does that overcome the fact  
**Translation:** 

**[14580.72s] English:** that your entire library over the past 15 years is there?  
**Translation:** 

**[14584.52s] English:** If developers have been afraid  
**Translation:** 

**[14586.24s] English:** to exercise their own economic interest,  
**Translation:** 

**[14588.26s] English:** because it's in a developer's interest  
**Translation:** 

**[14589.30s] English:** to sell on Epic and get, you know,  
**Translation:** 

**[14592.30s] English:** 18% more of the revenue,  
**Translation:** 

**[14595.72s] English:** you know, I think there's a real power to incumbents  
**Translation:** 

**[14599.08s] English:** that's very hard to overcome  
**Translation:** Vocabulary: incumbents: 连任者

**[14600.38s] English:** through just being there and being as good.  
**Translation:** 

**[14604.90s] English:** Ultimately, where I hope it converges to,  
**Translation:** Vocabulary: converges: 汇聚

**[14608.92s] English:** is less exclusivity  
**Translation:** 

**[14611.00s] English:** and where the competition can be the kind I love the most,  
**Translation:** Vocabulary: exclusivity: 排他性

**[14616.30s] English:** which is on the UI, on the experience,  
**Translation:** 

**[14622.22s] English:** on the just...  
**Translation:** 

**[14624.34s] English:** And then on the Steam side, on the 12%.  
**Translation:** 

**[14627.88s] English:** So it can go from 30% and start to support the developer  
**Translation:** 

**[14632.60s] English:** by lowering it from 30% closer to 12%.  
**Translation:** 

**[14635.94s] English:** So anyway, I'm a big supporter.  
**Translation:** Vocabulary: lowering: 降低

**[14638.92s] English:** And...  
**Translation:** 

**[14640.00s] English:** I don't like the criticism of Epic Games Store,  
**Translation:** 

**[14642.64s] English:** but I also have to say that I don't love the exclusivity,  
**Translation:** 

**[14645.76s] English:** but I understand.  
**Translation:** 

**[14647.28s] English:** I understand the reality of the world  
**Translation:** 

**[14649.30s] English:** is that you have to have some mechanism  
**Translation:** 

**[14651.28s] English:** to get people to switch,  
**Translation:** 

**[14654.76s] English:** or not to switch,  
**Translation:** 

**[14655.70s] English:** but to at least get some of their games  
**Translation:** 

**[14658.52s] English:** to try out, to experience,  
**Translation:** 

**[14661.36s] English:** to allocate some of their library to the underdog.  
**Translation:** 

**[14665.00s] English:** So I totally understand.  
**Translation:** Vocabulary: allocate: 分配; underdog: 弱者

**[14667.08s] English:** And hope the UI keeps improving.  
**Translation:** 

**[14670.36s] English:** Thanks.  
**Translation:** 

**[14672.00s] English:** One more bit on that exclusivity point  
**Translation:** 

**[14674.34s] English:** is that when we told Google  
**Translation:** 

**[14676.16s] English:** that we were going to launch Fortnite outside of Google Play  
**Translation:** 

**[14678.72s] English:** and go into competition with them,  
**Translation:** Vocabulary: fortnite: 堡垒之夜

**[14681.60s] English:** they viewed exclusivity as such a powerful competitive force  
**Translation:** 

**[14685.32s] English:** that they went around to the top 30 publishers  
**Translation:** 

**[14688.84s] English:** and paid out hundreds of millions of dollars  
**Translation:** 

**[14692.20s] English:** to them in order to agree  
**Translation:** 

**[14694.34s] English:** not to do exclusive deals with competitors.  
**Translation:** 

**[14699.36s] English:** And that was,  
**Translation:** 

**[14700.00s] English:** and that was one of the major pieces of evidence  
**Translation:** 

**[14711.74s] English:** on which the jury found their practices  
**Translation:** 

**[14713.56s] English:** to be illegal and anti-competitive.  
**Translation:** 

**[14716.58s] English:** And the one more data point on that,  
**Translation:** 

**[14718.04s] English:** you know, we talk about 30%,  
**Translation:** 

**[14719.16s] English:** and there's always a lot of people defending Steam.  
**Translation:** 

**[14721.52s] English:** Well, of course, they have more costs  
**Translation:** 

**[14722.54s] English:** because they have more features than Epic.  
**Translation:** 

**[14724.36s] English:** We have data on that that's very detailed.  
**Translation:** 

**[14727.40s] English:** The all-in cost of operating the Google Play Store,  
**Translation:** 

**[14730.00s] English:** stocking it, maintaining it, the software,  
**Translation:** 

**[14733.90s] English:** the entire ecosystem,  
**Translation:** Vocabulary: stocking: 储存

**[14736.08s] English:** is around 6% of revenue.  
**Translation:** 

**[14738.98s] English:** So, you know, in a competitive market,  
**Translation:** 

**[14742.26s] English:** would a company whose cost is 6%  
**Translation:** 

**[14744.16s] English:** be able to charge 30%?  
**Translation:** 

**[14747.98s] English:** Like, absolutely not.  
**Translation:** 

**[14749.58s] English:** And Apple's costs are similar.  
**Translation:** 

**[14750.76s] English:** Apple runs an even more efficient  
**Translation:** 

**[14752.06s] English:** and lean operation than Google,  
**Translation:** 

**[14753.62s] English:** so their costs are also likely in the range of 6% all-in.  
**Translation:** 

**[14757.86s] English:** They market up from 6%  
**Translation:** 

**[14759.80s] English:** to 6% in the future.  
**Translation:** 

**[14759.98s] English:** So, you know, we talk about 30%,  
**Translation:** 

**[14760.00s] English:** 30 percent like only a monopoly can do that yeah look at competitive businesses they have a margin  
**Translation:** 

**[14766.04s] English:** of a few percentage there the numbers there are strikingly uh supportive of just outright  
**Translation:** 

**[14773.70s] English:** anti-competitive market distortions okay what do you think is the future of the gaming industry  
**Translation:** 

**[14778.94s] English:** so we we've said to me a bunch of exciting stuff about indie developers so you know do uh uh what  
**Translation:** Vocabulary: distortions: 市场扭曲; indie: 独立开发者

**[14786.70s] English:** are called triple a video game companies so these big uh gaming companies do they have a future what  
**Translation:** 

**[14792.52s] English:** is their role how do you see like in the next 5 10 20 years the evolution of these big uh companies  
**Translation:** Vocabulary: triple: 三重

**[14800.24s] English:** and indie developers yeah there's one constant in gaming that i think the industry manages to  
**Translation:** 

**[14805.84s] English:** lose sight of from time to time astonishingly and and that's fun and people play games for fun yes  
**Translation:** Vocabulary: astonishingly: 令人惊讶地

**[14811.48s] English:** our whole job is to deliver fun and um when you look at a lot of the games that failed  
**Translation:** 

**[14816.70s] English:** they just didn't deliver fun or they didn't deliver fun in a manner that was nearly competitive  
**Translation:** 

**[14823.26s] English:** with the other sources of fun just in people's lives and so you know at a basic level we don't  
**Translation:** 

**[14830.34s] English:** need a terribly complicated theory to explain a lot of the malaise in the game industry there's  
**Translation:** Vocabulary: malaise: 身心不适

**[14835.08s] English:** been a degradation of the capabilities of a lot of publishers partly because of competition for  
**Translation:** 

**[14840.64s] English:** talent you know companies like with really vibrant game businesses like epic or riot or others are  
**Translation:** Vocabulary: degradation: 退化; vibrant: 充满活力

**[14846.70s] English:** hiring the best developers and accumulating them in big tech companies that are hiring the best  
**Translation:** 

**[14850.44s] English:** game developers because there's super talent there and so in some cases their companies aren't  
**Translation:** Vocabulary: accumulating: 聚集

**[14855.40s] English:** competing robustly or getting worse they're making games that are less fun and you know i think  
**Translation:** 

**[14860.22s] English:** everything else that's happened is kind of a sideshow to that um you know there's always  
**Translation:** Vocabulary: robustly: 强劲地; sideshow: 附带事件

**[14865.30s] English:** political drama and so on but i think they just the core is a failure to deliver fun and you know  
**Translation:** 

**[14870.40s] English:** the the nature of fun is changing it turns out that playing a game together with your friends  
**Translation:** 

**[14876.70s] English:** engaging way with voice chat is just way more fun than playing  
**Translation:** 

**[14880.00s] English:** playing a solitary game for the most part and there are exceptions to that um but i think we're  
**Translation:** Vocabulary: solitary: 独自的

**[14884.94s] English:** seeing much much more playtime shifting towards games you're playing together with your friends  
**Translation:** 

**[14889.08s] English:** and not just random internet strangers who happen to play that game too but the people actually  
**Translation:** Vocabulary: playtime: 游戏时间; shifting: 转移

**[14893.62s] English:** know in the real world um and that's certainly been the case with me and with almost everybody  
**Translation:** 

**[14898.44s] English:** i know who's playing fortnite or similar games and that has really significant effects in reshaping  
**Translation:** Vocabulary: fortnite: 堡垒之夜; reshaping: 重塑

**[14904.00s] English:** the whole game business because like a single player game if you have 20 people with 20 different  
**Translation:** 

**[14909.64s] English:** opinions of which game to play each one might buy a different single player game but in a multiplayer  
**Translation:** 

**[14914.42s] English:** game uh if there are 20 games out and each one might have their own completely individual  
**Translation:** 

**[14919.98s] English:** preference and each one we're independently choosing which game to play each one might buy  
**Translation:** Vocabulary: independently: 独立地

**[14924.32s] English:** a different game but uh if you know but they're all realizing that they want to play together  
**Translation:** 

**[14928.08s] English:** and so what players are doing increasingly is playing the a game they like and accept  
**Translation:** 

**[14935.12s] English:** together with their friends even if it's not the game that every one of them might  
**Translation:** 

**[14939.62s] English:** be preferring to play themselves like if you have uh and you know that's certainly the case in you  
**Translation:** 

**[14945.26s] English:** know different fortnite groups i play with from time to time it's like you know one player might  
**Translation:** 

**[14949.66s] English:** have been preferring to play cod one might have been preferring league of legends somebody else  
**Translation:** 

**[14953.94s] English:** something completely random but it's just so fun to play together we're doing that and that means  
**Translation:** 

**[14958.22s] English:** that there's really strong metcast law effect in which games which are able to attract a large  
**Translation:** 

**[14963.90s] English:** percentage of your friends are more able to attract you and not only attract but also  
**Translation:** 

**[14969.62s] English:** retain and so you know i think matthew ball's analysis of this over the years has really  
**Translation:** 

**[14975.60s] English:** documented the trend towards you know you can call it the metaverse or you can call it large scale  
**Translation:** 

**[14980.30s] English:** multiplayer social gaming he's really documented this trend and you know over the past year or so  
**Translation:** Vocabulary: metaverse: 元宇宙

**[14985.46s] English:** it's taken a really really strong turn towards increasing rate of change increasing numbers of  
**Translation:** 

**[14990.68s] English:** players coming to fortnite you know we hit an all-time high of 110 million monthly active users  
**Translation:** 

**[14996.08s] English:** a year ago and another  
**Translation:** 

**[14999.62s] English:** like  
**Translation:** 

**[15000.00s] English:** close to peak this time roblox is bigger than ever and you know this trend is players consolidating  
**Translation:** 

**[15005.64s] English:** into multiplayer experiences they play together and we're seeing another trend overlaid with that  
**Translation:** Vocabulary: consolidating: 合并; overlaid: 叠加

**[15010.22s] English:** which is like when an awesome single player game comes out or a small multiplayer game comes out  
**Translation:** 

**[15014.84s] English:** people often will like treat it as a vacation they'll go off and play that game for a while  
**Translation:** 

**[15017.98s] English:** then come back i think wukong was an awesome example of that a wonderful game from a brilliant  
**Translation:** 

**[15023.20s] English:** team in china they made a game that's like no western players had really seen that that type  
**Translation:** 

**[15028.82s] English:** of thing done before and it was awesome and it did well but most players play it for a while and  
**Translation:** 

**[15032.98s] English:** and move back on and that can be lucrative but a business that's building that kind of game is  
**Translation:** Vocabulary: lucrative: 有利可图

**[15037.94s] English:** going to have to build a new one every few years and uh and build a business around that while the  
**Translation:** 

**[15042.04s] English:** other games continue to accrete users but you know when you have a small a large number of gamers  
**Translation:** Vocabulary: accrete: 逐渐增加

**[15048.60s] English:** migrating to a small number of games the effect of that is increasing revenue for those games  
**Translation:** 

**[15055.48s] English:** increasing reinvestment um and you know there are things  
**Translation:** Vocabulary: migrating: 迁移; reinvestment: 再投资

**[15058.80s] English:** that epic can do with a team of thousands of people building fortnite  
**Translation:** 

**[15061.82s] English:** internally and um tens of thousands contributing to fortnite as independent creators um you know  
**Translation:** Vocabulary: fortnite: 堡垒之夜

**[15069.08s] English:** there are just things that can happen with that level of investment that can't happen in a smaller  
**Translation:** 

**[15072.62s] English:** game and so there's somewhat of a an increasing winner take all dynamic where the biggest games  
**Translation:** 

**[15077.92s] English:** reinvest more to make their games more fun to gain fun at a faster rate than other games and uh  
**Translation:** 

**[15082.54s] English:** you know the industry is changing around that and you know so i think the the lesson for the game  
**Translation:** Vocabulary: reinvest: 重新投资

**[15087.50s] English:** industry now is that they're  
**Translation:** 

**[15088.80s] English:** really two big opportunities being pursued there's big games or games that have the potential to be  
**Translation:** 

**[15093.92s] English:** really big multiplayer experiences that keep players players around you know indefinitely  
**Translation:** 

**[15098.02s] English:** for very long periods of time and then they're just really good single player and small scale  
**Translation:** Vocabulary: indefinitely: 无期限

**[15103.52s] English:** games that people are taking a break from their big games for and you know the trend there is  
**Translation:** 

**[15108.06s] English:** going to be towards efficiently developing those games you can't build one of those games with a  
**Translation:** 

**[15112.22s] English:** 300 million dollar budget but if you can do it with a 40 million dollar budget you can make a  
**Translation:** 

**[15116.34s] English:** lot of money so i think that's the main reason why i think that's the main reason why i think  
**Translation:** 

**[15118.80s] English:** that's the main reason why i think that's the main reason why i think that's the main reason  
**Translation:** 

**[15120.00s] English:** it creates a rather bleak outlook for a lot of the category of  
**Translation:** Vocabulary: bleak: 悲观

**[15124.62s] English:** single-player games that don't have a huge audience to reach.  
**Translation:** 

**[15130.42s] English:** But this is just one of the trends of restructuring  
**Translation:** Vocabulary: restructuring: 结构调整

**[15133.02s] English:** the business around the technology and changes of the day.  
**Translation:** 

**[15137.20s] English:** Okay, this is going to be a ridiculous question, but aside from the  
**Translation:** 

**[15141.02s] English:** games you've created, what are some of the greatest video games  
**Translation:** 

**[15144.94s] English:** ever created to you? What video games have been like  
**Translation:** 

**[15150.00s] English:** either impactful to you in your life, or maybe you've seen  
**Translation:** 

**[15154.36s] English:** created, and you're like, huh, that's a beautiful art piece.  
**Translation:** 

**[15158.60s] English:** It could be in a totally different realm. Obviously, for me,  
**Translation:** 

**[15162.06s] English:** I return often to the single-player domain of role-playing  
**Translation:** 

**[15166.34s] English:** games, of the Elder Scrolls series, Skyrim. That was like a world  
**Translation:** 

**[15170.30s] English:** that they created. A recent game, Baldur's Gate 3,  
**Translation:** Vocabulary: scrolls: 卷轴

**[15174.58s] English:** that was a really incredible piece of work and art,  
**Translation:** 

**[15177.60s] English:** and doing a lot of innovative stuff, again in the single-player  
**Translation:** 

**[15181.88s] English:** domain. Is there games like that outside the ones you've  
**Translation:** 

**[15185.80s] English:** created? I'm most impressed with the games that have  
**Translation:** 

**[15189.24s] English:** created what appears to be a full, living, breathing world.  
**Translation:** 

**[15196.40s] English:** Games that give you the sense that  
**Translation:** 

**[15197.90s] English:** you're just a part of it, and there's a lot more happening, and  
**Translation:** 

**[15201.32s] English:** there's always more.  
**Translation:** 

**[15205.40s] English:** It gives you the sense that you go,  
**Translation:** 

**[15207.60s] English:** anywhere, and do anything. Even though these games really do have  
**Translation:** 

**[15210.56s] English:** finite limitations, and there are places you can't go, really  
**Translation:** 

**[15213.22s] English:** creating that sense of wonder is just a magical thing.  
**Translation:** Vocabulary: finite: 有限的

**[15217.78s] English:** Zelda Breath of the Wild, Skyrim, Red Dead Redemption.  
**Translation:** 

**[15221.94s] English:** Red Dead is great, yeah. There's an entire ecology simulator in there.  
**Translation:** Vocabulary: redemption: 救赎; simulator: 模拟器

**[15226.64s] English:** I have a high school classmate that got into studying river ecology,  
**Translation:** 

**[15229.72s] English:** and he was commenting on, this is one of the very few games that's  
**Translation:** 

**[15233.52s] English:** hydrologically sound. They actually went to the effort,  
**Translation:** 

**[15237.60s] English:** of shaping the rivers to follow, like,  
**Translation:** Vocabulary: hydrologically: 水文上

**[15240.00s] English:** erosion dynamics and so on is the attention to detail and there's something there that's big and  
**Translation:** 

**[15245.44s] English:** it's been funny during through the industry like i last designed a game in 1992 i'm not a game  
**Translation:** 

**[15252.82s] English:** designer um you have a very open-minded here that like the best game genre that will ever exist has  
**Translation:** 

**[15260.68s] English:** not yet been invented um and as we get more technological capabilities um and creatives  
**Translation:** Vocabulary: creatives: 创意人员

**[15268.38s] English:** people use that uh to and you know hopefully empowered by higher productivity tools and so  
**Translation:** 

**[15273.48s] English:** on that we'll see more and more cool things emerge that we'd never dreamed possible  
**Translation:** Vocabulary: empowered: 赋能

**[15276.54s] English:** and you know the idea of a world simulator is actually really interesting there um it's been  
**Translation:** 

**[15282.16s] English:** tried a lot it's you know usually extremely slow and expensive to create but over time maybe we'll  
**Translation:** 

**[15286.84s] English:** get better at that and that will be a thing too you said so many interesting things there  
**Translation:** 

**[15290.78s] English:** new city builders yeah civilization that's just mind-boggling they build a game with that depth  
**Translation:** 

**[15296.80s] English:** that can evolve so  
**Translation:** 

**[15298.38s] English:** on your actions to do that that scale of world but to where you can step into it  
**Translation:** 

**[15305.46s] English:** and be in it you know i think red dead is a great example but to do red dead redemption in a  
**Translation:** 

**[15313.04s] English:** in a way where you can walk around with friends at a large scale  
**Translation:** 

**[15318.60s] English:** and uh and i guess what you have given so many years to is creating the tools that enable  
**Translation:** 

**[15327.22s] English:** the artists to  
**Translation:** 

**[15328.38s] English:** give that attention to detail that red dead does on those on several of the things  
**Translation:** 

**[15333.52s] English:** and once you do there's something magical about that  
**Translation:** 

**[15337.16s] English:** but once you give the that attention to detail like i don't know what what it is but the love  
**Translation:** 

**[15345.30s] English:** of the artist comes through somehow and you could feel the care that they put into it that's right  
**Translation:** 

**[15352.44s] English:** the best games have a soul you can really sense it um yeah like call of duty has a very different  
**Translation:** 

**[15357.00s] English:** soul than fortnite and it's just kind of like a different soul than fortnite and it's just kind of  
**Translation:** Vocabulary: fortnite: 堡垒之夜

**[15358.38s] English:** exudes not only in what you  
**Translation:** 

**[15360.00s] English:** see in the game but also in how players interact with it and interact with each other online  
**Translation:** Vocabulary: exudes: 散发

**[15364.06s] English:** that's a really fascinating thing i wish would be studied more  
**Translation:** 

**[15367.28s] English:** i think we talked about the soul on several fronts right i wish it would be studied more  
**Translation:** 

**[15374.06s] English:** yeah yeah these little game design decisions the designers make um have a profound impact on what  
**Translation:** 

**[15382.32s] English:** players think of the game and see in the game you know fortnite battle royale always had a sense of  
**Translation:** Vocabulary: designers: 设计师; profound: 深远

**[15386.96s] English:** mystery so you're on this island but you're not sure exactly what's happening here there are all  
**Translation:** 

**[15390.24s] English:** these houses they're abandoned why and you know i'm not the secret holder i'm i'm you know i'm  
**Translation:** 

**[15397.18s] English:** not on the design team i experienced fortnite as a player but it really exudes a lot of that and  
**Translation:** 

**[15402.14s] English:** a good spiritedness as well because even when you're eliminated in fortnite you know there's  
**Translation:** Vocabulary: spiritedness: 精神风貌

**[15407.28s] English:** not like blood spurts and there's not good jibs you're just you know teleported out of the  
**Translation:** 

**[15412.20s] English:** simulation and often you know you end up losing the game in a way that's hilarious enough that  
**Translation:** 

**[15416.94s] English:** like actually you're laughing at it or you're like respect to that player who just won because  
**Translation:** 

**[15421.34s] English:** that was clever um and you know it creates a very different dynamic than these other games where  
**Translation:** 

**[15425.94s] English:** players tend to be very very positive towards each other um one of the things i like to do in  
**Translation:** 

**[15430.66s] English:** fortnite just to kind of gauge how the game is going is i play fill squads a match made with  
**Translation:** Vocabulary: gauge: 评估

**[15436.28s] English:** you know three other random players and play a game together sometimes they have voice chat  
**Translation:** 

**[15440.22s] English:** sometimes they don't and uh you know back when our matchmaking regions were bigger i learned a  
**Translation:** Vocabulary: matchmaking: 匹配交友

**[15444.68s] English:** little bit of like battlefield spanish so i could speak  
**Translation:** 

**[15446.94s] English:** to people who are down as far south as a you know mexico city and you know the the positivity of  
**Translation:** Vocabulary: battlefield: 战场; positivity: 积极

**[15453.84s] English:** the interactions there uh among every kind of person you might ever meet online were really  
**Translation:** 

**[15458.76s] English:** quite impressive and completely unlike what you would see in a game like call of duty where it's  
**Translation:** 

**[15462.38s] English:** always you know yeah everybody's got to be an edgelord uh i love online gaming culture  
**Translation:** 

**[15472.18s] English:** i have to ask you because it's kind of like one of the legendary games is grand  
**Translation:** Vocabulary: edgelord: 边缘人

**[15476.94s] English:** theft auto speaking of the worlds that are just like  
**Translation:** 

**[15480.00s] English:** i mean that's a whole it's that's its own thing right that's uh that world the characters the  
**Translation:** 

**[15486.70s] English:** style the edginess all of that but the the interesting thing about grand theft auto 6  
**Translation:** 

**[15492.34s] English:** to me that i want to ask you about is they took forever it's the six month thing that you mentioned  
**Translation:** Vocabulary: edginess: 尖锐感

**[15496.78s] English:** before you know there's some games like that just take years to bring to the conclusion  
**Translation:** 

**[15503.08s] English:** what can you say about that process that you know you eventually were able to  
**Translation:** 

**[15510.86s] English:** take unreal to completion if you were to look from the outside  
**Translation:** 

**[15515.92s] English:** why does it take grand theft auto that long or other um companies uh to to take the games to  
**Translation:** 

**[15525.20s] English:** conclusion and what um i mean just insight into what that process is like making games is very  
**Translation:** 

**[15533.06s] English:** hard and um especially when you're pushing the boundaries of something um you know with grand  
**Translation:** 

**[15539.12s] English:** theft auto it's just the realism and feeling that you're in this huge city um and anything can  
**Translation:** 

**[15544.72s] English:** happen and it's all living and breathing and you're just a part of it the level with which  
**Translation:** 

**[15549.92s] English:** rockstar has brought quality to that genre is astonishing and when you're building something  
**Translation:** 

**[15554.72s] English:** at a level of quality and detail that's never been achieved before you can't predict how long  
**Translation:** Vocabulary: astonishing: 令人惊讶; rockstar: 摇滚明星

**[15559.62s] English:** it will take uh whatever problems you're solving today  
**Translation:** 

**[15563.06s] English:** to get to you know the next iteration of quality on it you you don't know what new problems that  
**Translation:** Vocabulary: iteration: 迭代

**[15569.10s] English:** will unlock and often you fix one thing and that make it super realistic and that just highlights  
**Translation:** 

**[15573.80s] English:** the unrealism of other things that you need to need to fix um i think the other thing that always  
**Translation:** 

**[15578.96s] English:** comes to mind is that uh shipping a game is easy if you don't have a high quality standard uh we  
**Translation:** 

**[15586.66s] English:** also won't have much success what we've seen from rockstar is they take a long time but they ship  
**Translation:** 

**[15591.68s] English:** amazing games and uh  
**Translation:** 

**[15593.06s] English:** it's worth it in the end right a bad game is bad forever a late good game is eventually is released  
**Translation:** 

**[15599.34s] English:** and it's good  
**Translation:** 

**[15600.00s] English:** do you ever feel like rocks has a good example of that the pressure of delivering quality you  
**Translation:** 

**[15608.24s] English:** you know epic has not missed recently that i'm aware of in terms of delivering quality  
**Translation:** 

**[15613.88s] English:** you feel the pressure of that that you're not allowed misses we certainly do we uh  
**Translation:** 

**[15621.38s] English:** everybody's often working very much to the last minute to make something excellent and um it's  
**Translation:** 

**[15627.98s] English:** really hard with these fast delivery time frames because you really have to get a lot of stuff up  
**Translation:** 

**[15633.20s] English:** and running before you can judge it like a new fortnight season holistically um you know it's  
**Translation:** 

**[15638.04s] English:** not until like the last month or so that you really know what you're you've built and you  
**Translation:** Vocabulary: fortnight: 两个星期; holistically: 整体地

**[15642.34s] English:** really understand it and if any late breaking problems emerge in like balance or anything else  
**Translation:** 

**[15647.26s] English:** it's is usually towards the end and that usually leads to a rapid push to  
**Translation:** 

**[15651.32s] English:** to fix it and then other lessons you can only learn live um and uh you know from experience  
**Translation:** 

**[15657.84s] English:** and  
**Translation:** 

**[15657.98s] English:** that means uh accepting a game that like it's a live experience and it's also an experiment and  
**Translation:** 

**[15664.48s] English:** it's going to continually be improving at any time there's some things that some people don't like  
**Translation:** 

**[15668.70s] English:** and uh you learn from it and you uh improve it and you move on let me ask you a big philosophical  
**Translation:** 

**[15674.02s] English:** question so you've created these gigantic worlds that bring so much fun to humanity  
**Translation:** Vocabulary: gigantic: 巨大的; philosophical: 哲学的

**[15681.96s] English:** now but you also get to learn about humanity what gives you hope  
**Translation:** 

**[15686.32s] English:** about a  
**Translation:** 

**[15687.98s] English:** about us humans about the future of humans of the future of humanity you know i see two  
**Translation:** 

**[15695.46s] English:** contrasting worlds that you know have been brought about in the digital age one is the world of  
**Translation:** 

**[15701.04s] English:** social networks and people typing at each other and just you know massive negativity and politics  
**Translation:** 

**[15706.96s] English:** and you know hucksterism and uh you know engagement curation by engagement often promoting negativity  
**Translation:** Vocabulary: curation: 内容筛选; hucksterism: 欺诈销售; negativity: 负面情绪

**[15717.98s] English:** and toxicity uh  
**Translation:** 

**[15720.00s] English:** That's a harsh world that I think is a step backwards in many ways.  
**Translation:** Vocabulary: backwards: 倒退; toxicity: 毒性

**[15722.80s] English:** I think the foundation of the world is actually a little bit shaky  
**Translation:** 

**[15725.96s] English:** because of just the social dynamic that those platforms have brought on.  
**Translation:** 

**[15731.30s] English:** But then I compare that with the good-spiritedness  
**Translation:** 

**[15733.22s] English:** of what's happening online when you're connected to real people,  
**Translation:** 

**[15736.56s] English:** like actually playing Fortnite,  
**Translation:** 

**[15737.96s] English:** playing Fortnite fill squads with people you've never met before,  
**Translation:** Vocabulary: fortnite: 王者荣耀

**[15740.32s] English:** never talked to,  
**Translation:** 

**[15741.14s] English:** and just judging what human connections develop there  
**Translation:** 

**[15744.52s] English:** and whether they're positive.  
**Translation:** 

**[15745.40s] English:** I found those to be really, really excellent and endearing.  
**Translation:** Vocabulary: endearing: 令人喜爱的

**[15748.72s] English:** I think the lesson from all of that is that humans talking to humans  
**Translation:** 

**[15753.56s] English:** and being together in a simulated world,  
**Translation:** Vocabulary: simulated: 虚拟

**[15757.02s] English:** the real world or virtual world,  
**Translation:** 

**[15759.34s] English:** is a naturally empathetic medium,  
**Translation:** Vocabulary: empathetic: 富有同情心的

**[15762.24s] English:** which naturally leads to bonding.  
**Translation:** 

**[15764.66s] English:** And though conflict sometimes occurs,  
**Translation:** 

**[15766.28s] English:** it's just generally so much more promoting of our social norms  
**Translation:** 

**[15769.84s] English:** and good interactions between people and positivity promoting,  
**Translation:** Vocabulary: positivity: 积极心态

**[15774.22s] English:** whereas kind of the typing angry messages thing at each other  
**Translation:** 

**[15778.48s] English:** is a little bit more of a,  
**Translation:** 

**[15778.70s] English:** you know,  
**Translation:** 

**[15778.72s] English:** as a self-reinforcing negative dynamic that's negative.  
**Translation:** 

**[15783.00s] English:** And I think you look at social media  
**Translation:** 

**[15786.16s] English:** and you look at gaming that is increasingly social,  
**Translation:** 

**[15788.72s] English:** and I couldn't see a bigger divide between any two mediums  
**Translation:** 

**[15791.30s] English:** as I see there in terms of the actual social dynamics.  
**Translation:** 

**[15794.60s] English:** One super positive, one super toxic at times.  
**Translation:** 

**[15798.92s] English:** Yeah, that's actually really the text-based medium.  
**Translation:** 

**[15803.20s] English:** Now that could even be around gaming.  
**Translation:** 

**[15804.94s] English:** You could look at discourse that could be a real toxic in text,  
**Translation:** 

**[15808.00s] English:** but you,  
**Translation:** 

**[15808.70s] English:** you place humans together in the real world here in the room.  
**Translation:** 

**[15812.66s] English:** I literally have never,  
**Translation:** 

**[15813.82s] English:** like I very rarely see humans not get along in the physical space.  
**Translation:** 

**[15819.72s] English:** And the degree to which you can create a digital space,  
**Translation:** 

**[15824.18s] English:** like a metaverse type of space,  
**Translation:** Vocabulary: metaverse: 元宇宙

**[15826.12s] English:** where it's sufficiently immersive,  
**Translation:** 

**[15828.88s] English:** where you're,  
**Translation:** Vocabulary: immersive: 身临其境; sufficiently: 足够

**[15829.42s] English:** you feel the other person,  
**Translation:** 

**[15831.60s] English:** the empathy comes out.  
**Translation:** Vocabulary: empathy: 共情

**[15833.52s] English:** And then the joy that's derived from the empathy comes out.  
**Translation:** 

**[15837.00s] English:** And it's just a reminder that,  
**Translation:** 

**[15838.68s] English:** humans like.  
**Translation:** 

**[15840.00s] English:** I don't know, the humans are good and they want to see the good in others.  
**Translation:** 

**[15844.78s] English:** They want to share the goodness.  
**Translation:** 

**[15846.96s] English:** And then, you know, like when they get in that group together, there's love there.  
**Translation:** 

**[15852.30s] English:** Now, they might talk shit about some other group.  
**Translation:** 

**[15856.16s] English:** This is the dark side of humans.  
**Translation:** 

**[15859.08s] English:** But together, in terms of the dynamics of that group, is joyful.  
**Translation:** 

**[15863.42s] English:** So, yeah, that gives me hope as well.  
**Translation:** 

**[15865.42s] English:** And the more degree which we can create those worlds online that make it super easy for us to connect in that empathic way, the better.  
**Translation:** 

**[15874.28s] English:** And I am grateful that you are pushing the boundaries of what's possible in creating such worlds.  
**Translation:** Vocabulary: empathic: 共情的

**[15881.00s] English:** And I'm grateful that you would talk with me today, Tim.  
**Translation:** 

**[15883.32s] English:** This is amazing.  
**Translation:** 

**[15884.24s] English:** It's an honor to talk to you.  
**Translation:** 

**[15886.32s] English:** Oh, thank you very much.  
**Translation:** 

**[15887.30s] English:** It's been fun.  
**Translation:** 

**[15888.90s] English:** Thanks for listening to this conversation with Tim Sweeney.  
**Translation:** 

**[15891.40s] English:** To support this podcast, please check out our sponsor in the description.  
**Translation:** 

**[15894.84s] English:** And now.  
**Translation:** 

**[15895.60s] English:** Let me leave you some words from Benjamin Franklin.  
**Translation:** 

**[15899.76s] English:** We do not stop playing because we grow old.  
**Translation:** 

**[15903.46s] English:** We grow old because we stop playing.  
**Translation:** 

**[15907.22s] English:** Thank you for listening.  
**Translation:** 

**[15908.58s] English:** I hope to see you next time.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
