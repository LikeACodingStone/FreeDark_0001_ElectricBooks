# Podcast vocabulary notes
Source file: Lex Fridman - Demis Hassabis： Future of AI, Simulating Reality, Physics and Video Games ｜ Lex Fridman Podcast #475.opus
Improved subtitle: punctuation and vocabulary regenerated from current config.

**[0.00s] English:** It's hard for us humans to make any kind of clean predictions about highly nonlinear dynamical systems.  
**Translation:** 

**[5.00s] English:** But, again, to your point, we might be very surprised at what classical learning systems might be able to do with even fluid.  
**Translation:** Vocabulary: dynamical: 动力学的

**[11.88s] English:** Yes, exactly. I mean, fluid dynamics, Navier-Stokes equations—these are traditionally thought of as very, very difficult, intractable problems to solve on classical systems.  
**Translation:** 

**[20.18s] English:** They take enormous amounts of compute, such as weather prediction systems, which all involve fluid dynamics calculations.  
**Translation:** Vocabulary: compute: 计算; equations: 方程; intractable: 难以解决的

**[26.44s] English:** But again, if you look at something like VO, our video generation model, it can model liquids quite well—surprisingly well—and materials, specular lighting.  
**Translation:** 

**[37.52s] English:** I love the ones where, you know, there are people who generate videos of clear liquids going through hydraulic presses and then getting squeezed out.  
**Translation:** Vocabulary: hydraulic: 液压; lighting: 照明; liquids: 液体; presses: 压机; specular: 镜面; squeezed: 挤压

**[45.32s] English:** I used to write physics engines and graphics engines in my early days in gaming, and I know it's just so painstakingly hard to build programs that can do that.  
**Translation:** 

**[54.42s] English:** And yet, somehow, these systems.  
**Translation:** Vocabulary: painstakingly: 极其费力地

**[56.44s] English:** Are you know, reverse-engineering from just watching YouTube videos.  
**Translation:** 

**[60.94s] English:** So, presumably, what is happening is that it is extracting some underlying structure around how these materials behave.  
**Translation:** Vocabulary: extracting: 提取; presumably: 推测而言

**[68.66s] English:** So, perhaps there is some kind of lower-dimensional manifold that can be learned if we actually fully understood what's going on under the hood.  
**Translation:** 

**[76.68s] English:** That's maybe, you know, maybe true of most of reality.  
**Translation:** Vocabulary: manifold: 多维流形

**[82.10s] English:** The following is a conversation with Demis Hassabis.  
**Translation:** 

**[85.28s] English:** His second time on the podcast, he is the leader of Google DeepMind and is now a Nobel Prize winner.  
**Translation:** Vocabulary: hassabis: 哈萨斯; nobel: 诺贝尔奖

**[94.22s] English:** Demis is one of the most brilliant and fascinating minds in the world today, working on understanding and building intelligence and exploring the big mysteries of our universe.  
**Translation:** 

**[107.90s] English:** This was truly an honor and a pleasure for me.  
**Translation:** 

**[111.40s] English:** This is the Lex Friedman Podcast. To support it:  
**Translation:** 

**[114.60s] English:** Please check out ours.  
**Translation:** Vocabulary: friedman: 弗里德曼

**[115.28s] English:** Sponsors in the description, and consider subscribing to this.  
**Translation:** 

**[120.00s] English:** And now, dear friends, here's Demis Hassabis.  
**Translation:** Vocabulary: sponsors: 赞助商; subscribing: 订阅

**[150.00s] English:** Yeah. Neuroscience. What are we talking about? Sure. Well, look, I felt that it's sort of a  
**Translation:** 

**[154.68s] English:** Tradition, I think, is for Nobel Prize lectures to be a little provocative, and  
**Translation:** Vocabulary: neuroscience: 神经科学; provocative: 发人深省的

**[158.78s] English:** I wanted to follow that tradition. What I was talking about there is if you take a step back.  
**Translation:** 

**[162.70s] English:** And you look at all the work that we've done, especially with the Alpha X projects. So, I'm  
**Translation:** Vocabulary: alpha: 最先的

**[167.28s] English:** Thinking about AlphaGo, of course, and AlphaFold. What they really are is that we're building models of very  
**Translation:** 

**[172.72s] English:** Combinatorially high-dimensional spaces that, you know, if you try to brute-force a solution,...  
**Translation:** Vocabulary: combinatorially: 组合上

**[178.24s] English:** Find the best move, and go.  
**Translation:** 

**[180.00s] English:** Or find the exact shape of a protein. And if you enumerated all the possibilities,  
**Translation:** Vocabulary: enumerated: 列举出

**[185.26s] English:** There wouldn't be enough time in the, you know, the entire universe. So you have to do  
**Translation:** 

**[189.44s] English:** Something much smarter. And what we did in both cases was build models of those environments.  
**Translation:** Vocabulary: environments: 环境

**[195.20s] English:** And that guided the search in a smart way, and that makes it tractable. So, if you think about it,  
**Translation:** 

**[201.26s] English:** Protein folding, which is obviously a natural system, you know, why should that be possible?  
**Translation:** Vocabulary: tractable: 可处理的

**[205.18s] English:** How does physics do that? You know, proteins fold in milliseconds in our bodies.  
**Translation:** 

**[209.08s] English:** So, somehow,  
**Translation:** Vocabulary: milliseconds: 毫秒

**[210.00s] English:** Physics solves this problem, that we've now also solved computationally. And I think the reason,  
**Translation:** 

**[215.56s] English:** That's possible: in nature, natural systems have structure because they were subject to  
**Translation:** Vocabulary: computationally: 通过计算

**[221.46s] English:** Evolutionary processes that shape them. And if that's true, then you can maybe learn.  
**Translation:** 

**[227.04s] English:** What that structure is.  
**Translation:** Vocabulary: evolutionary: 进化的

**[229.68s] English:** So, this perspective is really interesting. One, you've hinted at it,  
**Translation:** 

**[234.08s] English:** Which is almost like crudely stating, "anything that can be evolved,  
**Translation:** Vocabulary: crudely: 粗略地; evolved: 进化; hinted: 暗示

**[240.00s] English:** Can be efficiently modeled, I think there's some truth to that. Yeah, I sometimes call it "survival.  
**Translation:** 

**[244.54s] English:** Of the stabilist, or something like that, because you know, it's of course there's evolution.  
**Translation:** Vocabulary: efficiently: 高效地; modeled: 建模; stabilist: 稳定者

**[249.10s] English:** For life, or living things, but there's also, you know, if you think about geological time, so the  
**Translation:** 

**[255.36s] English:** The shape of mountains that have been shaped by weathering processes, right, over thousands of years, but then  
**Translation:** Vocabulary: geological: 地质的

**[261.04s] English:** You can even take it cosmological, like the orbits of planets and the shapes of asteroids; these have all  
**Translation:** 

**[266.30s] English:** Been subjected to processes that have acted on them many, many times, so if that's true, then  
**Translation:** Vocabulary: asteroids: 小行星; cosmological: 宇宙的; orbits: 轨道

**[272.20s] English:** There should be some sort of pattern that you can kind of reverse-engineer and learn, and a kind of manifold.  
**Translation:** 

**[278.34s] English:** Really, that helps you search for the right solution to the right shape, and actually allows you to.  
**Translation:** Vocabulary: manifold: 多面体

**[284.80s] English:** Predict things about it in an efficient way because it's not a random pattern, right? So it may not be  
**Translation:** 

**[290.64s] English:** Possible for man-made things or abstract things, like factorizing large numbers, because unless  
**Translation:** 

**[295.76s] English:** There's patterns.  
**Translation:** 

**[296.28s] English:** In the number space, which there might be, but if there's not, in its uniformity, then there's no pattern.  
**Translation:** 

**[300.78s] English:** To learn, there's no model to learn that will help you search; you have to do brute-force searching. So, in that case,...  
**Translation:** 

**[305.54s] English:** Case you know, you might need a quantum computer something like this, but in most cases,  
**Translation:** Vocabulary: quantum: 量子计算机

**[309.48s] English:** In nature, those that we're interested in are not like that; they have structure that evolved for a  
**Translation:** 

**[315.42s] English:** Reason and survived over time, and if that's true, I think that's potentially learnable by a neural network.  
**Translation:** Vocabulary: evolved: 进化; neural: 神经

**[320.48s] English:** Network: It's like nature is doing a search process, and it's so fascinating that it's.  
**Translation:** 

**[326.26s] English:** In that search process, we are creating systems that can be efficiently modeled, yes, right, yeah, so.  
**Translation:** Vocabulary: efficiently: 高效率地; modeled: 建模

**[333.02s] English:** Interesting, so they can be efficiently rediscovered or recovered. Um, because nature is not random, right?  
**Translation:** 

**[338.58s] English:** These things that we see around us, including even the more stable elements, all of  
**Translation:** Vocabulary: rediscovered: 重新发现

**[343.02s] English:** Those things are subject to some kind of selection process or pressure, do you think?  
**Translation:** 

**[348.64s] English:** You're also a fan of theoretical computer science and complexity. Do you think we can come up with a  
**Translation:** 

**[352.92s] English:** Complexity class, like a complexity zoo.  
**Translation:** 

**[356.26s] English:** Type of class where maybe it's a set of learning objectives.  
**Translation:** Vocabulary: complexity: 复杂性; objectives: 目标

**[360.00s] English:** Systems, the set of learnable natural systems (LNS). This is a new class of systems that could be  
**Translation:** 

**[370.18s] English:** Actually, some natural systems that can be learned by classical systems in this kind of way.  
**Translation:** 

**[375.20s] English:** Modeled efficiently, yeah. I mean, I've always been fascinated by the P = MP question and  
**Translation:** 

**[381.16s] English:** What is modelable by classical systems, i.e., non-quantum systems, you know, Turing machines.  
**Translation:** Vocabulary: fascinated: 着迷; modelable: 可建模的; turing: 图灵机

**[387.76s] English:** In effect, and that's exactly what I'm working on actually, in kind of my few moments of spare.  
**Translation:** 

**[392.58s] English:** Time with a few colleagues about whether there should be, you know, maybe a new class of problem.  
**Translation:** Vocabulary: colleagues: 同行

**[397.14s] English:** That is solvable by this type of neural network process and kind of mapped onto these natural.  
**Translation:** 

**[403.40s] English:** Systems. So, you know, the things that exist in physics and have structure. So, I think that could.  
**Translation:** Vocabulary: neural: 神经网络; solvable: 可解决的

**[409.10s] English:** Be a very interesting new way of thinking about it, and it sort of fits with the way I think about it.  
**Translation:** 

**[413.76s] English:** Physics in general, which is that you know, I think information is primary.  
**Translation:** 

**[417.76s] English:** Information is the most fundamental unit of the universe, more fundamental than energy and  
**Translation:** 

**[421.68s] English:** Matter. I think they can all be converted into each other. But I think of the universe as a  
**Translation:** Vocabulary: converted: 转换

**[425.92s] English:** Kind of an informational system. So, when you think of the universe as an informational system,...  
**Translation:** 

**[430.14s] English:** Then the P = MP question is a physics question. That's right, and it's a question.  
**Translation:** 

**[436.34s] English:** That can help us actually solve the entirety of this whole thing going on. Yeah. I think it's one.  
**Translation:** 

**[441.08s] English:** Of the most fundamental questions, actually, if you think of physics as informational, and the  
**Translation:** Vocabulary: entirety: 全部

**[446.90s] English:** The answer to that, I think, is that it's a fundamental question. And I think it's a fundamental question.  
**Translation:** 

**[447.76s] English:** That can help us actually solve the entirety of this whole thing going on. Yeah. I think it's  
**Translation:** 

**[447.84s] English:** Going to be, you know, very enlightening. More specifically to the P and MP question.  
**Translation:** 

**[453.62s] English:** This, again, some of the stuff we're saying is kind of crazy right now.  
**Translation:** Vocabulary: enlightening: 启发性的

**[457.30s] English:** Just like the Christian Anfinson Nobel Prize speech, controversial things that he said.  
**Translation:** 

**[461.90s] English:** Sounded crazy. And then you went and got a Nobel Prize for this with John Jumper.  
**Translation:** Vocabulary: nobel: 诺贝尔奖

**[466.20s] English:** Solved the problem. So, let me just stick to P = MP. Do you think there's something?  
**Translation:** 

**[470.84s] English:** In this thing we're talking about, that could be shown if you can do.  
**Translation:** 

**[477.76s] English:** Something like a polynomial.  
**Translation:** 

**[480.00s] English:** Time or constant-time computation, computed ahead of time, and constructing this gigantic model, then you can solve.  
**Translation:** Vocabulary: computation: 计算; computed: 已计算; constructing: 构建; gigantic: 巨大的; polynomial: 多项式

**[487.64s] English:** Some of these extremely difficult problems, in a theoretical computer science kind of way, yeah, I  
**Translation:** 

**[492.58s] English:** I think that there are actually a huge class of problems that could be couched in this way.  
**Translation:** 

**[497.44s] English:** The way we did AlphaGo and the way we did AlphaFold, where you model what the dynamics of  
**Translation:** 

**[502.88s] English:** The system has the properties of that system, and the environment that you're trying to  
**Translation:** 

**[507.80s] English:** Understand, and then that makes the search for the solution or the prediction of the next step.  
**Translation:** 

**[514.16s] English:** Efficient, basically, in polynomial time, so tractable by a classical system, which a neural network is.  
**Translation:** Vocabulary: neural: 神经网络; tractable: 可处理的

**[522.00s] English:** It runs on normal computers, right? Classical computers, Turing machines, in effect, and I think.  
**Translation:** 

**[528.92s] English:** It's one of the most interesting questions there is: how far can that paradigm go? You know, I  
**Translation:** Vocabulary: paradigm: 范式; turing: 图灵机

**[533.30s] English:** Think we've proven, and the AI community in general, that classical systems  
**Translation:** 

**[537.78s] English:** Turing machines can go a lot further than we previously thought; you know, they can do things.  
**Translation:** 

**[542.16s] English:** Like, model the structures of proteins and play Go to better than world-champion level, and uh,...  
**Translation:** 

**[548.84s] English:** Know, a lot of people would have thought maybe 10 or 20 years ago that was decades away, or maybe you.  
**Translation:** 

**[553.80s] English:** Would need some sort of quantum machines to interact with quantum systems to be able to do things like.  
**Translation:** 

**[558.64s] English:** Protein folding, and so I think we haven't really, uh, even sort of scratched the surface yet of what  
**Translation:** Vocabulary: quantum: 量子; scratched: 触及

**[565.06s] English:** Uh, classical systems, so-called, uh  
**Translation:** 

**[567.78s] English:** Could do, and of course, AGI being built on a neural network system on top of a neural network.  
**Translation:** 

**[573.76s] English:** A system on top of a classical computer would be the ultimate expression of that, and I think the limit.  
**Translation:** 

**[579.32s] English:** That you know, the bounds of that kind of system, what it can do—it's very  
**Translation:** Vocabulary: bounds: 界限

**[583.78s] English:** Interesting question, and it directly speaks to the "p = mp" issue. What do you think?  
**Translation:** 

**[588.72s] English:** Again, hypothetically, it might be outside of this, maybe emergent phenomena, like if you look at cellular.  
**Translation:** Vocabulary: cellular: 细胞的; emergent: emergent; hypothetically: 假设地

**[596.10s] English:** Automata: Some of the ones you have the  
**Translation:** 

**[597.78s] English:** Extremely simple systems, and then some complexity.  
**Translation:** Vocabulary: automata: 自动机; complexity: 复杂性

**[600.00s] English:** Emerges: Yes, maybe that would be outside, or even, would you guess, that might be amenable to.  
**Translation:** 

**[607.22s] English:** Efficient modeling by a classical system, I think, would be right on the boundary.  
**Translation:** Vocabulary: emerges: 出现

**[612.28s] English:** Right, so, um, I think most emergent systems, like cellular automata, could be modeled by a  
**Translation:** 

**[618.58s] English:** Classical systems, you just sort of do a forward simulation of it, and it'd probably be efficient.  
**Translation:** Vocabulary: modeled: 模拟

**[622.16s] English:** Enough, um, of course there's the question of things like chaotic systems where the initial conditions  
**Translation:** 

**[627.68s] English:** Really, it matters, and then you get to some you know, uncorrelated end state; now, those could be difficult.  
**Translation:** Vocabulary: chaotic: 混乱; uncorrelated: 不相关的

**[633.70s] English:** To model, so I think these are kind of the open questions, but I think when you step back and  
**Translation:** 

**[638.60s] English:** Look at what we've done with the systems and the problems we've solved, and then you look at  
**Translation:** 

**[643.96s] English:** Things like VO3, for example, in video generation, sorting, rendering physics and lighting, and things like that.  
**Translation:** 

**[651.18s] English:** That you know, really in core fundamental things in physics, it's pretty interesting. I think it's  
**Translation:** Vocabulary: lighting: 照明; sorting: 排序

**[656.44s] English:** Telling us something quite fundamental.  
**Translation:** 

**[657.68s] English:** About how the universe is structured, in my opinion, um, so you know, in a way, that's what I want to build.  
**Translation:** 

**[662.90s] English:** AGI is for helping us, as scientists, answer questions like P = NP, yeah; I think.  
**Translation:** 

**[670.10s] English:** We might be continuously surprised about what is modelable by classical computers. I mean, Alpha.  
**Translation:** Vocabulary: alpha: 阿尔法; modelable: 可建模的

**[675.78s] English:** Fold three on the interaction side is surprising because you can make any kind of progress on that.  
**Translation:** 

**[682.22s] English:** Direction Alpha Genome is surprising that you can map the genetic code to the  
**Translation:** Vocabulary: genome: 基因组

**[687.66s] English:** Function: Kind of playing with the emergent phenomena, you think there are so many combinatorial possibilities.  
**Translation:** 

**[692.44s] English:** Options that, and then here you go—you can find the kernel that is efficiently modeled, yes, because  
**Translation:** Vocabulary: combinatorial: 组合的; efficiently: 高效地; emergent: 涌现的; kernel: 内核

**[697.40s] English:** There's some structure there, and some landscape— you know, in the energy landscape, or whatever it is that.  
**Translation:** 

**[702.56s] English:** You can follow some gradients, and of course, what neural networks are very good at.  
**Translation:** Vocabulary: gradients: 梯度; neural: 神经

**[706.32s] English:** Is following gradients, and so if there's one to follow, an object, and you can specify the objective.  
**Translation:** 

**[711.32s] English:** Function correctly, you know, you don't have to deal with all that complexity, which I think is how we  
**Translation:** Vocabulary: complexity: 复杂性; specify: 指定

**[717.50s] English:** Make it work, and I think that's a really good question. And I think that's a really good question.  
**Translation:** 

**[717.66s] English:** Maybe you've naively thought about it for decades.  
**Translation:** Vocabulary: naively: 天真地

**[720.00s] English:** Those problems, if you just enumerate all the possibilities, look totally intractable.  
**Translation:** 

**[724.22s] English:** And there are many, many problems like that, and then you think, "Well, it's like 10 to 300.  
**Translation:** Vocabulary: enumerate: 列举; intractable: 难以解决

**[727.94s] English:** Possible protein structures: 10 to the hundred and seventy. There are also all of these Go positions.  
**Translation:** 

**[735.22s] English:** Are there way more than atoms in the universe, so how could one possibly find the right solution?  
**Translation:** 

**[740.14s] English:** Or predict the next step, and it turns out that it is possible, and of course, reality shows that this is indeed true.  
**Translation:** 

**[745.74s] English:** Nature does it right; proteins do fold, so that gives you confidence that there must be a way to design stable structures as well.  
**Translation:** 

**[751.02s] English:** Understood how physics was doing that, in a sense, and then we could mimic that process.  
**Translation:** 

**[757.18s] English:** I model that process; it should be possible on our classical systems, is basically what the  
**Translation:** 

**[763.56s] English:** Conjecture is about, and of course, there are non-linear dynamical systems, which are highly non-linear.  
**Translation:** 

**[768.16s] English:** Dynamical systems, everything involving fluid, yes, right? You know, the recent conversation with...  
**Translation:** Vocabulary: conjecture: 猜测; dynamical: 动力学的

**[773.58s] English:** Terence Tao, who is mathematically  
**Translation:** 

**[774.88s] English:** Uh, it contends with a very difficult aspect of systems that have some singularities in them.  
**Translation:** Vocabulary: mathematically: 用数学方法

**[781.52s] English:** That breaks the mathematics, and it's just hard for us humans to make any kind of clean predictions.  
**Translation:** 

**[786.88s] English:** About highly nonlinear dynamical systems, but again, to your point, we might be very surprised.  
**Translation:** 

**[792.84s] English:** What classical learning systems might be able to do about even fluid, yes, exactly. I mean, fluid.  
**Translation:** 

**[798.14s] English:** Dynamics Navier-Stokes equations; these are traditionally thought to be very, very difficult.  
**Translation:** Vocabulary: equations: 方程

**[802.10s] English:** Intractable kinds of problems to do on classical systems, but I think it's a very difficult problem.  
**Translation:** 

**[804.88s] English:** To do on classical systems, they take enormous amounts of compute, you know, like weather prediction.  
**Translation:** Vocabulary: compute: 计算; intractable: 难以解决的

**[808.34s] English:** Systems, you know, these kinds of things all involve fluid dynamics calculations, and, um, but again, if you  
**Translation:** 

**[815.10s] English:** Look at something like our video generation model; it can model liquids quite well, surprisingly.  
**Translation:** Vocabulary: liquids: 液体

**[820.80s] English:** Well, and materials with specular lighting—I love the ones where you know, there are people who  
**Translation:** 

**[826.88s] English:** Generate videos where there are clear liquids going through hydraulic presses, and then it's  
**Translation:** Vocabulary: hydraulic: 液压; presses: 压机; specular: 镜面

**[830.94s] English:** Being squeezed out, I used to write physics engines and graphics systems, and I used to write.  
**Translation:** 

**[834.88s] English:** Graphics engines, and in my early days in gaming, I know it's just so painstakingly hard to build.  
**Translation:** Vocabulary: painstakingly: 极其费力; squeezed: 被挤出

**[840.00s] English:** Programs that can do that, and yet somehow, these systems are—you know—reverse-engineering from.  
**Translation:** 

**[845.62s] English:** Just watching YouTube videos, so presumably what's happening is it's extracting some underlying  
**Translation:** Vocabulary: extracting: 提取; presumably: 大概

**[851.58s] English:** Structure around how these materials behave, so perhaps there is some kind of lower-dimensional  
**Translation:** 

**[858.14s] English:** Manifold that can be learned if we actually fully understood what's going on under the hood: that's  
**Translation:** Vocabulary: manifold: 低维流形

**[863.88s] English:** Maybe you know, maybe it's true of most of reality. Yeah, I've been continuously precisely by this.  
**Translation:** 

**[869.88s] English:** Aspect of VO3, I think a lot of people highlight different aspects, including the comedic and the  
**Translation:** Vocabulary: comedic: 喜剧的; highlight: 强调; precisely: 精确地

**[875.06s] English:** Media and all that kind of stuff, and then the ultra-realistic ability to capture humans in a  
**Translation:** 

**[880.60s] English:** Really, in a nice way that's compelling and it feels close to reality, and then combine that with native.  
**Translation:** Vocabulary: compelling: 有吸引力的

**[886.02s] English:** All of those are marvelous things about VO3, but the exact thing you're mentioning...  
**Translation:** 

**[890.94s] English:** Which is the physics? Yeah, it's not perfect, but it's pretty damn good, and then the really...  
**Translation:** 

**[897.28s] English:** An interesting scientific question is: what is it?  
**Translation:** 

**[899.80s] English:** You're talking about  
**Translation:** 

**[899.88s] English:** Understanding about our world in order to be able to do that, because of the cynicism.  
**Translation:** 

**[905.52s] English:** Take, with diffusion models, there's no way it understands anything, but it seemed (i.e., I) mean I  
**Translation:** Vocabulary: cynicism: 怀疑一切; diffusion: 扩散

**[911.92s] English:** Don't think you can generate that kind of video without understanding, and then our own philosophical.  
**Translation:** 

**[917.16s] English:** Notion of what it means to understand is like brought to the surface: like, to what degree do  
**Translation:** Vocabulary: philosophical: 哲学的

**[922.66s] English:** You think VO3 understands our world? I think to the extent that it can predict the next frames.  
**Translation:** 

**[928.24s] English:** You know, in a coherent way.  
**Translation:** Vocabulary: coherent: 连贯的

**[929.80s] English:** That's some form of understanding, right, not in the anthropomorphic version of you.  
**Translation:** 

**[935.58s] English:** I know it's not some kind of deep philosophical understanding of what's going on, I don't think.  
**Translation:** Vocabulary: anthropomorphic: 拟人化的

**[939.70s] English:** These systems have that, but they certainly have modeled enough of the dynamics, you know.  
**Translation:** 

**[945.50s] English:** Put it that way, and they can pretty accurately generate whatever it is eight seconds of.  
**Translation:** Vocabulary: modeled: 模拟

**[950.96s] English:** Consistent video, that by eye at least, you know, at a glance, is quite hard to distinguish what.  
**Translation:** 

**[956.12s] English:** The issues are, and imagine that in two or three more years' time—that's the thing I'm talking about.  
**Translation:** 

**[959.80s] English:** I'm thinking.  
**Translation:** 

**[960.00s] English:** And how incredible that they will look, given where we've come from—you know, the early versions of that one or two years ago. And so, the rate of progress is incredible. And I think I'm like you: a lot of people love all the stand-up comedians, and that actually captures a lot of human dynamics very well—and body language.  
**Translation:** Vocabulary: comedians: 喜剧演员

**[982.20s] English:** But actually, the thing I'm most impressed with and fascinated by is the physics behavior, the lighting, and materials—and liquids. And it's pretty amazing that it can do that. And I think that shows that it has some notion of at least intuitive physics, right—how things are supposed to work intuitively, maybe the way a human child would understand physics, right, as opposed to, you know, a PhD student really being able to unpack all the equations.  
**Translation:** 

**[1011.40s] English:** It's more of an intuitive understanding of physics.  
**Translation:** Vocabulary: equations: 方程式; fascinated: 着迷; intuitive: 直觉的; intuitively: 直观地; lighting: 照明; liquids: 液体; unpack: 解析

**[1013.32s] English:** Well, that intuitive physics understanding is the base layer. That's the thing people sometimes call common sense. Again, it really understands something—and I think that really surprised a lot of people. It blows my mind that I just didn't think it would be possible to generate that level of realism without understanding.  
**Translation:** 

**[1032.14s] English:** There's this notion that you can only understand the physical world by having an embodied AI system—a robot that interacts with that world.  
**Translation:** Vocabulary: embodied: 具身化的; interacts: 交互

**[1040.46s] English:** That's the only way to construct an understanding of that world.  
**Translation:** 

**[1043.14s] English:** Yeah.  
**Translation:** 

**[1043.60s] English:** But VO3 is directly challenging that; it feels like.  
**Translation:** 

**[1047.88s] English:** Right. Yes. And it's very interesting; you know, even if you were to ask me five or ten years ago, I would have said, even though I was immersed in all of this, I would have said, "Well, yeah, you probably need to understand intuitive physics.  
**Translation:** Vocabulary: immersed: 沉浸其中

**[1058.12s] English:** You know, if I push this glass off the table, it will probably shatter, and the liquid will spill out, right? So we know all of these things.  
**Translation:** 

**[1067.14s] English:** But I thought that, you know, there are a lot of theories in neuroscience.  
**Translation:** Vocabulary: neuroscience: 神经科学; shatter: 碎裂

**[1070.02s] English:** It's called "action in perception," where, you know, you need to act in the world to really, truly perceive it in a deep way.  
**Translation:** 

**[1076.34s] English:** And there were a lot of theories about needing embodied intelligence or robots.  
**Translation:** Vocabulary: perceive: 认知; perception: 感知

**[1080.00s] English:** Or, something, or maybe at least simulated action so that you would understand things like intuition.  
**Translation:** 

**[1085.82s] English:** Physics, but it seems like you can understand it through passive observation, which is pretty.  
**Translation:** Vocabulary: intuition: 直觉; simulated: 模拟

**[1091.18s] English:** Surprising to me, and again, I think it hints at something underlying about the nature of reality.  
**Translation:** 

**[1097.26s] English:** In my opinion, beyond just the cool videos that it generates, of course,  
**Translation:** Vocabulary: generates: 产生

**[1103.72s] English:** There's the next stage, which might even involve making those videos interactive so one can actually step into them.  
**Translation:** 

**[1109.54s] English:** They and move around them, which would be really mind-blowing, especially given my game background.  
**Translation:** Vocabulary: interactive: 交互式的

**[1114.78s] English:** So, you can imagine, and then I think you know, we're starting to get towards what I  
**Translation:** 

