# Podcast vocabulary notes
Source file: Lex Fridman - Demis Hassabis： Future of AI, Simulating Reality, Physics and Video Games ｜ Lex Fridman Podcast #475.opus

**[0.00s] English:** It's hard for us humans to make any kind of clean predictions about highly nonlinear dynamical systems.  
**Translation:** 

**[5.00s] English:** But again, to your point, we might be very surprised what classical learning systems might be able to do about even fluid.  
**Translation:** Vocabulary: dynamical: 动力学的

**[11.88s] English:** Yes, exactly. I mean, fluid dynamics, Navier-Stokes equations, these are traditionally thought of as very, very difficult, intractable problems to do on classical systems.  
**Translation:** 

**[20.18s] English:** They take enormous amounts of compute, you know, weather prediction systems, you know, these kind of things all involve fluid dynamics calculations.  
**Translation:** Vocabulary: equations: 方程式; intractable: 难以解决的

**[26.44s] English:** But again, if you look at something like VO, our video generation model, it can model liquids quite well, surprisingly well, and materials, specular lighting.  
**Translation:** 

**[37.52s] English:** I love the ones where, you know, there's people who generate videos where there's like clear liquids going through hydraulic presses and then it's being squeezed out.  
**Translation:** Vocabulary: hydraulic: 液压; specular: 镜面; squeezed: 挤压

**[45.32s] English:** I used to write physics engines and graphics engines in my early days in gaming, and I know it's just so painstakingly hard to build programs that can do that.  
**Translation:** 

**[54.42s] English:** And yet somehow these systems.  
**Translation:** Vocabulary: painstakingly: 费力地

**[56.44s] English:** Are, you know, reverse engineering from just watching YouTube videos.  
**Translation:** 

**[60.94s] English:** So presumably what's happening is it's extracting some underlying structure around how these materials behave.  
**Translation:** Vocabulary: extracting: 提取; presumably: 推测

**[68.66s] English:** So perhaps there is some kind of lower dimensional manifold that can be learned if we actually fully understood what's going on under the hood.  
**Translation:** 

**[76.68s] English:** That's maybe, you know, maybe true of most of reality.  
**Translation:** Vocabulary: manifold: 多维流形

**[82.10s] English:** The following is a conversation with Demis Hassabis.  
**Translation:** 

**[85.28s] English:** His second time on the podcast, he is the leader of Google DeepMind and is now a Nobel Prize winner.  
**Translation:** Vocabulary: hassabis: 哈萨斯; nobel: 诺贝尔

**[94.22s] English:** Demis is one of the most brilliant and fascinating minds in the world today, working on understanding and building intelligence and exploring the big mysteries of our universe.  
**Translation:** 

**[107.90s] English:** This was truly an honor and a pleasure for me.  
**Translation:** 

**[111.40s] English:** This is the Lex Friedman podcast to support it.  
**Translation:** 

**[114.60s] English:** Please check out our.  
**Translation:** 

**[115.28s] English:** Sponsors in the description and consider subscribing to this.  
**Translation:** 

**[120.00s] English:** And now, dear friends, here's Demis Hassabis.  
**Translation:** Vocabulary: sponsors: 赞助商; subscribing: 订阅

**[150.00s] English:** Yeah. Neuroscience. What are we talking about? Sure. Well, look, I felt that it's sort of a  
**Translation:** 

**[154.68s] English:** tradition, I think, of Nobel Prize lectures that you're supposed to be a little provocative. And  
**Translation:** Vocabulary: neuroscience: 神经科学; provocative: 激进的

**[158.78s] English:** I wanted to follow that tradition. What I was talking about there is if you take a step back  
**Translation:** 

**[162.70s] English:** and you look at all the work that we've done, especially with the Alpha X projects. So I'm  
**Translation:** Vocabulary: alpha: 阿尔法

**[167.28s] English:** thinking AlphaGo, of course, AlphaFold. What they really are is we're building models of very  
**Translation:** 

**[172.72s] English:** combinatorially high dimensional spaces that, you know, if you try to brute force a solution,  
**Translation:** Vocabulary: brute: 粗暴; combinatorially: 组合地

**[178.24s] English:** find the best move and go.  
**Translation:** 

**[180.00s] English:** Or find the exact shape of a protein. And if you enumerated all the possibilities,  
**Translation:** Vocabulary: enumerated: 列举出

**[185.26s] English:** there wouldn't be enough time in the, you know, the time of the universe. So you have to do  
**Translation:** 

**[189.44s] English:** something much smarter. And what we did in both cases was build models of those environments.  
**Translation:** 

**[195.20s] English:** And that guided the search in a smart way. And that makes it tractable. So if you think about  
**Translation:** 

**[201.26s] English:** protein folding, which is obviously a natural system, you know, why should that be possible?  
**Translation:** Vocabulary: tractable: 可处理的

**[205.18s] English:** How does physics do that? You know, proteins fold in milliseconds in our bodies.  
**Translation:** 

**[209.08s] English:** So somehow,  
**Translation:** Vocabulary: milliseconds: 毫秒

**[210.00s] English:** physics solves this problem that we've now also solved computationally. And I think the reason  
**Translation:** 

**[215.56s] English:** that's possible is that in nature, natural systems have structure because they were subject to  
**Translation:** Vocabulary: computationally: 通过计算

**[221.46s] English:** evolutionary processes that shape them. And if that's true, then you can maybe learn  
**Translation:** 

**[227.04s] English:** what that structure is.  
**Translation:** Vocabulary: evolutionary: 进化

**[229.68s] English:** So this perspective, I think, is really interesting one. You've hinted at it,  
**Translation:** 

**[234.08s] English:** which is almost like crudely stated, anything that can be evolved,  
**Translation:** 

**[240.00s] English:** can be efficiently modeled i think there's some truth to that yeah i sometimes call it survival  
**Translation:** 

**[244.54s] English:** of the stabilist or something like that because you know it's it's of course there's evolution  
**Translation:** Vocabulary: efficiently: 高效地; stabilist: 稳定者

**[249.10s] English:** for life uh living things but there's also you know if you think about geological time so the  
**Translation:** 

**[255.36s] English:** shape of mountains that's been shaped by weathering processes right over thousands of years but then  
**Translation:** Vocabulary: geological: 地质的

**[261.04s] English:** you can even take it cosmological the orbits of planets the shapes of asteroids these have all  
**Translation:** 

**[266.30s] English:** been survived kind of processes that have acted on them many many times so if that's true then  
**Translation:** Vocabulary: asteroids: 小行星; cosmological: 宇宙的

**[272.20s] English:** there should be some sort of pattern that you can kind of reverse learn and a kind of manifold  
**Translation:** 

**[278.34s] English:** really that helps you search to the right solution to the right shape and actually allow you to  
**Translation:** Vocabulary: manifold: 多面体

**[284.80s] English:** predict things about it in an efficient way because it's not a random pattern right so it may not be  
**Translation:** 

**[290.64s] English:** possible for man-made things or abstract things like factorizing large numbers because unless  
**Translation:** 

**[295.76s] English:** there's patterns  
**Translation:** 

**[296.28s] English:** in the number space which there might be but if there's not in its uniform then there's no pattern  
**Translation:** 

**[300.78s] English:** to learn there's no model to learn that will help you search you have to do brute force so in that  
**Translation:** 

**[305.54s] English:** case you you know you maybe need a quantum computer something like this but in most things  
**Translation:** Vocabulary: brute: 粗暴

**[309.48s] English:** in nature that we're interested in uh are not like that they have structure um that evolved for a  
**Translation:** 

**[315.42s] English:** reason and survived over time and if that's true i think that's potentially learnable by a neural  
**Translation:** Vocabulary: neural: 神经网络

**[320.48s] English:** network it's like nature is doing a search process and it's so fascinating that it's  
**Translation:** 

**[326.26s] English:** in that search process is creating systems that can be efficiently modeled yes right yeah so  
**Translation:** 

**[333.02s] English:** interesting so they can be efficiently rediscovered or recovered um because nature is not random right  
**Translation:** 

**[338.58s] English:** these everything that we see around us including like the elements that are more stable all of  
**Translation:** Vocabulary: rediscovered: 重新发现

**[343.02s] English:** those things they're subject to um some kind of selection process pressure do you think because  
**Translation:** 

**[348.64s] English:** you're also a fan of theoretical computer science and complexity do you think we can come up with a  
**Translation:** 

**[352.92s] English:** complexity class like a complexity zoo  
**Translation:** 

**[356.26s] English:** type of class where maybe it's the set of learning  
**Translation:** 

**[360.00s] English:** systems, the set of learnable natural systems, LNS. This is a new class of systems that could be  
**Translation:** 

**[370.18s] English:** actually learnable by classical systems in this kind of way, natural systems that can be  
**Translation:** 

**[375.20s] English:** modeled efficiently. Yeah. I mean, I've always been fascinated by the P equals MP question and  
**Translation:** 

**[381.16s] English:** what is modelable by classical systems, i.e. non-quantum systems, you know, Turing machines  
**Translation:** Vocabulary: efficiently: 高效地; fascinated: 着迷; modelable: 可建模的; turing: 图灵机

**[387.76s] English:** in effect. And that's exactly what I'm working on actually in kind of my few moments of spare  
**Translation:** 

**[392.58s] English:** time with a few colleagues about should there be, you know, maybe a new class of problem  
**Translation:** 

**[397.14s] English:** that is solvable by this type of neural network process and kind of mapped onto these natural  
**Translation:** 

**[403.40s] English:** systems. So, you know, the things that exist in physics and have structure. So I think that could  
**Translation:** Vocabulary: solvable: 可解决的

**[409.10s] English:** be a very interesting new way of thinking about it. And it sort of fits with the way I think about  
**Translation:** 

**[413.76s] English:** physics in general, which is that, you know, I think information is primary.  
**Translation:** 

**[417.76s] English:** Information is the most sort of fundamental unit of the universe, more fundamental than energy and  
**Translation:** 

**[421.68s] English:** matter. I think they can all be converted into each other. But I think of the universe as a  
**Translation:** 

**[425.92s] English:** kind of informational system. So when you think of the universe as an informational system,  
**Translation:** 

**[430.14s] English:** then the P equals MP question is a physics question. That's right. And it's a question  
**Translation:** 

**[436.34s] English:** that can help us actually solve the entirety of this whole thing going on. Yeah. I think it's one  
**Translation:** 

**[441.08s] English:** of the most fundamental questions, actually, if you think of physics as informational. And the  
**Translation:** Vocabulary: entirety: 全部

**[446.90s] English:** answer to that, I think, is that it's a fundamental question. And I think it's a fundamental question  
**Translation:** 

**[447.76s] English:** that can help us actually solve the entirety of this whole thing going on. Yeah. I think it's  
**Translation:** 

**[447.84s] English:** going to be, you know, very enlightening. More specific to the P and MP question.  
**Translation:** 

**[453.62s] English:** This, again, some of the stuff we're saying is kind of crazy right now.  
**Translation:** Vocabulary: enlightening: 启发性的

**[457.30s] English:** Just like the Christian Anfinson Nobel Prize speech controversial thing that he said  
**Translation:** 

**[461.90s] English:** sounded crazy. And then you went and got a Nobel Prize for this with John Jumper,  
**Translation:** Vocabulary: nobel: 诺贝尔奖

**[466.20s] English:** solved the problem. So let me just stick to the P equals MP. Do you think there's something  
**Translation:** 

**[470.84s] English:** in this thing we're talking about that could be shown if you can do  
**Translation:** 

**[477.76s] English:** something like polynomial  
**Translation:** 

**[480.00s] English:** time or constant time compute ahead of time and construct this gigantic model then you can solve  
**Translation:** Vocabulary: gigantic: 巨大; polynomial: 多项式

**[487.64s] English:** some of these extremely difficult problems in a theoretical computer science kind of way yeah i  
**Translation:** 

**[492.58s] English:** think that there are actually a huge class of problems that could be couched in this way the  
**Translation:** 

**[497.44s] English:** way we did alpha go and the way we did alpha fold where you know you you model what the dynamics of  
**Translation:** 

**[502.88s] English:** the system is the the the properties of that system the environment that you're trying to  
**Translation:** Vocabulary: alpha: 阿尔法

**[507.80s] English:** understand and then that makes the search for the solution or the prediction of the next step  
**Translation:** 

**[514.16s] English:** efficient basically polynomial time so tractable by a classical system which a neural network is  
**Translation:** Vocabulary: neural: 神经网络; tractable: 可处理的

**[522.00s] English:** it runs on normal computers right classical computers turing machines in effect and i think  
**Translation:** 

**[528.92s] English:** it's one of the most interesting questions there is is how far can that paradigm go you know i  
**Translation:** Vocabulary: paradigm: 范式; turing: 图灵

**[533.30s] English:** think we've proven and the ai community in general that classical systems  
**Translation:** 

**[537.78s] English:** turing machines can go a lot further than we previously thought you know they can do things  
**Translation:** 

**[542.16s] English:** like model the structures of proteins and play go to better than world champion level and uh you  
**Translation:** 

**[548.84s] English:** know a lot of people would have thought maybe 10 20 years ago that was decades away or maybe you  
**Translation:** 

**[553.80s] English:** would need some sort of quantum machines to to quantum systems to be able to do things like  
**Translation:** 

**[558.64s] English:** protein folding and so i think we haven't really uh even sort of scratched the surface yet of what  
**Translation:** 

**[565.06s] English:** uh classical systems so-called uh  
**Translation:** 

**[567.78s] English:** could do and of course agi being built on a on a neural network system on top of a neural network  
**Translation:** 

**[573.76s] English:** system on top of a classical computer would be the ultimate expression of that and i think the limit  
**Translation:** 

**[579.32s] English:** that you know the the what what the bounds of that kind of system what it can do it's very  
**Translation:** 

**[583.78s] English:** interesting question and and and directly speaks to the p equals mp question what do you think  
**Translation:** 

**[588.72s] English:** again hypothetical might be outside of this maybe emergent phenomena like if you look at cellular  
**Translation:** Vocabulary: cellular: 细胞的; emergent: 涌现的; hypothetical: 假设的

**[596.10s] English:** automata some of the you have the  
**Translation:** 

**[597.78s] English:** extremely simple systems and then some complexity  
**Translation:** Vocabulary: automata: 自动机; complexity: 复杂性

**[600.00s] English:** emerges yes maybe that would be outside or even would you guess even that might be amenable to  
**Translation:** 

**[607.22s] English:** efficient modeling by a classical yeah i think those systems would be right on the boundary  
**Translation:** Vocabulary: amenable: 可接受的

**[612.28s] English:** right so um i think most emergent systems cellular automata things like that could be modelable by a  
**Translation:** 

**[618.58s] English:** classical system you just sort of do a forward simulation of it and it'd probably be efficient  
**Translation:** Vocabulary: modelable: 可建模; simulation: 模拟

**[622.16s] English:** enough um of course there's the question of things like chaotic systems where the initial conditions  
**Translation:** 

**[627.68s] English:** really matter and then you get to some you know uncorrelated end state now those could be difficult  
**Translation:** Vocabulary: uncorrelated: 不相关的

**[633.70s] English:** to model so i think these are kind of the open questions but i think when you step back and  
**Translation:** 

**[638.60s] English:** look at what we've done with the systems and the problems that we've solved and then you look at  
**Translation:** 

**[643.96s] English:** things like vo3 on like video generation sort of rendering physics and lighting and things like  
**Translation:** 

**[651.18s] English:** that you know really in core fundamental things in physics um it's pretty interesting i think it's  
**Translation:** 

**[656.44s] English:** telling us something quite fundamental  
**Translation:** 

**[657.68s] English:** about how the universe is structured in my opinion um so you know in a way that's what i want to build  
**Translation:** 

**[662.90s] English:** agi for is to help uh us uh as scientists answer these questions uh like p equals mp yeah i think  
**Translation:** 

**[670.10s] English:** we might be continuously surprised about what is modelable by classical computers i mean alpha  
**Translation:** Vocabulary: alpha: 阿尔法

**[675.78s] English:** fold three on the interaction side is surprising that you can make any kind of progress on that  
**Translation:** 

**[682.22s] English:** direction alpha genome is surprising that you can map the genetic code to the  
**Translation:** Vocabulary: genome: 基因组

**[687.66s] English:** function kind of playing with the emergent kind of phenomena you think there's so many combinatorial  
**Translation:** 

**[692.44s] English:** options that and then here you go you can find the kernel that is efficiently modeled yes because  
**Translation:** Vocabulary: combinatorial: 组合的; efficiently: 高效地; kernel: 内核

**[697.40s] English:** there's some structure there's some landscape you know in the energy landscape or whatever it is that  
**Translation:** 

**[702.56s] English:** you can follow some gradient you can follow and of course what neural networks are very good at  
**Translation:** Vocabulary: gradient: 梯度; neural: 神经

**[706.32s] English:** is following gradients and so if there's one to follow an object and you can specify the objective  
**Translation:** 

**[711.32s] English:** function correctly you know you don't have to deal with all that complexity which i think is how we  
**Translation:** Vocabulary: gradients: 梯度

**[717.50s] English:** make it work and i think that's a really good question and i think that's a really good question  
**Translation:** 

**[717.66s] English:** maybe you've naively thought about it for decades  
**Translation:** Vocabulary: naively: 天真地

**[720.00s] English:** those problems if you just enumerate all the possibilities it looks totally intractable  
**Translation:** 

**[724.22s] English:** and there's many many problems like that and then you think well it's like 10 to 300  
**Translation:** Vocabulary: enumerate: 列举; intractable: 无法解决

**[727.94s] English:** possible protein structures uh 10 to the hundred and you know 70 possible go positions all of these  
**Translation:** 

**[735.22s] English:** are way more than atoms in the universe so how could one possibly find the the right solution  
**Translation:** 

**[740.14s] English:** or predict the next step and and it but it turns out that it is possible and of course reality in  
**Translation:** 

**[745.74s] English:** nature does do it right proteins do fold so that that gives you confidence that there must be if we  
**Translation:** 

**[751.02s] English:** understood how physics was doing that uh in a sense uh then and we could mimic that process  
**Translation:** 

**[757.18s] English:** i model that process uh it should be possible on our classical systems is is is basically what the  
**Translation:** 

**[763.56s] English:** conjecture is about and of course there's non-linear dynamical systems highly non-linear  
**Translation:** 

**[768.16s] English:** dynamical systems everything involving fluid yes right you know the recent conversation with  
**Translation:** Vocabulary: conjecture: 猜测; dynamical: 动力学

**[773.58s] English:** terence tau who mathematically  
**Translation:** 

**[774.88s] English:** uh it contends with a very difficult aspect of systems that have some singularities in them  
**Translation:** Vocabulary: contends: 主张; mathematically: 从数学上

**[781.52s] English:** that break the mathematics and it's just hard for us humans to make any kind of clean predictions  
**Translation:** 

**[786.88s] English:** about highly non-linear dynamical systems but again to your point we might be very surprised  
**Translation:** 

**[792.84s] English:** what classical learning systems might be able to do about even fluid yes exactly i mean fluid  
**Translation:** 

**[798.14s] English:** dynamics navier-stokes equations these are traditionally thought it was very very difficult  
**Translation:** Vocabulary: equations: 方程组

**[802.10s] English:** intractable kind of problems to do on classical systems but i think it's a very difficult problem  
**Translation:** 

**[804.88s] English:** to do on classical systems they take enormous amounts of compute you know weather prediction  
**Translation:** 

**[808.34s] English:** systems you know these kind of things all involve fluid dynamics calculations and um but again if you  
**Translation:** 

**[815.10s] English:** look at something like vo our video generation model it can model liquids quite well surprisingly  
**Translation:** 

**[820.80s] English:** well and materials specular lighting i love the ones where you know there's there's people who  
**Translation:** 

**[826.88s] English:** generate videos where there's like clear liquids going through hydraulic presses and then it's  
**Translation:** Vocabulary: hydraulic: 液压; specular: 镜面

**[830.94s] English:** being squeezed out i used to write uh physics engines and graphics systems and i used to write  
**Translation:** 

**[834.88s] English:** graphics engines and in my early days in gaming and i know it's just so painstakingly hard to build  
**Translation:** Vocabulary: painstakingly: 极其费力; squeezed: 被挤出

**[840.00s] English:** programs that can do that and yet somehow these systems are you know reverse engineering from  
**Translation:** 

**[845.62s] English:** just watching youtube videos so presumably what's happening is it's extracting some underlying  
**Translation:** Vocabulary: extracting: 提取; presumably: 推测

**[851.58s] English:** structure around how these materials behave so perhaps there is some kind of lower dimensional  
**Translation:** 

**[858.14s] English:** manifold that can be learned if we actually fully understood what's going on under the hood that's  
**Translation:** Vocabulary: manifold: 低维流形

**[863.88s] English:** maybe you know maybe true of most of reality yeah i've been continuously precisely by this  
**Translation:** 

**[869.88s] English:** aspect of vo3 i think a lot of people highlight different aspects including the comedic and the  
**Translation:** 

**[875.06s] English:** media and all that kind of stuff and then the ultra realistic ability to capture humans in a  
**Translation:** 

**[880.60s] English:** really nice way that's compelling and it feels close to reality and then combine that with native  
**Translation:** Vocabulary: compelling: 引人入胜; ultra: 超现实

**[886.02s] English:** audio all of those are marvelous things about vo3 but the exactly the thing you're mentioning  
**Translation:** 

**[890.94s] English:** which is the physics yeah it's not perfect but it's pretty damn good and then the really  
**Translation:** 

**[897.28s] English:** interesting scientific question is what is it  
**Translation:** 

**[899.80s] English:** you're talking about  
**Translation:** 

**[899.88s] English:** understanding about our world in order to be able to do that because of the cynical  
**Translation:** 

**[905.52s] English:** take with diffusion models there's no way it understands anything but it seemed i mean i  
**Translation:** Vocabulary: cynical: 悲观看法; diffusion: 扩散模型

**[911.92s] English:** don't think you can generate that kind of video without understanding and then our own philosophical  
**Translation:** 

**[917.16s] English:** notion what it means to understand then is like brought to the surface like do to what degree do  
**Translation:** Vocabulary: philosophical: 哲学的

**[922.66s] English:** you think vo3 understands our world i think to the extent that it can predict the next frames  
**Translation:** 

**[928.24s] English:** you know in a coherent way  
**Translation:** Vocabulary: coherent: 连贯的

**[929.80s] English:** that some that is a form you know of understanding right not in the anthropomorphic version of you  
**Translation:** 

**[935.58s] English:** know it's not some kind of deep philosophical understanding of what's going on i don't think  
**Translation:** Vocabulary: anthropomorphic: 拟人化的

**[939.70s] English:** these systems have that but they they certainly have uh modeled enough of the dynamics you know  
**Translation:** 

**[945.50s] English:** put it that way that they can pretty accurately generate whatever it is eight seconds of  
**Translation:** 

**[950.96s] English:** consistent video that by eye at least you know at a glance is quite hard to distinguish what  
**Translation:** 

**[956.12s] English:** the issues are and imagine that in two or three more years time that's the thing i'm talking about  
**Translation:** 

**[959.80s] English:** i'm thinking  
**Translation:** 

**[960.00s] English:** And how incredible that they will look, given where we've come from, you know, the early versions of that one or two years ago. And so the rate of progress is incredible. And I think I'm like you is like a lot of people love all of the the stand up comedians and that actually captures a lot of human dynamics very well and and body language.  
**Translation:** 

**[982.20s] English:** But actually, the thing I'm most impressed with and fascinated by is the physics behavior, the lighting and materials and liquids. And it's pretty amazing that it can do that. And I think that shows that it has some notion of at least intuitive physics, right, how things are supposed to work intuitively, maybe the way that a human child would understand physics, right, as opposed to, you know, a PhD student really being able to unpack all the equations.  
**Translation:** 

**[1011.40s] English:** It's more of an intuitive physics understanding.  
**Translation:** Vocabulary: equations: 方程式; fascinated: 着迷; intuitive: 直觉; intuitively: 直观地

**[1013.32s] English:** Well, that intuitive physics understanding, that's the base layer. That's the thing people sometimes call a common sense. Again, it really understands something. I think that really surprised a lot of people. It blows my mind that I just didn't think it would be possible to generate that level of realism without understanding.  
**Translation:** 

**[1032.14s] English:** There's this notion that you can only understand the physical world by having an embodied AI system, a robot that interacts with that world.  
**Translation:** Vocabulary: embodied: 具身化; interacts: 交互

**[1040.46s] English:** That's the only way to construct an understanding of that world.  
**Translation:** 

**[1043.14s] English:** Yeah.  
**Translation:** 

**[1043.60s] English:** But VO3 is directly challenging that, it feels like.  
**Translation:** 

**[1047.88s] English:** Right. Yes. And it's very interesting, you know, even if you were to ask me five, ten years ago, I would have said, even though I was immersed in all of this, I would have said, well, yeah, you probably need to understand intuitive physics.  
**Translation:** Vocabulary: immersed: 沉浸其中

**[1058.12s] English:** You know, like if I push this off the table, this glass, it will maybe shatter, you know, and the liquid will spill out. Right. So we know all of these things.  
**Translation:** 

**[1067.14s] English:** But I thought that, you know, there's a lot of theories in neuroscience.  
**Translation:** Vocabulary: neuroscience: 神经系统科学

**[1070.02s] English:** It's called action in perception where, you know, you need to act in the world to really, truly perceive it in a deep way.  
**Translation:** 

**[1076.34s] English:** And there was a lot of theories about you need embodied intelligence or robots.  
**Translation:** Vocabulary: perceive: 感知

**[1080.00s] English:** or something or maybe at least simulated action so that you would understand things like intuitive  
**Translation:** 

**[1085.82s] English:** physics but it seems like you can understand it through passive observation which is pretty  
**Translation:** Vocabulary: simulated: 模拟的

**[1091.18s] English:** surprising to me and again I think hints at something underlying about the nature of reality  
**Translation:** 

**[1097.26s] English:** in my opinion beyond just the you know the cool videos that it generates and of course  
**Translation:** 

**[1103.72s] English:** there's next stages is maybe even making those videos interactive so one can actually step into  
**Translation:** 

**[1109.54s] English:** them and move around them which would be really mind-blowing especially given my games background  
**Translation:** Vocabulary: interactive: 互动的

**[1114.78s] English:** so you can imagine and then and then I think you know you're we're starting to get towards what I  
**Translation:** 

**[1119.48s] English:** would call a world model a model of how the world works the mechanics of the world the physics of  
**Translation:** 

**[1124.76s] English:** the world and the things in that world and of course that's what you would need for a true  
**Translation:** 

**[1129.02s] English:** AGI system. I have to talk to you about video games so you you were being a bit trolly I think  
**Translation:** Vocabulary: trolly: 爱搞恶作剧的

**[1135.10s] English:** you're having more and more fun on twitter on x which is great to see  
**Translation:** 

