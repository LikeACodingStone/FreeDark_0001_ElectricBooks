# Podcast vocabulary notes
Source file: Lex Fridman - Chris Lattner： The Future of Computing and Programming Languages ｜ Lex Fridman Podcast #131.opus

**[0.00s] English:** The following is a conversation with Chris Lattner, his second time on the podcast.  
**Translation:** 

**[4.68s] English:** He's one of the most brilliant engineers in modern computing, having created LLVM Compiler  
**Translation:** Vocabulary: computing: 计算

**[9.88s] English:** Infrastructure Project, the Clang Compiler, the Swift Programming Language, a lot of key  
**Translation:** 

**[15.40s] English:** contributions to TensorFlow and TPUs as part of Google.  
**Translation:** Vocabulary: clang: clang 编译器

**[19.08s] English:** He served as Vice President of Autopilot Software at Tesla, was a software innovator and leader  
**Translation:** 

**[25.22s] English:** at Apple, and now is at Sci-5 as Senior Vice President of Platform Engineering, looking  
**Translation:** Vocabulary: innovator: 创新者

**[31.18s] English:** to revolutionize chip design to make it faster, better, and cheaper.  
**Translation:** 

**[36.50s] English:** Quick mention of each sponsor, followed by some thoughts related to the episode.  
**Translation:** Vocabulary: revolutionize: 彻底改变

**[40.84s] English:** First sponsor is Blinkist, an app that summarizes key ideas from thousands of books.  
**Translation:** 

**[45.28s] English:** I use it almost every day to learn new things or to pick which books I want to read or listen  
**Translation:** Vocabulary: blinkist: 闪电速读; summarizes: 总结

**[51.02s] English:** to next.  
**Translation:** 

**[51.98s] English:** Second is Neuro, the maker of functional sugar.  
**Translation:** 

**[55.22s] English:** It's a sugar-free gum and mints that I use to supercharge my mind with caffeine,  
**Translation:** 

**[59.28s] English:** L-theanine, and B vitamins.  
**Translation:** Vocabulary: caffeine: 咖啡因; supercharge: 提神; vitamins: 维生素

**[61.30s] English:** Third is Masterclass, online courses from the best people in the world on each of the  
**Translation:** 

**[67.32s] English:** topics covered, from rockets, to game design, to poker, to writing, and to guitar.  
**Translation:** Vocabulary: masterclass: 大师课程; poker: 扑克

**[73.90s] English:** And finally, Cash App, the app I use to send money to friends for food, drinks, and unfortunately  
**Translation:** 

**[79.98s] English:** lost bets.  
**Translation:** 

**[81.44s] English:** Please check out the sponsors in the description to get a discount and to subscribe.  
**Translation:** 

**[85.22s] English:** And as always, thanks for watching, and I'll see you in the next video.  
**Translation:** Vocabulary: sponsors: 赞助商; subscribe: 订阅

**[115.22s] English:** Looks at me, it makes me feel like I might be someone special, it can be truly inspiring.  
**Translation:** 

**[120.00s] English:** that's a lesson for educators the weird kid in the corner with a dream is someone who might need  
**Translation:** Vocabulary: educators: 教育者

**[126.80s] English:** your love and support in order for that dream to flourish if you enjoy this thing subscribe on  
**Translation:** 

**[132.58s] English:** youtube review it with five stars on apple podcast follow on spotify support on patreon or connect  
**Translation:** Vocabulary: flourish: 繁荣成长

**[138.26s] English:** with me on twitter at lex friedman and now here's my conversation with chris latner what are the  
**Translation:** 

**[146.54s] English:** strongest qualities of steve jobs elon musk and the great and powerful jeff dean since you've  
**Translation:** Vocabulary: friedman: 弗里德曼

**[153.48s] English:** gotten a chance to work with each you're starting with an easy question there um these are three  
**Translation:** 

**[159.28s] English:** very different people i guess you could do maybe a pairwise comparison between them instead of a  
**Translation:** Vocabulary: pairwise: 一对一

**[164.84s] English:** group comparison so if you look at steve jobs and elon i worked a lot more with elon than i did with  
**Translation:** 

**[169.80s] English:** steve um they have a lot of commonality they're both um visionary in their own way they're both  
**Translation:** Vocabulary: visionary: 有远见的人

**[176.54s] English:** their own way um my sense is steve is much more human factor focused where elon is more technology  
**Translation:** 

**[183.78s] English:** focused what does human factor mean steve's trying to build things that feel good that people love  
**Translation:** 

**[189.28s] English:** that affect people's lives how they live he's looking into into the future a little bit in  
**Translation:** 

**[194.76s] English:** terms of um what people want um where i think that elon focuses more on uh learning how exponentials  
**Translation:** Vocabulary: exponentials: 指数

**[201.24s] English:** work and predicting the development of those steve worked with a lot of engineers that was  
**Translation:** 

**[206.52s] English:** one of the things that are reading the biography and how how can a designer essentially talk to  
**Translation:** 

**[212.58s] English:** engineers and like get their respect i think so i did not work very closely with steve i'm not an  
**Translation:** 

**[218.12s] English:** expert at all my sense is that he uh pushed people really hard but then when he got an explanation  
**Translation:** 

**[223.14s] English:** that made sense to him then he would let go and he did actually have a lot of respect for engineering  
**Translation:** 

**[228.86s] English:** and but he also knew when to push and you know when you can read people well you can know when  
**Translation:** 

**[236.52s] English:** and when you can get a little bit more out of them and i think he was very good at that  
**Translation:** 

**[240.00s] English:** i mean if you if you compare the other the other folks so jeff dean right jeff dean's an amazing  
**Translation:** 

**[245.92s] English:** guy he's super smart um as as are the other guys um jeff is a really really really nice guy  
**Translation:** 

**[253.06s] English:** well-meaning he's a classic googler he uh wants people to be happy he combines it with brilliance  
**Translation:** Vocabulary: brilliance: 卓越智慧

**[259.70s] English:** so he can pull people together in a really great way he's definitely not a ceo type i don't think  
**Translation:** 

**[265.00s] English:** he'd even want to be that do you know if he still programs oh yeah he definitely programs jeff is an  
**Translation:** 

**[271.00s] English:** amazing engineer today right and that has never changed so um it's really hard to compare jeff to  
**Translation:** 

**[276.34s] English:** to either of those two um he uh i think that jeff leads through technology and building it himself  
**Translation:** 

**[284.72s] English:** and then pulling people in and inspiring them and so i think that that's um one of the amazing  
**Translation:** 

**[289.76s] English:** things about jeff but each of these people you know what their pros and cons all are really  
**Translation:** 

**[294.42s] English:** inspirational  
**Translation:** 

**[295.00s] English:** and have achieved amazing things yes it's been a it's been i've been very fortunate to get to work  
**Translation:** Vocabulary: inspirational: 鼓舞人心的

**[299.94s] English:** with these guys for yourself you've led large teams you've done so many incredible difficult  
**Translation:** 

**[306.60s] English:** technical challenges is there something you've picked up from them about how to lead yeah well  
**Translation:** 

**[312.96s] English:** so i mean i think leadership is really hard it really depends on what you're looking for there  
**Translation:** 

**[316.14s] English:** um i think you really need to know what you're talking about so being grounded on the product  
**Translation:** 

**[322.12s] English:** on the technology on the business on the mission  
**Translation:** 

**[325.00s] English:** is really important being uh understanding what people are looking for why they're there  
**Translation:** 

**[330.54s] English:** one of the most amazing things about tesla is the unifying vision right people are there because  
**Translation:** 

**[335.36s] English:** they believe in clean energy and electrification all these kinds of things um uh the others is to  
**Translation:** Vocabulary: electrification: 电气化; unifying: 统一的

**[342.78s] English:** understand what really motivates people how to get the best people how to how to build a plan  
**Translation:** 

**[347.36s] English:** that actually can be executed right there's so many different aspects of leadership and it really  
**Translation:** Vocabulary: motivates: 激励人们

**[350.82s] English:** depends on the time the place the problems you know you know the people that are involved in the  
**Translation:** 

**[355.00s] English:** world the people that are involved in the world they're part of it you know there's a lot of  
**Translation:** 

**[356.62s] English:** issues that don't need to be solved and so if you focus on the right things and prioritize well  
**Translation:** 

**[360.00s] English:** can really help move things two interesting things you mentioned one is you really have  
**Translation:** Vocabulary: prioritize: 优先排序

**[364.26s] English:** to know what you're talking about how you've uh you've worked on a lot of very challenging  
**Translation:** 

**[370.82s] English:** technical things sure so i kind of assume you were born uh technically savvy but assuming that's not  
**Translation:** Vocabulary: savvy: 精通技术

**[379.52s] English:** the case uh how did how did you develop technical expertise like even at google you worked on i  
**Translation:** 

**[387.50s] English:** don't know how many projects but really challenging very varied compilers tpus hardware cloud stuff  
**Translation:** 

**[394.54s] English:** bunch of different things um the thing that i've become comfortable as i've more comfortable with  
**Translation:** 

**[399.54s] English:** as i've uh gained experience is uh being okay with not knowing and so a major part of leadership is  
**Translation:** 

**[408.00s] English:** actually it's not about having the right answer it's about getting the right answer and so if  
**Translation:** 

**[413.16s] English:** you're working in a team of amazing people right and many of these places  
**Translation:** 

**[417.50s] English:** many of these companies all have amazing people it's the question of how do you get people  
**Translation:** 

**[421.58s] English:** together how do you get how do you build trust how do you get people to open up how do you people  
**Translation:** 

**[426.48s] English:** get people to you know be vulnerable sometimes with an idea that maybe isn't good enough but  
**Translation:** 

**[431.84s] English:** it's the start of something beautiful how do you um how do you provide an environment where you're  
**Translation:** 

**[437.82s] English:** not just like top down thou shalt do the thing that i tell you to do right but you're encouraging  
**Translation:** 

**[441.74s] English:** people to be part of the solution and uh and providing a safe space where if you're not doing  
**Translation:** Vocabulary: shalt: 必须

**[447.34s] English:** the right thing you're not doing the right thing you're not doing the right thing you're not doing  
**Translation:** 

**[447.48s] English:** the right thing you're not doing the right thing you're not doing the right thing you're not doing the  
**Translation:** 

**[447.50s] English:** thing they're willing to tell you about it right so you're asking dumb questions yeah dumb questions  
**Translation:** 

**[452.18s] English:** are my specialty yeah well i so i've been in the hardware realm recently and i don't know  
**Translation:** Vocabulary: specialty: 专长

**[456.76s] English:** much at all about how chips are designed i know a lot about using them i know some of the principles  
**Translation:** 

**[460.88s] English:** and the ars technica level of this but it turns out it turns out that if you ask a lot of dumb  
**Translation:** Vocabulary: technica: 技术实现

**[466.78s] English:** questions you get smarter really really quick and when you're surrounded by people that want to teach  
**Translation:** 

**[470.94s] English:** and learn that themselves it can be a beautiful thing so let's talk about programming languages  
**Translation:** 

**[477.86s] English:** if it's okay at the highest absurd  
**Translation:** 

**[480.00s] English:** philosophical level because i don't get romantic on me lex i will forever get romantic and uh  
**Translation:** Vocabulary: philosophical: 哲学的

**[487.34s] English:** torture i apologize uh why do programming languages even matter okay well thank you very much you're  
**Translation:** 

**[495.84s] English:** saying why should why should you care about any one programming language or why do you why do we  
**Translation:** 

**[499.38s] English:** care about programming computers or no why why do we why do we care about programming language  
**Translation:** 

**[504.66s] English:** design creating effective programming languages uh choosing a you know one programming languages  
**Translation:** 

**[512.52s] English:** versus another programming language why we keep struggling and improving through the evolution  
**Translation:** 

**[518.64s] English:** of these programming languages sure okay so so i mean i think you have to come back to what are  
**Translation:** 

**[522.56s] English:** we trying to do here right so we have these these uh beasts called computers that are very good at  
**Translation:** 

**[527.80s] English:** specific kinds of things and we think it's useful to have them do it for us right uh now you have  
**Translation:** 

**[533.02s] English:** this question of how best to  
**Translation:** 

**[534.66s] English:** express that because you have a human brain still that has an idea in its head and you want to  
**Translation:** 

**[539.20s] English:** achieve something right so well there's lots of ways of doing this you can go directly to the  
**Translation:** 

**[544.46s] English:** machine and speak assembly language and then you can express directly what the computer understands  
**Translation:** 

**[548.64s] English:** that's fine um you can then have higher and higher and higher levels of abstraction up until  
**Translation:** 

**[553.94s] English:** machine learning and you're designing a neural net to do the work for you um the question is where  
**Translation:** Vocabulary: abstraction: 抽象; neural: 神经

**[558.96s] English:** where along this way do you want to stop and what benefits do you get out of doing so and so  
**Translation:** 

**[563.88s] English:** programming language is a very good question and i think it's a good question and i think it's a  
**Translation:** 

**[564.64s] English:** in general you have c you have fortran and java and ada pascal swift you have lots of different  
**Translation:** 

**[572.10s] English:** things um they'll have different trade-offs and they're tackling different parts of the problems  
**Translation:** Vocabulary: pascal: 帕斯卡; tackling: 应对

**[576.26s] English:** now one of the things that most programming languages do is they're trying to make it so  
**Translation:** 

**[580.94s] English:** that you have pretty basic things like portability across different hardware so you've got i'm going  
**Translation:** Vocabulary: portability: 设备兼容性

**[586.34s] English:** to run on an intel pc i'm going to run a wrist 5 pc i'm going to run on uh arm phone or something  
**Translation:** 

**[591.90s] English:** like that fine um i want to write one program and have it do it for me so i'm going to run it on an  
**Translation:** 

**[594.64s] English:** intel pc and have it portable and this is something the assembly doesn't do now when you  
**Translation:** 

**[598.16s] English:** start looking at the space of programming  
**Translation:** 

**[600.00s] English:** languages this is where i think it's fun because programming languages all have trade-offs and most  
**Translation:** 

**[606.54s] English:** people will walk up to them and they look at the surface level of syntax and say oh i like curly  
**Translation:** Vocabulary: syntax: 语法规则

**[611.94s] English:** braces or i like tabs or i like you know semicolons or not or whatever right subjective fairly  
**Translation:** 

**[618.64s] English:** subjective very shallow things but programming languages when done right can actually be very  
**Translation:** Vocabulary: braces: 花括号; semicolons: 分号

**[623.92s] English:** powerful and the the benefit they bring is expression okay and if you look at programming  
**Translation:** 

**[632.08s] English:** languages there's really kind of two different levels to them one is the down in the dirt nuts  
**Translation:** 

**[637.44s] English:** and bolts of how do you get the computer to be efficient stuff like that how they work type  
**Translation:** 

**[640.82s] English:** systems compiler stuff things like that the other is the ui and the ui for programming language is  
**Translation:** 

**[647.34s] English:** really a design problem and a lot of people don't think about it that way and the ui you mean all  
**Translation:** 

**[652.02s] English:** that stuff with the braces and yeah  
**Translation:** 

**[653.92s] English:** all that stuff's the ui and what it is and ui means user interface um and so what what's really  
**Translation:** 

**[659.68s] English:** going on is it's the interface between the guts and the human and humans are hard right humans  
**Translation:** Vocabulary: interface: 人机界面

**[666.18s] English:** have feelings they have things they like they have things they don't like and a lot of people  
**Translation:** 

**[671.52s] English:** treat programming languages as though humans are just kind of abstract creatures that cannot be  
**Translation:** 

**[676.66s] English:** predicted but it turns out that actually there are there is better and worse like people can tell  
**Translation:** 

**[682.98s] English:** when a  
**Translation:** 

**[683.90s] English:** program language is good or when it was an accident right and uh one of the things with  
**Translation:** 

**[688.58s] English:** swift in particular is that a tremendous amount of time by tremendous number of people have been  
**Translation:** 

**[693.50s] English:** put into really polishing and make it feel good but it also has really good nuts and bolts  
**Translation:** 

**[698.18s] English:** underneath it you said that uh swift makes a lot of people feel good how do you get to that point  
**Translation:** Vocabulary: polishing: 打磨

**[704.36s] English:** so how do you predict that um you know tens of thousands hundreds of thousands of people  
**Translation:** 

**[712.74s] English:** are going to enjoy using the ui and how do you predict that uh hundreds of thousands of people  
**Translation:** 

**[713.26s] English:** are going to enjoy using it and how do you predict that um you know tens of thousands hundreds of  
**Translation:** 

**[713.76s] English:** using this user experience  
**Translation:** 

**[716.00s] English:** of this programming language?  
**Translation:** 

**[717.14s] English:** Well, you can look at it  
**Translation:** 

**[718.10s] English:** in terms of better and worse, right?  
**Translation:** 

**[719.58s] English:** So if you have to...  
**Translation:** 

**[720.00s] English:** write lots of boilerplate or something like that you will feel unproductive and so that's a bad  
**Translation:** 

**[724.18s] English:** thing you can look at in terms of safety if like c for example is what's called a memory unsafe  
**Translation:** Vocabulary: boilerplate: 模板代码

**[729.52s] English:** language and so you get dangling pointers and you get all these kind of bugs but then you have spent  
**Translation:** 

**[733.90s] English:** tons of time debugging and it's a real pain in the butt and you feel unproductive and so by  
**Translation:** Vocabulary: dangling: 悬空的

**[738.16s] English:** subtracting these things from the experience you get um you know happier people but uh again keep  
**Translation:** 

**[744.32s] English:** interrupting i'm sorry uh but so hard to deal with if you look at the people people that are  
**Translation:** Vocabulary: interrupting: 打断; subtracting: 减去

**[751.14s] English:** most productive on stack overflow they are uh they have a set of priorities yeah that may not  
**Translation:** 

**[758.10s] English:** always correlate perfectly with the experience of the majority of users you know if you look at the  
**Translation:** Vocabulary: correlate: 相关; overflow: 溢出; priorities: 优先级

**[764.56s] English:** most upvoted uh quote-unquote correct answer on stack overflow it usually really um sort of  
**Translation:** 

**[773.60s] English:** uh  
**Translation:** 

**[774.32s] English:** prioritizes like safe code proper code stable code uh you know that kind of stuff as opposed  
**Translation:** 

**[782.26s] English:** to like if i want to use go-to statements in my basic right uh i want to use go-to state like  
**Translation:** Vocabulary: prioritizes: 优先考虑

**[790.02s] English:** what if 99 of people want to use go-to statements so you use completely improper  
**Translation:** 

**[793.96s] English:** you know unsafe syntax i don't think that people actually like if you boil it down and you get  
**Translation:** Vocabulary: syntax: 语法规则

**[799.08s] English:** below the surface level people don't actually care about go-tos or if statements or things like this  
**Translation:** 

**[804.06s] English:** they can't  
**Translation:** 

**[804.32s] English:** care about achieving a goal yeah right so the real question is i want to set up a web server and i  
**Translation:** 

**[809.98s] English:** want to do a thing whatever like how how quickly can i achieve that right and so the from programming  
**Translation:** 

**[815.46s] English:** language perspective there's really two things that that matter there one is what libraries exist  
**Translation:** 

**[821.86s] English:** and then how quickly can you put it together and what do the tools around that look like  
**Translation:** 

**[826.30s] English:** right and uh and when you want to build a library that's missing what do you do okay now this is  
**Translation:** 

**[831.66s] English:** where you see huge divergence in the force between the two of them and then you're like oh my god this  
**Translation:** Vocabulary: divergence: 分歧

**[834.32s] English:** is going to be interesting okay and then you're like oh my god this is going to be interesting  
**Translation:** 

**[834.82s] English:** okay and so you look at python for example python is really good at assembling things but it's not  
**Translation:** Vocabulary: assembling: 组装

**[839.74s] English:** so  
**Translation:** 

**[840.00s] English:** great at building all the libraries and so you get because of performance reasons other things  
**Translation:** 

**[844.66s] English:** like this is you get python layered on top of c for example and that means that doing certain  
**Translation:** 

**[850.60s] English:** kinds of things well it doesn't really make sense to do in python instead you do it in c  
**Translation:** 

**[854.24s] English:** and then you wrap it and then you have you're living in two worlds and two worlds never is  
**Translation:** 

**[858.62s] English:** really great because tooling and the debugger doesn't work right and like all these kinds of  
**Translation:** 

**[862.76s] English:** things can you clarify a little bit what uh what you mean by python is not good at building  
**Translation:** 

**[867.72s] English:** libraries meaning it doesn't make certain kinds of certain kinds of libraries no but just the  
**Translation:** 

**[872.60s] English:** actual meaning of the sentence yeah uh meaning like it's not conducive to developers to come in  
**Translation:** 

**[878.82s] English:** and add libraries or it's it's or the language or is it the the duality of the it's a dance between  
**Translation:** Vocabulary: conducive: 有利的

**[885.72s] English:** python and c and well so python's amazing python's great language i do not mean to say that python  
**Translation:** 

**[891.60s] English:** is bad for libraries what i meant to say is um they're python they're libraries that python's  
**Translation:** 

**[897.24s] English:** really good at  
**Translation:** 

**[897.72s] English:** that you can write in python but there are other things like if you want to build a machine learning  
**Translation:** 

**[902.32s] English:** framework you're not going to build a machine learning framework in python because of performance  
**Translation:** 

**[906.56s] English:** for example or you want gpu acceleration or things like this instead what you do is you  
**Translation:** Vocabulary: acceleration: 加速

**[911.50s] English:** write a bunch of c or c++ code or something like that and then you talk to it from python  
**Translation:** 

**[917.16s] English:** right and so this is because of decisions that were made in the python design and um and those  
**Translation:** 

**[925.06s] English:** decisions have other counterbalancing forces but  
**Translation:** 

**[927.40s] English:** you  
**Translation:** Vocabulary: counterbalancing: 制衡

**[927.72s] English:** but the trick when you start looking at this from a programming language perspective is you start to  
**Translation:** 

**[931.76s] English:** say okay cool how do i build this catalog of libraries that are really powerful and how do i  
**Translation:** 

**[938.24s] English:** make it so that then they can be assembled into ways they feel good and they generally work the  
**Translation:** 

**[943.50s] English:** first time because when you're talking about building a thing you have to include the debugging  
**Translation:** Vocabulary: assembled: 组装

**[947.96s] English:** the fixing the turnaround cycle the development cycle all that kind of stuff in in into the  
**Translation:** 

**[954.62s] English:** process of building the thing.  
**Translation:** Vocabulary: turnaround: 周转周期

**[956.02s] English:** It's not just about pounding out the code.  
**Translation:** 

**[958.42s] English:** And so this is where things like  
**Translation:** Vocabulary: pounding: 敲打

**[960.00s] English:** you know, catching bugs at compile time is valuable, for example.  
**Translation:** 

**[963.94s] English:** But if you dive into the details in this, Swift, for example, has certain things like value  
**Translation:** 

**[969.94s] English:** semantics, which is this fancy way of saying that when you treat a variable like a value,  
**Translation:** 

**[976.82s] English:** it acts like a mathematical object would. Okay, so you have used PyTorch a little bit.  
**Translation:** Vocabulary: semantics: 变量的语义

**[984.68s] English:** And in PyTorch, you have tensors. Tensors are n-dimensional grid of numbers. Very simple. You  
**Translation:** 

**[992.06s] English:** can do plus and other operators on them. It's all totally fine. But why do you need to clone  
**Translation:** 

**[996.82s] English:** a tensor sometimes? Have you ever run into that? Yeah. Okay. And so why is that? Why do you need  
**Translation:** 

**[1003.08s] English:** to clone a tensor? It's the usual object thing that's in Python. So in Python, and just like  
**Translation:** 

**[1008.66s] English:** with Java and many other languages, this isn't unique to Python. In Python, it has a thing called  
**Translation:** 

**[1012.78s] English:** reference semantics, which is the nerdy way of...  
**Translation:** Vocabulary: nerdy: 书呆子气的

**[1014.68s] English:** Explaining this. And what that means is you actually have a pointer to a thing instead of  
**Translation:** 

**[1019.36s] English:** the thing. Okay. Now, this is due to a bunch of implementation details that you don't want to go  
**Translation:** Vocabulary: implementation: 实现细节

**[1026.04s] English:** into. But in Swift, you have this thing called value semantics. And so when you have a tensor  
**Translation:** 

**[1030.30s] English:** in Swift, it is a value. If you copy it, it looks like you have a unique copy. And if you go change  
**Translation:** 

**[1035.74s] English:** one of those copies, then it doesn't update the other one because you just made a copy of this  
**Translation:** 

**[1040.24s] English:** thing. Right? So that's like highly error prone.  
**Translation:** Vocabulary: prone: 容易

**[1044.68s] English:** And at least computer science, math centric disciplines about Python, that like the thing  
**Translation:** 

**[1052.40s] English:** you would expect to behave... Like math.  
**Translation:** Vocabulary: disciplines: 学科领域

**[1055.40s] English:** Like math. It doesn't behave like math. And in fact, quietly, it doesn't behave like math,  
**Translation:** 

**[1061.64s] English:** and it can ruin the entirety of your math thing. Exactly. Well, and then it puts you in debugging  
**Translation:** Vocabulary: entirety: 整体

**[1065.32s] English:** land again. Yeah. Right now, you just want to get something done. And you're like, wait a second,  
**Translation:** 

**[1069.52s] English:** where do I need to put clone? And what level of the stack, which is very complicated, which,  
**Translation:** 

**[1074.68s] English:** I thought I was reusing somebody's library, and now I need to understand it to know where to  
**Translation:** 

**[1078.34s] English:** clone a thing, right? And hardly ever.  
**Translation:** Vocabulary: reusing: 重复使用

**[1080.00s] English:** to debug by the way exactly right and so this is where programming languages really matter  
**Translation:** 

**[1084.08s] English:** right so in swift having value semantics so that um both you get the benefit of math working like  
**Translation:** 

**[1090.72s] English:** math right but also the efficiency that comes with certain advantages there certain implementation  
**Translation:** 

**[1096.46s] English:** details there really benefit you as a programmer right so by the value semantics like how do you  
**Translation:** Vocabulary: programmer: 程序员

**[1101.50s] English:** know that things should be treated like a value yeah so so swift uh has a pretty strong culture  
**Translation:** 

**[1107.56s] English:** and good language support for defining values and so if you have an array so tensors are one  
**Translation:** 

**[1112.96s] English:** example that the machine learning folks are very used to um just think about arrays same thing  
**Translation:** 

**[1118.00s] English:** where you have an array you put you create an array you put two or three or four things into it  
**Translation:** 

**[1123.76s] English:** and then you pass it off to another function what happens if that or that function adds some more  
**Translation:** 

**[1130.20s] English:** things to it well you'll see it on the side that you pass it in right this is called reference  
**Translation:** 

**[1135.30s] English:** semantics now what  
**Translation:** 

**[1137.56s] English:** if you pass an array off to a function it scrolls it away in some dictionary or some other data  
**Translation:** Vocabulary: scrolls: 滚动; semantics: 语义

**[1143.42s] English:** structure somewhere right well it thought that you just handed it that array then you return back  
**Translation:** 

**[1148.90s] English:** and that that that reference to that array still exists in the caller and they go and put more  
**Translation:** 

**[1153.66s] English:** stuff in it right the the person you handed it off to may have thought they had the only reference  
**Translation:** 

**[1159.76s] English:** that and so they didn't know what they that this was going to change underneath the covers and so  
**Translation:** 

**[1164.20s] English:** this is where you end up having to do clone so like i was passed a  
**Translation:** 

**[1167.56s] English:** thing i'm not sure if i have the only version of it so now i have to clone it so what value semantics  
**Translation:** 

**[1173.06s] English:** does is it allows you to say hey i have a so in swift it defaults to value semantics  
**Translation:** 

**[1178.00s] English:** also defaults to value semantics and then yeah because most things should end up then it makes  
**Translation:** 

**[1184.80s] English:** sense for that to be the default and one of the important things about that is that arrays and  
**Translation:** 

**[1188.10s] English:** dictionaries and all these other collections that are aggregations of other things also have value  
**Translation:** Vocabulary: aggregations: 集合

**[1192.02s] English:** semantics and so when you pass this around uh to different parts of your program you don't have to  
**Translation:** 

**[1197.56s] English:** do the same thing over and over again you don't have to do the same thing over and over again you can  
**Translation:** 

**[1200.00s] English:** great for two sides right it's great because you define away the bug which is a big deal for  
**Translation:** 

**[1205.38s] English:** productivity the the number one thing most people care about but it's also good for performance  
**Translation:** 

**[1209.34s] English:** because when you're doing a clone so you pass the array down to the thing it's like i don't know if  
**Translation:** 

**[1214.18s] English:** anybody else has it i have to clone it well you just did a copy of a bunch of data it could be  
**Translation:** 

**[1218.74s] English:** big and then it could be that the thing that called you is not keeping track of the old thing  
**Translation:** 

**[1223.86s] English:** so you just made a copy of it and you may not have had to yeah and so the way the value semantics  
**Translation:** 

**[1229.04s] English:** work is in swift is it uses this thing called copy on right which means that you get you get  
**Translation:** 

**[1233.80s] English:** the benefit of safety that's cool and performance and it has another special trick because um if  
**Translation:** 

**[1239.62s] English:** you think certain languages like java for example they have immutable strings and so what they're  
**Translation:** 

**[1244.52s] English:** trying to do is they provide value semantics by having pure immutability functional languages  
**Translation:** Vocabulary: immutability: 不可变性

**[1249.54s] English:** have pure immutability in lots of different places and this provides a much safer model  
**Translation:** 

**[1253.86s] English:** and it provides value semantics the problem with this is if you have immutability everything is  
**Translation:** 

**[1258.86s] English:** expensive  
**Translation:** 

**[1259.04s] English:** everything requires a copy um for example in java if you have a string x and a string y  
**Translation:** 

**[1266.30s] English:** you append them together we have to allocate a new string to hold x y oh if they're immutable  
**Translation:** 

**[1273.30s] English:** well and strings strings in java are immutable and if there's there's optimizations for short  
**Translation:** Vocabulary: allocate: 分配; append: 追加; immutable: 不可变; optimizations: 优化

**[1279.04s] English:** ones and it's complicated but but generally uh think about them as a separate allocation  
**Translation:** 

**[1283.80s] English:** and so when you append them together you have to go allocate a third thing  
**Translation:** Vocabulary: allocation: 分配

**[1288.28s] English:** because somebody  
**Translation:** 

**[1289.04s] English:** might have a pointer to either of the other ones right and you can't go change them so you have to  
**Translation:** 

**[1292.32s] English:** go allocate a third thing um because of the beauty of how the swift value semantics system works out  
**Translation:** 

**[1297.40s] English:** if you have a string on swift and you say hey put in x right and they say append on y z w what  
**Translation:** Vocabulary: semantics: 语义

**[1304.30s] English:** it knows that there's only one reference to that and so it can do an in-place update  
**Translation:** 

**[1308.82s] English:** and so you're not allocating tons of stuff on the side you're not you don't have all those  
**Translation:** Vocabulary: allocating: 分配内存

**[1314.20s] English:** problems when you pass it off you can know you have the only reference if you pass it off to  
**Translation:** 

**[1318.34s] English:** multiple different people you're not allocating tons of stuff on the side you're not you don't have  
**Translation:** 