**[1119.48s] English:** Would call a world model a model of how the world works, the mechanics of the world, and the physics of it.  
**Translation:** 

**[1124.76s] English:** The world, and the things in that world, and of course, that's what you would need for a true...  
**Translation:** 

**[1129.02s] English:** AGI system, I have to talk to you about video games. So, you were being a bit trolly, I think.  
**Translation:** Vocabulary: trolly: 爱搞恶作剧的

**[1135.10s] English:** You're having more and more fun on Twitter on X, which is great to see!  
**Translation:** 

**[1138.82s] English:** So,  
**Translation:** 

**[1139.54s] English:** A guy named Jimmy Apples tweeted, "Let me play a video game. I've already played three videos.  
**Translation:** 

**[1144.36s] English:** Google cooked up some really good playable world models when spelled W-E-N, and then you  
**Translation:** Vocabulary: jimmy: 吉米

**[1151.90s] English:** Quote" tweeted that, "with now wouldn't that be something?" So, how hard is it to build game worlds?  
**Translation:** 

**[1158.30s] English:** With AI, maybe you could look out into the future of video games five to ten years out: what do you think it will be like?  
**Translation:** 

**[1165.72s] English:** I think that looks like well, games were my first love, really, and  
**Translation:** 

**[1169.54s] English:** I think the next time I thought I wanted to have a computer, uh, putting it so I didn't.  
**Translation:** 

**[1172.54s] English:** Even though I didn't know how, I came to create games with a computer, which was for  
**Translation:** 

**[1172.80s] English:** The first-of-a-kind AI for games was the first thing I did professionally, and in  
**Translation:** 

**[1176.26s] English:** My teenage years, and it was the first major AI system that I built, and I  
**Translation:** 

**[1181.10s] English:** I always want to come back to that each day and scratch that itch.  
**Translation:** Vocabulary: scratch: 搔痒

**[1183.56s] English:** So, you know, and I'll do it. I think, and  
**Translation:** 

**[1185.90s] English:** I think I'd sort of dream about, you know, what would I have done back in the 90s.  
**Translation:** 

**[1193.08s] English:** If I had access to the kind of AI systems we have today, and I think you,  
**Translation:** 

**[1196.40s] English:** Could build absolutely mind-blowing games, and I think the next stages I  
**Translation:** 

**[1199.38s] English:** I'll open.  
**Translation:** 

**[1200.00s] English:** World games, so they're games where there's a simulation, and then there's AI characters.  
**Translation:** 

**[1205.56s] English:** Then, the player interacts with that simulation, and the simulation adapts to the way the player.  
**Translation:** 

**[1210.60s] English:** Plays, and I always thought they were the coolest games because, uh, games like Theme Park that I  
**Translation:** Vocabulary: adapts: 适应; interacts: 互动

**[1215.46s] English:** Worked on where everybody's game experience would be unique to them, right? Because you're kind of  
**Translation:** 

**[1220.20s] English:** Co-creating the game, right? We set up the parameters, we set up initial conditions, and  
**Translation:** 

**[1225.28s] English:** Then, you as the player are immersed in it, and you are co-creating it with the simulation.  
**Translation:** 

**[1230.38s] English:** But, of course, it's very hard to program open-world games; you know, you've got to be able to create  
**Translation:** Vocabulary: immersed: 身临其境

**[1235.08s] English:** Uh, content wherever the player goes, and you want it to be compelling no matter what.  
**Translation:** 

**[1239.60s] English:** The player chooses, um, and so it was always quite difficult to build things like cellular.  
**Translation:** Vocabulary: cellular: 蜂窝状的; compelling: 引人入胜的

**[1245.40s] English:** Automata are actually a type of those kind of classical systems which create some emergent behavior.  
**Translation:** 

**[1249.60s] English:** But they're always a little bit fragile, a little bit limited. Now, we're maybe on the cusp.  
**Translation:** Vocabulary: automata: 自动机; emergent: 涌现; fragile: 脆弱

**[1254.42s] English:** Next few years: five.  
**Translation:** 

**[1255.20s] English:** Ten years.  
**Translation:** 

**[1255.26s] English:** Ten years of having AI systems that can truly create around your imagination, um, can now sort  
**Translation:** 

**[1261.50s] English:** Of course, dynamically change the story and tell the narrative around it, making it dramatic no matter what.  
**Translation:** Vocabulary: dynamically: 灵活地

**[1267.14s] English:** What you end up choosing, so it's like the ultimate "choose your own adventure" sort of game, and uh, you  
**Translation:** 

**[1273.86s] English:** Know, I think maybe we're within reach if you think of an interactive version of Vo-uh, and then  
**Translation:** Vocabulary: interactive: 交互的

**[1279.00s] English:** Wind will forward five to ten years, and you know, imagine how good it's going to be.  
**Translation:** 

**[1283.98s] English:** Yeah, so you said a lot of.  
**Translation:** 

**[1285.18s] English:** Stuff there, so one of the open-world elements built into that is a deep personalization, as you've described.  
**Translation:** 

**[1292.82s] English:** It's not just that it's an open-world game; like, you can open any door, and there'll be something there.  
**Translation:** 

**[1297.96s] English:** It's that the choice of which door you open, in an unconstrained way, defines the worlds you see.  
**Translation:** 

**[1304.98s] English:** So, some games try to do that—they give you choices, yes, but it's really just an illusion of choice.  
**Translation:** Vocabulary: unconstrained: 不受限制的

**[1310.94s] English:** Because the only thing like Stanley Parable is  
**Translation:** 

**[1315.10s] English:** It's really just a couple of doors, and that's it.  
**Translation:** 

**[1320.00s] English:** Takes you down the narrative, Stanley Parable is a great video game. I recommend people play it.  
**Translation:** 

**[1323.72s] English:** That kind of, uh, in a meta way, mocks the illusion of choice, and there's philosophical.  
**Translation:** Vocabulary: parable: 比喻故事; philosophical: 哲学的

**[1330.72s] English:** Notions of free will and so on, but uh, I do like one of my favorite games, The Elder Scrolls Daggerfall.  
**Translation:** 

**[1337.08s] English:** Fall, I believe that they really played with a randomly generated dungeon, yeah.  
**Translation:** Vocabulary: daggerfall: 刀锋; dungeon: 地牢; notions: 观念; scrolls: 卷轴

**[1345.36s] English:** If you can step in, and they give you this feeling of an open world, and there, you mentioned  
**Translation:** 

**[1350.58s] English:** Interactivity: You don't need to interact — that's a first step, because you don't need to interact.  
**Translation:** 

**[1355.18s] English:** That much, you just when you open the door, whatever you see is randomly generated for you.  
**Translation:** 

**[1360.86s] English:** And that's already an incredible experience because you might be the only person to ever  
**Translation:** 

**[1365.46s] English:** See that, yeah, exactly. And so, but what you'd like is a little bit better than just sort of a  
**Translation:** 

**[1371.10s] English:** Random generation, right? So you'd like it to be better than a  
**Translation:** 

**[1375.16s] English:** Simple.  
**Translation:** 

**[1375.36s] English:** Choice: Right, that's not really an open world, as you say; it's just giving you the illusion.  
**Translation:** 

**[1382.68s] English:** Of choice, what you want to be able to do is potentially anything in that game environment.  
**Translation:** 

**[1386.50s] English:** Um, and I think the only way you can do that is to have generated systems systems that.  
**Translation:** 

**[1393.54s] English:** Uh, we'll generate that on the fly, of course, you can't create an infinite amount of game assets.  
**Translation:** 

**[1398.14s] English:** Right, it's expensive enough already. How tripling game costs like this were made today, and that was obvious to  
**Translation:** Vocabulary: infinite: 无尽的; tripling: 三倍增加

**[1402.88s] English:** To us back in the '90s, when I was working on all these games, and I was working on all these games.  
**Translation:** 

**[1405.36s] English:** I think maybe "Black and White" was the game that I worked on during its early stages, that had the  
**Translation:** 

**[1411.28s] English:** Still, probably the best AI learning AI; it was an early reinforcement learning system.  
**Translation:** 

**[1415.60s] English:** That you, you know, you were looking after this mythical creature and growing it.  
**Translation:** Vocabulary: reinforcement: 强化学习

**[1420.14s] English:** And nurturing it, and depending how you treated it, it would treat the villagers in that world accordingly.  
**Translation:** 

**[1425.18s] English:** The same way, so if you were mean to it, it would be mean; if you were good to it, it would be protective.  
**Translation:** Vocabulary: accordingly: 相应地; nurturing: 培养; villagers: 村民

**[1428.62s] English:** And so, it was really a reflection of the way you played it. So, actually, all of the... I've been  
**Translation:** 

**[1434.30s] English:** Working on sort of simulation games, and I've been working on sort of simulation games and I've been  
**Translation:** 

**[1435.36s] English:** Working on sort-of simulations and AI through the medium of games at the beginning of my career, and  
**Translation:** 

**[1440.00s] English:** And really, the whole of what I do today is still a follow-on from those early, more hard-coded ways of doing AI to now, you know, fully general learning systems that are trying to achieve the same thing.  
**Translation:** Vocabulary: simulations: 模拟

**[1451.82s] English:** Yeah, it's been interesting, hilarious, and fun to watch you and Elon, obviously itching to create games because you're both gamers.  
**Translation:** 

**[1460.36s] English:** And one of the sad aspects of your incredible success in so many domains of science, like serious adult stuff, is that you might not have time to really create a game.  
**Translation:** Vocabulary: hilarious: 滑稽; itching: 渴望

**[1472.28s] English:** You might end up creating the tooling, while others would create the game.  
**Translation:** 

**[1476.24s] English:** You have to watch others create the thing you've always dreamed of.  
**Translation:** 

**[1482.12s] English:** Do you think it's possible that, somehow, in your extremely busy schedule, you could find time to create something like black and white?  
**Translation:** 

**[1488.94s] English:** Some, some.  
**Translation:** 

**[1490.20s] English:** Yeah.  
**Translation:** 

**[1490.30s] English:** Yeah.  
**Translation:** 

**[1490.34s] English:** Yeah.  
**Translation:** 

**[1490.36s] English:** It's like an actual video game where, like, you could make your childhood dreams come true.  
**Translation:** 

**[1497.66s] English:** Well, you know, there are two things I think about: maybe with vibe coding getting better, there's a possibility that I could, you know, do that actually in my spare time.  
**Translation:** 

**[1506.22s] English:** So, I'm quite excited about that, as it would be my project if I had the time to do some vibe coding.  
**Translation:** 

**[1512.14s] English:** I'm actually itching to do that.  
**Translation:** 

**[1513.72s] English:** And then the other thing is: you know, maybe it's a sabbatical after AGI has been safely stewardied into the world and delivered into the world.  
**Translation:** Vocabulary: sabbatical: 休假; stewardied: 管理

**[1520.34s] English:** You know, that and then working on my physics theory, as we talked about at the beginning, those would be the two—my two post-AGI projects.  
**Translation:** 

**[1528.12s] English:** Let's call it that way.  
**Translation:** 

**[1528.88s] English:** I would love to see what the ultimate game post-AGI looks like, which you choose to solve the problem that some of the smartest people in human history have contended with.  
**Translation:** 

**[1538.64s] English:** So, P = MP, or creating a cool video.  
**Translation:** Vocabulary: contended: 争论过

**[1542.92s] English:** Yeah.  
**Translation:** 

**[1543.56s] English:** But in my world, they'd be related because it would be an open-world, simulated game as realistic.  
**Translation:** Vocabulary: simulated: 模拟的

**[1550.12s] English:** Realistic as possible.  
**Translation:** 

**[1551.36s] English:** So, you know, what is the universe?  
**Translation:** 

**[1553.98s] English:** That's that's speaking to the same question, right?  
**Translation:** 

**[1556.14s] English:** And P equals MP.  
**Translation:** Vocabulary: equals: 等于

**[1557.02s] English:** I think all these things are related, at least in my mind.  
**Translation:** 

**[1559.04s] English:** I mean, you know.  
**Translation:** 

**[1560.00s] English:** Really, in a serious way, it's like video games sometimes are looked down upon; there's just this fun side.  
**Translation:** 

**[1565.98s] English:** Activity, but especially as AI does more and more of the difficult and boring tasks, something we  
**Translation:** 

**[1575.06s] English:** Modern world called work, you know, but video games is the thing in which we may find meaning.  
**Translation:** 

**[1582.00s] English:** We may find it like what to do with our time, and you could create incredibly rich and meaningful experiences.  
**Translation:** 

**[1589.38s] English:** Like, that's what human life is, and then in video games, you can create more sophisticated, more  
**Translation:** 

**[1596.54s] English:** Diverse ways of living, yeah, I think so. I mean, those of us who love games—and I still do—are  
**Translation:** Vocabulary: sophisticated: 复杂的

**[1605.68s] English:** Um, you know, it's almost like letting your imagination run wild, right? Like, I used to love games, um,...  
**Translation:** 

**[1613.20s] English:** And they were working on games so much because it's the fusion, especially in the 1990s and the early 2000s.  
**Translation:** Vocabulary: fusion: 融合

**[1618.40s] English:** Sort of golden era.  
**Translation:** 

**[1619.36s] English:** And maybe in the 1980s, the gaming industry was all about discovering new things.  
**Translation:** 

**[1624.30s] English:** Genres Were Being Discovered, Weweren't Just Making Games; We Felt We Were Creating  
**Translation:** 

**[1627.92s] English:** A new entertainment medium that never existed before, especially with these open-world games.  
**Translation:** Vocabulary: genres: 类型

**[1632.40s] English:** And in simulation games, where you were co-creating the story with the game as the player.  
**Translation:** 

**[1636.22s] English:** There's no other media, or entertainment media, where you can do that as the audience.  
**Translation:** 

**[1641.20s] English:** Actually, co-create the story, and of course, now with multiplayer games as well, it can be a  
**Translation:** 

**[1646.22s] English:** Very social activity and  
**Translation:** 

**[1649.36s] English:** It's very important to also enjoy and experience the physical world, but the question is then:  
**Translation:** 

**[1660.22s] English:** You know, I think we're going to have to kind of confront the question again of what is the  
**Translation:** Vocabulary: confront: 面对

**[1663.48s] English:** Fundamental Nature of Reality: Uh, what is going to be the difference between these increasingly?  
**Translation:** 

**[1667.76s] English:** Realistic simulations and multiplayer ones, and emergent behavior—what we do in the real world.  
**Translation:** Vocabulary: simulations: 模拟

**[1675.20s] English:** Yeah, there's clearly a huge amount of value in experiencing really interesting games and  
**Translation:** 

**[1679.18s] English:** Experiencing the real world.  
**Translation:** 

**[1680.00s] English:** Nature, there's also a huge amount of value in experiencing other humans directly in person.  
**Translation:** 

**[1685.76s] English:** The way we're sitting here today, but we need to really scientifically and rigorously answer the  
**Translation:** Vocabulary: rigorously: 严格地; scientifically: 科学地

**[1691.52s] English:** Question: Why, yeah, and which aspect of that can be mapped into the virtual world exactly, and it's not?  
**Translation:** 

**[1698.44s] English:** It's not enough to say, "Yeah, you should go touch grass and hang out in nature." It's like, why exactly?  
**Translation:** 

**[1704.02s] English:** Is that valuable? Yes, and I guess that's maybe the thing that's been haunting me or obsessing me.  
**Translation:** 

**[1709.62s] English:** From the beginning of my career, if you think about all the different things I've done, that's  
**Translation:** Vocabulary: haunting: 困扰; obsessing: 痴迷

**[1712.90s] English:** They're all related in that way: the simulation nature of reality, and what are the bounds of you?  
**Translation:** 

**[1718.72s] English:** Know what can be modeled? Sorry for the ridiculous question, but so far, what is the greatest video game?  
**Translation:** Vocabulary: bounds: 界限; modeled: 建模

**[1723.40s] English:** Game of All Time: What's up there? Well, my favorite one of all time is Civilization. I have to say.  
**Translation:** 

**[1728.68s] English:** That was Civilization I and Civilization II—my favorite games of all time.  
**Translation:** 

**[1734.10s] English:** Um, I can only assume you've avoided the most recent one because it would probably  
**Translation:** 

**[1739.62s] English:** You would—that would be your sabbatical, where you would disappear, yes—exactly. They take a lot of  
**Translation:** 

**[1744.86s] English:** Time these civilization games; so, I've got to be careful with them. One question: you and Elon seem to  
**Translation:** 

**[1749.96s] English:** Is there a connection between being great at gaming and being somehow solid in other areas?  
**Translation:** 

**[1757.70s] English:** Great leaders of AI companies—I don't know, it's an interesting one. I mean, uh, we both love games.  
**Translation:** 

**[1763.68s] English:** And, uh, it's interesting that he wrote games as well. To start off with, it's probably especially relevant in the era,...  
**Translation:** 

**[1769.42s] English:** I grew up in I grew up in I grew up in I grew up in I grew up in I grew up in I grew up in  
**Translation:** 

**[1769.62s] English:** I grew up in the late '80s and '90s, when home computers were just becoming a thing.  
**Translation:** 

**[1774.28s] English:** Especially in the UK, I had a Spectrum, and then a Commodore Amiga 500, which is my favorite computer.  
**Translation:** 

**[1779.36s] English:** Ever, and that's why I learned all my programming. And of course, it's a very fun thing to program.  
**Translation:** Vocabulary: amiga: 阿美吉; commodore: Commodore

**[1784.96s] English:** Is to program games, so I think it's a great way to learn programming. Probably still is, and um, and  
**Translation:** 

**[1792.34s] English:** Then, of course, I immediately took it in directions of AI and simulations, which allowed me to.  
**Translation:** Vocabulary: simulations: 模拟

**[1797.08s] English:** Express my interest in games, and I think it's a great way to learn programming; I think it's  
**Translation:** 

**[1799.62s] English:** A great way to learn programming and experience playing games.  
**Translation:** 

**[1800.00s] English:** And my broader scientific interests, all together, and then the final thing I think that's  
**Translation:** 

**[1805.22s] English:** Great about games is that it fuses, um, artistic design—you know, art—with the most cutting-edge technology.  
**Translation:** Vocabulary: fuses: 融合

**[1813.16s] English:** Programming, um, so again in the 1990s, all of the most interesting technical advances were  
**Translation:** 

**[1819.18s] English:** Happening in gaming, whether that was AI, graphics, physics engines, or even GPUs, of course.  
**Translation:** Vocabulary: advances: 进展

**[1825.36s] English:** Were designed for gaming originally, um, so everything that was pushing computing forward.  
**Translation:** 

**[1829.98s] English:** In the 1990s, it was due to gaming, so interestingly, that was where the forefront.  
**Translation:** Vocabulary: computing: 计算; forefront: 前沿

**[1835.66s] English:** Of the research was going on, and it was this incredible fusion with art—um—you know, graphics, but also...  
**Translation:** 

**[1842.56s] English:** Music, and just the whole new medium of storytelling—I love that. For me, it's a sort of  
**Translation:** Vocabulary: fusion: 融合; storytelling: 叙事艺术

**[1847.66s] English:** A multidisciplinary kind of effort is something I've enjoyed my whole life.  
**Translation:** 

**[1852.20s] English:** I have to ask you; I almost forgot about it.  
**Translation:** Vocabulary: multidisciplinary: 跨学科的

**[1855.36s] English:** One of the many, and I would say one of the most incredible things recently, that somehow didn't  
**Translation:** 

**[1861.42s] English:** Yet, getting enough attention is alpha; we talked about evolution a little bit, but it's the  
**Translation:** Vocabulary: alpha: 阿尔法

**[1866.24s] English:** Google DeepMind's system that evolves algorithms, yeah—are these kinds of evolution-like techniques?  
**Translation:** 

**[1871.92s] English:** Promising as a component of future super-intelligence systems, so for people who don't  
**Translation:** Vocabulary: evolves: 演化

**[1875.76s] English:** Know, it's kind of like an LLM-guided evolutionary search, I don't think it's entirely fair to say it that way, though.  
**Translation:** 

**[1883.82s] English:** Evolution algorithms are the most incredible things that are promising in the future, super!  
**Translation:** Vocabulary: evolutionary: 进化的

**[1885.34s] English:** Algorithms are doing the search, and LMSs are telling you where—yes, exactly! So, LMSs are kind.  
**Translation:** 

**[1890.38s] English:** Of proposing some possible solutions, and then you use evolutionary computing on top to find...  
**Translation:** Vocabulary: proposing: 提出

**[1896.98s] English:** Some novel part of the search space, so actually I think it's an example of very promising.  
**Translation:** 

**[1903.04s] English:** Directions: Where you combine LLMs or foundation models with other computational techniques.  
**Translation:** Vocabulary: computational: 计算的

**[1909.74s] English:** Evolutionary methods is one, but you could also imagine Monte Carlo Tree Search, basically many.  
**Translation:** 

**[1915.34s] English:** Search algorithms or reasoning algorithms, sort of on top of or using,...  
**Translation:** 

**[1920.00s] English:** The foundation model as a basis, so I actually think there's quite a lot of interesting  
**Translation:** 

**[1924.82s] English:** Uh, things to be discovered probably with these sorts of hybrid systems—let's call them—  
**Translation:** Vocabulary: hybrid: 混合的

**[1929.44s] English:** But, not to romanticize evolution, yeah, I'm only human. But you think there's some value in whatever.  
**Translation:** 

**[1935.64s] English:** That mechanism is because we already talked about natural systems. Do you think where there's a lot,  
**Translation:** 

**[1941.64s] English:** Of low-hanging fruit in our understanding, being able to model and simulate.  
**Translation:** 

**[1948.06s] English:** Evolution, and using what we understand about that nature-inspired mechanism to then  
**Translation:** Vocabulary: simulate: 模拟

**[1955.30s] English:** Do a search better and better and better, yes. So, if you think about it again, breaking down the  
**Translation:** 

**[1960.28s] English:** Sort of systems we've built, uh, to their really fundamental core, you've got like the model of the  
**Translation:** 

**[1965.86s] English:** Of the underlying dynamics of the system, uh, and then if you want to discover something new.  
**Translation:** 

**[1971.38s] English:** Something novel that hasn't been seen before; then you need some kind of search process on top.  
**Translation:** 

**[1977.20s] English:** To take,  
**Translation:** 

**[1978.06s] English:** You can take them to a novel region of the search space, and you can do that in a number of ways.  
**Translation:** 

**[1984.30s] English:** Evolutionary computing is one way; with AlphaGo, we just use Monte Carlo tree search, right? And that's  
**Translation:** 

**[1990.02s] English:** What was found was a new kind of strategy in Go that had never been seen before, and that's how you can.  
**Translation:** Vocabulary: carlo: 蒙特卡洛; computing: 计算; evolutionary: 进化; monte: 蒙特

**[1996.90s] English:** Go beyond what is potentially already known, so the model can model everything that you currently know.  
**Translation:** 

**[2001.74s] English:** About right, all the data that you currently have, but then how do you go beyond that? So that starts.  
**Translation:** 

**[2006.22s] English:** To speak about the ideas of creativity.  
**Translation:** 

**[2008.06s] English:** How can these systems create something new or find/discover something novel? Obviously, this is surely challenging.  
**Translation:** 

**[2012.86s] English:** Relevant for scientific discovery or pushing science and medicine forward, which we want to.  
**Translation:** 

**[2017.02s] English:** To do with these systems, and you can actually bolt on some fairly simple search systems.  
**Translation:** 

**[2024.14s] English:** On top of these models, and get you into a new region of space; of course, you also have to.  
**Translation:** 

**[2030.06s] English:** Make sure that you're not searching that space totally randomly; it would be too big.  
**Translation:** 

**[2034.14s] English:** So, you have to have some objective function that you're trying to optimize, and hill-climb towards.  
**Translation:** 

**[2038.06s] English:** And that guides the search.  
**Translation:** Vocabulary: optimize: 使最优化

**[2040.00s] English:** But there's some mechanisms of evolution that are interesting, maybe in the space of programs, but then the space of programs is an extremely important space because you can probably generalize to everything.  
**Translation:** 

**[2050.90s] English:** But, you know, for example, mutation; it's not just a Monte Carlo tree search where it's like a search.  
**Translation:** Vocabulary: generalize: 泛化; mutation: 变异

**[2059.24s] English:** You could combine things, like components of a thing, every once in a while.  
**Translation:** 

**[2066.20s] English:** Yes.  
**Translation:** 

**[2066.34s] English:** So then, you know, what evolution is really good at is not just natural selection.  
**Translation:** 

**[2072.12s] English:** It's combining things and building increasingly complex hierarchical systems.  
**Translation:** Vocabulary: hierarchical: 等级制的

**[2078.18s] English:** So, that component is super interesting, especially with AlphaGo in the space of programs.  
**Translation:** 

**[2083.02s] English:** Yeah, exactly.  
**Translation:** 

**[2083.88s] English:** So, there's a way to get a bit of an extra property out of evolutionary systems, which is that some new emergent capability may come about.  
**Translation:** 

**[2091.00s] English:** Yes.  
**Translation:** Vocabulary: capability: 能力; emergent: 涌现的; evolutionary: 进化的

**[2091.14s] English:** Of course, as happened with life.  
**Translation:** 

**[2093.80s] English:** Interestingly, with a naive sort of traditionalism.  
**Translation:** Vocabulary: naive: 幼稚

**[2096.34s] English:** You know, evolution computing methods without LLMs and modern AI had their problems. The issues with them were very well studied in the 1990s and early 2000s, and they yielded some promising results.  
**Translation:** 

**[2106.58s] English:** But the problem was that they could never work out how to evolve new properties, new emergent properties.  
**Translation:** Vocabulary: computing: 计算; evolve: 演化; yielded: 产生

**[2111.90s] English:** You always had a sort of subset of the properties that you put into the system.  
**Translation:** 

**[2115.42s] English:** But maybe, if we combine them with these foundation models, perhaps we can overcome that limitation.  
**Translation:** 

**[2121.08s] English:** Obviously, natural evolution clearly did so because it evolved new capabilities.  
**Translation:** 

**[2126.28s] English:** Right.  
**Translation:** Vocabulary: capabilities: 能力; evolved: 进化

**[2126.34s] English:** So, from bacteria to where we are now.  
**Translation:** 

**[2128.70s] English:** So, clearly, it must be possible with evolutionary systems to generate new patterns. Going back to the first thing we talked about, new capabilities and emergent properties.  
**Translation:** 

**[2141.28s] English:** And maybe we're on the cusp of discovering how to do that.  
**Translation:** 

**[2144.92s] English:** Yeah.  
**Translation:** 

**[2145.26s] English:** Listen, Alpha Evolve is one of the coolest things I've ever seen on my desk at home.  
**Translation:** 

**[2150.26s] English:** You know, most of my time is spent on that computer just programming.  
**Translation:** Vocabulary: alpha: 初始版本

**[2154.38s] English:** And next to that,  
**Translation:** 

**[2156.26s] English:** The three screens is a skull of a TikTok, which.  
**Translation:** Vocabulary: skull: 头骨

**[2160.00s] English:** Which is one of the early organisms that crawled out of the water onto land.  
**Translation:** 

**[2165.64s] English:** And I just kind of watched that little guy.  
**Translation:** Vocabulary: crawled: 爬出

**[2170.46s] English:** It's like, whatever the computational mechanism of evolution is,  
**Translation:** 

**[2174.90s] English:** It's quite incredible.  
**Translation:** Vocabulary: computational: 计算的

**[2176.60s] English:** It's truly, truly incredible.  
**Translation:** 

**[2178.46s] English:** Now, whether that's exactly the thing we need to do for our search,  
**Translation:** 

**[2181.84s] English:** But never dismiss the power of nature; what it did here.  
**Translation:** 

**[2186.52s] English:** Yeah, and it's amazing.  
**Translation:** Vocabulary: dismiss: 忽视

**[2187.74s] English:** Um, which is a relatively simple algorithm, right?  
**Translation:** 

**[2191.46s] English:** Effectively, and it can generate all of this immense complexity that emerges,  
**Translation:** Vocabulary: algorithm: 算法; complexity: 复杂性; emerges: 出现; immense: 巨大的

**[2195.54s] English:** Obviously, running over you know, 4 billion years of time.  
**Translation:** 

**[2198.92s] English:** But, but it's you know, you can think about that as again, a process.  
**Translation:** 

**[2203.34s] English:** A search process that ran over the physics substrate of the universe for  
**Translation:** 

**[2207.16s] English:** A long amount of computational time.  
**Translation:** Vocabulary: substrate: 基础介质

**[2209.42s] English:** But then it generated all this incredible, rich diversity.  
**Translation:** 

**[2213.92s] English:** So, I have so many questions I want to ask you.  
**Translation:** 

**[2216.02s] English:** One, you do have a dream.  
**Translation:** 

