# Podcast vocabulary notes
Source file: Lex Fridman - Cursor Team： Future of Programming with AI ｜ Lex Fridman Podcast #447.opus

**[0.00s] English:** The following is a conversation with the founding members of the Cursor team,  
**Translation:** 

**[4.58s] English:** Michael Truel, Swali Asif, Arvid Lundmark, and Aman Sanger.  
**Translation:** Vocabulary: arvid: 阿维德; founding: 创始; lundmark: 伦德马克

**[10.42s] English:** Cursor is a code editor based on VS Code that adds a lot of powerful features for AI-assisted coding.  
**Translation:** 

**[17.74s] English:** It has captivated the attention and excitement of the programming and AI communities.  
**Translation:** Vocabulary: captivated: 吸引注意

**[23.40s] English:** So I thought this is an excellent opportunity to dive deep into the role of AI in programming.  
**Translation:** 

**[30.00s] English:** This is a super technical conversation that is bigger than just about one code editor.  
**Translation:** 

**[36.68s] English:** It's about the future of programming, and in general, the future of human-AI collaboration  
**Translation:** 

**[41.56s] English:** in designing and engineering complicated and powerful systems.  
**Translation:** 

**[46.68s] English:** This is the Lex Friedman Podcast. To support it, please check out our sponsors in the description.  
**Translation:** 

**[51.78s] English:** And now, dear friends, here's Michael, Swali, Arvid, and Aman.  
**Translation:** Vocabulary: friedman: 弗里德曼; sponsors: 赞助商

**[58.70s] English:** All right, this is awesome.  
**Translation:** 

**[60.00s] English:** We have Michael, Aman, Swali, Arvid here from the Cursor team.  
**Translation:** 

**[64.94s] English:** First up, big ridiculous question.  
**Translation:** 

**[67.38s] English:** What's the point of a code editor?  
**Translation:** 

**[70.22s] English:** So the code editor is largely the place where you build software.  
**Translation:** 

**[74.38s] English:** And today, or for a long time, that's meant the place where you text edit a formal programming language.  
**Translation:** 

**[80.88s] English:** And for people who aren't programmers, the way to think of a code editor is like a really souped-up word processor for programmers.  
**Translation:** 

**[87.20s] English:** Where the reason it's souped up is code has...  
**Translation:** Vocabulary: processor: 处理器; programmers: 程序员

**[90.00s] English:** a lot of structure.  
**Translation:** 

**[91.42s] English:** And so the quote-unquote word processor, the code editor, can actually do a lot for you that word processors, you know, sort of in the writing space, haven't been able to do for people editing text there.  
**Translation:** Vocabulary: processors: 处理器

**[102.22s] English:** And so, you know, that's everything from giving you visual differentiation of like the actual tokens in the code so you can scan it quickly, to letting you navigate around the code base, sort of like you're navigating around the Internet with like hyperlinks.  
**Translation:** 

**[113.14s] English:** You're going to sort of definitions of things you're using, to error checking, you know, to catch rudimentary bugs.  
**Translation:** Vocabulary: differentiation: 区分; hyperlinks: 超链接; navigate: 导航; navigating: 导航; rudimentary: 初级

**[120.00s] English:** um and so traditionally that's what a code editor has meant and i think that what a code editor is  
**Translation:** 

**[129.98s] English:** is going to change a lot over the next 10 years um as what it means to build software maybe starts  
**Translation:** 

**[134.72s] English:** to look a bit different i think also a code editor should just be fun yes that is very important that  
**Translation:** 

**[141.50s] English:** is very important and it's actually sort of an underrated aspect of how we decide what to build  
**Translation:** 

**[147.10s] English:** like a lot of the things that we build and then we we try them out we do an experiment and then we  
**Translation:** 

**[153.38s] English:** actually throw them out because they're not fun and and so a big part of being fun is like  
**Translation:** 

**[158.86s] English:** being fast a lot of the time fast is funny yeah fast yeah uh yeah that should be a t-shirt  
**Translation:** 

**[166.80s] English:** like fundamentally i think one of the things that draws a lot of people to building stuff  
**Translation:** Vocabulary: fundamentally: 从根本上

**[172.64s] English:** on computers is this like insane iteration speed where you know in other disciplines  
**Translation:** 

**[177.10s] English:** you might be sort of gatecapped by resources or the ability even the ability you know to get a  
**Translation:** Vocabulary: disciplines: 学科领域; iteration: 迭代

**[182.22s] English:** large group together and coding is this like amazing thing where it's you and the computer and  
**Translation:** 

**[185.64s] English:** uh that alone you can you can build really cool stuff really quickly so for people to know cursor  
**Translation:** 

**[191.26s] English:** is this super cool new editor that's a fork of vs code it would be interesting to get your kind of  
**Translation:** 

**[199.50s] English:** explanation of your own journey of editors how did you i think all of you are were big fans of  
**Translation:** 

**[206.14s] English:** vs code with code pod  
**Translation:** 

**[207.10s] English:** pilot how did you arrive to vs code and how did that lead to your journey with cursor yeah um so  
**Translation:** 

**[214.82s] English:** i think a lot of us well all of us were originally fam users pure pure pure vim yeah no neo vim just  
**Translation:** 

**[222.32s] English:** pure vim in a terminal and at least at least for myself it was around the time that copilot came  
**Translation:** Vocabulary: copilot: 代码助手

**[229.74s] English:** out so 2021 that i really wanted to try it so i went into vs code the only place where i could  
**Translation:** 

**[237.10s] English:** form the only code editor in which it was available  
**Translation:** 

**[240.00s] English:** And even though I really enjoyed using Vim, just the experience of Copilot with VS Code was more than good enough to convince me to switch.  
**Translation:** 

**[250.86s] English:** And so that kind of was the default until we started working on Cursor.  
**Translation:** 

**[254.46s] English:** And maybe we should explain what Copilot does.  
**Translation:** 

**[257.34s] English:** It's like a really nice autocomplete.  
**Translation:** Vocabulary: autocomplete: 自动完成

**[259.70s] English:** It suggests, as you start writing a thing, it suggests one or two or three lines how to complete the thing.  
**Translation:** 

**[265.14s] English:** And there's a fun experience in that, you know, like when you have a close friendship and your friend completes your sentences, like when it's done well, there's an intimate feeling.  
**Translation:** Vocabulary: intimate: 亲密的

**[276.96s] English:** There's probably a better word than intimate, but there's a there's a cool feeling of like, holy shit, it gets me now.  
**Translation:** 

**[284.38s] English:** And then there's an unpleasant feeling when it doesn't get you.  
**Translation:** 

**[287.92s] English:** And so there's that kind of friction.  
**Translation:** 

**[290.42s] English:** But I would say for a lot of people, the feeling that it gets me overpowers that it doesn't.  
**Translation:** Vocabulary: friction: 摩擦; overpowers: 压倒

**[295.14s] English:** And I think actually one of the underrated aspects of GitHub Copilot is that even when it's wrong, it's like a little bit annoying, but it's not that bad because you just type another character and then maybe then it gets you or you type another character and then it gets you.  
**Translation:** 

**[308.12s] English:** So even when it's wrong, it's not that bad.  
**Translation:** 

**[309.48s] English:** Yeah, you can sort of iterate and fix it.  
**Translation:** 

**[311.56s] English:** I mean, the other underrated part of Copilot for me sort of was just the first real real AI product.  
**Translation:** 

**[317.82s] English:** So the first language model consumer product.  
**Translation:** 

**[321.60s] English:** So Copilot was kind of like the first killer app.  
**Translation:** 

**[325.14s] English:** For LLMs.  
**Translation:** 

**[326.96s] English:** Yeah.  
**Translation:** 

**[327.20s] English:** And like the beta was out in 2021.  
**Translation:** 

**[329.06s] English:** Right.  
**Translation:** 

**[329.68s] English:** Okay.  
**Translation:** 

**[331.02s] English:** So what's the the origin story of Cursor?  
**Translation:** 

**[334.10s] English:** So around 2020, the scaling loss papers came out from from OpenAI.  
**Translation:** 

**[338.70s] English:** And that was a moment where this looked like clear, predictable progress for the field, where even if we didn't have any more ideas, it looks like you can make these models a lot better if you had more compute and more data.  
**Translation:** Vocabulary: predictable: 可预测的

**[349.38s] English:** By the way, we'll probably talk for three to four hours on the topic of scaling loss.  
**Translation:** 

**[355.14s] English:** Just to summarize, it's a paper and a set of papers and a set of ideas.  
**Translation:** Vocabulary: summarize: 概括

**[360.00s] English:** ideas that say bigger might be better for model size and data size in the in the realm of machine  
**Translation:** 

**[365.22s] English:** learning it's bigger and better but predictably better okay that's another topic of conversation  
**Translation:** 

**[370.32s] English:** yeah so around that time for some of us there were like a lot of conceptual conversations about  
**Translation:** 

**[374.84s] English:** what's this going to look like what's the the story going to be for all these different  
**Translation:** Vocabulary: conceptual: 概念性的

**[379.34s] English:** knowledge worker fields about how they're going to be um made better by this technology getting  
**Translation:** 

**[383.94s] English:** better and then um i think there were a couple of moments where like the theoretical gains  
**Translation:** 

**[389.08s] English:** predicted in that paper uh started to feel really concrete and it started to feel like a moment  
**Translation:** 

**[393.64s] English:** where you could actually go and not you know do a phd if you wanted to work on uh do useful work  
**Translation:** 

**[399.68s] English:** in ai actually felt like now there was this this whole set of systems one could build that were  
**Translation:** 

**[403.70s] English:** really useful and i think that the first moment we already talked about a little bit which was  
**Translation:** 

**[407.50s] English:** playing with the early bit of copilot like that was awesome and magical um i think that the next  
**Translation:** 

**[412.64s] English:** big moment where everything kind of clicked together was actually getting early access to  
**Translation:** Vocabulary: copilot: 飞行助手

**[416.54s] English:** gpd4 so it was sort of end of 2022  
**Translation:** 

**[419.08s] English:** was when we were um tinkering with that model and the step of incapabilities felt  
**Translation:** Vocabulary: incapabilities: 能力不足; tinkering: 摸索

**[424.10s] English:** enormous and previous to that we had been working on a couple of different projects we had been  
**Translation:** 

**[429.18s] English:** because of copilot because of scaling oz because of our prior interest in the technology we had  
**Translation:** 

**[435.38s] English:** been uh tinkering around with tools for programmers but things that are like very  
**Translation:** 

**[439.88s] English:** specific so you know we were building tools for uh financial professionals who have to work within  
**Translation:** 

**[445.04s] English:** a jupiter notebook or like you know playing around with can you do static analysis with  
**Translation:** 

**[448.20s] English:** these models  
**Translation:** 

**[449.08s] English:** and then the step up in gpd4 felt like look that really made concrete the theoretical gains that  
**Translation:** 

**[455.72s] English:** we had predicted before felt like you could build a lot more just immediately at that point in time  
**Translation:** 

**[460.84s] English:** and also if we were being consistent it really felt like this wasn't just gonna be a point  
**Translation:** 

**[467.24s] English:** solution thing this was gonna be all of programming was gonna flow through these models it felt like  
**Translation:** 

**[471.24s] English:** that demanded a different type of programming environment a different type of programming  
**Translation:** 

**[475.48s] English:** and so we set off to build that that sort of larger vision  
**Translation:** 

**[479.08s] English:** around that  
**Translation:** 

**[480.04s] English:** there's  
**Translation:** 

**[481.08s] English:** a lot of  
**Translation:** 

**[482.08s] English:** stuff  
**Translation:** 

**[483.08s] English:** that's  
**Translation:** 

**[484.08s] English:** going  
**Translation:** 

**[485.08s] English:** on  
**Translation:** 

**[486.08s] English:** in  
**Translation:** 

**[487.08s] English:** the  
**Translation:** 

**[488.08s] English:** world  
**Translation:** 

**[489.08s] English:** and  
**Translation:** 

**[490.08s] English:** i  
**Translation:** 

**[491.08s] English:** don't  
**Translation:** 

**[492.08s] English:** know  
**Translation:** 

**[493.08s] English:** what  
**Translation:** 

**[494.08s] English:** to  
**Translation:** 

**[495.08s] English:** do  
**Translation:** 

**[496.08s] English:** and  
**Translation:** 

**[497.08s] English:** i  
**Translation:** 

**[498.08s] English:** don't  
**Translation:** 

**[499.08s] English:** know  
**Translation:** 

**[500.08s] English:** what  
**Translation:** 

**[501.08s] English:** to  
**Translation:** 

**[502.08s] English:** do  
**Translation:** 

**[503.08s] English:** and  
**Translation:** 

**[504.08s] English:** i  
**Translation:** 

**[505.08s] English:** don't  
**Translation:** 

**[506.08s] English:** know  
**Translation:** 

**[507.08s] English:** what  
**Translation:** 

**[508.08s] English:** to  
**Translation:** 

**[480.00s] English:** There's one that I distinctly remember. So my roommate is an IMO gold winner. And there's a  
**Translation:** 

**[486.24s] English:** competition in the US called the Putnam, which is sort of the IMO for college people. And it's this  
**Translation:** Vocabulary: putnam: 普特南数学竞赛; roommate: 室友

**[491.04s] English:** math competition. It's exceptionally good. So Sheng Tong and Amon, I remember it sort of  
**Translation:** 

**[497.64s] English:** June of 2022, had this bet on whether 2024, June or July, you were going to win a gold medal in  
**Translation:** Vocabulary: exceptionally: 非常; sheng: 盛

**[508.94s] English:** the IMO with models. IMO is International Math Olympiad.  
**Translation:** 

**[513.32s] English:** Yeah. IMO is International Math Olympiad. And so Arvid and I are both, also competed in it. So  
**Translation:** Vocabulary: arvid: 阿维德; olympiad: 奥林匹克数学竞赛

**[519.02s] English:** it was sort of personal. And I remember thinking, Matt, this is not going to happen.  
**Translation:** 

**[527.30s] English:** This was like, even though I sort of believed in progress, I thought, IMO gold, Amon is just  
**Translation:** 

**[535.04s] English:** delusional. And to be honest, I mean, I don't know. I don't know. I don't know. I don't know.  
**Translation:** 

**[538.92s] English:** I was, to be clear, very wrong, but that was maybe the most prescient bet in the group.  
**Translation:** Vocabulary: delusional: 妄想; prescient: 先知的

**[545.48s] English:** So the new results from DeepMind, it turned out that you were correct.  
**Translation:** 

**[550.58s] English:** Well, it was technically not.  
**Translation:** 

**[552.54s] English:** Technically incorrect, but one point away.  
**Translation:** 

**[555.08s] English:** Amon was very enthusiastic about this stuff.  
**Translation:** 

**[556.80s] English:** And before, Amon had this scaling loss t-shirt that he would walk around with, where it had the charts and the formulas on it.  
**Translation:** 

**[565.24s] English:** So you felt the AGI, or you felt the scaling loss?  
**Translation:** 

**[568.62s] English:** Yeah, I distinctly remember there was this one conversation I had with Michael, where before I hadn't thought super deeply and critically about scaling laws.  
**Translation:** 

**[578.32s] English:** And he kind of posed the question, why isn't scaling all you need?  
**Translation:** Vocabulary: critically: 深入地

**[582.64s] English:** Or why isn't scaling going to result in massive gains in progress?  
**Translation:** 

**[586.02s] English:** And I think I went through the stages of grief.  
**Translation:** 

**[589.54s] English:** There is anger, denial, and then finally at the end, just thinking about it, acceptance.  
**Translation:** 

**[595.54s] English:** And I think I've been quite...  
**Translation:** 

**[598.62s] English:** Hopeful.  
**Translation:** 

**[600.00s] English:** and optimistic about progress since i think one thing i'll caveat is i think it also depends on  
**Translation:** Vocabulary: caveat: 保留意见; optimistic: 乐观

**[606.52s] English:** like which domains you're going to see progress like math is a great domain because especially  
**Translation:** 

**[610.90s] English:** like formal theorem proving because you get this fantastic signal of actually verifying if the  
**Translation:** Vocabulary: theorem: 定理; verifying: 验证

**[617.08s] English:** thing was correct and so this means something like rl can work really really well and i think like  
**Translation:** 

**[621.80s] English:** you could have systems that are perhaps very superhuman to math and still not technically  
**Translation:** 

**[626.40s] English:** have agi okay so can we take it all the way to cursor and what is cursor it's a fork of vs code  
**Translation:** 

**[634.28s] English:** and vs code is one of the most popular editors for a long time like everybody fell in love with it  
**Translation:** 

**[639.42s] English:** everybody left vim i left emax for it sorry uh so unified in some fundamental way the uh the  
**Translation:** 

**[651.18s] English:** developer community and then that you look at the space of things you look at the scaling laws ai  
**Translation:** 

**[656.14s] English:** is  
**Translation:** 

**[656.38s] English:** and you decided okay it's not enough to just write an extension for vs code  
**Translation:** 

**[662.50s] English:** because there's a lot of limitations to that we need if ai is going to keep getting better better  
**Translation:** 

**[668.78s] English:** better we need to really like rethink how the the ai is going to be part of the editing process  
**Translation:** 

**[673.78s] English:** and so you decided to fork vs code and start to build a lot of the amazing features we'll be able  
**Translation:** 

**[679.84s] English:** to to talk about but what was that decision like because there's a lot of extensions including  
**Translation:** Vocabulary: extensions: 插件

**[686.38s] English:** co-pilot of vs code that are doing sort of ai type stuff what was the decision like to just  
**Translation:** 

**[691.76s] English:** fork vs code so the decision to do an editor seemed kind of self-evident to us for at least  
**Translation:** 

**[698.42s] English:** what we wanted to do and achieve because when we started working on the editor the idea was  
**Translation:** 

**[703.06s] English:** these models are going to get much better their capabilities are going to improve and it's going  
**Translation:** 

**[705.82s] English:** to entirely change how you build software both in a you will have big productivity gains but also  
**Translation:** 

**[710.28s] English:** radical and not like the act of building software is going to change a lot and so you're very limited  
**Translation:** 

**[716.38s] English:** control you have over a code editor if you're a plug-in to an existing coding environment  
**Translation:** 

**[720.00s] English:** and we didn't want to get locked in by those limitations.  
**Translation:** 

**[724.70s] English:** We wanted to be able to just build the most useful stuff.  
**Translation:** 

**[728.18s] English:** Okay, well, then the natural question is,  
**Translation:** 

**[731.36s] English:** you know, VS Code is kind of with Copilot a competitor.  
**Translation:** 

**[735.20s] English:** So how do you win?  
**Translation:** Vocabulary: copilot: 代码伙伴

**[737.24s] English:** Is it basically just the speed and the quality of the features?  
**Translation:** 

**[740.24s] English:** Yeah, I mean, I think this is a space  
**Translation:** 

**[741.96s] English:** that is quite interesting, perhaps quite unique,  
**Translation:** 

**[746.22s] English:** where if you look at previous tech waves,  
**Translation:** 

**[749.20s] English:** maybe there's kind of one major thing that happened  
**Translation:** 

**[751.72s] English:** and it unlocked a new wave of companies.  
**Translation:** Vocabulary: unlocked: 解锁

**[754.12s] English:** But every single year, every single model capability  
**Translation:** 

**[756.86s] English:** or jump you get in model capabilities,  
**Translation:** Vocabulary: capability: 能力

**[759.72s] English:** you now unlock this new wave of features,  
**Translation:** 

**[763.58s] English:** things that are possible, especially in programming.  
**Translation:** 

**[766.92s] English:** And so I think in AI programming,  
**Translation:** 

**[769.74s] English:** being even just a few months ahead,  
**Translation:** 

**[771.66s] English:** let alone a year ahead,  
**Translation:** 

**[773.10s] English:** makes your product much, much, much more useful.  
**Translation:** 

**[775.76s] English:** I think the cursor a year from now  
**Translation:** 

**[777.64s] English:** will need to make the cursor  
**Translation:** 

**[778.80s] English:** of the future of the AI.  
**Translation:** 

**[779.18s] English:** And I think, you know, Microsoft  
**Translation:** 

**[783.18s] English:** has done a number of like fantastic things,  
**Translation:** 

**[786.22s] English:** but I don't think they're in a great place  
**Translation:** 

**[788.28s] English:** to really keep innovating and pushing on this  
**Translation:** 

**[790.94s] English:** in the way that a startup can.  
**Translation:** Vocabulary: innovating: 不断创新

**[793.26s] English:** Just rapidly implementing features.  
**Translation:** 

**[795.88s] English:** And push, yeah, like, and kind of doing  
**Translation:** Vocabulary: implementing: 执行

**[798.00s] English:** the research experimentation necessary  
**Translation:** 

**[800.98s] English:** to really push the ceiling.  
**Translation:** Vocabulary: experimentation: 实验

**[804.08s] English:** I don't know if I think of it in terms of features  
**Translation:** 

**[805.94s] English:** as I think of it in terms of like capabilities  
**Translation:** 

**[808.08s] English:** for programming.  
**Translation:** 

**[809.18s] English:** It's that like, you know, as, you know,  
**Translation:** 

**[813.02s] English:** the new one model came out,  
**Translation:** 

**[814.96s] English:** and I'm sure there are going to be more models  
**Translation:** 

**[817.16s] English:** of different types, like longer context  
**Translation:** 

**[818.92s] English:** and maybe faster.  
**Translation:** 

**[820.58s] English:** Like there's all these crazy ideas that you can try  
**Translation:** 

**[824.32s] English:** and hopefully 10% of the crazy ideas  
**Translation:** 

**[827.26s] English:** will make it into something kind of cool and useful.  
**Translation:** 

**[830.76s] English:** And we want people to have that sooner.  
**Translation:** 

**[835.74s] English:** To rephrase, it's like an underrated fact  
**Translation:** 

**[837.54s] English:** is we're making it for ourself.  
**Translation:** Vocabulary: ourself: 我们自己; rephrase: 重新表述

**[839.18s] English:** When we started,  
**Translation:** 

**[840.00s] English:** cursor you really felt this frustration that you know models you could see models getting better  
**Translation:** 

**[845.54s] English:** but the cobalt experience had not changed it was it's like man these guys like the ceiling is  
**Translation:** 

**[852.38s] English:** getting higher like why are they not making new things like they should be making new things they  
**Translation:** Vocabulary: cobalt: 钴

**[856.20s] English:** should be like he like like where's where's all the alpha features there were no alpha features  
**Translation:** 

**[860.58s] English:** it was like uh i i'm sure it was selling well i'm sure it was a great business but  
**Translation:** Vocabulary: alpha: 测试特性

**[866.30s] English:** it didn't feel i i'm one of these people that really want to try and use new things and was  
**Translation:** 

**[872.28s] English:** just there's no new thing for like a very long while yeah it's interesting uh i don't know how  
**Translation:** 

**[877.70s] English:** you put that into words but when you compare cursor with copilot copilot pretty quickly became  
**Translation:** 

**[883.32s] English:** started to feel stale for some reason yeah i think one thing that i think uh helps us is that  
**Translation:** Vocabulary: copilot: 副驾; stale: 陈旧

**[890.06s] English:** we're sort of doing it all in one where we're developing the the ux and the way you interact  
**Translation:** 

**[896.14s] English:** with it and the way you interact with it and the way you interact with it and the way you  
**Translation:** 

**[896.30s] English:** model and at the same time as we're developing like how we actually make the model give better  
**Translation:** 

**[901.98s] English:** answers so like how you build up the the prompt or or like how do you find the context and for  
**Translation:** 

**[907.64s] English:** a cursor tab like how do you train the model um so i think that helps us to have all of it like  
**Translation:** 

**[912.74s] English:** sort of like the same people working on the entire experience end-to-end yeah it's like the person  
**Translation:** 

**[918.50s] English:** making the ui and the person training the model like sit to like 18 feet away so often the same  
**Translation:** 

**[924.86s] English:** person even yeah often often even the same person so you you can you can create things that are sort  
**Translation:** 

**[930.24s] English:** of not possible if you're not you're not talking you're not experimenting and you're using like  
**Translation:** 

**[935.30s] English:** you said cursor to write cursor of course oh yeah yeah well let's talk about some of these features  
**Translation:** Vocabulary: experimenting: 实验

**[940.52s] English:** let's talk about the all-knowing the all-powerful praise b to the tab you know autocomplete on  
**Translation:** 

**[948.32s] English:** steroids basically so what how does tab work what is tab to highlight and summarize at a high level  
**Translation:** Vocabulary: autocomplete: 自动完成; steroids: 增强; summarize: 总结

**[954.40s] English:** you  
**Translation:** 

**[954.86s] English:** i'd say that there are two things that cursor is pretty good at right now there are other things  
**Translation:** 

**[959.70s] English:** that it does  
**Translation:** 

**[960.00s] English:** does. But two things it helps programmers with. One is this idea of looking over your shoulder  
**Translation:** Vocabulary: programmers: 程序员

**[967.70s] English:** and being like a really fast colleague who can kind of jump ahead of you and type and figure  
**Translation:** 

**[972.98s] English:** out what you're going to do next. And that was the original idea behind, that was kind of the  
**Translation:** 

**[979.40s] English:** kernel of the idea behind good autocomplete was predicting what you're going to do next.  
**Translation:** 

**[983.16s] English:** But you can make that concept even more ambitious by not just predicting the characters after your  
**Translation:** Vocabulary: kernel: 核心

**[989.00s] English:** cursor, but actually predicting the next entire change you're going to make, the next diff,  
**Translation:** 

**[992.08s] English:** next place you're going to jump to. And the second thing cursor is pretty good at right now too,  
**Translation:** 

**[999.88s] English:** is helping you sometimes jump ahead of the AI and tell it what to do and go from instructions to  
**Translation:** 

**[1006.06s] English:** code. And on both of those, we've done a lot of work on making the editing experience for those  
**Translation:** 

**[1010.14s] English:** things ergonomic and also making those things smart and fast.  
**Translation:** 

**[1014.62s] English:** One of the things we really wanted was we wanted the model to be able to edit code for us.  
**Translation:** Vocabulary: ergonomic: 人体工学的

**[1019.00s] English:** That was kind of a wish. And we had multiple attempts at it before we had a sort of a good  
**Translation:** 

**[1024.42s] English:** model that could edit code for you. Then after we had a good model, I think there've been a lot of  
**Translation:** 

**[1030.94s] English:** effort to make the inference fast for having a good experience. And we've been starting to  
**Translation:** 

**[1041.78s] English:** incorporate, I mean, Michael sort of mentioned this ability to jump to different places. And  
**Translation:** Vocabulary: incorporate: 吸收; inference: 推断

**[1046.40s] English:** that jump to different places, I think, came from a feeling of like, oh, I'm going to do this. I'm  
**Translation:** 

**[1049.00s] English:** feeling off. Once you accept an edit, it's like, man, it should be just really obvious where to go  
**Translation:** 

**[1057.08s] English:** next. It's like I'd made this change. The model should just know that the next place to go to is  
**Translation:** 

**[1062.72s] English:** like 18 lines down. If you're a WIM user, you could press 1, 8, JJ or whatever. But why am I  
**Translation:** 

**[1071.60s] English:** doing this? The model should just know it. And then so the idea was, oh, you just press tab,  
**Translation:** 

**[1076.76s] English:** it would go 18 lines down and then make...  
**Translation:** 

**[1079.00s] English:** It showed you the...  
**Translation:** 

**[1080.00s] English:** next edit and you would press tab so it's just you as long as you could keep pressing tab and  
**Translation:** 

**[1084.78s] English:** so the internal competition was how many tabs can we make someone press it once you have like the  
**Translation:** 

