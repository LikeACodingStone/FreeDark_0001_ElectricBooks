# Podcast vocabulary notes
Source file: Lex Fridman - Jensen Huang： NVIDIA - The $4 Trillion Company & the AI Revolution ｜ Lex Fridman Podcast #494.opus
Improved subtitle: punctuation and vocabulary regenerated from current config.

**[0.00s] English:** The following is a conversation with Jensen Huang, CEO of NVIDIA, one of the most important  
**Translation:** 

**[6.72s] English:** And NVIDIA is one of the most influential companies in the history of human civilization, as the engine powering the AI revolution.  
**Translation:** Vocabulary: huang: 黄; influential: 有影响力的

**[13.32s] English:** Revolution, and a lot of its success can be directly attributed to Jensen's sheer force of will.  
**Translation:** 

**[19.00s] English:** Will and his many brilliant bets and decisions as a leader, engineer, and innovator. This is  
**Translation:** Vocabulary: attributed: 归因; innovator: 创新者

**[27.06s] English:** Alex Friedman Podcast, and now, dear friends: here's Jensen Huang.  
**Translation:** 

**[33.08s] English:** You've propelled NVIDIA into a new era in AI, moving beyond its focus on chip-scale design to  
**Translation:** Vocabulary: friedman: 弗里德曼; propelled: 推动

**[40.36s] English:** Now, rack-scale design. And I think it's fair to say that winning for NVIDIA for a long time has used  
**Translation:** 

**[46.00s] English:** To be about building the best GPU possible, and you still do. But now you've expanded that to  
**Translation:** 

**[51.64s] English:** Extreme Co-Design of GPU, CPU, Memory, Networking, Storage, Power, Cooling,  
**Translation:** 

**[57.06s] English:** Software, the rack itself, the pod that you've announced, and even the data center.  
**Translation:** 

**[62.14s] English:** So, let's talk about extreme co-design. What is the hardest part of co-designing a system with?  
**Translation:** 

**[67.42s] English:** That involves many complex components and design variables, right? Yeah, thanks for that question. So, firstly,  
**Translation:** Vocabulary: firstly: 首先

**[73.66s] English:** The reason why extreme co-design is necessary is because the problem no longer fits inside.  
**Translation:** 

**[79.02s] English:** One computer to be accelerated by one GPU. The problem that you're trying to solve is: you would  
**Translation:** 

**[87.06s] English:** Like going faster than the number of computers you add. So, if you added, say, 10,000...  
**Translation:** 

**[93.52s] English:** Computers, but you would like it to go a million times faster. Then all of a sudden, you have to.  
**Translation:** 

**[100.94s] English:** Take the algorithm; you have to break it up, refactor it, and then proceed.  
**Translation:** 

**[107.04s] English:** Shard the pipeline; you have to shard the data, you have to shard the model. Now, all of a sudden,  
**Translation:** Vocabulary: algorithm: 算法; pipeline: 流程; refactor: 重构; shard: 分片

**[112.98s] English:** When you distribute the problem this way, not just,...  
**Translation:** 

**[117.06s] English:** Scaling up the problem, but you're distributing the problem.  
**Translation:** Vocabulary: distributing: 分配

**[120.00s] English:** Then everything gets in the way. This is the Amdahl's Law problem, where the amount of speed-up achievable by parallel computing is limited by the time needed for the sequential portion of an application to execute.  
**Translation:** 

**[126.74s] English:** Up, what you have for something depends on how much of the total workload it is. And so if computation,...  
**Translation:** Vocabulary: achievable: 可实现的; computation: 计算; computing: 计算; execute: 执行; parallel: 并行; sequential: 顺序; workload: 工作负载

**[134.20s] English:** Represents 50% of the problem, and I sped up computation infinitely, like a million times.  
**Translation:** 

**[142.96s] English:** I only sped up the total workload by a factor of two. Now, all of a sudden, not only do you have  
**Translation:** Vocabulary: infinitely: 无限地

**[149.54s] English:** To distribute the computation, you have to, you know, shard the pipeline somehow, and you also have  
**Translation:** 

**[155.74s] English:** To solve the networking problem, because you've got all of these computers and they're all connected.  
**Translation:** 

**[160.62s] English:** Together. And so, at the scale that we do distributed computing, the CPU is a problem; the GPU,  
**Translation:** 

**[168.62s] English:** Is a problem; the networking is a problem; the switching is a problem. And distributing the  
**Translation:** 

**[174.18s] English:** Workload across all these computers is a problem. It's just a massively complex.  
**Translation:** 

**[179.36s] English:** Computation.  
**Translation:** Vocabulary: massively: 极其

**[179.54s] English:** And so we just have to bring every technology to bear. Otherwise, we scale up linearly.  
**Translation:** 

**[187.56s] English:** Or we scale up based on the capabilities of Moore's Law, which has largely slowed because  
**Translation:** Vocabulary: capabilities: 能力

**[194.94s] English:** Dennard scaling has slowed. I'm sure there are trade-offs there. Plus, you have a complete  
**Translation:** 

**[199.32s] English:** Disparate disciplines here. I'm sure you have specialists in each one of these high-bandwidth areas.  
**Translation:** Vocabulary: dennard: Dennard缩放; disciplines: 学科; disparate: 不同的

**[203.92s] English:** Memory, the network, and the NVLink; the NICs, the optics, and the copper that you're doing.  
**Translation:** 

**[208.96s] English:** The power delivery.  
**Translation:** Vocabulary: copper: 铜; optics: 光学

**[209.54s] English:** The cooling is all that. I mean, there are like world experts in each of those. How do you?  
**Translation:** 

**[213.48s] English:** Get them in a room together to figure out why my staff is so large?  
**Translation:** 

**[217.56s] English:** What's the product? Can you take me through the process of the specialists and the journalists?  
**Translation:** 

**[222.18s] English:** Like, how do you put together the rack when you know what set of things you have?  
**Translation:** 

**[226.36s] English:** To shove into a rack together? Yeah, like, what does that process look like of designing?  
**Translation:** 

**[230.54s] English:** Is it all together?  
**Translation:** Vocabulary: shove: 硬塞

**[231.26s] English:** There's the first question, which is "What is extreme co-design?" You were optimizing.  
**Translation:** 

**[236.88s] English:** Across the entire stack of software.  
**Translation:** Vocabulary: optimizing: 优化

**[238.88s] English:** Yeah.  
**Translation:** 

**[239.88s] English:** And so you're like, "Oh, okay," because I, you know, I don't like to go out there and  
**Translation:** 

**[240.00s] English:** To chips, to systems, to system software, to the algorithms, to the applications. That's  
**Translation:** 

**[240.88s] English:** Get, like, I'm not like, I'm really into it. But if I go in and I'm like, "I want to go.  
**Translation:** 

**[241.88s] English:** To every store and look at it, you know—I'm really into it. Yeah.  
**Translation:** 

**[242.00s] English:** Yeah.  
**Translation:** 

**[242.08s] English:** And so, you have a lot of different recording systems that you guys have to deal with.  
**Translation:** 

**[242.86s] English:** Got to choose, like in the office; you've got to, I've got to, some kind of domain.  
**Translation:** 

**[243.56s] English:** Explanation: To do it.  
**Translation:** 

**[243.80s] English:** Right.  
**Translation:** 

**[243.84s] English:** Yeah.  
**Translation:** 

**[243.98s] English:** I'll show you how you could do that.  
**Translation:** 

**[244.18s] English:** All right.  
**Translation:** 

**[244.22s] English:** Cool.  
**Translation:** 

**[244.36s] English:** So, then, I don't want this one to end up.  
**Translation:** 

**[244.44s] English:** Yeah, no, I've got this.  
**Translation:** 

**[244.66s] English:** One layer. The second thing that you and I just talked about goes beyond CPUs and GPUs and  
**Translation:** 

**[244.68s] English:** Let's see.  
**Translation:** 

**[244.80s] English:** Okay.  
**Translation:** 

**[244.96s] English:** All right.  
**Translation:** 

**[245.04s] English:** Okay.  
**Translation:** 

**[245.10s] English:** So, here's what I would like to do.  
**Translation:** 

**[250.76s] English:** Networking chips, and scale-up switches and scale-out switches. And then, of course, you've  
**Translation:** 

**[256.10s] English:** Got to include power and cooling and all of that because, you know, all these computers are.  
**Translation:** 

**[262.18s] English:** Extremely power-hungry. They do a lot of work, and they're very energy-efficient.  
**Translation:** 

**[268.08s] English:** But they, in aggregate, still consume a lot of power. And so that's one. The first question is:  
**Translation:** Vocabulary: aggregate: 总体

**[273.18s] English:** What is it? The second question is, why is it? And we just spoke about the reason, you know.  
**Translation:** 

**[278.50s] English:** You want to distribute the workloads so that you can exceed the benefit of just increasing the.  
**Translation:** Vocabulary: exceed: 超过; workloads: 工作负载

**[285.58s] English:** Number of computers. And then the third question is: how is it? How do you do it? And that's kind.  
**Translation:** 

**[294.26s] English:** Of the miracle of this company. You know, when you're designing a computer, you have  
**Translation:** 

**[298.02s] English:** To have a lot of power. And so that's one. The second question is: why is it? And we just spoke.  
**Translation:** 

**[298.06s] English:** To have an operating system for computers. When you're designing a company, you should first  
**Translation:** 

**[303.14s] English:** Think about what it is that you want the company to produce. You know, I see a lot of companies  
**Translation:** 

**[307.40s] English:** Organization charts, and they all look the same. Hamburger organization charts, software organization.  
**Translation:** 

**[312.76s] English:** Charts, and car company organization charts, all look the same. And it doesn't make any sense.  
**Translation:** 

**[317.22s] English:** To me, you know, the goal of a company is to be the machinery, the mechanism, the system that  
**Translation:** Vocabulary: machinery: 机器

**[323.94s] English:** Produces the output, and that output is the product of the company. And that output is the  
**Translation:** 

**[328.04s] English:** That we would like to create. It is also designed; the architecture of the company should reflect...  
**Translation:** 

**[333.26s] English:** The environment in which it exists. It almost directly says what you should do with the.  
**Translation:** 

**[339.14s] English:** Organization. My direct staff is 60 people. You know, I don't have one-on-one meetings with them.  
**Translation:** 

**[345.04s] English:** Because it's impossible. You can't have 60 people on your staff if you're, you know,  
**Translation:** 

**[349.94s] English:** Going to get work done. So, you still have 60 reports. You still have more. Yeah.  
**Translation:** 

**[353.78s] English:** More. Yeah. And most stars, at least have a  
**Translation:** 

**[357.98s] English:** Foot in Engineering. Almost.  
**Translation:** 

**[360.00s] English:** All of them: there are experts in memory, experts in CPUs, and experts in optical technology.  
**Translation:** 

**[366.40s] English:** Yeah, GPUs and architecture, algorithms, and design—so you constantly have an eye on the entire stack.  
**Translation:** Vocabulary: optical: 光学的

**[373.70s] English:** And you're having intense discussions about the design of the entire set, and no conversation.  
**Translation:** 

**[379.42s] English:** Is there ever one person? That's why I don't do one-on-ones. We present a problem, and all of us...  
**Translation:** 

**[385.46s] English:** Attack it, you know, because we're doing extreme code design, and literally the company is doing  
**Translation:** 

**[391.26s] English:** Extreme code design all the time, so even if you're talking about a particular component,...  
**Translation:** 

**[395.54s] English:** Like cooling, networking; everybody's listening in, yeah, and they can contribute. Well, this doesn't.  
**Translation:** 

**[402.96s] English:** Work for the power distribution. This doesn't exactly work for the power distribution.  
**Translation:** 

**[407.08s] English:** The memory: this doesn't work for this, exactly. And whoever wants to tune out, feel free to do so.  
**Translation:** 

**[413.48s] English:** Yeah, and the reason for that is because  
**Translation:** 

**[415.18s] English:** Because the people on the staff know when to pay attention; they're supposed to.  
**Translation:** 

**[420.10s] English:** You know, something they could have contributed to, they didn't contribute to. I'm going to call  
**Translation:** 

**[423.68s] English:** They're out, you know, and so hey, come on, let's get in here. So, as you mentioned in the videos, this company...  
**Translation:** 

**[429.52s] English:** Is adapting to the environment, so at which point can you say that the environment changed and you began?  
**Translation:** Vocabulary: adapting: 适应

**[435.64s] English:** Began adapting, sort of secretly, in the early days, from GPU for gaming, maybe the early deep.  
**Translation:** 

**[443.68s] English:** Learning Revolution: We're now going to be part of the early deep learning revolution.  
**Translation:** 

**[445.16s] English:** Early days, from GPU for gaming, maybe the early deep learning revolution, and we're now going to start.  
**Translation:** 

**[445.78s] English:** Thinking of it as an AI factory, what does NVIDIA do? It produces AI. Let's build a factory.  
**Translation:** 

**[450.70s] English:** I could, you could, I could reason through it just systematically. Um, we started out as an accelerator.  
**Translation:** 

**[457.64s] English:** Company, but the problem with accelerators is that the application domain is too narrow; it has the  
**Translation:** Vocabulary: accelerator: 加速器; accelerators: 加速器

**[463.52s] English:** The benefit of being incredibly optimized for the job—you know, any specialist has that benefit.  
**Translation:** 

**[470.02s] English:** The problem with intense specialization is that, of course, your market reach can suffer.  
**Translation:** Vocabulary: optimized: 优化

**[475.16s] English:** Is it narrower, but that's okay. The problem is...  
**Translation:** 

**[480.00s] English:** The market size also dictates your R&D capacity, and your R&D capacity ultimately dictates the influence and impact that you can possibly have in computing.  
**Translation:** Vocabulary: computing: 计算; dictates: 决定; narrower: 更窄

**[494.34s] English:** And so, when we first started out as an accelerator, a very specific one, we always knew that would be our first step.  
**Translation:** 

**[502.70s] English:** We had to find a way to become an accelerated computing solution.  
**Translation:** Vocabulary: accelerated: 加速的

**[505.78s] English:** But the problem is, when you become a computing company, it's too general-purpose, and it takes away from your specialization.  
**Translation:** 

**[513.40s] English:** I connected two words that actually have fundamental tension.  
**Translation:** 

**[519.44s] English:** The better computing company we become, the worse we become as a specialist.  
**Translation:** 

**[523.68s] English:** The more specialized we become, the less capacity we have for overall computing.  
**Translation:** 

**[529.22s] English:** And I connected those two words together on purpose.  
**Translation:** 

**[532.70s] English:** That the company has to find that really narrow path, step by step by step, to expand our aperture of computing, but not give up on the most important specialization that we had.  
**Translation:** Vocabulary: aperture: 视野

**[546.72s] English:** Okay, so the first step that we took beyond acceleration was to invent the programmable pixel shader.  
**Translation:** 

**[553.00s] English:** So, that was the first step towards programmability.  
**Translation:** Vocabulary: pixel: 像素; shader: 着色器

**[556.62s] English:** You know, it was our first journey toward moving into the world of computing.  
**Translation:** 

**[560.58s] English:** The second thing that we did was we....  
**Translation:** Vocabulary: computing: 计算

**[562.70s] English:** We created and put FP32 into our shaders.  
**Translation:** 

**[567.86s] English:** That FP32 step, IEEE-compatible FP32, was a huge step in the direction of computing.  
**Translation:** Vocabulary: shaders: 着色器

**[576.46s] English:** It was the reason why all of the people who were working on stream processors and other types of data flow processors discovered us.  
**Translation:** 

**[586.32s] English:** And they said, "Hey, all of a sudden, you know, we might be able to use this GPU that's incredibly computationally intensive.  
**Translation:** Vocabulary: computationally: 计算上; processors: 处理器

**[591.98s] English:** And it's now.  
**Translation:** 

**[593.24s] English:** You know, it's compliant with IEEE.  
**Translation:** Vocabulary: compliant: 符合要求的

**[594.84s] English:** I can take the software that I was writing previously for CPUs and I can...  
**Translation:** 

**[600.00s] English:** You know, seeing about using the GPU for them and which led us to create Put C.  
**Translation:** 

**[607.24s] English:** On top of FP32, we called it CG. That CG path took us to eventually CUDA, step by step.  
**Translation:** 

**[616.14s] English:** Step, um, uh, with well, putting CUDA on G-Force—that was a strategic decision that was very, very  
**Translation:** 

**[624.00s] English:** It's hard to do because it costs the company enormous amounts of our profits, and we couldn't afford it.  
**Translation:** 

**[629.80s] English:** At the time, but we did it anyway because we wanted to be a computing company.  
**Translation:** 

**[635.30s] English:** The company's computing architecture must be compatible across all of  
**Translation:** 

**[641.14s] English:** The chips that we build, can you take me through that decision? So, putting CUDA on G-Force could...  
**Translation:** Vocabulary: compatible: 兼容的; computing: 计算

**[645.44s] English:** Not afford to do? Can you explain that decision? Why, why did you boldly choose to do that anyway? Yeah, you.  
**Translation:** 

**[652.42s] English:** Explain that, excellent—that was the first. I would say that was the first, um,  
**Translation:** Vocabulary: boldly: 勇敢地

**[659.80s] English:** The first strategic decision that is as close to an existential threat for those who don't know  
**Translation:** 

**[667.78s] English:** It turned out to be (spoiler alert) one of the most incredibly brilliant decisions ever made by a  
**Translation:** Vocabulary: spoiler: 剧透

**[675.04s] English:** Company, so CUDA turned out to be an incredible foundation for computation, uh, in this AI.  
**Translation:** 

**[681.70s] English:** Infrastructure world: So, you're just setting the context. It turned out to be a good decision.  
**Translation:** Vocabulary: computation: 计算

**[687.12s] English:** Yeah, it turned out to have been a good decision, I think.  
**Translation:** 

**[689.80s] English:** So, here's the way it went: We invented this thing called CUDA, and it expanded the  
**Translation:** 

**[696.30s] English:** The aperture of applications that we can accelerate with our accelerator: the question is...  
**Translation:** 

**[702.90s] English:** How do we attract developers to CUDA, because a computing platform is all about  
**Translation:** Vocabulary: accelerate: 加速; accelerator: 加速器; aperture: 通路

**[710.30s] English:** Developers and developers don't come to a computing platform just because you know it.  
**Translation:** 

**[718.32s] English:** Could perform something interesting, and they don't come to a computing platform just because.  
**Translation:** 

**[719.80s] English:** They're inputters, just because they want to change it if you know what they think the information is.  
**Translation:** 

**[720.00s] English:** They come to a computing platform because the install base is large, because a developer likes  
**Translation:** Vocabulary: inputters: 输入者

**[725.40s] English:** Anybody else wants to develop software that reaches a lot of people, so the install base?  
**Translation:** 

**[725.74s] English:** The approach is if it's classical information and they can appreciate all kinds of information.  
**Translation:** 

**[730.14s] English:** Is, in fact, the single most important part of an architecture; the architecture could attract.  
**Translation:** 

**[732.32s] English:** And toggles and stuff like that, so, um, I think it's really important to differentiate.  
**Translation:** Vocabulary: differentiate: 区分; toggles: 切换按钮

**[736.42s] English:** Enormous amounts of criticism, for example; no architecture has ever attracted more.  
**Translation:** 

**[737.96s] English:** Between what may come out as information and what may not, create something that is  
**Translation:** 

**[742.30s] English:** Ommen meant to be, and so I'm just going to go ahead and run through some statements overall.  
**Translation:** 

**[743.12s] English:** Than the x86, you know, as a less-than-elegant architecture, but it is the  
**Translation:** 

**[747.34s] English:** Today, let's try something we've talked about a lot. The first thing we want to do is toücht.  
**Translation:** 

**[749.12s] English:** Through saved to avoid collusion with the inflation, right? So if you're doing something like your company or  
**Translation:** Vocabulary: collusion: 勾结; inflation: 通货膨胀

**[751.52s] English:** Defining the architecture of today, it gives you an example that in fact, so many risk architectures.  
**Translation:** 

**[757.84s] English:** Which were beautifully architectured, incredibly well-designed by some of the brightest computer experts.  
**Translation:** Vocabulary: architectured: 精心设计的

**[765.48s] English:** Scientists in the world largely failed, and so I've given you two examples where one is, you know,  
**Translation:** 

**[772.14s] English:** One is elegant.  
**Translation:** Vocabulary: elegant: 优雅的

**[773.06s] English:** One is elegant.  
**Translation:** 

**[773.10s] English:** One is elegant.  
**Translation:** 

**[773.12s] English:** The other one's barely aesthetic, and so X86 survived — install base is everything.  
**Translation:** 

**[779.58s] English:** Base defines an architecture, not everything else is secondary, okay. And so, there were other...  
**Translation:** Vocabulary: aesthetic: 美感

**[785.92s] English:** Architectures at the time CUDA came out, OpenCL was here, and there were, you know, several others.  
**Translation:** 

**[790.88s] English:** Competing architectures, but the thing that we decided was good was that we said  
**Translation:** 

**[795.90s] English:** Hey, look; ultimately, it's about the install base, and what is the best way we could get a new  
**Translation:** 

**[803.24s] English:** Computing architecture into the world by that time frame, GeForce had become successful, and we were already...  
**Translation:** Vocabulary: computing: 计算

**[810.30s] English:** Selling millions and millions of GeForce GPUs a year, and we said, "You know, we had to put CUDA...  
**Translation:** 

**[815.86s] English:** On GeForce, and put it into every single PC, whether customers use it or not, and use it as a starting point.  
**Translation:** 

**[825.08s] English:** Point of  
**Translation:** 

**[825.90s] English:** Cultivating our install base, meanwhile, we'll go and attract developers and visit universities.  
**Translation:** Vocabulary: cultivating: 培养

**[833.70s] English:** And he wrote books, taught classes, and put CUDA everywhere, and eventually people will discover.  
**Translation:** 

**[840.00s] English:** And at the time, the PC was the primary computing vehicle.  
**Translation:** 

**[843.62s] English:** There was no cloud.  
**Translation:** 

**[844.72s] English:** And we could put a supercomputer in the hands of every researcher in school and every scientist.  
**Translation:** Vocabulary: supercomputer: 超级计算机

**[849.78s] English:** Every engineer in school, every student in school, and eventually something amazing will happen.  
**Translation:** 

**[854.78s] English:** Happen.  
**Translation:** 

**[855.58s] English:** Well, the problem was that CUDA increased our cost of that GPU, which is a consumer product.  
**Translation:** 

**[862.16s] English:** So, it was tremendously consuming, completely consuming all of the company's gross profit dollars.  
**Translation:** Vocabulary: tremendously: 巨大地

**[868.56s] English:** And so at the time, the company was probably worth, I don't know, $8 billion.  
**Translation:** 

**[877.06s] English:** Or something, $6 or $7 billion or something like that.  
**Translation:** 

**[880.22s] English:** After we launched CUDA, I recognized that it was going to add so much cost, but it was  
**Translation:** 

**[887.88s] English:** Something we believed in.  
**Translation:** 

**[890.04s] English:** Our market cap went down to about $1.5 billion.  
**Translation:** 

**[893.32s] English:** And so, we were down there for a while.  
**Translation:** 

**[896.96s] English:** And we clawed our way.  
**Translation:** 

**[898.56s] English:** Way back slowly.  
**Translation:** Vocabulary: clawed: 奋力

**[900.54s] English:** But we carried CUDA on GeForce.  
**Translation:** 

**[903.14s] English:** I always say that NVIDIA is the house that GeForce built, because it was GeForce that  
**Translation:** 

**[908.36s] English:** Took CUDA out to everyone.  
**Translation:** 

**[910.78s] English:** Researchers and scientists discovered CUDA on GeForce because they were all, you know,  
**Translation:** 

**[918.10s] English:** Many of them were gamers.  
**Translation:** 

**[919.82s] English:** Many of them built their own PCs, anyway.  
**Translation:** 

**[922.52s] English:** In a university lab, many of them built clusters themselves, using PC components.  
**Translation:** 

**[928.56s] English:** And so, you know, that's kind of how we got going.  
**Translation:** Vocabulary: clusters: 计算集群

**[931.58s] English:** And then that became the platform and foundation for the deep learning revolution.  
**Translation:** 

**[935.18s] English:** That was also another great, great observation.  
**Translation:** 

**[937.60s] English:** Yeah.  
**Translation:** 

**[937.94s] English:** That existential moment.  
**Translation:** Vocabulary: existential: 存在主义的

**[939.48s] English:** Do you remember, like, what were those meetings like?  
**Translation:** 

**[942.76s] English:** What were those discussions like, deciding as a company to risk everything?  
**Translation:** 

**[948.38s] English:** Well, I had to make it clear to the board what we were trying to do.  
**Translation:** 

**[956.04s] English:** And the management team knew our gross margins.  
**Translation:** Vocabulary: margins: 利润 margin

**[958.56s] English:** We were going to get crushed.  
**Translation:** 

**[960.00s] English:** So, you could imagine a world where GeForce would carry the burden of CUDA, and none of the gamers would appreciate it, and none of the gamers would pay for it. They only pay a certain price, and it doesn't matter what your cost is.  
**Translation:** Vocabulary: burden: 负担

**[974.54s] English:** And so we increased our cost by 50%, and we were a 35% gross margin company. And so it was quite a difficult decision to make. But you could imagine that someday this would go into workstations, and it would go into supercomputers, and in those segments, maybe we can capture more margin.  
**Translation:** 

**[997.26s] English:** So, you could reason your way into being able to afford this, but it still took a decade.  
**Translation:** Vocabulary: margin: 利润率; segments: 市场细分; supercomputers: 超级计算机; workstations: 工作站

**[1004.54s] English:** But that's more of a conversation with the board, convincing them psychologically. Because NVIDIA has continued to make bold bets that predict the future—and in part, especially now, define it. So I'm almost looking for wisdom about how you were able to make those decisions and take leaps like that as a company.  
**Translation:** 

**[1030.60s] English:** Yeah.  
**Translation:** Vocabulary: psychologically: 心理上

**[1034.54s] English:** Well, first of all, I'm driven by a lot of curiosity.  
**Translation:** 

**[1041.30s] English:** At some point, there's a reasoning system that convinces me so clearly that this outcome will happen, and this will happen.  
**Translation:** Vocabulary: convinces: 说服