**[2217.74s] English:** One of the natural systems you want to try to model is a cell.  
**Translation:** 

**[2222.62s] English:** Yes.  
**Translation:** 

**[2223.24s] English:** That's a beautiful dream.  
**Translation:** 

**[2224.70s] English:** Uh, I could ask you about that.  
**Translation:** 

**[2227.08s] English:** I also, just for that purpose on the AI scientist front, just broadly.  
**Translation:** Vocabulary: broadly: 宽泛地

**[2231.86s] English:** So there's an essay from Daniel Coccataglio, Scott Alexander, and others that  
**Translation:** 

**[2237.40s] English:** The outline includes steps along the way to get to ASI, and it has a lot of interesting ideas in it.  
**Translation:** Vocabulary: outline: 提纲

**[2242.82s] English:** One of which is, uh, including a superhuman coder and a  
**Translation:** 

**[2247.54s] English:** Superhuman AI researcher.  
**Translation:** 

**[2250.36s] English:** And in that, there's a term for research taste.  
**Translation:** 

**[2253.70s] English:** That's really interesting.  
**Translation:** 

**[2254.98s] English:** So, in everything you've seen, do you think it's possible for AI systems?  
**Translation:** 

**[2258.70s] English:** To have research taste to help you in the way that an AI co-scientist does.  
**Translation:** 

**[2265.42s] English:** Help steer human, brilliant scientists, and then potentially by.  
**Translation:** 

**[2272.92s] English:** Itself to figure out what directions you want to go?  
**Translation:** 

**[2277.42s] English:** How do you want to generate truly novel ideas?  
**Translation:** 

**[2280.00s] English:** To be like a really important component of how to do great science, yeah, I think that's going to be  
**Translation:** 

**[2285.00s] English:** One of the hardest things to mimic or model is this idea of taste or judgment, I think.  
**Translation:** 

**[2292.04s] English:** That's what separates the great scientists from the good ones, you know.  
**Translation:** Vocabulary: separates: 区分

**[2296.58s] English:** All professional scientists are good technically, right? Otherwise, it wouldn't have made it.  
**Translation:** 

**[2300.14s] English:** That far in academia, and things like that, but then do you have the taste to sort of sniff out what?  
**Translation:** Vocabulary: academia: 学术界; technically: 在技术上

**[2306.10s] English:** The right direction is what the right experiment is, which is what the right question is. So, the question is:  
**Translation:** 

**[2311.02s] English:** Picking the right question is the hardest part of science, um, and making the right hypothesis.  
**Translation:** Vocabulary: hypothesis: 假设

**[2316.24s] English:** And, um, that's what you know; today's systems definitely can't do it. So, I often...  
**Translation:** 

**[2322.30s] English:** Say it's harder to come up with a really good conjecture than it is to solve it.  
**Translation:** Vocabulary: conjecture: 猜测

**[2327.08s] English:** So, we may have systems soon that can solve pretty hard conjectures. Um, you know, I am in math.  
**Translation:** 

**[2333.04s] English:** Olympiad problems, where we, you know, alpha-proof.  
**Translation:** Vocabulary: conjectures: 猜想; olympiad: 奥林匹克

**[2335.86s] English:** You know, Alpha Proof.  
**Translation:** 

**[2336.08s] English:** In a year, our system got a silver medal for solving those really hard problems. Maybe eventually we'll...  
**Translation:** Vocabulary: alpha: 首字母

**[2340.96s] English:** Better at solving a Millennium Prize problem, but could a system come up with a conjecture?  
**Translation:** 

**[2346.64s] English:** Worthy of study, that someone like Terence Tao would have gone— you know, what that's a really  
**Translation:** Vocabulary: millennium: 千年

**[2350.80s] English:** A deep question about the nature of math, or the nature of numbers, or the nature of physics.  
**Translation:** 

**[2355.60s] English:** And that is a far harder type of creativity, and we don't really know today's systems clearly can't.  
**Translation:** 

**[2361.68s] English:** Do that, and we're not quite sure what that mechanism would be—this kind of leap of  
**Translation:** 

**[2365.84s] English:** Imagination.  
**Translation:** 

**[2366.08s] English:** Like, like Einstein had when he came up with, you know, special relativity and then general relativity.  
**Translation:** 

**[2371.44s] English:** With the knowledge he had at the time, as for conjecture, you want to come up with a thing?  
**Translation:** Vocabulary: einstein: 爱因斯坦; relativity: 相对论

**[2378.80s] English:** That's interesting; it's amenable to proof, yes. So, like, it's easy to come up with a thing that's  
**Translation:** 

**[2383.76s] English:** Extremely difficult, yeah. It's easy to come up with something that's extremely easy, but that at  
**Translation:** Vocabulary: amenable: 易于处理的

**[2387.84s] English:** That very end, that sweet spot, right? Basically, advancing the science and splitting.  
**Translation:** 

**[2392.40s] English:** The hypothesis space into two ideally; is it true, or not? It's going to be a  
**Translation:** Vocabulary: advancing: 推进; hypothesis: 假设; ideally: 理想地

**[2395.84s] English:** A little bit more complicated, but it's going to be a little bit more complicated, but it's going to be  
**Translation:** 

**[2400.00s] English:** And that's hard. And making something that's also, you know, falsifiable and within sort of the technologies that you have currently available is a very creative process, actually—a highly creative process—that I think just a kind of naive search on top of a model won't be enough for.  
**Translation:** Vocabulary: falsifiable: 可证伪的; naive: 幼稚的

**[2420.92s] English:** Okay, the idea of splitting the hypothesis space into super interesting. So I've heard you say that there's basically no failure in or failure is extremely valuable. If it's done right, if you construct the questions, right; if you construct the experiments, right; if you design them, right, that failure or success are both useful. So perhaps because it splits the hypothesis space too, it's like a binary search.  
**Translation:** 

**[2444.02s] English:** That's right. So, when you do, like, real blue-sky research, there's no such thing as failure, really, as long as you're picking it.  
**Translation:** Vocabulary: binary: 二分法; experiments: 实验; splits: 分割

**[2450.92s] English:** So, to go to your dream.  
**Translation:** 

**[2480.92s] English:** Of modeling a cell, what are the big challenges that lie ahead for us to make that happen? We should maybe highlight that AlphaFold solved, if it's fair to say, protein folding, and there are so many incredible things we could talk about there, including open sourcing, everything you've released. AlphaFold 3 is doing protein-RNA-DNA interactions, which is super complicated and fascinating — this is amenable to modeling AlphaGene.  
**Translation:** 

**[2510.92s] English:** Genome predicts how small genetic changes, like single mutations, link to actual function. So,  
**Translation:** 

**[2520.00s] English:** So, it seems like it's creeping along to much more complicated things, like a cell.  
**Translation:** Vocabulary: creeping: 缓慢进展; genome: 基因组; mutations: 突变

**[2527.24s] English:** But a cell has a lot of really complicated components.  
**Translation:** 

**[2530.50s] English:** Yeah. So, what I've tried to do throughout my career is that I have these really grand dreams.  
**Translation:** 

**[2535.56s] English:** And then I try to, as you've noticed, and then I try to break them down.  
**Translation:** 

**[2539.52s] English:** You know, it's easy to have a kind of crazy ambitious dream.  
**Translation:** 

**[2543.48s] English:** But the trick is: how do you break it down into manageable, achievable interim steps that are meaningful and useful in their own right?  
**Translation:** 

**[2552.80s] English:** And so, Virtual Cell, which is what I call the project of modeling a cell.  
**Translation:** Vocabulary: achievable: 可实现的; interim: 过渡的

**[2556.24s] English:** I've had this idea, you know, of wanting to do that for maybe 25 years.  
**Translation:** 

**[2561.18s] English:** And I used to talk with Paul Nurse, who is a bit of a mentor of mine in biology.  
**Translation:** Vocabulary: mentor: 导师

**[2565.44s] English:** He runs the Crick Institute, which he founded, and won the Nobel Prize in 2001.  
**Translation:** 

**[2572.08s] English:** We've been talking about it since.  
**Translation:** Vocabulary: nobel: 诺贝尔奖

**[2573.48s] English:** You know, before, in the '90s.  
**Translation:** 

**[2576.44s] English:** And I used to come back every five years. Is like, what would you need to model the full internals of a cell so that you could do experiments on the virtual cell, and what those experiments, you know, in silico, and those predictions would be useful for you to save you a lot of time in the wet lab, right?  
**Translation:** Vocabulary: experiments: 实验; internals: 内部; silico: 计算机

**[2592.78s] English:** That would be the dream.  
**Translation:** 

**[2593.58s] English:** Maybe you could 100x speed up experiments by doing most of it in silico, the search in silico, and then you do the validation step in the wet lab.  
**Translation:** Vocabulary: validation: 验证步骤

**[2601.04s] English:** That would be the dream.  
**Translation:** 

**[2603.36s] English:** And.  
**Translation:** 

**[2603.48s] English:** And so, but maybe now, finally, I was trying to build these components—alphaFold being one—that would allow you eventually to model the full interaction and a full simulation of a cell.  
**Translation:** 

**[2616.34s] English:** And I'd probably start with a yeast cell.  
**Translation:** 

**[2618.46s] English:** And partly that's what Paul Nurse studied, because the yeast cell is like a whole organism.  
**Translation:** 

**[2622.30s] English:** That's a single cell.  
**Translation:** Vocabulary: organism: 生物; yeast: 酵母

**[2623.50s] English:** Right.  
**Translation:** 

**[2623.78s] English:** So, it's the kind of simplest single-cell organism.  
**Translation:** 

**[2626.80s] English:** And so, it's not just a cell.  
**Translation:** 

**[2628.14s] English:** It's a full organism.  
**Translation:** 

**[2630.44s] English:** And yeast is very well understood.  
**Translation:** 

**[2633.10s] English:** And.  
**Translation:** 

**[2633.12s] English:** And so, that would be a good candidate for a kind of full simulated model.  
**Translation:** 

**[2637.94s] English:** Now, AlphaFold is the.  
**Translation:** Vocabulary: simulated: 模拟的

**[2640.00s] English:** Is the solution to the kind of static picture of what a protein looks like, its 3D-structured form?  
**Translation:** 

**[2645.02s] English:** Look like a static picture of it, but we know that in biology, all the interesting things happen.  
**Translation:** 

**[2649.46s] English:** With the dynamics and interactions. And that's what AlphaFold 3 is the first step toward.  
**Translation:** 

**[2654.46s] English:** Modeling those interactions. So, first of all, pairwise—proteins with proteins.  
**Translation:** Vocabulary: pairwise: 成对地

**[2659.04s] English:** Proteins with RNA and DNA. But then, the next step after that would be modeling maybe a whole pathway.  
**Translation:** 

**[2664.62s] English:** Maybe, like the TOR pathway that's involved in cancer, or something like this. And then eventually,...  
**Translation:** Vocabulary: pathway: 信号通路

**[2668.64s] English:** You might be able to model, you know, a whole cell. Also, there's another complexity here that.  
**Translation:** 

**[2673.32s] English:** Stuff in a cell happens at different timescales. Is that tricky? It's like, you know, protein.  
**Translation:** Vocabulary: complexity: 复杂性; timescales: 时间尺度; tricky: 棘手的

**[2679.34s] English:** Folding is, you know, super fast. Yes. I don't know all the biological mechanisms.  
**Translation:** 

**[2686.24s] English:** But some of them take a long time. Yeah. And so, that's a level. So, the levels of  
**Translation:** 

**[2690.24s] English:** Interaction has a different temporal scale that you have to be able to model. So, that would be  
**Translation:** 

**[2694.56s] English:** Hard. So, you'd probably need several simulated systems that can interact with each other.  
**Translation:** Vocabulary: temporal: 时间的

**[2698.64s] English:** Different temporal dynamics, or at least maybe it's like a hierarchical system. So,...  
**Translation:** 

**[2702.96s] English:** You can jump up and down through the different temporal stages. So, can you avoid one of the  
**Translation:** Vocabulary: hierarchical: 层次分明的

**[2710.14s] English:** Challenges here is not to avoid simulating, for example, the quantum mechanical aspects of anything.  
**Translation:** 

**[2717.66s] English:** Of this, right? You want to not over-model. You can skip ahead and just model the really high-level concepts.  
**Translation:** Vocabulary: quantum: 量子; simulating: 模拟

**[2724.24s] English:** Things that get you a really good estimate of what's going to happen. Yes, so you've got to  
**Translation:** 

**[2728.64s] English:** Make a decision when you're modeling any natural system. What is the cutoff level of the granularity?  
**Translation:** Vocabulary: cutoff: 阈值; estimate: 估算; granularity: 细分程度

**[2732.74s] English:** That you're going to model it to that, then captures the dynamics that you're interested in.  
**Translation:** 

**[2737.24s] English:** So, probably for a cell, I would hope that would be the protein level, and that one wouldn't have to go.  
**Translation:** 

**[2743.22s] English:** Down to the atomic level. So, you know, that's where AlphaFold really kicks in. So that  
**Translation:** 

**[2749.94s] English:** Would be kind of the basis, and then you'd build these higher-level simulations that take those as  
**Translation:** Vocabulary: simulations: 模拟

**[2757.04s] English:** Building blocks. And then.  
**Translation:** 

**[2758.64s] English:** You get the emergent behavior.  
**Translation:** Vocabulary: emergent: 涌现的

**[2760.98s] English:** Apologize in advance for the "pothead" questions, but do you think we'll be able to simulate a model of the origin of life?  
**Translation:** 

**[2771.30s] English:** So, being able to simulate the emergence of a living organism from non-living organisms, the birth of life.  
**Translation:** Vocabulary: emergence: 出现; organism: 有机体; simulate: 模拟

**[2779.74s] English:** I think that's one of the deepest and most fascinating questions, of course.  
**Translation:** 

**[2783.96s] English:** I love that area of biology.  
**Translation:** 

**[2785.56s] English:** You know, there's a great book by Nick Lane, one of the top experts in this area, called "The 10 Greatest Inventions of Evolution.  
**Translation:** 

**[2794.70s] English:** I think it's fantastic.  
**Translation:** 

**[2795.48s] English:** And it also speaks to what the great filters might be—prior or are they ahead of us?  
**Translation:** 

**[2800.74s] English:** I think they're most likely in the past if you read that book about how unlikely it is to go—have any life at all.  
**Translation:** 

**[2806.94s] English:** And then, from single-cell to multi-cell organisms, it seems like an unbelievably big jump that took about a billion years to occur on Earth, I think.  
**Translation:** 

**[2813.60s] English:** Right. So, it shows you how hard it was.  
**Translation:** Vocabulary: unbelievably: 难以置信地

**[2815.30s] English:** Right.  
**Translation:** 

**[2815.56s] English:** In theory, we're super happy for a very long time.  
**Translation:** 

**[2817.30s] English:** For a very long time before they captured mitochondria somehow, right?  
**Translation:** 

**[2820.54s] English:** I don't see why not; why AI couldn't help with that, some kind of simulation.  
**Translation:** Vocabulary: mitochondria: 线粒体

**[2825.70s] English:** Again, it's a bit of a search process through a combinatorial space.  
**Translation:** 

**[2830.10s] English:** Here's like all the, you know, chemical soup that you start with—the primordial soup that, you know, maybe was on Earth near these hot vents.  
**Translation:** Vocabulary: combinatorial: 组合; primordial: 原始; vents: 喷口

**[2837.66s] English:** Here's some initial conditions.  
**Translation:** 

**[2839.26s] English:** Can you generate something that looks like a cell?  
**Translation:** 

**[2842.32s] English:** So, perhaps that would be the next stage after the virtual cell project.  
**Translation:** 

**[2845.56s] English:** It is, well, how could something like that actually emerge from the chemical soup?  
**Translation:** 

**[2850.86s] English:** Well, I would love it if there were a move 37 for the origin of life.  
**Translation:** 

**[2854.44s] English:** Yeah.  
**Translation:** 

**[2854.74s] English:** I think that's one of the great mysteries.  
**Translation:** 

**[2857.82s] English:** I think, ultimately, what we'll figure out is that they're continuing.  
**Translation:** 

**[2860.22s] English:** There's no such thing as a line between non-living and living.  
**Translation:** 

**[2862.82s] English:** But if we can make that rigorous,  
**Translation:** Vocabulary: rigorous: 严格的

**[2864.62s] English:** Yes.  
**Translation:** 

**[2865.04s] English:** That the very thing, from the Big Bang to today, has been the same process.  
**Translation:** 

**[2869.82s] English:** If we can break down that wall that we've constructed in our minds about the actual origin of,  
**Translation:** 

**[2875.56s] English:** From non-living to living, and it's not a line; that's a continuum.  
**Translation:** 

**[2880.00s] English:** Next, in physics and chemistry and biology — and there's no line. I mean, this is my whole reason.  
**Translation:** 

**[2884.66s] English:** Why I worked on AI and AGI my whole life because I think it can be the ultimate tool to help us.  
**Translation:** 

**[2889.80s] English:** Answer these kinds of questions, and I don't really understand why, you know, for the average person.  
**Translation:** 

**[2895.42s] English:** Doesn't think like worrying about this stuff; more like how can we not have a good definition?  
**Translation:** Vocabulary: worrying: 忧虑

**[2901.06s] English:** Of life, and not living, and non-living, and the nature of time, and let alone consciousness.  
**Translation:** 

**[2907.00s] English:** Gravity and all these things—it's just quantum mechanics' weirdness. It's just, to me,  
**Translation:** Vocabulary: consciousness: 觉醒; gravity: 引力; quantum: 量子; weirdness: 奇异

**[2912.78s] English:** I've always had this sort of screaming at me in my face, the whole "I need that." It's getting  
**Translation:** 

**[2917.44s] English:** Louder, you know? It's like, "How is this going on here?" You know, in and I mean that in the deeper...  
**Translation:** 

**[2922.38s] English:** Sense, like in the nature of reality, which has to be the ultimate question, yeah, that.  
**Translation:** 

**[2927.52s] English:** Would answer all of these things—it's sort of crazy if you think about it—we can stare at each other for hours and still not exhaust all there is to say.  
**Translation:** Vocabulary: exhaust: 耗尽

**[2930.86s] English:** Other and all these living things; we can inspect them with microscopes and take them apart, all the time.  
**Translation:** 

**[2937.00s] English:** Down to the atomic level, and yet we still can't answer that clearly in a simple way—that question.  
**Translation:** Vocabulary: inspect: 检查; microscopes: 显微镜

**[2942.14s] English:** Of how do you define "living"? Yeah, it's kind of amazing. Living—you can kind of talk about it.  
**Translation:** 

**[2947.88s] English:** Way out of thinking about, but like consciousness—like, we have this very obviously subjective...  
**Translation:** 

**[2953.14s] English:** Conscious experience is like we're at the center of our own world, and it feels like something.  
**Translation:** 

**[2957.92s] English:** Then, how are you not screaming "at the mystery of it all"? Right? I mean, but really, humans...  
**Translation:** 

**[2964.70s] English:** Have we been contending with the mystery?  
**Translation:** 

**[2967.00s] English:** Of the world around them, for a long time, there are lots of mysteries, like what's up with  
**Translation:** Vocabulary: contending: 争论

**[2973.00s] English:** The sun and the rain, yeah—what's that about? Then, last year, we had a lot of.  
**Translation:** 

**[2979.10s] English:** Rain, and this year we don't have rain. Like, what did we do wrong? Humans have been asking that.  
**Translation:** 

**[2983.96s] English:** Question for a long time, so we're quite, I guess, we've developed a lot of mechanisms to cope with.  
**Translation:** 

**[2988.74s] English:** This, uh, these deep mysteries that we can't fully understand, even though we can see them.  
**Translation:** 

**[2994.22s] English:** Have to, have to just get on with daily life and...  
**Translation:** 

**[2997.00s] English:** We get so busy, right? In a way, did we keep ourselves distracted?  
**Translation:** Vocabulary: distracted: 分心

**[3000.00s] English:** I mean, weather is one of the most important questions in human history.  
**Translation:** 

**[3005.30s] English:** That's the go-to small talk direction about the weather.  
**Translation:** 

**[3010.06s] English:** Especially in England.  
**Translation:** 

**[3011.40s] English:** And then, which is famously an extremely difficult system to model.  
**Translation:** 

**[3017.08s] English:** And even that system, Google DeepMind has made progress on.  
**Translation:** 

**[3022.76s] English:** Yes, we've created the best weather prediction systems in the world.  
**Translation:** 

**[3027.04s] English:** And they're better than traditional fluid dynamics systems, which are usually calculated on massive supercomputers.  
**Translation:** 

**[3034.16s] English:** It takes days to calculate it.  
**Translation:** Vocabulary: supercomputers: 超级计算机

**[3036.22s] English:** We've managed to model a lot of the weather dynamics with neural network systems.  
**Translation:** 

**[3040.84s] English:** With our WeatherNet system.  
**Translation:** Vocabulary: neural: 神经的

**[3042.58s] English:** And again, it's interesting that those kinds of dynamics can be modeled.  
**Translation:** 

**[3046.44s] English:** Even though they're very complicated, almost bordering on chaotic systems in some cases.  
**Translation:** Vocabulary: bordering: 接近; chaotic: 混乱的; modeled: 建模

**[3050.64s] English:** A lot of the interesting aspects of that can be modeled by these neural network systems.  
**Translation:** 

**[3055.98s] English:** Including very,...  
**Translation:** 

**[3057.04s] English:** Very recently, we had, you know, cyclone predictions of where, you know, piles of hurricanes might go.  
**Translation:** 

**[3061.24s] English:** Of course, it's super useful and super important for the world.  
**Translation:** Vocabulary: cyclone: 气旋; hurricanes: 飓风

**[3063.90s] English:** And it's super important to do that very timely and very quickly.  
**Translation:** 

**[3066.78s] English:** And, in addition to accurately.  
**Translation:** 

**[3068.52s] English:** And I think it's a very promising direction, again, of simulating.  
**Translation:** 

**[3072.58s] English:** And so that you can run forward predictions and simulations of very complicated real-world systems.  
**Translation:** Vocabulary: simulating: 模拟; simulations: 模拟

**[3078.52s] English:** I should mention that I have a chance in Texas to meet a community of folks called the Storm Chasers.  
**Translation:** 

**[3084.98s] English:** Yes.  
**Translation:** Vocabulary: chasers: 追风暴的人; texas: 德克萨斯州

**[3085.16s] English:** And what's really incredible about...  
**Translation:** 

**[3087.04s] English:** I need to talk to them more.  
**Translation:** 

**[3088.62s] English:** They are extremely tech-savvy.  
**Translation:** 

**[3090.04s] English:** Because what they have to do is use models to predict where the storm is.  
**Translation:** 

**[3094.32s] English:** So, they're...  
**Translation:** 

**[3094.80s] English:** It's this beautiful mix of, like, crazy enough to, like, go into the eye of the storm.  
**Translation:** 

**[3100.82s] English:** And, like, in order to protect your life and predict where extreme events are going to be,  
**Translation:** 

**[3106.02s] English:** They have to have increasingly sophisticated models of weather.  
**Translation:** Vocabulary: sophisticated: 复杂的

**[3109.94s] English:** Yeah.  
**Translation:** 

**[3110.08s] English:** Yeah, it's a beautiful balance of, like, being in it as living organisms.  
**Translation:** 

**[3116.52s] English:** And the...  
**Translation:** 

**[3117.00s] English:** The cutting edge of science.  
**Translation:** 

**[3118.26s] English:** So, they actually might be using...  
**Translation:** 

**[3120.00s] English:** DeepMind system, so that's yeah; they hope they are, and I'd love to join them in one of.  
**Translation:** 

**[3124.34s] English:** Those cases look amazing, right? To actually experience it once, exactly, and then also to  
**Translation:** 

**[3129.02s] English:** Experience the correct prediction: yeah, where something will come and how it's going to evolve.  
**Translation:** Vocabulary: evolve: 演变

**[3134.00s] English:** It's incredible, yeah. You've estimated that we'll have AGI by 2030, um, so there's interesting...  
**Translation:** 

**[3141.68s] English:** Questions around that: How will we actually know that we got there? And what may be the move?  
**Translation:** 

**[3149.86s] English:** Quote: Move 37 of AGI, my estimate is sort of a 50% chance by in the next five years, so you know.  
**Translation:** 

**[3157.86s] English:** 2030, let's say, and uh, so I think there's a good chance that that could happen. Part of it is what?  
**Translation:** 

**[3163.66s] English:** Is your definition of AGI? Of course, people are arguing about that now, and mine's quite a high bar.  
**Translation:** 

**[3169.18s] English:** And always has it been about matching the cognitive functions that the brain has, right?  
**Translation:** Vocabulary: cognitive: 认知的

**[3174.26s] English:** We know our brains are pretty much general Turing machines, approximate, and of course,  
**Translation:** 

**[3179.86s] English:** We've created an incredible modern civilization with our minds, so that also speaks to how general the  
**Translation:** Vocabulary: approximate: 近似; turing: 图灵

**[3185.62s] English:** The brain is, and um, for us to know we have true AGI, we would have to make sure that it has all  
**Translation:** 

**[3192.54s] English:** Those capabilities aren't really a jagged intelligence, where some things it's really good.  
**Translation:** Vocabulary: capabilities: 能力; jagged: 参差不齐的

**[3196.82s] English:** At like today's systems, but other things it's really uh flawed, and that's what we  
**Translation:** 

**[3202.04s] English:** Currently, with today's systems, they're not consistent, so you'd want that consistency.  
**Translation:** Vocabulary: flawed: 有缺陷的

**[3206.10s] English:** Intelligence across the board, and then we have some missing, I think.  
**Translation:** 

**[3209.86s] English:** Capabilities like, sort of, uh, the true invention and creativity that we were talking about.  
**Translation:** 

**[3214.90s] English:** About earlier, so you'd want to see those. How you test that, um, I think you just test it one way to.  
**Translation:** 

**[3220.32s] English:** It would be a kind of brute-force test of tens of thousands of cognitive tasks, you know.  
**Translation:** 

**[3226.26s] English:** We know that humans can do, and maybe also make the system available to a few hundred of the world's  
**Translation:** 

**[3233.60s] English:** Top experts, such as Terence Towers from each subject area, and see if they can find out or confirm what you know.  
**Translation:** 

**[3239.86s] English:** The  
**Translation:** 

**[3240.00s] English:** After a month or two, and see if they can find an obvious flaw in the system. And if they can't, then I think  
**Translation:** 

**[3245.64s] English:** You're pretty, you know. You can be pretty confident; we have a fully general system.  
**Translation:** 

**[3250.82s] English:** Maybe to push back a little bit, it seems like humans are really incredible.  
**Translation:** 

**[3254.38s] English:** As the intelligence improves across all domains, we can take it for granted, as you mentioned, Terence.  
**Translation:** 

**[3261.72s] English:** Tau, uh, these brilliant experts might quickly, in a span of weeks, take for granted all the  
**Translation:** 

**[3269.48s] English:** Incredible things you can do, and then focus in. Ha! Right there, you know. I consider  
**Translation:** 

**[3274.38s] English:** Myself, uh, first of all, I am a human, yeah. Um, I identify as human. This, you know, some people listen.  
**Translation:** 

**[3284.90s] English:** To me, they're like that guy is not good at talking; the stuttering, you know, so like  
**Translation:** 

**[3290.80s] English:** Even humans have obvious limits across domains, even just outside of mathematics and physics, and  
**Translation:** Vocabulary: stuttering: 结巴

**[3297.74s] English:** So, on  
**Translation:** 

**[3299.48s] English:** I wonder if it will take something like a Move 37, so on the positive side, versus like.  
**Translation:** 

**[3305.84s] English:** A barrage of 10,000 cognitive tasks; where it would be one or two where it's like, "Yes, holy...  
**Translation:** 

**[3313.34s] English:** Shit, this is special. Exactly, so I think there's the sort of blanket testing to just make sure.  
**Translation:** Vocabulary: cognitive: 认知的

**[3318.22s] English:** You've got the consistency, but I think there are the sort of "lighthouse moments" like the move at 37.  
**Translation:** 

**[3325.02s] English:** That would involve looking for something like one being to invent a new control system, and the other would be  
**Translation:** 

**[3329.48s] English:** Inventing a game like Go, not just coming up with Move 37 or a new strategy, but can it invent a game that's  
**Translation:** 

**[3359.42s] English:** A new strategy, and then come up with a game that's a new strategy, and then come up with a new strategy.  
**Translation:** 

**[3359.48s] English:** That's deep.  
**Translation:** 

**[3360.00s] English:** As aesthetically beautiful as, or as elegant as Go. And those are the sorts of things I would be.  
**Translation:** Vocabulary: aesthetically: 审美上; elegant: 优雅的

**[3364.78s] English:** Looking out for them, and probably a system being able to do several of those things, right?  
**Translation:** 