**[1138.82s] English:** so  
**Translation:** 

**[1139.54s] English:** guy named Jimmy Apples tweeted let me play a video game of my video three videos already  
**Translation:** 

**[1144.36s] English:** Google cooked so good playable world models when spelled w e n question mark and then you  
**Translation:** Vocabulary: jimmy: 吉米

**[1151.90s] English:** quote tweeted that with now wouldn't that be something so how hard is it to build game worlds  
**Translation:** 

**[1158.30s] English:** with AI maybe can you look out into the future of video games five ten years out what do you  
**Translation:** 

**[1165.72s] English:** think that looks like well games were my first love really and  
**Translation:** 

**[1169.54s] English:** I think the next time I thought I wanted to have a computer uh putting it so I didn't  
**Translation:** 

**[1172.54s] English:** even know how but I came to created games with a computer Which was for  
**Translation:** 

**[1172.80s] English:** the first of kind AI for games was the first thing I did professionally and in  
**Translation:** 

**[1176.26s] English:** my teenage years and and was the first major AI systems that I built and I  
**Translation:** 

**[1181.10s] English:** always want to I have I want to scratch that each one day and come back to that  
**Translation:** 

**[1183.56s] English:** so you know and I will do I think and  
**Translation:** 

**[1185.90s] English:** I think I'd sort of dream about you know what would I have done back in the 90s  
**Translation:** 

**[1193.08s] English:** if I'd have access to the kind of AI systems we have today and I think you  
**Translation:** 

**[1196.40s] English:** could build absolutely mind-blowing games and I think the next stages I  
**Translation:** 

**[1199.38s] English:** I'll open  
**Translation:** 

**[1200.00s] English:** world games so they're games where there's a simulation and then there's ai characters and  
**Translation:** Vocabulary: simulation: 模拟

**[1205.56s] English:** then the player uh interacts with that simulation and the simulation adapts to the way the player  
**Translation:** 

**[1210.60s] English:** plays and i always thought they were the coolest games because uh so games like theme park that i  
**Translation:** Vocabulary: interacts: 互动

**[1215.46s] English:** worked on where everybody's game experience would be unique to them right because you're kind of  
**Translation:** 

**[1220.20s] English:** co-creating the game right uh we set up the parameters we set up initial conditions and  
**Translation:** 

**[1225.28s] English:** then you as the player immersed in it and then you are co-creating it with the with the simulation  
**Translation:** 

**[1230.38s] English:** but of course it's very hard to program open world games you know you've got to be able to create  
**Translation:** Vocabulary: immersed: 身临其境

**[1235.08s] English:** uh content whichever direction the player goes in and you want it to be compelling no matter what  
**Translation:** 

**[1239.60s] English:** the player chooses um and so it was always quite difficult to build uh things like cellular  
**Translation:** Vocabulary: cellular: 蜂窝状; compelling: 引人入胜; whichever: 无论哪个

**[1245.40s] English:** automata actually type of those kind of classical systems which created some emergent behavior  
**Translation:** 

**[1249.60s] English:** but they're always a little bit fragile a little bit limited now we're maybe on the cusp in the  
**Translation:** Vocabulary: automata: 自动机; emergent: 涌现; fragile: 脆弱

**[1254.42s] English:** next few years five  
**Translation:** 

**[1255.20s] English:** ten years  
**Translation:** 

**[1255.26s] English:** ten years of having ai systems that can truly create around your imagination um can now sort  
**Translation:** 

**[1261.50s] English:** of dynamically change the story and storytell the narrative around uh and make it dramatic no matter  
**Translation:** Vocabulary: dynamically: 灵活地; storytell: 讲述故事

**[1267.14s] English:** what you end up choosing so it's like the ultimate choose your own adventure sort of game and uh you  
**Translation:** 

**[1273.86s] English:** know i think maybe we're within reach if you think of a kind of interactive version of vo uh and then  
**Translation:** Vocabulary: interactive: 交互式

**[1279.00s] English:** wind that forward five to ten years and you know imagine how good it's going to be  
**Translation:** 

**[1283.98s] English:** yeah so you said a lot of  
**Translation:** 

**[1285.18s] English:** stuff there so one the open world built into that is a deep personalization the way you've described  
**Translation:** 

**[1292.82s] English:** it so it's not just that it's open world like you can open any door and there'll be something there  
**Translation:** 

**[1297.96s] English:** it's that the choice of which door you open in an unconstrained way defines the worlds you see  
**Translation:** 

**[1304.98s] English:** so some games try to do that they give you choice yes but it's really just an illusion of choice  
**Translation:** Vocabulary: unconstrained: 自由

**[1310.94s] English:** because the only uh like like stanley parable is  
**Translation:** 

**[1315.10s] English:** it's it's it's really there's a couple of doors and it really just  
**Translation:** 

**[1320.00s] English:** takes you down the narrative stanley parable is a great video game i recommend people play  
**Translation:** 

**[1323.72s] English:** that kind of uh in a meta way uh mocks the illusion of choice and there's philosophical  
**Translation:** Vocabulary: philosophical: 哲学的

**[1330.72s] English:** notions of free will and so on but uh i do like one of my favorite games felder scrolls dagger  
**Translation:** 

**[1337.08s] English:** fall i believe that they really played with a like random generation of the dungeons yeah of  
**Translation:** Vocabulary: dagger: 短剑; dungeons: 地牢; scrolls: 卷轴

**[1345.36s] English:** if you can step in and they give you this feeling of an open world and there you mentioned  
**Translation:** 

**[1350.58s] English:** interactivity you don't need to interact that's a first step because you don't need to interact  
**Translation:** 

**[1355.18s] English:** that much you just when you open the door whatever you see is randomly generated for you  
**Translation:** 

**[1360.86s] English:** and that's already an incredible experience because you might be the only person to ever  
**Translation:** 

**[1365.46s] English:** see that yeah exactly and and so but what you'd like is a little bit better than just sort of a  
**Translation:** 

**[1371.10s] English:** random generation right so you'd like uh and and also better than a  
**Translation:** 

**[1375.16s] English:** simple  
**Translation:** 

**[1375.36s] English:** choice right that's not really uh open world right as you say it's just giving you the illusion  
**Translation:** 

**[1382.68s] English:** of choice what you want to be able to do is potentially anything in that game environment  
**Translation:** 

**[1386.50s] English:** um and i think the only way you can do that is to have uh generated systems systems that  
**Translation:** 

**[1393.54s] English:** uh will generate that on the fly of course you can't create infinite amounts of game assets  
**Translation:** 

**[1398.14s] English:** right it's expensive enough already how triple a games are made today and that was obvious to  
**Translation:** Vocabulary: triple: 三倍

**[1402.88s] English:** to us back in the 90s when i was working on all these games and i was working on all these games  
**Translation:** 

**[1405.36s] English:** i think maybe black and white uh was the game that i worked on early stages of that that had the  
**Translation:** 

**[1411.28s] English:** still probably the best ai learning ai in it it was an early reinforcement learning system  
**Translation:** 

**[1415.60s] English:** that you you know you were you were looking after this mythical creature and growing it  
**Translation:** Vocabulary: mythical: 神话般的; reinforcement: 强化学习

**[1420.14s] English:** and nurturing it and depending how you treated it it would treat the villagers in that world in the  
**Translation:** 

**[1425.18s] English:** same way so if you were mean to it it would be mean if you were good it would be protective  
**Translation:** Vocabulary: nurturing: 抚养; villagers: 村民

**[1428.62s] English:** and so it was really a reflection of the way you played it so actually all of the uh i've been  
**Translation:** 

**[1434.30s] English:** working on sort of simulation games and i've been working on sort of simulation games and i've been  
**Translation:** Vocabulary: simulation: 模拟游戏

**[1435.36s] English:** working on sort of simulations and ai through the medium of games at the beginning of my career and  
**Translation:** 

**[1440.00s] English:** And really, the whole of what I do today is still a follow on from those early, more hard coded ways of doing the AI to now, you know, fully general learning systems that are trying to achieve the same thing.  
**Translation:** 

**[1451.82s] English:** Yeah, it's been interesting, hilarious and fun to watch you and Elon obviously itching to create games because you're both gamers.  
**Translation:** 

**[1460.36s] English:** And one of the sad aspects of your incredible success in so many domains of science, like serious adult stuff, that you might not have time to really create a game.  
**Translation:** 

**[1472.28s] English:** You might end up creating the tooling that others would create the game.  
**Translation:** 

**[1476.24s] English:** You have to watch others create the thing you've always dreamed of.  
**Translation:** 

**[1482.12s] English:** Do you think it's possible you can somehow in your extremely busy schedule actually find time to create something like black and white?  
**Translation:** 

**[1488.94s] English:** Some, some.  
**Translation:** 

**[1490.20s] English:** Yeah.  
**Translation:** 

**[1490.30s] English:** Yeah.  
**Translation:** 

**[1490.34s] English:** Yeah.  
**Translation:** 

**[1490.36s] English:** It's like an actual video game where like you could make the childhood dream come become reality.  
**Translation:** 

**[1497.66s] English:** Well, you know, there's two things I think about that is maybe with vibe coding as it gets better, there's a possibility that I could, you know, one could do that actually in your spare time.  
**Translation:** 

**[1506.22s] English:** So I'm quite excited about that as that would be my project if I got the time to do some vibe coding.  
**Translation:** 

**[1512.14s] English:** I'm actually itching to do that.  
**Translation:** 

**[1513.72s] English:** And then the other thing is, you know, maybe it's a sabbatical after AGI has been safely stewarded into the world and delivered into the world.  
**Translation:** Vocabulary: sabbatical: 休假; stewarded: 管理

**[1520.34s] English:** You know, that and then working on my physics theory, as we talked about at the beginning, those would be the two, my, my two post AGI projects.  
**Translation:** 

**[1528.12s] English:** Let's call it that way.  
**Translation:** 

**[1528.88s] English:** I would love to see what the ultimate game post AGI, which you choose solving the problem that some of the smartest people in human history contended with.  
**Translation:** 

**[1538.64s] English:** So P equals MP or creating a cool video.  
**Translation:** Vocabulary: contended: 争论

**[1542.92s] English:** Yeah.  
**Translation:** 

**[1543.56s] English:** But in my world, they'd be related because it would be an open world simulated game as realistic.  
**Translation:** Vocabulary: simulated: 模拟的

**[1550.12s] English:** Realistic as possible.  
**Translation:** 

**[1551.36s] English:** So, you know, what, what is, what is the universe?  
**Translation:** 

**[1553.98s] English:** That's, that's, that's speaking to the same question, right?  
**Translation:** 

**[1556.14s] English:** And P equals MP.  
**Translation:** 

**[1557.02s] English:** I think all these things are related, at least in my mind.  
**Translation:** 

**[1559.04s] English:** I mean, you know.  
**Translation:** 

**[1560.00s] English:** really serious way it's like video games sometimes are looked down upon there's just this fun side  
**Translation:** 

**[1565.98s] English:** activity but especially as ai does more and more of the difficult boring tasks something we in a  
**Translation:** 

**[1575.06s] English:** modern world called work you know video games is the thing in which we may find meaning in which  
**Translation:** 

**[1582.00s] English:** we may find like what to do with our time you could create incredibly rich meaningful experiences  
**Translation:** 

**[1589.38s] English:** like that's what human life is and then in video games you can create more sophisticated more  
**Translation:** 

**[1596.54s] English:** diverse ways of living yeah i think so i mean those of us who love games and i still do is is is  
**Translation:** Vocabulary: sophisticated: 复杂多样的

**[1605.68s] English:** um you know it's almost can let your imagination run wild right like i i used to love games um  
**Translation:** 

**[1613.20s] English:** and working on games so much because it's the fusion especially in the 90s and to early 2000s  
**Translation:** 

**[1618.40s] English:** sort of golden era  
**Translation:** 

**[1619.36s] English:** and maybe the 80s of of of game of the games industry and it was all being discovered new  
**Translation:** 

**[1624.30s] English:** genres were being discovered we weren't just making games we felt we were we were creating  
**Translation:** 

**[1627.92s] English:** a new entertainment medium that never existed before especially with these open world games  
**Translation:** 

**[1632.40s] English:** and simulation games where you were co-create you as the player were co-creating the story  
**Translation:** 

**[1636.22s] English:** there's no other media uh entertainment media where you do that where you as the audience  
**Translation:** 

**[1641.20s] English:** actually co-create the the story and of course now with multiplayer games as well it can be a  
**Translation:** 

**[1646.22s] English:** very social activity and  
**Translation:** 

**[1649.36s] English:** it's very important to um also enjoy and experience uh the physical world but the question is then  
**Translation:** 

**[1660.22s] English:** you know i think we're going to have to kind of confront the question again of what is the  
**Translation:** Vocabulary: confront: 面对

**[1663.48s] English:** fundamental nature of reality uh what is going to be the difference between these increasingly  
**Translation:** 

**[1667.76s] English:** realistic simulations and uh multiplayer ones and emergent um and what we do in the real world  
**Translation:** Vocabulary: emergent: 自发产生

**[1675.20s] English:** yeah there's clearly a huge amount of value to experiencing really interesting games and  
**Translation:** 

**[1679.18s] English:** experiencing the real world.  
**Translation:** 

**[1680.00s] English:** nature there's also a huge amount of value in experiencing other humans directly in person  
**Translation:** 

**[1685.76s] English:** the way we're sitting here today but we need to really scientifically rigorously answer the  
**Translation:** Vocabulary: rigorously: 严格地; scientifically: 科学地

**[1691.52s] English:** question why yeah and which aspect of that can be mapped into the virtual world exactly and it's not  
**Translation:** 

**[1698.44s] English:** it's not enough to say yeah you should go touch grass and hang out in nature it's like why exactly  
**Translation:** 

**[1704.02s] English:** is that valuable yes and i guess that's maybe the thing that's been uh haunting me or obsessing me  
**Translation:** 

**[1709.62s] English:** from the beginning of my career if you think about all the different things i've done that's  
**Translation:** Vocabulary: haunting: 困扰; obsessing: 痴迷

**[1712.90s] English:** they're all related in that way the simulation nature of reality and what is the bounds of you  
**Translation:** 

**[1718.72s] English:** know what can be modeled sorry for the ridiculous question but so far what is the greatest video  
**Translation:** Vocabulary: simulation: 模拟

**[1723.40s] English:** game of all time what's up there well my favorite one of all time is civilization i have to say  
**Translation:** 

**[1728.68s] English:** that that was the the civilization one and civilization two my favorite games of all time  
**Translation:** 

**[1734.10s] English:** um i can only assume you've avoided the most recent one because it would probably  
**Translation:** 

**[1739.62s] English:** you would that would be your sabbatical that you would disappear yes exactly they take a lot of  
**Translation:** 

**[1744.86s] English:** time these civilization games so uh i've got to be careful with them one question you and elon seem to  
**Translation:** 

**[1749.96s] English:** be somehow solid gamers uh is there a connection between being great at gaming and and uh being  
**Translation:** 

**[1757.70s] English:** great leaders of ai companies i don't know it's an interesting one i mean uh we both love games  
**Translation:** 

**[1763.68s] English:** and uh it's interesting he wrote games as well to start off with it's probably especially in the era  
**Translation:** 

**[1769.42s] English:** i grew up in i grew up in i grew up in i grew up in i grew up in i grew up in i grew up in  
**Translation:** 

**[1769.62s] English:** i grew up in where home computers were just became a thing you know in the late 80s and 90s  
**Translation:** 

**[1774.28s] English:** especially in the uk i had a spectrum and then a commodore amiga 500 which is my favorite computer  
**Translation:** 

**[1779.36s] English:** ever and that's why i learned all my programming and of course it's a very fun thing uh to program  
**Translation:** Vocabulary: amiga: 阿美佳

**[1784.96s] English:** is to program games so i think it's a great way to learn programming probably still is and um and  
**Translation:** 

**[1792.34s] English:** then of course i immediately took it in directions of ai and simulations which so i was able to  
**Translation:** 

**[1797.08s] English:** express my interest in in games and i think it's a great way to learn programming and i think it's  
**Translation:** 

**[1799.62s] English:** a great way to learn programming and experience playing games  
**Translation:** 

**[1800.00s] English:** and my sort of wider scientific interests all together and then the final thing i think that's  
**Translation:** 

**[1805.22s] English:** great about games is it fuses um artistic design you know art with the the most cutting edge  
**Translation:** Vocabulary: fuses: 融合

**[1813.16s] English:** programming um so again in the 90s all of the most interesting uh technical advances were  
**Translation:** 

**[1819.18s] English:** happening in gaming whether that was ai graphics physics engines uh hardware even gpus of course  
**Translation:** 

**[1825.36s] English:** were designed for gaming originally um so everything that was pushing computing forward  
**Translation:** 

**[1829.98s] English:** in the in the 90s was due to gaming so interestingly that was where the forefront  
**Translation:** Vocabulary: computing: 计算机; forefront: 前沿

**[1835.66s] English:** of research was going on and it was this incredible fusion with with art um you know graphics but also  
**Translation:** 

**[1842.56s] English:** music and just the whole new media of storytelling and i love that for me it's a sort of  
**Translation:** Vocabulary: storytelling: 叙事艺术

**[1847.66s] English:** multidisciplinary kind of effort is again something i've enjoyed my whole my whole life  
**Translation:** 

**[1852.20s] English:** i have to ask you i almost forgot about  
**Translation:** Vocabulary: multidisciplinary: 跨学科的

**[1855.36s] English:** one of the many and i would say one of the most incredible things recently uh that somehow didn't  
**Translation:** 

**[1861.42s] English:** yet get enough attention is alpha evolve we talked about evolution a little bit but it's the  
**Translation:** Vocabulary: alpha: 阿尔法

**[1866.24s] English:** google deep mind system that evolves algorithms yeah are these kinds of evolution-like techniques  
**Translation:** 

**[1871.92s] English:** promising as a component of future super intelligence systems so for people who don't  
**Translation:** 

**[1875.76s] English:** know it's kind of um i don't know if it's fair to say it's llm guided evolution search yeah so  
**Translation:** 

**[1883.82s] English:** evolution algorithms are the most incredible things that are promising in the future super  
**Translation:** 

**[1885.34s] English:** algorithms are doing the search and lms are telling you where yes exactly so lms are kind  
**Translation:** 

**[1890.38s] English:** of proposing some possible solutions and then you do you use evolutionary computing on top to to find  
**Translation:** Vocabulary: evolutionary: 进化

**[1896.98s] English:** some novel part of the of the search space so actually i think it's an example of very promising  
**Translation:** 

**[1903.04s] English:** directions where you combine llms or foundation models with other computational techniques  
**Translation:** Vocabulary: computational: 计算的

**[1909.74s] English:** evolutionary methods is one but you could also imagine monte carlo tree search basically many  
**Translation:** 

**[1915.34s] English:** search algorithms or reasoning algorithms sort of on top of or using  
**Translation:** 

**[1920.00s] English:** the foundation model as a basis so i actually think there's quite a lot of interesting  
**Translation:** 

**[1924.82s] English:** uh things to be discovered probably with these sort of hybrid systems let's call them  
**Translation:** 

**[1929.44s] English:** but not to romanticize evolution yeah i'm only human but you think there's some value in whatever  
**Translation:** 

**[1935.64s] English:** that mechanism is because we already talked about natural systems do you think where there's a lot  
**Translation:** 

**[1941.64s] English:** of low-hanging fruit of us understanding being being able to model uh being able to simulate  
**Translation:** 

**[1948.06s] English:** evolution and using that whatever we understand about that nature inspired mechanism to to then  
**Translation:** 

**[1955.30s] English:** do search better and better and better yes so if you think about uh again breaking down the  
**Translation:** 

**[1960.28s] English:** sort of systems we've built uh to their really fundamental core you've got like the model of the  
**Translation:** 

**[1965.86s] English:** of the underlying dynamics of the system uh and then if you want to discover something new  
**Translation:** 

**[1971.38s] English:** something novel that hasn't been seen before um then you need some kind of search process on top  
**Translation:** 

**[1977.20s] English:** to take  
**Translation:** 

**[1978.06s] English:** you to a novel region of the of the of the search space and um you can do that in a number of ways  
**Translation:** 

**[1984.30s] English:** evolutionary computing is one um with alpha go we just use monte carlo tree search right and that's  
**Translation:** 

**[1990.02s] English:** what found move 37 the new kind of never seen before strategy in go and so that's how you can  
**Translation:** Vocabulary: alpha: 阿尔法; carlo: 卡洛; computing: 计算; monte: 蒙特

**[1996.90s] English:** go beyond potentially what is already known so the model can model everything that you currently know  
**Translation:** 

**[2001.74s] English:** about right all the data that you currently have but then how do you go beyond that so that starts  
**Translation:** 

**[2006.22s] English:** to speak about the ideas of creativity  
**Translation:** 

**[2008.06s] English:** how can these systems create something new find discover something new obviously this is super  
**Translation:** 

**[2012.86s] English:** relevant for scientific discovery or pushing science and medicine forward which we want to  
**Translation:** 

**[2017.02s] English:** do with these systems and you can actually bolt on some fairly simple search systems  
**Translation:** 

**[2024.14s] English:** on top of these models and get you into a new region of space of course you also have to  
**Translation:** 

**[2030.06s] English:** make sure that you're not searching that space totally randomly it would be too big  
**Translation:** 

**[2034.14s] English:** so you have to have some objective function that you're trying to optimize and hill climb towards  
**Translation:** 

**[2038.06s] English:** and that guides that search  
**Translation:** Vocabulary: optimize: 优化

**[2040.00s] English:** But there's some mechanism of evolution that are interesting, maybe in the space of programs, but then the space of programs is an extremely important space because you can probably generalize to everything.  
**Translation:** 

**[2050.90s] English:** But, you know, for example, mutation, it's not just Monte Carlo tree search where it's like a search.  
**Translation:** Vocabulary: generalize: 泛化; mutation: 变异

**[2059.24s] English:** You could every once in a while combine things, like components of a thing.  
**Translation:** 

**[2066.20s] English:** Yes.  
**Translation:** 

**[2066.34s] English:** So then, you know, what evolution is really good at is not just the natural selection.  
**Translation:** 

**[2072.12s] English:** It's combining things and building increasingly complex hierarchical systems.  
**Translation:** Vocabulary: hierarchical: 等级制度的

**[2078.18s] English:** So that component is super interesting, especially like with alpha evolve in the space of programs.  
**Translation:** 

**[2083.02s] English:** Yeah, exactly.  
**Translation:** 

**[2083.88s] English:** So there's a you can get a bit of an extra property out of evolutionary systems, which is some new emergent capability may come about.  
**Translation:** 

**[2091.00s] English:** Yes.  
**Translation:** Vocabulary: capability: 能力; emergent: 涌现; evolutionary: 进化

**[2091.14s] English:** Of course, like happened with life.  
**Translation:** 

**[2093.80s] English:** Interestingly, with naive sort of traditionalism.  
**Translation:** Vocabulary: naive: 幼稚

**[2096.34s] English:** You know, evolution computing methods without LLMs and the modern AI, the problem with them, they were very well studied in the 90s and early 2000s and some promising results.  
**Translation:** 

**[2106.58s] English:** But the problem was they could never work out how to evolve new properties, new emergent properties.  
**Translation:** 

**[2111.90s] English:** You always had a sort of subset of the properties that you put into the system.  
**Translation:** 

**[2115.42s] English:** But maybe if we combine them with these foundation models, perhaps we can overcome that limitation.  
**Translation:** 

**[2121.08s] English:** Obviously, natural evolution clearly did because it did evolve new capabilities.  
**Translation:** 

**[2126.28s] English:** Right.  
**Translation:** 

**[2126.34s] English:** So bacteria to where we are now.  
**Translation:** 

**[2128.70s] English:** So clearly that it must be possible with evolutionary systems to generate new patterns, going back to the first thing we talked about and new capabilities and emergent properties.  
**Translation:** 

**[2141.28s] English:** And maybe we're on the cusp of discovering how to do that.  
**Translation:** 

**[2144.92s] English:** Yeah.  
**Translation:** 

**[2145.26s] English:** Listen, alpha evolve is one of the coolest things I've ever seen on my desk at home.  
**Translation:** 

**[2150.26s] English:** You know, most of my time is spent on that computer is just programming.  
**Translation:** Vocabulary: alpha: 测试版本

**[2154.38s] English:** And next to that.  
**Translation:** 

**[2156.26s] English:** The three screens is a skull of a tiktok, which.  
**Translation:** Vocabulary: skull: 头骨

**[2160.00s] English:** which is one of the early organisms that crawled out of the water onto land.  
**Translation:** 

**[2165.64s] English:** And I just kind of watch that little guy.  
**Translation:** 

**[2170.46s] English:** It's like whatever the computation mechanism of evolution is,  
**Translation:** 

**[2174.90s] English:** it's quite incredible.  
**Translation:** 

**[2176.60s] English:** It's truly, truly incredible.  
**Translation:** 

**[2178.46s] English:** Now, whether that's exactly the thing we need to do to do our search,  
**Translation:** 

**[2181.84s] English:** but never dismiss the power of nature, what it did here.  
**Translation:** 

**[2186.52s] English:** Yeah, and it's amazing.  
**Translation:** 

**[2187.74s] English:** Um, which is a relatively simple algorithm, right?  
**Translation:** 

**[2191.46s] English:** Effectively, and it can generate all of this immense complexity emerges,  
**Translation:** Vocabulary: algorithm: 算法; complexity: 复杂性; immense: 巨大

**[2195.54s] English:** obviously running over, you know, 4 billion years of time.  
**Translation:** 

**[2198.92s] English:** But, but it's, it's, it's, you know, you can think about that as, again, a process,  
**Translation:** 

**[2203.34s] English:** a search process that ran over the physics substrate of the universe for  
**Translation:** 

**[2207.16s] English:** a long amount of computational time.  
**Translation:** Vocabulary: computational: 计算的; substrate: 基底

**[2209.42s] English:** But then it generated all this incredible, rich diversity.  
**Translation:** 

**[2213.92s] English:** So, so many questions I want to ask you.  
**Translation:** 

**[2216.02s] English:** One, you do have a dream.  
**Translation:** 

**[2217.74s] English:** One of the natural systems you want to try to model is a, is a cell.  
**Translation:** 

**[2222.62s] English:** Yes.  
**Translation:** 

**[2223.24s] English:** That's a beautiful dream.  
**Translation:** 

**[2224.70s] English:** Uh, I could ask you about that.  
**Translation:** 

**[2227.08s] English:** I also just for that purpose on the AI scientist front, just broadly.  
**Translation:** 

**[2231.86s] English:** So there's a essay from Daniel Coccataglio, Scott Alexander, and others that  
**Translation:** 

**[2237.40s] English:** outline steps along the way to get to ASI and has a lot of interesting ideas in it.  
**Translation:** 

**[2242.82s] English:** One of which is, uh, including a superhuman coder and a  
**Translation:** 