**[1054.62s] English:** And so I believe it in my mind, and when I believe it, you know how it is: you manifest a future, and that future is so convincing.  
**Translation:** 

**[1064.54s] English:** And there's no way it won't happen. There's a lot of suffering in between, but you've got to believe what you believe.  
**Translation:** Vocabulary: manifest: 显现

**[1072.86s] English:** So, you envision the future.  
**Translation:** 

**[1075.48s] English:** Yeah.  
**Translation:** Vocabulary: envision: 构想

**[1075.92s] English:** And you essentially, from an engineering perspective, manifest it.  
**Translation:** 

**[1079.68s] English:** Yeah.  
**Translation:** 

**[1080.00s] English:** You reason about how to get there. You reason about why it must exist. We all reason. The management team will reason about it, and we spend a lot of time reasoning about it.  
**Translation:** 

**[1094.76s] English:** The thing that the next part of it is probably a skill thing, which is oftentimes in leadership, the leaders stay quiet or they learn about something and then do some manifesto, and it's a brand new year.  
**Translation:** Vocabulary: manifesto: 宣言; oftentimes: 经常

**[1109.96s] English:** And somehow, at the end of the year, next year, we're going to have a brand-new plan, a big, huge layoffs this way, a big, huge organizational change this way, a new mission statement, and brand-new logos—stuff like that.  
**Translation:** 

**[1123.24s] English:** I never do things that way.  
**Translation:** Vocabulary: layoffs: 裁员

**[1126.96s] English:** When I learn about something and it's starting to influence how I think, I'll make it very clear to everyone near me that this is interesting.  
**Translation:** 

**[1137.08s] English:** This is going to make a difference.  
**Translation:** 

**[1139.56s] English:** This is going to impact that.  
**Translation:** 

**[1141.70s] English:** And I reason about things step by step, by step.  
**Translation:** 

**[1144.36s] English:** Oftentimes, I've already made up my mind, but I'll take every possible opportunity, external information, new insights, and new discoveries.  
**Translation:** 

**[1152.70s] English:** New engineering revelations emerge as new milestones develop.  
**Translation:** Vocabulary: milestones: 重要节点; revelations: 新发现

**[1157.74s] English:** I'll take those opportunities, and I'll use them to shape everyone else's belief system.  
**Translation:** 

**[1165.58s] English:** And I'm doing that literally every single day.  
**Translation:** 

**[1168.72s] English:** I'm doing that with my board.  
**Translation:** 

**[1170.28s] English:** I'm doing that with my management team.  
**Translation:** 

**[1172.14s] English:** I'm doing that with my employees.  
**Translation:** 

**[1173.76s] English:** I'm trying to shape their belief system such that when I come, the day I say, "Hey, let's buy Mellanox.  
**Translation:** Vocabulary: mellanox: 美林诺克斯

**[1182.70s] English:** It's completely obvious to everybody that we absolutely should have gone all in on deep learning on the day that I said, "Hey, guys, let's go all in on deep learning.  
**Translation:** 

**[1194.10s] English:** And let me tell you why.  
**Translation:** 

**[1195.24s] English:** I've already laid down the bricks for different organizations.  
**Translation:** 

**[1200.00s] English:** Inside the company, every organization and everyone — many of the people might have heard.  
**Translation:** 

**[1206.48s] English:** Everything, most of the company, had heard here, of course, were pieces of it, and on the day that I announced,  
**Translation:** 

**[1212.98s] English:** It, um, everybody's kind of bought into many pieces of it, and in a lot of ways, I like to announce.  
**Translation:** 

**[1221.48s] English:** These things, and I imagine that the employees are kind of saying, you know, Jensen.  
**Translation:** 

**[1228.90s] English:** What took you so long? And, in fact, I've been shaping their belief system for some time.  
**Translation:** 

**[1233.80s] English:** And therefore, leadership sometimes looks like you're leading from behind, but you've been shaping.  
**Translation:** 

**[1240.28s] English:** There, you know, to the point where on the day that I declared it, a hundred percent buy-in, but that's  
**Translation:** 

**[1245.62s] English:** What you want to bring everybody along, you know, otherwise we announce something about.  
**Translation:** 

**[1250.14s] English:** Deep learning, and everybody goes, "What are you talking about?" You know, you announce something.  
**Translation:** 

**[1253.94s] English:** About, let's go all in on this thing, and your management team.  
**Translation:** 

**[1258.90s] English:** Your board, your employees, your customers—they're kind of like, "Where's this coming from?"你知道吗？  
**Translation:** 

**[1263.00s] English:** This is insane, and so so GTCT. In fact, if you go back in time and look at the keynotes,  
**Translation:** 

**[1270.08s] English:** I'm also shaping the belief system of my partners in the industry, and I'm using that to shape...  
**Translation:** Vocabulary: keynotes: keynote演讲

**[1277.84s] English:** You know, the belief system of my own employees, and so by the time I announced  
**Translation:** 

**[1283.00s] English:** Something, like for example, we just announced Grok; we've been late.  
**Translation:** 

**[1288.90s] English:** I've been talking about the stepping stones for two and a half years. You guys just go back and  
**Translation:** 

**[1294.50s] English:** Oh, my goodness! They've been talking about it for two and a half years, and so I've been laying the  
**Translation:** 

**[1299.42s] English:** Foundation, step by step, so when the time comes, you announce it; everybody's, you know, what.  
**Translation:** 

**[1303.78s] English:** Took you so long, but it's not just inside the company; you're shaping the landscape more broadly.  
**Translation:** Vocabulary: broadly: 广泛地

**[1307.42s] English:** Global landscape of innovation, like putting those ideas out there, you really are manifesting reality.  
**Translation:** 

**[1312.62s] English:** We don't build computers; we actually don't build clouds. We don't, as it turns out.  
**Translation:** Vocabulary: manifesting: 显现

**[1317.98s] English:** Computing platform companies: We don't build computers, we don't build clouds, we don't build...  
**Translation:** 

**[1318.90s] English:** Cloud companies? We don't build. Cloud companies? We don't build. Cloud companies? We don't build.  
**Translation:** Vocabulary: computing: 计算

**[1320.00s] English:** Nobody can buy anything from us. That's the weird thing. We vertically design and vertically integrate.  
**Translation:** 

**[1328.26s] English:** To design and optimize, but then we open up the entire platform at every single layer to be:  
**Translation:** Vocabulary: integrate: 整合; optimize: 优化; vertically: 纵向

**[1335.08s] English:** Integrated into other companies' products and services, as well as clouds and supercomputers, and OEM.  
**Translation:** 

**[1341.04s] English:** Computers: The amazing thing is, I can't do what I do without having convinced them first.  
**Translation:** Vocabulary: integrated: 融合; supercomputers: 超级计算机

**[1348.00s] English:** And so, most of GTC is about manifesting a future that, by the time that my product is ready,  
**Translation:** 

**[1355.82s] English:** They're going, what took you so long? Yeah. So, one of the things you've been a believer  
**Translation:** Vocabulary: believer: 信仰者

**[1362.10s] English:** For a long time, scaling laws (broadly defined) have been a topic of belief. Are you still a believer in the scaling laws?  
**Translation:** 

**[1369.62s] English:** Yeah, we have more scaling laws now. So I think you've outlined four of them with pre-training.  
**Translation:** Vocabulary: outlined: 列举

**[1374.30s] English:** Post-training, test time, and agentic scaling.  
**Translation:** 

**[1376.94s] English:** Scaling. What do you think, when you think about the future—deep future and the near-term future—?  
**Translation:** Vocabulary: agentic: 自主的

**[1384.10s] English:** What are the blockers that you're most concerned about that keep you up at night, and that you have to  
**Translation:** 

**[1389.58s] English:** Overcome challenges in order to keep scaling? Well, we can go back and reflect on  
**Translation:** 

**[1394.08s] English:** What people thought were blockers. So, in the beginning, we were the first, the pre-training.  
**Translation:** 

**[1399.90s] English:** Scaling Law. People thought, well, rightfully so, that the amount of data we have,  
**Translation:** 

**[1406.50s] English:** High-quality data, high-quality data, high-quality data, high-quality data, high-quality data,  
**Translation:** 

**[1406.92s] English:** Data that we have will limit the intelligence that we achieve. And that scaling law was an.  
**Translation:** 

**[1412.30s] English:** Important: very important scaling law. The larger the model, the corresponding amount of data increases.  
**Translation:** 

**[1417.00s] English:** Results in a better, smarter AI. And so that was pre-training. And Ilya Sutskever.  
**Translation:** Vocabulary: corresponding: 相应的

**[1424.84s] English:** Ilya said, "We're out of data, or something like that." Pre-training is over, or something like that.  
**Translation:** 

**[1429.24s] English:** The industry panicked that this is the end of AI. And, of course, that's obviously not true.  
**Translation:** Vocabulary: panicked: 恐慌

**[1436.92s] English:** We're going to keep on scaling the amount of data that we have.  
**Translation:** 

**[1440.00s] English:** Have to train with a lot of that data, which is probably going to be synthetic.  
**Translation:** Vocabulary: synthetic: 人造的

**[1444.34s] English:** And that also confused people. And what people don't realize is that they've kind of forgotten.  
**Translation:** 

**[1450.42s] English:** That most of the data we train on, teach each other with, and inform each other with,  
**Translation:** 

**[1456.42s] English:** Is synthetic. It's synthetic because it didn't come out of nature. You created it. I'm consuming.  
**Translation:** 

**[1465.14s] English:** It. I modify it, augment it. I regenerate it. Somebody else consumes it. And so we've now  
**Translation:** Vocabulary: augment: 增加; consumes: 消耗; regenerate: 再生

**[1474.32s] English:** Reached a level where AI is able to take ground truth, augment it, enhance it, and synthetically generate new data.  
**Translation:** 

**[1485.06s] English:** Generate an enormous amount of data, and that part of post-training continues to scale. And so,...  
**Translation:** Vocabulary: enhance: 提升; synthetically: 合成

**[1491.42s] English:** The amount of data that we could use that is human-generated,  
**Translation:** 

**[1495.14s] English:** Will be smaller and smaller and smaller. The amount of data that we use to train a model,...  
**Translation:** 

**[1500.82s] English:** Is going to continue to scale to the point where we're no longer limited. Training is no longer  
**Translation:** 

**[1507.82s] English:** Limited by data. It's now limited by compute. And the reason for that is most of the data is  
**Translation:** Vocabulary: compute: 计算能力

**[1512.22s] English:** Synthetic. Then, the next phase is test time. And I still remember people telling me that.  
**Translation:** 

**[1521.04s] English:** Inference: oh, yeah, that's easy. Pre-training, that's hard.  
**Translation:** Vocabulary: synthetic: 合成的

**[1525.02s] English:** Yeah.  
**Translation:** 

**[1525.12s] English:** These are giant systems that people are talking about. Inference must be easy, and so it should be.  
**Translation:** Vocabulary: inference: 推断

**[1529.70s] English:** Chips are going to be little, tiny chips. And they're not like NVIDIA's chips. Oh, those are...  
**Translation:** 

**[1534.66s] English:** Going to be complicated and expensive. And in the future, inference is going to be the biggest.  
**Translation:** 

**[1541.54s] English:** Market. And it's going to be easy. And we're going to commoditize, and everybody can build.  
**Translation:** 

**[1546.04s] English:** Their own chips. And that was always illogical to me because inference is thinking, and I think.  
**Translation:** Vocabulary: commoditize: 商品化; illogical: 不合逻辑

**[1554.14s] English:** Thinking is hard.  
**Translation:** 

**[1555.00s] English:** Thinking is way harder than reading.  
**Translation:** 

**[1560.00s] English:** It's just memorization and generalization, you know, and looking for patterns and relationships.  
**Translation:** 

**[1565.48s] English:** You're reading versus thinking, reasoning, solving problems, taking unexplored experiences,  
**Translation:** Vocabulary: generalization: 概括; memorization: 记忆; unexplored: 未探索

**[1577.22s] English:** New experiences, and breaking it down into decomposing it into, you know, solvable pieces.  
**Translation:** 

**[1583.86s] English:** That we then go off either through first-principle reasoning or, you know, through  
**Translation:** Vocabulary: decomposing: 分解; solvable: 可解决的

**[1588.72s] English:** Previous examples, prior experiences, you know, or just exploration and search, and  
**Translation:** 

**[1596.94s] English:** You know, trying different things.  
**Translation:** 

**[1598.84s] English:** And that whole process of testing, time-scaling, and inference is really about thinking.  
**Translation:** 

**[1606.84s] English:** And it's about reasoning.  
**Translation:** Vocabulary: inference: 推理

**[1608.38s] English:** It's about planning.  
**Translation:** 

**[1609.18s] English:** It's about search.  
**Translation:** 

**[1610.14s] English:** It's about, and so how could that possibly be compute-light?  
**Translation:** 

**[1614.12s] English:** And we were absolutely right about that, you know.  
**Translation:** 

**[1616.12s] English:** So, test-time scaling is intense.  
**Translation:** 

**[1618.72s] English:** Intensely compute-intensive.  
**Translation:** Vocabulary: intensely: 非常

**[1621.00s] English:** Then the question is: Okay, now we're at inference and test-time scaling.  
**Translation:** 

**[1624.44s] English:** What's beyond that?  
**Translation:** 

**[1626.02s] English:** Well, obviously, we have now created, you know, one agentic person.  
**Translation:** 

**[1632.48s] English:** And that one agentic person has a large language model that we've now, you know, developed.  
**Translation:** Vocabulary: agentic: 有自主性的

**[1638.28s] English:** But during test time, that agentic system goes off and does research and bangs on databases.  
**Translation:** 

**[1644.84s] English:** And it goes and, you know, uses tools.  
**Translation:** Vocabulary: databases: 数据库

**[1647.94s] English:** And one of the most important things about test-time scaling is that it's not just a  
**Translation:** 

**[1648.70s] English:** Single agent.  
**Translation:** 

**[1648.74s] English:** One of the most important things it does is spin off and spawn off a whole bunch of  
**Translation:** 

**[1652.10s] English:** Sub-agents, which means we're now creating large teams.  
**Translation:** Vocabulary: spawn: 繁殖

**[1656.34s] English:** It's so much easier to scale NVIDIA by hiring more employees than it is to scale myself.  
**Translation:** 

**[1664.12s] English:** And so the next scaling law is the agentic scaling law.  
**Translation:** 

**[1666.96s] English:** It's kind of like multiplying AI.  
**Translation:** 

**[1671.62s] English:** Multiplying AI, we could spin off agents as fast as you want to spin off agents.  
**Translation:** Vocabulary: multiplying: 增加

**[1675.56s] English:** And so, you know, I have four scaling laws.  
**Translation:** 

**[1678.70s] English:** And I'm going to show you how to do that in just a moment.  
**Translation:** 

**[1680.00s] English:** And as we use agency systems, they're going to create a lot more data.  
**Translation:** 

**[1684.56s] English:** They're going to create a lot of experiences.  
**Translation:** 

**[1686.28s] English:** Some of it we're going to say, "Wow, this is really good.  
**Translation:** 

**[1689.76s] English:** We ought to memorize this.  
**Translation:** Vocabulary: memorize: 背下来

**[1691.82s] English:** That data set then comes all the way back to pre-training.  
**Translation:** 

**[1694.92s] English:** We memorize and generalize it.  
**Translation:** Vocabulary: generalize: 泛化

**[1697.10s] English:** We then refine it and fine-tune it back into post-training.  
**Translation:** 

**[1701.96s] English:** Then we enhance it even more with test-time techniques.  
**Translation:** Vocabulary: enhance: 提升; refine: 精炼

**[1704.98s] English:** And the agency systems put it out into the industry.  
**Translation:** 

**[1710.54s] English:** And so this loop, this cycle, is going to go on and on and on.  
**Translation:** 

**[1714.56s] English:** It kind of comes down to the fact that basic intelligence will scale primarily by one thing: compute.  
**Translation:** 

**[1721.86s] English:** But there's a tricky thing there that you have to anticipate and predict.  
**Translation:** Vocabulary: anticipate: 预判; compute: 计算; tricky: 棘手

**[1725.18s] English:** Which is some of these components; it requires a different kind of hardware to really do it optimally.  
**Translation:** 

**[1733.08s] English:** So, you have to anticipate.  
**Translation:** Vocabulary: optimally: 最优化地

**[1734.32s] English:** You have to anticipate where AI innovation is going to lead.  
**Translation:** 

**[1737.06s] English:** For example, make sure "that's" is first with sparsity.  
**Translation:** Vocabulary: sparsity: 稀疏性

**[1739.64s] English:** Perfect.  
**Translation:** 

**[1740.08s] English:** With hardware, you can't just pivot on a week's notice.  
**Translation:** 

**[1743.90s] English:** You have to anticipate what that will look like.  
**Translation:** 

**[1746.08s] English:** So good.  
**Translation:** 

**[1746.94s] English:** That's so scary and difficult to do, right?  
**Translation:** 

**[1749.48s] English:** For example, these AI model architectures are being invented about once every six months.  
**Translation:** 

**[1755.66s] English:** Yeah.  
**Translation:** 

**[1757.12s] English:** Right?  
**Translation:** 

**[1759.00s] English:** And system architectures and hardware architectures,  
**Translation:** 

**[1763.00s] English:** Kind of,  
**Translation:** 

**[1763.32s] English:** Every three years.  
**Translation:** 

**[1766.08s] English:** And so, you need to anticipate what is likely to happen two or three years from now.  
**Translation:** 

**[1773.08s] English:** And there are a couple of ways that you could do that.  
**Translation:** 

**[1774.64s] English:** First of all, we could do research internally ourselves.  
**Translation:** Vocabulary: internally: 内部地

**[1776.66s] English:** And that's one of the reasons why we have basic research.  
**Translation:** 

**[1778.70s] English:** We have applied research.  
**Translation:** 

**[1780.00s] English:** We create our own models.  
**Translation:** 

**[1781.50s] English:** And so we have, we have hands-on life experience right here.  
**Translation:** 

**[1785.44s] English:** This is part of the co-design that I'm talking about.  
**Translation:** 

**[1788.10s] English:** We're also the only AI company in the world that works with literally every AI company in the world.  
**Translation:** 

**[1791.90s] English:** And, to the extent that we can,  
**Translation:** 

**[1793.10s] English:** We try to get a sense of what challenges people are experiencing.  
**Translation:** 

**[1798.98s] English:** So, you're listening to the whisper.  
**Translation:** 

**[1800.00s] English:** Across the industry, the ad-libs.  
**Translation:** Vocabulary: whisper: 耳语

**[1802.50s] English:** That's right.  
**Translation:** 

**[1802.98s] English:** You've got to listen and learn from everybody.  
**Translation:** 

**[1805.72s] English:** And then the last part is to have an architecture that's flexible.  
**Translation:** 

**[1810.86s] English:** That can adapt and move with the wind.  
**Translation:** Vocabulary: flexible: 有弹性的

**[1813.62s] English:** And one of the benefits of CUDA is that it's, on the one hand,  
**Translation:** 

**[1818.64s] English:** An incredible accelerator.  
**Translation:** Vocabulary: accelerator: 加速器

**[1820.14s] English:** On the other hand, it's really flexible.  
**Translation:** 

**[1822.92s] English:** And so that balance— incredible balance between specialization,  
**Translation:** 

**[1827.36s] English:** Otherwise, we can't accelerate the CPU.  
**Translation:** 

**[1830.94s] English:** Versus generalization, so that we can adapt to changing algorithms.  
**Translation:** Vocabulary: accelerate: 加速; generalization: 泛化

**[1835.30s] English:** That's really, really important.  
**Translation:** 

**[1836.76s] English:** That's the reason why CUDA has been so resilient, on the one hand,  
**Translation:** Vocabulary: resilient: 坚韧的

**[1842.48s] English:** And yet, we continue to enhance it.  
**Translation:** 

**[1844.14s] English:** We're at CUDA 13.2.  
**Translation:** Vocabulary: enhance: 提高

**[1846.04s] English:** And so, we're evolving the architecture so fast.  
**Translation:** 

**[1849.16s] English:** That we can stay with the modern algorithms.  
**Translation:** Vocabulary: evolving: 演变

**[1855.28s] English:** For example,  
**Translation:** 

**[1857.36s] English:** When Mixture Experts came out,  
**Translation:** Vocabulary: mixture: 混合物

**[1859.64s] English:** That's the reason why we had MVLink-72 instead of MVLink-8.  
**Translation:** 

**[1863.64s] English:** We could now take an entire 4.1 trillion-parameter model.  
**Translation:** 

**[1867.80s] English:** And put it in one computing domain, as if it's running on one GPU.  
**Translation:** 

**[1875.24s] English:** People probably didn't notice I said it.  
**Translation:** Vocabulary: computing: 计算

**[1879.00s] English:** But if you look at the architecture of the Grace Blackwell racks,  
**Translation:** 

**[1884.24s] English:** It was completely focused on doing one thing.  
**Translation:** Vocabulary: blackwell: 布莱克威尔

**[1887.36s] English:** Processing the LLM.  
**Translation:** 

**[1890.04s] English:** All of a sudden, one year later,  
**Translation:** 

**[1892.36s] English:** You're looking at a Vera Rubin rack.  
**Translation:** 

**[1894.42s] English:** It has storage accelerators.  
**Translation:** Vocabulary: accelerators: 加速器; rubin: 鲁宾

**[1897.78s] English:** It has this incredible new CPU called Vera.  
**Translation:** 

**[1900.58s] English:** It has Vera Rubin and MVLink-72 to run the LLMs.  
**Translation:** 

**[1905.88s] English:** It also has this new additional rack called Grok.  
**Translation:** 

**[1909.64s] English:** And so, this entire rack system is completely different.  
**Translation:** 

**[1914.02s] English:** Than the previous one.  
**Translation:** 

**[1916.04s] English:** And it's got all these new things.  
**Translation:** 

**[1917.24s] English:** It's got all these new components in it.  
**Translation:** 

**[1918.32s] English:** And the reason for that is because the last...  
**Translation:** 

**[1920.00s] English:** This one was designed to run MOE large language models for inference, and this one is for running agents, which bang on tools.  
**Translation:** 

**[1930.58s] English:** Obviously, the design of the system had to have been done before Cloud Code, Codex, and OpenClaw.  
**Translation:** Vocabulary: codex: 代码库; inference: 推断

**[1939.62s] English:** You were anticipating the future, essentially.  
**Translation:** 

**[1941.66s] English:** Yeah.  
**Translation:** Vocabulary: anticipating: 预知

**[1941.88s] English:** And that comes from what?  
**Translation:** 

**[1943.20s] English:** From the whispers, from the understanding, what is all the state-of-the-art?  
**Translation:** Vocabulary: whispers: 低语

**[1946.24s] English:** No, it's easier than that.  
**Translation:** 

**[1948.54s] English:** You just reason about it.  
**Translation:** 

**[1950.00s] English:** First of all, you just reason.  
**Translation:** 

**[1954.44s] English:** No matter what happens, at some point, in order for that large language model to be a digital worker, let's just use that metaphor.  
**Translation:** Vocabulary: metaphor: 比喻

**[1965.26s] English:** Let's say that we want the LLM to be a digital worker.  
**Translation:** 

**[1967.46s] English:** What does it have to do?  
**Translation:** 

**[1968.84s] English:** It has to access ground truth.  
**Translation:** 

**[1971.18s] English:** That's our file system.  
**Translation:** 

**[1972.50s] English:** It has to be able to do research.  
**Translation:** 

**[1974.32s] English:** It doesn't know everything.  
**Translation:** 

**[1975.78s] English:** And I don't want to wait until this AI becomes universal.  
**Translation:** 

**[1980.00s] English:** I want to be universally smart about everything, past, present, and future, before making it useful, and so, therefore, I might as well let it go do the research.  
**Translation:** Vocabulary: universally: 普适地

**[1989.50s] English:** It's obvious that if it wants to help me, it's got to use my tools.  
**Translation:** 

**[1993.26s] English:** A lot of people would say that AI is going to completely destroy software.  
**Translation:** 

**[1998.16s] English:** We don't need software anymore.  
**Translation:** 

**[1999.08s] English:** We don't even need tools anymore.  
**Translation:** 

**[2000.24s] English:** That's ridiculous.  
**Translation:** 

**[2001.72s] English:** Let's use a thought experiment.  
**Translation:** 

**[2005.16s] English:** And you could just sit there, enjoy a glass of whiskey, and think about it.  
**Translation:** 

**[2009.98s] English:** And think about all these things, and it would become completely obvious.  
**Translation:** Vocabulary: whiskey: 威士忌

**[2012.84s] English:** Like, if I were to create the most amazing agent that we can imagine in the next 10 years, let's say it would be a humanoid robot.  
**Translation:** 

**[2023.00s] English:** If that humanoid robot were to be created, is it more likely that the humanoid robot comes into my house and uses the tools that I have to do the work that it needs to do?  
**Translation:** Vocabulary: humanoid: 类人形的

**[2034.24s] English:** Does this hand turn into a 10-pound hammer in one instance?  
**Translation:** 

**[2039.52s] English:** Turns?  
**Translation:** Vocabulary: hammer: 铁锤

**[2039.98s] English:** Turns.  
**Translation:** 

**[2040.00s] English:** To sterilize a scalpel, in another instance, and in order to boil water, it beams microwaves out.  
**Translation:** Vocabulary: microwaves: 微波; scalpel: 手术刀; sterilize: 消毒

**[2047.00s] English:** It's fingers, you know, or is it more likely just to use the microwave, you know, and the first time it  
**Translation:** 

**[2051.80s] English:** Goes up to the microwave, it probably doesn't know how to use it, but that's okay; it's connected to.  
**Translation:** Vocabulary: microwave: 微波炉

**[2057.26s] English:** The Internet reads the manual of this microwave, instantly becomes an expert, and so it  
**Translation:** 

**[2065.06s] English:** Uses it, and so I think the one I just described, in fact, almost all of the properties of open claw.  
**Translation:** Vocabulary: instantly: 立刻

**[2073.86s] English:** You know that it's going to use tools, access files, and be able to do  
**Translation:** 

**[2078.84s] English:** Research it has an IO subsystem, and when you're done reasoning through it, reasoning about it thoroughly.  
**Translation:** Vocabulary: thoroughly: 详尽地

**[2084.74s] English:** Through it in that way, um, then you say, "Oh my gosh, the impact to the future of computing is deeply  
**Translation:** 