**[1089.32s] English:** idea uh more more uh sort of abstractly the the thing to think about is sort of like once how  
**Translation:** Vocabulary: abstractly: 抽象地

**[1096.08s] English:** how are the edits sort of zero zero entropy so once you've sort of expressed your intent and  
**Translation:** 

**[1101.08s] English:** the edit is there's no like new bits of information to finish your thought but you still have to type  
**Translation:** Vocabulary: entropy: 信息熵

**[1108.38s] English:** some characters to like make the computer understand what you're actually thinking  
**Translation:** 

**[1112.30s] English:** then maybe the model should just sort of read your mind and and all the zero entropy bits should just  
**Translation:** 

**[1118.10s] English:** be like tabbed away yeah that was that was sort of the abstract there's this interesting thing  
**Translation:** 

**[1123.52s] English:** where if you look at language model loss on on different domains um i believe the bits per byte  
**Translation:** 

**[1129.18s] English:** which is a kind of character normalized loss for code is lower than language which means in general  
**Translation:** 

**[1135.90s] English:** there are a lot of tokens in code that are super predictable  
**Translation:** Vocabulary: predictable: 可预测的

**[1138.26s] English:** a lot of characters that are super predictable um and this is i think even magnified when you're  
**Translation:** 

**[1143.22s] English:** not just trying to auto-complete code but predicting what the user is going to do next  
**Translation:** Vocabulary: magnified: 放大

**[1148.32s] English:** in their editing of existing code and so you know the goal of cursor tabs let's eliminate  
**Translation:** 

**[1153.28s] English:** all the low entropy actions you take inside of the editor when the intent is effectively  
**Translation:** 

**[1158.60s] English:** determined let's just jump you forward in time skip you forward well well what's the intuition  
**Translation:** 

**[1163.84s] English:** and what's the technical details of how to do next cursor prediction how the that  
**Translation:** Vocabulary: intuition: 直觉

**[1168.14s] English:** just  
**Translation:** 

**[1168.26s] English:** don't that's not that's not so intuitive i think to people yeah i think i can speak to a few of the  
**Translation:** Vocabulary: intuitive: 直观的

**[1174.52s] English:** details on how how to make these things work they're incredibly low latency so you need to  
**Translation:** 

**[1179.06s] English:** train small models on this on this task um in particular they're incredibly pre-filled token  
**Translation:** Vocabulary: latency: 低延迟; token: 标记

**[1188.00s] English:** hungry what that means is they have these really really long prompts where they see a lot of your  
**Translation:** 

**[1191.72s] English:** code and they're not actually generating that many tokens and so the perfect fit for that is using a  
**Translation:** 

**[1198.04s] English:** sparse model meaning an moe model  
**Translation:** 

**[1200.00s] English:** So that was kind of one breakthrough we made that substantially improved its performance at longer context.  
**Translation:** Vocabulary: sparse: 稀疏

**[1206.22s] English:** The other being a variant of speculative decoding that we kind of built out called speculative edits.  
**Translation:** 

**[1213.02s] English:** These are two, I think, important pieces of what make it quite high quality and very fast.  
**Translation:** Vocabulary: speculative: 推测性

**[1220.38s] English:** Okay, so MOE, mixture of experts, the input is huge, the output is small.  
**Translation:** 

**[1224.94s] English:** Yeah.  
**Translation:** 

**[1225.18s] English:** Okay, so what else can you say about how to make these caching play a role?  
**Translation:** 

**[1230.60s] English:** Oh, caching plays a huge role.  
**Translation:** Vocabulary: caching: 缓存

**[1233.70s] English:** Because you're dealing with this many input tokens, if every single keystroke that you're typing in a given line,  
**Translation:** 

**[1239.80s] English:** you had to rerun the model on all of those tokens passed in, you're just going to, one, significantly degrade latency,  
**Translation:** Vocabulary: degrade: 降低性能; keystroke: 按键

**[1247.52s] English:** two, you're going to kill your GPUs with load.  
**Translation:** 

**[1249.60s] English:** So you need to design the actual prompts used for the model such that they're,  
**Translation:** 

**[1255.32s] English:** cache, caching aware.  
**Translation:** 

**[1257.24s] English:** And then, yeah, you need to reuse the KV cache across requests just so that you're spending less work, less compute.  
**Translation:** Vocabulary: cache: 缓存; reuse: 重用

**[1264.36s] English:** Again, what are the things that tab is supposed to be able to do kind of in the near term?  
**Translation:** 

**[1270.72s] English:** Just to like sort of linger on that.  
**Translation:** 

**[1273.52s] English:** Generate code, like fill empty space, also edit code across multiple lines.  
**Translation:** 

**[1280.96s] English:** Yeah.  
**Translation:** 

**[1281.50s] English:** And then jump to different locations inside the same file.  
**Translation:** 

**[1284.24s] English:** Yeah.  
**Translation:** 

**[1284.50s] English:** And then like,  
**Translation:** 

**[1285.18s] English:** Hopefully jump to different files also.  
**Translation:** 

**[1286.94s] English:** So if you make an edit in one file and maybe you have to go to another file to finish your thought,  
**Translation:** 

**[1293.46s] English:** it should go to the second file also.  
**Translation:** 

**[1296.02s] English:** And then the full generalization is like next action prediction.  
**Translation:** 

**[1300.76s] English:** Like sometimes you need to run a command in the terminal and it should be able to suggest the command based on the code that you wrote to.  
**Translation:** Vocabulary: generalization: 泛化

**[1309.36s] English:** Or sometimes you actually need to, like it suggests something,  
**Translation:** 

**[1314.22s] English:** but you,  
**Translation:** 

**[1314.62s] English:** you,  
**Translation:** 

**[1315.18s] English:** it's hard for you to know if it's correct because you actually need some more information to learn.  
**Translation:** 

**[1319.70s] English:** Like,  
**Translation:** 

**[1319.92s] English:** you know,  
**Translation:** 

**[1320.00s] English:** need to know the type to be able to verify that it's correct and so maybe it should actually take  
**Translation:** 

**[1324.50s] English:** you to a place that's like the definition of something and then take you back so that you  
**Translation:** Vocabulary: verify: 核实

**[1329.54s] English:** have all the requisite knowledge to be able to accept the next completion so providing the human  
**Translation:** 

**[1334.42s] English:** the knowledge yes right yeah can you integrate like i just uh gotten to know a guy named prime  
**Translation:** Vocabulary: integrate: 整合; requisite: 必需的

**[1341.92s] English:** gen who i believe has an ss you can order coffee via ssh oh yeah we did that we did that uh so can  
**Translation:** 

**[1351.56s] English:** that also the model do that like feed you and like yeah and provide you with caffeine okay so that's  
**Translation:** Vocabulary: caffeine: 咖啡因

**[1357.90s] English:** the general framework yeah yeah and the magic moment would be if it is programming is this  
**Translation:** 

**[1365.38s] English:** weird discipline where um sometimes the next five minutes not always but sometimes the next five  
**Translation:** 

**[1371.46s] English:** minutes what you're  
**Translation:** 

**[1371.90s] English:** going to do is actually predictable from the stuff you've done recently and so can you get  
**Translation:** Vocabulary: predictable: 可预测的

**[1374.98s] English:** to a world where that next five minutes either happens by you disengaging and it taking you  
**Translation:** 

**[1379.12s] English:** through or maybe a little bit more of just you seeing next step what it's going to do and you're  
**Translation:** Vocabulary: disengaging: 脱离

**[1383.50s] English:** like okay that's good that's good that's good that's good and you can just sort of tap tap tap  
**Translation:** 

**[1387.08s] English:** through these big changes as we're talking about this as you've mentioned like one of the really  
**Translation:** 

**[1392.30s] English:** cool and noticeable things about cursor is that there's this whole diff interface situation going  
**Translation:** 

**[1397.24s] English:** on so like the model suggests with uh with the red and the green  
**Translation:** Vocabulary: interface: 界面

**[1401.88s] English:** of like here's how we're going to modify the code and in the chat window you can apply and it shows  
**Translation:** 

**[1407.78s] English:** you the diff and you can accept the diff so maybe can you speak to whatever direction of that we'll  
**Translation:** 

**[1412.84s] English:** probably have like four or five different kinds of diffs uh so we we have optimized the diff for  
**Translation:** 

**[1419.52s] English:** for the autocomplete so that has a different diff interface than uh then when you're reviewing  
**Translation:** Vocabulary: autocomplete: 自动完成; optimized: 优化

**[1425.80s] English:** larger blocks of code and then we're trying to optimize uh another diff thing for when you're  
**Translation:** 

**[1431.88s] English:** doing multiple different files uh and and sort of at a high level the difference is for when you're  
**Translation:** Vocabulary: optimize: 优化

**[1439.62s] English:** doing auto  
**Translation:** 

**[1440.00s] English:** autocomplete it should be really really fast to read uh actually it should be really fast to read  
**Translation:** 

**[1445.16s] English:** in all situations uh but in autocomplete it's sort of you're really like your eyes focused in one  
**Translation:** 

**[1450.90s] English:** area you you can't be in too many you the humans can't look in too many different places so you're  
**Translation:** 

**[1455.66s] English:** talking about on the interface side on the interface so it currently has this box on the  
**Translation:** 

**[1459.88s] English:** side so we have the current box and if it tries to delete code in some place and tries to add  
**Translation:** 

**[1466.32s] English:** other code it tries to show you a box on the side maybe show it if we pull it up and cursor.com  
**Translation:** 

**[1471.18s] English:** this is what we're talking about so that that box it was like three or four different attempts at  
**Translation:** 

**[1478.60s] English:** trying to make this this thing work where first the attempt was like this blue crossed out line  
**Translation:** 

**[1485.56s] English:** so before it was a box on the side it used to show you the code to delete by showing you like  
**Translation:** 

**[1491.24s] English:** like google doc style you would see like a line through it then you would see the  
**Translation:** 

**[1495.98s] English:** the  
**Translation:** 

**[1496.30s] English:** new code and that was super distracting and then we tried many different you know there was there  
**Translation:** 

**[1502.68s] English:** was sort of deletions there was trying to red highlight then the next iteration of it which  
**Translation:** Vocabulary: distracting: 分心; iteration: 迭代

**[1508.44s] English:** is sort of funny would you would hold the on mac the option button so it would it would sort of  
**Translation:** 

**[1515.72s] English:** highlight a region of code to show you that there might be something coming so maybe in this example  
**Translation:** 

**[1521.66s] English:** like the input and the value would get would all get blue  
**Translation:** 

**[1525.96s] English:** and the blue would to highlight that the ai had a suggestion for you  
**Translation:** 

**[1530.08s] English:** so instead of directly showing you the thing it would show you that the ai it would just hint  
**Translation:** 

**[1535.36s] English:** that the ai had a suggestion and if you really wanted to see it you would hold the option button  
**Translation:** 

**[1539.86s] English:** and then you would see the new suggestion then if you release the option button you would then  
**Translation:** 

**[1545.94s] English:** see your original code so that's by the way that's pretty nice but you have to know to hold the option  
**Translation:** 

**[1551.00s] English:** one yeah i say by the way i'm not a mac user but i got it  
**Translation:** 

**[1554.56s] English:** it was it was i got it it was it was it was kind of a weird idea because it was completely an option that—  
**Translation:** 

**[1555.10s] English:** but then you wouldn'tand it wouldn't be like that anymore so why would whatever thing i had an option button and i had an option button after it wouldn't buy it except for something else.  
**Translation:** 

**[1555.96s] English:** It's a button, I guess, you people have.  
**Translation:** 

**[1559.22s] English:** It's, you know,  
**Translation:** 

**[1560.00s] English:** Again, it's just non-intuitive.  
**Translation:** 

**[1561.96s] English:** I think that's the key thing.  
**Translation:** 

**[1563.72s] English:** And there's a chance this is also not the final version of it.  
**Translation:** 

**[1566.42s] English:** I am personally very excited for making a lot of improvements in this area.  
**Translation:** 

**[1573.80s] English:** We often talk about it as the verification problem,  
**Translation:** Vocabulary: verification: 验证问题

**[1577.94s] English:** where these diffs are great for small edits.  
**Translation:** 

**[1581.56s] English:** For large edits, or when it's multiple files or something,  
**Translation:** 

**[1585.70s] English:** it's actually a little bit prohibitive.  
**Translation:** 

**[1590.00s] English:** to review these diffs.  
**Translation:** Vocabulary: prohibitive: 昂贵到不实际

**[1592.74s] English:** And so there are a couple of different ideas here.  
**Translation:** 

**[1596.56s] English:** One idea that we have is,  
**Translation:** 

**[1598.30s] English:** parts of the diffs are important.  
**Translation:** 

**[1601.10s] English:** They have a lot of information.  
**Translation:** 

**[1602.48s] English:** And then parts of the diff are just very low entropy.  
**Translation:** 

**[1606.60s] English:** They're the same thing over and over again.  
**Translation:** Vocabulary: entropy: 信息量少

**[1609.58s] English:** And so maybe you can highlight the important pieces  
**Translation:** 

**[1612.12s] English:** and then gray out the not-so-important pieces.  
**Translation:** 

**[1615.06s] English:** Or maybe you can have a model that looks at the diff  
**Translation:** 

**[1618.50s] English:** and sees, oh, there is...  
**Translation:** 

**[1620.16s] English:** there's a likely bug here.  
**Translation:** 

**[1621.36s] English:** I will mark this with a little red squiggly and say,  
**Translation:** Vocabulary: squiggly: 波浪线

**[1624.72s] English:** you should probably review this part of the diff.  
**Translation:** 

**[1627.92s] English:** And ideas in that vein, I think, are exciting.  
**Translation:** 

**[1631.72s] English:** Yeah, that's a really fascinating space of UX design engineering.  
**Translation:** 

**[1636.12s] English:** So you're basically trying to guide the human programmer  
**Translation:** Vocabulary: programmer: 程序员

**[1640.92s] English:** through all the things they need to read and nothing more, like optimally.  
**Translation:** 

**[1645.32s] English:** Yeah, and you want an intelligent model to do it.  
**Translation:** Vocabulary: optimally: 最优化地

**[1648.16s] English:** Like currently,  
**Translation:** 

**[1648.72s] English:** diffs algorithm,  
**Translation:** Vocabulary: algorithm: 算法

**[1649.76s] English:** diff algorithms are just normal algorithms.  
**Translation:** 

**[1656.12s] English:** There is no intelligence.  
**Translation:** 

**[1658.04s] English:** There's intelligence that went into designing the algorithm,  
**Translation:** 

**[1660.34s] English:** but then you don't care if it's about this thing or this thing,  
**Translation:** 

**[1665.38s] English:** as you want a model to do this.  
**Translation:** 

**[1667.34s] English:** So I think the general question is,  
**Translation:** 

**[1671.42s] English:** Matt, these models are going to get much smarter.  
**Translation:** 

**[1673.70s] English:** As the models get much smarter,  
**Translation:** 

**[1675.96s] English:** the changes they will be able to propose are much bigger.  
**Translation:** 

**[1679.76s] English:** So,  
**Translation:** 

**[1680.00s] English:** as the changes gets bigger and bigger and bigger the humans have to do more and more and more  
**Translation:** 

**[1683.78s] English:** verification work it gets more and more and more hard like it's just you need you need to help them  
**Translation:** 

**[1688.46s] English:** out it's sort of i don't want to spend all my time reviewing code uh can you say a little more  
**Translation:** 

**[1696.38s] English:** across multiple files div yeah i mean so github tries to solve this right with code review when  
**Translation:** 

**[1705.28s] English:** you're doing code review you're reviewing multiple diffs across multiple files but like arvid said  
**Translation:** 

**[1710.68s] English:** earlier i think you can do much better than code review you know code review kind of sucks like you  
**Translation:** Vocabulary: arvid: 阿维德

**[1717.26s] English:** spend a lot of time trying to grok this code that's often quite unfamiliar to you and it often  
**Translation:** 

**[1724.34s] English:** like doesn't even actually catch that many bugs and i think you can significantly significantly  
**Translation:** Vocabulary: unfamiliar: 不熟悉

**[1729.82s] English:** improve that review experience using language models for example using the kinds of tricks  
**Translation:** 

**[1733.68s] English:** that arvid had described maybe  
**Translation:** 

**[1735.26s] English:** pointing you towards the regions that actually matter um i think also if the code is produced  
**Translation:** 

**[1743.92s] English:** by these language models and it's not produced by someone else like the code review experience  
**Translation:** 

**[1750.14s] English:** is designed for both the reviewer and the person that produced the code in the case where the  
**Translation:** 

**[1757.54s] English:** person that produced the code is the language model you don't have to care that much about  
**Translation:** 

**[1761.56s] English:** their experience and you can design the entire thing around the reviewer such that  
**Translation:** 

**[1765.24s] English:** the reviewer's job is as fun as easy as productive as possible um and i think that that feels like  
**Translation:** 

**[1774.00s] English:** the issue with just kind of naively trying to make these things look like code review i think  
**Translation:** 

**[1779.66s] English:** you can be a lot more creative and and push the boundary on what's possible just one one idea  
**Translation:** Vocabulary: naively: 天真地

**[1784.28s] English:** there is i think ordering matters generally when you review a pr you you have this list of files  
**Translation:** 

**[1790.06s] English:** and you're reviewing them from top to bottom but actually like you actually want to understand this  
**Translation:** 

**[1795.24s] English:** part first because that came like logically first and then you want to understand the next part and  
**Translation:** 

**[1800.00s] English:** you don't want to have to figure out that yourself you want a model to guide you through the thing  
**Translation:** Vocabulary: logically: 合乎逻辑地

**[1805.24s] English:** and is the step of creation going to be more and more natural language is the goal versus with  
**Translation:** 

**[1811.40s] English:** actual i think sometimes i don't think it's going to be the case that all of programming will be  
**Translation:** 

**[1816.94s] English:** natural language and the reason for that is you know if i'm pair programming with swallow and  
**Translation:** 

**[1822.52s] English:** swallow is at the computer in the keyboard and sometimes if i'm like driving i want to  
**Translation:** 

**[1828.32s] English:** say to swallow hey like implement this function and that that works and then sometimes it's just  
**Translation:** 

**[1834.78s] English:** so annoying to explain to swallow what i want him to do and so i actually take over the keyboard  
**Translation:** 

**[1839.94s] English:** and i show him i write like part of the example and then it makes sense and that's the easiest  
**Translation:** 

**[1846.32s] English:** way to communicate and so i think that's also the case for ai like sometimes the easiest way  
**Translation:** 

**[1850.70s] English:** to communicate with the ai will be to show an example and then it goes and does the thing  
**Translation:** 

**[1854.06s] English:** everywhere else or sometimes if you're making a website for example  
**Translation:** 

**[1857.24s] English:** the easiest way to show to the ai what you want is not to tell it what to do but you know drag  
**Translation:** 

**[1863.36s] English:** things around or draw things um and yeah and and like maybe eventually we will get to like  
**Translation:** 

**[1869.48s] English:** brain machine interfaces or whatever and kind of like understand what you're thinking and so i think  
**Translation:** 

**[1873.24s] English:** natural language will have a place i think it will not definitely not be the way most people  
**Translation:** Vocabulary: interfaces: 接口

**[1878.32s] English:** program most of the time i'm really feeling the agi with this editor  
**Translation:** 

**[1882.50s] English:** it feels like there's a lot of machine learning going on underneath  
**Translation:** 

**[1887.24s] English:** tell me about some of the ml stuff that makes it all work  
**Translation:** 

**[1890.50s] English:** where cursor really works via this ensemble of custom models that that we've trained alongside  
**Translation:** Vocabulary: ensemble: 集成模型

**[1897.00s] English:** you know the frontier models that are fantastic at the reasoning intense things and so cursor tab  
**Translation:** 

**[1901.66s] English:** for example is a great example of where you can specialize this model to be even better than even  
**Translation:** Vocabulary: frontier: 最前沿; specialize: 专门化

**[1906.88s] English:** frontier models if you look at evals on the task we set it at the other domain which it's kind of  
**Translation:** 

**[1912.08s] English:** surprising that it requires custom models but but it's kind of necessary and works quite well  
**Translation:** 

**[1917.24s] English:** in apply um so  
**Translation:** 

**[1920.00s] English:** i think these models are like the frontier models are quite good at sketching out plans  
**Translation:** Vocabulary: sketching: 草图绘制

**[1924.70s] English:** for code and generating like rough sketches of like the change but actually creating diffs  
**Translation:** 

**[1930.72s] English:** is quite hard um for frontier models for your training models um like you try to do this with  
**Translation:** 

**[1938.92s] English:** sonnet with o1 any frontier model and it really messes up stupid things like counting line numbers  
**Translation:** 

**[1945.26s] English:** especially in super super large files um and so what we've done to alleviate this is we let the  
**Translation:** Vocabulary: alleviate: 缓解

**[1952.42s] English:** model kind of sketch out this rough code block that indicates what the change will be and we  
**Translation:** 

**[1958.44s] English:** train a model to then apply that change to the file and we should say that apply is the model  
**Translation:** 

**[1965.50s] English:** looks at your code it gives you a really damn good suggestion of what new things to do and the  
**Translation:** 

**[1972.88s] English:** seemingly for humans trivial step of  
**Translation:** 

**[1975.26s] English:** combining the two you're saying is not so trivial contrary to popular perception it is not a  
**Translation:** 

**[1981.90s] English:** deterministic algorithm yeah i i think like you see shallow copies of apply um elsewhere and it  
**Translation:** Vocabulary: algorithm: 算法; deterministic: 决定论的

**[1989.94s] English:** just breaks like most of the time because you think you can kind of try to do some deterministic  
**Translation:** 

**[1993.52s] English:** matching and then it fails you know at least 40 of the time and that just results in a terrible  
**Translation:** 

**[2000.18s] English:** product experience um i think in general this this regime  
**Translation:** 

**[2005.24s] English:** of you are going to get smarter and smarter models and like so one other thing that apply lets you do  
**Translation:** 

**[2011.72s] English:** is it lets you use fewer tokens with the most intelligent models  
**Translation:** 

**[2017.08s] English:** this is both expensive in terms of latency for generating all these tokens  
**Translation:** Vocabulary: latency: 响应延迟

**[2022.52s] English:** and cost so you can give this very very rough sketch and then have your small models go and  
**Translation:** 

**[2029.24s] English:** implement it because it's a much easier task to implement this very very sketched out code and i  
**Translation:** Vocabulary: sketched: 草图

**[2034.28s] English:** think that this this really is a very important part of the process and i think that this this  
**Translation:** 

**[2035.08s] English:** really is a very important part of the process and i think that this this really is a very important  
**Translation:** 

**[2035.24s] English:** part of the process and i think that this this really is a very important part of the regime will continue where  
**Translation:** 

**[2036.44s] English:** regime will continue where you can use smarter and smarter models to do the  
**Translation:** 

**[2038.44s] English:** you can use smarter and smarter models to do the planning and then maybe the inflation  
**Translation:** 

**[2039.96s] English:** planning and then maybe the inflation  
**Translation:** 

**[2040.00s] English:** details uh can be handled by the less intelligent ones perhaps you'll have you know maybe a one  
**Translation:** 

**[2045.72s] English:** maybe it'll be even more capable models given an even higher level plan that is kind of recursively  
**Translation:** Vocabulary: recursively: 递归地

**[2052.34s] English:** uh applied by sonnet and an apply model maybe we should we should talk about how to how to make it  
**Translation:** 

**[2058.44s] English:** fast yeah i feel like yeah fast is always an interesting detail that's good yeah how do you  
**Translation:** 

**[2063.78s] English:** make it fast yeah so one big component of making it fast is speculative edits so speculative edits  
**Translation:** 

**[2070.88s] English:** are a variant of speculative decoding and maybe it'd be helpful to briefly describe speculative  
**Translation:** Vocabulary: speculative: 推测性的

**[2076.08s] English:** decoding um with speculative decoding what you do is you you can kind of take advantage of the fact  
**Translation:** 

**[2082.96s] English:** that you know most of the time and i'll add the caveat that it would be when you're memory bound  
**Translation:** Vocabulary: caveat: 免责声明

**[2088.90s] English:** in language model generation um if you  
**Translation:** 

**[2093.78s] English:** process multiple tokens at once um it is faster than generating one token at a time  
**Translation:** Vocabulary: token: 标记

**[2098.22s] English:** so this is like the same reason why if you look at tokens per second uh with prompt tokens versus  
**Translation:** 

**[2104.40s] English:** generated tokens it's much much faster for prompt tokens um so what we do is instead of using what  
**Translation:** 

**[2112.40s] English:** speculative decoding normally does which is using a really small model to predict these draft tokens  
**Translation:** 

**[2117.00s] English:** that your larger model will then go in and verify um with code edits we have a very strong  
**Translation:** Vocabulary: verify: 验证

**[2123.60s] English:** process to predict these draft tokens and then we can go in and verify um with code edits we have a  
**Translation:** 

**[2123.76s] English:** prior of what the existing code will look like and that prior is literally the same exact code  
**Translation:** 

**[2129.20s] English:** so you can do is you can just feed chunks of the original code back into the into the model  
**Translation:** 

**[2133.48s] English:** and then the model will just pretty much agree most of the time that okay i'm just going to  
**Translation:** 

**[2139.62s] English:** spit this code back out and so you can process all of those lines in parallel and you just do  
**Translation:** 

**[2144.06s] English:** this with sufficiently many chunks and eventually you'll reach a point of disagreement where the  
**Translation:** 

**[2148.38s] English:** model will now predict text that is different from the ground truth original code it'll  
**Translation:** 

**[2153.58s] English:** generate those tokens and then we kind of will decide after enough tokens match uh the original  
**Translation:** 

**[2158.82s] English:** code to re  
**Translation:** 

**[2160.00s] English:** start speculating in chunks of code. What this actually ends up looking like is just a much  
**Translation:** Vocabulary: speculating: 猜测

**[2166.14s] English:** faster version of normal editing code. So it looks like a much faster version of the model  
**Translation:** 

**[2172.82s] English:** rewriting all the code. So we can use the same exact interface that we use for diffs, but it  
**Translation:** Vocabulary: interface: 接口; rewriting: 重写

**[2179.36s] English:** will just stream down a lot faster. And then the advantage is that wireless streaming, you can just  
**Translation:** 

**[2185.08s] English:** also be reviewing, start reviewing the code before it's done. So there's no big loading screen.  
**Translation:** Vocabulary: wireless: 无线

**[2192.14s] English:** So maybe that is part of the advantage. So the human can start reading before the thing is done.  
**Translation:** 

**[2199.32s] English:** I think the interesting riff here is something like, speculation is a fairly common idea  
**Translation:** Vocabulary: speculation: 猜测

**[2204.94s] English:** nowadays. It's like not only in language models, I mean, there's obviously speculation in CPUs,  
**Translation:** 

**[2209.30s] English:** and there's speculation for databases, and speculation all over the place.  
**Translation:** Vocabulary: databases: 数据库

**[2214.32s] English:** Well, let me ask.  
**Translation:** 

**[2215.10s] English:** This is sort of the ridiculous question of which LLM is better at coding. GPT,  
**Translation:** 

**[2220.76s] English:** Claude, who wins in the context of programming? And I'm sure the answer is much more nuanced,  
**Translation:** 

**[2225.72s] English:** because it sounds like every single part of this involves a different model.  
**Translation:** Vocabulary: nuanced: 细腻的

**[2232.14s] English:** Yeah, I think there's no model that Pareto dominates others, meaning it is better in  
**Translation:** 

