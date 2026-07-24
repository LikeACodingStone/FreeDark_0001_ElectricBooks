# Podcast vocabulary notes
Source file: Lex Fridman - Chris Lattner： Future of Programming and AI ｜ Lex Fridman Podcast #381.opus

**[0.00s] English:** On one axis, you have more hardware coming in.  
**Translation:** 

**[1.82s] English:** On the other hand, you have an explosion of innovation in AI.  
**Translation:** 

**[5.46s] English:** And so what happened with both TensorFlow and PyTorch is that the explosion of innovation in AI has led to,  
**Translation:** 

**[11.32s] English:** it's not just about matrix multiplication and convolution.  
**Translation:** Vocabulary: convolution: 卷积; matrix: 矩阵; multiplication: 乘法

**[13.76s] English:** These things have now like 2,000 different operators.  
**Translation:** 

**[17.18s] English:** And on the other hand, you have, I don't know how many pieces of hardware there are out there.  
**Translation:** 

**[20.38s] English:** It's a lot.  
**Translation:** 

**[21.04s] English:** Part of my thesis, part of my belief of where computing goes, if you look out 10 years from now,  
**Translation:** Vocabulary: computing: 计算技术

**[26.24s] English:** is it's not going to get simpler.  
**Translation:** 

**[27.32s] English:** If physics isn't going back to where we came from, it's only going to get weirder from here on out, right?  
**Translation:** 

**[33.52s] English:** And so to me, the exciting part about what we're building is it's about building that universal platform,  
**Translation:** 

**[40.26s] English:** which the world can continue to get weird, because again, I don't think it's avoidable.  
**Translation:** 

**[44.26s] English:** It's physics.  
**Translation:** 

**[45.30s] English:** But we can help lift people's scale, do things with it,  
**Translation:** 

**[48.36s] English:** and they don't have to rewrite their code every time a new device comes out.  
**Translation:** 

**[50.90s] English:** And I think that's pretty cool.  
**Translation:** 

**[54.38s] English:** The following is a conversation with Chris Ladner.  
**Translation:** 

**[57.32s] English:** His third time on this podcast.  
**Translation:** Vocabulary: ladner: 拉德纳

**[59.26s] English:** As I've said many times before, he's one of the most brilliant engineers in modern computing.  
**Translation:** 

**[64.64s] English:** Having created LLM Compiler Infrastructure Project, the Clang Compiler, the Swift Programming Language,  
**Translation:** Vocabulary: clang: clang 编译器

**[70.96s] English:** a lot of key contributions to TensorFlow and TPUs as part of Google.  
**Translation:** 

**[74.30s] English:** He served as Vice President of Autopilot Software at Tesla, was a software innovator and leader at Apple,  
**Translation:** Vocabulary: innovator: 创新者

**[81.92s] English:** and now he co-created a new full-stack AI infrastructure for distribution.  
**Translation:** 

**[87.32s] English:** He has distributed training, inference, and deployment on all kinds of hardware called Modular,  
**Translation:** Vocabulary: deployment: 部署; inference: 推理; modular: 模块化

**[92.50s] English:** and a new programming language called Mojo that is a superset of Python,  
**Translation:** 

**[98.12s] English:** giving you all the usability of Python, but with the performance of C, C++.  
**Translation:** Vocabulary: usability: 易用性

**[103.16s] English:** In many cases, Mojo code has demonstrated over 30,000x speedup over Python.  
**Translation:** 

**[111.56s] English:** If you love machine learning, if you love Python, you should definitely give Mojo a try.  
**Translation:** Vocabulary: speedup: 加速

**[116.36s] English:** This program is a great example of that.  
**Translation:** 

**[117.22s] English:** This programming language, this new AI framework,  
**Translation:** 

**[120.00s] English:** and infrastructure, and this conversation with Chris is mind-blowing. I love it.  
**Translation:** 

**[127.34s] English:** It gets pretty technical at times, so I hope you hang on for the ride. This is the Lex Friedman  
**Translation:** 

**[132.68s] English:** podcast. To support it, please check out our sponsors in the description. And now, dear friends,  
**Translation:** 

**[137.98s] English:** here's Chris Lattner. It's been, I think, two years since we last talked, and in that time,  
**Translation:** Vocabulary: sponsors: 赞助商

**[144.30s] English:** you somehow went and co-created a new programming language called Mojo. So it's optimized for AI.  
**Translation:** 

**[151.80s] English:** It's a superset of Python. Let's look at the big picture. What is the vision for Mojo?  
**Translation:** Vocabulary: optimized: 优化

**[157.60s] English:** For Mojo? Well, I think you have to zoom out. I've been working on a lot of related technologies for  
**Translation:** 

**[163.38s] English:** many, many years. I've worked on LLVM and a lot of things, and mobile, and servers, and things like  
**Translation:** 

**[169.20s] English:** this. But the world's changing, and what's happened with AI is we have new GPUs and new  
**Translation:** 

**[174.30s] English:** machine learning accelerators and other ASICs and things like that that make AI go real fast.  
**Translation:** Vocabulary: accelerators: 加速器

**[180.74s] English:** At Google, I worked on TPUs. That's one of the biggest, larger-scale deployed systems that exist  
**Translation:** 

**[185.52s] English:** for AI. And really what you see is if you look across all of the things that are happening in  
**Translation:** Vocabulary: deployed: 部署

**[190.44s] English:** the industry, there's this new compute platform coming. And it's not just about CPUs, or GPUs,  
**Translation:** 

**[196.22s] English:** or TPUs, or NPUs, or IPUs, or whatever, all the PUs. It's about how do we program these things?  
**Translation:** 

**[204.30s] English:** For software folks like us, it doesn't do us any good if there's this amazing hardware that we  
**Translation:** 

**[209.80s] English:** can't use. And one of the things you find out really quick is that having the theoretical  
**Translation:** 

**[214.94s] English:** capability of programming something, and then having the world's power and the innovation of  
**Translation:** 

**[220.14s] English:** all the smart people in the world get unleashed on something can be quite different. And so really  
**Translation:** Vocabulary: capability: 能力; unleashed: 释放

**[225.74s] English:** where Mojo came from was starting from a problem of we need to be able to take machine learning,  
**Translation:** 

**[231.02s] English:** take the infrastructure underneath it, and make it way more accessible, way more,  
**Translation:** 

**[234.30s] English:** usable, way more understandable by normal people and researchers and other folks that are not  
**Translation:** 

**[239.38s] English:** themselves.  
**Translation:** Vocabulary: understandable: 容易理解; usable: 可用

**[240.00s] English:** of, like, experts in GPUs and things like this.  
**Translation:** 

**[242.44s] English:** And then through that journey, we realized, hey, we need syntax for this.  
**Translation:** Vocabulary: syntax: 语法规则

**[245.90s] English:** We need to do a programming language.  
**Translation:** 

**[247.36s] English:** So one of the main features of the language, I say so fully in jest,  
**Translation:** 

**[252.32s] English:** is that it allows you to have the file extension to be an emoji or the fire emoji,  
**Translation:** 

**[260.12s] English:** which is one of the first emojis used as a file extension I've ever seen in my life.  
**Translation:** 

**[267.10s] English:** And then you ask yourself the question, why in the 21st century are we not using Unicode for file extensions?  
**Translation:** 

**[274.64s] English:** I mean, it's an epic decision.  
**Translation:** Vocabulary: extensions: 文件扩展名

**[276.48s] English:** I think clearly the most important decision you made, but you could also just use MOJO as the file extension.  
**Translation:** 

**[282.28s] English:** Well, so, okay, so take a step back.  
**Translation:** 

**[283.88s] English:** I mean, come on, Lex, do you think that the world's ready for this?  
**Translation:** 

**[285.80s] English:** This is a big moment in the world, right?  
**Translation:** 

**[287.82s] English:** We're releasing this onto the world.  
**Translation:** 

**[289.42s] English:** This is innovation.  
**Translation:** 

**[291.60s] English:** I mean, it really is kind of brilliant.  
**Translation:** 

**[293.80s] English:** Emojis are such a big part of our daily lives.  
**Translation:** 

**[297.10s] English:** Why is it not in programming?  
**Translation:** 

**[300.18s] English:** Well, and, like, you take a step back and look at what file extensions are, right?  
**Translation:** 

**[304.66s] English:** They're basically metadata, right?  
**Translation:** 

**[306.56s] English:** And so why are we spending all the screen space on them and all this stuff?  
**Translation:** Vocabulary: metadata: 元数据

**[309.74s] English:** Also, you know, you have them stacked up next to text files and PDF files and whatever else.  
**Translation:** 

**[313.86s] English:** Like, if you're going to do something cool, you want it to stand out, right?  
**Translation:** 

**[316.62s] English:** Emojis are colorful.  
**Translation:** 

**[317.72s] English:** They're visual.  
**Translation:** 

**[318.58s] English:** They're beautiful, right?  
**Translation:** 

**[319.94s] English:** What's been the response so far from, is there support on, like, Windows on operating systems in displaying, like, File Explorer?  
**Translation:** Vocabulary: explorer: 资源管理器

**[326.64s] English:** Yeah.  
**Translation:** 

**[327.10s] English:** The one problem I've seen is that Git doesn't escape it right.  
**Translation:** 

**[331.48s] English:** And so it thinks that the Fire Emoji is unprintable, and so it, like, prints out weird hex things if you use the command line Git tool.  
**Translation:** 

**[337.10s] English:** But everything else, as far as I'm aware, works fine.  
**Translation:** 

**[339.54s] English:** And I have faith that Git can be improved.  
**Translation:** 

**[341.82s] English:** And so GitHub is fine.  
**Translation:** 

**[343.96s] English:** GitHub is fine.  
**Translation:** 

**[344.86s] English:** Yep.  
**Translation:** 

**[345.28s] English:** GitHub is fine.  
**Translation:** 

**[346.18s] English:** Visual Studio Code, Windows, like, all this stuff, totally ready.  
**Translation:** 

**[349.30s] English:** Because people have internationalization in their normal part of their paths.  
**Translation:** 

**[354.24s] English:** So this is just, like, taking the next step, right?  
**Translation:** 

**[355.80s] English:** Somewhere between, oh, wow, that makes sense.  
**Translation:** 

**[359.42s] English:** Cool.  
**Translation:** 

**[360.00s] English:** i like new things too oh my god you're killing my baby like what are you talking about this can  
**Translation:** 

**[364.72s] English:** never be like i can never handle this how am i going to type this like all these things and so  
**Translation:** 

**[369.76s] English:** this is something where i think that the world will get there we don't have to bet  
**Translation:** 

**[373.36s] English:** the whole farm on this i think we can provide both paths but i think it'll be great uh when can we  
**Translation:** 

**[379.36s] English:** have emojis as part of the code i wonder uh yeah so i mean lots of languages provide that so um i  
**Translation:** 

**[384.96s] English:** think that we have partial support for that it's probably not fully done yet but but yeah you can  
**Translation:** 

**[389.52s] English:** you can do that for example in swift you can do that for sure so an example we give david apple  
**Translation:** 

**[394.88s] English:** was the the dog cow yeah so that's a classical mac heritage thing and so you use the dog and the cow  
**Translation:** 

**[400.88s] English:** emoji together and that could be your variable name but of course the internet went and made  
**Translation:** 

**[404.72s] English:** pile of poop for everything yeah so you know if you want to name your function pile of poop then  
**Translation:** 

**[409.60s] English:** you can totally go to town and see how that gets through code review  
**Translation:** 

**[414.16s] English:** okay so uh let me just ask a bunch of random questions uh so is  
**Translation:** 

**[419.12s] English:** moji  
**Translation:** 

**[419.52s] English:** joe primarily designed for ai's or is it a general purpose programming yeah good question  
**Translation:** 

**[424.24s] English:** so it's ai first and so ai is driving a lot of the requirements and so um modular is building and  
**Translation:** 

**[431.28s] English:** designing and driving mojo forward and it's not because it's an interesting project theoretically  
**Translation:** Vocabulary: modular: 模块化; theoretically: 理论上

**[436.00s] English:** to build it's because we need it and so at modular we're really tackling the ai infrastructure  
**Translation:** 

**[442.48s] English:** landscape and the big problems in ai and the reasons that it is so difficult to use and scale  
**Translation:** Vocabulary: tackling: 应对

**[446.96s] English:** and adopt and deploy and like all these  
**Translation:** 

**[449.52s] English:** big problems in ai and so we're coming at it from that perspective now when you do that  
**Translation:** Vocabulary: deploy: 部署

**[454.72s] English:** when you start tackling these problems you realize that the um solution to these problems isn't  
**Translation:** 

**[460.64s] English:** actually an ai specific solution and so while we're doing this we're building mojo to be a  
**Translation:** 

**[464.80s] English:** fully general programming language and that means that you can uh obviously tackle gpus  
**Translation:** 

**[470.40s] English:** and cpus and like these ai things but it's also a really great way to build  
**Translation:** 

**[474.64s] English:** numpy and other things like that or you know just if you look at what many python library  
**Translation:** 

**[479.52s] English:** are today.  
**Translation:** 

**[480.00s] English:** Often they're a layer of Python for the API, and they end up being C and C++ code underneath them.  
**Translation:** 

**[485.70s] English:** That's very true in AI.  
**Translation:** 

**[487.30s] English:** That's true in lots of other domains as well.  
**Translation:** 

**[489.28s] English:** And so anytime you see this pattern, that's an opportunity for Mojo to help simplify the world and help people have one thing.  
**Translation:** Vocabulary: anytime: 任何时候; simplify: 简化

**[495.78s] English:** To optimize through simplification by having one thing.  
**Translation:** 

**[500.40s] English:** So you mentioned modular.  
**Translation:** Vocabulary: optimize: 优化; simplification: 简化

**[501.98s] English:** Mojo is the programming language.  
**Translation:** 

**[503.30s] English:** Modular is the whole software stack.  
**Translation:** 

**[505.60s] English:** So just over a year ago, we started this company called Modular.  
**Translation:** 

**[508.12s] English:** Yeah.  
**Translation:** 

**[508.48s] English:** What Modular is about is it's about taking AI and up-leveling it into the next generation.  
**Translation:** 

**[514.38s] English:** And so if you take a step back, what's gone on in the last five, six, seven, eight years is that we've had things like TensorFlow and PyTorch and these other systems come in.  
**Translation:** 

**[524.78s] English:** You've used them.  
**Translation:** 

**[525.38s] English:** You know this.  
**Translation:** 

**[526.38s] English:** And what's happened is these things have grown like crazy.  
**Translation:** 

**[529.68s] English:** They get tons of users.  
**Translation:** 

**[530.98s] English:** It's in production deployment scenarios.  
**Translation:** 

**[533.08s] English:** It's being used to power so many systems.  
**Translation:** Vocabulary: deployment: 部署; scenarios: 场景

**[535.44s] English:** I mean, AI is all around us now.  
**Translation:** 

**[537.48s] English:** It used to be controversial.  
**Translation:** 

**[538.48s] English:** It used to be controversial years ago, but now it's a thing.  
**Translation:** 

**[541.32s] English:** But the challenge with these systems is that they haven't always been thought out with current demands in mind.  
**Translation:** 

**[549.06s] English:** And so you think about it, where were LLMs eight years ago?  
**Translation:** 

**[553.26s] English:** Well, they didn't exist, right?  
**Translation:** 

**[554.74s] English:** AI has changed so much.  
**Translation:** 

**[556.20s] English:** And a lot of what people are doing today are very different than when these systems were built.  
**Translation:** 

**[560.06s] English:** And meanwhile, the hardware side of this has gotten into a huge mess.  
**Translation:** 

**[563.04s] English:** There's tons of new chips and accelerators, and every big company is announcing a new chip every day, it feels like.  
**Translation:** Vocabulary: accelerators: 加速器

**[568.52s] English:** So between that, you have this one moving system on one side, a moving system on the other side, and it just turns into this gigantic mess, which makes it very difficult for people to actually use AI, particularly in production deployment scenarios.  
**Translation:** 

**[582.38s] English:** And so what Modular is doing is we're helping build out that software stack to help solve some of those problems, so then people can be more productive and get more AI research into production.  
**Translation:** Vocabulary: gigantic: 巨大的; modular: 模块化的

**[591.02s] English:** Now, what Mojo does is it's a really, really, really important piece of that.  
**Translation:** 

**[595.26s] English:** And so that is part of that engine and part of the technology.  
**Translation:** 

**[597.22s] English:** That's what it's doing.  
**Translation:** 

**[597.60s] English:** And I think that's where the technology is going.  
**Translation:** 

**[597.86s] English:** Need help?  
**Translation:** 

**[597.96s] English:** Yeah.  
**Translation:** 

**[598.10s] English:** It's really good.  
**Translation:** 

**[598.38s] English:** So yeah.  
**Translation:** 

**[598.48s] English:** allows us to solve this problem.  
**Translation:** 

**[600.68s] English:** So Mojo is a programming language that allows you to do the high-level programming, the low-level programming.  
**Translation:** 

**[607.90s] English:** They do all kinds of programming in that spectrum that gets you closer and closer to the hardware.  
**Translation:** 

**[614.10s] English:** So take a step back.  
**Translation:** 

**[614.78s] English:** So, Lex, what do you love about Python?  
**Translation:** 

**[616.98s] English:** Oh, boy.  
**Translation:** 

**[618.42s] English:** Where do I begin?  
**Translation:** 

**[620.86s] English:** What is love?  
**Translation:** 

**[622.14s] English:** What do I love about Python?  
**Translation:** 

**[623.66s] English:** You're a guy who knows love.  
**Translation:** 

**[624.74s] English:** I know this.  
**Translation:** 

**[625.26s] English:** Yes.  
**Translation:** 

**[627.20s] English:** How intuitive it is.  
**Translation:** 

**[630.00s] English:** How it feels like I'm writing natural language English.  
**Translation:** Vocabulary: intuitive: 直观的

**[636.00s] English:** How when I can not just write, but read other people's code, somehow I can understand it faster.  
**Translation:** 

**[642.24s] English:** It's more condensed than other languages, like ones I'm really familiar with, like C++ and C.  
**Translation:** Vocabulary: condensed: 浓缩的

**[650.94s] English:** There's a bunch of sexy little features.  
**Translation:** 

**[653.62s] English:** Yeah.  
**Translation:** 

**[654.82s] English:** We'll probably talk about some of them, but list comprehensions and stuff like this.  
**Translation:** 

**[658.90s] English:** And don't forget the entire ecosystem of all the packages.  
**Translation:** Vocabulary: comprehensions: 理解

**[663.08s] English:** Oh, yeah.  
**Translation:** 

**[663.38s] English:** That's probably huge.  
**Translation:** 

**[664.52s] English:** Because there's always something.  
**Translation:** 

**[665.42s] English:** If you want to do anything, there's always a package.  
**Translation:** 

**[667.84s] English:** Yeah.  
**Translation:** 

**[668.14s] English:** So it's not just the ecosystem of the packages and the ecosystem of the humans that do it.  
**Translation:** 

**[674.40s] English:** That's an interesting dynamic.  
**Translation:** 

**[677.54s] English:** That's huge.  
**Translation:** 

**[678.00s] English:** I think something about the usability and the ecosystem makes the thing viral.  
**Translation:** 

**[684.16s] English:** It grows, and then it's a virtuous cycle, I think.  
**Translation:** Vocabulary: usability: 易用性; viral: 病毒式传播; virtuous: 良性循环

**[687.08s] English:** Well, and there's many things that went into that.  
**Translation:** 

**[688.90s] English:** I think that ML was very good for Python.  
**Translation:** 

**[691.42s] English:** And so I think that TensorFlow and PyTorch and these systems embracing Python really took and helped Python grow.  
**Translation:** 

**[698.00s] English:** But I think that the major thing underlying it is that Python's like the universal connector.  
**Translation:** Vocabulary: connector: 连接器; embracing: 接纳

**[703.30s] English:** It really helps bring together lots of different systems so you can compose them and build out larger systems without having to understand how it works.  
**Translation:** 

**[710.36s] English:** But then what is the problem with Python?  
**Translation:** 

**[713.16s] English:** Well, I guess you could say several things, but probably that it's slow.  
**Translation:** 

**[716.96s] English:** I think that's usually what people complain about.  
**Translation:** 

**[719.28s] English:** Right.  
**Translation:** 

**[719.38s] English:** And so...  
**Translation:** 

**[720.00s] English:** So, I mean, other people complain about tabs and spaces versus curly braces or whatever, but, I mean, those people are just wrong because it is actually just better to use indentation.  
**Translation:** 

**[731.12s] English:** Wow, strong words.  
**Translation:** Vocabulary: braces: 花括号; indentation: 缩进

**[732.90s] English:** So, actually, on a small tangent, let's actually take that.  
**Translation:** 

**[735.80s] English:** Let's take all kinds of tangents.  
**Translation:** Vocabulary: tangent: 旁枝话题; tangents: 旁支话题

**[737.36s] English:** Oh, come on, Lex.  
**Translation:** 

**[737.96s] English:** You can push me on it.  
**Translation:** 

**[738.76s] English:** I can take it.  
**Translation:** 

**[739.20s] English:** Design.  
**Translation:** 

**[740.92s] English:** Listen, I've recently left Emacs for VS Code.  
**Translation:** 

**[744.18s] English:** Okay.  
**Translation:** Vocabulary: emacs: 编辑器

**[744.36s] English:** The kind of hate mail I had to receive because on the way to doing that, I also said I've considered Vim and chose not to and went with VS Code.  
**Translation:** 

**[753.84s] English:** You're touching on deep religions, right?  
**Translation:** 

**[756.46s] English:** Anyway, tabs is an interesting design decision, and so you've really written a new programming language here.  
**Translation:** 

**[762.98s] English:** Yes, it is a superset of Python, but you can make a bunch of different interesting decisions here.  
**Translation:** 

**[768.12s] English:** Totally, yeah.  
**Translation:** 

**[768.68s] English:** And you chose, actually, to stick with Python in terms of some of the syntax.  
**Translation:** Vocabulary: syntax: 语法规则

**[774.36s] English:** Well, so let me explain why, right?  
**Translation:** 

**[776.96s] English:** So, I mean, you can explain this in many rational ways.  
**Translation:** 

**[782.48s] English:** I think that the indentation is beautiful, but that's not a rational explanation, right?  
**Translation:** 

**[786.80s] English:** But I can defend it rationally, right?  
**Translation:** 

**[788.32s] English:** So, first of all, Python 1 has millions of programmers.  
**Translation:** 

**[792.64s] English:** It's huge.  
**Translation:** Vocabulary: programmers: 程序员

**[793.32s] English:** It's everywhere.  
**Translation:** 

**[793.86s] English:** It owns machine learning, right?  
**Translation:** 

**[795.06s] English:** So, factually, it is the thing, right?  
**Translation:** 

**[798.34s] English:** Second of all, if you look at it, C code, C++ code, Java, whatever, Swift, curly brace languages.  
**Translation:** Vocabulary: brace: 花括号

**[804.36s] English:** Also, run through formatting tools and get indented.  
**Translation:** 

**[808.90s] English:** And so, if they're not indented correctly, first of all, it will twist your brain around.  
**Translation:** Vocabulary: formatting: 排版; indented: 缩进

**[813.86s] English:** It can lead to bugs.  
**Translation:** 

**[815.14s] English:** There's notorious bugs that have happened across time where the indentation was wrong or misleading, and it wasn't formatted right.  
**Translation:** Vocabulary: formatted: 格式正确

**[821.20s] English:** And so, it turned into an issue, right?  
**Translation:** 

**[823.56s] English:** And so, what ends up happening in modern, large-scale code bases is people run automatic formatters.  
**Translation:** Vocabulary: formatters: 自动格式化工具

**[828.92s] English:** So, now what you end up with is indentation and curly braces.  
**Translation:** 

**[833.24s] English:** Well, if you're going to have...  
**Translation:** 

**[834.36s] English:** You know, the notion of grouping, why not have one thing?  
**Translation:** 

**[840.00s] English:** right and get rid of all the clutter and have a more beautiful thing right also you look at many  
**Translation:** Vocabulary: clutter: 杂乱; grouping: 分类

**[843.36s] English:** of these languages it's like okay well you can have curly braces or you can omit them if there's  
**Translation:** 

**[847.36s] English:** one statement or you just like enter this entire world of complicated design space that objectively  
**Translation:** Vocabulary: objectively: 客观地

**[852.56s] English:** you don't need if you have python style indentation so yeah i would love to actually see statistics on  
**Translation:** 

**[857.44s] English:** errors made because of indentation like how many errors are made in python versus in c plus plus  
**Translation:** Vocabulary: indentation: 缩进

**[863.44s] English:** that have to do with basic formatting all that kind of stuff i would love to see i think it's  
**Translation:** 

**[867.76s] English:** probably pretty minor because once you get uh like you use vs code i do too so if you get vs  
**Translation:** 

**[872.88s] English:** code set up it does the indentation for you generally right and so you don't you know it's  
**Translation:** 

**[876.64s] English:** actually really nice to not have to fight it and then what you can see is the editor is telling you  
**Translation:** 

**[881.84s] English:** how your code will work by indenting it which i think is pretty cool i honestly don't think  
**Translation:** 

**[887.76s] English:** i've ever i don't remember having an error in python because i indented stuff wrong so i mean  
**Translation:** Vocabulary: indenting: 缩进

**[893.84s] English:** i think that there's again this is a religious thing and so i can joke about it and i love  
**Translation:** 

**[897.76s] English:** i love to kind of you know i realize that this is such a polarizing thing and everybody wants to  
**Translation:** Vocabulary: polarizing: 引起争议的

**[903.28s] English:** argue about it and so i like poking at the bear a little bit right but but frankly right come back  
**Translation:** 

**[908.80s] English:** to the first point python one like it's huge it's an ai um it's the right thing for us like we see  
**Translation:** Vocabulary: poking: 戳一下

**[914.00s] English:** mojo as being an incredible part of the python ecosystem we're not looking to break python or  
**Translation:** 

**[918.88s] English:** change it or quote unquote fix it we love python for what it is our view is that python is just  
**Translation:** Vocabulary: unquote: 引号

**[924.56s] English:** not done yet and so if you look at you know you mentioned python it's just not done yet  
**Translation:** 

**[927.76s] English:** python being slow well there's a couple of different things that go into that which we  
**Translation:** 

**[930.48s] English:** can talk about if you want but one of them is it just doesn't have those features that you would  
**Translation:** 

**[934.80s] English:** use to do c-like programming and so if you say okay well i'm forced out of python into c for  
**Translation:** 

**[940.96s] English:** certain use cases well then what we're doing is we're saying okay well why why is that can we  
**Translation:** 

**[945.92s] English:** just add those features that are missing from python back up to mojo and then you can have  
**Translation:** 

**[950.72s] English:** everything that's great about python all the things you're talking about that you love  
**Translation:** 

**[954.08s] English:** plus not be forced out of it when you do something a little bit  
**Translation:** 

**[957.76s] English:** more computationally intense or weird or  
**Translation:** 

**[960.00s] English:** or hardware-y, or whatever it is that you're doing.  
**Translation:** Vocabulary: computationally: 计算上

**[962.96s] English:** Well, a million questions I want to ask,  
**Translation:** 

**[965.08s] English:** but high level again, is it compiled  
**Translation:** Vocabulary: compiled: 汇编而成

**[967.28s] English:** or is it an interpretive language?  
**Translation:** 

**[968.48s] English:** So Python is just-in-time compilation.  
**Translation:** Vocabulary: compilation: 编译; interpretive: 解释型

**[971.18s] English:** What's Mojo?  
**Translation:** 

**[973.92s] English:** So Mojo, the complicated answer,  
**Translation:** 

**[975.48s] English:** does all the things.  
**Translation:** 

**[976.84s] English:** So it's interpreted, it's JIT compiled,  
**Translation:** Vocabulary: interpreted: 解释执行

**[978.38s] English:** and it's statically compiled.  
**Translation:** 

**[981.68s] English:** And so this is for a variety of reasons.  
**Translation:** Vocabulary: statically: 静态地

**[984.12s] English:** So one of the things that makes Python beautiful  
**Translation:** 

**[986.96s] English:** is that it's very dynamic.  
**Translation:** 

**[989.36s] English:** And because it's dynamic, one of the things they added  
**Translation:** 

**[992.16s] English:** is that it has this powerful metaprogramming feature.  
**Translation:** Vocabulary: metaprogramming: 元编程

**[995.10s] English:** And so if you look at something like PyTorch,  
**Translation:** 

**[997.04s] English:** or TensorFlow, or even a simple use case,  
**Translation:** 

**[1001.52s] English:** like you define a class that has the plus method.  
**Translation:** 

**[1005.46s] English:** You can overload the dunder methods,  
**Translation:** Vocabulary: dunder: 双下划线方法

**[1007.22s] English:** like dunder add, for example,  
**Translation:** 

**[1008.80s] English:** and then the plus method works on your class.  
**Translation:** 

**[1011.02s] English:** And so it has very nice and very expressive  
**Translation:** 

**[1013.54s] English:** dynamic metaprogramming features.  
**Translation:** Vocabulary: expressive: 富有表现力的

**[1016.76s] English:** In Mojo, we want all those features to come in.  
**Translation:** 

**[1018.80s] English:** Like, we don't want to break down all those features.  
**Translation:** 

**[1019.34s] English:** Like Python, we want it all to work.  
**Translation:** 

**[1020.84s] English:** But the problem is you can't run those super dynamic features  
**Translation:** 

**[1024.06s] English:** on an embedded processor, or on a GPU, right?  
**Translation:** 

**[1029.02s] English:** Or if you could, you probably don't want to  
**Translation:** 

**[1030.76s] English:** just because of the performance.  
**Translation:** 

**[1031.96s] English:** And so we entered this question of saying,  
**Translation:** 

**[1034.68s] English:** okay, how do you get the power of this dynamic metaprogramming  
**Translation:** 

**[1038.88s] English:** into a language that has to be super efficient  
**Translation:** 

**[1041.80s] English:** in specific cases?  
**Translation:** 

**[1043.14s] English:** And so what we did was we said,  
**Translation:** 

**[1044.32s] English:** okay, we'll take that interpreter.  
**Translation:** 

**[1045.88s] English:** Python has an interpreter in it, right?  
**Translation:** Vocabulary: interpreter: 解释器

**[1048.02s] English:** Take that interpreter and allow it  
**Translation:** 

**[1049.12s] English:** to run at compile time.  
**Translation:** 

**[1051.46s] English:** And so now what you get is you get compile time metaprogramming.  
**Translation:** 

**[1054.40s] English:** And so this is super interesting and super powerful  
**Translation:** 

**[1056.58s] English:** because one of the big advantages you get  
**Translation:** 

**[1059.32s] English:** is you get Python-style expressive APIs.  
**Translation:** 

**[1062.12s] English:** You get the ability to have overloaded operators.  
**Translation:** 

**[1065.02s] English:** And if you look at what happens inside of like PyTorch,  
**Translation:** Vocabulary: overloaded: 重载的

**[1067.36s] English:** for example, with automatic differentiation  
**Translation:** 

**[1069.34s] English:** and eager mode and like all these things,  
**Translation:** Vocabulary: differentiation: 求导

**[1071.08s] English:** they're using these really dynamic  
**Translation:** 

**[1072.66s] English:** and powerful features at runtime.  
**Translation:** Vocabulary: runtime: 运行时

**[1074.70s] English:** But we can take those features and lift them  
**Translation:** 

**[1076.48s] English:** so that they run at compile time.  
**Translation:** 

**[1078.24s] English:** So you're...  
**Translation:** 

**[1079.12s] English:** Because if you pass pass  
**Translation:** 

**[1080.00s] English:** of metaprogramming with templates, but it's really messy.  
**Translation:** 

**[1085.36s] English:** It's super messy.  
**Translation:** Vocabulary: templates: 模板

**[1086.50s] English:** It's always, it was accidentally, I mean,  
**Translation:** 

**[1089.66s] English:** different people have different interpretations.  
**Translation:** Vocabulary: interpretations: 解释

**[1091.50s] English:** My interpretation is that it was made accidentally powerful.  
**Translation:** 

**[1094.40s] English:** It was not designed to be Turing-complete, for example,  
**Translation:** 

**[1097.70s] English:** but that was discovered kind of along the way, accidentally.  
**Translation:** 

**[1101.14s] English:** And so there have been a number of languages in the space,  
**Translation:** 

**[1104.40s] English:** and so they usually have templates or code instantiation,  
**Translation:** 

**[1107.88s] English:** code copying features of various sorts.  
**Translation:** Vocabulary: instantiation: 实例化

**[1110.78s] English:** Some more modern languages or some more newer languages, let's say,  
**Translation:** 

**[1114.38s] English:** like, you know, they're fairly unknown, like Zig, for example, says,  
**Translation:** 

**[1120.20s] English:** okay, well, let's take all of those types that you can run it,  
**Translation:** 

**[1123.80s] English:** all those things you can do at runtime,  
**Translation:** 

**[1125.40s] English:** and allow them to happen at compile time.  
**Translation:** 

**[1128.24s] English:** And so one of the problems with C++, I mean,  
**Translation:** 

**[1131.16s] English:** which is one of the problems with C++ is...  
**Translation:** 

**[1134.20s] English:** There we go.  
**Translation:** 

**[1134.96s] English:** Wrong words.  
**Translation:** 

**[1135.88s] English:** We're going to offend everybody today.  
**Translation:** 

**[1137.06s] English:** Oh, it's okay.  
**Translation:** 

**[1137.80s] English:** I mean, everybody hates me for a variety of reasons anyways.  
**Translation:** 

**[1139.78s] English:** I'm sure, right?  
**Translation:** 

**[1141.40s] English:** I've written enough...  
**Translation:** 

**[1142.34s] English:** It's just the way they show love.  
**Translation:** 

**[1143.44s] English:** I have written enough C++ code to earn a little bit of grumpiness with C++.  
**Translation:** Vocabulary: grumpiness: 爱发牢骚

**[1147.56s] English:** But one of the problems with it is that the metaprogramming system templates  
**Translation:** 

**[1152.36s] English:** is just a completely different universe from the normal runtime programming world.  
**Translation:** Vocabulary: metaprogramming: 元编程

**[1158.26s] English:** And so if you do metaprogramming and programming,  
**Translation:** 

**[1160.32s] English:** it's just like a different universe, different syntax, different concepts,  
**Translation:** Vocabulary: syntax: 语法规则

**[1163.78s] English:** different stuff going on.  
**Translation:** 

**[1164.76s] English:** And so, again, one of our goals with Mojo is to make things really easy to use,  
**Translation:** 

**[1168.92s] English:** easy to learn,  
**Translation:** 

**[1169.72s] English:** and so there's a natural stepping stone.  
**Translation:** 

**[1172.78s] English:** And so as you do this, you say,  
**Translation:** 

**[1173.94s] English:** okay, well, I have to do programming at runtime.  
**Translation:** 

**[1176.46s] English:** I have to do programming at compile time.  
**Translation:** 

**[1179.06s] English:** Why are these different things?  
**Translation:** 

**[1181.22s] English:** How hard is that to pull it off?  
**Translation:** 

**[1182.38s] English:** Because that sounds, to me as a fan of metaprogramming in C++ even,  
**Translation:** 

**[1187.06s] English:** how hard is it to pull that off?  
**Translation:** 

**[1189.00s] English:** That sounds really, really exciting  
**Translation:** 

**[1190.38s] English:** because you can do the same style of programming at compile time and at runtime.  
**Translation:** 

**[1194.18s] English:** That's really, really exciting.  
**Translation:** Vocabulary: runtime: 运行时

**[1195.88s] English:** And so, I mean, in terms of the compiler implementation details,  
**Translation:** 

**[1198.90s] English:** it's hard.  
**Translation:** Vocabulary: implementation: 实现细节

**[1199.72s] English:** Yeah.  
**Translation:** 

**[1200.00s] English:** I won't be shy about that.  
**Translation:** 

**[1201.88s] English:** It's super hard.  
**Translation:** 

**[1202.98s] English:** It requires, I mean, what Mojo has underneath the covers  
**Translation:** 

**[1205.66s] English:** is a completely new approach to the design of the compiler itself.  
**Translation:** 

**[1209.20s] English:** And so this builds on these technologies like MLIR that you mentioned,  
**Translation:** 

**[1212.98s] English:** but it also includes other, like, caching and other interpreters  
**Translation:** 

**[1217.22s] English:** and JIT compilers and other stuff like that.  
**Translation:** Vocabulary: caching: 缓存; compilers: 编译器; interpreters: 解释器

**[1219.22s] English:** So you have, like, an interpreter inside the compiler.  
**Translation:** 

**[1220.62s] English:** Within the compiler, yes.  
**Translation:** Vocabulary: interpreter: 解释器

**[1222.96s] English:** And so it really takes the standard model of programming languages  
**Translation:** 

**[1227.92s] English:** and kind of twists it and unifies it with the runtime model,  
**Translation:** 

**[1232.14s] English:** which I think is really cool.  
**Translation:** 

**[1234.12s] English:** And to me, the value of that is that, again,  
**Translation:** 

**[1236.26s] English:** many of these languages have metaprogramming features.  
**Translation:** 

**[1238.18s] English:** Like, they grow macros or something.  
**Translation:** Vocabulary: macros: 宏

**[1240.18s] English:** Lisp, right?  
**Translation:** 

**[1241.70s] English:** Yes.  
**Translation:** 

**[1242.26s] English:** I know your roots, right?  
**Translation:** 

**[1244.32s] English:** You know, and this is a powerful thing, right?  
**Translation:** 

**[1246.70s] English:** And so, you know, if you go back to Lisp,  
**Translation:** 

**[1248.38s] English:** one of the most powerful things about it is that it said that  
**Translation:** 

**[1250.98s] English:** the metaprogramming and the programming are the same, right?  
**Translation:** 

**[1254.06s] English:** And so that made it way simpler, way more consistent,  
**Translation:** 

**[1256.56s] English:** way easier to understand and reason about.  
**Translation:** 

**[1258.04s] English:** And it made it more composable.  
**Translation:** 

**[1259.78s] English:** So if you build a library, you can use it both at runtime and compile time,  
**Translation:** 

**[1263.40s] English:** which is pretty cool.  
**Translation:** 

**[1264.44s] English:** Yeah.  
**Translation:** 

**[1264.68s] English:** And for machine learning, I think metaprogramming,  
**Translation:** 

**[1267.18s] English:** I think we could generally say, is extremely useful.  
**Translation:** 

**[1271.88s] English:** And so you get features.  
**Translation:** 

**[1273.42s] English:** I mean, I'll jump around, but there's the feature of auto-tuning  
**Translation:** 

**[1276.90s] English:** and adaptive compilation just blows my mind.  
**Translation:** Vocabulary: adaptive: 自适应; compilation: 编译

**[1280.84s] English:** Well, so, okay, so let's come back to that.  
**Translation:** 

**[1282.26s] English:** All right.  
**Translation:** 

**[1282.82s] English:** So what is machine learning?  
**Translation:** 

**[1285.14s] English:** Or what is a machine learning model?  
**Translation:** 

**[1286.42s] English:** Like, you take a PyTorch model off there,  
**Translation:** 

**[1287.94s] English:** and then, right, it's really interesting to me  
**Translation:** 

**[1290.32s] English:** because what PyTorch and what TensorFlow and all these frameworks  
**Translation:** 

**[1293.64s] English:** are kind of pushing compute into  
**Translation:** 

**[1295.56s] English:** is they're pushing into, like, this abstract specification  
**Translation:** 

**[1298.76s] English:** of a compute problem,  
**Translation:** Vocabulary: specification: 规范说明

**[1300.90s] English:** which then gets mapped in a whole bunch of different ways, right?  
**Translation:** 

**[1303.38s] English:** And so this is why it became a metaprogramming problem,  
**Translation:** Vocabulary: metaprogramming: 元编程

**[1305.36s] English:** is that you want to be able to say,  
**Translation:** 

**[1306.92s] English:** cool, I have this neural net.  
**Translation:** 

**[1308.74s] English:** Now run it with batch size 1,000, right?  
**Translation:** 

**[1311.46s] English:** Do a mapping across batch.  
**Translation:** 

**[1314.46s] English:** Or, okay, I want to take this problem,  
**Translation:** 

**[1316.08s] English:** now run it across 1,000 CPUs.  
**Translation:** 

**[1318.30s] English:** Or GPUs, right?  
**Translation:** 

**[1319.64s] English:** And so...  
**Translation:** 

**[1320.00s] English:** Like, this problem of, like, describe the compute and then map it and do things and transform it are, like, actually it's very profound, and that's one of the things that makes machine learning systems really special.  
**Translation:** 

**[1332.00s] English:** Maybe can you describe auto-tuning and how do you pull off – I mean, I guess adaptive compilation is what we're talking about as metaprogramming.  
**Translation:** Vocabulary: profound: 深刻

**[1339.54s] English:** Yeah.  
**Translation:** 

**[1339.70s] English:** How do you pull off auto-tuning?  
**Translation:** 

**[1340.76s] English:** I mean, is that as profound as I think it is?  
**Translation:** 

**[1343.22s] English:** It seems like a really, like, you know, we mentioned list comprehensions.  
**Translation:** Vocabulary: comprehensions: 理解

**[1347.58s] English:** To me, from a quick glance at Mojo, which, by the way, I have to absolutely, like, dive in, as I realize how amazing this is, I absolutely must dive in, that looks like just an incredible feature for machine learning people.  
**Translation:** 

**[1363.22s] English:** Yeah.  
**Translation:** 

**[1363.50s] English:** Well, so what is auto-tuning?  
**Translation:** 

**[1364.70s] English:** So take a step back.  
**Translation:** 

**[1366.20s] English:** Auto-tuning is a feature in Mojo.  
**Translation:** 

**[1367.82s] English:** It's not – so very little of what we're doing is actually research.  
**Translation:** 

**[1371.02s] English:** Like, many of these ideas have existed in other systems and other places, and so what we're doing is we're pulling together good ideas, remixing them.  
**Translation:** 

**[1377.58s] English:** And making them into, hopefully, a beautiful system, right?  
**Translation:** Vocabulary: remixing: 重新混音

**[1381.54s] English:** And so auto-tuning, the observation is that it turns out hardware systems, algorithms are really complicated.  
**Translation:** 

**[1389.16s] English:** It turns out maybe you don't actually want to know how the hardware works, right?  
**Translation:** 

**[1393.48s] English:** A lot of people don't, right?  
**Translation:** 

**[1394.74s] English:** And so there are lots of really smart hardware people – I know a lot of them – where they know everything about, okay, the cache size is this, and the number of registers is that.  
**Translation:** Vocabulary: cache: 缓存

**[1404.32s] English:** And if you use this length of vector, it's going to be super efficient because it maps.  
**Translation:** 

**[1407.58s] English:** It maps directly onto what it can do and, like, all this kind of stuff.  
**Translation:** 

**[1410.08s] English:** Or the GPU has SMs and it has a warp size of whatever, right?  
**Translation:** 

**[1413.36s] English:** All the stuff that goes into these things, or the tile size of a TPU is 128, like these factoids, right?  
**Translation:** Vocabulary: factoids: 琐闻趣事

**[1420.26s] English:** My belief is that most normal people – and I love hardware people also.  
**Translation:** 

**[1424.46s] English:** I'm not trying to offend literally everybody on the internet.  
**Translation:** 

**[1427.24s] English:** But most programmers actually don't want to know this stuff, right?  
**Translation:** 

**[1431.70s] English:** And so if you come at it from the perspective of how do we allow people to build both more abstracted but also more portable?  
**Translation:** Vocabulary: abstracted: 抽象化; programmers: 程序员

**[1437.58s] English:** Because, you know, it could be –  
**Translation:** 

**[1440.00s] English:** the vector length changes or the cache size changes or it could be that the tile size of  
**Translation:** 

**[1443.20s] English:** your matrix changes or the number you know an a100 versus an h100 versus a volta versus a whatever  
**Translation:** 

**[1448.56s] English:** gpu have different characteristics right a lot of the algorithms that you run are actually the same  
**Translation:** Vocabulary: matrix: 矩阵; volta: 伏特

**[1454.40s] English:** but the parameters these magic numbers you have to fill in end up being really fiddly numbers  
**Translation:** 

**[1458.88s] English:** that an expert has to go figure out and so what auto tuning does it says okay well guess what  
**Translation:** Vocabulary: fiddly: 繁琐的

**[1464.32s] English:** there's a lot of compute out there right so instead of having humans go randomly try all  
**Translation:** 

**[1469.12s] English:** the things or do a grid search or go search some complicated multi-dimensional space  
**Translation:** 

**[1474.00s] English:** how about we have computers do that right and so what auto tuning does is you can say hey here's  
**Translation:** 

**[1478.32s] English:** my algorithm if it's a a matrix operation or something like that you can say okay i'm going  
**Translation:** Vocabulary: algorithm: 算法

**[1483.84s] English:** to carve it up into blocks i'm going to do those blocks in parallel and i want this this with 128  
**Translation:** 

**[1489.52s] English:** things that i'm running on i want to cut it this way or that way or whatever and you can say hey  
**Translation:** 

**[1493.44s] English:** go see which one's actually empirically better on the system and then the result of that you  
**Translation:** 

**[1498.72s] English:** cache  
**Translation:** Vocabulary: empirically: 根据实证

**[1499.12s] English:** for that system yep you save it and so come back to twisting your compiler brain right so not only  
**Translation:** 

**[1505.92s] English:** does the compiler have an interpreter that's used to do metaprogramming that compiler that  
**Translation:** Vocabulary: interpreter: 解释器; metaprogramming: 元编程

**[1510.72s] English:** interpreter that metaprogramming now has to actually take your code and go run it on a  
**Translation:** 

**[1515.04s] English:** target machine see see which one it likes the best and then stitch it in and then keep going  
**Translation:** 

**[1520.56s] English:** right so part of the compilation is machine specific yeah well so i mean this is an optional  
**Translation:** 

**[1525.20s] English:** feature right so you don't have to use it for everything but yeah if you if you're so one of  
**Translation:** Vocabulary: compilation: 汇编; optional: 可选

**[1529.12s] English:** the things that we're in the quest of is ultimate performance yes right ultimate performance is  
**Translation:** 

**[1535.04s] English:** important for a couple of reasons right so if you're an enterprise you're looking to save costs  
**Translation:** 

**[1538.56s] English:** and compute and things like this ultimate performance translates to you know fewer servers  
**Translation:** 

**[1543.76s] English:** like if you care about the environment hey better performance leads to more efficiency right i mean  
**Translation:** 

**[1549.84s] English:** you could joke and say like you know python's bad for the environment  
**Translation:** 

**[1553.76s] English:** right and so if you move to mojo it's like at least 10x better just out of the box and keep going  
**Translation:** 

**[1558.08s] English:** right  
**Translation:** 

**[1559.12s] English:** um  
**Translation:** 

**[1560.00s] English:** But performance is also interesting because it leads to better products.  
**Translation:** 

**[1563.64s] English:** And so in the space of machine learning, right,  
**Translation:** 

**[1565.84s] English:** if you reduce the latency of a model so that it runs faster,  
**Translation:** 

**[1569.84s] English:** so every time you query the server running the model, it takes less time,  
**Translation:** Vocabulary: latency: 响应延迟

**[1572.76s] English:** well, then the product team can go and make the model bigger.  
**Translation:** 

**[1575.50s] English:** Well, that actually makes it so you have a better experience as a customer,  
**Translation:** 

**[1579.88s] English:** and so a lot of people care about that.  
**Translation:** 

**[1581.52s] English:** So for auto-tuning, for, like, tile size, you mentioned 128 for TPU,  
**Translation:** 

**[1585.08s] English:** you would specify, like, a bunch of options to try?  
**Translation:** 

**[1587.54s] English:** Yeah.  
**Translation:** 

**[1588.16s] English:** Just in the code?  
**Translation:** 

**[1589.20s] English:** Yep.  
**Translation:** 

**[1589.38s] English:** It's just a simple statement, and then you can just set and forget  
**Translation:** 

**[1592.74s] English:** and know depending on wherever it compiles, it'll actually be the fastest.  
**Translation:** Vocabulary: compiles: 编译外

**[1597.34s] English:** Yeah, exactly.  
**Translation:** 

**[1598.04s] English:** And the beauty of this is that it helps you in a whole bunch of different ways, right?  
**Translation:** 

**[1600.66s] English:** So if you're building – so often what will happen is that, you know,  
**Translation:** 

**[1603.92s] English:** you've written a bunch of software yourself, right?  
**Translation:** 

**[1606.00s] English:** You wake up one day, you say, I have an idea.  
**Translation:** 

**[1607.94s] English:** I'm going to go code up some code.  
**Translation:** 

**[1609.34s] English:** I get to work.  
**Translation:** 

**[1610.86s] English:** I forget about it.  
**Translation:** 

**[1612.56s] English:** I move on with life.  
**Translation:** 

**[1613.58s] English:** I come back six months or a year or two years or three years later.  
**Translation:** 

**[1615.94s] English:** You dust it off, and you go use it again in a new environment.  
**Translation:** 

**[1618.52s] English:** Mm-hmm.  
**Translation:** 

**[1619.38s] English:** And maybe your GPU is different.  
**Translation:** 

**[1620.76s] English:** Maybe you're running on a server instead of a laptop.  
**Translation:** 

**[1623.20s] English:** Maybe – whatever, right?  
**Translation:** 

**[1624.50s] English:** And so the problem now is you say, okay, well – I mean, again, not everybody cares about performance.  
**Translation:** 

**[1629.20s] English:** But if you do, you say, okay, well, I want to take advantage of all these new features.  
**Translation:** 

**[1632.98s] English:** I don't want to break the old thing, though, right?  
**Translation:** 

**[1635.78s] English:** And so the typical way of handling this kind of stuff before is, you know,  
**Translation:** 

**[1640.34s] English:** if you're talking about C++ templates or you're talking about C with macros,  
**Translation:** Vocabulary: macros: 宏; templates: 模板

**[1644.36s] English:** you end up with if-defs.  
**Translation:** 

**[1645.34s] English:** You get, like, all these weird things get layered in, make the code super complicated,  
**Translation:** 

**[1649.38s] English:** and how do you test it, right?  
**Translation:** 

**[1651.04s] English:** It becomes this crazy complexity, multidimensional space that you have to worry about.  
**Translation:** Vocabulary: complexity: 复杂性; multidimensional: 多维空间

**[1655.58s] English:** And, you know, that just doesn't scale very well.  
**Translation:** 

**[1658.84s] English:** Actually, let me just jump around before I go to some specific features.  
**Translation:** 

**[1662.14s] English:** Like, the increase in performance here that we're talking about can be just insane.  
**Translation:** 

**[1667.90s] English:** You're right that Moja can provide a 35,000x speedup over Python.  
**Translation:** Vocabulary: speedup: 加速

**[1675.72s] English:** How does it do that?  
**Translation:** 

**[1677.10s] English:** Yeah, so it can even do more.  
**Translation:** 

**[1678.86s] English:** Yeah.  
**Translation:** 

**[1679.38s] English:** Oh, okay.  
**Translation:** 

**[1680.00s] English:** to that so uh so first of all when we say that we're talking about what's called c python it's  
**Translation:** 

**[1687.18s] English:** the default python that everybody uses when you type python 3 that's like typically the one you  
**Translation:** 

**[1691.68s] English:** use right c python is an interpreter and so interpreters they have an extra layer of like  
**Translation:** 

**[1697.66s] English:** byte codes and things like this that they have to go read parse interpret and it makes them kind of  
**Translation:** Vocabulary: interpret: 解释执行; interpreter: 解释器; interpreters: 解释器; parse: 解析

**[1701.98s] English:** slow from that perspective and so one of the first things we do is we move to a compiler  
**Translation:** 

**[1706.28s] English:** and so i'm just moving to a compiler getting the interpreter out of the loop  
**Translation:** 

**[1709.74s] English:** is two to five to ten x speed up depending on the code so just out of the gate just using  
**Translation:** 

**[1716.64s] English:** more modern techniques right now if you do that one of the things you can do is you can start to  
**Translation:** 

**[1721.60s] English:** look at how c python started to lay out data and so one of the things that c python did and this  
**Translation:** 

**[1729.02s] English:** isn't part of the python spec necessarily but this is just sets of decisions is that if you take an  
**Translation:** 

**[1735.30s] English:** integer for example  
**Translation:** 

**[1736.28s] English:** it'll put it in an object because in python everything's an object and so they do the  
**Translation:** Vocabulary: integer: 整数

**[1741.22s] English:** very logical thing of keeping the memory representation of all objects the same  
**Translation:** 

**[1746.10s] English:** so all objects have a header they have like payload data they and what this means is that  
**Translation:** Vocabulary: payload: 载荷数据

**[1751.22s] English:** every time you pass around an object you're passing around a pointer to the data well this  
**Translation:** 

**[1755.86s] English:** has overhead it turns out that modern computers don't like chasing pointers very much and things  
**Translation:** 

**[1760.54s] English:** like this it means that you have to allocate the data means you have to reference count it which  
**Translation:** 

**[1764.94s] English:** is another way of that python  
**Translation:** Vocabulary: allocate: 分配

**[1766.18s] English:** uses keep track of memory and so this has a lot of overhead and so if you say okay let's try to get  
**Translation:** 

**[1772.30s] English:** that out of the heap out of a box out of an indirection and into the registers that's that's  
**Translation:** 

**[1780.98s] English:** another 10x so it adds up if you if you're reference counting every single every every  
**Translation:** 

**[1785.94s] English:** single thing you create that adds up yep and if you look at you know people complain about the  
**Translation:** 

**[1790.10s] English:** python gill this is one of the things that hurts parallelism that's because the reference counter  
**Translation:** 

**[1796.18s] English:** right and so the gill and reference counting are very tightly intertwined in python it's not the only  
**Translation:** Vocabulary: intertwined: 紧密相关

**[1800.00s] English:** but it's very tightly intertwined and so then you lean into this and you say okay cool well  
**Translation:** 

**[1804.04s] English:** modern computers they can do more than one operation at a time and so they have vectors  
**Translation:** 

**[1808.52s] English:** what is a vector well a vector allows you to take one instead of taking one piece of data doing an  
**Translation:** 

**[1812.68s] English:** add or multiply and then pick up the next one you can now do four or eight or 16 or 32 at a time  
**Translation:** Vocabulary: multiply: 乘法

**[1818.46s] English:** right well python doesn't expose that because of reasons and so now you can say okay well you can  
**Translation:** 

**[1822.78s] English:** adopt that now you have threads now you have like additional things like you can control memory  
**Translation:** 

**[1827.44s] English:** and so what mojo allows you to do is it allows you to start taking advantage of all these powerful  
**Translation:** 

**[1831.94s] English:** things that have been built into the hardware over time and it gives the library gives um very nice  
**Translation:** 

**[1837.28s] English:** features so you can say just parallelize this do this in parallel right so it's very um very  
**Translation:** 

**[1843.78s] English:** powerful weapons against slowness which is why people have been i think having fun like just  
**Translation:** 

**[1849.16s] English:** taking code and making it go fast because it's just kind of an adrenaline rush to see like how  
**Translation:** 

**[1853.06s] English:** fast you can get things before i talk about some of the interesting stuff with parallelization all  
**Translation:** Vocabulary: adrenaline: 肾上腺素

**[1857.18s] English:** that  
**Translation:** 

**[1857.40s] English:** let's let's first talk about like the basics we talked to indentation right so this thing looks  
**Translation:** Vocabulary: indentation: 缩进

**[1862.16s] English:** like python it's sexy and beautiful like python as we mentioned uh is it a typed language so what's  
**Translation:** 

**[1869.54s] English:** the role of types yeah good question so python has types it has strings has integers it has  
**Translation:** Vocabulary: integers: 整数

**[1876.42s] English:** dictionaries and like all that stuff but they all live at runtime right and so because all those  
**Translation:** 

**[1882.16s] English:** types live at runtime in python you never or you don't have to spell them python also has  
**Translation:** Vocabulary: runtime: 运行时

**[1887.40s] English:** like this whole typing thing going on now and a lot of people use it yeah i'm not talking about  
**Translation:** 

**[1891.22s] English:** that that's that's kind of a different thing we can go back to that if you want but but typically  
**Translation:** 

**[1894.70s] English:** the um you know you just say i take i have a def and my def takes two parameters i'm going to call  
**Translation:** 

**[1900.68s] English:** them a and b and i don't have to write a type okay so that is great but what that does is that forces  
**Translation:** 

**[1907.10s] English:** what's called a consistent representation so these things have to be a pointer to an object with the  
**Translation:** 

**[1912.08s] English:** object header and they all have to look the same and then when you dispatch a method you go through  
**Translation:** Vocabulary: dispatch: 分发调用

**[1916.90s] English:** all the same things and you have to look the same thing and you have to look the same thing and you  
**Translation:** 

**[1917.40s] English:** different paths no matter what the the receiver whatever that  
**Translation:** 

**[1920.00s] English:** type is so what mojo does is it allows you to have more than one kind of type and so what it does is  
**Translation:** 

**[1925.84s] English:** allows you to say okay cool i have i have an object and objects behave like python does and so it's  
**Translation:** 

**[1930.48s] English:** fully dynamic and that's all great and for many things classes like that's all very powerful and  
**Translation:** 

**[1934.96s] English:** very important but if you want to say hey it's an integer and it's 32 bits or 64 bits or whatever it  
**Translation:** Vocabulary: integer: 整数

**[1940.48s] English:** is or it's a floating point value it's 64 bits well then the compiler can take that and it can  
**Translation:** 

**[1946.08s] English:** use that to do way better optimization it turns out again getting rid of the interactions that's  
**Translation:** Vocabulary: optimization: 优化

**[1950.88s] English:** huge means you can get better code completion because you have um because compiler knows what  
**Translation:** 

**[1956.08s] English:** the type is and so it knows what operations work on it and so that's actually pretty huge and so  
**Translation:** 

**[1961.68s] English:** what mojo does is it allows you to progressively adopt types into your program and so you can  
**Translation:** 

**[1966.80s] English:** start again it's compatible with python and so then you can add however many types you want  
**Translation:** Vocabulary: compatible: 兼容; progressively: 逐步

**[1971.04s] English:** wherever you want them and if you don't want to deal with it you don't have to deal with it right  
**Translation:** 

**[1974.88s] English:** and so one of one of  
**Translation:** 

**[1976.08s] English:** you know our opinions on this is that it's not that types are the right thing or the wrong thing  
**Translation:** 

**[1983.04s] English:** it's that they're a useful thing well so it's kind of optional it's not strict typing you don't have  
**Translation:** Vocabulary: optional: 可选的

**[1988.16s] English:** to specify a type exactly okay so starting from the thing that python's kind of reaching towards  
**Translation:** 

**[1993.68s] English:** right now with trying to inject types into it yeah with a very different approach but yes  
**Translation:** 

**[1999.60s] English:** yeah what's the different approach i'm actually one of the people that have not been using types  
**Translation:** 

**[2005.60s] English:** very much  
**Translation:** 

**[2006.08s] English:** in python seven okay why did you say it just well because i i know the importance it's like adults  
**Translation:** 

**[2012.72s] English:** use strict typing and so i i refuse to grow up in that sense it's a it's a kind of rebellion but i i  
**Translation:** Vocabulary: rebellion: 反抗

**[2019.84s] English:** just know that um it probably reduces the amount of errors even just for forget about performance  
**Translation:** 

**[2026.16s] English:** improvements it probably reduces errors when you do strict typing yeah so i mean i think it's  
**Translation:** 

**[2030.24s] English:** interesting if you look at that right and the reason i'm giving you a hard time again is that  
**Translation:** 

**[2034.40s] English:** that there's this  
**Translation:** 

**[2036.08s] English:** this cultural norm this pressure this like there has to be a right way to do things  
**Translation:** 

**[2040.00s] English:** It's like, you know, grown-ups only do it one way,  
**Translation:** 

**[2041.94s] English:** and if you don't do that, you should feel bad, right?  
**Translation:** 

**[2043.94s] English:** Like, some people feel like Python's a guilty pleasure or something,  
**Translation:** 

**[2046.88s] English:** and it's like, when it gets serious, I need to go rewrite it, right?  
**Translation:** 

**[2049.50s] English:** Yeah, exactly.  
**Translation:** 

**[2050.20s] English:** Well, I mean, cool, I understand history,  
**Translation:** 

**[2052.74s] English:** and I understand kind of where this comes from,  
**Translation:** 

**[2054.24s] English:** but I don't think it has to be a guilty pleasure, right?  
**Translation:** 

**[2057.50s] English:** So if you look at that, you say, why do you have to rewrite it?  
**Translation:** 

**[2060.12s] English:** Well, you have to rewrite it to deploy.  
**Translation:** 

**[2062.18s] English:** Well, why do you want to deploy?  
**Translation:** Vocabulary: deploy: 部署

**[2063.40s] English:** Well, you care about performance, or you care about predictability,  
**Translation:** 

**[2065.90s] English:** or you want, you know, a tiny thing on the server  
**Translation:** 

**[2068.88s] English:** that has no dependencies, or, you know,  
**Translation:** 

**[2070.46s] English:** you have objectives that you're trying to attain.  
**Translation:** 

**[2074.00s] English:** So what if Python can achieve those objectives?  
**Translation:** 

**[2077.44s] English:** So if you want types, well, maybe you want types  
**Translation:** 

**[2079.34s] English:** because you want to make sure you're passing on the right thing.  
**Translation:** 

**[2081.78s] English:** Sure, you can add a type.  
**Translation:** 

**[2083.14s] English:** If you don't care, you're prototyping some stuff,  
**Translation:** 

**[2085.78s] English:** you're hacking some things out,  
**Translation:** Vocabulary: hacking: 快速开发; prototyping: 原型制作

**[2086.86s] English:** you're, like, pulling some RAM code off the Internet,  
**Translation:** 

**[2088.98s] English:** it should just work, right?  
**Translation:** 

**[2091.02s] English:** And you shouldn't be, like, pressured.  
**Translation:** 

**[2093.10s] English:** You shouldn't feel bad about doing the right thing  
**Translation:** 

**[2095.52s] English:** or the thing that feels good.  
**Translation:** 

**[2096.62s] English:** Now, if you're in a team, right,  
**Translation:** 

**[2098.76s] English:** you're working at some massive Internet company  
**Translation:** 

**[2100.86s] English:** and you have 400 million lines of Python code,  
**Translation:** 

**[2103.74s] English:** well, they may have a house rule that you use types, right?  
**Translation:** 

**[2107.08s] English:** Because it makes it easier for different humans  
**Translation:** 

**[2108.54s] English:** to talk to each other and understand what's going on  
**Translation:** 

**[2110.30s] English:** and bugs at scale, right?  
**Translation:** 

**[2112.44s] English:** And so there are lots of good reasons  
**Translation:** 

**[2114.06s] English:** why you might want to use types,  
**Translation:** 

**[2115.84s] English:** but that doesn't mean that everybody should use them all the time, right?  
**Translation:** 

**[2118.84s] English:** So what Mojo does is it says,  
**Translation:** 

**[2120.06s] English:** cool, well, allow people to use types,  
**Translation:** 

**[2122.62s] English:** and if you use types, you get nice things out of it, right?  
**Translation:** 

**[2125.46s] English:** You get better performance and things like this, right?  
**Translation:** 

**[2127.80s] English:** But Mojo,  
**Translation:** 

**[2128.76s] English:** there's a full compatible superset of Python, right?  
**Translation:** 

**[2133.32s] English:** And so that means it has to work without types.  
**Translation:** 

**[2136.76s] English:** It has to support all the dynamic things.  
**Translation:** 

**[2138.56s] English:** It has to support all the packages.  
**Translation:** 

**[2139.34s] English:** It has to support list comprehensions and things like this, right?  
**Translation:** 

**[2143.88s] English:** And so that starting point, I think, is really important.  
**Translation:** Vocabulary: comprehensions: 理解能力

**[2147.18s] English:** And I think that, again,  
**Translation:** 

**[2149.18s] English:** you can look at why I care so much about this,  
**Translation:** 

**[2151.00s] English:** and there's many different aspects of that,  
**Translation:** 

**[2152.62s] English:** one of which is the world went through a very challenging migration  
**Translation:** 

**[2156.20s] English:** from Python 2 to Python 3.  
**Translation:** 

**[2158.76s] English:** Right?  
**Translation:** 

**[2159.46s] English:** Yes.  
**Translation:** 

**[2160.00s] English:** this migration took many years and it was very painful for many teams right and there's a lot of  
**Translation:** 

**[2164.66s] English:** a lot of things that went on in that um i'm not an expert in all the details i honestly don't want to  
**Translation:** 

**[2170.12s] English:** be i don't want the world to have to go through that yeah right and you know people can ignore  
**Translation:** 

**[2174.54s] English:** mojo and if it's not their thing that's that's cool but if they want to use mojo i don't want  
**Translation:** 

**[2178.36s] English:** them to have to rewrite all their code i mean this okay the superset part is it's just i mean  
**Translation:** 

**[2184.30s] English:** so much brilliant stuff here that definitely is is incredible um we'll talk about that yeah  
**Translation:** 

**[2189.96s] English:** first of all how's the typing implemented differently in uh in python versus uh mojo  
**Translation:** 

**[2196.42s] English:** so this heterogeneous flexibility you said is definitely implemented yeah so i'm not a full  
**Translation:** 

**[2202.36s] English:** expert in the whole backstory on types in python so i'll give you i'll give you that i can give  
**Translation:** Vocabulary: flexibility: 灵活性; heterogeneous: 异构的

**[2206.94s] English:** you my understanding um my understanding is basically like many dynamic languages the  
**Translation:** 

**[2212.54s] English:** ecosystem went through a phase where people went from writing scripts to writing large scale  
**Translation:** 

**[2217.88s] English:** huge code bases in python  
**Translation:** 

**[2219.96s] English:** and at scale it kind of helps have types yeah people want to be able to reason about interfaces  
**Translation:** Vocabulary: interfaces: 接口

**[2225.46s] English:** what what do you expect string or an inch or like what these basic things right and so what the  
**Translation:** 

**[2230.72s] English:** python community started doing is it started saying okay let's have tools on the side checker  
**Translation:** 

**[2236.52s] English:** tools right that go and like enforce invariance check for bugs try to identify things these are  
**Translation:** 

**[2242.72s] English:** called static analysis tools generally and so these tools run over your code and try to look  
**Translation:** Vocabulary: invariance: 不变性

**[2246.68s] English:** for bugs what ended up happening is there's so many of these things so many of these things  
**Translation:** 

**[2249.96s] English:** made different weird patterns and different approaches on specifying the types and different  
**Translation:** Vocabulary: specifying: 指定

**[2253.58s] English:** things going on that the python community realized and recognized hey hey there's a thing here and so  
**Translation:** 

**[2259.12s] English:** what they started to do is they started to standardize the syntax for adding types to python  
**Translation:** Vocabulary: standardize: 规范化; syntax: 语法规则

**[2262.66s] English:** now one of the challenges that they had is that they're coming from kind of this fragmented world  
**Translation:** 

**[2267.22s] English:** where there's lots of different tools they have different trade-offs and interpretations and the  
**Translation:** Vocabulary: fragmented: 支离破碎; interpretations: 解释

**[2270.90s] English:** types being different things and so if you look at types in python according to the python spec  
**Translation:** 

**[2275.74s] English:** the types are ignored right so according to python the types are ignored and so they're  
**Translation:** 

**[2279.96s] English:** the types that are ignored so if you look at you know children and children can be a little bit  
**Translation:** 

**[2285.28s] English:** forgetful and they're not secret and it's kind of interesting but if you look at the game experience  
**Translation:** 

**[2288.90s] English:** and you kind of like the game experience and you're like oh this is what this is it's going to be  
**Translation:** 

**[2291.84s] English:** different right so you can find lots of things to focus on and you can you can use them to gain  
**Translation:** 

**[2296.62s] English:** understanding for each of these things and so we started to after we started to think about how to  
**Translation:** 

**[2300.90s] English:** make this work the key is to start to think about what do we want to do and what it's going to look  
**Translation:** 

**[2305.40s] English:** like and then we started to think about how to do things without any kind of scientific knowledge  
**Translation:** 

**[2309.30s] English:** and so we started to think about how to use the 컨 merchant to create a database that was going to be  
**Translation:** 

**[2309.78s] English:** a Python's database and so in our case we started to think about the type that was going to be meant to be a  
**Translation:** 

**[2280.00s] English:** spec you can write pretty much anything in a type position okay and um you can technically you can  
**Translation:** 

**[2288.10s] English:** write any expression okay now that's beautiful because you can extend it you can do cool things  
**Translation:** 

**[2294.34s] English:** you can write build your own tools you can build your own house linter or something like that right  
**Translation:** Vocabulary: linter: 代码检查工具

**[2298.48s] English:** but it's also a problem because any existing python program may be using different tools  
**Translation:** 

**[2303.86s] English:** and they have different interpretations and so if you adopt somebody's package into your ecosystem  
**Translation:** 

**[2308.38s] English:** try around the tool you prefer it may throw out tons of weird errors and warnings and problems  
**Translation:** 

**[2312.82s] English:** just because it's incompatible with how these things work also because they're added late and  
**Translation:** Vocabulary: incompatible: 不兼容

**[2317.70s] English:** they're not checked by the python interpreter it's always kind of more of a hint than it is a  
**Translation:** 

**[2321.20s] English:** requirement also uh the c python implementation can't use them for performance and so it's really  
**Translation:** Vocabulary: implementation: 实现; interpreter: 解释器

**[2327.26s] English:** that's a big one right so you can't utilize the for the compilation for the just in time  
**Translation:** 

**[2331.38s] English:** compilation okay exactly and this this all comes back to the design principle of it's  
**Translation:** Vocabulary: compilation: 编译

**[2335.82s] English:** it's kind of they're kind of hints they're kind of the definition  
**Translation:** 

**[2338.38s] English:** is a little bit murky it's unclear exactly the interpretation in a bunch of cases and so  
**Translation:** Vocabulary: murky: 模糊不清

**[2342.14s] English:** because of that you can't actually um even if you want to it's really difficult to use them to say  
**Translation:** 

**[2347.00s] English:** like it is going to be an int and if it's not it's a problem right a lot of code would break if you  
**Translation:** 

**[2351.94s] English:** did that so so in mojo right so you can still use those kind of type annotations it's fine  
**Translation:** 

**[2356.76s] English:** but in mojo if you declare a type and you use it then it means it is going to be that type  
**Translation:** Vocabulary: annotations: 注解

**[2362.50s] English:** and the compiler helps you check that and force it and it's safe um and it's not it's not a like  
**Translation:** 

**[2368.38s] English:** best effort hint kind of a thing so if you try to shove a string type thing into an integer you  
**Translation:** Vocabulary: integer: 整数; shove: 强行插入

**[2374.42s] English:** get an error and you get another from the compiler compile time nice okay what kind of basic types  
**Translation:** 

**[2381.14s] English:** are there yeah so uh mojo is um pretty hardcore in terms of what it tries to do in the language  
**Translation:** Vocabulary: hardcore: 严格要求的

**[2389.26s] English:** which is the philosophy there is that we um again if you if you look at python right python's  
**Translation:** 

**[2396.78s] English:** beautiful language because it's so extensible  
**Translation:** Vocabulary: extensible: 可扩展的

**[2398.38s] English:** right and so all of  
**Translation:** 

**[2400.00s] English:** the different things in python like for loops and plus and like all these things can be accessed  
**Translation:** Vocabulary: accessed: 被访问

**[2405.34s] English:** through these underbar armbar methods okay so you have to say okay if i make something that is super  
**Translation:** 

**[2411.56s] English:** fast i can go all the way down to the metal why do i need to have integers built into the language  
**Translation:** Vocabulary: integers: 整数

**[2415.80s] English:** right and so what mojo does is it says okay well we can have this notion of structs  
**Translation:** 

**[2420.70s] English:** so you have classes in python now you can have structs classes are dynamic structs are static  
**Translation:** 

**[2426.22s] English:** cool we can get high performance we can write c++ kind of code with structs if you want these  
**Translation:** 

**[2431.74s] English:** things mix and work beautifully together um but what that means is that you can go and implement  
**Translation:** 

**[2436.08s] English:** strings and ints and floats and arrays and all that kind of stuff in the language right and so  
**Translation:** 

**[2441.96s] English:** that's really cool because you know to me as a ideal idealizing compiler language type of person  
**Translation:** 

**[2449.82s] English:** what i want to do is i want to get magic out of the compiler and put in the libraries because if  
**Translation:** 

**[2454.64s] English:** somebody can you know if we  
**Translation:** 

**[2456.20s] English:** can build an integer that's beautiful and it has an amazing api it does all the things you'd expect  
**Translation:** 

**[2460.00s] English:** an integer to do but you don't like it maybe you want a big integer maybe you want to like sideways  
**Translation:** Vocabulary: sideways: 横着

**[2465.46s] English:** integer i don't know like what what all the space of integers are um then uh then you can do that  
**Translation:** 

**[2471.80s] English:** and it's not a second class citizen and so if you look at certain other languages like c++ one i  
**Translation:** 

**[2478.14s] English:** also love and use a lot um int is hardcoded in the language but complex is not  
**Translation:** 

**[2485.66s] English:** the  
**Translation:** Vocabulary: hardcoded: 固定不变的

**[2486.20s] English:** and so isn't it kind of weird that you have this std complex class but you have int and complex  
**Translation:** 

**[2492.98s] English:** tries to look like a natural numeric type and things like this but integers and floating point  
**Translation:** Vocabulary: numeric: 数值的

**[2498.42s] English:** have these like special promotion rules and other things like that that are magic and they're hacked  
**Translation:** 

**[2502.56s] English:** into the compiler and because of that you can't actually make something that works like the built  
**Translation:** Vocabulary: hacked: 被修改

**[2506.16s] English:** in types is there something provided as a standard because uh you know because it's ai first you know  
**Translation:** 

**[2514.12s] English:** numerical types are so important here so is there something like a nice standard  
**Translation:** Vocabulary: numerical: 数字的

**[2520.00s] English:** implementation of integer and float yeah so so we're still building all that stuff out so we  
**Translation:** 

**[2523.18s] English:** provide integers and floats and all that kind of stuff we also provide like buffers and tensors  
**Translation:** Vocabulary: implementation: 实现; integer: 整数

**[2527.06s] English:** and things like that that you'd expect in an ml context honestly we need to keep designing and  
**Translation:** 

**[2532.64s] English:** redesigning and working with the community to build that out and make that better that's not  
**Translation:** 

**[2535.32s] English:** our strength right now give us six months or a year and i think it'll be way better but um but  
**Translation:** 

**[2540.70s] English:** the power of putting in the library means we can have teams of experts that aren't compiler  
**Translation:** 

**[2544.74s] English:** engineers that can help us design and refine and drive us forward so uh one of the exciting things  
**Translation:** 

**[2550.24s] English:** we should mention here is that this is uh this is new and fresh this cake is unbaked it's almost  
**Translation:** Vocabulary: refine: 精炼; unbaked: 未烤

**[2558.28s] English:** baked you can tell it's delicious but it's not fully ready to be consumed yep that's very fair  
**Translation:** 

**[2563.72s] English:** it is very useful but it's very useful if you're a super low level programmer right now and what  
**Translation:** Vocabulary: programmer: 程序员

**[2568.20s] English:** we're doing is we're working our way up the stack and so the way i would look at mojo today in may  
**Translation:** 

**[2573.50s] English:** in 2023  
**Translation:** 

**[2574.74s] English:** is that it's like a 0.1 so i think that you know a year from now it's gonna be way more interesting  
**Translation:** 

**[2582.02s] English:** to a variety of people but what we're doing is we're we decide to release it early so that people  
**Translation:** 

**[2587.50s] English:** can get access to and play with and we can build with community we um have a big roadmap fully  
**Translation:** 

**[2593.54s] English:** published being transparent about this and a lot of people are involved in this stuff and so what  
**Translation:** Vocabulary: transparent: 公开透明

**[2597.48s] English:** we're doing is we're really optimizing for building this thing the right way and building it the right  
**Translation:** 

**[2602.80s] English:** way is kind of interesting working with the community  
**Translation:** Vocabulary: optimizing: 优化

**[2604.74s] English:** because everybody wants it yesterday and so it's sometimes it's kind of you know there's some  
**Translation:** 

**[2611.12s] English:** dynamics there but yeah i think it's a good it's the right thing so there's a discord also so the  
**Translation:** 

**[2615.86s] English:** dynamics is pretty interesting sometimes the community probably can be very chaotic  
**Translation:** 

**[2619.98s] English:** and uh introduce a lot of stress guido famously quit over the stress of the walrus operator i  
**Translation:** Vocabulary: guido: 古迪奥; walrus: 海象

**[2628.06s] English:** mean yes you know i broke maybe that was the camel's back exactly and so like it could be  
**Translation:** 

**[2633.70s] English:** very stressful as you do it but i think it's a good thing because i think it's a good thing because  
**Translation:** 

**[2634.74s] English:** it's a good thing to develop but can you just a tangent upon a tangent is it stressful to do  
**Translation:** 

**[2640.00s] English:** uh to work through the design of various features here given that the community is so  
**Translation:** Vocabulary: tangent: 旁枝逸出

**[2646.20s] English:** richly involved well so um so i've been doing open development and community stuff for decades now  
**Translation:** 

**[2651.84s] English:** somehow this has happened to me um so i've i've learned some tricks but the the thing that always  
**Translation:** 

**[2657.10s] English:** gets me is i want to make people happy right and so this this is maybe not all people all happy all  
**Translation:** 

**[2663.14s] English:** the time but generally i want i want people to be happy right and so the challenge is that again  
**Translation:** 

**[2668.32s] English:** we're tapping into some long some deep-seated long tensions and pressures both in the python  
**Translation:** 

**[2675.02s] English:** world but also in the ai world in the hardware world and things like this and so people just  
**Translation:** 

**[2678.88s] English:** want us to move faster right and so again our decision was let's release this early let's get  
**Translation:** 

**[2685.00s] English:** people used to it or access to it and play with it and like let's let's build in the open which  
**Translation:** 

**[2690.16s] English:** we could have you know had the the language monk sitting in the cloister up on the hilltop like  
**Translation:** 

**[2698.32s] English:** wearing away trying to build something but in my experience you get something that's way better if  
**Translation:** Vocabulary: cloister: 僧院; hilltop: 山顶

**[2701.76s] English:** you work with the community right uh and so yes it can be frustrating can be challenging for lots of  
**Translation:** 

**[2706.68s] English:** people involved and you know if you i mean if you mention our discord we have over 10 000 people on  
**Translation:** Vocabulary: frustrating: 令人沮丧的

**[2711.18s] English:** the discord 11 000 people or something keep in mind we released mojo like two weeks ago yeah  
**Translation:** 

**[2715.64s] English:** so um it's very active so it's very cool um but what that means is that um you know 10 11 000  
**Translation:** 

**[2723.36s] English:** people all will want something different right and so what we've done is we've tried to say  
**Translation:** 

**[2728.32s] English:** okay cool here's our roadmap here here and the roadmap isn't completely arbitrary it's based on  
**Translation:** Vocabulary: arbitrary: 随意

**[2734.32s] English:** here's the logical order in which to build these features or add these capabilities and things like  
**Translation:** 

**[2738.48s] English:** that and what we've done is we've spun really fast on like bug fixes and so we actually have  
**Translation:** 

**[2743.12s] English:** very few bugs which is cool i mean actually for a project in the state but then what we're doing is  
**Translation:** 

**[2748.96s] English:** we're dropping in features very deliberately i mean this is fun to watch because you got the two  
**Translation:** Vocabulary: deliberately: 有目的地

**[2753.84s] English:** gigantic communities of like hardware like systems engineers and then you have  
**Translation:** 

**[2758.32s] English:** the machine learning  
**Translation:** Vocabulary: gigantic: 巨大的

**[2760.00s] English:** any python people that are like higher level yeah and it's just too like for like army like uh  
**Translation:** 

**[2767.20s] English:** they've been at war yeah they've been at war right and so so here's a tolkien novel or something okay  
**Translation:** 

**[2773.66s] English:** so here's the test again like it's it's super funny for for something that's only been out for  
**Translation:** 

**[2777.24s] English:** two weeks right people are so impatient right but okay cool let's fast forward a year like in a  
**Translation:** 

**[2783.48s] English:** year's time mojo will be actually quite amazing and solve tons of problems and be very good um  
**Translation:** 

**[2788.78s] English:** people still have these problems right and so you you look at this and you say and the way i look at  
**Translation:** 

**[2794.50s] English:** this at least is to say okay well we're solving big long-standing problems to me i again working  
**Translation:** 

**[2802.38s] English:** on many different problems i want to make sure we do it right right there's like a responsibility  
**Translation:** 

**[2806.08s] English:** you feel because if you mess it up right there's very few opportunities to do projects like this  
**Translation:** 

**[2811.68s] English:** and have them really have impact on the world if we do it right then maybe we can take those  
**Translation:** 

**[2816.00s] English:** feuding armies and actually heal some of those wounds  
**Translation:** 

**[2818.78s] English:** yeah this is like this feels this feels like a speech by george washington or abraham or something  
**Translation:** Vocabulary: feuding: 争吵

**[2824.10s] English:** and you look at this and it's like okay well how different are we yeah we all want beautiful things  
**Translation:** 

**[2829.44s] English:** we all want something that's nice we all want to be able to work together we all want our stuff to  
**Translation:** 

**[2832.54s] English:** be used right and so if we can help heal that now i'm not optimistic that all people will use mojo  
**Translation:** 

**[2838.04s] English:** and they'll stop using c++ like that's not my goal right but um but if we can heal some of that i  
**Translation:** 

**[2842.88s] English:** think that'd be pretty cool yeah and and we start by putting the people who like braces into the  
**Translation:** 

**[2848.78s] English:** mojo uh so so so there are proposals for adding braces to mojo and we just what's your thing we  
**Translation:** Vocabulary: braces: 牙套

**[2854.02s] English:** tell them no okay politely yeah anyway so there's a lot of amazing features on the roadmap and those  
**Translation:** 

**[2861.76s] English:** already implemented it'd be awesome i could just ask you a few things so uh the the other  
**Translation:** Vocabulary: politely: 礼貌地

**[2867.68s] English:** performance improvement comes from immutability so what's the what's this var and this let  
**Translation:** 

**[2873.02s] English:** thing that we got going on well what's immutability yeah so one of the things that  
**Translation:** Vocabulary: immutability: 不可变性

**[2878.78s] English:** uh useful  
**Translation:** 

**[2880.00s] English:** and it's not always required but it's useful is knowing whether something can change out from  
**Translation:** 

**[2884.34s] English:** underneath you right and so in python you have a pointer to an array right and so you pass that  
**Translation:** 

**[2890.38s] English:** pointer to an array around to things if you pass into a function they may take that and scroll away  
**Translation:** Vocabulary: scroll: 滚动

**[2896.32s] English:** in some other data structure and so you get your array back and you go to use it now somebody else  
**Translation:** 

**[2901.08s] English:** is like putting stuff in your array how do you reason about that it gets to be very complicated  
**Translation:** 

**[2906.26s] English:** at least lots of bugs right and so one of the things that you know again this is not something  
**Translation:** 

**[2911.50s] English:** mojo forces on you but something that mojo enables is a thing called value semantics and what value  
**Translation:** Vocabulary: semantics: 语义

**[2916.76s] English:** semantics do is they take collections like arrays like dictionaries also tensors and strings and  
**Translation:** 

**[2924.66s] English:** things like this that are much higher level and make them behave like proper values and so it  
**Translation:** 

**[2929.94s] English:** makes it look like if you pass these things around you get a logical copy of all the data  
**Translation:** 

**[2934.54s] English:** and so if i pass you  
**Translation:** 

**[2936.14s] English:** you  
**Translation:** 

**[2936.26s] English:** an array it's your array you can go do what you want to it you're not going to hurt my array  
**Translation:** 

**[2939.72s] English:** now that is an interesting and very powerful design principle it defines away a ton of bugs  
**Translation:** 

**[2945.20s] English:** you have to be careful to implement it in an efficient way it has their performance hit  
**Translation:** 

**[2949.96s] English:** that's a significant uh generally not if you implement it the right way but it requires a  
**Translation:** 

**[2956.34s] English:** lot of very low level uh getting the language right bits i assume there'll be a huge performance  
**Translation:** 

**[2962.18s] English:** hit because it's a really the benefit is really nice because you don't get into absolutely i  
**Translation:** 

**[2966.14s] English:** hope so  
**Translation:** 

**[2966.26s] English:** yeah well the trick is is you can't do you can't do copies so you have to provide  
**Translation:** 

**[2970.68s] English:** the behavior of copying without doing the copy yeah how do you do that is that how do you do  
**Translation:** 

**[2978.84s] English:** that it's not magic it's just it's actually pretty cool well so first before we talk about  
**Translation:** 

**[2983.38s] English:** how that works let's talk about how it works in python right so in python you define a person  
**Translation:** 

**[2988.28s] English:** class or maybe a person class is a bad idea you define a database class right and database class  
**Translation:** 

**[2992.98s] English:** has an array of records something like that right and so the problem is that you can't do that in a  
**Translation:** 

**[2996.26s] English:** database if you pass in a record or a class instance into the data  
**Translation:** 

**[3000.00s] English:** it'll take a hold of that object and then it assumes it has it and if you're  
**Translation:** 

**[3005.68s] English:** passing an object in you have to know that that database is gonna take take it  
**Translation:** 

**[3009.40s] English:** and therefore you shouldn't change it after you put in the database right this  
**Translation:** 

**[3012.12s] English:** is this is just kind of have to know that you just have to kind of know that  
**Translation:** 

**[3014.76s] English:** right and so you roll out version one of the database you just kind of have to  
**Translation:** 

**[3018.78s] English:** know that of course Lex uses his own database right yeah right cuz you built  
**Translation:** 

**[3022.74s] English:** it you understand this works right somebody else joins the team they don't  
**Translation:** 

**[3026.16s] English:** know this yes right and so now they suddenly get bugs you're having to  
**Translation:** 

**[3030.06s] English:** maintain the database you shake your fist you argue the tenth time this  
**Translation:** 

**[3034.38s] English:** happens you're like okay we have to do something different right and so what  
**Translation:** 

**[3037.20s] English:** you do is you go change your Python code and you change your database class to  
**Translation:** 

**[3040.86s] English:** copy the record every time you add it and so what ends up happening is you say  
**Translation:** 

**[3045.06s] English:** okay I will do what's called a defensive copy inside the database and then that  
**Translation:** 

**[3050.10s] English:** way if somebody passes something in I will have my own copy of it and they can  
**Translation:** 

**[3054.92s] English:** go do whatever and they're not gonna break  
**Translation:** 

**[3056.10s] English:** my code and they're not gonna break my code and they're not gonna break my code  
**Translation:** 

**[3056.14s] English:** and they're not gonna break my thing okay this is usually the the two design  
**Translation:** 

**[3060.22s] English:** patterns if you look in pytorch for example this is cloning a tensor like  
**Translation:** 

**[3063.86s] English:** there's a specific thing and you have to know where to call it if you don't call  
**Translation:** 

**[3066.46s] English:** in the right place you get these bugs and this is state-of-the-art right so a  
**Translation:** 

**[3070.76s] English:** different approach so it's used in many languages so I work with it in Swift as  
**Translation:** 

**[3074.86s] English:** you say okay well let's provide value semantics and so we want to provide the  
**Translation:** 

**[3079.36s] English:** view that you get a logically independent copy but we want to do that  
**Translation:** Vocabulary: logically: 逻辑上; semantics: 语义

**[3083.62s] English:** lazily and so what what we do  
**Translation:** 

**[3086.08s] English:** is you say okay if you pass something into a function it doesn't actually make  
**Translation:** 

**[3089.76s] English:** a copy what actually does is it just increment the reference to it and if you  
**Translation:** 

**[3093.46s] English:** pass it around you stick in your database it can go in the database you  
**Translation:** Vocabulary: increment: 增加

**[3096.78s] English:** own it and then you come back out of the stack nobody's copied anything you come  
**Translation:** 

**[3101.50s] English:** back out of the stack and then the caller lets go of it well then you've  
**Translation:** 

**[3105.48s] English:** just handed it off to the database you've transferred it and there's no  
**Translation:** 

**[3109.06s] English:** copies made now on the other hand if you know your  
**Translation:** 

**[3113.14s] English:** co-worker goes and hands you a record and you pass it  
**Translation:** 

**[3116.00s] English:** it in you stick in the database and then you go to town and you start modifying it  
**Translation:** Vocabulary: modifying: 修改

**[3120.00s] English:** what happens is you get a copy lazily on demand and so what this does is gives you copies only  
**Translation:** 

**[3126.40s] English:** when you need them and it also so it defines away the bugs but also generally reduces the  
**Translation:** 

**[3131.04s] English:** number of copies in practice and so but the implementation details are tricky here  
**Translation:** 

**[3135.92s] English:** so this is yes something with reference counting but to make it performant uh across a number of  
**Translation:** Vocabulary: implementation: 实现细节

**[3143.20s] English:** different kinds of objects yeah so you need a couple of things and so there's many so this  
**Translation:** 

**[3148.88s] English:** concept has existed in many different worlds and so again it's not novel research at all right the  
**Translation:** 

**[3155.28s] English:** magic is getting the design right so that you can do this in a reasonable way right and so there's  
**Translation:** 

**[3159.68s] English:** a number of components that go into this one is when you're passing around so you we're talking  
**Translation:** 

**[3164.24s] English:** about python and reference counting at the expense of doing that when you're passing values around  
**Translation:** 

**[3169.12s] English:** you don't want to do extra reference counting for no good reason and so you have to make sure that  
**Translation:** 

**[3172.96s] English:** you're efficient and you transfer ownership instead of duplicating references and things  
**Translation:** 

**[3177.44s] English:** like that which is a very low level  
**Translation:** Vocabulary: duplicating: 复制

**[3178.88s] English:** problem you also have to adopt this and you have to build these data structures and so if you say  
**Translation:** 

**[3186.00s] English:** you know mojo has to be compatible with python so of course the default  
**Translation:** Vocabulary: compatible: 兼容的

**[3189.36s] English:** list is a reference semantic list that works the way you'd expect in python but then you  
**Translation:** 

**[3194.40s] English:** have to design a value semantic list and so you just have to implement that and then you  
**Translation:** Vocabulary: semantic: 语义

**[3198.40s] English:** implement the logic within and so the the role of the language here is to provide all the  
**Translation:** 

**[3203.04s] English:** low-level hooks that allow the author of the type to be able to get and express this behavior without  
**Translation:** 

**[3208.88s] English:** forcing it into all cases or hardcoding this into the language itself but there's a ownership so  
**Translation:** 

**[3214.08s] English:** you you're constantly transferring you're tracking who owns the thing yes and so there's a whole  
**Translation:** Vocabulary: hardcoding: 固化; transferring: 转移

**[3217.84s] English:** system called ownership and so this is related to work done in the rust community also the swift  
**Translation:** 

**[3223.84s] English:** community has done a bunch of work and there's a bunch of different other languages that have  
**Translation:** 

**[3226.74s] English:** all kind of c plus plus actually has copy constructors and destructors and things like that  
**Translation:** 

**[3231.44s] English:** and so um and i mean c++ has everything so it has move constructors it has like this whole world of  
**Translation:** Vocabulary: constructors: 构造函数; destructors: 析构函数

**[3236.64s] English:** things and so this is uh you know one of my favorite things about c++ is the ability to do this and uh  
**Translation:** 

**[3236.96s] English:** and and i think that's one of my favorite things about c++ is that you can you can kind of do the whole thing  
**Translation:** 

**[3237.42s] English:** and that's one of the things about c++ is that you have to build this thing and you have to work on  
**Translation:** 

**[3237.88s] English:** This is a...  
**Translation:** 

**[3240.00s] English:** body of work that's kind of been developing for many, many years now. And so Mojo takes some of  
**Translation:** 

**[3244.34s] English:** the best ideas out of all these systems and remixes in a nice way so that you get the power  
**Translation:** 

**[3250.50s] English:** of something like the Rust programming language, but you don't have to deal with it when you don't  
**Translation:** 

**[3255.04s] English:** want to, which is a major thing in terms of teaching and learning and being able to use  
**Translation:** 

**[3258.86s] English:** and scale these systems. How does that play with argument conventions? What are they? Why are they  
**Translation:** 

**[3264.72s] English:** important? How does the value semantics, how does the transfer ownership work with the arguments  
**Translation:** Vocabulary: conventions: 约定俗成; semantics: 语义

**[3269.90s] English:** when they're passing? So if you go deep into systems programming land, this isn't again,  
**Translation:** 

**[3275.54s] English:** it's not something for everybody, but if you go deep into systems programming land,  
**Translation:** 

**[3278.64s] English:** what you encounter is you encounter these types that get weird. So if you're used to Python,  
**Translation:** 

**[3284.86s] English:** you think about everything. I can just copy it around. I can go change it and mutate it and do  
**Translation:** Vocabulary: mutate: 变异

**[3289.48s] English:** these things and it's all cool. If you get into systems programming land, you get into these  
**Translation:** 

**[3294.24s] English:** things like I have an atomic number or I have a mutex or I have a  
**Translation:** 

**[3299.12s] English:** students.  
**Translation:** 

**[3299.90s] English:** uniquely owned database handle things like this right so these types you can't necessarily copy  
**Translation:** Vocabulary: uniquely: 独一无二地

**[3305.58s] English:** sometimes you can't necessarily even move them to a different address and so what mojo allows you to  
**Translation:** 

**[3311.16s] English:** do is it allows you to express hey i don't want to get a copy of this thing i want to actually  
**Translation:** 

**[3316.34s] English:** just get a reference to it and by doing that what you can say is you can say okay if i'm defining  
**Translation:** 

**[3320.92s] English:** something weird like a atomic number or something it's like it has to be so an atomic number is a  
**Translation:** 

**[3327.62s] English:** an area in memory that multiple threads can access at a time without synchronous without  
**Translation:** 

**[3332.38s] English:** without locks right and so uh and so like the definition of atomic numbers multiple different  
**Translation:** Vocabulary: synchronous: 同步的

**[3338.54s] English:** things have to be poking it that therefore they have to agree on where it is right so you can't  
**Translation:** 

**[3342.74s] English:** just like move it out from underneath one because it kind of breaks what what it means and so that's  
**Translation:** Vocabulary: poking: 捅戳

**[3347.10s] English:** an example of a type that you can't even you can't copy you can't move it like once you create it has  
**Translation:** 

**[3351.74s] English:** to be where it was right now if you look at many other examples like a database handle right it's  
**Translation:** 

**[3357.62s] English:** so okay well what happens  
**Translation:** 

**[3360.00s] English:** How do you copy a database handle?  
**Translation:** 

**[3361.68s] English:** Do you copy the whole database?  
**Translation:** 

**[3363.00s] English:** That's not something you necessarily want to do.  
**Translation:** 

**[3366.32s] English:** There's a lot of types like that where you want to be able to say that they are uniquely owned.  
**Translation:** 

**[3371.74s] English:** So there's always one of this thing.  
**Translation:** 

**[3375.50s] English:** Or if I create a thing, I don't copy it.  
**Translation:** 

**[3379.44s] English:** And so what Mojo allows you to do is it allows you to say,  
**Translation:** 

**[3382.18s] English:** hey, I want to pass around a reference to this thing without copying it.  
**Translation:** 

**[3384.50s] English:** And so it has borrowed conventions.  
**Translation:** 

**[3386.90s] English:** So you can say you can use it, but you don't get to change it.  
**Translation:** 

**[3391.06s] English:** You can pass it by mutable reference.  
**Translation:** 

**[3393.36s] English:** And so if you do that, then you get a reference to it, but you can change it.  
**Translation:** 

**[3397.44s] English:** And so it manages all that kind of stuff.  
**Translation:** 

**[3399.78s] English:** So it's just a really nice implementation of like C++ has the different kinds of pointers.  
**Translation:** 

**[3407.22s] English:** Yeah, it has pointers.  
**Translation:** Vocabulary: implementation: 实现方式

**[3408.40s] English:** Different kinds of implementations and smart pointers that you can explicitly define.  
**Translation:** 

**[3412.72s] English:** But you're saying that's more like the weird case versus the clunky.  
**Translation:** Vocabulary: clunky: 笨拙的; explicitly: 明确地; implementations: 实现方式

**[3416.90s] English:** Well, it depends on where, I mean, I don't think I'm a normal person.  
**Translation:** 

**[3421.88s] English:** So, I mean, I'm not one to call other people weird.  
**Translation:** 

**[3425.18s] English:** But, you know, if you talk to a normal Python, a typical Python programmer,  
**Translation:** 

**[3430.76s] English:** you're typically not thinking about this, right?  
**Translation:** Vocabulary: programmer: 程序员

**[3432.28s] English:** This is a lower level of abstraction.  
**Translation:** 

**[3434.00s] English:** Now, if you talk to a C++ programmer, certainly if you talk to a Rust programmer,  
**Translation:** Vocabulary: abstraction: 抽象

**[3437.42s] English:** again, they're not weird, they're delightful.  
**Translation:** 

**[3439.54s] English:** Like these are all good people, right?  
**Translation:** 

**[3441.98s] English:** Those folks will think about all the time, right?  
**Translation:** 

**[3444.74s] English:** And so I look at this as there's a spectrum.  
**Translation:** 

**[3446.90s] English:** I mean, very deep, low-level systems.  
**Translation:** 

**[3449.14s] English:** I'm going to go poke the bits and care about how they're laid out in memory  
**Translation:** 

**[3451.78s] English:** all the way up to application and scripting and other things like this.  
**Translation:** 

**[3455.66s] English:** And so it's not that anybody's right or wrong.  
**Translation:** 

**[3457.80s] English:** It's about how do we build one system that scales.  
**Translation:** 

**[3460.98s] English:** By the way, the idea of an atomic number has been something that always brought me deep happiness  
**Translation:** 

**[3470.28s] English:** because the flip side of that,  
**Translation:** 

**[3473.10s] English:** the idea that threads can just,  
**Translation:** 

**[3476.90s] English:** you know, modify stuff is  
**Translation:** 

**[3480.00s] English:** synchronously. The whole idea of concurrent programming is a source of  
**Translation:** Vocabulary: concurrent: 同时发生的

**[3483.70s] English:** infinite stress for me.  
**Translation:** 

**[3485.36s] English:** Again, you zoom out and get out of programming languages or compilers  
**Translation:** Vocabulary: compilers: 编译器

**[3492.04s] English:** and you just look at what the industry has done. My mind is constantly  
**Translation:** 

**[3495.60s] English:** blown by this. And you look at Moore's Law.  
**Translation:** 

**[3500.02s] English:** Moore's Law has this idea that computers, for a long time,  
**Translation:** 

**[3503.42s] English:** single-thread performance just got faster and faster and faster and faster for free.  
**Translation:** 

**[3506.40s] English:** But then physics and other things intervened  
**Translation:** 

**[3510.40s] English:** and power consumption and other things started to matter. And so what ended up happening  
**Translation:** Vocabulary: intervened: 介入

**[3514.28s] English:** is we went from single-core computers to multi-core. Then we went to accelerators.  
**Translation:** 

**[3518.98s] English:** And this trend towards specialization of hardware is only going to  
**Translation:** 

**[3522.40s] English:** continue. And so for years, us programming  
**Translation:** 

**[3526.50s] English:** language nerds and compiler people have been saying, okay, well, how do we  
**Translation:** Vocabulary: nerds: 痴迷者

**[3529.94s] English:** tackle multi-core? For a while, it was like, multi-core is the future. We have to get on top of this  
**Translation:** 

**[3534.46s] English:** thing. And then it was, multi-core is the  
**Translation:** 

**[3536.38s] English:** fault. What are we doing with this thing? And then it's like, there's chips with hundreds of  
**Translation:** 

**[3540.28s] English:** cores in them. What happened? And so  
**Translation:** 

**[3543.70s] English:** I'm super inspired by the fact that, in the face of this,  
**Translation:** 

**[3548.44s] English:** those machine learning people invented this idea of a tensor.  
**Translation:** 

**[3552.82s] English:** And what is a tensor? A tensor is an arithmetic  
**Translation:** 

**[3556.38s] English:** and algebraic concept. It's like an abstraction around a  
**Translation:** Vocabulary: abstraction: 抽象; algebraic: 代数的; arithmetic: 算术的

**[3560.30s] English:** gigantic, parallelizable data set. And because  
**Translation:** 

**[3564.30s] English:** of that, and because of things like TensorFlow and PyTorch, we're able to say, okay, we'll  
**Translation:** Vocabulary: gigantic: 巨大的; parallelizable: 可并行的

**[3567.92s] English:** express the math of the system. This enables you to do  
**Translation:** 

**[3572.22s] English:** automatic differentiations, enables you to do all these cool things.  
**Translation:** Vocabulary: differentiations: 微分计算

**[3576.42s] English:** And it's an abstract representation. Because you have  
**Translation:** 

**[3580.36s] English:** that abstract representation, you can now map it onto these parallel machines without  
**Translation:** 

**[3584.14s] English:** having to control, okay, put that byte here, put that byte there, put that byte  
**Translation:** 

**[3588.32s] English:** there. And this has enabled an explosion in terms of AI, compute,  
**Translation:** 

**[3592.86s] English:** accelerators, all the stuff.  
**Translation:** 

**[3594.30s] English:** And so that's super, super exciting.  
**Translation:** Vocabulary: accelerators: 加速器

**[3596.38s] English:** What about the deployment and the execution across multiple machines?  
**Translation:** 

**[3600.00s] English:** So you write that the modular compute platform dynamically partitions models with billions of parameters and distributes their execution across multiple machines, enabling unparalleled efficiency scale and reliability for the largest workloads.  
**Translation:** Vocabulary: deployment: 部署; distributes: 分配; dynamically: 动态地; modular: 模块化; partitions: 划分; reliability: 可靠性; workloads: 工作负载

**[3622.52s] English:** So how do you do this abstraction of distributed deployment of large models?  
**Translation:** 

**[3652.52s] English:** Yeah. So so if you look at just TensorFlow and PyTorch, which is pretty recent history in the big picture. Right. But TensorFlow is all about graphs. PyTorch, I think, pretty unarguably ended up winning. And why did it win? Mostly because of usability. Right. And the usability of PyTorch is, I think, huge. And I think, again, that's a huge testament to the power of taking abstract theoretical technical concepts and bring it to the masses. Right.  
**Translation:** Vocabulary: testament: 证明; unarguably: 无可争议地; usability: 易用性

**[3680.24s] English:** Now, the challenge with what.  
**Translation:** 

**[3682.52s] English:** The TensorFlow versus the PyTorch design points was that TensorFlow is kind of difficult to use for researchers, but it was actually pretty good for deployment. PyTorch is really good for researchers. It kind of not super great for deployment. Right. And so I think that we as an industry have been struggling. And if you look at what deploying a machine learning model today means is that you'll have researchers who are, I mean, wicked smart, of course, but they're wicked smart at model architecture and data and calculus.  
**Translation:** Vocabulary: calculus: 微积分; deploying: 部署; wicked: 非常聪明

**[3712.52s] English:** And they're wicked smart in various domains. They don't want to know anything about the hardware deployment or C++ or things like this. Right. And so what's.  
**Translation:** 

**[3720.00s] English:** happened is you get people who train the model they throw over throw it over the fence and they  
**Translation:** 

**[3724.36s] English:** have people that try to deploy the model well every time you have a team a does x they throw  
**Translation:** 

**[3732.04s] English:** it over the fence and team y does some team b does y like you have a problem because of course  
**Translation:** Vocabulary: deploy: 部署

**[3738.76s] English:** it never works the first time and so you throw over the fence they figure out okay it's too slow  
**Translation:** 

**[3743.44s] English:** it won't fit doesn't use the right operator the tool crashes whatever the problem is then they  
**Translation:** 

**[3750.50s] English:** have to throw it back over the fence and every time you throw a thing over a fence it takes three  
**Translation:** 

**[3755.30s] English:** weeks of project managers and meetings and things like this and so uh what we've seen today is that  
**Translation:** 

**[3760.16s] English:** getting models in production can take weeks or months like it's not atypical right i talked to  
**Translation:** 

**[3765.14s] English:** lots of people and you talk about like vp of software at some internet company trying to  
**Translation:** 

**[3769.56s] English:** deploy a model and they're like why do i need a team of 45 people  
**Translation:** 

**[3772.54s] English:** you  
**Translation:** 

**[3773.44s] English:** like it's so easy to train a model why why can't i deploy it right and if you dig into this  
**Translation:** 

**[3779.18s] English:** every layer is problematic so if you look at the language piece i mean this is tip of the  
**Translation:** 

**[3784.56s] English:** iceberg it's a very exciting tip of the iceberg for folks but you've got python on one side and  
**Translation:** 

**[3789.68s] English:** c++ on the other side python doesn't really deploy i mean can theoretically technically  
**Translation:** Vocabulary: iceberg: 冰山一角

**[3794.70s] English:** in some cases but often a lot of production teams will want to get things out of python  
**Translation:** 

**[3798.52s] English:** because they get better performance and control and whatever else so mojo can help with that  
**Translation:** 

**[3803.44s] English:** if you look at serving so you talk about gigantic models well a gigantic model won't fit on one  
**Translation:** 

**[3809.26s] English:** machine right and so now you have this model it's written in python it has to be rerun in c++  
**Translation:** Vocabulary: gigantic: 巨大的模型

**[3815.56s] English:** now it also has to be carved up so that half of it runs on one machine half of it runs on another  
**Translation:** 

**[3819.94s] English:** machine or maybe it runs on 10 machines well so now suddenly the complexity is exploding right  
**Translation:** Vocabulary: complexity: 复杂性; exploding: 激增

**[3826.80s] English:** and the reason for this is that if you if you look into tense flow pytorch these systems they weren't  
**Translation:** 

**[3832.78s] English:** really designed to be able to run on one machine so you have to be able to run on one machine and  
**Translation:** 

**[3833.44s] English:** for this world right they were designed for you know back in the day when we were starting and  
**Translation:** 

**[3838.54s] English:** doing things where  
**Translation:** 

**[3840.00s] English:** it was a different much simpler world like you want to run resnet 50 or some ancient model  
**Translation:** 

**[3844.48s] English:** architecture like this it was just a it was a completely different world than rain on one gpu  
**Translation:** 

**[3849.44s] English:** exactly doing alex one gp yeah alex net right in the major breakthrough and um and the world  
**Translation:** 

**[3856.64s] English:** has changed right and so now the challenge is is that tense flow pytorch these systems they  
**Translation:** 

**[3860.80s] English:** weren't actually designed for llms like that that was not that was not a thing and so what where  
**Translation:** 

**[3865.76s] English:** tenseville actually has amazing power in terms of scale and deployment and things like that and i  
**Translation:** Vocabulary: deployment: 部署

**[3870.00s] English:** think google is i mean maybe not unmatched but they're like incredible in terms of their  
**Translation:** 

**[3874.24s] English:** capabilities and gigantic scale um many researchers using pytorch right and so pytorch doesn't have  
**Translation:** 

**[3881.44s] English:** those same capabilities and so what modular can do is it can help with that now if you take a  
**Translation:** 

**[3885.12s] English:** step back and say like what is modular doing right so modular has like a a bitter enemy  
**Translation:** Vocabulary: modular: 模块化

**[3891.76s] English:** that we're fighting against in the industry and it's one of these things where everybody  
**Translation:** 

**[3895.76s] English:** knows it but nobody is usually willing to talk about it the bitter enemy the bitter thing that  
**Translation:** 

**[3903.36s] English:** we have to destroy that we're all struggling with and it's like all right it's like fish can't see  
**Translation:** 

**[3907.28s] English:** water it's complexity sure yes it's complexity right that was very philosophical and so if you  
**Translation:** Vocabulary: philosophical: 哲学的

**[3915.44s] English:** look at it yes it is on the hardware side yes all these all these accelerators all these software  
**Translation:** 

**[3920.72s] English:** stacks that go with the accelerator all these like there's massive complexity over there you look at  
**Translation:** Vocabulary: accelerator: 加速器; accelerators: 加速器

**[3926.08s] English:** what's happening on the modeling side massive amount of complexity like things are changing  
**Translation:** 

**[3930.32s] English:** all the time people are inventing turns out the research is not done right and so people want to  
**Translation:** 

**[3935.20s] English:** be able to move fast transformers are amazing but there's a ton of diversity even within  
**Translation:** 

**[3939.68s] English:** transformers and what's the next transformer right and you look into serving also huge amounts of  
**Translation:** 

**[3946.08s] English:** complexity it turns out that all the cloud providers right have all their very weird but  
**Translation:** 

**[3951.04s] English:** very cool hardware for networking all this kind of stuff and it's all very complicated people aren't  
**Translation:** Vocabulary: complexity: 复杂性

**[3955.76s] English:** doing that you look at classical serving right there there's this whole  
**Translation:** 

**[3960.00s] English:** world of people who know how to write high performance servers with zero copy networking  
**Translation:** 

**[3963.44s] English:** and like all all this fancy asynchronous io and like all these fancy things in the in the serving  
**Translation:** 

**[3969.98s] English:** community very little that has pervaded into the machine learning world right and why is that well  
**Translation:** Vocabulary: asynchronous: 异步的; pervaded: 渗透

**[3975.72s] English:** it's because again these systems have been built up over many years they they haven't been rethought  
**Translation:** 

**[3981.20s] English:** there hasn't been a first principles approach to this and so what modular is doing is we're saying  
**Translation:** 

**[3985.52s] English:** okay we've built many of these things like so i've worked on tensorflow and tpus and things  
**Translation:** 

**[3991.08s] English:** like that other folks on our team like worked on pytorch core we've worked on onyx runtime we've  
**Translation:** Vocabulary: runtime: 运行时环境

**[3996.60s] English:** worked on many of these other systems and so built the systems like the apple accelerators and all  
**Translation:** 

**[4002.04s] English:** that kind of stuff like our team is quite amazing and so one of the things that roughly everybody  
**Translation:** 

**[4007.80s] English:** at modular is grumpy about is that when you're working on one of these projects you have a first  
**Translation:** 

**[4012.64s] English:** order goal get the hardware to work  
**Translation:** Vocabulary: grumpy: 爱发脾气; modular: 模块化

**[4015.20s] English:** get the hardware to work get the hardware to work get the hardware to work get the hardware to work  
**Translation:** 

**[4015.50s] English:** get the system to enable one more model get this product out the door enable the specific  
**Translation:** 

**[4020.40s] English:** workload or make it solve this problem for this this product team right and nobody's been given  
**Translation:** 

**[4025.68s] English:** a chance to actually do that step back and so we as an industry we didn't take two steps forward  
**Translation:** Vocabulary: workload: 工作量

**[4029.96s] English:** we took like 18 steps forward in terms of all this really cool technology across compilers and systems  
**Translation:** 

**[4035.38s] English:** and runtimes and heterogeneous computing like all this kind of stuff and like all this technology  
**Translation:** Vocabulary: compilers: 编译器; computing: 计算; heterogeneous: 异构; runtimes: 运行时

**[4039.46s] English:** has been you know i wouldn't say uh beautifully designed but it's been proven in different  
**Translation:** 

**[4044.82s] English:** quadrants like you know you look at google with tpus massive huge exaflops of compute strapped  
**Translation:** Vocabulary: exaflops: 每秒千万亿次; quadrants: 不同区域; strapped: 配备

**[4051.94s] English:** together and into machines that researchers are programming in python in a notebook that's huge  
**Translation:** 

**[4057.66s] English:** that's amazing that's incredible right it's incredible and so you look at the technology  
**Translation:** 

**[4061.40s] English:** that goes into that and the the algorithms are actually quite general and so lots of other  
**Translation:** 

**[4067.74s] English:** hardware out there and lots of other teams out there don't have the sophistication or maybe the  
**Translation:** Vocabulary: sophistication: 复杂程度

**[4071.94s] English:** the years working on it or the the budget or whatever and so i think it's a really good  
**Translation:** 

**[4074.82s] English:** example of how people are using the same algorithms and and how they're using the same  
**Translation:** 

**[4078.70s] English:** algorithms and and so i think it's a really good example of how people are using the same  
**Translation:** 

**[4080.00s] English:** right and so what modular is doing is we're saying cool this is not research anymore like we've we've  
**Translation:** 

**[4085.52s] English:** built auto tuning in many systems we've built programming languages right and so like have  
**Translation:** 

**[4090.72s] English:** have you know implemented c plus plus have implemented swift have implemented many of  
**Translation:** 

**[4094.08s] English:** these things and so you know this it's hard but it's not research and you look at accelerators  
**Translation:** 

**[4101.52s] English:** well we know there's a bunch of different weird kind of accelerators but they actually cluster  
**Translation:** Vocabulary: accelerators: 加速器; cluster: 聚集

**[4106.00s] English:** together right and you look at gpus well there's a couple of major vendors of gpus and they maybe  
**Translation:** 

**[4111.36s] English:** don't always get along but their architectures are very similar you look at cpus cpus are still  
**Translation:** 

**[4116.32s] English:** super important for the deployment side of things and you see new new architectures coming out from  
**Translation:** 

**[4120.96s] English:** all the cloud providers and things like this and they're all super important to the world  
**Translation:** 

**[4125.04s] English:** right but they don't have the 30 years of development that the entrenched people do  
**Translation:** 

**[4129.36s] English:** right and so what modular can do is we're saying okay all this complexity like it's not it's not  
**Translation:** Vocabulary: complexity: 复杂性; entrenched: 根深蒂固的

**[4136.00s] English:** it's actually innovation right and so it's innovation that's happening and it's for good  
**Translation:** 

**[4142.16s] English:** reasons but i have sympathy for the poor software people right i mean again i'm a generally software  
**Translation:** 

**[4147.84s] English:** person too i love hardware but software people want to build applications and products and  
**Translation:** 

**[4152.64s] English:** solutions that scale over many years they don't want to build a solution for one generation of  
**Translation:** 

**[4158.16s] English:** hardware with one vendor's tools right and because of this they need something that  
**Translation:** 

**[4162.96s] English:** scales with them they need something that works on cloud and they need something that works on  
**Translation:** 

**[4166.00s] English:** mobile right because you know their product manager said hey i want it to be have lower  
**Translation:** 

**[4171.12s] English:** latency and it's better for personalization or whatever they decide right products evolve and so  
**Translation:** Vocabulary: latency: 延迟

**[4177.44s] English:** the challenge with the machine learning technology and the infrastructure we have today in the  
**Translation:** 

**[4181.04s] English:** industry is that it's all these point solutions and because there are all these point solutions  
**Translation:** 

**[4186.08s] English:** it means that as your product evolves you have to like switch different technology stacks or  
**Translation:** 

**[4189.76s] English:** switch to a different vendor and what that does is that slows down progress so basically  
**Translation:** 

**[4196.00s] English:** a lot of the things we've developed in those little uh silos  
**Translation:** 

**[4200.00s] English:** for machine learning tasks you want to make that the first class citizen of a general purpose  
**Translation:** Vocabulary: silos: 独立系统

**[4205.06s] English:** programming language that can then be compiled across all these kinds of hardware well so it's  
**Translation:** 

**[4209.22s] English:** not really about a programming language i mean the programming language is a component of the  
**Translation:** 

**[4212.84s] English:** mission right and the mission is our not literal but our joking mission is to save the world from  
**Translation:** 

**[4217.92s] English:** terrible ai software excellent okay so so you know if you look at this mission you need a syntax  
**Translation:** 

**[4225.90s] English:** so that's so yes you need a programming language right and and like we wouldn't have to build the  
**Translation:** 

**[4231.28s] English:** programming language if one existed right so if python was already good enough then cool we would  
**Translation:** 

**[4235.44s] English:** just used it right we're not just doing very large scale expensive engineering projects for the sake  
**Translation:** 

**[4240.40s] English:** of it like it's to solve a problem right it's also about um uh accelerators it's also about  
**Translation:** 

**[4247.74s] English:** exotic numerics and b float 16 and matrix multiplications and convolutions and like this  
**Translation:** 

**[4252.50s] English:** this kind of stuff um within the stack there are things like uh  
**Translation:** Vocabulary: convolutions: 卷积; matrix: 矩阵; multiplications: 乘法; numerics: 数值

**[4255.90s] English:** kernel fusion that's a esoteric but really important thing that leads to much better  
**Translation:** 

**[4260.90s] English:** performance and much more general research hackability together right and that that's  
**Translation:** Vocabulary: esoteric: 深奥; hackability: 易用性; kernel: 内核

**[4267.52s] English:** enabled by the asics that's enabled by certain hardware so it's like where's the dance between  
**Translation:** 

**[4272.68s] English:** um i mean there's several questions here like how do you add a piece of hardware to this stack  
**Translation:** 

**[4277.86s] English:** yeah if a new piece like if i have this genius invention of a specialized accelerator yeah how  
**Translation:** 

**[4285.08s] English:** do i add that  
**Translation:** 

**[4285.90s] English:** to the modular framework and also how does modular as a standard start to define the kind of  
**Translation:** 

**[4292.44s] English:** hardware that should be developed yeah so let me take a step back and talk about status quo  
**Translation:** Vocabulary: modular: 模块化

**[4297.62s] English:** okay and so um if you go back to tensorflow one pytorch one the this kind of time frame um and  
**Translation:** 

**[4305.84s] English:** these have all evolved and gone way more complicated so let's go back to the the glorious  
**Translation:** 

**[4309.36s] English:** simple days right these things basically were cpus and cuda and so what you do is you say go  
**Translation:** 

**[4315.90s] English:** to a dense layer and a dense layer has a matrix multiplication in it  
**Translation:** Vocabulary: multiplication: 矩阵乘法

**[4320.00s] English:** right and so when you say that you say go do this big operation matrix multiplication  
**Translation:** 

**[4324.80s] English:** and if it's on a gpu kick off a cuda kernel if it's on a cpu go do like an intel algorithm or  
**Translation:** Vocabulary: algorithm: 计算方法

**[4331.84s] English:** something like that with the intel mko okay now that's really cool if you're either nvidia or  
**Translation:** 

**[4337.84s] English:** intel right but then more hardware comes in right and and on one access you have more hardware  
**Translation:** 

**[4344.96s] English:** coming in on the other hand you have an explosion of innovation in ai and so what happened with both  
**Translation:** 

**[4350.16s] English:** tensorflow and pytorch is that the explosion of innovation in ai has led to it's not just  
**Translation:** 

**[4355.28s] English:** about matrix multiplication and convolution these things have now like 2 000 different operators  
**Translation:** 

**[4360.64s] English:** and on the other hand you have i don't know how many pieces of hardware out there are there it's  
**Translation:** Vocabulary: convolution: 卷积运算

**[4364.08s] English:** a lot okay it's it's not it's not even hundreds it's probably thousands okay and across all of  
**Translation:** 

**[4370.08s] English:** edge and across like all all the different things that are used at scale yeah exactly  
**Translation:** 

**[4374.96s] English:** it's not just like everywhere yeah it's not a handful of tpu alternatives correct it's it's  
**Translation:** 

**[4380.80s] English:** it's every phone often with many different right chips inside of it from different vendors right  
**Translation:** 

**[4387.20s] English:** like it's ai is everywhere it's a thing right why are they all making their own chips like  
**Translation:** 

**[4392.72s] English:** why is everybody making their own thing uh well so because is that a good thing for sure so chris's  
**Translation:** 

**[4398.32s] English:** philosophy on hardware yeah right so my philosophy is that there isn't one right solution right  
**Translation:** 

**[4404.96s] English:** and so i think that again we're at the end of moore's law specialization happens yeah if you  
**Translation:** 

**[4409.92s] English:** if you're building if you're training gpt5 you want some crazy supercomputer data center thingy  
**Translation:** 

**[4417.92s] English:** if you're making a smart camera that runs on batteries you want something that looks very  
**Translation:** Vocabulary: supercomputer: 超级计算机

**[4422.80s] English:** different if you're building a phone you want something that looks very different if you have  
**Translation:** 

**[4426.24s] English:** something like a laptop you want something that looks maybe similar but a different scale right  
**Translation:** 

**[4431.04s] English:** and so ai ends up touching all of our lives robotics  
**Translation:** 

**[4434.96s] English:** right and like lots of different things and so as you look into this these have different power  
**Translation:** 

**[4440.00s] English:** envelopes there's different trade-offs in terms of the algorithms there's new innovations and  
**Translation:** 

**[4444.08s] English:** sparsity and other data formats and things like that and so uh hardware innovation i think is a  
**Translation:** Vocabulary: innovations: 创新; sparsity: 稀疏性

**[4449.46s] English:** really good thing right and what i'm interested in is unlocking that innovation there's also like  
**Translation:** 

**[4453.40s] English:** analog and quantum and like all the the the really weird stuff right and so if somebody can come up  
**Translation:** Vocabulary: analog: 模拟; unlocking: 解锁

**[4459.94s] English:** with a chip that uses analog computing and it's 100x more power efficient think what that would  
**Translation:** 

**[4464.42s] English:** mean in terms of the daily impact on the products we use that'd be huge now if you're building an  
**Translation:** Vocabulary: computing: 计算

**[4471.04s] English:** analog computer you may not be a compiler specialist right these are different skill sets right and so  
**Translation:** 

**[4476.82s] English:** you can hire some compiler people if you're running a big company maybe but it turns out  
**Translation:** 

**[4481.30s] English:** these are really uh like exotic new generation of compilers like this this is a different thing  
**Translation:** 

**[4487.66s] English:** right and so if you if you take a step back out and come back to what is the status quo  
**Translation:** Vocabulary: compilers: 编译器

**[4491.24s] English:** status quo is that if you're intelligent  
**Translation:** 

**[4494.42s] English:** or you're in video you continue to keep up with the industry and you chase and  
**Translation:** 

**[4497.72s] English:** okay there's 1900 now there's 2000 now there's 2100 and you have a huge team of people that  
**Translation:** 

**[4503.06s] English:** are like trying to keep up and tune and optimize and even when uh one of the big guys comes out  
**Translation:** Vocabulary: optimize: 优化

**[4507.76s] English:** with a new generation of their chip they have to go back and rewrite all these things right so  
**Translation:** 

**[4512.30s] English:** really it's only powered by having hundreds of people they're all like frantically trying to  
**Translation:** Vocabulary: frantically: 疯狂地

**[4516.76s] English:** keep up and what that does is that keeps out the little guys and sometimes they're not so little  
**Translation:** 

**[4520.96s] English:** guys the big guys that are also just not not in those dominant positions  
**Translation:** 

**[4524.42s] English:** and so um and so what has been happening and so a lot of you talk about the rise of new exotic  
**Translation:** 

**[4531.04s] English:** crazy accelerators is people have been trying to turn this from a let's go write lots of special  
**Translation:** Vocabulary: accelerators: 加速器

**[4535.38s] English:** kernels problem into a compiler problem and so we and i contributed to this as well we as an  
**Translation:** 

**[4542.34s] English:** industry went into it like let's go make this compiler problem phase let's call it and much of  
**Translation:** Vocabulary: kernels: 内核

**[4548.04s] English:** the industry is still in this phase by the way so it's i wouldn't say this phase is over and so the  
**Translation:** 

**[4552.30s] English:** idea is to say look okay  
**Translation:** 

**[4554.42s] English:** what a compiler does is it provides a much more general extensible  
**Translation:** 

**[4558.10s] English:** uh  
**Translation:** Vocabulary: extensible: 可扩展的

**[4560.00s] English:** hackable interface for dealing with the general case right and so um within machine learning  
**Translation:** 

**[4567.68s] English:** algorithms for example people figured out that hey if i do a matrix multiplication and i do a relu  
**Translation:** Vocabulary: hackable: 可破解; interface: 接口; matrix: 矩阵; multiplication: 乘法

**[4572.88s] English:** right the classic activation function it is way faster to do one pass over the data and then do  
**Translation:** 

**[4580.56s] English:** the relu on the output where i'm writing out the data because relu is just a maximum operation  
**Translation:** 

**[4585.92s] English:** right max with zero and so it's an amazing optimization take matmul relu squished together  
**Translation:** 

**[4592.72s] English:** in one operation now i have matmul relu well wait a second if i do that now i just went from having  
**Translation:** Vocabulary: optimization: 优化; squished: 压缩

**[4598.80s] English:** you know two operators to three but now i figure out okay well there's a lot of activation functions  
**Translation:** 

**[4603.52s] English:** what about uh leaky value what about like like a million things that are out there right and  
**Translation:** Vocabulary: leaky: 漏激活

**[4609.36s] English:** so as i start fusing these in now i get permutations of all these algorithms right  
**Translation:** 

**[4614.32s] English:** and so what the compiler people said is they said  
**Translation:** Vocabulary: fusing: 融合; permutations: 排列组合

**[4615.92s] English:** hey cool well i will go enumerate all the algorithms and i will enumerate all the pairs  
**Translation:** 

**[4619.84s] English:** and i will actually generate a kernel for you and i think that this has been very very useful for the  
**Translation:** Vocabulary: enumerate: 列举; kernel: 内核

**[4624.72s] English:** industry this is one of the things that powers google tpus uh pytorch twos like rolling out  
**Translation:** 

**[4629.60s] English:** really cool compiler stuff with triton this other technology and things like this and so the compiler  
**Translation:** Vocabulary: triton: 编译技术

**[4634.88s] English:** people are kind of coming into their four and saying like awesome this is a compiler problem  
**Translation:** 

**[4638.56s] English:** we'll compiler it here's the problem not everybody's a compiler person i love compiler  
**Translation:** 

**[4644.32s] English:** people trust me right but not everybody's a compiler but i love compiler people trust me right  
**Translation:** 

**[4645.92s] English:** i can or should be a compiler person it turns out that they're people that know analog computers  
**Translation:** 

**[4651.20s] English:** really well or they know some gpu internal architecture thing really well or they know  
**Translation:** 

**[4656.48s] English:** some crazy sparse numeric interesting algorithm that is the cusp of research but they're not  
**Translation:** Vocabulary: algorithm: 算法; numeric: 数值的; sparse: 稀疏的

**[4662.56s] English:** compiler people and so one of the challenges with this new wave of technology trying to turn  
**Translation:** 

**[4667.04s] English:** everything into a compiler is again is excluded a ton of people and so you look at what does mojo  
**Translation:** Vocabulary: excluded: 排除

**[4673.04s] English:** do what does the modular stack do this brings programming  
**Translation:** 

**[4675.92s] English:** ability back into this world like it enables i wouldn't say normal people  
**Translation:** Vocabulary: modular: 模块化

**[4680.00s] English:** people, but like a new, you know,  
**Translation:** 

**[4681.92s] English:** a different kind of delightful nerd that cares about numerics or cares about  
**Translation:** 

**[4685.40s] English:** hardware or cares about things like this to be able to express that in the  
**Translation:** 

**[4688.56s] English:** stack and extend the stack without having to actually go hack the compiler  
**Translation:** 

**[4692.20s] English:** itself.  
**Translation:** 

**[4692.84s] English:** So extend the stack on the, on the algorithm side.  
**Translation:** 

**[4695.86s] English:** Yeah.  
**Translation:** 

**[4696.48s] English:** And then on the hardware side.  
**Translation:** 

**[4698.42s] English:** Yeah.  
**Translation:** 

**[4698.66s] English:** So again, go back to like the simplest example of int, right?  
**Translation:** 

**[4701.56s] English:** And so what both Swift and Mojo and other things like this did is we said,  
**Translation:** 

**[4705.22s] English:** okay,  
**Translation:** 

**[4705.68s] English:** pull magic out of the compiler and put it in the standard library.  
**Translation:** 

**[4708.76s] English:** Right.  
**Translation:** 

**[4709.16s] English:** And so what modular is doing with the engine that we're providing and like  
**Translation:** 

**[4711.90s] English:** this, this very deep technology stack, right.  
**Translation:** 

**[4714.60s] English:** Which goes into heterogeneous runtimes and like a whole bunch of really cool,  
**Translation:** 

**[4718.60s] English:** really cool things.  
**Translation:** Vocabulary: heterogeneous: 异构的; runtimes: 运行时环境

**[4720.62s] English:** This,  
**Translation:** 

**[4721.18s] English:** this whole stack allows that stack to be extended and hacked and changed by  
**Translation:** Vocabulary: hacked: 破解

**[4725.84s] English:** researchers and by hardware innovators and by people who know things that we  
**Translation:** 

**[4730.28s] English:** don't know.  
**Translation:** Vocabulary: innovators: 创新者

**[4731.46s] English:** Cause you know,  
**Translation:** 

**[4732.28s] English:** modular has some smart people,  
**Translation:** 

**[4733.24s] English:** but we don't have all the smart people it turns out.  
**Translation:** 

**[4735.16s] English:** Right.  
**Translation:** 

**[4735.94s] English:** What are heterogeneous runtimes?  
**Translation:** 

**[4737.92s] English:** Yeah.  
**Translation:** 

**[4738.24s] English:** So,  
**Translation:** 

**[4738.48s] English:** so what is,  
**Translation:** 

**[4740.54s] English:** what is heterogeneous,  
**Translation:** 

**[4741.24s] English:** right?  
**Translation:** 

**[4741.42s] English:** So heterogeneous just means many different kinds of things together.  
**Translation:** 

**[4744.54s] English:** And so the simple simplest example you might come up with is a CPU and a  
**Translation:** 

**[4748.28s] English:** GPU.  
**Translation:** 

**[4749.54s] English:** And so it's a simple heterogeneous computer to say,  
**Translation:** 

**[4752.46s] English:** I will run my data loading and pre-processing and other algorithms on the  
**Translation:** 

**[4755.64s] English:** CPU.  
**Translation:** 

**[4756.58s] English:** And then once I get it into the right shape,  
**Translation:** 

**[4758.16s] English:** I shove it into the GPU.  
**Translation:** Vocabulary: shove: 硬塞

**[4759.54s] English:** I do a lot of matrix multiplications and convolutions and things like this,  
**Translation:** 

**[4763.24s] English:** and I get it back out and I do some reductions and summaries and they shove  
**Translation:** Vocabulary: convolutions: 卷积; matrix: 矩阵; multiplications: 乘法

**[4767.34s] English:** it across the wire.  
**Translation:** 

**[4768.26s] English:** They're across the network to another machine.  
**Translation:** 

**[4770.96s] English:** Right.  
**Translation:** 

**[4771.26s] English:** And so you've got now what are effectively two computers,  
**Translation:** 

**[4776.06s] English:** a CPU and a GPU talking to each other,  
**Translation:** 

**[4778.34s] English:** working together in a heterogeneous system.  
**Translation:** 

**[4780.98s] English:** Um,  
**Translation:** 

**[4782.12s] English:** but that was 10 years ago.  
**Translation:** 

**[4784.28s] English:** Okay.  
**Translation:** 

**[4785.18s] English:** You look at a modern cell phone,  
**Translation:** 

**[4787.34s] English:** modern cell phone,  
**Translation:** 

**[4788.00s] English:** you've got CPUs and they're not just CPUs.  
**Translation:** 

**[4791.12s] English:** There's like big dot,  
**Translation:** 

**[4792.00s] English:** little CPUs.  
**Translation:** 

**[4793.04s] English:** And so there's multiple different kinds of CPUs that are kind of working  
**Translation:** 

**[4795.44s] English:** together.  
**Translation:** 

**[4796.20s] English:** They're multi-core.  
**Translation:** 

**[4797.32s] English:** You've got GPUs,  
**Translation:** 

**[4798.12s] English:** you've got neural network.  
**Translation:** 

**[4800.00s] English:** accelerators you got dedicated hardware blocks for for media so for video decode and jpeg decode  
**Translation:** Vocabulary: accelerators: 专用加速器; neural: 神经网络

**[4806.50s] English:** and things like this and so you've got this massively complicated system and this isn't  
**Translation:** 

**[4809.88s] English:** just cell phones every laptop these days is doing the same thing and all these blocks can run at the  
**Translation:** Vocabulary: massively: 大规模地

**[4815.06s] English:** same time and need to be choreographed right and so again one of the cool things about machine  
**Translation:** 

**[4821.78s] English:** learning is it's moving things to like data flow graphs and higher level of abstractions and tensors  
**Translation:** Vocabulary: abstractions: 抽象层次; choreographed: 协调动作

**[4826.34s] English:** and these things that it doesn't specify here's how to do the algorithm it gives the system a lot  
**Translation:** 

**[4831.92s] English:** more flexibility in terms of how to translate or map or compile it onto the system that you have  
**Translation:** Vocabulary: algorithm: 算法; flexibility: 灵活性

**[4836.72s] English:** and so what you need you know at the bottom is part of the layer there is a way for all these  
**Translation:** 

**[4841.58s] English:** devices to talk to each other and so this is one thing that you know i'm very passionate about i  
**Translation:** 

**[4845.78s] English:** i mean you know i'm a nerd but um but all these all these machines and all these systems are  
**Translation:** 

**[4851.46s] English:** effectively parallel computers running at the same time sending messages to each other  
**Translation:** 

**[4856.32s] English:** and so they're all fully asynchronous well this is actually a small version of the same problem  
**Translation:** 

**[4861.66s] English:** you have in a data center right in a data center you now have multiple different machines sometimes  
**Translation:** Vocabulary: asynchronous: 非同步

**[4866.66s] English:** very specialized sometimes with gpus or tpus in one node and sometimes with disks and other nodes  
**Translation:** 

**[4872.02s] English:** and so you get a much larger scale heterogeneous computer and so what ends up happening is you have  
**Translation:** Vocabulary: heterogeneous: 异构的

**[4877.32s] English:** this like multi-layer abstraction of hierarchical parallelism hierarchical asynchronous communication  
**Translation:** 

**[4883.78s] English:** and making that again the enemy  
**Translation:** Vocabulary: abstraction: 抽象; hierarchical: 层次的

**[4886.32s] English:** my enemy is complexity by getting that away from being different specialized systems at every  
**Translation:** 

**[4892.08s] English:** different part of the stack and having more consistency and uniformity i think we can help  
**Translation:** Vocabulary: complexity: 复杂性

**[4896.60s] English:** lift the world and make it much simpler and actually get used but how do you leverage like  
**Translation:** 

**[4900.84s] English:** the strengths of the different specialized systems so we're looking inside the smartphone  
**Translation:** Vocabulary: leverage: 利用

**[4904.38s] English:** yeah like there's just what i don't know five six computers essentially inside the smartphone  
**Translation:** 

**[4909.34s] English:** uh how do you uh without trying to minimize the explicit  
**Translation:** Vocabulary: explicit: 明确的

**[4916.32s] English:** uh making it explicit which which computer is supposed to be useful  
**Translation:** 

**[4920.00s] English:** operation yeah so there's there's a pretty well-known algorithm and what you're doing  
**Translation:** 

**[4923.94s] English:** is you're looking at two two factors you're looking at the factor of sending data from  
**Translation:** 

**[4927.78s] English:** one thing to another right because it takes time to get it from that side of the chip to that side  
**Translation:** 

**[4931.50s] English:** of the chip and things like this and then you're looking at what is the time it takes to do an  
**Translation:** 

**[4936.00s] English:** operation on a particular block so take cpus cpus are fully general they can do anything right but  
**Translation:** 

**[4943.84s] English:** then you have a neural net accelerator that's really good at matrix multiplications okay and  
**Translation:** 

**[4948.16s] English:** so you say okay well if my workload is all matrix multiplications i start up i send the data over  
**Translation:** Vocabulary: accelerator: 加速器; matrix: 矩阵; multiplications: 乘法; neural: 神经; workload: 工作量

**[4953.22s] English:** the neural net thing it goes and does matrix multiplications when it's done it sends me back  
**Translation:** 

**[4957.26s] English:** the result all is good right and so the simplest thing is just saying do matrix do matrix operations  
**Translation:** 

**[4963.20s] English:** over there right but then you realize you get a little bit more complicated because you can do  
**Translation:** 

**[4967.54s] English:** matrix multiplications on a gpu you can do it on a neural net accelerator you can do it on cpu  
**Translation:** 

**[4973.64s] English:** and they'll have different trade-offs and costs and it's not just matrix multiplication  
**Translation:** 

**[4977.50s] English:** and  
**Translation:** Vocabulary: multiplication: 乘法

**[4978.16s] English:** so what you actually look at is you look at i have generally a graph of compute i want to do  
**Translation:** 

**[4983.62s] English:** a partitioning i want to look at the communication the bisection bandwidth and like the overhead and  
**Translation:** Vocabulary: bandwidth: 带宽; bisection: 二分; partitioning: 划分

**[4989.22s] English:** the sending of all these different things and and build a model for this and then decide okay  
**Translation:** 

**[4994.04s] English:** it's an optimization problem where do i want to place this compute so it's the old school  
**Translation:** Vocabulary: optimization: 最优化

**[4999.04s] English:** theoretical computer science problem of scheduling and then how does uh presumably it's possible to  
**Translation:** 

**[5006.50s] English:** somehow magically include  
**Translation:** Vocabulary: presumably: 似乎

**[5008.16s] English:** autotune into this absolutely so i mean in my opinion this is an opinion this is not uh not  
**Translation:** 

**[5015.82s] English:** everybody would agree with this but in my opinion the world benefits from simple and predictable  
**Translation:** Vocabulary: autotune: 自动调谐; predictable: 可预测的

**[5020.54s] English:** systems at the bottom that you can control but then once you have a predictable execution layer  
**Translation:** 

**[5026.64s] English:** you can build lots of different policies on top of it right and so one policy can be that  
**Translation:** 

**[5031.52s] English:** the human programmer says do that here do that here do that here do that here and like  
**Translation:** 

**[5038.16s] English:** this you have a set of these kind of defaults that you can do what you want it to do for the  
**Translation:** 

**[5049.62s] English:** function and then that's what really sets it up so if you build aNET you can do this the way it would  
**Translation:** 

**[5050.62s] English:** otherwise and that's when at the end of the day you need to build your own code so here's a couple  
**Translation:** 

**[5052.04s] English:** things to consider before we end the video you just need to know that the data server does not  
**Translation:** 

**[5054.74s] English:** necessarily control everything the human programmer has to do this to know that it can control it  
**Translation:** 

**[5056.66s] English:** individually and that's why we've been able to explore these applications and to type out the  
**Translation:** 

**[5058.54s] English:** information into that that you want and then we're going to go over these in the next slide  
**Translation:** Vocabulary: individually: 单独地

**[5060.78s] English:** that we need to take a look at so the the following is a little bit more detailed but we're  
**Translation:** 

**[5062.70s] English:** going to go over this completely a lot and we're going to talk about the other things so  
**Translation:** 

**[5040.00s] English:** and the system should just do it right then you quickly get in the mode of like i don't want to  
**Translation:** 

**[5044.50s] English:** have to tell it to do it yeah and so the next logical step that people typically take is they  
**Translation:** 

**[5048.92s] English:** write some terrible heuristic oh if it's a major multiplication do it over there or if it's  
**Translation:** 

**[5053.80s] English:** floating point do it on the gpu if it's integer do it on the cpu like something like that right  
**Translation:** Vocabulary: heuristic: 启发式; integer: 整数

**[5057.10s] English:** and and then you you then get into this mode of like people care more and more and more and you  
**Translation:** 

**[5062.36s] English:** say okay well let's actually um like make the heuristic better let's get into auto tuning let's  
**Translation:** 

**[5067.88s] English:** actually do a search of the space to decide well what is actually better right well then you get  
**Translation:** 

**[5076.30s] English:** into this problem where you realize this is not a small space this is a many-dimensional  
**Translation:** 

**[5079.62s] English:** hyper-dimensional space that you cannot exhaustively search so do you know of any  
**Translation:** 

**[5086.56s] English:** algorithms that are good at searching very complicated spaces for don't tell me you're  
**Translation:** Vocabulary: cannot: 不能; exhaustively: 彻底地

**[5090.98s] English:** going to turn this into a machine learning problem so then you turn into a machine learning problem  
**Translation:** 

**[5095.10s] English:** and then you have a space of genetic algorithms and reinforcements  
**Translation:** Vocabulary: reinforcements: 加强部队

**[5097.88s] English:** learning and like all these all these but can you include that into the stack into the into the  
**Translation:** 

**[5103.34s] English:** modular stack yeah yeah and where does it sit where does it live is it separate thing or is  
**Translation:** Vocabulary: modular: 模块化

**[5107.40s] English:** it part of the compilation so you start from simple and predictable models and so you can  
**Translation:** 

**[5112.42s] English:** have full control and you can have coarse grain knobs that like nudge nudge systems you don't  
**Translation:** Vocabulary: compilation: 汇编; knobs: 旋钮; nudge: 微调

**[5117.54s] English:** have to do this but if you really care about getting the best you know the last ounce out of  
**Translation:** 

**[5122.34s] English:** a problem then you can use additional tools and they're the cool thing is you don't want to do  
**Translation:** 

**[5126.74s] English:** this every time you run a model  
**Translation:** 

**[5127.88s] English:** you want to figure out the right answer and then cash it and once you do that you can get you can  
**Translation:** 

**[5133.46s] English:** say okay cool i can get up and running very quickly i can get good execution out of my system i can  
**Translation:** 

**[5140.26s] English:** decide if something's important and if it's important i can go throw a bunch of machines  
**Translation:** 

**[5143.72s] English:** at it and do a big expensive search over the space using whatever technique i feel like it's  
**Translation:** 

**[5148.38s] English:** really up to the problem and then when i get the right answer cool i can just start using it  
**Translation:** 

**[5152.34s] English:** right and so you can get out of this um this trade-off between okay am i going to like spend  
**Translation:** 

**[5157.88s] English:** forever doing a thing or do i get up and running quick  
**Translation:** 

**[5160.00s] English:** and is a quality result.  
**Translation:** 

**[5161.66s] English:** These are actually not in contention with each other  
**Translation:** Vocabulary: contention: 竞争

**[5164.98s] English:** if the system is designed to scale.  
**Translation:** 

**[5167.10s] English:** You started and did a little bit of a whirlwind overview  
**Translation:** Vocabulary: whirlwind: 旋风式

**[5170.82s] English:** of how you get the 35,000x speedup or more over Python.  
**Translation:** 

**[5177.72s] English:** Jeremy Howard did a really great presentation  
**Translation:** Vocabulary: speedup: 加速倍数

**[5179.64s] English:** about sort of the basic, like, look at the code,  
**Translation:** 

**[5182.44s] English:** here's how you get the speedup.  
**Translation:** 

**[5183.86s] English:** Like you said, that's something probably developers can do  
**Translation:** 

**[5187.26s] English:** for their own code to see how you can get  
**Translation:** 

**[5189.56s] English:** this gigantic speedup.  
**Translation:** 

**[5191.16s] English:** But can you maybe speak to the machine learning task in general?  
**Translation:** Vocabulary: gigantic: 巨大的

**[5194.14s] English:** How do you make some of this code fast, some specifics?  
**Translation:** 

**[5196.94s] English:** Like, what would you say is the main bottleneck  
**Translation:** Vocabulary: bottleneck: 瓶颈

**[5199.98s] English:** for machine learning tasks?  
**Translation:** 

**[5204.82s] English:** So are we talking about matmul, matrix multiplication?  
**Translation:** Vocabulary: matrix: 矩阵; multiplication: 乘法

**[5209.04s] English:** How do you make that fast?  
**Translation:** 

**[5210.32s] English:** So, I mean, if you just look at the Python problem, right,  
**Translation:** 

**[5212.84s] English:** you can say, how do I make Python faster?  
**Translation:** 

**[5215.92s] English:** And there's been a lot of people that have been working on the,  
**Translation:** 

**[5218.18s] English:** okay, how do I make Python 2?  
**Translation:** 

**[5219.56s] English:** 10x faster, 10x faster, or something like that, right?  
**Translation:** 

**[5221.48s] English:** And there have been a ton of projects in that vein, right?  
**Translation:** 

**[5224.30s] English:** Mojo started from the, what can the hardware do?  
**Translation:** 

**[5228.32s] English:** Like, what is the limit of physics?  
**Translation:** 

**[5229.82s] English:** What is the speed of light?  
**Translation:** 

**[5231.06s] English:** What is the, like, how fast can this thing go?  
**Translation:** 

**[5233.22s] English:** And then, how do I express that?  
**Translation:** 

**[5235.56s] English:** Right, and so it wasn't anchored relatively on  
**Translation:** 

**[5238.48s] English:** make Python a little bit faster.  
**Translation:** Vocabulary: anchored: 固定

**[5240.24s] English:** It's saying, cool, I know what the hardware can do.  
**Translation:** 

**[5242.58s] English:** Let's unlock that, right?  
**Translation:** 

**[5243.86s] English:** Now, when you, right now.  
**Translation:** 

**[5245.66s] English:** You can just say how gutsy that is to be in the meeting  
**Translation:** Vocabulary: gutsy: 勇敢

**[5248.86s] English:** and, you know, be in the meeting.  
**Translation:** 

**[5249.56s] English:** As opposed to trying to see, how do we get the improvement?  
**Translation:** 

**[5251.78s] English:** It's like, what can the physics do?  
**Translation:** 

**[5253.80s] English:** I mean, maybe I'm a special kind of nerd,  
**Translation:** 

**[5255.88s] English:** but you look at that, what is the limit of physics?  
**Translation:** 

**[5258.62s] English:** How fast can these things go, right?  
**Translation:** 

**[5261.40s] English:** When you start looking at that,  
**Translation:** 

**[5262.86s] English:** typically, it ends up being a memory problem, right?  
**Translation:** 

**[5265.52s] English:** And so today, particularly with these specialized accelerators,  
**Translation:** 

**[5269.38s] English:** the problem is that you can do a lot of math within them,  
**Translation:** Vocabulary: accelerators: 加速器

**[5272.84s] English:** but you get bottleneck sending data back and forth to memory,  
**Translation:** 

**[5276.32s] English:** whether it be local memory or distant memory,  
**Translation:** 

**[5279.56s] English:** or distant memory.  
**Translation:** 

**[5280.00s] English:** or whatever it is and and that that bottleneck particularly as the training sizes get large  
**Translation:** 

**[5285.20s] English:** as you start doing tons of inferences all all over the place like that becomes a huge bottleneck for  
**Translation:** 

**[5290.24s] English:** people right so again what happened is we went through a phase of many years where people took  
**Translation:** Vocabulary: inferences: 推断

**[5296.16s] English:** the special case and hand tuned it and tweaked it and tricked it out and they knew exactly how  
**Translation:** 

**[5300.48s] English:** the hardware worked and they knew the model and they made it they made it fast didn't generalize  
**Translation:** Vocabulary: generalize: 泛化; tweaked: 调整

**[5304.64s] English:** and so you can make you know resident 50 or some or alex net or something inception v1 like you can  
**Translation:** 

**[5310.64s] English:** you can do that right because the models are small they fit in your head right but as the models get  
**Translation:** Vocabulary: inception: 创生

**[5316.16s] English:** bigger more complicated as the machines get more complicated it stops working right and so this is  
**Translation:** 

**[5321.28s] English:** where things like kernel fusion come in so what is kernel fusion this is this idea of saying let's  
**Translation:** 

**[5327.20s] English:** avoid going to memory and let's do that by building a new hybrid kernel and a numerical algorithm  
**Translation:** 

**[5334.64s] English:** that actually keeps things in the accelerator instead of having to write all the way out to  
**Translation:** Vocabulary: accelerator: 加速器; algorithm: 算法; kernel: 内核; numerical: 数值的

**[5339.12s] English:** memory right what's happened with with these accelerators now you get multiple levels of  
**Translation:** 

**[5343.68s] English:** memory like in a gpu for example you'll have global memory and local memory and like all these things  
**Translation:** 

**[5350.40s] English:** if you zoom way into how hardware works the register file is actually a memory so the  
**Translation:** 

**[5356.32s] English:** registers are like an l0 cache and so a lot of taking advantage of the hardware ends up being  
**Translation:** Vocabulary: cache: 高速缓存

**[5363.68s] English:** fully used  
**Translation:** 

**[5364.64s] English:** utilizing the full power in all of its capability and this has a number of problems right one of  
**Translation:** Vocabulary: capability: 能力; utilizing: 利用

**[5370.96s] English:** which is again the complexity of disaster right there's too much hardware even if you just say  
**Translation:** 

**[5375.84s] English:** let's look at the chips from one line of vendor like apple or intel or whatever it is  
**Translation:** 

**[5381.92s] English:** each version of the chip comes out with new features and they change things so that it  
**Translation:** 

**[5386.32s] English:** takes more time or less time to do different things and you can't rewrite all the software  
**Translation:** 

**[5390.08s] English:** whenever a new chip comes out right and so this is where you need a much more scalable approach  
**Translation:** 

**[5394.64s] English:** and this is what mojo and what the modular stack provides is it provides this infrastructure and  
**Translation:** Vocabulary: modular: 模块化; scalable: 可扩展

**[5400.00s] English:** for factoring all this complexity  
**Translation:** 

**[5401.66s] English:** and then allowing people to express algorithms.  
**Translation:** Vocabulary: complexity: 复杂性; factoring: 简化

**[5404.14s] English:** You talk about auto-tuning, for example,  
**Translation:** 

**[5406.48s] English:** express algorithms in a more portable way  
**Translation:** 

**[5408.70s] English:** so that when a new chip comes out,  
**Translation:** 

**[5410.68s] English:** you don't have to rewrite it all.  
**Translation:** 

**[5413.54s] English:** So to me, I kind of joke, what is a compiler?  
**Translation:** 

**[5416.88s] English:** Well, there's many ways to explain that.  
**Translation:** 

**[5419.38s] English:** You convert thing A into thing B  
**Translation:** 

**[5421.26s] English:** and you convert source code to machine code.  
**Translation:** 

**[5423.54s] English:** You can talk about many, many things that compilers do.  
**Translation:** 

**[5427.96s] English:** But to me, it's about a bag of tricks.  
**Translation:** Vocabulary: compilers: 编译器

**[5430.78s] English:** It's about a system and a framework  
**Translation:** 

**[5432.48s] English:** that you can hang complexity.  
**Translation:** 

**[5435.04s] English:** It's a system that can then generalize  
**Translation:** 

**[5436.98s] English:** and it can work on problems that are bigger  
**Translation:** Vocabulary: generalize: 泛化

**[5438.44s] English:** than fit in one human's head, right?  
**Translation:** 

**[5441.34s] English:** And so what that means, what a good stack  
**Translation:** 

**[5443.82s] English:** and what the modular stack provides  
**Translation:** 

**[5445.50s] English:** is the ability to walk up to it with a new problem  
**Translation:** 

**[5448.66s] English:** and it'll generally work quite well.  
**Translation:** 

**[5451.34s] English:** And that's something that a lot of machine learning  
**Translation:** 

**[5452.88s] English:** infrastructure and tools and technologies don't have.  
**Translation:** 

**[5456.54s] English:** Typical state of the art today is you walk up,  
**Translation:** 

**[5458.72s] English:** particularly if you're deploying,  
**Translation:** 

**[5459.60s] English:** if you walk up with a new model,  
**Translation:** 

**[5461.20s] English:** you try to push it through the converter  
**Translation:** 

**[5462.50s] English:** and the converter crashes.  
**Translation:** Vocabulary: converter: 转换器

**[5466.10s] English:** That's crazy.  
**Translation:** 

**[5467.46s] English:** The state of ML tooling today  
**Translation:** 

**[5469.64s] English:** is not anything that a C programmer would ever accept, right?  
**Translation:** 

**[5473.60s] English:** And it's always been this kind of flaky set of tooling  
**Translation:** Vocabulary: flaky: 不稳定的; programmer: 程序员

**[5476.54s] English:** that's never been integrated well  
**Translation:** 

**[5477.86s] English:** and it's been never worked together  
**Translation:** 

**[5480.88s] English:** because it's not designed together.  
**Translation:** 

**[5482.94s] English:** It's built by different teams.  
**Translation:** 

**[5484.14s] English:** It's built by different hardware vendors.  
**Translation:** 

**[5485.56s] English:** It's built by different systems.  
**Translation:** 

**[5486.80s] English:** It's built by different internet companies  
**Translation:** 

**[5488.26s] English:** that are trying to solve their,  
**Translation:** 

**[5489.14s] English:** their problems, right?  
**Translation:** 

**[5490.70s] English:** And so that means that we get this fragmented,  
**Translation:** Vocabulary: fragmented: 支离破碎

**[5493.58s] English:** terrible mess of complexity.  
**Translation:** 

**[5495.76s] English:** So, I mean, the specifics of,  
**Translation:** 

**[5497.74s] English:** and Jeremy showed this,  
**Translation:** 

**[5499.40s] English:** there's the vectorized function,  
**Translation:** 

**[5500.68s] English:** which I guess is built into Mojo.  
**Translation:** 

**[5507.36s] English:** Vectorized, as he showed, is built into the library.  
**Translation:** Vocabulary: vectorized: 向量化的

**[5509.40s] English:** Into the library, instead of the library.  
**Translation:** 

**[5512.06s] English:** Vectorized, parallelized,  
**Translation:** 

**[5513.98s] English:** which vectorized is more low level,  
**Translation:** 

**[5516.52s] English:** parallelized is higher level.  
**Translation:** 

**[5518.20s] English:** There's the tiling,  
**Translation:** 

**[5519.14s] English:** which is how he,  
**Translation:** 

**[5520.00s] English:** demonstrated the um autotune i think so so think of think about this in like levels hierarchical  
**Translation:** 

**[5527.82s] English:** levels of abstraction right and so at the very if you zoom all the way into a compute problem you  
**Translation:** Vocabulary: abstraction: 抽象; autotune: 自动校准; hierarchical: 层次分明的

**[5533.34s] English:** have one floating point number right and so then you say okay i want to be i can do things one at  
**Translation:** 

**[5538.06s] English:** a time in an interpreter it's pretty slow right so i can get to doing one one at a time in a compiler  
**Translation:** Vocabulary: interpreter: 解释器

**[5544.60s] English:** i can see then i can get to doing four or eight or sixteen at a time with vectors that's called  
**Translation:** 

**[5551.08s] English:** vectorization then you can say hey i have a whole bunch of different you know what what a multi-core  
**Translation:** Vocabulary: vectorization: 向量处理

**[5557.02s] English:** computer is is basically a bunch of computers right so they're all independent computers that  
**Translation:** 

**[5562.62s] English:** they can talk to each other and they share memory and so now what parallelize does it says okay  
**Translation:** 

**[5567.16s] English:** run multiple instances on different computers and now they can all work together on chrome  
**Translation:** 

**[5571.94s] English:** right and so what you're doing is you're saying keep going out  
**Translation:** 

**[5574.58s] English:** to the next level out and and as you do that how do i take advantage of this so tiling is  
**Translation:** 

**[5580.74s] English:** a memory optimization right it says okay let's make sure that we're keeping the data close to  
**Translation:** Vocabulary: optimization: 优化

**[5585.62s] English:** the compute part of the problem instead of sending it all back and forth through memory  
**Translation:** 

**[5590.74s] English:** every every time i load a block and the size of the block size is as all that's how you get to  
**Translation:** 

**[5595.86s] English:** the auto tune to make sure it's optimized yeah well so all of these the details matter so much  
**Translation:** 

**[5600.18s] English:** to get good performance um this is another funny thing about machine learning and high  
**Translation:** Vocabulary: optimized: 优化

**[5604.42s] English:** performance is that it's it's it's it's it's it's it's it's it's it's it's it's it's it's it's  
**Translation:** 

**[5604.58s] English:** performance computing that is very different than c compilers we all grew up grew up with where  
**Translation:** Vocabulary: compilers: 编译器; computing: 计算

**[5610.20s] English:** you know if you get a new version of gcc or new version of clang or something like that  
**Translation:** 

**[5614.64s] English:** you know maybe something will go one percent faster right and so compiler engineers will work  
**Translation:** Vocabulary: clang: 编译器

**[5621.24s] English:** really really really hard to get half a percent out of your c code something like that but when  
**Translation:** 

**[5626.88s] English:** you're talking about an accelerator or an ai application or you're talking about these kinds  
**Translation:** 

**[5631.76s] English:** of algorithms and these are things people used to write down and they're not going to be able to  
**Translation:** 

**[5634.58s] English:** write in fortran for example right if you get it wrong it's not five percent or one percent  
**Translation:** 

**[5640.00s] English:** It could be 2x or 10x, right?  
**Translation:** 

**[5643.00s] English:** If you think about it, you really want to make use of the full memory you have, the cache, for example.  
**Translation:** Vocabulary: cache: 缓存

**[5649.04s] English:** But if you use too much space, it doesn't fit in the cache.  
**Translation:** 

**[5651.76s] English:** Now you're going to be thrashing all the way back out to main memory.  
**Translation:** Vocabulary: thrashing: 频繁置换

**[5654.78s] English:** And these can be 2x, 10x, major performance differences.  
**Translation:** 

**[5658.34s] English:** And so this is where getting these magic numbers and these things right is really actually quite important.  
**Translation:** 

**[5664.06s] English:** So you mentioned that Moji is a superset of Python.  
**Translation:** 

**[5667.14s] English:** Can you run Python code as if it's Mojo code?  
**Translation:** 

**[5676.44s] English:** Yes.  
**Translation:** 

**[5677.20s] English:** Yes.  
**Translation:** 

**[5678.58s] English:** And this has two sides of it.  
**Translation:** 

**[5681.30s] English:** So Mojo's not done yet.  
**Translation:** 

**[5682.62s] English:** So I'll give you a disclaimer.  
**Translation:** 

**[5683.66s] English:** Mojo's not done yet.  
**Translation:** 

**[5684.42s] English:** But already we see people that take small pieces of Python code, move it over, they don't change it, and you can get 12x speedups.  
**Translation:** 

**[5692.82s] English:** Somebody was just tweeting about that yesterday, which is pretty cool.  
**Translation:** Vocabulary: speedups: 加速倍数; tweeting: 发推文

**[5696.04s] English:** And again, interpretation.  
**Translation:** 

**[5697.30s] English:** First, compilers, right?  
**Translation:** 

**[5698.12s] English:** And so without changing any code, without – also, this is not JIT compiling or doing anything fancy.  
**Translation:** 

**[5705.14s] English:** This is just basic stuff.  
**Translation:** Vocabulary: compiling: 编译

**[5707.20s] English:** Move it straight over.  
**Translation:** 

**[5708.48s] English:** Now, Mojo will continue to grow out.  
**Translation:** 

**[5710.26s] English:** And as it grows out, it will have more and more and more features.  
**Translation:** 

**[5713.22s] English:** And our North Star is to be a full superset of Python.  
**Translation:** 

**[5715.86s] English:** And so you can bring over basically arbitrary Python code and have it just work.  
**Translation:** 

**[5720.42s] English:** And it may not always be 12x faster, but it should be at least as fast and way faster in many cases.  
**Translation:** 

**[5726.42s] English:** This is the goal.  
**Translation:** 

**[5727.38s] English:** Right.  
**Translation:** 

**[5729.28s] English:** Now, it'll take time to do that.  
**Translation:** 

**[5731.08s] English:** And Python is a complicated language.  
**Translation:** 

**[5732.48s] English:** There's not just the obvious things, but there's also non-obvious things that are complicated.  
**Translation:** 

**[5737.56s] English:** Like, we have to be able to talk to CPython packages that talk to the CAPI.  
**Translation:** 

**[5742.00s] English:** And there's a bunch of pieces to this.  
**Translation:** 

**[5744.52s] English:** So you have to – I mean, just to make explicit the obvious, it may not be so obvious until you think about it.  
**Translation:** Vocabulary: explicit: 明确的

**[5751.20s] English:** So, you know, to run Python code, that means you have to run all the Python packages and libraries.  
**Translation:** 

**[5756.82s] English:** Yeah.  
**Translation:** 

**[5757.14s] English:** Yeah.  
**Translation:** 

**[5757.82s] English:** So that means what?  
**Translation:** 

**[5759.68s] English:** How?  
**Translation:** 

**[5760.00s] English:** What's the relationship between Mojo and CPython, the interpreter that presumably would be tasked with getting those packages to work?  
**Translation:** Vocabulary: interpreter: 解释器; presumably: 大概

**[5769.62s] English:** Yep.  
**Translation:** 

**[5769.90s] English:** So in the fullness of time, Mojo will solve for all the problems, and you'll be able to move Python packages over and run them in Mojo.  
**Translation:** 

**[5777.94s] English:** Without the CPython?  
**Translation:** 

**[5779.20s] English:** Without CPython.  
**Translation:** 

**[5780.34s] English:** Someday.  
**Translation:** 

**[5781.32s] English:** Yeah.  
**Translation:** 

**[5781.52s] English:** Not today, but someday.  
**Translation:** 

**[5783.26s] English:** And that'll be a beautiful day, because then you'll get a whole bunch of advantages, and you'll get massive speedups and things like this.  
**Translation:** 

**[5789.04s] English:** But you can do that one at a time, right?  
**Translation:** 

**[5790.38s] English:** You can move packages one at a time.  
**Translation:** 

**[5791.52s] English:** Exactly.  
**Translation:** 

**[5792.06s] English:** But we're not willing to wait for that.  
**Translation:** 

**[5794.74s] English:** Python is too important.  
**Translation:** 

**[5795.96s] English:** The ecosystem is too broad.  
**Translation:** 

**[5797.70s] English:** We want to both be able to build Mojo out.  
**Translation:** 

**[5800.58s] English:** We also want to do it the right way without intense time pressure.  
**Translation:** 

**[5804.62s] English:** We're obviously moving fast.  
**Translation:** 

**[5806.04s] English:** And so what we do is we say, okay, well, let's make it so you can import an arbitrary existing package.  
**Translation:** 

**[5814.24s] English:** Arbitrary.  
**Translation:** 

**[5815.60s] English:** Including, like, you write your own on your local disk or whatever.  
**Translation:** Vocabulary: arbitrary: 任意

**[5818.80s] English:** It's not.  
**Translation:** 

**[5819.04s] English:** It's not like a standard, like, an arbitrary package.  
**Translation:** 

**[5821.54s] English:** And import that using CPython.  
**Translation:** 

**[5824.20s] English:** Because CPython already runs all the packages, right?  
**Translation:** 

**[5826.92s] English:** And so what we do is we built an integration layer where we can actually use CPython.  
**Translation:** 

**[5832.00s] English:** Again, I'm practical.  
**Translation:** 

**[5834.20s] English:** And to actually just load and use all the existing packages as they are.  
**Translation:** 

**[5838.22s] English:** The downside of that is you don't get the benefits of Mojo for those packages, right?  
**Translation:** Vocabulary: downside: 不利之处

**[5842.06s] English:** And so they'll run as fast as they do in the traditional CPython way.  
**Translation:** 

**[5846.32s] English:** But what that does is that gives you an incremental migration.  
**Translation:** Vocabulary: incremental: 逐步的

**[5849.04s] English:** And so if you say, hey, cool, well, here's a, you know, the Python ecosystem is vast.  
**Translation:** 

**[5854.10s] English:** I want all of it to just work.  
**Translation:** 

**[5855.70s] English:** But there's certain things that are really important.  
**Translation:** 

**[5857.80s] English:** And so if I'm doing weather forecasting or something, well, I want to be able to load all the data.  
**Translation:** Vocabulary: forecasting: 天气预报

**[5863.88s] English:** I want to be able to work with it.  
**Translation:** 

**[5864.64s] English:** And then I have my own crazy algorithm inside of it.  
**Translation:** Vocabulary: algorithm: 计算方法

**[5867.32s] English:** Well, normally I'd write that in C++.  
**Translation:** 

**[5870.08s] English:** If I can write in Mojo and have one system that scales, well, that's way easier to work with.  
**Translation:** 

**[5874.64s] English:** Is it hard to do that, to have that layer that's running?  
**Translation:** 

**[5878.72s] English:** See Python.  
**Translation:** 

**[5880.00s] English:** Because is there some communication back and forth?  
**Translation:** 

**[5882.40s] English:** Yes, it's complicated.  
**Translation:** 

**[5884.00s] English:** I mean, this is what we do.  
**Translation:** 

**[5885.16s] English:** So, I mean, we make it look easy, but it is complicated.  
**Translation:** 

**[5888.82s] English:** But what we do is we use the CPython existing interpreter.  
**Translation:** 

**[5893.12s] English:** So it's running its own bytecodes, and that's how it provides full compatibility.  
**Translation:** Vocabulary: bytecodes: 字节码; compatibility: 兼容性; interpreter: 解释器

**[5896.88s] English:** And then it gives us CPython objects.  
**Translation:** 

**[5900.50s] English:** And we use those objects as is.  
**Translation:** 

**[5902.60s] English:** And so that way, we're fully compatible with all the CPython objects and all the, you know,  
**Translation:** 

**[5908.20s] English:** it's not just the Python part.  
**Translation:** Vocabulary: compatible: 兼容的

**[5910.10s] English:** It's also the C packages, the C libraries underneath them, because they're often hybrid.  
**Translation:** 

**[5914.22s] English:** And so we can fully run and we're fully compatible with all that.  
**Translation:** 

**[5917.22s] English:** And the way we do that is that we have to play by the rules, right?  
**Translation:** 

**[5920.22s] English:** And so we keep objects in that representation when they're coming from that world.  
**Translation:** 

**[5924.52s] English:** What's the representation that's being used?  
**Translation:** 

**[5926.56s] English:** In memory.  
**Translation:** 

**[5927.38s] English:** We'd have to know a lot about how the CPython interpreter works.  
**Translation:** 

**[5931.00s] English:** It has, for example, reference counting, but also different rules on how to pass pointers around and things like this.  
**Translation:** 

**[5937.52s] English:** Super low level.  
**Translation:** 

**[5938.20s] English:** It's super low level fiddly, and it's not like Python.  
**Translation:** Vocabulary: fiddly: 繁琐的

**[5940.22s] English:** It's like how the interpreter works, okay?  
**Translation:** 

**[5942.72s] English:** And so that gets all exposed out, and then you have to define wrappers around the low level C code, right?  
**Translation:** Vocabulary: wrappers: 接口封装

**[5948.94s] English:** And so what this means is you have to know not only C, which is a different rule from Python, obviously,  
**Translation:** 

**[5956.46s] English:** not only Python.  
**Translation:** 

**[5957.98s] English:** But the wrappers.  
**Translation:** 

**[5958.88s] English:** But the interpreter and the wrappers and the implementation details and the conventions,  
**Translation:** Vocabulary: conventions: 约定; implementation: 实现

**[5962.50s] English:** and it's just this really complicated mess.  
**Translation:** 

**[5964.72s] English:** And when you do that, now suddenly you have a debugger that debugs Python,  
**Translation:** 

**[5968.58s] English:** they can't step into C code.  
**Translation:** 

**[5971.00s] English:** So you have this two-world problem, right?  
**Translation:** 

**[5973.10s] English:** And so by pulling this all into Mojo, what you get is you get one world.  
**Translation:** 

**[5978.46s] English:** You get the ability to say, cool, I have untyped, very dynamic, beautiful, simple code.  
**Translation:** Vocabulary: untyped: 未类型化

**[5984.26s] English:** Okay, I care about performance for whatever reason, right?  
**Translation:** 

**[5986.64s] English:** There's lots of reasons you might care.  
**Translation:** 

**[5989.66s] English:** And so then you add types, you can parallelize things, you can vectorize things,  
**Translation:** 

**[5992.98s] English:** you can use these techniques, which are general techniques to solve a problem.  
**Translation:** Vocabulary: vectorize: 向量化

**[5997.02s] English:** And then you can do that.  
**Translation:** 

**[5998.16s] English:** You can do that by staying in the system.  
**Translation:** 

**[6000.00s] English:** And if you have that one Python package  
**Translation:** 

**[6003.22s] English:** that's really important to you,  
**Translation:** 

**[6004.12s] English:** you can move it to Mojo.  
**Translation:** 

**[6005.18s] English:** You get massive performance benefits on that  
**Translation:** 

**[6007.12s] English:** and other advantages.  
**Translation:** 

**[6009.38s] English:** You know, if you like stack types,  
**Translation:** 

**[6010.56s] English:** it's nice if they're enforced.  
**Translation:** 

**[6012.34s] English:** Some people like that, right, rather than being hints.  
**Translation:** Vocabulary: enforced: 强制执行

**[6014.66s] English:** So there's other advantages too.  
**Translation:** 

**[6016.56s] English:** And then you can do that incrementally as you go.  
**Translation:** Vocabulary: incrementally: 逐步地

**[6022.12s] English:** So one different perspective on this  
**Translation:** 

**[6024.84s] English:** would be why Mojo instead of making CPython faster,  
**Translation:** 

**[6030.98s] English:** redesigning CPython?  
**Translation:** 

**[6032.48s] English:** Yeah.  
**Translation:** 

**[6033.10s] English:** Well, I mean, you could argue Mojo is redesigning CPython.  
**Translation:** 

**[6036.08s] English:** But why not make CPython faster and better  
**Translation:** 

**[6039.68s] English:** and other things like that?  
**Translation:** 

**[6040.98s] English:** There's lots of people working on that.  
**Translation:** 

**[6042.94s] English:** So actually, there's a team at Microsoft  
**Translation:** 

**[6044.36s] English:** that is really improving.  
**Translation:** 

**[6046.78s] English:** I think CPython 3.11 came out in October,  
**Translation:** 

**[6050.56s] English:** something like that.  
**Translation:** 

**[6051.26s] English:** And it was 15% faster, 20% faster.  
**Translation:** 

**[6054.84s] English:** Across the board, which is pretty huge  
**Translation:** 

**[6057.06s] English:** given how mature Python is and things like this.  
**Translation:** 

**[6060.48s] English:** And so that's awesome.  
**Translation:** 

**[6062.64s] English:** I love it.  
**Translation:** 

**[6064.16s] English:** It doesn't run on GPU.  
**Translation:** 

**[6066.20s] English:** It doesn't do AI stuff.  
**Translation:** 

**[6068.06s] English:** It doesn't do vectors.  
**Translation:** 

**[6068.94s] English:** It doesn't do things.  
**Translation:** 

**[6071.36s] English:** 20% is good.  
**Translation:** 

**[6072.52s] English:** 35,000 times is better.  
**Translation:** 

**[6074.92s] English:** So they're definitely...  
**Translation:** 

**[6077.98s] English:** I'm a huge fan of that work, by the way,  
**Translation:** 

**[6079.46s] English:** and it composes well with what we're doing.  
**Translation:** Vocabulary: composes: 搭配得当

**[6081.16s] English:** And so it's not like we're fighting or anything like that.  
**Translation:** 

**[6083.92s] English:** It's actually just generalizing.  
**Translation:** Vocabulary: generalizing: 泛化

**[6085.00s] English:** It's goodness for the world.  
**Translation:** 

**[6086.06s] English:** But it's just a different path, right?  
**Translation:** 

**[6087.84s] English:** And again, we're not working forwards  
**Translation:** 

**[6089.88s] English:** from making Python a little bit better.  
**Translation:** 

**[6091.92s] English:** We're working backwards from what is the limit of physics.  
**Translation:** 

**[6095.16s] English:** What's the process of porting Python code to Mojo?  
**Translation:** Vocabulary: backwards: 逆向

**[6098.88s] English:** Is there...  
**Translation:** 

**[6100.16s] English:** What's involved in that process?  
**Translation:** 

**[6103.42s] English:** Is there tooling for that?  
**Translation:** 

**[6104.88s] English:** Not yet.  
**Translation:** 

**[6105.48s] English:** So we're missing some basic features right now.  
**Translation:** 

**[6108.28s] English:** And so we're continuing to drop out new features  
**Translation:** 

**[6110.36s] English:** on a weekly basis.  
**Translation:** 

**[6111.40s] English:** But at the fullness of time,  
**Translation:** 

**[6114.84s] English:** give us a year and a half, maybe two years.  
**Translation:** 

**[6117.96s] English:** Is it an automatable process?  
**Translation:** Vocabulary: automatable: 可自动化

**[6120.00s] English:** When we're ready, it will be very automatable.  
**Translation:** 

**[6122.86s] English:** Yes.  
**Translation:** 

**[6123.48s] English:** Is it possible to automate, in the general case, the Python to Moja conversion?  
**Translation:** 

**[6130.52s] English:** Yeah.  
**Translation:** Vocabulary: automate: 自动化

**[6130.86s] English:** You're saying it's possible.  
**Translation:** 

**[6131.98s] English:** Well, so, and this is why, I mean, among other reasons why we use tabs.  
**Translation:** 

**[6136.58s] English:** Yes.  
**Translation:** 

**[6137.24s] English:** Right?  
**Translation:** 

**[6137.60s] English:** So, first of all, by being a superset, it's like C versus C++.  
**Translation:** 

**[6142.70s] English:** Can you move C code to C++?  
**Translation:** 

**[6145.50s] English:** Yes.  
**Translation:** 

**[6145.96s] English:** Yeah.  
**Translation:** 

**[6146.64s] English:** Right?  
**Translation:** 

**[6146.90s] English:** And you can move C code to C++, and then you can adopt classes.  
**Translation:** 

**[6152.52s] English:** You can adopt templates.  
**Translation:** 

**[6153.58s] English:** You can adopt other references or whatever C++ features you want after you move C code to C++.  
**Translation:** Vocabulary: templates: 模板

**[6160.04s] English:** Like, you can't use templates in C.  
**Translation:** 

**[6162.50s] English:** Right?  
**Translation:** 

**[6162.96s] English:** And so, if you leave it at C, fine, you can't use the cool features, but it still works.  
**Translation:** 

**[6166.48s] English:** Right?  
**Translation:** 

**[6166.70s] English:** And C and C++ code work together.  
**Translation:** 

**[6168.94s] English:** And so, that's the analogy.  
**Translation:** 

**[6170.42s] English:** Right?  
**Translation:** 

**[6170.90s] English:** Now, here, right, there's not a...  
**Translation:** 

**[6176.90s] English:** Python is bad, and then Mojo is good.  
**Translation:** 

**[6179.84s] English:** Right?  
**Translation:** 

**[6180.26s] English:** Mojo just gives you superpowers.  
**Translation:** 

**[6181.96s] English:** Right?  
**Translation:** Vocabulary: superpowers: 超能力

**[6182.24s] English:** And so, if you want to stay with Python, that's cool.  
**Translation:** 

**[6185.10s] English:** But the tooling should be actually very beautiful and simple because we're doing the hard work of defining a superset.  
**Translation:** 

**[6192.70s] English:** Right.  
**Translation:** 

**[6192.86s] English:** So, you're...  
**Translation:** 

**[6193.54s] English:** Right.  
**Translation:** 

**[6193.88s] English:** So, there's several things to say there, but also the conversion tooling should probably give you hints as to, like, how you can improve the code.  
**Translation:** 

**[6200.64s] English:** And then you...  
**Translation:** 

**[6201.14s] English:** Yeah, exactly.  
**Translation:** 

**[6201.68s] English:** Once you're in the new world, then you can build all kinds of cool tools to say, like, hey, should you adopt this feature?  
**Translation:** 

**[6206.22s] English:** Or, like...  
**Translation:** 

**[6206.70s] English:** And we haven't built those tools yet, but I fully expect those tools will exist.  
**Translation:** 

**[6209.90s] English:** And then you can, like, you know, quote, unquote, modernize your code or however you want to look at it.  
**Translation:** Vocabulary: modernize: 现代化; unquote: 引用结束

**[6213.86s] English:** Right?  
**Translation:** 

**[6214.34s] English:** So, I mean, one of the things that I think is really interesting about Mojo is that there have been a lot of projects to improve Python over the years.  
**Translation:** 

**[6222.66s] English:** Everything from, you know, getting Python to run on the Java virtual machine, PyPy, which is a JIT compiler.  
**Translation:** 

**[6229.32s] English:** There's tons of these projects out there that have been working on improving Python in various ways.  
**Translation:** 

**[6234.30s] English:** They fall into one of two camps.  
**Translation:** 

**[6235.68s] English:** So, PyPy is a great example of a camp that is trying to be compatible.  
**Translation:** Vocabulary: compatible: 兼容的

**[6240.00s] English:** with python even there not really it doesn't work with all the c packages and stuff like that  
**Translation:** 

**[6245.10s] English:** but um but they're trying to be compatible with python there's also another category of these  
**Translation:** 

**[6249.84s] English:** things where they're saying well python is too complicated and you know i'm gonna cheat on the  
**Translation:** 

**[6255.54s] English:** edges and it you know like integers in python can be an arbitrary size integer like if you care about  
**Translation:** Vocabulary: arbitrary: 任意的; integer: 整数; integers: 整数

**[6261.84s] English:** it fitting in a going fast in a register in a computer that's really annoying right and so you  
**Translation:** 

**[6267.48s] English:** can you can choose to pass on that right you can say well people don't really use big integers that  
**Translation:** 

**[6272.62s] English:** often therefore i'm going to just not do it and it'll be fine not not a python superset or you  
**Translation:** 

**[6279.46s] English:** can do the hard thing and say okay this is python you can't be a superset of python without being a  
**Translation:** 

**[6285.84s] English:** superset of python and that's a really hard technical problem but it's in my opinion worth  
**Translation:** 

**[6291.62s] English:** it right and it's worth it because it's not about any one package it's about this ecosystem it's  
**Translation:** 

**[6296.86s] English:** about  
**Translation:** 

**[6297.48s] English:** what python means for the world and it also means we don't want to repeat the python 2 to python 3  
**Translation:** 

**[6302.16s] English:** transition like we want we want people to be able to adopt this stuff quickly and so by doing that  
**Translation:** 

**[6307.62s] English:** work we can help lift people yeah the challenge it's really interesting technical philosophical  
**Translation:** Vocabulary: philosophical: 哲学的

**[6312.76s] English:** challenge of really making a language a superset of another language that's breaking my brain a  
**Translation:** 

**[6320.96s] English:** little bit well it paints you into corners so um again i'm very happy with python i so joking all  
**Translation:** 

**[6326.86s] English:** joking aside  
**Translation:** 

**[6327.48s] English:** i think that the annotation thing is not the actual important part of the problem yes right but  
**Translation:** Vocabulary: annotation: 注释

**[6333.32s] English:** the the fact that python has amazing dynamic metaprogramming features and they translate to  
**Translation:** 

**[6337.80s] English:** beautiful static metaprogramming features i think is profound i think that's huge right and so python  
**Translation:** Vocabulary: metaprogramming: 元编程; profound: 深刻

**[6343.76s] English:** i've talked with guido about this it's it's like it was not designed to do what we're doing that  
**Translation:** 

**[6350.02s] English:** was not the reason they built it this way but because they really cared and they were very  
**Translation:** 

**[6353.26s] English:** thoughtful about how they designed the language it scales very elegantly in the space  
**Translation:** 

**[6357.48s] English:** but if you look at other languages for example  
**Translation:** Vocabulary: elegantly: 优雅地; thoughtful: 周到

**[6360.00s] English:** of C and C++, right?  
**Translation:** 

**[6362.66s] English:** If you're building a superset,  
**Translation:** 

**[6364.50s] English:** you get stuck with the design decisions of the subset, right?  
**Translation:** 

**[6369.50s] English:** And so, you know, C++ is way more complicated  
**Translation:** 

**[6373.54s] English:** because of C in the legacy than it would have been  
**Translation:** 

**[6376.40s] English:** if they would have theoretically designed  
**Translation:** Vocabulary: theoretically: 理论上

**[6378.14s] English:** a from scratch thing.  
**Translation:** 

**[6380.30s] English:** And there's lots of people right now  
**Translation:** 

**[6381.70s] English:** that are trying to make C++ better and re-syntax C++.  
**Translation:** 

**[6385.32s] English:** It's gonna be great, we'll just change all the syntax.  
**Translation:** Vocabulary: syntax: 语法规则

**[6388.00s] English:** But if you do that, now suddenly you have zero packages.  
**Translation:** 

**[6391.18s] English:** You don't have compatibility.  
**Translation:** Vocabulary: compatibility: 兼容性

**[6392.18s] English:** So what are the, if you could just linger on that,  
**Translation:** 

**[6395.98s] English:** what are the biggest challenges  
**Translation:** 

**[6398.28s] English:** of keeping that superset status?  
**Translation:** 

**[6400.84s] English:** What are the things you're struggling with?  
**Translation:** 

**[6402.48s] English:** Is it all boiled down to having a big integer?  
**Translation:** 

**[6405.72s] English:** No, I mean, it's-  
**Translation:** Vocabulary: integer: 整数

**[6406.72s] English:** What are the other things like?  
**Translation:** 

**[6408.02s] English:** Usually it's the long tail weird things.  
**Translation:** 

**[6410.94s] English:** So let me give you a war story.  
**Translation:** 

**[6412.96s] English:** So war story in the space is you go way back in time  
**Translation:** 

**[6418.00s] English:** and you have this project you're working on  
**Translation:** 

**[6421.04s] English:** and it's called Clang.  
**Translation:** Vocabulary: clang: 编译器

**[6422.50s] English:** Clang, what it is is a C, C++ parser, right?  
**Translation:** 

**[6426.02s] English:** And when I started working on Clang,  
**Translation:** Vocabulary: parser: 解析器

**[6428.86s] English:** it must have been like 2006 or something,  
**Translation:** 

**[6430.98s] English:** it was when I, 2007, 2006,  
**Translation:** 

**[6433.20s] English:** when I first started working on it, right?  
**Translation:** 

**[6435.52s] English:** It's funny how time flies.  
**Translation:** 

**[6437.00s] English:** Yeah.  
**Translation:** 

**[6437.84s] English:** Yeah.  
**Translation:** 

**[6438.68s] English:** I started that project, and I'm like,  
**Translation:** 

**[6440.62s] English:** okay, well, I wanna build a C parser,  
**Translation:** Vocabulary: wanna: 想要

**[6443.98s] English:** C++ parser for LLVM.  
**Translation:** 

**[6446.24s] English:** It's gonna be, the world, GCC, is UDL,  
**Translation:** 

**[6446.26s] English:** it's gonna be the world, GCC, is UDL,  
**Translation:** 

**[6446.36s] English:** it's gonna be the world, GCC, is UDL,  
**Translation:** 

**[6447.46s] English:** it's gonna be the world, GCC, is UDL,  
**Translation:** 

**[6447.50s] English:** it's gonna be the world, GCC, is UDL, is yucky.  
**Translation:** Vocabulary: yucky: 难吃

**[6449.16s] English:** This is me in earlier times.  
**Translation:** 

**[6451.62s] English:** It's yucky, it's unprincipled,  
**Translation:** Vocabulary: unprincipled: 道德败坏

**[6453.00s] English:** it has all these weird features,  
**Translation:** 

**[6454.14s] English:** like all these bugs, like it's yucky,  
**Translation:** 

**[6457.42s] English:** so I'm gonna build a standard compliant C and C++ parser.  
**Translation:** 

**[6461.56s] English:** It's gonna be beautiful, it'll be amazing,  
**Translation:** Vocabulary: compliant: 符合标准

**[6463.78s] English:** well engineered, all the cool things  
**Translation:** 

**[6465.04s] English:** an engineer wants to do.  
**Translation:** 

**[6466.74s] English:** And so I started implementing and building it out  
**Translation:** 

**[6468.18s] English:** and building it out and building it out,  
**Translation:** 

**[6469.36s] English:** and then I got to include standardio.h.  
**Translation:** 

**[6474.02s] English:** And all of the headers in the world use all the GCC stuff.  
**Translation:** Vocabulary: standardio: 标准输入输出

**[6477.50s] English:** Mm-hmm.  
**Translation:** 

**[6478.84s] English:** Okay, this ends.  
**Translation:** 

**[6480.00s] English:** So again, come back away from theory back to reality, right?  
**Translation:** 

**[6485.64s] English:** I was at a fork in the road.  
**Translation:** 

**[6488.12s] English:** I could have built an amazingly beautiful academic thing  
**Translation:** 

**[6491.06s] English:** that nobody would ever use.  
**Translation:** 

**[6493.38s] English:** Or I could say, well, it's yucky in various ways.  
**Translation:** 

**[6498.04s] English:** All these design mistakes, accents of history, the legacy.  
**Translation:** 

**[6501.64s] English:** At that point, GCC was like over 20 years old,  
**Translation:** 

**[6504.86s] English:** which, by the way, now LLVM's over 20 years old, right?  
**Translation:** 

**[6507.80s] English:** So it's funny how time catches up to you, right?  
**Translation:** 

**[6510.36s] English:** And so you say, okay, well, what is easier, right?  
**Translation:** 

**[6515.50s] English:** I mean, as an engineer, it's actually much easier for me  
**Translation:** 

**[6518.42s] English:** to go implement long-tail compatibility weird features,  
**Translation:** Vocabulary: compatibility: 兼容性

**[6521.52s] English:** even if they're distasteful, and just do the hard work  
**Translation:** 

**[6524.66s] English:** and figure it out, reverse engineer it, understand what it is,  
**Translation:** Vocabulary: distasteful: 令人不悦

**[6528.08s] English:** write a bunch of test cases, try to understand the behavior.  
**Translation:** 

**[6531.02s] English:** It's way easier to do all that work as an engineer  
**Translation:** 

**[6533.36s] English:** than it is to go talk to all C programmers and argue with them  
**Translation:** 

**[6536.70s] English:** and try to get them to rewrite.  
**Translation:** Vocabulary: programmers: 程序员

**[6537.80s] English:** That's their code.  
**Translation:** 

**[6538.74s] English:** Yeah.  
**Translation:** 

**[6539.82s] English:** Right.  
**Translation:** 

**[6540.70s] English:** Because that breaks a lot more things.  
**Translation:** 

**[6542.90s] English:** Yeah.  
**Translation:** 

**[6543.48s] English:** And you have realities.  
**Translation:** 

**[6545.10s] English:** Like, nobody actually even understands how the code works  
**Translation:** 

**[6547.60s] English:** because it was written by the person who quit 10 years ago.  
**Translation:** 

**[6551.28s] English:** Right?  
**Translation:** 

**[6551.82s] English:** And so this software is kind of frustrating that way,  
**Translation:** Vocabulary: frustrating: 令人沮丧的

**[6556.46s] English:** but that's how the world works.  
**Translation:** 

**[6559.08s] English:** Yeah, unfortunately, it can never be this perfect, beautiful thing.  
**Translation:** 

**[6563.10s] English:** Well, there are occasions in which you get to build,  
**Translation:** 

**[6566.02s] English:** like, you know, you invent a new.  
**Translation:** 

**[6567.80s] English:** Data structure or something like that.  
**Translation:** 

**[6569.40s] English:** Or there's this beautiful algorithm that just, like, makes you super happy.  
**Translation:** Vocabulary: algorithm: 算法

**[6572.18s] English:** And I love that moment.  
**Translation:** 

**[6574.08s] English:** But when you're working with people,  
**Translation:** 

**[6575.98s] English:** and you're working with code and dusty deck code bases  
**Translation:** 

**[6578.60s] English:** and things like this, right,  
**Translation:** 

**[6580.18s] English:** it's not about what's theoretically beautiful.  
**Translation:** 

**[6582.80s] English:** It's about what's practical, what's real, what people actually use.  
**Translation:** Vocabulary: theoretically: 理论上

**[6585.78s] English:** And I don't meet a lot of people that say,  
**Translation:** 

**[6588.56s] English:** I want to rewrite all my code just for the sake of it.  
**Translation:** 

**[6592.32s] English:** By the way, there could be interesting possibilities,  
**Translation:** 

**[6594.26s] English:** and we'll probably talk about it, where AI can help rewrite some code.  
**Translation:** 

**[6597.34s] English:** Yeah.  
**Translation:** 

**[6597.62s] English:** It might be farther out future.  
**Translation:** 

**[6600.00s] English:** but it's a really interesting one how that could create more be a a tool in the battle against this  
**Translation:** 

**[6607.50s] English:** monster of complexity that you mentioned yeah you mentioned guido the the benevolent dictator for  
**Translation:** Vocabulary: benevolent: 仁慈的; complexity: 复杂性; dictator: 独裁者

**[6615.72s] English:** life of python what does he think about mojo have you talked to him much about it uh i have talked  
**Translation:** 

**[6621.74s] English:** with him about it he found it very interesting um we actually talked with guido before it launched  
**Translation:** Vocabulary: guido: 吉多·范·罗苏姆

**[6625.92s] English:** and so he was aware of it before it went public um i have a ton of respect for guido for a bunch  
**Translation:** 

**[6630.62s] English:** of different reasons you talk about walrus operator and like guido is pretty amazing in  
**Translation:** Vocabulary: walrus: 海象

**[6636.52s] English:** terms of steering such a huge and diverse community and and and like driving it forward and  
**Translation:** 

**[6644.46s] English:** i think python is what it is thanks to him right and so to me it was really important starting to  
**Translation:** 

**[6651.30s] English:** work on mojo to get his feedback and get his input and get his eyes on this right  
**Translation:** 

**[6655.92s] English:** now um a lot of what guido was is was and is i think concerned about is have we not fragment  
**Translation:** 

**[6662.58s] English:** the community yeah we don't want a python 2 to python 3 thing like that was that was really  
**Translation:** 

**[6667.30s] English:** painful for everybody involved and so we spent quite a bit of time talking about that and some  
**Translation:** 

**[6671.38s] English:** of the tricks i learned from swift for example so in the migration from swift we managed to like  
**Translation:** 

**[6676.68s] English:** not just convert objective c into a slightly prettier objective c which we did we then  
**Translation:** 

**[6682.98s] English:** converted not entirely but almost  
**Translation:** 

**[6685.92s] English:** an entire community to a completely different language right and so there's a bunch of tricks  
**Translation:** 

**[6691.42s] English:** that you learn along the way that are directly relevant to what we do and so this is where  
**Translation:** 

**[6695.62s] English:** for example the you leverage c python while bringing up the new thing like that that approach  
**Translation:** Vocabulary: leverage: 利用

**[6701.96s] English:** is i think proven and and comes from experience and so guido was very interested in like okay  
**Translation:** 

**[6707.62s] English:** cool like i think the python is really his legacy it's his baby i have tons of respect for that  
**Translation:** 

**[6712.98s] English:** incidentally i see mojo as a member of the python family  
**Translation:** 

**[6715.92s] English:** we're not trying to take python away from guido and from the python community um  
**Translation:** 

**[6720.00s] English:** And so to me, it's really important that we're a good member of that community.  
**Translation:** 

**[6725.24s] English:** And so I think that, again, you would have to ask Guido this, but I think that he was very interested in this notion of like, cool, Python gets beaten up for being slow.  
**Translation:** 

**[6735.56s] English:** Maybe there's a path out of that.  
**Translation:** 

**[6738.38s] English:** Right. And that, you know, the future is Python.  
**Translation:** 

**[6742.96s] English:** Right. I mean, look, look at the far outside.  
**Translation:** 

**[6745.72s] English:** Case on this. Right. And I'm not saying this is Guido's perspective, but, you know, there's this path of saying like, OK, well, suddenly Python can suddenly go all the places it's never been able to go before.  
**Translation:** 

**[6758.20s] English:** Right. And that means that Python can go even further and can have even more impact on the world.  
**Translation:** 

**[6762.22s] English:** So in some sense, Mojo could be seen as Python 4.0.  
**Translation:** 

**[6767.92s] English:** I would not say that. I think that would drive a lot of people really crazy.  
**Translation:** 

**[6771.40s] English:** Because of the PTSD of the 3.0, 2.0.  
**Translation:** 

**[6774.10s] English:** I'm willing to annoy people about Emacs.  
**Translation:** 

**[6775.72s] English:** Emacs versus Vim.  
**Translation:** 

**[6776.44s] English:** But not that one.  
**Translation:** 

**[6776.98s] English:** Emacs versus Spaces.  
**Translation:** Vocabulary: emacs: 编辑器

**[6777.74s] English:** But not that one.  
**Translation:** 

**[6778.52s] English:** I don't know. That might be a little bit far even for me.  
**Translation:** 

**[6780.46s] English:** Like, my skin may not be that thick.  
**Translation:** 

**[6782.12s] English:** But the point is the step to being a superset and allowing all of these capabilities, I think, is the evolution of a language.  
**Translation:** 

**[6790.30s] English:** It feels like an evolution of a language.  
**Translation:** 

**[6792.82s] English:** So he's interested by the ideas that you're playing with, but also concerned about the fragmentation.  
**Translation:** Vocabulary: fragmentation: 碎片化

**[6798.46s] English:** So how, what are the ideas you've learned?  
**Translation:** 

**[6800.90s] English:** What are you thinking about?  
**Translation:** 

**[6801.86s] English:** How do we avoid fragmenting the community?  
**Translation:** 

**[6804.08s] English:** Where the...  
**Translation:** Vocabulary: fragmenting: 分裂

**[6805.72s] English:** The Pythonistas and the...  
**Translation:** 

**[6809.34s] English:** I don't know what to call the Mojo people.  
**Translation:** 

**[6812.50s] English:** Magicians.  
**Translation:** 

**[6813.16s] English:** The magicians. I like it.  
**Translation:** Vocabulary: magicians: 魔术师

**[6814.68s] English:** There you go.  
**Translation:** 

**[6815.32s] English:** Can coexist happily and share code.  
**Translation:** Vocabulary: coexist: 共存

**[6818.34s] English:** And basically just have these big code bases that are using CPython and more and more moving towards Mojo.  
**Translation:** 

**[6826.26s] English:** Well, so again, these are lessons I learned from Swift.  
**Translation:** 

**[6828.28s] English:** And here we face very similar problems, right?  
**Translation:** 

**[6831.14s] English:** In Swift, you have Objective-C, super dynamic.  
**Translation:** 

**[6835.72s] English:** They're very different syntax, right?  
**Translation:** 

**[6839.40s] English:** But...  
**Translation:** Vocabulary: syntax: 句法

**[6840.00s] English:** You're talking to people who have large-scale codebases.  
**Translation:** 

**[6843.28s] English:** I mean, Apple's got the biggest, largest-scale codebase of Objective-C code, right?  
**Translation:** Vocabulary: codebase: 代码库; codebases: 代码库

**[6847.68s] English:** And so, you know, none of the companies, none of the iOS developers, none of the other developers want to rewrite everything all at once.  
**Translation:** 

**[6853.74s] English:** And so you want to be able to adopt things piece at a time.  
**Translation:** 

**[6856.34s] English:** And so a thing that I found that worked very well in the Swift community was saying, okay, cool.  
**Translation:** 

**[6860.94s] English:** And this is when Swift was very young.  
**Translation:** 

**[6863.28s] English:** And she'd say, okay, you have a million line of code Objective-C app.  
**Translation:** 

**[6867.86s] English:** Don't rewrite it all.  
**Translation:** 

**[6868.88s] English:** But when you implement a new feature, go implement that new class using Swift, right?  
**Translation:** 

**[6875.42s] English:** And so now this, it turns out, is a very wonderful thing for an app developer, but it's a huge challenge for the compiler team and the systems people that are implementing this, right?  
**Translation:** Vocabulary: implementing: 实现

**[6885.58s] English:** And this comes back to what is this tradeoff between doing the hard thing that enables scale versus doing the theoretically pure and ideal thing, right?  
**Translation:** 

**[6893.98s] English:** And so Swift adopted and built a lot of different machinery to deeply integrate.  
**Translation:** Vocabulary: integrate: 整合; machinery: 机械; theoretically: 理论上; tradeoff: 权衡

**[6898.88s] English:** With the Objective-C runtime.  
**Translation:** 

**[6900.12s] English:** And we're doing the same thing with Python, right?  
**Translation:** Vocabulary: runtime: 运行时

**[6902.48s] English:** Now, what happened in the case of Swift is that Swift as a language got more and more and more mature over time, right?  
**Translation:** 

**[6909.78s] English:** And incidentally, Mojo is a much simpler language than Swift in many ways.  
**Translation:** 

**[6913.40s] English:** And so I think that Mojo will develop way faster than Swift for a variety of reasons.  
**Translation:** 

**[6917.62s] English:** But as the language gets more mature, in parallel with that, you have new people starting new projects, right?  
**Translation:** 

**[6923.56s] English:** And so when the language is mature and somebody's starting a new project, that's when they say, okay, cool.  
**Translation:** 

**[6927.80s] English:** I'm not dealing with...  
**Translation:** 

**[6928.88s] English:** A million lines of code.  
**Translation:** 

**[6929.92s] English:** I'll just start and use the new thing for my whole stack.  
**Translation:** 

**[6932.98s] English:** Now, the problem is, again, you come back to where communities and where people that work together, you build a new subsystem or a new feature, a new thing in Swift or you build a new thing in Mojo.  
**Translation:** 

**[6945.06s] English:** Then you want to end up being used on the other side, right?  
**Translation:** 

**[6949.28s] English:** And so then you need to work on integration back the other way.  
**Translation:** 

**[6952.54s] English:** And so it's not just Mojo talking to Python.  
**Translation:** 

**[6955.40s] English:** It's also Python talking to Mojo, right?  
**Translation:** 

**[6957.96s] English:** And so what I would love...  
**Translation:** 

**[6958.88s] English:** I'd love to see...  
**Translation:** 

**[6959.64s] English:** I don't know.  
**Translation:** 

**[6960.00s] English:** see this next month right but what i want to see over the course of time is i would love to see  
**Translation:** 

**[6964.56s] English:** people that are building these packages like you know numpy or uh you know tensorflow or what you  
**Translation:** 

**[6970.96s] English:** know these packages that are half python half c plus plus and if you say okay cool i want to get  
**Translation:** 

**[6977.68s] English:** out of this python c plus plus world into a unified world and so i can move to mojo but i  
**Translation:** 

**[6984.40s] English:** can't give up all my python clients because they're like these libraries get used by everybody  
**Translation:** 

**[6990.00s] English:** and they're not all going to switch all you know all once and maybe never right well so the way we  
**Translation:** 

**[6995.76s] English:** should do that is we should vend python interfaces to the mojo types and that's what we did in swift  
**Translation:** 

**[7001.84s] English:** and worked great i mean it was a huge implementation challenge for the compiler people  
**Translation:** Vocabulary: implementation: 实现; interfaces: 接口

**[7005.84s] English:** right but um there's only a dozen of those compiler people and there are millions of users  
**Translation:** 

**[7010.80s] English:** and so it's a very expensive capital intensive  
**Translation:** 

**[7014.40s] English:** like skill set intensive problem but once you solve that problem it really helps adoption it  
**Translation:** 

**[7020.28s] English:** really helps the community progressively adopt technologies and so i think that this approach  
**Translation:** Vocabulary: progressively: 逐步地

**[7024.50s] English:** will work quite well with with the python and the mojo world so for a package ported to mojo  
**Translation:** 

**[7029.48s] English:** and then create a python interface yep so how do just to linger on these packages numpy  
**Translation:** Vocabulary: interface: 接口

**[7037.64s] English:** py torch tensorflow yeah how do they play nicely together so is uh mojo supposed to be let's  
**Translation:** 

**[7044.38s] English:** talk about the machine learning ones is mojo kind of vision to replace py torch intensive flow  
**Translation:** 

**[7051.32s] English:** uh to incorporate it what's what's the relationship in this all right so um dance so take a step back  
**Translation:** 

**[7057.20s] English:** so i wear many hats so you're you're angling it on the mojo side yes mojo is a programming language  
**Translation:** Vocabulary: incorporate: 吸收

**[7064.76s] English:** and so it can help solve the c c plus plus python feud that's happening the fire emoji got me i'm  
**Translation:** 

**[7071.52s] English:** sorry we should be talking about modular yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes  
**Translation:** Vocabulary: modular: 模块化的

**[7074.38s] English:** yes okay so the fire emoji is amazing i love it uh it's it's a big deal the  
**Translation:** 

**[7080.00s] English:** other side of this is the fire emoji is in service of solving some big ai problems right and so the  
**Translation:** 

**[7085.66s] English:** big ai problems are again this fragmentation this hardware nightmare this uh this explosion of new  
**Translation:** 

**[7091.94s] English:** potential but that's not getting felt by the industry right and so when you look at how does  
**Translation:** Vocabulary: fragmentation: 碎片化

**[7097.62s] English:** the modular engine help tensorflow and pytorch right it's not replacing them right in fact when  
**Translation:** 

**[7103.28s] English:** i talk to people again they don't like to rewrite all their code you have people that are using a  
**Translation:** 

**[7107.72s] English:** bunch of pytorch a bunch of tensorflow they have models that they've been building over the course  
**Translation:** 

**[7112.02s] English:** of many years right and when i talk to them there's a few exceptions but generally they don't  
**Translation:** Vocabulary: exceptions: 例外

**[7117.00s] English:** want to rewrite all their code right and so what we're doing is we're saying okay well you don't  
**Translation:** 

**[7121.36s] English:** have to rewrite all your code what happens is the modular engine goes in there and goes underneath  
**Translation:** 

**[7125.74s] English:** tensorflow and pytorch it's fully compatible and just provides better performance better predictability  
**Translation:** 

**[7131.12s] English:** better tooling it's a better experience that helps lift tensorflow and pytorch and make them even  
**Translation:** Vocabulary: compatible: 兼容

**[7136.10s] English:** better i love python  
**Translation:** 

**[7137.72s] English:** i love tensorflow i love pytorch right this is about making the world better because we need ai  
**Translation:** 

**[7143.22s] English:** to go further but uh if i have a process that trains a model and i have a process that performs  
**Translation:** 

**[7148.56s] English:** inference on that model and i have the model itself uh what should i do with that in the long  
**Translation:** Vocabulary: inference: 推断

**[7154.60s] English:** arc of history uh in terms of if i use pytorch to train it should i rewrite stuff in mojo would  
**Translation:** 

**[7162.36s] English:** that if i care about performance oh so i mean again it depends so if you care about performance  
**Translation:** 

**[7167.72s] English:** then writing in mojo is going to be way better than writing in python but if you look at um if  
**Translation:** 

**[7172.60s] English:** you look at llm companies for example so you look at open ai rumored and you look at many of the  
**Translation:** 

**[7177.38s] English:** other folks that are working on many of these many of these llms and other like innovative  
**Translation:** 

**[7182.82s] English:** machine learning models on the one hand they're innovating in the data collection and the model  
**Translation:** Vocabulary: innovating: 创新

**[7187.36s] English:** billions of parameters and the model architecture and the rle hf and the the like all these all  
**Translation:** 

**[7194.18s] English:** the cool things that people are talking about but on the other hand there's still a lot of  
**Translation:** 

**[7197.72s] English:** a lot of time writing cuda girls  
**Translation:** 

**[7200.00s] English:** right and so you say wait a second how much faster could all this progress go if they were not having  
**Translation:** 

**[7206.26s] English:** to handwrite all these cuda kernels right and so there are a few technologies that are out there  
**Translation:** 

**[7210.34s] English:** and people have been working on this problem for a while and um and they're trying to solve  
**Translation:** Vocabulary: handwrite: 亲手书写; kernels: 内核

**[7214.72s] English:** subsets of the problem again kind of fragmenting the space and so what mojo provides for these  
**Translation:** 

**[7219.02s] English:** kinds of companies is the ability to say cool i can have a unifying theory right and again this  
**Translation:** Vocabulary: fragmenting: 分割; unifying: 统一

**[7224.10s] English:** the the better together the unifying theory the the two world problem or the three world problem  
**Translation:** 

**[7228.90s] English:** or the n world problem like this is the thing that is slowing people down and so as we help  
**Translation:** 

**[7233.10s] English:** solve this problem i think it'll be very helpful for making this whole cycle go faster so obviously  
**Translation:** 

**[7238.66s] English:** we've talked about uh the transition from objective c to swift if design this uh programming  
**Translation:** 

**[7244.86s] English:** language and you've also talked quite a bit about the use of swift for machine learning  
**Translation:** 

**[7249.12s] English:** context why have you decided to move away from uh maybe an intense focus on swift  
**Translation:** 

**[7258.90s] English:** for the machine learning context versus sort of designing a new programming language that happens  
**Translation:** 

**[7265.50s] English:** to be a superset this is an irrational set of life choices i make did you go to the desert  
**Translation:** Vocabulary: irrational: 不合逻辑的选择

**[7271.62s] English:** and did you meditate on it okay all right no it was bold it was bold and needed and i think uh  
**Translation:** 

**[7278.58s] English:** i mean it's just bold and sometimes to take those leaps is a difficult leap to take yeah well so  
**Translation:** Vocabulary: meditate: 静思

**[7283.46s] English:** okay i mean i think there's a couple of different things so um actually i left apple back in 2017  
**Translation:** 

**[7288.90s] English:** like january 2017 so it's been a number of years that i left apple and the reason i left apple was  
**Translation:** 

**[7295.46s] English:** to do ai okay so and again i won't comment on apple and ai but the uh uh at the time right i  
**Translation:** 

**[7305.28s] English:** wanted to get into and understand and understand the technology understand the applications the  
**Translation:** 

**[7309.62s] English:** workloads and so i was like okay i'm gonna go dive deep into applied and ai and then the technology  
**Translation:** 

**[7314.68s] English:** underneath it right um i found myself at google  
**Translation:** 

**[7318.90s] English:** and i was like  
**Translation:** 

**[7320.00s] English:** and tpus were yep waking up exactly and so i found myself at google and uh jeff dean who's  
**Translation:** 

**[7326.70s] English:** a rock star as you know right and the and in 2017 tense flow is like really taking off and doing  
**Translation:** 

**[7333.68s] English:** incredible things and i was attracted to google to help them with the tpus right and tpus are an  
**Translation:** 

**[7339.02s] English:** innovative hardware accelerator platform uh have now i mean i think proven massive scale and like  
**Translation:** 

**[7344.64s] English:** done incredible things right and so one of the things that this led into is a bunch of different  
**Translation:** 

**[7350.64s] English:** projects which i'll skip over right one of which was this swift for tense flow project right and so  
**Translation:** 

**[7355.76s] English:** that project was a research project and so the idea of that is say okay well let's look at  
**Translation:** 

**[7361.66s] English:** innovative new programming models where we can get a fast programming language we can get  
**Translation:** 

**[7366.48s] English:** automatic differentiation into language let's push the boundaries of these things in a research  
**Translation:** Vocabulary: differentiation: 自动求导

**[7371.36s] English:** setting right now that  
**Translation:** 

**[7374.64s] English:** project i think lasted two three years there's some really cool outcomes of that so one of one  
**Translation:** 

**[7379.16s] English:** of the things that's really interesting is um i published a talk at an lvm conference in 2018  
**Translation:** 

**[7385.70s] English:** again this seems like so long ago uh about graph program abstraction which is basically the thing  
**Translation:** Vocabulary: abstraction: 抽象

**[7391.34s] English:** that's in pytorch 2 and so pytorch 2 with all this dynamo real thing it's all about this graph  
**Translation:** 

**[7396.28s] English:** program abstraction thing from python bytecodes and so a lot of the research that was done um  
**Translation:** Vocabulary: bytecodes: 字节码; dynamo: 动态编译

**[7401.92s] English:** ended up pursuing and going out through the  
**Translation:** 

**[7404.64s] English:** history and influencing things and i think it's super exciting and awesome to see that  
**Translation:** 

**[7408.04s] English:** but the swift for test project itself did not work out super well and so there's a couple of  
**Translation:** 

**[7412.64s] English:** different problems with that one of which is that uh you may have noticed swift is not python  
**Translation:** 

**[7417.46s] English:** there's a few people that write python code yes and so it turns out that all of ml is pretty happy  
**Translation:** 

**[7425.72s] English:** with python it's actually a problem other programming languages have as well that they're  
**Translation:** 

**[7430.50s] English:** not python we'll probably maybe briefly talk about julia  
**Translation:** 

**[7434.64s] English:** it was a very interesting uh beautiful programming language but it's not python exactly well and so  
**Translation:** 

**[7440.00s] English:** Like, if you're saying, I'm going to solve a machine learning problem where all the programmers are Python programmers, and you say the first thing you have to do is switch to a different language, well, your new thing may be good or bad or whatever, but if it's a new thing, the adoption barrier is massive.  
**Translation:** 

**[7457.44s] English:** It's still possible.  
**Translation:** Vocabulary: programmers: 程序员

**[7458.52s] English:** It's still possible.  
**Translation:** 

**[7459.18s] English:** Yeah, absolutely.  
**Translation:** 

**[7459.62s] English:** The world changes and evolves, and there's definitely room for new and good ideas, but it just makes it so much harder.  
**Translation:** 

**[7465.12s] English:** And so, lesson learned, Swift is not Python, and people are not always in search of learning a new thing for the sake of learning a new thing.  
**Translation:** 

**[7473.48s] English:** And if you want to be compatible with all the world's code, turns out, meet the world where it is.  
**Translation:** 

**[7479.74s] English:** Second thing is that, you know, a lesson learned is that Swift, as a very fast and efficient language, kind of like Mojo, but a different take on it still, really worked well with eager mode.  
**Translation:** 

**[7494.42s] English:** And so.  
**Translation:** 

**[7495.12s] English:** So, eager mode is something that PyTorch does, and it proved out really well, and it enables really expressive and dynamic and easy-to-debug programming.  
**Translation:** Vocabulary: expressive: 富有表现力的

**[7505.32s] English:** TensorFlow at the time was not set up for that, let's say.  
**Translation:** 

**[7508.98s] English:** That was not.  
**Translation:** 

**[7509.46s] English:** The timing is also important in this world.  
**Translation:** 

**[7511.66s] English:** Yeah, yeah, and TensorFlow is a good thing, and it has many, many strengths, but you could say Swift for TensorFlow is a good idea, except for the Swift and except for the TensorFlow part.  
**Translation:** 

**[7524.42s] English:** Swift.  
**Translation:** 

**[7525.12s] English:** Because it's not Python and TensorFlow, because it's not eager.  
**Translation:** 

**[7527.50s] English:** It wasn't set up for eager mode at the time.  
**Translation:** 

**[7529.32s] English:** Yeah.  
**Translation:** 

**[7529.50s] English:** It was 1.0.  
**Translation:** 

**[7530.24s] English:** Exactly.  
**Translation:** 

**[7530.88s] English:** And so, one of the things about that is that, in the context of it being a research project, I'm very happy with the fact that we built a lot of really cool technology.  
**Translation:** 

**[7540.52s] English:** We learned a lot of things.  
**Translation:** 

**[7541.78s] English:** I think the ideas went on to have influence in other systems, like PyTorch.  
**Translation:** 

**[7544.66s] English:** A few people use that, I hear.  
**Translation:** 

**[7546.34s] English:** Right?  
**Translation:** 

**[7546.60s] English:** And so, I think that's super cool.  
**Translation:** 

**[7548.54s] English:** And for me, personally, I learned so much from it.  
**Translation:** 

**[7551.28s] English:** Right?  
**Translation:** 

**[7551.54s] English:** And I think a lot of the engineers that worked on it also learned a tremendous amount.  
**Translation:** 

**[7555.12s] English:** And so, you know, I think that that's just really exciting to see.  
**Translation:** 

**[7559.00s] English:** And, you know, I'm  
**Translation:** 

**[7560.00s] English:** sorry that the project didn't work out i wish it did of course right but um uh but you know it's  
**Translation:** 

**[7566.44s] English:** it's it's a research project and so you're there to learn from it well it's interesting to think  
**Translation:** 

**[7570.38s] English:** about uh the evolution of programming as we come up with these whole new set of algorithms in  
**Translation:** 

**[7579.68s] English:** machine learning in artificial intelligence and what's going to win out because it could be a new  
**Translation:** 

**[7584.62s] English:** programming language yeah it could be um i mean we i just mentioned julia i think there's a lot  
**Translation:** 

**[7591.98s] English:** of ideas behind julia that mojo shares um what what are your thoughts about julia in general  
**Translation:** 

**[7599.28s] English:** um so i would i will have to say that when we launched mojo the one of the biggest things i  
**Translation:** 

**[7605.96s] English:** didn't predict was the response from the julia community and so um i was not i mean i've okay  
**Translation:** 

**[7612.28s] English:** let me take a step back i've known the julia  
**Translation:** 

**[7614.62s] English:** folks for a really long time they were they're an adopter of llvm a long time ago they've been  
**Translation:** 

**[7619.64s] English:** pushing state of the art in a bunch of different ways julia is a really cool system um i had always  
**Translation:** 

**[7625.14s] English:** thought of julia as being mostly a scientific computing focused environment right and and i  
**Translation:** 

**[7630.74s] English:** thought that was its focus um i neglected to understand that one of their missions is to like  
**Translation:** Vocabulary: computing: 计算; neglected: 忽视

**[7636.72s] English:** help make python work end to end and so i think that was my my error for not understanding that  
**Translation:** 

**[7643.08s] English:** so i could have been maybe more  
**Translation:** 

**[7644.48s] English:** sensitive to that but um but there's major differences between what mojo is doing and  
**Translation:** 

**[7649.10s] English:** what julia is doing so as you say julia is not python right and so one of the things that a lot  
**Translation:** 

**[7655.18s] English:** of the julia people came out and said is like okay well if we put a ton of more energy and  
**Translation:** 

**[7660.28s] English:** ton more money or engineering or whatever into julia maybe uh that would be better than starting  
**Translation:** 

**[7666.50s] English:** mojo right well i mean maybe that's true but it still wouldn't make julian to python so if you've  
**Translation:** 

**[7672.96s] English:** worked backwards from the goal of let's build something for python programmers without requiring  
**Translation:** Vocabulary: backwards: 倒着; programmers: 编程者

**[7678.00s] English:** them to relearn  
**Translation:** 

**[7680.00s] English:** syntax then julia just isn't there right i mean that's a different thing right and so if you  
**Translation:** Vocabulary: syntax: 语法规则

**[7687.00s] English:** anchor on i love julia and i want julia to go further then you can you can look at it from a  
**Translation:** 

**[7691.68s] English:** different lens but the lens we were coming at was hey everybody is using python python isn't  
**Translation:** 

**[7696.98s] English:** syntax isn't broken let's take what's great about python make it even better and so it's just a  
**Translation:** 

**[7701.90s] English:** different starting point so i think julia is a great language the community is a lovely community  
**Translation:** 

**[7706.08s] English:** they're doing really cool stuff but it's just a different slightly different angle but it does  
**Translation:** 

**[7710.86s] English:** seem that python is quite sticky uh is there some uh philosophical almost thing you could say about  
**Translation:** Vocabulary: philosophical: 哲学的

**[7718.10s] English:** why python by many measures seems to be the most popular programming language in the world well i  
**Translation:** 

**[7723.32s] English:** can tell you things i love about it maybe that's one way to answer the question right so huge package  
**Translation:** 

**[7728.02s] English:** ecosystem super lightweight and easy to integrate it has very low startup time right so what startup  
**Translation:** 

**[7735.48s] English:** time you mean  
**Translation:** Vocabulary: integrate: 集成; lightweight: 轻量

**[7736.02s] English:** yeah so if you if you look at certain other languages that you say like go and it just  
**Translation:** 

**[7741.98s] English:** takes a like java for example it takes a long time to compile all the things and and then the the vm  
**Translation:** 

**[7747.52s] English:** starts up and the garbage clusters kicks in and then it revs its engines and then it can plow  
**Translation:** 

**[7751.26s] English:** through a lot of internet stuff or whatever right um python is like scripting like it's it just goes  
**Translation:** Vocabulary: clusters: 垃圾集群

**[7756.78s] English:** right um python has very little compile time like so you're not sitting there waiting python  
**Translation:** 

**[7761.38s] English:** integrates into notebooks in a very elegant way that makes exploration super interactive  
**Translation:** Vocabulary: integrates: 集成; interactive: 交互式

**[7766.02s] English:** and it's awesome right python is also um it's like almost the glue of computing because it has  
**Translation:** 

**[7773.10s] English:** such a simple object representation a lot of things plug into it that dynamic metaprogramming  
**Translation:** Vocabulary: computing: 计算机计算; metaprogramming: 元编程

**[7778.50s] English:** thing we were talking about also enables really expressive and beautiful apis right so there's  
**Translation:** 

**[7782.90s] English:** lots of reasons that you can look at technical things that python has done and say like okay  
**Translation:** Vocabulary: expressive: 富有表现力的

**[7788.28s] English:** wow this is actually a pretty amazing thing and any one of those you can neglect people i'll just  
**Translation:** 

**[7793.72s] English:** talk about indentation and it can be a pretty amazing thing and it can be a pretty amazing thing  
**Translation:** Vocabulary: indentation: 缩进

**[7796.02s] English:** ignore like the fundamental things but then you also look at the community side  
**Translation:** 

**[7800.00s] English:** So Python owns machine learning.  
**Translation:** 

**[7802.80s] English:** Machine learning is pretty big.  
**Translation:** 

**[7804.16s] English:** Yeah, and it's growing.  
**Translation:** 

**[7805.04s] English:** And it's growing, right?  
**Translation:** 

**[7805.88s] English:** And it's growing in importance, right?  
**Translation:** 

**[7807.28s] English:** And there's a reputation and prestige to machine learning to where, like, if you're a new programmer, you're thinking about, like, which programming language do I use?  
**Translation:** 

**[7816.42s] English:** Well, I should probably care about machine learning.  
**Translation:** Vocabulary: prestige: 声望; programmer: 程序员

**[7818.30s] English:** Therefore, let me try Python.  
**Translation:** 

**[7820.18s] English:** And it kind of builds and builds and builds.  
**Translation:** 

**[7821.44s] English:** And you even go back before that.  
**Translation:** 

**[7824.28s] English:** Like, my kids learn Python.  
**Translation:** 

**[7826.22s] English:** Right, not because I'm telling them to learn Python, but because.  
**Translation:** 

**[7829.76s] English:** Were they rebelling against you or what?  
**Translation:** Vocabulary: rebelling: 反抗

**[7831.74s] English:** Well, no, no, right.  
**Translation:** 

**[7832.38s] English:** Well, they also learn Scratch, right, and things like this, too.  
**Translation:** 

**[7834.78s] English:** But it's because Python is taught everywhere, right, because it's easy to learn, right, and because it's pervasive, right?  
**Translation:** 

**[7840.62s] English:** Back in my day, we learned Java and C++.  
**Translation:** Vocabulary: pervasive: 无处不在

**[7844.06s] English:** Yeah, well.  
**Translation:** 

**[7845.74s] English:** Uphill both directions.  
**Translation:** Vocabulary: uphill: 逆着坡走

**[7847.48s] English:** But, yes, I guess Python is the main language of teaching software engineering in schools now.  
**Translation:** 

**[7851.78s] English:** Yeah, well, and if you look at this, there's these growth cycles, right?  
**Translation:** 

**[7856.22s] English:** And if you look at what causes things to become popular and then gain in popularity, there's reinforcing feedback loops and things like this.  
**Translation:** 

**[7863.50s] English:** And I think Python has done, again, the whole community has done a really good job of building those growth loops and help propel the ecosystem.  
**Translation:** Vocabulary: propel: 推动; reinforcing: 强化

**[7870.08s] English:** And I think that, again, you look at what you can get done with just a few lines of code.  
**Translation:** 

**[7873.34s] English:** It's amazing.  
**Translation:** 

**[7874.20s] English:** So this kind of self-building loop is interesting to understand because when you look at Mojo, what it stands for, some of the features,  
**Translation:** 

**[7884.50s] English:** is it seems sort of clear that this is a good direction for programming languages to evolve in the machine learning community.  
**Translation:** 

**[7893.28s] English:** But it's still not obvious that it will because of this, whatever the engine of popularity, of virality.  
**Translation:** 

**[7900.94s] English:** Is there something you could speak to, like, how do you get people to switch?  
**Translation:** Vocabulary: virality: 传播性

**[7905.56s] English:** Yeah, well, I mean, I think that the viral growth loop is to switch people to Unicode.  
**Translation:** 

**[7910.74s] English:** Yes.  
**Translation:** Vocabulary: viral: 病毒式的

**[7911.16s] English:** I think the Unicode file extensions are what I'm betting on.  
**Translation:** 

**[7913.30s] English:** I think that's going to be the thing.  
**Translation:** Vocabulary: extensions: 文件扩展名

**[7914.76s] English:** Yeah.  
**Translation:** 

**[7915.82s] English:** Tell the kids that you could use the fire emoji and they'd be like, what?  
**Translation:** 

**[7919.16s] English:** Exactly.  
**Translation:** 

**[7920.00s] English:** uh well in all seriousness like i mean i think there's really i'll give you two opposite answers  
**Translation:** 

**[7926.64s] English:** one is i hope if it's useful if it solves problems and people care about those problems being solved  
**Translation:** 

**[7932.96s] English:** they'll adopt the tech right that's the that's kind of the simple answer and when you're looking  
**Translation:** 

**[7938.82s] English:** to get tech adopted the question is is it solving an important problem people need solved and is the  
**Translation:** 

**[7944.80s] English:** adoption cost low enough that they're willing to make the switch and cut over and do do the pain  
**Translation:** 

**[7951.68s] English:** up front so that they can actually do it right and so hopefully mojo will be that for a bunch of  
**Translation:** 

**[7956.94s] English:** people and you know people building these hybrid packages are suffering and it's really painful  
**Translation:** 

**[7962.04s] English:** and so i think that we have a good shot of helping people but the other side is like it's okay if  
**Translation:** 

**[7966.86s] English:** people don't use mojo like it's not my job to say like everybody should do this like i'm not saying  
**Translation:** 

**[7971.58s] English:** python is bad like i hope python see python like all these  
**Translation:** 

**[7974.64s] English:** implementations are going to be okay but i think it's okay if people don't use mojo  
**Translation:** Vocabulary: implementations: 实现版本

**[7974.78s] English:** because python ecosystem is not just see python it's also a bunch of different implementations  
**Translation:** 

**[7979.42s] English:** with different trade-offs and this ecosystem is really powerful and exciting as are other  
**Translation:** 

**[7984.62s] English:** programming languages it's not like typescript or something is going to go away right and so it's  
**Translation:** 

**[7989.58s] English:** not a there's not a winner-take-all thing and so i hope that mojo is exciting and useful to people  
**Translation:** 

**[7994.22s] English:** but if it's not that's also fine but i also wonder what the the use case for why you should try mojo  
**Translation:** 

**[8002.24s] English:** would be so practically speaking  
**Translation:** 

**[8004.62s] English:** it seems like uh so there's entertainment there's a dopamine hit of saying holy shit this is 10 times  
**Translation:** 

**[8013.38s] English:** faster uh this little piece of code is 10 times faster in mojo out of the box before you get to  
**Translation:** Vocabulary: dopamine: 多巴胺

**[8019.14s] English:** 35 000 exactly i mean just even that i mean that's the dopamine hit that uh every programmer sort of  
**Translation:** 

**[8027.02s] English:** dreams of is uh the optimization it's it's also the drug that can uh pull you in and have you  
**Translation:** Vocabulary: optimization: 代码优化; programmer: 程序员

**[8034.20s] English:** waste your time and money and you know you're not going to be able to do anything about it  
**Translation:** 

**[8034.46s] English:** waste way too much of your life optimizing and over optimizing right um  
**Translation:** 

**[8040.00s] English:** But so what do you see that would be like comedy?  
**Translation:** 

**[8043.32s] English:** It's very hard to predict, of course, but if you look 10 years from now and Mojo is super successful, what do you think would be the thing where people try it and then use it regularly and it kind of grows and grows and grows?  
**Translation:** 

**[8058.48s] English:** Well, so you talk about dopamine hit.  
**Translation:** 

**[8059.80s] English:** And so, again, humans are not one thing.  
**Translation:** 

**[8064.48s] English:** And some people love rewriting their code and learning new things and throwing themselves in the deep end and trying out a new thing.  
**Translation:** 

**[8070.18s] English:** In my experience, most people don't like they're too busy.  
**Translation:** Vocabulary: rewriting: 重写代码

**[8074.58s] English:** They have other things going on by number.  
**Translation:** 

**[8077.78s] English:** Most people don't like this.  
**Translation:** 

**[8079.46s] English:** I want to rewrite all my code.  
**Translation:** 

**[8083.36s] English:** But even those people, the too busy people, the people that don't actually care about the language, just care about getting stuff done.  
**Translation:** 

**[8090.44s] English:** Those people do like learning new things.  
**Translation:** 

**[8093.30s] English:** Right.  
**Translation:** 

**[8094.00s] English:** And so you talk about the dopamine rush of 10x faster.  
**Translation:** 

**[8096.50s] English:** Wow, that's cool.  
**Translation:** 

**[8097.12s] English:** I want to do that again.  
**Translation:** 

**[8098.32s] English:** Well, it's also like here's here's the thing.  
**Translation:** 

**[8100.02s] English:** I've heard about in a different domain and I don't have to rewrite all my code.  
**Translation:** 

**[8102.92s] English:** I can learn a new trick.  
**Translation:** 

**[8104.70s] English:** Right.  
**Translation:** 

**[8105.14s] English:** Well, that's called growth.  
**Translation:** 

**[8107.12s] English:** And so and so one thing that I think is cool about Mojo and again, those will take a little bit of time for, for example, the blog posts and the books and like all that kind of stuff develop and the language needs to get further along.  
**Translation:** 

**[8118.92s] English:** But what we're doing, you talk about types like you can say, look, you can start with the world you already know and you can progressively learn new things and adopt them where it makes sense.  
**Translation:** Vocabulary: progressively: 逐步地

**[8128.34s] English:** If you never do that.  
**Translation:** 

**[8130.00s] English:** That's cool.  
**Translation:** 

**[8130.80s] English:** You're not a bad person.  
**Translation:** 

**[8131.70s] English:** If you if you get really excited about it, want to go all the way in the deep end and rewrite everything and like, whatever, that's cool, right?  
**Translation:** 

**[8138.82s] English:** But I think the middle path is actually the more likely one where it's, you know, you come out with a new a new idea and you discover, wow, that makes my code way simpler, way more beautiful, way faster, way whatever.  
**Translation:** 

**[8150.32s] English:** And I think that's what people like now, if you fast forward and you said, like, 10 years out, right, I can give you a very different answer on that, which is.  
**Translation:** 

**[8158.70s] English:** Yeah.  
**Translation:** 

**[8158.94s] English:** Yeah.  
**Translation:** 

**[8159.16s] English:** Yeah.  
**Translation:** 

**[8159.40s] English:** Yeah.  
**Translation:** 

**[8159.64s] English:** Yeah.  
**Translation:** 

**[8159.70s] English:** Yeah.  
**Translation:** 

**[8159.82s] English:** Yeah.  
**Translation:** 

**[8159.96s] English:** Yeah.  
**Translation:** 

**[8160.00s] English:** I mean, if you go back and look at what computers looked like 20 years ago, every 18 months they got faster for free, right?  
**Translation:** 

**[8169.12s] English:** 2x faster every 18 months, it was like clockwork, it was free, right?  
**Translation:** Vocabulary: clockwork: 机械装置

**[8173.18s] English:** You go back 10 years ago, and we entered in this world where suddenly we had multi-core CPUs, and we had GPUs.  
**Translation:** 

**[8179.56s] English:** And if you squint and turn your head, what a GPU is, it's just a mini-core, very simple CPU thing, kind of, right?  
**Translation:** Vocabulary: squint: 眯眼看

**[8186.50s] English:** And 10 years ago, it was CPUs and GPUs and graphics.  
**Translation:** 

**[8193.80s] English:** Today, we have CPUs, GPUs, graphics, and AI.  
**Translation:** 

**[8199.42s] English:** Because it's so important, because the compute is so demanding, because of the smart cameras and the watches and all the different places the AI needs to work in our lives, it's caused this explosion of hardware.  
**Translation:** 

**[8210.32s] English:** And so part of my thesis, part of my belief of where computing goes, if you look out 10 years from now,  
**Translation:** Vocabulary: computing: 计算

**[8216.18s] English:** is that it's not just a computer, it's a machine.  
**Translation:** 

**[8216.48s] English:** It's a machine.  
**Translation:** 

**[8216.50s] English:** It's not going to get simpler.  
**Translation:** 

**[8218.40s] English:** Physics isn't going back to where we came from.  
**Translation:** 

**[8220.60s] English:** It's only going to get weirder from here on out, right?  
**Translation:** 

**[8223.48s] English:** And so to me, the exciting part about what we're building is it's about building that universal platform, which the world can continue to get weird, because again, I don't think it's avoidable, it's physics.  
**Translation:** 

**[8235.28s] English:** But we can help lift people's scale, do things with it, and they don't have to rewrite their code every time a new device comes out.  
**Translation:** 

**[8240.96s] English:** And I think that's pretty cool.  
**Translation:** 

**[8242.22s] English:** And so if Mojo can help with that problem, then I think that it will be, hopefully,  
**Translation:** 

**[8246.34s] English:** quite interesting and quite useful to a wide range of people, because there's so much potential.  
**Translation:** 

**[8251.16s] English:** And maybe analog computers will become a thing or something, right?  
**Translation:** 

**[8255.22s] English:** And we need to be able to get into a mode where we can move this programming model forward,  
**Translation:** Vocabulary: analog: 模拟的

**[8259.96s] English:** but do so in a way where we're lifting people and growing them instead of forcing them to rewrite all their code and exploding them.  
**Translation:** 

**[8266.70s] English:** Do you think there'll be a few major libraries that go Mojo first?  
**Translation:** Vocabulary: exploding: 摧毁

**[8273.52s] English:** Well, so I mean, the modular engine is all Mojo.  
**Translation:** 

**[8276.34s] English:** So again, come back to like, we're not building Mojo because it's fun.  
**Translation:** Vocabulary: modular: 模块化的

**[8280.00s] English:** because we had to to solve these accelerators that's the origin story but i mean ones that  
**Translation:** 

**[8284.54s] English:** are currently in python yeah so i think that a number of these projects will and so one of the  
**Translation:** 

**[8288.46s] English:** things again this is just my best guess like each of the package maintainers also has i'm sure plenty  
**Translation:** 

**[8293.46s] English:** of other things going on people don't like really don't like rewriting code just for the sake of  
**Translation:** Vocabulary: maintainers: 维护者; rewriting: 重写代码

**[8297.10s] English:** rewriting code um but sometimes like people are excited about like adopting a new idea yeah it  
**Translation:** 

**[8304.78s] English:** turns out that while rewriting code is generally not people's first thing turns out that redesigning  
**Translation:** 

**[8311.14s] English:** something while you rewrite it and using a rewrite as an excuse to redesign can lead to the 2.0 of  
**Translation:** 

**[8317.88s] English:** your thing that's way better than the 1.0 right and so i have no idea i can't predict that but  
**Translation:** 

**[8323.66s] English:** there's a lot of these places where again if you have a package that is half c and half python  
**Translation:** 

**[8328.76s] English:** right you just solve the pain make it easier to move things faster make it easier to debug and  
**Translation:** 

**[8333.60s] English:** evolve your  
**Translation:** 

**[8334.22s] English:** you  
**Translation:** 

**[8334.78s] English:** major tech adopting mojo kind of makes sense to start with and then it gives you this opportunity  
**Translation:** 

**[8338.88s] English:** to rethink these things so the two big gains are that there's a performance gain and then  
**Translation:** 

**[8345.34s] English:** there's the portability to all kinds of different devices and there's safety right so you talk about  
**Translation:** 

**[8352.26s] English:** real types i mean not saying this is for everybody but that's actually a pretty big thing right  
**Translation:** Vocabulary: portability: 便携性

**[8357.92s] English:** and so there's a bunch of different aspects of what you know what value mojo provides  
**Translation:** 

**[8362.78s] English:** and so i mean it's funny for me  
**Translation:** 

**[8364.22s] English:** Like, I've been working on these kinds of technologies and tools for too many years now.  
**Translation:** 

**[8370.18s] English:** But you look at Swift, right?  
**Translation:** 

**[8371.96s] English:** And we talked about Swift for TensorFlow, but Swift as a programming language, right?  
**Translation:** 

**[8376.34s] English:** Swift's now 13 years old from when I started it.  
**Translation:** 

**[8381.30s] English:** Yeah.  
**Translation:** 

**[8381.92s] English:** Because I started in 2010, if I remember.  
**Translation:** 

**[8384.46s] English:** And so that project, and I was involved with it for 12 years or something, right?  
**Translation:** 

**[8390.16s] English:** That project has gone through its own really interesting story arc, right?  
**Translation:** 

**[8393.66s] English:** And it's a mature, successful, used by millions of people system, right?  
**Translation:** 

**[8397.72s] English:** Certainly not dead yet, right?  
**Translation:** 

**[8400.00s] English:** But also, going through that story arc, I learned a tremendous amount about building languages, about building compilers, about working with community, and things like this.  
**Translation:** 

**[8407.78s] English:** And so that experience, I'm helping channel and bring directly into Mojo.  
**Translation:** Vocabulary: compilers: 编译器

**[8412.18s] English:** And other systems, same thing.  
**Translation:** 

**[8414.16s] English:** Apparently, I like building and iterating and evolving things.  
**Translation:** Vocabulary: evolving: 发展演变

**[8417.36s] English:** And so you look at this LLVM thing I worked on 20 years ago, and you look at MLIR, right?  
**Translation:** 

**[8422.60s] English:** And so a lot of the lessons learned in LLVM got fed into MLIR.  
**Translation:** 

**[8426.50s] English:** And I think that MLIR is a way better system than LLVM was.  
**Translation:** 

**[8429.42s] English:** And Swift is a really good system, and it's amazing.  
**Translation:** 

**[8433.16s] English:** But I hope that Mojo will take the next step forward in terms of design.  
**Translation:** 

**[8440.48s] English:** In terms of running Mojo, people can play with it.  
**Translation:** 

**[8443.52s] English:** What's Mojo Playground?  
**Translation:** 

**[8445.52s] English:** Yeah.  
**Translation:** 

**[8445.98s] English:** And from the interface perspective and from the hardware perspective, what's this incredible thing running on?  
**Translation:** 

**[8454.54s] English:** Yeah.  
**Translation:** Vocabulary: interface: 用户界面

**[8454.86s] English:** So right now, here we are two weeks after launch.  
**Translation:** 

**[8457.62s] English:** Yes.  
**Translation:** 

**[8457.86s] English:** We decided that, okay, we're...  
**Translation:** 

**[8459.40s] English:** We have this incredible set of technology that we think might be good, but we have not given it to lots of people yet.  
**Translation:** 

**[8466.48s] English:** And so we were very conservative and said, let's put it in a workbook so that if it crashes, we can do something about it.  
**Translation:** 

**[8471.66s] English:** We can monitor and track that, right?  
**Translation:** Vocabulary: workbook: 工作簿

**[8473.56s] English:** And so, again, things are still super early, but we're having, like, one person a minute sign up with over 70,000 people two weeks in.  
**Translation:** 

**[8485.02s] English:** It's kind of crazy.  
**Translation:** 

**[8485.84s] English:** So you can sign up to Mojo Playground, and you can use it.  
**Translation:** 

**[8489.40s] English:** In the cloud.  
**Translation:** 

**[8490.76s] English:** Yeah.  
**Translation:** 

**[8491.22s] English:** In your browser.  
**Translation:** 

**[8492.40s] English:** And so what that's running on, right?  
**Translation:** 

**[8493.48s] English:** Notebook.  
**Translation:** 

**[8493.80s] English:** Yeah, what that's running on is that's running on cloud VMs.  
**Translation:** 

**[8497.40s] English:** And so you share a machine with a bunch of other people.  
**Translation:** 

**[8500.66s] English:** But it turns out there's a bunch of them now because there's a lot of people.  
**Translation:** 

**[8503.90s] English:** And so what you're doing is you're getting free compute, and you're getting to play with this thing in kind of a limited, controlled way so that we can make sure that it doesn't totally crash and be embarrassing, right?  
**Translation:** 

**[8514.84s] English:** Yeah.  
**Translation:** 

**[8515.78s] English:** So now a lot of the feedback we've gotten is people want to download it locally.  
**Translation:** 

**[8518.80s] English:** So we're working on that.  
**Translation:** 

**[8519.40s] English:** Right now.  
**Translation:** 

**[8520.00s] English:** So that's the goal, to be able to download locally into it.  
**Translation:** 

**[8523.40s] English:** Yeah, that's what everybody expects.  
**Translation:** 

**[8524.66s] English:** And so we're working on that right now.  
**Translation:** 

**[8525.94s] English:** And so we just want to make sure that we do it right.  
**Translation:** 

**[8527.98s] English:** And I think this is one of the lessons I learned from Swift also, by the way,  
**Translation:** 

**[8532.62s] English:** is that when we launched Swift, gosh, it feels like forever ago.  
**Translation:** 

**[8536.10s] English:** It was 2014.  
**Translation:** 

**[8537.72s] English:** And we, I mean, it was super exciting.  
**Translation:** 

**[8540.90s] English:** I and we, the team, had worked on Swift for a number of years in secrecy.  
**Translation:** 

**[8545.44s] English:** And we, four years into this development, roughly,  
**Translation:** Vocabulary: secrecy: 秘密

**[8550.00s] English:** of working on this thing, at that point,  
**Translation:** 

**[8552.54s] English:** about 250 people at Apple knew about it.  
**Translation:** 

**[8555.48s] English:** Okay, so it was secret.  
**Translation:** 

**[8556.58s] English:** Apple's good at secrecy, and it was a secret project.  
**Translation:** 

**[8559.02s] English:** And so we launched this at WWC, a bunch of hoopla and excitement,  
**Translation:** 

**[8562.98s] English:** and said, developers, you're going to be able to develop  
**Translation:** Vocabulary: hoopla: 喧闹

**[8565.46s] English:** and submit apps to the App Store in three months.  
**Translation:** 

**[8569.08s] English:** Well, several interesting things happened, right?  
**Translation:** 

**[8571.62s] English:** So first of all, we learned that, A, it had a lot of bugs.  
**Translation:** 

**[8575.72s] English:** It was not actually production quality.  
**Translation:** 

**[8578.36s] English:** And it was extremely stressful.  
**Translation:** 

**[8580.00s] English:** In terms of, like, trying to get it working for a bunch of people.  
**Translation:** 

**[8583.72s] English:** And so what happened was we went from zero to, you know,  
**Translation:** 

**[8586.82s] English:** I don't know how many developers Apple had at the time,  
**Translation:** 

**[8588.68s] English:** but a lot of developers overnight.  
**Translation:** 

**[8591.10s] English:** And they ran into a lot of bugs, and it was really embarrassing.  
**Translation:** 

**[8593.92s] English:** And it was very stressful for everybody involved, right?  
**Translation:** 

**[8596.66s] English:** It was also very exciting, because everybody was excited about that.  
**Translation:** 

**[8599.88s] English:** The other thing I learned is that when that happened,  
**Translation:** 

**[8602.14s] English:** roughly every software engineer who did not know about the project at Apple,  
**Translation:** 

**[8605.74s] English:** their head exploded when it was launched, because they didn't know it was coming.  
**Translation:** 

**[8609.28s] English:** And so,  
**Translation:** Vocabulary: exploded: 爆裂

**[8610.02s] English:** they're like, wait, what is this?  
**Translation:** 

**[8611.18s] English:** I signed up to work for Apple because I love Objective-C.  
**Translation:** 

**[8613.50s] English:** Why is there a new thing, right?  
**Translation:** 

**[8614.92s] English:** And so,  
**Translation:** 

**[8615.90s] English:** now what that meant, practically,  
**Translation:** 

**[8618.96s] English:** is that the push from launch to, first of all, the fall,  
**Translation:** 

**[8623.16s] English:** but then to 2.0 and 3.0 and, like, all the way forward,  
**Translation:** 

**[8626.82s] English:** was super painful for the engineering team and myself.  
**Translation:** 

**[8631.34s] English:** It was very stressful.  
**Translation:** 

**[8633.12s] English:** The developer community was very grumpy about it,  
**Translation:** Vocabulary: grumpy: 脾气坏的

**[8635.04s] English:** because they're like, okay, well, wait a second.  
**Translation:** 

**[8636.48s] English:** You're changing and breaking my code, and, like, we have to fix the bugs.  
**Translation:** 

**[8640.00s] English:** And it was just like a lot of tension and friction on all sides.  
**Translation:** 

**[8644.90s] English:** There's a lot of technical debt in the compiler because we have to run really fast.  
**Translation:** 

**[8649.36s] English:** You have to go implement the thing and unblock the use case and do the thing.  
**Translation:** 

**[8651.90s] English:** And you know it's not right, but you never have time to go back and do it right.  
**Translation:** 

**[8654.86s] English:** And I'm very proud of the Swift team because they've come, I mean, we, but they came so far and made so much progress over this time since launch.  
**Translation:** 

**[8666.14s] English:** It's pretty incredible.  
**Translation:** 

**[8667.22s] English:** And Swift is a very, very good thing.  
**Translation:** 

**[8668.70s] English:** And I just don't want to do that again, right?  
**Translation:** 

**[8671.16s] English:** So iterate more through the development process.  
**Translation:** 

**[8675.56s] English:** And so what we're doing is we're not launching it when it's hopefully 0.9 with no testers.  
**Translation:** 

**[8680.28s] English:** We're launching it and saying it's 0.1, right?  
**Translation:** 

**[8683.12s] English:** And so we're setting expectations of saying like, okay, well, don't use this for production, right?  
**Translation:** 

**[8688.10s] English:** If you're interested in what we're doing, we'll do it in an open way and we can do it together.  
**Translation:** 

**[8693.10s] English:** But don't use it in production yet.  
**Translation:** 

**[8694.80s] English:** Like we'll get there, but let's do it the right way.  
**Translation:** 

**[8697.52s] English:** And I'm also saying.  
**Translation:** 

**[8699.16s] English:** We're not in a race.  
**Translation:** 

**[8700.86s] English:** The thing that I want to do is build the world's best thing.  
**Translation:** 

**[8703.92s] English:** Yeah.  
**Translation:** 

**[8704.60s] English:** Right.  
**Translation:** 

**[8705.08s] English:** Because if you do it right and it lifts the industry, it doesn't matter if it takes an extra two months.  
**Translation:** 

**[8709.96s] English:** Yeah.  
**Translation:** 

**[8710.48s] English:** Like two months is worth waiting.  
**Translation:** 

**[8711.56s] English:** And so doing it right and not being overwhelmed with technical debt and things like this is like, again, war wounds, lessons learned, whatever you want to say, I think is absolutely the right thing to do.  
**Translation:** 

**[8723.98s] English:** Even though right now people are very frustrated that, you know, you can't download it or it doesn't have feature.  
**Translation:** 

**[8728.70s] English:** X or something like this.  
**Translation:** 

**[8730.06s] English:** What have you learned in a little bit of time since it's been released into the wild that people have been complaining about feature X or Y or Z?  
**Translation:** 

**[8741.74s] English:** What have they been complaining about?  
**Translation:** 

**[8743.26s] English:** What they have been excited about?  
**Translation:** 

**[8746.48s] English:** Like, yeah, almost like detailed things versus.  
**Translation:** 

**[8749.24s] English:** I think everyone would be very excited about the big vision.  
**Translation:** 

**[8753.06s] English:** Yeah.  
**Translation:** 

**[8753.30s] English:** Yeah.  
**Translation:** 

**[8753.48s] English:** Well, so, I mean, I've been very pleased.  
**Translation:** 

**[8754.68s] English:** I mean, in fact, I mean, we've been massively overwhelmed with response, which is.  
**Translation:** 

**[8758.70s] English:** A good problem to have.  
**Translation:** Vocabulary: massively: 极其

**[8760.00s] English:** have um it's kind of like a success disaster yeah in a sense right um and um so i mean if you go  
**Translation:** 

**[8767.42s] English:** back in time when we started modular which is just not yet a year and a half ago so it's still a  
**Translation:** Vocabulary: modular: 模块化的

**[8772.88s] English:** pretty new company new team small but very good team of people like we started with extreme  
**Translation:** 

**[8778.98s] English:** conviction that there's a set of problems that we need to solve and if we solve it then people will  
**Translation:** 

**[8784.06s] English:** be interested in what we're doing right but but again you're building in basically secret right  
**Translation:** 

**[8789.38s] English:** you're trying to figure it out it's the creation is a messy process you're having to go through  
**Translation:** 

**[8793.98s] English:** different paths and understand what you want to do and how to explain it often when you're doing  
**Translation:** 

**[8798.14s] English:** disruptive and new kinds of things just knowing how to explain it is super difficult right um and  
**Translation:** Vocabulary: disruptive: 破坏性的

**[8804.62s] English:** so when we launched we hoped people would be excited but you know i'm i'm an optimist but i'm  
**Translation:** 

**[8810.64s] English:** also like don't want to get ahead of myself and so when people found out about mojo i think their  
**Translation:** Vocabulary: optimist: 乐天派

**[8816.08s] English:** heads exploded a little bit right and you know  
**Translation:** 

**[8819.38s] English:** here here's a i think a pretty credible team that has built some languages and some tools before and  
**Translation:** Vocabulary: credible: 可信的

**[8823.58s] English:** so they have some lessons learned and are tackling some of the deep problems in the python ecosystem  
**Translation:** 

**[8829.26s] English:** and giving it the love and attention that it should be getting and i think people got very  
**Translation:** Vocabulary: tackling: 应对

**[8833.32s] English:** excited about that and so if you look at that i mean i think people are excited about ownership  
**Translation:** 

**[8837.32s] English:** and taking a step beyond rust right there's people that are very excited about that there's people  
**Translation:** 

**[8841.22s] English:** that are excited about uh you know just like i made game of life go 400 times faster right and  
**Translation:** 

**[8848.20s] English:** things like that and that's really cool  
**Translation:** 

**[8849.38s] English:** there are people that are really excited about the okay i really hate writing stuff in c++  
**Translation:** 

**[8853.94s] English:** save me like systems in your they're like stepping up like yeah yes so that that's that's that's that's  
**Translation:** 

**[8859.38s] English:** me by the way also um i really want to stop writing c++ but the um i get third person excitement  
**Translation:** 

**[8867.54s] English:** when people tweet yeah i made this code game of life or whatever it's faster and you're like yeah  
**Translation:** 

**[8873.94s] English:** yeah and and also like um well i would also say that um let me let me cast blame  
**Translation:** 

**[8879.38s] English:** out  
**Translation:** 

**[8880.00s] English:** to people who deserve it sure these terrible people who convinced me to do some of this yes  
**Translation:** 

**[8886.18s] English:** jeremy howard yes that guy well he's been pushing for this kind of thing he's wanted this for years  
**Translation:** Vocabulary: jeremy: 杰里米

**[8892.94s] English:** yeah he's wanted this for a long time for years and for people who don't know jeremy howard he's  
**Translation:** 

**[8897.44s] English:** like one of the most legit people in the machine learning community he's uh he's a grassroots he  
**Translation:** Vocabulary: grassroots: 基层; legit: 正经

**[8903.84s] English:** really teaches he's an incredible educator he's an incredible teacher but also legit uh in terms  
**Translation:** 

**[8908.72s] English:** of a machine learning engineer himself yeah he's been running the fast.ai and looking i think for  
**Translation:** Vocabulary: educator: 教育者

**[8914.84s] English:** exactly what you exactly and so and so um i mean the first time so i met jeremy pretty early on  
**Translation:** 

**[8922.12s] English:** but the first time i sat up and i'm like this guy is ridiculous is when i was at google and  
**Translation:** 

**[8929.50s] English:** we're bringing up tpus and we had a whole team of people and we're there's this competition called  
**Translation:** 

**[8935.42s] English:** dawn bench of who can train uh  
**Translation:** 

**[8938.72s] English:** image net yeah fastest right yes and jeremy and one of his researchers  
**Translation:** 

**[8943.46s] English:** crushed google by not through sheer force of the amazing amount of compute and the number of tpus  
**Translation:** 

**[8950.36s] English:** and stuff like that that he just decided that progressive imagery sizing was the right way to  
**Translation:** 

**[8955.58s] English:** train the model and fury epochs faster and make the whole thing go go vroom right and i'm like  
**Translation:** Vocabulary: epochs: 训练周期; vroom: 加速

**[8961.94s] English:** this guy is incredible right and so you can say anyways come back to you know where's mojo coming  
**Translation:** 

**[8968.72s] English:** chris finally listened to jeremy it's all his fault but there's a kind of very uh refreshing uh  
**Translation:** 

**[8977.92s] English:** pragmatic view that he has about machine learning that um i don't know if it's like this mix of uh  
**Translation:** 

**[8986.68s] English:** desire for efficiency but ultimately grounded and desire to make uh machine learning more  
**Translation:** Vocabulary: pragmatic: 实用主义的

**[8992.14s] English:** accessible to a lot of people i don't know what that is i guess that's coupled with efficiency  
**Translation:** 

**[8996.32s] English:** and performance but it's not just efficiency it's not just efficiency it's not just efficiency it's  
**Translation:** 

**[8998.56s] English:** not just efficiency it's not just efficiency it's not just efficiency it's not just efficiency  
**Translation:** 

**[8998.72s] English:** i'm not just obsessed about  
**Translation:** 

**[9000.00s] English:** performance so a lot of ai and ai research ends up being that it has to go fast enough to get scale  
**Translation:** 

**[9006.48s] English:** so a lot of people don't actually care about performance particularly on the research side  
**Translation:** 

**[9010.48s] English:** until it allows them to have more a bigger data set right and so suddenly now you care about  
**Translation:** 

**[9015.48s] English:** distributed compute and like all these exotic hpc like you don't actually want to know about that  
**Translation:** 

**[9020.16s] English:** you just want to be able to do more experiments faster and do so with bigger data sets right  
**Translation:** 

**[9024.60s] English:** and so jeremy has been really pushing the limits and one of the things i'll say about jeremy  
**Translation:** Vocabulary: jeremy: 杰里米

**[9029.14s] English:** and there's many things i could say about jeremy because i'm a fanboy of his but uh he uh it fits  
**Translation:** 

**[9035.22s] English:** in his head and jeremy actually takes the time where many people don't to really dive deep into  
**Translation:** 

**[9041.28s] English:** why is the beta parameter of the atom optimizer equal to this yeah right and he'll go survey and  
**Translation:** 

**[9048.18s] English:** understand what are all the activation functions and the trade-offs and why is it that everybody  
**Translation:** Vocabulary: optimizer: 优化器; parameter: 参数

**[9052.24s] English:** that does uh you know this model pick that thing so the why not just trying different values like  
**Translation:** 

**[9058.84s] English:** really  
**Translation:** 

**[9059.14s] English:** what is going on here right and so as a consequence of that like he's always he  
**Translation:** 

**[9063.54s] English:** again he makes time but he he spends time to understand things at a depth that a lot of people  
**Translation:** 

**[9068.80s] English:** don't and as you say he then brings it and teaches people and he's his mission is to help lift you  
**Translation:** 

**[9076.14s] English:** know his website says making ai uncool again like it's about like forget about the hype let's it's  
**Translation:** 

**[9081.24s] English:** actually practical and useful let's teach people how to do this right now the problem jeremy  
**Translation:** 

**[9085.54s] English:** struggled with is that he's pushing the envelope right research isn't  
**Translation:** Vocabulary: struggled: 挣扎

**[9089.14s] English:** about doing the thing that is staying on the happy path or the the well-paved road right  
**Translation:** 

**[9093.70s] English:** and so a lot of the systems today have been these really fragile fragmented things or special case  
**Translation:** Vocabulary: fragile: 易碎; fragmented: 碎片化

**[9099.38s] English:** in this happy path and if you fall off the happy path you get eaten by an alligator uh so  
**Translation:** 

**[9105.54s] English:** what about uh so python has this giant ecosystem of packages uh  
**Translation:** Vocabulary: alligator: 鳄鱼

**[9112.48s] English:** and there's a package repository do you have ideas of how to do that well for mojo yeah how to do it  
**Translation:** 

**[9119.14s] English:** repository at  
**Translation:** Vocabulary: repository: 软件仓库

**[9120.00s] English:** Well, so that's another really interesting problem that I knew about, but I didn't understand how big of a problem it was.  
**Translation:** 

**[9126.88s] English:** Python packaging, a lot of people have very big pain points and a lot of scars with Python packaging.  
**Translation:** 

**[9133.12s] English:** Oh, you mean, so there's several things.  
**Translation:** 

**[9134.98s] English:** Building and distributing and managing dependencies and versioning and all this stuff.  
**Translation:** Vocabulary: versioning: 版本管理

**[9139.88s] English:** So from the perspective of if you want to create your own package.  
**Translation:** 

**[9143.16s] English:** Yes.  
**Translation:** 

**[9143.46s] English:** Or you want to build on top of a bunch of other people's packages and then they get updated and things like this.  
**Translation:** 

**[9148.52s] English:** Now, I'm not an expert in this, so I don't know the answer.  
**Translation:** 

**[9153.58s] English:** I think this is one of the reasons why it's great that we work as a team and there's other really good and smart people involved.  
**Translation:** 

**[9160.56s] English:** But one of the things I've heard from smart people who've done a lot of this is that the packaging becomes a huge disaster when you get the Python and C together.  
**Translation:** 

**[9170.86s] English:** And so if you have this problem where you have code split between Python and C.  
**Translation:** 

**[9175.68s] English:** Now, not only do you have to package the C code.  
**Translation:** 

**[9178.18s] English:** You have to build the C code.  
**Translation:** 

**[9180.00s] English:** C doesn't have a package manager.  
**Translation:** 

**[9182.40s] English:** C doesn't have a dependency versioning management system.  
**Translation:** 

**[9185.94s] English:** And so I'm not experienced in the state of the art and all the different Python package managers.  
**Translation:** 

**[9192.58s] English:** But my understanding is that's a massive part of the problem.  
**Translation:** 

**[9195.92s] English:** And I think Mojo solves that part of the problem directly heads on.  
**Translation:** 

**[9199.36s] English:** Now, one of the things I think we'll do with the community, and this isn't, again, we're not solving all the world's problems at once.  
**Translation:** 

**[9205.18s] English:** We have to be kind of focused to start with.  
**Translation:** 

**[9207.54s] English:** Is that.  
**Translation:** 

**[9208.18s] English:** I think that we will have an opportunity to reevaluate packaging.  
**Translation:** Vocabulary: reevaluate: 重新评估

**[9211.74s] English:** Right.  
**Translation:** 

**[9212.18s] English:** And so I think that we can come back and say, OK, well, given the new tools and technologies and the cool things we have that we've built up because we have not just syntax.  
**Translation:** Vocabulary: syntax: 句法

**[9219.90s] English:** We have an entirely new compiler stack that works in a new way.  
**Translation:** 

**[9222.82s] English:** Maybe there's other innovations we can bring together and maybe we can help solve that problem.  
**Translation:** Vocabulary: innovations: 创新

**[9227.02s] English:** So almost a tangent to that question from the user perspective of packages.  
**Translation:** 

**[9230.40s] English:** It was always surprising to me that it was not easier to sort of explore and find packages.  
**Translation:** Vocabulary: tangent: 旁枝话题

**[9238.18s] English:** Yes.  
**Translation:** 

**[9238.30s] English:** Yes.  
**Translation:** 

**[9238.34s] English:** Yes.  
**Translation:** 

**[9238.38s] English:** Yes.  
**Translation:** 

**[9240.00s] English:** you know with with pip install and it just it feels uh it's an incredible ecosystem it's just  
**Translation:** 

**[9246.86s] English:** uh interesting that it wasn't made it's still i think not made easier to discover packages to do  
**Translation:** 

**[9253.24s] English:** yeah like uh uh search and discovery as youtube calls it well i mean it's kind of funny because  
**Translation:** 

**[9261.58s] English:** this is one of the challenges of these like intentionally decentralized communities  
**Translation:** Vocabulary: decentralized: 分散管理的

**[9266.56s] English:** and so i don't know what the right answer is for python i mean there are many people that would  
**Translation:** 

**[9271.02s] English:** or i don't even know the right answer for mojo like so there are many people that would have  
**Translation:** 

**[9277.08s] English:** much more informed opinions than i do but but it's interesting if you look at this right open  
**Translation:** 

**[9280.74s] English:** source communities um you know there's git git is a fully decentralized anybody could do it any  
**Translation:** 

**[9286.84s] English:** way they want but then there's github right and github centralized commercial in that case right  
**Translation:** 

**[9292.84s] English:** thing uh really helped pull together and help solve some of the discoveries  
**Translation:** 

**[9296.56s] English:** problems and help build a more consistent community and so maybe there's opportunities  
**Translation:** 

**[9301.48s] English:** for something like a github for yeah although even github i might be wrong on this but the  
**Translation:** 

**[9306.94s] English:** search and discovery for github is not that great like i still use google search yeah well i mean  
**Translation:** 

**[9313.90s] English:** maybe that's because github doesn't want to replace google search right and i think there  
**Translation:** 

**[9319.24s] English:** is room for specialized solutions to specific problems but sure i don't know i don't know the  
**Translation:** 

**[9324.28s] English:** right answer for github either that's i think  
**Translation:** 

**[9326.56s] English:** they can go figure that out but the point is to have an interface that's usable that's accessible  
**Translation:** 

**[9331.48s] English:** to people of all different skill levels well well and again like what are the benefit of standards  
**Translation:** Vocabulary: interface: 人机界面; usable: 可使用的

**[9335.88s] English:** right standards allow you to build these next level up ecosystem the next level of infrastructure  
**Translation:** 

**[9340.84s] English:** or next level of things and so um again come back to i hate complexity c c plus python is  
**Translation:** Vocabulary: complexity: 复杂性

**[9348.12s] English:** complicated it makes everything more difficult to deal with it makes it difficult to port move  
**Translation:** 

**[9352.84s] English:** code around work with all these things get more complicated and so  
**Translation:** 

**[9356.56s] English:** i mean i'm not an expert but maybe mojo can help a little bit by  
**Translation:** 

**[9360.00s] English:** helping reduce the amount of C in this ecosystem  
**Translation:** 

**[9362.42s] English:** and make it, therefore, scale better.  
**Translation:** 

**[9363.88s] English:** So any kind of packages that are hybrid in nature  
**Translation:** 

**[9366.50s] English:** would be a natural fit to move to Moja.  
**Translation:** 

**[9369.42s] English:** Which is a lot of them, by the way.  
**Translation:** 

**[9370.94s] English:** A lot of them, especially,  
**Translation:** 

**[9373.56s] English:** they're doing some interesting stuff, computation-wise.  
**Translation:** 

**[9376.82s] English:** Let me ask you about some features.  
**Translation:** 

**[9378.86s] English:** Yeah.  
**Translation:** 

**[9379.66s] English:** So we talked about, obviously, indentation,  
**Translation:** 

**[9382.26s] English:** that it's a typed language or optionally typed.  
**Translation:** Vocabulary: indentation: 缩进; optionally: 可选地

**[9385.80s] English:** Is that the right way to say it?  
**Translation:** 

**[9387.22s] English:** It's either optionally or progressively.  
**Translation:** Vocabulary: progressively: 逐步地

**[9389.04s] English:** Progressively.  
**Translation:** 

**[9389.44s] English:** So people have very strong opinions on the right word to use.  
**Translation:** 

**[9393.58s] English:** Yeah.  
**Translation:** 

**[9394.28s] English:** I don't know.  
**Translation:** 

**[9395.06s] English:** I look forward to your letters.  
**Translation:** 

**[9397.58s] English:** So there's the var versus let.  
**Translation:** 

**[9400.08s] English:** But let is for constants.  
**Translation:** 

**[9402.44s] English:** Var is an optional.  
**Translation:** Vocabulary: constants: 常量; optional: 可选的

**[9404.44s] English:** Yeah, var makes it mutable, so you can reassign.  
**Translation:** 

**[9407.16s] English:** Okay.  
**Translation:** Vocabulary: reassign: 重新分配

**[9408.28s] English:** Then there's function overloading.  
**Translation:** 

**[9412.56s] English:** Oh, okay.  
**Translation:** Vocabulary: overloading: 函数重载

**[9413.30s] English:** Yeah.  
**Translation:** 

**[9414.12s] English:** I mean, there's a lot of source of happiness for me,  
**Translation:** 

**[9416.34s] English:** but function overloading, that's, I guess,  
**Translation:** 

**[9419.44s] English:** is that for performance?  
**Translation:** 

**[9423.50s] English:** Why does Python not have function overloading?  
**Translation:** 

**[9427.04s] English:** So I can speculate.  
**Translation:** Vocabulary: speculate: 猜测

**[9428.40s] English:** So Python is a dynamic language.  
**Translation:** 

**[9430.58s] English:** The way it works is that Python and Objective-C  
**Translation:** 

**[9435.18s] English:** are actually very similar worlds if you ignore syntax.  
**Translation:** 

**[9441.04s] English:** And so Objective-C is straight line derived from small talk,  
**Translation:** Vocabulary: syntax: 语法规则

**[9446.58s] English:** a really venerable, interesting,  
**Translation:** 

**[9449.44s] English:** language that much of the world has forgotten about,  
**Translation:** Vocabulary: venerable: 德高望重

**[9451.84s] English:** but the people that remember it love it, generally.  
**Translation:** 

**[9454.84s] English:** And the way that small talk works is that every object  
**Translation:** 

**[9457.34s] English:** has a dictionary in it.  
**Translation:** 

**[9459.10s] English:** And the dictionary maps from the name of a function  
**Translation:** 

**[9461.42s] English:** or the name of a value within an object to its implementation.  
**Translation:** 

**[9465.64s] English:** And so the way you call a method in Objective-C is you say,  
**Translation:** Vocabulary: implementation: 实现

**[9469.02s] English:** go look up, the way I call foo is I go look up foo,  
**Translation:** 

**[9472.10s] English:** I get a pointer to the function back, and then I call it.  
**Translation:** 

**[9475.20s] English:** That's how Python works.  
**Translation:** 

**[9476.68s] English:** Right.  
**Translation:** 

**[9477.52s] English:** And so now the problem with that is that,  
**Translation:** 

**[9479.28s] English:** the dictionary  
**Translation:** 

**[9480.00s] English:** within a python object all the keys are strings and it's a dictionary yeah so you can only have  
**Translation:** 

**[9485.46s] English:** one entry per name you think it's as simple as that i think it's as simple as that and so now  
**Translation:** 

**[9490.60s] English:** why do they never fix this like why do they not change it to not be a dictionary when they don't  
**Translation:** 

**[9495.52s] English:** change like do other things um well you don't really have to in python because it's dynamic  
**Translation:** 

**[9501.40s] English:** and so you can say i get into the function now if i got past an integer do some dynamic tests for it  
**Translation:** 

**[9507.22s] English:** if it's a string go do another thing um there's another additional challenge which is even if you  
**Translation:** Vocabulary: integer: 整数

**[9512.34s] English:** did support overloading you're saying okay well here's a version of a function for integers and  
**Translation:** 

**[9516.44s] English:** a function for strings well you'd have even if you could put it in that dictionary you'd have  
**Translation:** 

**[9520.64s] English:** to have the caller do the dispatch and so every time you call the function you'd have to say like  
**Translation:** 

**[9525.08s] English:** is an integer is a string and so you'd have to figure out where to do that test and so in a  
**Translation:** Vocabulary: dispatch: 分发处理

**[9529.52s] English:** dynamic language um overloading is something you generally you don't have to have so but now you  
**Translation:** 

**[9536.48s] English:** get into a test  
**Translation:** Vocabulary: overloading: 重载函数

**[9537.22s] English:** language and you know in python if you subscript with an integer then you get typically one element  
**Translation:** 

**[9544.92s] English:** out of a collection if you subscript with a range you get a different thing out right and so often  
**Translation:** 

**[9551.04s] English:** in type languages you'll want to be able to express the fact that cool i have different behavior  
**Translation:** 

**[9556.22s] English:** depending on what i actually pass into this thing if you can model that it can make it safer and  
**Translation:** 

**[9560.76s] English:** more predictable and faster and like all these things it somehow feels safer yes but also feels  
**Translation:** 

**[9566.96s] English:** impossible  
**Translation:** Vocabulary: predictable: 可预测的

**[9567.22s] English:** like in terms of clarity like you don't have to design hold different functions yeah well this is  
**Translation:** 

**[9573.32s] English:** also one of the the challenges with the existing python typing systems is that in practice like you  
**Translation:** 

**[9580.64s] English:** take subscript like in practice a lot of these functions they don't have one signature they  
**Translation:** 

**[9585.78s] English:** actually have different behavior in different cases and so this is why it's difficult to like  
**Translation:** 

**[9589.70s] English:** retrofit this into existing python code and make it play well with typing you kind of have to design  
**Translation:** 

**[9596.48s] English:** for that  
**Translation:** Vocabulary: retrofit: 返工以适应

**[9597.22s] English:** okay so there's a interesting distinction  
**Translation:** 

**[9600.00s] English:** that people that program Python might be interested in is def versus fn.  
**Translation:** 

**[9605.48s] English:** So it's two different ways to define a function.  
**Translation:** 

**[9608.76s] English:** And fn is a stricter version of def.  
**Translation:** 

**[9613.58s] English:** What's the coolness that comes from the strictness?  
**Translation:** 

**[9616.26s] English:** So here you get into what is the tradeoff with a superset?  
**Translation:** Vocabulary: tradeoff: 权衡取舍

**[9619.84s] English:** Yes.  
**Translation:** 

**[9620.52s] English:** Okay.  
**Translation:** 

**[9621.22s] English:** So a superset, you have to or you really want to be compatible.  
**Translation:** 

**[9624.88s] English:** If you're doing a superset, you've decided compatibility with existing code.  
**Translation:** Vocabulary: compatibility: 兼容性; compatible: 兼容的

**[9630.00s] English:** It's the important thing, even if some of the decisions they made were maybe not what you choose.  
**Translation:** 

**[9634.34s] English:** Yeah.  
**Translation:** 

**[9634.74s] English:** Okay.  
**Translation:** 

**[9636.04s] English:** So that means you put a lot of time into compatibility, and it means that you get locked into decisions of the past, even if they may not have been a good thing, right?  
**Translation:** 

**[9644.38s] English:** Now, systems programmers typically like to control things, right?  
**Translation:** 

**[9649.18s] English:** And they want to make sure that, you know, not in all cases, of course, and even systems programmers are not one thing, right?  
**Translation:** Vocabulary: programmers: 程序员

**[9655.24s] English:** But often you want predictability.  
**Translation:** 

**[9657.54s] English:** And so one of the things that Python has, for example...  
**Translation:** 

**[9660.00s] English:** As you know, is that if you define a variable, you just say x equals 4.  
**Translation:** 

**[9663.88s] English:** I have a variable named x.  
**Translation:** 

**[9666.62s] English:** Now I say some long name equals 17.  
**Translation:** 

**[9671.32s] English:** Print out some long name.  
**Translation:** 

**[9673.38s] English:** Oops, but I typoed it.  
**Translation:** 

**[9675.32s] English:** Right?  
**Translation:** 

**[9675.54s] English:** Well, the compiler, the Python compiler doesn't know, in all cases, what you're defining and what you're using.  
**Translation:** 

**[9681.08s] English:** And did you typo the use of it or the definition?  
**Translation:** 

**[9684.64s] English:** Right?  
**Translation:** 

**[9684.76s] English:** And so for people coming from type languages, again, I'm not saying they're right or wrong.  
**Translation:** 

**[9690.00s] English:** But that drives them crazy because they want the compiler to tell them, you typoed the name of this thing, right?  
**Translation:** 

**[9695.34s] English:** And so what FN does is it turns on, as you say, it's a strict mode.  
**Translation:** 

**[9698.68s] English:** And so it says, okay, well, you have to actually intentionally declare your variables before you use them.  
**Translation:** 

**[9703.34s] English:** That gives you more predictability, more error checking and things like this.  
**Translation:** 

**[9707.54s] English:** But you don't have to use it.  
**Translation:** 

**[9711.66s] English:** And this is a way that Mojo is both compatible, because defs work the same way that defs have always worked.  
**Translation:** 

**[9717.80s] English:** But it provides a new alternative that gives you more compatibility.  
**Translation:** 

**[9720.00s] English:** and it allows certain kinds of people that have a different philosophy  
**Translation:** 

**[9723.04s] English:** to be able to express that and get that.  
**Translation:** 

**[9725.50s] English:** But usually, if you're writing Mojo code from scratch, you'll be using Fn.  
**Translation:** 

**[9730.52s] English:** It depends.  
**Translation:** 

**[9731.28s] English:** Again, it depends on your mentality, right?  
**Translation:** 

**[9733.32s] English:** It's not that def is Python and Fn is Mojo.  
**Translation:** 

**[9737.64s] English:** Mojo has both, and it loves both, right?  
**Translation:** 

**[9739.70s] English:** It really depends on...  
**Translation:** 

**[9740.58s] English:** Python is just straight.  
**Translation:** 

**[9741.40s] English:** Yeah, exactly.  
**Translation:** 

**[9742.32s] English:** Are you playing around and scripting something out,  
**Translation:** 

**[9745.06s] English:** and is it a one-off throwaway script?  
**Translation:** 

**[9747.14s] English:** Cool.  
**Translation:** Vocabulary: throwaway: 一次性用品

**[9747.70s] English:** Like, Python is great at that.  
**Translation:** 

**[9749.12s] English:** I will still be using Fn, but, yeah.  
**Translation:** 

**[9751.42s] English:** I love strictness.  
**Translation:** 

**[9753.04s] English:** Okay, well, so...  
**Translation:** 

**[9754.10s] English:** Control.  
**Translation:** 

**[9755.16s] English:** Power.  
**Translation:** 

**[9755.74s] English:** You also like suffering, right?  
**Translation:** 

**[9758.02s] English:** Yes.  
**Translation:** 

**[9758.86s] English:** I go hand in hand.  
**Translation:** 

**[9759.74s] English:** How many pull-ups?  
**Translation:** 

**[9762.80s] English:** I've lost count at this point.  
**Translation:** 

**[9766.20s] English:** And that's cool.  
**Translation:** 

**[9766.96s] English:** I love you for that.  
**Translation:** 

**[9767.86s] English:** And I love other people who like strict things, right?  
**Translation:** 

**[9770.44s] English:** But I don't want to say that that's the right thing,  
**Translation:** 

**[9773.50s] English:** because Python is also very beautiful for hacking around  
**Translation:** Vocabulary: hacking: 随意编程

**[9775.90s] English:** and doing stuff and research and these other cases  
**Translation:** 

**[9778.30s] English:** where you may not want that.  
**Translation:** 

**[9779.20s] English:** You see, I just feel like...  
**Translation:** 

**[9781.50s] English:** Maybe I'm wrong on that,  
**Translation:** 

**[9782.60s] English:** but it feels like strictness leads to faster debugging.  
**Translation:** 

**[9785.68s] English:** So in terms of going from...  
**Translation:** 

**[9787.82s] English:** Even on a small project, from zero to completion,  
**Translation:** 

**[9790.82s] English:** it just...  
**Translation:** 

**[9791.60s] English:** I guess it depends how many bugs you generate, usually.  
**Translation:** 

**[9794.94s] English:** Well, so, I mean, it's, again, lessons learned  
**Translation:** 

**[9796.88s] English:** in looking at the ecosystem.  
**Translation:** 

**[9798.08s] English:** It's really...  
**Translation:** 

**[9799.44s] English:** I mean, I think it's...  
**Translation:** 

**[9800.60s] English:** If you study some of these languages over time,  
**Translation:** 

**[9802.88s] English:** like the Ruby community, for example.  
**Translation:** 

**[9805.22s] English:** Now, Ruby is a pretty well-developed,  
**Translation:** 

**[9807.16s] English:** pretty established community,  
**Translation:** 

**[9808.12s] English:** but along the way, it's a pretty well-developed community.  
**Translation:** 

**[9809.10s] English:** So I think that the Ruby community  
**Translation:** 

**[9813.32s] English:** has really pushed forward the state-of-the-art of testing  
**Translation:** 

**[9816.52s] English:** because they didn't have a type system  
**Translation:** 

**[9818.42s] English:** that caught a lot of bugs at compile time, right?  
**Translation:** 

**[9820.92s] English:** And so you can have the best of both worlds.  
**Translation:** 

**[9823.20s] English:** You can have good testing and good types, right?  
**Translation:** 

**[9824.86s] English:** And things like this.  
**Translation:** 

**[9825.86s] English:** But I thought that it was really interesting  
**Translation:** 

**[9827.72s] English:** to see how certain challenges get solved.  
**Translation:** 

**[9830.06s] English:** And in Python, for example,  
**Translation:** 

**[9831.94s] English:** the interactive notebook kind of experiences  
**Translation:** 

**[9833.68s] English:** and stuff like this are really amazing.  
**Translation:** Vocabulary: interactive: 互动的

**[9835.54s] English:** And if you typo something, it doesn't matter.  
**Translation:** 

**[9837.76s] English:** It just tells you.  
**Translation:** 

**[9838.46s] English:** That's fine.  
**Translation:** 

**[9838.82s] English:** And so I think...  
**Translation:** 

**[9840.00s] English:** that the trade-offs are very different if you're building a um you know large-scale production  
**Translation:** 

**[9844.16s] English:** system versus you're building and exploring a notebook and speaking of control the hilarious  
**Translation:** 

**[9848.92s] English:** thing if you look at code i write just for myself for fun it's like littered with asserts everywhere  
**Translation:** 

**[9854.26s] English:** okay it's it's a kind of yeah you'd like types it's basically saying uh in a dictatorial way  
**Translation:** Vocabulary: dictatorial: 专制; littered: 布满

**[9864.10s] English:** this should be true now otherwise everything stops well and that that is the sign again i  
**Translation:** 

**[9871.16s] English:** love you man but that is a sign of somebody who likes control yeah and so yes i think that you'll  
**Translation:** 

**[9876.18s] English:** like fn this turn i think you'll like mojo therapy session yes i definitely will uh uh speaking of  
**Translation:** 

**[9882.86s] English:** asserts uh exceptions are called errors why is it called errors so we i mean we we use the same  
**Translation:** 

**[9889.08s] English:** we're the same as python right but um we implement in a very different way right and so  
**Translation:** 

**[9894.10s] English:** if you look at um other languages like we'll pick on c++ our favorite right uh c++ has a thing  
**Translation:** 

**[9900.62s] English:** called zero cost exception handling okay so and this is in my opinion something to learn lessons  
**Translation:** 

**[9908.42s] English:** from it's a nice polite way of saying it and so um and so zero cost exception handling the way  
**Translation:** 

**[9915.52s] English:** it works is that it's called zero cost because if you don't throw an exception there's supposed to  
**Translation:** 

**[9921.66s] English:** be no overhead for the non-error  
**Translation:** 

**[9924.04s] English:** um  
**Translation:** 

**[9924.10s] English:** code and so it takes the error path out of the uh the common path um it does this by making  
**Translation:** 

**[9932.00s] English:** throwing an error extremely expensive and so if you actually throw an error with a c++ compiler  
**Translation:** 

**[9937.96s] English:** using exceptions has to go look up in tables on the side and do all this stuff and so throwing  
**Translation:** Vocabulary: exceptions: 异常处理

**[9942.38s] English:** an error could be like 10 000 times more expensive than returning from a function right um also it's  
**Translation:** 

**[9948.68s] English:** called zero cost exceptions but it's not zero cost by any stretch of the imagination because  
**Translation:** 

**[9953.04s] English:** it massively bloats out  
**Translation:** 

**[9954.04s] English:** your code your binary it also adds a whole bunch of different paths because of destruction  
**Translation:** Vocabulary: binary: 二进制文件; bloats: 膨胀; massively: 大量地

**[9960.00s] English:** and other things like that that exist in C++.  
**Translation:** 

**[9962.46s] English:** And it reduces the number of optimizations.  
**Translation:** Vocabulary: optimizations: 优化

**[9964.60s] English:** It has like all these effects.  
**Translation:** 

**[9966.24s] English:** And so this thing that was called zero cost exceptions,  
**Translation:** 

**[9969.88s] English:** it really ain't, okay?  
**Translation:** 

**[9972.44s] English:** Now, if you fast forward to newer languages  
**Translation:** 

**[9975.76s] English:** and this includes Swift and Rust and Go and now Mojo,  
**Translation:** 

**[9982.88s] English:** well, and Python's a little bit different  
**Translation:** 

**[9984.12s] English:** because it's interpreted.  
**Translation:** 

**[9985.00s] English:** And so like, it's got a little bit  
**Translation:** Vocabulary: interpreted: 解释

**[9986.22s] English:** of a different thing going on.  
**Translation:** 

**[9987.06s] English:** But if you look at compiled languages,  
**Translation:** 

**[9990.00s] English:** many newer languages say, okay, well,  
**Translation:** 

**[9993.46s] English:** let's not do that zero cost exception handling thing.  
**Translation:** 

**[9997.00s] English:** Let's actually treat throwing an error the same  
**Translation:** 

**[10000.10s] English:** as returning a variant,  
**Translation:** 

**[10002.96s] English:** returning either the normal result or an error.  
**Translation:** 

**[10006.82s] English:** Now, programmers generally don't want to deal  
**Translation:** Vocabulary: programmers: 程序员

**[10010.62s] English:** with all the typing machinery  
**Translation:** 

**[10011.98s] English:** and like pushing around a variant.  
**Translation:** Vocabulary: machinery: 机器设备

**[10014.76s] English:** And so you use all the syntax that Python gives us,  
**Translation:** 

**[10017.26s] English:** for example, try and catch,  
**Translation:** Vocabulary: syntax: 语法规则

**[10018.60s] English:** you know, functions that raise and things like this.  
**Translation:** 

**[10021.52s] English:** You can put a raises decorator on your functions,  
**Translation:** Vocabulary: decorator: 装饰器

**[10024.32s] English:** stuff like this.  
**Translation:** 

**[10025.24s] English:** And if you want to control that,  
**Translation:** 

**[10026.68s] English:** and then the language can provide syntax for it,  
**Translation:** 

**[10029.90s] English:** but under the hood, the way the computer executes it,  
**Translation:** Vocabulary: executes: 运行

**[10032.56s] English:** throwing an error is basically as fast as returning something.  
**Translation:** 

**[10035.86s] English:** Oh, interesting.  
**Translation:** 

**[10036.70s] English:** So it's exactly the same way from a compiler perspective.  
**Translation:** 

**[10039.12s] English:** And so this is actually, I mean,  
**Translation:** 

**[10041.26s] English:** it's a fairly nerdy thing, right?  
**Translation:** 

**[10043.24s] English:** Which is why I love it.  
**Translation:** Vocabulary: nerdy: 书呆子气的

**[10044.80s] English:** But this has a huge impact on the way you design your API.  
**Translation:** 

**[10047.90s] English:** You design your APIs, right?  
**Translation:** 

**[10049.82s] English:** So in C++, huge communities turn off exceptions  
**Translation:** 

**[10055.06s] English:** because the cost is just so high, right?  
**Translation:** 

**[10057.52s] English:** And so the zero cost cost is so high, right?  
**Translation:** 

**[10060.42s] English:** And so that means that you can't actually use exceptions  
**Translation:** Vocabulary: exceptions: 例外情况

**[10063.42s] English:** in many libraries, right?  
**Translation:** 

**[10066.62s] English:** And even for the people that do use it, well, okay,  
**Translation:** 

**[10069.46s] English:** how and when do you want to pay the cost?  
**Translation:** 

**[10071.92s] English:** If I try to open a file, should I throw an error?  
**Translation:** 

**[10075.22s] English:** Well, what if I'm probing around looking for something?  
**Translation:** 

**[10077.88s] English:** Right?  
**Translation:** 

**[10078.72s] English:** I'm looking it up and made different paths.  
**Translation:** 

**[10080.00s] English:** If it's really slow to do that, maybe I'll add another function that doesn't throw an error or turns an error code instead.  
**Translation:** 

**[10086.90s] English:** And now I have two different versions of the same thing.  
**Translation:** 

**[10089.12s] English:** And so it causes you to fork your APIs.  
**Translation:** 

**[10091.68s] English:** And so, you know, one of the things I learned from Apple and I still love is the art of API design is actually really profound.  
**Translation:** 

**[10098.76s] English:** I think this is something that Python's also done a pretty good job at in terms of building out this large-scale package ecosystem.  
**Translation:** Vocabulary: profound: 深奥

**[10104.30s] English:** It's about having standards and things like this.  
**Translation:** 

**[10106.26s] English:** And so, you know, we wouldn't want to enter a mode where, you know, there's this theoretical feature that exists in language, but people don't use it in practice.  
**Translation:** 

**[10114.84s] English:** Now, I'll also say one of the other really cool things about this implementation approach is that it can run on GPUs and it can run on accelerators and things like this.  
**Translation:** 

**[10122.46s] English:** And that standard zero-cost exception thing would never work on an accelerator.  
**Translation:** Vocabulary: accelerator: 加速器; accelerators: 加速器; implementation: 实现方式

**[10127.42s] English:** And so this is also part of how Mojo can scale all the way down to, like, little embedded systems and to running on GPUs and things like that.  
**Translation:** 

**[10134.40s] English:** Can you actually say about this?  
**Translation:** 

**[10136.26s] English:** Maybe is there some high-level way to describe the challenge of exceptions and how they work in code during compilation?  
**Translation:** 

**[10146.66s] English:** So it's just this idea of percolating up a thing, an error.  
**Translation:** Vocabulary: compilation: 编译; percolating: 渗透

**[10151.92s] English:** Yeah.  
**Translation:** 

**[10152.56s] English:** Yeah, so the way to think about it is think about a function that doesn't return anything, just as a simple case, right?  
**Translation:** 

**[10158.28s] English:** And so you have function one calls function two, calls function three, calls function four.  
**Translation:** 

**[10164.94s] English:** Along that call stack.  
**Translation:** 

**[10166.26s] English:** There are try blocks, right?  
**Translation:** 

**[10168.14s] English:** And so if you have function one calls function two, function two has a try block, and then within it, it calls function three, right?  
**Translation:** 

**[10174.40s] English:** Well, what happens if function three throws?  
**Translation:** 

**[10177.72s] English:** Well, actually, start simpler.  
**Translation:** 

**[10179.44s] English:** What happens if it returns?  
**Translation:** 

**[10180.68s] English:** Well, if it returns, it's supposed to go back out and continue executing and then fall off the bottom of the try block and keep going and all's good.  
**Translation:** 

**[10186.50s] English:** But if the function throws, you're supposed to exit the current function and then get into the accept clause, right?  
**Translation:** 

**[10194.10s] English:** And then do whatever code's there and then keep falling off.  
**Translation:** 

**[10196.26s] English:** And so the way that a compiler like Mojo works.  
**Translation:** 

**[10200.00s] English:** is that the call to that function, which happens in the accept block, calls a function, and then  
**Translation:** 

**[10206.00s] English:** instead of returning nothing, it actually returns, you know, a variant between nothing and an error.  
**Translation:** 

**[10213.00s] English:** And so if you return normally, fall off the bottom or do return, you return nothing. And if you throw  
**Translation:** 

**[10219.00s] English:** an error, you return the variant that is, I'm an error, right? So when you get to the call,  
**Translation:** 

**[10225.38s] English:** you say, okay, cool, I called a function. Hey, I know locally I'm in a try block, right? And so I  
**Translation:** 

**[10231.12s] English:** call the function, and then I check to see what it returns. Aha, if it's that error thing,  
**Translation:** 

**[10235.60s] English:** jump to the accept block. And that's all done for you behind the scenes. Exactly. And so the  
**Translation:** 

**[10240.56s] English:** compiler does all this for you. And I mean, one of the things, if you dig into how this stuff works  
**Translation:** 

**[10244.64s] English:** in Python, it gets a little bit more complicated because you have finally blocks, which now you  
**Translation:** 

**[10249.78s] English:** need to go into, do some stuff, and then those can also throw and return. Wait, what?  
**Translation:** 

**[10254.72s] English:** Yeah.  
**Translation:** 

**[10255.38s] English:** Oh, and like this stuff matters for compatibility. Like there's-  
**Translation:** 

**[10259.68s] English:** Really? You can nest them?  
**Translation:** Vocabulary: compatibility: 兼容性

**[10260.82s] English:** There's with clauses. And so with clauses are kind of like finally blocks with some special  
**Translation:** 

**[10264.58s] English:** stuff going on. And so there's-  
**Translation:** 

**[10266.18s] English:** Nesting in general, nesting of anything, nesting of functions should be illegal.  
**Translation:** 

**[10271.76s] English:** Well-  
**Translation:** 

**[10272.44s] English:** It just feels like it adds a level of complexity.  
**Translation:** 

**[10275.06s] English:** Lex, I'm merely an implementer. And so this is, again, one of the trade-offs you get when you  
**Translation:** Vocabulary: complexity: 复杂性; implementer: 实施者

**[10281.88s] English:** decide to build a superset is you get to implement a full fidelity.  
**Translation:** 

**[10285.38s] English:** Yeah, I mean, we can complain about the reality of the world and shake our fist, but-  
**Translation:** Vocabulary: fidelity: 保真度

**[10296.18s] English:** It always feels like you shouldn't be allowed to do that, like to declare functions and  
**Translation:** 

**[10300.66s] English:** set functions inside functions.  
**Translation:** 

**[10303.48s] English:** Oh, wait, wait, wait. What happened to Lex, the Lisp guy?  
**Translation:** 

**[10307.62s] English:** No, I understand that. But Lisp is what I used to do in college.  
**Translation:** 

**[10312.20s] English:** So now you've grown up?  
**Translation:** 

**[10313.46s] English:** Yeah.  
**Translation:** 

**[10313.86s] English:** Yeah.  
**Translation:** 

**[10314.30s] English:** Yeah.  
**Translation:** 

**[10314.34s] English:** Yeah.  
**Translation:** 

**[10314.38s] English:** Yeah.  
**Translation:** 

**[10314.44s] English:** Yeah.  
**Translation:** 

**[10314.46s] English:** Yeah.  
**Translation:** 

**[10314.48s] English:** Yeah.  
**Translation:** 

**[10314.50s] English:** Yeah.  
**Translation:** 

**[10314.52s] English:** Yeah.  
**Translation:** 

**[10314.54s] English:** Yeah.  
**Translation:** 

**[10314.56s] English:** Yeah.  
**Translation:** 

**[10314.58s] English:** Yeah.  
**Translation:** 

**[10314.68s] English:** Yeah.  
**Translation:** 

**[10314.70s] English:** Yeah.  
**Translation:** 

**[10314.72s] English:** Yeah.  
**Translation:** 

**[10314.74s] English:** Yeah.  
**Translation:** 

**[10314.76s] English:** Yeah.  
**Translation:** 

**[10314.80s] English:** Yeah.  
**Translation:** 

**[10314.82s] English:** Yeah.  
**Translation:** 

**[10314.84s] English:** Yeah.  
**Translation:** 

**[10314.86s] English:** Yeah.  
**Translation:** 

**[10315.38s] English:** You've all done things in college you're not proud of.  
**Translation:** 

**[10317.18s] English:** No, no, no.  
**Translation:** 

**[10317.76s] English:** Wait a second.  
**Translation:** 

**[10318.56s] English:** Wait a second.  
**Translation:** 

**[10318.90s] English:** I love Lisp.  
**Translation:** 

**[10319.60s] English:** I love Lisp.  
**Translation:** 

**[10320.00s] English:** Okay, yeah, I was going to say, you're afraid of me irritating the whole internet?  
**Translation:** Vocabulary: irritating: 烦扰

**[10323.64s] English:** Yeah, I love this.  
**Translation:** 

**[10325.48s] English:** It worked as a joke in my head and it came out right.  
**Translation:** 

**[10329.26s] English:** So nested functions are, joking aside, actually really great for certain things, right?  
**Translation:** 

**[10333.82s] English:** And so these are also called closures.  
**Translation:** Vocabulary: closures: 闭包

**[10336.34s] English:** Closures are pretty cool, and you can pass callbacks.  
**Translation:** 

**[10338.92s] English:** There's a lot of good patterns.  
**Translation:** Vocabulary: callbacks: 回调函数

**[10339.82s] English:** So speaking of which, I don't think you have nested functions implemented yet in Mojo.  
**Translation:** 

**[10348.44s] English:** We don't have lambda syntax, but we do have nested functions.  
**Translation:** Vocabulary: lambda: 匿名函数; syntax: 语法

**[10352.44s] English:** There's a few things on the roadmap that you have that it would be cool to sort of just fly through  
**Translation:** 

**[10357.24s] English:** because it's interesting to see how many features there are in a language, small and big,  
**Translation:** 

**[10363.38s] English:** that you have to implement.  
**Translation:** 

**[10364.94s] English:** So first of all, there's tuple support.  
**Translation:** Vocabulary: tuple: 元组

**[10367.02s] English:** That has to do with some very specific aspect of it, like the parentheses or not parentheses, that?  
**Translation:** 

**[10372.48s] English:** Yeah, this is just totally a syntactic thing.  
**Translation:** Vocabulary: parentheses: 括号; syntactic: 句法的

**[10374.44s] English:** A syntactic thing.  
**Translation:** 

**[10375.60s] English:** Okay, but it's cool still.  
**Translation:** 

**[10378.44s] English:** So keyword arguments and functions?  
**Translation:** 

**[10381.34s] English:** Yeah, so this is where in Python you can say call a function x equals 4.  
**Translation:** Vocabulary: keyword: 关键字参数

**[10385.68s] English:** Yeah.  
**Translation:** 

**[10386.06s] English:** And x is the name of the argument.  
**Translation:** 

**[10387.64s] English:** That's a nice sort of documenting, self-documenting feature.  
**Translation:** 

**[10391.22s] English:** Yeah, I mean, and again, this isn't rocket science to implement.  
**Translation:** Vocabulary: documenting: 文档记录

**[10393.52s] English:** It's just the laundry list of things.  
**Translation:** 

**[10394.42s] English:** It's just on the list.  
**Translation:** 

**[10396.40s] English:** The bigger features are things like traits.  
**Translation:** 

**[10399.58s] English:** So traits are when you want to define abstract.  
**Translation:** 

**[10402.62s] English:** So when you get into typed languages, you need the ability to write generics.  
**Translation:** 

**[10407.70s] English:** And so you want to say,  
**Translation:** Vocabulary: generics: 泛型编程

**[10408.44s] English:** I'm going to write this function,  
**Translation:** 

**[10409.46s] English:** and now I want to work on all things that are arithmetic-like.  
**Translation:** 

**[10413.28s] English:** Well, what does arithmetic-like mean?  
**Translation:** 

**[10414.94s] English:** Well, arithmetic-like is a categorization of a bunch of types.  
**Translation:** 

**[10419.24s] English:** And so, again, you can define it in many different ways,  
**Translation:** 

**[10421.92s] English:** and I'm not going to go into ring theory or something.  
**Translation:** 

**[10424.70s] English:** But you can say it's arithmetic-like if you can add, subtract, multiply, divide it, for example.  
**Translation:** 

**[10429.94s] English:** And so what you're saying is you're saying there's a set of traits that apply to a broad variety of types.  
**Translation:** Vocabulary: multiply: 乘法; subtract: 减法

**[10437.58s] English:** And so there are...  
**Translation:** 

**[10438.44s] English:** There are all these types of arithmetic-like.  
**Translation:** 

**[10440.00s] English:** all these tensors and floating point integer and like there's this category of types and then i can  
**Translation:** 

**[10445.36s] English:** define on an orthogonal axis algorithms that then work against types that have those properties  
**Translation:** Vocabulary: integer: 整数; orthogonal: 正交

**[10450.64s] English:** and so this is a again it's a widely known thing it's been implemented in swift and rust and many  
**Translation:** 

**[10457.86s] English:** languages so it's not haskell which is where everybody learns learns their tricks from  
**Translation:** Vocabulary: haskell: 哈斯克尔

**[10463.98s] English:** but the uh but we need to implement that and that will enable a new level of expressivity  
**Translation:** 

**[10470.00s] English:** uh so classes yeah classes are big deal it's a big deal still to be implemented  
**Translation:** 

**[10475.64s] English:** um like you said lambda syntax and there's like detailed stuff like whole module import  
**Translation:** 

**[10482.76s] English:** support for top level code and file scope so and then global variables also  
**Translation:** Vocabulary: lambda: 匿名函数; module: 模块; syntax: 语法

**[10489.98s] English:** so being able to have variables outside of a top level well and so this comes back to the  
**Translation:** 

**[10495.66s] English:** where mojo came from and the fact that this is your point one right and so  
**Translation:** 

**[10499.44s] English:** you  
**Translation:** 

**[10500.00s] English:** we're building so modular is building an ai stack right and an ai stack has a bunch of  
**Translation:** Vocabulary: modular: 模块化

**[10505.20s] English:** problems working with hardware and writing high performance kernels and doing this kernel fusion  
**Translation:** 

**[10509.68s] English:** thing i was talking about and getting the most out of the hardware and so we've really prioritized  
**Translation:** Vocabulary: kernel: 内核; kernels: 内核; prioritized: 优先

**[10513.80s] English:** and built mojo to solve modular's problem right now our north star is build out and support all  
**Translation:** 

**[10520.62s] English:** the things and so we're making incredible progress by the way mojo is only like seven months old  
**Translation:** 

**[10524.90s] English:** so that's another interesting thing i mean part of the reason i wanted to mention some of these  
**Translation:** 

**[10529.64s] English:** things is because i think it's a really interesting thing and i think it's a really interesting thing  
**Translation:** 

**[10529.98s] English:** is like there's a lot to to do and it's pretty cool how you just kind of sometimes you take for  
**Translation:** 

**[10536.68s] English:** granted how much there is in a programming language how many cool features you kind of rely on and this  
**Translation:** 

**[10540.60s] English:** is kind of a nice reminder when you lay it as a to-do list yeah and so i mean but also you look  
**Translation:** 

**[10546.08s] English:** into it's it's amazing how much is also there and you take it for granted that a value if you define  
**Translation:** 

**[10553.62s] English:** it it will get destroyed automatically like that little feature itself is actually really complicated  
**Translation:** 

**[10559.20s] English:** to do and so i think it's a really interesting thing to look into and i think it's a really  
**Translation:** 

**[10559.98s] English:** interesting thing to look into and i think it's a really interesting thing to look into and i think  
**Translation:** 

**[10560.00s] English:** and the way the ownership system has to work,  
**Translation:** 

**[10561.92s] English:** and the way that works within Mojo  
**Translation:** 

**[10563.90s] English:** is a huge step forward from what Rust and Swift have done.  
**Translation:** 

**[10566.54s] English:** Can you say that again?  
**Translation:** 

**[10567.38s] English:** When a value, when you define it,  
**Translation:** 

**[10569.26s] English:** it gets destroyed automatically.  
**Translation:** 

**[10570.10s] English:** Yeah, so like say you have a string, right?  
**Translation:** 

**[10572.00s] English:** So you define a string on the stack, okay?  
**Translation:** 

**[10574.04s] English:** Or whatever that means, like in your local function, right?  
**Translation:** 

**[10577.68s] English:** And so you say, like whether it be in a def,  
**Translation:** 

**[10580.76s] English:** and so you just say x equals hello world, right?  
**Translation:** 

**[10584.10s] English:** Well, if your string type requires you to allocate memory,  
**Translation:** 

**[10587.94s] English:** then when it's destroyed, you have to deallocate it.  
**Translation:** Vocabulary: allocate: 分配; deallocate: 释放

**[10590.74s] English:** So in Python and in Mojo,  
**Translation:** 

**[10591.94s] English:** you define that with the del method, right?  
**Translation:** 

**[10594.96s] English:** Where does that get run?  
**Translation:** 

**[10598.72s] English:** Well, it gets run sometime between the last use of the value  
**Translation:** 

**[10603.56s] English:** and the end of the program.  
**Translation:** 

**[10607.32s] English:** Like in this, you now get into garbage collection,  
**Translation:** 

**[10609.56s] English:** you get into like all these long debated,  
**Translation:** 

**[10611.94s] English:** you talk about religions and trade-offs  
**Translation:** 

**[10615.42s] English:** and things like this.  
**Translation:** 

**[10616.26s] English:** This is a hugely,  
**Translation:** 

**[10617.18s] English:** hotly contested,  
**Translation:** 

**[10617.92s] English:** contested world.  
**Translation:** 

**[10619.38s] English:** If you look at C++,  
**Translation:** 

**[10620.70s] English:** the way this works is that if you define a variable  
**Translation:** 

**[10624.14s] English:** or a set of variables within a function,  
**Translation:** 

**[10626.52s] English:** they get destroyed in a last in, first out order.  
**Translation:** 

**[10630.80s] English:** So it's like nesting, okay?  
**Translation:** 

**[10633.58s] English:** This has a huge problem because if you define,  
**Translation:** 

**[10635.70s] English:** you have a big scope,  
**Translation:** 

**[10636.84s] English:** and you define a whole bunch of values at the top,  
**Translation:** 

**[10638.92s] English:** and then you use them,  
**Translation:** 

**[10640.06s] English:** and then you do a whole bunch of code that doesn't use them,  
**Translation:** 

**[10642.64s] English:** they don't get destroyed until the very end of that scope.  
**Translation:** 

**[10645.44s] English:** Right?  
**Translation:** 

**[10646.28s] English:** And so this also destroys tail calls.  
**Translation:** 

**[10647.80s] English:** So good functional programming, right?  
**Translation:** 

**[10650.08s] English:** This, this has a bunch of different impacts on,  
**Translation:** 

**[10652.56s] English:** you know, you talk about reference counting optimizations  
**Translation:** Vocabulary: optimizations: 优化措施

**[10655.14s] English:** and things like this,  
**Translation:** 

**[10655.98s] English:** a bunch of very low level things.  
**Translation:** 

**[10657.90s] English:** And so what Mojo does is it has a different approach  
**Translation:** 

**[10660.58s] English:** on that from any language I'm familiar with,  
**Translation:** 

**[10662.84s] English:** where it destroys them as soon as possible.  
**Translation:** 

**[10666.32s] English:** And by doing that, you get better memory use,  
**Translation:** 

**[10668.38s] English:** you get better predictability,  
**Translation:** 

**[10669.66s] English:** you get tail calls that work,  
**Translation:** 

**[10671.38s] English:** you get a bunch of other things,  
**Translation:** 

**[10672.82s] English:** you get better ownership tracking.  
**Translation:** 

**[10674.24s] English:** There's a bunch of these very simple things that are very fun,  
**Translation:** 

**[10677.42s] English:** fundamental that are already built in  
**Translation:** 

**[10680.00s] English:** or in Mojo today that are the things that nobody talks about generally,  
**Translation:** 

**[10684.02s] English:** but when they don't work right, you find out and you have to complain about.  
**Translation:** 

**[10687.60s] English:** Is it trivial to know what's the soonest possible to delete a thing  
**Translation:** 

**[10692.54s] English:** that's not going to be used again?  
**Translation:** 

**[10694.00s] English:** Yeah, well, I mean, it's generally trivial.  
**Translation:** 

**[10695.98s] English:** It's after the last use of it.  
**Translation:** 

**[10697.42s] English:** So if you define X as a string,  
**Translation:** 

**[10699.34s] English:** and then you have some use of X somewhere in your code.  
**Translation:** 

**[10701.80s] English:** Within that scope, you mean?  
**Translation:** 

**[10703.12s] English:** Within a scope that is accessible?  
**Translation:** 

**[10705.24s] English:** Yeah, exactly.  
**Translation:** 

**[10706.20s] English:** So you can only use something within its scope,  
**Translation:** 

**[10707.88s] English:** and so then it doesn't wait until the end of the scope to delete it.  
**Translation:** 

**[10711.42s] English:** It destroys it after the last use.  
**Translation:** 

**[10714.18s] English:** So there's kind of some very eager machine that's just sitting there and deleting.  
**Translation:** 

**[10718.32s] English:** Yeah, and it's all in the compiler, so it's not at runtime, which is also cool.  
**Translation:** Vocabulary: runtime: 运行时

**[10722.16s] English:** And this is actually non-trivial because you have control flow.  
**Translation:** 

**[10728.30s] English:** And so it gets complicated pretty quickly,  
**Translation:** 

**[10730.16s] English:** and so getting this right was not...  
**Translation:** 

**[10731.70s] English:** Oh, so you have to insert delete in a lot of places.  
**Translation:** Vocabulary: insert: 插入

**[10734.28s] English:** Potentially, yeah, exactly.  
**Translation:** 

**[10735.46s] English:** So the compiler has to reason about this,  
**Translation:** 

**[10737.30s] English:** and this is where...  
**Translation:** 

**[10737.86s] English:** Again, it's experience building languages and not getting this right.  
**Translation:** 

**[10741.18s] English:** So again, you get another chance to do it,  
**Translation:** 

**[10742.94s] English:** and you get basic things like this, right?  
**Translation:** 

**[10745.52s] English:** But it's extremely powerful when you do that.  
**Translation:** 

**[10748.20s] English:** And so there's a bunch of things like that that kind of combine together.  
**Translation:** 

**[10752.20s] English:** And this comes back to the...  
**Translation:** 

**[10753.78s] English:** You get a chance to do it the right way, do it the right way,  
**Translation:** 

**[10756.16s] English:** and make sure that every brick you put down is really good,  
**Translation:** 

**[10758.54s] English:** so that when you put more bricks on top of it,  
**Translation:** 

**[10760.68s] English:** they stack up to something that's beautiful.  
**Translation:** 

**[10762.16s] English:** Well, there's also...  
**Translation:** 

**[10764.16s] English:** Like, how many...  
**Translation:** 

**[10765.16s] English:** design discussions do there have to be about particular details,  
**Translation:** 

**[10770.58s] English:** like implementation of particular small features?  
**Translation:** 

**[10772.86s] English:** Because the features that seem small,  
**Translation:** Vocabulary: implementation: 实施

**[10776.54s] English:** I bet some of them might be, like,  
**Translation:** 

**[10779.52s] English:** really...  
**Translation:** 

**[10780.72s] English:** require really big design decisions.  
**Translation:** 

**[10782.78s] English:** Yeah.  
**Translation:** 

**[10783.50s] English:** Well, so, I mean, let me give you another example of this.  
**Translation:** 

**[10785.74s] English:** Python has a feature called async await.  
**Translation:** Vocabulary: async: 异步等待

**[10787.88s] English:** So it's a new feature.  
**Translation:** 

**[10790.28s] English:** I mean, in the long arc of Python history,  
**Translation:** 

**[10792.86s] English:** it's a relatively new feature, right?  
**Translation:** 

**[10795.16s] English:** That allows way more expressive asynchronous programming.  
**Translation:** Vocabulary: asynchronous: 异步的; expressive: 富有表现力的

**[10799.20s] English:** Okay.  
**Translation:** 

**[10799.32s] English:** Okay.  
**Translation:** 

**[10800.00s] English:** Again, this is a, Python's a beautiful thing,  
**Translation:** 

**[10802.58s] English:** and they did things that are great for Mojo  
**Translation:** 

**[10804.30s] English:** for completely different reasons.  
**Translation:** 

**[10806.70s] English:** The reason that async await got added to Python,  
**Translation:** 

**[10809.68s] English:** as far as I know, is because Python doesn't support threads.  
**Translation:** 

**[10813.04s] English:** Okay?  
**Translation:** 

**[10813.98s] English:** And so Python doesn't support threads,  
**Translation:** 

**[10816.48s] English:** but you want to work with networking  
**Translation:** 

**[10818.54s] English:** and other things like that that can block.  
**Translation:** 

**[10820.54s] English:** I mean, Python does support threads.  
**Translation:** 

**[10821.88s] English:** It's just not its strength.  
**Translation:** 

**[10822.88s] English:** And so they added this feature called async await.  
**Translation:** 

**[10827.74s] English:** It's also seen in other languages,  
**Translation:** 

**[10828.96s] English:** like Swift and JavaScript and many other places as well.  
**Translation:** 

**[10833.60s] English:** Async await in Mojo is amazing  
**Translation:** 

**[10835.06s] English:** because we have a high-performance heterogeneous compute runtime  
**Translation:** Vocabulary: heterogeneous: 异构的

**[10837.80s] English:** underneath the covers that then allows non-blocking I.O.  
**Translation:** 

**[10842.62s] English:** so you get full use of your accelerator.  
**Translation:** 

**[10845.52s] English:** That's huge, it turns out.  
**Translation:** 

**[10847.14s] English:** It's actually really an important part of fully utilizing a machine.  
**Translation:** Vocabulary: utilizing: 充分利用

**[10850.64s] English:** You talk about design discussions.  
**Translation:** 

**[10852.52s] English:** That took a lot of discussions, right?  
**Translation:** 

**[10854.66s] English:** And it probably will require more iteration.  
**Translation:** 

**[10856.86s] English:** And so my philosophy with Mojo  
**Translation:** Vocabulary: iteration: 迭代

**[10858.76s] English:** is that we have a small team of really good people  
**Translation:** 

**[10861.20s] English:** that are pushing forward,  
**Translation:** 

**[10862.34s] English:** and they're very good at the extremely deep,  
**Translation:** 

**[10865.26s] English:** knowing how the compiler and runtime  
**Translation:** Vocabulary: runtime: 运行时环境

**[10866.72s] English:** and all the low-level stuff works together.  
**Translation:** 

**[10870.24s] English:** But they're not perfect.  
**Translation:** 

**[10871.44s] English:** Same thing as the Swift team, right?  
**Translation:** 

**[10873.04s] English:** And this is where one of the reasons we released Mojo much earlier  
**Translation:** 

**[10876.44s] English:** is so we can get feedback.  
**Translation:** 

**[10878.00s] English:** And we've already renamed a keyword  
**Translation:** Vocabulary: keyword: 关键词; renamed: 重命名

**[10879.94s] English:** due to community feedback.  
**Translation:** 

**[10882.24s] English:** Which one?  
**Translation:** 

**[10883.70s] English:** We used an ampersand, and now it's named in-out.  
**Translation:** 

**[10886.70s] English:** We're not renaming existing Python keywords,  
**Translation:** Vocabulary: ampersand: 与号; keywords: 关键字; renaming: 重命名

**[10888.76s] English:** because that breaks compatibility, right?  
**Translation:** 

**[10890.36s] English:** We're renaming things we're adding  
**Translation:** Vocabulary: compatibility: 兼容性

**[10891.96s] English:** and making sure that they are designed well,  
**Translation:** 

**[10895.16s] English:** we get usage experience,  
**Translation:** 

**[10896.64s] English:** we iterate and work with the community,  
**Translation:** 

**[10897.84s] English:** because, again, if you scale something really fast  
**Translation:** 

**[10900.50s] English:** and everybody writes all their code  
**Translation:** 

**[10901.38s] English:** and they start using it in production,  
**Translation:** 

**[10902.80s] English:** then it's impossible to change.  
**Translation:** 

**[10904.66s] English:** And so you want to learn from people,  
**Translation:** 

**[10906.20s] English:** you want to iterate and work on that early on,  
**Translation:** 

**[10908.14s] English:** and this is where design discussions,  
**Translation:** 

**[10910.02s] English:** it's actually quite important.  
**Translation:** 

**[10911.58s] English:** Could you incorporate an emoji into the language,  
**Translation:** Vocabulary: incorporate: 吸收

**[10915.08s] English:** into the main language?  
**Translation:** 

**[10916.44s] English:** Good.  
**Translation:** 

**[10917.64s] English:** Do you have a favorite?  
**Translation:** 

**[10918.96s] English:** Go ahead, Rowan.  
**Translation:** 

**[10919.60s] English:** Well, I really...  
**Translation:** 

**[10920.00s] English:** really like uh in terms of humor like uh rawful whatever rolling on the floor laughing so that  
**Translation:** 

**[10926.70s] English:** could be like uh what would that be the use case for that like an exception throw an exception of  
**Translation:** 

**[10931.92s] English:** some sort i don't know you should totally file a feature request uh or maybe a hard one it has to  
**Translation:** 

**[10938.24s] English:** be a hard one uh people have told me that i'm insane so this is this is this is i i'm liking  
**Translation:** 

**[10943.16s] English:** this i'm gonna i'm gonna use the viral nature of the internet to to actually get this to get this  
**Translation:** Vocabulary: viral: 病毒式的

**[10949.24s] English:** passed i mean it's funny you come back to the flame emoji file extension right the uh um you  
**Translation:** 

**[10955.42s] English:** know we have the option to use the flame emoji which just even that concept cause for example  
**Translation:** 

**[10961.08s] English:** the people at github say now i've seen everything you know like yeah there's something uh it kind of  
**Translation:** 

**[10967.68s] English:** it's reinvigorating it's like uh it's like oh that's possible that's really cool that  
**Translation:** Vocabulary: reinvigorating: 振奋人心

**[10973.18s] English:** for some reason that makes everything else really exciting the world is ready for this stuff right  
**Translation:** 

**[10978.16s] English:** and so you know when we have  
**Translation:** 

**[10979.20s] English:** a  
**Translation:** 

**[10979.24s] English:** package manager we'll clearly have to innovate by having the compiled package thing be the little  
**Translation:** Vocabulary: compiled: 编译后的; innovate: 创新

**[10983.80s] English:** box with the bow on it right i mean it has to be done it has to be done is there some stuff on the  
**Translation:** 

**[10990.80s] English:** roadmap that you're particularly stressed about or excited about that you're thinking about a lot  
**Translation:** 

**[10995.68s] English:** i mean as a today snapshot which will be obsolete tomorrow uh the lifetime stuff is really exciting  
**Translation:** 

**[11001.46s] English:** and so lifetimes give you safe references to memory without dangling pointers and so this  
**Translation:** Vocabulary: dangling: 悬空的; lifetimes: 生命周期; obsolete: 过时的; snapshot: 快照

**[11008.12s] English:** has been done in languages  
**Translation:** 

**[11009.20s] English:** like rust before and so we have a new approach which is really cool i'm very excited about that  
**Translation:** 

**[11012.72s] English:** that'll be out to the community very soon um the traits feature is really a big deal and so that's  
**Translation:** 

**[11019.42s] English:** blocking a lot of api design and so there's that i think that's really exciting um a lot of it is  
**Translation:** 

**[11025.96s] English:** these kind of table stakes features um one of the things that is again also lessons learned with  
**Translation:** 

**[11031.78s] English:** swift uh is that uh programmers in general like to add syntactic sugar  
**Translation:** Vocabulary: programmers: 程序员; syntactic: 语法糖

**[11037.64s] English:** mm-hmm  
**Translation:** 

**[11038.32s] English:** and so that's the thing that's really exciting and so we have a new approach which is really cool and  
**Translation:** 

**[11039.16s] English:** So it's like, oh.  
**Translation:** 

**[11040.00s] English:** well, this annoying thing, like in Python,  
**Translation:** 

**[11042.72s] English:** you have to spell it under bar, under bar, add.  
**Translation:** 

**[11045.06s] English:** Why can't I just use plus?  
**Translation:** 

**[11047.22s] English:** Def plus, come on.  
**Translation:** 

**[11048.34s] English:** Why can't I just do that, right?  
**Translation:** 

**[11049.40s] English:** And so, trivial bit of syntactic sugar,  
**Translation:** 

**[11051.48s] English:** it makes sense, it's beautiful, it's obvious.  
**Translation:** 

**[11053.82s] English:** We're trying not to do that.  
**Translation:** 

**[11056.26s] English:** And so, for two different reasons,  
**Translation:** 

**[11058.90s] English:** one of which is that, again, lesson learned with Swift.  
**Translation:** 

**[11061.54s] English:** Swift has a lot of syntactic sugar,  
**Translation:** 

**[11064.50s] English:** which may be a good thing, may be not, I don't know.  
**Translation:** 

**[11067.66s] English:** But because it's such an easy and addictive thing to do,  
**Translation:** Vocabulary: addictive: 上瘾的

**[11071.90s] English:** sugar, like make sure blood get crazy, right?  
**Translation:** 

**[11075.58s] English:** Like the community will really dig into that  
**Translation:** 

**[11077.62s] English:** and want to do a lot of that.  
**Translation:** 

**[11078.68s] English:** And I think it's very distracting  
**Translation:** Vocabulary: distracting: 分散注意力的

**[11079.82s] English:** from building the core abstractions.  
**Translation:** 

**[11082.00s] English:** The second is we want to be a good member  
**Translation:** Vocabulary: abstractions: 抽象概念

**[11083.34s] English:** of the Python community, right?  
**Translation:** 

**[11086.72s] English:** And so, we want to work with the broader Python community.  
**Translation:** 

**[11090.02s] English:** And yeah, we're pushing forward  
**Translation:** 

**[11091.80s] English:** a bunch of systems programming features  
**Translation:** 

**[11093.40s] English:** and we need to build them out to understand them.  
**Translation:** 

**[11095.08s] English:** But once we get a long ways forward,  
**Translation:** 

**[11097.42s] English:** I want to make sure that we go back  
**Translation:** 

**[11098.80s] English:** to the Python community and say,  
**Translation:** 

**[11099.98s] English:** okay, let's do some design reviews.  
**Translation:** 

**[11101.28s] English:** Let's actually talk about this stuff.  
**Translation:** 

**[11102.42s] English:** Let's figure out how we want this stuff  
**Translation:** 

**[11103.94s] English:** all to work together.  
**Translation:** 

**[11105.00s] English:** And syntactic sugar just makes all that more complicated.  
**Translation:** 

**[11109.04s] English:** And yeah, list comprehensions are yet to be implemented.  
**Translation:** Vocabulary: comprehensions: 列表推导式

**[11112.78s] English:** And my favorite, I mean, dictionaries.  
**Translation:** 

**[11116.66s] English:** Yeah, there's some basic stuff.  
**Translation:** 

**[11118.38s] English:** 0.1.  
**Translation:** 

**[11119.54s] English:** 0.1.  
**Translation:** 

**[11120.64s] English:** Yeah, but nonetheless,  
**Translation:** 

**[11121.46s] English:** it's actually still quite interesting and useful.  
**Translation:** 

**[11123.40s] English:** As you mentioned, modular is very new.  
**Translation:** 

**[11127.42s] English:** It's a relatively small team  
**Translation:** Vocabulary: modular: 模块化的

**[11130.22s] English:** that's building up this gigantic stack,  
**Translation:** 

**[11134.90s] English:** this incredible stack that's going to perhaps define  
**Translation:** Vocabulary: gigantic: 巨大的

**[11137.98s] English:** the future of development of our AI overlords.  
**Translation:** 

**[11143.42s] English:** We just hope it will be useful.  
**Translation:** 

**[11146.40s] English:** As do all of us.  
**Translation:** 

**[11148.76s] English:** So, what have you learned  
**Translation:** 

**[11150.86s] English:** from this process of building up a team?  
**Translation:** 

**[11154.02s] English:** Maybe one question is, how do you hire?  
**Translation:** 

**[11156.84s] English:** Yeah.  
**Translation:** 

**[11157.42s] English:** Great programmers, great...  
**Translation:** Vocabulary: programmers: 程序员

**[11160.00s] English:** people that operate in this compiler hardware machine learning software interface design space  
**Translation:** 

**[11170.52s] English:** yeah and maybe are a little bit fluid yeah what they can do so okay so language design too so  
**Translation:** Vocabulary: interface: 接口

**[11176.54s] English:** building a company is just as interesting in different ways as building a language like  
**Translation:** 

**[11182.12s] English:** different skill sets different things but super interesting and i've built a lot of teams a lot  
**Translation:** 

**[11186.04s] English:** of different places um if you zoom in from the big problem into recruiting well so here's our  
**Translation:** 

**[11192.40s] English:** problem okay i'll just i'll be very straightforward about this we started modular with a lot of  
**Translation:** Vocabulary: recruiting: 招聘; straightforward: 直截了当

**[11198.00s] English:** conviction about we understand the problems we understand the customer pain points we need to  
**Translation:** 

**[11202.64s] English:** work backwards from the suffering in the industry and if we solve those problems we think it'll be  
**Translation:** Vocabulary: backwards: 逆向

**[11207.30s] English:** useful for people but the problem is is that the people we need to hire as you say are all these  
**Translation:** 

**[11212.82s] English:** super specialized people that have jobs at big tech  
**Translation:** 

**[11216.02s] English:** big tech worlds right and you know we i don't think we have um product market fit in the way  
**Translation:** 

**[11222.90s] English:** that a normal startup does we don't have product market fit challenges because right now everybody's  
**Translation:** 

**[11228.92s] English:** using ai and so many of them are suffering and they want help and so again we started with strong  
**Translation:** 

**[11233.52s] English:** conviction now again you have to hire and recruit the best and the best all have jobs and so what  
**Translation:** 

**[11239.32s] English:** we've done is we said okay well let's build an amazing culture start with that that's usually  
**Translation:** 

**[11244.46s] English:** not something a company starts with  
**Translation:** 

**[11246.02s] English:** usually you hire a bunch of people and then it people start fighting and it turns into a gigantic  
**Translation:** 

**[11250.34s] English:** mess and then you try to figure out how to improve your culture later my co-founder tim in particular  
**Translation:** 

**[11255.28s] English:** is super passionate about making sure that that's right and we've spent a lot of time early on to  
**Translation:** 

**[11260.18s] English:** make sure that we can scale can you comment sorry before we get to the second yeah what makes for a  
**Translation:** 

**[11264.74s] English:** good culture um so i mean there's many different cultures and i have learned many things from  
**Translation:** 

**[11270.00s] English:** several very unique almost famously unique cultures and some of them i  
**Translation:** 

**[11276.02s] English:** learned what to do and some of them i learned what not to do okay and so  
**Translation:** 

**[11280.00s] English:** So we want an inclusive culture.  
**Translation:** Vocabulary: inclusive: 包容的

**[11284.00s] English:** I believe in amazing people working together.  
**Translation:** 

**[11289.06s] English:** And so I've seen cultures where you have amazing people  
**Translation:** 

**[11291.46s] English:** and they're fighting each other.  
**Translation:** 

**[11293.24s] English:** I see amazing people and they're told what to do.  
**Translation:** 

**[11296.58s] English:** Like, thou shalt line up and do what I say.  
**Translation:** 

**[11298.80s] English:** It doesn't matter if it's the right thing.  
**Translation:** Vocabulary: shalt: 必须

**[11300.08s] English:** Do it, right?  
**Translation:** 

**[11301.58s] English:** And neither of these is the...  
**Translation:** 

**[11303.10s] English:** And I've seen people that have no direction.  
**Translation:** 

**[11304.72s] English:** They're just kind of floating in different places.  
**Translation:** 

**[11306.96s] English:** And they want to be amazing.  
**Translation:** 

**[11308.34s] English:** They just don't know how.  
**Translation:** 

**[11309.00s] English:** And so a lot of it starts with have a clear vision, right?  
**Translation:** 

**[11313.12s] English:** And so we have a clear vision of what we're doing.  
**Translation:** 

**[11315.28s] English:** And so I kind of grew up at Apple in my engineering life, right?  
**Translation:** 

**[11319.86s] English:** And so a lot of the Apple DNA rubbed off on me.  
**Translation:** 

**[11323.36s] English:** My co-founder, Tim, also is like a strong product guy.  
**Translation:** 

**[11326.10s] English:** And so what we learned is, you know,  
**Translation:** 

**[11328.22s] English:** I was taught at Apple that you don't work from building cool technology.  
**Translation:** 

**[11332.08s] English:** You don't work from, like, come up with a cool product  
**Translation:** 

**[11334.64s] English:** and think about the features you'll have  
**Translation:** 

**[11336.02s] English:** and the big checkboxes and stuff like this.  
**Translation:** Vocabulary: checkboxes: 复选框

**[11337.68s] English:** Because if you go talk to customers,  
**Translation:** 

**[11339.48s] English:** they don't actually care about your product.  
**Translation:** 

**[11341.62s] English:** They don't care about your technology.  
**Translation:** 

**[11343.20s] English:** What they care about is their problems, right?  
**Translation:** 

**[11346.60s] English:** And if your product can help solve their problems,  
**Translation:** 

**[11349.38s] English:** well, hey, they might be interested in that, right?  
**Translation:** 

**[11351.82s] English:** And so if you speak to them about their problems,  
**Translation:** 

**[11353.26s] English:** if you understand and you have compassion,  
**Translation:** Vocabulary: compassion: 同情

**[11354.72s] English:** you understand what people are working with,  
**Translation:** 

**[11356.94s] English:** then you can work backwards to building an amazing product.  
**Translation:** Vocabulary: backwards: 逆向

**[11359.36s] English:** So the vision starts by defining the problem.  
**Translation:** 

**[11361.78s] English:** And then you can work backwards in solving technology.  
**Translation:** 

**[11364.24s] English:** And at Apple, like, it's, I think, pretty famously said that, you know,  
**Translation:** 

**[11367.48s] English:** for every, you know, there's 100 no's for every yes.  
**Translation:** 

**[11372.72s] English:** I would refine that to say that there's 100 not yet's for every yes.  
**Translation:** 

**[11376.50s] English:** But famously, if you go back to the iPhone, for example, right?  
**Translation:** 

**[11379.86s] English:** The iPhone 1, I mean, many people laughed at it  
**Translation:** 

**[11382.54s] English:** because it didn't have 3G.  
**Translation:** 

**[11384.14s] English:** It didn't have copy and paste, right?  
**Translation:** 

**[11387.12s] English:** And then a year later, okay, finally it has 3G,  
**Translation:** 

**[11390.38s] English:** but it still doesn't have copy and paste.  
**Translation:** 

**[11392.02s] English:** It's a joke.  
**Translation:** 

**[11392.50s] English:** Nobody will ever use this product, blah, blah, blah, blah, blah, blah, blah, right?  
**Translation:** 

**[11395.54s] English:** Well, year three, it had...  
**Translation:** 

**[11397.48s] English:** Copy and paste, and people stopped talking about it, right?  
**Translation:** 

**[11400.00s] English:** And so being laser-focused and having conviction and understanding what the core problems are  
**Translation:** 

**[11406.24s] English:** and giving the team the space to be able to build the right tech is really important.  
**Translation:** 

**[11411.78s] English:** Also, I mean, you come back to recruiting, you have to pay well, right?  
**Translation:** Vocabulary: recruiting: 招聘

**[11415.98s] English:** So we have to pay industry-leading salaries and have good benefits and things like this.  
**Translation:** 

**[11419.20s] English:** That's a big piece.  
**Translation:** Vocabulary: salaries: 薪酬水平

**[11420.54s] English:** We're a remote-first company.  
**Translation:** 

**[11422.40s] English:** And so we have to – so remote-first has a very strong set of pros and cons.  
**Translation:** 

**[11430.88s] English:** On the one hand, you can hire people from wherever they are, and you can attract amazing talent  
**Translation:** 

**[11435.82s] English:** even if they live in strange places or unusual places.  
**Translation:** 

**[11439.08s] English:** On the other hand, you have time zones.  
**Translation:** 

**[11442.04s] English:** On the other hand, you have, like, everybody on the Internet will fight if they don't understand each other.  
**Translation:** 

**[11447.46s] English:** And so we've had to learn how to, like, have a system where we actually fly people in  
**Translation:** 

**[11451.46s] English:** and we get the whole thing.  
**Translation:** 

**[11452.40s] English:** We build the whole company together periodically, and then we get work groups together,  
**Translation:** 

**[11455.10s] English:** and we plan and execute together.  
**Translation:** 

**[11456.80s] English:** And there's, like, an intimacy to the in-person brainstorming that I guess you lose.  
**Translation:** 

**[11461.78s] English:** But maybe you don't.  
**Translation:** Vocabulary: brainstorming: 头脑风暴; intimacy: 亲密氛围

**[11462.90s] English:** Maybe if you get to know each other well and you trust each other, maybe you can do that.  
**Translation:** 

**[11466.48s] English:** Well, so when the pandemic first hit, I mean, I'm curious about your experience too.  
**Translation:** Vocabulary: pandemic: 全球大流行

**[11469.98s] English:** The first thing I missed was having whiteboards.  
**Translation:** 

**[11472.70s] English:** Yeah.  
**Translation:** Vocabulary: whiteboards: 白板

**[11473.50s] English:** Right?  
**Translation:** 

**[11473.76s] English:** Those design discussions where, like, I can high-intensity work through things, get things done,  
**Translation:** 

**[11479.90s] English:** work through the problem of the day, understand where you're on.  
**Translation:** 

**[11481.80s] English:** And figure out and solve the problem and move forward.  
**Translation:** 

**[11484.60s] English:** Yeah.  
**Translation:** 

**[11486.10s] English:** But we've figured out ways to work around that now with, you know, all these screen sharing  
**Translation:** 

**[11491.68s] English:** and other things like that that we do.  
**Translation:** 

**[11493.08s] English:** The thing I miss now is sitting down at a lunch table with the team.  
**Translation:** 

**[11496.92s] English:** Yeah.  
**Translation:** 

**[11497.60s] English:** The spontaneous things, like the coffee bar things and the bumping into each other  
**Translation:** Vocabulary: spontaneous: 随机发生

**[11504.04s] English:** and getting to know people outside of the transactional solve-a-problem-over-Zoom thing.  
**Translation:** 

**[11509.26s] English:** And I think there's just a lot of stuff that...  
**Translation:** 

**[11511.80s] English:** I'm not an expert at this.  
**Translation:** 

**[11513.76s] English:** I don't know who is.  
**Translation:** 

**[11515.02s] English:** Hopefully, there's some people.  
**Translation:** 

**[11516.34s] English:** But there's stuff that somehow is missing on Zoom.  
**Translation:** 

**[11519.56s] English:** Even...  
**Translation:** 

**[11520.00s] English:** With the whiteboard, if you look at that, if you have a room with one person at the whiteboard and there's, like, three other people at a table, there's a – first of all, there's a social aspect to that where you're just shooting the shit a little bit, almost like –  
**Translation:** 

**[11535.66s] English:** Yeah, as people are just kind of coming in and –  
**Translation:** 

**[11537.58s] English:** Yeah, that, but also while, like, it's a breakout discussion that happens for, like, seconds at a time, maybe an inside joke, or it's, like, this interesting dynamic that happens that Zoom –  
**Translation:** Vocabulary: breakout: 分组讨论

**[11550.38s] English:** And you're bonding, yeah.  
**Translation:** 

**[11551.38s] English:** You're bonding, you're bonding, but through that bonding, you get the excitement.  
**Translation:** 

**[11555.82s] English:** There's certain ideas that are, like, complete bullshit, and you'll see that in the faces of others that you won't see necessarily on Zoom.  
**Translation:** 

**[11564.30s] English:** Like, something – it feels like that should be possible.  
**Translation:** Vocabulary: bullshit: 胡说八道

**[11567.58s] English:** It should be possible to do without being in person.  
**Translation:** 

**[11570.78s] English:** Well, I mean, being in person is a very different thing.  
**Translation:** 

**[11573.36s] English:** I don't –  
**Translation:** 

**[11574.02s] English:** It's worth it, but you can't always do it.  
**Translation:** 

**[11576.44s] English:** And so, again, we're still learning, and we're all still learning as, like, humanity with this new reality, right?  
**Translation:** 

**[11582.94s] English:** But what we found is that getting people together, whether it be a team or the whole company or whatever, is worth the expense because people work together and are happier after that.  
**Translation:** 

**[11593.18s] English:** Like, it just – like, there's a massive period of time where you, like, go out and things.  
**Translation:** 

**[11597.60s] English:** You start getting afraid, pull people together, and then you realize that we're all working together.  
**Translation:** 

**[11602.02s] English:** We see things the same way.  
**Translation:** 

**[11603.04s] English:** We work through the disagreement or the misunderstanding.  
**Translation:** 

**[11604.98s] English:** We're talking across each other, and then you work much better together.  
**Translation:** 

**[11608.18s] English:** And so things like that, I think, are really quite important.  
**Translation:** 

**[11610.74s] English:** What about people that are kind of specialized in very different aspects of the stack working together?  
**Translation:** 

**[11616.36s] English:** What are some interesting challenges there?  
**Translation:** 

**[11618.32s] English:** Yeah, well, so, I mean, there's lots of interesting people, as you can tell.  
**Translation:** 

**[11621.02s] English:** I'm, you know, hard to deal with, too.  
**Translation:** 

**[11624.36s] English:** You're one of the most lovable people.  
**Translation:** 

**[11627.58s] English:** So one of the – so there's different philosophies in building teams.  
**Translation:** Vocabulary: lovable: 讨人喜欢; philosophies: 哲学

**[11631.64s] English:** For me – and so some people say, hire 10x programmers, and that's the only thing – whatever that means, right?  
**Translation:** 

**[11638.78s] English:** What I believe in is build –  
**Translation:** Vocabulary: programmers: 程序员

**[11640.00s] English:** building well-balanced teams teams that have people that are different in them like if you  
**Translation:** 

**[11645.72s] English:** have all generals and no troops or all troops and no generals or you have all people that think in  
**Translation:** 

**[11651.90s] English:** one way and not the other way what you get is you get a very biased and skewed and weird situation  
**Translation:** 

**[11656.28s] English:** where people end up being unhappy and so what i like to do is i like to build teams of people  
**Translation:** Vocabulary: skewed: 歪曲的

**[11660.66s] English:** where they're not all the same you know we do have teams and they're focused on like runtime  
**Translation:** 

**[11665.60s] English:** or compiler gpu or accelerator or whatever the the speciality is but people bring a different  
**Translation:** Vocabulary: accelerator: 加速器; runtime: 运行时

**[11670.54s] English:** take and have a different perspective and i look for people that complement each other  
**Translation:** 

**[11674.62s] English:** and particularly if you look at leadership teams and things like this you don't want  
**Translation:** 

**[11678.52s] English:** everybody thinking the same way you want people bringing different perspectives and experiences  
**Translation:** 

**[11683.22s] English:** and so i think that's really important that's team but what about building a company as ambitious  
**Translation:** Vocabulary: perspectives: 观点

**[11688.40s] English:** as modular so what uh some interesting questions there oh i mean so many like so um one of the  
**Translation:** 

**[11695.44s] English:** things that i've been doing is i've been doing a lot of things that i've been doing for a long  
**Translation:** Vocabulary: modular: 模块化的

**[11695.58s] English:** time and one of the things i love about okay so modular is the first company i built from scratch  
**Translation:** 

**[11699.18s] English:** um uh one of the first things that was profound was i'm not cleaning up somebody else's mess  
**Translation:** Vocabulary: profound: 深刻

**[11707.02s] English:** right and so if you look at that's liberating to some degree it's super liberating and um  
**Translation:** 

**[11712.76s] English:** and also many of the projects i've built in the past have not been core to the product of the  
**Translation:** Vocabulary: liberating: 解放性的

**[11718.56s] English:** company swift is not apple's product right uh mlir is not google's product is not apple's product  
**Translation:** 

**[11725.58s] English:** is not google's revenue machine or whatever right it's not it's it's important but it's like working  
**Translation:** 

**[11731.10s] English:** on the accounting software for you know the the retail giant or something right it's it's it's  
**Translation:** 

**[11736.76s] English:** it's like enabling infrastructure and technology and so at modular the the tech we're building is  
**Translation:** 

**[11742.48s] English:** here to solve people's problems like it is directly the thing that we're giving to people  
**Translation:** 

**[11747.10s] English:** and so this is a really big difference and what it means for me as a leader but also  
**Translation:** 

**[11751.82s] English:** for many of our engineers is they're working on the thing that matters  
**Translation:** 

**[11755.58s] English:** and that's actually pretty i mean again for for compiler people and things like that that's that's  
**Translation:** 

**[11760.00s] English:** usually not the case right and so that's that's also pretty exciting and and quite nice but the  
**Translation:** 

**[11765.84s] English:** um one of the ways that this manifests is it makes it easier to make decisions  
**Translation:** Vocabulary: manifests: 表现

**[11771.20s] English:** and so one of the challenges i've had in other worlds is it's like okay well  
**Translation:** 

**[11775.44s] English:** community matters somehow for the goodness of the world like or open source matters theoretically  
**Translation:** Vocabulary: theoretically: 理论上

**[11781.68s] English:** but i don't want to pay for a t-shirt yeah right or some swag like well t-shirts cost  
**Translation:** 

**[11787.84s] English:** 10 bucks each you can have 100 t-shirts for a thousand dollars to a mega corp a thousand dollars  
**Translation:** Vocabulary: bucks: 美元

**[11792.64s] English:** is uncountably can't count that low right but justifying it and getting a t-shirt by the way  
**Translation:** 

**[11799.52s] English:** if you'd like a t-shirt i can give you a t-shirt well i would 100 percent like a t-shirt are you  
**Translation:** Vocabulary: justifying: 辩解

**[11804.56s] English:** joking you can have a fire emoji t-shirt i will i will treasure this i will pass it down to my  
**Translation:** 

**[11812.32s] English:** grandchildren and so you know it's very liberating to be able to decide i think that should have a  
**Translation:** 

**[11816.80s] English:** t-shirt  
**Translation:** 

**[11818.80s] English:** right and it becomes very simple because i like lex this this uh this is awesome um so  
**Translation:** 

**[11829.68s] English:** i have to ask you about the one of the interesting developments with large language models  
**Translation:** 

**[11838.00s] English:** is that they're able to generate code uh recently really well yes to a degree that uh maybe a  
**Translation:** 

**[11848.80s] English:** i don't know if you understand but i have i struggle to understand because it  
**Translation:** 

**[11853.12s] English:** it forces me to ask questions about the nature of programming of the nature of thought because  
**Translation:** 

**[11860.24s] English:** the uh language models are able to predict the kind of code i was about to write so well  
**Translation:** 

**[11865.12s] English:** yep that it makes me wonder like how unique my brain is and where the valuable  
**Translation:** 

**[11869.60s] English:** ideas actually come from like how much do i contribute in terms of uh ingenuity innovation  
**Translation:** 

**[11877.12s] English:** to code  
**Translation:** Vocabulary: ingenuity: 创造力

**[11877.84s] English:** i write or design and that kind of  
**Translation:** 

**[11880.00s] English:** stuff um when you stand on the shoulders of giants are you really doing anything and what llms are  
**Translation:** 

**[11885.40s] English:** helping you do is they help you stand on the shoulders of giants in your program  
**Translation:** 

**[11889.90s] English:** there's mistakes they're interesting that you learn from but i just it would love to get your  
**Translation:** 

**[11895.28s] English:** opinion first high level yeah of what you think about uh this impact of large language models  
**Translation:** 

**[11901.30s] English:** when they do program synthesis when they generate code yeah well so um i don't know where it all  
**Translation:** Vocabulary: synthesis: 合成

**[11907.98s] English:** goes yeah um i'm an optimist and i'm a human optimist right i think that um things i've seen  
**Translation:** 

**[11914.66s] English:** are that a lot of the llms are really good at crushing leak code projects and they can reverse  
**Translation:** Vocabulary: optimist: 乐观主义者

**[11919.80s] English:** the link list like crazy um well it turns out there's a lot of instances of that on the internet  
**Translation:** 

**[11925.18s] English:** and it's a pretty stock thing and so if you want to see standard questions answered llms can  
**Translation:** 

**[11931.06s] English:** memorize all the answers and that can be amazing and also they do generalize out from that and so  
**Translation:** 

**[11935.30s] English:** there's good work on that but um  
**Translation:** Vocabulary: generalize: 归纳; memorize: 记忆

**[11937.98s] English:** but i think that if you in my experience building things building something like you talk about  
**Translation:** 

**[11942.94s] English:** mojo or you talk about these things you talk about building an applied solution to a problem it's  
**Translation:** 

**[11948.12s] English:** also about working with people it's about understanding the problem what is the product  
**Translation:** 

**[11952.06s] English:** that you want to build what are the use case what are the customers you can't just go survey all the  
**Translation:** 

**[11956.34s] English:** customers because they'll tell you that they want a faster horse maybe they need a car right and so  
**Translation:** 

**[11961.78s] English:** a lot of it comes into um you know i don't feel like we have to compete with llms i think they'll  
**Translation:** 

**[11966.86s] English:** help automate a ton of the problems that we're dealing with and i think that's a really good  
**Translation:** 

**[11967.98s] English:** thing to do and i think that's a really good thing to do and i think that's a really good thing to do  
**Translation:** Vocabulary: automate: 自动化

**[11968.04s] English:** mechanical stuff out of the way and just like you know i think we all try to scale through  
**Translation:** 

**[11973.00s] English:** delegation and things like this delegating wrote things to an llm i think is an extremely valuable  
**Translation:** Vocabulary: delegating: 委托任务

**[11978.16s] English:** and approach that will help us all scale and be more productive but i think it's a it's a  
**Translation:** 

**[11983.78s] English:** fascinating companion but i'd say i don't think that means that we're going to be done with coding  
**Translation:** 

**[11987.36s] English:** but there's power in it as a companion and from there i could i would love to zoom in onto mojo  
**Translation:** 

**[11995.94s] English:** a little bit do you think uh  
**Translation:** 

**[11997.98s] English:** do you think about that do you think about  
**Translation:** 

**[12000.00s] English:** about LLMs generating Mojo code and helping sort of like when you design a new programming language,  
**Translation:** 

**[12007.64s] English:** it almost seems like, man, it would be nice to sort of almost as a way to learn how I'm supposed to use this thing for them to be trained on some of the Mojo code.  
**Translation:** 

**[12019.48s] English:** So I do lead an AI company, so maybe there will be a Mojo LLM at some point.  
**Translation:** 

**[12024.76s] English:** But if your question is like, how do we make a language to be suitable for LLMs?  
**Translation:** 

**[12030.72s] English:** I think the cool thing about LLMs is you don't have to, right?  
**Translation:** 

**[12036.96s] English:** And so if you look at what is English or any of these other terrible languages that we as humans deal with on a continuous basis,  
**Translation:** 

**[12043.22s] English:** they're never designed for machines, and yet they're the intermediate representation.  
**Translation:** 

**[12048.44s] English:** They're the exchange format that we humans use to get stuff done, right?  
**Translation:** 

**[12052.24s] English:** And so these programming languages, they're an intermediate.  
**Translation:** 

**[12054.76s] English:** They're an intermediate representation between the human and the computer, or the human and the compiler, roughly, right?  
**Translation:** 

**[12060.58s] English:** And so I think the LLMs will have no problem learning whatever keyword we pick.  
**Translation:** Vocabulary: keyword: 关键字

**[12065.60s] English:** Maybe the phi emoji is going to be critical.  
**Translation:** 

**[12067.60s] English:** Oh, maybe that's going to break it. It doesn't tokenize.  
**Translation:** Vocabulary: tokenize: 分词

**[12069.42s] English:** No, the reverse of that, it will actually enable it.  
**Translation:** 

**[12072.42s] English:** Because one of the issues I could see with being a superset of Python is there would be confusion about the gray area.  
**Translation:** 

**[12079.26s] English:** So it would be mixing stuff.  
**Translation:** 

**[12083.00s] English:** Well, I'm a human optimist. I'm awesome.  
**Translation:** Vocabulary: optimist: 乐观主义者

**[12084.76s] English:** I'm an LLM optimist. I think that we'll solve that problem.  
**Translation:** 

**[12086.78s] English:** We'll solve it, yeah.  
**Translation:** 

**[12087.70s] English:** But you look at that and you say, okay, well, reducing the root thing, right?  
**Translation:** 

**[12094.60s] English:** It turns out compilers are very particular, and they really want things.  
**Translation:** Vocabulary: compilers: 编译器

**[12098.02s] English:** They really want the indentation to be right.  
**Translation:** 

**[12099.50s] English:** They really want the colon to be there on your else, or else it will complain, right?  
**Translation:** Vocabulary: indentation: 缩进

**[12103.24s] English:** I mean, compilers can do better at this, but LLMs can totally help solve that problem.  
**Translation:** 

**[12108.66s] English:** And so I'm very happy about the new predictive coding and copilot-type features and things like this,  
**Translation:** Vocabulary: predictive: 预测性

**[12113.78s] English:** because I think it will all just make sense.  
**Translation:** 

**[12114.60s] English:** I think it will all just make sense.  
**Translation:** 

**[12114.74s] English:** I think it's more productive.  
**Translation:** 

**[12115.98s] English:** It's still messy and fuzzy and uncertain, unpredictable.  
**Translation:** Vocabulary: fuzzy: 模糊

**[12120.00s] English:** But is there a future you see, given how big of a leap GPT-4 was, where you start to see something like LLMs inside a compiler or no?  
**Translation:** 

**[12131.58s] English:** I mean, you could do that.  
**Translation:** 

**[12133.02s] English:** Yeah, absolutely.  
**Translation:** 

**[12133.80s] English:** I mean, I think that would be interesting.  
**Translation:** 

**[12135.20s] English:** Is that wise?  
**Translation:** 

**[12136.36s] English:** Well, I mean, it would be very expensive.  
**Translation:** 

**[12139.36s] English:** So compilers run fast and they're very efficient and LLMs are currently very expensive.  
**Translation:** 

**[12143.94s] English:** There's on-device LLMs and there's other things going on.  
**Translation:** 

**[12146.30s] English:** And so maybe there's an answer there.  
**Translation:** 

**[12148.34s] English:** I think that one of the things that I haven't seen enough of is that LLMs to me are amazing when you tap into the creative potential of the hallucinations.  
**Translation:** Vocabulary: hallucinations: 幻觉

**[12160.16s] English:** And so if you're doing creative brainstorming or creative writing or things like that, the hallucinations work in your favor.  
**Translation:** 

**[12168.26s] English:** If you're writing code that has to be correct because you're going to ship it in production, then maybe that's not actually a feature.  
**Translation:** Vocabulary: brainstorming: 头脑风暴

**[12173.60s] English:** And so I think that there has been research and there has been work on building.  
**Translation:** 

**[12178.34s] English:** And so I think that there could be interesting work in terms of building more reliable at scale systems.  
**Translation:** 

**[12190.10s] English:** And that could be interesting.  
**Translation:** 

**[12191.38s] English:** But if you chase that rabbit hole down, the question then becomes, how do you express your intent to the machine?  
**Translation:** 

**[12196.78s] English:** And so maybe you want LLM to provide the spec, but you have a different kind of net that then actually implements the code.  
**Translation:** 

**[12203.60s] English:** Right.  
**Translation:** Vocabulary: implements: 实现代码

**[12204.16s] English:** So it's to use the documentation and inspiration.  
**Translation:** 

**[12208.34s] English:** This is the actual implementation.  
**Translation:** 

**[12210.62s] English:** Yeah, potentially.  
**Translation:** 

**[12213.08s] English:** Since a successful modular will be the thing that runs, I say so jokingly, our AI overlords.  
**Translation:** Vocabulary: modular: 模块化

**[12220.98s] English:** But AI systems that are used across, I know it's a cliche term, but Internet of Things.  
**Translation:** 

**[12227.74s] English:** So I'll joke and say like AGI should be written in Mojo.  
**Translation:** Vocabulary: cliche: 陈词滥调

**[12232.12s] English:** Yeah, AGI should be written in Mojo.  
**Translation:** 

**[12234.12s] English:** You're joking, but it's also possible that it's not a joke.  
**Translation:** 

**[12238.34s] English:** That a lot of the ideas.  
**Translation:** 

**[12240.00s] English:** behind Mojo, it seems like the natural set of ideas that would enable at-scale training  
**Translation:** 

**[12246.90s] English:** and inference of AI systems.  
**Translation:** 

**[12250.46s] English:** So I just have to ask you about the big philosophical question about human civilization.  
**Translation:** Vocabulary: inference: 推理; philosophical: 哲学的

**[12255.04s] English:** So folks like Eliezer Yudkowsky are really concerned about the threat of AI.  
**Translation:** 

**[12260.40s] English:** Do you think about the good and the bad that can happen at scale deployment of AI systems?  
**Translation:** Vocabulary: deployment: 部署

**[12269.16s] English:** Well, so I've thought a lot about it, and there's a lot of different parts to this problem,  
**Translation:** 

**[12274.00s] English:** everything from job displacement to Skynet, things like this.  
**Translation:** Vocabulary: displacement: 岗位替代

**[12278.52s] English:** And so you can zoom into subparts of this problem.  
**Translation:** 

**[12283.32s] English:** I'm not super optimistic about AGI being solved next year.  
**Translation:** Vocabulary: optimistic: 乐观; subparts: 子部分

**[12288.10s] English:** I don't think that's going to happen personally.  
**Translation:** 

**[12290.16s] English:** So you have a kind of Zen-like calm about it.  
**Translation:** 

**[12294.00s] English:** There's a nervousness because the leap of GPT-4 seemed so big.  
**Translation:** 

**[12298.74s] English:** Sure.  
**Translation:** Vocabulary: nervousness: 焦虑感

**[12299.70s] English:** It's like we're almost where there's some kind of transitionary period.  
**Translation:** 

**[12304.04s] English:** You're thinking we're a little bit over.  
**Translation:** Vocabulary: transitionary: 过渡的

**[12305.96s] English:** So, I mean, there's a couple of things going on there.  
**Translation:** 

**[12307.80s] English:** One is I'm sure GPT-5 and 7 and 19 will be also huge leaps.  
**Translation:** 

**[12313.42s] English:** They're also getting much more expensive to run.  
**Translation:** 

**[12315.80s] English:** And so there may be a limiting function in terms of just expense on the one hand and train.  
**Translation:** 

**[12320.50s] English:** That could be a limiter that slows things down.  
**Translation:** 

**[12323.12s] English:** But I think the bigger limiter is outside of Skynet takes over.  
**Translation:** 

**[12328.08s] English:** And I don't spend any time.  
**Translation:** 

**[12329.16s] English:** I'm thinking about that because if Skynet takes over and kills us all, then I'll be dead.  
**Translation:** 

**[12332.12s] English:** So I don't worry about that.  
**Translation:** 

**[12334.10s] English:** So, you know, I mean, that's just OK.  
**Translation:** 

**[12336.66s] English:** Other things to worry about, I'll just focus on.  
**Translation:** 

**[12338.58s] English:** I'll focus and not worry about that one.  
**Translation:** 

**[12341.22s] English:** But I think that the other thing I'd say is that AI moves quickly, but humans move slowly and we adapt slowly.  
**Translation:** 

**[12348.90s] English:** And so what I expect to happen is just like any technology diffusion, like the promise and then the application takes time to roll out.  
**Translation:** Vocabulary: diffusion: 扩散

**[12358.16s] English:** And so I think that I'm.  
**Translation:** 

**[12360.00s] English:** not even too worried about autonomous cars defining away all the taxi drivers remember  
**Translation:** 

**[12365.02s] English:** autonomy is supposed to be solved by 2020 yeah i boy do i remember so and um and so like i think  
**Translation:** 

**[12371.26s] English:** that on the one hand we can see amazing progress but on the other hand we can see that uh you know  
**Translation:** Vocabulary: autonomy: 自主权

**[12377.00s] English:** the reality is a little bit more complicated and it may take longer to roll out than than you might  
**Translation:** 

**[12381.50s] English:** expect well that's in the physical space i i do think in the digital space is uh the stuff that's  
**Translation:** 

**[12386.96s] English:** built on top of llms that runs you know the millions of apps that can be built on top of them  
**Translation:** 

**[12393.22s] English:** and that could be run on millions of devices millions of types of devices yeah i i just think  
**Translation:** 

**[12400.20s] English:** that the rapid effect it has on human civilization could be  
**Translation:** 

**[12405.60s] English:** truly transformative to it yeah well we don't even know well and so that predict well and there  
**Translation:** 

**[12411.24s] English:** i think it depends on are you an optimist or a pessimist or a masochist um just to clarify  
**Translation:** 

**[12416.96s] English:** uh optimist about human civilization me too and so i look at that as saying okay cool well yeah i do  
**Translation:** Vocabulary: masochist: 受虐者; optimist: 乐观主义者; pessimist: 悲观主义者

**[12424.06s] English:** right and so some people say oh my god it's going to destroy us all how do we prevent that  
**Translation:** 

**[12427.94s] English:** i i kind of look at it from a is it going to unlock us all right you talk about coding it's  
**Translation:** 

**[12433.84s] English:** going to make so i don't have to do all the repetitive stuff well suddenly that's a very  
**Translation:** 

**[12437.62s] English:** optimistic way to look at and you look at what a lot of a lot of these technologies have done to  
**Translation:** Vocabulary: optimistic: 乐观; repetitive: 重复

**[12442.94s] English:** improve our lives and i want that to go faster  
**Translation:** 

**[12445.34s] English:** so  
**Translation:** 

**[12445.60s] English:** what do you think the future of programming looks like in the next 10 20 30 50 years  
**Translation:** 

**[12451.24s] English:** the lms and uh with with mojo with modular like the vision for devices the hardware to the compilers  
**Translation:** Vocabulary: compilers: 编译器; modular: 模块化

**[12461.46s] English:** to this to the different stacks of software yeah well so what i want i mean coming coming back to  
**Translation:** 

**[12466.48s] English:** my arch nemesis right it's complexity right so again me being the optimist if we drive down  
**Translation:** Vocabulary: complexity: 复杂性; nemesis: 宿敌

**[12473.10s] English:** complexity we can make these tools easier and we can make these tools easier and we can make these  
**Translation:** 

**[12475.60s] English:** technologies these cool hardware widgets accessible to way more people right and  
**Translation:** Vocabulary: widgets: 小工具

**[12480.00s] English:** So what I'd love to see is more personalized experiences, more things, the research getting into production instead of being lost at NeurIPS, right?  
**Translation:** 

**[12488.36s] English:** And these things that impact people's lives by entering products.  
**Translation:** 

**[12495.28s] English:** And so one of the things that I'm a little bit concerned about is right now, the big companies are investing huge amounts of money and are driving the top line of AI capability forward really quickly.  
**Translation:** 

**[12505.32s] English:** But if it means that you have to have $100 million to train a model or more, $100 billion, right?  
**Translation:** Vocabulary: capability: 能力

**[12512.26s] English:** Well, that's going to make it very concentrated with very few people in the world that can actually do this stuff.  
**Translation:** 

**[12518.34s] English:** I would much rather see lots of people across the industry be able to participate and use this, right?  
**Translation:** 

**[12525.24s] English:** And you look at this, you know, I mean, a lot of great research has been done in the health world and looking at like detecting pathologies and doing radiology with AI and like doing.  
**Translation:** 

**[12535.32s] English:** Well, the problem today is that to deploy and build these systems, you have to be an expert in radiology and an expert in AI.  
**Translation:** Vocabulary: deploy: 部署; detecting: 检测; pathologies: 病理; radiology: 放射学

**[12543.82s] English:** And if we can break down the barriers so that more people can use AI techniques, and it's more like programming Python, which roughly everybody can do if they want to, right?  
**Translation:** 

**[12554.98s] English:** Then I think that we'll get a lot more practical application of these techniques and a lot more nichier, cool, but narrower domains.  
**Translation:** Vocabulary: barriers: 障碍; narrower: 更窄

**[12562.36s] English:** And I think that's going to be really cool.  
**Translation:** 

**[12564.00s] English:** Do you think we'll have more?  
**Translation:** 

**[12565.32s] English:** Or less programmers in the world than now?  
**Translation:** 

**[12568.64s] English:** Well, so I think we'll have more programmers, but they may not consider themselves to be programmers.  
**Translation:** Vocabulary: programmers: 程序员

**[12573.74s] English:** That'd be a different name for it.  
**Translation:** 

**[12574.94s] English:** Right?  
**Translation:** 

**[12575.18s] English:** I mean, do you consider somebody that uses, you know, I think that arguably the most popular programming language is Excel.  
**Translation:** 

**[12582.68s] English:** Yeah.  
**Translation:** Vocabulary: arguably: 可以说

**[12584.08s] English:** Right?  
**Translation:** 

**[12584.80s] English:** Yeah.  
**Translation:** 

**[12585.10s] English:** And so do they consider themselves to be programmers?  
**Translation:** 

**[12587.46s] English:** Maybe not.  
**Translation:** 

**[12588.22s] English:** I mean, some of them make crazy macros and stuff like that.  
**Translation:** 

**[12591.02s] English:** But what you mentioned, Steve?  
**Translation:** 

**[12595.32s] English:** Steve Jobs, it's the bicycle for the mind that allows you to go fast.  
**Translation:** 

**[12600.00s] English:** right and so i think that as we look forward right what is ai i look at it as hopefully a  
**Translation:** 

**[12605.82s] English:** new programming paradigm it's like object-oriented programming right if you want to write a cat  
**Translation:** 

**[12610.22s] English:** detector you don't use for loops it turns out that's not the right tool for the job right  
**Translation:** Vocabulary: detector: 检测器; paradigm: 范式

**[12614.42s] English:** and so right now unfortunately because i mean it's not unfortunate but it's just kind of where  
**Translation:** 

**[12619.02s] English:** things are ai is this weird different thing that's not integrated into programming languages  
**Translation:** 

**[12624.84s] English:** and normal tool chains and all the technology is really weird and doesn't work right and you  
**Translation:** 

**[12629.30s] English:** have to babysit it and every time you switch hardware it's different it shouldn't be that way  
**Translation:** 

**[12633.88s] English:** when you change that when you fix that suddenly again the tools technologies can be way easier to  
**Translation:** 

**[12638.64s] English:** use you can start using them for many more things and so that that's that's why i would be excited  
**Translation:** 

**[12642.74s] English:** about what kind of advice could you give to somebody in high school right now or maybe early  
**Translation:** 

**[12647.58s] English:** college who's curious about programming and feeling like the world is changing really quickly  
**Translation:** 

**[12655.22s] English:** here yeah well what kind of stuff to learn what kind of stuff to work on  
**Translation:** 

**[12659.04s] English:** you  
**Translation:** 

**[12659.30s] English:** should they finish college they go work at a company should they build a thing what do you  
**Translation:** 

**[12664.92s] English:** think well so i mean one of the things i'd say is that um you'll be most successful if you work on  
**Translation:** 

**[12670.04s] English:** something you're excited by and so don't get the book and read the book cover to cover and study  
**Translation:** 

**[12676.70s] English:** and memorize and recite and flashcard and go build something like go solve a problem go build the  
**Translation:** Vocabulary: flashcard: 速记卡片; memorize: 记忆

**[12681.90s] English:** thing that you want to exist go build an app go build train a model like go build something and  
**Translation:** 

**[12688.16s] English:** actually use it and set a goal for you  
**Translation:** 

**[12689.28s] English:** yourself and if you do that then you'll you know there's a success there's the adrenaline rush  
**Translation:** 

**[12694.44s] English:** there's the achievement there's the unlock that i think is where you know if you keep setting goals  
**Translation:** Vocabulary: adrenaline: 肾上腺素

**[12699.02s] English:** and you keep doing things and building things learning by building is really powerful um in  
**Translation:** 

**[12704.24s] English:** terms of career advice i mean everybody's different it's very hard to give generalized  
**Translation:** Vocabulary: generalized: 泛化

**[12707.46s] English:** experience generalized advice um i'll speak as you know a compiler nerd if everybody's going  
**Translation:** 

**[12713.82s] English:** left sometimes it's pretty cool to go right yeah and so just because everybody's going left is  
**Translation:** 

**[12719.28s] English:** doing a thing  
**Translation:** 

**[12720.00s] English:** It doesn't mean you have to do the same thing and follow the herd.  
**Translation:** 

**[12723.96s] English:** In fact, I think that sometimes the most exciting paths through life lead to being curious about  
**Translation:** 

**[12730.58s] English:** things that nobody else actually focuses on, right?  
**Translation:** 

**[12733.40s] English:** And it turns out that understanding deeply parts of the problem that people want to take  
**Translation:** 

**[12738.84s] English:** for granted makes you extremely valuable and specialized in ways that the herd is not.  
**Translation:** 

**[12744.38s] English:** And so, again, I mean, there's lots of rooms for specialization, lots of rooms for generalists.  
**Translation:** 

**[12749.44s] English:** There's lots of room for different kinds and parts of the problem.  
**Translation:** Vocabulary: generalists: 通才人士

**[12752.24s] English:** But I think that it's, you know, just because everybody's doing one thing doesn't mean you  
**Translation:** 

**[12756.66s] English:** should necessarily do it.  
**Translation:** 

**[12757.94s] English:** And now the herd is using Python, so if you want to be a rebel, go check out Mojo and  
**Translation:** 

**[12765.72s] English:** help Chris and the rest of the world fight the arch nemesis of complexity, because simple  
**Translation:** Vocabulary: complexity: 复杂性; nemesis: 宿敌

**[12770.80s] English:** is beautiful.  
**Translation:** 

**[12771.44s] English:** There you go.  
**Translation:** 

**[12772.58s] English:** Chris, you're an incredible person.  
**Translation:** 

**[12774.30s] English:** You've been so kind to me ever since we met.  
**Translation:** 

**[12776.78s] English:** You've been extremely supportive.  
**Translation:** 

**[12778.16s] English:** I'm forever grateful.  
**Translation:** 

**[12779.60s] English:** Thank you for being who you are, for being legit, for being kind, for fighting this really  
**Translation:** 

**[12787.06s] English:** interesting problem of how to make AI accessible to a huge number of people, a huge number  
**Translation:** Vocabulary: legit: 正直的

**[12792.78s] English:** of devices.  
**Translation:** 

**[12793.98s] English:** Yeah.  
**Translation:** 

**[12794.26s] English:** Well, so Lex, you're a pretty special person, too, right?  
**Translation:** 

**[12796.40s] English:** And so I think that, you know, one of the funny things about you is that besides being  
**Translation:** 

**[12801.26s] English:** curious and pretty damn smart, you're actually willing to push on things.  
**Translation:** 

**[12804.56s] English:** And I think that you've got an agenda to, like, make the world think.  
**Translation:** 

**[12809.44s] English:** Which I think is a pretty good agenda.  
**Translation:** 

**[12811.28s] English:** It's a pretty good one.  
**Translation:** 

**[12812.70s] English:** Thank you so much for talking to me, Chris.  
**Translation:** 

**[12814.38s] English:** Yeah.  
**Translation:** 

**[12814.70s] English:** Thanks, Lex.  
**Translation:** 

**[12816.12s] English:** Thanks for listening to this conversation with Chris Ladner.  
**Translation:** 

**[12818.78s] English:** To support this podcast, please check out our sponsors in the description.  
**Translation:** 

**[12822.46s] English:** And now, let me leave you with some words from Isaac Asimov.  
**Translation:** Vocabulary: sponsors: 赞助商

**[12826.12s] English:** I do not fear computers.  
**Translation:** 

**[12828.42s] English:** I fear the lack of them.  
**Translation:** 

**[12831.54s] English:** Thank you for listening, and hope to see you next time.  
**Translation:** 

**[12839.44s] English:** Thank you.  
**Translation:** 

**[12840.00s] English:** Teksting av Nicolai Winther  
**Translation:** Vocabulary: teksting: 测序


<!-- TRANSCRIPTION_COMPLETE -->