**[2247.54s] English:** superhuman AI researcher.  
**Translation:** 

**[2250.36s] English:** And in that there's a term of research taste.  
**Translation:** 

**[2253.70s] English:** That's really interesting.  
**Translation:** 

**[2254.98s] English:** So in everything you've seen, do you think it's possible for AI systems  
**Translation:** 

**[2258.70s] English:** to have research taste to help you in the way that AI co-scientist does to  
**Translation:** 

**[2265.42s] English:** help steer human, um, human brilliant scientists, and then potentially by  
**Translation:** 

**[2272.92s] English:** itself to figure out what are the directions, uh, where you want to go?  
**Translation:** 

**[2277.42s] English:** How do you want to generate truly novel ideas?  
**Translation:** 

**[2280.00s] English:** to be like a really important component of how to do great science yeah i think that's going to be  
**Translation:** 

**[2285.00s] English:** one of the hardest things to to uh mimic or model is is this this idea of taste or judgment i think  
**Translation:** 

**[2292.04s] English:** that's what separates the you know the the great scientists from the good scientists like all  
**Translation:** 

**[2296.58s] English:** all professional scientists are good technically right otherwise it wouldn't have made it  
**Translation:** 

**[2300.14s] English:** that far in academia and things like that but then do you have the taste to sort of sniff out what  
**Translation:** Vocabulary: academia: 学术界

**[2306.10s] English:** the right direction is what the right experiment is what the right question is so the question is  
**Translation:** 

**[2311.02s] English:** picking the right question is is the hardest part of science um and and making the right hypothesis  
**Translation:** Vocabulary: hypothesis: 假设

**[2316.24s] English:** and um that's what you know today's systems definitely they can't do so you know i often  
**Translation:** 

**[2322.30s] English:** say it's harder to come up with a conjecture a really good conjecture than it is to solve it  
**Translation:** Vocabulary: conjecture: 猜测

**[2327.08s] English:** so we may have systems soon that can solve pretty hard conjectures um you know i i am in maths  
**Translation:** 

**[2333.04s] English:** olympiad problems where we you know alpha proof  
**Translation:** Vocabulary: alpha: 阿尔法; conjectures: 猜想; olympiad: 奥林匹克

**[2335.86s] English:** you know alpha proof  
**Translation:** 

**[2336.08s] English:** year our system got you know silver medal in that really hard problems maybe eventually we'll  
**Translation:** 

**[2340.96s] English:** better solve a millennium price kind of problem but could a system come up with a conjecture  
**Translation:** 

**[2346.64s] English:** worthy of study that someone like terence tower would have gone you know what that's a really  
**Translation:** Vocabulary: millennium: 千年难题

**[2350.80s] English:** deep question about the nature of maths or the nature of numbers or the nature of physics  
**Translation:** 

**[2355.60s] English:** and that is far harder type of creativity and we don't really know today's systems clearly can't  
**Translation:** 

**[2361.68s] English:** do that and we're not quite sure what that mechanism would be this kind of leap of  
**Translation:** 

**[2365.84s] English:** imagination  
**Translation:** 

**[2366.08s] English:** like like einstein had when he came up with you know special relativity and then general relativity  
**Translation:** 

**[2371.44s] English:** with the knowledge he had at the time as for conjecture the you want to come up with a thing  
**Translation:** Vocabulary: einstein: 爱因斯坦; relativity: 相对论

**[2378.80s] English:** that's interesting it's amenable to proof yes so like it's easy to come up with a thing that's  
**Translation:** 

**[2383.76s] English:** extremely difficult yeah it's easy to come up with a thing that's extremely easy but that at  
**Translation:** 

**[2387.84s] English:** that very end that sweet spot right of of basically advancing the science and splitting  
**Translation:** 

**[2392.40s] English:** the hypothesis space into two ideally right whether if it's true or not it's going to be a  
**Translation:** Vocabulary: advancing: 推进

**[2395.84s] English:** little bit more complicated but it's going to be a little bit more complicated but it's going to be  
**Translation:** 

**[2400.00s] English:** And that's hard. And making something that's also, you know, falsifiable and within sort of the technologies that you have, you currently have available. So it's a very creative process, actually, highly creative process that I think just a kind of naive search on top of a model won't be enough for that.  
**Translation:** Vocabulary: falsifiable: 可证伪的; naive: 幼稚的

**[2420.92s] English:** Okay, the idea of splitting the hypothesis space into super interesting. So I've heard you say that there's basically no failure in or failure is extremely valuable. If it's done, if you construct the questions, right, if you construct the experiments, right, if you design them, right, that failure or success are both useful. So perhaps because it splits the hypothesis, basically, too, it's like a binary search.  
**Translation:** 

**[2444.02s] English:** That's right. So when you do like, you know, real blue sky research, there's no such thing as failure, really, as long as you're picking it.  
**Translation:** Vocabulary: binary: 二分搜索; hypothesis: 假设

**[2450.92s] English:** So to go to your dream.  
**Translation:** 

**[2480.92s] English:** Of modeling a cell, what are the big challenges that lay ahead for us to make that happen? We should maybe highlight that alpha four, I mean, there's just so many leaps. So alpha fold solved, if it's fair to say protein folding, and there's so many incredible things we could talk about there, including the open sourcing, everything you've released, alpha fold three is doing protein RNA DNA interactions, which is super complicated, and fascinating, this amenable to modeling alpha gene.  
**Translation:** Vocabulary: alpha: 阿尔法; amenable: 易于处理; sourcing: 开源

**[2510.92s] English:** genome predicts how small genetic changes, like if we think about single mutations, how they link to actual function. So  
**Translation:** 

**[2520.00s] English:** So it seems like it's creeping along to much more complicated things like a cell.  
**Translation:** Vocabulary: creeping: 缓慢进展; genome: 基因组; mutations: 突变

**[2527.24s] English:** But a cell has a lot of really complicated components.  
**Translation:** 

**[2530.50s] English:** Yeah. So what I've tried to do throughout my career is I have these really grand dreams.  
**Translation:** 

**[2535.56s] English:** And then I try to, as you've noticed, and then I try to break, but I try to break them down.  
**Translation:** 

**[2539.52s] English:** You know, it's easy to have a kind of crazy ambitious dream.  
**Translation:** 

**[2543.48s] English:** But the trick is, how do you break it down into manageable, achievable interim steps that are meaningful and useful in their own right?  
**Translation:** 

**[2552.80s] English:** And so virtual cell, which is what I call the project of modeling a cell.  
**Translation:** Vocabulary: achievable: 可实现; interim: 过渡的

**[2556.24s] English:** I've had this idea, you know, of wanting to do that for maybe more like 25 years.  
**Translation:** 

**[2561.18s] English:** And I used to talk with Paul Nurse, who is a bit of a mentor of mine in biology.  
**Translation:** 

**[2565.44s] English:** He runs the, you know, founded the Crick Institute and won the Nobel Prize in 2001.  
**Translation:** 

**[2572.08s] English:** We've been talking about it since.  
**Translation:** Vocabulary: nobel: 诺贝尔

**[2573.48s] English:** You know, before, you know, in the 90s.  
**Translation:** 

**[2576.44s] English:** And I used to come back to every five years is like, what would you need to model of the full internals of a cell so that you could do experiments on the virtual cell and what those experiments, you know, in silico and those predictions would be useful for you to save you a lot of time in the wet lab, right?  
**Translation:** Vocabulary: internals: 细胞内部; silico: 计算机模拟

**[2592.78s] English:** That would be the dream.  
**Translation:** 

**[2593.58s] English:** Maybe you could 100x speed up experiments by doing most of it in silico, the search in silico, and then you do the validation step in the wet lab.  
**Translation:** Vocabulary: validation: 验证步骤

**[2601.04s] English:** That would be that's the that's the dream.  
**Translation:** 

**[2603.36s] English:** And.  
**Translation:** 

**[2603.48s] English:** And so but maybe now, finally, so I was trying to build these components, alpha fold being one that that would allow you eventually to model the full interaction, a full simulation of a cell.  
**Translation:** 

**[2616.34s] English:** And I'd probably start with a yeast cell.  
**Translation:** Vocabulary: alpha: 阿尔法; simulation: 模拟; yeast: 酵母

**[2618.46s] English:** And partly that's what Paul Nurse studied, because the yeast cell is like a full organism.  
**Translation:** 

**[2622.30s] English:** That's a single cell.  
**Translation:** 

**[2623.50s] English:** Right.  
**Translation:** 

**[2623.78s] English:** So it's the kind of simplest single cell organism.  
**Translation:** 

**[2626.80s] English:** And so it's not just a cell.  
**Translation:** 

**[2628.14s] English:** It's a full organism.  
**Translation:** 

**[2630.44s] English:** And yeast is very well understood.  
**Translation:** 

**[2633.10s] English:** And.  
**Translation:** 

**[2633.12s] English:** And so that would be a good candidate for a kind of full simulated model.  
**Translation:** 

**[2637.94s] English:** Now, alpha fold is the.  
**Translation:** 

**[2640.00s] English:** is the solution to the kind of static picture of what does a protein look, 3D structured protein  
**Translation:** 

**[2645.02s] English:** look like, a static picture of it. But we know that biology, all the interesting things happen  
**Translation:** 

**[2649.46s] English:** with the dynamics, the interactions. And that's what AlphaFold3 is the first step towards is  
**Translation:** 

**[2654.46s] English:** modeling those interactions. So first of all, pairwise, you know, proteins with proteins,  
**Translation:** Vocabulary: pairwise: 成对地

**[2659.04s] English:** proteins with RNA and DNA. But then the next step after that would be modeling maybe a whole pathway,  
**Translation:** 

**[2664.62s] English:** maybe like the TOR pathway that's involved in cancer or something like this. And then eventually  
**Translation:** Vocabulary: pathway: 信号通路

**[2668.64s] English:** you might be able to model, you know, a whole cell. Also, there's another complexity here that  
**Translation:** 

**[2673.32s] English:** stuff in a cell happens at different timescales. Is that tricky? It's like, you know, protein  
**Translation:** Vocabulary: complexity: 复杂性; timescales: 时间尺度

**[2679.34s] English:** folding is, you know, super fast. Yes. I don't know all the biological mechanisms,  
**Translation:** 

**[2686.24s] English:** but some of them take a long time. Yeah. And so is that that's a level. So the levels of  
**Translation:** 

**[2690.24s] English:** interaction has a different temporal scale that you have to be able to model. So that would be  
**Translation:** 

**[2694.56s] English:** hard. So you'd probably need several simulated systems that can interact at these.  
**Translation:** Vocabulary: simulated: 模拟; temporal: 时间的

**[2698.64s] English:** Different temporal dynamics, or at least maybe it's like a hierarchical system. So  
**Translation:** 

**[2702.96s] English:** you can jump up and down the different temporal stages. So can you avoid, I mean, one of the  
**Translation:** Vocabulary: hierarchical: 等级制度

**[2710.14s] English:** challenges here is not avoid simulating, for example, the quantum mechanical aspects of any  
**Translation:** 

**[2717.66s] English:** of this, right? You want to not overmodel. You can skip ahead to just model the really high level  
**Translation:** Vocabulary: overmodel: 过度建模; simulating: 模拟

**[2724.24s] English:** things that get you a really good estimate of what's going to happen. Yes. So you've got to  
**Translation:** 

**[2728.64s] English:** make a decision when you're modeling any natural system. What is the cutoff level of the granularity  
**Translation:** Vocabulary: cutoff: 截止点; granularity: 精细度

**[2732.74s] English:** that you're going to model it to that then captures the dynamics that you're interested in.  
**Translation:** 

**[2737.24s] English:** So probably for a cell, I would hope that would be the protein level and that one wouldn't have to go  
**Translation:** 

**[2743.22s] English:** down to the atomic level. So, you know, of course, that's where alpha fold stock kicks in. So that  
**Translation:** 

**[2749.94s] English:** would be kind of the basis. And then you'd build these higher level simulations that take those as  
**Translation:** Vocabulary: alpha: 阿尔法

**[2757.04s] English:** building blocks. And then.  
**Translation:** 

**[2758.64s] English:** You get the emergent behavior.  
**Translation:** Vocabulary: emergent: 涌现的

**[2760.98s] English:** Apologize for the pothead questions ahead of time, but do you think we'll be able to simulate a model, the origin of life?  
**Translation:** 

**[2771.30s] English:** So being able to simulate the first from non-living organisms, the birth of a living organism.  
**Translation:** Vocabulary: simulate: 模拟

**[2779.74s] English:** I think that's one of the, of course, one of the deepest and most fascinating questions.  
**Translation:** 

**[2783.96s] English:** I love that area of biology.  
**Translation:** 

**[2785.56s] English:** You know, there's people like, there's a great book by Nick Lane, one of the top, top experts in this area called the 10 Great Inventions of Evolution.  
**Translation:** 

**[2794.70s] English:** I think it's fantastic.  
**Translation:** 

**[2795.48s] English:** And it also speaks to what the great filters might be, you know, prior or are they ahead of us?  
**Translation:** 

**[2800.74s] English:** I think they're most likely in the past, if you read that book, of how unlikely to go, you know, have any life at all.  
**Translation:** 

**[2806.94s] English:** And then single cell to multi-cell seems an unbelievably big jump that took like a billion years, I think, on Earth to do.  
**Translation:** 

**[2813.60s] English:** Right. So it shows you how hard it was.  
**Translation:** Vocabulary: unbelievably: 难以置信地

**[2815.30s] English:** Right.  
**Translation:** 

**[2815.56s] English:** In theory, we're super happy for a very long time.  
**Translation:** 

**[2817.30s] English:** For a very long time before they captured mitochondria somehow, right?  
**Translation:** 

**[2820.54s] English:** I don't see why not, why AI couldn't help with that, some kind of simulation.  
**Translation:** Vocabulary: mitochondria: 线粒体; simulation: 模拟

**[2825.70s] English:** Again, it's again, it's a bit of a search process through a combinatorial space.  
**Translation:** 

**[2830.10s] English:** Here's like all the, you know, the chemical soup that you start with, the primordial soup that, you know, maybe was on Earth near these hot vents.  
**Translation:** Vocabulary: combinatorial: 组合搜索; primordial: 原始汤; vents: 热泉出口

**[2837.66s] English:** Here's some initial conditions.  
**Translation:** 

**[2839.26s] English:** Can you generate something that looks like a cell?  
**Translation:** 

**[2842.32s] English:** So perhaps that would be a next stage after the virtual cell project.  
**Translation:** 

**[2845.56s] English:** It is, well, how could you actually, something like that emerge from the chemical soup?  
**Translation:** 

**[2850.86s] English:** Well, I would love it if there was a move 37 for the origin of life.  
**Translation:** 

**[2854.44s] English:** Yeah.  
**Translation:** 

**[2854.74s] English:** I think that's one of the sort of great mysteries.  
**Translation:** 

**[2857.82s] English:** I think ultimately what we'll figure out is they're continuing.  
**Translation:** 

**[2860.22s] English:** There's no such thing as a line between non-living and living.  
**Translation:** 

**[2862.82s] English:** But if we can make that rigorous.  
**Translation:** Vocabulary: rigorous: 严谨

**[2864.62s] English:** Yes.  
**Translation:** 

**[2865.04s] English:** That the very thing from the Big Bang to today has been the same process.  
**Translation:** 

**[2869.82s] English:** If we can break down that wall that we've constructed in our minds of the actual origin of,  
**Translation:** 

**[2875.56s] English:** from non-living to living, and it's not a line, that it's a continuum.  
**Translation:** 

**[2880.00s] English:** next physics and chemistry and biology yeah there's no line i mean this is my whole reason  
**Translation:** 

**[2884.66s] English:** why i worked on ai and agi my whole life because i think it can be the ultimate tool to help us  
**Translation:** 

**[2889.80s] English:** answer these kind of questions and i don't really understand why um you know the average person  
**Translation:** 

**[2895.42s] English:** doesn't think like worry about this stuff more like how how can we not have a good definition  
**Translation:** 

**[2901.06s] English:** of life and not and not living and non-living and the nature of time and let alone consciousness and  
**Translation:** 

**[2907.00s] English:** gravity and all these things it's it's just and quantum mechanics weirdness it's just to me it's  
**Translation:** Vocabulary: gravity: 引力; weirdness: 奇异现象

**[2912.78s] English:** i've always had is this sort of screaming at me in my face the whole i need that's it's getting  
**Translation:** 

**[2917.44s] English:** louder you know it's like how what is going on here you know in in and i mean that in the deeper  
**Translation:** 

**[2922.38s] English:** sense like in the you know the nature of reality which has to be the ultimate question yeah that  
**Translation:** 

**[2927.52s] English:** would answer all of these things it's sort of crazy if you think about it we can stare at each  
**Translation:** 

**[2930.86s] English:** other and all these living things all the time we can inspect it microscopes and take it apart  
**Translation:** 

**[2937.00s] English:** down to the atomic level and yet we still can't answer that clearly in a simple way that question  
**Translation:** 

**[2942.14s] English:** of how do you define living yeah it's kind of amazing yeah living you can kind of talk your  
**Translation:** 

**[2947.88s] English:** way out of thinking about but like consciousness like we have this very obviously subjective  
**Translation:** 

**[2953.14s] English:** conscious experience like we're at the center of our own world and it it feels like something and  
**Translation:** 

**[2957.92s] English:** then how how are you not screaming yeah at the mystery of it all right i mean but really humans  
**Translation:** 

**[2964.70s] English:** have been contending with the mystery  
**Translation:** 

**[2967.00s] English:** of the world around them uh for a long long there's a lot of mysteries like what's up with  
**Translation:** Vocabulary: contending: 争辩

**[2973.00s] English:** the sun and and the rain yeah like what's that about and then like last year we had a lot of  
**Translation:** 

**[2979.10s] English:** rain and this year we don't have rain like what did we do wrong humans have been asking that  
**Translation:** 

**[2983.96s] English:** question for a long time so we're quite i guess we've developed a lot of mechanisms to cope with  
**Translation:** 

**[2988.74s] English:** this uh these deep mysteries that we can't fully we can see but we can't fully understand and we  
**Translation:** 

**[2994.22s] English:** have to have to just get on with daily life and and  
**Translation:** 

**[2997.00s] English:** we get we keep ourselves busy right in a way did we keep ourselves distracted  
**Translation:** Vocabulary: distracted: 分心

**[3000.00s] English:** I mean, weather is one of the most important questions of human history.  
**Translation:** 

**[3005.30s] English:** That's the go-to small talk direction of the weather.  
**Translation:** 

**[3010.06s] English:** Especially in England.  
**Translation:** 

**[3011.40s] English:** And then, which is famously an extremely difficult system to model.  
**Translation:** 

**[3017.08s] English:** And even that system, Google DeepMind has made progress on.  
**Translation:** 

**[3022.76s] English:** Yes, we've created the best weather prediction systems in the world.  
**Translation:** 

**[3027.04s] English:** And they're better than traditional fluid dynamics sort of systems that are usually calculated on massive supercomputers.  
**Translation:** 

**[3034.16s] English:** Takes days to calculate it.  
**Translation:** Vocabulary: supercomputers: 超级计算机

**[3036.22s] English:** We've managed to model a lot of the weather dynamics with neural network systems.  
**Translation:** 

**[3040.84s] English:** With our WeatherNet system.  
**Translation:** Vocabulary: neural: 神经网络

**[3042.58s] English:** And again, it's interesting that those kinds of dynamics can be modeled.  
**Translation:** 

**[3046.44s] English:** Even though they're very complicated, almost bordering on chaotic systems in some cases.  
**Translation:** Vocabulary: bordering: 临近

**[3050.64s] English:** A lot of the interesting aspects of that can be modeled by these neural network systems.  
**Translation:** 

**[3055.98s] English:** Including very...  
**Translation:** 

**[3057.04s] English:** Very recently, we had, you know, cyclone prediction of where, you know, piles of hurricanes might go.  
**Translation:** 

**[3061.24s] English:** Of course, super useful, super important for the world.  
**Translation:** Vocabulary: cyclone: 气旋; hurricanes: 飓风

**[3063.90s] English:** And it's super important to do that very timely and very quickly.  
**Translation:** 

**[3066.78s] English:** And as well as accurately.  
**Translation:** 

**[3068.52s] English:** And I think it's a very promising direction, again, of, you know, simulating.  
**Translation:** 

**[3072.58s] English:** And so that you can run forward predictions and simulations of very complicated real-world systems.  
**Translation:** Vocabulary: simulating: 模拟

**[3078.52s] English:** I should mention that I've got a chance in Texas to meet a community of folks called the Storm Chasers.  
**Translation:** 

**[3084.98s] English:** Yes.  
**Translation:** Vocabulary: chasers: 追风暴的人; texas: 德克萨斯州

**[3085.16s] English:** And what's really incredible about...  
**Translation:** 

**[3087.04s] English:** I need to talk to them more.  
**Translation:** 

**[3088.62s] English:** Is they're extremely tech-savvy.  
**Translation:** 

**[3090.04s] English:** Because what they have to do is they have to use models to predict where the storm is.  
**Translation:** 

**[3094.32s] English:** So they're...  
**Translation:** 

**[3094.80s] English:** It's this beautiful mix of, like, crazy enough to, like, go into the eye of the storm.  
**Translation:** 

**[3100.82s] English:** And, like, in order to protect your life and predict where the extreme events are going to be,  
**Translation:** 

**[3106.02s] English:** they have to have increasingly sophisticated models of weather.  
**Translation:** 

**[3109.94s] English:** Yeah.  
**Translation:** 

**[3110.08s] English:** Yeah, it's a beautiful balance of, like, being in it as living organisms.  
**Translation:** 

**[3116.52s] English:** And the...  
**Translation:** 

**[3117.00s] English:** The cutting edge of science.  
**Translation:** 

**[3118.26s] English:** So they actually might be using...  
**Translation:** 

**[3120.00s] English:** deep mind system so that's yeah they hopefully they are and i'd love to join them in one of  
**Translation:** 

**[3124.34s] English:** those cases they look amazing right to actually experience it one time exactly and then also to  
**Translation:** 

**[3129.02s] English:** experience the correct prediction yeah where something will come and how it's going to evolve  
**Translation:** 

**[3134.00s] English:** it's incredible yeah you've estimated that we'll have agi by 2030 um so there's interesting  
**Translation:** 

**[3141.68s] English:** questions around that how will we actually know that we got there uh and uh what may be the move  
**Translation:** 

**[3149.86s] English:** quote move 37 of agi my estimate is sort of 50 chance by in the next five years so you know by  
**Translation:** 

**[3157.86s] English:** 2030 let's say and uh so i think there's a good chance that that could happen part of it is what  
**Translation:** 

**[3163.66s] English:** is your definition of agi of course people arguing about that now and and uh mine's quite a high bar  
**Translation:** 

**[3169.18s] English:** and always has been of like can we match the cognitive functions that the brain has right so  
**Translation:** 

**[3174.26s] English:** we know our brains are pretty much general turing machines approximate and of course  
**Translation:** 

**[3179.86s] English:** we've created incredible modern civilization with our minds so that also speaks to how general the  
**Translation:** Vocabulary: approximate: 近似; turing: 图灵

**[3185.62s] English:** brain is and um for us to know we have a true agi we would have to like make sure that it has all  
**Translation:** 

**[3192.54s] English:** those capabilities it isn't kind of a jagged intelligence where some things it's really good  
**Translation:** Vocabulary: jagged: 参差不齐

**[3196.82s] English:** at like today's systems but other things it's really uh flawed at and and that's what we  
**Translation:** 

**[3202.04s] English:** currently have with today's systems they're not consistent so you'd want that consistency of  
**Translation:** 

**[3206.10s] English:** intelligence across the board and then we have some missing i think  
**Translation:** 

**[3209.86s] English:** capabilities like sort of uh the true invention capabilities and creativity that we were talking  
**Translation:** 

**[3214.90s] English:** about earlier so you'd want to see those how you test that um i think you just test it one way to  
**Translation:** 

**[3220.32s] English:** do it would be kind of brute force test of tens of thousands of cognitive tasks that um you know  
**Translation:** Vocabulary: brute: 粗暴的; cognitive: 认知的

**[3226.26s] English:** we know that humans can do uh and maybe also make the system available to a few hundred of the world's  
**Translation:** 

**[3233.60s] English:** top experts uh terence towers of each each subject area and see if they can find you know given given  
**Translation:** 

**[3239.86s] English:** the  
**Translation:** 

**[3240.00s] English:** month or two and see if they can find an obvious flaw in the system and if they can't then i think  
**Translation:** 

**[3245.64s] English:** you're you're pretty uh you know pretty you can be pretty confident we have a fully general system  
**Translation:** 

**[3250.82s] English:** maybe to push back a little bit it seems like humans are really incredible  
**Translation:** 

**[3254.38s] English:** as the intelligence improves across all domains to take it for granted like you mentioned terence  
**Translation:** 

**[3261.72s] English:** tau uh these brilliant experts they might quickly in a span of weeks take for granted all the  
**Translation:** 

**[3269.48s] English:** incredible things you can do and then focus in while ha ha right there you know i i consider  
**Translation:** 

**[3274.38s] English:** myself uh first of all human yeah uh i identify as human um this i you know some people listen  
**Translation:** 

**[3284.90s] English:** to me talk and they're like that guy is not good at talking the stuttering the you know so like  
**Translation:** 

**[3290.80s] English:** even humans have obvious across domains limits even just outside of mathematics and physics and  
**Translation:** Vocabulary: stuttering: 口吃

**[3297.74s] English:** so on  
**Translation:** 

**[3299.48s] English:** i i wonder if it will take something like a move 37 so on the positive side versus like  
**Translation:** 

**[3305.84s] English:** a barrage of 10 000 cognitive tasks where it would be one or two where it's like yes holy  
**Translation:** 

**[3313.34s] English:** shit this is special exactly so i think there's the sort of blanket testing to just make sure  
**Translation:** 

**[3318.22s] English:** you've got the consistency but i think there are the sort of lighthouse moments like the move 37  
**Translation:** 

**[3325.02s] English:** that would i would be looking for so one would be inventing a new control system and the other would be  
**Translation:** Vocabulary: lighthouse: 灯塔时刻

**[3329.48s] English:** inventing a game like go not just come up with move 37 a new strategy but can it invent a game that's  
**Translation:** 

**[3359.42s] English:** a new strategy and then come up with a game that's a new strategy and then come up with a new strategy  
**Translation:** 

**[3359.48s] English:** that's deep  
**Translation:** 

**[3360.00s] English:** as aesthetically beautiful, as elegant as go. And those are the sorts of things I would be  
**Translation:** Vocabulary: aesthetically: 审美地

**[3364.78s] English:** looking out for. And probably a system being able to do several of those things, right,  
**Translation:** 

**[3370.42s] English:** for it to be very general, not just one domain. And so I think that would be the signs,  
**Translation:** 