**[2240.54s] English:** all categories that we think matter. The categories being speed,  
**Translation:** Vocabulary: dominates: 超越; pareto: 帕累托

**[2245.08s] English:** ability to edit code, ability to process lots of code, long context,  
**Translation:** 

**[2252.02s] English:** you know, a couple of other things, and kind of coding capabilities.  
**Translation:** 

**[2255.22s] English:** The one that I'd say right now is just kind of net best is Sonnet. I think this is a consensus  
**Translation:** 

**[2260.26s] English:** opinion. Our one's really interesting, and it's really good at reasoning. So if you give it really  
**Translation:** 

**[2266.08s] English:** hard programming interview style problems, or lead code problems, it can do quite well on them.  
**Translation:** 

**[2273.60s] English:** But it doesn't feel...  
**Translation:** 

**[2275.08s] English:** like it kind of understands your rough intent as well as Sonnet does.  
**Translation:** 

**[2280.00s] English:** like if you look at a lot of the other frontier models um one qualm i have is it feels like  
**Translation:** Vocabulary: frontier: 前沿; qualm: 顾虑

**[2287.88s] English:** they're not necessarily over i'm not saying they train on benchmarks um but they perform really  
**Translation:** 

**[2293.00s] English:** well in benchmarks relative to kind of everything that's kind of in the middle so if you tried on  
**Translation:** Vocabulary: benchmarks: 评估标准

**[2298.42s] English:** all these benchmarks and things that are in the distribution of the benchmarks they're evaluated  
**Translation:** 

**[2301.76s] English:** on you know they'll do really well but when you push them a little bit outside of that sonnet's  
**Translation:** Vocabulary: evaluated: 评估过的

**[2306.06s] English:** i think the one that that kind of does best at kind of maintaining that same capability like  
**Translation:** 

**[2311.58s] English:** you kind of have the same capability in the benchmark as when you try to instruct it to do  
**Translation:** Vocabulary: benchmark: 衡量标准; capability: 能力; instruct: 指示

**[2315.50s] English:** anything with coding what another ridiculous question is the difference between the normal  
**Translation:** 

**[2321.00s] English:** programming experience versus what benchmarks represent like where do benchmarks fall short  
**Translation:** 

**[2326.80s] English:** do you think when we're evaluating these models by the way that's like a really really hard  
**Translation:** 

**[2330.94s] English:** it's like like critically important detail like how how different like  
**Translation:** Vocabulary: critically: 至关重要; evaluating: 评估

**[2335.76s] English:** benchmarking is from a benchmarking perspective to a benchmarking perspective  
**Translation:** 

**[2336.06s] English:** versus versus like real coding where real coding it's not interview style coding it's you're you're  
**Translation:** Vocabulary: benchmarking: 基准测试

**[2344.60s] English:** doing these you know humans are saying like half broken english sometimes and sometimes you're  
**Translation:** 

**[2351.74s] English:** saying like oh do what i did before sometimes you're saying uh you know go add this thing and  
**Translation:** 

**[2359.16s] English:** do this other thing for me and then make this ui element and then you know it's just like a lot of  
**Translation:** 

**[2365.56s] English:** things are sort of  
**Translation:** 

**[2366.06s] English:** context dependent you really want to like understand the human and then do do what the  
**Translation:** 

**[2371.10s] English:** human wants as opposed to sort of this maybe the the way to put it is sort of abstractly is  
**Translation:** Vocabulary: abstractly: 抽象地

**[2375.76s] English:** uh the interview problems are very well specified they lean a lot on specification  
**Translation:** 

**[2384.26s] English:** while the human stuff is less specified yeah i think that this this benchmark question is  
**Translation:** Vocabulary: specification: 详细说明; specified: 规定

**[2392.12s] English:** both complicated by what um so all i just mentioned and then also  
**Translation:** 

**[2396.06s] English:** to what amman was getting into is that even  
**Translation:** Vocabulary: amman: 安曼

**[2399.98s] English:** you  
**Translation:** 

**[2400.00s] English:** if you like you know there's this problem of like the skew between what can you actually model in a  
**Translation:** 

**[2403.10s] English:** benchmark versus uh real programming and that can be sometimes hard to encapsulate because it's like  
**Translation:** 

**[2407.94s] English:** real programming is like very messy and sometimes things aren't super well specified what's correct  
**Translation:** Vocabulary: encapsulate: 封装

**[2413.12s] English:** or what isn't but then uh it's also doubly hard because of this public benchmark problem and  
**Translation:** 

**[2418.52s] English:** that's both because public benchmarks are sometimes kind of hill climbed on but then it's like really  
**Translation:** Vocabulary: benchmarks: 公开基准

**[2422.60s] English:** really hard to also get the data from the public benchmarks out of the models and so for instance  
**Translation:** 

**[2429.22s] English:** like one of the most popular like agent benchmarks sweet bench um is really really  
**Translation:** 

**[2435.60s] English:** contaminated and the training data of uh these foundation models and so if you ask these  
**Translation:** 

**[2440.26s] English:** foundation models to do a sweet bench problem you actually don't give them the context of a code base  
**Translation:** Vocabulary: contaminated: 污染的

**[2443.88s] English:** they can like hallucinate the right file pass they can hallucinate the right function names  
**Translation:** 

**[2447.28s] English:** um and so the the it's it's also just the public aspect of these things is tricky  
**Translation:** Vocabulary: hallucinate: 妄想

**[2452.78s] English:** yeah like in that case it could be trained on the literal issues or pull requests themselves  
**Translation:** 

**[2458.38s] English:** and and  
**Translation:** 

**[2459.22s] English:** maybe the labs will start to do a better job um or they've already done a good job at  
**Translation:** 

**[2463.90s] English:** decontaminating those things but they're not going to emit the actual training data of the  
**Translation:** Vocabulary: decontaminating: 消毒

**[2468.48s] English:** repository itself like these are all like some of the most popular python repositories like  
**Translation:** 

**[2472.80s] English:** simpi is one example i don't think they're going to handicap their models on simpi and all these  
**Translation:** Vocabulary: handicap: 限制; repositories: 存储库; repository: 存储库

**[2478.62s] English:** popular python repositories in order to get uh true evaluation scores in these benchmarks yeah  
**Translation:** 

**[2483.96s] English:** i think that given the dearths and benchmarks um there have been like a  
**Translation:** 

**[2489.22s] English:** few interesting crutches that uh places that build systems with these models or build these models  
**Translation:** 

**[2493.90s] English:** actually use to get a sense of are they going the right direction or not and uh in a lot of places  
**Translation:** Vocabulary: crutches: 辅助工具

**[2499.02s] English:** uh people will actually just have humans play with the things and give qualitative feedback on these  
**Translation:** 

**[2503.62s] English:** um like one or two of the foundation model companies they they have people who that's  
**Translation:** Vocabulary: qualitative: 质量上的

**[2507.50s] English:** that's a big part of their role and you know internally we also uh you know qualitatively  
**Translation:** 

**[2512.34s] English:** assess these models and actually lean on that a lot in addition to like private evals that we have  
**Translation:** Vocabulary: internally: 内部; qualitatively: 质量上

**[2516.34s] English:** it's like the vibe  
**Translation:** 

**[2517.90s] English:** divide yeah the vibe  
**Translation:** 

**[2519.22s] English:** Thank you.  
**Translation:** 

**[2520.00s] English:** vibe benchmark human benchmark yeah you pull in the humans to do a vibe check yeah okay i mean  
**Translation:** Vocabulary: benchmark: 标准

**[2526.98s] English:** that's that's kind of what i do like just like reading online forums and reddit and x just like  
**Translation:** 

**[2532.98s] English:** well i don't know how to properly load in people's opinions because they'll say things like  
**Translation:** 

**[2540.14s] English:** i feel like claude or gpt's gotten dumber or something they'll say i feel like and then i  
**Translation:** 

**[2548.10s] English:** sometimes feel like that too but i wonder if it's the model's problem or mine yeah with claude  
**Translation:** 

**[2554.54s] English:** there's an interesting take i heard where i think aws has different chips um and i i suspect they  
**Translation:** 

**[2562.88s] English:** have slightly different numerics than uh nvidia gpus and someone speculated that claude's  
**Translation:** Vocabulary: numerics: 数字特性; speculated: 推测

**[2569.56s] English:** degraded performance had to do with maybe using the quantized version that existed on aws bedrock  
**Translation:** 

**[2575.92s] English:** versus uh whatever  
**Translation:** Vocabulary: bedrock: 基础; degraded: 下降; quantized: 量化

**[2578.10s] English:** was running on on anthropics gpus i interview a bunch of people that have conspiracy theories so  
**Translation:** 

**[2583.04s] English:** i'm glad you spoke to this conspiracy well it's it's not not like conspiracy theory as much  
**Translation:** Vocabulary: anthropics: 人类中心主义

**[2589.30s] English:** they're just they're like they're you know humans humans are humans and there's there's these details  
**Translation:** 

**[2594.20s] English:** and you know you're doing like this crazy amount of flops and you know chips are messy and man you  
**Translation:** Vocabulary: flops: 计算量

**[2601.66s] English:** can just have bugs like bugs are it's it's hard to overstate how hard bugs are to avoid  
**Translation:** 

**[2608.10s] English:** what's uh the role of a good prompt in all this see you mentioned that benchmarks have really  
**Translation:** Vocabulary: benchmarks: 衡量标准; overstate: 夸大其词

**[2615.08s] English:** uh structured well-formulated prompts what what should a human be doing to maximize success  
**Translation:** 

**[2623.76s] English:** and what's the importance of what the humans you wrote a blog post on you called it prompt design  
**Translation:** Vocabulary: maximize: 最大化

**[2629.96s] English:** yeah uh i think it depends on which model you're using and all of them are slightly different and  
**Translation:** 

**[2637.46s] English:** they respond to the same model and they respond to the same model and they respond to the same model  
**Translation:** 

**[2638.10s] English:** differently to different prompts  
**Translation:** 

**[2640.00s] English:** But I think the original GPT-4 and the original sort of pre-double models last year, they were quite sensitive to the prompts.  
**Translation:** 

**[2650.62s] English:** They also had a very small context window.  
**Translation:** 

**[2653.62s] English:** And so we have all of these pieces of information around the code base that would maybe be relevant in the prompt.  
**Translation:** 

**[2660.36s] English:** Like you have the docs, you have the files that you add, you have the conversation history.  
**Translation:** 

**[2664.70s] English:** And then there's a problem like how do you decide what you actually put in the prompt?  
**Translation:** 

**[2668.72s] English:** And when you have a limited space.  
**Translation:** 

**[2670.78s] English:** And even for today's models, even when you have long context, filling out the entire context window means that it's slower.  
**Translation:** 

**[2677.98s] English:** It means that sometimes the model actually gets confused and some models get more confused than others.  
**Translation:** 

**[2683.20s] English:** And we have this one system internally that we call pre-empt, which helps us with that a little bit.  
**Translation:** Vocabulary: internally: 内部

**[2689.12s] English:** And I think it was built for the era before where we had 8,000.  
**Translation:** 

**[2698.40s] English:** Yeah.  
**Translation:** 

**[2698.72s] English:** Token context windows.  
**Translation:** 

**[2701.10s] English:** And it's a little bit similar to when you're making a website.  
**Translation:** Vocabulary: token: 令牌

**[2706.10s] English:** You sort of, you want it to work on mobile.  
**Translation:** 

**[2709.88s] English:** You want it to work on a desktop screen.  
**Translation:** 

**[2712.36s] English:** And you have this dynamic information, which you don't have, for example, if you're making, like designing a print magazine.  
**Translation:** 

**[2720.00s] English:** You have like, you know exactly where you can put stuff.  
**Translation:** 

**[2722.16s] English:** But when you have a website or when you have a prompt, you have these inputs.  
**Translation:** 

**[2725.52s] English:** And then you need to format them to always work.  
**Translation:** 

**[2727.78s] English:** Even if the input is really...  
**Translation:** 

**[2728.72s] English:** If the input is really big, then you might have to cut something down.  
**Translation:** 

**[2731.24s] English:** And so the idea was, OK, like, let's take some inspiration.  
**Translation:** 

**[2734.46s] English:** What's the best way to design websites?  
**Translation:** 

**[2737.42s] English:** Well, the thing that we really like is React and the declarative approach where you use JSX in JavaScript and then you declare, this is what I want.  
**Translation:** 

**[2750.34s] English:** And I think this has higher priority or like this has higher z-index than something else.  
**Translation:** Vocabulary: declarative: 声明式的

**[2756.40s] English:** And then you have this rendering.  
**Translation:** 

**[2758.64s] English:** And then you have this rendering.  
**Translation:** 

**[2758.72s] English:** In web design.  
**Translation:** 

**[2760.00s] English:** And it's like Chrome, and in our case, it's a preempt renderer, which then fits everything onto the page.  
**Translation:** Vocabulary: renderer: 渲染器

**[2767.04s] English:** And as you clearly decide what you want, and then it figures out what you want.  
**Translation:** 

**[2771.74s] English:** And so we have found that to be quite helpful.  
**Translation:** 

**[2774.34s] English:** And I think the role of it has sort of shifted over time, where initially it was to fit to these small context windows.  
**Translation:** 

**[2781.72s] English:** Now it's really useful because it helps us with splitting up the data that goes into the prompt and the actual rendering of it.  
**Translation:** 

**[2790.26s] English:** And so it's easier to debug because you can change the rendering of the prompt and then try it on old prompts because you have the raw data that went into the prompt.  
**Translation:** 

**[2799.94s] English:** And then you can see, did my change actually improve it for this entire eval set?  
**Translation:** 

**[2805.16s] English:** So do you literally prompt with JSX?  
**Translation:** 

**[2808.10s] English:** Yes.  
**Translation:** 

**[2808.88s] English:** So it kind of looks like React.  
**Translation:** 

**[2810.56s] English:** There are components.  
**Translation:** 

**[2811.36s] English:** We have one component that's a file component, and it takes in the cursor.  
**Translation:** 

**[2817.62s] English:** Usually there's one line where the cursor is.  
**Translation:** 

**[2820.00s] English:** And that's probably the most important line because that's the one you're looking at.  
**Translation:** 

**[2823.70s] English:** And so then you can give priorities.  
**Translation:** Vocabulary: priorities: 优先级

**[2825.10s] English:** So that line has the highest priority, and then you subtract one for every line that is farther away.  
**Translation:** 

**[2831.68s] English:** And then eventually when it's rendered, it figures out how many lines can actually fit, and it centers around that thing.  
**Translation:** Vocabulary: subtract: 减去

**[2837.12s] English:** That's amazing.  
**Translation:** 

**[2837.60s] English:** And you can do other fancy things where if you have lots of code blocks from the entire code base, you could use retrieval and things like embedding and re-ranking scores to add priorities for each of these components.  
**Translation:** Vocabulary: embedding: 嵌入式表示; retrieval: 检索

**[2850.56s] English:** So should humans, when they ask questions, also try to use something like that?  
**Translation:** 

**[2855.80s] English:** Would it be beneficial to write JSX in the problem?  
**Translation:** 

**[2859.98s] English:** Or the whole idea is it should be loose and messy?  
**Translation:** 

**[2863.32s] English:** I think our goal is kind of that you should just do whatever is the most natural thing for you.  
**Translation:** 

**[2869.78s] English:** And then our job is to figure out how do we actually retrieve the relative event thing so that your thing actually makes sense.  
**Translation:** 

**[2876.70s] English:** Well, this is sort of the discussion I had with Arvind.  
**Translation:** Vocabulary: retrieve: 检索

**[2880.00s] English:** of perplexity is like his whole idea is like you should let the person be as lazy yes yeah but like  
**Translation:** 

**[2887.52s] English:** yeah that's a beautiful thing but i feel like you're allowed to ask more of programmers right  
**Translation:** Vocabulary: perplexity: 困惑; programmers: 程序员

**[2894.16s] English:** so like if you say just do what you want i mean humans are lazy there's a kind of tension between  
**Translation:** 

**[2900.36s] English:** just being lazy versus like provide more as uh be prompted almost like the system  
**Translation:** 

**[2906.74s] English:** pressuring you or inspiring you to be articulate not in terms of the grammar of the sentences but  
**Translation:** 

**[2914.60s] English:** in terms of the depth of thoughts that you convey inside the uh the prompts i think even as a system  
**Translation:** Vocabulary: articulate: 表达清晰

**[2920.00s] English:** gets closer to some level of perfection often when you ask the model for something you just  
**Translation:** 

**[2927.52s] English:** are not not enough intent is conveyed to know what to do and there are like a few ways to resolve  
**Translation:** Vocabulary: conveyed: 传达

**[2933.38s] English:** that intent one is the simple thing of having the model just  
**Translation:** 

**[2936.74s] English:** ask you i'm not sure how to do these parts based on your query could you clarify that  
**Translation:** 

**[2944.26s] English:** i think the other could be maybe if you there are five or six possible generations  
**Translation:** 

**[2951.94s] English:** given the uncertainty present in your query so far why don't we just actually show you all of  
**Translation:** 

**[2956.10s] English:** those and let you pick them how hard is it to for the model to choose to speak talk back sort of  
**Translation:** 

**[2964.82s] English:** versus generating that's a  
**Translation:** 

**[2966.74s] English:** it's hard to sort of like how to deal with the uncertainty do i do i choose to  
**Translation:** 

**[2971.82s] English:** ask for more information to reduce the ambiguity so i mean one of the things we we do is um it's  
**Translation:** Vocabulary: ambiguity: 不确定性

**[2979.58s] English:** like a recent addition is try to suggest files that you can add so and while you're typing  
**Translation:** 

**[2985.84s] English:** one can guess what the uncertainty is and maybe suggest that like you know maybe maybe you're  
**Translation:** 

**[2994.68s] English:** writing your api and you're writing your api and you're writing your api and you're writing your  
**Translation:** 

**[2996.74s] English:** api and uh we can get  
**Translation:** 

**[3000.00s] English:** using the commits that you've made previously  
**Translation:** 

**[3004.48s] English:** in the same file that the client and the server  
**Translation:** 

**[3007.64s] English:** is super useful.  
**Translation:** 

**[3009.34s] English:** And there's like a hard technical problem  
**Translation:** 

**[3012.56s] English:** of how do you resolve it across all commits,  
**Translation:** 

**[3015.36s] English:** which files are the most important  
**Translation:** 

**[3016.74s] English:** given your current prompt.  
**Translation:** 

**[3019.54s] English:** And we're still sort of, initial version is ruled out  
**Translation:** 

**[3022.88s] English:** and I'm sure we can make it much more accurate.  
**Translation:** 

**[3026.64s] English:** It's very experimental.  
**Translation:** 

**[3028.04s] English:** But then the idea is we show you like,  
**Translation:** 

**[3029.42s] English:** do you just want to add this file, this file, this file also  
**Translation:** 

**[3032.50s] English:** to tell the model to edit those files for you?  
**Translation:** 

**[3036.94s] English:** Because if maybe you're making the API,  
**Translation:** 

**[3039.16s] English:** like you should also edit the client and the server  
**Translation:** 

**[3041.04s] English:** that is using the API and the other one resolving the API.  
**Translation:** 

**[3044.24s] English:** And so that'll be kind of cool.  
**Translation:** 

**[3046.08s] English:** Both there's the phase where you're writing a prompt  
**Translation:** 

**[3049.24s] English:** and there's before you even click enter,  
**Translation:** 

**[3051.96s] English:** maybe we can help resolve some of the uncertainty.  
**Translation:** 

**[3054.46s] English:** To what degree do you use agentic approaches?  
**Translation:** 

**[3057.04s] English:** How useful are agents?  
**Translation:** 

**[3058.70s] English:** We think,  
**Translation:** 

**[3059.42s] English:** I think agents are really, really cool.  
**Translation:** 

**[3062.46s] English:** Like, I think agents is like,  
**Translation:** 

**[3066.14s] English:** it's like, it resembles sort of like a human,  
**Translation:** 

**[3067.96s] English:** it's sort of like the things like you can kind of feel  
**Translation:** 

**[3070.44s] English:** that it, like you're getting closer to AGI  
**Translation:** 

**[3072.60s] English:** because you see a demo where it acts as a human would.  
**Translation:** 

**[3077.66s] English:** And it's really, really cool.  
**Translation:** 

**[3079.70s] English:** I think agents are not yet super useful for many things.  
**Translation:** 

**[3086.70s] English:** They, I think we're getting close to where they will actually be useful.  
**Translation:** 

**[3089.26s] English:** They, I think we're getting close to where they will actually be useful.  
**Translation:** 

**[3089.42s] English:** And so I think there are certain types of tasks  
**Translation:** 

**[3095.24s] English:** where having an agent would be really nice.  
**Translation:** 

**[3099.66s] English:** Like I would love to have an agent.  
**Translation:** 

**[3100.74s] English:** For example, if like we have a bug  
**Translation:** 

**[3102.06s] English:** where you sometimes can't command C and command V  
**Translation:** 

**[3105.32s] English:** inside our chat input box.  
**Translation:** 

**[3108.48s] English:** And that's a task that's super well specified.  
**Translation:** Vocabulary: specified: 规定

**[3110.84s] English:** I just want to say like in two sentences,  
**Translation:** 

**[3112.58s] English:** this does not work, please fix it.  
**Translation:** 

**[3114.38s] English:** And then I would love to have an agent  
**Translation:** 

**[3115.84s] English:** that just goes off, does it.  
**Translation:** 

**[3118.14s] English:** And then,  
**Translation:** 

**[3119.42s] English:** a day later,  
**Translation:** 

**[3120.00s] English:** i i come back and i reviewed that the thing you mean it goes finds the right file yeah it finds  
**Translation:** 

**[3125.92s] English:** the right files it like tries to reproduce the bug it like fixes the bug and then it verifies  
**Translation:** Vocabulary: verifies: 验证

**[3130.88s] English:** that it's correct and this is could be a process that takes a long time um and so i think i would  
**Translation:** 

**[3136.10s] English:** love to have that uh and then i think a lot of programming like there is often this belief that  
**Translation:** 

**[3142.18s] English:** agents will take over all of programming um i don't think we think that that's the case because  
**Translation:** 

**[3148.54s] English:** a lot of programming a lot of the value is in iterating or you don't actually want to specify  
**Translation:** 

**[3154.28s] English:** something up front because you don't really know what you want until you've seen an initial version  
**Translation:** 

**[3158.98s] English:** and then you want to iterate on that and then you provide more information and so for a lot of  
**Translation:** 

**[3164.36s] English:** programming i think you actually want a system that's instant that gives you an initial version  
**Translation:** 

**[3168.34s] English:** instantly back and then you can iterate super super quickly uh what about something like that  
**Translation:** 

**[3174.08s] English:** came out replant agent that does also like setting up  
**Translation:** 

**[3178.38s] English:** you  
**Translation:** 

**[3178.54s] English:** the development environment installing software packages configuring everything configuring the  
**Translation:** 

**[3182.82s] English:** databases and actually deploying the app yeah is that also in the set of things you dream about  
**Translation:** Vocabulary: configuring: 配置; databases: 数据库; deploying: 部署

**[3189.20s] English:** i think so i think that would be really cool for for certain types of programming uh it would be  
**Translation:** 

**[3194.72s] English:** really cool is that within scope of cursor yeah we aren't actively working on it right now um  
**Translation:** 

**[3201.56s] English:** but it's definitely like we want to make the programmers life easier and more fun and  
**Translation:** 

**[3207.94s] English:** some things are just really tedious and you need to go through a bunch of steps and you want to  
**Translation:** Vocabulary: programmers: 程序员; tedious: 繁琐

**[3212.08s] English:** delegate that to an agent um and then some things you can actually have an agent in the background  
**Translation:** 

**[3216.54s] English:** while you're working like let's say you have a pr that's both back end and front end and you're  
**Translation:** Vocabulary: delegate: 授权

**[3221.78s] English:** working on the front end and then you can have a background agent that doesn't work and figure out  
**Translation:** 

**[3225.90s] English:** kind of what you're doing and then when you get to the back end part of your pr then you have some  
**Translation:** 

**[3231.50s] English:** like initial piece of code that you can iterate on um and and so that that would also be really cool  
**Translation:** 

**[3237.94s] English:** one of the things we already talked about  
**Translation:** 

**[3240.00s] English:** is speed but i wonder if we can just uh linger on that some more in the the various places  
**Translation:** 

**[3245.94s] English:** that uh the technical details involved in making this thing really fast so every single aspect of  
**Translation:** 

**[3253.38s] English:** cursor most aspects of cursor feel really fast like i mentioned the apply is probably the slowest  
**Translation:** 

**[3258.16s] English:** thing and for me from i'm sorry the pain it's a pain it's a pain that we're feeling and we're  
**Translation:** 

**[3264.98s] English:** working on fixing it uh yeah i mean it says something that something that feels i don't  
**Translation:** 

**[3270.40s] English:** know what it is like one second or two seconds that feels slow that means that's actually uh  
**Translation:** 

**[3276.02s] English:** shows that everything else is just really really fast um so is there some technical details about  
**Translation:** 

**[3281.14s] English:** how to make some of these models how to make the chat fast how to make the diffs fast is there  
**Translation:** 

**[3287.56s] English:** something that just jumps to mind yeah i mean so we can go over a lot of the strategies that we use  
**Translation:** 

**[3291.74s] English:** one interesting thing is cash warming um  
**Translation:** 

**[3294.70s] English:** and  
**Translation:** 

**[3294.96s] English:** so what you can do is if as the user is typing you can have you know you're probably going to use  
**Translation:** 

**[3302.88s] English:** uh some piece of context and you can know that before the user's done typing so you know as we  
**Translation:** 

**[3309.10s] English:** discussed before reusing the kv cache results in lower latency lower costs uh cross requests  
**Translation:** Vocabulary: cache: 缓存; latency: 延迟; reusing: 重复使用

**[3315.42s] English:** so as the user starts typing you can immediately warm the cache with like let's say the current  
**Translation:** 

**[3319.80s] English:** file contents and then when they press enter uh there's very few  
**Translation:** 

**[3324.96s] English:** tokens it actually has to pre-fill and compute before starting the generation this will  
**Translation:** 

**[3329.00s] English:** significantly lower ttfd can you explain how kv cache works yeah so the way transformers work  
**Translation:** 

**[3335.86s] English:** i like it i mean like one of the mechanisms that allow transformers to not just independently  
**Translation:** 

**[3344.86s] English:** like the mechanism that allows transformers to not just independently look at each token but see  
**Translation:** Vocabulary: independently: 独立地; token: 标记

**[3348.86s] English:** previous tokens are the keys and values to attention and generally the way attention works is  
**Translation:** 

**[3354.84s] English:** you have at your current token, some query, and then you've all the keys.  
**Translation:** 

**[3360.00s] English:** values of all your previous tokens, which are some kind of representation that the model stores  
**Translation:** 

**[3364.70s] English:** internally of all the previous tokens in the prompt. And like by default, when you're doing  
**Translation:** Vocabulary: internally: 内部地

**[3372.14s] English:** a chat, the model has to, for every single token, do this forward pass through the entire model.  
**Translation:** 

**[3379.22s] English:** That's a lot of matrix multiplies that happen, and that is really, really slow. Instead, if you  
**Translation:** Vocabulary: matrix: 矩阵; multiplies: 乘法

**[3385.06s] English:** have already done that, and you stored the keys and values, and you keep that in the GPU,  
**Translation:** 

**[3390.40s] English:** then when I'm, let's say I have to sort it for the last n tokens, if I now want to compute the  
**Translation:** 