**[3370.42s] English:** For it to be very general, not just one domain. And so I think that would be the sign.  
**Translation:** 

**[3375.64s] English:** At least, that is what I would be looking for: that we've got a system that's at the AGI level. And then maybe to...  
**Translation:** 

**[3381.36s] English:** Fill that out, you would also check for consistency and make sure there are no holes.  
**Translation:** 

**[3385.28s] English:** In that system, either. Yeah, something like a new conjecture or scientific discovery.  
**Translation:** 

**[3390.78s] English:** That would be a cool feeling. Yeah, that would be amazing. So, it's not just helping us do that,  
**Translation:** Vocabulary: conjecture: 猜测

**[3395.40s] English:** But actually, coming up with something brand new. And you would be in the room for that.  
**Translation:** 

**[3399.76s] English:** And so, it would be like probably two or three months before announcing it. And you would just...  
**Translation:** 

**[3406.14s] English:** Be sitting there trying not to tweet. Something like that. Exactly. It's like, what is this?  
**Translation:** 

**[3412.06s] English:** Amazing new physics idea. And then we would try.  
**Translation:** 

**[3415.28s] English:** Probably check it with world experts in that domain, right, and validate it before going.  
**Translation:** 

**[3421.12s] English:** Through its workings. And I guess it would be explaining its workings, too. Yeah, that would be amazing.  
**Translation:** Vocabulary: validate: 验证; workings: 运作

**[3427.06s] English:** Moment. Do you worry that we, as humans—even expert humans like you—might miss it? Well,  
**Translation:** 

**[3432.80s] English:** It may be pretty complicated. So, it could be the analogy I give there is: I don't think it will be.  
**Translation:** Vocabulary: analogy: 类比

**[3438.04s] English:** Totally mysterious to the best human scientists, but it may be a bit like, for example,...  
**Translation:** 

**[3444.86s] English:** In chess.  
**Translation:** 

**[3445.28s] English:** If I were to talk to Garry Kasparov or Magnus Carlsen and play a game with them, and they make  
**Translation:** 

**[3450.80s] English:** A brilliant move—I might not be able to come up with that move, but they could explain why.  
**Translation:** Vocabulary: carlsen: 卡尔森; garry: 加里; kasparov: 卡斯帕罗夫; magnus: 马格努斯

**[3455.40s] English:** Afterwards, that move made sense. And we would be able to understand it to some degree, not to the  
**Translation:** 

**[3460.14s] English:** They would do better. But, you know, if they were good at explaining, which is actually part of intelligence,  
**Translation:** 

**[3464.54s] English:** Too, is being able to explain in a simple way what you're thinking about. I think that  
**Translation:** 

**[3470.24s] English:** That will be very possible for the best human scientists. But I wonder—maybe you can.  
**Translation:** 

**[3474.22s] English:** Educate me on the side.  
**Translation:** 

**[3475.28s] English:** I wonder if there are any moves from Magnus or Garry where they at first will.  
**Translation:** 

**[3480.00s] English:** Dismiss it as a bad move, yeah, sure it could be, but then afterwards, they'll figure it out with their  
**Translation:** 

**[3486.36s] English:** Intuition that this works, and then empirically, the nice thing about...  
**Translation:** Vocabulary: dismiss: 忽视; empirically: 通过实验; intuition: 直觉

**[3490.90s] English:** Games is one of the great things about games; it's a sort of scientific test, does it?  
**Translation:** 

**[3495.00s] English:** Do you win the game, or not? And then, that tells you okay, that move in the end was good.  
**Translation:** 

**[3501.54s] English:** Strategy was good, and then you can go back and analyze that and explain it even to  
**Translation:** 

**[3506.28s] English:** Yourself a little bit more, why explore around it? And that's how chess analysis and things like that work.  
**Translation:** 

**[3511.36s] English:** That works, so perhaps that's why my brain works like that because I've been doing that since I  
**Translation:** 

**[3515.42s] English:** Was four, and you're trained — you know, it's sort of hardcore training in that way, but even now,...  
**Translation:** Vocabulary: hardcore: 严格的

**[3521.00s] English:** Like, when I generate code, there is this kind of nuanced, fascinating contention that's happening.  
**Translation:** 

**[3528.90s] English:** Where I might, at first, identify as a set of generated code is incorrect in some interesting ways.  
**Translation:** Vocabulary: contention: 争端; nuanced: 细腻的

**[3535.88s] English:** Nuance  
**Translation:** 

**[3536.26s] English:** Ways, but then I'm always have to ask the question: Is there a deeper insight here?  
**Translation:** Vocabulary: nuance: 细微差别

**[3541.80s] English:** That I'm the one who's incorrect, and that's going to be as the systems get more and more intelligent.  
**Translation:** 

**[3547.90s] English:** You're gonna have to contend with that. It's like, what? What is this—a bug or a feature? What you  
**Translation:** Vocabulary: contend: 应对

**[3553.68s] English:** Just came up with, yeah, and they're going to be pretty complicated to do, but of course it will be.  
**Translation:** 

**[3557.42s] English:** You can also imagine AI systems that are producing that code or whatever it is.  
**Translation:** 

**[3561.70s] English:** And then, human programmers looking at it, but also not unaided — with the help of —  
**Translation:** 

**[3566.26s] English:** AI tools, as well, so it's going to be kind of an interesting, you know, maybe different AI tools to  
**Translation:** Vocabulary: programmers: 编程人员; unaided: 未受辅助的

**[3571.66s] English:** The ones that they're more about, you know, are the ones that generate it.  
**Translation:** 

**[3575.84s] English:** So, if we look at an AGI system—sorry to bring it back up, but AlphaGo is super cool. So, Alpha  
**Translation:** Vocabulary: alpha: 初始

**[3583.74s] English:** Evolve enables, on the programming side, something like recursive self-improvement, uh, potentially.  
**Translation:** 

**[3590.42s] English:** Like, what if we can imagine what that AGI system might look like in a future version, but  
**Translation:** Vocabulary: evolve: 进化; recursive: 递归

**[3596.26s] English:** A few versions beyond that, what does that actually look like?  
**Translation:** 

**[3600.00s] English:** Do you think it will be simple?  
**Translation:** 

**[3601.44s] English:** Do you think it will be something like a self-improving program, and a simple one?  
**Translation:** 

**[3606.36s] English:** I mean, potentially that's possible, I would say.  
**Translation:** 

**[3608.52s] English:** I'm not sure it's even desirable, because that's a kind of hard takeoff scenario.  
**Translation:** 

**[3612.86s] English:** But these current systems, like Alpha Evolve, they have, you know, humans in the loop deciding.  
**Translation:** Vocabulary: scenario: 情景; takeoff: 起飞

**[3618.70s] English:** On various things.  
**Translation:** 

**[3620.20s] English:** They're separate hybrid systems that interact.  
**Translation:** Vocabulary: hybrid: 混合系统

**[3622.72s] English:** One could imagine eventually doing that end-to-end.  
**Translation:** 

**[3625.88s] English:** I don't see why that wouldn't be possible.  
**Translation:** 

**[3627.62s] English:** But right now, you know, I think the systems are not good enough to do that, in terms of  
**Translation:** 

**[3632.48s] English:** Coming up with the architecture of the code.  
**Translation:** 

**[3635.94s] English:** And again, it's a little bit connected to this idea of coming up with a new conjectural.  
**Translation:** 

**[3639.88s] English:** Hypothesis.  
**Translation:** Vocabulary: conjectural: 推测的; hypothesis: 假设

**[3641.28s] English:** They're good if you give them very specific instructions about what you're trying to do.  
**Translation:** 

**[3645.80s] English:** But if you give them a very vague, high-level instruction, that wouldn't work currently.  
**Translation:** 

**[3650.62s] English:** And I think that's related to this idea of inventing a game as good as Go, right?  
**Translation:** 

**[3654.96s] English:** Imagine that was the prompt.  
**Translation:** Vocabulary: prompt: 提示

**[3656.46s] English:** That's pretty undesperate.  
**Translation:** 

**[3657.62s] English:** And so, the current systems wouldn't know what to do with that, how to narrow  
**Translation:** Vocabulary: undesperate: 不绝望的

**[3662.40s] English:** That down to something tractable.  
**Translation:** 

**[3664.28s] English:** And I think there's something similar: look, just make a better version of yourself.  
**Translation:** Vocabulary: tractable: 易于处理的

**[3666.98s] English:** That's too unconstrained.  
**Translation:** 

**[3669.44s] English:** But we've done it, you know, and as you know, with Alpha Evolve, like things like  
**Translation:** Vocabulary: alpha: 测试版

**[3672.86s] English:** Faster Matrix Multiplication.  
**Translation:** 

**[3674.52s] English:** So, when you hone it down to a very specific thing you want, it's very good at incrementally.  
**Translation:** Vocabulary: incrementally: 逐步地; matrix: 矩阵; multiplication: 乘法

**[3680.48s] English:** Improving that.  
**Translation:** 

**[3681.30s] English:** But at the moment, these are more like incremental improvements, sort of small iterations.  
**Translation:** Vocabulary: incremental: 逐步的; iterations: 迭代

**[3685.74s] English:** Whereas, if you know, if you want to do a very specific thing, you want to do a very  
**Translation:** 

**[3687.62s] English:** Big leap in understanding, you need a much larger advance.  
**Translation:** 

**[3694.34s] English:** Yeah, but it could also be sort of to push back against a hard takeoff scenario.  
**Translation:** 

**[3697.94s] English:** It could be just a sequence of incremental improvements, like matrix multiplication.  
**Translation:** Vocabulary: scenario: 情景; takeoff: 起飞

**[3704.78s] English:** Like it has to sit there for days, thinking how to incrementally improve a thing.  
**Translation:** 

**[3709.96s] English:** And it does so recursively.  
**Translation:** Vocabulary: recursively: 递归地

**[3711.84s] English:** And as you do more and more improvements, it will slow down.  
**Translation:** 

**[3715.36s] English:** Right.  
**Translation:** 

**[3715.54s] English:** There'll be like a, like a...  
**Translation:** 

**[3717.62s] English:** The path to AGI won't be like a...  
**Translation:** 

**[3720.00s] English:** Be a gradual improvement over time. Yes. If it was just incremental improvements,  
**Translation:** 

**[3725.04s] English:** That's how it would look. So the question is: Could it come up with a new leap like the  
**Translation:** Vocabulary: gradual: 逐步的

**[3729.48s] English:** Transformers architecture? Could it have done that back in 2017 when we did it and Brain did it?  
**Translation:** 

**[3735.80s] English:** And it's not clear that these systems, something like AlphaVol, wouldn't be able to do, make such  
**Translation:** 

**[3741.16s] English:** A big leap. So, for sure, these systems are good. We have systems, I think, that can do incremental.  
**Translation:** 

**[3745.80s] English:** Hill climbing. And that's a kind of bigger question: is that all that's needed?  
**Translation:** 

**[3749.80s] English:** Here? Or do we actually need one or two more big breakthroughs? And can the same kind of  
**Translation:** 

**[3755.94s] English:** Systems provide the breakthroughs, too? So make it a bunch of S-curves, like incremental.  
**Translation:** Vocabulary: breakthroughs: 重大突破

**[3761.58s] English:** Improvement, but also every once in a while, leaps. Yeah. I don't think anyone has perfect systems.  
**Translation:** 

**[3766.66s] English:** That have shown unequivocally those big leaps. We have a lot of systems that do the hill climbing.  
**Translation:** Vocabulary: unequivocally: 毫无疑问地

**[3773.08s] English:** Of the S-curve that you're currently on, yeah.  
**Translation:** 

**[3775.80s] English:** And that would be Move 37. Yeah, I think it would be a leap; something like that.  
**Translation:** 

**[3781.40s] English:** Do you think the scaling laws are holding strong for pre-training, post-training, and test-time compute?  
**Translation:** 

**[3787.98s] English:** Do you, on the flip side of that, anticipate AI progress hitting a wall?  
**Translation:** Vocabulary: anticipate: 預期; compute: 計算

**[3793.16s] English:** We certainly feel there's a lot more room just in the scaling. So, actually, all steps,...  
**Translation:** 

**[3798.64s] English:** Pre-training, post-training, and inference time. So there are sort of three scalings that are  
**Translation:** Vocabulary: inference: 推断

**[3804.88s] English:** Happening concurrently.  
**Translation:** 

**[3805.80s] English:** And again, there, it's about how innovative you can be. And we pride ourselves on having the.  
**Translation:** Vocabulary: concurrently: 同时发生; innovative: 富有创新的

**[3813.72s] English:** Broadest and deepest research bench. We have amazing, incredible researchers, and people like:  
**Translation:** 

**[3821.18s] English:** Noam Shazea, who came up with Transformers, and Dave Silver, who led the AlphaGo project,  
**Translation:** Vocabulary: broadest: 最广泛的

**[3826.64s] English:** And so on. And that research base means that if a new breakthrough is required, like in AlphaGo,  
**Translation:** 

**[3835.80s] English:** For Transformers, I would have us be the place that does that.  
**Translation:** 

**[3840.00s] English:** You quite like it when the terrain gets harder, right? Because then it veers more from just...  
**Translation:** 

**[3844.38s] English:** Engineering, to truly research and you know, research plus engineering, and that's our sweet.  
**Translation:** Vocabulary: terrain: 地形; veers: 偏离

**[3850.24s] English:** Spot, and I think that's harder—it's harder to invent things than to, you know, fast.  
**Translation:** 

**[3856.38s] English:** Follow up, and um, so you know, we don't know; I would say it's kind of a 50-50 chance whether new things will happen.  
**Translation:** 

**[3863.62s] English:** Are we going to need more resources, or will scaling the existing stuff be enough? And so, in true...  
**Translation:** 

**[3868.98s] English:** Of empirical fashion, we're pushing both of those as hard as possible—the new blue-sky ideas—and you.  
**Translation:** Vocabulary: empirical: 经验的

**[3874.94s] English:** Know, maybe about half of our resources on that, and then scaling to the max the current...  
**Translation:** 

**[3880.58s] English:** The current capabilities are impressive, and we're still seeing some fantastic progress.  
**Translation:** Vocabulary: capabilities: 现有能力

**[3886.34s] English:** Each different version of Gemini, as you put it, is interesting in terms of the deep bench.  
**Translation:** 

**[3891.38s] English:** That if progress toward AGI is more than just scaling compute,  
**Translation:** Vocabulary: compute: 计算; gemini: 金星

**[3898.98s] English:** So, the engineering side of the problem is more on the scientific side, where there's  
**Translation:** 

**[3905.70s] English:** Breakthroughs are needed, then you'll feel more confident in DeepMind as well, Google's DeepMind.  
**Translation:** Vocabulary: breakthroughs: 重大进展

**[3910.36s] English:** Positioned to yes, kick ass in that domain. Well, I mean, if you look at the history of the last...  
**Translation:** 

**[3915.08s] English:** Decade or 15 years, um, it's been—I mean, you know—maybe I don't know 80-90 percent of the breakthroughs.  
**Translation:** 

**[3920.82s] English:** That more underpins the modern AI field today was originally from Google Brain, Google.  
**Translation:** 

**[3925.18s] English:** Research and DeepMind, so yeah, I would back that to continue hopefully.  
**Translation:** Vocabulary: underpins: 奠定基础

**[3928.98s] English:** Uh, so on the data side, are you concerned about running out of high-quality data, especially high?  
**Translation:** 

**[3935.14s] English:** Quality human data; I'm not very worried about that, partly because I think there's enough data.  
**Translation:** 

**[3940.14s] English:** Uh, and it's been proven to get the systems to be pretty good, and this goes back to simulations.  
**Translation:** 

**[3946.14s] English:** Again, if you do, you have enough data to make simulations, or so that you can create more.  
**Translation:** Vocabulary: simulations: 模拟

**[3951.40s] English:** Synthetic data that are from the right distribution, obviously, is the key. So, you need enough real.  
**Translation:** 

**[3957.40s] English:** World data in order to be able to do that, so I'm not very worried about that. I'm not very worried.  
**Translation:** 

**[3958.96s] English:** About that, so I'm not very worried about that. I'm not very worried about that. I'm not very worried.  
**Translation:** 

**[3960.00s] English:** Create those kinds of generator data generators, and I think we're at that step now.  
**Translation:** Vocabulary: generator: 发电器

**[3964.80s] English:** Moment, yeah. You've done a lot of incredible stuff on the side of science and biology.  
**Translation:** 

**[3968.60s] English:** Doing a lot with not so much data, yeah. I mean, it's still a lot of data, but I guess it's enough.  
**Translation:** 

**[3974.56s] English:** Take that, going exactly, yeah, exactly. How crucial is the scaling of compute to building?  
**Translation:** 

**[3981.14s] English:** This is a question that's an engineering question; it's almost a geopolitical question.  
**Translation:** Vocabulary: compute: 计算; crucial: 至关重要的; geopolitical: 地缘政治的

**[3987.62s] English:** Because it also integrates into supply chains and energy, yes, a thing that you care about.  
**Translation:** 

**[3994.72s] English:** A lot about which is, uh, potentially fusion, yes. Innovating on the side of energy, also, do you?  
**Translation:** Vocabulary: fusion: 核聚变; innovating: 创新; integrates: 整合

**[3999.58s] English:** I think we're going to keep scaling compute, I think so, for several reasons. I think compute, there's  
**Translation:** 

**[4004.68s] English:** There's the amount of compute you have for training, often it needs to be co-located.  
**Translation:** 

**[4008.86s] English:** Actually, even like you know, bandwidth constraints between data centers can affect that, so it's...  
**Translation:** 

**[4014.64s] English:** It's there are additional constraints, even there, and that.  
**Translation:** Vocabulary: bandwidth: 带宽; constraints: 限制

**[4017.62s] English:** That's important for training, obviously, the largest models you can, but there's also because  
**Translation:** 

**[4022.34s] English:** Now, AI systems are in products and being used by billions of people around the world. You need a ton.  
**Translation:** 

**[4028.66s] English:** Of inference computing now, um, and then on top of that, there are the thinking systems—the new paradigm.  
**Translation:** 

**[4034.52s] English:** Of the last year, that is, where they get smarter the longer amount of inference time you give them.  
**Translation:** Vocabulary: computing: 计算; inference: 推理; paradigm: 范式

**[4039.74s] English:** At test time, so all of those things need a lot of compute, and I don't really see that slowing down.  
**Translation:** 

**[4045.90s] English:** Um, and  
**Translation:** 

**[4047.62s] English:** As AI systems become better, they'll become more useful, and there'll be more demand for them.  
**Translation:** 

**[4051.56s] English:** So, both from the training side: the training side is actually only one part of that, and may even  
**Translation:** 

**[4055.98s] English:** Become the smaller part of what's needed, um, in the overall compute that is required.  
**Translation:** 

**[4062.20s] English:** Yeah, that's one sort of almost meme-y kind of thing, which is like the success and the incredible  
**Translation:** Vocabulary: compute: 计算

**[4067.40s] English:** Aspects of VO3: There's kind of a funny thing where, as it becomes more successful, people start making fun of it.  
**Translation:** 

**[4073.80s] English:** Know the servers are sweating, yes.  
**Translation:** 

**[4075.74s] English:** Yeah, yeah.  
**Translation:** 

**[4077.62s] English:** Exactly, we did a little video of what other  
**Translation:** 

**[4080.00s] English:** Of the servers frying eggs and things, and that's right. We're going to have to figure out  
**Translation:** 

**[4085.12s] English:** How to do that? Um, there are a lot of interesting hardware innovations that we do, as you know. We  
**Translation:** Vocabulary: innovations: 新技术

**[4089.48s] English:** We have our own TPU line, and we're looking at inference-only chips and  
**Translation:** 

**[4094.06s] English:** How can we make those more efficient? We're also very interested in building AI systems and we  
**Translation:** 

**[4098.08s] English:** Have we done any help with energy usage, such as for the cooling systems in data centers?  
**Translation:** 

**[4104.62s] English:** Be efficient, um, for grid optimization, um, and then eventually, things like helping with plasma.  
**Translation:** Vocabulary: optimization: 电网优化; plasma: 等离子

**[4111.14s] English:** Containment fusion reactors: we've done lots of work on that with Commonwealth Fusion, and also...  
**Translation:** 

**[4116.10s] English:** One could imagine reactor design, um, and then material design—I think—is one of the most exciting.  
**Translation:** Vocabulary: containment: 包容性; fusion: 融合

**[4121.26s] English:** New types of solar materials, such as solar panel material and superconductors that work at room temperature, have always  
**Translation:** 

**[4126.40s] English:** Been on my list of dream breakthroughs, and optimal batteries. And I think a solution to any.  
**Translation:** Vocabulary: breakthroughs: 重大突破; optimal: 最佳的; superconductors: 超导体

**[4132.22s] English:** You know, one of those things would be absolutely revolutionary.  
**Translation:** 

**[4134.62s] English:** For you know, climate and energy usage, and we're probably close, you know, and again, in the next.  
**Translation:** Vocabulary: revolutionary: 根本性的变革

**[4140.76s] English:** Five years to having AI systems that can materially help with those problems. If you were to bet, sorry.  
**Translation:** 

**[4146.46s] English:** For the ridiculous question, yeah, what is the main source of energy in like 20-30 to 40 years?  
**Translation:** Vocabulary: materially: 实质性地

**[4153.32s] English:** Do you think it's going to be nuclear fusion? I think fusion and solar are the two that I would consider.  
**Translation:** 

**[4159.02s] English:** Bet on solar, I mean. You know, it's the fusion reactor in the sky, of course, and I think  
**Translation:** 

**[4164.52s] English:** You know, I think it's going to be nuclear fusion, and I think it's going to be nuclear fusion.  
**Translation:** 

**[4164.60s] English:** And I think it's going to be nuclear fusion, and I think it's going to be nuclear fusion, and I think.  
**Translation:** 

**[4164.62s] English:** Really, the problem there is batteries and transmission, so you know, as well as more.  
**Translation:** 

**[4169.74s] English:** Efficient, more and more efficient solar materials—perhaps eventually—in space, you know.  
**Translation:** 

**[4173.98s] English:** These kinds of Dyson sphere-type ideas and fusion seem definitely doable. If we have...  
**Translation:** 

**[4181.50s] English:** The right design of the reactor, and we can control the plasma and do it fast enough, and so on, I think.  
**Translation:** Vocabulary: doable: 可行的; dyson: 迪松

**[4188.14s] English:** Both of those things will actually get solved, so we'll probably have at least those are probably.  
**Translation:** 

**[4191.98s] English:** The two primary sources of renewable energy, so I think it's going to be a really interesting.  
**Translation:** 

**[4194.60s] English:** And I think it's going to be a really interesting.  
**Translation:** 

**[4195.10s] English:** Almost free or perhaps free energy—what a time to be alive! If I  
**Translation:** 

**[4200.00s] English:** Traveled into the future with you, a hundred years from now, how much would you be surprised if we've  
**Translation:** 

**[4207.60s] English:** Passed a Type I Kardashev scale civilization, I would not be that surprised if there's a lot of advanced technology out there.  
**Translation:** Vocabulary: kardashev: 卡达舍夫文明

**[4214.62s] English:** Hundred-year time scale from here, I mean, I think it's pretty clear—if we crack the energy problems,...  
**Translation:** 

**[4219.68s] English:** In one of the ways we've just discussed, fusion or very efficient solar, then if energy is  
**Translation:** Vocabulary: fusion: 核聚变

**[4226.08s] English:** Kind of free, and renewable, and clean — um, then that solves a whole bunch of other problems, so for...  
**Translation:** 

**[4232.72s] English:** Example: The water access problem goes away because you can just use desalination, and we have the technology.  
**Translation:** Vocabulary: desalination: 淡化

**[4238.14s] English:** It's just too expensive, so only fairly wealthy countries like Singapore and Israel and  
**Translation:** 

**[4243.42s] English:** So, on the other hand, actually use it, but if it was really cheap, then you know, all countries would.  
**Translation:** Vocabulary: wealthy: 富有

**[4248.48s] English:** Have a coastline could also give you unlimited rocket fuel; you could just separate seawater out.  
**Translation:** 

**[4253.24s] English:** Into hydrogen and oxygen, using energy—and that's the kind of thing we're talking about.  
**Translation:** Vocabulary: coastline: 海岸; seawater: 海水; unlimited: 无限的

**[4256.08s] English:** That's rocket fuel, so, uh, combined with you know Elon's amazing self-landing rockets, then it could...  
**Translation:** 

**[4263.02s] English:** It would be like having a bus service to space, so that opens up incredible new resources.  
**Translation:** Vocabulary: rockets: 火箭

**[4269.12s] English:** And domains, uh, asteroid mining I think will become a thing, and maximizing human flourishing to the stars.  
**Translation:** 

**[4274.72s] English:** Like, that's what I dream about, as well as Carl Sagan's sort of idea of bringing consciousness.  
**Translation:** Vocabulary: asteroid: 小行星; consciousness: 意识; flourishing: 繁荣; maximizing: 最大化

**[4279.80s] English:** To the universe, waking it up; I think human civilization will do that in the full sense.  
**Translation:** 

**[4285.20s] English:** Of time, if we get.  
**Translation:** 

**[4286.08s] English:** AI, right, and uh, and and and, let's crack some of these problems with it, yeah. I wonder what it would look like.  
**Translation:** 

**[4291.68s] English:** Like, if you were just a tourist flying through space, you would probably notice Earth because if you  
**Translation:** 

**[4298.22s] English:** Solve the energy problem, and you would see a lot of space rockets probably, so it would be like traffic.  
**Translation:** 

**[4303.28s] English:** Here in London, but in space, yes, it's just a lot of rockets, yes, and then you would probably see.  
**Translation:** 

**[4310.22s] English:** Floating in space, some kind of source of energy like solar—yeah, potentially. So Earth would just...  
**Translation:** 

**[4316.08s] English:** Look more on the surface, more um, technological.  
**Translation:** 

**[4320.00s] English:** And then you would use the power of that energy to preserve the natural.  
**Translation:** 

**[4324.92s] English:** Yes, like the rainforest and all that stuff, because for the first time in human history, we wouldn't.  
**Translation:** Vocabulary: rainforest: 热带雨林

**[4331.08s] English:** Be resource-constrained, and I think that could be an amazing new era for humanity where it's not.  
**Translation:** 

**[4338.46s] English:** Zero-sum, right? I have this land, you don't have it. Or if we take, you know, if the tigers have their...  
**Translation:** 

**[4344.30s] English:** Forest, then the local villagers will wonder what they are going to use it for, I think that this will.  
**Translation:** 

**[4349.88s] English:** Help a lot, no; it won't solve all problems because there's still other human foibles that will.  
**Translation:** Vocabulary: foibles: 缺点; villagers: 村民

**[4355.00s] English:** Will still exist, but it will at least remove one—I think—one of the big vectors.  
**Translation:** 

**[4359.90s] English:** Scarcity of resources, you know, including land, and more materials and energy, and, um, you know, we  
**Translation:** Vocabulary: scarcity: 资源匮乏; vectors: 风险因素

**[4366.54s] English:** Should be: I sometimes call it "like," and others call it "about" this kind of radical abundance era.  
**Translation:** 

**[4370.12s] English:** Where, um, there are plenty of resources to go around, of course, the next big  
**Translation:** 

**[4374.22s] English:** The question is: What is the next big question, and the next big question is: what is the next big?  
**Translation:** 

**[4374.28s] English:** Is making sure that it's fairly, you know, shared and that everyone in society benefits from.  
**Translation:** 

**[4380.40s] English:** That, so, there is something about human nature where I go—you know—it's like Borat, like my.  
**Translation:** 

**[4386.72s] English:** Neighbors, like I like you to start trouble; we do start conflicts, and that's why games throughout.  
**Translation:** 

**[4395.30s] English:** As I'm learning, actually, more and more, even ancient history serves the purpose of pushing.  
**Translation:** 

**[4400.36s] English:** People away from war are generally safer, so maybe.  
**Translation:** 

**[4404.20s] English:** We can figure out increasingly sophisticated video games that pull us in; they give us that.  
**Translation:** 

**[4410.14s] English:** Uh, that scratches the itch of like conflict, whatever that is about, us and our human nature, and then...  
**Translation:** Vocabulary: scratches: 挠痒; sophisticated: 复杂的

**[4418.84s] English:** Avoid the actual hot wars that would come with increasingly sophisticated technologies.  
**Translation:** 

**[4426.28s] English:** We're now well past the stage where the weapons we are able to create can actually just  
**Translation:** 

**[4431.48s] English:** Destroy all of human civilization, so it's no longer.  
**Translation:** 

**[4434.20s] English:** Um, that's no longer a great way to start.  
**Translation:** 

**[4439.88s] English:** Sharing,  
**Translation:** 