**[3375.64s] English:** at least that I would be looking for, that we've got a system that's AGI level. And then maybe to  
**Translation:** 

**[3381.36s] English:** fill that out, you would also check the consistency, you know, make sure there's no holes  
**Translation:** 

**[3385.28s] English:** in that system either. Yeah, something like a new conjecture or scientific discovery.  
**Translation:** 

**[3390.78s] English:** That would be a cool feeling. Yeah, that would be amazing. So it's not just helping us do that,  
**Translation:** Vocabulary: conjecture: 猜测

**[3395.40s] English:** but actually coming up with something brand new. And you would be in the room for that.  
**Translation:** 

**[3399.76s] English:** And so it would be like probably two or three months before announcing it. And you would just  
**Translation:** 

**[3406.14s] English:** be sitting there trying not to tweet. Something like that. Exactly. It's like, what is this  
**Translation:** 

**[3412.06s] English:** amazing new, you know, physics idea. And then we would try.  
**Translation:** 

**[3415.28s] English:** Probably check it with world experts in that domain, right, and validate it and kind of go  
**Translation:** 

**[3421.12s] English:** through its workings. And I guess it would be explaining its workings, too. Yeah, be an amazing  
**Translation:** Vocabulary: validate: 验证; workings: 工作机制

**[3427.06s] English:** moment. Do you worry that we as humans, even expert humans like you might miss it? Well,  
**Translation:** 

**[3432.80s] English:** it may be pretty complicated. So it could be the analogy I give there is I don't think it will be  
**Translation:** 

**[3438.04s] English:** totally mysterious to the to the best human scientists, but it may be a bit like, for example,  
**Translation:** 

**[3444.86s] English:** in chess.  
**Translation:** 

**[3445.28s] English:** If I was to talk to Garry Kasparov or Magnus Carlsen and play a game with them and they make  
**Translation:** 

**[3450.80s] English:** a brilliant move, I might not be able to come up with that move, but they could explain why  
**Translation:** Vocabulary: garry: 加里·卡斯帕罗夫; kasparov: 卡斯帕罗夫; magnus: 马格努斯·卡尔森

**[3455.40s] English:** afterwards that move made sense. And we would be able to understand it to some degree, not to the  
**Translation:** 

**[3460.14s] English:** level they do. But, you know, if they were good at explaining, which is actually part of intelligence,  
**Translation:** 

**[3464.54s] English:** too, is being able to explain in a simple way that what you're thinking about. I think that  
**Translation:** 

**[3470.24s] English:** that will be very possible for the best human scientists. But I wonder maybe you can you can  
**Translation:** 

**[3474.22s] English:** educate me on the side.  
**Translation:** 

**[3475.28s] English:** I wonder if there's moves from Magnus or Garry where they at first will.  
**Translation:** 

**[3480.00s] English:** dismiss it as a bad move yeah sure it could be but then afterwards they'll figure out with their  
**Translation:** 

**[3486.36s] English:** intuition that that this why this works and then and then and then empirically the nice thing about  
**Translation:** Vocabulary: empirically: 经验上; intuition: 直觉

**[3490.90s] English:** games is one of the great things about games is you can it's a sort of scientific test does it  
**Translation:** 

**[3495.00s] English:** do you win the game or not win and then um that tells you okay that move in the end was good that  
**Translation:** 

**[3501.54s] English:** strategy was good and then you can go back and analyze that and and and and explain even to  
**Translation:** 

**[3506.28s] English:** yourself a little bit more why explore around it and that's how chess analysis and things like  
**Translation:** 

**[3511.36s] English:** that work so perhaps that's why my brain works like that because i've been doing that since i  
**Translation:** 

**[3515.42s] English:** was four and you're trained you know it's sort of hardcore training in that way but even even now  
**Translation:** Vocabulary: hardcore: 严格的

**[3521.00s] English:** like when i generate code there is this kind of nuanced fascinating contention that's happening  
**Translation:** 

**[3528.90s] English:** where i might at first identify as a set of generated code is incorrect in some interesting  
**Translation:** Vocabulary: contention: 争端; nuanced: 细腻

**[3535.88s] English:** nuance  
**Translation:** 

**[3536.26s] English:** ways but then i'm always have to ask the question is there a deeper insight here that  
**Translation:** Vocabulary: nuance: 细微差别

**[3541.80s] English:** that i'm the one who's incorrect and that's going to as the systems get more and more intelligent  
**Translation:** 

**[3547.90s] English:** you're gonna have to contend with that it's like what what what is this a bug or a feature what you  
**Translation:** Vocabulary: contend: 应对

**[3553.68s] English:** just came up with yeah and they're going to be pretty complicated to do but of course it will be  
**Translation:** 

**[3557.42s] English:** you can imagine also ai systems that are producing that code or whatever that is  
**Translation:** 

**[3561.70s] English:** and then human programmers looking at but also not unaided with the help of  
**Translation:** 

**[3566.26s] English:** ai tools as well so it's going to be kind of an interesting you know maybe different ai tools to  
**Translation:** 

**[3571.66s] English:** the ones that they're more about you know kind of monitoring tools are the ones that generated it  
**Translation:** 

**[3575.84s] English:** so if we look at an agi system sorry to bring it back up but alpha evolve super cool so alpha  
**Translation:** Vocabulary: alpha: 阿尔法

**[3583.74s] English:** evolve enables on the programming side something like recursive self-improvement uh potentially  
**Translation:** 

**[3590.42s] English:** like what if we can imagine what that agi system maybe not the first version but  
**Translation:** Vocabulary: recursive: 递归

**[3596.26s] English:** a few versions beyond that what does that actually look like  
**Translation:** 

**[3600.00s] English:** Do you think it will be simple?  
**Translation:** 

**[3601.44s] English:** Do you think it will be something like a self-improving program and a simple one?  
**Translation:** 

**[3606.36s] English:** I mean, potentially that's possible, I would say.  
**Translation:** 

**[3608.52s] English:** I'm not sure it's even desirable because that's a kind of like hard takeoff scenario.  
**Translation:** 

**[3612.86s] English:** But these current systems like Alpha Evolve, they have, you know, human in the loop deciding  
**Translation:** Vocabulary: desirable: 值得期望的

**[3618.70s] English:** on various things.  
**Translation:** 

**[3620.20s] English:** They're separate hybrid systems that interact.  
**Translation:** 

**[3622.72s] English:** One could imagine eventually doing that end to end.  
**Translation:** 

**[3625.88s] English:** I don't see why that wouldn't be possible.  
**Translation:** 

**[3627.62s] English:** But right now, you know, I think the systems are not good enough to do that in terms of  
**Translation:** 

**[3632.48s] English:** coming up with the architecture of the code.  
**Translation:** 

**[3635.94s] English:** And again, it's a little bit reconnected to this idea of coming up with a new conjectural  
**Translation:** 

**[3639.88s] English:** hypothesis.  
**Translation:** Vocabulary: conjectural: 推测的; hypothesis: 假设; reconnected: 重新关联

**[3641.28s] English:** They're good if you give them very specific instructions about what you're trying to do.  
**Translation:** 

**[3645.80s] English:** But if you give them a very vague high level instruction, that wouldn't work currently.  
**Translation:** 

**[3650.62s] English:** And I think that's related to this idea of like invent a game as good as go, right?  
**Translation:** 

**[3654.96s] English:** Imagine that was the prompt.  
**Translation:** 

**[3656.46s] English:** That's pretty undesperate.  
**Translation:** 

**[3657.62s] English:** And so the current systems wouldn't know, I think, what to do with that, how to narrow  
**Translation:** Vocabulary: undesperate: 不绝望

**[3662.40s] English:** that down to something tractable.  
**Translation:** 

**[3664.28s] English:** And I think there's similar like, look, just make a better version of yourself.  
**Translation:** Vocabulary: tractable: 易于处理

**[3666.98s] English:** That's too unconstrained.  
**Translation:** 

**[3669.44s] English:** But we've done it in, you know, and as you know, with Alpha Evolve, like things like  
**Translation:** Vocabulary: unconstrained: 缺乏限制

**[3672.86s] English:** faster matrix multiplication.  
**Translation:** 

**[3674.52s] English:** So when you hone it down to a very specific thing you want, it's very good at incrementally  
**Translation:** Vocabulary: incrementally: 逐步地; matrix: 矩阵; multiplication: 乘法

**[3680.48s] English:** improving that.  
**Translation:** 

**[3681.30s] English:** But at the moment, these are more like incremental improvements, sort of small iterations.  
**Translation:** Vocabulary: incremental: 逐步的; iterations: 迭代

**[3685.74s] English:** Whereas if, you know, if you want to do a very specific thing, you want to do a very  
**Translation:** 

**[3687.62s] English:** big leap in understanding, you need a much larger advance.  
**Translation:** 

**[3694.34s] English:** Yeah, but it could also be sort of to push back against hard takeoff scenario.  
**Translation:** 

**[3697.94s] English:** It could be just a sequence of incremental improvements, like matrix multiplication.  
**Translation:** 

**[3704.78s] English:** Like it has to sit there for days thinking how to incrementally improve a thing.  
**Translation:** 

**[3709.96s] English:** And it does so recursively.  
**Translation:** Vocabulary: recursively: 递归地

**[3711.84s] English:** And as you do more and more improvement, it'll slow down.  
**Translation:** 

**[3715.36s] English:** Right.  
**Translation:** 

**[3715.54s] English:** There'll be like a, like a...  
**Translation:** 

**[3717.62s] English:** The path to AGI won't be like a...  
**Translation:** 

**[3720.00s] English:** be a gradual improvement over time. Yes. If it was just incremental improvements,  
**Translation:** 

**[3725.04s] English:** that's how it would look. So the question is, could it come up with a new leap like the  
**Translation:** 

**[3729.48s] English:** Transformers architecture? Could it have done that back in 2017 when we did it and Brain did it?  
**Translation:** 

**[3735.80s] English:** And it's not clear that these systems, something like AlphaVol wouldn't be able to do, make such  
**Translation:** 

**[3741.16s] English:** a big leap. So for sure, these systems are good. We have systems, I think, that can do incremental  
**Translation:** 

**[3745.80s] English:** hill climbing. And that's a kind of bigger question about, is that all that's needed from  
**Translation:** 

**[3749.80s] English:** here? Or do we actually need one or two more big breakthroughs? And can the same kind of  
**Translation:** 

**[3755.94s] English:** systems provide the breakthroughs also? So make it a bunch of S-curves, like incremental  
**Translation:** Vocabulary: breakthroughs: 重大突破

**[3761.58s] English:** improvement, but also every once in a while, leaps. Yeah. I don't think anyone has systems  
**Translation:** 

**[3766.66s] English:** that have shown unequivocally those big leaps. We have a lot of systems that do the hill climbing  
**Translation:** Vocabulary: unequivocally: 毫无疑问地

**[3773.08s] English:** of the S-curve that you're currently on. Yeah.  
**Translation:** 

**[3775.80s] English:** And that would be the Move 37. Yeah, I think it would be a leap, something like that.  
**Translation:** 

**[3781.40s] English:** Do you think the scaling laws are holding strong on pre-training, post-training, test time, compute?  
**Translation:** 

**[3787.98s] English:** Do you, on the flip side of that, anticipate AI progress hitting a wall?  
**Translation:** Vocabulary: anticipate: 預期

**[3793.16s] English:** We certainly feel there's a lot more room just in the scaling. So actually all steps,  
**Translation:** 

**[3798.64s] English:** pre-training, post-training, and inference time. So there's sort of three scalings that are  
**Translation:** Vocabulary: inference: 推理

**[3804.88s] English:** happening concurrently.  
**Translation:** 

**[3805.80s] English:** And again, there, it's about how innovative you can be. And we pride ourselves on having the  
**Translation:** Vocabulary: concurrently: 同时进行

**[3813.72s] English:** broadest and deepest research bench. We have amazing, incredible researchers and people like  
**Translation:** 

**[3821.18s] English:** Noam Shazia, who came up with Transformers, and Dave Silver, who led the AlphaGo project,  
**Translation:** Vocabulary: broadest: 最广泛的

**[3826.64s] English:** and so on. And that research base means that if some new breakthrough is required, like in AlphaGo,  
**Translation:** 

**[3835.80s] English:** or Transformers, I would back us to be the place that does that.  
**Translation:** 

**[3840.00s] English:** you quite like it when the terrain gets harder right because then it veers more from just  
**Translation:** 

**[3844.38s] English:** engineering to to true research and you know research plus engineering and that's our sweet  
**Translation:** Vocabulary: terrain: 地形; veers: 转向

**[3850.24s] English:** spot and i think that's harder it's harder to invent things than to than to um you know fast  
**Translation:** 

**[3856.38s] English:** follow and um so you know we don't know i would say it's a it's kind of 50 50 whether new things  
**Translation:** 

**[3863.62s] English:** are needed or whether the scaling the existing stuff is going to be enough and so in true kind  
**Translation:** 

**[3868.98s] English:** of empirical fashion we're pushing both of those as hard as possible the new blue sky ideas and you  
**Translation:** Vocabulary: empirical: 经验的

**[3874.94s] English:** know maybe about half our resources on that and then and then uh scaling to the max the the current  
**Translation:** 

**[3880.58s] English:** the current capabilities and um we're still seeing some you know fantastic progress on  
**Translation:** 

**[3886.34s] English:** each different version of gemini that's interesting the way you put it in terms of the deep bench  
**Translation:** 

**[3891.38s] English:** that if uh progress towards agi is more than just scaling compute  
**Translation:** Vocabulary: gemini: 双子座模型

**[3898.98s] English:** so the engineering side of the problem and is more on the scientific side where there's  
**Translation:** 

**[3905.70s] English:** breakthroughs needed then you feel confident deep mind as well google deep mind as well  
**Translation:** Vocabulary: breakthroughs: 重大突破

**[3910.36s] English:** positioned to yes kick ass in that domain well i mean if you look at the history of the last  
**Translation:** 

**[3915.08s] English:** decade or 15 years um it's been i mean you know maybe i don't know 80 90 percent of the breakthroughs  
**Translation:** 

**[3920.82s] English:** that more that underpins modern ai field today was from you know originally google brain google  
**Translation:** 

**[3925.18s] English:** research and deep mind so yeah i would back that to continue hopefully  
**Translation:** Vocabulary: underpins: 奠定基础

**[3928.98s] English:** uh so on the data side are you concerned about running out of high quality data especially high  
**Translation:** 

**[3935.14s] English:** quality human data i'm not very worried about that partly because i think there's enough data  
**Translation:** 

**[3940.14s] English:** uh and it's been proven to get the systems to be pretty good and this goes back to simulations  
**Translation:** 

**[3946.14s] English:** again if you do you have enough data to make simulations or so that you can create more  
**Translation:** 

**[3951.40s] English:** synthetic data that are from the right distribution obviously that's the key so you need enough real  
**Translation:** 

**[3957.40s] English:** world data in order to be able to do that so i'm not very worried about that i'm not very worried  
**Translation:** 

**[3958.96s] English:** about that so i'm not very worried about that i'm not very worried about that i'm not very worried  
**Translation:** 

**[3960.00s] English:** create those kinds of generator data generators and um i think that we're at that step at the  
**Translation:** Vocabulary: generator: 发电器

**[3964.80s] English:** moment yeah you've done a lot of incredible stuff on the side of science and biology  
**Translation:** 

**[3968.60s] English:** doing a lot with not so much data yeah i mean it's still a lot of data but i guess enough  
**Translation:** 

**[3974.56s] English:** take that going exactly yeah exactly uh how crucial is the scaling of compute to building  
**Translation:** 

**[3981.14s] English:** this is a question that's an engineering question it's a almost a geopolitical question  
**Translation:** Vocabulary: geopolitical: 地缘政治的

**[3987.62s] English:** because it also integrated into that is supply chains and energy yes a thing that you care a  
**Translation:** 

**[3994.72s] English:** lot about which is uh potentially fusion yes innovating on the side of energy also do you  
**Translation:** Vocabulary: innovating: 创新

**[3999.58s] English:** think we're going to keep scaling compute i think so for several reasons i think compute there's  
**Translation:** 

**[4004.68s] English:** there's the amount of compute you have for training often it needs to be co-located so  
**Translation:** 

**[4008.86s] English:** actually even like you know bandwidth constraints between data centers can affect that so it's it's  
**Translation:** 

**[4014.64s] English:** it's there's additional constraints even there and that  
**Translation:** Vocabulary: bandwidth: 带宽; constraints: 限制

**[4017.62s] English:** that's important for training obviously the largest models you can but there's also because  
**Translation:** 

**[4022.34s] English:** now ai systems are in products and being used by billions of people around the world you need a ton  
**Translation:** 

**[4028.66s] English:** of inference compute now um and then on top of that there's the thinking systems the new paradigm  
**Translation:** 

**[4034.52s] English:** of the last year that uh where they get smarter the longer amount of inference time you give them  
**Translation:** Vocabulary: inference: 推理; paradigm: 范式

**[4039.74s] English:** at test time so all of those things need a lot of compute and i don't really see that slowing down  
**Translation:** 

**[4045.90s] English:** um and  
**Translation:** 

**[4047.62s] English:** as ai systems become better they'll become more useful and there'll be more demand for them  
**Translation:** 

**[4051.56s] English:** so both from the training side the training side actually is is only just one part of that may even  
**Translation:** 

**[4055.98s] English:** become the smaller part of of what's needed um uh in the overall compute that that's required  
**Translation:** 

**[4062.20s] English:** yeah that's one sort of almost meme-y kind of thing which is like the success and the incredible  
**Translation:** 

**[4067.40s] English:** aspects of vo3 there's uh people kind of make fun of like the more successful it becomes the you  
**Translation:** 

**[4073.80s] English:** know the servers are sweating yes  
**Translation:** 

**[4075.74s] English:** yeah yeah  
**Translation:** 

**[4077.62s] English:** exactly we did a little video of what other  
**Translation:** 

**[4080.00s] English:** of the servers frying eggs and things and um that's right and and and we're gonna have to figure out  
**Translation:** 

**[4085.12s] English:** how to do that um there's a lot of interesting hardware innovations that we do as you know we  
**Translation:** Vocabulary: innovations: 技术创新

**[4089.48s] English:** have our own tpu line and we're looking at like inference only things inference only chips and  
**Translation:** 

**[4094.06s] English:** how we can make those more efficient we're also very interested in building ai systems and we  
**Translation:** 

**[4098.08s] English:** have done the help with energy usage so help um data center energy like for the cooling systems  
**Translation:** 

**[4104.62s] English:** be efficient um grid optimization um and then eventually things like helping with plasma  
**Translation:** Vocabulary: optimization: 优化; plasma: 等离子

**[4111.14s] English:** containment fusion reactors we've done lots of work on that with commonwealth fusion and also  
**Translation:** 

**[4116.10s] English:** one could imagine reactor design um and then material design i think is one of the most exciting  
**Translation:** Vocabulary: containment: 包容

**[4121.26s] English:** new types of solar material solar panel material super room temperature superconductors has always  
**Translation:** 

**[4126.40s] English:** been on my list of dream breakthroughs and um optimal batteries and i think a solution to any  
**Translation:** Vocabulary: breakthroughs: 重大突破; optimal: 最佳的; superconductors: 超导体

**[4132.22s] English:** you know one of those things would be absolutely revolutionary  
**Translation:** 

**[4134.62s] English:** for you know climate and energy usage and we're probably close you know and again in the next  
**Translation:** 

**[4140.76s] English:** five years to having ai systems that can materially help with those problems if you were to bet sorry  
**Translation:** 

**[4146.46s] English:** for the ridiculous question yeah what what is the main source of energy in like 20 30 40 years  
**Translation:** Vocabulary: materially: 实质上

**[4153.32s] English:** do you think it's going to be nuclear fusion i think fusion and solar are the two that i i would  
**Translation:** 

**[4159.02s] English:** bet on um solar i mean you know it's the fusion reactor in the sky of course and i think  
**Translation:** 

**[4164.52s] English:** you know i think it's going to be nuclear fusion and i think it's going to be nuclear fusion  
**Translation:** 

**[4164.60s] English:** and i think it's going to be nuclear fusion and i think it's going to be nuclear fusion and i think  
**Translation:** 

**[4164.62s] English:** really the problem there is is is batteries and transmission so you know as well as more  
**Translation:** 

**[4169.74s] English:** efficient more and more efficient solar material perhaps eventually you know in space you know  
**Translation:** 

**[4173.98s] English:** these kind of dyson sphere type ideas and fusion i think is definitely doable seems uh if we have  
**Translation:** 

**[4181.50s] English:** the right design of reactor and we can control the plasma and uh fast enough and so on and i think  
**Translation:** Vocabulary: doable: 可行; dyson: 迪森

**[4188.14s] English:** both of those things will actually get solved so we'll probably have at least those are probably  
**Translation:** 

**[4191.98s] English:** the two primary sources of renewable energy so i think it's going to be a really interesting  
**Translation:** 

**[4194.60s] English:** and i think it's going to be a really interesting and i think it's going to be a really interesting  
**Translation:** 

**[4195.10s] English:** almost free or perhaps free energy what a time to be alive if i  
**Translation:** 

**[4200.00s] English:** traveled into the future with you a hundred years from now how much would you be surprised if we've  
**Translation:** 

**[4207.60s] English:** passed a type one kardashev scale civilization i would not be that surprised if there's a like a  
**Translation:** Vocabulary: kardashev: 卡达舍夫文明

**[4214.62s] English:** hundred year time scale from here i mean i think it's pretty clear if we crack the energy problems  
**Translation:** 

**[4219.68s] English:** in one of the ways we've just discussed fusion or or very efficient solar um then if energy is  
**Translation:** 

**[4226.08s] English:** kind of free and renewable and clean um then that solves a whole bunch of other problems so for  
**Translation:** 

**[4232.72s] English:** example the water access problem goes away because you can just use desalination we have the technology  
**Translation:** Vocabulary: desalination: 海水淡化

**[4238.14s] English:** it's just too expensive so only you know fairly wealthy countries like singapore and israel and  
**Translation:** 

**[4243.42s] English:** so on like actually use it but but if it was uh cheap then every then you know all countries that  
**Translation:** 

**[4248.48s] English:** have a coast could but also you'd have unlimited rocket fuel you could just separate sea water out  
**Translation:** 

**[4253.24s] English:** into hydrogen and oxygen using energy and that's the kind of thing that we're talking about  
**Translation:** 

**[4256.08s] English:** that's rocket fuel so uh combined with you know elon's amazing self-landing rockets then it could  
**Translation:** 

**[4263.02s] English:** be like you sort of like a bus service to to space so that opens up you know incredible new resources  
**Translation:** 

**[4269.12s] English:** and domains uh asteroid mining i think will become a thing and maximum human flourishing to the stars  
**Translation:** 

**[4274.72s] English:** like that's what i uh dream about as well as like carl sagan's sort of idea of bringing consciousness  
**Translation:** Vocabulary: asteroid: 小行星; flourishing: 繁荣

**[4279.80s] English:** to the universe waking up the universe and i think human civilization will do that in the full sense  
**Translation:** 

**[4285.20s] English:** of time if we get  
**Translation:** 

**[4286.08s] English:** ai right and uh and and and crack some of these problems with it yeah i wonder what it would look  
**Translation:** 

**[4291.68s] English:** like if you just a tourist flying through space you would probably notice earth because if you  
**Translation:** 

**[4298.22s] English:** solve the energy problem you would see a lot of space rockets probably so it would be like traffic  
**Translation:** 

**[4303.28s] English:** here in london but in space yes it's just a lot of rockets yes and then you would probably see  
**Translation:** 

**[4310.22s] English:** floating in space some kind of source of energy like solar yeah potentially so earth would just  
**Translation:** 

**[4316.08s] English:** look more on the surface more um technological  
**Translation:** 

**[4320.00s] English:** and then then you would use the power of that energy then to preserve the natural  
**Translation:** 

**[4324.92s] English:** yes like the rainforest and all that stuff because for the first time in in human history we wouldn't  
**Translation:** Vocabulary: rainforest: 热带雨林

**[4331.08s] English:** be uh resource constrained and i think that could be amazing new era for humanity where it's not  
**Translation:** 

**[4338.46s] English:** zero sum right i have this land you don't have it or if we take you know if the tigers have their  
**Translation:** 

**[4344.30s] English:** forest then the the local villagers can't what are they going to use i i think that this will  
**Translation:** 

**[4349.88s] English:** help a lot no it won't solve all problems because there's still other human uh foibles that will  
**Translation:** Vocabulary: foibles: 缺点; villagers: 村民

**[4355.00s] English:** will will still exist but it will at least remove one i think one of the big vectors which is  
**Translation:** 

**[4359.90s] English:** scarcity of resources you know including land and more materials and energy and um you know we  
**Translation:** Vocabulary: scarcity: 资源匮乏

**[4366.54s] English:** should be i sometimes call it like and others call it about this kind of radical abundance era  
**Translation:** 

**[4370.12s] English:** where um there's plenty of resources to go around of course the next big  
**Translation:** 

**[4374.22s] English:** question is what is the next big question and the next big question is what is the next big  
**Translation:** 

**[4374.28s] English:** is making sure that that's fairly you know shared fairly uh and everyone in society benefits from  
**Translation:** 

**[4380.40s] English:** that so there is something about human nature where i go you know it's like borat like my  
**Translation:** 

**[4386.72s] English:** neighbor like i like you start trouble we we do start conflicts and that's why games throughout  
**Translation:** 

**[4395.30s] English:** as i'm learning actually more and more even in ancient history serve the purpose of pushing  
**Translation:** 

**[4400.36s] English:** people away from war actually hot war so maybe  
**Translation:** 

**[4404.20s] English:** we can figure out increasingly sophisticated video games that pull us they they give us that  
**Translation:** 

**[4410.14s] English:** uh that scratch the itch of like conflict whatever that is about about us the human nature and then  
**Translation:** Vocabulary: sophisticated: 复杂高级

**[4418.84s] English:** avoid the actual hot wars that would come with increasingly sophisticated technologies because  
**Translation:** 

**[4426.28s] English:** we're now we've long past the stage where the weapons we're able to create can actually just  
**Translation:** 

**[4431.48s] English:** destroy all of human civilization so it's no longer  
**Translation:** 

**[4434.20s] English:** um that's no longer a great way to uh start  
**Translation:** 

**[4439.88s] English:** sharing  
**Translation:** 

**[4440.00s] English:** it with your neighbor it's better to play a game of chess or football or football yeah yeah and i  
**Translation:** 

**[4445.44s] English:** think i mean i think that's what my modern sport is so and i love football watching it and and i  
**Translation:** 

**[4450.58s] English:** just feel like uh and i used to play it a lot as well and it's it's it's it's it's very visceral  
**Translation:** Vocabulary: visceral: 直觉的

**[4456.36s] English:** and it's tribal and i think it does channel a lot of those energies into uh which i think is a kind  
**Translation:** 