**[3395.78s] English:** output token for the n plus one token, I don't need to pass those first n tokens through the  
**Translation:** 

**[3402.40s] English:** entire model, because I already have all those keys and values. And so you just need to do the  
**Translation:** 

**[3407.66s] English:** forward pass through that last token. And then when you're doing attention, you're reusing those  
**Translation:** 

**[3413.48s] English:** keys and values that have been computed, which is the only kind of sequential part, or sequentially  
**Translation:** Vocabulary: computed: 计算出的

**[3418.16s] English:** dependent part of the transformer.  
**Translation:** 

**[3420.00s] English:** Is there like higher level caching, or like caching of the prompts, or that kind of stuff?  
**Translation:** Vocabulary: caching: 缓存

**[3425.62s] English:** I see. Yeah, there's other types of caching you can kind of do. One interesting thing that you can  
**Translation:** 

**[3434.10s] English:** do for CursorTab is you can basically predict ahead as if the user would have accepted the  
**Translation:** 

**[3442.36s] English:** suggestion, and then trigger another request. And so then you've cached, you've done a speculative,  
**Translation:** 

**[3449.20s] English:** it's a mix of speculative, and then you've done a speculative, and then you've done a speculative,  
**Translation:** Vocabulary: cached: 缓存; speculative: 推测性

**[3449.98s] English:** right? Because you're speculating what would happen if they accepted it. And then you have  
**Translation:** 

**[3455.16s] English:** this value that is cached, this suggestion. And then when they press tab, the next one would be  
**Translation:** Vocabulary: speculating: 猜测

**[3460.24s] English:** waiting for them immediately. It's a kind of clever heuristic slash trick that uses a higher  
**Translation:** 

**[3466.32s] English:** level caching and can give the, it feels fast, despite there not actually being any changes in  
**Translation:** Vocabulary: heuristic: 启发式方法

**[3473.48s] English:** the model.  
**Translation:** 

**[3474.16s] English:** And if you can make the KV cache smaller, one of the advantages you get is like, maybe you can  
**Translation:** Vocabulary: cache: 缓存

**[3478.94s] English:** speculate even more.  
**Translation:** 

**[3479.98s] English:** Yeah, I think that's a really good point. I think that's a really good point. I think that's a really good point.  
**Translation:** Vocabulary: speculate: 猜测

**[3480.00s] English:** you can guess here's the 10 things that you know could be useful i like uh like you predict the  
**Translation:** 

**[3486.26s] English:** next 10 and and then like it's possible the user hits the the one of the 10 it's like much higher  
**Translation:** 

**[3491.50s] English:** chance than the user hits like the exact one that you show them uh maybe they type another character  
**Translation:** 

**[3496.18s] English:** in and we sort of hit hit something else in the cache so there's there's all these tricks where  
**Translation:** 

**[3500.64s] English:** um the the general phenomena here is uh i think it's also super useful for rl is you know  
**Translation:** 

**[3509.10s] English:** maybe a single sample from the model isn't very good but if you predict like 10 different things  
**Translation:** 

**[3516.94s] English:** uh turns out that one of the 10 uh that's right is the probability is much higher there's these  
**Translation:** 

**[3523.00s] English:** passive key curves and you know part of rl like what rl does is you know you can you can exploit  
**Translation:** 

**[3529.72s] English:** this passive k phenomena to to make many different predictions and and uh what one way to think about  
**Translation:** 

**[3537.04s] English:** this the model sort of knows internally has like  
**Translation:** Vocabulary: internally: 内部

**[3539.08s] English:** has some uncertainty over like which of the k things is correct or like which of the k things  
**Translation:** 

**[3543.96s] English:** does the human want so when we rl our uh you know cursor tab model one of the things we're doing is  
**Translation:** 

**[3551.44s] English:** we're predicting which like which of the hundred different suggestions the model produces is more  
**Translation:** 

**[3559.46s] English:** amenable for humans like which of them do humans more like than other things uh maybe maybe like  
**Translation:** Vocabulary: amenable: 易于接受

**[3564.52s] English:** there's something where the model can predict very far ahead versus like a little bit and  
**Translation:** 

**[3569.08s] English:** maybe somewhere in the middle and and you know just and then you can give a reward to the things  
**Translation:** 

**[3574.24s] English:** that humans would like more and and sort of punish the things that it would like and sort of then  
**Translation:** 

**[3578.38s] English:** train the model to output the suggestions that humans would like more you have these like rl  
**Translation:** 

**[3582.06s] English:** loops that are very useful that exploit these passive k curves um oman maybe can can go into  
**Translation:** 

**[3587.44s] English:** even more detail yeah it's a little it is a little different than speed um but i mean like  
**Translation:** 

**[3594.38s] English:** technically you tie it back in because you can get away with the smaller model if you rl your  
**Translation:** 

**[3598.18s] English:** smaller model and get to the bottom of it and then you can get to the bottom of it and then you can  
**Translation:** 

**[3599.08s] English:** get to the bottom of it and then you can get to the same performances  
**Translation:** 

**[3600.00s] English:** the bigger one um that's like and while i was mentioning stuff about kb about reducing the  
**Translation:** 

**[3607.98s] English:** size of your kb cache there are other techniques there as well that are really helpful for speed  
**Translation:** 

**[3611.12s] English:** um so kind of back in the day like all the way two years ago uh people mainly use multi-head  
**Translation:** Vocabulary: cache: 缓存

**[3618.72s] English:** attention um and i think there's been a migration towards more efficient attention schemes like  
**Translation:** 

**[3624.60s] English:** group query um or multi-query attention and this is really helpful for then uh with larger batch  
**Translation:** 

**[3632.72s] English:** sizes being able to generate the tokens much faster the interesting thing here is um this  
**Translation:** 

**[3639.84s] English:** now has no effect on that uh time to first token pre-fill speed uh the thing this matters for is  
**Translation:** Vocabulary: token: 令牌

**[3646.54s] English:** uh now generating tokens and and why is that because when you're generating tokens instead of  
**Translation:** 

**[3652.54s] English:** uh being bottlenecked  
**Translation:** Vocabulary: bottlenecked: 瓶颈外化

**[3654.60s] English:** by doing these super paralyzable matrix multiplies across all your tokens you're bottlenecked by how  
**Translation:** 

**[3659.90s] English:** quickly it's for long context um with large batch sizes by how quickly you can read those cache keys  
**Translation:** Vocabulary: matrix: 矩阵

**[3666.30s] English:** and values um and so then how that's memory bandwidth and how can we make this faster  
**Translation:** 

**[3671.88s] English:** we can try to compress the size of these keys and values so multi-query attention is the most  
**Translation:** Vocabulary: bandwidth: 带宽; compress: 压缩

**[3677.00s] English:** aggressive of these um where normally with multi-head attention you have some number of  
**Translation:** 

**[3682.12s] English:** quote-unquote attention heads  
**Translation:** 

**[3684.60s] English:** um and some number of kind of query query heads multi-query just preserves the query heads gets  
**Translation:** 

**[3692.44s] English:** rid of all the key value heads so there's only one kind of key value head and there's all the  
**Translation:** Vocabulary: preserves: 保留

**[3698.92s] English:** remaining uh query heads with group query um you instead you know preserve all the query heads and  
**Translation:** 

**[3707.56s] English:** then your keys and values are kind of there are fewer heads for the keys and values but you're not  
**Translation:** 

**[3714.60s] English:** it's just one um but anyways like the whole point here is you're just reducing the size of your kv cache  
**Translation:** 

**[3720.00s] English:** And then there is MLA.  
**Translation:** 

**[3722.50s] English:** Yeah, multi-latent.  
**Translation:** 

**[3723.82s] English:** That's a little more complicated.  
**Translation:** 

**[3726.20s] English:** And the way that this works is it kind of turns the entirety of your keys and values across all your heads into this kind of one latent vector that is then kind of expanded inference time.  
**Translation:** 

**[3739.90s] English:** But MLA is from this company called DeepSeq.  
**Translation:** Vocabulary: entirety: 全部; inference: 推断

**[3743.76s] English:** It's quite an interesting algorithm.  
**Translation:** 

**[3745.32s] English:** Maybe the key idea is sort of in both MQA and in other places, what you're doing is you're sort of reducing the number of KV heads.  
**Translation:** Vocabulary: algorithm: 算法

**[3758.76s] English:** The advantage you get from that is there's less of them.  
**Translation:** 

**[3763.72s] English:** But maybe the theory is that you actually want a lot of different, like you want each of the keys and values to actually be different.  
**Translation:** 

**[3772.62s] English:** So one way to reduce the size is you.  
**Translation:** 

**[3775.32s] English:** You keep one big shared vector for all the keys and values.  
**Translation:** 

**[3781.36s] English:** And then you have smaller vectors for every single token so that you can store only the smaller thing as some sort of like low-rank reduction.  
**Translation:** 

**[3790.16s] English:** And the low-rank reduction, at the end of the time, when you eventually want to compute the final thing, remember that like your memory bound, which means that like you still have some compute left that you can use for these things.  
**Translation:** Vocabulary: token: 标记

**[3801.30s] English:** And so if you can expand the latent.  
**Translation:** 

**[3805.32s] English:** Vector back out and somehow like this is far more efficient because just like you're reducing, like, for example, maybe like reducing like 32 or something like the size of the vector that you're keeping.  
**Translation:** 

**[3817.86s] English:** Yeah, there's perhaps some richness in having a separate set of keys and values and query that kind of pairwise match up versus compressing that all into one.  
**Translation:** 

**[3829.20s] English:** And that interaction, at least.  
**Translation:** Vocabulary: compressing: 压缩; pairwise: 一一对应

**[3831.24s] English:** OK, all of that is dealing with being memory bound.  
**Translation:** 

**[3835.32s] English:** Yeah.  
**Translation:** 

**[3836.20s] English:** And what I mean, ultimately, how does that map to the.  
**Translation:** 

**[3840.00s] English:** user experience trying to get the yeah the two things that it maps to is you can now make your  
**Translation:** 

**[3844.86s] English:** cache a lot larger because you've less space allocated for the kv cache you can maybe cache  
**Translation:** 

**[3850.26s] English:** a lot more aggressively and a lot more things so you get more cache hits which are helpful for  
**Translation:** Vocabulary: aggressively: 激进地; allocated: 分配; cache: 缓存

**[3854.94s] English:** reducing the time to first token for the reasons that were kind of described earlier and then the  
**Translation:** 

**[3859.86s] English:** second being when you start doing inference with more and more requests and larger and larger batch  
**Translation:** 

**[3865.08s] English:** sizes you don't see much of a slowdown in as it's generating the tokens the speed of that  
**Translation:** 

**[3871.36s] English:** what it also allows you to make your prompt bigger for certain yeah yeah so like the basic the size  
**Translation:** Vocabulary: slowdown: 减速

**[3877.12s] English:** of your kv cache is uh both the size of all your prompts multiplied by the number of prompts being  
**Translation:** 

**[3882.60s] English:** processed in parallel so you could increase either those dimensions right the batch size  
**Translation:** Vocabulary: dimensions: 维度; multiplied: 乘以; processed: 处理

**[3886.52s] English:** or the size of your prompts without degrading the latency of generating tokens arvid you wrote a  
**Translation:** 

**[3892.72s] English:** blog post shadow of a workspace yeah iterating  
**Translation:** Vocabulary: degrading: 性能下降; latency: 延迟; workspace: 工作空间

**[3895.06s] English:** on code in the background yeah so what's going on uh so to be clear we want there to be a lot of  
**Translation:** 

**[3901.72s] English:** stuff stuff happening in the background and we're experimenting with a lot of things uh right now  
**Translation:** 

**[3906.32s] English:** uh we don't have much of that happening other than like the the cache warming or like you know  
**Translation:** 

**[3912.20s] English:** figuring out the right context that goes into your command key prompts for example  
**Translation:** 

**[3915.76s] English:** but the idea is if you can actually spend computation in the background then you can help  
**Translation:** 

**[3921.58s] English:** um help the user maybe  
**Translation:** Vocabulary: computation: 计算

**[3925.04s] English:** like at a slightly longer time horizon than just predicting the next few lines that you're going to  
**Translation:** 

**[3930.42s] English:** make but actually like in the next 10 minutes what are you going to make and by doing it in  
**Translation:** 

**[3935.18s] English:** background you can spend more computation doing that and so the idea of the shadow workspace that  
**Translation:** 

**[3941.78s] English:** that we implemented and we use it internally for like experiments um is that to actually get  
**Translation:** Vocabulary: internally: 内部使用

**[3948.66s] English:** advantage of doing stuff in the background you want some kind of feedback signal to give back  
**Translation:** 

**[3954.20s] English:** to the model because i don't know if you've ever done that but i don't know if you've ever done that  
**Translation:** 

**[3955.04s] English:** because otherwise like you can get higher performance by just letting the model think for  
**Translation:** 

**[3959.46s] English:** longer  
**Translation:** 

**[3960.00s] English:** And so like O1 is a good example of that.  
**Translation:** 

**[3963.00s] English:** But another way you can improve performance  
**Translation:** 

**[3964.78s] English:** is by letting the model iterate and get feedback.  
**Translation:** 

**[3968.04s] English:** And so one very important piece of feedback  
**Translation:** 

**[3971.18s] English:** when you're a programmer is the language server,  
**Translation:** 

**[3974.98s] English:** which is this thing, it exists for most different languages  
**Translation:** Vocabulary: programmer: 程序员

**[3980.06s] English:** and there's like a separate language server per language.  
**Translation:** 

**[3982.64s] English:** And it can tell you, you know,  
**Translation:** 

**[3984.66s] English:** you're using the wrong type here  
**Translation:** 

**[3986.12s] English:** and then it gives you an error,  
**Translation:** 

**[3987.32s] English:** or it can allow you to go to definition  
**Translation:** 

**[3989.42s] English:** and sort of understands the structure of your code.  
**Translation:** 

**[3991.90s] English:** So language servers are extensions developed by,  
**Translation:** 

**[3994.94s] English:** like there's a TypeScript language server  
**Translation:** Vocabulary: extensions: 扩展

**[3996.46s] English:** developed by the TypeScript people,  
**Translation:** 

**[3998.16s] English:** a Rust language server developed by the Rust people,  
**Translation:** 

**[4000.10s] English:** and then they all interface  
**Translation:** 

**[4001.48s] English:** over the language server protocol to VS Code.  
**Translation:** Vocabulary: interface: 接口

**[4003.50s] English:** So that VS Code doesn't need to have  
**Translation:** 

**[4005.14s] English:** all of the different languages built into VS Code,  
**Translation:** 

**[4007.48s] English:** but rather you can use  
**Translation:** 

**[4009.00s] English:** the existing compiler infrastructure.  
**Translation:** 

**[4010.88s] English:** For linting purposes, what-  
**Translation:** 

**[4012.88s] English:** It's for linting, it's for going to definition  
**Translation:** 

**[4015.98s] English:** and for like seeing the right types that you're using.  
**Translation:** 

**[4019.42s] English:** So it's doing like type checking also?  
**Translation:** 

**[4021.40s] English:** Yes, type checking and going to references.  
**Translation:** 

**[4025.06s] English:** And that's like, when you're working in a big project,  
**Translation:** 

**[4027.04s] English:** you kind of need that.  
**Translation:** 

**[4028.46s] English:** If you don't have that,  
**Translation:** 

**[4029.62s] English:** it's like really hard to code in a big project.  
**Translation:** 

**[4032.74s] English:** Can you say again how that's being used inside Cursor,  
**Translation:** 

**[4036.30s] English:** the language server protocol communication thing?  
**Translation:** 

**[4040.46s] English:** So it's being used in Cursor to show to the programmer,  
**Translation:** 

**[4042.54s] English:** just like in VS Code.  
**Translation:** 

**[4043.66s] English:** But then the idea is you want to show that same information  
**Translation:** 

**[4046.86s] English:** to the models, the IAM models.  
**Translation:** 

**[4049.42s] English:** And you want to do that in a way  
**Translation:** 

**[4051.84s] English:** that doesn't affect the user  
**Translation:** 

**[4053.38s] English:** because you want to do it in background.  
**Translation:** 

**[4054.82s] English:** And so the idea behind the Shadow Workspace was,  
**Translation:** 

**[4058.00s] English:** okay, like one way we can do this is  
**Translation:** Vocabulary: workspace: 工作空间

**[4061.70s] English:** we spawn a separate window of Cursor that's hidden.  
**Translation:** 

**[4066.52s] English:** And so you can set this flag and electron is hidden.  
**Translation:** Vocabulary: spawn: 孵化

**[4068.92s] English:** There is a window, but you don't actually see it.  
**Translation:** 

**[4070.74s] English:** And inside of this window,  
**Translation:** 

**[4072.68s] English:** the AI agents can modify code however they want,  
**Translation:** 

**[4076.00s] English:** as long as they don't save it  
**Translation:** 

**[4077.10s] English:** because it's still the same folder.  
**Translation:** 

**[4079.42s] English:** And then,  
**Translation:** 

**[4080.00s] English:** get feedback from from the linters and go to definition and iterate on their code so like  
**Translation:** 

**[4084.32s] English:** literally run everything in the background like as if right yeah maybe even run the code so that's  
**Translation:** Vocabulary: linters: 代码检查工具

**[4091.32s] English:** the eventual version okay that's what you want and a lot of the blog post is actually about  
**Translation:** 

**[4095.84s] English:** how do you make that happen because it's a little bit tricky you want it to be on the user's machine  
**Translation:** Vocabulary: eventual: 最终的

**[4102.18s] English:** so that it exactly mirrors the user's environment and then on linux you can do this cool thing  
**Translation:** 

**[4108.72s] English:** where you can actually mirror the file system and have the ai make changes to the files and  
**Translation:** 

**[4115.52s] English:** it thinks that it's operating on the file level but actually that's stored in in memory and you  
**Translation:** 

**[4123.34s] English:** you can create this kernel extension to make it work whereas on mac and windows it's a little bit  
**Translation:** Vocabulary: kernel: 内核

**[4130.76s] English:** more difficult uh and and uh but it's it's a fun technical problem so that's why one one may be  
**Translation:** 

**[4137.88s] English:** hacky but interesting  
**Translation:** 

**[4138.72s] English:** idea that i like is holding a lock on saving and so basically you can then have the language model  
**Translation:** 

**[4144.62s] English:** kind of hold the lock on on saving to disk and then instead of you operating in the ground truth  
**Translation:** 

**[4149.80s] English:** version of the files uh that are safe to disk you you actually are operating what was the shadow  
**Translation:** 

**[4153.98s] English:** workspace before and these unsaved things that only exist in memory that you still get linter  
**Translation:** Vocabulary: linter: 代码检查工具; unsaved: 未保存的

**[4157.34s] English:** errors for and you can code in and then when you try to maybe run code it's just like there's a  
**Translation:** 

**[4162.26s] English:** small warning that there's a lock and then you kind of will take back the lock from the language  
**Translation:** 

**[4166.72s] English:** server if you're trying to do things concurrently or for example if you're trying to do things concurrently  
**Translation:** 

**[4168.72s] English:** from the shadow workspace if you're trying to do things concurrently that's such an exciting future  
**Translation:** Vocabulary: concurrently: 同时进行

**[4172.88s] English:** by the way it's a bit of a tangent but like to allow a model to change files it's scary for  
**Translation:** 

**[4179.08s] English:** people but like it's really cool to be able to just like let the agent do a set of tasks and you  
**Translation:** Vocabulary: tangent: 旁枝话题

**[4186.20s] English:** come back the next day and kind of observe like it's a colleague or something like that yeah and  
**Translation:** 

**[4192.54s] English:** i think there may be different versions of like run ability where for the simple things where  
**Translation:** 

**[4197.82s] English:** you're doing things concurrently and you're doing things concurrently and you're doing things concurrently  
**Translation:** 

**[4198.72s] English:** in the span of a few minutes  
**Translation:** 

**[4200.00s] English:** behalf of the user as they're programming, it makes sense to make something work locally in  
**Translation:** 

**[4204.80s] English:** their machine. I think for the more aggressive things where you're making larger changes that  
**Translation:** 

**[4208.64s] English:** take longer periods of time, you'll probably want to do this in some sandbox remote environment.  
**Translation:** 

**[4213.52s] English:** And that's another incredibly tricky problem of how do you exactly reproduce or mostly reproduce  
**Translation:** Vocabulary: sandbox: 测试环境

**[4220.00s] English:** to the point of it being effectively equivalent for running code, the user's environment with  
**Translation:** 

**[4225.04s] English:** this remote sandbox. I'm curious what kind of agency you want for coding. Do you want them  
**Translation:** 

**[4232.08s] English:** to find bugs? Do you want them to implement new features? What agency do you want?  
**Translation:** 

**[4236.64s] English:** So by the way, when I think about agents, I don't think just about coding. I think so for  
**Translation:** 

**[4242.32s] English:** the practices, this particular podcast is video editing. And a lot of if you look in Adobe,  
**Translation:** 

**[4247.84s] English:** a lot of this code behind, it's very poorly documented code. But you can interact with  
**Translation:** 

**[4253.76s] English:** Premiere, for example.  
**Translation:** 

**[4255.04s] English:** Using code and basically all the uploading, everything I do on YouTube,  
**Translation:** Vocabulary: uploading: 上传

**[4259.52s] English:** everything as you could probably imagine, I do all of that through code and including  
**Translation:** 

**[4264.24s] English:** translation and overdubbing all of this. So I envision all of those kinds of tasks,  
**Translation:** Vocabulary: envision: 想象; overdubbing: 配音

**[4270.00s] English:** so automating many of the tasks that don't have to do directly with the editing.  
**Translation:** 

**[4274.00s] English:** So that, okay. That's what I was thinking about. But in terms of  
**Translation:** Vocabulary: automating: 自动化

**[4278.08s] English:** coding, I would be fundamentally thinking about bug finding.  
**Translation:** 

**[4285.04s] English:** Like many levels of kind of bug finding and also bug finding, like logical bugs,  
**Translation:** Vocabulary: fundamentally: 从根本上

**[4290.08s] English:** not logical, like spiritual bugs or something.  
**Translation:** 

**[4294.16s] English:** One's like sort of big directions of implementation, that kind of stuff.  
**Translation:** Vocabulary: implementation: 实施方案

**[4298.48s] English:** Logical finding and bug finding.  
**Translation:** 

**[4300.00s] English:** Yeah. I mean, it's really interesting that these models are so bad at bug finding when  
**Translation:** 

**[4306.56s] English:** just naively prompted to find a bug. They're incredibly poorly calibrated.  
**Translation:** 

**[4311.20s] English:** Even the smartest models.  
**Translation:** Vocabulary: calibrated: 校准; naively: 天真地; prompted: 提示

**[4312.72s] English:** Exactly. Even O1.  
**Translation:** 

**[4313.52s] English:** Even O1.  
**Translation:** 

**[4314.00s] English:** Exactly. Even O1.  
**Translation:** 

**[4314.48s] English:** Exactly. Even O1.  
**Translation:** 

**[4314.72s] English:** How do you explain that? Is there a good intuition?  
**Translation:** 

**[4317.52s] English:** I think these models are  
**Translation:** Vocabulary: intuition: 直觉

**[4319.84s] English:** .  
**Translation:** 

**[4320.00s] English:** really strong reflection of the pre-training distribution and you know i do think they  
**Translation:** 

**[4326.06s] English:** they generalize as the loss gets lower and lower but i don't think the the loss and the scale is  
**Translation:** 

**[4330.98s] English:** quite or the loss is low enough such that they're like really fully generalizing in code like the  
**Translation:** Vocabulary: generalize: 泛化

**[4336.54s] English:** things that we use these things for uh the frontier models that that they're quite good at  
**Translation:** 

**[4341.28s] English:** are really code generation and question answering and these things exist in massive quantities and  
**Translation:** Vocabulary: frontier: 前沿技术

**[4348.52s] English:** pre-training with all the code on github on the scale of many many trillions of tokens  
**Translation:** 

**[4352.54s] English:** and questions and answers on things like stack overflow and maybe github issues and so when you  
**Translation:** Vocabulary: overflow: 溢出; trillions: 万亿

**[4360.80s] English:** try to push into these things that really don't exist uh very much online like for example the  
**Translation:** 

**[4367.80s] English:** cursor tap objective of predicting the next edit given the edits done so far uh the brittleness  
**Translation:** Vocabulary: brittleness: 脆弱性

**[4372.66s] English:** kind of shows and then bug detection is another great example where there aren't really that many  
**Translation:** 

**[4377.44s] English:** examples of like  
**Translation:** Vocabulary: detection: 检测

**[4378.32s] English:** you know  
**Translation:** 

**[4378.50s] English:** actually detecting real bugs and then proposing fixes um and the models just kind of like really  
**Translation:** Vocabulary: detecting: 检测外泄

**[4384.66s] English:** struggle at it but i think it's a question of transferring the model like in the same way that  
**Translation:** 

**[4389.34s] English:** you get this fantastic transfer um from pre-trained models uh just on code in general to the cursor  
**Translation:** Vocabulary: transferring: 模型迁移

**[4395.54s] English:** tab objective uh you'll see a very very similar thing with generalized models that are really  
**Translation:** 

**[4400.96s] English:** good at code to bug detection it just takes like a little bit of kind of nudging in that direction  
**Translation:** Vocabulary: generalized: 泛化的; nudging: 引导

**[4404.96s] English:** like to be clear i think they sort of understand code really well like  
**Translation:** 

**[4408.30s] English:** while they're being pre-trained like the representation that's being built up like  
**Translation:** 

**[4413.50s] English:** almost certainly like you know somewhere in the stream there's the model knows that maybe there's  
**Translation:** 

**[4420.06s] English:** there's some sketch something sketchy going on right it sort of has some sketchiness but  
**Translation:** Vocabulary: sketchiness: 草率性; sketchy: 可疑的

**[4424.06s] English:** actually eliciting the sketchiness to uh like actually like part part of it is that humans are  
**Translation:** 

**[4431.90s] English:** really calibrated on which bugs are really important it's not just actually it's not just  
**Translation:** Vocabulary: calibrated: 校准; eliciting: 激发

**[4436.40s] English:** actually saying like there's something sketchy it's not just like dead and i don't know it's or  
**Translation:** 

**[4437.06s] English:** something sketchy or something like that like and even beyond that no Frage if it's something it's  
**Translation:** 

**[4438.06s] English:** It's like, it's just, it's just a sketchy.  
**Translation:** 

**[4440.00s] English:** trivial it's the sketchy like you're going to take the server down it's like like part of it  
**Translation:** 

**[4444.38s] English:** is maybe the cultural knowledge of uh like why is the staff engineer staff engineer a staff  
**Translation:** 

**[4449.64s] English:** engineer is is good because they know that three years ago like someone wrote a really you know  
**Translation:** 

**[4455.04s] English:** sketchy piece of code that took took the server down and as opposed to like as opposed to maybe  
**Translation:** 

**[4460.96s] English:** it's like you know you just this thing is like an experiment so like a few bugs are fine like  
**Translation:** 

**[4467.64s] English:** you're just trying to experiment and get the feel of the thing and so if the model gets really  
**Translation:** 

**[4471.52s] English:** annoying when you're writing an experiment that's really bad but if you're writing something for  
**Translation:** 

**[4475.72s] English:** super production you're like writing a database right you're writing code in postgres or linux  
**Translation:** 

**[4480.22s] English:** or whatever like your linus torvalds your yours it's sort of unacceptable to have even in edge  
**Translation:** Vocabulary: torvalds: 托瓦尔; unacceptable: 不可接受

**[4484.82s] English:** case and just just having the calibration of like how paranoid is the user like but even then like  
**Translation:** 