**[1319.04s] English:** the only reference if you pass it off to multiple different people but nobody changes  
**Translation:** 

**[1320.00s] English:** it they can all share the same thing so you get a lot of the benefit of of purely mutable design  
**Translation:** 

**[1325.68s] English:** and so you get a really nice sweet spot that i haven't seen in other languages yeah that's  
**Translation:** 

**[1329.62s] English:** interesting like i thought i thought there was going to be a philosophical like narrative here  
**Translation:** Vocabulary: philosophical: 哲学性的

**[1335.98s] English:** that you're gonna have to pay a cost for it because it sounds like uh i think value semantics  
**Translation:** 

**[1344.12s] English:** is beneficial for easing of debugging or minimizing the risk of errors like bringing  
**Translation:** Vocabulary: minimizing: 减少

**[1351.80s] English:** the errors closer to the source bringing the symptom of the error closer to the source of  
**Translation:** 

**[1358.76s] English:** the error however you say that and but you're saying there's not a performance cost either  
**Translation:** 

**[1364.66s] English:** if you implement yeah correctly well so there's trade-offs with everything and so if you are  
**Translation:** 

**[1369.42s] English:** doing very low level stuff then sometimes you can notice the cost but then what you're  
**Translation:** 

**[1374.10s] English:** you're doing is you're saying what is the right default so um coming back to user interface when  
**Translation:** 

**[1379.24s] English:** you when you talk about programming languages one of the major things that swift does that makes  
**Translation:** Vocabulary: interface: 用户界面

**[1383.24s] English:** people love it that is not obvious when it comes to designing a language is this ui principle of  
**Translation:** 

**[1390.14s] English:** progressive disclosure of complexity okay so swift like many languages are is very powerful  
**Translation:** Vocabulary: complexity: 复杂性

**[1395.98s] English:** the question is when do you have to learn the power as a user so swift like python allows you  
**Translation:** 

**[1402.30s] English:** to start with like print hello world right certain other languages uh start with like public static  
**Translation:** 

**[1407.42s] English:** void main class like all the ceremony right yeah and so you go to teach you teach a new person  
**Translation:** 

**[1414.24s] English:** hey welcome welcome to this new thing let's talk about public access control classes wait what's  
**Translation:** 

**[1420.72s] English:** that string system dot out dot print land like packages like right and so instead if you take  
**Translation:** 

**[1428.18s] English:** this and you say hey we need you need we need packages you know modules we need we need  
**Translation:** 

**[1432.30s] English:** powerful things like classes we need data structures we need like all these things  
**Translation:** 

**[1436.74s] English:** the question is how do you factor the complexity and how do you make  
**Translation:** 

**[1440.00s] English:** it so that the normal case scenario is you're dealing with things that work the right way in  
**Translation:** 

**[1445.70s] English:** the right way and give you good performance the right by default but then as a power user if you  
**Translation:** 

**[1451.26s] English:** want to dive down to it you have full c c performance full control over low level pointers  
**Translation:** 

**[1455.90s] English:** you can call malik if you want to call malik this is not recommended on the first page of every  
**Translation:** 

**[1460.06s] English:** tutorial but it's actually really important when you want to get work done right and so being able  
**Translation:** 

**[1465.06s] English:** to have that is really the design in programming language design and design is really really hard  
**Translation:** Vocabulary: tutorial: 教程

**[1471.20s] English:** it's something that i think a lot of people kind of um outside of ui again a lot of people just  
**Translation:** 

**[1477.50s] English:** think is uh subjective like there's nothing you know it's just like curly braces or whatever it's  
**Translation:** Vocabulary: braces: 花括号

**[1483.68s] English:** just like somebody's preference but actually good design is something you can feel and how many  
**Translation:** 

**[1489.78s] English:** people are involved with good design so if we looked at swift we'll look at historically i mean  
**Translation:** Vocabulary: historically: 历史上

**[1495.04s] English:** this might touch like uh there's almost like a steve jobs question too like how much dictatorial  
**Translation:** 

**[1502.22s] English:** decision making is required versus um collaborative and we'll talk about how all that can go wrong or  
**Translation:** Vocabulary: collaborative: 合作的; dictatorial: 独裁的

**[1510.64s] English:** right yeah but yeah well swift so i can't speak to in general all design everywhere uh so the way  
**Translation:** 

**[1515.88s] English:** it works with swift is that um there's a core team and so core team is uh six or seven people  
**Translation:** 

**[1522.18s] English:** ish something like that that is people that have been working  
**Translation:** 

**[1525.02s] English:** with swift since very early days and so and by early days it's not that long ago okay yeah so  
**Translation:** 

**[1530.82s] English:** it became public in 2014 so it's been six years public now but um but so that's enough time that  
**Translation:** 

**[1537.70s] English:** there's a story arc there okay yeah and there's mistakes have been made that then get fixed and  
**Translation:** 

**[1542.88s] English:** you learn something and then you you know and so uh that what the core team does is it provides  
**Translation:** 

**[1547.36s] English:** continuity and so you want to have a okay well uh there's a big hole that we want to fill we know we  
**Translation:** Vocabulary: continuity: 连贯性

**[1554.58s] English:** want to fill it and we want to fill it and we want to fill it and we want to fill it and we want to  
**Translation:** 

**[1555.00s] English:** it so don't do other things that invade that space until we fill the hole right there  
**Translation:** 

**[1560.00s] English:** There's a boulder that's missing here.  
**Translation:** 

**[1561.20s] English:** We will do that boulder, even though it's not today.  
**Translation:** Vocabulary: boulder: 巨石

**[1564.80s] English:** Keep out of that space.  
**Translation:** 

**[1566.14s] English:** And the whole team remembers the myth of the boulder that's there.  
**Translation:** 

**[1571.08s] English:** Yeah, there's a general sense of what the future looks like in broad strokes  
**Translation:** 

**[1574.32s] English:** and a shared understanding of that,  
**Translation:** 

**[1576.30s] English:** combined with a shared understanding of what has happened in the past  
**Translation:** 

**[1579.22s] English:** that worked out well and didn't work out well.  
**Translation:** 

**[1581.80s] English:** The next level out is you have what's called the Swift Evolution Community,  
**Translation:** 

**[1585.64s] English:** and you've got, in that case, hundreds of people  
**Translation:** 

**[1587.52s] English:** that really care passionately about the way Swift evolves.  
**Translation:** 

**[1591.08s] English:** And that's an amazing thing to, again,  
**Translation:** Vocabulary: passionately: 热情地

**[1593.22s] English:** the core team doesn't necessarily need to come up with all the good ideas.  
**Translation:** 

**[1596.76s] English:** You've got hundreds of people out there that care about something,  
**Translation:** 

**[1598.94s] English:** and they come up with really good ideas too.  
**Translation:** 

**[1601.10s] English:** And that provides this rock tumbler for ideas.  
**Translation:** 

**[1604.92s] English:** And so the evolution process is a lot of people in a discourse forum  
**Translation:** 

**[1610.24s] English:** that are hashing it out and trying to talk about,  
**Translation:** Vocabulary: discourse: 讨论; hashing: 争论

**[1612.00s] English:** okay, well, should we go left or right?  
**Translation:** 

**[1614.06s] English:** Or if we did this, what would be good?  
**Translation:** 

**[1615.70s] English:** And here you're talking about hundreds of people.  
**Translation:** 

**[1617.68s] English:** So you're not going to get consensus necessarily.  
**Translation:** 

**[1620.30s] English:** You're not obvious consensus.  
**Translation:** 

**[1621.98s] English:** And so there's a proposal process  
**Translation:** 

**[1624.16s] English:** that then allows the core team and the community to work this out.  
**Translation:** 

**[1628.46s] English:** And what the core team does is it aims to get consensus out of the community  
**Translation:** 

**[1632.70s] English:** and provide guardrails, but also provide long-term,  
**Translation:** 

**[1637.16s] English:** make sure we're going the right direction kind of things.  
**Translation:** Vocabulary: guardrails: 防护措施

**[1640.14s] English:** So does that group represent how much people will love the user interface?  
**Translation:** 

**[1647.52s] English:** Do you think they're able to capture that?  
**Translation:** Vocabulary: interface: 用户界面

**[1649.42s] English:** Well, I mean, it's something we talk about a lot.  
**Translation:** 

**[1651.04s] English:** It's something we care about.  
**Translation:** 

**[1652.38s] English:** How well we do that is up for debate,  
**Translation:** 

**[1654.78s] English:** but I think that we've done pretty well so far.  
**Translation:** 

**[1656.78s] English:** Is the beginner in mind?  
**Translation:** 

**[1658.52s] English:** Yeah.  
**Translation:** 

**[1658.82s] English:** Because you said the progressive disclosure complexity.  
**Translation:** 

**[1660.80s] English:** Yeah, so we care a lot about that, a lot about power,  
**Translation:** Vocabulary: complexity: 复杂性

**[1665.10s] English:** a lot about efficiency, a lot about there are many factors to good design,  
**Translation:** 

**[1668.50s] English:** and you have to figure out a way to kind of work your way through that.  
**Translation:** 

**[1673.18s] English:** So if you think about, like, a language I love is Lisp.  
**Translation:** 

**[1677.22s] English:** Okay.  
**Translation:** 

**[1677.52s] English:** Probably still because I use Emacs, but I haven't.  
**Translation:** 

**[1680.00s] English:** done anything any serious working list but it has a ridiculous amount of parentheses yeah um  
**Translation:** Vocabulary: emacs: 编辑器; parentheses: 括号

**[1686.06s] English:** i've also you know with java and c++ uh the braces um you know i i like i i enjoyed the comfort of  
**Translation:** 

**[1697.82s] English:** being between braces you know yeah yeah well python is really sorry to interrupt just like  
**Translation:** Vocabulary: braces: 花括号

**[1703.50s] English:** and last thing to me as a design if i was a language designer uh god forbid as i would be  
**Translation:** 

**[1709.66s] English:** very surprised that python with no braces would nevertheless somehow be comforting also so like  
**Translation:** 

**[1718.48s] English:** i could see arguments for all of these but look at this this is evidence that it's not about braces  
**Translation:** 

**[1722.88s] English:** versus tabs right exactly you're good it's a good point right so like you know there's there's  
**Translation:** 

**[1729.38s] English:** evidence that but see like it's one of the most argued about things oh yeah of course just like  
**Translation:** 

**[1733.36s] English:** tabs and spaces which it doesn't i mean there's one obvious right answer but it doesn't it doesn't  
**Translation:** 

**[1738.44s] English:** actually matter what's that  
**Translation:** 

**[1739.66s] English:** come on we're friends like come on what are you trying to do to me here people are gonna yeah  
**Translation:** 

**[1744.26s] English:** half the people are gonna tune out yeah um so so so you're able to identify things that don't  
**Translation:** 

**[1750.02s] English:** really matter for the experience well no no it's it's always a really hard so the easy decisions  
**Translation:** 

**[1755.88s] English:** are easy right i mean you you can fine those are not the interesting ones the hard ones are the  
**Translation:** 

**[1760.16s] English:** ones that are most interesting right the hard ones are the places where hey we want to do a thing  
**Translation:** 

**[1764.86s] English:** everybody agrees we should do it there's one proposal on the table but it has all these  
**Translation:** 

**[1769.66s] English:** bad things associated with it well okay what are we gonna do about that do we just take it  
**Translation:** 

**[1774.54s] English:** do we delay it do we say hey well maybe there's this other feature that if we do that first this  
**Translation:** 

**[1779.80s] English:** will work out better um how does this if if we do this are we paying ourselves into a corner right  
**Translation:** 

**[1786.10s] English:** and so this is where again you're having that core team of people that uh has some continuity  
**Translation:** 

**[1790.40s] English:** and has perspective has some of the historical understanding is really valuable because you get  
**Translation:** Vocabulary: continuity: 连贯性

**[1795.20s] English:** um it's not just like one brain you get the power of multiple people coming together to make a  
**Translation:** 

**[1799.54s] English:** decision and you're able to do it and you're able to do it and you're able to do it and you're able to  
**Translation:** 

**[1799.66s] English:** make a decision  
**Translation:** 

**[1800.00s] English:** and then you get the best out of all these people and you also can harness the the community around  
**Translation:** 

**[1805.50s] English:** it what about like the decision of whether like in python having one type or having you know  
**Translation:** 

**[1812.34s] English:** strict typing yeah okay yeah let's talk about this so so um i like how you put that by the way like  
**Translation:** 

**[1819.14s] English:** so so many people would say that python doesn't have types doesn't have types yeah but you're  
**Translation:** 

**[1823.18s] English:** right i've listened to you enough to where yeah i'm a fan of yours and i've listened to way too  
**Translation:** 

**[1829.10s] English:** many podcasts and videos of you talking about this oh yeah so i would argue that python has  
**Translation:** 

**[1833.98s] English:** one type and so um so like when you import python and swift which by the way works really well  
**Translation:** 

**[1839.30s] English:** you have everything comes in as a python object now here they're trade-offs because um uh you  
**Translation:** 

**[1846.06s] English:** know it depends on where you're optimizing for and python is a super successful language for  
**Translation:** Vocabulary: optimizing: 优化

**[1849.36s] English:** really good reason um because it has one type uh you get duck typing for free and things like this  
**Translation:** 

**[1855.04s] English:** but also you're pushing you're making it very easy to  
**Translation:** 

**[1858.36s] English:** to pound out  
**Translation:** 

**[1859.04s] English:** code on the one hand but you're also making it very easy to introduce uh complicated bugs you  
**Translation:** 

**[1864.48s] English:** have to debug and you pass a string into something that expects an integer and it doesn't immediately  
**Translation:** 

**[1869.70s] English:** die it goes all the way down the stack trace and you find yourself in the middle of some code that  
**Translation:** Vocabulary: integer: 整数

**[1873.52s] English:** you really didn't want to know anything about and it blows up and you're just saying well what did  
**Translation:** 

**[1876.76s] English:** i do wrong right and so types are good and bad and they have trade-offs they're good for performance  
**Translation:** 

**[1882.48s] English:** and certain other things depending on where you're coming from but it's all about trade-offs and so  
**Translation:** 

**[1886.60s] English:** this is this is what design is right design is about weighing trade-offs and trying to understand  
**Translation:** 

**[1891.02s] English:** the ramifications of the the things that you're weighing like types or not or one type or many  
**Translation:** 

**[1896.78s] English:** types um but also within many types how powerful do you make that type system is another very  
**Translation:** Vocabulary: ramifications: 深远影响

**[1902.64s] English:** complicated question uh with lots of trade-offs it's very interesting by the way uh but uh but  
**Translation:** 

**[1908.70s] English:** that's like one one dimension and there's a bunch of other dimensions jit compiled versus static  
**Translation:** Vocabulary: compiled: 编译过的; dimension: 维度; dimensions: 多个维度

**[1914.66s] English:** compiled garbage collected versus  
**Translation:** 

**[1916.50s] English:** reference counted versus memory manual memory management  
**Translation:** 

**[1920.00s] English:** versus, you know, like in like all these different trade-offs  
**Translation:** 

**[1922.86s] English:** and how you balance them  
**Translation:** 

**[1923.74s] English:** are what make a programming language good.  
**Translation:** 

**[1925.82s] English:** Concurrency.  
**Translation:** Vocabulary: concurrency: 并发

**[1926.80s] English:** Yeah.  
**Translation:** 

**[1927.16s] English:** So in all those things, I guess,  
**Translation:** 

**[1929.34s] English:** when you're designing the language,  
**Translation:** 

**[1931.30s] English:** you also have to think of how that's going to get all compiled down to.  
**Translation:** 

**[1935.08s] English:** If you care about performance, yeah.  
**Translation:** 

**[1937.34s] English:** Well, and go back to Lisp, right?  
**Translation:** 

**[1938.78s] English:** So Lisp, also I would say JavaScript  
**Translation:** 

**[1940.44s] English:** is another example of a very simple language, right?  
**Translation:** 

**[1944.08s] English:** And so one of the, so I also love Lisp.  
**Translation:** 

**[1947.04s] English:** I don't use it as much as maybe you do or you did.  
**Translation:** 

**[1949.58s] English:** No, I think we're both, everyone who loves Lisp,  
**Translation:** 

**[1952.52s] English:** it's like, you love, it's like, I don't know,  
**Translation:** 

**[1954.92s] English:** I love Frank Sinatra,  
**Translation:** 

**[1956.30s] English:** but like how often do I seriously listen to Frank Sinatra?  
**Translation:** Vocabulary: sinatra: 弗兰克·辛纳屈

**[1959.18s] English:** Sure, sure.  
**Translation:** 

**[1960.46s] English:** But you look at that or you look at JavaScript,  
**Translation:** 

**[1962.74s] English:** which is another very different but relatively simple language,  
**Translation:** 

**[1965.90s] English:** and there's certain things that don't exist in the language,  
**Translation:** 

**[1969.00s] English:** but there is inherent complexity to the problems  
**Translation:** 

**[1971.78s] English:** that we're trying to model.  
**Translation:** Vocabulary: complexity: 复杂性

**[1973.06s] English:** And so what happens to the complexity?  
**Translation:** 

**[1974.62s] English:** In the case of both of them, for example,  
**Translation:** 

**[1977.08s] English:** you say, well, what about large-scale software development?  
**Translation:** 

**[1979.58s] English:** Okay, well, you need something like packages.  
**Translation:** 

**[1982.38s] English:** Neither language has a language affordance for packages.  
**Translation:** 

**[1985.80s] English:** And so what you get is patterns.  
**Translation:** Vocabulary: affordance: 使用提示

**[1987.42s] English:** You get things like NPN.  
**Translation:** 

**[1988.70s] English:** You get things like these ecosystems that get built around.  
**Translation:** 

**[1992.16s] English:** And I'm a believer that if you don't model  
**Translation:** 

**[1994.96s] English:** at least the most important inherent complexity in the language,  
**Translation:** Vocabulary: believer: 信仰者

**[1998.50s] English:** then what ends up happening is that complexity gets pushed elsewhere.  
**Translation:** 

**[2002.70s] English:** And when it gets pushed elsewhere, sometimes that's great  
**Translation:** 

**[2005.00s] English:** because often building things as libraries is very flexible  
**Translation:** 

**[2008.16s] English:** and very powerful and allows you to evolve.  
**Translation:** 

**[2009.58s] English:** But often it leads to a lot of unnecessary divergence  
**Translation:** 

**[2013.78s] English:** in the force and fragmentation.  
**Translation:** Vocabulary: divergence: 分歧; fragmentation: 碎片化

**[2015.80s] English:** And when that happens, you just get kind of a mess.  
**Translation:** 

**[2019.56s] English:** And so the question is, how do you balance that?  
**Translation:** 

**[2022.88s] English:** Don't put too much stuff in the language  
**Translation:** 

**[2024.12s] English:** because that's really expensive and it makes things complicated.  
**Translation:** 

**[2026.68s] English:** But how do you model enough of the inherent complexity of the problem  
**Translation:** 

**[2030.02s] English:** that you provide the framework and the structure for people to think about?  
**Translation:** 

**[2034.86s] English:** So the key thing to think about with programming languages,  
**Translation:** 

**[2038.84s] English:** and you think about it a lot,  
**Translation:** 

**[2039.42s] English:** you think about what it.  
**Translation:** 

**[2040.00s] English:** programming languages therefore is it's about making a human more productive right and so like  
**Translation:** 

**[2044.62s] English:** there's an old i think it's a steve jobs quote about um it's a bicycle for the mind right you  
**Translation:** 

**[2050.86s] English:** can you can you can definitely walk but you'll get there a lot faster if you can bicycle on your way  
**Translation:** 

**[2056.90s] English:** and a programming language is a bicycle for the mind yeah it's basically uh wow that's a really  
**Translation:** 

**[2062.52s] English:** interesting way to think about it but by raising the level of abstraction now you can fit more  
**Translation:** Vocabulary: abstraction: 抽象

**[2066.28s] English:** things in your head by being able to just directly leverage somebody's library you can now get  
**Translation:** 

**[2071.50s] English:** something done quickly um in the case of swift swift ui is this new framework that apple has  
**Translation:** Vocabulary: leverage: 利用

**[2076.94s] English:** released recently for doing ui programming and it has this declarative programming model which  
**Translation:** 

**[2083.18s] English:** defines away entire classes of bugs it's make it builds on value semantics and many other nice  
**Translation:** Vocabulary: declarative: 声明式的; semantics: 语义

**[2087.78s] English:** swift things and what this does is allows you to get way more done with way less code and now your  
**Translation:** 

**[2094.48s] English:** productivity as a developer is much higher  
**Translation:** 

**[2096.28s] English:** right and so that that's really the what programming languages should be about is it's  
**Translation:** 

**[2100.46s] English:** not about tabs versus spaces or curly braces or whatever it's about how productive do you make  
**Translation:** Vocabulary: braces: 花括号

**[2104.70s] English:** the person and you can only see that when you have libraries that were built with the right  
**Translation:** 

**[2110.40s] English:** intention that the language was designed for and with swift i think we're still a little bit early  
**Translation:** 

**[2115.90s] English:** um but swift ui and many other things that are coming out now are really showing that and i  
**Translation:** 

**[2120.44s] English:** think that they're opening people's eyes it's kind of interesting to think about like how  
**Translation:** 

**[2126.28s] English:** that you know the knowledge of something of how good the bicycle is how people learn about that  
**Translation:** 

**[2133.24s] English:** you know so i've used c plus plus now this is not going to be a trash talking session about c plus  
**Translation:** 

**[2139.48s] English:** plus but you see plus plus for a really long go there if you want i have the scars i i feel like  
**Translation:** 

**[2146.04s] English:** i spent many years without realizing like there's languages that could for my particular life style  
**Translation:** 

**[2154.12s] English:** brain style thinking style thinking style thinking style thinking style thinking style thinking style  
**Translation:** 

**[2156.28s] English:** there's languages that could make me a lot more productive  
**Translation:** 

**[2160.00s] English:** In the debugging stage, in just the development stage and thinking like the bicycle for the mind that I could fit more stuff into my...  
**Translation:** 

**[2167.76s] English:** Python's a great example of that, right?  
**Translation:** 

**[2169.30s] English:** I mean, a machine learning framework in Python is a great example of that.  
**Translation:** 

**[2172.28s] English:** It's just very high abstraction level.  
**Translation:** 

**[2174.74s] English:** And so you can be thinking about things on a very high level algorithmic level instead of thinking about, okay, well, am I copying this tensor to a GPU or not?  
**Translation:** 

**[2182.72s] English:** Right?  
**Translation:** Vocabulary: algorithmic: 算法的

**[2183.74s] English:** It's not what you want to be thinking about.  
**Translation:** 

**[2185.34s] English:** And as I was telling you, I mean, I guess the question I had is, you know, how does a person like me or in general people discover more productive, you know, languages?  
**Translation:** 

**[2196.78s] English:** Like how I was, as I've been telling you offline, I've been looking for like a project to work on in Swift so I can really try it out.  
**Translation:** 

**[2205.34s] English:** I mean, my intuition was like doing a hello world is not going to get me there to get me to experience the power of language.  
**Translation:** Vocabulary: intuition: 直觉

**[2213.54s] English:** You need a few weeks to change your metabolism.  
**Translation:** 

**[2216.00s] English:** Exactly.  
**Translation:** Vocabulary: metabolism: 新陈代谢

**[2216.70s] English:** I think that's beautifully put.  
**Translation:** 

**[2219.34s] English:** That's one of the problems with people with diets.  
**Translation:** 

**[2221.66s] English:** Like I'm actually currently to go in parallel, but in a small tangent is I've been recently eating only meat.  
**Translation:** 

**[2229.56s] English:** Okay.  
**Translation:** Vocabulary: tangent: 旁支

**[2229.80s] English:** Okay.  
**Translation:** 

**[2231.04s] English:** So most people are like, think that's horribly unhealthy or whatever.  
**Translation:** Vocabulary: horribly: 极其

**[2236.88s] English:** You have like a million, whatever the science is, it just doesn't sound right.  
**Translation:** 

**[2242.48s] English:** So back when I was in college, we did the Atkins diet.  
**Translation:** Vocabulary: atkins: 阿特金斯饮食法

**[2245.06s] English:** That was, that was a thing.  
**Translation:** 

**[2246.42s] English:** Similar.  
**Translation:** 

**[2247.14s] English:** And, but if you, you have to always give these things a chance.  
**Translation:** 

**[2250.44s] English:** I mean, with dieting, always not dieting, but it's just the things that you like.  
**Translation:** 

**[2255.44s] English:** If I eat personally, if I eat meat, just everything, I can be super focused or more focused than usual.  
**Translation:** 

**[2262.72s] English:** I just feel great.  
**Translation:** 

**[2264.02s] English:** I mean, I've been running a lot of, you know, doing pushups and posts and so on.  
**Translation:** 

**[2268.00s] English:** I mean, Python is similar in that sense for me.  
**Translation:** Vocabulary: pushups: 俯卧撑

**[2270.52s] English:** Where are you going with this?  
**Translation:** 

**[2271.54s] English:** I mean, literally, I just.  
**Translation:** 

**[2275.06s] English:** I felt I had like a stupid smile on my face when I first started using Python.  
**Translation:** 

**[2280.00s] English:** i could uh code up really quick things like i like i i would see the world i'll be empowered  
**Translation:** 

**[2286.54s] English:** to write a script to to um you know to do some basic data processing to rename files on my  
**Translation:** 

**[2293.04s] English:** computer yeah right like pearl didn't do that for me uh uh i mean a little bit well and again like  
**Translation:** Vocabulary: rename: 重命名文件

**[2300.36s] English:** none of these are about which which is best or something like that but there's definitely better  
**Translation:** 

**[2304.34s] English:** and worse here but it clicks right well yeah and if you if you look at pearl for example you get  
**Translation:** 

**[2309.62s] English:** bogged down in uh scalars versus arrays versus hashes versus type globs and like all that kind  
**Translation:** 

**[2315.30s] English:** of stuff and and python's like yeah let's not do this right and some of it's debugging like  
**Translation:** Vocabulary: bogged: 陷入; globs: 类型glob; hashes: 哈希; scalars: 标量

**[2320.18s] English:** everyone has different priorities but for me it's can i create systems for myself that  
**Translation:** 

**[2325.30s] English:** empower me to debug quickly like i've always been a big fan even just crude like asserts like always  
**Translation:** Vocabulary: empower: 赋予权力; priorities: 优先级

**[2332.70s] English:** uh stating things that should be true which in python i found in myself do  
**Translation:** 

**[2339.44s] English:** more and more and more and more and more and more and more and more and more and more and more  
**Translation:** 

**[2339.60s] English:** and more because of type all these kinds of stuff well you could think of types in a programming  
**Translation:** 

**[2344.24s] English:** language as being kind of assert yeah they could check to compile time right um so how do you learn  
**Translation:** 

**[2350.60s] English:** a new thing well so this or how do how do people learn new things right this this is hard uh people  
**Translation:** 

**[2355.48s] English:** don't like to change people generally don't like change around them either and so uh we're all very  
**Translation:** 

**[2361.42s] English:** slow to adapt and change and usually there's a catalyst that's required to to force yourself  
**Translation:** 

**[2366.14s] English:** over the over over this so for learning a  
**Translation:** Vocabulary: catalyst: 催化剂

**[2369.42s] English:** programming language it really comes down to finding an excuse like build a thing that  
**Translation:** 

**[2374.40s] English:** that's that the language is actually good for that the ecosystem's ready for um and so um and  
**Translation:** 

**[2381.02s] English:** so if you were to write an ios app for example that would be the easy case obviously you would  
**Translation:** 

**[2384.94s] English:** you would use swift for that right there are android so swift runs on android oh does it  
**Translation:** 

**[2390.86s] English:** oh yeah yeah swift runs in lots of services that work so uh okay so swift swift is built on top of  
**Translation:** 

**[2397.66s] English:** is built on top of llvm yeah lvm runs where is my business do you do well in early class did i ever  
**Translation:** 

**[2398.60s] English:** be during class what was it now was it教 me i don't know abc used to playing games on my own  
**Translation:** 

**[2399.26s] English:** everywhere  
**Translation:** 

**[2400.00s] English:** lvm for example builds the android kernel oh wow okay so yeah um so i didn't realize this  
**Translation:** 

**[2406.68s] English:** yeah so swift swift is very portable runs on windows there's it runs on lots of different  
**Translation:** Vocabulary: kernel: 内核

**[2411.84s] English:** things and uh swift side uh swift ui and then there's a thing called ui kit so can i build an  
**Translation:** 

**[2418.64s] English:** app with swift uh well so that that's the thing is the ecosystem is what matters there so swift ui  
**Translation:** 

**[2424.98s] English:** and ui kit are apple technologies okay got it and so they happen to like swift ui happens to be  
**Translation:** 

**[2429.84s] English:** written in swift but it's an apple proprietary framework that um apple loves and wants to keep  
**Translation:** Vocabulary: proprietary: 专有框架

**[2435.00s] English:** on its platform which makes total sense you go to go to android and you don't have that library  
**Translation:** 

**[2438.82s] English:** yeah right and so android has a different ecosystem of things that hasn't been built  
**Translation:** 

**[2443.76s] English:** out and doesn't work as well with swift and so you can totally use swift to do uh like arithmetic  
**Translation:** 

**[2448.68s] English:** and things like this but building ui with swift on android is not not not a not a great experience  
**Translation:** Vocabulary: arithmetic: 算术

**[2453.86s] English:** right now so so if i wanted to uh to learn swift what's the pro i mean the one  
**Translation:** 

**[2459.84s] English:** practical different version of that is um swift for tensorflow for example and one of the inspiring  
**Translation:** 

**[2466.92s] English:** things for me with both tensorflow and pytorch is how quickly the community can like switch  
**Translation:** 

**[2472.80s] English:** from different libraries like you could see some of the communities switching to pytorch now  
**Translation:** 

**[2478.96s] English:** but it's very easy to see and then tensorflow is really stepping up its game and then there's  
**Translation:** 

**[2485.12s] English:** no reason why i think it the way it works is basically it has to be one github repo like  
**Translation:** 

**[2489.84s] English:** one paper steps up to get it gets people excited it gets people excited and they're like i have to  
**Translation:** 

**[2494.36s] English:** learn this swift for what swift again yeah and then they learn and they fall in love with i mean  
**Translation:** 

**[2501.38s] English:** that's what happened by torch has there has to be a reason a catalyst yeah and so and and there i  
**Translation:** 

**[2506.72s] English:** mean people don't like change but it turns out that once you've worked with one or two programming  
**Translation:** Vocabulary: catalyst: 催化剂

**[2511.54s] English:** languages they're the basics are pretty similar and so one of the fun things about learning  
**Translation:** 

**[2516.12s] English:** programming languages even even maybe lisp i don't know if you agree with this  
**Translation:** 

**[2519.84s] English:** it's  
**Translation:** 

**[2520.00s] English:** is that when you start doing that, you start learning new things.  
**Translation:** 

**[2523.74s] English:** Because you have a new way to do things, and you're forced to do them,  
**Translation:** 

**[2526.82s] English:** and that forces you to explore, and it puts you in learning mode.  
**Translation:** 

**[2530.28s] English:** And when you get in learning mode, your mind kind of opens a little bit,  
**Translation:** 

**[2532.76s] English:** and you can see things in a new way, even when you go back to the old place.  
**Translation:** 

**[2537.12s] English:** Right.  
**Translation:** 