**[2093.00s] English:** Profound, and the reason for that is  
**Translation:** Vocabulary: computing: 计算; profound: 深远

**[2095.06s] English:** I think we've just reinvented the computer, and then now you say, "Okay, when did we reason about...  
**Translation:** 

**[2100.60s] English:** That when did we reason about the open claw? If you take the open claw schematic I used at GTC.  
**Translation:** Vocabulary: schematic: 原理图

**[2107.32s] English:** You'll find it; two years ago, literally two years ago at GTC, I was talking about...  
**Translation:** 

**[2115.32s] English:** Agentic systems that exactly reflect OpenCL today, and of course, the confluence of  
**Translation:** Vocabulary: agentic: 自主的; confluence: 汇合

**[2124.40s] English:** Of  
**Translation:** 

**[2125.00s] English:** Of  
**Translation:** 

**[2125.02s] English:** Of  
**Translation:** 

**[2125.04s] English:** Of  
**Translation:** 

**[2125.06s] English:** Of many things had to happen, first of all, we needed Cloud and GPT, and you know, all of these.  
**Translation:** 

**[2131.32s] English:** Models to reach a level of capability, so that their innovation and breakthroughs can be achieved, and their  
**Translation:** Vocabulary: breakthroughs: 重大进展; capability: 能力

**[2136.32s] English:** Continued advances were really important, and then, of course, someone had to create an open-source project.  
**Translation:** 

**[2142.48s] English:** You know, um, a project that is sufficiently robust, you know, it's sufficiently complete.  
**Translation:** Vocabulary: advances: 进步; robust: 健壮; sufficiently: 足够

**[2150.00s] English:** And that we can all put to work, and I think we can open claw.  
**Translation:** 

**[2154.76s] English:** Did Chat GPT do for generative systems what AGENTIC systems did for agentic systems?  
**Translation:** Vocabulary: generative: 生成的

**[2160.00s] English:** And I just think it's a very big deal. Yeah, it's a really special moment. I'm not exactly sure why.  
**Translation:** 

**[2165.46s] English:** It captured so much of the world's attention, but it did more than Cloud Code and Codex, and so on.  
**Translation:** Vocabulary: codex: 法典

**[2171.82s] English:** Because consumers could reach it, sure, yeah, but there's also so much of this is about vibes.  
**Translation:** 

**[2177.82s] English:** And Peter, uh, I had a podcast with him; a wonderful human being. So, part of it is also about the humans that.  
**Translation:** Vocabulary: vibes: 感觉

**[2183.98s] English:** Represent the thing, and no doubt part of it is memes. And because we're all trying to figure it out.  
**Translation:** 

**[2188.20s] English:** It out there's really serious and complicated security concerns about when you have such.  
**Translation:** 

**[2193.44s] English:** Powerful technology: How do you hand over your data so they can do useful stuff, but then there's scary.  
**Translation:** 

**[2198.04s] English:** Things associated with that, and we as a civilization, as individual people, and as a  
**Translation:** 

**[2202.02s] English:** Civilization figuring out how to find that right balance, yeah. We jumped on it right away.  
**Translation:** 

**[2206.44s] English:** And we sent a bunch of security experts this way, and we did this thing called Open Shell; it's  
**Translation:** 

**[2212.24s] English:** Already been integrated into OpenCL, and NVIDIA put forward Nemo Claw.  
**Translation:** 

**[2218.18s] English:** Yeah, exactly. They install super easy. It makes sure that it's secure. We give you two out of three.  
**Translation:** Vocabulary: integrated: 合并

**[2224.70s] English:** Rights-agentic systems can access sensitive information, it can execute code, and it can  
**Translation:** 

**[2230.20s] English:** Communicate externally, we could keep things safe if we gave you two out of those three.  
**Translation:** Vocabulary: execute: 运行代码; externally: 外部地

**[2237.36s] English:** Capabilities can be selected at any time, but not all three. Out of those, two out of three capabilities are also available.  
**Translation:** 

**[2243.24s] English:** Give you access control based on whatever rights you are given by.  
**Translation:** Vocabulary: capabilities: 能力

**[2247.92s] English:** Enterprise.  
**Translation:** 

**[2248.18s] English:** And then we connect it to a policy engine that all these enterprises already have.  
**Translation:** Vocabulary: enterprises: 企业

**[2252.86s] English:** And so, um, we're going to try to do our best to help Open Claw become a better claw.  
**Translation:** 

**[2259.98s] English:** So, you eloquently explained how we have a long history of blockers that we thought were going  
**Translation:** Vocabulary: eloquently: 口才好地

**[2265.42s] English:** To be blockers, and we overcame them. But now, looking into the future, what do you think might  
**Translation:** 

**[2269.14s] English:** Be the blockers now that it's clear that agents will be everywhere, so it's obviously we're going.  
**Translation:** Vocabulary: overcame: 克服了障碍

**[2274.76s] English:** To need compute, so what is going to be the blocker for the future?  
**Translation:** 

**[2278.16s] English:** Future, so the network will have to be structured accordingly, scaling the democracy.  
**Translation:** Vocabulary: accordingly: 相应地; compute: 计算

**[2279.76s] English:** Of that, scaling badly; though Theaporger will take over.  
**Translation:** 

**[2280.00s] English:** Is a concern, but it's not the only concern. But that's the reason why we're pushing so hard on.  
**Translation:** 

**[2281.22s] English:** The Gov  
**Translation:** 

**[2282.20s] English:** One thing else, my friend.  
**Translation:** 

**[2285.48s] English:** Extreme co-design, so that we can improve tokens per second per watt by orders of magnitude.  
**Translation:** 

**[2294.80s] English:** Every single year, and so in the last 10 years, Moore's law would have progressed computing about  
**Translation:** Vocabulary: computing: 计算; progressed: 进展

**[2302.18s] English:** Good.  
**Translation:** 

**[2302.18s] English:** 100 times in the last 10 years. We progressed and scaled up computing by a million times in...  
**Translation:** 

**[2303.14s] English:** Public  
**Translation:** 

**[2304.28s] English:** But  
**Translation:** 

**[2307.30s] English:** Yeah.  
**Translation:** 

**[2307.50s] English:** It's  
**Translation:** 

**[2307.72s] English:** Going.  
**Translation:** 

**[2308.00s] English:** To  
**Translation:** 

**[2308.02s] English:** The last 10 years, and so we're going to keep on doing that through extreme co-design.  
**Translation:** 

**[2312.96s] English:** So, energy efficiency per watt completely affects a company's revenues. It affects the revenues,...  
**Translation:** Vocabulary: revenues: 收入

**[2321.46s] English:** Of a factory, and we're just going to push that to the limit so that we can keep on driving tokens.  
**Translation:** 

**[2327.28s] English:** Costs are coming down as fast as we can. Our computer prices are going up, but our token generation effectiveness is improving.  
**Translation:** Vocabulary: effectiveness: 效果; token: 代币

**[2336.50s] English:** Is going up so much faster. And so we're going to keep on doing that through extreme co-design.  
**Translation:** 

**[2338.02s] English:** The token cost is coming down. It's coming down by an order of magnitude every year.  
**Translation:** 

**[2344.68s] English:** So, power—that's an interesting one. The way to try to get around the power blocker is to try to,  
**Translation:** 

**[2351.12s] English:** With the tokens per second per watt, we should try to make it more and more efficient. Of course.  
**Translation:** 

**[2354.30s] English:** There's the question of how we get more power. We should also get more power.  
**Translation:** 

**[2357.60s] English:** That's a really complicated one. You've talked about small modular nuclear power plants. There's  
**Translation:** Vocabulary: modular: 模块化的

**[2361.46s] English:** All kinds of ideas for energy. How much do they keep you up at night? The bottlenecks in the  
**Translation:** 

**[2368.02s] English:** Supply chain of AI, like ASML with EUV lithography machines, and GSMC with advanced packaging, such as COAS.  
**Translation:** Vocabulary: bottlenecks: 瓶颈; lithography: 光刻

**[2375.28s] English:** And SK Hynix with high-bandwidth memory. All the time. And we're working on it all the time.  
**Translation:** 

**[2381.24s] English:** No company in history has ever grown at a scale that we're growing, while accelerating that growth.  
**Translation:** Vocabulary: accelerating: 加速

**[2389.10s] English:** It's incredible, and it's hard for people to even understand this. In the overall world of AI,...  
**Translation:** 

**[2395.44s] English:** Computing, we're increasing our share.  
**Translation:** Vocabulary: computing: 计算

**[2398.02s] English:** And so, supply chain; upstream.  
**Translation:** 

**[2400.00s] English:** And downstream are really important to us. I spend a lot of time informing all the CEOs.  
**Translation:** Vocabulary: downstream: 下游; informing: 通知; upstream: 上游

**[2408.20s] English:** That I work with, what are the dynamics that will cause the growth to continue or even  
**Translation:** 

**[2414.78s] English:** Accelerate? It's part of the reason why, to the entire right-hand side of me, we're CEOs of  
**Translation:** Vocabulary: accelerate: 加快

**[2422.26s] English:** Practically the entire IT industry, upstream, and practically the entire  
**Translation:** 

**[2427.30s] English:** Infrastructure industry downstream. There were several hundred CEOs, and I don't think there's  
**Translation:** Vocabulary: practically: 几乎

**[2436.92s] English:** Ever been to keynotes where several hundred CEOs show up? Part of it is I'm telling them about...  
**Translation:** 

**[2443.42s] English:** Our business condition now. I'm telling them about the growth drivers in the very near future.  
**Translation:** Vocabulary: keynotes: 重要演讲

**[2449.60s] English:** And what's happening? I'm also describing where we're going next, so that they can use.  
**Translation:** 

**[2457.30s] English:** To inform them how they want to invest, I inform them that way—like I inform my own employees.  
**Translation:** 

**[2466.16s] English:** Then, of course, I make trips out to them and make sure that, hey, listen; I want you to know.  
**Translation:** 

**[2471.82s] English:** This quarter, this coming year, and the next year, these things are going to happen.  
**Translation:** 

**[2477.64s] English:** If you look at the CEOs of the DRAM industry, the number-one DRAM in the world is DDR memory for  
**Translation:** 

**[2487.30s] English:** CPUs and data centers. About three years ago, I was able to convince several of the CEOs that:  
**Translation:** 

**[2496.18s] English:** Even though, at the time, HBM memory was used quite sparingly and barely by supercomputers,  
**Translation:** 

**[2503.02s] English:** That this was going to be a mainstream memory for data centers in the future. At first, it sounded  
**Translation:** Vocabulary: mainstream: 主流; sparingly: 少量地; supercomputers: 超级计算机

**[2508.30s] English:** Ridiculous, but several of the CEOs believed me and decided to invest in building HBM memories.  
**Translation:** 

**[2515.38s] English:** Another memory was...  
**Translation:** 

**[2517.30s] English:** It's rather odd to put into a data center.  
**Translation:** 

**[2520.00s] English:** The low-power memories that we use for cell phones.  
**Translation:** 

**[2522.84s] English:** And we wanted them to adapt them.  
**Translation:** 

**[2524.74s] English:** For supercomputers in the data center.  
**Translation:** 

**[2527.48s] English:** And they go, "Cell phone memory for supercomputers?  
**Translation:** 

**[2531.00s] English:** And I explained to them why.  
**Translation:** 

**[2533.26s] English:** Well, look at these two memories.  
**Translation:** 

**[2534.64s] English:** LPDDR5, HBM4.  
**Translation:** 

**[2537.34s] English:** The volumes are so incredible.  
**Translation:** 

**[2539.92s] English:** All three of them had record years in history.  
**Translation:** 

**[2542.24s] English:** And these are 45-year-old companies.  
**Translation:** 

**[2545.66s] English:** And so, you know, that's part of my job.  
**Translation:** 

**[2548.82s] English:** Is to inform and shape, inspire, you know?  
**Translation:** 

**[2556.16s] English:** So, you're not just manifesting the future.  
**Translation:** Vocabulary: manifesting: 显现

**[2558.18s] English:** And maybe inspiring NVIDIA,  
**Translation:** 

**[2561.32s] English:** The different engineers of the company.  
**Translation:** 

**[2563.98s] English:** You're manifesting the supply chain of the future.  
**Translation:** 

**[2566.84s] English:** So, you're having conversations with TSMC, with ASML.  
**Translation:** 

**[2570.12s] English:** Upstream, downstream.  
**Translation:** 

**[2571.26s] English:** Upstream, downstream.  
**Translation:** Vocabulary: downstream: 水流向下游; upstream: 水流向上游

**[2572.76s] English:** So, that's the thing.  
**Translation:** 

**[2574.34s] English:** GEV, Caterpillar.  
**Translation:** Vocabulary: caterpillar: 拖拉机

**[2576.62s] English:** Yeah, that's downstream from us.  
**Translation:** 

**[2578.52s] English:** Yeah, yeah.  
**Translation:** 

**[2578.82s] English:** Yeah, the whole thing.  
**Translation:** 

**[2580.28s] English:** I mean, but that's so,  
**Translation:** 

**[2582.22s] English:** There's so much incredibly difficult engineering.  
**Translation:** 

**[2585.28s] English:** That happens in the entire semiconductor industry.  
**Translation:** 

**[2588.80s] English:** And it just feels scary.  
**Translation:** 

**[2591.82s] English:** How intricate the supply chain is,  
**Translation:** Vocabulary: intricate: 复杂的

**[2595.76s] English:** How many components are there?  
**Translation:** 

**[2596.94s] English:** But it works, somehow.  
**Translation:** 

**[2598.64s] English:** Exactly.  
**Translation:** 

**[2599.08s] English:** The deep science, the deep engineering,  
**Translation:** 

**[2601.76s] English:** The incredible manufacturing,  
**Translation:** 

**[2603.24s] English:** And so much of the manufacturing is already done with robotics.  
**Translation:** Vocabulary: robotics: 机器人技术

**[2606.02s] English:** But we have a couple of hundred suppliers.  
**Translation:** 

**[2608.78s] English:** That contributes the technology.  
**Translation:** Vocabulary: suppliers: 供应商

**[2611.32s] English:** That goes into our 1.3 million-component rack.  
**Translation:** 

**[2615.90s] English:** Each rack contains 1.3 to 1.5 million components.  
**Translation:** 

**[2621.12s] English:** There are 200 suppliers across the Vera Rubin rack.  
**Translation:** 

**[2625.00s] English:** So, it's interesting that you don't list that.  
**Translation:** Vocabulary: rubin: 鲁宾

**[2626.64s] English:** As the thing that keeps you up at night.  
**Translation:** 

**[2628.00s] English:** In the list of blockers.  
**Translation:** 

**[2629.52s] English:** But I'm doing all the things necessary to....  
**Translation:** 

**[2632.36s] English:** Okay, to...  
**Translation:** 

**[2633.18s] English:** See?  
**Translation:** 

**[2633.88s] English:** I can go to sleep because I checked it off.  
**Translation:** 

**[2635.78s] English:** I said, "Okay, you know, I go,  
**Translation:** 

**[2637.86s] English:** I can go to sleep.  
**Translation:** 

**[2638.76s] English:** I go....  
**Translation:** 

**[2640.00s] English:** Well, let's see.  
**Translation:** 

**[2641.32s] English:** Let's reason about this.  
**Translation:** 

**[2642.52s] English:** What's important for us?  
**Translation:** 

**[2645.06s] English:** Okay, let's reason about this.  
**Translation:** 

**[2646.84s] English:** Because we changed the system architecture.  
**Translation:** 

**[2649.42s] English:** From the original DGX-1 that you remembered.  
**Translation:** 

**[2652.42s] English:** To MVLink 72 Rack Scale Computing,  
**Translation:** Vocabulary: computing: 计算

**[2656.42s] English:** What does that mean?  
**Translation:** 

**[2658.82s] English:** What does that mean to software?  
**Translation:** 

**[2661.28s] English:** What does that mean to engineering?  
**Translation:** 

**[2662.88s] English:** What does that mean for how we design and test?  
**Translation:** 

**[2665.84s] English:** And what does that mean to the supply chain?  
**Translation:** 

**[2667.24s] English:** Well, one of the things that it meant was  
**Translation:** 

**[2670.00s] English:** We moved towards supercomputer integration.  
**Translation:** 

**[2674.72s] English:** At the data center.  
**Translation:** Vocabulary: supercomputer: 超级计算机

**[2676.34s] English:** Into supercomputer manufacturing.  
**Translation:** 

**[2679.04s] English:** In the supply chain.  
**Translation:** 

**[2682.22s] English:** If you're doing that,  
**Translation:** 

**[2684.26s] English:** You also have to recognize.  
**Translation:** 

**[2685.30s] English:** You're going to move one.  
**Translation:** 

**[2686.80s] English:** And if you're in a total footprint,  
**Translation:** Vocabulary: footprint: 足迹

**[2691.24s] English:** Of whatever data center you're going to build,  
**Translation:** 

**[2694.34s] English:** Let's say you would like to have.  
**Translation:** 

**[2696.38s] English:** You know, 50 gigawatts of supercomputers.  
**Translation:** 

**[2699.68s] English:** That are running simultaneously.  
**Translation:** Vocabulary: gigawatts: 兆瓦; supercomputers: 超级计算机

**[2701.84s] English:** And it takes one week to manufacture.  
**Translation:** 

**[2705.10s] English:** That is equivalent to 50 gigawatts of supercomputers.  
**Translation:** 

**[2708.20s] English:** Then, each week in the supply chain,  
**Translation:** 

**[2711.58s] English:** The supercomputers are going to need  
**Translation:** 

**[2712.78s] English:** A gigawatt of power.  
**Translation:** 

**[2713.80s] English:** And so, we're going to need the supply chain.  
**Translation:** Vocabulary: gigawatt: 吉瓦

**[2716.12s] English:** To increase the amount of power it has,  
**Translation:** 

**[2718.04s] English:** To build and test.  
**Translation:** 

**[2721.46s] English:** The supercomputers in the supply chain.  
**Translation:** 

**[2723.62s] English:** Before I ship it.  
**Translation:** 

**[2725.02s] English:** Well, MVLink 72 literally built supercomputers.  
**Translation:** 

**[2727.40s] English:** In the supply chain, we kept track of them and shipped them.  
**Translation:** 

**[2729.68s] English:** Two to three tons at a time per rack.  
**Translation:** 

**[2732.74s] English:** It used to be that they used to come in parts.  
**Translation:** 

**[2735.02s] English:** And we used to assemble them inside the data center.  
**Translation:** 

**[2737.72s] English:** But that's impossible now.  
**Translation:** Vocabulary: assemble: 组装

**[2738.86s] English:** Because MVLink 72 is so dense.  
**Translation:** 

**[2741.18s] English:** And so, that's an example.  
**Translation:** 

**[2742.58s] English:** And I would have to go into, you know,  
**Translation:** 

**[2745.08s] English:** I'd fly into the supply chain.  
**Translation:** 

**[2746.86s] English:** Go meet my partners and say,  
**Translation:** 

**[2747.80s] English:** Hey, I said, "Guess what?  
**Translation:** 

**[2749.66s] English:** So, here's what we're going to do:  
**Translation:** 

**[2751.40s] English:** This is the way we used to build our DGXs.  
**Translation:** 

**[2754.08s] English:** We're going to build them this way.  
**Translation:** 

**[2755.38s] English:** This is going to be so much better!  
**Translation:** 

**[2756.42s] English:** Because we're going to need them for inference.  
**Translation:** 

**[2758.92s] English:** The market for inference,  
**Translation:** Vocabulary: inference: 推理

**[2759.68s] English:** Inference.  
**Translation:** 

**[2760.00s] English:** Is coming. The inflection point for inference is coming. It's going to be a big market.  
**Translation:** Vocabulary: inflection: 转折点

**[2765.48s] English:** And so, I first explain to them what is going on and why it's going to happen. Then I ask them.  
**Translation:** 

**[2771.18s] English:** To make several billion dollars of capital investments each, and because they trust me.  
**Translation:** Vocabulary: investments: 资金投入

**[2779.90s] English:** And I'm very respectful of them, and I give them every opportunity to question me, and I spend time doing so.  
**Translation:** 

**[2786.14s] English:** To explain things to people, I reason about it. I draw them pictures and I reason about it.  
**Translation:** 

**[2790.82s] English:** In first principles. And by the time I'm done with them, there's no way to do it.  
**Translation:** 

**[2795.36s] English:** So, a lot of it is about relationships and building a shared view of the future.  
**Translation:** 

**[2801.40s] English:** But do you worry about certain bottlenecks? I mean, what are the biggest bottlenecks in this process?  
**Translation:** 

**[2806.32s] English:** The supply chain? Are you worried about ASML's EUV tooling? Are you worried about  
**Translation:** Vocabulary: bottlenecks: 瓶颈

**[2810.78s] English:** The packaging, Co-op packaging of TSMC, about how fast it could scale?  
**Translation:** 

**[2816.04s] English:** Like, what are the biggest bottlenecks in the supply chain?  
**Translation:** 

**[2816.14s] English:** Like you said, you're not only growing incredibly fast; you're also accelerating your growth. So,  
**Translation:** 

**[2820.62s] English:** It feels like everybody in the supply chain, and those are certainly bottlenecks, would have to  
**Translation:** Vocabulary: accelerating: 加快

**[2826.42s] English:** Scale up. Are you having conversations with them? How can you scale this up faster?  
**Translation:** 

**[2832.22s] English:** Do you worry about it?  
**Translation:** 

**[2833.28s] English:** No.  
**Translation:** 

**[2833.82s] English:** Okay.  
**Translation:** 

**[2834.46s] English:** Because I told them what I needed, they understood what I needed, and they told me what  
**Translation:** 

**[2839.64s] English:** They're going to go do it, and I believe in what they're going to do.  
**Translation:** 

**[2842.00s] English:** Interesting.  
**Translation:** 

**[2842.52s] English:** Yeah.  
**Translation:** 

**[2842.72s] English:** That's great to hear. So, maybe if we can just linger on the power,  
**Translation:** 

**[2846.00s] English:** For a little bit, what are your hopes for how to solve the energy problem?  
**Translation:** Vocabulary: linger: 停留

**[2850.50s] English:** One of the areas that I would love us to talk about and just get the message out:  
**Translation:** 

**[2858.50s] English:** Our power grid is designed for the worst-case condition with some margin. Well, 99% of the  
**Translation:** Vocabulary: margin: 余量

**[2870.82s] English:** Time, we're nowhere near the worst-case condition because the worst-case condition is just a few days in.  
**Translation:** 

**[2875.02s] English:** The winter, a few days in the summer. And we're nowhere near the worst-case condition because the  
**Translation:** 

**[2875.98s] English:** The worst-case condition is a few days in the summer and extreme weather.  
**Translation:** 

**[2880.00s] English:** At any given time, we're nowhere near the worst-case scenario, and we're probably just running around.  
**Translation:** Vocabulary: scenario: 假设情况

**[2884.90s] English:** Call it 60% of peak. And so, 99% of the time, our power grid has excess power, and they're just  
**Translation:** 

**[2895.66s] English:** Sitting idle, but they have to be there, sitting idle, because just in case, when the time comes,  
**Translation:** 

**[2900.98s] English:** Hospitals have to be powered, and infrastructure has to be powered, and airports have to run, and  
**Translation:** 

**[2905.20s] English:** So, and so forth. And so, the question that I have is whether we could go and help them.  
**Translation:** 

**[2911.84s] English:** Understand and create contractual agreements and design computer architecture systems.  
**Translation:** 

**[2917.54s] English:** Data centers, such that when they need the maximum power for infrastructure in society,  
**Translation:** 

**[2926.60s] English:** That the data centers would get less, but that's in a very rare instance, anyway.  
**Translation:** 

**[2931.72s] English:** And during that time, we either have a backup generator for that little part of it.  
**Translation:** Vocabulary: backup: 备用; generator: 发电机组

**[2934.86s] English:** Or, we have a backup generator for that little part of it.  
**Translation:** 

**[2935.20s] English:** Or we just have our computers shift a workload somewhere else, or we have the computers just do it themselves.  
**Translation:** Vocabulary: workload: 工作任务

**[2939.74s] English:** Run slower. We could degrade our performance, reduce our power consumption, and provide for  
**Translation:** 

**[2947.24s] English:** A slightly longer latency response when somebody asks for an answer. And so, I think that's the way.  
**Translation:** Vocabulary: degrade: 降低; latency: 延迟

**[2955.72s] English:** Of using computers, of building data centers, instead of expecting 100% uptime, and these  
**Translation:** 

**[2963.40s] English:** Contracts that are really, really...  
**Translation:** Vocabulary: uptime: 开机时间

**[2965.20s] English:** Quite rigorous, it's putting a lot of pressure on the grid to be able to... Now they're going to.  
**Translation:** 

**[2970.48s] English:** I have to increase from their maximum. I just want to use their excess; it's just sitting there.  
**Translation:** Vocabulary: rigorous: 严格的

**[2976.66s] English:** Yeah, that's not talked about enough. So, what's stopping it? Is it regulation? Is it  
**Translation:** 

**[2981.52s] English:** Bureaucracy? I think it's a three-way problem. It starts with the end customer. The end customer,...  
**Translation:** Vocabulary: bureaucracy: 官僚主义

**[2988.28s] English:** Puts requirements on the data centers that they can never...  
**Translation:** 

**[2995.20s] English:** Not be available. So that the end customer expects perfection.  
**Translation:** 

**[3000.00s] English:** Now, in order to deliver that perfection, you need a combination of backup generators and your grid power supplier to deliver on it.  
**Translation:** 

**[3010.04s] English:** And so everyone's got to have six nines.  
**Translation:** Vocabulary: generators: 发电机组; supplier: 供应商

**[3013.26s] English:** Well, I think, first of all, right now, we ought to have everybody understand that when the customer asks for these things, you have somebody in your data center operations team who is disconnected from the CEO.  
**Translation:** 

**[3025.38s] English:** I bet the CEO doesn't know this.  
**Translation:** Vocabulary: disconnected: 不联系的

**[3026.84s] English:** I'm going to talk to all the CEOs.  
**Translation:** 

**[3028.02s] English:** The CEOs are probably not paying any attention to the contracts that are being signed.  
**Translation:** 

**[3034.32s] English:** And so everyone wants to sign the best contract, of course.  
**Translation:** 