**[4492.72s] English:** if you're putting in a maximum paranoia it still just like doesn't quite get it  
**Translation:** Vocabulary: calibration: 校准; paranoia: 妄想; paranoid: 多疑

**[4497.64s] English:** yeah yeah yeah i mean but this is hard for humans too to understand what which line of code is  
**Translation:** 

**[4503.76s] English:** important which is not like you i think one of your principles on a website says if if a code  
**Translation:** 

**[4509.40s] English:** can do a lot of damage one should add a comment that say this this this line of code is is  
**Translation:** 

**[4515.72s] English:** dangerous and all caps 10 times no you say like for every single line of code inside the function  
**Translation:** 

**[4525.48s] English:** you have to add and that's quite profound  
**Translation:** 

**[4527.64s] English:** that says something about human beings because the the engineers move on even the same person  
**Translation:** Vocabulary: profound: 深奥的

**[4534.40s] English:** might just forget how it can sync the titanic a single function like you don't you might not  
**Translation:** 

**[4539.70s] English:** intuit that quite clearly by looking at the single piece of code yeah and i think that that one is  
**Translation:** Vocabulary: intuit: 直观理解; titanic: 泰坦尼克号

**[4544.28s] English:** also uh partially also for today's ai models where uh if you actually write dangerous dangerous  
**Translation:** 

**[4551.30s] English:** dangerous in every single line like and the models will pay more attention to that  
**Translation:** 

**[4557.64s] English:** and will be more likely to find bugs in that  
**Translation:** 

**[4560.00s] English:** that's actually just straight up a really good practice of labeling code of how much  
**Translation:** Vocabulary: labeling: 标签化

**[4566.42s] English:** damage this can do yeah i mean it's controversial like some people think it's ugly uh well i actually  
**Translation:** 

**[4573.50s] English:** think it's like in fact i actually think this is one of the things i learned from arvid is you know  
**Translation:** Vocabulary: arvid: 例子

**[4578.02s] English:** like i sort of aesthetically i don't like it but i think there's certainly something where like  
**Translation:** 

**[4584.66s] English:** it's useful for the models and in humans just forget a lot and it's really easy to make a  
**Translation:** Vocabulary: aesthetically: 审美上

**[4589.84s] English:** small mistake and cause like bring down you know like just bring down the server and like you like  
**Translation:** 

**[4596.32s] English:** of course we like test a lot and whatever but there's always these things that you have to  
**Translation:** 

**[4601.98s] English:** be very careful yeah like with just normal doc strings i think people will often just skim it  
**Translation:** 

**[4605.96s] English:** when making a change and think oh this i know how to do this um and you kind of really need to point  
**Translation:** 

**[4612.66s] English:** it out to them so that that doesn't slip through yeah you have to be reminded that you can do a lot  
**Translation:** 

**[4617.70s] English:** of damage  
**Translation:** 

**[4618.22s] English:** that's  
**Translation:** 

**[4619.82s] English:** like we don't really think about that like yeah you think about okay how do i figure out how this  
**Translation:** 

**[4624.62s] English:** works so i can improve it you don't think about the other direction until until we have formal  
**Translation:** 

**[4630.86s] English:** verification for everything then you can do whatever you want and you you know for certain  
**Translation:** Vocabulary: verification: 验证

**[4636.38s] English:** that you have not introduced a bug if the proof pass but concretely what do you think that future  
**Translation:** 

**[4640.46s] English:** would look like i think uh people will just not write tests anymore and um the model will suggest  
**Translation:** Vocabulary: concretely: 具体地

**[4649.82s] English:** like you write a function the model will suggest a spec and you review the spec and in the meantime  
**Translation:** 

**[4656.78s] English:** smart reasoning model computes a proof that the implementation follows this spec  
**Translation:** Vocabulary: computes: 计算; implementation: 实现; meantime: meantime

**[4661.34s] English:** um and i think that happens for for most functions yeah do you think this gets at a little bit some  
**Translation:** 

**[4666.38s] English:** of the stuff you were talking about earlier with the difficulty of specifying intent for what you  
**Translation:** Vocabulary: specifying: 说明意图

**[4669.58s] English:** want with software um where sometimes it might be because the intent is really hard to specify it's  
**Translation:** 

**[4674.86s] English:** also then going to be really hard to prove that it's actually matching whatever your intent is  
**Translation:** 

**[4678.30s] English:** like you think that spec is hard because it's really hard to specify what your intent is well  
**Translation:** 

**[4679.66s] English:** hard  
**Translation:** 

**[4680.00s] English:** to generate yeah or just like for a given spec maybe you can i think there is a question of like  
**Translation:** 

**[4688.90s] English:** can you actually do the formal verification like that's like is that possible i think that there's  
**Translation:** 

**[4693.44s] English:** like more to dig into there but then also even if you have the spec if you have the spec how do  
**Translation:** 

**[4698.40s] English:** you have the spec is the spec written in natural language yeah how do you map the spec spec would  
**Translation:** 

**[4703.42s] English:** be formal but how easy would that be so then i think that you care about things that are not  
**Translation:** 

**[4708.44s] English:** going to be easily well specified in the spec language i see i see yeah yeah maybe uh an  
**Translation:** Vocabulary: specified: 规定

**[4713.60s] English:** argument against formal verification is all you need yeah the worry is there's this massive  
**Translation:** 

**[4717.98s] English:** replacing replacing something like unit tests sure yeah yeah um i think you can probably also  
**Translation:** 

**[4724.40s] English:** evolve the the spec languages to capture some of the things that they don't really capture right  
**Translation:** 

**[4730.82s] English:** now um but i don't know i think it's very exciting and you're speaking not just about  
**Translation:** 

**[4736.52s] English:** like single functions you're speaking  
**Translation:** 

**[4738.42s] English:** about entire code bases i think entire code basis is harder but that that is what i would love to  
**Translation:** 

**[4743.66s] English:** have and i think it should be possible and because you can even there there's like a lot of work  
**Translation:** 

**[4748.70s] English:** recently where uh you can prove formally verified down to the hardware so like through the you  
**Translation:** Vocabulary: verified: 验证通过

**[4755.38s] English:** formally verify the c code and then you formally verify through the gcc compiler and then through  
**Translation:** 

**[4760.54s] English:** the variolog down to the hardware um and that's like incredibly big system but it actually works  
**Translation:** Vocabulary: variolog: 验证工具; verify: 验证

**[4766.68s] English:** and i think big code bases are sort of similar in that they're like multi-layered system and  
**Translation:** 

**[4771.28s] English:** um if you can decompose it and formally verify each part then i think it should be possible i  
**Translation:** Vocabulary: decompose: 分解

**[4776.64s] English:** think the specification problem is a real problem but how do you handle side effects or how do you  
**Translation:** 

**[4781.72s] English:** handle i guess external dependencies like calling the stripe api maybe stripe would write a spec for  
**Translation:** Vocabulary: specification: 规范

**[4788.46s] English:** but like you can't do this for everything like can you do this for everything you use like how do you  
**Translation:** 

**[4793.34s] English:** how do you do it for if there's a language model like maybe maybe like people will use  
**Translation:** 

**[4796.66s] English:** language models as primitives in the programs they write and there's like a  
**Translation:** 

**[4800.00s] English:** dependence on it and like how how do you now include that i think you might be able to prove  
**Translation:** Vocabulary: primitives: 基本元素

**[4804.10s] English:** prove that still prove what about language models i think if it feels possible that you could  
**Translation:** 

**[4809.76s] English:** actually prove that a language model is aligned for example or like you can prove that it actually  
**Translation:** Vocabulary: aligned: 对齐

**[4816.44s] English:** gives the the right answer um that's the dream yeah that is i mean that's yeah if it's possible  
**Translation:** 

**[4823.50s] English:** that's your i have a dream speech if it's possible that will certainly help with you know uh  
**Translation:** 

**[4829.98s] English:** making sure your code doesn't have bugs and making sure ai doesn't destroy all human  
**Translation:** 

**[4834.42s] English:** civilization so the the full spectrum of ai safety to just bug finding uh what so you said  
**Translation:** 

**[4840.82s] English:** the models struggle with bug finding what's the hope you know my hope initially is and and i can  
**Translation:** 

**[4847.02s] English:** let michael michael chime in too but it was like this um it should you know first help with the  
**Translation:** Vocabulary: chime: 插话

**[4853.58s] English:** stupid bugs like it should very quickly catch the stupid bugs like off by one editors like  
**Translation:** 

**[4858.56s] English:** sometimes you write something in a  
**Translation:** 

**[4859.98s] English:** comment and do the other way it's like very common like i do this i write like less than  
**Translation:** 

**[4864.42s] English:** in a comment and like i maybe write the greater than something like that and the model is like  
**Translation:** 

**[4869.04s] English:** yeah you look sketchy like dude you sure you want to do that uh but eventually it should be able to  
**Translation:** 

**[4874.20s] English:** catch harder bugs too yeah and i think that it's also important to note that this is having good  
**Translation:** Vocabulary: sketchy: 可疑的

**[4881.08s] English:** bug finding models feels necessary to get to the highest reaches of having ai do more and more  
**Translation:** 

**[4886.74s] English:** programming for you where you're going to you know if the ai is  
**Translation:** 

**[4889.98s] English:** building more and more of the system for you you need to not just generate but also verify  
**Translation:** 

**[4892.98s] English:** and without that some of the problems that we've talked about before with programming with these  
**Translation:** Vocabulary: verify: 验证

**[4898.24s] English:** models um will just become untenable um so it's not just for humans like you write a bug i write  
**Translation:** 

**[4905.88s] English:** a bug find the bug for me but it's also being able to to verify the ai's code and check it  
**Translation:** 

**[4910.58s] English:** um is really important yeah and then how do you actually do this like we have had a lot of  
**Translation:** 

**[4915.12s] English:** contentious dinner discussions of how do you actually train a bug model but one very popular  
**Translation:** Vocabulary: contentious: 有争议的

**[4919.98s] English:** those are some of the questions we've seen um you had a question on the internet and i'd like to  
**Translation:** 

**[4922.08s] English:** know how to do it uh so i'm gonna go ahead and just share it with you and yeah i'll go ahead and  
**Translation:** 

**[4925.02s] English:** i'll look at it and i'll see if there's any questions i can drop you a link down in the  
**Translation:** 

**[4927.28s] English:** chat later but that's it and that's it so for this video that i wanted to tell you guys about  
**Translation:** 

**[4932.28s] English:** the bug find two bugs so i wanted to talk about my own bug start and i'm gonna wait a minute over  
**Translation:** 

**[4938.88s] English:** here so i'm going to show you my other bug find two bugs and i'll show you guys how to do it and  
**Translation:** 

**[4943.38s] English:** then i'm going to see it and then i'll show you i want you to go ahead and look at the other  
**Translation:** 

**[4944.10s] English:** one and i'll tell you what the bug find two bugs do so the first one is a bug find you want to  
**Translation:** 

**[4920.00s] English:** you know, it's kind of potentially easy to introduce a bug than actually finding the bug.  
**Translation:** 

**[4925.34s] English:** And so you can train a model to introduce bugs in existing code. And then you can train a reverse  
**Translation:** 

**[4932.28s] English:** bug model then that can find bugs using this synthetic data. So that's like one example.  
**Translation:** 

**[4939.36s] English:** But yeah, there are lots of ideas for how to do this.  
**Translation:** 

**[4943.16s] English:** You can also do a bunch of work, not even at the model level, of taking the biggest models,  
**Translation:** 

**[4947.02s] English:** and then maybe giving them access to a lot of information that's not just the code.  
**Translation:** 

**[4952.28s] English:** Like it's kind of a hard problem to like stare at a file and be like, where's the bug?  
**Translation:** 

**[4955.74s] English:** And you know, that's hard for humans often, right? And so often you have to run the code and  
**Translation:** 

**[4959.82s] English:** being able to see things like traces and step through a debugger. There's a whole other  
**Translation:** 

**[4964.10s] English:** direction where it like kind of tends toward that. And it could also be that there are kind  
**Translation:** 

**[4967.26s] English:** of two different product form factors here. It could be that you have a really specialty model  
**Translation:** 

**[4970.58s] English:** that's quite fast, that's kind of running in the background and trying to spot bugs. And it might  
**Translation:** Vocabulary: specialty: 特殊型号

**[4974.12s] English:** be that sometimes, sort of to Arvid's earlier example, it's kind of like, you know, you're  
**Translation:** 

**[4977.02s] English:** about, you know, some nefarious input box bug. It might be that sometimes you want to like,  
**Translation:** Vocabulary: nefarious: 邪恶的

**[4981.02s] English:** there's, you know, there's a bug. You're not just like checking hypothesis free. You're like,  
**Translation:** 

**[4984.40s] English:** this is a problem. I really want to solve it. And you zap that with tons and tons and tons  
**Translation:** Vocabulary: hypothesis: 假设

**[4988.38s] English:** of compute. And you're willing to put in like $50 to solve that bug or something even more.  
**Translation:** 

**[4992.98s] English:** Have you thought about integrating money into this whole thing? Like I would pay probably a  
**Translation:** Vocabulary: integrating: 整合

**[4996.42s] English:** large amount of money for if you found a bug or even generated code that I really appreciated.  
**Translation:** 

**[5001.10s] English:** Like I had a moment a few days ago when I started using cursor where it generated,  
**Translation:** 

**[5007.02s] English:** uh, perfect, uh, like perfect three functions for interacting with the YouTube API to update  
**Translation:** 

**[5016.92s] English:** captions and for localization, like different in different languages. The API documentation  
**Translation:** Vocabulary: captions: 字幕

**[5023.48s] English:** is not very good. And the code across, like if I Googled it for a while, I couldn't find exactly,  
**Translation:** 

**[5029.40s] English:** there's a lot of confusing information and cursor generated perfectly. And I was like,  
**Translation:** 

**[5033.72s] English:** I just sat back, I read the code. I was like, this is correct. I tested,  
**Translation:** 

**[5037.02s] English:** it's correct. I was like, I want a tip.  
**Translation:** 

**[5040.00s] English:** on a button that goes yeah here's five dollars one that's really good just to support the company  
**Translation:** 

**[5045.84s] English:** and support what the interface is and the other is that probably sends a strong signal like good job  
**Translation:** Vocabulary: interface: 用户界面

**[5053.68s] English:** right there's a much stronger signal than just accepting the code right you just actually send  
**Translation:** 

**[5058.08s] English:** like a strong good job that and for bug finding obviously like there's a lot of people  
**Translation:** 

**[5064.32s] English:** you know that would pay a huge amount of money for a bug like a bug bounty thing right is that  
**Translation:** 

**[5072.22s] English:** you guys think about that yeah it's a controversial idea inside the the company i think it sort of  
**Translation:** Vocabulary: bounty: 悬赏

**[5077.86s] English:** depends on how much uh you believe in humanity almost you know like uh i think it would be  
**Translation:** 

**[5085.00s] English:** really cool if like uh you spend nothing to try to find a bug and if it doesn't find a bug you  
**Translation:** 

**[5090.36s] English:** you spend zero dollars and then if it does find a bug uh and you click accept  
**Translation:** 

**[5094.30s] English:** then it also shows like in parentheses like one dollar and so you spend one dollar to accept the  
**Translation:** 

**[5099.44s] English:** bug uh and then of course there's a worry like okay we spent a lot of computation like maybe  
**Translation:** 

**[5103.94s] English:** people will just copy paste um i think that's a worry um and then there is also the worry that  
**Translation:** Vocabulary: computation: 计算

**[5109.80s] English:** like introducing money into the product makes it like kind of you know like it doesn't feel as fun  
**Translation:** 

**[5115.78s] English:** anymore like you have to like think about money and and you all you want to think about is like  
**Translation:** 

**[5120.14s] English:** the code and so maybe it actually makes more sense to separate it out and like you pay some  
**Translation:** 

**[5125.22s] English:** fee like every month and then you get all of these things for free but there could be a tipping  
**Translation:** 

**[5130.16s] English:** component which is not like it yes but it still has that like dollar symbol i think it's fine but  
**Translation:** 

**[5135.60s] English:** i i also see the point where like maybe you don't want to introduce it yeah i was gonna say the  
**Translation:** 

**[5140.68s] English:** moment that feels like people do this is when they share it when they have a fantastic example they  
**Translation:** 

**[5145.24s] English:** just kind of share it with their friend there is also a potential world where there's a technical  
**Translation:** 

**[5148.80s] English:** solution to this like  
**Translation:** 

**[5150.14s] English:** on our system problem too where if we can get to a place where we understand the output of the  
**Translation:** 

**[5154.68s] English:** system more i mean to the stuff we were talking about with like you know error checking with the  
**Translation:** 

**[5158.80s] English:** lsp and then also running  
**Translation:** 

**[5160.00s] English:** the code but if you could get to a place where you could actually somehow verify oh i have fixed the  
**Translation:** 

**[5164.26s] English:** bug maybe then the the bounty system doesn't need to rely on the honor system too how much  
**Translation:** Vocabulary: verify: 验证

**[5169.54s] English:** interaction is there between the terminal and the code like how much information is gained from if  
**Translation:** 

**[5174.48s] English:** you run the code in the terminal like can you use can you do like a a loop where it runs runs the  
**Translation:** 

**[5182.34s] English:** code and suggest how to change the code if the code and runtime gives an error is right now  
**Translation:** 

**[5188.32s] English:** they're separate worlds completely like i know you can like do control k inside the terminal  
**Translation:** Vocabulary: runtime: 运行时

**[5193.56s] English:** to help you write the code you can use terminal context as well uh inside of checkman k kind of  
**Translation:** 

**[5200.22s] English:** everything um we don't have the looping part yet though we suspect something like this could make  
**Translation:** Vocabulary: checkman: 核查曼

**[5206.40s] English:** a lot of sense there's a question of whether it happens in the foreground too or if it happens  
**Translation:** 

**[5210.30s] English:** in the background like what we've been discussing sure the background is pretty cool like we do  
**Translation:** Vocabulary: foreground: 前景

**[5214.76s] English:** running the code in different ways plus there's a database side to this  
**Translation:** 

**[5218.28s] English:** you  
**Translation:** 

**[5218.32s] English:** which how do you protect it from not modifying the database but okay  
**Translation:** 

**[5221.62s] English:** i mean there's there's certainly cool solutions there uh there's this new api that is being  
**Translation:** Vocabulary: modifying: 修改

**[5228.44s] English:** developed for it's it's not an aws uh but you know it's it certainly is i think it's in planet  
**Translation:** 

**[5236.08s] English:** scale i don't know if planet scale was the first one to add it it's this ability sort of add  
**Translation:** 

**[5240.34s] English:** branches to a database uh which is uh like if you're working on a feature and you want to test  
**Translation:** 

**[5246.60s] English:** against the broad database but you don't actually have a database you can't do that  
**Translation:** 

**[5248.32s] English:** you couldn't actually want a document to have a X belle because we send it to you to try to  
**Translation:** 

**[5261.44s] English:** control it but because today's the big thing so if you don't actually want to test against the broad  
**Translation:** 

**[5268.22s] English:** database you could sort of add a branch to the database in the way to do that is to add a branch  
**Translation:** 

**[5272.36s] English:** to the writeahead log and there's obviously a lot of technical complexity in doing it correctly i i  
**Translation:** Vocabulary: complexity: 复杂性; writeahead: 预写日志

**[5273.32s] English:** guess database companies need need need new things to do  
**Translation:** 

**[5278.32s] English:** And so maybe...  
**Translation:** 

**[5280.00s] English:** the the ai agents will use will use branching they'll like test against some branch and it's  
**Translation:** 

**[5286.30s] English:** sort of going to be a requirement for the database to like support branching or something it'd be  
**Translation:** 

**[5290.72s] English:** really interesting if you could branch a file system right yeah i feel like everything needs  
**Translation:** 

**[5294.98s] English:** branching it's like yeah yeah sick that's the problem with the multiverse right  
**Translation:** Vocabulary: multiverse: 多宇宙

**[5299.50s] English:** like if you branch on everything that's like a lot i mean there's there's obviously these like  
**Translation:** 

**[5305.80s] English:** super clever algorithms to make sure that you don't actually sort of use a lot of space or  
**Translation:** 

**[5310.30s] English:** cpu or whatever okay this is a good place to ask about infrastructure so you guys mostly use aws  
**Translation:** 

**[5316.48s] English:** what what are some interesting details what are some interesting challenges  
**Translation:** 

**[5319.24s] English:** why did you choose aws why is why is aws still winning hashtag aws is just really  
**Translation:** 

**[5326.54s] English:** really good it's really good like um whenever you use an aws product you just know that  
**Translation:** 

**[5335.78s] English:** it's going to work like it might be absolute hell to go through the steps to set it up um why is the  
**Translation:** 

**[5342.50s] English:** interface so horrible because it's just so good it doesn't need the nature of winning i think it's  
**Translation:** Vocabulary: interface: 用户界面

**[5349.38s] English:** exactly it's just nature they're winning yeah yeah but aws you can always trust like it will  
**Translation:** 

**[5354.18s] English:** always work and if there is a problem it's probably your problem uh yeah okay is there  
**Translation:** 

**[5361.54s] English:** some interesting like challenges to you guys a pretty new startup to get scaling to like  
**Translation:** 

**[5367.52s] English:** to so many people and yeah i think that they're uh it has been an interesting journey adding you  
**Translation:** 

**[5375.06s] English:** know each extra zero to the request per second you run into all of these with like you know the  
**Translation:** 

**[5379.60s] English:** general components you're using for for caching and databases run into issues as you make things  
**Translation:** Vocabulary: caching: 缓存; databases: 数据库

**[5383.66s] English:** bigger and bigger and now we're at the scale where we get like you know into overflows on our tables  
**Translation:** 

**[5386.82s] English:** and things like that um and then also there have been some custom  
**Translation:** Vocabulary: overflows: 溢出

**[5391.54s] English:** systems that we've built like for instance our retrieval system for  
**Translation:** 

**[5395.62s] English:** computing a semantic index of your code base and answering questions about a code base  
**Translation:** Vocabulary: computing: 计算; retrieval: 检索; semantic: 语义

**[5400.00s] English:** that have continually, I feel like, been one of the trickier things to scale.  
**Translation:** 

**[5404.12s] English:** I have a few friends who are super, super senior engineers.  
**Translation:** Vocabulary: trickier: 更棘手的

**[5407.60s] English:** And one of their sort of lines is like, it's very hard to predict where systems will break  
**Translation:** 

**[5411.46s] English:** when you scale them.  
**Translation:** 

**[5413.44s] English:** You can sort of try to predict in advance, but there's always something weird that's  
**Translation:** 

**[5419.20s] English:** going to happen when you add this extra zero.  
**Translation:** 

**[5421.82s] English:** And you thought you thought through everything, but you didn't actually think through everything.  
**Translation:** 

**[5425.44s] English:** Uh, but I think for that particular system, we've, so for concrete details, the thing  
**Translation:** 

**[5434.90s] English:** we do is obviously we upload, um, when like we chunk up all of your code and then we send  
**Translation:** 

**[5442.38s] English:** up sort of the code for, for embedding and we embed the code and then we store the embeddings  
**Translation:** Vocabulary: embed: 嵌入; embedding: 嵌入; embeddings: 嵌入

**[5447.74s] English:** in a, in a database, but we don't actually store any of the code.  
**Translation:** 

**[5451.50s] English:** And then there's reasons around making sure that we don't introduce.  
**Translation:** 

**[5455.44s] English:** Client bugs, because we're very, very paranoid about client bugs.  
**Translation:** 

**[5458.82s] English:** We store, uh, uh, much of the details on the server, uh, like everything is sort of encrypted.  
**Translation:** Vocabulary: encrypted: 加密; paranoid: 多疑

**[5467.80s] English:** So one, one of the technical challenges is, is always making sure that the local index,  
**Translation:** 

**[5472.76s] English:** the local code base state is the same as the state that is on the server.  
**Translation:** 

**[5477.76s] English:** And, and the way sort of technically we ended up doing that is so for every single file,  
**Translation:** 

**[5483.42s] English:** you can, you can sort of keep this hash.  
**Translation:** 

**[5485.60s] English:** And then for every folder, you can sort of keep a hash, which is the hash of all of its  
**Translation:** 

**[5490.78s] English:** children.  
**Translation:** 

**[5491.06s] English:** And you can sort of recursively do that until the top.  
**Translation:** 

**[5493.80s] English:** And why, why do something, something complicated?  
**Translation:** Vocabulary: recursively: 依次反复

**[5497.24s] English:** Uh, one thing you could do is you could keep a hash for every file.  
**Translation:** 

**[5500.74s] English:** Then every minute you could try to download the hashes that are on the server, figure  
**Translation:** Vocabulary: hashes: 文件摘要

**[5505.00s] English:** out what are the files that don't exist on the server.  
**Translation:** 

**[5507.40s] English:** Maybe you just created a new file.  
**Translation:** 

**[5508.92s] English:** Maybe you just deleted a file.  
**Translation:** 

**[5510.26s] English:** Maybe you checked out a new branch and try to reconcile the state between the client  
**Translation:** Vocabulary: reconcile: 协调一致

**[5515.14s] English:** and the server.  
**Translation:** 

**[5515.42s] English:** But that introduces like absolutely ginormous.  
**Translation:** Vocabulary: ginormous: 巨大无比

**[5520.00s] English:** network overhead both uh both on the client side i mean nobody really wants us to hammer their wi-fi  
**Translation:** 

**[5526.84s] English:** all the time if you're using cursor uh but also like i mean it would introduce like ginormous  
**Translation:** 

**[5532.32s] English:** overhead on the database it would sort of be reading this uh tens of terabyte database sort  
**Translation:** 

**[5540.70s] English:** of approaching like 20 terabytes or something database like every second that's just just  
**Translation:** Vocabulary: terabyte: 万亿字节; terabytes: 万亿字节

**[5546.54s] English:** kind of crazy you definitely don't want to do that so what do you do you sort of you just try  
**Translation:** 

**[5552.72s] English:** to reconcile the single hash which is at the root of the project and then if something mismatches  
**Translation:** 

**[5557.26s] English:** then you go you find where all the things disagree maybe you look at the children and see if the  
**Translation:** 

**[5561.38s] English:** hashes match and if the hashes don't match go look at their children and so on but you only do that  
**Translation:** 

**[5565.60s] English:** in the scenario where things don't match and for most people most of the time the hashes match  
**Translation:** 

**[5569.72s] English:** so it's a kind of like hierarchical reconciliation yeah something like that yeah it's called the  
**Translation:** Vocabulary: hierarchical: 层次分明的; reconciliation: 核对一致

**[5575.54s] English:** merkle tree yeah  
**Translation:** 

**[5576.54s] English:** yeah i mean so yeah this is cool to see that you kind of have to think through all these problems  
**Translation:** Vocabulary: merkle: 默克尔树

**[5581.70s] English:** and i mean the the point of like the reason it's gotten hard is just because like the number of  
**Translation:** 

**[5586.32s] English:** people using it and you know if some of your customers have really really large code bases  
**Translation:** 

**[5592.14s] English:** to the point where we you know we originally reordered our code base which is which is big  
**Translation:** 

**[5598.36s] English:** but i mean it's just not the size of some company that's been there for 20 years and  
**Translation:** 

**[5602.76s] English:** sort of has a ginormous number of files and you sort of want to scale  
**Translation:** 

**[5606.52s] English:** that across programmers there's there's all these details where like building the simple thing is  
**Translation:** 

**[5610.96s] English:** easy but scaling it to a lot of people like a lot of companies is it's obviously a difficult problem  
**Translation:** 