**[2537.56s] English:** Yeah, so Lisp is functional.  
**Translation:** 

**[2539.88s] English:** Yeah.  
**Translation:** 

**[2540.92s] English:** But I wish there was a kind of window.  
**Translation:** 

**[2543.64s] English:** Maybe you can tell me if there is.  
**Translation:** 

**[2545.42s] English:** There you go.  
**Translation:** 

**[2545.96s] English:** This is a question to ask, what is the most beautiful feature in a programming language?  
**Translation:** 

**[2550.90s] English:** Before I ask it, let me say, like, with Python, I remember I saw Lisp Comprehensions.  
**Translation:** Vocabulary: comprehensions: 列表推导

**[2556.62s] English:** Yeah.  
**Translation:** 

**[2557.26s] English:** It was like when I, like, really took it in.  
**Translation:** 

**[2560.74s] English:** Yeah.  
**Translation:** 

**[2561.66s] English:** I don't know.  
**Translation:** 

**[2562.38s] English:** I just loved it.  
**Translation:** 

**[2563.68s] English:** It was, like, fun to do.  
**Translation:** 

**[2565.26s] English:** Like, it was fun to do that kind of – something about it, to be able to filter through a list  
**Translation:** 

**[2572.54s] English:** and to create a new list all in a single line.  
**Translation:** 

**[2575.10s] English:** It was elegant.  
**Translation:** 

**[2576.28s] English:** I could all get into my head, and it just made me fall in love with the language.  
**Translation:** 

**[2582.22s] English:** So is there – let me ask you a question.  
**Translation:** 

**[2584.60s] English:** Is there – what do you use the most beautiful feature in a programming language that you've ever encountered?  
**Translation:** Vocabulary: encountered: 遇到

**[2591.72s] English:** In Swift, maybe, and then outside of Swift?  
**Translation:** 

**[2595.08s] English:** I think the thing that I like the most from a programming language –  
**Translation:** 

**[2598.88s] English:** so I think the thing you have to think about with a programming language, again, what is the goal?  
**Translation:** 

**[2603.34s] English:** You're trying to get people to get –  
**Translation:** 

**[2605.10s] English:** you're trying to get things done quickly.  
**Translation:** 

**[2607.18s] English:** And so you need libraries, you need high-quality libraries,  
**Translation:** 

**[2610.14s] English:** and then you need a user base around them that can assemble them and do cool things with them, right?  
**Translation:** 

**[2614.80s] English:** And so to me, the question is, what enables high-quality libraries?  
**Translation:** Vocabulary: assemble: 组装

**[2619.54s] English:** Okay.  
**Translation:** 

**[2620.38s] English:** Yeah.  
**Translation:** 

**[2620.72s] English:** And there's a huge divide in the world between libraries who enable high-quality libraries  
**Translation:** 

**[2627.26s] English:** versus the ones that put special stuff in the language.  
**Translation:** 

**[2632.48s] English:** So programming languages that enable –  
**Translation:** 

**[2635.10s] English:** High-quality libraries.  
**Translation:** 

**[2635.76s] English:** High-quality libraries.  
**Translation:** 

**[2636.78s] English:** Got it.  
**Translation:** 

**[2637.48s] English:** So what I mean by that is expressive.  
**Translation:** 

**[2640.00s] English:** libraries that then feel like a natural integrated part of the language itself so um an example of  
**Translation:** Vocabulary: expressive: 表达能力强的

**[2647.60s] English:** this in swift is that int and float and also rain string things like this these are all part of the  
**Translation:** 

**[2652.80s] English:** library like int is not hard-coded into swift and so what that means is that because int is just a  
**Translation:** 

**[2660.46s] English:** library thing defined in the standard library along with strings and arrays and all the other  
**Translation:** 

**[2664.20s] English:** things that come with the standard library um well hopefully you do like int but anything that  
**Translation:** 

**[2670.68s] English:** any language features that you needed to define int you can also use in your own types so if you  
**Translation:** 

**[2676.34s] English:** wanted to find a uh quaternion or something like this right um well it doesn't come in the standard  
**Translation:** Vocabulary: quaternion: 四元数

**[2682.40s] English:** library um there's a very special set of people that care a lot about this but those people are  
**Translation:** 

**[2688.22s] English:** also important it's not it's not about classism right it's not about the people who care about  
**Translation:** 

**[2692.80s] English:** instant floats are more important  
**Translation:** 

**[2694.08s] English:** than the people care about quaternions and so to me the beautiful things about programming  
**Translation:** Vocabulary: quaternions: 四元数

**[2697.42s] English:** languages is when you allow those communities to build high quality libraries that feel native  
**Translation:** 

**[2702.90s] English:** that feel like they're built into the built into the compiler without having to be what does it  
**Translation:** 

**[2708.42s] English:** mean for the int to be part of not hard-coded in so is it like how so what isn't what is an int  
**Translation:** 

**[2717.94s] English:** okay int is just a integer in this case it's like a you know like a 64-bit integer or something like  
**Translation:** Vocabulary: integer: 整数

**[2724.00s] English:** that  
**Translation:** 

**[2724.08s] English:** but so like the 64-bit is hard-coded or no no none of that's hard-coded so int int if you go look at  
**Translation:** 

**[2731.14s] English:** how it's implemented it's just a struct in swift and so it's a struct and then how do you add two  
**Translation:** 

**[2737.02s] English:** structs well you define plus and so you can define plus on int well you can define plus on your thing  
**Translation:** Vocabulary: struct: 结构体

**[2743.08s] English:** too you can define uh int has like an is odd method or something like that on it and so yeah  
**Translation:** 

**[2748.30s] English:** you can add methods onto things yeah uh so you can you can define operators like how it would be  
**Translation:** 

**[2754.66s] English:** yeah yeah that's used beautiful when there's something about the language which enables  
**Translation:** 

**[2759.68s] English:** other  
**Translation:** 

**[2760.00s] English:** Others to create libraries which are not hacky.  
**Translation:** 

**[2765.38s] English:** Yeah, they feel native.  
**Translation:** 

**[2767.32s] English:** And so one of the best examples of this is Lisp, right?  
**Translation:** 

**[2770.80s] English:** Because in Lisp, all the libraries are basically part of the language, right?  
**Translation:** 

**[2775.40s] English:** You write term rewrite systems and things like this.  
**Translation:** 

**[2777.48s] English:** Can you, as a counterexample, provide what makes it difficult to write a library that's native?  
**Translation:** Vocabulary: counterexample: 反例

**[2783.88s] English:** Is it the Python C?  
**Translation:** 

**[2785.52s] English:** Well, so one example, I'll give you two examples.  
**Translation:** 

**[2788.14s] English:** Java and C++, or Java and C, they both allow you to define your own types.  
**Translation:** 

**[2795.48s] English:** But int is hard-coded in the language.  
**Translation:** 

**[2798.44s] English:** Okay, well, why?  
**Translation:** 

**[2799.38s] English:** Well, in Java, for example, coming back to this whole reference semantic value semantic thing,  
**Translation:** Vocabulary: semantic: 语义的

**[2805.16s] English:** int gets passed around by value.  
**Translation:** 

**[2808.84s] English:** But if you make, like, a pair or something like that, a complex number, right,  
**Translation:** 

**[2815.04s] English:** it's a class in Java, and now it gets passed around by,  
**Translation:** 

**[2818.14s] English:** by reference, by pointer, and so now you lose value semantics, right?  
**Translation:** Vocabulary: semantics: 语义

**[2822.58s] English:** You lost math, okay?  
**Translation:** 

**[2824.88s] English:** Well, that's not great, right?  
**Translation:** 

**[2826.86s] English:** If you can do something with int, why can't I do it with my type?  
**Translation:** 

**[2830.24s] English:** Right, so that's the negative side of the thing I find beautiful,  
**Translation:** 

**[2835.00s] English:** is when you can solve that, when you can have full expressivity,  
**Translation:** 

**[2839.16s] English:** where you, as a user of the language, have as much or almost as much power  
**Translation:** 

**[2844.08s] English:** as the people who implemented all the standard built-in stuff.  
**Translation:** 

**[2846.78s] English:** Because what that enables is that it enables truly beautiful libraries.  
**Translation:** 

**[2851.42s] English:** You know, it's kind of weird, because I've gotten used to that.  
**Translation:** 

**[2855.96s] English:** That's one, I guess, other aspect of program language design.  
**Translation:** 

**[2859.10s] English:** You have to think, you know, the old first principles thinking,  
**Translation:** 

**[2863.48s] English:** like, why are we doing it this way?  
**Translation:** 

**[2865.42s] English:** By the way, I mean, I remember, because I was thinking about the Waller's operator,  
**Translation:** 

**[2871.00s] English:** and I'll ask you about it later,  
**Translation:** 

**[2873.64s] English:** but it hit me that, like, the equal sign,  
**Translation:** 

**[2876.62s] English:** for assignment, like, why are we using?  
**Translation:** 

**[2880.00s] English:** the equal sign it's wrong and that's not the only solution right so if you look at pascal they use  
**Translation:** 

**[2885.78s] English:** colon equals for assignment and equals for um for equality and they use like less than greater than  
**Translation:** Vocabulary: pascal: 帕斯卡语言

**[2892.94s] English:** instead of the not equal yeah like there are other answers here so but like and yeah like i ask you  
**Translation:** 

**[2899.12s] English:** all but how do you then decide uh to break convention to say you know what this everybody's  
**Translation:** 

**[2908.48s] English:** doing it wrong we're gonna do it right yeah so so it's like an roi like return on investment  
**Translation:** 

**[2914.68s] English:** trade-off right so if you do something weird let's just say like not like colon equal instead of equal  
**Translation:** 

**[2920.40s] English:** for assignment that would be weird with today's aesthetic right and so you'd say cool this is  
**Translation:** 

**[2926.40s] English:** theoretically better but is it better in which ways like what do i get out of that do i define  
**Translation:** Vocabulary: aesthetic: 审美; theoretically: 理论上

**[2931.26s] English:** away class of bugs well one of the class of bugs that c has is that you can use like you know if  
**Translation:** 

**[2936.22s] English:** x equals without equals  
**Translation:** 

**[2938.48s] English:** equals f x equals y yeah right well turns out you can solve that problem in lots of ways  
**Translation:** 

**[2944.98s] English:** clang for example gcc all these compilers will detect that as a as a likely bug produce a  
**Translation:** Vocabulary: clang: 编译器; compilers: 编译器

**[2950.16s] English:** warning do they yeah i feel like they didn't or clang gcc didn't and it's like one of the  
**Translation:** 

**[2957.30s] English:** important things about programming language design is like you're literally creating suffering in the  
**Translation:** 

**[2962.26s] English:** world okay like like i feel like i mean one way to see it is the bicycle  
**Translation:** 

**[2968.48s] English:** for the mind but the other way is to like minimizing suffering well you have to decide if  
**Translation:** Vocabulary: minimizing: 减少

**[2972.90s] English:** it's worth it right and so let's come back to that okay but um but if you if you look at this and  
**Translation:** 

**[2978.10s] English:** again this is where there's a lot of detail that goes into each of these things um uh equal and c  
**Translation:** 

**[2983.62s] English:** returns a value yep that's messed up that allows you to say x equals y equals z like that works  
**Translation:** 

**[2991.66s] English:** yeah um is it messed up you know well so that most people think it's messed up i think uh it is  
**Translation:** 

**[2998.48s] English:** very by messed up  
**Translation:** 

**[3000.00s] English:** what i mean is it is very rarely used for good and it's often used for bugs yeah right and so  
**Translation:** 

**[3006.72s] English:** that's a good definition yeah you could use you know it's it's a in hindsight this was not such  
**Translation:** 

**[3012.64s] English:** a great idea right now one of the things with swift that is really powerful and one of the  
**Translation:** Vocabulary: hindsight: 事后诸葛

**[3016.42s] English:** reasons it's actually good um versus it being full of good ideas is that um when when we launched  
**Translation:** 

**[3022.90s] English:** swift one we announced that it was public people could use it people could build apps but it was  
**Translation:** 

**[3028.22s] English:** going to change and break okay when swift 2 came out we said hey it's open source and there's this  
**Translation:** 

**[3033.66s] English:** open process which people can uh help evolve and direct the language so the community at large  
**Translation:** 

**[3039.30s] English:** like swift users can now help shape the language as it is and what happened is that part as part  
**Translation:** 

**[3045.12s] English:** of that process is a lot of really bad mistakes got taken out so for example swift used to have  
**Translation:** 

**[3051.34s] English:** the c style plus plus and minus minus operators like what does it mean when you put it before  
**Translation:** 

**[3056.42s] English:** versus after  
**Translation:** 

**[3057.26s] English:** right well that got cargo culted from c into swift early on what's cargo culted cargo culted  
**Translation:** 

**[3064.24s] English:** means uh brought forward without really considering considering it okay um this is maybe not the most  
**Translation:** 

**[3070.22s] English:** pc term but i have to look it up in urban dictionary yeah yeah so it got pulled it got  
**Translation:** 

**[3075.46s] English:** pulled into c without or it got pulled into swift without very good consideration and we went through  
**Translation:** 

**[3081.30s] English:** this process and one of the first things got ripped out was plus plus and minus minus because  
**Translation:** 

**[3085.82s] English:** they lead to confusion  
**Translation:** 

**[3087.26s] English:** they have very little value over saying you know x plus equals one and x plus equals one is way more  
**Translation:** 

**[3093.14s] English:** clear and so when you're optimizing for teachability and clarity and bugs and this  
**Translation:** Vocabulary: optimizing: 优化

**[3098.26s] English:** multi-dimensional space that you're looking at um things like that really matter and so being  
**Translation:** 

**[3102.94s] English:** first principles on where you're coming from and what you're trying to achieve and being anchored  
**Translation:** Vocabulary: anchored: 根基牢固

**[3107.18s] English:** on the objective is really important well let me ask you about uh the most uh sort of this this uh  
**Translation:** 

**[3115.90s] English:** this this podcast isn't a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a  
**Translation:** 

**[3117.26s] English:** podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast it's a podcast  
**Translation:** 

**[3120.00s] English:** talking about some drama so you mentioned pascal and colon equals uh there's something that's  
**Translation:** 

**[3127.34s] English:** called the walrus operator okay and python in python 3.8 added the walrus operator and the  
**Translation:** 

**[3135.90s] English:** reason i think it's interesting uh it's not just because of the feature it does it's it has the  
**Translation:** Vocabulary: walrus: 海象

**[3141.82s] English:** same kind of expression feature you can mention to see that it returns the value of the assignment  
**Translation:** 

**[3146.50s] English:** and maybe you can comment on that in general but on the other side of it it's also the thing that  
**Translation:** 

**[3153.10s] English:** that uh toppled the dictator uh so okay it finally drove guido to uh step down from edfl the toxicity  
**Translation:** 

**[3161.80s] English:** of the community so maybe um what do you think about the walrus operator in in python is there  
**Translation:** Vocabulary: dictator: 独裁者; toppled: 推翻; toxicity: 毒化

**[3167.22s] English:** an equivalent thing in swift that really uh stress tested the community and uh and then on the flip  
**Translation:** 

**[3176.36s] English:** side of the coin uh what do you think about the walrus operator in python is there an equivalent  
**Translation:** 

**[3176.48s] English:** what do you think about guido stepping down over it yeah well if like if i look past the details of  
**Translation:** 

**[3181.22s] English:** the walrus walrus operator one of the things that makes it most polarizing is that it's  
**Translation:** Vocabulary: guido: 吉多; polarizing: 极化

**[3184.62s] English:** syntactic sugar okay what do you mean by syntactic sugar it means you can take something that already  
**Translation:** 

**[3190.92s] English:** exists in language and you can express it in a more concise way so okay i'm gonna play dollars  
**Translation:** Vocabulary: concise: 简洁; syntactic: 语法

**[3195.54s] English:** advocate so uh this is great uh is that an objective or subjective statement like can you  
**Translation:** 

**[3202.56s] English:** can you argue that basically anything isn't syntactic sugar or not uh  
**Translation:** Vocabulary: advocate: 提倡者

**[3206.48s] English:** you know you not everything is a syntactic sugar so for example um the type system like can you  
**Translation:** 

**[3213.24s] English:** have classes versus uh versus uh like do you have types or not right so so one type versus many  
**Translation:** 

**[3221.38s] English:** types is not something that affects syntactic sugar and so if you say i want to have the ability  
**Translation:** 

**[3226.90s] English:** to define types i have to have all this like language mechanics to define classes and oh now  
**Translation:** 

**[3231.98s] English:** i have to have inheritance and i have like i have all this stuff that's just making language more  
**Translation:** 

**[3235.86s] English:** complicated  
**Translation:** Vocabulary: inheritance: 遗产

**[3236.48s] English:** that's not that's not about sugaring it  
**Translation:** 

**[3240.00s] English:** um swift has sugar so like swift has this thing called if let and it has various operators that  
**Translation:** 

**[3246.60s] English:** are used to concisify specific use cases so the problem with syntactic sugar when you're talking  
**Translation:** 

**[3253.28s] English:** about hey i have a thing that takes a lot to write and i have a new way to write it you have this  
**Translation:** Vocabulary: concisify: 简化表达

**[3258.16s] English:** like horrible trade-off which becomes almost completely subjective which is how often does  
**Translation:** 

**[3264.10s] English:** this happen and does it matter and one of the things that is true about human psychology  
**Translation:** 

**[3268.36s] English:** particularly when you're talking about introducing a new thing is that uh people over overestimate  
**Translation:** 

**[3274.04s] English:** the burden of learning something and so it looks foreign when you haven't gotten used to it but if  
**Translation:** Vocabulary: overestimate: 高估

**[3279.06s] English:** it was there from the beginning of course it's just part of python like unquestionably like this  
**Translation:** 

**[3283.38s] English:** is this is just the thing i know and it's not a new thing that you're worried about learning it's  
**Translation:** 

**[3287.76s] English:** just part of part of the deal now with guido uh i don't know guido well um yeah have you passed  
**Translation:** 

**[3296.28s] English:** across much yeah i've met him a couple of times but  
**Translation:** 

**[3298.36s] English:** i don't know guido well but the the sense that i got out of that whole dynamic was that he had put  
**Translation:** 

**[3304.38s] English:** the not just the decision maker weight on his shoulders but it was so tied to his personal  
**Translation:** 

**[3310.90s] English:** identity that um he took it personally and he felt the need and he kind of put himself in the  
**Translation:** 

**[3316.02s] English:** situation of being the person instead of building a base of support around him i mean he this is  
**Translation:** 

**[3322.02s] English:** probably not quite literally true but by too much so there's too much too much concentrated on him  
**Translation:** 

**[3328.36s] English:** right and so and that can wear you down well yeah particularly because people then say guido you're  
**Translation:** Vocabulary: guido: 朱利奥

**[3334.54s] English:** a horrible person i hate this thing blah blah blah blah blah blah blah and sure it's like you know  
**Translation:** 

**[3338.70s] English:** maybe one percent of the community that's doing that but python's got a big community and one  
**Translation:** 

**[3343.86s] English:** percent of it of millions of people is a lot of hate mail and that just from human factor will  
**Translation:** 

**[3348.66s] English:** just wear on you well to to clarify it looked from just what i saw in the messaging for the  
**Translation:** 

**[3353.84s] English:** let's not look at the million python users but at the python core developers  
**Translation:** 

**[3358.36s] English:** it feels like the majority  
**Translation:** 

**[3360.00s] English:** the big majority on a vote were opposed to it okay i'm not that close to it so i don't know  
**Translation:** 

**[3366.24s] English:** so this okay so the situation is like literally uh yeah i mean the majority the core developers  
**Translation:** 

**[3373.04s] English:** again were opposed so i and they weren't they weren't even like against it it was uh there  
**Translation:** 

**[3381.60s] English:** was a few well they were against it but the the against it wasn't like this is a bad idea  
**Translation:** 

**[3387.60s] English:** they were more like we don't see why this is a good idea and what that results in is there's  
**Translation:** 

**[3393.44s] English:** a stalling feeling like you you just slow things down now from my perspective now you could argue  
**Translation:** Vocabulary: stalling: 拖延

**[3401.20s] English:** this and i think it's a very it's very interesting if we look at politics today and the way congress  
**Translation:** 

**[3407.20s] English:** works it's slowed down everything it's a dampener yeah it's a dampener but like that's a dangerous  
**Translation:** Vocabulary: dampener: 抑制剂

**[3412.88s] English:** thing too because if it dampens things like you know  
**Translation:** 

**[3417.60s] English:** the dampening results what are you talking about like it's a low-pass filter but if you need  
**Translation:** Vocabulary: dampening: 减振效果

**[3421.28s] English:** billions of dollars injected into the economy or trillions of dollars then suddenly stuff happens  
**Translation:** 

**[3426.48s] English:** right and so for sure so you're not i'm not i'm not defending our political situation just to be  
**Translation:** Vocabulary: trillions: 万亿

**[3432.24s] English:** clear but you're talking about like a global pandemic well i was hoping we could fix like  
**Translation:** 

**[3438.96s] English:** the healthcare system and the education system like you know uh i'm not i'm not a politics  
**Translation:** Vocabulary: healthcare: 医疗体系; pandemic: 全球疫情

**[3444.24s] English:** person i don't i don't i don't know um when it comes to languages  
**Translation:** 

**[3448.00s] English:** the community is kind of right in terms of it's a very high burden to add something to a language  
**Translation:** 

**[3453.04s] English:** so as soon as you add something you have a community of people building on it and you can't  
**Translation:** 

**[3456.32s] English:** remove it okay and if there's a community of people that feel really uncomfortable with it  
**Translation:** 

**[3461.44s] English:** then taking it slow i think is is is an important thing to do and there's no rush particularly if  
**Translation:** 

**[3467.44s] English:** with something that's 25 years old and is very established and you know it's not like coming  
**Translation:** 

**[3472.16s] English:** coming into its own um what about features well so i think that the issue with  
**Translation:** 

**[3477.60s] English:** with guido is that maybe this is  
**Translation:** 

**[3480.00s] English:** a case where he realized it had outgrown him and it went from being or the language the language  
**Translation:** 

**[3485.82s] English:** so python i mean guido is amazing but but python isn't about guido anymore it's about the users  
**Translation:** Vocabulary: guido: 古德罗

**[3493.02s] English:** and to a certain extent the users own it and you know guido spent years of his life a significant  
**Translation:** 

**[3500.26s] English:** fraction of his career on python and from his perspective i imagine he's like well this is my  
**Translation:** 

**[3505.50s] English:** thing i should be able to do the thing i think is right but you can also understand the users  
**Translation:** 

**[3510.06s] English:** where they feel like you know this is my thing i use this like and um and i don't know it's it's  
**Translation:** 

**[3517.10s] English:** a hard it's a hard thing but what if we could talk about leadership in this because it's so  
**Translation:** 

**[3521.70s] English:** interesting to me i'm gonna i'm gonna make i'm gonna work hopefully somebody makes it if not  
**Translation:** 

**[3525.80s] English:** i'll make it a walrus operator shirt because i think it represents to me maybe it's my russian  
**Translation:** 

**[3531.22s] English:** roots or something uh you know it's the burden of  
**Translation:** Vocabulary: walrus: 海象

**[3535.38s] English:** leadership  
**Translation:** 

**[3535.50s] English:** Like, I feel like to push back, I feel like progress can only, like most difficult decisions, just like you said, there'll be a lot of divisiveness over, especially in the passionate community.  
**Translation:** Vocabulary: divisiveness: 分裂倾向

**[3550.94s] English:** It just feels like leaders need to take those risky decisions that if you, like, listen, that with some non-zero probability, maybe even a high probability would be the wrong decision.  
**Translation:** 

**[3565.84s] English:** But they have to use their gut and make that decision.  
**Translation:** 

**[3568.86s] English:** Well, this is like one of the things where you see amazing founders.  
**Translation:** 

**[3574.12s] English:** The founders understand exactly what's happened and how the company got there and are willing to say, we have been doing thing X.  
**Translation:** Vocabulary: founders: 创始团队

**[3580.94s] English:** The last 20 years.  
**Translation:** 

**[3582.80s] English:** But today, we're going to do thing Y.  
**Translation:** 

**[3585.18s] English:** And they make a major pivot for the whole company.  
**Translation:** 

**[3587.40s] English:** The company lines up behind them.  
**Translation:** 

**[3588.60s] English:** They move, and it's the right thing.  
**Translation:** 

**[3590.48s] English:** But then when the founder dies, the successor doesn't always feel that agency to be able to make those kinds of decisions.  
**Translation:** 

**[3598.90s] English:** Even though they're the CEO.  
**Translation:** 

**[3600.00s] English:** they could theoretically do whatever there's two reasons for that in my opinion or in many cases  
**Translation:** Vocabulary: theoretically: 理论上

**[3606.16s] English:** it's always different but um one of which is they weren't there for all the decisions that were made  
**Translation:** 

**[3610.94s] English:** and so they don't know the principles in which those decisions were made and once the principles  
**Translation:** 

**[3616.20s] English:** change you're you should be obligated to change what you're doing and change direction right and  
**Translation:** 

**[3622.82s] English:** so if you don't know how you got to where you are it just seems like gospel and you know you're not  
**Translation:** Vocabulary: gospel: 金科玉律; obligated: 有责任

**[3628.76s] English:** going to question it you may not understand that it really is the right thing to do so you just may  
**Translation:** 

**[3632.92s] English:** not see it that's so brilliant i never thought of it that way like this it's so much higher burden  
**Translation:** 

**[3638.12s] English:** when as a leader you step into a thing that's already worked for a long time yeah yeah well  
**Translation:** 

**[3642.64s] English:** and if you change it and it doesn't work out now you're the person who screwed it up people always  
**Translation:** 

**[3646.78s] English:** second guess that yeah and the second thing is that even if you decide to make a change even if  
**Translation:** 

**[3651.40s] English:** you're theoretically in charge you're just you're just a person that thinks they're in charge  
**Translation:** 

**[3657.02s] English:** meanwhile you have to motivate the troops  
**Translation:** 

**[3658.76s] English:** you have to explain it to them in terms of understand you have to get them to buy into  
**Translation:** 

**[3661.46s] English:** and believe in it because if they don't then they're not going to be able to make the turn  
**Translation:** 

**[3665.82s] English:** even if you tell them you know their bonuses are going to be curtailed they're just not going to  
**Translation:** 

**[3668.98s] English:** like buy into it you know and so there's only so much power you have as a leader and you have to  
**Translation:** 

**[3673.88s] English:** understand what that what those limitations are are you still bdfl you've been a bdfl of some stuff  
**Translation:** 

**[3680.04s] English:** uh you're very heavy on the b the benevolent uh benevolent dictator for life uh i guess lvm  
**Translation:** 

**[3688.76s] English:** yeah so i still lead the lvm world uh i mean what's the role of uh so then on swift you said  
**Translation:** Vocabulary: benevolent: 仁慈的; dictator: 独裁者

**[3696.68s] English:** that there's a group of people yeah so if you contrast python with swift right one of the  
**Translation:** 

**[3702.12s] English:** reasons so everybody on the core team takes the role really seriously and i think we all really  
**Translation:** 

**[3707.30s] English:** care about where swift goes but you're almost delegating the final decision making to the  
**Translation:** 

**[3713.20s] English:** wisdom of the group and so it doesn't become personal and also when you're talking about the  
**Translation:** 

**[3718.76s] English:** with the community so  
**Translation:** 

**[3720.00s] English:** yeah, some people are very annoyed at certain decisions that get made.  
**Translation:** 

**[3724.06s] English:** There's a certain faith in the process because it's a very transparent process.  
**Translation:** 

**[3728.24s] English:** And when a decision gets made, a full rationale is provided, things like this.  
**Translation:** 

**[3732.20s] English:** These are almost defense mechanisms to help both guide future discussions and provide  
**Translation:** 

**[3736.86s] English:** case law, kind of like the Supreme Court does, about this decision was made for this reason,  
**Translation:** 

**[3740.96s] English:** and here's the rationale and what we want to see more of or less of.  
**Translation:** 

**[3745.22s] English:** But it's also a way to provide a defense mechanism so that when somebody's griping about it,  
**Translation:** 

**[3749.00s] English:** they're not saying, that person did the wrong thing.  
**Translation:** 

**[3751.80s] English:** They're saying, well, this thing sucks, and later they move on and they get over it.  
**Translation:** 

**[3758.46s] English:** Yeah, the analogy of the Supreme Court, I think, is really good.  
**Translation:** 

**[3762.76s] English:** But then, okay, not to get personal on the Swift team, but it just seems like it's impossible  
**Translation:** 

**[3769.16s] English:** for division not to emerge.  
**Translation:** 

**[3772.76s] English:** Well, each of the humans on the Swift core team, for example, are different, and the  
**Translation:** 

**[3777.26s] English:** membership of the Swift core team changes.  
**Translation:** 

**[3779.00s] English:** Slowly, over time, which is, I think, a healthy thing.  
**Translation:** 

**[3782.60s] English:** And so each of these different humans have different opinions.  
**Translation:** 

**[3785.24s] English:** Trust me, it's not a singular consciousness by any stretch of the imagination.  
**Translation:** 

**[3791.00s] English:** You've got three major organizations, including Apple, Google, and Sci-5, all kind of working  
**Translation:** 

**[3795.78s] English:** together, and it's a small group of people, but you need high trust.  
**Translation:** 

**[3800.06s] English:** Again, it comes back to the principles of what you're trying to achieve and understanding  
**Translation:** 

**[3804.40s] English:** what you're optimizing for.  
**Translation:** Vocabulary: optimizing: 优化

**[3807.76s] English:** And I think that...  
**Translation:** 

**[3809.00s] English:** Starting with strong principles and working towards decisions is always a good way to  
**Translation:** 

**[3813.40s] English:** both make wise decisions in general, but then be able to communicate them to people so that  
**Translation:** 

**[3818.14s] English:** they can buy into them.  
**Translation:** 

**[3819.40s] English:** And that is hard.  
**Translation:** 

**[3821.42s] English:** And so you mentioned LLVM.  
**Translation:** 

**[3822.64s] English:** LLVM is going to be 20 years old this December, so it's showing its own age.  
**Translation:** 

**[3829.46s] English:** Do you have like a dragon cake plan?  
**Translation:** Vocabulary: dragon: 龙蛋糕

**[3833.12s] English:** No, we should definitely do that.  
**Translation:** 

**[3834.70s] English:** Yeah, if we can have a pandemic cake.  
**Translation:** Vocabulary: pandemic: 全球大流行

**[3838.08s] English:** Pandemic cake.  
**Translation:** 

**[3838.88s] English:** Pandemic cake.  
**Translation:** 

**[3839.00s] English:** Everybody gets a slice of cake.  
**Translation:** 

**[3840.00s] English:** it gets you know sent through email um but the uh uh but lvm has had tons of its own challenges  
**Translation:** 

**[3848.04s] English:** over time too right and one of the challenges that um the lvm community has in my opinion is  
**Translation:** 

**[3853.44s] English:** that it has a whole bunch of people that have been working on lvm for 10 years right because  
**Translation:** 

**[3859.16s] English:** this happens somehow and lvm has always been one way but it needs to be a different way  
**Translation:** 

**[3863.68s] English:** right and they've worked on it for like 10 years is a long time to work on something  
**Translation:** 