**[4461.58s] English:** of human need to belong to some some group and um but into a into a into a fun way a healthy way and  
**Translation:** Vocabulary: energies: 能量; tribal: 部落的

**[4469.88s] English:** and a not and not destructive way kind of constructive uh thing and i think going back  
**Translation:** 

**[4474.60s] English:** to games again is i think they're originally why they're so great as well for kids to play  
**Translation:** 

**[4478.52s] English:** things like chess is they're great little microcosm simulations of the world they're  
**Translation:** 

**[4482.76s] English:** simulations of the world too they're simplified versions of some real world situation whether  
**Translation:** 

**[4486.36s] English:** it's poker or or go or chess different aspects or diplomacy different aspects of of the real world  
**Translation:** 

**[4492.92s] English:** and allows you to practice at them too and and because you know how many times do you get to  
**Translation:** Vocabulary: diplomacy: 外交艺术; poker: 纸牌游戏

**[4498.32s] English:** practice a massive decision moment  
**Translation:** 

**[4499.88s] English:** in your life you know what job to take what university go to you know you get maybe i don't  
**Translation:** 

**[4504.42s] English:** know a dozen or so key decisions one has to make and you've got to make those as best as you can  
**Translation:** 

**[4509.12s] English:** and games is a kind of safe environment repeatable environment where you can get better  
**Translation:** 

**[4514.02s] English:** at your decision making process um and it maybe has this additional benefit of channeling some  
**Translation:** 

**[4519.88s] English:** energies into uh into more creative and constructive pursuits well i think it's also  
**Translation:** Vocabulary: channeling: 引导; pursuits: 追求

**[4524.98s] English:** really important to practice um losing and winning right like losing  
**Translation:** 

**[4529.88s] English:** is a really you know that's why i love games that's why i love even um things like uh brazilian  
**Translation:** 

**[4534.62s] English:** jiu-jitsu yeah where you can get your ass kicked in a safe environment over and over it reminds you  
**Translation:** 

**[4540.46s] English:** about the way about physics about the way the world works about sometimes you lose sometimes  
**Translation:** 

**[4545.74s] English:** you win you can still be friends with everybody yeah that that feeling of losing i mean it's a  
**Translation:** 

**[4552.28s] English:** weird one for us humans to like really like make sense of like that's just part of life that is a  
**Translation:** 

**[4558.24s] English:** fundamental part of life is losing  
**Translation:** 

**[4559.88s] English:** you  
**Translation:** 

**[4560.00s] English:** Yeah. And I think the martial arts, as I understand it, but also in things like light  
**Translation:** 

**[4563.68s] English:** chess, at least the way I took it, it's a lot to do with self-improvement, self-knowledge,  
**Translation:** Vocabulary: martial: 武术

**[4568.66s] English:** you know, that, okay, so I did this thing. It's not about really being the other person.  
**Translation:** 

**[4573.50s] English:** It's about maximizing your own potential. If you do it in a healthy way, you learn to use  
**Translation:** Vocabulary: maximizing: 发挥最大潜能

**[4578.36s] English:** victory and losses in a way. Don't get carried away with victory and think you're just the best  
**Translation:** 

**[4583.94s] English:** in the world. And the losses keep you humble and always knowing there's always something more to  
**Translation:** 

**[4589.10s] English:** learn. There's always a bigger expert that you can mentor you. You know, I think you learn that  
**Translation:** 

**[4593.52s] English:** I'm pretty sure in martial arts. And, and, and I think that's also the way that at least I was  
**Translation:** 

**[4598.84s] English:** trained in chess. And so in the same way, and it can be very hardcore and very important. And of  
**Translation:** 

**[4603.44s] English:** course you want to win, but you also need to learn how to deal with setbacks in a, in a healthy way  
**Translation:** Vocabulary: hardcore: 极其认真; setbacks: 挫折

**[4608.60s] English:** that, and, and, and, and why are that, that feeling that you have when you lose something  
**Translation:** 

**[4612.78s] English:** into a constructive thing of next time, I'm going to improve this, right. Or get better at this.  
**Translation:** 

**[4617.72s] English:** There is something,  
**Translation:** 

**[4619.10s] English:** there's a source of happiness, a source of meaning that improvements that it's not about  
**Translation:** 

**[4623.00s] English:** the winning or losing. Yeah. It's the mastery. Yeah. There's nothing more satisfying in a way  
**Translation:** 

**[4627.12s] English:** is like, Oh wow, this thing I couldn't do before now I can. And, and, and again, games and physical  
**Translation:** 

**[4632.86s] English:** sports and mental sports, their way, their ways of measuring they're beautiful because you can  
**Translation:** 

**[4637.18s] English:** measure that, that progress. Yeah. I mean, there's something about, I guess why I love role-playing  
**Translation:** 

**[4641.84s] English:** games. Like the, uh, number go up of like on the skill tree, like literally that is a source of  
**Translation:** 

**[4648.00s] English:** meaning for us humans.  
**Translation:** 

**[4649.10s] English:** Yeah. We're quite, we're, we're quite addicted to this sort of, yeah, these numbers going up and,  
**Translation:** 

**[4653.74s] English:** uh, and, and, and maybe that's why we made games like that because obviously that is something  
**Translation:** Vocabulary: addicted: 上瘾

**[4658.46s] English:** we're, we're, we're hill climbing systems ourselves. Right. Yeah. It would be quite sad if we didn't  
**Translation:** 

**[4663.66s] English:** have any mechanism, but we do this everywhere, right. Where we just have this thing that  
**Translation:** 

**[4670.70s] English:** I don't want to dismiss that. That is a source of deep meaning for us humans.  
**Translation:** 

**[4675.02s] English:** So one of the incredible stories on the business, on the leadership side is, uh,  
**Translation:** 

**[4679.10s] English:** what Google  
**Translation:** 

**[4680.00s] English:** has done over the past year. So I think it's fair to say that Google was losing on the LLM product  
**Translation:** 

**[4687.44s] English:** side a year ago with Gemini 1.5. And now it's winning with Gemini 2.5. And you took the helm  
**Translation:** 

**[4694.04s] English:** and you led this effort. What did it take to go from, let's say, quote unquote, losing to quote  
**Translation:** Vocabulary: gemini: 双子座; unquote: 引用结束

**[4699.08s] English:** unquote, winning in the span of a year? Yeah, well, firstly, it's absolutely incredible team  
**Translation:** 

**[4704.68s] English:** that we have, you know, led by Corey and Jeff Dean and and Oriol and the amazing team we have  
**Translation:** Vocabulary: corey: 科里

**[4710.26s] English:** on Gemini. Absolutely world class. So you can't do it without the best talent. And of course,  
**Translation:** 

**[4717.10s] English:** you have you know, we have a lot of great compute as well. But then it's the research culture we  
**Translation:** 

**[4721.84s] English:** created. Right. And basically coming together, both different groups in Google, you know,  
**Translation:** 

**[4727.52s] English:** there was Google Brain, world class team and and then the old DeepMind and pulling together all  
**Translation:** 

**[4732.50s] English:** the best people and the best ideas.  
**Translation:** 

**[4734.68s] English:** And gathering around to make the absolute greatest system we could. And it was been hard. But we're  
**Translation:** 

**[4741.98s] English:** all very competitive. And we, you know, love research. This is so fun to do. And we you know,  
**Translation:** 

**[4749.20s] English:** it's great to see our trajectory wasn't a given. But we're very pleased with the where we are in  
**Translation:** Vocabulary: trajectory: 发展轨迹

**[4754.86s] English:** the rate of progress is the most important thing. So if you look at where we've come to from two  
**Translation:** 

**[4759.46s] English:** years ago, to one year ago to now, you know, I think our we call it relentless progress,  
**Translation:** Vocabulary: relentless: 坚持不懈

**[4764.68s] English:** along with relentless shipping of that progress is being very successful. And, you know, it's  
**Translation:** 

**[4770.68s] English:** unbelievably competitive, the whole space, the whole AI space, with some of the greatest  
**Translation:** Vocabulary: unbelievably: 难以置信地

**[4775.76s] English:** entrepreneurs and leaders, and companies in the world, all competing now, because everyone's  
**Translation:** 

**[4781.30s] English:** realized how important AI is. And it's very, you know, been pleasing for us to see that progress.  
**Translation:** Vocabulary: entrepreneurs: 企业家

**[4787.42s] English:** You know, Google is a gigantic company. Can you speak to the natural things that happen in that  
**Translation:** 

**[4792.04s] English:** case is the bureaucracy that emerges, like you want to be able to, you know, be able to, you know,  
**Translation:** Vocabulary: bureaucracy: 官僚体系; gigantic: 巨大的

**[4794.66s] English:** be careful, like, you know, like, the natural kind of there's there's me  
**Translation:** 

**[4800.00s] English:** Meetings and there's managers and that, like what, what are some of the challenges from a leadership perspective of breaking through that in order to, like you said, ship, like the number of products, Gemini related products has been shipped over the past year. It's just insane.  
**Translation:** 

**[4813.88s] English:** Right. It is. Yeah, exactly. That's, that's what relentlessness looks like. I think it's, it's a question of like any big company, you know, ends up having a lot of layers of management and things like that is sort of the nature of how it works.  
**Translation:** 

**[4828.72s] English:** Um, but I still operate and I was always operating with old deep mind as a, as a startup still large one, but still as a startup. And that's what we still act like today as with Google deep mind and acting with decisiveness and the energy that you get from the best smaller organizations.  
**Translation:** Vocabulary: decisiveness: 果断; relentlessness: 坚持不懈

**[4846.18s] English:** And we try to get the best of both worlds where we have this incredible billions of users, surfaces, uh, incredible products that we can power up with our AI and our, and our research.  
**Translation:** 

**[4857.54s] English:** Um, and that's amazing.  
**Translation:** 

**[4858.72s] English:** And you can, you know, that's very few places in the world.  
**Translation:** 

**[4860.90s] English:** You can get that, do incredible world-class research on the one hand, and then plug it in and improve billions of people's lives the next day.  
**Translation:** 

**[4867.82s] English:** Uh, that's a pretty amazing combination and we're continually fighting and cutting away bureaucracy to allow the research culture and the relentless shipping culture to flourish.  
**Translation:** 

**[4878.84s] English:** And I think we've got a pretty good balance whilst being responsible with it, you know, as you have to be, uh, as a large company and also, uh, with a number of, you know, uh, huge projects.  
**Translation:** Vocabulary: flourish: 蓬勃发展

**[4888.72s] English:** Uh, so a funny thing you mentioned about like the, the surface with a billion, I, I had a conversation with a guy named, um, brilliant guy, uh, here at the British museum called Irvin Finkel.  
**Translation:** 

**[4899.90s] English:** He's a world expert at Kinea forms, which is a ancient writing on tablets.  
**Translation:** Vocabulary: finkel: 芬克尔; irvin: 伊里文

**[4906.74s] English:** And he doesn't know about Chad GPT or Gemini.  
**Translation:** 

**[4911.24s] English:** He doesn't even know anything about AI, but his first encounter with this AI is AI mode on Google.  
**Translation:** Vocabulary: gemini: 星♂座

**[4917.64s] English:** Yes.  
**Translation:** 

**[4918.12s] English:** He's like,  
**Translation:** 

**[4918.72s] English:** is that what you're talking about?  
**Translation:** 

**[4920.00s] English:** this ai mode and you know it's just it's just a reminder that there's a large part of the world  
**Translation:** 

**[4926.22s] English:** that doesn't know about this ai thing yeah i know it's funny because if you live on uh x and twitter  
**Translation:** 

**[4931.76s] English:** and i mean it's sort of at least my feed it's all ai and and there's certain places where you know  
**Translation:** 

**[4936.32s] English:** in the valley and certain pockets where everyone's just all they're thinking about is ai but a lot of  
**Translation:** 

**[4941.88s] English:** the normal world hasn't hasn't come across it yet but that's a great responsibility to  
**Translation:** 

**[4946.10s] English:** the their first interaction yeah um the the grand scale of the rural india or anywhere across the  
**Translation:** 

**[4953.06s] English:** world right right and we want it to be as good as possible and in a lot of cases it's just under the  
**Translation:** 

**[4957.50s] English:** hood powering making something like maps or search work better and um and it's ideally for a lot of  
**Translation:** 

**[4964.20s] English:** those people should just be seamless it's just new technology that makes their lives more you know  
**Translation:** Vocabulary: seamless: 天衣无缝

**[4968.42s] English:** productive and and and helps them a bunch of folks on the gemini product and engineering teams  
**Translation:** 

**[4973.00s] English:** spoken extremely highly of you on another dimension  
**Translation:** Vocabulary: dimension: 维度

**[4975.88s] English:** that i almost didn't even expect because i kind of think of you as the like deep scientists and  
**Translation:** 

**[4983.00s] English:** caring about these big research scientific questions but they also said you're a great  
**Translation:** 

**[4986.72s] English:** product guy like how to create a thing that a lot of people would use and enjoy using so  
**Translation:** 

**[4992.04s] English:** can you maybe speak to what it takes to create a ai based product that a lot of people don't  
**Translation:** 

**[4998.14s] English:** enjoy using yeah well i mean again that comes back from my game design days where i used to design  
**Translation:** 

**[5002.58s] English:** games for millions of gamers people forget about that  
**Translation:** 

**[5005.88s] English:** i've had experience with cutting edge technology in product that that that is how games was in the  
**Translation:** 

**[5011.00s] English:** 90s and so i love actually the combination of cutting edge research and then being applied  
**Translation:** 

**[5017.56s] English:** in a product and to power a new experience and so um i think it's the same skill really of of you  
**Translation:** 

**[5024.86s] English:** know imagining what it would be like to use it viscerally um and having good taste coming back  
**Translation:** Vocabulary: viscerally: 直觉上

**[5030.44s] English:** to earlier the same thing that's useful in science um i think is is can also be useful in  
**Translation:** 

**[5035.88s] English:** in product design and um i've just had a very  
**Translation:** 

**[5040.00s] English:** you know, always being a sort of multidisciplinary person. So I don't see the boundaries really  
**Translation:** 

**[5044.74s] English:** between, you know, arts and sciences or product and research. It's a continuum for me. I mean,  
**Translation:** Vocabulary: continuum: 连续体; multidisciplinary: 跨学科的

**[5050.48s] English:** I only work on, I like working on products that are cutting edge. I wouldn't be able to, you know,  
**Translation:** 

**[5054.06s] English:** have cutting edge technology under the hood. I wouldn't be excited about them if they were just  
**Translation:** 

**[5058.20s] English:** run-of-the-mill products. So it requires this invention creativity capability.  
**Translation:** 

**[5063.90s] English:** What are some specific things you kind of learned about when you, even on the LLM side,  
**Translation:** Vocabulary: capability: 能力

**[5069.10s] English:** you're interacting with Gemini, like this doesn't feel like the layout, the interface,  
**Translation:** 

**[5075.12s] English:** maybe the trade-off between the latency, like how to present to the user, how long to wait  
**Translation:** Vocabulary: gemini: 双子座; interface: 界面; latency: 延迟; layout: 布局

**[5082.16s] English:** and how that waiting is shown or the reasoning capabilities. There's some interesting things  
**Translation:** 

**[5087.18s] English:** because like you said, it's the very cutting edge. We don't know how to present it correctly. So is  
**Translation:** 

**[5092.98s] English:** there some specific things you've learned? I mean, it's such a fast evolving space.  
**Translation:** 

**[5097.30s] English:** We're evaluating this all the time.  
**Translation:** Vocabulary: evaluating: 评估; evolving: 演变

**[5099.10s] English:** But where we are today is that you want to continually simplify things, whether that's  
**Translation:** 

**[5105.12s] English:** the interface or what you build on top of the model. You kind of want to get out of the way  
**Translation:** Vocabulary: simplify: 简化

**[5110.46s] English:** of the model. The model train is coming down the track and it's improving unbelievably fast. This  
**Translation:** 

**[5115.12s] English:** relentless progress we talked about earlier, you know, you look at 2.5 versus 1.5 and it's just a  
**Translation:** Vocabulary: relentless: 毫不懈怠; unbelievably: 难以置信地

**[5120.08s] English:** gigantic improvement. And we expect that again for the future versions. And so the models are  
**Translation:** 

**[5125.42s] English:** becoming more capable. So you've got the interesting thing about the design space,  
**Translation:** Vocabulary: gigantic: 巨大的

**[5129.10s] English:** in today's world, these AI first products is you've got to design not for what the thing can do  
**Translation:** 

**[5134.40s] English:** today, the technology can do today, but in a year's time. So you actually have to be a very technical  
**Translation:** 

**[5140.06s] English:** product person because you've got to kind of have a good intuition for and feel for, okay, that thing  
**Translation:** 

**[5147.00s] English:** that I'm dreaming about now can't be done today, but is the research track on schedule to basically  
**Translation:** Vocabulary: intuition: 直觉

**[5152.30s] English:** intercept that in six months or a year's time? So you kind of got to intercept where this highly  
**Translation:** 

**[5157.22s] English:** changing technology is going.  
**Translation:** Vocabulary: intercept: 截获

**[5159.10s] English:** As well as the  
**Translation:** 

**[5160.00s] English:** um uh new capabilities are coming online all the time that you didn't realize before that can allow  
**Translation:** 

**[5165.64s] English:** like deep search to work or now we've got video generation what do we do with that um this  
**Translation:** 

**[5171.40s] English:** multimodal stuff you know is it one question i have is is it really going to be the current ui  
**Translation:** Vocabulary: multimodal: 多模态的

**[5177.12s] English:** that we have today these text box chats seems very unlikely give once you think about these  
**Translation:** 

**[5182.26s] English:** super multimodal uh uh systems shouldn't it be something more like minority report where you're  
**Translation:** 

**[5187.46s] English:** you're sort of vibing with it in a in a coat in a kind of collaborative way right it seems very  
**Translation:** 

**[5192.76s] English:** restricted today i think we'll look back on today's interfaces and products and systems as quite  
**Translation:** Vocabulary: collaborative: 合作; interfaces: 接口

**[5198.16s] English:** archaic in maybe in just a couple of years so i think there's a lot of space actually for innovation  
**Translation:** 

**[5204.18s] English:** to happen on the product side as well as the the research side and then we're offline talking about  
**Translation:** Vocabulary: archaic: 古董级的

**[5209.26s] English:** this keyboard is the the open question is how when and how much will we move to audio as the primary  
**Translation:** 

**[5217.46s] English:** with the machines around us versus typing stuff yeah i mean typing is a very low bandwidth way of  
**Translation:** Vocabulary: bandwidth: 传输容量

**[5223.38s] English:** doing even if you're very fast you know typer and i think we're going to have to start utilizing  
**Translation:** 

**[5228.32s] English:** other devices whether that's smart glasses you know audio earbuds um and eventually maybe some  
**Translation:** Vocabulary: typer: 打字者; utilizing: 利用

**[5235.42s] English:** sorts of neural devices where we can increase the the input and the output bandwidth to something  
**Translation:** 

**[5241.24s] English:** uh you know maybe 100x of what is today i think that you know under appreciated art form  
**Translation:** 

**[5247.46s] English:** the interface design but i think you can not unlock the power of the intelligence of a system  
**Translation:** 

**[5253.86s] English:** if you don't have the right interface their interface is really the way you unlock its  
**Translation:** Vocabulary: interface: 用户界面

**[5257.98s] English:** power yeah it's such an interesting question of how to do that yeah so how you would think  
**Translation:** 

**[5263.80s] English:** like getting out of the way is in real art form yes you know it's the sort of thing that i guess  
**Translation:** 

**[5268.98s] English:** steve jobs always talked about right it's simplicity beauty and elegance that we want  
**Translation:** 

**[5273.02s] English:** right and we're not that nobody's there yet in my opinion and that's what i would like  
**Translation:** Vocabulary: elegance: 优雅; simplicity: 简洁

**[5277.46s] English:** to get to again it sort of speaks to like go again  
**Translation:** 

**[5280.00s] English:** right as a game the most elegant beautiful game can you you know that can you make an interface  
**Translation:** 

**[5284.76s] English:** as beautiful as that and actually i think we're going to enter an era of ai generated interfaces  
**Translation:** 

**[5290.02s] English:** that are probably personalized to you so it fits the way that you your aesthetic your feel the way  
**Translation:** Vocabulary: aesthetic: 审美

**[5296.18s] English:** that your brain works and um and and and the ai kind of generates that depending on the task you  
**Translation:** 

**[5302.00s] English:** know that feels like that's probably the direction we'll end up in yeah because some people are power  
**Translation:** 

**[5306.40s] English:** users and they want every single parameter on screen everything and everything based like  
**Translation:** 

**[5310.66s] English:** perhaps me with a keyboard keyboard based navigation i'd like to have shortcuts for  
**Translation:** Vocabulary: navigation: 导航; parameter: 参数; shortcuts: 快捷键

**[5314.68s] English:** everything and some people like the minimalism just hide all of that complexity yeah exactly  
**Translation:** 

**[5319.20s] English:** yeah uh well i'm glad you have a steve jobs mode in you as well this is great einstein most steve  
**Translation:** Vocabulary: complexity: 复杂性; minimalism: 极简主义

**[5325.54s] English:** jobs mode um all right let me try to trick you into answering a question when when will gemini  
**Translation:** 

**[5330.96s] English:** three come out it's a before or after dts6 the world waits for both and what  
**Translation:** Vocabulary: gemini: 双子座

**[5336.38s] English:** does it take to go from 2.5 to 3.0 because it seems like there's been a lot of releases of  
**Translation:** 

**[5344.26s] English:** 2.5 which are already leaps in performance so what what does it even mean to go to a new version  
**Translation:** 

**[5349.76s] English:** is it about performance this is about a completely different flavor of an experience yeah well so  
**Translation:** 

**[5356.74s] English:** the way it works with our different uh version numbers is we you know we try to collect so maybe  
**Translation:** 

**[5362.90s] English:** it takes you know roughly six months or something to  
**Translation:** 

**[5365.90s] English:** to  
**Translation:** 

**[5366.38s] English:** do a new kind of full run and the full productization of a new version and during that  
**Translation:** 

**[5373.10s] English:** time lots of new interesting research iterations and ideas come up and we sort of collect them  
**Translation:** Vocabulary: iterations: 迭代; productization: 产品化

**[5378.82s] English:** all together that you know you could imagine the last six months worth of interesting ideas on the  
**Translation:** 

**[5383.68s] English:** architecture front uh maybe it's on the data front it's like many different possible things  
**Translation:** 

**[5388.98s] English:** and we collect package that all up test which ones are likely to be useful for the next iteration  
**Translation:** 

**[5394.78s] English:** and then bundle that all together and then we sort of collect them all together and then we sort of  
**Translation:** Vocabulary: bundle: 打包; iteration: 迭代

**[5395.90s] English:** do a new kind of full run and the full productization of a new version and during that time lots of new  
**Translation:** 

**[5396.38s] English:** ideas come up and we sort of collect them all together and then we sort of collect them all together and then we start the new you know giant hero training  
**Translation:** 

**[5400.00s] English:** right and and then uh and then of course that gets monitored uh and then at the end then there's the  
**Translation:** 

**[5405.62s] English:** of the pre-training then there's all the post-training there's many different ways of  
**Translation:** 

**[5408.70s] English:** doing that different ways of patching it so there's a whole experiment and phase there which  
**Translation:** 

**[5412.60s] English:** you can also get a lot of gains out and that's where you see the version numbers usually referring  
**Translation:** Vocabulary: patching: 打补丁

**[5416.98s] English:** to the base model the pre-trained model and then the interim versions of 2.5 you know and the  
**Translation:** 

**[5423.14s] English:** different sizes and the different little additions they're often uh patches or post-training ideas  
**Translation:** Vocabulary: interim: 过渡版本

**[5428.86s] English:** that can be done afterwards uh off the same basic architecture and then of course on top of that we  
**Translation:** 

**[5433.82s] English:** also have different sizes pro and flash and flashlight that are often distilled from the  
**Translation:** Vocabulary: distilled: 提炼; flashlight: 手电筒

**[5439.00s] English:** biggest ones you know the flash model from the pro model and that means we have a range of different  
**Translation:** 

**[5444.76s] English:** choices if you are the developer of do you want to prioritize performance or speed right and cost  
**Translation:** 

**[5451.44s] English:** and we like to think of this pareto frontier of of you know on the one hand uh the y-axis is you  
**Translation:** 

**[5457.62s] English:** know like performance  
**Translation:** Vocabulary: frontier: 边界; pareto: 帕累托

**[5458.56s] English:** and then the the x-axis is you know cost or latency and speed uh basically and we we have  
**Translation:** 

**[5465.42s] English:** models that completely define the frontier so whatever your trade-off is that you want as an  
**Translation:** Vocabulary: latency: 延迟

**[5471.00s] English:** individual user or as a as a developer you should find one of our models satisfies that constraint  
**Translation:** 

**[5476.74s] English:** so behind the version changes there is a big hero run yes and then there's uh just an insane  
**Translation:** Vocabulary: constraint: 限制

**[5485.44s] English:** complexity of productization  
**Translation:** 

**[5488.56s] English:** then there's the distillation of the different sizes along that parade or front  
**Translation:** Vocabulary: complexity: 复杂性; distillation: 提炼

**[5493.30s] English:** and then as each step you take you realize there might be a cool product  
**Translation:** 

**[5498.16s] English:** there's side quests yes exactly but and then you also don't want to take too many side quests  
**Translation:** 

**[5503.08s] English:** because then you have a million versions of a million products yes it's very unclear yeah but  
**Translation:** 

**[5507.64s] English:** you also get super excited because it's super cool yeah like how does even you look at vl's  
**Translation:** 

**[5511.88s] English:** very cool how does it fit into the bigger thing exactly exactly and then you constantly  
**Translation:** 

**[5518.56s] English:** you can see that they are not just converging upstream  
**Translation:** Vocabulary: converging: 汇聚

**[5520.00s] English:** We call it, you know, ideas from the, from the product surfaces or, or, or from the post  
**Translation:** 

**[5525.02s] English:** training and, and even further downstream than that, you, you kind of upstream that  
**Translation:** 

**[5528.94s] English:** into the, the core model training for the next run, right?  
**Translation:** 

**[5532.36s] English:** So then the main model, the main Gemini track becomes more and more general and eventually,  
**Translation:** Vocabulary: gemini: Gemini模型

**[5537.42s] English:** you know, AGI.  
**Translation:** 

**[5539.86s] English:** One hero run at a time.  
**Translation:** 

**[5541.30s] English:** Yes, exactly.  
**Translation:** 

**[5542.06s] English:** A few hero runs later.  
**Translation:** 

**[5543.58s] English:** Yeah.  
**Translation:** 

**[5544.06s] English:** So sometimes when you release these new versions or every version really,  
**Translation:** 

**[5550.00s] English:** are benchmarks productive or counterproductive for showing the performance of a model?  
**Translation:** 