**[5616.00s] English:** which is sort of you know independent of actually so that's there's part of this scaling our current  
**Translation:** 

**[5620.00s] English:** solution is also you know coming up with new ideas that obviously we're working on uh but then but  
**Translation:** 

**[5625.90s] English:** then scaling all of that in the last few weeks months yeah and there are a lot of clever things  
**Translation:** 

**[5630.48s] English:** like additional things that that go into this indexing system um for example the bottleneck in  
**Translation:** 

**[5636.52s] English:** cost is not storing things in the vector database or the database it's actually embedded  
**Translation:** Vocabulary: bottleneck: 瓶颈; embedded: 嵌入; indexing: 索引

**[5640.00s] English:** the code and you don't want to re-embed the code base for every single person in a company that is  
**Translation:** 

**[5645.08s] English:** using the same exact code except for maybe there is a branch with a few different files or they've  
**Translation:** 

**[5650.30s] English:** made a few local changes and so because again embeddings are the bottleneck you can do is one  
**Translation:** 

**[5655.36s] English:** clever trick and not have to worry about like the complexity of like dealing with branches and the  
**Translation:** Vocabulary: complexity: 复杂性; embeddings: 嵌入表示

**[5659.82s] English:** other databases where you just have some cache on the actual vectors uh computed from the hash of a  
**Translation:** 

**[5668.94s] English:** given chunk and so this means that when the nth person at a company goes and embeds their code  
**Translation:** Vocabulary: cache: 缓存; computed: 计算; databases: 数据库; embeds: 嵌入

**[5674.52s] English:** base it's it's really really fast and you do all this without actually storing any code on our  
**Translation:** 

**[5679.50s] English:** servers at all no code data stored we just store the vectors in the vector database and the vector  
**Translation:** 

**[5684.54s] English:** cache what's the biggest gains at this time you get from indexing the code base i could just out  
**Translation:** 

**[5692.46s] English:** of curiosity like what what benefit do users have it seems like longer term there'll be more and more  
**Translation:** 

**[5698.10s] English:** benefit but  
**Translation:** 

**[5698.94s] English:** short term just asking questions of the code base uh what what's the use what's the usefulness of  
**Translation:** 

**[5705.36s] English:** that i think the most obvious one is um just you want to find out where something is happening in  
**Translation:** 

**[5713.26s] English:** your large code base and you sort of have a fuzzy memory of okay i want to find the place where we  
**Translation:** 

**[5718.44s] English:** do x um but you don't exactly know what to search for in a normal text search and so you ask a chat  
**Translation:** 

**[5724.52s] English:** you hit command enter to ask with with the code base chat and then  
**Translation:** 

**[5728.94s] English:** very often it finds the the right place that you were thinking of i i think like you like you  
**Translation:** 

**[5734.16s] English:** mentioned in the future i think this is only going to get more and more powerful where we're working  
**Translation:** 

**[5739.08s] English:** a lot on improving the quality of our retrieval and i think the ceiling for that is really really  
**Translation:** 

**[5744.00s] English:** much higher than people give credit for one question that's good to ask here have you  
**Translation:** Vocabulary: retrieval: 检索

**[5748.44s] English:** considered and why haven't you much done sort of local stuff to where you can do the it seems like  
**Translation:** 

**[5754.62s] English:** everything we just discussed is exceptionally difficult to do to go to go to the cloud you have  
**Translation:** Vocabulary: exceptionally: 特别地

**[5758.94s] English:** to think about all these things with  
**Translation:** 

**[5760.00s] English:** the caching and the, you know, large code base  
**Translation:** Vocabulary: caching: 缓存

**[5765.20s] English:** with a large number of programmers  
**Translation:** 

**[5766.46s] English:** that are using the same code base.  
**Translation:** 

**[5767.62s] English:** You have to figure out the puzzle of that.  
**Translation:** 

**[5769.48s] English:** A lot of it, you know, most software  
**Translation:** 

**[5772.24s] English:** just does stuff, this heavy computational stuff locally.  
**Translation:** 

**[5776.42s] English:** Have you considered doing sort of embeddings locally?  
**Translation:** Vocabulary: computational: 计算的

**[5778.92s] English:** Yeah, we thought about it,  
**Translation:** 

**[5779.90s] English:** and I think it would be cool to do it locally.  
**Translation:** 

**[5782.56s] English:** I think it's just really hard.  
**Translation:** 

**[5784.86s] English:** And one thing to keep in mind is that, you know,  
**Translation:** 

**[5787.26s] English:** some of our users use the latest MacBook Pro,  
**Translation:** 

**[5791.78s] English:** but most of our users, like more than 80% of our users,  
**Translation:** 

**[5794.74s] English:** are in Windows machines,  
**Translation:** 

**[5796.30s] English:** which many of them are not very powerful.  
**Translation:** 

**[5800.02s] English:** And so local models really only works  
**Translation:** 

**[5802.56s] English:** on the latest computers.  
**Translation:** 

**[5804.34s] English:** And it's also a big overhead to build that in.  
**Translation:** 

**[5808.44s] English:** And so even if we would like to do that,  
**Translation:** 

**[5811.48s] English:** it's currently not something that we are able to focus on.  
**Translation:** 

**[5814.40s] English:** And I think there are some people  
**Translation:** 

**[5816.34s] English:** that don't.  
**Translation:** 

**[5817.30s] English:** And I think that's great.  
**Translation:** 

**[5819.78s] English:** But especially as models get bigger and bigger  
**Translation:** 

**[5822.50s] English:** and you want to do fancier things with like bigger models,  
**Translation:** 

**[5825.60s] English:** it becomes even harder to do it locally.  
**Translation:** 

**[5828.34s] English:** And it's not a problem of like weaker computers.  
**Translation:** 

**[5831.56s] English:** It's just that, for example, if you're some big company,  
**Translation:** 

**[5834.98s] English:** you have big company code base,  
**Translation:** 

**[5837.54s] English:** it's just really hard to process big company code base  
**Translation:** 

**[5840.16s] English:** even on the beefiest MacBook Pros.  
**Translation:** Vocabulary: beefiest: 性能最强的

**[5842.10s] English:** So even if it's not even a matter of like,  
**Translation:** 

**[5844.50s] English:** if you're just like a student,  
**Translation:** 

**[5847.26s] English:** or something,  
**Translation:** 

**[5847.88s] English:** I think if you're like the best programmer at a big company,  
**Translation:** 

**[5851.58s] English:** you're still going to have a horrible experience  
**Translation:** 

**[5853.82s] English:** if you do everything locally.  
**Translation:** 

**[5855.76s] English:** I mean, you could do edge and sort of scrape by,  
**Translation:** 

**[5858.68s] English:** but like, again, it wouldn't be fun anymore.  
**Translation:** Vocabulary: scrape: 勉强维持

**[5860.94s] English:** Yeah, like an approximate nearest neighbors  
**Translation:** 

**[5862.28s] English:** and this massive code base is going to just eat up  
**Translation:** Vocabulary: approximate: 近似

**[5864.38s] English:** your memory and your CPU.  
**Translation:** 

**[5866.34s] English:** And that's just that.  
**Translation:** 

**[5870.12s] English:** Like, let's talk about like also the modeling side  
**Translation:** 

**[5872.70s] English:** where, as Arvid said,  
**Translation:** 

**[5873.86s] English:** there are these massive headwinds  
**Translation:** 

**[5875.78s] English:** against local models.  
**Translation:** Vocabulary: headwinds: 逆风

**[5877.24s] English:** Where one, things that...  
**Translation:** 

**[5880.00s] English:** seems to move towards moes which like one benefit is maybe they're more memory bandwidth bound which  
**Translation:** Vocabulary: bandwidth: 带宽

**[5885.52s] English:** plays in favor of local uh versus uh using gpus um or using nvidia gpus but the downside is these  
**Translation:** 

**[5894.80s] English:** models are just bigger in total and you know they're going to need to fit often not even on  
**Translation:** Vocabulary: downside: 缺点

**[5899.34s] English:** a single node of multiple nodes um there's no way that's going to fit inside of even really good  
**Translation:** 

**[5905.24s] English:** macbooks and i think especially for coding it's not a question as much of like does it clear some  
**Translation:** Vocabulary: macbooks: 苹果笔记本

**[5912.54s] English:** bar of like the model's good enough to do these things and then like we're satisfied which may  
**Translation:** 

**[5917.66s] English:** be maybe the case for other other problems and maybe where local models shine but people are  
**Translation:** 

**[5922.10s] English:** always going to want the best the most intelligent the most capable things and that's going to be  
**Translation:** 

**[5927.10s] English:** really really hard to run for almost all people locally don't you want the the most capable model  
**Translation:** 

**[5933.48s] English:** like you want you want  
**Translation:** 

**[5935.24s] English:** and also with oh i like how you're pitching me would you be satisfied with an inferior model  
**Translation:** Vocabulary: inferior: 较差的; pitching: 推荐

**[5942.88s] English:** listen i yeah i'm yes i'm one of those but there's some people that like to do stuff locally  
**Translation:** 

**[5947.88s] English:** especially like yeah i really there's a whole obviously open source movement that kind of  
**Translation:** 

**[5952.78s] English:** resists and it's good that they exist actually because you want to resist the power centers  
**Translation:** 

**[5958.64s] English:** that are growing are there's actually an alternative to local models uh that i am  
**Translation:** 

**[5963.58s] English:** particularly fond of  
**Translation:** 

**[5964.74s] English:** i think it's still very much in the research stage but you could imagine um to do homomorphic  
**Translation:** Vocabulary: homomorphic: 同态的

**[5971.94s] English:** encryption for language model inference so you encrypt your input on your local machine then you  
**Translation:** 

**[5977.10s] English:** send that up and then um the server uh can use loss of computation they can run models that you  
**Translation:** Vocabulary: computation: 计算; encrypt: 加密; encryption: 加密; inference: 推断

**[5983.88s] English:** cannot run locally on this encrypted data um but they cannot see what the data is and then they  
**Translation:** 

**[5988.86s] English:** send back the answer and you decrypt the answer and only you can see the answer uh so i think  
**Translation:** Vocabulary: cannot: 不能; decrypt: 解密; encrypted: 加密

**[5992.94s] English:** that's still very much  
**Translation:** 

**[5994.74s] English:** research and all of it is about trying to make the overhead  
**Translation:** 

**[6000.00s] English:** lower because right now the overhead is really big but if you can make that happen i think that  
**Translation:** 

**[6004.88s] English:** would be really really cool and i think it would be really really impactful um because i think one  
**Translation:** 

**[6010.72s] English:** thing that's actually kind of worrisome is that as these models get better and better uh they're  
**Translation:** 

**[6014.98s] English:** going to become more and more economically useful and so more and more of the world's information  
**Translation:** Vocabulary: economically: 经济效益; worrisome: 令人担忧

**[6019.92s] English:** and data will flow through you know one or two centralized actors um and then there are worries  
**Translation:** 

**[6028.44s] English:** about you know there can be traditional hacker attempts but it also creates this kind of scary  
**Translation:** Vocabulary: hacker: 黑客

**[6034.52s] English:** part where if all of the world's information is flowing through one node in plain text  
**Translation:** 

**[6039.48s] English:** you can have surveillance in very bad ways and sometimes that will happen for you know  
**Translation:** 

**[6047.66s] English:** initially will be like good reasons like people will want to try to protect against like bad  
**Translation:** 

**[6053.06s] English:** actors using ai models in bad ways and then you will add in some surveillance code and then  
**Translation:** 

**[6057.82s] English:** someone else  
**Translation:** 

**[6058.44s] English:** will come in and you know you're in a slippery slope and then you start uh doing bad things with  
**Translation:** 

**[6064.68s] English:** a lot of the world's data and so i i'm very hopeful that uh we can solve homomorphic encryption  
**Translation:** 

**[6071.28s] English:** for doing privacy preserving machine learning but i would say like that's the challenge we have with  
**Translation:** 

**[6076.40s] English:** all software these days it's like there's so many features that can be provided from the cloud  
**Translation:** 

**[6082.80s] English:** and all of us increasingly rely on it and make our life awesome but there's downsides and that's  
**Translation:** Vocabulary: downsides: 缺点

**[6088.12s] English:** why you're not going to be able to do that because you're not going to be able to do it  
**Translation:** 

**[6088.42s] English:** you're not going to be able to do it because you're not going to be able to do it because you're not  
**Translation:** 

**[6088.44s] English:** you rely on really good security to protect from basic attacks but there's also only a small set  
**Translation:** 

**[6094.42s] English:** of companies that are controlling that data you know and they they obviously have leverage and  
**Translation:** Vocabulary: leverage: 影响力

**[6100.14s] English:** they could be infiltrated in all kinds of ways that's the world we live in yeah i mean the thing  
**Translation:** 

**[6105.00s] English:** i'm just actually quite worried about is sort of the world where i mean so entropic has this  
**Translation:** Vocabulary: entropic: 熵增的; infiltrated: 渗透

**[6109.56s] English:** responsible scaling policy and so where we're on like the low low asls which is the entropic  
**Translation:** 

**[6115.78s] English:** security level or whatever uh of like of the world and so i think that's the world we live in  
**Translation:** 

**[6118.42s] English:** of the models but as we get to like  
**Translation:** 

**[6120.00s] English:** quote-unquote ASL 3, ASL 4, whatever models, which are sort of very powerful.  
**Translation:** 

**[6126.66s] English:** But for mostly reasonable security reasons, you would want to monitor all the prompts.  
**Translation:** 

**[6133.34s] English:** But I think that's sort of reasonable and understandable where everyone is coming from.  
**Translation:** Vocabulary: understandable: 可以理解的

**[6138.50s] English:** But Matt, it'd be really horrible if sort of like all the world's information is sort of monitored that heavily.  
**Translation:** 

**[6144.88s] English:** It's way too centralized.  
**Translation:** 

**[6146.44s] English:** Just it's like sort of this really fine line you're walking where on the one side, like you don't want the models to go rogue.  
**Translation:** 

**[6155.10s] English:** On the other side, like humans, like I don't know if I trust like all the world's information to pass through like three model providers.  
**Translation:** Vocabulary: rogue: 行为失控

**[6163.20s] English:** Yeah.  
**Translation:** 

**[6164.24s] English:** Why do you think it's different than cloud providers?  
**Translation:** 

**[6167.64s] English:** Because I think a lot of this data would never have gone to the cloud providers in the first place.  
**Translation:** 

**[6176.44s] English:** Where this is often like you want to give more data to the EIA models.  
**Translation:** 

**[6182.44s] English:** You want to give personal data that you would never have put online in the first place to these companies or to these models.  
**Translation:** 

**[6190.86s] English:** And it also centralizes control where right now for cloud, you can often use your own encryption keys and like AWS can't really do much.  
**Translation:** Vocabulary: encryption: 加密

**[6206.02s] English:** But here.  
**Translation:** 

**[6206.44s] English:** It's just centralized actors that see the exact plain text of everything.  
**Translation:** 

**[6212.52s] English:** On the topic of context, that's actually been a friction for me when I'm writing code, you know, in Python, there's a bunch of stuff imported.  
**Translation:** 

**[6220.02s] English:** There's a you could probably intuit the kind of stuff I would like to include in the context.  
**Translation:** Vocabulary: friction: 矛盾; imported: 导入; intuit: 推断

**[6225.44s] English:** Is there like how hard is it to auto figure out the context?  
**Translation:** 

**[6230.94s] English:** It's tricky.  
**Translation:** 

**[6232.74s] English:** I think we can do a lot better at.  
**Translation:** 

**[6236.44s] English:** Computing the context automatically in the future.  
**Translation:** Vocabulary: computing: 计算

**[6238.60s] English:** One thing that's important to note is.  
**Translation:** 

**[6240.00s] English:** there are trade-offs with including automatic context. So the more context you include for  
**Translation:** 

**[6245.08s] English:** these models, first of all, the slower they are, and the more expensive those requests are,  
**Translation:** 

**[6252.20s] English:** which means you can then do less model calls and do less fancy stuff in the background.  
**Translation:** 

**[6256.10s] English:** Also, for a lot of these models, they get confused if you have a lot of information in the prompt.  
**Translation:** 

**[6260.24s] English:** So the bar for accuracy and for relevance of the context you include should be quite high.  
**Translation:** Vocabulary: relevance: 相关性

**[6265.86s] English:** Um, but this is already, we do some automatic context in some places within the product.  
**Translation:** 

**[6272.80s] English:** It's definitely something we want to get a lot better at. And, um, I think that there are a lot  
**Translation:** 

**[6277.94s] English:** of cool ideas to try there. Um, both on the learning better retrieval systems, like better  
**Translation:** 

**[6286.50s] English:** embedding models, better re-rankers. I think that there are also cool academic ideas, you know,  
**Translation:** Vocabulary: embedding: 嵌入模型; retrieval: 检索系统

**[6291.98s] English:** stuff we've tried out internally, but also the field is grappling with writ large.  
**Translation:** 

**[6295.86s] English:** About, can you get language models to a place where you can actually just have the model itself,  
**Translation:** Vocabulary: grappling: 艰难探索; internally: 内部地

**[6300.32s] English:** like understand a new corpus of information. And the most popular talked about version of this is,  
**Translation:** 

**[6305.76s] English:** can you make the context windows infinite? Then if you make the context windows infinite,  
**Translation:** 

**[6308.92s] English:** can you make the model actually pay attention to the infinite context? And then after you can make  
**Translation:** 

**[6312.66s] English:** it pay attention to the infinite context to make it somewhat feasible to actually do it,  
**Translation:** Vocabulary: feasible: 可行的

**[6316.68s] English:** can you then do caching for that infinite context? You don't have to recompute that all the time.  
**Translation:** 

**[6320.68s] English:** But there are other cool ideas that are being tried that are a little bit more analogous to  
**Translation:** Vocabulary: analogous: 类比

**[6325.22s] English:** fine tuning.  
**Translation:** 

**[6325.86s] English:** I've actually learning this information in the weights of the model. And it might be that you  
**Translation:** 

**[6330.36s] English:** actually get sort of a qualitatively different type of understanding if you do it more at the  
**Translation:** 

**[6335.62s] English:** weight level than if you do it at the in-context learning level. I think the journey, the jury's  
**Translation:** Vocabulary: qualitatively: 质地上

**[6339.14s] English:** still a little bit out on how this is all going to work in the end. Uh, but in the interim, us,  
**Translation:** 

**[6344.08s] English:** us as a company, we are really excited about better retrieval systems and, um, picking the  
**Translation:** Vocabulary: interim: 过渡时期

**[6348.52s] English:** parts of the code base that are most relevant to what you're doing. Uh, we could do that a lot  
**Translation:** 

**[6351.76s] English:** better.  
**Translation:** 

**[6352.70s] English:** Like one interesting proof of concept for the learning,  
**Translation:** 

**[6355.86s] English:** this knowledge directly in the weights is with VS code.  
**Translation:** 

**[6360.00s] English:** so we're in a vs code fork and vs code the code is all public so these models in pre-training  
**Translation:** 

**[6366.74s] English:** have seen all the code um they've probably also seen questions and answers about it and then  
**Translation:** 

**[6371.40s] English:** they've been fine-tuned and early chef to be able to be able to answer questions about code in  
**Translation:** 

**[6375.20s] English:** general so when you ask it a question about vs code you know sometimes it'll hallucinate but  
**Translation:** Vocabulary: hallucinate: 胡言乱语

**[6380.22s] English:** sometimes it actually does a pretty good job at answering the question and i think like this is  
**Translation:** 

**[6386.30s] English:** just by it happens to be okay but what if you could actually like specifically train or post  
**Translation:** 

**[6392.42s] English:** train a model such that it really was built to understand this code base um it's an open research  
**Translation:** 

**[6399.48s] English:** question one that we're quite interested in and then there's also uncertainty of like do you want  
**Translation:** 

**[6403.32s] English:** the model to be the thing that end to end is doing everything i.e it's doing the retrieval and its  
**Translation:** 

**[6408.82s] English:** internals and then kind of answering the question creating the code or do you want to separate the  
**Translation:** Vocabulary: internals: 内部机制; retrieval: 检索

**[6414.30s] English:** retrieval from the front end of the code and then kind of answer the question creating the code  
**Translation:** 

**[6416.30s] English:** into your model where maybe you know you'll get some really capable models that are much better  
**Translation:** 

**[6420.16s] English:** than like the best open source ones in a handful of months um and then you'll want to separately  
**Translation:** 

**[6426.14s] English:** train a really good open source model to be the retriever to be the thing that feeds in the  
**Translation:** Vocabulary: retriever: 检索模型

**[6430.86s] English:** context um to these larger models can you speak a little more to the post training a model to  
**Translation:** 

**[6437.02s] English:** understand the code base like what do you what do you mean by that with is this a synthetic  
**Translation:** Vocabulary: synthetic: 合成的

**[6441.24s] English:** data direction is this yeah i mean there are many possible ways you could  
**Translation:** 

**[6445.98s] English:** try to train a model to be the retriever and then you'll want to separately train a really good  
**Translation:** 

**[6446.28s] English:** open source model to be the retriever and then you'll want to separately train a really good  
**Translation:** 

**[6446.30s] English:** doing it there's certainly no shortage of ideas um it's just a question of going in and like trying  
**Translation:** 

**[6451.74s] English:** all of them and being empirical about which one works best um you know one one very naive thing  
**Translation:** 

**[6457.62s] English:** is to try to replicate what's done uh with vs code uh and these frontier models so let's like  
**Translation:** Vocabulary: empirical: 经验主义; frontier: 前沿; naive: 幼稚

**[6464.38s] English:** continue pre-training some kind of continued pre-training that includes general code data  
**Translation:** 

**[6467.94s] English:** but also throws in a lot of the data of some particular repository that you care about  
**Translation:** Vocabulary: repository: 代码仓库

**[6472.98s] English:** and then in post-training um meaning in  
**Translation:** 

**[6476.28s] English:** let's just start with instruction fine tuning you have like a normal instruction fine tuning  
**Translation:** 

**[6480.00s] English:** data set about code but you throw in a lot of questions about code in that repository  
**Translation:** 

**[6485.66s] English:** so you could either get ground truth ones which might be difficult or you could do what you kind  
**Translation:** 

**[6491.40s] English:** of hinted at or suggested using synthetic data i.e. kind of having the model ask questions about  
**Translation:** 

**[6500.20s] English:** various recent pieces of the code so you kind of take the pieces of the code then prompt the model  
**Translation:** 

**[6505.48s] English:** or have a model propose a question for that piece of code and then add those as instruction  
**Translation:** 

**[6511.14s] English:** fine-tuning data points and then in theory this might unlock the model's ability to answer  
**Translation:** 

**[6516.62s] English:** questions about that code base. Let me ask you about OpenAI 01. What do you think is the role  
**Translation:** 

**[6523.30s] English:** of that kind of test time compute system in programming? I think test time compute is really  
**Translation:** 

**[6529.52s] English:** really interesting. So there's been the pre-training regime which will kind of as  
**Translation:** 

**[6535.30s] English:** you see in the video, it's kind of like a test time compute system. So it's kind of like a  
**Translation:** 

**[6535.46s] English:** scale up the amount of data and the size of your model get you better and better performance both  
**Translation:** 

**[6539.70s] English:** on loss and then on downstream benchmarks and just general performance when we use it for coding  
**Translation:** Vocabulary: benchmarks: 评估标准

**[6544.84s] English:** or other tasks. We're starting to hit a bit of a data wall meaning it's going to be hard to  
**Translation:** 

**[6554.06s] English:** continue scaling up this regime and so scaling up test time compute is an interesting way of now  
**Translation:** 

**[6559.54s] English:** you know increasing the number of inference time flops that we use but still  
**Translation:** 

**[6565.28s] English:** getting like yeah as you increase the number of flops use inference time getting corresponding  
**Translation:** Vocabulary: flops: 运算次数; inference: 推理

**[6570.12s] English:** improvements in the performance of these models. Traditionally we just had to literally train a  
**Translation:** 

**[6575.12s] English:** bigger model that always uses that always used that many more flops but now we could perhaps  
**Translation:** 

**[6579.90s] English:** use the same size model and run it for longer to be able to get an answer at the quality of a much  
**Translation:** 

**[6586.12s] English:** larger model. And so the really interesting thing I like about this is there are some problems that  
**Translation:** 

**[6591.12s] English:** perhaps require a hundred trillion parameter model intelligence.  
**Translation:** 

**[6595.10s] English:** Let's train on a hundred trillion tokens but that's like maybe one percent.  
**Translation:** Vocabulary: parameter: 参数; trillion: 万亿

**[6600.00s] English:** maybe like 0.1% of all queries.  
**Translation:** 

**[6602.86s] English:** So are you going to spend all of this effort,  
**Translation:** 

**[6605.60s] English:** all this compute training a model that costs that much  
**Translation:** 

**[6609.34s] English:** and then run it so infrequently?  
**Translation:** Vocabulary: infrequently: 不经常

**[6611.96s] English:** It feels completely wasteful  
**Translation:** 

**[6613.76s] English:** when instead you get the model that can,  
**Translation:** Vocabulary: wasteful: 浪费的

**[6616.06s] English:** that you train the model that's capable of doing  
**Translation:** 

**[6618.08s] English:** the 99.9% of queries.  
**Translation:** 

**[6620.18s] English:** Then you have a way of inference time,  
**Translation:** 

**[6622.50s] English:** running it longer for those few people  
**Translation:** 

**[6624.50s] English:** that really, really want max intelligence.  
**Translation:** 

**[6626.66s] English:** How do you figure out which problem requires  
**Translation:** 

**[6631.00s] English:** what level of intelligence?  
**Translation:** 

**[6633.02s] English:** Is that possible to dynamically figure out  
**Translation:** Vocabulary: dynamically: 动态地

**[6634.98s] English:** when to use GPT-4, when to use a small model  
**Translation:** 

**[6638.82s] English:** and when you need the 0.1?  
**Translation:** 

**[6642.72s] English:** I mean, yeah, that's an open research problem, certainly.  
**Translation:** 

**[6647.28s] English:** I don't think anyone's actually cracked  
**Translation:** 

**[6648.72s] English:** this model routing problem quite well.  
**Translation:** 

**[6651.04s] English:** We'd like to.  
**Translation:** Vocabulary: routing: 路径选择

**[6651.92s] English:** We have like kind of initial implementations of this  
**Translation:** 

**[6654.54s] English:** for things, for something like cursor tasks,  
**Translation:** Vocabulary: implementations: 实施方案

**[6656.66s] English:** but at the level of like going between 4.0 Sonnet to 0.1.  
**Translation:** 

**[6663.24s] English:** It's a bit trickier.  
**Translation:** Vocabulary: trickier: 更棘手

**[6664.38s] English:** Like there's also a question,  
**Translation:** 

**[6665.70s] English:** like what level of intelligence do you need  
**Translation:** 

**[6667.70s] English:** to determine if the thing is too hard  
**Translation:** 

**[6672.20s] English:** for the four level model?  
**Translation:** 

**[6673.86s] English:** Maybe you need the 0.1 level model.  
**Translation:** 

**[6677.68s] English:** It's really unclear.  
**Translation:** 

**[6679.54s] English:** But you mentioned this,  
**Translation:** 

**[6680.34s] English:** so there's a pre-training process  
**Translation:** 

**[6683.20s] English:** and there's post-training  
**Translation:** 

**[6684.92s] English:** and then there's like test time compute.  
**Translation:** 

**[6686.70s] English:** Is that fair to sort of separate?  
**Translation:** 