**[3867.92s] English:** and you know you suddenly can't see the faults in the thing that you're working on and lvm has  
**Translation:** 

**[3874.04s] English:** lots of problems and we need to address them and we need to make it better and if we don't make  
**Translation:** 

**[3877.26s] English:** it better then somebody else will come up with a better idea right and so it's just kind of of  
**Translation:** 

**[3881.96s] English:** that age where the community is like in danger of getting too calcified and um and so i'm happy to  
**Translation:** Vocabulary: calcified: 僵化

**[3889.10s] English:** see new projects joining and new things mixing it up you know fortran is now a new a new thing  
**Translation:** 

**[3893.66s] English:** in the lvm community which is hilarious and good i've been trying to find uh and there's  
**Translation:** 

**[3897.92s] English:** a little tangent find people who program in cobalt or fortran fortran especially to talk to  
**Translation:** 

**[3904.70s] English:** they're hard to find yeah yeah look to the uh scientific community they still use fortran quite  
**Translation:** Vocabulary: cobalt: 合金; tangent: 旁枝

**[3910.78s] English:** a bit well interesting thing you kind of mentioned with lvm or just in general that as something  
**Translation:** 

**[3916.38s] English:** evolved you're not able to see the faults so do you uh fall in love with the thing over time or  
**Translation:** 

**[3923.20s] English:** do you start hating everything about the thing over time well so so my my personal  
**Translation:** 

**[3927.92s] English:** folly is that um i see maybe not all but many of the faults and they grate on me and i don't have  
**Translation:** Vocabulary: grate: 磨炼

**[3934.70s] English:** time to go fix them yeah and they get magnified over time and well and they may not get magnified  
**Translation:** 

**[3938.82s] English:** but they never get fixed it's like sand underneath you know it's just like grating against you and  
**Translation:** Vocabulary: grating: 刺耳; magnified: 放大

**[3943.70s] English:** it's like sand underneath your fingernails or something it's just like you know it's there  
**Translation:** 

**[3946.84s] English:** you can't get rid of it um and so the the problem is that if other people don't see it right nobody  
**Translation:** Vocabulary: fingernails: 指甲

**[3954.32s] English:** ever get like i can't go i don't have time to go write the code and fix it anymore  
**Translation:** 

**[3957.92s] English:** but then uh people resist  
**Translation:** 

**[3960.00s] English:** into change and so you say hey we should go fix this thing they're like oh yeah that sounds risky  
**Translation:** 

**[3964.68s] English:** well is it the right thing or not are the challenges uh the the group dynamics or is  
**Translation:** 

**[3970.42s] English:** it also just technical i mean some of these features like yeah i think uh as an observer  
**Translation:** 

**[3976.02s] English:** is almost like a fan in in the uh you know as a spectator of the whole thing it i don't often  
**Translation:** Vocabulary: observer: 观察者

**[3982.90s] English:** think about you know some things might actually be technically difficult to implement an example  
**Translation:** 

**[3987.96s] English:** this is we we built this new compiler framework called mlir yes mlir is this a whole new framework  
**Translation:** 

**[3993.62s] English:** it's not many people think it's about machine learning the ml stands for multi-level because  
**Translation:** 

**[3999.48s] English:** compiler people can't name things very well i guess can we dig into what mlir is yeah so when  
**Translation:** 

**[4006.18s] English:** you look at compilers compilers have historically been solutions for a given space so lvm is a it's  
**Translation:** 

**[4014.86s] English:** really good for dealing with cpus let's just say at a high level  
**Translation:** Vocabulary: compilers: 编译器; historically: 历史上

**[4017.96s] English:** you look at um java java has a jvm the jvm is very good for garbage collected languages that need  
**Translation:** 

**[4024.52s] English:** dynamic compilation and it's very optimized for specific space and so hotspot is one of the  
**Translation:** Vocabulary: compilation: 编译; optimized: 优化

**[4029.48s] English:** compilers that gets used in that space and that compiler is really good at that kind of stuff  
**Translation:** 

**[4032.68s] English:** um usually when you build these domain specific compilers you end up building the whole thing  
**Translation:** 

**[4038.02s] English:** from scratch for each domain uh what's the domain so what what's the what's the scope of a domain  
**Translation:** 

**[4047.96s] English:** like if you look at swift there's several different parts to the swift compiler  
**Translation:** 

**[4051.34s] English:** one of which is covered by um the lvm part of it there's also a high level piece that's specific  
**Translation:** 

**[4058.26s] English:** to swift and there's a huge amount of redundancy between those two different infrastructures and a  
**Translation:** Vocabulary: infrastructures: 基础设施; redundancy: 冗余

**[4064.28s] English:** lot of re-implemented stuff that is similar but different what is lvm defined lvm is effectively  
**Translation:** 

**[4071.40s] English:** an infrastructure so you can mix and match it in different ways it's built out of libraries you can  
**Translation:** 

**[4076.28s] English:** use it for different things but it's really a high level piece that's specific to swift and it's  
**Translation:** 

**[4077.96s] English:** really good at cpus and gpus  
**Translation:** 

**[4080.00s] English:** GPUs and like the tip of the iceberg on GPUs.  
**Translation:** 

**[4082.50s] English:** It's not really great at GPUs.  
**Translation:** Vocabulary: iceberg: 冰山一角

**[4084.40s] English:** Okay.  
**Translation:** 

**[4085.56s] English:** But it turns out languages that then use it to talk to CPUs.  
**Translation:** 

**[4090.18s] English:** Got it.  
**Translation:** 

**[4090.78s] English:** And so it turns out there's a lot of hardware out there that is custom accelerators.  
**Translation:** Vocabulary: accelerators: 专用加速器

**[4094.86s] English:** So machine learning, for example, there are a lot of matrix multiply accelerators and things like this.  
**Translation:** 

**[4100.36s] English:** There's a whole world of hardware synthesis.  
**Translation:** Vocabulary: matrix: 矩阵; multiply: 乘法; synthesis: 合成

**[4102.76s] English:** So we're using MLIR to build circuits.  
**Translation:** 

**[4106.40s] English:** Okay.  
**Translation:** Vocabulary: circuits: 电路

**[4106.80s] English:** And so you're compiling for a domain of transistors.  
**Translation:** 

**[4110.92s] English:** And so what MLIR does is it provides a tremendous amount of compiler infrastructure that allows you to build these domain-specific compilers in a much faster way and have the result be good.  
**Translation:** Vocabulary: compiling: 编译; transistors: 晶体管

**[4121.68s] English:** If we're thinking about the future, now we're talking about like ASICs, so anything.  
**Translation:** 

**[4126.86s] English:** Yeah, yeah.  
**Translation:** 

**[4127.28s] English:** So if we project into the future, it's very possible that the number of these kinds of ASICs, very specific infrastructure thing.  
**Translation:** 

**[4139.66s] English:** The architecture things, like, multiplies exponentially.  
**Translation:** Vocabulary: exponentially: 成倍增长; multiplies: 增加

**[4145.30s] English:** I hope so, yeah.  
**Translation:** 

**[4146.32s] English:** So that's MLIR.  
**Translation:** 

**[4148.42s] English:** So what MLIR does is it allows you to build these compilers very efficiently.  
**Translation:** 

**[4153.28s] English:** Right.  
**Translation:** Vocabulary: compilers: 编译器; efficiently: 高效地

**[4153.50s] English:** Now, one of the things that, coming back to the LLVM thing, and then we'll go to hardware, is LLVM is a specific compiler for a specific domain.  
**Translation:** 

**[4164.04s] English:** MLIR is now this very general, very flexible thing that can solve lots of different kinds of problems.  
**Translation:** 

**[4168.68s] English:** So LLVM is a subset of what MLIR does.  
**Translation:** 

**[4172.50s] English:** So MLIR is, I mean, it's an ambitious project then.  
**Translation:** 

**[4175.30s] English:** Yeah, it's a very ambitious project, yeah.  
**Translation:** 

**[4177.04s] English:** And so to make it even more confusing, MLIR has joined the LLVM umbrella project, so it's part of the LLVM family.  
**Translation:** 

**[4184.30s] English:** Right.  
**Translation:** 

**[4185.00s] English:** But where this comes full circle is now folks that work on the LLVM part, the classic part that's 20 years old, aren't aware of all the cool new things that have been done and the new thing that, you know, MLIR was built by me.  
**Translation:** 

**[4198.32s] English:** Right.  
**Translation:** 

**[4198.64s] English:** Right.  
**Translation:** 

**[4198.68s] English:** And many other people that...  
**Translation:** 

**[4200.00s] English:** knew a lot about LLVM. And so we fixed a lot of the mistakes that lived in LLVM.  
**Translation:** 

**[4205.14s] English:** And so now you have this community dynamic where it's like, well, there's this new thing,  
**Translation:** 

**[4208.44s] English:** but it's not familiar. Nobody knows it. It feels like it's new. And so let's not trust it. And so  
**Translation:** 

**[4212.98s] English:** it's just really interesting to see the cultural social dynamic that comes out of that. And I think  
**Translation:** 

**[4218.32s] English:** it's super healthy because we're seeing the ideas percolate and we're seeing the technology diffusion  
**Translation:** Vocabulary: diffusion: 扩散; percolate: 渗透

**[4222.98s] English:** happen as people get more comfortable with it. They start to understand things in their own terms.  
**Translation:** 

**[4227.04s] English:** And it takes a while for ideas to propagate, even though they may be very different than what  
**Translation:** Vocabulary: propagate: 传播

**[4234.16s] English:** people are used to. So maybe let's talk about that a little bit, the world of ASICs. Well,  
**Translation:** 

**[4239.08s] English:** actually, you have a new role at SciFive. What's that place about? What is the vision  
**Translation:** 

**[4248.08s] English:** for their vision for, I would say, the future of computing?  
**Translation:** 

**[4252.96s] English:** So I lead the engineering and product teams at SciFive. SciFive is,  
**Translation:** 

**[4257.04s] English:** a company who was founded with this architecture called RISC-V. RISC-V is a new instruction set.  
**Translation:** 

**[4264.44s] English:** Instruction sets are the things inside of your computer that tell it how to run things.  
**Translation:** 

**[4268.46s] English:** x86 from Intel and ARM from the ARM company and things like this are other instruction sets.  
**Translation:** 

**[4273.84s] English:** I've talked to, sorry to interrupt, I've talked to Dave Patterson, who's super excited about RISC-V.  
**Translation:** Vocabulary: patterson: 帕特森

**[4277.78s] English:** Dave is awesome.  
**Translation:** 

**[4278.88s] English:** Yeah, he's brilliant.  
**Translation:** 

**[4279.66s] English:** Yeah. The RISC-V is distinguished by not being proprietary.  
**Translation:** 

**[4284.68s] English:** And so x86 can only be...  
**Translation:** Vocabulary: proprietary: 私有产权的

**[4287.04s] English:** made by Intel and AMD. ARM can only be made by ARM. They sell licenses to build ARM chips to other  
**Translation:** 

**[4292.86s] English:** companies, things like this. MIPS is another instruction set that is owned by the MIPS company,  
**Translation:** 

**[4297.44s] English:** Now Wave, and then it gets licensed out, things like that. And so RISC-V is an open standard that  
**Translation:** 

**[4303.48s] English:** anybody can build chips for. And so SciFive was founded by three of the founders of RISC-V that  
**Translation:** Vocabulary: founders: 创立者

**[4309.60s] English:** designed and built it in Berkeley, working with Dave. And so that was the genesis of the company.  
**Translation:** 

**[4316.46s] English:** So I've had a lot of experience with RISC-V. I've had a lot of experience with RISC-V.  
**Translation:** Vocabulary: berkeley: 伯克利

**[4317.02s] English:** I've had a lot of experience with RISC-V. I've had a lot of experience with RISC-V. I've had a lot of experience with RISC-V.  
**Translation:** 

**[4317.04s] English:** I've today had some of the world's best RISC-V cores, and we're...  
**Translation:** 

**[4320.00s] English:** selling them and that's really great they're going to tons of products it's very exciting  
**Translation:** 

**[4323.04s] English:** so they're taking this thing that's open source and just being trying to be or are the best in  
**Translation:** 

**[4329.10s] English:** the world at building these things yeah so here it's the specifications open source it's like  
**Translation:** 

**[4333.54s] English:** saying tcpip is an open standard or c is an open standard but then you have to build an  
**Translation:** Vocabulary: tcpip: 传输控制协议

**[4339.00s] English:** implementation of the standard and so sci-fi on the one hand pushes forward and defined and pushes  
**Translation:** 

**[4344.92s] English:** forward the standard on the other hand we have implementations that are best in class for  
**Translation:** Vocabulary: implementation: 实施方案; implementations: 实施例

**[4349.54s] English:** different points in the space depending on if you want a really tiny cpu or if you want a really  
**Translation:** 

**[4354.18s] English:** big beefy one that that uh is faster but it uses more area and things like this what about the  
**Translation:** Vocabulary: beefy: 体积大

**[4359.52s] English:** actual manufacturer which is so like what yeah so where does that all fit i'm gonna ask a bunch  
**Translation:** 

**[4364.64s] English:** of dumb questions that's okay this is how we learn right uh and so uh what the the way this  
**Translation:** 

**[4370.98s] English:** works is that there's generally a separation of the people who design the circuits and then  
**Translation:** 

**[4375.36s] English:** people who manufacture them and so that you'll hear about fabs like  
**Translation:** Vocabulary: circuits: 电路; manufacture: 制造

**[4379.34s] English:** tscp  
**Translation:** 

**[4379.54s] English:** smc and samsung and things like this that actually produce the chips but they take a  
**Translation:** 

**[4384.40s] English:** design coming in and that design specifies how um how the you know you turn uh code for the chip  
**Translation:** 

**[4393.24s] English:** into uh little rectangles that then use photolithography to make uh mask sets and  
**Translation:** Vocabulary: photolithography: 光刻技术; rectangles: 矩形图案; specifies: 规定

**[4400.34s] English:** then burn transistors onto a chip or onto onto silicon rather well so and we're talking about  
**Translation:** 

**[4406.22s] English:** mass manufacturing so yeah they're talking about making hundreds  
**Translation:** Vocabulary: transistors: 晶体管

**[4409.54s] English:** of millions of parts and things like that yeah and so the fab handles the volume production  
**Translation:** 

**[4413.44s] English:** things like that but um when you look at this problem um the interesting thing about the space  
**Translation:** 

**[4419.02s] English:** when you look at it is that um these the steps that you go from designing a chip and writing  
**Translation:** 

**[4424.74s] English:** the quote-unquote code for it and things like verilog and languages like that down to what  
**Translation:** 

**[4429.98s] English:** you hand off to the fab is a really well studied really old problem okay um tons of people have  
**Translation:** 

**[4437.06s] English:** worked on it lots of smart people have built systems and tools and things like that and so  
**Translation:** 

**[4439.54s] English:** we're going to talk a little bit more about that in a little bit more detail but i'm going to  
**Translation:** 

**[4440.00s] English:** These tools then have generally gone through acquisitions.  
**Translation:** Vocabulary: acquisitions: 收购

**[4443.50s] English:** And so they've ended up at three different major companies  
**Translation:** 

**[4446.18s] English:** that build and sell these tools.  
**Translation:** 

**[4447.80s] English:** They're called EDA tools,  
**Translation:** 

**[4448.98s] English:** like for electronic design automation.  
**Translation:** Vocabulary: automation: 自动化

**[4451.66s] English:** The problem with this is you have huge amounts  
**Translation:** 

**[4453.22s] English:** of fragmentation, you have loose standards,  
**Translation:** Vocabulary: fragmentation: 碎片化

**[4458.36s] English:** and the tools don't really work together.  
**Translation:** 

**[4460.04s] English:** So you have tons of duct tape  
**Translation:** 

**[4461.32s] English:** and you have tons of lost productivity.  
**Translation:** 

**[4464.24s] English:** Now, these are tools for designing.  
**Translation:** 

**[4466.74s] English:** So the RISC-V is an instruction,  
**Translation:** 

**[4470.26s] English:** like what is RISC-V?  
**Translation:** 

**[4472.06s] English:** Like how deep does it go?  
**Translation:** 

**[4473.22s] English:** How much does it touch the hardware?  
**Translation:** 

**[4475.92s] English:** How much does it define how much of the hardware is?  
**Translation:** 

**[4478.46s] English:** Yeah, so RISC-V is all about given a CPU,  
**Translation:** 

**[4481.90s] English:** so the processor and your computer,  
**Translation:** 

**[4484.88s] English:** how does the compiler, like the Swift compiler,  
**Translation:** 

**[4487.42s] English:** the C compiler, things like this,  
**Translation:** 

**[4488.94s] English:** how does it make it work?  
**Translation:** 

**[4490.48s] English:** So it's what is the assembly code?  
**Translation:** 

**[4492.68s] English:** And so you write RISC-V assembly  
**Translation:** 

**[4494.16s] English:** instead of X86 assembly, for example.  
**Translation:** 

**[4496.74s] English:** But it's a set of instructions  
**Translation:** 

**[4498.62s] English:** as opposed to...  
**Translation:** 

**[4499.46s] English:** A set of instructions, yeah.  
**Translation:** 

**[4500.30s] English:** What do you say?  
**Translation:** 

**[4501.12s] English:** It tells you how the compiler works.  
**Translation:** 

**[4503.68s] English:** Sorry, it's what the compiler talks to.  
**Translation:** 

**[4505.38s] English:** Okay.  
**Translation:** 

**[4506.22s] English:** Yeah.  
**Translation:** 

**[4507.06s] English:** And then the tooling you mentioned,  
**Translation:** 

**[4508.68s] English:** the disparate tools, are for what?  
**Translation:** 

**[4510.68s] English:** For when you're building a specific chip.  
**Translation:** Vocabulary: disparate: 不相同

**[4513.36s] English:** So RISC-V...  
**Translation:** 

**[4514.20s] English:** In hardware.  
**Translation:** 

**[4515.04s] English:** In hardware, yeah.  
**Translation:** 

**[4515.88s] English:** So RISC-V, you can buy a RISC-V core from Sci-5  
**Translation:** 

**[4519.12s] English:** and say, hey, I want to have a certain number of,  
**Translation:** 

**[4521.66s] English:** run a certain number of gigahertz,  
**Translation:** Vocabulary: gigahertz: 吉赫兹

**[4523.40s] English:** I want it to be this big,  
**Translation:** 

**[4524.68s] English:** I want it to be, have these features,  
**Translation:** 

**[4526.26s] English:** I want to have, like, I want floating point or not,  
**Translation:** 

**[4529.86s] English:** for example.  
**Translation:** 

**[4531.48s] English:** And then what you get is you get a description of a CPU  
**Translation:** 

**[4534.68s] English:** with those characteristics.  
**Translation:** 

**[4536.62s] English:** Now, if you want to make a chip,  
**Translation:** 

**[4538.16s] English:** you want to build, like, an iPhone chip  
**Translation:** 

**[4539.94s] English:** or something like that, right?  
**Translation:** 

**[4541.20s] English:** You have to take both the CPU,  
**Translation:** 

**[4542.74s] English:** but then you have to talk to memory,  
**Translation:** 

**[4544.40s] English:** you have to have timers, IOs, a GPU, other components.  
**Translation:** 

**[4549.30s] English:** And so you need to pull all those things together  
**Translation:** 

**[4551.40s] English:** into what's called an ASIC,  
**Translation:** 

**[4553.88s] English:** an application-specific integrated circuit,  
**Translation:** 

**[4555.50s] English:** so a custom chip.  
**Translation:** 

**[4556.26s] English:** And then you take that design  
**Translation:** 

**[4558.48s] English:** and then you have to transform it  
**Translation:** 

**[4560.00s] English:** into something that the fabs like tsmc for example know how to take to production got it  
**Translation:** 

**[4567.34s] English:** so but yeah okay and and so that process i will i can't help but see it is is a big compiler  
**Translation:** 

**[4575.00s] English:** yeah it's a whole bunch of compilers written without thinking about it through that lens  
**Translation:** 

**[4580.88s] English:** isn't the universe a compiler in that okay like compilers do two things they represent things  
**Translation:** Vocabulary: compilers: 编译器

**[4587.62s] English:** and transform them yeah and so there's a lot of things that end up being compilers yeah but this  
**Translation:** 

**[4592.16s] English:** is this is a space where we're talking about design and usability and the way you think about  
**Translation:** Vocabulary: usability: 易用性

**[4596.92s] English:** things the way things compose correctly it matters a lot and so sci-fi is investing a lot into that  
**Translation:** 

**[4602.96s] English:** space and we think there's a lot a lot of benefit that can be made by allowing people to design  
**Translation:** 

**[4607.78s] English:** ships faster get them to market quicker and scale out because you know at the alleged more end of  
**Translation:** 

**[4615.14s] English:** law uh you've got this problem  
**Translation:** Vocabulary: alleged: 指控的

**[4617.62s] English:** of uh you're not getting free performance just by waiting another year for a faster cpu  
**Translation:** 

**[4623.04s] English:** and so um you have to find performance in other ways and one of the ways to do that is with custom  
**Translation:** 

**[4628.30s] English:** accelerators and other things and hardware and and so well we'll talk a little about  
**Translation:** 

**[4634.00s] English:** a little more about asics but um do you see that a lot of people a lot of companies will try to  
**Translation:** 

**[4643.72s] English:** have a like different sets of requirements that this whole process  
**Translation:** 

**[4647.62s] English:** has to go for so like like almost different car companies might use different uh and like  
**Translation:** 

**[4653.00s] English:** different uh pc manufacturers like so is this like is risk five um in this whole process  
**Translation:** 

**[4660.50s] English:** is it potentially the future of all computing devices yeah i think that so if you look at risk  
**Translation:** Vocabulary: computing: 计算设备

**[4666.84s] English:** five and step back from the silicon side of things risk five is an open standard and one of the things  
**Translation:** 

**[4672.86s] English:** that has happened over the course of decades if you look over the long arc of computing  
**Translation:** 

**[4677.62s] English:** somehow became decades old yeah  
**Translation:** 

**[4680.00s] English:** that you have uh companies that come and go and you have instruction sets that come and go  
**Translation:** 

**[4684.16s] English:** like one example of this out of many is uh sun with spark yeah sun went away spark still lives  
**Translation:** 

**[4692.00s] English:** on at fujitsu but we have hp had this instruction set called pa risk so pa risk was this big server  
**Translation:** 

**[4700.24s] English:** business and had tons of customers they decided to move to this architecture called itanium from  
**Translation:** 

**[4706.48s] English:** intel yeah this didn't work out so well yeah right and so you have this issue of you're making  
**Translation:** 

**[4713.44s] English:** many billion dollar investments on instruction sets that are owned by a company and even  
**Translation:** 

**[4718.60s] English:** companies as big as intel don't always execute as well as they could they have their own issues  
**Translation:** 

**[4723.58s] English:** hp for example decided that it wasn't in their best interest to continue investing in the space  
**Translation:** 

**[4728.54s] English:** because it was very expensive and so they make technology decisions or product they make their  
**Translation:** 

**[4733.08s] English:** own business decisions and this means that as a customer  
**Translation:** 

**[4736.48s] English:** you do you've sunk all this time all this engineering all the software work all these  
**Translation:** 

**[4741.12s] English:** you've built other products around them and now you're stuck right what risk 5 does is provide you  
**Translation:** 

**[4746.64s] English:** more optionality in the space because if you buy an implementation of risk 5 from sci-fi and you  
**Translation:** Vocabulary: implementation: 实施方案; optionality: 选择权

**[4752.72s] English:** should they're the best ones yeah um but if something bad happens to sci-fi in 20 years  
**Translation:** 

**[4758.96s] English:** right well great you can turn around and buy a risk 5 core from somebody else  
**Translation:** 

**[4763.12s] English:** and there's an ecosystem of people that are all making different risk 5 cores  
**Translation:** 

**[4766.48s] English:** with different trade-offs which means that if you have more than one requirement if you have a  
**Translation:** 

**[4771.06s] English:** family of products you can probably find something in the risk 5 space that fits your needs whereas  
**Translation:** 

**[4776.34s] English:** with if you're talking about xa6 for example it's intel's only going to bother to make certain  
**Translation:** 

**[4781.96s] English:** classes of devices right i see so uh maybe a weird question but like if sci-fi is uh like  
**Translation:** 

**[4792.62s] English:** infinitely successful in the next 20-30 years what is the next 20-30 years  
**Translation:** Vocabulary: infinitely: 无穷地

**[4796.48s] English:** the world look like so like how does the world  
**Translation:** 

**[4800.00s] English:** of computing change so too much diversity in hardware instruction sets i think is bad  
**Translation:** Vocabulary: computing: 计算机领域

**[4806.10s] English:** like we have a lot of people that are using um lots of different instruction sets particularly  
**Translation:** 

**[4811.24s] English:** in the embedded the like very tiny microcontroller space the thing in your toaster um that uh that  
**Translation:** Vocabulary: embedded: 嵌入式; microcontroller: 微控制器

**[4818.32s] English:** are just weird and different for historical reasons and so the compilers and the tool chains  
**Translation:** 

**[4822.94s] English:** and the languages on top of them uh aren't there and so the developers for that software have to  
**Translation:** 

**[4829.50s] English:** use really weird tools because the ecosystem that supports is not big enough so i expect that will  
**Translation:** 

**[4834.92s] English:** change right people will have better tools and better languages better features everywhere  
**Translation:** 

**[4838.98s] English:** that then can service many different points in the space um and i think risk five will progressively  
**Translation:** 

**[4845.34s] English:** eat more of the ecosystem because it can scale up it can scale down sideways left right it's  
**Translation:** Vocabulary: progressively: 逐步地; sideways: 横向地

**[4851.76s] English:** very flexible and very well considered and well designed instruction set um i think when you look  
**Translation:** 

**[4856.98s] English:** at sci-fi of tackling silicon and how people build  
**Translation:** Vocabulary: tackling: 应对

**[4859.48s] English:** chips which is a very different space um that's where you say i think we'll see a lot more custom  
**Translation:** 

**[4866.64s] English:** chips and that means that you get much more battery life you get better better tuned solutions  
**Translation:** 

**[4872.68s] English:** for your iot thingy you get you get people that move faster you get the ability to have faster  
**Translation:** 

**[4879.96s] English:** time to market for example so how many custom so first of all on the iot side of things do you see  
**Translation:** Vocabulary: thingy: 小玩意儿

**[4885.44s] English:** the number of smart toasters increasing  
**Translation:** 

**[4889.48s] English:** exponentially so uh and if you do like how much customization per toaster is there do all toasters  
**Translation:** Vocabulary: exponentially: 成倍增加

**[4899.60s] English:** in the world run the same uh silicon like the same design or is it different companies have  
**Translation:** 

**[4905.28s] English:** different design like how much how much customization is possible here well a lot of it comes down to  
**Translation:** 

**[4910.68s] English:** cost right and so the way that chips work is you end up paying by the one one of the factors is the  
**Translation:** 

**[4917.40s] English:** the size of the chip  
**Translation:** 

**[4919.48s] English:** and so  
**Translation:** 

**[4920.00s] English:** So what ends up happening, just from an economic perspective, is there's only so many chips that get made in a year of a given design.  
**Translation:** 

**[4927.44s] English:** And so often what customers end up having to do is they end up having to pick up a chip that exists that was built for somebody else so that they can then ship their product.  
**Translation:** 

**[4936.46s] English:** And the reason for that is they don't have the volume of the iPhone.  
**Translation:** 

**[4939.24s] English:** They can't afford to build a custom chip.  
**Translation:** 

**[4941.66s] English:** However, what that means is they're now buying an off-the-shelf chip that isn't a perfect fit for their needs, and so they're paying a lot of money for it.  
**Translation:** 

**[4950.00s] English:** Because they're buying silicon that they're not using.  
**Translation:** 

**[4953.26s] English:** Well, if you now reduce the cost of designing the chip, now you get a lot more chips.  
**Translation:** 

**[4957.88s] English:** And the more you reduce it, the easier it is to design chips.  
**Translation:** 

**[4962.18s] English:** The more the world keeps evolving and we get more AI accelerators, we get more other things, we get more standards to talk to, we get 6G, right?  
**Translation:** Vocabulary: accelerators: 加速器; evolving: 发展

**[4970.80s] English:** You get changes in the world that you want to be able to talk to these different things.  
**Translation:** 

**[4974.80s] English:** There's more diversity in the cross-product of features that people want.  
**Translation:** 

**[4978.64s] English:** And that drives...  
**Translation:** 

**[4980.42s] English:** Differentiated chips in another direction.  
**Translation:** Vocabulary: differentiated: 区分化的

**[4983.40s] English:** And so nobody really knows what the future looks like, but I think that there's a lot of silicon in the future.  
**Translation:** 

**[4989.54s] English:** Speaking of the future, you said Moore's Law allegedly is dead.  
**Translation:** Vocabulary: allegedly: 据说

**[4993.82s] English:** So do you agree with Dave Patterson and many folks that Moore's Law is dead?  
**Translation:** 

**[5001.84s] English:** Or do you agree with Jim Keller, who's standing at the helm of the pirate ship, saying it's...  
**Translation:** Vocabulary: keller: 凯勒; patterson: 帕特森

**[5010.00s] English:** It's still alive.  
**Translation:** 

**[5010.70s] English:** It's still alive.  
**Translation:** 

**[5011.60s] English:** Yeah.  
**Translation:** 

**[5012.42s] English:** Also, I agree with what they're saying and different people are interpreting the end of Moore's Law in different ways.  
**Translation:** Vocabulary: interpreting: 解释

**[5019.30s] English:** Yeah.  
**Translation:** 

**[5019.54s] English:** So Jim would say, you know, there's another thousand X left in physics and we can continue to squeeze the stone and make it faster and smaller and smaller geometries and all that kind of stuff.  
**Translation:** Vocabulary: geometries: 几何结构

**[5032.22s] English:** He's right.  
**Translation:** 

**[5033.58s] English:** So Jim is absolutely right that there's a ton of progress left and we're not at the limit of physics yet.  
**Translation:** 

**[5040.00s] English:** Um, uh, that's not really what Moore's law is though. If you look at what Moore's law is,  
**Translation:** 

**[5046.58s] English:** is that it's a very simple, uh, evaluation of, okay, well you look at the cost for, um,  
**Translation:** 

**[5053.56s] English:** I think it was cost per area and the most economic point in that space. And if you go look at the,  
**Translation:** 

**[5058.42s] English:** the, the now quite old paper that describes this, um, Moore's law has a specific economic  
**Translation:** 

**[5063.62s] English:** aspect to it. And I think this is something that Dave and others often point out. And so on a  
**Translation:** 

**[5069.30s] English:** technicality, that's right. Um, I look at it from, so I can acknowledge both of those viewpoints.  
**Translation:** Vocabulary: technicality: 技术细节; viewpoints: 观点

**[5074.72s] English:** They're both right. They're both right. I'll give you a third wrong viewpoint that may be  
**Translation:** 

**[5079.60s] English:** right in its own way, which is, um, single threaded performance doesn't improve like it  
**Translation:** Vocabulary: threaded: 多线程的

**[5085.46s] English:** used to. And it used to be back when you got a, uh, you know, a Pentium 66 or something. And  
**Translation:** 

**[5090.90s] English:** the year before you had a Pentium 33 and now it's twice as fast, right? Well, it was twice as fast  
**Translation:** 