**[4440.00s] English:** It's better to play a game of chess or football with your neighbor, yeah, and I.  
**Translation:** 

**[4445.44s] English:** I think I mean, I think that's what my modern sport is, so, and I love watching football, and.  
**Translation:** 

**[4450.58s] English:** Just feel like, uh, and I used to play it a lot as well. It's very visceral.  
**Translation:** Vocabulary: visceral: 直觉的

**[4456.36s] English:** And it's tribal, and I think it does channel a lot of those energies into that, which I think is a kind  
**Translation:** 

**[4461.58s] English:** Of human need to belong to some group, and, um, but into a fun, healthy way, and  
**Translation:** Vocabulary: energies: 能量; tribal: 部落的

**[4469.88s] English:** And, a non-destructive, kind of constructive way, and I think going back,  
**Translation:** 

**[4474.60s] English:** To games again, I think they're originally why they're so great as well for kids to play.  
**Translation:** 

**[4478.52s] English:** Things like chess are great little microcosms of the world; they're  
**Translation:** 

**[4482.76s] English:** Simulations of the world are too simplified versions of some real-world situations, whether...  
**Translation:** Vocabulary: microcosms: 小世界; simplified: 简化的; simulations: 模拟

**[4486.36s] English:** It's poker, or Go, or chess—different aspects of diplomacy, or different aspects of the real world.  
**Translation:** 

**[4492.92s] English:** And it allows you to practice them, too. And because, you know, how many times do you get to?  
**Translation:** Vocabulary: diplomacy: 外交; poker: 纸牌游戏

**[4498.32s] English:** Practice a massive decision moment.  
**Translation:** 

**[4499.88s] English:** In your life, you know what job to take, what university to go to. You know, maybe I don't.  
**Translation:** 

**[4504.42s] English:** Know a dozen or so key decisions, and you've got to make those as best as you can.  
**Translation:** 

**[4509.12s] English:** And games are a kind of safe, repeatable environment where you can get better.  
**Translation:** 

**[4514.02s] English:** At your decision-making process, um, and it might have this additional benefit of channeling some.  
**Translation:** 

**[4519.88s] English:** Energies should be directed into more creative and constructive pursuits, well, I think it's also  
**Translation:** Vocabulary: channeling: 引导; pursuits: 活动

**[4524.98s] English:** It's really important to practice losing and winning, right? Like losing.  
**Translation:** 

**[4529.88s] English:** Is a really fun game, you know? That's why I love games. That's why I love even things like, uh, Brazilian  
**Translation:** 

**[4534.62s] English:** Jiu-jitsu, yeah, where you can get your ass kicked in a safe environment over and over; it reminds you.  
**Translation:** 

**[4540.46s] English:** About the way physics works, about the way the world operates, about sometimes losing sometimes.  
**Translation:** 

**[4545.74s] English:** You win, you can still be friends with everybody, yeah. That feeling of losing, I mean, it's a  
**Translation:** 

**[4552.28s] English:** Weird one for us humans to like, really try to make sense of. Like, that's just part of life; that is a.  
**Translation:** 

**[4558.24s] English:** A fundamental part of life is losing.  
**Translation:** 

**[4559.88s] English:** You.  
**Translation:** 

**[4560.00s] English:** Yeah. And I think the martial arts, as I understand it, but also in things like light.  
**Translation:** 

**[4563.68s] English:** Chess, at least the way I took it, is a lot about self-improvement and self-knowledge.  
**Translation:** Vocabulary: martial: 武术

**[4568.66s] English:** You know, that okay, so I did this thing. It's not really about being the other person.  
**Translation:** 

**[4573.50s] English:** It's about maximizing your own potential. If you do it in a healthy way, you learn to use  
**Translation:** Vocabulary: maximizing: 发挥最大潜能

**[4578.36s] English:** Victory and losses, don't get carried away with victory and think you're just the best.  
**Translation:** 

**[4583.94s] English:** In the world, and the losses keep you humble, always reminding you that there's always something more to learn.  
**Translation:** 

**[4589.10s] English:** Learn. There's always a bigger expert that you can learn from. You know, I think you learn that.  
**Translation:** 

**[4593.52s] English:** I'm pretty sure in martial arts. And, and, and I think that's also the way that at least I was.  
**Translation:** 

**[4598.84s] English:** Trained in chess. And so, in the same way, it can be very hardcore and very important. And of  
**Translation:** 

**[4603.44s] English:** Course, you want to win, but you also need to learn how to deal with setbacks in a healthy way.  
**Translation:** Vocabulary: hardcore: 极其严肃; setbacks: 挫折

**[4608.60s] English:** That, and, and, and, and why are those feelings that you have when you lose something.  
**Translation:** 

**[4612.78s] English:** Into a constructive thing for next time, I'm going to improve this, right, or get better at it.  
**Translation:** 

**[4617.72s] English:** There is something,  
**Translation:** 

**[4619.10s] English:** There's a source of happiness, a source of meaning. It's not about improvements.  
**Translation:** 

**[4623.00s] English:** The winning or losing. Yeah. It's the mastery. Yeah. There's nothing more satisfying, in a way.  
**Translation:** 

**[4627.12s] English:** It's like, "Oh wow, this thing I couldn't do before; now I can." And, and again, games and physical.  
**Translation:** Vocabulary: mastery: 精通

**[4632.86s] English:** Sports and mental sports: their way, their ways of measuring—they're beautiful because you can  
**Translation:** 

**[4637.18s] English:** Measure that, that progress. Yeah. I mean, there's something about—I guess why I love role-playing.  
**Translation:** 

**[4641.84s] English:** Games. Like the number goes up on the skill tree—literally, that is a source of  
**Translation:** 

**[4648.00s] English:** The meaning for us humans.  
**Translation:** 

**[4649.10s] English:** Yeah. We're quite addicted to seeing these numbers go up, and,  
**Translation:** 

**[4653.74s] English:** Uh, and and maybe that's why we made games like that because obviously that is something.  
**Translation:** Vocabulary: addicted: 上瘾

**[4658.46s] English:** We're, we're, we're hill-climbing systems ourselves, right? Yeah. It would be quite sad if we didn't.  
**Translation:** 

**[4663.66s] English:** Have any mechanism, but we do this everywhere, right? Where we just have this thing that  
**Translation:** 

**[4670.70s] English:** I don't want to dismiss that; it is a source of deep meaning for us humans.  
**Translation:** 

**[4675.02s] English:** So, one of the incredible stories on the business and leadership side is, uh,  
**Translation:** Vocabulary: dismiss: 轻视

**[4679.10s] English:** What about Google?  
**Translation:** 

**[4680.00s] English:** Has done over the past year. So, I think it's fair to say that Google was losing on the LLM product.  
**Translation:** 

**[4687.44s] English:** Side a year ago with Gemini 1.5, and now it's winning with Gemini 2.5. And you took the helm.  
**Translation:** 

**[4694.04s] English:** And you led this effort. What did it take to go from, let's say, "losing" to "quote"?  
**Translation:** Vocabulary: gemini: 双子座

**[4699.08s] English:** Unquote, winning in the span of a year? Yeah, well, firstly, it's absolutely incredible teamwork.  
**Translation:** 

**[4704.68s] English:** That we have, you know, been led by Corey and Jeff Dean, and Oriol, and the amazing team we have.  
**Translation:** Vocabulary: corey: 科里; firstly: 首先; teamwork: 团队合作

**[4710.26s] English:** On Gemini. Absolutely world-class. So, you can't do it without the best talent. And of course,  
**Translation:** 

**[4717.10s] English:** You know, we have a lot of great computing power as well. But then it's the research culture we  
**Translation:** Vocabulary: computing: 计算能力

**[4721.84s] English:** Created. Right. And basically, coming together, both different groups at Google, you know,  
**Translation:** 

**[4727.52s] English:** There was Google Brain, a world-class team, and then the old DeepMind, pulling together all.  
**Translation:** 

**[4732.50s] English:** The best people and the best ideas.  
**Translation:** 

**[4734.68s] English:** And gathering around to make the absolute greatest system we could. And it was hard. But we're  
**Translation:** 

**[4741.98s] English:** All very competitive. And we, you know, love research. This is so much fun to do. And we, you know,  
**Translation:** 

**[4749.20s] English:** It's great to see that our trajectory wasn't a given. But we're very pleased with where we are in.  
**Translation:** Vocabulary: trajectory: 发展趋势

**[4754.86s] English:** The rate of progress is the most important thing. So, if you look at where we've come from two  
**Translation:** 

**[4759.46s] English:** Years ago, to one year ago, and now, you know, I think we call it relentless progress.  
**Translation:** Vocabulary: relentless: 毫不懈怠的

**[4764.68s] English:** Along with the relentless shipping of that progress, we are being very successful. And, you know,...  
**Translation:** 

**[4770.68s] English:** Unbelievably competitive, the whole space—especially the AI space—with some of the greatest  
**Translation:** Vocabulary: unbelievably: 难以置信地

**[4775.76s] English:** Entrepreneurs and leaders, and companies in the world, are all competing now, because everyone's  
**Translation:** 

**[4781.30s] English:** Realized how important AI is. And it's very pleasing for us to see that progress.  
**Translation:** Vocabulary: entrepreneurs: 企业家

**[4787.42s] English:** You know, Google is a gigantic company. Can you speak to the natural things that happen there?  
**Translation:** 

**[4792.04s] English:** The case is the bureaucracy that emerges; you want to be able to, you know, be able to, you know.  
**Translation:** Vocabulary: bureaucracy: 官僚主义; emerges: 出现; gigantic: 巨大的

**[4794.66s] English:** Be careful, like, you know, the natural kind of thing, there's me.  
**Translation:** 

**[4800.00s] English:** Meetings and there's managers, and that—like, what are some of the challenges from a leadership perspective when it comes to breaking through that in order to, as you said, ship more products? The number of Gemini-related products shipped over the past year is just insane.  
**Translation:** 

**[4813.88s] English:** Right. It is. Yeah, exactly. That's what relentlessness looks like. I think it's a question of, like, any big company—you know—ends up having a lot of layers of management and things like that; is sort of the nature of how it works.  
**Translation:** 

**[4828.72s] English:** Um, but I still operate, and I was always operating with Old Deep Mind as a, as a startup—still large, one, but still as a startup. And that's what we still act like today, as with Google Deep Mind, and acting with decisiveness and the energy that you get from the best smaller organizations.  
**Translation:** Vocabulary: decisiveness: 果断; relentlessness: 坚持不懈

**[4846.18s] English:** And we try to get the best of both worlds: where we have this incredible billion-plus users, surfaces, and incredible products that we can power up with our AI and our research.  
**Translation:** 

**[4857.54s] English:** And that's amazing.  
**Translation:** 

**[4858.72s] English:** And you can, you know, that's very few places in the world.  
**Translation:** 

**[4860.90s] English:** You can get that: on one hand, do incredible world-class research, and on the other hand, plug it in and improve billions of people's lives the next day.  
**Translation:** 

**[4867.82s] English:** Uh, that's a pretty amazing combination, and we're continually fighting and cutting away bureaucracy to allow the research culture and the relentless shipping culture to flourish.  
**Translation:** 

**[4878.84s] English:** And I think we've got a pretty good balance while being responsible with it—you know, as you have to be, as a large company—and also, with a number of huge projects.  
**Translation:** Vocabulary: bureaucracy: 官僚主义; flourish: 繁荣; relentless: 不屈不挠的

**[4888.72s] English:** Uh, so a funny thing you mentioned about the surface with a billion—I had a conversation with a guy named, um, a brilliant guy here at the British Museum called Irvin Finkel.  
**Translation:** 

**[4899.90s] English:** He's a world expert in Kinea forms, which is an ancient writing on tablets.  
**Translation:** 

**[4906.74s] English:** And he doesn't know about Chad GPT or Gemini.  
**Translation:** 

**[4911.24s] English:** He doesn't even know anything about AI, but his first encounter with this AI was in AI mode on Google.  
**Translation:** Vocabulary: encounter: 遇见; gemini: Gemini

**[4917.64s] English:** Yes.  
**Translation:** 

**[4918.12s] English:** He's like,  
**Translation:** 

**[4918.72s] English:** Is that what you're talking about?  
**Translation:** 

**[4920.00s] English:** This AI mode, and you know, it's just a reminder that there's a large part of the world...  
**Translation:** Vocabulary: reminder: 提示

**[4926.22s] English:** That doesn't know about this AI thing, yeah, I know it's funny because if you live on Twitter and X,...  
**Translation:** 

**[4931.76s] English:** And I mean, it's sort of like, at least in my feed, it's all AI, and there are certain places where you know.  
**Translation:** 

**[4936.32s] English:** In the valley, and in certain pockets where everyone's just all they're thinking about is AI, but a lot of  
**Translation:** 

**[4941.88s] English:** The normal world hasn't come across it yet, but that's a great responsibility to.  
**Translation:** 

**[4946.10s] English:** Their first interaction, yeah, um, was on the grand scale of rural India—or anywhere across the country.  
**Translation:** 

**[4953.06s] English:** World, right? And we want it to be as good as possible, and in a lot of cases, it's just under the  
**Translation:** 

**[4957.50s] English:** Hood is powering making something like maps or search work better, and it's ideally for a lot of.  
**Translation:** 

**[4964.20s] English:** Those people should just be seamless; it's just new technology that makes their lives more, you know.  
**Translation:** Vocabulary: ideally: 最合适; seamless: 无缝的

**[4968.42s] English:** Productive, and it helps a bunch of folks on the Gemini product and engineering teams.  
**Translation:** 

**[4973.00s] English:** Spoken extremely highly of you on another dimension.  
**Translation:** Vocabulary: dimension: 维度

**[4975.88s] English:** That I almost didn't even expect, because I kind of think of you as a deep scientist and  
**Translation:** 

**[4983.00s] English:** Caring about these big, research scientific questions, but they also said, "You're a great...  
**Translation:** Vocabulary: caring: 关心

**[4986.72s] English:** A product guy likes how to create a thing that a lot of people would use and enjoy using, so  
**Translation:** 

**[4992.04s] English:** Can you maybe speak to what it takes to create an AI-based product that a lot of people don't?  
**Translation:** 

**[4998.14s] English:** Enjoy using, yeah. Well, I mean, again, that comes back from my game design days where I used to design.  
**Translation:** 

**[5002.58s] English:** Games for millions of gamers; people forget about that.  
**Translation:** 

**[5005.88s] English:** I've had experience with cutting-edge technology in products, like those used in gaming.  
**Translation:** 

**[5011.00s] English:** In the 90s, and so I love the combination of cutting-edge research and then seeing it applied.  
**Translation:** 

**[5017.56s] English:** In a product, and to power a new experience, and so on, I think it's the same skill really.  
**Translation:** 

**[5024.86s] English:** Know, imagining what it would be like to use it, viscerally, um, and having good taste coming back.  
**Translation:** Vocabulary: viscerally: 直觉地

**[5030.44s] English:** To me, what's useful in science, I think, can also be useful in other fields.  
**Translation:** 

**[5035.88s] English:** In product design, and I've just had a very  
**Translation:** 

**[5040.00s] English:** You know, always being a sort of multidisciplinary person, so I don't see the boundaries really.  
**Translation:** 

**[5044.74s] English:** Between, you know, arts and sciences or product and research, it's a continuum for me. I mean,  
**Translation:** Vocabulary: continuum: 连续体; multidisciplinary: 跨学科的

**[5050.48s] English:** I only work on products that are cutting-edge. I wouldn't be able to, you know,  
**Translation:** 

**[5054.06s] English:** Have cutting-edge technology under the hood. I wouldn't be excited about them if they were just.  
**Translation:** 

**[5058.20s] English:** Run-of-the-mill products. So, it requires this invention's creativity capability.  
**Translation:** 

**[5063.90s] English:** What are some specific things you kind of learned about when you, even on the LLM side,  
**Translation:** Vocabulary: capability: 能力

**[5069.10s] English:** You're interacting with Gemini, like this doesn't feel like the layout or the interface.  
**Translation:** 

**[5075.12s] English:** Maybe the trade-off between latency, like how to present information to the user and how long to wait.  
**Translation:** Vocabulary: gemini: 双子座; interacting: 交互; interface: 界面; latency: 延迟; layout: 布局

**[5082.16s] English:** And how that waiting is shown, or the reasoning capabilities—there are some interesting things.  
**Translation:** 

**[5087.18s] English:** Because, as you said, it's at the very cutting edge. We don't know how to present it correctly. So, is  
**Translation:** Vocabulary: capabilities: 能力

**[5092.98s] English:** There are some specific things you've learned? I mean, it's such a fast-evolving space.  
**Translation:** 

**[5097.30s] English:** We're evaluating this all the time.  
**Translation:** Vocabulary: evaluating: 评估

**[5099.10s] English:** But where we are today is that you want to continually simplify things, whether that's  
**Translation:** 

**[5105.12s] English:** The interface, or what you build on top of the model, you kind of want to get out of the way.  
**Translation:** Vocabulary: simplify: 简化

**[5110.46s] English:** Of the model: the train is coming down the track, and it's improving unbelievably fast. This  
**Translation:** 

**[5115.12s] English:** Relentless progress, we talked about earlier: you know, you look at 2.5 versus 1.5, and it's just a  
**Translation:** Vocabulary: relentless: 毫不留情; unbelievably: 难以置信地

**[5120.08s] English:** Gigantic improvement. And we expect that again for future versions. And so the models are  
**Translation:** 

**[5125.42s] English:** Becoming more capable. So, you've got the interesting thing about the design space,  
**Translation:** Vocabulary: gigantic: 巨大的

**[5129.10s] English:** In today's world, these AI-first products are ones you've got to design not for what the thing can do,  
**Translation:** 

**[5134.40s] English:** Today, the technology can do what it can today, but in a year's time. So you actually have to be a very technical  
**Translation:** 

**[5140.06s] English:** Product person, because you've really got to have a good intuition for and feel for that thing, okay.  
**Translation:** 

**[5147.00s] English:** That I'm dreaming about now can't be done today, but is the research track on schedule to basically?  
**Translation:** Vocabulary: intuition: 直觉

**[5152.30s] English:** Intercept that in six months or a year's time? So, you kind of got to intercept where this is highly  
**Translation:** 

**[5157.22s] English:** Changing technology is going.  
**Translation:** Vocabulary: intercept: 截断

**[5159.10s] English:** As well as the  
**Translation:** 

**[5160.00s] English:** Um, uh, new capabilities are coming online all the time that you didn't realize before that can allow.  
**Translation:** 

**[5165.64s] English:** Like deep search to work, or now we've got video generation—what do we do with that? Um, this...  
**Translation:** 

**[5171.40s] English:** Multimodal stuff, you know, is it really going to be the current UI?  
**Translation:** Vocabulary: multimodal: 多种模态的

**[5177.12s] English:** That we have today's text box chats seems very unlikely given once you think about it.  
**Translation:** 

**[5182.26s] English:** Super multimodal systems, shouldn't they be more like "Minority Report," where you're  
**Translation:** 

**[5187.46s] English:** You're sort of vibing with it in a collaborative way, right? It seems very...  
**Translation:** 

**[5192.76s] English:** Restricted today, I think we'll look back on today's interfaces and products and systems as quite  
**Translation:** Vocabulary: collaborative: 合作; interfaces: 界面

**[5198.16s] English:** Archaic, I think, might become obsolete in just a couple of years, so I believe there's a lot of space actually for innovation.  
**Translation:** 

**[5204.18s] English:** To happen on the product side as well as the research side, and then we're offline talking about...  
**Translation:** Vocabulary: archaic: 陈旧; obsolete: 过时

**[5209.26s] English:** This keyboard is the open question: how, when, and how much will we move to audio as the primary?  
**Translation:** 

**[5217.46s] English:** With the machines around us versus typing stuff, yeah; I mean, typing is a very low-bandwidth way of  
**Translation:** 

**[5223.38s] English:** Doing even if you're a very fast typist, I think we're going to have to start utilizing other methods.  
**Translation:** 

**[5228.32s] English:** Other devices, whether that's smart glasses, you know, audio earbuds, um, and eventually maybe some.  
**Translation:** Vocabulary: earbuds: 耳机; typist: 打字员; utilizing: 利用

**[5235.42s] English:** Sorts of neural devices where we can increase the input and output bandwidth to something.  
**Translation:** 

**[5241.24s] English:** Uh, you know, maybe 100 times of what it is today, I think that you know, under-appreciated art form.  
**Translation:** Vocabulary: bandwidth: 带宽; neural: 神经的

**[5247.46s] English:** The interface design, but I think you cannot unlock the power of the intelligence of a system.  
**Translation:** 

**[5253.86s] English:** If you don't have the right interface, their interface is really the way you unlock it.  
**Translation:** 

**[5257.98s] English:** Power, yeah; it's such an interesting question of how to do that. Yeah, so how you would think.  
**Translation:** 

**[5263.80s] English:** Like getting out of the way is in a real art form, yes. You know, it's the sort of thing I guess.  
**Translation:** 

**[5268.98s] English:** Steve Jobs always talked about it: simplicity, beauty, and elegance are what we want.  
**Translation:** 

**[5273.02s] English:** Right, and we're not there yet, in my opinion, and that's what I would like.  
**Translation:** Vocabulary: elegance: 优雅; simplicity: 简洁

**[5277.46s] English:** To get there again, it sort of speaks to the idea of going back.  
**Translation:** 

**[5280.00s] English:** Right, as a game, the most elegant and beautiful game — can you, you know, make an interface?  
**Translation:** Vocabulary: elegant: 优雅; interface: 界面

**[5284.76s] English:** As beautiful as that is, and actually, I think we're going to enter an era of AI-generated interfaces.  
**Translation:** 

**[5290.02s] English:** That are probably personalized to you, so it fits the way that you feel and your aesthetic.  
**Translation:** Vocabulary: aesthetic: 审美; interfaces: 界面

**[5296.18s] English:** That your brain works, and the AI kind of generates that depending on the task you.  
**Translation:** 

**[5302.00s] English:** Know that, that feels like that's probably the direction we'll end up in, yeah, because some people are power.  
**Translation:** Vocabulary: generates: 产生

**[5306.40s] English:** Users and they want every single parameter on screen, everything and everything-based like.  
**Translation:** 

**[5310.66s] English:** Perhaps, with a keyboard-based navigation, I'd like to have shortcuts for.  
**Translation:** Vocabulary: navigation: 导航; parameter: 参数; shortcuts: 快捷键

**[5314.68s] English:** Everything and some people like minimalism, just hiding all of that complexity, yeah, exactly.  
**Translation:** 

**[5319.20s] English:** Yeah, uh, well, I'm glad you have a Steve Jobs mode in you as well. This is great, Einstein! Most Steve.  
**Translation:** Vocabulary: complexity: 复杂性; minimalism: 极简主义

**[5325.54s] English:** Jobs Mode: Um, all right, let me try to trick you into answering a question. When will Gemini...  
**Translation:** 

**[5330.96s] English:** Three come out; it's a before or after DTS6. The world waits for both, and what?  
**Translation:** Vocabulary: gemini: 双子座

**[5336.38s] English:** Does it take to go from 2.5 to 3.0? Because it seems like there's been a lot of releases since then.  
**Translation:** 

**[5344.26s] English:** 2.5, which are already leaps in performance, so what does it even mean to go to a new version?  
**Translation:** 

**[5349.76s] English:** Is it about performance? This is about a completely different flavor of an experience, yeah? Well, so  
**Translation:** 

**[5356.74s] English:** The way it works with our different version numbers is that we try to collect as much information as possible, but maybe.  
**Translation:** 

**[5362.90s] English:** It takes, you know, roughly six months or so.  
**Translation:** 

**[5365.90s] English:** To  
**Translation:** 

**[5366.38s] English:** Do a new kind of full run, and the full productization of a new version, and during that  
**Translation:** 

**[5373.10s] English:** Time lots of new, interesting research, iterations, and ideas come up, and we sort of collect them.  
**Translation:** Vocabulary: iterations: 迭代; productization: 产品化

**[5378.82s] English:** All together, you know, you could imagine the last six months' worth of interesting ideas on the  
**Translation:** 

**[5383.68s] English:** Architecture front, uh, maybe it's on the data front; it's like many different possible things.  
**Translation:** 

**[5388.98s] English:** And we collect packages, that all up, test which ones are likely to be useful for the next iteration.  
**Translation:** 

**[5394.78s] English:** And then, we bundle that all together, and then we sort of collect them all together, and then we sort of  
**Translation:** Vocabulary: bundle: 打包; iteration: 迭代

**[5395.90s] English:** Do a new kind of full run, and the full productization of a new version. During that time, lots of new  
**Translation:** 

**[5396.38s] English:** Ideas come up, and we sort of collect them all together. Then we sort of collect them all together and then we start the new, you know, giant hero training.  
**Translation:** 

**[5400.00s] English:** Right, and then that gets monitored, and then at the end, there's the  
**Translation:** 

**[5405.62s] English:** Of the pre-training, then there's all the post-training; there are many different ways of  
**Translation:** 

**[5408.70s] English:** Doing that involves different ways of patching it, so there's a whole experiment and phase there which  
**Translation:** 

**[5412.60s] English:** You can also get a lot of gains out, and that's where you see the version numbers usually referring.  
**Translation:** Vocabulary: patching: 打补丁

**[5416.98s] English:** To the base model, the pre-trained model, and then the interim versions of 2.5, you know, and the  
**Translation:** 

**[5423.14s] English:** Different sizes, and the different little additions—they're often patches or post-training ideas.  
**Translation:** Vocabulary: interim: 过渡版本; patches: 补丁

**[5428.86s] English:** That can be done afterwards, uh, off the same basic architecture, and then, of course, on top of that, we  
**Translation:** 

**[5433.82s] English:** Also, they come in different sizes: pro, flash, and flashlight, which are often distilled from the  
**Translation:** Vocabulary: distilled: 提炼; flashlight: 手电筒

**[5439.00s] English:** Biggest ones, you know, like the Flash model from the Pro model, and that means we have a range of different options.  
**Translation:** 

**[5444.76s] English:** Choices: If you are the developer, do you want to prioritize performance or speed, right? And cost?  
**Translation:** Vocabulary: prioritize: 优先考虑

**[5451.44s] English:** And we like to think of this Pareto frontier, where on the one hand, the y-axis is, you know, something like utility or cost.  
**Translation:** 

**[5457.62s] English:** Know, like, performance.  
**Translation:** Vocabulary: frontier: 边界; pareto: 帕累托; utility: 效用

**[5458.56s] English:** And then the x-axis is, you know, cost or latency and speed — basically, and we have  
**Translation:** 

**[5465.42s] English:** Models that completely define the frontier, so whatever trade-off you want as an  
**Translation:** Vocabulary: latency: 延迟

**[5471.00s] English:** Individual users or developers, you should find one of our models satisfies that constraint.  
**Translation:** 

**[5476.74s] English:** So, behind the version changes, there is a big hero run, yes, and then there's just an insane...  
**Translation:** Vocabulary: constraint: 限制

**[5485.44s] English:** Complexity of Productization  
**Translation:** 

**[5488.56s] English:** Then there's the distillation of the different sizes along that parade or front.  
**Translation:** Vocabulary: complexity: 复杂性; distillation: 提炼; parade: 行列; productization: 产品化

**[5493.30s] English:** And then, as each step you take, you realize there might be a cool product.  
**Translation:** 

**[5498.16s] English:** There are side quests, yes, exactly, but then you also don't want to take too many side quests.  
**Translation:** Vocabulary: quests: 支线任务

**[5503.08s] English:** Because then you have a million versions of a million products. Yes, it's very unclear. Yeah, but.  
**Translation:** 

**[5507.64s] English:** You also get super excited because it's super cool, yeah? Like, how does even you look at VL's?  
**Translation:** 

**[5511.88s] English:** Very cool! How does it fit into the bigger picture exactly? And then you constantly...  
**Translation:** 

**[5518.56s] English:** You can see that they are not just converging upstream.  
**Translation:** Vocabulary: converging: 汇聚; upstream: 上游

**[5520.00s] English:** We call it, you know, ideas from the product surfaces or, or from the posts.  
**Translation:** 

**[5525.02s] English:** Training and, and even further downstream than that, you kind of go upstream that.  
**Translation:** Vocabulary: downstream: 下游

**[5528.94s] English:** Into the core model training for the next run, right?  
**Translation:** 

**[5532.36s] English:** So then, the main model, the main Gemini track, becomes more and more general, and eventually,  
**Translation:** Vocabulary: gemini: 双子座模型

**[5537.42s] English:** You know, AGI.  
**Translation:** 

**[5539.86s] English:** One hero at a time.  
**Translation:** 

**[5541.30s] English:** Yes, exactly.  
**Translation:** 

**[5542.06s] English:** A few hero runs later.  
**Translation:** 

**[5543.58s] English:** Yeah.  
**Translation:** 