**[3037.26s] English:** And they go down to the cloud service providers, and the two contract negotiators.  
**Translation:** Vocabulary: negotiators: 谈判者; providers: 供应商

**[3044.20s] English:** I could just see them now negotiating these multi-year contracts.  
**Translation:** 

**[3048.96s] English:** Both sides want the best contract.  
**Translation:** 

**[3052.10s] English:** As a result, the CSPs then have to go down to the utilities.  
**Translation:** 

**[3057.10s] English:** And they expect the six nines.  
**Translation:** Vocabulary: utilities: 公共事业

**[3060.18s] English:** And so, I think the first thing is just to make sure that all of the customers, and their CEOs, realize what they're asking for.  
**Translation:** 

**[3068.74s] English:** Now, the second thing is that we have to build data centers that gracefully degrade.  
**Translation:** Vocabulary: degrade: 性能下降

**[3073.50s] English:** And so, if the power company, the grid, tells us, "Listen, we're going to have to back you down to about 80 percent," we're going to say that's no problem at all.  
**Translation:** 

**[3081.64s] English:** We're just going to move our workload around.  
**Translation:** 

**[3083.66s] English:** We're going to make sure that data is never lost.  
**Translation:** 

**[3086.02s] English:** But we can reduce the computing rate and use less energy.  
**Translation:** Vocabulary: computing: 计算

**[3091.58s] English:** The quality of service degrades a little bit.  
**Translation:** 

**[3093.90s] English:** For the critical workloads, I shift them somewhere else right away so I don't have that problem.  
**Translation:** Vocabulary: degrades: 下降; workloads: 负载

**[3099.86s] English:** And so, you know, whoever or whichever data center still has 100 percent uptime.  
**Translation:** 

**[3103.70s] English:** And so, how difficult of an engineering problem is the smart, dynamic allocation of power in the data center?  
**Translation:** 

**[3109.18s] English:** As soon as you could specify it, you could engineer it.  
**Translation:** 

**[3112.14s] English:** Beautifully put.  
**Translation:** Vocabulary: specify: 明确说明

**[3114.30s] English:** So long as it obeys the laws of physics.  
**Translation:** 

**[3116.02s] English:** On first principles, I think we're good.  
**Translation:** 

**[3118.26s] English:** What was the third thing you were mentioning?  
**Translation:** 

**[3120.00s] English:** So, the second thing is the data centers. And the third thing is we need utilities to also recognize that this is an opportunity. And instead of saying, "Look, it's going to take me five years to increase my grid capability.  
**Translation:** Vocabulary: capability: 能力

**[3137.50s] English:** Uh, if you're willing to take on this level of guarantee, I can make them available for you next month and at this price. And so if utilities also offered more segments of power delivery promises, then I think everybody will figure out what to do with it. Yeah. But there's just way too much waste in the grid right now. We should go after it.  
**Translation:** 

**[3163.22s] English:** Uh, you've uh highly lauded Elon and, uh, XAICs.  
**Translation:** Vocabulary: lauded: 赞扬; segments: 部分; utilities: 公用事业

**[3167.50s] English:** He has accomplished building the Colossus supercomputer in Memphis in just four months, probably setting a record. It now boasts 200,000 GPUs and is growing very quickly. Is there something about his approach that you could speak to, which is instructive for all data center creators and enables that kind of accomplishment?  
**Translation:** 

**[3190.30s] English:** His approach to engineering, his approach to the whole management of construction—everything.  
**Translation:** Vocabulary: accomplishment: 成就; boasts: 配备; colossus: 巨无霸; instructive: 有启发的; supercomputer: 超级计算机

**[3195.86s] English:** First of all, Elon is deep.  
**Translation:** 

**[3197.50s] English:** In so many different topics, um, uh, yet he's also a really good systems thinker.  
**Translation:** Vocabulary: thinker: 思考者

**[3204.54s] English:** And so he's able to think through multiple disciplines and, and, um, uh, he obviously, uh, pushes things, questions everything—where the number one question is: Is it necessary?  
**Translation:** 

**[3218.62s] English:** Number two, does it have to be done this way?  
**Translation:** Vocabulary: disciplines: 学科领域

**[3221.26s] English:** And, in other words, do we have to wait this long?  
**Translation:** 

**[3225.24s] English:** And, and so, so he.  
**Translation:** 

**[3227.50s] English:** He has the ability to question everything to the point where everything is reduced to its minimal necessary amount.  
**Translation:** 

**[3238.16s] English:** You can't take anything else out.  
**Translation:** Vocabulary: minimal: 最少的

**[3240.00s] English:** And yet, the necessary capabilities of the product retain, and so he is as minimalist as you could possibly imagine, and he does it at a system scale.  
**Translation:** 

**[3253.98s] English:** I also love the fact that he is represented. He is present at the point of action. He'll just go there. If there's a problem, he'll just go there and show me the problem.  
**Translation:** Vocabulary: capabilities: 能力; minimalist: 极简主义者

**[3271.12s] English:** When you do all of this in combination, you overcome a lot of previous challenges. This is just the way we do it. I'm waiting for them.  
**Translation:** 

**[3282.98s] English:** I mean, it's just...  
**Translation:** 

**[3283.98s] English:** Everybody has a lot of excuses, and then the last thing is when you act personally with so much urgency, it causes everybody else to act with urgency, and every supplier has a lot of customers going on.  
**Translation:** 

**[3297.98s] English:** Every supplier has a lot of projects going on, and he makes it his business to be the top priority of everybody else's projects, and so he does that by demonstrating it.  
**Translation:** Vocabulary: supplier: 供应商; urgency: 紧迫感

**[3309.80s] English:** Yeah, I've been in a bunch of those meetings. It's fun to watch because really, not enough people show up.  
**Translation:** 

**[3313.98s] English:** Yeah, I've been in a bunch of those meetings. It's fun to watch because really, not enough people show up.  
**Translation:** 

**[3343.98s] English:** And just building up that intuition from every single task involved in putting together the data center, you start to immediately get a sense of the detailed scale and the broad system scale of...  
**Translation:** 

**[3360.00s] English:** Where the inefficiencies are.  
**Translation:** Vocabulary: inefficiencies: 不效率; intuition: 直觉

**[3361.62s] English:** And so, you can make it more and more and more efficient.  
**Translation:** 

**[3364.28s] English:** Plus, you have the big hammer of being able to say,  
**Translation:** Vocabulary: hammer: 大杀器

**[3366.88s] English:** Let's do it totally different and remove all possible blockers.  
**Translation:** 

**[3370.62s] English:** That's right.  
**Translation:** 

**[3371.50s] English:** Is there a parallel in the NVIDIA Extreme Systems?  
**Translation:** 

**[3374.16s] English:** Co-design approach that you see in the way,  
**Translation:** Vocabulary: parallel: 相似之处

**[3376.26s] English:** Elon approaches systems engineering?  
**Translation:** 

**[3378.62s] English:** Well, first of all, co-design is an ultimate.  
**Translation:** Vocabulary: approaches: 倾向于

**[3380.74s] English:** Systems engineering problem.  
**Translation:** 

**[3382.06s] English:** And so, we approach the work that we do from that principle.  
**Translation:** 

**[3386.82s] English:** The other thing that we do, and this is a philosophy that,  
**Translation:** 

**[3393.26s] English:** A thought, a state of mind—I guess.  
**Translation:** 

**[3397.86s] English:** A method that I started 30 years ago,  
**Translation:** 

**[3402.34s] English:** And it's called the speed of light.  
**Translation:** 

**[3404.22s] English:** The speed of light is not just about the speed.  
**Translation:** 

**[3405.92s] English:** The speed of light is my shorthand for what's the limit.  
**Translation:** Vocabulary: shorthand: 简化书写

**[3411.24s] English:** Of what physics can do.  
**Translation:** 

**[3412.96s] English:** And so, everything that we do is compared against this.  
**Translation:** 

**[3416.82s] English:** Speed of light.  
**Translation:** 

**[3417.76s] English:** Memory speed, math speed, power, cost, time, effort,  
**Translation:** 

**[3425.24s] English:** Number of people, manufacturing cycle time.  
**Translation:** 

**[3429.08s] English:** And when you think about latency versus throughput,  
**Translation:** Vocabulary: latency: 延迟; throughput: 吞吐量

**[3432.78s] English:** When you think about cost versus throughput,  
**Translation:** 

**[3435.84s] English:** Cost versus capacity: all of these things,  
**Translation:** 

**[3440.14s] English:** You test against the speed of light to achieve.  
**Translation:** 

**[3443.76s] English:** All of these different constraints,  
**Translation:** Vocabulary: constraints: 限制条件

**[3447.24s] English:** Separately.  
**Translation:** 

**[3448.52s] English:** And then, when you consider it together,  
**Translation:** Vocabulary: separately: 单独地

**[3451.42s] English:** You know, you have to make compromises.  
**Translation:** 

**[3452.84s] English:** Because a system that achieves extremely low latency,...  
**Translation:** Vocabulary: compromises: 妥协

**[3456.00s] English:** versus a system that achieves very high throughput.  
**Translation:** 

**[3458.96s] English:** Are they architected fundamentally differently?  
**Translation:** Vocabulary: architected: 设计; fundamentally: 本质上

**[3461.80s] English:** But, you want to know what the speed of light is?  
**Translation:** 

**[3464.16s] English:** Of a system that achieves high throughput.  
**Translation:** 

**[3467.82s] English:** What is the speed of light in a system?  
**Translation:** 

**[3469.58s] English:** That achieves low latency?  
**Translation:** 

**[3472.10s] English:** And then, when you think about the total system,  
**Translation:** 

**[3474.28s] English:** You could make trade-offs.  
**Translation:** 

**[3475.96s] English:** And so I,  
**Translation:** 

**[3476.82s] English:** I force everyone to think about what this is.  
**Translation:** 

**[3478.56s] English:** What is the first,  
**Translation:** 

**[3479.04s] English:** The first principle.  
**Translation:** 

**[3480.00s] English:** The physical limits for everything, before we you know, before we do anything,  
**Translation:** 

**[3488.08s] English:** And we test everything against that, and so that's a good frame of mind. I don't love it completely.  
**Translation:** 

**[3494.34s] English:** The other method, which is continuous improvement, has the problem that it  
**Translation:** 

**[3501.76s] English:** First, you should engineer something from first principles at the speed you know with speed.  
**Translation:** 

**[3507.74s] English:** Of light, thinking is limited only by physical and physics limits, and after that, of course.  
**Translation:** 

**[3516.50s] English:** You would improve it over time, um, but I don't like going into a problem and somebody says, "hey,  
**Translation:** 

**[3522.88s] English:** You know, it takes 74 days to do this today, right now, and we can do it for you in 72 days, you know.  
**Translation:** 

**[3530.10s] English:** I'd rather strip it all back to zero and say, first of all, explain to me why it's 74 days in the first place.  
**Translation:** 

**[3535.06s] English:** Place, and let's know. Let's think about it, and let's think about it, and let's think about it.  
**Translation:** 

**[3537.74s] English:** What is possible today, and if I were to build it completely from scratch, you know, how long would it take?  
**Translation:** Vocabulary: scratch: 从头开始

**[3543.80s] English:** It often takes, and you'd be surprised, it might come to six days. Now, the rest of the six days to.  
**Translation:** 

**[3550.36s] English:** 74 could be very well-reasoned, and compromises, and you know, cost reductions, and all kinds of improvements.  
**Translation:** Vocabulary: compromises: 妥协; reductions: 削减

**[3557.78s] English:** Different things, but at least you know what they are, and then now that you know that it's six days.  
**Translation:** 

**[3562.26s] English:** Possible, then the conversation from 7:46.  
**Translation:** 

**[3567.74s] English:** Surprisingly, it is much more effective in such incredibly complex systems that you're working with.  
**Translation:** 

**[3572.46s] English:** With simplicity sometimes a good heuristic to reach for, I mean, if I can just, I mean, the pod.  
**Translation:** Vocabulary: heuristic: 启发法; simplicity: 简洁性

**[3581.50s] English:** The Vera Rubin Pod that you announced is just incredible. Uh, we're talking about seven chips.  
**Translation:** 

**[3586.48s] English:** Seven chip types, five purpose-built rack types, 40 racks, 1.2 quadrillion transistors.  
**Translation:** Vocabulary: quadrillion: 万亿; rubin: 鲁宾; transistors: 晶体管

**[3592.06s] English:** Nearly 20,000 NVIDIA chips over 1,100 Rubin GPUs.  
**Translation:** 

**[3597.74s] English:** 60 exaflops, 10 petabytes per second.  
**Translation:** Vocabulary: exaflops: 每秒千万亿次浮点运算; petabytes: 千兆字节

**[3600.00s] English:** Going to scale bandwidth, that's just one pod. That's just yeah, that's just.  
**Translation:** 

**[3607.08s] English:** One point five, I mean, so you have the, and then even the NVL 72 rack alone is 1.3 million components.  
**Translation:** Vocabulary: bandwidth: 带宽

**[3615.16s] English:** 1,300 chips, 4,000 pounds, crammed into a single 19-inch-wide rack. And Lex; we'll probably kind of...  
**Translation:** 

**[3620.56s] English:** Crank out about 200 of these pods a week, just to put in perspective the amount of different...  
**Translation:** Vocabulary: crammed: 塞满; crank: 生产

**[3627.16s] English:** Components—I suppose, simplicity is impossible—but is that a metric that you kind of reach for?  
**Translation:** 

**[3633.52s] English:** And trying to design things, you know, the phrase I use most often is "we need.  
**Translation:** Vocabulary: metric: 衡量标准

**[3639.88s] English:** Things should be as complex as necessary, but as simple as possible, and so the question is: is all that?  
**Translation:** 

**[3645.86s] English:** Complexity is necessary, and we ought to test for it and challenge it, and then  
**Translation:** Vocabulary: complexity: 复杂性

**[3652.18s] English:** After that, everything else above it, you know, is gratuitous.  
**Translation:** 

**[3655.90s] English:** But some of the most incredible things are happening in the semiconductor industry broadly, but what NVIDIA is doing stands out.  
**Translation:** Vocabulary: broadly: 广泛地

**[3660.92s] English:** Uh, some of the greatest engineering feats in history, so these systems are just truly marvelous.  
**Translation:** 

**[3668.98s] English:** Of all engineering, it is the most complex computer the world has ever made, yeah, the engineering.  
**Translation:** 

**[3673.94s] English:** Teams, I mean, I don't know; it's not a competition, but I don't know if it was like an Olympics of...  
**Translation:** 

**[3678.20s] English:** Engineering teams, I mean, TSMC does incredible engineering, like I said, as well as ASML, at every scale.  
**Translation:** 

**[3683.88s] English:** But NVIDIA is gonna.  
**Translation:** 

**[3685.90s] English:** Give them a run for their money, yeah—just incredible! Incredible teams, gold medalists.  
**Translation:** 

**[3690.22s] English:** In every single sport, everyone has to assemble right here, work together, and report.  
**Translation:** 

**[3695.44s] English:** Directly to you, this is wonderful. Uh, you've recently traveled to China, uh, so it's interesting.  
**Translation:** Vocabulary: assemble: 集合

**[3702.62s] English:** To ask you: China has been incredibly successful in building up its technology sector. What do you think about that?  
**Translation:** 

**[3708.98s] English:** Understand about how China has been able to, over the past 10 years, build so many incredible world-class projects.  
**Translation:** 

**[3715.90s] English:** Companies with world-class engineering teams and just this technology.  
**Translation:** 

**[3720.00s] English:** Ecosystem that produces so many incredible products—there are a whole bunch of reasons for this, well, first,...  
**Translation:** 

**[3726.90s] English:** Of all, let's start with some facts: 50% of the world's AI researchers are Chinese.  
**Translation:** 

**[3732.00s] English:** Plus or minus, and they're mostly in China still. We have many of them here, but there's amazing.  
**Translation:** 

**[3741.58s] English:** Researchers, still in China, um, their tech industry showed up at precisely the right time.  
**Translation:** 

**[3750.00s] English:** At the time of the mobile cloud era, their way of contributing with software, and so this is a  
**Translation:** Vocabulary: precisely: 正好

**[3755.64s] English:** The country's incredible science and math programs really well-educated kids, and their tech industry was  
**Translation:** 

**[3764.46s] English:** Created during the era of software, they're very comfortable with modern software.  
**Translation:** 

**[3770.08s] English:** China is not one giant economic country; it's got many provinces and cities.  
**Translation:** 

**[3779.00s] English:** With mayors all competing with each other, that's the reason why there are so many EV companies.  
**Translation:** Vocabulary: mayors: 市长; provinces: 省份

**[3784.42s] English:** The reason why there are so many AI companies is that there are so many opportunities.  
**Translation:** 

**[3788.20s] English:** Company, you could imagine, they all create some of them, and as a result, they have insane.  
**Translation:** 

**[3797.18s] English:** Competition internally, and you know, what remains is an incredible company. They also have a social.  
**Translation:** 

**[3809.00s] English:** Network: where it's family first, friends second, and company third, and so on.  
**Translation:** Vocabulary: internally: 内部地

**[3816.08s] English:** The amount of conversation that goes back and forth between them is essentially open source.  
**Translation:** 

**[3826.18s] English:** All the time, so the fact that they contribute more to open source is so sensible because  
**Translation:** Vocabulary: sensible: 合乎情理的

**[3831.80s] English:** They're probably what we're protecting, you know, my engineers' brothers are in that company.  
**Translation:** 

**[3837.28s] English:** Their friends are in that company, and they're in that company, and they're in that company, and they're.  
**Translation:** 

**[3838.98s] English:** All schoolmates.  
**Translation:** 

**[3840.00s] English:** You know, the schoolmate concept is one schoolmate, your brother for life. And so they share knowledge very, very quickly. And so there's no sense in keeping technology hidden; you might as well put it on open source. And so the open source community then amplifies and accelerates the innovation process.  
**Translation:** Vocabulary: accelerates: 加速; amplifies: 放大; schoolmate: 同学; schoolmates: 同学们

**[3862.40s] English:** So, you get this rapid, incredible, great talent, rapid innovation because of open source—and just, you know, the nature of friends and intense competition among companies.  
**Translation:** 

**[3877.06s] English:** What emerges is incredible stuff.  
**Translation:** Vocabulary: emerges: 出现

**[3880.20s] English:** And so, this is the fastest-innovating country in the world today.  
**Translation:** 

**[3885.32s] English:** And this is something that has everything I've just said is fundamental to how the kids were grown.  
**Translation:** 

**[3891.86s] English:** The fact that they have excellent education, the fact that their parents want them to do well in school, and the fact that their culture is that way.  
**Translation:** 

**[3900.28s] English:** These are, you know, just things about their country.  
**Translation:** 

**[3903.60s] English:** And they showed up at precisely the time when technology is going through that exponential growth.  
**Translation:** 

**[3909.26s] English:** Plus, culturally, it's pretty cool to be an engineer.  
**Translation:** Vocabulary: culturally: 文化上; exponential: 指数的; precisely: 精确地

**[3912.40s] English:** It connects to all the components that you're mentioning.  
**Translation:** 

**[3916.62s] English:** It's a builder nation.  
**Translation:** 

**[3918.10s] English:** It's a builder nation.  
**Translation:** 

**[3918.98s] English:** Yeah, it's a builder nation.  
**Translation:** 

**[3920.52s] English:** Our country's leaders.  
**Translation:** 

**[3922.02s] English:** Incredible.  
**Translation:** 

**[3922.86s] English:** But they're mostly lawyers.  
**Translation:** 

**[3925.16s] English:** Their country's leaders.  
**Translation:** 

**[3926.32s] English:** And because they're trying to keep us safe.  
**Translation:** 

**[3928.86s] English:** The rule of law, governing their country, was built out of poverty.  
**Translation:** 

**[3935.30s] English:** And so, most of their leaders are incredible engineers.  
**Translation:** 

**[3940.38s] English:** Some of the brightest minds.  
**Translation:** 

**[3942.78s] English:** To take a small tangent, because you mentioned open source, I have to go to Perplexity here, who you have been a fan of for a long time.  
**Translation:** 

**[3951.14s] English:** I love it.  
**Translation:** 

**[3951.68s] English:** Yeah.  
**Translation:** 

**[3951.86s] English:** And thank you for releasing open-source Nematron 3.0, which you can also use inside Perplexity to look stuff up now.  
**Translation:** Vocabulary: nematron: 内马tron; perplexity: 困惑

**[3959.86s] English:** Thank you.  
**Translation:** 

**[3960.00s] English:** Which is a 120 billion-parameter open-weight MOE model.  
**Translation:** 

**[3965.54s] English:** What's your vision with open source?  
**Translation:** 

**[3969.18s] English:** So, you mentioned China with DeepSeek and Minimax.  
**Translation:** Vocabulary: minimax: 最大最小值法

**[3973.62s] English:** With all these companies really pushing forward,  
**Translation:** 

**[3977.08s] English:** The open-source AI movement.  
**Translation:** 

**[3980.38s] English:** And NVIDIA is really leading the way.  
**Translation:** 

**[3982.14s] English:** In close to state-of-the-art open-source LLMs.  
**Translation:** 

**[3987.16s] English:** What's your vision there?  
**Translation:** 

**[3988.76s] English:** First off,  
**Translation:** 

**[3990.00s] English:** If we are going to be a great AI computing company,  
**Translation:** 

**[3992.60s] English:** We have to understand how AI models are evolving.  
**Translation:** Vocabulary: computing: 计算; evolving: 演变

**[3996.28s] English:** One of the things that I love about Nemotron 3:  
**Translation:** 

**[3998.70s] English:** It's not just a pure transformer model.  
**Translation:** Vocabulary: nemotron: 奈莫tron

**[4002.60s] English:** It's transformers and SSMs.  
**Translation:** 

**[4005.30s] English:** And we were early in developing the conditional GANs.  
**Translation:** Vocabulary: conditional: 条件性的

**[4011.94s] English:** That progressive GANs,  
**Translation:** 

**[4013.38s] English:** Which led, step by step, to diffusion.  
**Translation:** Vocabulary: diffusion: 扩散

**[4015.88s] English:** And so, the fact that we're doing basic research,...  
**Translation:** 

**[4019.02s] English:** And...  
**Translation:** 

**[4020.00s] English:** In model architecture and in different domains.  
**Translation:** 

**[4023.06s] English:** Gives us visibility into, you know,  
**Translation:** Vocabulary: visibility: 可见性

**[4026.20s] English:** What kind of computing systems?  
**Translation:** 

**[4027.54s] English:** It would do a good job for future models.  
**Translation:** 

**[4029.36s] English:** And so, it is part of our extreme co-design strategy.  
**Translation:** 

**[4033.02s] English:** Second,  
**Translation:** 

**[4034.70s] English:** I think we rightfully recognize.  
**Translation:** 

**[4038.36s] English:** That on the one hand,  
**Translation:** 

**[4041.64s] English:** We want world-class models as products.  
**Translation:** 

**[4044.82s] English:** And they should be proprietary.  
**Translation:** Vocabulary: proprietary: 专有技术

**[4047.28s] English:** On the other hand,  
**Translation:** 

**[4048.84s] English:** We also want....  
**Translation:** 

**[4050.00s] English:** We want AI to diffuse into every industry.  
**Translation:** 

**[4052.34s] English:** And every country,  
**Translation:** Vocabulary: diffuse: 分散

**[4053.70s] English:** Every researcher,  
**Translation:** 

**[4055.16s] English:** Every student.  
**Translation:** 

**[4057.10s] English:** And if everything is proprietary,  
**Translation:** 

**[4059.58s] English:** It's hard to do research.  
**Translation:** 

**[4061.02s] English:** And it's hard to innovate on top of.  
**Translation:** 

**[4064.14s] English:** Around,  
**Translation:** Vocabulary: innovate: 创新

**[4064.98s] English:** With.  
**Translation:** 

**[4066.34s] English:** And so, open source is fundamentally necessary.  
**Translation:** Vocabulary: fundamentally: 从根本上

**[4069.80s] English:** For many industries to join the AI revolution.  
**Translation:** 

**[4074.66s] English:** NVIDIA has the scale.  
**Translation:** 

**[4075.74s] English:** And we have the motives.  
**Translation:** 

**[4077.50s] English:** To not only...  
**Translation:** 

**[4079.86s] English:** For AI,  
**Translation:** 

**[4080.00s] English:** Skills, scale, and motivation to build and continue to build these AI models for as long as we shall.  
**Translation:** 

**[4081.84s] English:** But, for us to be able to do all the work,...  
**Translation:** 

**[4085.10s] English:** That we have to do to help us.  
**Translation:** 

**[4086.46s] English:** To change the world around us.  
**Translation:** 

**[4087.22s] English:** We'll be working on doing some of that.  
**Translation:** 

**[4088.58s] English:** So, if we can see that,  
**Translation:** 

**[4088.88s] English:** Live and so, therefore, we ought to do that. We can open up and activate every industry, every  
**Translation:** 

**[4090.06s] English:** You know,  
**Translation:** 

**[4090.10s] English:** I think we have a year and a half.  
**Translation:** 

**[4092.14s] English:** To do more research.  
**Translation:** 

**[4093.58s] English:** And I think that's going to be something.  
**Translation:** 

**[4095.12s] English:** That we have to look at for the future.  
**Translation:** 

**[4095.68s] English:** Researcher, you know, every country needs to be able to join the AI revolution, and there's the third reason.  
**Translation:** 

**[4097.14s] English:** So, if we could look into the future,  
**Translation:** 

**[4098.34s] English:** It's going to be very, very, very important.  
**Translation:** 

**[4100.40s] English:** To do that.  
**Translation:** 

**[4100.60s] English:** And I'm certainly looking forward to seeing.  
**Translation:** 

**[4101.80s] English:** The way we can do this.  
**Translation:** 

**[4102.26s] English:** Which is from that to recognizing that AI is not just about language; these AIs will likely use  
**Translation:** 

**[4103.42s] English:** I mean....  
**Translation:** 

**[4103.92s] English:** So, thank you for all your time.  
**Translation:** 

**[4104.70s] English:** And I think that's it.  
**Translation:** 

**[4106.04s] English:** For our discussion today.  
**Translation:** 

**[4106.72s] English:** Thank you.  
**Translation:** 

**[4107.18s] English:** Thank you.  
**Translation:** 

**[4107.36s] English:** Thank you.  
**Translation:** 