**[5097.92s] English:** at doing exactly the same.  
**Translation:** 

**[5099.30s] English:** Thing. Okay. Like literally the same program ran twice as fast. You just wrote a check and waited  
**Translation:** 

**[5105.44s] English:** a year, year and a half. Well, so that's what a lot of people think about Moore's law. And I think  
**Translation:** 

**[5110.52s] English:** that is dead. And so what we're seeing instead is we're pushing, we're pushing people to write  
**Translation:** 

**[5116.10s] English:** software in different ways. And so we're pushing people to write CUDA so they can get GPU compute  
**Translation:** 

**[5120.84s] English:** and the, the thousands of cores on GPU. We're talking about C programmers having to use P  
**Translation:** Vocabulary: programmers: 程序员

**[5125.96s] English:** threads because they now have, you know, a hundred, a hundred threads or,  
**Translation:** 

**[5129.30s] English:** or 50 cores in a machine or something like that. Um, you're not talking about machine learning  
**Translation:** 

**[5132.96s] English:** accelerators. They're now domain specific. And when you look at these kinds of use cases,  
**Translation:** 

**[5138.02s] English:** you can still get performance. Um, and Jim will come up with cool things that, uh, utilize the  
**Translation:** 

**[5144.02s] English:** silicon in new ways for sure, but you're also going to change the programming model. Right.  
**Translation:** 

**[5148.76s] English:** And now when you start talking about changing the programming model, that's when you come back to  
**Translation:** 

**[5152.12s] English:** languages and things like this too, because often what you see is, um, like you take the C programming  
**Translation:** 

**[5159.10s] English:** language, right? The C  
**Translation:** 

**[5160.00s] English:** programming language is designed for cpus and so if you want to talk to a gpu now you're talking  
**Translation:** 

**[5165.50s] English:** to its cousin cuda okay cuda's a different thing with a different set of tools a different world  
**Translation:** 

**[5172.74s] English:** a different way of thinking and we don't have one world that scales and i think that we can get  
**Translation:** 

**[5178.26s] English:** there we can have one world that scales in a much better way on a small tangent then i think most  
**Translation:** Vocabulary: tangent: 附言

**[5183.12s] English:** programming languages are designed for cpus for single core even just in their spirit even if  
**Translation:** 

**[5189.26s] English:** they allow for parallelization so what does it look like for a programming language to have  
**Translation:** 

**[5194.74s] English:** parallelization or massive parallelization as its like first principle so the canonical example of  
**Translation:** 

**[5203.14s] English:** this is the hardware design world so verilog vhdl these kinds of languages they're what's called a  
**Translation:** Vocabulary: canonical: 标准示例

**[5211.20s] English:** high-level synthesis language this is the thing people design chips in and when you're designing  
**Translation:** 

**[5217.48s] English:** a chip it's kind of like a brain  
**Translation:** 

**[5219.26s] English:** where you have infinite parallelism like you've got you're you're like laying down transistors  
**Translation:** 

**[5225.12s] English:** transistors are always running okay and so you're not saying run run this transistor then this  
**Translation:** Vocabulary: transistor: 晶体管; transistors: 晶体管

**[5230.56s] English:** transistor than this transistor it's like your brain like your neurons are always just doing  
**Translation:** 

**[5234.50s] English:** something they're not clocked right they're just they're just doing they're they're doing their  
**Translation:** Vocabulary: neurons: 神经元

**[5239.38s] English:** thing and so when you design a chip or when you design a cpu when you design a gpu when you design  
**Translation:** 

**[5245.06s] English:** when you're laying down the transistors uh similarly you're talking about well okay well  
**Translation:** 

**[5249.26s] English:** how do these things communicate?  
**Translation:** 

**[5251.12s] English:** And so these languages exist.  
**Translation:** 

**[5252.82s] English:** Verilog is a kind of mixed example of that.  
**Translation:** 

**[5256.18s] English:** None of these languages are really great.  
**Translation:** 

**[5257.76s] English:** Yeah, they're very low level.  
**Translation:** 

**[5259.24s] English:** Yeah, they're very low level.  
**Translation:** 

**[5260.74s] English:** And abstraction is necessary here.  
**Translation:** 

**[5262.54s] English:** And there's different approaches with that.  
**Translation:** Vocabulary: abstraction: 抽象

**[5264.60s] English:** And it's itself a very complicated world.  
**Translation:** 

**[5267.46s] English:** But it's implicitly parallel.  
**Translation:** Vocabulary: implicitly: 暗含

**[5270.24s] English:** And so having that as the domain that you program towards  
**Translation:** 

**[5276.04s] English:** makes it so that by default, you get parallel systems.  
**Translation:** 

**[5279.26s] English:** If you look at...  
**Translation:** 

**[5280.00s] English:** CUDA. CUDA is a point halfway in the space where in CUDA, when you write a CUDA kernel for your  
**Translation:** Vocabulary: halfway: 中途; kernel: 内核

**[5285.20s] English:** GPU, it feels like you're writing a scalar program. So you're like, you have ifs, you have  
**Translation:** 

**[5289.44s] English:** for loops, stuff like this. You're just writing normal code. But what happens outside of that  
**Translation:** Vocabulary: scalar: 标量计算

**[5294.16s] English:** in your driver is that it actually is running you on like a thousand things at once, right?  
**Translation:** 

**[5298.88s] English:** And so it's parallel, but it has pulled it out of the programming model. And so now you as a  
**Translation:** 

**[5304.76s] English:** programmer are working in a simpler world, and it's solved that for you, right?  
**Translation:** 

**[5311.46s] English:** How do you take the language like Swift? You know, if we think about GPUs, but also ASICs,  
**Translation:** Vocabulary: programmer: 程序员

**[5319.04s] English:** maybe if we can dance back and forth between hardware and software,  
**Translation:** 

**[5322.52s] English:** is, you know, how do you design for these features to be able to program, make it a first  
**Translation:** 

**[5329.26s] English:** class citizen to be able to do like Swift for TensorFlow, to be able to do machine learning,  
**Translation:** 

**[5335.08s] English:** on current hardware, but also future hardware like TPUs and all kinds of ASICs that I'm sure  
**Translation:** 

**[5341.00s] English:** will be popping up more and more? Yeah. Well, so a lot of this comes down to this whole idea of  
**Translation:** 

**[5345.42s] English:** having the nuts and bolts underneath the covers that work really well. So you need, if you're  
**Translation:** 

**[5349.60s] English:** talking to TPUs, you need, you know, MLIR or XLA or one of these compilers that talks to TPUs  
**Translation:** 

**[5354.88s] English:** to build on top of, okay? And if you're talking to circuits, you need to figure out how to lay  
**Translation:** Vocabulary: circuits: 电路; compilers: 编译器

**[5360.72s] English:** down the transistors and how to organize it and how to set up clocking and like all the domain  
**Translation:** 

**[5363.94s] English:** problems that you get. And so you need to figure out how to lay down the transistors and how to  
**Translation:** Vocabulary: transistors: 晶体管

**[5364.76s] English:** with circuits. Then you have to decide how to explain it to a human. What is the UI, right?  
**Translation:** 

**[5371.82s] English:** And if you do it right, that's a library problem, not a language problem. And that works if you  
**Translation:** 

**[5377.28s] English:** have a library or a language, which allows your library to write things that feel native in the  
**Translation:** 

**[5383.26s] English:** language by implementing libraries, because then you can innovate in programming models without  
**Translation:** Vocabulary: implementing: 实现; innovate: 创新

**[5389.38s] English:** having to change your syntax again. And like you have to invent new code formatting tools,  
**Translation:** 

**[5394.76s] English:** and like all the other things that languages come with. And this gets really interesting.  
**Translation:** Vocabulary: formatting: 格式化; syntax: 语法规则

**[5400.00s] English:** And so if you look at the space,  
**Translation:** 

**[5402.30s] English:** the interesting thing once you separate out syntax  
**Translation:** 

**[5405.84s] English:** becomes what is that programming model?  
**Translation:** 

**[5407.86s] English:** And so do you want the CUDA style?  
**Translation:** 

**[5410.24s] English:** I write one program and it runs many places.  
**Translation:** 

**[5414.32s] English:** Do you want the implicitly parallel model?  
**Translation:** Vocabulary: implicitly: 暗含地

**[5416.82s] English:** How do you reason about that?  
**Translation:** 

**[5417.76s] English:** How do you give developers, chip architects,  
**Translation:** 

**[5420.76s] English:** the ability to express their intent?  
**Translation:** 

**[5424.08s] English:** And that comes into this whole design question  
**Translation:** 

**[5426.28s] English:** of how do you detect bugs quickly  
**Translation:** 

**[5429.16s] English:** so you don't have to tape out a chip  
**Translation:** 

**[5430.24s] English:** to find out what's wrong, ideally, right?  
**Translation:** 

**[5432.62s] English:** How do you, and this is a spectrum,  
**Translation:** 

**[5435.52s] English:** how do you make it so that people feel productive  
**Translation:** 

**[5438.52s] English:** so their turnaround time is very quick?  
**Translation:** Vocabulary: turnaround: 周转时间

**[5440.46s] English:** All these things are really hard problems.  
**Translation:** 

**[5442.42s] English:** And in this world, I think that not a lot of effort  
**Translation:** 

**[5446.10s] English:** has been put into that design problem  
**Translation:** 

**[5448.06s] English:** and thinking about the layering and other pieces.  
**Translation:** Vocabulary: layering: 分层

**[5451.14s] English:** Well, you've, on the topic of concurrency,  
**Translation:** 

**[5453.52s] English:** you've written the Swift concurrency manifest.  
**Translation:** Vocabulary: concurrency: 并行性; manifest: 宣言

**[5455.58s] English:** I think it's kind of interesting.  
**Translation:** 

**[5457.62s] English:** Anything that,  
**Translation:** 

**[5459.16s] English:** has the word manifesto in it is very interesting.  
**Translation:** 

**[5462.38s] English:** Can you summarize the key ideas  
**Translation:** Vocabulary: manifesto: 宣言; summarize: 总结

**[5464.08s] English:** of each of the five parts you've written about?  
**Translation:** 

**[5467.40s] English:** So what is a manifesto?  
**Translation:** 

**[5468.90s] English:** Yes.  
**Translation:** 

**[5469.74s] English:** How about we start there?  
**Translation:** 

**[5471.82s] English:** So in the Swift community, we have this problem,  
**Translation:** 

**[5475.16s] English:** which is on the one hand,  
**Translation:** 

**[5476.10s] English:** you want to have relatively small proposals  
**Translation:** 

**[5479.32s] English:** that you can kind of fit in your head.  
**Translation:** 

**[5481.42s] English:** You can understand the details at a very fine-grained level  
**Translation:** 

**[5484.10s] English:** that move the world forward.  
**Translation:** 

**[5486.02s] English:** But then you also have these big arcs, okay?  
**Translation:** 

**[5488.24s] English:** Yeah.  
**Translation:** 

**[5489.16s] English:** And often when you're working on something  
**Translation:** 

**[5490.80s] English:** that is a big arc,  
**Translation:** 

**[5492.32s] English:** but you're tackling it in small pieces,  
**Translation:** 

**[5494.08s] English:** you have this question of,  
**Translation:** Vocabulary: tackling: 应对

**[5495.10s] English:** how do I know I'm not doing a random walk?  
**Translation:** 

**[5497.56s] English:** Where are we going?  
**Translation:** 

**[5498.78s] English:** How does this add up?  
**Translation:** 

**[5499.76s] English:** Furthermore, when you start the first small step,  
**Translation:** 

**[5503.60s] English:** what terminology do you use?  
**Translation:** 

**[5505.28s] English:** How do we think about it?  
**Translation:** Vocabulary: terminology: 术语

**[5506.56s] English:** What is better and worse in the space?  
**Translation:** 

**[5507.92s] English:** What are the principles?  
**Translation:** 

**[5508.74s] English:** What are we trying to achieve?  
**Translation:** 

**[5510.10s] English:** And so what a manifesto in the Swift community does  
**Translation:** 

**[5512.04s] English:** is it starts to say,  
**Translation:** 

**[5513.20s] English:** hey, well, let's step back from the details of everything.  
**Translation:** 

**[5516.62s] English:** Let's paint a broad picture to talk about how, you know,  
**Translation:** 

**[5518.28s] English:** how do we do this?  
**Translation:** 

**[5519.16s] English:** How do we do this?  
**Translation:** 

**[5520.00s] English:** we're trying to achieve let's give an example design point let's try to paint the big picture  
**Translation:** 

**[5525.16s] English:** so that then we can zero in on the individual steps and make sure that we're making good progress  
**Translation:** 

**[5528.84s] English:** and so the swift concurrency manifesto is something i wrote three years ago it's been a while maybe  
**Translation:** 

**[5534.74s] English:** maybe more um trying to do that for for swift and concurrency it starts with some fairly uh simple  
**Translation:** 

**[5541.96s] English:** things like making the observation that when you have multiple different computers or multiple  
**Translation:** 

**[5547.04s] English:** different threads that are communicating it's best for them to be asynchronous right and so  
**Translation:** 

**[5552.30s] English:** you need things to be able to run separately and then communicate with each other and this means  
**Translation:** Vocabulary: asynchronous: 非同步

**[5556.32s] English:** asynchrony and this means that you need a way to modeling asynchronous communication  
**Translation:** 

**[5560.78s] English:** many languages have features like this async await is a popular one and so that's what i  
**Translation:** Vocabulary: async: 异步; asynchrony: 异步性

**[5566.22s] English:** think is very likely in swift but as you start building this tower of abstractions it's not just  
**Translation:** 

**[5571.76s] English:** about how do you write this you then reach into the how do you get memory safety  
**Translation:** Vocabulary: abstractions: 抽象

**[5576.38s] English:** um  
**Translation:** 

**[5577.04s] English:** because you want correctness you want debuggability and sanity for developers  
**Translation:** Vocabulary: correctness: 正确性; debuggability: 可调试性

**[5581.12s] English:** and how do you get uh that memory safety into um into the language so if you take a language like go  
**Translation:** 

**[5587.80s] English:** or c or any of these languages you get what's called a race condition when two different threads  
**Translation:** 

**[5593.38s] English:** or go routines or whatever touch the same point in memory right this is a huge like maddening  
**Translation:** 

**[5599.60s] English:** problem to debug because uh it's not reproducible generally and so there's tools there's a whole  
**Translation:** Vocabulary: reproducible: 可重现的

**[5605.88s] English:** ecosystem of solutions  
**Translation:** 

**[5606.86s] English:** there's a whole ecosystem of solutions  
**Translation:** 

**[5607.02s] English:** there's a whole ecosystem of solutions  
**Translation:** 

**[5607.04s] English:** built up around this but it's it's a huge problem when you're writing concurrent code  
**Translation:** Vocabulary: concurrent: 并行的

**[5610.80s] English:** and so with swift uh this whole value semantics thing is really powerful there because it turns  
**Translation:** 

**[5615.92s] English:** out that math and copies actually work even in concurrent worlds and so um you get a lot of  
**Translation:** Vocabulary: semantics: 语义

**[5622.12s] English:** safety just out of the box but there are also some hard problems and it talks about some of that  
**Translation:** 

**[5626.02s] English:** when you start building up to the next level up and you start talking beyond memory safety you  
**Translation:** 

**[5630.58s] English:** have to talk about what is the programmer model how does a human think about this so a developer  
**Translation:** 

**[5635.30s] English:** that's trying to build a program think about this and then you have to talk about what is the  
**Translation:** Vocabulary: programmer: 程序员

**[5637.02s] English:** tree about this you've got to have a very limited Swan doesn't have the ability to manage  
**Translation:** 

**[5646.14s] English:** all the innocents and Михailoputin skill that the more the better launches you have  
**Translation:** Vocabulary: innocents: 无辜者

**[5648.46s] English:** bie has I was trying to think about this and it proposes a really old model  
**Translation:** 

**[5640.00s] English:** with a new spin called Actors.  
**Translation:** 

**[5642.02s] English:** Actors are about saying  
**Translation:** 

**[5643.42s] English:** we have islands of single-threadedness, logically.  
**Translation:** Vocabulary: logically: 合逻辑地

**[5648.08s] English:** So you write something that feels like  
**Translation:** 

**[5649.32s] English:** it's one program running in a unit,  
**Translation:** 

**[5653.00s] English:** and then it communicates asynchronously  
**Translation:** 

**[5654.96s] English:** with other things.  
**Translation:** Vocabulary: asynchronously: 不同时地

**[5657.98s] English:** And so making that expressive and natural feel good,  
**Translation:** 

**[5660.84s] English:** be the first thing you reach for,  
**Translation:** Vocabulary: expressive: 表达丰富的

**[5661.92s] English:** and it being safe by default  
**Translation:** 

**[5662.92s] English:** is a big part of the design of that proposal.  
**Translation:** 

**[5666.38s] English:** When you start going beyond that,  
**Translation:** 

**[5667.70s] English:** now you start to say, cool,  
**Translation:** 

**[5668.60s] English:** well, these things that communicate asynchronously,  
**Translation:** 

**[5671.10s] English:** they don't have to share memory.  
**Translation:** 

**[5672.92s] English:** Well, if they don't have to share memory  
**Translation:** 

**[5674.18s] English:** and they're sending messages to each other,  
**Translation:** 

**[5676.06s] English:** why do they have to be in the same process?  
**Translation:** 

**[5679.02s] English:** These things should be able to be  
**Translation:** 

**[5680.24s] English:** in different processes on your machine.  
**Translation:** 

**[5682.62s] English:** And why just processes?  
**Translation:** 

**[5684.10s] English:** Well, why not different machines?  
**Translation:** 

**[5686.66s] English:** And so now you have a very nice gradual transition  
**Translation:** 

**[5689.46s] English:** towards distributed programming.  
**Translation:** 

**[5691.70s] English:** And of course, when you start talking about the big future,  
**Translation:** 

**[5695.00s] English:** the manifesto doesn't go into it,  
**Translation:** 

**[5696.94s] English:** but accelerating,  
**Translation:** Vocabulary: accelerating: 加速; manifesto: 宣言

**[5698.60s] English:** the operators are things you talk to asynchronously  
**Translation:** 

**[5701.98s] English:** by sending messages to them.  
**Translation:** 

**[5704.36s] English:** And how do you program those?  
**Translation:** 

**[5705.84s] English:** Well, that gets very interesting.  
**Translation:** 

**[5707.72s] English:** That's not in the proposal.  
**Translation:** 

**[5709.58s] English:** So, and how much do you want to make that explicit,  
**Translation:** Vocabulary: explicit: 明确

**[5715.02s] English:** like the control of that whole process  
**Translation:** 

**[5716.94s] English:** explicit to the programmer?  
**Translation:** 

**[5718.10s] English:** Yeah, good question.  
**Translation:** 

**[5719.30s] English:** So when you're designing any of these kinds of features  
**Translation:** 

**[5722.76s] English:** or language features or even libraries,  
**Translation:** 

**[5725.30s] English:** you have this really hard trade-off  
**Translation:** 

**[5727.04s] English:** that you have to make, which is,  
**Translation:** 

**[5728.14s] English:** you have to make a lot of things.  
**Translation:** 

**[5728.60s] English:** How much is it magic  
**Translation:** 

**[5729.62s] English:** or how much is it in the human's control?  
**Translation:** 

**[5732.14s] English:** How much can they predict and control it?  
**Translation:** 

**[5734.64s] English:** What do you do when the default case is the wrong case?  
**Translation:** 

**[5739.60s] English:** Okay.  
**Translation:** 

**[5740.24s] English:** And so when you're designing a system,  
**Translation:** 

**[5742.12s] English:** I won't name names,  
**Translation:** 

**[5745.06s] English:** but there are systems where you,  
**Translation:** 

**[5748.38s] English:** it's really easy to get started  
**Translation:** 

**[5750.10s] English:** and then you jump.  
**Translation:** 

**[5752.60s] English:** So let's pick like logo.  
**Translation:** 

**[5754.16s] English:** Okay.  
**Translation:** 

**[5754.36s] English:** So something like this.  
**Translation:** 

**[5755.58s] English:** So it's really easy to get started.  
**Translation:** 

**[5757.06s] English:** It's really designed for,  
**Translation:** 

**[5758.14s] English:** for teaching kids.  
**Translation:** 

**[5759.66s] English:** But as you know,  
**Translation:** 

**[5760.00s] English:** you get into it you hit a ceiling and then you can't go any higher and then what do you do well  
**Translation:** 

**[5764.22s] English:** you have to go switch to a different world and rewrite all your code and this logo is a silly  
**Translation:** 

**[5768.48s] English:** example here this exists in many other languages uh with python you would say uh like concurrency  
**Translation:** 

**[5774.92s] English:** right so python has the global interpreter lock so threading is challenging in python and so if you  
**Translation:** 

**[5780.04s] English:** if you start writing a large-scale application in python and then suddenly you need concurrency  
**Translation:** Vocabulary: concurrency: 并行性; interpreter: 解释器; threading: 线程

**[5784.52s] English:** you're kind of stuck with a series of bad trade-offs right um uh there's other ways to go  
**Translation:** 

**[5791.44s] English:** where you say like voiced all the all the complexity on the user all at once right and  
**Translation:** 

**[5797.20s] English:** that's also bad in a different way and so what what i what i prefer is building a simple model  
**Translation:** 

**[5803.38s] English:** that you can explain that then has an escape hatch so you get in you have guardrails you uh  
**Translation:** Vocabulary: guardrails: 防护栏

**[5810.52s] English:** memory safety works like this in swift where you can start with you like  
**Translation:** 

**[5814.12s] English:** bite  
**Translation:** 

**[5814.50s] English:** default if you use all the standard things it's memory safe you're not going to shoot your foot  
**Translation:** 

**[5817.90s] English:** off but if you want to get a uh a c-level pointer to something you can explicitly do that but by  
**Translation:** Vocabulary: explicitly: 明确地

**[5824.66s] English:** default it's uh there's guardrails there's guardrails okay so but like you know uh whose  
**Translation:** 

**[5833.06s] English:** job is it to figure out which part of the code is parallelizable um so in the case of the proposal  
**Translation:** Vocabulary: parallelizable: 可并行化

**[5838.56s] English:** it is the human's job so they decide how to architect their application  
**Translation:** 

**[5843.38s] English:** and then  
**Translation:** 

**[5844.50s] English:** uh the runtime in the compiler is very predictable and so this this is in contrast to um like there's  
**Translation:** 

**[5852.04s] English:** a long body of work including on fortran for auto parallelizing compilers and um this is an example  
**Translation:** Vocabulary: compilers: 编译器; predictable: 可预测的; runtime: 运行时

**[5858.92s] English:** of a bad thing and my so as a compiler person i can rag on compiler people um often compiler  
**Translation:** 

**[5864.24s] English:** people will say cool since i can't change the code i'm going to write my compiler that then  
**Translation:** 

**[5868.80s] English:** takes this unmodified code and makes it go way faster on this machine okay application development  
**Translation:** 

**[5874.50s] English:** so it does pattern matching it does like really deep analysis compiler people are really smart  
**Translation:** Vocabulary: unmodified: 未经修改的

**[5879.48s] English:** and so they like  
**Translation:** 

**[5880.00s] English:** Like, want to, like, do something really clever and tricky,  
**Translation:** 

**[5882.48s] English:** and you get, like, 10x speedup by taking, like, an array of structures  
**Translation:** 

**[5885.96s] English:** and turn it into a structure of arrays or something  
**Translation:** Vocabulary: speedup: 加速

**[5887.98s] English:** because it's so much better for memory.  
**Translation:** 

**[5889.36s] English:** Like, there's bodies, like, tons of tricks.  
**Translation:** 

**[5891.68s] English:** Yeah.  
**Translation:** 

**[5892.36s] English:** They love optimization.  
**Translation:** Vocabulary: optimization: 优化

**[5893.78s] English:** Yeah, you love optimization.  
**Translation:** 

**[5894.62s] English:** Everyone loves optimization.  
**Translation:** 

**[5895.70s] English:** Everyone loves it.  
**Translation:** 

**[5896.40s] English:** Well, and it's this promise of build with my compiler and your thing goes fast.  
**Translation:** 

**[5900.08s] English:** Yeah.  
**Translation:** 

**[5900.70s] English:** Right, but here's the problem.  
**Translation:** 

**[5902.40s] English:** Lex, you write a program.  
**Translation:** 

**[5904.44s] English:** You run it with my compiler.  
**Translation:** 

**[5905.96s] English:** It goes fast.  
**Translation:** 

**[5906.56s] English:** You're very happy.  
**Translation:** 

**[5907.30s] English:** Wow, it's so much faster than the other compiler.  
**Translation:** 

**[5908.82s] English:** Then you go and you add a feature to your program  
**Translation:** 

**[5911.14s] English:** or you refactor some code,  
**Translation:** 

**[5912.32s] English:** and suddenly you got a 10x loss in performance.  
**Translation:** Vocabulary: refactor: 重构代码

**[5915.52s] English:** Well, why?  
**Translation:** 

**[5916.38s] English:** What just happened there?  
**Translation:** 

**[5917.50s] English:** What just happened there is the heuristic,  
**Translation:** 

**[5919.94s] English:** the pattern matching, the compiler,  
**Translation:** Vocabulary: heuristic: 启发式方法

**[5921.94s] English:** whatever analysis it was doing just got defeated  
**Translation:** 

**[5923.74s] English:** because you didn't inline a function or something, right?  
**Translation:** Vocabulary: inline: 内联

**[5928.00s] English:** As a user, you don't know.  
**Translation:** 

**[5929.38s] English:** You don't want to know.  
**Translation:** 

**[5930.16s] English:** That was the whole point.  
**Translation:** 

**[5930.80s] English:** You don't want to know how the compiler works.  
**Translation:** 

**[5932.54s] English:** You don't want to know how the memory hierarchy works.  
**Translation:** 

**[5934.52s] English:** You don't want to know how it got parallelized across all these things.  
**Translation:** Vocabulary: hierarchy: 层次结构

**[5937.02s] English:** You wanted that abstracted way.  
**Translation:** 

**[5938.82s] English:** But then the magic is lost as soon as you did something  
**Translation:** Vocabulary: abstracted: 抽离的

**[5942.62s] English:** and you fall off a performance cliff.  
**Translation:** 

**[5945.02s] English:** And now you're in this funny position where,  
**Translation:** 

**[5947.02s] English:** what do I do?  
**Translation:** 

**[5947.98s] English:** I don't change my code.  
**Translation:** 

**[5948.98s] English:** I don't fix that bug.  
**Translation:** 

**[5950.62s] English:** It costs 10x performance.  
**Translation:** 

**[5952.30s] English:** Now what do I do?  
**Translation:** 

**[5953.50s] English:** Well, this is the problem with unpredictable performance.  
**Translation:** 

**[5956.02s] English:** If you care about performance,  
**Translation:** 

**[5957.38s] English:** predictability is a very important thing.  
**Translation:** 

**[5959.60s] English:** And so what the proposal does is it provides architectural patterns  
**Translation:** 

**[5964.68s] English:** for being able to lay out your code,  
**Translation:** Vocabulary: architectural: 建筑风格的

**[5966.68s] English:** gives you full control over that,  
**Translation:** 

**[5967.98s] English:** makes it really simple so you can explain it,  
**Translation:** 

**[5970.30s] English:** and then if you want to scale out in different ways,  
**Translation:** 

**[5974.72s] English:** you have full control over that.  
**Translation:** 

**[5976.52s] English:** So in your sense,  
**Translation:** 

**[5977.56s] English:** the intuition is for a compiler,  
**Translation:** Vocabulary: intuition: 直觉

**[5979.46s] English:** it's too hard to do automated parallelization.  
**Translation:** 

**[5983.00s] English:** Because the compilers do stuff automatically  
**Translation:** Vocabulary: automated: 自动化; compilers: 编译器

**[5987.00s] English:** that's incredibly impressive for other things.  
**Translation:** 

**[5989.82s] English:** Right.  
**Translation:** 

**[5990.32s] English:** But for parallelization, we're not close to there.  
**Translation:** 

**[5994.54s] English:** Well, it depends on the programming model.  
**Translation:** 

**[5996.06s] English:** So there's many different kinds of compilers.  
**Translation:** 

**[5997.98s] English:** And so if you talk about a C component,  
**Translation:** 

**[6000.00s] English:** or a Swift compiler or something like that  
**Translation:** 

**[6001.90s] English:** where you're writing imperative code,  
**Translation:** Vocabulary: imperative: 命令式的

**[6004.94s] English:** parallelizing that and reasoning about all the pointers  
**Translation:** 

**[6007.12s] English:** and stuff like that is a very difficult problem.  
**Translation:** 

**[6010.12s] English:** Now, if you switch domains,  
**Translation:** 

**[6012.20s] English:** so there's this cool thing called machine learning, right?  
**Translation:** 

**[6015.52s] English:** So the machine learning nerds among other endearing things  
**Translation:** 

**[6018.94s] English:** like solving cat detectors and other things like that  
**Translation:** Vocabulary: detectors: 猫检测器; nerds: 极客

**[6023.36s] English:** have done this amazing breakthrough  
**Translation:** 

**[6025.38s] English:** of producing a programming model,  
**Translation:** 

**[6027.52s] English:** operations that you compose together  
**Translation:** 

**[6030.24s] English:** that has raised levels of abstraction high enough  
**Translation:** Vocabulary: abstraction: 抽象

**[6033.16s] English:** that suddenly you can have auto-paralyzing compilers, right?  
**Translation:** 

**[6036.82s] English:** You can write a model using a TensorFlow  
**Translation:** 

**[6039.58s] English:** and have it run on 1,024 nodes of a TPU.  
**Translation:** 

**[6043.42s] English:** Yeah, that's true.  
**Translation:** 

**[6044.26s] English:** I didn't even think about like,  
**Translation:** 

**[6046.84s] English:** cause there's so much flexibility  
**Translation:** 

**[6048.18s] English:** in the design of architectures  
**Translation:** 

**[6049.56s] English:** that ultimately boil down to a graph  
**Translation:** 

**[6051.44s] English:** that's parallelizable for you, parallelized for you.  
**Translation:** 

**[6054.16s] English:** And if you think about it, that's pretty cool.  
**Translation:** 

**[6056.68s] English:** That's pretty cool, yeah.  
**Translation:** 

**[6057.52s] English:** And you think about batching, for example,  
**Translation:** 

**[6059.74s] English:** as a way of being able to exploit more parallelism.  
**Translation:** 

**[6062.42s] English:** Like that's a very simple thing that now is very powerful.  
**Translation:** 

**[6065.38s] English:** That didn't come out of the programming language nerds,  
**Translation:** 

**[6067.74s] English:** right, those people.  
**Translation:** 

**[6068.90s] English:** Like that came out of people  
**Translation:** 

**[6070.12s] English:** that are just looking to solve a problem  
**Translation:** 

**[6071.44s] English:** and use a few GPUs and organically developed  
**Translation:** 

**[6074.02s] English:** by the community of people focusing on machine learning.  
**Translation:** Vocabulary: organically: 自然发展

**[6076.84s] English:** And it's an incredibly powerful abstraction layer  
**Translation:** 

**[6079.88s] English:** that enables the compiler people to go and exploit that.  
**Translation:** 

**[6082.80s] English:** And now you can drive supercomputers from Python.  
**Translation:** 