**[5555.88s] English:** You need them and, and, but it's important that you don't overfit to them, right?  
**Translation:** Vocabulary: benchmarks: 参考标准; counterproductive: 适得其反

**[5559.94s] English:** So there shouldn't be the end with a be all and end all.  
**Translation:** 

**[5562.00s] English:** So there's, there's LM Arena or used to be called Elemsys.  
**Translation:** 

**[5565.10s] English:** That's one of them that turned out sort of organically to be one of the, the main ways  
**Translation:** 

**[5569.02s] English:** people like to test these systems, at least the chatbots.  
**Translation:** Vocabulary: chatbots: 聊天机器人; organically: 自然地

**[5571.92s] English:** Obviously there's loads of academic benchmarks on from, from the test mathematics and coding  
**Translation:** 

**[5577.30s] English:** ability, general language ability.  
**Translation:** 

**[5580.00s] English:** Science ability and so on.  
**Translation:** 

**[5581.80s] English:** And then we have our own internal benchmarks that we care about.  
**Translation:** 

**[5584.74s] English:** It's a kind of multi-objective, you know, optimization problem, right?  
**Translation:** 

**[5588.84s] English:** You want, you don't want to be good at just one thing.  
**Translation:** Vocabulary: optimization: 最优化

**[5590.96s] English:** We're trying to build general systems that are good across the board.  
**Translation:** 

**[5594.12s] English:** And you try and make no regret improvements.  
**Translation:** 

**[5597.44s] English:** So where you improve in like, you know, coding but it doesn't reduce your performance in other areas.  
**Translation:** 

**[5603.64s] English:** Right?  
**Translation:** 

**[5603.88s] English:** So that's the hard part.  
**Translation:** 

**[5604.76s] English:** Cause you, you can, of course you could put more coding data in, or you could put more,  
**Translation:** 

**[5609.22s] English:** um,  
**Translation:** 

**[5610.00s] English:** I don't know, gaming data in, but then does it make worse your language, uh, system or,  
**Translation:** 

**[5615.40s] English:** or, uh, in your translation systems and other things that you care about.  
**Translation:** 

**[5619.12s] English:** So it's, you've got to kind of continually monitor this increasingly larger and larger  
**Translation:** 

**[5624.18s] English:** suite of, of benchmarks.  
**Translation:** 

**[5625.78s] English:** And also there's, uh, when you stick them into products, these models, you also care  
**Translation:** 

**[5629.98s] English:** about the direct usage and the direct stats and the signals that you're getting from the  
**Translation:** 

**[5635.48s] English:** end users, whether they're coders or, or, or the average person using, using the chat  
**Translation:** 

**[5639.56s] English:** interface.  
**Translation:** 

**[5640.00s] English:** Yeah, because ultimately you want to measure the usefulness, but it's so hard to convert that into a number.  
**Translation:** Vocabulary: interface: 界面

**[5645.14s] English:** Right.  
**Translation:** 

**[5645.48s] English:** It's really vibe-based benchmarks across a large number of users, and it's hard to know.  
**Translation:** 

**[5651.60s] English:** And it would be just terrifying to me to, you know you have a much smarter model, but it's just something vibe-based.  
**Translation:** 

**[5659.52s] English:** It's not quite working.  
**Translation:** Vocabulary: terrifying: 令人恐惧

**[5661.22s] English:** And everything you just said, it has to be smart and useful across so many domains.  
**Translation:** 

**[5668.64s] English:** So you get super excited because it's all of a sudden solving programming problems you've never been able to solve before, but now it's crappy poetry or something.  
**Translation:** Vocabulary: crappy: 糟糕的诗

**[5678.58s] English:** And it's just, I don't know, that's stressful.  
**Translation:** 

**[5680.58s] English:** That's so difficult to balance.  
**Translation:** 

**[5684.06s] English:** And because you can't really trust the benchmarks, you really have to trust the end users.  
**Translation:** 

**[5687.90s] English:** Yeah.  
**Translation:** Vocabulary: benchmarks: 参考标准

**[5688.48s] English:** And then other things that are even more esoteric come into play, like, you know, the style of the persona of the system, you know, how it, you know, is it verbose?  
**Translation:** 

**[5698.64s] English:** Is it succinct?  
**Translation:** Vocabulary: esoteric: 深奥; succinct: 简洁; verbose: 啰嗦

**[5699.92s] English:** Is it humorous?  
**Translation:** 

**[5701.40s] English:** You know, and different people like different things.  
**Translation:** 

**[5703.82s] English:** So, you know, it's very interesting.  
**Translation:** 

**[5705.98s] English:** It's almost like cutting edge part of psychology research or personality research.  
**Translation:** 

**[5710.82s] English:** You know, I used to do that in my PhD, like five factor personality.  
**Translation:** 

**[5714.24s] English:** What do we actually want our systems to be like?  
**Translation:** 

**[5716.46s] English:** And different people will like different things as well.  
**Translation:** 

**[5718.96s] English:** So these are all just sort of new problems in product space that I don't think have ever really been tackled before, but we're going to sort of rapidly have to deal with now.  
**Translation:** 

**[5727.62s] English:** I think it's a super interesting topic.  
**Translation:** 

**[5728.58s] English:** Super fascinating space, developing the character of the thing.  
**Translation:** 

**[5731.40s] English:** Yeah.  
**Translation:** 

**[5731.84s] English:** And in so doing, it puts a mirror to ourselves.  
**Translation:** 

**[5734.88s] English:** What are the kind of things that we like?  
**Translation:** 

**[5738.12s] English:** Because prompt engineering allows you to control a lot of those elements, but can the product make it easier for you to control the different flavors of those experiences, the different characters that you interact with?  
**Translation:** 

**[5751.82s] English:** Yeah, exactly.  
**Translation:** 

**[5753.02s] English:** So what's the probability of Google DeepMind winning?  
**Translation:** 

**[5756.44s] English:** Well, I don't see it as sort of winning.  
**Translation:** 

**[5757.84s] English:** I mean, I think we need to think.  
**Translation:** 

**[5760.00s] English:** winning is the wrong way to look at it given how important and consequential what it is we're  
**Translation:** 

**[5764.20s] English:** building so funnily enough i don't i try not to view it like a game or competition even though  
**Translation:** Vocabulary: consequential: 有重大影响的

**[5769.02s] English:** that's a lot of my mindset it's it's about in my view all of us have those of us at the leading  
**Translation:** 

**[5774.54s] English:** edge have a responsibility to um steward this unbelievable technology that could be used for  
**Translation:** Vocabulary: mindset: 思维模式; steward: 管理者

**[5780.40s] English:** incredible good but also has risks um steward it safely into the world for the benefit of humanity  
**Translation:** 

**[5786.28s] English:** that's always um what i've um uh i dreamed about and what we've always tried to do and i hope  
**Translation:** 

**[5792.66s] English:** that's what eventually the community maybe the international community will rally around when  
**Translation:** 

**[5797.16s] English:** it becomes obvious that as we get closer and closer to to agi that um that's what's needed  
**Translation:** 

**[5802.42s] English:** i agree with you i think that's beautifully put you've said that um you talk to and are on good  
**Translation:** 

**[5808.52s] English:** terms with the leads of some of these uh labs as the competition heats up uh how hard is it to  
**Translation:** 

**[5816.00s] English:** maintain  
**Translation:** 

**[5816.28s] English:** sort of those relationships it's been okay so far i try to pride myself in being uh collaborative  
**Translation:** Vocabulary: collaborative: 合作的

**[5823.38s] English:** i'm a collaborative person research is a collaborative endeavor science is a collaborative  
**Translation:** 

**[5827.58s] English:** endeavor right it's all good for humanity in the end if you cure incredible you know  
**Translation:** Vocabulary: endeavor: 努力

**[5831.30s] English:** terrible diseases and you come with an incredible cure this is net win for humanity and the same  
**Translation:** 

**[5837.20s] English:** with energy all of the things that i'm interested in in in helping solve with ai so i just want that  
**Translation:** 

**[5842.84s] English:** technology to exist in the world and be used for the right things  
**Translation:** 

**[5845.62s] English:** and  
**Translation:** 

**[5846.28s] English:** and and and the the kind of the benefits of that the productivity benefits of that  
**Translation:** 

**[5850.36s] English:** being shared for every the benefit of everyone so i try to maintain good relations with all the  
**Translation:** 

**[5855.78s] English:** leading lab uh people they have very interesting characters many of them as you might expect  
**Translation:** 

**[5859.98s] English:** um but yeah i'm on good terms i i hope with pretty much all of them and uh i think that's  
**Translation:** 

**[5865.60s] English:** going to be important when when things get even more serious than they are now uh that there are  
**Translation:** 

**[5870.78s] English:** those communication channels and uh that's what will facilitate uh cooperation and uh you know  
**Translation:** Vocabulary: facilitate: 促进

**[5876.28s] English:** collaboration or collaboration if that's what is required especially on things like safety  
**Translation:** 

**[5880.00s] English:** yeah i hope there's some collaboration on stuff that's uh sort of less high stakes and in so doing  
**Translation:** 

**[5886.86s] English:** serves as a mechanism for maintaining friendships and relationships so for example i think the  
**Translation:** 

**[5891.12s] English:** internet would love it if you and elon somehow collaborate on creating a video game that kind  
**Translation:** Vocabulary: collaborate: 合作

**[5895.14s] English:** of thing that i think that enables camaraderie and good terms and also you two are legit gamers  
**Translation:** 

**[5901.40s] English:** so it's just fun to yeah fun yeah that would be awesome and we've talked about that in the past  
**Translation:** Vocabulary: camaraderie: 同伴情谊; legit: 真正的

**[5905.68s] English:** and it may be a cool thing that that you know we can do and i agree with you it'd be nice to have  
**Translation:** 

**[5909.64s] English:** um kind of side projects in a way where where one can just lean into the collaboration aspect of it  
**Translation:** 

**[5917.22s] English:** and it's a sort of uh win-win for both sides and it's um and it kind of builds up that that that  
**Translation:** 

**[5923.44s] English:** uh collaborative muscle i see the scientific endeavor as that kind of side project for  
**Translation:** 

**[5928.44s] English:** humanity yeah and i think deep google deep mind has been really pushing that i would love it if  
**Translation:** 

**[5934.20s] English:** to see other labs do more scientific stuff and then collaborate because it just seems like easier  
**Translation:** 

**[5939.02s] English:** to collaborate  
**Translation:** 

**[5939.62s] English:** and the big scientific questions i agree and i would love to see a lot of people all of the  
**Translation:** 

**[5943.94s] English:** other labs talk about science but i think we're really the only ones using it for science and  
**Translation:** 

**[5948.08s] English:** doing that and that's why projects like alpha fold are so important to me and i think to our  
**Translation:** Vocabulary: alpha: 阿尔法

**[5952.98s] English:** mission is to show uh how ai can this you know be clearly used in a very concrete way for the  
**Translation:** 

**[5959.64s] English:** benefit of humanity and and also we spun out companies like isomorphic off the back of alpha  
**Translation:** Vocabulary: isomorphic: 同构的

**[5963.96s] English:** fold to do drug discovery and it's going really well and build sort of you know you can think of  
**Translation:** 

**[5968.84s] English:** build additional alpha fold type type systems to go into chemistry space to help accelerate drug  
**Translation:** Vocabulary: accelerate: 加速

**[5974.12s] English:** design and the examples i think we need to show and society needs to understand where ai can bring  
**Translation:** 

**[5980.48s] English:** these huge benefits well from the bottom of my heart thank you for pushing the scientific efforts  
**Translation:** 

**[5985.94s] English:** forward with rigor with fun with humility all of it i just love to see and still talking about p  
**Translation:** 

**[5991.56s] English:** equals mp i mean it's just incredible so i love it uh there there's been uh seemingly a war for the  
**Translation:** Vocabulary: humility: 谦逊; rigor: 严谨

**[5998.84s] English:** word talent some of it is  
**Translation:** 

**[6000.00s] English:** I don't know  
**Translation:** 

**[6001.38s] English:** What do you think about meta buying up talent with huge salaries and and the heating up of this battle?  
**Translation:** 

**[6008.06s] English:** For talent and I should say that I think a lot of people see deep mine is a really great place to do  
**Translation:** Vocabulary: salaries: 高薪

**[6014.18s] English:** Cutting-edge work for the reasons that you've outlined is like there's this  
**Translation:** 

**[6018.88s] English:** Vibrant scientific culture. Yeah. Well look, of course, you know, there's a strategy that that meta is taking right now  
**Translation:** Vocabulary: outlined: 阐述; vibrant: 活跃

**[6025.74s] English:** I think that from my perspective at least I think the people that are  
**Translation:** 

**[6030.32s] English:** real  
**Translation:** 

**[6031.54s] English:** Believers in the mission of AGI and what it can do and understand the real consequences both good and bad from that and what's what?  
**Translation:** 

**[6037.52s] English:** That responsibility entails. I think they're mostly doing it to be like myself to be on the frontier of that research  
**Translation:** Vocabulary: believers: 信仰者; entails: 包含; frontier: 前沿

**[6044.18s] English:** So, you know, they can help influence the way that goes and steward that technology safely into the world and you know  
**Translation:** 

**[6051.14s] English:** Meta right now are not at the frontier. Maybe they'll they'll manage to get back on there and  
**Translation:** Vocabulary: steward: 监护

**[6055.66s] English:** You know  
**Translation:** 

**[6056.30s] English:** It's probably rational what they're doing from their perspective because they're behind and they need to do something  
**Translation:** 

**[6060.26s] English:** But I think there's more important things than just money  
**Translation:** 

**[6063.80s] English:** Of course one has to pay, you know people their market rates and all of these things and that continues to go up  
**Translation:** 

**[6069.24s] English:** But as problem and and I was expecting this because more and more people are finally  
**Translation:** 

**[6074.80s] English:** Realizing leaders of companies what I've always known for 30 plus years now, which is that AGI is the most important technology  
**Translation:** 

**[6081.64s] English:** Probably there's ever going to be invented. So in some senses, it's rational to be doing that  
**Translation:** 

**[6086.26s] English:** But I also think there's a much bigger question  
**Translation:** 

**[6088.98s] English:** I mean people in a  
**Translation:** 

**[6089.92s] English:** ai these days are very well paid you know i remember when we were starting out back in 2010  
**Translation:** 

**[6095.08s] English:** you know i didn't even pay myself a couple of years because it wasn't enough money we couldn't  
**Translation:** 

**[6098.86s] English:** raise any money and these days interns are being paid you know the amount that we raised as our  
**Translation:** Vocabulary: interns: 实习生

**[6103.58s] English:** first entire seat round so it's pretty funny and i remember the days where we used i used to have to  
**Translation:** 

**[6108.46s] English:** to work for free and almost pay my own way to do an internship right now it's all the other way  
**Translation:** 

**[6113.02s] English:** around but that's just how it is it's the new world and um but i think that you know we've been  
**Translation:** 

**[6118.46s] English:** discussing like what happens post  
**Translation:** 

**[6120.00s] English:** agi and energy systems are solved and so on what is even money going to mean so i think uh you know  
**Translation:** 

**[6126.46s] English:** in the economy and and we're going to have much bigger issues to work through and how does the  
**Translation:** 

**[6130.44s] English:** economy function in that world and companies so i think you know it's a little bit uh of a side  
**Translation:** 

**[6135.04s] English:** issue about uh salaries and things like that today yeah when you're facing such gigantic  
**Translation:** Vocabulary: gigantic: 巨大的; salaries: 工资

**[6141.14s] English:** consequences and and gigantic fascinating scientific questions which may be only a few  
**Translation:** 

**[6146.22s] English:** years away so so on the practicals or pragmatic sense uh if we zoom in on jobs we can look at  
**Translation:** Vocabulary: practicals: 实践; pragmatic: 实用

**[6153.08s] English:** programmers because it seems like ai systems are currently doing incredibly well at programming  
**Translation:** 

**[6157.96s] English:** and increasingly so so a lot of people that uh program for a living love programming are worried  
**Translation:** 

**[6164.92s] English:** they will lose their jobs how worried should they be do you think and what's the right way to  
**Translation:** 

**[6170.84s] English:** uh sort of adjust to the new reality and ensure that you survive and thrive as  
**Translation:** 

**[6176.14s] English:** a human being  
**Translation:** 

**[6176.22s] English:** in the programming world well it's interesting that programming and it's again counterintuitive  
**Translation:** Vocabulary: counterintuitive: 违反直觉的

**[6181.40s] English:** to what we thought uh years ago maybe that some of the skills that we think of as harder skills  
**Translation:** 

**[6186.52s] English:** are turned out maybe to be the easier ones for various reasons but you know coding and math  
**Translation:** 

**[6190.80s] English:** because you can create a lot of synthetic data and verify if that data is correct so because of  
**Translation:** 

**[6196.00s] English:** that nature of that it's easier to make things like synthetic data to train from um it's also  
**Translation:** Vocabulary: synthetic: 合成的; verify: 验证

**[6200.84s] English:** an area of course we're all interested in because as programmers right to help us and get faster at  
**Translation:** 

**[6205.84s] English:** it and more productive and more productive and more productive and more productive and more  
**Translation:** Vocabulary: programmers: 程序员

**[6206.20s] English:** productive so i think the for the next era like the next five ten years i think what we're going to  
**Translation:** 

**[6211.26s] English:** find is people who are kind of embrace these technologies become almost at one with them  
**Translation:** 

**[6217.02s] English:** um whether that's in the creative industries or the technical industries will become sort of  
**Translation:** 

**[6221.28s] English:** superhumanly productive i think so the great programmers will be even better but there'll  
**Translation:** 

**[6225.78s] English:** be even 10x even what they are today and because there you'll be able to use their skills to  
**Translation:** 

**[6230.16s] English:** utilize that the tools to the maximum uh you know exploit them to the maximum  
**Translation:** 

**[6236.20s] English:** and um so i think that's what we're going to see in the next domain  
**Translation:** 

**[6240.00s] English:** So that's going to cause quite a lot of change, right?  
**Translation:** 

**[6242.50s] English:** And so that's coming.  
**Translation:** 

**[6243.54s] English:** A lot of people benefit from that.  
**Translation:** 

**[6245.24s] English:** So I think one example of that is if coding becomes easier,  
**Translation:** 

**[6249.24s] English:** it becomes available to many more creatives to do more.  
**Translation:** Vocabulary: creatives: 创意人士

**[6254.00s] English:** But I think the top programmers will still have huge advantages  
**Translation:** 

**[6257.50s] English:** in terms of specifying, going back to specifying  
**Translation:** Vocabulary: specifying: 指定说明

**[6260.24s] English:** what the architecture should be, the question should be,  
**Translation:** 

**[6262.74s] English:** how to guide these coding assistants in a way that's useful,  
**Translation:** 

**[6267.68s] English:** or check whether the code they produce is good.  
**Translation:** 

**[6270.82s] English:** So I think there's plenty of headroom there for the foreseeable next few years.  
**Translation:** Vocabulary: foreseeable: 可预见的; headroom: 余地

**[6276.74s] English:** So I think there's several interesting things there.  
**Translation:** 

**[6278.78s] English:** One is there's a lot of imperative to just get better and better consistently  
**Translation:** Vocabulary: imperative: 迫切需要

**[6283.58s] English:** of using these tools.  
**Translation:** 

**[6285.04s] English:** So they're riding the wave of the improving models  
**Translation:** 

**[6288.62s] English:** versus competing against them.  
**Translation:** 

**[6291.92s] English:** But sadly, but that's the nature of life on Earth.  
**Translation:** 

**[6296.36s] English:** There could be a huge amount of value to certain kinds of programming  
**Translation:** 

**[6300.62s] English:** at the cutting edge and less value to other kinds.  
**Translation:** 

**[6304.82s] English:** For example, it could be like front-end web design  
**Translation:** 

**[6309.14s] English:** might be more amenable to, as you mentioned,  
**Translation:** Vocabulary: amenable: 易于接受的

**[6314.78s] English:** to generation by AI systems.  
**Translation:** 

**[6318.32s] English:** And maybe, for example, game engine design or something like this,  
**Translation:** 

**[6321.16s] English:** or back-end design, or guiding systems in high-performance situations.  
**Translation:** 

**[6326.36s] English:** High-performance programming type of design decisions,  
**Translation:** 

**[6329.68s] English:** that might be extremely valuable.  
**Translation:** 

**[6331.76s] English:** But it will shift where the humans are needed most,  
**Translation:** 

**[6335.46s] English:** and that's scary for people to adjust.  
**Translation:** 

**[6337.60s] English:** Yeah, I think that's right.  
**Translation:** 

**[6338.96s] English:** At any time where there's a lot of disruption and change,  
**Translation:** 

**[6342.36s] English:** and we've had this, it's not just this time,  
**Translation:** Vocabulary: disruption: 干扰

**[6343.98s] English:** we've had this many times in human history with the internet, mobile,  
**Translation:** 

**[6348.38s] English:** but before that was the Industrial Revolution.  
**Translation:** 

**[6351.16s] English:** And it's going to be one of those eras where there will be a lot of change.  
**Translation:** 

**[6354.34s] English:** I think there'll be new jobs we can't even imagine,  
**Translation:** 

**[6356.36s] English:** today, just like the internet created.  
**Translation:** 

**[6358.88s] English:** And then those people with the right...  
**Translation:** 

**[6360.00s] English:** skill sets to ride that wave will become incredibly valuable, those skills. But maybe  
**Translation:** 

**[6366.90s] English:** people will have to relearn or adapt a bit their current skills. And it's the thing that's going  
**Translation:** 

**[6373.10s] English:** to be harder to deal with this time around is that I think what we're going to see is something like  
**Translation:** 

**[6377.86s] English:** probably 10 times the impact the Industrial Revolution had, but 10 times faster as well.  
**Translation:** 

**[6384.44s] English:** So instead of 100 years, it takes 10 years. And so that's going to make it, it's like 100x  
**Translation:** 

**[6389.12s] English:** the impact and the speed combined. So that's what's, I think, going to make it more difficult  
**Translation:** 

**[6394.14s] English:** for society to deal with. And there's a lot to think through. And I think we need to be  
**Translation:** 

**[6400.32s] English:** discussing that right now. And I encourage top economists in the world and philosophers to  
**Translation:** Vocabulary: economists: 经济学家

**[6405.70s] English:** start thinking about how is society going to be affected by this and what should we do,  
**Translation:** 

**[6412.08s] English:** including things like universal basic provision or something like that, where a lot of the  
**Translation:** 

**[6419.02s] English:** increased productivity gets shared out and distributed to society, and maybe in the form  
**Translation:** 

**[6426.32s] English:** of services and other things, where if you want more than that, you still go and get some incredibly  
**Translation:** 

**[6432.14s] English:** rare skills and things like that and make yourself unique. But there's a basic provision that is  
**Translation:** 

**[6438.52s] English:** provided. And if you think of government as technology, there's also interesting questions,  
**Translation:** 

**[6442.76s] English:** not just in economics, but just politics. How do you design a system that's responding to the,  
**Translation:** 

**[6449.02s] English:** rapidly changing times, such that you can represent the different pain that people feel  
**Translation:** 

**[6455.68s] English:** from the different groups? And how do you reallocate resources in a way that addresses  
**Translation:** 

**[6462.90s] English:** that pain and represents the hope and the pain and the fears of different people in a way that  
**Translation:** Vocabulary: reallocate: 重新分配

**[6469.06s] English:** doesn't lead to division? Because politicians are often really good at sort of fueling the division  
**Translation:** 

**[6475.84s] English:** and using that to get elected. The other,  
**Translation:** 

**[6479.02s] English:** Nick.  
**Translation:** 

**[6480.00s] English:** defining the other and then saying that's bad and so based on that i think that's often  
**Translation:** 

**[6486.68s] English:** counterproductive to leveraging a rapidly changing technology how to help the world flourish so we  
**Translation:** 

**[6492.38s] English:** almost need to improve our political systems as well rapidly if you think of them as a technology  
**Translation:** Vocabulary: counterproductive: 适得其反; flourish: 繁荣发展; leveraging: 利用

**[6499.40s] English:** definitely and i think i think we'll need new governance structures institutions probably to  
**Translation:** 

**[6505.04s] English:** help with this transition so i think political philosophy and political science is going to be  
**Translation:** Vocabulary: governance: 治理结构

**[6510.34s] English:** key uh to that but i think the number one thing first of all is to create more abundance of  
**Translation:** 

**[6516.48s] English:** resources right then there's the so that's the number one thing increase productivity get more  
**Translation:** 

**[6521.92s] English:** resources maybe eventually get out of the zero sum situation then the second question is how to use  
**Translation:** 

**[6528.08s] English:** those resources and distribute those resources but yeah you can't do that without having that  
**Translation:** 

**[6532.78s] English:** abundance first uh you mentioned  
**Translation:** 

**[6535.02s] English:** to me uh the book the maniac uh by benjamin libitute a book on uh first of all about you  
**Translation:** Vocabulary: maniac: 狂热者

**[6542.74s] English:** there's a bio about you um it's strange yeah it's unclear yes sir it's unclear how much is fiction  
**Translation:** 

**[6549.64s] English:** how much is reality um but i think the central figure that is uh john von neumann i would say  
**Translation:** Vocabulary: neumann: 冯诺伊曼

**[6555.98s] English:** it's a haunting and beautiful exploration of madness and genius and let's say the double-edged  
**Translation:** 

**[6561.24s] English:** sword of discovery and  
**Translation:** Vocabulary: haunting: 令人不安的

**[6565.02s] English:** you know for um people don't know john von neumann is a kind of legendary mind he contributed to  
**Translation:** 

**[6570.06s] English:** quantum mechanics he was on the manhattan project he is widely considered to be the father of or  
**Translation:** 

**[6575.92s] English:** pioneer the modern computer and ai and so on so as many people say he's like one of the smartest  
**Translation:** 

**[6582.92s] English:** humans ever so it's just fascinating and what's also fascinating is as a person who saw nuclear  
**Translation:** 

**[6589.60s] English:** science and physics become the atomic bomb so you you got the  
**Translation:** 

**[6595.02s] English:** ideas become a thing that has a huge amount of impact on the world  
**Translation:** 

**[6600.00s] English:** he also foresaw the same thing for computing.  
**Translation:** 

**[6604.22s] English:** And that's a little bit, again, beautiful and haunting aspect of the book.  
**Translation:** Vocabulary: computing: 计算

**[6610.58s] English:** Then taking a leap forward and looking at this at least at all AlphaGo, AlphaZero big moment  
**Translation:** 

**[6618.64s] English:** that maybe John von Neumann's thinking was brought to reality.  
**Translation:** 

**[6626.02s] English:** So I guess the question is, what do you think if you got to hang out with John von Neumann  
**Translation:** 

**[6631.62s] English:** now, what would he say about what's going on?  
**Translation:** 

**[6635.40s] English:** Well, that would be an amazing experience.  
**Translation:** 

**[6636.78s] English:** You know, he's a fantastic mind.  
**Translation:** 