**[4107.54s] English:** Thank you.  
**Translation:** 

**[4107.66s] English:** Thank you.  
**Translation:** 

**[4108.00s] English:** Thank you.  
**Translation:** 

**[4108.68s] English:** Thank you.  
**Translation:** 

**[4110.54s] English:** Tools, and models, and sub-agents that were trained on other modalities of information.  
**Translation:** Vocabulary: modalities: 信息模态

**[4119.28s] English:** Maybe it's biology or chemistry, or um, you know, laws of physics or you know, fluids and  
**Translation:** 

**[4126.22s] English:** Thermodynamics, and not all of it is in language structure, and so somebody has to go make sure.  
**Translation:** Vocabulary: fluids: 流体; thermodynamics: 热力学

**[4132.24s] English:** That, weather prediction, biology, AI, AI for biology, physical AI — all of that stuff stays.  
**Translation:** 

**[4142.64s] English:** Can be pushed to the limits and pushed to the frontier. We don't build cars, but we want to make.  
**Translation:** Vocabulary: frontier: 最前沿

**[4147.36s] English:** Sure, every car company has access to great models. We don't discover drugs, but I want to.  
**Translation:** 

**[4152.38s] English:** Make sure that Lily has the world's best biology AI systems so that they can go use it for.  
**Translation:** 

**[4158.18s] English:** Discovering drugs: so, these three fundamental reasons.  
**Translation:** 

**[4161.64s] English:** You.  
**Translation:** 

**[4162.24s] English:** Both in recognizing that AI is not just about language, that AI is really broad, and that we want  
**Translation:** 

**[4167.64s] English:** To engage everybody in the world of AI, and then also co-design of AI, well, I have to say once again,  
**Translation:** 

**[4174.02s] English:** Thank you so much for truly open-sourcing NEMATRON 3. I appreciate it.  
**Translation:** 

**[4179.76s] English:** For saying that, we open-source the models, we open-source the weights, and we open-source the data.  
**Translation:** 

**[4183.82s] English:** We open-sourced how we created it. Yeah, it's pretty amazing; it's really incredible.  
**Translation:** 

**[4190.02s] English:** You're originally from  
**Translation:** 

**[4192.24s] English:** Taiwan has a close relationship with TSMC, so I have to ask—uh, TSMC—I think, uh  
**Translation:** 

**[4200.00s] English:** Also, it is a legendary company in terms of its engineering teams.  
**Translation:** Vocabulary: legendary: 传奇的

**[4203.70s] English:** Incredible engineering work that they do. What do you understand about TSMC's culture and?  
**Translation:** 

**[4210.28s] English:** Their approach, which explains how they're able to achieve this singular, unmatched success, is quite fascinating.  
**Translation:** 

**[4217.40s] English:** Everything they're doing with semiconductors, you know, first of all, the deepest misunderstanding.  
**Translation:** 

**[4222.76s] English:** About TSMC, what's notable is that their technology is essentially all they have; somehow, they seem to have a  
**Translation:** Vocabulary: semiconductors: 半导体

**[4236.06s] English:** Really great transistor, and if somebody shows up with another transistor, game over—it's the technology.  
**Translation:** 

**[4242.90s] English:** And, of course, you know I don't mean just the transistors and metallization systems; the  
**Translation:** Vocabulary: transistor: 晶体管; transistors: 晶体管

**[4248.00s] English:** Packaging the 3D, packaging the silicon photonics that you know, all of the  
**Translation:** 

**[4252.62s] English:** Technology that they're concerned about is that it's a technology that they've  
**Translation:** Vocabulary: photonics: 光子学; silicon: 硅

**[4252.74s] English:** They are concerned that it is a technology that they are  
**Translation:** 

**[4252.76s] English:** That technology is really what makes the company special. Their technology makes the company special. But their ability to orchestrate the demands—the dynamic demands of hundreds of companies in the world—as they're moving up, shifting out, increasing, decreasing, pushing out, pulling in, changing from customer to customer.  
**Translation:** Vocabulary: decreasing: 减少; orchestrate: 协调; shifting: 变化

**[4282.76s] English:** Wafer starting, wafer stopping, emergency wafer starts. All of this dynamics of the world's complexity, as the world is shifting all the time. And somehow, they're running a factory with high throughput, high yields, really great costs, and excellent customer service.  
**Translation:** 

**[4306.58s] English:** They take their promises very seriously.  
**Translation:** Vocabulary: complexity: 复杂性; throughput: 产能; wafer: 晶圆; yields: 产量

**[4310.56s] English:** Because they know that they're helping you.  
**Translation:** 

**[4312.76s] English:** When the wafers were promised to show up, they showed up so that you could run your company appropriately.  
**Translation:** Vocabulary: appropriately: 适当地; wafers: 晶圆

**[4320.00s] English:** And so, their manufacturing system is completely miraculous. I would say that the second thing is their culture. This culture is simultaneously technology-focused on one hand, advancing technology, and simultaneously customer-service-oriented on the other hand.  
**Translation:** 

**[4337.62s] English:** A lot of companies are very customer-service oriented, but they're not very technology-excellent. They're not at the bleeding edge of technology. There are a lot of companies who are at the bleeding edge of technology, but they're not the best customer-service oriented company.  
**Translation:** Vocabulary: advancing: 进步; miraculous: 奇迹; oriented: 导向

**[4351.98s] English:** And so it just depends on how they've balanced these two things, and they're world-class at both. And then, probably the third thing is the technology that I most value in them — that they created this.  
**Translation:** 

**[4367.62s] English:** An intangible called trust. I trust them to put my company on top, and that's a very big deal.  
**Translation:** Vocabulary: balanced: 权衡; intangible: 无形

**[4375.24s] English:** Well, they trust. I mean, there's a really close relationship there that you have established, and that trust is based on many years of performance, but there are also human relationships involved there as well.  
**Translation:** 

**[4385.14s] English:** Three decades. I don't know how many tens, hundreds of billions of dollars of business we've done through them, and we don't have a contract. That's pretty great.  
**Translation:** 

**[4395.32s] English:** Amazing. Okay, there's the story.  
**Translation:** 

**[4398.24s] English:** That in 2013, the founders of TSMC, Morris Chang, offered you the chance to become TSMC's chief executive. And you said you already had a job. Is this story true?  
**Translation:** Vocabulary: chang: 变化; founders: 创始人

**[4409.98s] English:** The story is true. I didn't dismiss it, but I was deeply honored. And of course, I knew then, as I know now, that TSMC is one of the most consequential companies in history.  
**Translation:** 

**[4423.90s] English:** Yeah.  
**Translation:** Vocabulary: consequential: 有重大影响的; dismiss: 否定

**[4425.78s] English:** And Morris is one of the...  
**Translation:** 

**[4427.62s] English:** The highest-regarded executive and business, as well as personal, friend that I've had in my life. And for him to ask is...  
**Translation:** 

**[4440.00s] English:** Uh, um, I was humbled and really honored. Um, but the work that I'm doing,...  
**Translation:** 

**[4446.96s] English:** Here is really important. And I've seen, you know, in my mind's eye,  
**Translation:** Vocabulary: humbled: 谦卑

**[4452.34s] English:** What NVIDIA was going to be, and what the impact that we could have. And, um, it was really  
**Translation:** 

**[4458.90s] English:** Important work. Uh, and it's my responsibility—my sole responsibility—to make this happen.  
**Translation:** 

**[4464.64s] English:** Happen. And so, I declined it, you know, not because it wasn't an  
**Translation:** 

**[4472.62s] English:** Incredible offer. Uh, it's an unbelievable offer. Um, but, but I simply couldn't take it.  
**Translation:** Vocabulary: declined: 拒绝了

**[4478.80s] English:** I think NVIDIA, both NVIDIA and TSMC, are two of the greatest companies in the history of humanity.  
**Translation:** 

**[4484.82s] English:** Civilization and running either one, I'm sure, is an incredibly complicated effort and takes,  
**Translation:** 

**[4489.94s] English:** You have to truly be all in, uh, everybody at every scale.  
**Translation:** 

**[4494.06s] English:** Not just at the,  
**Translation:** 

**[4494.64s] English:** At the CEO level, everyone is really, truly all in to accomplish this kind of complexity.  
**Translation:** 

**[4500.56s] English:** See, now I can help both companies.  
**Translation:** Vocabulary: complexity: 复杂性

**[4502.16s] English:** Exactly. Um, so, NVIDIA is now the most valuable company in the world. I have to ask, what is the  
**Translation:** 

**[4510.26s] English:** NVIDIA's biggest moat, as the folks in the tech sector say, is the edge you have that  
**Translation:** 

**[4517.34s] English:** Protects you from the competition?  
**Translation:** 

**[4520.28s] English:** Our single most important, uh,  
**Translation:** 

**[4524.64s] English:** Property as a company is the installed base of our computing platform. Our single most important  
**Translation:** 

**[4533.10s] English:** The thing is, today is our install base for CUDA. Now, the reason why, uh,  
**Translation:** Vocabulary: computing: 计算

**[4540.50s] English:** 20 years ago, of course, there was no install base, but what makes, and if somebody,  
**Translation:** 

**[4548.04s] English:** If somebody came up with a GUDA or TUDA, it wouldn't make any difference at all.  
**Translation:** 

**[4554.64s] English:** And the reason for that is because it's never been just about the technology.  
**Translation:** 

**[4559.16s] English:** The technology of  
**Translation:** 

**[4559.90s] English:** .  
**Translation:** 

**[4560.00s] English:** Course, he was an incredible visionary. But it's the fact that the company was dedicated to it,  
**Translation:** Vocabulary: visionary: 有远见的人

**[4567.02s] English:** Stuck with it and expanded its reach. It wasn't just three people that made CUDA successful. It was  
**Translation:** 

**[4574.26s] English:** 43,000 people that made CUDA successful, and several million developers that believed in us.  
**Translation:** 

**[4581.62s] English:** That trusted that we were going to continue to make CUDA 1, 2, 3, and 13, that they decided to port.  
**Translation:** 

**[4588.34s] English:** And they dedicate their software on top of it, their mountain of software on top of it.  
**Translation:** Vocabulary: dedicate: 奉献

**[4592.88s] English:** And so, the install base is the number one most important advantage. That install base,  
**Translation:** 

**[4599.56s] English:** When you amplify it with the velocity of our execution, at the scale that we're talking about,  
**Translation:** Vocabulary: amplify: 放大; execution: 执行

**[4605.42s] English:** No company in history had ever built systems of this complexity, period.  
**Translation:** 

**[4610.80s] English:** And then, building it once a year is impossible.  
**Translation:** Vocabulary: complexity: 复杂性

**[4616.18s] English:** And that's...  
**Translation:** 

**[4618.34s] English:** Velocity combined with the install base, in the developer's mind,  
**Translation:** 

**[4624.20s] English:** You just can now take a developer's mind. From the developer's perspective, if I support CUDA,  
**Translation:** 

**[4630.98s] English:** Tomorrow, it will be 10 times better. I just have to wait six months on average.  
**Translation:** 

**[4636.54s] English:** Not only that, if I develop it on CUDA, I can reach a few hundred million people.  
**Translation:** 

**[4642.68s] English:** Computers. I'm in every cloud. I'm in every computer company. I'm in every single industry.  
**Translation:** 

**[4648.36s] English:** I'm in every single country.  
**Translation:** 

**[4651.00s] English:** So, if I create an open-source package and put it on CUDA first,  
**Translation:** 

**[4655.44s] English:** I get both attributes simultaneously.  
**Translation:** 

**[4660.32s] English:** And not only that,  
**Translation:** Vocabulary: attributes: 特性

**[4662.26s] English:** I trust 100% that NVIDIA is going to keep CUDA around, maintain it, and improve it.  
**Translation:** 

**[4670.84s] English:** And keep optimizing the libraries for as long as they shall live.  
**Translation:** Vocabulary: optimizing: 优化

**[4676.88s] English:** You could take that to the bank, and that library....  
**Translation:** 

**[4678.20s] English:** You could take that to the bank, and that library....  
**Translation:** 

**[4680.00s] English:** You put all that stuff together, and if I were a developer today, I would target CUDA first. I would target it most. And that's the reason I think, in the final analysis, is our first core advantage.  
**Translation:** 

**[4698.10s] English:** Our second one is our ecosystem. The fact that we vertically integrated this incredibly complex system, but we also integrated horizontally into every single company's computers. We're in the Google Cloud, we're in Amazon, we're in Azure. We're ramping up AWS like crazy right now. We're in new companies like CoreWeave and Scale. We're in supercomputers at Lilly. We're in enterprise computers. We're at the edge in radio base stations.  
**Translation:** Vocabulary: horizontally: 横向整合; integrated: 整合; ramping: 迅速增加; supercomputers: 超级计算机; vertically: 纵向

**[4727.32s] English:** You know, I'm just...  
**Translation:** 

**[4728.10s] English:** It's just crazy. One architecture is used in all these different systems. We're in cars, we're in robots, we're in satellites. We're out in space. And so, the fact that you have this one architecture and such a broad ecosystem, it basically covers every single industry in the world.  
**Translation:** 

**[4743.32s] English:** Well, how will the CUDA install base evolve into the future with AI factories as a moat? Do you think it's possible that NVIDIA in the future is all about the AI factory?  
**Translation:** 

**[4755.54s] English:** Well, the unit of computing...  
**Translation:** Vocabulary: computing: 计算; evolve: 演变

**[4758.10s] English:** It used to be GPU to us. Then it became a computer. Then it became a cluster. Now it's an entire AI factory. When I see a computer, when I see what NVIDIA builds, in the old days, I visualized the chip. And then, when I announced a new product, like, new generation—like, "Ladies and gentlemen, we're announcing Ampere today"—I picked up the chip.  
**Translation:** 

**[4779.86s] English:** Yeah.  
**Translation:** Vocabulary: ampere: 安培; cluster: 集群; visualized: 想象

**[4780.14s] English:** That was my mental model of what I was building. Today, I wouldn't say picking up the chip is kind of still adorable.  
**Translation:** 

**[4787.56s] English:** Yeah.  
**Translation:** 

**[4788.10s] English:** Adorable. It's not my mental model of what I'm doing. My mental model is this giant, gigawatt thing that has power generation connections.  
**Translation:** 

**[4800.00s] English:** To the grid, it's got cooling systems and networking of incredible monstrosity, you know.  
**Translation:** Vocabulary: gigawatt: 兆瓦; monstrosity: 怪兽般的东西

**[4805.24s] English:** 10,000 people are in there trying to install it; hundreds of networking engineers are in there.  
**Translation:** 

**[4810.88s] English:** Thousands of engineers behind it, trying to power it up—you know, powering up one of those factories.  
**Translation:** 

**[4816.18s] English:** As you know, it's not something that one person can do; it takes thousands of people to make it happen now.  
**Translation:** 

**[4822.70s] English:** Mentally, you're actually thinking about a single unit of compute, and you're like,  
**Translation:** Vocabulary: compute: 计算

**[4826.46s] English:** Literally, when you go to bed at night, you're thinking about a collection of racks and pods.  
**Translation:** 

**[4832.20s] English:** Not individual chips, but the entire infrastructure. And I'm hoping my next click is when I'm thinking.  
**Translation:** 

**[4836.78s] English:** About building computers, it's you know, planetary scale—that'll be the next big thing. What do you think?  
**Translation:** 

**[4842.80s] English:** About the space angle that Elon has talked about, doing computation in space to solve some of the  
**Translation:** Vocabulary: computation: 计算

**[4850.20s] English:** It makes some of the energy issues, in terms of scaling energy, easier.  
**Translation:** 

**[4856.08s] English:** You.  
**Translation:** 

**[4856.46s] English:** Cooling issues are not easy, you know. Cooling, well, there's a large number of engineering considerations involved.  
**Translation:** 

**[4861.36s] English:** Complexities involved with that, yeah. So, what you know, NVIDIA has also announced that you're already.  
**Translation:** Vocabulary: complexities: 复杂性

**[4867.58s] English:** Thinking about that, yeah, we're already there. NVIDIA GPUs are the first GPUs in space.  
**Translation:** 

**[4872.84s] English:** And, um, I didn't realize it was so interesting; I would have declared it maybe.  
**Translation:** 

**[4879.68s] English:** We're in space, you know—little astronaut suit on one of our GPUs.  
**Translation:** 

**[4886.46s] English:** But, but we've been in space; it's the right place to do a lot of imaging, you know.  
**Translation:** 

**[4892.44s] English:** Those satellites have really high-resolution imaging systems, and they're sweeping the Earth.  
**Translation:** 

**[4897.30s] English:** You know, continuously now, and you want centimeter-scale imaging that is.  
**Translation:** Vocabulary: sweeping: 全面覆盖

**[4904.76s] English:** Done continuously, uh, for the world, so that you'll basically have real-time telemetry.  
**Translation:** 

**[4910.66s] English:** Of everything, uh, you don't want to beam that back down to Earth; it's just, you know,  
**Translation:** Vocabulary: telemetry: 遥测数据

**[4916.34s] English:** You don't want to beam that back down to Earth; it's just, you know, you don't want to beam that.  
**Translation:** 

**[4916.46s] English:** Back down to Earth; it's just that you don't want to beam that back down to Earth, petabytes and petabytes of data.  
**Translation:** Vocabulary: petabytes: 千兆字节

**[4918.84s] English:** Petabytes and petabytes of data.  
**Translation:** 

**[4918.86s] English:** Petabytes and petabytes of data—you've got to just do AI.  
**Translation:** 

**[4920.00s] English:** You've got to just do AI.  
**Translation:** 

**[4920.00s] English:** There, at the edge, throw away everything you don't need; you've seen it before and it didn't change.  
**Translation:** 

**[4924.48s] English:** And then just keep the stuff that you need, and so AI ought to be done at the edge.  
**Translation:** 

**[4929.12s] English:** Um, obviously, we have a 24/7 solar system if we put it at the poles, and um, uh,  
**Translation:** 

**[4939.04s] English:** But you know, there's no conduction, no convection, and so you're pretty much just radiation.  
**Translation:** 

**[4945.44s] English:** And, um, you know, space is big. I guess we're just going to put big, giant radiators out there.  
**Translation:** Vocabulary: conduction: 热传导; convection: 对流; radiators: 散热器

**[4951.92s] English:** How crazy of an idea do you think it is—like, is this five years out, ten years out, twenty years out?  
**Translation:** 

**[4956.88s] English:** Out. So, uh, we're talking about blockers for AI scaling. You know, I'm just a lot more practical.  
**Translation:** 

**[4962.80s] English:** I look for where my next bucket of opportunities are first.  
**Translation:** 

**[4971.28s] English:** Meanwhile, I'm cultivating space, and so I sent engineers.  
**Translation:** Vocabulary: cultivating: 培育

**[4975.44s] English:** Uh, to go work on the problem, we're starting, and we're learning a lot about it.  
**Translation:** 

**[4980.40s] English:** How do we handle radiation? How do we address degrading performance? How do we deal with...  
**Translation:** Vocabulary: degrading: 性能下降

**[4985.68s] English:** Continuous, uh, testing and attestation of defects, and how do we deal with them?  
**Translation:** 

**[4992.48s] English:** Redundancy, and how do we degrade gracefully, and things like that. So, we could do  
**Translation:** Vocabulary: defects: 缺陷; degrade: 降级; redundancy: 冗余

**[4998.88s] English:** What about software? How do you think about software, redundancy, and performance?  
**Translation:** 

**[5005.44s] English:** So, that the computer never breaks; it just gets slower, you know. And um, I suppose we could start.  
**Translation:** 

**[5013.68s] English:** Doing a lot of engineering exploration up front, but in the meantime, my favorite answer is...  
**Translation:** 

**[5019.76s] English:** Eliminate waste. You know, we've got all that idle power; I want to evacuate it as fast as possible.  
**Translation:** Vocabulary: evacuate: 撤离; meantime: meantime

**[5025.20s] English:** Possible, yeah, yeah, there's a lot of low-hanging fruit here on Earth, yeah, that we can utilize.  
**Translation:** 

**[5032.24s] English:** Uh, for AI scaling, uh, quick pause.  
**Translation:** Vocabulary: utilize: 利用

**[5035.44s] English:** Quick 30-second thank you to our sponsors. Check them out in the description.  
**Translation:** 

**[5040.00s] English:** It really is the best way to support this podcast.  
**Translation:** Vocabulary: sponsors: 赞助商

**[5042.72s] English:** Go to lexfriedman.com/sponsors.  
**Translation:** 

**[5046.26s] English:** We got Perplexity for curiosity-driven knowledge exploration, Shopify for selling stuff online,  
**Translation:** Vocabulary: perplexity: 困惑; shopify: 电子商务平台

**[5053.04s] English:** Element for electrolytes, Finn for customer service AI agents, and Quo for a phone system.  
**Translation:** 

**[5060.18s] English:** Like calls, texts, and contacts for your business.  
**Translation:** 

**[5063.86s] English:** Choose wisely, my friends.  
**Translation:** 

**[5065.52s] English:** And now, back to my conversation with Jensen Kwong.  
**Translation:** 

**[5070.00s] English:** Do you think NVIDIA may be worth $10 trillion at some point?  
**Translation:** 

**[5076.00s] English:** Let's ask it this way.  
**Translation:** Vocabulary: trillion: 兆

**[5077.84s] English:** What does the future of the world look like if that's true?  
**Translation:** 

**[5084.80s] English:** I think that NVIDIA's growth is extremely likely, and in my mind, inevitable.  
**Translation:** 

**[5095.20s] English:** And let me explain why.  
**Translation:** 

**[5096.64s] English:** We're the largest computer company in history.  
**Translation:** 

**[5100.00s] English:** That alone should beg the question: why?  
**Translation:** 

**[5104.24s] English:** And the reason, of course—two reasons.  
**Translation:** 

**[5106.78s] English:** First, two foundational technical reasons:  
**Translation:** 

**[5110.46s] English:** The first reason is that computing went from being a retrieval-based, file-retrieval system.  
**Translation:** Vocabulary: computing: 计算; foundational: 基础的

**[5117.06s] English:** Almost everything is a file.  
**Translation:** 

**[5118.08s] English:** We pre-write something.  
**Translation:** 

**[5120.78s] English:** We pre-record something.  
**Translation:** 

**[5122.60s] English:** You know, we draw something.  
**Translation:** 

**[5124.06s] English:** We put it on the web.  
**Translation:** 

**[5124.72s] English:** We put it in a file.  
**Translation:** 

**[5125.32s] English:** And we use a recommender system, some smart filter.  
**Translation:** 

**[5129.12s] English:** To figure it out.  
**Translation:** Vocabulary: recommender: 推荐系统

**[5130.10s] English:** What to retrieve for you?  
**Translation:** 

**[5131.50s] English:** And so we were a pre-recording, human-pre recording, and file-retrieving system.  
**Translation:** Vocabulary: retrieve: 找回

**[5136.60s] English:** That's what a computer is, largely.  
**Translation:** 

**[5139.38s] English:** To now, AI computers are contextually aware.  
**Translation:** 

**[5143.42s] English:** Which means that it has to process and generate tokens in real time.  
**Translation:** 

**[5147.28s] English:** So, we went from a retrieval-based computing system to a generative-based computing system.  
**Translation:** 

**[5153.50s] English:** We're going to need a lot more processing in this new world than in the old world.  
**Translation:** 

**[5157.82s] English:** We need a lot of storage in the old world.  
**Translation:** 

**[5160.00s] English:** In the old world, we needed a lot of computation, but in this new world, we need even more, and so that's the first part.  
**Translation:** 

**[5167.40s] English:** Of it, we fundamentally changed computing in the way it is done. The only thing that,...  
**Translation:** Vocabulary: computation: 计算; fundamentally: 根本上

**[5173.00s] English:** Would cause it to go back is if this way of computation, this way of computing, generating.  
**Translation:** 

**[5179.52s] English:** Information that is contextually relevant, situationally aware, and grounded in new data.  
**Translation:** Vocabulary: situationally: 情境地

**[5186.40s] English:** Insight before it generates information in this computation-intensive way of doing computing.  
**Translation:** 

**[5192.36s] English:** Would only go back if it's not effective, so for the last 10-15 years, while working on deep learning.  
**Translation:** Vocabulary: computing: 计算; generates: 生成

**[5200.06s] English:** If, at any single moment, I would have come to the conclusion that, you know, what this is not,...  
**Translation:** 

**[5207.70s] English:** Going to work out, I think this is a dead end, or it's not going to scale; it's not going to solve.  
**Translation:** 

**[5212.00s] English:** This modality is not going to be used in this application, then of course I would feel very  
**Translation:** 

**[5216.26s] English:** Different.  
**Translation:** Vocabulary: modality: 方式

**[5216.40s] English:** About it, but I think the last five years have given me more confidence than the last ten years.  
**Translation:** 

**[5223.62s] English:** The previous 10 years, the second idea is computers because it was a storage system.  
**Translation:** 

**[5229.70s] English:** It was largely a warehouse, and we're now building factories; warehouses don't make much money.  
**Translation:** 

**[5238.58s] English:** Factories directly correlate with a company's revenues.  
**Translation:** Vocabulary: correlate: 相关; revenues: 收入; warehouse: 仓库; warehouses: 仓库

**[5244.10s] English:** And so  
**Translation:** 

**[5246.40s] English:** The computer did two things: not only did it change the way it did it, but its purpose in the world also shifted.  
**Translation:** Vocabulary: shifted: 改变

**[5255.08s] English:** Changed, it's no longer a computer; it's a factory. It's used for generating revenues.  
**Translation:** 

**[5262.86s] English:** We're now seeing not only is this factory generating products and commodities that people  
**Translation:** 

**[5271.04s] English:** We want to consume, and we're seeing that the commodities are so interesting.  
**Translation:** 

**[5276.26s] English:** Valuable to so many different audiences.  
**Translation:** 

**[5280.00s] English:** That the tokens are starting to segment, like iPhones.  
**Translation:** 

**[5283.66s] English:** You have free tokens, you have premium tokens.  
**Translation:** Vocabulary: premium: 高级的; segment: 划分

**[5287.88s] English:** And you have several tokens in the middle.  
**Translation:** 

**[5290.26s] English:** And so, intelligence, as it turns out,  
**Translation:** 

**[5293.42s] English:** You know, it's a scalable product.  
**Translation:** 