**[6086.84s] English:** That's pretty cool.  
**Translation:** Vocabulary: supercomputers: 超级计算机

**[6087.68s] English:** That's amazing.  
**Translation:** 

**[6088.50s] English:** So just to pause on that,  
**Translation:** 

**[6089.34s] English:** cause I'm not sufficiently low level.  
**Translation:** 

**[6092.30s] English:** I forget to admire the beauty and power of that,  
**Translation:** Vocabulary: sufficiently: 足够地

**[6095.40s] English:** but maybe just to linger on it,  
**Translation:** 

**[6098.52s] English:** like what does it take to run a neural network fast?  
**Translation:** Vocabulary: neural: 神经的

**[6102.64s] English:** Like how hard is that compilation?  
**Translation:** 

**[6104.06s] English:** It's really hard.  
**Translation:** Vocabulary: compilation: 汇编

**[6105.66s] English:** So we just skipped.  
**Translation:** 

**[6106.92s] English:** You said like, it's amazing that that's a thing,  
**Translation:** 

**[6109.60s] English:** but how hard is that of a thing?  
**Translation:** 

**[6111.52s] English:** It's hard.  
**Translation:** 

**[6112.36s] English:** And I would say that not all of the systems are really great.  
**Translation:** 

**[6116.84s] English:** Including the ones I helped build.  
**Translation:** 

**[6118.64s] English:** So there's a lot of work left.  
**Translation:** 

**[6120.00s] English:** be done there is it the compiler nerds working on that or is it a whole new group of people well  
**Translation:** 

**[6124.72s] English:** it's a full stack problem including compiler people um including apis so like charis and the  
**Translation:** 

**[6130.80s] English:** the the module api and pytorch and jacks and there's a bunch of people pushing on all the  
**Translation:** Vocabulary: charis: 查里斯; module: 模块

**[6136.36s] English:** different parts of these things because when you look at it as it's both how do i express the  
**Translation:** 

**[6140.44s] English:** computation do i stack up layers well cool like setting up a linear sequence of layers is great  
**Translation:** Vocabulary: computation: 计算

**[6146.00s] English:** for the simple case but how do i do the hard case how do i do reinforcement learning well now i need  
**Translation:** 

**[6149.96s] English:** to integrate my application logic in this right then it's you know the next level down of how do  
**Translation:** Vocabulary: integrate: 整合; reinforcement: 强化学习

**[6154.88s] English:** you represent that for the runtime how do you get hardware abstraction and then you get to the next  
**Translation:** 

**[6159.94s] English:** level down of saying like forget about abstraction how do i get the peak performance out of my tpu  
**Translation:** Vocabulary: abstraction: 抽象层; runtime: 运行时

**[6163.98s] English:** or my iphone accelerator or whatever right and all these different things and how and so this  
**Translation:** 

**[6169.36s] English:** is a layered problem with a lot of really interesting uh design and work going on in the  
**Translation:** 

**[6174.14s] English:** space and a lot of really smart people working on it machine learning is a very well-funded  
**Translation:** 

**[6178.56s] English:** area of investment  
**Translation:** 

**[6179.96s] English:** right now and so there's a lot of progress being made so how much innovation is there on the  
**Translation:** 

**[6184.86s] English:** lower level so closer to the to the asic so redesigning the hardware or redesigning  
**Translation:** 

**[6190.84s] English:** concurrently compilers with that hardware is that if you were to predict the biggest  
**Translation:** 

**[6195.62s] English:** uh you know the equivalent of moore's law improvements in the inference in the training  
**Translation:** Vocabulary: compilers: 编译器; concurrently: 同时; inference: 推理

**[6203.12s] English:** of neural networks sure and just all of that where is that going to come from you think sure  
**Translation:** 

**[6207.06s] English:** you get scalability you have different things and so you get um  
**Translation:** Vocabulary: scalability: 可扩展性

**[6209.96s] English:** you know jim keller shrinking process technology you get three nanometer instead of five or seven  
**Translation:** 

**[6216.18s] English:** or ten or twenty eight or whatever um and so that that marches forward and that provides  
**Translation:** Vocabulary: keller: 凯勒; nanometer: 纳米; shrinking: 缩小

**[6220.56s] English:** improvements you get uh architectural level performance and so the you know a tpu with a  
**Translation:** 

**[6226.56s] English:** matrix multiply unit and a systolic array is much more efficient than having a scalar core doing  
**Translation:** Vocabulary: architectural: 架构; matrix: 矩阵; multiply: 乘法; scalar: 标量; systolic: systolic

**[6231.94s] English:** multiplies and ads and things like that you then get um uh system level improvements so how you  
**Translation:** 

**[6239.14s] English:** talk to memory  
**Translation:** Vocabulary: multiplies: 增加

**[6239.96s] English:** you  
**Translation:** 

**[6240.00s] English:** you talk across a cluster of machines how you scale out how you have fast interconnects between  
**Translation:** Vocabulary: cluster: 机器集群; interconnects: 高速互联

**[6245.04s] English:** machines you then get system level programming models so now that you have all this hardware  
**Translation:** 

**[6249.90s] English:** how to utilize it you then have algorithmic breakthroughs where you say hey wow cool  
**Translation:** Vocabulary: algorithmic: 算法相关的; breakthroughs: 突破

**[6253.96s] English:** instead of training in uh you know resonant 50 and uh a week i'm now training it in you know 25  
**Translation:** 

**[6260.68s] English:** seconds yeah and now it's a combination it's a combination of uh you know new new optimizers  
**Translation:** Vocabulary: optimizers: 优化器

**[6266.78s] English:** and new new new just training regimens and different different approaches to train and  
**Translation:** 

**[6272.32s] English:** and all these things come together to to push the world forward that was a a beautiful exposition  
**Translation:** Vocabulary: exposition: 展览; regimens: 训练方案

**[6278.84s] English:** but if you were to uh force to bet all your money on one of these  
**Translation:** 

**[6283.70s] English:** why do we have to that's true unfortunately we have people working on all this okay it's  
**Translation:** 

**[6290.96s] English:** an exciting time right so i mean you know uh open the eye did this little paper showing the  
**Translation:** 

**[6296.78s] English:** improvement you can get has been you know improving exponentially uh i haven't quite  
**Translation:** Vocabulary: exponentially: 成倍增长

**[6302.12s] English:** seen the same kind of analysis on other layers of the stack i'm sure it's also improving  
**Translation:** 

**[6308.24s] English:** significantly i just it's uh it's a nice intuition builder i mean there's a reason why  
**Translation:** Vocabulary: intuition: 直觉

**[6313.72s] English:** moore's law that's the beauty of moore's law is somebody writes a paper that makes a ridiculous  
**Translation:** 

**[6320.54s] English:** prediction yeah and it you know becomes reality in a sense  
**Translation:** 

**[6326.78s] English:** there's there's something about these narratives when you uh when chris latner on a silly little  
**Translation:** 

**[6333.00s] English:** podcast makes all bets all his money on a particular thing somehow it can have a ripple  
**Translation:** Vocabulary: ripple: 波纹效应

**[6338.88s] English:** effect of actually becoming real that's an interesting aspect of it because like it might  
**Translation:** 

**[6344.28s] English:** have been uh you know we focus with moore's law most of the computing industry really really  
**Translation:** Vocabulary: computing: 计算

**[6350.62s] English:** focused on the hardware i mean software innovation i don't know how much software innovation there  
**Translation:** 

**[6356.60s] English:** wasn't  
**Translation:** 

**[6356.78s] English:** what intel giveth bill takes away  
**Translation:** 

**[6360.00s] English:** Yeah. I mean, compilers improved significantly also.  
**Translation:** Vocabulary: compilers: 编译器

**[6364.08s] English:** Well, not really. So, actually, I mean, I'm joking about how software's gotten slower pretty much as fast as hardware got better, at least through the 90s.  
**Translation:** 

**[6373.00s] English:** There's another joke, another law in compilers, which is called, I think it's called Probstein's Law, which is compilers double the performance of any given code every 18 years.  
**Translation:** 

**[6385.96s] English:** So, they move slowly.  
**Translation:** 

**[6387.16s] English:** Well, yeah, it's exponential also.  
**Translation:** 

**[6391.04s] English:** Yeah, but you're making progress. But there, again, it's not about, the power of compilers is not just about how do you make the same thing go faster. It's how do you unlock the new hardware?  
**Translation:** 

**[6401.60s] English:** A new chip came out, how do you utilize it? You say, oh, the programming model, how do we make people more productive? How do we, like, have better error messages?  
**Translation:** 

**[6411.90s] English:** Even such mundane things like, how do I generate a very specific error message?  
**Translation:** 

**[6417.16s] English:** About your code actually makes people happy because then they know how to fix it, right? And it comes back to how do you help people get their job done?  
**Translation:** Vocabulary: mundane: 平凡事务

**[6424.76s] English:** Yeah. And yeah, and then in this world of exponentially increasing smart toasters, how do you expand computing to all these kinds of devices?  
**Translation:** 

**[6435.72s] English:** I mean, do you see this world where just everything's a computing surface? You see that possibility? Just everything's a computer?  
**Translation:** Vocabulary: exponentially: 成倍地

**[6443.74s] English:** Yeah, I don't see any reason that that couldn't be achieved.  
**Translation:** 

**[6446.68s] English:** It turns out that sand goes into glass, and glass is pretty useful, too. And, you know, like, why not?  
**Translation:** 

**[6455.32s] English:** Why not? So, very important question, then, if we're living in a simulation, and the simulation is running a computer, like, what's the architecture of that computer, do you think?  
**Translation:** 

**[6471.46s] English:** So, you're saying, is it a quantum system?  
**Translation:** Vocabulary: simulation: 模拟

**[6474.56s] English:** Yeah, like, this whole quantum discussion.  
**Translation:** 

**[6476.68s] English:** Is it needed? Or can we run it on a...  
**Translation:** 

**[6480.00s] English:** you know with a risk 5 architecture uh a bunch of cpus i think it comes down to the right tool  
**Translation:** 

**[6486.42s] English:** for the job okay and so and what's the compiler yeah exactly that's that's my question how do i  
**Translation:** 

**[6492.74s] English:** get that job be the universe compiler um uh and so there as far as we know quantum quantum quantum  
**Translation:** 

**[6501.02s] English:** systems are the bottom of the pile of turtles so far yeah and so we don't know efficient ways  
**Translation:** 

**[6508.22s] English:** to implement quantum systems without using quantum computers yeah and that's totally outside  
**Translation:** 

**[6513.42s] English:** of everything we've talked about but but who runs that quantum computer yeah right so if it if it if  
**Translation:** 

**[6518.96s] English:** we really are living in a simulation then is it bigger quantum computers is it different ones like  
**Translation:** 

**[6525.40s] English:** how does that work out how does that scale well it's it's the same size it's the same size but  
**Translation:** 

**[6530.76s] English:** then but then the thought of the simulation is that you don't have to run the whole thing  
**Translation:** 

**[6534.10s] English:** that you know we humans are cognitively very limited checkpoints  
**Translation:** Vocabulary: checkpoints: 检查点; cognitively: 认知上

**[6537.40s] English:** checkpoints  
**Translation:** 

**[6538.22s] English:** and uh and if we the point at which we human so you basically do minimal amount of uh what is it  
**Translation:** 

**[6547.38s] English:** uh the swift does um on right copy on right yeah so you only yeah you only adjust the simulation  
**Translation:** 

**[6554.60s] English:** parallel universe theories right and so and so every time a decision's made yeah somebody opens  
**Translation:** 

**[6561.02s] English:** the short ringer box then there's a fork and then this could happen and and then uh thank you for uh  
**Translation:** 

**[6568.22s] English:** but considering the possibility but yeah so it may not require you know the entirety of the universe  
**Translation:** Vocabulary: entirety: 整个宇宙

**[6573.74s] English:** to simulate it but it's um interesting to think about uh as we create this this higher and higher  
**Translation:** 

**[6581.00s] English:** fidelity systems but i do want to ask on the on the quantum computer side because everything we've  
**Translation:** Vocabulary: fidelity: 清晰度; simulate: 模拟

**[6587.36s] English:** talked about with us with your work with sci-fi with everything with compilers none of that  
**Translation:** 

**[6592.74s] English:** includes quantum computers right that's true so  
**Translation:** 

**[6596.42s] English:** do you ever  
**Translation:** 

**[6598.22s] English:** thought  
**Translation:** 

**[6600.00s] English:** About what this whole serious engineering work of quantum computers looks like, of compilers, of architectures, all of that kind of stuff.  
**Translation:** 

**[6610.64s] English:** So I've looked at it a little bit.  
**Translation:** Vocabulary: compilers: 编译器

**[6611.82s] English:** I know almost nothing about it, which means that at some point I will have to find an excuse to get involved because that's how it works.  
**Translation:** 

**[6618.56s] English:** Do you think that's a thing to be – with your little tingly senses of the timing of when to be involved, is it not yet?  
**Translation:** Vocabulary: tingly: 麻酥酥

**[6626.42s] English:** Well, so the thing I do really well is I jump into messy systems and figure out how to make them – figure out what the truth in the situation is.  
**Translation:** 

**[6635.48s] English:** Try to figure out what the unifying theory is, how to factor the complexity, how to find a beautiful answer to a problem that has been well studied and lots of people have bashed their heads against it.  
**Translation:** Vocabulary: bashed: 撞头; complexity: 复杂性; unifying: 统一理论

**[6646.98s] English:** I don't know that quantum computers are mature enough and accessible enough to be figured out yet.  
**Translation:** 

**[6653.24s] English:** And the –  
**Translation:** 

**[6656.42s] English:** I think the open question with quantum computers is, is there a useful problem that gets solved with a quantum computer that makes it worth the economic cost of having one of these things and having legions of people that set it up?  
**Translation:** 

**[6671.46s] English:** You go back to the 50s, right, and there's the projections of the world will only need seven computers, right?  
**Translation:** Vocabulary: projections: 预测

**[6677.70s] English:** Yeah.  
**Translation:** 

**[6678.14s] English:** Well, and part of that was that people hadn't figured out what they're useful for.  
**Translation:** 

**[6681.72s] English:** What are the algorithms we want to run?  
**Translation:** 

**[6683.18s] English:** What are the problems that get solved?  
**Translation:** 

**[6684.30s] English:** And this comes back to how do we make the world?  
**Translation:** 

**[6686.42s] English:** Either economically or making somebody's life better or like solving a problem that wasn't solved before, things like this.  
**Translation:** Vocabulary: economically: 经济上

**[6693.24s] English:** And I think that just we're a little bit too early in that development cycle because it's still like literally a science project, not a negative connotation, right?  
**Translation:** 

**[6701.46s] English:** It's literally a science project and the progress there is amazing.  
**Translation:** Vocabulary: connotation: 隐含意义

**[6705.48s] English:** And so I don't know if it's 10 years away, if it's two years away, exactly where that breakthrough happens.  
**Translation:** 

**[6711.52s] English:** But you look at machine learning, it –  
**Translation:** 

**[6716.42s] English:** We went through a few winters before the AlexNet transition.  
**Translation:** 

**[6720.00s] English:** And then suddenly it had its breakout moment.  
**Translation:** Vocabulary: breakout: 爆发

**[6723.02s] English:** And that was the catalyst that then drove the talent flocking into it.  
**Translation:** 

**[6727.62s] English:** That's what drove the economic applications of it.  
**Translation:** Vocabulary: catalyst: 催化剂; flocking: 蜂拥

**[6730.20s] English:** That's what drove the technology to go faster because you now have more minds thrown at  
**Translation:** 

**[6735.02s] English:** the problem.  
**Translation:** 

**[6735.90s] English:** This is what caused a serious knee in deep learning and the algorithms that we're using.  
**Translation:** 

**[6742.24s] English:** And so I think that's what quantum needs to go through.  
**Translation:** 

**[6745.44s] English:** And so right now it's in that formidable finding itself, getting literally the physics  
**Translation:** 

**[6751.06s] English:** figured out.  
**Translation:** Vocabulary: formidable: 强大的

**[6753.34s] English:** And then it has to figure out the application that makes this useful.  
**Translation:** 

**[6757.68s] English:** Yeah, but I'm not skeptical that I think that will happen.  
**Translation:** Vocabulary: skeptical: 怀疑的

**[6760.82s] English:** I think it's just 10 years away, something like that.  
**Translation:** 

**[6763.48s] English:** I forgot to ask, what programming language do you think the simulation is written in?  
**Translation:** Vocabulary: simulation: 模拟

**[6768.70s] English:** Probably Lisp.  
**Translation:** 

**[6771.68s] English:** So not Swift.  
**Translation:** 

**[6772.72s] English:** Like if you were to bet.  
**Translation:** 

**[6775.44s] English:** Yeah, I'll just leave it at that.  
**Translation:** 

**[6778.12s] English:** So, I mean, we've mentioned that you worked with all these companies.  
**Translation:** 

**[6781.32s] English:** We've talked about all these projects.  
**Translation:** 

**[6783.68s] English:** It's kind of like if we just step back and zoom out about the way you did that work.  
**Translation:** 

**[6790.04s] English:** And we look at COVID times, this pandemic we're living through that may, if I look at  
**Translation:** Vocabulary: pandemic: 全球疫情

**[6795.42s] English:** the way Silicon Valley folks are talking about it, the way MIT is talking about it, this  
**Translation:** 

**[6800.10s] English:** might last for a long time.  
**Translation:** 

**[6802.84s] English:** Not just the virus, but the...  
**Translation:** 

**[6805.44s] English:** The remote nature.  
**Translation:** 

**[6808.32s] English:** The economic impact.  
**Translation:** 

**[6809.64s] English:** I mean, yeah, it's going to be a mess.  
**Translation:** 

**[6812.10s] English:** Do you think, what's your prediction?  
**Translation:** 

**[6814.50s] English:** I mean, from sci-fi to Google to just all the places you worked in, just Silicon Valley,  
**Translation:** 

**[6823.38s] English:** you're in the middle of it.  
**Translation:** 

**[6824.22s] English:** What do you think is, how is this whole place going to change?  
**Translation:** 

**[6826.56s] English:** Yeah.  
**Translation:** 

**[6826.82s] English:** So, I mean, I really can only speak to the tech perspective.  
**Translation:** 

**[6830.44s] English:** I am in that bubble.  
**Translation:** 

**[6833.06s] English:** I think it's going to be really interesting.  
**Translation:** 

**[6835.44s] English:** Because the Zoom culture of being remote and on video chat all the time.  
**Translation:** 

**[6840.00s] English:** has really interesting effects on people.  
**Translation:** 

**[6842.02s] English:** So on the one hand, it's a great normalizer.  
**Translation:** 

**[6844.64s] English:** It's a normalizer that I think will help communities of people  
**Translation:** 

**[6849.40s] English:** that have traditionally been underrepresented  
**Translation:** 

**[6851.54s] English:** because now you're taking, in some cases, a face-off  
**Translation:** Vocabulary: underrepresented: 代表性不足

**[6855.90s] English:** because you don't have to have a camera going, right?  
**Translation:** 

**[6858.74s] English:** And so you can have conversations without physical appearance  
**Translation:** 

**[6860.88s] English:** being part of the dynamic, which is pretty powerful.  
**Translation:** 

**[6864.34s] English:** You're taking remote employees that have already been remote  
**Translation:** 

**[6866.82s] English:** and you're saying you're now on the same level  
**Translation:** 

**[6869.74s] English:** and footing as everybody else.  
**Translation:** 

**[6871.38s] English:** Nobody gets whiteboards.  
**Translation:** 

**[6873.14s] English:** You're not going to be the one person  
**Translation:** Vocabulary: whiteboards: 白板

**[6874.52s] English:** that doesn't get to be participating in the whiteboard conversation,  
**Translation:** 

**[6877.14s] English:** and that's pretty powerful.  
**Translation:** Vocabulary: whiteboard: 白板会议

**[6880.30s] English:** You're forcing people to think asynchronously in some cases  
**Translation:** 

**[6884.86s] English:** because it's hard to just get people physically together,  
**Translation:** Vocabulary: asynchronously: 不同时地

**[6888.24s] English:** and the bumping into each other forces people  
**Translation:** 

**[6889.98s] English:** to find new ways to solve those problems,  
**Translation:** 

**[6892.54s] English:** and I think that that leads to more inclusive behavior, which is good.  
**Translation:** 

**[6896.48s] English:** On the other hand, it's also, it just sucks.  
**Translation:** Vocabulary: inclusive: 包容的

**[6899.74s] English:** Right?  
**Translation:** 

**[6900.78s] English:** And so...  
**Translation:** 

**[6902.40s] English:** The actual communication just sucks being not with people  
**Translation:** 

**[6908.64s] English:** on a daily basis and collaborating with them.  
**Translation:** Vocabulary: collaborating: 合作

**[6911.44s] English:** Yeah, all of that.  
**Translation:** 

**[6913.00s] English:** I mean, everything, this whole situation is terrible.  
**Translation:** 

**[6915.56s] English:** What I meant primarily was the...  
**Translation:** 

**[6918.94s] English:** I think that most humans like working physically with humans.  
**Translation:** 

**[6922.92s] English:** I think this is something that not everybody,  
**Translation:** 

**[6924.62s] English:** but many people are programmed to do,  
**Translation:** 

**[6927.00s] English:** and I think that we get something out of that  
**Translation:** 

**[6929.12s] English:** that is very hard to do.  
**Translation:** 

**[6929.74s] English:** It's hard to express, at least for me,  
**Translation:** 

**[6931.36s] English:** and so maybe this isn't true of everybody.  
**Translation:** 

**[6934.44s] English:** And so the question to me is,  
**Translation:** 

**[6936.22s] English:** when you get through that time of adaptation,  
**Translation:** Vocabulary: adaptation: 适应期

**[6939.74s] English:** you get out of March and April,  
**Translation:** 

**[6941.86s] English:** and you get into December,  
**Translation:** 

**[6943.06s] English:** and you get into next March if it's not changed.  
**Translation:** 

**[6946.22s] English:** It's already terrifying.  
**Translation:** Vocabulary: terrifying: 令人恐惧的

**[6947.70s] English:** Well, you think about that,  
**Translation:** 

**[6949.04s] English:** and you think about what is the nature of work,  
**Translation:** 

**[6951.14s] English:** and how do we adapt?  
**Translation:** 

**[6952.64s] English:** And humans are very adaptable species, right?  
**Translation:** Vocabulary: adaptable: 适应性强的

**[6954.96s] English:** We can learn things,  
**Translation:** 

**[6957.08s] English:** and when we're forced to,  
**Translation:** 

**[6958.04s] English:** and there's a catalyst,  
**Translation:** 

**[6958.86s] English:** to make that happen.  
**Translation:** 

**[6959.90s] English:** And so I think that's one of the things  
**Translation:** 

**[6960.02s] English:** that we need to do.  
**Translation:** 

**[6960.08s] English:** And I think that's one of the things  
**Translation:** 

**[6960.14s] English:** that we need to do.  
**Translation:** 

**[6960.00s] English:** and so what is it that comes out of this and are we better or worse off right i think that  
**Translation:** 

**[6965.20s] English:** you know you look at the bay area housing prices are insane well why well there's a high incentive  
**Translation:** Vocabulary: incentive: 激励

**[6970.74s] English:** to be physically located because if you don't have proximity you end up paying for it and commute  
**Translation:** 

**[6976.60s] English:** right and there's there has been huge social social pressure in terms of like you will be  
**Translation:** Vocabulary: proximity: 近距离

**[6982.64s] English:** there for the meeting right or whatever scenario it is and i think that's gonna be way better i  
**Translation:** 

**[6988.30s] English:** think it's gonna be much more the norm to have remote employees and i think this is gonna be  
**Translation:** 

**[6992.32s] English:** really great do you uh do you have friends or do you hear of people moving yeah i i know one family  
**Translation:** 

**[6998.62s] English:** friend that moved they moved back to michigan and uh you know they were a family with three kids  
**Translation:** 

**[7005.50s] English:** living in a small apartment and like we're going insane right and they're in tech uh  
**Translation:** 

**[7012.26s] English:** husband works for google so first of all friends of mine have are in the process of  
**Translation:** 

**[7018.06s] English:** or  
**Translation:** 

**[7018.30s] English:** are have already lost the business the thing that represents their passion their dream it could be  
**Translation:** 

**[7023.66s] English:** small entrepreneur projects but it could be large businesses like people that run gyms like do  
**Translation:** 

**[7028.38s] English:** restaurants like tons of things yeah so but also people like look them at themselves in the mirror  
**Translation:** Vocabulary: entrepreneur: 商人

**[7033.98s] English:** and ask the question of like what do i want to do in life for some reason they don't they haven't  
**Translation:** 

**[7038.94s] English:** done it until covet like yeah they really ask that question and that results often in moving or  
**Translation:** Vocabulary: covet: 羡慕

**[7044.30s] English:** leaving the company or with starting your own business or transitioning to different company  
**Translation:** 

**[7050.50s] English:** do you think we're going to see that a lot like in um i well i can't speak to that i mean we're  
**Translation:** Vocabulary: transitioning: 转换

**[7057.20s] English:** definitely going to see it at a higher frequency than we did before um just because i think what  
**Translation:** 

**[7061.64s] English:** you're trying to say is there are decisions that you make yourself and big life decisions that you  
**Translation:** 

**[7067.16s] English:** make yourself and like i'm gonna like quit my job and start a new thing there's also decisions to  
**Translation:** 

**[7071.84s] English:** get made for you like i got fired from my job  
**Translation:** 

**[7074.30s] English:** what am i gonna do right and that's not a decision that you think about but you're forced to act  
**Translation:** 

**[7080.00s] English:** Okay. And so I think that those you're forced to act kind of moments where like, you know, global pandemic comes and wipes out the economy and now your business doesn't exist. I think that does lead to more reflection, right? Because you're less anchored on what you have. And it's not a, what do I have to lose versus what do I have to gain? A, B comparison. It's more of a fresh slate. Cool. I could do anything now. Do I want to do the same thing I was doing? Did that make me happy?  
**Translation:** Vocabulary: anchored: 根深蒂固; pandemic: 全球疫情; slate: 空白 slate

**[7107.68s] English:** Is this now time to go back to college and take a class and learn a new skill? Is this a time to spend time with family? If you can afford to do that, is this time to like, you know, literally move in with the parents, right?  
**Translation:** 

**[7120.92s] English:** I mean, all these things that were not normative before suddenly become, I think, very, the value system has changed. And I think that's actually a good thing in the short term, at least, because it leads to, you know, there's kind of been an over optimization along one set of priorities for the world. And now maybe we'll get to a more balanced and more interesting world where people are doing different things. I think it could be good. I think there could be more innovation that comes out of it, for example.  
**Translation:** Vocabulary: normative: 规范的; optimization: 优化; priorities: 优先级

**[7150.00s] English:** What do you think about all the social chaos we're in the middle of?  
**Translation:** 

**[7153.92s] English:** It sucks.  
**Translation:** 

**[7155.88s] English:** Let me ask you, do you think it's all going to be okay?  
**Translation:** 

**[7160.92s] English:** Well, I think humanity will survive.  
**Translation:** 

**[7164.00s] English:** From an existential perspective?  
**Translation:** 

**[7165.44s] English:** Yeah, I don't think the virus is going to kill all the humans. I don't think all the humans are going to kill all the humans. I think that's unlikely.  
**Translation:** 

**[7172.72s] English:** But I look at it as progress required.  
**Translation:** 

**[7180.00s] English:** There's a catalyst, right? So you need a reason for people to be willing to do things that are uncomfortable. I think that the US, at least, but I think the world in general is a pretty unoptimal place to live in for a lot of people. And I think that what we're seeing right now is we're seeing a lot of unhappiness.  
**Translation:** Vocabulary: catalyst: 推动因素; unhappiness: 不快乐; unoptimal: 不尽如人意

**[7200.00s] English:** and because because of all the pressure because of all the the badness in the world that's coming  
**Translation:** 

**[7205.72s] English:** together it's really kind of igniting some of that debate that should have happened a long time ago  
**Translation:** Vocabulary: igniting: 点燃

**[7209.70s] English:** right i mean i think that we'll see more progress you're asking about offline you're asking about  
**Translation:** 

**[7213.68s] English:** politics and wouldn't be great if politics move faster because there's all these problems in the  
**Translation:** 

**[7216.78s] English:** world we can move it well people are intentional or inherently uh conservative and so if you're  
**Translation:** 

**[7223.02s] English:** talking about conservative people particularly if they have heavy burdens on their shoulders  
**Translation:** Vocabulary: intentional: 有意图的

**[7227.26s] English:** because they represent literally thousands of people um it makes sense to be conservative  
**Translation:** 

**[7232.80s] English:** but on the other hand when you need change how do you get it the global pandemic will probably  
**Translation:** Vocabulary: pandemic: 全球疫情

**[7238.48s] English:** lead to some change and it's not a directed it's not directed plan but i think that it leads to  
**Translation:** 

**[7245.52s] English:** people asking really interesting questions and some of those questions should have been asked  
**Translation:** 

**[7248.70s] English:** a long time ago well let me know if if you've observed this as well something that's bothered  
**Translation:** 

**[7253.94s] English:** me in the machine learning community i'm guessing it might be  
**Translation:** Vocabulary: bothered: 困扰

**[7257.24s] English:** prevalent in other places is um something that feels like in 2020 increase the level of toxicity  
**Translation:** 

**[7264.42s] English:** like people are just quicker to pile on to just be they're just harsh on each other to to like  
**Translation:** Vocabulary: prevalent: 普遍; toxicity: 毒化

**[7274.18s] English:** mob uh pick a person that screwed up and like make it a big thing yeah and uh is there something  
**Translation:** 

**[7283.94s] English:** that we can like yeah have you observed that  
**Translation:** 

**[7287.18s] English:** um  
**Translation:** 

**[7287.24s] English:** other places uh is there is there some way out of this i think there's a inherent thing in  
**Translation:** 

**[7291.76s] English:** humanity that's kind of an us versus them thing which is that you want to succeed and how do you  
**Translation:** 

**[7296.62s] English:** succeed well it's relative to somebody else and so what what's happening in at least in some part  
**Translation:** 

**[7303.04s] English:** is that with the internet and with online communication the world's getting smaller  
**Translation:** 

**[7308.06s] English:** right and so we're having some of the the social ties of like my name my town versus your town's  
**Translation:** 

**[7315.62s] English:** football team  
**Translation:** 

**[7316.22s] English:** yeah  
**Translation:** 

**[7317.18s] English:** right turn into a much larger larger  
**Translation:** 

**[7320.00s] English:** and yet shallower problems and uh people don't have time the incentives so if clickbait and like  
**Translation:** Vocabulary: clickbait: 诱饵标题; incentives: 激励; shallower: 更浅

**[7327.40s] English:** all these things kind of really really feed into this machine and i don't know where that goes  
**Translation:** 

**[7331.60s] English:** yeah i mean the reason i think about that i i mentioned to you this offline a little bit but  
**Translation:** 

**[7337.68s] English:** uh you know i've uh a few difficult conversations scheduled some of them political related some of  
**Translation:** 

**[7345.50s] English:** them within the community uh difficult personalities that went through some stuff  
**Translation:** 

**[7350.32s] English:** i mean one of them i've talked before i will talk again is yann lacoon he got a little bit of crap  
**Translation:** 

**[7355.60s] English:** on twitter uh for uh for uh talking about a particular paper and the bias within a data set  
**Translation:** 