**[6638.98s] English:** And I also love the way he spent a lot of his time at Princeton at the Institute of  
**Translation:** 

**[6643.42s] English:** Advanced Studies, a very special place for thinking.  
**Translation:** Vocabulary: princeton: 普林斯顿大学

**[6646.82s] English:** And it's amazing how much of a polymath he was in the spread of things he helped invent,  
**Translation:** 

**[6652.70s] English:** including, of course, the von Neumann architecture that all the  
**Translation:** Vocabulary: polymath: 博学之人

**[6655.34s] English:** modern computers have.  
**Translation:** 

**[6656.02s] English:** And he had amazing foresight.  
**Translation:** Vocabulary: foresight: 远见

**[6660.46s] English:** I think he would have loved where we are today.  
**Translation:** 

**[6663.50s] English:** And he would have, I think he would have really enjoyed AlphaGo being, you know, he also did  
**Translation:** 

**[6668.44s] English:** game theory.  
**Translation:** 

**[6669.62s] English:** I think he foresaw a lot of what would happen with learning machine systems that are kind  
**Translation:** 

**[6675.44s] English:** of grown, I think he called it, rather than programmed.  
**Translation:** 

**[6678.14s] English:** I'm not sure how even, maybe he wouldn't even be that surprised.  
**Translation:** 

**[6680.64s] English:** There's the fruition of what I think he already foresaw in the 1950s.  
**Translation:** 

**[6684.68s] English:** I wonder what advice he would give to people.  
**Translation:** 

**[6686.02s] English:** You got to see the building of the atomic bomb with the Manhattan Project.  
**Translation:** 

**[6690.22s] English:** I'm sure there's interesting stuff that maybe is not talked about enough.  
**Translation:** 

**[6693.66s] English:** Maybe some bureaucratic aspect, maybe the influence of politicians, maybe not enough  
**Translation:** 

**[6699.08s] English:** of picking up the phone and talking to people that are called enemies by the said politicians.  
**Translation:** Vocabulary: bureaucratic: 官僚主义

**[6704.66s] English:** There might be some like deep wisdom that we just may have lost from that time, actually.  
**Translation:** 

**[6708.58s] English:** Yeah, I'm sure.  
**Translation:** 

**[6709.28s] English:** I'm sure there is.  
**Translation:** 

**[6710.20s] English:** I mean, I've taught, we, you know, study, I read a lot of books for that time as well,  
**Translation:** 

**[6713.92s] English:** Chronicle Time.  
**Translation:** 

**[6714.88s] English:** And some brilliant people involved.  
**Translation:** Vocabulary: chronicle: 编年史

**[6717.30s] English:** I agree with you.  
**Translation:** 

**[6718.18s] English:** I think maybe there needs to be more.  
**Translation:** 

**[6720.00s] English:** dialogue and understanding um i hope we can learn from those those times i think the difference here  
**Translation:** 

**[6726.32s] English:** is that the ai has so many it's a multi-use technology obviously we're trying to do things  
**Translation:** 

**[6731.22s] English:** like that like solve you know all diseases um help with energy uh and scarcity these incredible  
**Translation:** 

**[6738.58s] English:** things this is why all of us and myself you know i worked started on this journey 30 plus years ago  
**Translation:** Vocabulary: scarcity: 资源匮乏

**[6744.16s] English:** and um but of course there are risks too and probably von neumann my guess is he foresaw both  
**Translation:** 

**[6751.56s] English:** and um and i think he sort of said i think is to his wife that that it would be a this is  
**Translation:** Vocabulary: neumann: 冯·诺伊曼

**[6757.28s] English:** computers would be even more impactful in the world and as we just discussed you know i think  
**Translation:** 

**[6762.34s] English:** that's right i think it's going to be 10 times at least of the industrial revolution so i think  
**Translation:** 

**[6767.30s] English:** he's right so i think he would have been i imagine fascinated by uh where we are now and i think one  
**Translation:** 

**[6774.14s] English:** of the maybe you can correct me but one of the takeaways from the book is that reason has uh  
**Translation:** Vocabulary: fascinated: 着迷; takeaways: 收获

**[6782.00s] English:** said in the book mad dreams of reason it's not enough for guiding humanity as we build these  
**Translation:** 

**[6787.62s] English:** super powerful technology that there's something else i mean there's also like a religious component  
**Translation:** 

**[6793.36s] English:** whatever god whatever religion gives it pulls it something in the human spirit that  
**Translation:** 

**[6798.58s] English:** raw cold reason doesn't give us and i agree with that i think we need to  
**Translation:** 

**[6804.14s] English:** approach it with whatever you want to call it the spiritual dimension or humanist dimension  
**Translation:** 

**[6808.86s] English:** doesn't have to be to do with religion right but this idea of of a soul what makes us human this  
**Translation:** Vocabulary: dimension: 维度; humanist: 人本主义

**[6814.06s] English:** spark that we have perhaps is to do with consciousness when we finally understand that  
**Translation:** 

**[6818.54s] English:** um i think that has to be at the heart of the endeavor um and technology i've always seen  
**Translation:** Vocabulary: endeavor: 努力

**[6823.42s] English:** technology as the enabler right the tools that enable us to to flourish and to understand more  
**Translation:** 

**[6829.98s] English:** about the world and i'm sort of with feynman on this and he used to always talk about  
**Translation:** Vocabulary: enabler: 助力者; flourish: 繁荣生长

**[6834.14s] English:** science and art being companions right you can understand it from both sides the  
**Translation:** 

**[6840.00s] English:** of a flower how beautiful it is and also understand why the colors of the flower evolved like that  
**Translation:** 

**[6845.26s] English:** right that just makes it more beautiful that just the intrinsic beauty of the flower and and i've  
**Translation:** 

**[6850.42s] English:** always sort of seen it like that and maybe you know in the renaissance times the great discoverers  
**Translation:** Vocabulary: intrinsic: 本质的; renaissance: 文艺复兴

**[6855.22s] English:** then like people like da vinci you know they were i don't think he saw any difference between science  
**Translation:** 

**[6860.12s] English:** and art uh and perhaps religion right everything was it's just part of being human and um being  
**Translation:** Vocabulary: vinci: 达·芬奇

**[6866.34s] English:** inspired about the world around us and that's what i the philosophy i try to take and uh one of my  
**Translation:** 

**[6872.60s] English:** favorite philosophers is spinoza and i think he combined that all very well you know this idea of  
**Translation:** Vocabulary: spinoza: 斯宾诺莎

**[6877.46s] English:** trying to understand the universe and understanding our place in it and that was his kind of way of  
**Translation:** 

**[6882.56s] English:** understanding religion and i think that's quite beautiful and for me every all of these things are  
**Translation:** 

**[6888.08s] English:** related interrelated the technology and um what it means to be human and uh i think it's very  
**Translation:** 

**[6894.76s] English:** important though that we remain  
**Translation:** Vocabulary: interrelated: 相互关联

**[6896.34s] English:** remember that as when we're immersed in the technology and the the research i think a lot  
**Translation:** 

**[6902.30s] English:** of researchers that i see in in our field are a little bit too narrow and only understand the  
**Translation:** Vocabulary: immersed: 沉浸

**[6908.52s] English:** technology and i think also that's why it's important for this to be debated by society at  
**Translation:** 

**[6914.08s] English:** large and i'm very supportive of things like this the ai summits that will happen and governments  
**Translation:** 

**[6918.38s] English:** understanding it and i think that's one good thing about the chatbot era and the product era of ai is  
**Translation:** 

**[6923.50s] English:** that everyday person can actually feel and understand the world around them and i think  
**Translation:** 

**[6926.32s] English:** that's a really good thing that people should be able to do and and interact with cutting-edge ai and  
**Translation:** 

**[6928.48s] English:** and and feel feel it for themselves yeah because they they force the technologists to have the  
**Translation:** Vocabulary: technologists: 技术人员

**[6932.90s] English:** human conversation yeah for sure yeah that's the whole aspect of it like you said it's a dual-use  
**Translation:** 

**[6937.16s] English:** technology that we're forcefully integrating the entire humanity into it by into the discussion  
**Translation:** Vocabulary: forcefully: 强行

**[6942.82s] English:** about ai because ultimately ai agi will be used for things that states use technologies for  
**Translation:** 

**[6950.54s] English:** which is a conflict and so on and the more we uh  
**Translation:** 

**[6956.32s] English:** humans into this picture by having chats with them.  
**Translation:** 

**[6960.00s] English:** more we will guide yeah be able to adapt society will be able to adapt to these technologies like  
**Translation:** 

**[6965.24s] English:** we've always done in the past with with uh the incredible technologies we've invented in the past  
**Translation:** 

**[6970.04s] English:** do you think there will be something like a manhattan project where um there will be an  
**Translation:** 

**[6978.72s] English:** escalation of the power of this technology in states in their old way of thinking we'll try  
**Translation:** 

**[6983.02s] English:** to use it as weapons technologies and there will be this kind of escalation i hope not um i think  
**Translation:** Vocabulary: escalation: 升级

**[6989.18s] English:** that would be uh very dangerous to do and i think also um you know not the right use of the  
**Translation:** 

**[6996.48s] English:** technology i hope we'll end up with more something more collaborative if needed like more like a  
**Translation:** Vocabulary: collaborative: 合作的

**[7002.32s] English:** like a cern project you know where um it's research focused and the best minds in the world  
**Translation:** 

**[7009.16s] English:** come together to carefully complete the final steps and make sure it's responsibly done before  
**Translation:** 

**[7016.26s] English:** you know like deploying it to the world we'll see  
**Translation:** 

**[7019.18s] English:** i mean it's difficult with the current geopolitical climate i think uh to to see cooperation but  
**Translation:** Vocabulary: deploying: 部署; geopolitical: 地缘政治的

**[7024.88s] English:** things can change and um i think at least on the scientific level it's important for the  
**Translation:** 

**[7030.08s] English:** researchers to to to to keep in touch and and and keep close to each other on at least on those  
**Translation:** 

**[7035.58s] English:** kinds of topics yeah and i personally believe on the education side and uh immigration side it  
**Translation:** 

**[7041.16s] English:** would be great if both directions uh people from the west immigrated china and china back i mean  
**Translation:** Vocabulary: immigrated: 移民

**[7049.18s] English:** human aspect of people just intermixing yeah and thereby those ties grow strong so you can't sort of  
**Translation:** 

**[7055.84s] English:** divide against each other this kind of old school way of thinking and so uh multi uh multicultural  
**Translation:** Vocabulary: intermixing: 混合; multicultural: 多元文化

**[7062.60s] English:** multidisciplinary research teams working on scientific questions that's like the hope  
**Translation:** 

**[7067.06s] English:** don't don't let the the warm leaders that are warmongers because they divide us i think science  
**Translation:** Vocabulary: multidisciplinary: 跨学科; warmongers: 挑起战争的人

**[7072.58s] English:** is the ultimately really beautiful connector yeah science has always been uh i think quite a  
**Translation:** 

**[7078.04s] English:** very collaborative and  
**Translation:** Vocabulary: connector: 连接器

**[7079.18s] English:** ever and  
**Translation:** 

**[7080.00s] English:** And, you know, scientists know that it's it's a it's a collective endeavor as well.  
**Translation:** 

**[7083.54s] English:** And we can all learn from each other. So perhaps it could be a vector to get a bit of cooperation.  
**Translation:** 

**[7088.20s] English:** What's your ridiculous question? What's your P-Doom? Probability of the human civilization destroys itself.  
**Translation:** 

**[7093.90s] English:** Well, look, I don't have a it's a you know, I don't have a P-Doom number.  
**Translation:** 

**[7099.94s] English:** The reason I don't is because I think it would imply a level of precision that is not there.  
**Translation:** 

**[7105.96s] English:** So I don't know how people are getting their P-Doom numbers.  
**Translation:** 

**[7109.00s] English:** I think it's a kind of a little bit of a ridiculous notion, because what I would say is it's definitely non-zero and it's probably non-negligible.  
**Translation:** 

**[7118.72s] English:** So that in itself is pretty sobering. And my view is it's just hugely uncertain.  
**Translation:** 

**[7124.98s] English:** Right. What these technologies are going to be able to do, how fast are they going to take off, how controllable they're going to be.  
**Translation:** Vocabulary: sobering: 令人警醒

**[7130.74s] English:** Some things may turn out to be and hopefully like way easier than we thought.  
**Translation:** 

**[7134.74s] English:** Right. But it may be there's some really hard.  
**Translation:** 

**[7137.84s] English:** Problems that are harder than we guessed today.  
**Translation:** 

**[7139.84s] English:** And I think we don't know that for sure.  
**Translation:** 

**[7141.84s] English:** And so under those conditions of a lot of uncertainty, but huge stakes both ways, you know, on the one hand, we could solve all diseases, energy problems, the scarcity problem, and then travel to the stars and consciousness of the stars and maximum human flourishing.  
**Translation:** 

**[7158.84s] English:** On the other hand, is this sort of P-Doom scenarios.  
**Translation:** Vocabulary: flourishing: 繁荣; scarcity: 匮乏; scenarios: 情景

**[7160.84s] English:** So given the uncertainty around it and the importance of it, it's clear to me, the only rational, sensible way to solve it is to solve it.  
**Translation:** 

**[7165.56s] English:** And that's what we're trying to do.  
**Translation:** 

**[7166.52s] English:** And that's what we're trying to do.  
**Translation:** 

**[7167.02s] English:** And that's what we're trying to do.  
**Translation:** 

**[7167.52s] English:** And that's what we're trying to do.  
**Translation:** 

**[7167.72s] English:** The idea behind that is that we think.  
**Translation:** 

**[7169.14s] English:** As a non- societal world, I think it's going to be a very, very useful approach is to proceed with cautious optimism.  
**Translation:** 

**[7174.14s] English:** So we want the outcome, we want the, um, uh, the benefits of course.  
**Translation:** Vocabulary: optimism: 乐观

**[7178.32s] English:** Uh, and, uh, all of the, the amazing things that AI can bring.  
**Translation:** 

**[7183.22s] English:** And actually, I would be really worried for humanity if I, if given the other challenges that we have, climate, you know, aging, uh, resources, all of that.  
**Translation:** 

**[7193.46s] English:** If I didn't know something that AI was coming down the line.  
**Translation:** 

**[7196.18s] English:** Right.  
**Translation:** 

**[7196.48s] English:** How would we solve all those other problems?  
**Translation:** 

**[7197.72s] English:** amazingly transformative for good.  
**Translation:** 

**[7200.00s] English:** But on the other hand, there are these risks that we know are there, but we can't quite quantify. So the best thing to do is to use the scientific method to do more research to try and more precisely define those risks and, of course, address them. And I think that's what we're doing. I think there probably needs to be 10 times more effort of that than there is now as we're getting closer and closer to the AGI line.  
**Translation:** 

**[7227.78s] English:** What would be the source of worry for you more? Would it be human-caused or AI, AGI-caused?  
**Translation:** Vocabulary: quantify: 量化

**[7235.08s] English:** Humans abusing that technology versus AGI itself through a mechanism that you've spoken about, which is fascinating, deception or this kind of stuff, getting better and better and better secretly.  
**Translation:** 

**[7244.56s] English:** I think they operate over different timescales and they're equally important to address.  
**Translation:** Vocabulary: deception: 欺骗; timescales: 时间尺度

**[7250.18s] English:** So there's just the common garden of variety of bad actors using new technology, in this case journalism.  
**Translation:** 

**[7257.78s] English:** And that's a huge risk.  
**Translation:** 

**[7262.88s] English:** And I think that has a lot of complications because generally, you know, I'm in huge favor of open science and open source.  
**Translation:** 

**[7270.78s] English:** And in fact, we did it with all our science projects like AlphaFold and all of those things for the benefit of the scientific community.  
**Translation:** 

**[7278.18s] English:** But how does one restrict bad actors access to these powerful systems, whether they're individuals or even rogue states?  
**Translation:** 

**[7286.24s] English:** And but enable access.  
**Translation:** Vocabulary: rogue: 叛逆国家

**[7288.38s] English:** At the same time, to good actors to to maximally build on top of it's pretty tricky problem that I've not heard a clear solution to.  
**Translation:** 

**[7296.78s] English:** So there's the bad actor use case problem.  
**Translation:** Vocabulary: maximally: 最大程度上

**[7298.70s] English:** And then there's obviously as the systems become more gentic and closer to AGI and more autonomous, how do we ensure the guardrails and they stick to what we want them to do and under our control?  
**Translation:** 

**[7312.28s] English:** Yeah, I tend to maybe on my mind is limited, worry more about the humans, the bad actors.  
**Translation:** Vocabulary: autonomous: 自主; guardrails: 防护栏

**[7317.78s] English:** And there it could be.  
**Translation:** 

**[7320.00s] English:** So in part, how do you not put destructive technology in the hands of bad actors? But in another part, from, again, geopolitical technology perspective, how do you reduce the number of bad actors in the world? That's also an interesting human problem.  
**Translation:** Vocabulary: geopolitical: 地缘政治的

**[7333.94s] English:** Yeah, it's a hard problem. I mean, look, we can maybe also use the technology itself to help early warning on some of the bad actor use cases, right? Whether that's bio or nuclear or whatever it is, like AI could be potentially helpful there, as long as the AI that you're using is itself reliable, right?  
**Translation:** 

**[7356.26s] English:** So it's a sort of interlocking problem. And that's what makes it very tricky. And again, it may require some agreement internationally, at least potentially.  
**Translation:** 

**[7363.94s] English:** Between China and the US of some basic standards, right?  
**Translation:** 

**[7370.36s] English:** I have to ask you about the book, The Maniac. There's this, the hand of God moment, Lisa Dahl's move 78, that perhaps the last time a human did a move of sort of pure human genius and beat AlphaGo, or like broke his brain.  
**Translation:** Vocabulary: maniac: 狂人

**[7388.40s] English:** Yes.  
**Translation:** 

**[7388.54s] English:** Sorry to anthropomorphize, but it's an interesting moment, because I think in so many domains, it will keep happening.  
**Translation:** Vocabulary: anthropomorphize: 赋予人类特征

**[7393.94s] English:** Yeah, it's a special moment. And, you know, it was great for Lisa Dahl. And, you know, I think it's, in a way, they were sort of inspiring each other, we as a team were inspired by Lisa Dahl's brilliance and nobleness. And then maybe he got inspired by, you know, what AlphaGo was doing to then conjure this incredible inspirational moment. It's all, you know, captured very well in the in the documentary about it. And I think that will continue in many domains where there's this, at least for the, for the again, for the foreseeable future.  
**Translation:** 

**[7423.94s] English:** future of like, the humans bringing in the ingenuity, and asking the right question, let's say, and then utilizing these tools, in a way that then cracks a problem.  
**Translation:** Vocabulary: brilliance: 卓越; conjure: 创造; foreseeable: 可预见的; ingenuity: 创造力; inspirational: 激励人的; nobleness: 高尚; utilizing: 利用

**[7438.08s] English:** Yeah, what is the AI become smarter?  
**Translation:** 

**[7440.00s] English:** and smarter one of the interesting questions we can ask ourselves is what makes humans special  
**Translation:** 

**[7445.08s] English:** it does feel um perhaps biased that we humans are deeply special i don't know if it's our  
**Translation:** 

**[7452.68s] English:** intelligence it could be something else that that other thing that's outside the mad dreams of  
**Translation:** 

**[7459.68s] English:** reason i think that's what i've always imagined uh when i was a kid and starting on this journey  
**Translation:** 

**[7465.06s] English:** of like um i was of course fascinated by things like consciousness did did a neuroscience phd to  
**Translation:** Vocabulary: fascinated: 着迷; neuroscience: 神经科学

**[7471.06s] English:** look at how the brain works especially imagination and memory i focused on the hippocampus and it's  
**Translation:** 

**[7475.72s] English:** sort of going to be interesting i always thought the best way of course one can come philosophize  
**Translation:** Vocabulary: hippocampus: 海马区; philosophize: 哲学思考

**[7479.98s] English:** about it and have thought experiments and maybe even do actual experiments like you do in  
**Translation:** 

**[7484.52s] English:** neuroscience on on real brains but in the end i always imagined that building ai a kind of  
**Translation:** 

**[7490.16s] English:** intelligent artifact and then comparing that to the human mind and seeing what the differences  
**Translation:** 

**[7494.44s] English:** were  
**Translation:** Vocabulary: artifact: 人工制品

**[7494.94s] English:** uh would be the best way to uncover what's special about the human mind if indeed there  
**Translation:** 

**[7499.70s] English:** is anything special and i suspect there probably is but it's going to be hard to you know i think  
**Translation:** 

**[7504.52s] English:** this journey we're on will help us uh understand that and define that and you know there may be a  
**Translation:** 

**[7509.60s] English:** difference between carbon-based substrates that we are and silicon wants when they process  
**Translation:** Vocabulary: substrates: 基底材料

**[7515.14s] English:** information you know one of the best definitions i like of of consciousness is it's the way  
**Translation:** 

**[7519.78s] English:** information feels when we process it right um it could be i mean it doesn't it's not a very  
**Translation:** 

**[7524.74s] English:** helpful way to understand it but it's a way to understand it and it's a way to understand it  
**Translation:** 

**[7524.92s] English:** but it's a way to understand it and it's a way to understand it and it's a helpful scientific  
**Translation:** 

**[7525.80s] English:** explanation i think it's kind of interesting intuition intuitive one and um and so you know  
**Translation:** 

**[7530.74s] English:** on this this this journey this scientific journey we're on will i think um help uncover that mystery  
**Translation:** Vocabulary: intuition: 直觉; intuitive: 直观的

**[7536.14s] English:** yeah what i cannot create i do not understand that's uh somebody you deeply admire richard  
**Translation:** 

**[7541.46s] English:** feinman like you mentioned you also reach um for the the wigner's dreams of universality that he  
**Translation:** Vocabulary: cannot: 不能; universality: 普遍性

**[7548.54s] English:** saw in constrained domains but also broadly generally in in mathematics and so on so so many  
**Translation:** 

**[7554.92s] English:** aspects on which you're pushing towards not to start trouble at the end but uh roger  
**Translation:** Vocabulary: constrained: 限制的

**[7560.00s] English:** penrose yes okay so uh you know do you think consciousness there's this hard problem of  
**Translation:** 

**[7567.40s] English:** consciousness how information feels um do you think consciousness first of all is a computation  
**Translation:** Vocabulary: computation: 计算; penrose: 彭罗斯

**[7574.98s] English:** and if it is if it's information processing like you said everything is is it something that could  
**Translation:** 

**[7581.52s] English:** be modeled by a classical computer yeah or is it a quantum mechanical in nature well look at  
**Translation:** 

**[7586.78s] English:** penrose is amazing thinker one of the greatest of the modern era and he we've had a lot of  
**Translation:** 

**[7590.84s] English:** discussions about this of course we cordially disagree which is you know i i feel like um i  
**Translation:** Vocabulary: cordially: 友好地

**[7596.62s] English:** mean he collaborated with a lot of good neuroscientists to see if he could find mechanisms  
**Translation:** 

**[7600.60s] English:** for quantum mechanics behavior in the brain and they to my knowledge they haven't found anything  
**Translation:** Vocabulary: collaborated: 合作; neuroscientists: 神经科学家

**[7606.00s] English:** um convincing yet so my betting is there is is that it's mostly you know it is just classical  
**Translation:** 

**[7612.54s] English:** computing that's going on in the brain which suggests that all the phenomena  
**Translation:** Vocabulary: computing: 计算

**[7616.78s] English:** are modelable or mimicable by a classical computer but we'll see you know that there  
**Translation:** 

**[7622.88s] English:** may be this final mysterious things of the feeling of consciousness the qualia these kinds of things  
**Translation:** Vocabulary: mimicable: 可模仿; modelable: 可模拟; qualia: 主观体验

**[7628.66s] English:** that philosophers debate where it's unique to the substrate we may even come towards understanding  
**Translation:** 

**[7634.24s] English:** that when if we do things like neural link and and have neural interfaces to the ai systems which i  
**Translation:** Vocabulary: interfaces: 接口; neural: 神经; substrate: 基底

**[7640.46s] English:** think we probably will eventually um maybe to keep up with the ai systems uh we might actually be  
**Translation:** 

**[7646.12s] English:** able to feel for our own consciousness and we might be able to feel for our own consciousness  
**Translation:** 

**[7646.78s] English:** what it's like to compute on silicon right so um and maybe that will tell us uh so i think it's it's  
**Translation:** 

**[7655.60s] English:** going to be interesting and i had a debate once with the late daniel dennett about why do we think  
**Translation:** Vocabulary: dennett: 丹尼特

**[7660.46s] English:** each other are conscious okay so it's for two reasons one is you're exhibiting the same behavior  
**Translation:** 

**[7664.88s] English:** that i am so that's one thing behaviorally you seem like a conscious being if i am but the second  
**Translation:** Vocabulary: exhibiting: 展示

**[7670.28s] English:** thing which is often overlooked is that we're running on the same substrate so if you're  
**Translation:** 

**[7674.32s] English:** behaving in the same way and we're running on the same substrate  
**Translation:** Vocabulary: overlooked: 忽视的

**[7676.78s] English:** it's most parsimonious to assume you're feeling the same  
**Translation:** 

**[7680.00s] English:** that i'm feeling but with an ai uh that's on silicon we won't be able to rely on the second  
**Translation:** Vocabulary: parsimonious: 简洁

**[7686.12s] English:** part even if it exhibits the first part that behavior looks like a behavior of a conscious  
**Translation:** 

**[7689.94s] English:** being it might even claim it is um but we but but we wouldn't know how it actually felt um and it  
**Translation:** Vocabulary: exhibits: 表现

**[7697.24s] English:** probably couldn't know we what we felt at least in the first stages maybe when we get to super  
**Translation:** 

**[7701.64s] English:** intelligence and the technologies that builds perhaps we'll we'll be able to bridge that no  
**Translation:** 

**[7706.30s] English:** that's a huge test for radical empathy is to empathize with a different substrate right  
**Translation:** 

**[7712.42s] English:** exactly we never had to confront that before yeah so maybe maybe through brain computer  
**Translation:** Vocabulary: confront: 面对; empathize: 共情; empathy: 共情

**[7717.84s] English:** interfaces be able to truly empathize what it feels like to be a computer  
**Translation:** 

**[7721.76s] English:** well for information to be computed not on a carbon system i mean that's deeply i mean some  
**Translation:** Vocabulary: computed: 计算完成

**[7728.36s] English:** people kind of think about that with plants with other life forms which could be exactly similar  
**Translation:** 

**[7732.88s] English:** substrate but sufficiently far enough  
**Translation:** Vocabulary: sufficiently: 足够地

**[7736.30s] English:** on the uh evolutionary tree yeah that it's requires a radical empathy but to do that with  
**Translation:** 

**[7741.86s] English:** a computer i mean no we sort of there are animal studies on this of like of course higher animals  
**Translation:** Vocabulary: evolutionary: 进化