**[5295.40s] English:** There's extremely high-intelligence products,  
**Translation:** Vocabulary: scalable: 可扩展的

**[5297.84s] English:** Tokens that are used for specialized things.  
**Translation:** 

**[5300.60s] English:** People will be willing to pay, you know,  
**Translation:** 

**[5302.76s] English:** The idea that somebody's willing to pay  
**Translation:** 

**[5304.74s] English:** $1,000 per million tokens is just around the corner.  
**Translation:** 

**[5309.70s] English:** It's not if, but only when.  
**Translation:** 

**[5312.44s] English:** And so, now we're seeing that the commodity  
**Translation:** Vocabulary: commodity: 商品

**[5316.32s] English:** That what this factory makes is actually valuable.  
**Translation:** 

**[5319.12s] English:** And it is revenue-generating and profit-generating.  
**Translation:** 

**[5322.40s] English:** Now, the question is: How many of these factories?  
**Translation:** 

**[5324.84s] English:** Does the world need something in particular?  
**Translation:** 

**[5327.90s] English:** How many tokens does the world need?  
**Translation:** 

**[5331.98s] English:** And how much is society willing to pay for these tokens?  
**Translation:** 

**[5338.88s] English:** And,...  
**Translation:** 

**[5339.70s] English:** What would happen to the world's economy?  
**Translation:** 

**[5341.82s] English:** If productivity were to improve so substantially?  
**Translation:** 

**[5346.82s] English:** What would happen?  
**Translation:** 

**[5348.48s] English:** Are we going to discover new drugs, new products, or new services?  
**Translation:** 

**[5352.44s] English:** And so, when you take these things in combination,  
**Translation:** 

**[5355.64s] English:** I am absolutely certain.  
**Translation:** 

**[5357.06s] English:** That the world's GDP is going to accelerate in growth.  
**Translation:** Vocabulary: accelerate: 加快

**[5362.12s] English:** I'm absolutely certain the percentage of that GDP.  
**Translation:** 

**[5366.56s] English:** That will be used for computation.  
**Translation:** Vocabulary: computation: 计算

**[5369.70s] English:** There will be a hundred times more than in the past.  
**Translation:** 

**[5372.52s] English:** Because it's no longer a storage unit.  
**Translation:** 

**[5375.60s] English:** It's a product generation unit.  
**Translation:** 

**[5378.48s] English:** And so, when you look at it in that context,  
**Translation:** 

**[5381.78s] English:** And then you back into what is NVIDIA's.  
**Translation:** 

**[5385.18s] English:** What does NVIDIA do?  
**Translation:** 

**[5387.78s] English:** And how much of that new economics and new industry,  
**Translation:** 

**[5393.28s] English:** Would we have to benefit to address?  
**Translation:** 

**[5396.24s] English:** I think we're going to be a lot, lot bigger.  
**Translation:** 

**[5398.46s] English:** And then the rest of it,  
**Translation:** 

**[5399.62s] English:** We're going to be a lot bigger.  
**Translation:** 

**[5400.00s] English:** To me, is it possible for NVIDIA to be a $3 trillion revenue company in the near future?  
**Translation:** Vocabulary: trillion: 万亿

**[5408.56s] English:** The answer is, of course, yes.  
**Translation:** 

**[5410.20s] English:** And the reason for that is because it's not limited by any physical constraints.  
**Translation:** Vocabulary: constraints: 限制

**[5415.20s] English:** There's nothing that I see that says, "Gosh, $3 trillion is not possible.  
**Translation:** 

**[5421.22s] English:** And, as it turns out, the burden of NVIDIA's supply chain is shared by 200 companies.  
**Translation:** Vocabulary: burden: 负担

**[5431.04s] English:** And the fact that we scale out on the backs of, with the partnership of this ecosystem, the question is: Do we have the energy to do so?  
**Translation:** 

**[5441.34s] English:** And surely, we will have the energy to do so.  
**Translation:** 

**[5445.16s] English:** And so, all of these things combined—that number is just a number.  
**Translation:** 

**[5451.22s] English:** And I still remember that NVIDIA was the first time we crossed a billion dollars.  
**Translation:** 

**[5457.76s] English:** I was reminded of a CEO who told me, Jensen: It's theoretically impossible for a fabulous semiconductor company to exceed a billion dollars.  
**Translation:** 

**[5467.68s] English:** And I won't bore you with why, but of course, it's illogical, and there's a lot of evidence we're not.  
**Translation:** Vocabulary: exceed: 超过; fabulous: 卓越的; illogical: 不合逻辑的; semiconductor: 半导体; theoretically: 理论上

**[5474.74s] English:** And then somebody told me, Jensen: "You'll never be more than $25 billion.  
**Translation:** 

**[5479.94s] English:** Because of some other company, somebody told me that you'll never be, you know, because—and then, so that those aren't principles-first reasoning.  
**Translation:** 

**[5492.18s] English:** And the simple way to think about that is: what do we make, and how large is the opportunity we can create?  
**Translation:** 

**[5502.02s] English:** Now, NVIDIA is not in the market-share business.  
**Translation:** 

**[5504.98s] English:** Almost everything that I just talked about doesn't exist.  
**Translation:** 

**[5508.68s] English:** That's the part that's hard.  
**Translation:** 

**[5509.94s] English:** You know, if NVIDIA was a $10 billion company trying to take market share from NVIDIA, then it's easy to see for shareholders.  
**Translation:** 

**[5520.00s] English:** That, oh, yeah, if they could just take a 10% share, they could be much larger. But it's hard for  
**Translation:** Vocabulary: shareholders: 股东

**[5528.02s] English:** People might imagine how large we could be, because there's nobody we could take a share from.  
**Translation:** 

**[5533.78s] English:** You know, and so I think that that's one of the challenges for the world is the imagination of  
**Translation:** 

**[5540.14s] English:** The future. But I've got plenty of time, and I'll keep reasoning about it and keep talking.  
**Translation:** 

**[5544.16s] English:** About it, and every single GTC will become more and more real, you know, and then more and more.  
**Translation:** 

**[5549.38s] English:** People talk about it in one of these days, you know. We'll get there, but I'm a hundred percent.  
**Translation:** 

**[5553.50s] English:** We'll get there. Yeah. This view of, you know, token factories—essentially, this token per second.  
**Translation:** Vocabulary: token: 代币

**[5559.72s] English:** Per watt, and every token having value—like it's an actual thing that brings value and it brings.  
**Translation:** 

**[5566.10s] English:** Different kinds of value, different amounts of value to different people. That's the  
**Translation:** 

**[5570.02s] English:** The actual product can really be loosely thought of as the token. And so you have a bunch of tokens.  
**Translation:** 

**[5574.26s] English:** Factors, and it's very easy. First, the principle is to imagine a future given all the potential things.  
**Translation:** Vocabulary: loosely: 大致地

**[5579.28s] English:** That AI can solve this will require an exponential number of additional token factories.  
**Translation:** 

**[5585.16s] English:** Yeah. And what's really interesting is the reason why I was so excited about it,  
**Translation:** Vocabulary: exponential: 成倍的

**[5589.78s] English:** The iPhone of tokens arrived. What do you call it? Wait, are you saying Open Clause iPhone?  
**Translation:** 

**[5593.86s] English:** Yeah. That's interesting. Agents. Yeah. Agents, in general. The iPhone of tokens.  
**Translation:** Vocabulary: clause: 条款

**[5600.68s] English:** Arrived. It is the fastest-growing application in history. It went straight up. Yeah. Went.  
**Translation:** 

**[5606.02s] English:** Straight up, that says something. Yup. There's no question.  
**Translation:** 

**[5609.28s] English:** Open Claw is the iPhone of tokens. Yeah. There's something truly, as you know,  
**Translation:** 

**[5614.58s] English:** Something truly special was happening from about December, where people really woke up to the  
**Translation:** 

**[5620.36s] English:** The power of cloud code and Codex of Open Claw. Um, I mean, I've been embarrassed to admit that on the way.  
**Translation:** 

**[5628.28s] English:** Here at the airport, I'm doing this for the first time in public, and I was "programming," quote unquote.  
**Translation:** Vocabulary: codex: 法典; unquote: 引号外

**[5636.30s] English:** By talking.  
**Translation:** 

**[5637.96s] English:** Yeah.  
**Translation:** 

**[5639.28s] English:** And I was embarrassed.  
**Translation:** 

**[5640.00s] English:** Because I was pretending like I'm talking to a human colleague.  
**Translation:** Vocabulary: colleague: 同行

**[5643.82s] English:** I'm not sure how I feel about the future where everybody is walking around talking to their AI, but it's such an efficient way to get stuff done.  
**Translation:** 

**[5653.12s] English:** And it's more likely that your AI is bothering you all the time.  
**Translation:** 

**[5657.76s] English:** And the reason for that is because it's getting stuff done so fast.  
**Translation:** 

**[5661.80s] English:** It's reporting back to you; I got that done.  
**Translation:** 

**[5664.34s] English:** What do you want me to do next?  
**Translation:** 

**[5665.52s] English:** You know, that's the part that I think most people don't realize: the person who's going to be chatting with them, texting them most, is their claw, is their lobster.  
**Translation:** Vocabulary: lobster: 龙虾

**[5677.50s] English:** What an incredible future!  
**Translation:** 

**[5679.88s] English:** I read that you attribute a lot of your success to your ability to work harder than anyone and withstand more suffering than anyone.  
**Translation:** Vocabulary: attribute: 归因; withstand: 承受

**[5686.56s] English:** So, we can list many of the things that entail.  
**Translation:** 

**[5690.50s] English:** I mean, dealing with failure and the cost of engineering problems we've talked about.  
**Translation:** Vocabulary: entail: 包含

**[5695.52s] English:** The human problems, uncertainties, responsibilities, exhaustion, embarrassment, and the near-death company moments that you've mentioned.  
**Translation:** 

**[5705.68s] English:** But also the pressure.  
**Translation:** Vocabulary: exhaustion: 疲劳; uncertainties: 不确定性

**[5707.52s] English:** Now, as the CEO of this company that economies and nations strategize around, plan their financial allocations around, and plan their AI infrastructure around.  
**Translation:** 

**[5723.06s] English:** How do you deal with this much pressure?  
**Translation:** Vocabulary: allocations: 资金分配; strategize: 制定策略

**[5725.52s] English:** What gives you strength, given how many nations and peoples depend on you?  
**Translation:** 

**[5737.28s] English:** I'm conscious of the fact that NVIDIA's success is very important to the United States.  
**Translation:** 

**[5746.70s] English:** We generate enormous amounts of tax revenues.  
**Translation:** 

**[5750.88s] English:** We establish technology leadership for our nation.  
**Translation:** Vocabulary: revenues: 税收收入

**[5754.20s] English:** Technology leadership is important.  
**Translation:** 

**[5755.52s] English:** It's important for national security.  
**Translation:** 

**[5757.32s] English:** National security is not just in one aspect.  
**Translation:** 

**[5760.00s] English:** Of national security, all aspects of national security. When our country is more prosperous,  
**Translation:** Vocabulary: prosperous: 繁荣昌盛

**[5765.28s] English:** We could do a better job with domestic policies and helping social benefits. Because we're  
**Translation:** 

**[5771.74s] English:** Generating so much re-industrialization in the United States, we're creating mountains of jobs.  
**Translation:** 

**[5777.42s] English:** We're helping shift how we build things back to the United States in so many different plants.  
**Translation:** 

**[5787.84s] English:** Chips, computers, and, of course, these manufacturing facilities. I'm completely aware.  
**Translation:** 

**[5793.68s] English:** And I have the benefit, and this is a real gift for mainstream investors.  
**Translation:** 

**[5805.54s] English:** Teachers, policemen who have somehow, for whatever reason, invested in NVIDIA, or because they watched,  
**Translation:** 

**[5812.98s] English:** Jim Cramer bought some stock and now they are millionaires.  
**Translation:** 

**[5817.84s] English:** And I am completely aware of that circumstance. I'm aware of the circumstance that NVIDIA  
**Translation:** Vocabulary: circumstance: 情况; cramer: 吉姆·克ramer; millionaires: 百万富翁

**[5826.64s] English:** Is central to a very large network of ecosystem partners behind us and downstream from us.  
**Translation:** 

**[5836.74s] English:** And so, the way I deal with that is exactly what I just did. I reasoned about  
**Translation:** Vocabulary: downstream: 下游的

**[5842.94s] English:** What is it that we're doing? What is it causing?  
**Translation:** 

**[5847.84s] English:** What's the impact that has on other people, positively or even through a great burden?  
**Translation:** Vocabulary: burden: 负担

**[5855.84s] English:** For example, to address the supply chain? And the question is, therefore, what are you going to do about it?  
**Translation:** 

**[5864.42s] English:** In almost everything that I feel, I break it down. I reason about: okay,  
**Translation:** 

**[5870.16s] English:** What's the circumstance? What has changed? What's hard? And what am I going to do about it?  
**Translation:** 

**[5876.14s] English:** And I break it down.  
**Translation:** 

**[5877.84s] English:** I decompose the problem.  
**Translation:** 

**[5880.00s] English:** And the decomposition of these circumstances turns it into manageable things that I can do.  
**Translation:** Vocabulary: decompose: 分解; decomposition: 分解

**[5889.88s] English:** And the only thing that I could do after that was ask, "Did you do it?  
**Translation:** 

**[5893.90s] English:** Did you do it, or did you get somebody else to do it?  
**Translation:** 

**[5897.06s] English:** And if you didn't do it, you reasoned that you needed to do it and you didn't do it, and you didn't get anybody else to do it, then stop crying about it, you know?  
**Translation:** 

**[5905.58s] English:** And so, I'm fairly tough on myself.  
**Translation:** 

**[5913.02s] English:** But I also break things down so that I don't panic.  
**Translation:** 

**[5918.54s] English:** I can go to sleep because I've made the list of things that needed to be done.  
**Translation:** 

**[5923.24s] English:** And I've made sure that everything that could put our company in harm's way, or my partners' or our industry's as well, I've told somebody.  
**Translation:** 

**[5934.04s] English:** Everything that I feel.  
**Translation:** 

**[5935.58s] English:** Could put anybody in harm's way; I've told someone.  
**Translation:** 

**[5940.18s] English:** And I've told someone who could do something about it.  
**Translation:** 

**[5943.42s] English:** And so, I've gotten it off my chest.  
**Translation:** 

**[5945.16s] English:** Or, I'm doing something about it.  
**Translation:** 

**[5947.32s] English:** And so after that, Lex, what else can you do?  
**Translation:** 

**[5950.54s] English:** So, given all the insane, intense amount of suffering on the journey of building up NVIDIA, have you hit low points psychologically?  
**Translation:** Vocabulary: psychologically: 心理上

**[5962.26s] English:** Oh, yeah.  
**Translation:** 

**[5962.80s] English:** Oh, yeah, sure.  
**Translation:** 

**[5963.90s] English:** All the time.  
**Translation:** 

**[5964.46s] English:** All the time.  
**Translation:** 

**[5965.58s] English:** All the time.  
**Translation:** 

**[5967.28s] English:** And there, you just break down the problem into pieces.  
**Translation:** 

**[5971.38s] English:** Yeah.  
**Translation:** 

**[5971.82s] English:** See what you can do about it.  
**Translation:** 

**[5973.76s] English:** And part of it, Lex, is forgetting.  
**Translation:** 

**[5978.68s] English:** One of the most important attributes of AI learning, as you know, is systematic forgetting.  
**Translation:** Vocabulary: attributes: 特性

**[5984.38s] English:** You need to know when to forget some things.  
**Translation:** 

**[5987.46s] English:** You can't memorize everything.  
**Translation:** Vocabulary: memorize: 记忆

**[5988.94s] English:** You can't keep everything.  
**Translation:** 

**[5990.46s] English:** And, you know, you don't want to carry everything.  
**Translation:** 

**[5993.40s] English:** One of the things that I do very quickly.  
**Translation:** 

**[5994.90s] English:** One of the things that I do very quickly is to decompose the problem.  
**Translation:** Vocabulary: decompose: 分解

**[5996.76s] English:** I reason about the problem.  
**Translation:** 

**[5997.96s] English:** And I share the load with it.  
**Translation:** 

**[5999.72s] English:** When I say.  
**Translation:** 

**[6000.00s] English:** I tell everybody: I'm essentially sharing that burden as quickly as possible. Whatever worries,...  
**Translation:** Vocabulary: burden: 负担

**[6007.14s] English:** Me, tell somebody else; don't just keep it to yourself, you know, don't let it decompose, and don't freak them out.  
**Translation:** 

**[6013.02s] English:** Decompose the problem into smaller parts and get people to do it, and inspire them to be able to go do it.  
**Translation:** 

**[6019.66s] English:** Something about it, but part of it is just forgetting, you know. A lot of it is you've got  
**Translation:** 

**[6025.64s] English:** To be tough on yourself, you know, just come on; stop crying about it. Let's get going, you know.  
**Translation:** 

**[6030.26s] English:** And then you get out of bed. And then the other part is that you're attracted to  
**Translation:** 

**[6036.12s] English:** The next shiny light, the next future, the next opportunity—okay, that's  
**Translation:** 

**[6041.08s] English:** Behind us, what's next? And it's a lot, I think. You know, you watch this with great athletes,...  
**Translation:** 

**[6046.56s] English:** They just worry about the next point. The last point is behind them, and the embarrassment.  
**Translation:** 

**[6054.16s] English:** The, you know,  
**Translation:** 

**[6055.64s] English:** You know, and then, and because I do so much of my job publicly, Lex, you do a fair  
**Translation:** 

**[6062.82s] English:** Amount of my job is publicly visible. And so, I do a lot of my job publicly. And so, um, you know,  
**Translation:** 

**[6068.38s] English:** I say a lot of things that seem sensible or funny at the time. Mostly, it's  
**Translation:** Vocabulary: sensible: 合乎情理的

**[6073.80s] English:** Just because it's funny to me at the time. And then, you know, you reflect on it; it's less.  
**Translation:** 

**[6077.92s] English:** Funny, but, yeah, no, trust me—I know. But you basically allow yourself to be pulled by  
**Translation:** 

**[6084.76s] English:** The light of the moment.  
**Translation:** 

**[6085.64s] English:** Of the future. Forget the past and just keep, keep, keep working towards that. I mean, you did.  
**Translation:** 

**[6090.62s] English:** Say there's this kind of famous thing. You said that, if you knew how hard it would be to  
**Translation:** 

**[6098.14s] English:** Build NVIDIA; uh, it turned out to be a million times harder than you anticipated.  
**Translation:** 

**[6104.56s] English:** That you wouldn't do it. Um, but it isn't, you know, when I hear that, that's probably true.  
**Translation:** 

**[6112.02s] English:** About everything worth doing, right?  
**Translation:** 

**[6113.68s] English:** Exactly.  
**Translation:** 

**[6115.64s] English:** Because, by the way, what I was trying to explain is that there's a, there's a,  
**Translation:** 

**[6120.00s] English:** Incredible superpower of being, um, having the mind of a child, yeah. You know, and I say,...  
**Translation:** 

**[6128.76s] English:** To myself, oftentimes when I look at something—and almost everything—my first  
**Translation:** Vocabulary: oftentimes: 经常; superpower: 超能力

**[6136.54s] English:** Thought is, how hard can it be? You know, and so on, and so on. You get yourself into that mode: How hard could it be?  
**Translation:** 

**[6143.34s] English:** It would be, and nobody's ever done it before. It looks gigantic, and it's going to cost hundreds of billions.  
**Translation:** Vocabulary: gigantic: 巨大的

**[6150.18s] English:** Of dollars, it's going to take you know, all this, and you just go, "Yeah, but how hard could it be?  
**Translation:** 

**[6154.84s] English:** You know, yeah, how hard could it be? Yeah, and so you've got to get yourself into that state of...  
**Translation:** 

**[6160.00s] English:** Mind, you don't want to actually over-simulate everything and all the setbacks.  
**Translation:** 

**[6167.00s] English:** All the trials and tribulations, and all the disappointments — you don't want to simulate all.  
**Translation:** Vocabulary: disappointments: 失望; setbacks: 挫折; simulate: 模拟; tribulations: 磨难

**[6170.86s] English:** That in advance, you don't want to know; you don't want to know that you don't want.  
**Translation:** 

**[6173.32s] English:** Want to go into a new experience thinking it's going to be perfect. It's going to be great.  
**Translation:** 

**[6177.86s] English:** It's going to be incredibly fun. And then, while you're there, you need to have endurance. You  
**Translation:** 

**[6184.50s] English:** Need to have grit so that when the setbacks actually happen, and those setbacks are  
**Translation:** Vocabulary: endurance: 毅力

**[6189.52s] English:** Going to surprise you, the disappointments aren't going to surprise you, the embarrassments are.  
**Translation:** 

**[6194.66s] English:** Going to surprise you: the humiliations are going to surprise you. Now you just have to turn on the  
**Translation:** Vocabulary: embarrassments: 尴尬; humiliations: 羞辱

**[6200.58s] English:** Other bit, which is just forget about it. Move on. Keep moving. And to the extent that,...  
**Translation:** 

**[6205.78s] English:** My assumptions about the future, and why the future is going to manifest.  
**Translation:** Vocabulary: assumptions: 假设; manifest: 显现

**[6215.66s] English:** So long as those assumptions and inputs don't change or didn't change materially,  
**Translation:** 

**[6222.56s] English:** Then, I should expect that the output won't change. And so, my simulated output of the future.  
**Translation:** Vocabulary: inputs: 输入; materially: 实质上; simulated: 模拟的

**[6228.74s] English:** Is still going to happen.  
**Translation:** 

**[6230.58s] English:** And if it's still going to happen, I'm still going to go after it. I believe it's going to,  
**Translation:** 

**[6235.22s] English:** You know, and so there's a combination of two or three human characteristics.  
**Translation:** 

**[6240.00s] English:** The ability to go into an experience fresh-minded, the ability to forget the setbacks.  
**Translation:** Vocabulary: characteristics: 性格特质

**[6247.28s] English:** The ability to believe in yourself, you know, to believe what you believe and stay  
**Translation:** 

**[6253.62s] English:** Stay true to that belief, um, but you're constantly re-evaluating this combination of  
**Translation:** 

**[6261.20s] English:** Three, four, and five things I think are really important for resilience, and um,...  
**Translation:** 

**[6268.64s] English:** And you know, I'm fortunate that whatever life experiences have led me to this point.  
**Translation:** Vocabulary: resilience: 韧性

**[6275.60s] English:** Kind of, those four or five things. You know, I'm always curious and always learning.  
**Translation:** 

**[6281.22s] English:** From everybody, I'm always asking "what," and because I'm humble about everything.  
**Translation:** Vocabulary: humble: 谦逊

**[6286.94s] English:** I'm always thinking, "Gosh, they did that so nicely; they did that so wonderfully, you know. I wonder...  
**Translation:** 

**[6293.30s] English:** What they're thinking through: how do they, you know? So I'm simulating everyone in a lot of ways.  
**Translation:** Vocabulary: nicely: 做得很好; simulating: 模拟

**[6298.64s] English:** You know, emulating almost everyone I watch; you're so empathetic, right?  
**Translation:** 

**[6303.02s] English:** Towards everything they do that you're observing, and respect and  
**Translation:** Vocabulary: empathetic: 共情的; emulating: 模仿

**[6306.96s] English:** And so, you're constantly learning, and you know you're now one of the wealthiest people on Earth.  
**Translation:** 

**[6314.22s] English:** One of the most successful humans on Earth is it harder to be humble and to be able to  
**Translation:** Vocabulary: wealthiest: 最富有的人

**[6320.88s] English:** Do you feel the effect of money, power, and fame making it harder for you to  
**Translation:** 

**[6328.64s] English:** Sort of be wrong in your own head enough to.  
**Translation:** 

**[6334.00s] English:** Hear out an opinion of somebody else when it disagrees with you, and learn from them.  
**Translation:** 

**[6337.84s] English:** Those kinds of things, um, surprisingly, no, and I would actually go the other way.  
**Translation:** 

**[6346.40s] English:** Because I do so much of my work publicly, when I'm wrong, pretty much everybody sees it.  
**Translation:** 

**[6353.52s] English:** You get humbled, yeah, and when I'm wrong, or  
**Translation:** 

**[6358.64s] English:** When things didn't turn out that way, or  
**Translation:** 

**[6360.00s] English:** Um, you know, I mean, most of the things that I say outside, I'm fairly certain about and the  
**Translation:** 

**[6368.40s] English:** The reason for that is because it's going to impact somebody else, and I want to be quite.  
**Translation:** 

**[6372.70s] English:** Concerned about that, and quite circumspect about it for stuff I'm reasoning.  
**Translation:** Vocabulary: circumspect: 谨慎

**[6378.32s] English:** About inside a meeting, you know, a lot of things could turn out differently, and so but it doesn't.  
**Translation:** 

**[6384.54s] English:** Ever stop me from reasoning the way that I manage and lead? I'm constantly...  
**Translation:** 

**[6390.92s] English:** Reasoning in front of people, and even when I'm talking to you, you can kind of see me kind of.  
**Translation:** 

**[6394.64s] English:** Reasoning through things, and I want to make sure that you understand what I'm saying, not because  
**Translation:** 

**[6398.34s] English:** I told you because I'm so humble about what I'm about to tell you, I kind of show you the steps.  
**Translation:** 

**[6404.80s] English:** That I got there, and then you could decide whether to believe what I said in the end.  
**Translation:** Vocabulary: humble: 谦逊

**[6408.44s] English:** And so, I'm doing that all day long in meetings with all of my employees; I'm constantly reasoning.  
**Translation:** 

**[6414.30s] English:** Through  
**Translation:** 

**[6414.52s] English:** Let me tell you: let me tell you what I see and how I reason through it; it gives everybody...  
**Translation:** 

**[6419.52s] English:** The opportunity to intercept and say, "I disagree with that part." The nice thing about reasoning:  
**Translation:** Vocabulary: intercept: 打断

**[6425.26s] English:** Through things and letting people interact with them is that they don't have to  
**Translation:** 

**[6429.74s] English:** Disagree with your outcome, they can disagree with your reasoning steps, and they could pull me in.  
**Translation:** 

**[6436.22s] English:** Different directions, and then we can reason forward. So we're kind of you know,  
**Translation:** 