**[6688.72s] English:** Where's the biggest gains?  
**Translation:** 

**[6690.82s] English:** Well, it's weird because like test time compute,  
**Translation:** 

**[6693.70s] English:** there's like a whole training strategy needed  
**Translation:** 

**[6696.04s] English:** to get test time to compute to work.  
**Translation:** 

**[6698.26s] English:** And the other really weird thing about this  
**Translation:** 

**[6700.72s] English:** is no one, like outside of the big labs  
**Translation:** 

**[6704.50s] English:** and maybe even just open AI,  
**Translation:** 

**[6706.06s] English:** no one really knows how it works.  
**Translation:** 

**[6707.78s] English:** Like there've been some really interesting papers  
**Translation:** 

**[6709.30s] English:** that show hints of what they might be doing.  
**Translation:** 

**[6713.82s] English:** And so perhaps they're doing something  
**Translation:** 

**[6716.64s] English:** with tree search using process reward models.  
**Translation:** 

**[6720.00s] English:** But yeah, I just I think the issue is, we don't quite know exactly what it looks like. So it would  
**Translation:** 

**[6725.30s] English:** be hard to kind of comment on like, where it fits in, I would put it in post training, but maybe  
**Translation:** 

**[6729.78s] English:** like the compute spent for this kind of for getting test time compute to work for a model  
**Translation:** 

**[6734.40s] English:** is going to dwarf pre training eventually. So we don't even know if O1 is using just like,  
**Translation:** 

**[6742.72s] English:** chain of thought RL, we don't know how they're using any of these. I don't know anything.  
**Translation:** 

**[6746.74s] English:** It's fun to speculate.  
**Translation:** 

**[6750.22s] English:** Like if you were to build a competing model, what would you do?  
**Translation:** Vocabulary: speculate: 猜测

**[6755.08s] English:** Yeah, so one thing to do would be, I think you probably need to train a process reward model,  
**Translation:** 

**[6761.12s] English:** which is so maybe we can get into reward models and outcome reward models versus process reward  
**Translation:** 

**[6765.56s] English:** models. Outcome reward models are the kind of traditional reward models that people are trained  
**Translation:** 

**[6770.54s] English:** for these for for language models, language modeling. And it's just looking at the final  
**Translation:** 

**[6775.10s] English:** thing. So if you're doing some math problem,  
**Translation:** 

**[6776.54s] English:** let's look at that final thing, you've done everything. And let's assign a great how likely  
**Translation:** 

**[6782.64s] English:** we think, like, what's the reward for this, this outcome, process reward models instead try to  
**Translation:** 

**[6787.82s] English:** grade the chain of thought. And so open AI had some preliminary paper on this, I think, last  
**Translation:** 

**[6793.08s] English:** summer, where they use human labelers to get this pretty large several 100,000 data set of grading  
**Translation:** 

**[6801.18s] English:** chains of thought. Ultimately, it feels like I haven't seen anything interesting,  
**Translation:** Vocabulary: labelers: 标注人员

**[6806.54s] English:** in the ways that people use process reward models, outside of just using it as a means of  
**Translation:** 

**[6813.98s] English:** affecting how we choose between a bunch of samples. So like what people do in all these papers is they  
**Translation:** 

**[6819.66s] English:** sample a bunch of outputs from the language model, and then use the process reward models to grade  
**Translation:** 

**[6825.74s] English:** all those generations alongside maybe some other heuristics, and then use that to choose  
**Translation:** Vocabulary: heuristics: 启发式方法

**[6830.14s] English:** the best answer. The really interesting thing that people think might work and people want to work,  
**Translation:** 

**[6836.54s] English:** is tree search with these process reward models, because if you really can,  
**Translation:** 

**[6840.00s] English:** grade every single step of the chain of thought then you can kind of branch out and you know  
**Translation:** 

**[6846.64s] English:** explore multiple paths of this chain of thought and then use these process forward models to  
**Translation:** 

**[6850.50s] English:** evaluate how good is this branch that you're taking yeah when when the quality of the branch  
**Translation:** 

**[6856.12s] English:** is somehow strongly correlated with the quality of the outcome at the very end so like you have  
**Translation:** Vocabulary: correlated: 相关联; evaluate: 评估

**[6860.88s] English:** a good model of knowing which branch to take so not just this in the short term and like in the  
**Translation:** 

**[6865.44s] English:** long term yeah and like the interesting work that i think has been done is figuring out how to  
**Translation:** 

**[6869.04s] English:** properly train the process or the interesting work that has been open sourced and people i think  
**Translation:** 

**[6874.34s] English:** talk about is how to train the process reward models maybe in a more automated way i could  
**Translation:** Vocabulary: automated: 自动化

**[6881.58s] English:** be wrong here could not be mentioning something because i haven't seen anything super that seems  
**Translation:** 

**[6886.32s] English:** to work really well for using the process reward models creatively to do tree search and code  
**Translation:** Vocabulary: creatively: 创造性地

**[6891.76s] English:** this is kind of an ai safety maybe a bit of a philosophy question so open ai says that they're  
**Translation:** 

**[6897.46s] English:** hiding the chain of thought from the user  
**Translation:** 

**[6899.02s] English:** and they've said that that was a difficult decision to make they instead of showing the  
**Translation:** 

**[6905.16s] English:** chain of thought they're asking the model to summarize the chain of thought they're also in  
**Translation:** 

**[6909.84s] English:** the background saying they're going to monitor the chain of thought to make sure the model is  
**Translation:** 

**[6913.94s] English:** not trying to manipulate the user which is a fascinating possibility but anyway what do you  
**Translation:** Vocabulary: manipulate: 操控

**[6919.16s] English:** think about hiding the chain of thought one consideration for open ai and this is completely  
**Translation:** 

**[6923.26s] English:** speculative could be that they want to make it hard for people to distill these capabilities  
**Translation:** Vocabulary: distill: 提炼; speculative: 推测

**[6927.96s] English:** out of their model  
**Translation:** 

**[6929.58s] English:** it might actually be easier if you had access to that hidden chain of thought  
**Translation:** 

**[6933.42s] English:** to replicate the technology because that's pretty important data like seeing seeing the steps that  
**Translation:** 

**[6938.22s] English:** the model took to get to the final result so you could probably train on that also and there was  
**Translation:** 

**[6942.62s] English:** sort of a mirror situation with this with some of the large language model providers and also this  
**Translation:** 

**[6947.58s] English:** is speculation but um some of these apis um used to offer easy access to log probabilities for  
**Translation:** Vocabulary: probabilities: 概率; speculation: 猜测

**[6955.66s] English:** all the tokens that they're generating um and also log probabilities that they're generating  
**Translation:** 

**[6959.02s] English:** um and also some of these apis um used to offer easy access to log probabilities for the prompt tokens  
**Translation:** 

**[6959.82s] English:** and  
**Translation:** 

**[6967.42s] English:** and  
**Translation:** 

**[6970.38s] English:** um  
**Translation:** 

**[6971.98s] English:** so  
**Translation:** 

**[6975.58s] English:** so  
**Translation:** 

**[6981.58s] English:** so  
**Translation:** 

**[6984.78s] English:** um  
**Translation:** 

**[6987.18s] English:** um  
**Translation:** 

**[6987.66s] English:** so  
**Translation:** 

**[6960.00s] English:** then some of these APIs took those away. And again, complete speculation, but one of the  
**Translation:** 

**[6966.24s] English:** thoughts is that the reason those were taken away is if you have access log probabilities,  
**Translation:** 

**[6970.96s] English:** similar to this hidden chain of thought, that can give you even more information to try and distill  
**Translation:** 

**[6975.04s] English:** these capabilities out of the APIs, out of these biggest models, into models you control.  
**Translation:** 

**[6979.92s] English:** As an asterisk on also the previous discussion about us integrating O1, I think that we're  
**Translation:** Vocabulary: integrating: 整合

**[6987.12s] English:** still learning how to use this model. We made O1 available in Cursor because  
**Translation:** 

**[6992.64s] English:** when we got the model, we were really interested in trying it out. I think a lot of programmers  
**Translation:** Vocabulary: programmers: 程序员

**[6997.12s] English:** are going to be interested in trying it out. But O1 is not part of the default Cursor experience  
**Translation:** 

**[7003.36s] English:** in any way. And we still haven't found a way to yet integrate it into the editor in a way that  
**Translation:** Vocabulary: integrate: 整合

**[7012.24s] English:** we reach for every hour, maybe even every day.  
**Translation:** 

**[7017.12s] English:** I think the jury is still out on how to use the model. We haven't seen examples yet of  
**Translation:** 

**[7024.56s] English:** people releasing things where it seems really clear, like, Oh, that's like now the  
**Translation:** 

**[7028.64s] English:** use case. The obvious one to turn to is maybe this can make it easier for you  
**Translation:** 

**[7032.96s] English:** to have these background things running, to have these models and loops, to have these models be  
**Translation:** 

**[7037.04s] English:** Egeonciaq, but we're still still discovering.  
**Translation:** 

**[7042.24s] English:** To be clear, we have ideas. We just need to try and  
**Translation:** 

**[7046.72s] English:** try again and know what is important. When you really want to use stuff that might even be and  
**Translation:** 

**[7046.96s] English:** decide to get a few manageable things. There is no guarantee that you'll actually get an example on  
**Translation:** 

**[7047.08s] English:** something we have. It might do trouble with some software you're working on coming along. You  
**Translation:** 

**[7047.10s] English:** incredibly useful before we put it out there but it has these significant limitations like even  
**Translation:** 

**[7052.86s] English:** like barring capabilities uh it does not stream and that means it's really really painful to use  
**Translation:** 

**[7060.52s] English:** for things where you want to supervise the output um and instead you're just waiting for the wall  
**Translation:** 

**[7065.64s] English:** text to show up um also it does feel like the early innings of test time compute and search  
**Translation:** Vocabulary: innings: 球局; supervise: 监督

**[7070.76s] English:** where it's just like a very very much a v zero um and there's so many things that like  
**Translation:** 

**[7076.10s] English:** like don't feel quite right and i suspect  
**Translation:** 

**[7080.00s] English:** in parallel to people increasing the amount of pre-training data  
**Translation:** 

**[7085.50s] English:** and the size of the models and pre-training and finding tricks there,  
**Translation:** 

**[7088.10s] English:** you'll now have this other thread of getting search to work better and better.  
**Translation:** 

**[7093.42s] English:** So let me ask you about strawberry tomorrow eyes.  
**Translation:** 

**[7099.68s] English:** So it looks like GitHub Copilot might be integrating O1 in some kind of way.  
**Translation:** 

**[7107.48s] English:** And I think some of the comments are saying, does this mean Cursor is done?  
**Translation:** Vocabulary: copilot: 副驾; integrating: 整合

**[7112.84s] English:** I think I saw one comment saying that.  
**Translation:** 

**[7115.16s] English:** I saw time to shut down Cursor.  
**Translation:** 

**[7116.96s] English:** Time to shut down Cursor, thank you.  
**Translation:** 

**[7119.44s] English:** So is it time to shut down Cursor?  
**Translation:** 

**[7121.38s] English:** I think this space is a little bit different from past software spaces over the 2010s,  
**Translation:** 

**[7127.12s] English:** where I think that the ceiling here is really, really, really incredibly high.  
**Translation:** 

**[7131.38s] English:** And so I think that the best product in three to four years  
**Translation:** 

**[7134.36s] English:** will just be so much more useful than the best product today.  
**Translation:** 

**[7137.10s] English:** And so I think that the best product in three to four years  
**Translation:** 

**[7137.46s] English:** and you can wax poetic about moats this and brand that,  
**Translation:** Vocabulary: moats: 护城河

**[7142.92s] English:** and this is our advantage.  
**Translation:** 

**[7145.08s] English:** But I think in the end, just if you don't have,  
**Translation:** 

**[7147.70s] English:** if you stop innovating on the product, you will lose.  
**Translation:** 

**[7150.94s] English:** And that's also great for startups.  
**Translation:** Vocabulary: innovating: 持续创新; startups: 初创企业

**[7153.12s] English:** That's great for people trying to enter this market  
**Translation:** 

**[7155.36s] English:** because it means you have an opportunity  
**Translation:** 

**[7157.10s] English:** to win against people who have lots of users already  
**Translation:** 

**[7160.80s] English:** by just building something better.  
**Translation:** 

**[7164.46s] English:** And so I think, yeah, over the next few years,  
**Translation:** 

**[7166.10s] English:** it's just about building.  
**Translation:** 

**[7167.46s] English:** Building the best product, building the best system.  
**Translation:** 

**[7169.90s] English:** And that both comes down to the modeling engine side of things.  
**Translation:** 

**[7174.54s] English:** And it also comes down to the editing experience.  
**Translation:** 

**[7177.50s] English:** Yeah, I think most of the additional value from Cursor  
**Translation:** 

**[7180.80s] English:** versus everything else out there  
**Translation:** 

**[7182.60s] English:** is not just integrating the new model fast like 01.  
**Translation:** 

**[7186.22s] English:** It comes from all of the kind of depth that goes into these custom models  
**Translation:** 

**[7191.58s] English:** that you don't realize are working for you  
**Translation:** 

**[7193.50s] English:** in kind of every facet of the product,  
**Translation:** 

**[7195.50s] English:** as well as like the really,  
**Translation:** Vocabulary: facet: 方面

**[7197.46s] English:** thoughtful UX with every single.  
**Translation:** 

**[7200.00s] English:** feature all right uh from that profound answer let's descend back down to the technical you  
**Translation:** Vocabulary: thoughtful: 周到

**[7205.82s] English:** mentioned you have a taxonomy of synthetic data oh yeah uh can you please explain yeah i think  
**Translation:** 

**[7211.40s] English:** uh there are three main kinds of synthetic data the first is so what is synthetic data first  
**Translation:** Vocabulary: synthetic: 合成数据; taxonomy: 分类体系

**[7217.86s] English:** so there's normal data like non-synthetic data which is just data that's naturally created i.e  
**Translation:** 

**[7224.32s] English:** usually it'll be from humans having done things so from some human process you get this data  
**Translation:** 

**[7229.82s] English:** synthetic data uh the first one would be distillation so having a language model  
**Translation:** 

**[7236.06s] English:** kind of output tokens or probability distributions over tokens um and then you can train some less  
**Translation:** Vocabulary: distillation: 蒸馏

**[7243.40s] English:** capable model on this uh this approach is not going to get you a net like more capable model  
**Translation:** 

**[7249.02s] English:** than the original one that has produced the tokens um but it's really useful for if there's  
**Translation:** 

**[7254.52s] English:** some capability you want to elicit from some really expensive high latency model you can  
**Translation:** 

**[7259.44s] English:** then that  
**Translation:** Vocabulary: capability: 能力; elicit: 诱发; latency: 延迟

**[7259.70s] English:** distкі  
**Translation:** 

**[7259.82s] English:** distill that down into some smaller task-specific model.  
**Translation:** Vocabulary: distill: 提炼

**[7265.00s] English:** The second kind is when one direction of the problem is easier than the reverse.  
**Translation:** 

**[7272.30s] English:** And so a great example of this is bug detection, like we mentioned earlier, where it's a lot  
**Translation:** 

**[7279.28s] English:** easier to introduce reasonable-looking bugs than it is to actually detect them.  
**Translation:** 

**[7285.02s] English:** And this is probably the case for humans too.  
**Translation:** 

**[7288.68s] English:** And so what you can do is you can get a model that's not trained in that much data, that's  
**Translation:** 

**[7293.04s] English:** not that smart, to introduce a bunch of bugs in code.  
**Translation:** 

**[7295.86s] English:** And then you can use that to then train, use the synthetic data to train a model that can  
**Translation:** 

**[7300.12s] English:** be really good at detecting bugs.  
**Translation:** Vocabulary: detecting: 检测外泄

**[7302.22s] English:** The last category I think is, I guess, the main one that it feels like the big labs are  
**Translation:** 

**[7307.54s] English:** doing for synthetic data, which is producing text with language models that can then be  
**Translation:** 

**[7315.54s] English:** verified easily.  
**Translation:** 

**[7318.34s] English:** So like...  
**Translation:** Vocabulary: verified: 验证过

**[7318.66s] English:** You know, an extreme example of this is...  
**Translation:** 

**[7320.00s] English:** if you have a verification system that can detect if language is Shakespeare level, and then you have  
**Translation:** Vocabulary: verification: 验证系统

**[7326.04s] English:** a bunch of monkeys typing in typewriters, like, you can eventually get enough training data to  
**Translation:** 

**[7330.76s] English:** train a Shakespeare level language model. And I mean, this is the case, like very much the case  
**Translation:** Vocabulary: typewriters: 打字机

**[7334.66s] English:** for math, where verification is actually really, really easy for formal languages. And then what  
**Translation:** 

**[7343.54s] English:** you can do is you can have an okay model, generate a ton of rollouts, and then choose the ones that  
**Translation:** Vocabulary: rollouts: 模拟结果

**[7349.86s] English:** you know have actually proved the ground truth theorems and train that further. There's similar  
**Translation:** 

**[7355.04s] English:** things you can do for code with leet code-like problems, where if you have some set of tests  
**Translation:** Vocabulary: theorems: 定理

**[7361.02s] English:** that you know correspond to, if something passes these tests, it has actually solved the problem.  
**Translation:** 

**[7365.52s] English:** You could do the same thing where you verify that it's passed the test and then train the model and  
**Translation:** Vocabulary: correspond: 符合; verify: 验证

**[7368.80s] English:** the outputs that have passed the test. I think it's gonna be a little tricky getting this to work  
**Translation:** 

**[7373.80s] English:** in all domains or just in general. Like having the perfect verifier feels  
**Translation:** Vocabulary: verifier: 验证器

**[7379.56s] English:** really difficult. I think it's gonna be a little tricky getting this to work in all domains or just  
**Translation:** 

**[7379.84s] English:** really, really hard to do with just like open-ended miscellaneous tasks you give the model or more like  
**Translation:** Vocabulary: miscellaneous: 杂项

**[7386.16s] English:** long horizon tasks, even in coding. That's because you're not as optimistic as Arvid,  
**Translation:** 

**[7391.02s] English:** but yeah. So yeah, so that third category requires having a verifier. Yeah. Verification, it feels  
**Translation:** 

**[7398.28s] English:** like it's best when you know for a fact that it's correct. And then it wouldn't be like using a  
**Translation:** 

**[7403.14s] English:** language model to verify. It would be using tests or formal systems. Or running the thing,  
**Translation:** 

**[7409.84s] English:** doing like the human form of verification where you just do manual quality control.  
**Translation:** 

**[7413.98s] English:** Yeah. Yeah. But like the language model version of that where it's like running the thing and  
**Translation:** 

**[7417.90s] English:** actually understands the output. Yeah. No, that's true. Somewhere between. Yeah. I think that's the  
**Translation:** 

**[7423.12s] English:** category that is most likely to result in like massive gains. What about RL with feedback side,  
**Translation:** 

**[7430.40s] English:** RLHF versus RLAIF? What's the role of that in getting better performance on the models?  
**Translation:** 

**[7439.84s] English:** Yeah. So that's an interesting question. Yeah. And what are you  
**Translation:** 

**[7442.62s] English:** arguing that that's an advantage that the model needs to have?  
**Translation:** 

**[7445.00s] English:** What are the potential costs?  
**Translation:** 

**[7446.26s] English:** Yeah. So, one is on the final point, the cost of a model really needs to be done at a later time.  
**Translation:** 

**[7452.08s] English:** Because if the model is not going to be the one to work on, then that doesn't change.  
**Translation:** 

**[7455.36s] English:** OK, so then there's the cost of the model, doesn't matter how much you put it back together.  
**Translation:** 

**[7459.58s] English:** So, that's one. And then there's the cost of final product. Yeah, so the cost of building a model  
**Translation:** 

**[7464.26s] English:** is going to depend on the model and the cost of the model itself. Yeah, it really depends on what  
**Translation:** 

**[7467.94s] English:** you're going to build.  
**Translation:** 

**[7468.60s] English:** All right, thanks a lot.  
**Translation:** 

**[7469.14s] English:** Thanks, guys.  
**Translation:** 

**[7469.52s] English:** Thanks.  
**Translation:** 

**[7469.70s] English:** Thanks.  
**Translation:** 

**[7469.76s] English:** Thanks.  
**Translation:** 

**[7440.00s] English:** Yeah. So RLHF is when the reward model you use is trained from some labels you've collected  
**Translation:** 

**[7449.78s] English:** from humans giving feedback. I think this works if you have the ability to get a ton of human  
**Translation:** 

**[7457.74s] English:** feedback for this kind of task that you care about. RLAIF is interesting because you're kind  
**Translation:** 

**[7465.12s] English:** of depending on, like, this is actually kind of going to, it's depending on the constraint that  
**Translation:** 

**[7471.66s] English:** verification is actually a decent bit easier than generation. Because it feels like, okay,  
**Translation:** Vocabulary: constraint: 限制; verification: 验证

**[7477.82s] English:** what are you doing? Are you using this language model to look at the language model outputs and  
**Translation:** 

**[7481.36s] English:** then prove the language model? But no, it actually may work if the language model has a much easier  
**Translation:** 

**[7487.42s] English:** time verifying some solution than it does generating it. Then you actually could perhaps  
**Translation:** 

**[7492.36s] English:** get this kind of recursive loop. I don't think it's going to look exactly,  
**Translation:** Vocabulary: recursive: 递归; verifying: 验证

**[7495.12s] English:** like, that. The other thing you could do is, that we kind of do, is, like, a little bit of a mix  
**Translation:** 

**[7502.64s] English:** of RLAIF and RLHF, where usually the model is actually quite correct. And this is in the case  
**Translation:** 

**[7508.32s] English:** of CursorTab, picking between, like, two possible generations of what is the better one. And then  
**Translation:** 

**[7515.48s] English:** it just needs, like, a little bit of human nudging with only, like, on the order of 50, 100 examples  
**Translation:** Vocabulary: nudging: 引导

**[7523.86s] English:** to, like,  
**Translation:** 

**[7525.12s] English:** kind of align that prior the model has with exactly with what you want. It looks different  
**Translation:** Vocabulary: align: 使一致

**[7529.66s] English:** than, I think, normal RLHF, where you're usually training these reward models on tons of examples.  
**Translation:** 

**[7535.72s] English:** What's your intuition when you compare generation and verification, or generation and ranking?  
**Translation:** Vocabulary: intuition: 直觉

**[7542.18s] English:** Is ranking way easier than generation?  
**Translation:** 

**[7545.62s] English:** My intuition would just say, yeah, it should be. Like, this is kind of going back to,  
**Translation:** 

**[7553.72s] English:** like, if you believe,  
**Translation:** 

**[7555.12s] English:** P does not equal NP, then there's this massive class of problems that are much  
**Translation:** 

**[7560.00s] English:** much easier to verify given a proof than actually proving it i wonder if the same thing will prove  
**Translation:** 

**[7565.92s] English:** p not equal to mp or p equal to mp that would be that would be really cool that'd be of whatever  
**Translation:** Vocabulary: verify: 验证

**[7572.60s] English:** feels metal by ai who gets the credit another open philosophical question  
**Translation:** 

**[7579.40s] English:** i'm actually i'm actually surprisingly curious what what what like a good bet for one uh one  
**Translation:** Vocabulary: philosophical: 哲学的

**[7589.40s] English:** yeah i will get the fields metal will be actually don't have a month specialty uh i i don't know  
**Translation:** 

**[7594.00s] English:** what a month's bet here is oh sorry nobel prize or feels metal first metal feels metal level  
**Translation:** Vocabulary: nobel: 诺贝尔; specialty: 专长

**[7599.56s] English:** feels metal needs to solve i think feels metal comes first well you would say that of course  
**Translation:** 

**[7603.80s] English:** but it's also this like isolated system you know if i and no sure yeah like i don't even know if i  
**Translation:** Vocabulary: isolated: 孤立的

**[7609.74s] English:** don't need to do i feel like i have much more to do there it felt like the path to get to imo was  
**Translation:** 

**[7613.66s] English:** a little bit more clear because it already could get a few imo problems and there are a bunch of  
**Translation:** 

**[7618.56s] English:** like there's  
**Translation:** 

**[7619.40s] English:** a bunch of low-hanging fruit given the literature at the time of like what what tactics people could  
**Translation:** Vocabulary: tactics: 策略

**[7623.40s] English:** take i think i'm one much less versed in the space that they're improving now and two yeah less  
**Translation:** 

**[7629.88s] English:** intuition about how close we are to solving these really really hard open problems so you think  
**Translation:** 

**[7636.20s] English:** you'll be feels my first it won't be like in uh physics or in oh 100 i think i think i think that's  
**Translation:** 

**[7642.12s] English:** probably more likely like it's probably much more likely that i'll get then yeah yeah well i think  
**Translation:** 

**[7649.40s] English:** it's just the same thing like if you've got like like natural  
**Translation:** 

**[7660.00s] English:** if you have a really hard math problem like like almost fully realized otherwise like that you could  
**Translation:** 

**[7664.94s] English:** probably you could actually solve it yeah you can you can do that but in the end things are  
**Translation:** 

**[7671.22s] English:** just everywhere but you know you can't solve that problem you've got completely like you can get  
**Translation:** 

**[7675.08s] English:** you don't have to be like a real math teacher you can get a real math teacher or you can do it easily  
**Translation:** 

**[7678.04s] English:** AGI, I mean,  
**Translation:** 

**[7680.00s] English:** Yeah. I'd be very happy. I'd be very happy. But I don't know if I think 2028, 2030.  
**Translation:** 

**[7689.54s] English:** What feels metal.  
**Translation:** 

**[7690.80s] English:** Feels metal.  
**Translation:** 

**[7691.44s] English:** All right. It feels like forever from now, given how fast things have been going. Speaking of how fast things have been going, let's talk about scaling laws.  
**Translation:** 

**[7701.10s] English:** So for people who don't know, maybe it's good to talk about this whole idea of scaling laws.  
**Translation:** 

**[7710.00s] English:** What are they? Where do you think stand? And where do you think things are going?  
**Translation:** 

**[7713.88s] English:** I think it's interesting. The original scaling laws paper by OpenAI was slightly wrong because I think of some issues they did with learning rate schedules.  
**Translation:** 

**[7723.46s] English:** And then Chinchilla showed a more correct version.  
**Translation:** Vocabulary: chinchilla: 金毛鼠

**[7726.68s] English:** And then from then, people have again kind of deviated from doing the compute optimal thing because people start now optimizing more so for making the thing work really well, given an inference budget.  
**Translation:** 

**[7738.72s] English:** And I think there are a lot more dimensions to these curves than what we originally used of just compute, number of parameters and data.  
**Translation:** Vocabulary: deviated: 偏离; dimensions: 维度; inference: 推理; optimal: 最优; optimizing: 优化

**[7750.68s] English:** Like inference compute is the obvious one.  
**Translation:** 

**[7752.66s] English:** I think context length is another obvious one.  
**Translation:** 

**[7754.68s] English:** So if you care, like, let's say you care about the two things of inference compute and then context window, maybe the thing you want to train is some kind of SSM because they're much, much cheaper and faster at super, super long context.  
**Translation:** 

**[7768.72s] English:** And even if maybe it is 10x worth scaling properties during training, meaning you spend 10x more compute to train the thing to get the same level of capabilities, it's worth it because you care most about that inference budget for really long context windows.  
**Translation:** 

**[7783.16s] English:** So it'll be interesting to see how people kind of play with all these dimensions.  
**Translation:** 

**[7787.30s] English:** So, yeah, I mean, you speak to the multiple dimensions, obviously.  
**Translation:** 