**[7746.40s] English:** like you know killer whales and dolphins and dogs and and monkeys you know they have some and  
**Translation:** 

**[7752.38s] English:** elephants you know they have some aspects certainly of consciousness right even though they're not  
**Translation:** 

**[7756.68s] English:** might not be that that that smart on an iq sense so we can already empathize with that and maybe  
**Translation:** 

**[7762.06s] English:** even some of our systems one day like we built this thing called dolphin gemma you know which  
**Translation:** Vocabulary: gemma: 海豚宝石

**[7766.14s] English:** could be a computer that could be a computer that could be a computer that could be a computer  
**Translation:** 

**[7766.30s] English:** and one a version of our system was trained on dolphin and whale sounds and maybe we'll be able  
**Translation:** 

**[7771.14s] English:** to build a an interpreter or translator at some point which would be pretty cool what gives you  
**Translation:** 

**[7775.86s] English:** hope for the future of human civilization well what gives me hope is i think our almost limitless  
**Translation:** Vocabulary: interpreter: 口译员; limitless: 无穷的; translator: 翻译器

**[7782.40s] English:** ingenuity first of all i think the best of us and the best human minds are incredible um and you  
**Translation:** 

**[7789.84s] English:** know i love you know meeting and watching any human that's the top of their game whether that's  
**Translation:** Vocabulary: ingenuity: 聪明才智

**[7796.14s] English:** sport or science or art you know it's it's it's just nothing more one  
**Translation:** 

**[7800.00s] English:** than that seeing them in their element in flow um i think it's almost limitless you know our brains  
**Translation:** 

**[7804.82s] English:** are general systems intelligent systems so i think it's almost limitless what we can potentially do  
**Translation:** 

**[7810.72s] English:** with them and then the other thing is our extreme adaptability i think it's gonna be okay in terms  
**Translation:** Vocabulary: adaptability: 适应能力

**[7817.56s] English:** of there's gonna be a lot of change but that but look where we are now without effectively our  
**Translation:** 

**[7822.88s] English:** hunter-gatherer brains how is it we can you know we can cope with the modern world right flying on  
**Translation:** 

**[7829.40s] English:** planes doing podcasts you know playing computer games and virtual simulations i mean it's already  
**Translation:** 

**[7835.42s] English:** mind-blowing given that our mind was was developed for you know hunting buffaloes on the on the  
**Translation:** Vocabulary: buffaloes: 野牛

**[7840.32s] English:** tundra and and so i think this is just the next step and and and it's actually kind of interesting  
**Translation:** 

**[7845.94s] English:** to see how society's already adapted to this mind-blowing ai technology we have today already  
**Translation:** Vocabulary: tundra: 冻原

**[7851.12s] English:** it's sort of like oh i talk to chatbots totally fine and it's uh very possible that this very  
**Translation:** 

**[7856.34s] English:** podcast activity which i'm here for  
**Translation:** Vocabulary: chatbots: 聊天机器人

**[7859.40s] English:** completely replaced by ai i'm very replaceable and i'm waiting not to the level that you can do it  
**Translation:** 

**[7863.92s] English:** lex i don't think i thank you that's that's what we humans do to each other we complement  
**Translation:** Vocabulary: replaceable: 可以替代的

**[7867.86s] English:** all right and uh i'm uh deeply grateful for us humans to have this uh infinite capacity for  
**Translation:** 

**[7873.92s] English:** curiosity adaptability like you said and also compassion and ability to love exactly all of  
**Translation:** Vocabulary: compassion: 同情心

**[7879.30s] English:** those human things that are deeply human well this is a huge honor demis you're one of the  
**Translation:** 

**[7884.14s] English:** truly special humans in the world uh thank you so much for doing what you do and for talking to me  
**Translation:** 

**[7889.40s] English:** today well thank you very much lex thanks for listening to this conversation with demis kasabas  
**Translation:** 

**[7894.52s] English:** to support this podcast please check out our sponsors in the description and consider subscribing  
**Translation:** Vocabulary: sponsors: 赞助商; subscribing: 订阅

**[7900.18s] English:** to this channel and now let me answer some questions and try to articulate some things  
**Translation:** 

**[7907.02s] English:** i've been thinking about if you'd like to submit questions including in audio and video form go to  
**Translation:** Vocabulary: articulate: 表达清楚

**[7912.96s] English:** lexfreeman.com slash ama i got a lot of amazing questions thoughts and requests from folks  
**Translation:** 

**[7919.40s] English:** i'll keep trying  
**Translation:** 

**[7920.00s] English:** pick some randomly and comment on it at the end of every episode. I got a note on May 21st this year  
**Translation:** 

**[7928.64s] English:** that said, Hi Lex, 20 years ago today, David Foster Wallace delivered his famous This Is Water speech  
**Translation:** Vocabulary: foster: 培养

**[7936.04s] English:** at Kenyon College. What do you think of this speech? Well, first, I think this is probably  
**Translation:** 

**[7944.58s] English:** one of the greatest and most unique commencement speeches ever given. But of course, I have many  
**Translation:** Vocabulary: kenyon: Kenyon学院

**[7951.76s] English:** favorites, including the one by Steve Jobs. And David Foster Wallace is one of my favorite  
**Translation:** 

**[7957.68s] English:** writers and one of my favorite humans. There's a tragic honesty to his work, and it always felt  
**Translation:** 

**[7966.18s] English:** as if he was engaging in a constant battle with his own mind. And the writing, his writing,  
**Translation:** 

**[7973.08s] English:** were kind of his notes.  
**Translation:** 

**[7974.58s] English:** Notes from the front lines of that battle. Now, onto the speech. Let me quote some parts.  
**Translation:** 

**[7981.90s] English:** There's, of course, the parable of the fish and the water that goes, There are these two young fish  
**Translation:** 

**[7988.18s] English:** swimming along, and they happen to meet an older fish swimming the other way, who nods at them and  
**Translation:** 

**[7995.28s] English:** says, Morning, boys. How's the water? And the two young fish swim on for a bit, and eventually one  
**Translation:** 

**[8003.58s] English:** of them looks over at the other. And he says, Hey, how's the water? And he says, Hey, how's the  
**Translation:** 

**[8004.56s] English:** other? And goes, What the hell is water? In the speech, David Foster Wallace goes on to say,  
**Translation:** 

**[8012.94s] English:** The point of the fish story is merely that the most obvious, important realities are often the  
**Translation:** 

**[8018.06s] English:** ones that are hardest to see and talk about. Stated as an English sentence, of course,  
**Translation:** 

**[8023.66s] English:** this is just the banal platitude. But the fact is that in the day-to-day trenches of adult  
**Translation:** 

**[8029.34s] English:** existence, banal platitudes can have a life-or-death importance. Or so I wish to say.  
**Translation:** Vocabulary: platitude: 陈词滥调; platitudes: 陈词滥调; trenches: 战壕

**[8034.56s] English:** to you in this dry and lovely morning. I have several takeaways from this.  
**Translation:** 

**[8040.00s] English:** parable and the speech that follows. First, I think we must question everything, and in particular  
**Translation:** Vocabulary: takeaways: 收获

**[8046.94s] English:** the most basic assumptions about our reality, our life, and the very nature of existence,  
**Translation:** 

**[8053.66s] English:** and that this project is a deeply personal one. In some fundamental sense, nobody can really help  
**Translation:** Vocabulary: assumptions: 基本假设

**[8060.14s] English:** you in this process of discovery. The call to action here, I think, from David Foster Wallace,  
**Translation:** 

**[8067.78s] English:** as he puts it, is to, quote, to be just a little less arrogant, to have just a little more critical  
**Translation:** Vocabulary: arrogant: 骄傲; foster: 培养

**[8074.96s] English:** awareness about myself and my certainties, because a huge percentage of the stuff that I tend to be  
**Translation:** 

**[8081.80s] English:** automatically certain of is, it turns out, totally wrong and deluded. All right, back to me,  
**Translation:** Vocabulary: certainties: 确信; deluded: 错觉

**[8090.62s] English:** Lex speaking. The second takeaway is that the central spiritual battles of our life  
**Translation:** 

**[8096.50s] English:** are not fun.  
**Translation:** Vocabulary: takeaway: 要点

**[8097.78s] English:** It is not fought on a mountaintop somewhere at a meditation retreat, but it is fought in the mundane  
**Translation:** 

**[8105.30s] English:** moments of daily life. Third takeaway is that we too easily give away our time and attention  
**Translation:** Vocabulary: mountaintop: 高山顶; mundane: 平凡事务

**[8113.44s] English:** to the multitude of distractions that the world feeds us, the insatiable black holes of attention.  
**Translation:** 

**[8122.90s] English:** David Foster Wallace's call to action, in this case, is to be deeply aware of the  
**Translation:** 

**[8127.78s] English:** beauty in each moment and to find meaning in the mundane. I often quote David Foster Wallace in his  
**Translation:** 

**[8136.68s] English:** advice that the key to life is to be unboreable. And I think this is exactly right. Every moment,  
**Translation:** Vocabulary: unboreable: 不无聊的

**[8144.30s] English:** every object, every experience, when looked at closely enough, contains within it infinite  
**Translation:** 

**[8151.58s] English:** richness to explore. And since Demis Kassabas of this very podcast episode,  
**Translation:** 

**[8157.78s] English:** and I are such fans of Richard Feynman,  
**Translation:** 

**[8160.00s] English:** allow me to also quote Mr. Feynman on this topic as well.  
**Translation:** Vocabulary: feynman: 费曼

**[8165.62s] English:** Quote, I have a friend who's an artist  
**Translation:** 

**[8168.66s] English:** and has sometimes taken a view which I don't agree with very well.  
**Translation:** 

**[8174.38s] English:** He'll hold up a flower and say, look how beautiful it is.  
**Translation:** 

**[8178.16s] English:** And I'll agree.  
**Translation:** 

**[8179.92s] English:** Then he says, I as an artist can see how beautiful this is,  
**Translation:** 

**[8184.70s] English:** but you as a scientist take this all apart and it becomes a dull thing.  
**Translation:** 

**[8190.00s] English:** And I think that's kind of nutty.  
**Translation:** 

**[8193.12s] English:** First of all, the beauty that he sees is available to other people  
**Translation:** Vocabulary: nutty: 荒谬的

**[8197.66s] English:** and to me too, I believe.  
**Translation:** 

**[8200.28s] English:** Although I may not be quite as refined aesthetically as he is,  
**Translation:** Vocabulary: aesthetically: 审美; refined: 精致

**[8204.74s] English:** I can appreciate the beauty of a flower.  
**Translation:** 

**[8207.96s] English:** At the same time, I see much more about the flower than he sees.  
**Translation:** 

**[8212.66s] English:** I can imagine the cells in there,  
**Translation:** 

**[8214.78s] English:** the complicated actions inside which also have beauty.  
**Translation:** 

**[8218.36s] English:** I mean,  
**Translation:** 

**[8219.20s] English:** it's not just beauty at this dimension, at one centimeter.  
**Translation:** Vocabulary: dimension: 维度

**[8222.94s] English:** There's also beauty at the smaller dimensions,  
**Translation:** 

**[8225.48s] English:** the inner structure, also the processes.  
**Translation:** Vocabulary: dimensions: 尺寸

**[8228.22s] English:** The fact that the colors in the flower evolved  
**Translation:** 

**[8230.36s] English:** in order to attract insects to pollinate it is interesting.  
**Translation:** Vocabulary: pollinate: 授粉

**[8234.60s] English:** It means that the insects can see the color.  
**Translation:** 

**[8237.54s] English:** It adds a question.  
**Translation:** 

**[8238.98s] English:** Does this aesthetic sense also exist in lower forms?  
**Translation:** 

**[8242.84s] English:** Why is it aesthetic?  
**Translation:** Vocabulary: aesthetic: 审美

**[8244.48s] English:** All kinds of interesting questions,  
**Translation:** 

**[8246.46s] English:** which the science knowledge only adds to the excitement,  
**Translation:** 

**[8249.20s] English:** the mystery,  
**Translation:** 

**[8250.70s] English:** and the awe of a flower.  
**Translation:** 

**[8252.94s] English:** It only adds.  
**Translation:** 

**[8256.38s] English:** All right, back to David Foster Wallace's speech.  
**Translation:** Vocabulary: foster: 培养

**[8259.74s] English:** He has a great story in there that I particularly enjoy.  
**Translation:** 

**[8265.22s] English:** It goes,  
**Translation:** 

**[8266.82s] English:** There are these two guys sitting together in a bar  
**Translation:** 

**[8269.50s] English:** in the remote Alaskan wilderness.  
**Translation:** Vocabulary: alaskan: 阿拉斯加的; wilderness: 荒野

**[8271.78s] English:** One of the guys is religious.  
**Translation:** 

**[8273.66s] English:** The other is an atheist.  
**Translation:** Vocabulary: atheist: 无神论者

**[8275.58s] English:** And the two are arguing about the existence of God  
**Translation:** 

**[8278.52s] English:** with the people of Alaska.  
**Translation:** 

**[8279.08s] English:** And the other is an atheist.  
**Translation:** 

**[8279.18s] English:** And that's special.  
**Translation:** 

**[8280.00s] English:** intensity that comes after about the fourth beer. And the atheist says, look, it's not like I don't  
**Translation:** 

**[8285.70s] English:** have actual reasons for not believing in God. It's not like I haven't ever experimented with  
**Translation:** 

**[8291.44s] English:** the whole God and prayer thing. Just last month, I got caught away from the camp in that terrible  
**Translation:** 

**[8297.70s] English:** blizzard. And I was totally lost. And I couldn't see a thing. And it was 50 below. And so I tried  
**Translation:** Vocabulary: blizzard: 暴风雪

**[8305.18s] English:** it. I fell to my knees in the snow and cried out, oh God, if there is a God, I'm lost in this  
**Translation:** 

**[8311.16s] English:** blizzard. And I'm going to die if you don't help me. And now back in the bar, the religious guy  
**Translation:** 

**[8317.34s] English:** looks at the atheist all puzzled. Well, then you must believe now, he says. After all, there you  
**Translation:** 

**[8323.82s] English:** are, alive. The atheist just rolls his eyes. No, man. All that happened was a couple of Eskimos  
**Translation:** Vocabulary: eskimos: 因纽特人

**[8330.96s] English:** happened to be wandering by and show me the way back to the camp.  
**Translation:** 

**[8336.16s] English:** All this, I think, teaches us that everything is a matter of perspective and that wisdom may arrive  
**Translation:** 

**[8343.30s] English:** if we have the humility to keep shifting and expanding our perspective on the world.  
**Translation:** 

**[8350.96s] English:** Thank you for allowing me to talk a bit about David Foster Wallace.  
**Translation:** Vocabulary: humility: 谦逊; shifting: 转变

**[8354.62s] English:** He's one of my favorite writers and he's a beautiful soul.  
**Translation:** 

**[8360.02s] English:** If I may, one more thing I wanted to briefly comment on.  
**Translation:** 

**[8363.72s] English:** I find myself to be in the middle of a world where I'm not alone. I find myself to be in  
**Translation:** 

**[8365.16s] English:** this strange position of getting attacked online often from all sides, including being lied about  
**Translation:** 

**[8372.76s] English:** sometimes through selective misrepresentation, but often through downright lies. I don't know  
**Translation:** 

**[8378.58s] English:** how else to put it. This all breaks my heart, frankly. But I've come to understand that it's  
**Translation:** Vocabulary: selective: 挑拣的

**[8384.92s] English:** the way of the internet and the cost of the path I've chosen. There's been days when it's been  
**Translation:** 

**[8390.60s] English:** rough on me mentally. It's not fun being lied about.  
**Translation:** 

**[8395.16s] English:** Especially when it's about things that are usually, for a long time, have been a  
**Translation:** 

**[8400.00s] English:** source of happiness and joy for me. But again, that's life. I'll continue exploring the world  
**Translation:** 

**[8406.38s] English:** of people and ideas with empathy and rigor, wiring my heart on my sleeve as much as I can.  
**Translation:** 

**[8414.18s] English:** For me, that's the only way to live. Anyway, a common attack on me is about my time at MIT  
**Translation:** Vocabulary: empathy: 同理心; rigor: 严谨

**[8421.40s] English:** and Drexel, two great universities I love and have tremendous respect for.  
**Translation:** 

**[8426.70s] English:** Since a bunch of lies have accumulated online about me on these topics, to a sad and at times  
**Translation:** Vocabulary: accumulated: 累积; drexel: 德雷塞尔大学

**[8433.46s] English:** hilarious degree, I thought I would once more state the obvious facts about my bio  
**Translation:** 

**[8438.10s] English:** for the small number of you who may care. TLGR, two things. First, as I say often,  
**Translation:** 

**[8445.76s] English:** including in a recent podcast episode that somehow was listened to by many millions of people,  
**Translation:** 

**[8451.52s] English:** I proudly went to Drexel University for my bachelor's, master's,  
**Translation:** 

**[8456.64s] English:** and master's degrees. I went to the University of New York for my bachelor's,  
**Translation:** 

**[8456.68s] English:** master's, and master's degrees. I went to the University of New York for my bachelor's,  
**Translation:** 

**[8456.70s] English:** and doctorate degrees. Second, I am a research scientist at MIT and have been there in a paid  
**Translation:** 

**[8464.80s] English:** research position for the last 10 years. Allow me to elaborate a bit more on these two things now,  
**Translation:** Vocabulary: elaborate: 详细说明

**[8471.68s] English:** but please skip if this is not at all interesting. So like I said, a common attack on me is that  
**Translation:** 

**[8478.04s] English:** I have no real affiliation with MIT. The accusation, I guess, is that I'm falsely  
**Translation:** Vocabulary: accusation: 指控; affiliation: 关联; falsely: 虚假地

**[8484.36s] English:** claiming an MIT affiliation because I'm not an MIT student. So I'm not an MIT student.  
**Translation:** 

**[8486.68s] English:** I'm not an MIT student because I taught a lecture there once. Nope, that accusation against me  
**Translation:** 

**[8492.66s] English:** is a complete lie. I have been at MIT for over 10 years in a paid research position from 2015  
**Translation:** 

**[8502.04s] English:** to today. To be extra clear, I'm a research scientist at MIT working in LIDS, the Laboratory  
**Translation:** 

**[8511.00s] English:** for Information and Decision Systems in the College of Computing. For now, I'm going to  
**Translation:** 

**[8516.66s] English:** since I'm still at MIT.  
**Translation:** Vocabulary: computing: 计算机科学

**[8520.00s] English:** You can see me in the directory and on the various lab pages.  
**Translation:** 

**[8525.36s] English:** I have indeed given many lectures at MIT over the years, a small fraction of which I posted online.  
**Translation:** 

**[8533.24s] English:** Teaching, for me, always has been just for fun and not part of my research work.  
**Translation:** 

**[8538.08s] English:** I personally think I suck at it, but I have always learned and grown from the experience.  
**Translation:** 

**[8543.60s] English:** It's like Feynman spoke about, if you want to understand something deeply, it's good to try to teach it.  
**Translation:** 

**[8552.52s] English:** But, like I said, my main focus has always been on research.  
**Translation:** Vocabulary: feynman: 费曼

**[8555.98s] English:** I published many peer-reviewed papers that you can see in my Google Scholar profile.  
**Translation:** 

**[8562.04s] English:** For my first four years at MIT, I worked extremely intensively.  
**Translation:** Vocabulary: intensively: 刻苦地

**[8567.68s] English:** Most weeks were 80-100 hour work weeks.  
**Translation:** 

**[8570.64s] English:** After that, in 2019, I still kept my research.  
**Translation:** 

**[8573.60s] English:** I split my time taking a leap to pursue projects in AI and robotics outside MIT, and to dedicate a lot of focus to the podcast.  
**Translation:** 

**[8583.32s] English:** As I've said, I've been continuously surprised just how many hours preparing for an episode takes.  
**Translation:** 

**[8589.88s] English:** There are many episodes of the podcast for which I have to read, write, and think for 100, 200 or more hours across multiple weeks and months.  
**Translation:** 

**[8599.66s] English:** Since 2020, I have not actively published research papers.  
**Translation:** 

**[8603.60s] English:** Just like the podcast, I think it's something that's a serious full-time effort.  
**Translation:** 

**[8610.28s] English:** But, not publishing and doing full-time research has been eating at me.  
**Translation:** 

**[8615.66s] English:** Because I love research, and I love programming and building systems that test out interesting technical ideas, especially in the context of human AI or human-robot interaction.  
**Translation:** 

**[8628.22s] English:** I hope to change this in the coming months and years.  
**Translation:** 

**[8632.12s] English:** What I've come to realize about myself is that I'm not just a human being.  
**Translation:** 

**[8633.32s] English:** What I've come to realize about myself is that if I don't publish or if I don't launch systems that people use, I definitely feel like I'm not a human being.  
**Translation:** 

**[8640.00s] English:** like a piece of me is missing.  
**Translation:** 

**[8642.30s] English:** It legitimately is a source of happiness for me.  
**Translation:** Vocabulary: legitimately: 确实地

**[8646.14s] English:** Anyway, I'm proud of my time at MIT.  
**Translation:** 

**[8648.72s] English:** I was and am constantly surrounded  
**Translation:** 

**[8652.14s] English:** by people much smarter than me, many of whom  
**Translation:** 

**[8654.96s] English:** have become lifelong colleagues and friends.  
**Translation:** 

**[8658.82s] English:** MIT is a place I go to escape the world,  
**Translation:** 

**[8661.94s] English:** to focus on exploring fascinating questions  
**Translation:** 

**[8664.40s] English:** at the cutting edge of science and engineering.  
**Translation:** 

**[8667.14s] English:** This, again, makes me truly happy.  
**Translation:** 

**[8670.30s] English:** And it does hit pretty hard on a psychological level  
**Translation:** 

**[8674.84s] English:** when I'm getting attacked over this.  
**Translation:** 

**[8678.32s] English:** Perhaps I'm doing something wrong.  
**Translation:** 

**[8680.36s] English:** If I am, I will try to do better.  
**Translation:** 

**[8683.86s] English:** In all this discussion of academic work,  
**Translation:** 

**[8686.26s] English:** I hope you know that I don't ever  
**Translation:** 

**[8688.58s] English:** mean to say that I'm an expert at anything.  
**Translation:** 

**[8692.20s] English:** In the podcast and in my private life,  
**Translation:** 

**[8695.20s] English:** I don't claim to be smart.  
**Translation:** 

**[8697.10s] English:** In fact, I often call myself an idiot and mean it.  
**Translation:** 

**[8702.24s] English:** I try to make fun of myself as much as possible  
**Translation:** 

**[8704.76s] English:** and in general to celebrate others instead.  
**Translation:** 

**[8709.10s] English:** Now to talk about Drexel University, which I also love  
**Translation:** 

**[8713.18s] English:** and am proud of and am deeply grateful for my time there.  
**Translation:** Vocabulary: drexel: 德雷塞尔大学

**[8718.04s] English:** As I said, I went to Drexel for my bachelors, masters,  
**Translation:** 

**[8720.98s] English:** and doctorate degrees in computer science  
**Translation:** Vocabulary: bachelors: 学士学位

**[8723.56s] English:** and electrical engineering.  
**Translation:** 

**[8726.26s] English:** I've talked about Drexel.  
**Translation:** 

**[8726.84s] English:** Drexel many times, including, as I mentioned at the end of a recent podcast, the Donald Trump  
**Translation:** 

**[8733.50s] English:** episode, funny enough, that was listened to by many millions of people, where I answered a  
**Translation:** 

**[8739.16s] English:** question about graduate school and explained my own journey at Drexel and how grateful I am for it.  
**Translation:** 

**[8746.26s] English:** If it's at all interesting to you, please go listen to the end of that episode or  
**Translation:** 

**[8750.10s] English:** watch the related clip. At Drexel, I met and worked with many brilliant researchers and mentors  
**Translation:** 

**[8756.62s] English:** from whom I've learned a lot about engineering.  
**Translation:** 

**[8760.00s] English:** science, and life. There are many valuable things I gained from my time at Drexel.  
**Translation:** 

**[8765.06s] English:** First, I took a large number of very difficult math and theoretical computer science courses.  
**Translation:** 

**[8770.42s] English:** They taught me how to think deeply and rigorously, and also how to work hard and not give up,  
**Translation:** 

**[8776.12s] English:** even if it feels like I'm too dumb to find a solution to a technical problem.  
**Translation:** Vocabulary: rigorously: 严谨地

**[8781.48s] English:** Second, I programmed a lot during that time, mostly C, C++. I programmed robots,  
**Translation:** 

**[8787.44s] English:** optimization algorithms, computer vision systems, wireless network protocols,  
**Translation:** Vocabulary: optimization: 优化; wireless: 无线

**[8792.64s] English:** multimodal machine learning systems, and all kinds of simulations of physical systems.  
**Translation:** 

**[8797.64s] English:** This is where I really developed a love for programming, including, yes, Emacs and the  
**Translation:** Vocabulary: emacs: 编辑器; multimodal: 多模态

**[8806.44s] English:** Kinesis keyboard. I also, during that time, read a lot. I played a lot of guitar, wrote a lot of  
**Translation:** 

**[8814.86s] English:** poetry, and, uh,  
**Translation:** 

**[8817.44s] English:** trained a lot of, uh, in Judo and Jiu-Jitsu, which I cannot sing enough praises to. Jiu-Jitsu humbled  
**Translation:** 

**[8824.92s] English:** me on a daily basis throughout my 20s, and it still does to this very day whenever I get a chance  
**Translation:** Vocabulary: cannot: 不能

**[8830.94s] English:** to train. Anyway, I hope that the folks who occasionally get swept up in the chanting online  
**Translation:** 

**[8837.60s] English:** crowds that want to tear down others don't lose themselves in it too much. In the end, I still  
**Translation:** Vocabulary: chanting: 诵念

**[8844.80s] English:** think there's more good than bad.  
**Translation:** 

**[8847.44s] English:** In people.  
**Translation:** 

**[8848.92s] English:** But, we're all, each of us, a mixed bag. I know I am very much flawed. I speak awkwardly. I sometimes  
**Translation:** 

**[8857.66s] English:** say stupid shit. I can get irrationally emotional. I can be too much of a dick when I should be kind.  
**Translation:** Vocabulary: awkwardly: 局促不安; irrationally: 不合逻辑

**[8864.48s] English:** I can lose myself in a biased rabbit hole before I wake up to the bigger, more accurate picture of  
**Translation:** 

**[8870.38s] English:** reality. I'm human. And so are you. For better or for worse.  
**Translation:** 

**[8877.44s] English:** And, I do still believe.  
**Translation:** 

**[8879.68s] English:** I'm human. And so are you. For better or for worse.  
**Translation:** 

**[8880.00s] English:** We're in this whole beautiful mess together.  
**Translation:** 

**[8883.78s] English:** I love you all.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