**[6444.48s] English:** Collective  
**Translation:** 

**[6444.52s] English:** Path searching method, and it's really fantastic! Yeah, you have this way about you of when you're  
**Translation:** 

**[6452.92s] English:** Explaining stuff, I can feel you actually reasoning on the spot about it with a constant open-mindedness.  
**Translation:** 

**[6459.98s] English:** Where you could I could feel like I could steer your thinking, yeah, and that's really  
**Translation:** 

**[6465.52s] English:** Beautiful that you've been able to maintain that after so many years of success and pain.  
**Translation:** 

**[6469.84s] English:** I think sometimes pain makes you close down a bit.  
**Translation:** 

**[6474.48s] English:** Yeah, and I think you maintain a tolerance for embarrassment, I think it's  
**Translation:** 

**[6480.00s] English:** That's the tolerance.  
**Translation:** 

**[6481.52s] English:** I mean, that's a real thing.  
**Translation:** Vocabulary: tolerance: 忍耐

**[6483.00s] English:** Yeah.  
**Translation:** 

**[6483.50s] English:** There are many years of embarrassing yourself, even in those meetings, knowing that there are people around you who have declared one idea and it was shown to be wrong, and being able to admit it and grow from that.  
**Translation:** 

**[6495.34s] English:** That's not very difficult on a human level.  
**Translation:** 

**[6497.86s] English:** Yeah.  
**Translation:** 

**[6498.22s] English:** Well, you know, they knew I was, they knew that recently my first job was cleaning toilets.  
**Translation:** 

**[6504.32s] English:** So I'm glad you maintain that same spirit of Denny's, um, the way you approach the work.  
**Translation:** 

**[6510.30s] English:** I mean, that was beautiful.  
**Translation:** 

**[6511.26s] English:** Your whole journey, from starting at Denny's, is a beautiful one.  
**Translation:** 

**[6514.72s] English:** Uh, let me ask you about video games.  
**Translation:** 

**[6518.22s] English:** So, I'm a big gaming fan.  
**Translation:** 

**[6520.56s] English:** Yeah.  
**Translation:** 

**[6521.32s] English:** So, I have to say thank you to Nvidia for many years of incredible graphics.  
**Translation:** 

**[6526.92s] English:** Um, by the way, GeForce is still ours to this day.  
**Translation:** 

**[6530.74s] English:** Yeah.  
**Translation:** 

**[6531.14s] English:** Our number one marketing strategy.  
**Translation:** 

**[6535.20s] English:** Right.  
**Translation:** 

**[6535.72s] English:** People learn about Nvidia while they're in their teenage years, and then they go to college and they know who Nvidia is.  
**Translation:** 

**[6542.14s] English:** And then in the beginning, it's just, you know, playing Call of Duty, you know, and Fortnite.  
**Translation:** Vocabulary: fortnite: 一款多人在线战斗游戏

**[6547.24s] English:** And then later, they're using CUDA, and then later, they're using NVIDIA with Blender and Dassault and Autodesk.  
**Translation:** 

**[6556.26s] English:** I mean, I should say—I mentioned to a friend that I'm, uh, talking with you, and he said, "Oh, they make great games.  
**Translation:** Vocabulary: autodesk: 建筑设计软件; blender: 三维建模软件; dassault: 航空航天公司

**[6564.32s] English:** I mean GPUs.  
**Translation:** 

**[6565.22s] English:** Yeah, exactly.  
**Translation:** 

**[6566.54s] English:** Exactly.  
**Translation:** 

**[6567.18s] English:** You know, there's more to it, but yeah.  
**Translation:** 

**[6570.88s] English:** People really love it; it brought a lot of joy to a lot of people.  
**Translation:** 

**[6574.40s] English:** The hardware really brings these worlds to life.  
**Translation:** 

**[6578.36s] English:** Uh, there was some controversy around this with DLSS 5.  
**Translation:** 

**[6583.84s] English:** Yeah.  
**Translation:** Vocabulary: controversy: 争议

**[6584.02s] English:** Can you explain to me the drama around this?  
**Translation:** 

**[6586.12s] English:** Uh, I guess people, gamers online, were concerned that it makes games look like AI slop.  
**Translation:** 

**[6593.68s] English:** Yeah.  
**Translation:** 

**[6594.32s] English:** Uh, what do you think of this drama?  
**Translation:** 

**[6596.28s] English:** Yeah.  
**Translation:** 

**[6597.32s] English:** I think their perspective makes.  
**Translation:** 

**[6599.96s] English:** Yeah.  
**Translation:** 

**[6600.00s] English:** Sense, and I could see where they're coming from, because I don't love AI either myself.  
**Translation:** 

**[6605.76s] English:** You know, all of the AI-generated content increasingly looks similar, and they're all  
**Translation:** 

**[6613.14s] English:** Beautiful, and I'm empathetic toward what they're thinking. That's just not what DLSS 5.  
**Translation:** Vocabulary: empathetic: 同情的

**[6620.32s] English:** Is trying to do. I showed several examples of it, but DLSS 5 is 3D-conditioned, 3D-guided.  
**Translation:** 

**[6630.00s] English:** It's ground-truth, structured data-guided. And so the artist determined the geometry.  
**Translation:** Vocabulary: geometry: 几何结构

**[6636.48s] English:** We are completely truthful to the geometry, maintaining it so in every single frame.  
**Translation:** 

**[6643.90s] English:** It's conditioned by the textures, the artistry of the artist. And so, every single frame,  
**Translation:** Vocabulary: artistry: 艺术家的技巧; truthful: 真实

**[6650.96s] English:** It enhances, but it doesn't change anything. Now, the question is: the question about enhancing.  
**Translation:** 

**[6659.10s] English:** DLSS 5 also...  
**Translation:** Vocabulary: enhances: 提升; enhancing: 提升

**[6660.00s] English:** Because the system is open, you could train your own models to determine, and you could:  
**Translation:** 

**[6667.16s] English:** Even in the future, prompt it. You know, I want it to be a toon shader. I want it to  
**Translation:** Vocabulary: prompt: 提示; shader: 着色器

**[6671.92s] English:** Look like this: So, you can give it even an example, and it would generate.  
**Translation:** 

**[6677.26s] English:** In the style of that, all consistent with the artistry, the style, and the intent of the  
**Translation:** Vocabulary: intent: 意图

**[6684.96s] English:** Artist. And so, all of that is done for the artist.  
**Translation:** 

**[6690.00s] English:** So that they can create something that is more beautiful, but still in the style that.  
**Translation:** 

**[6695.94s] English:** They want. I think that they got the impression that the games are going to come out the way  
**Translation:** 

**[6703.40s] English:** The games are shipped the way they do, and then we're going to post-process it. That's not  
**Translation:** 

**[6709.18s] English:** What DLSS is intended to do, DLSS is integrated with the artist, and so it's about giving  
**Translation:** 

**[6715.94s] English:** The artist is the tool of AI, the tool of generative AI. They could design it. They could design it.  
**Translation:** Vocabulary: generative: 生成式的; integrated: 整合的

**[6720.00s] English:** To use it, you know, I think people are very sensitive to human faces, yeah, and we're now  
**Translation:** 

**[6725.04s] English:** Living in this moment, which I think is a beautiful one, where people are sensitive to.  
**Translation:** 

**[6729.92s] English:** AI_slope, yeah, it puts a mirror to ourselves to help us realize that what we seek are imperfections.  
**Translation:** 

**[6736.48s] English:** We seek graphics that are sometimes not perfect, as they help us understand what we find compelling.  
**Translation:** Vocabulary: compelling: 有吸引力的

**[6742.64s] English:** In the worlds we create, and that's beautiful. And as long as they're tools that help us create those,  
**Translation:** 

**[6747.66s] English:** Worlds, yeah, that's right. It's wonderful, that's right. It's yet another tool, and they want.  
**Translation:** 

**[6751.84s] English:** The generative models can generate the opposite of a photo reel, too.  
**Translation:** 

**[6759.90s] English:** And so, it's just yet another tool I think the gamers might also appreciate that.  
**Translation:** 

**[6766.34s] English:** That, um, in the last couple of years, we introduced skin shaders to the game developers.  
**Translation:** 

**[6776.66s] English:** And many  
**Translation:** Vocabulary: shaders: 着色器

**[6777.64s] English:** Of those games, have skin shaders that include subsurface scattering that make skin look more realistic.  
**Translation:** 

**[6783.98s] English:** Skin like, and so the industries' game developers are looking for more and more tools.  
**Translation:** Vocabulary: scattering: 散射; subsurface: 次表面

**[6790.72s] English:** To express their art, and so this is just yet another tool they get to decide what to use.  
**Translation:** 

**[6796.46s] English:** Ridiculous question, uh. What do you think is the greatest or most influential game ever made?  
**Translation:** Vocabulary: influential: 有影响力的

**[6801.48s] English:** Maybe, from Nvidia's perspective, Doom unquestionably was the start of the 3D revolution.  
**Translation:** 

**[6808.30s] English:** I would say Doom from the intersection of cultural implications as well as the  
**Translation:** Vocabulary: intersection: 交汇点

**[6814.60s] English:** Industry turning a PC into a gaming device was a very important moment, now of course.  
**Translation:** 

**[6820.90s] English:** Flight simulation companies were around before it, but they just didn't have the popularity that  
**Translation:** Vocabulary: popularity: 知名度

**[6826.94s] English:** Doom did not have made the industry turn the PC from a  
**Translation:** 

**[6831.00s] English:** Obviously,  
**Translation:** 

**[6831.48s] English:** An office automation tool into a personal computer for families and gamers, and things like that.  
**Translation:** 

**[6837.36s] English:** So, Doom was really impactful there from an actual  
**Translation:** 

**[6840.00s] English:** From a game technology perspective, I would say Virtual Fighter, and so we're great friends with both of.  
**Translation:** 

**[6846.06s] English:** They, you know, and then there are games—more recently, I mean, Cyberpunk 2077—is really nice for GPU.  
**Translation:** Vocabulary: cyberpunk: 赛博朋克

**[6853.84s] English:** Accelerated graphics, like fully ray-traced graphics, are great. At first, I'm a huge fan.  
**Translation:** 

**[6861.22s] English:** Of Skyrim, uh, Elder Scrolls, and the, you know, it's been released a long time ago, but people  
**Translation:** Vocabulary: accelerated: 加速; scrolls: 卷轴

**[6867.36s] English:** Release mods, and they love these. I mean, it's like a different game, and it just allows me to.  
**Translation:** 

**[6874.96s] English:** Replay the game over and over, and you get it. Makes you realize that you can re-experience.  
**Translation:** 

**[6880.98s] English:** In a totally new way, the world you already love: yeah, so I do that all the time. One of my favorite...  
**Translation:** 

**[6886.66s] English:** Things just walk around Skyrim. We created this thing called RTX mod, huh? Yeah, it's a modding project.  
**Translation:** Vocabulary: modding: 修改模块

**[6892.14s] English:** Tool awesome; it allows the community to inject the latest.  
**Translation:** 

**[6897.36s] English:** Technology into an old game, of course. Like, what makes a great video game is not just graphics.  
**Translation:** Vocabulary: inject: 注入

**[6903.00s] English:** It's also about story and character development, but that's right; beautiful graphics can add to the  
**Translation:** 

**[6909.08s] English:** The immersion, the feeling like it's another place you're transported to.  
**Translation:** Vocabulary: immersion: 沉浸感; transported: 被带入

**[6914.32s] English:** Uh, what's accurate is that you said the AGI timeline fairly accurately.  
**Translation:** 

**[6920.32s] English:** The question rests on your definition of AGI.  
**Translation:** 

**[6925.00s] English:** So, let's  
**Translation:** 

**[6927.36s] English:** Let me ask you about possible timelines here. Let's use this ridiculous definition, perhaps, of what AGI is.  
**Translation:** Vocabulary: timelines: 时间轴

**[6935.04s] English:** But an AI system that's able to essentially do your job—so run, no start, grow, and run a successful...  
**Translation:** 

**[6948.80s] English:** Technology company that's worth at least a billion, or better yet, much more.  
**Translation:** 

**[6957.36s] English:** Dollars more—more than a billion dollars.  
**Translation:** 

**[6960.00s] English:** So, you know how hard it is to do all those components. How far are we away from?  
**Translation:** 

**[6968.36s] English:** That's so we're talking about an open claw that does all the incredibly complex stuff that is required.  
**Translation:** 

**[6977.22s] English:** To innovate, first of all, to find customers to sell to them, to manage, and to build a team.  
**Translation:** Vocabulary: innovate: 创新

**[6984.10s] English:** Of some agents, some humans, all that kind of stuff—is this 5, 10, 15, 20 years away? I think it's now.  
**Translation:** 

**[6992.52s] English:** Do you think we've achieved AGI? Do you think it's possible to run a company with an AI system like this?  
**Translation:** 

**[6997.78s] English:** And the reason for that is: this. You said "a billion," and you didn't say "forever," and so, for example,  
**Translation:** 

**[7004.26s] English:** It is not out of the question that a claw was able to create a web service.  
**Translation:** 

**[7014.10s] English:** Some interesting little app that, all of a sudden, you know, a few billion people used.  
**Translation:** 

**[7023.98s] English:** For 50 cents, and then it went out of business again shortly after. Now, we saw a whole bunch of.  
**Translation:** 

**[7030.46s] English:** Those types of companies during the Internet era, and most of those websites were not much.  
**Translation:** 

**[7036.30s] English:** More sophisticated than what an open claw could generate today, achieving virality and monetization.  
**Translation:** Vocabulary: monetization: 盈利; sophisticated: 复杂; virality: 病毒式传播

**[7043.12s] English:** That virality, yeah.  
**Translation:** 

**[7044.10s] English:** It's just; I don't know what it is, but I couldn't have predicted any of those companies.  
**Translation:** 

**[7048.18s] English:** At the time, either you know, you're gonna get a lot of people excited with that statement.  
**Translation:** 

**[7052.04s] English:** Yeah, no, it's like, what do you mean? I could just launch an agent and make a lot.  
**Translation:** 

**[7058.26s] English:** Of course, money is being well managed right now, as you know when you go to China.  
**Translation:** 

**[7061.92s] English:** Uh, you're gonna see you're gonna see a whole bunch of people getting their  
**Translation:** 

**[7067.82s] English:** Claws to try to go out and look for jobs and, you know, do work, make money, and I'm not.  
**Translation:** 

**[7074.10s] English:** I'm not; I'm not actually. I wouldn't be surprised if some social thing happened or somebody did something.  
**Translation:** Vocabulary: claws: 爪子

**[7080.00s] English:** Created a digital influencer, super cute, or some social application that, you know,  
**Translation:** 

**[7087.44s] English:** Feeds your little Tomagotchi, or something like that. And it becomes out-of-the-blue and  
**Translation:** Vocabulary: influencer: 网络红人; tomagotchi: 电子宠物

**[7093.36s] English:** Instant success. A lot of people use it for a couple of months, and it kind of dies away.  
**Translation:** 

**[7098.84s] English:** Now, the odds of a hundred thousand of those agents building NVIDIA are virtually zero percent.  
**Translation:** Vocabulary: virtually: 几乎

**[7106.88s] English:** And, and then, and then the one part that I will not do, and I want to make sure we  
**Translation:** 

**[7114.56s] English:** All we have to do is recognize that people are really worried about their jobs. And, I just want  
**Translation:** 

**[7122.04s] English:** To remind them that the purpose of your job, and the tasks and the tools that you use to do your  
**Translation:** 

**[7130.86s] English:** Jobs are related, but not the same. I've been doing my job for 33 years. I'm the longest-running tech  
**Translation:** 

**[7136.34s] English:** CEO in the World. I've been doing my job for 33 years. I'm the longest-running tech CEO in the  
**Translation:** 

**[7136.86s] English:** World. I've been doing my job for 34 years, and the tools that I've used to do my job have changed.  
**Translation:** 

**[7141.52s] English:** Continuously in the last 34 years, and sometimes quite dramatically, you know, over the course of  
**Translation:** 

**[7149.72s] English:** A couple of two or three years. And the one story that I really want to make sure  
**Translation:** Vocabulary: dramatically: 剧烈地

**[7154.70s] English:** That's the story everyone hears: the first job that computer scientists said.  
**Translation:** 

**[7161.64s] English:** AI researchers said that what was going to go away was radiology because computer vision was going to  
**Translation:** Vocabulary: radiology: 放射科

**[7166.78s] English:** achieve that. And so, and, and, and, and, and, and, and, and, and, and, and, and, and, and, and,  
**Translation:** 

**[7166.86s] English:** Achieve superhuman levels. And it did. Computer vision was superhuman in 2019, 2020, maybe, maybe a little later.  
**Translation:** 

**[7176.92s] English:** Little bit later, in 2020. Okay. And so it's been a long time since computer vision has been superhuman.  
**Translation:** 

**[7182.84s] English:** And so, the prediction was that radiologists would go away because studying radiology scans was  
**Translation:** Vocabulary: radiologists: 放射科医生

**[7188.76s] English:** Thing of the past. AI will do that. Well, they were absolutely right.  
**Translation:** 

**[7194.78s] English:** Computer vision is completely superhuman.  
**Translation:** 

**[7196.86s] English:** Every radiology platform and package today.  
**Translation:** 

**[7200.00s] English:** Is driven by AI, and yet the number of radiologists grew, so the question is:  
**Translation:** 

**[7207.12s] English:** Why, and we now have a shortage of radiologists in the world, and so one the  
**Translation:** 

**[7213.28s] English:** An alarmist warning went too far and it scared people from pursuing this profession.  
**Translation:** 

**[7221.16s] English:** That is so important to society, and so it did harm. Now, why was it wrong?  
**Translation:** 

**[7227.12s] English:** The reason is because the purpose of a radiologist is to diagnose.  
**Translation:** Vocabulary: diagnose: 确诊; radiologist: 放射科医生

**[7232.28s] English:** Disease, and help patients and doctors diagnose diseases, and because we're able  
**Translation:** 

**[7239.84s] English:** To study scans is so much faster now; you could study more scans, you could.  
**Translation:** 

**[7244.58s] English:** Diagnose better, you could be more patient and see more people faster.  
**Translation:** 

**[7251.54s] English:** The hospitals are making more money; you have more patients in the hospital, you  
**Translation:** 

**[7255.92s] English:** We need more radiologists.  
**Translation:** 

**[7257.12s] English:** I mean, the amazing thing is that it's so obvious this was going to happen.  
**Translation:** 

**[7263.54s] English:** The number of software engineers at Nvidia is going to grow, not decline, and the  
**Translation:** 

**[7268.82s] English:** Reason for that is because the purpose of a software engineer and the task of a  
**Translation:** 

**[7273.14s] English:** Software dreams of coding are related, but not the same. I wanted my software engineers  
**Translation:** 

**[7277.94s] English:** To solve problems, I didn't care how many lines of code they wrote, you know.  
**Translation:** 

**[7282.66s] English:** Their job's purpose didn't change: solving problems, working.  
**Translation:** 

**[7287.10s] English:** As a team, diagnosing problems, evaluating the results, looking for new solutions.  
**Translation:** Vocabulary: diagnosing: 诊断; evaluating: 评估

**[7292.64s] English:** Problems to solve, innovation, connecting the dots — you know, none of that stuff is  
**Translation:** 

**[7298.32s] English:** Going away, do you think it's possible that, let's even take coding, you?  
**Translation:** 

**[7302.48s] English:** Think the number of programmers in the world might increase—that's yes, and  
**Translation:** 

**[7307.64s] English:** The reason for that is: What is the definition of coding?  
**Translation:** Vocabulary: programmers: 程序员

**[7311.66s] English:** I believe that is the definition. Coding, as of today, is simply specifying the  
**Translation:** 

**[7317.10s] English:** Specification, and maybe.  
**Translation:** Vocabulary: specification: 规范; specifying: 制定

**[7320.00s] English:** If you want to be rather directive, you could even give it an architecture for the software in the year.  
**Translation:** 

**[7326.52s] English:** You wanted to write, so the question is: How many people could do that? Describe a specification for.  
**Translation:** 

**[7332.52s] English:** A computer to go tell the computer what to go build; how many people? I think we just went from.  
**Translation:** 

**[7338.56s] English:** 30 million to probably 1 billion, and so every carpenter in the future will be a coder.  
**Translation:** Vocabulary: carpenter: 木匠

**[7347.04s] English:** Except, a carpenter with AI is also an architect; they just increased the value they could.  
**Translation:** 

**[7355.04s] English:** Deliver to the customer, and their artistry just elevated tremendously. I believe that every  
**Translation:** Vocabulary: artistry: 艺术造诣; elevated: 提升; tremendously: 极大程度上

**[7364.04s] English:** An accountant is, you know, also a financial analyst, also a financial advisor, so all of these.  
**Translation:** 

**[7370.48s] English:** Professions have just been elevated, and if I were a carpenter, I would see AI as just  
**Translation:** Vocabulary: analyst: 分析人员; professions: 职业

**[7376.72s] English:** Completely  
**Translation:** 

**[7377.02s] English:** Go berserk, you know, the services I can bring to my clients if I were a plumber — completely go berserk.  
**Translation:** Vocabulary: berserk: 狂躁; plumber: 水管工

**[7384.10s] English:** And the people who are currently programmers and software engineers, I think they're at the  
**Translation:** 

**[7388.98s] English:** Cutting-edge understanding of intuitively communicating with the agents using natural  
**Translation:** Vocabulary: intuitively: 直觉地; programmers: 程序员

**[7396.80s] English:** Language in order to design the best kind of software that's right, so over time they'll.  
**Translation:** 

**[7402.32s] English:** Converge, but I think there's still value in getting.  
**Translation:** Vocabulary: converge: 汇聚

**[7407.02s] English:** Uh, learning how to program is like learning what programming languages are; the old ones...  
**Translation:** 

**[7412.32s] English:** Kind of programming, uh, what are some good practices for programming languages?  
**Translation:** 

**[7417.80s] English:** Design principles for programming languages for large software systems, and the reasons for that.  
**Translation:** 

**[7424.96s] English:** Lex, and you know, I just say for the audience, I think  
**Translation:** 

**[7427.64s] English:** The goal and the artistry of specification.  
**Translation:** 

**[7437.02s] English:** It's going to depend on what problem you're trying to solve.  
**Translation:** Vocabulary: artistry: 技艺; specification: 规范

**[7440.00s] English:** Trying to solve these issues, when I'm thinking about giving the company strategies and formulating corporate  
**Translation:** 

**[7447.60s] English:** Directions and things that we should do, I describe it at a level that is sufficiently  
**Translation:** Vocabulary: sufficiently: 足够地

**[7455.54s] English:** Specific that people generally understand the direction and it's actionable. It's so specific.  
**Translation:** 

**[7464.06s] English:** Enough that they can take action on it, but I under-specify it on purpose so that it enables 43,000.  
**Translation:** 

**[7471.70s] English:** Amazing people to make it even better than I imagined. And so, when I'm working with engineers,  
**Translation:** 

**[7479.30s] English:** When I'm working with people, I think about what problem I'm trying to solve? Who am I working with?  
**Translation:** 

**[7485.84s] English:** With what? And the level of specification, the level of architecture definition,  
**Translation:** 

**[7493.80s] English:** You can't just say, "I'm going to do this," or "I'm going to do that.  
**Translation:** 

**[7494.06s] English:** Relates to that. And so, everyone's going to have to learn how, where in the spectrum of  
**Translation:** 

**[7502.56s] English:** Coding, they want to be. Writing a specification is coding. And so you might decide to be.  
**Translation:** 

**[7507.46s] English:** Quite prescriptive, because there's a very specific outcome you're looking for.  
**Translation:** 

**[7512.36s] English:** You might decide that this is an area you want to be much more exploratory, and so you might.  
**Translation:** 

**[7518.02s] English:** Under-specify and enable you to go back and forth with the AI to even push your own boundaries.  
**Translation:** 

**[7523.80s] English:** Boundaries of creativity. And so, this artistry of where you are in the spectrum,  
**Translation:** Vocabulary: artistry: 艺术造诣

**[7528.80s] English:** This is the future of coding. But just to linger on it outside of coding, I think a lot of people,  
**Translation:** 

**[7534.66s] English:** Rightfully so, they are worried about their jobs and have a lot of anxiety about them.  
**Translation:** Vocabulary: linger: 逗留

**[7540.22s] English:** Especially in the white-collar sector, I don't think any of us know what to do.  
**Translation:** 

**[7549.98s] English:** With tumultuous times that always come when automation and new technologies,...  
**Translation:** Vocabulary: automation: 自动化; tumultuous: 动荡的

**[7553.80s] English:** Technology arrives. And I just, firstly, I think  
**Translation:** 

**[7560.00s] English:** We all need to have compassion and the responsibility to feel, sort of, the burden.  
**Translation:** Vocabulary: burden: 负担; compassion: 同情; firstly: 首先

**[7565.36s] English:** Of what the actual suffering feels like for individuals and families that lose their  
**Translation:** 

**[7570.32s] English:** Job: I think whenever you have transformative technology like that, coming with artificial intelligence,  
**Translation:** 

**[7576.04s] English:** Intelligence, there's going to be a lot of pain. And I don't know what to do about that.  
**Translation:** 

**[7580.20s] English:** Pain. Hopefully, it creates much more opportunities for those same people.  
**Translation:** 

**[7584.14s] English:** For the same kind of job, as the tooling evolves and makes them more productive, it also makes them:  
**Translation:** 

**[7593.72s] English:** More fun. Hopefully, as it does in programming, I've been having so much fun programming; I have  
**Translation:** Vocabulary: evolves: 发展

**[7598.50s] English:** To say, I've never had this much fun. So hopefully it makes their job easier and automates the  
**Translation:** 

**[7603.00s] English:** Boring parts and makes the creative parts, the ones that the human beings are responsible for,  
**Translation:** Vocabulary: automates: 自动化

**[7609.00s] English:** But still, there is going to be a lot of pain and suffering. So, my first recommendation is before  
**Translation:** 

**[7613.98s] English:** And this is how I deal with anxiety. In fact, we just talked about it earlier.  
**Translation:** Vocabulary: recommendation: 建议

**[7619.48s] English:** Enormous anxiety about the future, enormous anxiety about the pressure.  
**Translation:** 

**[7622.74s] English:** Enormous anxiety about uncertainty. I first break it down, and then I'm going to tell myself,...  
**Translation:** 