**[7790.00s] English:** The original conception was just looking at the variables of the size of the model as measured by parameters and the size of the data as measured by the number of tokens.  
**Translation:** 

**[7798.06s] English:** And look.  
**Translation:** Vocabulary: conception: 观念

**[7798.72s] English:** With the ratio of the two?  
**Translation:** 

**[7799.78s] English:** Yeah.  
**Translation:** 

**[7800.00s] English:** And it's it's kind of a compelling notion that there is a number or at least a minimum.  
**Translation:** 

**[7806.04s] English:** And it seems like one was emerging.  
**Translation:** Vocabulary: compelling: 有说服力的

**[7810.04s] English:** Do you still believe that there is a kind of bigger is better?  
**Translation:** 

**[7815.32s] English:** I mean, I think bigger is certainly better for just raw performance and intelligence and raw intelligence.  
**Translation:** 

**[7823.28s] English:** I think that the path that people might take is I'm particularly bullish on distillation.  
**Translation:** 

**[7827.28s] English:** And like, yeah, how many knobs can you turn to if we spend like a ton, ton of money on training, like get the most capable, cheap model, right?  
**Translation:** Vocabulary: bullish: 看涨; distillation: 提纯; knobs: 旋钮

**[7838.38s] English:** Like really, really caring as much as you can, because like the naive version of caring as much as you can about inference time computers, what people have already done with like the Lama models are just overtraining the shit out of 7B models on way, way, way more tokens than is essentially optimal.  
**Translation:** 

**[7853.88s] English:** But if you really care about it, maybe the thing to do is what Gamma did, which is.  
**Translation:** Vocabulary: gamma: 伽马; naive: 幼稚

**[7857.28s] English:** Let's just not let's not just train on tokens.  
**Translation:** 

**[7858.94s] English:** Let's literally train on minimizing the KL divergence with the distribution of Gamma 27B, right?  
**Translation:** Vocabulary: divergence: 差异; minimizing: 最小化

**[7868.50s] English:** So knowledge distillation there.  
**Translation:** 

**[7870.82s] English:** And you're spending the compute of literally training this 27 billion model, billion parameter model on all these tokens just to get out this, I don't know, smaller model.  
**Translation:** Vocabulary: parameter: 参数

**[7880.42s] English:** And the distillation gives you just a faster model.  
**Translation:** 

**[7882.54s] English:** Smaller means faster.  
**Translation:** 

**[7883.58s] English:** Yeah, distillation in theory is.  
**Translation:** 

**[7887.28s] English:** I think getting out more signal from the data that you're training on.  
**Translation:** 

**[7890.68s] English:** And it's like another it's perhaps another way of getting over, not like completely over, but like partially helping with the data wall where like you only have so much data to train on.  
**Translation:** 

**[7899.44s] English:** Let's like train this really, really big model on all these tokens and we'll distill it into a smaller one.  
**Translation:** Vocabulary: distill: 浓缩

**[7903.78s] English:** And maybe we can get more signal per token for this for this much smaller model than we would have originally if we trained it.  
**Translation:** 

**[7911.30s] English:** So if I gave you 10 trillion dollars, how would you spend it?  
**Translation:** Vocabulary: token: 令牌; trillion: 万亿

**[7916.50s] English:** I mean, you can't buy.  
**Translation:** 

**[7917.28s] English:** An island or whatever.  
**Translation:** 

**[7918.38s] English:** How would you allocate it?  
**Translation:** 

**[7920.00s] English:** in terms of improving the the big model versus maybe paying for hf in the rlhf yeah or yeah i  
**Translation:** Vocabulary: allocate: 分配

**[7931.22s] English:** think there's a lot of these secrets and details about training these large models that i i just  
**Translation:** 

**[7937.70s] English:** don't know and are only privy to the large labs and the issue is i would waste a lot of that money  
**Translation:** Vocabulary: privy: 知情

**[7941.94s] English:** if i even attempted this because i wouldn't know those things uh suspending a lot of disbelief  
**Translation:** 

**[7947.86s] English:** and assuming like you had the know-how um and operate or or if you're saying like you have to  
**Translation:** Vocabulary: disbelief: 怀疑; suspending: 放下

**[7954.82s] English:** operate with like the limited information you have now no no actually i would say you swoop in and  
**Translation:** 

**[7960.90s] English:** you get all the information all the little heuristics all the little parameters all the  
**Translation:** Vocabulary: heuristics: 启发式; swoop: 突袭

**[7964.92s] English:** all the parameters that define how the thing is trained if we look in how to invest money  
**Translation:** 

**[7972.98s] English:** for the next five years in terms of maximizing what you called raw intelligence i mean it's  
**Translation:** Vocabulary: maximizing: 最大化

**[7977.84s] English:** isn't the answer like really simple you just you just try to get as much compute as possible  
**Translation:** 

**[7981.96s] English:** like like at the end of the day all you need to buy is the gpus and then sort of the the  
**Translation:** 

**[7987.06s] English:** researchers can find find all the all like they can sort of you can tune whether you want  
**Translation:** 

**[7991.74s] English:** to be trained a big model or a small model like well this gets into the question of like are you  
**Translation:** 

**[7996.82s] English:** really limited by compute and money or are you limited by these other things and i'm more  
**Translation:** 

**[8002.52s] English:** privy to arvid's arvid's belief that we're sort of idea limited but there's always like  
**Translation:** 

**[8007.84s] English:** if you have a lot of compute you can run a lot of experiments so you would run a lot of  
**Translation:** 

**[8014.06s] English:** experiments versus like use that compute to train a gigantic model i would but i i do believe that  
**Translation:** Vocabulary: gigantic: 巨大的

**[8021.74s] English:** we are limited in terms of ideas that we have i think yeah because even with all this compute  
**Translation:** 

**[8027.56s] English:** and like you know all the data you could collect in the world i think you really are ultimately  
**Translation:** 

**[8032.16s] English:** limited by not even ideas but just like really good engineering  
**Translation:** 

**[8037.84s] English:** like even  
**Translation:** 

**[8040.00s] English:** with all the capital in the world would you really be able to assemble like there aren't that many  
**Translation:** 

**[8044.68s] English:** people in the world who really can like make the difference here um and and there's so much work  
**Translation:** Vocabulary: assemble: 聚集

**[8049.60s] English:** that goes into research that is just like pure really really hard engineering work um as like a  
**Translation:** 

**[8056.42s] English:** very kind of hand wavy example if you look at the original transformer paper you know how much work  
**Translation:** 

**[8061.34s] English:** was kind of joining together a lot of these really interesting concepts embedded in the literature  
**Translation:** 

**[8066.26s] English:** versus then going in and writing all the codes like maybe the cuda kernels maybe whatever else  
**Translation:** Vocabulary: embedded: 嵌入; kernels: 内核

**[8071.88s] English:** i don't know if it ran on gpus or tpus originally such that it actually saturated the gpu gpu  
**Translation:** 

**[8076.80s] English:** performance right getting gnomes here to go in and do do all this code right and gnome is like  
**Translation:** Vocabulary: gnome: 小型助手; gnomes: 小型助手

**[8081.82s] English:** probably one of the best engineers in the world or maybe going a step further like the next  
**Translation:** 

**[8085.64s] English:** generation of models having these things like getting model parallelism to work and scaling  
**Translation:** 

**[8090.04s] English:** it on like you know thousands of or maybe tens of thousands of like v100s which i think gbde3  
**Translation:** 

**[8095.58s] English:** may have been  
**Translation:** 

**[8096.26s] English:** um there's just so much engineering effort that has to go into all these things to make it work  
**Translation:** 

**[8101.58s] English:** um if you really brought that cost down to like you know maybe not zero but just made it 10x  
**Translation:** 

**[8109.36s] English:** easier made it super easy for someone with really fantastic ideas to immediately get to the version  
**Translation:** 

**[8115.68s] English:** of like the new architecture they dreamed up that is like getting 50 40 percent uh utilization on  
**Translation:** 

**[8121.80s] English:** the gpus i think that would just speed up research by  
**Translation:** 

**[8125.88s] English:** you  
**Translation:** 

**[8126.26s] English:** a ton i mean i think i think if you see a clear path to improvement you you should always sort of  
**Translation:** 

**[8131.52s] English:** take the low-hanging fruit first right and i think probably open the eye and and all the other labs  
**Translation:** 

**[8136.70s] English:** that did the right thing to pick off the low-hanging fruit where the low-hanging fruit is  
**Translation:** 

**[8140.36s] English:** like sort of you you could scale up to a gpt 4.25 scale um and you just keep scaling and  
**Translation:** 

**[8151.18s] English:** and like things things keep getting better and as long as like you there's there's no  
**Translation:** 

**[8156.26s] English:** point of experimenting with new ideas when like everything everything is working and  
**Translation:** Vocabulary: experimenting: 尝试新想法

**[8160.00s] English:** you should sort of bang on it and try to try to get as much as much juice out of the possible and  
**Translation:** 

**[8164.26s] English:** then and then maybe maybe when you really need new ideas for i think i think if you're if you're  
**Translation:** 

**[8168.12s] English:** spending 10 trillion dollars probably want to spend some you know then actually like re-evaluate  
**Translation:** 

**[8172.86s] English:** your ideas like probably your idea limited at that point i think all of us believe new ideas  
**Translation:** Vocabulary: trillion: 万亿

**[8177.54s] English:** are probably needed to get you know all the way there to agi and all of us also probably believe  
**Translation:** 

**[8186.40s] English:** there exist ways of testing out those ideas at smaller scales and being fairly confident that  
**Translation:** 

**[8194.28s] English:** they'll play out it's just quite difficult for the labs in their current position to dedicate  
**Translation:** 

**[8201.34s] English:** their very limited research and engineering talent to exploring all these other ideas when  
**Translation:** 

**[8207.52s] English:** there's like this core thing that will probably like improve performance for some like decent  
**Translation:** 

**[8213.88s] English:** amount of time yeah  
**Translation:** 

**[8216.32s] English:** yeah  
**Translation:** 

**[8216.38s] English:** yeah  
**Translation:** 

**[8216.40s] English:** this is going wild okay  
**Translation:** 

**[8222.72s] English:** so how uh big question looking out into the future you're now at the the center of the  
**Translation:** 

**[8230.96s] English:** programming world how do you think programming the nature of programming changes in the next  
**Translation:** 

**[8235.32s] English:** few months in the next year in the next two years next five years ten years  
**Translation:** 

**[8240.02s] English:** i think we're really excited about a future where the programmers in the driver's seat  
**Translation:** 

**[8245.64s] English:** for a long time and you've heard us talk about this a little bit but one that emphasizes  
**Translation:** 

**[8251.56s] English:** speed and agency for the programmer and control the ability to modify anything you want to modify  
**Translation:** 

**[8258.52s] English:** the ability to iterate really fast on what you're building and this is a little different i think  
**Translation:** 

**[8265.30s] English:** than where some people um are are jumping to uh in the space where i think one idea that's  
**Translation:** 

**[8273.38s] English:** captivated people is can you talk to people and can you talk to people and can you talk to people  
**Translation:** Vocabulary: captivated: 深深吸引

**[8275.62s] English:** and can you talk to your um computer can you have it build software for you as if you're  
**Translation:** 

**[8280.00s] English:** talking to like an engineering department or an engineer over slack and can it just be this this  
**Translation:** 

**[8283.86s] English:** sort of isolated text box and um part of the reason we're not excited about that is you know  
**Translation:** 

**[8291.52s] English:** some of the stuff we've talked about with latency but then a big piece a reason we're not excited  
**Translation:** Vocabulary: isolated: 独立的; latency: 延迟

**[8295.24s] English:** about that is because that comes with giving up a lot of control it's much harder to be really  
**Translation:** 

**[8300.14s] English:** specific when you're talking in the text box and um if you're necessarily just going to communicate  
**Translation:** 

**[8305.66s] English:** with a thing like you would be communicating with an engineering department you're actually  
**Translation:** 

**[8308.38s] English:** abdicating tons of tons of really important decisions um to the spot um and this kind of  
**Translation:** Vocabulary: abdicating: 放弃决策

**[8314.20s] English:** gets at fundamentally what engineering is um i think that some people who are a little bit more  
**Translation:** 

**[8321.14s] English:** removed from engineering might think of it as you know the spec is completely written out and then  
**Translation:** Vocabulary: fundamentally: 从根本上

**[8325.36s] English:** the engineers just come and they just implement and it's just about making the thing happen in  
**Translation:** 

**[8329.76s] English:** code and making the thing um exist um but i think a lot of the the best engineering engineering we  
**Translation:** 

**[8335.82s] English:** enjoy um involves tons of  
**Translation:** 

**[8338.38s] English:** tiny micro decisions about what exactly you're building and about really hard trade-offs between  
**Translation:** 

**[8343.50s] English:** you know speed and cost and just all the other things uh things involved in a system and uh  
**Translation:** 

**[8350.30s] English:** we want as long as humans are actually the ones making you know designing the software and the  
**Translation:** 

**[8355.58s] English:** ones um specifying what they want to be built and it's not just like company run by all ais  
**Translation:** 

**[8360.62s] English:** we think you'll really want the humor the human in a driver's seat um dictating these decisions  
**Translation:** Vocabulary: dictating: 决定; specifying: 规定

**[8366.22s] English:** and so there's the jury's still out on kind of what  
**Translation:** 

**[8368.38s] English:** what that looks like i think that you know one weird idea for what that could look like is it  
**Translation:** 

**[8374.54s] English:** could look like you kind of you can control the level of abstraction you view a code base at  
**Translation:** 

**[8379.74s] English:** and you can point at specific parts of a code base that um may like maybe you digest a code  
**Translation:** Vocabulary: abstraction: 抽象程度

**[8386.38s] English:** base by looking at it in the form of pseudocode and um you can actually edit that pseudocode too  
**Translation:** 

**[8392.46s] English:** and then have changes get me down at the the sort of formal programming level and you keep the like  
**Translation:** Vocabulary: pseudocode: 伪代码

**[8398.38s] English:** you can gesture at any  
**Translation:** 

**[8400.00s] English:** piece of logic in your software component of programming,  
**Translation:** 

**[8404.18s] English:** you keep the inflow text editing component of programming,  
**Translation:** 

**[8407.18s] English:** you keep the control of, you can even go down into the code,  
**Translation:** 

**[8410.10s] English:** you can go at higher levels of abstraction,  
**Translation:** 

**[8412.36s] English:** while also giving you these big productivity gains.  
**Translation:** 

**[8414.70s] English:** It'd be nice if you can go up and down  
**Translation:** 

**[8416.38s] English:** the abstraction stack.  
**Translation:** 

**[8418.30s] English:** Yeah, and there are a lot of details to figure out there  
**Translation:** 

**[8420.26s] English:** that's sort of like a fuzzy idea,  
**Translation:** Vocabulary: fuzzy: 模糊的

**[8421.84s] English:** time will tell if it actually works,  
**Translation:** 

**[8423.26s] English:** but these principles of control and speed  
**Translation:** 

**[8425.82s] English:** in the human and the driver's seat  
**Translation:** 

**[8426.66s] English:** we think are really important.  
**Translation:** 

**[8428.74s] English:** We think for some things, like Arvid mentioned before,  
**Translation:** 

**[8431.14s] English:** for some styles of programming,  
**Translation:** 

**[8432.40s] English:** you can kind of hand it off chatbot style,  
**Translation:** 

**[8434.84s] English:** if you have a bug that's really well specified,  
**Translation:** Vocabulary: specified: 说明详细

**[8436.86s] English:** but that's not most of programming,  
**Translation:** 

**[8439.30s] English:** and that's also not most of the programming  
**Translation:** 

**[8441.84s] English:** we think a lot of people value.  
**Translation:** 

**[8443.50s] English:** What about the fundamental skill of programming?  
**Translation:** 

**[8446.12s] English:** There's a lot of people, young people right now,  
**Translation:** 

**[8449.88s] English:** kind of scared, thinking, because they love programming,  
**Translation:** 

**[8455.30s] English:** but they're scared about, will I be able to have a future  
**Translation:** 

**[8457.68s] English:** if I pursue this career?  
**Translation:** 

**[8458.74s] English:** Do you think the very skill of programming  
**Translation:** 

**[8461.88s] English:** will change fundamentally?  
**Translation:** Vocabulary: fundamentally: 根本上

**[8464.06s] English:** I actually think this is a really, really exciting time  
**Translation:** 

**[8466.64s] English:** to be building software.  
**Translation:** 

**[8468.38s] English:** We remember what programming was like in 2013, 2012,  
**Translation:** 

**[8473.98s] English:** whatever it was, and there was just so much more cruft  
**Translation:** 

**[8479.50s] English:** and boilerplate and looking up something really gnarly,  
**Translation:** 

**[8485.38s] English:** and that stuff still exists, it's definitely not at zero,  
**Translation:** Vocabulary: boilerplate: 标准条款; gnarly: 糟糕的

**[8488.68s] English:** but programming today is way more fun than back then.  
**Translation:** 

**[8492.58s] English:** It's like, we're really getting down  
**Translation:** 

**[8494.26s] English:** to the delight concentration,  
**Translation:** 

**[8496.76s] English:** and all the things that really draw people to programming,  
**Translation:** 

**[8499.58s] English:** like, for instance, this element of being able  
**Translation:** 

**[8501.20s] English:** to build things really fast, and speed,  
**Translation:** 

**[8504.16s] English:** and also individual control,  
**Translation:** 

**[8506.06s] English:** all those are just being turned up a ton.  
**Translation:** 

**[8509.28s] English:** And so I think it's just gonna be,  
**Translation:** 

**[8510.30s] English:** I think it's gonna be a really, really fun time  
**Translation:** 

**[8511.78s] English:** for people who build software.  
**Translation:** 

**[8513.78s] English:** I think that the skills will probably change too.  
**Translation:** 

**[8516.16s] English:** I think that people's taste in creative ideas  
**Translation:** 

**[8518.64s] English:** will be magnified.  
**Translation:** 

**[8520.00s] English:** will be less about maybe less a little bit about boilerplate text editing maybe even a little bit  
**Translation:** 

**[8526.32s] English:** less about carefulness which i think is really important today if you're a programmer i think  
**Translation:** 

**[8531.92s] English:** it'll be a lot more fun what do you guys think i agree i'm i'm very excited to be able to change  
**Translation:** 

**[8537.94s] English:** like just what one thing that that happened recently was like we wanted to do a relatively  
**Translation:** 

**[8545.06s] English:** big migration to our code base we were using async local storage in in no js which is known  
**Translation:** 

**[8550.82s] English:** to be not very performant and we wanted to migrate to a context object and this is a big migration  
**Translation:** Vocabulary: async: 异步; migrate: 迁移

**[8555.34s] English:** and affects the entire code base and sual and i spent i don't know five days uh working through  
**Translation:** 

**[8561.86s] English:** this even with today's ai tools and i am really excited for a future where i can just show a  
**Translation:** 

**[8569.06s] English:** couple of examples and then the ai applies that to all of the locations and then it highlights  
**Translation:** 

**[8575.04s] English:** oh this is a new example like what should i do and then i show exactly what to do there  
**Translation:** 

**[8579.00s] English:** and then that can be done in like 10 minutes and then you can iterate much much faster then you can  
**Translation:** 

**[8585.40s] English:** then you don't have to think as much up front and stay stand at the blackboard and like  
**Translation:** 

**[8590.20s] English:** think exactly like how are we going to do this because the cost is so high but you can just try  
**Translation:** 

**[8594.60s] English:** something first and you realize oh this is not actually exactly what i want and then you can  
**Translation:** 

**[8598.90s] English:** change it instantly again after and so yeah i think being a programmer in the future is  
**Translation:** 

**[8605.04s] English:** going to be a lot of fun yeah i i really like that point about it feels like a lot of the time  
**Translation:** Vocabulary: programmer: 程序员

**[8610.68s] English:** with programming there are two ways you can go about it one is like you think really hard carefully  
**Translation:** 

**[8616.80s] English:** up front about the best possible way to do it and then you spend your limited time of engineering  
**Translation:** 

**[8621.90s] English:** to actually implement it uh but i much prefer just getting in the code and like you know taking a  
**Translation:** 

**[8627.28s] English:** crack at it seeing how it kind of lays out and then iterating really quickly on that that feels  
**Translation:** 

**[8632.96s] English:** more fun um  
**Translation:** 

**[8635.04s] English:** yeah like just speaking to generating the boilerplate is great so you just  
**Translation:** Vocabulary: boilerplate: 标准条款

**[8640.00s] English:** focus on the difficult design nuanced difficult design decisions migration i feel like this is  
**Translation:** 

**[8646.20s] English:** this is a cool one like it seems like larger language models able to basically translate  
**Translation:** Vocabulary: nuanced: 细致入微

**[8651.10s] English:** from one program language to another or like translate like migrate in the general sense of  
**Translation:** 

**[8656.30s] English:** what migrate is um but that's in the current moment so i mean the fear has to do with like  
**Translation:** 

**[8662.54s] English:** okay as these models get better and better then you're doing less and less creative decisions  
**Translation:** 

**[8666.86s] English:** and is it going to kind of move to a place where it's uh you're operating in the design  
**Translation:** 

**[8672.56s] English:** space of natural language where natural language is the main programming language and i guess i  
**Translation:** 

**[8678.02s] English:** could ask that by way of advice like if somebody's interested in programming now what do you think  
**Translation:** 

**[8681.86s] English:** they should learn like to say uh you guys started in some java and uh i forget the oh some php  
**Translation:** 

**[8692.92s] English:** objective c objective c there you go yeah i mean in the  
**Translation:** 

**[8696.84s] English:** end we all know javascript is going to win uh and not typescript is going to be like vanilla  
**Translation:** 

**[8703.84s] English:** javascript it's going to eat the world and maybe a little bit php and i mean it also brings up the  
**Translation:** Vocabulary: vanilla: 原味

**[8709.80s] English:** question of like i think don knuth has a this idea that some percent of the population is geeks  
**Translation:** 

**[8715.96s] English:** and like there's a particular kind of psychology and mind required for programming and it feels  
**Translation:** Vocabulary: geeks: 极客

**[8722.70s] English:** like more and more that expands the kind of person that should be able to can do great  
**Translation:** 

**[8729.44s] English:** programming might expand i think different people do programming for different reasons but i think  
**Translation:** 

**[8736.94s] English:** the true maybe like the best programmers um are the ones that really love  
**Translation:** 

**[8743.16s] English:** just like absolutely love programming for example they're folks on our team  
**Translation:** Vocabulary: programmers: 程序员

**[8747.94s] English:** who literally when they're  
**Translation:** 

**[8752.70s] English:** they get back from work they go and then they boot up cursor and then they start coding on their  
**Translation:** 

**[8760.00s] English:** projects for the entire night and they stay up till 3 a.m doing that um and when they're sad  
**Translation:** 

**[8765.72s] English:** they said i just really need to code and i i think like you know there's there's that level  
**Translation:** 

**[8774.92s] English:** of programmer where like this obsession and love of programming um i think makes really  
**Translation:** 

**[8780.76s] English:** the best programmers and i think these types of people will really get into the details of how  
**Translation:** Vocabulary: obsession: 痴迷; programmer: 程序员

**[8788.10s] English:** things work i guess the question i'm asking that exact program let's think about that person  
**Translation:** 

**[8793.28s] English:** when you're when the super tab the super awesome praise be the tab is succeeds and you keep  
**Translation:** 

**[8800.82s] English:** pressing tab that person in the team loves to curse the tab more than anybody else yeah and  
**Translation:** 

**[8806.10s] English:** it's also not just like like pressing tab is like the just pressing tab that's like the easy way to  
**Translation:** 

**[8811.44s] English:** say it and the catch catchphrase you know uh but what you're actually doing when you're pressing  
**Translation:** 

**[8816.16s] English:** tab is that you're you're injecting  
**Translation:** Vocabulary: catchphrase: 流行语; injecting: 注入

**[8818.10s] English:** intent uh all the time while you're doing it you're you're uh sometimes you're rejecting it  
**Translation:** 

**[8823.38s] English:** sometimes you're typing a few more characters um and and that's the way that you're um you're sort  
**Translation:** 

**[8830.02s] English:** of shaping the things that's being created and i i think programming will change a lot to just  
**Translation:** 

**[8835.82s] English:** what is it that you want to make it's sort of higher bandwidth the communication to the computer  
**Translation:** Vocabulary: bandwidth: 传输速率

**[8840.06s] English:** just becomes higher and higher bandwidth as opposed to like like just typing is much lower  
**Translation:** 

**[8845.26s] English:** bandwidth than than communicating intent i mean there's  
**Translation:** 

**[8848.10s] English:** this goes to your uh manifesto titled engineering genius we are an applied research lab building  
**Translation:** 

**[8856.08s] English:** extraordinary productive human ai systems so speaking to this like hybrid element to start  
**Translation:** Vocabulary: manifesto: 宣言

**[8863.02s] English:** we're building the engineer of the future a human ai programmer that's an order of magnitude more  
**Translation:** 

**[8868.36s] English:** effective than any one engineer this hybrid engineer will have effortless control over  
**Translation:** 

**[8873.40s] English:** their code base and no low entropy keystrokes they will iterate  
**Translation:** 

**[8878.10s] English:** at the speed of their judgment  
**Translation:** Vocabulary: entropy: 信息杂乱; keystrokes: 按键

**[8880.00s] English:** even in the most complex systems.  
**Translation:** 

**[8882.12s] English:** Using a combination of AI and human ingenuity,  
**Translation:** Vocabulary: ingenuity: 聪明才智

**[8885.26s] English:** they will outsmart and out-engineer  
**Translation:** 

**[8887.38s] English:** the best pure AI systems.  
**Translation:** 

**[8889.54s] English:** We are a group of researchers and engineers.  
**Translation:** 

**[8892.14s] English:** We build software and models  
**Translation:** 

**[8893.36s] English:** to invent at the edge of what's useful and what's possible.  
**Translation:** 

**[8896.26s] English:** Our work has already improved the lives  
**Translation:** 

**[8897.90s] English:** of hundreds of thousands of programmers.  
**Translation:** 

**[8901.20s] English:** And on the way to that,  
**Translation:** 

**[8902.62s] English:** we'll at least make programming more fun.  
**Translation:** 

**[8905.00s] English:** So thank you for talking today.  
**Translation:** 

**[8906.72s] English:** Thank you.  
**Translation:** 

**[8907.20s] English:** Thanks for having us.  
**Translation:** 

**[8908.00s] English:** Thank you.  
**Translation:** 

**[8908.28s] English:** Thanks for listening to this conversation  
**Translation:** 

**[8911.24s] English:** with Michael, Swale, Arvid, and Aman.  
**Translation:** 

**[8914.34s] English:** To support this podcast,  
**Translation:** Vocabulary: arvid: 阿维德; swale: 沼泽

**[8915.64s] English:** please check out our sponsors in the description.  
**Translation:** 

**[8918.24s] English:** And now let me leave you with a random,  
**Translation:** Vocabulary: sponsors: 赞助商

**[8921.36s] English:** funny, and perhaps profound programming code  
**Translation:** 

**[8924.58s] English:** I saw on Reddit.  
**Translation:** Vocabulary: profound: 深奥

**[8926.32s] English:** Nothing is as permanent  
**Translation:** 

**[8927.66s] English:** as a temporary solution that works.  
**Translation:** 

**[8932.00s] English:** Thank you for listening,  
**Translation:** 

**[8933.44s] English:** and hope to see you next time.  
**Translation:** 

**[8938.28s] English:** Thank you.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