**[7362.50s] English:** and then there's been a huge uh in my view and i'm willing comfortable saying it uh irrational  
**Translation:** 

**[7370.44s] English:** over exaggerated pile on on his comments because uh  
**Translation:** Vocabulary: exaggerated: 夸大其词; irrational: 不合逻辑

**[7375.50s] English:** he made pretty basic comments about the fact that if there's bias in the data there's going to be  
**Translation:** 

**[7380.76s] English:** bias in the results so we should not have bias in the data but people piled on to him because he  
**Translation:** 

**[7387.00s] English:** said he trivialized the problem of bias like it's a lot more than just bias in the data but like  
**Translation:** 

**[7393.66s] English:** yes that's a very good point but that's that's not what he was saying  
**Translation:** Vocabulary: trivialized: 轻描淡写

**[7398.20s] English:** it's not what he was saying and the response like the implied response that he's basically  
**Translation:** 

**[7404.68s] English:** sexist  
**Translation:** 

**[7405.50s] English:** and racist uh is uh is something that completely drives away the possibility of nuanced discussion  
**Translation:** 

**[7412.04s] English:** yeah one nice thing about like a pocket long form of conversation is you can talk it out  
**Translation:** Vocabulary: nuanced: 细致入微

**[7419.90s] English:** you can lay your reasoning out and even if you're wrong you can still show that you're a good human  
**Translation:** 

**[7426.78s] English:** being underneath it you know your point about you can't have a productive discussion well how do you  
**Translation:** 

**[7431.42s] English:** get to that point where people can turn they can learn they can listen they can  
**Translation:** 

**[7435.50s] English:** think they can engage versus just being a uh a shallow like  
**Translation:** 

**[7440.00s] English:** like, and then keep moving, right?  
**Translation:** 

**[7442.50s] English:** And I don't think that progress really comes from that, right?  
**Translation:** 

**[7446.92s] English:** And I don't think that one should expect that.  
**Translation:** 

**[7449.66s] English:** I think that you'd see that as reinforcing individual circles  
**Translation:** Vocabulary: reinforcing: 加强

**[7453.08s] English:** and the us versus them thing, and I think that's fairly divisive.  
**Translation:** 

**[7457.60s] English:** Yeah, I think there's a big role in, like,  
**Translation:** Vocabulary: divisive: 分裂的

**[7461.10s] English:** the people that bother me most on Twitter when I observe things  
**Translation:** 

**[7465.10s] English:** is not the people who get very emotional and angry, like, over the top.  
**Translation:** 

**[7470.00s] English:** It's the people who, like, prop them up.  
**Translation:** 

**[7474.00s] English:** It's all the, it's that.  
**Translation:** 

**[7475.94s] English:** I think what should be the, we should teach each other  
**Translation:** 

**[7479.36s] English:** is to be sort of empathetic.  
**Translation:** Vocabulary: empathetic: 换位思考

**[7482.42s] English:** The thing that it's really easy to forget,  
**Translation:** 

**[7484.70s] English:** particularly on, like, Twitter or the Internet or an email,  
**Translation:** 

**[7487.66s] English:** is that sometimes people just have a bad day, right?  
**Translation:** 

**[7490.76s] English:** You have a bad day or you're, like, I've been in this situation  
**Translation:** 

**[7494.16s] English:** where it's, like, between meetings, like, fire off a quick response to an email  
**Translation:** 

**[7497.10s] English:** because I want to, like, help get something unblocked.  
**Translation:** 

**[7500.00s] English:** And phrase it really objectively wrong, I screwed up,  
**Translation:** 

**[7504.96s] English:** and suddenly this is now something that sticks with people.  
**Translation:** Vocabulary: objectively: 客观地

**[7508.64s] English:** And it's not because they're bad.  
**Translation:** 

**[7510.52s] English:** It's not because you're bad.  
**Translation:** 

**[7511.80s] English:** It's just psychology of, like, you said a thing, it sticks with you.  
**Translation:** 

**[7516.00s] English:** You didn't mean it that way, but it really impacted somebody  
**Translation:** 

**[7518.40s] English:** because the way they interpret it,  
**Translation:** 

**[7520.86s] English:** and this is just an aspect of working together as humans.  
**Translation:** Vocabulary: interpret: 解释

**[7523.42s] English:** And I have a lot of optimism in the long term, the very long term,  
**Translation:** 

**[7527.02s] English:** about what we as humanity can do,  
**Translation:** Vocabulary: optimism: 樂觀

**[7529.12s] English:** but I think that's going to be,  
**Translation:** 

**[7530.02s] English:** it's just always a rough ride.  
**Translation:** 

**[7531.20s] English:** And you came into this by saying, like,  
**Translation:** 

**[7533.12s] English:** what does COVID and all the social strife that's happening right now mean?  
**Translation:** Vocabulary: strife: 纷争

**[7538.00s] English:** And I think that it's really bad in the short term,  
**Translation:** 

**[7540.90s] English:** but I think it will lead to progress.  
**Translation:** 

**[7542.48s] English:** And for that, I'm very thankful.  
**Translation:** 

**[7545.80s] English:** Yeah, it's painful in the short term, though.  
**Translation:** 

**[7547.94s] English:** Well, yeah, I mean, people are out of jobs.  
**Translation:** 

**[7549.78s] English:** Like, some people can't eat.  
**Translation:** 

**[7550.86s] English:** Like, it's horrible.  
**Translation:** 

**[7553.32s] English:** But, you know, it's progress.  
**Translation:** 

**[7556.78s] English:** So we'll see what happens.  
**Translation:** 

**[7558.56s] English:** I mean, the real question is,  
**Translation:** 

**[7559.68s] English:** when you're in a situation like this,  
**Translation:** 

**[7560.04s] English:** when you're in a situation like this,  
**Translation:** 

**[7560.00s] English:** look back 10 years 20 years 100 years from now how do we evaluate the decisions are being made  
**Translation:** 

**[7565.30s] English:** right now i think that's really the way you can frame that and look at it and you say you know  
**Translation:** Vocabulary: evaluate: 评估

**[7571.60s] English:** you integrate across all the short-term horribleness that's happening and you look at what that means  
**Translation:** 

**[7577.06s] English:** and is the you know improvement across the world or the regression across the world  
**Translation:** Vocabulary: horribleness: 糟糕情况; integrate: 整合; regression: 倒退

**[7580.98s] English:** uh significant enough to make it a good or bad thing i think that's the question  
**Translation:** 

**[7585.54s] English:** yeah and for that it's good to study history i mean one of the big problems for me right now is  
**Translation:** 

**[7592.14s] English:** i'm reading the rise and fall of the third reich okay light reading so everything is just i just  
**Translation:** 

**[7599.98s] English:** see parallels and it means it's it's you have to be really careful not to overstep it but just the  
**Translation:** Vocabulary: overstep: 逾越

**[7606.06s] English:** the thing that worries me the most is the pain that people feel when uh come when a few things  
**Translation:** 

**[7613.82s] English:** combine which is like economic depression  
**Translation:** 

**[7615.54s] English:** which is quite possible in this country and then just being disrespected yeah uh by in some kind of  
**Translation:** 

**[7622.36s] English:** way which the german people were really disrespected by most of the world uh like in a way that's over  
**Translation:** Vocabulary: disrespected: 不受尊重

**[7629.50s] English:** the top that something can it can build up and then all you need is a charismatic leader uh  
**Translation:** 

**[7635.68s] English:** just to go either positive or negative and both work uh as long as they're charismatic and there's  
**Translation:** 

**[7641.84s] English:** it's taking advantage of again that that inflection point that the world's in  
**Translation:** 

**[7645.52s] English:** and what they do with it could be good or bad yeah and so it's a good way to think about times  
**Translation:** Vocabulary: inflection: 转折点

**[7652.04s] English:** now like on an individual level what we decide to do is when when history is written you know  
**Translation:** 

**[7658.22s] English:** 30 years from now what happened in 2020 probably history is going to remember 2020 yeah i think  
**Translation:** 

**[7663.64s] English:** either for good or bad and it's like up to us to write it so it's good well one of the things i've  
**Translation:** 

**[7670.34s] English:** observed that i find fascinating is most people act as though the world doesn't change  
**Translation:** 

**[7675.52s] English:** you make decisions knowingly right  
**Translation:** 

**[7680.00s] English:** you make a decision where you're predicting the future based on what you've  
**Translation:** Vocabulary: knowingly: 明知故犯

**[7683.28s] English:** seen in the recent past.  
**Translation:** 

**[7684.52s] English:** And so if something's always been,  
**Translation:** 

**[7686.04s] English:** it's rained every single day,  
**Translation:** 

**[7687.32s] English:** then of course you expect it to rain today too.  
**Translation:** 

**[7689.20s] English:** Right.  
**Translation:** 

**[7689.98s] English:** On the other hand,  
**Translation:** 

**[7690.44s] English:** the world changes all the time.  
**Translation:** 

**[7693.36s] English:** Yeah.  
**Translation:** 

**[7694.10s] English:** Constantly like for better and for worse.  
**Translation:** 

**[7696.50s] English:** Right.  
**Translation:** 

**[7696.92s] English:** And so the question is,  
**Translation:** 

**[7697.66s] English:** if you're interested in something that's not right,  
**Translation:** 

**[7700.82s] English:** what is the inflection point that led to a change?  
**Translation:** 

**[7702.72s] English:** And you can look to history for this.  
**Translation:** 

**[7704.50s] English:** Like what is,  
**Translation:** 

**[7705.08s] English:** what is the catalyst that led to that,  
**Translation:** Vocabulary: catalyst: 催化剂

**[7707.16s] English:** that explosion that led to that bill that led to the,  
**Translation:** 

**[7710.00s] English:** like you,  
**Translation:** 

**[7710.62s] English:** you can kind of work your way backwards from that.  
**Translation:** 

**[7713.04s] English:** And maybe if you pull together the right people and you get the right ideas  
**Translation:** Vocabulary: backwards: 逆向

**[7716.60s] English:** together,  
**Translation:** 

**[7716.86s] English:** you can actually start driving that change and doing it in a way that's  
**Translation:** 

**[7719.78s] English:** productive and hurts fewer people.  
**Translation:** 

**[7721.74s] English:** Yeah.  
**Translation:** 

**[7722.04s] English:** Like a single person,  
**Translation:** 

**[7723.04s] English:** a single event can turn all of this.  
**Translation:** 

**[7724.74s] English:** Absolutely.  
**Translation:** 

**[7725.24s] English:** Everything starts somewhere.  
**Translation:** 

**[7726.14s] English:** And often it's a combination of multiple factors,  
**Translation:** 

**[7728.34s] English:** but,  
**Translation:** 

**[7729.34s] English:** but yeah,  
**Translation:** 

**[7729.84s] English:** this is these,  
**Translation:** 

**[7730.62s] English:** these things can be engineered.  
**Translation:** 

**[7732.62s] English:** That's actually the optimistic view that I'm,  
**Translation:** Vocabulary: optimistic: 乐观的

**[7735.32s] English:** I'm a long-term optimist on pretty much everything and human nature.  
**Translation:** 

**[7738.84s] English:** You know,  
**Translation:** Vocabulary: optimist: 乐天派

**[7739.32s] English:** we can look to all,  
**Translation:** 

**[7739.90s] English:** all the negative things that the humanity has,  
**Translation:** 

**[7742.16s] English:** all the pettiness and all the like self self-servingness and the just the,  
**Translation:** 

**[7748.00s] English:** the cruelty,  
**Translation:** Vocabulary: pettiness: 琐碎小事

**[7748.94s] English:** right.  
**Translation:** 

**[7749.72s] English:** The,  
**Translation:** 

**[7750.00s] English:** the biases,  
**Translation:** 

**[7751.04s] English:** the just humans can be very horrible,  
**Translation:** 

**[7753.28s] English:** but on the other hand,  
**Translation:** 

**[7754.38s] English:** we're capable of amazing things.  
**Translation:** 

**[7756.96s] English:** And,  
**Translation:** 

**[7757.44s] English:** and the progress across,  
**Translation:** 

**[7760.26s] English:** you know,  
**Translation:** 

**[7760.58s] English:** a hundred year chunks is striking.  
**Translation:** 

**[7763.46s] English:** And even across decades,  
**Translation:** 

**[7765.24s] English:** it's,  
**Translation:** 

**[7765.58s] English:** we've come a long ways and there's still a long ways to go,  
**Translation:** 

**[7767.84s] English:** but that doesn't mean that we've stopped.  
**Translation:** 

**[7769.90s] English:** Yeah.  
**Translation:** 

**[7770.32s] English:** The kind of stuff we've done in the last hundred years is,  
**Translation:** 

**[7773.38s] English:** is unbelievable.  
**Translation:** 

**[7774.88s] English:** It's kind of scary to think what's going to happen this hundred years.  
**Translation:** 

**[7777.34s] English:** It's scary,  
**Translation:** 

**[7777.84s] English:** like exciting,  
**Translation:** 

**[7779.06s] English:** like scary in a sense that it's kind of sad that the kind of technology is going to come out in 10,  
**Translation:** 

**[7784.22s] English:** 20,  
**Translation:** 

**[7784.50s] English:** 30 years.  
**Translation:** 

**[7785.44s] English:** We're probably too old to really appreciate it.  
**Translation:** 

**[7787.82s] English:** Cause you don't grow up with it.  
**Translation:** 

**[7788.90s] English:** It'll be like kids these days with their virtual reality and their,  
**Translation:** 

**[7792.12s] English:** their TikToks and stuff like this.  
**Translation:** 

**[7794.56s] English:** Like,  
**Translation:** 

**[7794.76s] English:** how does this thing?  
**Translation:** 

**[7795.66s] English:** And like,  
**Translation:** 

**[7796.74s] English:** come on,  
**Translation:** 

**[7797.16s] English:** give me my,  
**Translation:** 

**[7797.70s] English:** you know,  
**Translation:** 

**[7798.10s] English:** static photo.  
**Translation:** 

**[7799.90s] English:** You know,  
**Translation:** 

**[7800.00s] English:** my commodore 64 yeah yeah exactly okay uh sorry we kind of skipped over let me ask on um  
**Translation:** 

**[7808.24s] English:** you know the machine learning world has been kind of inspired their imagination captivated  
**Translation:** 

**[7815.66s] English:** with gpt3 and these language models i thought it'd be cool to get your opinion on it what's  
**Translation:** Vocabulary: captivated: 深深吸引

**[7822.42s] English:** your thoughts on this exciting world of um it connects to computation actually uh is of  
**Translation:** 

**[7830.58s] English:** language models that are huge yeah and take multiple many many computers not just to train  
**Translation:** Vocabulary: computation: 计算

**[7837.30s] English:** but to also do inference on sure well i mean it depends on what you're speaking to there but i  
**Translation:** 

**[7843.60s] English:** mean i think that there's been a pretty well understood maximum deep learning that if you  
**Translation:** Vocabulary: inference: 推断

**[7848.76s] English:** make the model bigger and you shove more data into it assuming you train it right  
**Translation:** 

**[7852.42s] English:** you have a good model architecture that you'll get a better model out and so on the one hand  
**Translation:** Vocabulary: shove: 强行塞入

**[7857.04s] English:** gpt3 was not that surprising um on the other hand a tremendous amount of engineering went  
**Translation:** 

**[7862.20s] English:** into making it possible um the implications of it are pretty huge i think that when gpt2  
**Translation:** 

**[7868.22s] English:** came out there was a very provocative blog post from open ai talking about  
**Translation:** 

**[7871.98s] English:** you know we're not going to release it because of the social damage it could cause if it's misused  
**Translation:** Vocabulary: misused: 用错; provocative: 激进

**[7876.24s] English:** um i think that's still a concern i think that we need to look at how  
**Translation:** 

**[7881.48s] English:** um technology can be used to do that and i think that's a big concern i think that we need to look  
**Translation:** 

**[7882.40s] English:** at how technology is applied and you know well-meaning tools can be applied in very horrible  
**Translation:** 

**[7886.32s] English:** ways and they can have very profound impact on that um i think the gpt3 is a huge technical  
**Translation:** Vocabulary: profound: 深远

**[7892.90s] English:** achievement and what will gpt4 be will probably be bigger more expensive to train  
**Translation:** 

**[7897.54s] English:** really cool uh architectural tricks what do you think is there um i don't know how much  
**Translation:** Vocabulary: architectural: 建筑学的

**[7904.54s] English:** thought you've done on distributed computing uh is there is there some technical challenges that  
**Translation:** 

**[7912.40s] English:** you're dealing with that you're hopeful about exploring in terms of you know a system that  
**Translation:** Vocabulary: computing: 计算

**[7917.52s] English:** like a piece of code that you  
**Translation:** 

**[7920.00s] English:** You know, with GPT-4, that might have, I don't know, hundreds of trillions of parameters would have to run on thousands of computers.  
**Translation:** Vocabulary: trillions: 万亿

**[7931.46s] English:** Is there some hope that we can make that happen?  
**Translation:** 

**[7935.32s] English:** Yeah, well, I mean, today you can write a check and get access to a thousand TPU cores and do really interesting large-scale training and inference and things like that in Google Cloud, for example, right?  
**Translation:** 

**[7947.30s] English:** And so I don't think it's a question about scale.  
**Translation:** 

**[7951.30s] English:** It's a question about utility.  
**Translation:** 

**[7953.06s] English:** And when I look at the Transformer series of architectures that the GPT series is based on, it's really interesting to look at that because they're actually very simple, simple designs.  
**Translation:** 

**[7962.96s] English:** They're not recurrent.  
**Translation:** Vocabulary: recurrent: 循环的

**[7964.34s] English:** The training regimens are pretty simple.  
**Translation:** 

**[7967.04s] English:** And so they don't really reflect, like, human brains, right?  
**Translation:** Vocabulary: regimens: 训练计划

**[7971.30s] English:** But they're really good at learning language models, and they're unrolled enough that you can simulate.  
**Translation:** 

**[7977.30s] English:** Some recurrence, right?  
**Translation:** Vocabulary: recurrence: 重复; simulate: 模拟; unrolled: 展开

**[7978.98s] English:** And so the question I think about is, where does this take us?  
**Translation:** 

**[7983.32s] English:** Like, so we can just keep scaling it, have more parameters, more data, more things.  
**Translation:** 

**[7987.62s] English:** We'll get a better result for sure.  
**Translation:** 

**[7989.34s] English:** But are there architectural techniques that can lead to progress at a faster pace?  
**Translation:** 

**[7994.74s] English:** Right?  
**Translation:** 

**[7995.18s] English:** This is when, you know, how do you get, instead of just, like, making it a constant time bigger, how do you get, like, an algorithmic improvement out of this, right?  
**Translation:** Vocabulary: algorithmic: 算法的

**[8004.10s] English:** And whether it be a new training regimen, if it becomes...  
**Translation:** 

**[8007.30s] English:** Sparse networks, for example.  
**Translation:** Vocabulary: regimen: 训练计划; sparse: 稀疏的

**[8010.24s] English:** The human brain is sparse.  
**Translation:** 

**[8011.44s] English:** All these networks are dense.  
**Translation:** 

**[8013.64s] English:** The connectivity patterns can be very different.  
**Translation:** 

**[8016.12s] English:** I think this is where I get very interested, and I'm way out of my league on the deep learning side of this.  
**Translation:** 

**[8021.52s] English:** But I think that could lead to big breakthroughs.  
**Translation:** 

**[8023.34s] English:** When you talk about large-scale networks, one of the things that Jeff Dean likes to talk about, and he's given a few talks on,  
**Translation:** Vocabulary: breakthroughs: 重大突破

**[8030.98s] English:** is this idea of having a sparsely gated mixture of experts kind of a model, where you have, you know,  
**Translation:** 

**[8037.30s] English:** different nets that are trained and are really...  
**Translation:** Vocabulary: sparsely: 稀疏地

**[8040.00s] English:** good at certain kinds of tasks. And so you have this distributed across a cluster. And so you  
**Translation:** 

**[8045.16s] English:** have a lot of different computers that end up being kind of locally specialized in different  
**Translation:** Vocabulary: cluster: 计算集群

**[8048.80s] English:** demands. And then when a query comes in, you gate it and you use learned techniques to route to  
**Translation:** 

**[8054.28s] English:** different parts of the network. And then you utilize the compute resources of the entire  
**Translation:** 

**[8058.30s] English:** cluster by having specialization within it. And I don't know where that goes or when it starts to  
**Translation:** 

**[8065.14s] English:** work, but I think things like that could be really interesting as well. And on the data side too,  
**Translation:** 

**[8070.00s] English:** if you can think of data selection as a kind of programming. I mean, essentially, if you look at  
**Translation:** 

**[8077.94s] English:** like Karpathy talked about software 2.0, I mean, in a sense, data is the programming.  
**Translation:** Vocabulary: karpathy: 卡普拉希

**[8084.18s] English:** Yeah, yeah. So let me try to summarize Andre's position really quick before I disagree with it.  
**Translation:** 

**[8089.66s] English:** Yeah. So Andre Karpathy is amazing. So this is nothing personal with him. He's an amazing  
**Translation:** Vocabulary: andre: 安德烈; summarize: 概括

**[8096.18s] English:** engineer. And also a good blog post writer.  
**Translation:** 

**[8099.24s] English:** Yeah.  
**Translation:** 

**[8099.66s] English:** Well,  
**Translation:** 

**[8100.00s] English:** he's a great communicator. He's just an amazing person. He's also really sweet.  
**Translation:** Vocabulary: communicator: 沟通高手

**[8104.40s] English:** So his basic premise is that software is suboptimal. I think we can all agree to that.  
**Translation:** 

**[8111.56s] English:** He also points out that deep learning and other learning-based techniques are really great  
**Translation:** Vocabulary: premise: 基本前提; suboptimal: 次优的

**[8116.32s] English:** because you can solve problems in more structured ways with less like ad hoc code that people write  
**Translation:** 

**[8122.72s] English:** out and don't write test cases for in some cases. And so they don't even know if it works in the  
**Translation:** 

**[8129.66s] English:** real world. So if you're using systems of imperative code with deep learning models,  
**Translation:** 

**[8134.00s] English:** then you get a better result. And I think that he argues that software 2.0 is a pervasively learned  
**Translation:** Vocabulary: imperative: 命令式; pervasively: 渗透地

**[8142.42s] English:** set of models, and you get away from writing code. And he's given talks where he talks about  
**Translation:** 

**[8147.88s] English:** swapping over more and more and more parts of the code to being learned and driven that way.  
**Translation:** Vocabulary: swapping: 替换

**[8153.88s] English:** I think that works. And if you're predisposed to liking machine learning,  
**Translation:** 

**[8159.06s] English:** then I think that  
**Translation:** Vocabulary: predisposed: 倾向

**[8160.00s] English:** but that's definitely a good thing.  
**Translation:** 

**[8161.78s] English:** I think this is also good for accessibility in many ways  
**Translation:** Vocabulary: accessibility: 易于使用

**[8164.62s] English:** because certain people are not going to write C code or something.  
**Translation:** 

**[8167.80s] English:** And so having a data-driven approach to do this kind of stuff,  
**Translation:** 

**[8170.98s] English:** I think can be very valuable.  
**Translation:** 

**[8172.48s] English:** On the other hand, there are huge trade-offs.  
**Translation:** 

**[8174.22s] English:** And it's not clear to me that software 2.0 is the answer.  
**Translation:** 

**[8179.22s] English:** And probably Andre wouldn't argue  
**Translation:** 

**[8180.50s] English:** that it's the answer for every problem either.  
**Translation:** 

**[8183.10s] English:** But I look at machine learning  
**Translation:** 

**[8185.78s] English:** as not a replacement for software 1.0.  
**Translation:** 

**[8187.74s] English:** I look at it as a new programming paradigm.  
**Translation:** Vocabulary: paradigm: 编程范式

**[8190.86s] English:** And so programming paradigms,  
**Translation:** 

**[8193.02s] English:** when you look across domains,  
**Translation:** Vocabulary: paradigms: 编程范式

**[8195.30s] English:** is structured programming  
**Translation:** 

**[8197.02s] English:** where you go from go-tos to if-then-else  
**Translation:** 

**[8199.44s] English:** or functional programming from Lisp  
**Translation:** 

**[8202.12s] English:** and you start talking about higher-order functions  
**Translation:** 

**[8204.22s] English:** and values and things like this.  
**Translation:** 

**[8205.84s] English:** Or you talk about object-oriented programming.  
**Translation:** 

**[8208.02s] English:** You're talking about encapsulation, subclassing, inheritance.  
**Translation:** 

**[8210.44s] English:** You start talking about generic programming  
**Translation:** Vocabulary: encapsulation: 封装; inheritance: 继承

**[8212.48s] English:** where you start talking about code reuse  
**Translation:** 

**[8214.28s] English:** through specialization and different type instantiations.  
**Translation:** Vocabulary: instantiations: 实例化; reuse: 重用

**[8218.94s] English:** When you start talking about differentiable programming,  
**Translation:** 

**[8221.76s] English:** something that I am very excited about  
**Translation:** Vocabulary: differentiable: 可微分的

**[8224.42s] English:** in the context of machine learning,  
**Translation:** 

**[8225.92s] English:** talking about taking functions and generating variants,  
**Translation:** 

**[8229.52s] English:** like the derivative of another function.  
**Translation:** 

**[8231.22s] English:** That's a programming paradigm  
**Translation:** Vocabulary: derivative: 导数

**[8232.52s] English:** that's very useful for solving certain classes of problems.  
**Translation:** 

**[8236.20s] English:** Machine learning is amazing  
**Translation:** 

**[8237.52s] English:** at solving certain classes of problems.  
**Translation:** 

**[8239.26s] English:** You're not going to write a cat detector  
**Translation:** Vocabulary: detector: 检测器

**[8241.44s] English:** or even a language translation system by writing C code.  
**Translation:** 

**[8245.74s] English:** That's not a very productive way to do things anymore.  
**Translation:** 

**[8248.70s] English:** And so, machine learning is absolutely the right way to do that.  
**Translation:** 

**[8252.02s] English:** In fact, I would say that learned models  
**Translation:** 

**[8254.02s] English:** are really one of the best ways to work with the human world in general.  
**Translation:** 

**[8258.28s] English:** And so, anytime you're talking about sensory input of different modalities,  
**Translation:** Vocabulary: anytime: 任何时候; modalities: 感觉模式

**[8261.38s] English:** anytime that you're talking about generating things  
**Translation:** 

**[8264.24s] English:** in a way that makes sense to a human,  
**Translation:** 

**[8265.78s] English:** I think that learned models are really, really useful.  
**Translation:** 

**[8268.66s] English:** And that's because humans are very difficult to characterize.  
**Translation:** Vocabulary: characterize: 描述

**[8271.88s] English:** And so, this is a very powerful paradigm  
**Translation:** 

**[8275.06s] English:** for solving classes of problems.  
**Translation:** 

**[8276.78s] English:** But on the other hand,  
**Translation:** 

**[8277.84s] English:** imperative code is too.  
**Translation:** Vocabulary: imperative: 命令式的

**[8279.64s] English:** You're not going to write a code  
**Translation:** 

**[8280.00s] English:** right? A bootloader for your computer with a deep learning model. Deep learning models are very  
**Translation:** Vocabulary: bootloader: 启动加载程序

**[8285.30s] English:** hardware intensive. They're very energy intensive because you have a lot of parameters  
**Translation:** 

**[8290.40s] English:** and you can provably implement any function with a learned model, like this has been shown,  
**Translation:** Vocabulary: provably: 可以证明地

**[8297.40s] English:** but that doesn't make it efficient. And so if you're talking about carrying about a few orders  
**Translation:** 

**[8302.26s] English:** of magnitudes worth of energy usage, then it's useful to have other tools in the toolbox.  
**Translation:** Vocabulary: magnitudes: 数量级; toolbox: 工具箱

**[8306.56s] English:** There's also robustness too.  
**Translation:** 

**[8308.84s] English:** Yeah, exactly. All the problems of dealing with data and bias in data,  
**Translation:** Vocabulary: robustness: 稳固性

**[8312.54s] English:** all the problems of software 2.0. And one of the great things that Andre is arguing towards,  
**Translation:** 

**[8319.32s] English:** which I completely agree with him, is that when you start implementing things with deep learning,  
**Translation:** Vocabulary: implementing: 实施

**[8324.46s] English:** you need to learn from software 1.0 in terms of testing, continuous integration, how you deploy,  
**Translation:** 

**[8330.08s] English:** how do you validate, all these things and building systems around that. So that you're not just  
**Translation:** Vocabulary: deploy: 部署; validate: 验证

**[8334.62s] English:** saying like, oh, it seems like it's good.  
**Translation:** 

**[8336.56s] English:** Ship it, right? Well, what happens when I regress something? What happens when I  
**Translation:** Vocabulary: regress: 退化

**[8340.62s] English:** make a classification that's wrong and now I hurt somebody, right?  
**Translation:** 

**[8345.52s] English:** I mean, all these things you have to reason about.  
**Translation:** 

**[8347.18s] English:** Yeah, but at the same time, the bootloader that works for us humans looks awfully a lot like a  
**Translation:** 

**[8354.36s] English:** neural network, right? It's messy and you can cut out different parts of the brain. There's a lot of  
**Translation:** Vocabulary: awfully: 非常; neural: 神经

**[8360.36s] English:** this neuroplasticity work that shows that it's going to adjust. I mean, it's a really interesting  
**Translation:** 

**[8366.30s] English:** question.  
**Translation:** Vocabulary: neuroplasticity: 神经可塑性

**[8366.54s] English:** How much of the world's programming could be replaced by software 2.0?  
**Translation:** 

**[8372.36s] English:** Well, I mean, it's provably true that you could replace all of it.  
**Translation:** 

**[8377.38s] English:** Right. So then it's a question of trade-offs.  
**Translation:** 

**[8379.20s] English:** Anything that's a function, you can. So it's not a question about if. I think it's an economic  
**Translation:** 

**[8384.28s] English:** question. It's a, what kind of talent can you get? What kind of trade-offs in terms of maintenance?  
**Translation:** 

**[8390.16s] English:** Those kinds of questions, I think. What kind of data can you collect? I think one of the reasons  
**Translation:** 

**[8394.16s] English:** that I'm most interested in...  
**Translation:** 

**[8396.54s] English:** Machine learning as a programming paradigm is that one of the things that we.  
**Translation:** Vocabulary: paradigm: 范式

**[8400.00s] English:** you've seen across computing in general is that being laser focused on one paradigm often puts  
**Translation:** 

**[8406.00s] English:** you in a box it's not super great and so you look at object-oriented programming like it was all the  
**Translation:** Vocabulary: computing: 计算机领域

**[8411.04s] English:** rage in the early 80s and like everything has to be objects and people forgot about functional  
**Translation:** 

**[8415.10s] English:** programming even though it came first and and then people rediscovered that hey if you mix  
**Translation:** Vocabulary: rediscovered: 重新发现

**[8420.52s] English:** functional and object-oriented and structure like you mix these things together you can provide  
**Translation:** 

**[8424.78s] English:** very interesting tools that are good at solving different problems and so the question there is  
**Translation:** 

**[8429.34s] English:** how do you get the best way to solve the problems it's not about whose tribe should win right it's  
**Translation:** 

**[8436.14s] English:** not about you know that that shouldn't be the question the question is how do you make it so  
**Translation:** 