**[5544.06s] English:** So, sometimes when you release these new versions—or every version, really—  
**Translation:** 

**[5550.00s] English:** Are benchmarks productive or counterproductive for showing the performance of a model?  
**Translation:** 

**[5555.88s] English:** You need them, and and but, it's important that you don't overfit to them, right?  
**Translation:** Vocabulary: benchmarks: 参考标准; counterproductive: 适得其反; overfit: 拟合过度

**[5559.94s] English:** So, there shouldn't be an end with a be-all and end-all.  
**Translation:** 

**[5562.00s] English:** So there's LM Arena, or it used to be called Elemsys.  
**Translation:** Vocabulary: elemsys: 全能系统

**[5565.10s] English:** That's one of them that turned out sort of organically to be one of the main ways.  
**Translation:** 

**[5569.02s] English:** People like to test these systems, at least the chatbots.  
**Translation:** Vocabulary: chatbots: 聊天机器人; organically: 自然地

**[5571.92s] English:** Obviously, there are lots of academic benchmarks for both math and coding tests.  
**Translation:** 

**[5577.30s] English:** Ability: General Language Ability.  
**Translation:** 

**[5580.00s] English:** Science ability, and so on.  
**Translation:** 

**[5581.80s] English:** And then, we have our own internal benchmarks that we care about.  
**Translation:** 

**[5584.74s] English:** It's a kind of multi-objective optimization problem, right?  
**Translation:** 

**[5588.84s] English:** You want to be good at just one thing, but you don't want to.  
**Translation:** Vocabulary: optimization: 最优化

**[5590.96s] English:** We're trying to build general systems that are good across the board.  
**Translation:** 

**[5594.12s] English:** And you try and make no-regret improvements.  
**Translation:** 

**[5597.44s] English:** So, where you improve in, for example, coding, but it doesn't reduce your performance in other areas.  
**Translation:** 

**[5603.64s] English:** Right?  
**Translation:** 

**[5603.88s] English:** So, that's the hard part.  
**Translation:** 

**[5604.76s] English:** Cause you can, of course, you could put more coding data in, or you could put more,  
**Translation:** 

**[5609.22s] English:** Um,  
**Translation:** 

**[5610.00s] English:** I don't know; gaming data in, but then does it make your language system worse, uh?  
**Translation:** 

**[5615.40s] English:** Or, uh, in your translation systems and other things you care about.  
**Translation:** 

**[5619.12s] English:** So it's you've got to kind of continually monitor this increasingly larger and larger.  
**Translation:** 

**[5624.18s] English:** Suite of, of benchmarks.  
**Translation:** 

**[5625.78s] English:** And also, when you stick them into products, these models, you also care.  
**Translation:** 

**[5629.98s] English:** About the direct usage, the direct stats, and the signals you're getting from the  
**Translation:** 

**[5635.48s] English:** End users, whether they're coders or the average person using the chat,  
**Translation:** Vocabulary: coders: 程序员

**[5639.56s] English:** Interface.  
**Translation:** 

**[5640.00s] English:** Yeah, because ultimately you want to measure the usefulness, but it's so hard to convert that into a number.  
**Translation:** Vocabulary: convert: 转换; interface: 接口

**[5645.14s] English:** Right.  
**Translation:** 

**[5645.48s] English:** It's really vibe-based benchmarks across a large number of users, and it's hard to know.  
**Translation:** Vocabulary: benchmarks: 参考标准

**[5651.60s] English:** And it would be just terrifying to me to, you know, have a much smarter model, but it's just something vibe-based.  
**Translation:** 

**[5659.52s] English:** It's not quite working.  
**Translation:** Vocabulary: terrifying: 令人恐惧的

**[5661.22s] English:** And everything you just said has to be smart and useful across so many domains.  
**Translation:** 

**[5668.64s] English:** So, you get super excited because it's all of a sudden solving programming problems you've never been able to solve before, but now it's crappy poetry or something.  
**Translation:** Vocabulary: crappy: 糟糕的诗

**[5678.58s] English:** And it's just, I don't know, that's stressful.  
**Translation:** 

**[5680.58s] English:** That's so difficult to balance.  
**Translation:** 

**[5684.06s] English:** And because you can't really trust the benchmarks, you really have to trust the end users.  
**Translation:** 

**[5687.90s] English:** Yeah.  
**Translation:** 

**[5688.48s] English:** And then other things that are even more esoteric come into play, like, you know, the style of the persona of the system. You know, is it verbose?  
**Translation:** 

**[5698.64s] English:** Is it succinct?  
**Translation:** Vocabulary: esoteric: 深奥的; succinct: 简洁的; verbose: 啰嗦的

**[5699.92s] English:** Is it humorous?  
**Translation:** 

**[5701.40s] English:** You know, different people like different things.  
**Translation:** Vocabulary: humorous: 幽默的

**[5703.82s] English:** So, you know, it's very interesting.  
**Translation:** 

**[5705.98s] English:** It's almost like the cutting-edge part of psychology research or personality research.  
**Translation:** 

**[5710.82s] English:** You know, I used to do that in my PhD, like the five-factor personality model.  
**Translation:** 

**[5714.24s] English:** What do we actually want our systems to be like?  
**Translation:** 

**[5716.46s] English:** And different people will like different things as well.  
**Translation:** 

**[5718.96s] English:** So, these are all just sort of new problems in product space that I don't think have ever really been tackled before, but we're going to have to deal with them rapidly now.  
**Translation:** Vocabulary: tackled: 解决

**[5727.62s] English:** I think it's a super interesting topic.  
**Translation:** 

**[5728.58s] English:** Super fascinating space: developing the character of the thing.  
**Translation:** 

**[5731.40s] English:** Yeah.  
**Translation:** 

**[5731.84s] English:** And in doing so, it puts a mirror to ourselves.  
**Translation:** 

**[5734.88s] English:** What kinds of things do we like?  
**Translation:** 

**[5738.12s] English:** Because prompt engineering allows you to control a lot of those elements, but can the product make it easier for you to control the different flavors of those experiences and the various characters you interact with?  
**Translation:** Vocabulary: flavors: 口味; prompt: 提示

**[5751.82s] English:** Yeah, exactly.  
**Translation:** 

**[5753.02s] English:** So, what's the probability of Google DeepMind winning?  
**Translation:** 

**[5756.44s] English:** Well, I don't see it as sort of winning.  
**Translation:** 

**[5757.84s] English:** I mean, I think we need to think.  
**Translation:** 

**[5760.00s] English:** Winning is the wrong way to look at it, given how important and consequential what it is we're doing is.  
**Translation:** 

**[5764.20s] English:** Building, so funny enough, I don't try to view it like a game or competition, even though.  
**Translation:** Vocabulary: consequential: 有重大影响的

**[5769.02s] English:** That's a lot of my mindset. It's about, in my view, that all of us have those of us at the leading  
**Translation:** 

**[5774.54s] English:** Edge has a responsibility to steward this unbelievable technology that could be used for  
**Translation:** Vocabulary: mindset: 思想模式; steward: 管理者

**[5780.40s] English:** Incredible, but also has risks; we must steward it safely into the world for the benefit of humanity.  
**Translation:** 

**[5786.28s] English:** That's always been what I've dreamed about, and what we've always tried to do, and I hope.  
**Translation:** 

**[5792.66s] English:** That's what eventually the community, maybe even the international community, will rally around when.  
**Translation:** 

**[5797.16s] English:** It becomes obvious that, as we get closer and closer to AGI, that's what's needed.  
**Translation:** 

**[5802.42s] English:** I agree with you; I think that's beautifully put. You've said that, um, you talk to and are on good  
**Translation:** 

**[5808.52s] English:** Terms with the leads of some of these labs as the competition heats up—how hard is it to?  
**Translation:** 

**[5816.00s] English:** Maintain  
**Translation:** 

**[5816.28s] English:** Sort of those relationships, it's been okay so far. I try to pride myself in being collaborative.  
**Translation:** Vocabulary: collaborative: 合作的

**[5823.38s] English:** I'm a collaborative person. Research is a collaborative endeavor, and science is a collaborative effort.  
**Translation:** 

**[5827.58s] English:** Endeavor: Right, it's all good for humanity in the end if you cure something incredible, you know.  
**Translation:** Vocabulary: endeavor: 努力

**[5831.30s] English:** Terrible diseases, and you come with an incredible cure. This is a net win for humanity, and the same.  
**Translation:** 

**[5837.20s] English:** With energy, all of the things that I'm interested in, in helping solve with AI. So, I just want that.  
**Translation:** 

**[5842.84s] English:** Technology should exist in the world and be used for the right things.  
**Translation:** 

**[5845.62s] English:** And  
**Translation:** 

**[5846.28s] English:** And and the kinds of benefits of that, including the productivity benefits of that.  
**Translation:** 

**[5850.36s] English:** Being shared for the benefit of everyone, so I try to maintain good relations with all the  
**Translation:** 

**[5855.78s] English:** Leading lab people have very interesting characters. Many of them, as you might expect.  
**Translation:** 

**[5859.98s] English:** Um, but yeah, I'm on good terms with pretty much all of them, and I think that's  
**Translation:** 

**[5865.60s] English:** Going to be important when things get even more serious than they are now, that there are  
**Translation:** 

**[5870.78s] English:** Those communication channels and that's what will facilitate cooperation and, you know,  
**Translation:** Vocabulary: facilitate: 促进合作

**[5876.28s] English:** Collaboration, or collaboration if that's what is required, especially on things like safety.  
**Translation:** 

**[5880.00s] English:** Yeah, I hope there's some collaboration on stuff that's sort of less high-stakes, and in so doing,  
**Translation:** Vocabulary: collaboration: 合作

**[5886.86s] English:** Serves as a mechanism for maintaining friendships and relationships, so, for example, I think the  
**Translation:** 

**[5891.12s] English:** The internet would love it if you and Elon somehow collaborated on creating a video game that kind  
**Translation:** Vocabulary: collaborated: 合作

**[5895.14s] English:** Of the thing that I think enables camaraderie and good terms, and also you two are legit gamers.  
**Translation:** 

**[5901.40s] English:** So, it's just fun, yeah. Fun, yeah. That would be awesome, and we've talked about that in the past.  
**Translation:** Vocabulary: camaraderie: 同伴情谊; legit: 真正的

**[5905.68s] English:** And it might be a cool thing that we can do, and I agree with you; it'd be nice to have.  
**Translation:** 

**[5909.64s] English:** Um, kind of side projects in a way where one can just lean into the collaboration aspect of it.  
**Translation:** 

**[5917.22s] English:** And it's a sort of win-win for both sides, and it's kind of builds up that.  
**Translation:** 

**[5923.44s] English:** Uh, collaborative muscle. I see the scientific endeavor as that kind of side project for.  
**Translation:** Vocabulary: collaborative: 合作的; endeavor: 努力

**[5928.44s] English:** Humanity, yeah, and I think Deep Google Deep Mind has been really pushing that. I would love it if.  
**Translation:** 

**[5934.20s] English:** To see other labs do more scientific stuff and then collaborate, because it just seems like an easier way to go.  
**Translation:** Vocabulary: collaborate: 合作

**[5939.02s] English:** To collaborate  
**Translation:** 

**[5939.62s] English:** And the big scientific questions—I agree, and I would love to see a lot more people involved in that.  
**Translation:** 

**[5943.94s] English:** Other labs talk about science, but I think we're really the only ones using it for science and...  
**Translation:** 

**[5948.08s] English:** Doing that, and that's why projects like Alpha Fold are so important to me and I think to our  
**Translation:** Vocabulary: alpha: 阿尔法

**[5952.98s] English:** The mission is to show, how AI can be clearly used in a very concrete way for the  
**Translation:** 

**[5959.64s] English:** The benefit of humanity, and also, we spun out companies like Isomorphic off the back of Alpha.  
**Translation:** Vocabulary: isomorphic: 同构的公司

**[5963.96s] English:** Fold to do drug discovery, and it's going really well. You know, you can think of  
**Translation:** 

**[5968.84s] English:** Build additional AlphaFold-type systems to go into the chemistry space to help accelerate drug discovery.  
**Translation:** 

**[5974.12s] English:** Design and the examples I think we need to show, and society needs to understand where AI can bring.  
**Translation:** 

**[5980.48s] English:** These huge benefits—well, from the bottom of my heart, thank you for pushing the scientific efforts.  
**Translation:** 

**[5985.94s] English:** Forward with rigor, with fun, with humility—all of it. I just love to see, and still talking about p...  
**Translation:** 

**[5991.56s] English:** Equals MP; I mean, it's just incredible, so I love it. Uh, there seems to have been a war for the  
**Translation:** Vocabulary: equals: 等于; humility: 谦逊; rigor: 严谨

**[5998.84s] English:** Word talent; some of it is.  
**Translation:** 

**[6000.00s] English:** I don't know.  
**Translation:** 

**[6001.38s] English:** What do you think about Meta buying up talent with huge salaries, and the heating up of this battle?  
**Translation:** 

**[6008.06s] English:** For talent, and I should say that I think a lot of people see Deep Mine as a really great place to do.  
**Translation:** Vocabulary: salaries: 高薪

**[6014.18s] English:** Cutting-edge work for the reasons that you've outlined is like there's this:  
**Translation:** 

**[6018.88s] English:** Vibrant scientific culture. Yeah. Well, look, of course, there's a strategy that Meta is taking right now.  
**Translation:** Vocabulary: outlined: 阐述; vibrant: 充满活力的

**[6025.74s] English:** I think, from my perspective at least, that the people who are  
**Translation:** 

**[6030.32s] English:** Real  
**Translation:** 

**[6031.54s] English:** Believers in the mission of AGI and what it can do and understand the real consequences, both good and bad, from that. What's at stake?  
**Translation:** 

**[6037.52s] English:** That responsibility entails. I think they're mostly doing it to be like myself—to be on the frontier of that research.  
**Translation:** Vocabulary: believers: 信仰者; entails: 包含; frontier: 前沿

**[6044.18s] English:** So, you know, they can help influence the way it goes and steward that technology safely into the world. You know.  
**Translation:** 

**[6051.14s] English:** Meta are not at the forefront right now. Maybe they'll manage to get back there.  
**Translation:** Vocabulary: forefront: 前沿; steward: 管理

**[6055.66s] English:** You know,  
**Translation:** 

**[6056.30s] English:** It's probably rational what they're doing from their perspective, because they're behind and they need to do something.  
**Translation:** 

**[6060.26s] English:** But I think there are more important things than just money.  
**Translation:** 

**[6063.80s] English:** Of course, one has to pay people their market rates, and all of these things, and that continues to go up.  
**Translation:** 

**[6069.24s] English:** But as problems arise, and I was expecting this because more and more people are finally starting to recognize it.  
**Translation:** 

**[6074.80s] English:** Realizing that leaders of companies, what I've always known for 30-plus years now, is that AGI is the most important technology.  
**Translation:** 

**[6081.64s] English:** Probably there will be something invented someday. So, in some senses, it's rational to be doing that.  
**Translation:** 

**[6086.26s] English:** But I also think there's a much bigger question.  
**Translation:** 

**[6088.98s] English:** I mean, people in a  
**Translation:** 

**[6089.92s] English:** AI, these days are very well-paid, you know. I remember when we were starting out back in 2010.  
**Translation:** 

**[6095.08s] English:** You know, I didn't even pay myself for a couple of years because it wasn't enough money; we couldn't.  
**Translation:** 

**[6098.86s] English:** Raise any money, and these days interns are being paid—you know, the amount that we raised as our.  
**Translation:** Vocabulary: interns: 实习生

**[6103.58s] English:** First, I'll take the entire seat round, so it's pretty funny, and I remember the days when I used to have to.  
**Translation:** 

**[6108.46s] English:** To work for free and almost pay my own way to do an internship — right now, it's all the other way.  
**Translation:** 

**[6113.02s] English:** Around, but that's just how it is; it's the new world. And, um, but I think that you know, we've been  
**Translation:** 

**[6118.46s] English:** Discussing, like, what happens post-  
**Translation:** 

**[6120.00s] English:** AGI and energy systems are solved, and so on. What is "even money" going to mean? So, I think... you know.  
**Translation:** 

**[6126.46s] English:** In the economy, and we're going to have much bigger issues to work through. How do we  
**Translation:** 

**[6130.44s] English:** Economy functions in that world, and companies, so I think you know it's a little bit of a side.  
**Translation:** 

**[6135.04s] English:** Issue about salaries and things like that today, yeah. When you're facing such gigantic...  
**Translation:** Vocabulary: gigantic: 巨大的; salaries: 工资

**[6141.14s] English:** Consequences, and gigantic, fascinating scientific questions, which may be only a few.  
**Translation:** 

**[6146.22s] English:** Years away, so, so from a practical or pragmatic sense, if we zoom in on jobs, we can look at  
**Translation:** Vocabulary: pragmatic: 实用的

**[6153.08s] English:** Programmers, because it seems like AI systems are currently doing incredibly well at programming.  
**Translation:** 

**[6157.96s] English:** And increasingly, so many people who program for a living love programming but are worried.  
**Translation:** Vocabulary: programmers: 程序员

**[6164.92s] English:** They will lose their jobs. How worried should they be? Do you think, and what's the right way to  
**Translation:** 

**[6170.84s] English:** Uh, sort of adjust to the new reality and ensure that you survive and thrive as.  
**Translation:** Vocabulary: thrive: 繁荣发展

**[6176.14s] English:** A human being.  
**Translation:** 

**[6176.22s] English:** In the programming world, well, it's interesting that programming is again counterintuitive.  
**Translation:** Vocabulary: counterintuitive: 违反直觉的

**[6181.40s] English:** To what we thought years ago, maybe some of the skills that we think of as harder skills,...  
**Translation:** 

**[6186.52s] English:** Are turned out maybe to be the easier ones for various reasons, but you know, coding and math.  
**Translation:** 

**[6190.80s] English:** Because you can create a lot of synthetic data and verify if that data is correct, so because of  
**Translation:** 

**[6196.00s] English:** That nature of it being easier to make things like synthetic data to train from, um, it's also  
**Translation:** Vocabulary: synthetic: 人造的; verify: 验证

**[6200.84s] English:** An area, of course, we're all interested in because, as programmers, right, to help us and get faster at.  
**Translation:** 

**[6205.84s] English:** It has become more productive, more productive, more productive, and more productive.  
**Translation:** 

**[6206.20s] English:** Productive, so I think for the next era, like the next five to ten years, I think what we're going to  
**Translation:** 

**[6211.26s] English:** Find people who are kind of embracing these technologies, and they become almost at one with them.  
**Translation:** Vocabulary: embracing: 接纳

**[6217.02s] English:** Um, whether that's in the creative industries or the technical industries, it will become sort of  
**Translation:** 

**[6221.28s] English:** Superhumanly productive, I think so. The great programmers will be even better, but there'll  
**Translation:** 

**[6225.78s] English:** Be even 10x what they are today, and because there, you'll be able to use their skills to.  
**Translation:** 

**[6230.16s] English:** Utilize those tools to the maximum, you know, exploit them to the maximum.  
**Translation:** Vocabulary: exploit: 榨取; utilize: 利用

**[6236.20s] English:** And, um, so I think that's what we're going to see in the next domain.  
**Translation:** 

**[6240.00s] English:** So that's going to cause quite a lot of change, right?  
**Translation:** 

**[6242.50s] English:** And so that's coming.  
**Translation:** 

**[6243.54s] English:** A lot of people benefit from that.  
**Translation:** 

**[6245.24s] English:** So, I think one example of that is if coding becomes easier,  
**Translation:** 

**[6249.24s] English:** It becomes available to many more creatives to do more.  
**Translation:** Vocabulary: creatives: 有创造力的人

**[6254.00s] English:** But I think the top programmers will still have huge advantages.  
**Translation:** 

**[6257.50s] English:** In terms of specifying, going back to specifying,...  
**Translation:** Vocabulary: programmers: 程序员; specifying: 指定

**[6260.24s] English:** What the architecture should be, the question should be:  
**Translation:** 

**[6262.74s] English:** How to guide these coding assistants in a way that's useful,  
**Translation:** 

**[6267.68s] English:** Or check whether the code they produce is good.  
**Translation:** 

**[6270.82s] English:** So, I think there's plenty of headroom there for the foreseeable next few years.  
**Translation:** Vocabulary: foreseeable: 可预见的; headroom: 余量

**[6276.74s] English:** So, I think there are several interesting things there.  
**Translation:** 

**[6278.78s] English:** One is, there's a lot of imperative to just get better and better consistently.  
**Translation:** Vocabulary: imperative: 至关重要

**[6283.58s] English:** Of using these tools.  
**Translation:** 

**[6285.04s] English:** So, they're riding the wave of the improving models.  
**Translation:** 

**[6288.62s] English:** Versus competing against them.  
**Translation:** 

**[6291.92s] English:** But sadly, that's the nature of life on Earth.  
**Translation:** 

**[6296.36s] English:** There could be a huge amount of value to certain kinds of programming.  
**Translation:** 

**[6300.62s] English:** At the cutting edge, but less value to other kinds.  
**Translation:** 

**[6304.82s] English:** For example, it could be like front-end web design.  
**Translation:** 

**[6309.14s] English:** Might be more amenable to, as you mentioned,  
**Translation:** Vocabulary: amenable: 易于接受的

**[6314.78s] English:** To generate content by AI systems.  
**Translation:** 

**[6318.32s] English:** And maybe, for example, game engine design, or something like that.  
**Translation:** 

**[6321.16s] English:** For backend design, or guiding systems in high-performance situations.  
**Translation:** 

**[6326.36s] English:** High-performance programming: type of design decisions,  
**Translation:** Vocabulary: backend: 后端

**[6329.68s] English:** That might be extremely valuable.  
**Translation:** 

**[6331.76s] English:** But it will shift where the humans are needed most.  
**Translation:** 

**[6335.46s] English:** And that's scary for people to adjust.  
**Translation:** 

**[6337.60s] English:** Yeah, I think that's right.  
**Translation:** 

**[6338.96s] English:** At any time where there's a lot of disruption and change,  
**Translation:** 

**[6342.36s] English:** And we've had this before; it's not just this time.  
**Translation:** Vocabulary: disruption: 干扰

**[6343.98s] English:** We've had this many times in human history with the Internet, mobile,  
**Translation:** 

**[6348.38s] English:** But before that was the Industrial Revolution.  
**Translation:** 

**[6351.16s] English:** And it's going to be one of those eras where there will be a lot of change.  
**Translation:** 

**[6354.34s] English:** I think there'll be new jobs we can't even imagine.  
**Translation:** 

**[6356.36s] English:** Today, just like the Internet created.  
**Translation:** 

**[6358.88s] English:** And then, those people with the right...  
**Translation:** 

**[6360.00s] English:** Skills sets to ride that wave will become incredibly valuable, those skills. But maybe,  
**Translation:** 

**[6366.90s] English:** People will have to relearn or adapt a bit their current skills, and it's the thing that's going  
**Translation:** 

**[6373.10s] English:** To be harder to deal with this time around is that I think what we're going to see is something like...  
**Translation:** 

**[6377.86s] English:** Probably 10 times the impact the Industrial Revolution had, but 10 times faster as well.  
**Translation:** 

**[6384.44s] English:** So instead of 100 years, it takes 10 years. And so that's going to make it 100 times faster.  
**Translation:** 

**[6389.12s] English:** The impact and the speed combined. So, that's what's I think is going to make it more difficult.  
**Translation:** 

**[6394.14s] English:** For society to deal with, and there's a lot to think through. I think we need to be  
**Translation:** 

**[6400.32s] English:** Discussing that right now, and I encourage top economists in the world and philosophers to  
**Translation:** Vocabulary: economists: 经济学家; philosophers: 哲学家

**[6405.70s] English:** Start thinking about how society will be affected by this, and what we should do.  
**Translation:** 

**[6412.08s] English:** Including things like universal basic provision or something like that, where a lot of the  
**Translation:** Vocabulary: provision: 供应

**[6419.02s] English:** Increased productivity is shared out and distributed to society, and maybe in the form,  
**Translation:** 

**[6426.32s] English:** Of services and other things, where if you want more than that, you still have to go and get some incredibly  
**Translation:** 

**[6432.14s] English:** Rarer skills and things like that, and make yourself unique. But there's a basic provision that is  
**Translation:** 

**[6438.52s] English:** Provided, and if you think of government as technology, there are also some interesting questions.  
**Translation:** 

**[6442.76s] English:** Not just in economics, but also in politics. How do you design a system that's responsive to the,  
**Translation:** 

**[6449.02s] English:** Rapidly changing times, such that you can represent the different pains that people feel.  
**Translation:** 

**[6455.68s] English:** From the different groups? And how do you reallocate resources in a way that addresses...  
**Translation:** 

**[6462.90s] English:** That pain, and it represents the hopes, the pain, and the fears of different people in a way that  
**Translation:** Vocabulary: reallocate: 重新分配

**[6469.06s] English:** Doesn't it lead to division? Because politicians are often really good at fueling the division.  
**Translation:** 

**[6475.84s] English:** And using that to get elected. The other,  
**Translation:** Vocabulary: fueling: 煽动

**[6479.02s] English:** Nick.  
**Translation:** 

**[6480.00s] English:** Defining the other and then saying that's bad, and so, based on that, I think that's often  
**Translation:** 

**[6486.68s] English:** It is counterproductive to leverage a rapidly changing technology; how can we help the world flourish instead?  
**Translation:** 

**[6492.38s] English:** Almost, we need to improve our political systems as well rapidly, if you think of them as a technology.  
**Translation:** Vocabulary: counterproductive: 适得其反; flourish: 繁荣; leverage: 利用

**[6499.40s] English:** Definitely, and I think we'll need new governance structures and institutions probably to.  
**Translation:** 

**[6505.04s] English:** Help with this transition, so I think political philosophy and political science are going to be  
**Translation:** Vocabulary: governance: 治理结构

**[6510.34s] English:** Key to that, but I think the number one thing, first of all, is to create more abundance of  
**Translation:** 

**[6516.48s] English:** Resources, right? Then there's the fact that's the number one thing: increase productivity and get more.  
**Translation:** 

**[6521.92s] English:** Resources might eventually get out of the zero-sum situation, then the second question is how to use them.  
**Translation:** 

**[6528.08s] English:** Those resources and distribute those resources, but yeah, you can't do that without having that.  
**Translation:** 

**[6532.78s] English:** Abundance, first. Uh, you mentioned  
**Translation:** 

**[6535.02s] English:** To me, uh, the book "The Maniac" by Benjamin Libet is a book about, um, first of all, about you.  
**Translation:** Vocabulary: benjamin: 利贝特; maniac: 狂人

**[6542.74s] English:** There's a bio about you. Um, it's strange; yeah, it's unclear, yes, sir. It's unclear how much is fiction.  
**Translation:** 

**[6549.64s] English:** How much is "Reality,"? But I think the central figure that is, uh, John von Neumann. I would say.  
**Translation:** Vocabulary: neumann: 冯·诺伊曼

**[6555.98s] English:** It's a haunting and beautiful exploration of madness and genius, and let's say, the double-edged.  
**Translation:** 

**[6561.24s] English:** Sword of Discovery and  
**Translation:** Vocabulary: haunting: 令人不安; madness: 疯狂

**[6565.02s] English:** You know, for people don't know that John von Neumann is a kind of legendary mind; he contributed to  
**Translation:** 

**[6570.06s] English:** Quantum mechanics; he was on the Manhattan Project, and he is widely considered to be the father of or.  
**Translation:** Vocabulary: legendary: 传奇; manhattan: 曼哈顿; quantum: 量子

**[6575.92s] English:** Pioneer the modern computer and AI, and so on. So, as many people say, he's one of the smartest.  
**Translation:** 

**[6582.92s] English:** Humans, ever so it's just fascinating, and what's also fascinating is as a person who saw nuclear.  
**Translation:** Vocabulary: pioneer: 开拓者

**[6589.60s] English:** Science and physics became the basis for the atomic bomb, so you got the  
**Translation:** 

**[6595.02s] English:** Ideas can become something that has a huge amount of impact on the world.  
**Translation:** 

**[6600.00s] English:** He also foresaw the same thing for computing.  
**Translation:** 

**[6604.22s] English:** And that's a little bit, again, a beautiful and haunting aspect of the book.  
**Translation:** Vocabulary: computing: 计算; foresaw: 预见

**[6610.58s] English:** Then, taking a leap forward and looking at this—at least in all of AlphaGo and AlphaZero—was a big moment.  
**Translation:** 

**[6618.64s] English:** That might be why John von Neumann's thinking was brought to reality.  
**Translation:** 

**[6626.02s] English:** So, I guess the question is: What do you think if you got to hang out with John von Neumann?  
**Translation:** 

**[6631.62s] English:** Now, what would he say about what's going on?  
**Translation:** Vocabulary: neumann: 冯·诺伊曼