**[7629.50s] English:** Okay, there are some things you can do something about. There are some things you can't do anything about.  
**Translation:** 

**[7634.22s] English:** About, but for the stuff that you can do something about, let's reason about it and let's go do it.  
**Translation:** 

**[7639.88s] English:** If we were to hire a new college graduate today,  
**Translation:** 

**[7643.18s] English:** And if I have a chance to do it, I'm going to tell myself, "I'm going to tell myself," I'm going to tell  
**Translation:** 

**[7643.96s] English:** A choice between two: one that has no clue what AI is, and one that is an expert in using AI.  
**Translation:** 

**[7654.04s] English:** I would hire the one who's an expert in using AI. If I had an accountant or a marketing person,  
**Translation:** 

**[7661.90s] English:** The one that is an expert in using AI, supply chain, customer service, and a salesperson.  
**Translation:** 

**[7668.20s] English:** Business development: A lawyer, I would hire the one who is an expert in using AI.  
**Translation:** Vocabulary: salesperson: 销售人员

**[7673.96s] English:** And so, I would advise that every college student, every  
**Translation:** 

**[7680.00s] English:** Every teacher should encourage their students to go use AI.  
**Translation:** 

**[7684.34s] English:** Every college student should graduate and be an expert in AI.  
**Translation:** 

**[7688.80s] English:** And, for everyone who is a carpenter or an electrician, go use AI.  
**Translation:** Vocabulary: carpenter: 木匠; electrician: 电工

**[7695.48s] English:** Go see what it can do to transform your current job.  
**Translation:** 

**[7699.80s] English:** Elevate yourself.  
**Translation:** Vocabulary: elevate: 提升

**[7701.00s] English:** If I were a farmer, I would absolutely use AI.  
**Translation:** 

**[7703.84s] English:** If I were a pharmacist, I would use AI.  
**Translation:** Vocabulary: pharmacist: 药师

**[7707.20s] English:** I want to see what it could do to elevate my job.  
**Translation:** 

**[7710.00s] English:** So, that I could be the innovator to revolutionize this industry myself.  
**Translation:** Vocabulary: innovator: 创新者; revolutionize: 彻底改变

**[7716.48s] English:** And so, that would be the first thing that I would do.  
**Translation:** 

**[7718.94s] English:** And then, I would also help them.  
**Translation:** 

**[7723.62s] English:** It is the case that the technology will dislocate and eliminate many tasks.  
**Translation:** 

**[7732.02s] English:** And because it will automate it.  
**Translation:** Vocabulary: automate: 自动化; dislocate: 使脱位

**[7734.02s] English:** If your job is the task,  
**Translation:** 

**[7736.34s] English:** If your job is the task,  
**Translation:** 

**[7738.54s] English:** Then you're very high.  
**Translation:** 

**[7740.00s] English:** You're going to be highly disrupted.  
**Translation:** Vocabulary: disrupted: 被打乱

**[7742.32s] English:** If your job's purpose includes certain tasks,  
**Translation:** 

**[7748.06s] English:** Then it's vital that you go learn how to use AI to automate those tasks.  
**Translation:** 

**[7752.44s] English:** And then, there's the world of spectrum in between.  
**Translation:** 

**[7754.86s] English:** And by the way, the beautiful thing about AI,  
**Translation:** 

**[7757.70s] English:** So, the chatbot versions,  
**Translation:** 

**[7761.02s] English:** Is it that you can break down if you have anxiety?  
**Translation:** Vocabulary: chatbot: 聊天机器人

**[7764.74s] English:** And you can break down the problem by talking to it.  
**Translation:** 

**[7767.68s] English:** Like I've recently, it's really,  
**Translation:** 

**[7770.00s] English:** It's just incredible how much you can think through your life's problems and through,  
**Translation:** 

**[7774.20s] English:** And I don't mean like therapy problems.  
**Translation:** 

**[7775.74s] English:** I mean, like, very practically, okay, I'm worried about my, literally,...  
**Translation:** 

**[7779.72s] English:** I'm worried about my job.  
**Translation:** Vocabulary: practically: 实际上

**[7780.76s] English:** What are the skills?  
**Translation:** 

**[7781.50s] English:** What are the steps I need to take?  
**Translation:** 

**[7782.72s] English:** How do I get better at AI?  
**Translation:** 

**[7783.92s] English:** Everything you just said, you can literally ask:  
**Translation:** 

**[7786.02s] English:** And it's going to give you a point-by-point plan.  
**Translation:** 

**[7789.06s] English:** I mean, it's just a great life coach, period.  
**Translation:** 

**[7791.90s] English:** I don't know how to use AI.  
**Translation:** 

**[7793.10s] English:** And the AI goes, "Well, let me show you.  
**Translation:** 

**[7795.76s] English:** It's very meta, but it's kind of incredible.  
**Translation:** 

**[7799.02s] English:** So, people definitely should.  
**Translation:** 

**[7799.86s] English:** Yeah.  
**Translation:** 

**[7800.00s] English:** You can't just walk up to Excel and say, "I don't know how to use Excel.  
**Translation:** 

**[7802.54s] English:** You're done.  
**Translation:** 

**[7803.10s] English:** I mean, that's really what AI has done for me in all walks of life: it's reduced the initial friction of being a beginner, of using a thing for the first time.  
**Translation:** Vocabulary: friction: 初始障碍

**[7811.64s] English:** I can literally ask about any single thing: what are the first steps I need to take?  
**Translation:** 

**[7816.62s] English:** That's right.  
**Translation:** 

**[7817.04s] English:** And that hand-holding that it does, removing the friction of all the experiences that the world offers—like I mentioned to you offline, you mentioned I'm going to China and Taiwan.  
**Translation:** 

**[7830.44s] English:** So awesome!  
**Translation:** Vocabulary: taiwan: 台湾

**[7831.36s] English:** I'm so excited for you!  
**Translation:** 

**[7832.56s] English:** Where do I go?  
**Translation:** 

**[7834.14s] English:** How do I?  
**Translation:** 

**[7834.78s] English:** All of those questions were immediately answered.  
**Translation:** 

**[7836.78s] English:** It is beautiful.  
**Translation:** 

**[7837.50s] English:** Well, when you go to Taiwan, just ask AI: What are Jensen's favorite restaurants in Taiwan?  
**Translation:** 

**[7844.04s] English:** Yeah.  
**Translation:** 

**[7844.50s] English:** And it will actually tell you.  
**Translation:** 

**[7845.62s] English:** Oh, yeah, yeah.  
**Translation:** 

**[7846.14s] English:** Is it accurate?  
**Translation:** 

**[7846.78s] English:** Yeah, yeah.  
**Translation:** 

**[7847.30s] English:** All right.  
**Translation:** 

**[7847.72s] English:** It's all over Taiwan.  
**Translation:** 

**[7850.16s] English:** Well, you're a rock star over there.  
**Translation:** 

**[7852.78s] English:** And, like we also mentioned offline, maybe our paths will cross, which would be really wonderful.  
**Translation:** 

**[7857.78s] English:** Computex.  
**Translation:** Vocabulary: computex: COMPUTEX展览

**[7858.36s] English:** NVIDIA GTC Taiwan.  
**Translation:** 

**[7860.00s] English:** Do you think there are some things about human nature, or about human consciousness, that is fundamentally non-computational?  
**Translation:** Vocabulary: consciousness: 意识; fundamentally: 本质上

**[7872.62s] English:** Maybe there's something a chip, no matter how powerful, can never replicate?  
**Translation:** 

**[7877.78s] English:** I don't know if the chip will ever get nervous.  
**Translation:** 

**[7879.84s] English:** And that's the conditions by which that causes anxiety or nervousness or whatever emotion.  
**Translation:** 

**[7890.00s] English:** But I believe that AI will be able to recognize those and understand them.  
**Translation:** Vocabulary: nervousness: 紧张感

**[7897.84s] English:** I don't think my chips will feel those.  
**Translation:** 

**[7901.48s] English:** And therefore, how that anxiety, how that feeling, how that excitement, and how all of those feelings manifest in human performance.  
**Translation:** Vocabulary: manifest: 显现

**[7913.84s] English:** For example, extremely amazing human and athletic performance.  
**Translation:** 

**[7918.72s] English:** You know, average or lesser.  
**Translation:** 

**[7920.00s] English:** Than average, that entire spectrum of human performance that comes out of exactly the  
**Translation:** 

**[7927.50s] English:** Same circumstances for different people manifesting in different outcomes, manifesting in different  
**Translation:** Vocabulary: manifesting: 显现; outcomes: 结果

**[7934.28s] English:** Performance, I don't think there's anything that we're building that would suggest that.  
**Translation:** 

**[7942.46s] English:** Two different computers being presented with all of exactly the same context, of course.  
**Translation:** 

**[7949.34s] English:** It would produce statistically different outcomes, but it's not because it felt different.  
**Translation:** 

**[7954.36s] English:** Yeah, the subjective—boy, there's something truly special about the subjective experience.  
**Translation:** Vocabulary: statistically: 统计上

**[7959.56s] English:** That's how we humans feel.  
**Translation:** 

**[7963.02s] English:** Like I mentioned to you, I was pretty nervous talking to you, and that  
**Translation:** 

**[7968.22s] English:** The hope, the fear, the anxiety, and just life itself—the richness of life—and how amazing.  
**Translation:** 

**[7974.58s] English:** Everything is about how deeply we fall in love, how deeply our hearts get broken.  
**Translation:** 

**[7979.34s] English:** How afraid we are of death, and how much pain we feel when our loved ones pass away.  
**Translation:** 

**[7985.22s] English:** All of that, the whole thing.  
**Translation:** 

**[7987.60s] English:** I know it's very hard to think that an AI, or a computational device, being able to do  
**Translation:** 

**[7993.14s] English:** That, but there are so many mysteries about this whole thing that we're yet to uncover.  
**Translation:** Vocabulary: computational: 计算的; uncover: 揭开

**[7997.70s] English:** That I am open to be surprised.  
**Translation:** 

**[8000.98s] English:** I've been surprised a lot over the past few months and years.  
**Translation:** 

**[8005.42s] English:** Scaling can create some incredible miracles in the space of intelligence.  
**Translation:** 

**[8009.34s] English:** It has been truly marvelous to watch, so I'm open to surprises.  
**Translation:** 

**[8014.26s] English:** And it's just really important to break down what intelligence is.  
**Translation:** 

**[8018.56s] English:** That word we use all the time is not a mysterious word.  
**Translation:** 

**[8023.38s] English:** Intelligence has a meaning, and it's a system that, it's something we do that includes  
**Translation:** 

**[8032.30s] English:** Perception, understanding, and reasoning, and the ability to plan.  
**Translation:** Vocabulary: perception: 感觉与知觉

**[8036.10s] English:** And that loop, that loop.  
**Translation:** 

**[8039.34s] English:** That loop is.  
**Translation:** 

**[8040.00s] English:** Is um, the fundamentally what intelligence is: intelligence is not one word that is exactly.  
**Translation:** 

**[8048.48s] English:** Equal to humanity, and that's why I think it's really important to separate the two. We have two words.  
**Translation:** Vocabulary: fundamentally: 本质上

**[8054.42s] English:** For that, I'm not one to over-fantasize or over-romanticize about intelligence.  
**Translation:** 

**[8062.34s] English:** Intelligence is, and people have heard me say it before: I actually think intelligence is a commodity.  
**Translation:** Vocabulary: commodity: 商品

**[8068.34s] English:** I'm surrounded by intelligent people, and I'm surrounded by even more intelligent people.  
**Translation:** 

**[8075.52s] English:** Than I am in each one of the spaces that they're in, and yet I have a role in that circle; it's  
**Translation:** 

**[8083.16s] English:** Actually, kind of interesting, they're more educated than I am; they went to better schools than I did.  
**Translation:** 

**[8090.50s] English:** They are deeper than in any of the fields they are in; all of them. I have 60 of them. They are  
**Translation:** 

**[8097.30s] English:** All of that is superhuman to me.  
**Translation:** 

**[8098.34s] English:** And somehow, I'm sitting in the middle, orchestrating all 60 of them, and so you've got to ask yourself.  
**Translation:** 

**[8104.26s] English:** What is it about a dishwasher that allows it to sit in the middle of such  
**Translation:** 

**[8112.42s] English:** Humans, does that make sense? And so, but that's my point: my point is that intelligence is a functional...  
**Translation:** Vocabulary: dishwasher: 洗碗机; functional: 实用的

**[8120.56s] English:** Thing: Humanity is not just a function, but a much, much bigger concept.  
**Translation:** 

**[8128.34s] English:** And our life experiences, our tolerance for pain, our determination—those are all different.  
**Translation:** Vocabulary: tolerance: 忍耐力

**[8137.10s] English:** Words in intelligence, and so the thing I want to help the audience understand.  
**Translation:** 

**[8142.70s] English:** If I could give them one thing, it's that "intelligence" is a word we've elevated to a very high form.  
**Translation:** Vocabulary: elevated: 提升

**[8149.70s] English:** Over time, the word we should really elevate is "humanity," its character, and all of those things.  
**Translation:** 

**[8158.34s] English:** And that's what I'm trying to do: I'm trying to give them a little bit more of a sense of generosity.  
**Translation:** Vocabulary: elevate: 提升; generosity: 慷慨

**[8160.00s] English:** All of the things that you said just now, I believe are superhuman powers.  
**Translation:** 

**[8161.06s] English:** And I'm trying to give them a little bit more of a sense of generosity.  
**Translation:** 

**[8166.62s] English:** And that now, intelligence is going to be commoditized because we've spoken about it.  
**Translation:** 

**[8170.78s] English:** The most important thing is your education.  
**Translation:** Vocabulary: commoditized: 商品化

**[8173.34s] English:** Now, even when they said the most important thing is your education, when you went to school, there's more than just knowledge that you gained.  
**Translation:** 

**[8182.32s] English:** But unfortunately, our society has put everything into one single word.  
**Translation:** 

**[8187.58s] English:** And life is more than one word.  
**Translation:** 

**[8190.92s] English:** And I'm just telling you: my life would suggest that being lower on the intelligence curve than everybody around me doesn't change the fact that I'm the most successful.  
**Translation:** 

**[8203.02s] English:** And I'm hoping to inspire everybody else: don't let this democratization of intelligence, this commodification of intelligence,...  
**Translation:** 

**[8217.58s] English:** You know, it causes you anxiety, but you should be inspired by that.  
**Translation:** Vocabulary: commodification: 商品化; democratization: 民主化

**[8220.08s] English:** Yeah, I think AI will help us celebrate humanity more.  
**Translation:** 

**[8223.92s] English:** And I am certainly human, and human-first.  
**Translation:** 

**[8230.42s] English:** And I think what makes this world incredible is that humans will always be so.  
**Translation:** 

**[8235.86s] English:** And just AI is this incredible tool that makes us humans more powerful.  
**Translation:** 

**[8240.02s] English:** That's exactly right.  
**Translation:** 

**[8242.10s] English:** So much of the success of NVIDIA and the lives of millions,...  
**Translation:** 

**[8247.58s] English:** The people that I mentioned depend on you.  
**Translation:** 

**[8251.66s] English:** But you're just one human, like we mentioned—mortal, like all of us.  
**Translation:** Vocabulary: mortal: 凡人

**[8256.76s] English:** Do you think about your mortality?  
**Translation:** 

**[8258.82s] English:** Are you afraid of death?  
**Translation:** 

**[8262.28s] English:** I really don't want to die.  
**Translation:** 

**[8265.10s] English:** I have a great life.  
**Translation:** 

**[8266.00s] English:** I've got a great family.  
**Translation:** 

**[8268.64s] English:** I have really important work.  
**Translation:** 

**[8274.28s] English:** This is not a once-in-a-lifetime opportunity.  
**Translation:** 

**[8277.58s] English:** Once in a lifetime.  
**Translation:** 

**[8279.62s] English:** Once in a lifetime.  
**Translation:** 

**[8280.00s] English:** Experience suggests that it has been experienced by many people, just not one person. This is a  
**Translation:** 

**[8287.70s] English:** Once in a humanity experience, what I'm going through. NVIDIA is one of the most consequential.  
**Translation:** 

**[8293.60s] English:** Technology companies in history. We're doing very important work. I take it very seriously.  
**Translation:** Vocabulary: consequential: 有重大影响的

**[8300.76s] English:** And so, some of the things that, of course, are practical things, like how do we think about it?  
**Translation:** 

**[8307.26s] English:** Succession planning? And I'm famous in saying that I don't believe in succession planning.  
**Translation:** 

**[8315.96s] English:** And the reason for that isn't because I'm immortal. The reason for that is because  
**Translation:** 

**[8323.70s] English:** If you're worried about succession planning, if you're worried about all that anxiety surrounding it,  
**Translation:** Vocabulary: immortal: 长生不老

**[8330.42s] English:** Planning, then what should you do about it? Then, you break it all the way back down.  
**Translation:** 

**[8333.76s] English:** The most important thing you should do today, if you care about the future, is [insert action].  
**Translation:** Vocabulary: insert: 插入

**[8337.26s] English:** Of your company, our posts are to pass on knowledge, information, insight, and skills.  
**Translation:** 

**[8344.98s] English:** Experience as often and continuously as you can, which is the reason why I continue to reason.  
**Translation:** 

**[8350.34s] English:** About everything in front of my team. Every single meeting is about a reasoning meeting.  
**Translation:** 

**[8356.22s] English:** Every moment I spend inside or outside a company is about passing on knowledge to people.  
**Translation:** 

**[8362.02s] English:** As fast as I can. Nothing I learn ever sits on my desk.  
**Translation:** 

**[8367.26s] English:** A fraction of a second. I'm passing that information and that knowledge. Oh my gosh.  
**Translation:** 

**[8372.06s] English:** This is cool. Before I even finish learning all of it myself, I've already pointed it to somebody.  
**Translation:** 

**[8377.30s] English:** Else, get on this. This is so cool. You're going to want to learn this. And so, I'm constantly...  
**Translation:** 

**[8383.02s] English:** Passing knowledge, empowering people, elevating the capability of everyone around me, so that  
**Translation:** 

**[8389.72s] English:** The outcome that I seek, that I hope for, is that I die on it.  
**Translation:** Vocabulary: capability: 能力; elevating: 提升; empowering: 赋能

**[8396.98s] English:** I die on it. I die on it. I die on it. I die on it. I die on it. I die on it. I die on it. I die on it. I die on it.  
**Translation:** 

**[8397.26s] English:** I died on the job.  
**Translation:** 

**[8400.00s] English:** I die on the job instantly, yeah, and there's no long periods of suffering, you know.  
**Translation:** 

**[8405.10s] English:** Well, from a fan's perspective, uh, given your extremely  
**Translation:** Vocabulary: instantly: 立刻

**[8411.36s] English:** Um, your enormous positive impact on civilization—of course, I hope you keep going, but also it's  
**Translation:** 

**[8419.48s] English:** Just fun to watch what he's doing; you know, it's just the rate of innovation, and I'm a huge fan.  
**Translation:** 

**[8425.70s] English:** Of engineering, it's so much incredible engineering is continuously being done by NVIDIA; it's just fun!  
**Translation:** 

**[8431.20s] English:** To watch, it's a celebration of humanity, a celebration of great builders, the celebration of great.  
**Translation:** 

**[8435.92s] English:** Engineering, so it represents something special, uh. So I hope you and NVIDIA keep going. What gives?  
**Translation:** 

**[8442.80s] English:** You hope about this whole thing we're got going on about humanity and the future of humanity when  
**Translation:** 

**[8448.66s] English:** You look out and think about the future quite a bit when you look out 10, 20, 50, or 100 years from now.  
**Translation:** 

**[8453.80s] English:** Now, what gives you hope?  
**Translation:** 

**[8455.70s] English:** I've always had great confidence in the kindness of people, uh-huh.  
**Translation:** 

**[8467.00s] English:** Generosity, uh, um, the compassion—the human capacity—I've always been extremely confident in that.  
**Translation:** Vocabulary: compassion: 同情; generosity: 慷慨

**[8478.42s] English:** Sometimes, um,...  
**Translation:** 

**[8480.10s] English:** More so than I should.  
**Translation:** 

**[8484.34s] English:** And  
**Translation:** 

**[8485.70s] English:** And I get taken advantage of, but it doesn't ever cause me not to start with.  
**Translation:** 

**[8492.58s] English:** Always, uh, people want to do good and help others.  
**Translation:** 

**[8502.04s] English:** Vastly, I am proven right.  
**Translation:** Vocabulary: vastly: 广泛地

**[8506.12s] English:** Constantly proven right, and often exceeds my expectations.  
**Translation:** 

**[8515.70s] English:** And so, I have complete confidence in the human capacity.  
**Translation:** Vocabulary: exceeds: 超过

**[8520.00s] English:** I think the things that give me incredible hope are what I see as I extrapolate: as what I see now is possible, and as I extrapolate based on the things we're doing, what will very likely happen.  
**Translation:** 

**[8540.64s] English:** And there are so many things that we want to solve. There are so many problems we want to address. There are so many things we want to build. There are so many good things we want to do, and they're now within our reach—and within the reach of my lifetime. You just can't possibly not be romantic about that, you know what I'm saying?  
**Translation:** Vocabulary: extrapolate: 推断

**[8565.84s] English:** Yeah, what an exciting time to be alive. Truly, truly so.  
**Translation:** 

**[8570.32s] English:** How can you not be romantic about that? The fact that it's a reasonable thing to expect the end of disease. It's a reasonable thing to expect. It's a reasonable thing to expect that pollution will be drastically reduced. It's a reasonable thing to expect that traveling at the speed of light is actually in our future.  
**Translation:** Vocabulary: drastically: 剧烈地

**[8596.72s] English:** And then, you know, not for long distances, but for short distances.  
**Translation:** 

**[8600.32s] English:** You know, people ask me how. Well, first of all, very soon, I'm going to put a humanoid on a spaceship, and it's going to be my humanoid. And we're going to send it out as soon as possible. And it's going to keep improving and enhancing along the flight.  
**Translation:** Vocabulary: enhancing: 提升; humanoid: 类人机器人

**[8616.60s] English:** And then, when it's time, all of my consciousness has already been, you know, so much of my life has been uploaded to the internet. Take all my inbox, take everything that I've done, everything I've said—you know, it's been becoming my AI.  
**Translation:** 

**[8630.32s] English:** And, you know, when the time comes, we'll just send that at the speed of light to catch up with my robot.  
**Translation:** Vocabulary: consciousness: 意识

**[8640.00s] English:** Oh, that's brilliant.  
**Translation:** 

**[8640.88s] English:** I mean, but for me, that's sort of application-focused.  
**Translation:** 

**[8644.50s] English:** But also, for me, the curiosity-maxing perspective,  
**Translation:** 

**[8649.60s] English:** I just can't believe all of those mysteries.  
**Translation:** 

**[8651.42s] English:** There are so many fascinating scientific questions there.  
**Translation:** 

**[8654.72s] English:** Understanding the biological machine is right around the corner.  
**Translation:** 

**[8658.24s] English:** It's not 10 years; it's five years, probably.  
**Translation:** 

**[8660.30s] English:** And the neurobiological machine, the human mind,  
**Translation:** Vocabulary: neurobiological: 神经生物学的

**[8663.06s] English:** And cracking physics and theoretical physics open is so exciting.  
**Translation:** 

**[8666.42s] English:** Explaining consciousness—that would be awesome.  
**Translation:** Vocabulary: cracking: 破解

**[8668.72s] English:** And it's all within our reach.  
**Translation:** 

**[8671.20s] English:** Jensen, thank you so much for everything you've done over the years.  
**Translation:** 

**[8674.22s] English:** Thank you for everything you're doing for the world.  
**Translation:** 

**[8676.26s] English:** Thank you for being who you are.  
**Translation:** 

**[8678.00s] English:** I can tell you're a great human being.  
**Translation:** 

**[8681.48s] English:** And I wish you incredible success this year!  
**Translation:** 

**[8685.84s] English:** I can't wait.  
**Translation:** 

**[8686.36s] English:** As a fan, I can't wait to see what you'll do next.  
**Translation:** 

**[8688.48s] English:** And hopefully, I'll see you in Taiwan.  
**Translation:** 

**[8690.44s] English:** And thank you so much for talking today!  
**Translation:** Vocabulary: taiwan: 台湾

**[8692.74s] English:** Thank you, Lex.  
**Translation:** 

**[8693.38s] English:** I had a great time.  
**Translation:** 

**[8694.78s] English:** And also, if I could just say one more thing.  
**Translation:** 

**[8696.72s] English:** Yes.  
**Translation:** 

**[8697.04s] English:** And thank you for all the interviews.  
**Translation:** 

**[8698.72s] English:** The interviews that you do, the depth, the respect that you go through with,  
**Translation:** 

**[8704.30s] English:** And the research you do to reveal, you know, for all of us,  
**Translation:** 

**[8709.36s] English:** The amazing people that you've interviewed over the years.  
**Translation:** 

**[8712.78s] English:** I've enjoyed them immensely.  
**Translation:** 

**[8715.08s] English:** And as an innovator to have created this long-form, unbelievable,  
**Translation:** Vocabulary: immensely: 非常; innovator: 创新者

**[8722.32s] English:** And yet, you know, it's just captivating.  
**Translation:** 

**[8724.76s] English:** So, anyway, thank you for everything you do.  
**Translation:** Vocabulary: captivating: 引人入胜

**[8726.08s] English:** It means the world.  
**Translation:** 

**[8726.68s] English:** Thank you, Jensen.  
**Translation:** 

**[8727.44s] English:** Thank you, Lex.  
**Translation:** 

**[8729.08s] English:** Thank you for listening to this conversation with Jensen Huang.  
**Translation:** Vocabulary: huang: 黄

**[8732.46s] English:** To support this podcast, please check out our sponsor in the description.  
**Translation:** 

**[8735.90s] English:** Where you can also find links to contact me, ask questions, give feedback, and so on.  
**Translation:** Vocabulary: sponsor: 赞助商

**[8742.24s] English:** And now, let me leave you with some words from Alan Kay.  
**Translation:** 

**[8746.56s] English:** The best way to predict the future is to invent it.  
**Translation:** 

**[8751.10s] English:** Thank you for listening.  
**Translation:** 

**[8752.74s] English:** And I hope to see you next time.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