**[8440.10s] English:** the people can solve those problems the fastest and they have the right uh tools in their box to  
**Translation:** 

**[8444.38s] English:** build good libraries and they can solve these problems and when you look at that that's like  
**Translation:** 

**[8448.50s] English:** you know you look at reinforcement learning as one really interesting subdomain of this  
**Translation:** 

**[8452.56s] English:** reinforcement learning often you have to have the integration of a of a learned model combined with  
**Translation:** Vocabulary: reinforcement: 强化; subdomain: 子领域

**[8458.36s] English:** your atari  
**Translation:** 

**[8459.18s] English:** or whatever the other scenario it is that you're you're working in you have to combine that that  
**Translation:** 

**[8464.14s] English:** thing with the robot control for the arm right and so now it's not just about that one uh paradigm  
**Translation:** 

**[8471.66s] English:** it's about integrating that with all the other systems that you have including often legacy  
**Translation:** Vocabulary: integrating: 集成

**[8476.50s] English:** systems and things like this right and so to me i think that the interesting the interesting thing  
**Translation:** 

**[8481.12s] English:** to say is like how do you get the best out of this domain and how do you enable people to achieve  
**Translation:** 

**[8485.46s] English:** things that they otherwise couldn't do without excluding all the  
**Translation:** 

**[8489.18s] English:** good things we already know how to do right but okay this is a crazy question but  
**Translation:** Vocabulary: excluding: 不包括

**[8495.54s] English:** we talked a little bit about gpt3 but do you think it's possible that these language models  
**Translation:** 

**[8501.28s] English:** that uh in essence in the language domain software 2.0 could replace some aspect of  
**Translation:** 

**[8511.14s] English:** compilation for example or do program synthesis replace some aspect of programming  
**Translation:** 

**[8516.48s] English:** yeah absolutely so i think that that learned  
**Translation:** Vocabulary: compilation: 编译; synthesis: 合成

**[8519.18s] English:** models in general  
**Translation:** 

**[8520.00s] English:** are extremely powerful, and I think the people underestimate them.  
**Translation:** Vocabulary: underestimate: 低估

**[8524.84s] English:** Maybe you can suggest what I should do.  
**Translation:** 

**[8527.24s] English:** So I have access to the GPT-3 API.  
**Translation:** 

**[8531.26s] English:** Would I be able to generate Swift code, for example?  
**Translation:** 

**[8534.22s] English:** Do you think that could do something interesting and would work?  
**Translation:** 

**[8537.32s] English:** So GPT-3 is probably not trained on the right corpus,  
**Translation:** 

**[8541.10s] English:** so it probably has the ability to generate some Swift.  
**Translation:** 

**[8543.66s] English:** I bet it does.  
**Translation:** 

**[8545.08s] English:** It's probably not going to generate a large enough body of Swift to be useful.  
**Translation:** 

**[8548.20s] English:** But take it a next step further.  
**Translation:** 

**[8550.70s] English:** If you had the goal of training something like GPT-3  
**Translation:** 

**[8553.18s] English:** and you wanted to train it to generate source code,  
**Translation:** 

**[8557.38s] English:** it could definitely do that.  
**Translation:** 

**[8559.72s] English:** Now the question is, how do you express the intent of what you want filled in?  
**Translation:** 

**[8564.08s] English:** You can definitely write scaffolding of code and say fill in the hole  
**Translation:** Vocabulary: scaffolding: 框架代码

**[8567.94s] English:** and sort of put in some for loops or put in some classes or whatever.  
**Translation:** 

**[8571.70s] English:** And the power of these models is impressive,  
**Translation:** 

**[8573.70s] English:** but there's an unsolved question, at least unsolved to me,  
**Translation:** 

**[8576.68s] English:** which is, how do I express the intent?  
**Translation:** Vocabulary: unsolved: 未解决

**[8578.20s] English:** How do I express the intent of what to fill in?  
**Translation:** 

**[8580.80s] English:** And kind of what you'd really want to have,  
**Translation:** 

**[8583.20s] English:** and I don't know that these models are up to the task,  
**Translation:** 

**[8586.32s] English:** is you want to be able to say, here's the scaffolding,  
**Translation:** 

**[8589.52s] English:** and here are the assertions at the end.  
**Translation:** 

**[8592.20s] English:** And the assertions always pass.  
**Translation:** Vocabulary: assertions: 断言

**[8594.06s] English:** And so you want a generative model on the one hand, yes.  
**Translation:** 

**[8596.42s] English:** Oh, that's fascinating, yeah.  
**Translation:** Vocabulary: generative: 生成模型

**[8597.56s] English:** Right?  
**Translation:** 

**[8597.86s] English:** But you also want some loopback,  
**Translation:** Vocabulary: loopback: 环回测试

**[8600.46s] English:** some reinforcement learning system or something  
**Translation:** 

**[8602.54s] English:** where you're actually saying,  
**Translation:** Vocabulary: reinforcement: 强化

**[8604.40s] English:** I need to hill climb towards something that is more correct.  
**Translation:** 

**[8608.20s] English:** And I don't know that we have that.  
**Translation:** 

**[8609.84s] English:** So it would generate not only a bunch of the code,  
**Translation:** 

**[8613.68s] English:** but the checks that do the testing.  
**Translation:** 

**[8615.98s] English:** It would generate the tests.  
**Translation:** 

**[8616.80s] English:** I think the humans would generate the tests, right?  
**Translation:** 

**[8618.84s] English:** Oh, okay.  
**Translation:** 

**[8619.84s] English:** But it would be fascinating if...  
**Translation:** 

**[8621.36s] English:** Well, the tests are the requirements.  
**Translation:** 

**[8623.00s] English:** Yes, but the...  
**Translation:** 

**[8623.76s] English:** Okay, so...  
**Translation:** 

**[8624.22s] English:** Because you have to express to the model what you want to...  
**Translation:** 

**[8627.00s] English:** You don't just want gibberish code.  
**Translation:** 

**[8628.80s] English:** Look at how compelling this code looks.  
**Translation:** Vocabulary: compelling: 引人入胜; gibberish: 乱码

**[8631.28s] English:** You want a story about four-horned unicorns or something.  
**Translation:** 

**[8634.72s] English:** Well, okay, so exactly.  
**Translation:** Vocabulary: unicorns: 独角兽

**[8635.84s] English:** But that's human requirements.  
**Translation:** 

**[8637.80s] English:** But then...  
**Translation:** 

**[8638.20s] English:** I thought it's a compelling idea.  
**Translation:** 

**[8640.00s] English:** that the gpt4 model could generate uh checks like that are more um high fidelity that check for  
**Translation:** Vocabulary: fidelity: 清晰度

**[8651.62s] English:** correctness because uh the code generates like say i ask it to generate a function that um gives me  
**Translation:** 

**[8660.06s] English:** the fibonacci sequence sure i don't like so so decompose the problem right so you have you have  
**Translation:** Vocabulary: correctness: 正确性; decompose: 分解; fibonacci: 斐波那契

**[8666.36s] English:** two things you have you need the ability to generate syntactically correct swift code that  
**Translation:** 

**[8670.92s] English:** that's interesting right i think gpt series of model architectures can do that but then you need  
**Translation:** Vocabulary: syntactically: 语法上

**[8678.12s] English:** the ability to add the requirements so generate fibonacci yeah the human needs to express that  
**Translation:** 

**[8684.96s] English:** goal we don't have that language that i know of no i mean it can generate stuff have you seen  
**Translation:** 

**[8691.28s] English:** with gpt3 can generate you can say i mean there's uh interface stuff like  
**Translation:** 

**[8696.36s] English:** it can generate html it can generate uh basic for loops that give you like right but pick html  
**Translation:** 

**[8702.78s] English:** how do i say i want google.com well no you could say or not not literally google.com how do i say  
**Translation:** 

**[8709.70s] English:** i want a web page that's got a shopping cart into this and that yeah it does that i mean so okay so  
**Translation:** 

**[8714.98s] English:** just uh i don't know if you've seen these demonstrations but you type in i want a red  
**Translation:** 

**[8719.34s] English:** button with the text that says hello and you typed that natural language and it generates the correct  
**Translation:** 

**[8726.36s] English:** language in the demo that's it's kind of compelling so you have to uh prompt it with  
**Translation:** 

**[8731.46s] English:** similar kinds of mappings of course it's probably handpicked i have to experiment that probably  
**Translation:** Vocabulary: handpicked: 人工挑选

**[8737.26s] English:** but the fact that you could do that once even out of like 20 yeah yeah it's uh it's quite  
**Translation:** 

**[8742.66s] English:** impressive again that's very basic uh like the html is kind of messy and and bad for sure but  
**Translation:** 

**[8748.54s] English:** yes the intent is the idea is the intent to specify the natural language okay and so i've  
**Translation:** 

**[8756.36s] English:** yeah but the question is uh the correctness of that like  
**Translation:** 

**[8760.00s] English:** visually you can check oh the button is red but the for more uh for more complicated  
**Translation:** 

**[8767.92s] English:** functions where the intent is harder to check this goes into like mp completeness kind of things like  
**Translation:** Vocabulary: completeness: 完备性

**[8775.60s] English:** i want to know that this code is correct in general it's a giant thing yeah that uh just  
**Translation:** 

**[8782.10s] English:** some kind of calculation it seems to be working it's interesting to think like should the system  
**Translation:** 

**[8789.12s] English:** also try to generate checks for itself for correctness yeah i don't know and this this  
**Translation:** 

**[8793.90s] English:** is way beyond my experience the uh uh the thing that i think about is that there doesn't seem to  
**Translation:** 

**[8799.92s] English:** be a lot of equational reasoning going on right there's a lot of pattern matching and filling in  
**Translation:** 

**[8805.16s] English:** and kind of propagating patterns that have been seen before into the future and into the  
**Translation:** Vocabulary: equational: 等价推理; propagating: 传播

**[8809.84s] English:** generated result and so if you want to get correctness you kind of need through improving  
**Translation:** 

**[8814.32s] English:** kind of things and like a higher level of logic and i don't know that you could talk to  
**Translation:** Vocabulary: correctness: 正确性

**[8819.12s] English:** about that um and see and see what uh the the bright minds are thinking about right now but i  
**Translation:** 

**[8824.98s] English:** don't think the gpt is in that that vein it's still really cool yeah and surprisingly who knows  
**Translation:** 

**[8830.96s] English:** you know maybe reasoning is is uh is overrated yeah right i mean do we reason yeah how do you  
**Translation:** 

**[8837.82s] English:** tell right are we just pattern matching based on what we have and then reverse justifying to  
**Translation:** Vocabulary: justifying: 辩解

**[8842.18s] English:** ourselves exactly the reverse so like i think what the neural networks are missing and i think gpt  
**Translation:** 

**[8849.12s] English:** might have is to be able to uh tell stories to itself about what it did well that's what humans  
**Translation:** Vocabulary: neural: 神经网络

**[8854.40s] English:** do right i mean you talk about uh like network explainability right and we give no that's a hard  
**Translation:** 

**[8859.58s] English:** time about this but humans don't know why we make decisions we have this thing called intuition and  
**Translation:** Vocabulary: explainability: 可解释性; intuition: 直觉

**[8863.88s] English:** then we try to like say this feels like the right thing but why right and you know you wrestle with  
**Translation:** 

**[8868.94s] English:** that when you're making hard decisions and is that science not really let me ask about a few  
**Translation:** Vocabulary: wrestle: 挣扎

**[8875.62s] English:** high level questions i guess is um  
**Translation:** 

**[8879.12s] English:** you  
**Translation:** 

**[8880.00s] English:** done a million things in your life and been very successful a bunch of young folks listen to this  
**Translation:** 

**[8886.88s] English:** ask for advice from successful people like you uh if you were to give advice to uh  
**Translation:** 

**[8894.64s] English:** somebody you know another graduate student or some high school student about uh pursuing a  
**Translation:** 

**[8901.44s] English:** career in computing or just advice about life in general is there sure there's some words of  
**Translation:** Vocabulary: computing: 计算机科学

**[8907.20s] English:** wisdom you can give them so i think you come back to change and you know profound  
**Translation:** 

**[8913.28s] English:** leaps happen because people are willing to believe that change is possible and that  
**Translation:** Vocabulary: profound: 深刻

**[8917.76s] English:** the world does change and are willing to do the hard thing that it takes to make change happen  
**Translation:** 

**[8922.56s] English:** and whether it be implementing a new programming language or employing a new system or  
**Translation:** Vocabulary: employing: 采用; implementing: 实施

**[8927.44s] English:** employing a new research paper designing a new thing moving the world forward in science and  
**Translation:** 

**[8932.08s] English:** philosophy whatever it really comes down to somebody who's willing to put in the work  
**Translation:** 

**[8936.64s] English:** right and  
**Translation:** 

**[8937.20s] English:** you have the the work is hard for a whole bunch of different reasons one of which is um  
**Translation:** 

**[8943.28s] English:** you uh it's work right and so you have to have the space in your life in which you can do that work  
**Translation:** 

**[8949.68s] English:** which is why going to grad school can be a beautiful thing for certain people um but also  
**Translation:** 

**[8955.04s] English:** there's a self-doubt that happens like you're two years into a project is it going anywhere right  
**Translation:** 

**[8960.08s] English:** well what do you do do you just give up because it's hard well no i mean some people like suffering  
**Translation:** 

**[8966.80s] English:** and  
**Translation:** 

**[8967.20s] English:** so you plow through it the the secret to me is that you have to love what you're doing  
**Translation:** 

**[8971.84s] English:** and and follow that passion because if when you get to the hard times that's when  
**Translation:** 

**[8977.84s] English:** you know if you if you love what you're doing you're willing to kind of push through  
**Translation:** 

**[8981.60s] English:** and um this is really uh hard because it's it's hard to know what you  
**Translation:** 

**[8987.76s] English:** will love doing until you start doing a lot of things and so that's why i think that  
**Translation:** 

**[8991.52s] English:** particularly early in your career it's good to experiment do a little bit of everything go go take  
**Translation:** 

**[8996.64s] English:** the the survey class on you know for different the first half of  
**Translation:** 

**[9000.00s] English:** of every class in your upper division you know lessons and um just get exposure to things because  
**Translation:** 

**[9005.82s] English:** certain things will resonate with you and you'll find out wow i'm really good at this i'm really  
**Translation:** 

**[9009.24s] English:** smart at this well it's just because it's it works with the way your brain and when something  
**Translation:** 

**[9013.54s] English:** jumps out i mean that's one of the things that people often ask about is like well i think  
**Translation:** 

**[9019.72s] English:** there's a bunch of cool stuff out there like how do i pick the thing like uh yeah how do you how  
**Translation:** 

**[9025.62s] English:** do you hook in your life how did you just hook yourself in and stuck with it well i got lucky  
**Translation:** 

**[9031.08s] English:** right i mean i think that many people uh forget that a huge amount of it or most of it is luck  
**Translation:** 

**[9037.92s] English:** right so um let's not forget that um so for me i fell in love with computers early on because i'm  
**Translation:** 

**[9045.80s] English:** they spoke to me i guess uh what language did they speak basic basic yeah um but the uh uh  
**Translation:** 

**[9055.44s] English:** basically  
**Translation:** 

**[9055.60s] English:** But then it was just kind of following a set of logical progressions, but also deciding that something that was hard was worth doing and a lot of fun, right?  
**Translation:** 

**[9063.98s] English:** And so I think that that is also something that's true for many other domains, which is if you find something that you love doing that's also hard, if you invest yourself in it and add value to the world, then it will mean something generally, right?  
**Translation:** Vocabulary: progressions: 逻辑推理

**[9077.12s] English:** And again, that can be a research paper, that can be a software system, that can be a new robot, that can be, there's many things that that can be.  
**Translation:** 

**[9084.70s] English:** But a lot of it is like real value comes from doing things that are hard.  
**Translation:** 

**[9089.10s] English:** And that doesn't mean you have to suffer, but it's hard.  
**Translation:** 

**[9094.44s] English:** I mean, you don't often hear that message.  
**Translation:** 

**[9096.28s] English:** We talked about it last time a little bit, but it's one of my, not enough people talk about this.  
**Translation:** 

**[9103.76s] English:** It's beautiful to hear a successful person.  
**Translation:** 

**[9107.08s] English:** Well, and self-doubt and imposter syndrome, and these are all things that successful people suffer with as well.  
**Translation:** 

**[9113.76s] English:** Particularly when they put themselves.  
**Translation:** 

**[9114.70s] English:** In a point of being uncomfortable, which I like to do now and then just because it puts.  
**Translation:** 

**[9120.00s] English:** you in learning mode like if you want to if you want to grow as a person put yourself in a room  
**Translation:** 

**[9126.02s] English:** with a bunch of people that know way more about whatever you're talking about than you do and  
**Translation:** 

**[9130.06s] English:** ask dumb questions and guess what smart people love to teach often not always but often and if  
**Translation:** 

**[9136.98s] English:** you listen if you're prepared to listen if you're prepared to grow if you're prepared to make  
**Translation:** 

**[9139.82s] English:** connections you can do some really interesting things and i think that a lot of progress is made  
**Translation:** 

**[9144.52s] English:** by people who kind of hop between domains now and then because they bring uh they bring a  
**Translation:** 

**[9150.58s] English:** perspective into a field that nobody else has if people have only been working in that field  
**Translation:** 

**[9156.38s] English:** themselves we mentioned that the universe is kind of like a compiler uh you know the entirety of it  
**Translation:** 

**[9163.90s] English:** the whole evolution is kind of a kind of compilation maybe our us human beings are kind  
**Translation:** Vocabulary: compilation: 汇编; entirety: 全部

**[9169.72s] English:** of compilers um let me ask the the old absurd question that i didn't ask you last  
**Translation:** 

**[9174.50s] English:** time which is uh what's the meaning of it all is there a meaning like if you asked a compiler why  
**Translation:** 

**[9180.46s] English:** what would a compiler say what's the meaning of life what's the meaning of life uh you know i'm  
**Translation:** 

**[9186.94s] English:** prepared for it not to mean anything here we are all biological things programmed to survive and  
**Translation:** 

**[9194.60s] English:** and propagate our our dna um and maybe the universe is just a just a computer and you just  
**Translation:** 

**[9202.50s] English:** go until entropy takes over the world and or  
**Translation:** Vocabulary: entropy: 无序; propagate: 传播

**[9204.50s] English:** takes over the universe and then you're done um i don't think that's a very productive way to live  
**Translation:** 

**[9209.98s] English:** your life if so and so i prefer to bias towards the other way which is saying the world has the  
**Translation:** 

**[9216.62s] English:** universe has a lot of value and i take uh i take happiness out of other people and a lot a lot of  
**Translation:** 

**[9222.64s] English:** times part of that's having kids but also the relationships you build with other people and so  
**Translation:** 

**[9227.50s] English:** uh the way i try to live my life is like what what can i do that has value how can i move the world  
**Translation:** 

**[9231.98s] English:** forward how can i take what i'm good at and how can i move the world forward and how can i move the  
**Translation:** 

**[9234.50s] English:** and like bring it bring it into the world and how can i i'm one of these people that likes to work  
**Translation:** 

**[9240.00s] English:** really hard and be very focused on the things that I do. And so if I'm going to do that, how can it  
**Translation:** 

**[9245.50s] English:** be in a domain that actually will matter? Because a lot of things that we do, we find ourselves in  
**Translation:** 

**[9250.76s] English:** the cycle of like, okay, I'm doing a thing. I'm very familiar with it. I've done it for a long  
**Translation:** 

**[9254.32s] English:** time. I've never done anything else, but I'm not really learning. I'm not really, I'm keeping  
**Translation:** 

**[9261.12s] English:** things going, but there's a younger generation that can do the same thing, maybe even better  
**Translation:** 

**[9265.38s] English:** than me, right? And maybe if I actually step out of this and jump into something I'm less  
**Translation:** 

**[9269.86s] English:** comfortable with, it's scary. But on the other hand, it gives somebody else a new opportunity.  
**Translation:** 

**[9274.76s] English:** It also then puts you back in learning mode, and that can be really interesting. And one of the  
**Translation:** 

**[9280.02s] English:** things I've learned is that when you go through that, that first you're deep into imposter syndrome.  
**Translation:** 

**[9285.10s] English:** But when you start working your way out, you start to realize, hey, well, there's actually  
**Translation:** 

**[9288.50s] English:** a method to this. And now I'm able to add new things because I bring different perspective.  
**Translation:** 

**[9294.68s] English:** And this is one of the things that I've learned.  
**Translation:** 

**[9295.38s] English:** the the good things about bringing different kinds of people together diversity of thought  
**Translation:** 

**[9300.72s] English:** is really important and um if you can pull together people that are coming at things from  
**Translation:** 

**[9305.34s] English:** different directions you often get innovation and i i love to see that that aha moment where you're  
**Translation:** 

**[9310.76s] English:** like oh what we've like really cracked this is something never nobody's ever done before  
**Translation:** 

**[9314.62s] English:** and then if you can do it in the context where it adds value other people can build on it it helps  
**Translation:** 

**[9319.26s] English:** move the world then that's what that's what really excites me so the that kind of description of the  
**Translation:** 

**[9324.90s] English:** magic of the human experience do you think we'll ever create that in like an agi system you think  
**Translation:** Vocabulary: excites: 激发兴趣

**[9330.16s] English:** we'll be able to create uh give uh give ai systems the sense of meaning where they operate in this  
**Translation:** 

**[9339.02s] English:** kind of world exactly in the way you've described which is they interact with each other they  
**Translation:** 

**[9343.36s] English:** interact with us humans sure well so i mean i why why are you being so uh speciest right all right  
**Translation:** 

**[9351.08s] English:** so so agis versus bionet  
**Translation:** Vocabulary: speciest: 物种主义者

**[9354.30s] English:** or is that  
**Translation:** 

**[9354.90s] English:** um you know uh what are we but machines  
**Translation:** 

**[9360.00s] English:** right we're just programmed to run our we have our objective function that we're optimized for  
**Translation:** 

**[9364.78s] English:** right and so we're doing our thing we think we have purpose but do we really yeah right i'm not  
**Translation:** 

**[9370.34s] English:** prepared to say that those newfangled agis have no soul just because we don't understand them  
**Translation:** 

**[9376.32s] English:** right and i think that would be um when that when they exist uh that would be very premature to uh  
**Translation:** Vocabulary: newfangled: 新奇; premature: 过早

**[9382.20s] English:** look at a new thing through your own lens without fully understanding it  
**Translation:** 

**[9386.36s] English:** um you might be just saying that because ai systems in the future will be listening to this  
**Translation:** 

**[9392.62s] English:** and then oh yeah exactly you don't want to say please be nice to me you know when skynet skynet  
**Translation:** 

**[9397.48s] English:** kills everybody please spare me so wise wise uh look ahead thinking yeah but i mean i think that  
**Translation:** 

**[9404.10s] English:** people spend a lot of time worrying about this kind of stuff and i think that what we should  
**Translation:** 

**[9407.46s] English:** be worrying about is how do we make the world better and the thing that i'm most scared about  
**Translation:** 

**[9412.08s] English:** with agis is not that um that necessarily  
**Translation:** 

**[9416.36s] English:** the skynet will start shooting everybody with lasers and stuff like that to to use us for  
**Translation:** 

**[9421.16s] English:** our calories the thing that i'm worried about is that um humanity i think needs a challenge  
**Translation:** 

**[9427.50s] English:** and if we get into a mode of not having a personal challenge not having a personal contribution  
**Translation:** 

**[9432.96s] English:** whether that be like you know your kids and seeing what they grow into and helping  
**Translation:** 

**[9437.58s] English:** helping guide them whether it be um your community that you're engaged in you're driving forward  
**Translation:** 

**[9442.70s] English:** whether it be your work and the things that you're doing and the people you're working with  
**Translation:** 

**[9445.92s] English:** and the production  
**Translation:** 

**[9446.36s] English:** building and the contribution there if people don't have a uh objective i'm afraid what that  
**Translation:** 

**[9452.68s] English:** means and um i think that this would lead to a rise of the worst part of people right instead  
**Translation:** 

**[9460.20s] English:** of people striving together and trying to make uh the world better it could degrade into a very  
**Translation:** 

**[9467.84s] English:** unpleasant world but but i don't know i mean we hopefully have a long ways to go before we  
**Translation:** Vocabulary: degrade: 退化; striving: 努力

**[9473.96s] English:** discover that unfortunately we have a long way to go before we discover that  
**Translation:** 

**[9476.36s] English:** we have pretty on the ground problems with the pandemic right now and so i think we should be  
**Translation:** Vocabulary: pandemic: 全球大流行

**[9480.00s] English:** focused on that as well yeah ultimately just as you said you're optimistic i think it helps for  
**Translation:** 

**[9485.54s] English:** us to be optimistic because that's uh take it until you make it yeah well and why not right  
**Translation:** Vocabulary: optimistic: 积极乐观

**[9491.42s] English:** what's what's the other side right so i mean uh uh i'm not personally a very religious person but  
**Translation:** 

**[9497.56s] English:** i've heard people say like oh yeah of course i believe in god of course i go to church because  
**Translation:** 

**[9501.68s] English:** if god's real you know i want to be on the right side of that if it's not real it doesn't matter  
**Translation:** 

**[9506.96s] English:** yeah it doesn't matter and so you know that's that's a fair way to do it um yeah i mean the  
**Translation:** 

**[9512.76s] English:** same thing with uh with the nuclear deterrence all you know global warming all these things  
**Translation:** 

**[9517.94s] English:** all these threats natural engineer pandemics all these threats we face i think it's uh  
**Translation:** Vocabulary: deterrence: 威慑; pandemics: 流行病

**[9524.66s] English:** uh it's paralyzing to be terrified of all the possible ways we could destroy ourselves i think  
**Translation:** 

**[9532.76s] English:** it's much better or least productive to be  
**Translation:** Vocabulary: paralyzing: 使人瘫痪

**[9536.84s] English:** uh  
**Translation:** 

**[9536.96s] English:** hopeful and to engineer defenses against these things to uh engineer a future where like  
**Translation:** 

**[9543.64s] English:** you know see like a positive future and engineer that future yeah well and i think that's other  
**Translation:** 

**[9549.10s] English:** another thing to think about as you know a human particularly if you're young and trying to figure  
**Translation:** 

**[9554.38s] English:** out what it is that you want to be when you grow up like i am um i'm always looking for that uh  
**Translation:** 

**[9559.68s] English:** the the question then is how do you want to spend your time and right now there seems to be a norm  
**Translation:** 

**[9565.86s] English:** of being a  
**Translation:** 

**[9566.96s] English:** consumption culture like i'm going to watch the news and and revel in how horrible everything is  
**Translation:** Vocabulary: revel: 庆祝

**[9572.84s] English:** right now i'm going to go find out about the latest atrocity and find out all the details of  
**Translation:** 

**[9577.70s] English:** like the terrible thing that happened and be outraged by it um you can spend a lot of time  
**Translation:** Vocabulary: atrocity: 暴行; outraged: 愤怒

**[9582.94s] English:** watching tv and watching the news sitcom or whatever people watch these days i don't know  
**Translation:** 

**[9587.74s] English:** um uh but that's a lot of hours right and those are hours that if you're turned into being  
**Translation:** Vocabulary: sitcom: 情景喜剧

**[9594.12s] English:** productive learning growing  
**Translation:** 

**[9596.96s] English:** experiencing uh you know when the pandemic's over going  
**Translation:** 

**[9600.00s] English:** exploring, right? It leads to more growth. And I think it leads to more optimism and happiness  
**Translation:** 

**[9606.28s] English:** because you're building, right? You're building yourself, you're building your capabilities,  
**Translation:** Vocabulary: optimism: 乐观主义

**[9611.02s] English:** you're building your viewpoints, you're building your perspective. And I think that a lot of the  
**Translation:** 

**[9616.00s] English:** consuming of other people's messages leads to kind of a negative viewpoint, which you need to  
**Translation:** Vocabulary: viewpoints: 观点

**[9622.90s] English:** be aware of what's happening because that's also important. But there's a balance that  
**Translation:** 

**[9626.80s] English:** I think focusing on creation is a very valuable thing to do.  
**Translation:** 

**[9632.10s] English:** Yeah. So what you're saying is people should focus on working on the sexiest field of them all,  
**Translation:** 

**[9637.36s] English:** which is compiler design.  
**Translation:** 

**[9638.44s] English:** Exactly. Hey, you could go work on machine learning and be crowded out by the thousands  
**Translation:** 

**[9643.00s] English:** of graduates popping out of school that all want to do the same thing. Or you could work in the  
**Translation:** 

**[9646.54s] English:** place that people overpay you because there's not enough smart people working in it.  
**Translation:** 

**[9651.38s] English:** And here at the end of Moore's law, according to some people, actually the software is the  
**Translation:** 

**[9656.34s] English:** hard part too.  
**Translation:** 

**[9656.80s] English:** Yeah. I mean, optimization is truly, truly beautiful. And also on the YouTube side or  
**Translation:** Vocabulary: optimization: 优化

**[9663.88s] English:** education side, it'd be nice to have some material that shows the beauty of compilers.  
**Translation:** 

**[9672.18s] English:** Yeah, yeah.  
**Translation:** Vocabulary: compilers: 编译器

**[9673.16s] English:** That's something. So that's a call for people to create that kind of content as well.  
**Translation:** 

**[9678.94s] English:** Chris, you're one of my favorite people to talk to. It's such a huge honor that you would waste  
**Translation:** 

**[9684.68s] English:** your time talking to me.  
**Translation:** 

**[9686.16s] English:** I always appreciate it. Thank you so much for talking to me today.  
**Translation:** 

**[9689.24s] English:** The truth of it is you spent a lot of time talking to me just on walks and other things like that.  
**Translation:** 

**[9694.46s] English:** So it's great to catch up with you.  
**Translation:** 

**[9695.66s] English:** Thanks, man.  
**Translation:** 

**[9697.02s] English:** Thanks for listening to this conversation with Chris Lattner. And thank you to our sponsors,  
**Translation:** Vocabulary: sponsors: 赞助商

**[9702.36s] English:** Blinkist, an app that summarizes key ideas from thousands of books.  
**Translation:** 

**[9706.64s] English:** Neuro, which is a maker of functional gum and mints that supercharge my mind.  
**Translation:** Vocabulary: blinkist: 知识萃取; summarizes: 总结; supercharge: 提神

**[9711.70s] English:** Masterclass, which are online courses from world experts.  
**Translation:** 

**[9715.08s] English:** And finally,  
**Translation:** Vocabulary: masterclass: 大师课程

**[9716.16s] English:** Cash App, which is an app for sending money to friends.  
**Translation:** 

**[9720.00s] English:** Please check out these sponsors in the description to get a discount and to support this podcast.  
**Translation:** 

**[9725.72s] English:** If you enjoy this thing, subscribe on YouTube, review it with 5 stars on Apple Podcasts, follow on Spotify, support on Patreon, or connect with me on Twitter at Lex Friedman.  
**Translation:** 

**[9735.92s] English:** And now, let me leave you with some words from Chris Lattner.  
**Translation:** 

**[9739.10s] English:** So much of language design is about trade-offs, and you can't see those trade-offs unless you have a community of people that really represent those different points.  
**Translation:** 

**[9747.60s] English:** Thank you for listening, and hope to see you next time.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