**[6635.40s] English:** Well, that would be an amazing experience.  
**Translation:** 

**[6636.78s] English:** You know, he's a fantastic mind.  
**Translation:** 

**[6638.98s] English:** And I also love the way he spent a lot of his time at Princeton at the Institute of.  
**Translation:** 

**[6643.42s] English:** Advanced Studies, a very special place for thinking.  
**Translation:** Vocabulary: princeton: 普林斯顿

**[6646.82s] English:** And it's amazing how much of a polymath he was, in the spread of things he helped invent.  
**Translation:** 

**[6652.70s] English:** Including, of course, the von Neumann architecture, which is used in all the  
**Translation:** Vocabulary: polymath: 博学之人

**[6655.34s] English:** Modern computers have.  
**Translation:** 

**[6656.02s] English:** And he had amazing foresight.  
**Translation:** Vocabulary: foresight: 远见

**[6660.46s] English:** I think he would have loved where we are today.  
**Translation:** 

**[6663.50s] English:** And he would have; I think he would have really enjoyed AlphaGo being, you know, he also did.  
**Translation:** 

**[6668.44s] English:** Game theory.  
**Translation:** 

**[6669.62s] English:** I think he foresaw a lot of what would happen with learning machine systems that are.  
**Translation:** 

**[6675.44s] English:** Of course, I think he called it, rather than programmed.  
**Translation:** 

**[6678.14s] English:** I'm not sure how even that, maybe he wouldn't even be that surprised.  
**Translation:** 

**[6680.64s] English:** There's the fruition of what I thought he already foresaw in the 1950s.  
**Translation:** 

**[6684.68s] English:** I wonder what advice he would give to people.  
**Translation:** Vocabulary: foresaw: 预见

**[6686.02s] English:** You got to see the building of the atomic bomb with the Manhattan Project.  
**Translation:** 

**[6690.22s] English:** I'm sure there's interesting stuff that maybe isn't talked about enough.  
**Translation:** 

**[6693.66s] English:** Maybe some bureaucratic aspect, maybe the influence of politicians, maybe not enough.  
**Translation:** 

**[6699.08s] English:** Of picking up the phone and talking to people who are called enemies by the said politicians.  
**Translation:** Vocabulary: bureaucratic: 官僚主义的

**[6704.66s] English:** There might be some deep wisdom that we just may have lost from that time, actually.  
**Translation:** 

**[6708.58s] English:** Yeah, I'm sure.  
**Translation:** 

**[6709.28s] English:** I'm sure there is.  
**Translation:** 

**[6710.20s] English:** I mean, I've taught and studied a lot, you know. I read a lot of books back then as well.  
**Translation:** 

**[6713.92s] English:** Chronicle Time.  
**Translation:** 

**[6714.88s] English:** And some brilliant people were involved.  
**Translation:** Vocabulary: chronicle: 史书

**[6717.30s] English:** I agree with you.  
**Translation:** 

**[6718.18s] English:** I think maybe there needs to be more.  
**Translation:** 

**[6720.00s] English:** Dialogue and understanding, um, I hope we can learn from those times. I think the difference here is...  
**Translation:** 

**[6726.32s] English:** Is that the AI, which has so many applications, is a multi-use technology? Obviously, we're trying to do things with it.  
**Translation:** 

**[6731.22s] English:** Like that, like solving all diseases, um, helping with energy and scarcity; these are incredible.  
**Translation:** 

**[6738.58s] English:** Things like this is why all of us, and myself, you know, started on this journey over 30 years ago.  
**Translation:** Vocabulary: scarcity: 资源匮乏

**[6744.16s] English:** And, um, but of course, there are risks too, and probably von Neumann; my guess is he foresaw both.  
**Translation:** 

**[6751.56s] English:** And, um, I think he sort of said, "I think it would be," to his wife.  
**Translation:** Vocabulary: neumann: 冯·诺伊曼

**[6757.28s] English:** Computers would be even more impactful in the world, and as we just discussed, I think.  
**Translation:** 

**[6762.34s] English:** That's right; I think it's going to be at least 10 times the impact of the Industrial Revolution, so I think.  
**Translation:** 

**[6767.30s] English:** He's right, so I think he would have been, I imagine, fascinated by where we are now, and I think one.  
**Translation:** 

**[6774.14s] English:** Of the maybe you can correct me, but one of the takeaways from the book is that reason has, uh  
**Translation:** Vocabulary: fascinated: 着迷; takeaways: 收获

**[6782.00s] English:** Said in the book "Mad Dreams of Reason," it's not enough for guiding humanity as we build these.  
**Translation:** 

**[6787.62s] English:** Super powerful technology—that there's something else, I mean, there's also like a religious component.  
**Translation:** 

**[6793.36s] English:** Whatever god, or whatever religion gives it, pulls it something in the human spirit that.  
**Translation:** 

**[6798.58s] English:** Raw, cold reason doesn't give us, and I agree with that. I think we need to.  
**Translation:** 

**[6804.14s] English:** Approach it with whatever you want to call it—the spiritual dimension, or the humanist dimension.  
**Translation:** 

**[6808.86s] English:** Doesn't have to be to do with religion, right? But this idea of a soul — what makes us human — this  
**Translation:** Vocabulary: dimension: 维度; humanist: 人本主义者

**[6814.06s] English:** Spark, that we have perhaps is to do with consciousness, when we finally understand that.  
**Translation:** 

**[6818.54s] English:** Um, I think that has to be at the heart of the endeavor, um, and technology. I've always seen  
**Translation:** Vocabulary: consciousness: 觉醒; endeavor: 努力

**[6823.42s] English:** Technology, as the enabler, is the tool that enables us to flourish and understand more.  
**Translation:** 

**[6829.98s] English:** About the world, and I'm sort of with Feynman on this, and he used to always talk about  
**Translation:** Vocabulary: enabler: 促进者; flourish: 繁荣发展

**[6834.14s] English:** Science and art being companions, right? You can understand it from both sides.  
**Translation:** 

**[6840.00s] English:** Of a flower, how beautiful it is, and also understand why the colors of the flower evolved like that.  
**Translation:** Vocabulary: evolved: 演化

**[6845.26s] English:** Right, that just makes it more beautiful — that just the intrinsic beauty of the flower, and I've  
**Translation:** 

**[6850.42s] English:** Always sort of seen it that way, and maybe you know, in the Renaissance times, the great discoverers.  
**Translation:** Vocabulary: intrinsic: 本质的; renaissance: 文艺复兴

**[6855.22s] English:** Then, like people like Da Vinci, you know, I don't think he saw any difference between science and art.  
**Translation:** 

**[6860.12s] English:** And art, uh, and perhaps religion—right? Everything was just part of being human and, um, being.  
**Translation:** Vocabulary: vinci: 达·芬奇

**[6866.34s] English:** Inspired by the world around us, and that's what I try to incorporate into my philosophy. One of my  
**Translation:** 

**[6872.60s] English:** Favorite philosophers are Spinoza, and I think he combined that very well—you know, this idea of  
**Translation:** Vocabulary: incorporate: 吸收; philosophers: 哲学家; spinoza: 斯宾诺莎

**[6877.46s] English:** Trying to understand the universe and our place in it, and that was his kind of way of thinking.  
**Translation:** 

**[6882.56s] English:** Understanding religion, and I think that's quite beautiful. For me, all of these things are  
**Translation:** 

**[6888.08s] English:** Related, interrelated, the technology and what it means to be human, and I think it's very  
**Translation:** 

**[6894.76s] English:** Important, though, that we remain  
**Translation:** Vocabulary: interrelated: 相互关联

**[6896.34s] English:** Remember that, as when we're immersed in the technology and research, I think a lot  
**Translation:** 

**[6902.30s] English:** Of researchers that I see in our field are a little bit too narrow, and only understand the  
**Translation:** Vocabulary: immersed: 沉浸

**[6908.52s] English:** Technology, and I think that's why it's important for this to be debated by society at  
**Translation:** 

**[6914.08s] English:** Large, and I'm very supportive of things like this—the AI summits that will happen—and governments.  
**Translation:** Vocabulary: summits: 高峰会议

**[6918.38s] English:** Understanding it, and I think that's one good thing about the chatbot era and the product era of AI is  
**Translation:** 

**[6923.50s] English:** That everyday person can actually feel and understand the world around them, and I think  
**Translation:** Vocabulary: chatbot: 聊天机器人

**[6926.32s] English:** That's a really good thing that people should be able to do and interact with cutting-edge AI and.  
**Translation:** 

**[6928.48s] English:** And let them feel it for themselves, yeah, because they force the technologists to have the  
**Translation:** Vocabulary: technologists: 技术人员

**[6932.90s] English:** Yeah, for sure. Yeah, that's the whole aspect of it—like you said, it's a dual-use.  
**Translation:** 

**[6937.16s] English:** Technology that we're forcibly integrating the entire humanity into it—and into the discussion.  
**Translation:** Vocabulary: forcibly: 强制地; integrating: 整合

**[6942.82s] English:** About AI, because ultimately AGI will be used for things that states use technologies for.  
**Translation:** 

**[6950.54s] English:** Which is a conflict, and so on. The more we, uh,...  
**Translation:** 

**[6956.32s] English:** Humans into this picture by having chats with them.  
**Translation:** 

**[6960.00s] English:** More we will guide, and yes, we will be able to adapt; society will be able to adapt to these technologies like.  
**Translation:** 

**[6965.24s] English:** We've always done in the past with the incredible technologies we've invented in the past.  
**Translation:** 

**[6970.04s] English:** Do you think there will be something like a Manhattan Project where, um, there will be an  
**Translation:** 

**[6978.72s] English:** Escalation of the power of this technology in states, in their old way of thinking, we'll try.  
**Translation:** 

**[6983.02s] English:** To use it as weapons technologies, and there will be this kind of escalation—I hope not—um, I think.  
**Translation:** Vocabulary: escalation: 升级

**[6989.18s] English:** That would be very dangerous to do, and I think also not the right use of the.  
**Translation:** 

**[6996.48s] English:** Technology; I hope we'll end up with more that's more collaborative, if needed, like more of a  
**Translation:** Vocabulary: collaborative: 合作的

**[7002.32s] English:** Like a CERN project, you know, where it's research-focused and the best minds in the world.  
**Translation:** 

**[7009.16s] English:** Come together to carefully complete the final steps and make sure it's responsibly done before...  
**Translation:** Vocabulary: responsibly: 有责任感地

**[7016.26s] English:** You know, like deploying it to the world, we'll see.  
**Translation:** 

**[7019.18s] English:** I mean, it's difficult with the current geopolitical climate to see cooperation, but  
**Translation:** Vocabulary: deploying: 部署; geopolitical: 地缘政治的

**[7024.88s] English:** Things can change, and, um, I think, at least on the scientific level, it's important for the  
**Translation:** 

**[7030.08s] English:** Researchers should keep in touch and stay close to each other at least on those occasions.  
**Translation:** 

**[7035.58s] English:** Kinds of topics, yeah, and I personally believe on the education side and immigration side, it  
**Translation:** 

**[7041.16s] English:** It would be great if people from the West immigrated to China, and China immigrated back.  
**Translation:** Vocabulary: immigrated: 迁移

**[7049.18s] English:** The human aspect of people just intermixing, yeah, and thereby those ties grow strong, so you can't sort of  
**Translation:** 

**[7055.84s] English:** Divide against each other in this kind of old-school way of thinking, and so on, but also multicultural.  
**Translation:** Vocabulary: intermixing: 混合; multicultural: 多元文化

**[7062.60s] English:** Multidisciplinary research teams are working on scientific questions—that's like the hope.  
**Translation:** 

**[7067.06s] English:** Don't let the warm leaders who are warmongers because they divide us, I think. Science,  
**Translation:** Vocabulary: multidisciplinary: 跨学科的; warmongers: 挑起争端的人

**[7072.58s] English:** Is the ultimate really beautiful connector, yeah? Science has always been, I think, quite a  
**Translation:** 

**[7078.04s] English:** Very collaborative and  
**Translation:** Vocabulary: collaborative: 合作的; connector: 连接器

**[7079.18s] English:** Ever and  
**Translation:** 

**[7080.00s] English:** And, you know, scientists know that it's a collective endeavor as well.  
**Translation:** Vocabulary: endeavor: 努力

**[7083.54s] English:** And we can all learn from each other. So, perhaps it could be a vector to get a bit of cooperation.  
**Translation:** 

**[7088.20s] English:** What's your ridiculous question? What's your P-Doom? (Probability of the human civilization destroying itself.)  
**Translation:** 

**[7093.90s] English:** Well, look, I don't have a P-Doom number, you know.  
**Translation:** 

**[7099.94s] English:** The reason I don't is because I think it would imply a level of precision that is not there.  
**Translation:** 

**[7105.96s] English:** So, I don't know how people are getting their P-Doom numbers.  
**Translation:** 

**[7109.00s] English:** I think it's a kind of a little bit of a ridiculous notion, because what I would say is that it's definitely non-zero and it's probably non-negligible.  
**Translation:** 

**[7118.72s] English:** So, that in itself is pretty sobering. And, my view is that it's just hugely uncertain.  
**Translation:** 

**[7124.98s] English:** Right. What these technologies are going to be able to do, how fast they are going to take off, and how controllable they are going to be.  
**Translation:** Vocabulary: hugely: 非常; sobering: 令人警醒

**[7130.74s] English:** Some things may turn out to be, and hopefully, way easier than we thought.  
**Translation:** 

**[7134.74s] English:** Right. But it may be that there's some really hard.  
**Translation:** 

**[7137.84s] English:** Problems that are harder than we guessed today.  
**Translation:** 

**[7139.84s] English:** And I think we don't know that for sure.  
**Translation:** 

**[7141.84s] English:** And so, under those conditions of a lot of uncertainty, but huge stakes both ways, you know, on the one hand, we could solve all diseases, energy problems, the scarcity problem—and then travel to the stars, consciousness of the stars, and maximum human flourishing.  
**Translation:** 

**[7158.84s] English:** On the other hand, there are these sorts of P-Doom scenarios.  
**Translation:** Vocabulary: consciousness: 意识; flourishing: 繁荣; scarcity: 短缺; scenarios: 情景; stakes: 利害

**[7160.84s] English:** So, given the uncertainty around it and the importance of it, it's clear to me that the only rational and sensible way to solve it is to do so.  
**Translation:** 

**[7165.56s] English:** And that's what we're trying to do.  
**Translation:** Vocabulary: sensible: 合理的

**[7166.52s] English:** And that's what we're trying to do.  
**Translation:** 

**[7167.02s] English:** And that's what we're trying to do.  
**Translation:** 

**[7167.52s] English:** And that's what we're trying to do.  
**Translation:** 

**[7167.72s] English:** The idea behind that is that we think.  
**Translation:** 

**[7169.14s] English:** As a nonsocietal world, I think it's going to be a very, very useful approach to proceed with cautious optimism.  
**Translation:** 

**[7174.14s] English:** So, we want the outcome, we want the benefits, of course.  
**Translation:** Vocabulary: nonsocietal: 非社会性的; optimism: 乐观

**[7178.32s] English:** Uh, and all of the amazing things that AI can bring.  
**Translation:** 

**[7183.22s] English:** And actually, I would be really worried about humanity if I were given the other challenges we have—climate, you know, aging, resources—and all of that.  
**Translation:** 

**[7193.46s] English:** If I didn't know that AI was coming down the line.  
**Translation:** 

**[7196.18s] English:** Right.  
**Translation:** 

**[7196.48s] English:** How would we solve all those other problems?  
**Translation:** 

**[7197.72s] English:** Amazingly transformative for good.  
**Translation:** 

**[7200.00s] English:** But on the other hand, there are these risks that we know are there, but we can't quite quantify. So, the best thing to do is to use the scientific method to do more research to try and more precisely define those risks, and, of course, address them. And I think that's what we're doing. I think there probably needs to be 10 times more effort in that than there is now as we're getting closer and closer to the AGI line.  
**Translation:** 

**[7227.78s] English:** What would be the source of worry for you more: human-caused or AI/AGI-caused?  
**Translation:** Vocabulary: precisely: 准确地; quantify: 量化

**[7235.08s] English:** Humans abusing that technology versus AGI itself, through a mechanism that you've spoken about—fascinating deception or this kind of stuff—that gets better and better and better, secretly.  
**Translation:** 

**[7244.56s] English:** I think they operate on different timescales, and they're equally important to address.  
**Translation:** Vocabulary: abusing: 滥用; deception: 欺骗; timescales: 时间尺度

**[7250.18s] English:** So, there's just a common garden variety of bad actors using new technology—in this case, journalism.  
**Translation:** 

**[7257.78s] English:** And that's a huge risk.  
**Translation:** Vocabulary: journalism: 新闻业

**[7262.88s] English:** And I think that has a lot of complications because, generally, you know, I'm in huge favor of open science and open source.  
**Translation:** 

**[7270.78s] English:** And, in fact, we did it with all our science projects, like AlphaFold, and all of those things, for the benefit of the scientific community.  
**Translation:** 

**[7278.18s] English:** But how does one restrict bad actors' access to these powerful systems, whether they're individuals or even rogue states?  
**Translation:** 

**[7286.24s] English:** And but enable access.  
**Translation:** Vocabulary: rogue: 叛逆的国家

**[7288.38s] English:** At the same time, for good actors, to maximally build upon it is pretty tricky; a problem that I've not heard a clear solution to.  
**Translation:** 

**[7296.78s] English:** So, there's the bad-actor use-case problem.  
**Translation:** Vocabulary: maximally: 最大程度上; tricky: 棘手的

**[7298.70s] English:** And then, there's obviously the question of how we ensure the guardrails remain effective as the systems become more genetic and closer to AGI and more autonomous. How do we keep them under our control and aligned with our intentions?  
**Translation:** 

**[7312.28s] English:** Yeah, I tend to worry more about the humans, the bad actors, given that my mind is limited.  
**Translation:** Vocabulary: aligned: 一致; autonomous: 自主; guardrails: 防护栏

**[7317.78s] English:** And there it could be.  
**Translation:** 

**[7320.00s] English:** So, in part, how do you prevent destructive technology from falling into the hands of bad actors? But, from another perspective, given the geopolitical implications of technology, how do you reduce the number of bad actors in the world? That's also an interesting human problem.  
**Translation:** Vocabulary: geopolitical: 地缘政治的; implications: 影响

**[7333.94s] English:** Yeah, it's a hard problem. I mean, look, we can maybe also use the technology itself to help with early warning on some of the bad actor use cases, right? Whether that's bio or nuclear or whatever it is—like, AI could be potentially helpful there—as long as the AI you're using is itself reliable, right?  
**Translation:** 

**[7356.26s] English:** So, it's a sort of interlocking problem, and that's what makes it very tricky. And again, it may require some international agreement, at least potentially.  
**Translation:** 

**[7363.94s] English:** Between China and the U.S., there should be some basic standards, right?  
**Translation:** 

**[7370.36s] English:** I have to ask you about the book, "The Maniac." There's this "hand of God" moment: Lisa Dahl's move 78, that perhaps was the last time a human did a move of sort of pure human genius and beat AlphaGo—or like broke its brain.  
**Translation:** Vocabulary: maniac: 狂热爱好者

**[7388.40s] English:** Yes.  
**Translation:** 

**[7388.54s] English:** Sorry to anthropomorphize, but it's an interesting moment, because I think in so many domains, it will keep happening.  
**Translation:** Vocabulary: anthropomorphize: 赋予人类特征

**[7393.94s] English:** Yeah, it's a special moment. And, you know, it was great for Lisa Dahl. And, you know, I think it's, in a way, they were sort of inspiring each other. We as a team were inspired by Lisa Dahl's brilliance and nobleness. And then maybe he got inspired by, you know, what AlphaGo was doing to then conjure this incredible, inspirational moment. It's all, you know, captured very well in the documentary about it. And I think that will continue in many domains where there's this kind of collaboration at least for the foreseeable future.  
**Translation:** 

**[7423.94s] English:** The future of humanity lies in bringing in ingenuity, asking the right questions, and then utilizing these tools in a way that cracks a problem.  
**Translation:** Vocabulary: brilliance: 卓越; collaboration: 合作; conjure: 创造; cracks: 破解; foreseeable: 可预见的; ingenuity: 创造力; inspirational: 启发性的; nobleness: 高尚; utilizing: 利用

**[7438.08s] English:** Yeah, what becomes of AI as it gets smarter?  
**Translation:** 

**[7440.00s] English:** And, smarter: one of the interesting questions we can ask ourselves is what makes humans special.  
**Translation:** 

**[7445.08s] English:** It does feel, um, perhaps biased that we humans are deeply special. I don't know if it's our  
**Translation:** 

**[7452.68s] English:** Intelligence, it could be something else—that other thing that's outside the mad dreams of...  
**Translation:** Vocabulary: biased: 有偏见的

**[7459.68s] English:** Reason, I think that's what I've always imagined—uh, when I was a kid and starting on this journey.  
**Translation:** 

**[7465.06s] English:** Of, like, um, I was, of course, fascinated by things like consciousness and did a neuroscience PhD.  
**Translation:** Vocabulary: consciousness: 觉醒; fascinated: 着迷; neuroscience: 神经科学

**[7471.06s] English:** Look at how the brain works, especially imagination and memory. I focused on the hippocampus, and it's  
**Translation:** 

**[7475.72s] English:** Sort of going to be interesting. I always thought the best way, of course, one can come philosophize.  
**Translation:** Vocabulary: hippocampus: 海马区; philosophize: 哲学思考

**[7479.98s] English:** About it, and have thought experiments, and maybe even do actual experiments, like you do in,...  
**Translation:** 

**[7484.52s] English:** Neuroscience on real brains, but in the end, I always imagined building AI to be a kind of  
**Translation:** Vocabulary: experiments: 实验

**[7490.16s] English:** Intelligent artifact, and then comparing that to the human mind and seeing what the differences are.  
**Translation:** 

**[7494.44s] English:** Were  
**Translation:** Vocabulary: artifact: 人工制品

**[7494.94s] English:** Uh, would be the best way to uncover what's special about the human mind if, indeed, there  
**Translation:** 

**[7499.70s] English:** Is anything special? And I suspect there probably is, but it's going to be hard to, you know, I think.  
**Translation:** Vocabulary: uncover: 揭露

**[7504.52s] English:** This journey we're on will help us understand that and define it, and you know, there may be a  
**Translation:** 

**[7509.60s] English:** The difference between carbon-based substrates that we use and silicon when they process.  
**Translation:** Vocabulary: silicon: 硅; substrates: 基底

**[7515.14s] English:** Information you know, one of the best definitions I like of consciousness is it's the way  
**Translation:** 

**[7519.78s] English:** Information feels when we process it right, um, it could be; I mean, it's not very  
**Translation:** 

**[7524.74s] English:** A helpful way to understand it, but it's a way to understand it, and it's a way to understand it.  
**Translation:** 

**[7524.92s] English:** But it's a way to understand it, and it's a way to understand it, and it's a helpful scientific.  
**Translation:** 

**[7525.80s] English:** Explanation: I think it's kind of interesting, an intuitive one, and, you know,  
**Translation:** 

**[7530.74s] English:** On this scientific journey we're on, I think it will help uncover that mystery.  
**Translation:** Vocabulary: intuitive: 直觉的

**[7536.14s] English:** Yeah, what I cannot create, I do not understand. That's, uh, somebody you deeply admire, Richard.  
**Translation:** 

**[7541.46s] English:** Feinman, as you mentioned, you also reach for Wigner's dreams of universality that he  
**Translation:** Vocabulary: cannot: 不能; universality: 普遍性

**[7548.54s] English:** Saw in constrained domains, but also broadly, generally in mathematics and so on, so forth.  
**Translation:** 

**[7554.92s] English:** Aspects on which you're pushing towards not to start trouble at the end, but uh, Roger.  
**Translation:** Vocabulary: broadly: 广泛地; constrained: 受限的

**[7560.00s] English:** Penrose: Yes, okay, so, you know, do you think consciousness—there's this hard problem of...  
**Translation:** 

**[7567.40s] English:** Consciousness: how information feels. Um, do you think consciousness, first of all, is a computation?  
**Translation:** Vocabulary: computation: 计算; consciousness: 意识

**[7574.98s] English:** And if it is information processing, as you said, is everything it something that could  
**Translation:** 

**[7581.52s] English:** Be modeled by a classical computer, yeah? Or is it a quantum-mechanical in nature? Well, let's look at it.  
**Translation:** Vocabulary: modeled: 模拟

**[7586.78s] English:** Penrose is an amazing thinker, one of the greatest of the modern era, and he's someone we've had a lot of.  
**Translation:** 

**[7590.84s] English:** Discussions about this, of course, we cordially disagree. Which is, you know, I feel like, um, I  
**Translation:** Vocabulary: cordially: 友好地; thinker: 思想家

**[7596.62s] English:** Meaning he collaborated with a lot of good neuroscientists to see if he could find mechanisms.  
**Translation:** 

**[7600.60s] English:** For quantum mechanics behavior in the brain, and they, to my knowledge, haven't found anything.  
**Translation:** Vocabulary: collaborated: 合作; neuroscientists: 神经科学家; quantum: 量子

**[7606.00s] English:** Um, convincing, yet so, my betting is that it's mostly just classical.  
**Translation:** 

**[7612.54s] English:** Computing that's going on in the brain, which suggests that all the phenomena,...  
**Translation:** Vocabulary: computing: 计算

**[7616.78s] English:** Are modelable or mimicable by a classical computer, but we'll see—you know—that there.  
**Translation:** 

**[7622.88s] English:** May be this final, mysterious thing: the feeling of consciousness, the qualia, these kinds of things.  
**Translation:** Vocabulary: mimicable: 可模仿; modelable: 可建模; qualia: 主观体验

**[7628.66s] English:** That philosophers debate whether consciousness is unique to the substrate; we may even come to understand this.  
**Translation:** 

**[7634.24s] English:** That, when we do things like neural links and have neural interfaces to AI systems, which I  
**Translation:** Vocabulary: interfaces: 接口; neural: 神经的; philosophers: 哲学家; substrate: 基底

**[7640.46s] English:** Think we probably will eventually, um, maybe to keep up with the AI systems, uh, we might actually be.  
**Translation:** 

**[7646.12s] English:** Able to feel for our own consciousness, and we might be able to feel for our own consciousness.  
**Translation:** 

**[7646.78s] English:** What it's like to compute on silicon, right? So, um, and maybe that will tell us, uh, so I think it's—it's  
**Translation:** 

**[7655.60s] English:** Going to be interesting, and I had a debate once with the late Daniel Dennett about why we think.  
**Translation:** Vocabulary: compute: 计算; silicon: 硅

**[7660.46s] English:** Each other are conscious, okay? So it's for two reasons: one is that you're exhibiting the same behavior.  
**Translation:** 

**[7664.88s] English:** That I am, so that's one thing: behaviorally, you seem like a conscious being. If I am, but the second...  
**Translation:** Vocabulary: exhibiting: 表现

**[7670.28s] English:** The thing which is often overlooked is that we're running on the same substrate, so if you're  
**Translation:** 

**[7674.32s] English:** Behaving in the same way, and we're running on the same substrate.  
**Translation:** Vocabulary: behaving: 行为; overlooked: 忽视

**[7676.78s] English:** It's most parsimonious to assume you're feeling the same.  
**Translation:** 

**[7680.00s] English:** That I'm feeling, but with an AI that's on silicon, we won't be able to rely on the second.  
**Translation:** Vocabulary: parsimonious: 节俭的

**[7686.12s] English:** Part, even if it exhibits the first part of that behavior, looks like it is driven by conscious.  
**Translation:** 

**[7689.94s] English:** Being it might even claim it is, um, but we but we wouldn't know how it actually felt, um, and it.  
**Translation:** Vocabulary: exhibits: 表现

**[7697.24s] English:** Probably couldn't have known what we felt, at least in the first stages, maybe when we get to super.  
**Translation:** 

**[7701.64s] English:** Intelligence and the technologies that build it; perhaps we'll be able to bridge that gap.  
**Translation:** 

**[7706.30s] English:** That's a huge test for radical empathy: to empathize with a different substrate, right?  
**Translation:** 

**[7712.42s] English:** Exactly, we never had to confront that before. Yeah, so maybe maybe through brain-computer.  
**Translation:** Vocabulary: confront: 面对; empathize: 共情; empathy: 共情

**[7717.84s] English:** Interfaces should be able to truly empathize with what it feels like to be a computer.  
**Translation:** 

**[7721.76s] English:** Well, for information to be computed not on a carbon-based system, I mean that's deeply interesting.  
**Translation:** Vocabulary: computed: 计算; interfaces: 接口

**[7728.36s] English:** People kind of think about that with plants, with other life forms, which could be exactly similar.  
**Translation:** 

**[7732.88s] English:** Substrate, but sufficiently far enough.  
**Translation:** Vocabulary: substrate: 基质; sufficiently: 足够地

**[7736.30s] English:** On the uh evolutionary tree, yeah, that it requires radical empathy, but to do that with...  
**Translation:** 

**[7741.86s] English:** A computer, I mean. No, we sort of have animal studies on this, of course, involving higher animals.  
**Translation:** Vocabulary: evolutionary: 进化的

**[7746.40s] English:** Like, you know, killer whales and dolphins and dogs and monkeys—they have some too.  
**Translation:** 

**[7752.38s] English:** Elephants, you know, they have some aspects certainly of consciousness, right, even though they're not  
**Translation:** 

**[7756.68s] English:** Might not be that smart on an IQ sense, so we can already empathize with that, and maybe.  
**Translation:** 

**[7762.06s] English:** Even some of our systems, one day, like we built this thing called Dolphin Gemma, you know?  
**Translation:** Vocabulary: dolphin: 海豚; gemma: 宝石

**[7766.14s] English:** Could be a computer, or could be a computer, or could be a computer, or could be a computer.  
**Translation:** 

**[7766.30s] English:** And one, a version of our system was trained on dolphin and whale sounds, and maybe we'll be able  
**Translation:** 

**[7771.14s] English:** To build an interpreter or translator at some point, which would be pretty cool, what gives you?  
**Translation:** 

**[7775.86s] English:** Hope for the future of human civilization. Well, what gives me hope is that I think our almost limitless  
**Translation:** Vocabulary: interpreter: 口译员; limitless: 无穷的; translator: 翻译器

**[7782.40s] English:** Ingenuity: First of all, I think the best of us and the best human minds are incredible, um, and you  
**Translation:** 

**[7789.84s] English:** Know, I love watching humans when they're at the top of their game, whether that's  
**Translation:** Vocabulary: ingenuity: 发明创造

**[7796.14s] English:** Sports, or science, or art—you know, it's just nothing more than that.  
**Translation:** 

**[7800.00s] English:** Than that, seeing them in their element in flow, I think it's almost limitless. Our brains,  
**Translation:** 

**[7804.82s] English:** Are general systems intelligent systems? So, I think it's almost limitless what we can potentially do.  
**Translation:** 

**[7810.72s] English:** With them, and then the other thing is our extreme adaptability. I think it's gonna be okay in terms of...  
**Translation:** Vocabulary: adaptability: 适应性

**[7817.56s] English:** Of, there's going to be a lot of change, but look where we are now without effectively our.  
**Translation:** 

**[7822.88s] English:** Hunter-gatherer brains: How is it that we can, you know, cope with the modern world, right? Flying on.  
**Translation:** 

**[7829.40s] English:** Planes doing podcasts, you know, playing computer games, and virtual simulations—I mean, it's already  
**Translation:** 

**[7835.42s] English:** Mind-blowing, given that our minds were developed for, you know, hunting buffaloes on the open plains.  
**Translation:** Vocabulary: buffaloes: 野牛; simulations: 模拟

**[7840.32s] English:** Tundra: And, and so I think this is just the next step, and it's actually kind of interesting.  
**Translation:** 

**[7845.94s] English:** To see how society has already adapted to this mind-blowing AI technology, we have today already.  
**Translation:** 

**[7851.12s] English:** It's sort of like, oh, I talk to chatbots totally fine, and it's very possible that this very well might be one.  
**Translation:** 

**[7856.34s] English:** Podcast activity, which I'm here for.  
**Translation:** Vocabulary: chatbots: 聊天机器人

**[7859.40s] English:** Completely replaced by AI, I'm very replaceable, and I'm waiting—not to the level that you can do it.  
**Translation:** 

**[7863.92s] English:** Lex, I don't think I thank you, but that's what humans do to each other—we complement.  
**Translation:** Vocabulary: replaceable: 可以替代的

**[7867.86s] English:** All right, and I'm deeply grateful that we humans have this infinite capacity for.  
**Translation:** 

**[7873.92s] English:** Curiosity, adaptability, like you said, and also compassion and the ability to love—exactly all of  
**Translation:** Vocabulary: compassion: 同情; infinite: 无限

**[7879.30s] English:** Those human things that are deeply human. Well, this is a huge honor, Demis. You're one of the  
**Translation:** 

**[7884.14s] English:** Truly special humans in the world, uh, thank you so much for doing what you do and for talking to me.  
**Translation:** 

**[7889.40s] English:** Today, well, thank you very much, Lex. Thanks for listening to this conversation with Demis Kasabas.  
**Translation:** 

**[7894.52s] English:** To support this podcast, please check out our sponsors in the description and consider subscribing.  
**Translation:** Vocabulary: sponsors: 赞助商; subscribing: 订阅

**[7900.18s] English:** To this channel, and now let me answer some questions and try to articulate some things.  
**Translation:** 

**[7907.02s] English:** I've been thinking about whether you'd like to submit questions, including in audio and video form. Go to  
**Translation:** Vocabulary: articulate: 表达; submit: 提交

**[7912.96s] English:** LexFreeman.com/slash/AMA: I got a lot of amazing questions, thoughts, and requests from folks.  
**Translation:** 

**[7919.40s] English:** I'll keep trying.  
**Translation:** 

**[7920.00s] English:** Pick some randomly and comment on it at the end of every episode. I got a note on May 21st, this year.  
**Translation:** 

**[7928.64s] English:** That said, hi Lex. Twenty years ago today, David Foster Wallace delivered his famous "This Is Water" speech.  
**Translation:** Vocabulary: foster: 培养; wallace: 瓦尔劳

**[7936.04s] English:** At Kenyon College. What do you think of this speech? Well, first, I think this is probably  
**Translation:** 

**[7944.58s] English:** One of the greatest and most unique commencement speeches ever given. But of course, I have many.  
**Translation:** Vocabulary: commencement: 毕业

**[7951.76s] English:** Favorites, including the one by Steve Jobs. And David Foster Wallace is one of my favorites.  
**Translation:** 

**[7957.68s] English:** Writers, and one of my favorite humans: there's a tragic honesty to his work, and it always felt  
**Translation:** 

**[7966.18s] English:** As if he was engaging in a constant battle with his own mind. And his writing,  
**Translation:** 

**[7973.08s] English:** Were kind of his notes.  
**Translation:** 

**[7974.58s] English:** Notes from the front lines of that battle. Now, onto the speech. Let me quote some parts.  
**Translation:** 

**[7981.90s] English:** There's, of course, the parable of the fish and the water: "That's how things are," go these two young fish.  
**Translation:** Vocabulary: parable: 寓言

**[7988.18s] English:** Swimming along, and they happen to meet an older fish swimming the other way, who nods at them and  
**Translation:** 

**[7995.28s] English:** Says, "Morning, boys. How's the water?" And the two young fish swim on for a bit, and eventually one  
**Translation:** 

**[8003.58s] English:** Of them looks over at the other and says, "Hey, how's the water?" And he says, "Hey, how's the  
**Translation:** 

**[8004.56s] English:** Other? And he asks, "What the hell is water?" In the speech, David Foster Wallace goes on to say,  
**Translation:** 

**[8012.94s] English:** The point of the fish story is merely that the most obvious, important realities are often the easiest to overlook.  
**Translation:** 

**[8018.06s] English:** Those are the ones that are hardest to see and talk about. Stated as an English sentence, of course.  
**Translation:** Vocabulary: overlook: 忽视; realities: 现实

**[8023.66s] English:** This is just a banal platitude. But the fact is that, in the day-to-day trenches of adulthood,...  
**Translation:** 

**[8029.34s] English:** Existence, banal platitudes can have a life-or-death importance. Or so I wish to say.  
**Translation:** Vocabulary: platitude: 陈词滥调; platitudes: 陈词滥调; trenches: 战壕

**[8034.56s] English:** To you in this dry and lovely morning, I have several takeaways from this.  
**Translation:** 

**[8040.00s] English:** Parable and the speech that follows. First, I think we must question everything, and in particular,...  
**Translation:** Vocabulary: takeaways: 收获

**[8046.94s] English:** The most basic assumptions about our reality, our life, and the very nature of existence,  
**Translation:** 

**[8053.66s] English:** And that this project is a deeply personal one. In some fundamental sense, nobody can really help.  
**Translation:** Vocabulary: assumptions: 假设

**[8060.14s] English:** You're in this process of discovery. The call to action here, I think, from David Foster Wallace,  
**Translation:** 

**[8067.78s] English:** As he puts it, is to be "just a little less arrogant, and to have just a little more critical.  
**Translation:** Vocabulary: arrogant: 骄傲

**[8074.96s] English:** Awareness about myself and my certainties, because a huge percentage of the stuff that I tend to be  
**Translation:** 

**[8081.80s] English:** Automatically, certain of it is; it turns out, is totally wrong and deluded. All right, back to me.  
**Translation:** Vocabulary: certainties: 确信; deluded: 错觉

**[8090.62s] English:** Lex speaking. The second takeaway is that the central spiritual battles of our lives are often internal.  
**Translation:** 

**[8096.50s] English:** Are not fun.  
**Translation:** Vocabulary: takeaway: 要点

**[8097.78s] English:** It is not fought on a mountaintop somewhere at a meditation retreat, but it is fought in the mundane.  
**Translation:** 

**[8105.30s] English:** Moments of daily life. The third takeaway is that we too easily give away our time and attention.  
**Translation:** Vocabulary: mountaintop: 山顶; mundane: 平凡; retreat: 静修

**[8113.44s] English:** To the multitude of distractions that the world feeds us, the insatiable black holes of attention.  
**Translation:** 

**[8122.90s] English:** David Foster Wallace's call to action, in this case, is to be deeply aware of the  
**Translation:** Vocabulary: distractions: 分散注意力的东西; foster: 培养; insatiable: 贪得无厌的; multitude: 众多

**[8127.78s] English:** Beauty in each moment, and to find meaning in the mundane. I often quote David Foster Wallace in his  
**Translation:** 

**[8136.68s] English:** Advice that the key to life is to be unboresome. And I think this is exactly right. Every moment,  
**Translation:** Vocabulary: unboresome: 不单调

**[8144.30s] English:** Every object, every experience, when looked at closely enough, contains within it infinite.  
**Translation:** 

**[8151.58s] English:** Richness to explore. And since Demis Kassabas, of this very podcast episode,...  
**Translation:** Vocabulary: infinite: 无穷的

**[8157.78s] English:** And we are such fans of Richard Feynman.  
**Translation:** 

**[8160.00s] English:** Allow me to also quote Mr. Feynman on this topic as well.  
**Translation:** Vocabulary: feynman: 费曼

**[8165.62s] English:** I have a friend who's an artist.  
**Translation:** 

**[8168.66s] English:** And has sometimes taken a view that I don't agree with very well.  
**Translation:** 

**[8174.38s] English:** He'll hold up a flower and say, "Look how beautiful it is.  
**Translation:** 

**[8178.16s] English:** And I'll agree.  
**Translation:** 

**[8179.92s] English:** Then he says, "I, as an artist, can see how beautiful this is.  
**Translation:** 

**[8184.70s] English:** But, you as a scientist take this all apart, and it becomes a dull thing.  
**Translation:** 

**[8190.00s] English:** And I think that's kind of nutty.  
**Translation:** 

**[8193.12s] English:** First of all, the beauty that he sees is available to other people.  
**Translation:** Vocabulary: nutty: 荒谬的

**[8197.66s] English:** And to me, too; I believe.  
**Translation:** 

**[8200.28s] English:** Although I may not be quite as refined aesthetically as he is,  
**Translation:** Vocabulary: aesthetically: 审美; refined: 有品味

**[8204.74s] English:** I can appreciate the beauty of a flower.  
**Translation:** 

**[8207.96s] English:** At the same time, I see much more about the flower than he does.  
**Translation:** 

**[8212.66s] English:** I can imagine the cells in there.  
**Translation:** 

**[8214.78s] English:** The complicated actions, inside which also have beauty.  
**Translation:** 

**[8218.36s] English:** I mean,  
**Translation:** 

**[8219.20s] English:** It's not just beauty at this dimension; at one centimeter.  
**Translation:** Vocabulary: dimension: 维度

**[8222.94s] English:** There's also beauty at smaller dimensions.  
**Translation:** 

**[8225.48s] English:** The inner structure, as well as the processes.  
**Translation:** Vocabulary: dimensions: 尺寸

**[8228.22s] English:** The fact that the colors in the flowers evolved,  
**Translation:** 

**[8230.36s] English:** In order to attract insects to pollinate, it is interesting.  
**Translation:** Vocabulary: evolved: 演化; pollinate: 授粉

**[8234.60s] English:** It means that the insects can see the color.  
**Translation:** 

**[8237.54s] English:** It adds a question.  
**Translation:** 

**[8238.98s] English:** Does this aesthetic sense also exist in lower forms?  
**Translation:** 

**[8242.84s] English:** Why is it aesthetically pleasing?  
**Translation:** Vocabulary: aesthetic: 审美

**[8244.48s] English:** All kinds of interesting questions,  
**Translation:** 

**[8246.46s] English:** Which science knowledge only adds to the excitement,  
**Translation:** 

**[8249.20s] English:** The mystery,  
**Translation:** 

**[8250.70s] English:** And the awe of a flower.  
**Translation:** 

**[8252.94s] English:** It only adds.  
**Translation:** 

**[8256.38s] English:** All right, back to David Foster Wallace's speech.  
**Translation:** Vocabulary: foster: 培养

**[8259.74s] English:** He has a great story in there that I particularly enjoy.  
**Translation:** 

**[8265.22s] English:** It goes,  
**Translation:** 

**[8266.82s] English:** There are these two guys sitting together in a bar.  
**Translation:** 

**[8269.50s] English:** In the remote Alaskan wilderness.  
**Translation:** Vocabulary: alaskan: 阿拉斯加的; wilderness: 荒野

**[8271.78s] English:** One of the guys is religious.  
**Translation:** 

**[8273.66s] English:** The other is an atheist.  
**Translation:** Vocabulary: atheist: 无神论者

**[8275.58s] English:** And the two are arguing about the existence of God.  
**Translation:** 

**[8278.52s] English:** With the people of Alaska.  
**Translation:** 

**[8279.08s] English:** And the other is an atheist.  
**Translation:** 

**[8279.18s] English:** And that's special.  
**Translation:** 

**[8280.00s] English:** Intensity that comes after about the fourth beer. And the atheist says, "Look, it's not like I don't.  
**Translation:** 

**[8285.70s] English:** Have actual reasons for not believing in God. It's not like I haven't ever experimented with.  
**Translation:** 

**[8291.44s] English:** The whole God and prayer thing. Just last month, I got caught away from the camp in that terrible.  
**Translation:** 

**[8297.70s] English:** Blizzard. And I was totally lost. And I couldn't see a thing. And it was 50 below. And so I tried.  
**Translation:** Vocabulary: blizzard: 暴风雪

**[8305.18s] English:** It. I fell to my knees in the snow and cried out, "Oh God, if there is a God, I'm lost in this.  
**Translation:** 

**[8311.16s] English:** Blizzard. And I'm going to die if you don't help me. And now, back in the bar, the religious guy...  
**Translation:** 

**[8317.34s] English:** Looks at the atheist all puzzled. "Well, then you must believe now," he says. After all, there you  
**Translation:** 

**[8323.82s] English:** Are they alive? The atheist just rolls his eyes. "No, man. All that happened was a couple of Eskimos.  
**Translation:** Vocabulary: eskimos: 爱斯基摩人; puzzled: 困惑的

**[8330.96s] English:** Happened to be wandering by and showed me the way back to the camp.  
**Translation:** 

**[8336.16s] English:** All this, I think, teaches us that everything is a matter of perspective, and that wisdom may arrive  
**Translation:** 

**[8343.30s] English:** If we have the humility to keep shifting and expanding our perspective on the world.  
**Translation:** 

**[8350.96s] English:** Thank you for allowing me to talk a bit about David Foster Wallace.  
**Translation:** Vocabulary: foster: 培养; humility: 谦逊; shifting: 转变

**[8354.62s] English:** He's one of my favorite writers, and he's a beautiful soul.  
**Translation:** 

**[8360.02s] English:** If I may, one more thing I wanted to briefly comment on.  
**Translation:** 

**[8363.72s] English:** I find myself to be in the middle of a world where I'm not alone. I find myself to be in  
**Translation:** 

**[8365.16s] English:** This strange position of getting attacked online often, from all sides, including being lied about.  
**Translation:** 

**[8372.76s] English:** Sometimes through selective misrepresentation, but often through downright lies. I don't know.  
**Translation:** 

**[8378.58s] English:** How else to put it? This all breaks my heart, frankly. But I've come to understand that it's  
**Translation:** Vocabulary: frankly: 坦白讲; selective: 挑拣的

**[8384.92s] English:** The way of the Internet and the cost of the path I've chosen. There have been days when it's been  
**Translation:** 

**[8390.60s] English:** Rough on me mentally. It's not fun being lied to.  
**Translation:** 

**[8395.16s] English:** Especially when it's about things that are usually, for a long time, have been a  
**Translation:** 

**[8400.00s] English:** Source of happiness and joy for me. But again, that's life. I'll continue exploring the world.  
**Translation:** 

**[8406.38s] English:** Of people and ideas with empathy and rigor, I wire my heart on my sleeve as much as I can.  
**Translation:** 

**[8414.18s] English:** For me, that's the only way to live. Anyway, a common attack on me is about my time at MIT.  
**Translation:** Vocabulary: empathy: 共情; rigor: 严谨

**[8421.40s] English:** And Drexel, two great universities I love and have tremendous respect for.  
**Translation:** 

**[8426.70s] English:** Since a bunch of lies have accumulated online about me on these topics, to a sad and at times heartbreaking extent,  
**Translation:** Vocabulary: accumulated: 累积; heartbreaking: 令人心碎的

**[8433.46s] English:** Hilariously, I thought I would once more state the obvious facts about my bio.  
**Translation:** 

**[8438.10s] English:** For the small number of you who may care: TLGR, two things. First, as I often say,  
**Translation:** Vocabulary: hilariously: 可笑地

**[8445.76s] English:** Including in a recent podcast episode, which somehow was listened to by many millions of people,  
**Translation:** 

**[8451.52s] English:** I proudly went to Drexel University for my bachelor's and master's.  
**Translation:** Vocabulary: drexel: 德雷塞尔大学; proudly: 自豪地

**[8456.64s] English:** And master's degrees. I went to the University of New York for my bachelor's.  
**Translation:** 

**[8456.68s] English:** Master's and master's degrees. I went to the University of New York for my bachelor's.  
**Translation:** 

**[8456.70s] English:** And doctorate degrees. Second, I am a research scientist at MIT and have been there in a paid  
**Translation:** 

**[8464.80s] English:** Research position for the last 10 years. Allow me to elaborate a bit more on these two things now.  
**Translation:** Vocabulary: elaborate: 详述

**[8471.68s] English:** But please skip if this is not at all interesting. So, as I said, a common attack on me is that  
**Translation:** 

**[8478.04s] English:** I have no real affiliation with MIT. The accusation, I guess, is that I'm falsely.  
**Translation:** Vocabulary: accusation: 指控; affiliation: 关联; falsely: 虚假地

**[8484.36s] English:** Claiming an MIT affiliation because I'm not an MIT student. So, I'm not an MIT student.  
**Translation:** 

**[8486.68s] English:** I'm not an MIT student because I taught a lecture there once. No, that accusation against me...  
**Translation:** 

**[8492.66s] English:** Is a complete lie. I have been at MIT for over 10 years in a paid research position from 2015.  
**Translation:** 

**[8502.04s] English:** To today. To be extra clear, I'm a research scientist at MIT, working in LIDS (the Laboratory for Information and Decision Systems).  
**Translation:** 

**[8511.00s] English:** For information and decision systems in the College of Computing. For now, I'm going to.  
**Translation:** 

**[8516.66s] English:** Since I'm still at MIT.  
**Translation:** Vocabulary: computing: 计算机科学

**[8520.00s] English:** You can see me in the directory, and on the various lab pages.  
**Translation:** 

**[8525.36s] English:** I have indeed given many lectures at MIT over the years, and a small fraction of those I posted online.  
**Translation:** 

**[8533.24s] English:** Teaching, for me, has always been just for fun and not part of my research work.  
**Translation:** 

**[8538.08s] English:** I personally think I suck at it, but I have always learned and grown from the experience.  
**Translation:** 

**[8543.60s] English:** It's like Feynman said: if you want to understand something deeply, it's good to try to teach it.  
**Translation:** 

**[8552.52s] English:** But, like I said, my main focus has always been on research.  
**Translation:** Vocabulary: feynman: 费曼

**[8555.98s] English:** I published many peer-reviewed papers, which you can see in my Google Scholar profile.  
**Translation:** 

**[8562.04s] English:** For my first four years at MIT, I worked extremely intensively.  
**Translation:** Vocabulary: intensively: 专注地

**[8567.68s] English:** Most weeks were 80-100 hour workweeks.  
**Translation:** 

**[8570.64s] English:** After that, in 2019, I still kept up with my research.  
**Translation:** Vocabulary: workweeks: 工作周

**[8573.60s] English:** I split my time taking a leap to pursue projects in AI and robotics outside of MIT, and to dedicate a lot of focus to the podcast.  
**Translation:** 

**[8583.32s] English:** As I've said, I've been continuously surprised just how many hours preparing for an episode takes.  
**Translation:** Vocabulary: dedicate: 投入; robotics: 机器人学

**[8589.88s] English:** There are many episodes of the podcast for which I have to read, write, and think for 100, 200, or more hours across multiple weeks and months.  
**Translation:** 

**[8599.66s] English:** Since 2020, I have not actively published research papers.  
**Translation:** Vocabulary: actively: 积极地

**[8603.60s] English:** Just like the podcast, I think it's something that's a serious, full-time effort.  
**Translation:** 

**[8610.28s] English:** But, not publishing and doing full-time research has been eating at me.  
**Translation:** 

**[8615.66s] English:** Because I love research, and I love programming and building systems that test out interesting technical ideas, especially in the context of human-AI or human-robot interaction.  
**Translation:** 

**[8628.22s] English:** I hope to change this in the coming months and years.  
**Translation:** 

**[8632.12s] English:** What I've come to realize about myself is that I'm not just a human being.  
**Translation:** 

**[8633.32s] English:** What I've come to realize about myself is that if I don't publish or if I don't launch systems that people use, I definitely feel like I'm not a human being.  
**Translation:** 

**[8640.00s] English:** Like a piece of me is missing.  
**Translation:** 

**[8642.30s] English:** It legitimately is a source of happiness for me.  
**Translation:** Vocabulary: legitimately: 真正地

**[8646.14s] English:** Anyway, I'm proud of my time at MIT.  
**Translation:** 

**[8648.72s] English:** I was and am constantly surrounded.  
**Translation:** 

**[8652.14s] English:** By people much smarter than me, many of whom,  
**Translation:** 

**[8654.96s] English:** Have become lifelong colleagues and friends.  
**Translation:** Vocabulary: colleagues: 同行

**[8658.82s] English:** MIT is a place I go to escape the world.  
**Translation:** 

**[8661.94s] English:** To focus on exploring fascinating questions.  
**Translation:** 

**[8664.40s] English:** At the cutting edge of science and engineering.  
**Translation:** 

**[8667.14s] English:** This, again, makes me truly happy.  
**Translation:** 

**[8670.30s] English:** And it does hit pretty hard on a psychological level.  
**Translation:** 

**[8674.84s] English:** When I'm getting attacked over this.  
**Translation:** 

**[8678.32s] English:** Perhaps I'm doing something wrong.  
**Translation:** 

**[8680.36s] English:** If I am able to, I will try to do better.  
**Translation:** 

**[8683.86s] English:** In all this discussion of academic work,  
**Translation:** 

**[8686.26s] English:** I hope you know that I don't ever.  
**Translation:** 

**[8688.58s] English:** Mean to say that I'm an expert at anything.  
**Translation:** 

**[8692.20s] English:** In the podcast, and in my private life,  
**Translation:** 

**[8695.20s] English:** I don't claim to be smart.  
**Translation:** 

**[8697.10s] English:** In fact, I often call myself an idiot—and mean it.  
**Translation:** 

**[8702.24s] English:** I try to make fun of myself as much as possible.  
**Translation:** 

**[8704.76s] English:** And, in general, to celebrate others instead.  
**Translation:** 

**[8709.10s] English:** Now, to talk about Drexel University, which I also love.  
**Translation:** 

**[8713.18s] English:** And I am proud of and am deeply grateful for my time there.  
**Translation:** Vocabulary: drexel: 德雷塞尔大学

**[8718.04s] English:** As I said, I went to Drexel for my bachelor's and master's.  
**Translation:** 

**[8720.98s] English:** And doctoral degrees in computer science.  
**Translation:** 

**[8723.56s] English:** And electrical engineering.  
**Translation:** 

**[8726.26s] English:** I've talked about Drexel.  
**Translation:** 

**[8726.84s] English:** Drexel many times, including, as I mentioned at the end of a recent podcast, the Donald Trump.  
**Translation:** 

**[8733.50s] English:** Episode, funny enough, that was listened to by many millions of people, where I answered a  
**Translation:** 

**[8739.16s] English:** A question about graduate school, and I explained my own journey at Drexel and how grateful I am for it.  
**Translation:** 

**[8746.26s] English:** If it's at all interesting to you, please go listen to the end of that episode or  
**Translation:** 

**[8750.10s] English:** Watch the related clip. At Drexel, I met and worked with many brilliant researchers and mentors.  
**Translation:** 

**[8756.62s] English:** From whom I've learned a lot about engineering.  
**Translation:** Vocabulary: mentors: 导师

**[8760.00s] English:** Science, and life. There are many valuable things I gained from my time at Drexel.  
**Translation:** 

**[8765.06s] English:** First, I took a large number of very difficult math and theoretical computer science courses.  
**Translation:** 

**[8770.42s] English:** They taught me how to think deeply and rigorously, and also how to work hard and not give up.  
**Translation:** 

**[8776.12s] English:** Even if it feels like I'm too dumb to find a solution to a technical problem.  
**Translation:** Vocabulary: rigorously: 严谨地

**[8781.48s] English:** Second, I programmed a lot during that time, mostly in C and C++. I programmed robots,  
**Translation:** 

**[8787.44s] English:** Optimization algorithms, computer vision systems, wireless network protocols,  
**Translation:** Vocabulary: optimization: 优化; wireless: 无线

**[8792.64s] English:** Multimodal machine learning systems, and all kinds of simulations of physical systems.  
**Translation:** 

**[8797.64s] English:** This is where I really developed a love for programming, including, yes, Emacs and the  
**Translation:** Vocabulary: emacs: 一种文本编辑器; multimodal: 多模态的; simulations: 模拟

**[8806.44s] English:** Kinesis keyboard. I also read a lot during that time. I played a lot of guitar and wrote a lot of  
**Translation:** 

**[8814.86s] English:** Poetry, and uh,...  
**Translation:** 

**[8817.44s] English:** Trained a lot in Judo and Jiu-Jitsu, which I cannot sing enough praises for. Jiu-Jitsu humbled me,  
**Translation:** 

**[8824.92s] English:** On a daily basis throughout my 20s, and it still does to this very day whenever I get a chance.  
**Translation:** Vocabulary: cannot: 不能; humbled: 使谦逊; praises: 赞美

**[8830.94s] English:** To train, anyway. I hope that the folks who occasionally get swept up in the online chanting will find this helpful.  
**Translation:** 

**[8837.60s] English:** Crowds that want to tear down others don't lose themselves in it too much. In the end, I still.  
**Translation:** Vocabulary: chanting: 诵念

**[8844.80s] English:** I think there's more good than bad.  
**Translation:** 

**[8847.44s] English:** In people.  
**Translation:** 

**[8848.92s] English:** But, we're all a mixed bag, each of us. I know I am very much flawed. I speak awkwardly. I sometimes  
**Translation:** 

**[8857.66s] English:** Say stupid shit. I can get irrationally emotional. I can be too much of a dick when I should be kind.  
**Translation:** Vocabulary: awkwardly: 不自然; flawed: 有缺陷; irrationally: 不合理地

**[8864.48s] English:** I can lose myself in a biased rabbit hole before I wake up to the bigger, more accurate picture of.  
**Translation:** 

**[8870.38s] English:** Reality: I'm human, and so are you. For better or for worse.  
**Translation:** Vocabulary: biased: 有偏见的

**[8877.44s] English:** And, I do still believe.  
**Translation:** 

**[8879.68s] English:** I'm human, and so are you. For better or for worse.  
**Translation:** 

**[8880.00s] English:** We're in this whole beautiful mess together.  
**Translation:** 

**[8883.78s] English:** I love you all.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
